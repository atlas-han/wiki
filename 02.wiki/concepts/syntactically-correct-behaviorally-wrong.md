---
title: 문법은 맞고 동작은 틀리다 (Syntactically Correct, Behaviorally Wrong)
type: concept
category: framing
tags: [code-translation, migration, testing, verification, legacy, trust]
aliases: [동작이 틀린 번역, 컴파일되지만 틀리다]
related: [behavior-validated-trust, legacy-code-modernization, shift-left-security, decision-quality, verifiable-goals, generator-evaluator-pattern, risk-proportional-human-review]
first-seen: tech-bridge-legacy-code-modernization-ai
sources: [tech-bridge-legacy-code-modernization-ai]
created: 2026-09-18
updated: 2026-09-18
---

# 문법은 맞고 동작은 틀리다

**AI가 한 언어의 코드를 다른 언어로 옮길 때, 결과는 컴파일되고 돌아가지만 원래 코드와 다르게 행동할 수 있다.** [[anna-gutowska|Anna Gutowska]]([[ibm|IBM]])가 [[tech-bridge-legacy-code-modernization-ai]]에서 AI 현대화의 한계로 명시했다.

> AI 모델은 **매우 복잡하게 얽힌 도메인별 논리**를 처리하는 데 어려움을 겪을 수 있습니다. 또한 **문법적으로는 올바르지만 동작상으로는 잘못된 번역**을 생성할 수도 있습니다. (07:34~07:51)

## 왜 마이그레이션에서 특히 위험한가

같은 소스가 앞서 번역을 *"기본 논리와 원래 의도는 그대로 유지"*(04:56)라고 소개했다. 그런데 레거시의 정의가 **아무도 완전히 이해하지 못하는 도메인 로직**이므로, **번역이 의도를 유지했는지 판정할 기준 자체가 없다** — 원래 의도를 아는 사람이 없고, 자동화 테스트도 없다. 문법 오류는 컴파일러가 잡지만 **동작 차이는 그것을 알아볼 테스트나 사람이 있어야 잡힌다.** 이 소스가 처방을 *워크플로*(테스트·사람 검토·검증)로 두는 이유다.

## 이 위키의 명제와의 관계 — 같은 벤더의 세 번째 진술

이 문장은 [[behavior-validated-trust]]의 명제(*작성자가 아니라 검증된 행동을 신뢰하라*)를 **마이그레이션 쪽에서 다시 말한 것**이다. [[ibm]]이 같은 원리를 세 번 말했다:

| 날짜 | 소스 | 무엇이 신뢰를 속이는가 |
|---|---|---|
| 09-08 | [[tech-bridge-ai-era-code-quality]] | **우아해 보이는 코드**(외형) |
| 09-17 | [[tech-bridge-shift-left-security-ai-code]] | **컴파일되고 테스트를 통과하는 코드**(통과 이력) |
| **09-18** | **[[tech-bridge-legacy-code-modernization-ai]]** | **문법적으로 옳은 번역**(구문 정합) |

세 번째가 더하는 것은 **비교 대상이 있다**는 점이다 — 앞의 둘은 *코드가 옳은가* 였고, 이쪽은 *원본과 같은가* 다. 검증이 **기능 검증**이 아니라 **동등성 검증**이 된다.

## 관련

- [[decision-quality]] — 09-08의 *결정의 품질* 은 새 코드를 쓸 때의 기준이고, 번역에서는 *결정을 보존했는가* 가 기준이 된다.
- [[verifiable-goals]] · [[generator-evaluator-pattern]] — 동등성을 판정할 verifier가 없는 자리. 이 소스는 그것을 *사람 검토* 로 메운다 → [[risk-proportional-human-review]].
- [[shift-left-security]] ① *"결과를 믿어라, 생성만이 아니라"* — 하루 전 같은 벤더의 보안판.

## 표시해 둔 것

> ⚠️ **사례·빈도·수치가 없다.** 어떤 종류의 동작 차이가 흔한지(경계 조건? 정밀도? 예외 처리?) 소스는 말하지 않는다. *"의도는 유지된다"*(04:56)와 이 한계의 긴장을 화자가 해소하지 않는다.

## References

- [[tech-bridge-legacy-code-modernization-ai]] · [[anna-gutowska]] · [[ibm]]
- 관련: [[behavior-validated-trust]] · [[legacy-code-modernization]] · [[shift-left-security]] · [[decision-quality]] · [[verifiable-goals]] · [[risk-proportional-human-review]]
