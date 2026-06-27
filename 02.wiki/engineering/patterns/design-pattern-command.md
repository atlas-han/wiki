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

요청을 객체로 캡슐화해 실행, 큐잉, 로깅, undo/redo를 가능하게 한다. [[design-patterns]]의 행동 패턴에 속하며, 원문 기준 URL은 `https://refactoring.guru/ko/design-patterns/command`이다.

## 문제 신호

작업을 나중에 실행하거나 기록/재시도/취소해야 하고 invoker와 receiver를 분리하고 싶을 때.

## 구조

Command 인터페이스가 execute를 정의하고 ConcreteCommand가 receiver와 action parameters를 보유한다. Invoker는 command만 실행한다.

## 적용 메모

- 클라이언트가 구상 타입이나 구체 협력자를 직접 알아야 하는 지점을 줄이는 데 초점을 둔다.
- 패턴명보다 중요한 것은 변경 축이다. 변경 축이 없거나 단순하면 일반 함수/클래스/언어 기능으로 충분할 수 있다.
- 테스트에서는 패턴이 만든 seam을 활용해 구상 구현 대신 fake/mock을 주입할 수 있는지 확인한다.

## 장단점

작업을 값처럼 다룰 수 있어 macro, queue, transaction, undo가 쉬워진다. 작은 작업마다 클래스/객체가 늘 수 있다.

## 관련 패턴

undo snapshot에는 [[design-pattern-memento]]가, UI/menu action 분리에는 [[design-pattern-observer]]나 [[design-pattern-mediator]]가 함께 쓰인다.

## References

- [[refactoring-guru-ko-design-patterns]] — 커맨드 원문: https://refactoring.guru/ko/design-patterns/command
- [[design-patterns]]
