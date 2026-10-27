---
title: 위험 비례 사람 검토 (Risk-Proportional Human Review)
type: concept
category: pattern
tags: [human-in-the-loop, review, risk, automation, force-multiplier, migration, agents]
aliases: [승수로서의 AI, 가장 위험한 결정 곁의 사람, force multiplier]
related: [agent-trust-curve, named-human-accountability, verification-bottleneck, legacy-code-modernization, syntactically-correct-behaviorally-wrong, task-entropy-matrix, decision-quality, goal-level-delegation, model-calibration, system-1-model, action-reversibility, human-as-async-api, three-level-agent-review]
first-seen: tech-bridge-legacy-code-modernization-ai
sources: [tech-bridge-legacy-code-modernization-ai, tech-bridge-sdd-enterprise-lessons, tech-bridge-conductor-orchestras-not-factories, tech-bridge-warp-factory-engineering, tech-bridge-death-of-code-review, tech-bridge-jev-calibrated-decisions, tech-bridge-pocock-pr-bottleneck, tech-bridge-human-is-async-api, tech-bridge-gitar-agentic-pr-validation, tech-bridge-dental-clinic-ax-transformation, tech-bridge-three-level-agent-review, tech-bridge-pocock-skills-implement-spec-pr-retro, tech-bridge-laurie-voss-product-engineer]
created: 2026-09-18
updated: 2026-10-27
---

# 위험 비례 사람 검토

**AI에게 기계적인 일을 배속시키고, 사람은 가장 큰 위험을 수반하는 결정 곁에 둔다.** 사람의 자리를 *루프 안/밖* 이나 *단계* 로 정하는 대신 **결정의 위험도**로 정하는 배치. [[anna-gutowska|Anna Gutowska]]([[ibm|IBM]])가 [[tech-bridge-legacy-code-modernization-ai]]의 처방으로 제시했다.

> 최고의 성과를 내는 팀들은 **AI를 자동화의 승수(force multiplier)로 활용**합니다. 그들은 이를 통해 **기계적인 작업 속도를 높이는 동시에, 가장 큰 위험을 수반하는 결정에 경험 많은 엔지니어들이 가까이 있도록** 합니다. 이러한 방식으로 AI를 사용하면 레거시 코드 마이그레이션이 **더 빠를 뿐만 아니라 더 철저하게** 이루어집니다. (08:26~08:48)

> ⚠️ ko는 *force multiplier* 를 **"시너지 효과"** 로 옮겼다. *승수* 는 **한 사람의 효과를 배로** 한다는 뜻이고, 그래서 이 문장의 구도(기계적 일은 배속, 위험한 결정은 사람)가 성립한다.

## 무엇이 다른가

이 위키가 가진 *사람의 자리* 명제들과 나란히 놓으면:

| 페이지 | 사람을 두는 기준 |
|---|---|
| [[agent-trust-curve]] (Lauren Tan) | **시간** — in-loop → 자동 병합 + 사후 리뷰로 **옮겨 간다** |
| [[named-human-accountability]] | **책임** — 이름 붙은 사람이 있어야 한다 |
| [[goal-level-delegation]] | **추상 수준** — 목표는 사람, 실행은 에이전트 |
| [[task-entropy-matrix]] | **수용 기준의 불확실성** — 검증이 실행과 구분되지 않으면 에이전트를 만들지 않는다 |
| **이 페이지** | **결정의 위험도** — 위험이 큰 결정 *곁에* 사람 |

[[task-entropy-matrix]]와 가장 가깝다 — 그쪽은 *어떤 작업을 에이전트에게 줄지*, 이쪽은 *한 작업 안에서 사람이 어디 서 있을지* 다. 그리고 **동일한 마이그레이션 안에서 자리가 갈린다** — 발견·번역·테스트 작성은 배속하고, *무엇을 서비스로 쪼갤지 · 어느 로직을 보존해야 하는지* 같은 결정은 사람이 본다(⚠️ 이 예시는 위키의 추론이다 — **소스는 "가장 큰 위험을 수반하는 결정"의 예를 들지 않는다**).

## 왜 "더 철저하게"인가

