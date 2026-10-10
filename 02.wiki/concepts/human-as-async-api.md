---
title: "인간은 비동기 API (Human as an Async API)"
type: concept
category: pattern
tags: [human-in-the-loop, async, durable-execution, wait-condition, signal, approval, agents, alert-fatigue]
aliases: [human is an async API, 인간은 비동기 API, 사람을 비동기 API로, wait condition + signal, durable human-in-the-loop]
related: [durable-execution, agent-distributed-systems, risk-proportional-human-review, no-silent-write, human-plumbing, agent-harness-design, action-reversibility, model-calibration, agent-trust-curve]
first-seen: tech-bridge-human-is-async-api
sources: [tech-bridge-human-is-async-api]
created: 2026-10-10
updated: 2026-10-10
---

# 인간은 비동기 API (Human as an Async API)

**에이전트가 사람의 입력(승인·수정·답변)을 기다리는 일을 동기 함수 호출이 아니라 비동기 이벤트로 설계하라는 패턴.** 워크플로를 *wait condition* 으로 멈춰(park) 두고, 사람의 응답은 언제든 *signal* 로 주입하며, 그 대기 상태는 [[durable-execution|durable]] 층에 저장돼 프로세스가 죽어도 살아남는다. [[temporal|Temporal]] 직원의 발표 [[tech-bridge-human-is-async-api]]의 제목이자 테제.

> *"the human is an async API"* (03:22~03:24) · *"the human granted, you know, we're not tools, but we are a tool to the agent."* (07:17~07:23)

> ⚠️ **벤더 발표 하나에서 온 개념**이다. 처방(wait condition + signal)은 Temporal primitive의 이름이고, 화자는 그것을 파는 회사 직원이다. 패턴 자체는 특정 제품에 묶이지 않는다 — 아래는 그렇게 일반화해 적었다.

## 문제 — "call the human" 함수

> *"If you write it just straight out as a function to say call the human or let the human have a an input, it can become a blocking call and it can get lost if your service went down. It might lose track of what was going on with that human's uh engagement."* (07:30~07:51)

실패 두 가지:

1. **blocking** — 사람은 *"not going to respond in 200 milliseconds"*, *"several minutes, maybe days, maybe weeks, maybe longer"*(14:29~14:44). 그동안 스레드·프로세스를 붙잡는다.
2. **유실** — 기다리는 사이 서비스가 죽으면 *무엇을 누구에게 물었는지* 가 사라진다.

## 처방 — 두 primitive

| primitive | 하는 일 | en-orig |
|---|---|---|
| **wait condition** | 해당 workflow만 멈춘다. 그 대기를 durability 층에 저장해 *"when that ca system came back up, it would know where it left off"* | 08:00~08:17 |
| **signal** | *"you could send a signal at any point"* — 실행 중인 workflow에 사람의 입력을 주입 | 08:17~08:26 · 11:03~11:10 |
| (+ timeout) | *"you want to make sure that it only waits for so long"* | 08:51~08:58 |

결과: *"the whole system could keep running without you necessarily being blocked on that one call to the human"*(08:20~08:26), *"you're not holding a thread"*(08:41~08:43), 크래시 생존(08:43~08:48).

## 두 방향, 같은 모양

| 방향 | 누가 개시 | 데모 | 구현 |
|---|---|---|---|
| **사람 → 에이전트** | 고객이 주문 변경을 제출, 다른 사람이 승인 | 기사 A 한 명만 멈추고 나머지는 계속(02:18~02:50) | 변경 요청이 signal, 해당 workflow만 wait |
| **에이전트 → 사람** | dispatch 에이전트가 고액 주문에서 사람 승인 요청 | worker를 죽이고 오프라인 중 approve → replay로 재개(14:21~16:11) | LangGraph `interrupt` → wait condition → signal (12:37~13:06) |

*"whether it's the human initiating it or the computer initiating it (…) we are using two main primitives"*(17:36~17:46).

## 언제 사람을 부르나

이 패턴은 **어떻게** 기다릴지이고, **언제** 부를지는 별개 판단이다. 화자의 기준:

- ⭐ *"the cost of being wrong is high"*(16:35~16:42) — 경우별, 특히 보안 관점(17:02~17:04).
- ⭐ 반대편 비용 **alert fatigue** — *"you just start saying yes, yes, yes, yes, yes every time it asks you questions"*(17:09~17:15).
- *"we're trying to get the models better so that you can trust them so that you can address that alert fatigue, but they're still probabilistic models"*(17:15~17:25).

→ 기준 자체는 [[risk-proportional-human-review]]와 같다(위험도에 비례해 사람을). 이 소스가 더한 것은 **사람을 부르는 비용** 쪽 이름(alert fatigue)이다 — [[no-silent-write]]가 *"승인 피로 — 어느 소스도 말하지 않는다"* 고 남긴 자리. ⚠️ 수치·처방은 없다.

## 이 위키에서의 좌표

- **[[human-plumbing]]** — 짝을 이루는 반대 방향. human plumbing은 *사람이 에이전트의 루프를 손으로 이어 주는* 안티패턴이고, 이 패턴은 *에이전트가 사람을 불러야 할 때* 그 호출을 견고하게 한다. 둘 다 사람을 **동기적 배관**에서 빼낸다.
- **[[agent-distributed-systems]]** — 원칙 6 *"승인은 행동·타임스탬프·행위자·만료에 묶인다"* 와 맞물려야 한다. 이 패턴은 승인을 **잃지 않게** 하지만, 승인이 **무엇에 유효한지**는 다루지 않는다. 며칠 뒤 도착한 signal이 그 사이 바뀐 상태에도 유효한가 — ⚠️ 발표에 없는 질문(timeout만 언급).
- **[[agent-trust-curve]] · [[model-calibration]]** — 언제 부를지를 *시간에 따라* 옮기거나(trust curve) *보정된 확률 임계값* 으로 정하는(calibration) 쪽과 결합하면, 이 패턴은 그 판정이 "사람"으로 떨어졌을 때의 **실행 경로**가 된다.
- **[[action-reversibility]]** — *"cost of being wrong"* 의 구체 축 하나(되돌릴 수 있는가). 화자는 이 말을 쓰지 않는다.

## ⚠️ 유보

- 근거는 벤더 데모 1회. *"millions of workflows (…) parked"*(09:01~09:06) 같은 확장성 주장은 근거 미발화.
- 사람 쪽 UX(알림 채널, 누가 승인권자인지, 대기열이 쌓일 때)는 다루지 않는다 — *다른 사람이 승인한다*(02:36~02:44)는 장면뿐.
- durable 층이 없는 환경(일반 웹 서버 + DB 상태 플래그)으로도 같은 패턴을 구현할 수 있는지, 그 비용은 — 발표 범위 밖.

## References

- [[tech-bridge-human-is-async-api]] — first-seen · [[temporal]]
- 관련: [[durable-execution]] · [[agent-distributed-systems]] · [[risk-proportional-human-review]] · [[no-silent-write]] · [[human-plumbing]] · [[agent-trust-curve]] · [[model-calibration]] · [[action-reversibility]]
