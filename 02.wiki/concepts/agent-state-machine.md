---
title: "에이전트 상태 머신 (Agent State Machine) — 규칙은 전이로, 내용은 모델로"
type: concept
category: pattern
tags: [state-machine, determinism, control-flow, mega-prompt, observability, edge-evals, self-improvement, process-mining, agent-workflows, guardrails]
aliases: [agent state machine, 상태 머신 에이전트, state machine for agents, 명시적 상태 머신, explicit state machine, edge evals, 엣지 eval]
related: [workflow-vs-agent, hard-vs-soft-enforcement, context-rot, ai-slop, skill-self-improvement, production-trace-eval-flywheel, generator-evaluator-pattern, system-1-model, design-pattern-state, linear-vs-closed-loop-harness, hook-enforced-workflow]
first-seen: tech-bridge-goodbye-slop-state-machines
sources: [tech-bridge-goodbye-slop-state-machines]
created: 2026-10-09
updated: 2026-10-09
---

# 에이전트 상태 머신

**에이전트 워크플로의 제어 흐름을 프롬프트 텍스트가 아니라 명시적 상태 머신(상태 + 이벤트 → 다음 상태)으로 두고, 비결정론적인 일(내용 생성·질문·판단)만 모델에게 맡기는 설계.** 금지된 행동은 *전이가 없어서* 일어날 수 없고, 로그는 상태·이벤트로 구조화되며, 그 머신 자체가 트레이스·eval과 함께 **다른 에이전트가 개선안을 내는 대상**이 된다. [[david-khourshid|David Khourshid]]([[xstate|XState]]), [[tech-bridge-goodbye-slop-state-machines]].

> *"Given a state and given an event, you are expected to reach a next state."* (01:14~01:18) · *"determinism lives in the rules"* (05:27~05:29) · *"The state machine is how you could have the agent self-improve."* (17:18~17:23)

## 무엇을 어디에 두는가

| | 결정론 — 상태 머신 | 비결정론 — 모델 |
|---|---|---|
| 이메일 드래프터 예 | 보내기 전 초안 · 승인된 메일만 전송 · 수신자 창작 금지 | 본문 · 명확화 질문 · 피드백 루프의 초안들 |
| 강제 방식 | 전이의 유무(구성상) | 프롬프트·평가 |
| 출처 | 05:27~05:45 | 05:45~06:03 |

## 메가 프롬프트 대비 (06:06~07:49)

1. **제어 흐름이 텍스트에** — *"First do this, then do that"* 이 프롬프트와 **도구 설명**에 반복된다. *"you should never write tools like this where the tool is part of the control flow"*(06:41~06:47).
2. **단일 모델·시스템 프롬프트·설정** — 단계마다 다른 전략을 쓸 수 없다.
3. **증명·관찰 불가** — 추론을 켜도 어디서 실패했는지 가리킬 수 없다. *"you cannot draw arrows in paragraphs"*(11:39~11:42).
4. **규칙 희석** — *"the rules decay with context"*(07:23~07:26) → [[context-rot]]

## 이득

- **불가능성** — drafting·reviewing 상태에서 send로 가는 전이가 없으면 전송은 *"mathematically impossible"*(08:27~08:38). ⚠️ 모델 안에서의 보증 — 구현이 모델을 따른다는 전제.
- **구조화된 관측** — *"structured logs for what states you are in, what events happened"*(10:57~11:03).
- **eval의 세 층** — 단계 · 전체 결과 · ⭐ **전이(edge)**. 모든 단계 eval이 통과해도 경로가 번거로울 수 있다(12:29~12:43, 14:38~14:51).
- **공유 산출물** — *"modeling is not ceremony when it actually replaces confusion, both for you and for the agents"*(10:16~10:21).

## 최소 루프

```
state = initial
while not done(state):
    events = execute(effects)                 # LLM 호출 · 도구 호출 · 외부 비동기
    state, effects = machine(state, events)   # 결정론적 전이 함수
```

`machine` 은 XState·switch 문·reducer·LangGraph 무엇이든(15:36~15:54). (위키의 의사코드 — 발화 15:08~15:33)

## 자기 개선 루프 — model → observe → propose → compare (15:58~17:25)

머신 + 실제/시뮬레이션 사용자 트레이스 + 단계별·전체 eval을 **다른 에이전트**(*"Not the exact same agent"*)에게 넘겨 개선안을 받고(V2), 같은 시나리오를 V1·V2에 돌려 비교한다. 데모의 V2는 *"draft the email first and then figure out what's needed after"*(14:06~14:11). 선행: Agent Spec · AIFlow · **process mining**(이벤트 트레이스 → 형식 모델 → 최적화 지점, 16:53~17:12).

## 런타임의 확률적 선택자

Jev 데모: 상태 머신 + 가능한 이벤트 전부를 [[jev|Jev]]에 주고, Jev가 **허용된 다음 이벤트를 확률과 함께 고른다**(18:54~19:57) — 결정론적 그래프 위의 [[system-1-model|System 1]] 선택. 고장 주입 시 수리 이벤트를 먼저 골랐다. ⚠️ 1회 시연.

## 위키에서의 좌표

- **[[design-pattern-state]]** — GoF State 패턴은 객체 내부의 상태별 행동 분기. 이 개념은 같은 아이디어를 **에이전트 워크플로 단위**로 올리고, 전이 그래프를 사람·에이전트가 읽고 고치는 **산출물**로 다룬다.
- **[[hard-vs-soft-enforcement]]** — 프롬프트 규칙(소프트) → 전이 부재(하드). [[hook-enforced-workflow]]가 훅으로 하는 일을 그래프 구조로.
- **[[workflow-vs-agent]]** — ⚠️ Contradiction: *"Loops are graphs"*(02:52). 런타임엔 워크플로, 버전 사이엔 에이전트가 경로를 바꾼다.
- **[[linear-vs-closed-loop-harness]]** — 최소 루프는 결정론적 전이 함수를 감싼 폐루프.
- **[[skill-self-improvement]] · [[production-trace-eval-flywheel]]** — 트레이스 → 개선. 대상이 스킬·eval 세트가 아니라 **그래프**.
- **[[ai-slop]]** — 슬롭 = *"unstructured delegation"*(03:31~03:32)의 처방.

## ⚠️ 유보

- **실측 없음** — V1→V2, Stately 내부 적용, Jev 데모 모두 1회 시연·체감.
- **언제 모델링할 가치가 있는가**의 기준은 *"where it applies"*(10:43~10:46)뿐.
- 2023(*가드레일*) vs 2026(*자기 개선*) — 대체가 아니라 층이 다르다(런타임 vs 개선 루프). 위키의 독해.
- Agent Spec·AIFlow·process mining — 미확인.

## References

- [[tech-bridge-goodbye-slop-state-machines]] — first-seen
- [[david-khourshid]] · [[xstate]] · [[jev]] · [[langchain]]
- 관련: [[design-pattern-state]] · [[hard-vs-soft-enforcement]] · [[context-rot]] · [[workflow-vs-agent]] · [[skill-self-improvement]] · [[production-trace-eval-flywheel]] · [[generator-evaluator-pattern]] · [[system-1-model]] · [[ai-slop]]