화자의 주장은 속도만이 아니다 — *"더 빠를 뿐만 아니라 더 철저하게"*. 논리는 이렇다: 기계적인 일(읽기·요약·번역·테스트 작성)이 배속되면 **사람의 시간이 위험한 결정으로 옮겨가고**, 그 결정이 더 많은 주의를 받는다. 즉 [[verification-bottleneck|검증 병목]]을 없애는 것이 아니라 **병목을 가장 값진 자리로 옮기는** 처방이다.

## 같은 소스 안의 긴장

같은 영상이 에이전트를 *"최소한의 사람 개입으로 순차적으로"*(05:24)라고 소개하고, 처방에서는 *"테스트, 사람 검토 및 검증을 마이그레이션 전 구간에"*(08:18)라고 한다. **개입을 줄이는 것과 검토를 전 구간에 두는 것이 같은 영상 안에서 정리되지 않는다** — 이 페이지의 기준(위험도)으로 읽으면 *개입은 줄이되 위험한 결정에는 남긴다* 가 되지만, **그렇게 말한 것은 위키이지 화자가 아니다.**

## 표시해 둔 것

> ⚠️ **"가장 큰 위험을 수반하는 결정"이 무엇인지 예시가 없다.** *"최고의 성과를 내는 팀"* 이 누구인지, 근거가 무엇인지도 없다. 위험도를 **누가 어떻게 판정하는가**(사람이 판정하면 그 판정이 병목)도 다뤄지지 않는다.

## 구체 예 — ERP 모듈의 criticality (2026-10-02 · [[tech-bridge-sdd-enterprise-lessons]])

위 IBM 편이 예시 없이 말한 "가장 위험한 결정"에 [[simon-martinelli|Simon Martinelli]]가 예를 붙인다. ERP의 모듈은 *"don't have all the same, how should I say, criticality"*(07:24~07:31) — 재고 관리가 멈추면 *"they can just go and grab a coffee"*(07:39~07:41), 주문 관리가 멈추면 *"the company probably will lose money"*(07:47~07:50). *"So you should do risk management and then decide how much review um your code probably needs. But that's not different from AI or manual driven development."*(07:52~07:59) 리뷰 방식은 PR 없이 **trunk-based + 두 개발자의 peer review**(24:38~25:04). ⚠️ 모듈별 리뷰 강도를 어떻게 정하는지의 기준표는 없다. ko는 *criticality* 를 **"비판적 사고"** 로 옮겼다.

## References

- [[tech-bridge-legacy-code-modernization-ai]] · [[anna-gutowska]] · [[ibm]]
- 관련: [[agent-trust-curve]] · [[named-human-accountability]] · [[goal-level-delegation]] · [[task-entropy-matrix]] · [[verification-bottleneck]] · [[legacy-code-modernization]] · [[syntactically-correct-behaviorally-wrong]] · [[decision-quality]]

## 코드베이스 구역판 — 슬롭 없는 구역 (2026-10-02 · [[tech-bridge-conductor-orchestras-not-factories]])

[[conductor|Conductor]]의 [[slop-free-zone]]은 이 페이지의 기준(결정의 위험도)을 **코드 위치**로 옮긴 형태로 읽힌다 — *"in our CI uh any change to migrations file requires the a uh a human to review it"*(05:51~06:02). DB 마이그레이션처럼 **되돌리기 어려운 곳**에는 강제 사람 검토, 나머지는 *"very loose"*(05:28~05:31). 이 페이지가 비워 둔 *"가장 큰 위험을 수반하는 결정의 예"* 에 대한 실무 사례 하나. ⚠️ 위험도 기준이라는 연결은 위키의 정리이며, 화자는 위험이라는 말을 쓰지 않는다.

## 공장의 코드 리뷰 칸 — 에이전트 먼저, 사람 투입은 리스크 관리 (2026-10-03 · [[tech-bridge-warp-factory-engineering]])

[[zach-lloyd|Zach Lloyd]]([[warp|Warp]])는 [[software-factory]]의 리뷰 단계를 *"in many ways the most painful part"*(10:53~10:54)라 하고, 처방을 이 원칙의 언어로 말한다 — *"I would have an agent do code review first, and then it becomes over time like a risk management exercise of like when do you bring in humans to do code review, but you want to have a step in here where humans can do it."*(10:59~11:13) 사람의 자리는 없애지 않고 **언제 부를지를 위험으로 정한다.** ⚠️ 위험 기준(무엇이 사람을 부르는가)은 말하지 않는다 — [[slop-free-zone]]의 migrations CI 게이트 같은 구체 규칙이 없다.

