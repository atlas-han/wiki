---
title: "구독을 들고 다니기 (Bring Your Own Subscription)"
type: concept
category: pattern
tags: [platform, subscription, pricing, app-developer, token-economics, openai, chatgpt, byo]
aliases: [BYO subscription, bring your own subscription, 구독 연동, 구독 이동]
related: [model-mixing-economics, software-marginal-cost, intelligence-abundance, compute-constrained-growth, reserve-then-settle]
first-seen: tech-bridge-altman-devday-dots
sources: [tech-bridge-altman-devday-dots, tech-bridge-cooking-with-codex, tech-bridge-stigg-ai-companies-building-banks, tech-bridge-codex-app-server]
created: 2026-10-09
updated: 2026-10-16
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

## 메커니즘의 이름 하나 — Codex App Server (2026-10-11 · [[tech-bridge-cooking-with-codex]])

위 ⚠️ *"메커니즘이 없다"* 에 대한 부분적 단서. [[charlie-guo|Charlie Guo]]([[openai|OpenAI]], **2026-06-29 녹화** — DevDay 대담보다 앞선 시점): App Server로 [[codex|Codex]]를 제품에 넣으면 *"it brings the ability for your users to uh use their chat GBT subscription and perhaps more importantly use their Chat GBT token budget uh to power the products that you're building."*(59:07~59:20) App Server는 *"the core protocol that underpins the Codex app, the Codex CLI, uh, the Codex VS code extension"*(58:29~58:37), 오픈소스.

- 즉 적어도 **Codex 하네스를 임베드하는 경로**에선 구독 토큰을 들고 오는 길이 6월에 이미 있었다. DevDay에서 말한 *"앱 개발자에게 구독을 가져가기"* 가 같은 메커니즘인지는 **두 소스 모두 말하지 않는다.**
- 빠지는 것: *"the ones that need to live on your computer like computer use are, you know, not going to be there"*(59:26~59:31).

> ⚠️ ko는 App Server를 **"섬기는 사람"**(59:05, 59:35), open source를 **"영업 중"**(1:01:09)으로 옮긴다.

**두 번째 OpenAI 1인칭과 실제 사례 (2026-10-14 · [[tech-bridge-codex-app-server]]).** [[dominik-kundel|Dominik Kundel]]: *"you can have signin with chat GPT as part of that meaning that if someone is using your app they can still bring their own chat GPT subscription and it goes off their codeex uh use usage limit. So if you've used something like T3 code or similar, you're actually using that."*(06:18~06:36) — 차감 대상은 **사용자 자신의 Codex 사용 한도**다. Charlie의 *"Chat GBT token budget"* 과 같은 방향이고, 실사용 앱(T3 Code, ⚠️ ASR *"T3 code"*)이 처음 이름으로 나온다. 그리고 Python SDK가 sign in with ChatGPT를 쉽게 붙여 준다(10:28~10:33). ⚠️ **`en`·ko 공유 반전** — *"this won't affect your Codex usage limits"* / "사용량 제한에 영향을 미치지 않습니다"(06:29). 자막 번역으로 읽으면 이 페이지와 충돌하는 것처럼 보이지만, **en-orig로 보면 충돌이 아니다.**

## 반대 방향의 사건 — 서드파티 에이전트의 구독 사용 차단 (2026-10-12 · [[tech-bridge-stigg-ai-companies-building-banks]])

[[dor-sasson|Dor Sasson]]([[stigg|Stigg]] CEO, ⚠️ 벤더 주장·출처 미제시): 4월(연도 미발화) *"Anthropic basically eliminating access for open flow[=OpenClaw, 판독] and other third-party agents to basically use the subscriptions plans."*(01:38~01:47) — OpenAI가 구독을 *들고 나가게* 하는 쪽이라면, 이건 **제3자가 구독을 쓰는 경로를 닫는** 쪽이다.

> ⚠️ **방향이 반대인 두 정책.** 사실 충돌은 아니다(회사·시점이 다르다). 하지만 Sasson의 진단 — *"Anthropic didn't have a an effective way to delineate between users who are using their APIs and users are using their subscription programs"*(03:13~03:22) — 을 받아들이면, 이 페이지의 BYO는 **바로 그 구분을 런타임에 하는 계층**(어느 앱·에이전트가 어느 구독의 토큰을 얼마나 쓰는지 요청마다 판정·차감)을 전제로 한다. 위 ⚠️ *"메커니즘이 없다"* 의 빈칸이 어떤 모양인지에 대한 간접 단서 → [[reserve-then-settle]]

## References

- [[tech-bridge-altman-devday-dots]] — first-seen
- [[openai]] · [[sam-altman]] · [[dan-shipper]]
- 관련: [[software-marginal-cost]] · [[model-mixing-economics]] · [[intelligence-abundance]]
- [[tech-bridge-stigg-ai-companies-building-banks]] — 반대 방향의 사건(Anthropic, 화자 주장) · [[reserve-then-settle]]
