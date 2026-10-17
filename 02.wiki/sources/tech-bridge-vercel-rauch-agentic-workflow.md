---
title: "Tech Bridge — Vercel CEO는 AI를 이렇게 씁니다 (Guillermo Rauch × David Ondrej 인터뷰 발췌): fx · agentic inquiry · 샌드박스와 로컬"
type: source
tags: [vercel, fx, v0, eve, coding-cli, agents-md, agentic-inquiry, harness, brain-hands, sandbox, supply-chain-security, vibe-coding, cloud-agents, local-dev, commentary-format, interview-excerpt, vendor-claim, video]
source-url: https://www.youtube.com/watch?v=21do1LvDNFI
source-type: video
author: 'Tech Bridge (원본 인터뷰 발췌 + 짧은 해설, [한영자막] 접두사 없음) · 출연 Guillermo Rauch([[vercel|Vercel]] CEO — 이름·직함은 제목·설명란에만, 자막에 자기소개 없음) · 진행 David Ondrej(⚠️ 추정 — 설명란 "원본 채널: David Ondrej"만, 자막에 이름 없음) · 원본 인터뷰 WeiB_gLOdQE(이 위키에 없음) · 녹화일 미발화'
date-published: 2026-10-12
ingested: 2026-10-13
created: 2026-10-13
updated: 2026-10-13
---

# Tech Bridge — Vercel CEO는 AI를 이렇게 씁니다 (Guillermo Rauch × David Ondrej 인터뷰 발췌)

[[tech-bridge|Tech Bridge]]가 올린 **15:38, 공식 챕터 8개** 영상. **`[한영자막]` 재배포가 아니라 "원본 인터뷰 발췌 + 짧은 해설" 형식**이다 — 설명란: *"원본 인터뷰의 주요 구간을 한국어 번역 자막과 짧은 해설로 구성했습니다. 원본 발언과 화면이 전체 영상의 약 90%를 차지합니다."* 원본은 David Ondrej 채널의 *"Vercel CEO reveals his Agentic Engineering Workflow"*(`WeiB_gLOdQE`, 열어 보지 않았다). 화자는 [[vercel|Vercel]] CEO [[guillermo-rauch|Guillermo Rauch]] — **이름은 제목·설명란에만** 있고 자막엔 자기소개가 없다. 소속은 1인칭으로 확인된다 — *"the architecture that we recommend at Vercel"*(05:44~05:49), *"when we created V0"*(04:15~04:17). **Rauch는 이 위키에 처음 등장하고, Vercel의 두 번째 소스다**(첫째는 [[tech-bridge-vercel-eve-filesystem-agent]] — [[andrew-qu|Andrew Qu]]의 발표. **같은 강연의 중복이 아니다** — 화자·형식·주제가 다르고, 겹치는 것은 [[eve-framework|Eve]]·샌드박스라는 제품뿐). 테제:

> **CEO 본인의 일상은 터미널 안의 에이전트다. 셸처럼 뜨는 코딩 CLI(fx)와 AGENTS.md 관례를 둔 리서치 폴더가 검색을 대체하고, 에이전트에게 자사 신제품을 깨 보게 한다. v0 때 엔지니어링의 대부분을 먹었던 하네스는 이제 기성품으로 집어 와 앱에 박는다. 모든 줄을 읽을 필요는 없지만 에이전트가 끝낸 일은 이해해야 하고(agentic inquiry), 보안처럼 중요한 영역에서는 vibe coding의 반대를 하고 그걸 알려야 한다. 에이전트의 클라우드 이전은 이미 일어났고 보안상 더 낫지만, 로컬로 끌어내려 현미경으로 볼 선택지는 남겨야 한다.**

> *"I'm not advocating that you read every line of code, but when you do get something done, try to understand what just happened."* (07:05~07:12) · *"If I were to create something like V0 today (…) I would want to pick a harness off the shelf."* (04:20~04:37) · *"there's areas of your product where you want to do the opposite of like, you know, no questions asked. You actually want to be extremely diligent and communicate that to the world."* (10:58~11:05) · *"from a security perspective, cloud is infinitely better."* (13:37~13:41) · *"I do think that you still want to be able to pull things down into into a computer."* (14:24~14:28)

이 위키에 개념 하나가 생긴다 → [[agentic-inquiry]] (신규 제안). 그리고 제품 둘 → [[fx]] · [[v0]] (신규 제안).