## 사람 체크포인트가 살아남는 세 자리 (2026-10-03 · [[tech-bridge-death-of-code-review]])

[[laurie-voss|Laurie Voss]]가 업계 사례를 훑은 뒤 같은 배치를 **관찰**로 내놓는다 — 사람 체크포인트는 *"moving around uh but it is surviving in predictable places"*(19:46~19:50):

1. *"where correctness isn't cheaply checkable"* → [[mergeability-gap]]
2. *"where uh the blast radius is large"* — 보안 민감 환경에선 사람 리뷰를 빼자는 말에 *"an immediate no"* (19:54~20:04)
3. *"wherever someone has to put their name on the result"* (20:04~20:08) → [[named-human-accountability]]

이 페이지의 기준(결정의 위험도)에 **검증 비용**(1번)과 **귀속**(3번)이 붙었다. 그리고 역할은 위로 — *"from inspecting the code directly to designing and tuning the systems that inspect the code and designing the definition of good"*(20:13~20:22). → [[automated-code-review]]

## 위험 비례를 숫자 하나로 — 보정된 확률의 임계값 (2026-10-09 · [[tech-bridge-jev-calibrated-decisions]])

분류 확률이 **> 0.9면 자동, 0.1~0.9면 사람, < 0.1이면 무시**(지원 이메일의 환불 판정, 10:45~12:05, 값은 예시). *"Because the numbers are calibrated, the threshold also tells us roughly how often the automatic path will be wrong. So the more a mistake is going to cost, the higher we would set the threshold."*(12:05~12:20) — 이 페이지의 *가장 위험한 결정 곁에 사람을* 이 **실수 비용에 맞춰 조정하는 임계값**으로 구현된다. 전제는 확률이 **보정돼 있다**는 것이다 → [[model-calibration]]. ⚠️ 사람 구간(0.1~0.9)으로 떨어지는 **물량**은 말하지 않는다 → [[verification-bottleneck]]

## PR 단위의 기준 — "every single one-way door you do" (2026-10-09 · [[tech-bridge-pocock-pr-bottleneck]])

[[matt-pocock|Matt Pocock]]은 이 원칙을 **PR 하나하나에 붙는 라벨**로 만든다 — 첫 원칙 *"some reviews are more important than others"*(17:02~17:07), 기준은 one-way/two-way door와 blast radius([[action-reversibility]]), 결과는 PR 하단의 *merge danger* 요약(18:22~18:32). 결론: *"You really don't need to review every single two-way door. Every single one-way door you do."*(22:06~22:12) IBM 편이 비워 둔 *"가장 위험한 결정이 무엇인가"* 에 Martinelli(모듈 criticality) · Conductor(마이그레이션 파일)에 이어 **세 번째 구체 예**(이메일 대량 발송 · 비싼 마이그레이션 · 데이터 손실)가 붙는다.

> ⚠️ ko 자막은 결론 문장을 캡션 경계에서 **"되돌릴 수 있는 모든 결정을 검토하십시오"** 로 쪼개 반대로 읽히게 했다(22:07~22:12). 위험도를 누가 판정하는지는 이 소스에서도 열려 있다.

## 반대편 비용에 이름이 붙는다 — alert fatigue (2026-10-10 · [[tech-bridge-human-is-async-api]])

[[temporal|Temporal]] 직원(설명란 기준 Melanie Warrick)이 *"When should the human be in the loop?"*(16:31)에 같은 기준으로 답한다 — *"the big thing you want to take into consideration is the cost of being wrong is high. Okay, it's a case- by case basis"*(16:35~16:43), *"especially in a security standpoint"*(17:02~17:04). 이 페이지의 소스들이 대개 **사람을 덜 부를 때의 위험**만 말했다면, 여기선 **사람을 너무 자주 부를 때의 비용**이 짝으로 선다: *"alert fatigue is real (…) you just start saying yes, yes, yes, yes, yes every time it asks you questions. So, you're trying to balance between those two"*(17:06~17:16). 사람을 부르는 쪽의 구현(대기를 blocking call로 만들지 않기)은 → [[human-as-async-api]].

