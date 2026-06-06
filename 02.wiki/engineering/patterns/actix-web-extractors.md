---
title: "Actix Web — Extractors (FromRequest)"
type: engineering
category: pattern
tags: [actix-web, rust, extractors, from-request, serde, web]
created: 2026-06-06
updated: 2026-06-06
related: [actix-web-handlers-responders, actix-web-application-state, actix-web-routing, actix-web-error-handling, serde]
first-seen: actix-web-official-docs
sources: [actix-web-official-docs]
---

**추출기(extractor)** 는 요청에서 타입 안전하게 정보를 꺼내는 메커니즘으로, `FromRequest` trait를 구현한 타입을 핸들러 인자로 선언하면 actix-web이 알아서 채워준다. [[actix-web]]는 다양한 내장 추출기를 제공하며, **핸들러 하나당 최대 12개**까지 조합할 수 있다. 핸들러·응답 쪽은 [[actix-web-handlers-responders]] 참고.

## FromRequest 기본 개념

추출기는 핸들러 함수의 인자로 선언되며, 대부분 **인자 위치(순서)는 상관없다**. 단 본문(body)을 읽는 추출기(`Json`, `Form`, `Bytes`, `Payload` 등)는 요청 본문 스트림을 소비하므로, 본문을 읽는 추출기는 **하나만** 성공한다. "JSON으로 파싱하되 실패하면 raw bytes" 같은 폴백이 필요하면 `Either` 추출기를 쓴다(예: `Either<Json<T>, Bytes>`).

경로 동적 세그먼트 2개 + JSON 본문을 한 번에 추출하는 예:

```rust
async fn index(path: web::Path<(String, String)>, json: web::Json<MyInfo>) -> impl Responder {
    let path = path.into_inner();
    format!("{} {} {} {}", path.0, path.1, json.id, json.username)
}
```

## web::Path — 경로 세그먼트

중괄호로 표시한 동적 세그먼트(dynamic segment)를 추출한다. 선언 순서대로 **튜플**로 받거나, `serde::Deserialize`를 구현한 **구조체**로 필드명을 세그먼트명과 매칭해 받는다([[serde]]의 `derive` feature 필요). 라우팅 패턴 정의는 [[actix-web-routing]] 참고.

```rust
use actix_web::{get, web, Result};
use serde::Deserialize;

// 1) 튜플 추출: 선언 순서대로 (u32, String)
#[get("/users/{user_id}/{friend}")]
async fn index_tuple(path: web::Path<(u32, String)>) -> Result<String> {
    let (user_id, friend) = path.into_inner();
    Ok(format!("Welcome {}, user_id {}!", friend, user_id))
}

// 2) serde 구조체 추출: 필드명 = 세그먼트명
#[derive(Deserialize)]
struct Info {
    user_id: u32,
    friend: String,
}

#[get("/users/{user_id}/{friend}")]
async fn index_struct(info: web::Path<Info>) -> Result<String> {
    Ok(format!("Welcome {}, user_id {}!", info.friend, info.user_id))
}
```

> 비-타입세이프 대안으로 `req.match_info().get("friend")` / `.query("user_id")`로 이름으로 직접 조회할 수도 있지만, 파싱 실패가 런타임 panic으로 이어지기 쉬워 권장하지 않는다.

## web::Query<T> — 쿼리 파라미터

쿼리 스트링(`?username=...`)을 구조체로 역직렬화한다. 내부적으로 `serde_urlencoded`를 쓰며, 역직렬화에 실패하면 자동으로 **400 Bad Request**를 반환한다.

```rust
use actix_web::{get, web};
use serde::Deserialize;

#[derive(Deserialize)]
struct Info {
    username: String,
}

#[get("/")]
async fn index(info: web::Query<Info>) -> String {
    format!("Welcome {}!", info.username)
}
```

## web::Json<T> — JSON 본문 (+ JsonConfig)

본문을 `serde::Deserialize` 구조체로 역직렬화한다. 임의의 JSON은 `serde_json::Value`로 받을 수 있다. 기본 크기 제한·에러 핸들러는 **`JsonConfig`** 를 resource의 `.app_data()`에 등록해 바꾼다. 아래 예는 payload를 4kb로 제한하고 커스텀 에러 핸들러를 단다(에러 처리 일반론은 [[actix-web-error-handling]]).

```rust
use actix_web::{error, web, App, HttpResponse, HttpServer, Responder};
use serde::Deserialize;

#[derive(Deserialize)]
struct Info {
    username: String,
}

async fn index(info: web::Json<Info>) -> impl Responder {
    format!("Welcome {}!", info.username)
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        let json_config = web::JsonConfig::default()
            .limit(4096)
            .error_handler(|err, _req| {
                error::InternalError::from_response(err, HttpResponse::Conflict().finish())
                    .into()
            });

        App::new().service(
            web::resource("/")
                .app_data(json_config)
                .route(web::post().to(index)),
        )
    })
    .bind(("127.0.0.1", 8080))?
    .run()
    .await
}
```

