---
title: "에이전트 코딩 성숙도 곡선 (Agentic Coding Maturity Curve) — 9단계 · 4레벨, 계곡, 자율 모드"
type: concept
category: pattern
tags: [agentic-coding, maturity-model, enterprise-adoption, salesforce, subagents, autonomy, ci, change-management]
aliases: [agentic coding maturity curve, 에이전트 코딩 성숙도 곡선, AI 성숙도 곡선, 9단계 성숙도 곡선, Salesforce maturity curve]
related: [eval-platform-maturity-stages, agent-change-evidence, goal-level-delegation, persistent-agent-teams, software-factory, perceived-vs-actual-productivity]
first-seen: tech-bridge-salesforce-claude-code-agentic-shift
sources: [tech-bridge-salesforce-claude-code-agentic-shift]
created: 2026-11-08
updated: 2026-11-08
---

# 에이전트 코딩 성숙도 곡선

**엔지니어 한 사람이 에이전트 코딩을 얼마나 깊이 쓰는지를 단계로 그린 지도.** [[salesforce|Salesforce]]가 사내 확산 과정에서 만들었다고 [[tech-bridge-salesforce-claude-code-agentic-shift]]의 해설이 전한다. 아홉 단계가 네 레벨로 묶이고, 대부분은 맨 왼쪽에서 시작한다.

> *"에이전트 코딩 성숙도 곡선입니다. 아홉 단계네 개의 레벨론 단이죠[=아홉 단계, 네 개의 레벨로 된 거죠]."*(02:30~02:34)

> ⚠️ **소스 하나, 2차 전달.** 곡선 그림은 화면에만 있고 위키는 보지 않았다. 아홉 단계의 이름과 레벨 2의 내용은 해설에 없다. 원 자료(Salesforce News · Claude 공식 영상)를 열지 않았다.

## 해설이 전하는 모양

| 구간 | 내용 |
|---|---|
| 출발 | 도구를 다 나눠줬는데 단순한 일에만 씀 — 그래서 지도를 만들었다 |
| 초반 상승 | *뭐든 시키면 되니까* 신난다 |
| **계곡** | *"자신감이 떨어지는 구간이죠."*(02:43~02:45) |
| 레벨 1 | *이거 해 줘*만 말하고 좋은 결과의 기준을 주지 않는다. 짧은 일은 되고 긴 일은 무너진다 — *좋은 결과의 기준도 계획도 없었으니까* |
| 레벨 2 | (해설에 없음) |
| 레벨 3 | 서브에이전트 팀을 꾸리고 일을 쪼개 병렬로 돌린다 |
| 레벨 4 | 사람이 시키지 않아도 돌아가는 **자율형** — CI 테스트가 깨지면 에이전트가 고치고, 다른 에이전트가 리뷰 · 머지 |

결과(해설 전달): 한두 달 만에 많은 엔지니어를 레벨 3 · 4로 올렸고 수천 명이 자율 모드로 일한다.

## 읽는 법

- **계곡이 레벨 1의 실패와 겹친다.** 해설은 계곡의 원인을 기준 · 계획의 부재로 설명한다. 그래서 곡선을 오르는 수단이 *도구*가 아니라 *일을 주는 방식*(좋은 결과 · 나쁜 결과의 기준, 증거 요구)이 된다 → [[agent-change-evidence]] · [[goal-level-delegation]].
- **확산 수단은 명령이 아니라 데모**였다고 한다 — 라이브 시연과 실제 출시 제품(같은 소스 5절).
- **레벨 4는 사람 없는 루프**다. 같은 날의 [[tech-bridge-anthropic-code-review-seven-layers]]가 그 루프를 지탱하는 층(필수 검사 · 위험도별 승인 · 롤백)을 말한다. 이 곡선에는 검증 쪽 단계가 보이지 않는다(해설 범위 안에서).
- 다른 영역의 단계 모델: [[eval-platform-maturity-stages]](eval 도구의 단계). 이것은 **사람의 사용 습관**의 단계다.

## 미해결

- 아홉 단계의 이름 · 레벨 2 · 단계별 측정 기준. 곡선의 y축이 무엇인지(자신감? 생산성?) 해설은 *계곡 = 자신감이 떨어지는 구간*이라고만 한다.
- 레벨 상승과 [[effective-output-metric|유효 산출량]] 상승의 관계는 해설이 따로 말하지 않는다.

## References

- [[tech-bridge-salesforce-claude-code-agentic-shift]] (4절)
- [[salesforce]]
