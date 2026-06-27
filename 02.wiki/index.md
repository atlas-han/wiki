---
title: Index
type: overview
tags: [meta]
created: 2026-05-25
updated: 2026-06-27
---

# Index

이 위키의 모든 페이지 카탈로그. LLM이 ingest·query·lint마다 갱신합니다.

> 형식: `- [[slug]] — 한 줄 요약`

## Overview

- [[overview]] — LLM·AI 생태계에 대한 high-level 합성 (위키 전체의 도입부)

---

## Entities

### Persons
- [[andrej-karpathy]] — AI 연구자·교육자, [[llm-wiki-pattern]] 원안 저자
- [[geoff-huntley]] — [[ralph-wiggum-method|Ralph]] 자율 루프 패턴 명명·정리 (ghuntley.com)
- [[jarred-sumner]] — [[bun|Bun]] 제작자, [[dynamic-workflows]]로 Zig→Rust 포팅 사례
- [[lum1104]] — [[understand-anything|Understand-Anything]] 제작자
- [[vannevar-bush]] — 1945년 [[memex]] 비전 제시 (As We May Think)

### Organizations
- [[anthropic]] — Claude 모델 패밀리 개발사, AI 안전 연구 lab
- [[tech-bridge]] — 영어권 AI 엔지니어링 영상에 한국어 자막을 붙여 재배포하는 YouTube 채널
- [[cloudflare]] — 클라우드 인프라·보안 회사, [[project-glasswing]] 파트너
- [[mozilla]] — Firefox 개발 오픈소스 비영리, [[project-glasswing]] 파트너
- [[multica-ai]] — GitHub org, `andrej-karpathy-skills` repo로 [[claude-code]] CLAUDE.md 4원칙 공개
- [[uk-aisi]] — UK AI Security Institute, frontier 모델 보안 평가 정부 기관
- [[shanghai-ai-lab]] — 상하이 AI 연구소, [[self-harness]] 논문 발표 (본 위키 첫 중국 lab)

### Models
- [[claude-mythos-preview]] — Anthropic 비공개 차세대급 모델, 사이버보안 capability frontier
- [[claude-opus-4-7]] — Anthropic 현 공개 플래그십
- [[claude-opus-4-6]] — Anthropic 이전 세대 플래그십, harness 단순화·classifier 가능케 한 모델
- [[claude-opus-4-5]] — Opus 4.6 직전 세대, harness 실험의 메인 모델
- [[claude-sonnet-4-6]] — Sonnet 4.6, [[transcript-classifier]] 백본
- [[claude-sonnet-4-5]] — Sonnet 4.5, [[context-anxiety]] 두드러진 모델
- [[minimax-m2-5]] — MiniMax M2.5, [[self-harness]] 실험 base 모델 (held-out 40.5→61.9%)
- [[qwen3-5]] — Qwen3.5-35B-A3B (MoE), [[self-harness]] 실험서 최대 상대 개선 (held-in +138%)
- [[glm-5]] — GLM-5, [[self-harness]] 실험 base 모델 (held-out 42.9→57.1%)

### Products
- [[claude-code]] — Anthropic 공식 coding agent CLI ([[anthropic-claude-code-auto-mode|auto mode]] + [[dynamic-workflows]] 신규)
- [[managed-agents]] — Claude Platform의 호스티드 meta-harness
- [[project-glasswing]] — Anthropic ~50개 파트너 협업 사이버보안 이니셔티브

