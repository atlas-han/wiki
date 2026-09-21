---
title: 도구는 중립적 부가물이 아니다 (Tools Are Not Neutral Add-Ons)
type: concept
category: theory
tags: [tooling, scalability, cost, knowledge-work, adoption]
aliases: [도구의 비중립성, 확장 가능성, neutral add-on]
related: [tool-organization-loop, knowledge-agents-vs-coding-agents, oracle-gap, retrieval-primitive-repertoire, build-a-lever, agent-tool-design-practices, true-cost-to-perfect-answer, model-mixing-economics]
first-seen: tech-bridge-knowledge-agents-not-coding-agents
sources: [tech-bridge-knowledge-agents-not-coding-agents]
created: 2026-09-21
updated: 2026-09-21
---

# 도구는 중립적 부가물이 아니다

**도구가 정하는 것은 그 일이 가능한가가 아니라, 그 일이 *할 만한가*다.** 싸지면 규모가 생기고, 규모가 생기면 안 하던 일을 하게 된다.

> **도구라는 건 "아 내 검색이 5% 좋아졌네" 같은 게 아닙니다. 도구가 있느냐 없느냐가 결정하는 것은 그 작업이 가능한가가 아닙니다** — **올바른 도구 없이도 일을 할 수는 있으니까요** — **그 작업이 실제로 확장 가능하고 싸게 수행될 수 있는가입니다. 왜냐하면 싸다는 것은 곧 확장될 수 있다는 뜻이니까요.** — [[benjamin-clavie]], [[tech-bridge-knowledge-agents-not-coding-agents]] (08:01~08:18)

## 세 가지 예

| 도구 | 없을 때 | 있을 때 | 무엇이 바뀌나 |
|---|---|---|---|
| **[피나케스]**(도서관 목록) | 원고 찾기 **2~3주** — *"그 지식이 정말 정말 정말 필요해야 합니다"* | **10분** | *"좀 더 알아야겠네, 검색해 봐야지"* 가 **쉬워진다** |
| **지도** | *"인도로 가는 길에 우연히 아메리카를 발견"* 에 의존 | 어디로 가는지 안다 | **탐험이 합리적 선택이 된다** |
| **멀티모달 검색** | *"그건 아카이브에 있으니 건드리지 않겠어"* | **수백만 PDF를 검색** | **포기했던 사용 사례가 유용해진다** |

(08:18~09:05)

**세 예의 공통 형태는 "가능 → 불가능"이 아니라 "비싸서 안 함 → 싸서 기본값"** 이다.

## 수치로 제시된 대응물

같은 발표가 이 원리를 자기 리더보드 수치로 옮긴다.

> **그 90.2%의 정확도를 20% 더 적은 [툴] 호출로 달성한다는 것입니다.** (…) **토큰 사용량이 20% 줄어드는 것** (…) **그건 사실상 20%의 공짜 현금이나 마찬가지예요.** (10:23~10:37)

> **그러니까 결국 그 일을 할 만한 가치가 있게 만드는 건 도구인 거죠. [25번의 호출]이 필요하다면 아무도 그 도구를 계속 쓰지 않을 겁니다. 하지만 8번의 호출로 해결된다면 "오, 멋지다. 이런 워크플로우를 도입할 수 있겠네"라고 생각하게 될 겁니다.** (10:44~10:54)

**정확도가 같은데 채택 여부가 갈린다** — 이것이 이 페이지의 논지를 가장 압축한 관측이다.

> ⚠️ **수치는 전부 자기 보고이고 측정 조건이 없다.** *"25번 → 8번"* 도 어느 시스템 쌍의 비교인지 자막에 없다. **이 위키는 논지만 받는다.** → [[which-bm25-problem]]

## 이 위키의 비용 논의에 붙는 자리

이 위키는 비용을 **예산 배분** 문제로 다뤄 왔다.

| 페이지 | 무엇을 최적화하나 |
|---|---|
| [[model-mixing-economics]] | 어느 모델에 어느 작업을 |
| [[fixed-budget-alpha]] · [[token-roles]] | 정해진 토큰을 어디에 |
| [[true-cost-to-perfect-answer]] | 완벽에 드는 값 |

**이 페이지는 축이 하나 위다**: 비용이 내려가면 **예산 안에서의 배분이 아니라 무엇을 시도할지의 집합 자체가 바뀐다.** [[build-a-lever]]와 가장 가깝지만, 그쪽은 *레버를 만들어라*(제작자 시점)이고 이쪽은 *레버가 있으면 사람들이 다른 일을 한다*(채택 시점)이다.

## ⚠️ 그리고 도구에 과적합하지 말라는 단서가 붙는다

같은 발표의 마지막이 이 페이지를 스스로 제한한다:

> **도구에 과적합(overfit)해서는 안 됩니다. 도구는 그 자체로 일을 하는 방법으로 존재하는 게 아닙니다. 도구는 천장(ceiling)을 넘어서는 방법으로 존재합니다. 성능이 원하는 곳에 있지 않다는 천장을 볼 때 더 나은 도구를 원하게 되는 겁니다.** (15:44~16:02)

**즉 도구는 중요하되 목적이 아니다 — 천장이 보일 때 꺼내는 것**이고, 어느 천장인지 모르면 도구를 바꿀 이유도 없다. → [[oracle-gap]]이 그 천장을 재는 방법이다.

## References

- [[tech-bridge-knowledge-agents-not-coding-agents]] · [[benjamin-clavie]]
- 상위: [[tool-organization-loop]] · [[knowledge-agents-vs-coding-agents]]
- 관련: [[oracle-gap]] · [[retrieval-primitive-repertoire]] · [[build-a-lever]] · [[agent-tool-design-practices]]
- 비용 축: [[model-mixing-economics]] · [[fixed-budget-alpha]] · [[token-roles]] · [[true-cost-to-perfect-answer]]
