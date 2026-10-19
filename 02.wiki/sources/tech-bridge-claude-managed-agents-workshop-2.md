---
title: "Tech Bridge — Claude Managed Agents 워크숍 2/4 (Priyanka Phatak · Gabe Cemaj, Anthropic): 콘솔 한 줄에서 리서치 데스크까지 — 이벤트 스트림·스킬·하위 에이전트·메모리 스토어·Outcome, 그리고 아직 없는 것 넷"
type: source
tags: [managed-agents, claude-managed-agents, workshop, ai-engineer, event-stream, sse, agent-environment, sandbox, self-hosted-sandbox, agent-skills, subagents, self-referential-subagent, custom-tools, memory-store, shared-memory, outcomes, rubric, grader, self-supervision, generator-evaluator, vaults, credential-injection, egress-proxy, mcp-tunnel, agent-sdk, harness, session-steering, session-forking, budget-controls, dreaming, lock-in, sec-edgar, nvidia, vendor-pitch, video]
source-url: https://www.youtube.com/watch?v=U0ZCwwG8sac
source-type: video
author: Tech Bridge (한영자막 재배포) · 원본 채널 AI Engineer(설명란) · 진행 Priyanka Phatak · Gabe Cemaj([[anthropic|Anthropic]] Claude Managed Agents 팀 — ⚠️ **이 편에서는 이름만 발화**. 성 Phatak · Cemaj는 이 편 설명란 *"Anthropic의 Priyanka Phatak과 Gabe Cemaj"*에서 옴. 1부 자기소개에서 Priyanka는 성을 말하지 않고, Gabe는 en-orig *"Semach"*) · 행사 AI Engineer World's Fair 2026(⚠️ 설명란에만)
date-published: 2026-10-18
ingested: 2026-10-19
created: 2026-10-19
updated: 2026-10-19
---

# Tech Bridge — Claude Managed Agents 워크숍 2/4 (Priyanka Phatak · Gabe Cemaj)

[[tech-bridge|Tech Bridge]]가 재배포한 [[ai-engineer|AI Engineer]] 워크숍 4부작의 **2부, 35:09**다. [[tech-bridge-claude-managed-agents-workshop-1|1부]](14:39)가 설계 이야기와 콘솔 Quick Start 안내에서 끝나고, 이 편은 1부 발표에 대한 청중 질문으로 시작한다. 진행은 [[anthropic|Anthropic]]에서 Claude Managed Agents를 만든 팀의 [[priyanka-phatak|Priyanka Phatak]](1부 자기소개 *"I lead the engineering team that built Claude managed agents"*)과 [[gabe-cemaj|Gabe Cemaj]]다. 이 편에서는 성이 발화되지 않는다. 성 *Phatak*은 이 편 설명란(*"Anthropic의 Priyanka Phatak과 Gabe Cemaj"*)에서 왔고, 1부 자기소개(*"My name is Priyanka"*)·1부 설명란에는 없다. 앞 3분은 Priyanka의 콘솔 데모이고, 나머지는 Gabe의 핸즈온(**research desk** 저장소)과 Q&A 8건이다. 공식 챕터는 `meta.txt` 기준 18개다. 3/4·4/4는 아직 올라오지 않았다. 이 편이 보여 주는 것은 다음과 같다.

> **[[managed-agents|Claude Managed Agents]]에서 개발자가 다루는 것은 agent(버전이 붙는 정의) · environment(샌드박스 템플릿) · session(이벤트 스트림)이고, 하네스·샌드박스·스케일링·이벤트 로그 저장은 Anthropic이 맡는다. 에이전트는 스킬·하위 에이전트(자기 참조 포함)·맞춤 도구·공유 메모리 스토어로 키우고, Outcome(과제 + 루브릭 + 최대 반복)을 주면 채점 하위 에이전트가 결과를 확인한다. 비밀은 Vault가 샌드박스에 placeholder로만 넣고 egress에서 허용된 도메인에만 진짜 값으로 바꾼다. 그리고 세션당 예산 상한, 되감기·분기, 메모리 밖의 dreaming, 외부 메모리 공급자는 아직 없다.**

> *"All you have to do is start a session with the agent, send events, get back events. Everything else is managed by us."* (03:00~03:05) · *"really, everything that happens in the communication for these more chat-like applications happens on that stream."* (12:07~12:14) · *"Outcomes is how we've created self-supervision."* (17:45~17:50) · *"We at Egress[=at egress] swap it out for the real value only on the host domains that you specified are allowed for that secret."* (24:23~24:32)

이 위키에 새 페이지는 인물 둘뿐이다([[priyanka-phatak]] · [[gabe-cemaj]], 1부와 공유). 나머지는 기존 페이지에 붙는 **제품 팀의 1차 증언**이다.
- [[managed-agents]]: 리소스 모델(agent · environment · session)과 **현재 없는 기능 넷**을 처음으로 팀이 직접 말한다
- [[credential-injection-outside-sandbox]]: 셋째 메커니즘 — **샌드박스 안의 placeholder를 egress에서 도메인별로 바꿔치기**
- [[generator-evaluator-pattern]]·[[outcome-engineering]]: Outcome의 입력(루브릭·max iterations)과 범위(세션 수준만, sub-outcome 없음)
- [[agent-dreaming]]: *"Today the dreaming's constrained to memory stores"* — 09-01 진술과 갈린다(아래 Contradiction)
- [[agent-memory]]: 세션 간 공유 메모리 스토어, 세션당 여러 스토어(사용자 수준 + 조직 수준), API로 꺼낼 수 있음
- [[subagent-vs-thread-handoff]]: 자기 참조 하위 에이전트는 트랜스크립트가 아니라 **프롬프트·도구·스키마만** 복사한다
- [[agent-skills]]: 스킬은 *"live artifacts"* — 갱신하면 그 스킬을 참조하는 새 세션이 받는다
- [[agent-harness-design]]·[[claude-agent-sdk]]: CMA는 Agent SDK에서 배운 것으로 **다시 지은 범용 하네스**(*"sort of a fork? — yeah"*)
- [[brain-hands-decoupling]]·[[agent-sandboxing]]: 자체 호스팅 샌드박스 공급자(Vercel·Modal·Daytona·Google Cloud·AWS), environment의 네트워크·패키지 설정

