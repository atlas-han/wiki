---
title: Comments
type: engineering
tags: [engineering, refactoring]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [code-smells, refactoring-techniques, technical-debt]
first-seen: refactoring-guru-refactoring
sources: [refactoring-guru-refactoring]
---

# Comments

메서드가 설명적 주석으로 가득 차, 주석이 직관적이지 않은 코드의 문제를 가리는 데오도란트(deodorant) 역할을 하는 상태. [[code-smells]] 중 **Dispensables(불필요한 것)** 계열이다.

## 신호와 증상
- 메서드 안이 "이 부분은 무엇을 한다"는 설명 주석으로 빽빽하다.
- 주석을 먼저 읽어야 코드가 이해되며, 주석을 지우면 의도를 알 수 없다.
- 주석이 복잡한 표현식·코드 블록의 의미를 대신 설명하고 있다.

## 원인
- 작성자가 코드가 직관적이지 않다고 느낄 때 주석을 덧붙인다.
- 주석은 개선이 필요한 나쁜 코드의 냄새를 덮는 향수처럼 쓰인다. 가장 좋은 주석은 메서드·클래스의 좋은 이름 그 자체다.

## 해결 방법 (Treatment)
- `Extract Variable` — 복잡한 표현식을 이해하기 쉬운 이름의 부분 표현식으로 쪼개 주석을 대체한다.
- `Extract Method` — 주석으로 구분하던 코드 블록을 별도 메서드로 추출하고, 주석 내용을 메서드 이름으로 옮긴다.
- `Rename Method` — 메서드가 하는 일을 설명하던 주석을 자명한 이름으로 흡수한다.
- `Introduce Assertion` — "여기서는 이 상태여야 한다"는 설명 주석을 코드로 강제되는 단언으로 바꾼다.

## 이득 (Payoff)
- 코드가 더 직관적이고 명확해진다.
- 이름과 구조가 의도를 드러내므로 주석을 따로 유지·동기화할 필요가 줄어든다.

## 무시해도 될 때
특정 구현을 왜 그렇게 했는지(WHY)를 설명하는 주석, 또는 다른 모든 단순화 시도가 실패한 복잡한 알고리즘을 설명하는 주석은 남겨두는 것이 좋다.

## References
- [[refactoring-guru-refactoring]] — Comments 원문: https://refactoring.guru/smells/comments
- [[code-smells]]
