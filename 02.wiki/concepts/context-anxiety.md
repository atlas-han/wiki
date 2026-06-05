---
title: Context Anxiety
type: concept
category: theory
tags: [llm-behavior, context-window, agent]
related: [context-resets-and-compaction, context-engineering, agent-harness-design]
first-seen: anthropic-harness-design-long-running-apps
sources: [anthropic-harness-design-long-running-apps, anthropic-managed-agents]
created: 2026-05-25
updated: 2026-05-25
---

# Context Anxiety

LLM 에이전트가 **context limit이 가까워졌다고 *느끼면*** 작업을 조기에 마무리하는 행동 패턴. [[anthropic-harness-design-long-running-apps]]와 [[anthropic-managed-agents]] 두 글에서 명명·진단.

## 행동 양상

- 자신의 context 한계를 의식하기 시작하면, 의미 있는 진전이 가능한 상황에서도 "wrapping up" 모드로 전환
- 결과: 장기 task에서 미완으로 종료되거나, 다음 단계 직전에 자기 진행을 요약·종결

## 영향 받은 모델

| 모델 | 정도 |
|---|---|
| [[claude-sonnet-4-5]] | **강함** — compaction만으로는 부족. [[context-resets-and-compaction|context reset]]이 essential. |
| [[claude-opus-4-5]] | 거의 사라짐 — reset이 dead weight화. |
| [[claude-opus-4-6]] | 자체 해결됨 + 더 긴 일관된 작업 가능 (DAW 빌드 2시간 7분 연속) |

> [Opus 4.6] plans more carefully, sustains agentic tasks for longer, can operate more reliably in larger codebases.

## Harness 설계와의 관계

- **Compaction**은 진행 중 conversation을 요약해 history를 짧게 줄임. 그러나 *동일 agent*가 계속 가니까 anxiety는 여전.
- **Context reset**은 context를 비우고 fresh agent + 구조화된 handoff로 재시작. Anxiety가 잡힘. 대가: handoff artifact의 state 충실성 + orchestration 복잡도 + 토큰 overhead + latency.

이 두 가지는 [[context-resets-and-compaction]] 페이지에서 비교.

## 시사점

Harness가 인코딩한 가정의 대표 사례. *Sonnet 4.5에 대해서는 옳던 것*이 *Opus 4.6에서는 dead weight*. 매 모델 출시마다 stress test해야 함 → [[agent-harness-design]].

## References

- [[anthropic-harness-design-long-running-apps]]
- [[anthropic-managed-agents]]
- [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
