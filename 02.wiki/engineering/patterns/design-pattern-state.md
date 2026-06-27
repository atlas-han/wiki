---
title: 상태 (State)
type: engineering
tags: [engineering, design-patterns, gof, behavioral]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [design-patterns, design-pattern-chain-of-responsibility, design-pattern-command, design-pattern-iterator]
first-seen: refactoring-guru-ko-design-patterns
sources: [refactoring-guru-ko-design-patterns]
---

# 상태 (State)

객체의 내부 상태가 변경될 때 그 객체가 행동을 바꿀 수 있도록, 마치 객체의 클래스가 바뀐 것처럼 동작하게 하는 패턴이다. [[design-patterns]]의 행동 패턴에 속한다.

## 문제
상태에 따라 다르게 동작하는 객체를 구현하면 메서드 곳곳에 상태를 분기하는 조건문이 늘어난다. 예를 들어 문서 객체가 초안·검토·출판 상태를 가지고 각 상태에서 `publish` 메서드가 다르게 작동해야 한다면, 상태 수와 전이 규칙이 늘수록 조건문이 비대해진다. 이런 코드는 유지보수가 어렵고, 새 상태나 전이 규칙을 추가할 때마다 기존 메서드를 모두 수정해야 한다.

## 해결책
가능한 각 상태마다 별도의 클래스(ConcreteState)를 만들고, 상태별 행동을 그 클래스로 추출한다. 원래 객체(Context)는 현재 상태 객체에 대한 참조를 들고 모든 상태 의존적 작업을 그 상태 객체에 위임한다. 다른 상태로 전환하려면 Context가 참조하는 상태 객체를 교체하면 되며, 상태 전이는 Context나 상태 객체 스스로가 주도할 수 있다.

## 실세계 비유
스마트폰의 버튼과 스위치는 장치의 현재 상태에 따라 다르게 행동한다. 잠금이 해제된 상태에서 버튼을 누르면 다양한 기능이 실행되지만, 잠긴 상태에서는 어떤 버튼을 눌러도 잠금 해제 화면이 나타난다. 같은 입력이라도 현재 상태에 따라 결과가 달라진다.

## 적용 가능성
- 객체가 현재 상태에 따라 다르게 행동해야 하고, 상태의 수가 많으며 상태별 코드가 자주 바뀔 때
- 클래스 필드의 현재 값에 따라 객체가 어떻게 행동하는지를 결정하는 거대한 조건문으로 코드가 오염되었을 때
- 유사한 상태들에 걸쳐 중복된 코드와 조건 기반 상태 머신의 전이가 많을 때

## 장단점
**장점**
- 특정 상태와 관련된 코드를 별도 클래스로 모은다 (단일 책임 원칙)
- Context나 다른 상태를 변경하지 않고 새 상태를 도입할 수 있다 (개방/폐쇄 원칙)
- 거대한 상태 머신 조건문을 제거해 Context 코드를 단순화한다

**단점**
- 상태가 몇 개뿐이고 거의 변하지 않는다면 패턴 적용이 과도할 수 있다

## 다른 패턴과의 관계
- [[design-pattern-strategy]]와 구조가 거의 동일하지만 의도가 다르다. State는 상태 객체들이 서로를 인식하며 상태 전이를 스스로 주도하는 반면, Strategy의 알고리즘들은 서로를 전혀 알지 못한다. 그래서 State는 Strategy의 확장으로 볼 수 있다
- [[design-pattern-bridge]], [[design-pattern-adapter]]와 합성 기반의 유사한 구조를 공유하지만 해결하는 문제가 다르다

## References
- [[refactoring-guru-ko-design-patterns]] — 상태 (State) 원문: https://refactoring.guru/ko/design-patterns/state
- [[design-patterns]]
