---
title: "Tech Bridge — 코드 슬롭과의 싸움: 소프트웨어 팩토리의 현실 (Dex Horthy · HumanLayer): 감독 없는 모델은 코드베이스를 좋게 만들지 못한다, 그러니 지금은 코드를 읽고 공장에 압력을 건다"
type: source
tags: [software-factory, lights-off-factory, dark-factory, unattended-agents, ai-slop, slopcodebench, maintainability, oracle, rl-incentives, benchmark-saturation, code-review, read-the-code, planning, expected-pain, show-me, visual-alignment, back-pressure, forward-pressure, loops, anti-slop-lint, typescript, feature-flags, incident-to-pr, compounding, session-analysis, software-forge, system-of-record, control-plane, agent-platform-layers, multiplayer, humanlayer, video]
source-url: https://www.youtube.com/watch?v=XejHwIKi5qg
source-type: video
author: Tech Bridge (한영자막 재배포) · 발표 Dex Horthy([[humanlayer|HumanLayer]] CEO·공동 창업자 — **직함·회사는 발화**(00:49~00:53), **이름은 "I'm Dex"(15:44)만 발화, 성 Horthy는 제목·설명란에만**) · 행사명 미발화(설명란 AGNTCon NA·Agentic AI Foundation 링크 → 추정) · 녹화일 미발화
date-published: 2026-10-14
ingested: 2026-10-15
created: 2026-10-15
updated: 2026-10-15
---

# Tech Bridge — 코드 슬롭과의 싸움: 소프트웨어 팩토리의 현실 (Dex Horthy · HumanLayer)

[[tech-bridge|Tech Bridge]]가 재배포한 **16:11 발표, Q&A 없음, 공식 챕터 14개.** 화자는 [[dex-horthy|Dex Horthy]] — *"Uh I am the CEO and co-founder of a company called HumanLayer."*(00:49~00:53), 끝에서 *"I'm Dex."*(15:44). **성 Horthy는 제목·설명란에만 있다.** 화자는 이 슬롯이 *"10 minutes and not 25"*(00:08~00:09)라 하지만 영상은 16분이다. 테제:

> **감독 없는 모델은 코드베이스 품질을 개선하지도 유지하지도 못한다 — maintainability에는 빠른 oracle이 없어서 RL이 좋은 아키텍처를 보상할 길이 없고, 벤치마크(SlopCodeBench)도 그렇게 말한다. 그러니 "lights-off factory"는 아직 환상이고, 지금은 코드를 읽어야 한다. 대신 공장에 사람이 오래 해 온 관행을 다시 깐다: 계획을 먼저(expected pain), 시각적으로 맞추고, 에이전트가 스스로 테스트하게 하고(back pressure), anti-slop 규칙을 쓰고, 사용자 피드백·인시던트를 에이전트 PR로 바꾸고, 실험시키고, 세션에서 배워 쌓는다. 그 위에 필요한 도구는 세션·계획·프롬프트의 system of record이고, HumanLayer는 그 control plane을 판다.**

> *"unattended models will not improve or maintain your code base quality over time."* (05:17~05:23) · *"maintainability has no fast oracle."* (06:13~06:15) · *"So if unattended model code gets worse over time, then for now we should probably read the code"* (09:01~09:07) · *"I think loops are basically a combination of forward pressure and back pressure."* (12:30~12:34)

이 위키에서 [[dex-horthy|Horthy]]는 지금까지 [[tech-bridge-death-of-code-review|Laurie Voss]]가 인용한 **철회**(*"I was wrong. Please please read the code."*)로만 등장했다. 이 영상은 **그 철회의 당사자가 직접 낸 근거와 처방**이다 — 다만 그는 이 발표에서 자기 철회를 언급하지 않고, Steve(Gas Town)의 입장 변화를 든다. 새 개념 셋을 제안한다 → [[back-pressure]](forward pressure + back pressure = loop) · [[expected-pain-planning]](계획 깊이를 변경 확률 × 변경 비용으로 고른다) · [[agent-platform-layers]](compute · dev environment · harness · control plane). 나머지는 기존 페이지의 증언이다 — [[software-factory]](lights-off 반론의 세 번째 화자) · [[verification-bottleneck]] · [[ai-slop]] · [[verifiable-goals]]·[[reward-hacking]](maintainability의 oracle 부재) · [[hard-vs-soft-enforcement]](anti-slop 규칙) · [[trace-to-memory-loop]]·[[skill-self-improvement]](세션에서 compound) · [[multiplayer-agent-context]](HumanLayer 워크스페이스).

