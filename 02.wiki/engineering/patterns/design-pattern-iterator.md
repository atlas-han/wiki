---
title: 반복자 (Iterator)
type: engineering
tags: [engineering, design-patterns, gof, behavioral]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [design-patterns, design-pattern-chain-of-responsibility, design-pattern-command, design-pattern-mediator]
first-seen: refactoring-guru-ko-design-patterns
sources: [refactoring-guru-ko-design-patterns]
---

# 반복자 (Iterator)

컬렉션 요소들의 기본 표현(리스트, 스택, 트리 등)을 노출하지 않고 그것들을 하나씩 순회할 수 있게 하는 패턴이다. [[design-patterns]]의 행동 패턴에 속한다.

## 문제

컬렉션은 리스트, 스택, 트리 등 서로 다른 내부 구조를 가질 수 있고, 복잡한 자료구조를 순회하려면 여러 순회 알고리즘이 필요하다. 이런 알고리즘을 컬렉션 클래스에 직접 넣으면 컬렉션의 본래 책임(데이터 저장)이 모호해진다. 또한 클라이언트 코드가 특정 컬렉션 구현에 종속되어 버린다.

## 해결책

순회 동작을 반복자(iterator)라는 별도 객체로 추출한다. Iterator는 `next()`, `hasNext()` 같은 공통 인터페이스를 제공하고, ConcreteIterator는 현재 순회 위치 등 순회 상태를 캡슐화한다. 상태가 캡슐화되므로 여러 반복자가 같은 컬렉션을 동시에 독립적으로 순회할 수 있고, 클라이언트는 구체 구현과 분리된다.

## 실세계 비유

로마 여행에 비유할 수 있다. 같은 도시의 관광명소를 무작정 발길 닿는 대로 돌아다니거나, 스마트폰 내비게이터를 따라가거나, 현지 가이드를 고용해 둘러볼 수 있다. 각 방법은 동일한 관광지 집합을 서로 다른 방식으로 "순회"하는 반복자에 해당한다.

## 적용 가능성

- 컬렉션의 복잡한 내부 자료구조를 클라이언트에게 숨기고 싶을 때
- 앱 곳곳에 흩어진 순회 코드의 중복을 줄이고 싶을 때
- 코드가 다양한 자료구조를 순회해야 하거나 그 구조 유형을 미리 알 수 없을 때

## 장단점

**장점**
- 단일 책임 원칙(SRP): 큰 순회 알고리즘을 별도 클래스로 분리한다.
- 개방/폐쇄 원칙(OCP): 기존 코드를 바꾸지 않고 새 컬렉션·반복자를 추가할 수 있다.
- 같은 컬렉션을 여러 반복자로 병렬 순회하거나, 순회를 잠시 멈췄다가 이어갈 수 있다.

**단점**
- 단순한 컬렉션만 다룰 때는 과한 설계가 될 수 있다.
- 특수한 컬렉션에서는 요소를 직접 탐색하는 것보다 효율이 떨어질 수 있다.

## 다른 패턴과의 관계

- [[design-pattern-composite]] 트리를 순회하는 데 반복자를 사용할 수 있다.
- [[design-pattern-factory-method]]와 함께 써서 컬렉션과 호환되는 반복자를 반환하게 만들 수 있다.
- [[design-pattern-memento]]와 함께 쓰면 현재 순회 상태를 포착해 두었다가 필요할 때 롤백할 수 있다.
- [[design-pattern-visitor]]와 함께 쓰면 복잡한 자료구조를 순회하며 각 요소에 작업을 실행할 수 있다.

## References

- [[refactoring-guru-ko-design-patterns]] — 반복자 원문: https://refactoring.guru/ko/design-patterns/iterator
- [[design-patterns]]
