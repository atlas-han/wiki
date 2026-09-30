---
title: ARIA (Weights & Biases 에이전트)
type: entity
category: product
tags: [agent, research-agent, self-improvement, evals, weights-and-biases]
aliases: [ARIA, Arya, 아리아, W&B ARIA, coreweave Arya]
links:
  - https://wandb.ai
sources: [tech-bridge-wandb-aria-self-improving-agent]
created: 2026-09-30
updated: 2026-09-30
---

# ARIA (Weights & Biases 에이전트)

**[[weights-and-biases|Weights & Biases]] 플랫폼 안에서 사용자를 대신해 연구(학습 실행·분석·리포트)를 하는 에이전트 — 그리고 자기 자신의 오프라인 eval 루프를 돌려 스스로를 개선하는 데 쓰이는 에이전트.** [[zubin-aysola|Zubin Aysola]]의 [[tech-bridge-wandb-aria-self-improving-agent]]로 이 위키에 들어왔다.

> ⚠️ **이름.** 자막은 전부 *"Arya"*(ko *"아리아"*), 설명란은 **"ARIA"**. 약어 풀이는 어디에도 없다. 출시: *"something that we released to general availability on Monday"*(00:07~00:11) — 어느 월요일인지 미확정.

## 무엇인가

- *"we're doing some work at Weights and Biases to build our own agent harness to do research for you in the Weights and Bices platform"*(00:56~01:00) — 자체 하네스.
- 모델 중립: CoreWeave 추론 모델과 파운데이션 모델 회사들의 모델을 모두 시험(07:00~07:07). → [[yaml-agent-eval-pipeline]]
- 샌드박스에서 무엇이든 — 발표 준비 중 ARIA가 **자기 병렬 실행용 샌드박스를 스스로 만들었다**(08:03~08:18).
- 다른 데모: *"training machine learning models on H200s running on Corey[=CoreWeave] infrastructure and doing auto research for Karpathy's nanohat[=nanochat]"*(14:59~15:05). → [[automated-ai-research]]

## 자기 개선 — "Arya Researches Arya"

*"the thing that we use to now build itself because it's sophisticated enough that it can actually do that offline hill climbing uh by itself"*(02:29~02:35). 데모에서 ARIA는:

1. 프로덕션 트레이스로 *"wrote itself a new task, ran it, and then scored it"*(13:00~13:02)
2. *"we weren't calling weave.log (…) properly in the sandbox"* 라는 원인을 짚고(13:22~13:27)
3. 시스템 프롬프트나 스킬에 짧은 프롬프트를 넣은 **후보 변형**을 만들어 prod 변형과 비교했다(15:55~16:02)

⚠️ 후보가 이겼는지·배포됐는지는 화면에만 있다 — **"스스로 해결"은 자막으로 확인되지 않는다.** 야간 CI가 깨졌을 때 *"we had Arya have to fix itself last night"*(04:46~04:47)라는 말도 있다. → [[self-harness]] · [[production-trace-eval-flywheel]]

## 수치 (자막)

- eval 태스크 **886개**, 레벨별 분류(11:28~11:30)
- *"about like 66% performance on some of the tasks"*(04:49~04:50) — ⚠️ 분모 미상
- 7주치 야간 CI(04:34~04:37)

## References

- [[tech-bridge-wandb-aria-self-improving-agent]] · [[weights-and-biases]] · [[wandb-weave]] · [[zubin-aysola]]
