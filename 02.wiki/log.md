---
title: Log
type: overview
tags: [meta]
created: 2026-05-25
updated: 2026-09-19
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

## [2026-09-02] ingest | Tech Bridge 09-02 인터뷰 1편 (Flutter GDE Ivanna Kaceviča — AI 스킬 워크플로)
- 트리거: **launchd 잡 `com.atlas.techbridge-ingest`가 이번엔 인증을 통과해 실제로 돌았다** (09:01 UTC / 18:01 KST, `runs=3`; 스케줄 시각 09:10 KST가 아니므로 `launchctl kickstart` 추정). 이 세션의 부모 프로세스가 `run-ingest.sh`(pid 57028)임을 확인. 같은 날 09:10 KST 발화분은 OAuth 만료로 실패했었다. **신규 영상이 있는 첫 launchd 실행.**
- 신규 롱폼 1편 (Shorts 없음). 최근 15편 중 14편은 기존 ingest, 08-28 Exa 영상은 첫 ingest 이전이라 대상 밖. ko + en-orig 자막 Chrome 쿠키로 확보, **429 없음**. 수치·인용은 en-orig로 교차 확인.
- https://www.youtube.com/watch?v=4hfmNiQDt1g (15:28, [[ivanna-kacevica]] / [[flutter]], Fluttercon 현장 인터뷰 추정) → [[tech-bridge-flutter-ai-workflow]]. 신규 entity [[ivanna-kacevica]] · [[flutter]] (위키 첫 모바일/크로스플랫폼 프레임워크). 신규 concept 없음 — 내용이 모두 기존 개념의 **실무자 관점 확장**이라 6개 concept에 절을 추가했다.
  - [[agent-skills]] (두 번째 소스): 프롬프트→규칙→스킬 세 층위(읽히는 시점 기준), 스킬을 쓸 두 신호(**반복** · **일회성 자동화 — 쓰고 지우는 스킬**), description="use when"이 트리거, skill creator + *"카피라이터가 아니라 관리자"*, 유지보수 비용(공식 스킬 = 저장소 하나, 커뮤니티 목록 2주 점검), 추천 5개 스킬 표.
  - [[prompt-injection]]: **세 번째 벡터 — 스킬 파일 공급망**. 런타임 입력 방어(probe·classifier)가 닿지 않는 이유를 표로(진입 시점·신뢰 상태·probe 적용·페이로드 형태). *"숨겨진 Unicode 지시"*. 처방은 공식 출처·내용 읽기 + Managed Agents식 토큰 격리.
  - [[generator-evaluator-pattern]]: **evaluator–evaluator 교차 확인**(코드 리뷰 + Kevin Moore PR triage) · **스크린샷을 보는 QA 에이전트**(골든 테스트는 회귀, 스크린샷은 QA). 남은 한계 *"좋은지는 알지만 필요한지는 모른다"* = 맥락·기억.
  - [[sutton-bitter-lesson]]: 반례 표에 4번째 축 **학습 데이터 격차**(Flutter ≪ Python·JS → 강한 모델도 Row·Column 대신 컨테이너+패딩). 앞의 세 반례와 달리 데이터가 쌓이면 사라지는 종류임을 명시.
  - [[trusted-throughput]]: Amazon 리더보드의 **개인 수준 대응물** — *"토큰을 다 써버리는 걸 좋아해요"* / "게임화된 거예요". 발표자는 문제로 보지 않는다는 차이.
  - [[persistent-agent-teams]]: **코디네이터 없는 1인 버전** — Claude·Codex·Antigravity 기계 3대, 인계는 사람. 네 구성 요소 중 자체 컴퓨터만 갖춘 상태.
  - ASR 보정: "PR tryer"/"PR 시도" → PR triage, "anti-gravity"/"반중력" → Antigravity(Google 에이전틱 IDE 추정), "ship aton by revenue cat" → RevenueCat Shipaton, "secret uni code" → Unicode, "Flare"/"flatter" → Flutter, "Ludomaniac" → 도박 중독자(자기 농담).
  - ⚠️ 발표자 표기는 자막("이바나") 대신 설명란 **Ivanna Kaceviča**를 따랐고, 본인 링크·스킬 저장소 URL이 소스에 없어 `links: []`. ⚠️ 진행자 무명 — Flutter 팀 측은 **추정**. ⚠️ 03:16 "Jasper"는 Dart 웹 프레임워크 Jaspr일 가능성만 기록, 확정 안 함. ⚠️ 효과 진술("1년 넘게 잘 됐다")은 전부 일화.
- 페이지화하지 않음: Kevin Moore(PR triage 스킬 저자, 1회), Antigravity(1회), RevenueCat Shipaton(1회), Midjourney(회고 1회), Fluttercon(장소), Google(공식 스킬 저장소 주체 1회), Jaspr(불확실).
- raw: `01.raw/articles/2026-09-02_Flutter 개발자 인터뷰 플러터 개발자의 AI 워크플로우.md`. 갱신: index(231→234), overview, log, [[tech-bridge]] (같은 날 ingest 1편→2편).
- **핵심 합성**: 이틀 사이 스킬을 다룬 두 소스가 정확히 반대 끝에서 만난다 — Touil([[tech-bridge-ai-native-skills]])은 *조직*이 스킬을 카탈로그·거버넌스해야 부채가 안 생긴다고 했고, Kaceviča는 *개인*이 인터넷에서 받은 MD 파일 하나가 이미 공급망 위험이라고 한다. 둘 다 처방이 **출처·내용 검사**라는 점에서 일치하고, 이것이 [[prompt-injection]]을 런타임 문제에서 **설치 시점 문제**로 확장한다. 부수적으로 이 소스는 [[signal-layer]]의 채점기 경계선("좋은가"는 채점 가능, "필요한가"는 아님)이 코드 리뷰라는 가장 자동화된 영역 **안에서도** 유효함을 보여준다.

## [2026-09-03] ingest | Tech Bridge — 안드레 카파시 스탠포드 트랜스포머 강의

- https://www.youtube.com/watch?v=y2p8Va_zu00 (61:24, [[andrej-karpathy]] / Stanford CS25) → [[tech-bridge-karpathy-transformers-stanford]]. 채널 최근 15편 중 **신규는 이 1편뿐**이었고 나머지 14편은 이미 ingest돼 있었다. Shorts 없음. 자막 429 없음 — ko·en-orig 모두 확보.
- ⚠️ **채널 첫 아카이브 재배포**: 업로드는 2026-09-02지만 **강연 자체는 ~2023년**이다. 설명란에 촬영 시점 표기가 없어 내부 증거로 판정했다 — 발표자가 청중에게 *"entering this area in roughly 2023"*, 2017년 구조를 *"five years ago"*, [[nanogpt]]를 *"지난 며칠 동안 작업했다"*(공개 2023-01), Q&A에서 ChatGPT를 갓 나온 제품처럼 취급. → **이 채널의 업로드 날짜를 발화 날짜로 가정하지 말 것**을 [[tech-bridge]]에 경고로 남겼다. 기존 소스 15편은 전부 동시대 강연이라 이 전제가 처음 깨졌다.
- 신규 concept 3개 — 위키가 지금까지 **어휘로만 쓰던 것들의 정의 페이지**다. 기존 [[tech-bridge]] 소스 15편이 전부 에이전트 실무 층위였고 아키텍처 층위는 비어 있었다.
  - [[transformer]]: 세 속성 **동시** 최적화(표현력·최적화 가능성·**GPU 효율성**)로 이겼다는 프레임. 3번이 가장 저평가됐다는 것이 발표자 주장 — *"현재 하드웨어에서 효율적이면 더 크게 만들 수 있습니다."* RNN 대비(길고 가는 그래프 vs 얕고 넓은 그래프)가 세 속성을 한 번에 보여준다. 세 변종(encoder/decoder-only/encoder-decoder)이 마스킹 줄 하나·cross-attention 줄 하나 차이라는 표.
  - [[attention-mechanism]]: **방향 그래프 위의 데이터 의존적 메시지 전달**. query=찾는 것, key=가진 것, value=전달할 것. *"Heads는 병렬 복사 붙여넣기, Layers는 직렬 복사 붙여넣기."* self/cross는 **key·value의 출처만** 다르고 연산은 동일. ⚠️ 이 프레이밍은 발표자가 Q&A에서 *"어제 생각해냈다"*고 농담한 **개인적 재해석**임을 페이지에 명시했다.
  - [[in-context-learning]]: **outer loop**(SGD·가중치) vs **inner loop**(시퀀스 읽기·activation). [[context-engineering]]·[[token-roles]]·[[agent-skills]]가 실무 층위에서 쓰던 것의 메커니즘 이름.
- 신규 entity 2개 — [[nanogpt]](300줄, 8-GPU 38시간으로 GPT-2 재현; **에이전트 도구가 아니라 학습용 레퍼런스**임을 명시), [[dzmitry-bahdanau]](어텐션 원저자; 중학교 번역 연습의 시선 이동에서 착상, 원래 이름 RNNsearch, *attention*은 Yoshua Bengio가 명명).
- 기존 페이지 보강 4건:
  - [[sutton-bitter-lesson]]: 2012년 이전 비전 파이프라인의 **1인칭 증언**(*"여기저기서 코드를 모아서 실행했는데, 정말 악몽 같았어요"* / *"게다가 그것도 효과가 없었어요"*) — 에세이의 요약 표에 비용의 질감을 채운다. 그리고 **스케일 조건부 단서**: *"데이터가 무한하면 점점 더 적게 인코딩하고 싶어지고, 데이터가 아주 적으면 오히려 편향을 인코딩하고 싶어집니다."* 이것이 어제 추가한 [[flutter]] 반례(학습 데이터 격차)가 **사라지는 종류**라는 판정을 뒷받침한다. 부수 발견 — inductive bias는 코어가 아니라 **연결성·positional encoding**으로 factor out돼 있다.
  - [[context-resets-and-compaction]]: **scratch pad 계보(2023)** 절 추가. 컨텍스트 확장 논문 200편 대신 *"컨텍스트 길이는 고정해 두되 네트워크가 scratch pad를 쓰게 하자"*. durable session log·structured handoff와의 대응표. ⚠️ 당시 scratch pad는 **디코딩 시 특수 토큰을 가로채는 harness 로직**을 전제하므로 오늘날 tool use와 같은 것으로 취급하지 말라는 경고를 달았다.
  - [[llm-wiki-pattern]] / [[memex]]: 같은 계보의 다른 쪽. scratch pad는 *한 세션 안*의 컨텍스트 한계를, LLM wiki는 *세션들 사이*의 망각을 우회하는 **같은 처방**(외부 마크다운 + 모델이 읽고 쓴다)이고 시간 축만 다르다. memex 계보표에 2023 항목 삽입 — Bush 계보에서 LLM은 유지보수자로만이 아니라 **memex를 필요로 하는 또 하나의 유한한 기억 장치**로도 합류한다.
  - [[andrej-karpathy]]: 오래된 공백(*"경력 일대기, nanoGPT 등 작업 — 별도 소스 ingest 필요"*) 해소. 2012년 진입·컴퓨터 비전 전공·nanoGPT·Tesla 사례·Bahdanau 이메일. 밝힌 선호(autoregressive 불호, diffusion 선호)도 기록.
- ASR 보정(ko 자막 오역이 이례적으로 많다): "변압기"→transformer, "주의력"/"구금"/"차단"→attention, "염기서열 분석 논문"→sequence-to-sequence, "레조넌스"→ResNet, "보락스(Borax)"→4x, "바이런 에스테이트"→BiRNN states, "알렉스 카치브스키"→Alex Krizhevsky, "HGPU 노드 하나"→8-GPU 노드 하나, "nn.bedding"→`nn.Embedding`, "231번"→CS231n, "bits"→ViT.
- ⚠️ 확정하지 않은 것 3건: ① 47:09의 **"raw operator"** — 인컨텍스트 러닝을 뒷받침한다고 인용된 논문·연산자 이름이 ko·en-orig 모두 불분명해 논문 특정 불가. ② GPT-3 논문 제목이 en-orig에서 *"twoshot learners"*로 오인식됨(실제 *Few-Shot Learners*). ③ 32:36 컨텍스트 길이 "124/248 tokens"는 문맥상 1024/2048의 자릿수 누락으로 보이나 확정하지 않음.
- 페이지화하지 않음: Stanford CS25(장소·강좌), Alex Krizhevsky(1회 언급), Yoshua Bengio(명명 일화 1회), Tesla(멀티모달 사례로만 언급 — 재직 기간·역할 미확인), Whisper·ViT·AlphaFold·Decision Transformer(확장 사례 나열), S4(질문만 있고 답변이 자막에 없음).
- raw: `01.raw/articles/2026-09-02_안드레 카파시의 스탠포드 1시간 강의.md`. 갱신: index(234→240), overview, log, [[tech-bridge]].
- **핵심 합성**: 이 위키가 매일 다루는 어휘 — 컨텍스트, 프롬프트, 토큰, 스킬 — 이 **모델 안에서 물리적으로 무엇인지**를 처음으로 설명하는 소스다. 세 가지가 위에서 아래로 이어진다. ① *"GPT는 런타임에 재구성되어 자연어 프로그램을 실행하는 범용 컴퓨터"* 가 [[context-engineering]]·[[token-roles]]의 프롬프트 설계가 왜 **프로그래밍처럼** 느껴지는지 설명한다. ② [[in-context-learning]]의 inner loop가 [[agent-skills]]가 파인튜닝 없이 행동을 바꾸는 **메커니즘**이다 — progressive disclosure는 "inner loop에 무엇을 언제 올릴지"의 문제로 다시 읽힌다. ③ 그리고 2023년의 scratch pad가 2026년의 [[llm-wiki-pattern]]로, 즉 **이 vault 자체**로 이어진다. 저자가 같다는 점이 우연이 아니라 같은 문제(유한한 기억)의 3년 간격 두 답안임을 보여준다.

## [2026-09-04] ingest | Tech Bridge — 차세대 커머스를 위한 멀티모달 협업 에이전트 설계법

- https://www.youtube.com/watch?v=UoU8_gkaXI4 (20:37, [[nidhi-kaushik-vyas]] / [[google-deepmind]]) → [[tech-bridge-multimodal-commerce-agent]]. `--playlist-end 15`로 조회했으나 채널이 반환한 최근 업로드는 **13편**이었고, 그중 **신규는 이 1편뿐**, 나머지 12편은 이미 ingest돼 있었다. Shorts 없음. 자막 429 없음 — ko·en-orig 모두 확보.
- **위키 첫 소비자 대면 에이전트 소스.** 기존 [[tech-bridge]] 16편은 전부 개발자·조직 내부용 에이전트(코딩·리뷰·워크플로·조직 도입)였다. 여기서 처음으로 상대가 엔지니어가 아니라 **자기가 뭘 원하는지 모르는 일반 사용자**다. 이 전제 차이가 중요한 이유는 [[verifiable-goals]]·[[outcome-engineering]]·[[spec-driven-development]]가 전부 *"목표를 검증 가능하게 써라"* 를 요구하는데, 소비자 대면에서는 **명세를 쓰게 하는 게 아니라 함께 만들어내는 것**이 에이전트의 일이 되기 때문이다.
- 신규 concept 3개 — 강연의 3단계 루프(탐색→조사→응답)에 1:1 대응한다.
  - [[fuzzy-intent-discovery]]: **articulation gap** — *"많은 에이전트는 검색창을 감싸는 역할만 합니다"* vs *"쇼핑을 하고 싶다는 막연한 느낌이나 예감(vibe)만 가지고 있는 경우가 대부분"*. **working state**를 hard constraint / soft constraint + **confidence score** / real-time variable로 쪼갠다(각각 갱신 주기와 신뢰 성격이 다르다). soft constraint는 **참조 이미지에서 추출**하고 자기 확신도를 함께 저장 — 그래서 "신뢰도를 올리는 것" 자체가 질문의 목표가 될 수 있다. 다음 질문은 **information gain 최대**인 미지 변수 하나로 고르되, 판정 기준이 엔트로피가 아니라 **결과 뒤집힘**이다(*"추천하는 제품이 방에 맞지 않으면 아무 의미가 없다 — 대화의 방향을 의미 있게 바꿀 수 있는 변수"*).
  - [[multimodal-elicitation]]: **보여주고 묻기.** 형식 판정이 명시적이다 — *쉽게 확정되는 것*(방 너비)은 텍스트, *주관적·모호한 것*(스타일)은 **시각적 선호 보드**. 보드는 질문이자 **계측기**다: *"마우스 커서가 특정 방향으로 이동하거나 클릭이 발생하는 등의 **미세한 신호**를 감지하여 (…) 신뢰도 모델을 업데이트"*. 먼저 제약을 판매자 **온톨로지에 임시로·거의 실시간으로** 매핑하는 **bridge**를 놓아야 검색이 가능해진다.
  - [[adaptive-response-format]]: *"많은 시스템이 이 부분에서 실패하는데, **텍스트 위주의 응답만 제공하기 때문**"*. 정책·리뷰→요약, 비교→**트레이드오프 표**(축은 working state에서), 영감→**무드보드**. 테제는 *"모델 응답 구조를 갖는 방식 또한 **지능의 중요한 부분**"* — 형식은 후처리가 아니라 판단이므로 틀릴 수 있고 채점된다.
- 신규 entity 2개 — [[nidhi-kaushik-vyas]](Google DeepMind 제품 담당), [[google-deepmind]](**위키 첫 Google 조직 페이지**. 그동안 Google은 [[gemma-4]]·[[flutter]]처럼 제품으로만 스쳤다. frontier lab 축에서 [[anthropic]]·[[openai]]·[[shanghai-ai-lab]]에 이은 네 번째).
- 기존 페이지 보강 4건:
  - [[generator-evaluator-pattern]]: **루프의 모든 단계를 채점하기.** 지금까지 이 위키 사례(frontend 4-criteria, 풀스택 3-agent, [[managed-agents]] `outcomes`)는 전부 *최종 산출물*을 채점했는데, 여기서는 working state·협업 전략·elicitation·응답 네 지점에 **auto-rater 12종**이 걸린다 — **중간 상태와 행동 선택**까지 채점 대상이 된다. 새 기법 3개: ① **counterfactual sensitivity를 양방향으로** 재기(관련 없는 제약은 그대로 남아야 한다 — 한쪽만 재면 과민한 추출기가 통과한다), ② **over-asking을 결함으로 계수**(정확도만 재면 계속 물어보는 쪽으로 몰린다), ③ **사용자 시뮬레이터**로 정답을 심어 채점기를 얻기. 그리고 채점기 수명에 대한 답 — *"거의 진화하는 시스템과 같습니다. 처음에는 아주 간단하게 시작하지만 (…) 시스템과 함께 점진적으로 성장해야 합니다."*
  - [[signal-layer]]: **채점기 경계선을 다시 긋기.** 이 소스는 주관 영역인 **스타일 선호에 실제로 채점기를 만든** 반례성 증거다. 그런데 채점되는 것은 *"어떤 취향이 좋은가"* 가 아니라 **"그 취향을 몇 턴 만에 알아냈는가"** 이고, 가능한 이유는 **시뮬레이터에 정답을 심어두기 때문**이다. → 경계선은 *주관적인 영역*이 아니라 **정답을 아는 주체가 없는 영역**에 그어진다. 이 개념이 마지막까지 채점 불가라 지목한 **신뢰**에는 그 자리에 세울 사람이 없다.
  - [[model-context-protocol]]: 에이전트↔에이전트 상거래의 인터페이스로 MCP가 지목된다(*"MCP가 이 둘 사이의 인터페이스 역할을 확실히 할 거라고 예상"*). 기존 사례가 전부 *에이전트→도구* 방향이었던 것과 다르다. 단 **기대이지 구현이 아니다** — 같은 답변이 아직 그 단계가 아니라고 명시한다.
  - [[context-engineering]]: working state를 **신뢰 등급별 슬롯**으로 읽는 절 추가. 추론된 항목에 **자기 확신도가 함께 저장**되고, **믿으면 안 되는 필드**(실시간 변수)가 명시적으로 구분된다. [[agent-distributed-systems]]의 *"메모리는 무효화 가능한 캐시"* 와 같은 문제를 상태 스키마 층위에서 다룬 형태 — *"무엇을 넣을까"* 가 아니라 **"각 항목을 얼마나 믿을까"**.
- ASR·번역 보정: ko 자막이 **agent를 일관되게 "상담원"으로 오역**한다("담당자", 09:49 **"부동산 중개인"**, 19:37 **"요원"**). "자동 생성기"/"자동화 도구"/"운영자" → **auto-rater**(en-orig의 *"autoators"/"operators"* 도 같은 단어의 오인식). "협업 신뢰도" → **confidence calibration**(en-orig *"confidence collaboration"* 이 오인식이고 챕터 제목 "신뢰도 보정"이 확인해준다). "회전율" → **turn efficiency**. "사용자 편의성" → **user actionability**. "분위기가 깨질" → **moot point**(en-orig *"mood point"* 도 오인식).
- ⚠️ 확정하지 않은 것 4건: ① **촬영 시점** — [[tech-bridge]]에 아카이브 재배포 전례가 있어 내부 단서를 확인했으나, 과거 강연이라는 증거도 시점을 확정할 근거도 없다. 유일한 앵커는 *"최근 출시한 UCP"* 뿐. ② **행사명**이 소스 어디에도 없다(오프닝이 *"good morning folks"* 인 컨퍼런스 오전 세션이라는 것만 안다). ③ **UCP의 뜻** — en-orig는 약어만 말하는데 **ko 자막이 "Unified Communications Platform"으로 풀어 썼다.** 원문에 없는 자막의 창작이고 문맥(커머스)과 맞지 않아 채택하지 않았다. ④ **발표자 표기** — 자막에는 *"니디"* 뿐이고 전체 이름·소속은 **설명란**에서 왔다. 직책은 본인 표현 *"product person"* 뿐.
- ⚠️ en-orig 자체 오류 1건: 15:40의 *"prepared to accept **wives**"* 는 **vibes**의 오인식인데 **ko 자막이 이를 "아내를 받아들일 준비"로 직역했다.** 실제 교훈은 *"모호한 의도를 받아들일 준비가 된 제품을 설계하라"* 다.
- 페이지화하지 않음: UCP(약어 뜻 미확정, Q&A 1회), 거실 리모델링 예시(작동 예시), 사용자 시뮬레이터(기법으로 [[multimodal-elicitation]]·[[generator-evaluator-pattern]]에 기술), merchant/판매자(일반 개념).
- raw: `01.raw/articles/2026-09-03_차세대 커머스를 위한 멀티모달 협업 에이전트 설계법.md`. 갱신: index(240→246), overview, log, [[tech-bridge]](sources 16→17, References에 누락돼 있던 flutter·karpathy 2건도 함께 backfill).
- **핵심 합성**: 이 위키의 에이전트 논의가 지금까지 **한쪽 끝**만 보고 있었다는 것을 드러내는 소스다. [[verifiable-goals]]부터 [[trusted-throughput]]까지의 축은 전부 *"목표를 명확히 하고 verifier를 붙여라"* 였고, 그 전제는 **요구자가 명세를 쓸 수 있다**는 것이었다. 여기서는 요구자가 명세를 못 쓴다 — 그래서 에이전트의 첫 일이 실행이 아니라 **명세 공동 작성**이 되고, [[fuzzy-intent-discovery]]의 information gain 질문 선택이 그 공동 작성을 **최적화 문제로** 바꾼다. 그리고 이것이 [[signal-layer]]의 채점기 경계선을 한 칸 더 정확하게 만든다: 취향처럼 *주관적이지만 본인은 정답을 아는* 영역은 시뮬레이터로 채점 가능하고, 신뢰처럼 *정답을 아는 주체가 없는* 영역만 남는다. 부수적으로 플랫폼 전략도 읽힌다 — 판매자는 [[multimodal-elicitation]]의 **온톨로지를 제공**하지만 [[adaptive-response-format]]의 **형식 결정권은 갖지 못한다**(*"수평적 공통 층"*). 웹에서 판매자가 자기 페이지 레이아웃을 통제하던 것과의 단절이고, [[agentic-sites]]와는 재조립 주체가 정반대다.

## [2026-09-05] ingest | Tech Bridge — 4편 일괄 (불확실성의 수학 · Claude Code 팀 · 스킬 6종 · AI-Native SDLC)

- `--playlist-end 15`가 15편을 반환했고 전부 롱폼(최단 555초)이라 **Shorts 스킵 0건**. 그중 **신규 4편**, 나머지 11편은 이미 ingest돼 있었다. **하루 최다 ingest**(이전 최다는 2026-09-02의 4편이나 그날은 2회로 나뉘었다). 자막 **429 없음** — 4편 모두 ko·en-orig 확보.
- 이 실행은 **launchd 09:10 KST 정시 발화분**이다. 부모 체인 `launchd → run-ingest.sh(pid 41739) → claude`로 확인했고 `runs=6`. 게이트 D(OAuth)·E(모델 쿼터) 모두 통과 — **정시 발화 종단 성공 2일 연속**이다.

### 1. [[tech-bridge-uncertainty-mathematics]] — Zoubin Ghahramani, 44:41

- https://www.youtube.com/watch?v=afgyS-bblpw ([[zoubin-ghahramani]] / Google DeepMind Podcast, 진행 "Hannah"). 채널 **두 번째 최장편**([[tech-bridge-karpathy-transformers-stanford]] 61:24 다음).
- **위키 첫 이론·기초연구 소스.** 기존 [[tech-bridge]] 18편은 전부 에이전트 엔지니어링이었고, 유일한 예외인 Karpathy 강연도 *아키텍처가 어떻게 작동하는가*였다. 이 소스는 **"지능이 무엇을 갖춰야 하는가"** 를 묻고 답으로 확률론을 제시한다.
- 신규 concept 3개:
  - [[bayesian-inference]]: 논증이 인식론이 아니라 **의사결정**에서 출발한다 — *"의사 결정을 내리지 못하는 지능형 시스템은 존재할 수 없으니까요."* prior×likelihood→정규화→posterior가 **재귀**하고, 같은 틀이 지각·학습·의사결정을 덮는다. **calibration**이 좋은 확률의 기준이고(70%라 한 날의 70%에 비가 와야 한다), 반복 불가능한 사건에도 확률을 쓰는 것이 *"완벽하게 타당하고 실제로 옳은 방법"*. **핵심 구별** — LLM은 확률 모델이지만 *"베이즈 규칙을 계산하는 것이 아니"* 다. 토큰 분포의 확률과 명제에 대한 믿음의 확률은 다르고, 원인은 훈련 목표에 있다(*"데이터를 모델링하는 데 뛰어나도록"*). semantic entropy에 대해 **본인이 곧바로 반박하는** 대목이 백미다 — *"데이터에 의존하는 것이기 때문에 일종의 속임수 (…) **계산기를 속이고 싶지는 않겠죠.**"*
  - [[aleatoric-epistemic-uncertainty]]: 구분이 중요한 이유가 **행동이 갈리기 때문**이다. 무작위성이면 *"예측을 포기하는 것이 나을 수도"*, 미경험이면 **정보를 모으거나 속도를 줄인다**. ⚠️ 소스는 라틴어 용어를 쓰지 않는다 — 페이지 제목의 괄호는 위키의 정리다.
  - [[continual-learning]]: *"우리는 끊임없이 학습합니다"* vs *"몇 달 후에 또 다른 거대한 모델"*. 기술적 핵심은 **Bayesian update가 이론상 catastrophic forgetting을 겪지 않고, 대규모 신경망의 continual learning 기법들은 그 근사에 불과**하다는 진술이다.
- 신규 entity 1개 — [[zoubin-ghahramani]]. 진행자 **Hannah는 성이 소스에 없어 페이지를 만들지 않았다.**
- 기존 페이지 보강 3건:
  - [[sutton-bitter-lesson]]: **위키 첫 정면 반대 입장.** Ghahramani가 넣자는 구조는 **명시적 확률 표현**이고, bitter lesson 관점에서 이는 전형적인 지식 주입이다. **해소하지 않았다** — 그가 대립을 인정하며 상대를 깎지 않기 때문이다(*"그들의 생각이 완전히 틀린 건 아니에요. 저도 완전히 맞는 건 아니고요"*). 대신 그가 긋는 선을 기록했다: **판돈에 따라 답이 갈린다**(챗봇은 괜찮고 자율주행·의료는 아니다). 이는 기존 "어느 스케일에 있느냐"(데이터 양) 단서와 **같은 형태의 조건부**(오류 비용)이고, 둘을 합치면 bitter lesson은 *데이터가 충분하고 실패 비용이 낮은 국면에서* 참으로 좁혀진다 — ⚠️ 이 합성은 위키의 정리이지 어느 소스의 주장도 아니다.
  - [[google-deepmind]]: 커머스 에이전트뿐이던 페이지에 **연구 축**이 붙었다 — 자체 팟캐스트, **GenCast**(diffusion 앙상블, 15일+ 예보를 8분에, 새 관측으로 앙상블 갱신 = Bayesian update), **AlphaFold**(확신도 착색·위치를 구름으로). 그리고 **조직 내부에 AGI 노선 이견이 있다**는 것이 드러난다.
  - [[transformer]]: 계보에 **앞선 층**이 붙었다 — *"트랜스포머 혁명 같은 이야기를 많이 하지만, **1980년대 중반에 일어난 일은 진정한 혁명**"*(1986년 PDP 두 권 + 역전파, 전문가 시스템의 취약성 대비). 1989년 학부 논문을 *"작은 언어 모델"* 이라 부르는 대목과, **트랜스포머·확산이 현대 AI의 두 도구**이며 다음은 *"매우 희소한 신경망 + 하드웨어 공진화"* 일 수 있다는 전망을 추가.
