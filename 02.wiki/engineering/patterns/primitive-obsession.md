---
title: Primitive Obsession
type: engineering
tags: [engineering, refactoring]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [code-smells, refactoring-techniques, technical-debt]
first-seen: refactoring-guru-refactoring
sources: [refactoring-guru-refactoring]
---

# Primitive Obsession

Primitive Obsession는 [[code-smells]] 중 하나로, 도메인 의미가 있는 값·범위·분류를 작은 객체 대신 primitive·상수로 표현하는 상태.

## 문제 신호

- 코드를 읽는 사람이 실제 의도보다 구조적 noise를 먼저 이해해야 한다.
- 같은 변경을 반복하거나, 변경 위치를 예측하기 어려워진다.
- 테스트 없이 고치면 behavior drift가 생기기 쉽다.

## 대표 대응

- 후보 technique: `Replace Data Value with Object`, `Replace Type Code with Class`, `Replace Type Code with State/Strategy`, `Introduce Parameter Object`
- 먼저 현재 feature와 관련된 최소 범위를 정하고, [[refactoring]] 원칙대로 behavior-preserving step으로 쪼갠다.
- smell 제거가 더 큰 API churn을 만들면 [[technical-debt]]로 명시하고 상환 시점을 따로 잡는다.

## 관련

- [[code-smells]]
- [[refactoring-techniques]]
- [[technical-debt]]

## References

- [[refactoring-guru-refactoring]] — https://refactoring.guru/smells/primitive-obsession
