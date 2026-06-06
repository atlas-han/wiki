---
title: "Actix Web — Testing"
type: engineering
category: pattern
tags: [actix-web, rust, testing]
created: 2026-06-06
updated: 2026-06-06
related: [actix-web-extractors, actix-web-handlers-responders, actix-web-http-server]
first-seen: actix-web-official-docs
sources: [actix-web-official-docs]
---

[[actix-web]]는 `actix_web::test` 모듈로 통합 테스트(전체 `App` 구동)와 단위 테스트(추출기·미들웨어·responder 직접 검증)를 모두 지원한다. 핵심은 `TestRequest` 빌더로 요청을 만들고, `test::init_service(App)`로 서비스를 초기화한 뒤, `test::call_service`로 호출하고 응답을 검증하는 흐름이다.

## 테스트 도구 구성

- **`TestRequest`** — builder-like 패턴의 요청 빌더. `get()`/`post()`/`default()` 등으로 시작해 `.uri()`, `.insert_header()` 등을 체이닝한다. `.to_request()`로 `Request`를, `.to_http_request()`로 `HttpRequest`를 생성한다.
- **`test::init_service(App)`** — 일반 `App` 빌더를 받아 테스트용 `Service`를 만든다. 실제 HTTP 서버([[actix-web-http-server]])를 띄우지 않고 서비스 레이어를 그대로 구동한다.
- **`test::call_service` / `test::try_call_service`** — 초기화된 서비스에 요청을 보내 `ServiceResponse`를 받는다.
- **`test::read_body` / `test::read_body_json` / `test::call_and_read_body_json`** — 응답 바디를 바이트 또는 역직렬화된 타입으로 읽는다.
- **`#[actix_web::test]`** — async 테스트 함수에 런타임을 붙여주는 매크로. `#[tokio::test]`의 actix 버전.

## 통합 테스트 (전체 App)

`init_service`로 핸들러를 등록한 `App`을 구동하고, `TestRequest`로 요청을 보낸다. 응답의 상태 코드로 성공/실패를 검증한다.

```rust
#[cfg(test)]
mod tests {
    use actix_web::{http::header::ContentType, test, App};

    use super::*;

    #[actix_web::test]
    async fn test_index_get() {
        let app = test::init_service(App::new().service(index)).await;
        let req = test::TestRequest::default()
            .insert_header(ContentType::plaintext())
            .to_request();
        let resp = test::call_service(&app, req).await;
        assert!(resp.status().is_success());
    }

    #[actix_web::test]
    async fn test_index_post() {
        let app = test::init_service(App::new().service(index)).await;
        let req = test::TestRequest::post().uri("/").to_request();
        let resp = test::call_service(&app, req).await;
        assert!(resp.status().is_client_error());
    }
}
```

### 애플리케이션 상태가 필요한 경우

상태를 쓰는 핸들러는 실제 앱과 동일하게 `App`에 `app_data(web::Data::new(...))`로 상태를 붙여 테스트한다 ([[actix-web-application-state]]). 응답을 JSON으로 역직렬화하려면 `call_and_read_body_json`이 편리하다.

```rust
#[actix_web::test]
async fn test_index_get() {
    let app = test::init_service(
        App::new()
            .app_data(web::Data::new(AppState { count: 4 }))
            .service(index),
    )
    .await;
    let req = test::TestRequest::get().uri("/").to_request();
    let resp: AppState = test::call_and_read_body_json(&app, req).await;

    assert_eq!(resp.count, 4);
}
```

## 단위 테스트 (핸들러 직접 호출)

추출기·미들웨어·responder를 개발할 때 유용하다. `TestRequest::...to_http_request()`로 `HttpRequest`를 만들어 핸들러 함수를 직접 `.await` 한다.

> ⚠️ 직접 호출이 가능한 것은 **routing 매크로(`#[get("/")]` 등) 없이 stand-alone으로 정의된 핸들러**뿐이다. 매크로가 붙으면 함수 시그니처가 바뀌어 직접 호출할 수 없으므로 통합 테스트로 검증한다. 핸들러·responder 작성법은 [[actix-web-handlers-responders]] 참고.

```rust
#[cfg(test)]
mod tests {
    use super::*;
    use actix_web::{
        http::{self, header::ContentType},
        test,
    };

    #[actix_web::test]
    async fn test_index_ok() {
        let req = test::TestRequest::default()
            .insert_header(ContentType::plaintext())
            .to_http_request();
        let resp = index(req).await;
        assert_eq!(resp.status(), http::StatusCode::OK);
    }

    #[actix_web::test]
    async fn test_index_not_ok() {
        let req = test::TestRequest::default().to_http_request();
        let resp = index(req).await;
        assert_eq!(resp.status(), http::StatusCode::BAD_REQUEST);
    }
}
```

## 스트리밍 응답 테스트

SSE(Server-Sent Events)처럼 스트림을 생성하는 응답은 `resp.into_body()`로 바디를 꺼낸 뒤 future로 만들어 chunk 단위로 검증하거나, `body::to_bytes`로 전체 페이로드를 한 번에 읽는다.

```rust
#[actix_web::test]
async fn test_stream_full_payload() {
    let app = test::init_service(App::new().route("/", web::get().to(sse))).await;
    let req = test::TestRequest::get().to_request();

    let resp = test::call_service(&app, req).await;
    assert!(resp.status().is_success());

    let body = resp.into_body();
    let bytes = body::to_bytes(body).await;
    assert_eq!(
        bytes.unwrap(),
        web::Bytes::from_static(b"data: 5\n\ndata: 4\n\ndata: 3\n\ndata: 2\n\ndata: 1\n\n")
    );
}
```

chunk 단위 검증은 `pin!(body)` 후 `future::poll_fn(|cx| body.as_mut().poll_next(cx))`로 한 프레임씩 당겨 비교한다.

## 언제 무엇을 쓰나

- **통합 테스트** — 대부분의 엔드포인트 검증. 라우팅([[actix-web-routing]])·추출기([[actix-web-extractors]])·미들웨어가 실제 파이프라인에서 동작하는지 확인할 때.
- **단위 테스트** — 커스텀 추출기/미들웨어/responder 자체의 로직을 격리 검증할 때. 산문에서도 밝히듯 일반 애플리케이션 로직에 대한 단위 테스트의 가치는 제한적이다.

## References

- [[actix-web-official-docs]] — Testing (https://actix.rs/docs/testing)
- [[actix-web]] · [[actix-web-extractors]] · [[actix-web-handlers-responders]] · [[actix-web-http-server]]
