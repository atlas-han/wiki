---
title: "백 프레셔 (Back Pressure) — forward pressure + back pressure = loop"
type: concept
category: pattern
tags: [loops, feedback, verification, triggers, agents, software-factory, hill-climbing]
aliases: [back pressure, backpressure, forward pressure, 역압, 순방향 압력, 역방향 압력]
related: [loop-is-the-product, agent-verification-skill, agent-visual-qa, scheduled-agent-automations, feedforward-feedback-steering, human-plumbing, verifiable-goals, software-factory, linear-vs-closed-loop-harness, hard-vs-soft-enforcement]
first-seen: tech-bridge-horthy-state-of-software-factory
sources: [tech-bridge-horthy-state-of-software-factory, tech-bridge-dex-horthy-twelve-rules-no-slop-factory, tech-bridge-steve-yegge-software-factories-trash-mountain]
created: 2026-10-16
updated: 2026-11-27
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

## 2026-11-26 — 규칙 1번이 됐다: 앞 압력 · 뒤 압력 ([[tech-bridge-dex-horthy-twelve-rules-no-slop-factory]])

10-15 소스에서 여덟 번째 항목이던 루프가 Code Summit 발표에서는 **첫 번째 규칙** 이다(한국어 해설 — 내레이션은 *앞 압력* · *뒤 압력* 이라고 옮긴다).

- 앞 압력: *"일을 시작시키는 힘입니다."*(01:54~01:56) Horthy 원음(en-orig 단일 트랙)의 예 — 사고가 나면 호출과 함께 PR이 온다: *"when I get page 3 in the morning, I'm looking at a pull request that we think is going to solve it."*(02:08~02:11) (ASR *page 3* 는 새벽 3시의 호출로 읽힌다.)
- 뒤 압력이 필요한 이유: *"이제 만드는 건 몇 분, 몇 시간이면 끝나는데 리뷰와 테스트는 여전히 며칠씩 걸립니다."*(02:22~02:27) 그래서 투자하는 곳 — 에이전트 코드 리뷰 · 에이전트 테스트 · CI(ASR *CRI*, 추정) · 린터: *"사람이 끼지 않아도 에이전트가 스스로 더 나은 결과를 내게 하는 장치들입니다."*(02:33~02:37)
- 맞물림: *"요즘 유행하는 루프라는 말을 그는 앞 압력과 뒤 압력이 맞물리는 것으로 봅니다."*(02:38~02:44)
- ⭐ 기준이 하나 붙었다: *"일은 자동으로 시작되고 사람 손에 닿을 때쯤엔 쉬운 문제는 이미 다 고쳐져 있어야 한다는 겁니다."*(02:44~02:49) — 뒤 압력의 몫은 *쉬운 문제* 까지이고 그다음은 사람이다.

이 페이지 *유보* 에 적은 열린 문제(뒤 압력의 거짓 통과)에 대해서는 원음 조각 하나가 방향만 준다 — 에이전트 리뷰어 · 린터 · 검증기는 *"they are not sufficient."*(11:12) ⚠️ 이유를 말하는 자리는 무캡션이다.

## 2026-11-27 — 이름이 닮은 다른 힘: 정리에만 쓰는 예산 ([[tech-bridge-steve-yegge-software-factories-trash-mountain]])

[[steve-yegge|Steve Yegge]]의 공장 발표(한국어 해설 전달)에 *반대로 미는 힘* 이라는 말이 나온다. 더빙은 *counter-pressure* 로 옮긴다 — ⚠️ 원음은 무캡션이라 그가 *back pressure* 라는 낱말을 썼는지는 알 수 없다.

- *"그래서 그는 반대로 미는 힘을 공장에 넣으라고 합니다."*(06:40~06:42) *"토큰 예산의 일정 비율은 정리에만 쓰고 뭔가 더하기 전에 먼저 지우거나 줄이게 합니다."*(06:44~06:48)
- 겨누는 것은 에이전트들이 쌓는 기록이다: *"사장이 마음을 바꿀 때마다 기록은 계속 쌓입니다."*(05:55~05:57)
- 일의 흐름 쪽에도 같은 모양이 있다 — 아침마다 *"너무 빨리 달린 쪽은 사람의 승인을 기다리게 늦춥니다."*(05:07~05:09)

이 페이지의 back pressure는 에이전트가 결과를 스스로 고쳐 나가게 하는 **피드백 신호** 다. Yegge의 것은 쌓이는 **양** 을 줄이는 예산이고 신호가 아니다. 같은 개념으로 합치지 않고 이웃으로 적어 둔다 → [[trash-mountain]]
