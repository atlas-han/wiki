---
title: Overview
type: overview
tags: [meta, synthesis]
created: 2026-05-25
updated: 2026-09-02
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

- *2026-09-02*: [[tech-bridge]] `@TechBridge-KR` 09-01~09-02 업로드 롱폼 4편 — **에이전트를 운영 시스템으로 다루기 시작한 날.** 지금까지 이 위키의 에이전트 축은 *어떻게 더 많이 만들까*(도입·하네스·스킬)였는데, 이날 들어온 네 소스는 모두 **그 다음 질문**을 한다. (1) [[tech-bridge-agents-as-distributed-systems]] — [[salman-munaf]]/[[tiktok]]이 [[agent-distributed-systems]]를 신설. 에이전트가 **부작용**을 낼 수 있게 된 순간 그것은 모델 문제가 아니라 분산 시스템 문제이고, 처방은 전부 기존 도구다 — 멱등성 키, 서킷 브레이커, saga 보상, 최소 권한. 새로운 것은 **호출자가 비결정론적**이라는 점뿐. 가장 이식성 높은 한 줄은 *"타임아웃은 실패가 아니라 **알 수 없음**"*이고, 두 번째는 *"행동에 영향을 주는 맥락은 **상태**"* → 메모리를 **무효화 가능한 캐시**로 다루라는 것. (2) [[tech-bridge-claude-platform-agent-era]] — [[anthropic]] Claude Platform의 [[angela-jiang]]·[[katelyn-lesse]]가 [[token-roles]]를 신설하고 [[agent-harness-design]]의 정의를 확정한다(*"하네스는 **while 루프**"*, 그 위가 **메타 하네스 / 전략**). 핵심 아키텍처는 **수명 주기 분리** — 하네스는 내구성 서버에서 돌고 샌드박스는 작업 시점에 만들었다 지운다(샌드박스 기술이 애초에 *일시적* 용도라서). 이것이 [[managed-agents]] 3분할의 이유다. 그리고 토큰에 **advising / grading / dreaming** 역할을 준다 — grading은 `outcomes`라는 실제 기능이 되어 [[generator-evaluator-pattern]]을 플랫폼이 프로비저닝한다. (3) [[tech-bridge-trusted-throughput]] — [[mingsheng-hong]]/[[ironclad]]가 [[trusted-throughput]]을 신설. **토큰 지출 = LOC**라는 비유가 논증 전체를 지탱하고, 대시보드는 리더보드가 아니라 **연기 감지기**이며 조사할 신호는 *많이 쓰는 쪽이 아니라 안 쓰는 쪽*이다. 병목이 코드 생성에서 **리뷰와 CI**로 옮겨갔고, flaky 테스트가 재시도를 유발하므로 **토큰 낭비의 원인이 CI 품질**일 수 있다는 연결이 새롭다. (4) [[tech-bridge-signal-layer]] — [[lena-hall]]이 [[signal-layer]]를 신설하고 [[sutton-bitter-lesson]]의 유효 범위를 이 위키에서 가장 정밀하게 자른다: *"컴파일러는 무료 채점 도구, 테스트 스위트는 무료 채점 도구"* → **코드가 먼저 자동화된 것은 그것이 가장 검증하기 쉬웠기 때문**이고, 채점기가 없는 영역(문제 선택·신뢰)은 남는다. 부수적으로 [[dhh]]의 *taste 병목*을 정면 반박한다 — 넓은 취향은 학습 가능한 선호도다. **핵심 합성**: 세 소스가 서로를 모른 채 같은 결론에 도달했다 — 구매자([[ironclad]])와 공급자([[anthropic]])가 모두 **"토큰 단가는 잘못된 최적화 대상"**이라 말하고, [[signal-layer]]와 Claude Platform 팀이 모두 실행이 싸지면 남는 일은 **문제 선택과 정렬**이라고 말한다. 그리고 [[agent-distributed-systems]]와 [[token-roles]] 사이에는 순서가 있다 — 기본 루프의 신뢰성이 풀려야 전략 계층이 열린다(*"가장 기본적인 내용들이 어느 정도 이해 가능해졌기 때문"*). ⚠️ 네 소스 중 둘은 벤더/자사 대담이고, Sonnet+Opus advisor 평가·"12년→3개월"·Amazon 리더보드 일화는 모두 독립 검증이 없다.

