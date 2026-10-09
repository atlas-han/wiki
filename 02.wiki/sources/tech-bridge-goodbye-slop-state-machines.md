---
title: "Tech Bridge — 슬롭이여 안녕, 결정론이여 어서 와 (David Khourshid · Stately/XState): 슬롭은 구조 없는 위임에서 온다, 상태 머신은 가드레일에서 자기 개선의 도구로"
type: source
tags: [state-machine, determinism, ai-slop, unstructured-delegation, mega-prompt, control-flow, observability, edge-evals, self-improvement, process-mining, xstate, langgraph, jev, agent-conf, video]
source-url: https://www.youtube.com/watch?v=D7q8fa589FY
source-type: video
author: Tech Bridge (한영자막 재배포) · 발표 [[david-khourshid]] ([[xstate|XState]] 제작자 · Stately 창업자) · Agent Conf 2026(폴란드, 도시 미발화) · Jev 발표 며칠 뒤 녹화(⚠️ 2026년 9월 전후 추정)
date-published: 2026-10-08
ingested: 2026-10-09
created: 2026-10-09
updated: 2026-10-09
---

# Tech Bridge — 슬롭이여 안녕, 결정론이여 어서 와 (David Khourshid · Stately/XState)

[[tech-bridge|Tech Bridge]]가 재배포한 **20:29 발표, Q&A 없음, 공식 챕터 21개.** 화자는 상태 머신 라이브러리 [[xstate|XState]]의 제작자이자 Stately(stately.ai) 창업자 [[david-khourshid|David Khourshid]](@DavidKPiano). 폴란드에서 열린 **Agent Conf**의 2026년 회차이고, 화자는 3년 전(2023) 같은 행사에서 *"에이전트 행동을 상태 머신으로 제약하기"* 를 발표했다. 이번 주장은 그 뒤집기다 — **상태 머신은 에이전트를 묶는 울타리가 아니라 에이전트가 스스로 워크플로를 개선하게 하는 공유 산출물이다.** 이 위키에 **상태 머신을 에이전트 설계 단위로 다루는 첫 소스**이고, 개념 하나가 생긴다 → [[agent-state-machine]] (신규).

> **슬롭은 모델이 멍청해서가 아니라 구조 없이 전부 넘겨서(unstructured delegation) 생긴다. 결정론은 내용이 아니라 규칙에 산다 — 내용은 에이전트에게, 규칙은 상태와 전이로. 메가 프롬프트는 제어 흐름을 텍스트에 묻어 증명도 관찰도 안 되고 규칙이 컨텍스트에 묻혀 희석된다. 명시적 상태 머신이면 금지된 행동은 "전이가 없어서" 불가능하고, 로그는 구조화되고, eval은 상태·결과뿐 아니라 전이(edge)까지 겨눌 수 있다. 그리고 그 머신을 트레이스·eval과 함께 다른 에이전트에게 넘겨 V2를 받아 V1과 비교한다 — 상태 머신은 에이전트가 자기 개선하는 방법이다.**

> *"So, where does slop in agents come from? In my opinion, it comes from unstructured delegation."* (03:28~03:32) · *"modeling is not ceremony when it actually replaces confusion, both for you and for the agents"* (10:16~10:21) · *"you cannot draw arrows in paragraphs"* (11:39~11:42) · *"But one thing we're missing is actually evaling the edges."* (12:29~12:31) · *"The state machine is how you could have the agent self-improve."* (17:18~17:23)

ASR·ko 보정: ko(와 `en`)가 **slop을 "쓰레기"·"여유분"으로**(00:00, 03:26 — `en` *"trash"·"junk"*, 공유 오류), **edges를 "한계"로**(12:30 — `en` *"limits"*, 공유 오류) 옮겼고, *non-deterministic parts* 를 **"결정론적 예시"로**(05:45~05:48), *replaces confusion* 을 **"혼란을 줄 것"으로**(10:16~10:23), *I'm not arguing that (…) modeling everything (…) is good* 을 **"모델링이 좋다고 말하는 거예요"로**(11:14~11:22), 컨텍스트 속 규칙이 *less significant* 해진다를 **"더 엄격해집니다"로**(07:33~07:37) 뒤집었다. 녹화 시점의 유일한 상대 단서 *"A couple days ago (…) Type Safe announced Jev"* 는 ko에서 **"두세 개 그 당시 (…) 비판을 받았습니다"** 로 사라졌다(17:51~17:56). en-orig는 행사명을 첫머리에서 *"Agent Comp"* 로 들었다(00:10, 세 트랙 공유). 전체 목록은 raw. **인용은 en-orig에서만** 했다.

