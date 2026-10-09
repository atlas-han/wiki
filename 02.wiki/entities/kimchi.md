---
title: Kimchi (Cast AI 코딩 하네스)
type: entity
category: product
tags: [coding-agents, harness, model-routing, open-source, long-running-agents, cloud-agents, kanban, cost-per-task]
aliases: [Kimchi, Kimchi coding, Kimchi harness, Ferment, Kimchi Teleport, Kimchi Studio]
links:
  - https://kimchi.dev/
  - https://github.com/getkimchi/kimchi
sources: [tech-bridge-kimchi-cost-per-task-harness]
created: 2026-10-09
updated: 2026-10-09
---

# Kimchi

**[[cast-ai|Cast AI]]의 오픈소스 코딩 에이전트 하네스 — 작업 결과를 기준으로 상용·오픈 모델을 자동 선택하고, 장시간 자율 루프(Ferment)·원격 샌드박스(Teleport)·팀 칸반(Studio)을 얹은 플랫폼.** 이 위키에서는 [[tech-bridge-kimchi-cost-per-task-harness]]로 처음 등장한다. 발화된 부제: *"proprietary models for edge case but use open source for the rest"*(00:12~00:17).

> ⚠️ **이름.** en-orig는 *"Kimshi"·"Kimy"·"Kimmy Coding"*, ko는 앞부분 *"김시"*, 08:00 이후 *"김치"*. 설명란 kimchi.dev를 따른다. 기능 이름 Ferment는 en-orig *"Fant"·"fment"*, ko *"발효"·"파멘트"*.

## 구성 (전부 자사 발표)

| 구성 | 내용 | 자막 |
|---|---|---|
| **하네스** | *"select the right model for the task at the right time based on the outcome of the task"*. 내부 *"py mono SSDK"*(⚠️ pi-mono로 추정). 6월 12일 무렵 1순위가 Kimi 2.6 → **[[minimax-m3\|MiniMax 3]]** 로 이동한 사내 차트 → [[automatic-model-routing]] | 04:17~04:28 · 05:40~06:25 · 07:46~07:57 |
| **Ferment** | 장시간 과제(*"more than two hours"*), 질문 → 마일스톤 분할 → 빌드·점검·재수정 루프 → **점수 B 이상이면 완료**(A 재시도 가능) → **스테이징까지만 자동 배포** | 08:02~10:45 |
| **Teleport** | 노트북을 닫아도 원격 보안 샌드박스(Google Kubernetes)에서 계속, SaaS·온프레미스, 모바일 접근. ⚠️ *"62% of our engineers are only using teleports"* → [[cloud-agent-delegation]] | 11:35~14:09 |
| **Studio** | Teleport 위 팀 보드 — 계획을 동료·PM이 리뷰, 검토 요청 세션을 넘겨받는 칸반, 5~10명 팀 | 14:10~16:51 |

**오픈소스 범위**: *"Most of it at least the harness is entirely open source. Uh studio and teleport. You need a Google account"*, *"five minute install"*(17:06~17:17). ⚠️ Studio·Teleport 자체의 오픈소스 여부는 문장이 끊겨 불분명.

## 설계상의 사람 위치

- Ferment의 *"human envelope[=involvement]"* 는 *"every two hours every three hours"*(08:04~08:11) — Teleport는 그 간격을 전제로 만들어졌다(12:04~12:12).
- *"We still believe there's like some little human that needs to be in the loop before going to the production. At least at this point"*(10:11~10:18) — 다음 단계는 SLO·파드 헬스체크를 보고 자동 출시.

> ⚠️ **채점자 미상.** 점수를 매기는 모델·루브릭·*"B"* 의 기준은 발화되지 않는다(*"higher order model"* 은 공동 발표자 Laura의 해설, 09:29~09:37). 점수가 모델 선택에 되먹임되는 방식도 미발화.

## References

- [[tech-bridge-kimchi-cost-per-task-harness]] · [[cast-ai]] · [[automatic-model-routing]] · [[model-mixing-economics]] · [[true-cost-to-perfect-answer]] · [[cloud-agent-delegation]] · [[generator-evaluator-pattern]] · [[minimax-m3]]
