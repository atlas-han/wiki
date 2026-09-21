---
title: 오케스트레이터-서처 분업 (Orchestrator–Searcher Split)
type: concept
category: architecture
tags: [multi-agent, subagent, orchestration, knowledge-work, retrieval, memo]
aliases: [서처 에이전트, searcher agent, 로펌 구조, 파트너-어시스턴트]
related: [knowledge-agents-vs-coding-agents, oracle-gap, agent-collaboration-as-search, agents-as-patient-specialists, dynamic-workflows, context-window-as-floppy-disk, agent-manager-analogy, goal-level-delegation]
first-seen: tech-bridge-knowledge-agents-not-coding-agents
sources: [tech-bridge-knowledge-agents-not-coding-agents]
created: 2026-09-21
updated: 2026-09-21
---

# 오케스트레이터-서처 분업

**메인 에이전트는 직접 검색하지 않는다. 문제를 쪼개 쿼리를 발주하고, 서처 에이전트들이 각자 조사해 *메모*를 올리면, 그것으로 답한다.**

근거로 제시되는 것은 벤치마크가 아니라 **로펌의 분업 구조**다.

> 고객이 오면 **[로펌]의 파트너 변호사**를 찾아가서 *"제 상황은 이렇습니다"* 라고 말하는 거죠. 그리고 **파트너가 하는 일은 모든 법률 조사를 직접 하는 것이 아닙니다.** (…) 그들에게는 **[패러리걸]이 있고, 어시스턴트들이 있고, 그 어시스턴트들이 이 조사를 진행할 것입니다. 그들은 훈련받은 도구 [일습]을 사용하고 메모(memo)를 작성한 다음, 이를 [파트너]에게 전달할 것입니다.** — [[benjamin-clavie]], [[tech-bridge-knowledge-agents-not-coding-agents]] (11:12~11:53)

> [파트너는] 아마도 한 가지 정도 추가 설명을 직접 알아볼 수도 있겠지만, **대부분은 서처 에이전트, 즉 어시스턴트가 찾아낸 정보에 의존**할 것이고, **그것이 바로 여러분이 받게 될 답변입니다.** (11:53~12:06)

## 구현 형태

> 기본적으로 **질문에 답하는 메인 에이전트에게 이렇게 말하는 겁니다 — "그건 큰 주제이고 PDF가 수천 개나 있으니 당신이 직접 검색하지는 마세요. 그냥 저를 위해 문제를 쪼개 주세요. 실제 쿼리에 답하는 데 중요하다고 생각하는 측면들에 대해 쿼리를 작성해 주세요."** (14:00~14:21)

> **그러면 서처들이 각자 알아서 나가서 올바른 결과를 찾아오고, 여러분의 에이전트에게 작은 메모를 가져다주며, 그러면 에이전트가 실제로 답을 합니다.** (14:21~14:31)

| 역할 | 하는 일 | 하지 않는 일 |
|---|---|---|
| **오케스트레이터** | 문제를 **측면(aspect)으로 쪼개고** 쿼리를 작성한다 | **직접 검색하지 않는다** |
| **서처** | 각자 조사하고 **메모로 요약**해 올린다 | 최종 답을 쓰지 않는다 |

**메모가 인터페이스다.** 서처가 읽은 원문 전체가 아니라 **요약된 판단**이 올라간다 — 그래서 [[context-window-as-floppy-disk|플로피 디스크]]가 터지지 않는다.

## 왜 이 분업이 필요한가 — 코딩 에이전트에는 이미 있었다

> **코드에서는, [Claude Code]를 사용할 때 여러분이 그 작업을 직접 하고 있습니다. 여러분은 이미 쿼리를 쪼개 놓았고, 무엇을 하고 싶은지 알고 있으며, [Linear] 티켓 같은 걸 가지고 있죠.** **반면 현실에서는 아주 개방적인 문제를 가진 고객이 있고, 여러분이 직접 그것을 쪼개야 하고, 여러분의 에이전트도 스스로 그것을 쪼개야 하며, 그런 다음 이 조사를 수행할 서브 에이전트를 써야 합니다.** (12:06~12:28)

