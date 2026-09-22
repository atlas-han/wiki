---
title: 검색 지연 티어 (Search Latency Tiers)
type: concept
category: architecture
tags: [retrieval, latency, voice-agents, real-time, product, agent-harness]
aliases: [200ms 검색, latency tiers, 지연 티어]
related: [voice-latency-thinking-tradeoff, agentic-search, per-customer-search-engine, retrieval-side-context-compression]
first-seen: tech-bridge-exa-perfect-search-for-agents
sources: [tech-bridge-exa-perfect-search-for-agents]
created: 2026-09-22
updated: 2026-09-22
---

# 검색 지연 티어

**같은 검색 제품이 두 개의 지연 등급을 동시에 판다 — 200밀리초와 "몇 분".** 그리고 빠른 쪽의 근거가 *사람이 아니라 기계가 쓴다* 는 것이다.

> **200밀리초 검색 엔드포인트**인데, 실제로도 그렇게 느껴집니다. **인간에게는 너무 빠르죠. 하지만 우리는 인간을 위해 봉사하는 것이 아닙니다. AI 시스템에 서비스를 제공하고 있습니다.** — [[will-bryk]], [[tech-bridge-exa-perfect-search-for-agents]] (11:08~11:19)

> **[음성 에이전트]와 대화하는 중에 내부적으로 검색을 수행해야 하는 경우 매 밀리초가 중요합니다.** (11:19~11:27)

반대쪽 티어:

> *"YC의 투자를 받은 AI 스타트업을 모두 찾아서 배치와 현재 상태를 알려줘."* (…) **시간이 좀 걸릴 겁니다. 몇 초가 아니라 몇 분이 걸릴 수도 있지만, 원하는 정보를 얻으실 수 있을 겁니다.** (10:39~11:05)

## ⭐ 09-19에 세운 질문에 부품 쪽 답이 왔다

[[venky-b|Venky B]]([[plivo|Plivo]], 09-19)의 [[voice-latency-thinking-tradeoff]]는 **실시간 제약이 thinking을 금지하므로 모델을 더 생각하게 만들 수 없고 주변을 고칠 수밖에 없다**고 말했다. 그때 이 위키가 세운 질문은:

> **이 기법은 몇 초를 쓰는가, 그 도메인은 몇 초를 허용하는가.**

**이 소스가 그 "주변"의 한 부품을 지연 예산의 항목으로 내놓는다** — 음성 루프 안의 검색은 **200ms**다.

| 층 | 09-19 [[plivo\|Plivo]] 쪽 | 이 소스 |
|---|---|---|
| 누가 말하나 | **에이전트를 만드는 쪽** | **부품을 파는 쪽** |
| 검색의 위치 | 예산을 먹는 항목 | **그 항목의 공급자** |
| 수치의 성격 | 도메인 제약(실측) | ⚠️ **벤더 자기 보고** |

⚠️ **여전히 실측이 아니다.** *"세계에서 가장 빠른"*(11:08)에 비교 대상이 없고, 200ms가 **p50인지 p99인지, 어떤 코퍼스·설정인지** 말하지 않는다.

## 지연이 검색의 *종류* 를 가른다

**두 티어는 같은 물건의 빠른 버전·느린 버전이 아니다.**

| | **200ms 티어** | **분 단위 티어** |
|---|---|---|
| 쿼리 | 단발 조회 | **복합 질의**(전수 조건·구조화 출력) |
| 호출자 | 루프 안의 에이전트 · 음성 | 조사 과제 |
| 답의 모양 | 문서·스니펫 | **목록·표** |
| 이 위키의 짝 | [[voice-latency-thinking-tradeoff]] | [[perfect-search-as-cost-problem]] |

⚠️ **소스는 무엇이 이 차이를 만드는지 말하지 않는다** — 다른 인덱스인지, 다른 파이프라인인지, 같은 엔진의 타임아웃 설정인지 알 수 없다. → [[per-customer-search-engine]]

## 미해결

- **200ms의 측정 조건** — 퍼센타일·코퍼스 크기·설정 전부 없음.
- **두 티어를 가르는 메커니즘.**
- **품질이 지연에 따라 어떻게 변하는지** — 곡선이 없다.
- 음성 에이전트의 **전체 지연 예산에서 검색이 차지하는 몫**은 이쪽에도 저쪽에도 없다.

## References

- [[tech-bridge-exa-perfect-search-for-agents]] · [[will-bryk]] · [[exa]]
- ⭐ 짝: [[voice-latency-thinking-tradeoff]] · [[venky-b]] · [[plivo]]
- 관련: [[agentic-search]] · [[per-customer-search-engine]] · [[retrieval-side-context-compression]] · [[perfect-search-as-cost-problem]]