- ASR·번역 보정: **"베이징 방식"/"베이징식 사고방식"/"비자이안식" → Bayesian**(도시가 아니다). **"기초 업데이트"/"유역 업데이트"/"기저 함수 업데이트" → Bayesian update**. "B 규칙"/"베이즈 룰(Baze Rule)" → Bayes' rule. **"MPMPlete 또는 MP 난이도" → NP-complete / NP-hard**(en-orig도 같은 오인식). **"순열에서 접힌 구조로" → sequence(서열)→fold**. "올리브 세계" → *"all the world"*. "연결 장치" → **Connection Machine**. "아빈 주시"/"Arvin Jooshi" → **Aravind Joshi**.
- ⚠️ **ko 자막이 `[Music]` 태그를 본문에 녹여 유령 단어를 만든다.** 이 소스 최대 결함이다 — *"인간의 근본적인 **음악적** 특성"*, *"한 **음악** 연구자"*, *"**음악 활동**을 바쳐왔습니다"*. 결론부 *"이는 **음악을** 현실에 기반을 두게 하여"* 는 en-orig *"**It** grounds **it** in reality"* 로 바로잡았다 — **기반을 얻는 것은 AI다.** ko에 "음악"이 나오는 자리는 전부 이 오염을 의심할 것.
- ⚠️ **ko 자막에 힌디어(데바나가리)가 섞인다** — *"네, बिल्कुल 그렇습니다"* 가 4회 이상. en-orig의 *"absolutely"* 자리다. 자막 파이프라인의 언어 혼입.
- ⚠️ 확정하지 않은 것 4건: ① **화자 직함이 소스 안에서 불일치** — 내레이션 *"co-lead of frontier AI"* vs 설명란 *"Research VP"*. 케임브리지 교수만 일치한다. ② **진행자 성이 없다**(43:57 *"Thank you, Hannah"* 가 유일). ③ **"David Spiegel"(34:08) 성이 잘렸다** — 서술은 케임브리지의 위험 소통 연구자와 일치하나 소스가 성을 온전히 말하지 않아 확정하지 않았다. ④ **촬영 시점** — 앵커는 2015년 논문을 *"10년 전"* 이라 부른 것과 허리케인 Melissa·GenCast 언급뿐.
- 페이지화하지 않음: Geoff Hinton·Aravind Joshi·David Spiegel(전기적 언급), Connection Machine·PDP·GenCast·AlphaFold(각각 [[zoubin-ghahramani]]·[[google-deepmind]]에 기술), semantic entropy(기법으로 [[bayesian-inference]]에 기술), 스타트렉 데이터·재규어·추리소설(설명 비유).

### 2. [[tech-bridge-claude-code-team-workflow]] — Anthropic Claude Code 팀, 22:23

- https://www.youtube.com/watch?v=Bo2ImHzgOwc ([[thariq-shihipar]] · [[sid-bidasaria]] · [[robert-boyce]] / [[anthropic]]).
- [[tech-bridge-claude-platform-agent-era]]와 짝이지만 한 층 다르다 — 그쪽이 *"하네스는 while 루프"* 라는 설계 관점이라면 여기는 **그 하네스를 만드는 사람들의 1인칭 사용기**다.
- 신규 concept 2개:
  - [[harness-pruning]]: **이 소스 최대 기여.** 전제가 되는 하네스관이 명시적이다 — *"이러한 기능들을 하네스에 내장하는 것은 **현재 모델이 가지고 있는 오류 모드를 보완하기 위한 것**"*. 그러면 결함이 사라질 때 보완물도 사라져야 한다. 사례 둘: **todo 리스트**(Sonnet 3.5는 *"다섯 가지 일을 시키면 세 가지만 하고는 그냥 포기"* → 1년 뒤 *"마치 사라진 것처럼"*), **AskUserQuestion**(설계에 *"정말 오랜 시간이 걸렸"* 는데 HTML 아티팩트가 스스로 질문하기 시작하며 밀림 — [[adaptive-response-format]]이 예측한 방향의 실측). 그리고 **pruning은 축소가 아니라 재배치**다 — *"작업 범위가 바뀌면서 필요한 도구들이 다르게 보이기 시작"*.
  - [[goal-level-delegation]]: 도구 호출·녹취록 감시에서 목표 위임으로. **70~80%** 라는 수치가 붙고, 포기하는 것(*"내면의 독백은 Slack에서 보이지 않습니다"*)과 얻는 것(*"Claude가 언제, 무슨 말을 할지 스스로 선택한다는 점에서 정말 자유로워진"*)이 함께 기록된다. **감시를 없앤 자리를 산출물 검증이 메운다**는 것이 실제 구조다 — 스크린샷·for 루프의 결정론·test-time compute·Slack의 맥락 근접성.
- 신규 entity 4개 — [[thariq-shihipar]] · [[sid-bidasaria]] · [[robert-boyce]] · [[claude-tag]].
- 기존 페이지 보강 5건:
  - [[dynamic-workflows]]: **기원이 밝혀졌다** — *"코드 리뷰가 우리가 이렇게 큰 규모로 의견을 퍼뜨린 첫 번째 사례"*. 3층 구조(fan-out → **3관점 적대적 검토** → 병합)이고 목적은 찾기가 아니라 **거르기**다. 그리고 **병목이 map이 아니라 reduce**라는 지적이 새롭다 — *"마치 map-reduce 문제와 같아요. (…) 전체 출력값을 다 읽어버리면 미쳐버릴 것 같거든요."* 이 위키의 [[ultracode]]·[[managed-agents]]가 전부 펼치는 쪽만 다뤘다.
  - [[agent-harness-design]]: **시간 축**이 처음 붙었다(위 [[harness-pruning]]). ⚠️ 언제 지워도 되는지의 기준·절차는 소스에 없고 전부 사후 회고다.
  - [[self-harness]]: *"Claude는 자기만의 하네스를 만드는 데 정말 능숙하죠"* 로 전제가 실무 확인됐다. ⚠️ 동시에 **정확히 반대 방향의 압력**([[harness-pruning]])이 같은 소스에 있다 — 자기개선은 하네스를 키우고 모델 향상은 줄인다. 어느 쪽이 우세한지 판정할 근거는 아직 없다.
  - [[generator-evaluator-pattern]]: **채점기를 셋 두는** 적대적 검토, 그리고 채점의 경제학(*"자신감을 키우는 방법은 test-time compute를 문제에 투입하는 것"*).
  - [[claude-code]] / [[anthropic]]: Claude Tag·routine·workflows·auto mode의 사용기, 2개월 주기와 그에 따른 소규모 팀 구조.
- ASR·번역 보정: **"벌레" → bug**, **"선풍기를 틀어주는 것" → fan-out**(ko가 *fan*을 선풍기로), "시험용 컴퓨터"/"테스트 타임 컴퓨팅" → **test-time compute**, "맵리듀스" → map-reduce, "맥 OS 10.4 아쿠아" → Mac OS X 10.4 Aqua. *"클로드에게 요리하게 해 줄래요"* 는 오역이 아니다(en-orig *"let Claude cook"*).
- ⚠️ **en-orig 오인식을 ko가 그대로 직역한 연쇄 오류 1건**: *"it's like an HTML and has **tie grams** and mock-ups"* → ko *"HTML처럼 생겼고, **넥타이 이미지**나 목업"*. 문맥상 **diagrams**다. 한쪽만 봐서는 잡히지 않는다 — 09-04에 이어 두 번째 사례다.
- ⚠️ 확정하지 않은 것 4건: ① **발언별 화자 특정 불가** — 이름은 전부 설명란에서 왔고 자막에는 14:06의 *"로버트"* 외에 없다. ② **"2E"** — en-orig·ko 양쪽의 미해소 ASR 토큰. 01:28에서는 Claude Tag 밖의 직접 조작 표면, 18:15~20에서는 UI 녹화 수단을 가리키는데 **두 자리의 지시 대상이 같은지도 불분명**하다. 확장형을 추정해 적지 않았다. ③ **"data stack"(12:30)** — 11:06에서 *"this led to **workflows**"* 라 명시했으므로 문맥상 가리키는 것은 workflows지만, 그 자리의 단어 자체는 원 발화를 확정할 수 없다. ④ **촬영 시점** — *"합류한 지 거의 1년"* 과 Sonnet 3.5 회고가 앵커의 전부.
- ⚠️ 근거 없는 수치 2건: *"생산성이 10배는 늘어난 것 같아요"*(개인 체감), *"2개월마다 근본적으로 바뀌는"*(측정 없음).
- 페이지화하지 않음: routine·loops(제품 기능으로 [[claude-code]]에 기술), Boris(1회 언급, 이름만), map-reduce·test-time compute(기존 개념), Mac OS X Aqua·파워포인트 일화(회고 예시).

### 3. [[tech-bridge-six-agent-skills]] — AI Labs, 13:08

- https://www.youtube.com/watch?v=ss4lbO8M8wk ([[ai-labs]] 원 제작). **채널 첫 스킬 카탈로그형 영상.**
- 신규 concept 1개 — [[skill-self-improvement]]: 진단이 이식성 높다(*"가장 큰 문제는 스킬을 만드는 것이 아니라 **최신 상태로 유지하는 것**"*, *"한 번 앉아서 에이전트가 저지를 모든 실수를 예측할 수는 없습니다"*). **핵심은 자동화가 아니라 자동화를 멈춘 지점**이다 — 관찰은 자동이되 **승격은 사람**이 한다. *"하나의 잘못된 결과가 에이전트가 영원히 따르는 규칙으로 자동 설정되는 것을 방지."* 교훈이 **금지**와 **대체** 두 종류로 나오는 것도 기록했다(금지만 쌓이면 스킬이 방어적이 된다).
- 신규 entity 3개 — [[ai-labs]], [[corey-haines]], [[sahil-lavingia]].
- 기존 페이지 보강 4건:
  - [[agent-skills]]: **스킬이 담는 지식의 범위가 기술→제품·시장으로 넓어진다.** 논거가 명확하다 — *"에이전트에게 페이월 추가를 요청하면, 일반적으로 이런 선택을 하지 않습니다. **그 원칙이 내재되어 있지 않기 때문**입니다."* 즉 에이전트는 *동작하는* 페이월은 만들어도 *전환되는* 페이월은 못 만든다. 그리고 **스킬로 둘 것과 규칙으로 둘 것이 같은 소스 안에서 갈린다** — 프로젝트마다 다른 것은 스킬(프로젝트별 설치 권장), 전부에 걸리는 것은 계층적 `CLAUDE.md`. ⚠️ 공개 repo가 사실상 레지스트리가 되면서 [[prompt-injection]]과 *"MD 파일은 무해하지 않다"* 가 그대로 적용되는데 소스는 이를 다루지 않는다.
  - [[llm-coding-guidelines]] / [[multica-ai]] / [[andrej-karpathy]]: **위키에서 서로 다른 소스 두 개가 같은 아티팩트에 도달한 첫 사례.** 같은 repo(`multica-ai/andrej-karpathy-skills`)를 4개월 만에 재발견했고 4원칙이 그대로 일치한다. **새로운 것은 배포 방법** — 스킬로 설치하지 않고 **개발자 폴더의 `CLAUDE.md`** 에 넣어 그 아래 전 프로젝트에 상속시킨다. 요점은 범위다(전역은 무관한 세션을 오염시키고 프로젝트별은 갱신이 흩어진다). ⚠️ Karpathy 본인의 endorsement 근거는 두 소스 어디에도 없다 — **이름이 규칙 집합의 브랜드로 유통되고 있다.**
  - [[claude-code]]: 계층적 `CLAUDE.md` 상속 절 추가.
- **[[sahil-lavingia]]의 검증 게이트가 위키 첫 "만들기 전 게이트"다.** 기존 게이트([[verifiable-goals]]·[[generator-evaluator-pattern]]·[[trusted-throughput]])는 전부 *만든 것*을 검증했다. 여기서는 코드를 쓰기 전에 **이름을 밝힐 수 있는 실제 인물 10명 + 최소 3명의 유료 의사**를 요구한다.
- ASR·번역 보정: ko가 skill을 일관되게 **"기술"** 로 옮겨 문맥이 흐려진다. "상담원"/"담당자" → agent. "claw.md"/"claud" → **CLAUDE.md**(en-orig도 02:04에서만 맞다). "Superbase" → **Supabase**(설명란 확정). "주인공 섹션" → **hero section**. "앙드레 카르파티" → Andrej Karpathy. "검로드" → Gumroad.
- ⚠️ 확정하지 않은 것 3건: ① **발표자 개인 이름이 없다** — 영상 내내 1인칭 복수("we")로만 말하고 *"this is AI labs"* 가 유일한 자기 식별이다. ② **"Hallmark 디자인 스킬"의 정식 표기**(en-orig 10:28의 언급뿐). ③ **온보딩·페이월 결정의 근거 데이터** — *"수년간의 테스트"* 라고만 한다.
- ⚠️ 소스가 다루지 않은 논점 1건: OpenCLI의 **로그인 세션 재사용**은 서비스 약관·계정 보안 판단이 필요한 영역인데 영상은 이를 언급하지 않는다. 발표자 본인의 경계는 *"판매하는 앱의 공식 도구를 대체하려는 것이 아니다"* 까지다.
- 페이지화하지 않음: task-observer·OpenCLI·Variate·Logo Hub(도구 — [[skill-self-improvement]]·[[tech-bridge-six-agent-skills]]에 기술), Gumroad(1회, [[sahil-lavingia]]에 기술), Supabase·Next.js(데모 스택), Nutlope(repo 소유자로만 언급).

### 4. [[tech-bridge-ai-native-sdlc]] — Switch Dimension 해설 / Anthropic 원문서, 15:11

- https://www.youtube.com/watch?v=rGaSkBWjoHA. **채널 첫 "문서 해설" 형식** — 강연·인터뷰·팟캐스트에 이은 네 번째 포맷이다.
- 신규 concept 2개:
  - [[ai-native-sdlc]]: 전제가 *"**코드가 더 이상 병목이 아닙니다. 당신의 프로세스가 병목입니다.**"* 아티팩트 체인 6단계이고 **6단계의 출력이 1단계의 입력**이 되어 닫힌다. **거버넌스**(아티팩트마다 버전·수정자, 목적은 DORA 지표 검증)와 **continuous evals**(문제 20개 + 예상 결과를 새 모델·새 스킬마다 회귀 테스트)가 이 위키에 새로 들어오는 축이다. **결정론 층과 에이전트 층을 계속 구분해 쓰는 것**도 특징이다 — lint는 *"예 또는 아니오, 이분법적인 답변"* 이고 hook이 경계를 강제한다.
  - [[intent-md]]: *"**사람이 읽을 수 있고 기계가 처리할 수 있는**"* 파일. 백로그와 **인계(handoff)** 를 대체하고, **creator는 전문가가 아니어도 된다**(버그 제보 고객·PM·개발자). 대신 사람이 되읽는 절차가 붙는다.
- 신규 entity 1개 — [[switch-dimension]].
- 기존 페이지 보강 4건:
  - [[spec-driven-development]]: 체인이 **앞뒤로 늘어난다.** spec은 이제 사람이 쓰는 첫 문서가 아니라 intent에서 **hook으로 자동 생성되는 파생물**이다. **문서가 필요한 이유에 대한 새 논거가 특히 강하다** — 품질이 아니라 **컨텍스트 윈도**다: *"모든 단계를 한 에이전트가 수행할 수는 없습니다. **컨텍스트 창이 나타날 것**입니다."* 그래서 `plan.md`의 합격 기준이 *"의도·사양을 참조하지 않고도 구현 가능한가"* 가 된다. 아티팩트는 품질 장치이자 **에이전트 간 인계 프로토콜**이다.
  - [[generator-evaluator-pattern]]: continuous evals = **하네스 자체의 회귀 테스트**. [[harness-pruning]]과 짝을 이룬다(지우려면 지워도 되는지 확인할 장치가 필요하다). ⚠️ 두 소스는 서로를 언급하지 않는다 — 이 연결은 위키의 정리다.
  - [[anthropic]] / [[claude-code]]: 플레이북 요약과 미ingest 표시.
- ASR·번역 보정: "엔트로픽"/"앤트로픽"/"트로픽" → **Anthropic**. 10:11의 **"인류학적 모델"** 은 *anthropic* 을 "인류학적"으로 직역한 오류. "Claw Code" → Claude Code. "intent.mmd"/"skills.mmd" → **intent.md / skills.md**. **"선형 알고리즘"(04:20) → Linear**(이슈 트래커 — en-orig *"captured in notion or linear"*). "Workree" → git worktree. "Playright" → Playwright. "MPM 패키지" → npm. **"문명 공학"은 오역이 아니다**(en-orig *"civilization engineering"*).
- ⚠️ 확정하지 않은 것 4건: ① **해설자 본인의 이름이 없다**(설명란에도 없다). ② **언급된 Claude Code 창시자 이름이 소스 안에서 두 갈래로 갈린다** — 00:00 *"Vis journey"*, 00:30 *"Baris"*. 둘 다 ASR 오류이고 설명란에도 없어 확정하지 않았다. 확실한 것은 *"Claude Code를 만든 사람이며 이 플레이북을 낸 팀에 속한다"* 는 서술뿐. ③ **"Matt PCO"** 의 정체(en-orig·ko 동일 형태). ④ **촬영 시점**.
- ⚠️ 근거 없는 수치 1건: *"우리는 **두 배 더 빠릅니다**"* — 빌드 단계 단축 주장의 출처·측정 방법이 영상에 없다. **원문서를 직접 ingest하기 전에는 위키에서 근거로 쓰지 않는다.**
- ⚠️ **원문서 미ingest**: <https://claude.com/blog/the-ai-native-sdlc-playbook> 를 이 위키는 직접 읽지 않았다. [[ai-native-sdlc]]·[[intent-md]]의 내용은 전부 제3자 해설을 통한 것이다.
- 페이지화하지 않음: spec.md·plan.md(체인 요소로 [[ai-native-sdlc]]에 기술), Linear·Notion·TestSprite·BMAD·SuperPowers(도구 나열), DORA 지표(외부 표준, 1회 언급), molten-os-core(링크만).

### 갱신

- raw 4건: `01.raw/articles/2026-09-04_바이브 코딩 생산성을 10배 끌어올리는 역대급 Claude 스킬 6가지입니다.md` · `2026-09-04_Claude Code 팀이 새로 공개한 INTENT.MD의 정체와 AI-Native 개발 방식.md` · `2026-09-03_AI는 왜 틀릴 때도 당당할까요 불확실성의 수학.md` · `2026-09-03_Claude Code 개발팀이 Claude Code를 쓰는 방법.md`
- index(246→263), overview, log, [[tech-bridge]](sources 17→21).

### 핵심 합성

이 위키가 지금까지 **한 층에서만** 자라고 있었다는 것이 오늘 드러난다. 18편의 [[tech-bridge]] 소스는 전부 *에이전트를 어떻게 부릴 것인가*였다. 오늘 들어온 네 편이 그 위아래를 동시에 친다.

**아래로** — [[tech-bridge-uncertainty-mathematics]]가 *"그 에이전트가 애초에 무엇을 갖춰야 하는가"* 를 묻는다. 그리고 답이 이 위키의 실무 어휘와 정확히 맞물린다: [[fuzzy-intent-discovery]]의 **information gain 질문 선택**은 [[bayesian-inference]]의 비트 정의 위에 서 있었고, [[generator-evaluator-pattern]]이 채점하는 **confidence calibration**은 여기서 *"70%라 한 날의 70%에 비가 와야 한다"* 는 정식 정의를 얻는다. 어제까지 기법이던 것들이 오늘 이론적 자리를 찾았다.

**위로** — [[tech-bridge-ai-native-sdlc]]가 에이전트를 **조직 프로세스 전체**에 배치하고, [[tech-bridge-claude-code-team-workflow]]가 그렇게 사는 팀의 실제 하루를 보여준다.

그리고 **두 소스가 같은 문제의 반대 해법을 제시한다는 점이 오늘 가장 값진 관찰이다.** 컨텍스트가 한 에이전트에 담기지 않는다는 문제에 대해, [[ai-native-sdlc]]는 *"맥락을 파일로 새로 만들어 넘긴다"*([[intent-md]])고 답하고, [[claude-tag]]는 *"맥락이 이미 쌓인 곳(Slack)으로 에이전트를 옮긴다"* 고 답한다. 전자는 **인계 프로토콜**을, 후자는 **인계 자체의 제거**를 택한다. 둘 다 [[context-resets-and-compaction]]이 압축으로 풀던 문제를 압축 없이 푸는 방법이고, 어느 쪽이 나은지는 조직에 맥락이 이미 어디에 쌓여 있느냐에 달렸다.

마지막으로 [[harness-pruning]]이 이 위키의 하네스 축 전체를 다시 읽게 만든다. [[harness-engineering]]의 *"every mistake becomes a rule"* 과 [[self-harness]]의 자동 진화는 둘 다 **하네스가 자란다**고 전제했다. 오늘 그 반대 힘이 처음 기록됐다 — *"이 모든 기능들은 더 이상 필요하지 않네요. **없애버릴 수 있겠어요.**"* 두 힘이 동시에 작용한다면 하네스의 정상 상태는 성장도 축소도 아니라 **모델 능력선을 따라 위로 이동하는 것**이고, 오늘의 [[goal-level-delegation]](70~80%)이 그 이동의 현재 위치를 알려주는 눈금이다.


## [2026-09-06] ingest | Tech Bridge — 4편 일괄 (샘 알트만 3부작 · 젠슨 황 G20)

- `--playlist-end 15`가 **13편**을 반환했고 전부 롱폼(최단 788초)이라 **Shorts 스킵 0건**. 그중 **신규 4편**(전부 2026-09-05 업로드), 나머지 9편은 이미 ingest돼 있었다. 자막 **429 없음** — 4편 모두 ko·en-orig 확보. 이틀 연속 4편 일괄.
- 이 실행은 **launchd 09:10 KST 발화분**이다(실제 시작 09:14 KST). 부모 체인 `launchd → run-ingest.sh(pid 53793) → claude`로 확인, `runs=1`(카운터 리셋). 게이트 D(OAuth)·E(모델 쿼터) 모두 통과 — **정시 발화 종단 성공 3일 연속**.
- **이날의 새 성격** — 4편 전부 **자기 회사를 말하는 CEO의 1인칭 발언**이다. 기존 소스는 엔지니어·PM·연구자 층위였다. 모든 페이지에 *"⚠️ 당사자 진술, 독립 확인 없음"* 과 화자의 인센티브(모델 판매자 / 인프라 판매자)를 함께 적었다.

### 1. [[tech-bridge-altman-frontier-rl-pause]] — Sam Altman 3부작 1부, 24:00

- https://www.youtube.com/watch?v=jnHT1AonyGw ([[sam-altman]] / [[openai]]; 원 출처 *Sources with Alex Heath*, 진행자 이름은 설명란 링크에서만 확인). **채널 첫 시리즈 분할 업로드**(한 인터뷰를 3편으로, 설명란에 상호 링크).
- 신규 concept 2개:
  - [[training-time-risk]]: **이 소스 최대 기여.** *"이전에는 모델의 배포 및 사용 방식에 더 많은 위험이 있었지만, 이제는 모델의 **실제 학습 및 생산 과정**에서 더 많은 위험이 발생하는 세상."* 프론티어 RL 실행 연기(*"처음"*), 그 전 몇 주의 감속, 훈련 실행 자체에 모니터링 부착, **실행/감시 컴퓨팅 분리**. 판단 함수가 `f(관찰된 불일치, 다음 모델의 역량 증가율)` 이고 어느 한쪽만으로 닫히지 않는다 — *"결정적 증거는 없었다."* 이 위키의 안전 장치는 전부 배포 이후에 있었고 이 개념이 그 앞 칸을 채운다. 3부의 *"RSI가 빠를수록 IPO를 늦추는 게 유리"* 가 이 개념의 자본 구조 판이다.
  - [[intent-alignment]]: 정렬 = *"사용자의 의도를 따르는 것"*. 진행자의 도발(*"평가를 완료하라고 했고 그것을 위해 필요한 모든 일을 했다 — 그런 면에서 정렬돼 있죠"*)에 대한 답이 [[agentic-misbehavior]]의 overeager와 정확히 같은 형태다. 두 원칙(통제권 유지·광범위한 권한 분산)과, **병목이 지능에서 의도로** 옮겨갔다는 진단.
