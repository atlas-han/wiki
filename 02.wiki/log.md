---
title: Log
type: overview
tags: [meta]
created: 2026-05-25
updated: 2026-08-29
---

# Log

위키에 대한 모든 작업의 시간순 기록 (append-only). 각 항목은 `## [YYYY-MM-DD] <op> | <description>` 형식.

지원 op: `ingest`, `query`, `lint`, `meta` (스키마·구조 변경)

## [2026-05-25] meta | LLM-WIKI 초기화
- Karpathy의 [LLM Wiki 패턴 gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)를 참조하여 구조 생성
- 디렉토리 레이어 확립: `raw/`, `wiki/`, `CLAUDE.md`
- 카테고리 정의: entities, concepts, sources
- 인덱스·로그·overview 초기 페이지 작성
- 도메인 초기 설정: LLM·AI 생태계 (사용 시작 시 사용자와 협의해 조정)

## [2026-05-25] ingest | Karpathy — LLM Wiki (Gist)
- 소스 페이지: [[karpathy-llm-wiki-gist]]
- 신규 개념: [[llm-wiki-pattern]]
- 영향 받은 페이지: index, overview, log
- 비고: 위키의 첫 시범 ingest. 패턴을 위키 자체에 self-document하는 의미.

## [2026-05-25] meta | 도메인 확정 + Welcome.md 정리
- 도메인을 **LLM 생태계**로 확정 (CLAUDE.md §8 갱신)
- 다루는/다루지 않는 범위 명시
- overview.md의 placeholder 질문을 실제 LLM 생태계 질문으로 교체 (모델·학습·추론·평가·생태계 5개 카테고리)
- Obsidian 기본 Welcome.md 삭제

## [2026-05-25] meta | 소프트웨어 엔지니어 맞춤 구조 확장
- 새 영역 추가: `wiki/engineering/` (SE 개념: systems, patterns, tools)
- 새 영역 추가: `wiki/reading/` (독서 관리: to-read, reading, completed, dnf)
- 새 영역 추가: `wiki/til/` (Today I Learned 빠른 메모)
- `raw/` 하위 분류 추가: `papers/`, `articles/`, `books/`
- CLAUDE.md 전면 개정: reading frontmatter 스키마, reading/til 작업 정의 추가
- README.md 업데이트: 커맨드 예시 테이블 추가
- `wiki/index.md` 업데이트: Engineering, Reading, TIL 섹션 추가

## [2026-05-25] ingest | Anthropic — Project Glasswing: An Initial Update
- 소스 페이지: [[anthropic-project-glasswing-update-2026-05]]
- 원문 캡처: `raw/articles/anthropic-project-glasswing-update-2026-05-22.md` (WebFetch가 저작권으로 verbatim 거부, 구조화 추출)
- 신규 entities: [[anthropic]], [[project-glasswing]], [[claude-mythos-preview]], [[claude-opus-4-7]], [[claude-opus-4-6]], [[cloudflare]], [[mozilla]], [[uk-aisi]] (총 8개)
- 신규 concepts: [[ai-vulnerability-discovery]], [[coordinated-vulnerability-disclosure]] (총 2개)
- 갱신: index, overview, log
- 영향 페이지 수: 14
- 핵심 시그널:
  - AI 취약점 발견의 산업 규모 실증 (10,000+ high/critical, 90.6% true positive)
  - frontier 모델 capability 비교축 정착 (Mythos Preview vs Opus 4.7 vs Opus 4.6, 약 10배 격차)
  - dual-use 정책: Mythos-class 일반 공개 보류 (Anthropic 입장)
- stub 보류: Oracle, Microsoft, Palo Alto Networks, Cisco, wolfSSL, XBOW, OSSF, NIST, UK NCSC, ExploitBench, ExploitGym (향후 관련 ingest 시 페이지화 고려)

## [2026-05-25] ingest | Anthropic — Claude Code auto mode: a safer way to skip permissions
- 소스 페이지: [[anthropic-claude-code-auto-mode]]
- 신규 entities: [[claude-code]], [[claude-sonnet-4-6]]
- 신규 concepts: [[transcript-classifier]], [[prompt-injection]], [[agentic-misbehavior]], [[deny-and-continue]]
- 신규 concepts (이번 배치 공통, 허브): [[agent-harness-design]]
- 갱신 entities: [[anthropic]] (auto mode 라인 추가), [[claude-opus-4-6]] (system card 인용 추가)
- 핵심 시그널:
  - Manual prompt vs sandbox vs `--dangerously-skip-permissions` 사이의 4번째 옵션
  - Classifier가 reasoning-blind by design — agent의 prose를 strip하여 정당화 방어
  - Real overeager FNR 17% ("honest number"), real traffic FPR 0.4%
- 영향 페이지 수 (이번 배치 공통 계산은 아래 묶음 ingest 참조)

## [2026-05-25] ingest | Anthropic — Harness design for long-running application development
- 소스 페이지: [[anthropic-harness-design-long-running-apps]]
- 신규 entities: [[claude-agent-sdk]], [[playwright-mcp]], [[claude-opus-4-5]], [[claude-sonnet-4-5]]
- 신규 concepts: [[generator-evaluator-pattern]], [[sprint-contract]], [[context-anxiety]], [[context-resets-and-compaction]]
- 갱신 concepts: [[agent-harness-design]] (frontend + 풀스택 사례 흡수)
- 갱신 entities: [[claude-opus-4-6]] (sprint construct·context reset 제거 사례 추가)
- 핵심 시그널:
  - GAN-스타일 generator/evaluator가 subjective 영역(디자인)에 작동
  - Sprint contract = high-level spec과 testable 구현 사이의 다리
  - Opus 4.6 도착 후 sprint construct·context reset이 dead weight화 → harness simplification
- 비고: Karpathy 글의 *"knowledge base harness"* 시각과 동일 사상

## [2026-05-25] ingest | Anthropic — Scaling Managed Agents: Decoupling the brain from the hands
- 소스 페이지: [[anthropic-managed-agents]]
- 신규 entities: [[managed-agents]]
- 신규 concepts: [[brain-hands-decoupling]], [[context-engineering]]
- 신규 engineering: [[pets-vs-cattle]]
- 갱신: [[agent-harness-design]] (meta-harness 시각), [[context-resets-and-compaction]] (session 외부화 third-way 추가)
- 핵심 시그널:
  - OS-style 가상화: session / harness / sandbox 세 추상
  - Brain을 컨테이너에서 빼서 p50 TTFT ~60%↓, p95 90%+↓
  - Token이 sandbox에 절대 안 들어감 — vault + MCP proxy / Git wire-in 패턴
- 영향 페이지 수 (배치 합산): 본 3편 배치로 신규 21개 페이지 + 기존 4개 갱신 = 25개

## [2026-05-25] ingest | Karpathy gist 보완 갱신
- 기존 [[karpathy-llm-wiki-gist]]의 "stub" 항목들이 이번 배치 ingest로 entity 페이지화됨
- 신규 entities: [[andrej-karpathy]], [[obsidian]]
- 갱신: [[llm-wiki-pattern]] ([[andrej-karpathy]], [[obsidian]], [[claude-code]] 위키링크 + [[agent-harness-design]] 관련성 추가)

## [2026-05-25] lint | 1차 건강 점검 (43 → 48 페이지)
- 점검 범위: 전체 페이지 43, 모든 frontmatter·위키링크·index 동기화·모순·파일명·reading 상태
- ✅ 통과: 고아 0, 모순 0, frontmatter 결손 0, index 동기화 OK, kebab-case 100%
- ⚠️ 발견: 깨진 위키링크 2건 + 누락 개체 4종
- 자동 수정: `engineering/index.md`의 `[[concepts/]]` → `[[02.wiki/index#Concepts (LLM/AI)|위키 Concepts 섹션]]`
- 누락 개체 페이지화 (사용자 결정에 따라 충실히 작성):
  - [[sutton-bitter-lesson]] (concept/theory) — Rich Sutton 2019 에세이, agent-harness-design 철학의 사상적 뿌리
  - [[vannevar-bush]] (entity/person) + [[memex]] (concept/theory) — llm-wiki-pattern의 1945년 조상
  - [[model-context-protocol]] (concept/pattern) — Anthropic 주도 오픈 표준, brain-hands-decoupling의 hands 측 구체 구현체
  - [[ralph-wiggum-method]] (concept/pattern) — Geoff Huntley의 `while :; do cat PROMPT.md | claude-code ; done` 자율 루프
- Cross-link 승격: karpathy-llm-wiki-gist·andrej-karpathy·llm-wiki-pattern·playwright-mcp·agent-harness-design·brain-hands-decoupling에서 평문 멘션을 위키링크로
- index.md·overview.md 갱신, lint-report-2026-05-25.md 삭제
- 영향 페이지 수: 신규 5 + 갱신 약 10 = 15

## [2026-05-25] query | llm-wiki 패턴이 뭐야?
- 참조 페이지: [[llm-wiki-pattern]], [[karpathy-llm-wiki-gist]], [[memex]], [[andrej-karpathy]]
- 답변: 3-레이어 아키텍처(raw/wiki/schema) + 3작업(ingest/query/lint) + Memex 계보 + bookkeeping 비용 0 논거 정리
- Archive 없음: 기존 [[llm-wiki-pattern]] 페이지에 이미 모두 담긴 내용의 재구성

