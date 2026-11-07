---
title: "바이브코딩을 멈추세요: AI 에이전트와 TDD로 코딩하는 EXACT"
type: video
source: https://www.youtube.com/watch?v=hRhjL6BsxTU
site: youtube.com
author:
  - "[[Tech Bridge]]"
duration: 17:04
published: 2026-11-06
created: 2026-11-07
description: "Emily Bache(이름은 설명란 · tags뿐)가 codecentric의 Marco Emrich · Ferdinand Ade를 인터뷰한 17:04 편집본에 짧은 한국어 해설을 더했다. 공식 챕터 14 · 영어 원본 오디오만. 예시 매핑, 테스트 목록, 레드 · 그린 · 리팩터, 실험실 결과, 서브에이전트, 예측형 TDD, 사람의 개입을 다룬다."
tags:
  - clippings/youtube
---

**Source URL**: https://www.youtube.com/watch?v=hRhjL6BsxTU
**Channel**: Tech Bridge · **Duration**: 17:04 · **Published**: 2026-11-06

> **게시일.** `upload_date` **`20261106`**(UTC), `timestamp` 1794002408(= 2026-11-06 22:00:08 UTC = **2026-11-07 07:00 KST**), `availability: public`. 파일명 · `published`는 관례대로 `upload_date`를 쓴다.
>
> **오디오 트랙과 자막 — 인용 규칙.** 오디오는 `English (US) original (default)`와 더빙 7개 언어(de · es · fr · hi · id · it · pt)이고 한국어 트랙이 없다. 수동 자막은 없다. `ko-orig`가 없고 ko는 `kind=asr&lang=en&tlang=ko` 기계 번역이다. **인용은 en-orig로만 한다.**
>
> ⭐ **한국어 해설이 `en`에만 보인다.** en-orig에 한국어 해설이 없고(한글 0줄) 무캡션 간격 11곳이 있다: 00:00~00:22 · 02:17~02:34 · 04:11~04:33 · 06:00~06:22 · 08:34~08:52 · 09:42~09:55 · 09:55~10:04 · 12:14~12:36 · 13:47~14:07 · 16:08~16:25 · 16:45~17:00. `en`은 그중 일부에 해설의 영역으로 보이는 문장을 담는다(아래 발췌). 두 트랙의 json3 파라미터는 같다(`kind=asr&lang=en`, `variant` 없음). `en`은 인용 근거로 쓰지 않고 존재만 기록한다. 카타 수치(`Claim Office` 27% → 94%, `Sphinx` 15% → 100%)는 화면 표를 보지 않아 미확정이다.
>
> **형식.** Emily Bache(설명란 · tags 근거, 발화에 이름 없음)의 인터뷰 편집본에 짧은 한국어 해설을 더했다. 인터뷰이는 Marco Emrich · Ferdinand Ade(설명란), codecentric(설명란 · `en` 해설). 원본 링크 · 녹화일 미상. 시점 단서는 Opus 5.5 언급이다.
>
> **ASR 판독.** *wipe coding* · *VIP coding* → vibe coding, *exampleg guided* → example-guided, *Daniel Turus North* → Daniel Terhorst-North(`en`), *Matt Wyn* → Matt Wynne(`en`), *Marco Emerick* · *Ferdinand Ara* → 설명란 Emrich · Ade(`en`은 `Ada`), *code carters* · *cutters* → code katas, *porest* → PR(`en` `pull request`), *cloud code* → Claude Code, *OPU 4.6* → Opus 4.6, *refure* · *refracture* → refactor, *RTD* → TDD, *eventtor storming* → event storming, *loss in the middle* → lost in the middle.
>
> ⚠️ **화면 자료.** 워크플로 그림과 데이터 표는 영상을 보지 않아 이 파일에 없다. 품질 · 비용 비교는 방향만 자막에 있다.

## 설명란

AI에게 코드를 맡겼더니, 돌아가긴 하는데 원하던 게 아니었던 적이 있나요? 바이브 코딩의 이런 문제를 풀기 위해 codecentric의 Marco Emrich와 Ferdinand Ade가 만든 EXACT 코딩을 Emily Bache와의 인터뷰 원음과 한국어 자막, 짧은 해설로 소개합니다.

예시 매핑으로 무엇을 만들지 먼저 정하고, 테스트 목록과 레드·그린·리팩터의 TDD 사이클로 AI 에이전트를 이끄는 방법을 다룹니다. 예시 매핑 실험에서 달라진 결과, 단순 TDD와 EXACT의 코드 품질·비용 비교, 서브 에이전트를 쓰는 이유, 예측형 TDD, 그리고 사람이 얼마나 개입해야 하는지와 TDD를 잘 몰라도 되는지까지 함께 살펴봅니다.

타임라인
0:00 도입: AI가 만든 코드, 정말 원하던 건가요?
0:22 예시 주도 개발이라는 관점
1:11 EXACT를 만든 이유: 바이브 코딩의 문제
2:34 EXACT 워크플로
3:21 예시 매핑은 사람을 위한 것
4:33 실험실과 예시 매핑 결과
6:21 현실의 모호함과 스펙 주도 개발
8:52 안쪽 루프: 품질과 비용 데이터
10:03 서브 에이전트 실험
12:35 예측형 TDD
14:07 사람은 얼마나 개입해야 할까
15:23 TDD를 잘 몰라도 될까
16:25 Emily Bache의 정리
16:46 마무리

#바이브코딩 #TDD #테스트주도개발 #AI에이전트 #EXACT #예시매핑 #ClaudeCode #AI코딩

> info.json `tags`: AI 에이전트 · AI 코딩 · Claude Code · EXACT · Emily Bache · Example Mapping · TDD · codecentric · vibe coding · 바이브 코딩 · 서브 에이전트 · 예시 매핑 · 테스트 주도 개발 · 테크브릿지

## 트랜스크립트 — en-orig (원음 영어 ASR — 인용 근거)

