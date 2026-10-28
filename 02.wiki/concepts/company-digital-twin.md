---
title: "회사의 디지털 트윈 (Company Digital Twin) — 회사를 행동 시퀀스로"
type: concept
category: technique
tags: [digital-twin, counterfactual, simulation, sequence-modeling, merchants, business-ai]
aliases: [디지털 트윈, digital twin of the company, 회사 시뮬레이션, counterfactual interventions, 반사실적 개입]
related: [model-mixing-economics, agent-roi-measurement, automated-ai-research]
first-seen: tech-bridge-parakhin-shopify-ai-cost-barbell
sources: [tech-bridge-parakhin-shopify-ai-cost-barbell]
created: 2026-10-28
updated: 2026-10-28
---

# 회사의 디지털 트윈 (Company Digital Twin)

**회사를 행동의 시퀀스로 표현해 다음 행동을 예측하는 모델을 만들고, 실제 회사 대신 그 모델에 개입해 결과를 보는 방법이다.** [[mikhail-parakhin|Parakhin]]([[shopify|Shopify]])이 [[tech-bridge-parakhin-shopify-ai-cost-barbell]]에서 설명했다. 이 위키에서 LLM의 **다음 토큰 예측**을 조직 행동에 옮긴 첫 사례다.

> *"The you know how text is just sequence of letters and LLMs learn really well how to predict the next (…) You can represent a company as a sequence of actions."*(03:19~03:36)

## 구조 (발화 기준)

1. **표현** — 신용 한도 개설 · 제품 출시 · 카드 결제 수락 · 대출 같은 큰 변화부터 직원의 매 순간 행동까지 전부 행동 시퀀스로 만든다(03:36~03:57).
2. **트윈** — *"you can create a digital twin of the company. And then you can start doing things to it instead of to real company"*(03:59~04:06)
3. **반사실적 개입** — 광고 캠페인을 하면? 배송이 하루 빨라지면? 대출을 주면? *"we find sequence of interactions that would maximize their chances of growth."*(04:08~04:26)
4. **운영 실행** — *"we we actually do that in production"*(04:28~04:30). 대출 제안, 배송 가속 권유, 광고 캠페인.

화자가 꼽는 가치는 *"play with a company without endangering anything, you know, real people"*(04:50~04:55)이다.

## 이 위키와의 연결

- [[automated-ai-research]]의 *발견 루프*와 같은 모양이다. 실제 대상 대신 싼 대리물 위에서 많이 시도하고, 고른 것만 현실에 적용한다. 차이는 대리물이 **학습된 시퀀스 모델**이라는 점이다.
- [[agent-roi-measurement]]: 같은 화자가 *"very direct impact on our bottom line"* 이라고 하지만 금액도 측정 설계도 말하지 않는다. 에이전트 효과를 무엇으로 재느냐는 그 페이지의 질문이 그대로 남는다.

## ⚠️ 유보

- **당사자 진술 하나뿐**이다. 모델 구조 · 학습 데이터 · 시뮬레이션 결과를 현실과 대조한 검증 방법이 없다. 반사실을 학습된 모델로 추정할 때 생기는 교란(관측된 개입만 학습)도 다루지 않는다.
- 머천트에게 *대출을 권하는* 개입이 누구의 성장을 최대화하는지(머천트 vs 플랫폼)는 발화되지 않는다.

## References

- [[tech-bridge-parakhin-shopify-ai-cost-barbell]] · [[mikhail-parakhin]] · [[shopify]]
