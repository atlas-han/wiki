---
title: Engineering
type: overview
tags: [meta, engineering]
created: 2026-05-25
updated: 2026-07-08
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
- [[twelve-factor-app]] — SaaS 앱 12원칙(config-in-env·stateless·dev/prod parity), cloud-native의 사상적 토대 (sources: 1).
- [[tree-sitter-llm-hybrid]] — 결정론적 파서(Tree-sitter)와 LLM을 각자 잘하는 일로 분업하는 코드 분석 패턴.
- [[design-patterns]] — Refactoring.Guru 한국어 기준 GoF 디자인 패턴 22개 허브(생성·구조·행동).
- [[refactoring]] — behavior를 유지하면서 내부 구조를 개선하는 작은 변경들의 연속.
- [[technical-debt]] — 빠른 delivery를 위해 미룬 구조 개선이 이후 변경 비용의 이자로 돌아오는 상태.
- [[code-smells]] — 리팩터링 후보를 찾는 진단 vocabulary(23개 smell).
  - *Bloaters*: [[long-method]] · [[large-class]] · [[primitive-obsession]] · [[long-parameter-list]] · [[data-clumps]]
  - *OO Abusers*: [[alternative-classes-with-different-interfaces]] · [[refused-bequest]] · [[switch-statements]] · [[temporary-field]]
  - *Change Preventers*: [[divergent-change]] · [[parallel-inheritance-hierarchies]] · [[shotgun-surgery]]
  - *Dispensables*: [[comments]] · [[duplicate-code]] · [[data-class]] · [[dead-code]] · [[lazy-class]] · [[speculative-generality]]
  - *Couplers*: [[feature-envy]] · [[inappropriate-intimacy]] · [[message-chains]] · [[middle-man]]
  - *Other*: [[incomplete-library-class]]
- [[refactoring-techniques]] — behavior-preserving 구조 변경 technique family 허브(6개 family, 66+ technique).
  - [[refactoring-techniques-composing-methods]] · [[refactoring-techniques-moving-features-between-objects]] · [[refactoring-techniques-organizing-data]] · [[refactoring-techniques-simplifying-conditional-expressions]] · [[refactoring-techniques-simplifying-method-calls]] · [[refactoring-techniques-dealing-with-generalization]]

**GoF 디자인 패턴 (Refactoring.Guru KO)**
- [[design-pattern-factory-method]] · [[design-pattern-abstract-factory]] · [[design-pattern-builder]] · [[design-pattern-prototype]] · [[design-pattern-singleton]] — 생성 패턴.
- [[design-pattern-adapter]] · [[design-pattern-bridge]] · [[design-pattern-composite]] · [[design-pattern-decorator]] · [[design-pattern-facade]] · [[design-pattern-flyweight]] · [[design-pattern-proxy]] — 구조 패턴.
- [[design-pattern-chain-of-responsibility]] · [[design-pattern-command]] · [[design-pattern-iterator]] · [[design-pattern-mediator]] · [[design-pattern-memento]] · [[design-pattern-observer]] · [[design-pattern-state]] · [[design-pattern-strategy]] · [[design-pattern-template-method]] · [[design-pattern-visitor]] — 행동 패턴.

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
- [[obsidian-cli-workflow]] — Obsidian 공식 CLI를 quick capture·search·daily note append·agent automation의 terminal command surface로 쓰는 workflow.
- [[actix-web]] — Rust 비동기 웹 프레임워크 (entities/, 위 패턴·시스템 페이지의 허브).
- [[actix-actor-framework]] · [[tokio]] · [[serde]] — actix 생태계·런타임·직렬화 (entities/).

---

## 관련 위키 영역

- LLM/AI 개념은 [[02.wiki/index#Concepts (LLM/AI)|위키 Concepts 섹션]] 참조
- LLM 에이전트·도구는 entities/ 참조
- SE 관련 책 노트는 [[02.wiki/reading/index]] 참조
