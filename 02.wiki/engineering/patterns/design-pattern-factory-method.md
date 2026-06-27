---
title: 팩토리 메서드 (Factory Method)
type: engineering
tags: [engineering, design-patterns, gof, creational]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [design-patterns, design-pattern-abstract-factory, design-pattern-builder, design-pattern-prototype]
first-seen: refactoring-guru-ko-design-patterns
sources: [refactoring-guru-ko-design-patterns]
---

# 팩토리 메서드 (Factory Method)

부모 클래스가 객체 생성 인터페이스를 제공하고, 자식 클래스가 실제 생성 제품을 바꾸게 한다. [[design-patterns]]의 생성 패턴에 속하며, 원문 기준 URL은 `https://refactoring.guru/ko/design-patterns/factory-method`이다.

## 문제 신호

구상 클래스 생성이 클라이언트 코드 곳곳에 퍼져 있고, 제품군이 늘 때마다 조건문과 결합도가 증가할 때.

## 구조

Creator가 Product 인터페이스를 반환하는 factory method를 선언하고, ConcreteCreator가 ConcreteProduct 선택을 캡슐화한다.

## 적용 메모

- 클라이언트가 구상 타입이나 구체 협력자를 직접 알아야 하는 지점을 줄이는 데 초점을 둔다.
- 패턴명보다 중요한 것은 변경 축이다. 변경 축이 없거나 단순하면 일반 함수/클래스/언어 기능으로 충분할 수 있다.
- 테스트에서는 패턴이 만든 seam을 활용해 구상 구현 대신 fake/mock을 주입할 수 있는지 확인한다.

## 장단점

새 제품 추가 시 클라이언트 변경을 줄이고 생성 책임을 한 곳으로 모은다. 다만 Creator 계층이 늘어나 단순 생성에는 과할 수 있다.

## 관련 패턴

[[design-pattern-abstract-factory]]는 여러 관련 제품군의 factory method 묶음으로 볼 수 있고, [[design-pattern-template-method]]와 함께 Creator의 알고리즘 일부를 생성 단계로 열어둘 수 있다.

## References

- [[refactoring-guru-ko-design-patterns]] — 팩토리 메서드 원문: https://refactoring.guru/ko/design-patterns/factory-method
- [[design-patterns]]
