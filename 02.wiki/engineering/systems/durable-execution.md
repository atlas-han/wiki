---
title: "Durable Execution — 내구 실행 (worker · workflow · activity, replay)"
type: engineering
category: system
tags: [durable-execution, workflow-engine, distributed-systems, fault-tolerance, replay, event-history, determinism, agents, human-in-the-loop, temporal]
aliases: [durable execution, 내구 실행, 내구성 있는 실행, durable workflow, workflow engine]
related: [agent-distributed-systems, human-as-async-api, agent-harness-design, managed-agents, workflow-vs-agent, deterministic-agent-pipeline, agent-state-machine, brain-hands-decoupling]
first-seen: tech-bridge-human-is-async-api
sources: [tech-bridge-human-is-async-api]
created: 2026-10-10
updated: 2026-10-10
---

# Durable Execution — 내구 실행

**프로세스가 죽어도 실행이 멈춘 자리에서 이어지도록, 코드의 진행 상태를 실행 엔진이 저장·복원하는 실행 모델.** 개발자는 평범한 코드처럼 쓰고, 엔진은 각 단계의 결과를 이벤트 히스토리로 남겼다가 재기동 시 **replay** 해서 상태를 되살린다. 이 위키에는 [[temporal|Temporal]] 직원의 발표 [[tech-bridge-human-is-async-api]]로 들어왔고, 거기서의 용도는 **에이전트 루프와 그 안의 사람 대기**를 견고하게 하는 것이다.

> *"that is durable execution with temporal and ADK integrated"* (03:16~03:21) · *"It's not redone. It's just replayed up until the point at which it last liftoff[=left off]."* (15:52~15:58)

> ⚠️ 이 페이지의 1차 출처는 **벤더 발표 하나**다. 화자가 말하지 않은 배경(왜 workflow가 결정론적이어야 하는지 등)은 **"위키의 배경지식"** 으로 따로 표시했다.

## 세 primitive (Temporal 기준)

| primitive | 무엇 | 결정론 | 에이전트에서 |
|---|---|---|---|
| **worker** | 코드를 실제로 실행하는 프로세스 — *"The worker is really running that code."* (06:17~06:20) | — | 죽여도 되는 것. 데모에서 *"kill worker"*(15:06) |
| **workflow** | 단계를 추적하는 durable 코드 단위 — *"keep track of the steps in your system"* (06:20~06:28) | **결정론적** (12:25~12:28) | 에이전트 루프 자체, ADK 프레임워크, LangGraph의 각 단계 (06:28~06:37 · 12:16~12:23) |
| **activity** | 외부와 상호작용하는 모든 것 (06:37~06:41) | **비결정론적** (12:28~12:30) | **모델 호출과 도구 호출** — *"those would be set up as activities"* (06:44~06:49) |

배치 규칙 한 줄: **루프(제어 흐름)는 workflow, 바깥 세계를 건드리는 호출(LLM 포함)은 activity.**

> **위키의 배경지식(자막 밖):** workflow가 결정론적이어야 하는 이유는 replay 때문이다. 재기동한 worker는 workflow 코드를 처음부터 다시 돌리되, 이미 끝난 activity는 **다시 호출하지 않고** 이벤트 히스토리에 기록된 결과를 돌려준다 — 화자의 *"It's not redone. It's just replayed"* 가 이것이다. 그래서 LLM 호출처럼 매번 다른 답을 내는 것은 반드시 activity에 넣어야 하고, workflow 코드 안에서 직접 시각·난수·네트워크를 쓰면 replay가 어긋난다.

## 무엇을 얻는가 (발표가 보여 준 것)

1. **부분 정지** — 한 주문의 변경 대기가 *"only pausing one part of your system"*(02:27~02:34), 나머지 주문은 계속 처리된다.
2. **장기 대기** — workflow를 wait condition으로 멈추면 스레드를 잡지 않고(*"you're not holding a thread"* 08:41~08:43) 메모리에서 내려가 *"parked"* 된다(11:12~11:20). 사람의 응답처럼 *"several minutes, maybe days, maybe weeks"*(14:37~14:44) 걸리는 일에 맞다.
3. **크래시 복구** — 대기 중 worker를 죽이고, 오프라인 상태에서 들어온 승인은 *"over on its own data store"* 에 큐잉되고(15:26~15:34), 재기동 후 replay로 *"here's my current state and this is now the next step"*(15:58~16:03).
4. **표준화** — *"standardize your fa failure handling and your state management"*(05:34~05:39), timeout 같은 내장 primitive(08:48~08:58).

