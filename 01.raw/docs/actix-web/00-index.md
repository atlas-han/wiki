---
title: "Actix Web Documentation — Index"
type: docs
source: https://actix.rs/docs
site: actix.rs
project: actix-web
section: Index
created: 2026-06-06
tags:
  - clippings/docs
  - actix-web
  - rust
  - index
---

**Source**: https://actix.rs/docs (캡처일 2026-06-06)

actix.rs 공식 문서 전체를 `01.raw` 원본 레이어로 캡처한 모음. 렌더링 페이지를 `pandoc`으로 verbatim 변환하고 네비게이션·앵커 노이즈만 제거했으며, 다이어그램 페이지는 mermaid `.mmd` 소스를 보존했다. 총 **33 페이지** (actix-web 본 문서 21 + actix actor 프레임워크 12).

> 이 디렉토리는 `raw/` 레이어 = 진실의 출처(immutable). wiki 흡수(`/ingest`)는 별도 단계.

## actix-web (core, 21)

### Introduction
- [Welcome](welcome.md) — https://actix.rs/docs/
- [What is Actix Web](whatis.md) — https://actix.rs/docs/whatis

### Basics
- [Getting Started](getting-started.md) — https://actix.rs/docs/getting-started
- [Application](application.md) — https://actix.rs/docs/application
- [Server](server.md) — https://actix.rs/docs/server
- [Extractors](extractors.md) — https://actix.rs/docs/extractors
- [Handlers](handlers.md) — https://actix.rs/docs/handlers

### Advanced
- [Errors](errors.md) — https://actix.rs/docs/errors
- [URL Dispatch](url-dispatch.md) — https://actix.rs/docs/url-dispatch
- [Requests](request.md) — https://actix.rs/docs/request
- [Responses](response.md) — https://actix.rs/docs/response
- [Testing](testing.md) — https://actix.rs/docs/testing
- [Middleware](middleware.md) — https://actix.rs/docs/middleware
- [Static Files](static-files.md) — https://actix.rs/docs/static-files
- [CORS](cors.md) — https://actix.rs/docs/cors

### Protocols
- [WebSockets](websockets.md) — https://actix.rs/docs/websockets
- [HTTP/2](http2.md) — https://actix.rs/docs/http2

### Patterns
- [Auto-Reloading](autoreload.md) — https://actix.rs/docs/autoreload
- [Databases](databases.md) — https://actix.rs/docs/databases

### Diagrams (mermaid 소스 보존)
- [HTTP Server Initialization](http_server_init.md) — https://actix.rs/docs/http_server_init
- [Connection Lifecycle](conn_lifecycle.md) — https://actix.rs/docs/conn_lifecycle

## actix — Actor Framework (12)

actix-web가 기반하는 actor 시스템. → `actor-framework/`

- [Actix (Actor Framework)](actor-framework/actix.md) — https://actix.rs/docs/actix
- [Getting Started (Actix)](actor-framework/getting-started.md) — https://actix.rs/docs/actix/getting-started
- [Actor](actor-framework/actor.md) — https://actix.rs/docs/actix/actor
- [Address](actor-framework/address.md) — https://actix.rs/docs/actix/address
- [Context](actor-framework/context.md) — https://actix.rs/docs/actix/context
- [Arbiter](actor-framework/arbiter.md) — https://actix.rs/docs/actix/arbiter
- [SyncArbiter](actor-framework/sync-arbiter.md) — https://actix.rs/docs/actix/sync-arbiter
- [Stream](actor-framework/sec-7-stream.md) — https://actix.rs/docs/actix/sec-7-stream *(WIP 스텁)*
- [IO Helpers](actor-framework/sec-8-io-helpers.md) — https://actix.rs/docs/actix/sec-8-io-helpers *(WIP 스텁)*
- [Supervisor](actor-framework/sec-9-supervisor.md) — https://actix.rs/docs/actix/sec-9-supervisor *(WIP 스텁)*
- [Registry](actor-framework/sec-10-registry.md) — https://actix.rs/docs/actix/sec-10-registry *(WIP 스텁)*
- [Helper Actors](actor-framework/sec-11-helper-actors.md) — https://actix.rs/docs/actix/sec-11-helper-actors *(WIP 스텁)*
