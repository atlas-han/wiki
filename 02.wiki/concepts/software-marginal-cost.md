---
title: 한계비용이 생긴 소프트웨어 (Software with Marginal Cost — 좌석은 사용 권리)
type: concept
category: theory
tags: [business-model, pricing, tokens, subsidy, seats, usage-based, microsoft]
aliases: [소프트웨어의 한계비용, 좌석 + 사용량, seats are entitlements to usage, 보조금의 끝]
related: [transaction-cut-monetization, agent-roi-measurement, overspending-underusing-loop, model-mixing-economics, compute-constrained-growth, inference-revenue-training-rnd, token-roles]
first-seen: tech-bridge-nadella-copilot-autopilot
sources: [tech-bridge-nadella-copilot-autopilot]
created: 2026-09-29
updated: 2026-09-29
---

# 한계비용이 생긴 소프트웨어

**전통 소프트웨어는 한 부를 더 파는 비용이 0에 가까웠지만, AI 소프트웨어는 사용할 때마다 토큰을 태우므로 처음으로 한계비용을 갖는다 — 지금의 보조금은 끝나고, 모든 사업 모델은 결국 그 비용을 누가 대는지로 설명돼야 한다**는 프레이밍. [[satya-nadella|Satya Nadella]]가 [[tech-bridge-nadella-copilot-autopilot]]에서 상시 가동 에이전트의 비용 질문에 답하며 세웠다.

> **once the subsidy stop[s] for everybody, this is going to — there's marginal cost to tokens.** (04:55~05:02)
> **there are finite number of business models that have to ultimately account for the fact that software for the first time has marginal cost.** (05:43~05:49)

> ⚠️ **당사자 진술.** 좌석+사용량 과금을 파는 회사의 CEO가 **자기 가격 구조를 정당화하는 맥락**에서 나온 말이다. 토큰 원가·보조금 규모·마진 수치는 하나도 없다.

## 세 단계의 논리

| 단계 | 소스 |
|---|---|
| **① 보조금은 일시적** — *"there's a certain amount of subsidy anyone can do. But at the end of the day, this all has to be about return that the user gets"* | 05:07~05:16 |
| **② 사업 모델은 유한하다** — 구독 · 종량제(pay as you go) · 광고 같은 양면 시장 · 거래 | 05:28~05:43 |
| **③ 좌석은 사용 권리의 포장** — *"seats are nothing other than entitlements to usage"*, *"a more convenient way to budget and buy versus just having usage-based billing"* | 06:16~06:27 |

③이 핵심이다. 좌석(seat) 과금은 한계비용 0 시대의 형식인데, 이것을 **"미리 정한 사용량 묶음"** 으로 재정의해 한계비용 시대에도 유지한다. 그 위에 사용량 과금을 얹는다 — *"usage-based functionality that any user at any time can use with no limits"*(06:48~06:53). 진행자 정리로는 **Chat은 좌석, Co-work·Autopilot은 사용량**(05:50~05:59).

비용 곡선은 내려간다고 본다 — *"Autopilot will start with a certain cost footprint and it'll only reduce after that"*(07:35~07:38). 그래서 구독의 약속은 *"deliver more value every day of the week as models … improve"*(06:40~06:48), 즉 **같은 좌석 값에 더 많은 가치**다.

## 이 위키에서의 좌표

- [[transaction-cut-monetization]] — ⚠️ **대립.** [[mark-zuckerberg|Zuckerberg]]의 [[muse|Muse]]는 **주당 1억 토큰 무료**로 사용자 쪽 한계비용을 **없애고** 거래 상대 기업에서 몫을 뗀다. Nadella는 그런 보조금이 *"for everybody"* 끝난다고 본다. 단 그의 유한 목록에도 *"transactions"* 와 *"an ad"* 가 들어 있다 — 두 사람은 **한계비용을 누가 대는가**(상대 기업 vs 사용자 기업)에서 갈린다.
- [[overspending-underusing-loop]] · [[agent-roi-measurement]] — 사용량 과금은 **"쓴 만큼 가치가 있었나"** 를 증명할 척도를 요구한다. Nadella는 *"aligned with the ROI the customer see[s]"*(07:14~07:18)라 말하지만 척도를 제시하지 않는다.
- [[model-mixing-economics]] — 한계비용이 있으면 **싼 모델로 라우팅**하는 것이 곧 원가 관리다. 같은 대담의 *"auto가 제품"* 과 한 쌍이다.
- [[inference-revenue-training-rnd]] — 같은 대담에서 공급 쪽 등식(추론 = 매출). 이 페이지는 **수요 쪽**(누가 추론 비용을 내나)이다.
- [[token-roles]] — 토큰을 비용·매출·가치 중 무엇으로 셀지의 문제와 같은 자리.

## ⚠️ 유보

- **"보조금"의 주체** — 누가 지금 보조하고 있는지(모델 회사? MS 자신?) 말하지 않는다.
- **"no limits"와 비용** — 사용량 과금 기능이 *"no limits"* 라는 것은 **사용자가 무제한으로 쓸 수 있고 무제한으로 낸다**는 뜻으로 읽히나, 기업 예산 통제 수단은 [[agent-365|Agent 365]]의 *"finops"* 한 단어뿐이다.
- **비용 하락 전망**(*"it'll only reduce"*)의 근거 없음 — [[compute-constrained-growth]]의 *"효율은 수요가 삼킨다"* 와 긴장이 있다(단가는 내려도 총비용은 오를 수 있다).

## References

- [[tech-bridge-nadella-copilot-autopilot]] — first-seen
- [[satya-nadella]] · [[microsoft]] · [[microsoft-copilot]]
- 대비: [[transaction-cut-monetization]] · [[tech-bridge-zuckerberg-muse-personal-agent]]
