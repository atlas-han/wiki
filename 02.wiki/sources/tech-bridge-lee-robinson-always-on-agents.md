---
title: "Tech Bridge — Grok Bot 같은 상시 작동 에이전트는 어떻게 작동할까 (Lee Robinson · SpaceX, Stanford 강의): 서버에서 자고 깨는 루프, 단일 도구 send user, durable workflow, prompt caching, 캐시가 따뜻할 때 compaction"
type: source
tags: [always-on-agents, persistent-agents, grokbot, agent-harness, thin-client, firecracker, durable-execution, temporal, job-queue, message-priority, tool-search, escalation-ladder, computer-use, accessibility-tree, subagents, auto-review, prompt-injection, prompt-caching, context-engineering, compaction, agent-memory, training-flywheel, sft, reinforcement-learning, evals, delete-the-product, spacex, cursor, stanford, lecture, video]
source-url: https://www.youtube.com/watch?v=N8gD8ebFlMI
source-type: video
author: Tech Bridge (한영자막 재배포) · 강의 Lee Robinson([[spacex|SpaceX]] — **자막에는 "I'm Lee"만**, 성·직함·스탠퍼드 CS146S는 제목·설명란) · 수업 강의(발화 — week one, last lecture, last week) · 녹화일 미발화
date-published: 2026-10-17
ingested: 2026-10-18
created: 2026-10-18
updated: 2026-10-18
---

# Tech Bridge — Grok Bot 같은 상시 작동 에이전트는 어떻게 작동할까 (Lee Robinson · SpaceX)

[[tech-bridge|Tech Bridge]]가 재배포한 **45:17 단독 강의**다. 공식 챕터는 없다. 질문 시간을 두 번 약속하지만(02:28~02:30, 43:21~43:26) 영상은 45:14 박수에서 끝난다. 화자는 *"So, as mentioned, I'm Lee."*(00:00)라고만 말한다. 성 Robinson, "SpaceX 엔지니어", 스탠퍼드 CS146S는 제목·설명란에만 있다. 소속 단서는 *"We're working on at SpaceX"*(00:17~00:19)와 *"one of the principles that we had at Cursor uh and now at SpaceX"*(37:45~37:52)다. 이 위키는 [[lee-robinson|Lee Robinson]](신규 제안)으로 적는다.

제목은 *"Grok Bot 같은"*이라고 하지만 화자는 **자기가 만드는 [[grokbot|GrokBot]]의 구조를 1인칭으로** 설명한다(*"how we built this architecture, how we built the harness"* 02:10~02:13, *"The biggest difference with the Grockbot[=GrokBot] harness"* 18:21~18:23). 이 위키가 GrokBot을 사용자 쪽(봇 팀·바깥 루프)에서만 보아 왔다면, 이번에는 **안쪽 설계**가 처음 나온다. 테제는 다음과 같다.

> **수업에서 만든 하네스(모델이 루프에서 도구를 부른다)는 노트북을 닫으면 멈춘다. always-on agent는 그 루프를 서버로 옮기고, 자기 컴퓨터(VM)를 따로 주고, 사람의 프롬프트 말고도 Slack·이메일·루틴이 깨우게 하며, 동료처럼 중요할 때만 말을 건다. 이것을 받치는 것은 새 이론이 아니라 오래된 인프라 부품이다. thin client와 thick server, 재우고 깨우는 VM, 재시도해도 안전한 durable workflow, 우선순위 큐가 그렇다. 하네스 안에서는 컨텍스트를 아낀다. 도구는 이름만 싣고, 무거운 일은 helper에게 넘기고, 프롬프트 접두는 고정해 캐시를 지키고, 캐시가 따뜻할 때 미리 요약한다. 모델은 지금이 가장 못한 때이니 제품을 지울 각오로 다음 세대 모델을 위해 만든다.**

> *"this type of always on agent is more like a colleague where it doesn't always immediately send you a message. It knows when to be quiet."* (01:27~01:36) · *"if you put the agent loop on the virtual machine, then you can't shut down the virtual machine independently from the uh from the agent server."* (14:53~15:06) · *"what you really want here is you want a durable workflow, which means that it's safe for you to actually retry that."* (16:51~16:59) · *"if there's a cash cache miss, it's kind of like a bug in the system really."* (29:51~29:55) · *"you kind of have to internalize and assume that the models today are the worst they'll ever be."* (37:54~38:00)

이 위키에 개념 둘이 생긴다. [[always-on-agent-architecture]](신규 제안)는 서버·VM·트리거·큐·단일 도구로 이루어진 상시 에이전트의 골격이다. [[prompt-caching]](신규 제안)은 지금까지 여덟 페이지에 흩어져 있던 캐시 이야기를 이 강의의 기법 다섯으로 모은다. 나머지는 기존 페이지에 붙는 **새 증언**이다.
- [[brain-hands-decoupling]]: 루프를 VM 밖에 두는 이유. Anthropic Managed Agents와 같은 결론을 **다른 회사가 운영 이유(제로데이 패치·다운타임)로** 낸다
- [[durable-execution]]·[[temporal]]: 벤더가 아닌 **사용자**의 첫 증언(*"we use an open source uh tool called Temporal"* 17:08~17:11)
- [[deferred-tool-context]]: tool search, 그리고 그 페이지가 미해결로 둔 캐시 질문에 대한 한 가지 답(턴 중에는 도구를 바꾸지 않는다)
- [[context-resets-and-compaction]]: 캐시가 따뜻할 때 compaction한다
- [[agent-memory]]: core facts · dated logs · scratchpad · 파일의 층
- [[persistent-agent-teams]]·[[grokbot]]·[[spacex]]: 같은 제품의 안쪽, 그리고 SpaceX에서 봇이 회의에 대신 들어간다는 진술
- [[transcript-classifier]]: auto review가 사람 승인보다 안전하다는 주장(⚠️ 근거 없음)

