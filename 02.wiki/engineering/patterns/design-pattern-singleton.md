---
title: 싱글턴 (Singleton)
type: engineering
tags: [engineering, design-patterns, gof, creational]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [design-patterns, design-pattern-factory-method, design-pattern-abstract-factory, design-pattern-builder]
first-seen: refactoring-guru-ko-design-patterns
sources: [refactoring-guru-ko-design-patterns]
---

# 싱글턴 (Singleton)

클래스 인스턴스를 하나로 제한하고 전역 접근점을 제공한다. [[design-patterns]]의 생성 패턴에 속하며, 원문 기준 URL은 `https://refactoring.guru/ko/design-patterns/singleton`이다.

## 문제 신호

프로세스 전체에서 하나만 존재해야 하는 설정, registry, connection manager가 필요할 때. 단, 테스트와 결합도 비용을 감수할 수 있어야 한다.

## 구조

private constructor, static instance/accessor, lazy/eager initialization, thread-safe initialization으로 구성된다.

## 적용 메모

- 클라이언트가 구상 타입이나 구체 협력자를 직접 알아야 하는 지점을 줄이는 데 초점을 둔다.
- 패턴명보다 중요한 것은 변경 축이다. 변경 축이 없거나 단순하면 일반 함수/클래스/언어 기능으로 충분할 수 있다.
- 테스트에서는 패턴이 만든 seam을 활용해 구상 구현 대신 fake/mock을 주입할 수 있는지 확인한다.

## 장단점

유일성을 보장하지만 전역 상태가 되어 테스트·동시성·숨은 의존성 문제가 생기기 쉽다. 가능하면 DI container나 명시적 lifetime 관리가 더 낫다.

## 관련 패턴

[[design-pattern-abstract-factory]]나 [[design-pattern-facade]] 인스턴스를 단일 진입점으로 둘 때 쓰이지만, 남용하면 안티패턴이 된다.

## References

- [[refactoring-guru-ko-design-patterns]] — 싱글턴 원문: https://refactoring.guru/ko/design-patterns/singleton
- [[design-patterns]]
