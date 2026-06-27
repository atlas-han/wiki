---
title: Duplicate Code
type: engineering
tags: [engineering, refactoring]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [code-smells, refactoring-techniques, technical-debt]
first-seen: refactoring-guru-refactoring
sources: [refactoring-guru-refactoring]
---

# Duplicate Code

두 개 이상의 코드 조각이 거의 동일하게 보이는 상태. [[code-smells]] 중 **Dispensables(불필요한 것)** 계열이다.

## 신호와 증상
- 서로 다른 위치의 코드 조각이 거의 똑같이 생겼다.
- 한 곳을 고치면 똑같은 수정을 다른 곳에서도 반복해야 한다.
- 복사-붙여넣기로 만들어진 흔적이 보인다.

## 원인
- 여러 개발자가 같은 프로그램의 다른 부분을 동시에 작업하다 동료가 이미 작성한 유사 코드를 모르고 다시 만든다.
- 마감에 쫓기거나 게으름 때문에 기존 코드를 복사-붙여넣기한다.

## 해결 방법 (Treatment)
- `Extract Method` — 같은 클래스 안에 중복이 있으면 공통 부분을 메서드로 추출한다.
- `Pull Up Field` / `Pull Up Constructor Body` — 같은 부모를 가진 서브클래스들의 중복을 상위 클래스로 끌어올린다.
- `Extract Superclass` / `Extract Class` — 관련 없는 두 클래스에 중복이 있으면 공통 상위 클래스나 새 클래스로 묶는다.
- `Consolidate Conditional Expression` — 같은 결과로 이어지는 조건들을 하나로 합친 뒤 `Extract Method`로 빼낸다.

## 이득 (Payoff)
- 중복을 한 곳으로 모아 코드 구조가 단순해지고 길이가 짧아진다.
- 수정 지점이 하나로 줄어 유지보수 비용이 낮아진다.

## 무시해도 될 때
아주 드물게, 동일해 보이는 두 조각을 하나로 합치면 오히려 코드의 직관성이 떨어지는 경우에는 그대로 둔다.

## References
- [[refactoring-guru-refactoring]] — Duplicate Code 원문: https://refactoring.guru/smells/duplicate-code
- [[code-smells]]
