---
title: "[한글자막] Anthropic은 하루 코드 변경 3만 건을 어떻게 병합할까요? | Addy Osmani"
type: video
source: https://www.youtube.com/watch?v=CmsICMUPtII
site: youtube.com
author:
  - "[[Tech Bridge]]"
duration: 11:06
published: 2026-10-30
created: 2026-10-31
description: "Addy Osmani(Anthropic 쪽 — 발화 1인칭 'at Anthropic, we' · 발화 호명 · 제목 · 설명란) × Manish Kapur(설명란 근거만, 소속 미상) 2인 대담(무대 · 청중 있음) 편집본 11:06, 공식 챕터 11, 내레이션 없음. CircleCI 통계(처리량 +59%, 병합 시도 10건 중 3건 실패), lights-on vs dark software factory, Anthropic 병합량(진행자: 하루 3만 건 / Addy: 5월 2,500건), Claude 1차 리뷰 + 실제 사용자처럼 시험 + hooks 수정 루프, CLAUDE.md · AGENTS.md에 taste 성문화, 사람은 검증 증거(브라우저 영상 · 스크린샷)를 본다, 다음 개선은 검증, 결정론 · 에이전트 리뷰 · 공급망 3층 검증, 통제 · 권한 · 샌드박스, 에이전트 작성 PR 라벨과 사람 책임자, 'Fast to write is not fast to ship', 'autonomy is earned'."
tags:
  - clippings/youtube
---

**Source URL**: https://www.youtube.com/watch?v=CmsICMUPtII
**Channel**: Tech Bridge · **Duration**: 11:06 · **Published**: 2026-10-30

> **게시일.** info.json 기준 `upload_date` **`20261030`**(UTC), `timestamp` 1793350806(= **2026-10-30 18:00 KST**), `availability: public`, `release_date` 없음. 파일명에서 제목 앞의 `[한글자막]`과 `?` · `|`는 뺐다.
>
> **오디오 트랙과 자막 — 인용 규칙.** 10-27 Voss · 10-28 Parakhin · 10-29 Chase 편과 같은 구성이다. 오디오는 **`English (US) original (default)`** 하나가 원본이고 나머지(de · es · fr · hi · id · it · pt)는 더빙이다. **한국어 오디오 트랙이 없다.** 메타 `language`=`en`. **수동 자막(`subtitles`)은 비어 있다** — 제목의 "[한글자막]"과 달리 YouTube에 올라간 한국어 자막 파일은 없다(번인 자막 여부는 영상을 보지 않아 미확인). `automatic_captions`에 **`ko-orig`가 없고**, ko는 `lang=en&variant=gemini&tlang=ko` 기계 번역이다. en-orig URL은 `kind=asr&lang=en&variant=gemini`. 인용은 **en-orig로만** 한다.
>
> ⚠️ **`en` 파일은 en-orig와 다르다(md5 불일치).** info.json의 `en` 첫 URL은 en-orig와 같은 파라미터(`lang=en&variant=gemini`)인데, 받은 `en` 파일 내용은 원문을 고쳐 쓴 문장이다 — 예: en-orig *"software factory is harnessing loops at scale"*(00:45~00:48) → en *"A software factory is about leveraging cycles at scale"*, *"throughput jumped"* → *"performance increased"*. ko는 줄 구분 · 타임스탬프가 en과 거의 같다(빈 줄 2개 차이) → ko는 **en 계열을 옮긴 것으로 추정**. 둘 다 인용 근거가 아니다. `variant=gemini`는 이 채널 기록에서 처음 보는 값이다(같은 날 다른 영상 `-B-967gXzHY`의 en-orig는 `variant=timing-optimized`).
>
> **형식 — 2인 대담 편집본, 내레이션 없음.** 무대 대담이다: *"a lot of folks here have probably heard"*(00:53~00:55), *"the financial customers here"*(09:23~09:25) — 청중이 있고 금융권 고객이 포함된 행사로 보인다. 행사명 · 녹화일 · 원본 링크는 없다. 진행 쪽(Manish 추정)이 통계 · 질문 슬라이드를 읽고(*"this is a quote from Addy"* 00:45, *"Should agent-written code be labeled in the PR?"* 08:28~08:30, *"the agent opened the PR. It is safe to merge when"* 10:20~10:23), Addy가 답하는 구조다. 끝(10:29~11:04)은 진행 쪽의 정리 발언.
>
> **화자 — 두 사람, 귀속 근거의 강도가 다르다.** ASR의 `>>` 화자 전환 표시가 두 목소리를 번갈아 가른다.
> - **Addy Osmani — 강함.** 발화 안에서 두 번 호명된다: *"I I I have the same point of view, Addy."*(09:10), *"Adi was talking about agents review review that code"*(07:11~07:13, ASR "Adi"). 제목 · 설명란에도 이름이 있다. 1인칭 소속: *"at Anthropic, like we we think about this a little bit differently"*(08:42~08:45), *"we were merging about 2,500 changes all the way back in May"*(03:50~03:53), *"our recent refresh of Claude.ai, we put out a case study"*(03:55~03:58). 진행 쪽도 *"the Claude Code team that you're working with"*(03:48~03:49)라고 묻는다. 직함은 발화되지 않는다.
> - **Manish Kapur — 약함(설명란 근거 + 소거법).** 이름은 **발화 · 제목 · 태그 어디에도 없고 설명란에만** 있다. Addy를 3인칭(*"a quote from Addy"* · *"Adi was talking about"*) · 2인칭(*"Addy"* 09:10)으로 부르고 질문을 던지는 목소리(00:20~00:51 · 01:49~02:17 · 03:25~03:49 · 06:24~07:45 · 08:28~08:30 · 09:10~09:32 · 09:45~09:50 · 10:20~10:23 · 10:29~11:04)가 Addy가 아니므로 설명란의 다른 이름에 귀속했다 — **추정**. 소속은 발화되지 않는다: *"most of our customers that I speak to every day"*(00:42~00:44), *"So we look at it in terms of layers"*(06:50~06:51)처럼 고객을 상대하는 회사 쪽이라는 단서뿐이다. 10:29~11:04 정리 발언은 `>>` 표시 뒤 같은 목소리로 이어져 진행 쪽으로 귀속했다(추정).
>
> **내부 시점 단서.** *"all the way back in May"*(03:50~03:53), CircleCI *"this year"*(00:24), *"you take a look at Opus 5.5"*(05:56), *"a couple of months ago"*(07:50), *"the foreseeable (…) 6 to 9 months"*(09:14~09:15). 녹화는 5월 이후이고 Opus 5.5가 나온 뒤다. 연도는 발화되지 않는다(2026년으로 추정).
>
> **무캡션 간격.** **00:00~00:20**(첫 공식 챕터 *"하루 코드 변경 3만 건, 누가 검증할까요?"* 전체 — 타이틀 또는 한국어 훅으로 추정, 미확인). 그 밖의 4초 이상 간격은 00:36→00:40 · 01:38→01:42 · 02:00→02:04 · 02:30→02:34 · 02:50→02:54 · 10:37→10:41뿐이고 모두 문장 중간의 머뭇거림이다. 그러나 **편집 컷으로 보이는 이음매**가 있다: 07:45~07:48 *"Uh (…) in terms of"* 가 끊기고 Addy가 다른 주제(에이전트 통제)로 시작한다. 03:25 *"Yep, yep, absolutely right, spot on."* 바로 뒤에 30,000건 슬라이드 낭독이 이어진다.
>
> ⚠️ **"하루 3만 건"은 진행 쪽 발화다.** *"They are merging about 30,000 code changes every single day. They used to do about 3,000 or so, 2,500 or so code changes just a few months back. They've scaled from 2,500 code changes to 3,000 30,000 code changes per day."*(03:27~03:41) — 스스로 3,000 → 30,000으로 고쳐 말한다. **Addy는 3만을 되풀이하지 않는다.** 그의 숫자는 *"about 2,500 changes all the way back in May"*(단위 기간 미발화)와 Claude.ai 개편 때 *"about 3,000 pull requests in a very short space of time"*(04:03~04:05)뿐이다. 설명란 링크(anthropic.com/research/redesigning-source-control)가 출처일 수 있으나 **열어 보지 않았다(미확인)**.
>
> ⚠️ **ASR 판독.** *"Circle CI"*(00:20) → CircleCI. *"sequel injection"*(07:02) → SQL injection. *"Claude.md, Agents.md"*(05:09~05:12) → CLAUDE.md · AGENTS.md. *"Adi"*(07:11) → Addy. *"two to three by"*(03:21~03:23) · *"three-byed"*(04:01) → 2~3배 · 3배. *"you have to basically count what is getting merged, looked at what is getting merged"*(10:41~10:43) — "control"일 수 있으나 판독 보류.
>
> ⚠️ **회사 · 통계 주장은 전부 미확인.** CircleCI 2,800만 워크플로 · 처리량 약 59% 증가 · 병합 시도 10건 중 3건 실패(00:20~00:32), *"85% of the organizations"* · *"76% of the developers"*(01:54~02:09, 출처 미발화), Claude.ai 개편 *"three-byed the performance"*(03:59~04:01, 사례 연구 링크 없음), *"two to three by like the quality of your outcomes"*(03:21~03:23, 측정 없음).
>
> ⚠️ **ko(기계 번역)는 인용 근거가 아니다.** 참고용으로만 아래에 둔다.

