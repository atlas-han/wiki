---
title: Middle Man
type: engineering
tags: [engineering, refactoring]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [code-smells, refactoring-techniques, technical-debt]
first-seen: refactoring-guru-refactoring
sources: [refactoring-guru-refactoring]
---

# Middle Man

클래스가 의미 있는 자기 책임 없이 대부분의 메서드를 그저 다른 객체로 위임만 하는 상태. [[code-smells]] 중 **Couplers(결합도 관련)** 계열이다.

## 신호와 증상
- 클래스의 메서드 대부분이 실제 일을 하지 않고 다른 클래스의 메서드를 그대로 호출(위임)하기만 한다.
- 한 가지 동작만 하면서 작업을 통째로 다른 클래스에 넘긴다면, 그 클래스가 존재할 이유가 의심된다.
- 위임만 하는 껍데기 계층이 늘어 호출 경로가 불필요하게 길어진다.

## 원인
- [[message-chains]]를 없애려고 `Hide Delegate`를 과하게 적용한 결과(과교정)로 위임 메서드만 잔뜩 남는 경우.
- 클래스의 쓸모 있는 일이 점차 다른 클래스로 빠져나가, 빈 껍질만 남는 경우.

## 해결 방법 (Treatment)
- `Remove Middle Man` — 대부분이 위임뿐이라면 중간자를 제거하고 클라이언트가 실제 대상과 직접 소통하게 한다.
- `Inline Method` — 위임 메서드가 거의 가치를 더하지 않으면 호출부에 인라인한다.
- 일부만 위임이고 자기 동작도 있다면, `Replace Delegation with Inheritance`로 위임을 상속으로 전환하는 것도 고려한다.

## 이득 (Payoff)
- 더 간결한 코드 구조를 얻는다.
- 불필요한 위임 계층이 사라져 호출 경로와 유지보수 부담이 준다.

## 무시해도 될 때
의도적으로 만든 미들맨은 제거하면 안 된다. 클래스 간 직접 의존을 끊기 위해 일부러 둔 경우, 또는 [[design-pattern-proxy]]·[[design-pattern-decorator]]처럼 위임 자체가 패턴의 목적인 경우(접근 제어·기능 추가 등)는 정상이다. 일부 결합과 위임은 받아들일 수 있다.

## References
- [[refactoring-guru-refactoring]] — Middle Man 원문: https://refactoring.guru/smells/middle-man
- [[code-smells]]
