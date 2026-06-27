---
title: 어댑터 (Adapter)
type: engineering
tags: [engineering, design-patterns, gof, structural]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [design-patterns, design-pattern-bridge, design-pattern-composite, design-pattern-decorator]
first-seen: refactoring-guru-ko-design-patterns
sources: [refactoring-guru-ko-design-patterns]
---

# 어댑터 (Adapter)

호환되지 않는 인터페이스를 클라이언트가 기대하는 인터페이스로 변환한다. [[design-patterns]]의 구조 패턴에 속하며, 원문 기준 URL은 `https://refactoring.guru/ko/design-patterns/adapter`이다.

## 문제 신호

레거시/외부 라이브러리/서드파티 API를 기존 도메인 인터페이스 뒤에 붙이고 싶을 때.

## 구조

Adapter가 Target 인터페이스를 구현하고 내부에서 Adaptee 호출을 변환한다. object adapter는 composition, class adapter는 inheritance를 쓴다.

## 적용 메모

- 클라이언트가 구상 타입이나 구체 협력자를 직접 알아야 하는 지점을 줄이는 데 초점을 둔다.
- 패턴명보다 중요한 것은 변경 축이다. 변경 축이 없거나 단순하면 일반 함수/클래스/언어 기능으로 충분할 수 있다.
- 테스트에서는 패턴이 만든 seam을 활용해 구상 구현 대신 fake/mock을 주입할 수 있는지 확인한다.

## 장단점

기존 코드를 수정하지 않고 통합할 수 있다. 변환 계층이 늘어 복잡도가 증가하고, 잘못 쓰면 도메인 모델 누수가 생긴다.

## 관련 패턴

[[design-pattern-facade]]가 하위 시스템을 단순화한다면 Adapter는 인터페이스 호환성에 초점을 둔다. [[design-pattern-decorator]]와 구조는 비슷하지만 목적이 다르다.

## References

- [[refactoring-guru-ko-design-patterns]] — 어댑터 원문: https://refactoring.guru/ko/design-patterns/adapter
- [[design-patterns]]
