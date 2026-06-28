---
title: 데코레이터 (Decorator)
type: engineering
tags: [engineering, design-patterns, gof, structural]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [design-patterns, design-pattern-adapter, design-pattern-bridge, design-pattern-composite, actix-web-middleware]
first-seen: refactoring-guru-ko-design-patterns
sources: [refactoring-guru-ko-design-patterns]
---

# 데코레이터 (Decorator)

객체를 새로운 행동이 담긴 특수 래퍼(wrapper) 객체 안에 넣어, 그 행동을 원래 객체에 동적으로 연결한다. [[design-patterns]]의 구조 패턴에 속한다.

## 문제

알림 라이브러리가 처음에는 이메일 알림만 지원했는데, 사용자들이 SMS, 페이스북, 슬랙 등 여러 채널과 그 조합을 요청하기 시작했다. 이를 상속으로 구현하면 채널 조합마다 새 자식 클래스(예: SMS+슬랙, 이메일+SMS+페이스북)가 필요해 클래스 수가 폭발적으로 늘어난다.

## 해결책

상속 대신 합성을 사용해 객체를 래퍼로 감싼다. 래퍼는 감싼 대상과 동일한 인터페이스를 구현하므로 클라이언트 입장에서는 원본과 구별되지 않는다. 래퍼는 요청을 내부 객체에 위임하면서 그 전후에 자신의 동작을 추가하며, 여러 래퍼를 중첩해 다양한 행동 조합을 런타임에 동적으로 구성할 수 있다.

## 실세계 비유

옷을 겹쳐 입는 것과 같다. 추울 때는 스웨터를 입고, 더 추우면 그 위에 재킷을 걸치고, 비가 오면 비옷까지 덧입는다. 각 옷은 기본 행동(체온 유지, 방수)을 "확장"하지만, 필요 없어지면 언제든 하나씩 벗을 수 있다.

## 적용 가능성

- 객체를 사용하는 코드를 훼손하지 않으면서 런타임에 객체에 추가 행동을 부여해야 할 때
- 상속으로 객체의 행동을 확장하기 어렵거나 어색할 때
- `final` 등으로 상속이 막혀 있어 클래스의 행동을 다른 방법으로 확장해야 할 때

## 장단점

**장점**
- 새 자식 클래스를 만들지 않고도 객체의 행동을 확장할 수 있다
- 런타임에 책임을 동적으로 추가하거나 제거할 수 있다
- 여러 데코레이터로 래핑해 행동들을 자유롭게 조합할 수 있다
- 단일 책임 원칙: 다양한 변형을 작은 클래스들로 나눌 수 있다

**단점**
- 래퍼 스택 중간의 특정 래퍼를 제거하기 어렵다
- 데코레이터의 순서에 동작이 의존하지 않도록 구현하기 까다롭다
- 계층을 구성하는 초기 설정 코드가 복잡해질 수 있다

## 다른 패턴과의 관계

- [[design-pattern-adapter]]는 인터페이스를 변경하지만, 데코레이터는 인터페이스를 그대로 두고 객체를 향상시킨다.
- [[design-pattern-proxy]]와 구조는 거의 같지만 의도가 다르다. 데코레이터는 기능을 추가하는 것이 목적이고, 프록시는 접근 제어가 목적이다. 또 데코레이터는 보통 클라이언트가 수명 주기를 제어하고, 프록시는 스스로 관리한다.
- [[design-pattern-chain-of-responsibility]]와 유사하게 래퍼 체인을 이루지만, 책임 연쇄는 요청 전달을 도중에 중단할 수 있는 반면 데코레이터는 항상 흐름을 계속 이어간다.
- [[design-pattern-composite]]와 달리 데코레이터는 자식 컴포넌트를 하나만 가진다.

## References

- [[refactoring-guru-ko-design-patterns]] — 데코레이터 원문: https://refactoring.guru/ko/design-patterns/decorator
- [[design-patterns]]
- 실무 예: [[actix-web-middleware]] — `Transform`+`Service` 미들웨어가 내부 service를 감싸 전·후처리 추가
