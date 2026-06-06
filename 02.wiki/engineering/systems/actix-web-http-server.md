---
title: "Actix Web — HttpServer & Worker Model"
type: engineering
category: system
tags: [actix-web, rust, http-server, worker-model, tls, http2, graceful-shutdown]
created: 2026-06-06
updated: 2026-06-06
related: [actix-web-application-state, actix-web-connection-lifecycle, actix-web-handlers-responders, tokio]
first-seen: actix-web-official-docs
sources: [actix-web-official-docs]
---

`HttpServer`는 [[actix-web]]의 HTTP 요청 처리 진입점이다. **애플리케이션 팩토리**(`App`을 만드는 클로저)를 받아, 물리 CPU 코어 수만큼 **워커 스레드**를 spawn하고 각 워커에 `App` 복제본을 하나씩 건넨다. 소켓에 `bind()`한 뒤 `run()`으로 `Server` 핸들을 얻어 `await`하면 종료 시그널이 올 때까지 요청을 처리한다.

## 기본 구동

팩토리는 `Send + Sync`여야 한다(워커 스레드로 옮겨지므로). 반면 각 워커가 갖는 **애플리케이션 상태는 `Send`/`Sync`일 필요가 없다** — 워커끼리 공유되지 않기 때문이다.

```rust
use actix_web::{web, App, HttpResponse, HttpServer};

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| App::new().route("/", web::get().to(HttpResponse::Ok)))
        .bind(("127.0.0.1", 8080))?
        .run()
        .await
}
```

## 워커 모델 (멀티스레딩)

워커 수는 기본값이 물리 CPU 코어 수이며 `workers()`로 조정한다. 각 워커는 **독립된 `App` 인스턴스**를 받아 자기 복제본의 상태를 락 없이 자유롭게 다룬다.

```rust
HttpServer::new(|| App::new().route("/", web::get().to(HttpResponse::Ok)))
    .workers(4) // <- 워커 4개 기동
    .bind(("127.0.0.1", 8080))?
    .run()
    .await
```

워커 간에 상태를 **공유**하려면 `Arc`/`web::Data`를 써야 한다 → 자세한 패턴·락 비용은 [[actix-web-application-state]] 참조. 핸들러를 요청별로 흐르게 만드는 내부 경로는 [[actix-web-connection-lifecycle]]에 정리되어 있다.

> ⚠️ **핸들러에서 블로킹 금지.** 각 워커는 요청을 **순차적으로** 처리하므로, 핸들러가 현재 스레드를 막으면 그 워커 전체가 새 요청을 못 받는다([[tokio]] 이벤트 루프 차단). 동기 `sleep`/IO 대신 비동기를 쓰고, 불가피한 CPU/동기 작업은 [[actix-web-databases|web::block]]로 별도 스레드풀에 넘긴다.

```rust
// 나쁜 예 — 워커 스레드가 5초간 멈춘다
fn bad() -> impl Responder {
    std::thread::sleep(Duration::from_secs(5));
    "response"
}

// 좋은 예 — 다른 요청을 그동안 처리
async fn good() -> impl Responder {
    tokio::time::sleep(Duration::from_secs(5)).await;
    "response"
}
```

같은 제약이 **extractor**(`FromRequest`)에도 적용된다 → [[actix-web-extractors]].

## Keep-Alive

연결을 열어 두고 후속 요청을 기다린다. HTTP/1.0은 기본 **off**, HTTP/1.1·HTTP/2는 기본 **on**.

```rust
use actix_web::{http::KeepAlive, HttpServer};
use std::time::Duration;

HttpServer::new(app).keep_alive(Duration::from_secs(75)); // 75초 타이머
HttpServer::new(app).keep_alive(KeepAlive::Os);           // OS keep-alive
HttpServer::new(app).keep_alive(None);                    // 비활성화
```

응답 단위로 강제 종료하려면 `HttpResponseBuilder::force_close()`를 호출한다. keepalive 값이 워커 점유·동시성에 미치는 영향은 [[actix-web-connection-lifecycle]] 참조.

