---
title: Harness Engineering
type: concept
category: pattern
tags: [agent, harness, ai-layer, coding-agent, orchestration, llm-engineering]
related: [agent-harness-design, context-engineering, ralph-wiggum-method, dynamic-workflows, generator-evaluator-pattern, model-context-protocol, llm-coding-guidelines, brain-hands-decoupling, verifiable-goals]
first-seen: tech-bridge-harness-engineering
sources: [tech-bridge-harness-engineering]
created: 2026-06-03
updated: 2026-06-03
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
| **Skills & MCP** | 워크플로·외부 기능 부여 | [[model-context-protocol|MCP]] |
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

## References

- [[tech-bridge-harness-engineering]] (1차, 영상)
- [[agent-harness-design]] — Anthropic 관점 허브
- [[context-engineering]] — 진화의 출발점
- [[ralph-wiggum-method]] · [[dynamic-workflows]] — 오케스트레이션 두 갈래