> ⚠️ **실측이 없는 발표다.** V1 → V2 개선은 **화면 시연 1회와 화자 체감**(*"this actually feels better"* 14:33~14:35)뿐, diff는 *"if you find me after the talk"*(13:51~13:53). Stately 내부 적용(*"software factories at Stately"*, 상태 머신 생성·편집 파이프라인 13:15~13:23)도 결과 미공개. Jev 데모는 1회, 화자 스스로 *"I'm actually surprised."*(20:23). 선행 연구 *"Agent Spec, AIFlow (…) process mining"*(16:53~16:58)은 이름만 — 이 위키는 어느 것도 열어 보지 않았다.
>
> ⚠️ **행사·시점.** 행사명은 발화 *"the previous Agent Conf, which was 3 years ago"*(03:07~03:12)·*"in 2023, at the last Agent Conf"*(17:26~17:30)와 설명란 링크(Callstack 단축 링크 clstk.com)로 **Agent Conf**. 장소 *"We're in Poland"*(00:56~00:58), 연도 *"in 2026"*(17:36~17:41). ⭐ *"A couple days ago, I was pretty much nerd sniped when Type Safe announced Jev"*(17:52~17:56) → **[[jev|Jev]] 발표 며칠 뒤 녹화.** Jev 발표일은 이 위키에 1차 기록이 없다(09-19 업로드 Almeida 편 *"곧 출시"*, 09-25 업로드 LangChain 편 *"방금 나온"*) → **2026년 9월 전후로 추정(⚠️).** 업로드는 2026-10-08.
>
> ⚠️ **설명란 vs 발화.** 설명란은 Jev를 *"최신 에이전트 프레임워크"* 라 부르지만 이 위키의 [[jev]]는 **System 1 모델**이고 화자도 프레임워크라 하지 않는다. *"실시간 자율 복구"* 의 고장은 화자가 일부러 낸 것이다(*"Let me break the grinder"* 20:04).

## 1. 상태 머신 = 결정론, 그리고 "루프는 그래프다" (00:00~03:28)

- 정의를 수학도 다이어그램도 아닌 관계 하나로: *"Given a state and given an event, you are expected to reach a next state."*(01:14~01:18) — *"This is how pretty much every single application that you've ever built works"*(01:21~01:25). 이것이 *"what we call deterministic, and this is going to be a key point in this entire talk"*(01:30~01:36).
- 6개월 된 아들의 비유: 신생아 때는 *"embarrassingly deterministic"*(01:56) 울음 → 먹음 → 배부름 → 잠 → 깸의 단순 루프, 3개월쯤부터 상태 머신이 복잡해지고 지금은 *"sleep regression, so like nothing works"*(02:29~02:32).
- ⭐ *"babies pretty much went from loops to graphs for me, just like our whole hype cycle of agents. You saw everyone talking about loops, and now people are talking about graphs. They're the same picture. They're the same thing, actually. Loops are graphs."*(02:38~02:52)
- 2023년(직전 Agent Conf)엔 *"constraining agent behaviors to state machines"*(03:15~03:17), 오늘은 *"how we could use state machines and determinism to improve agent behavior, and to remove slop"*(03:19~03:27).

→ [[agent-state-machine]] · [[workflow-vs-agent]] · [[design-pattern-state]]

## 2. 슬롭은 어디서 오나 — 구조 없는 위임 (03:28~04:52)

