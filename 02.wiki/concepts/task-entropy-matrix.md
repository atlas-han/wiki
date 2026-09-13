---
title: 엔트로피 매트릭스 (Task Entropy Matrix)
type: concept
category: pattern
tags: [task-selection, entropy, verification, acceptance-criteria, information-theory]
aliases: [작업 선정 매트릭스, entropy matrix]
related: [verification-cost-asymmetry, agent-roi-measurement, verifiable-goals, generator-evaluator-pattern, intentional-out-of-distribution, goal-level-delegation, dynamic-workflows]
first-seen: tech-bridge-mousepower-measuring-agents
sources: [tech-bridge-mousepower-measuring-agents]
created: 2026-09-13
updated: 2026-09-13
---

# 엔트로피 매트릭스

**어떤 작업에 에이전트를 붙일지를 두 개의 불확실성 축으로 고르는 틀.** [[maximillian-piras]]가 [[tech-bridge-mousepower-measuring-agents]]에서 제시했다. 바탕은 Claude Shannon의 엔트로피(= 확률 분포의 불확실성)인데, **모델의 성능이 아니라 맡기는 작업**에 적용한다는 것이 요점이다.

> **에이전트를 구축할 때 어떤 작업이 가치 있을까만 생각해서는 부족하고, 그 작업을 수행하는 단계에 불확실성이 얼마나 있는지도 생각해야 합니다.**

## 축 1 — 작업 단계의 불확실성

| 수준 | 판정 |
|---|---|
| **낮음** | 경로가 예측 가능하다 → ***"왜 토큰을 낭비합니까, 그냥 스크립트를 쓰세요."*** |
| **높음** | 정보가 예측 불가능 → **사전학습에서 분포 밖(out of distribution)일 위험 + 강화학습 보상이 희소** → 에이전트에 맞지 않는다 |

예시는 양 끝뿐이다 — **항공권 예약**(출발지·도착지·좌석이 반드시 있어야 완료된다)과 **걸작 그리기**(단계를 아무도 모른다).

## 축 2 — 수용 기준의 불확실성

> **에이전트가 그 작업을 할 수 있는가만이 아니라, 그것이 어떻게 채점되는지에 대한 깨끗한 루브릭이 실제로 있는가.**

| 수준 | 판정 |
|---|---|
| **낮음** | 검증이 싸다 → 반복 가능한 검증 패턴을 만들 수 있다 |
| **높음** | **검증이 실행과 구분되지 않는다** → *"사람이 그 일을 다시 해야 한다면 왜 에이전트를 만듭니까"* → 토큰 낭비 |

## 스위트 스팟

가운데 — **스크립트로 쓸 만큼 뻔하지도, 훈련 분포 밖일 만큼 낯설지도 않으면서, 가치 확인이 상대적으로 쉬운** 작업. 모양이 정해져 있다 → [[verification-cost-asymmetry]].

## 위키의 다른 페이지와의 관계

- **[[verifiable-goals]]** — 그 개념이 *작업을 검증 가능하게 만들라* 였다면, 이 매트릭스는 **그렇게 만들 수 없는 작업은 애초에 고르지 말라**고 한다. 한 단계 앞의 결정이다.
- **[[intentional-out-of-distribution]]** — ⚠️ **같은 용어, 반대 방향.** 09-12의 그 페이지는 *분포 밖* 을 창의성의 **처방**으로 썼고, 여기서는 작업 선택의 **회피 기준**이다. **모순이 아니라 층이 다르다** — 그쪽은 출력의 다양성, 이쪽은 작업의 학습 가능성.
- **[[goal-level-delegation]]** · **[[dynamic-workflows]]** — 무엇을 얼마나 위임할지의 판단에 **두 번째 축(채점 가능성)** 을 더한다.
- **[[fuzzy-intent-discovery]]** — 수용 기준이 불확실한 경우의 다른 처방(사람에게 의도를 캐묻기)이 있다. 이 매트릭스는 **그 비용이 실행 비용을 넘으면 하지 말라**고 한다.

## 표시해 둔 것

> ⚠️ **축에 단위도 임계값도 없고, 스위트 스팟의 구체적 사례가 한 건도 없다.** 화자가 **시간 초과**로 끝을 서둘렀고, 스스로 *"생각의 출발점이고 아직 작업 중"* 이라고 말한다.

## References

- [[tech-bridge-mousepower-measuring-agents]] · [[verification-cost-asymmetry]] · [[verifiable-goals]] · [[agent-roi-measurement]] · [[maximillian-piras]]
