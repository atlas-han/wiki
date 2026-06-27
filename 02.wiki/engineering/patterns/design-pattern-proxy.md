---
title: 프록시 (Proxy)
type: engineering
tags: [engineering, design-patterns, gof, structural]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [design-patterns, design-pattern-adapter, design-pattern-bridge, design-pattern-composite]
first-seen: refactoring-guru-ko-design-patterns
sources: [refactoring-guru-ko-design-patterns]
---

# 프록시 (Proxy)

원본 객체에 대한 대리자를 제공해 접근을 제어하거나 부가 동작을 삽입한다. [[design-patterns]]의 구조 패턴에 속하며, 원문 기준 URL은 `https://refactoring.guru/ko/design-patterns/proxy`이다.

## 문제 신호

원격 호출, lazy loading, cache, access control, logging처럼 객체 접근 전후 제어가 필요할 때.

## 구조

Proxy가 Subject 인터페이스를 구현하고 RealSubject 참조를 보유해 호출을 위임하며 필요한 제어를 추가한다.

## 적용 메모

- 클라이언트가 구상 타입이나 구체 협력자를 직접 알아야 하는 지점을 줄이는 데 초점을 둔다.
- 패턴명보다 중요한 것은 변경 축이다. 변경 축이 없거나 단순하면 일반 함수/클래스/언어 기능으로 충분할 수 있다.
- 테스트에서는 패턴이 만든 seam을 활용해 구상 구현 대신 fake/mock을 주입할 수 있는지 확인한다.

## 장단점

클라이언트 변경 없이 접근 정책을 넣을 수 있다. 지연/네트워크/권한 실패가 숨겨져 예측성이 낮아질 수 있다.

## 관련 패턴

[[design-pattern-decorator]]와 구조는 같지만 목적이 다르다. [[design-pattern-facade]]는 여러 객체의 단순 진입점이고 Proxy는 한 객체의 대리자다.

## References

- [[refactoring-guru-ko-design-patterns]] — 프록시 원문: https://refactoring.guru/ko/design-patterns/proxy
- [[design-patterns]]
