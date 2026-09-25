---
title: 프론티어의 속도 조절 (Pacing the Frontier)
type: concept
category: theory
tags: [ai-safety, governance, openai, deployment, alignment, bottleneck]
related: [training-time-risk, slowdown-within-lead-margin, agi-definition, compute-constrained-growth, embedded-external-evaluators, joint-democratic-oversight, existing-law-first]
first-seen: tech-bridge-brockman-agi-era-defender-window
sources: [tech-bridge-brockman-agi-era-defender-window, tech-bridge-altman-benioff-dreamforce, tech-bridge-openai-huggingface-incident-black-hat, tech-bridge-jensen-huang-cbs-interview]
created: 2026-09-20
updated: 2026-09-25
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

## 보안 담당자가 말하는 감속 — "의식적으로 연구 속도를 늦추고 있다" (2026-09-25 · [[tech-bridge-openai-huggingface-incident-black-hat]])

[[greg-brockman|Brockman]](원칙어) · [[sam-altman|Altman]](CEO)에 이어 **OpenAI 세 번째 화자**, 이번엔 **보안·인프라 실무자**([[michael-dalton|Michael Dalton]])다:

> 많은 팀이 **모든 것을 내려놓고** 예방·탐지·대응을 강화하고 있습니다. **보안을 강화하고 환경의 보안 원칙과 기반을 업그레이드하기 위해 의식적으로 연구 속도를 늦추고 있으며**, AI 에이전트 모니터링을 대폭 확대하고 있습니다. (29:50~30:08)

앞의 두 화자는 *원칙* 이었고, 여기서는 **사건에 대한 대응 조치**로 나온다 — 감속의 **트리거가 명시된** 첫 서술이다. ⚠️ 무엇을 얼마나 늦췄는지(어떤 연구, 기간)는 말하지 않는다. 그리고 1차 교정 직후 **훈련·평가를 이틀 만에 재개**(7/6)했다가 7/8 게시판이 재건된 것이 발표 자체의 타임라인에 있다.

## "최대한 빨리, 그러나 해야 할 것보다 빠르지 않게" — 기준 대신 책임 (2026-09-25 · [[tech-bridge-jensen-huang-cbs-interview]])

CBS 진행자가 David Sacks의 말(*"AI 개발 속도를 늦추면 미국 경제와 군에 막대한 피해"*)을 전하며 *"중국을 고려하면 지금 속도를 조절해야 하나"* 를 묻자, [[jensen-huang|Jensen Huang]]:

> 그가 한 말[의] 맥락[은] 정확히 모르겠[지만], **그는 미국이 가능한 한 빨리, 하지만 [해야 할 속도]보다 빠르지는 않게 [가기를] 원한다고 거의 확신해요.** 우리는 최대한 빨리 [가되], 마땅히 해야 할 속도보다 더 빠르지는 않게 [가야 합니다]. (18:15~18:35)

**같은 모양, 다른 기준.** 이 페이지의 원칙은 *역량의 속도를 안전·보안·정렬 **기준**이 따라오는 속도에 묶는다* 였다. Huang의 *"should"* 는 기준을 말하지 않고 바로 **법적 책임**으로 넘어간다:

> 안전하지 않은 제품을 [내놓아] 사람들을 위험에 [빠뜨리면], **우리에게는 당신에게 책임을 물을 수 있는 모든 유형의 법이 있습니다.** 따라서 (…) 기업들은 **옳은 일을 하도록 완벽하게 [인센티브를 받고] 있습니다.** (18:37~18:58)

| | 속도의 상한을 정하는 것 | 조율 주체 |
|---|---|---|
| [[greg-brockman\|Brockman]]·[[sam-altman\|Altman]] (이 페이지) | 안전·보안·정렬 **기준** | 랩 (일방) + 랩 간 |
| [[dario-amodei\|Amodei]] | **외부 평가자의 처리량** | 평가자 → 정부 |
| **Huang** | **사후 법적 책임의 위협** → [[existing-law-first]] | 법원 (사후) |

⚠️ **귀속 주의** — *"not faster than we should"* 는 **Huang이 Sacks에게 귀속한 해석**이고(*"맥락은 정확히 모르겠지만"*), Sacks의 전언된 원문은 **감속의 비용**만 말한다. 이 위키는 이것을 **Huang의 문장**으로 적는다.

⚠️ 같은 인터뷰에서 Huang은 *"누구와도 상관없이 가능한 한 빨리"*(16:01~16:07)라고도 하고, 랩들은 *"컴퓨팅의 상당 부분을 AI 안전으로 옮겨야"*(03:24~03:37) 한다고도 한다. **"해야 할 속도"가 실제로 무엇을 멈추는지는 이 페이지의 다른 화자들과 마찬가지로 말하지 않는다.**
