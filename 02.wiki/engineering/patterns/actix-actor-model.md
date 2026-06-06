---
title: "Actix — Actor Model"
type: engineering
category: pattern
tags: [actix, actor-model, rust, concurrency]
created: 2026-06-06
updated: 2026-06-06
related: [actix-actor-framework, actix-actor-address, actix-actor-context, actix-arbiter]
first-seen: actix-web-official-docs
sources: [actix-web-official-docs]
---

[[actix-actor-framework]]는 [Actor Model](https://en.wikipedia.org/wiki/Actor_model) 위에 세워진 Rust 동시성 프레임워크다. 애플리케이션을 **상태와 행동을 캡슐화하고 메시지로만 통신하는 독립 실행 actor들의 집합**으로 작성한다. actor는 직접 참조되지 않고 오직 주소([[actix-actor-address]])를 통해서만 접근하며, 각 actor는 자신만의 실행 컨텍스트([[actix-actor-context]]) 안에서 동작한다.

## 핵심 trait

actor를 정의하려면 세 가지 조각이 필요하다.

- **`Actor`** — 어떤 Rust 타입이든 이 trait을 구현하면 actor가 된다. `type Context`로 실행 컨텍스트를 지정한다 (async actor는 `Context<Self>`).
- **`Message`** — actor 간 주고받는 메시지. `type Result`로 응답 타입을 정의한다. 모든 메시지는 정적 타입이다.
- **`Handler<M>`** — actor가 특정 메시지 `M`을 처리하는 방법. `handle()` 메서드에서 메시지를 받아 `Result` 타입을 반환한다.

### Message 정의

`Message` trait을 직접 구현하거나, `#[derive(Message)]` + `#[rtype(result = "...")]`로 간결하게 선언한다.

```rust
use actix::prelude::*;

// 수동 구현
struct Ping;

impl Message for Ping {
    type Result = Result<bool, std::io::Error>;
}
```

```rust
// derive 매크로 — rtype이 Message::Result를 지정
#[derive(Message)]
#[rtype(result = "Result<bool, std::io::Error>")]
struct Ping;
```

## Actor lifecycle

actor는 4단계 상태를 거친다. 상태 전이 시 `Actor` trait의 훅 메서드가 호출된다.

| 상태 | 설명 | 훅 |
|------|------|-----|
| **Started** | 항상 이 상태에서 시작. 컨텍스트 사용 가능 — 다른 actor 시작, async stream 등록, 설정 작업 | `started()` |
| **Running** | `started()` 이후 진입. 무기한 머무를 수 있음 | — |
| **Stopping** | 아래 조건에서 진입 | `stopping()` |
| **Stopped** | 최종 상태. actor가 drop됨 | `stopped()` |

**Stopping 진입 조건:**
- actor 스스로 `Context::stop()` 호출
- actor의 모든 주소가 drop됨 (참조하는 곳이 없음)
- 컨텍스트에 등록된 이벤트 객체가 없음

**Stopping에서 복귀:** 새 주소를 만들거나 이벤트 객체를 추가한 뒤 `stopping()`이 `Running::Continue`를 반환하면 `Running` 상태로 되돌아간다. 기본 구현은 `Running::Stop`을 반환해 정지를 확정한다. `Context::stop()`으로 정지가 시작된 경우 컨텍스트는 즉시 수신 메시지 처리를 멈추고, 복귀하지 않으면 처리되지 않은 메시지는 모두 drop된다.

```rust
fn stopping(&mut self, ctx: &mut Self::Context) -> Running {
    // 기본 구현. 복귀하려면 Running::Continue 반환
    Running::Stop
}
```

## Canonical 예제 — Ping

`#[derive(Message)]`로 메시지를, `Actor`로 lifecycle 훅을, `Handler<Ping>`로 처리 로직을 정의하고, `start()`로 띄운 뒤 `send().await`로 응답을 받는다.

```rust
use actix::prelude::*;

/// Define message
#[derive(Message)]
#[rtype(result = "Result<bool, std::io::Error>")]
struct Ping;

// Define actor
struct MyActor;

// Provide Actor implementation for our actor
impl Actor for MyActor {
    type Context = Context<Self>;

    fn started(&mut self, ctx: &mut Context<Self>) {
       println!("Actor is alive");
    }

    fn stopped(&mut self, ctx: &mut Context<Self>) {
       println!("Actor is stopped");
    }
}

/// Define handler for `Ping` message
impl Handler<Ping> for MyActor {
    type Result = Result<bool, std::io::Error>;

    fn handle(&mut self, msg: Ping, ctx: &mut Context<Self>) -> Self::Result {
        println!("Ping received");

        Ok(true)
    }
}

#[actix::main]
async fn main() {
    // Start MyActor in current thread
    let addr = MyActor.start();

    // send() message returns Future object, that resolves to message result
    let result = addr.send(Ping).await;

    match result {
        Ok(res) => println!("Got result: {}", res.unwrap()),
        Err(err) => println!("Got error: {}", err),
    }
}
```

## MessageResponse — 커스텀 응답 타입

`handle()`이 반환하는 타입은 `MessageResponse<A, M>` trait을 구현해야 한다. 대부분의 표준 타입(`Result`, `usize` 등)은 이미 구현되어 있지만, 자체 타입으로 응답하려면 직접 구현한다.

```rust
pub trait MessageResponse<A: Actor, M: Message> {
    fn handle(self, ctx: &mut A::Context, tx: Option<OneshotSender<M::Result>>);
}
```

## Actor 띄우기

async actor는 `Actor::start()` 또는 `Actor::create()`로 시작한다. `start()`는 인스턴스를 즉시 만들 수 있을 때, `create()`는 인스턴스 생성 전에 컨텍스트 객체에 접근해야 할 때 쓴다. 둘 다 주소([[actix-actor-address]])를 반환한다. actor가 실제로 돌아가는 스레드/이벤트 루프는 [[actix-arbiter]]가 제공하며, CPU-bound 작업은 [[actix-sync-arbiter]]를 쓴다.

## When to use

- 가변 상태를 공유 락 없이 순차적으로 처리하고 싶을 때 (actor의 mailbox가 직렬화 보장)
- WebSocket 연결, 구독/이벤트 시스템 등 stateful 동시 처리 — [[actix-web]]의 [[actix-web-websockets]]가 이 모델 위에 구축됨
- 메시지 패싱으로 컴포넌트 간 결합도를 낮추고 싶을 때

## References

- [[actix-actor-framework]] — actor 프레임워크 엔티티
- [[actix-actor-address]] · [[actix-actor-context]] · [[actix-arbiter]] · [[actix-sync-arbiter]]
- [[actix-web]] — 같은 생태계의 웹 프레임워크
- raw: `01.raw/docs/actix-web/actor-framework/actor.md`, `getting-started.md`
- [actix.rs — Actor](https://actix.rs/docs/actix/actor)
