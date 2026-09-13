---
title: 가장 짧은 경로를 가장 좋은 경로로 (Shortest Path Architecture)
type: concept
category: pattern
tags: [architecture, conventions, agents, codebase-design, guardrails]
aliases: [shortest path is the best path, 가장 멍청한 에이전트를 위한 설계]
related: [hard-vs-soft-enforcement, dune-architecture, organic-architecture, greenfield-vs-brownfield-agent-risk, llm-coding-guidelines, agent-harness-design, surgical-edits]
first-seen: tech-bridge-lauren-tan-trusting-agents
sources: [tech-bridge-lauren-tan-trusting-agents]
created: 2026-09-13
updated: 2026-09-13
---

# 가장 짧은 경로를 가장 좋은 경로로

**에이전트는 지름길을 택한다 — 그러니 지름길이 정답이 되도록 코드베이스를 설계한다.** [[lauren-tan]]이 [[dune-architecture|Dune]]의 핵심 원칙으로 제시했다.

> **이 프레임워크의 핵심 원칙 하나는 — 가장 짧은 경로가 가장 좋은 경로**라는 겁니다.

> **그게 에이전트가 코드를 쓰는 방식에 정확히 들어맞기** 때문입니다 — **에이전트는 지름길을 좋아하고 문제를 푸는 가장 빠른 길을 찾습니다. 그렇다면 그것을 문제를 푸는 가장 좋은 길로 만들면 되지 않겠습니까?**

## 설계 대상을 바꾼다

> **가장 멍청한 에이전트를 위해 설계된 겁니다. 생각할 필요가 없어야** 하죠.

이 문장은 같은 소스의 다른 관찰과 짝을 이룬다 — 대기업 인프라가 **가장 능력이 부족한 엔지니어**를 기준으로 설계됐다는 것. **그래서 그 인프라가 이미 에이전트 친화적이다.** → [[greenfield-vs-brownfield-agent-risk]]

## 구체적 형태

- **feature 단위 디렉터리** — 한 기능의 모든 코드가 한곳에. *"에이전트가 여기저기 더듬으며 어디 있는지 찾을 필요가 없습니다."* 자기 보고로 **작업의 80%가 그 안에 캡슐화**된다.
- **프레임워크의 명사** — `feature` · `entry point` · `transcript card`. 만드는 방법이 **아주 관례적**이라 베낄 대상이 명확하다.
- **가장 강한 강제가 곧 관례** — *"에이전트는 기존 패턴을 그대로 베끼는 걸 정말 좋아하니까요."* → [[hard-vs-soft-enforcement]]

## 반대 극 — 가드레일이 없을 때

같은 성향이 가드레일 없는 코드베이스에서는 **정확히 반대 결과**를 낳는다:

> 에이전트에게 과제를 주면 **가장 편리한 방법으로 풀어 버립니다.** (…) **그들이 만든 건 지름길에 최적화된 것**이고 **그 애플리케이션으로 많은 문제를 겪게** 됩니다.

→ [[organic-architecture]]

**즉 이 원칙은 에이전트의 성향을 고치려 하지 않는다.** 성향을 상수로 두고 **환경을 바꾼다.**

## 위키의 다른 페이지와 맞닿는 자리

- **[[agent-harness-design]]** · **[[context-engineering]]** — 그쪽이 *에이전트에게 무엇을 주는가* 라면 이쪽은 **에이전트가 들어갈 코드베이스의 모양**이다.
- **[[surgical-edits]]** — 변경 범위를 좁게 유지하는 처방과 같은 방향. feature 디렉터리는 그것을 **구조로 강제**한다.
- **[[sutton-bitter-lesson]]** — ⚠️ 반대 방향의 투자. *"모델이 좋아지면 해결된다"* 가 아니라 **환경에 투자하라**는 주장이다. 다만 화자도 모델 향상을 반기므로 **반례가 아니라 보완**이다.
- **[[ralph-wiggum-method]]** — 단순한 루프가 통하게 만드는 환경 설계와 같은 계열.

## References

- [[tech-bridge-lauren-tan-trusting-agents]] · [[dune-architecture]] · [[organic-architecture]] · [[hard-vs-soft-enforcement]] · [[greenfield-vs-brownfield-agent-risk]] · [[lauren-tan]]
