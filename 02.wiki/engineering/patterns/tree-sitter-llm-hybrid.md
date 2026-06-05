---
title: Tree-sitter + LLM Hybrid Analysis
type: engineering
category: pattern
tags: [static-analysis, llm, parser, hybrid, code-understanding]
related: [code-knowledge-graph, brain-hands-decoupling]
first-seen: lum1104-understand-anything
sources: [lum1104-understand-anything, james-ai-explorer-understand-anything]
created: 2026-05-30
updated: 2026-06-01
---

# Tree-sitter + LLM Hybrid Analysis

코드 분석에서 **결정론적 정적 분석과 LLM을 각자 잘하는 일로 분업**하는 패턴. [[tree-sitter|Tree-sitter]]가 구조적 사실을, LLM이 의미적 해석을 담당한다. [[lum1104-understand-anything|Understand-Anything]]의 핵심 엔진. *"Static analysis and LLMs do what each does best."*

## 분업 구조

| 측면 | 담당 | 산출물 | 성질 |
|------|------|--------|------|
| **구조 (structural)** | [[tree-sitter|Tree-sitter]] | import/export, 함수·클래스 정의, call site, 상속 | **결정론적** — same input → same output |
| **의미 (semantic)** | LLM | 평문 요약, 태그, 아키텍처 레이어 배정, 비즈니스 도메인 매핑, guided tour, language concept callout | **non-deterministic** — 의도를 포착 |

- 스캔 단계에서 Tree-sitter가 import를 `importMap`으로 **pre-resolve** → 다운스트림 file-analyzer가 소스에서 import를 재유도하지 않음 (LLM 토큰·오류 절약)
- LLM은 *파싱된 구조 + 원본 소스*를 함께 읽어, 파서가 못 내는 "이 파일은 *무엇을 위한* 것인가"를 생산

## 왜 이렇게 나누는가

1. **Reproducibility**: 구조 엣지(그래프의 뼈대)가 매 실행 동일 → [[code-knowledge-graph|지식 그래프]]가 안정적. LLM 호출만으로 그래프를 만들면 매번 흔들림.
2. **증분 업데이트**: Tree-sitter fingerprint로 바뀐 파일만 감지 → 전체 재분석 회피.
3. **비용·정확도**: 구문 파싱은 파서가 빠르고 정확·무료. LLM은 비싸고 흔들리므로 *판단이 필요한 부분에만* 투입.

## 사상적 위치

[[brain-hands-decoupling|brain–hands decoupling]]의 변주로 읽을 수 있다 — "기계적으로 정확해야 하는 일(hands/parser)"과 "맥락 판단이 필요한 일(brain/LLM)"을 좁은 인터페이스(`importMap`, 파싱된 구조)로 분리. [[sutton-bitter-lesson|Bitter Lesson]]과는 긴장 관계: 순수 LLM이 아니라 구조 추출을 파서에 위임하는 *하이브리드*이므로, "general method가 이긴다"는 명제에 대한 실용적 절충(현재 비용·신뢰성 제약에서의 엔지니어링 답).

## 일반화

이 패턴은 코드에 국한되지 않는다 — 결정론적 파서(마크다운 wikilink 파서, AST, 정규 스키마)로 *뼈대*를 뽑고 LLM으로 *살*을 붙이는 모든 곳에 적용. Understand-Anything의 `/understand-knowledge`도 `index.md` wikilink를 결정론적으로 파싱한 뒤 LLM이 암묵 관계를 발굴하는 동일 구조. → [[llm-wiki-pattern]].

## 2차 검증 (전달 가능성)

[[james-ai-explorer-understand-anything|한국어 블로그(James AI Explorer, 2026-05-28)]] 가 동일한 구조/의미 분업 메시지를 한국어로 자연스럽게 번역해 정리했다 — 즉 *"파서는 구조, LLM 은 의미"* 라는 핵심 분업이 사용자 측에서도 무리 없이 인식되는 *전달 가능한 추상* 임을 보여준다. 2차 소스에서 메시지가 거의 손실 없이 도착하는 것은 추상의 견고함의 시그널.

## References

- [[lum1104-understand-anything]] (1차)
- [[james-ai-explorer-understand-anything]] (2차, 한국어 블로그)
- [[tree-sitter]] · [[code-knowledge-graph]] · [[brain-hands-decoupling]]
