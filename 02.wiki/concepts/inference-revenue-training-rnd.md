---
title: 추론은 매출, 훈련은 R&D (손익계산서의 물리 법칙)
type: concept
category: theory
tags: [capex, data-center, training, inference, business-model, bubble, microsoft]
aliases: [laws of physics of the income statement, 손익계산서의 물리 법칙, 추론 = 매출, 훈련 = R&D, 과잉 구축 판단 규칙]
related: [compute-constrained-growth, intelligence-as-infrastructure, software-marginal-cost, power-shortfall, data-center-local-backlash]
first-seen: tech-bridge-nadella-copilot-autopilot
sources: [tech-bridge-nadella-copilot-autopilot]
created: 2026-09-29
updated: 2026-09-29
---

# 추론은 매출, 훈련은 R&D

**AI 인프라가 과잉인지 과소인지를 컴퓨트의 절대량이 아니라 회계 구조로 판단하는 규칙 — 추론은 매출(top line)로 돈이 되고, 훈련은 그 매출의 일정 비율로 쓰는 R&D다. 그러니 길게 보면 추론이 컴퓨트를 지배해야 하고, 훈련 지출은 매출 대비 R&D 비율의 제약을 받는다.** [[satya-nadella|Satya Nadella]]가 [[tech-bridge-nadella-copilot-autopilot]]에서 *"과잉 구축과 과소 구축 중 무엇이 더 큰 위험인가"* 에 답하며 세웠다.

> **Ultimately, inference has to dominate because otherwise, uh what are you training for?** (22:58~23:01)
> **what percentage of your revenue is R&D? Training is like R&D, right? Is it 10? Is it 15? Is it 20? All of us are subject ultimately to some laws. And inference is revenue, right?** (23:05~23:17)
> **that is the laws of physics of the income statement that all of us are going to be subject to.** (23:29~23:34)

> ⚠️ **당사자 진술.** 화자는 *"we feel pretty confident about our compute ramp"*(22:49~22:51)라 하는 하이퍼스케일러의 CEO다. **10·15·20%는 질문형**이고 Microsoft 자신의 비율은 말하지 않는다.

## 규칙의 형태

```
매출(top line)  ←  추론을 수익화
R&D            =  매출 × 일정 비율   ←  이것이 훈련
```

*"for a period of time, someone can say, 'Hey, I'm going to go build and I'm going to train.' Ultimately, it's a percentage of … revenue is R&D."*(23:34~23:41) — **훈련에 앞서 쓰는 것은 한동안 가능하지만, 결국 추론 매출이 따라와야** 한다. 과잉 구축의 정의가 여기서 나온다: **추론 매출로 정당화되지 않는 훈련 컴퓨트.**

## 같은 답의 앞 절반 — "완벽한 선은 없다"

- *"there will never be a way … to say there's a perfect line of under build over build"*(21:06~21:13). 판단 기준은 컴퓨트량이 아니라 **확산** — *"the market is still a lot more concentrated. It's about the hit app"*(20:53~21:00), 목표는 기업이 토큰으로 **실질 ROI**를 얻어 *"real GDP growth"* 에 나타나는 것(21:17~21:25).
- 남과의 차이: *"Some folks may be catching up because … we've had like a more gradual ramp"*(22:24~22:28), AI 컴퓨트 배분이 Redmond에서 *"a long before … other hyperscalers"*(22:30~22:38). 진행자는 다른 하이퍼스케일러가 *"borrowing heavily while they build"* 한다고 짚는다(22:13~22:17).

## 이 위키에서의 좌표

- [[compute-constrained-growth]] — [[sam-altman|Altman]]: *"우리 회사의 구축 계획은 걱정 안 한다, 전 세계의 계획이 걱정"*. Nadella도 **같은 구조**(우리는 점진적, 남은 따라잡는 중)이지만 **판단 규칙**을 준다는 점이 다르다. ⚠️ 두 CEO 모두 거품의 위험을 **남에게** 둔다.
- [[intelligence-as-infrastructure]] — [[jensen-huang|Huang]]은 토큰을 kWh처럼 보는 **공급자의 인프라 프레임**. 이 페이지는 **구매자·운영자의 손익 프레임**이다. Huang에게 컴퓨트는 더 지을수록 좋은 인프라, Nadella에게는 **매출 비율로 제한되는 비용**.
- [[software-marginal-cost]] — 같은 대담의 수요 쪽 짝. 추론이 매출이 되려면 누군가 한계비용을 내야 한다.
- [[data-center-local-backlash]] — 같은 대담에서 구축의 **사회적** 제약(지역 사회의 허가)을, 이 페이지는 **재무적** 제약을 말한다.

## ⚠️ 유보

- **비율의 근거 없음** — 10·15·20%는 예시 질문. 어느 업종의 R&D 비율을 기준으로 하는지 없다.
- **프론티어 랩에 적용되는가** — 훈련이 매출의 10~20%라는 틀은 **매출이 큰 기존 기업**에는 맞지만, 매출보다 훈련 지출이 큰 프론티어 랩에는 **정의상 과잉**이 된다. 화자는 특정 회사를 지목하지 않는다.
- **추론 비용 자체** — 추론도 컴퓨트를 먹는다. *"inference is revenue"* 는 추론의 **매출**이지 **마진**이 아니다.
- *"whether that will be a linear line, I don't know"*(21:28~21:29) — 화자 자신의 단서.

## References

- [[tech-bridge-nadella-copilot-autopilot]] — first-seen
- [[satya-nadella]] · [[microsoft]]
- 관련: [[compute-constrained-growth]] · [[intelligence-as-infrastructure]] · [[software-marginal-cost]]