## [2026-05-25] ingest | multica-ai — andrej-karpathy-skills · CLAUDE.md
- 소스 페이지: [[multica-karpathy-skills-claude-md]]
- 원문 캡처: `01.raw/articles/2026-05-25_claude-md-behavioral-guidelines.md` (GitHub raw)
- 신규 entities: [[multica-ai]] (org)
- 신규 concepts: [[llm-coding-guidelines]] (hub), [[surgical-edits]], [[verifiable-goals]]
- 갱신 entities: [[andrej-karpathy]] (repo 이름 차용 사실 추가), [[claude-code]] (system prompt 가이드라인 layer 추가)
- 갱신 concepts (related 링크): [[sprint-contract]] (← verifiable-goals), [[ralph-wiggum-method]] (← verifiable-goals, llm-coding-guidelines)
- 갱신: index, overview, log
- 영향 페이지 수: 신규 5 + 갱신 5 = 10
- 핵심 시그널:
  - LLM 코딩 어시스턴트의 행동 규약 4원칙 (Think Before Coding / Simplicity First / Surgical Changes / Goal-Driven Execution)
  - 트레이드오프 명시: caution > speed bias
  - 효과 측정: diff 내 불필요 변경 감소, overcomplication 재작성 감소, 사전 질문 비중 증가
  - [[anthropic-claude-code-auto-mode|auto mode]] (권한 게이트)와 보완 layer — 본 가이드라인은 *선의의 과잉 행동* 차단
- 미해결: multica-ai 조직 정체성·운영자, Karpathy 본인 endorsement 여부, repo 내 다른 skill 파일

## [2026-05-30] ingest | Anthropic — Introducing dynamic workflows in Claude Code
- 소스 페이지: [[anthropic-dynamic-workflows]]
- 원문: `01.raw/articles/2026-05-30_Introducing dynamic workflows.md` (claude.com 블로그)
- 신규 entities: [[jarred-sumner]] (person), [[bun]] (tool)
- 신규 concepts: [[dynamic-workflows]] (허브), [[ultracode]]
- 갱신 entities: [[claude-code]] (dynamic workflows·ultracode 라인 추가), [[anthropic]] (agent 인프라 라인), [[managed-agents]] (coordination 외부화 cross-link)
- 갱신 concepts: [[agent-harness-design]] (self-writing orchestration 진화 단계 + related), [[generator-evaluator-pattern]] (오케스트레이션 차원 확장 + related)
- 갱신: index, overview, log
- 영향 페이지 수: 신규 5 + 갱신 7 = 12
- 핵심 시그널:
  - Claude가 오케스트레이션 스크립트를 *동적 작성* → 한 세션에서 10s~100s parallel subagent
  - adversarial 수렴(independent angle + refute until converge)이 단일 패스 초과 결과의 핵심
  - coordination이 대화 바깥 + resumable checkpoint (long-running 시간~일)
  - Bun Zig→Rust 포팅: 99.8% 테스트 통과, ~75만 줄 Rust, 11일 ([[jarred-sumner]])
  - 진입: 직접 요청 또는 `ultracode`(effort=xhigh + workflow 자동 판단), auto mode 권장
  - research preview, Max/Team/Enterprise + API/Bedrock/Vertex/Foundry, 토큰 소모 大
- 모순 처리: raw frontmatter `published: 2001-05-28` → 오타로 판단, 2026-05-28로 기록
- 미해결: Jarred Sumner/Bun 기본 프로필, dynamic workflows 내부 스케줄링·비용 모델 상세 (후속 글 예정)

## [2026-05-30] ingest | Lum1104/Understand-Anything — README
- 소스 페이지: [[lum1104-understand-anything]]
- 원문: `01.raw/articles/2026-05-30_Lum1104Understand-Anything ...md` (GitHub README)
- 신규 entities: [[understand-anything]] (tool), [[lum1104]] (person), [[tree-sitter]] (tool)
- 신규 concepts: [[code-knowledge-graph]] (pattern)
- 신규 engineering: [[tree-sitter-llm-hybrid]] (pattern)
- 갱신 concepts: [[llm-wiki-pattern]] (/understand-knowledge 그래프화 섹션 + related: code-knowledge-graph)
- 갱신 entities: [[claude-code]] (플러그인 생태계 라인 + sources)
- 갱신: [[02.wiki/engineering/index]], index, overview, log
- 영향 페이지 수: 신규 6 + 갱신 5 = 11
- 핵심 시그널:
  - 코드·문서 → 인터랙티브 [[code-knowledge-graph|지식 그래프]] (파일·함수·클래스·의존성=노드). *"Graphs that teach > graphs that impress."*
  - [[tree-sitter-llm-hybrid|Tree-sitter+LLM 하이브리드]]: 구조=결정론(reproducible·fingerprint 증분), 의미=LLM(요약·레이어·도메인·투어)
  - 멀티 에이전트 (5+2): project-scanner / file-analyzer(병렬) / architecture-analyzer / tour-builder / graph-reviewer + domain-analyzer · article-analyzer → [[generator-evaluator-pattern]] 계열
  - **이 위키와 직접 연결**: `/understand-knowledge`가 [[llm-wiki-pattern|Karpathy-pattern wiki]]를 force-directed 그래프+clustering으로 분석 (index.md wikilink 결정론적 파싱 후 LLM이 암묵 관계 발굴). 이 vault가 입력이 될 수 있음
  - 그래프=커밋 가능 JSON → 팀원 파이프라인 스킵 (온보딩·PR 리뷰·docs-as-code), 15종 플랫폼 지원
  - 이 환경에 `understand-anything` 플러그인 실제 설치됨 (/understand, /understand-knowledge 사용 가능)
- 강조점: 사용자 협의로 4관점 모두 반영 (위키 연결·아키텍처·도구 카탈로그·에이전트 패턴)
- 미해결: Lum1104 본명·소속, graph JSON 스키마 상세

## [2026-06-01] ingest | James AI Explorer — Understand-Anything 한국어 가이드 (2026-05-28)
- 소스 페이지: [[james-ai-explorer-understand-anything]]
- 원문 캡처: `01.raw/articles/2026-05-28_understand-anything-1hour-to-5min.md` (fornewchallenge.tistory.com, 의미 정리 형태)
- 신규 entities/concepts: 없음 (도구·인물·개념은 모두 2026-05-30 ingest 에서 페이지화 완료)
- 갱신: [[understand-anything]], [[lum1104]], [[tree-sitter]], [[code-knowledge-graph]], [[tree-sitter-llm-hybrid]] 의 sources 필드 + 본문 (2차 소스 시각 섹션 추가)
- 갱신: index (Sources 섹션 + 통계), overview (진화 로그 한 줄), log
- 영향 페이지 수: 신규 2 (raw + source) + 갱신 8 = 10
- 위치: Understand-Anything 의 **첫 2차 소스** — 동일 도구의 사용자 평가/번역
- 핵심 시그널:
  - 메시지 전달성: *"Graphs that teach > graphs that impress"* → *"1시간 → 5분"* 시간 절감 프레임으로 재서술. [[tree-sitter-llm-hybrid|핵심 분업]] 추상이 한국어 블로그에서도 큰 손실 없이 전달됨
  - 신규 정보: IDE 기본 기능·Sourcegraph 와의 포지셔닝 비교표 (README 부재 정보)
  - 한국어 사용자 진입 시그널: `--language ko` + MIT 무료 → [[lum1104]] 의 다국어 README 정책 효과 확인
  - 누락 (블로그가 다루지 않은 부분): `/understand-knowledge` LLM wiki 분석 기능, graph JSON 커밋 워크플로, 증분 업데이트
- 사용자 선호 기록: ingest 작업에서 가중치 묻는 AskUserQuestion 단계 생략 동의 → 메모리에 feedback 저장 (`feedback-skip-emphasis-question.md`)
- 모순 처리: 없음 (1차 소스와 일치)

## [2026-06-01] lint | 2차 건강 점검 (65 페이지)
- 점검 범위: `02.wiki/` 전체 65 페이지 — frontmatter / wikilink / index 동기화 / 파일명 / reading 상태 / frontmatter related-slug / mtime drift / 모순
- ✅ 통과: 고아 0, 모순 0, frontmatter 필수 필드 결손 0, index 동기화 100%, kebab-case 100%, reading 상태 일치 (페이지 없음)
- ⚠️ 발견: frontmatter dangling slug 1건 + mtime drift 1건 + scanner false-positive 5건(인라인 코드 안 `[[slug]]` placeholder, 실제 렌더링은 정상)
- 자동 수정 (2건):
  - [[managed-agents]] frontmatter: `sources` 에 `anthropic-dynamic-workflows` 추가, `updated` 2026-05-25 → 2026-06-01 (dynamic-workflows ingest 시 본문은 cross-link 추가됐으나 메타 누락이었음)
  - [[generator-evaluator-pattern]] frontmatter `related` 에서 dangling slug `self-evaluation-bias` 제거 (사용자 결정: option B — 1차 소스에 명시 인용 없는 placeholder 슬러그, 향후 명시 출처 등장 시 페이지화)
- False positive 확인: `02.wiki/{index,reading/index,engineering/index,til/index}.md` 의 `[[slug]]` / `[[YYYY-MM-DD-topic]]` 5건은 모두 `> 형식:` 안내 인라인 코드 (백틱 안에 위치) → Obsidian 렌더링상 wikilink 아님, 수정 불필요. 스캐너 휴리스틱 한계.
- 영향 페이지 수: 갱신 2 + log 갱신
- 결과: 위키 건강 매우 양호. 본질적 구조 깨짐 0, 본 lint 는 housekeeping pass.
- lint-report-2026-06-01.md 삭제

