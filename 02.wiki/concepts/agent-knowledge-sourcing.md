---
title: Agent Knowledge Sourcing
type: concept
category: pattern
tags: [agent, knowledge, routing, decision, skills, mcp, rag, memory]
aliases: [에이전트 지식 조달, 지식 라우팅]
related: [agent-skills, model-context-protocol, retrieval-augmented-generation, agent-memory, context-engineering]
first-seen: tech-bridge-agent-knowledge-four-ways
sources: [tech-bridge-agent-knowledge-four-ways]
created: 2026-09-08
updated: 2026-09-08
---

# Agent Knowledge Sourcing

에이전트에게 **학습 데이터 밖의 지식**을 줄 때 어떤 메커니즘을 쓸지 고르는 문제. [[tech-bridge-agent-knowledge-four-ways]]가 네 갈래 라우팅 규칙으로 정리했다.

## 라우팅 규칙

| 조건 | 답 |
|---|---|
| **누군가가 글로 적어 놓은** 지식 | [[retrieval-augmented-generation\|RAG]] |
| 에이전트가 **경험을 통해 습득한** 지식 | [[agent-memory\|메모리]] |
| **따라야 할 절차**·**반복 가능한** 일 | [[agent-skills\|에이전트 스킬]] |
| 바깥에서 **실제로 조회**해야 하는 것 (*"proprietary code를 쓰지 않고"*) | [[model-context-protocol\|MCP]] |

⚠️ 마지막 줄의 *"without using proprietary code"* 한정은 **소스가 부연하지 않는다.**

## 왜 이 표가 필요한가 — 쏟아붓기의 세 가지 실패

출발점은 *"컨텍스트 창에 다 넣으면 되지 않나"* 에 대한 반박이다.

> AI 에이전트가 **길을 잃거나**, **막다른 길로 들어서거나**, **특정 결제 페이지의 실제 작동 방식을 제대로 반영하지 못하는 일반적인 방식으로 동작할** 가능성이 크기 때문입니다.

**세 번째가 이 개념의 근거다.** 앞의 둘(길 잃음·막다른 길)은 이 위키가 [[harness-pruning]]·[[self-harness]]에서 **하니스 문제**로 다뤄왔다. 세 번째 — *일반론으로의 후퇴* — 는 컨텍스트가 모자라서가 아니라 **이 시스템에만 해당하는 지식의 종류가 잘못 조달되어** 생긴다. 그래서 조달 경로를 나누는 것이 답이 된다.

## 네 방법은 릴레이로 이어진다

소스의 논증 구조 자체가 이 개념의 내용이다. 각 방법을 설명한 직후 **그것이 멈추는 자리**를 짚고 다음으로 넘긴다.

1. **[[agent-skills|스킬]]** — 절차와 판단을 준다. → *"하지만 이야기는 거기서 끝납니다. (…) 에이전트가 실제로 대시보드에 접속하여 오류율을 확인할 수 있는 것은 아닙니다."*
2. **[[model-context-protocol|MCP]]** — 실제로 도달해 로그·지표를 읽는다. → *"이 특정 웹페이지 설정이 어떻게 작동하는지 (…) 실질적인 지식이 없다"*
3. **[[retrieval-augmented-generation|RAG]]** — 사람이 적어둔 문서를 가져온다. → 문서에 없는 것이 남는다.
4. **[[agent-memory|메모리]]** — 에이전트가 겪은 것. → (소스가 여기서 닫는다)

**①→②의 이음매**가 이 위키에서 특히 유용하다. [[agent-skills]]는 조직 지식·거버넌스 축으로, [[model-context-protocol]]은 연결 표준 축으로 따로 자라 왔고 서로를 `related`로만 걸고 있었다. 이 규칙이 둘의 분업을 한 문장으로 준다 — **스킬은 무엇을 할지 알고, MCP는 그것을 할 수 있게 한다.** [[brain-hands-decoupling]]의 뇌/손 분리를 지식 층에서 다시 그린 형태다.

## 이 위키의 다른 결정 기준들과의 위치

| 기준 | 무엇을 묻는가 | 출처 |
|---|---|---|
| [[verifiable-goals]] · [[generator-evaluator-pattern]] | 결과물이 됐는가 | 여러 소스 |
| 실명 10명 / 유료 3명 | **착수해도 되는가** | [[tech-bridge-six-agent-skills]] |
| **이 페이지** | **어느 메커니즘으로 지식을 줄 것인가** | [[tech-bridge-agent-knowledge-four-ways]] |

**설계 시점의 선택을 묻는 표는 이것이 처음**이다.

## 한계

- **비용·지연 비교가 없다.** 쏟아붓기가 *"비효율적"* 이라는 판단에 측정이 붙어 있지 않다.
- **조합을 다루지 않는다.** 소스는 *"또는 이 모든 것"* 이라고 열어두고 넘어간다. 실제로는 네 가지가 동시에 붙고, 그때 **RAG의 문서와 [[agent-memory|메모리]]의 경험이 어긋나는 경우**가 생긴다 — 소스의 예제 자체가 그런 사례인데(런북에 없던 진짜 원인) 판정 규칙이 없다.
- **네 갈래가 배타적이지 않다.** 반복 절차이면서 외부 조회가 필요한 일은 스킬과 MCP 둘 다다. 표는 그것을 인정하지만 우선순위는 주지 않는다.

## References

- [[tech-bridge-agent-knowledge-four-ways]]
- 관련: [[agent-skills]] · [[model-context-protocol]] · [[retrieval-augmented-generation]] · [[agent-memory]] · [[context-engineering]] · [[brain-hands-decoupling]]
