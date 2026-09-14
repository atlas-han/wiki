---
title: 지렛대를 만들어라 (Build a Lever)
type: concept
category: pattern
tags: [tooling, cli, automation, skills, verification, pstack]
aliases: [lever, 도구를 만들어라]
related: [skill-self-improvement, agent-verification-skill, agent-tool-design-practices, executable-standards, harness-engineering]
first-seen: tech-bridge-pstack-third-party-review
sources: [tech-bridge-pstack-third-party-review]
created: 2026-09-14
updated: 2026-09-14
---

# 지렛대를 만들어라

**에이전트로 같은 일을 손으로 여러 번 하게 될 것 같으면, 그 일을 위한 도구를 먼저 만들어라.** [[pstack|Pstack]]의 다섯 번째 원칙.

> **에이전트로 뭔가를 손으로 여러 번 하게 될 것 같으면, 그걸 위한 도구를 만들지 그래요? **CLI**일 수도 있고, **같은 검증을 계속 반복하는 스크립트**일 수도 있습니다** — 검증 스킬에서 본 게 그거죠. — [[tech-bridge-pstack-third-party-review]] (09:41~09:55)

## 이 위키의 같은 계열과의 차이

| 개념 | 무엇이 자라는가 | 계기 |
|---|---|---|
| [[skill-self-improvement]] | **스킬** | **에이전트의 실패 모드를 관찰**했을 때 — *"볼 때마다 이건 스킬로 만들자"* |
| [[harness-engineering]] | **규칙** | *"모든 실수가 규칙이 된다"* |
| **지렛대** | **실행 가능한 도구(CLI·스크립트)** | **반복이 예상**될 때 |

**계기가 다르다.** 앞의 둘은 **사후**(실패를 보고 나서)이고, 지렛대는 **사전**(반복을 예상하고)이다. 그리고 산출물이 **문서나 프롬프트가 아니라 실행 가능한 코드**다 — [[executable-standards]]와 같은 방향이다.

이 차이가 실무에서 갖는 뜻은 [[tech-bridge-knowledge-work-agent-infrastructure|Composio 편]](09-08)이 짚은 것과 맞물린다: **프롬프트는 compaction으로 날아간다.** CLI는 날아가지 않는다.

## Pstack 안에서의 자기 참조

이 원칙은 **Pstack 자신의 존재 이유이기도 하다.** `create verification` / `maintain verification` 스킬이 하는 일이 정확히 *"같은 검증을 반복하는 스크립트를 만들고 유지하는 것"* 이다 → [[agent-verification-skill]].

즉 **스택이 자기 원칙의 사례다.** 09-13 [[pstack]] 페이지에 기록된 제작 경위(*"스킬 몇 개로 시작했다"*)와 이 원칙을 함께 읽으면, **Pstack = 반복을 관찰하고 만든 지렛대들의 누적**으로 읽힌다.

## 열려 있는 것

- ⚠️ **"여러 번"의 문턱이 없다.** 두 번? 다섯 번? 기준이 소스에 없다.
- ⚠️ **도구 자체의 유지 비용**이 다뤄지지 않는다 — 다만 같은 스택의 `maintain verification` 스킬이 **그 문제를 인정하고 있다**(*"앱이 자라며 검증기가 개발과 어긋나는 일이 잦다"*).
- ⚠️ **모델이 흡수할 층인가**라는 물음이 같은 소스에서 제기되지만 답은 검증에 한정된다 — *"[[fable-5-1|Fable]]이나 [[openai-astra|Astra]] 같은 모델이라면 이런 걸 자연스럽게 내장하기 시작하길 바라겠지만, 검증 단계에 관해서는 사후에 적용해도 나쁠 게 없다"*. → [[harness-pruning]]

## References

- [[tech-bridge-pstack-third-party-review]] · [[pstack]] · [[lauren-tan]] · [[molten-base]]
- 관련: [[skill-self-improvement]] · [[agent-verification-skill]] · [[executable-standards]] · [[harness-engineering]] · [[harness-pruning]] · [[agent-tool-design-practices]] · [[laziness-protocol]]
