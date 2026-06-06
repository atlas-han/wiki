---
title: "Actix — SyncArbiter"
type: engineering
category: system
tags: [actix, actor-model, rust, thread-pool, cpu-bound]
created: 2026-06-06
updated: 2026-06-06
related: [actix-arbiter, actix-actor-model]
first-seen: actix-web-official-docs
sources: [actix-web-official-docs]
---

`SyncArbiter`는 **CPU-bound·블로킹 작업을 위한 동기 actor 스레드 풀**이다. 하나의 actor 타입을 여러 OS 스레드에서 **병렬 인스턴스**로 띄워, 일반 [[actix-arbiter|Arbiter]]의 단일 스레드 이벤트 루프를 블로킹하지 않고 무거운 연산을 처리한다. actor 정의는 → [[actix-actor-model]].

## 일반 Arbiter와의 대비

| | `Arbiter` (async) | `SyncArbiter` |
|---|---|---|
| 실행 모델 | 단일 스레드 이벤트 루프 | OS 스레드 풀 (N개 워커) |
| Context 타입 | `Context<A>` (`AsyncContext`) | `SyncContext<A>` (async 아님) |
| 적합한 작업 | I/O-bound, async | CPU-bound, 블로킹 (예: 무거운 계산, 동기 DB 드라이버) |
| 한 풀에 담는 actor | 여러 타입 가능 | **단일 타입만** |
| mailbox 한도 | bounded (기본 16) | **무제한** |
| 동시성 | 자체로는 단일 스레드 | N개 인스턴스 병렬 |

## Sync Actor 만들기

`SyncArbiter`에서 돌릴 actor는 Context를 `Context`가 아니라 **`SyncContext`**로 바꿔야 한다. `SyncContext`는 async가 아니므로 `spawn`/`notify` 같은 async 기능을 제공하지 않는다.

```rust
use actix::prelude::*;

struct MySyncActor;

impl Actor for MySyncActor {
    type Context = SyncContext<Self>;
}
```

## SyncArbiter 시작하기

`SyncArbiter::start(N, factory)`로 N개 스레드 풀을 만든다. factory 클로저는 각 워커 인스턴스를 생성한다. **스레드 개수는 생성 시점에만 정할 수 있고 이후 추가/제거할 수 없다.** 반환되는 `Addr`는 일반 actor와 똑같이 쓴다.

```rust
use actix::prelude::*;

struct MySyncActor;

impl Actor for MySyncActor {
    type Context = SyncContext<Self>;
}

// 2개 워커 스레드로 풀 생성. 각 워커는 factory가 만든 MySyncActor 인스턴스
let addr = SyncArbiter::start(2, || MySyncActor);
```

`addr`로 메시지를 보내면 풀의 가용 워커 중 하나가 처리한다. 메시지 전송·future 수신·결과 받기 등은 일반 actor와 동일하다 (→ [[actix-actor-address]]).

## Sync Actor Mailbox

Sync Actor는 **mailbox 한도가 없다.** 그래도 `do_send`·`try_send`·`send`는 평소처럼 가려 써야 한다 — mailbox 한도 외의 에러나 sync/async 동작 차이를 처리해야 하기 때문이다.

## When to use

- **CPU-bound 연산**: 이미지 처리, 압축, 해시, 직렬화 등 이벤트 루프를 오래 점유할 작업
- **블로킹 I/O / 동기 라이브러리**: async 미지원 DB 드라이버나 FFI 호출 — 워커 스레드에 격리
- **고도 병렬 워크로드**: 같은 작업을 N개 인스턴스로 동시에 처리
- 반대로 I/O-bound·async 작업이면 → [[actix-arbiter|Arbiter]]를 그대로 쓴다.

> ⚠️ 한 `SyncArbiter`는 actor 타입 하나만 호스팅한다. 여러 종류의 sync actor가 필요하면 타입마다 별도 `SyncArbiter`를 만들어야 한다.

## References

- [[actix-arbiter]] — async 단일 스레드 이벤트 루프 (대비 대상)
- [[actix-actor-model]] — Actor·Handler 정의
- [[actix-actor-address]] — `Addr`로 sync actor 호출
- [[actix-actor-framework]] · [[actix-web]]
- raw: `01.raw/docs/actix-web/actor-framework/sync-arbiter.md`
- [actix.rs — SyncArbiter](https://actix.rs/docs/actix/sync-arbiter)