- ⭐ *"it comes from unstructured delegation"*(03:31~03:32): 판단도, 구조도, 구현과 취향(*taste*)도 전부 에이전트에게 넘기는 것(03:36~03:48). 모델은 좋아져서 환각·실수가 줄었지만 *"there's still always a risk of slop when you're just throwing things over the wall and you're hoping for the best from the agent"*(03:59~04:05).
- 그렇다고 *"no, agent, you must do these specific things"* 로 돌아가자는 게 아니다 — *"I'm going to demonstrate the opposite soon"*(04:05~04:14).
- ⭐ *"we say it works, so who cares? The problem is it works until it doesn't and when it stops working, what can we actually point to to tell the agent this is what you need to fix?"*(04:14~04:27) — **고칠 자리를 가리킬 구조가 없다**는 것이 문제의 정의다.
- 결정론의 정의: *"given the same input, you get the same predictable output every single time"*(04:34~04:40). AI와 반대처럼 보이지만 *"specifically for how we improve agent behavior"*(04:48~04:51) 쓸모가 있다.

→ [[ai-slop]]

## 3. 이메일 드래프터 — 결정론은 규칙에, 비결정론은 내용에 (04:52~06:06)

예제는 일부러 단순하게 — *"a distillation of some of the most complex problems that I've been working on for the last few months"*(05:13~05:17).

| | 무엇 | en-orig |
|---|---|---|
| **결정론 (규칙)** | 보내기 전에 반드시 초안 · 사용자가 승인한 메일만 전송 · 수신자를 지어내지 않는다 | *"determinism lives in the rules"* (05:27~05:45) |
| **비결정론 (내용)** | 이메일 본문 · 명확히 하려고 묻는 질문 · 피드백 루프에서 나오는 초안들 | 05:45~06:03 |

→ [[agent-state-machine]]

## 4. 메가 프롬프트의 문제 — 제어 흐름을 텍스트에 묻는다 (06:06~07:49)

*"I'm just going to write a mega prompt. I'm going to have some rules over here. I'm going to give it a tool call to send the email."*(06:09~06:15) — 대부분 작동하지만:

1. **제어 흐름이 프롬프트에** — *"First do this, then do that. If the user asks for changes, revise the draft, and never call send email until the user explicitly approve the email."*(06:24~06:34), 그리고 **도구 설명에도 반복** — *"Only call this after the user approves it."*(06:37~06:41). *"Obviously, you should never write tools like this where the tool is part of the control flow"*(06:41~06:47).
2. **단일 모델·단일 시스템 프롬프트·단일 설정**에 묶인다 — 단계별로 다르게 할 수 없다(06:53~07:05), *"with one prompt, you're limited to one strategy"*(07:39~07:41).
3. **증명·관찰 불가** — *"when you have this black box of a prompt, you can't prove that it works, you can't even see what the agent is thinking or how it's working, even if you turn reasoning on"*(07:10~07:18).
4. ⭐ **규칙이 컨텍스트와 함께 희석된다** — *"the rules decay with context because that prompt, the rules in there, are just it's text, just like the rest of your context. So, as your context builds up, the rules get a little bit less significant over time."*(07:23~07:37)

→ [[hard-vs-soft-enforcement]] · [[context-rot]]

## 5. 명시적 상태 머신 — 금지된 행동은 전이가 없다 (07:49~10:10)

- 요청 → drafting → reviewing(명확화 필요·수정 요청 등) → 수신자가 있으면 sending → 보내기로 결정해야만 sent. 안전장치: *"we should never send an email without a recipient"*(08:14~08:16).
- ⭐ *"it's actually mathematically impossible to send an email when you're in one of in the drafting state or the reviewing state because there just doesn't exist any transition there."*(08:27~08:38) ⚠️ 위키의 주석: **모델 안에** 그 전이가 없다는 뜻 — 구현이 모델을 따른다는 전제 위의 보증이다.
- **데모 v1**(08:46~10:09): 상태 머신에서 자동 시각화된 화면, 머신 자체는 *"an agent wrote this"*(08:52~08:54). *"email Jenny, invite them for coffee after my talk"* — 일부러 모호하게 → 정보 요청 → 제목 입력 → *"draft anyway"* → reviewing → 이름 보충 → 전송. 화자: *"this is pretty cool, but it's not the best workflow. And that is exactly the point that I'm going to show next."*(09:51~09:57) ⚠️ *"we forgot the email address"*(09:43~09:46) 뒤 수신자 가드가 어떻게 작동했는지는 자막에 없다.

