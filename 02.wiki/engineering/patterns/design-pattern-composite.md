---
title: 복합체 (Composite)
type: engineering
tags: [engineering, design-patterns, gof, structural]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [design-patterns, design-pattern-adapter, design-pattern-bridge, design-pattern-decorator]
first-seen: refactoring-guru-ko-design-patterns
sources: [refactoring-guru-ko-design-patterns]
---

# 복합체 (Composite)

개별 객체와 객체 트리를 같은 인터페이스로 다룬다. [[design-patterns]]의 구조 패턴에 속하며, 원문 기준 URL은 `https://refactoring.guru/ko/design-patterns/composite`이다.

## 문제 신호

파일 시스템, UI 트리, 조직도처럼 부분-전체 계층을 재귀적으로 처리해야 할 때.

## 구조

Component가 공통 operation을 정의하고 Leaf는 단일 객체, Composite는 children을 보유해 operation을 위임/집계한다.

## 적용 메모

- 클라이언트가 구상 타입이나 구체 협력자를 직접 알아야 하는 지점을 줄이는 데 초점을 둔다.
- 패턴명보다 중요한 것은 변경 축이다. 변경 축이 없거나 단순하면 일반 함수/클래스/언어 기능으로 충분할 수 있다.
- 테스트에서는 패턴이 만든 seam을 활용해 구상 구현 대신 fake/mock을 주입할 수 있는지 확인한다.

## 장단점

클라이언트가 leaf/composite를 구분하지 않아도 된다. 너무 일반적인 Component 인터페이스는 leaf에 의미 없는 메서드를 강제할 수 있다.

## 관련 패턴

트리 생성에는 [[design-pattern-builder]]가 잘 맞고, 순회는 [[design-pattern-iterator]], 동작 추가는 [[design-pattern-visitor]]와 자주 결합된다.

## References

- [[refactoring-guru-ko-design-patterns]] — 복합체 원문: https://refactoring.guru/ko/design-patterns/composite
- [[design-patterns]]
