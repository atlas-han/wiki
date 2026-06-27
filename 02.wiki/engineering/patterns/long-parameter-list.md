---
title: Long Parameter List
type: engineering
tags: [engineering, refactoring]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [code-smells, refactoring-techniques, technical-debt]
first-seen: refactoring-guru-refactoring
sources: [refactoring-guru-refactoring]
---

# Long Parameter List

메서드 호출에 필요한 파라미터가 지나치게 많아(보통 3~4개를 넘김) 호출자와 구현이 강하게 얽힌 상태다. [[code-smells]] 중 **Bloaters(비대화)** 계열이다.

## 신호와 증상
- 메서드의 파라미터가 3~4개를 넘는다.
- 파라미터 일부가 늘 함께 따라다녀 [[data-clumps]]를 이룬다.
- 호출부마다 같은 객체에서 값을 하나씩 꺼내 여러 개로 풀어 넘긴다.

## 원인
여러 알고리즘을 한 메서드로 합치다 보면 파라미터가 늘어난다. 또 긴 파라미터 목록은 클래스 간 의존을 줄이려는 시도의 부산물일 수 있다 — 객체 생성 코드를 메서드 안이 아니라 호출부로 옮기면, 생성된 객체들이 다시 파라미터로 전달되어 목록이 길어진다.

## 해결 방법 (Treatment)
- `Replace Parameter with Method Call` — 어떤 파라미터 값이 다른 객체의 메서드 호출로 얻어진다면, 그 호출을 메서드 안으로 옮겨 파라미터를 없앤다.
- `Preserve Whole Object` — 한 객체에서 꺼낸 여러 값을 넘기는 대신 객체 자체를 넘긴다.
- `Introduce Parameter Object` — 여러 출처에서 온 파라미터들을 하나의 파라미터 객체로 묶는다.

## 이득 (Payoff)
- 더 읽기 쉽고 짧은 코드가 된다.
- 가려져 있던 중복 코드([[duplicate-code]])가 드러날 수 있다.

## 무시해도 될 때
파라미터를 줄이려고 객체 전체를 넘기면 클래스 간에 불필요한 의존성이 생길 수 있다. 그런 의존을 피해야 하는 상황이라면 긴 파라미터 목록을 그대로 두는 편이 낫다.

## References
- [[refactoring-guru-refactoring]] — Long Parameter List 원문: https://refactoring.guru/smells/long-parameter-list
- [[code-smells]]
