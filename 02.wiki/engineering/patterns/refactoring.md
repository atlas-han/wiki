---
title: Refactoring
type: engineering
tags: [engineering, refactoring]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [code-smells, refactoring-techniques, technical-debt, design-patterns]
first-seen: refactoring-guru-refactoring
sources: [refactoring-guru-refactoring]
---

# Refactoring

Refactoring은 외부 동작을 유지하면서 내부 설계를 개선하는 작은 변경들의 연속이다. [[refactoring-guru-refactoring]] 기준으로 핵심 흐름은 [[code-smells]]를 진단하고, 적절한 [[refactoring-techniques]]를 선택하며, [[technical-debt]]의 이자를 낮추는 것이다.

## 판단 기준

- 기능 추가와 구조 개선을 섞지 않는다. 기능 변경 PR과 refactoring PR을 분리하면 regression 원인 추적이 쉬워진다.
- 테스트가 안전망이다. 동작 보존을 검증할 수 없으면 리팩터링은 개선이 아니라 재작성 위험이 된다.
- 큰 redesign보다 작은 mechanical step을 선호한다. `Extract Method` → `Move Method` → `Replace Conditional with Polymorphism`처럼 관찰 가능한 단계를 쌓는다.
- smell은 명령이 아니라 signal이다. [[code-smells]]가 있어도 지금 변경 축과 관련 없으면 미룰 수 있다.

## 리뷰에서 쓸 질문

1. 이 변경은 외부 behavior를 바꾸는가, 내부 구조만 바꾸는가?
2. 어떤 smell을 줄이는가? ([[long-method]], [[duplicate-code]], [[feature-envy]], [[shotgun-surgery]] 등)
3. 어떤 technique을 적용했는가? ([[refactoring-techniques]]의 family 이름으로 설명)
4. 변경 후 다음 feature가 더 싸지는가, 아니면 단지 취향에 맞게 바뀐 것인가?

## 관련 페이지

- [[technical-debt]] — 리팩터링을 미룰 때 누적되는 이자 비용
- [[code-smells]] — 리팩터링 후보를 찾는 진단 vocabulary
- [[refactoring-techniques]] — smell을 낮추는 구체적 변환 vocabulary
- [[design-patterns]] — 반복 설계 문제의 구조 vocabulary

## References

- [[refactoring-guru-refactoring]]
