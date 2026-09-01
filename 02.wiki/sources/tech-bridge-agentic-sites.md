---
title: "Tech Bridge — 에이전틱 사이트: 초개인화 웹사이트 구축 (Carlos Sanchez)"
type: source
tags: [agentic-sites, personalization, rag, inference-latency, adobe, cerebras, video]
source-url: https://www.youtube.com/watch?v=PXHUHNX7nbI
source-type: video
author: Tech Bridge (한영자막 재배포) · 발표자 Carlos Sanchez (Adobe)
date-published: 2026-08-31
ingested: 2026-09-01
created: 2026-09-01
updated: 2026-09-01
---

# Tech Bridge — 에이전틱 사이트: 초개인화 웹사이트 구축

[[tech-bridge|Tech Bridge]]가 한영자막을 입힌 20:13 컨퍼런스 강연. 발표자 [[carlos-sanchez|Carlos Sanchez]]는 [[adobe|Adobe]] Experience Manager 수석 과학자. 한 줄 테제:

> 사이트 **전체**를 다시 생성하지 말고, 사이트 **전체를 코퍼스로** 써서 **블록 몇 개만** 1초 안에 다시 조립하라.

본문은 ko 자막을 채널 공식 15개 챕터 순서로 재구성했고 수치는 en-orig로 교차 확인했다. ASR 보정: "AMX delivery" → AEM Edge Delivery, "랙" → RAG, "세레브라(스)" → [[cerebras|Cerebras]], "Prompt Foo/Full" → promptfoo. 16:33의 "Off One Labs"는 두 자막 모두 불분명해 원 표기를 기록하지 않는다.

이 위키에서 **[[agentic-sites]] 개념의 첫 소스**이자, 지금까지 코딩 에이전트에 쏠려 있던 축([[agent-org-adoption]]·[[frontier-engineering]])에 **소비자 대면 생성 UI**를 처음 추가하는 소스다.

## 문제 정의: 의도를 읽는 사이트 (00:00–02:07)

에이전틱 사이트는 방문자의 **의도**를 파악해 페이지를 실시간 개인화한다. 목표는 마케팅의 참여도·전환율.

스택은 **AEM Edge Delivery**(콘텐츠가 엣지에 있는 제품 계층) + 여러 LLM 제공업체를 부르는 백엔드. 빠른 추론에 [[cerebras|Cerebras]], 그 외 Bedrock 등도 시험.

## 블록 단위 개인화 + 자기 사이트 RAG (02:07–04:24)

핵심 설계 결정 두 가지가 붙어 있다.

1. **개인화 단위는 페이지가 아니라 블록** — 히어로 카드, 제품 목록, 블로그 피드, 내비게이션, CTA
2. **그라운딩 코퍼스는 자기 사이트 전체** — 생성물이 기존 사이트에 근거한다

> 사이트 전체를 새로 생성하는 것을 원하지 않습니다. 마케팅 담당자들과 이야기를 나눠보면, 그들은 매우 엄격한 브랜드 가이드라인을 가지고 있습니다.

브랜드 가이드라인이 곧 환각 예산이라는 뜻 — 이 위키의 [[verifiable-goals]]가 코드에서 verifier를 요구하는 것과 같은 자리에, 여기서는 **기존 사이트 코퍼스가 제약**으로 들어간다.

## 사이트마다 다른 모델 평가 (04:24–06:45)

백엔드는 모델·제공업체를 계속 평가한다. **결과가 사이트마다 크게 다르다**는 것이 현장 발견 — 사이트 규모, 타겟 고객층, 상거래 유형에 좌우된다. 그래서 평가는 일회성이 아니라 **지속 실행**이고, 도구는 **promptfoo**(여러 제공업체·로컬 모델·OpenAI 호환 엔드포인트 대상).

평가 축은 둘뿐이다.

| 축 | 기준 |
|---|---|
| 정확성 | 통상적으로 가장 중시되는 것 |
| **속도** | 사이트 생성 **1~2초 이내** |

속도가 정확성과 나란히 1급 지표로 올라온 것이 이 소스의 특징이다. 근거는 사이트 속도 ↔ 전환율·UX의 기존 입증.

## 지연 시간이 아키텍처를 결정한다 (06:45–09:03)

예시 사이트 프롬프트 15개 기준:

> with Cerebras on the Gemma 4 model that was announced last last week, we can get an average latency of 1.1 seconds generating a page. You can compare that to the second one, which is 4.6 seconds, right? So, the difference is huge.

| 구성 | 페이지 생성 평균 지연 |
|---|---|
| Cerebras + [[gemma-4|Gemma 4]] | **1.1초** |
| 2위 구성 | 4.6초 |

그리고 이 강연의 가장 이식성 높은 주장:

> 이런 종류의 작업을 하는 데에는 거대한 LLM이 필요하지 않습니다.

이유는 작업의 성격이다 — 텍스트를 만들고 **어떤 블록을 어디에 놓을지 고르는 일**이라 많은 정보가 필요 없다. 즉 **블록 선택으로 문제를 축소했기 때문에 작은 모델로 충분해졌다.** 모델을 키워 문제를 푸는 대신 문제를 작게 정의한 쪽이다.

