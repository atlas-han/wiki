---
title: Switch Statements
type: engineering
tags: [engineering, refactoring]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [code-smells, refactoring-techniques, technical-debt]
first-seen: refactoring-guru-refactoring
sources: [refactoring-guru-refactoring]
---

# Switch Statements

복잡한 `switch` 문이나 `if` 연쇄가 타입·상태별로 분기하며 프로그램 곳곳에 흩어져 있는 상태다. [[code-smells]] 중 **객체지향 남용** 계열이다.

## 신호와 증상
- 복잡한 `switch` 연산자 또는 긴 `if`/`else if` 연쇄가 존재한다.
- 같은 분기 로직(같은 타입 코드에 대한 `case` 묶음)이 프로그램 여러 위치에 중복되어 나타난다.
- 새로운 조건(타입·변형)을 추가할 때 흩어진 모든 `switch`를 찾아 함께 고쳐야 한다 ([[shotgun-surgery]]로 번지기 쉽다).

## 원인
객체지향 코드에서는 `switch`/`case`가 상대적으로 드물어야 한다. 다형성으로 풀 수 있는 분기를 절차적으로 작성하면 동일한 조건 분기가 곳곳에 복제된다.

## 해결 방법 (Treatment)
- `Extract Method` + `Move Method` — `switch` 블록을 떼어내 책임이 맞는 클래스로 옮긴다.
- `Replace Type Code with Subclasses` — 타입 코드가 객체 행동을 가른다면 서브클래스로 치환한다.
- `Replace Type Code with State/Strategy` — 타입 코드가 런타임에 바뀌거나 다른 이유로 서브클래싱이 어렵다면 상태/전략 객체로 치환한다. [[design-pattern-state]]·[[design-pattern-strategy]]와 연결된다.
- `Replace Conditional with Polymorphism` — 위로 클래스 계층이 갖춰지면 조건 분기를 다형 메서드 호출로 대체해 `switch`를 제거한다.
- `Replace Parameter with Explicit Methods` — 매개변수 값으로 동작이 갈리면 명시적 메서드들로 분리한다.
- `Introduce Null Object` — `null` 여부를 검사하는 분기를 널 객체로 대체한다.

## 이득 (Payoff)
- 분기가 한 곳(다형 계층)으로 모여 새 변형 추가 시 클래스 하나만 더하면 된다.
- 조건 검사 중복이 사라져 코드가 짧고 의도가 드러난다.
- 개방-폐쇄 원칙(OCP)에 가까워진다.

## 무시해도 될 때
`switch`가 단순한 작업만 수행하거나, `Factory Method`·`Abstract Factory`처럼 어떤 클래스를 생성할지 고르는 자리에서 쓰일 때는 그대로 두는 편이 낫다.

## References
- [[refactoring-guru-refactoring]] — Switch Statements 원문: https://refactoring.guru/smells/switch-statements
- [[code-smells]]
