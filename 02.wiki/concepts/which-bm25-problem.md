---
title: "어떤 BM25를 말하는가 (Which BM25 Do You Mean?)"
type: concept
category: theory
tags: [benchmark, baseline, evaluation, methodology, bm25, reproducibility]
aliases: [기준선 최적화, unoptimized baseline, which BM25]
related: [bm25, browsecomp-plus, ir-evaluation-obsolescence, agentic-search, skill-evals, all-or-nothing-accuracy]
first-seen: tech-bridge-bm25-agentic-search
sources: [tech-bridge-bm25-agentic-search, tech-bridge-knowledge-agents-not-coding-agents, tech-bridge-exa-perfect-search-for-agents]
created: 2026-09-21
updated: 2026-09-22
---

# 어떤 BM25를 말하는가

**"BM25보다 우리가 낫다"는 주장은 그 BM25가 어떻게 설정됐는지를 말하지 않으면 아무 내용이 없다.** 구현·성능·매개변수가 갈리고, **그 차이가 벤치마크 전체의 정확도를 뒤집을 만큼 크다.**

> 저는 이게 마음에 드는데, **"어떤 BM25를 말씀하시는 건가요?"** 왜냐하면 **그것이 특정 벤치마크의 전반적인 정확도에 상당히 큰 영향을 미치기 때문**입니다. — [[jo-bergum]], [[tech-bridge-bm25-agentic-search]] (10:25~10:32)

## ⭐ 같은 날 두 화자가 독립적으로 같은 지적을 했다

**이 위키에서 서로 다른 회사의 두 발표자가 같은 무대에서 같은 방법론적 결함을 지목한 첫 사례**다.

| | [[jo-bergum\|Bergum]] ([[hornet\|Hornet]]) | [[benjamin-clavie\|Clavié]] ([[mixedbread\|Mixedbread]]) |
|---|---|---|
| 지적 | *"[BrowseComp-Plus]도 BM25를 기준선으로 쓰지만 **알고 보니 그 기준선은 형편없었습니다**"* (09:54~09:59) | *"BM25라는 게 하나만 있는 게 아니기 때문입니다. **그것들은 수백 개나 됩니다**"* (09:43~09:47) |
| 진단 | **매개변수가 긴 문서에 맞지 않았다** (10:15~10:23) | **사람들이 기준선을 최적화하지 않는다** (09:49~09:53) |
| 처방 | *"어떤 BM25를 말씀하시는 건가요?"* | *"**항상 기준선을 최적화해야 합니다.** 당신이 걸고 있는 것을 항상 최적화해야 합니다"* |
| 증거 | 최근 연구가 [BrowseComp-Plus] 논문의 매개변수를 반박 | 리더보드에 **BM25가 두 줄**로 올라 있다 — 최적화/비최적화 |

**둘 다 자기 제품을 파는 자리에서 이 말을 했고, 둘 다 이 지적이 자기에게 유리하지 않다.** [[hornet|Hornet]]은 BM25에 걸고 있으므로 *BM25가 원래 강한데 잘못 측정됐다*가 유리하고, [[mixedbread|Mixedbread]]는 BM25 위를 파므로 *BM25에는 천장이 있다*가 유리하다. **그런데 둘 다 "기준선을 제대로 맞춰라"라는 같은 중립적 방법론에 닿는다.**

## 왜 이것이 이 위키의 문제인가

이 위키는 **"X가 Y보다 낫다"** 형태의 주장을 많이 모아 왔고, 그 대부분이 **당사자 진술**이었다.

- [[reference-graph-vs-vector-search]] — *"대부분의 코딩 에이전트는 벡터 검색을 아예 쓰지 않습니다"* ([[graft]] 개발팀). **벡터 쪽 기준선이 어떻게 설정됐는지 없다.**
- [[self-harness]] — 자기 하니스가 고정 하니스를 이긴다. **고정 하니스가 얼마나 잘 짜였는지가 결과를 정한다.**
- [[slop-probes]] · [[generator-evaluator-pattern]] — 채점기의 설정이 결과를 정한다.

**이 페이지는 그 주장들 전부에 붙는 각주**다: **기준선이 약하면 개선폭은 기준선의 약함을 잰 것이다.**

## ⚠️ 그리고 이 페이지 자신에게도 적용된다

두 소스가 이 원칙을 말하면서 **정작 자기 수치의 조건을 제시하지 않는다.**

- [[hornet|Hornet]]의 처리량 비교는 상대가 **"익명화된 엔진"** 이고 설정이 없다 — 게다가 **Y축을 말하다 정정한다**(16:12~16:23).
- [[mixedbread|Mixedbread]]의 *"20% 적은 툴 호출"* · *"3.5포인트"* · *"오라클 갭 10→6"* 은 **측정 조건이 없다.**

→ **이 위키는 두 소스의 자사 수치를 인용하지 않고, 이 방법론적 지적만 개념으로 올린다.**


## 같은 문제가 제품 형태로 재발한다 (2026-09-22 추가)

이 페이지는 *"어떤 BM25를 말하는가"* 를 **방법론적 결함**으로 세웠다. 하루 뒤 [[exa|Exa]]가 **같은 가변성을 제품의 미덕으로** 내놓는다.

> **완벽한 검색이란 한 가지로 정의될 수 있는 것이 아닙니다. 사실 저희는 고객 5,000곳 각각에 [하나씩] 5,000개의 검색 엔진을 보유하고 있는 셈이죠.** — [[will-bryk]], [[tech-bridge-exa-perfect-search-for-agents]] (12:26~12:36)

→ **[[per-customer-search-engine]]**

| | 이 페이지 (09-21) | [[per-customer-search-engine]] (09-22) |
|---|---|---|
| 가변성의 위치 | **하이퍼파라미터** | **고객 설정 전체** |
| 어떻게 다뤄지나 | **결함** | **기능** |
| 귀결 | 벤치마크가 **틀린다** | ⚠️ 벤치마크가 **성립하지 않는다** |

⚠️ **그래서 같은 발표의 *"인간을 위해 만들어진 구글보다 낫다"*(13:14~13:18)는 원리적으로 검증할 수 없다** — 어떤 설정의 Exa가 나은지 말할 수 없기 때문이다. **이 페이지가 제기한 질문의 가장 강한 사례이고, 그것을 내놓은 쪽은 그것을 문제로 보지 않는다.**

## References

- [[tech-bridge-bm25-agentic-search]] · [[tech-bridge-knowledge-agents-not-coding-agents]] · [[tech-bridge-exa-perfect-search-for-agents]]
- 인물: [[jo-bergum]] · [[benjamin-clavie]]
- 개념: [[bm25]] · [[browsecomp-plus]] · [[ir-evaluation-obsolescence]] · [[agentic-search]]
- 각주가 붙는 곳: [[reference-graph-vs-vector-search]] · [[self-harness]] · [[skill-evals]] · [[generator-evaluator-pattern]]
