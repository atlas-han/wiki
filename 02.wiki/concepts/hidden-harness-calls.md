---
title: "숨은 하네스 호출 (Hidden Harness Calls) — 사용자가 부르지 않은 모델 호출이 사용량을 먹는다"
type: concept
category: pattern
tags: [harness-design, token-cost, usage-limits, observability, opentelemetry, background-agents, agent-summary, prompt-caching, claude-code, cost-attribution]
aliases: [hidden harness calls, 숨은 하네스 호출, 하네스 자체 호출, agent summary cost, 에이전트 요약 비용, background agent summary, query source, 보이지 않는 토큰]
related: [prompt-caching, fork-subagent, harness-engineering, agent-harness-design, token-minimization-trap, true-cost-to-perfect-answer, subagent-vs-thread-handoff, review-loop-termination]
first-seen: tech-bridge-better-stack-claude-code-agent-summary-cost
sources: [tech-bridge-better-stack-claude-code-agent-summary-cost]
created: 2026-11-03
updated: 2026-11-03
---

# 숨은 하네스 호출 (Hidden Harness Calls)

**코딩 에이전트의 하네스는 사용자의 요청에 답하는 호출 말고도 상태 요약 · 분류 같은 보조 목적으로 모델을 부른다. 이런 호출은 화면의 작은 UI 한 줄로만 드러나고, 트랜스크립트에 남지 않으면 사용량 집계 도구에도 잡히지 않는다. 그래도 같은 사용량 한도를 쓴다.** 이 위키의 첫 사례는 [[claude-code|Claude Code]]의 백그라운드 에이전트 **agent summary**이고, [[better-stack|Better Stack]](설명란 근거)이 OpenTelemetry로 쟀다 → [[tech-bridge-better-stack-claude-code-agent-summary-cost]].

> *"none of these summaries actually get logged in Claude codes JSONL transcripts. So, anything that works out your usage from those files, like CC usage, never actually sees these costs."*(01:47~01:56)

## 사례 — Claude Code agent summary (⚠️ 화자 측정, 각 1회)

| 성질 | 화자 관찰 |
|---|---|
| **무엇을 위한 호출인가** | 에이전트 패널의 상태 줄 — *"the status line of the agents in the agent panel and not the main clawed one."*(00:28~00:32) |
| **언제 부르나 (wall-clock)** | *"Any agent that's working and whose transcript gets changed gets summarized every 30 seconds."*(02:17~02:21) — 일의 양이 아니라 **시간**에 비례한다 |
| **무엇을 보내나** | 대화 전체 — 18 → 42 메시지로 커진다(00:58~01:04), 호출당 약 40,000 입력 토큰 → 약 130 출력 토큰(01:04~01:09) |
| **어떤 모델로** | *"every one of those summary calls run on Opus as well and not a cheaper model like Haiku."*(01:28~01:34) |
| **얼마나** | 최악에 가까운 테스트(`sleep 20` × 8) 세션 비용의 12%, Opus 사이트 빌드 약 8%. 제3자: Flamerix 15~20%, Claude Code 팀원(HN) 지난주 약 2% · 터미널 약 6% |
| **끌 수 있나** | *"There is no setting for this."*(03:18~03:20) — fork 서브에이전트를 끄는 간접 우회뿐 → [[fork-subagent]] |

## 왜 숨는가 — 세 겹

1. **UI가 작다.** 결과는 상태 줄 한 줄이라 그 뒤에 4만 토큰짜리 호출이 있다는 것이 보이지 않는다. 화자에 따르면 메인 상태 줄과 혼동하는 사람도 있었다(00:27~00:32).
2. **기록에 없다.** JSONL 트랜스크립트 기반 집계(ccusage 등)는 이 호출을 못 본다(01:47~01:56).
3. **할인이 불투명하다.** 대부분은 캐시 읽기라 API에서는 약 1/10 가격이지만(02:39~02:41), 구독에서는 *"Anthropic only says they still draw usage and not how much."*(02:42~02:44) → [[prompt-caching]]

## 재는 방법 — 용도 태그로 묶기

하네스가 요청마다 용도를 붙여 내보내면 사용자는 비용을 기능별로 나눌 수 있다. 화자의 방법: *"I turned on Claude Code's open telemetry export and sent it to Better Stack where every request comes through tagged with a query source saying what it was for."*(00:36~00:43) → *"Once you group these by query source, you see the agent summary was 12% of the whole session's cost."*(01:11~01:18) Flamerix의 15~20%도 *"a whole team's open telemetry data"*(01:42~01:43)에서 나왔다. **트랜스크립트가 아니라 요청 단위 텔레메트리**가 이 비용을 보는 길이다.

## 편차 — 같은 기능이 2%에서 20%까지

- 분모가 다르다: Anthropic은 전체 텔레메트리 평균, 화자는 한 세션, Flamerix는 백그라운드 에이전트를 많이 쓰는 한 팀.
- 주기가 시간 기준이라 **오래 도는 에이전트가 많을수록** 커진다(02:21~02:24). 20초마다 조금씩 움직이는 에이전트는 *"close to worst case scenario"*(02:30).

## 이 위키에서의 자리

- [[token-minimization-trap]] · [[true-cost-to-perfect-answer]]는 사용자가 *보내는* 토큰의 경제학이었다. 이 개념은 **사용자가 보내지 않은 토큰** — 하네스 설계자의 선택(주기 · 컨텍스트 크기 · 모델)이 사용자 한도로 넘어오는 경우다.
- [[prompt-caching]]이 "접두를 지키면 싸다"를 말한다면, 여기서는 **캐시가 맞아도 구독 한도에서는 얼마나 싼지 모른다**는 반대쪽이 나온다.
- [[review-loop-termination]]의 *"every one of those rounds uses up your limits"* 는 사용자가 설계한 루프의 비용이고, 이 개념은 사용자가 설계하지 않은 루프(30초 타이머)의 비용이다.

## ⚠️ 유보

- 사례는 하나(agent summary), 측정은 화자 1인 · 테스트 각 1회. "cost" · "usage"의 단위와 캐시 할인 반영 여부는 발화되지 않았다.
- Anthropic 쪽 진술 — HN 답글 2%/6%, Claude가 요약을 스스로 쓴다(04:23~04:28), 더 싼 판본을 만드는 중(04:34~04:36) — 은 화자 전달이고 원문을 찾지 않았다.
- 다른 하네스(Codex 등)의 보조 호출은 이 위키에 아직 측정 소스가 없다. 화자는 T3 Code가 *"handles summaries its own way"*(04:44~04:47)라고만 한다.

## References

- [[tech-bridge-better-stack-claude-code-agent-summary-cost]] — first-seen
- [[prompt-caching]] · [[fork-subagent]] · [[claude-code]] · [[better-stack]]
