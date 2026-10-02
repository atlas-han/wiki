---
title: GitHub Spec Kit
type: entity
category: tool
tags: [github, spec, cli, copilot, agent]
links:
  - https://github.com/github/spec-kit
  - https://github.github.io/spec-kit/
sources: [tech-bridge-spec-driven-development, tech-bridge-sdd-full-course, tech-bridge-sdd-enterprise-lessons]
created: 2026-08-29
updated: 2026-10-02
---

# GitHub Spec Kit

GitHub이 공개한 **스펙 주도 개발 하니스**. `specify` CLI로 저장소에 constitution / spec / plan / task 템플릿과 에이전트 슬래시 커맨드(`/speckit.*`)를 심는다. Copilot·[[claude-code|Claude Code]]·Cursor 등 다수 코딩 에이전트와 붙는 것이 공식 포지션. 본 위키에는 [[tech-bridge-spec-driven-development]]를 통해 첫 등장.

## 위키에서 알려진 사실

- 코어: Constitution → Spec → Plan → Task → Implement. 공식은 그 위에 clarify / checklist / analyze / converge.
- `specify init`이 에이전트별 인스트럭션을 심는다 (데모는 Copilot + Windows PowerShell). 발표자: 마법이 아니라 마크다운과 스크립트.
- 산출물은 Git history의 일부. 다음 기능은 같은 베이스 위에 새 spec.
- [[tech-bridge-spec-driven-development]] 라이브 데모: Build 2026 세션 플래너 MCP 서버를 빈 레포에서 만들어 MCP Inspector로 `search session`까지 실행.

> ⚠️ 제품 커맨드·에이전트 목록은 변동 가능. 구현 세부는 공식 문서를 재확인할 것.

## 여러 도구 중 하나로 (2026-09-27 · [[tech-bridge-sdd-full-course]])

[[jetbrains|JetBrains]] 협업 SDD 강좌는 도구 없이 워크플로를 가르친 뒤 끝부분에서 Spec Kit을 *"GitHub's Spec Kit is **one attempt** at formalizing a spec-driven development workflow with agents"*(54:43~54:49)로 소개한다. 설치하면 *"slash commands in your agent, similar to the workflow you used in this course"* — *"SpecKit.constitution, plan, tasks, and implement"*(54:50~55:01).

- ⚠️ 강좌의 열거에는 **`specify` 단계가 없다**(en-orig 그대로). 08-29 편 데모의 `/speckit.specify`와 다르다 — 강좌가 생략한 것인지 발화의 누락인지 확인하지 않았다.
- 대안으로 **OpenSpec**(Fission AI, propose · explore · apply · archive)을 나란히 두고, 둘 다 *"branch management, verification scripts, and opinionated spec document formats"*(55:26~55:34)를 갖췄다고 한다. 권고는 채택보다 **자기 워크플로를 다듬는 참고**(55:35~55:39).
- ⚠️ **constitution의 뜻이 다르다** — Spec Kit(08-29 편)은 규칙, 강좌는 mission · tech stack · roadmap. [[spec-driven-development]] 참조.

## "too developer centric" — 엔터프라이즈 실무자의 평 (2026-10-02 · [[tech-bridge-sdd-enterprise-lessons]])

[[simon-martinelli|Simon Martinelli]]는 [[kiro|Amazon Kiro]] · BMAD Method · Tessl 도구와 함께 Spec Kit을 *"great tools"* 라 하면서도 *"they are all in my opinion at least too developer centric"*(03:13~03:24)이라 묶는다. 대안은 요구공학자가 쓰는 use case + entity model에서 **plan/tasks 없이** 바로 구현하는 [[ai-unified-process|AI Unified Process]]. Spec Kit에 대한 구체 비판(커맨드·산출물)은 없다 — 도구 일반의 흐름(PRD → plan → tasks → implement)을 Kiro를 예로 설명할 뿐이다(05:49~06:01).

## References

- [[tech-bridge-spec-driven-development]] · [[tech-bridge-sdd-full-course]] · [[spec-driven-development]]
- <https://github.github.io/spec-kit/>
