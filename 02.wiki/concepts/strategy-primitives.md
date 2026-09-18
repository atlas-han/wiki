---
title: 전략 프리미티브 (Strategy Primitives)
type: concept
category: pattern
tags: [meta-harness, orchestration, multi-agent, managed-agents, token-roles, composition, anthropic]
aliases: [프리미티브 조합, 메타 하네스 층, 동적 전략 구성]
related: [token-roles, managed-agents, agent-harness-design, generator-evaluator-pattern, self-harness, dynamic-workflows, agent-memory, harness-engineering, brain-hands-decoupling]
first-seen: tech-bridge-tokens-should-have-jobs
sources: [tech-bridge-tokens-should-have-jobs]
created: 2026-09-18
updated: 2026-09-18
---

# 전략 프리미티브

**개별 에이전트용 하네스 위에 메타 하네스(오케스트레이션) 층을 두고, 실행자·조언자·채점자·드리머 같은 역할을 조합 가능한 기본 요소(primitive)로 제공한다 — 그러면 전략을 짜는 일이 "비교적 간단"해지고, 새 역할을 발명할 수 있으며, 장기적으로는 모델과 플랫폼이 전략을 동적으로 구성한다.** [[angela-jiang|Angela Jiang]]([[anthropic|Anthropic]])이 [[tech-bridge-tokens-should-have-jobs]]의 마지막 챕터에서 [[managed-agents|Claude Managed Agents]]의 구조로 설명했다.

## 두 층

> 저희는 **개별 에이전트를 위한 정말 훌륭한 하네스**를 만들기 위해 많은 노력을 기울였습니다. (…) 이것이 바로 저희가 **Claude Managed Agents**에 사용한 아키텍처입니다. (10:35~10:48)

> 그리고 우리는 이 위에 더 나아가 **메타 하네스 수준, 즉 다중 에이전트 오케스트레이션 및 실행 수준**으로 진입하여 이 전략이 **실행자와 조언자 또는 전략 내의 다른 에이전트 간에 조정**될 수 있도록 합니다. 그리고 이러한 것들 중 일부, 예를 들어 **회고(dreaming)와 `outcomes`는 Claude Managed Agents에서 기본적으로 제공**됩니다. (10:52~11:12)

| 층 | 무엇 | 이 위키의 페이지 |
|---|---|---|
| **하네스** | 개별 에이전트의 루프 — 09-01의 *"하네스는 while 루프"* | [[agent-harness-design]] · [[managed-agents]](session/harness/sandbox) |
| **메타 하네스** | 여러 에이전트(역할) 사이의 조정 — 09-01의 *"우리는 '전략'이라 불렀다"* | **이 페이지** |

09-01에는 *"어떤 사람들은 메타 하네스라고 부른다"* 는 **말**이었고, 여기서는 **제품 층**이다 — 그리고 세 전략 중 **둘(회고·`outcomes`)이 기본 제공**된다. 조언은 기본 제공 목록에 없다(⚠️ 소스가 *"일부"* 라고만 한다).

## 조합 — 한 루프로 꿰기

> 이러한 **기본 요소(primitives)** 들을 활용하면 다양한 전략들을 결합하고 (…) 아키텍처를 구축하는 것이 **비교적 간단**합니다. (11:14~11:25)

> 작업을 수행하고 조언을 제공할 수 있으며 (…) **이 모든 결과를 가져와서 채점자에게 보내 검증이 루프 안에서 제대로 되는지** 확인 (…) 만약 통과된다면 (…) **그 모든 자료를 회고에 보내서 다음 시도가 그 어느 때보다 더 나아지도록** (11:27~11:51)

즉 **실행 → 조언 → 채점 → 회고**. 이 위키는 이 루프의 조각을 따로 가지고 있었다:

| 조각 | 이 위키의 페이지 | 출처 |
|---|---|---|
| 실행 + 채점 | [[generator-evaluator-pattern]] | Anthropic Labs 블로그 → `outcomes`(09-01) |
| 실행 + 회고 | [[self-harness]] · [[agent-memory]] | Shanghai AI Lab 논문 → dreaming(09-01) |
| 실행 + 조언 | [[token-roles]] · [[model-mixing-economics]] | 09-01 *Sonnet + Opus* |

이 소스가 더하는 것은 **셋이 같은 프리미티브 위에 직렬로 놓인다**는 것 — 그리고 *"완전히 새로운 역할들을 만들어낼 수도"*(12:09~12:13) 있다는 **확장성**이다.

## 장기 목표 — 동적 구성

> **장기적으로 저희의 큰 목표는 여러분이 업무를 수행하는 동안 이러한 전략을 동적으로 구성할 수 있도록 모델과 플랫폼을 더욱 개선하는 것**입니다. (12:16~12:23)

이 위키가 이미 두 방향에서 본 것의 **플랫폼 선언**이다 — [[self-harness]]에 기록된 Claude Code 팀의 *"Claude는 자기만의 하네스를 만드는 데 정말 능숙"*(09-05), 그리고 [[dynamic-workflows]](coordination이 대화 밖에서 돈다). 09-01의 [[brain-hands-decoupling|many brains, many hands]]가 *실행 단위* 의 분리였다면, 여기서는 **역할 단위의 조합을 모델에게 맡기는** 방향이다. ⚠️ **목표 선언뿐이고 실체가 없다.**

## 표시해 둔 것

> ⚠️ **화면의 아키텍처 그림은 자막에 없다.** ⚠️ *"Fable이 다시 온라인"*(11:33) 문장은 양 트랙 불분명 — 조언자 자리에 무엇을 배정했는지 판독 불가. ⚠️ **프리미티브의 실제 인터페이스**(09-01 문서의 `execute`/`provision`/`emitEvent` 와 어떻게 대응하는지)는 없다. ⚠️ 채점자·드리머가 실행자와 **같은 모델인지**, 루브릭을 누가 쓰는지 — 09-09 이래의 검증자 독립성 빈자리가 **판매자 발표에서도 열린 채**다.

## References

- [[tech-bridge-tokens-should-have-jobs]] · [[angela-jiang]] · [[katelyn-lesse]] · [[anthropic]]
- 관련: [[token-roles]] · [[managed-agents]] · [[agent-harness-design]] · [[generator-evaluator-pattern]] · [[self-harness]] · [[agent-memory]] · [[dynamic-workflows]] · [[harness-engineering]] · [[brain-hands-decoupling]] · [[model-mixing-economics]]
