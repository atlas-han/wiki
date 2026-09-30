---
title: 연구·프로덕션 에이전트 동일성 (Research–Production Agent Parity)
type: concept
category: pattern
tags: [evals, sim-to-real, drift, agent-harness, observability, benchmarking]
aliases: [byte-wise identical agent, 바이트 단위 동일 에이전트, research production parity, 벤치마크·eval·에이전트의 공변성, covariance of benchmarks evals and agents, sim-to-real gap]
related: [production-trace-eval-flywheel, yaml-agent-eval-pipeline, self-harness, harness-engineering, agent-harness-design, skill-evals]
first-seen: tech-bridge-wandb-aria-self-improving-agent
sources: [tech-bridge-wandb-aria-self-improving-agent]
created: 2026-09-30
updated: 2026-09-30
---

# 연구·프로덕션 에이전트 동일성

**오프라인에서 벤치마크하는 에이전트와 프로덕션에 배포된 에이전트를 코드 수준에서 같게 유지해, 오프라인 점수가 프로덕션 행동을 말해 주게 만드는 설계 원칙.** 동기는 *벤치마크·eval·에이전트·구성이 서로 공변한다* 는 관찰이다. [[zubin-aysola|Zubin Aysola]]([[weights-and-biases|Weights & Biases]])가 [[tech-bridge-wandb-aria-self-improving-agent]]에서.

> *"we benchmark a bite-wise[=byte-wise] identical version of the agent in our production environment and our simulated environment"* (05:27~05:33)

## 문제 — 공변성

> *"benchmarks, evaluations, the agents, and how you configure them are all covariant. And so like if you're trying to apply principled evaluations to any sort of system that dynamically changes, you need to have good measurement to see how the system actually performs and you really want to see how the system performs in both your production environment and your offline environment"* (01:21~01:38)

넷 중 하나가 바뀌면 나머지의 뜻이 바뀐다 — 에이전트를 고치면 벤치마크가 재는 것이 달라지고, 태스크를 고치면 같은 점수가 다른 에이전트를 가리킨다. 화자는 이를 RL의 **sim-to-real gap**에 빗댄다(*"sim tore gap"* 01:40~01:42). 그리고 에이전트를 어떻게 포장하느냐(도구 호출 방식 등)에 따라 벤치마크 결과가 크게 달라진다는 관찰(00:48~00:54)이 **자체 하네스를 만든 이유**로 제시된다.

## 해법 — 세 겹의 동일성

| 겹 | 무엇 | en-orig |
|---|---|---|
| **코드** | *"our research and production code are exactly the same"* | 05:44~05:46 |
| **동기화** | ⭐ *"there's like a 4-hour sync job that happens between production to our research environment so that we don't get any drift when you, you know, researchers are cutting new variants of the agent, new skills, etc."* | 05:47~05:54 |
| **로그 형식** | [[wandb-weave|Weave]]로 프로덕션·오프라인을 *"the exact same format"* 으로 | 02:16~02:18 |
| **실행** | eval DAG의 실행 단계도 *"in the bite-wise identical version that you have in production"* | 09:17~09:19 |

결과는 *"this nice little tight loop that basically mirror each other on two sides of the stack from our deployment layer and our offline benchmarking layer"*(05:56~06:02).

⚠️ **"100% 동일"은 설명란의 말이다.** 자막의 동일성은 **4시간 주기 동기화**로 유지된다 — 연구 쪽은 프로덕션의 **주기적 복제본**이다. 무엇이(코드·스킬·구성·데이터) 어느 방향으로 동기화되는지는 말하지 않는다.

## 드리프트는 두 군데서 난다

1. **에이전트 드리프트** — 연구자가 변형·스킬을 만들며 프로덕션에서 멀어지는 것 → 동기화 잡이 막는다.
2. **eval 드리프트** — 태스크 세트가 실제 사용에서 멀어지는 것. 동료가 하루를 *"thinking about the health of our evaluations and the drift between our evaluations and production"*(09:43~09:47)에 썼다. → [[production-trace-eval-flywheel]]이 프로덕션 트레이스를 계속 태스크로 넣어 이쪽을 막는다.

## 이 위키에서의 좌표

- [[self-harness]] — 논문은 모델 $M$과 평가자 $\mathcal{E}$를 **고정**한다. 공변성 논증은 그 고정이 **실무에선 가정**임을 짚는다 — 평가자(태스크 세트)도 움직이니, 적어도 에이전트 쪽은 두 환경에서 같게 묶는다.
- [[skill-evals]] — [[impeccable|Impeccable]]의 eval 하네스가 Claude Code·Codex의 **조건과 도구를 재현**한 것(09-28)과 같은 문제의식. 그쪽은 **남의 하네스를 흉내**, 여기는 **자기 프로덕션 코드를 그대로** 쓴다.
- [[harness-engineering]] · [[agent-harness-design]] — 하네스가 곧 측정 대상이라는 관점.

## ⚠️ 유보

- 수치 없음 — 동일성을 지키기 전후 오프라인 점수와 프로덕션 성과의 상관이 얼마나 좋아졌는지 말하지 않는다.
- 환경(데이터·외부 서비스)의 동일성은 다른 문제다 — 화자는 환경 준비가 비싸고 일부 런타임 구성은 YAML로 못 담아 **hot patch** 한다고 한다(09:06~09:13). 코드는 같아도 **환경은 근사**다. → [[yaml-agent-eval-pipeline]]
- 당사자 진술.

## References

- [[tech-bridge-wandb-aria-self-improving-agent]] (first-seen) · [[zubin-aysola]] · [[wandb-aria]] · [[wandb-weave]]
- 관련: [[production-trace-eval-flywheel]] · [[yaml-agent-eval-pipeline]] · [[self-harness]]
