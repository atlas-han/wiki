---
title: "Actix Web — Error Handling (ResponseError)"
type: engineering
category: pattern
tags: [actix-web, rust, error-handling]
created: 2026-06-06
updated: 2026-06-06
related: [actix-web-handlers-responders, actix-web-middleware, actix-web-extractors]
first-seen: actix-web-official-docs
sources: [actix-web-official-docs]
---

[[actix-web]]은 자체 `actix_web::error::Error` 타입과 `ResponseError` trait으로 핸들러 에러를 처리한다. 핸들러가 `ResponseError`를 구현한 에러를 `Result`로 반환하면, actix-web이 그 에러를 대응하는 `StatusCode`의 HTTP 응답으로 자동 렌더링한다(기본은 500).

## ResponseError trait

핵심은 두 method다. 커스텀 에러 타입에 이를 구현하면 핸들러에서 `?` 연산자로 자동 변환되어 그대로 HTTP 응답이 된다.

```rust
pub trait ResponseError {
    fn error_response(&self) -> HttpResponse<BoxBody>;
    fn status_code(&self) -> StatusCode;
}
```

`Responder`가 `Result`를 응답으로 강제 변환하는 부분의 시그니처는 다음과 같다 — `E`가 `Into<Error>`면 `Result<T, E>`가 곧 Responder가 된다 → [[actix-web-handlers-responders]].

```rust
impl<T: Responder, E: Into<Error>> Responder for Result<T, E>
```

actix-web은 흔한 non-actix 에러에 대한 `ResponseError` 구현을 기본 제공한다. 예를 들어 핸들러가 `io::Error`를 반환하면 자동으로 `HttpInternalServerError`로 변환된다.

```rust
use std::io;
use actix_files::NamedFile;

fn index(_req: HttpRequest) -> io::Result<NamedFile> {
    Ok(NamedFile::open("static/index.html")?) // io::Error -> 500 자동 변환
}
```

## 기본 구현으로 시작하기 (derive_more / thiserror)

`Display` + `Error`만 derive하고 `ResponseError`를 빈 impl로 두면, default `error_response()`가 500을 렌더링한다. `Display` 구현에는 `derive_more`(아래 예시) 또는 `thiserror`를 쓴다.

```rust
use actix_web::{error, Result};
use derive_more::derive::{Display, Error};

#[derive(Debug, Display, Error)]
#[display("my error: {name}")]
struct MyError {
    name: &'static str,
}

// error_response()는 default 구현 사용 -> 500
impl error::ResponseError for MyError {}

async fn index() -> Result<&'static str, MyError> {
    Err(MyError { name: "test" })
}
```

## 상태 코드별 응답 매핑

`status_code()`로 variant마다 적절한 코드를 돌려주고, `error_response()`로 본문·헤더를 구성하면 의미 있는 에러 응답이 된다.

```rust
use actix_web::{
    error, get,
    http::{header::ContentType, StatusCode},
    App, HttpResponse,
};
use derive_more::derive::{Display, Error};

#[derive(Debug, Display, Error)]
enum MyError {
    #[display("internal error")]
    InternalError,

    #[display("bad request")]
    BadClientData,

    #[display("timeout")]
    Timeout,
}

impl error::ResponseError for MyError {
    fn error_response(&self) -> HttpResponse {
        HttpResponse::build(self.status_code())
            .insert_header(ContentType::html())
            .body(self.to_string())
    }

    fn status_code(&self) -> StatusCode {
        match *self {
            MyError::InternalError => StatusCode::INTERNAL_SERVER_ERROR,
            MyError::BadClientData => StatusCode::BAD_REQUEST,
            MyError::Timeout => StatusCode::GATEWAY_TIMEOUT,
        }
    }
}

#[get("/")]
async fn index() -> Result<&'static str, MyError> {
    Err(MyError::BadClientData) // -> 400, body "bad request"
}
```

## Error 헬퍼 함수

`ResponseError`를 구현하지 않은 에러를 즉석에서 특정 HTTP 코드로 바꿀 때 `error::ErrorBadRequest` 등 헬퍼를 `map_err`와 함께 쓴다(다른 헬퍼: `ErrorInternalServerError`, `ErrorNotFound` 등 `error` 모듈 참조).