→ [[agent-state-machine]] · [[hard-vs-soft-enforcement]]

## 6. "너무 많은 의식(ceremony) 아닌가?" — 관측 가능성과 명시성 (10:10~11:57)

- ⭐ *"modeling is not ceremony when it actually replaces confusion, both for you and for the agents"*(10:16~10:21) — 사람과 에이전트가 **같은 그림**으로 행동을 이해하고, 에이전트는 그것으로 자기 성찰(*introspect*)한다(10:24~10:35).
- 단, *"not everything needs to be formally modeled as a state machine. I'm not saying that you should do this with every single one of your agents, but where it applies, it's really, really useful."*(10:35~10:46)
- **관측**: 평문 로그나 *"agent thinking"* 이 아니라 *"structured logs for what states you are in, what events happened"*(10:57~11:03) — 단순 경로와 복잡 경로가 같은 *sent* 상태에 도달했음을 비교할 수 있다(11:03~11:13).
- ⭐ 요점은 상태 머신 자체가 아니라 **명시성**: *"when things are explicit and you have an explicit structure like a state machine, it's inspectable (…) because you cannot draw arrows in paragraphs. You can't say like, you know, in this prompt, this is where it failed"*(11:27~11:48).

## 7. eval의 세 번째 대상 — 엣지(전이) (11:57~12:44)

| eval 대상 | 예 | en-orig |
|---|---|---|
| 단계(state) | 초안 작성 단계: 이 입력에 이 출력 | 12:05~12:14 |
| 전체 결과(outcome) | 초기 입력 → 전 과정 → 기대한 최종 산출, LLM-as-judge 가능 | 12:14~12:29 |
| ⭐ **전이(edge)** | 사용자로선 *"it does get me to the end state (…) but it's a little bit annoying"* — 경로 자체의 품질 | 12:29~12:43 |

→ [[agent-state-machine]] · [[generator-evaluator-pattern]]

## 8. 에이전트에게 개선안을 묻는다 — V2 (12:44~15:00)

- ⭐ *"take that state machine as a durable artifact and you could pass it to an agent and say, 'Here's my state machine. Here's all the traces from a few of the sample workflows (…) It could be real users. It could be simulated users like you dogfooding your agent. And here's actually all of the evals from each of the steps and the overall evals from the machine. Please propose some changes to this agent.'"*(12:44~13:15)
- 자사 사례: *"software factories at Stately"*, *"state machine generation and editing pipeline"*(13:15~13:23) — ⚠️ 결과 미공개.
- **V2**(13:47~14:28): 작은 문제를 고치려 여러 번 왕복하던 것을 *"draft the email first and then figure out what's needed after"*(14:06~14:11) — 바로 reviewing으로 가는 더 짧은 흐름.
- ⭐ *"all of your evals could pass uh with the first machine, but unless you're dog fooding and you're going through these iteration processes where you're actually having the agent improve its own state machine, you know, you're not going to get the optimal results"*(14:38~14:51) — **eval 통과 ≠ 좋은 경로.**

→ [[skill-self-improvement]] · [[production-trace-eval-flywheel]]

## 9. 필요한 루프는 하나 (15:00~15:58)

*"you don't need a special library. You don't need a special tool. In fact, this is pretty much the only loop you need"*(15:02~15:08):

```
state = initial
while not done(state):
    events = execute(effects)            # LLM 호출 · 도구 호출 · 에이전트 밖 비동기 프로세스
    state, effects = machine(state, events)   # 현재 상태 + 방금 일어난 이벤트 → 다음 상태와 실행할 효과
```

(위키의 의사코드 — 화자의 슬라이드 코드는 자막에 없다. 발화: 15:08~15:33.) `machine` 은 *"it could be XState, you could write a switch statement, a reducer function"*(15:36~15:40), *"Um coding agents are really good at updating these things regardless of whatever you use"*(15:40~15:45), *"You could use LangGraph, I guess, which actually is um one of the uh most popular tools for using state machines with agents"*(15:48~15:54).

→ [[agent-state-machine]] · [[xstate]] · [[langchain]]

