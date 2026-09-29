---
title: Agent 365 (Microsoft)
type: entity
category: product
tags: [microsoft, agent-governance, observability, audit, finops, enterprise-ai]
aliases: [Agent 365, 에이전트 365]
links: []
sources: [tech-bridge-nadella-copilot-autopilot]
created: 2026-09-29
updated: 2026-09-29
---

# Agent 365

[[microsoft|Microsoft]]의 **엔터프라이즈 에이전트 관찰·거버넌스 제품**. [[satya-nadella|Satya Nadella]]가 [[tech-bridge-nadella-copilot-autopilot]]에서 [[microsoft-copilot|Copilot]]의 어떤 폼팩터보다 먼저 꺼낸 이름이다.

> **Agent 365 is probably the most important, you know, it's the product that is getting the fastest adoption in the enterprise. That ability to observe everything, govern everything, set policy, have security, have the finops.** (04:41~04:50)

> ⚠️ **당사자 진술, 수치 없음.** *"fastest adoption"* 이 무엇 대비인지, 몇 개 기업인지 없다. 기능 목록은 위 한 문장이 전부다.

## 소스가 말하는 역할

| 역할 | 소스 |
|---|---|
| **관찰·거버넌스·정책·보안·FinOps** | 04:46~04:50 |
| **Autopilot의 호스팅 환경** — *"the work that's gone in to create this hosting environment … with agent 365 that really has the auditability of the activity of an autopilot. That's what is going to be the key in the enterprise."* | 12:49~13:02 |
| **격리(containment)** — *"building out that containment is a solid engineering problem"*, Autopilot이 도는 환경이 *"heavy lifting so that the enterprises can trust it, can audit it, can have observability, can have governance policy"* | 15:27~15:43 (이름은 여기서 다시 말하지 않는다) |

화자의 논리 순서: **신뢰가 최대 이슈**(04:10~04:12) → 자격 증명을 맡길 수 있나, 통제하고 감사할 수 있나(04:20~04:31) → *"in the enterprise, this is everything"* → 그래서 Agent 365. 즉 이 제품은 **자율 에이전트(Autopilot) 판매의 전제 조건**으로 위치한다.

## 이 위키에서의 좌표

- [[agent-governance-layers]] — *"경계는 프롬프트가 아니라 에이전트 바깥에"* 의 **벤더 제품판**. 이 위키가 모아 온 벽의 자리(도구 정의·자격 증명 주입·실행 게이트)와 달리 Agent 365는 **관찰·감사·정책·비용** 쪽으로 서술된다 — 행동을 **막는** 층인지 **보는** 층인지 소스가 구분하지 않는다.
- [[agent-action-record]] — *"auditability of the activity"* 는 행동 기록의 요구와 같다.
- [[ai-arms-limitation-lens]] — 같은 대담에서 **격리 실패 시 국가 간 통보**를 말한다. 기업 층의 격리(Agent 365)와 국가 층의 통보가 **같은 insider risk 논리**로 이어진다(13:53~14:17).

## ⚠️ 유보

- **막는가, 보는가** — *"observe · govern · set policy · security"* 가 실행 전 차단을 포함하는지 불명.
- **Microsoft 밖의 에이전트** — 다른 벤더 에이전트까지 관찰하는지 없음.
- 가격·출시일·아키텍처 없음.

## References

- [[tech-bridge-nadella-copilot-autopilot]] — 첫 소스
- [[microsoft]] · [[microsoft-copilot]] · [[satya-nadella]] · [[agent-governance-layers]]
