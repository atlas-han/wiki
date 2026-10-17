---
title: "백 프레셔 (Back Pressure) — forward pressure + back pressure = loop"
type: concept
category: pattern
tags: [loops, feedback, verification, triggers, agents, software-factory, hill-climbing]
aliases: [back pressure, backpressure, forward pressure, 역압, 순방향 압력, 역방향 압력]
related: [loop-is-the-product, agent-verification-skill, agent-visual-qa, scheduled-agent-automations, feedforward-feedback-steering, human-plumbing, verifiable-goals, software-factory, linear-vs-closed-loop-harness]
first-seen: tech-bridge-horthy-state-of-software-factory
sources: [tech-bridge-horthy-state-of-software-factory]
created: 2026-10-16
updated: 2026-10-16
---

# 백 프레셔 (Back Pressure)

**에이전트가 일하는 도중 사람에게 가지 않고도 결과를 hill-climb할 수 있게 해 주는 피드백 신호(back pressure), 그리고 새 일을 시작시키는 trigger(forward pressure). 둘을 합친 것이 "loop".** [[dex-horthy|Dex Horthy]]가 [[tech-bridge-horthy-state-of-software-factory]]에서 Loops 열풍을 해체하며 쓴 틀이다.

> *"I think loops are basically a combination of forward pressure and back pressure. This idea of loops was a little mystical. I think if you disentangle it into like, how do you kick off new work? What triggers cause new work to happen? And then, how do you give the agent like feedback while it's working so it can hill climb an outcome without having to go to a human? That's like the core of loops, I think."* (12:30~12:50)

## 두 방향

| | 질문 | 발화된 예 |
|---|---|---|
| **forward pressure** | *"What triggers cause new work to happen?"* | *"whether it's schedules or automations or webhooks"*(12:52~12:55) · 사용자 지원 티켓 → 에이전트 PR(11:45~11:56) · 페이저 알림에 에이전트 PR을 붙인다(11:54~12:01) |
| **back pressure** | 작업 중 에이전트에게 어떤 피드백을 주나 | *"Give them a browser, let them run the app, let them use curl, let them record videos (…) Like give them back pressure."*(11:19~11:25) · UI: 세 버전을 feature flag로 사용자에게 → *"This is how you give (…) your models back pressure for UI."*(12:21~12:30) |

- ⭐ UI 사례에서 **back pressure의 원천은 사용자**다 — 모델은 *"can make beautiful UIs, but they can't really see them in the way that you and I see them"*(12:17~12:21).

## 위키에서의 자리

- [[loop-is-the-product]] — 루프를 제품 단위로 올리는 쪽. Horthy는 반대로 루프를 **두 질문으로 분해**해 "신비"를 걷어낸다. 같은 대상, 다른 방향.
- [[agent-verification-skill]] · [[agent-visual-qa]] — back pressure의 구체 도구(브라우저·curl·영상).
- [[scheduled-agent-automations]] — forward pressure의 한 종류(스케줄).
- [[human-plumbing]] — back pressure가 없으면 사람이 피드백 배관이 된다(*without having to go to a human* 의 반대).
- ⚠️ **용어 충돌 주의**: [[feedforward-feedback-steering]]의 *feedforward* 는 행동 **전**의 안내(AGENTS.md·스킬 등)이고, Horthy의 *forward pressure* 는 일을 **시작시키는 trigger**다. back pressure ≈ feedback 칸과는 겹친다.
- 이름 *back pressure* 는 분산 시스템의 흐름 제어 용어와 같지만 의미가 다르다(위키의 actix 페이지 참고 — 여기서는 "생산자 속도를 늦추는 신호"가 아니라 "품질을 끌어올리는 신호").

## ⚠️ 유보

- 단일 화자, 정의는 발표 중 한 단락. back pressure의 품질(거짓 통과)을 어떻게 다루는지는 말하지 않는다 — [[reward-hacking]] 쪽 문제는 열려 있다.

## References

- [[tech-bridge-horthy-state-of-software-factory]]