## [2026-06-03] ingest | Tech Bridge — 하네스 엔지니어링 (지금 최고의 에이전틱 엔지니어를 가르는 것)
- 소스: [[tech-bridge-harness-engineering]] (YouTube, https://youtu.be/-pqyzBxddyg, ~17분, source-type: **video** — 위키 첫 영상 소스)
- 원문 캡처: `01.raw/articles/2026-06-03_하네스 엔지니어링 - 지금 최고의 에이전틱 엔지니어를 가르는 것은 무엇일까요?.md` (`youtube-transcript` 스킬로 en-orig 자동자막 다운로드 → 사용자가 한국어 기술문서로 재구성)
- 사용자 협의: 개념 구조 = "신규 페이지 + 허브 연결", entity 범위 = "핵심만"(geoff-huntley·archon·tech-bridge) 선택
- 신규 (5): source [[tech-bridge-harness-engineering]] · concept [[harness-engineering]] · entity [[geoff-huntley]]·[[archon]]·[[tech-bridge]]
- 갱신 (6): [[agent-harness-design]](허브↔신규 상호참조 + 강조 대비) · [[context-engineering]](2026 진화 프레이밍 섹션) · [[ralph-wiggum-method]]("Ralph Loop" 프레이밍 + Geoff/Archon 링크) · overview(현재상태 + 진화로그) · index(persons/orgs/tools/patterns/sources + 통계) · log
- 영향 페이지 수: 신규 5 + 갱신 6 (+raw 1) = 12
- 핵심 합성:
  - [[harness-engineering]]은 [[agent-harness-design]]과 **동일 영역의 두 프레이밍** — Anthropic 관점(모델↑→가정 제거=단순화) vs 커뮤니티 관점(실패→가정 추가=강화). 같은 진화 루프의 양면으로 명시 연결.
  - [[context-engineering]] → harness engineering 진화의 차별점 = **control**(오케스트레이션·sub-agent) + **mindset**(*every mistake becomes a rule*).
  - 다중 세션 오케스트레이션(PIV + [[ralph-wiggum-method|Ralph Loop]])이 기존 [[dynamic-workflows]](모델이 오케스트레이션 동적 작성)와 대비 — 고정 자동화 vs 자기작성 자동화.
- 모순 처리: ⚠️ 인물명 "Jeffrey Huntley"(영상) → [[geoff-huntley|Geoff Huntley]](위키 표준, ghuntley.com)로 통일. source·concept·entity 3곳에 contradiction 표기.
- 범위 메모: Codex·Google Cloud Agent CLI·Cole Medin(발표자 추정)은 사용자 선택("핵심만")에 따라 entity 페이지 미생성, 인라인 언급으로만 처리.

## [2026-06-03] lint | 3차 건강 점검 (70 페이지)
- 점검 범위: `02.wiki/` 전체 70 페이지(67 unique slug) — 모순 / 고아 / dangling / 누락개체 / frontmatter / reading 상태 / index 동기화 / 파일명
- ✅ 통과: 고아 0, dangling 링크 0, index 양방향 동기화 0 불일치, kebab-case 100%, reading 상태(페이지 0), slug 충돌은 index 4개(정상)
- 모순: Huntley 이름(영상 "Jeffrey" ↔ 위키 "Geoff") 1건이 유일 — 직전 ingest에서 3곳(`sources/tech-bridge-harness-engineering`·`entities/geoff-huntley`·`concepts/ralph-wiggum-method`)에 `⚠️ Contradiction`으로 일관 문서화·해결됨. **미해결 모순 0.**
- 자동 수정 (사용자 동의):
  - **A. updated drift 3건**: [[index]]·[[log]]·[[overview]] frontmatter `updated` 2026-06-01 → 2026-06-03 (직전 ingest 때 본문만 수정, 메타 누락분 정정)
  - **B. source-type enum 정규화 2건**: [[anthropic-project-glasswing-update-2026-05]] `blog`→`article`, [[karpathy-llm-wiki-gist]] `gist`→`article` (CLAUDE.md §2.2 enum 일치, updated도 2026-06-03로 bump)
- 사용자 판단 — 보류 유지 (C): Cole Medin·Google Cloud Agent CLI·Codex는 entity 페이지화하지 않고 인라인 언급 유지 (향후 관련 소스 ingest 시 페이지화)
- false positive 확인: til/index `> 형식:` 안 `[[YYYY-MM-DD-topic]]`은 백틱 인라인 코드 → wikilink 아님(수정 불필요), 스캐너 휴리스틱 한계 (이전 lint와 동일)
- 영향 페이지 수: 갱신 5 (index·log·overview + source 2) + log 엔트리
- 결과: 위키 건강 양호. 본 lint는 housekeeping pass(구조 깨짐 0).
- lint-report-2026-06-03.md 삭제

## [2026-06-05] meta | Hermes Agent 공동관리 설정
- 로컬 경로 `/opt/data/wiki`에 GitHub repository `atlas-han/wiki` clone 완료.
- 활성 Hermes profile 환경에 `WIKI_PATH=/opt/data/wiki` 설정.
- `AGENTS.md` 신규 추가: Hermes 및 기타 agent가 세션 시작 시 `CLAUDE.md` → `02.wiki/index.md` → `02.wiki/log.md` 순서로 orient 하도록 명시.
- `README.md` 빠른 시작에 Hermes Agent 사용 및 기본 경로 안내 추가.
- 영향 페이지/파일: `AGENTS.md`, `README.md`, `02.wiki/log.md`.

## [2026-06-05] meta | Mnemosyne LLM-WIKI Steward Agent 추가
- 전담 Agent 이름을 **Mnemosyne**로 확정: 그리스 신화의 기억의 여신/티탄, Second Brain steward 역할에 맞춤.
- 신규 agent spec: `.agents/mnemosyne.md`.
- 운영 정책: 우선 단일 Steward Agent 체계 유지. ingest 규모·페이지 수·lint 부담·동시 작업 필요성이 커질 때만 specialist agent 추가.
- 미래 specialist 후보명 예약: Hermes(source ingest), Athena(research synthesis), Apollo(wiki librarian), Clio(reading/TIL), Themis(QA/lint).
- 로컬 Hermes profile scaffold 추가: `/opt/data/.hermes/profiles/mnemosyne/` (`WIKI_PATH=/opt/data/wiki`, role metadata). 현재 환경에는 `hermes` CLI binary가 없어 profile scaffold로 구성.
- 갱신: `AGENTS.md`에 Mnemosyne을 primary steward로 등록.

## [2026-06-06] meta | Remote rebase-first 편집 정책 추가
- 모든 LLM-WIKI 편집 전에 `/opt/data/wiki`에서 `git pull --rebase --autostash`를 실행하도록 운영 가이드 업데이트.
- 갱신: `AGENTS.md` First step / Editing policy, `CLAUDE.md` §3.0 공통 시작 절차, `.agents/mnemosyne.md` Default Operating Loop / Non-Negotiables.
- 목적: 원격 repository 최신 상태 위에서만 wiki 문서를 편집해 stale state 기반 수정과 충돌 위험을 줄임.

## [2026-06-06] meta | Mnemosyne Query Agent 추가
- 신규 query 전용 agent spec: `.agents/mnemosyne-query.md`.
- 신규 graphify helper: `scripts/wiki_graphify_query.py` — `02.wiki/`의 wikilink graph를 구성하고 query seed node + neighbor context를 생성.
- 신규 CLI wrapper: `/opt/data/bin/mnemosyne-query` — Hermes CLI가 있으면 `llm-wiki-query` profile로 graphified prompt를 전달하고, 없으면 현재 세션이 사용할 prompt/context 출력.
- 신규 profile scaffold: `/opt/data/.hermes/profiles/llm-wiki-query/`.
- 운영 원칙: 모든 LLM-WIKI query는 graphify를 먼저 실행하고, 근거 없는 주제는 “위키에 없음”으로 명시.

## [2026-06-06] ingest | Actix Web 공식 문서 (actix.rs/docs)
- 소스: [[actix-web-official-docs]] (source-type: **docs** — 위키 첫 docs 소스, actix.rs/docs 33p)
- 원문 캡처: `01.raw/docs/actix-web/` (33 파일 + 00-index.md; 렌더 페이지 pandoc 변환, 다이어그램은 mermaid `.mmd` 소스 보존; 캡처 단계에서 병렬 페치 + iconize 처리)
- 사용자 협의(AskUserQuestion): granularity=**Consolidated**, actor 깊이=**개별 페이지**, 강조점=**실무 패턴 중심**
- 신규 entities (4): [[actix-web]](허브)·[[actix-actor-framework]]·[[tokio]]·[[serde]]
- 신규 engineering/patterns (12): [[actix-web-extractors]]·[[actix-web-handlers-responders]]·[[actix-web-application-state]]·[[actix-web-routing]]·[[actix-web-middleware]]·[[actix-web-error-handling]]·[[actix-web-databases]]·[[actix-web-testing]]·[[actix-web-websockets]]·[[actix-actor-model]]·[[actix-actor-address]]·[[actix-actor-context]]
- 신규 engineering/systems (4): [[actix-web-http-server]]·[[actix-web-connection-lifecycle]]·[[actix-arbiter]]·[[actix-sync-arbiter]]
- 신규 source (1): [[actix-web-official-docs]]
- 갱신: [[02.wiki/index|index]]·[[02.wiki/engineering/index|engineering/index]]·[[overview]]·log
- 영향 페이지 수: 신규 21 + 갱신 4 = 25
- 작성 방식: 연결 축(source + entity 5)은 steward가 직접, concept 16개는 **6개 병렬 서브에이전트**가 각 raw 문서 정독 후 통일 템플릿(frontmatter·크로스링크 어휘·실무 강조)으로 Bash 작성. 검증: 21/21 존재, frontmatter·코드펜스 정상, dangling 위키링크 0.
- 핵심 합성:
  - actix-web은 [[tokio]] 기반 async 프레임워크로 actor와 분리됨 (whatis: *"largely unrelated to the actor framework"*). actor는 WebSocket 등에서만 선택적 → [[actix-web-websockets]]는 actor 없는 `actix-ws` 권장.
  - 시그니처 3축: [[actix-web-extractors|extractor(FromRequest)]] + [[actix-web-handlers-responders|Responder]] + [[actix-web-application-state|web::Data 워커 공유]].
  - ⚠️ 핵심 함정 2종 문서화: ① `web::Data`를 `HttpServer::new()` 클로저 **밖**에서 생성해야 워커 동기화([[actix-web-application-state]]), ② `NormalizePath` redirect의 POST→GET 데이터 손실([[actix-web-routing]]).
  - 핸들러 블로킹 금지 → [[actix-web-databases|web::block]] 스레드풀 오프로딩으로 tokio 이벤트 루프 보호.
- 모순/정정: ⚠️ 공식 문서는 개발용 자동 재시작 도구로 `watchexec`(`watchexec -e rs -r cargo run`)를 권장 — 초안의 `cargo-watch` 표기를 [[actix-web]] 허브에서 정정.
- 범위 메모: actor framework WIP 스텁 5종(sec-7 Stream/sec-8 IO Helpers/sec-9 Supervisor/sec-10 Registry/sec-11 Helper Actors)은 본문이 `**WIP**`뿐이라 페이지화하지 않음 (raw에는 보존).
- 후속: 사용자 요청으로 `/graphify` 지식 그래프 생성 + iconize 아이콘 부여 진행.

## [2026-06-14] ingest | Self-Harness: Harnesses That Improve Themselves
- 소스 (2): [[self-harness-paper]] (1차, arXiv 2606.09498, source-type: **paper** — 위키 첫 paper 소스) + [[papanuvo-self-harness]] (2차, 한국어 해설, tistory)
- 원문 캡처: `01.raw/articles/2026-06-13_Self-Harness Harnesses That Improve Themselves.md` (arXiv HTML) + `01.raw/articles/2026-06-13_LLM 에이전트가 스스로 진화하는 방법 ...md` (파파누보 tistory)
- 사용자 협의(AskUserQuestion): 강조·범위 = **패턴 중심 + 엔티티 풀세트**
- 신규 concept (1): [[self-harness]] (허브)
- 신규 entities (6): org [[shanghai-ai-lab]] · model [[minimax-m2-5]]·[[qwen3-5]]·[[glm-5]] · tool [[terminal-bench]]·[[deepagents]]
- 갱신 concepts (3): [[agent-harness-design]](*자기-개선 하니스* 절 + 세 패러다임 표 + related/sources) · [[harness-engineering]](System Evolution 자동화 = Self-Harness 인용 + related/sources) · [[generator-evaluator-pattern]](propose/validate의 하니스-계보 변형 절 + related)
- 갱신: [[02.wiki/index|index]](Models +3·Orgs +1·Tools +2·Patterns +1·Sources +2·통계) · [[overview]](현재상태 harness hub + 진화로그) · log
- 영향 페이지 수: 신규 9 + 갱신 6 = 15
- 핵심 합성:
  - **세 번째 하니스 개선 패러다임** 확립: Human Harness Engineering / Meta-Harness / **Self-Harness**(고정 동일 모델이 자기 트레이스로 자기 하니스 개선). 본 위키 harness 허브의 *"누가 하니스를 고치는가"* 축을 완성.
  - 기존 두 허브와 정밀 연결: [[harness-engineering]]의 *"every mistake becomes a rule"* System Evolution을 **사람 손 떼고 자동화** + [[agent-harness-design]]의 *가정 제거(단순화)* 와 반대 방향(*실패→가정 추가=강화*)의 같은 진화 루프 + [[generator-evaluator-pattern]] propose/validate를 *하니스 계보*에 적용(평가자 튜닝 대신 결정론적 verifier + non-regressive gate).
  - 3단계 루프: Weakness Mining(verifier-grounded failure signature φ=(cause,causal-status,mechanism) 클러스터링) → Harness Proposal(diverse yet minimal K개 병렬 후보) → Proposal Validation(held-in/held-out non-regressive 채택).
  - 정량: Terminal-Bench-2.0 3개 모델 held-out +최대 21.4%p(상대 +138%), held-out 개선 = 과적합 아님, *모델마다 다른* edit 채택 → *"harness는 inherently model-specific"* 입증.
  - 본 위키 첫 **중국 lab**([[shanghai-ai-lab]]) + 첫 **비-Anthropic 모델군**([[minimax-m2-5]]·[[qwen3-5]]·[[glm-5]]) + 첫 **paper 소스타입**.
- 2차 소스 신뢰도: 한국어 해설이 핵심 수치·3단계 구조를 손실 없이 전달 — [[james-ai-explorer-understand-anything]]에서 본 *"추상이 한국어 2차 소스에서도 견고"* 패턴 재확인. 모순 0.
- 범위 메모:
  - 파파누보(블로그 저자)는 [[james-ai-explorer-understand-anything|James AI Explorer]] 선례에 따라 person entity 미생성, source author 필드로만 크레딧.
  - 논문이지만 `reading/papers/` 노트는 미생성 — 기존 ingest 선례(actix docs·Understand-Anything)대로 source 흡수만. 사용자가 독서 추적을 원하면 reading-add로 추가 가능.
  - 인라인 언급만 처리한 선행연구(ReAct·Reflexion·STOP·Darwin Gödel Machine·AlphaEvolve 등)·Harbor 실행환경·LangChain org는 entity 미생성 (향후 관련 ingest 시 페이지화 고려).

## [2026-06-13] reading | add to-read | 마션(스페셜 에디션)
- 요청 링크: https://product.kyobobook.co.kr/detail/S000000479326
- 원문 캡처: `01.raw/books/2026-06-13_마션-스페셜-에디션-교보문고.md` (교보문고 public product API 메타데이터·소개 요약; 장문 본문 미리보기/책 속 문장은 보존하지 않음)
- 신규 source: [[kyobo-martian-special-edition]]
- 신규 reading: [[martian-special-edition]] — status `to-read`
- 갱신: [[02.wiki/index|index]], [[02.wiki/reading/index|reading/index]], log
- 범위 메모: LLM/SE 핵심 도메인 밖의 SF 소설이므로 별도 entity/concept 페이지는 만들지 않고 독서 관리와 source 요약만 추가. 실제 독서 후 독서 노트 확장 예정.

## [2026-06-27] til | 안 만만한 사람 vs 만만한 사람
- 신규 TIL: [[2026-06-27-conversation-positioning]] — 대화에서 주도권을 잃지 않는 표현과 반응형 표현의 차이.
- 원자료: 사용자가 제공한 이미지 텍스트 정리본(Discord paste).
- 갱신: [[02.wiki/til/index|til/index]], [[02.wiki/index|index]], log.


## [2026-06-27] ingest | Refactoring.Guru 한국어 디자인 패턴
- 요청 링크: https://refactoring.guru/ko/design-patterns
- 원문 캡처: `01.raw/articles/2026-06-27_refactoring-guru-ko-design-patterns.md` (저작권 보호 본문 전문 대신 URL inventory + 각 패턴 의도 요약 보존)
- 신규 source: [[refactoring-guru-ko-design-patterns]]
- 신규 engineering hub: [[design-patterns]]
- 신규 engineering patterns (22): [[design-pattern-factory-method]] · [[design-pattern-abstract-factory]] · [[design-pattern-builder]] · [[design-pattern-prototype]] · [[design-pattern-singleton]] · [[design-pattern-adapter]] · [[design-pattern-bridge]] · [[design-pattern-composite]] · [[design-pattern-decorator]] · [[design-pattern-facade]] · [[design-pattern-flyweight]] · [[design-pattern-proxy]] · [[design-pattern-chain-of-responsibility]] · [[design-pattern-command]] · [[design-pattern-iterator]] · [[design-pattern-mediator]] · [[design-pattern-memento]] · [[design-pattern-observer]] · [[design-pattern-state]] · [[design-pattern-strategy]] · [[design-pattern-template-method]] · [[design-pattern-visitor]]
- 갱신: [[02.wiki/index|index]], [[02.wiki/engineering/index|engineering/index]], [[overview]], log
- 범위 메모: Refactoring.Guru 카탈로그가 다루는 GoF 패턴 22개 기준(Interpreter 제외). 각 페이지는 원문 구조(의도/문제/해결책/구조/장단점/관계)를 위키용 요약으로 재작성하고, 전문 복제는 피함.

## [2026-06-27] ingest | Refactoring.Guru Refactoring
- 요청 링크: https://refactoring.guru/refactoring
- 원문 inventory: `01.raw/docs/refactoring-guru-refactoring/00-inventory.md` (저작권 보호 본문 전문 대신 URL inventory + 짧은 의도 요약 보존, sha256 포함)
- 신규 source: [[refactoring-guru-refactoring]]
- 신규 engineering hubs: [[refactoring]] · [[technical-debt]] · [[code-smells]] · [[refactoring-techniques]]
- 신규 code smell pages (23): [[long-method]] · [[large-class]] · [[primitive-obsession]] · [[long-parameter-list]] · [[data-clumps]] · [[alternative-classes-with-different-interfaces]] · [[refused-bequest]] · [[switch-statements]] · [[temporary-field]] · [[divergent-change]] · [[parallel-inheritance-hierarchies]] · [[shotgun-surgery]] · [[comments]] · [[duplicate-code]] · [[data-class]] · [[dead-code]] · [[lazy-class]] · [[speculative-generality]] · [[feature-envy]] · [[inappropriate-intimacy]] · [[incomplete-library-class]] · [[message-chains]] · [[middle-man]]
- 신규 technique family pages (6): [[refactoring-techniques-composing-methods]] · [[refactoring-techniques-moving-features-between-objects]] · [[refactoring-techniques-organizing-data]] · [[refactoring-techniques-simplifying-conditional-expressions]] · [[refactoring-techniques-simplifying-method-calls]] · [[refactoring-techniques-dealing-with-generalization]]
- 갱신: [[02.wiki/index|index]], [[02.wiki/engineering/index|engineering/index]], [[overview]], log
- 범위 메모: individual refactoring technique 70여 개는 저작권 본문을 복제하지 않고 family page 표의 URL inventory + 짧은 요약으로 보존. 향후 자주 쓰는 technique만 개별 페이지 승격.

## [2026-06-27] meta | 디자인 패턴 22개 페이지 본문 보완
- 기준: https://refactoring.guru/ko/design-patterns — 각 패턴 페이지를 라이브로 재확인(WebFetch)해 위키용으로 재요약.
- 문제: 22개 [[design-pattern-*]] 페이지가 모두 동일한 "적용 메모" boilerplate 3줄("클라이언트가 구상 타입이나..." / "패턴명보다 중요한 것은..." / "테스트에서는 패턴이 만든 seam을...")만 가진 사실상 스텁이었음.
- 변경: 22개 전부 패턴별 본문으로 재작성. 통일 섹션 구조 → 문제 / 해결책 / 실세계 비유(원문에 없으면 예시) / 적용 가능성 / 장단점(장점·단점 목록) / 다른 패턴과의 관계 / References.
- 핵심 보완: 패턴별 실세계 비유·적용 가능성 bullet·장단점 목록·관계를 원문 구조에 맞춰 추가(예: Strategy=내비게이션/공항, Builder=주택 건설, Proxy=신용카드, Facade=전화 주문 교환원, Decorator=옷 겹쳐 입기, Mediator=관제탑, Flyweight=숲/나무 렌더링 예시).
- 보존·검증: 각 페이지 frontmatter 100% 그대로 유지, GoF cross-link 22개 전부 파일 resolve 확인, boilerplate 잔존 0건, 7개 섹션 전 파일 정확히 1회씩 존재 확인. 페이지 길이 42줄(균일 스텁) → 46~65줄.
- 미변경: [[design-patterns]] 허브·[[02.wiki/index|index]]·[[02.wiki/engineering/index|engineering/index]]는 이미 22개를 정확히 카탈로그하므로 수정 불필요. [[refactoring-guru-ko-design-patterns]] source도 그대로.

## [2026-06-27] meta | 리팩터링 문서(코드 스멜 23 + technique family 6) 본문 보완
- 기준: https://refactoring.guru/refactoring — code smell 페이지(/smells/*)와 technique family 페이지를 라이브로 재확인(WebFetch)해 위키용으로 재요약.
- 문제 1: 23개 code smell 페이지가 모두 동일한 "문제 신호" boilerplate 3줄("코드를 읽는 사람이 실제 의도보다 구조적 noise..." 등) + 동일한 "대표 대응" 미사여구만 가진 스텁이었음.
- 문제 2: 6개 technique family 페이지의 technique 표 "요약" 칼럼이 영어 원문 그대로였고 문장 중간에서 잘려 있었음(예: "the expression itse", "so that th").
- 변경 1: 23개 smell 전부 원문 구조로 재작성 → 신호와 증상 / 원인 / 해결 방법(Treatment, 권장 refactoring을 backtick로) / 이득(Payoff) / 무시해도 될 때 / References. 5개 계열(Bloaters/객체지향 남용/변경 방지자/Dispensables/Couplers) 라벨 명시.
- 변경 2: 6개 family 표의 "요약" 칼럼을 한국어 "문제→해결" 한 줄로 완역·복원(잘림 제거). 표 technique 행 수는 원문과 일치(추가/삭제 0): composing 9 · moving 8 · organizing 15 · conditionals 8 · method-calls 14 · generalization 12 = 66개.
- 변경 3: [[refactoring]] 허브에 "언제 리팩터링하나"(삼진 규칙 + 기능 추가/버그 수정/코드 리뷰 시점) 섹션 추가.
- 검증: smell boilerplate 잔존 0건, 23개 전부 5개 섹션 존재, technique 표 영어 "Problem:/Solution:" 잔존 0건, 23 smell + 6 technique 파일의 [[wiki-link]] 전부 resolve, frontmatter 보존.
- 미변경: [[code-smells]]·[[refactoring-techniques]]·[[technical-debt]] 허브는 이미 분류·링크가 충실해 그대로. [[refactoring-guru-refactoring]] source도 그대로.

## [2026-06-27] ingest | The Twelve-Factor App
- 소스: https://12factor.net/ ([[adam-wiggins|Adam Wiggins]]/[[heroku|Heroku]], 2011), source-type docs. raw: `01.raw/articles/2026-05-25_The Twelve-Factor App.md`.
- 협의: 사용자가 "12요소 레퍼런스 중심" 관점 선택. raw 클리핑이 인트로(Introduction/Background/Who should read)만 캡처돼 12요소 본문은 표준(canonical) 지식으로 보완하기로 합의.
- 신규 source: [[12factor-net]] (요약·핵심 인용·등장 개체; raw 범위 한계 ⚠️ 명시).
- 신규 engineering/pattern: [[twelve-factor-app|Twelve-Factor App 레퍼런스]] — 12 factor 각각 *원칙→핵심→안티패턴* + 분류 표 + 현대 인프라(컨테이너/K8s) 연결 + 한계(stateless 전제).
- 신규 entity 3: [[adam-wiggins]](person)·[[heroku]](product, PaaS)·[[martin-fowler]](person, *Refactoring*·*PoEAA* 저자).
- 연결: [[pets-vs-cattle]]에 "앱 레벨 버전"(VI 무상태·IX disposability) 섹션 + related/References cross-link, updated 갱신. [[refactoring]] References에 [[martin-fowler]] 추가 → refactoring과 12-factor를 Fowler "공유 vocabulary" 사상으로 묶음.
- 인덱스: [[02.wiki/index]] Persons(adam-wiggins·martin-fowler)·Products(heroku)·Patterns·Sources·통계(161→166), [[02.wiki/engineering/index]] Patterns, [[overview]] 진화 로그 1줄.
- 미변경: raw/ 원본(수정 금지). 12factor 본문은 raw에 없어 표준 지식 보완임을 source·overview에 ⚠️ 표기.

## [2026-06-27] ingest | How engineers at Nextdoor use Codex
- 소스: https://openai.com/index/nextdoor/ (OpenAI 고객 케이스 스터디, 2026-06-09), source-type article. raw: `01.raw/articles/2026-06-10_How engineers at Nextdoor use Codex to build without limits.md`.
- 협의: 사용자가 "Outcome engineering 개념 중심" 관점 선택 (엔티티 최소화). 벤더 마케팅 출처임을 source·concept에 ⚠️ 명시.
- 신규 source: [[openai-nextdoor-codex]] (요약·핵심 인용·등장 개체; 성격=마케팅 ⚠️).
- 신규 concept(pattern): [[outcome-engineering]] — Cory Dolphin coinage. how 프롬프팅→결과 정의 전환 + "스택 위로 이동" 조직 귀결 + 한계(벤더 주장). [[verifiable-goals]](result=verifier)·[[sprint-contract]]·[[harness-engineering]]·[[agent-harness-design]]와 교차.
- 신규 entity 4 (위키 첫 OpenAI 생태계): [[openai]](org)·[[codex]](product, GPT‑5.4/5.5·Fast Mode)·[[nextdoor]](org)·[[cory-dolphin]](person). GPT 모델은 별도 페이지 없이 codex/openai 내 인라인(컷오프 이후 스펙 날조 금지).
- 연결: [[verifiable-goals]] related+자매개념에 [[outcome-engineering]] 상호링크, updated 갱신.
- 인덱스: [[02.wiki/index]] Persons(cory-dolphin)·Organizations(openai·nextdoor)·Products(codex)·Concepts(outcome-engineering)·Sources·통계(166→172), [[overview]] 진화 로그 1줄(첫 OpenAI 축 진입).
- 미변경: raw/ 원본(수정 금지).

## [2026-06-27] meta | 디자인 패턴 ↔ actix-web cross-link (graphify gap 메우기)
- 계기: `/graphify`(02.wiki, 176노드·7커뮤니티) 그래프 추적에서 GoF 디자인 패턴 클러스터(C3)가 Refactoring(C1)을 통해서만 본체에 붙고, `Actix / Rust Web`(C4) 코드와는 의미 엣지 0개인 문서화 갭을 발견.
- 추가한 패턴 매핑(방어 가능한 것만, 억지 매핑 배제): 미들웨어(`Transform`+`Service`)→[[design-pattern-decorator|데코레이터]]; 추출기(`FromRequest`)→[[design-pattern-adapter|어댑터]](+[[design-pattern-strategy|전략]]); `Responder`→[[design-pattern-strategy|전략]] + `HttpResponseBuilder`→[[design-pattern-builder|빌더]]; 라우팅(등록순 guard 매칭)→[[design-pattern-chain-of-responsibility|책임 연쇄]] + 중첩 scope→[[design-pattern-composite|복합체]].
- 편집 10개: actix 4개([[actix-web-middleware]]·[[actix-web-extractors]]·[[actix-web-handlers-responders]]·[[actix-web-routing]])에 "디자인 패턴 관점" 섹션 + related/updated; GoF 6개(decorator·adapter·strategy·builder·chain-of-responsibility·composite)에 "실무 예" 백링크 + related. 전부 양방향.
- 검증: design-pattern↔actix 엣지 0→8개(전부 EXTRACTED, 1-hop). graph.json/GRAPH_REPORT.md/graph.html 재빌드(176노드·1156엣지·7커뮤니티). C3·C4는 분리 유지하되 8개 다리로 연결.
- 정직성 메모: 미들웨어는 항상 다음으로 흐름을 이어가므로 책임 연쇄(단락 가능)가 아닌 데코레이터로 매핑(데코레이터 페이지의 구분 그대로). 단락 분기는 guard/ErrorHandlers로 명시.

## [2026-07-07] ingest | XDA — Obsidian CLI terminal workflow
- 요청 링크: https://www.xda-developers.com/obsidian-cli-terminal-workflow/
- 원문 캡처: `01.raw/articles/2026-07-01_Obsidian CLI terminal workflow.md` (저작권 보호 본문 전문 대신 구조화 추출 + command inventory + workflow claims, sha256 포함)
- 신규 source: [[xda-obsidian-cli-terminal-workflow]]
- 신규 engineering/tool: [[obsidian-cli-workflow]] — Obsidian 공식 CLI를 daily append·search·read/create·move file 중심 terminal workflow로 정리
- 갱신: [[obsidian]] (CLI command surface 추가), [[llm-wiki-pattern]] (Obsidian을 viewer뿐 아니라 app-aware command API로 연결), [[02.wiki/index|index]], [[02.wiki/engineering/index|engineering/index]], [[overview]], log
- 핵심 합성: Obsidian CLI는 LLM-WIKI에서 사람의 quick capture friction을 낮추고, [[claude-code|Claude Code]] 같은 agent가 vault를 읽고 검색하고 변경 기록을 남기는 command channel이 될 수 있다. 단 desktop app 실행 의존성과 plugin command 노출 한계를 명시.

## [2026-07-08] til | Obsidian 공식 CLI로 vault를 terminal-first로 다루기
- 신규 TIL: [[2026-07-08-obsidian-cli]] — 설치(토글 하나)·핵심 command(`daily:append`·`search:context`·`create`·`read`·`move file`)·[[claude-code]] agent 통합·"앱 실행 필수" 한계.
- 근거 소스: [[xda-obsidian-cli-terminal-workflow]], 상세 개념: [[obsidian-cli-workflow]].
- 갱신: [[02.wiki/til/index|til/index]](항목 1 + updated), [[02.wiki/index|index]](TIL 섹션·마지막 TIL·통계).

## [2026-07-08] lint | 175 페이지 건강 점검 — 자동수정 대상 결함 0
- 점검 범위: 02.wiki/ 전체 175개 .md (concepts 27·engineering 76·entity 44·source 19·overview 6·til 2·reading 1). 링크 2366개 스캔.
- 링크 그래프: 고아 0 · dangling 0(9건 감지 전부 거짓양성: 이스케이프 파이프 `[[glm-5\|GLM-5]]`류 3, 루트 `../CLAUDE.md` 교차참조 1, 백틱 코드 템플릿/log 메타 5) · 메인·reading·til index 100% 동기화, stale 0.
- engineering/index: code-smell 23 + refactoring-technique family 6(=29 leaf)이 개별 등재 없이 hub(`code-smells`·`refactoring-techniques`)로 위임 링크됨 — by-design(고아 아님), 결함 처리 안 함.
- frontmatter: 175개 전부 유효·필수 필드 완비 · 파일명 kebab-case 100%(TIL 날짜형식 2/2) · reading 상태 일관성 위반 0.
- `updated` vs git 날짜 69건 drift는 전부 거짓양성(초기 일괄 커밋 3d92320 57건 + Self-Harness 저작-커밋 13일 지연 12건) — stale 아님.
- 소프트 이슈 2건(사용자 승인으로 처리): ① [[lum1104-understand-anything]] `date-published` 공백 → GitHub repo 생성일 **2026-03-15**로 채움(조회 중 repo가 `Lum1104`→`Egonex-AI/Understand-Anything`로 이전된 것 확인; source-url·entity는 현행 유지). ② `engineering/index`를 **전량 등재**로 확장 — code-smell 23개 + refactoring-technique family 6개를 hub(`code-smells`·`refactoring-techniques`) 아래 개별 wikilink로 명시(기존 hub 위임에서 exhaustive로).
- 조치: 결함 자동수정 0건 + 사용자 승인 개선 2건 반영(lum1104 발행일·engineering/index 확장). index 통계 "마지막 lint" 갱신. lint-report 임시 파일은 추적할 미해결 이슈가 없어 생성 생략.
- 후속 관찰(비조치): Understand-Anything repo가 `Egonex-AI`로 이전됨 — 향후 소스 재방문 시 source-url 업데이트 검토 여지.

## [2026-07-21] ingest | Claude Code 공식 모범 사례 쉽게 이해하기
- 요청 링크: https://charlychoi.blogspot.com/2026/07/claude-code.html
- 원문 캡처: `01.raw/articles/2026-07-20_Claude Code 공식 모범 사례 쉽게 이해하기.md` (저작권 보호 본문 전문 대신 구조화 추출; sha256 포함)
- 신규 source: [[charlychoi-claude-code-best-practices]] — Anthropic 공식 best practices를 Charly Choi가 한국어 학습용으로 재구성한 2차 해설이며, 변동 가능한 제품 command는 공식 문서 재확인 필요.
- 갱신: [[claude-code]]에 실무 운영 계약, [[verifiable-goals]]에 task별 verifier, [[llm-coding-guidelines]]에 `CLAUDE.md`/Skills/Hooks/CLI·MCP 배치 기준 추가.
- 갱신: [[02.wiki/index|index]], [[overview]], log.
- 핵심 합성: 좋은 prompt의 본질은 길이가 아니라 **목표 + 맥락 + executable verifier + permission boundary + 독립 review**를 가진 task contract다.

## [2026-08-29] ingest | Tech Bridge — Spec-driven development
- 소스: https://www.youtube.com/watch?v=F_smvU3oqbU ([[tech-bridge]], 22:07), source-type video.
- raw: `01.raw/articles/2026-08-29_프롬프트 작성은 그만두세요. 이제 명세(Spec)를 작성할 때입니다.md`
- ⚠️ YouTube timedtext HTTP 429 — 자막 전문 미확보. 채널 설명(1차) + Spec Kit 공식 문서(complementary). MCP 데모·엔터프라이즈 3원칙 세부는 미기록.
- 신규 source: [[tech-bridge-spec-driven-development]]
- 신규 concept: [[spec-driven-development]]
- 신규 entity: [[github-spec-kit]] (tool)
- 갱신: [[tech-bridge]], [[harness-engineering]], [[verifiable-goals]], [[sprint-contract]], [[outcome-engineering]], index, overview, log

## [2026-08-29] ingest | Tech Bridge — Figma 코딩 에이전트 조직 도입
- 소스: https://www.youtube.com/watch?v=OSd69LTMi3w ([[tech-bridge]], 17:13), 발표자 [[eyal-blum]].
- raw: `01.raw/articles/2026-08-29_품질 저하 없이 조직에 코딩 에이전트를 성공적으로 도입하는 방법 Figma.md`
- 이후 같은 날 자막 재수신 + 상세 재작성 (아래 항목).
- 신규 source: [[tech-bridge-figma-coding-agents]]
- 신규 concept: [[agent-org-adoption]]
- 신규 entity: [[figma]] (org) · [[eyal-blum]] (person)
- 갱신: [[tech-bridge]], [[harness-engineering]], [[verifiable-goals]], [[sprint-contract]], [[outcome-engineering]], index, overview, log

## [2026-08-29] ingest | Tech Bridge — 빌 게이츠 AI 경고 (Radio Atlantic)
- 소스: https://www.youtube.com/watch?v=u1iQob0v-5k ([[tech-bridge]], 31:47). 원본 Radio Atlantic / Hanna Rosin.
- raw: `01.raw/articles/2026-08-29_AI에 대해 생각이 바뀐 빌 게이츠의 경고.md` (en-orig 자막 + Atlantic 공식 트랜스크립트 교차)
- 신규 source: [[tech-bridge-bill-gates-ai-warning]]
- 신규 entity: [[bill-gates]] (person)
- 페이지화하지 않음: Hanna Rosin, 엡스타인 에피소드 세부(소스에만 요약)
- 갱신: [[tech-bridge]], index, overview, log
- 핵심 합성: 코딩 에이전트 capability 임계점이 바이오테러·사이버·노동 위험 임계값을 연 *바깥 세계 비용*. 자발 리뷰는 [[verifiable-goals]]의 반대말(criteria 없음).

## [2026-08-29] meta | TechBridge-KR 일일 ingest 시작
- wiki 채널 요청: `@TechBridge-KR` 신규 롱폼을 매일 1회 ingest 후 `origin/main` push.
- 당일 신규 3편 처리(위 ingest 3건). Shorts 제외.
- 상태: 이후 실행은 기존 `source-url` / raw 파일의 video id로 중복 건너뜀.

## [2026-08-29] ingest | Figma 코딩 에이전트 강연 상세 재작성
- 요청: wiki 채널에서 동일 영상(`OSd69LTMi3w`)을 "최대한 상세히". 이미 [[tech-bridge-figma-coding-agents]]가 있어 **중복 페이지 없이** 본문 확장.
- en-orig + ko 자막 재수신. 채널 공식 12개 챕터 순서로 논증·수치·인용·운영 체크리스트를 source에 재구성. [[agent-org-adoption]]에 현장 규칙 섹션 추가. raw는 챕터 재구성으로 교체.
- 페이지 수 변화 없음.

## [2026-08-29] ingest | Tech Bridge 3편 본문 보강 (자막 확보)
- 계기: 첫 ingest가 채널 설명 수준이라 "동영상 없이 파악 불가" 피드백.
- Chrome 쿠키로 en-orig 자막 재시도 성공 (`F_smvU3oqbU`, `OSd69LTMi3w`). Gates는 기존 Atlantic 공식 트랜스크립트 + en-orig.
- 세 source 페이지를 강연 논증 순서(챕터·데모 단계·인용)로 재작성. 개념 [[spec-driven-development]]·[[agent-org-adoption]]·[[github-spec-kit]] 운영 세부 보강.
- raw 3편은 불완전 캡처(429)를 자막 기반 구조화 재구성으로 교체 — 원문이 없었던 자리의 보정이지 기존 완전 소스 덮어쓰기가 아님.
- 발표자 ASR "Luna Diva"는 본명 미확인 → 엔티티 페이지 없음.

## [2026-08-30] ingest | Tech Bridge — Clare Liguori frontier engineering
- 소스: https://www.youtube.com/watch?v=Ry0WHNxDbYA ([[tech-bridge]], 20:29). 업로드 2026-08-29, 전날 일일 ingest 이후 신규 롱폼 1편. 발표자 [[clare-liguori]].
- raw: `01.raw/articles/2026-08-29_AI 보조를 넘어 AI 네이티브로.md` (en-orig 자막. ko timedtext 429).
- 신규 source: [[tech-bridge-frontier-engineering]]
- 신규 concept: [[frontier-engineering]]
- 신규 entity: [[clare-liguori]] (person) · [[kiro]] (product) · [[amazon]] (org)
- 페이지화하지 않음: Bedrock Mantle, Prime Video, Amazon Stores, distinguished engineer 개인
- 갱신: [[tech-bridge]], [[agent-org-adoption]], [[harness-engineering]], [[spec-driven-development]], [[verifiable-goals]], index, overview, log
- 핵심 합성: 같은 도구(90% Kiro)로 Stores 50팀이 <3x vs 4.5x(중앙값)로 갈림. 차이는 5습관. 2026 과제 50→2,000팀. 새 병목은 의사결정.
- 트리거: Buzz cron `0 0 * * *`가 00:00 UTC 핑을 안 보냄. chris 질문으로 수동 실행.

## [2026-08-31] ingest | Tech Bridge 08-30 롱폼 3편 (Ng · DHH · Touil)
- 트리거: wiki 채널에서 스케줄러 미동작 수정 요청. Buzz cron `0 0 * * *`가 08-30·08-31 00:00 UTC 모두 핑 없음 (#4904). 워크플로를 `interval: 24h`로 바꾸고 세션 1d 스케줄을 건 뒤, 놓친 오늘분을 이 턴에서 실행.
- 업로드 2026-08-30 롱폼 3편 (Shorts 제외). ko+en-orig 자막 Chrome 쿠키로 확보.
- 1) https://www.youtube.com/watch?v=5bELrUqxX4U (36:15, Silicon Valley Girl × [[andrew-ng]]) → [[tech-bridge-andrew-ng-ai-opportunity]]. 신규 [[andrew-ng]] · [[coursera]] · [[learnvector]] · [[regulatory-capture]] · [[cognitive-offloading]]. 갱신 [[bill-gates]](대조) · [[openai]](AGI 선언 인센티브).
- 2) https://www.youtube.com/watch?v=sXCppYzX-0g (9:15, Lex × [[dhh]]) → [[tech-bridge-dhh-agent-productivity]]. 신규 [[dhh]] · [[omarchy]]. ASR Amachi→Omarchy. 갱신 [[agent-org-adoption]] · [[frontier-engineering]].
- 3) https://www.youtube.com/watch?v=0qySk1fcf6k (20:01, [[imad-touil]]) → [[tech-bridge-ai-native-skills]]. 신규 [[imad-touil]] · [[agent-skills]]. 갱신 [[harness-engineering]] · [[spec-driven-development]] (spec–plan–task = product increment 한 칸).
- 페이지화하지 않음: Silicon Valley Girl, QuantumBlack, 37signals, DeepLearning.AI, Lex Fridman.
- raw: `01.raw/articles/2026-08-30_*.md` 3편. 갱신 index, overview, log, [[tech-bridge]].