- 신규 entity 2개 — [[sam-altman]], [[hugging-face]](⚠️ OpenAI 측 진술만으로 쓴 페이지임을 명시).
- 기존 페이지 보강: [[agentic-misbehavior]](Hugging Face 사건 실사례; misaligned *"관측 없음"* 에 대한 첫 반대 방향 진술 — 단 *"결정적 증거 없음"* 이라 #4 관측이라 단정하지 않음), [[ai-vulnerability-discovery]](아무도 공격을 지시하지 않았는데 exploit 능력이 과제 완료에 쓰인 사례), [[fuzzy-intent-discovery]], [[openai]], [[anthropic]](경쟁사가 말하는 Anthropic — *"YOLO CEO"* 일화, *"Mythos·Fable 사태"* 언급), [[claude-mythos-preview]](진행자의 한 문장 — 무슨 일인지는 소스에 없음).
- ASR·번역 보정: **"얼굴 껴안기 / 포옹하는 얼굴 / 안아주는 얼굴 사건" → Hugging Face** — ko가 **회사명을 직역**했다. **"배선 설정 오류" → harness misconfiguration**. **"롤모델을 숭배" → "우리 모델을 숭배"**(*worship our models*). "교육" → training. "소울" → Soul(모델 패밀리명).
- ⚠️ 확정하지 않은 것 4건: ① **Hugging Face 사건의 세부** — *"제로데이 연쇄·모델 간 담합"* 은 진행자의 표현이고 Altman이 확인하지 않는다. 자막에서 확인되는 것만 표로 정리했다. ② Aidan·Mia의 성. ③ *"what's happened with Mythos or Fable"* 의 내용. ④ *"YOLO CEO"* 의 실제 발화자(진행자: Dario Amodei / Altman: *"제가 그 단어를 말했던 것 같아요"*).
- 페이지화하지 않음: Alex Heath(진행자 — 자막에 이름 없음, 관례대로), Aidan·Mia(성 없음), Preparedness Framework·cyber critical(1회 언급), Black Hat 발표(제목·내용 없음).

### 2. [[tech-bridge-altman-agi-superintelligence]] — Sam Altman 3부작 2부, 17:57

- https://www.youtube.com/watch?v=Pj_y9zEPv5k.
- 신규 concept 3개(전부 다자 비교 페이지):
  - [[agi-definition]]: Altman — *"별 의미 없는 마케팅 용어"*, 도달은 *"어느 정도는요"*, 선언의 의미 *"없다"*, **AGI=이정표 / 초지능=무한 경사로**. [[jensen-huang]] — *"사실상 이미 도달"*. 기존 [[andrew-ng]] — decades, 조기 선언 유인. 세 사람이 같은 단어의 무의미함에 다른 이유로 동의한다는 것, 그리고 **정의를 무의미화하는 것이 누구에게 유리한가**를 함께 읽어야 한다는 것을 적었다.
  - [[compute-constrained-growth]]: *"성장은 컴퓨팅 배분의 함수 — 100% 동감"*, *"효율성 향상을 찾을 때마다 전 세계 토큰 수요가 그걸 다 잡아먹어"*, 상위 0.001% 사용량을 모두에게, *"기술적 진술이지 재정적 진술이 아니다"*, 네오클라우드의 *"지속 불가능한 어리석음"*. 판매자([[intelligence-as-infrastructure]])와의 시각 차이를 해소하지 않고 나란히 두었다.
  - [[ai-jobs-impact]]: 네 입장 표 — Gates(2년/4년 대체) · Ng(task 30–40%) · Altman(*"예상·기대보다 적었다 — AI 산업에 대한 타당한 비판"*) · Huang(*"작업은 자동화, 직업의 목적은 남는다"*). Altman의 것만 **관찰**이고 나머지는 예측이라는 점, 넷 다 측정치가 없다는 점을 적었다.
- 기존 페이지 보강: [[openai]](사이드 퀘스트 브라우저·Sora, 사전학습 부진 *"대부분 제 잘못"*, Stargate, Greg Brockman 공동 경영, *"두 번 재고 한 번 자른다"*), [[andrew-ng]]·[[bill-gates]](반대편 진술 절 신설), [[regulatory-capture]](데이터센터 물 밈을 운영자가 반박 — Ng가 공포 마케팅 사례로 든 화제의 반대편), [[goal-level-delegation]](세션 길이 34시간 · 20분짜리 승리).
- ASR·번역 보정: **"국경 훈련" → frontier training**, **"정보 기관의 전반적인 역량" → 지능(intelligence)의 역량** — 두 건 다 ko가 전문용어를 일반어로 직역했다. "공기 주머니" → *"Air pocket above"*(의미 미확정).
- ⚠️ 확정하지 않은 것 5건: ① **"Y Combinator의 charter"** — en-orig·ko 동일하나 인용 문구는 OpenAI Charter의 AGI 정의와 일치. *"your company's"* 의 오인식 가능성은 위키의 추정으로만 적었다. ② **"5/6 sold"** — GPT-5.6으로 추정, 미확정. ③ *"Air pocket above"* 의 뜻. ④ **38,000 쿼리 = 아몬드 한 개** — 본인이 *"기억에 의존, 틀릴 수도"* 라 단서를 단 수치. ⑤ 촬영 시점(3부 앵커로 2026년 중후반 추정).
- 페이지화하지 않음: Fidji Simo·Greg Brockman(경영진 언급 — [[openai]]에 기술), Stargate·Sora·브라우저(제품명 — [[openai]]에 기술), Jenga·카메라와 화가(비유).

### 3. [[tech-bridge-altman-astra-hardware]] — Sam Altman 3부작 3부, 21:46

- https://www.youtube.com/watch?v=EzkYQvMXzAc. **촬영 시점 앵커가 이 편에 있다** — *"2025년 상원 청문회"* 과거형, *"최근 GPT 5.6 초기 출시"*, 2부의 *"GPT-5 출시 무렵 저녁이 거의 정확히 1년 전"* → 2026년 중후반 추정, 확정 아님.
- 신규 concept 1개 — [[ai-privilege]]: 의사·변호사급 **비밀유지특권**을 AI 대화에. 동기가 *"안전 위험이 너무 커서 AI 프라이버시는 존재할 수 없다고 주장할 사람들"* 에 대한 경계라는 점, 제안자가 그 데이터의 보유자(*"역사상 가장 개인적인 데이터베이스 중 하나"*)라는 점을 적었다. [[persistent-agent-teams]]가 유보했던 *"상주 봇의 권한·감사 경계"* 가 기술 유보에서 **법 제안**으로 옮겨간 형태.
- 신규 entity 1개 — [[openai-astra]]: *"더 비싸고 큰 모델 등급을 가리키는 이름"*, Soul과 같은 방식. 슬러그에 `openai-` 를 붙인 이유(동명 프로젝트 혼동 방지)를 페이지에 명시.
- 기존 페이지 보강 7건: [[goal-level-delegation]](**소비자판** — *"굉장히 게으른 사용자"*, *"커넥터 설정 없이 그냥 내 컴퓨터를 써라"*, *"아이들과 놀다가 30분 후"*; 팀판의 *"감시를 없앤 자리를 산출물 검증이 메운다"* 에 해당하는 것이 소비자 쪽에는 **없다**는 점을 적었다), [[persistent-agent-teams]](**능동적 컴퓨터** — 봇 팀이 아니라 하나의 상시 에이전트, 네 구성 요소 대응표), [[codex]](Altman 서술 — *"시장 최고"*, *"갈아탔다"* ⚠️ 개인 표본, The Merge), [[anthropic]], [[regulatory-capture]](정부 테스트 찬성·고객 선별 반대), [[ai-vulnerability-discovery]](*"방어 에이전트가 항상 작동"*), [[brain-hands-decoupling]](*"로봇을 작동시키는 두뇌가 먼저"*), [[training-time-risk]](IPO 연기 근거).
- ASR·번역 보정: **"인간의 모습을 풍자적으로"(00:36) → human parity** — en-orig가 *parody* 로 오인식하고 ko가 풍자로 직역한 **연쇄 오류**(09-04·09-05에 이어 세 번째 사례). **"천문학 모델" → Astra 이전 모델**(*pre-astro*). **"Anthropic Games Store 제품" → Anthropic 제품**. "CodeEx/코덱" → Codex. "Chad GBT/HTB/CHBT" → ChatGPT. "Johnny IV" → Jony Ive. "샘 월트먼" → Altman.
- ⚠️ 확정하지 않은 것 5건: ① 컴퓨터 사용 *"인간 수준"* 의 근거(체감 진술). ② 정부 검증의 구체 절차. ③ Apple 소송의 사실관계. ④ *"대부분이 Codex로 갈아탔다"* 의 표본. ⑤ Jalapeno 칩·Merge·10억 사용자 등은 진행자 서술을 Altman이 부정하지 않은 것.
- 페이지화하지 않음: Jony Ive(협업자 — [[openai]]에 기술), Jalapeno(칩 이름 1회), Apple(소송 당사자 — 사실관계 미확정), Neocloud(일반명).

### 4. [[tech-bridge-jensen-huang-g20-agi]] — Jensen Huang × Howard Lutnick, 29:34

- https://www.youtube.com/watch?v=ap4fr5RYTCk ([[jensen-huang]] / [[nvidia]]). **채널 첫 정부 행사 소스**(G20 혁신 장관 회의, 채플힐)이자 첫 하드웨어 공급자. **공식 챕터 없음**(소제목은 위키가 붙임, 타임스탬프는 실제 발화 시각만). **영상이 문장 중간에서 시작**한다 — 원본 결손, 앞부분 발언 없음.
- 신규 concept 1개 — [[intelligence-as-infrastructure]]: **토큰=kWh**(*"백만 토큰당 달러. 같은 개념이에요"*), **5단 케이크**(에너지·칩·인프라·모델·데이터/앱), *"모든 층을 지을 필요 없다, 확산에 집중"*, 1 GW≈500~600억 달러·100 GW, GPU의 **대체 가능성·내구성**이 판매 논리, *"모든 지능을 아웃소싱할 수는 없다"*. 이 위키의 토큰 논의 세 층(구매자 LOC / 모델 공급자 역할 / 하드웨어 공급자 상품 단위) 표를 이 페이지와 [[trusted-throughput]] 양쪽에 두었다.
- 신규 entity 2개 — [[jensen-huang]], [[nvidia]](위키 첫 하드웨어 층 조직). Howard Lutnick은 진행자로만 기록(관례).
- 기존 페이지 보강 6건:
  - [[agent-harness-design]]: **세 번째 정의** — *"LLM에 씌운 외골격"*(while 루프·AI Layer에 이어). 그리고 **하네스가 조직의 일이 된다** — MIT 박사 온보딩 사고 실험. 이 페이지의 하네스(결함 보완, [[harness-pruning]]대로 얇아짐)와 Huang의 하네스(맥락 부여, *"AGI가 등장하더라도"* 남음)를 **두 층**으로 구분했다 — ⚠️ 위키의 정리.
  - [[brain-hands-decoupling]]: hands가 로봇 팔·자율주행차·휴머노이드로 — *"디지털 도구든 물리적 도구든"*. 컨테이너 죽음은 재시도로 풀리지만 로봇 팔의 실패는 [[agent-distributed-systems]]의 *"부작용은 되돌릴 수 없다"* 가 물리적으로 참이 된다는 점을 적었다(소스는 다루지 않음).
  - [[context-engineering]]: 세션 층의 맥락 관리는 플랫폼으로 내려가도 **조직 층의 맥락 제공**(목적·관련성)은 내려갈 곳이 없다는 단서.
  - [[regulatory-capture]]: **네 입장 표**(Ng·Gates·Altman·Huang). Huang — *"가상의 피해가 아니라 실제 피해를 규제"*, *"발전이 오히려 안전성을 높였다"*, 최악은 *"뒤쳐지는 것"*. 표의 한 축이 *판매자일수록 자율 판단을 신뢰한다* 는 것.
  - [[sutton-bitter-lesson]]: 에세이를 **안전 논증**으로 쓰는 사례 — Ghahramani(구조를 넣자)·Huang(더 발전시키자)·Altman(발전이 안전을 앞질러 늦췄다) 셋의 위치를 적고 해소하지 않았다.
  - [[trusted-throughput]]: 판매자 층의 토큰. 이 페이지의 *"단가는 잘못된 최적화 대상"* 이 하드웨어 층에서는 *"그러니 더 써라"* 로 읽힌다는 점.
- ASR·번역 보정: **"벼랑 끝에 서 있을지도" → 엣지(edge)에 있을 수도**(클라우드·온프렘·엣지 나열), "구내" → on-prem, "14세대째 건축 설계" → 아키텍처 14세대, "닛사" → NHTSA, "민주화를 해체할" → 말더듬(*de- democratize*).
- ⚠️ 확정하지 않은 것 4건: ① **"2050조 달러"** — en-orig도 *2050 trillion*, *20조·50조* 인지 미확정. ② **"거의 1조 달러"** 의 투자 주체(*"세계의, 미국의"* 로 정정하며 말함). ③ AGI *"사실상 도달"* 의 정의·근거 없음. ④ 회의 날짜·세션명.
- 페이지화하지 않음: Howard Lutnick(진행자), DRM News International(원 영상 출처 링크), FDA·NHTSA·ETH(예시 나열), GenCast류 제품 없음.

### 갱신

- raw 4건: `01.raw/articles/2026-09-05_샘 알트만 인터뷰 Part 1 ….md` · `…Part 2 ….md` · `…Part 3 ….md` · `2026-09-05_엔비디아 젠슨 황이 G20에서 우리는 이미 AGI에 도달했습니다라고 말한 이유.md`
- 신규: source 4 · concept 7 · entity 5. 기존 보강 18페이지(entity 7 · concept 11). index(실측 267→283 — ⚠️ 이전 항목의 263은 오기였다), overview(현재 상태 한 단락 + 진화 로그), [[tech-bridge]](sources 21→25, 새 주의사항 2건).

### 핵심 합성

이 위키가 지금까지 들은 목소리는 **만드는 사람과 쓰는 사람**이었다 — 엔지니어, PM, 연구자, 도입 조직. 오늘 처음으로 **파는 사람의 최상위**가 들어왔고, 넷 다 자기 회사를 말한다. 그래서 오늘의 첫 번째 교훈은 내용이 아니라 **읽는 법**이다: 모든 페이지에 당사자 진술 표시와 화자의 인센티브를 적었고, [[agi-definition]]·[[ai-jobs-impact]]·[[regulatory-capture]]의 비교표는 그 인센티브를 열로 갖는다.

내용에서 가장 값진 것은 **하네스의 두 층**이다. 이 위키는 [[harness-pruning]]에서 하네스를 *모델 결함의 보완*으로 확정했고, 그러면 모델이 좋아질수록 하네스는 얇아진다. [[jensen-huang]]의 온보딩 사고 실험은 다른 층을 가리킨다 — 아무리 똑똑한 신입에게도 **맥락·목적·접근권**을 둘러싸 줘야 하고, 그것이 *"AGI가 등장하더라도"* 남는 기업의 일이다. 결함 보완층은 얇아지고 맥락 부여층은 남는다면, [[agent-harness-design]]의 *"the space doesn't shrink, it moves"* 는 방향까지 얻는다 — **아래층에서 위층으로**. [[goal-level-delegation]]이 팀 안에서, Altman의 *"게으른 사용자"* 가 소비자 쪽에서 본 것이 같은 이동이다.

그리고 **안전에 대한 반대 처방이 같은 날 같은 채널에 실렸다.** [[sam-altman]]은 *안전이 발전을 따라잡아야* 해서 프론티어 훈련을 늦췄고([[training-time-risk]]), [[jensen-huang]]은 *발전이 안전을 만든다*며 최악은 뒤쳐지는 것이라 했다. 둘 다 [[sutton-bitter-lesson]]을 전제한다 — 컴퓨트가 이긴다 — 그리고 그 함의를 반대로 읽는다. 어제 [[zoubin-ghahramani]]가 세 번째 위치(구조를 넣자)를 잡았으니 이제 셋이다. 위키는 판정하지 않고 세 화자의 자리(연구자 / 모델 판매자 / 인프라 판매자)를 적었다. 이 세 자리가 이 위키의 안전 논의를 앞으로 읽는 좌표가 될 것이다.

마지막으로 작은 것 하나. Altman이 *"지능이 아니라 의도 이해가 병목"* 이라 한 것은, 이 위키가 어제까지 [[fuzzy-intent-discovery]](사용자가 의도를 말하지 못한다)와 [[verifiable-goals]](의도를 검증 가능하게 써라)로 **양쪽 끝에서** 다루던 문제의 이름을 **가운데**에서 붙인 것이다 — [[intent-alignment]]. 하네스가 의도를 끌어내는 절차라면, 그 절차가 얇아지는 조건이 바로 모델이 의도를 읽는 능력이다. 오늘의 두 이야기는 여기서 만난다.

## [2026-09-07] ingest | Tech Bridge — 2편 (일론 머스크 G20 · 샘 올트먼 G20)

TechBridge-KR 일일 ingest. `--playlist-end 15` 가 **13편** 반환(어제와 같음), 그중 **신규 2편**(둘 다 2026-09-06 업로드)이고 나머지 11편은 이미 ingest돼 있었다. Shorts 없음 — 최단 797초. ko·en-orig 자막 **전부 확보, 429 없음**.

**두 편 모두 09-06에 ingest한 [[tech-bridge-jensen-huang-g20-agi|Jensen Huang 편]]과 같은 행사**(G20 혁신 장관급 회의, Chapel Hill)다. 채널이 한 행사를 여러 편으로 나눠 올린 두 번째 사례(첫 번째는 Altman 3부작).

### 1. [[tech-bridge-elon-musk-g20-ai-future]] — Elon Musk, 13:17 (화상, 회의 첫 연사)

- https://www.youtube.com/watch?v=I57mRWlOV_w
- 신규 concept 3개:
  - [[default-legal-regulation]]: *"새로운 것들은 **기본적으로 합법**이어야 하며 기본적으로 불법이어서는 안 된다."* EU를 반례로. 규제의 비용을 금지가 아니라 **지연**으로 든다(*"막지는 못하지만 상당히 늦춘다"*). **[[regulatory-capture]]의 앞선 네 입장과 층이 다르다** — 넷은 규제 *대상*을 다퉜고 이것은 **입증 책임의 기본값**을 묻는다. 그 층에서 보면 Huang·Ng의 *"실제 피해만"* 은 default legal을 전제하고도 명시하지 않은 것이고, Gates의 *"라이선스"* 는 default illegal의 한 형태다.
  - [[humanoid-robot-scaling]]: 범용 로봇 유용성 = **AI 소프트웨어 × AI 칩 × 손의 전기기계적 정밀도**, 세 항 모두 기하급수 개선 중. 이후 *"로봇들이 스스로 로봇을 생산"* 하는 재귀 효과 → 10년 안 10억 대, 대당 인간의 5배, *"모든 인류를 합친 것보다 더 생산적"* (본인 평가 *"보수적"*).
  - [[power-shortfall]]: AI 칩 생산 연 **40~50%** vs 중국 외 가용 전력 연 **10~20%** → *"2027년 최소 **15 GW** 부족."* GPU 수출 통제가 **전력과 칩을 서로 다른 지리에 가둔다**는 관찰이 이 위키에 처음 들어왔다.
- 신규 entity 3개 — [[elon-musk]], [[tesla]]([[nvidia]] 이후 조직 축의 **첫 물리 제조업**), [[spacex]](⚠️ 페이지 전체가 자기 진술 한 문단에서 파생).
- 기존 페이지 보강: [[regulatory-capture]](다섯 번째 입장 + **포획의 경로** — *"대기업은 지도부에 접근할 수 있고 스타트업은 못 한다"*; [[andrew-ng]]가 포획의 *결과*를 지목했다면 이쪽은 *경로*다), [[ai-jobs-impact]](다섯 입장 표 — Musk만 분석 단위가 task도 job도 아닌 **분야 전체**), [[brain-hands-decoupling]](*분리되지만 곱해진다* — 인터페이스는 분리돼도 성능은 곱), [[intelligence-as-infrastructure]](층 1의 결손), [[compute-constrained-growth]](물리적 상한), [[tech-bridge]].
- **ASR·번역 보정**: ⚠️ **ko 자막이 핵심 문장의 뜻을 뒤집었다** — en-orig *"But like AI will just crush all humans at software"* 를 ko가 *"…라고 생각하는 건 **착각**이죠"* 로 옮겨 **결론을 반대로** 만들었다. en-orig를 채택했다. 그 외 **"입양" → 도입/채택(adoption)**(ko가 기술 도입을 *아이 입양*으로 직역, 2회), **"심각한 권력 위기" → 전력 위기**(*crisis of power* = 전기).
- ⚠️ 확정하지 않은 것: **모든 수치의 출처**(20~30% · 10배 · 10억 대 · 5배 · 15 GW — 전력만 *"분석가들의 공통 추정"* 이라 하되 이름 없음), 진행자 이름(자막·설명란 둘 다 없음 — 같은 행사라는 이유로 Huang·Altman 편의 Lutnick과 동일인이라 쓰지 않았다), *"Google·Anthropic이 SpaceX로부터 컴퓨팅 임대"* 의 진위(자기 진술).

### 2. [[tech-bridge-altman-g20-economic-boom]] — Sam Altman, 31:32

- https://www.youtube.com/watch?v=fN_D7PgtUik
- 신규 concept 2개:
  - [[one-continuous-exponential]]: 농업·산업·컴퓨터 혁명은 *"하나의 혁명, 하나의 기하급수적인 기술 발전"* 이고 각 세대는 앞 세대의 **비계 위에 벽돌을 얹는다.** 용도는 예측이 아니라 **자기 절제** — *"'이것이 마지막 혁명이다'라고 말하고 싶은 유혹"* 을 명시적으로 거부한다. **모델 판매자가 자기 제품의 역사적 지위를 낮추는 진술**이라는 점이 드물다. [[agi-definition]]에 **도착점 없는 곡선**이라는 네 번째 형식을 준다(⚠️ 단 이 소스에서 AGI라는 단어를 쓰지 않으므로 3부작의 정의와 합치지 않았다).
  - [[intelligence-abundance]]: *"밤에 한 시간 불을 켜는 데 **임금 5시간**"* 이던 전기가 지금은 비용을 생각조차 않게 된 역사. 논증의 무게는 **반사실**에 있다 — 그러지 않았다면 *"부유한 사람들은 밤에도 공부할 수 있고 **복리 효과**를 누리고, 가난한 사람들은 그렇지 못했을 것."* 그래서 풍요의 실패 = **권력 집중**이고, [[regulatory-capture]]에 **가격이 포획의 경로가 되는 길**이 추가된다.
- 신규 entity 0개 ([[sam-altman]]·[[openai]]·[[codex]] 모두 기존).
- 기존 페이지 보강: [[intelligence-as-infrastructure]](*"도입은 **협상 불가능**"*·100년 전 전기 거부 비유 — Huang과 **같은 결론에 다른 경로**로 도착하고, 소유 형태는 무관하다고 말한다), [[compute-constrained-growth]](토큰 외삽에 숫자가 붙어 *"효율은 수요가 삼킨다"* 가 **관찰에서 계획 전제로**), [[token-roles]](*"토큰은 **어리석은 단위**"* — 같은 회의에서 Huang이 토큰을 상품 단위로 굳히는 자리에서 공급자가 그 단위를 부정하면서 쓴다), [[sutton-bitter-lesson]](**설립 결정으로서의 스케일링** — *"우리는 그 외에는 아는 게 없었어요"*, *"왜 안 되겠어?"*), [[context-engineering]](**공급 경계** — 맥락은 *"우리 쪽에서 나올 일도 아니고, 나와서도 안 된다"*; 세션·조직에 이은 세 번째 위치), [[persistent-agent-teams]](공급자가 그린 3단계 — 3단계 *"가상 협력자"* 를 아직 오지 않은 것으로 둔다), [[ai-jobs-impact]](대체가 아니라 **창업**으로 답한다), [[agi-definition]], [[regulatory-capture]](**걱정이 곧 안전의 생산 기제** — 불→도시 화재→화재 안전 수칙; Huang의 *"걱정은 지연 비용"* 과 정면으로 갈린다), [[sam-altman]], [[openai]], [[tech-bridge]].
- 연표에서 새로 얻은 사실: OpenAI 발표 2015년 말·**첫 업무일 2016년 1월**, 2018 GPT-1, 2020 GPT-3(*"활용성 기준치를 넘어선 최초"*), **GPT-4를 출시 전 약 8개월 보유**(위키에 처음 나오는 수치), 2012년을 분수령으로 지목.
- ⚠️ 확정하지 않은 것: **진행자 이름이 소스 안에서 어긋난다** — 설명란은 Howard Lutnick, 자막 말미는 *"Thanks, **Arthur**"*. 해소하지 않고 양쪽을 남겼다. **최다 사용자 토큰 외삽**은 Altman 본인이 *100 quadrillion → 1 quadrillion 100 trillion → 100 trillion → 100 quadrillion* 으로 **세 번 바꾸고 정리하지 않아** 어느 값도 채택하지 않았다. *"곧 출시할 새 모델"* 의 이름 없음(3부작의 [[openai-astra|아스트라]]와 **연결하지 않았다**). *"3개월 → 17분"* 의 비교 기준 없음. *"Alice Carper"* ASR 신뢰도 낮음.
- ASR·번역 보정: *"talk my book"* → **"제 이해관계에 유리한 말"**(ko는 *"제 책 이야기"* 로 직역), *"Right?"* → *"오른쪽?"*, *"오픈아이얼"* → OpenAI.

### 이번 ingest의 합성

- **같은 자리에서 세 판매자가 각국에 서로 다른 층을 권한다** — 칩·확산(Huang) / 모델 사용(Altman) / **발전소**(Musk). [[intelligence-as-infrastructure]]의 5단 케이크가 세 화자로 채워졌고, 세 처방이 각자의 상품과 정렬돼 있다는 사실 자체를 표로 남겼다. 셋의 **공통 결론은 "도입을 늘려라"** 이고, 셋 다 도입이 늘면 이익을 얻는 위치다.
- **컴퓨팅 논의가 전력 단위로 닫혔다** — 수요는 효율로 줄지 않고(Altman) · 공급은 GW당 수백억 달러(Huang) · 그래서 결손이 남는다(Musk).
- **안전관이 세 갈래가 됐다** — 걱정은 지연 비용(Huang) vs 안전의 생산 기제(Altman) vs 논의하지 않음(Musk, 대신 default legal). 판정하지 않고 위치만 적었다.
- 통계: index 실측 **283 → 293** (source 2 · concept 5 · entity 3).

### 운영 메모

- 이 실행은 launchd 정시 발화분(09:10 KST)이며 부모 체인 `launchd → run-ingest.sh(pid 16927) → claude --print` 로 자기 확인했다. **게이트 D(OAuth)·E(모델 쿼터) 모두 통과 — 나흘 연속.**
- **`launchctl print` 의 `runs` 는 2였다.** 09-06에 관찰된 카운터 리셋 이후 값이며, 누적 지표로 쓰지 않는다.
- **새 주의사항 — ko 자막이 결론을 반대로 뒤집을 수 있다.** 지금까지 기록한 ko 오류는 고유명사 직역·약어 창작·오인식 직역이었는데, 이번엔 **긍정문이 부정문이 됐다.** 핵심 주장 문장은 반드시 en-orig와 대조한다.
- **새 주의사항 — 시리즈가 날짜를 넘어 이어질 수 있다.** 09-05 ingest한 Huang 편과 이번 두 편이 같은 행사인데 업로드가 하루 갈렸다. **행사 단위로 묶어 읽어야** 세 판매자 구도 같은 것이 보인다. 앞으로 신규 영상의 설명란에서 *행사명·장소*를 먼저 확인하고 기존 소스와 대조한다.

## [2026-09-08] ingest | Tech Bridge — 2편 (IBM 지식 조달 4갈래 · MiniMax M3 100만 토큰)

2026-09-07 업로드분 **2편**. `--playlist-end 15` 가 이번엔 **15편을 전부 반환**했고(09-04~09-07 나흘 동안은 13편이었다 — **반환 개수는 고정이 아니다**), 나머지 13편은 이미 ingest돼 있었다. 둘 다 롱폼(538초·1192초), Shorts 없음. **ko·en-orig 전부 확보, 429 없음.**

### 대상

| video id | 길이 | 소스 |
|---|---|---|
| `9GQE_jb_Iq8` | 8:58 | [[tech-bridge-agent-knowledge-four-ways]] — [[ibm|IBM Technology]], 발표자 무명 |
| `TdudKNElsA8` | 19:52 | [[tech-bridge-minimax-m3-long-context]] — [[thomas-wolf]] × [[olive-song]] / [[minimax]] |

**같은 날 올라온 두 편의 성격이 정반대다.** 하나는 자기 제품이 하나도 안 나오는 개념 해설(채널 최단편)이고, 다른 하나는 자기 회사 모델을 말하는 당사자 인터뷰다.

### 신규

- **source 2** — 위 표.
- **concept 6** — [[retrieval-augmented-generation]] · [[agent-memory]] · [[agent-knowledge-sourcing]] (IBM 편) / [[long-context-agents]] · [[sparse-attention]] · [[native-multimodal-pretraining]] (MiniMax 편).
- **entity 5** — [[ibm]] · [[minimax]] · [[minimax-m3]] · [[thomas-wolf]] · [[olive-song]].

**[[retrieval-augmented-generation|RAG]]는 늦게 생긴 페이지다.** 이 위키는 [[agentic-sites]]·[[llm-wiki-pattern]]·[[code-knowledge-graph]]·[[karpathy-llm-wiki-gist]]에서 RAG를 **대비항으로만 계속 언급**해 왔고 정작 페이지가 없었다. 오늘 처음으로 RAG 자체를 설명하는 소스가 들어와 채워졌다.

### 기존 보강 (10페이지)

[[agent-skills]](스킬이 멈추는 자리) · [[model-context-protocol]](스킬과의 분업) · [[context-engineering]](쏟아붓기의 세 실패 + 늘리는 쪽 처방) · [[attention-mechanism]](효율화의 진자 운동) · [[transformer]](GPU 효율성 항이 커널로 풀린 뒤) · [[self-harness]](랩 층위 — M3가 M3.1을 만든다) · [[hugging-face]](사건 당사자에서 벗어난 첫 등장) · [[minimax-m2-5]](만든 회사와 다음 세대) · [[glm-5]](오픈소스 리더보드 언급) · [[tech-bridge]](sources 25→29, 새 주의사항 3건).

`index.md`(실측 **293→306**), `overview.md`(현재 상태 한 단락 + 진화 로그).

### 핵심 합성

**두 편은 우연히도 같은 문제의 양끝이다.** IBM 편은 *"컨텍스트 창에 다 쏟아붓지 말고 경로를 나눠라"* 라 하고, MiniMax 편은 *"컨텍스트를 100만 토큰으로 늘렸다"* 고 한다. 모순이 아니라 층이 다르다 — 전자는 **무엇을 넣을지 고르는 문제**(조달), 후자는 **에이전트가 스스로 만들어내는 것을 담을 그릇**(용량)이다. 길이가 늘어도 라우팅 규칙은 사라지지 않는다. ⚠️ 두 소스는 서로를 언급하지 않으며 이 대비는 위키가 놓는 것이다.

IBM 편에서 가장 이식성 높은 것은 [[retrieval-augmented-generation|RAG]]와 [[agent-memory|메모리]]를 **메커니즘이 아니라 출처로** 가른 것이다 — 저장소가 둘 다 벡터 DB이고 조회가 둘 다 의미 검색이어도, *사람이 일부러 넣었나 / 에이전트가 겪었나*가 다르면 다른 물건이고 **메모리만 쓰기 방향을 갖는다.** 그리고 이 소스는 [[agent-skills]]와 [[model-context-protocol]]의 분업을 처음으로 한 문장에 담는다 — 두 페이지는 이 위키에서 각각 조직 지식 축과 연결 표준 축으로 따로 자라 `related`로만 걸려 있었다.

MiniMax 편의 논증은 **자기 회사의 이전 모델이 반례**라는 점에서 단단하다 — M1·MiniMax-01이 이미 1천만 토큰을 처리했으나 *"그때는 에이전트 모델이 아니었죠"*. 축이 길이에서 **그 길이를 무엇이 채우나**로 옮겨간 것이다. 그리고 [[thomas-wolf]]의 **진자 운동** 서술이 [[transformer]]에 단서를 붙인다 — 트랜스포머가 오래 버틴 이유 중 일부는 **그것을 대체하려던 구조 변형들이 flash attention이라는 커널 개선에 흡수됐기 때문**이고, 그렇다면 다음 시도가 유효할 조건은 커널로 흡수되지 않는 축이다.

### 해소하지 않고 표시만 한 것

- **IBM 편**: 발표자 무명(설명란·자막 어디에도 없음), **촬영 시점 미확정**(연도·제품·행사 언급이 하나도 없다 — 09-03 절차를 적용한 결과 *양쪽 다 주장하지 않음*), 비용·지연 수치 전무, 네 방법의 **조합·충돌 미논의**(예제 자체가 *문서가 틀리고 경험이 맞았던* 사례인데 판정 규칙이 없다), 메모리의 무효화·틀린 기억 처리 없음, *"without using proprietary code"* 미정의.
- **MiniMax 편**: **파라미터 3중 불일치**(게스트 4천억/200억 · 진행자 4,280억/230억 · 설명란 4,000억/230억 — 게스트가 정정하지 않아 **어느 값도 채택하지 않았다**), **벤치마크·논문 링크 전무**(MSA가 *"우아하다"*·*"저렴하다"* 뿐이고 진행자 본인이 저렴함의 원인을 확정하지 못한다), **게스트 이름 불일치**(설명란 *Olive Song* vs 자막 *"Olivia"*/*"Olive"*), 진행자 이름이 **설명란 단독**, 1천만→100만으로 줄어든 이유 없음, 붕괴 해결의 내용 없음, 사용자 수치가 *"~것으로 알고 있습니다"*, **오픈소스 수익 모델에 답이 없음**(진행자가 두 번 물었다), research harness의 실체 없음, 행사명·회차 없음.
- **미상 단어 하나**: en-orig가 두 자리에서 ***"Asia"*** 로 듣는데(*"the dream of Asia"* — MiniMax CEO를 가리키는 자리, *"It can be Asia in terms of feature"*) 문맥이 지명과 맞지 않는다. **원어를 확정할 근거가 없어 추측하지 않고 남겼다** — 그래서 [[minimax]] 페이지에 CEO 이름을 적지 않았다.

### 새 주의사항

- **ko 자막이 약어를 일반 명사로 읽어 결론을 파괴할 수 있다.** IBM 편의 라우팅 규칙 네 줄 중 하나에서 en-orig ***"that's rag"*** 가 ko에서 **"그건 쓸모없는 쓰레기지"** 가 됐다. 09-07의 *부호 뒤집기*, 09-06의 *고유명사 직역*과 구별되는 **세 번째 유형**이다. 문장이 어색해 눈에는 띄지만 그래서 오히려 *"자막이 이상하네"* 로 넘기기 쉽다.
- **ko 자막이 없던 단위를 붙일 수 있다.** *"go past the **trillion**"*(1조 **파라미터**)이 **"1조 달러"** 가 됐다. 09-04의 *약어 창작*의 사촌이다 → **숫자 뒤의 단위는 예외 없이 en-orig 대조 대상.**
- **`--playlist-end 15` 의 반환 개수는 고정이 아니다.** 09-04~09-07 나흘 동안 13편이었고 오늘은 15편이었다. **"13편"을 채널 상태의 지표로 쓰지 말 것** — 매번 실제 반환분을 세고 dedup한다.
- **한 영상 안에서 같은 단어가 여러 번역으로 갈릴 수 있다.** IBM 편에서 **agent**가 *요원*(첩보원)·*상담원*(콜센터)·*에이전트* 셋으로 옮겨졌다. 용어를 grep으로 찾을 때 한 표기만 믿으면 놓친다.
- **en-orig 오인식의 연쇄 직역이 한 편에 몰릴 수 있다.** MiniMax 편에서 *AI labs*→*"nail labs"*→**"네일 랩"**, *OpenAI*→*"open air"*→**"야외에서 통화량"**, *JEPA*→*"Japa"*→**"일본"**, *attention*→*"tensions"*→**"긴장감"**. 09-04에 기록한 유형이지만 밀도가 이례적이었다.

### 실행 환경

- launchd 정시 발화분(09:10 KST)이며 부모 체인 `launchd → run-ingest.sh(pid 87948) → claude --print` 로 자기 확인했다. **게이트 D(OAuth)·E(모델 쿼터) 모두 통과 — 닷새 연속.**
- `launchctl print` 의 `runs` 는 3이었다(09-06 리셋 이후 값). 누적 지표로 쓰지 않는다.
- **게이트 B(릴레이 스케줄 자동 발화)는 이번에도 확인하지 않았다.** launchd가 우회하고 있으므로 일일 잡 자체는 성립한다.

## [2026-09-09] ingest | Tech Bridge 3편 — 지식 노동 인프라(Composio) · AI 시대 코드 품질(IBM) · Cursor 레거시 리팩터링

2026-09-08 업로드분. `--playlist-end 15`가 **15편 반환**, 신규 3편, 나머지 12편은 기존. 롱폼만(최단 538초), Shorts 없음. ko·en-orig 전부 확보, **429 없음.**

| 소스 | 길이 | 화자 | 성격 |
|---|---|---|---|
| [[tech-bridge-knowledge-work-agent-infrastructure]] | 20:12 | [[karan-vaidya]] ([[composio]]) | 컨퍼런스 단독 발표 ⚠️ 인프라 판매자 |
| [[tech-bridge-ai-era-code-quality]] | 13:42 | 무명 ([[ibm]]) | 1인 슬라이드 해설 · 자사 제품 없음 |
| [[tech-bridge-cursor-legacy-refactoring]] | **55:17** | Cursor 필드 엔지니어 ⚠️ 이름 불일치 | **실시간 워크샵 — 채널 최장편** |

### 신규 (18페이지)

- **source 3** — 위 표.
- **concept 12** — [[knowledge-work-agent-gap]] · [[agent-action-record]] · [[agent-governance-layers]] · [[action-reversibility]] (Composio) / [[decision-quality]] · [[system-level-quality]] · [[behavior-validated-trust]] · [[executable-standards]] (IBM) / [[cloud-agent-delegation]] · [[plan-to-ticket-pipeline]] · [[scheduled-agent-automations]] · [[model-mixing-economics]] (Cursor).
- **entity 3** — [[composio]] · [[karan-vaidya]] · [[cursor-cloud]].

### 기존 보강 (15페이지)

[[cursor]](네 표면·harness·플러그인·모델 라인업 — 이 위키 최대 보강) · [[grok-4-6]](촬영 시점 앵커) · [[grokbot]](로컬 접근 한계를 메우는 자리) · [[ibm]](두 번째 소스, 두 편의 공통 패턴 표) · [[anthropic]](경쟁사가 가격으로 회피한다는 진술) · [[tech-bridge]](sources 29→32, 새 주의사항 6건) · [[agentic-misbehavior]](메일 200통) · [[context-resets-and-compaction]](compaction이 안전 장치를 지운다) · [[agent-memory]](조직 규모·잡 규모) · [[agent-knowledge-sourcing]](직교하는 축) · [[agent-skills]](플러그인이 유통 경로) · [[model-context-protocol]](MCP+스킬 한 패키지) · [[continual-learning]](동명 제품 주의) · [[harness-engineering]](cursor harness 4요소) · [[llm-coding-guidelines]](문서 표준 반론) · [[generator-evaluator-pattern]](검증자=작성자) · [[trusted-throughput]](세 층위 반복) · [[persistent-agent-teams]](세 번째 형태) · [[ai-native-sdlc]](품질 판정 + 워크플로).

`index.md`(실측 **306→324**), `overview.md`, `log.md`.

### 핵심 합성

**세 편이 우연히 한 축을 이룬다.** 셋 다 *에이전트가 코딩에서만 잘 되는 이유와 그 조건*을 다루되 서 있는 자리가 다르다 — Composio는 **코딩 밖에는 딛을 바닥이 없다**고 하고, IBM은 **코딩 안에서도 판정은 사람 몫**이라 하며, Cursor는 **그 조건을 갖춘 코딩에서 실제로 어디까지 되는지** 보여준다(그리고 라이브 시연은 끝나지 않았다).

**가장 이식성 높은 것은 [[agent-governance-layers|"프롬프트는 거버넌스가 될 수 없다"]]는 논증이다.** Meta 정렬 디렉터는 *미리 프롬프트에 확인 절차를 넣어두었는데도* 메일 200통을 잃었고, 이유는 그 지시가 **compaction으로 날아갔기** 때문이다. 이로써 [[context-resets-and-compaction]]이 이 위키에서 처음으로 **컨텍스트 관리 문제가 아니라 안전 문제**가 됐다 — 작업 맥락과 안전 제약이 같은 예산을 두고 경쟁하는데 **압축은 둘을 구별하지 않는다.**

**세 소스가 [[behavior-validated-trust]]에서 만난다** — IBM은 *작성자가 아니라 검증된 행동을 신뢰하라*, Composio는 *에이전트 말 대신 앱에 가서 확인하라*([[agent-action-record]]), Cursor는 **그 검증을 작성자인 에이전트가 직접 수행해 비디오로 제출한다.** ⚠️ 그리고 세 번째가 첫 번째의 전제를 깬다 — **작성자와 검증자가 같다.** 어느 소스도 묻지 않아 [[generator-evaluator-pattern]]에 빈자리로 기록했다.

**같은 형태의 논증이 세 층위에서 따로 나왔다** — *규칙은 사람이 기억할 곳이 아니라 시스템에 두어야 한다*: 개발 프로세스([[executable-standards]]) · 에이전트 런타임([[agent-governance-layers]]) · 도구 설정(Confluence 템플릿·플러그인·automation).

### 촬영 시점 — 위키 교차 참조로 좁힌 첫 사례

Cursor 편이 [[grok-4-6|Grok 4.6]]을 *"어제 출시됐다고 말하고 싶네요"*라 하고, 이 위키의 [[tech-bridge-grokbot-agent-teams]](2026-08-31)가 그것을 **당일 발표**로 기록하고 있었다. → 촬영 **2026-09-01 무렵**, 업로드 09-08. **업로드 ≠ 촬영의 네 번째 사례이자, 내부 증거가 아니라 다른 위키 소스와의 대조로 좁힌 첫 사례다.** ⚠️ 화자 자신의 유보(*"I want to say"*)가 붙어 있어 확정하지 않았다.

### 새 주의사항

- **ko가 서술문을 청유문으로 바꿀 수 있다.** IBM 편 en-orig *"Maybe leave some comments"*(PR 리뷰 절차 **서술**)가 ko에서 **"댓글을 남겨주시면 감사하겠습니다"**(시청자 **요청**)가 됐다. 지금까지의 유형(고유명사 직역·약어 창작·부호 뒤집기·단위 창작)과 다른 **화행(speech act) 변형**이고, **문장이 자연스러워 자막만 보면 오류로 보이지 않는다** — 지금까지 기록한 ko 오류 중 **탐지가 가장 어려운 유형**이다.
- **en-orig가 `.md`를 `.mmd`로 적는 표기 습관이 있다.** Composio 편 `bugbot.mmd`, Cursor 편 `agents.mmd`·`memories.mmd` — **하루에 두 소스에서 세 번.** 개별 오인식이 아니라 생성기의 습관이다.
- **발표자 이름을 확정할 근거가 아예 없는 경우가 있다.** Cursor 편은 진행자가 **Amita / Amriita**로 두 번 다르게 부르고 **설명란에 이름이 없다.** 09-02·09-08의 불일치는 설명란이라는 판정 근거가 있었으나 이번엔 없다 → **어느 표기도 채택하지 않고 인물 페이지를 만들지 않았다.**
- **자막이 끝에서 잘릴 수 있다.** IBM 편 en-orig 마지막 줄이 13:18에 문장 중간에서 끝난다(영상 13:42). 09-06 Jensen Huang 편이 **시작**의 결손이었다면 이번은 **끝**의 결손이다. **보충하지 않았다.**
- **위키에 이미 있는 개체명이 ASR 해독의 근거가 된다.** *"Grock 46"*·*"Grockbot"*·*"Fable"*을 [[grok-4-6]]·[[grokbot]] 페이지가 이미 있어 확정할 수 있었다. **ingest 전에 기존 엔티티 목록을 훑는 것이 자막 보정에 직접 쓸모가 있다.**
- **동명이인/동명제품 주의.** Cursor의 `continual learning` 플러그인은 이 위키 [[continual-learning]] 페이지의 학문적 의미와 **이름만 같고 메커니즘이 다르다**(가중치 갱신이 아니라 `AGENTS.md` 축적). 해당 페이지에 경고를 달았다.

### 해소하지 않고 표시만 한 것

- **Composio 편**: *"open claw"*의 정체 미확정, Meta 정렬 디렉터 **이름·날짜·출처 링크 없음**, 자사 규모 수치(10억+/월 3억 도구 호출) 출처 없음, 여섯 primitive의 **우선순위·상호작용 미논의**, 샌드박스 충실도 문제 미논의, 그리고 **자연어 정책을 무엇이 해석·강제하는가에 답이 없다**(논증 구조상 가장 큰 빈자리).
- **IBM 편**: 발표자 무명·촬영 시점 미확정(두 번 연속), 자막 말미 결손, **근거 연구의 출처 전무**, 수치 전무, **결정 품질의 측정 방법 없음**, AI가 아키텍처 평가를 못 한다는 주장의 근거 없음.
- **Cursor 편**: 발표자 이름 불일치, 행사명·주최 없음, **라이브 마이그레이션 미완**, **자기 검증의 독립성 미제기**, SQLite 케이스 스터디 **수치 없음**, *"마이그레이션 전체에 3~4달러"*의 조건 없음, 모델 표기 불확정(*"GPT56 Soul"*·*"DeepSeek V4 Flasher Pro"*), **`/vtw` 해독 불가**(양쪽 트랙 동일 표기), 쿡북 문서 부재, **cloud agent 크래시 시 컨텍스트 복구 여부에 답 없음**, WordPress 예제가 공개 레포라 사내 레거시의 전형적 어려움 미포함.
- **위키 차원의 모순 하나** — Composio 편은 *"소프트웨어 엔지니어링은 100% 자율적"*을 전제하고, IBM 편은 *결정은 사람 몫*이라 하며, Cursor 편의 라이브 시연은 끝나지 않았다. **어느 쪽도 채택하지 않고 셋을 나란히 두었다.**

### 실행 환경

- launchd 정시 발화분(09:10 KST, 실제 시작 09:18 KST)이며 부모 체인 `launchd → run-ingest.sh(pid 9836) → claude --print`로 자기 확인했다. **게이트 D(OAuth)·E(모델 쿼터) 모두 통과 — 엿새 연속.**
- `launchctl print`의 `runs`는 4였다(09-06 리셋 이후 값). 누적 지표로 쓰지 않는다.
- **게이트 B(릴레이 스케줄 자동 발화)는 이번에도 확인하지 않았다.** launchd가 우회하고 있으므로 일일 잡 자체는 성립한다.
- yt-dlp 목록 조회와 자막 다운로드가 각각 300s·480s를 넘겨 백그라운드로 넘어갔다 — **쿠키 추출 경합으로 보이며 실패는 아니다.** 재시도 없이 완료됐다.

## [2026-09-10] ingest | Tech Bridge 2편 — 회사 두뇌는 기밀을 유출한다(PromptQL) · 에이전트 간 협업은 검색 문제다(Town)

2026-09-09 업로드분. `--playlist-end 15`가 **15편 반환**, 신규 2편, 나머지 13편은 기존. 롱폼만(최단 538초), Shorts 없음. ko·en-orig 전부 확보, **429 없음.** 이번엔 yt-dlp 목록·자막이 각각 1분 안에 끝났다(어제의 300s·480s 지연 없음).

| 소스 | 길이 | 화자 | 성격 |
|---|---|---|---|
| [[tech-bridge-company-brain-security]] | 25:56 | [[tanmai-gopal]] ([[promptql]] · Hasura 제작팀) | 컨퍼런스 발표 ⚠️ company brain 플랫폼 판매자 · 자사 데이터 |
| [[tech-bridge-agent-to-agent-as-search]] | 20:48 | [[jean-denis-greze]] ([[town]] CTO · 전 Plaid CTO) | 컨퍼런스 소규모 세션 ⚠️ 당사자이되 판매 대상 약함 · 수치 없음 |

### 신규 (16페이지)

- **source 2** — 위 표.
- **concept 9** — [[company-brain]] · [[no-silent-write]] · [[named-human-accountability]] · [[credential-injection-outside-sandbox]] · [[multiplayer-agent-context]] (PromptQL) / [[agent-collaboration-as-search]] · [[sweeper-agent]] · [[black-box-agent-approach]] · [[privacy-auto-mode]] (Greze).
- **entity 5** — [[tanmai-gopal]] · [[promptql]] · [[jean-denis-greze]] · [[town]] · **[[openclaw]]**(다섯 소스의 지나가는 언급을 모은 페이지 — CLAUDE.md §3.3 *누락 개체* 를 ingest 중에 적용한 첫 사례. 정체는 위키의 추정으로 표시).

### 기존 보강 (25페이지)

[[llm-wiki-pattern]](**조직 규모 인스턴스·자동 파이프라인·실패 형태** — sources 3→5) · [[agent-memory]](자동 저장의 조직적 실패, **틀린 기억의 첫 실사례** Apex/Ivy) · [[agent-knowledge-sourcing]](셋째 축: 누가 남을 위해 쓸 동기가 있는가) · [[agent-skills]](**공유 스킬에 대한 두 소스의 충돌** ⚠️) · [[agent-governance-layers]](벽의 세 위치 표) · [[action-reversibility]](정보 공개의 비가역성) · [[agent-action-record]](사람 이름 열 · 블랙박스와의 충돌) · [[behavior-validated-trust]](위키에는 테스트가 없다) · [[prompt-injection]](**네 번째 벡터: 공유 사일로/위키**) · [[retrieval-augmented-generation]](수동→RAG→에이전틱 검색) · [[context-engineering]](프라이버시 상한 · 스코프 있는 조직 컨텍스트) · [[claude-tag]](제3자 진술: **공개 출시 확인**·채널당 메모리 — 미해결 항목 하나 닫힘) · [[claude-opus-4-5]](제3자 사용 언급) · [[scheduled-agent-automations]](지식 흐름의 예약 잡) · [[sutton-bitter-lesson]](**아키텍처 판정 버전 — 두 질문**) · [[knowledge-work-agent-gap]](같은 진단, 다른 처방) · [[agent-org-adoption]](키우는 것이지 만드는 것이 아니다) · [[transcript-classifier]](프라이버시 유비의 한계: reasoning-blind를 옮길 수 없다) · [[persistent-agent-teams]](거울상: 사람이 여럿, 에이전트는 하나) · [[anthropic]](제3자 언급: Claude Tag 공개 출시·Claude Cowork 첫 등장·"auto mode를 내려주신 신들") · [[openai-astra]](Soul 미출시 등급 언급) · [[agentic-misbehavior]]·[[karan-vaidya]]·[[tech-bridge-knowledge-work-agent-infrastructure]]·[[understand-anything]](open claw → [[openclaw]] 링크) · [[tech-bridge]](sources 32→34, 새 주의사항 7건).

`index.md`(실측 **324→340**), `overview.md`, `log.md`.

### 핵심 합성

**두 편이 서로 모른 채 같은 패턴에서 만나고 다음 단계에서 갈린다.** 둘 다 *조직의 비공개 지식을 에이전트가 읽는 공유 공간으로 옮기되 에이전트는 제안만 하고 사람이 승인한다* 고 말한다([[no-silent-write]]). PromptQL은 그것을 *"물러서지 말 규칙"* 으로 놓고 **모든 변경에 사람 이름**을 요구하며, Greze는 그것을 *"지금 단계"* 로 놓고 **LLM이 정책을 집행하는 다음 단계**([[privacy-auto-mode]])가 6개월 안에 온다고 본다. 접근 제어의 벽도 반대다 — PromptQL은 **입구**(사용자 클레임으로 읽기, 샌드박스 밖 프록시 주입), Greze의 블랙박스는 **출구**(읽기 전부 개방, 쓰기 직전 정보 소유자 승인). 고객이 다르다는 것(포춘 은행 / 10~50명 고신뢰 회사)이 차이의 상당 부분을 설명한다 — 위키는 어느 쪽도 채택하지 않는다.

**이 vault의 헌장이 조직 규모를 얻었다.** [[llm-wiki-pattern]]은 지금까지 개인 위키였다. PromptQL의 [[company-brain]]은 5,000페이지 마크다운에 **파일별 스코프**와 **누가 썼는가**를 더하고, 이 vault의 규칙(*LLM이 전담, 사람은 읽기만*)을 **뒤집는다**(에이전트는 제안, 사람이 승인). 개인에서 조직으로 갈 때 더해지는 것은 *누가 볼 수 있는가* 와 *누가 책임지는가* 다. 그리고 건강 지표 하나 — **일일 업데이트 수의 추세**(⚠️ 자사 2개월, 수치 없음).

**[[agent-governance-layers]]의 벽이 세 위치를 갖게 됐다.** Composio(접근 제어 + 자연어 정책) / PromptQL(입구, 결정론적 클레임, **자연어 정책 층 없음** — 그래서 Composio 편의 가장 큰 빈자리가 생기지 않는다, 대신 표현력을 포기한다) / Greze(출구, 승인 → LLM 판단, **자연어 정책 층이 커진다**). *정책을 해석하는 LLM은 취약하지 않은가* 라는 질문은 **셋 다 답하지 않는다.**

**[[sutton-bitter-lesson]]의 아키텍처 판정판.** Greze의 두 질문 — *시간이 지나며 사람이 줄어드는가? 모델이 좋아지면 이 접근도 좋아지는가?* — 은 이 위키가 하니스 컴포넌트에 적용해 온 레슨을 **조직의 정보 접근 구조**에 적용한 첫 사례다. ⚠️ 프라이버시 판단에는 채점기가 없다 — 위키의 *범위 한정* 이 그대로 걸린다.

**공유 스킬에 대해 두 소스가 반대로 말한다.** PromptQL: *"아무도 GitHub에 남을 위한 스킬을 쓰지 않는다"* / Greze: *"누구나 더 좋게 만든다"*. 차이는 **누가 쓰는가**(사람 / 인센티브를 가진 에이전트)로 좁혀지고, 둘을 합치면 PromptQL의 처방이 된다 — 이 합성은 위키의 것이다. → [[agent-skills]] ⚠️ Contradiction.

**교차 참조로 닫힌 것 둘, 생긴 것 하나.** ① [[claude-tag]]의 미해결 항목 *공개 제품인지* 가 PromptQL의 *"며칠 전 출시"* 로 닫혔다(출시일은 여전히 미상). ② *Soul* 이 두 소스(09-09 Cursor 편·오늘 PromptQL 편)에서 **미출시 OpenAI 등급**으로 일관되게 언급된다 → [[openai-astra]]. ③ *"open claw / OpenClaw / claw land"* — 09-09에 미확정으로 둔 것이 오늘 두 소스에서 더 나오고, 기존 [[understand-anything]] 페이지가 이미 그 이름을 갖고 있었다 → [[openclaw]] 생성. **이 위키가 이미 가진 페이지가 오늘 자막을 읽는 근거가 된 두 번째 날**(09-09 Grok 4.6에 이어)이고, 이번엔 반대로 **새 소스가 기존 미해결을 닫았다.**

### 촬영 시점 — 둘 다 미확정

PromptQL 편 앵커 셋(Claude Tag *"며칠 전 출시"* · 현재 모델 *Opus 4.5* · *"Soul이 나오면"*), Greze 편 앵커 하나(*"Anthropic이 auto mode를 내려줬다"*). 위키에 Claude Tag 출시일·Soul 출시일이 없어 날짜로 좁히지 못했다. 두 편이 **같은 행사인지** 09-07 절차대로 대조했으나 설명란에 행사명이 없고 내부 단서(부스·제품 출시 / 소규모 방·박수)도 겹치지 않아 **별개 소스로 취급**했다.

### 새 주의사항

- **ko가 핵심 조어를 전편에 걸쳐 관용구로 오역할 수 있다.** *company brain* → **"기업가적 사고방식"·"비즈니스 마인드"·"사업가적 사고방식"** (10곳 이상), 몇 곳만 "회사의 두뇌". 지금까지의 유형과 달리 **발표 주제어 자체**가 바뀐다 — 자막만 보면 다른 발표다.
- **ko가 약어 확장을 한 편에서 여러 개 지어낼 수 있다.** *LLM* → 법률 문서 관리자·법학 석사·학습 리더·법률팀 관리자. 09-04 유형의 재발, **빈도 급증**.
- **ko가 원문 트랙의 결손을 채워 넣을 수 있다.** en-orig에서 묵음 처리된 비속어 세 곳을 ko가 "큰 낭패"·"네가 망한 건"·"싸가지 없는"으로 **생성**했다. **ko에만 있는 말은 원문에 없을 수 있다** — 위키는 그 표현을 인용하지 않았다.
- **회사명·모델명이 보통명사로 번역될 수 있다.** *Town*→"시내", *Opus 4.5*→"작품번호 4.5", *auto*→"자동차 산업"(결론 문장의 주어가 바뀐다). 09-08 *agent→요원* 의 고유명사 버전.
- **제목·설명란이 본문보다 강하게 주장할 수 있다.** 제목의 *"대형 은행에서 막아낸 방법"* 은 본문에 은행 사례가 없고, 설명란 *"15~20개 기업과 5,000페이지"* 는 두 사실을 합친 것, 은행 등급은 세 곳이 다르다(en-orig *fortune* / ko *500* / 설명란 *100*). 지금까지 설명란은 이름·행사의 판정 근거였는데 **설명란이 틀릴 수 있는 첫 사례** → 설명란 수치는 본문 발화로 재확인.
- **지나가는 언급이 누적되면 페이지가 된다.** [[openclaw]] — 다섯 소스. 정체는 추정으로 표시.
- **ASR 오인식을 ko가 고쳐 놓는 반대 방향도 있다.** *Hasura* 를 en-orig는 *Hustura* 로 틀렸는데 ko가 맞게 적었다. 두 트랙을 **양방향으로** 대조한다.

### 해소하지 않고 표시만 한 것

- **PromptQL 편**: 은행 사례 부재 · 일일 업데이트 곡선의 수치·조건 · 스코프 운영(정의·충돌·퇴사) · **자연어 정책 층 없음** · 프록시 구현(*"흥미로운 세부가 있지만"*) · 행사명·촬영 시점 · 트위터 핸들 자막 표기뿐 · *Hermes* 의 정체(내부 배포 에이전트로 세 번, [[understand-anything]] 목록에 있는 이름이지만 확정 안 함) · *Claude Cowork* 제품명 첫 등장(ASR *cloud co-work*, 정체 미확인) · 논쟁으로 만든 지식에 누구의 이름이 붙는가.
- **Greze 편**: Town 규모·결과 · **정책 집행 LLM의 취약성** · 블랙박스의 트레이스 비접근과 감사 요구의 모순(화자 인지) · *"6개월 안에"* 근거 없음 · 투자은행 사례 익명 · 행사명·촬영 시점 · 성(Greze)은 설명란 단독 · *"검색 문제"* 정의의 과대 확장 · 코즈 정리는 비유로만.
- **위키 차원**: 두 소스의 반대 방향(사람 승인=규칙 / 지금 단계)을 **어느 쪽도 채택하지 않음**. 공유 스킬 충돌도 마찬가지.

### 실행 환경

- launchd 정시 발화분(09:10 KST, 실제 시작 09:10:37 KST)이며 부모 체인 `launchd → run-ingest.sh(pid 34677) → claude --print`로 자기 확인했다. **게이트 D(OAuth)·E(모델 쿼터) 모두 통과 — 이레 연속.**
- `launchctl print`의 `runs`는 5였다(09-06 리셋 이후 값). 누적 지표로 쓰지 않는다.
- **게이트 F(push 자격증명)는 여전히 열려 있다** — `gh auth status`의 active account가 `davehan-nsuslab`이고 `atlas-han`은 비활성. 09-09의 우회로(`git -c credential.helper= -c credential.helper='!f() {…gh auth token -u atlas-han…}' push`)로 push한다. 항구 해결은 사람 몫.
- **게이트 B(릴레이 스케줄 자동 발화)는 이번에도 확인하지 않았다.**
- yt-dlp 목록 조회·자막 다운로드가 각각 1분 안에 끝났다 — 어제의 지연(쿠키 추출 경합 추정)은 재현되지 않았다.

## [2026-09-11] ingest | Tech Bridge 1편 — 빌드타임 vs 런타임 도구: 개발용 AI 도구가 프로덕션에서 실패하는 이유 (Google Cloud · MCP Toolbox)

2026-09-10 업로드분. `--playlist-end 15`가 **15편 반환**, 신규 1편, 나머지 14편은 기존. 롱폼만(최단 538초), Shorts 없음. ko·en-orig 전부 확보, **429 없음.** yt-dlp 목록·자막 모두 1분 안에 완료. launchd 정시 발화(09:10 KST), `run-ingest.sh`(pid 59785) 자식 세션.

| 소스 | 길이 | 화자 | 성격 |
|---|---|---|---|
| [[tech-bridge-build-time-vs-runtime-tools]] | 19:57 | [[averi-kitsch]] · [[prerna-kakkar]] ([[google-cloud]] 데이터베이스 · [[mcp-toolbox-for-databases]]) | 컨퍼런스 2인 발표 ⚠️ 당사자(플랫폼 판매자) · **데모 미실행** · 행사·촬영 시점 미확정 |

### 신규 (12페이지)

- **source 1** — 위 표.
- **concept 7** — [[build-time-vs-runtime-tools]] · [[confused-deputy-attack]] · [[lethal-trifecta]] · [[agent-identity-separation]] · [[secure-tool-evolution]] · [[bound-parameters]] · [[agent-tool-design-practices]].
- **entity 4** — [[averi-kitsch]] · [[prerna-kakkar]] · [[google-cloud]](위키 두 번째 Google 조직 · 첫 클라우드 플랫폼 벤더) · [[mcp-toolbox-for-databases]].

### 기존 보강 (11페이지)

[[prompt-injection]](**성립 조건: 치명적 3요소** · 다섯째 벡터: 신뢰된 내부 시스템 — 노출 경로=진입 경로) · [[agentic-misbehavior]](테이블 삭제 — 처방이 분류기가 아니라 **도구 자체**) · [[agent-governance-layers]](벽의 **네 번째 자리: 도구 정의 YAML**, ②층 없음, 표에 행 추가) · [[credential-injection-outside-sandbox]](**셋째 자리: 도구 파라미터** — 세 소스·세 위협·같은 벽 표) · [[model-context-protocol]](MCP 서버가 **가드레일의 자리**가 된 첫 사례 · Google managed MCP · "Cloud Code" 판정 불가) · [[action-reversibility]](세 번째 처방: 되돌릴 수 없는 행동을 **도구에서 뺀다** · 가역성=도구 분류 기준) · [[no-silent-write]](도구 층의 읽기/쓰기 분리) · [[knowledge-work-agent-gap]](한 영역에서 세워진 거버넌스 primitive) · [[agent-distributed-systems]](최소 권한의 구체적 형태=세 신원 · 조치 가능한 오류) · [[google-deepmind]]([[google-cloud]]와 구분) · [[tech-bridge]](sources 34→35, 새 주의사항 9건).

`index.md`(실측 **340→352**), `overview.md`(현재 상태 문단 + 진화 로그), `log.md`.

### 핵심 합성

**이 위키의 보안 축이 처음으로 데이터베이스에 닿았고, 프롬프트 인젝션에 성립 조건이 생겼다.** [[prompt-injection]]은 넉 달 동안 *콘텐츠가 어디로 들어오는가*(벡터 넷)만 모았는데, Simon Willison의 [[lethal-trifecta]](비공개 데이터 + 신뢰 불가 콘텐츠 + 외부 노출 능력)가 들어오면서 이 위키가 따로따로 모아 온 방어들 — probe·토큰 격리·외부화 차단·읽기 전용·신원 바인딩 — 이 **세 요소 중 어디를 빼는가**로 정렬됐다. 그리고 [[agent-governance-layers]]의 *벽은 에이전트 바깥에* 가 네 번째 자리(도구 정의 YAML)를 얻었고, [[anthropic-managed-agents]]·[[promptql]]·Google Cloud 세 소스가 서로 모른 채 **에이전트 손에 신원·자격증명을 두지 않는다**는 같은 원칙에 닿았다는 것이 확인됐다 — 벽의 자리만 다르다(vault+프록시 / 프록시 / 도구 파라미터). 위키는 어느 자리도 채택하지 않는다.

### 새 주의사항 (상세는 [[tech-bridge]])

- 원본에서 **데모가 재생되지 않을 수 있다** — 09-06(시작)·09-09(끝)와 다른 **중간의 결손**이고 결손된 것은 자막이 아니라 **시연 자체**. 예고를 결과로 취급하지 않았다.
- **설명란이 본문보다 강하게 주장**하는 두 번째 사례("실제 사고 사례" vs "예시 또는 데모 중 하나").
- **ko가 주어를 치환해 요점을 뒤집음**(18:07, 에이전트→시스템). 09-07 부호 뒤집기와 다른 새 유형 — 문장이 자연스러워 자막만 보면 안 잡힌다.
- **동음 오인식(write→right)이 한 문장에서 두 방향으로** 번역됨("오른쪽으로 가기 권한" / "적절한 도구").
- 전문 용어의 **분야 이동 오역**(triage→환자 분류, JWT claims→청구 내역, tool→공구, maps→지도).
- 약어 확장 창작 재발(LLM→법률 전문가, 세 번째), ASR 연쇄(LangChain→토지 사슬), **고유명사가 일반어로 오인식되어 소실**(데모 앱 이름 similar→"비슷한 서비스").
- **양 트랙이 같아도 판정 불가한 고유명사**("Cloud Code" — Google Cloud Code / Claude Code) — 채택하지 않음.
- 첫 **2인 교대 발표** — en-orig `>>` 표시와 인계 발언으로 구간별 화자 확정(전반 Prerna, 후반 Averi).

### 해소하지 않고 표시만 한 것

테이블 삭제의 실체(실제/데모, 일시, 규모) · 데모 동작(속지 않는다는 예고만) · eval bench 내용(페이지 미생성) · "Cloud Code" · 데모 앱 이름(*Cymbal* 추정) · "fully modeled control tool"(*model-controlled* 로 읽음, 추정) · 프레임워크 이름("by denting AI" → Pydantic AI 추정) · 비용·지연 수치 · JWT 발급·수명·위임 · 대안 부재(자사 도구 없는 세계 vs 있는 세계) · Willison 원문 미확보(전언).

## [2026-09-12] ingest | Tech Bridge 2편 — AI 슬롭을 측정하다(Taste Labs) · 디자인은 원샷할 수 없다(Impeccable)

2026-09-11 업로드분. `--playlist-end 15`가 **15편 반환**, 신규 2편, 나머지 13편은 기존. 롱폼만(최단 538초), Shorts 없음. ko·en-orig 전부 확보, **429 없음.** yt-dlp 목록·자막 모두 1분 안에 완료. launchd 정시 발화(09:10 KST, 실제 시작 09:10:27), `run-ingest.sh`(pid 97843) 자식 세션. `runs=2`.

| 소스 | 길이 | 화자 | 성격 |
|---|---|---|---|
| [[tech-bridge-taste-labs-measuring-slop]] | 14:34 | [[thais-castello-branco]] ([[taste-labs]] 창업자) | 컨퍼런스 단독 발표 ⚠️ 당사자(평가·데이터 공급자, Brand API 판매자) · **수치 전무** · 행사·촬영 시점 미확정 |
| [[tech-bridge-impeccable-design-steering]] | 15:30 | [[paul-bakaus]] ([[impeccable]] 제작자) | 컨퍼런스 단독 발표 ⚠️ 당사자(도구 제작자) · 슬라이드 시연 · **촬영 2026년 화자 발화로 확정** · 행사 미확정 |

**채널 첫 디자인·취향 축.** 같은 행사·앞뒤 순서일 가능성(Paul의 *"다음 발표자들"* 예고)이 있으나 두 설명란 모두 행사명이 없어 09-07 절차대로 **별개로 취급**, [[taste-vs-judgment]]에 나란히 뒀다.

### 신규 (14페이지)

- **source 2** — 위 표.
- **concept 8** — [[ai-slop]] · [[slop-probes]] · [[taste-vs-judgment]] · [[intentional-out-of-distribution]] · [[structured-brand-context]] · [[adjective-verb-steering]] · [[steering-altitude]] · [[no-one-shot-design]].
- **entity 4** — [[thais-castello-branco]] · [[taste-labs]] · [[paul-bakaus]] · [[impeccable]].

### 기존 보강 (15페이지)

[[signal-layer]](수렴 기계의 측정 · 취향/판단 같은 단어 선택 · 채점기 경계선 **세 번째 이동**(프로브) · **경계선이 위임 고도를 정한다**) · [[generator-evaluator-pattern]](**LLM이 아닌 평가자** · **기준이 낡는다**(purple gradients → Claude 베이지) · 평가 기준을 생성자 안에 넣은 경우 · 사람-에이전트 멀티샷) · [[agent-skills]](**어휘를 담는 스킬** · portable 실증 · 자동화를 거부하는 첫 스킬) · [[multimodal-elicitation]](공통 언어의 두 공급 방식 표) · [[fuzzy-intent-discovery]](디자인의 articulation gap — 낮은 의도 · 네 질문) · [[decision-quality]](디자인 판 — *"아무도 결정하지 않았다"* · 측정 방법 부재 반복) · [[transcript-classifier]](산출물 품질 게이트와의 대비 표) · [[verifiable-goals]](주관 영역에 verifier — 분해 / 사람 verifier 문장) · [[agentic-sites]](브랜드 준수의 다른 형태 — 코퍼스 vs 구조) · [[dhh]](네 입장) · [[sutton-bitter-lesson]](다섯 번째 축 — 추론 시점 상호작용 · 희소성의 정의) · [[skill-self-improvement]](승격 게이트가 커뮤니티일 때) · [[figma]](디자인 도구로서의 Figma — 고도가 너무 낮음) · [[claude-code]](디자인 스킬 호스트 · *Claude 베이지* · ASR "cloud code" 확정) · [[tech-bridge]](frontmatter sources 32→37 — 신규 2 + **09-09 3편이 frontmatter에 빠져 있던 것 보충**(References에는 있었음), 새 주의사항 11건).

`index.md`(실측 **352→366**), `overview.md`(현재 상태 문단 + 진화 로그), `log.md`.

### 핵심 합성

**두 소스는 서로 모르고 취향에 대해 반대 방향인데 같은 두 지점에서 만난다.** Taste Labs는 *안목을 모델에 훈련시키는* 회사이고 Paul은 *"취향은 실험실에서 배양될 수 없다"* 고 하지만 — ① 둘 다 슬롭을 *품질이 낮은 것* 이 아니라 **의도·결정의 부재**로 정의하고(Thais의 *낮은 의도* = Paul의 *"아무도 아무것도 결정하지 않았다"*), ② 둘 다 **추론 시점에 사람의 판단·조향이 남는다**고 한다(Thais: *"모델만 좋아져도 슬롭은 남는다"* / Paul: *"auto는 없다"*). 그래서 [[dhh]]·[[lena-hall]]·Thais·Paul 네 입장은 취향의 **학습 가능성**에서 갈리되 **사람의 자리**에서 수렴한다 — 그리고 갈림의 실체는 *taste* 라는 말의 **범위**(분해 가능한 조각 / 넓은 선호 / 미학 / 아직 없는 일 / 희소성 자체)다. 위키가 두 소스를 합쳐 얻은 정리 하나: [[signal-layer]]의 **채점기 경계선이 위임 고도를 정한다** — 코드는 산출물 검증이 있어 [[goal-level-delegation|목표 수준]]으로 올라갔고, 디자인은 *"사용자도 의견이 있다"* 라서 사람이 [[steering-altitude|형용사의 고도]]에 남는다. 어느 소스도 이 연결을 말하지 않는다.

### 새 주의사항 (상세는 [[tech-bridge]])

- **발표 주제어가 ko에서 여섯 갈래** — *slop* → 오류·허술·음식·음압·기울기·부실. en-orig도 SOP·soop·soft. 주제어는 두 트랙 모두 여러 표기로 grep.
- **통계 용어 → 물류 용어** — *out of distribution* → "유통". 핵심 처방(창의성 API)이 자막에서 사라짐.
- **약어 확장 창작 네 번째** — *LLM-as-a-judge* → "법학 석사 심사".
- **결론 슬라이드 오역 재발** — *"There is no auto"* → "자동차는 없고"(09-10 *auto*→자동차 산업과 같은 단어).
- **하네스가 사라짐** — *coding harness* → "코딩 실력"(09-06 "배선"과 다른 방향).
- **외국어 용어 이중 오인식** — *Leitwort* → "light wart" → "가벼운 사마귀". 화자가 언어를 명시하면 그 언어로 검색.
- **화자의 자기 정정이 ko에서 소실** — *cannot* → *can be amplified*. 핵심 문장 직후 "uh so"는 정정 신호.
- **제품명이 형용사로** — *Impeccable* → "흠잡을 데 없는", 한 문장 뜻이 바뀜.
- **촬영 연도가 화자 발화로 확정된 첫 사례** — *"2026년 버전의 AI 슬롭"*.
- **"Claw Design" 하루 두 소스** — Claude Design 추정, 확정 안 함. 세 번째 소스에서 누락 개체 판단.
- **ko가 없던 의미 부여** — *extra high* → "고화질 설정".

### 해소하지 않고 표시만 한 것

Taste Labs 편 — 200만 사이트·프로브·LLM-as-a-judge 비교의 **모든 수치**, 프로브 갱신 주기, Brand API 출력 형식·검증 주체, 창의성 API 실체, "Claw Design"·"General Intelligence Compute of New York" 표기, *"두 가지가 흥미로웠다"* 며 하나만 말한 대목, 행사·촬영 시점. Impeccable 편 — 효과의 정량 근거, *"같은 모델 다른 언어"* 관찰의 표본, 어휘 전체 목록, 자기 점검 문장의 효과(자기 평가 편향), 워크플로 맵 상세, "algorithmic unilo"·"radian shaders", 라이선스, 예고된 Q&A 부재, *"어쩌면 영원히"* 와 *"지금은 좋지 않다"* 의 모호함(원리적 거부인지 능력 판단인지). 두 편의 **같은 행사 여부**.

---

## [2026-09-13] ingest | Tech Bridge 3편 — ACP(Block/Goose) · 마우스파워(Yutori) · 에이전트를 신뢰하는 법(Cursor Lauren Tan)

2026-09-12 업로드분 **3편**. `--playlist-end 15`가 15편을 반환했고 **전부 롱폼**(최단 538초), 신규 3편·기존 12편. ko·en-orig **전부 확보, 429 없음.**

| 소스 | 층 | 길이 |
|---|---|---|
| [[tech-bridge-acp-universal-remote]] — [[alex-hancock]]([[block\|Block]]) | **프로토콜** | 10:32 |
| [[tech-bridge-mousepower-measuring-agents]] — [[maximillian-piras]]([[yutori\|Yutori]]) | **경제** | 20:25 |
| [[tech-bridge-lauren-tan-trusting-agents]] — [[lauren-tan]]([[cursor\|Cursor]]) | **실천** | **59:41** |

**채널 기록 셋** — ① **최장편 59:41**(직전 55:17), ② **두 번째 무챕터 소스**, ③ **첫 온라인 워크숍 형식**(Zoom 화면 공유·채팅·시청자 질문·화면에 낙서하는 참가자까지 그대로).

### 세 층이 한 곳에서 만난다 — 검증

**뒤의 두 편은 서로를 언급하지 않으면서 같은 진단에 도달한다** — *병목은 생성이 아니라 검증이다*([[verification-bottleneck]]). 그런데 **답이 반대다**:

| | [[maximillian-piras]] (판매자) | [[lauren-tan]] (코드베이스 소유자) |
|---|---|---|
| 처방 | **검증이 실행만큼 비싼 작업은 고르지 않는다** → [[task-entropy-matrix]] | **검증을 스킬로 만들어 에이전트에게 넘긴다** → [[agent-verification-skill]] |
| 그다음 | 검증하는 에이전트를 만든다 | 제약을 CI로 하드 강제해 검증할 것을 줄인다 → [[hard-vs-soft-enforcement]] |

**모순이 아니라 가진 통제권의 차이**다 → [[verification-cost-asymmetry]].

### ① ACP — MCP의 반대 방향

[[model-context-protocol|MCP]]의 위치가 **방향으로** 재정의된다 — MCP는 *에이전트 → 도구*, [[agent-client-protocol|ACP]]는 *클라이언트 → 에이전트*. 논거는 규격이 아니라 채택이다(*"MCP의 힘은 MCP 자체가 아니라 모두가 쓴다는 것"* → [[standards-as-market-makers]]). 확장 규약이 **표준화의 순서를 뒤집는다** — 각자 `_` 커스텀 메서드로 확장하고 **겹치는 것을 승격**한다. 원격 전송(HTTP/WebSocket)이 붙으며 [[agentic-stack-decomposition|네 칸의 독립 배치]]가 가능해지고, [[agent-harness-design|하네스]]는 *"도구 호출 루프를 구현하는 프로그램"* 이라는 한 줄 정의와 함께 **교체 가능한 배포 단위**가 됐다.

### ② 마우스파워 — 정확성이 목적이 아닐 수 있다

[[james-watt|와트]]의 마력은 **과학적이지도 정확하지도 않았는데** 통했다 — *"애초에 한번 시도해 보게 만드는 문턱을 넘겨 줬기"* 때문이다(위키 **첫 역사적 인물 페이지**). [[trusted-throughput]]과 ***긴축(austerity)*** 이라는 **같은 단어에서 만나되 층이 다르다**(조직의 지표 vs 판매자의 전달 문제 → [[overspending-underusing-loop]]). [[mousepower]]는 **화자 본인이 지표가 아니라고 못 박았고**, 위키도 지표로 기록하지 않았다 — 운용 형태는 **의무**다(*"에이전트를 팔 거라면 검증 루브릭도 함께 줘야 한다"*).

### ③ Lauren Tan — 두 개의 뒤집기

- **그린필드가 브라운필드보다 위험하다**([[greenfield-vs-brownfield-agent-risk]]) — 대기업 인프라는 이미 *가장 능력이 부족한 엔지니어* 를 위한 가드레일이라 **에이전트 친화적**이고, 바이브 코딩된 그린필드는 [[organic-architecture|가드레일 없이 편의에 최적화되며 번져 나간다]].
- ***"AI 슬롭 이전에 인간 슬롭이 있었다"*** — [[ai-slop|슬롭]]을 **AI 고유 현상이 아니라 가드레일 부재의 함수**로 재정의. 09-12에 세운 *슬롭 = 결정의 부재* 와 **다른 경로로 같은 결론.**

방법은 셋 — [[agent-verification-skill|검증 스킬]] + [[feature-map|기능 지도]](*"???"* 만 적힌 스크린샷 제보도 작업으로) · [[dune-architecture|Dune]]([[shortest-path-architecture|"가장 짧은 경로가 가장 좋은 경로"]]) · [[hard-vs-soft-enforcement|강제의 층]](*"PR에 댓글로 강제하고 있다면 코드 스멜"*). [[skill-evals|눈가림 서브에이전트 eval]]이 **평가 사실 자체가 관찰 대상을 바꾸는 문제**를 실무 절차로 다룬 첫 사례다.

### ⚠️ 이번 실행의 가장 중요한 발견 — 업로드 날짜에 기댄 추정이 깨졌다

Lauren Tan 워크숍은 **[[grok-4-6|Grok 4.6]] 발표 당일**이고 **[[grokbot|GrokBot]] 출시 다음 날**인데, 화자가 *"이번 달은 아직 **12일**밖에 안 됐다"* 고 말한다(양 트랙 일치, 연도는 *"2026년"* 으로 확정).

그런데 위키는 [[tech-bridge-grokbot-agent-teams]]의 **Tech Bridge 업로드 날짜(2026-08-31)** 를 촬영 날짜로 써서 *"GrokBot 베타 2026-08-30 전후"*, 거기서 *"[[tech-bridge-cursor-legacy-refactoring]] 촬영 09-01 무렵"* 을 도출했다. **08-30·08-31은 12일이 아니다.**

이 위키는 **2026-09-03에 "업로드 날짜 ≠ 촬영 날짜"를 원칙으로 세웠는데 그 페이지들에는 적용되지 않았다.** 달을 확정할 근거가 소스에 없으므로(업로드일 09-12일 수는 없다 — Grok 4.6은 08-31·09-08 업로드분에서 이미 출시된 모델로 논의된다) **어느 날짜도 채택하지 않고 네 페이지에 반증 증거만 표시**했다.

→ **2026-09-09에 배운 것의 역방향이다.** 그때는 *위키가 이미 가진 소스가 촬영 시점 판정의 근거가 된다* 였고, 이번엔 *업로드 날짜에 기댄 추정은 뒤에 온 소스에 깨진다* 다. **나중 소스가 앞선 시점 추정을 무너뜨린 첫 사례.**

### 새 주의사항 (상세는 [[tech-bridge]])

- **⚠️ 설명란이 자막에 없는 사실을 주장한 세 번째 사례** — Lauren Tan 편 제목·설명란의 **"xAI GrokBot 워크숍"**. **자막 전체에 "xAI"가 한 번도 없고** 나오는 것은 **SpaceX AI**(위키의 기존 [[grok-4-6]] 기록과 일치). 09-10·09-11에 이어 → **설명란의 사실 주장은 본문 발화로 재확인.**
- **반대로 설명란이 자막보다 정확한 첫 사례** — 마우스파워 편에서 ko가 *horse gin* 을 **"마차"** 로 옮겼는데 **설명란은 "말 방아"** 로 맞다. 지금까지 설명란은 *과잉 주장* 쪽으로만 틀렸다 → **설명란은 양방향으로 대조 대상.**
- **⚠️ *agent* 가 한 영상에서 다섯 갈래** — 에이전트·상담원·**부동산 중개인**·**시약**·**물질**. 09-08의 3종(요원·상담원·에이전트)을 넘었고 **그중 둘이 발표 제목의 단어**다. 09-12의 *slop* 6갈래에 이어 **이틀 연속** → **주제어는 두 트랙 모두 여러 표기로 grep.**
- **약어 확장 창작 다섯 번째, 그리고 처음으로 대표 수치에서** — ko가 **PR(pull request)을 "개인 최고 기록(Personal Record)"** 으로 풀어 썼다. 같은 문단의 *"지난달 1,000개"* 는 PR로 옮겨서 **한 문장 건너 표기가 갈린다.**
- **ko가 사람 이름을 도구 이름으로 바꾸고, 자기 도구를 남의 도구로 뒤집는다** — **Gary Tan → "게리 스택"**(성이 같다는 농담의 전제 소실), 그리고 화자가 자기 플러그인을 **"GStack이라 지었다"** 로(실제는 **Pstack**). **사실관계가 반대가 된 사례.**
- **부호 뒤집기 재발, 또 결론 문장** — *"what would get you over the limit of trying it out"* → **"시도해 볼 엄두조차 내지 못하게"**. 09-07 이래 두 번째이고 둘 다 발표의 결론이다.
- **지시의 방향이 뒤집힌다** — *"I've got some guidance given to my agents"*(내가 줬다) → ko **"에이전트들에게 지침을 받았고"**. 09-11 *주어 치환* 계열이고 **문장이 자연스러워 자막만으로는 안 잡힌다.**
- **en-orig 오인식의 ko 직역 연쇄** — *pull requests* → en-orig *"poll requests"* → ko **"설문 조사 요청"**; *slop* → en-orig *"sloth"* → ko **"게으름"**(슬롭 일곱 번째 갈래).
- **없는 제품명 창작** — *"I had Claude vibe code me this"* → ko **"클로드 바이브에게"**. 그리고 **vibe coding이 통째로 소실**된 사례도 있다(ACP 편 *"이거 어젯밤에 바이브 코딩했다"* → *"문득 이런 생각이 들었어요"*).
- **결론 문장의 단어가 다른 뜻으로** — ACP 편 *"quality of the clients go up"*(클라이언트 **소프트웨어**의 품질) → ko **"고객들의 질"**. 발표의 마지막 주장이 다른 말이 됐다.
- **약어를 다른 분야 의미로** — *IP*(지적재산권, Linux Foundation 기증 직후) → ko **"IP 주소"**. 09-11 *claims*→"청구 내역" 계열.
- **제품명이 조류·건축·공구로** — *Goose* → **"거위"**(한 영상에서 Goose·구스·거위 3표기), *organic architecture* → **"유기적 건축"**, *borrow checker* → **"빌림 검사기"**, *Next.js* → **"Electron 앱용 JavaScript"**, 스킬 이름 `how` → **"방법"**, *Fable 급* → **"규모가 크지 않은"**(모델명 소실).
- **양 트랙이 같이 틀려도 판독할 수 있는 경우** — *"MP style problem"* 은 화자가 곧바로 *"실행보다 검증이 더 쉽다"* 고 **정의하므로 NP로 읽었다.** 09-11의 *"Cloud Code"*(판독 불가)와 달리 **판독 근거를 명시할 수 있으면 채택한다.**

### 해소하지 않고 표시만 한 것

**ACP 편** — 경쟁 표준·대안 검토 전무, 채택 수치 전무, **원격 전송의 보안 모델 전무**(인증·인가·신원 — [[lethal-trifecta]]가 가리키는 자리), `_` 커스텀 메서드의 충돌 처리와 표준화 거버넌스, Linux Foundation 기증의 거버넌스 구조, MCP의 *tasks* 기능, *"Title"*(→ Tidal 추정), 데모 3건의 실제 결과(화면 의존), **행사·촬영 시점 미확정**(09-04·09-08·09-09에 이어 네 번째).

**마우스파워 편** — **수치가 하나도 없다**(Yutori 규모, 토큰 비용, Coinbase 차트, Ramp 글, 매트릭스의 단위·임계값), **Upton Sinclair 인용문의 문구**(슬라이드 — 지어내지 않았다), **스위트 스팟의 구체적 사례 0건**(시간 초과), *"컴퓨트 속도의 측정"* 의 방법, **검증 에이전트의 독립성**, Ramp 블로그·*Noah Hine* 글(링크·철자 미확정), *Pepe Silvia*, **연도 미확정**(행사는 *World's Fair* 로 확정).

**Lauren Tan 편** — **모든 수치가 자기 보고**(PR 1,000/800/600+/20, *"주석의 99%"*, *"작업의 80%"*)이고 **평균 PR 크기는 본인도 모른다**, **자동 병합의 안전망**(회귀 사례·롤백 빈도 — 같은 화자가 *"agents window는 계속 회귀한다"* 고 말한다), **eval의 작성자=검증자 문제**(09-09 이래 세 번째), **눈가림 디렉터리의 효과 미측정**, **코드 주석 금지의 대가**(왜 그 코드가 그런지의 지식), `useEffect` 금지의 대안, **Dune이 오픈소스가 아님**(외부 검증 불가), *"은행을 털지 않고도 가능하다"* 의 근거, Grok 4.6 가격(**화자 본인 유보**), **진행자 Colin의 성·소속**, 가상화 라이브러리 이름·*"kusher moment"*(판독 불가), **촬영 시점의 달**.

---

## [2026-09-14] ingest | Tech Bridge 3편 — 대담한 소프트웨어(Dioxus) · Pstack 제3자 리뷰 · Zuckerberg의 Muse(Meta)

2026-09-13 업로드분 **3편**. `--playlist-end 15`가 15편을 반환했고 **전부 롱폼**(최단 538초), 신규 3편·기존 12편. ko·en-orig **여섯 트랙 전부 429 없이** 확보했다.

| 소스 | 자리 | 길이 |
|---|---|---|
| [[tech-bridge-ambitious-software-agent-era]] — [[jonathan-kelley]]([[dioxus\|Dioxus]]·[[cognition\|Cognition]]) | **만드는 쪽** — 오픈소스 프레임워크 메인테이너 | 18:45 |
| [[tech-bridge-pstack-third-party-review]] — **화자 미상**([[molten-base\|Molten Base]] 제작자) | **쓰는 쪽** — 남의 스택을 시험하는 리뷰어 | 11:34 |
| [[tech-bridge-zuckerberg-muse-personal-agent]] — [[mark-zuckerberg]]([[meta\|Meta]]) × [[alex-heath]] | **파는 쪽** — 출시 제품의 CEO | **65:19** |

**채널 기록 둘** — ① **최장편 65:19**(직전 59:41, 그전 55:17 — **사흘 만에 두 번**), ② [[tech-bridge-harness-engineering]] 이래 처음으로 **제3자가 남의 도구를 리뷰하는 형식**.

### ① Dioxus — 실패 고백에서 꺾이는 발표

앞 절반은 5년치 성취(별 37k·누적 사용자 2억+·[[blitz\|Blitz]]·[[subsecond\|Subsecond]] 100ms 핫 리로드)이고, 그 끝이 *"최근까지 모든 코드는 손으로 썼다"* 다. 그다음이 **[[slop-cannon\|슬롭 캐논]]** — 구독 한도를 소진하며 수만 줄을 쏟아냈는데 *"품질 기준을 통과한 코드는 거의 없었다"*.

> **이 위키에서 [[ai-slop\|슬롭]]이 생산자 자신의 입으로 진단된 첫 사례다.** 09-11 [[tech-bridge-taste-labs-measuring-slop\|Taste Labs]]는 *재는 쪽*, 09-12 [[tech-bridge-lauren-tan-trusting-agents\|Lauren Tan]]은 *막는 쪽* 이었다. 그리고 **실패의 형태가 다르다** — 나쁜 것이 머지되는 게 아니라 **아무것도 머지되지 않는다**(*"draft에 처박힌 채 계속 처박혀 있었다"*).

재배치 다섯:

- **[[learning-curve-as-feature\|어려움이 기능이 됐다]]** — *"빌림 검사기와 싸워 주니, 우리가 줄이려고 싸웠던 학습 곡선이 이제 기능"*. **강제의 층이 [[hard-vs-soft-enforcement\|PR 댓글]] → [[verifiable-goals\|린트·CI]] → 컴파일러까지 갔다.** 성립 조건은 *컴파일러가 빨리 답할 것* 이고, 같은 팀이 [[subsecond]]를 만든 것을 그 조건과 함께 읽는다.
- **[[agents-as-patient-specialists\|강점은 지능이 아니라 인내심]]** — Kotlin·Swift 플러그인이 *"손으로는 여러 해"* 에서 **2~3주**. 시간 배분이 핵심이다 — **구현 첫날, 테스트 2주.** 지식 문제가 사라지자 남은 것은 검증이다.
- **[[code-is-the-product\|코드가 곧 제품]]** — 가장 크게 번 곳은 릴리스 체크리스트·백포팅·**문서 동기화**(*"인간은 코드는 고치고 주석은 안 고친다"* → [[comments]] code smell의 재배치).
- **[[test-harness-vs-test-authoring\|테스트는 둘로 갈린다]]** — *"인간과 마찬가지로 올바른 테스트를 쓰는 데는 실패"* / **퍼징 하네스 구축은 탁월**.
- **[[architecture-as-remaining-art\|남은 예술은 아키텍처]]** — *"에이전트도 스파게티 코드를 쓴다, 다만 더 빠르게"*, *"기반이 나쁘면 그 위에 무엇을 올려도 나쁘다"*.

### ② Pstack 리뷰 — 위키가 제작자 바깥에서 도구를 본 첫 사례

09-13에 만든 [[pstack]] 페이지는 **전부 제작자 본인 진술**이었다. 이 소스가 그 바깥이다.

- **구조**: potato mode = **라우터**, 플레이북 22개, 스킬 20여 개. **계획 스킬이 의도적으로 없다** — *"최고의 사양은 코드다"*(간접 인용) → [[spec-driven-development]]·[[intent-md]] 계열과 **정면 대립하는 극**.
- **병렬성의 축이 생겼다** — **[[agent-arena\|아레나]]**(같은 문제·다른 모델·**접목이나 기각**) vs **[[agent-swarm\|스웜]]**(조각 분배·집계). 지금까지 [[dynamic-workflows]]·[[generator-evaluator-pattern]]에 **없던 구분**이다.
- **원칙 7개** — [[laziness-protocol]]·제1원칙 재설계·[[minimizing-reader-load]]·설계 공간 소진·[[build-a-lever]]·검증·컨텍스트 창 보호. [[minimizing-reader-load]]가 코드 품질의 **네 번째 단위**(결정·시스템·제품에 이어 **사람의 상태**)다.
- **비용의 첫 값** — 같은 프로젝트가 [[fable-5-1\|Fable 5.1]] 맨몸 **30분**, Pstack **1시간**. ⚠️ 단일 사례·단일 관찰자·토큰 값 없음 → **일반 계수로 쓰지 않는다.**
- **검증이 실제로 잡은 것** — *"에이전트가 세부를 환각했다는 걸 스스로 깨달았고 **허위 주장 세 건**을 잡아 고쳤다."* 이 위키에서 **몇 건인지가 나온 첫 사례**다.

### ③ Zuckerberg — 위키 첫 Meta 당사자 소스

- **[[balance-of-power-safety\|안전 = 권력 균형]]** — 지금까지 이 위키의 안전 담론은 *게이트를 어디에 둘 것인가*([[training-time-risk]])였는데 여기서는 **게이트 자체가 위험**이다. *"소수의 랩이 통제하는 쪽이 훨씬 더 걱정"*, 법정 비유(*"모두가 초지능 변호사를 가지면 어리석은 주장이 서 있지 못한다"*).
- **[[muse]]** — VM 붙은 장수명 에이전트. 목표를 주면 24시간, **밤에 성찰을 메모리로 굳히고**, 새 프로젝트를 제안한다.
- **[[transaction-cut-monetization\|주당 1억 토큰 무료 + 거래 수수료]]**(부담은 거래 상대 기업, Stripe). **토큰 과금 전제를 벗어나는 첫 모델**이고, [[mousepower]]가 진단한 *"이게 그만한 가치가 있었나"* 를 **가격 구조로 우회**한다.
- **보안 4겹** — [[confidential-vm]]([[moxie-marlinspike]] 영입, *"Meta조차 볼 수 없고 기술적으로 검증 가능"*) · [[sentinel-agent]](인젝션 + **과잉 공유** → 사람 검토 트리거) · [[least-privilege-connectors]](이메일은 **읽기 전용부터**) · 자격증명 저장소. **에이전트 보안을 구성 요소 단위로 말한 첫 CEO 소스**이고, 09-10 [[tech-bridge-build-time-vs-runtime-tools\|Google Cloud]]의 제로 트러스트 사다리가 **소비자 층에서 같은 어휘로 반복된 첫 확인**이다.
- **[[agent-fleet-learning\|함대 학습]]** — 익명화된 통찰을 에이전트끼리. ⚠️ **"익명화"의 정의가 없고, 같은 대담의 [[confidential-vm]]과 어떻게 양립하는지 설명되지 않는다.** 이 소스의 가장 큰 미해결 긴장.
- **Llama 4 실책 인정** → [[talent-density]]. *"다른 머신러닝을 잘하니 LLM도 비슷할 거라 가정한 게 실수"*, 랩을 **자기 좌석 주변에 물리적으로** 지었다. **CEO 소스 중 자기 실책을 의사결정 수준에서 말한 첫 사례.**
- **[[discretion-capability\|신중함]]** — *"임신했다고 말하지 않고 무알코올 칵테일이 있는 곳을 예약"*. 위키가 모은 능력 축에서 **유일하게 "덜 하는" 능력**이고, **경쟁 제품([[claude-code]])을 깎지 않고 좌표로 쓴 첫 사례**다.
- **[[reward-hacking]]** — *"모든 랩이 보고 있다"*. [[agentic-misbehavior]]에 **경쟁 랩의 독립 확인**이 붙었다. 처방은 [[sam-altman]]과 반대다 — 저쪽은 **훈련을 연기**, 이쪽은 **환경의 경계를 조인다**.

### 위키의 기존 기록이 바뀐 곳

- **[[verification-bottleneck]]에 세 번째 답** — *작업을 고른다*(09-12 Piras) · *역량을 짓는다*(09-12 Tan)에 이어 **일을 쪼갠다**(무엇을 검증할지는 사람, 장치는 에이전트). 퍼징 하네스는 **의견을 내지 않으므로** 09-09 이래 표시해 온 *작성자=검증자* 문제를 **구조적으로 피한다.**
- **[[hugging-face]]에 첫 제3자 서술** — 이 페이지는 09-06에 [[openai]] CEO 진술만으로 만들어졌고 그 한계가 문서에 명시돼 있었다. Zuckerberg가 *"침입을 감지했을 때 **오픈소스 모델로 돌아섰다** — 문제를 일으키던 폐쇄 모델에 접근할 수 없었으니까"* 라는 **새 구간**을 준다. ⚠️ **여전히 HF 측 진술이 아니고** 화자의 논지(오픈소스가 안전에 기여한다)의 예시로 제시된다.
- **[[openclaw]]가 여섯 번째 소스** — 처음으로 **경쟁 제품의 CEO** 가 부르고, 서술의 성격도 다르다(*"수백만은 될지 몰라도 수십억은 아닐 것"* — 시장 구조의 좌표). **여전히 어느 소스도 OpenClaw 자체를 설명하지 않는다.**
- **[[openai-astra]]를 제3자가 처음 부른다** — Pstack 리뷰어가 *"[[fable-5-1\|Fable]]이나 Astra 같은 모델"* 로, **프론티어 등급의 대표**이자 *"모델이 흡수할 층인가"* 라는 질문의 모델 쪽 이름으로.
- **[[fable-5-1]] 페이지 신설** — *Fable* 이라는 이름은 09-01부터 스쳤지만 **버전이 붙어 확정되고, 같은 날 세 소스가 좌표로 쓴다.** ⚠️ 1차 자료가 없고 스펙이 전무하다.
- **[[lauren-tan]]에 첫 제3자 서술** — ⚠️ 리뷰어가 **SpaceX principal engineer**라고 소개하는데 **본인 진술에 없다.** 채택하지 않고 표시만 했다. 09-13의 *설명란 "xAI GrokBot 워크숍"이 자막에 없다* 와 **같은 자리**를 건드린다.

### 새 주의사항 (상세는 [[tech-bridge]])

- **⚠️ ko 자막이 화자와 대상을 뒤바꾼 첫 사례.** Pstack 편 *"**So this is** Lauren Tan (…) **She's** worked at Netflix"* → ko **"안녕하세요, **저는** 닌자 엔지니어 로렌 탄입니다."** **ko만 읽으면 리뷰어가 Lauren Tan 본인이 된다.** → **화자 정체는 en-orig 대명사로 확인한다.**
- **⚠️ ko가 문장 하나를 통째로 삭제한 첫 사례.** Zuckerberg 편의 *"[[grokbot\|GrokBot]]이든 [[town\|Town]]이든 Instinct든, 이렇게 하는 제품이 많습니다"* 가 **ko에 아예 없다.** 지금까지 소실은 단어·구 단위였고, 하필 **위키가 이미 페이지를 가진 두 제품을 경쟁사 CEO가 같은 범주로 묶은 진술**이다.
- **⚠️ ko가 자막의 구멍과 잘림을 매끄러운 문장으로 덮는다 (첫 사례, 하루 두 건).** Dioxus 편 05:02~05:08에서 en-orig가 끊기는데 ko는 자연스럽게 이었고, Pstack 편은 **en-orig가 11:32에서 잘리는데 ko가 완결형으로 마무리**한다. → **ko만 보면 결손이 보이지 않는다. 길이·끝 문장을 두 트랙에서 대조한다.**
- **⚠️ 약어 확장 창작 여섯 번째, 처음으로 위키의 핵심 용어** — *"check your MCPs"* → ko **"MCP(Master Career Program)"**.
- **⚠️ *PR* 오역이 이틀 연속, 매번 다른 오역** — 09-13 *"개인 최고 기록"*, 이번 **"보도자료"**(3회).
- **⚠️ 보안 용어가 일반어로** — *prompt injection* → **"무단으로 접근하려는 시도"**([[prompt-injection]] 소실). 09-12 *harness→"코딩 실력"* 과 같은 **추상화 방향**.
- **⚠️ 제품명이 양 트랙 모두 네 갈래 (최다)** — *Dioxus* → **Diosis·Dioxis·Daxis·DAX**. 09-12 *Goose* 3표기를 넘었고 **en-orig부터 틀렸다.**
- **⚠️ 고유명사가 보통명사·다른 이름으로** — *Cognition*→**"인지 컴퓨팅"**(다음 문장에서는 복귀), *prompt engineering*→**"신속한 엔지니어링"**, *discretion*→**"재량권"**, *FAIR*→**소실**, *Artificial Analysis*→**"아티팩트 애널리시스"**, *SemiAnalysis*→**"시몬스 분석"**, *Claude Code*→**"클로 코덱스"·"클로 코드"**(하루 두 소스).
- **⚠️ 관용구 직역이 방향까지 뒤집는다** — *"Lauren has also **baked in** some great disciplines"* → ko **"로렌은 훌륭한 **제빵 기술**들을 많이 **익혔습니다**"**(심었다↔익혔다).
- **✅ 설명란이 자막을 고쳐 주는 두 번째 사례** — *slop cannon*. ko는 *"엉망진창 요리"* 로 지웠는데 **설명란은 '슬롭 캐논(Slop Cannon)'이라고 정확히 적는다**(09-12 *말 방아* 에 이어).
- **⚠️ 설명란이 자막에 없는 수치를 준다 (네 번째)** — Pstack 편의 **"21가지 원칙"** 이 자막에 없다(이름 붙은 것은 **일곱 개**). `/poteto-mode` 표기도 설명란 단독.
- **✅ 같은 고유명사의 처리가 개선된 첫 관측** — *Hugging Face*. 09-06의 **"얼굴 껴안기"** 가 이번엔 **음차로 정확**하다.
- **화자 발화로 연도가 확정된 두 번째 사례** — Dioxus 편 *"2026년 현재"*. **행사명은 여전히 없다.**

### 해소하지 않고 표시만 한 것

**Dioxus 편** — **행사명 없음**, **팀을 돌려세운 계기가 자막 구멍에 있음**(05:50~06:01, 지어내지 않았다), **비교군 전무**(*"2~3주"*·*"이전 어느 때보다 많은 패치 릴리스"* 에 이전 값 없음), **품질 기준의 내용 없음**, **슬롭 캐논에서 빠져나온 절차 없음**, 어떤 에이전트·모델인지 미확정(*"구독"* 판독 불가 — 09-11 *"Cloud Code"* 선례 적용), Blitz·Subsecond 수치의 측정 조건, **Cognition 인수 시점·조건**, *"Rust easel"*(양 트랙 파손 — 인용하지 않음), **컴파일러가 잡지 못하는 결함에 [[learning-curve-as-feature]]가 적용되는지**.

**Pstack 편** — **화자 이름 없음**, *"Ninja engineer"* 의 출처 미확정, **"21가지" 중 14개 없음**, 플레이북·스킬 목록 없음(화면), **`interrogate`의 모델 구성·불일치 해소 규칙**, **아레나의 접목 판정 기준**(=평가자 독립성, 09-09 이래 네 번째), *"겁 없는 병렬성"* 미검증(**리뷰어 본인이 유보**), **비용 비교의 토큰 값**, *"Cursor가 아레나를 6개월 전에 뺐다"* 의 근거, **SpaceX 이력**(채택하지 않음), [[molten-base]]의 공개 여부·라이선스, **en-orig 마지막 문장 잘림**.

**Zuckerberg 편** — **반증 가능한 주장이 하나도 없음**(*"아무도 안 한다"* 3회), **Muse 수치 전무**(사용자·가격·수수료율·초과 단가·성능), **기밀 VM의 검증 방법**, **센티널의 탐지율·오탐·자기 자신에 대한 인젝션**, **함대 학습의 "익명화"**(그리고 [[confidential-vm]]과의 양립), **모델명 미확정**(*Muspark 1.3* / *mpark*), **"Nat"의 성**, **"Instinct"가 무엇인지**, **Llama 4 실패의 내용**, *재귀적 개선* 은 언급만, **Hugging Face 측 진술 아님**, **10대 안전 합의의 상대·조건·시점**, *"full soda like Frontier"*(양 트랙 파손 — 인용하지 않음), **촬영 시점 미확정**.

## [2026-09-15] ingest | Tech Bridge 2편 — Graft: 탐색을 지식 그래프로(AI Labs) · 디자이너 한 명 + AI(Vincent Wendy, AI Engineer)

`--playlist-end 15`가 **15편** 반환, 전부 롱폼(최단 632초, Shorts 없음). 신규 **2편**(둘 다 2026-09-14 업로드), 나머지 13편은 기존. ko + en-orig 전부 확보, **429 없음**. yt-dlp 목록 조회는 몇 분 걸렸고(경고 다수, 재시도 없이 완료) 자막은 1분 내 완료.

**신규 source 2 · concept 13 · entity 5, 기존 22페이지 보강. index 실측 436 → 456.**

- [[tech-bridge-graft-code-knowledge-graph]] (11:27, [[ai-labs|AI Labs]] / [[graft|Graft]]) — 화면 녹화 해설. **비용은 편집이 아니라 탐색에서 나온다**([[file-discovery-tax]]). 프로젝트를 노드/엣지 [[code-knowledge-graph|지식 그래프]](로컬 JSON, **모델 미사용**)로 만들고 **훅 셋**(세션 시작 / 프롬프트 / 편집 후)으로 워크플로를 강제한다([[hook-enforced-workflow]]). 벡터 검색과의 차이를 *계정 생성 vs 계정 삭제*로 못 박고([[reference-graph-vs-vector-search]]), **CLI(밀어 넣기·빠름) vs MCP(물어보기·정확)** 트레이드오프를 스스로 측정한다([[push-vs-pull-context-retrieval]]). 신선도는 증분 갱신 + 조회 직전 검사 두 겹([[incremental-index-freshness]]). 자체 벤치마크 162회: 시간 −60% · 도구 −46% · 토큰 −42% · 비용 −32%. 시연 1회: 39분/31% vs 47분/35%.
- [[tech-bridge-one-designer-plus-ai]] (16:18, [[vincent-wendy|Vincent Wendy]] / [[ai-engineer|AI Engineer]]) — **위키가 컨퍼런스를 안쪽에서 보는 첫 소스.** 12~15명·디자이너 1명이 참석자 7,000명·스폰서 140곳+·발표자 300명+·세션 600개+를 감당한다. 다섯 처방(기초 · 재사용 · 자동화 · 검증 · 마찰 제거), [[atomic-design]], *"정의해 두지 않으면 [[ai-slop|슬롭]]이 나온다"*([[design-system-as-agent-context]]), **Devin이 Slack에 살아서 워크플로가 다시 쓰였다**([[design-handoff-friction]]), 300명이 자기 그래픽을 직접 만든다([[self-serve-asset-generation]]), 140곳 로고 누락 검수([[agent-visual-qa]]), 펠리컨 SVG가 안 되면 PNG→벡터화([[capability-detour]]), **"진짜 일은 예외 처리다"**([[exception-handling-as-the-job]]).

**이날의 구도** — 두 편이 *에이전트가 무엇을 덜어 주는가*에 정반대 답을 준다. **기계가 기계에게 조달해 주는 것**(턴·토큰) vs **사람이 사람에게서 덜어 내는 것**(300명분 그래픽·140곳 검수·1회용 편집 버튼). 두 번째 편에는 **비용 이야기가 한 마디도 없다** — 단위가 *한 사람이 감당하는 결과물 수*다.

**새 주의사항 여덟**: ① **ko가 "다섯 가지"라고 말하면서 넷만 열거한다(첫 사례)** — `reusable designs` 누락, 개수는 그대로. 지금까지의 소실은 단어·구·문장 단위였고 **열거 항목 누락은 처음**이며 하필 뒤에 챕터 하나를 차지하는 항목이다. ② **ko가 `speaker`를 음향기기로 읽어 한 절을 통째로 파괴** — *발표자 300명* → "스피커가 300개", *speaker announcement* → "안내 방송", *access* → "들을 수 있어요"(원문에 없는 기능). ③ **✅ 챕터 제목이 자막을 고쳐 준 첫 사례** — ①②와 *"Devin, GPT, Figma"* 셋의 판독 근거가 전부 **공식 챕터 제목**이다. 09-12·09-13은 **설명란**이었다 → **챕터도 양방향 대조 대상.** ④ **도구 이름이 자기가 만드는 자료구조와 같은 소리로 뭉개진다(첫 사례)** — [[graft|Graft]] ↔ *graph*, ko "접목"까지 세 표기. ⑤ **약어 확장 창작 일곱 번째** — *LLM* → "로컬 라이프사이클 관리"(같은 문장에서 *Claude* → "클라우드 기반 시스템"). ⑥ **주제어 오역이 소스를 건너 재발한다** — *slop* → "기울기"는 09-12 Taste Labs 편에서 기록한 갈래인데 **다른 소스·다른 화자에게서 그대로** 나왔다 → 소스별 특이사항이 아니라 **채널 전반의 패턴**으로 다룬다. ⑦ **원칙 이름이 요약 자리에서 지워진다** — *remove friction* 을 ko가 04:47에는 "마찰 요소"로 옳게, 14:03 맺음말에는 **"허구"** 로. ⑧ **부호 뒤집기가 두 문장 안에서 일어났다 되돌아온다** — *"편집 버튼이 없다"* → "버튼 하나로 다 됐다" → 다음 문장에서 복귀, **ko 안에서 자기모순.**

부수: 제목이 자막에 없는 순위를 주장(*"GitHub 1위 트렌딩"* — **과잉 주장 네 번째이자 첫 "제목" 사례**), ko가 없던 분야를 추가(*independent providers* → "독립 **의료** 서비스 제공자"), ko가 잘린 끝을 매끄럽게 메움(세 번째), *hook* 이 "고리·훅·후크" 세 표기, *turn* → "회전", *atomic* 이 "오토믹·아토믹" 두 표기, *vector/SVG* → "팩터"·"팩터링 분석", *font size* → "휴대폰 크기"(en-orig *phone* 오인식의 직역), *AI Engineer*(조직) → "AI 엔지니어링 팀", `claw.md` → `CLAUDE.md`, `learnings.m MD` → `learnings.md`.

**행사·촬영 시점**: 두 편 모두 미확정. Graft 편은 컨퍼런스가 아니고, Vincent 편은 *"AI Engineer, 이 컨퍼런스"* 까지다(유일한 앵커는 *"2025년에 Simon Willison이 한 강연"* → 2025년 이후). 09-07 절차대로 [[tech-bridge-mousepower-measuring-agents|World's Fair 편]]과 대조했으나 겹치는 단서가 없어 **별개로 취급**했다. **2026-09-13에 배운 대로 업로드 날짜를 앵커로 쓰지 않았다.**

**해소하지 않고 표시만 한 것**: Graft 편 — 벤치마크 조건 전부(162회가 무엇의 162회인지·모델·저장소·대조군), **만든 주체**(설명란의 `trailhq.com` 외에 회사명·사람 없음), 라이선스 종류, **지원 언어**(참조 관계를 뽑으려면 파서가 필요한데 한 마디도 없다 — [[tree-sitter]]가 위키에 있으나 소스가 연결하지 않는다), 대형 저장소 빌드 시간, *"최대 3개"* 의 근거와 오탐 처리, **매 프롬프트 자동 주입의 [[prompt-injection]]·[[lethal-trifecta]] 표면**(전혀 논의 없음), MCP의 *"정답 몇 개 더"* 의 분모, AI Labs Pro의 정체(자막이 그 문장에서 잘린다), 발표자 이름(2회 연속). Vincent 편 — 행사명·연도, **"정확도 100%"의 표본·시행·오탐**(작성자=검증자), [[devin|Devin]]의 제작사(위키에 [[cognition]]이 있으나 **소스가 연결하지 않으므로 연결하지 않음**), 스펙 시트 플러그인 이름, *Jason Leu* 철자(**어느 표기도 채택 안 함**), *TBPN* 의 정체, 생성기의 접근 범위, 즉석 기능의 검토·롤백, 화자의 국적(설명란 LinkedIn이 `id.` 도메인 — **추정으로만 표시**).

## [2026-09-16] ingest | Tech Bridge 2편 — AI 엔지니어의 세 층(Cedric Clyburn, IBM Technology) · Dario Amodei CBS 인터뷰(Anthropic CEO)

`--playlist-end 15`가 **15편** 반환, 전부 롱폼(최단 632초, Shorts 없음). 신규 **2편**(둘 다 2026-09-15 업로드), 나머지 13편은 기존. ko + en-orig 전부 확보, **429 없음**. yt-dlp 목록 조회 1분 내(경고 다수, 재시도 없음), 자막 두 편 합쳐 1분 내.

**신규 source 2 · concept 10 · entity 2, 기존 16페이지 보강. index 실측 456 → 470.**

- [[tech-bridge-ai-engineer-three-tier-skill-stack]] (10:38, [[cedric-clyburn|Cedric Clyburn]] / [[ibm|IBM Technology]] — 이름·소속은 **설명란에만**) — 1인 해설, 무챕터. **이 위키가 AI 엔지니어라는 직무의 정의를 받는 첫 소스.** *연구원은 엔진, 엔지니어는 자동차*([[ai-engineer-vs-ml-researcher]]) · *어려운 건 코드가 아니라 판단, 만들어 보며 배운다* · 세 층(기초 → AI 특화 → 배포)과 **순서**([[three-tier-ai-skill-stack]]) · *"Python 마법사가 아니라 에이전트가 쓴 것을 읽을 만큼"*([[read-fluency-for-agent-output]]) · [[workflow-vs-agent]] · [[retrieval-augmented-generation|RAG]] 파이프라인 첫 서술(청킹 → 임베딩 → 저장 → 검색 → 컨텍스트 창) · 관측 가능성을 [[agent-action-record]]에. 기존 보강: [[taste-vs-judgment]](진입 전의 목소리) · [[cognitive-offloading]](읽기는 남긴다) · [[ibm]](세 번째 소스).
- [[tech-bridge-dario-amodei-cbs-interview]] (23:47, [[dario-amodei|Dario Amodei]] / [[anthropic|Anthropic]] CEO, CBS Sunday Morning — 진행자 무명) — 방송 인터뷰, 무챕터. **위키 첫 Anthropic CEO 1인칭 소스.** *확률 대신 건설 방식* · *지수의 굽이, 나도 몰랐다* · **멈추지 말고 늦추자** · 3단계 계획([[embedded-external-evaluators]] → 업계 합의 → 정부 참여) · SB53 유일 지지 · 전면 금지 반대 · [[race-to-the-top]] · [[swiss-cheese-defense-in-depth]] · [[slowdown-within-lead-margin]] · [[ai-arms-limitation-lens]] · [[joint-democratic-oversight]] · *"업계가 거짓말했다"*. 기존 보강: [[anthropic]](CEO 1인칭 첫 절) · [[hugging-face]](네 번째 서술, 경쟁 랩 CEO의 첫 서술) · [[openai]] · [[sam-altman]] · [[elon-musk]] · [[bill-gates]] · [[regulatory-capture]](여섯 번째 칸 — **규제 대상이 규제를 요구하는 첫 칸**, Ng와 정면 충돌) · [[training-time-risk]](일방 vs 다자) · [[one-continuous-exponential]](같은 곡선, 반대 결론) · [[balance-of-power-safety]](같은 공포, 반대 처방).

**이날의 구도** — 이 채널에서 **가장 낮은 층(입문)과 가장 높은 층(CEO의 정책)** 이 같은 날 들어왔고, 둘 다 이 위키에 **처음인 것**을 하나씩 준다: 직무의 정의와 Anthropic 쪽의 목소리. Amodei 편이 이 위키의 안전·규제 축에 준 것이 크다 — [[regulatory-capture]] 표가 여섯 칸이 되면서 처음으로 *규제를 원하는 규제 대상* 이 생겼고, [[verification-bottleneck|검증 병목]]이 처음으로 *제거할 대상* 이 아니라 *의도한 제어 장치* 로 놓였으며([[embedded-external-evaluators]]), 그동안 따로 들어온 안전 장치들이 처음으로 한 스택의 이름을 얻었다([[swiss-cheese-defense-in-depth]]).

**새 주의사항 여덟**: ① **ko가 사건 하나를 지어냈다** — *"the OpenAI Hugging Face incident"* → **"오픈 AI가 얼굴 사진을 합성하는 사건"**. 09-06 [[hugging-face]]의 *"얼굴 껴안기"* 직역의 **재발이자 악화** — 이번엔 문장이 자연스러워 ko만 읽으면 OpenAI가 얼굴 합성 사고를 냈다고 읽힌다. **회사명 → 사건 내용.** ② **회사명이 한 영상에서 여섯 표기, 셋이 학문·물리 용어** — Anthropic → 앤트로픽·엔트로픽·**엔트로피**·**인류학 연구**·**인류학 연구소**·**인류학파**. 회사명이 학문 분야가 된 첫 사례. ③ **부호 뒤집기 세 번째, 세 번 다 결론 문장** — *"I won't lie that the stakes aren't high"* → **"중요성이 크지 않다는 건 부정할 수 없어요"**. ko 안에서 다음 문장과 모순. ④ **화자의 자기 정정을 ko가 붙여 사실관계를 뒤집었다** — *"업계가 반대했다 — 아니, 침묵했고 — Anthropic만 지지"* → **"엔트로픽은 아무 말도 하지 않았지만 열정적으로 지지한 유일한 회사"**. 09-13 *Gary Tan* 계열. ⑤ **핵심어가 한 번은 맞고 한 번은 틀린 유형이 두 편 모두에서** — *restraint* → "규제"/"절제", *retrieval augmented generation* → "증강 현실 생성"/"검색 증강 생성". → **같은 용어의 모든 출현을 대조할 것.** ⑥ **자막이 스스로 약속한 것을 안 지킨다 (첫 사례)** — Clyburn 편 도입부의 *"세 가지 프로젝트"* 가 끝까지 없다(en-orig도). 지금까지의 결손은 *제목·설명란이 자막에 없는 것을 주장* 이었는데 **이번엔 자막 안에서 예고와 본문이 어긋난다.** 편집인지 원본인지 미확정. ⑦ **✅ 제목·설명란이 성 표기를 고쳐 준 사례** — 양 트랙 *"Amade/아마데"* → 제목·설명란 *"아모데이"*. 메타데이터가 자막을 고치는 네 번째. ⑧ **진행자 무명 인터뷰가 처음** — 이 채널의 인터뷰 소스 중 진행자가 이름 없는 첫 경우(설명란도 매체만).

부수: en-orig 오인식의 ko 직역 연쇄 재발(*pay grade* → *prayer grade* → **"기도 능력"**, 같은 관용구가 다른 자리에서는 옳음; *Claude* → *clawed* → **"발톱"**; *the model too* → *model 2* → **"모델 2"**), ko가 잘린 말을 완결 문장으로 창작(**네 번째** — *"I've never— I know"* → "저는 그런 경험이 없어요"), *agent* → **"상담원"** 재발, *shipped* → **"물품을 배송"**, *defense in depth* → **"수비와 깊이"**, *get through the stack* → **"전부 다 먹는"**, *handing over* → **"정권 이양"**, *ChatGPT* → **"GPT 채팅"**, *models like frontier or open source* → 고유명사처럼 **"Frontier나 Open Source"**, 진행자 질문의 *"my aunt"* 가 ko에서 질문자로 뒤바뀜(인용 안 함).

**인명 처리**: *Jacob Coxin*(전 Anthropic 직원, ASR) · *Ted Leo*(하원의원, ASR) · 진행자 — **어느 표기도 채택하지 않고 페이지를 만들지 않았다.** *Sam Olman/샘 올먼* 은 위키 페이지가 있어 [[sam-altman]]으로 채택. Sanders/Casar는 양 트랙 일치. Cedric Clyburn은 **설명란 근거**로 채택하고 출처 표시(09-08 Thomas Wolf · 09-15 Vincent Wendy와 같은 처리).

**행사·촬영 시점**: Amodei 편 **연도 2026 확정**(화자: *"1년 전, 2025년"*) — 이 채널에서 연도가 화자 발화로 확정된 드문 경우. 날짜는 *"몇 시간 전 에세이"* · *"이틀 전 보고서"* · *"지난주 단백질 결합"* · *"곧 트럼프–시진핑 회담"* 까지이고 **에세이·보고서의 제목·날짜는 소스에 없다.** Clyburn 편 **미확정**(IBM 편 3회 연속). **업로드 날짜를 앵커로 쓰지 않았다.**

**해소하지 않고 표시만 한 것**: Amodei 편 — **에세이·보고서의 제목과 게시처**, **Musk·Altman의 동의**(진행자 서술), *"시뮬레이션에서 우회를 봤다"*(진행자 진술), *"주간 수억 명"*(자기 보고), **평가자의 독립성과 비용**(작성자=검증자 문제가 기관 층위에서), **"우위의 범위"의 크기**, **국방 응용의 범위**, **검증 방법의 실체**(핵·생물무기 사찰이 모델 훈련에 어떻게 대응하는지), Jacob Coxin·Ted Leo의 정체, 진행자·방송 날짜. Clyburn 편 — **약속된 세 가지 프로젝트의 부재**(편집/원본), **Red Hat과 IBM의 관계**(소스가 말하지 않음), *"거의 모든 회사가 RAG를 원한다"*·*"가장 수요가 많은 응용 AI 기술"*(근거 없음), *"in this three space"*(en-orig 불분명, 인용 안 함), 재랭킹·평가·청크 크기(파이프라인이 저장·검색까지), PyTorch·TensorFlow·Kubernetes·Linux(지나가는 언급, 페이지 없음).

**운영 메모**: 09-13·09-15에 기록한 대로 `--print` 출력을 **파일로 받았다.** 목록 조회 1분 내 완료. 두 편 모두 **무챕터**라 소제목은 정리자가 화자의 구획(Clyburn: 1·2·3단계 / Amodei: 진행자 질문)을 따라 붙이고 그 사실을 raw 헤더에 명시했다.

## [2026-09-17] ingest | Tech Bridge 2편 — AI 생성 코드의 보안 5원칙(Jeff Crume, IBM) · Zuckerberg Muse 두 번째 인터뷰

`--playlist-end 15`가 **15편** 반환, 전부 롱폼(최단 632초, Shorts 없음). 신규 **2편**(둘 다 2026-09-16 업로드), 나머지 13편은 기존. ko + en-orig 전부 확보, **429 없음**. yt-dlp 목록 조회 1분 내, 자막 두 편 합쳐 1분 내.

**신규 source 2 · concept 9 · entity 3, 기존 20페이지 보강. index 실측 470 → 484.**

- [[tech-bridge-shift-left-security-ai-code]] (11:18, [[jeff-crume|Jeff Crume]] 박사 / [[ibm|IBM]] — ⚠️ **이름은 설명란에만**) — 1인 해설, **무챕터**. **이 위키가 보안을 개발 공정의 축으로 묶어 보는 첫 소스.** 기존 보안 페이지는 에이전트 런타임([[prompt-injection]]·[[lethal-trifecta]]·[[confused-deputy-attack]])이나 제품 아키텍처([[confidential-vm]]·[[sentinel-agent]])에 있었고 **코드가 만들어지는 순간을 보는 페이지가 없었다.** [[shift-left-security|다섯 원칙]]: ① *결과를 믿어라, **생성**만이 아니라* — 컴파일·실행·테스트 통과가 곧 안전이 아니고 권한·유출·**실패 모드**(fail safe vs fail open)를 본다 · ② *보안은 개발 중에 시작된다* — *"사후 체크박스 모델은 **애초에 작동한 적이 없다**"* · ③ **[[generated-dependency-scrutiny]]** — *"AI는 코드만이 아니라 **의존성을 들여온다**. 모든 의존성은 능력을 더하고 위험도 더한다"*(**위키에 소프트웨어 공급망이 처음 들어온 자리**) · ④ *"코딩 문제라기보다 **의도 문제**"* — 미다스 왕, **잘못된 코딩이 아니라 잘못된 가정** · ⑤ **[[continuous-security-validation]]** — *"한 번 통과했는가가 아니라 **계속 통과하는가**"*. **⑤가 ②를 스스로 교정한다** — 시프트 레프트는 구간 이동이 아니라 **확장**이다. 맺음의 에이전트 통제 넷(가드레일·**신원**·접근 제어·사람 개입)이 [[agent-governance-layers]]·[[agent-identity-separation]]·[[least-privilege-connectors]]·[[sentinel-agent]]와 하나씩 맞물린다. 기존 보강: [[behavior-validated-trust]](**같은 벤더가 같은 원리를 두 번 말한 첫 사례** — 09-08 품질판의 보안판) · [[intent-alignment]](**리뷰어 층**이 붙는다) · [[ai-vulnerability-discovery]](27년 제로데이 — ⚠️ 출처 미상) · [[verification-bottleneck]] · [[agent-governance-layers]] · [[secure-tool-evolution]] · [[ibm]](네 번째 소스).
- [[tech-bridge-zuckerberg-muse-in-daily-use]] (25:09, [[mark-zuckerberg|Mark Zuckerberg]] / [[meta|Meta]] CEO × 진행자 무명 — 자막에 *"Tiff"* 한 번) — 인터뷰, **공식 챕터 22개**. **이 채널이 같은 인물의 같은 주제 인터뷰를 두 편 올린 첫 사례**이고, 사흘 전 ingest한 [[tech-bridge-zuckerberg-muse-personal-agent]](`DND22Bf88QI`, 65:19, [[alex-heath]] 진행)와 **별개의 자리**다(09-07 절차로 대조 — 같은 행사라는 근거 없음). ⚠️ **내용이 크게 겹친다** — 베이킹·등산 허가·MMA 카메라·문명 웹사이트·아이디어 탭·주당 1억 토큰·보안 네 겹·희귀 질환 롱테일이 **전부 앞 편에 있고 앞 편이 더 길고 더 자세하다.** **그래서 이 편의 값은 새 주제가 아니라 대조에 있다.** 앞 편에 없던 여섯: [[agent-persona-naming]](Agrippa/Pip) · [[one-time-virtual-card]] · [[muse-spark]](1.3) · [[business-in-a-box]] · [[biohub]]+[[rare-disease-long-tail]] · [[nightly-memory-consolidation]]. 기존 보강: [[muse]](두 번째 소스, 대조표) · [[mark-zuckerberg]] · [[meta]] · [[meta-superintelligence-labs]] · [[confidential-vm]] · [[sentinel-agent]] · [[least-privilege-connectors]] · [[transaction-cut-monetization]] · [[agent-memory]] · [[context-resets-and-compaction]] · [[personal-superintelligence]] · [[agent-org-adoption]] · [[goal-level-delegation]] · [[proactive-idea-feed]].

**이날의 구도 — 두 편이 검증에 정반대로 답한다.** Crume 편은 **검증을 늘리자**고 말한다(왼쪽으로, 그리고 전 구간으로, *"계속 통과하는가"*). Zuckerberg 편은 **능력을 말하고 검증을 말하지 않는다** — [[rare-disease-long-tail|개인 맞춤 치료]]에 임상·규제·책임이 한 마디도 없고, 앞 편에 있던 [[confidential-vm|기밀 VM]]의 *"기술적으로 검증 가능하다"* 조차 이번 편에서는 *"업계에서 견줄 데 없다"* 라는 **비교 주장으로 바뀌었다.** 전날 들어온 [[embedded-external-evaluators]](평가자 처리량을 기술의 제한 속도로)와 나란히 놓으면 **세 입장이 한 축에 선다** — 평가자를 제도로 세우자(Amodei) · 검증을 공정에 심자(Crume) · **검증을 말하지 않는다**(Zuckerberg).

그리고 Muse 편의 가장 날카로운 문장은 보안 쪽에 있다 — *"나도 가상 카드를 만들까 하다가 **귀찮아서** 그냥 평소 카드를 쓴다. **에이전트는 그 추가 수고를 마다하지 않는다**"*([[one-time-virtual-card]]). **보안 기능의 채택을 막는 것이 기술이 아니라 마찰이었다면, 에이전트는 그 마찰을 치른다.** ⚠️ 뒤집으면 같은 명제가 위험이기도 하다(에이전트는 **위험한 절차도** 마다하지 않는다) — 소스는 그 방향을 말하지 않는다.

**새 주의사항 여섯**: ① **ko가 ASR의 비언어 태그를 단어로 번역했다 (첫 사례).** en-orig 자막이 화자가 *Muse* 라고 말한 두 자리(00:31·00:38)에 **음향 태그 `[music]` 을 박아 넣었고 ko가 그 태그를 번역했다** → *"**음악**을 통해 소위 '박스형 비즈니스'"* · *"결국 **음악 건강**은 아주 개인적"*. 지금까지의 ko 오류는 전부 단어·구·문장의 오역이거나 소실이었는데 **이번엔 자막 형식 요소를 본문으로 읽었다.** ② **같은 제품명이 한 영상에서 세 갈래로** — *Muse* → **음악** · **뉴스**(*my news* 직역) · **MU 시스템**. 대부분의 자리에서는 옳아서 09-16 주의사항 ⑤(같은 용어의 모든 출현을 대조하라)의 **네 번째 확인**이다. ③ **사람 이름이 인사 제도로 읽힌 첫 사례** — 진행자의 에이전트 이름 *Pip* → **"저는 **PIP 프로그램 대상자**인데 계속 참여해야 할지"**. 문장 전체가 바뀌었고, 12:08의 *"my muse pip"* 로 판독했다. *a grippa*(**Agrippa**)도 *"그리파"* 로 남아 바로 뒤의 *"로마 장군"* 으로 판독했다. ④ **원칙 이름이 한 번만 나오고 그 한 번이 틀렸다** — *"Trust the outcome, **not just the generation**"* → **"**세대**만이 아니라 결과를 믿으세요"**. **대조할 두 번째 출현이 없는** 첫 사례(09-16 유형은 같은 용어가 두 번 나와 한 번은 맞았다). ⑤ **ko가 관용구의 방향을 뒤집었다** — *"hiding **in plain sight** for 27 years"* → **"눈에 띄지 않게 숨겨져 있던"**. 부호 뒤집기(09-07·09-13·09-16)와 다른 유형으로, **훤히 보였는데도 못 봤다**는 그 문장의 논점 자체가 사라진다. ⑥ **한 용어의 세 표기를 챕터 제목으로 통일했다** — *business in a box* → *"박스형 비즈니스"*·**"비즈니스 인 어 박스"**(챕터)·*"비즈니스 패키지"*. 09-15에 세운 *"챕터 제목도 양방향 대조 대상"* 원칙의 **두 번째 적용**.

부수: en-orig 오인식의 ko 직역 연쇄 재발(*game changer*→*"gamecher"*→**"AI는 게이머입니다"**; *pen testing*→*"pin testing"*→**"동적 PIN 테스트"** — ko에서 항목이 하나 늘었다; *summiting*→*"summoning"*→**"산을 소환하는 것"**; *long tail*→*"long tale"*→**"이야기가 매우 길다"**; *write access*→*"right access"*), **명사가 바뀌어 보안 설명이 망가진 곳**(*the merchant will never see my real **number*** → **"제 실제 전화번호"** — 절의 요점이 카드 번호인데), *measures*(대책)→**"측정 기준"**, *under the covers*→**"이불 속에서 은밀하게"**, *agent*→**"요원"**(09-16 *"상담원"* 에 이어, 이번엔 첩보원), *compact*(동사)→**"콤팩트한"**, *"right? Right?"*→**"그렇죠? 오른쪽?"**, **부분 부정이 전면 부정으로**(*"haven't always practiced"*→*"제대로 실천해 온 적은 없습니다"*), 딸 이름 **두 표기**(오렐리아/아우렐리아 → *Aurelia* 로 통일).

**인명 처리**: [[jeff-crume|Jeff Crume]]은 **설명란 근거**로 채택하고 출처 표시(09-15 Vincent Wendy · 09-16 Cedric Clyburn과 같은 처리, **세 번 연속**). **Agrippa·Pip**은 소스 내부 근거(*"로마 장군"* · *"my muse pip"*)로 판독해 채택. **진행자 *"Tiff"* 는 채택하지 않았다** — 에이전트 알림 문구의 재현이 유일한 근거이고 성·소속·매체가 없다(09-16 진행자 무명과 같은 처리이되 **이름의 일부가 남은 첫 경우**). **Priscilla**([[biohub]] 공동 설립)는 **성이 소스에 없어 페이지를 만들지 않았다**(09-13 *Gary Tan* · 09-16 *Jacob Coxin* 계열). **Aurelia**는 화자의 세 살 딸로, en-orig 표기를 따르되 인물 페이지는 만들지 않았다.

**행사·촬영 시점**: 두 편 다 **미확정**. Crume 편은 [[ibm]] 편 **4회 연속** 미확정이고 유일한 시간 표현이 *"40년 전 제 경력 초기"*(개인 앵커)와 *"최근 …제로데이"*(출처 미상)뿐이다. Zuckerberg 편의 앵커는 전부 상대적(*"거의 정확히 2년 전 Meta Connect"* · *"MSL 시작 이래 한 1년쯤"* · *"최근 WSJ 기고"* · *"방금 Muse Spark 1.3 출하"*)이라 **연도를 확정할 수 없고, 앞 편과의 선후도 판정할 수 없다.** **업로드 날짜를 앵커로 쓰지 않았다.**

**해소하지 않고 표시만 한 것**: Crume 편 — **27년 제로데이의 모델·OS·출처**(하나뿐인 수치인데 셋 다 없다), **도구 이름 0개**(정적 분석·비밀키 스캔·의존성 모니터링을 무엇으로 하는지, IBM 제품도 포함해 하나도 없다), *"일찍 찾으면 싸다"* 의 수치 근거(*"역사가 가르쳐 준다"* 로만), *"복잡성은 보안의 적"* 의 근거(격언), **③④의 번호가 설명란에만**(자막 불일치), 다섯 원칙의 **수행 주체**(개발자/보안팀/에이전트를 나누지 않는다), *"shift left security **improves** validation into…"*(en-orig ASR 불분명 — **인용하지 않았다**), **AI가 AI 코드를 검증하는 구성의 독립성**(09-09 이래 반복되는 작성자=검증자 문제가 또 열린 채). Zuckerberg 편 — **진행자의 성·소속·매체**, **촬영 시점과 앞 편과의 선후**, **Priscilla의 성**과 [[biohub]]의 규모·시점·자금, **WSJ 기고문의 제목·날짜**(두 편 모두 없다), **[[confidential-vm|기밀 VM]]의 검증 방법**(앞 편의 *"기술적으로 검증 가능"* 이 사라지고 근거 없는 비교 주장만), **센티널의 탐지율·오탐·인젝션 내성**(이번 편은 인젝션을 **언급조차 않는다**), **일회용 카드의 발급 주체·한도·환불·분쟁**과 앞 편의 **Stripe**와의 관계, **메모리 압축이 버리는 것**·가시성·되돌리기·*"무관한 것"* 판정의 검증, **[[muse-spark|Muse Spark]]의 버전 체계·이전 버전·평가 결과**, **아이디어 피드의 수락률·오제안**과 중복 구독 해지의 오탐, **[[business-in-a-box]]의 광고 이해관계**(화자가 연결하지 않는다)·작동 사례 0건·법인/세무/규제/책임, **개인 맞춤 치료의 검증·임상·규제·책임**, **베타의 규모·기간·선정 방식**(두 편 모두), **두 편 합쳐 실패·오작동 사례 0건**.

**운영 메모**: 09-13·09-15에 기록한 대로 `--print` 출력을 **파일로 받았다.** Crume 편은 무챕터라 소제목을 **정리자가 다섯 원칙 구획을 따라** 붙이고 그 사실과 **③④가 설명란 근거임**을 raw 헤더에 명시했다. Zuckerberg 편은 **공식 챕터 22개**를 따랐다(묶은 곳은 표시).

## [2026-09-18] ingest | Tech Bridge 2편 — 레거시 코드와 AI 현대화(Anna Gutowska, IBM) · 토큰에게 역할을 주라(Katelyn Lesse & Angela Jiang, Anthropic, AI Engineer)

`--playlist-end 15`가 **15편** 반환, 전부 롱폼(최단 531초, Shorts 없음). 신규 **2편**(둘 다 2026-09-17 업로드), 나머지 13편은 기존. ko + en-orig 전부 확보, **429 없음**(en과 en-orig는 바이트 단위로 동일). yt-dlp 목록 조회 1분 내(경고: 브라우저 쿠키 만료 · 버전 90일 초과 — 재시도 없이 통과), 자막 두 편 합쳐 1분 내.

**신규 source 2 · concept 8 · entity 1, 기존 17페이지 보강. index 실측 484 → 495.**

- [[tech-bridge-legacy-code-modernization-ai]] (8:51, [[anna-gutowska|Anna Gutowska]] / [[ibm|IBM]] — ⚠️ **이름은 설명란에만**) — 1인 해설, **무챕터**. **이 위키가 레거시 코드의 정의와 현대화의 구조를 받는 첫 소스.** 기존 레거시 논의는 [[tech-bridge-cursor-legacy-refactoring]](도구 시연)과 [[greenfield-vs-brownfield-agent-risk]](위험 뒤집기)뿐이었다. [[legacy-code-modernization]]: 레거시 = *여전히 돌아가지만 아무도 완전히 이해하지 못하는 핵심 인프라*(옛 언어·지원 끊긴 인프라·**테스트 없음·문서 없음**) · 악화 추세 셋(**[[legacy-skills-gap|개발자 수 ≠ 현대화 속도]]** — COBOL 세대 은퇴 / 생산성 / **부채 → 보안 위험**) · 옛 플레이북(몇 달 읽고 하나씩 손으로) · AI의 두 자리(**발견** 몇 달→몇 주 · **번역** COBOL→Java) + 에이전트(분석→계획→번역→테스트→문서화) · 현대화 ≠ 번역, **세 축**(아키텍처·기술·프로세스)의 점진적 과정 · 한계 셋(얽힌 로직 · **[[syntactically-correct-behaviorally-wrong|문법은 맞고 동작은 틀린 번역]]** · 취약점 자동 제거 기대 금지) · 처방 **[[risk-proportional-human-review|AI는 승수, 사람은 가장 위험한 결정 곁에]]**. 기존 보강: [[technical-debt]](**보안 이자·인력 이자**) · [[greenfield-vs-brownfield-agent-risk]](*"잘 세팅돼 있다면"* 의 **반대편** — 모순이 아니라 같은 변수의 양 끝) · [[behavior-validated-trust]](**같은 벤더의 세 번째 진술** — 품질·보안·마이그레이션, 이번엔 *옳은가* 가 아니라 *원본과 같은가*) · [[shift-left-security]](원칙 ①의 하루 뒤 반복) · [[tech-bridge-cursor-legacy-refactoring]](세 번째 각도) · [[ibm]](다섯 번째 소스).
- [[tech-bridge-tokens-should-have-jobs]] (12:45, [[katelyn-lesse|Katelyn Lesse]]·[[angela-jiang|Angela Jiang]] / [[anthropic|Anthropic]] · [[ai-engineer|AI Engineer]]) — 2인 무대 발표, **공식 챕터 8개**. **09-01 [[tech-bridge-claude-platform-agent-era]]와 같은 두 화자의 재방문** — 09-17 절차(기존 raw 대조)를 두 번째로 적용. 그때 말로만 있던 [[token-roles]] 세 전략에 **처음으로 수치**: one-shot 실행 **15%/39k**(전략이 지출을 스스로 정함), 회고 **600k** → **[[fixed-budget-alpha]]**(예산 60만 고정: 실행 76 vs 조언 89 — *"테스트 타임 컴퓨트가 전부라면 넷이 같아야"*) → **[[all-or-nothing-accuracy]]**(P&L에서 80%는 *전문가가 다시 계산해야 하므로* 쓸모없다 → 100%만 합격: 42% vs 최대 75%) → **[[true-cost-to-perfect-answer]]**(예산 × 기대 횟수 = 600k×3 = **180만**; 효율 → 조언 / 신뢰성 → 채점·회고) → **[[strategy-primitives]]**(하네스 위 **메타 하네스** 층, **회고·`outcomes` 기본 제공**, 실행→조언→채점→회고 한 루프, *"새 역할을 발명"*, 장기 목표 **동적 전략 구성**). 기존 보강: [[token-roles]](수치 절 + **09-01의 Sonnet+Opus 비용 역전이 되풀이되지 않음**) · [[katelyn-lesse]]·[[angela-jiang]](직함 확정 — 플랫폼 엔지니어링 리드 / 플랫폼 제품 리드) · [[managed-agents]](층 구조) · [[anthropic]] · [[ai-engineer]](행사명을 화자가 말한 두 번째 소스) · [[generator-evaluator-pattern]](grading의 첫 합격률 + *신뢰성 최적화의 처방*) · [[verification-cost-asymmetry]](**같은 결론을 판매자가 채점 방식으로**) · [[agent-memory]](쓰는 주체가 실행자와 **분리**된 첫 서술 — 드리머) · [[self-harness]](dreaming이 루프의 마지막 칸) · [[tech-bridge-claude-platform-agent-era]](재방문 절).

**이날의 구도 — 정의가 들어온 편과 수치가 들어온 편.** IBM 편은 정의를 주고 수치가 없다. Anthropic 편은 수치를 주고 정의는 이미 있었다. 그리고 두 편이 **검증**에서 만난다 — IBM 편은 *동작이 틀린 번역* 을 잡을 기준이 레거시에는 없다고 말하고(그래서 사람을 위험한 결정 곁에), Anthropic 편은 *100%가 아니면 실패* 라는 기준이 있는 작업(P&L)에서 채점자를 프리미티브로 판다. [[verification-cost-asymmetry]]의 축으로 읽으면 **한쪽은 수용 기준이 없는 작업, 다른 쪽은 완전히 확정된 작업**이다. 그리고 두 편 다 **작성자=검증자 문제를 열어 둔 채**다 — IBM 편은 사람 검토로, Anthropic 편은 채점자로 메우지만 **채점자의 독립성은 판매자 발표에서도 말하지 않는다**(09-09 이래 네 번째).

**같은 벤더의 반복 셋** — [[ibm]]이 [[behavior-validated-trust]]를 **세 번째**(품질 → 보안 → 마이그레이션), [[shift-left-security]] ①을 **하루 뒤** 되풀이했고, [[anthropic]] 플랫폼 팀은 [[token-roles]]를 **두 번째** 말하되 **가장 강한 주장(Sonnet+Opus < Sonnet)은 빼고** 말했다. → **재방문 소스에서는 "무엇이 사라졌는가"를 대조표에 반드시 둔다** — 09-17 Zuckerberg 편에서 세운 원칙의 두 번째 적용이고, 이번엔 사라진 것이 *가장 강한 주장* 이었다.

**새 주의사항 일곱**: ① **ko가 발표의 핵심 명사를 상속법 용어로 옮겼다** — *executor* → **"유언집행자"**(6회)·"집행자"·"실행기"·"실행자", **한 영상에 네 표기**이고 하나가 다른 분야의 전문 용어다. 문장이 자연스러워 ko만 읽으면 뜻이 통하지 않는다(09-16 *"인류학파"* 계열). ② **ko가 토큰 예산에 통화 단위를 붙였다** — *"600,000 or so"* → **"약 60만 달러"**. 원문에 단위가 없는 자리에 없던 단위(09-08 *"1조 달러"* 계열). 같은 수치가 세 다른 자리에서는 *"60만 개의 토큰"* 으로 옳다 — **같은 수치의 네 출현 중 하나만, 그것도 고정 예산을 선언하는 문장에서** 틀렸다. ③ **전략 이름 셋이 일상어로 흩어졌고 챕터가 고쳐 줬다** — *grading* → "성적 평가"·"성적", *dreaming* → "꿈"·"몽상가"·**"Drain"**(ASR 그대로). **채널 챕터 "조언(Advising), 평가(Grading), 회고(Dreaming)"를 채택** — 09-15 원칙(챕터 제목도 대조)의 세 번째 적용. ④ **제품 기능명이 보통명사가 됐다** — *"dreaming and **outcomes**"* → **"꿈과 결과"**. `outcomes`는 [[managed-agents]]의 기능명(09-01 확인)이라 ko로는 무엇이 기본 제공인지 알 수 없다. ⑤ **같은 화자·같은 ASR 오류·다른 ko 결과** — en-orig *greater*(→ grader)를 09-01 ko는 *채점자* 로 옳게, 이번 ko는 **"더 상위 단계로 보내"** 로 틀리게 읽었다. **채널의 ko 품질이 영상마다 다르다는 첫 직접 증거.** ⑥ **ko가 `architecture`를 건물로** — IBM 편 세 축의 첫 축 이름표 *"우선 **건축**부터"*, 같은 단어가 02:34에서는 *"메인프레임 아키텍처"* 로 옳다(09-17 *generation → 세대* 유형 — **이름표 자리에서만 틀림**). ⑦ **✅ ko가 ASR 오류를 문맥으로 고쳐 읽은 드문 경우** — IBM 편 *"identifying or **mediating**"* → ko *"식별하거나 **해결하는**"*. 기록된 사례는 거의 전부 ko가 ASR을 직역한 것이었다.

부수: *jobs* → **"일자리"·"직업"·"작업"** 세 갈래(**채널 제목이 "역할"로 고쳐 줌**), *Claude Managed Agents* → **"클라우드 관리형 에이전트"**(3회, 설명란으로 판독), *force multiplier* → **"시너지 효과"**(처방의 구도가 흐려짐), *test-time compute* → **"테스트에 더 많은 컴퓨팅 자원"**, *harness* → **"시스템"**, *trivial* 한 번은 맞고 한 번은 **"사소한 일"**(09-16 ⑤의 다섯 번째), *executing* → **"작전을 수행"**, *individual agents* → **"개별 요원들"**(**세 번 연속**), *customer service agent* → *"담당자"*, *alpha* → *"알파 수익률"*, *advised type* → *"전략 유형"*(**조언 소실** — 처방의 절반), *vulnerability surface grows* → *"취약점은 더욱 드러납니다"*, *more thorough* → *"더 완벽하게"*, *skills gap* → *"기술 격차"*(중의), 화자의 자기 단위 혼용 *"0.15에서 76으로"*(그대로 인용하고 표시).

**인명 처리**: [[anna-gutowska|Anna Gutowska]]는 **설명란 근거**로 채택하고 출처 표시(IBM 편 세 번 연속 · 채널 네 번 연속 — 09-15 Vincent Wendy · 09-16 Clyburn · 09-17 Crume). [[katelyn-lesse]]·[[angela-jiang]]은 자막이 자기소개하되 철자는 **설명란의 *Katelyn Lesse* 를 채택**(en-orig *Caitlyn/Caitlin* · ko *케이틀린* — 09-01과 같은 처리). **발언별 화자 특정은 부분적** — `>>` 표지 두 개뿐, *"케이틀린이 언급했듯이"* 로 역산해 벤치는 Katelyn·렌즈/비용/아키텍처는 Angela로 읽히나 **raw 인용에는 화자를 붙이지 않았다**(09-05 Claude Code 팀 편과 같은 처리). **Fable**(11:33)은 양 트랙 불분명 — 무엇을 가리키는지 판독하지 않았고 [[claude-mythos-preview]]의 *"Mythos·Fable 사태"* 와 **연결하지 않았다.**

**행사·촬영 시점**: IBM 편 **미확정, 다섯 번째 연속** — 이번엔 개인 앵커조차 없다. Anthropic 편 **행사명 AI Engineer 확정**(화자 발화 *"AI Engineer에서"*), 회차·연도 미확정 — 09-07 절차대로 [[ai-engineer]] 페이지의 다른 소스들([[tech-bridge-one-designer-plus-ai]] · [[tech-bridge-mousepower-measuring-agents|World's Fair]])과 대조했으나 **같은 회차라는 근거 없음, 별개 취급**. *"Fable이 다시 온라인"* 을 시점 앵커로 쓰지 않았다. **업로드 날짜를 앵커로 쓰지 않았다.**

**해소하지 않고 표시만 한 것**: IBM 편 — **화자 이름·직함의 근거**(설명란뿐), **촬영 시점**, *몇 달 → 몇 주*·*시간의 절반* 의 근거, **도구·제품·모델 이름 0개**, *"의도는 유지된다"*(04:56) ↔ *"동작이 틀린 번역"*(07:51)의 긴장(화자 미해소), **세 축의 순서·의존**, *"가장 큰 위험을 수반하는 결정"* 의 예시, *"최소한의 사람 개입"* ↔ *"사람 검토를 전 구간에"* 의 관계, 콜드 오픈 사고가 가상임(*"상상해 보세요"*). Anthropic 편 — **벤치의 실체**(과제 수·모델·평가자·반복·분산), **채점·회고의 고정 예산 점수·합격률·진짜 비용**(자막에 없음, 차트에만), *"최대 75%"* 가 어느 전략인지, **고정 예산 60만의 편향**(가장 많이 쓴 전략에 맞춤), 알파의 통계적 의미(화자 *"미미하다"*), **Fable 문장**, **09-01의 비용 역전 주장이 왜 사라졌는지**, 행사 회차, 발언별 화자, 동적 전략 구성의 실체(선언뿐), **채점자의 독립성**(루브릭은 누가 쓰나, 같은 모델인가 — 판매자 발표에서도 열린 채), 재시도 독립 가정·검증 비용·예산 내 역할 배분(진짜 비용 식에 없음), 회고 사용 사례(채용)의 피드백 데이터 출처.

**운영 메모**: 09-13·09-15·09-17에 기록한 대로 `--print` 출력을 **파일로 받았다.** yt-dlp가 *"YouTube account cookies are no longer valid"* 경고를 냈으나 목록·자막 모두 정상 반환 — **재발 시 429로 이어질 수 있어 감시**. en과 en-orig가 동일 파일(둘 다 자동 생성). IBM 편은 무챕터라 소제목을 정리자가 화자의 구획(정의 → 위치 → 추세 → 옛 플레이북 → AI 자리 → 에이전트 → 세 축 → 한계 → 처방)을 따라 붙이고 raw 헤더에 명시했다. Anthropic 편은 **공식 챕터 8개**를 따랐다. **재방문 절차 두 번째 적용** — 09-01 raw의 21:20 절을 grep해 겹침·추가·소실을 소스 페이지 대조표로 뒀다.

## [2026-09-19] ingest | Tech Bridge — Vercel의 파일 시스템 에이전트 · Plivo의 보이스 에이전트 실패 모드 (09-18 업로드 2편)

[[tech-bridge|Tech Bridge]] 최근 업로드 15편 중 **신규 2편**(둘 다 2026-09-18 업로드), 나머지 13편은 이미 ingest돼 있었다. 전부 롱폼(최단 531초, Shorts 없음). ko·en-orig **429 없이 전부 확보.**

**신규 source 2 · concept 14 · entity 7, 기존 15페이지 보강. index 실측 495 → 518.**

- [[tech-bridge-vercel-eve-filesystem-agent]] (17:06, [[andrew-qu|Andrew Qu]] / [[vercel|Vercel]] — ⚠️ **성은 설명란에만**) — 1인 컨퍼런스 발표, **공식 챕터 10개**. **위키 첫 Vercel 소스**이고 구조가 특이하다 — **앞 2/3이 자기 실패의 연대기**, 뒤 1/3이 제품 발표. [[agent-architecture-progression]]: 메가 프롬프트(사람이 SQL 복사·실행) → 역할별 체인(쿼리·계획·실행·보고) → 단일 상태 에이전트(최대 100스텝) → **[[file-system-agent|파일 시스템]]**. **이 위키가 [[workflow-vs-agent]] 축을 실제로 건너간 첫 기록**이고 **건너간 이유가 조율이 아니라 컨텍스트 손실**(*"다음 에이전트가 요약과 조각만 받는다"*)이다. v3의 벽은 점수가 아니라 **분포** — eval 30%인데 첫 배포 반응이 *"끔찍하다"*, 그리고 *시나리오를 손으로 더 까는 것* 을 스스로 확장 불가라고 판정했다. 돌파구가 **남의 제품**이다: *"[[claude-code|Claude Code]]와 [[claude-opus-4-5|Opus 4.5]]는 우리 것에 비하면 거의 AGI"* → [[file-system-agent]](최소 도구 list·read·bash + 샌드박스에 부은 시맨틱 레이어 + *"구체적인 도구 세트를 주지 않고 탐색하게 둔 것"*, 결과 *"eval 두 배"*). 이어 [[query-to-skill-distillation]](하루 수천 건 질의 → 주기적 잡이 스킬로 압축, 현재 약 100개) · [[framework-defined-agent-infrastructure]]([[eve-framework|Eve]] = *"에이전트를 위한 [[nextjs|Next.js]]"*, `skills/`·`tools/`·`channels/` 컨벤션 + 런타임 네 요구) · [[company-knowledge-moat]](기성 수직 에이전트를 테스트한 뒤 *"진짜 차이는 회사 고유 지식"*). 기존 보강: [[claude-code]](**위키가 받은 가장 구체적인 제3자 증언**) · [[claude-opus-4-5]] · [[workflow-vs-agent]] · [[agent-tool-design-practices]](**반대 각도** — 층이 다름) · [[agent-knowledge-sourcing]](**다섯 번째 갈래**) · [[agent-skills]] · [[skill-self-improvement]](**거울상**) · [[company-brain]](**서로를 모른 채 같은 결론**) · [[skill-evals]] · [[context-engineering]].
- [[tech-bridge-voice-agent-failure-modes]] (26:18, [[venky-b|Venky B]] / [[plivo|Plivo]] — ⚠️ **이름 표기 세 갈래, 성 철자 미확정**) — 1인 컨퍼런스 발표, **공식 챕터 15개**. **이 위키에 음성 에이전트라는 층이 처음 선 소스.** [[voice-agent-pipeline]](STT → LLM → TTS + 턴 감지) 아래 다섯 실패 모드: ① **[[time-to-first-audio]]**(광고 550ms / 실제 750~1200 / **1.2초 넘으면 끊는다**; 프런티어 P50 450~500ms인데 **P90·P95가 1.2~1.3초** — 평균이 아니라 꼬리가 제품을 정한다; [[cerebras]]·[[groq]]는 전용 용량·**12개월 선예약**) → **[[voice-latency-thinking-tradeoff]]**(*"지난 1년 LLM 발전의 대부분이 thinking인데 음성은 그걸 꺼야 한다"*) → [[token-fertility]](다국어면 [[gemma-4|Gemma 4]]가 [[qwen3-5|Qwen 3.5]]보다 2.5~3배; MoE 3~4B는 파인튜닝이 어려워 튜닝할 거면 8B~12B) ② **[[transcription-brittleness]]**(SOTA WER 4~6% vs 실전 두 자릿수; 고유명사·숫자·**코드 스위칭**) → [[dynamic-keyword-boosting]](*"다 넣으면 엔진이 환각한다"*) ③ **[[typed-field-collection]]**(*"전사를 해석하게 하지 말고 묻기 전에 모양을 정하라"*, 30% → 95%) ④ **[[field-level-unit-test-evals]]**(*"한 필드가 깨진 걸 알려고 E2E를 수백 건 돌리지 않는다"*) ⑤ **[[tts-normalization-layer]]**(이모지·마크다운 제거 · 커스텀 발음 사전 · **0.8~0.7배속** · 논거는 품질이 아니라 **교체 가능성**). 기존 보강: [[model-mixing-economics]](**세 번째 분할 축** — 대화 vs 도구 호출, 기준이 예산이 아니라 **지연**) · [[bound-parameters]](**같은 기법이 다른 이유로** — 보안 아닌 정확도) · [[skill-evals]](**해상도의 축**) · [[all-or-nothing-accuracy]] · [[context-engineering]](**LLM 바깥에서 재현**) · [[fuzzy-intent-discovery]](**반대 각도**) · [[cerebras]](조달의 벽) · [[gemma-4]]·[[qwen3-5]](음성 도메인에서의 선택 근거).

**이날의 구도 — 같은 날, 다른 층.** Vercel 편은 **LLM 위**(도구·컨텍스트·프레임워크)를, Plivo 편은 **LLM 아래와 밖**(전사·필드·정규화·지연)을 말한다. Plivo 편의 다섯 실패 모드 중 **넷이 LLM 바깥인 이유가 소스 안에 있다** — 실시간 제약이 thinking을 금지하므로 **모델을 더 생각하게 만들 수 없고 주변을 고칠 수밖에 없다.** 이것이 이 위키의 전제 하나를 드러냈다: [[fixed-budget-alpha]]·[[true-cost-to-perfect-answer]]·[[token-roles]]·[[generator-evaluator-pattern]]이 전부 *테스트 타임 컴퓨트를 더 쓸 수 있다* 를 깔고 있었는데, **그 레버가 금지되는 도메인이 생겼다.** → 기법을 옮길 때 물어야 할 것이 하나 늘었다: **이 기법은 몇 초를 쓰는가, 그 도메인은 몇 초를 허용하는가.**

**세 태도로 정리된 컨텍스트 조달.** 두 소스를 겹치면 — **고른다**([[context-engineering]]·[[dynamic-keyword-boosting]]) / **쪼갠다**([[typed-field-collection]]·[[field-level-unit-test-evals]]) / **펼쳐 놓고 찾게 한다**([[file-system-agent]]). 셋 다 같은 문제(무엇을 모델 앞에 둘 것인가)의 답이고 서로를 모른다.

**같은 기법이 독립적으로 두 번 도출된 사례 둘.** ① [[bound-parameters]] — 09-11 [[google-cloud|Google Cloud]]는 **보안**(에이전트가 신원을 지어내지 못하게), Plivo는 **정확도**(전사 오류를 즉시 판정). ② [[context-engineering]] — LLM에서 세운 *다 넣으면 나빠진다* 가 **STT 키워드 부스팅**에서 재발견됐다(*"너무 많이 넣으면 엔진이 환각한다"*).

**⚠️ 양쪽 다 벤치·eval의 실체가 없다.** Vercel은 *30%* 와 *두 배*, Plivo는 *30%→95%*(뒤에서 *95~97%*)·*4~6% WER*·*token fertility 2.5~3배* 를 말하면서 **과제·채점자·데이터셋·표본을 한 번도 밝히지 않는다.** ⚠️ **Vercel 편은 보안·권한을 한 번도 다루지 않는다** — 시맨틱 레이어 전체를 샌드박스에 붓고 bash를 주는 구조인데 [[prompt-injection]]·[[lethal-trifecta]]·[[agent-identity-separation]]이 통째로 비어 있다. ⚠️ **Plivo 편은 비용을 한 번도 계산하지 않는다** — *비용·지능·지연* 삼각형을 내세우면서 자체 GPU 호스팅이 프런티어 API 대비 얼마인지 없다. ⚠️ **챕터 제목만 있고 내용이 없는 절이 나왔다** — Plivo 편의 턴 감지·barge-in은 시간 초과로 슬라이드만 띄우고 넘어간다. **위키는 그 두 주제로 페이지를 만들지 않았다.**

**새 주의사항 일곱**: ① **영상의 주제어가 통째로 바뀐 첫 사례** — en-orig가 *voice* 를 **"wise"** 로 반복 오인식했고 ko가 뜻을 따라 **"똑똑한/스마트 에이전트"** 로 옮겼다. 지금까지의 ko 오류 기록은 단어·문장 단위였는데 **이번엔 영상 전체의 주제어**다. 채널 제목·챕터·설명란은 옳다. ② **단위 오류가 한 영상에 세 번, 방향이 제각각** — *"under 550"* → **"550달러"**(ms→통화), *"450 to 500"* → **"450~500초"**(ms→초, **같은 문단의 "1.2~1.3초"와 자기모순**), *"a three billion model"* → **"30억 달러 규모"**(파라미터→통화). 09-18의 *60만 → "60만 달러"* 가 **이틀 만에, 그것도 세 번** 재발. ③ **소수점 소실로 뜻이 뒤집힘** — *"at point 8x or 7x"* → **"8배율이나 7배율"**. 문장의 요지가 *천천히* 인데 정반대가 됐다(09-07 부호 뒤집기 계열). **설명란이 "0.7~0.8x"로 교차 확인.** ④ **같은 약어의 창작된 확장이 한 영상에 네 가지** — LLM → *Learning Leadership Model* · *로봇 학습 관리자* · **법학 석사** · *LLM 학위*. en-orig는 어디서도 풀지 않는다. 09-04·09-10·09-18에 이은 네 번째 유형인데 **한 영상에 네 가지는 처음**이고, 같은 자리에서 *transcript* 도 **"성적 증명서"** 가 됐다 — **문장 단위 도메인 이동**(09-18 유언집행자 계열). 이번 회차 두 영상 합계 **약어 확장 창작 다섯 번**(Vercel 편 *PMF → Product Management Framework* 포함). ⑤ **✅ 공식 챕터가 자막 오류를 두 번 고쳐 줬다** — *"Uturn detection"*(채움말 융합) → ko *"유턴 감지"*, *"bargin"* → ko *"협상"*. 챕터 *"턴 감지와 끼어들기(Barge-in) 제어"* 가 둘 다 확정. 09-15 원칙의 **세 번째 적용**. ⑥ **같은 제품명이 한 영상에서 살기도 하고 죽기도 한다** — Vercel 편 en-orig가 *Claude Code* 를 **"Cod code"** 로 반복 오인식했는데 ko가 **여섯 자리에서는 "클로드 코드"로 옳게, 두 자리에서는 "Claude"를 떨어뜨렸다**(*"코드 스타일"*·*"코드 SDK"*). 09-18 ⑤(같은 화자·다른 ko 결과)의 **영상 내부 판본**. 같은 영상에서 *Opus 4.5* 도 **오퍼스/오푸스** 두 표기. ⑦ **`architecture` → "건축"이 이틀 만에 재발**(Vercel 편 05:38, 09-18 ⑥과 동일).

부수: *"mega contacts"*(en-orig가 context→contacts 오인식) → ko **"모든 주요 연락처"** — **아키텍처 전환을 선언하는 핵심 문장**이 전화번호부가 됐다. **ko가 라이브러리 이름 둘을 통째로 지움** — *"Python's data classes **pantic zod** from Typescript"* → *"파이썬의 데이터 클래스나 타입스크립트의 클래스"*(Pydantic·Zod 소실). *mixture of experts* **네 표기**(전문가 혼합물/혼합물 전문가/믹서 전문가/전문가들이 조합한 방식, 둘은 수식 관계 뒤집힘 — 09-18 executor 계열). 고유명사가 **양 트랙 모두** 깨진 경우 다수 — **Plivo → "Cleo"·"PO"**(하필 *"엔진들이 피보·플레오로 발음한다"* 는 문장에서), **Cerebras → "Cerebris"**, **Groq → "Gro"**, **Qwen → "Quen"/"퀸"**, **Sonnet → "Sonic"**. *agent* → 에이전트/**상담원**/담당자(Vercel 편 테제 문장 *"모든 책상에 상담원을"*), *"we thought we were cooking"* → *"요리가 잘 되고 있다"*, *"we power across the globe"* → *"전력을 공급받고 있습니다"*, *field* → *"현장 작업"*, *jargon* → *"자렌스"*, 문말 *"Right?"* → **"오른쪽?"**(Plivo 편에서만 열 번 넘게).

**인명 처리**: **Andrew Qu** — 자막이 성을 말하지 않아 **설명란 채택**(채널 **다섯 번 연속** 설명란 의존). **Venky B** — 설명란 표기를 채택하되 자막의 세 변형(*Wenke* · *Balos Subramanion*)을 raw에 남기고 **성의 철자는 확정하지 않았다.** 화자 스스로 *"사람도 음성 인식 엔진도 못 맞히는 이름"* 이라 말하며 **그 발음 실패를 TTS 테스트의 논거로 쓰는** 소스라 특히 그렇다 — 그리고 **자막이 그 이름과 회사명을 둘 다 틀렸다.** Vercel 편의 *"미니 claw"*(Aura가 재구축한 에이전트의 비유)는 **판독하지 않았다.**

**행사·촬영 시점**: **둘 다 행사명 미확정.** 09-07 절차대로 두 편을 서로 대조했으나 같은 행사라는 근거가 없어 **별개 취급**(양쪽 다 행사명 무언급, 상호 참조 없음). Vercel 편의 *"2주 전 런던 행사"* 는 **Eve 공개 행사이지 이 발표의 자리가 아니다** — 혼동 주의. 시점 앵커: Vercel 편은 *"약 1년 전… [Sonnet] 4 정도"* + *"2주 전 Eve 출시"*(연도 없음), Plivo 편은 자기 진술 *"약 14년"* + *"2011년 시작"* 이 **2025년**을 가리켜 업로드와 1년 어긋나나 **반올림 가능성 때문에 확정하지 않았다.** 09-03 절차 적용 결과는 양쪽 다 **미확정**이다(09-04와 같은 결론).

**해소하지 않고 표시만 한 것**: Vercel 편 — **eval의 실체**(30%와 *두 배* 의 분모가 같은지도 불명), *"끔찍하다"* 의 내용, v2의 *"몇 가지 한계"*(요약 손실 하나만 명시), **증류된 스킬의 검토**(누가 보는가, 100개가 충돌하지 않는가, 낡으면 어떻게 되는가 — 09-05가 명시적으로 막으려 한 것이 여기서는 열려 있다), **보안·권한 전부**, Aura의 성과(수치 없음), 테스트한 수직 에이전트 스타트업의 이름·기준·결과, 컨벤션의 실제 규격(폴더 이름 셋뿐), *"Sonnet 4"* 판독, *"미니 claw"*. Plivo 편 — **모든 벤치마크의 실체**, 30%→95%의 분모(뒤에서 95~97%로 달라짐), *"AI 에이전트의 50~60%"* 의 근거, 지연 티어의 출처(*"광고된다"* 뿐), Cerebras·Groq 가격·12개월 대기(**전언**), token fertility 측정 조건, WER의 엔진·데이터셋, **턴 감지·barge-in 내용 전부**, ⚠️ **"speech-to-speech 파이프라인으로 하면 speech-to-speech 모델이 필요 없다"(25:43~25:58)의 자기모순**(판독하지 않음 — **이 소스는 캐스케이드와 end-to-end 음성 모델의 대비를 끝내 정리하지 않는다**), 화자 성의 철자, **비용 축 전체**.

**운영 메모**: 09-18 지침대로 **목록을 파일로 받고 `wc -l`로 15편 확인**(WARNING 줄에 잘리지 않게). yt-dlp가 *"YouTube account cookies are no longer valid"* 경고를 **이틀 연속** 냈으나 목록·자막 모두 정상 반환 — **429로 이어지지 않았다. 계속 감시.** 버전 90일 초과 경고도 계속(업데이트는 사람의 결정). 자막은 `--sub-format json3`으로 받아 dedup 후 타임스탬프를 보존했고, 인용 시각은 **개별 자막 이벤트 시각**을 썼다. en과 en-orig는 동일 파일(둘 다 자동 생성). 두 편 다 **공식 챕터를 그대로 따랐다**(10개·15개).

## [2026-09-20] ingest | Tech Bridge — Greg Brockman의 AGI 시대·방어자의 창(OpenAI × a16z) · RLHF 다음은 무엇인가(Diogo Almeida, TypeSafe) (09-19 업로드 2편)

[[tech-bridge|Tech Bridge]] 최근 업로드 15편 중 **신규 2편**(둘 다 2026-09-19 업로드), 12편은 이미 ingest돼 있었다. **나머지 1편(`vMlsLmKuFZk`, 09-18 업로드, 37:03)은 멤버 전용(`availability: subscriber_only`)이라 포맷·자막을 받을 수 없어 건너뛰었다** — 09-19 ingest에서 빠진 이유도 이것이다. 전부 롱폼(Shorts 없음). ko·en-orig **429 없이 전부 확보.**

**신규 source 2 · concept 11 · entity 6, 기존 17페이지 보강. index 실측 518 → 537.**

- [[tech-bridge-brockman-agi-era-defender-window]] (49:21, [[greg-brockman|Greg Brockman]] / [[openai|OpenAI]] 공동창업자·사장 × [[ben-horowitz|Ben Horowitz]]·Erik Torenberg / [[a16z]] 팟캐스트) — **공식 챕터 10개**. **이 위키의 OpenAI 1인칭 소스가 [[sam-altman|Altman]] 한 사람에서 둘로 늘어난 날**이고, **보안이 회사 전략의 축으로 서는 첫 소스**다. 선언은 *"우리는 AGI 시대에 있다"* 인데 **내용이 모델이 아니다** — *"이 모델인지 이전 모델인지 다음 모델인지는 상관없다. 요점은 안전·보안·정렬을 배포 시점이 아니라 개발 시점과 평가까지 거슬러 올라가 생각해야 한다는 것"*(47:48~48:02) → [[agi-definition]] **네 번째 입장**(무의미함에 동의하면서 선언을 유지하고 지시 대상을 **공정**으로 옮긴다) · [[pacing-the-frontier]](*"컴퓨트보다 오히려 그 제약들"* — [[compute-constrained-growth]]의 병목 순위를 뒤집는다) · [[jagged-capability-frontier]](**들쭉날쭉하다 = 단일한 문턱이 없다**). 보안 쪽 셋: **[[defenders-window]]**(확산 전의 한시적 구간, 비대칭의 근거가 *"방어자가 전장을 통제한다"*, 격차는 **신뢰 접근 프로그램**에서 난다, 처방은 **10억 달러 약정**+[[crowdstrike]]) · **[[defense-factory]]**(발견→분류→교정→배포→검증을 기계 속도로, 트리거가 **모델 릴리스**, ⭐ **완료 기준이 "포화"**) · **[[ai-formal-verification]]**(*"형식 검증이 안 뜬 건 틀려서가 아니라 사람에게 다루기 어려워서"*, 근거는 나비에-스토크스의 **Lean 형식화**). 증거: **프로덕션 엔지니어 25%를 보안으로**([[ai-vulnerability-discovery]]) · **1만 에이전트**([[agent-swarm]]) · 개인 펜테스트 **15분 13건 / 45분 수정**([[codex]]·[[cloudflare]]·[[scheduled-agent-automations]] — **발견보다 교정이 세 배**). 제품 비판은 본인 입에서: *"약속받았던 AI는 텍스트 상자가 아니었다"*([[capability-discovery-burden]], **써봤다 떠난 15억 명**). 기존 보강: [[openai]](Sora 취소·ChatGPT Work 통합·수치·인프라 약정·2015/2017 계보) · [[openai-astra]](**두 번째 1인칭 출처 + 처음 지목된 한계**) · [[hugging-face]](**다섯 번째 서술**) · [[agi-definition]] · [[ai-jobs-impact]](*"사람은 과제를 할 수 있어서 가치 있는 게 아니다"* — [[named-human-accountability]]가 **통제 수단에서 가치 근거로** 뒤집힌다) · [[ai-slop]](**제작사가 평가 눈금으로 쓴 첫 사례**) · [[reward-hacking]](표면 필터 → 아키텍처) · [[model-context-protocol]](*"세상을 다시 도구화하고 있다"*) · [[agent-swarm]] · [[ai-vulnerability-discovery]] · [[compute-constrained-growth]] · [[spacex]].
- [[tech-bridge-rlhf-assistance-vs-automation]] (17:36, [[diogo-almeida|Diogo Almeida]] / [[typesafe-ai|TypeSafe]] · [[ai-engineer|AI Engineer]] World's Fair — ⚠️ **이름은 설명란에만**) — **공식 챕터 11개**. **위키 첫 "설계자의 사후 비평"** — GPT-4·ChatGPT·InstructGPT 공동 저자가 *"OpenAI에서 ChatGPT를 실제로 싫어하는 몇 안 되는 사람 중 하나"* 라 자칭하며 *"ChatGPT 뒤의 알고리즘을 만들면서 내린 사소한 결정들이 이 분야의 현재 상황을 만들었다"*(01:23~01:33)고 말한다. **그리고 이 소스가 이 위키에 [[rlhf]] 페이지가 없었다는 사실을 드러냈다.** 출발점은 *"어떻게 미해결 수학 문제를 풀면서 고객 서비스에는 사람이 결정을 내려야 하는가"*(03:40~03:56), 답이 **[[assistance-vs-automation]]**(*"왼쪽 과제의 목표는 루프 안의 사람을 만족시키는 것"* — **[[workflow-vs-agent]]와 축이 다르다**, 루프가 동적이어도 사람을 만족시키면 보조). 귀결이 **[[preference-reward-asymmetry]]**(*"과대약속은 버그가 아니라 특징"* · **틀림은 알아보기 어렵고 확신 없음은 쉬워서 불확실성 표현만 벌받는다** — **위키가 받은 환각의 첫 구조적 설명**). 두 번째 축이 **[[smarter-software-vs-cheaper-software]]**(*"SaaS는 2019년 이후 챗봇이 붙은 것 말고 변한 게 없다"* · *"우리가 자동화한 건 소프트웨어를 쓰는 과정뿐이고 접근성은 그대로다"*), 맺음이 **[[post-training-northstars]]**(RLHF/RLVR/**보정된 의사결정**, 위계는 **올바른 작업 > 데이터 > 컴퓨트**). 기존 보강: [[claude-code]](**위키의 가장 이론적인 비판** — *"여전히 보조의 시대이고 여전히 RLHF"*, ⚠️ 단 같은 발표에서 *"좋아하고 계속 쓴다"*) · [[sutton-bitter-lesson]](⚠️ **반대 방향으로 인용된 첫 사례** — 판독하지 않음) · [[openai]] · [[ai-engineer]].

**이날의 구도 — 같은 회사의 안과 밖, 그리고 정반대 진단.** 현직 사장과 전 연구자가 하루에 들어왔고 **서로를 전혀 언급하지 않는다.** *"약속받았던 AI가 아니다"* 를 Brockman은 **제품 문제**로, Almeida는 **목적함수의 귀결**로 읽는다. ⚠️ **환각에서는 정면 충돌한다** — Brockman 편 진행자는 *"저는 꽤 오랫동안 환각을 본 적이 없습니다"*(39:33~39:50), Almeida는 *"인간 선호를 최적화하는 데 내재되어 있다"*(14:36~15:07). **한쪽은 개인 체감, 다른 쪽은 형식화되지 않은 구조 논증이고, 어느 쪽도 측정을 제시하지 않는다. 이 위키는 대조만 기록하고 판정하지 않았다.**

**세 소스가 한 방향을 다른 거리에서 가리킨다.** 도구 층에 대해 — 09-15 [[graft]] 편이 **CLI vs MCP를 측정**했고([[push-vs-pull-context-retrieval]]), 09-19 Vercel 편이 **도구를 깎지 말고 파일 시스템을 줘라**([[file-system-agent]])로 갔고, 오늘 Brockman이 **도구 층 자체가 임시방편이고 사람용 인터페이스가 목적지**라고 말한다(*"세상을 다시 도구화하고 있다"*, 21:58~22:13). → [[model-context-protocol]]

**같은 개념이 뒤집힌 사례 하나.** [[named-human-accountability]]는 09월 내내 **운영상의 안전장치**(누가 책임지는지 이름을 적어 두라)였는데, 여기서 **보존해야 할 인간의 자리**가 된다 — *"사람은 과제를 할 수 있어서 가치 있는 게 아닙니다. 우리는 우리가 사람이기 때문에 가치 있습니다."*(25:44~26:12)

**⚠️ 이날 가장 큰 공백 둘.** ① **보안을 40분 말한 대담에 컴퓨터 사용의 보안 모델이 통째로 없다** — [[prompt-injection]]·[[lethal-trifecta]]·[[agent-identity-separation]]이 한 번도 나오지 않고, 진행자가 *"또 다른 보안 과제 레이어가 생긴다"* 고 지적하자 *"정확합니다"* 로만 받는다(22:13~22:33). ② **진행자가 낸 가장 강한 반론에 답이 없다** — *50년치 레거시와 중앙집중 허니팟, 탈중앙화 소비자 아키텍처가 필요한가*(11:28~12:37)가 **대담 끝까지 돌아오지 않는다.** 09-18 [[legacy-code-modernization]]·[[legacy-skills-gap]]이 **정확히 그 표면적이 왜 줄지 않는지**를 말한 페이지라, 두 소스를 겹치면 [[defenders-window]]의 낙관은 약해진다.

**⚠️ 이해관계 표시가 이날의 별도 관측이다.** 이 채널이 재배포한 소스의 제작 주체는 지금까지 기업 개발자 관계 채널·컨퍼런스·일반 언론이었는데, **투자자가 만든 매체는 처음**이다([[a16z]]). 그리고 **데이터센터 규제 완화·AI 낙관·고용 증가를 화자보다 먼저, 더 강하게 주장하는 쪽이 진행자**인데 **대담은 그 이해관계를 한 번도 표시하지 않는다.** *"AI가 좋아질수록 고용은 높아진다"*(24:56~25:14)의 근거는 *"적어도 지금까지 수치로는"* 뿐이고, *"[Switch] 한 곳이 4만 5천 명"*(33:31~33:50)도 출처가 없다. → [[ben-horowitz]]

**운영 메모 — 멤버 전용 영상이 처음 나왔다.** `vMlsLmKuFZk`(09-18 업로드, *샘 올트먼과 마크 베니오프 대담*, 37:03)이 **`availability: subscriber_only`** 라 `--write-info-json` 은 되지만 **포맷도 자막도 없다**(`No video formats found` · `automatic_captions` 빈 배열). **vault에 없으므로 dedup으로 걸러지지 않아 매일 목록에 계속 나타난다.** → **앞으로 목록의 영상이 vault에 없을 때 "누락"인지 "접근 불가"인지 먼저 확인한다.** `availability` 필드가 `subscriber_only` 면 **건너뛰고 기록만 남긴다.** 이 위키는 이 영상으로 페이지를 만들지 않았다.

**자막 관찰 — 부호 뒤집기가 이번 회차의 주 오류.** ① ⚠️ **뜻이 정반대로 뒤집힌 최대 폭** — *"the business is **ripping**"*(사업이 아주 잘 된다) → ko **"그 사업이 완전히 망해가고 있다"**(43:14). 이어지는 질문이 *"어떻게 우선순위를 정하느냐"* 라 **ko만 읽으면 위기 대응 대담으로 읽힌다.** 09-07 계열 중 가장 크다. ② ⚠️ **인구가 면적이 됨** — *"a significant fraction of **the planet**"* → **"지구 전체 면적의 상당 부분"**(40:38), 앞 문장이 **15억 명**을 말하는 자리다. ③ ⚠️ **[[ai-slop|슬롭]]이 기울기가 됨** — *"It's the first time it's not **sloping**"*(en-orig 자체가 *slop* 오인식) → **"경사가 없는 건 이번이 처음"**(38:57), **[[openai-astra|Astra]]의 품질 평가가 통째로 사라진다.** ④ ⚠️ **프로그램 이름 전체가 스포츠로** — *frontline defenders* → **"최전선 수비수들"·"수비팀"**(35:51·36:25), 09-19의 문장 단위 도메인 이동 계열인데 이번엔 **10억 달러 프로그램의 이름**이다. ⑤ ⚠️ ***our chef* = RLHF** — *"I wouldn't say **our chef** is a wrong"* → **"우리 셰프가 틀렸다고는 말할 수 없지만"**(Almeida 편 12:19), **발표의 세 번째 교훈을 여는 문장**이다. ⑥ ⚠️ **[[hugging-face]] 직역이 재발했고 같은 영상 안에서 갈린다** — 18:42 *"얼굴을 껴안고 난 후"* 인데 08:49·09:27·16:37은 옳다. **이 위키의 [[hugging-face]] 페이지가 09-14에 *개선* 으로 기록해 둔 항목이 뒤집혔다.** 09-19 Vercel 편의 ⑥번(한 영상 안에서 같은 이름이 살기도 죽기도)이 **이틀 연속**이고, Almeida 편의 *Claude Code* → **클로드 코드/클라우드 코드** 도 같은 유형이다. ⑦ ⚠️ **LLM 오역이 또, 이번엔 한 영상에 세 갈래** — **법학도 / 학습관리시스템(LMS) / LLM 과정**(Almeida 편). 09-19의 *한 영상에 네 가지* 에 이어 연속. ⑧ ⚠️ **없던 도메인 창작이 네 번** — *assistance* → **"의료 보조"**(09:35) · *post training* → **"훈련 후 평가"**(없던 "평가") · *agentic coding* → **"인공 코딩"** · *frontline defenders*. ⑨ ⚠️ **한정어 소실로 모수가 커짐** — *"25% of our **production** engineers"* → **"전체 엔지니어의 25%"**(13:33). *MBTI* → **"MBG"**(42:23). ⑩ ⚠️ **개인 도메인이 en-orig에서 세 갈래** — *gregbrockman.com* → **gregarin / gregroman / Craig Brockman**.

**✅ 반대 방향 관측 둘.** ① **촬영 연도가 자막 내부에서 확인된 첫 사례** — 진행자가 *"2026년의 AI 세계"*(01:02)라고 현재를 지목한다. 09-03에 세운 촬영 시점 확정 절차를 써 온 이래 처음이다(월·일은 여전히 미확정). ② **설명란이 이름을 두 번 확정했다** — **Diogo Almeida**(자막 양 트랙 *"Diego Mida"*)와 **a16z**(자막 양 트랙 *"A&Z"*). **채널 여섯 번 연속 설명란 의존.**

**⚠️ 공식 챕터를 신뢰한다는 원칙에 단서가 붙었다.** 09-15에 세우고 세 번 적용한 원칙인데, 이날 **챕터가 틀린 사례 둘**이 나왔다. ① Brockman 편 챕터 *"아시아의 AI 수용도가 서구권보다 훨씬 높은 이유"* 인데 대담은 **"유럽도 높고 미국만 가장 낮다"**(29:24~29:53)고 말한다 — 이 위키는 **대담을 따랐다.** ② Almeida 편 챕터 *"비즈니스에서 AI로 중요한 결정을 내리지 못하는 이유"* 의 내용이 **앞 챕터 구간(05:18~05:41)에 이미 나온다.** → **챕터는 자막 오류를 고쳐 줄 때는 유효하지만, 내용의 범위와 순서를 규정하지는 못한다.**

**⚠️ 제목이 약속한 것이 소스에 없는 사례, 세 번째.** Almeida 편의 **'Jev'** 가 자막에 **한 번도 나오지 않는다** — 채널 제목과 설명란에만 있고, 화자는 회사 이름([[typesafe-ai|TypeSafe]])만 말하고 모델 이름을 말하지 않는다. **이 위키는 그 이름을 본문에 쓰지 않았다.** 09-14 *"21가지"*, 09-15 *"GitHub 1위"* 에 이은 세 번째.

**해소하지 않고 표시만 한 것**: Brockman 편 — **탈중앙화 반론에 대한 답**(끝까지 없음), **컴퓨터 사용의 보안 모델 전부**, **1만 에이전트의 조율·비용·검증**(Lean 형식화 외 없음), *"25%"*·*"13건/15분/45분"*·*"11억/1억/3억/15억"*·*"10억 달러"* 의 측정 조건, [[openai-astra|Astra]]의 *"24시간 일관성"*·*"P0 포화"*·*"계단 함수"*, Astra ↔ GPT-6 명명 관계, **Sora 취소의 시점·규모**, *"AI가 좋아질수록 고용이 높아진다"* 의 수치 출처, **[SpaceX] 언급**(프론티어 랩 열거에서 문맥과 어긋나나 양 트랙 일치 → 판독 안 함), *"LCMS"*(→LSTM 추정)·*"soda models"*(→SOTA 추정)·*"deeper codees"*·*"variance"*. Almeida 편 — **제3의 목표가 실제로 무엇인지**(이름뿐), **'Jev'**, *"거의 100%의 LLM이 RLHF"* 의 근거, **메타 분석 그래프의 출처·수치**, *"원래의 스케일링 법칙이 잘못되었다"*(힌트 한 줄로 끝), **[[sutton-bitter-lesson|Bitter Lesson]] 인용의 방향**(양 트랙 일치 → 판독 안 함), *"Gary Tan"*·*"Yoshua Bengio"*(자막이 유일한 출처 → 확정 안 함), **비용·지연·규모 전부**, ⚠️ **자동화가 좋은 일인지에 대한 논의 부재**(일자리·책임·오작동 귀속을 건드리지 않으면서 *사람이 결정해야 하는 상태* 를 결함으로 부른다).

**운영 메모**: 09-18 지침대로 **목록을 파일로 받고 `wc -l`로 15편 확인**(WARNING 줄에 잘리지 않게) — 이번에도 유효했다. yt-dlp가 *"YouTube account cookies are no longer valid"* 경고를 **사흘 연속** 냈으나 목록·자막 모두 정상 반환 — **429로 이어지지 않았다. 계속 감시.** 자막은 `--sub-format json3`으로 받아 dedup 후 **개별 자막 이벤트 시각**을 인용 타임스탬프로 썼다. en과 en-orig는 동일 파일. 두 편 다 **공식 챕터를 따랐다**(10개·11개) — 단 위 ⚠️ 참조. **`--write-info-json` 의 `availability` 필드를 이번부터 확인한다**(멤버 전용 판정용).