ASR·ko 보정. ko는 **설계 근거를 네 번 뒤집는다.** *there's not enough computers in the world* → **"세상에는 충분한 컴퓨터가 있습니다"**(10:57), *rebuild that and not (…) blow away the entire agent loop* → **"에이전트 사이클 전체를 파괴하고 시스템 다운타임을 유발합니다"**(15:17~15:22), *you don't feel a degradation of the model's quality* → **"모델 품질이 향상됩니다"**(24:32), *It's more important than ever to think about the broader system design* → **"그것에 대해 절대 생각하지 않는 것이 중요합니다"**(43:30)다. 같은 방향의 반전이 더 있다.
- *they basically couldn't call tools very well* → **"그들은 도구를 아주 잘 다룰 줄 알았다"**(07:23)
- *I don't think that we have it perfect yet* → **"우리는 완벽한 것들을 가지고 있고"**(41:19)
- *if I would have given this talk six months ago* → **"이 대화는 6개월에서 1년 전에 있었던 일입니다"**(38:09)

ko는 단위도 바꾼다(*6 to 12 months* → **"6~12일"** 38:38, *trillions* → **"수십억 명"** 43:05). 용어 오역으로는 Temporal → **"임시직"**(17:10), Firecracker → **"폭죽"**(12:26), pre-training → **"운동 전 보충제"**(34:41), compaction → **"다짐"**, memory → **"추모"**(32:54), inner/outer loop → **"악순환"**(36:41~36:44), Hugging Face → **"포옹 얼굴"**(37:22), little optimizations → **"어린아이들"**(31:19)이 있다. `en`은 이 자리들을 대부분 바르게 옮겼다. en-orig는 GrokBot을 *"Grockbot"*·*"open grobbot"*으로 적는다. 전체 목록은 raw에 있다.

> ⚠️ **당사자 설명이고 측정치가 없다.** 화자는 자사 시스템을 설명한다. 사용자 수, 지연, 비용, 캐시 적중률, 실패율 같은 수치는 하나도 없다. 숫자는 예시와 전망이다. *"a 200,000 token context window"*(31:41~31:44), 캐시 창 *"Maybe it's 10 minutes, maybe it's 60 minutes"*(32:17~32:19), *"90% of its time"*(25:59), *"in the next 6 to 12 months"*(38:38~38:40)가 그 예다.
>
> ⚠️ **근거 없는 비교 주장 둘.** ① auto review: *"that's actually more secure than the fatigue of having to watch hundreds of shell commands (…) if you did a blind test (…) most of the time the the model's actually doing a better job."*(05:13~05:30) 누가 한 어떤 test인지 없다. ② 환각: *"you don't really hear people talk about hallucinations anymore because it's kind of a solved problem mostly."*(07:26~07:30)
>
> ⚠️ **이름·직함·학교는 설명란 기준이다.** 녹화일은 발화되지 않는다. 단서(*"January of this year (…) when OpenClaw was really getting popular"* 29:59~30:06, *"moldbook[=Moltbook] or the hugging face incident"* 37:21~37:23, *"at Cursor uh and now at SpaceX"* 37:48~37:52)로 보아 2026년 하반기로 보이지만 추정이다. 영상은 *"as mentioned"*로 시작해 앞의 소개가 잘려 있다.
>
> ⚠️ **en-orig 공백 하나.** 36:55→36:59 사이에 *"climbing on the eval"* 다음 말이 빠져 있다. ko·`en`은 그 자리에 문장을 갖지만 이 위키는 그것으로 메우지 않는다.

## 1. 도입 — 노트북을 닫으면 멈춘다 (00:00~02:34)

- *"this new category of always on proactive persistent agents"*(00:03~00:07). *"some of the things we'll talk about are in progress. We're working on at SpaceX."*(00:16~00:19)
- 출발점은 수업의 하네스다. *"you have a model. It can call tools in a loop. And that's actually very powerful."*(00:29~00:32) 단점은 *"you close your laptop and the process stops."*(00:38~00:41)
- always-on agent: *"this can run on a server. It can run in the cloud. You can close your computer. Uh it can restart. It can survive crashes."*(00:55~01:01) *"this agent has its own computer. So not just your laptop, but a Linux machine in the cloud where it has its own desktop files, browser"*(01:01~01:10). 시간이 지나며 *"build up a memory of how you work with it"*(01:19~01:21)이다.
- ⭐ *"this type of always on agent is more like a colleague where it doesn't always immediately send you a message. It knows when to be quiet. Sometimes it might just want to work in the background a little bit and only come back to you when there's an important update."*(01:27~01:41)
- 트리거: *"it can be triggered more than just you typing (…) Maybe there was a Slack message or an email or some other type of event that wakes up this agent"*(01:41~01:51)
- 지평: *"not just hours or days, but maybe even weeks or months. And that just requires a little bit of a different architecture"*(01:59~02:07)

→ [[always-on-agent-architecture]](신규) · [[persistent-agent-teams]] · [[cloud-agent-delegation]](노트북을 닫아도 돈다는 같은 출발점) · [[agent-attention-management]]

## 2. 네 시대, 그리고 지금의 조작 방식 (02:34~06:13)

| 시대 | 발화 |
|---|---|
| 1 | *"copy pasting code out of chat GBT[=ChatGPT] and putting it into your editor of choice"*(02:45~02:51) |
| 2 | 단순한 하네스로 *"edit files, run shell commands"*(03:05~03:08), 터미널 |
| 3 | 코딩 에이전트에 *"dedicated apps"*(03:29), *"many agents in parallel. Maybe they're running them in the cloud"*(03:31~03:37). 그래도 *"you were kind of the bottleneck in that you were reviewing every command"*(03:39~03:43) |
| 4 | *"always on agents and they can kind of run ambiently in the background where they have their own computer, they have their own memory, they learn new skills on the job, and they keep working after you go, you know, go to bed"*(03:54~04:07) |

