---
title: "매니저 봇 · 코딩 에이전트 분업 — first mile과 last mile은 봇이, 가운데는 코딩 에이전트가 (Manager Bot / Coding Agent Split)"
type: concept
category: pattern
tags: [orchestration, grokbot, coding-agents, cloud-agents, first-mile, last-mile, intent-management, isolation, subscription-cost, delegation, rob-shocks]
aliases: [manager bot, 매니저 봇, first mile, last mile, 봇은 매니저, bot as manager not coder, orchestrator bot]
related: [inner-outer-meta-loops, cloud-agent-delegation, persistent-agent-teams, agent-manager-analogy, goal-level-delegation, agent-sandboxing, hard-vs-soft-enforcement, agent-change-evidence]
first-seen: tech-bridge-rob-shocks-grokbot-manager-coding-agents
sources: [tech-bridge-rob-shocks-grokbot-manager-coding-agents]
created: 2026-11-03
updated: 2026-11-03
---

# 매니저 봇 · 코딩 에이전트 분업

**상시 대화형 봇(오케스트레이터)은 코드를 쓰지 않는다. 봇은 무엇을 지을지 정리하는 일(first mile)과 끝난 일을 확인하고 추적하는 일(last mile)을 맡는다. 가운데의 코드 작성은 자기 컴퓨터 · 컨텍스트 · 구독을 가진 코딩 에이전트에게 넘긴다.** [[rob-shocks|Rob Shocks]](설명란 근거)가 [[tech-bridge-rob-shocks-grokbot-manager-coding-agents]]에서 [[grokbot|GrokBot]] + [[claude-code|Claude Code]] · [[cursor-cloud|Cursor Cloud]] 구성으로 설명했다.

> *"Your bot should be the manager here, not the coder."*(00:21~00:23)

## 세 구간

| 구간 | 누가 | 하는 일 (en-orig) |
|---|---|---|
| **first mile** | 매니저 봇 | *"working out what to build"*(00:29) — Slack · 이메일 · X · Linear에 연결해 의도(intent)를 모으고 관리한다(00:40~00:49) |
| **가운데** | 코딩 에이전트 | *"doing the work, writing the code"*(01:24~01:26) — Claude Code · Codex · Cursor |
| **last mile** | 매니저 봇 | *"checking the work. So, chasing up on it, telling you what's done, keeping an eye on the task list."*(01:02~01:06) · *"It can check the proof whenever it comes back"*(01:33~01:37) |

"first mile"은 발표자가 **Grok 팀의 용어**라고 소개한 말이다(⚠️ 원 문서는 확인하지 않았다). 오케스트레이터 자리는 GrokBot이 아니어도 된다. 직접 만든 에이전트나 Claude · Cursor projects도 된다고 한다(01:09~01:22).

## 왜 나누나 — 발표자가 드는 근거 셋

1. **비용** — ⚠️ GrokBot은 Grok · Cursor와 주간 사용량 풀을 공유한다(발표자 진술, 02:22~02:28). 그래서 코딩을 봇에게 다 시키면 한도가 빨리 닳는다. 이미 낸 Claude Code · OpenCode 구독으로 넘긴다(02:34~02:38). → [[model-mixing-economics]]
2. **격리** — *"every worker get its own computer, its own context, and its own kill switch."*(02:40~02:44) → [[agent-sandboxing]]
3. **매니저 역할의 여유** — 클라우드 에이전트는 자기 컴퓨터를 갖고 있다. 그래서 *"it frees up your main orchestrator bot to be more of a manager"*(01:51~01:55)가 된다. 매니저가 Slack · 문서에 연결돼 있으면 하위 에이전트의 질문에도 직접 답해 막힘을 풀 수 있다(09:05~09:13).

## 운영 규칙 — 봇에게 붙여 넣는 한 줄

> *"For anything more than a short question, don't write the code yourself. Hand it to a coding agent with an acceptance test, check the proof, open a pull request, and report back."*(12:16~12:24)

이어서 *"every time you have to correct an agent, move that fix up the stack, code first, then a lint rule, then a rules file"*(12:24~12:30)라고 하고 영상이 끊긴다 → [[hard-vs-soft-enforcement]]. 위임 단위에 인수 테스트(acceptance test)와 증거가 붙는다는 점에서 [[agent-change-evidence]] · [[goal-level-delegation]]과 같은 방향이다.

## 위키의 다른 틀과의 관계

- **[[lauren-tan|Lauren Tan]]의 바깥 · 안쪽 루프** — *"cursor projects are my inner loop and grabbot[=GrokBot] is my outer loop"*(10-09 [[tech-bridge-lauren-tan-pocock-podcast-full]]). 같은 분업을 **사용자 쪽 말**로 바꾼 것이다. 바깥 루프는 first mile에 해당한다. 이 페이지는 거기에 **last mile(확인 · 추적)도 매니저 몫**이라는 점과 **비용 · 격리 근거**를 더한다. → [[inner-outer-meta-loops]]
- **[[persistent-agent-teams]]** — chief of staff 코디네이터 아래 봇 팀을 두는 구조. 발표자도 메인 에이전트 *"Chief"* 하나와 대화한다. 다만 역할이 다르다. 여기서 실제 작업자는 GrokBot 팀이 아니라 **외부 코딩 에이전트**다.
- **[[cloud-agent-delegation]]** — 가운데 구간의 실행 형태.
- **[[agent-manager-analogy]]** — 비유(헤드셰프)를 **도구 배치**로 옮긴 판본.

## ⚠️ 유보

- 1인 발표자의 구성 서술이다. 비용 절감, 실패율, 처리량을 잰 수치가 없다.
- 격리 근거는 같은 영상의 다른 진술과 긴장이 있다. 발표자는 *"All of your Grokbots share one cloud computer"*(10:56~10:59)라고 경고한다. 그러니 격리되는 것은 **코딩 에이전트 쪽**이고 매니저 봇들끼리는 아니다.
- 사용량 풀과 요금제 진술은 확인하지 않았다.

## References

- [[tech-bridge-rob-shocks-grokbot-manager-coding-agents]] · [[rob-shocks]] · [[grokbot]] · [[claude-code]] · [[cursor-cloud]]
- [[tech-bridge-lauren-tan-pocock-podcast-full]] — 안쪽 · 바깥 루프의 원 발화
