---
title: "Tech Bridge — 인간은 비동기 API다 (Melanie Warrick · Temporal): 사람을 기다리는 에이전트는 blocking call이 아니라 wait condition + signal로, durable execution 위에서"
type: source
tags: [human-in-the-loop, durable-execution, temporal, workflow, activity, worker, wait-condition, signal, replay, google-adk, langgraph, multi-agent, alert-fatigue, harness, vendor-talk, video]
source-url: https://www.youtube.com/watch?v=HjQ1G1NvvHQ
source-type: video
author: "Tech Bridge (한영자막 재배포) · 발표 Melanie Warrick([[temporal|Temporal]], 이름은 설명란에만) · 행사명 미발화(설명란 링크로 AI Engineer 계열 추정) · 녹화일 미상"
date-published: 2026-10-09
ingested: 2026-10-10
created: 2026-10-10
updated: 2026-10-10
---

# Tech Bridge — 인간은 비동기 API다 (Melanie Warrick · Temporal)

[[tech-bridge|Tech Bridge]]가 재배포한 **18:46 발표, 녹화된 Q&A 없음, 공식 챕터 20개.** 화자는 durable execution 플랫폼 [[temporal|Temporal]]의 직원(이름 Melanie Warrick은 설명란에만)이고, 스스로 *"you're going to hear me pitching about the company that I work for"*(00:13~00:19)라고 밝힌다 — **⚠️ 당사자 진술, 벤더 발표.** 이 위키에 **durable execution(내구 실행)과 Temporal을 다루는 첫 소스**이고, 새 페이지 셋이 생긴다 → [[durable-execution]] (engineering, 신규) · [[human-as-async-api]] (concept, 신규) · [[temporal]] (entity, 신규).

> **사람은 에이전트에게 도구지만 200ms 안에 답하지 않는다 — 몇 분, 며칠, 몇 주. 그래서 "사람을 부르는 함수"를 그대로 쓰면 blocking call이 되고, 서비스가 죽으면 그 상호작용을 잃는다. 처방은 사람의 입력을 비동기 이벤트로 다루는 것: 워크플로를 wait condition으로 멈춰(parked) 두고, 사람의 응답은 언제든 signal로 주입한다. 그 대기 상태가 durability 층에 저장돼 있으면 worker가 죽어도 이벤트 로그를 replay해 멈춘 자리에서 이어 간다. 사람을 언제 부를지는 "틀렸을 때의 비용"과 "alert fatigue" 사이의 경우별 판단이다.**

> *"the human is an async API"* (03:22~03:24) · *"we're not tools, but we are a tool to the agent"* (07:17~07:23) · *"it can become a blocking call and it can get lost if your service went down"* (07:39~07:44) · *"You want a weight[=wait] condition and a signal."* (07:55~07:57) · *"It's not redone. It's just replayed up until the point at which it last liftoff[=left off]."* (15:52~15:58)

ASR·ko 보정: ko는 회사명 **Temporal을 "시간"·"일시적인"·"임시"로** 거의 매번 풀어(00:12에서 *화자 소속* 자체가 사라진다), **worker를 "노동자"로**, **blocking call을 "통화 차단"으로**(07:39), **not holding a thread를 "실을 잡고 있는 거예요"로**(부정 소실, 08:42), 복구 설명 *"event log is getting replayed. It's not redone"* 을 **"등록이 이루어진다 … 모르겠습니다 그는 또 그랬어 … 연기한다"** 로(15:49~15:53), 판단 기준 *"the cost of being wrong is high"* 를 **"실수할 확률이 높습니다"** 로(16:38~16:40 — 비용이 확률로) 옮겼다. `en`이 **ADK를 "80K"로**(01:01), **durable execution을 "long-lasting execution"으로**(03:17), **ADK framework를 "LangChain"으로**(06:29) 바꾼 것을 ko가 물려받았다(공유 오류). en-orig는 *wait condition* 을 줄곧 **"weight condition"** 으로, LangGraph를 **"langraph"** 로 들었다. 전체 목록은 raw. **인용은 en-orig에서만** 했다.