- 조작이 프롬프트·대기에서 **steering**으로 바뀌었다: *"instead of kind of queuing commands, you can steer the agent and you might say, 'Hey, go check this thread.' and then immediately after, oh, by the way, you know, actually go do that on Thursday."*(04:29~04:41) 예전 모델은 끼어들면 헷갈렸지만 *"now they kind of understand just like how you might ramble on talking to a friend"*(04:46~04:51)이다.
- ⚠️ auto review: *"additional safety checks in place which a lot of companies are calling auto review which is essentially a separate AI model that's checking all of the commands that get run."*(05:02~05:10) *"more secure than the fatigue of having to watch hundreds of shell commands"*(05:13~05:20), blind test에서 모델이 대체로 낫다(05:21~05:30). 근거·회사 이름은 발화되지 않는다.
- *"kind of paradoxically, but as the models have gotten better, the interface has gotten quite a bit more simple actually. And this type of always on agent we're calling a bot."*(05:30~05:43) 이유는 *"we all know how to text"*(05:52~05:54)이고, 이제는 *"actually going and doing longer tasks like you would hand off to a co-orker[=coworker]"*(06:09~06:13)다.

→ [[transcript-classifier]]·[[anthropic-claude-code-auto-mode]](같은 장치 — 이 강의는 이름을 "auto review"라고 부른다) · [[steering-altitude]] · [[agent-trust-curve]]

## 3. 모델의 여섯 변화 — 파일·스킬·플러그인·루틴 (06:13~10:03)

화자는 *"I'll go over six"*(06:20)라고 하지만 서수는 *"The first one"*·*"Two"*·*"finally"*만 발화된다. 아래 여섯의 경계는 이 위키의 읽기다.

1. 긴 지시 이행: *"models can pretty confidently run for hours or days with the right uh compression and compaction"*(06:35~06:41)
2. 서브에이전트: 작업 기억이 차므로 *"hand off to these helpers that have a fresh set of working memory and that effectively can give it an unlimited context basically"*(06:59~07:08)
3. 도구 호출: *"just a few years ago, they basically couldn't call tools very well and they would hallucinate all the time."*(07:21~07:26) ⚠️ 이어서 *"you don't really hear people talk about hallucinations anymore because it's kind of a solved problem mostly."*(07:26~07:30)
4. 강력한 도구와 computer use: *"any SAS[=SaaS] product or any website that didn't expose an API or an MCP server can be used headlessly basically"*(07:55~08:06)
5. 파일: *"store all of the information in files (…) it's actually very easy for the models then to recall and search this information"*(08:11~08:17). 예: 모든 프롬프트에 들어가는 사용자 프로필(소문자로 쓰는 취향 08:46~08:50), 매일의 working log, *"the models are very good at using Linux commands, running shell commands to go GP[=grep] and search"*(09:11~09:15)
6. 보여 주면 배운다: *"you can just kind of show the bot how to do some work and it will kind of turn that into skills or memories or routines"*(08:19~08:28)

- 스킬: *"taking your knowledge of how to do a specific task and encoding it into a markdown file"*(09:20~09:26). *"a whole ecosystem now of companies and developers um writing these skills"*(09:34~09:41)
- ⭐ GrokBot: *"in Grockbot[=GrokBot] there is a whole system of plugins. So basically any tool that you want to use there's a plugin you can install which uses skills or servers and then also routines which if you're familiar with cron jobs you know you're running some prompt basically on some kind of schedule"*(09:45~10:01)

→ [[agent-skills]] · [[mcp-skill-distribution]](플러그인 = 스킬 또는 서버) · [[scheduled-agent-automations]](루틴) · [[file-system-agent]] · [[skill-self-improvement]] · [[preference-reward-asymmetry]](환각 주장 — 아래 "갈리는 것")

## 4. always-on의 내부 — 재우고 깨우고, 알릴지 고른다 (10:03~13:31)

- ⭐ sleep/wake: *"it starts out with the server being asleep and also this computer that the agent can use being asleep"*(10:19~10:26). 메시지나 트리거가 오면 *"loading up and booting up all of the state for this agent. And it's running on a server."*(10:35~10:41) 컴퓨터가 필요할 때만 켜고, 끝나면 *"put those to sleep"*(10:52~10:54)한다.
- 이유: *"It would be, you know, expensive and also uh there's not enough computers in the world to just have those computers running all of the time uh for everyone"*(10:54~11:02). 상태는 *"a database the the conversation logs the memories the routines"*(11:06~11:12)에 남는다.
- 트리거: Slack 멘션, 전화·회의, 몇 시간·며칠 걸린 백그라운드 루틴의 결과(11:25~11:52). ⭐ *"It's increasingly common now at SpaceX where we see bots joining meetings for employees where they couldn't make it to the meeting, but they want their bot to go and just take notes and come back to them"*(11:33~11:43)
- ⭐ router와 알림 heuristic: *"Then we have basically a router that ddupes[=dedupes] that and figures out how to put it into the conversation. And then it's has this heristic[=heuristic] of do I need to bug the user about this or not? Because not everything is actually important."*(11:53~12:06) 기준은 동료다. 진척마다 와서 보여 주면 *"pretty annoying"*이고 *"You really only need a status update maybe, I don't know, every day depending on the task."*(12:13~12:18)
- ⭐ 컴퓨터: *"this is running a firecracker virtual machine. And the reason this is really helpful is because it's it's very easy then to essentially snapshot the state of the machine and shut it down and start it back up."*(12:24~12:36) 사용자가 *"live view"*로 들어가 직접 조작할 수 있다(12:39~12:44). 개인 노트북이 아니라 *"this other environment that is you know secured and locked down"*(12:50~12:54)에서 셸을 돌린다. 봇 5개·10개가 각자 브라우저를 쓰도록 virtual desktop을 두고 *"shared infrastructure between these bots"*(13:00~13:13)로 쓴다.

