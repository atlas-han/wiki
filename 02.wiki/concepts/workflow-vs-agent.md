---
title: 워크플로 vs 에이전트 — 미리 정의된 경로와 동적 루프 (Workflow vs Agent)
type: concept
category: theory
tags: [agents, workflow, loop, tool-use, definition]
aliases: [워크플로와 에이전트의 구분, 에이전트 루프, 동적 결정]
related: [dynamic-workflows, agent-harness-design, three-tier-ai-skill-stack, ai-engineer-vs-ml-researcher, agent-distributed-systems, ralph-wiggum-method]
first-seen: tech-bridge-ai-engineer-three-tier-skill-stack
sources: [tech-bridge-ai-engineer-three-tier-skill-stack]
created: 2026-09-16
updated: 2026-09-16
---

# 워크플로 vs 에이전트

**워크플로는 미리 정의된 경로(A → B → C)를 따르고, 에이전트는 다음에 무엇을 할지 동적으로 결정한다 — 도구를 호출하고, 결과를 관찰하고, 루프를 돈다. 그 루프를 안정적으로, 대규모로 만드는 것이 AI 엔지니어의 일이다.** [[cedric-clyburn|Cedric Clyburn]]([[ibm|IBM Technology]])이 [[tech-bridge-ai-engineer-three-tier-skill-stack]]에서 세운 구분. **이 위키에 워크플로/에이전트의 정의가 나란히 놓인 첫 자리**다.

## 정의

> 간단히 구분하자면, **워크플로는 일반적으로 미리 정의된 경로를 따릅니다.** 서로 다른 행동이 일어나기 때문에 A단계, B단계, C단계가 있는 거죠. **하지만 에이전트는 조금 다릅니다. 에이전트는 다음에 무엇을 할지 동적으로 결정할 수 있습니다.** 필요한 도구를 호출하고, 그 결과를 관찰하고, 그것을 바탕으로 **루프를 돌며** 결정을 내립니다. (07:21~07:46)

> **이 루프를 만드는 것이 정말 중요한데, 이것을 안정적으로, 대규모로 해낼 수 있는 사람이 바로 좋은 AI 엔지니어이기 때문입니다.** (07:46~07:53)

| | 워크플로 | 에이전트 |
|---|---|---|
| 경로 | **미리 정의** | **실행 중 결정** |
| 단위 | 단계 | **루프**(호출 → 관찰 → 결정) |
| 엔지니어의 일 | 경로 설계 | **루프의 안정성·규모** |

에이전트의 값이 *"질문에 답하는 것을 넘어 실제로 일을 처리"*(07:11~07:16)라는 것도 같은 대목에서 나온다.

## 이 위키의 "workflow"와의 관계

이 위키에서 *워크플로* 는 [[dynamic-workflows]] — **에이전트들을 결정론적으로 조율하는 스크립트** — 로 먼저 들어왔다. 이 페이지의 정의로 보면 그것은 **바깥은 워크플로(미리 정의된 조율), 안은 에이전트(각 노드가 루프)** 인 구조다. 즉 두 개념은 **배타적이 아니라 층이 다르다** — [[anthropic]] Claude Code 팀이 *"fan-out의 병목은 reduce"* 라고 한 것은 정확히 워크플로 층의 문제였다.

[[agent-harness-design]]이 다루는 것이 *루프를 안정적으로 만드는 일* 이고, [[ralph-wiggum-method]]는 **루프 자체를 워크플로처럼 고정**한 극단(같은 프롬프트를 반복)이다. 이 페이지는 그 스펙트럼의 **양 끝 이름**이다.

## ⚠️ 유보

- **"안정적으로, 대규모로"의 기준**이 없다 — 무엇이 불안정한 루프인지(무한 루프·도구 오류·컨텍스트 소진)를 소스가 열거하지 않는다.
- 이 위키의 [[verification-cost-asymmetry]]가 말하는 *루프의 종료 조건(검증)* 이 이 정의에는 빠져 있다 — *결과를 관찰* 까지만 있다.
- 입문용 정의라 **하이브리드**(워크플로 안의 에이전트, 에이전트가 만드는 워크플로)를 다루지 않는다.

## References

- [[tech-bridge-ai-engineer-three-tier-skill-stack]] — first-seen
- [[cedric-clyburn]] · [[ibm]]
- 관련: [[dynamic-workflows]] · [[agent-harness-design]] · [[ralph-wiggum-method]] · [[three-tier-ai-skill-stack]]
