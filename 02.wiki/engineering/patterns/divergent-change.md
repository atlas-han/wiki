---
title: Divergent Change
type: engineering
tags: [engineering, refactoring]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [code-smells, refactoring-techniques, technical-debt]
first-seen: refactoring-guru-refactoring
sources: [refactoring-guru-refactoring]
---

# Divergent Change

한 클래스가 서로 무관한 여러 변경 이유 때문에 자꾸 수정되는 상태다. [[code-smells]] 중 **변경 방지자** 계열이다.

## 신호와 증상
- 어떤 변경을 가하면 그 클래스 안의 서로 관련 없는 메서드 여러 개를 함께 고쳐야 한다.
- 예: 새 상품 유형을 추가하는데 검색·표시·주문 처리 메서드를 한 클래스 안에서 모두 손봐야 한다.
- "이 클래스는 ~할 때 그리고 ~할 때 바뀐다"처럼 변경 이유가 여러 개다(단일 책임 위반).

## 원인
부실한 구조로 한 클래스에 여러 책임이 뭉쳐 있거나, 복사-붙여넣기 프로그래밍으로 무관한 로직이 한곳에 모였기 때문이다. [[shotgun-surgery]]와 정반대 방향의 냄새다(한 클래스가 여러 이유로 변함 vs 한 변경이 여러 클래스로 퍼짐).

## 해결 방법 (Treatment)
- `Extract Class` — 변경 이유(책임)별로 클래스를 쪼개, 각 클래스가 한 가지 이유로만 바뀌게 한다.
- `Extract Superclass` / `Extract Subclass` — 분리한 책임이 여러 클래스에 공통으로 나타나면 상속으로 통합한다.

## 이득 (Payoff)
- 변경이 한 책임 = 한 클래스로 국소화되어 수정 범위가 명확해진다.
- 책임 분리로 코드 조직이 개선되고 중복이 줄어든다.
- 유지보수가 단순해진다.

## 무시해도 될 때
원문에 별도의 예외 조건은 제시되어 있지 않다.

## References
- [[refactoring-guru-refactoring]] — Divergent Change 원문: https://refactoring.guru/smells/divergent-change
- [[code-smells]]
