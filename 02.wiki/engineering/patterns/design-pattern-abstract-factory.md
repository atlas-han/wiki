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

관련 객체들의 구상 클래스를 지정하지 않고도 서로 호환되는 객체들의 모음(제품군)을 생성하게 해 주는 패턴이다. [[design-patterns]]의 생성 패턴에 속한다.

## 문제
서로 어울려야 하는 객체들이 여러 변형(variant)으로 존재할 때, 잘못 조합하면 일관성이 깨진다. 예컨대 스타일이 제각각인 가구가 섞여 배송되면 고객이 불만족한다. 스타일이 맞지 않는 제품 조합을 막으면서도, 새 제품이나 새 스타일을 추가할 때 기존 코드 변경을 최소화해야 한다.

## 해결책
각 제품 유형마다 추상 인터페이스(예: `Chair`, `Sofa`, `CoffeeTable`)를 선언하고, 변형(스타일)별로 이 제품들을 함께 만드는 구상 팩토리 클래스를 둔다. AbstractFactory가 제품별 생성 메서드를 선언하고 ConcreteFactory가 한 제품군 전체를 생성한다. 클라이언트는 추상 팩토리·추상 제품 인터페이스만 다루므로, 변형을 바꿀 때는 팩토리 선택 로직만 수정하면 된다.

## 실세계 비유
가구 판매장을 위한 프로그램을 떠올려 보자. `Chair`(의자), `Sofa`(소파), `CoffeeTable`(커피 테이블) 같은 제품들이 각각 Modern, Victorian, ArtDeco 같은 스타일로 제공된다. 고객은 한 스타일로 통일된 가구 세트를 받기를 원하므로, 같은 스타일의 제품들을 묶어서 생산하는 팩토리가 필요하다.

## 적용 가능성
- 코드가 서로 관련된 여러 제품군(family)과 작동해야 하지만, 그 제품들의 구상 클래스에 의존하고 싶지 않을 때
- 향후 새로운 제품군 추가를 통한 확장을 허용하고 싶을 때
- 한 클래스에 여러 factory method가 모여 있어 그 클래스의 주된 책임이 흐려질 때(생성 책임을 분리하고 싶을 때)

## 장단점
**장점**
- 한 팩토리에서 만들어지는 제품들이 서로 호환됨을 보장한다.
- 구상 제품과 클라이언트 코드 사이의 결합을 피한다.
- 생성 코드를 한곳으로 모아 단일 책임 원칙(SRP)을 따른다.
- 기존 코드를 깨지 않고 새 변형을 추가할 수 있어 개방/폐쇄 원칙(OCP)을 따른다.

**단점**
- 새로운 인터페이스와 클래스가 많이 늘어나 코드가 복잡해질 수 있다.

## 다른 패턴과의 관계
- 흔히 [[design-pattern-factory-method]]로 시작했다가 복잡도가 커지면서 추상 팩토리로 발전한다. 추상 팩토리는 종종 factory method의 집합으로 구현되거나 [[design-pattern-prototype]]으로 구현되기도 한다.
- [[design-pattern-builder]]가 복잡한 객체를 단계별로 만드는 데 집중한다면, 추상 팩토리는 제품군을 한 번에 만드는 데 집중한다.
- [[design-pattern-facade]] 대신 쓰여 서브시스템 객체 생성을 감출 수 있고, [[design-pattern-bridge]]와 함께 쓰이기도 하며, 팩토리 자체를 [[design-pattern-singleton]]으로 관리하기도 한다.

## References
- [[refactoring-guru-ko-design-patterns]] — 추상 팩토리 원문: https://refactoring.guru/ko/design-patterns/abstract-factory
- [[design-patterns]]
