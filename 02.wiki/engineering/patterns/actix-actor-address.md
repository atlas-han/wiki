---
title: "Actix — Address (Addr & Recipient)"
type: engineering
category: pattern
tags: [actix, actor-model, rust, messaging]
created: 2026-06-06
updated: 2026-06-06
related: [actix-actor-model, actix-actor-context]
first-seen: actix-web-official-docs
sources: [actix-web-official-docs]
---

actor는 직접 참조되지 않고 **주소(address)를 통해서만 통신**한다. `Addr<A>`는 특정 actor 타입 `A`로 메시지를 보내는 핸들이고, `Recipient<M>`은 actor 타입을 지운 채 **단일 메시지 `M`만 받는** 수신자다. 메시지 정의는 → [[actix-actor-model]], mailbox 용량 제어는 → [[actix-actor-context]].

## 주소 얻기

`Actor::start()` / `Actor::create()`가 주소를 반환한다. actor 내부에서는 컨텍스트에서 자기 주소를 얻는다 (→ [[actix-actor-context]]).

```rust
struct MyActor;

impl Actor for MyActor {
    type Context = Context<Self>;
}

let addr = MyActor.start();
```

```rust
// actor 내부에서 자기 주소 — Context는 AsyncContext를 구현해야 함
impl Actor for MyActor {
    type Context = Context<Self>;

    fn started(&mut self, ctx: &mut Context<Self>) {
       let addr = ctx.address();
    }
}
```

## 메시지 보내는 세 가지 방법

`Addr`는 backpressure·에러 처리 정도가 다른 세 가지 send를 제공한다.

| 메서드 | 반환 | mailbox 가득 참 | mailbox 닫힘(actor 죽음) | 응답 |
|--------|------|----------------|------------------------|------|
| **`send(M)`** | `Future` → `Result<M::Result, MailboxError>` | future가 대기 | `MailboxError` | 받음 |
| **`try_send(M)`** | `Result<(), SendError>` 즉시 | `SendError` 반환 | `SendError` 반환 | 없음 |
| **`do_send(M)`** | `()` | 한도 무시하고 큐잉 (bypass) | 조용히 drop | 없음 |

- **`send(M)`** — future를 반환하고 메시지 처리 결과로 resolve된다. **이 future를 drop하면 메시지는 취소된다.** 응답이 필요하거나 backpressure를 원할 때 사용.
- **`try_send(M)`** — 즉시 전송 시도. mailbox가 가득 차거나 닫혀 있으면 `SendError` 반환. non-blocking으로 빠르게 떨궈야 할 때.
- **`do_send(M)`** — 결과·backpressure 없이 발사. mailbox가 가득 차도 **한도를 우회해 큐에 넣고**, 닫혀 있으면 조용히 버린다. 실패 indication이 전혀 없다는 점에 주의.

> ⚠️ `do_send`는 mailbox capacity([[actix-actor-context]] 기본 16)를 무시하므로 무분별하게 쓰면 메모리가 무한정 쌓일 수 있다.

## Recipient<M> — 타입 소거 수신자

`Recipient<M>`은 `M`을 처리할 수 있는 actor라면 타입에 상관없이 담을 수 있는 주소다. `Addr::recipient()`로 생성한다. 서로 다른 종류의 actor를 한 컬렉션에 모아 같은 메시지를 뿌리는 **구독(subscription) 시스템**에 적합하다.

### Canonical 예제 — 구독/이벤트 fan-out

`OrderEvents`가 `Recipient<OrderShipped>` 목록을 들고 있고, `EmailSubscriber`·`SmsSubscriber` 등 서로 다른 actor가 같은 이벤트를 구독한다.

```rust
use actix::prelude::*;

#[derive(Message)]
#[rtype(result = "()")]
struct OrderShipped(usize);

#[derive(Message)]
#[rtype(result = "()")]
struct Ship(usize);

/// Subscribe to order shipped event.
#[derive(Message)]
#[rtype(result = "()")]
struct Subscribe(pub Recipient<OrderShipped>);

/// Actor that provides order shipped event subscriptions
struct OrderEvents {
    subscribers: Vec<Recipient<OrderShipped>>,
}

impl OrderEvents {
    fn new() -> Self {
        OrderEvents { subscribers: vec![] }
    }

    /// Send event to all subscribers
    fn notify(&mut self, order_id: usize) {
        for subscr in &self.subscribers {
           subscr.do_send(OrderShipped(order_id));
        }
    }
}

impl Actor for OrderEvents {
    type Context = Context<Self>;
}

impl Handler<Subscribe> for OrderEvents {
    type Result = ();

    fn handle(&mut self, msg: Subscribe, _: &mut Self::Context) {
        self.subscribers.push(msg.0);
    }
}

impl Handler<Ship> for OrderEvents {
    type Result = ();

    fn handle(&mut self, msg: Ship, ctx: &mut Self::Context) {
        self.notify(msg.0);
        System::current().stop();
    }
}

struct EmailSubscriber;
impl Actor for EmailSubscriber { type Context = Context<Self>; }
impl Handler<OrderShipped> for EmailSubscriber {
    type Result = ();
    fn handle(&mut self, msg: OrderShipped, _ctx: &mut Self::Context) {
        println!("Email sent for order {}", msg.0)
    }
}

struct SmsSubscriber;
impl Actor for SmsSubscriber { type Context = Context<Self>; }
impl Handler<OrderShipped> for SmsSubscriber {
    type Result = ();
    fn handle(&mut self, msg: OrderShipped, _ctx: &mut Self::Context) {
        println!("SMS sent for order {}", msg.0)
    }
}

#[actix::main]
async fn main() -> Result<(), actix::MailboxError> {
    let email_subscriber = Subscribe(EmailSubscriber {}.start().recipient());
    let sms_subscriber = Subscribe(SmsSubscriber {}.start().recipient());
    let order_event = OrderEvents::new().start();

    order_event.send(email_subscriber).await?;
    order_event.send(sms_subscriber).await?;
    order_event.send(Ship(1)).await?;

    Ok(())
}
```

서로 다른 [[actix-arbiter]] 위에 있는 actor라도 `Addr`/`Recipient`로 동일하게 통신할 수 있다 — 메시지 패싱은 actor의 위치에 무관하다.

## References

- [[actix-actor-model]] — Message·Handler 정의
- [[actix-actor-context]] — mailbox 용량(`set_mailbox_capacity`)
- [[actix-arbiter]] — 교차 arbiter 통신
- [[actix-actor-framework]] · [[actix-web]]
- raw: `01.raw/docs/actix-web/actor-framework/address.md`
- [actix.rs — Address](https://actix.rs/docs/actix/address)