ASR·ko 보정. ko는 **설명 셋을 뒤집는다.** *unrestricted access* → **"지금은 제한이 있지만"**(02:08), *nothing stopping you from using other providers* → **"다른 서비스 제공업체를 이용하는 것을 막습니다"**(27:23~27:26), *use no more than this amount of money* → **"이 금액보다 더 많은 돈을 사용하세요"**(27:38)다. 셋 다 `en`은 맞다. 용어도 흩어진다. sandbox는 내내 **"테스트 환경"**, harness는 **"환경"**, scorecard는 **"대시보드"·"제어판"**, dreaming은 **"꿈"·"수면 기능"**, Anthropic은 **"인간이 만든"**(30:13), placeholder는 **"점수판 가치"**(24:22), real credential은 **"왕실 증서"**(25:50)다. 원문에 없는 문장도 둘 생긴다: **"고등학교 졸업 후 취업을 시작하는 학생들"**(15:25), **"저 사람은 자기가 대체 누구라고 생각하는 거야?"**(34:26). en-orig는 Claude를 *"Cloud"*로, Priyanka를 한 번 *"Bianca"*(11:54)로, RAG를 *"rack"*(33:09)으로 적는다. 전체 목록은 raw에 있다.

> ⚠️ **벤더 당사자 워크숍이다.** 제품 팀이 자기 제품을 시연한다. *"not just for minutes, but hours, days, weeks, and even months"*(13:14~13:18) 같은 진술에 근거는 붙지 않는다.
>
> ⚠️ **Nvidia 분석은 결과가 없다.** 보여 준 것은 *"something I ran yesterday"*(19:06~19:08)의 트레이스 설명이다. 라이브 실행은 *"about 10-ish minutes"*(19:03~19:04) 걸린다며 끝나지 않는다(*"I think this is still running"* 21:24~21:26). 스코어카드의 수치·결론은 발화되지 않는다. 설명란의 *"다시 시도하는 과정을 보여줍니다"*와 달리 **재시도 장면은 없다.** 채점 하위 에이전트는 첫 판정에서 *"satisfied"*(21:13~21:14)였다.
>
> ⚠️ **예고만 되고 이 편에 없는 것.** map-reduce 오케스트레이션(맞춤 도구 dispatch analysis로 세션 N개를 띄우고 모으기, 05:12~05:35·21:42~22:22), deployments API(일정 기반 반복 세션, 05:36~05:50), dreaming 시연(22:56~22:58, 29:57~30:01). 영상은 *"I'm going to continue to that with the demo"*(35:02~35:04)에서 잘린다. 3/4·4/4가 올라오면 이어 붙일 것.
>
> ⚠️ **화면은 확인하지 않았다.** 콘솔 UI, 저장소 QR(주소 미발화), 스코어카드 표, 콘솔의 thread 시각화는 자막에 없다. 1부와 2부 사이에 잘린 구간이 있을 수 있다(01:06 *"let let's try this one more time"* — 앞선 시도는 어느 편에도 없다).

## 1. 1부 질문 — 세션 저장 설계의 변화 (00:00~00:49)

- 청중: *"Out of curiosity for the design of the session, in um first iteration and second iteration, what has changed?"*(00:00~00:08). 1부의 진화 이야기(1·2차 설계)를 가리키는 질문이다. 1·2차의 내용은 [[tech-bridge-claude-managed-agents-workshop-1|1부]] 참조.
- Gabe: *"we wanted to abstract away as many things and compartmentalize them into different components um to make it so that we could extend the storage mechanisms for future events that we wanted to store uh without tying them, you know, so tightly coupled to the mechanics of the session work."*(00:22~00:39)
- ⭐ *"we basically applied the same principle of building and virtualizing interfaces all the way down uh not only across service boundaries, but also at the event layer."*(00:40~00:49)

→ [[brain-hands-decoupling]] · [[anthropic-managed-agents]](session / harness / sandbox 가상화가 **이벤트 층**까지 내려간다는 추가 진술)

## 2. 콘솔 Quick Start — 농담 에이전트 (00:51~03:27, Priyanka)

| 단계 | 발화 |
|---|---|
| 에이전트 | 프롬프트 *"Build me an agent that tells me jokes every time given a topic."*(01:09~01:18) → Claude가 *"a system prompt. It came up with a name, a description, chose a model"*(01:30~01:34), agent toolset 부여 → *"create agent. That should basically call the V1 agents endpoint"*(01:43~01:47) |
| environment | *"the template for the sandbox"*(01:53~01:54). 데모는 *"unrestricted access"*. *"when you're building a production agent you you want to tighten the access, control which domains it can uh reach out to or specific MCP servers."*(02:10~02:18) 설치할 패키지 선택(02:22~02:26) |
| session | *"Tell me jokes about cats"*(02:36) → 모델이 생각하고 고양이 농담(02:42~02:49) |

