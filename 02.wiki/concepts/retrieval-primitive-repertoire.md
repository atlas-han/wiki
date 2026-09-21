---
title: 검색 프리미티브 레퍼토리 (Retrieval Primitive Repertoire)
type: concept
category: patterns
tags: [tool-design, primitives, grep, bm25, semantic-search, co-design, training-data]
aliases: [프리미티브 레퍼토리, 도구 공동 설계, tool co-design]
related: [bm25, code-as-atypical-knowledge, tools-are-not-neutral, llm-as-search-user, ride-the-optimization-trajectory, agent-tool-design-practices, retrieval-augmented-generation, reference-graph-vs-vector-search]
first-seen: tech-bridge-knowledge-agents-not-coding-agents
sources: [tech-bridge-knowledge-agents-not-coding-agents]
created: 2026-09-21
updated: 2026-09-21
---

# 검색 프리미티브 레퍼토리

**`grep`·BM25·시맨틱 검색은 각각 프리미티브이고, 모델은 그 전부를 알고 골라 쓸 줄 알아야 한다.** 그리고 **도구는 에이전트와 함께 설계되어야 한다** — 모델이 쓸 줄 모르는 도구는 없는 것과 같다.

> 이건 **프리미티브(primitive)에 관한 것입니다 — [`grep`]이 프리미티브이고, BM25가 프리미티브이고, 시맨틱 검색이 프리미티브입니다. 그리고 그 모두가 아주 잘 훈련되어야 합니다. 모델이 그것들 전부에 대해 알아야 합니다.** — [[benjamin-clavie]], [[tech-bridge-knowledge-agents-not-coding-agents]] (16:28~16:41)

## ⭐ 학습 데이터가 도구 선택을 편향시킨다

**이 위키가 처음 받는 형태의 실패 모드**다.

> 자주 보게 되는 한 가지는 **에이전트가 [`grep`] 쿼리를 쓰려고 한다는 것입니다. [`grep`]은 학습 데이터 어디에나 있고 BM25도 데이터 어디에나 있으니까요. 그리고 그게 항상 필요한 것은 아닙니다.** (16:06~16:17)

> **때로는 PDF에 대한 시맨틱 검색이 필요한데, PDF는 [`grep`] 할 수 없습니다. PDF를 BM25 할 수는 있지만, 더 나은 쿼리를 써야 합니다.** (16:17~16:23)

**즉 모델은 가장 익숙한 도구로 손이 가고, 그 익숙함의 출처는 과제 적합성이 아니라 학습 코퍼스의 분포다.**

이 위키의 기존 도구 실패 모드들과 종류가 다르다:

| 실패 모드 | 원인 | 페이지 |
|---|---|---|
| 도구를 못 찾는다 | 발견 비용 | [[capability-discovery-burden]] · [[file-discovery-tax]] |
| 도구가 너무 많다 | 선택 과부하 | [[agent-tool-design-practices]] |
| 도구 설명이 나쁘다 | 인터페이스 | [[build-a-lever]] · [[adaptive-response-format]] |
| **도구가 있는데 익숙한 쪽으로 간다** | **학습 데이터 분포** | **이 페이지** |

## ⚠️ [[ride-the-optimization-trajectory]]의 청구서

같은 날 [[jo-bergum|Bergum]]은 **정확히 이 성질을 레버로 쓰라**고 말한다 — *모델이 `grep`·bash에 최적화돼 있으니 그 위에 얹어라*.

**두 소스가 같은 사실의 양면을 말한다.**

| | [[jo-bergum\|Bergum]] | [[benjamin-clavie\|Clavié]] |
|---|---|---|
| 같은 사실 | 모델은 `grep`·BM25에 **아주 익숙하다** | 〃 |
| 판정 | **레버** — 새 모델마다 공짜로 좋아진다 | **편향** — 틀린 도구로 손이 간다 |
| 조건 | **텍스트 코퍼스**에서 | **스캔 PDF**에서 |
| 처방 | 궤적 위에 얹어라 | **레퍼토리를 훈련시켜라** |

**이 위키는 어느 쪽도 채택하지 않고 조건을 기록한다**: *익숙함에 올라타는 것은 그 익숙함이 도메인에 맞을 때만 이득이다.*

## 공동 설계(co-design)

> **더 중요한 것은, 도구가 에이전트와 함께 설계(co-design)되어야 한다는 점입니다. 에이전트가 도구를 어떻게 쓰는지 알아야 하니까요.** (16:02~16:06)

> **여러분의 에이전틱 하네스나 에이전틱 모델이 하나 이상의 도구를 가지고 있다는 것을 아는 게 매우 중요합니다.** (16:23~16:28)

**"모델이 안다"는 요구가 하네스와 학습 양쪽에 걸린다** — 프롬프트로 알려 주는 것(하네스)과 그 도구에 훈련돼 있는 것(모델)이 둘 다 필요하다는 뜻이고, **후자는 도구 제작자가 통제할 수 없다.** ⚠️ **소스는 그 비대칭을 지적하지 않는다.**

## 이 위키의 검색 방법 목록이 이제 넷이다

| 프리미티브 | 강한 곳 | 약한 곳 | 페이지 |
|---|---|---|---|
| **`grep` / 정규식** | 코드·텍스트의 **문자 그대로** | **PDF·이미지** | [[code-as-atypical-knowledge]] |
| **BM25 / 어휘** | 이름·개체·SKU·**정확 일치** | 스캔 문서의 천장 | [[bm25]] |
| **시맨틱 / 임베딩** | 의미가 다른 말로 쓰인 것 | 고정 어휘·**비용** | [[retrieval-augmented-generation]] |
| **참조 그래프** | **무엇이 무엇을 쓰는가** | 코드 밖 | [[reference-graph-vs-vector-search]] |

**네 번째는 이 소스에 없다** — 이 위키가 09-15에 따로 받은 것이다. **넷을 어떻게 섞는지 말하는 소스는 이 위키에 아직 없다.**

## References

- [[tech-bridge-knowledge-agents-not-coding-agents]] · [[benjamin-clavie]]
- 양면을 이루는 곳: [[ride-the-optimization-trajectory]] · [[llm-as-search-user]]
- 개념: [[bm25]] · [[code-as-atypical-knowledge]] · [[tools-are-not-neutral]] · [[retrieval-augmented-generation]] · [[reference-graph-vs-vector-search]]
- 도구 실패 모드: [[agent-tool-design-practices]] · [[build-a-lever]] · [[capability-discovery-burden]] · [[file-discovery-tax]]
