---
title: Context Resets vs. Compaction
type: concept
category: technique
tags: [context-window, agent, context-engineering]
related: [context-anxiety, context-engineering, agent-harness-design]
first-seen: anthropic-harness-design-long-running-apps
sources: [anthropic-harness-design-long-running-apps, anthropic-managed-agents]
created: 2026-05-25
updated: 2026-05-25
---

# Context Resets vs. Compaction

장기 에이전트 task가 context window를 초과할 때 쓰는 두 가지 기본 전략과 그 한계.

## Compaction

- *동일 agent*의 conversation 초반부를 in-place 요약 → 짧아진 history로 계속 진행
- 장점: continuity 유지, 단일 세션
- 한계: [[context-anxiety]]를 해소 못 함 — agent는 여전히 자기 한계에 가까이 있다고 *느낌*

## Context Reset

- Context를 *완전히* 비우고 fresh agent로 시작
- **Structured handoff artifact**가 이전 agent의 state와 다음 step을 전달
- 장점: 깨끗한 시작, anxiety 제거
- 비용: handoff artifact 품질 (state 충실성), orchestration 복잡도, 토큰 overhead, latency

[[anthropic-harness-design-long-running-apps]]에서 [[claude-sonnet-4-5]]의 anxiety가 강해 context reset이 essential이었으나, [[claude-opus-4-5]]에서 anxiety가 자체 해결되어 reset을 drop. [[claude-opus-4-6]]에서는 sprint construct까지 drop 가능.

## Managed Agents의 Third Way — Session as External Context Object

[[anthropic-managed-agents]]는 다른 접근을 제시:

- Session log를 **context window 밖**에 durable storage로 둔다.
- `getEvents()`로 **positional slice**를 가져옴 — 특정 시점 직전으로 rewind, 특정 action 직전 재독, 마지막 지점에서 resume 등.
- Harness가 fetched events를 자유롭게 transform (prompt cache 히트율 최적화, [[context-engineering]] 적용).
- *Irreversible*한 compaction/trimming 결정을 미룰 수 있음 — 필요할 때 원본을 다시 본다.

> It is difficult to know which tokens the future turns will need.

관련 idea: REPL 안에 context를 *object*로 두고 LLM이 코드로 슬라이스하는 패턴 ([arXiv:2512.24601](https://arxiv.org/pdf/2512.24601) 인용).

## 메타 원리

세 가지 모두 *harness가 인코딩한 가정*에 따라 선택지가 바뀐다. 자세한 패턴: [[agent-harness-design]].

## References

- [[anthropic-harness-design-long-running-apps]]
- [[anthropic-managed-agents]]
- [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
