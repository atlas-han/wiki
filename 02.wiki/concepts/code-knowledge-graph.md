---
title: Code Knowledge Graph
type: concept
category: pattern
tags: [knowledge-graph, code-understanding, onboarding, developer-tooling]
related: [llm-wiki-pattern, tree-sitter-llm-hybrid, generator-evaluator-pattern, agent-harness-design]
first-seen: lum1104-understand-anything
sources: [lum1104-understand-anything, james-ai-explorer-understand-anything, tech-bridge-graft-code-knowledge-graph]
created: 2026-05-30
updated: 2026-09-15
---

# Code Knowledge Graph

코드베이스(또는 문서·지식 베이스)를 **노드와 엣지의 지식 그래프**로 변환해, 읽지 않고 *보면서* 이해하게 만드는 패턴. 파일·함수·클래스·의존성이 노드, import·call·상속·레이어 소속이 엣지. 목표는 "복잡함에 감탄하는 그래프"가 아니라 *"각 조각이 어떻게 맞물리는지 조용히 가르치는 그래프"*. [[lum1104-understand-anything|Understand-Anything]]에서 본 위키에 처음 등장.

## 해결하는 문제

> "새 팀에 합류했다. 코드베이스는 20만 줄. 어디서부터 봐야 하나?"

신규 합류자·PR 리뷰어·문서화 담당이 코드를 **선형으로 읽는(reading blind)** 대신, 아키텍처 레이어·의존성·비즈니스 흐름을 시각적으로 항해하게 한다.

## 구성 요소

1. **노드**: 파일·함수·클래스 단위. 각 노드는 평문(plain-English) 요약·태그·아키텍처 레이어·관계를 가짐.
2. **엣지**: import/export·call site·상속 등 구조적 관계 (+ 도메인 flow 같은 의미적 관계).
3. **레이어**: API / Service / Data / UI / Utility 등으로 자동 그룹핑, 색상 코딩.
4. **뷰**:
   - *Structural view* — 파일·함수·클래스 그래프
   - *Domain view* — 비즈니스 도메인·flow·step의 수평 그래프
   - *Knowledge view* — [[llm-wiki-pattern|wiki]]의 force-directed 그래프 + community clustering
5. **부가 기능**: guided tour(의존성 순 walkthrough), fuzzy/semantic search, diff impact 분석, persona-adaptive 상세도.

## 왜 작동하는가 (설계 원리)

- **[[tree-sitter-llm-hybrid|결정론 + 의미]] 분업**: 구조 엣지는 파서가 reproducible하게, 의도(요약·레이어·도메인)는 LLM이 — 둘 다 자기가 잘하는 일만.
- **그래프 = 커밋 가능한 JSON**: 한 번 만들면 artifact로 남아 팀 전체가 재사용 (파이프라인 스킵). [[llm-wiki-pattern]]의 *"누적되는 인공물"* 사상과 동형.
- **증분성**: fingerprint로 바뀐 파일만 재분석 → 그래프가 코드와 함께 살아 있음(docs-as-code, post-commit hook).

## 인접 패턴과의 관계

- **[[llm-wiki-pattern|LLM Wiki Pattern]]**: LLM Wiki가 *큐레이션된 raw → 마크다운 지식*이라면, Code Knowledge Graph는 *코드 → 그래프*. 둘 다 "LLM이 유지하는 누적 지식 인공물". Understand-Anything의 `/understand-knowledge`는 이 둘을 잇는 다리 — wiki를 입력으로 그래프를 출력.
- **[[generator-evaluator-pattern]] / [[agent-harness-design]]**: 그래프 생성은 멀티 에이전트 파이프라인(scanner/analyzer/reviewer)으로 구현 — `graph-reviewer`가 evaluator 역할(완전성·참조 무결성 검증).
- **RAG와의 차이**: RAG는 질의마다 chunk retrieve(누적 없음). Code Knowledge Graph는 구조화된 그래프를 *미리* 구축해 탐색·질의·온보딩에 재사용.

## 한계·열린 질문

- 그래프 정확도는 LLM 요약 품질에 의존 (의미적 측은 non-deterministic)
- 매우 큰 그래프(10MB+)는 git-lfs 필요 — 인공물 자체의 무게
- 그래프가 "가르치는가 vs. 압도하는가"는 UX·레이어링 설계에 좌우 (persona-adaptive UI가 대응책)

## 사용자 시각의 가치 제안

[[james-ai-explorer-understand-anything|한국어 블로그(2026-05-28)]] 는 같은 패턴을 *"새 프로젝트 코드 이해 1시간 → 5분"* 시간 절감 프레임으로 재서술한다. 그래프 자체의 형식적 우월성보다 **온보딩·레거시·diff 영향분석** 같은 *시나리오* 가 채택을 견인. IDE 기본 기능·Sourcegraph 와 대비해 *비즈니스 도메인 매핑·가이드 투어* 가 차별점으로 강조됨.


## 2026-09-15 — 사람이 보는 그래프에서 에이전트가 조회하는 인덱스로

[[tech-bridge-graft-code-knowledge-graph]]([[graft|Graft]])가 이 패턴의 **첫 코딩 에이전트용 런타임 구현**을 보여 준다. 같은 자료구조인데 **소비자가 바뀌었다.**

| | [[understand-anything]] (2026-05) | [[graft]] (2026-09) |
|---|---|---|
| 그래프를 **보는 쪽** | **사람** — 신규 합류자·리뷰어 | **에이전트** — 편집 전 위치 조회 |
| 노드의 값 | **평문 요약**(무엇을 하는가) | **위치**(어디에 있는가) — 평문 설명은 *선택이고 "꼭 필요하지 않다"* |
| 왜 만드나 | 코드베이스 **이해** | [[file-discovery-tax\|탐색 턴 제거]] |
| 성공 판정 | *"조용히 가르치는가"* | **턴 수·토큰·시간** |
| 신선도 | 대체로 다루지 않음 | **증분 갱신 + 조회 직전 검사** → [[incremental-index-freshness]] |

**에이전트가 소비자가 되면 설명이 덜 중요해지고 신선도가 훨씬 중요해진다** — 사람은 낡은 그래프를 보고도 알아차리지만 에이전트는 그 위에서 그냥 일한다.

같은 소스가 **벡터 검색과의 차이**를 코드 도메인에서 구체화한다 → [[reference-graph-vs-vector-search]]. 한계도 명시된다 — **코드만 매핑한다** → [[code-only-index-blind-spot]].

## References

- [[lum1104-understand-anything]] (1차, GitHub README)
- [[james-ai-explorer-understand-anything]] (2차, 한국어 블로그)
- [[understand-anything]] · [[tree-sitter-llm-hybrid]] · [[llm-wiki-pattern]]
