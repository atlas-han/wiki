---
title: Incomplete Library Class
type: engineering
tags: [engineering, refactoring]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [code-smells, refactoring-techniques, technical-debt]
first-seen: refactoring-guru-refactoring
sources: [refactoring-guru-refactoring]
---

# Incomplete Library Class

Incomplete Library Class는 [[code-smells]] 중 하나로, 사용 중인 라이브러리가 필요한 기능을 제공하지 않지만 직접 수정하기 어려운 상태.

## 문제 신호

- 코드를 읽는 사람이 실제 의도보다 구조적 noise를 먼저 이해해야 한다.
- 같은 변경을 반복하거나, 변경 위치를 예측하기 어려워진다.
- 테스트 없이 고치면 behavior drift가 생기기 쉽다.

## 대표 대응

- 후보 technique: `Introduce Foreign Method`, `Introduce Local Extension`
- 먼저 현재 feature와 관련된 최소 범위를 정하고, [[refactoring]] 원칙대로 behavior-preserving step으로 쪼갠다.
- smell 제거가 더 큰 API churn을 만들면 [[technical-debt]]로 명시하고 상환 시점을 따로 잡는다.

## 관련

- [[code-smells]]
- [[refactoring-techniques]]
- [[technical-debt]]

## References

- [[refactoring-guru-refactoring]] — https://refactoring.guru/smells/incomplete-library-class
