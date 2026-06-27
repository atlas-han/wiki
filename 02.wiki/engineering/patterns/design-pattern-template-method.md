---
title: 템플릿 메서드 (Template Method)
type: engineering
tags: [engineering, design-patterns, gof, behavioral]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [design-patterns, design-pattern-chain-of-responsibility, design-pattern-command, design-pattern-iterator]
first-seen: refactoring-guru-ko-design-patterns
sources: [refactoring-guru-ko-design-patterns]
---

# 템플릿 메서드 (Template Method)

상위 클래스가 알고리즘 골격을 정의하고, 일부 단계를 하위 클래스가 오버라이드하게 한다. [[design-patterns]]의 행동 패턴에 속하며, 원문 기준 URL은 `https://refactoring.guru/ko/design-patterns/template-method`이다.

## 문제 신호

전체 절차는 안정적이지만 일부 단계만 변하고, 절차 순서를 강제하고 싶을 때.

## 구조

AbstractClass의 template method가 단계 순서를 고정하고 abstract/hook operation을 호출한다. ConcreteClass가 변하는 단계를 구현한다.

## 적용 메모

- 클라이언트가 구상 타입이나 구체 협력자를 직접 알아야 하는 지점을 줄이는 데 초점을 둔다.
- 패턴명보다 중요한 것은 변경 축이다. 변경 축이 없거나 단순하면 일반 함수/클래스/언어 기능으로 충분할 수 있다.
- 테스트에서는 패턴이 만든 seam을 활용해 구상 구현 대신 fake/mock을 주입할 수 있는지 확인한다.

## 장단점

중복을 줄이고 알고리즘 순서를 보장한다. 상속 결합이 강하고 hook이 많아지면 이해하기 어렵다.

## 관련 패턴

[[design-pattern-strategy]]가 composition으로 알고리즘을 바꾸는 반면 Template Method는 inheritance 기반이다. [[design-pattern-factory-method]]가 template step으로 들어갈 수 있다.

## References

- [[refactoring-guru-ko-design-patterns]] — 템플릿 메서드 원문: https://refactoring.guru/ko/design-patterns/template-method
- [[design-patterns]]
