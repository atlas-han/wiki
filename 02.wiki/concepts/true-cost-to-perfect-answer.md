---
title: 완벽한 답까지의 진짜 비용 (True Cost to a Perfect Answer)
type: concept
category: theory
tags: [token-economics, cost, reliability, expected-value, evaluation, token-roles, anthropic]
aliases: [진짜 비용, 예산 나누기 합격률, 기대 실행 횟수]
related: [all-or-nothing-accuracy, fixed-budget-alpha, token-roles, trusted-throughput, overspending-underusing-loop, model-mixing-economics, verification-cost-asymmetry, compute-constrained-growth]
first-seen: tech-bridge-tokens-should-have-jobs
sources: [tech-bridge-tokens-should-have-jobs]
created: 2026-09-18
updated: 2026-09-18
---

# 완벽한 답까지의 진짜 비용

**에이전트의 비용은 한 번 돌리는 데 드는 토큰이 아니라, 쓸 수 있는 답 하나를 얻을 때까지 드는 토큰이다 — 실행당 예산 × 기대 실행 횟수(= 1 / 합격률).** [[angela-jiang|Angela Jiang]]·[[katelyn-lesse|Katelyn Lesse]]([[anthropic|Anthropic]])이 [[tech-bridge-tokens-should-have-jobs]]에서 제시했다.

> 만약 여러분이 완벽한 답을 얻으려고 노력하고 있고, 현실 세계에서 사업을 운영하고 있다면, **그 완벽한 답을 얻는 데 드는 비용**이 중요하다는 것입니다. (08:16~08:25)

## 계산

> 실행 전략을 사용하면 **약 40%의 확률로 완벽한 답**을 얻을 수 있습니다. **평균적으로 세 번 정도 실행**해야 할 것으로 예상되며 (…) **한 번의 실행에 60만 토큰을 사용한다면 대략 세 번** 실행해야 합니다. (…) **평균적으로 180만 개의 토큰**을 소모해야 할 것으로 예상됩니다. (08:29~08:58)

| 전략 | 실행당 예산 | 합격률 | 기대 횟수 | **진짜 비용** |
|---|---|---|---|---|
| 실행 | 600k | ~40% (42%) | ~3 | **1.8M** |
| 조언 · 채점 · 회고 | 600k | *(자막에 없음, 최대 75%)* | *(~1.3)* | *"약간의 차이"* · 조언·채점은 *"상당히 토큰 효율적"* |

> **이것이 바로 해당 에이전트가 해당 전략에 유용하게 사용되기 위해 해당 영역에서 실제로 발생한 비용**입니다. (09:05~09:09)

⚠️ 셋째 줄의 기대 횟수는 *75%* 를 넣은 위키의 계산이다 — **소스는 조언·채점·회고의 수치를 주지 않는다.**

## 왜 이 단위가 다른가

정확도 76 vs 89는 *"미미하다"*([[fixed-budget-alpha]]). 그런데 합격률이 분모에 들어가면 **정확도의 작은 차이가 비용의 큰 차이**가 된다 — 42%면 3회, 75%면 1.3회. 즉 **역할의 알파는 점수에서보다 비용에서 크게 보인다.** 이 계산이 성립하려면 [[all-or-nothing-accuracy|100%/실패 채점]]이 먼저 있어야 한다.

## 처방 — 최적화 대상에 따라 전략이 갈린다

> 어떤 기업들은 *"가장 중요한 것은 **토큰 효율성**"* (…) **조언 유형의 전략**을 (…) 다른 (…) **답변의 신뢰성**이 더 중요하다 (…) **완벽한 답변을 얻는 실행 비율을 극대화** (…) **채점이나 회고** 쪽에 (09:39~10:06)

| 최적화 대상 | 전략 |
|---|---|
| 토큰 효율 (같은 답을 가장 싸게) | **조언** |
| 신뢰성 (완벽한 답의 비율) | **채점 · 회고** |

⚠️ 이 처방의 근거 수치(조언·채점·회고의 합격률과 비용)는 자막에 없다.

## 이 위키에서의 자리

- **[[trusted-throughput]]·[[overspending-underusing-loop]]이 구매자 쪽에서 말한 것을 판매자가 계산식으로 인정했다** — *토큰은 산출물이지 결과가 아니다* → *비용은 토큰이 아니라 결과당 토큰이다*. [[jensen-huang]]의 *백만 토큰당 달러* 와 [[sam-altman]]의 *토큰은 어리석은 단위* 사이에서([[token-roles]]의 G20 절), 이 페이지는 **단위를 바꾸지 않고 분모를 바꾼다.**
- [[model-mixing-economics]]가 *계획은 무거운 모델, 실행은 싼 모델* 을 실행당 비용으로 정당화했는데, 이 단위로 재면 **싼 실행 모델의 합격률이 낮을 때 진짜 비용은 오히려 커질 수 있다** — 소스는 이 연결을 하지 않는다.
- [[verification-cost-asymmetry]] — 합격률을 알려면 검증이 있어야 하고, 검증이 실행만큼 비싸면 이 계산이 무의미해진다.

## 표시해 둔 것

> ⚠️ **재시도가 독립 시행이라는 가정**이 숨어 있다 — 같은 과제를 세 번 돌릴 때 실패가 상관되면(같은 함정에 세 번 빠지면) 기대 횟수는 3보다 크다. 소스는 다루지 않는다. ⚠️ **실패한 실행을 판정하는 비용**(검증 비용)이 식에 없다. ⚠️ 채점·회고는 실행 안에 이미 채점자·드리머의 토큰을 포함하므로 *600k 예산* 안에서 실행자 몫이 줄어드는데, 그 배분은 소스에 없다.

## References

- [[tech-bridge-tokens-should-have-jobs]] · [[angela-jiang]] · [[katelyn-lesse]] · [[anthropic]]
- 관련: [[all-or-nothing-accuracy]] · [[fixed-budget-alpha]] · [[token-roles]] · [[trusted-throughput]] · [[overspending-underusing-loop]] · [[model-mixing-economics]] · [[verification-cost-asymmetry]]