→ [[always-on-agent-architecture]] · [[agent-attention-management]](알릴지 말지 heuristic — ⚠️ 41:12~41:20에서 화자 스스로 미완성이라고 한다) · [[pets-vs-cattle]](snapshot·재기동) · [[agent-sandboxing]](노트북이 아닌 잠긴 환경)

## 5. 서버 — 큐, 루프, thin client와 thick server (13:31~15:27)

- *"commands will come in, they get put into this queue, and then it calls the purple box, which is the agent loop. And this is what we covered last week"*(13:34~13:42). 내릴 때 상태를 DB·저장소에 남긴다(13:46~13:50). *"there's this one kind of small piece that can then have all of these abstractions built on top"*(13:53~13:58)
- *"a pretty common practice in computing where you want to have kind of a thin client and a thick server. And computing has kind of oscillated between these things over the years."*(14:10~14:18) 이유 셋: 앱 스토어 업데이트 없이 서버만 배포(14:20~14:31), 전사·이미지 생성 같은 무거운 계산(14:33~14:41), 이미 아는 서버 확장법(14:44~14:52)
- ⭐ *"the most critical thing here is that if you put the agent loop on the virtual machine, then you can't shut down the virtual machine independently from the uh from the agent server. So yeah, you want to save everything on the server. Um, so you can always kind of rebuild that virtual machine. For example, let's say you need to do some critical zero day Linux uh update on the on the VM. Well, it would be great to be able to rebuild that and not, you know, blow away the entire agent loop and have downtime in the application."*(14:53~15:24)

→ [[brain-hands-decoupling]](⭐ 같은 분리, 다른 이유) · [[always-on-agent-architecture]] · [[pets-vs-cattle]]

## 6. 메시지 경로 — job queue 대 durable workflow, 우선순위 (15:27~18:08)

- 보내기: 클라이언트가 즉시 ack하고, 턴은 루프로 돌아 DB에 저장되며, 클라이언트는 서버 신호를 구독하다가 신호가 오면 최신을 가져온다. 재시도로 같은 메시지가 두 번 보이지 않게 dedupe한다(15:43~16:17). *"strong versus eventual consistency"*(15:39~15:41)는 주제로만 언급한다.
- ⭐ *"the like underlying infrastructure primitives to think about here (…) is a workflow versus a job queue."*(16:17~16:27) 일반 큐에서 3단계 도중 인프라 문제로 죽으면 *"now you have to replay steps one, two, and three"*(16:43~16:50)다. *"what you really want here is you want a durable workflow, which means that it's safe for you to actually retry that. And when you retry after a failure, it picks right up on step three."*(16:51~17:03)
- ⭐ *"this is like kind of a solved problem in some ways in um distributed systems and in infrastructure. So, we use an open source uh tool called Temporal (…) so that we don't have to rebuild a lot of this very complicated stuff from scratch. Of course, you still have to run the infrastructure for it"*(17:03~17:19)
- 우선순위: 내 DM이 그룹 채팅·Slack 스레드·백그라운드 루틴보다 앞선다. *"if I say, 'Oh, actually, you know, change the date for this event.' we actually want that agent loop to stop and my message is going to have priority over everything else"*(17:38~17:47). 나머지는 줄 뒤로 간다. 메시지 서너 개가 빨리 오면 *"batch those together so it's just one turn"*(17:58~18:01)이다.

→ [[durable-execution]] · [[temporal]] · [[agent-distributed-systems]] · [[human-as-async-api]](같은 primitive를 사람 대기에 쓰는 쪽)

## 7. 하네스 — 단일 도구 send user (18:08~19:58)

- ⭐ *"The biggest difference with the Grockbot[=GrokBot] harness um and probably some of the other tools like this uh on the market is the way we've done the thin client fix[=thick] server architecture is there's only one tool that communicates between the client and the server and it's just send user."*(18:21~18:39)
- *"the client is just texting the server in some ways and you're putting a lot of these heavier tools on the server"*(18:44~18:50). 서버 도구는 셸, 파일 읽기, *"calling on a cloud agent or recording your screen or doing demos"*(18:52~18:58)다. 그래서 모바일 앱·데스크톱 앱·이메일·Slack 어디에 클라이언트를 새로 붙여도 이 도구 하나로 통한다(19:01~19:13).
- 클라이언트는 받은 것을 풍부하게 그린다(19:15~19:58): 로그인 폼과 1Password, 결제는 Stripe Link·X Money, ⭐ *"if you're trying to do something that is non you can't reverse it sending an email or a Slack message, it might come back and ask you to you know edit and approve a draft before you send it."*(19:42~19:53), 메시지가 필요 없으면 이모지 반응.

→ [[always-on-agent-architecture]] · [[action-reversibility]] · [[no-silent-write]] · [[agent-native-interface]]

## 8. 컨텍스트를 아끼는 사다리 둘 (19:58~23:30)

- tool search: MCP 커넥터를 깔수록 도구 이름·스키마가 창을 채운다(20:26~20:44). *"one kind of context engineering or harness trick um that a lot of the the popular harnesses now use is uh it's called dynamic context or I think uh some other folks call it the tool search tool (…) you're only putting the names of the tools into the every message that gets sent to the model"*(20:51~21:11). 나머지는 *"files and a file system all the way down"*(21:18~21:21)이다.
- ⭐ "가장 싼 것부터": *"the principle here really is to try the cheapest option or the most reliable option first and kind of work your way up the ladder"*(21:30~21:39). 사다리는 대화 기록 → 플러그인·MCP·API(예: Plaid 은행 정보) → 웹 검색(예: 어젯밤 Cubs 경기) → 컴퓨터의 브라우저 → 데스크톱 전체(스크립트·명령·빌드) → *"only if all of those fail, then go bug the user"*(21:40~22:25) 순이다. *"they're not going to bug you for all these different things"*(22:31~22:32)
- 브라우저 정보 사다리: 스크린샷 → HTML → *"the accessibility tree, which is a nice way of like cutting down a lot of the uh token usage"*(22:55~23:03) → 픽셀 클릭(모달·대화상자) → 최악은 사용자에게 2FA 코드·CAPTCHA를 묻는다(22:47~23:27).