ASR·ko 보정: ko는 **PR을 "홍보"·"보도자료"로**(02:05 *incidents per PR is way up* → **"홍보 효과가 상당히 증가"**, 11:53·11:59·12:05), **HumanLayer를 "인권 문제"로**(14:55) 옮긴다. 테제 *"unattended models will not improve"* → **"모델이 없는 경우 감독은 개선되지 않을 것"**(05:16), *without really rewarding good architecture* → **"훌륭한 건축물에 상을 수여합니다"**(06:02), *"the data says otherwise"* → **"데이터가 그렇게 말하고 있다"**(02:16), *"don't even prompt anymore"* → **"프롬프트를 생성해야 합니다"**(01:47), Steve의 *"You're not going to make it"* → **"넌 해낼 거야"**(08:31), loop의 *without having to go to a human* → **"인간에게 의지해야 하는 상황"**(12:46), 스펙 *5 hours* → **"5일"**(10:08). `en`·ko 공유: *lights-off* → *"dark"*(04:50), *terminal bench* → *"final exam"*/"기말고사"(07:00), *anti-slop* → *"anti-disorder"*/"질서 유지"(11:32), *agents* → *"officers"*/"요원"(11:18), *compound* → *"compose"*/"작곡"(12:54). 전체 목록은 raw.

> ⚠️ **수치 대부분이 출처 미제시다.** 5월 리포트(01:48~02:09)는 **이름·발행처·수치 없이 방향만**(*"code review uh uh quality is way down (…) incidents per PR is way up. Bugs per developers way up."*). SlopCodeBench의 GPT-5.5 *"14.8%"*(06:57)는 화자의 인용이고, Astra의 *"one percentage point or 1.5% percentage points higher than GPT-5.5"*(08:46~08:51)는 화자도 1과 1.5 사이에서 확정하지 않는다. expected pain 곡선(50% · 10% · 0%)은 직관 수치, show me *"probably up to like 20K installs"*(11:14~11:16)는 추정이다.
>
> ⚠️ **화자 신원.** HumanLayer CEO·공동 창업자는 발화, 이름은 *"Dex"* 까지. 성 Horthy는 제목·설명란에서만 — **자막과 충돌하지 않는다.** [[tech-bridge-death-of-code-review]]의 en-orig *"Dexter Horthy"* 와 같은 인물로 읽는다.
>
> ⚠️ **2차 진술.** Anthropic 포스트모템(*"we had a security issue, uh, cuz we had a bunch of like messy code that accumulated over time"* 07:19~07:26)은 **화자의 요약**이다 — 포스트모템의 제목·날짜·원문 미발화. Steve의 *"last week"* 발언(08:36~08:43)도 화면을 읽은 것으로 보인다. Steve의 성(Yegge)은 챕터·설명란에만.
>
> ⚠️ **당사자 진술의 범위.** 14:53~15:44는 자사 제품 설명이다 — HumanLayer의 control plane·워크스페이스·custom harness(*"We're going to open source it in the next couple weeks"* 14:59~15:02). 고객·사용 수치는 없다. show me 스킬도 자사 것(*"this is built into human layer but you can go get the open source as well"* 10:55~11:00).
>
> ⚠️ **행사·시점.** 행사명 미발화. 설명란 *"AGNTCon NA 컨퍼런스"*·*"Agentic AI Foundation"* 링크 → **AGNTCon NA 추정**(확정 아님). 시점 단서는 모두 연도 없이: *"Loops thing last summer"*(01:43~01:46), *"a report that came out in May"*(01:48~01:50), *"this talk from June"*(05:48~05:51), *"Folks, we're at GPT-6"*(07:48), Steve의 *"last week"*(08:33~08:36).

## 1. 왜 이 회사가 이 말을 하나 — HumanLayer의 자리 (00:00~01:43)

