---
title: 병목은 추론이 아니라 검색이다 (Retrieval, Not Reasoning, Is the Bottleneck)
type: concept
category: theory
tags: [retrieval, reasoning, bottleneck, evaluation, agentic-search]
aliases: [추론은 병목이 아니다, retrieval bottleneck]
related: [agentic-search, browsecomp-plus, context-window-as-floppy-disk, llm-as-search-user, agent-harness-design, true-cost-to-perfect-answer, oracle-gap]
first-seen: tech-bridge-bm25-agentic-search
sources: [tech-bridge-bm25-agentic-search]
created: 2026-09-21
updated: 2026-09-21
---

# 병목은 추론이 아니라 검색이다

**증거를 손에 쥐여 주면 모델은 답한다. 못 답하는 이유는 생각을 못 해서가 아니라 증거를 못 찾아서다.**

이 위키가 받은 **가장 깔끔한 분리 실험**이다. 같은 벤치마크([[browsecomp-plus|BrowseComp-Plus]])를 두 조건으로 돌린다.

| 조건 | 무엇을 주나 | 결과 |
|---|---|---|
| **증거 주입** | 답에 필요한 증거 문서를 **컨텍스트에 인위적으로 채워 넣는다** | **정확도가 매우 높다** |
| **도구 제공** | 같은 모델에 **검색 도구가 달린 하네스**를 준다 | **정확도가 떨어진다** |

> 만약 이 질문에 답하는 데 **필요한 증거 문서를 모델의 컨텍스트 창에 인위적으로 채워 넣으면 정확도가 매우 높아집니다.** **그러므로 추론 능력이 병목 현상의 원인은 아닙니다.** — [[jo-bergum]], [[tech-bridge-bm25-agentic-search]] (06:55~07:17)

> 하지만 **검색 도구가 있는 하네스를 사용하여 모델을 노출시키면 정확도가 떨어집니다.** 왜냐하면 **이제 정확도가 하네스, 즉 모델의 쿼리 구성 능력과 검색 도구의 검색 품질에 따라 달라지기 때문**입니다. (07:20~07:34)

**두 조건의 차이가 곧 [[agentic-search]]의 세 부품 중 둘(하네스·엔진)이 까먹는 양**이다.

## 이 위키의 어느 전제를 건드리나

이 위키의 개선 처방은 대부분 **모델에게 더 생각하게 하는** 쪽이었다.

| 페이지 | 처방 |
|---|---|
| [[true-cost-to-perfect-answer]] | 테스트 타임 컴퓨트를 더 쓴다 |
| [[fixed-budget-alpha]] · [[token-roles]] | 토큰 예산을 어디에 쓸지 고른다 |
| [[generator-evaluator-pattern]] | 한 번 더 채점하고 고친다 |
| [[agent-verification-skill]] | 검증 단계를 붙인다 |

**이 소스는 그 레버를 당기기 전에 먼저 봐야 할 것을 지목한다** — *증거가 컨텍스트에 있었는가*. 증거가 없으면 **추가 추론은 없는 것 위에서 도는 것**이다.

09-19 [[voice-latency-thinking-tradeoff]]가 *"이 도메인은 그 레버를 **금지**한다"* 였다면, 이쪽은 ***"그 레버를 당길 자리가 애초에 아니다"*** 이다.

## 그리고 이것이 AGI보다 오래 산다

> 인공 일반 지능(AGI)과 같은 **완벽한 모델을 얻더라도** (…) **여전히 사용 가능한 컨텍스트 창의 크기가 플로피 디스크 크기 정도로 제한될 거라는 말씀이시죠? 따라서 해당 컨텍스트 창에 무엇이 들어갈지 결정해야 합니다.** (07:36~07:53)

→ [[context-window-as-floppy-disk]]

## ⚠️ 수치가 하나도 없다

- 발표 전체에 **정확도 숫자가 한 번도 나오지 않는다.** 그래프를 가리키며 *"매우 높다"* / *"떨어진다"* 로만 말한다.
- *"[GPT-4]조차도 매우 높은 정확도"*(07:13~07:17)는 **ko·en-orig 양 트랙이 일치**하지만 **모델 표기·측정 조건이 없다.**
- **"증거 문서를 인위적으로 채워 넣는다"** 가 정확히 무엇인지(골든 문서만? 노이즈 포함?) **없다.**

→ **이 위키는 방향만 받고 크기는 받지 않는다.**

## 같은 날의 정량적 대응물

[[benjamin-clavie|Clavié]]의 [[oracle-gap|오라클 갭]]이 **바로 이 차이에 이름과 숫자를 붙인 것**이다 — *완벽한 문서와 내 검색 시스템 사이의 거리*. **두 발표가 같은 양을 서로 모른 채 두 방식으로 말한다**: 한쪽은 *병목이 어디인가*(정성), 다른 쪽은 *그 병목이 몇 포인트인가*(⚠️ 자기 보고).

## References

- [[tech-bridge-bm25-agentic-search]] · [[jo-bergum]] · [[browsecomp-plus]]
- 개념: [[agentic-search]] · [[context-window-as-floppy-disk]] · [[llm-as-search-user]] · [[oracle-gap]] · [[ir-evaluation-obsolescence]]
- 전제를 건드리는 곳: [[true-cost-to-perfect-answer]] · [[fixed-budget-alpha]] · [[token-roles]] · [[generator-evaluator-pattern]] · [[voice-latency-thinking-tradeoff]]
