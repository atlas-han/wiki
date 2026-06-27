---
title: 프로토타입 (Prototype)
type: engineering
tags: [engineering, design-patterns, gof, creational]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [design-patterns, design-pattern-factory-method, design-pattern-abstract-factory, design-pattern-builder]
first-seen: refactoring-guru-ko-design-patterns
sources: [refactoring-guru-ko-design-patterns]
---

# 프로토타입 (Prototype)

코드가 객체의 구상 클래스에 의존하지 않고도 기존 객체를 복사(clone)해 새 객체를 만들 수 있게 하는 패턴이다. [[design-patterns]]의 생성 패턴에 속한다.

## 문제
객체를 외부에서 그대로 복제하려고 하면, 비공개(private) 필드에 접근할 수 없어 모든 상태를 복사하기 어렵다. 또 복사 코드가 객체의 구상 클래스에 의존하게 된다. 특히 인터페이스 타입으로만 객체를 받은 경우, 실제 클래스를 모르기 때문에 외부 코드에서 복제하기가 까다롭다.

## 해결책
복제를 객체 자신에게 위임한다. 복제를 지원하는 모든 객체가 공통 인터페이스(보통 `clone` 메서드 하나)를 선언하고, 각 ConcretePrototype이 자신의 상태(비공개 필드 포함)를 복사하는 로직을 구현한다. 클라이언트는 `clone`만 호출하면 되므로 구상 클래스를 알 필요가 없다. 자주 쓰는 prototype들을 prototype registry에 미리 등록해 이름으로 꺼내 복제할 수도 있다.

## 실세계 비유
산업용 시제품(프로토타입)은 실제로 스스로를 복제하지 않으므로, 이 패턴에 더 가까운 비유는 세포의 유사분열(mitosis)이다. 유사분열이 끝나면 원본과 동일한 한 쌍의 세포가 만들어진다. 즉 원본 객체가 자기 자신을 복제해 동일한 사본을 내놓는 것과 같다.

## 적용 가능성
- 복사할 객체의 구상 클래스에 코드가 의존해서는 안 될 때(인터페이스만 알고 있을 때)
- 객체 초기화 방식만 조금씩 다른 자식 클래스들의 수를 줄이고 싶을 때
- 미리 설정해 둔(pre-configured) 객체를 매번 새로 초기화하지 않고 복제해서 쓰고 싶을 때

## 장단점
**장점**
- 구상 클래스에 결합되지 않고 객체를 복제할 수 있다.
- 반복되는 초기화 코드를 미리 만들어 둔 prototype 복제로 대체할 수 있다.
- 복잡한 객체를 더 편리하게 생성할 수 있다.
- 복잡한 객체의 설정 변형을 상속 대신 prototype으로 다룰 수 있다.

**단점**
- 순환 참조가 있는 복잡한 객체를 복제하는 일은 매우 까다로울 수 있다.

## 다른 패턴과의 관계
- [[design-pattern-factory-method]]에서 출발한 설계가 더 유연함을 요구하면 [[design-pattern-abstract-factory]], [[design-pattern-builder]], 프로토타입으로 발전한다.
- [[design-pattern-abstract-factory]]를 프로토타입 집합으로 구현할 수 있다.
- [[design-pattern-memento]]의 더 간단한 대안이 될 수 있다(상태 객체가 단순하고 외부 리소스를 잡지 않을 때).
- [[design-pattern-command]] 기록을 저장하거나, [[design-pattern-composite]]/[[design-pattern-decorator]]로 만든 복잡한 구조를 복제할 때 유용하며, prototype을 [[design-pattern-singleton]]으로 둘 수도 있다.

## References
- [[refactoring-guru-ko-design-patterns]] — 프로토타입 원문: https://refactoring.guru/ko/design-patterns/prototype
- [[design-patterns]]