- ⭐ *"Now this agent is up and running in the cloud. All you have to do is start a session with the agent, send events, get back events. Everything else is managed by us. So we're managing all the infrastructure, the hosting, the harness, the sandbox management, the scaling, the storage of your event log, and then you can focus on building your product around this."*(02:57~03:16)

→ [[managed-agents]] · [[agent-sandboxing]](environment = 네트워크 허용 범위 + 패키지) · [[least-privilege-connectors]]

## 3. 워크숍 구성 — research desk, 6막, Claude Code 스킬 (03:34~09:58, Gabe)

- 저장소를 clone해 `research desk` 디렉터리에서 `npm install`/`bun i`, `bun run dev`(03:46~04:01, 06:37~06:42). 저장소 주소는 QR로만 나온다(미발화).
- 만들 것(04:28~05:50): 채팅 UI → 하위 에이전트에 위임하는 *"multi-agent uh ecosystem"* → SEC 공시를 읽는 스킬 → 오래 걸리는 비동기 작업 → *"map-reduce interface"*, 즉 *"how you can build a custom harness on top of CMA to orchestrate, you know, your own work with custom tools, uh and manage multi-session um kind of interactions"*(05:25~05:35) → deployments API(*"set up recurring work on a schedule"* 05:41~05:44).
- *"I'm going to be using uh Cloud[=Claude] Code for this. You're free to use whatever coding agent you prefer. Uh I don't think anybody's writing code by hand, so I'm not going to do that either."*(06:00~06:10)
- ⭐ 워크숍 자체가 **Claude Code 스킬**이다: *"there is a skill that we've loaded up in your repository that's going to walk you through the workshop step by step"*(06:11~06:19). *"in Cloud[=Claude] Code, you can type in uh workshop start (…) We're going to do it in six acts."*(07:25~07:35) *"We're going to go into auto mode. Um, Claude Claude is going to keep track of each of the acts (…) You can keep typing workshop next"*(07:48~07:57). Claude가 *"a little eager"*(08:24)해 앞서 나가는 장면이 두 번 있다(08:20~08:24, 13:27).
- 준비: `.env.local`에 API 키와, SEC가 요구하는 이름·이메일(*"the SEC wants to know who you are when you're calling their API"* 08:33~08:37)을 넣는다.
- 와이파이 문제로 따라온 청중은 *"one one person at least"*(09:07~09:08)였다.

→ [[agent-skills]](교육 과정을 스킬로 배포) · [[claude-code]]

## 4. 어디서 돌아가는가 (10:02~10:50, Q&A)

- 질문: *"where is this running? Is this running on AWS?"*(10:11~10:14)
- ⭐ Gabe: *"we're going to run it in our own infrastructure. Um today we we have like a 1P offering uh that we run on, but we also have cloud[=Claude] platform on AWS if you want to run on AWS using your AWS credits. What we also offer (…) is self-hosted sandboxes. So if you want to bring your own sandbox through uh different providers like Vercel or Modal or Daytona or a bunch of others, you can do that uh even, you know, through Google Cloud and and AWS."*(10:16~10:50)
- ⚠️ *"cloud platform on AWS"*는 Claude Platform on AWS로 읽었다(판독).

→ [[brain-hands-decoupling]](hands를 고객 쪽 공급자에 둔다) · [[agent-sandboxing]] · [[vercel]]

## 5. 이벤트 스트림 채팅 UI (10:52~13:18)

- 설정 페이지 버튼이 **environment**와 **agent**를 만든다. environment는 *"access to a few websites (…) mainly the SEC"*와 SEC용 Python 패키지(11:10~11:24). 에이전트는 *"very basic agent. Right now it has no tools. Um it has uh just a prompt. Uh well, it has the basic tools, but there's no skills. There's no sub-agent coordination"*(11:27~11:39).
- ⭐ *"the main uh way you communicate with a session is through an event stream. So, you listen onto that stream for all the events that the agent is pushing back down to you, and you can use that uh an endpoint to push events back up."*(11:54~12:05)
- 구현: 엔터를 누르면 *"a user.message event"*를 세션에 보내고(12:19~12:26), 백엔드가 API의 *"SSE stream"*을 듣고 프런트엔드로 다시 흘려보낸다(12:26~12:43).
- *"If you wanted to build a chat-like application, this is where you would stop."*(13:02~13:05) ⭐ *"The whole point of Claude managed agents is that you can do long-running asynchronous tasks, um not just for minutes, but hours, days, weeks, and even months."*(13:08~13:18) ⚠️ 근거 없는 벤더 진술.

→ [[managed-agents]] · [[anthropic-managed-agents]](`emitEvent`/`getEvents`의 사용자 쪽 모습)

## 6. 에이전트 키우기 — 스킬·하위 에이전트·맞춤 도구·메모리 스토어 (13:30~17:27)

*"we want to basically move up the ladder of intelligence."*(13:46~13:48) Claude Code가 *"provisioning scheme"*(13:58~13:59)을 구현한다.

