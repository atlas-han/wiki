---
title: File Discovery Tax
type: concept
category: theory
tags: [coding-agents, context-window, token-economics, tool-use]
related: [context-engineering, context-anxiety, code-knowledge-graph, reference-graph-vs-vector-search, agent-harness-design, retrieval-augmented-generation]
first-seen: tech-bridge-graft-code-knowledge-graph
sources: [tech-bridge-graft-code-knowledge-graph]
created: 2026-09-15
updated: 2026-09-15
---

# File Discovery Tax

**코딩 에이전트가 코드를 고치기 *전에* 고칠 자리를 찾느라 치르는 비용.** [[tech-bridge-graft-code-knowledge-graph]]가 이 비용을 편집 비용과 분리해 이름을 붙였다.

## 왜 곱셈이 되는가

1. 변경 요청 → 에이전트가 **터미널 검색**으로 자리를 찾는다.
2. **첫 시도에 찾는 경우가 드물어** 여러 도구로 좁힌다.
3. **매 턴마다 지금까지의 대화 전체 + 이미 쓴 도구의 응답이 다시 전송된다.**
4. 따라서 비용 ≈ **턴 수 × 누적 컨텍스트**. 검색이 하나 늘 때마다 **다음 모든 턴이 비싸진다.**

> **버튼 하나를 초록색으로 바꾸려 해도** 파일 검색 → 결과가 컨텍스트로 → 다른 도구로 해당 줄 읽기 → **그러고 나서야** 편집.

## 두 가지 결과

| 결과 | 소스의 진술 |
|---|---|
| **사용량 한도** | *"한 세션에서 여러 작업을 시키다 한도에 닿는 이유가 실은 이것"* |
| **품질 저하** | *"컨텍스트 창에 너무 많은 것이 들어 있어 에이전트가 한 번에 한 가지에 집중하지 못한다"* |

두 번째가 중요하다 — 이 위키의 [[context-anxiety]]·[[context-engineering]]은 **무엇을 넣을지 고르는 문제**를 다뤘는데, 여기서는 **넣을 것을 만들어 내는 행위 자체**가 원인이다.

## 다른 병목과의 관계

[[verification-bottleneck]]·[[verification-cost-asymmetry]]가 말하는 병목은 **변경한 뒤**에 있다. 탐색세는 **변경하기 전**에 있다. 둘은 경쟁하는 주장이 아니라 **작업의 앞뒤를 각각 가리킨다.**

## 어떻게 없애는가

탐색을 **미리 만들어 둔 인덱스 조회**로 바꾸면 턴이 사라진다 → [[code-knowledge-graph]], [[graft]]. 단 인덱스가 덮지 못하는 파일에서는 **그대로 남는다** → [[code-only-index-blind-spot]].

> ⚠️ 절감 폭은 **프로젝트 크기에 비례한다.** 화자 본인의 단서: *"작은 프로젝트에는 애초에 아낄 검색이 별로 없다."*

## References

- [[tech-bridge-graft-code-knowledge-graph]] — 이 위키 첫 명시적 진단
- [[graft]] · [[code-knowledge-graph]] · [[push-vs-pull-context-retrieval]]
