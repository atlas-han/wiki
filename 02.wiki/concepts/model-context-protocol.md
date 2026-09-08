---
title: Model Context Protocol (MCP)
type: concept
category: pattern
tags: [protocol, agent-tooling, interoperability, anthropic, open-standard]
aliases: [MCP]
related: [agent-harness-design, brain-hands-decoupling, agent-knowledge-sourcing, agent-skills]
first-seen: anthropic-harness-design-long-running-apps
sources: [anthropic-harness-design-long-running-apps, anthropic-managed-agents, tech-bridge-multimodal-commerce-agent, tech-bridge-agent-knowledge-four-ways]
created: 2026-05-25
updated: 2026-09-08
---

# Model Context Protocol (MCP)

[[anthropic|Anthropic]]이 주도해 만든 **오픈 표준** — AI 애플리케이션과 외부 시스템(데이터 소스·도구·워크플로) 사이의 연결 인터페이스. 본 위키에서 [[playwright-mcp|Playwright MCP]] 같은 구체적 서버가 등장.

## 한 줄 비유

> Think of MCP like a USB-C port for AI applications.

USB-C가 전자기기 연결의 표준이 된 것처럼, MCP는 AI 앱이 외부 시스템에 붙는 표준.

## 무엇을 가능하게 하나

- Agent가 Google Calendar·Notion에 접근해 개인화된 비서가 됨
- [[claude-code|Claude Code]]가 Figma 디자인으로 전체 웹 앱 생성
- 엔터프라이즈 챗봇이 여러 DB를 가로질러 데이터 분석
- AI가 Blender에서 3D 디자인을 만들어 3D 프린터로 출력

## 생태계 — 광범위한 클라이언트·서버 지원

| 카테고리 | 예 |
|---|---|
| AI 어시스턴트 | [Claude](https://claude.com/docs/connectors/building), [ChatGPT](https://developers.openai.com/api/docs/mcp/) |
| 개발 도구 | [VS Code](https://code.visualstudio.com/docs/copilot/chat/mcp-servers), [Cursor](https://cursor.com/docs/context/mcp) |
| 호환 클라이언트 | MCPJam 등 다수 |

"build once, integrate everywhere" — 한 번 MCP 서버로 노출하면 여러 클라이언트가 그대로 사용.

## 본 위키에서 등장한 MCP 사례

- [[playwright-mcp]] — 브라우저 자동화 (Playwright)를 MCP 서버로. [[anthropic-harness-design-long-running-apps]]의 evaluator agent가 실제 페이지 클릭·스크린샷·검증에 사용.
- [[anthropic-managed-agents]]에서: **MCP + secure vault + dedicated proxy** 패턴으로 토큰을 sandbox 밖에 격리. *"Claude calls MCP tools via a dedicated proxy; this proxy takes in a token associated with the session."*

## [[agent-harness-design]] 관점

MCP는 [[brain-hands-decoupling]]의 *hands* 쪽 구체적 구현체. `execute(name, input) → string`이라는 일반 인터페이스가 MCP tool 호출과 정합. Brain은 sandbox가 컨테이너인지·휴대폰인지·Pokémon emulator인지·MCP 서버인지 알 필요 없다.

## 에이전트 간 상거래의 인터페이스 기대 (2026-09-04)

[[tech-bridge-multimodal-commerce-agent]] Q&A에서 *"사용자가 사람이 아니라 에이전트가 되면"* 이라는 질문에 [[nidhi-kaushik-vyas]]가 답한 내용이다.

> **MCP가 이 둘 사이의 인터페이스 역할을 확실히 할 거라고 예상합니다.** 솔직히 말씀드리면, **아직 우리 에이전트가 다른 에이전트와 상호작용하는 단계에는 이르지 못했습니다.**

위 사례들이 전부 MCP를 *에이전트 → 도구* 방향으로 쓴 것과 달리, 여기서는 **에이전트 ↔ 에이전트**의 접점으로 지목된다. 다만 이는 **기대이지 구현이 아니다** — 같은 답변이 아직 그 단계가 아니라고 명시한다.

같은 소스가 판매자–에이전트 공통 언어로 **UCP**를 별도로 언급하는데, MCP와의 관계는 소스에 설명돼 있지 않고 약어의 뜻도 확정할 수 없다 ([[google-deepmind]] 참조).


## 스킬과의 분업 (2026-09-08 · [[tech-bridge-agent-knowledge-four-ways]])

이 페이지는 MCP를 **연결 표준**으로 설명해 왔고, [[agent-skills]]는 **조직 지식**으로 자라 왔다. 두 페이지가 서로를 `related`로만 걸고 있었는데 [[tech-bridge-agent-knowledge-four-ways]]가 **왜 둘이 함께 있어야 하는지**를 하나의 사고 위에서 보인다.

500 에러를 고치는 예제에서, [[agent-skills|스킬]]이 *"우선 오류율을 살펴봐야 합니다"* 라는 절차를 준 직후:

> **하지만 이야기는 거기서 끝납니다.** 해당 스킬은 에이전트에게 오류율을 확인하라고 지시할 수 있지만, **에이전트가 실제로 대시보드에 접속하여 오류율을 확인할 수 있는 것은 아닙니다.** 그래서 (…) **MCP**를 사용하는 것입니다.

> MCP를 사용하면 에이전트가 **MCP 호출을 통해 모든 로그 정보**를 얻을 수 있으므로 (…) 같은 방식으로 **지표**도 얻을 수 있으며, **실제 오류율을 확인**할 수 있습니다.

**스킬은 무엇을 할지 알고, MCP는 그것을 할 수 있게 한다.** [[brain-hands-decoupling]]의 뇌/손 분리를 **지식 조달 층**에서 다시 그린 형태이고, 이 페이지가 이미 적어 둔 *"MCP는 hands 쪽 구체적 구현체"* 라는 관찰과 정확히 맞물린다.

소스는 호스트/서버 관계도 간단히 정리한다 — *"에이전트 자체, 즉 **MCP 호스트**와 해당 에이전트가 통신하려는 **각 시스템(MCP 서버 뒤에 위치함)**"*. 그리고 MCP가 메우는 것이 **모델의 무지**임을 명시한다.

> 이 **모델 자체는 특정 로깅 스택의 백엔드를 쿼리하는 방법을 알지 못할 수도 있지만**, 해당 로깅 스택의 **MCP 서버는 연결 방법을 알고 있으며** 에이전트가 호출할 수 있도록 해당 연결을 제공합니다.

같은 소스의 라우팅 규칙에서 MCP는 *"바깥에서 실제로 조회해야 하는 것"* 에 배정된다. → [[agent-knowledge-sourcing]]

> ⚠️ 규칙의 한정어 *"without using proprietary code"* 가 무엇을 가리키는지 **소스가 부연하지 않는다.**

## References

- [[anthropic-harness-design-long-running-apps]]
- [[anthropic-managed-agents]]
- [[playwright-mcp]]
- [공식 사이트 modelcontextprotocol.io](https://modelcontextprotocol.io/introduction)
- [[tech-bridge-agent-knowledge-four-ways]] — 스킬과의 분업 · [[agent-knowledge-sourcing]]
