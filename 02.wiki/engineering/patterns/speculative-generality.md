---
title: Speculative Generality
type: engineering
tags: [engineering, refactoring]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [code-smells, refactoring-techniques, technical-debt]
first-seen: refactoring-guru-refactoring
sources: [refactoring-guru-refactoring]
---

# Speculative Generality

"언젠가 필요할지 모른다(just in case)"는 추측만으로 만들어졌지만 실제로는 쓰이지 않는 클래스·메서드·필드·매개변수. [[code-smells]] 중 **Dispensables(불필요한 것)** 계열이다.

## 신호와 증상
- 사용되지 않는 클래스·메서드·필드·매개변수가 존재한다.
- 실제 요구가 없는데도 "확장성"을 위해 미리 만든 추상 클래스나 위임 계층이 있다.
- 실제로 한 가지 경우만 처리하는데 일반화된 파라미터를 받는다.

## 원인
실제로 구현되지 않은 미래 기능에 대비해 "혹시 모르니까(just in case)" 코드를 미리 일반화해 두면, 그 추상화가 오히려 이해와 유지보수를 어렵게 만든다.

## 해결 방법 (Treatment)
- `Collapse Hierarchy` — 쓰이지 않는 추상 클래스를 상위/하위 클래스와 합친다.
- `Inline Class` — 불필요한 위임만 하는 클래스를 인라인한다.
- `Inline Method` — 쓰이지 않는 메서드를 호출부로 합쳐 제거한다.
- `Remove Parameter` — 사용되지 않는 매개변수를 제거한다.
- 사용되지 않는 필드는 직접 삭제한다.

## 이득 (Payoff)
- 코드가 더 간결해진다.
- 유지보수가 쉬워진다.

## 무시해도 될 때
프레임워크를 개발할 때는, 프레임워크 자체에서는 쓰이지 않더라도 사용자에게 필요한 기능이라면 일반화된 코드를 둘 수 있다. 또한 단위 테스트에서 쓰이는 요소는 삭제 전에 확인해야 한다.

## References
- [[refactoring-guru-refactoring]] — Speculative Generality 원문: https://refactoring.guru/smells/speculative-generality
- [[code-smells]]
