---
title: "Actix Web 공식 문서 (actix.rs/docs)"
type: source
tags: [actix-web, rust, web-framework, actor-model, docs]
created: 2026-06-06
updated: 2026-06-06
source-url: https://actix.rs/docs
source-type: docs
date-published: 2024-01-01
ingested: 2026-06-06
---

# Actix Web 공식 문서 (actix.rs/docs)

[actix.rs](https://actix.rs/docs)의 **actix-web** 공식 문서 전체(33 페이지)를 ingest한 소스. actix-web 4.x 기준의 Rust 비동기 웹 프레임워크 가이드와, 그 역사적 기반인 **actix** actor 프레임워크 문서로 구성된다. 원문 verbatim 캡처는 `01.raw/docs/actix-web/`에 보존(렌더 페이지를 pandoc 변환, 다이어그램은 mermaid 소스 보존).

## 구성

- **actix-web core (21)**: Welcome, What is Actix Web, Getting Started, Application, Server, Extractors, Handlers, Errors, URL Dispatch, Requests, Responses, Testing, Middleware, Static Files, CORS, WebSockets, HTTP/2, Auto-Reloading, Databases + 다이어그램 2종(HTTP Server Init, Connection Lifecycle)
- **actix actor framework (12)**: Actix, Getting Started, Actor, Address, Context, Arbiter, SyncArbiter + WIP 스텁 5종(Stream / IO Helpers / Supervisor / Registry / Helper Actors)

## 핵심 takeaway

1. **Tokio 기반 async 프레임워크, actor와는 분리됨** — *"Long ago, Actix Web was built on top of the `actix` actor framework. Now, Actix Web is largely unrelated to the actor framework"* (whatis). actor는 이제 WebSocket 등 일부에서만 선택적. stable Rust 1.72+(MSRV), HTTP/1.1·HTTP/2·TLS 네이티브.
2. **Extractor(`FromRequest`)가 시그니처 혁신** — 요청을 핸들러 인자에서 타입 안전하게 자동 추출(핸들러당 최대 12개). → [[actix-web-extractors]]
3. **멀티스레드 워커 모델** — `HttpServer`가 코어당 워커 1개를 띄우고 `App` 팩토리를 복제. 공유 상태는 클로저 밖에서 만들어 `web::Data`로 주입. → [[actix-web-application-state]] · [[actix-web-http-server]]
4. **`Responder` trait로 유연한 응답** — 기본 타입·커스텀 타입 모두 핸들러에서 직접 반환. → [[actix-web-handlers-responders]]
5. **`Transform`+`Service` 미들웨어** — 요청 전·응답 후 양방향 훅, 로깅/CORS/세션/압축 기본 제공. → [[actix-web-middleware]]

## 이 소스가 생성한 페이지

- 프레임워크 entity: [[actix-web]] (허브) · [[actix-actor-framework]] · [[tokio]] · [[serde]]
- 요청 처리: [[actix-web-extractors]] · [[actix-web-handlers-responders]] · [[actix-web-routing]]
- 앱·서버: [[actix-web-application-state]] · [[actix-web-http-server]] · [[actix-web-connection-lifecycle]]
- 횡단 관심사: [[actix-web-middleware]] · [[actix-web-error-handling]]
- 통합: [[actix-web-testing]] · [[actix-web-websockets]] · [[actix-web-databases]]
- actor 모델: [[actix-actor-model]] · [[actix-actor-address]] · [[actix-actor-context]] · [[actix-arbiter]] · [[actix-sync-arbiter]]

## 버전·범위 메모

- actix-web **4.x** (API 링크 `docs.rs/actix-web/4/`), MSRV **Rust 1.72**. actix actor 프레임워크는 Rust 1.40+.
- TLS는 `rustls` 또는 `openssl` feature 선택. HTTP/2는 TLS 위에서 협상(또는 prior-knowledge).
- WIP 스텁 5종(actor framework의 sec-7~11)은 본문이 `**WIP**`뿐이라 페이지화하지 않음.

## References

- 원문: <https://actix.rs/docs>
- API 문서: <https://docs.rs/actix-web/4>
- raw 캡처: `01.raw/docs/actix-web/` (33 파일 + 00-index.md)