```rust
use actix_web::{error, get};

#[derive(Debug)]
struct MyError {
    name: &'static str,
}

#[get("/")]
async fn index() -> actix_web::Result<String> {
    let result = Err(MyError { name: "test error" });
    result.map_err(|err| error::ErrorBadRequest(err.name)) // -> 400
}
```

## ⚠️ 사용자 노출 메시지 vs 내부 로깅 분리

에러를 **사용자 대상(user-facing)**과 **내부(internal)** 두 부류로 나누는 것이 권장 패턴이다. validation 에러처럼 사용자가 읽어도 되는 메시지는 `#[display(...)]`에 그대로 노출하고, DB 다운·템플릿 렌더 실패 같은 내부 실패는 구체 내용을 숨긴 일반 메시지로 매핑한다.

```rust
use actix_web::{
    error, get,
    http::{header::ContentType, StatusCode},
    HttpResponse,
};
use derive_more::derive::{Display, Error};

#[derive(Debug, Display, Error)]
enum UserError {
    // 내부 원인은 숨기고 일반화된 메시지만 노출
    #[display("An internal error occurred. Please try again later.")]
    InternalError,
}

impl error::ResponseError for UserError {
    fn error_response(&self) -> HttpResponse {
        HttpResponse::build(self.status_code())
            .insert_header(ContentType::html())
            .body(self.to_string())
    }
    fn status_code(&self) -> StatusCode {
        match *self {
            UserError::InternalError => StatusCode::INTERNAL_SERVER_ERROR,
        }
    }
}

#[get("/")]
async fn index() -> Result<&'static str, UserError> {
    do_thing_that_fails().map_err(|_e| UserError::InternalError)?; // 원인은 로깅, 사용자엔 일반 메시지
    Ok("success!")
}
```

이렇게 나눠두면 애플리케이션 내부에서 던진 에러를 사용자에게 실수로 노출하는 일을 막을 수 있다.

## 로깅 (log / env_logger)

actix는 모든 에러를 `WARN` 레벨로 로깅한다. 로그 레벨이 `DEBUG`이고 `RUST_BACKTRACE`가 켜져 있으면 backtrace도 함께 남는다.

```shell
$ RUST_BACKTRACE=1 RUST_LOG=actix_web=debug cargo run
```

`log`/`env_logger`와 [[actix-web-middleware]]의 `Logger`를 함께 쓰는 기본 예시:

```rust
use actix_web::{error, get, middleware::Logger, App, HttpServer, Result};
use derive_more::derive::{Display, Error};
use log::info;

#[derive(Debug, Display, Error)]
#[display("my error: {name}")]
pub struct MyError {
    name: &'static str,
}

impl error::ResponseError for MyError {}

#[get("/")]
async fn index() -> Result<&'static str, MyError> {
    let err = MyError { name: "test error" };
    info!("{}", err); // 내부 로깅
    Err(err)
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    env_logger::init();
    HttpServer::new(|| {
        App::new().wrap(Logger::default()).service(index)
    })
    .bind(("127.0.0.1", 8080))?
    .run()
    .await
}
```

## 관련 흐름
- 핸들러 반환값이 어떻게 응답이 되는가 → [[actix-web-handlers-responders]]
- 추출 실패(잘못된 path/query/JSON)도 에러로 변환됨 → [[actix-web-extractors]]
- 에러 응답을 상태 코드 단위로 후처리·가공 → `ErrorHandlers` 미들웨어 → [[actix-web-middleware]]

## When to use
- 도메인 에러를 enum 하나로 모으고 `ResponseError`를 구현해 `?`만으로 HTTP 응답이 나오게 하라.
- 사용자에게 보여줄 메시지와 내부 디버깅 정보를 의도적으로 분리하라.
- 일회성 변환은 `error::ErrorXxx` 헬퍼 + `map_err`로 충분하다.

## References
- [[actix-web-official-docs]] — `01.raw/docs/actix-web/errors.md`
- [[actix-web]] (hub)
- [[actix-web-handlers-responders]], [[actix-web-middleware]], [[actix-web-extractors]]
