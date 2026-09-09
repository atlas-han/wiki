---
title: 계획→티켓 파이프라인 (Plan-to-Ticket Pipeline)
type: concept
category: pattern
tags: [plan-mode, tickets, jira, scoping, migration, tdd]
aliases: [plan mode, 계획 모드, 계획에서 티켓으로]
related: [cloud-agent-delegation, spec-driven-development, intent-md, sprint-contract, executable-standards, model-mixing-economics, verifiable-goals]
first-seen: tech-bridge-cursor-legacy-refactoring
sources: [tech-bridge-cursor-legacy-refactoring]
created: 2026-09-09
updated: 2026-09-09
---

# 계획→티켓 파이프라인

**큰 마이그레이션을 한 번에 시키지 않고, 코드를 쓰지 않는 계획 단계를 거쳐 티켓으로 쪼갠 뒤 위임하는** 워크플로.

## 코드를 쓰지 않는 모드가 별도로 있다

> **출력이 마크다운 파일입니다. 문서입니다. Cursor는 plan mode에서 절대 코드를 만들거나 쓰지 않습니다. 오직 전략만 써줍니다.** — [[tech-bridge-cursor-legacy-refactoring]]

이것이 이 패턴의 핵심 성질이다. 이 위키의 [[spec-driven-development]]·[[intent-md]]·[[sprint-contract]]가 다뤄온 *코드 앞단의 산출물* 이 **제품 기능으로 강제되는** 사례다.

## 계획 전에 되묻는다

> 계획을 실제로 쓰기 전에 **Cursor가 아주 잘하는 것은 저에게서 방향을 일찍 받아내는 것**입니다. *"레거시 컴포넌트라는 게 좀 모호한데, 이 설계는 어떤 범위를 대상으로 해야 하나요?"*

`ask question` 도구는 **계획 전 최소 질문 수를 강제하도록 커스터마이즈할 수 있다.** → [[fuzzy-intent-discovery]]가 커머스 에이전트에서 본 *모호한 의도를 먼저 좁히는* 루프와 같은 구조가 개발 도구에 나타난 것이다.

## 계획서는 템플릿을 따르고 살아 있다

- 템플릿이 **Confluence에 산다** — *"제 모든 계획이 똑같이 생기기를 원하니까요."* → [[executable-standards]]
- 소스의 템플릿은 **TDD 템플릿**이다.
- 계획서는 **편집 가능한 살아 있는 문서** — 일부를 채팅에 넣어 *"이 섹션 줄여줘"* 가 가능하다.
- 내용: 기능·비기능 요구사항, 하이레벨 접근, **현재 상태 및 목표 아키텍처 다이어그램**, 시퀀스·데이터 흐름, API 설계, 데이터 모델, 피처 플래그.

다이어그램은 **mermaid**가 기본이고 Lucidchart·Excalidraw·FigJam으로 출력할 수 있다.

## 계획 → 티켓 → PR

계획을 **플러그인(Atlassian MCP)** 으로 Jira 에픽의 티켓들로 쪼갠다. 각 티켓에는 **목표·범위·수락 기준·테스트·의존성·노트**가 들어간다.

그 다음 티켓 묶음을 [[cloud-agent-delegation|cloud agent]]에 넘기면 **티켓당 별도 PR**이 나온다.

> **모든 걸 하나의 거대한 PR에 넣지 않도록 해야 합니다. 리뷰하기가 너무 감당이 안 되니까요.**

이 분할이 [[verifiable-goals]]가 말한 *검증 가능한 단위로 쪼개기* 와 같은 동기를 갖는다 — 다만 여기서는 **리뷰 가능성**이 명시적 이유다.

## 감사가 계획에 선행한다

계획 전에 `/canvas`로 코드베이스를 감사한다 — 테스트 커버리지, 빠진 부분, **마이그레이션 우선순위 분류**(다음에 옮길 것 / 그 다음 / 이미 React인 것). canvas는 코드베이스·파일·스프레드시트·MCP 데이터를 받아 **인터랙티브 시각화**를 만들고 **팀 범위로 공유**된다.

## ⚠️ 미해결

- **계획의 품질을 무엇이 검증하는가에 답이 없다** — 계획이 틀렸을 때 티켓과 PR이 전부 틀리는 경로가 논의되지 않는다.
- **WordPress 예제의 한계** — 공개 오픈소스 레포이고 **사내 레거시의 전형적 어려움(문서 없음·원저자 부재·비공개 의존성)이 다뤄지지 않는다.**

## References

- [[tech-bridge-cursor-legacy-refactoring]] · [[cursor]]
