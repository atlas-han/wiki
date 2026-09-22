---
title: 완벽한 검색은 비용 문제다 (Perfect Search as a Cost Problem)
type: concept
category: principle
tags: [retrieval, search, cost, optimization, embeddings, thought-experiment]
aliases: [1천만 달러 사고 실험, perfect search, 완벽한 검색]
related: [true-cost-to-perfect-answer, fixed-budget-alpha, context-window-as-floppy-disk, retrieval-not-reasoning-bottleneck, bm25, sutton-bitter-lesson]
first-seen: tech-bridge-exa-perfect-search-for-agents
sources: [tech-bridge-exa-perfect-search-for-agents]
created: 2026-09-22
updated: 2026-09-22
---

# 완벽한 검색은 비용 문제다

**이상적인 해는 이미 알려져 있다 — 쿼리와 문서의 모든 쌍에 LLM을 돌리는 것. 문제는 그것이 검색 한 건에 1천만 달러라는 것이다. 따라서 검색 공학은 품질 문제가 아니라 그 비용을 10억~1조 배 줄이는 최적화 문제가 된다.**

> 저를 항상 움직이게 했던 **사고 실험**은, **복잡한 쿼리와 문서를 가져와서 [GPT-3]를 실행하고 "이것이 일치하는가?"라고 묻는 것**이었습니다. 그것은 아주 잘 답해줄 겁니다. **이제 모든 검색에 대해 1조 개 문서를 처리한다고 가정하면 완벽하거나 거의 완벽한 검색 엔진을 얻을 수 있습니다.** — [[will-bryk]], [[tech-bridge-exa-perfect-search-for-agents]] (05:50~06:03)

> **문제는 그렇게 하면 검색 한 건당 1천만 달러 정도가 든다는 겁니다. 그래서 이것은 정말 흥미로운 최적화 문제가 됩니다. 어떻게 그 비용을 10억 배, 1조 배 줄일 것인가?** (06:03~06:11)

## 제시된 해 — 임베딩은 사전 계산된 LLM이다

> **모든 쿼리에 대해 모든 문서에 신경망을 실행할 수는 없습니다. 하지만 모든 문서를 임베딩 같은 구조로 사전 처리할 수 있습니다.** 그러면 그것이 **신경망의 지능을 상당 부분 포착**합니다. (06:45~06:56)

**논리는 "임베딩이 더 좋다"가 아니라 "임베딩은 이상적 해의 값싼 근사"다.** 그래서 [[sutton-bitter-lesson|쓰디쓴 교훈]]이 곧바로 따라온다 — *"다른 말로 하면, 그냥 층을 더 쌓는다는 뜻이에요"*(07:08~07:10).

## 이 위키의 다른 비용 프레임과

**품질 문제를 비용 문제로 바꿔 정의한 세 번째 자리이고, 가장 극단적이다.**

| | 다루는 것 | 단위 |
|---|---|---|
| [[fixed-budget-alpha]] (09-18) | **이미 돌아가는 에이전트**의 전략 비교 | 고정 토큰 예산 |
| [[true-cost-to-perfect-answer]] (09-18) | 정답까지의 기대 지출 | 예산 × 기대 횟수 |
| **이 페이지** | **검색 공학 전체의 정의** | **이상적 해로부터의 거리(배수)** |

앞의 둘은 *얼마나 쓸 것인가*를 물었다. 이쪽은 **해가 먼저 정의되고, 공학이 전부 그 해를 향한 비용 절감**이 된다.

## ⚠️ 전제가 검증되지 않는다

사고 실험이 성립하려면 ***"쌍마다 LLM을 돌리면 거의 완벽하다"* 가 참이어야 하는데 소스는 그것을 주장만 한다.**

가장 가까운 독립 증거는 하루 전 [[jo-bergum|Bergum]]의 [[retrieval-not-reasoning-bottleneck]]이다 — *증거 문서를 컨텍스트에 인위적으로 채워 넣으면 정확도가 매우 높아진다.* ⚠️ **그러나 같은 주장이 아니다**: 그쪽은 *후보를 이미 찾아낸 뒤* 의 판정이고, 이쪽은 **1조 개 전부에 대한 판정**이다. **오탐이 0.01%만 나도 1억 건**이라는 문제를 소스는 다루지 않는다.

## ⚠️ [[context-window-as-floppy-disk]]와 정면으로 만난다

[[jo-bergum|Bergum]]은 *AGI가 와도 컨텍스트 창은 플로피 디스크 한 장(약 35만 토큰)이라 **무엇을 넣을지 골라야 한다*** 고 말한다 — **고르는 일은 사라지지 않는다.**

**이 사고 실험은 고르는 문제를 비용으로 환원해 지운다** — 충분히 싸지면 전부 판정하면 되므로 고를 필요가 없다는 것이다.

> ⚠️ **두 소스는 서로를 모르고, 이 위키는 어느 쪽도 채택하지 않는다.** 다만 **축이 다르다**는 점은 분명하다: Bergum은 *모델에 무엇을 **넣을** 것인가*, Bryk은 *무엇을 **후보로 판정**할 것인가*. **완벽한 검색이 후보를 1조 개에서 10개로 줄여 줘도 그 10개를 창에 넣는 문제는 남는다.**

## 미해결

- **비용을 실제로 얼마나 줄였는지** 말하지 않는다. 임베딩 사전 처리까지만 설명하고 *"다양한 시스템의 결합"*(10:16~10:19)으로 닫는다.
- **"거의 완벽"의 측정** — 이 발표에 정확도 수치가 **0개**다.
- **1천만 달러의 계산 근거**(문서 수 × 토큰 × 단가)가 제시되지 않는다.
- 사전 처리가 *"신경망의 지능을 상당 부분 포착"* 한다는 **"상당 부분"의 크기.**

## References

- [[tech-bridge-exa-perfect-search-for-agents]] · [[will-bryk]] · [[exa]]
- 비용 프레임: [[true-cost-to-perfect-answer]] · [[fixed-budget-alpha]] · [[verification-cost-asymmetry]]
- ⚠️ 긴장: [[context-window-as-floppy-disk]] · [[retrieval-not-reasoning-bottleneck]]
- 관련: [[sutton-bitter-lesson]] · [[bm25]] · [[agentic-search]] · [[retrieval-augmented-generation]]
