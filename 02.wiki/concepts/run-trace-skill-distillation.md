---
title: 실행 트레이스 → 스킬 증류 (Run-Trace Skill Distillation)
type: concept
category: pattern
tags: [agent-skills, self-improving-agents, skill-library, trace-distillation, voyager, no-human-gate, organizational-flywheel]
aliases: [트레이스 증류, 스킬 증류기, skill distiller, self-improving organizational flywheel]
related: [skill-self-improvement, query-to-skill-distillation, trace-to-memory-loop, agent-skills, mcp-skill-distribution, agent-fleet-learning, company-knowledge-moat, skill-evals, prompt-injection]
first-seen: tech-bridge-runlayer-self-improving-skills-mcp
sources: [tech-bridge-runlayer-self-improving-skills-mcp]
created: 2026-10-16
updated: 2026-10-16
---

# 실행 트레이스 → 스킬 증류

**에이전트가 실제 작업을 하고 나면 그 실행 트레이스(성공이든 실패든)를 frontier LLM에 넘겨 재사용 가능한 [[agent-skills|스킬]]로 증류하고, 이후 실행이 그 스킬을 쓰게 하는 루프.** [[tech-bridge-runlayer-self-improving-skills-mcp]]에서 [[runlayer|Runlayer]]의 [[rafal-wilinski|Rafal Wilinski]]가 설명했다. 계보로는 Voyager의 skill library를 명시한다.

> *"exploration should be turned into reusable procedural knowledge"* (11:12~11:18)

## 계보 — Voyager의 skill library (09:49~11:18)

2023년 Minecraft 에이전트 Voyager: *"when the agent figured out something um it saved the recipe as a code that uh that consisted of the tool calls that lead it (…) to the discovery"*(10:41~10:51). 그래서 나중에 *"It didn't have to figure it out this whole knowledge from scratch"*(10:59~11:03)가 된다. 가중치·모델·프롬프트는 건드리지 않았다(10:19~10:24). ⚠️ 저자·논문 출처는 화자가 말하지 않았다.

## 루프

| 칸 | en-orig |
|---|---|
| 재료 | *"when the run succeeds and when there is something interesting in this run there's multiple tool calls"*(11:26~11:32) |
| 증류 | *"we just take that trace and we ask frontier LLM to simply distill a skill"*(11:32~11:41) — 증류 모델은 특정되지 않았다 |
| 실패도 재료 | *"a roundout[=run that] goes sideways is actually the richest signal (…) it exposes the missing guardrail, the missing library, some kind of edge case"*(11:57~12:05) |
| 효과 | 성공은 스킬을 *"more trustworthy"*, 실패는 *"more robust"* 하게 만든다(12:16~12:29) |
| 게이트 | ⚠️ *"completely autonomously asynchronously without human in loop"*(12:29~12:33) |
| 조직 단위 | 비슷한 실행을 묶어 증류 → 프롬프트 인젝션·PII 등 검사 → 스킬 라이브러리 → MCP gateway로 전사 배포(15:15~15:37) → [[mcp-skill-distribution]] |

**쓰는 쪽은 일한 에이전트가 아니라 별도의 증류기다.** 제목의 "스스로 스킬을 작성"은 이 점에서 부정확하다.

## 근거 — 36% → 100% (⚠️ 단일 사례)

Sonnet 4.6이 AWS Lambda 안에서 Chromium fork를 실행하는 사내 태스크에서 성공률이 36%였다. 한 실행이 문제를 풀고 그 트레이스로 증류한 스킬을 *"all the future runs"* 에 넣자 100%가 됐다(12:36~13:16). **실행 횟수·기간·증류 모델·비용 수치는 발화되지 않았다.** 같은 태스크에서 증류한 스킬을 같은 태스크에 다시 넣은 것이므로, 이 수치는 일반화가 아니라 *한 번 푼 해법의 재사용* 을 보여 준다. 화자 스스로 *"the success rate is the easiest number to show"*(13:22~13:24)라고 단서를 단다.

## 왜 하는가 — 빌린 지능 (13:45~14:25)

*"frontier intelligence is rented or borrowed. It can disappear. (…) we all miss Fable"* — 지능에 접근할 수 있는 동안 절차를 증류해 *"a catalog of how the works gets done inside our company as a collective subconscious"* 로 남기라는 주장이다. 효과로는 탐색 공간 축소와 토큰·비용 절감을 든다(13:24~13:42, ⚠️ 수치 없음).

## 이 위키에서의 좌표

| 패턴 | 재료 | 출력 | 승격 게이트 | 반경 |
|---|---|---|---|---|
| [[skill-self-improvement]] (task-observer) | 실패 관찰 | 스킬 수정안 | **사람** | 프로젝트 |
| [[query-to-skill-distillation]] (Vercel) | 성공한 실제 질의 | 새 스킬 | 없음 | 한 에이전트 |
| [[trace-to-memory-loop]] (LangChain) | 트레이스 | 메모리·스킬 파일 | procedural은 사람·eval | 한 에이전트 |
| **이 패턴 (Runlayer)** | **성공 + 실패 트레이스** | 새 스킬 | **자동 검사만**(인젝션·PII) | **전사**(MCP) |

## ⚠️ 유보

- **게이트.** 반경이 가장 큰데 게이트는 가장 얇다. 잘못 증류된 스킬을 회수하거나 롤백하는 방법, [[skill-evals|회귀 eval]], 스킬끼리 충돌할 때의 해소 방법은 발화되지 않았다 → [[skill-self-improvement]]의 *"한 번의 우연이 영구 규칙이 되면 오염"*.
- **노후화.** 한 모델의 실패에서 증류한 스킬이 다음 모델에서도 맞는지 다루지 않는다 → [[harness-pruning]].
- **트레이스 안의 비밀.** PII 검사는 언급되지만 자격증명 검사는 *"bunch of other stuff"*(15:27)에 묻혀 있다.
- 단일 실행 증류(11:32)와 "similar runs" 묶음 증류(15:15)의 관계는 설명되지 않았다.

## References

- [[tech-bridge-runlayer-self-improving-skills-mcp]] — first-seen
- [[skill-self-improvement]] · [[query-to-skill-distillation]] · [[trace-to-memory-loop]] · [[mcp-skill-distribution]] · [[agent-fleet-learning]]
