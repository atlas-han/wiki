---
title: Message Chains
type: engineering
tags: [engineering, refactoring]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [code-smells, refactoring-techniques, technical-debt]
first-seen: refactoring-guru-refactoring
sources: [refactoring-guru-refactoring]
---

# Message Chains

클라이언트가 `a.getB().getC().getD()`처럼 객체 그래프를 연쇄로 타고 들어가, 객체 간 내부 구조를 속속들이 알아야 호출할 수 있는 상태. [[code-smells]] 중 **Couplers(결합도 관련)** 계열이다.

## 신호와 증상
- `$a->b()->c()->d()` 같은 긴 호출 연쇄가 코드에 자주 보인다.
- 클라이언트가 객체들의 탐색(navigation) 구조에 의존해, 중간 관계가 바뀌면 호출부도 함께 깨진다.
- 중간 객체들의 클래스 구조 변화가 멀리 떨어진 클라이언트까지 전파된다.

## 원인
- 클라이언트가 한 객체에 요청하고, 그 객체가 또 다른 객체에 요청하는 식으로 이어지면서 객체 그래프의 내부 연결 구조에 클라이언트가 강하게 묶이기 때문이다.

## 해결 방법 (Treatment)
- `Hide Delegate` — 연쇄의 중간 단계를 위임 메서드 뒤로 숨겨, 클라이언트가 끝단 객체를 직접 알지 못하게 한다.
- `Extract Method` + `Move Method` — 연쇄를 사용하는 코드 조각을 떼어내 연쇄가 시작되는 객체 쪽으로 기능을 옮긴다.

## 이득 (Payoff)
- 클래스 간 의존성이 줄어든다.
- 호출 연쇄로 부푼 코드량이 줄어든다.

## 무시해도 될 때
위임 숨김을 과하게 적용하면 기능의 실제 위치를 파악하기 어려워지고, 책임 없는 위임만 남는 [[middle-man]] 냄새로 이어질 수 있다. 따라서 무조건 모든 연쇄를 없애기보다 균형을 본다.

## References
- [[refactoring-guru-refactoring]] — Message Chains 원문: https://refactoring.guru/smells/message-chains
- [[code-smells]]