## 설명란

Anthropic은 하루 코드 변경 3만 건을 어떻게 검토할까요? Addy Osmani와 Manish Kapur가 AI 코딩 에이전트의 검증 방식과 사람이 맡아야 할 책임을 설명합니다.

• Claude의 1차 코드 리뷰와 수정 루프
• 실제 브라우저 테스트, 화면과 영상으로 남기는 검증 증거
• 결정론적 검사·에이전트 리뷰·공급망 보안의 다층 검증
• 에이전트의 통제, 권한, 샌드박스와 PR 책임자

00:00 하루 코드 변경 3만 건, 누가 검증할까요?
00:20 코드는 늘었는데 병합은 실패한다
00:53 사람이 판단하는 공장, 스스로 도는 공장
03:26 하루 3만 건을 리뷰하는 방법
04:54 사람은 검증 증거를 확인한다
05:46 다음 개선은 검증에서 나온다
06:24 검증은 모든 루프에서 여러 겹으로
07:45 통제 · 권한 · 샌드박스
08:28 AI가 써도 책임자는 사람이다
09:46 리더와 주니어의 역량, 안전한 병합 기준
10:29 빨리 쓰는 것과 빨리 내놓는 것

📎 관련 자료:
Anthropic의 소스 관리 재설계: https://www.anthropic.com/research/redesigning-source-control
Addy Osmani의 소프트웨어 공장 글: https://addyosmani.com/blog/software-factories/

#AI코딩 #ClaudeCode #Anthropic #코드리뷰 #AI에이전트 #개발자

> info.json `tags`: AI에이전트 · AI코딩 · Anthropic · Claude Code · 개발자 · 코드리뷰

## 트랜스크립트 — en-orig (원음 영어 ASR — 인용 근거)

