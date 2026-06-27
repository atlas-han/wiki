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

객체들이 서로 직접 참조하지 못하게 하고 중재자 객체를 통해서만 상호작용하게 하여, 객체 간의 혼란스러운 의존 관계를 줄이는 패턴이다. [[design-patterns]]의 행동 패턴에 속한다.

## 문제

폼(form) 안의 UI 요소들처럼 객체들이 서로 직접 통신하면 상호작용이 복잡해지고 결합도가 강해진다. 한 요소를 변경하면 그와 연결된 다른 요소들에 연쇄적으로 영향이 가고, 특정 요소들이 서로 단단히 얽혀 다른 폼에서 재사용하기 어려워진다.

## 해결책

컴포넌트들이 서로를 직접 호출하지 않고 중재자(mediator) 객체를 통해 간접적으로 통신하도록 강제한다. 각 컴포넌트는 다른 컴포넌트가 아니라 중재자 인터페이스에만 의존하며, ConcreteMediator가 컴포넌트 참조를 보유하고 협업 규칙을 한곳에서 관리한다. 그 결과 컴포넌트 간 의존성이 중재자로 모여 결합도가 크게 낮아진다.

## 실세계 비유

공항 관제탑에 비유할 수 있다. 조종사들은 다음에 누가 착륙할지를 정하기 위해 서로 직접 대화하지 않는다. 모든 통신은 관제탑을 거치며, 관제탑이 항공기들의 상호작용을 조정한다.

## 적용 가능성

- 일부 클래스들이 다른 클래스들과 단단히 결합되어 변경하기 어려울 때
- 다른 객체에 대한 의존성이 너무 많아 어떤 컴포넌트를 다른 프로그램에서 재사용할 수 없을 때
- 어떤 기본 행동을 여러 콘텍스트에서 재사용하려고 수많은 컴포넌트 서브클래스를 만들고 있을 때

## 장단점

**장점**
- 단일 책임 원칙(SRP): 컴포넌트 간 통신 로직을 한곳으로 모은다.
- 개방/폐쇄 원칙(OCP): 컴포넌트를 바꾸지 않고 새 중재자를 도입할 수 있다.
- 컴포넌트 간 결합도를 낮추고 개별 컴포넌트의 재사용성을 높인다.

**단점**
- 시간이 지나면 중재자가 모든 것을 아는 전지전능한 객체(god object)로 비대해질 수 있다.

## 다른 패턴과의 관계

- [[design-pattern-chain-of-responsibility]], [[design-pattern-command]], [[design-pattern-observer]]와 함께 발신자-수신자 연결을 다루지만, 중재자는 컴포넌트 간 통신을 중앙으로 모은다.
- [[design-pattern-observer]]와 자주 비교되며, 실제로 옵서버를 이용해 중재자를 구현하기도 한다. 중재자는 협업 조정 로직 중앙화가, 옵서버는 단방향 이벤트 구독·통지가 핵심이다.
- [[design-pattern-facade]]와 닮았지만, 퍼사드는 하위 시스템에 대한 단순 인터페이스만 제공하고 객체들끼리 여전히 직접 통신할 수 있는 반면, 중재자는 컴포넌트 간 통신 자체를 자기에게로 집중시킨다.

## References

- [[refactoring-guru-ko-design-patterns]] — 중재자 원문: https://refactoring.guru/ko/design-patterns/mediator
- [[design-patterns]]
