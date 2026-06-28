---
title: "Actix Web — Handlers & Responder"
type: engineering
category: pattern
tags: [actix-web, rust, handlers, responder, http-response, serde]
created: 2026-06-06
updated: 2026-06-27
related: [actix-web-extractors, actix-web-error-handling, actix-web-middleware, serde, design-pattern-strategy, design-pattern-builder]
first-seen: actix-web-official-docs
sources: [actix-web-official-docs]
---

**핸들러(handler)** 는 0개 이상의 추출기(`impl FromRequest`)를 인자로 받아 **`Responder`를 구현한 타입**(`impl Responder`)을 반환하는 async 함수다. 처리는 2단계로 일어난다: 먼저 핸들러가 호출되어 `Responder` 객체를 반환하고, 그 객체의 `respond_to()`가 호출되어 `HttpResponse` 또는 `Error`로 변환된다. 추출기 쪽은 [[actix-web-extractors]] 참고. 전체 프레임워크는 [[actix-web]].

## 기본 Responder 구현

actix-web은 표준 타입들에 `Responder`를 기본 제공한다: `&'static str`, `String`, `HttpResponse`, `web::Json<T>`, `web::Bytes` 등. 따라서 단순 핸들러는 이들을 그대로 반환하면 된다.

```rust
async fn index_str(_req: HttpRequest) -> &'static str {
    "Hello world!"
}

async fn index_string(_req: HttpRequest) -> String {
    "Hello world!".to_owned()
}

// 복잡한 타입이 섞이면 impl Responder 로 반환 타입을 단일화
async fn index_bytes(_req: HttpRequest) -> impl Responder {
    web::Bytes::from_static(b"Hello world!")
}
```

## 커스텀 타입에 Responder 구현

핸들러에서 도메인 타입을 **직접** 반환하려면 그 타입에 `Responder`를 구현한다. `type Body`를 지정하고 `respond_to(self, &HttpRequest) -> HttpResponse<Self::Body>`를 작성한다. 본문 타입이 정해지지 않거나 여러 분기를 합칠 때는 `BoxBody`를 쓴다. 아래는 구조체를 `application/json` 응답으로 직렬화하는 예([[serde]]의 `Serialize` 필요).

```rust
use actix_web::{
    body::BoxBody, http::header::ContentType, HttpRequest, HttpResponse, Responder,
};
use serde::Serialize;

#[derive(Serialize)]
struct MyObj {
    name: &'static str,
}

impl Responder for MyObj {
    type Body = BoxBody;

    fn respond_to(self, _req: &HttpRequest) -> HttpResponse<Self::Body> {
        let body = serde_json::to_string(&self).unwrap();

        HttpResponse::Ok()
            .content_type(ContentType::json())
            .body(body)
    }
}

async fn index() -> impl Responder {
    MyObj { name: "user" }
}
```

> 실전 팁: 단순 JSON 응답이라면 커스텀 `Responder`를 직접 구현하기보다 `web::Json(obj)`를 반환하는 편이 짧고 의도가 명확하다. 커스텀 구현은 헤더·status·body를 타입마다 정교하게 통제해야 할 때 쓴다.

## HttpResponseBuilder — 빌더 패턴

`HttpResponse::Ok()`, `BadRequest()` 등은 `HttpResponseBuilder`를 반환한다. `.content_type()`, `.insert_header()` 등으로 체이닝한 뒤 `.body()` / `.finish()` / `.json()`으로 마무리해 `HttpResponse`를 만든다.

```rust
use actix_web::{http::header::ContentType, HttpResponse};

async fn index() -> HttpResponse {
    HttpResponse::Ok()
        .content_type(ContentType::plaintext())
        .insert_header(("X-Hdr", "sample"))
        .body("data")
}
```

> gotcha: `.body` / `.finish` / `.json` 같은 finalize 메서드를 **같은 빌더에 두 번** 호출하면 panic한다. 빌더는 한 번만 마무리할 것.

## web::Json<T> 응답

`Serialize` 구조체를 `web::Json<T>`로 감싸 반환하면 well-formed JSON 응답이 된다. `HttpResponse`에 `.json()`을 직접 호출하는 것보다, 반환 타입만으로 "이 핸들러는 JSON을 돌려준다"가 드러나는 장점이 있다.

```rust
use actix_web::{get, web, Responder, Result};
use serde::Serialize;

#[derive(Serialize)]
struct MyObj {
    name: String,
}

#[get("/a/{name}")]
async fn index(name: web::Path<String>) -> Result<impl Responder> {
    let obj = MyObj { name: name.to_string() };
    Ok(web::Json(obj))
}
```

