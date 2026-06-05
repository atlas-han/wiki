---
title: "Karpathy — LLM Wiki (Gist)"
type: source
tags: [pattern, knowledge-base, llm-tooling]
source-url: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
source-type: article
author: Andrej Karpathy
date-published: 2026
ingested: 2026-05-25
created: 2026-05-25
updated: 2026-06-03
---

# Karpathy — LLM Wiki (Gist)

Andrej Karpathy가 2026년에 공개한 짧은 글로, LLM을 활용한 개인 지식 베이스 구축의 **패턴**을 제시한다. 단발성 RAG가 아니라, LLM이 점진적으로 위키를 **누적·유지**하게 하는 방식이 핵심이다.

## 핵심 takeaways

1. **누적 vs. 재발견**: 기존 RAG는 매 질의마다 raw 문서에서 답을 재발견. Karpathy의 제안은 LLM이 wiki라는 **persistent, compounding artifact**를 만들고 유지하는 것.
2. **3-레이어 아키텍처**: `raw/` (immutable 소스) → `wiki/` (LLM이 작성) → `CLAUDE.md` 등 스키마 (운영 규칙).
3. **3가지 주요 작업**: Ingest (소스 흡수), Query (질의 응답, 가치 있는 답은 위키로 환원), Lint (모순·고아·누락 점검).
4. **역할 분담**: 사람은 큐레이션·방향 설정·질문 제기. LLM은 읽기·요약·교차 참조·정리 등 **북키핑(bookkeeping)** 전담.
5. **Obsidian + LLM 워크플로**: Obsidian을 IDE, LLM을 프로그래머, wiki를 코드베이스로 비유.
6. **Memex 계보**: [[vannevar-bush|Vannevar Bush]]의 1945년 [[memex|Memex]] 비전 — 개인이 큐레이션한 연관 추적이 있는 지식 저장소 — 의 직계. Bush가 풀지 못한 "누가 유지보수하는가" 문제를 LLM이 해결.

## 인용

> The tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping... LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass. The wiki stays maintained because the cost of maintenance is near zero.

> Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase.

## 등장 개체·개념

- 개념: [[llm-wiki-pattern]] (이 글이 제시하는 패턴 자체)
- 인물: [[andrej-karpathy]]
- 도구: [[obsidian|Obsidian]], *qmd*, *Obsidian Web Clipper*, *Marp*, *Dataview* (Obsidian 외 stub)
- 역사: [[memex|Memex]] ([[vannevar-bush|Vannevar Bush]], 1945)

## 적용 예시 (글에서 직접 언급)

- 개인: 목표·건강·심리 추적
- 연구: 한 주제를 수 주~수 개월간 깊게 파기
- 책 읽기: 챕터별 정리 → fan wiki 형태
- 비즈니스: Slack·미팅 기록·고객 콜 기반 내부 위키
- 기타: 경쟁사 분석, 실사, 여행 계획, 강의 노트, 취미

## References

- [원문 Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
