---
title: "Actix Web — Middleware"
type: engineering
category: pattern
tags: [actix-web, rust, middleware, cors]
created: 2026-06-06
updated: 2026-06-06
related: [actix-web-error-handling, actix-web-handlers-responders, actix-web-application-state]
first-seen: actix-web-official-docs
sources: [actix-web-official-docs]
---

[[actix-web]]의 **미들웨어**는 요청/응답 처리 파이프라인에 동작을 끼워 넣는 메커니즘이다. 요청 전처리(pre-process), 응답 후처리(post-process), application state 수정, 외부 서비스(redis·logging·session) 접근에 쓰이며, `App`·`scope`·`Resource` 단위로 등록한다.

## 2단계 trait: Transform + Service

미들웨어는 두 개의 trait로 구성된 2단계 구조다.

1. **`Transform`** (factory) — 초기화 단계. 체인의 다음 service를 인자로 받아 실제 미들웨어 service를 만든다.
2. **`Service`** — 실행 단계. 매 요청마다 `call`이 호출된다. 여기서 전처리 → `self.service.call(req)` → 후처리 순으로 흐른다.

각 method에는 default 구현이 있고, 즉시 결과를 반환하거나 future를 반환할 수 있다.

```rust
use std::future::{ready, Ready};

use actix_web::{
    dev::{forward_ready, Service, ServiceRequest, ServiceResponse, Transform},
    Error,
};
use futures_util::future::LocalBoxFuture;

// 1. 미들웨어 초기화: factory가 체인의 다음 service를 인자로 받아 호출됨
// 2. 미들웨어의 call: 일반 요청과 함께 호출됨
pub struct SayHi;

// 미들웨어 factory = `Transform` trait
// `S` - 다음 service의 타입
// `B` - 응답 body의 타입
impl<S, B> Transform<S, ServiceRequest> for SayHi
where
    S: Service<ServiceRequest, Response = ServiceResponse<B>, Error = Error>,
    S::Future: 'static,
    B: 'static,
{
    type Response = ServiceResponse<B>;
    type Error = Error;
    type InitError = ();
    type Transform = SayHiMiddleware<S>;
    type Future = Ready<Result<Self::Transform, Self::InitError>>;

    fn new_transform(&self, service: S) -> Self::Future {
        ready(Ok(SayHiMiddleware { service }))
    }
}

pub struct SayHiMiddleware<S> {
    service: S,
}

impl<S, B> Service<ServiceRequest> for SayHiMiddleware<S>
where
    S: Service<ServiceRequest, Response = ServiceResponse<B>, Error = Error>,
    S::Future: 'static,
    B: 'static,
{
    type Response = ServiceResponse<B>;
    type Error = Error;
    type Future = LocalBoxFuture<'static, Result<Self::Response, Self::Error>>;

    forward_ready!(service);

    fn call(&self, req: ServiceRequest) -> Self::Future {
        println!("Hi from start. You requested: {}", req.path()); // 전처리

        let fut = self.service.call(req);

        Box::pin(async move {
            let res = fut.await?;
            println!("Hi from response"); // 후처리
            Ok(res)
        })
    }
}
```

## 간편한 등록 방법: wrap_fn / from_fn

전체 trait 구현이 부담스러운 경우 짧은 ad-hoc 미들웨어를 함수로 만들 수 있다.

`wrap_fn` — `(req, srv)` 클로저로 즉석 미들웨어:

```rust
use actix_web::{dev::Service as _, web, App};
use futures_util::future::FutureExt;

#[actix_web::main]
async fn main() {
    let app = App::new()
        .wrap_fn(|req, srv| {
            println!("Hi from start. You requested: {}", req.path());
            srv.call(req).map(|res| {
                println!("Hi from response");
                res
            })
        })
        .route("/index.html", web::get().to(|| async { "Hello, middleware!" }));
}
```

`from_fn` — async 함수를 `wrap`과 조합해 미들웨어로:

```rust
use actix_web::{
    body::MessageBody,
    dev::{ServiceRequest, ServiceResponse},
    middleware::{from_fn, Next},
    App, Error,
};

async fn my_middleware(
    req: ServiceRequest,
    next: Next<impl MessageBody>,
) -> Result<ServiceResponse<impl MessageBody>, Error> {
    // 전처리
    next.call(req).await
    // 후처리
}

#[actix_web::main]
async fn main() {
    let app = App::new().wrap(from_fn(my_middleware));
}
```

