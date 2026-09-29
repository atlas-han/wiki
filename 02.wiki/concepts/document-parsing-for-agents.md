---
title: 에이전트를 위한 문서 파싱 (Document Parsing for Agents)
type: concept
category: technique
tags: [document-parsing, ocr, vlm, pdf, pareto, benchmark, latency, cost]
aliases: [document OCR, 문서 OCR, 문서 파싱, PDF 파싱, ParseBench]
related: [document-context-layer, tiered-document-parsing, search-latency-tiers, retrieval-augmented-generation, perfect-search-as-cost-problem, mixedbread]
first-seen: tech-bridge-llamaindex-document-context-layer
sources: [tech-bridge-llamaindex-document-context-layer]
created: 2026-09-29
updated: 2026-09-29
---

# 에이전트를 위한 문서 파싱

**PDF·Word·PPT를 에이전트가 해석할 수 있는 정확하고 토큰 효율적인 표현(마크다운·메타데이터)으로 바꾸는 일.** 에이전트가 원본 바이너리를 직접 읽을 수 없기 때문에 존재한다. 이 위키에는 [[jerry-liu|Jerry Liu]]([[llamaindex|LlamaIndex]])의 [[tech-bridge-llamaindex-document-context-layer]]로 처음 들어왔다 — **당사자 서술**이다.

> *"document understanding is definitely not 100% solved"* (14:39~14:41)

## 왜 어려운가 (08:27~10:40)

| 포맷 | 문제 | en-orig |
|---|---|---|
| **PDF** | 기계 소비가 아니라 **표시·인쇄용** | *"it's rendered for kind of like display purposes"*(08:48~08:49) · *"they're designed for printing"*(08:57~08:58) |
| | 텍스트 = **좌표 붙은 글리프** | *"individual glyphs with coordinates"*(09:00~09:03) |
| | 표 = **선분 + 셀 위치에 그린 텍스트** | *"tables are not represented as tables"*(09:03~09:05) |
| | 다단 레이아웃의 **읽기 순서 보장 없음** | 09:37~09:50 |
| **Word·PPT** | 구조는 더 있지만 *"custom bespoke XML format"* 에 *"a ton of like fluff"* — 태그를 무시하고 렌더링 구조를 봐야 | 09:59~10:29 |

## 세 접근 (10:41~13:00)

| 접근 | 장점 | 약점 (화자) |
|---|---|---|
| 휴리스틱·파이프라인 (PyPDF·PyMuPDF 등) | 파일 구조를 직접 다룬다 | 수작업 규칙 |
| **원샷 VLM** | 시각 구조를 읽는다 | *"It can hallucinate on text only pages. It costs a ton of money."*(11:34~11:36), 시맨틱·grounding 부족(11:38~11:41) |
| **하이브리드** | 컨테이너·바이너리 이해 + 비전 | — *"at the Pareto frontier of cost and accuracy"*(11:56~11:59, 당사자) |

화자의 더 강한 주장: 문서 OCR의 Pareto 프런티어는 프런티어 모델보다 *"will always be like much more accurate and cheap"*(12:06~12:11) — 좁은 데이터 유형이라 Gemini·GPT·Opus의 시각 능력을 **맞춤 워크플로로 증류**할 수 있기 때문(12:15~12:28). ⚠️ 측정 없음.

> ⚠️ **Contradiction:** [[mixedbread|Mixedbread]]([[tech-bridge-knowledge-agents-not-coding-agents]])는 PDF를 **OCR 없이 비전으로** 읽어 검색 정확도가 *"크게 뛴다"* 고 한다. Liu는 원샷 VLM의 환각·비용·grounding 부족을 든다. 둘 다 당사자이고, Mixedbread는 **검색용 표현**, Liu는 **파싱 출력**을 말한다 — 같은 질문에 대한 답인지부터 불확실하다.

## 평가 — ParseBench (13:31~14:50)

- *"2,000 human verified pages"* — 표·차트·내용 충실도·시맨틱 서식(13:39~13:46)
- ⭐ 기준은 **구문적 정확성이 아니라 에이전트가 이해하는가** — *"instead of like syntactic correctness"*(13:47~13:53). [[ir-evaluation-obsolescence]]가 검색에서 *nDCG → 작업 성공*으로 옮긴 것과 같은 방향의 이동이 **파싱 평가**에서 일어난 것.
- 약 50개 프런티어·오픈 웨이트 모델·전문 OCR 솔루션, 목표는 곡선의 *"left and up"* = 높은 정확도 + 낮은 비용(14:04~14:17)
- ⚠️ 결과 수치는 자막에 없다(화면 그래프). 제작자 = 판매자.

## 세 처리 영역 — 정확도·비용·지연 (14:54~16:44)

| 영역 | 요구 | 해법의 방향 |
|---|---|---|
| **고정확도** | 보험·금융, *"99 to almost 100%"* — 오추출이 재무 모델 붕괴·사기 플래그로 | 페이지당 더 내고 **deeper agentic reasoning** |
| **저비용** | 하루 백만+ 문서 인덱싱(RAG 지식 베이스) | 확장 가능한 오프라인 인덱싱, **조금 틀려도 된다 — 에이전트가 다시 들어간다** |
| **초저지연** | 천 개 문서를 1분 안에(실시간 업로드) | VLM은 *"really tough for basically every single OCR service … that includes ours"* → **VLM 없는 파서 + 필요시 VLM** → [[tiered-document-parsing]] |

이 표는 [[search-latency-tiers]](검색 200ms/분 단위)와 [[perfect-search-as-cost-problem]](완벽함은 비용 문제)의 **파싱 쪽 짝**이다 — 한 제품이 한 점이 아니라 **곡선 위 여러 점**을 팔아야 한다는 결론까지 같다(14:20~14:31).

## 미해결

- ParseBench 결과·측정 조건 전부.
- 하이브리드의 **라우팅 기준**(어떤 페이지가 프런티어 모델로 가는가) — *"auto routing"*(12:41~12:47)이라는 말뿐.
- 스캔 이미지·필기·수식 등 **어떤 문서에서 실패하는가**는 나오지 않는다.

## References

- [[tech-bridge-llamaindex-document-context-layer]] · [[llamaindex]] · [[jerry-liu]]
- [[document-context-layer]] · [[tiered-document-parsing]] · [[mixedbread]] · [[search-latency-tiers]]
