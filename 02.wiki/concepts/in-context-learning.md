---
title: In-Context Learning
type: concept
category: theory
tags: [in-context-learning, meta-learning, prompting, gpt-3, activation]
aliases: [인컨텍스트 러닝, ICL, 컨텍스트 내 학습]
related: [transformer, attention-mechanism, context-engineering, token-roles, agent-skills]
first-seen: tech-bridge-karpathy-transformers-stanford
sources: [tech-bridge-karpathy-transformers-stanford]
created: 2026-09-03
updated: 2026-09-03
---

# In-Context Learning

컨텍스트에 주어진 예시만으로 — **가중치를 전혀 바꾸지 않고** — 과제 수행이 개선되는 현상. [[andrej-karpathy|Karpathy]]는 이것이 [[transformer|트랜스포머]]를 특별하게 만드는 핵심이라고 본다.

> 저라면 [GPT-3 논문에] **"트랜스포머는 in-context learning 혹은 meta-learning이 가능하다"** 같은 제목을 붙였을 겁니다. **그게 트랜스포머를 정말 특별하게 만드는 것**이거든요.

(GPT-3 논문의 실제 제목은 *Language Models are Few-Shot Learners*다.)

## 관찰된 현상

프롬프트에 질문-답변 쌍을 하나, 둘, 셋 늘려 넣으면 **정확도가 올라간다.** 파인튜닝은 없었다.

> 트랜스포머가 전형적인 파인튜닝 방식의 **gradient descent를 전혀 하지 않고도 activation 안에서 학습**할 수 있다는 것입니다.

## inner loop / outer loop

이 위키에서 쓸모 있는 어휘. 학습이 두 층위에서 일어난다.

| 루프 | 무엇 | 어디에 저장되나 | 언제 |
|---|---|---|---|
| **outer** | stochastic gradient descent | **가중치** | 학습 시 |
| **inner** | 시퀀스를 읽어나가는 과정 | **activation** | 추론 시, 매 프롬프트마다 |

> 트랜스포머가 시퀀스를 소비하는 동안 **activation 안에서 어떤 학습이 일어나고 있고, 그것이 gradient descent와 아주 비슷해 보일 수 있다**는 겁니다.

## 왜 그럴 수 있는가 (handwavy)

발표자 본인이 "much more handwavy"라고 명시한 직관이다. 확립된 결과로 인용하지 말 것.

> gradient 기반 학습이 뭡니까? **forward pass, backward pass, 그리고 update**입니다. 그런데 그건 **ResNet처럼 보입니다.** 왜냐하면 가중치에 계속 더해 나가는 거니까요. (…) **트랜스포머는 ResNet입니다.**

> ⚠️ 강연은 어떤 논문이 "raw operator"라는 것을 제안하고 그 위에 ridge regression을 구현할 수 있음을 보였다고 언급하지만, **ko·en-orig 자막 모두 이름이 불분명해 논문을 특정할 수 없다.** 확정하지 않는다.

## 이 위키에서의 의미

이 페이지는 다른 소스들이 실무 층위에서 이미 쓰고 있던 것의 **메커니즘 이름**이다.

- [[context-engineering]] — 컨텍스트를 설계하는 일이 왜 학습처럼 작동하는가. inner loop가 그 답이다.
- [[token-roles]] — 컨텍스트에 들어가는 토큰이 왜 역할별로 다른 효과를 내는가.
- [[agent-skills]] — 스킬 파일이 파인튜닝 없이 행동을 바꾸는 것은 inner loop에 프로그램을 넣는 일이다. [[tech-bridge-ai-native-skills]]와 [[tech-bridge-flutter-ai-workflow]]가 다루는 progressive disclosure는 **inner loop에 무엇을 언제 올릴지**의 문제로 다시 읽힌다.
- 그리고 [[transformer]]의 재명명 — *"GPT는 런타임에 재구성되어 **자연어 프로그램**을 실행하는 범용 컴퓨터"* — 은 in-context learning을 "프로그램 로딩"으로 본 것이다.

## 스케일이 inductive bias를 정한다

인접한 Q&A 답변이 [[sutton-bitter-lesson]]의 조건부 버전을 준다.

> **데이터가 무한하면 실제로 점점 더 적게 인코딩하고 싶어지고 그게 더 잘 작동합니다.** 데이터가 아주 적으면 오히려 편향을 좀 인코딩하고 싶어집니다.

넣더라도 코어 트랜스포머가 아니라 **연결성**과 **positional encoding**에 factor out해서 넣는다.

## References

- [[tech-bridge-karpathy-transformers-stanford]]
