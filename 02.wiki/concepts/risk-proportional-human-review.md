---
title: 위험 비례 사람 검토 (Risk-Proportional Human Review)
type: concept
category: pattern
tags: [human-in-the-loop, review, risk, automation, force-multiplier, migration, agents]
aliases: [승수로서의 AI, 가장 위험한 결정 곁의 사람, force multiplier]
related: [agent-trust-curve, named-human-accountability, verification-bottleneck, legacy-code-modernization, syntactically-correct-behaviorally-wrong, task-entropy-matrix, decision-quality, goal-level-delegation]
first-seen: tech-bridge-legacy-code-modernization-ai
sources: [tech-bridge-legacy-code-modernization-ai]
created: 2026-09-18
updated: 2026-09-18
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

## References

- [[tech-bridge-legacy-code-modernization-ai]] · [[anna-gutowska]] · [[ibm]]
- 관련: [[agent-trust-curve]] · [[named-human-accountability]] · [[goal-level-delegation]] · [[task-entropy-matrix]] · [[verification-bottleneck]] · [[legacy-code-modernization]] · [[syntactically-correct-behaviorally-wrong]] · [[decision-quality]]
