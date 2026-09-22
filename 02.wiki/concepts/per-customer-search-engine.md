---
title: 고객마다 다른 검색 엔진 (Per-Customer Search Engine)
type: concept
category: architecture
tags: [retrieval, search, product, configuration, evaluation, benchmarking]
aliases: [5000개의 검색 엔진, per-customer search, 맞춤 검색]
related: [which-bm25-problem, ir-evaluation-obsolescence, agentic-search, search-latency-tiers, agent-roi-measurement]
first-seen: tech-bridge-exa-perfect-search-for-agents
sources: [tech-bridge-exa-perfect-search-for-agents]
created: 2026-09-22
updated: 2026-09-22
---

# 고객마다 다른 검색 엔진

**"완벽한 검색"은 하나의 물건이 아니다. 무엇이 완벽한지는 고객이 정한다.**

> **우리가 하나의 검색 엔진을 만드는 것이 아니라는 점입니다. 완벽한 검색이란 한 가지로 정의될 수 있는 것이 아닙니다. 사실 저희는 고객 5,000곳 각각에 [하나씩] 5,000개의 검색 엔진을 보유하고 있는 셈이죠.** — [[will-bryk]], [[tech-bridge-exa-perfect-search-for-agents]] (12:26~12:36)

> **우리는 완벽한 검색이 무엇인지 굳이 규정하고 싶지 않으니까요. 여러분이 정확히 무엇을 원하는지 말해 주길 바랍니다.** (12:36~12:47)

> ⚠️ **ko 자막이 이 문장을 "고객 5,000명당 각각 5,000개"로 옮겨 규모가 5,000배로 읽힌다.** 원문은 **고객 1곳당 1개, 합 5,000개**다.

## 노출된 축

소스가 드는 설정 축은 다섯이다(12:47~13:02):

| 축 | 선택지 |
|---|---|
| **속도 대 품질** | 200ms 엔드포인트 ↔ 분 단위 복합 질의 → [[search-latency-tiers]] |
| **도메인 화이트리스트** | *"[이] 1,000개 도메인에서만"* |
| **도메인 블랙리스트** | *"[저] 1,000개 도메인은 절대"* |
| **기간** | *"이 기간 내에서만"* |
| **문서 유형** | *"상품 페이지는 아예 안"* |

**앞의 넷은 고전적 검색 필터인데, 파는 쪽이 그것을 필터가 아니라 *엔진의 정체성* 으로 부른다** — 같은 코퍼스 위의 옵션이 아니라 **다른 제품**이라는 프레이밍이다.

## ⭐ [[which-bm25-problem]]이 제품 형태로 재발한다

**이 위키는 하루 전에 정확히 이 문제를 방법론적 결함으로 세워 놨다.**

> **"어떤 BM25를 말씀하시는 건가요?" 그것이 특정 벤치마크의 전반적 정확도에 상당히 큰 영향을 미치기 때문입니다.** — [[jo-bergum|Bergum]], [[tech-bridge-bm25-agentic-search]] (10:25~10:32)

**같은 구조인데 방향이 반대다.**

| | [[which-bm25-problem]] (09-21) | 이 페이지 (09-22) |
|---|---|---|
| 가변성의 위치 | **하이퍼파라미터** | **고객 설정 전체** |
| 어떻게 다뤄지나 | **결함** — 기준선을 제대로 맞춰라 | **기능** — 유연성이 제품이다 |
| 귀결 | 벤치마크가 **틀린다** | ⚠️ 벤치마크가 **성립하지 않는다** |

**⚠️ 그래서 같은 발표의 *"인간을 위해 만들어진 구글보다 낫다"*(13:14~13:18)는 원리적으로 검증할 수 없는 형태가 된다** — **어떤 설정의 Exa**가 나은지 말할 수 없기 때문이다. **화자는 이것을 장점으로만 제시하고 긴장을 다루지 않는다.**

이것은 [[ir-evaluation-obsolescence]]([[jo-bergum|Bergum]]: *nDCG는 끝났다, 모델이 작업을 해내는지 보라*)와도 어긋난다 — **작업 단위로 재려 해도 엔진이 고객마다 다르면 비교군이 없다.**

## ✅ 반대 방향의 관측

**"완벽함을 정의하지 않겠다"는 태도 자체는 이 위키의 다른 소스와 맞는다.** [[benjamin-clavie|Clavié]]의 [[code-as-atypical-knowledge]](*'30일'이 네 가지를 뜻할 때*)와 [[jo-bergum|Bergum]]의 [[bm25]] 도메인 대조(웹 문서 ↔ 스캔된 PDF)는 **검색의 정답이 도메인마다 다르다**는 것을 각자 다른 근거로 말한다. **이 소스는 그 사실을 제품 구조로 받아들인 첫 자리다.**

⚠️ **다만 그 둘은 "왜 다른가"를 설명했고, 이 소스는 "다르니까 고르세요"에서 멈춘다.**

## 미해결

- **기본값이 무엇인지** 말하지 않는다 — 고객이 아무것도 고르지 않으면 어떤 엔진을 받나.
- **설정이 품질에 얼마나 영향을 주는지** 수치가 없다.
- **5,000개가 정말 다른 엔진인지 같은 엔진의 5,000개 설정인지** 구분되지 않는다.
- 고객이 **자기 설정이 나쁘다는 것을 어떻게 아는지**(자기 평가 경로)가 없다.

## References

- [[tech-bridge-exa-perfect-search-for-agents]] · [[will-bryk]] · [[exa]]
- ⭐ 같은 구조·반대 방향: [[which-bm25-problem]] · [[ir-evaluation-obsolescence]]
- 관련: [[search-latency-tiers]] · [[agentic-search]] · [[bm25]] · [[code-as-atypical-knowledge]] · [[agent-roi-measurement]]
