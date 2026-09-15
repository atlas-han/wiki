---
title: 하드 강제와 소프트 강제 (Hard vs Soft Enforcement)
type: concept
category: pattern
tags: [ci, lint, guardrails, code-review, enforcement, standards]
aliases: [강제의 층, CI를 빨갛게, 소프트 강제에 의존하지 말라]
related: [executable-standards, verifiable-goals, llm-coding-guidelines, agent-governance-layers, shortest-path-architecture, verification-bottleneck, behavior-validated-trust]
first-seen: tech-bridge-lauren-tan-trusting-agents
sources: [tech-bridge-lauren-tan-trusting-agents, tech-bridge-graft-code-knowledge-graph]
created: 2026-09-13
updated: 2026-09-15
---

# 하드 강제와 소프트 강제

**제약을 층으로 쌓되, 에이전트가 잊을 수 있는 층에 강제를 의존하지 않는다**는 원칙. [[lauren-tan]]이 [[tech-bridge-lauren-tan-trusting-agents]]에서 제시했다.

## 층

| 층 | 성격 | 근거 |
|---|---|---|
| **1. 코드베이스** — 아키텍처·컨벤션·차단된 import | **하드** | *"가장 강한 수준의 강제. **에이전트는 기존 패턴을 그대로 베끼는 걸 정말 좋아하니까요**"* |
| **2. 정적 분석** — CI 검사·린트·컴파일러 진단 | **하드** | **CI를 빨갛게 만든다** |
| **3·4·5. 규칙 · 스킬 · bugbot** | **소프트** | *"에이전트는 여전히 잊을 수 있고 항상 일관되게 적용하지 않을 수 있습니다"* |

> 층 번호는 **화면의 다이어그램을 읽는 말**이라 항목명 전체는 확정할 수 없다.

## 핵심 경고

> **층으로 쌓기는 하되 그것들에만 강제를 의존하지는 않습니다. 아주아주 소프트하니까요.** **규칙과 bugbot과 스킬과 스타일 가이드만 있으면, 코드베이스가 완전히 쓰레기처럼 보이는 건 시간문제**입니다.

이것은 이 위키가 [[agent-skills]]·[[llm-coding-guidelines]]·[[intent-md]]에 모아 온 **마크다운 기반 지시**들에 대한 **한계 선언**이다. 그것들은 유용하지만 **강제가 아니다.**

## 기술 스택이 강제 수단이 된다

> **어떤 기술 스택을 쓰느냐도 아주 중요합니다.** 예를 들어 **Rust가 다시 엄청 인기를 얻고 있는 건 컴파일러가 아주 엄격하기** 때문이죠. **borrow checker를 달래야** 하고, **에이전트가 unsafe 블록을 쓰지 않게만 하면 코드가 컴파일되면 대체로 동작하고 괜찮다**고 어느 정도 확신할 수 있습니다.

**언어 선택을 검증 전략으로 다시 읽는 것** — 컴파일러가 [[verification-bottleneck|검증 병목]]의 일부를 공짜로 가져간다.

## 운용 규칙 — PR 댓글은 코드 스멜이다

이 소스에서 가장 이전 가능한 한 문장이다.

> **최악의 자리는 코드 리뷰 랜드에 갇혀서, 코드베이스의 모든 불변식을 문자 그대로 사람이 코드를 읽으며 "이건 하면 안 됩니다"라고 말해서 강제하는 것**입니다.

> **그걸 해야 할 때마다 코드 스멜, 안티패턴으로 여기고** 이렇게 말해야 합니다 — ***"PR에 댓글을 다는 대신, 이걸 어떻게 하드 규칙으로 바꾸지? 린트 규칙으로? CI 실패로? 아니면 이 문제를 아예 범주적으로 없애 버릴 수는 없나?"***

## 위키의 다른 페이지와 맞닿는 자리

- **[[executable-standards]]** — *"표준은 문서로 존재할 수 없다"* 를 **개인 실천의 규칙**으로 내린 것. 그 페이지가 *무엇을 심는가* 를 다뤘다면 이쪽은 **어디에 심으면 안 되는가**(소프트 층)를 더한다.
- **[[verifiable-goals]]** — 성공 기준을 CI 실패로 바꾸는 것이 곧 검증 가능화다.
- **[[agent-governance-layers]]** — 거버넌스의 층 구분과 같은 모양인데, 이쪽은 **강제력의 세기**로 층을 나눈다.
- **[[behavior-validated-trust]]** — 하드 층이 늘수록 사람이 확인할 것이 줄어든다. *"인간 엔지니어가 더 이상 직접 확인하러 갈 필요가 없다는 신뢰와 확신."*
- **[[deny-and-continue]]** · **[[no-silent-write]]** — 런타임 쪽의 하드 강제. 같은 원리가 실행 시점에 적용된 형태다.

## 표시해 둔 것

> ⚠️ **소프트 층을 버리라는 말은 아니다** — *"층으로 쌓기는 한다."* 다만 **유일한 강제 수단으로 쓰지 말라**는 것이다.
>
> ⚠️ 이 소스의 하드 강제 사례(주석 금지·`useEffect` 금지)는 **대가가 논의되지 않는다.** → [[dune-architecture]]

## References

- [[tech-bridge-lauren-tan-trusting-agents]] · [[executable-standards]] · [[verifiable-goals]] · [[dune-architecture]] · [[shortest-path-architecture]] · [[verification-bottleneck]] · [[lauren-tan]]
