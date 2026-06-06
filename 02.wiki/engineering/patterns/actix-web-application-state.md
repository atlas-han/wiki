---
title: "Actix Web — Application State (web::Data)"
type: engineering
category: pattern
tags: [actix-web, rust, state, web-data, concurrency]
created: 2026-06-06
updated: 2026-06-06
related: [actix-web-http-server, actix-web-extractors, actix-web-routing, actix-web-databases]
first-seen: actix-web-official-docs
sources: [actix-web-official-docs]
---

# Actix Web — Application State (web::Data)

[[actix-web]]에서 모든 핸들러가 공유하는 상태는 `App`에 `app_data()`로 등록하고, 핸들러에서는 `web::Data<T>` 추출기(extractor)로 꺼내 쓴다. 같은 scope 내 모든 route·resource·미들웨어가 같은 상태에 접근한다. 핵심은 **상태를 어디서 생성하느냐**다 — `HttpServer::new()` 클로저 밖에서 만들어 clone 해 넣어야 모든 워커가 같은 인스턴스를 공유한다.

## App과 상태의 기본 구조

`App`은 route·resource·미들웨어를 등록하고, 같은 scope 안에서 공유되는 application state를 저장한다. 상태 타입은 임의의 struct이며, `web::Data<T>` 추출기로 핸들러 인자에 주입된다.

```rust
use actix_web::{get, web, App, HttpServer};

// This struct represents state
struct AppState {
    app_name: String,
}

#[get("/")]
async fn index(data: web::Data<AppState>) -> String {
    let app_name = &data.app_name; // <- get app_name
    format!("Hello {app_name}!") // <- response with app_name
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new()
            .app_data(web::Data::new(AppState {
                app_name: String::from("Actix Web"),
            }))
            .service(index)
    })
    .bind(("127.0.0.1", 8080))?
    .run()
    .await
}
```

상태 타입은 몇 개든 등록할 수 있다. `web::Data<T>`는 내부적으로 `Arc<T>`를 쓰므로 clone은 저렴하다(참조 카운트 증가).

## ⚠️ 핵심 함정: 워커마다 별도 상태 vs. 전역 공유

`HttpServer`는 application **인스턴스가 아니라 application factory(클로저)** 를 받는다. 워커 스레드마다 이 클로저를 **한 번씩 호출**해 별도의 `App`을 만든다(→ [[actix-web-http-server]]). 따라서 클로저 **안**에서 `web::Data::new()`를 호출하면 워커 수만큼 서로 다른 상태가 생긴다.

전역 공유 상태를 원하면 **클로저 밖에서** `web::Data`를 만들고 클로저 안으로 `move`시킨 뒤 `.clone()` 해서 등록한다. `Arc`가 이중으로 생기는 것을 피하려면 등록 전에 `web::Data`를 먼저 만들어야 한다.

```rust
use actix_web::{web, App, HttpServer};
use std::sync::Mutex;

struct AppStateWithCounter {
    counter: Mutex<i32>, // <- Mutex is necessary to mutate safely across threads
}

async fn index(data: web::Data<AppStateWithCounter>) -> String {
    let mut counter = data.counter.lock().unwrap(); // <- get counter's MutexGuard
    *counter += 1; // <- access counter inside MutexGuard

    format!("Request number: {counter}") // <- response with count
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    // Note: web::Data created _outside_ HttpServer::new closure
    let counter = web::Data::new(AppStateWithCounter {
        counter: Mutex::new(0),
    });

    HttpServer::new(move || {
        // move counter into the closure
        App::new()
            .app_data(counter.clone()) // <- register the created data
            .route("/", web::get().to(index))
    })
    .bind(("127.0.0.1", 8080))?
    .run()
    .await
}
```

문서의 key takeaway:

- `HttpServer::new`에 넘긴 클로저 **안**에서 초기화한 상태는 워커 스레드에 local이며, 수정 시 워커 간 값이 어긋날 수 있다(de-synced).
- **전역 공유 상태**를 얻으려면 반드시 클로저 **밖**에서 생성해 move/clone 해 넣어야 한다.

