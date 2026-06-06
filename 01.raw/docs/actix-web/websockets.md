---
title: "WebSockets"
type: docs
source: https://actix.rs/docs/websockets
site: actix.rs
project: actix-web
section: Protocols
created: 2026-06-06
tags:
  - clippings/docs
  - actix-web
  - rust
---

**Source URL**: https://actix.rs/docs/websockets

> 본 파일은 actix.rs 렌더링 페이지를 pandoc 으로 변환한 verbatim 캡처다. 코드 블록·산문 원문 보존, 네비게이션·앵커 노이즈만 제거.

# WebSockets

Actix Web supports a high-level WebSocket interface via the `actix-ws`
crate. Using this crate, it's possible to convert a request's `Payload`
stream into a stream of
[*ws::Message*](https://docs.rs/actix-ws/0.3/actix_ws/enum.Message.html)s
and then react to them inside a spawned async task.

The following is an example of a simple WebSocket echo server:

```rust
use actix_web::{rt, web, App, Error, HttpRequest, HttpResponse, HttpServer};
use actix_ws::AggregatedMessage;
use futures_util::StreamExt as _;

async fn echo(req: HttpRequest, stream: web::Payload) -> Result<HttpResponse, Error> {
    let (res, mut session, stream) = actix_ws::handle(&req, stream)?;

    let mut stream = stream
        .aggregate_continuations()
        // aggregate continuation frames up to 1MiB
        .max_continuation_size(2_usize.pow(20));

    // start task but don't wait for it
    rt::spawn(async move {
        // receive messages from websocket
        while let Some(msg) = stream.next().await {
            match msg {
                Ok(AggregatedMessage::Text(text)) => {
                    // echo text message
                    session.text(text).await.unwrap();
                }

                Ok(AggregatedMessage::Binary(bin)) => {
                    // echo binary message
                    session.binary(bin).await.unwrap();
                }

                Ok(AggregatedMessage::Ping(msg)) => {
                    // respond to PING frame with PONG frame
                    session.pong(&msg).await.unwrap();
                }

                _ => {}
            }
        }
    });

    // respond immediately with response connected to WS session
    Ok(res)
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| App::new().route("/echo", web::get().to(echo)))
        .bind(("127.0.0.1", 8080))?
        .run()
        .await
}
```

> A simple WebSocket echo server example is available [in the examples
> repo](https://github.com/actix/examples/tree/master/websockets/echo-actorless).

> An example chat server is also available [in the examples
> directory](https://github.com/actix/examples/tree/master/websockets/chat-actorless)
