---
title: Claude Agent SDK
type: entity
category: tool
tags: [anthropic, sdk, agent, claude]
aliases: [Agent SDK]
sources: [anthropic-harness-design-long-running-apps, tech-bridge-claude-managed-agents-workshop-2]
links:
  - "https://platform.claude.com/docs/en/agent-sdk/overview"
created: 2026-05-25
updated: 2026-10-19
---

# Claude Agent SDK

[[anthropic|Anthropic]]이 제공하는 에이전트 빌딩 SDK. [[anthropic-harness-design-long-running-apps]]에서 Prithvi Rajasekaran의 frontend·풀스택 harness 모두 이 SDK 위에서 구현됨.

## 위키에서 알려진 사실

- 생성기·평가기 등 다중 에이전트의 **orchestration**을 단순하게 유지하는 베이스
- **자동 compaction**으로 context 성장 관리 (Opus 4.6 시점에서는 sprint construct 제거 후에도 안정적으로 작동했다고 보고됨)
- Frontend evaluator에 [[playwright-mcp|Playwright MCP]]를 연결해 실제 페이지 클릭·스크린샷·검토 수행

## Managed Agents와의 관계 — 팀의 답 (2026-10-19 · [[tech-bridge-claude-managed-agents-workshop-2]])

- *"Agent SDK is basically like a Cloud[=Claude] Code in the form of a binary that you can take and run wherever you want."*(26:39~26:46) · *"It's a headless Cloud[=Claude] Code version."*(26:18~26:20)
- [[managed-agents|Claude Managed Agents]]는 SDK 위에 지은 것이 아니라 *"taking a lot of inspiration about the benefits and lessons from the Agent SDK, but we've rebuilt uh the harness to be a more generic not just coding specific thing"*(26:25~26:34) — 질문자의 *"sort of a fork?"*에 *"yeah"*.
- 선택 기준(위키 정리): SDK = 어디서나 돌리는 바이너리(직접 호스팅), CMA = Anthropic 클라우드의 완전 호스팅.
- ⚠️ 두 답변자([[priyanka-phatak|Priyanka Phatak]]·[[gabe-cemaj|Gabe Cemaj]])를 자막만으로 가르지 못한다.

## 미해결 사항

- 정확한 API 표면, tool 정의 방식, 메모리·skill 모델 등 — 별도 문서 ingest 필요

## References

- [[anthropic-harness-design-long-running-apps]]
- [[tech-bridge-claude-managed-agents-workshop-2]] — Managed Agents 팀의 Agent SDK 설명
- [공식 문서](https://platform.claude.com/docs/en/agent-sdk/overview)
