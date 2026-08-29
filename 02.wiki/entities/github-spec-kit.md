---
title: GitHub Spec Kit
type: entity
category: tool
tags: [github, spec, cli, copilot, agent]
links:
  - https://github.com/github/spec-kit
  - https://github.github.io/spec-kit/
sources: [tech-bridge-spec-driven-development]
created: 2026-08-29
updated: 2026-08-29
---

# GitHub Spec Kit

GitHub이 공개한 **스펙 주도 개발 하니스**. `specify` CLI로 저장소에 constitution / spec / plan / task 템플릿과 에이전트 슬래시 커맨드(`/speckit.*`)를 심는다. Copilot·[[claude-code|Claude Code]]·Cursor 등 다수 코딩 에이전트와 붙는 것이 공식 포지션. 본 위키에는 [[tech-bridge-spec-driven-development]]를 통해 첫 등장.

## 위키에서 알려진 사실

- 코어: Constitution → Spec → Plan → Task → Implement. 공식은 그 위에 clarify / checklist / analyze / converge.
- `specify init`이 에이전트별 인스트럭션을 심는다 (데모는 Copilot + Windows PowerShell). 발표자: 마법이 아니라 마크다운과 스크립트.
- 산출물은 Git history의 일부. 다음 기능은 같은 베이스 위에 새 spec.
- [[tech-bridge-spec-driven-development]] 라이브 데모: Build 2026 세션 플래너 MCP 서버를 빈 레포에서 만들어 MCP Inspector로 `search session`까지 실행.

> ⚠️ 제품 커맨드·에이전트 목록은 변동 가능. 구현 세부는 공식 문서를 재확인할 것.

## References

- [[tech-bridge-spec-driven-development]] · [[spec-driven-development]]
- <https://github.github.io/spec-kit/>
