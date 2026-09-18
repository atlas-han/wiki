---
title: 100%가 아니면 0 (All-or-Nothing Accuracy)
type: concept
category: framing
tags: [evaluation, accuracy, pass-fail, expert-work, finance, verification, token-roles, anthropic]
aliases: [80%는 쓸모없다, 완벽 합격 채점, 합격률 렌즈]
related: [verification-cost-asymmetry, true-cost-to-perfect-answer, fixed-budget-alpha, task-entropy-matrix, trusted-throughput, verification-bottleneck, generator-evaluator-pattern, token-roles]
first-seen: tech-bridge-tokens-should-have-jobs
sources: [tech-bridge-tokens-should-have-jobs]
created: 2026-09-18
updated: 2026-09-18
---

# 100%가 아니면 0

**어떤 전문가 작업에서는 80% 정확한 답이 0% 정확한 답과 같다 — 전문가가 어차피 다시 해야 하기 때문이다. 그래서 채점을 부분 점수가 아니라 완벽/실패로 바꾼다.** [[angela-jiang|Angela Jiang]]([[anthropic|Anthropic]])이 [[tech-bridge-tokens-should-have-jobs]]에서 재무 분석 벤치의 두 번째 렌즈로 제시했다.

> 만약 벤치에서 **80%의 정확도**를 보였다면 훌륭해 보일 수 있지만, 실제로는 **전문가가 직접 손익계산서를 다시 계산하거나 수정하거나, 아니면 재실행을 해야 한다**는 것을 의미합니다. 왜냐하면 이러한 유형의 업무에서는 **100% 정확하지 않으면 사실상 쓸모가 없기 때문**입니다. **수입이나 비용을 마음대로 지어낼 수는 없습니다. 100% 정확해야 합니다.** (06:51~07:14)

> 우리 실험이 **만점을 받으면 합격**을 줄 수 있는 구조를 갖추도록 (…) **100% 미만의 점수를 받았다면, 우리는 그것을 실패로 간주**할 것입니다. (07:23~07:34)

## 렌즈를 바꾸면 수치가 바뀐다

| 렌즈 | 실행 | 더 복잡한 전략 |
|---|---|---|
| 정확도 (고정 예산) | 76 | 조언 89 — *"미미한 차이"* |
| **합격률 (100% 기준, 고정 예산)** | **42%** | **최대 75%** |

같은 실험, 같은 예산인데 **차이의 크기가 달라진다.** 부분 점수는 *거의 맞은* 답을 후하게 세고, 합격률은 그것을 0으로 센다 — 그리고 전문가 작업의 현실은 후자다.

## 이 위키의 명제와 만나는 자리

**[[verification-cost-asymmetry]]와 같은 결론을 판매자 쪽에서 냈다.** [[maximillian-piras]]([[yutori]], 09-13):

> **사람이 그 일을 다시 해야 한다면, 그 일에 왜 에이전트를 만듭니까.**

이 페이지의 화자:

> **전문가가 직접 손익계산서를 다시 계산해야 한다 (…) 100% 정확하지 않으면 사실상 쓸모가 없다.**

같은 문장인데 쓰임이 다르다 — Piras는 **작업을 고르는 기준**(비대칭이 없으면 만들지 마라)으로, Anthropic은 **채점 방식**(그러니 100% 아니면 실패로 세라)으로 쓴다. 두 소스는 서로를 언급하지 않는다. [[task-entropy-matrix]]의 축(수용 기준의 불확실성)으로 보면 P&L은 **수용 기준이 완전히 확정된 작업**이라 채점이 가능하고, 그래서 이 렌즈가 성립한다 — **수용 기준이 흐린 작업에는 이 렌즈를 쓸 수 없다.**

[[trusted-throughput]]이 *신뢰할 수 있는 처리량* 만 세라고 했던 것의 **벤치 버전**이기도 하다 — 신뢰할 수 없는 답은 처리량이 아니다.

## 귀결 — 비용의 분모가 된다

합격률이 정해지면 *쓸 수 있는 답 하나* 까지의 기대 실행 횟수가 나오고, 그것이 [[true-cost-to-perfect-answer]]의 분모가 된다. 이 렌즈 없이는 진짜 비용을 계산할 수 없다.

## 표시해 둔 것

> ⚠️ **누가 100%를 판정하는가**(사람? 채점 모델? 정답 대조?)가 없다. **"최대 75%"가 어느 전략인지** 없다. 그리고 이 렌즈는 **정답이 하나로 확정되는 작업**에만 적용된다 — 소스는 그 조건을 명시하지 않는다.

## References

- [[tech-bridge-tokens-should-have-jobs]] · [[angela-jiang]] · [[katelyn-lesse]] · [[anthropic]]
- 관련: [[verification-cost-asymmetry]] · [[true-cost-to-perfect-answer]] · [[fixed-budget-alpha]] · [[task-entropy-matrix]] · [[trusted-throughput]] · [[verification-bottleneck]] · [[token-roles]]