## 10. 모델 → 관찰 → 제안 → 비교, 그리고 선행 연구 (15:58~17:25)

1. **model** — 상태 머신을 만든다(16:05~16:08)
2. **observe** — 일어난 모든 전이를 관찰(16:08~16:14)
3. **propose** — *"Not the exact same agent, but a different agent that's actually introspecting and looking at its own state machine"*(16:17~16:26)이 트레이스로 개선안을 낸다
4. **compare** — *"run pretty much the same uh scenarios on machine version one and machine version two"*(16:36~16:46)

선행: *"Agent Spec, AIFlow, and also even older than that, about 20 years older, process mining as well, where it's essentially the same thing. We're going over traces of events and we're distilling that into some sort of formal model, which is a state machine, and using that we're identifying where we could optimize."*(16:53~17:12) ⚠️ 세 이름 모두 미확인.

⭐ *"I'm not saying that you could use a state machine and say, 'This is the way that the agent should always run.' Instead, I'm saying, 'The state machine is how you could have the agent self-improve.'"*(17:13~17:23)

## 11. 2023 가드레일 → 2026 자기 개선 (17:25~17:48)

*"in 2023, at the last Agent Conf, I was talking about how the graph keeps the agent honest. It gives it guardrails. It gives it boundaries to work from. And in 2026, I'm talking about how using that exact same graph thinking can make the agent improve on its own behavior."*(17:26~17:44)

## 12. Jev 에스프레소 머신 데모 (17:48~20:29)

- 시점 단서 ⭐ *"A couple days ago, I was pretty much nerd sniped when Type Safe announced Jev"*(17:52~17:56), 데모는 *"last night at like 1:00 a.m."*(18:07~18:09). 2023년의 에스프레소 머신 데모(에이전트가 음료 주문을 받아 머신을 조작)를 Jev로 다시 만들었다(18:14~18:30).
- ⭐ *"this is a giant state machine under the hood, and Jev is given the exact state machine and also all of the possible events that can that the the virtual barista can do."*(18:54~19:04) — 카푸치노(*"cap"*)·에스프레소(일부러 *"expresso"* 로 오타)·코르타도 주문(19:08~19:37).
- *"it's not pre-programmed. Jev just knows like hey given uh it it's showing the likelihood over here"*(19:50~19:57) — **허용된 이벤트 중 다음 것을 확률과 함께 고른다.** 화자가 *"chaos"* 로 부품 고장을 주입(19:28~19:34), 그라인더를 고장 내자 *"Jev's going to decide while it's working I should probably fix the grinder"*(20:06~20:09).
- ⚠️ 1회 시연, 확률 수치·상태 목록은 자막에 없다. *"the creator said, 'You're absolutely correct.'"*(18:38~18:40)의 creator 미특정.

→ [[jev]] · [[system-1-model]] · [[typesafe-ai]]

## 이 위키와의 연결

### 이어지는 것

- **[[ai-slop]]** — 기존 정의 *"슬롭 = 결정의 부재"* 와 같은 방향의 **원인론**: Khourshid는 슬롭을 *구조 없는 위임* 에서 찾는다. 처방이 금지 목록·프로브가 아니라 **구조(상태·전이)** 라는 점이 새롭다.
- **[[hard-vs-soft-enforcement]]** — 프롬프트 규칙과 도구 설명은 소프트 강제, *"전이가 없다"* 는 구성상 하드 강제. Khourshid의 *"you should never write tools like this where the tool is part of the control flow"* 는 소프트 강제를 도구 설명에 숨기지 말라는 말이다.
- **[[context-rot]]** — *"the rules decay with context"* 는 컨텍스트 부패를 **프롬프트 속 규칙**에 적용한 형태. 처방은 창을 줄이는 것이 아니라 규칙을 텍스트 밖(전이)으로 옮기는 것.
- **[[skill-self-improvement]] · [[production-trace-eval-flywheel]]** — 트레이스를 개선의 연료로 쓰는 같은 계열. 다만 여기서 개선 대상은 스킬·eval 세트가 아니라 **워크플로 그래프 자체**이고, 비교 단위는 *머신 V1 vs V2* 다.
- **[[generator-evaluator-pattern]]** — 개선안을 내는 쪽은 *"Not the exact same agent, but a different agent"*(16:17~16:23).
- **[[jev]] · [[system-1-model]]** — Jev를 다룬 **세 번째 소스, 첫 외부 개발자 사용례.** System 1 모델의 *choice* 질문이 **상태 머신의 허용 이벤트 목록**과 맞물린다 — 결정론적 그래프 + 확률적 다음 이벤트 선택.