## Either — 분기 응답

서로 다른 두 응답 타입을 하나로 합칠 때 `Either<L, R>`를 쓴다. 에러 분기, 동기/비동기 응답 혼합 등에 유용하다.

```rust
use actix_web::{Either, Error, HttpResponse};

type RegisterResult = Either<HttpResponse, Result<&'static str, Error>>;

async fn index() -> RegisterResult {
    if is_a_variant() {
        Either::Left(HttpResponse::BadRequest().body("Bad data"))
    } else {
        Either::Right(Ok("Hello!"))
    }
}
```

> 추출기 쪽에서도 `Either<Json<T>, Bytes>`처럼 폴백 추출에 쓰인다([[actix-web-extractors]]).

## 스트리밍 응답 본문

응답 본문을 비동기로 생성하려면 본문이 `Stream<Item = Result<Bytes, Error>>`를 구현해야 한다. 빌더의 `.streaming()`에 스트림을 넘긴다. 대용량/실시간 응답에 적합하다.

```rust
use actix_web::{get, web, Error, HttpResponse};
use futures::{future::ok, stream::once};

#[get("/stream")]
async fn stream() -> HttpResponse {
    let body = once(ok::<_, Error>(web::Bytes::from_static(b"test")));

    HttpResponse::Ok()
        .content_type("application/json")
        .streaming(body)
}
```

## 자동 압축 (Compress 미들웨어)

응답 압축은 핸들러가 아니라 **`Compress` 미들웨어**가 담당한다. `App::wrap(middleware::Compress::default())`로 등록하면 요청의 `Accept-Encoding`에 맞춰 자동 협상 압축한다(`ContentEncoding::Auto` 기본). 지원 코덱은 Brotli / Gzip / Deflate / Identity. 미들웨어 전반은 [[actix-web-middleware]] 참고.

```rust
use actix_web::{get, middleware, App, HttpResponse, HttpServer};

#[get("/")]
async fn index() -> HttpResponse {
    HttpResponse::Ok().body("data")
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new()
            .wrap(middleware::Compress::default())
            .service(index)
    })
    .bind(("127.0.0.1", 8080))?
    .run()
    .await
}
```

> 특정 핸들러에서 압축을 끄려면 응답에 `ContentEncoding::Identity` 헤더를 넣는다. 이미 압축된 에셋을 서빙할 때는 `ContentEncoding::Gzip` 등을 직접 설정해 미들웨어를 우회한다.

## 언제 무엇을

| 패턴 | 용도 |
|------|------|
| `&str` / `String` 반환 | 단순 텍스트 응답 |
| `web::Json<T>` 반환 | JSON API (의도가 타입에 드러남) |
| `impl Responder` 커스텀 | 도메인 타입을 status/헤더와 함께 직접 반환 |
| `HttpResponse::*().build()` | status·헤더를 세밀히 통제 |
| `Either<L, R>` | 분기마다 응답 타입이 다를 때 |
| `.streaming()` | 대용량·실시간 본문 |

## 디자인 패턴 관점

`Responder` trait은 **[[design-pattern-strategy|전략]]** 패턴이다 — `respond_to(self, &HttpRequest) -> HttpResponse`라는 공통 인터페이스를 `&str`·`String`·`web::Json<T>`·커스텀 타입이 *각자 다른 알고리즘*으로 구현하고, 프레임워크(Context)는 반환 타입이 무엇인지 모른 채 균일하게 `respond_to()`만 호출한다. 핸들러의 반환 타입을 바꾸는 것이 곧 응답 변환 전략을 교체하는 것이다.

응답 자체를 조립하는 `HttpResponse::Ok().content_type(...).insert_header(...).body(...)` 체인은 이 페이지가 이미 "빌더 패턴"이라 부른 그대로 **[[design-pattern-builder|빌더]]** 다 — 복잡한 `HttpResponse`를 단계별 메서드로 구성하고 `.body()`/`.finish()`로 마무리한다(한 번만 finalize).

## References

- [[actix-web]] — 프레임워크 허브
- [[design-pattern-strategy]] (`Responder`) · [[design-pattern-builder]] (`HttpResponseBuilder`) — 디자인 패턴 대응
- [[actix-web-extractors]] — 핸들러가 받는 추출기 (`FromRequest`)
- [[actix-web-error-handling]] — `respond_to`가 반환하는 `Error` 처리
- [[actix-web-middleware]] — `Compress` 등 미들웨어
- [[serde]] — `Serialize` derive 의존
- [[actix-web-official-docs]] — Handlers, Responses
