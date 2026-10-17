---
title: Runlayer
type: entity
category: org
tags: [mcp, mcp-gateway, agent-skills, skill-registry, governance, vendor]
aliases: [Run Layer, Rumlayer, 런레이어]
links:
  - "https://www.runlayer.com"
  - "https://x.com/runlayer"
sources: [tech-bridge-runlayer-self-improving-skills-mcp]
created: 2026-10-16
updated: 2026-10-16
---

# Runlayer

**스스로를 *"the golden path for AI at your company"*(01:28~01:31)라고 소개하는 회사.** 이 위키에는 [[tech-bridge-runlayer-self-improving-skills-mcp]]로 처음 들어왔다. 발표자는 founding engineer [[rafal-wilinski|Rafal Wilinski]].

⚠️ 표기: en-orig는 *"Rumlayer"*(01:28) · *"run layer"*(06:14, 08:16, 11:23) · *"run later"*(15:11)로 흔들린다. 설명란 `runlayer.com` 기준으로 판독했다. `en`과 ko는 **"Runway"**(01:28) · **"PromptLayer"**(06:14) · "Run AI"(15:11) — 모두 다른 회사 이름이므로 그대로 따르면 안 된다.

## 소스에서 확인되는 것 (⚠️ 전부 당사자 진술)

| 항목 | en-orig |
|---|---|
| 스킬 스캔 | *"at run layer we are scanning thousands of skills every day and there is really weird stuff inside."*(06:13~06:18) — 수치·사례 없음 |
| 원격 MCP 서버로 스킬 배포 | *"We've been doing that internally at run layer for the past 6 months and it's been working quite well."*(08:14~08:18) — 정책 적용, 역할별 스킬 버전(08:07~08:14) |
| 트레이스 증류 | 성공한 실행의 트레이스를 *"frontier LLM"* 에 넘겨 스킬로 증류(11:23~11:41). 실패 실행도 넣는다(11:50~12:14). *"without human in loop"*(12:31~12:33) |
| 36% → 100% | Sonnet 4.6, AWS Lambda 안의 Chromium fork(12:36~13:16) — ⚠️ 단일 태스크, 실행 횟수 미발화 |
| 조직 플라이휠 | *"self-improving organizational flywheel"*(15:11~15:14): 비슷한 실행을 묶어 증류 → 프롬프트 인젝션·PII 등 검사 → 스킬 라이브러리 → *"our MCB[=MCP] gateway"* 로 전사의 모든 클라이언트·에이전트에 배포(15:15~15:37) |

## 이 위키에서의 위치

- [[tessl|Tessl]]처럼 **스킬 유통 계층을 파는 쪽**이다. Tessl의 레지스트리는 *사람의 보안·품질 리뷰와 게시 권한* 을 내세우고, Runlayer는 **자동 증류 + 자동 검사 + MCP 배포**를 내세운다.
- MCP gateway를 가진 회사가 "MCP = 스킬의 배포 계층"을 주장한다 — ⚠️ 이해관계가 있다.

## 미해결 사항

- 제품명·가격·고객. "MCP gateway"의 기능 범위. 자동 검사의 *"bunch of other stuff"*(15:27).

## References

- [[tech-bridge-runlayer-self-improving-skills-mcp]] · [[rafal-wilinski]] · [[mcp-skill-distribution]] · [[run-trace-skill-distillation]]
