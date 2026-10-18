---
title: 에이전트 주의 관리 (Agent Attention Management)
type: concept
category: pattern
tags: [human-attention, multi-agent, orchestration-ui, supervision, burnout, visibility, game-design, accessibility]
aliases: [주의 관리, 사람 주의가 병목, we are the bottleneck, raise the ceiling lower the floor, 천장 높이기 바닥 낮추기, 게임식 에이전트 감독]
related: [verification-bottleneck, agent-manager-analogy, orchestras-not-factories, steering-altitude, agent-visual-qa, multiplayer-agent-context, software-factory, loop-is-the-product, capability-discovery-burden, minimizing-reader-load, persistent-agent-teams, goal-level-delegation]
first-seen: tech-bridge-agentcraft-strategy-game
sources: [tech-bridge-agentcraft-strategy-game, tech-bridge-lee-robinson-always-on-agents]
created: 2026-10-09
updated: 2026-10-18
---

# 에이전트 주의 관리 (Agent Attention Management)

**여러 에이전트를 돌릴 때 희소한 것은 모델 능력이 아니라 사람의 주의(attention)와 기력이며, 그 병목은 리뷰만이 아니라 조종·지시·리뷰 전체에 걸쳐 있다는 관점 — 그리고 답을 "무엇을, 언제, 어느 해상도로 사람에게 보여 줄 것인가"라는 인터페이스 설계에서 찾는 패턴.** [[ido-salomon|Ido Salomon]]이 [[tech-bridge-agentcraft-strategy-game]]에서 [[agentcraft|AgentCraft]]로 제시했다.

> *"each one of these agents require you to steer them, direct them, review them, and when it's at scale, especially, it's just exhausting. We need to find the skills to allow us to do it without burning out. So, in reality, we are the bottleneck."* (00:47~01:02)

## 진단 — 리뷰 병목보다 넓다

[[verification-bottleneck]]은 생성 이후의 **검증·리뷰**가 막힌다고 본다. 이 개념은 같은 *"we are the bottleneck"* 을 **에이전트 수명주기 전체의 주의 비용**으로 본다:

| 단계 | 사람의 부담 (화자 진술) | en-orig |
|---|---|---|
| 상황 파악 | 누가 내 주의가 필요한가 | 03:39~03:44 |
| 계획 | *"too much to hold in our heads"* — 다음 할 일조차 떠올리기 어렵다 | 05:22~05:37 |
| 실행 감독 | *"I have to babysit each and every one"* | 05:58~06:04 |
| 리뷰 | *"even five things to review at the same time"* | 07:00~07:09 |
| 고립 | *"It's pretty lonely to just talk to agents all day"*, 내가 적임 리뷰어가 아닐 수도 | 07:56~08:12 |

## 처방의 사다리 — 천장 높이기 (raise the ceiling)

각 단계가 앞 단계의 부담을 다음 장치로 옮긴다. 화자는 단계마다 *"it's not really enough"*, *"it's still pretty exhausting"* 으로 다음으로 넘어간다.

1. **가시성** — 상태 패널, 작업 위치의 지도·히트맵. 그러나 *"It's pretty exhausting to keep looking at what the agents are doing in the granularity of what files"*(05:05~05:14) — **가시성 자체가 새 감독 부담**이 된다.
2. **주의 라우팅** — ⭐ RTS·Civilization의 스페이스바처럼 *"the nearest thing that actually needed your attention"*(04:45~04:49)으로 점프. 보는 일을 *다 보기* 에서 *필요한 곳만 가기* 로 바꾼다.
3. **계획 외주(퀘스트)** — 에이전트가 할 일을 만들고 사람은 수락만(05:39~05:52). → [[proactive-idea-feed]]
4. **실행 외주(자율성)** — 오케스트레이터·격리 컨테이너·루프(06:20~06:54). → [[software-factory]] · [[loop-is-the-product]] · [[goal-level-delegation]]
5. **리뷰 압축** — 영상·사진 *"visual evidence"*, 병렬 구현 중 고르기(07:22~07:36). → [[agent-visual-qa]] · [[minimizing-reader-load]]
6. **주의 분산(협업)** — 사람을 더 들여 리뷰를 맞는 사람에게(08:08~09:43). → [[multiplayer-agent-context]]

## 바닥 낮추기 (lower the floor)

