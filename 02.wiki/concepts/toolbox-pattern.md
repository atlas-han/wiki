---
title: 툴박스 패턴 — 도구와 스킬도 검색해서 넣는다 (Toolbox Pattern)
type: concept
category: pattern
tags: [tools, skills, retrieval, vector-search, hnsw, context-engineering, progressive-disclosure]
aliases: [툴박스 패턴, 스킬박스 패턴, skillbox pattern, tool retrieval, 도구 검색]
related: [context-engineering, context-rot, agent-skills, agent-tool-design-practices, model-context-protocol, retrieval-augmented-generation, push-vs-pull-context-retrieval, build-time-vs-runtime-tools]
first-seen: tech-bridge-oracle-agent-memory-harness
sources: [tech-bridge-oracle-agent-memory-harness]
created: 2026-09-24
updated: 2026-09-24
---

# 툴박스 패턴 (Toolbox Pattern)

**사용 가능한 도구·스킬을 전부 컨텍스트에 싣지 않고 검색 가능한 저장소(벡터 인덱스)에 두었다가, 에이전트 루프의 매 반복마다 지금 필요한 것만 retrieve해 넣고 필요 없어지면 뺀다.** 스킬에 적용하면 *스킬박스 패턴*. [[ignacio-martinez|Ignacio Martinez]]([[oracle|Oracle]]), [[tech-bridge-oracle-agent-memory-harness]] — 화자에 따르면 *"[[andrew-ng|Andrew Ng]]과의 강좌에서 소개한"*(48:46~48:51) 개념이다(⚠️ 강좌명 미확인).

> 예를 들어, **툴박스 패턴과 스킬 박스 패턴** (…) 다음은 보관할 수 있는 방법입니다. 도구와 [스킬] 모델에서 사용할 수 있으므로 [최적으로 retrieve되도록]. 그리고 무엇 당신이 해야 할 일은 (…) **정말 필요한 것들을 넣고** (…) **컨텍스트 창은 다음과 같은 경우에만** (…) **필요한.** 각 반복에서 에이전트 주기에서 **이것이 맞는지 확인할 수 있습니다.** 정말 적절한 장소이고, 그렇지 않다면, 네, **간단히 빼내실 수 있습니다. 일시적으로.** (34:16~34:53)

> 핵심은 다음과 같습니다. **우리는 각각의 맥락을 구성할 것입니다. 에이전트 주기 반복**[루프의 매 반복마다 컨텍스트를 조립한다]. (35:05~35:08)

## 구성 요소 (Q&A에서)

**① 규모 — 인덱스로 추상화.** 청중 질문 *"조직에 도구가 수천 개면?"*(48:38~48:43):

> 최적화할 수 있도록 이러한 도구의 [retrieval이] **[무시할 만한 수준이 되도록].** 그러면 사용하게 될 것입니다 [**HNSW — Hierarchical Navigable Small World**] 인덱스 (…) **그래프의 각 노드는 (…) 벡터 인덱스 또는 저장소** (…) **이러한 유형의 문제에 대해서만 파일이 아니라 데이터베이스에 있습니다.** (48:54~49:21)

> 파일을 읽는 것과 더 비슷해요. 파일을 작성하고, **grep**을 실행하고 (…) 우리가 매일 하는 일은 대개 **100 또는 1,000을 초과[하지 않습니다]**. (…) 벡터 [스토어]에 있기 위해, **당신은 복잡성과 양을 추상화합니다.** (…) **2,000[개]을 쉽게 10,000[개]가** (49:37~50:07)

⚠️ *2,000개든 1만 개든 똑같이 간단하다*는 **검색 지연** 이야기이고, **검색 정확도(맞는 도구가 top-k에 드는가)** 는 말하지 않는다. 측정도 없다.

**② 분리도 — 설명을 LLM으로 보강.** 청중 질문 *"두 회사의 도구 설명이 아주 비슷하면?"*(50:45~50:51):