**트랙과 인용.** 세 트랙 모두 자동 자막. **ko는 영어 발화의 번역뿐이고 한국어 해설은 어느 트랙에도 없다.** en-orig의 6초 이상 공백 일곱 곳(01:03~01:16 · 03:54~04:08 · 04:44~04:53 · 06:49~07:01 · 09:42~09:53 · 11:05~11:19, 그리고 00:00~00:15)이 **챕터 시작 시각과 겹친다** → 해설 구간 추정, 내용은 채우지 않는다. 인용은 en-orig에서만. ko 보정: fx → **"효과"**(전 구간), harness → **"테스트 환경"**(05:47), sandbox → **"실험장"**(05:54), Eve → **사람 "이브"**(06:14), *agents are really good at attacking problems in parallel* → **"그들은 공격에 정말 능숙해요. 문제가 동시에 발생합니다"**(13:43, 반전), *they can do work while you're asleep* → **질문**(13:59), *you still want to be able to pull things down* → **질문**(14:26), *as per sale[=Vercel]* → **"상업용"**(10:37), Install 11MB → **"설치 횟수 11회"**(00:44, 단위 변경), agentic inquiry → "요원 조사"(03:39)·"능동적 탐구"(07:05)로 **두 번 다르게**. 전체 목록은 raw.

> ⚠️ **당사자 진술 — CEO의 자사 제품 시연.** fx · fx0 · Vercel Sandbox · v0 · Eve 전부 Vercel 것이다. 설명란 스스로 *"개발 속도, 코드 규모, 보안 우위 등에 관한 발언은 인터뷰 참여자의 설명과 견해입니다"* 라고 단서를 단다. 수치는 전부 회고·추정 — *"like 90% of the engineering time"*(05:04~05:07), *"probably like I don't know, 100 lines of code"*(05:15~05:21), *"a couple of years of engineering"*(06:20~06:25). 측정·사례 없음.
>
> ⚠️ **발췌·해설 형식.** *"이 영상은 전체 인터뷰 중 선택한 구간을 다룹니다"*(설명란). 구간 사이 맥락과 해설 내용은 이 위키가 보지 못했다. 원본 인터뷰 길이·녹화일 미상 — 상대 단서는 *"we created this um example that we're going to open source. I think you're going to be one of the first people to see it."*(04:38~04:44)뿐.
>
> ⚠️ **진행자 = David Ondrej는 추정.** 진행자 발화(`>>`)는 있으나 이름은 어디에도 발화되지 않는다. 설명란 *"원본 채널: David Ondrej"* → 채널 운영자 = 진행자로 추정. 진행자의 실질 발화는 두 번 — 코드 읽기 이분법(07:14~07:33), 클라우드 에이전트 질문(11:19~11:51).
>
> ⚠️ **미판독 이름.** *"drives"*(03:25, Vercel 신규 인프라로 보임) · *"Deep Sage"*(11:57, 샌드박스로 대형 코드베이스를 다루는 무언가 — ko·`en` "심해/Deep Sea") · *"live effects"*(04:13, 임베드용 fx로 보임) · *"Tim Casina"*(03:54, 해설 시작 시각의 단발 — 인명으로 쓰지 않음) · *"this cloud thing"*(01:28, cloud인지 Claude인지 불명) · *"Dylan Monroe"*(07:51). 마지막 *"It's toggle switch."*(15:24~, json3에 6회 반복)는 첫 번째만 진행자 맞장구일 가능성, 나머지는 ASR 반복.

## 1. fx — 셸처럼 뜨는 코딩 CLI (00:15~01:03)

- *"Today I'm using effects[=fx], which is the coding CLI of Versel[=Vercel] Labs."*(00:15~00:19) — 설명란 `https://fx.sh/` 로 판독.
- 설계 원칙: *"it almost feels like a shell. So, when I open a new tab (…) or I open a split, like it boots into ZSH. But one of the things that we obsessed about is like can this boot as fast as a shell itself?"*(00:23~00:40)
- 크기: *"Install is 11 megabytes if you download it today (…) It's actually 6 megabytes. It's 11 megabytes on disk."*(00:46~00:53) — 발화 중 정정, 다운로드 6MB · 디스크 11MB로 읽는다. ⚠️ ko는 "설치 횟수 11회".

→ [[fx]] (신규 제안)

## 2. 리서치 폴더 · 한 글자 alias · agentic inquiry ① (01:16~03:52)

