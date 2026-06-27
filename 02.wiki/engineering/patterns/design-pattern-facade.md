---
title: 퍼사드 (Facade)
type: engineering
tags: [engineering, design-patterns, gof, structural]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [design-patterns, design-pattern-adapter, design-pattern-bridge, design-pattern-composite]
first-seen: refactoring-guru-ko-design-patterns
sources: [refactoring-guru-ko-design-patterns]
---

# 퍼사드 (Facade)

라이브러리, 프레임워크 또는 복잡하게 얽힌 클래스 집합에 대해 단순화된 고수준 인터페이스를 제공한다. [[design-patterns]]의 구조 패턴에 속한다.

## 문제

정교한 라이브러리나 프레임워크에 속한 수많은 객체를 직접 다루려면 객체 초기화, 종속성 관리, 메서드 호출 순서 조정 등 신경 쓸 것이 많다. 그 결과 비즈니스 로직이 외부 클래스의 구현 세부사항과 강하게 결합되어, 코드를 이해하고 유지보수하기 어려워진다.

## 해결책

퍼사드는 복잡한 하위 시스템에 대한 간단한 인터페이스를 제공하는 클래스다. 하위 시스템 객체들을 알고 있으면서 클라이언트가 실제로 필요로 하는 기능만 노출하고, 나머지 복잡한 초기화와 호출 순서는 내부에 캡슐화한다. 클라이언트는 하위 시스템을 직접 알 필요 없이 퍼사드의 단순한 API만 사용한다.

## 실세계 비유

전화로 상품을 주문할 때 전화를 받는 상담원(교환원)이 바로 퍼사드다. 상담원은 매장의 모든 서비스와 부서, 주문 처리 시스템에 대한 단순화된 창구 역할을 한다. 고객은 복잡한 내부 절차를 알 필요 없이 상담원에게 원하는 것만 말하면 된다.

## 적용 가능성

- 복잡한 하위 시스템에 대해 제한적이지만 간단한 인터페이스가 필요할 때
- 하위 시스템을 여러 계층으로 구조화하고 싶을 때 (각 계층의 진입점을 퍼사드로 제공)
- 비즈니스 로직과 외부 라이브러리/프레임워크의 결합을 줄이고 싶을 때

## 장단점

**장점**
- 복잡한 하위 시스템으로부터 코드를 분리해 격리할 수 있다

**단점**
- 퍼사드가 앱의 모든 클래스에 결합된 전지전능한(god) 객체가 될 위험이 있다

## 다른 패턴과의 관계

- [[design-pattern-adapter]]는 기존 인터페이스를 다른 인터페이스로 변환하지만, 퍼사드는 기존 객체들 위에 새로운 인터페이스를 정의한다.
- [[design-pattern-abstract-factory]]는 하위 시스템 객체 생성 방식을 숨기고 싶을 때 퍼사드의 대안이 될 수 있다.
- [[design-pattern-flyweight]]가 작은 객체를 많이 만드는 것과 반대로, 퍼사드는 전체 하위 시스템을 대표하는 단일 객체를 만든다.
- [[design-pattern-mediator]]와 역할이 비슷하지만, 중재자는 컴포넌트 간 통신을 중앙화하고 퍼사드는 단순히 하위 시스템으로의 단방향 진입점을 제공한다. 퍼사드는 흔히 [[design-pattern-singleton]]으로 만들어진다. [[design-pattern-proxy]]와 유사하나 인터페이스가 다르다.

## References

- [[refactoring-guru-ko-design-patterns]] — 퍼사드 원문: https://refactoring.guru/ko/design-patterns/facade
- [[design-patterns]]
