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

여러 객체가 공통으로 가지는 상태를 객체마다 따로 저장하지 않고 서로 공유하게 하여 메모리 사용량을 줄인다. [[design-patterns]]의 구조 패턴에 속한다.

## 문제

비디오 게임의 입자(particle) 시스템에서 총알, 미사일, 파편을 각각 독립적인 객체로 표현한다고 하자. 입자가 대량으로 생성되면 RAM이 빠르게 소진되어 프로그램이 충돌한다. 원인은 색상이나 스프라이트처럼 메모리를 많이 차지하는 필드가 모든 입자 객체에 중복 저장되기 때문이다.

## 해결책

객체의 상태를 변하지 않고 공유 가능한 고유 상태(intrinsic state, 예: 색상·스프라이트)와 객체마다 다른 외부 상태(extrinsic state, 예: 좌표·속도)로 분리한다. 외부 상태는 메서드의 매개변수로 전달하고, 플라이웨이트 객체에는 고유 상태만 남겨 여러 콘텍스트가 같은 플라이웨이트를 재사용하게 한다. 보통 팩토리가 플라이웨이트 풀(캐시)을 관리해 동일한 고유 상태에 대해 하나의 인스턴스만 반환한다.

## 예시

숲을 렌더링할 때 나무마다 색상·텍스처 데이터를 통째로 저장하는 대신, 그 데이터를 몇 개의 플라이웨이트 객체에 보관한다. 그리고 좌표 같은 개별 정보만 가진 `Tree` 콘텍스트 객체들이 적절한 플라이웨이트를 참조하도록 연결한다. 수천 그루의 나무가 소수의 공유 객체를 가리키게 되어 메모리가 크게 절약된다.

## 적용 가능성

- 앱이 수많은 유사 객체를 생성해야 할 때
- 그 객체들이 대상 장치에서 사용 가능한 RAM을 거의 다 소모할 만큼 많을 때
- 객체들에 중복되는 상태가 들어 있고, 그 상태를 추출해 객체들 간에 공유할 수 있을 때

## 장단점

**장점**
- 유사한 객체가 많을 때 많은 양의 RAM을 절약할 수 있다

**단점**
- 플라이웨이트 메서드를 호출할 때마다 콘텍스트 데이터를 다시 계산해야 해서 CPU 시간이 더 들 수 있다 (메모리와 CPU의 트레이드오프)
- 고유/외부 상태를 분리하면서 코드 복잡도가 올라가 이해하기 어려워진다

## 다른 패턴과의 관계

- [[design-pattern-composite]] 트리의 공유되는 잎 노드를 플라이웨이트로 구현해 메모리를 아낄 수 있다.
- [[design-pattern-facade]]는 전체 하위 시스템을 대표하는 단일 객체를 만드는 반면, 플라이웨이트는 작은 객체를 다수 만들어 공유한다.
- [[design-pattern-singleton]]은 인스턴스를 하나만 두지만, 플라이웨이트는 서로 다른 고유 상태를 가진 여러 인스턴스를 둘 수 있고 불변이라는 점에서 다르다.
- 플라이웨이트 풀을 다룰 때 [[design-pattern-factory-method]]가 함께 쓰인다.

## References

- [[refactoring-guru-ko-design-patterns]] — 플라이웨이트 원문: https://refactoring.guru/ko/design-patterns/flyweight
- [[design-patterns]]