> 본문을 메모리에 직접 로드하고 싶다면 `web::Payload`를 받아 `web::BytesMut`에 누적한 뒤 `serde_json::from_slice`로 파싱할 수 있다. 이때 `MAX_SIZE` 검사를 직접 넣어야 한다(`Json<T>`는 자동으로 제한).

## web::Form<T> — URL-encoded 폼

`application/x-www-form-urlencoded` 본문을 `serde::Deserialize` 구조체로 받는다. 콘텐츠 타입이 일치하고 역직렬화에 성공해야만 핸들러가 호출된다. `FormConfig`로 추출 과정을 설정할 수 있다. UrlEncoded 추출은 콘텐츠 타입 불일치, `chunked` 전송, content-length가 256k 초과, payload 에러 종료 시 실패한다.

```rust
use actix_web::{post, web, Result};
use serde::Deserialize;

#[derive(Deserialize)]
struct FormData {
    username: String,
}

#[post("/")]
async fn index(form: web::Form<FormData>) -> Result<String> {
    Ok(format!("Welcome {}!", form.username))
}
```

> 폼이 선택적이거나 잘못된 입력을 직접 처리하려면 `Option<web::Form<FormData>>`로 감싸 핸들러에서 `None`을 체크한다.

## web::Data<T> — 공유 상태 추출

애플리케이션 상태에 **읽기 전용 참조**로 접근한다. 자세한 등록·공유 패턴(`Arc`/atomic, worker별 vs. 전역 상태)은 [[actix-web-application-state]]에서 다룬다.

```rust
use actix_web::{web, App, HttpServer, Responder};
use std::cell::Cell;

#[derive(Clone)]
struct AppState {
    count: Cell<usize>,
}

async fn show_count(data: web::Data<AppState>) -> impl Responder {
    format!("count: {}", data.count.get())
}
```

> gotcha: 핸들러는 비동기로 실행된다. 상태에 `Mutex`/`RwLock` 같은 blocking 동기화 primitive를 쓸 때 critical section이 너무 크거나 그 안에 `.await`가 있으면 안 된다. 필요하면 [[tokio]]의 blocking `Mutex` 가이드를 따른다.

## web::Bytes / web::Payload — raw body·스트리밍

- **`web::Bytes`**: 요청 본문을 `Bytes`로 통째 받는다(타입 없는 raw body).
- **`web::Payload`**: 저수준 본문 스트림. 다른 추출기를 만들거나 청크 단위 스트리밍 처리에 쓴다. `Bytes` 객체의 스트림이라 `.next().await`로 청크를 읽는다.

```rust
use actix_web::{get, web, Error, HttpResponse};
use futures::StreamExt;

#[get("/")]
async fn index(mut body: web::Payload) -> Result<HttpResponse, Error> {
    let mut bytes = web::BytesMut::new();
    while let Some(item) = body.next().await {
        let item = item?;
        println!("Chunk: {:?}", &item);
        bytes.extend_from_slice(&item);
    }
    Ok(HttpResponse::Ok().finish())
}
```

## 본문 처리 메모

- **자동 압축 해제**: 요청에 `Content-Encoding` 헤더가 있으면 actix-web이 자동으로 decompress한다. 지원 코덱은 Brotli / Gzip / Deflate / Zstd. 단 다중 코덱(`br, gzip`)은 미지원.
- **chunked transfer**: 자동 디코딩되며, `web::Payload`는 이미 디코딩(필요시 decompress)된 바이트 스트림을 담는다.
- **multipart**: `multipart/form-data`는 외부 크레이트 [`actix-multipart`](https://crates.io/crates/actix-multipart)로 지원한다.
- `HttpRequest`, `String` 자체도 추출기다(전자는 요청의 다른 부분 접근용, 후자는 본문을 문자열로 변환).

## 언제 무엇을

| 추출기 | 용도 |
|--------|------|
| `web::Path<T>` | URL 동적 세그먼트 (리소스 식별자) |
| `web::Query<T>` | 쿼리 스트링 (필터·페이징) |
| `web::Json<T>` | JSON API 본문 (크기 제한은 `JsonConfig`) |
| `web::Form<T>` | HTML 폼 / urlencoded 본문 |
| `web::Data<T>` | DB 풀·설정 등 공유 상태 → [[actix-web-application-state]] |
| `web::Bytes` / `web::Payload` | raw body·스트리밍·커스텀 추출기 |

## References

- [[actix-web]] — 프레임워크 허브
- [[actix-web-handlers-responders]] — 핸들러가 추출기를 받고 응답을 반환하는 짝
- [[actix-web-application-state]] — `web::Data` 등록·공유 패턴
- [[actix-web-routing]] — 동적 세그먼트 패턴 정의
- [[actix-web-error-handling]] — 추출 실패 시 에러 처리
- [[serde]] — `Deserialize` derive 의존
- [[actix-web-official-docs]] — Extractors, Requests, Getting Started