- *2026-09-01*: [[tech-bridge]] `@TechBridge-KR` 08-31 업로드 롱폼 2편 — 위키가 **코딩 에이전트 밖**으로 두 걸음 나간 날. (1) [[tech-bridge-agentic-sites]] — [[carlos-sanchez]]/[[adobe]]가 [[agentic-sites]]를 신설. 사이트 전체를 재생성하는 대신 **사이트 전체를 RAG 코퍼스로** 써서 **블록만** 1~2초 안에 재조립한다. 브랜드 가이드라인이 환각 예산을 정하고, promptfoo 평가가 사이트별로 상주한다. 가장 이식성 높은 주장은 *"거대한 LLM이 필요하지 않습니다"* — 작업이 생성이 아니라 **블록 선택**이라 [[cerebras]]+[[gemma-4]]로 평균 1.1초(2위 4.6초). 문제를 좁혀 모델 요구를 낮춘 사례라 [[sutton-bitter-lesson]]의 제품 측 대비로 읽힌다. 위키 첫 **소비자 대면 생성 UI** 축. (2) [[tech-bridge-grokbot-agent-teams]] — [[cursor]]의 [[lauren-tan]]·[[roshan-sadanani]]가 [[persistent-agent-teams]]를 신설. 세션형 코딩 하니스와 달리 **정체성 + 자체 컴퓨터 + 코디네이터 봇 + 메시징 UI**를 가진 상시 봇 팀이고, 엔지니어의 일이 둘로 갈라진다 — 위로는 **에이전트 매니저**, 아래로는 규칙을 **린트·CI 실패로 인코딩**하는 **환경 관리인**([[verifiable-goals]] 재확인). 대중화 병목을 모델이 아니라 **UX**로 특정한 것이 [[agent-org-adoption]]의 네 번째 현장. 경제적 전제는 [[grok-4-6]]의 70.8% @ $2.81 vs Fable 5 Max 70.5% @ $17.32 — **가격이 곧 병렬성**이라 1인 봇 팀은 작업당 한 자릿수 달러에서만 성립한다. ⚠️ 두 소스 모두 벤더 발표이고, 후자의 Grok/Cursor/SpaceX 귀속은 소스 서술 그대로 기록했다.

- *2026-08-31*: [[tech-bridge]] `@TechBridge-KR` 08-30 업로드 롱폼 3편. (1) [[tech-bridge-andrew-ng-ai-opportunity]] — [[andrew-ng]]가 공포를 [[regulatory-capture]]로, 노동을 30–40%/60% complement로, 통상의 LLM을 [[cognitive-offloading]]으로 읽고 [[learnvector]]로 1:1 학습을 짠다. Gates편과 같은 채널의 반대 입구. (2) [[tech-bridge-dhh-agent-productivity]] — [[dhh]] 직결 테제. 승인 계층이 10x를 죽이고, 경로는 [[omarchy]]처럼 자기 5%. Figma/Amazon의 세 번째 현장. (3) [[tech-bridge-ai-native-skills]] — [[imad-touil]]이 know-how를 [[agent-skills]]에 두고 거버넌스 없는 스킬을 새 기술부채로. spec–plan–task는 SDLC의 한 increment.

- *2026-08-30*: [[tech-bridge-frontier-engineering]] — [[clare-liguori|Clare Liguori]](AWS)가 Amazon 사내 세 실험(Bedrock Mantle 6명/76일, Prime Video 10일 스프린트, Stores 50팀 배포 속도)으로 [[frontier-engineering]]을 정의. 도구([[kiro|Kiro]])가 아니라 5습관(컨텍스트·감속·먹이·의도 문서·로컬 mock)이 3x 미만 vs 4.5x를 가름. 2026 과제는 50→2,000팀, 새 병목은 의사결정. [[agent-org-adoption]](Figma)의 Amazon 자매 관측.

