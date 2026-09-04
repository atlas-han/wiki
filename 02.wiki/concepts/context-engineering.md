---
title: Context Engineering
type: concept
category: technique
tags: [llm, context-window, agent, prompting]
related: [context-resets-and-compaction, context-anxiety, agent-harness-design, harness-engineering]
first-seen: anthropic-managed-agents
sources: [anthropic-managed-agents, anthropic-harness-design-long-running-apps, tech-bridge-harness-engineering, tech-bridge-multimodal-commerce-agent]
created: 2026-05-25
updated: 2026-09-04
---

# Context Engineering

LLM의 context window에 무엇을 넣고, 어떤 순서로 배치하고, 언제 다시 fetch하고, 어떻게 transform할지에 대한 설계 영역. [[anthropic|Anthropic]]은 별도 글 [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)를 보유. 본 위키에서는 [[anthropic-managed-agents]]와 [[anthropic-harness-design-long-running-apps]] 안에서 언급.

## 주요 기법 (Anthropic 글 인용)

- **Compaction** — 진행 중 context를 요약해 길이를 줄임 ([[context-resets-and-compaction]])
- **Context trimming** — 오래된 tool 결과·thinking block 등을 선택적으로 제거
- **Memory tool** — context를 파일에 써서 세션 간 학습
- **Context reset** — 깨끗한 새 agent로 handoff
- **Session as external context object** — context를 window *밖*에 두고 슬라이스로 가져옴 ([[anthropic-managed-agents]] 패턴)

> It is difficult to know which tokens the future turns will need. ... Prior work has explored ways to address this by storing context as an object that lives *outside* the context window.

## Prompt cache 친화적 조직

Managed Agents 모델에서 fetched event를 transform하는 한 가지 목적은 **prompt cache hit율**을 최대화하는 context 배치. [[transcript-classifier]]의 stage 1→stage 2 디자인도 동일 원리 — stage 2는 stage 1과 거의 동일 prompt로 cache hit.

## Generator-Evaluator 관점

[[anthropic-harness-design-long-running-apps]]에서 sprint construct가 사라진 후, **자동 compaction**이 [[claude-agent-sdk|Agent SDK]] 차원에서 context growth를 처리하는 것으로 충분해짐. → context engineering의 *어디까지를 harness가 담당하고 어디부터 SDK·플랫폼이 담당하는가*가 빠르게 이동 중.

## Harness engineering으로의 진화 (2026 프레이밍)

[[tech-bridge-harness-engineering]] 영상은 context engineering을 *"2025년의 화두"* 로 두고, 2026년의 [[harness-engineering|harness engineering]]을 그 **직접적 진화**로 제시한다. 단일 세션 수준에서는 둘이 거의 같은 질문(올바른 컨텍스트 생태계)을 공유하지만, harness engineering이 더하는 것은 **control**(루프·다중 세션 오케스트레이션·sub-agent)과 **mindset 리프레임**(*every mistake becomes a rule*). 즉 *어디까지가 context engineering이고 어디부터가 harness engineering인가*의 경계는, 위 [Generator-Evaluator 관점](#generator-evaluator-관점)에서 본 *harness ↔ SDK/플랫폼* 경계 이동과 마찬가지로 빠르게 움직이는 중.

## 컨텍스트를 신뢰 등급별 슬롯으로 나누기 (2026-09-04)

[[tech-bridge-multimodal-commerce-agent]]의 **working state**는 컨텍스트를 통짜 텍스트가 아니라 **필드별로 나눈 상태**로 다룬다 ([[fuzzy-intent-discovery]]).

| 슬롯 | 성격 | 갱신 |
|---|---|---|
| **hard constraint** | 쿼리에서 그대로 뽑힌 확정 조건 | 고정 |
| **soft constraint** + **confidence score** | 이미지 등에서 추론한 선호 | 대화 중 계속 갱신 |
| **real-time variable** | 재고 등 | **믿지 않고 매번 재조회** |

두 가지가 이 위키에 새롭다. 첫째, **추론된 항목에 자기 확신도가 함께 저장된다** — 그래서 "신뢰도를 올리는 것"이 에이전트의 행동 목표가 될 수 있다. 둘째, **믿으면 안 되는 필드가 명시적으로 구분된다** — *"오래된 정보라면 아무 의미가 없기 때문"*.

[[agent-distributed-systems]]가 *"에이전트 메모리는 무효화 가능한 캐시"* 라고 한 것과 같은 문제를 **상태 스키마 층위**에서 다룬 형태다. 컨텍스트를 "무엇을 넣을까"가 아니라 **"각 항목을 얼마나 믿을까"** 로 묻는다.

## References

- [[anthropic-managed-agents]]
- [[anthropic-harness-design-long-running-apps]]
- [[tech-bridge-harness-engineering]]
- [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
