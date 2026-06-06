---
title: "Actix Web — WebSockets"
type: engineering
category: pattern
tags: [actix-web, rust, websockets, actix-ws]
created: 2026-06-06
updated: 2026-06-06
related: [actix-web-handlers-responders, actix-actor-model, actix-actor-framework]
first-seen: actix-web-official-docs
sources: [actix-web-official-docs]
---

[[actix-web]]는 `actix-ws` crate로 고수준 WebSocket 인터페이스를 제공한다. 요청의 `Payload` 스트림을 `ws::Message` 스트림으로 변환한 뒤 spawn된 async task 안에서 메시지에 반응하는 방식으로, **actor를 쓰지 않는다**.

## 동작 방식 (actorless)

1. 핸들러는 `HttpRequest`와 `web::Payload`를 받는다 ([[actix-web-handlers-responders]]).
2. `actix_ws::handle(&req, stream)?`이 업그레이드 핸드셰이크를 처리하고 `(HttpResponse, Session, MessageStream)` 3-tuple을 돌려준다.
3. `rt::spawn`으로 메시지 수신 루프를 백그라운드 task로 띄운다 — **응답을 기다리지 않는다**.
4. 핸들러는 즉시 `res`(WS 세션에 연결된 `HttpResponse`)를 반환해 핸드셰이크를 완료한다.

`Session`으로 서버→클라이언트 메시지(`.text()`, `.binary()`, `.pong()`)를 보내고, `MessageStream`을 `.next().await`로 폴링해 클라이언트→서버 메시지를 받는다.

## Canonical: echo 서버

연속(continuation) 프레임을 합치려면 `.aggregate_continuations()`를 쓰고, 수신 메시지는 `AggregatedMessage`로 매칭한다. `.max_continuation_size(...)`로 합칠 최대 크기를 제한한다.

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

핸들러는 일반 라우트와 똑같이 `web::get().to(echo)`로 등록한다 — WebSocket이라고 특별한 라우팅이 필요하지 않다.

## 레거시: actix-web-actors (actor 기반)

이전에는 `actix-web-actors`를 통한 actor 기반 WebSocket이 표준이었다. 이 방식은 [[actix-actor-framework]]의 actor로 WS 연결을 모델링했고, [[actix-actor-model]]에서 "actor는 WebSocket 같은 상태 있는 장기 연결에서만 선택적으로 쓰면 된다"고 말하는 맥락이 바로 이것이다.

> ⚠️ **신규 코드는 `actix-ws`를 권장한다.** actorless 방식이 더 단순하고 일반 async task와 자연스럽게 어울린다. actor의 메일박스·라이프사이클 오버헤드 없이 `Session` + `MessageStream`만으로 충분하다. actor가 필요한 것은 WS 외에 복잡한 상태 머신을 actor로 관리하고 싶을 때뿐이다.

## 예제 레포

- echo (actorless): `actix/examples` → `websockets/echo-actorless`
- chat (actorless): `actix/examples` → `websockets/chat-actorless`

## References

- [[actix-web-official-docs]] — WebSockets (https://actix.rs/docs/websockets)
- [[actix-web]] · [[actix-web-handlers-responders]] · [[actix-actor-framework]] · [[actix-actor-model]]
