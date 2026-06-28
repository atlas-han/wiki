---
title: 어댑터 (Adapter)
type: engineering
tags: [engineering, design-patterns, gof, structural]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [design-patterns, design-pattern-bridge, design-pattern-composite, design-pattern-decorator, actix-web-extractors]
first-seen: refactoring-guru-ko-design-patterns
sources: [refactoring-guru-ko-design-patterns]
---

# 어댑터 (Adapter)

호환되지 않는 인터페이스를 가진 객체들이 협업할 수 있도록 한 객체의 인터페이스를 다른 객체가 기대하는 형식으로 변환한다. [[design-patterns]]의 구조 패턴에 속한다.

## 문제

기존 애플리케이션이 XML 데이터로 동작하는데, 새로 통합하려는 타사 분석 라이브러리는 JSON 형식만 지원한다고 하자. 라이브러리의 소스 코드는 수정할 수 없고, 그렇다고 앱 전체를 JSON으로 바꾸면 기존 코드가 망가질 위험이 있다. 서로 형식이 맞지 않는 두 객체를 그대로 연결하면 호환성 문제가 발생한다.

## 해결책

어댑터는 한쪽 객체와 호환되는 인터페이스를 제공하고, 호출을 받으면 이를 다른 객체가 이해할 수 있는 형식으로 변환해 전달하는 중간 객체다. 클라이언트는 Target 인터페이스로 어댑터를 호출하고, 어댑터는 내부에서 Adaptee(서비스 객체)의 호출로 변환한다. 합성(object adapter)으로 구현하면 어댑터가 서비스 객체를 감싸고, 상속(class adapter)으로 구현하면 두 인터페이스를 동시에 상속한다.

## 실세계 비유

해외 여행 시 미국식 전원 플러그는 독일 소켓에 맞지 않는다. 이때 미국식 소켓과 유럽식 플러그를 함께 가진 전원 어댑터를 끼우면 양쪽이 문제없이 연결된다. 어댑터 패턴이 서로 다른 두 인터페이스를 중개하는 방식과 같다.

## 적용 가능성

- 기존 클래스를 사용하고 싶지만 그 인터페이스가 나머지 코드와 호환되지 않을 때
- 레거시 클래스나 타사 클래스를 도메인 인터페이스 뒤에 붙이는 변환기가 필요할 때
- 여러 기존 자식 클래스를 재사용하면서, 상위 클래스에 추가하기 어려운 공통 기능을 보강해야 할 때

## 장단점

**장점**
- 단일 책임 원칙: 인터페이스 변환 코드를 비즈니스 로직에서 분리할 수 있다
- 개방/폐쇄 원칙: 기존 클라이언트 코드를 건드리지 않고 새 어댑터를 도입할 수 있다

**단점**
- 새로운 인터페이스와 클래스가 늘어나 전체 코드 복잡성이 증가한다
- 때로는 서비스 클래스를 직접 수정하는 편이 더 간단할 수 있다

## 다른 패턴과의 관계

- [[design-pattern-bridge]]는 앱 개발 전에 미리 설계해 추상화와 구현을 독립적으로 발전시키지만, 어댑터는 이미 존재하는 비호환 클래스들을 사후에 협업시킨다.
- [[design-pattern-decorator]]는 인터페이스를 바꾸지 않고 객체를 향상시키며 재귀적 합성을 지원하지만, 어댑터는 인터페이스 자체를 변경한다.
- [[design-pattern-proxy]]는 원본과 동일한 인터페이스를 제공하지만, 어댑터는 다른 인터페이스를 제공한다.
- [[design-pattern-facade]]는 여러 객체로 된 하위 시스템에 새 인터페이스를 정의하지만, 어댑터는 보통 하나의 객체만 래핑한다.

## References

- [[refactoring-guru-ko-design-patterns]] — 어댑터 원문: https://refactoring.guru/ko/design-patterns/adapter
- [[design-patterns]]
- 실무 예: [[actix-web-extractors]] — `FromRequest`가 raw 요청을 타입 안전 값(`Path`/`Json`/`Query`)으로 변환
