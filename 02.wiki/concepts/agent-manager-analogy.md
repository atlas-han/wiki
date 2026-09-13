---
title: 매니저·헤드셰프 유비 (Agent Manager Analogy)
type: concept
category: framing
tags: [management, delegation, trust, role, engineering-manager]
aliases: [관리 유비, 헤드 셰프, 뒷좌석 운전자]
related: [agent-trust-curve, persistent-agent-teams, agent-org-adoption, named-human-accountability, goal-level-delegation, taste-vs-judgment]
first-seen: tech-bridge-grokbot-agent-teams
sources: [tech-bridge-grokbot-agent-teams, tech-bridge-lauren-tan-trusting-agents]
created: 2026-09-13
updated: 2026-09-13
---

# 매니저·헤드셰프 유비

**에이전트를 다루는 일이 코드를 쓰는 일보다 사람을 관리하는 일에 가깝다**는 프레이밍. [[lauren-tan]]이 두 소스에 걸쳐 세 가지 비유로 반복한다.

## 세 비유

### 1. 매니저 — 신뢰가 없으면 마이크로매니지먼트

> 제가 어떤 팀의 엔지니어링 매니저이고 팀원들을 신뢰하지 못한다면, 제 운영 모드는 **마이크로매니지먼트**가 됩니다. **부하들 어깨너머를 들여다보며 일을 잘하는지 확인하는 데 시간을 많이 써야** 하죠.

화자의 이력(Netflix 테크리드 → EM → IC)이 이 비유의 출처다 — *"관리 스킬과 에이전트를 다루는 법 사이에 유사점이 정말 많다."*

### 2. 신입 — 코딩은 잘하는데 맥락이 없는 사람

> **코딩은 정말 잘하지만 비즈니스 맥락이 전혀 없는, 5초 전에 온보딩한 엔지니어**가 있다고 상상해 보세요. **그 사람을 어떻게 효과적으로 만들겠습니까?**

답이 스킬이다 — 마크다운으로 **맥락과 지시를 인코딩**하는 것. → [[agent-skills]] · [[feature-map]]

### 3. 헤드 셰프 — 환경을 설계하는 일

> **여러분은 헤드 셰프**고 **더 이상 음식을 직접 다 만들지 않습니다.** 라인 쿡이 있고 수 셰프가 있고 여러 스테이션이 있죠. 여러분의 일은 **환경을 설계하는 것** — **주방을 차리고 여러 사람에게 과제를 주는 것**입니다.

이 비유는 [[tech-bridge-grokbot-agent-teams]]에서 먼저 나왔고(미슐랭 주방·품질 관리), 이 소스가 **"환경 설계"** 로 초점을 옮긴다 → [[shortest-path-architecture]] · [[dune-architecture]].

## 유비가 처방으로 바뀌는 지점 — 뒷좌석 운전자

스킬을 만들고 유지하는 데 필요한 태도를 **페어 프로그래밍**에 빗댄다:

> **뒷좌석 운전자 노릇을 아주 잘해야** 해요. (…) **에이전트의 수동적 관찰자가 되고 싶지 않을 겁니다** — 자기 스킬 세트를 만드는 초기 단계에는 **운전석에 아주 깊이 있어야** 합니다. **모든 도구 호출을 열어 보고, 코드를 읽고, 에이전트의 행동과 사고 블록을 읽는 것이 그들이 어디서 실패하는지 보는 아주 좋은 방법**입니다.

→ [[agent-action-record]] · [[skill-self-improvement]]

## 유비의 한계 (위키의 관찰)

> ⚠️ 관리 유비는 **책임의 소재**를 다루지 않는다. 매니저는 부하의 실수에 책임을 지지만, 이 소스에서 **자동 병합된 PR의 회귀에 대한 책임 구조는 서술되지 않는다.** → [[named-human-accountability]]
>
> ⚠️ 그리고 [[persistent-agent-teams]]가 기록한 *정체성을 가진 팀원* 의 그림과 달리, 이 소스의 유비는 **일방향**이다 — 에이전트가 매니저에게 되묻거나 거절하는 경로가 없다.

## References

- [[tech-bridge-lauren-tan-trusting-agents]] · [[tech-bridge-grokbot-agent-teams]] · [[lauren-tan]] · [[agent-trust-curve]] · [[persistent-agent-teams]] · [[agent-skills]]
