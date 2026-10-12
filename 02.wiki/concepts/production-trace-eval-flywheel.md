---
title: 프로덕션 트레이스 → eval 태스크 플라이휠 (Production Trace Eval Flywheel)
type: concept
category: pattern
tags: [evals, production-traces, regression-tasks, hill-climbing, observability, self-improvement, flywheel]
aliases: [eval flywheel, eval 플라이휠, 평가 플라이휠, production traces to eval tasks, 프로덕션 트레이스를 평가 태스크로]
related: [research-production-agent-parity, yaml-agent-eval-pipeline, self-harness, skill-evals, generator-evaluator-pattern, verifiable-goals, automated-ai-research, field-level-unit-test-evals, agent-state-machine, eval-platform-maturity-stages, taste-encoded-evals, trace-to-memory-loop]
first-seen: tech-bridge-wandb-aria-self-improving-agent
sources: [tech-bridge-wandb-aria-self-improving-agent, tech-bridge-goodbye-slop-state-machines, tech-bridge-braintrust-eval-platform-systems-problem, tech-bridge-langchain-learning-agent-memory]
created: 2026-09-30
updated: 2026-10-12
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

## 트레이스가 eval 태스크가 아니라 그래프 변경이 될 때 (2026-10-09 · [[tech-bridge-goodbye-slop-state-machines]])

[[david-khourshid|David Khourshid]]의 루프 *model → observe → propose → compare* 도 트레이스를 연료로 쓰지만 산출물이 다르다 — 회귀 태스크가 아니라 **상태 머신 V2**. 그리고 eval이 모두 통과해도 남는 칸을 짚는다: *"all of your evals could pass uh with the first machine, but unless you're dog fooding (…) you're not going to get the optimal results"*(14:38~14:51) → eval의 세 번째 대상 *"evaling the edges"*(12:29~12:31). 화자는 이 계보를 **process mining**(*"about 20 years older"*, 16:53~17:12 — ⚠️ 미확인)에 잇는다. → [[agent-state-machine]]

## 두 번째 벤더, 같은 칸 — 사람이 배포를 결정한다 (2026-10-12 · [[tech-bridge-braintrust-eval-platform-systems-problem]])

[[braintrust|Braintrust]] 발표(설명란 기준 [[hossein-niazmandi|Hossein Niazmandi]])가 같은 루프를 *"the North Star for many teams"* 로 그린다: *"I can observe the failure modes that happen based on dimensions that I define. I want to be able to grab those failure modes and create test cases so that I can iterate offline. So, I can improve my agent quality without introducing new regressions."*(06:12~06:31), 반복의 이유는 *"just like in classical ML, drift becomes a real thing"*(06:31~06:36). W&B와 다른 점 셋:

1. **실패만 말한다** — 루프의 입력은 *failure modes* 와 *"scenarios where your users had poor interactions"*(10:24~10:31). W&B의 *"every production goodness as well"* 은 없다.
2. **루프를 도는 것은 사용자의 코딩 에이전트** — *"tell your coding agent of choice, "Find me all traces in the last 24 hours where the user had a poor experience. Run the evals for me.""*(13:59~14:10). W&B ARIA처럼 *자사 에이전트가 스스로* 가 아니라 headless 플랫폼을 외부 에이전트가 쓴다.
3. ⭐ **마지막 칸이 사람** — *"the human's responsibility is to review the outcome. If I have different iterations of these e-vals that are run by my coding agent, I can look at the outcome and make the decision of which version of it is the best for what I want to ship to production."*(16:05~16:23). 위 "⚠️ 유보"의 *작성자 = 검증자* 빈자리에 대한 한 답 — 단 측정·사례 없음.

그리고 루프 아래의 인프라를 처음 문제 삼는다 — 트레이스는 *"semi-structured JSON"*, 상호작용당 *"hundreds of megabytes"*, 실시간 쿼리와 장기 쿼리라는 *"Two different workloads"*(11:13~12:25). → [[eval-platform-maturity-stages]]

> ⚠️ **용어**: Niazmandi는 evals = *프로덕션 전*, observability = *프로덕션 중* 으로 나눈다(00:22~01:14). 이 페이지의 루프는 그 둘을 잇는 것이고, W&B는 프로덕션 트레이스를 곧장 eval 태스크로 부른다 — 이름의 경계가 다를 뿐 주장 충돌은 아니다.
> ⚠️ **화자 안의 긴장**: 같은 발표에서 *"You create the dimensions of failure and success because you know the outcomes"*(10:17~10:22)와 *"Rather than you having to think about these dimensions (…) Braintrust can surface these insights automatically"*(14:52~15:02). 후자는 자사 기능 피치.

## 트레이스의 세 갈래 — eval은 그중 하나 (2026-10-12 · [[tech-bridge-langchain-learning-agent-memory]])

[[jake-broekhuizen|Broekhuizen]]([[langchain|LangChain]]): *"most trace data actually should stay as history, as referenceable history. Some some might become data sets to do offline evaluations (…) A small (…) subset should end up becoming what changes your agent's memory."*(12:57~13:13). 이 페이지의 순환(트레이스 → eval 태스크)은 **세 갈래(history · eval 데이터셋 · 메모리 갱신) 중 하나**로 놓인다. 메모리 갱신 갈래는 [[trace-to-memory-loop]], 중요한 행동은 다시 eval로 보호한다(*"protecting important behavior with emails[=evals]"* 14:50~14:52). ⚠️ 벤더 진술, 비율·기준 미발화.
