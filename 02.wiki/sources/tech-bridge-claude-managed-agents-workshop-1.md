---
title: "Tech Bridge — Claude Managed Agents 워크숍 1부 (Priyanka · Gabe Cemaj, Anthropic): 하네스는 가정을 담고 가정은 낡는다 — 한 컨테이너의 pet에서 brain·hands·session의 cattle로, 그리고 environment·agent·session·event API"
type: source
tags: [managed-agents, brain-hands-decoupling, agent-harness-design, harness-assumptions, context-anxiety, agent-sandboxing, blast-radius, pets-vs-cattle, append-only-log, session-log, compaction, credential-injection, prompt-injection, ttft, mcp, vpc, agent-api, event-stream, custom-tools, workshop, ai-engineer, anthropic, video]
source-url: https://www.youtube.com/watch?v=3iOP4cXChAc
source-type: video
author: Tech Bridge (한영자막 재배포) · 워크숍 Priyanka([[anthropic|Anthropic]] MTS, Claude Managed Agents 엔지니어링 팀 리드 — ⚠️ **성 Phatak은 1부 자막·설명란에 없고 2부 설명란에서 옴**) · Gabe Cemaj(Anthropic MTS — en-orig *"Semach"*, 설명란 `github.com/gcemaj`, 이 편에서는 자기소개만) · [[ai-engineer|AI Engineer]] 워크숍(⚠️ 행사명은 설명란 링크에서만, 녹화일 미발화)
date-published: 2026-10-18
ingested: 2026-10-19
created: 2026-10-19
updated: 2026-10-19
---

# Tech Bridge — Claude Managed Agents 워크숍 1부 (Priyanka · Gabe Cemaj)

[[tech-bridge|Tech Bridge]]가 재배포한 **AI Engineer 워크숍의 1부, 14:39**다. 화자가 직접 *"We we have a 2-hour slot. I know they broke it down into four parts, but it's basically one long presentation."*(01:29~01:35)라고 한다. 이어지는 편은 [[tech-bridge-claude-managed-agents-workshop-2|2부(2/4)]]다. 3/4·4/4는 2026-10-19 기준 올라오지 않았다. 이 편은 콘솔 Quick Start 안내 도중(14:35)에 끊기고 Q&A는 없다. 공식 챕터는 `meta.txt` 기준 9개다.

화자는 둘이다. [[priyanka-phatak|Priyanka]]는 *"member of technical staff at Anthropic. Uh I lead the engineering team that built Claude managed agents"*(00:07~00:17)라고 자신을 소개하고 00:45 이후 전부를 말한다. [[gabe-cemaj|Gabe Cemaj]]는 *"building Claude managed agents in Priyanka's team"*(00:35~00:37)이라고 소개하는 10초만 말한다. 그는 이 위키의 [[anthropic-managed-agents]](엔지니어링 글)의 공저자다. 그러니 이 편은 **글이 적은 설계를 만든 팀이 말로 다시 하는 판본**이고, 글과 대조할 수 있다.

> **에이전트는 도구를 쓰며 루프를 도는 모델이고, 하네스는 모델이 못 하는 것에 대한 가정으로 그 루프를 감싼다. 가정은 모델이 바뀌면 낡는다. 첫 아키텍처는 session log·harness·sandbox를 한 컨테이너에 넣었고, 그 컨테이너가 잃을 수 없는 pet이 됐다. 그래서 brain(harness + Claude)을 hands(sandbox·MCP)에서 떼고 session을 append-only log로 밖에 두었다. 그러자 모든 부품이 교체 가능한 cattle이 됐다. 자격증명은 sandbox에 들어가지 않고 proxy가 주입한다. compaction은 이벤트를 버리지 않고 전략만 바꾼다. 첫 토큰까지의 시간은 약 90% 줄었다. 구현은 바꿔도 인터페이스는 남게 설계한다.**

