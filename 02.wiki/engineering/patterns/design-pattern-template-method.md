---
title: 템플릿 메서드 (Template Method)
type: engineering
tags: [engineering, design-patterns, gof, behavioral]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [design-patterns, design-pattern-chain-of-responsibility, design-pattern-command, design-pattern-iterator]
first-seen: refactoring-guru-ko-design-patterns
sources: [refactoring-guru-ko-design-patterns]
---

# 템플릿 메서드 (Template Method)

부모 클래스에서 알고리즘의 골격을 정의하되, 자식 클래스들이 그 알고리즘의 특정 단계들을 구조를 바꾸지 않고 오버라이드할 수 있게 하는 패턴이다. [[design-patterns]]의 행동 패턴에 속한다.

## 문제
PDF·DOC·CSV 등 다양한 파일 형식을 처리하는 데이터 마이닝 앱을 만들다 보면, 형식별 처리 클래스들이 서로 유사한 로직을 중복으로 갖게 된다. 파일을 열고 데이터를 추출하는 부분은 형식마다 다르지만, 추출 후의 데이터 처리·분석·보고서 생성 코드는 거의 동일해서 클래스마다 같은 코드가 반복된다. 이 중복은 유지보수를 어렵게 하고, 클라이언트 코드도 형식별 분기 조건문으로 복잡해진다.

## 해결책
알고리즘을 일련의 단계로 분해하고, 부모 클래스(AbstractClass)의 템플릿 메서드에서 이 단계들을 정해진 순서로 호출한다. 각 단계는 추상 메서드로 두거나 기본 구현을 제공하며, 자식 클래스(ConcreteClass)는 알고리즘 구조와 공통 단계는 그대로 둔 채 형식마다 달라지는 단계만 오버라이드한다. 선택적으로 오버라이드할 수 있는 빈 기본 구현인 후크(hook) 단계도 둘 수 있다.

## 실세계 비유
표준 주택 건설 계획에는 잠재적 주택 소유자가 결과물의 일부 세부 사항을 조정할 수 있도록 하는 여러 확장 지점이 포함될 수 있다. 골조·배관 같은 큰 단계와 순서는 표준 계획이 고정하고, 소유자는 벽 재질이나 난방 방식 같은 일부 단계만 자기 취향대로 바꾼다.

## 적용 가능성
- 클라이언트가 알고리즘 전체가 아니라 특정 단계들만 확장하게 하고, 전체 구조나 다른 단계는 건드리지 못하게 하고 싶을 때
- 비슷하지만 사소하게 다른 알고리즘을 가진 여러 클래스가 있어, 알고리즘이 바뀌면 모든 클래스를 수정해야 할 때
- 알고리즘의 구조는 유지하면서 형식별·경우별 중복 코드를 부모 클래스로 끌어올리고 싶을 때

## 장단점
**장점**
- 클라이언트가 큰 알고리즘의 특정 부분만 오버라이드하게 해, 다른 부분의 변경에 덜 영향받게 한다
- 중복 코드를 부모 클래스 하나로 끌어올릴 수 있다

**단점**
- 일부 클라이언트는 제공된 알고리즘 골격에 의해 자유가 제한될 수 있다
- 자식 클래스가 기본 단계 구현을 억제하면 리스코프 치환 원칙을 위반할 수 있다
- 단계 수가 많아질수록 템플릿 메서드를 유지보수하기 어려워진다

## 다른 패턴과의 관계
- [[design-pattern-factory-method]]는 템플릿 메서드의 특수화로, 큰 템플릿 메서드의 한 단계 역할을 할 수 있다
- [[design-pattern-strategy]]는 상속이 아니라 합성을 기반으로 한다. 템플릿 메서드는 상속으로 클래스 단위 동작을 정적으로 바꾸는 반면, Strategy는 객체에 위임해 런타임에 동작을 전환한다

## References
- [[refactoring-guru-ko-design-patterns]] — 템플릿 메서드 (Template Method) 원문: https://refactoring.guru/ko/design-patterns/template-method
- [[design-patterns]]
