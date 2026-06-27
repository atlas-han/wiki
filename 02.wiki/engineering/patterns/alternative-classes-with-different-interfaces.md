---
title: Alternative Classes With Different Interfaces
type: engineering
tags: [engineering, refactoring]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [code-smells, refactoring-techniques, technical-debt]
first-seen: refactoring-guru-refactoring
sources: [refactoring-guru-refactoring]
---

# Alternative Classes with Different Interfaces

같은 일을 하는 두 클래스가 서로 다른 메서드 이름·인터페이스를 노출하는 상태다. [[code-smells]] 중 **객체지향 남용** 계열이다.

## 신호와 증상
- 두 클래스가 기능적으로 같은 역할을 하지만 메서드 이름과 시그니처가 서로 다르다.
- 서로 교체해 쓸 수 있을 것 같은데, 인터페이스가 어긋나 직접 바꿔 끼울 수 없다.

## 원인
한 클래스를 만든 사람이 이미 동등한 기능의 클래스가 존재한다는 사실을 몰랐을 가능성이 크다. 그 결과 무의식적으로 중복 구현([[duplicate-code]])이 생긴다.

## 해결 방법 (Treatment)
- `Rename Methods` — 두 클래스의 메서드 이름을 같은 규약으로 통일한다.
- `Move Method` / `Add Parameter` / `Parameterize Method` — 메서드 시그니처와 동작을 서로 맞춰 인터페이스를 일치시킨다.
- `Extract Superclass` — 일부 기능이 겹치면 공통 부분을 상위 클래스로 추출한다.
- 인터페이스가 동일해진 뒤에는 한쪽 클래스가 불필요해지므로 중복 클래스를 제거한다.

## 이득 (Payoff)
- 불필요한 중복 코드가 사라져 코드가 간결해진다.
- 통일된 인터페이스로 두 구현을 서로 바꿔 쓸 수 있어 가독성과 재사용성이 높아진다.

## 무시해도 될 때
서로 다른 외부 라이브러리의 클래스처럼 통합이 사실상 불가능한 경우에는 적용하지 않는다.

## References
- [[refactoring-guru-refactoring]] — Alternative Classes with Different Interfaces 원문: https://refactoring.guru/smells/alternative-classes-with-different-interfaces
- [[code-smells]]
