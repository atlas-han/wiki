---
title: 추상 팩토리 (Abstract Factory)
type: engineering
tags: [engineering, design-patterns, gof, creational]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [design-patterns, design-pattern-factory-method, design-pattern-builder, design-pattern-prototype]
first-seen: refactoring-guru-ko-design-patterns
sources: [refactoring-guru-ko-design-patterns]
---

# 추상 팩토리 (Abstract Factory)

관련 객체들의 구상 클래스에 의존하지 않고, 서로 호환되는 제품군을 생성한다. [[design-patterns]]의 생성 패턴에 속하며, 원문 기준 URL은 `https://refactoring.guru/ko/design-patterns/abstract-factory`이다.

## 문제 신호

UI 위젯, DB 드라이버, 플랫폼별 객체처럼 “함께 써야 하는” 객체 집합이 여러 variant로 존재할 때.

## 구조

AbstractFactory가 제품별 생성 메서드를 제공하고 ConcreteFactory가 한 제품군 전체를 만든다. 클라이언트는 AbstractProduct 인터페이스만 본다.

## 적용 메모

- 클라이언트가 구상 타입이나 구체 협력자를 직접 알아야 하는 지점을 줄이는 데 초점을 둔다.
- 패턴명보다 중요한 것은 변경 축이다. 변경 축이 없거나 단순하면 일반 함수/클래스/언어 기능으로 충분할 수 있다.
- 테스트에서는 패턴이 만든 seam을 활용해 구상 구현 대신 fake/mock을 주입할 수 있는지 확인한다.

## 장단점

제품군 일관성을 강제하고 구상 클래스 의존을 제거한다. 새 제품군 추가는 쉽지만, 제품 종류를 추가하면 모든 factory 인터페이스를 바꿔야 한다.

## 관련 패턴

[[design-pattern-factory-method]]를 여러 개 모아 구현하는 경우가 많고, factory 자체는 [[design-pattern-singleton]]으로 관리되기도 한다.

## References

- [[refactoring-guru-ko-design-patterns]] — 추상 팩토리 원문: https://refactoring.guru/ko/design-patterns/abstract-factory
- [[design-patterns]]
