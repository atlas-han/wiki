---
title: Parallel Inheritance Hierarchies
type: engineering
tags: [engineering, refactoring]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [code-smells, refactoring-techniques, technical-debt]
first-seen: refactoring-guru-refactoring
sources: [refactoring-guru-refactoring]
---

# Parallel Inheritance Hierarchies

한 클래스에 서브클래스를 만들 때마다 다른 클래스에도 대응되는 서브클래스를 만들어야 하는 상태다. [[code-smells]] 중 **변경 방지자** 계열이다. [[shotgun-surgery]]의 특수한 형태로 볼 수 있다.

## 신호와 증상
- 어느 한 클래스의 서브클래스를 만들면, 매번 다른 클래스의 서브클래스도 함께 만들게 된다.
- 두 계층의 접두사(클래스 이름 앞부분)가 똑같이 짝지어 늘어난다.

## 원인
처음에는 계층이 작아 문제가 드러나지 않지만, 클래스가 계속 추가되면서 두 계층을 나란히 맞춰 확장·수정하는 일이 점점 어려워진다.

## 해결 방법 (Treatment)
- 먼저 한 계층의 인스턴스가 다른 계층의 인스턴스를 참조하도록 구성한다.
- `Move Method` / `Move Field` — 참조하는 쪽으로 메서드와 필드를 옮겨, 참조되던 쪽의 계층을 통째로 제거한다.

## 이득 (Payoff)
- 중복되던 한 계층이 사라져 코드 중복이 줄어든다.
- 코드 조직이 단순해지고 서브클래스 추가 부담이 없어진다.

## 무시해도 될 때
평행 계층을 없애는 것이 오히려 프로그램 아키텍처에 더 큰 혼란을 부를 때는, 그대로 두는 편이 나을 수 있다.

## References
- [[refactoring-guru-refactoring]] — Parallel Inheritance Hierarchies 원문: https://refactoring.guru/smells/parallel-inheritance-hierarchies
- [[code-smells]]
