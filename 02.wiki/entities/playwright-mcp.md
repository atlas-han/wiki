---
title: Playwright MCP
type: entity
category: tool
tags: [mcp, browser-automation, qa, agent-tooling]
aliases: [Playwright]
sources: [anthropic-harness-design-long-running-apps]
links: []
created: 2026-05-25
updated: 2026-05-25
---

# Playwright MCP

Browser 자동화 라이브러리 Playwright를 LLM 에이전트의 도구로 노출하는 [[model-context-protocol|MCP]] 서버. [[anthropic-harness-design-long-running-apps]]에서 evaluator agent가 실제 페이지를 네비게이트·클릭·스크린샷·검증하는 데 사용.

## 위키에서 알려진 사실

- Frontend 실험에서 evaluator가 **정적 스크린샷이 아닌 실제 페이지를 직접 조작**하며 평가 → 각 사이클이 wall-clock 시간을 소비 (최대 4시간 풀 런)
- 풀스택 harness에서는 UI 동작, API 엔드포인트, DB 상태를 사용자처럼 검사하는 QA 채널
- 발견 예시: drag로 안 채워지는 fill 툴, 잘못된 delete key 가드, FastAPI 라우트 순서 버그 → 모두 코드 위치까지 지목

## 미해결 사항

- 정확한 tool 집합, 자체 호스팅 vs Anthropic 호스팅, 정책·security 모델 — 별도 ingest 필요

## References

- [[anthropic-harness-design-long-running-apps]]
