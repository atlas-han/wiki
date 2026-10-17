---
title: MCP를 스킬의 배포 계층으로 (MCP as Skill Distribution Layer)
type: concept
category: pattern
tags: [mcp, agent-skills, distribution, governance, skills-over-mcp, enterprise-adoption, non-technical-users]
aliases: [skills over MCP, MCP 스킬 배포, 원격 스킬 서버]
related: [model-context-protocol, agent-skills, run-trace-skill-distillation, agent-org-adoption, prompt-injection, agent-governance-layers, deferred-tool-context]
first-seen: tech-bridge-runlayer-self-improving-skills-mcp
sources: [tech-bridge-runlayer-self-improving-skills-mcp]
created: 2026-10-16
updated: 2026-10-16
---

# MCP를 스킬의 배포 계층으로

**스킬을 각자 로컬에 설치하는 대신 원격 MCP 서버에 두고, 모든 클라이언트가 MCP로 스킬을 검색·수신하게 하는 패턴.** 이렇게 하면 서버가 회사 지식의 source of truth이자 정책을 적용하는 지점이 된다. [[tech-bridge-runlayer-self-improving-skills-mcp]]의 [[rafal-wilinski|Rafal Wilinski]]([[runlayer|Runlayer]]) 발표에서 나왔다.

> *"Skills can be delivering um the knowledge how to do something and tools gives us capabilities. (…) But MCP can be also used as a protocol to deliver the knowledge to deliver the skills. We can use MCP as the distribution layer."* (07:33~07:51)

## 무엇을 푸는가 — 로컬 스킬의 문제 두 가지

| 문제 | en-orig |
|---|---|
| dev-centric | *"they are local first and defcentric[=dev-centric]"*(05:10~05:14) — markdown·JSON·CLI·git. 비개발자는 스킬을 만들지도 나누지도 못한다 |
| 클라이언트 파편화 | *"not every LLM client support skills"*(06:44~06:50) — 마케팅·HR·법무·재무는 *"chat GPT or some other weird LM client"*(07:05~07:09)를 쓴다 |

→ *"MCP as a distribution layer fixes that because it's unified in and works in almost every single client not just developer clients."*(09:03~09:13)

## 구조

- *"you can create a remote MCP server which can become the source of truth across your whole company. Clients can connect to that. They can they can search for the right skills. uh server can enforce the policy and make sure that everyone gets the best version of the skill possible depending on a query and for instance the role that they have assigned."*(07:54~08:14)
- 거버넌스: *"one place to govern and manage what's the knowledge that's getting shared and distributed across your company"*(09:24~09:29)
- 표준화: *"a working group called skills over MCP and while the exact API is not final direction is clear"*(08:28~08:36). *"the official spec is leaning towards MCP resources the support for resources is also mixed. So we are going with tools."*(08:43~08:51)
- 설치 경로의 위험(`npx skills` → *"free prompt injections (…) root permissions and someone else's API key"* 06:04~06:13)을 중앙 서버의 검사로 대체한다 → [[prompt-injection]]

## 이 위키에서의 좌표

- [[tech-bridge-agent-knowledge-four-ways]]: 스킬은 *무엇을 할지*, MCP는 *할 수 있게* 한다. 이 패턴은 여기서 한 걸음 더 나가 **지식 자체도 MCP로 운반한다.**
- [[tech-bridge-ai-native-skills]](QuantumBlack): enablement 층의 *MCP gateway* 와 *skills registry* 를 따로 그린다. 이 패턴은 **둘을 하나로 합친다.**
- [[tech-bridge-tessl-harness-engineering-factory|Tessl]]: 스킬 레지스트리에 사람의 보안·품질 리뷰를 둔다. Runlayer는 자동 검사를 둔다.
- [[deferred-tool-context]] / progressive disclosure: 스킬의 요약만 먼저 보이는 구조(02:17~02:39)를 원격 검색으로 확장한 형태다.

> ⚠️ **Contradiction: MCP는 스킬로 대체되는가.** [[tech-bridge-sdd-full-course|SDD 강좌]]는 "MCP → CLI + 스킬"을 추세로 가르치고, [[tech-bridge-composio-dashboard-is-dead|Composio]]는 스킬을 *"band-aid"* 라고 부른다. Wilinski는 MCP 사망론(*"thank god MCP is finally dead because I'm not interested in dealing with oath"* 07:19~07:23)을 *"everyone missed the point"* 로 기각한다.

## ⚠️ 유보

- 벤더(MCP gateway 보유) 주장이고, 6개월 내부 운영(08:14~08:18)에 대한 측정이 없다.
- skills over MCP 워킹 그룹의 소속·상태는 확인하지 않았다.
- 중앙 서버가 전사에 배포하므로 **잘못된 스킬도 전사로 퍼진다** → [[run-trace-skill-distillation]]의 게이트 문제.

## References

- [[tech-bridge-runlayer-self-improving-skills-mcp]] — first-seen
- [[model-context-protocol]] · [[agent-skills]] · [[prompt-injection]] · [[run-trace-skill-distillation]]