- 청중 손들기: AI로 코드 100% 작성(00:14~00:20), 그 코드를 *"trying pretty hard to read"*(00:23~00:30).
- *"We build a multi multi-agent coding sorry. We build a multiplayer coding agent workspace."*(00:53~00:59) — 자기 정정이 그대로 남는다. 목표 *"building blocks for software factory builders"*(01:05~01:09).
- ⭐ 초점: *"hard problems in complex code bases. You have hundreds of engineers, you have hundreds of repos"*(01:10~01:16). 반면 *"you can build a ticket to PR or Slack message to PR pipeline for the small stuff. Our our focus is really like how do we as engineers and teams collaborate meaningfully on the big stuff?"*(01:25~01:37)
- 자기 이력: *"we have a list of everything we've ever written or said about coding agents and agentic AI and 12-factor agents and context engineering"*(00:43~00:49) → [[context-engineering]]. ⚠️ 12-factor agents의 내용은 이 발표에서 설명하지 않는다(설명란에 GitHub 링크만).

→ [[multiplayer-agent-context]] · [[plan-to-ticket-pipeline]]

## 2. 소음과 데이터 — Loops 열풍, 5월 리포트 (01:43~02:19)

- *"There was this whole Loops thing last summer of like just build Loops, don't even prompt anymore."*(01:43~01:48)
- *"at the same time there was a report that came out in May that, you know, since uh January when we all picked up Opus 4.5 and decided this stuff was good enough. Uh code review uh uh quality is way down. A lot of PRs just skipping review, longer comments, more comments. Uh incidents per PR is way up. Bugs per developers way up."*(01:48~02:09) ⚠️ 리포트 미특정, 수치 없음. [[claude-opus-4-5|Opus 4.5]]를 **"good enough" 전환점**으로 둔다.
- *"Do you think this is a skill issue?"* — *"I say the data says otherwise, that data and more data."*(02:09~02:19)

→ [[verification-bottleneck]] — [[tech-bridge-dx-ai-impact-trends|DX 편]]의 집계와 같은 방향의 **출처 미상** 진술. 같은 리포트인지 확인하지 않았다.

## 3. 공장은 1968년부터 있었다 — 2022년형과 agentic형 (02:19~04:47)

- *"cuz software factory is not an AI thing. This has been around since 1968. Uh the same the same year that we invented the word software engineering."*(02:24~02:31) ⚠️ 화자의 역사 진술, 출처 미제시.
- **2022년형 공장**(02:42~03:57): 팀(엔지니어·PM·GM/CEO) → 트래커(*"Linear or Jira or Beads"*) → 빌드 → 자동·수동 테스트(브라우저·curl) → PR → *"hundreds of CI checks and security scans"* → 사람이 pull해서 테스트·리뷰 → 문제 있으면 builder로 루프 → 프로덕션(*"rollouts and feature flags and canary systems"*) → 사용자의 feature request·불만 → 큐로 → 모니터링(*"wake up our engineers at 3:00 in the morning"*). *"most of what you see about software factories and AI is actually kind of like the same thing we've been doing as engineers for decades."*(02:33~02:42)
- **agentic형**(04:00~04:47): *"Not much changes here."* builder만 에이전트로 — *"this part now takes minutes or hours, but this part over here still takes hours or days."*(04:31~04:37) agentic 코드 리뷰·회귀 테스트로 리뷰를 당겨도 *"it may still be the bottleneck."*(04:43~04:47)
- 농담: *"Who has a little ticket to PR agent in their company that they're super proud of? (…) Everyone Everyone has one. You're falling behind."*(04:10~04:19)

→ [[software-factory]] — 이 위키의 정의들([[factory-ai|Factory]]의 자율 SDLC, [[warp|Warp]]의 *SDLC 그 자체*)과 달리 Horthy는 공장을 **AI 이전부터 있던 SDLC 그림**으로 놓고, agentic형은 *한 칸만 바뀐 것*이라 한다. → [[verification-bottleneck]]

## 4. lights-off factory와 테제 (04:47~06:23)

- *"this funny idea called the lights-off software factory, uh, where we just say, 'You know what? I don't I'm tired of reviewing code. (…) What if we just didn't review the code anymore? What if we just let it go in?'"*(04:47~05:03) — *"theoretically, if you invest into all this other stuff, you could like, probably get uh, close to a place where where this would actually work."*(05:03~05:11)
- ⭐ 테제: *"unattended models will not improve or maintain your code base quality over time."*(05:17~05:23)
- *"models got really, really good in 2026 at like solving problems and doing interesting things. I don't think they got very good at improving code base quality. You could tell them to go improve it, but then you have to know what to tell them to do and that means you have to understand the code base, which means it's not unattended."*(05:27~05:41) — **"개선하라고 시키려면 코드베이스를 이해해야 하고, 그러면 무인이 아니다."**
- ⭐ 원인(직관): *"how we do RL and how how the benchmarks are shaped that might incentivize sort of cheating. Uh, just trying to get the test to pass without really like rewarding good architecture. Um, because the cost of bad architecture is measured measured in months and years. And to do reinforcement learning, you need an oracle. You need a verifier. You need something to say, is this code maintainable or not? And maintainability has no fast oracle."*(05:53~06:15) — *"We don't find out that the code was ugly until 2 months later"*(06:15~06:19). ⚠️ 화자 스스로 *"intuition-based explanation"*(05:51~05:53, 6월 발표).