## ⚠️ 실행 순서는 등록의 역순

> **`wrap()` / `wrap_fn()`을 여러 번 쓰면, 마지막에 등록한 것이 가장 먼저 실행된다.**

즉 미들웨어는 등록 순서의 **역순(opposite order)**으로 실행된다. Logger를 "첫 미들웨어"로 두려면 보통 마지막에 `wrap`한다(또는 가장 바깥쪽에 배치되도록 의도). 스택처럼 쌓인다고 생각하면 된다 — 마지막에 wrap한 것이 가장 바깥 레이어.

## 기본 제공 미들웨어

### Logger
표준 `log` crate 기반 access log. 보통 애플리케이션의 가장 바깥 미들웨어로 등록하며, `env_logger` 같은 logger를 활성화해야 출력이 보인다. → [[actix-web-error-handling]]의 로깅 절과 연계.

```rust
use actix_web::middleware::Logger;
use env_logger::Env;

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    use actix_web::{App, HttpServer};

    env_logger::init_from_env(Env::default().default_filter_or("info"));

    HttpServer::new(|| {
        App::new()
            .wrap(Logger::default())
            .wrap(Logger::new("%a %{User-Agent}i"))
    })
    .bind(("127.0.0.1", 8080))?
    .run()
    .await
}
```

기본 포맷: `%a %t "%r" %s %b "%{Referer}i" "%{User-Agent}i" %T`. 주요 토큰 — `%a` 원격 IP, `%r` 요청 첫 줄, `%s` 상태 코드, `%b` 응답 바이트 수, `%T` 처리 시간(초), `%D` 처리 시간(ms), `%{FOO}i`/`%{FOO}o` 요청/응답 헤더.

### Compress
응답을 자동 압축한다. 클라이언트 `Accept-Encoding`에 맞춰 동작하므로 핸들러는 압축을 신경 쓸 필요가 없다 → [[actix-web-handlers-responders]].

### DefaultHeaders
기본 응답 헤더 설정. 응답에 이미 해당 헤더가 있으면 덮어쓰지 않는다.

```rust
use actix_web::{http::Method, middleware, web, App, HttpResponse, HttpServer};

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new()
            .wrap(middleware::DefaultHeaders::new().add(("X-Version", "0.2")))
            .service(
                web::resource("/test")
                    .route(web::get().to(HttpResponse::Ok))
                    .route(web::method(Method::HEAD).to(HttpResponse::MethodNotAllowed)),
            )
    })
    .bind(("127.0.0.1", 8080))?
    .run()
    .await
}
```

### NormalizePath
trailing slash 등 경로를 정규화해 라우팅 매칭 실패를 줄인다 → [[actix-web-routing]].

### ErrorHandlers
특정 상태 코드에 커스텀 핸들러를 붙여 응답을 가공·교체한다 → [[actix-web-error-handling]].

```rust
use actix_web::middleware::{ErrorHandlerResponse, ErrorHandlers};
use actix_web::{dev, http::{header, StatusCode}, web, App, HttpResponse, HttpServer, Result};

fn add_error_header<B>(mut res: dev::ServiceResponse<B>) -> Result<ErrorHandlerResponse<B>> {
    res.response_mut().headers_mut().insert(
        header::CONTENT_TYPE,
        header::HeaderValue::from_static("Error"),
    );
    Ok(ErrorHandlerResponse::Response(res.map_into_left_body()))
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new()
            .wrap(ErrorHandlers::new().handler(StatusCode::INTERNAL_SERVER_ERROR, add_error_header))
            .service(web::resource("/").route(web::get().to(HttpResponse::InternalServerError)))
    })
    .bind(("127.0.0.1", 8080))?
    .run()
    .await
}
```

### actix-session (세션)
`SessionMiddleware`로 세션을 관리한다. 여러 backend를 지원하며 기본은 cookie backend. `CookieSessionStore`는 cookie 한 개에 담기므로 4000 bytes 미만만 저장 가능(초과 시 500). signed cookie는 클라이언트가 볼 수는 있지만 수정 불가, private cookie는 보기·수정 모두 불가. 데이터 접근은 `Session` extractor → [[actix-web-application-state]] / [[actix-web-handlers-responders]].