→ [[deferred-tool-context]](같은 기법, 다른 이름) · [[toolbox-pattern]] · [[agent-attention-management]] · [[model-context-protocol]]

## 9. main agent와 durable helper (23:30~26:30)

- ⭐ *"you have this main agent and it's kind of like your orchestrator and the main agent, you want to keep the conversation as sparse as possible because it now has the ability to go call on all of these different helpers. And the helpers are just sub agents."*(23:34~23:52) 비싼 셸·도구 호출은 helper가 하고 *"It's only coming back with the result. And this is how you get to a product that feels like it has infinite context. Obviously there infinite context is not a real thing."*(24:07~24:19)
- *"Each one of these is its own durable workflow (…) if it fails, the video helper crashes (…) that can restart and keep going without losing progress"*(24:37~24:52). main agent는 to-do를 관리하며 helper를 확인·메시지·정지한다(24:56~25:05). *"modeled after the ideal way you would scale, you know, a team of engineers"*(25:05~25:11)
- 만들며 배운 것 셋(25:14~26:28): ① *"ideally you don't add or remove new tools during turns"*(25:23~25:28), 긴 도구 설명·스키마는 줄인다. ② *"you can model a lot of things this way, but if you see the model doing, you know, 90% of its time doing shell commands for this one thing, it actually can be more efficient to make a dedicated tool"*(25:55~26:06), 사람이 읽기에도 낫다. ③ 사람에게 좋은 오류 메시지가 *"Turns out that's also very helpful for agents. So there there is some DX in designing um good error messages for agents too."*(26:22~26:28)

→ [[subagent-vs-thread-handoff]] · [[orchestrator-searcher-split]] · [[agent-swarm]] · [[durable-execution]] · [[agent-tool-design-practices]](조치 가능한 오류) · [[file-system-agent]](단일 bash 도구에 대한 단서)

## 10. 보안 (26:30~27:26)

- *"even working on its own separate machine not polluting anything on your machine still you would like it if you know a model reviews every shell command before it goes. So auto review"*(26:42~26:54)
- ⭐ *"when these untrusted inputs like a email in your inbox could be a fishing[=phishing] email or some web hook you don't want to send that to the model and act like it was a user instruction and there's plenty of work to do here uh in the industry"*(26:54~27:07)
- 되돌릴 수 없는 일(이메일 보내기)은 사용자에게 먼저 묻고, *"build in some workflows into the product to keep passwords and other things outside of the model conversations."*(27:17~27:24)

→ [[prompt-injection]] · [[transcript-classifier]] · [[action-reversibility]] · [[credential-injection-outside-sandbox]] · [[agent-sandboxing]]

## 11. prompt caching과 compaction (27:26~32:50)

- *"context engineering is also known as harness engineering. Like I feel like it's kind of the same thing."*(27:26~27:33)
- ⭐ 왜: *"most of the tokens used are actually ideally cached tokens because you're sending it a conversation and then (…) you're basically rescending[=resending] the entire conversation over again. So if you look at the pricing for models, there's huge discounts of course on if a token is cached"*(27:56~28:14)
- 정적 접두: *"try to keep the tool definitions, the system prompts, all of this information as static as possible between different calls so that you don't break the cache"*(28:19~28:29). 그러면 새 메시지만이 *"the only delta that you're paying the uncashed[=uncached] tokens for"*(28:38~28:42)다.
- main agent의 컨텍스트를 작게: 긴 출력은 파일로, 스크린샷 같은 비싼 일은 helper로, 그리고 *"always gardening and trimming"*(29:39~29:44). ⭐ *"if there's a cash cache miss, it's kind of like a bug in the system really."*(29:51~29:55)
- ⭐ OpenClaw: *"all the way back to January of this year, uh, when OpenClaw was really getting popular and people were using it, uh, inside of subscription plans for, uh, model providers, this was a very new usage pattern that model providers hadn't really seen and the the harness hadn't really yet been optimized for this type of workflow. So, there was a lot of cache misses."*(29:59~30:22)
- 섹션 해시·고정 순서: A/B 테스트로 프롬프트에 새 조각을 넣어도 *"you can almost hash each section and always keep a fixed order (…) You really don't want that to screw up the prompt order for everybody else. Otherwise, you just busted the cache."*(30:48~31:01)
- cache warming: *"when you open the chat and you start typing, um the server can actually go and prepare the prompt early, uh, to basically warm the cache"*(31:06~31:13). 링크 hover 시 prefetch에 비유한다.
- compaction: *"let's say the model has a 200,000 token context window (…) Eventually, it's going to hit a point where it needs to summarize. And all compression is lossy."*(31:41~31:52)
- ⭐ **캐시가 따뜻할 때 compaction**: 10만 토큰 넘게 대화한 뒤 사용자가 자리를 뜨면 *"there is this time period where the model providers have uh like a cache window when the cache is still warm. Maybe it's 10 minutes, maybe it's 60 minutes. Uh one trick that we do (…) while you're still within the warm cache period, you should probably do the the compaction right now because (…) it's going to be much cheaper."*(32:11~32:30) 30분 뒤 돌아온 사용자는 더 싼 요약 위에서 이어 간다(32:33~32:43).

→ [[prompt-caching]](신규) · [[context-engineering]] · [[harness-engineering]](⚠️ 두 이름을 "같은 것"이라 한다 — 아래 "갈리는 것") · [[context-resets-and-compaction]] · [[openclaw]] · [[scripts-that-talk-back]](캐시를 대가로 치르는 기법)

## 12. 메모리 층 (32:50~34:27)