| 요소 | 발화 |
|---|---|
| **스킬** (SEC EDGAR) | *"We've described how to use the Python package, we've described that it has to use the Edgar identity to call"*(14:13~14:20) |
| **맞춤 도구** dispatch analysis | *"that custom tool is what we're going to be able to use to tell our head of research agent to spin off multiple sessions that we will coordinate uh, for a a sort of custom harness."*(14:26~14:35) *"we give it a schema"*(14:46). 이 편에서는 만들기만 하고 쓰지 않는다 |
| **새 에이전트 버전** | *"update the the description of the main agent so that it creates a new version of that agent"*(14:47~14:55) |
| **하위 에이전트 + 자기 참조** | *"a few different sub-agents, uh, that it can delegate work to, as well as a reference to itself. So, if the main agent ever wants to spin off a copy of itself with its same prompt, it can do that."*(15:02~15:15) |
| **메모리 스토어** | *"we we we also support um long-running memory store that can be shared across sessions. Uh and we're going to use that so that different sessions can learn about different financial instruments, and they can share that knowledge uh with each other."*(16:33~16:48) |

- 자기 참조의 이유: *"sometimes you don't necessarily know what sort of tasks your session's going to want to do, but you have a general uh, a a idea that you want to have sub agents that, you know, spin up and do work."*(15:16~15:29)
- ⭐ *"It doesn't copy the transcript of that session into the sub agent. It just copies over the tool description and the schemas and the prompt into into that sub agent."*(15:37~15:47) *"this question has come up in the past"*(15:36~15:37)
- 설정의 *"staff the desk"* 버튼이 리소스를 만든다(16:00~16:05). 미리 만들어 둔 스킬을 지우고 다시 만든다(*"I was trying to do the magic uh cook show thing"* 16:14~16:19).
- 결과: *"has the skill that we described. It has sub agents uh with their own prompts and tools and permissions. Uh it has a prompt, and it has a model."*(17:08~17:16)
- 메모리 예고: *"I'll show you how you can use that memory long-running memory to keep improving your agents long-term over many, many uh sessions, days, months, years."*(16:48~16:56) — 이 편에 없음.

→ [[agent-skills]] · [[subagent-vs-thread-handoff]] · [[agent-memory]] · [[persistent-agent-teams]]

## 7. Outcome — 자기 감독 (17:28~18:37)

- ⭐ *"Outcomes is how we've created self-supervision. So, in an outcome, you tell Claude, 'This is your task. This is your rubric to evaluate your task.' It's going to go off and do that work. And then when it thinks it's completed, it's going to ask a sub agent to look at the rubric and the work that it Claude did uh and evaluate did it do it correctly and did it do it to completion. Uh if it does, then great. And if it doesn't, it will try again."*(17:45~18:13)
- 구현: UI에서 티커로 세션을 시작할 때마다 *"this user-defined outcome with a specific rubric, uh max iterations, um and a description of the task at hand"*(18:25~18:33)을 보낸다.

| Outcome 입력 | 발화 |
|---|---|
| 과제 설명 | *"a description of the task at hand"* |
| 루브릭 | *"a specific rubric"* |
| 최대 반복 | *"max iterations"* |
| 채점자 | *"a sub agent"* — 본 에이전트가 끝났다고 판단할 때 호출 |

→ [[generator-evaluator-pattern]] · [[outcome-engineering]] · [[managed-agents]](09-01의 `outcomes` 서술과 일치, 입력 항목이 처음 나온다) · [[token-roles]](grading)

## 8. Nvidia 리서치 세션 — 사전 실행분의 트레이스 (18:39~21:39)

- 라이브: *"Hey, I I want to analyze Nvidia."*(18:43~18:45) → *"about 10-ish minutes"*. 대신 전날 실행분을 보여 준다.
- Outcome 지시(19:09~19:54, 화자의 재진술): *"analyze Nvidia's most recent SEC quarterly filings. You're going to use Edgar identities (…) You have memory, so check if you've already done analysis previously and make sure that you use that instead of refiling[=refetching?] and researching things that you already know. (…) I want two deliverables. I want you to write a note in in my memory for that specific company. And I want you to write a scorecard in a well-defined structured output. And I want you to save that in a specific file location."*

| 단계 | 발화 |
|---|---|
| 메모리 확인 | *"It didn't find any notes in its memory store. It looked in a few different places."*(20:00~20:06) |
| 위임 결정 | *"I'm going to leverage my sub-agents to do the bulk of this work."*(20:09~20:13) — *"a financial expert analysis agent or extractor and then a risk evaluator analysis"*(20:13~20:22) |
| 관찰 | ⭐ *"you can see all of that in the console here for full observability. Each of these lines here represents a thread and a thread represents the work done by a sub-agent."*(20:22~20:31) |
| 합류 | *"when they were done, they let the main agent know (…) And then the main agent woke up, got that information from the sub-agents"*(20:34~20:44) → JSON 파일 생성, 메모리 갱신(20:46~20:53) |
| 자기 감독 | *"it kicked off a sub-agent to verify that the outcome that we defined is being met. It looked at the rubric. It analyzed all the work that was done in the session and analyzed the artifacts that it created and it decided in the end that this was satisfied"*(20:55~21:14) — 확인 항목: 스코어카드 전달, *"the numbers are well defined"*, 메모리 갱신이 맞음(21:14~21:20) |
| 산출 | *"we can extract the reports the scorecard from the session and download it. You put it in a database for this demo we put it locally"*(21:31~21:39) |

- ⚠️ 채점자가 **세션 전체 작업과 산출물**을 본다는 것(*"analyzed all the work that was done in the session and analyzed the artifacts"*)은 확인되지만, *"numbers are well defined"*가 수치의 **정확성**을 검증했다는 뜻인지는 발화되지 않는다. SEC 원문과 대조했다는 말은 없다.
- ⚠️ *"main agent woke up"*은 하위 에이전트가 끝날 때까지 본 에이전트가 쉬는 구조를 뜻하지만 메커니즘은 설명되지 않는다.