## 가변 상태: Mutex / RwLock / Atomic

워커 팩토리는 `Send` + `Sync`여야 하므로, 공유되는 가변 상태는 스레드 안전한 래퍼로 감싼다.

- `Mutex<T>`: 단순 배타 락. 위 카운터 예시처럼 가장 기본.
- `RwLock<T>`: 읽기가 압도적으로 많을 때 non-exclusive 락으로 비용 절감.
- `Atomic*` (예: `AtomicUsize`): 락 자체가 없는 가장 빠른 경로. 단순 카운터/플래그에 적합.

> 문서 경고: 공유·동기화를 도입하면 락 비용이 의도치 않게 성능을 깎는다. 가장 빠른 구현은 보통 **아예 락이 없는** 형태다. 가능하면 `RwLock` 또는 atomic으로 락 경합을 줄여라.

## App::configure() — 설정 모듈화

`App`과 `web::Scope` 모두 `configure(fn)`을 제공한다. resource·route·data 설정을 다른 모듈이나 라이브러리로 분리해 재사용할 수 있다. 인자로 받는 `&mut web::ServiceConfig`는 각자 자신의 `data`, `routes`, `services`를 가질 수 있다.

```rust
use actix_web::{web, App, HttpResponse, HttpServer};

// this function could be located in a different module
fn scoped_config(cfg: &mut web::ServiceConfig) {
    cfg.service(
        web::resource("/test")
            .route(web::get().to(|| async { HttpResponse::Ok().body("test") }))
            .route(web::head().to(HttpResponse::MethodNotAllowed)),
    );
}

fn config(cfg: &mut web::ServiceConfig) {
    cfg.service(
        web::resource("/app")
            .route(web::get().to(|| async { HttpResponse::Ok().body("app") }))
            .route(web::head().to(HttpResponse::MethodNotAllowed)),
    );
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new()
            .configure(config)
            .service(web::scope("/api").configure(scoped_config))
            .route("/", web::get().to(|| async { HttpResponse::Ok().body("/") }))
    })
    .bind(("127.0.0.1", 8080))?
    .run()
    .await
}
```

위 결과는 `/ -> "/"`, `/app -> "app"`, `/api/test -> "test"`.

## web::scope() — 라우트 그룹화

`web::scope("/prefix")`는 그 안에 등록된 모든 resource 패턴에 공통 prefix를 붙이는 namespace다. scope `/app`은 `/app`, `/app/`, `/app/test`에는 매칭되지만 `/application`에는 매칭되지 않는다. 스코프별로 별도의 state(`app_data`)와 guard(예: virtual hosting의 `guard::Host`)를 둘 수 있다. 자세한 라우팅 규칙은 → [[actix-web-routing]].

## 실전 패턴: DB 풀을 상태로

가장 흔한 용례는 데이터베이스 connection pool을 `web::Data`로 공유하는 것이다. 풀은 클로저 **밖**에서 한 번 생성해 clone 해 넣고, 핸들러에서 `web::Data<Pool>`로 받는다. 구체적인 예시는 → [[actix-web-databases]]. 핸들러/추출기 일반론은 → [[actix-web-extractors]].

## 언제 무엇을 쓰나

- 읽기 전용 설정·이름·클라이언트 핸들 → `web::Data<T>` 그대로 (불변, 락 불필요).
- 공유 가변 카운터/캐시 → `web::Data<Mutex<T>>` 또는 `RwLock<T>`.
- 단순 수치/플래그 → `web::Data<AtomicUsize>` 등 atomic.
- 워커마다 독립적이어도 되는 상태 → 클로저 **안**에서 생성(공유 비용 없음).

## References

- [[actix-web-official-docs]] — Application (`app_data`, `web::Data`, Shared Mutable State, Configure, Scope)
- 워커/멀티스레딩 모델: [[actix-web-http-server]]
- 라우트 그룹화·매칭: [[actix-web-routing]]
- DB 풀 공유: [[actix-web-databases]]
- 추출기: [[actix-web-extractors]]
