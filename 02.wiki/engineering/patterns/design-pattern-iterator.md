---
title: 반복자 (Iterator)
type: engineering
tags: [engineering, design-patterns, gof, behavioral]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [design-patterns, design-pattern-chain-of-responsibility, design-pattern-command, design-pattern-mediator]
first-seen: refactoring-guru-ko-design-patterns
sources: [refactoring-guru-ko-design-patterns]
---

# 반복자 (Iterator)

컬렉션 내부 표현을 노출하지 않고 요소를 순차 접근한다. [[design-patterns]]의 행동 패턴에 속하며, 원문 기준 URL은 `https://refactoring.guru/ko/design-patterns/iterator`이다.

## 문제 신호

트리/그래프/복합 컬렉션의 순회 알고리즘을 컬렉션 밖으로 분리하고 싶을 때.

## 구조

Iterator가 next/current/hasNext를 제공하고 ConcreteIterator가 순회 상태를 보유한다. Aggregate는 iterator factory를 제공한다.

## 적용 메모

- 클라이언트가 구상 타입이나 구체 협력자를 직접 알아야 하는 지점을 줄이는 데 초점을 둔다.
- 패턴명보다 중요한 것은 변경 축이다. 변경 축이 없거나 단순하면 일반 함수/클래스/언어 기능으로 충분할 수 있다.
- 테스트에서는 패턴이 만든 seam을 활용해 구상 구현 대신 fake/mock을 주입할 수 있는지 확인한다.

## 장단점

컬렉션과 순회 알고리즘을 분리하고 여러 순회를 동시에 둘 수 있다. 단순 자료구조에는 언어 내장 iterator로 충분하다.

## 관련 패턴

[[design-pattern-composite]] 트리 순회에 자주 쓰이고, 순회 중 operation 추가는 [[design-pattern-visitor]]와 대비된다.

## References

- [[refactoring-guru-ko-design-patterns]] — 반복자 원문: https://refactoring.guru/ko/design-patterns/iterator
- [[design-patterns]]
