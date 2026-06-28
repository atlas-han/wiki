---
title: 전략 (Strategy)
type: engineering
tags: [engineering, design-patterns, gof, behavioral]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [design-patterns, design-pattern-chain-of-responsibility, design-pattern-command, design-pattern-iterator, actix-web-handlers-responders, actix-web-extractors]
first-seen: refactoring-guru-ko-design-patterns
sources: [refactoring-guru-ko-design-patterns]
---

# 전략 (Strategy)

알고리즘군을 정의하고 각각을 별도의 클래스에 캡슐화해, 그 객체들을 런타임에 상호 교체할 수 있도록 하는 패턴이다. [[design-patterns]]의 행동 패턴에 속한다.

## 문제
내비게이션 앱에서 도로·도보·대중교통·자전거 등 다양한 경로 계획 알고리즘을 하나의 메인 클래스에 계속 추가하다 보면 클래스가 비대해진다. 새 알고리즘을 추가할 때마다 기존 코드를 건드리게 되어 이미 동작하던 기능에 버그가 생길 위험이 커지고, 여러 사람이 같은 거대 클래스를 수정하면서 병합 충돌이 잦아진다.

## 해결책
같은 일을 하는 여러 알고리즘을 각각 독립된 클래스(Strategy)로 분리하고 공통 인터페이스를 구현하게 한다. 원래 클래스(Context)는 구체 전략을 직접 알지 않고 공통 인터페이스를 통해서만 위임한다. 클라이언트가 원하는 전략 객체를 골라 Context에 주입하므로, Context와 다른 전략을 수정하지 않고도 새 알고리즘을 추가하거나 런타임에 교체할 수 있다.

## 실세계 비유
공항에 가야 한다고 하자. 버스를 탈 수도, 택시를 부를 수도, 자전거를 탈 수도 있다. 이것들이 바로 운송 전략들이다. 예산과 시간 제약에 따라 그중 하나를 골라 실행하면 되고, 목적지(공항 도착)라는 목표는 동일하다.

## 적용 가능성
- 한 객체 안에서 알고리즘의 여러 변형을 사용하고, 런타임에 한 알고리즘에서 다른 알고리즘으로 전환하고 싶을 때
- 행동의 구현 방식만 다른 유사한 클래스가 많을 때
- 클래스의 비즈니스 로직을 그 안에서 그리 중요하지 않은 알고리즘 세부사항으로부터 분리하고 싶을 때
- 같은 알고리즘의 여러 변형을 선택하는 거대한 조건문으로 클래스가 오염되었을 때

## 장단점
**장점**
- 런타임에 객체 내부에서 사용하는 알고리즘을 교체할 수 있다
- 알고리즘 구현 세부사항을 사용하는 코드로부터 고립시킨다
- 상속을 합성으로 대체한다 (개방/폐쇄 원칙)

**단점**
- 알고리즘이 몇 개뿐이고 거의 바뀌지 않는다면 클래스·인터페이스가 늘어 과도하게 복잡해진다
- 클라이언트가 적절한 전략을 고르려면 전략 간 차이를 알아야 한다
- 함수형 언어에서는 익명 함수로 더 간단히 같은 효과를 낼 수 있다

## 다른 패턴과의 관계
- [[design-pattern-state]]와 구조는 사실상 같지만, Strategy의 알고리즘들은 서로를 전혀 인식하지 못하고 독립적으로 교체되는 반면 State는 상태 전이를 인지한다. State는 Strategy의 확장으로 간주된다
- [[design-pattern-template-method]]는 상속으로 알고리즘의 단계를 바꾸는 정적 방식인 반면, Strategy는 합성으로 알고리즘 전체를 런타임에 교체하는 동적 방식이다
- [[design-pattern-decorator]]는 객체의 겉(스킨)을 바꾸고 Strategy는 객체의 속(알맹이)을 바꾼다
- 전략 객체의 생성은 [[design-pattern-factory-method]]나 의존성 주입과 함께 구성할 수 있다

## References
- [[refactoring-guru-ko-design-patterns]] — 전략 (Strategy) 원문: https://refactoring.guru/ko/design-patterns/strategy
- [[design-patterns]]
- 실무 예: [[actix-web-handlers-responders]] (`Responder.respond_to` 다형성) · [[actix-web-extractors]] (`FromRequest` 타입별 추출)
