---
title: "Tech Bridge — AI 에이전트로 코딩할 때 알아야 할 5가지 개념 (Cedric Clyburn, IBM Technology): 구현에서 지휘로 — 스펙·컨텍스트·루프, 모델의 기초, 일회용 샌드박스, 그리고 \"AI는 새로운 전기\""
type: source
tags: [developer-role, inflection-point, autocomplete-to-agents, spec-driven-development, implementing-to-conducting, conductor-metaphor, architecture, goal-decomposition, context-engineering, context-window, loop-engineering, llm-fundamentals, time-estimation, gpu-memory, kv-cache, agent-skills, automations, sub-agents, prompt-injection, lethal-trifecta, sandboxing, attack-surface, ai-as-electricity, ibm, explainer, video]
source-url: https://www.youtube.com/watch?v=T8UcAUunSMw
source-type: video
author: Tech Bridge (한영자막 재배포) · 제작 [[ibm|IBM Technology]](설명란 링크 기준) · 화자 [[cedric-clyburn|Cedric Clyburn]](⚠️ 설명란에만 — 이번 설명란은 "IBM Technology의 Cedric Clyburn", 09-15 설명란은 "Red Hat 수석 개발자 애드보킷")
date-published: 2026-10-16
ingested: 2026-10-17
created: 2026-10-17
updated: 2026-10-17
---

# Tech Bridge — AI 에이전트로 코딩할 때 알아야 할 5가지 개념 (Cedric Clyburn, IBM Technology)

[[tech-bridge|Tech Bridge]]가 한영자막을 입힌 **9:53 1인 해설, 공식 챕터 10개.** 원어는 영어이고 ko는 기계 번역이다. 화자 [[cedric-clyburn|Cedric Clyburn]]의 **두 번째 소스**다(첫 소스는 [[tech-bridge-ai-engineer-three-tier-skill-stack]], 09-15 업로드). 이번에도 **이름은 설명란에만** 있고, 소속 표기가 첫 소스(Red Hat)와 다르다(이번엔 *"IBM Technology의"*). 측정은 없다. 일화(조종사, 화자 팀의 체감), 가정 예시(RPG), 그림 설명(GPU 메모리, PR을 읽는 에이전트)으로 된 **입문 해설**이다. 테제:

> **AI는 개발자를 대체하지 않고 개발의 모양을 바꾼다. 기능 전체를 에이전트에 맡기는 지금, 개발자의 일은 구현에서 지휘로 옮겨 간다. 프롬프트 대신 명세를 쓰고, 컨텍스트 창의 한계를 관리하고, 사람이 목적을 정하면 AI가 끝날 때까지 도는 루프를 설계한다. 이를 위해 모델의 기초를 알아야 하고, 에이전트를 일회용 샌드박스에 넣어야 한다. AI가 새로운 전기라면 그 망을 유지할 엔지니어가 필요하다.**

> *"what AI will do is change what software development looks like."* (00:35~00:40) · *"Next is the shift from implementing to conducting"* (02:27~02:30) · *"loop engineering works like a recursive goal where you as a human define the purpose and the AI iterates until it's complete"* (04:40~04:49) · *"that's why teams are running coding agents inside of disposable sandboxes whenever possible."* (08:04~08:10)

이 위키에 새 개념 페이지는 **필요하지 않다**(선택 제안 1개, 아래). 대부분 기존 페이지의 **입문 수준 증언**이다 — [[spec-driven-development]](동기: 프롬프트는 모델마다 다르게 해석되고 AI와 *"argue"* 해야 한다), [[orchestras-not-factories]](*"a conductor, a captain"* — Holtz와 같은 은유를 다른 화자가), [[context-engineering]](컨텍스트 창의 **자원 한계**로 정의하고 나중엔 automations·sub-agents까지 넣는다), [[loop-is-the-product]]·[[inner-outer-meta-loops]](*loop engineering* 의 **단일 루프 정의** — Knox의 meta loop와 다른 지시 대상), [[agent-skills]](*"markdown files"* — ⚠️ *"with each AI request"* 는 progressive disclosure와 긴장), [[scheduled-agent-automations]] · [[subagent-vs-thread-handoff]] · [[prompt-injection]]·[[lethal-trifecta]](세 조건을 **이름 없이** 같은 구조로), [[intelligence-as-infrastructure]]·[[intelligence-abundance]](전기 비유의 **노동 쪽** 판본).

