---
title: W&B Weave
type: entity
category: tool
tags: [observability, tracing, evals, agents, weights-and-biases]
aliases: [Weave, weave, W&B Weave, 직조]
links:
  - https://wandb.ai/site/weave
sources: [tech-bridge-wandb-aria-self-improving-agent]
created: 2026-09-30
updated: 2026-09-30
---

# W&B Weave

[[weights-and-biases|Weights & Biases]]의 **에이전트 트레이싱·eval 관측 도구.** [[tech-bridge-wandb-aria-self-improving-agent]]에서 [[zubin-aysola|Zubin Aysola]]가 **프로덕션과 오프라인 트레이스를 같은 형식으로 남기는 층**으로 설명했다.

> *"weights and biases weave for agents which is basically in my opinion at least the best observability platform for both production and offline tracing of agents"* (01:53~02:01) — ⚠️ 자사 직원의 평가.

⚠️ ko 자막은 Weave를 **"직조"** 로 옮긴다(01:52 *"가중치와 편향이 있는 직조"*).

## 소스에서의 역할

- **같은 형식** — 프로덕션 팀이 *"logging the same things in the exact same format so that I can rip those production traces into our environments"*(02:16~02:21). 이 동일 형식이 [[production-trace-eval-flywheel]]과 [[research-production-agent-parity]]의 전제다.
- **eval 결과도 Weave로** — *"we'll see those evaluations get logged into Weave as they're running"*(04:14~04:15). 점수 화면은 *"our real scores straight from weave"*(12:17~12:18).
- **트레이스 안** — ARIA의 평가 실행에서 *"predict and score column"* 과 도구 호출 목록(15:48~15:51).
- **SDK 호출 `weave.log`** — ARIA 데모가 짚은 문제: *"we weren't calling weave.log, one of our SDK calls, properly in the sandbox"*(13:22~13:27). ⚠️ 설명란은 이를 "SDK 버그"라 부르지만 자막은 **호출하는 쪽의 문제**다.

## References

- [[tech-bridge-wandb-aria-self-improving-agent]] · [[weights-and-biases]] · [[wandb-aria]]