→ [[generator-evaluator-pattern]] · [[subagent-vs-thread-handoff]](콘솔 thread = 하위 에이전트 작업) · [[agent-memory]] · [[nvidia]](분석 대상, 결과 미발화)

## 9. 스킬은 살아 있는 산출물 (21:42~23:12)

- 다음 단계로 예고한 것: *"what if you want to do 100 or or 10 tickers at a time? Wouldn't it be great if I could chat with an agent to build a custom harness that could then delegate work for each of the tickers into a different session and then when it's all done aggregate the results"*(21:42~22:01). *"main agent is going to decide, 'Hey, I want to spin up 10 different sessions to do work.'"*(22:14~22:19) — 그 전에 단계를 건너뛰었다며 돌아간다.
- ⭐ *"I wanted to show you that these skills are live artifacts that you can update. So you can improve the skill in this case we're adding the ability to look at a new form and then when you do so any new sessions that the reference that skill will get that new information."*(22:30~22:46)
- *"You can look at previous sessions to see how they performed. We're going to see that at the end of this demo that that happens with with something we call dreaming"*(22:49~22:59) — 이 편에 없음.

→ [[agent-skills]] · [[skill-self-improvement]] · [[agent-dreaming]]

## 10. Q&A — 플랫폼의 경계 (23:16~35:06)

### Vault — placeholder와 egress 바꿔치기 (23:41~25:53)

- 질문: SEC 데이터 접근에 자격증명이 필요한가, *"how that credential injection or or brokering works?"*(23:41~23:55)
- 데모는 *"For this demo, we just inject that in the prompt"*(23:59~24:01) — SEC는 이름·이메일만 요구한다.
- ⭐ *"in a real production application, we would use something called Vaults. Uh, the way Vaults work is you define a secret uh that you want to you inject in an environment variable. And instead of putting the real secret in, what we put is in is a placeholder. Uh, and then when Cloud[=Claude] is doing work and it wants to use that environment variable, um, it just injects the placeholder value. We at Egress[=at egress] swap it out for the real value only on the host domains that you specified are allowed for that secret. So, if you say uh my super secret MVAR[=env var] can only be used for the SEC, and then Cloud[=Claude] tries to use it for anthropic.com, we won't inject we wouldn't do the swap. But, when it tries to call the SEC.com[=sec.gov?], it would do the swap for that."*(24:01~24:45)
- 보충(Priyanka 추정): *"go create a Vault, give it a name, you'll get an ID, and then you essentially include that ID in your session as a way for us to authenticate with your MCPs, your CLI (…) you could do like a Google Workspace CLI that you install on your sandbox, and then you can give us like your API keys or environment credential"*(24:50~25:07). *"vaults also work with OAuth credentials"*(25:13~25:15).
- 콘솔: *"in a vault you would bundle credentials. Um so, you can have MCP auth. Um maybe you do notion you know, we have a few predefined things for OAuth (…) whenever you reference a session, you inject that vault ID, and it will bundle all the credentials into your session, and whenever it tries to use any of the domains that you specified in your credentials, it will swap for the real um credential instead of the placeholder."*(25:23~25:53)

→ [[credential-injection-outside-sandbox]](셋째 메커니즘) · [[anthropic-managed-agents]](vault + proxy) · [[prompt-injection]](샌드박스에서 env를 읽어도 placeholder뿐) · [[lethal-trifecta]](외부 전송 능력을 도메인 단위로 묶는다)

### Agent SDK와의 관계 (25:55~26:58)

- 질문: *"presumably this is built on top of the Agent SDK. I want to know what part of the capabilities are in the Agent SDK layer, and what's outside of it?"*(26:06~26:14)
- ⭐ 답 1: *"the the Agent SDK is packaged for uh like more more It's a headless Cloud[=Claude] Code version. So, it's actually we built a generic version of that. We took taking a lot of inspiration about the benefits and lessons from the Agent SDK, but we've rebuilt uh the harness to be a more generic not just coding specific thing."*(26:15~26:34) — *"So, it's sort of a fork?" "Uh yeah."*(26:34~26:36)
- 답 2: *"it's basically like it's own harness. Agent SDK is basically like a Cloud[=Claude] Code in the form of a binary that you can take and run wherever you want. This is a fully hosted solution running in our cloud, and we have our own harness that's heavily inspired by Cloud[=Claude] Code's harness, and we frequently stay stay in touch for like any enhancements across the board."*(26:37~26:58)

→ [[claude-agent-sdk]] · [[agent-harness-design]] · [[claude-code]]

### 반복·토큰 폭주의 가드레일 (27:02~27:47)

- 질문: 여러 에이전트를 오케스트레이션할 때 *"some guardrails that those agents would not go into loops and like consume a lot of tokens"*(27:06~27:13)
- ⭐ *"some of that we leave up to you to orchestrate and figure out. (…) if you're building these sort of custom harnesses, there's nothing stopping you from using uh like other providers if you wanted to do a sort of multi uh multi-provider system. Um we are exploring the idea of what it means to do like budget tighter budget controls so you can say use no more than this amount of money per session, use no more than this amount of tokens per session. Um but that's not something we offer today."*(27:17~27:44)

→ [[fixed-budget-alpha]] · [[agentic-misbehavior]] · [[harness-as-platform]](예산 강제를 하네스 층에 둔 [[southbridge|Southbridge]] Hank Weave와 대비)

### 조종과 분기 (27:50~28:48)

