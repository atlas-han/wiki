---
title: 검색은 추천 엔진이다 (Search as a Recommendation Engine)
type: concept
category: principle
tags: [retrieval, search, objective-function, incentives, seo, advertising]
aliases: [추천 엔진으로서의 검색, search as recommendation]
related: [agentic-search, suppressed-query-demand, perfect-search-as-cost-problem, preference-reward-asymmetry, bm25, llm-as-search-user]
first-seen: tech-bridge-exa-perfect-search-for-agents
sources: [tech-bridge-exa-perfect-search-for-agents]
created: 2026-09-22
updated: 2026-09-22
---

# 검색은 추천 엔진이다

**웹 검색이 원하는 것을 정확히 주지 못하는 이유는 성능이 부족해서가 아니라, 애초에 그것을 하도록 만들어지지 않았기 때문이다.**

> **왜 [줄무늬 없는 셔츠를 치면 줄무늬 셔츠가 나올까요]? 세상의 정보를 담은 데이터베이스가 되어 원하는 것을 정확히 주려는 게 아니기 때문입니다. 그건 일종의 추천 엔진이에요.** — [[will-bryk]], [[tech-bridge-exa-perfect-search-for-agents]] (02:58~03:05)

> **그건 거의 소셜 미디어와 비슷한 면이 있어요. 일종의 추천 엔진과 같아요.** (03:39~03:42)

> 📌 **이 위키가 검색 엔진의 *목적함수* 를 문제 삼는 첫 페이지다.** [[bm25]]·[[agentic-search]]·[[retrieval-augmented-generation|RAG]]는 전부 ***어떻게* 검색하는가**였다. 여기서 묻는 것은 ***무엇을 최적화하도록 만들어졌는가***다.

## 두 가지 물건

| | **추천 엔진** | **세상의 정보를 담은 데이터베이스** |
|---|---|---|
| 답의 성격 | *괜찮아 보이는 것 몇 개* | **조건에 맞는 것 전부** |
| 부정 조건 | 약하게 처리 — *"줄무늬 없는"* 이 무시된다 | 필터로 성립 |
| 최적화 대상 | 참여·광고·SEO | **관련성** |
| 쓰는 쪽 | 사람 | **에이전트** |

> **AI 시스템은 정말 완벽한 검색을 원해요. SEO를 원하지 않습니다. 광고를 원하지 않아요. 그들은 마치 세상의 정보를 담은 데이터베이스 같은 것을 원합니다.** (09:46~10:00)

**소스가 드는 실패 예는 셋이고 전부 같은 모양이다** — 부정 조건(*줄무늬 없는 셔츠*), 전수 조건(*싱가포르에서 AI 검색을 연구하는 모든 사람*), 신뢰 조건(*모든 매체를 통틀어 가장 중요한 미국 뉴스*). **셋 다 "몇 개 추천"으로는 원리적으로 답할 수 없는 형태다.**

## ⭐ 결함이 아니라 목적함수의 귀결

**이 위키에서 같은 모양의 논증이 하루 전에 다른 분야에 적용됐다.** [[diogo-almeida|Almeida]]의 [[preference-reward-asymmetry]]는 *과대약속은 버그가 아니라 특징* 이라고 말한다 — 인간 선호를 최적화하면 불확실성을 표현하는 쪽만 일관되게 벌받기 때문이다.

| | [[preference-reward-asymmetry]] (09-20) | 이 페이지 (09-22) |
|---|---|---|
| 시스템 | [[rlhf\|RLHF]]로 학습한 모델 | 웹 검색 랭킹 |
| 최적화 대상 | 인간 선호 | 참여·광고 |
| 귀결 | **환각·과대약속** | **추천이지 답이 아님** |
| 처방 | 목적함수를 바꿔라 ([[post-training-northstars]]) | **다른 소비자를 위한 다른 엔진** |

⚠️ **두 소스는 서로를 모르고, 이 소스는 자기 주장을 형식화하지 않는다** — 광고 수익 구조가 랭킹을 어떻게 왜곡하는지에 대한 메커니즘도 증거도 제시되지 않는다. **"추천 엔진"은 비유로 제시되고 비유로 끝난다.**

## ⚠️ 이해관계

**경쟁 제품을 파는 사람이 하는 진단이다.** 진단 자체는 [[bm25]]([[jo-bergum|Bergum]])나 [[oracle-gap]]([[benjamin-clavie|Clavié]])처럼 이 위키의 다른 검색 소스와 충돌하지 않지만, **"그래서 우리가 답이다"까지는 근거가 따라오지 않는다** — [[exa|Exa]]의 정확도 수치는 **0개**다.

## References

- [[tech-bridge-exa-perfect-search-for-agents]] · [[will-bryk]] · [[exa]]
- 인접: [[suppressed-query-demand]] — **같은 관측의 다른 면**(도구가 나쁘면 사용자가 질문을 줄인다)
- 같은 모양의 논증: [[preference-reward-asymmetry]] · [[post-training-northstars]]
- 관련: [[agentic-search]] · [[llm-as-search-user]] · [[bm25]] · [[retrieval-augmented-generation]] · [[perfect-search-as-cost-problem]]
