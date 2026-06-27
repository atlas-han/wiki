---
title: 플라이웨이트 (Flyweight)
type: engineering
tags: [engineering, design-patterns, gof, structural]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [design-patterns, design-pattern-adapter, design-pattern-bridge, design-pattern-composite]
first-seen: refactoring-guru-ko-design-patterns
sources: [refactoring-guru-ko-design-patterns]
---

# 플라이웨이트 (Flyweight)

많은 유사 객체가 공유할 수 있는 intrinsic state를 분리해 메모리를 절약한다. [[design-patterns]]의 구조 패턴에 속하며, 원문 기준 URL은 `https://refactoring.guru/ko/design-patterns/flyweight`이다.

## 문제 신호

대량 객체가 동일한 불변 데이터를 반복 보관해 메모리 압박이 큰 경우.

## 구조

Flyweight는 공유 가능한 intrinsic state만 갖고, extrinsic state는 호출자가 전달한다. Factory가 flyweight cache를 관리한다.

## 적용 메모

- 클라이언트가 구상 타입이나 구체 협력자를 직접 알아야 하는 지점을 줄이는 데 초점을 둔다.
- 패턴명보다 중요한 것은 변경 축이다. 변경 축이 없거나 단순하면 일반 함수/클래스/언어 기능으로 충분할 수 있다.
- 테스트에서는 패턴이 만든 seam을 활용해 구상 구현 대신 fake/mock을 주입할 수 있는지 확인한다.

## 장단점

메모리 사용을 크게 줄일 수 있다. 상태 분리와 cache 관리가 복잡하고, 불변성/동시성 정책이 중요하다.

## 관련 패턴

[[design-pattern-prototype]]이 복제로 생성 비용을 줄인다면 Flyweight는 공유로 메모리 비용을 줄인다. Factory 관리는 [[design-pattern-factory-method]]와 연결된다.

## References

- [[refactoring-guru-ko-design-patterns]] — 플라이웨이트 원문: https://refactoring.guru/ko/design-patterns/flyweight
- [[design-patterns]]