- 질문: 콘솔에서 매니저·하위 에이전트 트랜스크립트를 보다가 잘못된 경로를 발견하면 *"go back to that point in time and kind of start over, try it with some additional guidance?"*(28:10~28:14)
- ⭐ Gabe: *"You can steer it. (…) I could send a new user uh dot message event and steer the agent. Uh it'll queue it up. It's, you know, you can send like 10 messages at a time and it's fine. We don't currently have a way for like rewind and roll forward."*(28:17~28:36)
- Priyanka(추정): *"session forking is essentially what you're asking for. And we we've had a couple a few customers who've asked for that. It's it's on our road map, so hopefully we'll have it at some point."*(28:40~28:48)

→ [[steering-altitude]] · [[context-resets-and-compaction]] · [[action-reversibility]]

### 공유 메모리와 lock-in (29:02~31:14)

- 질문: 수십·수백 명이 같은 앱을 쓸 때 *"Is there a collective memory"*(29:31~29:37)
- ⭐ *"We have it today. We actually use it in this demo. So, we use the a memory store um that allows you to share knowledge across sessions. (…) I'll show you at the end how you can consolidate that knowledge over time using dreaming, so that you can continuously improve the memory stores as different agents run into different edge cases and collectively learn from each other."*(29:39~30:09)
- lock-in 질문(AWS Bedrock·자체 클러스터, 30:09~30:30): *"all of this is API based, so you you can extract the memories and put them in different systems if you want to. We don't currently support out of the box other memory providers in the session, but you would just build an MCP or a custom tool to do so."*(30:32~30:48)
- ⭐ 보충(Priyanka 추정): *"we do allow for attaching multiple memory stores. So you can imagine having a user level memory store and then having some sort of org wide memory store and then you bring both to each session (…) None of this is locked in and you can like take your data and go anywhere else if you wanted to. Everything is an API call."*(30:53~31:14)

→ [[agent-memory]] · [[agent-fleet-learning]] · [[agent-dreaming]] · [[multiplayer-agent-context]]

### 하위 에이전트는 누가 채점하나 (31:16~32:50)

- 질문: *"the a grader is at the main agent level, right? Like so how do you grade these sub agentic tasks"*(31:20~31:28)
- ⭐ *"Sub agents in the way that we've built them are meant to augment your context and leverage the capabilities of your of your session by collaborating between them. The outcome definition happens at like an overall arching session level. (…) There is no currently support for like a sub outcome definition."*(31:34~32:06)
- 후속: 하위 에이전트의 탈선에서 dreaming이 배우는가 → ⭐ *"Today the dreaming's constrained to memory stores. (…) the way dreaming works is they will analyze the transcripts and the memories created across multiple sessions so that it can update its memories so that future agents know what to pull. But you can imagine that we can continue to expand that for skills and for prompts and for agent definitions so that you can you have this continuous learning functionality. But right now we just have it for for memory stores."*(32:21~32:50)

→ [[generator-evaluator-pattern]] · [[agent-dreaming]] · [[continual-learning]]

### 비공개 데이터 — MCP + Vault, MCP 터널, 자체 호스팅 샌드박스 (33:03~34:12)

- 질문: 사내 데이터(*"traditional store or rack[=RAG]"*)를 CLI·MCP로 노출하는 *"safe path"*(33:03~33:18)
- ⭐ 세 경로: ① *"you would just create an MCP, give it give it the authentication vault and it would just be able to call your directly."* ② *"If you don't want to expose your MCP to the internet, we have a feature called MCP tunnels which lets you create a tunnel from your um network into ours"* ③ *"If if that's too big a barrier to climb, we do support self-hosted sandboxes so that you can bring your own sandbox which has which is peered with your network and has access to your applications and services and the agent would just call the sandbox that you manage and host"*(33:22~34:12)

→ [[model-context-protocol]] · [[brain-hands-decoupling]] · [[credential-injection-outside-sandbox]] · [[in-house-ai-data-boundary]]

### 환경 종속성 (34:15~34:57)

- *"It's a creation time and then we'll cache it and reuse that environment across like re- re-instantiations of the sandbox."*(34:27~34:36)
- 내부 패키지는? *"Right now, they are all they all have to be accessible via NPM, Cargo, pip, whatever. But, you can upload files directly into the session if or GitHub repos if you want to install them that way."*(34:42~34:56)
- deployments 탭 질문에는 *"I'm going to get to it"*(35:01~35:03)으로 답하고 영상이 끝난다.

→ [[agent-sandboxing]] · [[pets-vs-cattle]](environment = 재생성 가능한 레시피)

## 이 위키와의 연결

### 이어지는 것

