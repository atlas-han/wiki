---
title: Push vs Pull Context Retrieval
type: concept
category: pattern
tags: [context-engineering, mcp, retrieval, latency, accuracy]
related: [model-context-protocol, hook-enforced-workflow, file-discovery-tax, context-engineering, build-time-vs-runtime-tools]
first-seen: tech-bridge-graft-code-knowledge-graph
sources: [tech-bridge-graft-code-knowledge-graph]
created: 2026-09-15
updated: 2026-09-15
---

# Push vs Pull Context Retrieval

**같은 지식을 에이전트에게 주는 방법은 둘이고, 차이는 "누가 조회를 시작하는가"다.**

[[tech-bridge-graft-code-knowledge-graph]]가 이 축을 드물게 **하나의 도구가 두 방식을 모두 배포하고 스스로 비교하는 형태**로 보여 준다.

| | **Push** (훅/CLI) | **Pull** ([[model-context-protocol|MCP]]) |
|---|---|---|
| 조회를 시작하는 쪽 | **도구** — 프롬프트를 보고 추측 | **에이전트** — 필요할 때만 질의 |
| 프롬프트 첨부 | **매 메시지에** 최대 3개 위치, *"에이전트가 필요로 했든 아니든"* | **없음** |
| 추가 턴 | 없음 | **있다**(에이전트가 묻는 턴) |
| 자체 테스트 결과 | **더 빠르다** | **정답을 몇 개 더 맞혔다** |

> **설치하면 둘 다 받습니다.**

## 트레이드오프의 형태

**Push는 낭비를 감수하고 지연을 없앤다.** 필요 없는 위치도 붙지만 에이전트가 되묻는 턴이 사라진다.
**Pull은 턴을 하나 쓰고 적합성을 얻는다.** 에이전트가 자기 의도를 알고 묻기 때문에 **프롬프트 단어 매칭보다 정확하다.**

즉 **push의 추측은 프롬프트에서, pull의 판단은 에이전트의 상태에서 나온다.** push가 지는 지점은 *"사용자가 쓴 단어가 실제 필요와 어긋날 때"* 이고, 이것이 소스가 말한 **정답률 차이**의 방향과 일치한다.

## 위키에서의 위치

이 위키에서 [[model-context-protocol|MCP]]는 주로 *"에이전트에게 도구를 주는 규약"* 으로 다뤄져 왔다. 여기서는 **동일한 데이터에 대한 두 조달 방식 중 하나**로 놓인다 — MCP의 값이 *기능*이 아니라 **타이밍의 주도권**에 있다는 관점이다.

[[hook-enforced-workflow]]와 짝으로 읽으면 대비가 선명하다. 훅은 **강제**하고, MCP는 **제공**한다.

> ⚠️ *"정답을 몇 개 더 맞혔다"* 의 분모가 소스에 없고, 지연 차이의 크기도 없다. **방향만 있고 크기가 없다.**

## References

- [[tech-bridge-graft-code-knowledge-graph]] · [[graft]] · [[model-context-protocol]]
