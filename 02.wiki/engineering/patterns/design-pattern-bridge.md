---
title: 브리지 (Bridge)
type: engineering
tags: [engineering, design-patterns, gof, structural]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [design-patterns, design-pattern-adapter, design-pattern-composite, design-pattern-decorator]
first-seen: refactoring-guru-ko-design-patterns
sources: [refactoring-guru-ko-design-patterns]
---

# 브리지 (Bridge)

추상화와 구현을 분리해 둘을 독립적으로 확장한다. [[design-patterns]]의 구조 패턴에 속하며, 원문 기준 URL은 `https://refactoring.guru/ko/design-patterns/bridge`이다.

## 문제 신호

기능 축과 플랫폼/구현 축이 동시에 변해 상속 조합이 폭발할 때.

## 구조

Abstraction은 Implementor 인터페이스를 참조하고, RefinedAbstraction과 ConcreteImplementor가 각 축을 독립적으로 확장한다.

## 적용 메모

- 클라이언트가 구상 타입이나 구체 협력자를 직접 알아야 하는 지점을 줄이는 데 초점을 둔다.
- 패턴명보다 중요한 것은 변경 축이다. 변경 축이 없거나 단순하면 일반 함수/클래스/언어 기능으로 충분할 수 있다.
- 테스트에서는 패턴이 만든 seam을 활용해 구상 구현 대신 fake/mock을 주입할 수 있는지 확인한다.

## 장단점

두 차원의 확장을 분리해 클래스 폭발을 줄인다. 초기 설계에서 축 분리가 명확하지 않으면 과설계가 될 수 있다.

## 관련 패턴

[[design-pattern-adapter]]는 사후 호환용인 경우가 많고 Bridge는 사전 설계용이다. [[design-pattern-strategy]]와 유사하게 composition으로 구현 변화를 캡슐화한다.

## References

- [[refactoring-guru-ko-design-patterns]] — 브리지 원문: https://refactoring.guru/ko/design-patterns/bridge
- [[design-patterns]]