[00:20] Circle CI analyzed 28 million CI
[00:23] workflows
[00:24] this year.
[00:25] And they noticed that the throughput
[00:26] jumped by about 59%.
[00:29] Uh but yet three in 10 attempts to merge
[00:32] that code into production are failing.
[00:34] And this is a stat from one independent
[00:36] stat from Circle CI. Uh
[00:40] And I think I'm seeing the same trend
[00:42] for most of our customers that I speak
[00:44] to every day.
[00:45] Uh this is a quote from Addy. A software
[00:48] factory is harnessing loops at scale.
[00:51] This resonated quite a bit for me.
[00:53] >> So a lot of folks here have probably
[00:55] heard this term software factories and
[00:57] there's two types of factories that are
[00:58] at least worth keeping in mind. Well,
[01:00] you know, software factory is harnessing
[01:02] loops at scale. A lights-on factory is
[01:04] one where you have agents that are
[01:06] helping you
[01:08] um with planning, building, checking,
[01:10] and shipping code again and again, but
[01:12] you as a person still apply your
[01:14] judgment and taste inside the picture.
[01:16] And then we have a dark software
[01:18] factory, which is a little bit closer to
[01:20] how, you know, a car factory with
[01:22] robotics might be working where it's
[01:24] constantly doing the work. So it's
[01:26] scoping, building, checking, and you as
[01:29] the person move down um further to
[01:31] thinking about intent and you're pulled
[01:33] in when they're really the greatest of
[01:35] exceptions to the case. But that's sort
[01:37] of what I was thinking. I think a lot of
[01:38] teams are somewhere on this spectrum um
[01:42] and are on this journey to figure out
[01:43] like how how do I get further and
[01:44] further into automation in a way that I
[01:46] can trust it.
[01:47] >> Cool.
[01:49] >> So uh
[01:50] AI coding is now basically a solved
[01:52] problem. We all know agents are there.
[01:54] 85% of the organizations are already
[01:56] using coding agents. It'll go to 95% and
[01:58] very soon to 100%.
[02:00] Uh 75% of the uh 76% of the developers
[02:04] that generate AI code,
[02:06] uh they're saying that it it's being
[02:08] code is being produced at a speed that
[02:09] is impossible for them to verify it.
[02:12] So, they're spending more and more time
[02:13] reviewing the code. So, what do you
[02:15] think is the most pressing question that
[02:17] engineering leaders have right now?
[02:20] >> So, I think that teams have gotten
[02:22] better working with agents over the last
[02:24] year. Um models, harnesses have also
[02:26] gotten better. And what I see a lot of
[02:29] leaders being interested in is how do we
[02:30] enable you to ship code faster um with
[02:34] confidence. And that confidence piece is
[02:36] very important. Agents can now generate
[02:39] ways for you to check your code much
[02:41] more cheaply than ever before. And if
[02:43] you think about the things that enabled
[02:44] us to call good code, you know, high
[02:47] quality, uh those were things like good
[02:50] tests, benchmarks, uh specs, anything
[02:54] that gives us confidence. So, agents are
[02:56] able to help us generate that a little
[02:58] bit more easily these days, a little bit
[02:59] more quickly. We can of course refine
[03:01] those things, but I think that those
[03:02] checks are one of the most important
[03:04] things we should be spending our time on
[03:06] these days.
[03:07] Like if you are hoping to get the best
[03:10] quality output from your agents, you
[03:12] need to give your agents a way to verify
[03:14] that the work is correct. If you've got
[03:16] that in place and you can make sure that
[03:18] the code is both correct and complete,
[03:21] that can easily two to three by like the
[03:23] quality of your outcomes.
[03:25] >> Yep, yep, absolutely right, spot on.
[03:27] They are merging about 30,000 code
[03:29] changes every single day.
[03:31] They used to do about 3,000 or so, 2,500
[03:34] or so code changes just a few months
[03:35] back. They've scaled from 2,500 code
[03:38] changes to 3,000 30,000 code changes per
[03:41] day. That is mind-boggling. So, I think
[03:44] what does code review look like at
[03:46] Claude Code at Anthropic and with the
[03:48] Claude Code team that you're working
[03:49] with?
[03:49] >> Yeah, these are great questions. So, we
[03:50] were we were merging about 2,500 changes
[03:53] all the way back in May.
[03:55] Um and even for our recent refresh of
[03:58] Claude.ai, we put out a case study
[03:59] saying that we kind of three-byed the
[04:01] performance of it. That was accomplished
[04:03] by merging about 3,000 pull requests in
[04:05] a very short space of time with
[04:07] engineers, product designers, a number
[04:09] of different functions contributing to
[04:11] it. So, our workflow for being able to
[04:14] get verification and code review in
[04:15] place is that we first of all have
[04:17] Claude do a first pass review. What's
[04:20] very important in there is making sure
[04:22] that it has a way to actually try the
[04:24] experience out similar to a real user.
[04:26] So, that can mean end-to-end tasks, you
[04:29] know, opening up the experience,
[04:30] checking it in a browser, running any
[04:32] tools, doing any linting, doing any
[04:34] other checks that are necessary to build
[04:36] up that confidence.
[04:37] Um people usually ask us, "Okay, well
[04:39] what happens if, you know, you discover
[04:41] a bug or a gap in functionality?" Well,
[04:44] we have hooks that will then go and run
[04:46] on any edits, they will study the diffs,
[04:49] and allow us to get this loop in place
[04:50] where we're correcting the PR as quickly
[04:53] as possible.
[04:54] Um and increasingly what's important is
[04:57] for your teams to be thinking about how
[04:59] can you codify We talk about taste and
[05:01] judgment so much these days, right? It's
[05:03] important for you to be trying to codify
[05:05] what you consider best practice and
[05:07] taste in your team's shared like
[05:09] Claude.md, Agents.md, anywhere where the
[05:12] agent can then consult during code
[05:14] review. And then people are responsible
[05:17] for checking on the agent's evidence.
[05:19] So, how do we know if I'm building out
[05:21] um
[05:22] a piece of UI that's going to be, you
[05:24] know, used by a user in the browser, I
[05:26] want to make sure that it's tested in
[05:28] the browser, maybe generated me a video
[05:30] of that experience where it's been
[05:31] clicking around and gives me confidence,
[05:33] well, okay, well, this works. If I care
[05:35] about the mobile or desktop experience,
[05:37] maybe it generates me screenshots or
[05:38] videos of that. But basically, you want
[05:40] to get to a place where the agent's
[05:41] giving you as much verification evidence
[05:43] as possible. Cool.
[05:45] >> Yeah, verification is key.
[05:46] >> I think the next gains are going to come
[05:47] from a combination of us really nailing
[05:50] verification, right? As well as model
[05:52] quality. But models are already like you
[05:54] you take a look at Opus 5.5, model
[05:56] quality has already gotten to a place
[05:57] where it's pretty good. Um and I would
[06:00] say that us being able to share best
[06:02] practices about that verification step
[06:03] is going to become increasingly more
[06:05] important because if you tell people
[06:06] yeah, just like verify the work, you
[06:08] know, their next question is what does
[06:09] that even mean, right? And so I think
[06:11] that the conversation needs to evolve
[06:13] into specifically what kinds of tasks
[06:15] are useful. We lean a lot on end-to-end
[06:17] tasks, property tests, any visual
[06:20] verification tests, things that can help
[06:21] us just get that confidence to merge
[06:23] those changes in automatically.
[06:24] >> I would absolutely 100% believe that
[06:27] each company should adopt a zero trust
[06:29] multi-layered verification approach. And
[06:32] verification should be done in every
[06:33] loop. Whether you're operating inside
[06:36] the agentic loop or whether you're
[06:37] working inside the CI verification loop
[06:40] or whether you doing code maintenance.
[06:42] In each and every loop, it is important
[06:44] to verify the output of the factories or
[06:46] the agents that code that the agents are
[06:48] producing.
[06:50] So we look at it in
[06:51] terms of layers and
[06:54] think of it like you know, the there's
[06:55] first layer which is a deterministic
[06:57] layer which catches
[06:59] uh
[06:59] bugs, security issues, things like
[07:02] sequel injection,
[07:03] buffer overflow bugs and all of those
[07:05] are caught. And then there's a second
[07:07] layer where agentic review happens where
[07:09] agents are used to like
[07:11] Adi was talking about agents review
[07:13] review that code. And in that agentic
[07:15] review, they catch logic and intent
[07:17] issues which the deterministic layer is
[07:20] not well suited to catch. So we we use
[07:23] each layer is targeted at catching a
[07:25] specific types of issues. And then the
[07:27] third layer could be a software supply
[07:29] chain security layer
[07:30] where you look at all the CVEs, all your
[07:33] malware
[07:34] detection happens, all your malicious
[07:36] package detection happens. All of that
[07:38] happens in the third layer. So it's a
[07:40] layered approach where each layer is
[07:42] tuned and optimized to catch a certain
[07:44] type of issue.
[07:45] Uh
[07:47] in terms of
[07:48] >> So I've talked to so many companies
[07:50] where a couple of months ago one of
[07:51] their biggest worries was they were
[07:53] allowing their engineering teams to go
[07:54] off and play around with agents and they
[07:56] got to a place where there were
[07:58] hundreds, thousands of agents in some
[08:00] cases and they just didn't know what
[08:01] they were doing. Like what are these
[08:03] agents actually doing? They're touching
[08:04] all of our systems, accessing all kinds
[08:06] of data, maybe they're deploying to
[08:07] production. And so, a lot of enterprises
[08:10] think about concerns like uh you know,
[08:13] agent identity and telemetry and being
[08:15] able to track what's actually happening.
[08:17] And I'd say that the three biggest
[08:18] things for a lot of companies are how do
[08:20] we think about control, how do we think
[08:21] about permissions, and how do we think
[08:23] about the sandbox? Like, how are we
[08:24] making sure that the agent isn't jumping
[08:26] out of the sandbox and doing things that
[08:27] it shouldn't be doing?
[08:28] >> Yeah. Should agent-written code be
[08:30] labeled in the PR?
[08:32] >> I personally think it should.
[08:33] Historically, we have uh felt a great
[08:35] deal of ownership around our code, pride
[08:38] around the fact that hey, I wrote this
[08:39] thing. I'm putting my name on it. And at
[08:42] Anthropic, like we we think about this a
[08:43] little bit differently. We've evolved to
[08:45] the point where we don't really mind so
[08:47] much if Claude is like labeled as hey,
[08:50] I'm I'm the one that wrote this thing,
[08:51] because we're a little bit more focused
[08:52] on the outcomes and making sure that the
[08:54] code, the features, like what we're
[08:56] shipping to users um is the right thing.
[08:58] And so, I personally think it's fine for
[09:01] the code be written labeled as being
[09:03] coming from an agent, and that can also
[09:04] help us with things like figuring out
[09:06] okay, well, if the agent wrote it, what
[09:07] are some of the constraints and extra
[09:08] checks that we need to keep in place.
[09:10] >> I I I have the same point of view, Addy.
[09:12] I think in the short run, at least in
[09:14] the foreseeable uh you know, 6 to 9
[09:15] months, we should label the PRs
[09:18] till we are confident enough in our
[09:20] factories. We do want to know and track
[09:22] it, and it's also important for the
[09:23] financial customers here in terms of
[09:25] auditability. If you uh you know, if you
[09:28] uh label it, uh you know who's writing
[09:30] the code, because we are at the end of
[09:31] the day still accountable for
[09:32] >> Yeah, absolutely. The accountability is
[09:33] the most important part here. Like, we
[09:35] still label like who's the owner for
[09:37] this change. I might have kicked off a
[09:39] Claude a Claude run to complete a piece
[09:41] of work, but I'm I'm still on the hook.
[09:43] If something goes wrong, I have to go
[09:44] and fix it.
[09:45] >> Yep. Yep. Key point. Yep. What One skill
[09:48] a junior developer or leaders should uh
[09:50] build on this year?
[09:52] >> I think that you should push your teams
[09:54] if you're a leader, you should push your
[09:55] teams to really think hard about what
[09:57] verification means. Um how are you
[09:59] already approaching things like testing?
[10:01] What is the gap between that and you
[10:04] getting to a place where you're very
[10:05] comfortable with the agents being able
[10:07] to sign off on the code being good
[10:08] enough to merge on their own. And so,
[10:10] figuring that out, if you're a junior,
[10:12] it's the other side of that. Like,
[10:13] actually getting more experience in the
[10:15] different flavors of tests, whether it's
[10:17] like end-to-end tests, property tests,
[10:19] etc.
[10:20] >> Yep.
[10:20] >> Uh the agent opened the PR. It is safe
[10:23] to merge when
[10:25] >> You have full confidence nothing's going
[10:27] to go wrong, or that you've mitigated
[10:28] that as much as possible.
[10:29] >> Uh writing code is the fastest part, and
[10:31] that is solved. Strong review and
[10:33] verification for all teams uh is what
[10:35] will will help you maintain that speed.
[10:37] Fast to write is not fast to ship. Uh
[10:41] you have to basically count what is
[10:42] getting merged, looked at what is
[10:43] getting merged, and make sure it doesn't
[10:45] escape the sandbox and the things like
[10:46] that before it gets into the production.
[10:48] Verify everything. And autonomy is
[10:51] earned. Uh you We will get to software
[10:54] factories very soon, if not next year.
[10:56] Uh you need to put in independent
[10:58] automated verification inside each loop
[11:00] of your factory. Make sure that you can
[11:02] trust the output that the factory is
[11:04] producing.

