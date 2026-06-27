---
title: Dead Code
type: engineering
tags: [engineering, refactoring]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [code-smells, refactoring-techniques, technical-debt]
first-seen: refactoring-guru-refactoring
sources: [refactoring-guru-refactoring]
---

# Dead Code

변수·매개변수·필드·메서드·클래스가 더 이상 사용되지 않는 상태(대개 더 이상 쓸모없어졌기 때문). [[code-smells]] 중 **Dispensables(불필요한 것)** 계열이다.

## 신호와 증상
- 어디서도 호출·참조되지 않는 변수·필드·메서드·클래스가 남아 있다.
- 절대 참이 될 수 없는 조건 분기 등 도달 불가능한(unreachable) 코드가 있다.
- 코드를 읽을 때 실제로 쓰이는지 일일이 확인해야 한다.

## 원인
- 요구사항이 바뀌거나 버그를 고친 뒤 더 이상 필요 없어진 코드를 정리하지 않고 남겨둔다.
- 복잡한 조건문이 누적되면서 도달할 수 없는 분기가 생긴다.

## 해결 방법 (Treatment)
좋은 IDE를 활용하면 사용되지 않는 코드를 빠르게 찾을 수 있다.
- 사용되지 않는 코드와 파일은 그냥 삭제한다.
- `Inline Class` / `Collapse Hierarchy` — 거의 쓰이지 않는 클래스·서브클래스는 인라인하거나 계층을 합친다.
- `Remove Parameter` — 더 이상 쓰이지 않는 매개변수를 제거한다.

## 이득 (Payoff)
- 코드 크기가 줄어든다.
- 유지보수 시 살펴야 할 코드가 줄어 복잡도가 낮아진다.

## 무시해도 될 때
라이브러리·프레임워크처럼 외부 사용자가 호출할 수 있어 내부에서는 직접 쓰이지 않는 공개 API는 함부로 지우면 안 된다. 단위 테스트에서만 쓰이는 요소도 삭제 전에 확인해야 한다.

## References
- [[refactoring-guru-refactoring]] — Dead Code 원문: https://refactoring.guru/smells/dead-code
- [[code-smells]]
