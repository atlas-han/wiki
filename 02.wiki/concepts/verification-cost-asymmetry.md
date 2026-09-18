---
title: 검증 비용의 비대칭 (Verification Cost Asymmetry)
type: concept
category: theory
tags: [verification, np, complexity, agents, evaluation, economics]
aliases: [NP형 작업, 실행보다 검증이 쉬운, verify cheaper than execute]
related: [task-entropy-matrix, generator-evaluator-pattern, verification-bottleneck, agent-verification-skill, behavior-validated-trust, verifiable-goals]
first-seen: tech-bridge-mousepower-measuring-agents
sources: [tech-bridge-mousepower-measuring-agents, tech-bridge-lauren-tan-trusting-agents, tech-bridge-tokens-should-have-jobs]
created: 2026-09-13
updated: 2026-09-18
---

# 검증 비용의 비대칭

**에이전트가 경제적으로 성립하는 작업은 검증이 실행보다 싼 작업이다.** [[maximillian-piras]]가 [[tech-bridge-mousepower-measuring-agents]]에서 **NP형 문제의 모양**이라고 표현했다.

> 이런 것들은 **NP형 문제의 모양**이 됩니다 — **실행보다 검증이 더 쉽다**는 뜻입니다.

> 자막은 양 트랙 모두 *"MP style problem"* 이지만, 화자가 바로 이어 **"실행보다 검증이 더 쉽다"** 고 정의하므로 **NP로 읽는다.**

## 두 방향의 귀결

### ① 비대칭이 없으면 만들지 말라

> **수용 기준의 불확실성이 높으면 검증이 실행과 구분되지 않는 지점**에 옵니다. **유용했는지 검증하려고 사람이 사실상 그 일을 다시 해야 한다면, 그 일에 왜 에이전트를 만듭니까.**

→ [[task-entropy-matrix]]

### ② 비대칭이 있으면 검증도 자동화하라

> **검증의 반복 가능한 패턴을 찾아낼 수 있다면 그 문제에도 에이전트를 던져 넣을 수 있습니다.** 그러니 **에이전트만 만드는 게 아니라, 그 에이전트의 작업을 검증하는 에이전트도 만드는** 거죠.

이것이 [[generator-evaluator-pattern]]의 **경제적 정당화**다 — 그 패턴이 왜 성립하는지는 검증이 실행보다 싸기 때문이다.

## 두 소스가 갈라지는 자리

같은 날 업로드된 [[tech-bridge-lauren-tan-trusting-agents]]는 **같은 비대칭을 반대로 쓴다.**

| | [[maximillian-piras]] (Yutori) | [[lauren-tan]] (Cursor) |
|---|---|---|
| 비대칭이 없을 때 | **그 작업을 고르지 않는다** | **비대칭을 만든다** — 검증을 스킬로 짓고([[agent-verification-skill]]) 코드베이스를 검증 가능하게 다시 짓는다([[dune-architecture]]) |
| 전제 | 판매자는 고객의 작업을 고를 수 없다 | 자기 코드베이스는 자기가 바꿀 수 있다 |

**모순이 아니라 가진 통제권의 차이**다. 두 소스는 서로를 언급하지 않는다. → [[verification-bottleneck]]

## 표시해 둔 것

> ⚠️ **검증자의 독립성 문제가 두 소스 모두에서 제기되지 않는다.** 검증 에이전트가 실행 에이전트와 같은 모델·같은 편향이면 비대칭은 회복되지 않는다. Lauren Tan 쪽이 *다른 모델의 판정 에이전트* 를 쓰지만 **루브릭을 만드는 것은 여전히 코디네이터 에이전트**다. 2026-09-09 Cursor 편에서 처음 표시한 빈자리가 **세 번째로 반복**된다.

## References

- [[tech-bridge-mousepower-measuring-agents]] · [[tech-bridge-lauren-tan-trusting-agents]] · [[task-entropy-matrix]] · [[generator-evaluator-pattern]] · [[verification-bottleneck]] · [[agent-verification-skill]]

## 판매자가 같은 결론을 채점 방식으로 (2026-09-18 · [[tech-bridge-tokens-should-have-jobs]])

[[angela-jiang]]([[anthropic]])이 재무 분석 벤치의 채점을 바꾸는 이유로 **①과 같은 문장**을 말한다.

> 만약 벤치에서 **80%의 정확도**를 보였다면 훌륭해 보일 수 있지만, 실제로는 **전문가가 직접 손익계산서를 다시 계산하거나 수정하거나, 아니면 재실행을 해야 한다** (…) **100% 정확하지 않으면 사실상 쓸모가 없기 때문**입니다. (06:51~07:09)

| | [[maximillian-piras]] (Yutori, 09-13) | [[angela-jiang]] (Anthropic, 09-18) |
|---|---|---|
| 문장 | *사람이 다시 해야 하면 왜 에이전트를 만드나* | *전문가가 다시 계산해야 하면 80%는 쓸모없다* |
| 쓰임 | **작업 선택** 기준 | **채점 방식** — 100% 아니면 실패 |
| 위치 | 판매자가 자기 위치를 밝히고 | **판매자**(플랫폼) |

→ [[all-or-nothing-accuracy]]. 세 소스가 서로를 언급하지 않는다. 그리고 이 렌즈가 성립하려면 **수용 기준이 확정된 작업**이어야 한다(P&L) — [[task-entropy-matrix]]의 낮은 엔트로피 칸이다.

> ⚠️ 검증자의 독립성 빈자리가 **네 번째로** 반복된다 — 이번 소스도 *누가 100%를 판정하는가* 를 말하지 않는다.
