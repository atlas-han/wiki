---
title: 빌더 (Builder)
type: engineering
tags: [engineering, design-patterns, gof, creational]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [design-patterns, design-pattern-factory-method, design-pattern-abstract-factory, design-pattern-prototype]
first-seen: refactoring-guru-ko-design-patterns
sources: [refactoring-guru-ko-design-patterns]
---

# 빌더 (Builder)

복잡한 객체 생성 과정을 단계별로 분리해 같은 절차로 서로 다른 표현을 만들게 한다. [[design-patterns]]의 생성 패턴에 속하며, 원문 기준 URL은 `https://refactoring.guru/ko/design-patterns/builder`이다.

## 문제 신호

생성자 파라미터가 많거나 optional 조합이 폭발하고, 생성 순서/검증/표현 분리가 필요할 때.

## 구조

Director가 생성 순서를 알고, Builder 인터페이스가 단계별 build operation을 제공하며 ConcreteBuilder가 결과 표현을 조립한다.

## 적용 메모

- 클라이언트가 구상 타입이나 구체 협력자를 직접 알아야 하는 지점을 줄이는 데 초점을 둔다.
- 패턴명보다 중요한 것은 변경 축이다. 변경 축이 없거나 단순하면 일반 함수/클래스/언어 기능으로 충분할 수 있다.
- 테스트에서는 패턴이 만든 seam을 활용해 구상 구현 대신 fake/mock을 주입할 수 있는지 확인한다.

## 장단점

생성 과정을 명시적으로 모델링하고 불변/복합 객체를 안전하게 만들 수 있다. 단순 객체에는 보일러플레이트가 늘어난다.

## 관련 패턴

[[design-pattern-abstract-factory]]가 제품군 생성을 담당한다면 Builder는 한 복잡한 제품의 조립 절차에 집중한다. [[design-pattern-composite]] 구조 생성에 자주 쓰인다.

## References

- [[refactoring-guru-ko-design-patterns]] — 빌더 원문: https://refactoring.guru/ko/design-patterns/builder
- [[design-patterns]]
