---
title: Reference Graph vs Vector Search
type: concept
category: technique
tags: [retrieval, embeddings, code-search, knowledge-graph]
related: [retrieval-augmented-generation, code-knowledge-graph, file-discovery-tax, long-context-agents, agentic-search, eval-experiment-anatomy]
first-seen: tech-bridge-graft-code-knowledge-graph
sources: [tech-bridge-graft-code-knowledge-graph, tech-bridge-knowledge-agents-not-coding-agents, tech-bridge-unblocked-context-engine-structured-queries, tech-bridge-braintrust-agentic-vs-vector-search-eval]
created: 2026-09-15
updated: 2026-10-17
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

## ⭐ 2026-09-20 — 반대편에서 같은 구분에 도달했다

[[benjamin-clavie|Benjamin Clavié]]([[mixedbread|Mixedbread]])가 [[tech-bridge-knowledge-agents-not-coding-agents]]에서 **이 페이지와 같은 선을 반대 방향에서 긋는다.**

> **코드는 지식이지만 모든 지식이 코드는 아닙니다. 코드는 매우 독특한 형태의 지식입니다.** (03:38~03:46)

그가 드는 코드의 성질이 이 페이지의 대비표와 맞물린다 — **식별자·파일·경로라는 견고한 단서**가 있고 *"지식 노동에는 **함수 정의가 없습니다**"*(04:59). **참조 그래프를 세울 수 있는 이유가 정확히 그 정의 지점의 존재**이고, 일반 지식에는 그것이 없다.

| | **이 페이지** ([[graft]] 개발팀) | [[code-as-atypical-knowledge]] ([[benjamin-clavie\|Clavié]]) |
|---|---|---|
| 누가 파나 | **코드 검색 도구** | **지식 검색** |
| 결론 | 코드에서는 **벡터가 약하다** | 코드는 **쉬운 예외**다 — 여기서 일반화하지 마라 |
| 공통 전제 | **코드와 산문은 검색 문제로서 종류가 다르다** | 〃 |

**서로 모르는 두 회사가 같은 구분에 도달하고, 각자 자기 쪽이 어렵다고 말한다.** [[code-only-index-blind-spot]]이 세 번째 각도로 같은 선을 긋는다.

> ⚠️ **이 페이지가 적어 둔 *"벡터 검색 쪽의 반론은 이 위키에 아직 없다"* 는 여전히 유효하다.** Clavié도 벡터/임베딩을 변호하지 않는다 — 그는 **시맨틱 검색을 프리미티브 중 하나로 놓을 뿐**이다([[retrieval-primitive-repertoire]]).

그리고 같은 날 [[jo-bergum|Bergum]]이 **네 번째 선택지**를 강하게 민다 — [[bm25|BM25 어휘 검색]]. **이 위키의 검색 방법이 이제 넷이다**(어휘 · 시맨틱 · 참조 그래프 · `grep`). **넷을 어떻게 섞는지 말하는 소스는 아직 없다.**

## References

- [[tech-bridge-graft-code-knowledge-graph]] · [[code-knowledge-graph]] · [[graft]]

## 세 번째 질문 — "몇 개·누가·언제" (2026-10-15 · [[tech-bridge-unblocked-context-engine-structured-queries]])

이 페이지는 *의미가 비슷한 것* 과 *실제로 서로를 쓰는 것* 을 갈랐다. [[peter-werry|Peter]]([[unblocked|Unblocked]])는 셋째 유형을 더한다 — *"PRs that I merged last week. Who reviewed payments the most, open PRs, etc. Um and these are queries. They're not semantic searches."*(06:51~07:03)

| 질문 | 답하는 구조 |
|---|---|
| 의미가 비슷한 것 | 벡터 검색 |
| 서로를 쓰는 것 | 참조 그래프 |
| **필터·집계·시간 범위** | **구조화 쿼리** → [[nl-to-structured-query-scaffolding]] |

화자는 RAG를 깎지 않는다(*"RAG nails the content part"* 06:25) — 다른 절반을 더한다(*"the other half of Reg[=RAG]"* 17:03).

## 첫 직접 비교 — 같은 정확도, 4배 비용 (2026-10-17 · [[tech-bridge-braintrust-agentic-vs-vector-search-eval]])

[[jess-wang|Jess Wang]]([[braintrust|Braintrust]])이 코딩 에이전트의 버그 위치 찾기에서 vector search와 agentic search(grep·find·ls·cat)를 **같은 Claude Code 하네스 위에서** 비교했다. 데이터는 Microsoft TypeScript Go의 *"fix"* PR 약 20개이고, 채점은 테스트 통과 이진 채점이다. 결과: *"both got the same level of accuracy, but essentially vector search cost uh four times more than agentic search."*(14:51~15:01)

이 페이지의 대비표에서 벡터가 *"답하지 못하는 것: 연결·방향·파급"* 이라고 한 자리를 trace가 보여 준다.

- *"these chunks of code often miss things like um imports or tool calls or the calling code above it"*(15:15~15:22). 한 행에서는 *"the vector agent made 26 searches and still couldn't piece together how three functions interacted across the file."*(15:31~15:38)
- *"vector search gave a lot of proximity to the correct code, but agentic search had more of the connective tissue to connect the actual logic of those chunks of code."*(15:59~16:10)
- 비용은 정답률이 아니라 **반복 검색의 LLM 호출 누적**에서 왔다(16:19~16:33).

지금까지 이 페이지의 근거는 채택률 진술(당사자)과 논증이었다. 이 소스는 **변수 하나만 바꾼 첫 실험**이다. ⚠️ 약 20행, 작업당 1회 시행이고, 화자 스스로 *"my vector search implementation was relatively weak"*(17:00~17:03)라고 한다. 정확도 수치와 비용 단위는 발화되지 않는다. **혼합 구성은 시험하지 않았다.** 그래서 이 페이지가 적어 둔 *"벡터 검색 쪽의 반론은 이 위키에 아직 없다"* 는 여전히 유효하다. 이 실험도 벡터를 변호하지 않지만, 벡터가 **틀린다**고 하지도 않는다. 실험 설계의 틀은 [[eval-experiment-anatomy]].