[00:22] Both Daniel Turus North and Matt Wyn
[00:26] have suggested that what we call
[00:27] testdriven development should be called
[00:30] exampleg guided development because that
[00:33] captures the essence of all of
[00:35] behavior-driven development, acceptance
[00:37] testdriven development, and
[00:38] specification by example. And it's a
[00:41] particularly good framing, I think, for
[00:42] working with agentic AI tools because
[00:45] often they seem to do better with
[00:46] concrete examples than only a
[00:48] theoretical description of what you
[00:50] want. examples are at the heart of the
[00:53] exact coding workflow from Marco Emerick
[00:56] and Ferdinand Ara and they have data to
[01:00] back up that choice. I'm going to be
[01:02] interviewing them about it in today's
[01:04] video and how you can get the benefits
[01:06] of test-driven development or example
[01:08] guided development with Agentic AI. We
[01:11] did some experiments mostly at
[01:14] conferences but also at client projects.
[01:16] And what we found out is that when wipe
[01:18] coding came around, we had this issues
[01:20] that mostly everybody have tried wipe
[01:22] coding and what you get is something
[01:24] that produces code but maybe not exactly
[01:27] what you want and also you have a lot of
[01:29] issues with code quality. So the ideas
[01:32] and concepts we used in the past, we
[01:34] learned to do this as humans using
[01:37] testdriven development, using
[01:38] refactoring still works and we use this
[01:41] as um a counterpoint to wipe coding to
[01:44] actually profit from the the benefits
[01:47] the LLMs give us but still end up with
[01:50] good quality. I mean of course it's a
[01:52] word play so we want to get exactly what
[01:54] we want, not what you get with VIP
[01:56] coding. All
[01:58] >> I think we've all experienced poor
[01:59] quality from LLMs with vibe coding and
[02:02] many of us have been looking for good
[02:04] solutions to get exactly what we want.
[02:07] Marco and Ferdie have been working on
[02:09] this over a period of several years now
[02:12] and they've been getting some great
[02:13] results. So we're going to look more
[02:15] closely at this exact workflow in a
[02:17] moment.
[02:34] before the interview. Marco and Ferdie
[02:37] shared a picture of the exact workflow
[02:39] with me. So, it starts with example
[02:41] mapping. That's a technique from Matt
[02:44] Wyn of BDD fame for collaborating with
[02:46] stakeholders to map out a user story.
[02:49] And then you can work with the LLM to
[02:51] turn that into a test list. Now that's
[02:54] an idea from Kent Beck's Canon TDD where
[02:57] you keep track of the whole problem that
[02:59] you need to solve in a natural language
[03:01] list of ideas for test cases. And then
[03:05] you use this list in the inner TDD loop,
[03:08] one item from the list at a time, going
[03:10] through red, green, refactor, building
[03:12] up a working implementation. I asked
[03:15] Marco and Ferdie to explain each step of
[03:17] this exact workflow beginning with that
[03:20] example mapping.
[03:22] >> In this example, we used example mapping
[03:24] as a collaborative modeling technique
[03:26] which basically is is made for humans,
[03:28] right? It's really engaging. It's
[03:30] motivating. You have to think hard about
[03:32] what you're building and so it builds up
[03:33] the mental model really quickly we
[03:35] think. And then also we can see in the
[03:37] testless step there's this kind of
[03:40] there's this two icons. One is a human
[03:41] and one is kind of this technical brain
[03:43] which is showing the LLM basically. And
[03:46] so this also means that here we are
[03:48] collaborating. So for example in our
[03:50] exact coding harness the LLM is checking
[03:52] if we are missing any obvious
[03:55] permutations if you're missing any
[03:56] obvious examples in our suite. I really
[04:00] like this emphasis on collaboration with
[04:02] other human beings so that we build a
[04:04] shared understanding and then use the
[04:06] strengths of the LLM to improve that and
[04:09] turn it into an actionable list of test
[04:11] cases.
[04:33] Another thing that impresses me about
[04:35] Marco and Ferd's approach that it is
[04:38] empirical. It's driven by experiments
[04:41] with different LLMs and different
[04:43] programming languages and harnesses.
[04:45] They've developed a whole test lab to
[04:47] try out different approaches and see
[04:49] what works. And they've also invented a
[04:52] couple of new code carters. Love it. new
[04:54] code carters which of course aren't
[04:56] previously in the training data for the
[04:58] LLM. So they've got these problem
[05:00] descriptions which they can give the LLM
[05:02] to solve and a complete test suite of
[05:05] acceptance tests which they don't show
[05:07] the LLM that they can use to assess how
[05:10] well it implemented these novel
[05:12] requirements that it hasn't seen before.
[05:14] I asked Marco and Ferdie to show some of
[05:16] their results. Would you talk me through
[05:19] what these numbers mean? The first one
[05:21] is basically looking at the the level of
[05:24] the example mappings. We tried to
[05:27] describe the cutters basically just the
[05:30] rules the acceptance criteria in pros
[05:32] and run it through the LLM. So this is
[05:34] basically wipe coding and then we did
[05:36] the same thing but did example mapping
[05:39] before that. So we gave the LMM clear
[05:41] examples what we want to achieve in the
[05:43] cutter and you can see that the
[05:45] correctness increases by 60 70% 80% even
[05:50] in some cases
[05:52] >> these data are actually really clear
[05:54] compared with just giving it a problem
[05:55] description in pros the LM builds
[05:58] something much closer to what you want
[06:00] when you do example mapping Best.
[06:22] But is that realistic? Wouldn't it be
[06:23] better to work on giving the LLM a
[06:25] better description of the problem in the
[06:27] first place? Well, Ferdie explained that
[06:29] this test is actually pretty similar to
[06:31] the situation he faces in his normal
[06:34] work.
[06:34] >> I see a lot of success stories from
[06:36] parts of the software world where for
[06:39] example the team at cloud code, they're
[06:41] basically building a tool themselves for
[06:43] themselves. They so they're the users
[06:45] and the stakeholders and everything,
[06:47] right? But in our daily business, we
[06:49] usually are I don't know insuranceances,
[06:51] banks, e-commerce companies, whatever.
[06:54] And usually we come in and we are not
[06:55] the experts, right? And so there is
[06:57] always a lot of ambiguity in the
[06:59] requirements.
[07:00] >> Ambiguity and pros. Yeah, we've talked
[07:04] before on this channel about the value
[07:06] of acceptance tests so you specify
[07:08] clearly what to build. Example mapping
[07:11] is a complimentary approach. I asked
[07:13] Ferdie to compare that with other
[07:15] augmented coding approaches like
[07:17] specdriven development. before we had
[07:20] the phase of a vibe coding and then
[07:21] later on all these specdriven
[07:23] development frameworks pop up on on
[07:25] GitHub with like lots of stars and
[07:27] everything. These frameworks for example
[07:29] BMAD or others they have these different
[07:31] phases and in in each phase they make a
[07:34] a big picture plan or they make a kind
[07:37] of a more architecture plan or whatever
[07:39] after the second or third wave um and it
[07:42] it becomes more and more lines of
[07:44] markdown. But we think that um this does
[07:47] not really improve the UX of the the
[07:51] people that are building the stuff a
[07:52] lot. You kind of have the same looks
[07:55] good to me feeling you have you always
[07:58] had with a really big um porest. And so
[08:01] we thought we have to basically
[08:04] frontload or shift left some of the
[08:06] thinking and we thought that uh example
[08:09] mapping is a great tool for that. We
[08:11] also like stuff from the DDD world like
[08:14] eventtor storming on domain
[08:15] storytelling.
[08:16] >> So this first part of the exact workflow
[08:18] is all about human understanding,
[08:20] collaboration and not too much in the
[08:22] way of markdown files. It's more about
[08:24] examples, sticky notes, conversations,
[08:27] ideas from domain driven design and
[08:28] behavior-driven development. But let's
[08:30] turn now to the inner loop and how we're
[08:32] getting the LLM to do the detailed steps
[08:34] of TDD.
[08:52] Marco showed me this data about another
[08:54] one of their experiments. It shows a
[08:57] comparison of plain TDD with exact
[09:00] coding and a third variant which we'll
[09:02] come to in a moment. Plain TDD means
[09:05] just telling the LM to do TDD with very
[09:08] little explanation. Now, it shows in
[09:10] this table that is much cheaper in token
[09:12] cost, but the exact coding workflow does
[09:15] better in other areas. Longest function,
[09:18] that's perhaps obvious what it means.
[09:19] Lower is better, but I'll need to
[09:21] explain the others. Cognitive max is a
[09:24] static analysis measurement of code
[09:25] complexity. Lower is better. And
[09:28] mutation score is how good the tests are
[09:30] at finding bugs. Higher is better. So
[09:33] what we see here is that the code
[09:34] written using the exact workflow is much
[09:37] higher code quality, much better unit
[09:39] tests, although at a higher cost in
[09:42] tokens.
[09:55] Those
[10:04] are results from a rather recent
[10:06] experiment, but Marco and Ferdie started
[10:08] doing these experiments like way back.
[10:10] Ferdy told me about the first iteration
[10:12] of their approach and how this testing
[10:14] lab came about.
[10:16] >> Yeah, I mean we we we basically started
[10:18] out with one command back then. There
[10:21] were no skills back then. We were
[10:23] started out with one command TDD
[10:25] command. And then I read more and more
[10:28] about how LLMs work and how like context
[10:30] engineering works. And so then I
[10:33] basically asked like hey Marco shouldn't
[10:35] we actually have kind of sub agents
[10:38] because there I mean there's this famous
[10:40] uh loss in the middle paper right which
[10:42] basically says the longer the context
[10:44] gets the more gets lost in the middle of
[10:47] the context. So I thought okay it would
[10:49] make sense basically because you have
[10:51] these clear steps in TDD it would make
[10:54] sense to have each phase in a single sub
[10:56] agent with a fresh context right and and
[10:59] this is basically how how Marco said
[11:01] okay at at one like I think Sunday
[11:03] evening he said okay I'm I'm I'm going
[11:06] to research this quickly and so this
[11:08] whole framework research framework came
[11:10] came to life then and basically to
[11:12] answer the question would it actually be
[11:13] better to have separate sub agents with
[11:16] separate context for each
[11:18] a Sunday evening project that turned
[11:20] into an entire test lab for a gentic
[11:23] harnesses. I'm sure you've all had
[11:25] projects that got out of hand like that.
[11:27] Anyway, this is where that third line in
[11:29] this data table comes in. Marco and
[11:31] Ferdie have done lots of experiments and
[11:34] for this case for Opus 5.5 and Claude
[11:37] Code, they're getting better results
[11:39] with two agents. The main agent doing
[11:41] most of the TDD workflow and a separate
[11:44] sub agent for the refactoring step. And
[11:47] this gets them measurably better code
[11:49] quality although actually not by much.
[11:51] They said that the difference used to be
[11:53] bigger on previous models. So when we
[11:55] started with this approach it was OPU
[11:58] 4.6 and with OPU 4.6 the spread was much
[12:01] larger even. So with OPU 4.6 the
[12:04] dedicated refactoring agent brought a
[12:06] lot of additional value. Nowadays the
[12:09] additional value from the refactoring
[12:10] agent is not so strong but the
[12:12] additional value from having a dedicated
[12:14] TDD approach is still visible.
[12:36] Another detail of the specifics of how
[12:39] they ensure good code quality in the
[12:41] exact workflow is to ask the LLM to do
[12:44] predictive TDD. Now, this is an idea
[12:47] popularized by Ted M. Young and his TDD
[12:49] game and you may have seen it in the
[12:51] training tool cyber dojo. Marco and
[12:53] Ferdie explained what predictive TDD is
[12:56] and why that helps.
[12:58] >> The important point is that before you
[13:01] do any TDD step, you have to predict
[13:04] what the result would be. So if I do a
[13:07] red step, I first have to say this test
[13:09] will be red and for what reason will it
[13:11] be failing? What is the error message
[13:13] that I want to get? So this is something
[13:15] we did even before LLMs because it helps
[13:18] us as humans to confirm that we still
[13:22] are in touch with reality that we still
[13:24] understand what's actually going on in
[13:25] the code and in the environment and now
[13:28] this helps the LLM to check if it is
[13:30] still in alignment with reality. we
[13:32] would need to bring a um LLM researcher
[13:35] here but we think that this works
[13:37] because basically the prediction brings
[13:40] the problem to the front of the context
[13:42] for the LLM in a sense right so we think
[13:45] that's that's why it makes a difference
[13:47] in our data
[14:07] Now, this all sounds like a pretty
[14:09] sophisticated TDD process, and I wanted
[14:12] to know how much supervision the agent
[14:14] actually needs to succeed. Do you still
[14:16] need a human in the loop?
[14:18] >> Actually, I think there is no clear
[14:20] answer to this question right now. And
[14:22] um it it shifts all the time also. So
[14:26] what we built into our harness is that
[14:28] you actually get the choice to select
[14:30] the autonomy level that you want to
[14:33] have. So you could decide to go into
[14:35] every step, look after every red, after
[14:37] every green after every refure, maybe
[14:40] only after the refracture, maybe only
[14:41] after three tests. Or you want to run it
[14:44] completely autonomously. This is also a
[14:46] possibility. So I think at least you
[14:48] need to decide as a human how much human
[14:51] the loop you want to have. Me personally
[14:54] I found that the more I actually look
[14:57] after it, stay in the loop, understand
[15:00] what the LLM is doing and make course
[15:03] corrections, the better the result
[15:04] actually is. For a lot of these
[15:06] problems, the human loop is still really
[15:08] important because we first have to kind
[15:11] of build a mental model, parse all the
[15:13] information. We have to kind of get our
[15:15] mental model clear of what we actually
[15:17] kind of need, what the world looks like,
[15:19] and then we can build something there.
[15:21] The human in the loop is is still really
[15:23] important.
[15:24] >> What I'm hearing is that it still takes
[15:26] quite a bit of human skill to get the
[15:28] best results. So, I asked Marco and Fie,
[15:30] how easy would it be for somebody with
[15:32] little experience of TDD to pick up
[15:35] these agentic skills and be successful?
[15:37] Like Marco often says, he tried teaching
[15:39] TDD for 20 years and now finally uh
[15:42] something listens [laughter] is a joke
[15:45] of course, but I I do think that one of
[15:48] the hard things always has been the the
[15:51] thinking and the the learning aspect of
[15:53] TDD. I think you could start without
[15:55] having full TDD knowledge and get deeper
[15:58] understanding your more you use it.
[16:00] Having a deeper RTD knowledge of course
[16:02] would also help because then you could
[16:04] improve the harness, feed your own
[16:06] knowledge into it, but it's not so hard
[16:08] to get started.
[16:25] Today we've heard from Marco and Ferdy
[16:27] about their approach to firstly get an
[16:30] LLM coding agent to build the right
[16:32] thing with example mapping or another
[16:35] kind of collaborative modeling and to
[16:37] build the thing right with predictive
[16:40] test-driven development and perhaps
[16:42] separate refactoring sub aents depending
[16:45] on the model you've got. Fore
[17:00] speech.

