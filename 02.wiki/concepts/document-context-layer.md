---
title: 문서 컨텍스트 레이어 (Document Context Layer)
type: concept
category: architecture
tags: [rag, context-layer, document-parsing, agent-harness, extraction, workflow]
aliases: [context layer, 컨텍스트 레이어, 에이전트 네이티브 문서 플랫폼, agent native document platform]
related: [retrieval-augmented-generation, document-parsing-for-agents, tiered-document-parsing, agentic-search, tools-and-context-over-harness, context-engineering, workflow-vs-agent, corpus-as-filesystem-workspace]
first-seen: tech-bridge-llamaindex-document-context-layer
sources: [tech-bridge-llamaindex-document-context-layer]
created: 2026-09-29
updated: 2026-09-29
---

# 문서 컨텍스트 레이어

**RAG를 "검색 파이프라인"이 아니라 "에이전트 하네스 + 컨텍스트 레이어"로 분해했을 때, 문서에 갇힌 비정형 지식을 에이전트가 읽고 다룰 수 있게 만드는 쪽 절반.** [[jerry-liu|Jerry Liu]]([[llamaindex|LlamaIndex]])가 [[tech-bridge-llamaindex-document-context-layer]]에서 제시했다.

> *"RAG in 2026 … basically decomposes into an agent harness plus a context layer"* (00:30~00:36)

## 왜 분해되는가

naive RAG(2023)는 *청킹 → 임베딩 → 벡터 DB → top-k → 생성*, *"All the steps are fixed"*(01:40~01:53)였다. 그 뒤 **검색의 복잡도가 에이전트 루프로 넘어갔다** — *"the retrieval complexity has started to get baked into the agent layer"*(02:29~02:33). 그러면 파이프라인에 남는 일은 **"무엇을 검색할 수 있게 만들어 두느냐"** 다. 화자의 표현으로 *"context really is everything"*(05:20~05:24), *"you could have a infinitely smart agent"* 라도(05:24~05:26) 올바른 컨텍스트 없이는 가치가 없다.

## 세 층 (06:38~07:45)

| 층 | 역할 | 이 위키의 페이지 |
|---|---|---|
| **파싱** | PDF·PPT·Word를 *"accurate, token-efficient context"*(06:51~06:54)로 — 마크다운·메타데이터 | [[document-parsing-for-agents]] · [[tiered-document-parsing]] |
| **시맨틱·저장** | *"document management for humans and agents"*(07:05~07:07) — 에이전트 인터페이스로 문서를 담고 관리. 구조화 추출(인용·신뢰도 점수)과 검색 도구 세트(BM25·grep·벡터·읽기·스크롤)가 여기 | [[retrieval-primitive-repertoire]] · [[bm25]] |
| **반복 가능한 문서 워크플로** | 송장·KYC·청구 — *"instead of always offloading it to a generalized agent"*, 비용·정확도를 조율한 전용 워크플로(07:33~07:45) | [[workflow-vs-agent]] |

**미해결로 남긴 것**(08:02~08:10): 에이전트 네이티브 문서 포맷 · 문서 버전 관리 · 문서 편집 · *"hill climbing as a service"* — 발표에서 전부 건너뛰었다.

## 이 위키의 다른 분해와

- [[tools-and-context-over-harness]]([[ryan-lopopolo|Lopopolo]]) — *하네스는 고정, 도구·컨텍스트에 투자*. 같은 선을 긋고, 이 페이지는 그 **컨텍스트 쪽의 내부 구조**다.
- [[agentic-search]]의 삼분할(모델·하네스·**검색 엔진**, [[jo-bergum|Bergum]]) — 엔진을 "컨텍스트 레이어"로 넓히면 **파싱이 엔진 앞에 한 층 더 생긴다.** 엔진이 좋아도 PDF의 표가 선분으로 들어가면 소용없다.
- [[corpus-as-filesystem-workspace]] — 시맨틱·저장 층의 *"agent interface"* 가 파일 시스템 모양인지 MCP인지 소스는 말하지 않는다. ⚠️ 미확정.
- [[context-engineering]] — 화자는 *"context is moving up the stack"*(02:55~02:57): 컨텍스트 창 관리(compaction·long context)에서 **어떤 MCP 서버·스킬을 붙이느냐**로 화두가 옮겨 갔다고 본다.

## ⚠️ 유보

- **판매자의 분해다.** 세 층은 LlamaIndex의 제품 구획(LlamaParse·추출·워크플로)과 겹친다.
- 시맨틱·저장 층은 **정의 한 문단**뿐이다. 보안·접근 제어(SharePoint·Box·S3를 여는 일)는 없다 → [[prompt-injection]].

## References

- [[tech-bridge-llamaindex-document-context-layer]] · [[jerry-liu]] · [[llamaindex]]
- [[retrieval-augmented-generation]] · [[agentic-search]] · [[tools-and-context-over-harness]]
