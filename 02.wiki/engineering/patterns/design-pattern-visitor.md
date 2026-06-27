---
title: 비지터 (Visitor)
type: engineering
tags: [engineering, design-patterns, gof, behavioral]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [design-patterns, design-pattern-chain-of-responsibility, design-pattern-command, design-pattern-iterator]
first-seen: refactoring-guru-ko-design-patterns
sources: [refactoring-guru-ko-design-patterns]
---

# 비지터 (Visitor)

알고리즘을 그것이 작동하는 객체들로부터 분리하여, 객체 구조를 바꾸지 않고 새로운 연산을 추가할 수 있게 하는 패턴이다. [[design-patterns]]의 행동 패턴에 속한다.

## 문제
이미 잘 동작하는 객체 구조(예: 도시·건물·도로로 이루어진 지리 정보 그래프)의 모든 노드에 대해 새 기능(예: XML로 내보내기)을 추가해야 할 때, 각 노드 클래스에 메서드를 직접 추가하면 안정적인 클래스들을 모두 수정해야 해서 위험하다. 게다가 보조적인 동작(내보내기·통계 집계 등)을 핵심 비즈니스 클래스에 섞으면 그 클래스의 주된 책임이 흐려지고, 앞으로 비슷한 기능 요청이 들어올 때마다 같은 수정을 반복해야 한다.

## 해결책
새 동작을 노드 클래스가 아니라 별도의 비지터(Visitor) 클래스에 캡슐화하고, 각 노드 타입마다 대응하는 `visit` 메서드를 비지터에 둔다. 각 요소(Element)는 자신을 인자로 비지터의 알맞은 메서드를 호출해 주는 `accept(visitor)` 메서드를 구현한다. 이 이중 디스패치(double dispatch)를 통해, 요소의 실제 타입과 비지터의 실제 타입 양쪽에 따라 올바른 `visit` 메서드가 선택된다.

## 실세계 비유
노련한 보험 대리인을 상상해 보자. 그는 근방의 모든 건물을 방문하는데, 방문한 건물에 있는 회사나 조직의 유형에 따라 맞춤형 보험 정책을 제안한다. 주거용 건물에는 의료 보험을, 은행에는 도난 보험을, 카페에는 화재·홍수 보험을 제시하는 식이다. 건물(요소)은 그대로 두고, 방문자(비지터)가 타입별로 다른 동작을 수행한다.

## 적용 가능성
- 복잡한 객체 구조(예: 객체 트리)의 모든 요소에 대해 어떤 연산을 수행해야 할 때
- 보조적인 동작의 비즈니스 로직을 핵심 클래스에서 떼어내 한곳에 정리하고 싶을 때
- 어떤 동작이 클래스 계층의 일부 클래스에만 의미가 있고, 다른 클래스에는 무의미할 때

## 장단점
**장점**
- 다른 클래스를 바꾸지 않고 그 객체들과 함께 작동하는 새 동작을 도입할 수 있다 (개방/폐쇄 원칙)
- 같은 동작의 여러 버전을 한 비지터 클래스로 모은다 (단일 책임 원칙)
- 비지터 객체가 여러 요소를 순회하며 유용한 정보를 축적할 수 있다

**단점**
- 요소 클래스 계층에 클래스를 추가하거나 제거할 때마다 모든 비지터를 갱신해야 한다
- 비지터가 요소의 비공개 필드·메서드에 접근할 권한이 없을 수 있다

## 다른 패턴과의 관계
- [[design-pattern-command]]의 강력한 버전으로 볼 수 있다. 비지터 객체는 다양한 클래스의 객체에 대해 연산을 실행할 수 있다
- [[design-pattern-composite]] 트리 전체를 순회하며 각 노드에 어떤 연산을 수행할 때 비지터를 함께 쓰면 강력하다
- [[design-pattern-iterator]]와 함께 사용해 복잡한 데이터 구조를 순회하면서, 요소 타입이 달라도 비지터로 각 요소에 연산을 적용할 수 있다

## References
- [[refactoring-guru-ko-design-patterns]] — 비지터 (Visitor) 원문: https://refactoring.guru/ko/design-patterns/visitor
- [[design-patterns]]
