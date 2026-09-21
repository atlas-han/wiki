---
title: Mixedbread
type: entity
category: org
tags: [retrieval, multimodal-search, search-agent, startup]
aliases: [믹스드브레드, mixedbread.com]
links:
  - https://mixedbread.com
sources: [tech-bridge-knowledge-agents-not-coding-agents]
created: 2026-09-21
updated: 2026-09-21
---

# Mixedbread

검색(retrieval) 회사. [[benjamin-clavie|Benjamin Clavié]]가 소속이다.

## 소스에서 확인되는 제품 둘

| | 무엇인가 | 소스의 주장 |
|---|---|---|
| **멀티모달 검색 도구** | PDF를 **OCR 없이 비전으로** 읽어 표까지 검색에 넣는다 (13:17~13:38) | 정확도가 *"크게 뛴다"* |
| **검색 에이전트** | 메인 에이전트가 **문제를 쪼개고**, 서처들이 각자 조사해 **메모**를 올린다 (14:00~14:31) | **정확도 +3.5포인트**, [[oracle-gap\|오라클 갭]] **10→6포인트(약 40% 감소)** |

두 번째가 이 위키에 [[orchestrator-searcher-split]]을 세운다 — 그리고 그 설계의 근거로 소스가 드는 것은 벤치마크가 아니라 **로펌의 분업 구조**다.

## ⚠️ 수치는 전부 자기 보고다

- **측정 조건이 없다** — 벤치마크의 이름조차 자막에서 판독되지 않는다(*"[MQA]"*, [[hugging-face|Hugging Face]]·[Snowflake] 공동 공개 PDF 기반 기업용 과제라는 서술뿐). → [[tech-bridge-knowledge-agents-not-coding-agents]]
- **모델·턴 수 외에 설정이 없다** — *"벤치마크에서 10턴"*(13:53)만 나온다.
- **설명란이 자막보다 세게 적었다** — 설명란은 *"40% 이상"* 인데 자막은 *"약 40%"*(14:53)다. **이 위키는 자막을 따른다.**

## ✅ 그런데 자기 한계를 스스로 지목한다

> **왜 내 에이전트는 88.9를 받는데 인간은 99.4를 받죠? 10%를 그냥 테이블에 두고 오는 셈입니다. 그런데 저는 그걸 이해할 수 없습니다** — 그건 에이전트고, 벤치마크에서 10턴을 받습니다. **완전한 에이전틱 시스템이고, 자기 결과에 대해 생각할 기회를 얻는데도 성능을 놓치고 있는 겁니다.** (13:38~14:00)

이 문단이 제품 서사의 한가운데에서 **남은 격차를 먼저 말하고 들어간다.** 이 위키의 당사자 발표 중 드문 형태다.

## [[hornet|Hornet]]과 나란히

같은 날 같은 무대에서 두 검색 회사가 발표했고 **층이 다르다.**

| | [[hornet\|Hornet]] | **Mixedbread** |
|---|---|---|
| 판매 층 | **어휘 검색 엔진**(BM25 구현·top-K 가속) | **멀티모달 검색 + 오케스트레이션** |
| 진단 | 검색 **품질·비용**이 병목 | 검색 **조직**이 병목 |
| BM25 취급 | **건다**(핵심 프리미티브) | **천장**(아무리 최적화해도 인간도 못 넘는다) |
| 공통 | **BM25 기준선이 잘못 설정돼 있다** → [[which-bm25-problem]] | 〃 |

⚠️ **BM25에 대한 두 회사의 평가가 정반대로 읽히지만 실은 어긋나지 않는다.** Hornet은 *텍스트 웹 문서*에서 BM25가 강하다고 하고, Mixedbread는 *스캔된 PDF*에서 BM25가 천장에 부딪힌다고 한다 — **도메인이 다르다.** 두 소스 어느 쪽도 이 구분을 명시하지 않는다.

## 미해결

- **설립 시점·인원·자금·가격** 전부 없다.
- **모델을 직접 만드는가** — 말하지 않는다. *"[Gemini]와 [Mixedbread]의 검색 도구"*(13:27)라는 병렬이 나올 뿐이다.
- **[[benjamin-clavie|Clavié]]의 직함** 미확정.

## References

- [[tech-bridge-knowledge-agents-not-coding-agents]] · [[benjamin-clavie]]
- 개념: [[orchestrator-searcher-split]] · [[oracle-gap]] · [[retrieval-primitive-repertoire]] · [[which-bm25-problem]]
- 비교: [[hornet]]