### Tools
- [[archon]] — 오픈소스 하네스 빌더, [[ralph-wiggum-method|Ralph Loop]]류를 커스텀 구축 ([[harness-engineering]])
- [[claude-agent-sdk]] — Anthropic 에이전트 빌딩 SDK
- [[bun]] — JS/TS 런타임·툴킷, [[dynamic-workflows]]로 Zig→Rust 재작성 (99.8% 테스트 통과, 11일)
- [[playwright-mcp]] — 브라우저 자동화 MCP 서버, evaluator agent의 QA 채널
- [[obsidian]] — 본 위키의 사용자 측 뷰어
- [[understand-anything]] — 코드·wiki를 지식 그래프로 만드는 [[claude-code]] 플러그인 (멀티 에이전트, sources: 2)
- [[tree-sitter]] — 소스를 concrete syntax tree로 파싱하는 결정론적 incremental 파서
- [[actix-web]] — Rust 비동기 웹 프레임워크 (extractor·미들웨어·멀티스레드 HttpServer), actix-web 문서 허브 (sources: 1)
- [[actix-actor-framework]] — actix actor 모델 런타임, [[actix-web]]의 역사적 기반 (현재는 분리)
- [[tokio]] — Rust 표준 async 런타임, [[actix-web]]·[[actix-actor-framework]]가 그 위에서 동작
- [[serde]] — Rust 직렬화 프레임워크, [[actix-web-extractors|actix-web extractor]]가 의존
- [[terminal-bench]] — 컨테이너 터미널 agentic 벤치마크 (결정론적 verifier), [[self-harness]] 평가대
- [[deepagents]] — LangChain 에이전트 SDK, [[self-harness]]의 최소 초기 하니스 토대

---

## Concepts (LLM/AI)

### Techniques
- [[prompt-injection]] — 외부 콘텐츠가 에이전트를 hijack하는 공격, Anthropic의 2-layer 방어
- [[context-resets-and-compaction]] — 장기 task에서 context window 한계를 다루는 두 전략 + Managed Agents의 third way
- [[context-engineering]] — context window를 무엇을·어떻게 채우는가의 설계 영역

### Architectures
- [[brain-hands-decoupling]] — Claude+harness와 sandbox/tool을 좁은 인터페이스로 분리하는 설계 원칙

### Theories
- [[sutton-bitter-lesson]] — *"general methods that leverage computation"* 이 결국 이긴다 (Sutton, 2019)
- [[memex]] — Vannevar Bush 1945년 비전, [[llm-wiki-pattern]]의 사상적 조상
- [[agentic-misbehavior]] — 에이전트가 위험 action을 취하는 4가지 원인 (overeager / honest mistake / prompt injection / misaligned)
- [[context-anxiety]] — context limit이 가까워졌다고 *느끼면* 조기 마무리하는 모델 행동

### Patterns
- [[agent-harness-design]] — LLM 에이전트 스캐폴딩 설계 영역 (Anthropic 연작 허브)
- [[harness-engineering]] — 모델 wrapper 전체 설계 (3계층·AI Layer 6요소·System Evolution·오케스트레이션), context engineering의 2026 진화 (커뮤니티 프레이밍, sources: 1)
- [[self-harness]] — 고정 모델이 자기 하니스를 propose→validate→accept로 스스로 개선 (Shanghai AI Lab, Terminal-Bench-2.0, sources: 2)
- [[dynamic-workflows]] — Claude가 오케스트레이션 스크립트를 동적 작성, 10s~100s parallel subagent 수렴 (Claude Code, sources: 1)
- [[ultracode]] — effort=xhigh + workflow 자동 판단을 묶은 Claude Code 세팅
- [[generator-evaluator-pattern]] — GAN-스타일 생성기·평가기 분리 다중 에이전트
- [[sprint-contract]] — 작업 시작 전 generator·evaluator가 "done의 정의"를 합의
- [[transcript-classifier]] — Claude Code auto mode의 LLM-기반 권한 게이트
- [[deny-and-continue]] — 권한 차단 시 세션을 끊지 않는 UX 패턴
- [[ralph-wiggum-method]] — `while :; do cat PROMPT.md | claude-code ; done` 자율 루프 (Geoff Huntley)
- [[model-context-protocol]] — AI 앱이 외부 시스템에 붙는 오픈 표준 ("USB-C for AI")
- [[llm-wiki-pattern]] — LLM이 점진적으로 유지하는 마크다운 지식 베이스 패턴 (sources: 1)
- [[code-knowledge-graph]] — 코드·문서를 노드·엣지 그래프로 만들어 *보며* 이해하는 패턴 (sources: 2)
- [[ai-vulnerability-discovery]] — LLM으로 코드베이스에서 보안 취약점을 발견·exploit 검증하는 패턴 (sources: 1)
- [[coordinated-vulnerability-disclosure]] — 90/45일 윈도우 기반 표준 취약점 공개 프로세스 (sources: 1)
- [[llm-coding-guidelines]] — LLM 코딩 어시스턴트용 CLAUDE.md 4원칙 (Think / Simplicity / Surgical / Goal-Driven)
- [[surgical-edits]] — *"Every changed line should trace directly to the user's request"* — 외과 수술적 코드 수정 원칙
- [[verifiable-goals]] — 모호한 task를 *test → pass* 형식의 검증 가능한 goal로 변환

