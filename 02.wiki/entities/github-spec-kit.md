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

- 코어 파이프라인: Constitution → Spec → Plan → Task (채널 설명과 공식 퀵스타트가 일치).
- 산출물은 마크다운 아티팩트. 다음 단계의 입력이 되어 프롬프트 대신 **저장되는 계약**으로 에이전트를 묶는다 ([[spec-driven-development]]).
- [[tech-bridge-spec-driven-development]] 영상은 Copilot 연동과 Microsoft Build 세션 플래너 MCP 데모를 포함한다고 설명. 데모 세부는 자막 미확보.

> ⚠️ 제품 커맨드·에이전트 목록은 변동 가능. 구현 세부는 공식 문서를 재확인할 것.

## References

- [[tech-bridge-spec-driven-development]] · [[spec-driven-development]]
- <https://github.github.io/spec-kit/>
