---
title: 빌더 (Builder)
type: engineering
tags: [engineering, design-patterns, gof, creational]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [design-patterns, design-pattern-factory-method, design-pattern-abstract-factory, design-pattern-prototype, actix-web-handlers-responders]
first-seen: refactoring-guru-ko-design-patterns
sources: [refactoring-guru-ko-design-patterns]
---

# 빌더 (Builder)

복잡한 객체를 단계별로(step by step) 생성하게 하여, 같은 생성 코드로 서로 다른 표현(representation)을 만들 수 있게 하는 패턴이다. [[design-patterns]]의 생성 패턴에 속한다.

## 문제
필드가 많은 복잡한 객체를 초기화하려면 생성자에 매개변수가 잔뜩 붙는 "점층적 생성자(telescoping constructor)" 문제가 생기거나, 가능한 모든 구성 조합마다 자식 클래스를 만들어야 해 계층이 폭발한다. 게다가 대부분의 호출에서 상당수 매개변수는 실제로 쓰이지 않아 호출부가 지저분해진다.

## 해결책
객체 생성 코드를 본체에서 떼어내 `builder`라는 별도 객체로 옮기고, 생성 과정을 `buildWalls`, `buildDoor`처럼 단계별 메서드로 나눈다. 클라이언트는 필요한 단계만 호출하면 되고, 같은 단계들을 다르게 구현한 ConcreteBuilder로 서로 다른 표현을 만든다. 생성 순서를 재사용하고 싶다면 Director 클래스에 그 절차를 캡슐화한다.

## 예시
주택 건설을 예로 든다. 벽·문·창문·차고·수영장 등 옵션이 많은 `House` 객체를, 거대한 생성자나 수많은 자식 클래스 없이 `buildWalls()`, `buildDoor()` 같은 단계를 필요한 만큼만 호출해 조립한다. 같은 단계 집합을 다르게 구현하면 통나무집과 성처럼 다른 표현을 같은 절차로 만들 수 있다.

## 적용 가능성
- 점층적 생성자(매개변수가 과도하게 많은 생성자)를 제거하고 싶을 때
- 같은 생성 코드로 제품의 서로 다른 표현(예: 돌집 vs 나무집)을 만들고 싶을 때
- [[design-pattern-composite]] 트리 같은 복잡한 객체를 단계별로 구성해야 할 때

## 장단점
**장점**
- 객체를 단계별로 생성하거나, 단계 실행을 미루거나 재귀적으로 실행할 수 있다.
- 제품의 여러 표현을 만들 때 같은 생성 코드를 재사용할 수 있다.
- 생성 코드를 비즈니스 로직에서 분리해 단일 책임 원칙(SRP)을 지킨다.

**단점**
- 여러 새 클래스를 만들어야 하므로 코드 전체의 복잡성이 증가한다.

## 다른 패턴과의 관계
- [[design-pattern-factory-method]]로 시작했다가 더 유연함이 필요해지면 빌더로 발전하는 경우가 많다.
- [[design-pattern-abstract-factory]]는 관련 제품군을 즉시 반환하는 데 집중하는 반면, 빌더는 한 복잡한 제품을 여러 단계로 만들고 결과 반환을 마지막까지 미룰 수 있다.
- [[design-pattern-composite]] 트리를 만들 때 자주 함께 쓰이고, [[design-pattern-bridge]]와 조합할 수 있으며, Director를 [[design-pattern-singleton]]으로 구현하기도 한다.

## References
- [[refactoring-guru-ko-design-patterns]] — 빌더 원문: https://refactoring.guru/ko/design-patterns/builder
- [[design-patterns]]
- 실무 예: [[actix-web-handlers-responders]] — `HttpResponse::Ok().content_type(..).body(..)` 빌더 체인
