---
title: 프론티어의 속도 조절 (Pacing the Frontier)
type: concept
category: theory
tags: [ai-safety, governance, openai, deployment, alignment, bottleneck]
related: [training-time-risk, slowdown-within-lead-margin, agi-definition, compute-constrained-growth, embedded-external-evaluators, joint-democratic-oversight]
first-seen: tech-bridge-brockman-agi-era-defender-window
sources: [tech-bridge-brockman-agi-era-defender-window, tech-bridge-altman-benioff-dreamforce]
created: 2026-09-20
updated: 2026-09-23
---

# 프론티어의 속도 조절 (Pacing the Frontier)

**더 유능한 모델로 나아가는 속도를 안전·보안·정렬 기준이 따라오는 속도에 묶는다는 [[openai|OpenAI]]의 원칙어.** [[greg-brockman|Greg Brockman]]이 [[tech-bridge-brockman-agi-era-defender-window]]에서 이름과 함께 제시했다.

> 이제 우리가 **'프론티어의 속도 조절(pacing the frontier)'이라고 부르는 것**을 진지하게 생각해야 할 시점이라고 봅니다. **더 유능한 모델로 나아갈 때 안전, 보안, 정렬이 전부 계속 수준을 끌어올려야 하는 기준이라는 것을 확실히 해야 합니다.** (03:12~03:24)

> 그리고 그것들이 실제로 **진보의 병목에 가까워지거나**, 제대로 해내기 위해 많은 노력을 쏟아야 하는 부분이 됩니다. **제 머릿속에서는 컴퓨트보다 오히려 그 제약들**이고, 컴퓨트는 해낼 수 있다고 생각합니다. (03:24~03:41)

**주목할 점은 병목의 순위 매기기다** — 이 위키가 [[compute-constrained-growth]]·[[power-shortfall]]에서 컴퓨트를 제약으로 다뤄 왔는데, **화자는 안전 기준이 컴퓨트보다 먼저 묶는다고 말한다.**

## 무엇이 조절되는가 — 배포가 아니라 개발

> **안전·보안·정렬을 배포 시점만이 아니라 개발 시점과 평가까지 거슬러 올라가 정말로 생각해야 한다는 것입니다.** (47:48~48:02)

> 일부는 **우리가 취할 수 있는 일방적 조치**에 관한 것이며, **이런 모델들을 훈련하고 개발하고 평가하는 것에 대해서까지 어떻게 안전 사례(safety case)를 만들 것인가**에 관한 것입니다. **그건 전부 새롭습니다. 누구도 이것을 실제로 운영해 본 적이 없습니다.** (07:36~07:54)

**이것이 "AGI 시대" 선언의 실제 내용이다** → [[agi-definition]]

## 이 위키에서의 좌표 — 같은 처방, 다른 주체

| 소스 | 처방 | 조율 주체 |
|---|---|---|
| [[sam-altman]] (09-05, [[training-time-risk]]) | 프론티어 RL 실행 **연기** | **일방적** (사건 대응) |
| [[dario-amodei]] (09-16) | *"멈추지 말고 늦추자"* | **상주 외부 평가자 → 업계 합의 → 정부** ([[embedded-external-evaluators]]·[[joint-democratic-oversight]]) |
| **이 페이지** (09-19) | 기준이 따라오는 속도에 묶기 | **일방적 조치 + 랩 간 조율** (정부 언급 없음) |

**Amodei와 거의 같은 명제인데 거버넌스가 다르다.** Brockman은 *"조율(coordination)이 아주 중요한 주제"* 라고 하면서도 **정부·규제·외부 검증을 한 번도 말하지 않는다** — 조율의 범위가 **프론티어 랩 사이**다(07:18~07:36, 08:24~08:38).

그리고 [[training-time-risk]]가 09-05에 **사건**으로 들어온 것이 여기서 **상시 원칙**으로 승격된다. → [[slowdown-within-lead-margin]]

## ⚠️ 유보

- **당사자 진술이고 강제력이 없다.** *"기준"* 이 무엇인지, 누가 판정하는지, 못 맞추면 무엇이 멈추는지 **소스에 없다.**
- ***"안전 사례(safety case)"*** 의 형식·심사자·공개 여부 — 없음.
- **실제로 속도가 조절된 사례가 하나도 제시되지 않는다** — [[training-time-risk]]의 연기는 다른 소스(09-05)의 것이고 이 대담에서는 언급되지 않는다.
- **정부·외부 검증이 대담 전체에서 부재**한다.

## References

- [[tech-bridge-brockman-agi-era-defender-window]] — first-seen
- [[greg-brockman]] · [[openai]]
- 관련: [[training-time-risk]] · [[slowdown-within-lead-margin]] · [[agi-definition]] · [[compute-constrained-growth]] · [[embedded-external-evaluators]] · [[joint-democratic-oversight]] · [[race-to-the-top]]

## CEO가 같은 원칙을 말한다 (2026-09-23 · [[tech-bridge-altman-benioff-dreamforce]])

[[greg-brockman|Brockman]]이 이름 붙인 원칙을 [[sam-altman|Altman]]이 **[[hugging-face|Hugging Face 사건]]의 교훈으로** 반복한다:

> 우리는 **역량 개발 속도를 조절하여 정렬, 안전 및 모니터링이 항상 역량 개발보다 앞서 나가도록** 해야 합니다. (14:40~14:51)

근거는 **수학 사다리**(초등 수학 → 밀레니엄 난제, 3년)의 *"누구의 기준으로 봐도 확실히 빠른 이륙"*(14:19~14:24)이다. ⚠️ **같은 대담에서 Altman은 조건부 감속을 비판한다**(*"어떤 단서도 붙어서는 안 됩니다"*, 03:33) → [[slowdown-within-lead-margin]]. **"무조건 조절"이 실제로 무엇을 멈추는지는 말하지 않는다.**
