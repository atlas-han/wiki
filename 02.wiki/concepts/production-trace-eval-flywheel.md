---
title: 프로덕션 트레이스 → eval 태스크 플라이휠 (Production Trace Eval Flywheel)
type: concept
category: pattern
tags: [evals, production-traces, regression-tasks, hill-climbing, observability, self-improvement, flywheel]
aliases: [eval flywheel, eval 플라이휠, 평가 플라이휠, production traces to eval tasks, 프로덕션 트레이스를 평가 태스크로]
related: [research-production-agent-parity, yaml-agent-eval-pipeline, self-harness, skill-evals, generator-evaluator-pattern, verifiable-goals, automated-ai-research, field-level-unit-test-evals]
first-seen: tech-bridge-wandb-aria-self-improving-agent
sources: [tech-bridge-wandb-aria-self-improving-agent]
created: 2026-09-30
updated: 2026-09-30
---

# 프로덕션 트레이스 → eval 태스크 플라이휠

**배포된 에이전트의 실행 트레이스를 오프라인 eval 태스크로 옮기고, 그 태스크 위에서 후보 변형을 hill climb한 뒤 다시 배포하는 순환. 프로덕션의 실패뿐 아니라 성공도 태스크가 된다.** [[zubin-aysola|Zubin Aysola]]([[weights-and-biases|Weights & Biases]])가 [[tech-bridge-wandb-aria-self-improving-agent]]에서 ARIA 개발 방식으로 제시했다.

> *"that's the eval flywheel. So you know fundamentally every production miss or every production goodness as well because I think it's useful to hill climb in a positive direction uh becomes a task for our agent framework. And so we use that to sort of define the agent and make it better."* (12:02~12:14)

⚠️ ko 자막은 이 문장을 *"평가 양식 … 확장성이 유용하다고 … 우리 프레임워크의 과제 자치령 대표"* 로 무너뜨렸다 — flywheel·hill climb·agent가 모두 사라진다.

## 순환의 칸

| 칸 | 무엇 | en-orig |
|---|---|---|
| ① **같은 형식으로 기록** | 프로덕션 팀과 오프라인 팀이 [[wandb-weave|Weave]]에 *"the same things in the exact same format"* | 02:16~02:18 |
| ② **트레이스를 가져오기** | *"rip those production traces into our environments"* — 프로덕션 트레이스를 시뮬레이션 환경으로 | 02:19~02:21 |
| ③ **태스크로 만들기** | 트레이스를 **회귀 태스크**로 — 데모에서 *"turned it into a WBAF regression task"*, *"It replicates the source trace"* | 13:10~13:15, 13:27~13:29 |
| ④ **hill climb** | *"hill climb on them or resolve our errors"*, 후보 변형과 프로덕션 변형을 같은 태스크에 | 02:21~02:23, 04:06~04:11 |
| ⑤ **다시 배포** | *"deploy new versions of the agent uh, and work with my team to do that"* | 04:27~04:31 |

그리고 ① 앞에 **대량 생성**이 있다 — *"generate a ton of traces and then decide what you're going to do with said ton of traces"*(06:28~06:33), 프로덕션 트래픽과 오프라인 양쪽의 궤적에서 *"exploit the behavior patterns from both of those"*(11:44~11:52).

## 무엇이 새로운가

1. **성공도 태스크가 된다** — *"every production goodness as well"*. 실패 회귀만 막는 게 아니라 **잘한 행동을 고정·강화**하는 방향으로도 오른다. 이 위키의 eval 페이지들([[skill-evals]] · [[field-level-unit-test-evals]])은 대체로 **실패 → 테스트** 방향이었다.
2. **순환을 에이전트가 돈다** — *"the thing that we use to now build itself because it's sophisticated enough that it can actually do that offline hill climbing uh by itself"*(02:29~02:35). 데모에서 ARIA는 트레이스로 *"wrote itself a new task, ran it, and then scored it"*(13:00~13:02), 원인(샌드박스에서 `weave.log`를 제대로 호출하지 않음)을 짚고 **짧은 프롬프트를 시스템 프롬프트나 스킬에 넣은 후보 변형**을 만들었다(15:55~16:02). → [[self-harness]]
3. **전제는 형식의 동일성** — 트레이스가 오프라인으로 그대로 옮겨지려면 두 환경이 같은 에이전트, 같은 로그 형식이어야 한다. → [[research-production-agent-parity]]

## 이 위키에서의 좌표

- [[self-harness]] — 논문의 루프(트레이스에서 약점 발견 → bounded edit → 회귀 테스트로 채택)와 **칸이 거의 같다.** 차이: 입력이 **실사용자 프로덕션 트레이스**이고, 채택은 사람 팀이 한다.
- [[skill-evals]] — Lauren Tan의 *실패 → 테스트 → 스킬 수정*(09-12)을 **조직 규모의 파이프라인**으로 키운 형태. 태스크 886개는 **제품팀이 검토**한다(11:30~11:36).
- [[yaml-agent-eval-pipeline]] — 옮겨진 태스크가 돌아가는 기계.
- [[verifiable-goals]] — 태스크 = *시작 조건 + 종료 조건*(10:33~10:42).

## ⚠️ 유보

- **작성자 = 검증자.** 데모에서 태스크를 쓰고, 돌리고, 채점한 것이 모두 ARIA다(13:00~13:02). ARIA가 쓴 태스크가 제품팀 검토를 거치는지는 말하지 않는다 — [[skill-evals]]가 표시해 온 빈자리의 반복.
- **효과 수치 없음.** 플라이휠이 점수를 얼마나 올렸는지, 데모의 후보가 prod를 이겼는지(13:45~13:48) 화면에만 있다.
- **프라이버시.** 프로덕션 화면은 *"a sanitized view of internal customer traces or internal traces"*(03:27~03:31)라고만 한다. 고객 트레이스를 eval 태스크로 옮길 때의 비식별화 절차는 없다.
- **당사자 진술** — Weave를 파는 회사의 발표다.

## References

- [[tech-bridge-wandb-aria-self-improving-agent]] (first-seen) · [[zubin-aysola]] · [[wandb-aria]] · [[wandb-weave]]
- 관련: [[research-production-agent-parity]] · [[yaml-agent-eval-pipeline]] · [[self-harness]] · [[skill-evals]]