ASR·ko 보정: ko는 **장의 제목어를 여럿 잃는다** — *spec-driven development* → "사양에 따라"(02:06~02:08), *conducting* → "관리"(02:29, `en` 공유), *context engineering* → "공학 … 맥락"(04:24~04:26), *skills* → "기술"(04:19, 06:21), *prompt injections* → **"주사 / 제시된 질문들"**(07:23~07:25). **뒤집힌 문장**: 프롬프트 *대신* → "명령어를 통해 이루어질 수 있습니다"(01:51~01:54), 세 조건의 결합이 유출을 *가능하게 한다* → **"에이전트 덕분에 당신의 일이 매우 수월해질 수 있습니다"**(07:38~07:40), 에이전트가 *침해당하면* → "에이전트가 공격하는 경우"(08:21), *shifting away from manually writing code to designing* → **"설계를 위해 코드를 수동으로 작성합니다"**(09:36). 주어 교체: 조종사의 에이전트 팀 → "저는"(00:15, `en` 공유), 모델의 추정 → "제가 예상하기로는"(05:11). en-orig ASR *"tax surface"* → attack surface(08:19). 전체 보정표는 raw 헤더: `01.raw/articles/2026-10-16_AI 에이전트로 코딩할 때 알아야 할 5가지 개념.md`.

> ⚠️ **화자 이름·소속은 설명란에만.** 자막에는 이름도 소속도 없다. 이번 설명란은 *"IBM Technology의 Cedric Clyburn"*, 09-15 업로드 설명란은 *"Red Hat의 수석 개발자 애드보킷 Cedric Clyburn"* — **두 설명란의 소속 표기가 다르다.** 어느 쪽인지(또는 둘 다인지) 이 소스로는 정하지 않는다. 설명란 링크가 전부 `ibm.biz`·IBM 계열 채널이라 **제작 채널은 [[ibm|IBM Technology]]로 판정**한다(09-15와 같은 처리).
>
> ⚠️ **"다섯 가지 개념"의 목록이 발화되지 않는다.** *"I'll break down five key concepts (…) the last one is the most important."*(00:40~00:50) 서수는 *"first off is the inflection point"*(00:50) · *"Next is the shift from implementing to conducting"*(02:27) · *"Finally, the future."*(08:22)뿐이다. 아래 소제목은 정리자가 화자의 전환 문장을 따라 붙였다. 다섯이 무엇인지는 판독하지 않았다.
>
> ⚠️ **수치가 없다.** *"weeks, if not months, now in just a few minutes"*(01:04~01:09)는 화자와 팀의 체감이고, RPG의 *"several weeks to several months"* 대 *"within 5 minutes"*(05:07~05:27)는 *"might"* 로 말한 가정 예시다.
>
> ⚠️ **인용·일화는 화자를 거친다.** *"AI is becoming the new electricity"* 는 **화자가 기억으로 옮긴 [[andrew-ng|Andrew Ng]]의 말**(*"I remembered his quote"* 08:28~08:32)이고 원 출처는 발화되지 않는다. 화자가 Ng와 *"work with"*(08:26~08:28) 했다는 일의 내용도 없다. 조종사 일화(00:00~00:29)에는 이름·도구가 없다.

## 1. 도입 — 조종사의 에이전트 팀, 그리고 "대체하지 않는다" (00:00~00:52)

- ⭐ 일화: *"Just recently, I was talking to a software engineer, and mid-conversation, he stops to check his phone, approve a code change, and continue talking. It turns out he had multiple agents running in the background for all of the different roles that you would typically have on a team. So, he had a developer, a code reviewer, an operations, and many, many more. And it turns out this guy wasn't a software engineer by trade, he was actually a pilot."*(00:00~00:29) ⚠️ ko·`en`은 이 팀을 화자의 것으로 옮긴다(*"So I had a developer"*/"그래서 저는").
- *"when people keep asking whether AI will replace developers, I always say no. I've actually seen more people get into coding because of AI. But, what AI will do is change what software development looks like."*(00:25~00:40)

→ [[agent-attention-management]](휴대폰으로 승인하는 역할별 에이전트) · ⚠️ "AI 덕분에 코딩에 들어오는 사람이 늘었다"는 관찰이고 수치는 없다.

## 2. 변곡점 — 자동완성에서 기능 단위 위임으로 (00:50~01:49)

