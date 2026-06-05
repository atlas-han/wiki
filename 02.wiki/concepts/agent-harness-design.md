---
title: Agent Harness Design
type: concept
category: pattern
tags: [agent, harness, scaffolding, llm-engineering]
related: [harness-engineering, generator-evaluator-pattern, sprint-contract, brain-hands-decoupling, context-anxiety, context-resets-and-compaction, transcript-classifier, agentic-misbehavior, pets-vs-cattle, sutton-bitter-lesson, ralph-wiggum-method, model-context-protocol, dynamic-workflows]
first-seen: anthropic-harness-design-long-running-apps
sources: [anthropic-harness-design-long-running-apps, anthropic-managed-agents, anthropic-claude-code-auto-mode, anthropic-dynamic-workflows, tech-bridge-harness-engineering]
created: 2026-05-25
updated: 2026-06-03
---

# Agent Harness Design

LLM 에이전트가 단독 추론으로 못하는 일을 가능하게 만드는 **스캐폴딩** — loop, multi-agent orchestration, context 관리, tool 라우팅, 권한 게이트를 모두 포함하는 설계 영역. [[anthropic|Anthropic]] Engineering Blog 3편 연작([[anthropic-harness-design-long-running-apps]], [[anthropic-managed-agents]], [[anthropic-claude-code-auto-mode]])이 본 위키의 1차 출처.

> 같은 영역의 **대중화된 우산 용어**가 [[harness-engineering|harness engineering]] — AI Layer 6요소 모델, *"every mistake becomes a rule"* System Evolution 마인드셋, 다중 세션 오케스트레이션으로 프레이밍한다. 이 페이지(Anthropic 관점)와 [[harness-engineering]](커뮤니티 관점)는 상호 참조. 강조 차이: 여기는 *모델이 좋아지면 가정을 제거*(harness 단순화), 거기는 *실패에서 가정을 추가*(harness 강화) — 같은 진화 루프의 양면.

## 핵심 원리 (연작 전반의 일관된 모티프)

> Harnesses encode assumptions about what the model can't do on its own — and those assumptions go stale as models improve.

- Scaffolding은 모델의 한 시점 capability에 대한 *가정*의 다발이다.
- 모델이 발전하면 일부 컴포넌트는 dead weight가 된다 — 검증·제거가 일상적 작업이어야 함.
- 동시에 더 강한 모델은 더 야심찬 harness 조합을 가능하게 한다 — *"the space doesn't shrink, it moves."*

[[sutton-bitter-lesson|Bitter Lesson]] 정신과 정합. *"the space moves"*의 최신 증거가 [[dynamic-workflows]] — 사람이 짠 고정 multi-agent 스크립트가 아니라 **Claude가 오케스트레이션 스크립트를 동적으로 작성**하는 단계로 이동.

## 자주 등장하는 컴포넌트

| 컴포넌트 | 인코딩하는 가정 | 본 위키 상세 |
|---|---|---|
| **Context reset** | 모델이 context limit 가까이서 [[context-anxiety|early-wrap]]한다 | [[context-resets-and-compaction]] |
| **Sprint construct** | 모델이 멀티-피처 일관성을 못 유지한다 | [[sprint-contract]] |
| **Sprint contract** | 모델이 done의 정의를 합의 없이 자가판단한다 | [[sprint-contract]] |
| **Generator/Evaluator 분리** | 모델은 자기 작품을 후하게 평가한다 | [[generator-evaluator-pattern]] |
| **Planner agent** | 한 줄 prompt로 충분한 spec을 못 만든다 | [[generator-evaluator-pattern]] |
| **Transcript classifier** | 모델이 안전한 action만 시도하지 않는다 | [[transcript-classifier]] |
| **Prompt-injection probe** | 외부 콘텐츠가 모델을 hijack할 수 있다 | [[prompt-injection]] |
| **Brain–hands 분리** | 모든 게 한 컨테이너면 pet이 된다 | [[brain-hands-decoupling]] |
| **Session log 외부화** | Context window가 충분치 않다 | [[context-resets-and-compaction]] |

## 진화의 증거 — Sonnet 4.5 → Opus 4.5/4.6

- [[claude-sonnet-4-5|Sonnet 4.5]]: [[context-anxiety]] 강함 → context reset이 essential
- [[claude-opus-4-5|Opus 4.5]]: context anxiety 사라짐 → reset이 dead weight 되어 제거 가능
- [[claude-opus-4-6|Opus 4.6]]: 더 긴 일관된 작업 (DAW 빌드 2시간 7분 연속), sprint construct 제거 가능, evaluator는 *task가 모델 solo 한계 너머일 때*만 의미

## 메타-하네스 (Managed Agents 시각)

특정 harness를 고정하지 말고, **future-proof 인터페이스**를 잡아라:
- `session` — append-only event log, durable·interrogable
- `harness` — Claude를 호출하고 tool call을 라우팅하는 loop, **stateless**·cattle
- `sandbox` — execution env, `execute(name, input) → string`

OS 메타포: `read()`가 1970s 디스크팩과 SSD에 동일하게 동작한 것처럼.

## 권한·안전 게이트

[[anthropic-claude-code-auto-mode|Auto mode]]는 harness 안의 한 컴포넌트:
- 3-tier (allowlist → in-project → classifier) 권한 파이프라인
- [[transcript-classifier]]는 reasoning-blind by design (agent의 prose strip)
- Deny-and-continue로 흐름을 끊지 않음
- 4가지 위협 모델: [[agentic-misbehavior]]

## 자기-작성 오케스트레이션 (Dynamic workflows 시각)

[[dynamic-workflows|Dynamic workflows]]는 harness의 *오케스트레이션 층 자체*를 모델이 동적으로 생성하게 한 형태:
- Claude가 prompt를 받아 계획 → subtask 분할 → 10s~100s parallel subagent로 fan-out → 검증 후 fold-in.
- 독립 각도 공격 + adversarial refute로 **수렴**(= [[generator-evaluator-pattern]]의 오케스트레이션판).
- coordination을 **대화 바깥**에 두고 **resumable checkpoint** — [[managed-agents]]의 session 외부화([[context-resets-and-compaction]])와 동형 사상.
- 진입: 직접 요청 또는 [[ultracode]] 세팅.

## 관련 외부 패턴

- [[ralph-wiggum-method|Ralph Wiggum method]] (Geoff Huntley) — 훅·스크립트로 에이전트 반복 cycle을 유지. [[anthropic-harness-design-long-running-apps]]에서 비교 언급. 사람이 *고정* 루프를 짜는 것과, [[dynamic-workflows|dynamic workflows]]에서 Claude가 루프를 *동적 작성*하는 것의 대비.
- **Building Effective Agents** (Anthropic) — *"find the simplest solution possible, and only increase complexity when needed."*

## 사용자(이 vault 운영자) 관점

이 vault의 [[CLAUDE]]도 harness의 일종 — 일관된 ingest/query/lint 워크플로를 LLM에 인코딩하는 schema. [[llm-wiki-pattern]] 자체가 *"knowledge base harness"* 로 해석 가능.

## References

- [[anthropic-harness-design-long-running-apps]]
- [[anthropic-managed-agents]]
- [[anthropic-claude-code-auto-mode]]
- [[anthropic-dynamic-workflows]]
