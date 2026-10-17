---
title: "기성 하네스 임베드 (Embedded Agent Harness) — 하네스를 짓지 말고 빌려 쓰되, 제작사의 투자를 깎지 마라"
type: concept
category: pattern
tags: [agent-harness, embedded-harness, build-vs-buy, developer-instructions, system-prompt, deferred-tools, version-pinning, protocol, codex]
aliases: [building on an agent harness, pick a harness off the shelf, 하네스 임베드, 기성 하네스 위에 짓기]
related: [codex-app-server, harness-as-platform, tools-and-context-over-harness, deferred-tool-context, agent-client-protocol, harness-engineering, agent-harness-design, self-harness, bring-your-own-subscription]
first-seen: tech-bridge-codex-app-server
sources: [tech-bridge-codex-app-server, tech-bridge-vercel-rauch-agentic-workflow, tech-bridge-cooking-with-codex]
created: 2026-10-16
updated: 2026-10-16
---

# 기성 하네스 임베드

**에이전트가 들어가는 제품을 만들 때 하네스(루프·도구 호출·컨텍스트 관리·샌드박스·프롬프트)를 직접 짓지 않는다. 이미 검증된 하네스를 프로토콜로 붙여 그 위에 자기 인터페이스만 짓는다.** 그리고 그 하네스 제작사가 쌓은 투자(모델별 프롬프트 튜닝, 컨텍스트 예산)를 깎아 먹지 않도록 **덧붙이기만** 한다. 하네스 *제작사*의 처방은 [[dominik-kundel|Dominik Kundel]]([[openai|OpenAI]], [[codex-app-server|Codex App Server]]) — [[tech-bridge-codex-app-server]]. 하네스 *구매자*의 회고는 Guillermo Rauch(Vercel) — [[tech-bridge-vercel-rauch-agentic-workflow]].

> *"How many of you um feel like it's way too intimidating to build an agent harness?"* (Kundel 00:08~00:12) · *"I would want to pick a harness off the shelf"* (Rauch 04:35~04:37, 그 편 기준)

## 왜 — 하네스 비용

- 구매자 쪽: Rauch는 [[v0]]를 처음 만들 때 *"like 90% of the engineering time"* 이 하네스(AI SDK·모델·프롬프트·툴 호출)에 들어갔다고 회고한다. fx 위의 fx0 데모는 *"probably like I don't know, 100 lines of code"* 라고 한다(⚠️ 둘 다 회고·추정, Vercel 편).
- 제작사 쪽: Kundel은 Codex를 시켜 Visual Basic 클라이언트를 *"largely in one shot"*(11:11~11:13) 만들었다며 *"without you having to learn all the nitty-gritty parts of bu building an agent"*(11:17~11:21)라고 말한다. ⚠️ 측정 없음.

## 붙이는 방법 — 프로토콜

[[codex-app-server|App Server]] = 하네스를 감싼 JSON-RPC 스타일 프로토콜. 1st party 앱이 쓰는 기능을 거의 모두 노출한다(*"over 120"* 클라이언트 메시지). 비교 대상은 [[agent-client-protocol|ACP]] — ACP는 **여러 하네스에 걸친 일반 프로토콜**이고 App Server는 **한 하네스의 깊은 제어**다(06:04~06:13). 같은 하네스를 붙이니 채팅 UI가 아니어도 된다 — 백그라운드, 이상한 하드웨어, Doom 안(11:28~14:28).

## 규칙 셋 (Kundel, 15:44~17:25)

| # | 규칙 | 지키는 것 |
|---|---|---|
| ① | **하네스 버전을 직접 번들하라** — 사용자가 설치한 CLI에 기대지 마라 | 프로토콜이 *"regularly changes between versions"*(09:38~09:42) → breaking change·실험 기능·사용자 업데이트 여부에서 격리. Codex app 자신도 그렇게 한다 |
| ② | **새 함수는 노출하되 deferred로** | 컨텍스트 창 — system prompt에 넣지 않고 tool search로 찾게 한다 → [[deferred-tool-context]] |
| ③ | **base instructions 교체 대신 developer instructions 덧붙이기** | *"make sure that the actual prompt is in distribution and make sure that the agent performs well. And you're losing out on all of that if you're actually jumping in and like writing your own system prompt."*(17:11~17:21) |

위키의 독해: 셋 모두 **"제작사가 그 모델에 맞춰 쌓은 것을 깎지 마라"** 는 한 원칙의 변형이다. ①은 하네스 *코드*, ②는 *컨텍스트 예산*, ③은 *프롬프트 튜닝*을 지킨다.

## 이 위키에서의 좌표

- [[harness-as-platform]] — Uber에선 **사내 플랫폼 팀**이 하네스를 제공하고 도메인 팀이 스킬을 꽂는다. 이 패턴은 같은 분업을 **회사 경계 밖**으로 옮긴다: 제작사가 하네스를, 제품 팀이 인터페이스·도구·developer instructions를 낸다.
- [[tools-and-context-over-harness]] — "하네스는 고정, 노력은 도구·컨텍스트에"를 **사용자 쪽**에서 말한 페이지다. 규칙 ②·③은 같은 결론을 **제작사가 직접** 준다.
- [[bring-your-own-subscription]] — 임베드한 하네스가 사용자의 ChatGPT 구독으로 돈다(Kundel 06:18~06:31, T3 Code 사례). 이 패턴의 경제적 동력이다.
- [[mcp-skill-distribution]](10-13 Runlayer 제안) — 도구·지식을 **MCP로** 운반하는 쪽. App Server는 MCP도 되지만 *"you can also just straight up define tools"*(07:45~07:47)라고 말한다.

## ⚠️ 유보

- **긴장: 하네스를 직접 고치는 쪽.** [[self-harness]]·[[harness-engineering]] 계열은 과제에 맞춘 하네스 수정을 성과의 원천으로 본다. 규칙 ③은 *그 모델을 학습시킨 회사의 하네스* 라는 전제에서만 강하다. 어느 정도의 system prompt 변경이 "분포 밖"인지, 성능이 얼마나 떨어지는지의 근거는 없다(당사자 진술).
- **잠금(lock-in).** 깊은 제어(120개 메시지)는 곧 한 하네스·한 회사에 대한 의존이다. ACP 같은 일반 프로토콜과의 교환비를 소스가 따지지 않는다.
- **번들의 대가.** 규칙 ①은 보안 패치·모델 업데이트를 따라가는 책임을 제품 팀에 넘긴다. 이 비용은 발화되지 않았다.
- 두 소스 모두 **하네스를 파는 쪽**이다(OpenAI는 Codex, Vercel은 fx·Sandbox).

## References

- [[tech-bridge-codex-app-server]] — first-seen (제작사의 규칙 셋)
- [[tech-bridge-vercel-rauch-agentic-workflow]] — 구매자의 회고(v0 "90%", "off the shelf")
- [[tech-bridge-cooking-with-codex]] — App Server 첫 소개, Retrodex
- [[codex-app-server]] · [[harness-as-platform]] · [[tools-and-context-over-harness]] · [[deferred-tool-context]] · [[agent-client-protocol]]
