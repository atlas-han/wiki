---
title: 중재자 (Mediator)
type: engineering
tags: [engineering, design-patterns, gof, behavioral]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [design-patterns, design-pattern-chain-of-responsibility, design-pattern-command, design-pattern-iterator]
first-seen: refactoring-guru-ko-design-patterns
sources: [refactoring-guru-ko-design-patterns]
---

# 중재자 (Mediator)

객체들이 서로 직접 참조하지 않고 mediator를 통해 상호작용하게 한다. [[design-patterns]]의 행동 패턴에 속하며, 원문 기준 URL은 `https://refactoring.guru/ko/design-patterns/mediator`이다.

## 문제 신호

UI component, workflow participant처럼 many-to-many 통신이 복잡해지고 객체들이 서로 강하게 결합될 때.

## 구조

Mediator 인터페이스가 component event를 받고, ConcreteMediator가 협업 규칙과 component 참조를 관리한다.

## 적용 메모

- 클라이언트가 구상 타입이나 구체 협력자를 직접 알아야 하는 지점을 줄이는 데 초점을 둔다.
- 패턴명보다 중요한 것은 변경 축이다. 변경 축이 없거나 단순하면 일반 함수/클래스/언어 기능으로 충분할 수 있다.
- 테스트에서는 패턴이 만든 seam을 활용해 구상 구현 대신 fake/mock을 주입할 수 있는지 확인한다.

## 장단점

객체 간 결합을 낮추고 협업 규칙을 한곳에 모은다. Mediator가 커지면 god object가 된다.

## 관련 패턴

[[design-pattern-observer]]는 이벤트 broadcast에 가깝고 Mediator는 협업 조정 로직을 중앙화한다. [[design-pattern-facade]]는 외부 단순화, Mediator는 내부 상호작용 제어다.

## References

- [[refactoring-guru-ko-design-patterns]] — 중재자 원문: https://refactoring.guru/ko/design-patterns/mediator
- [[design-patterns]]
