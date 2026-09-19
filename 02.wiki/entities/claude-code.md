---
title: Claude Code
type: entity
category: product
tags: [anthropic, agent, cli, coding-agent]
aliases: [클로드 코드]
sources: [anthropic-claude-code-auto-mode, anthropic-managed-agents, multica-karpathy-skills-claude-md, anthropic-dynamic-workflows, lum1104-understand-anything, charlychoi-claude-code-best-practices, tech-bridge-impeccable-design-steering, tech-bridge-graft-code-knowledge-graph, tech-bridge-vercel-eve-filesystem-agent]
links:
  - https://code.claude.com/docs
created: 2026-05-25
updated: 2026-09-19
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

## 디자인 스킬의 호스트, 그리고 "Claude 베이지" (2026-09-12 · [[tech-bridge-impeccable-design-steering]])

- [[impeccable|Impeccable]](디자인 스킬)이 *"모든 하네스에서 동작"* 하는 목록의 첫 자리 — Claude Code, GitHub Copilot, [[cursor]], [[codex]]. ASR은 *"cloud code"* 였으나 하네스 목록 문맥이라 **Claude Code로 확정**(09-11 Google Cloud 편의 *"Cloud Code"* 판정 불가와 다른 처리).
- [[paul-bakaus]]가 지금의 [[ai-slop|슬롭]]을 **"Claude 베이지"**(Instrument Serif·이탤릭)라 부른다 — *"꼭 나쁜 디자인은 아니다, 그냥 전부 그렇게 생겼을 뿐."* 그리고 섹션 번호를 *"GPT가 아주 좋아하고 Claude도 좋아하는"* 흔적으로 든다. ⚠️ 이 관찰의 대상은 *"Claw Design"*(Claude Design 추정)의 기본 출력이며 Claude Code 자체의 평가는 아니다.

## 외부 증언 — 파일 시스템 에이전트의 원형으로 (2026-09-19 · [[tech-bridge-vercel-eve-filesystem-agent]])

[[vercel|Vercel]]의 [[andrew-qu|Andrew Qu]]가 **자사 에이전트를 세 번 실패한 뒤** Claude Code를 보고 무엇을 바꿨는지 공개했다. **이 위키가 받은 Claude Code에 대한 가장 구체적인 제3자 증언**이다 — 그동안의 서술은 대부분 [[anthropic|Anthropic]] 자신의 것이었다.

> 우리는 옆에서 **"와, [Claude Code]와 [[claude-opus-4-5|Opus 4.5]]는 우리가 이전에 가지고 있던 것과 비교하면 거의 인공 일반 지능(AGI)이나 다름없네."** 라고 생각했습니다. 우리가 직접 개발한 에이전트와는 달리, **이 에이전트는 거의 모든 질문에 막힘없이 답해줬습니다.** (07:38~07:53)

그가 **무엇이 달랐는지** 로 지목한 것:

> **핵심은 바로 파일 시스템이었다** … **최소한의 도구 세트, 즉 파일 목록 보기, 파일 읽기, bash 실행 정도만** … 하지만 가장 중요한 것은 **에이전트가 잘 훈련된 도구를 활용할 수 있었고 필요한 곳에 스스로 탐색하고 작업을 작성할 수 있었다**는 점입니다. **[Claude Code]에 매우 구체적인 도구 세트를 제공하지 않았습니다.** 마치 **자유롭게 탐색하고 새로운 행동(emergent behavior)을 발견하도록 내버려 둔 것**과 같았습니다. (07:53~08:28)

→ [[file-system-agent]]

그리고 **도약을 두 단계로 센다** — 단일 에이전트 → **[[claude-agent-sdk|Claude Code SDK]]** → 자기 용례에 맞춰 바닥을 다시 깐 파일 시스템 에이전트(09:04~09:09). 즉 SDK를 그대로 쓰는 것과 **원리를 가져와 자기 바닥을 까는 것**을 구분한다. 결과는 *"eval 점수 두 배"*(⚠️ 실체 없음).

Claude Code는 이 소스에서 **비교 기준점으로도** 쓰인다 — 베타 고객 Aura가 *"기성품 Claude 코드를 쓰는 것과 달리"* [[eve-framework|Eve]]로 처음부터 구축했다는 대목(14:15~14:26, ⚠️ 수치 없음).

⚠️ en-orig가 *Claude Code* 를 **"Cod code"** 로 반복 오인식했고 ko가 일부 자리에서 *Claude* 를 떨어뜨렸다 — raw 헤더 참조.

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
