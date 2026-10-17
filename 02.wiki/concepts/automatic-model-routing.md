---
title: "자동 모델 라우팅 (Automatic Model Routing)"
type: concept
category: technique
tags: [model-routing, router, cost, reliability, fallback, prompt-caching, open-models, model-selection]
related: [model-mixing-economics, software-factory, overspending-underusing-loop, token-roles, system-1-model, harness-engineering, true-cost-to-perfect-answer]
first-seen: tech-bridge-factory-software-factory
sources: [tech-bridge-factory-software-factory, tech-bridge-kimchi-cost-per-task-harness, tech-bridge-gitar-agentic-pr-validation, tech-bridge-tailscale-aperture-ai-without-lock-in]
created: 2026-10-02
updated: 2026-10-17
---

# 자동 모델 라우팅 (Automatic Model Routing)

**과제마다 사람이 모델을 고르지 않고, 라우터가 과제 난이도를 분류해 "끝낼 수 있다고 예측되는 가장 싼 모델"을 고르고, 실패나 공급자 장애 때 다른 모델로 바꾸는 하네스 기능.** 이 위키에선 [[factory-ai|Factory]]의 같은 이름 기능을 [[tereza-tizkova|Tereza Tížková]]가 설명한 [[tech-bridge-factory-software-factory]]에서 처음 메커니즘째 들어왔다. 라우팅이라는 *흐름*은 [[model-mixing-economics]]에 이미 쌓여 있다(Oracle·Jev·Nadella) — 이 페이지는 **단계별 메커니즘과 받은 질문들**을 모은다.

> ⚠️ **벤더 진술, 독립 검증 없음.** 25% 수치, 분류 정확도, 전환 빈도 모두 Factory 자체 주장이다.

## 4단계 (07:09~08:01)

| 단계 | 내용 (en-orig) |
|---|---|
| ① **할당** | 사용자는 과제를 맡기기만 한다. 조직은 *"give different permissions and different default models to different people"* — 마케팅·영업·엔지니어가 서로 다른 기본 모델(07:16~07:29) |
| ② **분류** ⭐ | *"This is the magic of the routing"* — 프롬프트 구조, 코드베이스, 과제 난이도, 사용 도구를 보고 *"make a classification of difficulty of the task"*(07:31~07:45) |
| ③ **임계값** | *"a threshold of what is enough to accomplish the task"*(07:48~07:54) |
| ④ **선택** | *"you choose the cheapest model above the threshold. So cheapest model that is predicted to accomplish your task"*(07:54~08:01) |

**런타임 전환**: 먼저 최적 모델을 정하고 *"it can switch to different model if it's failing the task or in case of any troubles but it usually doesn't happen"*(06:27~06:34).

## 비용만이 아니다

*"It also helps with reliability or with speed because open source models are often faster and uh if one LM provider fails you can just switch to another one automatically"*(06:41~06:51). 즉 라우터는 **비용 최적화 + 지연 최적화 + 공급자 failover**를 한 층에서 한다.

수치: *"This uh is our benchmark which is very conservative (…) You can save for example 25% but even more probably"*(06:56~07:09). ⚠️ 벤치마크 과제·기준선(전부 프런티어 모델 대비인지)이 발화되지 않는다.

## 받은 질문과 답 (08:04~08:43)

질문: 정말 되나? 모델이 놓치면? 더 느린가? 사실 더 비싼가? 모델이 과제를 못 끝내면, 업그레이드가 필요하면? 캐싱은?

답: *"that's why it's so difficult to build a good router like you need to basically classify it very well and the challenge is to not not to need to switch too often but even if you're switching in the middle of the task to (…) more difficult model you still overall are faster probably"*(08:22~08:40). ⚠️ *"probably"* — 근거 없음.

## 캐싱 — "기술이 아니라 가격 결정"

*"open models can do this as well (…) host open models as well uh on dedicated compute and you can take the same advantage of the caching"*(09:00~09:12). ⭐ *"the final price for users is just a pricing decision. It's not a technical challenge because everyone can do caching. It's just what price you pass on the users and what deals you make with the API providers"*(09:15~09:27).

> ⚠️ **답이 비켜 간 질문.** 청중 질문의 핵심은 아마 *라우터가 모델을 바꾸면 캐시가 깨지지 않느냐*였을 텐데, 화자는 **할인을 주느냐**로 받아 가격 정책으로 답했다. 과제 중간 전환 시 새 모델에서 프리필을 다시 해야 하는 비용은 말하지 않는다. [[tech-bridge-nadella-copilot-autopilot]]은 스웜·서브에이전트에서 *"여러 모델 패밀리를 넘나들며 KV 캐시 적중률"* 을 맞추는 것을 **명시적 난제**로 꼽았다 — 이 페이지는 둘을 긴장으로 둔다.

## 다른 라우터들과의 비교

