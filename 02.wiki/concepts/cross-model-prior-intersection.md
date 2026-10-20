---
title: "교차 모델 prior 교집합 (Cross-Model Prior Intersection)"
type: concept
category: technique
tags: [model-priors, silent-data-errors, correlated-errors, model-diversity, verification, ensemble, data-engineering, human-in-the-loop]
aliases: [cross-model prior intersection, prior intersection, 모델 prior, 모델의 사전 가정, 조용한 데이터 오류, silent data errors, LLMs as a species]
related: [just-in-time-ontology, generator-evaluator-pattern, cross-lab-peer-review, model-calibration, verification-bottleneck, verification-cost-asymmetry, system-1-model, ai-slop, three-level-agent-review]
first-seen: tech-bridge-just-in-time-ontology
sources: [tech-bridge-just-in-time-ontology, tech-bridge-three-level-agent-review]
created: 2026-10-18
updated: 2026-10-20
---

# 교차 모델 prior 교집합 (Cross-Model Prior Intersection)

**모델은 작업마다 "세상이 어때야 하는가"에 대한 prior를 가져오고, 그 prior가 데이터와 어긋나면 조용한 오류가 생긴다. 사람이 결과를 확인하는 것은 사람의 prior와 모델의 prior를 교차시키는 일이고, 계열이 다른 모델끼리도 같은 일을 할 수 있다.** 두 모델이 일치한 답은 믿고 불일치한 답에 검증을 몰아준다. [[hrishi-olickel|Hrishi Olickel]]이 [[tech-bridge-just-in-time-ontology]]에서 이름 붙였다.

> *"Just like humans, models bring their own priors, their beliefs about what should be in the world to every task. This is the fourth schema that I mentioned before, the one the model brings with it."* (13:57~14:07)
>
> *"it turns out you can also get really far with cross-model prior intersection. On our 200 held-out families, Jev and Luna agreed on 194. And none of those shared answers was wrong. Every error sat in the six families where they disagree."* (15:45~16:01)

## 문제 — prior가 만드는 조용한 오류

| 사례 | 무슨 일이 | 결과 |
|---|---|---|
| in-kind 표기 | 파이프라인은 밑줄 표기를 찾았고 파일은 대문자 I + 하이픈이었다 | 현물 기부 15,658건을 일반 돈으로 셈, 대출 상환도 같은 식으로 사라짐(14:20~14:36) |
| 날짜 형식 | 날짜 형식 넷을 시도했는데 파일은 다섯째를 썼다 | 거래일 99.4%가 비었지만 행 수·금액 합계가 맞아 에이전트가 넘어감(14:37~14:50) |
| 대출 부호 | 음수 대출액의 부호를 중복으로 판단해 절댓값 저장 | 순액 784,000이 부채 $5.3M이 됨, *"validated by multiple models"*(14:50~15:05) |

- *"Bigger models, in a strange way, are worse at this sometimes. They hold onto their beliefs and argue for them even more vehemently."*(14:10~14:16)
- *"this is quickly becoming the largest class of error I see across companies at Data Work as models take over."*(15:07~15:12)
- 행 수·합계 같은 **집계 검사를 통과하는 오류**라는 점이 공통이다(날짜 사례).

## 처방 — prior를 교차시킨다

1. **사람.** *"Sometimes you can solve this just by not vibing, by checking results and applying human intuition. (…) You're intersecting your priors with the models."*(15:12~15:25) 단 사람은 *"expensive (…) slow, they pause timelines, they're even more non-deterministic than models, and they hate interruptions."*(15:34~15:44)
2. **다른 계열의 모델.** *"Models from different families, different pedigrees, tend to disagree more and have different priors than models in the same group."*(16:01~16:08) 예외로 *"models that are distilled outside the same company"*(16:12~16:15, ⚠️ 판독 보류, 대상 미지목)를 든다.
3. **종 수준 오류는 목록으로.** 교차로 줄인 뒤에도 *"a much smaller but persistent class of problems that apply to LLMs as a species"*(16:20~16:24)가 남는다. *"in one benchmark, four different model families produced the same total down to the cent because they all shared a sign convention that the answer key didn't."*(16:26~16:34) 처방은 *"list them, look out for them, and apply specific solutions."*(16:37~16:40)

## 위키의 다른 페이지와

- [[generator-evaluator-pattern]]: 평가자가 생성자와 같은 prior를 공유하면 검증이 무력하다. 대출 부호 사례는 여러 모델이 *validated*한 오류다. 평가자를 **다른 계열**에서 고르라는 조건이 붙는다.
- [[cross-lab-peer-review]]: 랩끼리 출시 전 모델을 검증하자는 거버넌스 제안이다. 여기서는 데이터 파이프라인의 한 단계에서 랩이 다른 모델을 교차시킨다. 층은 다르지만 "다른 출신이 다른 맹점을 본다"는 가정이 같다.
- [[model-calibration]]: 한 모델의 확률이 보정돼 있어도 prior가 틀리면 자신 있게 틀린다. Jev의 *"confidently said no"*(11:31~11:33) 참조.
- [[verification-cost-asymmetry]]: 불일치에만 검증을 몰아주면 검증 단가를 낮출 수 있다. 그래도 오하이오 사례의 검증 총액은 첫 답의 약 4배였다.
- [[ai-slop]]: *"not vibing"*.

## ⚠️ 유보

- 194/200은 한 사례의 held-out 세트다. Luna가 어느 회사의 어떤 모델인지 발화되지 않는다([[tech-bridge-altman-devday-dots]]에 같은 이름이 미판독 모델명으로 있다).
- "four different model families" 벤치마크의 이름·계열은 발화되지 않는다.
- 일치 = 정답은 이 세트의 결과다. 대출 부호·네 계열 사례처럼 일치한 오답도 있다.

## References

- [[tech-bridge-just-in-time-ontology]] — first-seen
- [[hrishi-olickel]] · [[jev]]
- 관련: [[just-in-time-ontology]] · [[generator-evaluator-pattern]] · [[cross-lab-peer-review]] · [[model-calibration]] · [[verification-cost-asymmetry]] · [[ai-slop]]

## 같은 지시의 두 에이전트 + 원문 control total은 충분한가 (2026-10-20 · [[tech-bridge-three-level-agent-review]])

> ⚠️ Contradiction(긴장): [[corey-gallon|Corey Gallon]](⚠️ 이름 *추정*)의 Level 2는 **같은 지시**를 받은 에이전트 둘이다(*"two agents get an identical set of instructions"* 02:15~02:17, *"two more agents, tasked identically"* 08:12~08:15). 모델 다양성은 발화되지 않는다. 성공의 증거도 *"the whole year balanced to the penny"*(08:43~08:45)다. 이 페이지는 여러 모델이 같은 오류를 *"validated"*하고 1센트까지 같은 합계를 내도 공통 prior는 남는다고 했다. 화자의 방어는 합계를 **모델끼리가 아니라 원문과** 맞춘다는 것이다: *"we use the balance printed on the statements as the control total for each month"*(07:50~07:55), 차이는 *"against the statements themselves"*(08:09~08:11)로 정리한다. 남는 구멍: 월 잔액은 같은 달 안의 분류·설명 오류를 잡지 못하고, 두 에이전트가 같은 prior로 같은 오독을 하면 대조자에게 차이로 보이지 않는다. 화자는 56개 차이를 잡았다고 하지만(08:37~08:42) 함께 틀린 것에 대해서는 말하지 않는다. 해소하지 않는다. → [[three-level-agent-review]]
