---
title: 예산 고정 알파 (Fixed-Budget Alpha)
type: concept
category: technique
tags: [evaluation, benchmark, token-budget, test-time-compute, methodology, token-roles, anthropic]
aliases: [예산을 고정하고 비교하라, 역할의 알파]
related: [token-roles, true-cost-to-perfect-answer, all-or-nothing-accuracy, strategy-primitives, generator-evaluator-pattern, skill-evals, model-mixing-economics]
first-seen: tech-bridge-tokens-should-have-jobs
sources: [tech-bridge-tokens-should-have-jobs]
created: 2026-09-18
updated: 2026-09-18
---

# 예산 고정 알파

**전략(토큰 역할 배치)이 정말 효과가 있는지 알려면 토큰 예산을 고정하고 비교해야 한다 — 테스트 타임 컴퓨트가 전부라면 같은 예산의 전략들은 같은 점수여야 하고, 남는 차이가 알파다.** [[katelyn-lesse|Katelyn Lesse]]·[[angela-jiang|Angela Jiang]]([[anthropic|Anthropic]])이 [[tech-bridge-tokens-should-have-jobs]]에서 세 전략을 비교하며 쓴 방법.

## 왜 필요한가 — one-shot은 지출을 스스로 정한다

> 단발성이었기 때문에 **전략이 실제로 얼마나 많은 토큰을 사용할지 스스로 결정**할 수 있었습니다. 그래서 실행이 (…) **39,000개**만 사용하기로 결정했다는 것을 알 수 있습니다. (…) **회고가 정말 좋은 성적을 낸 건 맞지만, 그 성과를 내기 위해 무려 60만 개의 토큰을 사용했으니까요.** (04:54~05:18)

전략마다 지출이 다르면(15%/39k vs 회고/600k) 점수 차이가 **역할의 효과인지 지출의 효과인지** 구분되지 않는다.

## 방법

> **실제로 역할을 다양화하는 것이 알파를 생성하는지 알아내려면 예산을 일정하게 유지해야 합니다.** 이를 위해 우리는 **회고 전략의 예산, 즉 약 60만 토큰을 모든 전략에 일괄적으로 고정된 최대 예산**으로 삼겠습니다. (05:20~05:32)

귀무가설이 명시된다:

> **만약 그것(테스트 타임 컴퓨트)만이 유일하게 중요한 요소라면, 동일한 예산이 주어졌을 때 실행, 조언, 채점, 회고 모두가 정확히 같은 수준이어야 할 것입니다.** (05:56~06:04)

결과:

| | one-shot (자율 지출) | 고정 60만 |
|---|---|---|
| 실행 | **15%** (39k) | **76** |
| 조언 | *(수치 없음)* | **89** |
| 조언·채점 | *(수치 없음)* | *"60점대 → 90에 가깝게"* |
| 회고 | *"정말 잘했다"* (600k) | *(수치 없음)* |

> **실행을 살펴보면 76에 도달하지만, 조언은 89** 입니다. 따라서 **미미한 차이이긴 하지만, 분명히 존재**하며 (…) (06:13~06:22)

## 이 위키에서 이 방법이 값진 이유

- **[[token-roles]]의 첫 실험적 근거**다. 09-01의 *Sonnet + Opus* 주장은 *"우리가 본 몇몇 eval"* 이었는데, 이번엔 **통제 조건**(고정 예산)이 있다.
- [[skill-evals]](Lauren Tan)·[[generator-evaluator-pattern]]의 eval playbook들이 *무엇을 재는가* 를 다뤘다면, 이 방법은 **무엇을 고정하는가**를 다룬다 — 에이전트 eval에서 **토큰 지출이 교란 변수**라는 점을 명시한 첫 소스다.
- [[model-mixing-economics]]가 *계획은 무거운 모델, 실행은 싼 모델* 을 **예산** 논리로 정당화했는데, 그 주장도 이 방법으로 검증돼야 한다 — 같은 예산에서 혼합이 단일 모델을 이기는가.

## 표시해 둔 것

> ⚠️ **고정 예산이 가장 많이 쓴 전략(회고)의 지출이다** — 위로 맞췄다. 실행에 60만을 주면 그 전략이 예산을 어떻게 쓰는지(더 많은 시도? 더 긴 추론?) 소스가 말하지 않는다.
>
> ⚠️ **화자 스스로 차이가 "미미하다"고 말한다.** 76 vs 89가 과제 몇 개에서 나온 것인지, 분산이 어떤지 없다. **채점·회고의 고정 예산 점수는 자막에 없다.**
>
> ⚠️ 그래서 이 방법이 두 번째 렌즈([[all-or-nothing-accuracy]])로 이어진다 — 정확도로는 차이가 작아 보이는데 **합격률과 진짜 비용으로 재면 커진다**([[true-cost-to-perfect-answer]]).

## References

- [[tech-bridge-tokens-should-have-jobs]] · [[katelyn-lesse]] · [[angela-jiang]] · [[anthropic]]
- 관련: [[token-roles]] · [[true-cost-to-perfect-answer]] · [[all-or-nothing-accuracy]] · [[strategy-primitives]] · [[generator-evaluator-pattern]] · [[skill-evals]] · [[model-mixing-economics]]
