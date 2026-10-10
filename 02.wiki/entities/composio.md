---
title: Composio
type: entity
category: org
tags: [agent-infrastructure, tool-calling, knowledge-work, integrations, mcp, agent-native-interface]
links:
  - "https://composio.dev"
  - "https://composio.dev/mcp-gateway"
sources: [tech-bridge-knowledge-work-agent-infrastructure, tech-bridge-composio-dashboard-is-dead]
created: 2026-09-09
updated: 2026-10-10
---

# Composio

**지식 노동 에이전트를 위한 인프라**를 만든다고 밝히는 회사. 이 위키 첫 등장은 [[tech-bridge-knowledge-work-agent-infrastructure]](공동창업자 겸 CTO [[karan-vaidya]]), 두 번째는 [[tech-bridge-composio-dashboard-is-dead]]([[sarah-simionescu]], 팀이 Composio 대시보드 담당).

> ⚠️ **이 페이지의 모든 내용은 당사자 진술이며 독립 확인이 없다.** 회사가 파는 것이 곧 이 회사가 *병목* 이라고 주장하는 것이다.

## 위키에서 알려진 사실

- 자기 정의: 코딩에는 있고 지식 노동에는 없는 **여섯 primitive**(중앙화·히스토리·맥락·검증·거버넌스·가역성)를 짓는다 → [[knowledge-work-agent-gap]].
- 제품 축으로 서술된 것:
  - **"빠져 있는 중심(the missing center)"** — 모든 앱·연결·로그인이 존재하는 한 곳.
  - **기록(the record)** — 모든 앱에 걸친 행동 로깅 → [[agent-action-record]].
  - **샌드박스** — 실제 도구를 흉내 내어 파괴적 행동을 먼저 받아낸다 → [[action-reversibility]].
  - **두 층 거버넌스** — 결정론적 접근 제어 + 자연어 정책 → [[agent-governance-layers]].
- ⚠️ 주장된 규모, **출처 없음**: 누적 **10억+ 도구 호출**, 월 **3억 도구 호출**.
- 발표 말미에 **채용 중**이라고 밝힌다.

## 두 번째 발표 — 에이전트를 위한 인터페이스 (2026-10-10 · [[tech-bridge-composio-dashboard-is-dead]])

[[sarah-simionescu|Sarah Simionescu]]는 같은 회사를 **인프라 primitive가 아니라 인터페이스 설계**로 설명한다 — *"at Composeio[=Composio] we are developing a brand new interface specifically designed for agents. We translate messy, sparsely documented, everchanging APIs (…) into something that agents really love to use. So, we build on top of MCP, CLI, and native tools"*(06:37~06:55) → [[agent-native-interface]] (신규).

- 발화된 제품 요소: **Composio MCP**(Claude에 연결) · **Composio search** — 에이전트가 과제를 진술하면 *"not only the correct tools it needs, but actually a plan of how to use them"*(05:20~05:27) · **Composio remote workbench** — 중간 결과를 컨텍스트에 싣지 않고 정규식 SQL을 동적 생성(08:13~08:26) · **toolkit** = 앱의 사내 용어(07:38~07:41).
- 자사 문제의 고백: *"our GitHub like toolkit alone has over 200 tools"*(04:03~04:11) — 도구 과부하의 예가 자기 툴킷이다.
- 출발점: *"Composio began as a tool to help developers"*(09:03~09:05) — 이제 *"requests from startups saying their clients are begging for a way to use their services through their agents"*(09:21~09:28, ⚠️ 건수·회사명 없음).
- ⚠️ **벤치마크**: 앱별 네이티브 MCP(Claude 마켓플레이스 등재) 대비 *"early unreleased"* 결과, 같은 과제·같은 모델, *"a clear difference"*(06:16~06:32) — **수치 미발화, 당사자 진술.** 첫 데모는 화자 스스로 **목업**(04:42~04:45).
- 설명란은 *"Composio MCP 게이트웨이"*(composio.dev/mcp-gateway)를 링크하지만 **"gateway"는 발화에 없다.**

## 이 위키에서의 자리

이 위키가 본 조직 중 **에이전트 자체나 모델이 아니라 "에이전트가 딛고 설 바닥"을 판다고 말하는 첫 회사**다. [[cursor|Cursor]]가 코딩 안에서 하네스를 파는 것과 대비된다 — Composio의 주장은 **코딩 밖에는 하네스가 딛을 바닥조차 없다**는 것이다.

두 발표를 겹치면 Composio의 자기 서술은 **바닥(기록·거버넌스·샌드박스) + 그 위의 에이전트용 인터페이스(검색·계획·컨텍스트 절약)** 다. 두 화자 모두 같은 결손 — *앱이 흩어져 있다*(중앙화 primitive / *"Each MCP server knows about itself and nothing else"*) — 에서 출발한다.

## References

- [[tech-bridge-knowledge-work-agent-infrastructure]] · [[karan-vaidya]] · [[knowledge-work-agent-gap]]
- [[tech-bridge-composio-dashboard-is-dead]] · [[sarah-simionescu]] · [[agent-native-interface]] (2026-10-10)
