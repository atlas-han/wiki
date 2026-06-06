---
title: "Actix — Context"
type: engineering
category: pattern
tags: [actix, actor-model, rust, mailbox]
created: 2026-06-06
updated: 2026-06-06
related: [actix-actor-model, actix-actor-address]
first-seen: actix-web-official-docs
sources: [actix-web-official-docs]
---

`Context<A>`는 각 actor의 **실행 컨텍스트이자 내부 상태**다. actor는 컨텍스트를 통해 자기 주소를 알아내고, mailbox 한도를 바꾸고, 스스로를 멈추고, future/stream을 실행 큐에 등록한다. 컨텍스트는 실행 중에만 존재하며 actor마다 별개다. actor 정의는 → [[actix-actor-model]], 주소 핸들은 → [[actix-actor-address]].

## Mailbox

모든 메시지는 먼저 actor의 mailbox에 들어가고, 그다음 컨텍스트가 해당 핸들러를 호출한다. mailbox는 **bounded**이며, `Context` 타입의 기본 용량은 **16개**다. `Context::set_mailbox_capacity()`로 조정한다 (보통 `started()`에서).

```rust
struct MyActor;

impl Actor for MyActor {
    type Context = Context<Self>;

    fn started(&mut self, ctx: &mut Self::Context) {
        ctx.set_mailbox_capacity(1);
    }
}

let addr = MyActor.start();
```

> ⚠️ 이 한도는 우회하는 경로가 있다 — `Addr::do_send(M)`은 mailbox queue 한도를 무시하고, `AsyncContext::notify(M)` / `notify_later(M, Duration)`은 mailbox를 아예 건너뛴다. ([[actix-actor-address]]에서 `do_send` 동작 참고)

## 자기 주소 얻기 — `ctx.address()`

이벤트를 나중에 다시 큐잉하거나, 메시지에 자기 주소로 응답하거나, 다른 actor에게 자신을 알려줄 때 쓴다. 자기 자신에게 메시지를 보내려면 `AsyncContext::notify(M)`가 더 낫다.

```rust
struct MyActor;
struct WhoAmI;

impl Message for WhoAmI {
    type Result = Result<actix::Addr<MyActor>, ()>;
}

impl Actor for MyActor {
    type Context = Context<Self>;
}

impl Handler<WhoAmI> for MyActor {
    type Result = Result<actix::Addr<MyActor>, ()>;

    fn handle(&mut self, msg: WhoAmI, ctx: &mut Context<Self>) -> Self::Result {
        Ok(ctx.address())
    }
}

let who_addr = addr.do_send(WhoAmI{});
```

## Actor 멈추기 — `ctx.stop()`

컨텍스트 안에서 `Context::stop()`을 호출하면 이후 mailbox 메시지 처리를 멈춘다. 에러 상황이나 프로그램 종료 시 사용한다. 이는 lifecycle을 `Stopping` 상태로 전이시킨다 (→ [[actix-actor-model]]).

### Canonical 예제 — 4번째 ping 이후 정지

`stop()` 호출 후에는 mailbox가 닫혀 `try_send`가 에러를 반환한다.

```rust
impl Handler<Ping> for MyActor {
    type Result = usize;

    fn handle(&mut self, msg: Ping, ctx: &mut Context<Self>) -> Self::Result {
        self.count += msg.0;

        if self.count > 5 {
            println!("Shutting down ping receiver.");
            ctx.stop()
        }

        self.count
    }
}

#[actix::main]
async fn main() {
    let addr = MyActor { count: 10 }.start();

    let addr_2 = addr.clone();
    let res = addr.send(Ping(6)).await;

    match res {
        // actor가 멈춘 뒤이므로 try_send는 실패
        Ok(_) => assert!(addr_2.try_send(Ping(6)).is_err()),
        _ => {}
    }
}
```

## AsyncContext — future/stream 등록

`Context`는 `AsyncContext` trait을 구현한다. 이를 통해 actor는 자신의 이벤트 루프에 작업을 얹는다.

- **`ctx.address()`** — 자기 주소 반환 (위 참조)
- **`ctx.spawn(fut)`** — future를 컨텍스트에 등록해 실행
- **`ctx.wait(fut)`** — future가 끝날 때까지 actor가 다른 메시지를 처리하지 않도록 대기시킴
- **`ctx.notify(M)` / `ctx.notify_later(M, Duration)`** — 자기 자신에게 메시지 전달 (mailbox 우회)
- **`ctx.run_later(...)` / `ctx.add_stream(...)`** — 지연 작업·stream 등록

이 작업들은 actor가 속한 [[actix-arbiter]]의 이벤트 루프에서 실행된다.

## When to use

- mailbox capacity를 줄여 backpressure를 강하게 걸거나, 늘려서 burst를 흡수할 때 `set_mailbox_capacity`
- 자기 자신에게 후속 작업을 예약할 때 `notify` / `run_later`
- 에러·종료 조건에서 actor를 정리할 때 `stop`

## References

- [[actix-actor-model]] — Actor·lifecycle (`Stopping` 전이)
- [[actix-actor-address]] — `do_send`의 mailbox 한도 우회
- [[actix-arbiter]] — 컨텍스트가 실행되는 이벤트 루프
- [[actix-actor-framework]] · [[actix-web]]
- raw: `01.raw/docs/actix-web/actor-framework/context.md`
- [actix.rs — Context](https://actix.rs/docs/actix/context)
