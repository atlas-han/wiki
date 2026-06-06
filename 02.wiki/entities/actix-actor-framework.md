---
title: "Actix (Actor Framework)"
type: entity
category: tool
tags: [actix, actor-model, rust, concurrency]
created: 2026-06-06
updated: 2026-06-06
links: [https://actix.rs/docs/actix, https://docs.rs/actix, https://github.com/actix/actix]
sources: [actix-web-official-docs]
---

# Actix (Actor Framework)

Rust용 **actor 모델** 런타임 라이브러리. 각 actor는 독립된 실행 컨텍스트에서 동작하며 오직 **메시지 전달**로 통신한다(상태 공유 없음). [[tokio]] 위에서 동작하고 MSRV는 Rust 1.40+.

## actix-web과의 관계

역사적으로 [[actix-web]]은 이 actor 프레임워크 위에 구축됐지만, 현재는 *"largely unrelated"* — actix-web 코어는 actor를 쓰지 않는다. actor는 WebSocket 등 상태를 가진 장수 연결을 다룰 때 선택적으로 유용하다. (단, 최신 WebSocket 가이드는 actor 없는 `actix-ws`를 권장 → [[actix-web-websockets]].)

## 핵심 개념

- [[actix-actor-model]] — `Actor` trait, lifecycle(Started/Running/Stopping/Stopped), `Handler<M>`/`Message`
- [[actix-actor-address]] — `Addr<A>`·`Recipient<M>`, `send`/`do_send`/`try_send`
- [[actix-actor-context]] — `Context<A>`, mailbox 용량
- [[actix-arbiter]] — 단일 스레드 이벤트 루프, `System`
- [[actix-sync-arbiter]] — CPU-bound 작업용 동기 스레드 풀(`SyncContext`)

> ⚠️ 공식 문서의 actor 섹션 일부(Stream / IO Helpers / Supervisor / Registry / Helper Actors)는 **WIP 스텁**으로 본문이 없다.

## References

- 문서: <https://actix.rs/docs/actix> ([[actix-web-official-docs]])
- API: <https://docs.rs/actix>
