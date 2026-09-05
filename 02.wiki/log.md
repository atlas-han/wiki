---
title: Log
type: overview
tags: [meta]
created: 2026-05-25
updated: 2026-09-04
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