- *2026-08-29*: [[tech-bridge]] `@TechBridge-KR` 당일 롱폼 3편 ingest, 이후 en-orig 자막으로 본문 보강. (1) [[tech-bridge-spec-driven-development]] — 프롬프트를 메인 아티팩트에서 내리고 constitution/spec/plan/task를 Git history로. Build 2026 세션 플래너 MCP를 빈 레포에서 Spec Kit+Copilot으로 만드는 데모. (2) [[tech-bridge-figma-coding-agents]] — [[eyal-blum]]/[[figma]] 3막 곡선, 검증 피라미드, 계획 5x, 회의론자 로드맵, PR provenance. (3) [[tech-bridge-bill-gates-ai-warning]] — 코딩 임계점 이후 자율 규제 부정, 2년/4년 노동, human-reserved 직군.

- *2026-07-21*: [[charlychoi-claude-code-best-practices|Claude Code 공식 모범 사례 쉽게 이해하기]] ingest — Anthropic 공식 best practices의 한국어 2차 해설을 구조화해, [[verifiable-goals]]·[[llm-coding-guidelines]]·[[harness-engineering]]을 **목표 + 맥락 + verifier + permission + 독립 review**의 task contract로 합성. `CLAUDE.md`/Skills/Hooks/CLI·MCP를 context cost와 enforcement strength에 따라 배치하고, 복잡한 작업은 Explore→Plan→Implement→Verify→Review로 운영한다는 실무 checklist를 [[claude-code]]에 추가. ⚠️ 제품 command는 변동 가능하므로 공식 문서 재확인 필요.
- *2026-07-07*: [[xda-obsidian-cli-terminal-workflow|XDA Obsidian CLI workflow]] ingest — [[obsidian|Obsidian]]이 본 위키의 viewer를 넘어 terminal command surface로 확장되는 관점 추가. [[obsidian-cli-workflow]] 신설: `daily:append`·`search:context`·`read/create`가 quick capture, vault-aware search, [[claude-code|Claude Code]]류 agent automation의 마찰을 줄임. 단 desktop app 실행 의존성과 plugin command 노출 한계를 함께 기록.

- *2026-06-27*: [[openai-nextdoor-codex|How engineers at Nextdoor use Codex]] ingest (openai.com 케이스 스터디) — 위키 **첫 [[openai|OpenAI]]/[[codex|Codex]]/GPT 생태계** 진입(self-harness의 첫 중국 lab에 이은 두 번째 비-Anthropic 축). 핵심 개념 [[outcome-engineering]] 신설 — [[cory-dolphin|Cory Dolphin]]의 *"how 반복 프롬프팅 → 원하는 결과 정의·engineer"* 프레이밍을 [[verifiable-goals]](result=verifier)·[[sprint-contract]]·[[harness-engineering]]("harness for investigation")와 교차. Anthropic 계열 framing과 외부 관점이 *같은 원리의 다른 서술*로 합류. ⚠️ 벤더 마케팅 출처라 정량 근거 없는 조직·생산성 주장임을 명시, GPT‑5.4/5.5 스펙은 컷오프 이후로 소스 범위만 기록.
- *2026-06-27*: [[twelve-factor-app|The Twelve-Factor App]] ingest (12factor.net, [[adam-wiggins|Adam Wiggins]]/[[heroku|Heroku]]) — 보조 도메인에 cloud-native 방법론 레퍼런스 추가. config-in-env·stateless process·dev/prod parity 등 12원칙을 정리하고, [[pets-vs-cattle]]의 *무상태·disposability*를 **앱 설계 레이어**로 연결(인프라 운영 ↔ 프로세스 설계의 같은 원칙). [[martin-fowler|Fowler]] 엔티티를 신설해 [[refactoring]](저서 *Refactoring*)과 12-factor(*PoEAA*·*Refactoring* 형식 차용)를 *"문제에 이름을 붙이는 공유 vocabulary"* 사상으로 묶음. ⚠️ raw 클리핑은 인트로만 캡처돼 12요소 본문은 표준 지식으로 보완.
- *2026-06-27*: [[refactoring-guru-refactoring|Refactoring.Guru Refactoring]] ingest — 보조 도메인에 [[refactoring]] 허브를 추가하고 [[technical-debt]]·[[code-smells]]·[[refactoring-techniques]]를 연결. Code smell 23개를 개별 진단 페이지로, refactoring technique 6개 family를 카탈로그 페이지로 정리해 설계 리뷰 vocabulary를 확장.
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
