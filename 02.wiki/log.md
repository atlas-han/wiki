---
title: Log
type: overview
tags: [meta]
created: 2026-05-25
updated: 2026-06-27
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
