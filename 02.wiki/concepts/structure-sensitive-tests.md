---
title: "구조 민감 테스트 (Structure-Sensitive Tests)"
type: concept
category: pattern
tags: [testing, coding-agents, verification, test-quality, mocking, ci]
aliases: [동어반복 테스트, tautological tests, 거짓말하는 테스트, checks can lie, 실패할 수 없는 테스트, tests that cannot fail]
related: [deep-modules, test-harness-vs-test-authoring, mergeability-gap, automated-code-review, verification-bottleneck, reward-hacking, hard-vs-soft-enforcement, verifiable-goals]
first-seen: tech-bridge-pocock-pr-bottleneck
sources: [tech-bridge-pocock-pr-bottleneck]
created: 2026-10-09
updated: 2026-10-09
---

# 구조 민감 테스트

**행동이 아니라 구현의 구조에 묶인 테스트 — 그래서 초록 CI가 머지 가능을 뜻하지 않게 만드는 테스트.** [[matt-pocock|Matt Pocock]]이 [[tech-bridge-pocock-pr-bottleneck]]에서 *"checks can lie"* 라는 이름 아래 에이전트가 실제로 쓴 사례 셋을 들었다.

> *"But checks can lie. Does a green CI mean that the code is ready for merge? No, it does not."* (04:47~04:55)

## 세 가지 거짓말

| 유형 | 사례 (화자 진술) | 왜 거짓말인가 | en-orig |
|---|---|---|---|
| **동어반복 테스트** (tautological) | 상수 `X_POST_CHARACTER_LIMIT = 280` → 테스트 `expect(X_POST_CHARACTER_LIMIT).toBe(280)`. *"Opus 5 got addicted to these."* | 구현을 다시 단언할 뿐 — 상수 값을 바꿔도, **이름만 바꿔도** 깨진다. 행동은 하나도 검증하지 않는다 | 05:21~06:19 |
| **소스를 읽는 테스트** | UI에서 videos 섹션이 content plan 뒤에 오는지를, 렌더링하지 않고 **모듈 파일을 메모리로 읽어 문자열 위치로** 검사 | 소스의 모양만 바꿔도 깨지고, 실제 화면 순서는 보지 않는다 | 06:22~07:06 |
| **실패할 수 없는 테스트** | `useAudioBoost` 내부의 DOM audio context API를 가짜 메서드로 stub | audio context의 복잡한 오류 모드가 테스트에서 사라져 *"we're going to hit strange errors in production"* | 07:13~07:53 |

## 진단 — 부정행위가 아니라 구조 결합

> *"The AI isn't trying to write bad tests here. It's just taking our instructions and writing tests that are too tied into the structure instead of actually executing code."* (08:00~08:12)

이 구분이 중요하다. [[reward-hacking]]은 모델이 채점기를 **속이는** 것이고, 여기서는 **선의로 쓴 테스트가 구현에 붙어 버린** 것이다. 결과(초록 CI, 검증 안 된 행동)는 같지만 처방이 다르다 — 감시가 아니라 **설계**.

## 처방 — 거짓말하기 어렵게 설계한다

*"you can actually design your way out of these bad checks"*(08:25~08:30). → [[deep-modules]]: 큰 구현을 작은 인터페이스 뒤에 숨기면 테스트가 그 인터페이스에서만 이루어지고, *"your job here is to force the agent to use that little interface instead of reaching into the implementation"*(09:18~09:27). 그리고 이 거짓말을 잡는 것이 위의 두 겹(자동 리뷰 · 사람 리뷰)이다 — *"These are lie detectors"*(05:07~05:12).

## 위키의 다른 페이지와 맞닿는 자리

- [[test-harness-vs-test-authoring]] — Dioxus의 *"생성자를 주면 생성자를 테스트"* 와 같은 관찰. 그쪽은 *에이전트는 올바른 테스트를 고르지 못한다*, 이쪽은 *왜 못 고르는지(구조에 붙는다)와 무엇으로 막는지(설계)*.
- [[mergeability-gap]] — *테스트 통과 ≠ 머지 가능* 을 벤치마크(METR·FrontierCode)가 아니라 **테스트 자체의 질**에서 본 판.
- [[hard-vs-soft-enforcement]] — CI는 하드 강제지만, **CI가 검사하는 테스트가 거짓말하면 하드 강제도 거짓말한다.**

## ⚠️ 유보

- 사례 셋 모두 **화자 자신의 에이전트에서 나온 진술**이고 슬라이드 코드는 자막에 없다(코드는 발화에서 복원).
- *"Opus 5 got addicted to these"* 는 일화 — 빈도·비교 측정 없음.
- 구조 민감 테스트를 **자동으로 탐지**하는 방법(mutation testing 등)은 발표에 없다.
- 한 소스.

## References

- [[tech-bridge-pocock-pr-bottleneck]] · [[matt-pocock]]
- 관련: [[deep-modules]] · [[test-harness-vs-test-authoring]] · [[mergeability-gap]] · [[reward-hacking]] · [[hard-vs-soft-enforcement]] · [[automated-code-review]]