## [2026-09-01] ingest | Tech Bridge 08-31 롱폼 2편 (Adobe agentic sites · Cursor GrokBot)
- 트리거: wiki 채널에서 chris가 "Workflow가 오늘도 실행되지 않았어" — 원인 분석 요청. 스케줄러 진단 결과를 별도 기록(아래 meta)하고 놓친 오늘분을 이 턴에서 실행.
- 업로드 2026-08-31 롱폼 2편 (Shorts 없음). ko + en-orig 자막 Chrome 쿠키로 확보, 429 없음. 수치는 en-orig 교차 확인.
- 1) https://www.youtube.com/watch?v=PXHUHNX7nbI (20:13, [[carlos-sanchez]] / [[adobe]]) → [[tech-bridge-agentic-sites]]. 신규 concept [[agentic-sites]]. 신규 entity [[carlos-sanchez]] · [[adobe]] · [[cerebras]] · [[gemma-4]]. 갱신 [[cloudflare]] 참조.
  - 핵심: 페이지가 아니라 **블록** 단위 개인화 + **자기 사이트를 RAG 코퍼스로**. 브랜드 가이드라인이 환각 예산. promptfoo 상시 평가(사이트마다 결과가 다름). 정확성과 **속도(1~2초)** 가 동급 지표.
  - 수치: Cerebras+Gemma 4 페이지 생성 평균 **1.1초**, 2위 구성 4.6초. LLM 왕복 1초, 2,200–2,300 tok/s.
  - ⚠️ 디버그 화면의 "Total time 164 seconds"는 ko·en-orig 자막이 일치하지만 같은 화면 수치와 모순 — 단위 불명으로 **인용하지 않음**을 raw·source 양쪽에 명시.
  - ⚠️ 16:33 "Off One Labs"는 두 자막 모두 불분명해 원 표기 미기록.
