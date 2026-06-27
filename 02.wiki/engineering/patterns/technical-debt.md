---
title: Technical Debt
type: engineering
tags: [engineering, refactoring]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [refactoring, code-smells, surgical-edits]
first-seen: refactoring-guru-refactoring
sources: [refactoring-guru-refactoring]
---

# Technical Debt

Technical Debt는 “지금 빠르게 가기 위해 구조 개선을 미룬 선택”이 이후 변경 때마다 이자처럼 비용을 발생시키는 상태다. [[refactoring]]은 새 기능을 추가하지 않고 이 이자를 줄이는 대표적 상환 수단이다.

## 실무 해석

- debt 자체가 항상 나쁜 것은 아니다. 문제는 **의식적 debt인지**, **상환 시점과 비용을 추적하는지**다.
- [[code-smells]]는 debt가 코드 표면에 드러난 신호다. 예: [[duplicate-code]]는 수정 누락 위험, [[shotgun-surgery]]는 변경 비용, [[primitive-obsession]]은 도메인 표현력 부족을 만든다.
- 상환은 rewrite가 아니라 작은 [[refactoring-techniques]]의 누적이어야 한다. [[surgical-edits]] 원칙처럼 요청과 직접 관련 없는 대규모 정리는 오히려 위험하다.

## 상환 우선순위

1. 지금 만드는 feature와 같은 변경 축에 있는 smell
2. 테스트로 behavior 보존을 검증할 수 있는 영역
3. 반복 수정·장애·온보딩 지연의 실제 비용이 관찰된 영역
4. 단순 취향 문제가 아니라 coupling/cohesion/duplication을 개선하는 영역

## References

- [[refactoring-guru-refactoring]]
