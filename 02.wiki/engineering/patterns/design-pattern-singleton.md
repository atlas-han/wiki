---
title: 싱글턴 (Singleton)
type: engineering
tags: [engineering, design-patterns, gof, creational]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [design-patterns, design-pattern-factory-method, design-pattern-abstract-factory, design-pattern-builder]
first-seen: refactoring-guru-ko-design-patterns
sources: [refactoring-guru-ko-design-patterns]
---

# 싱글턴 (Singleton)

클래스의 인스턴스가 단 하나만 존재하도록 보장하면서, 그 인스턴스에 대한 전역 접근 지점(global access point)을 제공하는 패턴이다. [[design-patterns]]의 생성 패턴에 속한다.

## 문제
싱글턴은 사실 두 가지 문제를 동시에 풀려 한다. 첫째, 데이터베이스나 파일 같은 공유 리소스에 대한 접근을 관리하기 위해 클래스의 인스턴스 개수를 하나로 제어해야 한다. 둘째, 전역 변수처럼 어디서나 접근 가능하되 다른 코드가 그 인스턴스를 덮어쓰지 못하게 막는, 통제된 전역 접근 지점이 필요하다.

## 해결책
생성자를 비공개(private)로 만들어 외부에서 `new`로 직접 인스턴스를 만들지 못하게 막고, 정적(static) 생성 메서드(`getInstance`)를 제공한다. 이 메서드는 첫 호출 시 인스턴스를 생성해 정적 필드에 캐시하고, 이후 호출에서는 캐시된 동일 인스턴스를 반환한다. 그 결과 인스턴스는 처음 요청될 때만 초기화된다(지연 초기화).

## 실세계 비유
한 국가는 오직 하나의 공식 정부만 가질 수 있다. "국가의 정부"라는 명칭은, 구체적으로 누가 정부를 구성하는 사람들인지와 무관하게 그 책임자 그룹을 가리키는 전역 접근 지점 역할을 한다.

## 적용 가능성
- 모든 클라이언트가 공유하는 단일 인스턴스가 꼭 하나만 있어야 할 때(예: 프로그램 전역에서 공유되는 데이터베이스 객체)
- 전역 변수에 대해 더 엄격한 접근 제어가 필요할 때(전역 변수와 달리 덮어쓰기를 막을 수 있음)

## 장단점
**장점**
- 클래스에 인스턴스가 단 하나만 존재함을 보장한다.
- 그 인스턴스에 대한 전역 접근 지점을 제공한다.
- 싱글턴 객체는 처음 요청될 때만 초기화된다(지연 초기화).

**단점**
- 두 가지 문제를 한꺼번에 풀어 단일 책임 원칙(SRP)을 위반한다.
- 컴포넌트 간 결합이 과도한 등의 잘못된 설계를 가릴 수 있다.
- 다중 스레드 환경에서는 여러 스레드가 동시에 인스턴스를 생성하지 않도록 잠금(lock) 등 특별한 처리가 필요하다.
- 유닛 테스트가 어렵다. 생성자가 비공개이고 정적 메서드를 오버라이드할 수 없어, 상속에 의존하는 테스트 프레임워크로 모의 객체(mock)를 만들기 까다롭고 전역 상태가 테스트 간에 공유된다.

## 다른 패턴과의 관계
- [[design-pattern-facade]] 클래스는 종종 싱글턴으로 변환될 수 있다(대개 단일 facade 객체로 충분하므로).
- [[design-pattern-flyweight]]와 비슷해 보이지만, 싱글턴은 단 하나의 변경 가능한 인스턴스를 두는 반면 flyweight는 여러 개의 불변 인스턴스를 둔다.
- [[design-pattern-abstract-factory]], [[design-pattern-builder]], [[design-pattern-prototype]]은 싱글턴으로 구현될 수 있다.

## References
- [[refactoring-guru-ko-design-patterns]] — 싱글턴 원문: https://refactoring.guru/ko/design-patterns/singleton
- [[design-patterns]]
