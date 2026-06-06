---
title: "Tokio"
type: entity
category: tool
tags: [tokio, rust, async, runtime]
created: 2026-06-06
updated: 2026-06-06
links: [https://tokio.rs, https://docs.rs/tokio]
sources: [actix-web-official-docs]
---

# Tokio

Rust의 사실상 표준 **비동기 런타임**. async/await 기반 작업을 스케줄링하는 멀티스레드 이벤트 루프, 비동기 I/O, 타이머, 동기화 프리미티브를 제공한다.

[[actix-web]]과 [[actix-actor-framework]]가 모두 tokio 위에서 동작한다. actix-web의 [[actix-web-http-server|HttpServer 워커 모델]]·[[actix-web-connection-lifecycle|연결 lifecycle]]은 tokio 태스크 스케줄링에 기반하며, 그래서 핸들러 안에서의 블로킹(동기 sleep, 동기 DB 호출)이 이벤트 루프를 막는다 — 해결책은 [[actix-web-databases|web::block]] 오프로딩.

## References

- <https://tokio.rs>