| | 분류 주체 | 선택 규칙 | 출처 |
|---|---|---|---|
| **Factory** | 라우터(프롬프트·코드베이스·도구로 난이도 분류) | 임계값 위 최저가, 실패 시 전환 | [[tech-bridge-factory-software-factory]] |
| Oracle | 하네스 안 라우터 | (절감액의 10% 과금 모델) | [[tech-bridge-oracle-agent-memory-harness]] |
| Jev | 비-LLM System 1 모델 | 확률 판정 | [[tech-bridge-jev-agent-harness]] · [[system-1-model]] |
| Microsoft Copilot | **learned router** + 자체 MAI 모델 | 과제 강도, *"your agent picks the model"* | [[tech-bridge-nadella-copilot-autopilot]] |
| **Kimchi** ([[cast-ai\|Cast AI]]) | 하네스(*"based on the outcome of the task"*) — 사전 분류 여부 미발화 | 작업당 비용 + 산출물 점수 게이트(B 이상) | [[tech-bridge-kimchi-cost-per-task-harness]] |

공통 결론: **사람이 모델을 고르는 시대가 끝나 간다**(Nadella *"auto has become the product"*). Factory가 덧붙인 것은 **조직 단위의 기본 모델·권한**(①)과 **failover를 라우터의 이점으로 명시**한 것.

## 미해결

- 분류기 자체의 비용·지연, 오분류율.
- *"cheapest model above the threshold"* 의 임계값을 누가·무엇으로 보정하는가.
- 사용자가 모델을 고정할 수 있는가(Coinbase식 기본값 변경과의 관계).
- 전환 시 캐시 손실 비용.

## References

- [[tech-bridge-factory-software-factory]] — first-seen
- [[model-mixing-economics]] · [[software-factory]] · [[overspending-underusing-loop]] · [[token-roles]] · [[system-1-model]]
- [[factory-ai]] · [[tereza-tizkova]]

## 결과로 보증하는 라우터, 그리고 시간축 (2026-10-09 · [[tech-bridge-kimchi-cost-per-task-harness]])

[[kimchi|Kimchi]]([[cast-ai|Cast AI]])는 Factory와 **반대쪽 끝**에서 같은 기능을 말한다. Factory는 과제 **전에** 난이도를 분류해 *"임계값 위 최저가"* 를 고르고, Kimchi는 *"based on the outcome of the task"*(04:24~04:28) 고르며 산출물 **점수**를 *"to prove you that whatever model we will pick for you you will always have like good enough scoring"*(08:37~08:46) — **사후 품질 게이트로 라우팅을 보증**한다. 비교 단위는 토큰 단가가 아니라 **같은 품질의 작업당 비용**(03:07~03:23) → [[true-cost-to-perfect-answer]].

⭐ **이 페이지 첫 시간축 기록**: 사내 차트에서 1순위 모델이 *"The 3rd of June Kimmy[=Kimi] 2.6"* → *"It happened the 12th of June"* → *"21st of June (…) Minimat[=MiniMax] 3"*(06:05~06:25). [[minimax-m3]]가 6월 초 출시된 지 1~2주 안이다. 화자의 논점: *"Do you think we look at this as human? Absolutely not. But an autonomous harness (…) is going to do just that."*(06:32~06:47) — 라우터의 이점이 **한 과제의 비용**만이 아니라 **새 모델 채택 속도**라는 주장.

> ⚠️ **메커니즘 미발화.** 무엇이 *outcome* 신호인지, 과제 전 선택인지 실패 후 전환인지, 전환 빈도·임계값, 채점 모델 — 전부 말하지 않는다. 6월 12일 전환이 품질을 유지했다는 근거는 차트의 *"same outcome"*(05:04) 한 마디. 성과 수치(2.5배)는 화자 산수와도 맞지 않는다(토큰 ×1.5·비용 ÷1.5 = 2.25배).

## 검증 제품 내부의 부품으로 (2026-10-14 · [[tech-bridge-gitar-agentic-pr-validation]])

[[gitar|Gitar]]의 내부 구성 요소 셋 중 하나가 LLM proxy다: *"We also have an NLM[=LLM] proxy that handles the routing across different models as well as things like failover."*(08:37~08:45) 라우터가 제품 자체가 아니라 **검증 하네스의 부품**으로 나온다. 라우팅 기준은 미발화다. 같은 발표의 *"fixed PR price"*(08:30~08:36)는 [[tech-bridge-kimchi-cost-per-task-harness|Kimchi]]의 작업당 비용과 같은 계열의 과금 단위 전환이다.

## 라우터가 아니라 정책 — 신원별 모델·예산 (2026-10-17 · [[tech-bridge-tailscale-aperture-ai-without-lock-in]])

[[remy-guercio|Remy Guercio]]([[tailscale|Tailscale]] Aperture)의 모델 선택은 라우터가 고르는 방식이 아니다. 게이트웨이가 연결의 신원을 알고 관리자가 정한 정책을 적용한다: *"Once I connect to the (…) gateway, it knows who I am. It knows what I am."*(11:43~11:47) 그다음은 *"You can use GLM 5.2. Uh you get this budget with GLM 5.2, right? You get unlimited budget with a cheap model, and you get an extremely narrow budget with a frontier model, right?"*(11:52~12:01)이다. 이 페이지의 다른 라우터(Factory의 난이도 분류, Kimchi의 결과 보증)와 달리 **결정 주체가 관리자**다 → [[ai-gateway]]

⚠️ 모델 단가 기준의 배급이고 작업 결과 기준이 아니다. 어느 쪽이 나은지는 측정되지 않았다. *"GLM 5.2"* 는 예시이고 대조하지 않았다.
