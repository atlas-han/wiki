---
title: Harness Engineering
type: concept
category: pattern
tags: [agent, harness, ai-layer, coding-agent, orchestration, llm-engineering]
related: [agent-harness-design, self-harness, context-engineering, ralph-wiggum-method, dynamic-workflows, generator-evaluator-pattern, model-context-protocol, llm-coding-guidelines, brain-hands-decoupling, verifiable-goals, spec-driven-development, agent-org-adoption, frontier-engineering, tools-and-context-over-harness, shift-left-interventions, agent-loop-size]
first-seen: tech-bridge-harness-engineering
sources: [tech-bridge-harness-engineering, self-harness-paper, tech-bridge-spec-driven-development, tech-bridge-figma-coding-agents, tech-bridge-frontier-engineering, tech-bridge-ai-native-skills, tech-bridge-cursor-legacy-refactoring, tech-bridge-lopopolo-agent-harness]
created: 2026-06-03
updated: 2026-09-23
---

# Harness Engineering

대형 언어 모델(LLM)을 감싸는 **wrapper 전체를 설계·구현하는 기술이자 마인드셋**. 모델에 올바른 컨텍스트와 프로세스를 부여해 완전한 기능의 *에이전트*를 만들고, 나아가 여러 에이전트 세션을 자동화된 워크플로로 오케스트레이션한다. 2026년 들어 대중화된 우산 용어로, 2025년의 [[context-engineering|context engineering]]에서 한 단계 진화한 개념으로 제시된다. 출처: [[tech-bridge-harness-engineering]].

> `AI 에이전트 = 기본 LLM(추론 엔진) + 하네스 래퍼(컨텍스트·프로세스 정의)`

본 위키에는 동일 영역을 **Anthropic 관점**에서 다루는 허브 [[agent-harness-design]]가 먼저 존재한다. 이 페이지는 같은 영역의 *대중화된 프레이밍*(AI Layer 모델 · System Evolution 마인드셋 · 다중 세션 오케스트레이션)을 정리하고, agent-harness-design와 상호 참조한다.

## context engineering과의 관계 (진화 지점)

[[context-engineering|Context engineering]]과 harness engineering은 단일 세션 수준에서 거의 같은 질문 — *"모델에 올바른 컨텍스트 생태계를 어떻게 주는가"* — 을 공유한다. harness engineering이 더하는 것은 두 가지:

1. **Control** — 루프, 다중 세션 오케스트레이션, sub-agent. 단순 컨텍스트 주입을 넘어 *행동을 제어*. [[ralph-wiggum-method|Ralph Loop]]가 대표.
2. **Skill issue 리프레임 (마인드셋)** — 아래 [System Evolution](#3-system-evolution-마인드셋) 참조.

> ⚠️ 영상 스스로도 *"becoming such a buzzword"* 라며 대부분이 context engineering과의 차이를 이해하지 못한다고 지적. 차별점은 control과 mindset에 있다.

## 1. 3계층 아키텍처

단일 코딩 에이전트 세션은 세 겹의 래퍼로 본다:

| 계층 | 정체 | 누가 만드나 |
|---|---|---|
| **Base LLM** | [[claude-opus-4-7|Claude]]·GPT 등 순수 추론. 단독으로는 파일시스템·명령 실행 불가 | 모델 제공사 |
| **Tool Harness** | [[claude-code|Claude Code]], Codex 등 — 모델에 터미널·시스템 프롬프트를 입힌 상용 래퍼 | 도구 회사 |
| **AI Layer** | 컨텍스트·프로세스를 정의하는 **최상위 래퍼** | **개발자(나)** |

> *"도구를 고르는 순간 이미 하네스를 고르는 것"* — Claude Code vs Codex 논쟁도 결국 어느 Tool Harness를 택할지의 문제. 하지만 진짜 차이를 만드는 건 그 위의 AI Layer다.

## 2. AI Layer — 6가지 구성 요소

개발자가 직접 제어하는 층. *"프로세스·규칙을 주입하려면 이 6가지 중 하나를 통한다."*

| 구성 요소 | 역할 | 본 위키 |
|---|---|---|
| **Global Rules** | 코딩 표준·제약·패턴 (예: CLAUDE.md / agents.md) | [[llm-coding-guidelines]] |
| **Skills & MCP** | 워크플로·외부 기능 부여 | [[model-context-protocol|MCP]] · [[agent-skills]] (조직 거버넌스 면: inner harness vs outer workflow, registry) |
| **Codebase Search** | LSP·지식 그래프로 코드 컨텍스트 파악 | [[code-knowledge-graph]] |
| **Hooks** | 이벤트 트리거 — 보안 차단·품질 검증 | (아래) |
| **Sub-agents** | 세부 태스크 위임 (병렬/순차) | [[generator-evaluator-pattern]] |
| **Context Docs** | 온디맨드 외부 지식 (markdown·Confluence) | [[context-engineering]] |

**Hooks의 실전 3종**:
- **pre-tool-use 보안 훅** — 파괴적 명령(디렉토리 삭제 등)·민감 파일 읽기를 *실행 전* 차단.
- **stop validation 훅** — 에이전트가 "완료"를 선언하면 테스트·린트·타입체크를 결정론적으로 실행, 실패 시 재반복 강제. ([[verifiable-goals]] 사상과 동형 — *"done"의 검증을 코드에 박는다.)
- **post-edit lint** — 매 파일 수정 후 빠른 lint로 코드베이스를 깨끗이.

## 3. System Evolution 마인드셋

harness engineering의 핵심은 기술 스킬을 넘어 **태도의 전환**이다.

- **Skill issue (안티패턴)**: 에이전트가 실수 → 모델 탓 → *"Opus 5 / GPT-6 나올 때까지 기다리자"*. 책임을 다음 모델 버전으로 미룸.
- **System Evolution (권장)**: *"every mistake becomes a rule"* — 모든 실패는 **legible**(원인이 읽힌다)하므로 하네스 개선의 기회로 본다.
  - 컨벤션 위반 ➡️ `agents.md`에 규칙 추가
  - 파괴적 명령 실행 ➡️ pre-tool-use hook으로 차단
  - → 다음 세션에서 같은 문제 재발 확률을 낮춤. 인간이 *steering*하는 feed-forward 시스템.

이 사상은 [[ralph-wiggum-method|Ralph]]의 *"실패를 거부하지 말고 튜닝 신호로"* 철학, [[agent-harness-design]]의 *"harness는 모델이 못하는 것에 대한 가정의 다발"* 과 정확히 맞물린다. 단, 강조점이 다르다 — agent-harness-design은 *모델이 좋아지면 가정을 제거*(harness 단순화)에, harness engineering은 *실패에서 가정을 추가*(harness 강화)에 무게. 두 방향은 같은 진화 루프의 양면.

[[tech-bridge-frontier-engineering]]의 습관 1이 이 양면을 **매일의 steering 파일 루프**로 서술한다. 에이전트 실수 → skills/steering에 뭐가 빠졌나(추가). Sonnet 3.7 quirk용 do-not은 Opus 4.5 이후 **지울 것**(제거). "아직 필요한가, 아니면 컨텍스트 팽창인가."

> **자동화된 System Evolution = [[self-harness|Self-Harness]].** *"every mistake becomes a rule"* 에서 사람이 `agents.md`에 규칙을 적는 손을 떼고, **에이전트가 자기 실행 트레이스에서 직접 규칙을 합성**하면 그것이 [[self-harness|Self-Harness]](Shanghai AI Lab, [[self-harness-paper]])다. Weakness Mining(실패 클러스터링) → Proposal(diverse yet minimal edit) → Validation(회귀 게이트)의 3단계 루프로, [[terminal-bench|Terminal-Bench-2.0]] 3개 모델에서 *모델마다 다른* 하니스 진화를 정량 입증했다. *skill issue 안티패턴*(모델 탓하며 다음 버전 대기)의 정확한 반례.

## 4. 다중 세션 오케스트레이션 (최종 진화)

거대한 task/PRD를 단일 세션에 몰아넣으면 토큰 비효율 + 모델 과부하로 *"fall flat on its face"* — AI Layer 품질과 무관하게 실패. 해법은 역할이 분리된 세션에 **focused task**를 주고 아티팩트로 핸드오프하는 것.

- **PIV 워크플로 (Plan → Implement → Validate)**: 세 단계를 *각각 별도 세션*으로 분리해 토큰 효율·집중을 유지. 각 스킬이 markdown 아티팩트를 출력 → 다음 세션 입력. 수동으로 하면 사람이 plan 산출물을 직접 implement 세션에 넘김.
- **자동화 = [[ralph-wiggum-method|Ralph Loop]]**: 핸드오프·PR 생성을 스크립트가 자동 연결. 큰 작업을 세부 태스크로 분할 → 완료 표식(`done` 파일)까지 반복 → 보안·정확성·단순성 리뷰 에이전트를 병렬 실행. 인간 베이비시팅 없이 SDLC 자동화.

이는 본 위키의 [[dynamic-workflows|dynamic workflows]](Claude가 오케스트레이션 스크립트를 *동적 작성*)와 대비된다 — Ralph Loop는 사람이 *고정* 스크립트를 짜는 자동화, dynamic workflows는 모델이 오케스트레이션 층 자체를 생성. 둘 다 [[generator-evaluator-pattern]]의 병렬 리뷰 사상을 공유.

## 생태계 도구

- [[archon|Archon]] — 오픈소스 하네스 빌더. Ralph Loop류를 자신의 프로세스·SDLC에 맞춰 커스텀 구축. (발표자의 프로젝트)
- **Google Cloud Agent CLI** — 에이전트 구축 스킬 + 로컬 Playground + 단일 명령 프로덕션 배포·옵저버빌리티 (영상 스폰서).

## 사용자(이 vault 운영자) 관점

이 vault의 [[CLAUDE]] 스키마 + skills(ingest/query/lint/graphify 등) 자체가 AI Layer의 한 구현 — Global Rules(CLAUDE.md) + Skills + Hooks로 LLM에 일관된 워크플로를 인코딩. [[agent-harness-design]]의 *"knowledge base harness"* 시각과 동일.

## 2026-08 교차: 스펙 아티팩트와 조직 도입

[[tech-bridge-spec-driven-development]]의 [[spec-driven-development]]는 AI Layer의 Global Rules / Context Docs를 **저장소 계약**(constitution → spec → plan → task)으로 제품화한 형태. 프롬프트 대신 스펙을 메인 아티팩트로 두면 PIV의 Plan이 휘발되지 않는다.

[[tech-bridge-figma-coding-agents]]의 [[agent-org-adoption]]은 System Evolution을 *조직*에 적용한다. 유용한 에이전트 발견을 즉시 결정론적 체크로 코드화하는 것은 "every mistake becomes a rule"의 팀 운영판. 다만 규칙은 훅만이 아니라 PR 출처 표기·회의론자 로드맵이기도 하다.

## cursor harness — 네 구성요소 (2026-09-08)

[[tech-bridge-cursor-legacy-refactoring]]에서 [[cursor|Cursor]]가 자기 하네스를 명시적으로 정의한다. 이 위키가 모아온 하네스 정의에 하나가 더 붙는다.

> **플랫폼과 모델 사이에 있는 것을 cursor harness라고 부릅니다.** 플랫폼은 Cursor를 쓸 수 있는 모든 표면이고, 모델은 Cursor가 활용하거나 위임할 수 있는 LLM들입니다. 그 사이에 있는 것이 **도구 실행(tool execution) · 캐시 관리(cache management) · 동적 컨텍스트 관리(dynamic context management) · 컨텍스트 조립(context assembly)** 입니다.

| 소스 | 하네스를 무엇으로 정의하는가 |
|---|---|
| [[angela-jiang]] ([[tech-bridge-claude-platform-agent-era]]) | 모델 바깥에서 에이전트를 성립시키는 것 (토큰 역할·도구·루프) |
| **[[cursor]] (이 소스)** | **플랫폼과 모델 사이의 층** — 도구 실행·캐시·동적 컨텍스트·컨텍스트 조립 |

**Cursor 정의의 특징은 캐시 관리와 컨텍스트 조립을 1급 구성요소로 든다는 것**이다. 이 위키의 [[context-engineering]]·[[harness-pruning]]이 다뤄온 것들이 하네스의 **내부 부품으로 명시된** 첫 사례다.

그리고 하네스가 왜 필요한지가 **모델 교체 가능성**으로 설명된다 — 하네스가 그 층을 맡기 때문에 계획과 실행에 서로 다른 모델을 끼울 수 있다 → [[model-mixing-economics]].

> 모델과 플랫폼만 있는 게 아니라 **그 위에 우리가 제공하는 하네스도 있습니다.**

> ⚠️ **당사자 진술.** 하네스를 파는 회사가 하네스가 중요하다고 말하는 구조다. 4월에 쓰였다는 기술 블로그가 언급되나 소스에 링크가 없다.

## References

- [[tech-bridge-harness-engineering]] (1차, 영상)
- [[self-harness-paper]] — System Evolution 마인드셋의 자동화 사례
- [[tech-bridge-spec-driven-development]] · [[spec-driven-development]] — 스펙을 하니스 아티팩트로
- [[tech-bridge-figma-coding-agents]] · [[agent-org-adoption]] — 조직면
- [[agent-harness-design]] — Anthropic 관점 허브
- [[context-engineering]] — 진화의 출발점
- [[self-harness]] · [[ralph-wiggum-method]] · [[dynamic-workflows]] — 자기개선·오케스트레이션 갈래

## "하네스는 만들지 않는다"는 하네스 엔지니어 (2026-09-23 · [[tech-bridge-lopopolo-agent-harness]])

[[ryan-lopopolo|Ryan Lopopolo]](Google Cloud)가 **이 용어를 자기 것으로 부르는 사람**으로 나온다 — *"제가 '하네스 엔지니어링'이라고 부르는 것"*(14:50~14:52). 그의 정의는 이 페이지의 System Evolution과 같은 루프를 **"기본 상태로 되돌리기"** 로 요약한다.

> **기본적으로 하네스 엔지니어링의 모든 것은 에이전트를 기본 상태로 되돌리기 위한 점점 더 정교해지는 일련의 기법입니다.** (10:40~10:47)

그런데 그는 *"저는 하네스를 만들어 본 적이 없습니다"*(14:47)라고 한다 — Tool Harness(Antigravity 같은 것)는 **고정**하고 **도구와 컨텍스트**만 만진다. 위 3계층으로 옮기면 **Tool Harness는 고르고 AI Layer만 만진다**는 것과 같은 분업이다. → [[tools-and-context-over-harness]] · 개입의 순서는 [[shift-left-interventions]] · 긴 지평은 [[agent-loop-size]]

| 소스 | 하네스를 무엇으로 정의하는가 |
|---|---|
| **Google 에피소드 진행자 ([[tech-bridge-lopopolo-agent-harness]])** | **LLM이 아닌 모든 것** — *"하네스는 LLM을 제외한 AI 에이전트의 모든 구성 요소"*(00:47~00:49). 빌리: *"의도를 행동으로 연결"*(20:36~20:38) |

> ⚠️ Contradiction: 에피소드의 설명란·내레이션은 Lopopolo를 **"'에이전트 하네스'라는 용어를 만든"** 사람으로 소개한다(02:14~02:22). 본인이 명명을 주장하는 대상은 **harness engineering**이고, 이 위키의 [[agent-harness-design]]은 [[anthropic|Anthropic]] 블로그의 *harness* 용법에서 출발했다. **판정하지 않는다** — 양쪽 게재일이 위키에 월 단위로 없다. 이 페이지의 first-seen(06-03 Cole Medin 편)이 *"2026년 들어 대중화"* 라고 한 것과, Lopopolo의 **2026년 2월** 글(02:43~02:48)은 시간상 정합한다.