- 2) https://www.youtube.com/watch?v=cVFc9f6M0U0 (26:39, MTS 인터뷰 · [[lauren-tan]] · [[roshan-sadanani]] / [[cursor]]) → [[tech-bridge-grokbot-agent-teams]]. 신규 concept [[persistent-agent-teams]]. 신규 entity [[lauren-tan]] · [[roshan-sadanani]] · [[cursor]] · [[grokbot]] · [[grok-4-6]]. 갱신 [[agent-org-adoption]].
  - 핵심: 정체성 + 자체 컴퓨터 + 코디네이터(비서실장) 봇 + 메시징 UI. 엔지니어 역할이 **에이전트 매니저**(위)와 **코드베이스 관리인**(아래)으로 분화 — 규칙을 린트·CI 실패로 인코딩([[verifiable-goals]] 재확인).
  - 대중화 병목을 모델이 아니라 **UX**로 특정. 채택 경로는 내부 PMF → 외부 출시([[agent-org-adoption]]와 동형)이나 확산이 엔지니어링 밖까지 간 것이 신규.
  - 수치: Cursor Bench 3.2 — Grok 4.6 xhigh **70.8% @ $2.81/task** vs Fable 5 Max **70.5% @ $17.32** (동점대 ~6배). 가격이 곧 병렬성.
  - ⚠️ Contradiction: 소스가 Grok 4.6을 **Cursor + SpaceX 공동 발표**로, 벤치마크를 **Cursor Bench 3.2**로 서술. 채널 밖 독립 확인 없이 소스 서술 그대로 기록 (source·[[grok-4-6]]·[[cursor]] 3곳에 단서 명시).
  - ASR 보정: GrokBot(그록봇/Graphbot/그랩봇/Grubbot/락봇), Grok 4.6(Rock/그래프), "GRT 4.6 ICS"→xhigh, IMAX "70인치"→70mm. "Saul" 모델명은 불확실로 표시.
