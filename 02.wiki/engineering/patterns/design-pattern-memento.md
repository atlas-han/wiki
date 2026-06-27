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

객체의 구현 세부 사항을 공개하지 않으면서 그 객체의 이전 상태를 저장하고 복원할 수 있게 하는 패턴이다. [[design-patterns]]의 행동 패턴에 속한다.

## 문제

텍스트 편집기에서 실행 취소 기능을 구현하려면 모든 작업 직전에 객체의 상태를 어딘가에 저장해 두어야 한다. 그러나 다른 객체가 대상 객체의 비공개 필드에 직접 접근하면 캡슐화가 깨지고, 객체의 내부 구조가 바뀔 때마다 상태를 복사하는 로직도 함께 고쳐야 하는 문제가 생긴다.

## 해결책

상태 스냅샷 생성을, 그 상태의 실제 소유자인 오리지네이터(originator)에게 위임한다. 오리지네이터는 자신의 상태를 메멘토(memento)라는 특수 객체에 담아 만들고, 메멘토의 내용에는 오리지네이터만 접근할 수 있다. 케어테이커(caretaker)는 메멘토를 보관하고 주고받기만 할 뿐 그 내용을 해석하지 못하므로 캡슐화가 유지된다.

## 실세계 비유

이 패턴 페이지에는 명시적인 실세계 유추가 없다. 대신 본문은 텍스트 편집기의 실행 취소(undo)를 예시로 든다. 편집기는 글자를 입력하거나 지우기 전 매 작업 직전에 현재 문서 상태의 스냅샷을 메멘토로 보관해 두고, 사용자가 실행 취소를 누르면 가장 최근 스냅샷을 꺼내 이전 상태로 되돌린다.

## 적용 가능성

- 객체의 이전 상태로 되돌릴 수 있도록 상태 스냅샷을 만들고 싶을 때(실행 취소 등)
- 트랜잭션 처리 중 오류가 나면 작업을 롤백해야 할 때
- 객체의 필드/게터/세터에 직접 접근하는 방식이 객체의 캡슐화를 위반할 때

## 장단점

**장점**
- 캡슐화를 위반하지 않고도 객체 상태의 스냅샷을 만들 수 있다.
- 상태 기록 보관을 케어테이커에게 맡겨 오리지네이터 코드를 단순하게 유지한다.

**단점**
- 클라이언트가 메멘토를 너무 자주 생성하면 RAM 소모가 커진다.
- 케어테이커는 쓸모없어진 메멘토를 파괴하기 위해 오리지네이터의 수명주기를 추적해야 한다.
- PHP, 파이썬, JavaScript 같은 동적 언어에서는 메멘토 내부 상태가 변경되지 않음을 언어 차원에서 보장하기 어렵다.

## 다른 패턴과의 관계

- [[design-pattern-command]]와 함께 실행 취소를 구현할 때 자주 쓰인다. 커맨드는 작업을, 메멘토는 작업 직전의 객체 상태를 담당한다.
- [[design-pattern-iterator]]와 함께 쓰면 현재 순회 상태를 포착해 두었다가 필요할 때 롤백할 수 있다.
- [[design-pattern-prototype]]은 상태 복사가 단순한 객체라면 메멘토의 더 간단한 대안이 될 수 있다.

## References

- [[refactoring-guru-ko-design-patterns]] — 메멘토 원문: https://refactoring.guru/ko/design-patterns/memento
- [[design-patterns]]
