---
title: "출시 차단 eval 문턱 (Launch-Blocking Evals) — 이상적 행동 목록을 행 단위로 판정하고, 빨강이 남으면 출시하지 않는다"
type: concept
category: pattern
tags: [evals, launch, release-gate, behavior-evals, capability-evals, personal-agent, muse]
aliases: [launch blocking threshold, 출시 문턱, 행동별 eval]
related: [taste-encoded-evals, eval-platform-maturity-stages, production-trace-eval-flywheel, skill-evals, verifiable-goals, agent-trust-curve]
first-seen: tech-bridge-alexandr-wang-muse-launch
sources: [tech-bridge-alexandr-wang-muse-launch]
created: 2026-10-16
updated: 2026-10-16
---

# 출시 차단 eval 문턱

**제품에 필요한 구체적 행동·능력을 목록으로 만들고, 각 행동을 eval 행으로 판정한 뒤, 문턱을 넘지 못한 행이 남아 있으면 출시를 막는 방식.** [[alexandr-wang|Alexandr Wang]]이 [[muse|Muse]] 출시 과정을 설명하며 쓴 말에서 가져왔다([[tech-bridge-alexandr-wang-muse-launch]]).

> *"specific behaviors and capabilities that we knew the model needed to have to be able to build the ideal personal agent. Like it was very, very meticulous."* (04:12~04:21)
>
> *"Threshold is launch blocking above what threshold is good. We had many checkpoints that like were like green on 80 of the rows but red on 20 of the rows. We knew that wasn't good enough."* (05:11~05:36)

## 구조 (원음에서 확인되는 것만)

1. **목록이 먼저다.** 이상적인 개인 에이전트에 *필요하다고 알고 있던* 행동·능력을 정한다.
2. **행 단위 판정.** 체크포인트마다 행별로 초록/빨강이 나온다.
3. **평균이 아니라 빨강으로 막는다.** 80%가 초록이어도 빨강 20%가 남으면 *"wasn't good enough"*. 문턱은 *"launch blocking"* 이다.

해설은 여기에 **직접 써 본 감각**을 더한다(*"after the evaluation charts turned green, he felt it had improved through his own use. The decision to launch was based on both behavior-based evaluation and personal experience"* 05:36~05:52, 해설). ⚠️ 이 부분은 원음이 아니다.

## 이 위키의 다른 eval 절차와

- [[taste-encoded-evals]]: eval 위에 사람의 판단을 한 겹 더 두는 구조는 같다. 다만 그쪽은 **취향을 eval로 옮기는 절차**이고, 이 페이지는 **출시 게이트**다.
- [[eval-platform-maturity-stages]] · [[production-trace-eval-flywheel]]: 그쪽은 출시 **후** 트레이스로 eval을 키운다. 이 페이지는 출시 **전** 차단이다.
- [[verifiable-goals]] · [[reward-hacking]]: 행 단위 통과/실패 게이트도 지표가 될 수 있다. 소스는 게이밍을 논하지 않는다.

## ⚠️ 유보

- 80/20의 단위(퍼센트인지 행 수인지), 행의 수, 행 하나의 판정 방법(자동 grader인지 사람인지), 최종 출시 시점의 점수가 **모두 미발화**다.
- ko 트랙에만 *"and then over time we buil evs for all those…"* 라는 영어 조각이 있다(04:22~04:28). en-orig에 없어서 근거로 쓰지 않는다.
- 근거가 원음 두 구간(합쳐 약 40초)뿐이다.

## References

- [[tech-bridge-alexandr-wang-muse-launch]] · [[alexandr-wang]] · [[muse]] · [[taste-encoded-evals]]