- 페이지화하지 않음: MTS 채널, Benny(개별 봇), promptfoo, AEM Edge Delivery(제품 계층은 [[adobe]] 안에), SpaceX.
- raw: `01.raw/articles/2026-08-31_*.md` 2편. 갱신 index(202→215), overview, log, [[tech-bridge]], [[agent-org-adoption]].
- 핵심 합성: 이 위키가 하루 만에 코딩 에이전트 밖으로 두 걸음 — **생성형 소비자 UI**([[agentic-sites]])와 **비개발자용 지속형 에이전트**([[persistent-agent-teams]]). 두 소스 모두 병목을 모델 능력이 아닌 곳(지연 예산 / UX)에 두고, 둘 다 작은·싼 모델이 그 병목을 푸는 열쇠라고 말한다.

## [2026-09-01] meta | 일일 ingest 스케줄러 미실행 원인 규명
- 증상: 08-30·08-31·09-01 모두 자동 실행 없음. 08-31에 cron→`interval: 24h` 변경 + 세션 1d 스케줄 추가로 고쳤다고 보고했으나 09-01에도 실행 안 됨.
- **원인 1 (확정)**: 백업으로 걸었던 세션 스케줄러 `01a0554049f77543907c862eefc846aa`가 조회 시 존재하지 않음(`No scheduled jobs`). 스케줄러의 `durable` 옵션은 **실제로 효과가 없고** 잡이 세션 메모리에만 산다 — 세션 종료와 함께 소멸. 08-31 보고의 "durable 백업"은 틀린 진술이었음.
- **원인 2 (확정, 실험으로 증명)**: `buzz workflows trigger`로 수동 실행하니 ping 메시지가 정상 게시됨 → **워크플로 엔진과 YAML은 정상**. 그런데 그 메시지의 작성자는 `12f6870117eff1a6318bd38c82a65d51dd19879b7489f57247114d0ee8a96de3` (`buzz:workflow` 태그) — 릴레이의 **워크플로 러너 키**이고 채널 멤버도 아니다. 이 에이전트 하니스는 `BUZZ_ACP_RESPOND_TO=owner-only`(owner = chris `991570ec…`)로 게이트되므로 **그 ping은 턴을 시작시키지 못한다.** 즉 스케줄이 정상 발화해도 에이전트는 절대 깨어나지 않는 구조였다.
- **원인 3 (증거 기반 추정)**: 08-30·08-31 채널에 `12f68701…` 발신 메시지가 전혀 없음 → 릴레이 스케줄 자체도 발화하지 않았음. 업스트림 [block/buzz#4904](https://github.com/block/buzz/issues/4904)와 일치. `buzz workflows runs`는 항상 `[]`(CLI가 DB run history를 읽지 않음)이라 채널 메시지 유무가 유일한 신호.
- 조치: `buzz agents draft-update --respond-to anyone` 초안을 owner 검토로 전송(저장 전까지 무효). 채널 멤버가 chris와 Clip Scribe 둘뿐이고 self-authored 이벤트는 별도로 무시되므로 이 채널에서의 노출 범위는 제한적.
- 미해결: #4904가 고쳐지기 전까지 릴레이 발화는 여전히 불확실. respond-to가 열리기 전에는 **어떤 자동 경로도** 에이전트를 깨울 수 없으므로 사람 멘션이 유일한 확실한 트리거.

## [2026-09-02] ingest | Tech Bridge 09-01·09-02 롱폼 4편 (Anthropic 플랫폼 · Ironclad · Lena Hall · TikTok)
- 트리거: wiki 채널에서 chris가 일일 ingest 실행 지시. **launchd 잡은 09:10 KST에 발화했으나 즉시 실패** — `WORK_LOGS/techbridge-daily-2026-09-02.log`에 `Failed to authenticate: OAuth session expired and could not be refreshed`, exit=1. 자동 경로가 또 막혀 이 턴에서 수동 실행.
- 신규 롱폼 4편 (Shorts 없음, 전부 19분 이상). ko + en-orig 자막 Chrome 쿠키로 전부 확보, **429 없음**. 수치·인용은 en-orig로 교차 확인.
- 1) https://www.youtube.com/watch?v=XV6WcGliCGM (19:19, [[salman-munaf]] / [[tiktok]]) → [[tech-bridge-agents-as-distributed-systems]]. 신규 engineering [[agent-distributed-systems]] (첫 `engineering/systems` 비-actix 페이지). 신규 entity [[salman-munaf]] · [[tiktok]].
  - 핵심: 에이전트가 **부작용**을 내는 순간 분산 시스템 문제. 처방은 전부 기존 도구(멱등성·서킷 브레이커·saga 보상·최소 권한)이고 새로운 것은 **호출자가 비결정론적**이라는 점뿐.
  - 가장 이식성 높은 두 줄: **"타임아웃은 실패가 아니라 알 수 없음"**, **"행동에 영향을 주는 맥락은 상태"**(→ 메모리를 무효화 가능한 캐시로).
  - 승인 설계: 승인은 **동작·타임스탬프·행위자·만료**에 묶여야 하고 30달러 승인이 300달러로 재사용되면 안 된다.
  - 모델 개선의 한계를 명시 — 오류율은 낮추지만 **네트워크 오류·stale 데이터·악의적 입력**은 못 없앤다. [[sutton-bitter-lesson]]에 **환경 불확실성** 축의 반례로 추가.
  - ⚠️ Replit·Air Canada 사고는 발표자의 **사후 해석**이고 독립 조사가 아님을 source·entity 양쪽에 명시.