- *"over the past year, me and my team have all started to say the same thing. That AI is able to complete tasks that typically would have taken us weeks, if not months, now in just a few minutes."*(00:55~01:09)
- 이전: *"I used to use AI as an autocomplete in order to help me write better functions and test, but I would often spend more time fixing AI output if[=than if] I had just written it myself."*(01:09~01:20)
- ⭐ 지금: *"we just commonly assign entire features to AI coding agents, such as not just writing the code, but also understanding the code base and what's happening inside, writing and running those tests, and merging those changes into the actual code base. All from a single prompt or loop that can define when this agent should finish."*(01:23~01:49) ⚠️ ko·`en`은 *entire features* 를 "함수"/*"complete functions"* 로 옮긴다.

→ [[goal-level-delegation]] · [[verifiable-goals]](*"define when this agent should finish"*)

## 3. 스펙 주도 개발 — 프롬프트와 "논쟁"하지 않기 위해 (01:49~02:27)

- ⭐ *"instead of doing all of this via prompts, which can be interpreted differently by different types of coding models and having to argue with the AI in order to get the right output, what we typically now see is an approach that's known as spec-driven development where by creating the specification of the requirements and all the outcomes that we would like to see with the software project, we can then send that off to the AI coding agent and model in order for us to create this project and its artifacts."*(01:49~02:27)
- 화자가 드는 SDD의 이유는 둘이다. **모델 간 해석 차이**와 **반복 수정의 비용**. 도구(Spec Kit 등)·형식·단계(plan/tasks)는 말하지 않는다.

→ [[spec-driven-development]] · ⚠️ ko는 동기 문장을 **뒤집는다**(*instead of … via prompts* → "이 모든 것은 명령어를 통해 이루어질 수 있습니다" 01:51~01:54).

## 4. 구현에서 지휘로 (02:27~03:54)

- *"Next is the shift from implementing to conducting because I mentioned earlier that I don't think developers are going to disappear, but the priorities are definitely changing"*(02:27~02:38)
- 예전 병목: *"for decades the biggest bottleneck to taking code and shipping that was one, how fast you could write that code and two, how high-quality that code output was. And companies would hire who they thought were the best competitive programmers"*(02:38~02:55)
- 지금은 모델이 *"Java or Python or Rust"* 를 알고 *"tickets that are coming in from the team"* 을 *"staging, production, QA"* 까지 옮긴다(02:58~03:21).
- ⭐ *"if this can already be done with AI, the implementing phase, well then what becomes important for developers? That my friends is being a conductor, a captain, someone who can make important architectural decisions that will impact the software in a year from now for example."*(03:21~03:38)
- *"instead of writing functions yourself by hand, what we see now is defining goals that will break work down into specific milestones that can then be completed by a AI model or agent."*(03:38~03:54)

→ [[orchestras-not-factories]](지휘자 은유) · [[architecture-as-remaining-art]] · [[goal-level-delegation]] · [[taste-vs-judgment]]

## 5. 컨텍스트 관리와 루프 엔지니어링 (03:54~04:52)

- ⭐ 정의: *"context management is the idea of understanding the resource limitations of an AI model's context window and all of those extra components that are being added in addition to your code base when you're using it for engineering, such as tools or skills, or MCP servers to provide external data to the model. So, that's context engineering"*(04:02~04:26) — *management* 로 시작해 *engineering* 으로 부른다.
- ⭐ *"there's also the idea of loop engineering. And what loop engineering is is where instead of you being the person that prompts the agent back and forth and you continually iterate, well, what you do is you design a system that does it instead. So, loop engineering works like a recursive goal where you as a human define the purpose and the AI iterates until it's complete with whatever the task was that needed to be done."*(04:26~04:52)
- 화자의 loop engineering은 **한 작업의 반복 루프**(사람 = 목적, AI = 완료까지 반복)다. 검증 기준·종료 조건의 형식·실패 시 처리는 말하지 않는다.

→ [[context-engineering]] · [[context-rot]] · [[model-context-protocol]] · [[loop-is-the-product]] · [[inner-outer-meta-loops]] · [[ralph-wiggum-method]](⚠️ 화자는 이 이름을 쓰지 않는다)

## 6. 모델의 기초 — 시간 감각, GPU 메모리, KV 캐시 (04:52~06:14)

- *"However, understanding the fundamentals of AI models is really important, as well."*(04:52~04:56)
- ⭐ 예시: *"If I was to ask an AI model, how long would it take to build a third-person role-playing game, an RPG, it might say, "Hey, uh several weeks to several months." (…) But, if you ask that same model with a coding agent in order to actually uh build that game, well, it might give you a working example within 5 minutes, right?"*(04:56~05:27) → *"that's one of the limitations of LLMs, right? It doesn't quite understand time and memory like we do as humans."*(05:29~05:38) ⚠️ 가정 예시이고 어느 모델인지 없다. ko는 대상을 "인공지능을 개발하는 데"로, 추정의 주어를 "제가"로 바꾼다.
- *"Another example is how LLMs are stored in GPU memory and how you actually use them at inference. So, here you have the model's weights loaded into the GPUs memory. And here you have the KV cache, which is uh generated and stored as you request the model and get results back."*(05:43~06:07) — 그림을 가리키는 설명이다(화면 미확인). 메모리 용량·컨텍스트 길이와의 관계는 말하지 않는다.
- *"understanding how all of this works is going to give you a huge advantage as you proceed to use AI models as a software developer."*(06:07~06:14) — 어떤 이점인지는 구체화하지 않는다.

→ [[three-tier-ai-skill-stack]](같은 화자의 "기초를 건너뛰지 말라") · [[read-fluency-for-agent-output]]

## 7. 스킬·자동화·서브에이전트 (06:15~07:18)

- *"if we add on context engineering capabilities that we just talked about, such as skills, which are markdown files that add reusable and contextual information about your code and project with each AI request"*(06:15~06:30)
- *"as well as automations, so being able to set up kind of cron jobs and event-triggered (…) actions. So, for example, if someone comes to your website and fills in a form, that can kick off automation"*(06:30~06:45)
- *"sub-agents are essentially (…) used for situations where maybe you're investigating a problem with the code source and you send off a sub-agent to go see uh how that library works and test it out itself and then come back to the main agent."*(06:45~07:03)
- *"all of these are different examples of contextual engineering capabilities that you can start adding to your software engineering process (…) And these are the fundamentals, which are important to know."*(07:03~07:18) — 화자는 skills뿐 아니라 **automations·sub-agents까지 context engineering의 기능**으로 묶는다.

→ [[agent-skills]] · [[scheduled-agent-automations]] · [[subagent-vs-thread-handoff]]

## 8. 프롬프트 인젝션과 일회용 샌드박스 (07:20~08:22)

- *"just like how SQL injections can infiltrate our applications, prompt injections are also very real."*(07:20~07:27)
- ⭐ 성립 조건: *"That's because AI systems have access to sensitive data, they have exposure to the web, and also the ability to send data. And the combination of all three for your agent makes it quite possible for your AI agent to say for example read a pull request online. (…) and be tricked into sending your credentials to somebody else."*(07:27~07:55) — **[[lethal-trifecta|치명적 3요소]]와 같은 구조**(비공개 데이터 · 신뢰할 수 없는 콘텐츠 · 외부 전송)다. 화자는 이 이름도 Simon Willison도 말하지 않는다.
- 예: *"this is our little key with our private credentials that we have on our desktop. And this could happen without you even knowing."*(07:55~08:04)
- ⭐ 처방: *"that's why teams are running coding agents inside of disposable sandboxes whenever possible. So you can see this as an example where we have the agent and the code that we're working with sandboxed in its own environment in order to reduce the tax surface[=attack surface] if an AI agent gets compromised."*(08:04~08:22)
- 처방은 **샌드박스 하나**다. 세 조건 중 무엇을 끊는지(데스크톱 자격증명에 닿지 못하게 하는 것으로 읽힌다), 네트워크 차단이나 자격증명 주입 방식은 말하지 않는다.

→ [[prompt-injection]] · [[lethal-trifecta]] · [[credential-injection-outside-sandbox]] · [[brain-hands-decoupling]] · ⚠️ ko는 결합의 위험을 **"일이 매우 수월해질 수 있습니다"**(07:38~07:40)로 뒤집는다.

## 9. AI는 새로운 전기 — 망을 유지하는 엔지니어 (08:22~09:23)

- *"Finally, the future. Because I had the chance recently to work with AI legend Andrew Ng and I remembered his quote that AI is becoming the new electricity, right?"*(08:22~08:35)
- ⭐ *"there's also entire industries and thousands of people who for example work at substations to make sure that the grid is working, right? They also are in the field helping people for example to repair street lights and help out at their home. And they're also making sure that everyone can access electricity, right? And AI might follow the same path where we're going to need engineers who can maintain these systems, right? The grid to be able to ensure connectivity so that people can access these AI models and systems, ensure that AI systems are safe and reliable and have quality."*(08:45~09:23)
- 비유의 초점은 **노동**이다. 전기가 일자리를 없애지 않고 유지·접근성의 직업을 만들었듯 AI도 그럴 *"might"* 라고 말한다. 가격·발전량·접근 형평(Altman)이나 토큰 = kWh(Huang)를 말하지 않는다.

→ [[intelligence-as-infrastructure]] · [[intelligence-abundance]] · [[andrew-ng]]

## 10. 맺음 (09:23~09:53)

- *"So don't worry, I think software engineering isn't going anywhere, but I'm optimistic for the future for developers and what they'll be able to create. And yes, it is shifting away from just manually writing code to designing and orchestrating systems and AI agents. And those who excel in the architectural and critical thinking phases will become even more valuable as AI coding agents continue to improve."*(09:23~09:51)

→ [[architecture-as-remaining-art]] · [[taste-vs-judgment]]

## 이 위키와의 연결

### 이어지는 것

- **[[cedric-clyburn]] — 같은 화자의 두 번째 입문 해설.** 첫 소스의 *"코드 생성이 쉬워졌으니 어려운 것은 판단"*([[tech-bridge-ai-engineer-three-tier-skill-stack]])이 이번엔 *"architectural and critical thinking phases"*(09:42~09:48)와 *"being a conductor"*(03:28~03:31)로 반복된다. "기초를 알아야 한다"는 강조도 같다(첫 소스는 Python·Git, 이번엔 컨텍스트 창·GPU 메모리·KV 캐시).
- **[[orchestras-not-factories]]** — [[charlie-holtz|Holtz]]의 지휘자 은유를 **벤더가 아닌 해설자**가 같은 단어로 쓴다(*"a conductor, a captain"*). Clyburn은 공장 은유를 거부하는 논쟁은 하지 않는다. 지휘자의 일은 **아키텍처 결정과 목표 → 마일스톤 분해**(03:31~03:54)다.
- **[[spec-driven-development]]** — 동기를 **모델 간 해석 차이**(*"interpreted differently by different types of coding models"* 01:53~01:59)에서 찾는다. 이 페이지의 기존 소스들이 다루는 도구·단계는 없다.
- **[[context-engineering]]** — *"resource limitations of an AI model's context window"*(04:05~04:11) — 컨텍스트를 **유한 자원**으로 보는 정의다. tools·skills·MCP를 "코드베이스에 더해지는 구성 요소"로 둔다.
- **[[lethal-trifecta]] · [[prompt-injection]]** — 세 조건(*sensitive data · exposure to the web · ability to send data*)이 Willison의 틀과 같은 구조다. 이름 없이 같은 판정이 한 번 더 나왔다. 사례는 **PR을 읽고 데스크톱 자격증명을 보내는** 코딩 에이전트다. [[tech-bridge-death-of-code-review]]의 *리뷰 대상이 리뷰어를 설득한다* 벡터와 같은 입구(PR)다.
- **[[credential-injection-outside-sandbox]] · [[brain-hands-decoupling]]** — 샌드박스를 **보안 이유**(공격 표면 축소, 침해 시 피해 범위)로 쓴다. [[tech-bridge-claude-platform-agent-era]]의 *"내구성 서버 + 일회성 샌드박스"* 는 **수명 주기 이유**였다. 같은 구성을 서로 다른 근거로 설명한다.
- **[[scheduled-agent-automations]]** — cron + 이벤트 트리거(웹 폼 제출)로 기존 정의와 같다.
- **[[subagent-vs-thread-handoff]]** — 서브에이전트를 "라이브러리 동작을 확인하고 돌아오는 조사 위임"으로 설명한다. 가시성 문제는 다루지 않는다.

### 갈리는 것

> ⚠️ **긴장(약): "loop engineering"이 가리키는 대상.** [[loop-is-the-product]]·[[inner-outer-meta-loops]]에서 이 말은 [[dru-knox|Knox]]가 전한 **harness engineering의 새 이름**이다(*"It's also started to be called loop engineering"*). 거기서 개선의 레버는 실수를 하네스로 되먹이는 **meta loop**다. Clyburn의 정의는 **단일 작업의 반복 루프**다(*"a recursive goal where you as a human define the purpose and the AI iterates until it's complete"* 04:40~04:49). 이 정의는 [[ralph-wiggum-method]]나 `/goal` 류에 가깝다. 같은 용어가 두 층을 가리킨다.

> ⚠️ **긴장(약): 스킬은 "매 요청마다" 붙는가.** Clyburn은 skills를 *"markdown files that add reusable and contextual information about your code and project with each AI request"*(06:21~06:30)라고 설명한다. [[agent-skills]]는 **progressive disclosure**(맞는 스킬을 필요할 때만 넣는다)를 비용 축으로 둔다. 입문 해설의 단순화일 수 있지만, 문장 그대로라면 **매 요청 주입**이다. 그러면 화자가 바로 앞(§5)에서 말한 컨텍스트 창 자원 한계와 부딪힌다.

> **"AI가 개발자를 대체하나" — 낙관의 근거.** Clyburn의 근거는 **관찰 하나**(*"I've actually seen more people get into coding because of AI"* 00:33~00:35)와 **전기 비유**(유지·접근성 노동)다. 측정은 없다. [[intelligence-abundance]]의 Altman이 전기를 **가격·형평**의 비유로 썼다면, Clyburn은 **직업의 재배치** 비유로 쓴다.

## 해소하지 않고 표시만 한 것

- "다섯 가지 개념"의 목록. *"the last one is the most important"*(00:49~00:50)가 *"Finally, the future"*(08:22)를 가리키는지.
- 화자 소속 — 이번 설명란 "IBM Technology"와 09-15 설명란 "Red Hat 수석 개발자 애드보킷"의 차이.
- Andrew Ng 인용의 원 출처, 화자가 Ng와 한 일.
- 조종사의 신원·사용 도구·에이전트 구성. *"teams are running coding agents inside of disposable sandboxes"* 의 "teams".
- 화면 그림(GPU 메모리·KV 캐시, PR을 읽는 에이전트, 열쇠, 샌드박스).
- RPG 예시의 모델·도구, 5분 결과물의 수준.

## 등장 개체

- 인물: [[cedric-clyburn|Cedric Clyburn]](⚠️ 설명란에만 — 기존 페이지 보강) · [[andrew-ng|Andrew Ng]](화자의 기억으로 옮긴 인용) · 조종사(무명, 일화) — 페이지 없음
- 조직: [[ibm|IBM]](IBM Technology — 설명란 링크 기준) · Red Hat(⚠️ 이번 소스에 없음, 09-15 설명란 표기) — 페이지 없음
- 제품·도구: Java · Python · Rust · MCP servers([[model-context-protocol]]) — 언어는 페이지 없음
- 개념: [[spec-driven-development]] · [[orchestras-not-factories]] · [[architecture-as-remaining-art]] · [[goal-level-delegation]] · [[verifiable-goals]] · [[context-engineering]] · [[context-rot]] · [[loop-is-the-product]] · [[inner-outer-meta-loops]] · [[ralph-wiggum-method]] · [[agent-skills]] · [[scheduled-agent-automations]] · [[subagent-vs-thread-handoff]] · [[prompt-injection]] · [[lethal-trifecta]] · [[credential-injection-outside-sandbox]] · [[brain-hands-decoupling]] · [[intelligence-as-infrastructure]] · [[intelligence-abundance]] · [[three-tier-ai-skill-stack]] · [[read-fluency-for-agent-output]] · [[taste-vs-judgment]] · [[agent-attention-management]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=T8UcAUunSMw> (9:53, `upload_date` 2026-10-16)
- raw: `01.raw/articles/2026-10-16_AI 에이전트로 코딩할 때 알아야 할 5가지 개념.md`
- 설명란 링크: <https://ibm.biz/~qNwedZihN> · <https://ibm.biz/~UiJBNbzQ8> · <https://www.youtube.com/@IBMTechnology> (⚠️ 열어 보지 않았다)
- 같은 화자: [[tech-bridge-ai-engineer-three-tier-skill-stack]]
- 지휘자 은유: [[tech-bridge-conductor-orchestras-not-factories]] · loop engineering의 다른 정의: [[tech-bridge-tessl-harness-engineering-factory]] · 샌드박스의 수명 주기 근거: [[tech-bridge-claude-platform-agent-era]] · PR 경유 인젝션: [[tech-bridge-death-of-code-review]]
- [[tech-bridge]] · [[ibm]] · [[cedric-clyburn]]
