---
title: 슬롭 없는 구역 (Slop-Free Zone)
type: concept
category: pattern
tags: [ai-slop, human-review, code-quality, coding-agents, ci, claude-md, agent-skills]
aliases: [slop-free zone, slop free zone, 슬롭 없는 청정 구역, slot free zone (ASR)]
related: [ai-slop, slop-cannon, risk-proportional-human-review, verification-bottleneck, context-engineering, agent-skills, company-brain, no-silent-write]
first-seen: tech-bridge-conductor-orchestras-not-factories
sources: [tech-bridge-conductor-orchestras-not-factories]
created: 2026-10-02
updated: 2026-10-02
---

# 슬롭 없는 구역 (Slop-Free Zone)

**코드베이스나 앱 가운데 엄격한 사람 검토를 요구하는 부분을 명시적으로 정하고, 나머지는 느슨하게 두는 것.** [[conductor|Conductor]]의 사내 용어로, [[charlie-holtz|Charlie Holtz]]가 [[tech-bridge-conductor-orchestras-not-factories]]에서 여섯 원칙의 세 번째로 소개했다.

> *"at Conductor, we have this term we call a slot[=slop] free zone. And a slot-free zone is a part of the codebase or a part of the app that requires really strict human review."* (04:59~05:17)

⚠️ en-orig ASR은 *slop*을 **"slot"** 으로 여섯 번 들었다. 공식 챕터 *"슬롭 없는 청정 구역을 만들어라"* 와 en-orig 자신의 *"anything written in Slack is slop free"*(06:02~06:05)가 바로잡는다. ko는 **"쓰레기"**, 요약에서는 **"개방적인 공간"**(정반대)으로 옮겼다.

## 핵심은 구역의 **비대칭**

> *"a lot of people assume that we are pure token maxers and we are like ripping through like 30,000 line PRs, but we're actually not. We're actually quite careful with certain parts of our codebase and then very loose with other parts of our codebase."* (05:18~05:31)

모든 코드를 똑같이 검토하는 것도, 아무것도 검토하지 않는 것도 아니다. **어디가 엄격한지를 먼저 정한다.** 정하지 않은 대가 — *"We we've had to rewrite our whole app like a couple of times because we weren't careful about slot[=slop] free zones."*(05:42~05:48) → [[slop-cannon]]

## 구역의 예 (Conductor)

| 구역 | 장치 | 성격 |
|---|---|---|
| **DB migrations 파일** | *"in our CI uh any change to migrations file requires the a uh a human to review it"* (05:51~06:02) | ⭐ **강제 게이트** — 이 소스에서 유일하게 자동화된 장치 |
| **Slack** | *"we also assume that anything written in Slack is slop free. It's it's not written by the AI, it's written by a human"* (06:02~06:07) | **가정** — 집행 장치 없음 |
| **docs · CLAUDE.md · AGENTS.md · 스킬** | *"we put a ton of time into making them good"* (06:09~06:16) | **정성** — 리뷰 게이트는 발화되지 않음 |

왜 CLAUDE.md·스킬이 구역인가 — **인턴 비유**: 새 인턴이 일을 시작할 때마다 귀에 속삭일 수 있다면 무엇을 속삭일지 깊이 고민할 것이다. *"this is what the cloud MD or agents uh MD is. It's like information that gets loaded into the agents context every time they start working."*(06:45~06:52) **매 세션 주입되는 컨텍스트는 오염의 반경이 가장 크다** — 그래서 슬롭이 들어가면 안 되는 자리다. → [[context-engineering]] · [[agent-skills]]

## 이 위키의 다른 페이지와

| 페이지 | 사람 검토의 자리를 무엇으로 정하나 |
|---|---|
| [[risk-proportional-human-review]] (IBM) | **결정의 위험도** |
| [[agent-trust-curve]] (Lauren Tan) | **시간** — 신뢰가 쌓이면 사후 리뷰로 |
| [[no-silent-write]] · [[company-brain]] | **지식 베이스 쓰기** — 에이전트는 제안, 사람이 수락 |
| **이 페이지** | **코드베이스·문서의 구역** — 되돌리기 어렵거나(migrations) 매번 주입되는(CLAUDE.md) 곳 |

[[ai-slop]]의 처방들이 *무엇이 슬롭인가*(정의·측정·예방)를 다뤘다면, 이 개념은 **어디서 슬롭을 허용하지 않을 것인가**를 정한다 — 생산량을 줄이지 않고 품질 하한을 지키는 배치.

> ⚠️ **"Slack은 슬롭이 없다"는 검증되지 않는 가정이다.** 사람이 AI 출력을 붙여 넣는 경우는 다뤄지지 않는다. 그런데 같은 발표의 [[company-brain|CIA]]는 Slack 메시지를 **자동으로** 사내 DB에 쌓는다 — 가정이 깨지면 에이전트 컨텍스트로 슬롭이 흘러든다.
>
> ⚠️ **구역을 누가·어떻게 정하는지**, 구역 밖 코드에 어떤 최소 기준이 있는지(테스트? 자동 리뷰?)는 발화되지 않는다. 효과 측정 없음.

## References

- [[tech-bridge-conductor-orchestras-not-factories]] (first-seen) · [[charlie-holtz]] · [[conductor]]
- 관련: [[ai-slop]] · [[slop-cannon]] · [[risk-proportional-human-review]] · [[agent-trust-curve]] · [[no-silent-write]] · [[verification-bottleneck]] · [[context-engineering]] · [[agent-skills]] · [[value-maxing]]
