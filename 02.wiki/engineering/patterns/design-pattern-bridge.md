---
title: 브리지 (Bridge)
type: engineering
tags: [engineering, design-patterns, gof, structural]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [design-patterns, design-pattern-adapter, design-pattern-composite, design-pattern-decorator]
first-seen: refactoring-guru-ko-design-patterns
sources: [refactoring-guru-ko-design-patterns]
---

# 브리지 (Bridge)

큰 클래스나 밀접하게 연관된 클래스 묶음을 추상화와 구현이라는 두 개의 독립적인 계층구조로 나누어 각각 따로 개발할 수 있게 한다. [[design-patterns]]의 구조 패턴에 속한다.

## 문제

클래스가 서로 독립적인 여러 차원에서 동시에 확장되어야 할 때 상속만 사용하면 조합의 수가 기하급수적으로 늘어난다. 예를 들어 `원`과 `직사각형` 모양에 `빨강`과 `파랑` 색상을 더하면 네 가지 조합 클래스가 필요하고, 새 모양이나 색상을 추가할 때마다 만들어야 할 클래스가 곱셈으로 불어난다.

## 해결책

상속을 객체 합성으로 전환하여 한 차원(예: 색상)을 별도의 클래스 계층구조로 추출한다. 원래 클래스(Abstraction)가 새 계층(Implementation)의 객체를 참조 필드로 갖게 하면, 모양 계층과 색상 계층을 서로 독립적으로 확장할 수 있다. Abstraction은 고수준 제어 로직을, Implementation은 실제 저수준 작업을 담당한다.

## 실세계 비유

앱의 그래픽 사용자 인터페이스(GUI) 계층과 그 아래의 운영 체제 API의 관계와 같다. GUI는 사용자와 상호작용하는 추상화 계층이고, OS API는 플랫폼별 구현 계층이다. GUI는 플랫폼별 API를 직접 바꾸지 않고도 Windows, Linux, macOS 등 여러 OS 위에서 동작할 수 있다.

## 적용 가능성

- 어떤 기능의 여러 변형을 가진 모놀리식 클래스를 나누고 정리하고 싶을 때
- 클래스가 서로 직교(독립)하는 여러 차원에서 확장되어야 할 때
- 런타임에 구현 객체를 갈아 끼울 수 있어야 할 때

## 장단점

**장점**
- 플랫폼에 독립적인 클래스와 앱을 만들 수 있다
- 클라이언트 코드가 고수준 추상화만 다루며 플랫폼 세부 정보에 노출되지 않는다
- 개방/폐쇄 원칙: 추상화와 구현을 서로 독립적으로 새로 도입할 수 있다
- 단일 책임 원칙: 추상화는 고수준 로직, 구현은 세부 작업에 집중한다

**단점**
- 응집도가 높은 단일 클래스에 적용하면 오히려 코드가 더 복잡해질 수 있다

## 다른 패턴과의 관계

- [[design-pattern-adapter]]는 기존의 비호환 클래스를 사후에 맞추는 용도이고, 브리지는 처음부터 추상화와 구현을 분리하도록 사전에 설계한다.
- [[design-pattern-state]], [[design-pattern-strategy]]와 구조는 유사하지만(합성으로 동작 위임) 해결하는 문제가 다르다.
- [[design-pattern-abstract-factory]]와 함께 쓰면 특정 추상화가 사용할 구현들의 관계를 캡슐화할 수 있다.
- [[design-pattern-builder]]와 결합할 때 디렉터가 추상화 역할을, 빌더들이 구현 역할을 맡을 수 있다.

## References

- [[refactoring-guru-ko-design-patterns]] — 브리지 원문: https://refactoring.guru/ko/design-patterns/bridge
- [[design-patterns]]
