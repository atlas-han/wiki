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

## 만드는 팀의 사용기 (2026-09-05 ingest · [[tech-bridge-claude-code-team-workflow]])

Claude Code 팀 엔지니어 3인이 자기 도구를 어떻게 쓰는지 증언했다.

- **[[claude-tag|Claude Tag]]** — Slack 네이티브 에이전트. 팀 업무의 **70~80%** 가 여기서 일어난다. Slack을 고른 이유는 UI가 아니라 **맥락**이다 — 팀이 제품에 대해 내린 *"모든 결정들"* 이 이미 거기 있다.
- **routine** — 클라우드 컨테이너에서 도는 정기 작업. 예: *"매일 우리가 받는 **모든 피드백을 살펴보고 중요도에 따라 분류**한 다음, 실제로 해결할 가능성이 높은 문제부터 해결."*
- **workflows** — 에이전트가 서브에이전트 오케스트레이션 코드를 직접 쓴다. 신뢰의 근거가 고전적이다 — *"이 항목들을 순회하는 **for 루프**를 작성할 때 (…) '아, 맞다. **for 루프는 항목 중 하나라도 건너뛰지 않겠구나**'."*
- **기능은 지워진다** — todo 리스트는 Sonnet 3.5의 장기 시야 부족을 메우려 만들었고 1년 뒤 *"마치 사라진 것처럼"* 됐다. AskUserQuestion은 HTML 아티팩트에 밀렸다. → [[harness-pruning]]
- 지난 1년의 추가분을 팀이 이렇게 요약한다 — *"Claude Code로 시작해서 **자동 모드, 메모리, workflow** 같은 기본적인 기능들을 추가해 나간 것."*
- ⚠️ 자막에 미해소 토큰 **"2E"** 가 나온다(*"open up the 2E or the desktop app"*). Claude Tag 바깥의 직접 조작 표면을 가리키지만 확장형은 확정하지 않는다.

## 계층적 CLAUDE.md 상속 (2026-09-05 · [[tech-bridge-six-agent-skills]])

> Claude Code는 프로젝트 내의 `CLAUDE.md`와 **그 상위 폴더에 있는 모든 `CLAUDE.md`를 읽습니다.**

[[ai-labs]]가 이 성질로 **중간 스코프**를 만든다 — 모든 프로젝트를 담는 "개발자 폴더" 하나에 `CLAUDE.md`를 두어 공통 규칙을 상속시키되, *"컴퓨터의 **다른 부분에서 실행되는 관련 없는 세션에는 적용되지 않도록**"* 한다. 전역(`~/.claude`)과 프로젝트별 사이의 빈자리를 디렉터리 계층으로 메운 것이다. → [[llm-coding-guidelines]]

## References

- [[anthropic-claude-code-auto-mode]]
- [[anthropic-managed-agents]]
- [[anthropic-harness-design-long-running-apps]]
- [[anthropic-dynamic-workflows]]
- [[multica-karpathy-skills-claude-md]]
- [[lum1104-understand-anything]]
- [[charlychoi-claude-code-best-practices]]
- [[tech-bridge-claude-code-team-workflow]]
- [[tech-bridge-six-agent-skills]]
- [[tech-bridge-ai-native-sdlc]]