> ⚠️ **벤더 발표이고 실측이 없다.** 수치는 대비용 수사 *"200 milliseconds"*(14:29~14:32)와 확장성 주장 *"You can have millions of workflows out there parked and it can keep running."*(09:01~09:06)뿐 — 후자는 **근거·조건 미발화.** 데모는 화자 자신의 장난감 시스템 1회 시연이다. 슬라이드 코드는 자막에 없어 **실제 API 이름은 이 위키가 확인하지 못했다**(raw 헤더).
>
> ⚠️ **화자 이름·행사.** 이름은 설명란(*"Temporal의 멜라니 워릭(Melanie Warrick)"*)과 링크(LinkedIn·X·GitHub `nyghtowl`)에만. 행사명 미발화 — 설명란에 `ai.engineer` 링크가 있어 [[ai-engineer|AI Engineer]] 계열로 **추정**만 한다. 데모의 *"ferry building"*·*"Oracle Park"* 는 시나리오 속 샌프란시스코 지명이지 행사 장소 진술이 아니다.
>
> ⚠️ **설명란 vs 발화.** 설명란의 *"'인간 호출(Ask human)' 함수"* 는 발화에 없는 이름이고(발화는 *"call the human"* 07:33~07:35), *"무손실 복구"* 의 *무손실* 도 화자가 한 말이 아니다. 마지막 챕터 *"참고 자료 및 Q&A"* 에 **Q&A는 녹화돼 있지 않다**(18:07~18:10).

## 1. 데모 ① — 사람 → 에이전트: 주문 변경이 한 곳만 멈춘다 (00:00~03:22)

- 설정: Temporal 마스코트 Ziggy의 아이스크림 배달(*"Not really, but let's say he does"* 00:30~00:34). **fleet · customer · dispatch 세 에이전트**가 배달을 조율(00:47~00:58). [[google-cloud|Google]] **ADK**(Agent Development Kit) — *"a um solution that Google is providing to help you orchestrate agents or multiple agents"*(01:03~01:11) — 에 Temporal이 *"baked into it"*(01:15~01:21), 상태를 추적하고 UI로 **event history** 와 parent workflow를 보여 준다(01:24~01:44).
- 고객이 주문을 바꾼다 — *"depending on how you build it out, it could actually break your system"*(02:07~02:11). 여기서는 *"this order is currently pausing driver A"*(02:18~02:24), ⭐ *"The system is running while this one specific uh change is only pausing one part of your system."*(02:27~02:34)
- 승인은 **또 다른 사람**이 — *"another human needs to make a call and whether or not they want to accept that"*(02:36~02:44). 승인하는 동안 *"the rest of the system kept running. Orders were coming in."*(02:44~02:50) 갱신이 반영되고 기사 A는 Oracle Park로(03:05~03:14).
- *"that is durable execution with temporal and ADK integrated"*(03:16~03:21).

→ [[human-as-async-api]] · [[durable-execution]]

## 2. 에이전트 루프와 하네스, 그리고 durability (03:22~05:32)

- 에이전트 루프: *"You can reason, act, and observe"*(03:32~03:38), *"It can be a for loop, it can be a while loop."*(03:56~03:57)
- 하네스에 대해선 겸손하게 — *"I'm not going to sit here and tell you I I am the expert on the harness"*(04:09~04:13). 모델·도구·메모리·가드레일·보안이 하네스에 드는지 *"there's debates"*(04:27~04:34), 요점은 *"getting these agents with structure so that they can work reasonably well when they're put out into production"*(04:34~04:41). ⭐ *"And part of that picture should be durability."*(04:41~04:47)
- 데모 구조: fleet 에이전트는 Google Maps 같은 도구로 기사를, customer 에이전트는 Google search 같은 도구로 주문을 조사하고, dispatch 에이전트가 그 입력으로 결정한다(04:47~05:12). *"we need to have some durability in that system to make sure that it stays up and running and doesn't fall over"*(05:26~05:32).

→ [[agent-harness-design]] · [[harness-engineering]]

## 3. Temporal — worker · workflow · activity (05:32~07:09)

- *"temporal is helping you to standardize your fa failure handling and your state management in your system any system any distributed system especially any systems with agents"*(05:34~05:46). *"we're software and we're also a service"*(05:46~05:51), Python·TypeScript·Rust 등(06:00~06:05).

| primitive | 역할 (en-orig) | 에이전트에서 무엇이 여기 가나 |
|---|---|---|
| **worker** | *"The worker is really running that code."* (06:17~06:20) | 코드를 실제로 실행하는 프로세스 — 데모 ②에서 죽이는 대상 |
| **workflow** | *"where you're going to be able to uh keep track of the steps in your system"* (06:20~06:28) | ⭐ *"an ADK framework would be running inside a workflow. uh your agent could work run inside of a workflow because it's a loop, right?"* (06:28~06:37) |
| **activity** | *"all the stuff that's integrating or interacting with stuff externally"* (06:37~06:41) | ⭐ *"any kind of model call or any kind of tool call, those would be set up as activities"* (06:44~06:49) |

