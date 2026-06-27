---
title: Refused Bequest
type: engineering
tags: [engineering, refactoring]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [code-smells, refactoring-techniques, technical-debt]
first-seen: refactoring-guru-refactoring
sources: [refactoring-guru-refactoring]
---

# Refused Bequest

서브클래스가 부모로부터 물려받은 메서드·필드 중 일부만 실제로 쓰고 나머지는 거부(미사용하거나 예외로 재정의)하는 어긋난 상속 구조다. [[code-smells]] 중 **객체지향 남용** 계열이다.

## 신호와 증상
- 서브클래스가 상속받은 메서드와 속성의 일부만 사용한다.
- 불필요하게 물려받은 멤버가 그냥 방치되거나, 재정의되어 예외를 던지도록 막혀 있다.
- 상속 관계가 "is-a"로 자연스럽게 읽히지 않는다(예: Dog가 Chair를 상속).

## 원인
공통 동작이 실제로 닮아서가 아니라, 단지 상위 클래스의 코드를 재사용하려는 목적만으로 상속을 만들었기 때문이다. 실제로는 두 클래스가 서로 다른 것이다.

## 해결 방법 (Treatment)
- `Replace Inheritance with Delegation` — 상속이 부적절하면 위임으로 바꿔, 필요한 부분만 골라 호출한다.
- `Extract Superclass` (계층 재구성) — 상속이 타당하다면, 거부되는 멤버를 걷어내고 두 클래스가 진짜 공유하는 부분만 새 상위 클래스로 추출해 양쪽이 그것을 상속하게 한다.

## 이득 (Payoff)
- 상속 관계가 의미상 일관되어 코드가 자연스럽게 읽힌다.
- 거부되던 멤버가 사라져 클래스가 불필요한 짐을 지지 않는다.

## 무시해도 될 때
거부되는 양이 적고 상속이 주는 이점이 더 클 때는 굳이 바꾸지 않아도 된다. (원문에는 별도 절로 명시되어 있지 않다.)

## References
- [[refactoring-guru-refactoring]] — Refused Bequest 원문: https://refactoring.guru/smells/refused-bequest
- [[code-smells]]
