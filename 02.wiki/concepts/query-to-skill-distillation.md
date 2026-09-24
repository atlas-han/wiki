---
title: 쿼리를 스킬로 증류하기 (Query-to-Skill Distillation)
type: concept
category: pattern
tags: [agent-skills, feedback-loop, context, automation, no-human-gate]
aliases: [쿼리 증류, 스킬 자동 증류]
related: [agent-skills, skill-self-improvement, agent-knowledge-sourcing, context-engineering, sweeper-agent, no-silent-write]
first-seen: tech-bridge-vercel-eve-filesystem-agent
sources: [tech-bridge-vercel-eve-filesystem-agent, tech-bridge-oracle-agent-memory-harness]
created: 2026-09-19
updated: 2026-09-24
---

# 쿼리를 스킬로 증류하기

**실제로 들어온 사용자 질의를 주기적으로 모아 반복되는 형태를 [[agent-skills|스킬]]로 압축하고, 새 실행이 그 스킬 위에서 시작하게 하는 루프.** [[tech-bridge-vercel-eve-filesystem-agent]]에서 [[vercel|Vercel]]의 D0 에이전트가 돌리는 방식이다.

## 관찰 — 질의는 생각보다 같은 모양이다

> **고객 지표, 판매 지표, 수치 지표, NPM 다운로드** 등 모든 것에 대한 **쿼리가 하루에도 수천 건씩** 들어왔습니다. 알고 보니 **이러한 쿼리의 형태는 상당 부분 동일했습니다.** (10:02~10:19)

> **집계 방법, 제품 조회 방법, 청구 정보 조회 방법은 한정되어 있기 때문입니다.** (10:19~10:28)

**다양성은 표면에 있고 구조는 유한하다**는 관찰이다. 질문은 수천 가지지만 *집계한다 · 제품을 찾는다 · 청구를 본다* 라는 골격은 몇 개뿐이다.

## 루프

> **가장 최근의 쿼리를 가져와서** 처리하는 **반복 작업(recurring job)** 을 만들었습니다. 이러한 기능들을 **하나의 스킬로 압축(distill)** 하려고 합니다. 현재 저희는 … **약 100개의 스킬**을 보유하고 있습니다. (10:19~10:30)

## 왜 효과가 있는가 — 매 실행은 빈손에서 시작한다

> 이 방식이 매우 효과적이라는 것을 알게 되었는데, **새로운 에이전트를 실행할 때마다 사실상 아무것도 없는 상태에서 시작하기 때문입니다.** **시맨틱 레이어와 시스템 프롬프트 외에는 미리 설정된 컨텍스트가 거의 없습니다.** 하지만 **스킬을 사용하면 이미 많은 컨텍스트 지식이 축적된 상태에서 시작**할 수 있습니다. (10:36~10:47)

이것이 [[file-system-agent]]의 대가를 갚는 구조다. 파일 시스템 에이전트는 **매번 처음부터 탐색**하므로 자유롭지만 **아무것도 기억하지 못한다.** 스킬은 그 탐색의 **결과물을 고정**한다 — 즉 *탐색의 자유* 와 *누적* 을 두 개의 층으로 나눈 것이다.

## [[skill-self-improvement]]과의 거울상

이 위키에 이미 스킬을 갱신하는 패턴이 있었다. **원천과 게이트가 정반대다.**

| | [[skill-self-improvement]] (09-05) | **이 패턴** |
|---|---|---|
| 원천 | **실패 관찰** — 에이전트가 틀린 자리 | **성공한 실제 질의** — 사람이 실제로 물은 것 |
| 방향 | 금지·대체 규칙을 **더한다** | 반복 형태를 **압축한다** |
| 승격 게이트 | **사람의 검토** — *"하나의 잘못된 결과가 영구 규칙이 되는 것을 방지"* | **없음 — 주기적 잡이 자동 증류** |
| 빈도 | 작업 중 상시 | 주기적 배치 |

두 패턴을 나란히 놓으면 **스킬의 수명주기가 두 입력을 갖는다** — 무엇이 잘 되는가(수요)와 무엇이 안 되는가(실패). 이 소스는 앞쪽만 자동화했다.

## ⚠️ 유보 — 게이트가 없다

**이 패턴의 가장 큰 빈자리는 검토다.**

- **누가 증류된 스킬을 보는가**가 없다. 09-05 소스가 명시적으로 막으려 한 것(*"한 번의 우연이 영구 규칙이 되는 것"*)이 여기서는 막혀 있지 않다.
- 09-10 [[tech-bridge-agent-to-agent-as-search|Greze]]의 경고가 그대로 적용된다 — *"LLM이 실수해서 정보 하나가 틀리면 영원히 오염된다."* 증류가 잘못된 쿼리를 정답으로 굳히면 이후 모든 실행이 그것을 상속한다. → [[sweeper-agent]] · [[no-silent-write]]
- **100개의 스킬이 서로 충돌하지 않는지**, 낡은 스킬이 어떻게 폐기되는지 없다. → [[harness-pruning]]
- **무엇을 "같은 형태"로 볼지의 기준**(클러스터링 방법·임계값)이 없다.
- 증류의 입력이 **질의뿐이고 결과가 아니다** — 자주 물어본 것과 잘 답한 것은 다르다. 소스는 이 구분을 하지 않는다.

## References

- [[tech-bridge-vercel-eve-filesystem-agent]] — first-seen
- [[vercel]] · [[andrew-qu]] · [[eve-framework]]
- 관련: [[agent-skills]] · [[skill-self-improvement]] · [[file-system-agent]] · [[agent-knowledge-sourcing]] · [[sweeper-agent]] · [[no-silent-write]] · [[harness-pruning]] · [[agent-memory]]

## 짝이 하나 더 — 버전 교체형 승격 (2026-09-24)

[[tech-bridge-oracle-agent-memory-harness]]의 **스킬 승격**은 이 페이지와 같이 **성공**에서 배우고 **게이트를 말하지 않지만**, 재료가 *질의 다수*가 아니라 **성공한 긴 세션 하나**이고, 결과가 *새 스킬 추가*가 아니라 **기존 skill.md를 증류한 새 버전으로 교체 · 옛 버전 은퇴**다(36:47~37:04). → [[skill-self-improvement]]의 3자 비교표.
