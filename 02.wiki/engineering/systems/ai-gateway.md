---
title: "AI Gateway — 에이전트와 LLM·MCP·API 사이의 단일 통제·관측 지점"
type: engineering
category: system
tags: [ai-gateway, llm-gateway, mcp-gateway, identity-based-auth, budgets, observability, vendor-lock-in, credentials, proxy]
aliases: [AI gateway, LLM gateway, MCP gateway, AI 게이트웨이, LLM 게이트웨이]
related: [agent-identity-separation, credential-injection-outside-sandbox, least-privilege-connectors, automatic-model-routing, model-context-protocol, value-maxing, overspending-underusing-loop, design-pattern-proxy, agent-governance-layers, trace-to-memory-loop, reserve-then-settle]
first-seen: tech-bridge-tailscale-aperture-ai-without-lock-in
sources: [tech-bridge-tailscale-aperture-ai-without-lock-in]
created: 2026-10-17
updated: 2026-10-17
---

# AI Gateway

**에이전트와 그 인터페이스를 한쪽에, LLM·MCP·API 엔드포인트를 다른 쪽에 두고 그 사이에서 모든 호출을 통제·관측하는 단일 지점이다.** 인증·자격증명·모델 접근·예산·로그가 여기 모인다. 그래서 어느 층(모델·데이터·인터페이스·샌드박스)을 바꿔도 나머지가 그대로 남는다. [[remy-guercio|Remy Guercio]]([[tailscale|Tailscale]] Aperture)가 [[tech-bridge-tailscale-aperture-ai-without-lock-in]]에서 제시했다.

> *"it sits in between your agents and that interface of that agent uh and you know, all of your endpoints uh as well both like LLM endpoints as and data, you know, kind of MCP endpoints, API endpoints (…) and sits in the middle and let you both control and monitor what's happening."* (08:05~08:21)

"LLM gateway"가 아니라 "AI gateway"라고 부르는 이유는 LLM과 MCP·일반 API를 함께 다루기 때문이다(12:25~12:47).

## 왜 — 네 층의 선택권

화자는 내부 AI 배포를 네 층으로 나눈다(05:57~06:46).

| 층 | 화자의 서술 |
|---|---|
| LLM | *"There's the LLM or LLMs, right? There's that layer."* |
| 데이터 커넥터 | *"this is MCP for a lot of people, but in reality it's, you know, CLI or APIs or really just any way that you get data"*(06:03~06:10) |
| 인터페이스 | *"I think people kind of forget about this sometimes"*(06:15~06:16). chat · TUI · IDE · 휴대폰 · Slack. *"it is a component that you can break out."*(06:40~06:42) |
| 샌드박스 | *"just the environment in which the agent runs"*(06:44~06:46) |

> *"it's really important to be able to make a choice at any given layer that you need at any given time."* (07:09~07:13)

게이트웨이는 이 선택권을 한곳에 모으는 자리다. 청구서 공황 끝에 벤더 하나로 통합하는 대응(*"that is not not a great idea"* 04:21~04:23)의 대안으로 제시된다 → [[overspending-underusing-loop]] · [[value-maxing]]

## 기능 묶음 (한 벤더의 구현 기준)

1. **연결 신원 기반 인증.** 네트워크가 연결마다 기기·사용자 신원을 붙이고, 게이트웨이가 그 신원으로 판단한다 → [[agent-identity-separation]]. 사람·에이전트에게 API 키를 나눠 주지 않는다(*"there's no extra screen for create these API keys"* 11:38~11:41).
2. **신원별 모델·예산 정책.** *"You get unlimited budget with a cheap model, and you get an extremely narrow budget with a frontier model"*(11:56~12:01). 라우터가 고르는 것이 아니라 관리자가 정한다 → [[automatic-model-routing]]
3. **MCP gateway + auth 주입.** 일반 API에 auth를 주입하고 MCP로 재노출한다(12:33~12:43). 팀 신원별로 커넥터 권한을 나눈다(13:31~13:47) → [[credential-injection-outside-sandbox]] · [[least-privilege-connectors]] · [[model-context-protocol]]
4. **전환 비용 낮추기.** 새 도구는 엔드포인트만 치면 된다(*"all they have to do is hit that endpoint"* 14:09~14:12). *"It's all those little points of friction uh that lead to (…) people just don't try new use cases."*(14:31~14:38)
5. **로그 → 에이전트의 사후 진단.** 에이전트는 *"They're usually not great at stopping themselves, uh but they are great at analyzing where they went wrong after the fact."*(08:54~08:59) 게이트웨이 로그를 에이전트에게 되돌려 *"what happened?"*(09:03)라고 묻는다 → [[trace-to-memory-loop]]

## 실패 모드로 꼽힌 것 — 키를 키로 바꾸기

기존 게이트웨이에 대한 불만: *"I put all my keys on this gateway. Now I need to go create synthetic keys for everything that I have. (…) I've traded some keys for a bunch of other keys."*(09:19~09:28) 게이트웨이가 자격증명 문제를 옮기기만 한다면 효익이 줄어든다는 진단이다. 화자의 답은 네트워크 신원이다.

## 위키의 다른 페이지와

- [[design-pattern-proxy]]: 구조적으로는 원격 서비스 앞의 프록시다. 이 페이지는 그 패턴을 **AI 호출의 통제·관측** 용도로 쓴 시스템이다.
- [[reserve-then-settle]]: 둘 다 비용을 hot path에서 다룬다. reserve-then-settle은 **파는 쪽**이 잔액을 먼저 예약하는 구조이고, AI gateway는 **쓰는 쪽**이 신원별 예산과 모델 접근을 거는 자리다.
- [[agent-governance-layers]]: "보는 층"의 한 구현이다.
- MCP gateway는 [[tech-bridge-runlayer-self-improving-skills-mcp|Runlayer]]도 말한다(*"our MCB[=MCP] gateway"*). 기능이 발화된 것은 이 소스가 처음이다.

## ⚠️ 유보

- **단일 벤더 소스다.** 화자가 고지한다: *"I don't just mean necessarily using our AI gateway. I think it's nice, but you know, just any AI gateway"*(07:50~07:56). 측정·고객 수치는 없다.
- 층을 분리했을 때 잃는 것(수직 통합 하네스의 품질·속도)은 다루지 않는다. 게이트웨이 자체가 새 단일 실패 지점·지연 지점이 되는 문제도 다루지 않는다.
- pass-through auth와 샌드박스 orchestration은 예정 기능이다(16:08~16:12, 17:05~17:11).
- ROI를 게이트웨이 로그로 *어떻게* 증명하는지는 발화되지 않는다.

## References

- [[tech-bridge-tailscale-aperture-ai-without-lock-in]] · [[tailscale]] · [[remy-guercio]]
