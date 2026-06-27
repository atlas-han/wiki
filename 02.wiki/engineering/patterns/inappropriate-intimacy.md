---
title: Inappropriate Intimacy
type: engineering
tags: [engineering, refactoring]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [code-smells, refactoring-techniques, technical-debt]
first-seen: refactoring-guru-refactoring
sources: [refactoring-guru-refactoring]
---

# Inappropriate Intimacy

한 클래스가 다른 클래스의 내부 필드와 메서드에 과도하게 접근·의존하는 상태. [[code-smells]] 중 **Couplers(결합도 관련)** 계열이다.

## 신호와 증상
- 한 클래스가 다른 클래스의 private에 가까운 내부 세부사항을 직접 들여다보고 사용한다.
- 두 클래스가 서로의 내부를 너무 잘 알아 상호 의존(양방향 결합)이 생긴다.
- 한쪽을 바꾸면 다른 쪽도 함께 고쳐야 해 유지보수와 재사용이 어렵다.

## 원인
- 좋은 클래스 설계는 서로에 대한 지식을 최소화해야 하는데, 두 클래스가 지나치게 많은 시간을 "함께 보내며" 서로의 내부에 손을 뻗을 때 발생한다.

## 해결 방법 (Treatment)
- `Move Method` / `Move Field` — 한 클래스가 정말 필요로 하는 부분을 그 클래스 쪽으로 옮겨 결합을 끊는다.
- `Extract Class` — 두 클래스에 공통으로 얽힌 부분을 별도 클래스로 분리한다.
- `Hide Delegate` — 직접 접근 대신 위임 메서드를 두어 관계를 명확하게 한다.
- `Change Bidirectional Association to Unidirectional` — 상호 의존이 있으면 한 방향으로 줄인다.
- `Replace Delegation with Inheritance` — 부모-자식처럼 밀접하고 위임이 과한 관계라면 상속으로 전환을 고려한다.

## 이득 (Payoff)
- 코드 구조가 개선되고 결합도가 낮아진다.
- 유지보수와 재사용이 쉬워진다.

## 무시해도 될 때
일부 결합은 불가피하며 받아들일 수 있다. 긴밀한 협력이 도메인상 본질적이거나 분리 비용이 이득보다 큰 경우, [[message-chains]]·[[middle-man]]처럼 과교정으로 다른 냄새를 만들지 않도록 균형을 본다.

## References
- [[refactoring-guru-refactoring]] — Inappropriate Intimacy 원문: https://refactoring.guru/smells/inappropriate-intimacy
- [[code-smells]]
