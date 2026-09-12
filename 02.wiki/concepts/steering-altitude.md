---
title: 조향 고도 (Steering Altitude)
type: concept
category: pattern
tags: [design, control, human-in-the-loop, delegation, altitude, agent]
aliases: [level of control, right altitude, 통제 수준, 조향 고도]
related: [adjective-verb-steering, no-one-shot-design, goal-level-delegation, harness-pruning, signal-layer, decision-quality, agent-governance-layers, figma]
first-seen: tech-bridge-impeccable-design-steering
sources: [tech-bridge-impeccable-design-steering]
created: 2026-09-12
updated: 2026-09-12
---

# 조향 고도

**사람이 에이전트를 어느 높이에서 조종하는가 — 픽셀(직접 조작)은 너무 낮고 목표("디자인해 줘")는 슬롭이며, 그 사이의 정확한 통제 수준을 찾는 것이 도구 설계의 문제다.** [[paul-bakaus]]가 [[tech-bridge-impeccable-design-steering]]에서 *"디자인에 맞는 통제 수준을 찾는 것"* 으로 발표를 요약했다.

## 두 세계와 탐색되지 않은 중간

> 실제 디자인 작업에서는 지금 놀 수 있는 **두 세계**가 있는 것 같아요. 하나는 **직접 조작(direct manipulation)** — 픽셀 공간이죠. [[figma|Figma]]에서 마진·패딩을 만지거나, Webflow에서 최종 산출물을 직접 조작하는 것. (…) 그래서 반대쪽 극단으로 갑니다 — 에이전트에게 *"이거 디자인해 줘"* 라고 그냥 말하는 것. (03:32~04:05)

> 우리가 충분히 탐색하지 않은 **중간 지대**가 있는 것 같습니다 — **정확한 통제 수준은 무엇인가? 사람을 루프에 정확히 맞는 시점에 어떻게 끼워 넣을까?** (04:05~04:17)

| 고도 | 형태 | 판정 |
|---|---|---|
| **낮음** | 패딩·마진·간격 직접 조작 | *"대부분의 작업에서 **고도가 너무 낮다**"* — *"Opus로 div 가운데 정렬"*(인기 트윗) |
| **중간** | [[adjective-verb-steering\|형용사·동사]] | *"딱 필요한 만큼의 통제"* |
| **높음** | 완전 자율 — *"디자인해 줘"* | 2022년식 페이지 · [[ai-slop\|슬롭]] — *"아무도 아무것도 결정하지 않은"* |

## 고도는 옮겨 다닌다 — 그리고 양 끝이 남는다

> **올바른 고도(altitude)는 옮겨 다닙니다.** 그 고도에서 모든 문제를 풀 수 있다고는 생각하지 않아요. 맨 처음에는 여전히 여지가 있어요 — **탐색적 작업**을 원하고 뭔가 화면에 올리고 싶을 때, 또는 **마지막 폴리시**만 원할 때. 지금 AI는 **좋음에서 훌륭함으로 가는 마지막 5%, 10%, 어쩌면 20%** 에서 사람을 대체할 만큼 좋지 않다고 봅니다. (11:18~11:46)

즉 중간 고도는 **워크플로의 중간**에 해당한다 — 맨 앞(탐색, 높은 고도 허용)과 맨 뒤(폴리시, 낮은 고도 = 사람 손)는 남는다. 이것이 [[impeccable]]의 워크플로 맵(초기화 → 제작·반복 → harden·polish → 시스템 복귀)과 대응한다.

## 이 위키에서의 자리 — 위임 고도와 채점기

이 위키가 지금까지 본 *고도 이동* 은 전부 **위로** 였다.

| 소스 | 이동 | 이유 |
|---|---|---|
| [[goal-level-delegation]] ([[tech-bridge-claude-code-team-workflow\|Claude Code 팀]]) | 도구 호출 감시 → **목표 통째 위임** | **산출물 검증**이 감시를 대체 |
| [[harness-pruning]] | 토큰 수준 교정 삭제 | 모델이 좋아져서 |
| [[frontier-engineering]] | 사람은 루프 밖 | 컴파일·테스트·커버리지 바 |

이 개념은 **디자인에서는 그 이동을 멈춘다.** 이유가 다르다 — 모델이 못 해서가 아니라(*"어쩌면 영원히"* 라고 하면서도 *"AI가 더 낫게 만들기는 한다"*), **검증할 채점기가 없기 때문**이다: *"사용자도 의견이 있다. 디자인은 지저분하다."* [[signal-layer]]의 채점기 경계선을 여기에 대면 — **자동 채점기가 있는 영역(코드)은 위임 고도가 올라가고, 없는 영역(디자인)은 사람이 중간 고도에 남는다.** ⚠️ 이 연결은 위키의 정리이며 어느 소스도 말하지 않는다.

그리고 [[decision-quality]]([[ibm]])가 코드에서 *결정은 사람 몫* 이라 한 것과 같은 판정이다 — 디자인에서 *결정* 은 형용사를 고르는 일이고, 그것이 **자동화하면 안 되는 이유**로 제시된다(→ [[no-one-shot-design]]의 *"auto는 없다"*).

## ⚠️ 미해결

- *"올바른 고도는 옮겨 다닌다"* 의 **기준** — 언제 어느 고도인지 판정 규칙 없음. 사후 관찰.
- 화자가 *"어쩌면 영원히"* 와 *"지금 AI는 … 좋지 않다"* 를 함께 말한다 — 원리적 한계인지 현재 능력의 한계인지 **모호**. 위키는 어느 쪽도 채택하지 않는다.
- 당사자 진술, 정량 근거 없음.

## References

- [[tech-bridge-impeccable-design-steering]] (first-seen) · [[paul-bakaus]] · [[impeccable]]
- 관련: [[adjective-verb-steering]] · [[no-one-shot-design]] · [[goal-level-delegation]] · [[signal-layer]] · [[decision-quality]]
