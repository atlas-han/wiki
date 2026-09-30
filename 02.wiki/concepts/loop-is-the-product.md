---
title: "루프가 제품이다 (The Loop Is the Product) — 신호 · 검증기 · 두 번째 루프"
type: concept
category: pattern
tags: [agent-loop, verifier, signal, ooda, self-improvement, auto-research, productization]
aliases: [the loop is the product, loop is the product, 루프 자체가 제품, second loop, 두 번째 루프, OODA loop]
related: [agent-recipes, taste-encoded-evals, valued-work-per-watt, verifiable-goals, generator-evaluator-pattern, self-harness, harness-engineering, ralph-wiggum-method, agent-loop-size, linear-vs-closed-loop-harness, openclaw, automated-ai-research]
first-seen: tech-bridge-introspection-loop-is-the-product
sources: [tech-bridge-introspection-loop-is-the-product]
created: 2026-09-30
updated: 2026-09-30
---

# 루프가 제품이다

**에이전트 제품의 단위는 모델도 하네스도 아니라 "신호 → 행동 → 검증"을 도는 루프이고, 그 루프의 품질은 입력 신호의 품질(성공률)과 검증기의 품질(그 성공이 진짜인지)이 정하며, 첫 루프가 남긴 산출물을 다시 신호로 먹이는 두 번째 루프가 지속적 개선을 만든다는 프레이밍.** [[roland-gavrilescu|Roland Gavrilescu]]([[introspection-dev|Introspection]])가 [[tech-bridge-introspection-loop-is-the-product]]에서 세 아이디어 중 첫째로 제시했다.

> *"The loop is the product."* (01:04)

> ⚠️ 발표 한 편의 프레이밍이고 **측정치가 없다.** 화자는 이 루프들의 산출물을 관리하는 제품(pi.recipes)을 판다.

## 계보 — RLHF → 하네스 → 루프 (01:10~01:28)

> *"We've started with everything goes down to RLHF for models and how you should train the model to become better and better reasoning. We then quickly moved to harnesses and how the model is a commodity and it's all about the harness. And now we're talking about loops and how you should build these loops and not touch code anymore."*

→ [[rlhf]] · [[harness-engineering]]. 이 위키의 [[harness-engineering]] 서사(context → harness)에 **한 단계를 더 얹는** 서술이다. *"not touch code anymore"* 는 화자의 요약이고 근거는 없다.

## 첫 사례 — 자동차 가격 협상 (01:35~02:43)

*"this guy, AJ, built the first loop around Clawbot"*(01:45~01:47, Clawbot = 지금의 [[openclaw|OpenClaw]]의 옛 이름이라고 화자가 말한다). 단계:

1. Reddit에서 가격·재고 찾기
2. 딜러와 대화
3. *"put dealers head-to-head and try to figure out how to make them outbid each other"*(02:12~02:17)
4. ⭐ *"have a verifiable way to know when the price is right"*(02:18~02:21)
5. *"lock in. Get the car. And it worked."*(02:24~02:25)

화자에게 이것은 *"the first real example of loop is the product"*(02:33~02:36)이다. ⚠️ AJ가 누구인지, "첫 번째"라는 주장의 근거는 없다. ko는 3번을 **딜러끼리 "협력하여 … 돕는"** 으로 뒤집었다(02:13~02:16).

## 구조 — OODA, 신호, 검증기

- **OODA** — *"models have been trained with this loop in mind. And it comes from this idea of OODA loops"*(02:50~02:55). 모델이 도구를 부르고 관찰을 받는 것 자체가 그 루프다(03:12~03:19).
- **신호와 검증기의 역할 분담**:

> *"the quality of the signal determines the uh success rate of the loop and the uh quality of the verifier um is able to calibrate uh if that success is actually correct or not."* (03:33~03:49)

| 요소 | 무엇을 정하나 |
|---|---|
| **신호**(signal) | 루프의 **성공률** |
| **검증기**(verifier) | 그 성공이 **실제로 옳은지**(보정) |

→ [[verifiable-goals]]의 *verifier가 강하면 독립적으로 루프를 돈다* 와 같은 축. 이 프레이밍은 **신호 쪽을 따로 떼어** 성공률의 원인으로 둔다는 점이 다르다.

## 두 번째 루프 (03:52~04:09)

> *"what happens when you take that and feed it back into the signal? And this is what looping around is all about is how do you generate these artifacts at the end of the first loop to then run a second loop on and have a way to continuously improve."*

첫 루프 = 일을 하는 루프(*"the worker as the inner loop"* 11:42~11:45), 두 번째 루프 = 첫 루프의 산출물(트레이스·실패)을 보고 **무엇을 바꿀지 정하는** 루프. 두 번째 루프가 만드는 것이 [[agent-recipes|에이전트 레시피]]이고, 그 판단 기준이 제작자의 taste다([[taste-encoded-evals]]). 맺음말: *"You try to automate yourself as the uh as the um higher level judge and you want to make sure your second-loop agents are able to apply the same judgment"*(16:37~16:51).

## 이 위키의 다른 루프와

| 페이지 | 루프가 도는 곳 | 두 번째 루프의 판정자 |
|---|---|---|
| [[ralph-wiggum-method]] | 셸 루프로 같은 에이전트 반복 | 없음(사람이 프롬프트 수정) |
| [[self-harness]] | 같은 모델이 자기 하네스를 수정 | 회귀 테스트 |
| [[generator-evaluator-pattern]] | 생성자 ↔ 평가자 | 평가 에이전트 |
| [[agent-loop-size]] | 작은 변경을 끝에서 끝으로 | 신뢰가 쌓이면 사람이 빠진다 |
| **이 페이지** | 제품 = 루프 | **에이전트가 만든 judge + 사람의 보정 + 프로덕션 A/B** |

⚠️ 위키의 정리. 이 소스의 두 번째 루프는 **판정자를 세 겹**(judge · 사람 · 사용자)으로 두는 점에서 [[automated-ai-research]]의 발견 루프(실측 보상 · LLM taste · 사람)와 모양이 같다.

## ⚠️ 유보

- **"첫 루프"와 OODA 기원** — 화자 발화 그대로, 외부 확인 안 함.
- **신호 품질을 어떻게 재는가** — 말하지 않는다. 검증기 품질의 측정도 없다.
- 루프가 **제품**이라는 말이 무엇을 파는지(루프 자체인지, 루프의 산출물인지)는 두 번째 아이디어([[agent-recipes]])에서야 드러난다 — 화자의 답은 **레시피**다.

## References

- [[tech-bridge-introspection-loop-is-the-product]] (first-seen)
- 관련: [[agent-recipes]] · [[taste-encoded-evals]] · [[valued-work-per-watt]] · [[verifiable-goals]] · [[generator-evaluator-pattern]] · [[openclaw]]