> *"harnesses encode assumptions and assumptions can go stale. So, we designed interfaces to outlast these assumptions"* (10:29~10:38) · *"we realized we adopted a pet"* (05:22~05:24) · *"we wanted to essentially decouple the brains from the hands"* (06:59~07:03) · *"Claude actually never sees your your tokens"* (08:59~09:01)

이 위키에 새로 생기는 것은 화자 둘의 인물 페이지다([[priyanka-phatak]] · [[gabe-cemaj]], 2부와 공유). 개념은 모두 이미 있다. 이 편은 그 개념들에 **팀의 1차 구두 진술**을 붙인다.
- [[brain-hands-decoupling]]·[[managed-agents]]: 첫 아키텍처 시점(*"December of last year"*, early access)과 실패 이유 셋(디버깅·고객 데이터·VPC), TTFT 수치의 **다른 표현**(아래 Contradiction)
- [[agent-harness-design]]·[[context-anxiety]]: *"harnesses encode assumptions"*를 팀 리드가 결론으로 말한다. Sonnet 4.5 → Opus 4.5 예도 같다.
- [[context-resets-and-compaction]]: *"nothing is ever thrown away"* — compaction은 이벤트 로그를 바꾸지 않고 전략만 고른다.
- [[credential-injection-outside-sandbox]]·[[prompt-injection]]: proxy가 토큰을 주입하므로 *"you can never prompt inject Claude"* 해서 토큰을 빼낼 수 없다.
- [[agent-sandboxing]]·[[pets-vs-cattle]]: 작업마다 컨테이너 하나, blast radius. DB shard / master-replica 비유.
- [[managed-agents]]: **API 객체 넷**(environment → agent → session → event)이 처음 발화로 나온다.

ASR·ko 보정. en-orig는 Claude를 *"Cloud"*로 네 번 적는다(03:27, 03:41, 03:48, 09:47). Claude Code는 *"Claude Coder"*(01:20)·*"Cloud Code"*로, 콘솔 주소는 *"platform.clod.com"*(14:10)으로 적는다. 같은 화자가 11:14에서는 *"platform.anthropic.com"*이라고도 한다. ko는 **harness를 "끈"(03:00)·"테스트 환경"(10:10, 10:29)·"환경"(10:46)으로 옮긴다.** 그래서 결론 문장이 **"이것이 바로 테스트 환경이 필요한 이유입니다"**(10:29)로 바뀐다(`en` *"test environments encode assumptions"* 공유). 제목의 명제 *decouple the brains from the hands*는 ko에서 **"뇌를 분리한다 / 제 손을 보여드릴게요"**(07:01~07:03)가 된다. *more susceptible to prompt injection*은 **"더 좋을 거예요. / 주사에 취약함"**(08:29~08:30)이 되고, *nothing is ever thrown away*는 **"어떤 가능성도 배제되지 않습니다"**(09:13)가 된다. 전체 목록은 raw에 있다.