> ⚠️ 하단의 다른 구성들은 "완벽할 필요는 없고 충분히 빠르면 충분"하다는 판단 대상으로 제시됐다. 즉 정확도-속도 트레이드오프를 **사용 사례별로** 자른다.

## 비용은 사전 생성 쪽으로 옮겨간다 (09:03–12:31)

브라우징 신호(탐색 카테고리, 방문 페이지, 페이지별 체류 시간)가 기록되어 LLM 입력이 된다.

추천 페이지는 사용자가 돌아다니는 동안 **미리 생성**해 둘 수 있다 — 이 경로에서는 1초 제약이 풀린다. 대신 **여러 번의 LLM 호출 비용**이 새 제약으로 들어온다. 지연 예산과 비용 예산이 경로별로 갈리는 구조.

마케터의 자리는 **자연어로 페르소나·그룹을 정의**하는 것이고(이 사람은 사려는가 알아보려는가), AI가 그 그룹에 맞는 블록과 제안을 고른다. 조정 축은 블록 종류·순서·미디어.

런타임 구성: 브라우저 신호 수집 → 백엔드(일부 Google, 일부 [[cloudflare|Cloudflare]])가 사이트 RAG로 LLM 호출 → 엣지 서버가 페이지·정적 콘텐츠 제공. 벡터 DB와 Experience Manager가 받친다.

## Audience of One (12:31–17:16)

> 마케팅 담당자들은 항상 각 개인에게 맞춤형 서비스를 제공하는 것을 꿈꾸기 때문입니다. 그래서 저희는 그걸 '관객 한 명'이라고 부릅니다.

라이브 데모(커피 머신 사이트)에서 디버그 패널이 수집 신호를 그대로 보여주고, "캠핑 중에 커피를 준비할 커피 머신" 검색에 맞춰 카피와 추천 제품이 그 자리에서 생성된다.

디버그 수치는 LLM 왕복 **1초**, **2,200–2,300 tok/s** (Cerebras Gemma 4).

> ⚠️ 같은 화면의 "Total time 164 seconds"는 ko·en-orig 자막이 일치하지만 위 수치와 모순된다. 판독 단위가 불명확하므로 **페이지 생성 시간으로 인용하지 않는다.** 신뢰 가능한 것은 promptfoo 평균 1.1초와 LLM 시간 1초.

도입 비용에 대한 주장:

> we built this tool that generates an agentic site for any site we want. ... enter the URL. In less than an hour, you have an agentic site.

AI 엔지니어링 컨퍼런스 사이트로 시연했을 때, "유럽 AI 컨퍼런스" 질의에는 유럽 중심 페이지가, 두 컨퍼런스 비교 요구에는 나란히 비교하는 페이지가 생성됐다 — **질의 유형이 페이지 레이아웃을 고르는** 사례.

## 웹의 다음 형태 (17:16–20:13)

생성형 사이트가 청중 한 명을 상대할 수 있다면 그것이 웹의 미래일 수 있다는 관측. 개인 비서에게 말하고 거실 화면에서 맞춤 답을 받는 그림 — 전화도 컴퓨터도 필요 없고 목소리와 표시 장치면 된다는 것.

> 이제 이것이 가능하다는 것입니다. 앞으로는 점점 더 좋아질 거예요. 가격은 앞으로 더 저렴해질 겁니다. 속도는 앞으로 더 빨라질 겁니다.

## 이 위키와의 연결

- [[agentic-sites]] — 이 소스로 신설. 블록 단위 + 자기 사이트 RAG + 초 단위 예산의 3축
- **작은 모델 + 좁은 작업**: [[frontier-engineering]]·[[agent-org-adoption]]이 *조직* 레버리지를 다뤘다면 여기서는 *작업 정의*를 좁혀 모델 요구를 낮춘다. [[sutton-bitter-lesson]]의 "스케일이 이긴다"와 정면으로 대비되는 제품 측 반례로 읽을 수 있다 — 단, 대상 작업이 생성이 아니라 **선택**이라는 단서가 붙는다
- **평가가 상수**: promptfoo로 사이트별 평가를 계속 돌리는 것은 [[verifiable-goals]]의 verifier를 제품 운영에 상주시킨 형태
- ⚠️ 벤더(Adobe) 자사 제품 데모라 정확도 수치·"1시간" 도입 주장에 독립 검증은 없다

## References

- 원본: <https://www.youtube.com/watch?v=PXHUHNX7nbI> ([[tech-bridge]] 재배포, 20:13, 2026-08-31)
- raw: `01.raw/articles/2026-08-31_에이전틱 사이트 초개인화 웹사이트를 구축하는 방법.md`
- 발표자: [[carlos-sanchez]] — <https://csanchez.org/> · <https://x.com/csanchez> · <https://www.linkedin.com/in/carlossg/>
- 관련: [[agentic-sites]] · [[adobe]] · [[cerebras]] · [[gemma-4]] · [[cloudflare]] · [[verifiable-goals]] · [[sutton-bitter-lesson]]