→ [[verifiable-goals]] · [[reward-hacking]] — 이 위키의 "검증 가능한 목표" 논의에 **검증 지연(months and years)** 축을 더한다: 검증기는 있어도 **빠르지 않으면 학습 신호가 못 된다.** → [[software-factory]]의 lights-off/dark factory 논쟁

## 5. 증거 — SlopCodeBench, Anthropic, Steve (06:23~09:07)

- ⭐ **SlopCodeBench**: *"published out of a lab in the University of Wisconsin, uh, in the US"*(06:27~06:30). 설계: *"instead of telling the model the whole problem to solve up front, it gives the model the challenges. It discloses like parts of the challenge in bits and makes it write the code and then do another feature and then do another feature. Which maps much more closely to how everyone in this room builds software."*(06:33~06:47)
- *"when they launched this, GPT-5.5 was the best model on the market. It got a 14.8%."*(06:53~06:59) 대비: *"when you see terminal bench scores and everyone's getting 95% of it saying coding is solved, there is a small lab (…) came up with a benchmark that is full very much unsaturated."*(06:59~07:12) ⚠️ 14.8%가 무엇의 비율(통과율? 점수?)인지 미발화. 설명란엔 arXiv(`2603.24755`)와 snorkel.ai 리더보드 링크 — **Snorkel과의 관계는 발화되지 않는다.**
- Anthropic: *"Anthropic did a postmortem. They're like, yeah, we had a security issue, uh, cuz we had a bunch of like messy code that accumulated over time. To which the benchmark creator, of course, pointed out that there was a benchmark that would prove that models create sloppy code over time."*(07:19~07:31) ⚠️ 화자 요약.
- *"in the Opus 4 days, uh, or maybe even Sonnet 3.5, you would write the code and it would be a little sloppy and you would say, 'You know what? The code is slop, but that'll be GPT-7's problem.' Folks, we're at GPT-6, and I don't think we've gotten that much better at this."*(07:35~07:52) 그리고 *"people are online begging like please someone produce RL tasks about abstraction and centralization cuz these models still can't do it."*(08:05~08:12)
- ⭐ **Steve**: *"Gas Town, which apparently is only good for building other Gas Towns."*(08:18~08:23) *"he went around the internet telling people for a year that if you're still trying to read the code, you are going to fall behind."*(08:25~08:31) → *"And here he is in last week. Yeah, if you don't pay attention to the models, they're going to write slop code. They're going to build something so complex that they themselves can't debug it. So even Steve's come around."*(08:33~08:43) ⚠️ 성 Yegge는 챕터·설명란에만.
- Astra: *"here's the numbers by the way on Astra and Sol X I. Astra is one percentage point or 1.5% percentage points higher than GPT-5.5. So we are getting better at writing maintainable code (…) but not as fast as some people would have you have you believe."*(08:43~09:01) ⚠️ *"Sol X I"* 판독 보류. → [[openai-astra]]
- 결론: *"So if unattended model code gets worse over time, then for now we should probably read the code"*(09:01~09:07)

→ [[ai-slop]] · [[openai-astra]] · [[fable-5-1]](*"even Astra and Fable"* 07:33 — 문장이 끊긴다) · [[terminal-bench]] · [[tech-bridge-kent-beck-craft-augmented-development]](Steve Yegge 언급)

## 6. "12 factor factories" — 실제로는 아홉 (09:07~13:09)

화자 스스로 *"they told me I couldn't call this, but 12 factor factories. I will come up with a better title than that."*(09:08~09:14), 끝에서 *"I think it's only nine. It's not even close to 12."*(12:55~12:58). 발화 순서대로:

| # | 실천 (en-orig) | 핵심 |
|---|---|---|
| 1 | *"plan before you build. 20 minutes 30 minutes up front can save you hours during review."*(09:19~09:24) | 사람 팀이 AI 이전에 배운 것 — *"if it takes hours or days to build something, and if it takes hours or days to review something, then we better get together as a team"*(09:27~09:39). 단 *"don't over plan though"*(09:55~09:57) |
| 2 | *"you should align visually. Um, we published a skill called show me."*(10:52~10:55) | *"doesn't make you have to read like walls and walls of like agentic paragraphs and prose"*(11:01~11:08), stacked PR 분할·변경 순서를 맞춘다(11:08~11:13). 자사 오픈소스 |
| 3 | *"help agents test their work. (…) Give them a browser, let them run the app, let them use curl, let them record videos (…) Like give them back pressure."*(11:17~11:25) | → [[agent-verification-skill]] · [[agent-visual-qa]] |
| 4 | TypeScript: *"This is Dylan Mulroy. There's about a hundred anti-slop rules. He literally just like went through and cataloged every anti-pattern that agents put in the TypeScript code base and built excellent rules for them."*(11:30~11:42) + *"a bunch of stuff in the Slop Code Bench paper that you can steal"*(11:42~11:45) | → [[hard-vs-soft-enforcement]] · [[tech-bridge-sentry-stop-prompting-codify-linters]] |
| 5 | *"you should feed user feedback into the factory instead of like reading support tickets and then turning them into Jira tickets. You should just uh read the support ticket and the PR that the agent made for you."*(11:45~11:56) | 사람은 티켓 변환 대신 **티켓 + 에이전트 PR**을 읽는다 |
| 6 | *"For incidents, when you get paged at 3:00 in the morning, like have have the pager alert come with the PR the agent thinks will fix it. Even if you can only merge 50% of those, that's a huge difference in your throughput"*(11:54~12:05) | ⚠️ 50%는 가정 |
| 7 | *"let models experiment. Uh, give them feature flagging tooling (…) 'Hey, here's three versions of this feature.'"*(12:08~12:15) | UI: *"they can make beautiful UIs, but they can't really see them in the way that you and I see them"*(12:17~12:21) → *"give three UIs to all of your users and figure out which one people can figure out. This is how you give (…) your models back pressure for UI."*(12:21~12:30) — **사용자가 검증자** |
| 8 | ⭐ *"I think loops are basically a combination of forward pressure and back pressure. This idea of loops was a little mystical."*(12:30~12:36) | forward = *"What triggers cause new work to happen?"* — *"schedules or automations or webhooks"*; back = *"how do you give the agent like feedback while it's working so it can hill climb an outcome without having to go to a human?"*(12:36~12:55) → [[back-pressure]] (신규) |
| 9 | *"compound over time, learn from past sessions, go read what your engineer go analyze the sessions of your team, figure out what they're struggling with, figure out how to get that into your skills or your memory or whatever it is."*(12:58~13:09) | → [[trace-to-memory-loop]] · [[skill-self-improvement]] |

### expected pain — 계획의 깊이를 고르는 법 (09:55~10:52)

| 투입 | 화자가 든 재작업 확률 |
|---|---|
| *"YOLO a two-sentence prompt"* | *"probably a 50% chance you're going to be doing more prompting later"*(09:59~10:04) |
| *"handwrite a detailed spec for (…) 5 hours"* | *"maybe there's only a 10% chance (…) You just do a little bit of polish at the end."*(10:05~10:14) |
| *"write all the code by hand for 20 hours"* | *"there's a 0% chance you have to rework it because of something the agent did. Uh, you might still have to fix stuff. Uh, this is why we had code review before."*(10:14~10:26) |

- ⭐ *"I think of this in terms of expected pain, right? How how likely will you have to change something and how painful is that change?"*(10:26~10:32) — 버튼 색은 계획 중에 다투지 않는다(*"I know I can go change that later"* 10:38~10:42). *"you got to find your way up and down this curve depending on the task and depending on the code base (…) But planning is about eliminating expected pain."*(10:42~10:52)
- ⚠️ 수치는 직관(*"I think of this is like"* 09:59). 설명란의 *"수십 시간의 디버깅과 전면 재작업을 막아줍니다"* 는 발화보다 강하다(발화는 *"save you hours during review"*).

→ [[expected-pain-planning]] (신규) · [[spec-driven-development]] · [[plan-to-ticket-pipeline]] · [[risk-proportional-human-review]]

## 7. 새 software forge와 네 층 (13:09~14:53)