## 발췌 — en (해설 추정 구간만 — 인용하지 않음)

[00:00] Have you ever commissioned
[00:02] an AI to write code, and although it works, it's not what
[00:03] you wanted?
[00:05] In this video, we present "Exact Coding
[00:07] ", created by Marco and Ferdi from
[00:08] CodeCentric.   It's about
[00:10] first deciding what to
[00:11] build through examples and guiding the
[00:13] AI ​​with test-driven development.
[00:16] We will look at experimental data, subagents
[00:18] , predictive TDD, and how much
[00:20] human intervention is necessary.
[04:12] Example mapping is a method for
[04:13] organizing stories using
[04:14] colored cards.
[04:15] On the yellow cards we write
[04:17] user stories, on the blue ones
[04:19] rules, on the green ones concrete examples,
[04:21] and on the red ones unanswered questions
[04:22] .
[04:23] Red is the step of writing a test
[04:25] that fails, green is writing the code
[04:27] just to pass it, and refactoring is
[04:29] improving the structure while maintaining
[04:32] functionality.
[06:02] When viewing the table on screen, in the
[06:04] "Claim Office" task, the accuracy was
[06:06] 27% when only text was used for explanation.  By
[06:09] first performing the mapping of examples, it
[06:10] reached 94%.
[06:12] Sphinx's score rose from 15% to
[06:14] 100%.
[06:15] These are the results of running the
[06:17] Opus 5 model six times per cell.  Here, "
[06:19] code kata" refers to
[06:20] coding exercises for practice.
[16:15] 's also available as
[16:16] open source, and they say they're writing a
[16:17] book about it.
[16:18] In this article, the two divide
[16:20] autonomy into three levels.  They are: delegating
[16:21] until the end, pausing at each cycle,
[16:23] and pausing at each step.
[16:46] In summary, instead of letting AI
[16:48] work by intuition, it is better to define
[16:50] what to create with examples and guide it step by
[16:52] step with tests.
[16:54] What method do you use when
[16:56] programming with AI?
[16:57] If you found the video helpful, please
[16:59] subscribe and like it.
[17:00] Thank you for watching.  See you in the
[17:02] next video.

