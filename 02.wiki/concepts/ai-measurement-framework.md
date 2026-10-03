---
title: "AI 측정 프레임워크 (AI Measurement Framework) — utilization · impact · cost"
type: concept
category: pattern
tags: [measurement, ai-adoption, developer-productivity, cohorts, roi, token-economics, getdx, vendor-framework]
aliases: [AI Measurement Framework, AI 측정 프레임워크, utilization impact cost, 활용도·임팩트·비용]
related: [agent-roi-measurement, value-maxing, trusted-throughput, overspending-underusing-loop, dora-metrics, perceived-vs-actual-productivity, agent-readiness, mousepower]
first-seen: tech-bridge-dx-ai-impact-trends
sources: [tech-bridge-dx-ai-impact-trends]
created: 2026-10-03
updated: 2026-10-03
---

# AI 측정 프레임워크 (AI Measurement Framework)

**AI 코딩 도구의 효과를 새 지표가 아니라 이미 믿는 기초 지표(developer experience·생산성·품질) 위에서, 사용자 코호트를 비교해 재는 틀 — 세 차원 utilization · impact · cost.** [[getdx|DX]]의 [[justin-reock|Justin Reock]]이 [[tech-bridge-dx-ai-impact-trends]]에서 소개했다(자세한 방법론은 DX 백서, 이 위키는 읽지 않았다).

> *"we're all going to have to answer this question this year, right? Spent 10 million or way more (…) on tokens. uh where's our 10x productivity?"* (10:49~11:02)

> ⚠️ **벤더 프레임워크.** 측정 플랫폼 회사가 자사 백서로 배포하는 틀이다. 발표는 *"I won't spend too much time on this"*(11:45~11:47)라며 개요만 말한다. 이 페이지는 발화된 내용만 적는다.

## 출발점 — 측정은 AI 전에도 풀리지 않았다

> *"measuring developer productivity and measuring developer experience was a challenge before AI and we we never completed that conversation before kind of throwing accelerant on this"* (10:33~10:43)

지금은 *"even more difficult (…) because it's confounded by several different aspects of of AI"*(10:45~10:49).

## 원칙 — 기초 지표를 버리지 않는다

> *"it's important to bear in mind that we don't throw away what we're measuring, right? Our foundational developer experience and developer productivity metrics are still what matter the most"* (11:05~11:14)

1. 도구의 **API 텔레메트리**로 *"who's using what and where"* 를 파악해 **사용자 코호트**를 나눈다(11:20~11:31)
2. 코호트를 **기초 지표 위에서 비교**한다 — *"What is this actually doing to quality? What is this actually doing to speed? What is this doing to impact to the organization and value generation?"*(11:34~11:42)
3. 예: 두 코호트를 *"PR cycle time or PR size or push back and review"*(12:59~13:05)로 비교

## 세 차원과 성숙도 곡선 (12:02~12:52)

| 차원 | 무엇을 | en-orig |
|---|---|---|
| **Utilization** | DAU·WAU, 누가 무엇을 얼마나, 어떤 사용 사례에 | *"our daily active users, weekly active users"* (12:06~12:08) |
| **Impact** | 사용량이 오를 때 **어떤 지표가 움직이길 기대하는가** | *"as our utilization goes up, what do we hope to see in terms of impact to the business?"* (12:14~12:21) |
| **Cost** | 토큰 비용 | *"It's a fair joke that we're 15 years after the last major hype cycle and we're still trying to figure out cloud cost"* (12:21~12:28) |

*"you can think about this as a bit of a maturity curve as well. Most people start with utilization on the left"*(12:29~12:36) — 활용도 파악에서 시작해 impact 지표와 교차하는 데까지(12:40~12:50).

## 곁가지 — 에이전트에게 묻기

같은 발표는 측정 대상에 **에이전트 자신**을 넣는다: 에이전트가 *"steering with the human, the the context that was provided for them, the the feedback cycles"*(14:16~14:24)에서 겪은 문제를 질적으로 보고하게 하고, 사용 사례별로 *"which use cases are giving us the most efficient token spend"*(14:35~14:39)를 본다. 같은 사용 사례에서 **주니어가 토큰을 더 쓰고 staff+는 더 적은 토큰으로 비슷한 시간을 아낀다**(09:27~09:50)는 관측이 여기서 나왔다. ⚠️ 수집 방법 미발화.

## 위키의 다른 페이지와

- **[[agent-roi-measurement]]** (Piras, 09-12) — *측정 문제가 있다*는 문제 제기에 수치가 없었다. 이 틀은 그 빈자리에 들어오는 **구체적 절차**(코호트 × 기초 지표). 단 Piras의 3번(*척도는 고객의 멘탈 모델에*)은 다루지 않는다 — 이 틀의 독자는 조직 내부 리더다.
- **[[value-maxing]] · [[overspending-underusing-loop]]** — 토큰·DAU는 *활동*이지 *가치*가 아니다. 이 틀은 utilization을 **성숙도 곡선의 왼쪽 끝**으로 위치시켜 같은 결론에 닿는다: 활동량에서 멈추지 말고 impact로.
- **[[trusted-throughput]]** — *새 지표 대신 신뢰하는 결과 지표*. Reock의 *"trusted metrics that we've already been looking at"*(11:16~11:20)과 표현까지 겹친다.
- **[[dora-metrics]]** — impact 차원에서 쓰는 기초 지표의 대표.
- **[[perceived-vs-actual-productivity]]** — 왜 체감 설문만으로는 안 되는가. 이 틀은 설문(DevEx)과 시스템 지표를 함께 쓴다.

## 미해결

- 코호트 비교의 **선택 편향** — AI를 많이 쓰는 사람은 원래 다른 사람일 수 있다. 통제 방법 미발화.
- impact 지표를 **사전에** 정하라는 것인지(*"what do we hope to see"*), 사후 탐색인지.
- cost 차원의 단위(토큰·달러·엔지니어 시간) — 미발화.

## References

- [[tech-bridge-dx-ai-impact-trends]] — first-seen
- [[getdx]] · [[justin-reock]]
- [[agent-roi-measurement]] · [[value-maxing]] · [[trusted-throughput]] · [[overspending-underusing-loop]] · [[dora-metrics]] · [[perceived-vs-actual-productivity]] · [[agent-readiness]] · [[mousepower]]
