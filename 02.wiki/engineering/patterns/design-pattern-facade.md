---
title: 퍼사드 (Facade)
type: engineering
tags: [engineering, design-patterns, gof, structural]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [design-patterns, design-pattern-adapter, design-pattern-bridge, design-pattern-composite]
first-seen: refactoring-guru-ko-design-patterns
sources: [refactoring-guru-ko-design-patterns]
---

# 퍼사드 (Facade)

복잡한 하위 시스템에 단순한 고수준 인터페이스를 제공한다. [[design-patterns]]의 구조 패턴에 속하며, 원문 기준 URL은 `https://refactoring.guru/ko/design-patterns/facade`이다.

## 문제 신호

라이브러리/프레임워크/레거시 시스템의 사용 진입점을 단순화하고 결합을 줄이고 싶을 때.

## 구조

Facade가 하위 시스템 객체들을 알고, 클라이언트가 자주 쓰는 workflow를 하나의 API로 묶는다.

## 적용 메모

- 클라이언트가 구상 타입이나 구체 협력자를 직접 알아야 하는 지점을 줄이는 데 초점을 둔다.
- 패턴명보다 중요한 것은 변경 축이다. 변경 축이 없거나 단순하면 일반 함수/클래스/언어 기능으로 충분할 수 있다.
- 테스트에서는 패턴이 만든 seam을 활용해 구상 구현 대신 fake/mock을 주입할 수 있는지 확인한다.

## 장단점

사용성·결합도·테스트 seam이 좋아진다. Facade가 너무 많은 책임을 흡수하면 god object가 된다.

## 관련 패턴

[[design-pattern-adapter]]가 인터페이스 변환이면 Facade는 단순화다. Facade 인스턴스는 [[design-pattern-singleton]]으로 제공될 수 있지만 전역 상태 비용을 주의한다.

## References

- [[refactoring-guru-ko-design-patterns]] — 퍼사드 원문: https://refactoring.guru/ko/design-patterns/facade
- [[design-patterns]]
