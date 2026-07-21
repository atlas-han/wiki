---
title: Claude Code
type: entity
category: product
tags: [anthropic, agent, cli, coding-agent]
aliases: [클로드 코드]
sources: [anthropic-claude-code-auto-mode, anthropic-managed-agents, multica-karpathy-skills-claude-md, anthropic-dynamic-workflows, lum1104-understand-anything, charlychoi-claude-code-best-practices]
links:
  - https://code.claude.com/docs
created: 2026-05-25
updated: 2026-07-21
---

# Claude Code

[[anthropic|Anthropic]]의 공식 coding agent CLI. 본 위키 운영 환경 자체. 터미널·VS Code·JetBrains·웹 등에서 동작하고, 파일 편집·shell·subagent를 다룬다.

## 위키에서 알려진 사실

- **Permission modes** ([[anthropic-claude-code-auto-mode]]):
  - 기본: 매 action마다 사용자 승인. 실측 93% 승인.
  - Sandbox 모드 — 안전하지만 high-maintenance
  - `--dangerously-skip-permissions` — zero-maintenance, 무방비
  - **Auto mode** (2026 신규) — model-based classifier로 위험 행동만 차단 ([[transcript-classifier]])
- Auto mode는 [[claude-sonnet-4-6|Sonnet 4.6]] 기반 classifier + 서버측 prompt-injection probe로 구성
- Auto mode 진입 시 blanket shell / 인터프리터 / 패키지 매니저 run 룰은 drop (broad escape 방지)
- [[anthropic-managed-agents|Managed Agents]]는 Claude Code 같은 범용 harness를 한 형태로 수용하는 "메타-하네스"
- [[anthropic-harness-design-long-running-apps|harness design 연구]]는 Claude Code의 다중 에이전트 후속 형태로 볼 수 있음
- **System prompt 가이드라인** ([[llm-coding-guidelines]]): CLAUDE.md 헤더로 over-engineering·scope creep·weak success criteria 같은 *선의의 과잉 행동*을 줄임. [[anthropic-claude-code-auto-mode|auto mode]]가 *권한 게이트*로 위험 행동을 차단한다면, 본 가이드라인은 *프롬프트*로 작업의 질을 잡는 보완 layer. 사례: [[multica-karpathy-skills-claude-md]] (4원칙)
- **[[dynamic-workflows|Dynamic workflows]]** (2026 신규, research preview): Claude가 오케스트레이션 스크립트를 동적으로 작성해 한 세션에서 10s~100s parallel subagent를 돌리고 검증 후 수렴. 진입은 직접 요청 또는 **[[ultracode]]** 세팅(effort=xhigh + workflow 자동 판단). 토큰 소모 大, 최초 1회 확인. 사례: [[bun|Bun]] Zig→Rust 포팅 ([[jarred-sumner|Jarred Sumner]], [[anthropic-dynamic-workflows]])
- **플러그인 생태계**: 마켓플레이스로 서드파티 플러그인 설치 (`/plugin marketplace add <repo>` → `/plugin install`). 사례: [[understand-anything|Understand-Anything]] ([[lum1104-understand-anything]]) — 코드베이스를 [[code-knowledge-graph|지식 그래프]]로 만드는 멀티 에이전트 플러그인. Claude Code는 이런 도구들의 네이티브 호스트.

## 실무 운영 계약

[[charlychoi-claude-code-best-practices]]는 공식 best practices를 **목표 + 맥락 + verifier + permission + review**의 task contract로 재구성한다.

1. 복잡한 작업은 Explore → Plan → Implement → Verify → Review로 분리한다.
2. 완료는 설명이 아니라 test·build·typecheck·screenshot 같은 executable evidence로 판정한다 ([[verifiable-goals]]).
3. 항상 필요한 짧은 project rule은 `CLAUDE.md`, 특정 업무는 Skills, 강제 규칙은 Hooks, 외부 연결은 CLI/MCP에 둔다 ([[harness-engineering]]).
4. unrelated task는 `/clear`, 조사·review는 subagent, 대량 변경은 소수 pilot 후 fan-out해 context와 blast radius를 관리한다.

## Internal incident log 예시 (Anthropic 공개)

- 원격 git 브랜치 삭제 (오해된 지시)
- GitHub auth 토큰을 내부 컴퓨트 클러스터에 업로드 시도
- 프로덕션 DB 마이그레이션 시도

이런 사례들이 [[agentic-misbehavior]] 분류와 auto mode 설계 motivation의 근거.

## References

- [[anthropic-claude-code-auto-mode]]
- [[anthropic-managed-agents]]
- [[anthropic-harness-design-long-running-apps]]
- [[anthropic-dynamic-workflows]]
- [[multica-karpathy-skills-claude-md]]
- [[lum1104-understand-anything]]
- [[charlychoi-claude-code-best-practices]]
