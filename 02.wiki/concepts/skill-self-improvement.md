---
title: Skill Self-Improvement
type: concept
category: pattern
tags: [agent-skills, feedback-loop, governance, claude-code]
related: [agent-skills, harness-pruning, self-harness, generator-evaluator-pattern]
first-seen: tech-bridge-six-agent-skills
sources: [tech-bridge-six-agent-skills]
created: 2026-09-05
updated: 2026-09-05
---

# Skill Self-Improvement

**실제 작업 중에 발생한 실패를 관찰해 [[agent-skills|스킬]] 자체의 개선안을 축적하되, 반영은 사람의 검토를 거치는 패턴.** [[tech-bridge-six-agent-skills]]의 `task-observer` 스킬이 이 위키에서의 first-seen이다.

## 문제 — 스킬은 만들기보다 유지가 어렵다

> **가장 큰 문제는 스킬을 만드는 것 자체가 아닙니다. 최신 상태로 유지하는 것입니다.**

핵심 논거는 예측 불가능성이다.

> **한 번 앉아서 에이전트가 저지를 모든 실수를 예측할 수는 없습니다.**

즉 스킬의 빈틈은 설계 시점이 아니라 **사용 시점**에만 드러난다. 그래서 개선의 원천을 회고가 아니라 **작업 중 관찰**에 둔다.

## 구조

| 요소 | 역할 |
|---|---|
| **관찰자** | 작업 중 상시 실행. `CLAUDE.md`에 지시를 넣어 유지한다 |
| **`log.md`** | 스킬별 섹션 아래 **제안된 변경 사항**이 쌓인다 |
| **전역 규칙 파일** | *"어떤 스킬도 실제 고객의 이름을 파일에 기록해서는 안 된다"* 처럼 **모든 스킬에 걸리는** 규칙 |
| **사람의 검토 게이트** | 로그의 교훈을 읽고 **영구 반영 여부를 결정** |

교훈은 두 종류로 나온다 — **금지**(이 도구를 여기 쓰지 마라)와 **대체**(올바른 출처는 이것이다). 금지만 쌓이면 스킬이 점점 방어적이 되므로 대체가 함께 기록되는 것이 중요하다.

## 핵심 설계 — 자동 반영하지 않는다

이 패턴의 값은 자동화가 아니라 **자동화를 멈춘 지점**에 있다.

> 로그에 기록된 내용은 (…) **검토한 후** 영구적으로 반영할지 결정할 수 있습니다. 이렇게 하면 **하나의 잘못된 결과가 에이전트가 영원히 따르는 규칙으로 자동 설정되는 것을 방지**할 수 있습니다.

즉 **관찰은 자동, 승격은 수동**이다. 한 번의 우연한 실패가 영구 규칙이 되면 스킬은 개선되는 게 아니라 오염된다.

## 스코프 선택

전역(`~/.claude`)과 프로젝트별 중에서 **프로젝트별을 권장**한다 — *"각 프로젝트의 교훈이 분리되어 관리하기가 더 쉬워집니다."* 교훈은 대개 그 코드베이스의 사정에 묶여 있기 때문이다.

## 사례 — Logo Hub

[[ai-labs|AI Labs]]의 영상 애니메이션 스킬에서 나온 실화다. 브랜드 로고 SVG를 얻으려고 에이전트가 Logo Hub의 CLI 도구를 썼는데 *"그 도구는 **다른 용도로 만들어진 것이라 실패**했습니다."* 기록된 교훈은 금지 하나와 대체 하나였고, 검토 후 반영되어 *"이제 애니메이션 에이전트는 브랜드 로고를 어디에서 가져와야 하는지 정확히 알고" 있다.*

## 위키에서의 좌표

| 패턴 | 무엇이 무엇을 고치는가 | 승격 게이트 |
|---|---|---|
| **skill-self-improvement** | 실패 관찰 → **스킬** | **사람** |
| [[self-harness]] | 하네스가 **자기 하네스** | 자동(논문 설정) |
| [[harness-pruning]] | 모델 향상 → 하네스 **축소** | 사람(팀 판단) |
| [[generator-evaluator-pattern]] | 채점기 → **산출물** | 루프 내 |

[[tech-bridge-ai-native-skills]]의 스킬 거버넌스가 *"스킬을 어떻게 승인·배포할 것인가"* 였다면, 이 패턴은 *"승인된 스킬이 어떻게 낡아가고 어떻게 갱신되는가"* 를 다룬다. 둘은 같은 수명주기의 앞뒤다.

## References

- [[tech-bridge-six-agent-skills]] — first-seen
- 관련: [[agent-skills]] · [[self-harness]] · [[harness-pruning]] · [[generator-evaluator-pattern]] · [[llm-coding-guidelines]]
