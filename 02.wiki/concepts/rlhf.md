---
title: RLHF (인간 피드백 기반 강화 학습)
type: concept
category: technique
tags: [rlhf, post-training, alignment, human-preference, reward-model]
related: [preference-reward-asymmetry, assistance-vs-automation, post-training-northstars, reward-hacking, intent-alignment, decision-quality]
first-seen: tech-bridge-rlhf-assistance-vs-automation
sources: [tech-bridge-rlhf-assistance-vs-automation, tech-bridge-brockman-agi-era-defender-window]
created: 2026-09-20
updated: 2026-09-20
---

# RLHF (인간 피드백 기반 강화 학습)

**인간의 선호를 수집하고 그것을 최적화하도록 모델을 학습시키는 절차.** 오늘날 거의 모든 LLM의 post-training 기반이다.

> **이 위키에 이 페이지가 2026-09-20까지 없었다는 사실 자체가 기록할 만하다.** [[reward-hacking]]·[[intent-alignment]]·[[transformer]]·[[in-context-learning]]은 있었는데 **오늘날 거의 모든 모델을 만든 학습 절차의 페이지가 없었다.** 그리고 그 자리를 채운 소스가 **그것을 만든 사람의 비판**이다.

## 무엇을 하는가 — 그리고 무엇을 최적화하는가

> 요약하자면, 이것은 **인간의 선호도를 수집하고 그에 맞춰 최적화하는 것**입니다. ([[tech-bridge-rlhf-assistance-vs-automation]], 06:02~06:20)

[[diogo-almeida|Diogo Almeida]](InstructGPT/RLHF 논문 공동 저자)는 이 페이지의 핵심 문장을 이렇게 놓는다:

> **"왜 모든 [LLM]에 사람이 개입해야 하는가"** … **간단히 말해서, 우리가 말 그대로 그들을 그 루프에 집어넣었습니다. 이 루프의 목표는 인간의 선호도를 최적화하는 것입니다. 소프트웨어를 자율적으로 실행하기 위한 것이 아닙니다.** (06:20~06:39)

**즉 이 페이지의 요점은 알고리즘이 아니라 목적함수다.** → [[assistance-vs-automation]]

> ⚠️ *"제가 사용 현황을 살펴본 바로는 거의 100%의 [LLM]이 RLHF로 학습된 것 같다"*(05:41~06:02)는 **근거가 제시되지 않는다.**

## 기원 — 2017년

[[greg-brockman]]이 같은 주 소스에서 계보를 준다:

> **인간 선호로부터의 보상 학습·강화 학습도 2017년에 만들어졌습니다** — **사람들이 피드백을 제공함으로써 모델을 사람들이 원하는 것에 어떻게 정렬시킬 수 있을까**를 생각하기 시작한 거죠. ([[tech-bridge-brockman-agi-era-defender-window]], 05:08~05:25)

> 네. 그냥 **사용성(usability)** 을 위해서요. — **정확합니다.** (05:25~05:44)

**두 소스가 같은 절차의 기원과 귀결을 양쪽에서 말한다** — Brockman은 *정렬의 초기 아이디어* 로, Almeida는 *그 선택이 이 분야 전체의 천장이 된 지점* 으로. **상반되지 않고 같은 사실의 두 평가다.**

같은 자리에서 Brockman은 초기 안전 아이디어로 **토론(debate)** 과 **반복 증폭(iterative amplification)** 도 언급한다(05:44~06:01).

## 귀결

| 귀결 | 페이지 |
|---|---|
| 보조에는 탁월, 자동화에는 부적합 | [[assistance-vs-automation]] |
| 과대약속·환각이 설계상의 결과 | [[preference-reward-asymmetry]] |
| 다른 북극성이 가능하다(RLVR·보정된 의사결정) | [[post-training-northstars]] |
| 안전의 초기 접근이 *"가장자리를 둘러싸는"* 표면 조치였다 | [[tech-bridge-brockman-agi-era-defender-window]] 03:53~04:32 |

## ⚠️ 이 페이지에 없는 것

- **알고리즘의 실제 절차** — 보상 모델 학습, PPO/DPO 등. **두 소스 모두 "다들 아시니 넘어간다"고 명시적으로 건너뛴다.**
- **RLHF 이후 변형들**(DPO·GRPO 등)에 대한 언급 — 없음.
- **정량적 비교** — 없음.

## References

- [[tech-bridge-rlhf-assistance-vs-automation]] — first-seen
- [[tech-bridge-brockman-agi-era-defender-window]] — 기원
- [[diogo-almeida]] · [[greg-brockman]] · [[openai]]
- 관련: [[assistance-vs-automation]] · [[preference-reward-asymmetry]] · [[post-training-northstars]] · [[reward-hacking]] · [[intent-alignment]]
