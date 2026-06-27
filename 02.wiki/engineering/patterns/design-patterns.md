---
title: 디자인 패턴
type: engineering
tags: [engineering, design-patterns, gof]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [design-pattern-factory-method, design-pattern-abstract-factory, design-pattern-builder, design-pattern-adapter, design-pattern-strategy, design-pattern-observer]
first-seen: refactoring-guru-ko-design-patterns
sources: [refactoring-guru-ko-design-patterns]
---

# 디자인 패턴

디자인 패턴은 소프트웨어 설계에서 반복적으로 등장하는 문제와 그 해결 구조에 붙인 이름이다. [[refactoring-guru-ko-design-patterns]] 기준으로 생성·구조·행동 패턴 22개를 정리했으며, 핵심은 “코드 복붙 템플릿”이 아니라 **변경 축을 분리하고 결합도를 낮추는 설계 vocabulary**다.

## 분류 맵

### 생성 패턴 — 객체 생성 책임 분리

- [[design-pattern-factory-method]] — 생성 메서드를 하위 클래스로 열어 제품 타입을 바꾼다.
- [[design-pattern-abstract-factory]] — 관련 제품군을 구상 클래스 없이 생성한다.
- [[design-pattern-builder]] — 복잡한 객체를 단계적으로 조립한다.
- [[design-pattern-prototype]] — 기존 객체 복제로 새 객체를 만든다.
- [[design-pattern-singleton]] — 인스턴스를 하나로 제한하고 전역 접근점을 제공한다.

### 구조 패턴 — 객체 조합과 인터페이스 정리

- [[design-pattern-adapter]] — 맞지 않는 인터페이스를 맞춘다.
- [[design-pattern-bridge]] — 추상화와 구현 축을 분리한다.
- [[design-pattern-composite]] — leaf와 tree를 같은 인터페이스로 다룬다.
- [[design-pattern-decorator]] — wrapper로 런타임 기능을 추가한다.
- [[design-pattern-facade]] — 복잡한 하위 시스템의 단순 진입점을 만든다.
- [[design-pattern-flyweight]] — 공유 가능한 상태를 분리해 메모리를 줄인다.
- [[design-pattern-proxy]] — 대리 객체로 접근을 제어한다.

### 행동 패턴 — 객체 간 책임과 흐름 분배

- [[design-pattern-chain-of-responsibility]] — 요청을 handler chain으로 흘려보낸다.
- [[design-pattern-command]] — 요청을 객체로 캡슐화한다.
- [[design-pattern-iterator]] — 내부 구조 노출 없이 순회한다.
- [[design-pattern-mediator]] — 객체 간 통신을 중재자에 모은다.
- [[design-pattern-memento]] — 캡슐화를 깨지 않고 snapshot을 저장/복원한다.
- [[design-pattern-observer]] — 상태 변화를 구독자들에게 통지한다.
- [[design-pattern-state]] — 상태별 행동을 객체로 분리한다.
- [[design-pattern-strategy]] — 알고리즘군을 교체 가능하게 캡슐화한다.
- [[design-pattern-template-method]] — 알고리즘 골격은 고정하고 일부 단계를 열어둔다.
- [[design-pattern-visitor]] — 객체 구조 변경 없이 새 operation을 추가한다.

## 적용 원칙

- 먼저 변경 축을 식별한다: 생성 타입, 플랫폼 구현, wrapper 기능, 상태 전이, 알고리즘 선택, 이벤트 전파 등.
- 패턴은 간접 계층을 추가하므로 **변경 가능성이 실제로 존재할 때** 적용한다.
- 현대 언어 기능(DI, closure, iterator protocol, algebraic data type, trait/interface default method)이 일부 패턴의 보일러플레이트를 줄인다.
- [[design-pattern-singleton]]처럼 전역 상태를 만드는 패턴은 테스트성과 동시성 비용을 먼저 검토한다.

## References

- [[refactoring-guru-ko-design-patterns]]
