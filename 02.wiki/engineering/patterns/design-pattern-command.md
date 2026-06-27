---
title: 커맨드 (Command)
type: engineering
tags: [engineering, design-patterns, gof, behavioral]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [design-patterns, design-pattern-chain-of-responsibility, design-pattern-iterator, design-pattern-mediator]
first-seen: refactoring-guru-ko-design-patterns
sources: [refactoring-guru-ko-design-patterns]
---

# 커맨드 (Command)

요청을, 그 요청에 필요한 모든 정보를 담은 독립실행형 객체로 변환하는 패턴이다. [[design-patterns]]의 행동 패턴에 속한다.

## 문제

텍스트 편집기의 여러 버튼이 각기 다른 기능을 수행해야 할 때, 기능마다 버튼 자식 클래스를 만들면 클래스 수가 폭발하고, 복사·붙여넣기처럼 같은 작업이 버튼·메뉴·단축키 여러 곳에서 호출되면 코드가 중복된다. 결국 GUI 코드가 비즈니스 로직에 직접적이고 불안정하게 의존하게 된다.

## 해결책

GUI 객체가 비즈니스 로직 객체에 직접 요청을 보내는 대신, 요청 세부 정보를 별도의 커맨드(command) 클래스로 추출한다. 모든 커맨드는 동일한 인터페이스(보통 `execute()`)를 구현하며, ConcreteCommand는 receiver와 인자를 보유한다. Invoker는 어떤 커맨드인지 모른 채 실행만 하므로 GUI와 비즈니스 로직의 결합도가 낮아진다.

## 실세계 비유

식당 주문서에 비유할 수 있다. 웨이터가 주문을 종이에 적어 부엌에 붙이면 요리사는 그 종이 주문을 읽고 요리한다. 종이에 적힌 주문이 커맨드 역할을 하며, 요리사가 고객으로부터 직접 주문을 받지 않아도 작업이 전달된다.

## 적용 가능성

- 작업(operation)으로 객체를 매개변수화하고 싶을 때
- 작업의 실행을 예약하거나 대기열에 넣거나 원격으로 실행하고 싶을 때
- 되돌릴 수 있는 작업(실행 취소/다시 실행)을 구현하고 싶을 때

## 장단점

**장점**
- 단일 책임 원칙(SRP): 작업을 호출하는 클래스와 수행하는 클래스를 분리한다.
- 개방/폐쇄 원칙(OCP): 기존 코드를 손상시키지 않고 새 커맨드를 추가할 수 있다.
- 실행 취소/다시 실행과 작업의 지연 실행을 구현할 수 있고, 단순 커맨드를 묶어 복잡한 커맨드로 조합할 수 있다.

**단점**
- 발송자와 수신자 사이에 새 레이어가 생겨 코드 복잡성이 증가한다.

## 다른 패턴과의 관계

- [[design-pattern-chain-of-responsibility]], [[design-pattern-mediator]], [[design-pattern-observer]]와 함께 요청 발신자-수신자 연결을 다루며, 핸들러 자체를 커맨드로 구현할 수도 있다.
- [[design-pattern-memento]]와 함께 쓰면 실행 취소를 구현할 수 있다(작업 전 상태를 메멘토로 저장).
- [[design-pattern-strategy]]와 구조가 유사하지만, 전략은 알고리즘 교체가, 커맨드는 작업의 객체화가 의도다.
- [[design-pattern-prototype]]은 커맨드 히스토리에 저장할 복사본을 만드는 데 도움이 된다.

## References

- [[refactoring-guru-ko-design-patterns]] — 커맨드 원문: https://refactoring.guru/ko/design-patterns/command
- [[design-patterns]]
