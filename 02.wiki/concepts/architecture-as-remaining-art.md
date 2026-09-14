---
title: 남은 예술로서의 아키텍처 (Architecture as the Remaining Art)
type: concept
category: framing
tags: [architecture, code-quality, coding-agents, design, substrate]
aliases: [코드는 싸고 품질은 비싸다, 기반이 나쁘면 기여도 나쁘다]
related: [organic-architecture, shortest-path-architecture, decision-quality, ambitious-software, code-is-the-product, learning-curve-as-feature]
first-seen: tech-bridge-ambitious-software-agent-era
sources: [tech-bridge-ambitious-software-agent-era]
created: 2026-09-14
updated: 2026-09-14
---

# 남은 예술로서의 아키텍처

**코드 작성이 자동화되고 남은 잔여가 아키텍처다.** 그리고 **그 잔여가 나머지 전부의 품질을 결정한다.**

> **코드 아키텍처는 여전히 예술입니다.** 코딩 에이전트는 예외적으로 높은 속도로 배포하게 해 주는데, **여러분의 코딩 에이전트가 착지하는 기반(substrate)이 나쁘면 그들의 기여도 나쁠 것입니다.** — [[tech-bridge-ambitious-software-agent-era]] (15:50~16:08)

> **지금 우리 개발 시간의 대부분은 실제로 소프트웨어 아키텍처, 앞으로 원할 기능, 시스템이 어떻게 진화할지를 생각하는 데 쓰입니다.** (16:18~16:27)

> **인간 엔지니어가 스파게티 코드를 쓸 수 있듯 에이전트도 쓸 수 있습니다 — 다만 이제 더 빠르게요.** (16:27~16:33)

## 에이전트의 성질 하나가 양날이다

> **인간 엔지니어와 달리 코딩 에이전트는 기능이 잘 안 맞을 때 시스템을 통째로 리팩터하거나 아키텍처를 다시 설계하는 걸 자발적으로 하는 데 대체로 두려움이 없습니다. 대개 그냥 배포해 버립니다.** (16:08~16:18)

**두려움 없음**은 좋은 기반 위에서는 자산이고(사람이 미루던 리팩터가 실제로 일어난다), **나쁜 기반 위에서는 가속기**다. 이것이 [[organic-architecture]]가 말한 것과 정확히 같은 자리다 — 가드레일 없는 코드베이스는 **편의에 최적화되며 번져 나간다.**

## 미래 예측 — 그리고 그 조건

> **[[fable-5-1|Fable]] 급 도구라면, 의도를 제대로 전달하는 한 실제 코드 품질 자체가 아주 높아서, 앞으로는 제대로 된 소프트웨어 아키텍처가 시간의 압도적 대부분을 차지하게 될 것입니다. 실제 코드 작성은 그렇지 않고요.** (16:34~16:47)

조건절이 중요하다 — ***"의도를 제대로 전달하는 한"***. 소스는 곧바로 **그 조건이 아직 충족되지 않는다**고 말한다:

> **코딩 에이전트가 우리 마음을 읽을 수 있는 지점에는 아직 못 왔고, 우리는 여전히 텍스트라는 매체에 갇혀 있습니다.** 우스꽝스럽게 들릴지 몰라도 **프롬프트 엔지니어링은 실제로 존재합니다. 구현의 품질은 모델에게 주는 프롬프트에 크게 좌우될 수 있습니다.** (17:28~17:44)

→ [[context-engineering]] · [[steering-altitude]]

## 결론 문장

> **코드는 이제 싸지만, 품질은 그렇지 않습니다.**
>
> **소프트웨어 엔지니어의 일은 한 번도 화면에 코드 줄을 얹는 것이었던 적이 없습니다. 그것은 복잡한 문제에 우아한 해법을 설계하는 것, 시스템이 어떻게 진화할지 열 단계 앞을 생각하는 것, 요구사항이 바뀌는 상황에서 유연성을 유지하는 것이었습니다. 이 사실들은 바뀌지 않았고, 소프트웨어 엔지니어링의 기준은 그 어느 때보다 높아졌습니다.** (17:58~18:27)

> **코드를 읽는 것은 언제나 코드를 쓰는 것보다 중요했습니다.** (17:45~17:49)

## 위키의 같은 자리들

| 소스 | 표현 |
|---|---|
| [[tech-bridge-ai-era-code-quality]] (09-08) | **구현 품질↓ 결정 품질↑** — 평가의 자리가 옮겨갔다 → [[decision-quality]] |
| [[tech-bridge-lauren-tan-trusting-agents]] (09-12) | *"가장 짧은 경로가 가장 좋은 경로"* → [[shortest-path-architecture]] |
| **이 개념** (09-13) | **아키텍처는 자동화되지 않은 잔여이고, 그 잔여가 나머지의 품질을 정한다** |

**셋이 같은 방향을 가리키되 자동화의 정도를 다르게 잡는다.** IBM은 *작성자 신뢰 → 행동 검증* 으로 갔고, 여기서는 **여전히 사람이 모든 PR을 읽는다.**

## References

- [[tech-bridge-ambitious-software-agent-era]] · [[jonathan-kelley]] · [[dioxus]] · [[fable-5-1]]
- 관련: [[organic-architecture]] · [[shortest-path-architecture]] · [[decision-quality]] · [[ambitious-software]] · [[code-is-the-product]] · [[context-engineering]] · [[steering-altitude]] · [[learning-curve-as-feature]]
