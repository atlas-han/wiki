---
title: Technical Debt
type: engineering
tags: [engineering, refactoring]
created: 2026-06-27
updated: 2026-11-20
category: pattern
related: [refactoring, code-smells, surgical-edits, legacy-code-modernization, legacy-skills-gap]
first-seen: refactoring-guru-refactoring
sources: [refactoring-guru-refactoring, tech-bridge-legacy-code-modernization-ai, tech-bridge-g2i-generation-cheap-evaluation-expensive, tech-bridge-kanat-alexander-disposable-vs-durable, tech-bridge-jonathan-blow-30-years-zero-progress]
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

- (2026-10-15 · [[tech-bridge-g2i-generation-cheap-evaluation-expensive]]) *"any line of code you write is a liability, that the best code is no code at all. The cost of creating code is falling, but the cost of understanding a software program is not."*(02:54~03:06) 생성 비용이 떨어져도 **이해 비용**은 그대로라는 진술이다.

## 변경의 두 번째 위험 — 다음 변경을 어렵게 만드는 것 (2026-10-25 · [[tech-bridge-kanat-alexander-disposable-vs-durable]])

[[max-kanat-alexander|Max Kanat-Alexander]](발췌): 변경의 위험은 둘이다. 하나는 지금 바꾸는 과정의 문제이고, 둘째는 *"you could make it harder to make future changes. In particular, what that means is you could make it more likely to have future problems."*(01:18~01:25) 해설의 예: 할인 기능을 급하게 붙이면 오늘 결제가 틀릴 수도 있고, *"코드가 복잡해져서 다음 수정이 더 어려워질 수도"* 있다. 이 비용을 오래 감당할 필요가 없는 **disposable** 코드에서만 부채를 무시할 수 있다. → [[disposable-vs-durable-software]]

## 2026-11-20 — 양이 곧 빚: 같은 문제에 더 많은 코드 ([[tech-bridge-jonathan-blow-30-years-zero-progress]])

[[jonathan-blow|Jonathan Blow]]는 부채를 *미룬 구조 개선* 이 아니라 **같은 문제에 대한 코드의 양** 으로 센다(⚠️ 한국어 해설 전달 · 영어 인용은 en-orig에만 잡힌 원 대담 ASR). 잘하는 사람과 AI에게 같은 문제를 주면 — *"and the AI will give you a lot more code just like the the mathematical proofs would be a lot longer than if a real mathematician had written the proof."*(07:11~07:20) *"and then that extra code is all technical debt that you have to"*(07:24~07:27) *AI가 만든 부채는 AI가 갚으면 된다* 는 주장에 대한 그의 답이다. 해설이 옮긴 계산: 코드가 늘면 줄마다 생기는 오류도 같이 늘고 어느 선을 넘으면 손을 못 댄다 — *"코드를 보지 않는 순수한 바이브 코딩은 그 선에 꽤 빨리 닿는다고 봅니다."*(07:39~07:42)

산업 규모의 같은 그림: 1990년 유닉스 워크스테이션과 지금의 컴퓨터는 하는 일이 같은데 코드는 비교가 안 되게 늘었다(해설이 붙인 수치 — systemd 약 171만 줄, Phoronix 2022년 말, 위키 미열람). *"블로의 표현으로 우리는 거대한 쓰레기 매립지 위에 삽니다."*(09:21~09:23) 해설의 처방은 위 *상환* 절과 같은 쪽이다: *"그리고 코드가 늘어난 만큼 멈춰서 갚는 시간을 따로 잡습니다."*(11:56~11:58) ⚠️ 줄당 오류 · *선* 은 Blow의 추정이고 수치가 없다.