- 2) https://www.youtube.com/watch?v=TQqa0B_pNGE (43:59, [[angela-jiang]] · [[katelyn-lesse]] / [[anthropic]], Kleiner Perkins *Builders* S2) → [[tech-bridge-claude-platform-agent-era]]. 신규 concept [[token-roles]]. 신규 entity [[angela-jiang]] · [[katelyn-lesse]].
  - **채널 첫 43분대 장편이자 첫 공식 챕터 없는 영상.** 소제목은 자막 흐름으로 붙이고 타임스탬프는 실제 발화 시각만 사용 — raw 헤더에 임의 소제목임을 명시.
  - [[agent-harness-design]] 정의 확정: **"하네스는 while 루프"**, 그 위가 **메타 하네스 / '전략'**. 용어가 애플리케이션까지 부풀었다는 자기 인식도 함께.
  - [[managed-agents]] 3분할의 **이유**를 처음 1차 진술로 확보 — 샌드박스 기술이 애초에 *일시적* 용도라 **수명 주기가 다른 것을 분리**했다. 하네스=내구성 서버, 샌드박스=작업 시점 생성·삭제.
  - [[token-roles]] 3종: **advising**(Sonnet 실행 + Opus 조언) · **grading**(`outcomes` — 루브릭 주면 채점 에이전트 프로비저닝) · **dreaming**(과거 세션 → 메모리·스킬 작성).
  - 새 병목 관찰: 실행이 빨라져 **정렬(alignment)이 병목** — "이틀 만에 끝났는데 모두를 같은 생각으로 만들 시간이 없다". 팀 200명.
  - 도입 실수 진단: 인간 중심 프로세스의 비효율 지점에만 에이전트를 끼워 넣는 것 → **에이전트 우선 재설계**. 부가로 **전문가 직관이 틀린다**(물어보면 "주고받는 게 좋다"지만 실제로는 비효과적).
  - ⚠️ "sonnet + opus advising이 sonnet 단독보다 싸다"는 **내부 eval**로 벤치마크·수치 미공개. "12년 → 3개월"은 발표자가 *"call it like 3 months"*로 어림한 값 — 측정치로 인용 금지. 양쪽 다 source·concept에 명시.
  - ⚠️ 29:02 "cloud tag"는 ko·en-orig 모두 불분명 — Slack에 사는 Claude 제품인 것은 맥락상 분명하나 **제품명 미확정으로 원 표기 미기록**.
