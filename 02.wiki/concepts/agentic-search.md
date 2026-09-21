---
title: 에이전트 검색 (Agentic Search)
type: concept
category: architecture
tags: [retrieval, search, agent-loop, harness, bm25]
aliases: [agentic search, agentic retrieval, 에이전트 검색, 에이전트 기반 검색]
related: [retrieval-augmented-generation, agent-collaboration-as-search, agent-knowledge-sourcing, context-engineering, bm25, llm-as-search-user, corpus-as-filesystem-workspace, ir-evaluation-obsolescence]
first-seen: tech-bridge-bm25-agentic-search
sources: [tech-bridge-bm25-agentic-search, tech-bridge-knowledge-agents-not-coding-agents]
created: 2026-09-21
updated: 2026-09-21
---

# 에이전트 검색 (Agentic Search)

**에이전트 루프 *안에서* 일어나는 검색.** 사람이 질문하고 결과를 읽는 검색이 아니라, **작업을 수행하던 에이전트가 필요해서 스스로 던지고 스스로 읽고 다시 던지는** 검색.

> 제 정의에 따르면 **에이전트 검색은 본질적으로 에이전트 루프 내부에서의 검색**입니다. 그러니까 에이전트가 코딩을 하거나 심층적인 조사를 하는 등 **어떤 작업을 수행하려고 하는 거죠.** 그리고 그 안에는 **에이전트가 해당 작업을 성공적으로 완료하기 위해 필요한 정보**가 담겨 있죠. — [[jo-bergum]], [[tech-bridge-bm25-agentic-search]] (01:03~01:23)

> 📌 **이 위키가 검색을 독립된 주제로 다루는 첫 페이지다.** 지금까지 검색은 늘 **무언가의 부품**이었다 — [[retrieval-augmented-generation|RAG]]는 [[agent-knowledge-sourcing|지식 조달]] 4갈래 중 하나였고, [[reference-graph-vs-vector-search]]는 코드 인덱싱의 방법론이었고, [[agent-collaboration-as-search]]는 멀티 에이전트를 검색으로 **비유**한 것이었다. 여기서는 **검색을 20년 해 온 사람이 검색 자체를 놓고 말한다.**

## 세 가지 부품

> 훌륭한 에이전트 기반 검색 시스템을 구축하려면 기본적으로 **세 가지**가 필요합니다. (01:28~01:31)

| 부품 | 무엇을 하나 | 이 위키의 페이지 |
|---|---|---|
| **유능한 모델** | 도구를 쓰고 **쿼리를 구성한다** | [[llm-as-search-user]] |
| **하네스** | 검색·탐색 기능을 모델에 **어떻게 노출하는가** — 툴 호출 또는 **코드 모드** | [[agent-harness-design]] · [[corpus-as-filesystem-workspace]] |
| **검색 엔진** | **수십억 개 문서**를 효율적으로 뒤진다 | [[bm25]] · [[hornet]] |

**이 삼분할이 이 위키에 중요한 이유는 책임이 어디로 가는지를 바꾸기 때문이다.** 정확도가 떨어졌을 때 그것이 모델 탓인지, 하네스 탓인지, 엔진 탓인지가 **분리 가능해진다** — [[retrieval-not-reasoning-bottleneck]]이 바로 그 분리를 실험으로 보여 준다.

## 무엇이 달라지는가 — 검색이 한 번이 아니다

> [BrowseComp-Plus] 데이터 세트에서는 이러한 수수께끼 같은 질문 중 하나가 **검색 경로(search trajectory)** 가 됩니다. 모델이 **쿼리를 실행하고, 응답을 받고, 그 응답을 읽고, 쿼리를 재구성하고, 컨텍스트 창을 채우거나 답을 찾을 때까지 이 과정을 계속하기 때문**입니다. (08:02~08:19)

| | 고전적 검색 | 에이전트 검색 |
|---|---|---|
| 단위 | **쿼리 하나 → 순위 목록 하나** | **궤적(trajectory)** — 쿼리 여러 개의 연쇄 |
| 읽는 쪽 | 사람 (파란 링크 10개를 훑는다) | **모델** (읽고 재구성한다) |
| 종료 조건 | 사람이 만족 | **컨텍스트가 차거나 답을 찾거나, 둘 중 먼저** |
| 평가 | nDCG | **작업을 해냈는가** → [[ir-evaluation-obsolescence]] |

## 두 이름이 같은 것을 가리킨다

화자는 *"agentic search 또는 agentic **retrieval**"* 을 나란히 쓰고 **둘을 구분하지 않는다**(00:56~00:58, 17:19~17:22). ⚠️ **ko 자막은 두 단어를 같은 말로 옮겨 이 병렬 자체가 사라진다.** → [[tech-bridge-bm25-agentic-search]]

## 이 위키의 인접 프레이밍과

[[agent-collaboration-as-search]]([[jean-denis-greze|Greze]], 09-10)가 *"대부분의 LLM 시스템은 그냥 검색 문제"* 라고 했을 때 그것은 **멀티 에이전트를 설명하기 위한 재해석**이었다. 여기서는 **같은 문장이 비유가 아니라 직업**이다 — 그리고 [[jo-bergum|Bergum]]은 그 문장에서 멈추지 않고 **엔진·하네스·모델로 쪼갠 다음 어디가 병목인지 측정한다.**

같은 날 [[benjamin-clavie|Clavié]]는 **반대 방향**에서 온다 — 검색 품질이 아니라 **검색의 조직**이 병목이라고 본다([[orchestrator-searcher-split]]). **두 소스를 겹치면 에이전트 검색의 실패가 세 곳에서 날 수 있다**: 엔진이 나쁘거나(품질), 쿼리를 못 쓰거나(하네스), **문제를 안 쪼갰거나**(조직).

## References

- [[tech-bridge-bm25-agentic-search]] · [[tech-bridge-knowledge-agents-not-coding-agents]]
- 인물·조직: [[jo-bergum]] · [[hornet]] · [[benjamin-clavie]]
- 하위: [[bm25]] · [[llm-as-search-user]] · [[retrieval-not-reasoning-bottleneck]] · [[context-window-as-floppy-disk]] · [[corpus-as-filesystem-workspace]] · [[ir-evaluation-obsolescence]] · [[which-bm25-problem]]
- 관련: [[retrieval-augmented-generation]] · [[agent-collaboration-as-search]] · [[agent-knowledge-sourcing]] · [[agent-harness-design]] · [[reference-graph-vs-vector-search]]
