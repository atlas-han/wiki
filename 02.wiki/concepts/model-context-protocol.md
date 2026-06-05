---
title: Model Context Protocol (MCP)
type: concept
category: pattern
tags: [protocol, agent-tooling, interoperability, anthropic, open-standard]
aliases: [MCP]
related: [agent-harness-design, brain-hands-decoupling]
first-seen: anthropic-harness-design-long-running-apps
sources: [anthropic-harness-design-long-running-apps, anthropic-managed-agents]
created: 2026-05-25
updated: 2026-05-25
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

## References

- [[anthropic-harness-design-long-running-apps]]
- [[anthropic-managed-agents]]
- [[playwright-mcp]]
- [공식 사이트 modelcontextprotocol.io](https://modelcontextprotocol.io/introduction)
