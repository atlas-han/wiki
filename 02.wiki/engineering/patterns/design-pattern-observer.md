---
title: 옵서버 (Observer)
type: engineering
tags: [engineering, design-patterns, gof, behavioral]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [design-patterns, design-pattern-chain-of-responsibility, design-pattern-command, design-pattern-iterator]
first-seen: refactoring-guru-ko-design-patterns
sources: [refactoring-guru-ko-design-patterns]
---

# 옵서버 (Observer)

한 객체(출판사)에 일어나는 이벤트를 자신을 구독 중인 여러 객체에게 자동으로 알리는 구독 메커니즘을 정의하는 패턴이다. [[design-patterns]]의 행동 패턴에 속한다.

## 문제
관심 있는 객체의 상태 변화를 다른 객체들이 알아야 할 때, 매번 상태를 직접 확인(폴링)하면 비효율적이고 불필요한 검사가 많아진다. 반대로 모든 객체에게 무차별적으로 알림을 보내면 관심 없는 객체들에게 불편을 준다. 구독자의 수와 종류를 미리 알 수 없고 런타임에 동적으로 변하는 상황에서 이 알림 관리가 특히 어렵다.

## 해결책
상태를 가진 객체(Publisher/Subject)에 구독 메커니즘(subscribe/unsubscribe/notify)을 추가해, 개별 객체들이 이벤트 스트림을 동적으로 구독·취소할 수 있게 한다. 모든 구독자(Subscriber/Observer)가 동일한 인터페이스(update)를 구현하면 출판사는 구체적인 구독자 클래스에 결합되지 않고 인터페이스에만 의존한다. 상태가 바뀌면 출판사가 등록된 구독자 목록을 순회하며 알림을 보낸다.

## 실세계 비유
신문이나 잡지를 구독하면 다음 호가 나왔는지 가게에 확인하러 갈 필요가 없다. 대신 출판사가 새 발행물을 구독자의 우편함으로 직접 보낸다. 출판사는 구독자 목록을 관리하며, 구독자는 언제든 구독을 취소할 수 있다.

## 적용 가능성
- 한 객체의 상태 변경이 다른 객체들의 변경을 요구하지만, 영향받을 객체들의 집합을 미리 알 수 없거나 런타임에 동적으로 변할 때
- GUI에서 버튼 클릭 같은 이벤트에 사용자 정의 코드를 연결해야 하지만, 어떤 코드가 반응할지 컴파일 타임에 고정하고 싶지 않을 때
- 앱의 일부 객체들이 제한된 시간 동안 또는 특정 경우에만 다른 객체를 관찰해야 할 때

## 장단점
**장점**
- 출판사 코드를 변경하지 않고도 새 구독자 클래스를 도입할 수 있다 (개방/폐쇄 원칙)
- 런타임에 객체 간 관계를 형성하고 해제할 수 있다

**단점**
- 구독자들이 알림을 받는 순서가 보장되지 않아 무작위로 통지된다
- 구독 취소를 누락하면 메모리 누수로 이어질 수 있다

## 다른 패턴과의 관계
- [[design-pattern-chain-of-responsibility]], [[design-pattern-command]], [[design-pattern-mediator]], 옵서버는 모두 발신자와 수신자를 연결하는 방식을 다루지만, 옵서버는 수신자들이 동적으로 구독·취소하는 단방향 브로드캐스트에 특화된다
- [[design-pattern-mediator]]는 컴포넌트 간 협업 로직을 중재자에 집중시키는 반면, 옵서버는 객체 간 단방향 구독 관계를 형성한다. 다만 옵서버를 이용해 중재자를 구현할 수도 있다

## References
- [[refactoring-guru-ko-design-patterns]] — 옵서버 (Observer) 원문: https://refactoring.guru/ko/design-patterns/observer
- [[design-patterns]]