- 층 하나: *"facts about the user that are very important to be included every single time"*(33:00~33:06). 소문자 취향이 그 예다(*"if you're going like full Sam Alman[=Altman] style"* 33:15~33:17). 그 사실들에 *"this kind of garbage collection"*(33:32~33:34)이 필요하다. 뇌가 지금 대화와 무관한 축구 경기를 떠올리지 않듯이(33:36~33:50).
- ⭐ *"the the harness has of course these core facts. It also has these dated logs of kind of your past conversation history essentially and then also these kind of scratchpad notes. So it's like little things that you've been working on right now that are designed to be ephemeral and they will go away but they might be relevant just for the next 30 minutes or an hour. And everything else can be found through files."*(33:52~34:17)
- *"This is the magic of files of the models being good at running commands"*(34:17~34:23)

→ [[agent-memory]] · [[files-vs-database-agent-memory]](상태는 DB 11:06~11:12, 회상은 파일) · [[nightly-memory-consolidation]] · [[context-rot]]

## 13. 학습 플라이휠 (34:27~37:45)

- 단계 복습: pre-training, SFT(*"teaching the model how to behave uh in a certain way maybe as a chat assistant or as an agent"* 34:52~34:58), RL(*"kind of like teaching the model how to play games"* 35:01~35:04)
- always-on 맥락: SFT로 *"see examples of the harness and to know how to work inside of the harness"*(35:12~35:16), RL로 지시 이행, *"How to understand the right skill to call when there's hundreds of skills"*(35:25~35:30), 브라우저에서 바른 곳 클릭(35:30~35:34)
- inference: main agent는 *"very low latency"*(35:45), helper는 *"the difference between 10 minutes and 12 minutes is kind of negligible"*(35:57~36:00)
- ⭐ 두 루프: 실수 → eval → 하네스·버그·프롬프트·inference 수정 → eval로 확인이 *"this inner loop that you're always getting better at. But then there's this outer loop which is like every few months or every month or however long um you're training new models and ideally the new models are learning from all of these bugs"*(36:41~36:53). (36:55~36:59 en-orig 공백)
- 새 능력: *"There hasn't really been a lot of training data for example on using bots in a group chat. This is kind of an emergent thing (…) if you've seen things like moldbook[=Moltbook] or the hugging face incident like there are ways that that goes poorly. So it's important to be able to train the models how to behave well in a multi- aent[=multi-agent] system"*(37:09~37:31)

→ [[production-trace-eval-flywheel]] · [[inner-outer-meta-loops]](⚠️ 같은 이름, 다른 루프 — 아래) · [[emergent-agent-collective]]·[[tech-bridge-openai-huggingface-incident-black-hat]](⚠️ 같은 사건인지 발화로 확인 안 됨) · [[multiplayer-agent-context]] · [[inference-speed-as-capability]] · [[model-mixing-economics]]

## 14. "delete the product"와 전망 (37:45~40:20)

- ⭐ *"one of the principles that we had at Cursor uh and now at SpaceX is to delete the product. And what we mean by this is you kind of have to internalize and assume that the models today are the worst they'll ever be. Which means that in 6 months, uh, you might need to completely rebuild the UI."*(37:45~38:04) 오늘 말한 것 대부분이 6개월 전·1년 전에 했을 강의와 크게 다르다(38:04~38:17). *"you really want to try to build for the next generation of the model. like how do you build as little as possible"*(38:19~38:28)
- 6~12개월 전망(38:36~40:20, *"decently safe bets"*): 에이전트가 몇 시간·하루에서 *"weeks or months"*로, 과거 정보 회상이 나아짐(그래프든 파일이든), 디지털 동료에게 사람 신입처럼 모든 도구를 줌(조직은 아직 적응 중), speech-to-speech와 *"Johnny IV[=Jony Ive] device"*(39:45), 일하며 배운 스킬을 파일로, 회사가 자기 프로세스를 *"legible for agents"*(40:18~40:20)로 적음

→ [[harness-pruning]] · [[model-scaling-durability]] · [[sutton-bitter-lesson]] · [[skill-self-improvement]] · [[company-brain]]

## 15. 열린 문제와 새 building blocks (40:20~43:21)

- ⭐ *"What do you do when you need to evaluate an agent that runs for a month but the models ship every month? (…) you either have to figure out how to do a better eval or you know not ship models as fast and I think that's going to be a problem that the industry has to figure out in the next six months."*(40:30~40:53)
- 메모리 알고리즘, 보안(*"so they can't be taken over by bad actors"* 41:08~41:10), ⭐ 침묵 heuristic: *"I don't think that we have it perfect yet."*(41:18~41:20) 예: 어제 수업을 빠졌으니 녹음해 노트를 정리했다는 제안은 *"maybe that's helpful or maybe that's kind of annoying"*(41:33~41:34)
- *"at this time next year there will be significantly significantly more tokens flowing in the world"*(41:43~41:50) → 추론·모델·하네스의 토큰 효율
- OpenRouter의 Alex(성 미발화)가 X에 쓴 말: 모든 앱이 사이드바·에이전트·채팅창으로 똑같아 보인다는 불평은 2005년의 서버·DB·CRUD와 같다. *"every new product is going to have to have some kind of uh agentic side to it either integrating or it will become a uh a you know a headless piece of data for another agent to use."*(42:36~42:48)
- building blocks: *"Durable workflows, um, sandboxes, computers in the cloud, memory, skills, uh, connecting to other services, doing voice, payments, identity, eval, observability. Each one of those boxes is like multiple billions of dollars of VC capital, you probably trillions. There's 20 startups for each one of those."*(42:50~43:09)

→ [[launch-blocking-evals]] · [[agent-attention-management]] · [[agentic-sites]] · [[agent-native-interface]] · [[agent-platform-layers]]

## 16. 수강생에게 (43:21~45:14)

