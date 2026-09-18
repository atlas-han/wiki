---
title: Technical Debt
type: engineering
tags: [engineering, refactoring]
created: 2026-06-27
updated: 2026-09-18
category: pattern
related: [refactoring, code-smells, surgical-edits, legacy-code-modernization, legacy-skills-gap]
first-seen: refactoring-guru-refactoring
sources: [refactoring-guru-refactoring, tech-bridge-legacy-code-modernization-ai]
---

# Technical Debt

Technical Debt는 “지금 빠르게 가기 위해 구조 개선을 미룬 선택”이 이후 변경 때마다 이자처럼 비용을 발생시키는 상태다. [[refactoring]]은 새 기능을 추가하지 않고 이 이자를 줄이는 대표적 상환 수단이다.

## 실무 해석

- debt 자체가 항상 나쁜 것은 아니다. 문제는 **의식적 debt인지**, **상환 시점과 비용을 추적하는지**다.
- [[code-smells]]는 debt가 코드 표면에 드러난 신호다. 예: [[duplicate-code]]는 수정 누락 위험, [[shotgun-surgery]]는 변경 비용, [[primitive-obsession]]은 도메인 표현력 부족을 만든다.
- 상환은 rewrite가 아니라 작은 [[refactoring-techniques]]의 누적이어야 한다. [[surgical-edits]] 원칙처럼 요청과 직접 관련 없는 대규모 정리는 오히려 위험하다.

## 상환 우선순위

1. 지금 만드는 feature와 같은 변경 축에 있는 smell
2. 테스트로 behavior 보존을 검증할 수 있는 영역
3. 반복 수정·장애·온보딩 지연의 실제 비용이 관찰된 영역
4. 단순 취향 문제가 아니라 coupling/cohesion/duplication을 개선하는 영역

## References

- [[refactoring-guru-refactoring]]

## 보안 이자와 인력 이자 (2026-09-18 · [[tech-bridge-legacy-code-modernization-ai]])

이 페이지의 debt는 *변경 비용의 이자* 였다. [[anna-gutowska|Anna Gutowska]]([[ibm|IBM]])가 레거시 코드를 다루며 **이자의 종류를 둘 더 준다.**

> 그러한 **기술적 부채는 누적되어 실제 보안 위험을 초래**하고 있습니다. 이러한 시스템은 **보안 패치를 받지 못하므로 최신 규정 준수 기준을 충족하지 못합니다.** 기다리는 해가 길어질수록 **취약점 표면은 더 커집니다.** (03:11~03:33)

> **개발자 수가 많다고 해서 현대화 속도가 빨라지는 것은 아닙니다.** (…) 오래된 시스템을 깊이 이해하는 개발자들이 **은퇴하고 있습니다.** (02:15~02:39)

| 이자 | 무엇이 쌓이는가 | 이 위키의 페이지 |
|---|---|---|
| 변경 비용 (기존) | 수정할 때마다 드는 시간 | [[refactoring]] · [[code-smells]] |
| **보안** | 패치·규정 준수 불가 → 취약점 표면 | [[legacy-code-modernization]] · [[shift-left-security]] |
| **인력** | 부채를 갚을 줄 아는 사람이 사라진다 | [[legacy-skills-gap]] |

그리고 이 페이지의 *"상환은 rewrite가 아니라 작은 [[refactoring-techniques]]의 누적"* 과 같은 결론을 그 소스도 낸다 — *"현대화는 기존 프로세스를 유지하면서 그 아래에서 기술이 발전하는 **점진적인 과정**"*(07:21~07:29). ⚠️ 소스는 수치·사례 없이 일반론으로 말한다.
