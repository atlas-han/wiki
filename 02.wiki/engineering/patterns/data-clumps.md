---
title: Data Clumps
type: engineering
tags: [engineering, refactoring]
created: 2026-06-27
updated: 2026-06-27
category: pattern
related: [code-smells, refactoring-techniques, technical-debt]
first-seen: refactoring-guru-refactoring
sources: [refactoring-guru-refactoring]
---

# Data Clumps

여러 위치에서 늘 함께 몰려다니는 변수 묶음(예: 데이터베이스 연결 파라미터)이 반복적으로 나타나는 상태다. [[code-smells]] 중 **Bloaters(비대화)** 계열이다.

## 신호와 증상
- 서로 다른 코드 곳곳에서 동일한 변수 그룹이 반복해 등장한다(예: 데이터베이스 연결 파라미터).
- 여러 메서드의 파라미터 목록에 같은 값들이 같은 순서로 거듭 나타난다.
- 판별법: 값 하나를 빼봤을 때 나머지 값들이 의미를 잃는다면, 그 묶음은 객체로 합쳐야 한다는 신호다.

## 원인
이런 데이터 묶음은 보통 빈약한 프로그램 구조 설계나 코드 복사-붙여넣기로 생긴다.

## 해결 방법 (Treatment)
- `Extract Class` — 반복되는 필드들이 한 클래스 안에 있다면 그것들을 자체 클래스로 옮긴다.
- `Introduce Parameter Object` — 같은 데이터 묶음이 메서드 파라미터로 전달되면 하나의 객체로 묶는다.
- `Preserve Whole Object` — 일부 데이터가 다른 메서드로 넘어간다면 개별 필드 대신 전체 객체를 넘긴다.
- 이 필드들을 쓰는 코드를 살펴 [[data-class]]로 옮길 가치가 있는지 판단한다.

## 이득 (Payoff)
- 코드 전역에 흩어져 있던 특정 데이터에 대한 작업이 한곳으로 모여 이해도와 조직화가 좋아진다.
- 전체 코드 크기가 줄어든다.

## 무시해도 될 때
파라미터로 개별 원시 값 대신 객체 전체를 넘기면 두 클래스 사이에 불필요한 의존성이 생길 수 있다. 그런 경우라면 그대로 두는 편이 낫다.

## References
- [[refactoring-guru-refactoring]] — Data Clumps 원문: https://refactoring.guru/smells/data-clumps
- [[code-smells]]