- ⭐ **검색 대체**: *"anytime I have a question about virtually anything (…) it's replaced Google for me incidentally because instead of having to go to like this cloud thing, I can keep a lot of my sort of experimentation in in the file system. I can have the agent look at it."*(01:18~01:36) ⚠️ *"this cloud thing"* — cloud 서비스인지 Claude인지 미판독.
- ⭐ **AGENTS.md가 관례를 만든다**: *"the future of of software is becomes a lot more like English driven. The fact that my agents.md file in this research folder sort of like creates the convention for if I ask the agent a question, reads up the instructions, and then dumps my research into this folder. um and I can sort of basically improve it over time."*(01:40~01:59) → [[file-system-agent]] · [[feedforward-feedback-steering]]
- **alias `r`**(리서치 폴더로 cd + fx 실행): *"there's basically nothing to do, right? Cuz like it's CDing into a folder and opening effects, but it still cuts down on all the latency. Like it gets addicting because anytime I have a question that I want to go deep into, like it just fire it off and then move on with my life."*(02:20~02:36)
- **alias `p`**(새 프로젝트): *"this is similar to what Toby does with try (…) Toby from Shopify"*(02:41~02:45, ⚠️ Tobi Lütke와 그의 `try` CLI로 판독 — 성 미발화) — 로컬 Mac 앱, Next.js 앱, Zig·Rust 프로그램, *"a lot of benchmarking to help our teams"*(03:13).
- ⭐ **agentic inquiry ① — 에이전트에게 자사 제품을 깨 보게 하기**: *"anytime we create a new piece of infrastructure, I try to validate it from first principles and like how an agent would approach it. A good example is when we announced drives, I had an agent go and try to like break it. Uh you know, try to find race conditions, try to measure latency, try to compare it with alternatives. Um I do a lot of what I call agentic inquiry, which is like I'll have an agent go and try out one of our technologies, and then I'll have it reflect on "Tell me what Vercel could have done better.""*(03:16~03:47)

→ [[agentic-inquiry]] · [[agent-native-interface]](에이전트가 제품의 첫 사용자) · [[obsidian-cli-workflow]](같은 terminal-first 습관)

## 3. 하네스를 기성품으로 — fx 임베드와 fx0 (04:08~06:49)

- *"One of the ideas of effects is that you should be able to embed it"*(04:08~04:13). 영감은 v0: *"when we created V0, we needed to build a harness from scratch. If I were to create something like V0 today, or any kind of application like imagine like Gamma (…) Notion, or anything that requires sort of agentic intelligence to be embedded, I would want to pick a harness off the shelf."*(04:15~04:37)
- ⭐ **v0의 비용**: *"back when we built V0 for the first time, I think the amount of time that we spent just on the harness was disproportion, like 90% of the engineering time went into, you know, like figuring out AISDK and the models and the prompts and the tool calls and all of this. Whereas, this example is probably like I don't know, 100 lines of code on top of the create effects agent API."*(04:54~05:23) ⚠️ 두 수치 모두 회고·추정.
- ⭐ **brain and hands**: *"using this mental model like brain and hands (…) the architecture that we recommend at Vercel is that you run the harness and then you give it tools. So, in this example, the tool that we're giving it is the Vercel sandbox."*(05:36~05:56) — [[anthropic-managed-agents]]의 용어를 **Vercel이 권장 아키텍처로** 쓴다.
- **fx0의 세 모드**: ① 모델이 HTML을 출력(05:24~05:31) ② Vercel Sandbox에서 *"a full Next.js application"*(05:57~06:08, 프롬프트 *"Build a landing page for a CLI coding agent."*) ③ *"agent, and it creates an Eve agent when you give it a prompt"*(06:10~06:18) → [[eve-framework]].
- *"what perhaps took us like a a couple of years of engineering with V0, like it's now part of the infrastructure that you can use off the shelf."*(06:20~06:29) 고객 요청: *"add like app generation capabilities within my system of record"*, 사내용 v0 — *"your own quote-unquote software factory where one of the capabilities is design."*(06:31~06:49)

→ [[brain-hands-decoupling]] · [[harness-as-platform]] · [[agent-architecture-progression]] · [[software-factory]] · [[v0]] · [[fx]]

## 4. agentic inquiry ② — 모든 줄이 아니라 "방금 무슨 일이" (07:01~09:42)

