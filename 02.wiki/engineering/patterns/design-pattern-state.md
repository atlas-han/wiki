---
title: 상태 (State)
type: engineering
tags: [engineering, design-patterns, gof, behavioral]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [design-patterns, design-pattern-chain-of-responsibility, design-pattern-command, design-pattern-iterator]
first-seen: refactoring-guru-ko-design-patterns
sources: [refactoring-guru-ko-design-patterns]
---

# 상태 (State)

객체 내부 상태가 바뀔 때 행동도 바뀌게 하되 상태별 행동을 별도 클래스로 분리한다. [[design-patterns]]의 행동 패턴에 속하며, 원문 기준 URL은 `https://refactoring.guru/ko/design-patterns/state`이다.

## 문제 신호

상태별 조건문이 커지고 전이가 복잡해져서 상태 머신처럼 다루는 편이 명확할 때.

## 구조

Context가 State 인터페이스를 참조하고 ConcreteState가 상태별 행동과 전이 결정을 구현한다.

## 적용 메모

- 클라이언트가 구상 타입이나 구체 협력자를 직접 알아야 하는 지점을 줄이는 데 초점을 둔다.
- 패턴명보다 중요한 것은 변경 축이다. 변경 축이 없거나 단순하면 일반 함수/클래스/언어 기능으로 충분할 수 있다.
- 테스트에서는 패턴이 만든 seam을 활용해 구상 구현 대신 fake/mock을 주입할 수 있는지 확인한다.

## 장단점

조건문을 제거하고 상태별 책임을 분리한다. 상태 수가 많으면 클래스가 늘고 전이 규칙이 흩어질 수 있다.

## 관련 패턴

[[design-pattern-strategy]]와 구조는 유사하지만 State는 상태 전이를 통해 객체 행동이 자체적으로 바뀌고, Strategy는 외부에서 알고리즘을 선택하는 성격이 강하다.

## References

- [[refactoring-guru-ko-design-patterns]] — 상태 원문: https://refactoring.guru/ko/design-patterns/state
- [[design-patterns]]
