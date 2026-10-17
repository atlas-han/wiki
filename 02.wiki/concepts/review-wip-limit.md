---
title: "리뷰 WIP 한도 (Review WIP Limit)"
type: concept
category: pattern
tags: [verification-bottleneck, code-review, autonomous-agents, wip-limit, flow-control, human-in-the-loop, cost-limits]
aliases: [review WIP limit, work in progress limit, 리뷰 용량 한도, PR 할당 한도, 에이전트 PR 유량 제어]
related: [verification-bottleneck, compressed-review-surface, risk-proportional-human-review, human-as-async-api, agent-roi-measurement, software-factory, automated-code-review, trusted-throughput]
first-seen: tech-bridge-atlassian-build-your-own-sdlc
sources: [tech-bridge-atlassian-build-your-own-sdlc]
created: 2026-10-17
updated: 2026-10-17
---

# 리뷰 WIP 한도 (Review WIP Limit)

**자율 에이전트가 내는 PR의 양을 생성 능력이 아니라 팀의 리뷰 용량에 맞춰 묶는 설정.** 1인당 주당 PR 수, 진행 중 작업(WIP) 한도, 티켓·주 단위 비용 한도로 구현한다. 사람이 리뷰할 차례가 오면 적절한 때에 호출한다. [[andrei-bocan|Andrei Bocan]]([[atlassian|Atlassian]])이 [[tech-bridge-atlassian-build-your-own-sdlc]]에서 AutoDev의 설정으로 설명했다.

> *"with autod we want to be mindful of how much work we're actually hoisting on your team uh nobody wants to spend time reviewing uh 50 PRs a day so like we have configuration for letting you say cool like my team wants to get assigned I don't know each individual gets assigned three five PRs a week"* (41:41~42:01)

> *"the work in progress limit (…) where you want to make sure that like your team isn't getting inundated with PRs or like other work that might not be necessarily the work that you want to drive forward"* (43:50~44:00)

## 왜 필요한가 — 리뷰에서 일이 죽는다

> *"the other bit that we've also noticed with some of these autonomous workflows is the the the reviewing step is where things go to die. Um because people again are uh busy with other things."* (45:28~45:40)

- **큰 변경은 승인되지 않는다**: *"nobody's going to approve a PR that's like change half your code base because now you have a new standards (…) or (…) anything that like causes like a high amount of churn"*(41:32~41:41). 그래서 기존 코드를 기준에 맞출 때도 PR을 **점진적으로** 낸다(41:20~41:31).
- **비용 한도는 같은 장치의 다른 축**: *"set limits for how much we want to spend per ticket how much we want to spend per week all that stuff seems like it's uh just table stakes at this point"*(44:18~44:28)

## 세 부품

1. **유량 상한** — 1인당 주 3~5 PR(설정 예시), WIP 한도, 티켓·주 단위 비용.
2. **입구 필터** — 명세가 부족한 백로그 항목(*"one summary line that says is do the thing"* 44:56~44:58)은 에이전트가 집지 않고 사람에게 명세를 요청한다(45:08~45:18). → [[spec-driven-development]]
3. **사람 호출** — *"reach out to people at the opportune time in order to pull them in"*(45:43~45:46). 첫 릴리스의 수단은 Slack이다(45:55~46:00). → [[human-as-async-api]]

## 위키의 다른 페이지와

- [[verification-bottleneck]]의 답 가운데 **생성 쪽 유량을 리뷰 용량에 맞추는** 갈래다. 리뷰를 자동화하는 쪽([[automated-code-review]], Gitar의 *"more AI"*)이나 리뷰할 면을 줄이는 쪽([[compressed-review-surface]])과 다르다. 셋은 함께 쓸 수 있다.
- [[software-factory]]: 공장 루프가 사람 리뷰 용량이라는 제약을 어떻게 다루는지에 대한 한 벤더의 답이다. 사람을 루프 밖으로 빼는 대신 루프의 속도를 사람에게 맞춘다.
- [[trusted-throughput]]: 처리량을 "생성된 PR 수"가 아니라 "팀이 소화한 PR 수"로 보는 쪽이다.
- 칸반의 WIP 한도와 같은 이름과 같은 논리(병목 단계 앞에서 유입을 묶는다)다. ⚠️ 화자가 칸반을 언급하지는 않는다.

## ⚠️ 유보

- 단일 벤더 소스다. 한도 값(3~5 PR)은 **설정 예시**이고 권장치나 측정 결과가 아니다.
- 한도를 넘은 작업이 대기열에서 어떻게 우선순위가 매겨지는지, 한도가 리드타임에 주는 효과는 발화되지 않는다.

## References

- [[tech-bridge-atlassian-build-your-own-sdlc]]