- 라이선스·사업 모델: *"we're free and open source at that GitHub URL. Um, you pay us if you you have us manage your state with our service. Otherwise, you can host it, self-host it on your own system."*(06:55~07:08) — ⚠️ 당사자 진술.

→ [[durable-execution]] · [[temporal]]

## 4. "call the human" 함수가 실패하는 이유 → wait condition + signal (07:09~09:06)

- ⭐ *"the human granted, you know, we're not tools, but we are a tool to the agent."*(07:17~07:23)
- ⭐ 문제 정의: *"If you write it just straight out as a function to say call the human or let the human have a an input, it can become a blocking call and it can get lost if your service went down. It might lose track of what was going on with that human's uh engagement."*(07:30~07:51)
- 처방, 두 primitive: *"You want a weight[=wait] condition and a signal."*(07:55~07:57) — *"isolate an event, apply a weight condition, store that in that workflow, in that durability layer so that if anything fell over in the system, when that ca system came back up, it would know where it left off. And you could send a signal at any point, but the whole system could keep running without you necessarily being blocked on that one call to the human."*(08:00~08:26)
- 이득: *"you're not holding a thread. You're not it's going to survive any kind of crashes"*(08:41~08:48), **timeout** — *"If you're waiting on a human to respond and you want to make sure that it only waits for so long, you can apply timeouts"*(08:51~08:58), 확장성 *"millions of workflows out there parked"*(09:01~09:06, ⚠️ 벤더 주장).

→ [[human-as-async-api]]

## 5. 코드 — ADK 통합 (09:59~11:23)

- 모델: *"we have uh we have the temporal model class that you will wrap around the model and then you'll pass it in for ADK"*(10:12~10:21). 도구: *"you apply our activity tool uh to wrap around your tools"*(10:25~10:30). 에이전트는 *"like you would with any kind of ADK setup"*(10:32~10:36). worker에 *"the Google ADK plugin"*(10:38~10:44).
- wait condition은 asyncio의 await 위에서(*"using this async.io when it uses a weight"* 10:48~10:54 — `en` *"async IO when using await"*): *"for that specific workflow, I want you to pause it. don't run any other code but you can keep running the co- routines on that workflow or any other workflows in the system"*(10:52~11:03).
- signal: *"that workflows signal it will be able to take any kind of input and injected into a running workflow"*(11:03~11:10). 할 일이 없는 workflow는 *"taken off of your memory (…) and put in in parked"*(11:12~11:20).

⚠️ 실제 클래스·함수 이름은 슬라이드에만 있고 자막엔 위 묘사뿐이다.

## 6. 에이전트 → 사람: LangGraph 통합 (11:23~13:29)

- *"So I showed you human to agent. What I want to show you is what does it look like when the agent comes in and needs the human to be involved. It's pretty similar."*(11:23~11:32) — 같은 workflow + wait condition + signal.
- ⭐ *"with temporal we can work with multiple frameworks. We are framework agnostic."*(11:43~11:49)
- [[langchain|LangGraph]] 통합: *"you're passing us into each node for your graph"*(12:00~12:04). 모델 호출(*"like an invoke the model"*)과 다른 도구 호출은 activity, *"if it's a step, a step in that process, then that's set up as a workflow"*(12:08~12:23). ⭐ *"This is determinism and non-determinism in terms of workflows are deterministic, activities are non-deterministic."*(12:21~12:30) worker엔 *"the plug-in for the langraph"*(12:30~12:32).
- 사람 호출: *"we use the interrupt to call out from their node"*(12:37~12:42) → *"use that weight condition in the loop tracking for that interrupt signal to pause that workflow. And then the signal will capture whatever the human (…) responds with"*(12:52~13:06). LangGraph에 대해 공정하게: *"langraph is more than a framework. But in this case, I'm using it as a framework"*(12:44~12:49).
- 설계: customer·fleet 에이전트는 ADK, dispatch 에이전트는 LangGraph, *"Temporal is interwoven throughout"*(13:15~13:22).

→ [[langchain]] · [[durable-execution]]

## 7. 데모 ② — 고액 주문, 승인 대기 중 worker를 죽인다 (13:29~16:28)

