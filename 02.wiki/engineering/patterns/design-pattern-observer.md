---
title: 옵서버 (Observer)
type: engineering
tags: [engineering, design-patterns, gof, behavioral]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [design-patterns, design-pattern-chain-of-responsibility, design-pattern-command, design-pattern-iterator]
first-seen: refactoring-guru-ko-design-patterns
sources: [refactoring-guru-ko-design-patterns]
---

# 옵서버 (Observer)

주체 상태 변화가 여러 구독자에게 자동 통지되도록 일대다 의존성을 만든다. [[design-patterns]]의 행동 패턴에 속하며, 원문 기준 URL은 `https://refactoring.guru/ko/design-patterns/observer`이다.

## 문제 신호

이벤트 발행자와 여러 반응자를 분리하고, subscriber가 동적으로 늘고 줄어야 할 때.

## 구조

Subject가 subscribe/unsubscribe/notify를 제공하고 Observer가 update를 구현한다. ConcreteSubject는 상태 변경 시 통지한다.

## 적용 메모

- 클라이언트가 구상 타입이나 구체 협력자를 직접 알아야 하는 지점을 줄이는 데 초점을 둔다.
- 패턴명보다 중요한 것은 변경 축이다. 변경 축이 없거나 단순하면 일반 함수/클래스/언어 기능으로 충분할 수 있다.
- 테스트에서는 패턴이 만든 seam을 활용해 구상 구현 대신 fake/mock을 주입할 수 있는지 확인한다.

## 장단점

발행자와 구독자를 느슨하게 결합한다. 순서, 중복, memory leak, cascading update를 관리해야 한다.

## 관련 패턴

[[design-pattern-mediator]]는 협업 로직 중앙화, Observer는 event broadcast. [[design-pattern-command]]를 event payload/action으로 보낼 수 있다.

## References

- [[refactoring-guru-ko-design-patterns]] — 옵서버 원문: https://refactoring.guru/ko/design-patterns/observer
- [[design-patterns]]
