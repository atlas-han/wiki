---
title: Debug Assist (Uber)
type: entity
category: product
tags: [debugging-agent, root-cause-analysis, langgraph, mcp, subagents, uber, internal-tool]
aliases: [Debug Assist, Debugger Assist, 디버거 어시스트, Uber Debug Assist]
links: []
sources: [tech-bridge-uber-debug-assist]
created: 2026-10-09
updated: 2026-10-09
---

# Debug Assist (Uber)

[[uber|Uber]]의 사내 AI 디버깅 에이전트. 버그 신고·크래시를 받아 **근본 원인 분석(RCA) → 완화(기능 플래그 롤백) → 수정 → 재현 검증 → PR** 까지 처리한다. [[tech-bridge-uber-debug-assist]]([[kriti-dangi|Kriti Dangi]])가 유일한 소스.

> ⚠️ **사내 도구, 공개 자료 없음.** 아래 구조·수치는 전부 발표자의 자기 진술이다. 이름은 en-orig *"debug assist"*, `en`·ko *"Debugger Assist"*·*"디버거 어시스트"* — 제목·설명란 표기 **Debug Assist** 를 따른다.

## 구조 (08:46~14:52)

LangGraph 파이프라인, *"a mix of deterministic and LLM nodes"*(08:57~08:59) — 계획 단계를 우회하고 계획을 사람이 고정한다 → [[deterministic-agent-pipeline]]

| 노드 | 종류 | 모델·예산 |
|---|---|---|
| 컨텍스트 수집(로그 전처리·가지치기) | 결정론 | — |
| 분류·RCA(신뢰도 점수, [[model-context-protocol|MCP]]로 Jaeger·인시던트 조회, 병렬 서브에이전트: breadcrumb·crash correlation) | LLM | Sonnet, 턴 제한(약 20턴) |
| 완화·수정(기능 플래그 MCP → 강한 상관이면 롤백) | LLM | Opus, 더 큰 max turns |
| 검증(*"basil test"* — Bazel 추정; 유닛·E2E·시뮬레이터 재현, 재시도 고정) | — | — |
| PR(Jira·Wisdom·Healthline에 첨부, Slack 전달) | — | — |

골격은 고정, 스킬·플러그인은 **에이전트 타입**별로 런타임에 가져온다(사내 마켓플레이스 약 3,000개 중 일부) → [[harness-as-platform]] · [[agent-skills]]

PR 이후: diff fixer(작은 증분 수정) · Ask AI(교정 → *"improve its own prompts and skills"*, 반영 경로 미발화) · 내 머신/원격 머신에서 열기(17:30~19:01). 관측: Arize 트레이싱으로 모든 LLM 호출·도구 호출·bash 명령 추적(25:12~25:46) → [[arize-ai]]

## 지표 (19:05~20:18, 자기 보고)

- 월 약 9,000건 RCA · 정확도 50%(*"as compared to exact developer fixes"*) + 나머지의 약 40%는 *"right direction"*
- PR 머지율 **5% → 약 48%**(시작 1년)
- ⚠️ Jira *"resolution time has increased (…) by twofold, which is a huge improvement"* — 말 그대로면 악화, 방향 미확정
- 고유 서브에이전트 30개 → domain extensions로 *"roughly 10,000 by the end of next half"*(계획치)

## References

- [[tech-bridge-uber-debug-assist]] — first-seen
- [[uber]] · [[kriti-dangi]] · [[langchain]] · [[arize-ai]]
