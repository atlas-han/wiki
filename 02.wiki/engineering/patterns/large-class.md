---
title: Large Class
type: engineering
tags: [engineering, refactoring]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [code-smells, refactoring-techniques, technical-debt]
first-seen: refactoring-guru-refactoring
sources: [refactoring-guru-refactoring]
---

# Large Class

한 클래스가 필드·메서드·코드 라인을 지나치게 많이 떠안아 여러 책임이 한곳에 몰린 상태다. [[code-smells]] 중 **Bloaters(비대화)** 계열이다.

## 신호와 증상
- 한 클래스가 너무 많은 필드·메서드·코드 라인을 갖고 있다.
- 클래스가 떠안은 책임이 여러 갈래라 한 문장으로 설명하기 어렵다.
- 거대한 클래스는 종종 그 안에 [[long-method]]나 [[data-clumps]]도 함께 품고 있다.

## 원인
클래스는 보통 작게 시작하지만 프로그램이 커지면서 점점 비대해진다. 새 기능을 위해 새 클래스를 만드는 것보다 기존 클래스에 메서드·필드를 보태는 쪽이 정신적으로 부담이 적기 때문이다.

## 해결 방법 (Treatment)
- `Extract Class` — 한 클래스 안에서 분리 가능한 동작 묶음을 별도 컴포넌트로 떼어낸다.
- `Extract Subclass` — 일부 동작이 여러 방식으로 구현되거나 드물게만 쓰이면 하위 클래스로 분리한다.
- `Extract Interface` — 클라이언트가 의존할 연산 목록을 인터페이스로 추려낸다.
- `Duplicate Observed Data` — GUI를 담당하는 클래스라면 데이터·동작을 별도 도메인 객체로 옮긴다.

## 이득 (Payoff)
- 개발자가 클래스의 수많은 속성을 한꺼번에 기억할 필요가 없어진다.
- 큰 클래스를 쪼개면 코드와 기능의 중복([[duplicate-code]])을 막을 수 있는 경우가 많다.

## 무시해도 될 때
refactoring.guru는 이 스멜에 대한 별도의 예외를 명시하지 않는다. 다만 분리가 오히려 강한 결합을 만들거나 분할 비용이 이득보다 크다면 보류할 수 있다.

## References
- [[refactoring-guru-refactoring]] — Large Class 원문: https://refactoring.guru/smells/large-class
- [[code-smells]]