- **[[managed-agents]]: 리소스 모델과 "지금 없는 것"이 팀의 입으로.** 지금까지 이 위키의 Managed Agents는 엔지니어링 글([[anthropic-managed-agents]])의 인터페이스 시그니처, [[katelyn-lesse|Katelyn Lesse]]의 설계 이유(09-01), [[angela-jiang|Angela Jiang]]의 메타 하네스 층(09-18), [[lamis-mukta|Lamis Mukta]]의 memory·dreaming API(10-01), 그리고 같은 워크숍 1부의 설계 진화 이야기였다. [[tech-bridge-claude-managed-agents-workshop-1|1부]](7절)가 개념으로 소개한 environment · agent · session · event를 이 편은 콘솔과 코드로 만들고, 그 위에 **개발자가 실제로 만지는 단위**(agent 버전 · skill · memory store · vault · outcome)를 더해 처음 나란히 보여 준다. 그리고 **없는 것 넷**(세션당 예산·토큰 상한, rewind·fork, 메모리 밖 dreaming, 외부 메모리 공급자)을 명시한다.
- **[[credential-injection-outside-sandbox]]: 셋째 메커니즘.** 엔지니어링 글은 *bundled with resource*(Git 토큰으로 clone)와 *vault + proxy*(MCP 도구, OAuth)를 들었다. 이 편의 Vault는 **환경변수에 placeholder를 두고 egress에서 허용 도메인에만 진짜 값으로 바꾼다.** 샌드박스 안 CLI(Google Workspace CLI 예)도 같은 방식으로 쓴다. 비밀이 샌드박스에 없다는 원칙은 같고, 범위가 **도메인 단위**로 묶인다. 프롬프트 인젝션이 env를 읽어 다른 도메인으로 보내도 placeholder만 나간다([[lethal-trifecta]]의 셋째 다리를 도메인으로 자른다).
- **[[generator-evaluator-pattern]]·[[outcome-engineering]]: Outcome의 모양.** 09-01은 *"루브릭을 주면 채점하는 두 번째 에이전트를 프로비저닝"*이었다. 이 편에서 입력은 과제·루브릭·**max iterations**이고, 채점자는 본 에이전트가 끝났다고 판단할 때 부르는 **하위 에이전트**이며, 세션 전체 작업과 산출물을 본다. 범위는 **세션 수준 하나**다(*"no currently support for like a sub outcome definition"*).
- **[[subagent-vs-thread-handoff]]: 자기 참조 하위 에이전트.** 같은 프롬프트로 자기 사본을 띄우되 *"It doesn't copy the transcript"* — 컨텍스트 격리가 기본값이다. 콘솔에서는 하위 에이전트 작업 하나가 **thread** 하나로 보인다.
- **[[brain-hands-decoupling]]: hands를 고객 쪽에.** 자체 호스팅 샌드박스 공급자로 Vercel·Modal·Daytona·Google Cloud·AWS가 이름으로 나온다. 엔지니어링 글이 1세대 설계의 문제로 든 *customer VPC network peering*이, 이 편에서는 **자체 호스팅 샌드박스를 고객 네트워크에 peer하는** 선택지로 돌아온다(33:56~34:04). 09-01의 *"샌드박스 자체 호스팅, MCP 터널"*과 일치한다.
- **[[agent-skills]]: 스킬 = 버전이 바뀌는 공유 자원.** 갱신이 그 스킬을 참조하는 **새 세션**에 전파된다. 그리고 워크숍 교재 자체가 Claude Code 스킬(`workshop start`/`workshop next`)이다.
- **[[agent-memory]]·[[agent-fleet-learning]]: 공유 메모리 스토어.** 세션 간 공유, 세션당 여러 스토어(사용자 수준 + 조직 수준), API로 반출 가능. 외부 메모리는 MCP·맞춤 도구로 붙인다.

### 갈리는 것

> ⚠️ **Contradiction: dreaming은 스킬을 쓰는가.** [[tech-bridge-claude-platform-agent-era]](09-01)는 dreaming을 *"과거 세션을 되돌아보며 **메모리에 쓰고 스킬을 작성해** 개선"*으로 적었다. 이 편의 제품 팀은 *"Today the dreaming's constrained to memory stores (…) But right now we just have it for for memory stores."*(32:21~32:50)라고 하고, 스킬·프롬프트·에이전트 정의로의 확장은 *"you can imagine that we can continue to expand"*(32:40~32:46)로 **미래형**이다. [[tech-bridge-anthropic-dreaming-memory]](10-01)도 출력으로 메모리 스토어만 말했다. 09-01 진술이 방향(비전)을 말한 것이었을 수 있다. 2026-10 시점 제품 기준으로는 **메모리 전용**이 맞다.

> ⚠️ **Contradiction(약): 메타 하네스인가, 자체 하네스인가.** [[anthropic-managed-agents]]는 Managed Agents를 *"어떤 harness/sandbox가 들어올지는 비opinionated"*인 메타 하네스로, *"[[claude-code|Claude Code]] 같은 범용 harness, task-specific harness 모두 수용"*으로 그렸다. 이 편의 답은 *"we have our own harness that's heavily inspired by Cloud[=Claude] Code's harness"*(26:48~26:52)이고 Agent SDK의 *"sort of a fork"*(26:34~26:36)다. 사용자가 만드는 *"custom harness"*는 호스팅 하네스를 갈아 끼우는 것이 아니라 **맞춤 도구로 세션 여러 개를 바깥에서 조율하는 층**(05:25~05:35, 14:26~14:35)이다. 층은 다르다. 글은 인터페이스 설계 원칙을, 이 편은 현재 제공되는 제품을 말한다. 그래도 사용자 쪽에서 **하네스를 교체할 수 있다는 말은 이 편에 없다.**

> ⚠️ **긴장(약): rewind.** [[anthropic-managed-agents]]는 session을 *"context window 밖의 context object"*로 두고 `getEvents()`로 *"특정 시점 직전으로 rewind"*한 위치 조각을 읽을 수 있다고 했다. 이 편에서 사용자가 묻는 rewind는 **실행을 그 시점부터 다시 돌리는 것**이고 답은 *"We don't currently have a way for like rewind and roll forward"*(28:31~28:36), session forking은 로드맵이다. 하네스가 과거 이벤트를 **읽는** 능력과 사용자가 세션을 **분기하는** 기능은 다르다. 로그가 durable하다는 것이 곧 분기 기능은 아니라는 점이 확인된다.

