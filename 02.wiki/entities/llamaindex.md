---
title: LlamaIndex
type: entity
category: org
tags: [rag, document-parsing, ocr, benchmark, open-source, startup]
aliases: [라마인덱스, LlamaParse, Light Parse, LightParse, ParseBench]
links:
  - https://parsebench.ai
sources: [tech-bridge-llamaindex-document-context-layer]
created: 2026-09-29
updated: 2026-09-29
---

# LlamaIndex

**RAG 프레임워크로 알려졌고, 지금은 스스로를 "에이전트용 문서 인프라"로 규정하는 회사.** 공동창업자·CEO [[jerry-liu|Jerry Liu]]의 [[tech-bridge-llamaindex-document-context-layer]]로 이 위키에 처음 들어왔다.

> *"You might have seen us as a RAG framework. We started in 2023, got pretty popular, and kind of created a lot of techniques around like advanced RAG … Today, we're basically the main document infrastructure for AI agents."* (00:55~01:07)

> ⚠️ **회사명은 자막에서 한 번도 발화되지 않는다**(00:01에서 누락). 제목·설명란·해시태그(`#LlamaIndex` `#LlamaParse`)와 자막 속 제품명 *"Llama Parse"* 로 연결했다. *"We started in 2023"* 은 화자 발화 그대로이고 외부 확인하지 않았다. 설립·규모·자금·가격은 소스에 없다.

## 소스에서 확인되는 제품 셋

| | 무엇인가 | 소스의 주장 (전부 당사자) |
|---|---|---|
| **LlamaParse** (상용) | 문서 파싱·추출 서비스. ① PDF 엔진 + Word·PPT 최적화 ② *"an agentic harness that's like carefully tuned for auto routing between cheaper specialized models to frontier models"*(12:41~12:47) ③ 표·차트 등 요소별 **파인튜닝된 파라미터 효율적 문서 VLM**(12:48~12:57). 추출은 *"granular citations all the way back to the source document"* + **신뢰도 점수**(19:28~19:36) | 하이브리드가 *"at the Pareto frontier of cost and accuracy"*(11:56~11:59) |
| **"Light Parse"** (오픈소스) | **Rust 기반**, VLM 없는 마크다운 파서. *"one-click installable skill"*(17:59~18:01)로 에이전트에 장착 | *"the fastest open source parser out there"*(17:02~17:04), *"the most accurate like Markdown parser out there that doesn't use a VLN[=VLM]"*(17:10~17:16), 라이선스는 *"I think it's like MIT or Apache"*(17:07) |
| **ParseBench** (벤치마크) | *"2,000 human verified pages"* — 표·차트·내용 충실도·시맨틱 서식, **구문적 정확성이 아니라 에이전트의 이해** 기준(13:39~13:53). parsebench.ai · Hugging Face · Kaggle 공개. 약 50개 프런티어·오픈 웨이트 모델·OCR 솔루션 비교(14:04~14:08) | *"the most comprehensive enterprise document benchmark"*(13:37~13:39) |

⚠️ **"Light Parse" 철자 미확정** — en-orig *"Light Parse"*, 설명란 *"LightParse"*, ko는 *"Light라는 도구 … 구문 분석"* 으로 쪼갰다. 이 위키는 공식 이름·저장소를 확인하지 않았다.

⚠️ **벤치마크 제작자 = 판매자.** ParseBench 결과(순위·수치·LlamaParse의 위치)는 자막에 없고 화면의 그래프에만 있다. 자사 파서가 VLM 처리 속도에서 *"that includes ours, too"*(16:27~16:28)라며 한계를 인정한 문장이 한 곳 있다.

## 이 위키에서의 자리

- [[mixedbread|Mixedbread]]와 **PDF를 어떻게 읽느냐**에서 갈린다 — Mixedbread는 OCR 없이 비전, LlamaIndex는 원샷 VLM의 환각·비용·grounding 부족을 들어 하이브리드. → [[document-parsing-for-agents]]
- [[exa|Exa]]·[[hornet|Hornet]]·Mixedbread가 **검색 엔진** 층을 판다면, LlamaIndex는 그 앞단의 **파싱·추출** 층을 판다. → [[document-context-layer]]

## References

- [[tech-bridge-llamaindex-document-context-layer]] · [[jerry-liu]]
- 개념: [[document-context-layer]] · [[document-parsing-for-agents]] · [[tiered-document-parsing]] · [[retrieval-augmented-generation]]
