---
title: 검색 쪽 컨텍스트 압축 (Retrieval-Side Context Compression)
type: concept
category: technique
tags: [retrieval, context-engineering, token-efficiency, cost, agent-harness]
aliases: [토큰 추출, token extraction, 검색 단 압축]
related: [context-engineering, token-roles, harness-pruning, corpus-as-filesystem-workspace, bm25, true-cost-to-perfect-answer]
first-seen: tech-bridge-exa-perfect-search-for-agents
sources: [tech-bridge-exa-perfect-search-for-agents]
created: 2026-09-22
updated: 2026-09-22
---

# 검색 쪽 컨텍스트 압축

**문서를 통째로 넘기지 않고, 검색 엔진이 그중 가장 중요한 토큰만 골라서 넘긴다.** 압축의 책임이 에이전트가 아니라 **검색 쪽**에 있다.

> **[LLM]이 쿼리를 수행할 때 필요한 정보, 즉 필요한 토큰만 얻기를 원하기 때문입니다. 그래서 저희는 10개의 문서를 제공하고, 그중에서 가장 중요한 100개 정도의 토큰만 뽑아서 드립니다. 이렇게 하면 후속 LLM 비용을 크게 절감할 수 있습니다.** — [[will-bryk]], [[tech-bridge-exa-perfect-search-for-agents]] (11:45~12:00)

> 📌 **이 위키의 컨텍스트 절약 논의가 전부 에이전트 *안쪽* 에 있었다** — [[context-engineering]]·[[token-roles]]·[[harness-pruning]]·[[nightly-memory-consolidation]]. **압축을 외부 서비스가 대신 해 주는 형태는 처음이다.**

## ⭐ 같은 문제에 세 가지 정반대 처방

**2026-09-19~22 나흘 사이에 들어온 세 소스가 *검색 결과를 에이전트에게 어떻게 건넬 것인가* 에 각각 다르게 답한다.**

| 처방 | 소스 | 에이전트가 받는 것 | 근거 |
|---|---|---|---|
| **전부 줘라** | [[corpus-as-filesystem-workspace]] ([[jo-bergum\|Bergum]], 09-21) | 파일 시스템에 펼쳐진 **결과 전체** — `grep`·`sed`로 직접 판다 | 점진적 정보 공개, 모델이 코딩에 최적화돼 있다 |
| **왜 나왔는지 알려 줘라** | [[bm25]] ③ ([[jo-bergum\|Bergum]], 09-21) | 결과 + **설명 가능성** — 문자 그대로의 일치라 검사·재구성이 된다 | 모델의 **다음 쿼리**를 위해 |
| **골라서 줄여 줘라** | **이 페이지** ([[will-bryk\|Bryk]], 09-22) | **100 토큰** | 후속 LLM 비용 |

**⚠️ 세 번째는 앞의 둘과 양립하기 어렵다.** 버린 것을 에이전트가 모르면 **검사할 수도, 무엇을 놓쳤는지 알고 쿼리를 다시 쓸 수도 없다.** [[agentic-search]]가 정의한 **궤적**(쿼리 → 읽기 → 재구성)이 성립하려면 읽을 것이 남아 있어야 한다.

> ⚠️ **소스는 이 트레이드오프를 인지하지 않는다.** 비용 절감으로만 제시한다. **이 위키가 겹쳐서 읽은 것이다.**

## 압축의 주체가 바뀌면 무엇이 달라지나

| | 에이전트 안쪽 압축 | **검색 쪽 압축** |
|---|---|---|
| 무엇을 버렸는지 | 에이전트가 **안다** | ⚠️ **모른다** |
| 판단 기준 | 에이전트의 현재 과제 | **검색 엔진의 관련성 추정** |
| 실패 시 | 재요약·재탐색 가능 | ⚠️ **조용히 빈다** |
| 비용 | 버리기 전에 **한 번은 낸다** | **내지 않는다** |

**마지막 줄이 이 기법이 존재하는 이유다** — 에이전트 안쪽 압축은 **버릴 토큰의 값을 이미 치른 뒤**에 버린다. 검색 쪽 압축만이 그 비용을 처음부터 없앤다. → [[true-cost-to-perfect-answer]]

## 미해결

- **무엇을 기준으로 100 토큰을 고르는지** 말하지 않는다.
- **"가장 중요한"의 측정**도, 압축으로 인한 **정확도 손실**도 제시되지 않는다.
- 에이전트가 **버려진 부분을 다시 요청할 수 있는지**(확장 경로) 언급이 없다.
- 100 토큰·10 문서가 **조정 가능한 값인지** 불명.

## References

- [[tech-bridge-exa-perfect-search-for-agents]] · [[will-bryk]] · [[exa]]
- ⚠️ 반대 처방: [[corpus-as-filesystem-workspace]] · [[bm25]]
- 관련: [[context-engineering]] · [[token-roles]] · [[harness-pruning]] · [[agentic-search]] · [[true-cost-to-perfect-answer]] · [[retrieval-augmented-generation]]
