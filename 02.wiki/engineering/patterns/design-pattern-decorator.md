---
title: 데코레이터 (Decorator)
type: engineering
tags: [engineering, design-patterns, gof, structural]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [design-patterns, design-pattern-adapter, design-pattern-bridge, design-pattern-composite]
first-seen: refactoring-guru-ko-design-patterns
sources: [refactoring-guru-ko-design-patterns]
---

# 데코레이터 (Decorator)

객체를 wrapper로 감싸 런타임에 책임을 동적으로 추가한다. [[design-patterns]]의 구조 패턴에 속하며, 원문 기준 URL은 `https://refactoring.guru/ko/design-patterns/decorator`이다.

## 문제 신호

상속으로 기능 조합을 만들면 조합 폭발이 발생하고, 개별 객체 단위로 기능을 켜고 끄고 싶을 때.

## 구조

Decorator가 Component 인터페이스를 구현하고 내부 Component에 위임한 뒤 전/후처리를 추가한다.

## 적용 메모

- 클라이언트가 구상 타입이나 구체 협력자를 직접 알아야 하는 지점을 줄이는 데 초점을 둔다.
- 패턴명보다 중요한 것은 변경 축이다. 변경 축이 없거나 단순하면 일반 함수/클래스/언어 기능으로 충분할 수 있다.
- 테스트에서는 패턴이 만든 seam을 활용해 구상 구현 대신 fake/mock을 주입할 수 있는지 확인한다.

## 장단점

기능 조합이 유연하고 Open/Closed Principle에 맞다. wrapper 체인이 길어지면 디버깅과 동일성 비교가 어려워진다.

## 관련 패턴

[[design-pattern-proxy]]와 구조가 비슷하지만 Decorator는 기능 확장, Proxy는 접근 제어/지연/원격 대리 목적이다. [[design-pattern-chain-of-responsibility]]처럼 wrapper chain을 만들 수 있다.

## References

- [[refactoring-guru-ko-design-patterns]] — 데코레이터 원문: https://refactoring.guru/ko/design-patterns/decorator
- [[design-patterns]]
