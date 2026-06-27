---
title: Data Class
type: engineering
tags: [engineering, refactoring]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [code-smells, refactoring-techniques, technical-debt]
first-seen: refactoring-guru-refactoring
sources: [refactoring-guru-refactoring]
---

# Data Class

필드와 그 필드에 접근하기 위한 단순 getter/setter만 갖고, 자신의 데이터로 의미 있는 동작을 하지 못하는 클래스. [[code-smells]] 중 **Dispensables(불필요한 것)** 계열이다.

## 신호와 증상
- 클래스가 필드와 거친(crude) 접근 메서드(getter/setter)만 담고 있다.
- 다른 클래스가 사용할 데이터를 담을 뿐, 스스로 데이터를 가공하지 못한다.
- 데이터를 다루는 로직이 그 데이터를 가진 클래스 밖(클라이언트 코드)에 흩어져 있다.

## 원인
새로 만든 클래스가 공개 필드와 getter/setter만 갖는 것은 흔한 일이다. 하지만 객체의 진짜 가치는 데이터에 대한 동작·연산을 함께 가질 수 있다는 점에 있는데, 이를 활용하지 못한 상태다.

## 해결 방법 (Treatment)
- `Encapsulate Field` — 공개 필드를 숨겨 외부 접근을 제어한다.
- `Encapsulate Collection` — 배열 등 컬렉션 필드를 직접 노출하지 않고 보호한다.
- `Move Method` / `Extract Method` — 클라이언트에 흩어진, 그 데이터를 다루는 로직을 데이터 클래스 안으로 옮긴다.
- `Remove Setting Method` / `Hide Method` — 너무 넓게 열린 setter나 불필요한 접근 메서드를 제거·은닉한다.

## 이득 (Payoff)
- 특정 데이터에 대한 연산이 한 곳에 모여 코드 이해도와 조직성이 좋아진다.
- 클라이언트 코드에 흩어진 중복([[duplicate-code]])을 발견·제거하는 데 도움이 된다.

## 무시해도 될 때
계층 간 데이터 전달용 DTO처럼, 의도적으로 동작 없이 데이터만 담는 역할이라면 Data Class는 정상이다. (refactoring.guru 원문에는 별도의 무시 조건 섹션이 명시되어 있지 않다.)

## References
- [[refactoring-guru-refactoring]] — Data Class 원문: https://refactoring.guru/smells/data-class
- [[code-smells]]