1. 고액 주문 투입 — *"This is an order that'll most likely want a human involved."*(13:39~13:42) 주문마다 프레임워크별 **child workflow** 로 갈라진다(13:51~14:00).
2. customer·fleet가 평가해 dispatch로 → dispatch: *"I need to get uh a human involved in this. So, I'm going to go into a pause state while I'm waiting for the human to respond."*(14:21~14:29)
3. ⭐ *"humans are not going to respond in 200 milliseconds. (…) humans are most likely going to take several minutes, maybe days, maybe weeks, maybe longer."*(14:29~14:44) 그 사이 *"the little cars are continuing to keep going"*(14:49~14:51).
4. *"kill worker. Cool. So that takes it offline."*(15:06~15:09) → **오프라인 상태에서 approve**(15:18~15:22). *"this is stuff that's happening off of your service. It's over on its own data store. So, we can still keep track of that event and cue[=queue] it."*(15:22~15:34)
5. worker 재기동 → ⭐ *"your event log is getting replayed. It's not redone. It's just replayed up until the point at which it last liftoff[=left off]. So it knows here's my current state and this is now the next step in that state"*(15:50~16:03) → 주문 배정·배달 완료(16:06~16:11). *"That is durability in your system."*(16:11~16:15)

⚠️ 1회 시연. *"Don't mind me as I do this in a very interesting way"*(15:14~15:16) — 화면 조작은 자막으로 따라갈 수 없다. 오프라인 중 들어온 승인이 **어디에** 저장됐는지는 *"its own data store"* 이상으로 말하지 않는다(위키의 배경지식: Temporal 서버의 이벤트 히스토리 — 자막 밖).

→ [[durable-execution]] · [[human-as-async-api]]

## 8. 사람을 언제 루프에 넣나 — 틀렸을 때의 비용 vs alert fatigue (16:28~17:32)

- *"When should the human be in the loop? Ah, this is the real question. It's a hard one."*(16:31~16:36)
- ⭐ 기준 하나: *"the big thing you want to take into consideration is the cost of being wrong is high. Okay, it's a case- by case basis"*(16:35~16:43). 자율성을 원하지만 *"these models are probabilistic and they are hard to get to a place to be reliable. That's why we've got all this stuff happening around harnesses"*(16:47~16:54). *"you want to assess the cost of being wrong. What is that worth to you? And especially in a security standpoint."*(16:58~17:04)
- ⭐ 반대편: *"alert fatigue is real. like a lot of us are seeing, you know, you just start saying yes, yes, yes, yes, yes every time it asks you questions."*(17:06~17:15) *"So, you're trying to balance between those two"*(17:13~17:16).
- 결론은 판단의 위임: *"That's the thing you've got to evaluate for the problems that you're solving."*(17:26~17:29)

⚠️ ko는 *"the cost of being wrong is high"* 를 **"실수할 확률이 높습니다"** 로 옮겨 기준을 *비용* 에서 *확률* 로 바꾼다(16:38~16:40) — 이 위키가 [[risk-proportional-human-review]]·[[model-calibration]]에서 구분하는 두 축이다.

→ [[risk-proportional-human-review]] · [[no-silent-write]]

## 9. 요약 (17:32~18:46)

*"whether it's the human initiating it or the computer initiating it um you are seeing that we are using two main primitives in terms of you're applying a weight condition to pause that workflow and a signal from the human to be able to continue the work"*(17:36~17:51), 그리고 *"I've shown you that we can use multiple frameworks"*(18:00~18:03). 데모는 *"This is up on GitHub"*(18:19~18:22, QR 코드 — URL 미발화).

## 이 위키와의 연결

### 이어지는 것

- **[[agent-distributed-systems]]** — Salman Munaf의 *"에이전트가 부작용을 내는 순간 분산 시스템 문제"* 에 대한 **구현 쪽 답 하나**. 그 페이지의 타임아웃·보상·관측 요구를 Temporal은 *"standardize your failure handling and your state management"*(05:34~05:39)로 묶어 플랫폼에 넘긴다. ⚠️ 다만 그 페이지 원칙 6(**승인은 행동·타임스탬프·만료에 묶인다**)은 이 발표가 다루지 않는다 — 오프라인 중 들어온 *approve* 가 큐에 남았다 재생되는 데모는, 며칠 뒤 도착한 승인이 **여전히 유효한가**라는 질문을 남긴다(timeout은 언급만, 08:51~08:58).
- **[[agent-harness-design]] · [[managed-agents]]** — Claude Platform 팀의 *"하네스는 내구성이 뛰어난 서버에서"*([[tech-bridge-claude-platform-agent-era]])와 같은 방향. 여기서는 durability를 **하네스의 한 구성 요소**로 명시한다(*"part of that picture should be durability"* 04:41~04:47).
- **[[deterministic-agent-pipeline]] · [[agent-state-machine]]** — *"workflows are deterministic, activities are non-deterministic"*(12:25~12:30)는 Uber Debug Assist의 *결정론 노드 + LLM 노드* 와 겉모양이 같다. ⚠️ 그러나 결정론의 **뜻이 다르다** — Uber·Khourshid는 *경로가 고정됐다*(계획을 사람이 정한다)는 뜻이고, Temporal의 workflow 결정론은 *replay했을 때 같은 결과가 나와야 한다*는 실행 모델의 요구다(이 설명은 위키의 배경지식, 화자는 이유를 말하지 않는다). Temporal은 **에이전트 루프 전체를 workflow에** 둔다(06:30~06:37) — 경로가 동적이어도 된다. → [[durable-execution]]
- **[[langchain]]** — LangGraph의 `interrupt`를 durable 대기로 바꾸는 통합. LangGraph를 다룬 세 번째 소스(Uber 고객 사례, Khourshid 언급에 이어).
- **[[risk-proportional-human-review]]** — 기준(*cost of being wrong*)은 같고, 이 소스는 반대편 비용으로 **alert fatigue** 를 처음 명시적으로 세운다. [[no-silent-write]]가 *"승인 피로 — 어느 소스도 말하지 않는다"* 고 남긴 빈칸에 **이름만** 붙는다(수치·처방 없음).
- **[[human-plumbing]]** — 방향이 반대인 짝. Quenneville은 *사람이 루프를 손으로 이어 주는* 낭비를 없애자고 하고, Warrick은 *에이전트가 사람을 부를 때* 그 호출을 어떻게 견고하게 할지를 말한다. 둘 다 사람을 루프의 **배관**이 아니라 **비동기 입력원**으로 둔다.

