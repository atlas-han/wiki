---
title: Lazy Class
type: engineering
tags: [engineering, refactoring]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [code-smells, refactoring-techniques, technical-debt]
first-seen: refactoring-guru-refactoring
sources: [refactoring-guru-refactoring]
---

# Lazy Class

이해하고 유지보수하는 데 드는 시간·비용에 비해 하는 일이 너무 적어, 독립 클래스로 둘 이유가 약한 클래스. [[code-smells]] 중 **Dispensables(불필요한 것)** 계열이다.

## 신호와 증상
- 클래스가 자신의 존재 비용(이해·유지보수)을 정당화할 만큼 충분한 일을 하지 않는다.
- 거의 빈 껍데기이거나, 다른 클래스로 단순히 위임만 하는 클래스가 있다.
- 기능이 거의 없는 서브클래스가 계층에 매달려 있다.

## 원인
- 리팩토링 과정에서 클래스의 책임이 다른 곳으로 옮겨가 클래스가 불필요하게 작아졌다.
- 미래 개발을 염두에 두고 클래스를 만들었으나 실제 개발이 진행되지 않았다.

## 해결 방법 (Treatment)
- `Inline Class` — 거의 쓸모없는 컴포넌트를, 그 기능을 사용하는 다른 클래스 안으로 흡수한다.
- `Collapse Hierarchy` — 기능이 거의 없는 서브클래스를 상위 클래스와 합친다.

## 이득 (Payoff)
- 코드 크기가 줄어든다.
- 유지보수가 쉬워진다.

## 무시해도 될 때
미래 개발 의도를 명확히 드러내기 위해 의도적으로 만든 Lazy Class도 있다. 명확성과 단순성 사이의 균형을 고려해 판단한다. (지나치면 [[speculative-generality]]가 된다.)

## References
- [[refactoring-guru-refactoring]] — Lazy Class 원문: https://refactoring.guru/smells/lazy-class
- [[code-smells]]