## 트랜스크립트 — ko (`tlang=ko` 기계 번역 — 참고용, 인용하지 않음)

[00:00] 혹시 코드 작성을 의뢰해 보신 적 있으신가요?
[00:02] 인공지능이긴 하지만, 작동은 하더라도 원하는 것은 아닙니다.
[00:03] 원하셨나요?
[00:05] 이 영상에서는 "정확한 코딩"을 소개합니다.
[00:07] ", 마르코와 페르디가 만들었습니다
[00:08] 코드 중심적인.
[00:10] 먼저 무엇을 결정해야 할지 정하는 문제입니다.
[00:11] 예시를 통해 구축하고 안내합니다.
[00:13] 테스트 주도 개발 방식의 AI.
[00:16] 우리는 실험 데이터와 하위 작용제를 살펴볼 것입니다.
[00:18] 예측 TDD와 그 규모는 어느 정도여야 할까요?
[00:20] 인간의 개입.
[00:23] 다니엘 테르호스트-노스와 맷 모두
[00:27] 윈은 TDD를 "라고 부르자"고 제안했습니다.
[00:30] "사례 중심 개발"이란, 왜냐하면
[00:33] 이는 BDD, ATDD 및 그 핵심을 포착합니다.
[00:36] 예시를 통한 설명.
[00:40] 훌륭한 업무 방식입니다.
[00:43] 인공지능을 사용하면 성능이 더 좋아지는 경향이 있기 때문입니다.
[00:46] 구체적인 예를 들어
[00:48] 이론적 설명.
[00:51] 예시는 흐름의 핵심입니다.
[00:53] 마르코 엠리히의 작품 "정확한 코딩"과
[00:56] 페르디난드 아다.
[00:58] 그리고 그들은 그것을 뒷받침할 데이터를 가지고 있습니다.
[01:00] 선택.
[01:02] 오늘 저는 그들을 인터뷰하여 어떻게 하는지 알아낼 것입니다.
[01:05] 개발의 혜택을 누리기 위해
[01:08] AI를 활용한 예시를 통해 안내합니다.
[01:11] 우리는 몇 가지 실험을 했습니다.
[01:12] 주로 컨퍼런스에서 그렇지만,
[01:14] 고객 프로젝트에서도 마찬가지입니다.
[01:16] 우리는 "바이브 코딩"을 통해 다음과 같은 사실을 발견했습니다.
[01:19] 모두가 그렇게 프로그래밍하려고 하지만,
[01:22] 그 결과는 대개 다음과 같은 코드가 됩니다.
[01:25] 바로 당신이 찾던 것입니다.
[01:27] 게다가, 이로 인해 많은 문제가 발생합니다.
[01:29] 코드 품질.
[01:31] 우리가 과거에 사용했던 아이디어는 다음과 같습니다.
[01:34] 인간, 예를 들어 개발에 의해 주도되는 것
[01:36] 테스트 및 리팩토링이 계속 진행 중입니다.
[01:39] 일하고 있는.
[01:40] 우리는 이것을 "분위기"에 대한 반대 개념으로 사용합니다.
[01:44] "코딩"을 활용하여 이점을 얻으세요
[01:47] LLMs는 양호한 품질을 유지하고 있습니다.
[01:51] 이건 말장난이에요: 우리는 원해요
[01:52] 우리가 원하는 것을 정확히 얻기 ​​위해서가 아니라,
[01:55] 이는 "바이브 코딩"의 결과입니다. 그래서
[01:57] 저것...
[01:58] 우리 모두 안 좋은 경험을 해본 적이 있을 거라고 생각해요.
[02:00] LLM 및 "바이브 코딩" 경험
[02:03] 공정한 결과를 얻기 위한 해결책 모색
[02:06] 우리가 필요한 것. 마르코와 페르디는 가지고 있다
[02:08] 그들은 이 일을 수년간 해왔고,
[02:11] 탁월한 결과를 얻었습니다.
[02:14] 우리는 이 워크플로우를 분석할 것입니다.
[02:15] 잠시 후 더 자세히 설명드리겠습니다.
[02:34] 인터뷰에 앞서 마르코와 페르디는
[02:36] 그들은 나에게 그 사진을 보여주었다.
[02:38] 워크플로우. 모든 것은 ~에서 시작됩니다
[02:41] 예시 매핑. 이것은 하나의 기술입니다.
[02:43] BDD로 유명한 맷 윈은
[02:45] 이해관계자들과 협력하고
[02:47] 사용자 스토리를 정의하세요.
[02:49] 그런 다음 LLM 과정을 통해 다음과 같은 작업을 수행할 수 있습니다.
[02:51] 그것을 테스트 목록으로 바꾸세요.
[02:55] 그건 켄트의 정규 TDD에서 나온 아이디어입니다.
[02:57] Beck, 모든 것을 기록하는 곳
[02:58] 해결해야 할 문제는 목록에 있습니다.
[03:00] 언어 테스트 케이스에 대한 아이디어
[03:02] 자연스러운.
[03:04] 그런 다음 이 리스트를 반복문 안에서 사용합니다.
[03:06] TDD의 내부 개념으로, 한 번에 한 요소씩 진행합니다.
[03:08] 빨간색, 초록색을 통과하며
[03:10] 리팩토링, 빌드
[03:12] 기능적 구현.
[03:14] 나는 마르코와 페르디에게 설명해달라고 부탁했다.
[03:17] 이 워크플로의 각 단계
[03:18] 맞습니다, 그 매핑부터 시작해서요.
[03:20] 예시.
[03:21] 이 예제에서는 매핑을 사용합니다.
[03:23] 모델링 기법과 같은 예
[03:25] 협업으로 만들어진, 기본적으로
[03:27] 인간에게 해당되는 말이죠? 정말 그래요
[03:29] 매력적이고 동기 부여가 된다. 생각해야 해요
[03:31] 당신이 만들고 있는 것에는 많은 부분이 포함됩니다. 왜냐하면
[03:33] 정신적 모델을 구축하는 것은 무엇일까요?
[03:34] 우리는 그 속도가 빠를 것이라고 믿습니다.
[03:36] 그리고 우리는 또한 본문에서 볼 수 있듯이
[03:38] 테스트 목록에는 두 가지 유형이 있습니다.
[03:40] 아이콘.
[03:41] 하나는 인간이고 다른 하나는...
[03:42] 일종의 기술적인 두뇌를 보여주는
[03:44] 기본적으로 법학 석사(LLM) 과정과 같습니다.
[03:46] 그리고 이것은 또한 여기를 의미합니다.
[03:47] 우리는 협력하고 있습니다. 예를 들어, 에서
[03:49] 우리의 정밀한 코딩 도구,
[03:52] LLM은 누락된 항목이 있는지 확인합니다.
[03:54] 만약 우리가 놓치고 있다면 명백한 순열입니다.
[03:56] 저희 제품군에서 명백한 예시를 찾아보실 수 있습니다.
[03:59] 저는 이런 점을 강조하는 게 정말 마음에 들어요.
[04:01] 다른 사람들과의 협력
[04:03] 우리가 함께 무언가를 만들어낼 수 있도록 말이죠.
[04:12] 예시 매핑은 다음과 같은 방법입니다.
[04:13] 카드를 사용하여 이야기를 구성하세요
[04:14] 그림 물감.
[04:15] 옐로우 카드에는 다음과 같이 적습니다.
[04:17] 파란색으로 표시된 부분이 사용자 스토리입니다.
[04:19] 녹색 콘크리트 사례에서 규칙
[04:21] 그리고 빨간색으로 표시된 부분에는 질문이 없습니다.
[04:22] 답변.
[04:23] 빨간색은 시험 작성 단계를 나타냅니다.
[04:25] 실패하는 것은 녹색이 코드를 작성하는 것입니다.
[04:27] 통과하기만 하면 되고, 리팩토링은...
[04:29] 구조를 개선하면서 기존 구조를 유지합니다.
[04:32] 기능.
[06:02] 화면에 표시된 표를 볼 때, 작업에서
[06:04] "청구 사무소"에서 확인한 정확도는 다음과 같습니다.
[06:06] 텍스트로만 설명했을 때는 27%였습니다. ~에게
[06:09] 먼저 예제 매핑을 수행합니다.
[06:10] 94%에 달했습니다.
[06:12] 스핑크스의 점수는 15%에서 상승했습니다.
[06:14] 100%.
[06:15] 이는 모델 실행 결과입니다.
[06:17] Opus 5가 한 박스에 6개씩 들어 있습니다. 여기, "
[06:19] "코드 카타"는 연습 문제를 의미합니다.
[06:20] 코딩 연습.
[06:22] ?
[06:22] 하지만 그것이 현실적일까요? 그게 더 낫지 않을까요?
[06:24] LLM 과정을 더 좋게 만들기 위해 노력합니다
[06:25] 문제 설명
[06:27] 원칙? 페르디는 이렇게 설명했습니다.
[06:29] 이 테스트는 실제로는 상당히 유사합니다.
[06:31] 그가 직장에서 직면한 상황
[06:33] 보통.
[06:35] 저는 여러 분야에서 많은 성공 사례를 봅니다.
[06:37] 소프트웨어 세계에서는, 왜냐하면
[06:39] 예를 들어, 클라우드 코드 팀
[06:41] 그들을 위한 도구를 만들어라
[06:43] 같은.
[06:44] 그러니까 그들이 바로 사용자들이죠.
[06:46] 이해 관계자 등등, 그렇죠?
[06:47] 하지만 우리의 일상적인 업무에서는,
[06:49] 저희는 주로 보험 회사에 근무합니다.
[06:51] 은행, 전자상거래 회사
[06:53] , 무엇이든. 그리고 우리는 보통 도착해서
[06:55] 우리는 전문가가 아니잖아요? 그리고 ~을 위해
[06:57] 그 부분에는 항상 많은 모호함이 존재합니다.
[06:59] 요구 사항.
[07:00] 모호함과 산문.
[07:02] 응.
[07:03] 이 채널에서 이미 이 주제에 대해 이야기했습니다.
[07:05] 인수 테스트의 가치
[07:08] 무엇을 만들 것인지 명확하게 명시하십시오. 그
[07:10] "예제 매핑"은 하나의 접근 방식입니다.
[07:11] 상호 보완적입니다. 나는 페르디에게 부탁했다.
[07:14] 다른 접근 방식과 비교하기
[07:15] 증강 인코딩과 같은 것
[07:16] 명세 기반 개발.
[07:19] 이전에는 "바이브 코딩" 단계를 거쳤습니다.
[07:21] 그러자 이러한 모든 프레임워크들이 등장했습니다.
[07:23] 개발은 다음을 기반으로 합니다.
[07:24] GitHub에 있는 많은 사양
[07:26] 별과 관련된 모든 것들 말이죠.
[07:28] 예를 들어 B-Mad 또는 이러한 프레임워크
[07:31] 다른 것들은 여러 단계를 거치며 각 단계마다 차이가 있습니다.
[07:34] 그들은 전반적인 계획, 즉 계획을 세웁니다.
[07:36] 건축이든 뭐든 간에.
[07:39] 우리는 2차 또는 3차 유행의 한가운데에 있습니다.
[07:41] 점점 더 많은 줄이 늘어납니다.
[07:44] 가격 인하. 하지만 우리는 이것이 아니라고 생각합니다.
[07:47] 이는 사용자 경험을 크게 향상시킵니다.
[07:49] 이것들을 만드는 사람들의 사용자
[07:52] 것들.
[07:54] "내 생각엔"이라는 느낌과 똑같네요.
[07:56] "좋았어요" 항상 당겨서 사용할 수 있었잖아요
[07:58] 정말 큰 요청입니다.
[08:01] 그래서 우리는 그렇게 해야 한다고 생각했습니다.
[08:03] 일부를 예상하거나 앞당기다
[08:05] 반사.
[08:07] 그리고 우리는 "예제 매핑"이
[08:09] 그 목적에 아주 적합한 도구입니다. 또한
[08:11] 저희는 DDD(도메인 주도 개발) 관련 자료를 좋아합니다.
[08:13] "이벤트 스토밍" 및 "도메인"과 같은 것들
[08:15] 스토리텔링.
[08:16] 워크플로의 첫 번째 부분입니다.
[08:18] 이것은 인간에 대한 이해에 관한 것입니다.
[08:21] 파일 자체보다는 협업에 중점을 둡니다.
[08:22] 가격 인하. 예시를 드는 게 더 중요해요.
[08:24] 포스트잇, 대화, 그리고 아이디어
[08:25] 도메인 중심 설계 및
[08:27] 행동 중심 개발
[08:28] . 자, 이제 내부 루프로 넘어가 보겠습니다.
[08:32] LLM이 어떻게 일을 하도록 하는가
[08:35] 상세한 TDD 단계.
[10:04] 이것들은 실험 결과입니다.
[10:06] 비교적 최근이지만 마르코와 페르디
[10:08] 그들은 이러한 실험을 수행하기 시작했다.
[10:10] 꽤 오래 전에요. 페르디가 내게 그것에 대해 말해줬다
[10:12] 그들의 접근 방식의 첫 번째 시도와 그 방법
[10:13] 이 시험 연구소가 등장했습니다.
[10:16] 네, 그러니까 기본적으로 저희는 시작했어요.
[10:18] 당시 명령어로 사용되던 것이었습니다. 있었다
[10:21] 그렇다면 기술에 대해 이야기해 볼까요? 먼저 다음과 같은 것부터 시작합니다.
[10:24] 명령어, TDD 명령어, 그리고 나서 더 읽어봤습니다.
[10:27] LLM 과정이 어떻게 운영되는지에 대하여
[10:29] 컨텍스트 엔지니어링.
[10:32] 그래서 저는 마르코에게 기본적으로 물어봤습니다.
[10:34] 하위 요원을 두어야 하지 않을까요?
[10:36] 그 유명한 기사를 고려해 볼 때
[10:39] 매체에서의 정보 손실?
[10:42] 이는 기본적으로 더 많을수록 더 좋다는 것을 의미합니다.
[10:44] 맥락이 길어질수록 의미가 퇴색될 가능성이 커진다.
[10:47] 그것의 한가운데. 그래서 저는 그렇게 생각했습니다.
[10:49] 그럴 만도 하죠, 왜냐하면 이런 것들이 있으니까요.
[10:51] TDD의 명확한 단계. 그렇게 하면 말이 되겠네요.
[10:54] 각 단계를 고유한 하위 에이전트로 구성합니다.
[10:56] 새로운 맥락에서 말이죠, 그렇죠?
[10:59] 그게 그가 말한 요점이에요.
[11:01] 마르코, 좋아, 예를 들어 일요일에...
[11:03] 그는 나중에 "알았어, 갈게"라고 말했다.
[11:04] 이 문제를 신속하게 조사하십시오.
[11:07] 그리고 이것이 바로 이 전체 체계가 만들어진 방식입니다.
[11:08] 이 연구 프레임워크는 다음과 같습니다.
[11:10] 생명을 얻었다.
[11:11] 그리고 기본적으로 답변하자면,
[11:13] 문제는, 정말로 갖는 것이 더 나을 것인가 하는 점입니다.
[11:14] 컨텍스트를 가진 하위 에이전트를 분리합니다.
[11:16] 각 단계마다 따로따로 하시나요?
[11:18] ?
[11:18] 일요일 오후에 할 만한 프로젝트
[11:20] 그곳은 말 그대로 실험실이 되었다.
[11:22] 유전자 조작을 위한 검사?
[11:24] 누구나 한 번쯤은 겪어봤을 거라고 확신해요.
[11:25] 통제 불능 상태가 된 프로젝트들
[11:26] 그래서. 어쨌든, 여기가 바로 그곳입니다.
[11:28] 이 데이터 표의 세 번째 줄입니다.
[11:31] 마르코와 페르디는 많은 일을 해냈습니다.
[11:32] 실험.
[11:34] 그리고 이 경우에는 작품번호 5.5와 클로드에 해당합니다.
[11:36] 코드 실력이 점점 나아지고 있어요.
[11:38] 두 가지 에이전트를 사용한 결과입니다. 에이전트
[11:41] 대부분의 기능을 수행하는 주요 기능
[11:43] TDD 워크플로 및 하위 에이전트
[11:44] 리팩토링 단계를 별도로 진행합니다.
[11:46] . 그리고 이것이 그들에게 코드의 품질을 제공합니다.
[11:48] 눈에 띄게 좋아졌습니다. 하지만 실제로는
[11:50] 오래가진 않을 거예요. 그들은 차이점을 말했다.
[11:52] 이전 모델에서는 더 컸습니다.
[11:55] 그래서 우리가 이것을 시작했을 때
[11:57] 포커스는 Opus 4.0, 4.6과 함께였습니다.
[11:59] 작품 4.6의 차이는 훨씬 더 컸습니다.
[12:01] 연세가 드신. 따라서 Opus 4.6에서는 에이전트가
[12:04] 전담 리팩토링 기여
[12:06] 상당한 부가가치. 오늘날,
[12:09] 에이전트의 추가 가치
[12:10] 리팩토링은 그다지 강력한 기능은 아니지만,
[12:12] 접근 방식을 갖는 것의 부가가치
[12:14] 전담 TDD
[12:37] 방법의 세부 사항에 대한 또 다른 내용은 다음과 같습니다.
[12:39] 그들은 좋은 코드 품질을 보장합니다.
[12:41] 정확한 절차는 다음과 같습니다.
[12:43] 예측 기반 TDD를 수행하는 LLM.
[12:46] 자, 이것은 대중화된 아이디어입니다.
[12:47] TDD 게임에서 테드 M 영은 할 수 있습니다.
[12:49] 그들이 그것을 도구에서 보았다는 것
[12:51] 사이버 도장 훈련. 마르코와 페르디
[12:53] 그들은 예측 TDD가 무엇인지 설명했습니다.
[12:56] 왜 도움이 될까요?
[12:58] 중요한 점은 이전에는
[13:00] TDD 단계를 수행하려면 다음 사항을 준수해야 합니다.
[13:03] 결과가 어떻게 될지 예측하다.
[13:06] 그러니까 제가 빨간색 옷을 입고 한 발짝 내딛는다면, 먼저
[13:08] 이 시험은 다음과 같을 것이라고 말씀드려야겠습니다.
[13:10] 빨간색으로 표시된 이유는 무엇이며, 왜 실패할까요?
[13:12] 어떤 오류 메시지가 표시될 것으로 예상되나요?
[13:14] 얻다? 그래서 이것은 ~입니다
[13:16] 저희는 법학 석사 과정 이전부터 그 일을 해왔습니다.
[13:18] 왜냐하면 그것은 우리 인간에게 도움이 되기 때문입니다
[13:19] 우리가 여전히 연결되어 있는지 확인해 주세요.
[13:22] 우리가 여전히 이해하고 있는 현실은 바로 이것입니다.
[13:24] 코드에서 실제로 일어나는 일과
[13:26] 약. 그리고 이제 이것은 LLM에 도움이 됩니다.
[13:29] 여전히 제대로 조율되어 있는지 확인하세요
[13:31] 현실.
[13:32] 우리는 연구원을 영입해야 할 것입니다.
[13:35] LLM 출신이지만, 우리는 이것을 믿습니다.
[13:37] 기본적으로 효과가 있는 이유는 다음과 같습니다.
[13:39] 예측은 문제를 전면에 내세웁니다.
[13:42] LLM 과정의 맥락에서 말씀하시는 거죠? 그래서
[13:45] 우리는 이것이 바로 그것이 중요한 이유라고 생각합니다.
[13:47] 우리 데이터의 차이점입니다.
[14:07] 이 모든 게 TDD(테스트 주도 개발) 프로세스처럼 들리네요.
[14:09] 상당히 정교해서 알고 싶었어요.
[14:11] 그에게 실제로 필요한 감독의 정도는 어느 정도일까요?
[14:14] 에이전트가 성공할 것입니다.
[14:16] 인간이 여전히 필요한가요?
[14:17] 프로세스?
[14:18] 사실, 저는 그런 게 없다고 생각해요.
[14:20] 이 질문에 대한 명확한 답변을 지금 바로 알려드립니다.
[14:22] 그것은 똑같으면서도 끊임없이 변합니다.
[14:26] 우리가 환경에 포함시키는 것은 다음과 같습니다.
[14:28] 자율성 수준을 선택할 수 있다는 점
[14:31] 당신이 갖고 싶어하는 것.
[14:33] 각 단계를 검토하기로 결정할 수도 있습니다.
[14:35] 모든 실패, 모든 성공, 모든 것을 관찰하라
[14:37] 리팩토링은 아마도 그 후에나 가능할 것이다.
[14:40] 리팩토링은 세 번의 테스트 후에만 진행하거나,
[14:42] 완전히 자율적으로 실행하세요
[14:45] . 이것 또한 가능성이 있습니다. 그래서
[14:47] 적어도 인간으로서 나는 그렇게 믿는다.
[14:49] 당신은 어느 정도 개입할지 결정해야 합니다.
[14:51] 진행 중에. 개인적으로 저는
[14:54] 제가 감독을 하면 할수록,
[14:57] 참여하면 참여할수록 그 역할을 더 잘 이해하게 됩니다.
[15:00] LLM이 방향을 바로잡는 것이 더 낫습니다.
[15:04] 결과.
[15:05] 이러한 문제들 중 상당수는 다음과 같습니다.
[15:07] 인류는 여전히 매우 중요합니다.
[15:09] 왜냐하면 먼저 우리는 건설해야 하기 때문입니다
[15:11] 정신 모델과 프로세스 모두
[15:13] 정보. 우리는 우리의 입장을 분명히 해야 합니다.
[15:15] 실제로 무엇인지에 대한 정신적 모델
[15:17] 우리에게 필요한 것과 환경이 어떤지,
[15:19] 그럼 우리는 뭔가를 만들 수 있겠죠. 그게 다예요
[15:21] 인간적 요소가 여전히 남아 있는 곳
[15:22] 정말 중요해요.
[15:24] 제가 이해하기로는 여전히 그렇다는 것입니다.
[15:25] 인간적인 기술이 상당히 부족합니다.
[15:27] 최상의 결과를 얻기 위해.
[15:29] 그래서 마르코와 페르디에게 물어봤어요.
[15:31] ~을 가진 사람에게는 얼마나 쉬울까요?
[15:33] TDD 경험이 부족하여 이러한 것들을 습득하기 어렵습니다.
[15:35] 에이전트의 역량은 무엇이며, 어떻게 성공할 수 있을까요?
[15:38] 그리고 마르코는 자신이 가르치려고 노력했다고 자주 말합니다.
[15:40] 20년간 TDD를 해왔고, 이제 드디어 결실을 맺습니다.
[15:42] 누군가 듣고 있다.
[15:44] 물론 농담이지만, 난 진심으로 그렇게 믿어.
[15:47] 그건 항상 어려운 일 중 하나죠.
[15:50] 학습 측면이 바로 그것이었습니다.
[15:52] TDD 사고방식.
[15:53] 제 생각엔 아무것도 없어도 시작할 수 있을 것 같아요.
[15:55] TDD에 대한 완벽한 지식을 습득하고
[15:57] 맞춤형으로 더욱 심층적인 이해
[15:59] 당신이 그것을 사용한다는 것입니다.
[16:00] 더 깊이 이해하기 위해
[16:02] 물론 TDD도 도움이 될 것입니다.
[16:04] 환경을 개선할 수 있기 때문입니다.
[16:05] 본인의 경험을 공유하되,
[16:07] 시작하기가 너무 어려워요.
[16:15] 코드로도 이용 가능합니다.
[16:16] 문을 열었고 그들은 글을 쓰고 있다고 말합니다.
[16:17] 해당 주제에 관한 책.
[16:18] 이 기사에서 두 사람은 다음과 같이 나눕니다.
[16:20] 세 가지 수준의 자율성. 그것들은 다음과 같습니다: 위임하다
[16:21] 끝까지, 각 주기마다 멈추면서
[16:23] 그리고 모든 단계에서 멈춰 서십시오.
[16:26] 오늘 우리는 마르코와 페르디의 이야기를 들었습니다.
[16:28] 그들의 접근 방식에 대해 말씀드리자면, 첫째로,
[16:30] LLM 코딩 에이전트를 구축하세요
[16:32] 예시를 매핑하여 수정하거나
[16:35] 또 다른 유형의 협업 모델링,
[16:37] 둘째, 제대로 만드세요
[16:38] 예측 기반 테스트 개발
[16:40] 그리고 아마도 하위 에이전트를 재구성하는 것도 포함될 수 있습니다.
[16:43] 모델에 따라 분리됩니다.
[16:45] 사용.
[16:46] 요컨대, AI가 알아서 하도록 내버려두는 대신에
[16:48] 직관에 따라 일하는 것보다 정의하는 것이 더 낫습니다.
[16:50] 무엇을 만들어야 하는지 예시와 함께 단계별로 안내해 주세요.
[16:52] 저는 테스트를 진행합니다.
[16:54] 어떤 방법을 사용하시나요?
[16:56] 인공지능을 이용한 프로그래밍?
[16:57] 이 영상이 도움이 되었다면, 좋아요를 눌러주세요.
[16:59] 구독과 좋아요 부탁드립니다.
[17:00] 시청해 주셔서 감사합니다. 다음에 만나요
[17:02] 다음 영상.
