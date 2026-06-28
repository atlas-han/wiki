---
title: 복합체 (Composite)
type: engineering
tags: [engineering, design-patterns, gof, structural]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [design-patterns, design-pattern-adapter, design-pattern-bridge, design-pattern-decorator, actix-web-routing]
first-seen: refactoring-guru-ko-design-patterns
sources: [refactoring-guru-ko-design-patterns]
---

# 복합체 (Composite)

객체들을 트리 구조로 구성한 뒤, 이 구조 전체와 개별 객체를 동일한 방식으로 다룰 수 있게 한다. [[design-patterns]]의 구조 패턴에 속한다.

## 문제

제품(Product)과 상자(Box)로 이루어진 중첩 구조에서 주문 전체의 가격을 계산한다고 하자. 상자 안에는 제품이 들어갈 수도, 더 작은 상자가 들어갈 수도 있고 그 안에 또 제품이 있을 수 있다. 이런 구조에서 모든 상자를 일일이 열어 중첩 수준과 객체 타입을 직접 파악하며 합산하려면 코드가 매우 복잡해진다.

## 해결책

단순 요소(Leaf)와 컨테이너(Composite)가 모두 구현하는 공통 인터페이스(Component)를 정의한다. 이 인터페이스에는 가격 계산 같은 메서드가 선언되어 있어서, Leaf는 자기 값을 직접 반환하고 Composite는 자식 요소들에게 같은 요청을 재귀적으로 전달한 뒤 결과를 합산한다. 클라이언트는 단일 객체인지 트리인지 구분하지 않고 동일하게 호출한다.

## 실세계 비유

군대 조직과 같다. 군대는 여러 사단으로, 사단은 여단의 집합으로, 여단은 다시 더 작은 단위들로 구성된다. 명령은 계층구조의 최상위에서 내려와 각 하위 계층으로 전달되며, 결국 모든 병사가 자신이 수행해야 할 작업을 알게 될 때까지 같은 방식으로 흘러간다.

## 적용 가능성

- 트리처럼 부분-전체 계층을 가진 객체 구조를 구현해야 할 때
- 클라이언트 코드가 단순 요소와 복합 요소를 구분하지 않고 균일하게 다루기를 원할 때
- 파일 시스템, UI 컴포넌트 트리, 조직도처럼 재귀적 중첩 구조를 순회·집계해야 할 때

## 장단점

**장점**
- 다형성과 재귀를 활용해 복잡한 트리 구조를 편리하게 다룰 수 있다
- 개방/폐쇄 원칙: 기존 코드를 훼손하지 않고 새로운 요소 유형을 트리에 도입할 수 있다

**단점**
- 기능이 너무 다른 클래스들에 공통 인터페이스를 제공하기 어려울 수 있다
- 인터페이스를 과도하게 일반화하면 이해하기 어려워진다

## 다른 패턴과의 관계

- [[design-pattern-builder]]로 복잡한 복합체 트리를 단계적으로 생성할 수 있다.
- [[design-pattern-iterator]]로 복합체 트리를 순회하고, [[design-pattern-visitor]]로 트리 전체에 걸친 동작을 실행할 수 있다.
- 복합체 트리의 공유되는 잎 노드는 [[design-pattern-flyweight]]로 구현해 메모리를 절약할 수 있다.
- [[design-pattern-decorator]]와 구조가 비슷하지만(둘 다 재귀적 합성), 데코레이터는 자식이 하나뿐이고 복합체는 여러 자식을 가진다. [[design-pattern-chain-of-responsibility]], [[design-pattern-prototype]]과도 함께 쓰인다.

## References

- [[refactoring-guru-ko-design-patterns]] — 복합체 원문: https://refactoring.guru/ko/design-patterns/composite
- [[design-patterns]]
- 실무 예: [[actix-web-routing]] — 중첩 `web::scope`가 resource·하위 scope를 자식으로 담는 트리