### 갈리는 것

> ⚠️ **Contradiction: 워크플로와 에이전트는 다른가.** [[workflow-vs-agent]]는 *미리 정의된 경로* vs *동적 루프* 를 축으로 나눈다. Khourshid는 *"Loops are graphs"*(02:52)라며 둘이 *"the same picture"* 라고 하고, 그 그래프를 **에이전트가 버전업한다**(V1 → V2). 이 위키의 독해: 런타임에는 경로가 고정(워크플로), 버전 사이에는 에이전트가 경로를 바꾼다(에이전트) — **축이 "누가 경로를 정하는가"에서 "언제 경로가 바뀌는가"로 옮겨 간다.** 화자는 이 구분을 직접 말하지 않는다.

> ⚠️ **"가드레일이 아니다" vs 자신의 데모.** 화자는 *"I'm not saying (…) 'This is the way that the agent should always run'"*(17:13~17:17)라지만, 이메일 데모의 핵심 가치(전송 불가능 증명)는 **가드레일 자체**다. 두 주장은 층이 다르다 — 런타임엔 가드레일, 개선 루프에선 산출물. 화자가 2023/2026으로 나눈 것은 **강조점의 이동**이지 대체가 아니다(위키의 독해).

## 해소하지 않고 표시만 한 것

- **Agent Spec · AIFlow · process mining** — 어느 프로젝트·논문인지, *"about 20 years older"* 의 기준.
- **Jev 발표일** — *"a couple days ago"* 의 절대 날짜 → 녹화일.
- **V1 → V2 diff · Stately 내부 적용 결과 · Jev 데모의 상태·확률 수치** — 자막에 없다.
- **v1 데모의 수신자 가드** 작동 여부(*"we forgot the email address"*).
- **"the creator said 'You're absolutely correct'"** 의 화자.
- **행사 도시·주최** — *"Poland"* 와 Callstack 링크뿐.

## 등장 개체

- 인물: [[david-khourshid]] (신규) · Chopin(비유, 페이지 없음)
- 조직: Stately(stately.ai — [[xstate]]·[[david-khourshid]] 페이지에서 다룸) · [[typesafe-ai|TypeSafe]] · Callstack(설명란 링크만, 페이지 없음) · Agent Conf(행사, 페이지 없음)
- 제품·모델·도구: [[xstate]] (신규) · [[jev]] · LangGraph([[langchain]]) · Agent Spec · AIFlow(페이지 없음)
- 개념: [[agent-state-machine]] (신규) · [[ai-slop]] · [[hard-vs-soft-enforcement]] · [[context-rot]] · [[workflow-vs-agent]] · [[skill-self-improvement]] · [[production-trace-eval-flywheel]] · [[generator-evaluator-pattern]] · [[system-1-model]] · [[design-pattern-state]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=D7q8fa589FY> (20:29, `upload_date` 2026-10-08)
- raw: `01.raw/articles/2026-10-08_AI 에이전트의 엉망진창 결과물(Slop)을 없애려면 '이 구조'를 도입해야 합니다.md`
- 설명란 링크: <https://clstk.com/4rrdiXJ> · <https://x.com/AgentConf> · <https://clstk.com/4hgag3F> (⚠️ 열어 보지 않았다)
- 같은 주제: [[tech-bridge-jev-agent-harness]] · [[tech-bridge-jev-calibrated-decisions]] · [[tech-bridge-taste-labs-measuring-slop]] · [[tech-bridge-lauren-tan-trusting-agents]] · [[tech-bridge-introspection-loop-is-the-product]] · [[tech-bridge-wandb-aria-self-improving-agent]]
- [[tech-bridge]] · [[david-khourshid]] · [[xstate]]
