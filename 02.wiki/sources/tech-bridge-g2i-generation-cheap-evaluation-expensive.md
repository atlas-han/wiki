---
title: "Tech Bridge — 생성은 저렴하지만 검토는 비쌉니다 (Gabriel Martinez · G2i): 슬롭은 생성이 판단을 앞지를 때 생긴다 — 줄은 비용, 이해는 비싸고, 답은 관례·압축된 리뷰 표면·작은 변경"
type: source
tags: [ai-slop, judgment, ownership, code-as-liability, lines-spent, big-ball-of-mud, prototype-illusion, happy-path, performance-anxiety, incentives, large-prs, review-burden, verification-bottleneck, generation-vs-evaluation, ralph-loop, tokens-as-loc, diagrams, compressed-review-surface, declarative-code, cognitive-overhead, conventions, convention-over-configuration, rails, orchestration, vendor-pitch, g2i, video]
source-url: https://www.youtube.com/watch?v=utMfI1DXTOE
source-type: video
author: Tech Bridge (한영자막 재배포) · 발표 Gabriel Martinez("Gabo", [[g2i|G2i]] engineering manager · "resident slop warden" — **자막에서 직접 자기소개**, 설명란과 일치) · 행사명 미발화(설명란 ai.engineer 링크 + #AIEngineer → AI Engineer 계열 추정) · 녹화일 미발화
date-published: 2026-10-14
ingested: 2026-10-15
created: 2026-10-15
updated: 2026-10-15
---

# Tech Bridge — 생성은 저렴하지만 검토는 비쌉니다 (Gabriel Martinez · G2i)

[[tech-bridge|Tech Bridge]]가 재배포한 **16:48 단독 발표, Q&A 없음(끝에 박수), 공식 챕터 23개.** 화자 [[gabriel-martinez|Gabriel Martinez]]는 자막에서 스스로 소개한다 — *"My name is Gabriel Martinez. I go by Gabo. I'm an engineering manager and resident slop warden at G2i, and I'm here to talk about slop."*(00:00~00:08) [[g2i|G2i]]가 무슨 회사인지는 발화되지 않는다. 측정·사례 데이터는 없고, **원칙 선언 + 개인 고백 + 마지막 1분여의 자사 도구(ORC) 소개**다. 테제:

> **슬롭은 AI가 쓴 코드가 아니라 생성이 판단을 앞지른 산출물이다 — 생각이 끝나기 전에 끝나 보이는 것. 위험은 기계의 나쁜 선택이 아니라 엔지니어가 선택이 있었다는 걸 모르는 것이다. 코드는 부채이고 줄은 "쓰는 것"이며, 생성 비용은 떨어져도 이해 비용은 떨어지지 않는다. 사람이 평가할 수 있는 것보다 많이 생성하면 팀은 빨라지지 않고 병목이 생긴다. 그러니 사람이 이해할 층 — 다이어그램·선언적 코드라는 압축된 리뷰 표면, 관례, 작은 변경 — 에 최적화하라.**

> *"Slop is what happens when (…) generation outruns judgment. Slop is not AI-generated code."* (00:29~00:34) · *"Generation is cheap, but evaluation is expensive."* (10:05~10:08) · *"humans need a compressed review surface"* (12:35~12:37) · *"The future is orchestration with judgment."* (16:39~16:41)

이 위키에 개념 하나가 생긴다 → [[compressed-review-surface]](신규 제안 — 다이어그램·선언적 코드·잎으로 밀어낸 구현으로 사람이 볼 면을 압축). 나머지는 기존 페이지의 **새 증언**이다 — [[ai-slop]]("슬롭 = 결정의 부재"의 코드판 정의, *"Slop is not AI-generated code"*), [[verification-bottleneck]](*"it has created a bottleneck"*), [[trusted-throughput]](토큰 = LOC의 반복), [[ralph-wiggum-method]](*"just a while loop"* — 첫 회의적 언급), [[codebase-gardening]]·[[organic-architecture]](big ball of mud를 에이전트가 키운다), [[hard-vs-soft-enforcement]]·[[tech-bridge-rails-harness-engineering|Rails 편]](Rails 관례).

ASR·ko 보정: ko는 **슬롭 정의의 부정문을 긍정문으로 뒤집는다** — *"They never hit the ambiguity. They never felt the constraint"* → **"절대 / 그들은 모호함에 직면했다. 절대 / 그들은 제약을 느꼈다"**(01:06~01:12), *"where ownership was not taken"* → **"책임을 맡았다"**(00:53). 근거 문장도 흔든다 — *liability* → **"수동적인"**(02:57), *"AI makes it easier to spend lines"* → **"더욱 어렵게"**(04:08), *"Unless tamed, it exacerbates it"* → **"통제하려 애쓰는 것이 악화시킨다"**(13:26~13:29), *"haven't even tested themselves"* → **"직접 테스트해봤습니다"**(08:11). 수치: *multi-thousand line PR* → **"수천 건의 PR"**(08:35), *a gap of 4 years* → **"4분 간격"**(14:29). 결론부의 *"Not only because we think the answer is more agents"* → **"해답은 더 많은 요원을 배치하는 것"**(15:36, 단정문). ko·`en` 공유: *reviewable surface* → "수정 가능한 표면"/*"revisable"*(12:49), *a large PR* → "훌륭한 홍보 효과"/*"a great PR"*(09:53), *vibe coding* → "라이브 프로그램"/*"programming live"*(16:35). ko 단독: slop → **"기울기"**(00:27), choices → **"선거"**, PR → **"영주권"**(07:49), Rails → **"울타리"**(15:13). 전체 목록은 raw.

> ⚠️ **수치가 없다.** 숫자는 모두 예시·일화다 — *"10 bullets of scope"* → *"a 20-page document"*(09:19~09:26), *"12 escape hatches"*(04:38), *"multi-thousand line PR"*(08:37~08:39), *"a gap of 4 years"*(14:27~14:31). 어떤 팀·조직에서 몇 번 관찰했는지 없다. 챕터·설명란의 **"1,000줄짜리 PR"은 업로더 표기**다(발화는 *multi-thousand*).
>
> ⚠️ **자사 도구 소개.** 15:32~16:35는 G2i가 만든 ORC 소개다 — 이름 표기 ORC는 **챕터·설명란(`orc.ai`)에서만**, en-orig는 *"Ork"*. 기능은 *"The planning, the review, the adversarial checks, the context management"*(15:52~15:57)를 *"baking them into the workflow"*(16:11~16:15)한다는 데까지다. 사용법·고객·효과 수치 없음. 앞 15분의 진단이 이 도구의 동기로 제시된다(*"Everything I've talked about today is what led us to build Ork."* 15:32~15:35).
>
> ⚠️ **인용은 모두 화자를 거친다.** SQLite 제작자 인용은 **트윗을 통한 2차 인용**(06:38~06:45, 이름·원 출처 미발화, 트윗은 화면에만), Dijkstra의 *"lines spent"*(04:01~04:08)는 원 문헌 미제시, Rails doctrine의 두 기둥(15:14~15:18)은 화자 진술. 원문과 대조하지 않았다.
>
> ⚠️ **행사·시점.** 행사명·도시·연도 미발화. 설명란 `https://ai.engineer`·AI Engineer 링크·#AIEngineer → **[[ai-engineer|AI Engineer]] 계열 추정**(확정 아님). 시점 단서 *"the advancements made since December 25th"*(01:56~01:58)는 날짜인지 *December '25* 인지 판독 보류.

## 1. 슬롭의 정의 — 판단이 끝나기 전에 끝나 보이는 것 (00:00~01:41)

- *"The term slop has been beaten to a pulp, but the thing it points at has long been around. Only now it happens at warp speed."*(00:17~00:23) → [[ai-slop]]의 "슬롭은 AI 이전부터 있었다 — AI는 가속기"와 같은 문장.
- ⭐ *"Slop is what happens when judgment when generation outruns judgment. Slop is not AI-generated code."*(00:29~00:34) — *"I don't mean to define it as some concrete objective thing that can easily be sniffed out, although there are tells."*(00:36~00:41) 탐지 가능한 속성이 아니라 **과정의 결함**으로 정의한다.
- ⭐ *"Slop is output that looks finished before the thinking is finished. It is work product where ambiguity ambiguity was cleared with guesses, where tradeoffs were left to chance, where ownership was not taken. Output was produced, sure, but understanding was not."*(00:43~00:58)
- ⭐ 진짜 위험: *"the real danger is not simply that the machine made a bad choice. The danger is that the engineer never noticed that there was a choice to make. They never hit the ambiguity. They never felt the constraint. They never discovered the edge case that would have changed the design."*(01:01~01:14) — *"the unknown unknowns stayed unknown."*(01:19~01:21)
- *"software is a record of choices (…) If we do not see those choices, we cannot own them. And if we do not own them, we are not really engineering. We are just accepting output. We are just a code monkey hitting the merge button."*(01:23~01:41)

→ [[ai-slop]]("슬롭 = 결정의 부재" — Paul의 *"아무도 아무것도 결정하지 않았다"* 를 코드에서) · [[cognitive-offloading]] · [[decision-quality]]

## 2. AI는 나쁘지 않다 — 그러나 사람만의 일 (01:42~02:41)

- *"I'm not the purist that's come here to (…) tell you that AI is bad. It's not bad, okay?"*(01:42~01:47) *"we need to dial it in. We need to slow down. We need to sober up."*(02:00~02:03)
- 에이전트는 *"write code, scaffold screens, and with right tuning can build whole features or systems"*(02:10~02:15)지만 대체할 수 없는 것: *"deciding what matters, understanding what is being built, interpreting ambiguity, owning the system for the long haul, exercising judgment and restraint at the system architecture level, and arguably the most important important, knowing what not to build."*(02:16~02:33)
- *"Slop is not about AI as a tool, rather it is about the absence of judgment."*(02:34~02:39)

→ [[taste-vs-judgment]] · [[architecture-as-remaining-art]]

## 3. 코드는 부채, 줄은 "쓰는 것" (02:44~04:46)

- *"In a world where anything is possible, deciding what to build is more important than ever."*(02:44~02:47)
- ⭐ *"any line of code you write is a liability, that the best code is no code at all. The cost of creating code is falling, but the cost of understanding a software program is not."*(02:54~03:06)
- 단서 — 모든 줄을 읽으라는 게 아니다: *"I'm not saying every line of code needs to be personally read, blessed, and understood in isolation. That has never really been the standard."*(03:06~03:13) *"But the logic has to be understood. The main flows, the boundaries, the data model, and product behaviors have to be understood."*(03:19~03:25) → §7의 압축된 리뷰 표면의 전제.
- *"The code should reflect the shape of the domain."*(03:32~03:34) *"An agent can operate with much more effectively inside a code base that has structure, patterns, clear boundaries, and rationale. But if the system is already a big ball of mud, the agent does not rescue you from the mud. It just builds the ball bigger, faster."*(03:41~03:54)
- ⭐ Dijkstra(화자 인용): *"If we could count lines of code, we would not think of them as lines produced, but as lines spent."*(04:03~04:08) *"AI makes it easier to spend lines. It makes it easier to spend on files, abstractions, and complexity, but at the end of the day, you own the bill."*(04:10~04:16) 청구서는 *"confusion, brittle flows, features nobody wants to touch"*(04:19~04:24), 모든 화면에 *"12 escape hatches"*(04:38)가 있는 B2B 소프트웨어로 나타난다.

→ [[technical-debt]] · [[codebase-gardening]](*"코드베이스는 에이전트의 기억"* — 진흙이면 진흙을 키운다) · [[organic-architecture]] · [[legacy-code-modernization]](big ball of mud)

## 4. 책임과 프로토타입의 환상 (04:46~07:06)

- *"Teams should be held accountable for work they are producing. Accountability is the keyword here."*(04:46~04:51) *"Just in the mere fact of knowing that someone else will review your work will force engineers to pay just a little bit more attention to the finer details"*(04:57~05:04), *"Especially if there are accountability metrics that can be made visible for each chunk of work product."*(05:06~05:11) ⚠️ 어떤 지표인지는 발화되지 않는다.
- *"Today, anyone can buy code[=vibe code] an application in an hour and end up with a working clickable prototype. And that has changed expectations."*(05:21~05:29)
- ⭐ *"stakeholders that do not live in the code base often experience that prototype as evidence that the hard part is over."*(05:51~05:57) 엔지니어의 몫은 *"outside the happy path"*(06:00~06:02) — 기능 통합, 요구사항 명확화, 수동 테스트, UX(06:02~06:19), *"the last mile, where the judgment lives."*(06:24~06:26)
- SQLite 제작자(트윗 경유 2차 인용): *"You say, 'Oh, it's free.' No, it's not free. What you're doing is asking me to maintain it for you, to document it for you, to test it for you, to maintain it for you for the next 25 years. That is not free."*(06:45~06:55) → *"It's easy to yield a PR, but who has to own that thing?"*(07:00~07:04)

→ [[named-human-accountability]] · [[code-is-the-product]]("PR을 받는 자리") · [[slop-cannon]]

## 5. 성과 불안과 인센티브 (07:07~08:31)

- *"external pressures from stakeholders coupled with pressures of competing with slot meisters[=slop meisters] begets mucho slop-o."*(07:07~07:15)
- ⭐ *"the bad engineers, the ones who don't review the details, that don't refine the spec, that aren't detail-oriented, end up producing more faster. The folks who pay attention to the detail and go above and beyond are the ones that might seem like they're doing less and moving slower."*(07:19~07:33)
- *"team environments can pressure engineers to merge PRs faster than they can judge, leading to code being merged without full understanding."*(07:39~07:46)
- ⭐ 고백: *"I've personally felt this anxiety where engineers around me were merging at an incredible pace (…) And I can admit that it led me to merge code that I didn't necessarily review with a level of detail that I normally do or should have."*(07:52~08:05)
- *"We are driven by incentive. And if incentives are driving people to get PRs in, then we're going to be in for a rude awakening."*(08:15~08:22) 보상의 대상: *"producing value, elegant, well-factored, pragmatic system design, and around clarity of test and evaluation harnesses."*(08:24~08:31)

→ [[trusted-throughput]](⚠️ Goodhart — PR 수) · [[verifiable-goals]]

## 6. 큰 PR과 20페이지 문서 — 생각을 검토자에게 넘긴다 (08:34~10:17)

- *"seeing a multi-thousand line PR. There's no way in hell that a human can fully understand all the important bits of a change that big."*(08:36~08:43) *"It is our job as engineers to optimize for this new world, to decompose needs into its simplest chunks, which lends to understanding"*(08:44~08:51)
- *"What AI is really doing is producing more faster, more characters that eat more human time."*(09:11~09:16)
- ⭐ 일화: *"You give someone 10 bullets of scope, a few user journeys, something intentionally lightweight, and they come back with a 20-page document. (…) now I have to spend hours figuring out whether there's any real thinking inside it."*(09:19~09:35) *"It does not clarify the problem, it expanded it. It took ambiguity that should have been resolved by the person doing the work and handed it back as a larger artifact for other stakeholders to do it."*(09:38~09:50)
- *"In code, a vague task becomes a large PR. A small feature becomes a pile of files. The output arrives with the shape of completion, but the real work has just moved to the reviewer."*(09:51~10:02)
- ⭐ *"Generation is cheap, but evaluation is expensive. If AI produces more than humans can possibly evaluate, it has not accelerated the team, it has created a bottleneck."*(10:05~10:17)

→ [[verification-bottleneck]] · [[cognitive-debt]] · [[agent-attention-management]]

## 7. Twitter·Ralph loop·토큰 — 오래된 진실의 망각 (10:20~11:23)

- *"The Ralph loop was one of those. It was made to sound like a novel agentic breakthrough, when it's just a while loop."*(10:34~10:40) → [[ralph-wiggum-method]] — 이 위키에서 Ralph loop에 대한 **첫 회의적 평가**(기법을 부정하기보다 "새로움"을 부정).
- ⭐ *"we've completely forgotten that lines of code is a garbage metric for productivity, but then we decided that it's different than deciding the engineer who burns the most tokens must be producing the most."*(10:41~10:51) → [[trusted-throughput]]의 "토큰은 LOC다"와 같은 논증.
- *"We used to break a feature into small atomic pieces we could reason about. Small enough to hold in your head and actually review. Now, we type two sentences and expect a whole not fully thought out feature set back in one shot"*(10:52~11:05)
- *"60 years of software wisdom hasn't been invalidated by AI. Composable code, good patterns, and solid practices remain essential."*(11:16~11:23)

## 8. 코드의 모양은 왜 여전히 중요한가 — 압축된 리뷰 표면 (11:28~13:09)

- 친구의 질문: *"If the agent writes the code, why should we care about what the code looks like? And to an extent, I agree."*(11:43~11:47) 추상화 사다리(machine code → assembly → C → Java → Ruby, 11:56~12:09): *"AI is abstracting away the imperative bits. It does not remove the need to understand how a system comes together cohesively."*(12:14~12:21)
- ⭐ *"This is why diagrams matter so much, not as decorative documentation after the fact, but as a way of making systems legible. When a agents can generate thousands of lines of implementation detail, humans need a compressed review surface, service boundaries, data flows, state transitions, and failure modes."*(12:23~12:42)
- ⭐ *"We can leave the main process or workflow as the reviewable surface with implementation details pushed to the leaves. That is why I vouch for declarative code and architecture patterns that create layers humans can actually reason about."*(12:47~12:57)
- *"The goal is not just code generation, the goal is human knowledge, human understanding, and human review. We need to optimize for that human layer."*(13:00~13:09)

→ [[compressed-review-surface]] (신규) · [[deep-modules]](복잡함을 잎·인터페이스 뒤로) · [[agent-state-machine]](상태 전이를 리뷰 면으로) · [[read-fluency-for-agent-output]]

## 9. 인지 오버헤드와 관례 — Rails (13:11~15:29)

- ⭐ *"Cognitive overhead is a tax every engineer has to pay before they can make a meaningful change. It is the time spent figuring out where code belongs, which pattern to follow, and what proper implementation actually means. AI does not remove this tax. Unless tamed, it exacerbates it."*(13:11~13:30)
- *"An agent can generate five plausible patterns in five different styles. And now the human reviewer has to reverse-engineer not just the code, but the intent behind it."*(13:31~13:41)
- 처방 목록: *"conventions, standards, documented flows, small reviewable surfaces, and clear ownership boundaries and definitions of done. The more obvious the path, the less room there is for slop to hide."*(13:46~13:58)
- Rails: *"it shows what happens when a framework aggressively reduces decision surface. (…) Rather than ending up with 10 different ways to structure the same concept, you end up with one."*(14:07~14:20) 4년 공백 뒤에도 *"the same patterns and de facto libraries"*(14:27~14:41) — *"I could hop right back into a code base and immediately understand intent"*(14:42~14:45).
- ⭐ *"Environments with a single correct way of doing things are superior for agentic development because agents aren't confused by dozens of competing approaches."*(15:01~15:09) 대비: *"The same can't be said about other language ecosystems. JavaScript."*(14:55~14:57)
- Rails doctrine(화자 진술): *"Optimized for programmer happiness"* · *"Convention over configuration"*(15:14~15:18), 관례 = *"a way to eliminate recurring decisions and lowering the barrier to getting started. It is the reduction of cognitive overhead."*(15:21~15:29)

→ [[hard-vs-soft-enforcement]](§"기술 스택이 강제 수단이 된다") · [[tech-bridge-rails-harness-engineering]](Quenneville — 같은 Rails를 RuboCop·제너레이터로) · [[framework-defined-agent-infrastructure]](*convention* 기반 선언) · [[dhh|DHH]](⚠️ 이름은 발화되지 않는다)

## 10. ORC — 자사 도구 (15:32~16:46)

- *"Everything I've talked about today is what led us to build Ork. Not only because we think the ants Not only because we think the answer is more agents, and definitely not because we think engineering judgment can be automated away."*(15:32~15:44) ⚠️ *"Not only"* 은 말을 고친 자리 — 뒤의 *"definitely not"* 과 짝지어 **"에이전트를 더 넣는 게 답이라서가 아니다"** 로 읽는다(판독).
- *"AI could generate code, but the surrounding discipline was still missing. The planning, the review, the adversarial checks, the context management."*(15:48~15:57) *"Break down the work, manage context, weigh out your options, and make sure the output enters the code base in the way the team that can still reason about."*(16:02~16:10)
- *"It is not a magic box that makes correctness disappear as a human responsibility. It is a system for preserving that responsibility while letting agents do more of the lift."*(16:15~16:23)
- ⭐ *"The goal is not to ship more generated code. The goal is to ship software that is still coherent, tested, maintainable, and owned after the generation happens. Because the future is not vibe coding better, faster. The future is orchestration with judgment."*(16:25~16:41)

→ [[orchestras-not-factories]](사람이 지휘자) · [[generator-evaluator-pattern]](adversarial checks — ⚠️ 구현 미발화)

## 이 위키와의 연결

### 이어지는 것

- **[[ai-slop]] — 코드 쪽의 정의.** 디자인 쪽(Taste Labs·Paul의 *"아무도 아무것도 결정하지 않았다"*)과 Khourshid의 *"unstructured delegation"* 에 이어, Martinez는 **"generation outruns judgment"** 로 정의하고 *"Slop is not AI-generated code"* 라고 명시한다. 새로 더하는 것은 **위험의 위치** — 나쁜 선택이 아니라 *선택이 있었다는 것을 엔지니어가 못 본 것*(01:01~01:14). 원인 쪽에 **조직 인센티브**(성과 불안, PR 수)를 놓은 것도 처음이다.
- **[[verification-bottleneck]]** — *"If AI produces more than humans can possibly evaluate, it has not accelerated the team, it has created a bottleneck."*(10:11~10:17) 그의 답은 이 페이지의 "답" 목록 중 **"일을 쪼갠다"·"리뷰 표면을 줄인다"** 쪽이다 — 리뷰를 자동화하는 쪽(전날 업로드된 [[tech-bridge-gitar-agentic-pr-validation|Gitar 편]]의 *"Of course, it's more AI"*)과 대조된다.
- **[[trusted-throughput]]** — *"lines of code is a garbage metric (…) the engineer who burns the most tokens must be producing the most"*(10:41~10:51). Hong의 "토큰은 LOC다"와 같은 논증을 **풍자**로 한다.
- **[[codebase-gardening]] · [[organic-architecture]]** — *"if the system is already a big ball of mud, the agent does not rescue you from the mud. It just builds the ball bigger, faster."*(03:48~03:54) Lauren Tan의 *"코드베이스는 에이전트의 기억"* 과 같은 기제.
- **[[hard-vs-soft-enforcement]] · [[tech-bridge-rails-harness-engineering]]** — Rails를 고르는 이유가 같다(관례가 결정 면을 줄인다). Quenneville은 그 관례를 **도구로 강제**(RuboCop·제너레이터·훅)하고, Martinez는 **관례 자체가 인지 오버헤드를 줄인다**(사람·에이전트 모두)는 쪽에서 말한다. 강제 메커니즘은 Martinez 발표에 없다.
- **[[deep-modules]]** — *"implementation details pushed to the leaves"*(12:51~12:53)는 Pocock·Ousterhout의 "복잡함을 단순한 인터페이스 뒤로"와 같은 방향의 리뷰 쪽 판본 → [[compressed-review-surface]].
- **[[risk-proportional-human-review]]** — 모든 줄을 읽을 필요는 없지만(*"That has never really been the standard."* 03:11~03:13) *"main flows, the boundaries, the data model, and product behaviors"*(03:21~03:25)는 이해해야 한다 — 리뷰 범위를 **위험이 아니라 층(구조 vs 구현)** 으로 가른다.

### 갈리는 것

> ⚠️ **Contradiction(약): 검증은 실행보다 싼가.** [[verification-cost-asymmetry]]는 *에이전트가 경제적으로 성립하는 작업은 검증이 실행보다 싼 작업*(Piras, NP형)이라고 정리한다. Martinez는 **일반 명제로** *"Generation is cheap, but evaluation is expensive."*(10:05~10:08)라고 말한다. 둘은 범위가 다르다 — Piras는 *작업을 고르라*(검증이 싼 것만 맡겨라), Martinez는 *현재 일어나는 일*(큰 PR·20페이지 문서는 검증이 비싸다)을 묘사한다. 다만 Martinez의 처방(작게 쪼개기, 압축된 리뷰 표면)은 **검증을 싸게 만드는 쪽으로 작업 모양을 바꾸라**는 것이라, 두 페이지는 "비대칭은 주어진 것인가, 만드는 것인가"로 이어 읽어야 한다.

> ⚠️ **긴장: "Ralph loop는 그냥 while 루프".** [[ralph-wiggum-method]]·[[harness-engineering]]은 Ralph loop를 하네스의 기본 단위로 다룬다. Martinez는 기법 자체보다 **"새로운 돌파구"라는 포장을** 부정한다(*"made to sound like a novel agentic breakthrough"* 10:36~10:38) — 기법의 효과에 대한 반론은 아니다.

> **"더 많은 AI"가 답인가.** 전날(10-13) 업로드된 [[tech-bridge-gitar-agentic-pr-validation|Gitar 편]]의 *"So, what's the answer here? Of course, it's more AI."*(Gitar 03:27~03:31)와 달리 Martinez는 *"(not) because we think the answer is more agents"*(15:37~15:41, ⚠️ 판독)라고 한다. 다만 그도 자사 에이전트 도구(ORC)로 맺는다 — 차이는 "에이전트를 쓰느냐"가 아니라 **사람의 판단을 어디에 남기느냐**의 서술이다. 두 발표 모두 벤더 발표다.

## 해소하지 않고 표시만 한 것

- ORC가 실제로 하는 일(기능·인터페이스·adversarial checks의 구현), 사용자·효과. G2i가 무슨 회사인지.
- *"accountability metrics that can be made visible for each chunk of work product"*(05:06~05:11)의 구체적 지표.
- SQLite 제작자 인용의 원 트윗·작성자·원 발언 출처. Dijkstra 인용의 원 문헌. Rails doctrine 원문.
- *"since December 25th"*(01:56~01:58)의 의미(날짜 vs 2025년 12월).
- *"Not only because we think the answer is more agents"*(15:37~15:41)의 의도.
- 행사명·도시·녹화일. 슬라이드 내용(트윗·다이어그램 예시).

## 등장 개체

- 인물: [[gabriel-martinez|Gabriel Martinez]](신규 제안 — 자막에서 자기소개, 설명란과 일치) · SQLite 제작자(⚠️ 이름 미발화, 트윗 경유) · Edsger Dijkstra(화자 인용) — 페이지 없음 · [[dhh|DHH]](⚠️ 발화 없음 — Rails 연결로만)
- 조직: [[g2i|G2i]](신규 제안) · [[ai-engineer|AI Engineer]](⚠️ 설명란 링크만 — 추정)
- 제품·도구: ORC(⚠️ en-orig *"Ork"*, 표기는 챕터·설명란 — [[g2i]] 페이지에 합침 제안) · Ruby on Rails · Ruby · JavaScript · SQLite · Twitter — 페이지 없음
- 개념: [[compressed-review-surface]](신규 제안) · [[ai-slop]] · [[verification-bottleneck]] · [[verification-cost-asymmetry]] · [[trusted-throughput]] · [[ralph-wiggum-method]] · [[codebase-gardening]] · [[organic-architecture]] · [[technical-debt]] · [[legacy-code-modernization]] · [[deep-modules]] · [[hard-vs-soft-enforcement]] · [[framework-defined-agent-infrastructure]] · [[taste-vs-judgment]] · [[architecture-as-remaining-art]] · [[cognitive-debt]] · [[cognitive-offloading]] · [[decision-quality]] · [[named-human-accountability]] · [[code-is-the-product]] · [[slop-cannon]] · [[verifiable-goals]] · [[agent-state-machine]] · [[agent-attention-management]] · [[read-fluency-for-agent-output]] · [[risk-proportional-human-review]] · [[orchestras-not-factories]] · [[generator-evaluator-pattern]] · [[harness-engineering]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=utMfI1DXTOE> (16:48, `upload_date` 2026-10-14)
- raw: `01.raw/articles/2026-10-14_생성은 저렴하지만 검토는 비쌉니다 - 엉터리 AI 코드 배포를 멈추는 법.md`
- 설명란 링크: <https://orc.ai> · <https://www.g2i.ai> · <https://x.com/g2i_ai> · <https://ai.engineer> (⚠️ 열어 보지 않았다)
- 슬롭의 다른 정의: [[tech-bridge-taste-labs-measuring-slop]] · [[tech-bridge-goodbye-slop-state-machines]] · [[tech-bridge-conductor-orchestras-not-factories]]
- 같은 Rails, 다른 층: [[tech-bridge-rails-harness-engineering]]
- 하루 전(10-13 업로드)의 다른 답: [[tech-bridge-gitar-agentic-pr-validation]] · [[tech-bridge-sentry-stop-prompting-codify-linters]]
- [[tech-bridge]] · [[g2i]] · [[gabriel-martinez]]
