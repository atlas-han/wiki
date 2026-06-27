---
title: 전략 (Strategy)
type: engineering
tags: [engineering, design-patterns, gof, behavioral]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [design-patterns, design-pattern-chain-of-responsibility, design-pattern-command, design-pattern-iterator]
first-seen: refactoring-guru-ko-design-patterns
sources: [refactoring-guru-ko-design-patterns]
---

# 전략 (Strategy)

알고리즘군을 캡슐화해 런타임에 교체 가능하게 한다. [[design-patterns]]의 행동 패턴에 속하며, 원문 기준 URL은 `https://refactoring.guru/ko/design-patterns/strategy`이다.

## 문제 신호

조건문으로 알고리즘을 선택하거나, 같은 문제를 여러 방식으로 해결해야 할 때.

## 구조

Context가 Strategy 인터페이스를 참조하고 ConcreteStrategy가 알고리즘을 구현한다. 클라이언트나 context가 적절한 strategy를 선택한다.

## 적용 메모

- 클라이언트가 구상 타입이나 구체 협력자를 직접 알아야 하는 지점을 줄이는 데 초점을 둔다.
- 패턴명보다 중요한 것은 변경 축이다. 변경 축이 없거나 단순하면 일반 함수/클래스/언어 기능으로 충분할 수 있다.
- 테스트에서는 패턴이 만든 seam을 활용해 구상 구현 대신 fake/mock을 주입할 수 있는지 확인한다.

## 장단점

알고리즘 교체와 테스트가 쉬워지고 OCP에 맞다. strategy 수가 많으면 선택/구성이 별도 문제로 남는다.

## 관련 패턴

[[design-pattern-state]]와 구조는 유사하지만 전이 중심이 아니다. 생성은 [[design-pattern-factory-method]]나 DI와 함께 구성할 수 있다.

## References

- [[refactoring-guru-ko-design-patterns]] — 전략 원문: https://refactoring.guru/ko/design-patterns/strategy
- [[design-patterns]]
