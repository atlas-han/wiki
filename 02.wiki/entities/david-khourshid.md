---
title: David Khourshid
type: entity
category: person
tags: [xstate, stately, state-machine, determinism, agent-workflows, agent-conf]
aliases: [David Khourshid, DavidKPiano, 데이비드 쿠르시드]
links:
  - https://stately.ai
sources: [tech-bridge-goodbye-slop-state-machines]
created: 2026-10-09
updated: 2026-10-09
---

# David Khourshid

상태 머신 라이브러리 [[xstate|XState]]의 제작자이자 Stately(stately.ai) 창업자. 핸들 @DavidKPiano(*"piano's not my last name. I'm a pianist"*). [[tech-bridge-goodbye-slop-state-machines]](Agent Conf 2026, 폴란드)에서 **명시적 상태 머신을 에이전트 자기 개선의 도구로** 제안했다. 본 위키 첫 등장.

> en-orig 자기소개 *"I'm @DavidKPiano pretty much everywhere. Uh that's my handle. My name is David Khourshid. I created a state machine library called XState."*(00:20~00:31), *"I am also the founder of a company called stately.ai. I'm not trying to sell you anything. You could do this with uh pretty much anything. XState's an open-source library."*(00:40~00:51). 설명란 *"Stately 창립자이자 XState 제작자"* 와 일치.

## 발표에서 (자막 근거)

- 슬롭의 출처 = *"unstructured delegation"*(03:31~03:32) → [[ai-slop]]
- 결정론은 규칙에, 비결정론은 내용에. 메가 프롬프트는 제어 흐름을 텍스트에 묻고 *"the rules decay with context"*(07:23~07:26) → [[agent-state-machine]] · [[context-rot]]
- *"modeling is not ceremony when it actually replaces confusion"*(10:16~10:21), *"you cannot draw arrows in paragraphs"*(11:39~11:42)
- eval의 세 번째 대상 — *"evaling the edges"*(12:29~12:31)
- 상태 머신을 트레이스·eval과 함께 다른 에이전트에게 넘겨 V2를 받는다 — *"The state machine is how you could have the agent self-improve."*(17:18~17:23) → [[skill-self-improvement]]
- [[jev|Jev]]로 만든 에스프레소 머신 데모 — Jev가 상태 머신과 허용 이벤트를 받아 다음 이벤트를 확률과 함께 고른다(18:54~19:57)

## 태도

**도구 중립을 말하는 도구 제작자.** *"you don't need a special library"*(15:02~15:04), switch 문·reducer·[[langchain|LangGraph]]도 된다고 한다. 모든 에이전트를 모델링하라는 것도 아니다 — *"where it applies, it's really, really useful"*(10:43~10:46). 2023년 같은 행사에선 *"constraining agent behaviors to state machines"*(03:15~03:17)를, 2026년엔 자기 개선을 말했다(17:26~17:44).

> ⚠️ 이해관계: XState·Stately는 상태 머신 도구·서비스다. 화자는 판매하지 않겠다고 선을 그었다(00:43~00:47). V1→V2·Stately 내부 적용(*"software factories at Stately"* 13:15~13:17)의 결과는 공개되지 않았다.

## References

- [[tech-bridge-goodbye-slop-state-machines]] · [[xstate]]
- 관련: [[agent-state-machine]] · [[jev]] · [[ai-slop]]
