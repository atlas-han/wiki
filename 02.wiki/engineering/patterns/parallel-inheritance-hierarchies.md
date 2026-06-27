---
title: Parallel Inheritance Hierarchies
type: engineering
tags: [engineering, refactoring]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [code-smells, refactoring-techniques, technical-debt]
first-seen: refactoring-guru-refactoring
sources: [refactoring-guru-refactoring]
---

# Parallel Inheritance Hierarchies

Parallel Inheritance Hierarchies는 [[code-smells]] 중 하나로, 한 계층에 subclass를 추가할 때 다른 계층에도 대응 subclass를 추가해야 하는 상태.

## 문제 신호

- 코드를 읽는 사람이 실제 의도보다 구조적 noise를 먼저 이해해야 한다.
- 같은 변경을 반복하거나, 변경 위치를 예측하기 어려워진다.
- 테스트 없이 고치면 behavior drift가 생기기 쉽다.

## 대표 대응

- 후보 technique: `Move Method`, `Move Field`
- 먼저 현재 feature와 관련된 최소 범위를 정하고, [[refactoring]] 원칙대로 behavior-preserving step으로 쪼갠다.
- smell 제거가 더 큰 API churn을 만들면 [[technical-debt]]로 명시하고 상환 시점을 따로 잡는다.

## 관련

- [[code-smells]]
- [[refactoring-techniques]]
- [[technical-debt]]

## References

- [[refactoring-guru-refactoring]] — https://refactoring.guru/smells/parallel-inheritance-hierarchies