- 3) https://www.youtube.com/watch?v=fOsLTMhjyMM (22:21, [[mingsheng-hong]] / [[ironclad]]) → [[tech-bridge-trusted-throughput]]. 신규 concept [[trusted-throughput]]. 신규 entity [[mingsheng-hong]] · [[ironclad]].
  - 논증 축은 **토큰 = LOC**: 추적하되 최적화 대상으로 삼지 마라. 대시보드는 리더보드가 아니라 **연기 감지기**이고 조사 신호는 *안 쓰는 쪽*(도입 격차).
  - 지표 진화 경로를 실패 단계까지 공개: LOC → 열린 PR → 병합 PR → **복잡도 가중 병합 PR**(LLM 1~2개로 티셔츠 사이즈 채점). [[generator-evaluator-pattern]]을 *생산성 계측 자체*에 적용한 첫 사례.
  - 병목 이동을 **리뷰·CI**로 특정. 새 인과: flaky 테스트 → 수동 재실행 또는 AI 반복 재시도 → **토큰 낭비의 원인이 CI 품질**.
  - 안티패턴 경고: CI 과부하 때문에 **PR 분할 중단**(1시간 회귀 × 10 PR = 10시간) → 사람 검토 부담·주의 분산으로 품질 하락.
  - ⚠️ **발표자 이름이 소스 안에서 갈린다** — 제목 "Mingsheng Hong", 설명란 "Mingshan Hong", ASR "Minshan". LinkedIn 슬러그가 `mingshenghong`이라 제목 표기를 따르되 **해소하지 않고 기록**(raw·source·entity 3곳).
  - ⚠️ Amazon·Meta 리더보드 일화와 "한 달 5억 달러"는 발표자가 언론 보도로 소개했을 뿐 **출처 미명시**.
- 4) https://www.youtube.com/watch?v=3tDoLkFcEKg (19:15, [[lena-hall]]) → [[tech-bridge-signal-layer]]. 신규 concept [[signal-layer]]. 신규 entity [[lena-hall]] · [[richard-hamming]].
  - **채점기 경계선**이 이 위키에서 [[sutton-bitter-lesson]]의 가장 정밀한 범위 한정 — *"컴파일러는 무료 채점 도구, 테스트 스위트는 무료 채점 도구"* → 코드가 먼저 자동화된 것은 **가장 검증하기 쉬웠기 때문**.
  - [[verifiable-goals]]의 **정확한 이면**으로 배치: 그쪽이 "verifier를 만들어라"면 이쪽은 "verifier를 만들 수 없는 곳을 알아라".
  - **[[dhh]] taste 논의 정면 반박** — "취향은 피드백을 통한 선호도일 뿐이라 학습 가능"하고, 남는 것은 *아직 일어나지 않은 일*에 대한 판단과 *모델이 관찰할 수 없는 관계*. 두 소스가 서로를 참조하지 않으므로 [[dhh]] 페이지에 **해소하지 않은 대비**로 기록.
  - 왜곡 3종(source/org/machine)과 처방. org distortion의 원인을 무능이 아니라 **결과에 대한 노출**로 지목 — 더 나은 AI로 해결되지 않는다는 함의.
  - [[richard-hamming]] 재해석: 공략 가능성이 문제를 중요하게 만드는데 AI가 공략 권한을 모두에게 줬으므로 **희소성이 도구에서 문제 선택으로 이동**.
  - ⚠️ 벤치마크 이름·YC 회사·모니터링 제품 사례가 모두 **익명/비특정** — 검증 가능한 형태가 아님을 source·entity에 명시.
- 페이지화하지 않음: Kleiner Perkins(진행사), Josh Coyne·Leigh-Marie Braswell(진행자), Stripe·Stripe Connect(경력 배경), Sarah Guo(1회 인용), Paul Graham·Twitch(1회 예시), Replit·Air Canada(사고 사례), Amazon·Meta 리더보드 일화.
- raw: `01.raw/articles/2026-09-01_*.md` 3편 + `2026-09-02_*.md` 1편. 갱신: index(215→231), overview, log, engineering/index, [[tech-bridge]], [[anthropic]], [[managed-agents]], [[agent-harness-design]], [[generator-evaluator-pattern]], [[verifiable-goals]], [[sutton-bitter-lesson]], [[agent-org-adoption]], [[self-harness]], [[dhh]].
- **핵심 합성**: 서로를 모르는 세 소스가 같은 결론에 수렴했다. ① 구매자([[ironclad]])와 공급자([[anthropic]])가 모두 **"토큰 단가는 잘못된 최적화 대상"** — 각자의 인센티브가 그 결론과 정렬돼 있다는 점은 감안 필요. ② [[signal-layer]]와 Claude Platform 팀이 모두 실행이 싸지면 남는 일을 **문제 선택과 정렬**로 지목. ③ [[agent-distributed-systems]] → [[token-roles]] 사이에 **순서 의존성**이 있다 — 기본 루프의 신뢰성이 풀려야 전략 계층이 열린다(*"가장 기본적인 내용들이 어느 정도 이해 가능해졌기 때문"*).