## 에이전트 프레임워크와의 결합

| 프레임워크 | 결합 방식 (en-orig) |
|---|---|
| Google ADK | 모델을 *"temporal model class"* 로 감싸고(10:14~10:18), 도구를 *"activity tool"* 로 감싸고(10:25~10:30), worker에 *"Google ADK plugin"*(10:38~10:44) |
| LangGraph ([[langchain]]) | *"passing us into each node for your graph"*(12:00~12:04) — 모델·도구 호출은 activity, 단계는 workflow, worker에 LangGraph plugin(12:30~12:32). 사람 호출은 LangGraph `interrupt` → wait condition → signal(12:37~13:06) |

*"We are framework agnostic."*(11:47~11:49) — 프레임워크를 대체하지 않고 **아래에 깐다.** ⚠️ 실제 클래스·함수 이름은 슬라이드에만 있어 이 위키는 확인하지 못했다.

## 이 위키에서의 좌표

- **[[agent-distributed-systems]]** — *"에이전트는 분산 시스템 문제"* 의 처방(타임아웃=상태 불명, 재시도 예산, 보상, 관측)을 **개별 도구 설계**로 풀던 것을, durable execution은 **실행 모델**로 흡수한다. 둘은 겹치지만 같지 않다: 멱등성 키·보상(saga)·승인 바인딩은 여전히 activity 설계자의 몫이다(⚠️ 위키의 정리 — 발표는 이 셋을 말하지 않는다).
- **[[managed-agents]] · [[brain-hands-decoupling]]** — *"하네스는 내구성 있는 서버, 샌드박스는 일회용"* 과 같은 분리. durable execution에선 **workflow(두뇌의 진행 상태)가 durable, worker(실행 손)는 일회용**이다.
- **[[agent-harness-design]]** — 화자는 durability를 하네스의 한 구성 요소로 둔다(*"part of that picture should be durability"* 04:41~04:47).
- **[[human-as-async-api]]** — 이 실행 모델 위에서 human-in-the-loop를 구현하는 패턴.

> ⚠️ **Contradiction(용어): "workflow"와 "결정론".** [[workflow-vs-agent]]의 workflow는 *미리 정의된 경로*(에이전트의 반대)이고, [[deterministic-agent-pipeline]]·[[agent-state-machine]]의 결정론은 *경로가 고정됐다* 는 뜻이다. durable execution의 workflow는 **에이전트를 담는 그릇**이고(*"your agent could work run inside of a workflow because it's a loop"* 06:30~06:37), 결정론은 **replay 가능성**의 요구다 — 경로가 LLM 응답에 따라 매번 달라져도, 그 응답이 activity 결과로 기록돼 있으면 replay는 결정론적이다(위키의 배경지식). 같은 단어, 다른 축.

## ⚠️ 유보

- 근거는 **벤더 1인의 데모 1회**. 확장성(*"millions of workflows"* 09:01~09:06)·지연·비용 수치 없음.
- replay 비용(긴 에이전트 루프의 이벤트 히스토리 크기), workflow 코드 변경 시 진행 중 실행과의 호환(버저닝)은 발표가 다루지 않는다.
- Temporal 외 durable execution 구현은 이 위키에 아직 소스가 없다.

## References

- [[tech-bridge-human-is-async-api]] — first-seen ([[temporal]] 직원 발표)
- 관련: [[agent-distributed-systems]] · [[human-as-async-api]] · [[agent-harness-design]] · [[managed-agents]] · [[brain-hands-decoupling]] · [[workflow-vs-agent]] · [[deterministic-agent-pipeline]] · [[agent-state-machine]] · [[langchain]]
- 외부: <https://temporal.io> · <https://github.com/temporalio/temporal> (⚠️ 열어 보지 않았다)