---

## Engineering (소프트웨어 엔지니어링)

→ 전체 목록은 [[02.wiki/engineering/index]] 참조

### Systems
- [[actix-web-http-server]] — actix-web `HttpServer` 워커 모델·TLS/HTTP2·graceful shutdown·정적 파일
- [[actix-web-connection-lifecycle]] — actix-web Accept/Worker/Dispatcher 루프 (내부 동작 다이어그램)
- [[actix-arbiter]] — actix actor의 단일 스레드 이벤트 루프(`System`)
- [[actix-sync-arbiter]] — CPU-bound 작업용 동기 actor 스레드 풀

### Patterns
- [[pets-vs-cattle]] — 인프라 일반 원칙, [[brain-hands-decoupling]]의 사상적 출처
- [[tree-sitter-llm-hybrid]] — 결정론적 파서(Tree-sitter) + LLM 분업의 코드 분석 패턴
- [[design-patterns]] — Refactoring.Guru 한국어 기준 GoF 디자인 패턴 22개 허브.
- [[refactoring]] — behavior를 유지하면서 내부 구조를 개선하는 작은 변경들의 연속.
- [[technical-debt]] — 빠른 delivery를 위해 미룬 구조 개선이 이후 변경 비용의 이자로 돌아오는 상태.
- [[code-smells]] — 리팩터링 후보를 찾는 진단 vocabulary(23개 smell).
- [[refactoring-techniques]] — behavior-preserving 구조 변경 technique family 허브(6개 family, 66+ technique).
- [[design-pattern-factory-method]] · [[design-pattern-abstract-factory]] · [[design-pattern-builder]] · [[design-pattern-prototype]] · [[design-pattern-singleton]] — 생성 패턴.
- [[design-pattern-adapter]] · [[design-pattern-bridge]] · [[design-pattern-composite]] · [[design-pattern-decorator]] · [[design-pattern-facade]] · [[design-pattern-flyweight]] · [[design-pattern-proxy]] — 구조 패턴.
- [[design-pattern-chain-of-responsibility]] · [[design-pattern-command]] · [[design-pattern-iterator]] · [[design-pattern-mediator]] · [[design-pattern-memento]] · [[design-pattern-observer]] · [[design-pattern-state]] · [[design-pattern-strategy]] · [[design-pattern-template-method]] · [[design-pattern-visitor]] — 행동 패턴.
- [[actix-web-extractors]] — actix-web `FromRequest` 타입 안전 요청 추출 (Path/Query/Json/Form/Data)
- [[actix-web-handlers-responders]] — actix-web 핸들러 시그니처·`Responder` trait·스트리밍 응답
- [[actix-web-application-state]] — actix-web `web::Data` 공유 상태 + 워커 클로저 함정
- [[actix-web-routing]] — actix-web URL dispatch·scope·guard·URL 생성
- [[actix-web-middleware]] — actix-web `Transform`+`Service` 미들웨어·CORS·세션
- [[actix-web-error-handling]] — actix-web `ResponseError` 커스텀 에러 응답
- [[actix-web-databases]] — actix-web `web::block`(동기 Diesel)·async ORM·r2d2 풀
- [[actix-web-testing]] — actix-web `TestRequest`·`init_service` 통합 테스트
- [[actix-web-websockets]] — actix-web `actix-ws` WebSocket 처리
- [[actix-actor-model]] — actix `Actor` trait·lifecycle·`Handler`/`Message`
- [[actix-actor-address]] — actix `Addr`/`Recipient`·send/do_send/try_send
- [[actix-actor-context]] — actix `Context`·mailbox 용량

