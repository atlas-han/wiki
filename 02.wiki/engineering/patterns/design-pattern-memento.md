---
title: 메멘토 (Memento)
type: engineering
tags: [engineering, design-patterns, gof, behavioral]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [design-patterns, design-pattern-chain-of-responsibility, design-pattern-command, design-pattern-iterator]
first-seen: refactoring-guru-ko-design-patterns
sources: [refactoring-guru-ko-design-patterns]
---

# 메멘토 (Memento)

객체의 캡슐화를 깨지 않고 내부 상태 snapshot을 저장·복원한다. [[design-patterns]]의 행동 패턴에 속하며, 원문 기준 URL은 `https://refactoring.guru/ko/design-patterns/memento`이다.

## 문제 신호

undo/redo, checkpoint, rollback이 필요하지만 외부에 내부 상태를 노출하고 싶지 않을 때.

## 구조

Originator가 Memento를 만들고 복원하며, Caretaker는 memento를 저장만 하고 내부를 해석하지 않는다.

## 적용 메모

- 클라이언트가 구상 타입이나 구체 협력자를 직접 알아야 하는 지점을 줄이는 데 초점을 둔다.
- 패턴명보다 중요한 것은 변경 축이다. 변경 축이 없거나 단순하면 일반 함수/클래스/언어 기능으로 충분할 수 있다.
- 테스트에서는 패턴이 만든 seam을 활용해 구상 구현 대신 fake/mock을 주입할 수 있는지 확인한다.

## 장단점

캡슐화를 지키며 상태 복원이 가능하다. snapshot 크기와 lifecycle 관리, mutable reference 누수에 주의해야 한다.

## 관련 패턴

[[design-pattern-command]]의 undo와 결합되며, [[design-pattern-prototype]]은 복제 생성이 목적이고 Memento는 상태 복원이 목적이다.

## References

- [[refactoring-guru-ko-design-patterns]] — 메멘토 원문: https://refactoring.guru/ko/design-patterns/memento
- [[design-patterns]]
