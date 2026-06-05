---
title: Tree-sitter
type: entity
category: tool
tags: [parser, static-analysis, syntax-tree, developer-tooling]
links:
  - https://tree-sitter.github.io/tree-sitter/
sources: [lum1104-understand-anything, james-ai-explorer-understand-anything]
created: 2026-05-30
updated: 2026-06-01
---

# Tree-sitter

소스 코드를 concrete syntax tree(CST)로 파싱하는 incremental 파서 생성기·라이브러리. 다국어 문법을 지원하며, 결정론적(deterministic) — 같은 입력은 항상 같은 트리를 낸다. 본 위키에는 [[lum1104-understand-anything|Understand-Anything]]의 분석 엔진으로 처음 등장.

## 위키에서 알려진 역할

[[understand-anything|Understand-Anything]]의 [[tree-sitter-llm-hybrid|Tree-sitter + LLM 하이브리드]]에서 **결정론적(structural) 측**을 담당:

- import/export, 함수·클래스 정의, call site, 상속 등 구조적 사실 추출
- 스캔 단계에서 `importMap`으로 pre-resolve → file-analyzer가 import를 재유도하지 않게 함
- fingerprint 기반 변경 감지로 [[understand-anything|증분 업데이트]] 구동
- "Same input → same output, every run" — 그래프의 구조적 측면이 reproducible한 이유

LLM이 못 하는 일(정확한 구문 파싱)을 빠르고 싸게, 반복 가능하게 처리하고, 의미적 해석은 LLM에 넘기는 분업의 한 축.

## References

- [[lum1104-understand-anything]] (1차)
- [[james-ai-explorer-understand-anything]] (2차, 한국어 블로그)
- [[tree-sitter-llm-hybrid]] · [[understand-anything]]
- [Tree-sitter 공식 문서](https://tree-sitter.github.io/tree-sitter/)
