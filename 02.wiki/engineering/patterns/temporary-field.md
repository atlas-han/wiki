---
title: Temporary Field
type: engineering
tags: [engineering, refactoring]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [code-smells, refactoring-techniques, technical-debt]
first-seen: refactoring-guru-refactoring
sources: [refactoring-guru-refactoring]
---

# Temporary Field

특정 상황에서만 값이 채워지고 그 밖의 시간에는 비어 있는 필드가 객체에 존재하는 상태다. [[code-smells]] 중 **객체지향 남용** 계열이다.

## 신호와 증상
- 어떤 필드가 특정 알고리즘이 도는 동안에만 값을 갖고, 나머지 시간에는 비어(`null`/기본값) 있다.
- 객체의 정상 상태만 보고는 그 필드가 왜 거기 있는지, 언제 유효한지 알기 어렵다.
- 비어 있을 수 있는 필드 때문에 곳곳에 방어적 `null` 검사가 붙는다.

## 원인
알고리즘이 많은 입력을 필요로 할 때, 긴 매개변수 목록([[long-parameter-list]])을 피하려고 그 값들을 임시로 클래스 필드에 담아 두기 때문이다. 이 필드들은 알고리즘 실행 중에만 쓰이고 그 외에는 방치된다.

## 해결 방법 (Treatment)
- `Extract Class` — 임시 필드와 그것을 사용하는 코드를 별도 클래스로 분리한다. 그 알고리즘만을 위한 메서드 객체(Method Object)가 된다.
- `Introduce Null Object` — 필드가 비어 있을 때를 위한 널 객체를 도입해 흩어진 `null` 검사를 없앤다.

## 이득 (Payoff)
- 클래스의 정상 상태가 명확해지고, 필드의 생애주기가 한 곳으로 모인다.
- 방어적 조건 분기가 줄어 가독성과 구조가 개선된다.

## 무시해도 될 때
원문에 별도의 예외 조건은 제시되어 있지 않다.

## References
- [[refactoring-guru-refactoring]] — Temporary Field 원문: https://refactoring.guru/smells/temporary-field
- [[code-smells]]
