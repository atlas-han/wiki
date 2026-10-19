---
title: "Priyanka Phatak"
type: entity
category: person
tags: [anthropic, managed-agents, agent-infrastructure, harness, claude-platform]
aliases: [Priyanka, Priyanka Phatak]
links: []
sources: [tech-bridge-claude-managed-agents-workshop-1, tech-bridge-claude-managed-agents-workshop-2]
created: 2026-10-19
updated: 2026-10-19
---

# Priyanka Phatak

[[anthropic|Anthropic]]의 member of technical staff이고 [[managed-agents|Claude Managed Agents]]를 만든 엔지니어링 팀의 리드다. [[ai-engineer|AI Engineer]] 워크숍 *Claude Managed Agents*를 [[gabe-cemaj|Gabe Cemaj]]와 함께 진행했고, 1부에서는 진화 이야기와 API 개념을, 2부에서는 콘솔 Quick Start 데모를 맡았다([[tech-bridge-claude-managed-agents-workshop-1]] · [[tech-bridge-claude-managed-agents-workshop-2]]). 이 위키 첫 등장이다.

> ⚠️ **이름 표기.** 두 편 자막 모두에서 발화되는 것은 이름 *"Priyanka"*뿐이다(1부 자기소개 *"My name is Priyanka"* 00:07, 2부 11:04, 2부 en-orig 11:54는 ASR *"Bianca"*). 성 *Phatak*은 **2부(`U0ZCwwG8sac`) 설명란** *"Anthropic의 Priyanka Phatak과 Gabe Cemaj"*에서 왔다. 1부 설명란에는 없다.

## 위키에서 알려진 사실

- 자기소개(1부): *"I'm a member of technical staff at Anthropic. Uh I lead the engineering team that built Claude managed agents"*(00:07~00:17). *"I've been at Anthropic a little bit over 2 years. In the last 12 months I've been focused on uh building um agentic infrastructure"*(00:21~00:29).
- **1부 — 설계 진화.** 첫 아키텍처를 *"December of last year"*(04:34)에 early access 고객에게 냈다가 바꾼 이야기를 한다. 실패 이유는 셋이다: 장애가 구분되지 않는 디버깅, 고객 데이터 때문에 들어갈 수 없는 조사, 고객 VPC 연결. → [[brain-hands-decoupling]] · [[pets-vs-cattle]]
- **1부 — 결론.** *"harnesses encode assumptions and assumptions can go stale. So, we designed interfaces to outlast these assumptions"*(10:29~10:38). → [[agent-harness-design]]
- **1부 — TTFT.** *"about 90%"*(09:45~09:47) 줄였다고 말한다. ⚠️ 엔지니어링 글 [[anthropic-managed-agents]]의 p50 약 60% / p95 90% 이상과 표현이 다르다(백분위 미발화).
- **1부 — API.** Managed Agents API를 environment → agent → session → event 순서로 설명한다. → [[managed-agents]]
- **2부 — 콘솔 Quick Start.** 프롬프트 한 줄 → Claude가 시스템 프롬프트·이름·설명·모델을 고르고 *"V1 agents endpoint"*로 에이전트 생성 → environment(*"the template for the sandbox"*) → session(00:51~03:27). 요약: *"All you have to do is start a session with the agent, send events, get back events. Everything else is managed by us."*(03:00~03:05)
- **2부 Q&A 보충**(⚠️ 화자 추정 — Gabe를 3인칭으로 부르는 목소리): Vault 생성 흐름(ID를 세션에 포함, MCP·CLI 인증, Google Workspace CLI 예, 24:46~25:13), session forking은 *"on our road map"*(28:40~28:48), 세션당 메모리 스토어 여러 개(사용자 수준 + 조직 수준)와 *"None of this is locked in (…) Everything is an API call."*(30:49~31:14) → [[agent-memory]]

## ⚠️ 유보

- 당사자(제품 팀) 진술이다.
- 이 위키의 엔지니어링 글 [[anthropic-managed-agents]]의 저자 목록(Lance Martin, Gabe Cemaj, Michael Cohen)에는 없다.

## References

- [[tech-bridge-claude-managed-agents-workshop-1]] · [[tech-bridge-claude-managed-agents-workshop-2]]
- [[managed-agents]] · [[anthropic-managed-agents]]
- 같은 팀: [[gabe-cemaj]]
