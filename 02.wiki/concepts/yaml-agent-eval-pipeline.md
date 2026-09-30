---
title: YAML 기반 에이전트 eval 파이프라인 (YAML Agent Eval Pipeline)
type: concept
category: pattern
tags: [evals, yaml, variants, simulation, user-simulation, scoring, pairwise, parallelism, agent-harness]
aliases: [eval DAG, eval pipeline, 평가 파이프라인, YAML variants, YAML 변형, normative vs relative scoring, 절대 평가와 상대 평가, 규범적 채점, 상대적 채점]
related: [production-trace-eval-flywheel, research-production-agent-parity, skill-evals, generator-evaluator-pattern, verifiable-goals, harness-engineering, field-level-unit-test-evals]
first-seen: tech-bridge-wandb-aria-self-improving-agent
sources: [tech-bridge-wandb-aria-self-improving-agent]
created: 2026-09-30
updated: 2026-09-30
---

# YAML 기반 에이전트 eval 파이프라인

**에이전트 구성과 eval 태스크를 모두 YAML로 선언하고, ML 학습 파이프라인 같은 DAG(구성 → hydrate → 환경 → rehydrate → 실행 → 채점 → teardown)로 많은 변형을 병렬로 돌리는 오프라인 평가 방식.** [[zubin-aysola|Zubin Aysola]]([[weights-and-biases|Weights & Biases]])가 [[wandb-aria|ARIA]]의 오프라인 벤치마킹(WBAF, *"weights and biases agent factory"* 13:15~13:19)으로 [[tech-bridge-wandb-aria-self-improving-agent]]에서 설명했다.

> *"if we take an adage from old reinforcement learning training or just simple model training, it's just better to run more experiments than fewer. Um and so that's the thesis behind the agent harness itself too."* (07:34~07:44)

## 1. 변형은 YAML 한 장

하네스는 모델 중립이다 — *"relatively agnostic software stack for how we treat compaction and how we prepare context and how we assemble UI payloads"*(07:10~07:15). 그 위에서:

> *"make it very very simple to have lots of mutations of the exact same configuration. You want to basically YAML define different configurations of the agent to sort of get multiple parallel uh variants and then test them all and see what happens"* (07:20~07:31)

변형 = 모델·프롬프트·스킬 등 구성의 차이. 프로덕션 변형(prod)과 후보 변형(candidate)을 같은 태스크에 돌려 비교한다(04:06~04:11, 13:45~13:48). → [[harness-engineering]]

## 2. DAG (08:37~10:30)

*"a relatively agnostic DAG that you might think about in a traditional machine learning context"*(08:38~08:42):

| 단계 | 내용 | en-orig |
|---|---|---|
| 구성 | YAML 파일 | 08:42~08:46 |
| **hydrate** | *"we load the live data that we need to"* | 08:46~08:49 |
| 환경 준비 | 비싸다 — 프로덕션 데이터, *"full machine learning training logs"*, GPU 실행 시뮬레이션 → **병렬화** | 08:49~09:04 |
| **rehydrate** | *"runtime configurations that you can't encode in a YAML specification and so you hot patch that data back into the config"* | 09:06~09:13 |
| 실행 | *"running the agent is trivial"* — 프로덕션과 byte-wise 동일 버전 | 09:13~09:21 → [[research-production-agent-parity]] |
| **채점** | *"scoring is where I spend a lot of my time"* | 09:21~09:25 |
| teardown | *"you don't want to clobber your teammates's work"* | 10:17~10:22 |

**hydrate/rehydrate의 두 단계**가 이 설계의 특징이다 — 선언(YAML)만으로 재현할 수 없는 런타임 상태를 **명시적 단계**로 분리했다. ⚠️ ko는 rehydrate를 **"수분 보충"** 으로 옮겼다.

## 3. 채점 — 규범적 + 상대적

> *"Arya scores itself in two patterns which is normatively which gives us basically did we pass a task or not and then relativistically where we can set styles based on one variant where it asks questions to the user and one variant where it doesn't ask questions to the user and we can sort of see which one behaves better uh with a relative scoring"* (09:58~10:13)

| 방식 | 묻는 것 | 쓰임 |
|---|---|---|
| **규범적(normative)** | 태스크를 통과했나 | 절대 기준, 회귀 |
| **상대적(relativistic)** | 두 변형 중 어느 쪽이 더 낫나 | **행동 스타일** 비교 — 예: 사용자에게 되묻는 변형 vs 안 묻는 변형 |

화자는 이를 *"a pretty traditional formulation from a reinforcement learning standpoint"*(10:13~10:16)라 한다. 상대 비교가 **정답이 없는 스타일 선택**(되물을 것인가)에 쓰인다는 점이 요점이다 — 통과/실패로는 못 가르는 축. ⚠️ 상대 채점을 누가(LLM judge·사람·규칙) 하는지는 말하지 않는다. → [[generator-evaluator-pattern]]

## 4. 태스크 — 시작 조건과 종료 조건

- *"YAML specifications that we define as a starting condition of an environment with a bunch of user configurations as well as then an ending condition that we sort of want to get to"*(10:35~10:42) → [[verifiable-goals]]
- *"tasks are flows from users"*(10:42~10:45). 시뮬레이션: ① 단순 텍스트 지시 ② **페르소나 사용자 LLM** — *"hey, pretend to be this user, ask certain questions in a particular order so that we can simulate multi-turn environments"*(11:21~11:25). ⚠️ *"three ways"*(10:45~10:47)라 했지만 셋째는 자막에 없다.
- ⭐ **886개, 레벨별**(11:28~11:30), **제품팀 검토** — *"so that they can decide whether or not the tasks are good enough or they reflect things that we care about from our benchmarks"*(11:30~11:36). 그리고 *"we just run them a bunch of times"*(11:38~11:39).
- 새 태스크의 원천은 프로덕션 트레이스다 → [[production-trace-eval-flywheel]]

## 이 위키에서의 좌표

- [[skill-evals]] — [[impeccable|Impeccable]](09-28)의 **행렬**(니치 × 모델 × 릴리스당 5~10회)과 **사용자 역 LLM**이 여기의 변형 × 태스크 × 반복, 페르소나 사용자와 짝을 이룬다. 차이: Impeccable은 줄 단위 ablation, 여기는 **구성 전체의 변형**.
- [[field-level-unit-test-evals]] — 해상도 축에서 보면 여기의 규범 채점은 **태스크 단위 통과/실패**다.
- [[verifiable-goals]] — 종료 조건이 곧 검증 기준.

## ⚠️ 유보

- 채점기의 정체(규칙·LLM judge·사람) 미상. 상대 채점의 편향 처리 없음.
- 레벨 기준, 세 번째 시뮬레이션 방식, 반복 횟수 없음.
- 샌드박스는 *"unconstrained"*(08:21) — 병렬 teardown 외의 격리·비용 통제 이야기 없음.
- 당사자 진술. 슬라이드 문구는 화자도 *"I'm not really sure what the six phrases per record uh means"*(08:27~08:31)라 할 만큼 AI가 쓴 것이다.

## References

- [[tech-bridge-wandb-aria-self-improving-agent]] (first-seen) · [[zubin-aysola]] · [[wandb-aria]]
- 관련: [[production-trace-eval-flywheel]] · [[research-production-agent-parity]] · [[skill-evals]] · [[generator-evaluator-pattern]]
