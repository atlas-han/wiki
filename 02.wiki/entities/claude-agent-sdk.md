---
title: Claude Agent SDK
type: entity
category: tool
tags: [anthropic, sdk, agent, claude]
aliases: [Agent SDK]
sources: [anthropic-harness-design-long-running-apps]
links:
  - https://platform.claude.com/docs/en/agent-sdk/overview
created: 2026-05-25
updated: 2026-05-25
---

# Claude Agent SDK

[[anthropic|Anthropic]]이 제공하는 에이전트 빌딩 SDK. [[anthropic-harness-design-long-running-apps]]에서 Prithvi Rajasekaran의 frontend·풀스택 harness 모두 이 SDK 위에서 구현됨.

## 위키에서 알려진 사실

- 생성기·평가기 등 다중 에이전트의 **orchestration**을 단순하게 유지하는 베이스
- **자동 compaction**으로 context 성장 관리 (Opus 4.6 시점에서는 sprint construct 제거 후에도 안정적으로 작동했다고 보고됨)
- Frontend evaluator에 [[playwright-mcp|Playwright MCP]]를 연결해 실제 페이지 클릭·스크린샷·검토 수행

## 미해결 사항

- 정확한 API 표면, tool 정의 방식, 메모리·skill 모델 등 — 별도 문서 ingest 필요

## References

- [[anthropic-harness-design-long-running-apps]]
- [공식 문서](https://platform.claude.com/docs/en/agent-sdk/overview)
