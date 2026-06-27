---
title: Refactoring Techniques
type: engineering
tags: [engineering, refactoring]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [refactoring, code-smells, technical-debt]
first-seen: refactoring-guru-refactoring
sources: [refactoring-guru-refactoring]
---

# Refactoring Techniques

Refactoring technique는 behavior를 유지하면서 구조를 바꾸는 이름 붙은 작은 변환이다. [[code-smells]]가 “어디가 불편한가”를 말한다면, technique는 “어떤 순서로 바꿀 것인가”를 말한다.

## Technique families

- [[refactoring-techniques-composing-methods]] — 긴 메서드를 작은 의도 단위로 쪼개거나, 반대로 불필요한 간접층을 인라인해 메서드 내부 구성을 다듬는다.
- [[refactoring-techniques-moving-features-between-objects]] — 메서드·필드·책임이 더 자연스럽게 속해야 할 객체로 이동시켜 응집도를 높이고 결합도를 낮춘다.
- [[refactoring-techniques-organizing-data]] — primitive, 배열, type code, association 등 데이터 표현을 도메인 의미와 변경 축에 맞게 재구성한다.
- [[refactoring-techniques-simplifying-conditional-expressions]] — 복잡한 조건식을 명명·분해·다형성·guard clause 등으로 단순화한다.
- [[refactoring-techniques-simplifying-method-calls]] — 메서드 이름·파라미터·예외·가시성을 다듬어 API 호출면을 명확하게 만든다.
- [[refactoring-techniques-dealing-with-generalization]] — 상속·위임·공통화·계층 병합을 조정해 일반화 구조를 실제 변경 요구에 맞춘다.

## 적용 원칙

1. 테스트 또는 명확한 검증 루프를 먼저 확보한다.
2. 하나의 step은 하나의 구조 변화만 담는다.
3. PR 설명에는 smell → technique → 기대 효과를 연결한다.
4. [[design-patterns]] 적용은 technique의 결과일 수 있지만, 패턴을 목표로 과설계하지 않는다.

## References

- [[refactoring-guru-refactoring]]
