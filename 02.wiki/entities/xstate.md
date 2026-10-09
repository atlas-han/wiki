---
title: "XState (Stately)"
type: entity
category: tool
tags: [xstate, stately, state-machine, statecharts, javascript, open-source, agent-workflows]
aliases: [XState, Stately, stately.ai]
links: ["https://stately.ai"]
sources: [tech-bridge-goodbye-slop-state-machines]
created: 2026-10-09
updated: 2026-10-09
---

# XState (Stately)

[[david-khourshid|David Khourshid]]가 만든 **오픈소스 상태 머신 라이브러리**(*"XState's an open-source library"* 00:49~00:51). 그가 창업한 Stately(stately.ai)가 그 주변 회사다. 이 위키에는 [[tech-bridge-goodbye-slop-state-machines]]로 첫 등장 — 에이전트 워크플로를 명시적 상태 머신으로 모델링하는 도구 중 하나로.

> ⚠️ **소스에서 확인되는 것은 이름·오픈소스라는 것·제작자뿐이다.** API·언어·statecharts 지원 등 기능 서술은 자막에 없다(JS/TS 라이브러리라는 것은 위키 외부 상식 — 이 위키는 확인하지 않았다).

## 소스에서 (자막 근거)

- 화자 스스로 **필수가 아니라고** 한다: *"it could be XState, you could write a switch statement, a reducer function. Um coding agents are really good at updating these things regardless of whatever you use."*(15:36~15:45) — 같은 자리에 [[langchain|LangGraph]]를 *"one of the uh most popular tools for using state machines with agents"*(15:48~15:54)로 든다.
- 이메일 드래프터 데모의 화면은 *"automatically visualized from a state machine"*(08:48~08:52) — 시각화 도구가 무엇인지는 미발화.
- Stately 내부: *"software factories at Stately"*, *"state machine generation and editing pipeline"*(13:15~13:23)에 상태 머신 + 트레이스 + eval → 에이전트 개선 루프를 적용했다고 한다. ⚠️ 결과 미공개.

## References

- [[tech-bridge-goodbye-slop-state-machines]] · [[david-khourshid]]
- 관련: [[agent-state-machine]] · [[design-pattern-state]]
