---
title: 게으름 프로토콜 (Laziness Protocol)
type: concept
category: pattern
tags: [refactoring, minimal-change, code-deletion, maintainability, pstack]
aliases: [최소 변경, 지워라, laziness protocol]
related: [surgical-edits, shortest-path-architecture, minimizing-reader-load, dead-code, refactoring, speculative-generality]
first-seen: tech-bridge-pstack-third-party-review
sources: [tech-bridge-pstack-third-party-review]
created: 2026-09-14
updated: 2026-09-14
---

# 게으름 프로토콜

**리팩터할 때 더하지 말고 지워라. 그리고 일을 끝내는 가장 작은 변경을 노려라.** [[pstack|Pstack]]의 첫 번째 원칙이고, [[tech-bridge-pstack-third-party-review]]의 리뷰어가 *"이건 정말 좋아합니다"* 로 꼽는다.

> **코드를 리팩터할 때 코드를 더하기보다 **가능하면 지워서** 훨씬 더 단순하게 만들자. 그리고 **일을 끝내는 가장 작은 변경**을 노리자 — 그게 결국 나중에 훨씬 더 유지보수하기 좋은 코드로 이어지니까.** (08:08~08:26)

그리고 [[lauren-tan|Lauren Tan]]의 문장이 붙는다(리뷰어 간접 인용):

> ***"목표는 더 많은 코드가 아니다. 가장 적은 코드로 최대의 임팩트."*** (08:56~09:02)

## 왜 "게으름"인가

이름이 대상을 지목한다 — **에이전트는 게으르지 않다.** 요청받은 것을 하고, 부족해 보이면 **더 만든다.** 이 프로토콜은 그 기본 성향을 **명시적으로 되돌린다.**

같은 스택의 두 번째 원칙(**제1원칙에서 다시 설계하기**)이 같은 성향의 다른 얼굴을 친다:

> **프로젝트가 자라고 기능을 더하면 에이전트는 다음 기능을 **볼트로 덧대기**로 결정할 수 있습니다.** (08:26~08:34)

→ **덧대기(bolt-on)가 에이전트의 기본값이고, 두 원칙 모두 그것을 막는다.**

## 이 위키의 같은 계열

| 개념 | 강조 |
|---|---|
| [[surgical-edits]] | **건드리는 범위**를 최소화 |
| [[shortest-path-architecture]] | *"가장 짧은 경로가 가장 좋은 경로"* — **구조** |
| **게으름 프로토콜** | **변경의 방향** — 더하기보다 **빼기** |
| [[minimizing-reader-load]] | **읽는 사람의 부담** |

네 개가 같은 곳을 가리키되 **단위가 다르다**(범위 / 경로 / 부호 / 독자). 이 개념의 고유한 기여는 **부호** — *가능하면 지워라* 는 다른 셋에 없다.

[[refactoring]] 카탈로그의 [[dead-code]]·[[speculative-generality]] code smell과 정면으로 맞물린다. **차이는 대상**이다 — 리팩터링 카탈로그는 *이미 쌓인 것* 을 지우라 하고, 이 프로토콜은 **에이전트가 쌓기 전에** 건다.

## 열려 있는 것

- ⚠️ **"가능하면"의 판정 기준이 없다.** 무엇을 지워도 되는지 — 테스트 커버리지? 사용처 분석? — 소스에 없다.
- ⚠️ **최소 변경과 [[architecture-as-remaining-art|제1원칙 재설계]]는 충돌할 수 있다.** 첫 원칙은 *가장 작은 변경* 을, 둘째 원칙은 *첫날부터였다면 어떻게 설계했겠는가* 를 요구한다. **소스는 둘의 우선순위를 정하지 않는다.**
- ⚠️ **효과 측정이 없다.** 원칙 목록이 화면에 떠 있고 리뷰어가 읽어 줄 뿐이다.

## References

- [[tech-bridge-pstack-third-party-review]] · [[pstack]] · [[lauren-tan]]
- 관련: [[surgical-edits]] · [[shortest-path-architecture]] · [[minimizing-reader-load]] · [[build-a-lever]] · [[dead-code]] · [[speculative-generality]] · [[refactoring]]
