---
title: Exa
type: entity
category: org
tags: [retrieval, search-engine, embeddings, agent-infrastructure, marketplace, startup]
aliases: [Exa.ai, Metaphor, 엑사]
links:
  - https://exa.ai/
sources: [tech-bridge-exa-perfect-search-for-agents]
created: 2026-09-22
updated: 2026-09-22
---

# Exa

**AI 에이전트를 위한 검색 엔진.** [[will-bryk|Will Bryk]]이 2021년에 창업했고, **초기 사명은 Metaphor**였다.

> **Exa는 AI 에이전트를 위한 검색 엔진입니다. 저희는 AI를 위한 검색 엔진을 최초로 개발한 회사이고** — [[tech-bridge-exa-perfect-search-for-agents]] (00:57~01:03)

> ⚠️ **자막이 이 회사의 이름을 네 갈래로 깨뜨린다** — en-orig가 *Exxon*·*Exo*·*exon*·*XA* 로 오인식하고 ko가 따라간다. **제목·설명란·챕터만 Exa로 옳다.** 이 위키는 설명란을 따른다.

## 소스에서 확인되는 것

- **창업 2021년, 발표 시점에 5주년** — *"저희가 시작한 2021년"*(05:22) · *"어제가 바로 저희 5주년 기념일"*(06:16). **이 두 앵커가 촬영 연도를 2026년으로 확정한다.**
- **2022년 Metaphor 이름으로 첫 검색 엔진 공개**, **2주 뒤 [ChatGPT] 출시** (07:40~07:59).
- **API는 계획된 것이 아니라 요청에서 나왔다** — 트위터 DM 한 통, 그다음 룸메이트 (08:09~08:34). → [[tech-bridge-exa-perfect-search-for-agents]]
- **초기에 모금액의 절반을 GPU 클러스터에 썼다** — *"그 당시엔 정말 말도 안 되는 일이었죠"* (07:21~07:24).
- **임베딩에 건다** — 키워드는 간단한 쿼리까지이고 복잡한 쿼리는 신경망·임베딩이 필요하다는 입장 (06:29~06:43). *"층을 더 쌓아라"*·[[sutton-bitter-lesson|쓰디쓴 교훈]] (07:08~07:14).
- **두 개의 지연 티어** — 분 단위 복합 질의와 **200ms 엔드포인트** (10:39~11:19). → [[search-latency-tiers]]
- **토큰 추출** — 문서 10개에서 가장 중요한 100개 토큰만 (11:51~12:00). → [[retrieval-side-context-compression]]
- **비공개 데이터 마켓플레이스**를 최근 열었다 (13:37~14:05). → [[agent-data-marketplace]] ⚠️ **제품명은 미확정** — 자막이 *"exon"* 으로만 적고 설명란도 주지 않아 **이 위키는 이름을 만들지 않았다.**
- **고객 유형** — 코딩 에이전트([[cursor|Cursor]]), 시장 진출 에이전트(HubSpot), 금융 에이전트 (01:12~01:37).

## ⚠️ 자기 보고 수치뿐이고 정확도는 없다

| 주장 | 근거 |
|---|---|
| **5,000개 이상 기업 · 40만 명 이상 개발자** (01:08~01:10) | 자기 보고 |
| **"세계에서 가장 빠른 검색 API" · 200ms** (11:08~11:11) | 자기 보고, 비교 대상 없음 |
| **"인간을 위해 만들어진 구글보다 낫다"** (13:14~13:18) | ⚠️ **벤치마크 없음.** 발표 전체에 정확도 숫자가 **한 번도** 나오지 않는다 |
| **"AI를 위한 검색 엔진 최초"** (01:01~01:03) | 자기 보고 |

**자금·인원·가격·수익은 전무하다.**

⚠️ **고객마다 다른 엔진을 준다는 제품 구조가 검증을 원리적으로 어렵게 만든다** — *"고객 5,000곳 각각에 [하나씩] 5,000개의 검색 엔진"*(12:26~12:36). **어떤 설정의 Exa가 구글보다 나은지 말할 수 없다.** → [[per-customer-search-engine]]

## 이 위키의 다른 검색 벤더와

[[hornet|Hornet]]([[jo-bergum|Bergum]])과 **하루 차이로 들어왔고 반대 방향을 가리킨다** — Hornet은 [[bm25]]에, Exa는 임베딩에 건다. **둘 다 하이브리드가 필요하다고 한 줄씩 인정하고 아무도 설명하지 않는다.** 전체 대조는 [[tech-bridge-exa-perfect-search-for-agents]] 참조.

## References

- [[tech-bridge-exa-perfect-search-for-agents]] · [[will-bryk]] · [[tech-bridge]]
- 개념: [[search-as-recommendation-engine]] · [[perfect-search-as-cost-problem]] · [[agent-data-marketplace]] · [[per-customer-search-engine]] · [[retrieval-side-context-compression]] · [[search-latency-tiers]] · [[suppressed-query-demand]]
- 관련: [[agentic-search]] · [[bm25]] · [[hornet]] · [[cursor]] · [[retrieval-augmented-generation]]