- ⭐ *"It's more important than ever to think about the broader system design and the architecture of the code that you're working on because that the decisions you make there will really compound. Um, so I'm still I'm still pro looking at code, you know, I still look at the code that I'm writing, some people not looking at the code."*(43:30~43:45)
- 오늘 것을 적용해 자기 판본을 만들어 보라. *"I'm pretty sure there's like open grobbot[=GrokBot] on GitHub somewhere where somebody's like, you know, slotforked[=?] our code"*(44:08~44:15)
- *"just like when you're building a web app, it's helpful to know how databases work because increasingly the there are so many decisions you make at the product in the harness uh level that are influenced by the models themselves."*(44:50~45:04)

→ [[architecture-as-remaining-art]] · [[software-factory]](⚠️ 코드를 보지 않는 쪽과 대비)

## 이 위키와의 연결

### 이어지는 것

- **[[brain-hands-decoupling]]: 같은 분리를 다른 회사가 운영 이유로 낸다.** [[anthropic-managed-agents]]는 brain(하네스)과 hands(sandbox)를 나눠 sandbox를 cattle로 만들었다. Robinson은 같은 선을 긋고 이유를 구체적으로 댄다. 루프가 VM에 있으면 VM을 따로 내릴 수 없고, 제로데이 패치로 VM을 다시 지을 때 루프와 앱이 같이 멈춘다(14:53~15:24). ko는 바로 이 문장을 뒤집는다.
- **[[durable-execution]]·[[temporal]]: 사용자 증언.** 두 페이지의 1차 출처는 Temporal 직원의 발표 하나였다. 이번에는 **Temporal을 쓰는 쪽**이 job queue와 대비해 이유를 말한다(16:17~17:19). helper마다 durable workflow라는 적용(24:37~24:52)도 새롭다. ⚠️ 그래도 당사자(GrokBot 쪽) 진술이고, 무엇을 workflow로 두고 무엇을 activity로 두는지는 발화되지 않는다.
- **[[deferred-tool-context]]: 미해결 질문에 대한 한 답.** 그 페이지는 *"로드할 때마다 도구 정의가 추가되면 캐시 접두가 바뀌는가"*를 열어 두었다. Robinson은 tool search로 이름만 싣고(20:51~21:11), 턴 중에는 도구를 더하거나 빼지 않는다(25:23~25:28)고 한다. 로드한 정의가 어디에 붙는지는 말하지 않는다.
- **[[persistent-agent-teams]]·[[grokbot]]: 밖에서 본 모습과 안에서 본 모습.** [[lauren-tan|Lauren Tan]]은 GrokBot을 정체성·자기 컴퓨터·비서실장·루틴으로, 그리고 자기 일의 "바깥 루프"로 설명했다. Robinson은 그 컴퓨터가 Firecracker VM이고, 루틴이 cron 같은 예약 프롬프트이며, 봇들이 virtual desktop으로 인프라를 공유하고, 클라이언트-서버 도구가 send user 하나라고 한다. Tan이 말한 *"Dune의 host는 GrokBot 가상 머신에서 돈다"*와도 맞는다.
- **[[agent-attention-management]]: "언제 말을 걸까"가 설계 대상이 된다.** router 뒤의 heuristic(11:59~12:18), 사다리 끝의 사용자(22:21~22:25), 미완성 인정(41:12~41:20)이다.
- **[[prompt-caching]](신규)**: [[context-engineering]]의 "Prompt cache 친화적 조직", [[transcript-classifier]]의 stage 2 캐시 적중, [[scripts-that-talk-back]]의 대가, [[automatic-model-routing]]의 비켜 간 질문이 한 페이지에 모인다. 이 강의가 가장 자세하다.

### 갈리는 것

> ⚠️ **Contradiction(약): 환각은 해결됐는가.** Robinson은 *"it's kind of a solved problem mostly"*(07:26~07:30)라고 한다. [[preference-reward-asymmetry]]의 Almeida는 환각이 RLHF 목적함수에 내재한다고 했다. 그 페이지가 이미 기록한 [[tech-bridge-brockman-agi-era-defender-window|Brockman 편]] 진행자의 체감(*"꽤 오랫동안 환각을 본 적이 없습니다"*)과 같은 쪽이다. 세 발언 모두 측정이 없다. 이 위키는 판정하지 않는다.

> ⚠️ **같은 이름, 다른 루프.** 이 강의의 inner loop는 "버그 → eval → 하네스 수정"의 매일 순환이고, outer loop는 "몇 달마다 새 모델 학습"이다(36:41~36:53). [[inner-outer-meta-loops]]의 Knox는 개발 단계로 나눴고, [[lauren-tan|Lauren Tan]]은 GrokBot을 외부 이벤트를 받는 "바깥 루프"라고 불렀다([[grokbot]]). 같은 SpaceX 쪽 두 화자가 outer loop를 다른 것에 쓴다. 섞어 읽지 말 것.

> ⚠️ **긴장: context engineering과 harness engineering은 같은 것인가.** Robinson은 *"I feel like it's kind of the same thing. They've evolved over time"*(27:30~27:35)라고 한다. [[harness-engineering]]은 하네스를 context engineering을 포함하는 더 큰 우산(프로세스·오케스트레이션까지)으로 기록한다. 이 강의의 용례는 컨텍스트 최소화에 한정된다.

> ⚠️ **긴장(약): OpenClaw 구독 사용의 문제는 무엇이었나.** Robinson은 1월 OpenClaw의 구독 플랜 사용이 공급자가 못 본 패턴이라 **캐시 미스가 많았다**고 한다(29:59~30:22). [[tech-bridge-stigg-ai-companies-building-banks|Stigg 편]]의 Sasson은 Anthropic이 구독으로 소비를 **보조**하다 서드파티 접근을 끊었다고 했다([[openclaw]]). 두 설명은 배타적이지 않다(캐시 미스가 보조 비용을 키운다). 어느 쪽도 공급자 이름·수치를 함께 대지 않는다.