- 비유: *"has anyone remember the days when we used to send get[=git] patches around on like email lists? I think I think Linus still does this (…) but almost everybody now uses GitHub. (…) the protocol is is decentralized, but we have a centralized place to do this."*(13:12~13:30)
- ⭐ *"now there's other parts of the SDLC that I think are first class. So, you have session traces, you have architecture docs"*(13:28~13:35). 지금은 *"the AI native version of this Git mailing list thing is like I'm talking to my agent and I copy something out and I paste it into Slack or Teams. My my teammate reads it, they paste it into their agent (…) I paste that into my agent."*(13:35~13:50) → *"we need a place where our sessions and plans and prompts and all this stuff kind of lives in in a centralized sort of system of record."*(13:53~14:01)
- **네 층**(14:19~14:53, *"Each of these layers you can buy or build."*):

| 층 | 발화 |
|---|---|
| compute | *"we have some spare pods in our Kubernetes cluster (…) or you can go buy Daytona or E2B or whatever it is"*(14:23~14:33) |
| dev environment | *"How do you get your language set up? Your runtime? Your preview environments? Do I need to connect to internal services in our VPC in order to even run a dev environment so an agent can test its work?"*(14:33~14:43) |
| harness | *"of course, the harness, which you can buy or build. There's a ton of options here."*(14:43~14:47) |
| control plane | *"How do I dispatch work? How do I collaborate on sessions and plans?"*(14:49~14:52) |

- *"There's like an hour-long deep dive on just this slide."*(14:12~14:15) — 이 영상에선 개요만.

→ [[agent-platform-layers]] (신규) · [[harness-as-platform]] · [[model-harness-knowledge-stack]] · [[human-plumbing]](복사·붙여넣기로 사람이 배관이 되는 같은 모양)

## 8. HumanLayer — control plane의 multiplayer 워크스페이스 (14:53~16:05)

- *"human layer, we're kind of working very closely in this control plane. (…) We also have a custom harness that we really like. We're going to open source it in the next couple weeks."*(14:53~15:02)
- *"human layer is a shared collaborative workspace. I can see everything my team is working on. I can jump into a teammate session. I can invite people to co-prompt my session. Not even in the cloud, like it can be running on my laptop and I can pull somebody into my cloud code[=Claude Code?] session. It's got sort of a Google Docs Notion-shaped uh artifact collaboration built into the session view."*(15:03~15:22)
- ⭐ *"every agent running anywhere as it's writing code the diffs are streaming to the cloud. So we can do code review uh without waiting for pull request."*(15:22~15:31) — **리뷰를 PR 이전으로 당긴다.**
- *"We've been building this for a year basically mostly in secret"*(15:32~15:37). 자료: *"humanlayer.dev/resources for everything that's kind of chronological and broken into eras of like hey we learned a new thing and we kind of like revised our thinking on some stuff."*(15:46~15:58)

→ [[multiplayer-agent-context]] · [[verification-bottleneck]] · [[humanlayer]] (신규)

## 이 위키와의 연결

### 이어지는 것

