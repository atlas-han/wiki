---
title: Agent Knowledge Sourcing
type: concept
category: pattern
tags: [agent, knowledge, routing, decision, skills, mcp, rag, memory]
aliases: [에이전트 지식 조달, 지식 라우팅]
related: [agent-skills, model-context-protocol, retrieval-augmented-generation, agent-memory, context-engineering, company-brain, no-silent-write]
first-seen: tech-bridge-agent-knowledge-four-ways
sources: [tech-bridge-agent-knowledge-four-ways, tech-bridge-knowledge-work-agent-infrastructure, tech-bridge-company-brain-security]
created: 2026-09-08
updated: 2026-09-10
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

## 직교하는 축 — 누구의 범위로 집계하는가 (2026-09-08)

[[tech-bridge-knowledge-work-agent-infrastructure]]가 이 페이지의 4갈래 라우팅과 **직교하는 축**을 하나 놓는다.

이 페이지는 *지식이 어디서 왔는가* 로 가른다 — 사람이 적어둔 것([[retrieval-augmented-generation|RAG]])인가 에이전트가 겪은 것([[agent-memory|메모리]])인가. Composio 편은 **겪은 것을 누구의 범위로 집계하는가**를 가른다:

1. **도구가 일반적으로 어떻게 작동하는가** — 모든 사람에게 적용
2. **회사가 일을 어떻게 하는가** — 조직 범위
3. **당신이 어떻게 하기를 선호하는가** — 개인 범위

> 그것은 **당신 회사가 어떻게 작동하는지의 그림**입니다. — [[karan-vaidya]]

그리고 이 소스는 그 집계가 충분히 쌓이면 **[[agent-skills|스킬]]로 증류된다**고 말한다 — *"어떤 접근이 되고 어떤 게 안 되는지, 과거에 무엇이 실패로 이어졌는지."* 즉 **메모리 → 스킬의 승격 경로**를 제안하는 셈인데, 이 위키의 [[agent-knowledge-sourcing]] 라우팅은 둘을 **다른 상자**로 놓았다.

> ⚠️ Contradiction: [[tech-bridge-agent-knowledge-four-ways|IBM 편]]은 스킬을 *사람이 적어둔 절차* 로, 메모리를 *에이전트가 겪은 것* 으로 갈랐다. Composio 편은 **겪은 것이 쌓여 스킬이 된다**고 말한다. 두 소스는 서로를 언급하지 않으며 **위키는 어느 쪽도 채택하지 않고 두 서술을 나란히 둔다.** 승격의 메커니즘(무엇이 로그를 스킬로 만드는가)은 Composio 편이 설명하지 않는다.

## 조직 유통의 관점 — 스킬은 안 쓰고 메모리는 갇힌다 (2026-09-10)

[[tech-bridge-company-brain-security]]가 이 페이지의 4갈래 중 [[agent-skills|스킬]]과 [[agent-memory|메모리]]를 **조직 안에서 어떻게 흐르는가**로 다시 본다. 보안 질문서 예제 — *다른 사람이 답한 지식이 내 에이전트에 어떻게 오는가* — 로 셋을 비교한다.

| 경로 | 이 페이지의 상자 | 왜 안 되는가 |
|---|---|---|
| 모두가 GitHub에 공유 스킬을 쓴다 | 스킬 | *"**아무도 GitHub에 다른 사람을 위한 스킬을 쓰지 않는다.**"* — 동기 부재 |
| 팀 에이전트가 메모리를 자동 저장 | 메모리 | *"**사일로가 하나 더**"* — 그 팀·채널에 갇힌다 |
| **전사 단일 위키** + 스코프 + 사람 승인 | (RAG에 가장 가깝다 — *사람이 승인한 것*) | 채택 → [[company-brain]] |

즉 IBM의 표가 *지식이 어디서 왔는가* 로, Composio 편이 *누구의 범위로 집계하는가* 로 갈랐다면, 이 소스는 **누가 그것을 남에게 쓸 동기가 있는가**로 가른다. 셋째 축이다. 그리고 결론이 흥미롭다 — 조직에서 실제로 흐르는 것은 스킬도 메모리도 아니고 **사람이 승인한 위키 항목**, 즉 이 표의 첫 줄(사람이 적어 놓은 것)이다. 다만 *적는* 주체가 에이전트이고 사람은 *승인* 만 한다([[no-silent-write]]). IBM의 RAG 정의(*사람이 글로 적어 놓은*)가 여기서 **에이전트가 적고 사람이 서명한 것**으로 넓어진다.

> ⚠️ 같은 날 [[tech-bridge-agent-to-agent-as-search|Greze 편]]은 공유 스킬을 *"누구나 더 좋게 만든다"* 고 긍정적으로 말한다 → [[agent-skills]]의 충돌 표시 참조.

## References

- [[tech-bridge-agent-knowledge-four-ways]]
- 관련: [[agent-skills]] · [[model-context-protocol]] · [[retrieval-augmented-generation]] · [[agent-memory]] · [[context-engineering]] · [[brain-hands-decoupling]]
- [[tech-bridge-company-brain-security]] — 조직 유통 관점: 스킬 동기 부재·메모리 사일로·위키 채택 (2026-09-10)
