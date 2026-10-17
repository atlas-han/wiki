---
title: "노력 → 산출 → 결과 → 미션 (Effort, Output, Outcome, Mission)"
type: concept
category: framing
tags: [metrics, productivity, goodhart, outcomes, mission, kent-beck, lines-of-code, pr-count]
aliases: [effort output outcome impact, effort-output-outcome-impact, 노력 산출 결과 미션, tyranny of metrics, 지표의 폭정]
related: [trusted-throughput, value-maxing, ai-measurement-framework, perceived-vs-actual-productivity, agent-roi-measurement, outcome-engineering, features-vs-futures]
first-seen: tech-bridge-kent-beck-craft-augmented-development
sources: [tech-bridge-kent-beck-craft-augmented-development, tech-bridge-factory-bug-report-to-production]
created: 2026-10-09
updated: 2026-10-17
---

# 노력 → 산출 → 결과 → 미션

**소프트웨어 작업은 노력(effort) → 산출(output, 전달된 기능) → 결과(outcome, 사용자 행동의 변화) → 미션(만드는 쪽과 쓰는 쪽이 공유하는 목적)의 사슬이고, 측정은 앞쪽일수록 쉽고 Goodhart에 취약하며 뒤쪽일수록 중요하지만 귀속이 어렵다.** [[kent-beck|Kent Beck]]이 [[tech-bridge-kent-beck-craft-augmented-development]]에서 *"10 or 15 years"* 묵힌 그림의 개정판으로 내놓았다 — 마지막 칸은 원래 *impact* 였고, 강연 당일 아침 다른 연사를 듣고 *mission* 으로 바꿨다고 한다.

> *"I used to use the word impact but I love this word mission (…) and the mission is shared between the people making the program and the people using the program."* (45:32~45:52)

## 네 칸 (자막)

| 칸 | 화자 정의 | 예 |
|---|---|---|
| **노력 effort** | *"you put in a certain amount of effort"*(44:08~44:14) | ⭐ *"The Genie produced 200,000 lines of code. That's a measure of effort."*(46:00~46:05) |
| **산출 output** | *"a new feature that you can deliver to your customers and that's output"*(44:14~44:24) | PR 수(47:22) |
| **결과 outcome** | *"the customers use that feature and their behavior changes"*(44:24~44:31) — 행동이 안 바뀌면 *"we didn't need to produce the software"* | 웹 이후 관찰 가능해졌다(44:46~45:09) |
| **미션 mission** | 만든 쪽과 쓰는 쪽이 공유(45:47~45:52) | *"making enough money for my next yacht (…) or making the country safer"*(46:13~46:25) |

> ⚠️ **ko·en 자막에서 산출과 결과가 같은 말이 된다** — *"that's output"* 이 en *"that's the result"*, ko "결과"(44:22). 이 그림은 en-orig로만 읽을 것.

## 지표의 폭정 (tyranny of metrics)

- 노력·산출이 *"the easiest thing to measure"* 이라 *"we look for our keys under the lamp post"*(46:38~46:44).
- 생산성 = 산출/투입이라 지니의 대량 산출이 생산성처럼 보인다(46:48~47:07).
- *"lines of code, which we've known was Boulder Dash for a very very long time and somehow it's back PR count"*(47:10~47:22) — 노력·산출의 측정은 *"per definition not a measure of mission"*(47:28~47:35).
- 지니 10개 = 노력 10배, *"Yeah, but it doesn't matter."*(48:10~48:15)

## Goodhart — 앞쪽일수록

- *"the earlier in this cycle you measure, the more likely you are to see um Goodart's law"*(48:24~48:31).
- ⭐ *"I think Goodart was an optimist. It's not just that the measure ceases to be a measure. It's that people will twist the entire system out of shape. They'll make it worse in order to get better measures."*(48:41~48:56) — 잃는 것은 가시성이 아니라 **미션의 진척**(48:59~49:08).
- 뒤쪽일수록 **귀속이 어렵다** — *"the mission is now 7% better and I own 075% of that"*(49:17~49:24, ⚠️ 0.75%/0.075% 판독 불가). 미션의 가치는 *"bursty"* — 위기가 와야 준비됐음을 안다(47:42~47:51).

## 처방 — 리더십

측정 대신 **표현과 반복**: *"find an expression of the mission that speaks to people's heads and their hearts. And then you have to repeat it"*(50:15~50:25). 화자는 미션 측정 방법을 제시하지 않는다.

## 이 위키에서의 자리

- [[trusted-throughput]] — *"토큰은 LOC다"* 와 같은 결론. Beck은 LOC·PR 수를 **노력/산출 칸**에 놓는 위치 지도를 준다. Lauren Tan 편의 PR 수 Goodhart 실례와 직접 겹친다.
- [[value-maxing]] — 토큰맥싱 → 최소화 → 가치. Beck의 사슬로 보면 셋 다 **노력 칸**의 다툼이고, 가치는 결과·미션 칸이다.
- [[ai-measurement-framework]] — DX의 utilization·impact·cost는 **측정 가능한 쪽**에서 출발한다. Beck은 측정 가능한 쪽일수록 Goodhart에 가깝다고 본다(긴장, 화해 발언 없음).
- [[outcome-engineering]] — 에이전트에게 how 대신 결과를 지정하라는 처방과 같은 방향, 층은 다르다(프롬프트 vs 조직 지표).
- [[features-vs-futures]] — 같은 강연의 첫 그림. futures 투자는 산출 지표에 **보이지 않는다**.

> ⚠️ 그림 자체는 업계에 흔한 output/outcome/impact 구분과 겹친다. 이 위키는 **Beck의 이 강연에서의 정의와 "mission" 개정만** 기록한다 — 이전 버전의 출처는 확인하지 않았다.

## References

- [[tech-bridge-kent-beck-craft-augmented-development]] · [[kent-beck]]

## "measure outcomes, not tokens" — 벤더의 같은 구분 (2026-10-17 · [[tech-bridge-factory-bug-report-to-production]])

[[davis-palmie|Davis Palmie]]([[factory-ai|Factory]]): *"you want to measure outcomes, not tokens. Lines of code and tokens generated are gameable metrics. These are not actually associated with outcomes."*(16:18~16:31) 토큰 리더보드는 *"Goodhart's law in real time"*(16:39~16:41)이라고 한다. Beck의 네 칸 가운데 노력·산출 쪽 지표를 Goodhart로 부정하는 같은 논리다. 대신 내놓는 이름은 *"signal to production time, human intervention count, median time to repair, shelf life of code, and cost per PR"*(17:02~17:10)이다.

⚠️ 다섯 지표가 이 페이지의 *outcome* 칸에 드는지 *output* 칸에 드는지는 정의가 없어 판정하지 않는다(예: *cost per PR* 은 PR 단위다). 맺음 *"Your end users don't care about how much you're spending on AI."*(17:49~17:53)는 *mission* 쪽을 가리키지만 지표로 이어지지 않는다.