> **예산은 사용자 몫.** 세션당 돈·토큰 상한은 *"not something we offer today"*(27:43~27:44)이고 반복 폭주 방지는 *"we leave up to you"*(27:17~27:19)다. [[tech-bridge-just-in-time-ontology|적시형 온톨로지 편]]의 Hank Weave는 *"checkpointing, rollback, budget enforcement, everything built in"*을 하네스 층의 조건으로 들었고, [[fixed-budget-alpha]]는 예산 고정을 실험 설계의 전제로 삼는다. 호스팅 메타 하네스에 그 층이 아직 없다는 것이 기록된다.

> **lock-in 답변의 범위.** *"None of this is locked in (…) Everything is an API call."*(31:09~31:14)은 **메모리 데이터의 반출**에 대한 답이다. 하네스·Outcome·Vault·dreaming 같은 기능의 이식성은 말하지 않는다. 다중 공급자는 *"custom harnesses"*를 직접 만들 때의 이야기다(27:21~27:31).

## 해소하지 않고 표시만 한 것

- 1부와 2부 사이의 잘린 구간 여부(01:06 *"one more time"*). 1부의 1·2차 세션 저장 설계 내용(이 편 00:00 질문의 대상).
- 저장소 주소(QR만), dispatch analysis의 정확한 철자·스키마, *"staff the desk"* 이외의 설정 화면.
- Nvidia 스코어카드의 내용, 루브릭 문구, max iterations 값, 채점자의 *"numbers are well defined"*가 무엇을 확인했는지.
- *"cloud platform on AWS"* = Claude Platform on AWS(판독). *"SEC.com"* vs sec.gov. *"vaults also work with OAuth credentials for peace"*의 *"peace"*. *"rack"* = RAG.
- Agent SDK 답변 두 개의 화자, Q&A 보충 답변의 화자(Priyanka 추정).
- *"main agent woke up"*의 메커니즘. 사용자 메시지 큐의 한도(*"like 10 messages at a time"*가 한도인지 예시인지).
- deployments API, map-reduce 오케스트레이션, dreaming 시연 — 3/4·4/4 대기.
- 행사·녹화일: 설명란의 *"2026년 AI Engineer World's Fair"*는 발화되지 않는다.

## 등장 개체

- 인물: [[priyanka-phatak|Priyanka Phatak]](이 편에서는 *"Priyanka"* 11:04, ASR *"Bianca"* 11:54. 성은 이 편 설명란에서만) · [[gabe-cemaj|Gabe Cemaj]](*"Gabe"*, 1부 en-orig *"Gabe Semach"*) · Rohan·Travis(마이크 도우미, 페이지 없음)
- 조직: [[anthropic|Anthropic]] · [[ai-engineer|AI Engineer]](원본 채널·행사, 설명란) · [[vercel|Vercel]] · Modal · Daytona(자체 호스팅 샌드박스 공급자, 페이지 없음) · [[google-cloud|Google Cloud]] · AWS(Bedrock은 질문자가 언급) · SEC(EDGAR, 데모 데이터 원천) · [[nvidia|Nvidia]](분석 대상)
- 제품: [[managed-agents|Claude Managed Agents]](en-orig *"cloud-managed agents"*, *"CMA"*) · [[claude-code|Claude Code]](en-orig *"Cloud Code"*) · [[claude-agent-sdk|Claude Agent SDK]] · [[bun|Bun]] · Google Workspace CLI · Notion(Vault의 OAuth 예) · PagerDuty(화면 알림, 무관)
- 개념: [[credential-injection-outside-sandbox]] · [[generator-evaluator-pattern]] · [[outcome-engineering]] · [[agent-dreaming]] · [[agent-memory]] · [[agent-fleet-learning]] · [[subagent-vs-thread-handoff]] · [[agent-skills]] · [[skill-self-improvement]] · [[brain-hands-decoupling]] · [[agent-sandboxing]] · [[agent-harness-design]] · [[harness-as-platform]] · [[fixed-budget-alpha]] · [[agentic-misbehavior]] · [[steering-altitude]] · [[action-reversibility]] · [[context-resets-and-compaction]] · [[model-context-protocol]] · [[lethal-trifecta]] · [[prompt-injection]] · [[least-privilege-connectors]] · [[in-house-ai-data-boundary]] · [[multiplayer-agent-context]] · [[continual-learning]] · [[token-roles]] · [[persistent-agent-teams]] · [[pets-vs-cattle]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=U0ZCwwG8sac> (35:09, `upload_date` 2026-10-18)
- raw: `01.raw/articles/2026-10-18_Claude Managed Agents로 리서치 에이전트를 만들어봅니다 (2-4).md`
- 시리즈: [[tech-bridge-claude-managed-agents-workshop-1]](1부, `3iOP4cXChAc`) · 3/4·4/4 미업로드
- 설명란 링크(⚠️ 열어 보지 않았다): [Claude Managed Agents 문서](https://platform.claude.com/docs/en/managed-agents/overview) · [Managed Agents 엔지니어링 글](https://www.anthropic.com/engineering/managed-agents) → [[anthropic-managed-agents]] · <https://github.com/gcemaj> · <https://ai.engineer>
- 같은 제품의 다른 서술: [[anthropic-managed-agents]] · [[tech-bridge-claude-platform-agent-era]] · [[tech-bridge-tokens-should-have-jobs]] · [[tech-bridge-anthropic-dreaming-memory]]
- [[tech-bridge]] · [[managed-agents]] · [[priyanka-phatak]] · [[gabe-cemaj]]
