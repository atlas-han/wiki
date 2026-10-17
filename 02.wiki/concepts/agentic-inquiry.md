---
title: Agentic Inquiry (에이전트로 묻고 이해하기)
type: concept
category: pattern
tags: [comprehension, cognitive-debt, code-understanding, dogfooding, agent-workflow, vibe-coding]
aliases: [agentic inquiry, 에이전트 질의]
related: [cognitive-debt, code-knowledge-graph, read-fluency-for-agent-output, slop-free-zone, verification-bottleneck, agent-native-interface]
first-seen: tech-bridge-vercel-rauch-agentic-workflow
sources: [tech-bridge-vercel-rauch-agentic-workflow]
created: 2026-10-16
updated: 2026-10-16
---

# Agentic Inquiry

**에이전트가 만든 것을 줄 단위로 읽는 대신, 에이전트를 시켜 그것이 무엇을 했는지 묻고 이해를 돌려받는 습관.** [[guillermo-rauch|Guillermo Rauch]]([[vercel|Vercel]] CEO)가 자기 조어라고 소개했다 — *"the phrase that I've coined, I think I've coined this is agentic inquiry"*(07:01~07:07, [[tech-bridge-vercel-rauch-agentic-workflow]]).

> *"I'm not advocating that you read every line of code, but when you do get something done, try to understand what just happened."* (07:05~07:12)

## 두 용법 — 같은 화자, 다른 대상

| | ① 제품을 에이전트에게 시험시키기 (03:16~03:47) | ② 에이전트가 한 일을 이해하기 (07:01~09:35) |
|---|---|---|
| 대상 | 자사 신기술(예: *"drives"*) | 방금 생성·변경된 코드 |
| 질문 | *"try to find race conditions, try to measure latency, try to compare it with alternatives"* → *"Tell me what Vercel could have done better."* | 지연·할당·*"the new API shape"*(08:41~08:51) |
| 결과 | 제품 비평(dogfooding을 에이전트가) | 사람이 소화할 수 있는 이해 |

⚠️ 화자가 두 용법을 구분하지 않는다. 사이에 영상의 해설 공백(06:49~07:01)이 있어 원본에서 얼마나 떨어진 발화인지 모른다.

## 양극단 사이

진행자(⚠️ David Ondrej 추정): *"people see such a binary, like either you're reading the code and it's like line by line (…) Or you're just like fully yellowing[=YOLO-ing] and never looking at it"* — *"if you if you know how to use the agent to understand this file or this module, like that's enough."*(07:14~07:32)

## 실천 예

- **호출 스택 다이어그램 스킬**(X의 *"Dylan Monroe"*, ⚠️ 철자 미확인): 에이전트가 *"pseudo static analysis"* 를 해 *"the symbolic space of your program"* 을 보여준다. 고정 도구라면 매번 새 프로그램을 짜거나 *"very rigid tool"* 이 된다(07:41~08:39) → [[code-knowledge-graph]] · [[understand-anything]]
- **변경 알림 자동화**: 공개 API 형태가 바뀌면 Slack MCP로 알림 — *"better quote unquote agentic engineering than just do it, make no mistakes. Please auto merge and let's keep building a huge pile of slop."*(09:01~09:35) → [[model-context-protocol]] · [[ai-slop]]

## 이 위키에서의 위치

- [[cognitive-debt]]의 처방 하나 — 읽기량을 늘리지 않고 **에이전트에게 설명을 시켜** 부채를 갚는다.
- [[read-fluency-for-agent-output]](읽을 수 있을 만큼 배우기)과 짝: 그쪽은 사람의 읽기 능력, 이쪽은 읽기를 에이전트에게 위임.
- [[slop-free-zone]] — Rauch는 같은 인터뷰에서 *"areas of your code base (…) extremely diligent"*(10:56~11:05)를 말한다. 즉 **기본은 inquiry, 중요한 구역은 diligence**의 2단.
- ⚠️ 측정 없음. 에이전트의 설명이 틀릴 때의 검증 방법은 다루지 않는다 → [[verification-bottleneck]].

## References

- [[tech-bridge-vercel-rauch-agentic-workflow]] · [[guillermo-rauch]] · [[fx]]
- 관련: [[cognitive-debt]] · [[code-knowledge-graph]] · [[read-fluency-for-agent-output]] · [[slop-free-zone]] · [[verification-bottleneck]]