## 트랜스크립트 — ko (`tlang=ko` 기계 번역 — 참고용, 인용하지 않음)

[00:20] Circle CI는 2,800만 건의 흐름을 분석했습니다.
[00:23] CI의 올해 활동.
[00:25] 그들은 성능이 향상된 것을 알아차렸습니다.
[00:27] 약 59%이지만, 10명 중 3명은 그렇습니다.
[00:30] 해당 코드를 병합하려는 시도
[00:33] 생산에 실패했습니다. 그리고 이것은
[00:35] Circle CI에서 제공하는 독립적인 통계 자료입니다.
[00:39] 저도 같은 현상을 보고 있는 것 같아요.
[00:40] 우리 대부분의 추세
[00:42] 매일 대화하는 고객들입니다.
[00:45] 이것은 애디의 말입니다.
[00:48] 소프트웨어 팩토리는 활용에 관한 것입니다.
[00:50] 스케일링된 주기.
[00:51] 이 말이 제게 꽤 와닿았습니다.
[00:53] 여기 있는 많은 사람들이 아마도
[00:55] "공장들"이라는 용어를 들었습니다.
[00:56] 소프트웨어라는 분야가 있고, 공장에는 두 가지 유형이 있습니다.
[00:58] 적어도 하나쯤은 소장할 가치가 있는 것
[00:59] 계정. 음, 아시다시피, 공장
[01:01] 소프트웨어는 사이클을 활용하는 것입니다.
[01:02] 규모.
[01:03] 불이 켜진 공장은
[01:05] 당신에게 대리인이 있는 것
[01:08] 그들은 계획하고 건설하는 데 도움을 줍니다.
[01:09] 코드를 확인하고 계속해서 전송하세요.
[01:12] 하지만 당신은 개인으로서 여전히 당신의 원칙을 적용합니다.
[01:14] 그 과정에서 기준과 취향을 고려합니다.
[01:17] 그리고 소프트웨어 공장이 있습니다.
[01:18] "어두운"이라는 단어는 조금 더 가까운 의미입니다.
[01:20] 어떻게, 아시다시피,
[01:22] 로봇 공학을 도입한 자동차 공장
[01:23] 일이 이루어지는 곳
[01:24] 끊임없이.
[01:25] 그래서 범위 문제를 해결해 줍니다.
[01:27] 건설, 검증, 그리고 당신은
[01:29] 사람
[01:30] 의도에 대해 생각하는 데 더 많은 시간을 할애합니다.
[01:32] 그리고 정말 중요한 일이 있을 때만 연락을 줘요.
[01:34] 가장 큰 예외 사항들. 하지만 그건
[01:36] 제가 생각했던 것과 거의 비슷하네요. 제 생각에는
[01:38] 많은 팀들이 어느 시점에선가 그런 상황에 놓이게 됩니다.
[01:40] 우리는 이 스펙트럼에 있으며 이 여정에 있습니다.
[01:42] 더 깊이 파고드는 방법을 알아보세요
[01:44] 자동화 방식에서
[01:46] 내가 신뢰할 수 있는 사람.
[01:47] 멋진.
[01:49] AI 코딩은 이제,
[01:50] 기본적으로 문제가 해결됐습니다. 모두
[01:53] 우리는 요원들이 거기에 있다는 것을 알고 있습니다. 85
[01:54] 조직의 %가 이미
[01:56] 코딩 에이전트를 사용합니다.
[01:57] 95%에 도달할 것이고 곧 100%에 이를 것입니다.
[02:01] 개발자 중 76%가 생성
[02:04] AI 코드는 코드가 다음과 같다고 말합니다.
[02:06] 생산 속도는 다음과 같습니다.
[02:08] 검증이 불가능합니다.
[02:12] 그러므로 그들은 점점 더 많은 시간을 보낸다.
[02:13] 코드 검토 중. 그래서, 어느 쪽을 고르시겠어요?
[02:15] 그게 가장 시급한 질문이라고 생각하세요?
[02:17] 엔지니어링 리더들이 가지고 있는 것
[02:19] 이 순간이요?
[02:20] 팀들이 실력이 향상된 것 같아요.
[02:22] 지난 몇 달 동안 에이전트들과 함께 일하면서
[02:24] 년도. 모델 및 도구
[02:26] 그들도 발전했습니다. 제가 보는 것은 다음과 같습니다.
[02:29] 많은 지도자들이 관심을 갖는 것은 바로 '어떻게'입니다.
[02:31] 우리는 그들이 더 많은 코드를 보낼 수 있도록 허용할 수 있습니다.
[02:33] 빠르고 자신감 넘친다.
[02:35] 그리고 신뢰의 그 부분은 매우 중요합니다.
[02:37] 중요한. 이제 요원들은
[02:39] 귀하의 신원을 확인할 수 있는 방법을 제공합니다
[02:40] 코드를 작성하는 것이 훨씬 더 경제적입니다.
[02:42] 절대. 그리고 우리가 무엇을 하는지 생각해 보세요
[02:45] 이미 "좋은" 코드라고 부르는 것이 허용되었습니다.
[02:47] 아시다시피, 고품질이라는 건 그런 것들이죠.
[02:49] 좋은 테스트, 벤치마크와 같은 것들
[02:52] 사양, 우리가 가진 모든 것
[02:54] 자신감을 불어넣다. 그래서 요원들은
[02:56] 우리가 그것을 만들어내는 데 도움을 줄 수 있는
[02:57] 요즘은 조금 더 쉽게, 조금 더
[02:59] 더 빠르게. 물론이죠, 할 수 있어요.
[03:00] 그런 것들을 완벽하게 만들 수는 있겠지만, 제 생각에는...
[03:02] 그러한 제어는 가장 중요한 것 중 하나입니다.
[03:03] 우리가 해야 할 중요한 것들
[03:05] 오늘 우리의 시간을 투자하세요.
[03:07] 예를 들어, 최고의 결과를 기대한다면
[03:10] 상담원의 자질을 높이려면, 그들에게 필요한 것을 제공해야 합니다.
[03:12] 작업이 완료되었는지 확인하는 한 가지 방법
[03:15] 옳은.
[03:16] 만약 해당 기능을 구현했다면,
[03:18] 코드가 정확한지 확인하세요
[03:20] 그리고 완성되면 쉽게 할 수 있습니다.
[03:22] 당신의 품질을 두 배 또는 세 배로 높이세요
[03:24] 결과.
[03:25] 네, 네, 완전히 맞습니다. 정확히 지적하셨어요.
[03:26] 못. 그들은 긴밀하게 통합되고 있습니다.
[03:28] 매일 3만 건의 코드 변경이 발생합니다.
[03:31] 그들은 예전에 약 3,000번에서 2,500번 정도 거스름돈을 주곤 했습니다.
[03:34] 불과 몇 달 전까지만 해도 코딩을 하던 사람입니다. 그들은 가지고 있다
[03:36] 2,500건의 코드 변경에서 확장
[03:39] 하루에 3만 건의 코드 변경이 발생합니다. 즉
[03:42] 환각을 일으키는.
[03:43] 그렇다면 코드 리뷰는 구체적으로 어떤 모습일까요?
[03:45] Anthropic의 Claude Code와 함께
[03:47] 클로드 코드의 팀은 다음과 같은 팀과 함께
[03:48] 일하세요?
[03:49] 네, 아주 좋은 질문입니다.
[03:50] 우리는 약 2,500개를 통합하고 있었습니다.
[03:53] 5월 이후 변경 사항.
[03:55] 그리고 최근의 경우에도 마찬가지입니다.
[03:57] Claude.ai 업데이트 소식을 게시했습니다.
[03:59] 한 사례 연구에서는 다음과 같이 말합니다.
[04:00] 성능을 세 배로 향상시켰습니다.
[04:02] 이는 약 3,000개의 통합을 통해 달성되었습니다.
[04:04] 추출 요청 시간
[04:06] 엔지니어, 디자이너와 함께 아주 간략하게 설명드리겠습니다.
[04:08] 제품 및 여러 가지 기능
[04:10] 기여하고 있습니다.
[04:11] 목표 달성을 위한 워크플로우
[04:13] 검증 및 코드 검토
[04:16] 그것은 먼저 만드는 것으로 구성됩니다.
[04:18] 클로드, 초기 검토를 수행해 주세요. 그것
[04:20] 반드시 확인해야 할 사항은 다음과 같습니다.
[04:22] 그 경험을 테스트할 방법을 가지고 있다
[04:24] 마치 ~하는 방식과 유사하게
[04:26] 실제 사용자. 그것은 다음을 의미할 수 있습니다.
[04:28] 처음부터 끝까지 모든 작업을 말하는 거죠.
[04:29] 체험을 시작하고, 그에 대한 리뷰를 작성하세요.
[04:31] 브라우저, 도구 실행, 실행
[04:33] 보푸라기 및 기타 제어
[04:35] 그러한 신뢰를 구축하는 데 필수적입니다.
[04:37] 사람들은 종종 우리에게 "괜찮은 건가요?"라고 묻습니다.
[04:39] 하지만 만약 실수를 발견하게 된다면 어떻게 될까요?
[04:42] "기능상의 공백인가요?" 잘
[04:44] 우리는 실행되는 후크를 가지고 있습니다.
[04:46] 어떤 판본이든, 그들은 연구합니다.
[04:48] 차이점을 통해 우리가 이것을 만들어낼 수 있도록 해줍니다.
[04:50] PR을 최대한 교정하는 주기
[04:53] 가능한 한 빨리.
[04:54] 음, 그리고 그들의 그것이 점점 더 중요해지고 있습니다.
[04:57] 팀들은 어떻게 모방할지 고민한다...
[04:59] 오늘날 우리는 취향과 판단력에 대해 많은 이야기를 나눕니다.
[05:01] 요즘은 그렇지 않나요? 중요한 것은
[05:04] 그들이 생각하는 것을 법제화하려고 시도한다.
[05:06] 모범 사례와 좋은 취향
[05:08] 팀에서 공유하는 파일(예: ...)
[05:10] quad.md 또는 agents.md에서 에이전트
[05:12] 검토 중에 상담할 수 있습니다.
[05:14] 암호.
[05:15] 그리고 그다음에는 사람들이 책임을 져야 합니다.
[05:16] 제시된 증거를 검증하기 위해
[05:18] 에이전트. 그렇다면 우리는 어떻게 알 수 있을까요?
[05:20] 제가 만약 어떤 작품을 만들고 있다면,
[05:22] 사용자가 사용할 인터페이스
[05:24] 브라우저에 있는 사용자, 저는 원합니다.
[05:26] 반드시 테스트를 거치도록 하십시오.
[05:27] 브라우저가, 아마도 생성할 것입니다.
[05:29] 그 경험을 담은 영상이 있습니다.
[05:31] 클릭했더니 자신감이 생겼어요.
[05:32] 음, 이거 괜찮네요.
[05:35] 내가 모바일에 관심이 있다면
[05:36] 데스크톱, 아마도 생성될 것입니다.
[05:38] 해당 장면의 스크린샷이나 동영상.
[05:39] 하지만 기본적으로 여러분은 다음 단계에 도달하고 싶어합니다.
[05:41] 에이전트가 가장 높은 가격을 제시하는 지점
[05:42] 검증 증거의 양
[05:43] 가능한. 멋진.
[05:45] 네, 검증이 핵심입니다.
[05:46] 다음 수익은 반드시 발생할 것이라고 믿습니다.
[05:48] 우리 중 일부가 달성한 결과
[05:50] 검증을 마스터하는 거죠? 그래서
[05:51] 모델의 품질과 같은 것들 말입니다. 하지만
[05:53] 이미 모델들이 존재합니다...만약 살펴보신다면
[05:55] 오푸스 5.5, 모델의 품질은 이미 뛰어납니다.
[05:57] 상당히 늦은 지점에 이르렀습니다.
[05:58] 좋은.
[05:59] 그리고 저는 우리가 할 수 있다는 사실이 중요하다고 생각합니다.
[06:01] 모범 사례를 공유하세요
[06:02] 해당 검증 단계는 매번 수행됩니다.
[06:04] 더 중요한 것은, 만약 당신이 말한다면
[06:06] 사람들은 "네, 그냥 일자리를 확인해 보세요"라고 말합니다.
[06:08] 다음 질문은 그것이 무엇을 의미하는가 하는 것입니다.
[06:09] 심지어? 오른쪽? 그래서 저는 그렇게 생각합니다.
[06:11] 대화는 어떤 방향으로 흘러가야 할까요?
[06:13] 특정한 유형의 작업은 유용합니다.
[06:16] 우리는 극한의 과제에 크게 의존합니다.
[06:17] 극단적인, 속성 테스트,
[06:19] 시각적 검증 테스트
[06:20] 우리가 그것을 얻는 데 도움이 되는 것들
[06:22] 이러한 변화를 통합할 자신감
[06:23] 자동으로.
[06:25] 저는 각자가 절대적으로 그리고 전적으로 그렇게 믿습니다.
[06:26] 회사는 다음과 같은 접근 방식을 채택해야 합니다.
[06:28] 제로 트러스트 검증 및
[06:30] 다층 구조.
[06:31] 그리고 검증은 각 단계에서 이루어져야 합니다.
[06:33] 주기.
[06:34] 귀하가 다음 분야에서 활동하든
[06:36] 에이전트 주기 또는 그 안에서 작업
[06:38] CI 검증 주기의 일부 또는
[06:40] 코드 유지보수를 수행하는 동안,
[06:42] 매 주기마다
[06:44] 결과를 검증하는 것이 중요합니다
[06:46] 공장 또는 에이전트가 사용하는 코드
[06:48] 그들은 생산하고 있습니다.
[06:50] 그래서 우리는 그것을 계층적인 관점에서 봅니다.
[06:52] 그리고 우리는 그것을 이렇게 생각해요, 아시다시피, 그런 것들이 있죠
[06:55] 첫 번째 레이어는 레이어입니다.
[06:56] 결정론적 오류 탐지
[06:58] 보안 문제, 예를 들면...
[07:00] SQL 인젝션, 오버플로우 오류
[07:03] 버퍼의 모든 것이 감지됩니다.
[07:06] 그리고 그 다음에는 두 번째 층이 있습니다.
[07:08] 대리인 검토는 다음과 같은 경우에 발생합니다.
[07:10] 아디가 언급했듯이 그들은 요원을 이용합니다.
[07:12] 해당 코드를 검토해 보세요. 그리고 그 리뷰에서
[07:15] 에이전트 기반, 논리적 문제 감지
[07:18] 그리고 결정론적 계층이 의도하는 바는 그렇지 않다는 것입니다.
[07:20] 식별할 수 있습니다. 그래서 우리는 사용했습니다
[07:23] 각 계층은 유형 감지에 중점을 두었습니다.
[07:25] 구체적인 문제들.
[07:27] 그리고 세 번째 층은 다음과 같이 만들어질 수 있습니다.
[07:29] 공급망 보안
[07:31] 모든 CVE를 분석하는 소프트웨어입니다.
[07:33] 모든 악성코드 탐지 기능,
[07:35] 악성 패킷 탐지, 모든 것
[07:37] 그건 세 번째 레이어에서 일어납니다. 그것은
[07:40] 계층적 접근 방식, 여기서 각 단계는 다음과 같습니다.
[07:41] 감지하도록 조정 및 최적화됨
[07:43] 특정한 유형의 문제.
[07:45] 음, ~에 관해서
[07:48] 저는 정말 많은 회사들과 이야기를 나눠봤는데,
[07:50] 두 달 전, 그녀의 가장 큰 일 중 하나가 일어났습니다.
[07:52] 그들의 걱정은 그들이 허용했다는 점이었습니다.
[07:54] 엔지니어링 팀은 실험을 진행합니다.
[07:55] 요원들과... 그들은 다음과 같은 지점에 도달했습니다.
[07:57] 어떤 경우에는 수백 건에 달하기도 했습니다.
[07:59] 수천 명의 에이전트가 있지만, 그들은 전혀 그렇게 하지 않습니다.
[08:00] 그들은 자신들이 무엇을 하고 있는지 알고 있었다. 내 말은,
[08:02] 이 사람들은 실제로 무엇을 하고 있는 걸까요?
[08:03] 자치령 대표? 그들은 우리의 모든 것을 만지고 있어요
[08:05] 모든 유형의 시스템에 액세스합니다.
[08:06] 데이터, 어쩌면 배포까지 포함될 수도 있습니다.
[08:08] 생산. 그래서 많은 회사들이
[08:10] 그들은 정체성과 같은 주제를 고려합니다.
[08:12] 에이전트, 원격 측정 및 추적 기능
[08:15] 실제로 일어나는 일.
[08:17] 응.
[08:17] 그리고 저는 세 가지 측면 모두라고 말씀드리겠습니다.
[08:18] 많은 기업에게 있어 주요한 고려 사항은 다음과 같습니다.
[08:20] 우리가 통제에 대해 생각하는 방식,
[08:22] 권한 및 격리된 환경에서 (
[08:23] 모래 상자). 그렇다면 어떻게 하면 확실히 할 수 있을까요?
[08:25] 에이전트가 환경을 떠나지 않는다는 것
[08:26] 고립되어 있고 해서는 안 될 일들을 한다
[08:28] 하다?
[08:28] 예. 코드에 라벨을 붙여야 할까요?
[08:30] 지원서에 에이전트가 작성한 내용입니다.
[08:31] 추출(PR)?
[08:32] 개인적으로는 그렇게 생각합니다.
[08:33] 역사적으로 우리는 큰 만족감을 느껴왔습니다.
[08:35] 우리 코드에 대한 책임,
[08:37] "이봐, 나"라고 말하는 것에 자부심을 느낍니다.
[08:39] "이 글은 제가 썼습니다." 제가 제 이름을 적었습니다.
[08:41] 그리고 앤트로픽에서는 이 점을 다음과 같이 생각했습니다.
[08:43] 약간 다른 방식입니다.
[08:45] 우리는 다음과 같은 단계까지 진화했습니다.
[08:47] 우리는 클로드가 당하든 말든 그다지 신경 쓰지 않아.
[08:49] "야, 내가 그랬어"라고 표시해 둬.
[08:50] "그가 이걸 썼어." 왜냐하면 우리는 더 많이
[08:52] 결과에 집중하고
[08:53] 코드, 함수,
[08:55] 우리가 사용자에게 보내는 것이 무엇이든 간에,
[08:57] 옳은.
[08:58] 그래서 저는 개인적으로 그렇게 생각합니다.
[09:00] 코드가 표시되어 있는 한
[09:02] 그건 에이전트를 통해 오는 겁니다. 그리고 그것도
[09:04] "매우 잘"을 판단하는 데 도움이 될 수 있습니다.
[09:06] 만약 에이전트가 그 글을 썼다면, 그들은 누구인가?
[09:07] 제한 및 통제
[09:08] 우리가 유지해야 할 추가적인 사항은 무엇인가요?
[09:10] 저도 같은 생각입니다, 에디.
[09:12] 제 생각에는 단기적으로, 적어도 그 당시에는
[09:14] 향후 6~9개월 내에 우리는
[09:15] 레이블 추출 요청
[09:17] (PR) 충분한 양이 확보될 때까지
[09:19] 저희 공장을 믿으세요.
[09:21] 우리는 그것을 알고 추적하고 싶고, 또한
[09:22] 이는 우리 고객들에게 중요합니다.
[09:24] 감사 가능성 측면에서 재무적
[09:26] .
[09:27] 태그를 달면 누가 있는지 알 수 있어요.
[09:28] 결국 코드를 ​​작성하는 이유는...
[09:30] 궁극적으로 우리는 여전히 책임이 있습니다.
[09:32] 네, 물론입니다. 책임이란
[09:34] 여기서 가장 중요한 부분입니다. 예를 들어,
[09:35] 우리는 누가 누구인지 계속해서 규정짓고 있습니다.
[09:37] 이 변경 사항의 소유자입니다. 어쩌면 나
[09:38] 클로드에 대한 사형 집행을 시작했습니다.
[09:40] 일을 완료하기 위해서지만, 나는 계속 나아간다
[09:42] 책임감 있는. 만약 문제가 생긴다면
[09:43] 가서 고쳐야겠어요.
[09:45] 예. 예. 핵심입니다. 예. 어떤 기술
[09:48] 발전시켜야 한다
[09:49] 올해 주니어인가요, 아니면 리더인가요?
[09:52] 저는 리더라면 적극적으로 나서야 한다고 생각합니다.
[09:54] 팀원들이 생각하도록
[09:56] 그것이 의미하는 바를 진지하게 받아들이세요
[09:57] 확인.
[09:59] 그들은 현재 어떤 방식으로 문제를 해결하고 있습니까?
[10:00] 어떻게 테스트하나요?
[10:02] 그것과 목표 달성 사이의 차이는 무엇일까요?
[10:04] 당신이 편안함을 느끼는 지점
[10:06] 에이전트가 코드를 승인합니다
[10:08] 직접 병합해야 할까요?
[10:10] 그리고 만약 당신이 후배라면, 그것을 발견했을 때의 기분은 어떨까요?
[10:12] 동전의 다른 면. 즉,
[10:14] 다양한 분야에서 더 많은 경험을 쌓다
[10:15] 시험 유형, 시험이 어떤 종류의 시험인지 여부
[10:17] 엔드투엔드 테스트
[10:18] 부동산 등
[10:20] 응.
[10:20] 상담원이 애플리케이션을 열었습니다.
[10:21] 추출. 병합해도 안전한 경우는 언제인가요?
[10:25] 당신은 아무것도 없다는 것을 완전히 확신합니다.
[10:27] 결과가 좋지 않을 수도 있지만, 당신은 그 영향을 완화했을 수도 있습니다.
[10:28] 가능한 한.
[10:29] 코드를 작성하는 것이 가장 빠른 부분입니다.
[10:31] 그 문제는 이미 해결되었습니다. 리뷰 및
[10:33] 모든 항목에 대한 강력한 검증
[10:34] 장비는 유지 관리에 도움이 될 것입니다.
[10:36] 그 속도.
[10:37] 빠르게 타이핑한다고 해서 전송이 되는 것은 아닙니다.
[10:39] 빠른.
[10:41] 기본적으로, 그것을 고려해야 합니다.
[10:42] 병합되는 내용을 검토하세요.
[10:44] 병합하고 이탈하지 않도록 하세요.
[10:45] 테스트 환경에서 도착하기 전에
[10:47] 생산.
[10:48] 모든 것을 확인하세요. 자율성은 노력으로 얻어지는 것이다.
[10:51] 우리는 소프트웨어 공장에 도달할 것입니다
[10:53] 조만간, 늦어도 내년에는 가능할 겁니다.
[10:56] 검증을 구현해야 합니다.
[10:58] 자동화되고 독립적으로 작동합니다.
[11:00] 공장의 각 주기마다. 확실하게 하다
[11:02] 그 결과를 신뢰할 수 있도록
[11:04] 공장에서 생산합니다.