- **[[software-factory]] — lights-off 반론의 세 번째 화자.** [[kent-beck|Kent Beck]]의 *"there's no human involved There's no feedback. And that always goes off the rails. Always."* 에 이어 Horthy는 **원인**을 댄다 — *maintainability has no fast oracle*(06:13~06:15), 그래서 RL이 아키텍처를 보상하지 못한다. 그리고 [[tech-bridge-conductor-orchestras-not-factories|Conductor]]의 *오케스트라* 반론과 달리 그는 **"공장" 은유를 버리지 않는다** — 공장은 원래 사람이 있는 SDLC였다(02:31~02:42).
- **[[verification-bottleneck]]** — agentic형 공장에서 빌드는 분 단위, 리뷰는 여전히 시간·일 단위(04:31~04:37). 처방은 "리뷰를 없앤다"가 아니라 ① 계획을 앞에 둬 리뷰를 줄이고(09:21~09:24) ② 에이전트 back pressure로 작은 것을 걸러내고 ③ **diff 스트리밍으로 PR 이전 리뷰**(15:22~15:31).
- **[[verifiable-goals]] · [[reward-hacking]]** — *"just trying to get the test to pass without really like rewarding good architecture"*(06:00~06:04)는 [[tech-bridge-factory-software-factory|Factory 편]]의 루프 *"cheating"* 과 같은 현상을 **학습 단계**에서 설명한다. 이 위키에서 처음으로 *검증 지연*(months and years)을 이유로 든다.
- **[[ai-slop]]** — 정의는 하지 않지만 원인론을 하나 더한다: 슬롭은 *시간이 지나며 쌓이는* 것(*"messy code that accumulated over time"* 07:22~07:26, SlopCodeBench의 점진 공개 설계). [[tech-bridge-goodbye-slop-state-machines|Khourshid]]의 *"구조 없는 위임"* 과 나란하다.
- **[[hard-vs-soft-enforcement]] · [[tech-bridge-sentry-stop-prompting-codify-linters]]** — 같은 주(10-13·10-14 업로드) 두 화자가 **lint 규칙으로 슬롭을 막는다**는 처방을 낸다. Pstrucha는 *자기 트랜스크립트를 에이전트에게 훑게 해* 규칙을 만들고, Horthy는 **남이 카탈로그한 ~100개 규칙**(Dylan Mulroy)을 가져다 쓰라고 한다.
- **[[trace-to-memory-loop]] · [[skill-self-improvement]]** — *"analyze the sessions of your team (…) get that into your skills or your memory"*(13:01~13:08). 그리고 그 재료(세션 트레이스)를 **SDLC의 first-class 산출물**로 보관할 곳(system of record)이 필요하다는 도구 쪽 결론(13:28~14:01).
- **[[multiplayer-agent-context]]** — HumanLayer는 Conductor 편의 *여러 사람 × 여러 에이전트 공유 워크스페이스* 와 같은 범주의 제품이다. 차이: 세션이 **로컬 노트북에서 돌아도** 다른 사람을 끌어온다(15:12~15:16).
- **[[human-plumbing]]** — Slack에 복사·붙여넣기로 팀원의 에이전트와 내 에이전트를 잇는 묘사(13:39~13:50)는 Rails 편의 *사람이 배관 노릇* 과 같은 모양이다. Horthy의 해법은 하네스가 아니라 **공유 기록(system of record)**.

### 갈리는 것

> ⚠️ **Contradiction: lights-off/dark factory는 지금 가능한가.** [[tech-bridge-lauren-tan-pocock-podcast-full|Lauren Tan]]은 에이전트가 자기 PR을 머지하는 자기 환경을 *"It kind of is"*(dark factory)라 받아들이고, [[software-factory]]의 [[tech-bridge-cooking-with-codex|Codex 편]]은 *"기계를 만드는 기계"* 를 목표로 든다. Horthy는 *"unattended models will not improve or maintain your code base quality over time"*(05:17~05:23), *"for now we should probably read the code"*(09:03~09:07). 다만 그도 *"theoretically, if you invest into all this other stuff, you could like, probably get uh, close to a place where where this would actually work"*(05:03~05:11)라고 **원리적 불가능은 주장하지 않는다** — 갈리는 것은 *지금* 이다. ⚠️ 그리고 화자의 단어는 **lights-off**(en-orig 04:49)이고 *dark* 는 `en`·ko 번역이다 — 위키는 두 이름을 같은 대상으로 읽는다.

> ⚠️ **긴장: "loops"는 신비가 아니다 vs 루프가 제품이다.** [[loop-is-the-product]]는 루프를 제품의 단위로 올린다. Horthy는 *"This idea of loops was a little mystical"*(12:34~12:36)이라며 **trigger(forward) + feedback(back)** 두 질문으로 분해한다. 모순이라기보다 **해체 방향**이 다르다. 용어 주의: Horthy의 *forward pressure* 는 **일을 시작시키는 trigger**이고, [[feedforward-feedback-steering]]의 *feedforward* (행동 전 안내)와 **다른 개념**이다.

> **[[tech-bridge-death-of-code-review|Voss]]와의 관계.** Voss는 Horthy의 철회(*"Please please read the code"*)를 근거로 들면서 처방은 *"stop reviewing PRs"* 였다. Horthy 자신의 처방은 **PR을 기다리지 않는 리뷰**(15:28~15:31)다 — *PR 리뷰를 그만둔다* 와 *PR 이전으로 리뷰를 옮긴다* 가 같은 문장 *"review moves"* 의 두 판본이 된다. 이 영상에서 화자는 자기 철회를 직접 말하지 않는다.

## 해소하지 않고 표시만 한 것