> **LLM으로 강화된 설명** (…) **해당 도구들의 분리 가능성**[을 높이기 위해]. (…) [설명이 충분치 않다면] (…) 예를 들어 실행하려면 **명명된 개체의 인식[NER] 이는 매우 원시적인 방법입니다.** (…) **"docstring"의 표현** (…) **검색 수행 시 분리 가능성** (50:57~51:34)

→ 도구 선택을 **검색 문제**로 보면, 도구 설명의 품질은 곧 **임베딩 공간에서의 분리도**다. 이 위키의 [[agent-tool-design-practices]]가 도구 설명을 *모델에게 주는 안내*(규칙 2)로 봤다면, 여기서는 **검색기가 읽는 문서**이기도 하다.

**③ 데모에서의 가시화** — 앱의 컨텍스트 창 시각화가 *"에이전트가 사용하는 도구 컨텍스트에 로드하도록 선택됨"*(47:01~47:03)과 로딩된 스킬(47:16~47:18)을 보여 준다.

## 이 위키에서의 자리

| 소스 | 무엇을 필요할 때만 넣나 | 누가 고르나 |
|---|---|---|
| [[agent-skills]] progressive disclosure | 스킬 본문(설명만 먼저) | 모델이 설명을 보고 |
| [[push-vs-pull-context-retrieval]] | 코드 지식 | push(하네스) / pull(모델) |
| **툴박스 (이 페이지)** | **도구 정의 자체 + 스킬** | **검색기(벡터 인덱스)가 매 반복** |

⭐ 차이는 **스킬의 "설명"조차 컨텍스트에 상주하지 않는다**는 것 — progressive disclosure는 설명 목록을 늘 싣고 본문만 미루지만, 툴박스는 **목록 자체를 검색**한다. 도구가 수천 개일 때 설명 목록만으로도 창이 차는 문제([[context-rot]])에 대한 답이다.

[[agent-tool-design-practices]]의 실패 모드 표에서 *"도구가 너무 많다 → 선택 과부하"* 는 **도구를 줄이라**는 설계 쪽 처방이었다. 툴박스는 **줄이지 않고 숨긴다** — 두 처방은 층이 다르다(설계 시점 vs 실행 시점).

⚠️ **긴장 — [[file-system-agent]].** Vercel은 *"구체적인 도구 세트를 주지 않고 탐색하게 둔 것"* 으로 eval이 두 배가 됐다고 했다(list·read·bash 최소 도구). 툴박스는 **도구를 많이 두고 고르게** 하는 쪽이다. 화자도 일상 도구는 *파일 읽기·쓰기·grep* 이라고 인정한다(49:37~49:43) — **수천 개 도구가 필요한 환경이 얼마나 흔한지는 두 소스 모두 보여 주지 않는다.**

## ⚠️ 미해결

- **검색이 틀리면** — 필요한 도구가 top-k에 안 들면 에이전트는 **그 도구가 있는 줄 모른다**([[agent-umwelt]]의 *렌즈 밖은 존재하지 않는다*). 재검색·폴백 경로가 없다.
- **매 반복 재조립의 비용** — 프롬프트 캐시가 깨지는지.
- **보안** — 검색된 도구가 **권한이 있는 도구인지**의 필터(50:22~50:26 *"일부는 기밀 데이터에 접근 권한이 있다"* 는 질문이 들리지 않아 연결 불가).
- Andrew Ng 강좌에서의 **원래 정의**.

## References

- [[tech-bridge-oracle-agent-memory-harness]] · [[ignacio-martinez]] · [[andrew-ng]]
- [[agent-skills]] · [[agent-tool-design-practices]] · [[push-vs-pull-context-retrieval]] · [[context-engineering]] · [[context-rot]] · [[file-system-agent]] · [[model-context-protocol]] · [[retrieval-augmented-generation]] · [[agent-umwelt]]
