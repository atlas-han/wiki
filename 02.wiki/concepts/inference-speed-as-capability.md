---
title: "추론 속도라는 두 번째 축 (Inference Speed as Capability)"
type: concept
category: theory
tags: [inference-speed, latency, pricing, democratization, feedback-loop, openai, custom-chip, frontier-pricing]
aliases: [speed democratization, 속도의 민주화, ultra fast, price of IQ, 지능의 가격과 속도의 가격]
related: [intelligence-abundance, compute-constrained-growth, system-1-model, search-latency-tiers, voice-latency-thinking-tradeoff, model-mixing-economics, agentic-sites, speculative-decoding, open-model-customization-loop]
first-seen: tech-bridge-altman-devday-dots
sources: [tech-bridge-altman-devday-dots, tech-bridge-fireworks-train-to-deploy-open-models, tech-bridge-gpt-6-1-terra-first-look]
created: 2026-10-09
updated: 2026-10-30
---

# 추론 속도라는 두 번째 축

**모델 경쟁의 축이 "같은 지능을 더 싸게"(IQ의 가격)에서 "같은 지능을 더 빠르게"(속도의 가격)로 하나 더 늘었고, 속도는 단지 편의가 아니라 사람의 반복적 사고 루프를 바꾸는 능력이라는 프레이밍.** [[sam-altman|Sam Altman]]이 [[tech-bridge-altman-devday-dots]](DevDay 2026)에서 자신이 *"all your prompting on ultra fast"* 를 쓴다고 인정하며 세웠다.

> *"So historically what we have mostly focused on and I think done a great job of is bringing down the like price of IQ (…) Now there's this new vector that is clearly going to be very important of speed"* (29:38~29:58)

## 두 주장

### 1. 속도는 사고 루프를 바꾼다

> *"creators should have an immediate connection to what they're creating and how speed and the feedback loop was so important. And I did not realize what a difference that makes to my kind of iterative thinking loop to have responses come in so quickly."* (28:55~29:13)

근거는 Bret Victor의 강연(⚠️ 이름·연도 미발화, 화자 스스로 *"I'm going to get this a little bit wrong"*)과 **본인 체감**뿐이다. 그래서 *"I have such a hard time dragging it back over"* — 그리고 그 대가로 *"we kind of get out of touch with people building on our tools"* 를 스스로 걱정한다(28:09~28:29).

### 2. 속도도 지능처럼 "민주화"된다 — 그러나 최전선은 늘 비싸다

| 층 | 진술 |
|---|---|
| 지금 | *"You can pay us for it and do it now"* (30:25) |
| 가까운 미래 | *"8x at a great price in the notistant[=not-distant] future"* (30:29~30:33) |
| 그 다음 | *"100x faster"* (30:35) |
| 수단 | *"our own chip is going to be an incredible contributor"*, 추론 스택·모델 자체의 개선 (29:58~30:10) |
| 구조 | *"there will always be a real frontier in terms of intelligence or speed or whatever else at a higher price"* + *"relentless focus on driving value per dollar up"* (30:47~31:12) |

즉 **두 개의 동시 운동**이다 — 최전선(가장 똑똑하거나 가장 빠른 것)은 늘 비싼 등급으로 남고, 그 아래는 *"put Moore's law to shame"* 속도로 싸진다. 진행자는 같은 구도를 지능 쪽에서 *"the Astra is a more expensive model world"* 로 짚었다(29:28~29:30) → [[openai-astra]].

## 이 위키의 다른 속도 축과

- [[search-latency-tiers]] — 같은 제품이 200ms와 "몇 분"을 동시에 판다. 여기도 **속도가 가격 등급**이다. 다만 그쪽 근거는 *기계가 쓴다*, 여기는 *사람의 사고 루프*.
- [[voice-latency-thinking-tradeoff]] — 실시간 음성은 thinking을 꺼야 한다. 속도와 지능이 **맞바꾸는** 관계라는 점에서 이 페이지의 *"두 축"* 을 지지한다.
- [[system-1-model]] — *"지연이 게이트를 끄게 만든다"*. 같은 대담에서 Altman은 [[jev|Jev]]식 접근 대신 **주력 모델을 더 싸고 빠르게** 하겠다고 답한다(*"the best cheapest fastest most capable model at every point on the paro[=Pareto] curve"*, 20:31~20:36).
- [[agentic-sites]] — [[cerebras|Cerebras]] 기준 1.1초 페이지 생성. 하드웨어가 속도를 사는 사례.
- [[intelligence-abundance]] — 09-07 *"전기처럼 싸진다"* 의 형평 논거에 **속도**라는 두 번째 항목이 붙었다.
- [[compute-constrained-growth]] — 자체 칩. ⚠️ 09-06 진행자가 말한 추론 칩 *Jalapeno* 와 같은 것인지 소스는 말하지 않는다.

## 서빙 층의 속도 — 커널과 draft model (2026-10-18 · [[tech-bridge-fireworks-train-to-deploy-open-models]])

Altman이 속도를 모델 공급자의 축으로 말했다면, [[fireworks-ai|Fireworks AI]]는 **같은 오픈 모델을 고객 워크로드에 맞춰 빠르게** 내는 쪽을 판다. 자체 추론 엔진 FireAttention과 CUDA 커널을 입력·출력 토큰 수, prompt cache hit rate, latency 목표에 맞춰 최적화하고(05:41~06:08), [[speculative-decoding]]의 draft model을 고객이 학습한다(06:22~06:49). ⚠️ 사례 수치(Cursor *"13x faster inference"*, Vercel *"40x latency improvement"*)는 기준선이 없다.

## ⚠️ 유보

- **8배·100배의 기준이 없다** — 무엇 대비, 어떤 모델, 언제. *"GPT7 Galaxy or whatever"* 는 농담조다.
- *"ultra fast"* 의 정식 제품명·가격 — 없다(*"I don't think I can afford it"* 는 진행자의 농담).
- 사고 루프 주장은 **판매자 1인의 체감**이다. 측정 없음.

## References

- [[tech-bridge-altman-devday-dots]] — first-seen
- [[sam-altman]] · [[openai]] · [[openai-astra]]
- 관련: [[intelligence-abundance]] · [[compute-constrained-growth]] · [[search-latency-tiers]] · [[voice-latency-thinking-tradeoff]] · [[system-1-model]] · [[model-mixing-economics]] · [[agentic-sites]]

## 사용자 쪽에서 본 속도 — 빠르고 싸지만 끝까지 안 간다 (2026-10-30 · [[tech-bridge-gpt-6-1-terra-first-look]])

[[openai-terra|GPT 6.1 Terra]] 리뷰어(미상)는 평가를 속도로 연다: C++ 게임을 2분 35초에(*"I really want to drive home the point that this thing is insanely fast"* 00:46~00:48), 그리고 가격 · 속도 · 컴퓨터 사용의 조합으로 닫는다(04:50~05:04). 그러나 같은 리뷰가 *"it gives up very easily"*(04:19~04:22)를 패턴으로 짚는다 → **속도 축과 과제 완수(끈기) 축은 따로 움직일 수 있다.** 리뷰어 스스로 호감의 근거를 *"not because it's making insane-looking high-quality code results"*(05:07~05:11)라고 구분한다. ⚠️ 1인 체감 · 1회 실행.