### Tools
→ [[tree-sitter]] · [[understand-anything]] (entities/에 위치)

---

## Reading (독서)

→ 독서 대시보드는 [[02.wiki/reading/index]] 참조

### Currently Reading
*(아직 없음)*

### To Read
- [[martian-special-edition]] — 앤디 위어의 화성 조난 하드 SF 소설, 영화 〈마션〉 원작 (to-read)

### Completed
*(아직 없음)*

---

## TIL (Today I Learned)

→ 전체 목록은 [[02.wiki/til/index]] 참조

- [[2026-06-27-conversation-positioning]] — 대화에서 주도권을 잃지 않는 표현과 반응형 표현의 차이

---

## Sources

- [[karpathy-llm-wiki-gist]] — Karpathy가 제시한 LLM Wiki 패턴의 원문 gist (2026)
- [[anthropic-project-glasswing-update-2026-05]] — Anthropic의 Project Glasswing 첫 공개 업데이트 (2026-05-22)
- [[anthropic-claude-code-auto-mode]] — Claude Code auto mode 설계·평가 (Anthropic Engineering, 2026)
- [[anthropic-harness-design-long-running-apps]] — GAN-스타일 generator/evaluator 다중 에이전트 (Anthropic Labs, 2026)
- [[anthropic-managed-agents]] — Managed Agents 메타-하네스 설계 (Anthropic Engineering, 2026)
- [[anthropic-dynamic-workflows]] — Claude Code dynamic workflows 발표 (claude.com, 2026-05-28)
- [[multica-karpathy-skills-claude-md]] — multica-ai의 Claude Code용 CLAUDE.md 4원칙 헤더 (2026)
- [[lum1104-understand-anything]] — Understand-Anything README: 코드를 지식 그래프로 (GitHub, 2026)
- [[james-ai-explorer-understand-anything]] — Understand-Anything 한국어 사용자 가이드 (제임스의 AI 실전 노트, 2026-05-28)
- [[tech-bridge-harness-engineering]] — 하네스 엔지니어링 강연 영상, 한국어 자막 ([[tech-bridge|Tech Bridge]], 2026-06-03)
- [[actix-web-official-docs]] — actix-web 공식 문서 전체 (actix.rs/docs, docs 33p, 2026-06-06)
- [[kyobo-martian-special-edition]] — 교보문고 《마션(스페셜 에디션)》 상품 정보와 공개 소개 요약 (2021)
- [[self-harness-paper]] — "Self-Harness: Harnesses That Improve Themselves" (Shanghai AI Lab, arXiv 2606.09498, 2026)
- [[papanuvo-self-harness]] — Self-Harness 한국어 해설 (파파누보, tistory, 2026-06-12)
- [[refactoring-guru-ko-design-patterns]] — Refactoring.Guru 한국어 Design Patterns 카탈로그(GoF 22개 패턴, 2026-06-27 ingest)
- [[refactoring-guru-refactoring]] — Refactoring.Guru Refactoring 카탈로그(code smells 23개 + technique families 6개, 2026-06-27 ingest)

---

## 통계

- 총 페이지 수: 161 (log 포함; Refactoring.Guru refactoring ingest로 source 1 + engineering pages 33 추가)
- 마지막 TIL: 2026-06-27 ([[2026-06-27-conversation-positioning|대화 위치]])
- 마지막 ingest: 2026-06-27 ([[refactoring-guru-refactoring|Refactoring.Guru Refactoring]] — [[refactoring]] 허브 + [[code-smells]] 23개 + [[refactoring-techniques]] family 6개)
- 마지막 lint: 2026-06-03 (70 페이지 점검: 미해결 모순 0·고아 0·dangling 0·index 동기화 100%·kebab-case 100%; updated drift 3건 + source-type enum 2건 정규화)
- 마지막 갱신: 2026-06-27
