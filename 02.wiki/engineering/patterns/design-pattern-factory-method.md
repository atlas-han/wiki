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

부모 클래스가 객체 생성 인터페이스(factory method)를 제공하되, 어떤 구상 제품(concrete product)을 만들지는 자식 클래스가 결정하도록 하는 패턴이다. [[design-patterns]]의 생성 패턴에 속한다.

## 문제
기존 코드가 특정 구상 클래스(예: `Truck`)에 강하게 결합되어 있으면, 새로운 제품 유형(예: `Ship`)을 추가할 때 코드베이스 곳곳을 수정해야 한다. 결국 제품 유형에 따라 동작이 갈라지는 복잡한 조건문이 늘어나고, 제품군이 확장될수록 유지보수가 어려워진다.

## 해결책
직접적인 객체 생성 호출(`new`)을 별도의 factory method 호출로 대체한다. Creator가 Product 인터페이스를 반환하는 factory method를 선언하고, ConcreteCreator가 이를 오버라이드해 자신이 만들 ConcreteProduct를 반환한다. 클라이언트 코드는 추상 Product 인터페이스만 다루므로 구상 제품 클래스와 분리된다.

## 예시
물류 관리 앱에서 처음에는 트럭 운송(`Truck`)만 지원하다가 해상 운송(`Ship`)을 추가해야 하는 상황을 든다. 또 크로스플랫폼 UI에서 Windows 버튼과 Web 버튼처럼, 같은 다이얼로그 코드가 플랫폼별로 다른 버튼 객체를 생성해야 하는 경우를 예시로 보여준다.

## 적용 가능성
- 함께 작동할 객체들의 정확한 유형과 의존 관계를 코드 작성 시점에 미리 알 수 없을 때
- 제품 생성 코드를 사용 코드와 분리해 확장 지점을 한곳으로 모으고 싶을 때
- 라이브러리/프레임워크 사용자에게 내부 컴포넌트를 확장(교체)할 수 있는 방법을 제공하고 싶을 때
- 기존에 만든 객체를 매번 다시 생성하지 않고 재사용해 시스템 리소스를 절약하고 싶을 때

## 장단점
**장점**
- Creator와 구상 제품들 사이의 결합을 제거한다.
- 생성 코드를 한곳으로 모아 단일 책임 원칙(SRP)을 지킨다.
- 기존 클라이언트 코드를 손상시키지 않고 새 제품 유형을 추가할 수 있어 개방/폐쇄 원칙(OCP)을 따른다.

**단점**
- 패턴 도입을 위해 자식 클래스가 많이 늘어나 코드가 복잡해질 수 있다.

## 다른 패턴과의 관계
- 설계가 복잡해지면 [[design-pattern-abstract-factory]], [[design-pattern-prototype]], [[design-pattern-builder]]로 발전하는 경우가 많다.
- [[design-pattern-abstract-factory]]는 여러 factory method의 집합을 기반으로 구현되는 경우가 많다.
- [[design-pattern-template-method]]의 특수화로 볼 수 있으며, template method의 한 단계가 factory method일 수 있다.
- [[design-pattern-iterator]]와 함께 써서 컬렉션과 호환되는 반복자를 생성·반환하기도 한다.

## References
- [[refactoring-guru-ko-design-patterns]] — 팩토리 메서드 원문: https://refactoring.guru/ko/design-patterns/factory-method
- [[design-patterns]]