- 5월 리포트의 정체·수치. Anthropic 포스트모템의 원문·날짜. Steve의 *"last week"* 발언 원문.
- SlopCodeBench 14.8%의 지표 정의, Astra 차이(1 vs 1.5 percentage points)가 어느 벤치마크인지, *"Sol X I"* 의 정체. Snorkel과의 관계(설명란 리더보드 링크만).
- *"even Astra and Fable"*(07:33) 문장이 무엇을 말하려 했는지(끊김).
- Dylan Mulroy 저장소의 이름·URL·라이선스(화면에만). show me 스킬 URL·20K의 근거.
- 1968년 진술의 출처. *"this talk from June"* 의 행사.
- 네 층 슬라이드의 *"hour-long deep dive"* 내용. 오픈소스 예정 custom harness의 이름.
- 행사명(AGNTCon NA 추정)·도시·녹화일. *"10 minutes"* 슬롯과 16분 영상의 차이.

## 등장 개체

- 인물: [[dex-horthy|Dex Horthy]](신규 제안 — 이름 *"Dex"* 와 직함은 발화, 성은 제목·설명란에만) · Steve Yegge(⚠️ 성은 챕터·설명란에만, 발화 *"Steve"* — 페이지 없음, 신규 제안은 선택) · Dylan Mulroy(ASR 철자, 페이지 없음) · Andrew·Angie(현장 인물, 성 미발화) · Linus(Torvalds 추정, 성 미발화)
- 조직: [[humanlayer|HumanLayer]](신규 제안) · [[anthropic|Anthropic]] · University of Wisconsin(페이지 없음) · Snorkel(⚠️ 설명란 링크만)
- 모델: [[openai-astra|Astra]] · [[fable-5-1|Fable]](⚠️ 버전 미발화) · GPT-5.5 · GPT-6 · GPT-7(가정) · [[claude-opus-4-5|Opus 4.5]] · Opus 4 · Sonnet 3.5 · *"Sol X I"*(⚠️ 판독 보류)
- 벤치마크·도구: [[slopcodebench|SlopCodeBench]](신규 제안) · [[terminal-bench|Terminal-Bench]](*"terminal bench"*, 버전 미발화) · show me(HumanLayer 스킬) · Gas Town · Linear · Jira · Beads · Kubernetes · Daytona · E2B · GitHub · Slack · Teams · Google Docs · Notion · [[claude-code|Claude Code]](⚠️ ASR *"cloud code"*) — 대부분 페이지 없음
- 개념: [[back-pressure]](신규 제안) · [[expected-pain-planning]](신규 제안) · [[agent-platform-layers]](신규 제안) · [[software-factory]] · [[verification-bottleneck]] · [[ai-slop]] · [[verifiable-goals]] · [[reward-hacking]] · [[hard-vs-soft-enforcement]] · [[trace-to-memory-loop]] · [[skill-self-improvement]] · [[multiplayer-agent-context]] · [[human-plumbing]] · [[loop-is-the-product]] · [[feedforward-feedback-steering]] · [[spec-driven-development]] · [[plan-to-ticket-pipeline]] · [[risk-proportional-human-review]] · [[agent-verification-skill]] · [[agent-visual-qa]] · [[scheduled-agent-automations]] · [[harness-as-platform]] · [[model-harness-knowledge-stack]] · [[context-engineering]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=XejHwIKi5qg> (16:11, `upload_date` 2026-10-14)
- raw: `01.raw/articles/2026-10-14_코드 슬롭(Code Slop)과의 싸움 - 소프트웨어 팩토리의 현실을 짚어봅니다 - Dex Horthy.md`
- 설명란 링크: <https://humanlayer.dev/resources> · <https://www.humanlayer.dev/> · <https://github.com/humanlayer/12-factor-agents> · <https://arxiv.org/abs/2603.24755> · <https://snorkel.ai/leaderboard/slopcode-bench/> · <https://hubs.la/Q04gbXLb0> · <https://aaif.io/> (⚠️ 열어 보지 않았다)
- 같은 인물의 다른 언급: [[tech-bridge-death-of-code-review]](Voss가 인용한 철회)
- lights-off/dark factory 논쟁: [[tech-bridge-kent-beck-craft-augmented-development]] · [[tech-bridge-lauren-tan-pocock-podcast-full]] · [[tech-bridge-conductor-orchestras-not-factories]] · [[tech-bridge-factory-software-factory]] · [[tech-bridge-cooking-with-codex]]
- 같은 주의 lint 처방: [[tech-bridge-sentry-stop-prompting-codify-linters]]
- [[tech-bridge]] · [[humanlayer]] · [[dex-horthy]]
