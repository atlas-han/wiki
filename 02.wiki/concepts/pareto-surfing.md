---
title: "Pareto Surfing — 자기 최적화 파이프라인의 조건 넷과 단계 여섯"
type: concept
category: pattern
tags: [self-optimizing-pipelines, pareto-frontier, model-selection, cost, failure-surface, bounded-experiments, budget-enforcement, harness, hill-climbing, data-pipelines]
aliases: [Pareto surfing, Pareto serving, 파레토 서핑, hill climber, 자기 최적화 파이프라인, failure surface, codons, rigs]
related: [model-mixing-economics, self-harness, harness-as-platform, fixed-budget-alpha, verifiable-goals, deterministic-agent-pipeline, just-in-time-ontology, automatic-model-routing, system-1-model, action-reversibility]
first-seen: tech-bridge-just-in-time-ontology
sources: [tech-bridge-just-in-time-ontology]
created: 2026-10-18
updated: 2026-10-18
---

# Pareto Surfing

**작동하는 아키텍처를 기준선으로 잡고, 모델과 부품을 더 싸고 빠른 것으로 바꿔 가며 알려진 중간 결과와 비교하고, 성공 기준을 조여 비용·속도·정확도의 frontier를 밀어내는 일이다.** 사람이 아니라 hill climber 모델이 한다. [[hrishi-olickel|Hrishi Olickel]]([[southbridge|Southbridge]])이 [[tech-bridge-just-in-time-ontology]]에서 불렀다.

> *"We find an architecture that gives a solid result. We use it as a baseline. Then we swap models and some other parts for faster, cheaper options, compare against known intermediates, tighten the requirement for success each time, moving closer and closer to the ideal, and you just watch the frontier move."* (19:28~19:43)

⚠️ 표기: en-orig는 *"Pareto serving"*(01:00, 01:39)과 *"Pareto surfing"*(10:29), *"hill climbers or servers"*(10:09~10:11)를 섞는다. *"surf their way"*(07:21, 10:26)와 *"where the surfing happens"*(19:25~19:28)를 근거로 surfing으로 읽었다.

## 누가 하는가 — hill climber

모델의 세 역할 가운데 셋째다(→ [[model-mixing-economics]]). *"Models that can take a first one and self-optimize. Given the right knowledge, instructions, and an incredibly stable surface to stand on, they can try new things, vary budgets to limit cost exposure, debug quickly, take notes, surf their way, not just to the right solution, but the optimal one."*(10:11~10:27)

## 조건 넷

| # | 조건 | 발화 |
|---|---|---|
| 1 | stable deployment surface | 빠르게 바뀌는 에이전트 런타임(Claude Code·Pi) 위에 *"checkpointing, rollback, budget enforcement"*를 갖춘 일관된 로그·API 층(16:48~17:05). 화자는 자사 Hank Weave를 쓴다 → [[harness-as-platform]] |
| 2 | bounded experiments | *"You can't test unless you can control cost, time, and access as resources."*(17:20~17:25) → [[fixed-budget-alpha]] |
| 3 | know-how·methodology | 2년치 패턴·디버깅·프롬프팅을 *"very token efficiently"* 표현할 추상화 층(17:27~17:44) |
| 4 | **failure surface** (가장 중요) | *"Give me a place to stand, and I will move the earth."* *"we haven't met a problem or a constraint that we couldn't iterate ourselves to solving given a stable stack to build on and a failure surface to iterate against."*(17:46~18:02) → [[verifiable-goals]] |

*"The current best models are still only barely good at this, sparks of intelligence, so to speak."*(18:10~18:15)

## 단계 여섯

1. 명세와 분할 — 오하이오 사례: 약 800,000행 → 약 200,000 케이스 → *"typed questions"*(18:19~18:30)
2. failure surface 정하기 — 좋은 모델을 작은 조각에 돌리고 일부를 손으로 확인해 기준선. 그 밖에 자동 실패 시스템·스키마 검사. *"define a failure surface before you ever start."*(18:35~18:57)
3. minimal, bounded pilots로 아키텍처 시험(19:01~19:05)
4. 검사를 **rig**로 옮긴다 — *"code that runs between bounded work segments that we call codons"*(19:05~19:11) → [[deterministic-agent-pipeline]]
5. codon을 *"reused, looped independently, validated, and placed in sequence"*(19:13~19:17)
6. 프로덕션 배포, *"where they can slowly mature"*(19:20~19:24)

(4와 5의 경계는 위키의 판독이다. 화자는 *"six stages"*라고만 한다.)

*"Being able to break a complex problem into pieces means each piece can move its own to its own best position, as Adam Smith would say."*(19:44~19:52)

## 사례 — 오하이오 entity resolution (⚠️ 자기 보고)

에이전트(*"4A"*, ⚠️ 이름 미판독)가 [[openai-astra|Astra]], 뒤에는 Opus 위에서 10일 동안 아키텍처 십수 개를 시도했다. 실행 4,000회 이상, [[jev|Jev]] 호출 90,000회, 약 60억 토큰이 들었고 *"tried practically every model on the Pareto frontier"*(13:01~13:16)다. 결과는 미리 정한 예산 $800 안의 $795이고, 예상은 약 $10,000였다. 반복은 모두 *"a version controlled Hank. They were easy to revert, understand, debug, and critique."*(13:36~13:43) → [[action-reversibility]]

## 위키의 다른 페이지와

- [[self-harness]]: 하네스를 에이전트가 스스로 개선하는 루프다. 여기서는 개선 대상이 데이터 파이프라인의 모델 배치와 구조다.
- [[automatic-model-routing]]: 런타임에 요청마다 모델을 고른다. Pareto surfing은 설계 시점에 파이프라인 단계별 모델을 바꿔 보며 고정한다.
- [[fixed-budget-alpha]]: 예산을 고정해야 비교가 공정하다는 방법론이 여기서는 실험의 안전장치(*"vary budgets to limit cost exposure"*)다.
- [[just-in-time-ontology]]: 재사용되는 온톨로지가 다음 일의 기준선이 된다.

## ⚠️ 유보

- 근거는 화자 회사의 사례 하나이고 수치는 자기 보고다.
- Hank Weave·hank·codon·rig의 정확한 정의는 자막 밖에서 확인하지 않았다.
- *"sparks of intelligence"*: 화자도 현재 모델이 이 일을 *"barely"* 한다고 한다.

## References

- [[tech-bridge-just-in-time-ontology]] — first-seen
- [[hrishi-olickel]] · [[southbridge]]
- 관련: [[model-mixing-economics]] · [[self-harness]] · [[harness-as-platform]] · [[fixed-budget-alpha]] · [[verifiable-goals]] · [[deterministic-agent-pipeline]] · [[automatic-model-routing]] · [[action-reversibility]]
