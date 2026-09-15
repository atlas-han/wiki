---
title: Reference Graph vs Vector Search
type: concept
category: technique
tags: [retrieval, embeddings, code-search, knowledge-graph]
related: [retrieval-augmented-generation, code-knowledge-graph, file-discovery-tax, long-context-agents]
first-seen: tech-bridge-graft-code-knowledge-graph
sources: [tech-bridge-graft-code-knowledge-graph]
created: 2026-09-15
updated: 2026-09-15
---

# Reference Graph vs Vector Search

**코드 검색에서 "의미가 비슷한 것"과 "실제로 서로를 쓰는 것"은 다른 질문이다.** [[tech-bridge-graft-code-knowledge-graph]]가 이 구분을 한 문장으로 세운다.

> **계정을 만드는 코드와 계정을 지우는 코드는 둘 다 "계정" 질문에 걸리지만 정반대 일을 합니다. 잘못 고르면 대가가 큽니다.**

## 대비

| | 벡터 검색 | 참조 그래프 |
|---|---|---|
| 무엇을 저장하나 | 코드 구간의 **임베딩(숫자)** | **노드**(코드 조각) + **엣지**(무엇이 무엇을 쓰는가) |
| 질의 | *"이것과 비슷한 것"* | *"이것을 쓰는 것"* / *"이것이 쓰는 것"* |
| 답하지 못하는 것 | **연결·방향·파급** | 이름이 전혀 다른 유사 기능 |
| 갱신 | 보통 재임베딩 | **변경분만** → [[incremental-index-freshness]] |
| 모델 필요 | 임베딩 모델 필요 | **불필요**(정적 분석) |

## 왜 코드에서 특히 갈리는가

자연어 문서에서는 **유사도가 곧 관련성**인 경우가 많다. 코드에서는 **반대말이 가장 비슷하게 생긴다**(`createAccount` / `deleteAccount`). 게다가 편집 작업이 정말 알아야 하는 것은 *"이걸 바꾸면 무엇이 깨지는가"* 인데, **그건 유사도가 아니라 의존 관계**다.

소스는 이것을 이론이 아니라 **채택률**로 뒷받침한다 — *"대부분의 코딩 에이전트는 [벡터 검색을] 아예 쓰지 않습니다."*

## 위키에서의 위치

[[retrieval-augmented-generation]]가 2026-09-08 IBM 편에서 *"컨텍스트에 다 쏟아붓지 말고 경로를 나눠라"* 로 섰다면, 이 페이지는 **"그 경로 중 벡터 경로는 코드 도메인에서 약하다"** 를 더한다. 두 방식이 배타적이라는 주장은 **소스에 없다** — 소스는 자기 도구를 팔고 있고, **하이브리드 논의는 하지 않는다.**

> ⚠️ 진술의 출처는 [[graft]] 개발팀과 [[ai-labs]] — **당사자 진술**이다. 벡터 검색 쪽의 반론은 이 위키에 아직 없다.

## References

- [[tech-bridge-graft-code-knowledge-graph]] · [[code-knowledge-graph]] · [[graft]]
