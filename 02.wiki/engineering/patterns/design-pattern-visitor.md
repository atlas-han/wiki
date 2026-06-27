---
title: 비지터 (Visitor)
type: engineering
tags: [engineering, design-patterns, gof, behavioral]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [design-patterns, design-pattern-chain-of-responsibility, design-pattern-command, design-pattern-iterator]
first-seen: refactoring-guru-ko-design-patterns
sources: [refactoring-guru-ko-design-patterns]
---

# 비지터 (Visitor)

객체 구조를 바꾸지 않고 새로운 operation을 추가한다. [[design-patterns]]의 행동 패턴에 속하며, 원문 기준 URL은 `https://refactoring.guru/ko/design-patterns/visitor`이다.

## 문제 신호

클래스 구조는 안정적이지만 수행할 연산이 자주 늘고, 연산 로직을 타입별로 분리하고 싶을 때.

## 구조

Element가 accept(visitor)를 제공하고 Visitor가 element 타입별 visit 메서드를 가진다. ConcreteVisitor가 새 operation을 구현한다.

## 적용 메모

- 클라이언트가 구상 타입이나 구체 협력자를 직접 알아야 하는 지점을 줄이는 데 초점을 둔다.
- 패턴명보다 중요한 것은 변경 축이다. 변경 축이 없거나 단순하면 일반 함수/클래스/언어 기능으로 충분할 수 있다.
- 테스트에서는 패턴이 만든 seam을 활용해 구상 구현 대신 fake/mock을 주입할 수 있는지 확인한다.

## 장단점

새 operation 추가가 쉽고 연산 로직을 한곳에 모은다. 새 Element 타입 추가는 모든 Visitor 변경을 요구한다.

## 관련 패턴

[[design-pattern-composite]] 트리에 새 연산을 붙일 때 강력하다. 순회만 필요하면 [[design-pattern-iterator]]가 더 단순하다.

## References

- [[refactoring-guru-ko-design-patterns]] — 비지터 원문: https://refactoring.guru/ko/design-patterns/visitor
- [[design-patterns]]
