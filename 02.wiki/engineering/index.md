---
title: Engineering
type: overview
tags: [meta, engineering]
created: 2026-05-25
updated: 2026-06-06
---

# Engineering

소프트웨어 엔지니어링 지식 인덱스. LLM이 ingest·query마다 갱신합니다.

> 형식: `- [[slug]] — 한 줄 요약`

---

## Systems

분산 시스템, 데이터베이스, 네트워킹, 인프라 관련 개념.

- [[actix-web-http-server]] — [[actix-web]] `HttpServer` 워커 모델(코어당 1 워커)·TLS/HTTP2·graceful shutdown·정적 파일.
- [[actix-web-connection-lifecycle]] — actix-web 내부 Accept/Worker/Dispatcher 루프 (mermaid 다이어그램).
- [[actix-arbiter]] — [[actix-actor-framework|actix]] actor의 단일 스레드 이벤트 루프 + `System`.
- [[actix-sync-arbiter]] — CPU-bound/블로킹 작업용 동기 actor 스레드 풀(`SyncContext`).

## Patterns

디자인 패턴, 아키텍처 패턴 (Clean Architecture, DDD, CQRS, Event Sourcing 등).

- [[pets-vs-cattle]] — 인프라 운영의 mental model. LLM-에이전트 인프라([[brain-hands-decoupling]])에 적용된 사례 있음.
- [[tree-sitter-llm-hybrid]] — 결정론적 파서(Tree-sitter)와 LLM을 각자 잘하는 일로 분업하는 코드 분석 패턴.

**[[actix-web]] (Rust 웹 프레임워크)**
- [[actix-web-extractors]] — `FromRequest` 타입 안전 요청 추출 (Path/Query/Json/Form/Data).
- [[actix-web-handlers-responders]] — 핸들러 시그니처 + `Responder` trait.
- [[actix-web-application-state]] — `web::Data` 공유 상태 + 워커 클로저 함정.
- [[actix-web-routing]] — URL dispatch·scope·guard·URL 생성.
- [[actix-web-middleware]] — `Transform`+`Service` 미들웨어·CORS·세션.
- [[actix-web-error-handling]] — `ResponseError` 커스텀 에러 응답.
- [[actix-web-databases]] — `web::block`(동기 Diesel)·async ORM·r2d2 풀.
- [[actix-web-testing]] — `TestRequest`·`init_service` 통합 테스트.
- [[actix-web-websockets]] — `actix-ws` WebSocket 처리.

**[[actix-actor-framework|actix]] actor 모델**
- [[actix-actor-model]] — `Actor` trait·lifecycle·`Handler`/`Message`.
- [[actix-actor-address]] — `Addr`/`Recipient`·send/do_send/try_send.
- [[actix-actor-context]] — `Context`·mailbox 용량.

## Tools

개발 도구, 프레임워크, 언어별 기법.

- [[tree-sitter]] — 소스를 concrete syntax tree로 파싱하는 결정론적 incremental 파서 (entities/).
- [[understand-anything]] — 코드·wiki를 지식 그래프로 만드는 [[claude-code]] 플러그인 (entities/).
- [[actix-web]] — Rust 비동기 웹 프레임워크 (entities/, 위 패턴·시스템 페이지의 허브).
- [[actix-actor-framework]] · [[tokio]] · [[serde]] — actix 생태계·런타임·직렬화 (entities/).

---

## 관련 위키 영역

- LLM/AI 개념은 [[02.wiki/index#Concepts (LLM/AI)|위키 Concepts 섹션]] 참조
- LLM 에이전트·도구는 entities/ 참조
- SE 관련 책 노트는 [[02.wiki/reading/index]] 참조
