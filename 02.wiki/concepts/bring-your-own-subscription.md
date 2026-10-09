---
title: "구독을 들고 다니기 (Bring Your Own Subscription)"
type: concept
category: pattern
tags: [platform, subscription, pricing, app-developer, token-economics, openai, chatgpt, byo]
aliases: [BYO subscription, bring your own subscription, 구독 연동, 구독 이동]
related: [model-mixing-economics, software-marginal-cost, intelligence-abundance, compute-constrained-growth]
first-seen: tech-bridge-altman-devday-dots
sources: [tech-bridge-altman-devday-dots]
created: 2026-10-09
updated: 2026-10-09
---

# 구독을 들고 다니기

**사용자가 이미 낸 AI 구독(의 토큰)을 제3자 앱에 가져가 쓰게 해서, 앱 개발자가 모델 비용을 떠안지 않게 하는 플랫폼 설계.** [[openai|OpenAI]]가 DevDay 2026에 낸 것으로, [[tech-bridge-altman-devday-dots]]에서 진행자 [[dan-shipper|Dan Shipper]]가 개발자 쪽 경제학을, [[sam-altman|Sam Altman]]이 사용자 쪽 동기를 말했다. 챕터 제목은 *"BYO Subscription"* 이지만 **"BYO"라는 말은 자막에 없다.**

> ⚠️ **메커니즘이 없다** — 어떤 토큰이 어떻게 앱으로 넘어가는지, 한도·과금·모델 선택권·데이터 경계 모두 대담에 없다.

## 개발자 쪽 — 원가 딜레마가 풀린다

> *"being able to bring your tokens from your CHT[=ChatGPT] subscription to an app developer (…) normally you're you're thinking about okay, how much AI can I let my users use so that it doesn't bankrupt me? And then you're like, can I use should I use lower priced models and then the experience is worse? But if someone can bring their subscription, I'm like, great, you can use whatever model you want under your subscription."* — 진행자 (21:00~21:21)

[[software-marginal-cost]]가 *"AI 소프트웨어는 처음으로 한계비용을 갖는다 — 결국 누가 그 비용을 대는지로 설명돼야 한다"* 고 했다면, 이것은 **그 비용을 사용자의 기존 구독이 대는** 답이다. [[model-mixing-economics]]의 *"단계마다 다른 모델 = 예산 문제"* 도 앱 개발자 쪽에서는 사라진다.

## 사용자 쪽 — "그건 당신의 구독이다"

> *"I like I hate having to sign up for 100 subscriptions. (…) we want to make it just super easy for people to take it with them and it's your subscription. Like it's you should get to use wherever you want."* — Altman (22:26~22:44)

Altman은 이를 플랫폼 철학 안에 놓는다 — *"let people build apps in ChachiBT[=ChatGPT] (…) Let people bring their subscription wherever they'd like have the marketplace"*(03:52~04:05), 진행자가 꺼낸 Bill Gates의 *"create more value than you capture"*(04:18~04:20), *"we're going to give you all of the same tools we use"*(24:22~24:28).

## 이 위키의 다른 BYO와

- [[model-mixing-economics]]의 Microsoft Copilot BYO는 **기업 고객이 자기 모델을 라우터에 넣는 것**(공급 쪽 BYO). 여기는 **소비자가 자기 구독을 앱에 들고 가는 것**(수요 쪽 BYO). 방향이 반대다.

## ⚠️ 유보

- **플랫폼 잠금(lock-in)과의 관계**를 아무도 말하지 않는다 — *"구독을 어디든"* 은 동시에 *ChatGPT 구독이 앱 결제의 기본 단위*가 된다는 뜻일 수 있다(위키의 독해).
- 앱 개발자의 수익 배분, 구독 등급별 한도 — 없음.

## References

- [[tech-bridge-altman-devday-dots]] — first-seen
- [[openai]] · [[sam-altman]] · [[dan-shipper]]
- 관련: [[software-marginal-cost]] · [[model-mixing-economics]] · [[intelligence-abundance]]