*"we need to raise the ceiling, but we also need to uh lower the floor"*(10:54~10:59). 같은 주의 문제를 **파워 유저가 아닌 사람**에게서 풀면 답이 반대가 된다 — 정보를 더 보여 주는 대신 **숨긴다**: *"more of a mobile game level"*, *"I prompt, I get a result, I don't really care perhaps about the way, I can see it if I want to"*(11:44~12:09). → [[steering-altitude]](같은 제품 계열 안에서 고도를 둘로 나눔) · [[capability-discovery-burden]]

## 왜 게임인가

화자의 논거는 **전이(transfer)** 다 — 필요한 기술이 *"have been with us all along"*(01:15~01:18): Warcraft·Sims의 유닛 감독(01:29~01:42), RTS의 스페이스바 점프(04:40~04:49). 게임 UI는 *많은 유닛 · 실시간 · 제한된 주의* 라는 같은 제약을 수십 년 다듬어 왔다는 것. 사용자 반응 일화(아이들, StarCraft 중퇴자 10:27~10:52)를 근거로 든다. ⚠️ 일화이고 측정은 없다.

## 이 위키에서의 위치

- **[[verification-bottleneck]]** — 그 페이지의 네 답(작업을 고른다 · 역량을 짓는다 · 일을 쪼갠다 · 리뷰를 시스템으로)은 모두 *리뷰 처리량* 을 다룬다. 이 개념은 **리뷰 앞뒤의 주의 비용**과 **인터페이스**라는 다른 축을 연다.
- **[[agent-manager-analogy]]** — 매니저 비유가 *위임과 신뢰* 를, 이 개념의 게임 비유가 *주의 배분* 을 말한다.
- **[[orchestras-not-factories]]** — 같은 *여러 에이전트 한 화면* 앱 제작자의 다른 은유(지휘자 vs RTS 지휘관).
- **[[persistent-agent-teams]]** — 에이전트에게 정체성을 주고 문자하듯 소통하는 쪽은 *대화* 로 주의를 관리하고, 이 개념은 *공간·시각화* 로 관리한다.

## 언제 말을 걸까 — router 뒤의 heuristic (2026-10-18 · [[tech-bridge-lee-robinson-always-on-agents]])

[[lee-robinson|Lee Robinson]]([[grokbot|GrokBot]])은 사람의 주의를 **에이전트 쪽에서** 아낀다.
- router 뒤에 *"this heristic[=heuristic] of do I need to bug the user about this or not? Because not everything is actually important."*(12:00~12:06) 동료 기준으로는 *"You really only need a status update maybe, I don't know, every day depending on the task."*(12:13~12:18)
- 도구 사다리 맨 끝에 사용자를 둔다: *"only if all of those fail, then go bug the user and ask them to go give input or approve something"*(22:21~22:27).
- ⚠️ 화자 스스로 미완성이라고 한다: *"the heristics around when the agent is silent or when it kind of bugs you, uh I don't think that we have it perfect yet."*(41:12~41:20) 예: 어제 빠진 수업을 녹음해 노트를 정리했다는 제안은 *"maybe that's helpful or maybe that's kind of annoying"*(41:22~41:34)이다. ko는 이 부정을 **"완벽한 것들을 가지고 있고"**(41:19)로 뒤집는다.

이 페이지가 "무엇을, 언제, 어느 해상도로 사람에게 보여 줄 것인가"를 인터페이스 설계로 보았다면, 이 소스는 그 판단의 일부를 **에이전트의 heuristic**에 맡긴다.

## ⚠️ 미해결

- **가시성의 역설** — 더 보여 줄수록 더 지친다(05:05~05:14)는 진단과 *보기를 선택 사항으로* 내리는 단순판(12:05~12:09) 사이에서, **무엇은 반드시 봐야 하는가**의 기준이 없다. [[mergeability-gap]]·[[verification-bottleneck]]의 *"Please please read the code"*(Voss가 인용한 Dex Horthy) 쪽과 긴장한다.
- **주의 점프의 우선순위** — *"needed your attention"* 을 누가·어떻게 판정하는지(에이전트 자기보고? 규칙?) 발화되지 않는다.
- **검증 공백** — 결과를 판정할 수 없는 신규 사용자에게 *"I don't really care about the way"* 를 권할 때 품질은 누가 지키는가.
- 근거는 단일 당사자 데모. 측정 없음.

## References

- [[tech-bridge-agentcraft-strategy-game]] (first-seen) · [[ido-salomon]] · [[agentcraft]]
- 관련: [[verification-bottleneck]] · [[agent-manager-analogy]] · [[orchestras-not-factories]] · [[steering-altitude]] · [[agent-visual-qa]] · [[multiplayer-agent-context]] · [[capability-discovery-burden]]
