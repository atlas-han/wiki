---
title: 책임 연쇄 (Chain of Responsibility)
type: engineering
tags: [engineering, design-patterns, gof, behavioral]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [design-patterns, design-pattern-command, design-pattern-iterator, design-pattern-mediator, actix-web-routing]
first-seen: refactoring-guru-ko-design-patterns
sources: [refactoring-guru-ko-design-patterns]
---

# 책임 연쇄 (Chain of Responsibility)

핸들러들의 체인(chain)을 따라 요청을 전달해, 각 핸들러가 요청을 처리하거나 다음 핸들러로 넘기도록 하는 패턴이다. [[design-patterns]]의 행동 패턴에 속한다.

## 문제

온라인 주문 시스템처럼 하나의 요청에 인증, 데이터 검증, 공격 방어, 캐싱 등 여러 검사를 순차적으로 수행해야 하는 경우가 있다. 검사를 추가할 때마다 코드가 한곳에서 비대해지고 복잡해지며 유지보수 비용이 커진다. 또한 다른 컴포넌트에서 같은 검사를 재사용하려면 코드를 복제해야 하는 문제가 생긴다.

## 해결책

각 검사를 독립적인 핸들러(handler) 클래스로 분리하고, 이들을 체인으로 연결한다. Handler는 다음 핸들러에 대한 참조와 `handle(request)` 메서드를 가지며, ConcreteHandler는 요청을 처리할 수 있으면 처리하고 아니면 체인의 다음 핸들러로 전달한다. 이렇게 관심사를 분리해 sender와 receiver를 느슨하게 결합한다.

## 실세계 비유

기술 지원 전화에 비유할 수 있다. 문의는 "자동 응답기 → 일반 교환원 → 엔지니어"로 이어지는 체인을 따라 흐르며, 각 단계는 자기가 해결할 수 있으면 처리하고 그렇지 않으면 다음 담당자에게 넘긴다.

## 적용 가능성

- 다양한 종류의 요청을 여러 방식으로 처리해야 하지만 요청의 정확한 유형과 순서를 미리 알 수 없을 때
- 여러 핸들러를 정해진 순서로 실행해야 할 때
- 핸들러의 집합과 그 순서가 런타임에 바뀌어야 할 때

## 장단점

**장점**
- 요청 처리 순서를 제어할 수 있다.
- 단일 책임 원칙(SRP): 요청을 호출하는 클래스와 처리하는 클래스를 분리한다.
- 개방/폐쇄 원칙(OCP): 기존 코드를 수정하지 않고 새 핸들러를 체인에 추가할 수 있다.

**단점**
- 일부 요청은 체인 끝까지 처리되지 않을 수 있다.

## 다른 패턴과의 관계

- [[design-pattern-command]], [[design-pattern-mediator]], [[design-pattern-observer]]와 함께 요청 발신자와 수신자를 연결하는 방식을 다루지만, 책임 연쇄는 수신자가 처리할 때까지 요청을 순차 전달한다.
- [[design-pattern-composite]]와 자주 함께 쓰여, 자식이 처리하지 못한 요청을 부모로 올려보낼 수 있다.
- 체인을 구성하는 방식이 [[design-pattern-decorator]]와 구조적으로 닮았지만, 데코레이터는 흐름을 끊지 않고 책임 연쇄는 임의 핸들러가 처리를 멈출 수 있다.

## References

- [[refactoring-guru-ko-design-patterns]] — 책임 연쇄 원문: https://refactoring.guru/ko/design-patterns/chain-of-responsibility
- [[design-patterns]]
- 실무 예: [[actix-web-routing]] — 등록순 route/`Guard` 매칭(첫 매칭 처리, false면 다음으로)