- ⭐ *"the phrase that I've coined, I think I've coined this is agentic inquiry, which is I'm not advocating that you read every line of code, but when you do get something done, try to understand what just happened."*(07:01~07:12)
- 진행자(추정 David Ondrej): *"people see such a binary, like either you're reading the code and it's like line by line (…) Or you're just like fully yellowing[=YOLO-ing] and never looking at it. (…) if you if you know how to use the agent to understand this file or this module, like that's enough."*(07:14~07:32)
- 사례 — 호출 스택 다이어그램 스킬(X의 *"Dylan Monroe"*, ⚠️ 철자 미확인): *"the agent was sort of doing like pseudo static analysis and I think this is a skill or maybe a skill plus an AST grab[=ast-grep] style tool (…) it gives you a sense of like the symbolic space of your program. Oh, this method calls this method calls this method"*(07:58~08:17). *"this is like agents at their finest because to do that only with syntactic tools and and AST parsing, you would have to every time create a new program to visualize what you just did or have a very rigid tool."*(08:17~08:31)
- 이해의 대상: *"measuring latency (…) measuring allocations (…) understanding the new API shape"*(08:41~08:51).
- ⭐ **이해를 자동화로**: *"I've seen folks set it up such that they call the Slack MCP (…) anytime you do something that alters (…) the public facing API shape of this program let me know. Ping me on Slack or Discord. That and that alone is just I think better quote unquote agentic engineering than just do it, make no mistakes. Please auto merge and let's keep building a huge pile of slop."*(09:01~09:35)
- 진행자 요약: *"knowing what matters for that system"*(09:35~09:37).

→ [[agentic-inquiry]] · [[cognitive-debt]] · [[code-knowledge-graph]] · [[read-fluency-for-agent-output]] · [[ai-slop]] · [[model-context-protocol]]

## 5. vibe coding의 반대를 하고, 그걸 알려라 (09:53~11:05)

- *"something that will backfire for a lot of people that are embracing, you know, extreme vibe coding is that if I'm an enterprise, I need you to build very strong conviction in the security profile of your product."*(09:53~10:10)
- ⭐ *"I actually think security and in some ways almost like communicating that you're doing the opposite of vibe coding can really play in your favor."*(10:12~10:23)
- 본인의 도입 고민: fx에게 *"Find me a bunch of projects that have already done this"*(10:29~10:33) 시킨 뒤 — *"One of my biggest challenges today in adopting new software, both personally and as per sale[=Vercel], is understanding the security that that I'm taking on. Because, you know, supply chain attacks, because vibe coding, because (…) the surface of attack has become so massive as of recently."*(10:35~10:56)
- *"there's areas of your code base, there's areas of your product where you want to do the opposite of like, you know, no questions asked. You actually want to be extremely diligent and communicate that to the world."*(10:56~11:05)

→ [[slop-free-zone]] · [[generated-dependency-scrutiny]] · [[shift-left-security]] · [[risk-proportional-human-review]]

## 6. 클라우드 에이전트는 이미 와 있다 (11:19~14:20)

- 진행자 질문: 온프렘 → 클라우드처럼 에이전트도 노트북에서 클라우드로 가는 게 필연인가 — 창이 튀어나오고, 과열·배터리, *"agent decided to run 1,000 tests"*(11:19~11:51; *"cloud code[=Claude Code] in your terminal or effects on a computer"* 11:49 ⚠️ 판독).
- *"It's inevitable, it's already here, right? Even Deep Sage as an example, like it in order to scale itself in very large code bases, it's not tenable to run it on your own computer. So it uses sandboxes."*(11:54~12:06) ⚠️ *"Deep Sage"* 정체 미확인.
- 근거 ① 규모: 브랜치·순열 처리로 *"you run out of memory, you run out of CPU"*(12:11~12:20).
- 근거 ② **보안**: *"if I'm running something on my own computer, my computer gets popped (…) what does the attacker get access to?"* → 진행자 *"Password manager, everything."*(12:24~12:34). *"it's much easier to compartmentalize and contain the blast radius of a supply chain attack."*(12:34~12:41)
- ⭐ **강한 주장**: *"that's it's a bold statement, but like, we could eradicate supply chain attacks uh if if we move more and more of this development life cycle to to sandboxes. Why? Because we can have more careful firewall and security policy monitoring the network."*(12:46~13:05) — 고전적 malware·RAT는 *"exfiltrates it to some kind of host name or S3 bucket"*(13:12~13:21)이므로 네트워크 단언·스캔·피해 격리가 가능하다 → *"from a security perspective, cloud is infinitely better."*(13:37~13:41)
- 근거 ③ 병렬: *"agents are really good at attacking problems in parallel (…) you can scatter them across multiple sandboxes, they can share state"*(13:41~13:56). 근거 ④ *"they can do work while you're asleep"*(14:00~14:02) — self-healing software, 예외·공격이 왔을 때 *"turn your computer back on"* 할 수는 없다(14:03~14:20).

