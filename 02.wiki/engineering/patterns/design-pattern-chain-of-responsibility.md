---
title: 책임 연쇄 (Chain of Responsibility)
type: engineering
tags: [engineering, design-patterns, gof, behavioral]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [design-patterns, design-pattern-command, design-pattern-iterator, design-pattern-mediator]
first-seen: refactoring-guru-ko-design-patterns
sources: [refactoring-guru-ko-design-patterns]
---

# 책임 연쇄 (Chain of Responsibility)

요청을 handler chain을 따라 전달하며, 각 handler가 처리하거나 다음으로 넘긴다. [[design-patterns]]의 행동 패턴에 속하며, 원문 기준 URL은 `https://refactoring.guru/ko/design-patterns/chain-of-responsibility`이다.

## 문제 신호

요청 처리자가 여러 개이고 처리 주체/순서가 런타임에 바뀌거나 sender와 receiver를 분리하고 싶을 때.

## 구조

Handler가 next handler를 참조하고 handle(request)를 제공한다. ConcreteHandler는 처리 가능하면 처리하고 아니면 위임한다.

## 적용 메모

- 클라이언트가 구상 타입이나 구체 협력자를 직접 알아야 하는 지점을 줄이는 데 초점을 둔다.
- 패턴명보다 중요한 것은 변경 축이다. 변경 축이 없거나 단순하면 일반 함수/클래스/언어 기능으로 충분할 수 있다.
- 테스트에서는 패턴이 만든 seam을 활용해 구상 구현 대신 fake/mock을 주입할 수 있는지 확인한다.

## 장단점

결합도를 낮추고 pipeline을 유연하게 구성한다. 요청이 누구에게 처리되는지 불명확하거나 아무도 처리하지 않을 수 있다.

## 관련 패턴

[[design-pattern-decorator]]처럼 chain 구조를 만들지만 책임 분산이 목적이다. UI event bubbling, middleware pipeline과 가깝다.

## References

- [[refactoring-guru-ko-design-patterns]] — 책임 연쇄 원문: https://refactoring.guru/ko/design-patterns/chain-of-responsibility
- [[design-patterns]]
