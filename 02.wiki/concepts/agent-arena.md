---
title: 에이전트 아레나 (Agent Arena)
type: concept
category: pattern
tags: [parallelism, multi-model, sub-agents, pstack, design-space]
aliases: [arena, 접목과 기각, graft or reject]
related: [agent-swarm, model-mixing-economics, generator-evaluator-pattern, dynamic-workflows, no-one-shot-design, skill-evals]
first-seen: tech-bridge-pstack-third-party-review
sources: [tech-bridge-pstack-third-party-review]
created: 2026-09-14
updated: 2026-09-14
---

# 에이전트 아레나

**서로 다른 모델 3~4개를 같은 문제에 붙이고, 각자의 가장 좋은 부분을 접목(graft)하거나 기각하는 병렬 패턴.** [[pstack|Pstack]]의 스킬 중 하나로 [[tech-bridge-pstack-third-party-review]]에서 처음 관찰된다.

> **중요한 기능이 있고 토큰이 문제가 아니라면 아레나를 돌릴 수 있습니다. 서로 다른 에이전트 셋 또는 넷을 같은 문제에 붙이고, 각자의 가장 좋은 부분을 뽑아 최종 커밋으로 감싸는 방식입니다.** (02:37~02:48)

> **아레나는 각 서브에이전트가 문제를 풀며 배운 것을 근거로 접목할지 기각할지를 결정합니다.** (02:57~03:04)

관찰된 실행에서 디자인 아이디어가 **Claude · GPT · Grok · Claude Opus 5** 에 분산됐다. 리뷰어의 반응이 비용을 말해 준다 — *"토큰 예산이 저기 날아가네요."*

## [[agent-swarm|스웜]]과의 차이

| | **아레나** | **[[agent-swarm\|스웜]]** |
|---|---|---|
| 입력 | **같은 문제**를 전원에게 | **문제의 다른 조각**을 각자에게 |
| 목적 | **최선을 고르기** | **일을 나누기** |
| 출력 | **접목된 단일 커밋** | **집계된 보고서** |
| 실패 시 | 나쁜 안이 **기각된다** | 조각이 **비어 있다** |

**이 축이 이 위키에 처음 명시된다.** 지금까지 병렬성은 [[dynamic-workflows]](Claude가 오케스트레이션을 동적 작성)·[[sweeper-agent]]·[[generator-evaluator-pattern]]으로 있었는데, **"같은 문제냐 쪼갠 문제냐"가 구분의 축이 된 적은 없었다.**

## 무엇의 실행 층인가

**아레나는 [[model-mixing-economics]]를 실행 층으로 내린다.** 2026-09-01 [[grok-4-6]] 기록이 *가격이 곧 병렬성* 이었고(70.8% @ $2.81 vs Fable 5 Max 70.5% @ $17.32), 여기서는 **여러 모델을 동시에 붙이는 것 자체가 하나의 스킬**이다 — 가격 차가 아니라 **관점 차**를 산다.

그리고 원칙 하나와 직접 연결된다 — **"설계 공간을 소진하라(exhaust the design space)"**:

> **바로 여기가 에이전트 아레나가 들어오는 자리입니다. 여러 모델과 에이전트가 같은 문제에 붙어 전부 중 최선을 내놓고, 가장 좋은 부분들을 최종 커밋에 접목합니다.** (09:17~09:28)

[[no-one-shot-design]]의 구현 측 판이다 — **첫 답을 받아들이지 않는 절차를 병렬성으로 산다.**

## 계보

리뷰어가 하나 덧붙인다:

> **이건 [[cursor|Cursor]]가 6개월 전에 넣었다가 나중에 뺀 기능이기도 합니다.** (02:49~02:52)

⚠️ **리뷰어 진술이고 근거가 없다.** 뺀 이유도 제시되지 않는다. **위키는 사실로 기록하지 않는다.**

## 열려 있는 것

- ⚠️ **접목(graft) 판정 기준이 없다.** *"각 서브에이전트가 배운 것을 근거로"* 가 전부다. **누가 판정하는가**(같은 모델? 별도 판정자? 라우터?)가 소스에 없다.
- ⚠️ **평가자의 독립성** — 2026-09-09 이래 이 위키가 반복해 표시해 온 *작성자=검증자* 문제가 여기서도 비어 있다. 후보를 낸 에이전트들이 서로를 판정하는 구조라면 [[skill-evals]]의 **눈가림 절차**가 필요한데 언급이 없다.
- ⚠️ **비용이 정량화되지 않는다.** *"토큰 예산이 날아간다"* 가 전부다.
- ⚠️ **언제 쓰지 말아야 하는지**는 한 줄뿐 — *"중요한 기능이고 토큰이 문제가 아닐 때"*.

## References

- [[tech-bridge-pstack-third-party-review]] · [[pstack]] · [[lauren-tan]] · [[molten-base]]
- 관련: [[agent-swarm]] · [[model-mixing-economics]] · [[generator-evaluator-pattern]] · [[dynamic-workflows]] · [[no-one-shot-design]] · [[skill-evals]] · [[grok-4-6]] · [[fable-5-1]]