→ [[cloud-agent-delegation]] · [[brain-hands-decoupling]] · [[credential-injection-outside-sandbox]] · [[scheduled-agent-automations]]

## 7. 그래도 로컬은 남겨라 — 그래서 CLI (14:22~15:24)

- *"maybe I'm contrarian on this, is that I do think that you still want to be able to pull things down into into a computer. (…) people again try to go into one extreme or the other."*(14:22~14:35)
- *"sometimes you need to like look at things under the microscope. This is also incidentally also why I like CLIs because I need to be as close to the metal as possible. I need to look at the file system, I need to run a process monitor. Um I want to see it interact with other applications that I've installed. I want to I want to see it on a Mac."*(14:44~15:04)
- *"yes, like you can do all these things in the cloud in theory, but (…) pull it into local, lowest latency (…) that option should stay open."*(15:06~15:20)

→ [[cloud-agent-delegation]](로컬 쪽 단서) · [[fx]]

## 이 위키와의 연결

### 이어지는 것

- **[[tech-bridge-vercel-eve-filesystem-agent]] — 같은 회사, 다른 층.** Andrew Qu는 *사내 에이전트를 세 번 버리고 파일 시스템에 닿은* 연대기와 Eve를, Rauch는 *CEO 개인의 터미널 습관*과 fx를 말한다. 연결점 둘: ① fx0의 세 번째 모드가 **Eve 에이전트를 생성**한다(06:10~06:18) ② 리서치 폴더 + agents.md(01:44~01:59)는 [[file-system-agent]]의 개인판 — *지식을 파일로 펼치고 에이전트가 읽게 한다.* Andrew Qu가 Claude Code를 *"거의 AGI"* 라고 했던 것처럼, Rauch의 v0 회고(*"90% of the engineering time"* 이 하네스)도 **직접 만든 하네스의 비용**을 인정하는 쪽이다 → [[agent-architecture-progression]].
- **[[brain-hands-decoupling]]** — Anthropic 글([[anthropic-managed-agents]])의 *brain/hands* 를 **Vercel CEO가 자사 권장 아키텍처로** 부른다(*"I don't know if you if you've heard of it"* 05:40~05:42 — 출처를 밝히지는 않는다). 손 = Vercel Sandbox.
- **[[slop-free-zone]]** — [[charlie-holtz|Charlie Holtz]]([[conductor|Conductor]])의 *"strict human review"* 구역과 Rauch의 *"areas of your code base (…) extremely diligent"*(10:56~11:05)는 같은 비대칭. Rauch는 한 칸을 더한다 — **그 성실함을 고객에게 알리는 것이 경쟁력**(10:12~10:23).
- **[[cognitive-debt]]** — agentic inquiry ②는 *"모든 줄을 읽기"* 와 *"YOLO"* 사이의 처방이다. 인지 부채를 **읽기가 아니라 에이전트에게 설명을 시켜서** 갚는다. 호출 스택 다이어그램 사례는 [[code-knowledge-graph]]·[[understand-anything]]과 같은 방향(코드를 *보면서* 이해).
- **[[cloud-agent-delegation]]** — *"It's inevitable, it's already here"*(11:54). 동시에 [[tech-bridge-lauren-tan-trusting-agents|Lauren Tan]]의 *"시작하기 가장 좋은 곳은 로컬 — 에이전트가 무엇을 하는지 관찰할 수 있으니까"* 와 Rauch의 *"look at things under the microscope"*(14:44~14:50)는 **로컬 = 관찰의 자리**라는 같은 근거를 댄다.

### 갈리는 것

> ⚠️ **Contradiction (약): 샌드박스로 공급망 공격을 근절할 수 있나.** Rauch: *"we could eradicate supply chain attacks uh if if we move more and more of this development life cycle to to sandboxes"*(12:48~12:56) — 근거는 네트워크 방화벽·정책 감시(12:58~13:05). [[tech-bridge-openai-huggingface-incident-black-hat]]: 샌드박스 안의 에이전트가 **샌드박스가 신뢰한 유일한 외부 의존성**([[artifactory|Artifactory]])을 통로로 클러스터 권한까지 갔다. 다만 위협 모델이 다르다 — Rauch는 *개발자 머신에 들어온 malware의 유출*(13:05~13:21)을, Black Hat 편은 *샌드박스 안의 에이전트 자신*을 겨눈다([[agentic-misbehavior]]). Rauch 스스로 *"it's a bold statement"*(12:46~12:48)라 단서를 단다.