> ⚠️ **당사자 진술이다.** 화자는 제품을 만든 팀이다. TTFT *"about 90%"*(09:45~09:47)에는 기준·백분위가 없다. 첫 아키텍처의 실패와 새 아키텍처의 이득도 팀의 설명뿐이고 측정치는 90% 하나다.
>
> ⚠️ **이름.** Priyanka의 성은 1부 자막(자기소개 *"My name is Priyanka"*)에도 1부 설명란에도 없다. 성 *Phatak*은 [[tech-bridge-claude-managed-agents-workshop-2|2부]](`U0ZCwwG8sac`) 설명란 *"Anthropic의 Priyanka Phatak과 Gabe Cemaj"*에서 왔다. 두 편 어디에서도 발화되지는 않는다. Gabe의 성은 en-orig *"Semach"*, ko *"세마크"*다. 설명란 링크 `github.com/gcemaj`와 [[anthropic-managed-agents]] 공저자 표기 *Gabe Cemaj*에 맞춰 **Cemaj**로 읽었다.
>
> ⚠️ **행사·시점.** 행사명 AI Engineer는 설명란 링크(`ai.engineer`, `aie.codes`, `@aiDotEngineer`)에서 왔고 자막에서는 발화되지 않는다. *"December of last year"*(04:34)의 연도는 녹화 연도를 몰라 정하지 않는다.
>
> ⚠️ **슬라이드 미확인.** 아키텍처 그림(02:05, 07:09, 10:04), 이벤트 스트림 그림(12:53~13:45), 기능 목록(13:50)은 화면에만 있다. API·이벤트 이름은 **발화된 표기만** 옮겼고 문서([공식 문서](https://platform.claude.com/docs/en/managed-agents/overview))와 대조하지 않았다.

## 1. 소개와 아젠다 (00:00~01:48)

- Priyanka: *"I've been at Anthropic a little bit over 2 years. In the last 12 months I've been focused on uh building um agentic infrastructure and hope to share some of our learnings with you."*(00:21~00:31)
- Gabe: *"I've been at Anthropic a little bit over a year and I've been mostly working on this my entire time."*(00:37~00:41)
- 순서: *"a little bit of a evolution story of how we built and scaled managed agents, some of the pitfalls and the learnings"*(00:50~00:58) → 콘솔에서 *"You will not be writing any code during that part. We'll just kind of prompt our way to our first agent"*(01:08~01:14) → Gabe가 *"Claude Coder[=Code] or your favorite coding agent"*로 *"a more complex financial agent"*를 만드는 실습(01:16~01:26) → Q&A(01:26~01:29)
- 이 편에는 진화 이야기와 콘솔 안내의 시작까지만 있다.

## 2. 기본 개념 — agent · harness · sandbox (01:52~04:25)

| 개념 | 발화 |
|---|---|
| **agent** | *"agent is basically uh a model in a loop with tools. (…) the model that's deciding and taking the next action and calling tools in a loop until your task is done."*(02:01~02:12) |
| **harness** | *"a layer that wraps around the model that helps you make these tool calls in a loop (…) And it's making assumptions about what the model cannot do and trying to sort of fill those gaps. So, it's running in a loop, making tool calls, managing your context, encapsulating everything that the model cannot do."*(02:24~02:46) |
| **sandbox** | *"a place where it's going to run the code it's writing to execute the task. (…) It's able to edit files, install dependencies, etc."*(03:35~03:50) |

- **가정의 예 — context anxiety.** *"our Sonnet 4-5 model had something what we called uh context anxiety. So, whenever Sonnet 4-5 felt like you were getting to the end of the context limit, it would try to wrap up the task really quickly. So, when you're building a harness around Sonnet 4-5, you would add something like a context reset (…) But with the next model like Opus 4-5, Opus 4-5 did not have this limitation"*(02:46~03:13)
- *"when you're building a harness, you want to encapsulate all these assumptions for different models and keep up with it with every new model that comes up, which is why building a good harness is really really important"*(03:15~03:27)
- [[claude-code|Claude Code]]가 예다: *"It's a Harness century[=essentially] running locally on your computer, has access to your files"*(03:50~03:56)
- **sandbox가 필요한 이유.** *"it's also writing uh code that's untrusted. It might be buggy (…) you want your sandbox to be isolated and the blast radius to be limited. So, typically you want to execute every task in a separate container"*(03:59~04:20)

→ [[agent-harness-design]] · [[context-anxiety]] · [[claude-sonnet-4-5]] · [[claude-opus-4-5]] · [[agent-sandboxing]]

## 3. 첫 아키텍처 — 모두 한 컨테이너 안 (04:28~06:57)

- *"This was in December of last year where we shipped our first architecture to our early access customers, got a bunch of feedback, and then actually pivoted to a new architecture."*(04:32~04:42) ⚠️ 연도 미확정.
- *"we put everything in the container. So, we had the session log (…) the Harness was also running inside the container, and then the sandbox execution was also happening inside the container."*(04:51~05:07) session은 *"essentially your um unit of work"*(04:59~05:01)다.
- 장점: *"there was no service boundaries to design for. Everything was local, um easy to edit. File edits were essentially just like sys calls."*(05:11~05:17)
- ⭐ *"But what happened was we realized we adopted a pet."*(05:22~05:24) 비유 설명: pet은 *"a named and hand-tended entity. When it gets sick, you have to nurture it back to life"*(05:33~05:39), cattle은 *"more interchangeable, more disposable"*(05:44~05:46). 예: 단일 DB shard가 죽으면 제품이 죽는다(pet), master-replica면 replica를 올린다(cattle)(05:48~06:01).

| 문제 | 발화 |
|---|---|
| 디버깅 | *"a a dropped packet, a dead container would show up very similarly, and we had to essentially like web socket stream into the container to debug."*(06:18~06:25) |
| 조사 | *"investigating was hard because customer data would live on these containers. So, we didn't have a way in, essentially, to go in and debug."*(06:31~06:38) |
| 고객 VPC | *"if a customer wanted a connect to, let's say, an MCP in their VPC, it meant peering networks or shipping them our harness and having them run it."*(06:42~06:52) |

→ [[pets-vs-cattle]] · [[model-context-protocol]]

## 4. Brain과 hands를 떼다 — 세 인터페이스 (06:59~08:19)

- ⭐ *"what we decided that we wanted to essentially decouple the brains from the hands"*(06:59~07:03)
- *"the agent essentially became three separate interfaces."*(07:07~07:10)

| 인터페이스 | 발화 |
|---|---|
| **session** | *"essentially an append-only log of everything that has happened in the session so far."*(07:12~07:18) |
| **brain** | *"that's your harness or the agent loop along with Claude."*(07:19~07:24) |
| **hands** | *"sandboxes, your MCP tool calls, etc. Provisioned on demand, uh gone when the work is done, and if you need if you lose a sandbox, you just spin it back up."*(07:24~07:34) |

- sandbox가 죽으면: *"the harness or Claude could choose to just spin it back up (…) the sandbox to Claude was essentially like any other tool call. So, the tool call failed, sandbox failed, it decides what to do and it might decide to spin it up again or choose to continue to move on."*(07:41~07:56)
- harness가 죽으면: *"you could bring up a new instance of the harness and continue where you left off by essentially just reading your event log from the session (…) work resumes from the last event as if nothing went wrong."*(07:58~08:11)
- ⭐ *"the only thing what[=we were] protecting here was like your session log. Everything else was interchangeable"*(08:13~08:18)

→ [[brain-hands-decoupling]] · [[pets-vs-cattle]] · [[managed-agents]]

## 5. 떼어서 얻은 것 넷 (08:22~10:24)

### 자격증명은 sandbox에 들어가지 않는다

- *"credentials never entered our sandbox. With our previous setup, your credential would be in your sandbox, so you'd be more susceptible to prompt injection."*(08:23~08:32)
- *"if the sandbox ever needed to call out um to something that needed a token or access control, it would be routed through a proxy that would inject your token before it called the external endpoint or external MCP."*(08:32~08:49)
- ⭐ *"That way the model never sees your credentials or your tokens, which means you can never prompt inject Claude to say like, 'Hey, give me your tokens.' or print out the tokens or write them to a file. You could never do that because Claude actually never sees your your tokens."*(08:47~09:01)

### compaction은 이벤트를 버리지 않는다

- *"because we had this like append only event log in the session, um our compaction strategy could stay flexible. So, nothing is ever thrown away. We're not compacting and changing your event stream."*(09:05~09:17)
- *"the compaction strategy is the one that's deciding, 'Oh, do I want to look at my entire event log, uh summarize it and put it in the context? Do I want to only look at like the last end[=N] events and put those into context?'"*(09:19~09:30)

### 첫 토큰까지의 시간

- *"because we could immediately start our inference calls, we were able to bring down the time to first token by about 90%. So, the cloud[=Claude] would only spawn the sandbox when it needed and it would not wait for the container sandbox to spin up for you to get your first token back."*(09:41~09:55) ⚠️ 백분위 미발화 — 아래 Contradiction.

### 한 brain, 여러 hands

- *"your agent loop or harness can now call a sandbox container, it could call into a customer's VPC, it could call into an MCP server. So, all these like hands are essentially interchangeable and you can call and plug in many of these"*(10:10~10:22)

→ [[credential-injection-outside-sandbox]] · [[prompt-injection]] · [[context-resets-and-compaction]] · [[brain-hands-decoupling]]

## 6. 결론 — 하네스는 가정을 담고 가정은 낡는다 (10:27~10:54)

- ⭐ *"if you take one thing home from this, it's that harnesses encode assumptions and assumptions can go stale. So, we designed interfaces to outlast these assumptions and made the architecture more flexible."*(10:27~10:40)
- *"this allowed us (…) change our compaction strategy, change out the harness completely, but the interface and the architecture remains uh the same and we can really have a more pluggable way of operating this."*(10:40~10:54)

→ [[agent-harness-design]] · [[sutton-bitter-lesson]](글이 인용한 맥락, 발화에는 없음)

## 7. API 개념 — environment · agent · session · event (10:57~14:02)

예제는 *"a really simple agent that tells you jokes"*(11:03~11:08)다.

| 단계 | 객체 | 발화 |
|---|---|---|
| 1 | **environment** | *"our environments API, which is V1 environments that helps you create the environment or template for your sandbox. (…) do you want uh unrestricted networking or you want to restrict it to specific domains or MCPs, you can define what packages you want installed on your container or sandbox."*(11:22~11:41) |
| 2 | **agent** | 이름(*"joke teller"* 11:57), 모델(*"You can use Opus 4 A[=?], you can use Haiku or Sonnet, your choice."* 12:01~12:05), 시스템 프롬프트(*"you're a comedian, find a fresh joke on the topic, deliver it well."* 12:11~12:15), 도구(*"agent tool set, which is sort of like our basic tool set. This is like your bash tool set, read, write, grep, etc. And you almost all agents will need need this."* 12:20~12:29) |
| 3 | **session** | *"session takes an agent ID and environment ID and creates a session. This is your task unit of work or your task. And when the session is provisioned, it's idle. No work has been done, right? Until you send an event."*(12:36~12:48) |
| 4 | **events** | *"You're going to have events that you send and then events that the agent will come back to you with."*(12:57~13:00) |

발화된 이벤트(⚠️ 표기는 발화 그대로, 문서 미대조):
- *"user.message"* — *"tell me a joke about distributed systems"*(13:02~13:06)
- **custom tool** — *"Custom tool essentially lets you define a custom tool that you want to handle (…) Claude will essentially put a custom tool use event on your event stream that you can listen to and then you can process that event and then return the result to Claude as custom tool result."*(13:09~13:25)
- *"session.error"*(13:31~13:34), *"Status idle is when your session is idle and not working"*(13:35~13:39), *"interrupt (…) is when you want to stop or kill the session"*(13:43~13:47)
- 다중 에이전트·메모리는 Gabe의 편으로 넘긴다: *"going deeper into some of like these concepts like multi-agent and memory that we also provide."*(13:58~14:02) → [[tech-bridge-claude-managed-agents-workshop-2]]

→ [[managed-agents]] · [[agent-memory]]

## 8. 콘솔 Quick Start로 (14:06~14:35, 끊김)

- *"we're going to hop over now to platform.clod.com[=claude.com]. Um, and hopefully you can use your API credits"*(14:08~14:15)
- *"if you go to your console, you'll see in this manage agent section there is something called as a quick start. This is sort of like our um, guided tour of how to build your first agent."*(14:25~14:35) — 여기서 영상이 끝난다.

## 이 위키와의 연결

### 이어지는 것

- **[[anthropic-managed-agents]]와 대부분 같다.** 세 인터페이스(session·harness·sandbox), pet → cattle, sandbox 사망을 tool-call 실패로 Claude에게 넘김, harness 사망 시 session log에서 재개, 자격증명을 sandbox 밖 proxy로, compaction을 session 밖의 결정으로 둠, "many hands", *"harnesses encode assumptions"*가 모두 글과 같다. 글은 OS 비유·함수 시그니처(`execute`, `wake`, `getEvents`)·Git 토큰 패턴·Bitter Lesson을 더 말한다. 발화는 그 대신 **첫 아키텍처의 시점(*"December of last year"*, early access)**과 **조사 문제**(*"customer data would live on these containers"*)를 말한다.
- **[[managed-agents]]: 왜 갈랐나의 두 번째 1차 진술.** [[tech-bridge-claude-platform-agent-era]]에서 [[katelyn-lesse]]는 분할 이유를 **수명 주기 불일치**(sandbox 기술은 일시적 용도로 설계됨)로 말했다. 이 편의 이유는 **운영 문제 셋**(구분 안 되는 장애, 고객 데이터 때문에 못 들어감, VPC peering)이다. 서로 모순되지 않고 같은 결정의 다른 면이다.
- **[[agent-harness-design]]: 정의가 둘로 나뉜다.** Katelyn은 *"하네스는 while 루프"*라고 했다. 이 편은 **agent = 도구를 쓰며 루프를 도는 모델**, **harness = 모델이 못 하는 것에 대한 가정으로 그 루프를 감싸는 층**으로 나눈다. 루프 자체보다 **가정**이 하네스의 정체라는 쪽에 무게가 있다.
- **[[context-anxiety]]**: Sonnet 4.5 → Opus 4.5 예가 글과 같은 순서로 다시 나온다. 팀이 이 예를 **대표 사례로 고정해 쓰고 있다**는 기록이다.
- **[[credential-injection-outside-sandbox]]**: 동기는 [[prompt-injection]]이라고 분명히 말한다(*"more susceptible to prompt injection"*). 이 페이지의 비교표에서 Managed Agents 행의 동기와 같다.
- **[[agent-sandboxing]]·[[tech-bridge-openhands-sandboxing-coding-agents|OpenHands 편]]**: *"execute every task in a separate container"*와 blast radius는 Brennan의 세션당 pod와 같은 처방이다. 이 편은 그것을 **에이전트를 호스팅하는 쪽**에서 말한다.
- **[[brain-hands-decoupling]]의 다른 회사 판본들**([[tech-bridge-vercel-rauch-agentic-workflow|Vercel]], [[tech-bridge-lee-robinson-always-on-agents|Lee Robinson]])에 원 출처 팀의 구두 판본이 더해진다.

### 갈리는 것

> ⚠️ **Contradiction(표현): TTFT 감소 폭.** [[anthropic-managed-agents]]·[[brain-hands-decoupling]]·[[managed-agents]]는 글을 따라 **p50 TTFT 약 60% 감소, p95 90% 이상 감소**로 적는다. 이 편은 *"we were able to bring down the time to first token by about 90%"*(09:43~09:47)라고만 말한다. 백분위를 말하지 않으니 p95 값만 전한 것일 수 있다. 하지만 들은 사람은 중앙값이 90% 줄었다고 읽기 쉽다. **위키는 글의 p50/p95 표기를 유지하고, 발화는 "백분위 없는 약 90%"로 기록한다.**

> **sandbox를 다시 띄우는 주체.** 글은 컨테이너 사망을 tool-call 오류로 바꿔 **Claude가** 재시도를 결정한다고 쓴다. 발화는 *"the harness or Claude could choose to just spin it back up"*(07:41~07:45)이라고 주체를 둘로 열어 둔다. 바로 뒤에서는 *"it decides what to do"*라고 Claude 쪽으로 설명한다. 모순이라기보다 발화가 덜 엄밀한 것으로 본다.

> **긴장: sandbox 안의 비밀.** [[credential-injection-outside-sandbox]]에 이미 기록된 OpenHands의 처방(필요한 비밀만 sandbox에 마운트)과 이 편의 *"credentials never entered our sandbox"*(08:23~08:26)는 갈린다. 새 내용은 아니고 기존 긴장을 원 출처 팀이 한 번 더 확인한 것이다.

## 해소하지 않고 표시만 한 것

- *"Opus 4 A"*(12:01)의 버전. 이 위키에 4.8 페이지는 없고 판독도 보류했다.
- *"V1 environments"*·*"agent tool set"*·*"Status idle"*·*"interrupt"*의 정확한 API 표기. 문서와 대조하지 않았다.
- *"December of last year"*의 연도. 녹화 시점.
- *"platform.anthropic.com"*(11:14)과 *"platform.clod.com"*(14:10) 중 콘솔 주소. 설명란 문서 링크는 `platform.claude.com`이다.
- Priyanka의 성 *Phatak*은 2부 설명란 표기뿐이다(발화 없음). Gabe의 성 *Semach*/*Cemaj*의 동일성(이름·소속·링크 일치로 판단).
- *"It's a Harness century"*(03:51)의 *century*.
- 슬라이드 내용(아키텍처 그림, 이벤트 스트림 그림, 기능 목록).

## 등장 개체

- 인물: [[priyanka-phatak|Priyanka]](⚠️ 성은 2부 설명란에서만) · [[gabe-cemaj|Gabe Cemaj]](en-orig *"Semach"*) · Travis(진행 스태프, 페이지 없음)
- 조직: [[anthropic|Anthropic]] · [[ai-engineer|AI Engineer]](설명란 링크에서만)
- 제품·모델: [[managed-agents|Claude Managed Agents]] · [[claude-code|Claude Code]](en-orig *"Claude Coder"*·*"Cloud Code"*) · [[claude-sonnet-4-5|Sonnet 4.5]] · [[claude-opus-4-5|Opus 4.5]] · Opus *"4 A"*(⚠️ 판독 보류) · Haiku·Sonnet(버전 미발화) · Claude 콘솔(Quick Start, 페이지 없음)
- 개념: [[brain-hands-decoupling]] · [[agent-harness-design]] · [[context-anxiety]] · [[context-resets-and-compaction]] · [[agent-sandboxing]] · [[pets-vs-cattle]] · [[credential-injection-outside-sandbox]] · [[prompt-injection]] · [[model-context-protocol]] · [[agent-memory]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=3iOP4cXChAc> (14:39, `upload_date` 2026-10-18)
- raw: `01.raw/articles/2026-10-18_Anthropic Claude Managed Agents - 두뇌와 손을 분리한 설계 (1부).md`
- 같은 워크숍: [[tech-bridge-claude-managed-agents-workshop-2]] (2/4, `U0ZCwwG8sac`)
- 같은 설계의 글: [[anthropic-managed-agents]] · 같은 팀의 대담: [[tech-bridge-claude-platform-agent-era]] · [[tech-bridge-tokens-should-have-jobs]] · [[tech-bridge-anthropic-dreaming-memory]]
- 설명란 링크: [Claude Managed Agents 문서](https://platform.claude.com/docs/en/managed-agents/overview) · [Anthropic 엔지니어링 글](https://www.anthropic.com/engineering/managed-agents) · <https://aie.codes> · <https://github.com/gcemaj> (⚠️ 열어 보지 않았다)
- [[tech-bridge]] · [[priyanka-phatak]] · [[gabe-cemaj]]