```rust
use actix_session::{Session, SessionMiddleware, storage::CookieSessionStore};
use actix_web::{web, App, Error, HttpResponse, HttpServer, cookie::Key};

async fn index(session: Session) -> Result<HttpResponse, Error> {
    if let Some(count) = session.get::<i32>("counter")? {
        session.insert("counter", count + 1)?;
    } else {
        session.insert("counter", 1)?;
    }
    Ok(HttpResponse::Ok().body(format!("Count is {:?}!", session.get::<i32>("counter")?.unwrap())))
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new()
            .wrap(
                SessionMiddleware::builder(CookieSessionStore::default(), Key::from(&[0; 64]))
                    .cookie_secure(false)
                    .build(),
            )
            .service(web::resource("/").to(index))
    })
    .bind(("127.0.0.1", 8080))?
    .run()
    .await
}
```

## CORS (actix-cors)

브라우저 대상 API에서 흔한 미들웨어. 별도 crate `actix-cors`를 쓰며, **"무엇이든 허용"과 "정확히 이 값들만 허용"이 서로 다른 API**라는 점이 핵심이다.

### 단일 프론트엔드 origin 허용 (가장 흔한 프로덕션 형태)

```rust
use actix_cors::Cors;
use actix_web::{http::header, App};

let cors = Cors::default()
    .allowed_origin("https://app.example.com")
    .allowed_methods(vec!["GET", "POST"])
    .allowed_headers(vec![header::AUTHORIZATION, header::CONTENT_TYPE])
    .max_age(3600);

let app = App::new().wrap(cors);
```

여러 origin은 `allowed_origin(...)`을 반복 호출한다. scope에만 적용하려면 `web::scope("/api").wrap(cors)`처럼 scope를 wrap한다 → [[actix-web-routing]].

### 공개 API (credentials 불필요)

```rust
let cors = Cors::default()
    .allow_any_origin()
    .send_wildcard()
    .allow_any_method()
    .allow_any_header();
```

### ⚠️ wildcard와 credentials는 함께 못 쓴다

- `allowed_origin("*")`는 **거부됨** — wildcard는 `allow_any_origin()`을 써야 한다.
- `allow_any_origin()`(임의 origin 수용)과 `send_wildcard()`(응답 헤더를 `Access-Control-Allow-Origin: *`로 보냄)는 **다른 것**이다.
- `supports_credentials()` + `send_wildcard()` 조합은 **startup에서 실패**한다. 쿠키/인증 헤더가 필요하면 wildcard 대신 명시적 origin allowlist를 써라.

```rust
// credentials가 필요하면 명시적 origin 사용
let cors = Cors::default()
    .allowed_origin("https://app.example.com")
    .supports_credentials()
    .allowed_methods(vec!["GET", "POST"])
    .allowed_headers(vec![header::AUTHORIZATION, header::CONTENT_TYPE]);
```

`actix-cors`는 기본으로 `Vary` 헤더를 켠다(CDN·proxy에 CORS 응답이 요청 헤더에 따라 달라질 수 있음을 알림). 캐싱 영향을 완전히 이해하기 전엔 기본값을 유지하라. 정적 설정으로 충분치 않고 요청 데이터·패턴 매칭(예: tenant subdomain)이 필요할 때만 `allowed_origin_fn`을 사용한다.

## When to use
- **공통 횡단 관심사**(logging, 압축, 헤더, 인증, 세션, CORS)는 핸들러가 아니라 미들웨어로.
- 짧은 로직이면 `wrap_fn` / `from_fn`, 상태를 들고 재사용할 미들웨어면 `Transform` + `Service` 직접 구현.
- 에러 응답 본문/헤더를 후처리하려면 `ErrorHandlers` → [[actix-web-error-handling]].

## References
- [[actix-web-official-docs]] — `01.raw/docs/actix-web/middleware.md`, `cors.md`
- [[actix-web]] (hub)
- [[actix-web-error-handling]], [[actix-web-handlers-responders]], [[actix-web-application-state]], [[actix-web-routing]]