> ⚠️ 기준선·수치·처방 없음 — *"That's the thing you've got to evaluate for the problems that you're solving."*(17:26~17:29) ko는 *cost of being wrong is high* 를 **"실수할 확률이 높습니다"** 로 옮겨 기준을 *비용* 에서 *확률* 로 바꿨다 — 이 페이지와 [[model-calibration]]이 구분하는 바로 그 두 축이다(Jev 편의 임계값은 *확률* 을 *비용* 에 맞춰 조정한다).

> ⚠️ **Contradiction (2026-10-14 · [[tech-bridge-gitar-agentic-pr-validation]])**: 이 페이지는 사람이 반드시 볼 변경을 위험도로 가른다(Pocock: *"Every single one-way door you do."*). [[gitar|Gitar]]의 [[ali-reza|Ali-Reza]]는 자동 승인·머지 조건을 *"you can define rules and conditions that control when uh PRs get automatically approved by the agent and merged automatically"*(05:18~05:31)로 **사용자 설정에 넘기고**, 어떤 PR이 자동 머지에서 빠져야 하는지는 말하지 않는다. 위험 비례 기준이 제품에 기본값으로 들어 있는지는 이 소스로 알 수 없다.

## 1인 사업장 판본 — 운영 설정만 직접 승인 (2026-10-17 · [[tech-bridge-dental-clinic-ax-transformation]])

1인 사업장 판본이다. 에이전트가 만들고 시험하고 고치되 *"실제 운용 설정을 바꾸는 중요한 순간에는 본인이 직접 승인"*(06:27~06:31)하고, 보험 서류는 77%를 자동 확정하고 나머지 줄만 사람이 본다(03:18~03:36). 위험이 큰 결정에 사람을 두는 배치가 해설 전언으로 확인된다.

## 위험이 오르면 늘어나는 것은 에이전트 검토 단계 — "not by me" (2026-10-20 · [[tech-bridge-three-level-agent-review]])

> ⚠️ Contradiction(긴장): [[corey-gallon|Corey Gallon]](⚠️ 이름 *추정*)은 *"the highest-stakes example"*(08:53)인 법적 요구서의 검토를 **persona 에이전트**(litigator · vendor's counsel · auditor, *"The two lawyer agents"* 10:26)에게 맡기고, 결론을 *"I believe them because everything I rely on has been thoroughly reviewed and validated first. And most importantly, not by me."*(11:57~12:03)로 맺는다. 위험에 비례해 올라가는 것은 사람의 개입이 아니라 검토 단계의 수다(*"Each level adds to the one before as the stakes go up."* 03:45~03:47). 이 페이지의 배치(가장 큰 위험의 결정 곁에 경험 많은 사람)와 갈린다. 다만 ① 사례 1의 첫 거짓은 **화자의 질문**으로 드러났고(*"It came out when I questioned the results."* 04:43~04:45), ② 요구서 발송을 결정한 사람·사람 변호사의 최종본 검토 여부는 발화되지 않는다. 그래서 "사람이 없다"가 아니라 **"사람이 검토자 자리에서 빠진다(결정자 자리는 미발화)"**로 읽는다. → [[three-level-agent-review]] · [[named-human-accountability]]

## merge danger — 리뷰를 없애지 않고 어디를 볼지 알려 준다 (2026-10-25 · [[tech-bridge-pocock-skills-implement-spec-pr-retro]])

/pr 스킬의 세 번째 칸(발췌, 화자 추정 [[eric-tech|Eric Tech]]): *"if this po quest[pull request] breaks what is impact in production can we actually roll back if something happen and also what is the blast radius"*(03:01~03:11). 해설: *"위험을 적는다고 검토가 없어지는 건 아니에요. 어디를 더 꼼꼼히 봐야 할지 알려 주는 거죠."*(03:22~03:26) [[tech-bridge-pocock-pr-bottleneck]]의 one-way/two-way door가 **PR 템플릿의 한 칸**이 됐다.

## "high blast radius code"만 리뷰하라 (2026-10-27 · [[tech-bridge-laurie-voss-product-engineer]])

[[laurie-voss|Voss]]의 첫 처방이다. *"be prepared for a world in which humans are barely involved in the production of code. So, write down your high blast radius code and make that be the only thing that you are reviewing anymore because the rest of it your automatic reviewers are going to get done."*(05:59~06:12) 핵심은 위험한 코드를 **미리 적어 둔다**는 것이다. 위험 판정을 PR마다 하지 않고 목록으로 고정한다. 10-25 merge danger(PR마다 위험 지점을 표시하는 방식)와 비교된다.
