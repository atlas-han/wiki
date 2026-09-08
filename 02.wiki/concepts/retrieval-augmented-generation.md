---
title: Retrieval-Augmented Generation (RAG)
type: concept
category: technique
tags: [rag, retrieval, vector-db, semantic-search, context]
aliases: [RAG, 검색 증강 생성]
related: [agent-memory, agent-knowledge-sourcing, context-engineering, agentic-sites, llm-wiki-pattern, code-knowledge-graph]
first-seen: tech-bridge-agent-knowledge-four-ways
sources: [tech-bridge-agent-knowledge-four-ways, tech-bridge-agentic-sites, karpathy-llm-wiki-gist]
created: 2026-09-08
updated: 2026-09-08
---

# Retrieval-Augmented Generation (RAG)

컨텍스트 창에 모든 것을 미리 넣는 대신, **필요할 때 외부 소스에서 관련 조각만 가져와** 생성에 쓰는 기법.

> 핵심은 **모든 정보를 컨텍스트 창에 미리 입력하는 대신**, 에이전트가 필요한 정보, 즉 **외부 소스에서 관련 정보만 가져와 실제로 필요할 때만** 처리한다는 것입니다. — [[tech-bridge-agent-knowledge-four-ways]]

> 📌 **이 페이지는 늦게 생겼다.** RAG는 이 위키가 [[agentic-sites]]·[[llm-wiki-pattern]]·[[code-knowledge-graph]]·[[karpathy-llm-wiki-gist]]에서 **대비항으로만 계속 언급**해 온 용어였고, 2026-09-08에 [[tech-bridge-agent-knowledge-four-ways]]가 처음으로 RAG 자체를 설명하면서 페이지가 섰다.

## 동작

1. 문서 모음을 준비한다 — 소스의 예시는 **매뉴얼·의존성 맵**.
2. 에이전트가 질문을 던진다.
3. **의미 검색(semantic search)** 으로 일치하는 조각을 찾는다.
4. **관련 청크가 컨텍스트 창으로 반환된다.**

저장소는 통상 **벡터 데이터베이스**다.

## RAG를 정의하는 것은 검색 기술이 아니라 출처

[[agent-memory|메모리]]와 나란히 놓았을 때에만 RAG의 경계가 분명해진다. 둘 다 *필요할 때 관련 지식을 불러오고*, 둘 다 벡터 DB일 수 있으며, 둘 다 의미 검색을 쓸 수 있다.

> 언뜻 보면 메모리는 (…) **RAG와 상당히 유사해 보이지만** (…) **차이점은 그 지식이 어디에서 오는가에 있습니다.**

> RAG는 **벡터 데이터베이스에 저장된 문서**를 읽는데, 그 문서들은 **사람이 직접 벡터 데이터베이스에 넣은 것**들입니다. 마치 **일부러 거기에 보관해둔** 것 같았어요.

| | RAG | [[agent-memory\|메모리]] |
|---|---|---|
| **지식의 출처** | **사람이 의도적으로 적어 넣은 문서** | 에이전트가 겪고 스스로 저장한 경험 |
| **쓰기 주체** | 사람 | 에이전트 |
| **방향** | 읽기 | **읽고 쓴다** |
| 저장소·검색 | 벡터 DB · 의미 검색 | (같을 수 있다) |

→ [[agent-knowledge-sourcing]]

## 이 위키의 다른 RAG 사례

- **[[agentic-sites]]** — [[carlos-sanchez]]의 *"자기 사이트 RAG"*. 방문자 의도에 맞춰 자기 사이트의 블록을 검색해 재조립한다. **1~2초 예산** 안에서 도는 것이 제약이고, 그래서 작은 모델([[gemma-4]])+빠른 추론([[cerebras]]) 조합을 쓴다. → 이 위키에서 **RAG에 정량적 제약이 붙은 유일한 사례**다.
- **[[llm-wiki-pattern]]·[[karpathy-llm-wiki-gist]]** — LLM 위키는 RAG의 **대안**으로 제시된다. 검색해서 조각을 끌어오는 대신, **미리 합성해 둔 페이지**를 읽는다.
- **[[code-knowledge-graph]]** — 코드에 대해 청크 검색 대신 **구조를 그래프로** 둔다.

세 사례가 같은 축 위에 있다 — **검색 시점에 조각을 모을 것인가, 미리 합성해 둘 것인가.** [[tech-bridge-agent-knowledge-four-ways]]는 이 축을 다루지 않고 RAG를 기본형으로만 설명한다.

## 미해결 사항

- **RAG와 [[agent-memory|메모리]]가 어긋날 때** 무엇을 믿는가. 소스의 예시 자체가 이 충돌을 품고 있다 — *"실제 원인은 여기 런북에 기록되지 않은 내용이었을 수도 있습니다"*. 즉 **문서가 틀렸고 경험이 맞았던 사례**인데, 판정 규칙은 없다. [[context-engineering]]의 신뢰 등급 슬롯이 다루는 문제와 같은 자리다.
- 청킹·임베딩·재랭킹 등 구현 층위는 이 위키의 어느 소스도 다루지 않았다.
- 비용·지연 특성 (첫 소스에 수치가 없다).

## References

- [[tech-bridge-agent-knowledge-four-ways]] — RAG를 [[agent-skills]]·[[model-context-protocol]]·[[agent-memory]]와 나란히 정의한 첫 소스
- [[tech-bridge-agentic-sites]] · [[karpathy-llm-wiki-gist]]
- 관련: [[agent-knowledge-sourcing]] · [[agent-memory]] · [[context-engineering]] · [[agentic-sites]] · [[llm-wiki-pattern]] · [[code-knowledge-graph]]