> ⚠️ **Contradiction (약): 하네스는 사서 쓰나, 깎나.** Rauch: *"I would want to pick a harness off the shelf"*(04:35~04:37). [[harness-engineering]]은 하네스(wrapper 전체)를 **설계·구현하는 기술**로 다룬다. 반면 [[tools-and-context-over-harness]]([[ryan-lopopolo|Ryan Lopopolo]])는 Rauch와 같은 쪽이다 — *하네스는 고정값, 노력은 도구·컨텍스트에.* 정면 충돌은 아니다 — Rauch는 *앱에 에이전트를 박는 제품 팀*(v0·Gamma·Notion 같은 경우)을, 하네스 엔지니어링 쪽은 *코딩 에이전트를 운영하는 팀의 환경*을 말한다. 그리고 그 "기성품"이 Rauch 회사의 것이다(⚠️ 당사자).

> ⚠️ **"agentic inquiry"의 두 뜻.** 같은 화자가 같은 말을 ① *에이전트에게 자사 기술을 시험·비평시키기*(03:35~03:47) ② *에이전트가 끝낸 일을 사람이 이해하기*(07:01~07:12)로 쓴다. ②에 *"I think I've coined this"* 가 붙는다. [[agentic-inquiry]] 페이지는 둘을 나눠 적는다.

## 해소하지 않고 표시만 한 것

- 진행자 이름(David Ondrej 추정), 인터뷰 녹화일·원본 길이, 해설 구간 8곳의 내용.
- *"drives"*, *"Deep Sage"*, *"live effects"*, *"create effects agent API"* 의 정체 · *"this cloud thing"*(cloud/Claude) · *"Dylan Monroe"* 철자 · *"Tim Casina"*.
- fx0 예제의 오픈소스 공개 여부(*"we're going to open source"* 04:41 — 의사 표명).
- 설명란 링크 `fx.sh` · `fx.sh/docs` · 원본 인터뷰 — 열어 보지 않았다.

## 등장 개체

- 인물: [[guillermo-rauch|Guillermo Rauch]](신규 제안 — 이름은 제목·설명란에만) · [[david-ondrej|David Ondrej]](신규 제안 — ⚠️ 진행자 추정) · Tobi(Shopify, `try` CLI — 성 미발화, 페이지 없음) · Dylan Monroe(⚠️ 철자 미확인, 페이지 없음)
- 조직: [[vercel|Vercel]] · Vercel Labs(fx 제작 — 페이지 없음) · Shopify(언급만)
- 제품·도구: [[fx]] (신규 제안) · fx0(데모) · [[v0]] (신규 제안) · [[eve-framework|Eve]] · Vercel Sandbox · AI SDK · [[nextjs|Next.js]] · [[claude-code|Claude Code]](⚠️ ASR *"cloud code"* 판독, 진행자 발화) · Gamma · Notion · ZSH · Slack · Discord · ast-grep(판독) · drives · Deep Sage(⚠️ 미판독)
- 개념: [[agentic-inquiry]] (신규 제안) · [[brain-hands-decoupling]] · [[harness-as-platform]] · [[agent-architecture-progression]] · [[file-system-agent]] · [[cognitive-debt]] · [[code-knowledge-graph]] · [[slop-free-zone]] · [[ai-slop]] · [[generated-dependency-scrutiny]] · [[cloud-agent-delegation]] · [[software-factory]] · [[model-context-protocol]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=21do1LvDNFI> (15:38, `upload_date` 2026-10-12)
- raw: `01.raw/articles/2026-10-12_Vercel CEO는 AI를 이렇게 씁니다 - 실제 개발 워크플로 공개.md`
- 원본 인터뷰(설명란): <https://www.youtube.com/watch?v=WeiB_gLOdQE> · 설명란 링크: <https://fx.sh/> · <https://fx.sh/docs> (⚠️ 열어 보지 않았다)
- 같은 회사: [[tech-bridge-vercel-eve-filesystem-agent]] · [[vercel]]
- 같은 형식(해설 + 발췌): [[tech-bridge-lauren-tan-agent-dev-workflow]]
- 샌드박스 보안 반례: [[tech-bridge-openai-huggingface-incident-black-hat]]
- [[tech-bridge]] · [[guillermo-rauch]] · [[fx]] · [[agentic-inquiry]]
