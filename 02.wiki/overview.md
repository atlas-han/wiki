---
title: Overview
type: overview
tags: [meta, synthesis]
created: 2026-05-25
updated: 2026-06-27
sources: []
---

# Overview

이 페이지는 위키 전체의 **상위 합성(high-level synthesis)** 입니다. 새 소스가 들어올 때마다 LLM이 전체 그림이 어떻게 변하는지 한 문장씩 누적합니다.

## 위키의 목적

**LLM 생태계** 에 대한 개인 지식 베이스. 논문·블로그·강의·팟캐스트·릴리스 노트를 흡수하면서 모델·인물·조직·기법·아키텍처에 대한 누적적 이해를 구축합니다. 범위 정의는 [[CLAUDE#8. 도메인: LLM 생태계]] 참조.

## 현재 상태

[[anthropic|Anthropic]] 도메인이 큰 축으로 자리 잡는 중. 두 개의 큰 hub가 형성됨:
1. **사이버보안·dual-use** — [[project-glasswing]], [[ai-vulnerability-discovery]], [[coordinated-vulnerability-disclosure]] 라인.
2. **Agent harness 설계** — [[agent-harness-design]]을 허브로, Anthropic Engineering Blog 3편 연작([[anthropic-claude-code-auto-mode]], [[anthropic-harness-design-long-running-apps]], [[anthropic-managed-agents]])이 동시 ingest. 핵심 메시지: *"harnesses encode assumptions about what the model can't do — those assumptions go stale."* Sonnet 4.5 → Opus 4.5 → Opus 4.6 진화에 따라 컴포넌트(context reset, sprint construct)가 dead weight가 된 구체적 사례 확보. 같은 영역의 **커뮤니티 대중화 프레이밍**으로 [[harness-engineering]]([[tech-bridge-harness-engineering]])이 합류 — AI Layer 6요소 + *"every mistake becomes a rule"* + [[ralph-wiggum-method|Ralph Loop]] 다중 세션 오케스트레이션. 이제 그 진화 루프를 **모델 스스로 자동화**하는 [[self-harness|Self-Harness]]([[self-harness-paper]], [[shanghai-ai-lab|Shanghai AI Lab]])가 합류 — 고정 모델이 자기 트레이스로 자기 하니스를 propose→validate→accept. 본 위키 첫 **중국 lab + 비-Anthropic 모델군**([[minimax-m2-5]]·[[qwen3-5]]·[[glm-5]]) 진입.

[[andrej-karpathy|Karpathy]]의 [[llm-wiki-pattern]] 글이 이 vault 자체의 헌장. 두 흐름이 *"knowledge base 형태의 harness"* 라는 시각으로 연결됨.

## 핵심 질문 (열린 채로 두기)

위키가 답을 찾아갈 큰 질문들. 새 소스를 흡수할 때마다 이 질문들과 어떻게 연결되는지 고려하고, 새로운 질문이 떠오르면 추가합니다.

### 모델·아키텍처
- 현재 frontier 모델들(GPT, Claude, Gemini, Grok 등) 사이의 핵심 차별점은 무엇이고, 어떻게 수렴/분화하고 있는가?
- Transformer 이후의 아키텍처 후보(SSM, Mamba, diffusion LM 등)는 어디까지 왔는가?
- MoE는 dense 모델 대비 어디서 우위·열위가 명확한가?

### 학습·데이터
- Pre-training scaling은 어디서 한계에 부딪치고 있는가? (데이터, 컴퓨트, 알고리즘)
- Post-training (RLHF/DPO/GRPO/...)이 모델 capability에 기여하는 비중은 얼마나 커졌나?
- Synthetic data의 신뢰 가능한 사용법은 무엇인가?

### 추론·에이전트
- Test-time compute (reasoning, search)는 어떤 태스크에서 가장 큰 이득을 주는가?
- 에이전트 프레임워크들(Claude Code, Cursor, Devin 등)의 설계 패턴은 어디로 수렴하고 있는가? ([[agent-harness-design]])
- 도구 사용·MCP·메모리는 어떻게 표준화되고 있는가?
- *Harness가 인코딩한 가정*이 모델 발전에 따라 어디서 무너지는가? (예: [[context-anxiety]], sprint construct)
- 에이전트 안전 게이트(예: [[transcript-classifier]])는 어디까지 인간 승인을 대체할 수 있는가?

### 평가·정렬
- 현재 벤치마크가 실제 capability를 얼마나 반영하는가? Saturation된 것들은?
- Alignment·interpretability 연구의 실용적 진전은?

### 생태계·전략
- OpenAI / Anthropic / Google / Meta / xAI / 중국 lab들의 전략적 포지셔닝은?
- Open vs. closed 모델의 격차는 줄어들고 있는가, 벌어지고 있는가?

## 진화 로그 (요약)

새 소스마다 한 줄씩 누적:

- *2026-06-27*: [[refactoring-guru-ko-design-patterns|Refactoring.Guru 한국어 디자인 패턴]] ingest — 보조 도메인(소프트웨어 엔지니어링)에 [[design-patterns]] 허브와 GoF 패턴 22개 개별 페이지 추가. 생성/구조/행동 분류를 통해 객체 생성 책임, 객체 조합, 협력 흐름의 변경 축을 정리.
- *2026-05-25*: 위키 초기화 + Karpathy의 LLM Wiki gist를 첫 소스로 ingest, 패턴을 self-document.
- *2026-05-25*: Anthropic Project Glasswing 첫 업데이트 ingest. AI 취약점 발견의 산업 규모 실증, frontier 모델 capability 비교 baseline 형성.
- *2026-05-25*: Anthropic Engineering Blog 3편 ingest (auto mode / harness design / managed agents). [[agent-harness-design]] 허브 형성, Sonnet 4.5 → Opus 4.6 진화에 따른 harness 컴포넌트 stale화의 구체적 사례 축적.
- *2026-05-25*: Lint 통과. 누락 개체 4종 페이지화 — [[sutton-bitter-lesson]]([[agent-harness-design]] 철학적 뿌리), [[memex]] + [[vannevar-bush]] ([[llm-wiki-pattern]]의 사상적 조상), [[model-context-protocol]] ([[brain-hands-decoupling]]의 hands 측 표준), [[ralph-wiggum-method]] (autonomous loop 패턴).
- *2026-05-25*: multica-ai의 CLAUDE.md 4원칙 ingest ([[multica-karpathy-skills-claude-md]]). LLM 코딩 행동 규약 layer 신설 — [[llm-coding-guidelines]] 허브 + [[surgical-edits]] / [[verifiable-goals]]. [[anthropic-claude-code-auto-mode|auto mode]]의 *권한 게이트*가 위험 차단이라면, 본 가이드라인은 *프롬프트*로 over-engineering·scope creep 차단 — 보완 layer.
- *2026-05-30*: Claude Code [[dynamic-workflows]] 발표 ingest ([[anthropic-dynamic-workflows]]). [[agent-harness-design]] 허브에 *"self-writing orchestration"* 진화 단계 추가 — 사람이 짠 고정 multi-agent가 아니라 Claude가 오케스트레이션 스크립트를 *동적 작성*해 10s~100s parallel subagent를 adversarial 수렴시킴. [[generator-evaluator-pattern]]의 오케스트레이션판 + [[managed-agents]] coordination-외부화의 제품 표면 구현. 신규 개체 [[jarred-sumner]]·[[bun]] (Zig→Rust 75만 줄 11일 사례).
- *2026-05-30*: [[lum1104-understand-anything|Understand-Anything]] ingest ([[lum1104]] 제작 [[claude-code]] 플러그인). 코드·문서를 [[code-knowledge-graph|지식 그래프]]로 변환 — [[tree-sitter-llm-hybrid|Tree-sitter+LLM 하이브리드]](구조=결정론·reproducible, 의미=LLM) + 멀티 에이전트 파이프라인(scanner/analyzer/reviewer, [[generator-evaluator-pattern]] 계열). **결정적 연결**: `/understand-knowledge`가 이 vault 같은 [[llm-wiki-pattern|Karpathy-pattern wiki]]를 직접 그래프화 — LLM Wiki(코드→마크다운)와 Code Knowledge Graph(코드→그래프)가 *"LLM이 유지하는 누적 인공물"* 사상으로 합류. 이 위키 자체가 그 도구의 입력이 될 수 있음.
- *2026-06-01*: [[james-ai-explorer-understand-anything|James AI Explorer 한국어 가이드(2026-05-28)]] ingest. Understand-Anything 의 **2차 소스** 첫 사례 — README 의 *"Graphs that teach"* 가 사용자 측에서 *"1시간 → 5분"* 시간 절감 프레임으로 재서술됨. 신규 정보: IDE/Sourcegraph 와의 포지셔닝 비교, 한국어 사용자 진입(`--language ko` + MIT 무료). 2차 소스에서 [[tree-sitter-llm-hybrid|핵심 분업 메시지]] 가 큰 손실 없이 도착 — 추상의 견고함 시그널.
- *2026-06-06*: [[actix-web-official-docs|actix-web 공식 문서]] 전체(33p) ingest — 위키 첫 **`docs` 소스타입** + 첫 본격 **SE 프레임워크 클러스터**. [[actix-web]] 허브 아래 [[actix-web-extractors|extractor]]·[[actix-web-http-server|HttpServer 워커 모델]]·[[actix-web-middleware|미들웨어]]·[[actix-web-routing|라우팅]]·[[actix-web-error-handling|에러]]·[[actix-web-testing|테스트]]·[[actix-web-databases|DB]] + [[actix-actor-model|actix actor 모델]](5p)을 `engineering/{patterns,systems}`에 구축. 핵심: actix-web은 [[tokio]] 위 async 프레임워크로 actor와 분리됨(*"largely unrelated"*), 시그니처는 타입 안전 extractor + `Responder` + `web::Data` 워커 공유 3축. LLM 도메인과 별개의 **보조 도메인(소프트웨어 엔지니어링)** 본격 확장 시작.
- *2026-06-14*: [[self-harness-paper|Self-Harness 논문]](arXiv 2606.09498, [[shanghai-ai-lab|Shanghai AI Lab]]) + 한국어 해설([[papanuvo-self-harness]]) ingest. [[agent-harness-design]]·[[harness-engineering]] 허브에 **세 번째 하니스 개선 패러다임** [[self-harness|Self-Harness]] 신설 — Human Engineering / Meta-Harness 대비, *고정 동일 모델이 자기 실행 트레이스로 자기 하니스를 propose→validate→accept*. **핵심 합성**: harness-engineering의 *"every mistake becomes a rule"* System Evolution을 사람 손 떼고 자동화한 형태 + agent-harness-design의 *"가정 제거(단순화)"* 와 반대 방향(*실패→가정 추가=강화*)의 같은 진화 루프 + [[generator-evaluator-pattern]]의 propose/validate를 *하니스 계보*에 적용(평가자 튜닝 대신 결정론적 verifier+non-regressive gate). [[terminal-bench|Terminal-Bench-2.0]]에서 3개 모델 held-out +최대 21.4%p, *모델마다 다른* edit 채택으로 *"harness는 inherently model-specific"* 정량 입증. 본 위키 첫 **중국 lab + 비-Anthropic 모델군** 진입 ([[minimax-m2-5]]·[[qwen3-5]]·[[glm-5]]·[[terminal-bench]]·[[deepagents]]).
- *2026-06-03*: [[tech-bridge-harness-engineering|Tech Bridge 하네스 엔지니어링 영상]] ingest (첫 **영상 소스** + `youtube-transcript` 스킬 산출물). [[agent-harness-design]] 허브에 **커뮤니티 대중화 프레이밍** [[harness-engineering]] 신설 — context engineering의 2026 진화로서 ① 3계층(Base LLM→Tool Harness→AI Layer), ② AI Layer 6요소(rules/skills·MCP/codebase search/hooks/sub-agents/context docs), ③ *"every mistake becomes a rule"* System Evolution 마인드셋, ④ PIV + [[ralph-wiggum-method|Ralph Loop]] 다중 세션 오케스트레이션. **강조 대비 발견**: Anthropic 관점(agent-harness-design)은 *모델 발전 → 가정 제거*(단순화), 커뮤니티 관점(harness-engineering)은 *실패 → 가정 추가*(강화) — 같은 진화 루프의 양면. 신규 개체 [[geoff-huntley]](Ralph 제작자)·[[archon]](하네스 빌더)·[[tech-bridge]](채널). 인물명 모순(Jeffrey→Geoff Huntley) 통일.

---

전체 페이지 카탈로그는 [[02.wiki/index]], 시간순 작업 기록은 [[log]] 참조.
