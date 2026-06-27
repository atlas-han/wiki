---
title: Long Method
type: engineering
tags: [engineering, refactoring]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [code-smells, refactoring-techniques, technical-debt]
first-seen: refactoring-guru-refactoring
sources: [refactoring-guru-refactoring]
---

# Long Method

한 메서드가 너무 많은 코드 라인을 담고 있어 이름 붙일 수 있는 여러 단계와 책임이 한 몸에 뒤섞인 상태다. [[code-smells]] 중 **Bloaters(비대화)** 계열이다.

## 신호와 증상
- 메서드의 코드 라인이 너무 많다. 보통 10줄을 넘어서면 의심해 볼 신호다.
- 지역 변수와 파라미터가 많아 본문 흐름을 따라가기 어렵다.
- 본문이 여러 단계로 나뉘어 "이 부분은 X를 한다"처럼 따로 이름 붙일 수 있는 덩어리가 보인다.

## 원인
메서드에는 코드가 계속 추가되지만 좀처럼 제거되지 않는다. 코드를 쓰는 일이 읽는 일보다 쉽기 때문에, 새 메서드를 만드는 부담을 피해 기존 메서드에 한 줄씩 더 보태다 보면 메서드가 못생기고 거대해질 때까지 방치된다. 결과적으로 스파게티 코드의 얽힘이 생긴다.

## 해결 방법 (Treatment)
- `Extract Method` — 메서드를 의미 단위로 쪼개 본문 길이를 줄인다. 거의 모든 경우의 1차 대응이며, 반복문도 그 본문을 별도 메서드로 추출한다.
- `Replace Temp with Query` — 지역 변수가 추출을 방해하면 임시 변수를 쿼리 메서드로 바꿔 분해를 쉽게 만든다.
- `Introduce Parameter Object` / `Preserve Whole Object` — 추출 과정에서 늘어나는 파라미터를 객체로 묶는다.
- `Replace Method with Method Object` — 지역 변수가 많아 단순 추출이 어려우면 메서드 전체를 별도 객체로 옮긴다.
- `Decompose Conditional` — 길고 복잡한 조건문을 조건과 분기별 메서드로 분해한다.

## 이득 (Payoff)
- 짧은 메서드를 가진 클래스가 더 오래 살아남는다 — 이해와 유지가 쉽다.
- 긴 메서드 안에 숨어 있던 [[duplicate-code]]가 드러나 제거하기 쉬워진다.
- 잘 지은 메서드 이름이 문서 역할을 해 [[comments]] 의존이 줄어든다.

## 무시해도 될 때
refactoring.guru는 이 스멜에 대한 별도의 예외를 명시하지 않는다. 다만 추출이 오히려 응집도를 깨거나 의미 없는 간접 호출만 늘린다면 분해를 보류할 수 있다.

## References
- [[refactoring-guru-refactoring]] — Long Method 원문: https://refactoring.guru/smells/long-method
- [[code-smells]]
