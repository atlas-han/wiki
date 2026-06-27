---
title: Shotgun Surgery
type: engineering
tags: [engineering, refactoring]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [code-smells, refactoring-techniques, technical-debt]
first-seen: refactoring-guru-refactoring
sources: [refactoring-guru-refactoring]
---

# Shotgun Surgery

작은 변경 하나가 여러 클래스에 걸친 자잘한 수정으로 흩어지는 상태다. [[code-smells]] 중 **변경 방지자** 계열이다.

## 신호와 증상
- 하나를 바꾸려면 여러 클래스에 걸쳐 작은 수정을 여러 군데 가해야 한다.
- 고쳐야 할 곳이 흩어져 있어 일부를 빠뜨리기 쉽다.
- 변경이 산탄총처럼 사방으로 퍼진다.

## 원인
하나여야 할 책임이 여러 클래스에 잘게 흩어져 있기 때문이다. [[divergent-change]]를 과도하게 적용한 끝에(책임을 너무 잘게 쪼개) 발생하기도 한다.

## 해결 방법 (Treatment)
- `Move Method` / `Move Field` — 흩어진 동작과 데이터를 하나의 클래스로 모은다. 마땅한 클래스가 없으면 새로 만든다.
- `Inline Class` — 코드를 옮긴 뒤 거의 비어버린 원래 클래스는 [[lazy-class]]가 되므로 인라인해 제거한다.

## 이득 (Payoff)
- 관련 변경이 한 클래스로 모여 수정 지점이 한 곳이 된다.
- 코드 중복이 줄고 조직이 개선된다.
- 유지보수가 쉬워진다.

## 무시해도 될 때
원문에 별도의 예외 조건은 제시되어 있지 않다.

## References
- [[refactoring-guru-refactoring]] — Shotgun Surgery 원문: https://refactoring.guru/smells/shotgun-surgery
- [[code-smells]]
