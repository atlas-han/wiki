---
title: Primitive Obsession
type: engineering
tags: [engineering, refactoring]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [code-smells, refactoring-techniques, technical-debt]
first-seen: refactoring-guru-refactoring
sources: [refactoring-guru-refactoring]
---

# Primitive Obsession

통화·범위·전화번호처럼 도메인 의미가 있는 값을 작은 객체 대신 원시 타입과 상수로 표현하는 상태다. [[code-smells]] 중 **Bloaters(비대화)** 계열이다.

## 신호와 증상
- 통화, 범위, 전화번호용 특수 문자열 등 간단한 작업에 작은 객체 대신 원시 타입을 쓴다.
- 정보를 상수로 인코딩한다(예: 관리자 권한을 뜻하는 `USER_ADMIN_ROLE = 1`).
- 데이터 배열의 필드 이름으로 문자열 상수를 사용한다.

## 원인
원시 타입 남용은 "약한 순간의 결정"에서 비롯된다 — 새 클래스를 만들기보다 필드 하나 더 추가하는 게 쉬워 보인다. 이렇게 쌓인 원시 필드들이 클래스를 거대하고 다루기 힘들게 만든다. 또 원시 타입은 허용 값을 상수로 정의해 타입을 흉내 내거나, 배열 인덱스를 문자열 상수로 대신하는 식으로 오용된다.

## 해결 방법 (Treatment)
- `Replace Data Value with Object` — 관련된 원시 필드들을 하나의 새 클래스로 묶는다.
- `Introduce Parameter Object` / `Preserve Whole Object` — 메서드 파라미터로 떠도는 원시 값들을 객체로 정리한다.
- `Replace Type Code with Class` / `Replace Type Code with Subclasses` / `Replace Type Code with State/Strategy` — 변수에 인코딩된 타입 코드를 클래스·하위 클래스·상태/전략 객체로 바꾼다([[switch-statements]] 제거에도 도움이 된다).
- `Replace Array with Object` — 서로 다른 의미의 원소가 섞인 배열을 필드를 가진 객체로 바꾼다.

## 이득 (Payoff)
- 원시 타입 대신 객체를 써서 코드가 더 유연해진다.
- 특정 데이터에 대한 연산이 한곳에 모여 이해도와 조직화가 좋아진다.
- 중복 코드([[duplicate-code]])를 찾기 쉬워진다.

## 무시해도 될 때
refactoring.guru는 이 스멜에 대한 별도의 예외를 명시하지 않는다. 다만 값이 단순하고 도메인 규칙이 붙지 않는다면 객체화 비용이 이득보다 클 수 있다.

## References
- [[refactoring-guru-refactoring]] — Primitive Obsession 원문: https://refactoring.guru/smells/primitive-obsession
- [[code-smells]]
