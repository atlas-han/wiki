---
title: Refactoring.Guru 한국어 디자인 패턴
type: source
tags: [engineering, design-patterns, gof]
created: 2026-06-27
updated: 2026-06-27
source-url: https://refactoring.guru/ko/design-patterns
source-type: docs
date-published: unknown
ingested: 2026-06-27
---

# Refactoring.Guru 한국어 디자인 패턴

Refactoring.Guru의 한국어 Design Patterns 카탈로그를 기반으로 GoF 계열 디자인 패턴 22개를 [[design-patterns]] 허브와 개별 engineering pattern 페이지로 정리한 소스 요약이다. 원문은 각 패턴의 **의도, 문제, 해결책, 구조, 의사코드, 적용 가능성, 구현 방법, 장단점, 다른 패턴과의 관계**를 설명한다.

## 핵심 Takeaways

1. 디자인 패턴은 “외워서 끼워 넣는 코드 조각”이 아니라, 반복되는 설계 압력(생성 책임, 결합도, 객체 조합, 행동 분배)에 붙은 이름이다.
2. 생성/구조/행동 세 분류는 각각 **객체를 어떻게 만들 것인가**, **객체를 어떻게 조립할 것인가**, **객체들이 어떻게 협력할 것인가**를 나눈다.
3. 패턴의 장점은 대부분 결합도 감소와 변경 축 분리지만, 비용은 클래스/간접 계층 증가다. 따라서 단순 문제에 무리하게 적용하면 과설계가 된다.
4. 패턴 사이에는 관계가 많다. 예: [[design-pattern-factory-method]] → [[design-pattern-abstract-factory]], [[design-pattern-composite]] + [[design-pattern-visitor]], [[design-pattern-command]] + [[design-pattern-memento]].
5. 현대 언어/프레임워크는 일부 패턴을 언어 기능, DI container, iterator protocol, event system으로 흡수했지만, 설계 vocabulary로서의 가치는 유지된다.

## 포함 범위

- 생성 패턴: [[design-pattern-factory-method]], [[design-pattern-abstract-factory]], [[design-pattern-builder]], [[design-pattern-prototype]], [[design-pattern-singleton]]
- 구조 패턴: [[design-pattern-adapter]], [[design-pattern-bridge]], [[design-pattern-composite]], [[design-pattern-decorator]], [[design-pattern-facade]], [[design-pattern-flyweight]], [[design-pattern-proxy]]
- 행동 패턴: [[design-pattern-chain-of-responsibility]], [[design-pattern-command]], [[design-pattern-iterator]], [[design-pattern-mediator]], [[design-pattern-memento]], [[design-pattern-observer]], [[design-pattern-state]], [[design-pattern-strategy]], [[design-pattern-template-method]], [[design-pattern-visitor]]

## References

- Refactoring.Guru 한국어 Design Patterns: https://refactoring.guru/ko/design-patterns
- Raw inventory: `01.raw/articles/2026-06-27_refactoring-guru-ko-design-patterns.md`