## Graceful Shutdown

종료 시그널을 받으면 워커는 정해진 시간 안에 진행 중인 요청을 마무리하고, timeout 후에도 살아 있으면 강제 drop된다. 기본 shutdown timeout은 **30초**이며 `shutdown_timeout()`로 조정한다.

시그널별 동작(CTRL-C는 모든 OS, 나머지는 unix):

| 시그널 | 동작 |
|--------|------|
| SIGTERM | **Graceful** shutdown (timeout 내 마무리) |
| SIGINT / CTRL-C | **Force** shutdown |
| SIGQUIT | **Force** shutdown |

`disable_signals()`로 시그널 처리를 끌 수 있다(외부 supervisor가 직접 제어할 때).

## TLS / HTTPS

`rustls`·`openssl` 두 구현을 crate feature로 지원한다.

```toml
[dependencies]
actix-web = { version = "4", features = ["rustls-0_23"] }
rustls = "0.23"
rustls-pemfile = "2"
```

`bind_rustls_0_23()` / `bind_openssl()`로 TLS 소켓에 바인드한다.

```rust
HttpServer::new(|| App::new().route("/", web::get().to(index)))
    .bind_rustls_0_23(("127.0.0.1", 8443), tls_config)?
    .run()
    .await
```

## HTTP/2 협상

`rustls`/`openssl` feature가 켜지면 HTTP/2가 활성화된다. **협상 경로는 두 가지**:

- **TLS ALPN**: `bind_rustls`/`bind_openssl`로 TLS 위에서 ALPN으로 h2 협상.
- **Prior knowledge** (RFC 7540 §3.4): cleartext·TLS 모두 지원하되, 저수준 `actix-http` 서비스 빌더를 써야 한다.

> ⚠️ HTTP/1.1 → HTTP/2 평문 업그레이드(RFC 7540 §3.2)는 **지원하지 않는다**.

## 정적 파일 서빙 (actix-files)

`actix-files` crate로 파일을 서빙한다. 단일 파일은 `NamedFile`, 디렉토리는 `Files`(반드시 `App::service()`로 등록).

```rust
use actix_files as fs;
use actix_web::{App, HttpServer};

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new().service(
            fs::Files::new("/static", ".")
                .show_files_listing()   // 디렉토리 리스팅(기본 비활성)
                .use_last_modified(true),
        )
    })
    .bind(("127.0.0.1", 8080))?
    .run()
    .await
}
```

`NamedFile`은 `use_etag`, `use_last_modified`, `set_content_disposition` 같은 옵션을 제공한다.

> ⚠️ **경로 traversal 주의.** `/{filename:.*}` 같은 path tail 정규식으로 `NamedFile`을 열면, 공격자가 URL에 `../`를 넣어 서버 프로세스가 접근 가능한 임의 파일을 읽을 수 있다. 사용자 입력 경로는 반드시 정규화·검증한다.

## 개발 자동 재시작

`watchexec`로 `.rs` 변경 시 `cargo run`을 자동 재컴파일·재시작한다(과거 권장되던 `systemfd`+`listenfd` 조합은 gotcha가 많아 더 이상 권장하지 않음).

```sh
watchexec -e rs -r cargo run      # rs 파일 변경 시 재시작
watchexec -w src -r cargo run     # src 디렉토리만 감시
```

## References

- [[actix-web-application-state]] — 워커 간 공유 상태, `web::Data`/`Arc`
- [[actix-web-connection-lifecycle]] — 서버 내부 동작(워커 루프·dispatcher)
- [[actix-web-handlers-responders]] — 핸들러·응답 작성
- [[actix-web-databases]] — `web::block`로 동기 작업 오프로딩
- [[tokio]] — 비동기 런타임, 블로킹 금지의 근거
- [[actix-web-official-docs]] — Server / HTTP2 / Static Files / Auto-Reloading
