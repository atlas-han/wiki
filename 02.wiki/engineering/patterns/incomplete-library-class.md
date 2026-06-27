---
title: Incomplete Library Class
type: engineering
tags: [engineering, refactoring]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [code-smells, refactoring-techniques, technical-debt]
first-seen: refactoring-guru-refactoring
sources: [refactoring-guru-refactoring]
---

# Incomplete Library Class

사용 중인 라이브러리 클래스가 필요한 기능을 제공하지 않지만, 읽기 전용이라 직접 수정하기 어려운 상태. [[code-smells]] 중 **Couplers(결합도 관련) / 기타** 계열이다(refactoring.guru에서는 Other Smells로 분류).

## 신호와 증상
- 외부 라이브러리가 우리가 필요로 하는 기능을 더 이상 충족하지 못한다.
- 라이브러리는 읽기 전용이라 클래스 자체를 고칠 수 없다.
- 부족한 기능을 호출부마다 우회 구현해 비슷한 코드가 여러 곳에 중복된다.

## 원인
- 라이브러리 작성자가 필요한 기능을 애초에 제공하지 않았거나, 추가 요청을 거부(또는 구현하지 않음)했기 때문이다.

## 해결 방법 (Treatment)
- `Introduce Foreign Method` — 메서드 한두 개만 더 필요하다면, 라이브러리 클래스를 인자로 받는 보조 메서드를 클라이언트 쪽에 추가한다.
- `Introduce Local Extension` — 추가할 기능이 많다면, 라이브러리 클래스를 상속하거나 감싸는 별도 확장 클래스를 만들어 새 동작을 그곳에 모은다.

## 이득 (Payoff)
- 부족한 기능을 우회하느라 생기는 코드 중복이 줄어든다.
- 기존 라이브러리를 그대로 활용하므로 처음부터 새로 만들 필요가 없다.

## 무시해도 될 때
라이브러리를 확장하면, 이후 라이브러리 변경이 우리 확장 코드에 영향을 줘 추가 유지보수가 생길 수 있다. 확장 비용이 얻는 이득보다 크다면 무리해서 손대지 않는다.

## References
- [[refactoring-guru-refactoring]] — Incomplete Library Class 원문: https://refactoring.guru/smells/incomplete-library-class
- [[code-smells]]