### 갈리는 것

> ⚠️ **Contradiction(용어): "workflow".** 이 위키의 [[workflow-vs-agent]]에서 workflow는 *미리 정의된 코드 경로*(에이전트의 반대)다. Temporal의 workflow는 **durable하게 실행되는 코드 단위**이고, 화자는 *"your agent could work run inside of a workflow because it's a loop"*(06:30~06:37)라며 **에이전트를 workflow 안에** 넣는다. 같은 단어가 축이 다른 두 뜻으로 쓰인다 — 이 위키에서 Temporal 맥락의 workflow는 [[durable-execution]]의 뜻으로 읽는다.

## 해소하지 않고 표시만 한 것

- 화자 이름(설명란에만) · 행사명·도시·녹화일.
- 슬라이드 코드의 실제 API 이름(*"temporal model class"*, *"activity tool"*, *"weight condition"*, *"workflows signal"* 의 정확한 표기).
- *"millions of workflows (…) parked"* 의 근거.
- 오프라인 중 승인이 저장된 *"its own data store"* 의 정체(Temporal 서버로 추정 — 자막 밖).
- 승인의 유효 기간·바인딩([[agent-distributed-systems]] 원칙 6) — 다루지 않음.
- 데모 저장소 URL(QR 코드만) · 설명란 링크(`adk.dev/integrations/temporal/`, `docs.temporal.io/…/langgraph`) — 열어 보지 않았다.

## 등장 개체

- 인물: Melanie Warrick(설명란에만, 페이지 없음)
- 조직: [[temporal]] (신규) · Google([[google-cloud]]) · [[ai-engineer]](추정) · [[langchain]]
- 제품·도구: Temporal(오픈소스 + 관리형 서비스) · Google ADK(Agent Development Kit, 페이지 없음 — [[google-cloud]]에서 다룸) · LangGraph([[langchain]]) · Google Maps · Google search(데모 도구)
- 개념: [[human-as-async-api]] (신규) · [[durable-execution]] (신규) · [[agent-distributed-systems]] · [[agent-harness-design]] · [[risk-proportional-human-review]] · [[no-silent-write]] · [[workflow-vs-agent]] · [[deterministic-agent-pipeline]] · [[agent-state-machine]] · [[human-plumbing]] · [[model-calibration]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=HjQ1G1NvvHQ> (18:46, `upload_date` 2026-10-09)
- raw: `01.raw/articles/2026-10-09_인간은 비동기 API입니다 - AI 에이전트가 사람을 기다리다 멈추지 않는 법.md`
- 설명란 링크: <https://temporal.io> · <https://github.com/temporalio/temporal> · <https://adk.dev/integrations/temporal/> · <https://docs.temporal.io/develop/python/integrations/langgraph> · <https://ai.engineer> (⚠️ 열어 보지 않았다)
- 같은 주제: [[tech-bridge-agents-as-distributed-systems]] · [[tech-bridge-claude-platform-agent-era]] · [[tech-bridge-uber-debug-assist]] · [[tech-bridge-goodbye-slop-state-machines]] · [[tech-bridge-jev-calibrated-decisions]]
- [[tech-bridge]] · [[temporal]]