> **코드를 볼 것인가.** Robinson은 *"I'm still pro looking at code"*(43:40~43:42)라고 한다. [[tech-bridge-openhands-sandboxing-coding-agents|Brennan]]의 끝 그림(*"humans aren't even looking at the source code anymore"*)과 [[software-factory]]의 방향과 대비된다. [[tech-bridge-lauren-tan-trusting-agents|Lauren Tan]]은 GrokBot 첫 판이 *"사람은 코드를 전혀 읽지 않았다"*였고 600건 넘는 PR로 다시 짰다고 했다. 이 강의의 *"the decisions you make there will really compound"*(43:35~43:38)와 같은 방향이다.

> **auto review는 [[transcript-classifier]]와 같은 장치인가.** 별도 모델이 모든 명령을 실행 전에 본다는 구조는 같다. Robinson은 *"a lot of companies are calling auto review"*라고만 하고 출처·구현을 말하지 않는다. blind test 주장(05:21~05:30)은 그 페이지의 어떤 수치와도 대조할 수 없다.

## 해소하지 않고 표시만 한 것

- auto review blind test의 주체·방법·결과, *"a lot of companies"*가 누구인지.
- 환각 *"solved problem mostly"*의 근거.
- 사용자 수, 지연, 비용, 캐시 적중률, compaction 품질 같은 GrokBot의 수치. 캐시 창 10분·60분은 *"maybe"*다.
- send user 하나로 클라이언트가 사인인 폼·결제를 어떻게 구분하는지(도구 인자인지 별도 메시지 타입인지).
- router의 dedupe 기준, 알림 heuristic의 실제 규칙, 우선순위 큐의 등급 수.
- Temporal 위에서 루프·helper를 어떻게 나눴는지. *"you still have to run the infrastructure"*의 비용.
- *"the hugging face incident"*가 이 위키의 OpenAI–HF 사건과 같은지. Moltbook(이 위키에 페이지 없음).
- 여섯 변화의 경계, *"slotforked"*, *"Alex from Open Router"*의 성.
- 화자의 성·직함·이전 경력(Cursor에 있었다는 것 외), 학교·과목, 녹화일. 슬라이드 내용(*"this chart"*, *"the purple box"*, *"the slide with all of the uh boxes"*).

## 등장 개체

- 인물: [[lee-robinson|Lee Robinson]](신규 제안 — 자막에는 "Lee"만, 성·직함은 설명란) · [[sam-altman|Sam Altman]](소문자 비유, 지나가는 언급) · Jony Ive · OpenRouter의 Alex — 페이지 없음
- 조직: [[spacex|SpaceX]] · [[cursor|Cursor]](*"principles that we had at Cursor"*) · [[temporal|Temporal]] · [[hugging-face|Hugging Face]](사건 이름으로만) · OpenRouter · Plaid · Stripe · 1Password — 페이지 없는 것은 지나가는 언급
- 제품: [[grokbot|GrokBot]](en-orig *"Grockbot"*·*"open grobbot"*) · [[openclaw|OpenClaw]] · Firecracker · ChatGPT · Moltbook · X Money · Stripe Link — 페이지 없음
- 개념: [[always-on-agent-architecture]](신규 제안) · [[prompt-caching]](신규 제안) · [[persistent-agent-teams]] · [[brain-hands-decoupling]] · [[durable-execution]] · [[agent-distributed-systems]] · [[human-as-async-api]] · [[pets-vs-cattle]] · [[agent-sandboxing]] · [[cloud-agent-delegation]] · [[agent-attention-management]] · [[scheduled-agent-automations]] · [[deferred-tool-context]] · [[toolbox-pattern]] · [[context-engineering]] · [[harness-engineering]] · [[context-resets-and-compaction]] · [[context-rot]] · [[agent-memory]] · [[files-vs-database-agent-memory]] · [[nightly-memory-consolidation]] · [[file-system-agent]] · [[agent-skills]] · [[mcp-skill-distribution]] · [[skill-self-improvement]] · [[subagent-vs-thread-handoff]] · [[orchestrator-searcher-split]] · [[agent-swarm]] · [[agent-tool-design-practices]] · [[scripts-that-talk-back]] · [[transcript-classifier]] · [[prompt-injection]] · [[action-reversibility]] · [[no-silent-write]] · [[credential-injection-outside-sandbox]] · [[production-trace-eval-flywheel]] · [[inner-outer-meta-loops]] · [[launch-blocking-evals]] · [[emergent-agent-collective]] · [[multiplayer-agent-context]] · [[inference-speed-as-capability]] · [[model-mixing-economics]] · [[harness-pruning]] · [[model-scaling-durability]] · [[sutton-bitter-lesson]] · [[preference-reward-asymmetry]] · [[agentic-sites]] · [[agent-native-interface]] · [[agent-platform-layers]] · [[architecture-as-remaining-art]] · [[software-factory]] · [[steering-altitude]] · [[agent-trust-curve]] · [[company-brain]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=N8gD8ebFlMI> (45:17, `upload_date` 2026-10-17 — 멤버 전용 당시 목록 값 20261012)
- raw: `01.raw/articles/2026-10-17_Grok Bot 같은 상시 작동 에이전트는 어떻게 작동할까요? - SpaceX 엔지니어 Lee Robinson의 스탠퍼드 강연.md`
- 같은 제품의 다른 소스: [[tech-bridge-grokbot-agent-teams]] · [[tech-bridge-lauren-tan-trusting-agents]] · [[tech-bridge-lauren-tan-2000-prs]] · [[tech-bridge-lauren-tan-pocock-podcast-full]]
- 루프와 실행 환경의 분리: [[anthropic-managed-agents]] · durable execution의 벤더 쪽: [[tech-bridge-human-is-async-api]]
- 같은 주 샌드박스·클라우드 실행: [[tech-bridge-openhands-sandboxing-coding-agents]]
- 스탠퍼드 강의의 다른 소스: [[tech-bridge-karpathy-transformers-stanford]](CS25 — 과목 다름)
- [[tech-bridge]] · [[lee-robinson]] · [[grokbot]] · [[spacex]]
