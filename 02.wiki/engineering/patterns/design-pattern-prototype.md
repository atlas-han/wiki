---
title: 프로토타입 (Prototype)
type: engineering
tags: [engineering, design-patterns, gof, creational]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [design-patterns, design-pattern-factory-method, design-pattern-abstract-factory, design-pattern-builder]
first-seen: refactoring-guru-ko-design-patterns
sources: [refactoring-guru-ko-design-patterns]
---

# 프로토타입 (Prototype)

기존 객체를 복제해서 새 객체를 만들며, 생성 코드를 구상 클래스와 분리한다. [[design-patterns]]의 생성 패턴에 속하며, 원문 기준 URL은 `https://refactoring.guru/ko/design-patterns/prototype`이다.

## 문제 신호

객체 생성 비용이 크거나 런타임에 구상 타입이 결정되고, 클래스별 생성 로직을 클라이언트에 노출하고 싶지 않을 때.

## 구조

Prototype 인터페이스가 clone을 제공하고 ConcretePrototype이 자기 상태 복제를 구현한다. Registry를 두면 이름으로 prototype을 찾을 수 있다.

## 적용 메모

- 클라이언트가 구상 타입이나 구체 협력자를 직접 알아야 하는 지점을 줄이는 데 초점을 둔다.
- 패턴명보다 중요한 것은 변경 축이다. 변경 축이 없거나 단순하면 일반 함수/클래스/언어 기능으로 충분할 수 있다.
- 테스트에서는 패턴이 만든 seam을 활용해 구상 구현 대신 fake/mock을 주입할 수 있는지 확인한다.

## 장단점

상속 계층을 몰라도 객체를 만들 수 있고 초기화 비용을 재사용한다. 순환 참조/깊은 복사 정책은 까다롭다.

## 관련 패턴

[[design-pattern-factory-method]]의 subclass 폭발을 줄이는 대안이 될 수 있고, [[design-pattern-memento]]와 달리 외부 복원용 snapshot이 아니라 새 객체 생성을 목표로 한다.

## References

- [[refactoring-guru-ko-design-patterns]] — 프로토타입 원문: https://refactoring.guru/ko/design-patterns/prototype
- [[design-patterns]]
