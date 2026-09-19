---
title: 필드 단위 유닛 테스트 평가 (Field-Level Unit Test Evals)
type: concept
category: pattern
tags: [evaluation, testing, granularity, voice-agents, debuggability]
aliases: [필드 단위 평가, E2E 대신 유닛 테스트]
related: [typed-field-collection, skill-evals, all-or-nothing-accuracy, test-harness-vs-test-authoring, verification-bottleneck]
first-seen: tech-bridge-voice-agent-failure-modes
sources: [tech-bridge-voice-agent-failure-modes]
created: 2026-09-19
updated: 2026-09-19
---

# 필드 단위 유닛 테스트 평가

**에이전트를 통째로 돌려 통과/실패를 보지 말고, 수집하는 필드 하나하나를 유닛 테스트처럼 평가한다.** [[tech-bridge-voice-agent-failure-modes]]의 네 번째 실패 모드이자 [[typed-field-collection]]의 짝이다.

> 그런 다음 **단위 테스트 관점에서 이렇게 실행하도록 만듭니다. 그러니까 여러분의 모든 평가(eval) 도구는 이러한 필드들을 단위 테스트처럼 취급해야 합니다. 그리고 단위 테스트가 제대로 통과하기만 한다면, 여러분의 에이전트는 안정적이고 반복 가능한 성능을 보여줄 것입니다.** (20:32~20:52)

> **단지 하나의 필드 수집에 문제가 있다는 것을 알아내기 위해 수백 건의 엔드 투 엔드 에이전트 테스트 케이스를 실행하지는 않잖아요. 필드 수준 평가와 유닛 테스트 수준에서 평가를 진행합니다.** (20:52~21:12)

## 논점은 해상도다

**E2E 테스트는 통과/실패를 주고 어디가 깨졌는지 주지 않는다.** 그리고 필드가 여러 개면 하나의 실패가 전체를 실패로 만들어, **무엇을 고쳐야 할지 알려면 다시 사람이 들어가 봐야 한다.**

| | E2E 에이전트 테스트 | **필드 단위 유닛 테스트** |
|---|---|---|
| 신호 | 통과/실패 | **어느 필드가 왜** |
| 비용 | 통화 한 건 전체 | 필드 하나 |
| 회귀 감지 | 느림 | 빠름 |
| 무엇을 놓치나 | — | **필드 사이의 상호작용·대화 흐름** |

마지막 행이 중요하다 — 필드가 전부 통과해도 **대화가 어색하거나 순서가 틀릴 수 있다.** 소스는 이 한계를 다루지 않는다.

## 이 위키에서의 좌표

**[[skill-evals]]에 해상도의 축이 붙었다.**

| 질문 | 다루는 페이지 |
|---|---|
| **무엇을 재는가** (합격 기준) | [[all-or-nothing-accuracy]] — *100% 아니면 0* |
| **어떻게 세는가** (진짜 비용) | [[true-cost-to-perfect-answer]] |
| **어느 단위로 재는가** | **이 페이지** |

셋이 같은 문제의 다른 면이다. [[all-or-nothing-accuracy]]는 *80%는 쓸모없다* 고 말했는데, **80%가 왜 80%인지** 를 알려면 이 페이지의 해상도가 필요하다.

## 프롬프트 흔들기의 대안으로 제시된다

> 이런 사고방식이 **모든 것을 더 체계적으로 만들어준다**고 생각해요. **프롬프트를 잔뜩 넣고 매번 몇 글자씩 바꿔가면서 프롬프트를 조작하면 LLM이 마법처럼 지침에 맞춰 작동하고 이런 것들을 따르기 시작할 거라고 기대하는 대신에요.** (21:12~21:30)

> 사실 제가 말씀드렸듯이, **모델을 미세 조정하지 않고도 95~97%의 정확도를 달성하는 것을 보셨잖아요. 그 비결은 기본적으로 에이전트가 특정 시점에 수행하는 작업의 맥락을 에이전트가 겪고 있는 구체적인 상태로 나누는 데 있습니다.** (21:30~21:54)

**처방이 프롬프트도 파인튜닝도 아니라 구조다** — 작업을 상태로 쪼개고, 상태마다 필드를 정하고, 필드마다 테스트를 둔다. 이 위키의 [[context-engineering]]이 *무엇을 컨텍스트에 넣는가* 를 다뤘다면, 여기는 **컨텍스트를 흔드는 대신 작업을 쪼개라**는 반대 방향의 처방이다.

## ⚠️ 유보

- **필드 사이의 상호작용과 대화 흐름**을 어떻게 평가하는지 없다. 유닛 테스트만으로는 잡히지 않는 층이다.
- **골든 데이터를 어떻게 만드는지** 없다 — 필드별 정답 집합의 출처.
- **95~97%** 의 분모가 앞의 *30% → 95%* 와 같은지 불명.
- **오디오 입력의 변주**(억양·잡음·속도)를 유닛 테스트에 어떻게 넣는지 없다. 텍스트 필드만 테스트하면 [[transcription-brittleness]]가 잡히지 않는다.
- 사람 검토가 어디에 들어가는지 없다. → [[verification-bottleneck]]

## References

- [[tech-bridge-voice-agent-failure-modes]] — first-seen
- [[venky-b]] · [[plivo]]
- 관련: [[typed-field-collection]] · [[skill-evals]] · [[all-or-nothing-accuracy]] · [[true-cost-to-perfect-answer]] · [[test-harness-vs-test-authoring]] · [[context-engineering]] · [[verification-bottleneck]]
