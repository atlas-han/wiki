---
title: "Actix — Arbiter & System"
type: engineering
category: system
tags: [actix, actor-model, rust, runtime, concurrency, tokio]
created: 2026-06-06
updated: 2026-06-06
related: [actix-actor-model, actix-sync-arbiter, tokio]
first-seen: actix-web-official-docs
sources: [actix-web-official-docs]
---

`Arbiter`는 **전용 OS 스레드 위에서 도는 단일 스레드 이벤트 루프**로, actor·function·future를 위한 비동기 실행 환경을 제공한다. actor의 `Context`([[actix-actor-context]])가 actor 고유의 실행 상태를 정의한다면, Arbiter는 그 actor가 **돌아가는 환경**을 호스팅한다. "Arbiter = single-threaded event loop"로 기억하면 된다. [[tokio]] 런타임 위에서 동작한다.

## System과 Arbiter

`System`은 전체 actix 런타임을 대표한다. `System::new`는 actor들이 그 안에서 돌아갈 **System Arbiter**를 만든다. actor에 `start()`를 호출하면 그 actor는 System Arbiter의 스레드 안에서 실행된다. 대부분의 프로그램은 이 단일 Arbiter 하나로 충분하다.

```rust
// #[actix::main]은 내부적으로 System을 띄우고 main future를 구동한다
#[actix::main]
async fn main() {
    let addr = MyActor.start(); // System Arbiter 스레드에서 실행
    // ...
    System::current().stop();   // System 정지 → 모든 Arbiter·Actor 종료
}
```

단일 스레드이지만 매우 효율적인 이벤트 루프 패턴을 쓰므로 비동기 이벤트 처리에 적합하다. 반면 **동기·CPU-bound 작업은 이벤트 루프를 블로킹**하므로, 그런 경우엔 [[actix-sync-arbiter]]로 다른 스레드에 연산을 떠넘겨야 한다.

## 이벤트 루프와 동시성

하나의 `Arbiter`는 하나의 스레드와 하나의 이벤트 풀을 제어한다. `Arbiter::spawn`, `Context::run_later` 등으로 작업을 올리면 그 작업 큐에 큐잉된다.

actix 자체는 동시성을 지원하지만, **일반 `Arbiter`(SyncArbiter가 아닌)는 단일 스레드라 그 자체로는 병렬이 아니다.** 동시 실행이 필요하면 `Arbiter::new`, `ArbiterBuilder`, `Arbiter::start`로 여러 Arbiter를 띄운다.

- 새 Arbiter를 만들면 새 실행 컨텍스트(새 스레드)가 생긴다.
- actor는 **자신이 생성된 Arbiter에 묶이며 Arbiter 간을 자유롭게 이동하지 못한다.**
- 그러나 서로 다른 Arbiter 위의 actor들은 일반 `Addr`/`Recipient`([[actix-actor-address]])로 여전히 통신할 수 있다 — 메시지 패싱은 actor가 같은 Arbiter에 있든 다른 Arbiter에 있든 무관하다.

## Canonical 예제 — Arbiter로 async 이벤트 순서 보장

actor A의 결과가 완료된 뒤에만 actor B의 작업을 실행하고 싶을 때, `Arbiter::current().spawn`으로 future를 이벤트 루프에 올려 순서를 보장한다.

```rust
use actix::prelude::*;

struct SumActor {}
impl Actor for SumActor { type Context = Context<Self>; }

#[derive(Message)]
#[rtype(result = "usize")]
struct Value(usize, usize);

impl Handler<Value> for SumActor {
    type Result = usize;
    fn handle(&mut self, msg: Value, _ctx: &mut Context<Self>) -> Self::Result {
        msg.0 + msg.1
    }
}

struct DisplayActor {}
impl Actor for DisplayActor { type Context = Context<Self>; }

#[derive(Message)]
#[rtype(result = "()")]
struct Display(usize);

impl Handler<Display> for DisplayActor {
    type Result = ();
    fn handle(&mut self, msg: Display, _ctx: &mut Context<Self>) -> Self::Result {
        println!("Got {:?}", msg.0);
    }
}

fn main() {
    let system = System::new("single-arbiter-example");

    let execution = async {
        // `Actor::start`는 actor를 *현재* Arbiter(여기선 System Arbiter)에 띄운다
        let sum_addr = SumActor {}.start();
        let dis_addr = DisplayActor {}.start();

        // Addr::send는 Future를 구현한 Request를 반환한다.
        // await하면 Result<usize, MailboxError>로 resolve된다.
        let sum_result = sum_addr.send(Value(6, 7)).await;

        match sum_result {
            Ok(res) => {
                // A의 결과가 완료된 후에야 B(DisplayActor)로 전달
                dis_addr.send(Display(res)).await;
            }
            Err(e) => {
                eprintln!("Encountered mailbox error: {:?}", e);
            }
        };
    };

    // 현재 Arbiter/이벤트 루프에 future를 spawn
    Arbiter::current().spawn(execution);

    // System을 멈추면 내부의 모든 Arbiter → Actor Context → Actor가 차례로 종료된다
    System::current().stop();

    system.run();
}
```

## API 요약

| API | 역할 |
|-----|------|
| `System::new` / `System::current().stop()` | 전체 런타임 생성/정지 |
| `Arbiter::new`, `ArbiterBuilder`, `Arbiter::start` | 새 OS 스레드 + 이벤트 루프 생성 (동시성) |
| `Arbiter::current()` | 현재 실행 중인 Arbiter 핸들 |
| `Arbiter::spawn(fut)` | 해당 Arbiter 이벤트 루프에 future 올리기 |

## When to use

- **일반 `Arbiter`**: I/O-bound·async actor (대부분의 경우). [[actix-web]]의 HTTP worker도 이 모델 위에서 동작.
- **여러 `Arbiter`**: actor를 여러 스레드에 분산해 동시 처리 (단, 각 actor는 단일 스레드 보장)
- **CPU-bound·블로킹**: 일반 Arbiter를 블로킹하지 말고 → [[actix-sync-arbiter]]

## References

- [[actix-actor-model]] — Actor·Message 정의
- [[actix-actor-context]] — actor별 실행 컨텍스트
- [[actix-actor-address]] — 교차 Arbiter 통신
- [[actix-sync-arbiter]] — CPU-bound 동기 작업용 스레드 풀
- [[tokio]] — 하부 async 런타임
- [[actix-actor-framework]] · [[actix-web]]
- raw: `01.raw/docs/actix-web/actor-framework/arbiter.md`
- [actix.rs — Arbiter](https://actix.rs/docs/actix/arbiter)
