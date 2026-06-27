---
title: Feature Envy
type: engineering
tags: [engineering, refactoring]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [code-smells, refactoring-techniques, technical-debt]
first-seen: refactoring-guru-refactoring
sources: [refactoring-guru-refactoring]
---

# Feature Envy

메서드가 자기 클래스의 데이터보다 다른 객체의 데이터에 더 많이 접근·관심을 보이는 상태. [[code-smells]] 중 **Couplers(결합도 관련)** 계열이다.

## 신호와 증상
- 한 메서드가 다른 객체의 getter/필드를 여러 번 호출하며, 정작 자기 클래스의 데이터는 거의 쓰지 않는다.
- 계산 로직과 그 로직이 다루는 데이터가 서로 다른 클래스에 떨어져 있다.
- 같은 데이터 묶음에 대한 연산이 여러 곳에 흩어져 중복되기 쉽다.

## 원인
- 보통 필드를 [[data-class]]로 옮긴 뒤 그 데이터를 다루는 연산은 옮기지 않아서 발생한다. 데이터가 이동하면 데이터를 다루는 동작도 함께 따라가야 한다.

## 해결 방법 (Treatment)
- `Move Method` — 메서드 전체가 다른 객체의 데이터만 다룬다면, 그 데이터를 가진 클래스로 통째로 옮긴다.
- `Extract Method` — 메서드의 일부분만 다른 객체에 욕심을 낸다면, 그 부분만 떼어낸 뒤 `Move Method`로 옮긴다.
- 핵심 원칙은 "함께 변하는 것은 같은 곳에 둔다" — 가장 많은 데이터를 쓰는 클래스에 동작을 배치한다.

## 이득 (Payoff)
- 코드 중복 감소 (데이터 처리 로직이 한곳에 모인다).
- 데이터와 그 데이터를 다루는 메서드가 같은 클래스에 모여 코드 구성이 명확해진다.

## 무시해도 될 때
의도적으로 동작을 데이터에서 분리하는 경우는 정상이다. `Strategy`, `Visitor` 같은 디자인 패턴은 동작을 별도 객체로 두어 런타임에 교체·확장할 수 있게 하므로 Feature Envy처럼 보여도 문제가 아니다.

## References
- [[refactoring-guru-refactoring]] — Feature Envy 원문: https://refactoring.guru/smells/feature-envy
- [[code-smells]]