**즉 이 구조는 사람이 하던 분해 노동을 에이전트 안으로 옮기는 것**이다. → [[knowledge-agents-vs-coding-agents]]

## 성과로 제시된 것

| 지표 | 값 |
|---|---|
| 정확도 | **+3.5포인트** |
| [[oracle-gap\|오라클 갭]] | **약 10포인트 → 6포인트** |
| 실수 감소 | **약 40%** |

> **인간과 에이전트 사이의 격차가, 그저 검색을 위한 더 나은 아키텍처를 갖추는 것만으로 40% 줄어듭니다.** (14:51~14:59)

> ⚠️ **전부 자기 보고이고 측정 조건이 없다.** 벤치마크의 이름조차 자막에서 판독되지 않고, 서처의 개수·모델·비용이 전부 없다. **설명란은 *"40% 이상"* 이라 적었으나 자막은 *"약 40%"* 다 — 이 위키는 자막을 따른다.**

## 이 위키의 멀티 에이전트 논의와

**분업을 이득으로 셈한 첫 소스**다. 이 위키의 기존 페이지들은 분업을 **손실이나 필요악**으로 놓았다.

| 페이지 | 분업을 무엇으로 보나 |
|---|---|
| [[agent-collaboration-as-search]] ([[jean-denis-greze\|Greze]]) | **손실** — 이상은 단일 전지 에이전트, 멀티는 프라이버시 제약 아래의 **근사** |
| [[agent-architecture-progression]] ([[vercel\|Vercel]]) | **컨텍스트 손실 때문에** 오히려 구조를 **단순화**했다 |
| [[dynamic-workflows]] | 오케스트레이션을 **모델이 직접 쓴다** — 분업의 자동화 |
| [[agents-as-patient-specialists]] · [[agent-manager-analogy]] | 인간 조직 **비유**(관리·인내) |
| **이 페이지** | **이득** — 컨텍스트가 유한하고 문제가 개방형이라 **분업이 유일한 길** |

⚠️ **모순은 아니다.** [[agent-collaboration-as-search]]의 이상적 단일 에이전트는 *모든 정보를 볼 수 있다*고 가정하는데, 이 소스는 **볼 수 있어도 컨텍스트에 안 들어간다**고 말한다(16:47~17:03). **제약의 출처가 프라이버시냐 용량이냐가 다르다.**

## ⚠️ 빠져 있는 것

- **서처의 오류가 어떻게 전파되는가** — 메모가 틀리면 파트너는 알 수 없다. [[agent-collaboration-as-search]]가 기록한 *"LLM이 실수해서 정보 하나가 틀리면 영원히 오염된다"* 가 **그대로 적용되는데 소스는 다루지 않는다.**
- **비용** — 서처를 여럿 띄우는 값이 [[tools-are-not-neutral|20% 절감]]과 어떻게 상쇄되는지 없다.
- **몇 명의 서처인가 · 누가 정하는가** — 없다.
- **검증** — [[generator-evaluator-pattern]]·[[risk-proportional-human-review]]에 해당하는 게이트가 **한 번도 언급되지 않는다.** 법률·의료를 예시로 드는 발표인데 **사람의 승인 지점이 없다.**

## References

- [[tech-bridge-knowledge-agents-not-coding-agents]] · [[benjamin-clavie]] · [[mixedbread]]
- 상위: [[knowledge-agents-vs-coding-agents]] · [[tool-organization-loop]]
- 측정: [[oracle-gap]]
- 멀티 에이전트 축: [[agent-collaboration-as-search]] · [[agent-architecture-progression]] · [[dynamic-workflows]] · [[agents-as-patient-specialists]] · [[agent-manager-analogy]]
- ⚠️ 빈자리: [[generator-evaluator-pattern]] · [[risk-proportional-human-review]]
