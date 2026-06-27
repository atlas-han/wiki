---
title: Code Smells
type: engineering
tags: [engineering, refactoring]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [refactoring, refactoring-techniques, technical-debt]
first-seen: refactoring-guru-refactoring
sources: [refactoring-guru-refactoring]
---

# Code Smells

Code smell은 즉시 버그라는 뜻이 아니라, 코드가 이해·변경·확장 비용을 키우는 방향으로 굳어졌다는 진단 신호다. [[refactoring]]에서는 smell을 발견한 뒤 적절한 [[refactoring-techniques]]를 작은 단계로 적용한다.

## smell 분류

### Bloaters
- [[long-method]] — 한 메서드가 너무 길어 이름 붙일 수 있는 단계들이 한 몸에 섞인 상태.
- [[large-class]] — 한 클래스가 필드·메서드·책임을 과도하게 많이 떠안은 상태.
- [[primitive-obsession]] — 도메인 의미가 있는 값·범위·분류를 작은 객체 대신 primitive·상수로 표현하는 상태.
- [[long-parameter-list]] — 메서드 호출에 필요한 파라미터가 지나치게 많아 호출자와 구현이 강하게 결합된 상태.
- [[data-clumps]] — 여러 위치에서 항상 함께 움직이는 변수 묶음이 반복되는 상태.

### Object-Orientation Abusers
- [[alternative-classes-with-different-interfaces]] — 같은 역할의 클래스들이 서로 다른 메서드 이름·인터페이스를 노출하는 상태.
- [[refused-bequest]] — 하위 클래스가 상위 클래스의 일부 상속만 실제로 필요로 하는 어긋난 상속 구조.
- [[switch-statements]] — 타입·상태별 분기가 여러 곳에 반복되어 새 변형 추가가 여러 수정으로 번지는 상태.
- [[temporary-field]] — 특정 상황에서만 값이 채워지는 필드가 객체의 정상 상태를 흐리는 상태.

### Change Preventers
- [[divergent-change]] — 한 클래스가 서로 다른 변경 이유들 때문에 계속 수정되는 상태.
- [[parallel-inheritance-hierarchies]] — 한 계층에 subclass를 추가할 때 다른 계층에도 대응 subclass를 추가해야 하는 상태.
- [[shotgun-surgery]] — 작은 기능 변경 하나가 여러 클래스의 작은 수정으로 흩어지는 상태.

### Dispensables
- [[comments]] — 코드 자체가 설명하지 못하는 의도·절차를 주석이 대신 떠받치는 상태.
- [[duplicate-code]] — 동일하거나 거의 동일한 코드 조각이 여러 위치에 존재하는 상태.
- [[data-class]] — 데이터 필드와 단순 getter/setter만 있고 의미 있는 행동이 없는 클래스.
- [[dead-code]] — 더 이상 사용되지 않는 변수·필드·메서드·클래스가 남아 있는 상태.
- [[lazy-class]] — 존재 비용에 비해 책임이 너무 적어 독립 클래스로 둘 이유가 약한 상태.
- [[speculative-generality]] — 미래에 필요할 것이라는 추측만으로 만들어진 추상화·파라미터·클래스.

### Couplers
- [[feature-envy]] — 메서드가 자기 객체보다 다른 객체의 데이터에 더 관심을 보이는 상태.
- [[inappropriate-intimacy]] — 한 클래스가 다른 클래스의 내부 세부사항에 과하게 접근·의존하는 상태.
- [[message-chains]] — 클라이언트가 객체 그래프를 따라 연쇄 호출하며 내부 구조를 알아야 하는 상태.
- [[middle-man]] — 클래스가 의미 있는 책임 없이 대부분의 호출을 다른 객체에 위임만 하는 상태.

### Other Smells
- [[incomplete-library-class]] — 사용 중인 라이브러리가 필요한 기능을 제공하지 않지만 직접 수정하기 어려운 상태.

## 사용법

- smell 이름을 PR 코멘트의 vocabulary로 쓴다: “이 조건문은 [[switch-statements]]라서 `Replace Conditional with Polymorphism` 후보입니다.”
- 한 smell에 하나의 정답 technique이 있는 것은 아니다. 변경 축, 테스트 가능성, API 안정성에 따라 선택한다.
- smell 제거 자체가 목표가 아니라, 다음 변경의 비용과 위험을 낮추는 것이 목표다.

## References

- [[refactoring-guru-refactoring]]
