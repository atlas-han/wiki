---
title: "[한글자막] Grok Bot은 매니저, Claude Code는 개발자: AI 에이전트를 함께 쓰는 법"
type: video
source: https://www.youtube.com/watch?v=ra5WyQ-hKN4
site: youtube.com
author:
  - "[[Tech Bridge]]"
duration: 12:33
published: 2026-11-02
created: 2026-11-03
description: "Rob Shocks(설명란 근거 — 발화에 이름 없음, 1인칭 'my own factory' · 'this channel')의 12:33 1인 해설 영상, 공식 챕터 8, 내레이션 없음 · 영어 원본 오디오만. 테제: GrokBot(오케스트레이터)은 매니저 — first mile(무엇을 지을지, 의도 관리) · last mile(검사 · 추적)만 맡고, 코드는 Claude Code · Cursor Cloud agents 등 코딩 에이전트에게 넘긴다(구독 비용 · 격리). Lauren Tan의 다섯 단계 루프(Slack → Linear 티켓 → Cursor Cloud agent 재현 → fix and fuzz PR → 1시간 뒤 자동 머지) 전달, 신뢰의 역피라미드 4층(코드베이스 · 정적 분석 · 규칙 파일 · 사람 리뷰), Anthropic 수치(6~9월 Claude Code 머지 PR 2배+ · revert 비율 40%+ 감소) 전달, Alan Wells 6주 검증 투자, 발표자 자기 구성(메인 에이전트 Chief · 봇별 좁은 권한 · RICE + blast radius 백로그), 보안(GrokBot들이 컴퓨터 · 자격 증명 공유, Docker 등 secure software factory 참조 아키텍처), 시작 규칙 한 줄."
tags:
  - clippings/youtube
---

**Source URL**: https://www.youtube.com/watch?v=ra5WyQ-hKN4
**Channel**: Tech Bridge · **Duration**: 12:33 · **Published**: 2026-11-02

> **게시일.** info.json 기준 `upload_date` **`20261102`**(UTC), `timestamp` 1793610035(= 2026-11-02 09:00:35 UTC = **2026-11-02 18:00 KST**), `availability: public`, `release_date` 없음, `live_status: not_live`. UTC · KST 날짜가 같다. 파일명 · `published`는 `upload_date`(2026-11-02). 파일명에서 제목 앞의 `[한글자막]`과 `,` · `:`는 뺐다.
>
> **오디오 트랙과 자막 — 인용 규칙.** 10-27 Voss 편부터 이어진 **영어 원본 오디오만** 있는 구성이다. 오디오는 **`English (US) original (default)`** 가 원본이고 나머지(French (FR) · German (DE) · Hindi · Indonesian · Italian · Portuguese (BR) · Spanish (US))는 더빙이다. **한국어 오디오 트랙이 없다.** 메타 `language`=`en`. **수동 자막(`subtitles`)은 비어 있다** — 제목의 "[한글자막]"은 YouTube 자막 파일이 있다는 뜻이 아니다(번인 자막 여부는 영상을 보지 않아 미확인). `automatic_captions`(164키)에 **`ko-orig`가 없고**, ko는 `kind=asr&lang=en&variant=gemini&tlang=ko` 기계 번역이다. en-orig · en의 json3 URL은 둘 다 `kind=asr&lang=en&variant=gemini`(`tlang` 없음). `-orig` 키는 en · fr · de · hi · id · it · pt · es 여덟 개(더빙 쪽은 받지 않았다). 인용은 **en-orig로만** 한다.
>
> ⚠️ **`en` 파일은 en-orig와 다르다(md5 불일치)** — URL 파라미터가 같은데 내용은 고쳐 쓴 문장이다(10-30 Osmani 편 이후 7편째). 뜻이 바뀌는 곳: en-orig *"a Cursor Cloud agent is triggered to go and reproduce the issue on its own computer"*(03:15~03:21) → en *"reproduce the problem on your own computer"* — **에이전트의 컴퓨터가 사용자의 컴퓨터로 바뀐다.** 시작 규칙의 *"check the proof"*(12:22) → en *"verify the test"*. Anthropic 수치의 *"their merged pull requests to Claude code more than doubled"*(06:18~06:22) → en *"their pull requests to the claw code more than doubled"* — **"merged"가 빠진다.** *"blast radius"* → en *"impact radius"*(04:10) · *"explosion radius"*(10:36), *"playwright testing"*(10:50~10:52) → en *"execution (…) testing"*, *"the coder"*(00:23) → *"the programmer"*. ⚠️ **en은 en-orig에서 잘린 마지막 문장을 완성한다** — en-orig 마지막 큐는 *"then a rules file, and review comes"*(12:30)로 끝나는데 en은 *"and finally the review."*(12:31~12:32)를 붙인다. en · ko는 403 · 405줄, en-orig는 369줄. 둘 다 인용 근거가 아니다.
>
> **형식 — 1인 해설 영상(화면 자료 · 트윗 · 글 인용), 내레이션 없음.** en-orig 첫 큐는 **00:21.4**(*"Your bot should be the manager here, not the coder."* 00:21~00:23)이고 문장의 시작이다. **00:00~00:21(첫 공식 챕터 *"소개"* 00:00~00:21 전체)은 무캡션**이다 — 타이틀 또는 한국어 훅으로 추정, 미확인. 그 뒤로는 끝까지 **3.5초를 넘는 큐 간격이 없다**(최대 3.43초: 11:04, *"log a coding CLI in with an API key"* 문장 중간). 마지막 큐는 **12:30.7 시작(4초)** 의 *"then a rules file, and review comes"* 로 **문장 중간에서 끝난다** — 영상 길이 12:33(753초)과 맞물리므로 자막 누락이 아니라 **영상 자체가 문장 중간에 끝나는 것**으로 보인다(Tech Bridge 편집 여부 미확인). 맺음말 · 구독 권유는 없다.
>
> **화자 · 원 제작자.** **발화에 이름이 없다.** **설명란**(*"Rob Shocks가 Claude Code와 클라우드 코딩 에이전트에 일을 맡기고 결과를 검증하는 구성을 소개합니다"*)에만 Rob Shocks가 나온다 — info.json `tags`(AI 에이전트 · Claude Code · Cursor · Grok Bot · 소프트웨어 개발 · 코딩 에이전트)에는 없다. 발화 단서는 **1인칭 채널 화법**이다: *"I covered a lot of that in Entropic's SDLC in a video while back"*(00:34~00:38), *"some of her skills we covered on Pystack in another video previously"*(03:31~03:34), *"In one of our videos"*(04:22~04:24), *"You can also see that in my last video."*(06:30~06:33), *"for my own factory, I have bots set up for each area of my company"*(07:00~07:05), *"I use very same setup for this channel"*(08:48~08:52). → **원 제작자 · 발표자 Rob Shocks(설명란 근거), 원본 채널명 · 원본 링크 없음.** 목소리 동일성은 확인하지 않았다. ⚠️ 자기 언급이 가리키는 두 영상(Anthropic SDLC 해설 · Pstack 리뷰)은 이 위키에 이미 **화자 미상**으로 있다(09-04 [[tech-bridge-ai-native-sdlc]] — Switch Dimension 강사 익명, 09-13 [[tech-bridge-pstack-third-party-review]] — Molten Base 제작자 익명). 같은 사람일 **가능성**만 있고 확인하지 않았다.
>
> ⚠️ **세 층의 주장 — Lauren Tan(발표자 전달) · Anthropic 등 회사(발표자 전달) · 발표자 자기 구성.** Lauren 쪽(*"Lauren has a post exactly on this"* 01:38~01:41, *"Here's Lauren's daily loop"* 02:57~03:00, *"Lauren's answer to this is what she calls the inverse pyramid"* 05:11~05:15)은 **글 · 영상의 2차 요약**이고 원 글은 링크되지 않았다(설명란의 x.ai *Grok Bot for Engineering* 가이드가 그 글인지 미확인 — 열어 보지 않았다). Anthropic 쪽(녹색 · 노랑 · 빨강 blast radius, 6~9월 수치, *"We didn't remove review…"*)도 출처 미발화이고 설명란 링크(`claude.dev/blog/solving-code-review-at-anthropic/`)는 **열어 보지 않았다.** Alan Wells · Theo · Docker 참조 아키텍처 · *"Stripe, Vercel"* 은 한 문장씩의 전달이다.
>
> **시점.** 업로드일 ≠ 녹화일. 내부 단서: *"Opus 5.5 helping with visuals"*(08:50~08:53) — 이 위키의 Opus 5.5 첫 등장(백악관 패널 편) 이후, *"From June to September"*(06:18) 수치를 과거로 말함 → **9월 이후**, Docker 등의 참조 아키텍처를 *"just published"*(11:29~11:31), Theo의 시도는 *"on the nightly build and it's very early"*(09:23~09:24). 정확한 녹화일은 미상.
>
> ⚠️ **ASR 판독.** *"GrokBot"* · *"Grokbot"* · **"Rockbot"**(07:26~09:38 구간) → [[grokbot|GrokBot]]. **"Crusher"**(01:15 · 01:29) → Cursor. **"Entropic"**(00:36) → Anthropic. **"Cloud Code"**(02:17 · 02:36 · 08:14 · 08:42 · 08:46) → Claude Code(문맥상 *"subscription"* · *"headless"*), 단 *"cursor cloud agent"* · *"Cursor Cloud Agents"* · *"the Cloud Agents"*(08:59)는 클라우드 에이전트. **"Claude agents"**(01:47) → cloud agents 추정(*"have their own computer"* 와 짝). **"Pystack"**(03:33) → [[pstack|Pstack]]. **"play route"**(03:42~03:43) → Playwright. **"pros"**(06:02) → prose(규칙 파일 층). **"Adi Esmany from Anthropic"**(04:35~04:36) → [[addy-osmani|Addy Osmani]]. **"Rice scoring"**(09:41) → RICE. *"linear"* → Linear. *"Open Code"*(02:38) → OpenCode. *"complains to command on X"*(10:17~10:18) — **판독 불가**(X의 불만 · 댓글을 모은다는 뜻으로 추정). *"every worker get its own computer"*(02:42) 그대로.
>
> ⚠️ **ko(기계 번역)는 인용 근거가 아니고 뜻을 바꾸는 곳이 많다.** Linear를 *"선형"*(00:45), pull request를 *"추출 요청"*(03:26 · 03:38), Anthropic을 *"인류학"*(04:37), `Claude.md`를 *"claw.md"*(06:04), 규칙 파일 층 *"pros"* 를 *"장점"*(06:02), *"it's the one that doesn't scale"* 을 *"크기 측정 없음"*(06:15)으로 옮긴다. **시작 규칙의 핵심 *"Hand it to a coding agent"* 를 *"일정 담당자에게 전달하세요"*(12:18)**, 마지막 *"review"* 를 *"개정"*(12:32)으로 옮긴다. Lauren을 가리키는 *"she"* 를 *"그"* · *"그는"* 으로 옮기는 곳이 있다(10:16 등).
>
> ⚠️ **수치 · 제품 진술은 모두 발표자 전달이다.** Anthropic: *"From June to September, their merged pull requests to Claude code more than doubled. And the share that they had to revert fell by more than 40%."*(06:18~06:26). Alan Wells: 3인 팀, 신규 제품 작업 약 6주 중단(06:46~06:56). Lauren: 깨끗하면 *"auto merges after an hour unless she asks for changes"*(03:56~04:00). 제품: *"Grokbot runs on one weekly usage pool that's shared with Grok and Cursor. They have a unified plan now."*(02:22~02:28), *"Rockbot has evolved to store all your credentials."*(07:26~07:28), *"All of your Grokbots share one cloud computer"*(10:56~10:59). **위키는 어느 것도 확인하지 않았다.** ⚠️ 마지막 진술은 이 위키의 이전 소스(*"Every Grok Bot comes with its own virtual computer"* — 10-30 [[tech-bridge-dan-martell-grokbot-daily-automation]])와 **충돌한다**.

## 설명란

Grok Bot을 코딩 담당이 아닌 매니저로 쓰면 어떤 작업 흐름을 만들 수 있을까요? Rob Shocks가 Claude Code와 클라우드 코딩 에이전트에 일을 맡기고 결과를 검증하는 구성을 소개합니다.

로런 탄의 일상적인 작업 루프와 자동 병합의 조건, 코드베이스와 테스트를 중심으로 쌓는 신뢰 체계, 원본 제작자의 백로그 관리와 보안상 주의점을 살펴봅니다.

00:00 소개
00:21 봇은 매니저, 코딩은 에이전트
02:55 로런의 다섯 단계 작업 루프
04:48 신뢰를 쌓는 역피라미드
06:09 사람의 리뷰와 검증 투자
07:00 한 대화창에서 여러 봇 관리
09:27 백로그와 변경 영향 범위
10:53 보안과 첫 번째 운영 규칙

관련 자료
Grok Bot for Engineering: https://x.ai/bot/guides/grok-bot-for-engineering
Pstack: https://github.com/cursor/plugins/tree/main/pstack
Anthropic의 코드 리뷰: https://claude.dev/blog/solving-code-review-at-anthropic/

#GrokBot #ClaudeCode #AI에이전트 #코딩에이전트 #소프트웨어개발

> info.json `tags`: AI 에이전트 · Claude Code · Cursor · Grok Bot · 소프트웨어 개발 · 코딩 에이전트

## 트랜스크립트 — en-orig (원음 영어 ASR — 인용 근거)

[00:21] Your bot should be the manager here, not
[00:23] the coder. So, GrokBot is really good at
[00:25] two different jobs. The first is what
[00:27] the Grok team call the first mile. And
[00:29] this is working out what to build. A big
[00:32] part of any software factory is managing
[00:34] intent. I covered a lot of that in
[00:36] Entropic's SDLC in a video while back if
[00:38] you want to take a look. What Grok is
[00:40] good at is being connected to multiple
[00:42] different channels to manage intent. So,
[00:44] that's Slack, email, X, linear, and it
[00:48] can manage and connect all those and
[00:49] keep an eye on them itself. This is
[00:51] really useful for having a big picture
[00:54] on what should be built next, if there's
[00:55] any issues, and having an idea of the
[00:58] full conversation involved in feature
[01:00] development. The second is the last
[01:02] mile, which is checking the work. So,
[01:04] chasing up on it, telling you what's
[01:06] done, keeping an eye on the task list.
[01:09] Now, just to note here, you don't have
[01:10] to use GrokBot as your orchestrator. You
[01:13] can actually set up your own agents or
[01:15] use Claude projects or use Crusher
[01:17] projects, anything like that will work
[01:19] in a similar fashion. Anything I'm
[01:21] talking about here can be transferred to
[01:22] your own workflow.
[01:24] The bit in the middle really is doing
[01:26] the work, writing the code. And that's
[01:27] what coding agents like Claude code,
[01:29] Codex, and Crusher are really built for.
[01:31] So, in this workflow, you would let
[01:33] GrokBot plan and hand the job off. It
[01:35] can check the proof whenever it comes
[01:37] back and keep you abreast of what's
[01:38] happening. So, Lauren has a post exactly
[01:41] on this. It's basically about making a
[01:43] team engineer bot. Then you add it to
[01:45] Slack and tag it whenever you want some
[01:47] coding done. Because Claude agents or
[01:50] even agents running on your machine have
[01:51] their own computer, it frees up your
[01:53] main orchestrator bot to be more of a
[01:55] manager rather than going and writing
[01:56] the code itself. It's interesting to
[01:58] note in all these software factories
[02:00] I've covered from lots of the big
[02:01] companies like Stripe, Vercel, etc. They
[02:04] all tend to use Slack as their way of
[02:07] managing their agents. So, in this
[02:08] workflow, you either just work directly
[02:10] with Grokbot itself, or you can connect
[02:12] Grokbot to Slack and manage it from the
[02:14] thread where the rest of your team might
[02:15] work. So, I much prefer to use my Cloud
[02:17] Code subscription or my Cursor Cloud
[02:19] agents to do the actual work. And from
[02:22] the money side, Grokbot runs on one
[02:24] weekly usage pool that's shared with
[02:26] Grok and Cursor. They have a unified
[02:28] plan now. You're going to burn through
[02:30] your credits or your quota pretty quick
[02:32] if you're using Grok to do all of the
[02:34] coding work. I much prefer offload to
[02:36] the subscription that I have with Cloud
[02:38] Code or Open Code. Splitting the work
[02:40] also gives you isolation because every
[02:42] worker get its own computer, its own
[02:44] context, and its own kill switch.
[02:46] I've got environments set up locally in
[02:48] containers on my Mac. I've got
[02:50] environments set up on a VPS, and
[02:53] Grokbot is able to work with all of
[02:54] these. Okay, so what does it look like
[02:56] when someone runs this kind of workflow
[02:57] every day? Here's Lauren's daily loop,
[03:00] and it's five steps. So, one is to watch
[03:02] a Slack channel for feedback about the
[03:04] app. You've got a channel created for
[03:06] your team on a particular topic, and
[03:08] somebody's dumping in context about that
[03:10] particular app. Grokbot picks up on that
[03:13] and creates a ticket in linear. Next up,
[03:15] from linear or Jira or whatever, a
[03:17] Cursor Cloud agent is triggered to go
[03:20] and reproduce the issue on its own
[03:21] computer. So, step four, it reproduces
[03:24] the bug, and then it puts up what she
[03:26] calls a fix and fuzz pull request with a
[03:28] small swarm of agents. So, fix and fuzz
[03:31] relates back to some of her skills we
[03:33] covered on Pystack in another video
[03:34] previously. This is where a swarm of
[03:38] agents will open the pull request and
[03:40] try and break it. So, that's either by
[03:42] randomly clicking around or using play
[03:43] route or something like that to verify
[03:46] that the fix is correct user like a user
[03:48] would to make sure nothing breaks. This
[03:50] is why verification is huge in terms of
[03:52] these steps. So, step five, if the fuzz
[03:55] is clean, it will just ping her on
[03:56] Slack, and then it goes and auto merges
[03:59] after an hour unless she asks for
[04:00] changes. Now, one thing to add here, if
[04:02] you look at how Anthropic approach this,
[04:04] you wouldn't apply this to every single
[04:06] type of bug or issue. You'd have green,
[04:09] yellow, and red in terms of blast
[04:11] radius. If something is highly critical,
[04:13] if it deals with payments, you're not
[04:14] going to have it auto merge in the step.
[04:16] You want every human step in. But, a lot
[04:18] of bugs, a lot of small fixes, a lot of
[04:20] non-critical tasks can work in this kind
[04:22] of a workflow. In one of our videos, she
[04:24] also says she's not really a fan of the
[04:26] term software factory. She uses the
[04:28] analogy of a Michelin kitchen. And in
[04:31] her words, as developers, we're still
[04:33] responsible for the final outcome. And
[04:35] that's a concept that Adi Esmany from
[04:36] Anthropic also doubles down on. So, with
[04:39] agents, you're basically the head chef.
[04:41] You no longer cook all the dishes
[04:43] yourself, but it's still your name on
[04:45] every single plate that goes out, even
[04:47] if you have a team working for you. Big
[04:48] part of your Michelin kitchen or your
[04:50] software factory is knowing when you can
[04:52] trust what the agent has done enough to
[04:54] merge it. Okay, so let's cut through
[04:56] some of the hype. So, what we can learn
[04:58] is the few companies that are working in
[05:00] a pure software factory methodology are
[05:03] not doing it by adding more and more
[05:05] agents. What they're doing is starting
[05:06] with the raw infrastructure and trust.
[05:09] Because, how can you manage 50 agents if
[05:11] you can't even trust one? So, Lauren's
[05:13] answer to this is what she calls the
[05:15] inverse pyramid. There are four levels,
[05:17] and you want to put most of your effort
[05:18] at the top. So, number one is the code
[05:21] base level. So, that's better
[05:22] architecture, stronger typing, clear
[05:24] boundaries. Her exact line on this is
[05:27] that agents love to copy what exists and
[05:30] take the shortest path. So, make the
[05:32] easy thing the right thing. So, number
[05:35] two is static analysis. So, that means
[05:38] the traditional deterministic tests that
[05:39] we used to run long before agents came
[05:41] along. So, lint rules, tests, continuous
[05:44] integration CI. If you're finding that
[05:46] your agent keeps making the same
[05:48] mistakes over and over, you turn this
[05:50] into a deterministic lint rule. So,
[05:52] essentially, if you're tidying up after
[05:54] the agent every single time on the same
[05:56] issues, you're doing something wrong.
[05:58] That needs to be programmed in so that
[06:00] it doesn't happen again. Number three is
[06:02] pros. So, that's rule files. That's
[06:04] going to be your agents.md, your
[06:05] Claude.md, your skills, your bug bot,
[06:08] your security bot. And then number four,
[06:10] right at the bottom, is human review.
[06:12] It's the one most of us lean on the
[06:14] hardest. And again, it's the one that
[06:15] doesn't scale. Over at Anthropic,
[06:17] they're seeing a similar thing. From
[06:18] June to September, their merged pull
[06:20] requests to Claude code more than
[06:22] doubled. And the share that they had to
[06:23] revert fell by more than 40%. So, yes,
[06:27] they were doing double the amount of
[06:28] pull requests, but these pull requests
[06:29] were actually working. They were
[06:30] landing. They weren't breaking. You can
[06:32] also see that in my last video. And
[06:33] their line on this is, "We didn't remove
[06:35] review, but we did move most of the
[06:37] review reading to machines." So, all of
[06:39] the companies that I have covered admit
[06:41] that getting to this point of trust
[06:43] takes real work up front. For example,
[06:46] Alan Wells runs a team of three to get
[06:48] his factory shipping pull requests
[06:50] without human code review. They stopped
[06:52] all new product work for about 6 weeks
[06:54] just to build all the validation in. He
[06:57] says it was very painful in the moment,
[06:58] but totally worth it. Okay, so for my
[07:00] own factory, I have bots set up for each
[07:03] area of my company. And I've tried my
[07:05] very best not to create 50 different
[07:07] bots here because the overhead of
[07:09] managing them becomes too much. In an
[07:10] ideal world, I'd have one agent to chat
[07:13] with. And that's what my main agent
[07:15] Chief is for. He delegates and works
[07:17] with other bots. And you can even set up
[07:18] group chats so bots can chat to each
[07:20] other. Each one of my bots then has
[07:21] narrow permissions about what it
[07:23] connects to so that I can share those
[07:25] with other people if I need to. Now,
[07:26] Rockbot has evolved to store all your
[07:28] credentials. I don't know how
[07:29] comfortable I feel about this. A lot of
[07:30] what Rockbot does is it basically
[07:32] abstracts a lot of the complexity. But I
[07:35] kind of miss being able to see what
[07:36] memories are being stored, what skills,
[07:38] um how my vault is being managed. For me
[07:41] to continue trusting Rockbot as we move
[07:43] forward, I'm going to want to see more
[07:45] of that. But for now, I'm happy to take
[07:47] the risk with Rockbot and experiment on
[07:49] the edge of what's possible just so I
[07:50] can share it with you guys. So, let's
[07:52] take one project, for example, my
[07:53] marketing site. I chat with Chief and it
[07:55] spins up either a cursor cloud agent or
[07:58] a Claude code instance on my Mac. I also
[08:00] have it connected to my VPS. It's really
[08:02] very simple in terms of setup. You're
[08:03] basically just prompting Rockbot for the
[08:05] connection and letting it know how you'd
[08:07] like it to run. So, in this case, I've
[08:08] told Rockbot that I want you to run this
[08:10] on Cursor Cloud Agents with certain
[08:12] criteria. Or if I'm running instances of
[08:14] Cloud Code, I'm always specifying the
[08:16] the default model that should be used.
[08:17] Rockbot just basically saves this to a
[08:19] skill somewhere. Again, I can't see
[08:20] where that skill is, but it just seems
[08:22] to work fine for me. If you're
[08:23] uncomfortable with this level of control
[08:25] and not seeing your skills, of course
[08:26] you can set up your own agents to do
[08:28] something similar as Rockbot. I guess
[08:29] what I love about Rockbot is I have it
[08:31] on my phone, it works so easy. I got it
[08:33] on my Mac as a desktop, I've got it on a
[08:34] separate PC machine, and they're all
[08:36] able to coordinate together. You could
[08:38] do the same with something like
[08:39] Tailscale. So, in each folder or
[08:40] environment, whether that's Cursor CLI
[08:42] or Cloud Code, I have my own set of
[08:44] permissions and rules for security. So,
[08:46] then Rockbot will kick off Cloud Code
[08:48] headless with the model that I picked. I
[08:50] use very same setup for this channel
[08:52] when I'm having Opus 5.5 helping with
[08:53] visuals. It spins up multiple different
[08:55] agents and records different terminal
[08:57] clips. So, because Rockbot is acting as
[08:59] the orchestrator for the Cloud Agents or
[09:01] the machine agents, it's able to make
[09:03] certain decisions without my input. It's
[09:05] connected to my Slack, it's connected to
[09:07] multiple other different documentation
[09:09] sources. So, it can unblock these
[09:10] sub-agents in any questions that we they
[09:13] have. So, Theo is trying out a similar
[09:15] workflow with T3 Code. He documented
[09:17] some of it in a tweet. He's saying he
[09:18] can now drive his whole fleet of
[09:20] machines from Rockbot. Now, it's on the
[09:23] nightly build and it's very early, but
[09:24] you can kind of see where this is going.
[09:27] So, everything Chief picks up from Slack
[09:29] or my conversations basically goes into
[09:31] a backlog. And I get Rockbot to save all
[09:34] of that to Notion. You can use anything
[09:35] like Linear or Jira as well. I've set up
[09:38] a another routine with Rockbot to triage
[09:41] the backlog with Rice scoring. So,
[09:43] that's the reach, impact, confidence,
[09:45] and effort of each issue or feature that
[09:48] needs to be worked on. And I also have a
[09:50] blast radius score as well. So, with
[09:52] this setup, a small job that helps a lot
[09:54] of people rises to the top over a more
[09:57] over a minor fix. And it'll often
[09:59] suggest new improvements as well. Just
[10:01] ask the bot to be proactive about what
[10:03] to do next. But don't just do this for
[10:05] the sake of doing it because it'll
[10:06] quickly fill up your backlog with tasks
[10:08] just for the sake of it. So, Lauren does
[10:10] something similar in terms of
[10:12] improvement. She uses Grokbot routines
[10:14] to farm context from bug reports on
[10:17] Slack and then complains to command on
[10:18] X, and then she feeds that into what she
[10:20] calls her outer loop. Now, just a word
[10:22] of warning, that's something fine for
[10:24] someone like Lauren who has a ton of
[10:26] inference and credits to throw at these
[10:28] kind of things. If you're doing
[10:29] something similar like this yourself on
[10:31] an hourly schedule, you're going to burn
[10:32] a ton of tokens. So, one other thing I
[10:34] mentioned I do is I mark every change by
[10:37] blast radius or at least I don't, I get
[10:38] the agent to do that, which is how much
[10:40] could break if this goes wrong. You can
[10:42] get the agent to define the level of
[10:44] criticality, so the review level,
[10:46] whether that's human, AI level 1, 2, or
[10:48] 3, and this involves various different
[10:50] levels of playwright testing and
[10:52] security testing. The last thing you
[10:54] need to do in terms of trust is lock the
[10:56] doors. All of your Grokbots share one
[10:59] cloud computer, that's including files,
[11:00] browser sessions, command line
[11:02] credentials. So, be careful here. If you
[11:04] log a coding CLI in with an API key on
[11:07] one of Grokbot's computers, every bot
[11:10] you have can use that key. So, I'll be
[11:12] the first to say there's something
[11:13] really enticing and powerful about
[11:16] simply connecting a lot of your tools
[11:17] and giving your agents access to all of
[11:20] your workflows. There's a beautiful
[11:22] speed in moving fast and breaking
[11:24] things, but inevitably that will come
[11:26] back and bite you in the butt. If you're
[11:27] interested, Docker and a group of
[11:29] security companies just published a
[11:31] secure software factory reference
[11:33] architecture, and the central idea is
[11:35] this: the more autonomy you give the
[11:37] agent, the less you can rely on it to
[11:39] police itself. The controls have to live
[11:41] in the environment. I 100% agree with
[11:43] this. So, in practice, that means
[11:46] running your agents in a sandbox, giving
[11:48] them scoped credentials, read only where
[11:50] you can, and letting them open pull
[11:52] requests but not merge them, at least
[11:54] until you trust the stack that's in
[11:55] place. Now, Grokbot as an orchestrator
[11:57] isn't going to solve all those problems.
[11:59] These are decisions you need to make in
[12:01] each of the codebases that you have set
[12:02] up based on their criticality. Okay, so
[12:04] if you want to start on this, my advice
[12:07] is don't go building 50 agents. Start
[12:09] with one loop and paste this rule into
[12:12] your bot. So, here's a basic rule you
[12:14] want to pass to Grokbot. For anything
[12:16] more than a short question, don't write
[12:18] the code yourself. Hand it to a coding
[12:20] agent with an acceptance test, check the
[12:22] proof, open a pull request, and report
[12:24] back. Then, every time you have to
[12:26] correct an agent, move that fix up the
[12:28] stack, code first, then a lint rule,
[12:30] then a rules file, and review comes

## 트랜스크립트 — ko (`tlang=ko` 기계 번역 — 참고용, 인용하지 않음)

[00:21] 여기서 관리자는 봇이어야지, 다른 사람이어서는 안 됩니다.
[00:23] 프로그래머. 그래서 GrokBot은
[00:25] 두 가지 일을 정말 잘해요
[00:26] 다른. 첫 번째는 무엇인가
[00:27] 그록의 팀이 첫 1마일을 중계합니다. 그리고
[00:29] 이는 무엇을 결정하는 것을 포함합니다.
[00:31] 짓다. 어떤 것의 상당 부분
[00:33] 소프트웨어 팩토리가 관리하고 있습니다.
[00:34] 의도. 저는 SDLC 과정에서 그 내용을 많이 다뤘습니다.
[00:36] 엔트로픽이 예전에 올린 영상에서 나온 내용입니다.
[00:38] 한번 보시겠어요? 무엇에서
[00:40] Grok은 연결성이 뛰어납니다.
[00:41] 다양한 채널을 위해
[00:43] 의도를 관리합니다. 즉, 슬랙
[00:45] 이메일, X, 선형; ~할 수 있다
[00:47] 이 모든 것을 관리하고 연결합니다.
[00:49] 직접 보세요.
[00:51] 개요를 파악하는 데 매우 유용합니다.
[00:53] 무엇을 건설해야 하는지에 대한 일반적인 내용
[00:55] 다음으로, 문제가 발생했을 경우
[00:57] 전체 대화 내용에 대한 아이디어
[00:58] 개발에 참여함
[01:00] 함수. 두 번째는 마지막 1마일입니다.
[01:02] 이는 해당 작업을 검토하는 것으로 구성됩니다. ~이다
[01:04] 말하다, 후속 조치를 취하다, 무엇이 있는지 알려주다
[01:07] 완료했고 할 일 목록을 계속 주시하세요.
[01:09] 자, 여기서 한 가지 알아두셔야 할 점은, 여러분은 가지고 있지 않다는 것입니다.
[01:11] GrokBot을 오케스트레이터로 사용하려면.
[01:12] 에이전트를 직접 구성할 수 있습니다.
[01:15] Claude 또는 Cursor 프로젝트를 사용하세요.
[01:17] 그런 종류의 것은 어떤 식으로든 효과가 있을 것입니다.
[01:19] 비슷한. 제가 언급하는 모든 것
[01:21] 여기에서 본인 계정으로 전송할 수 있습니다.
[01:22] 워크플로우.
[01:24] 중간 부분이 정말 잘 작동하고 있어요
[01:25] 그 일은 코드를 작성하는 것입니다. 그리고 ~을 위해
[01:27] 그게 바로 그 용도로 설계된 겁니다.
[01:29] 클로드 코드와 같은 코딩 에이전트
[01:30] 코덱스와 커서. 그래서, 이 경우에는
[01:32] 워크플로우에서 GrokBot을 사용하시겠습니까?
[01:34] 업무를 계획하고 위임하십시오. 할 수 있다
[01:35] 돌아오시면 테스트 결과를 다시 검토해 보세요.
[01:37] 무슨 일이 일어나고 있는지 계속 알려드리겠습니다.
[01:39] 로렌은 정확히 같은 게시물을 올렸습니다.
[01:41] 이것에 관해서. 기본적으로, 그것은 ~에 관한 것입니다.
[01:43] 엔지니어링 봇을 제작하세요
[01:44] 장비. 그런 다음 슬랙에 추가하면...
[01:46] 필요할 때마다 라벨을 붙일 수 있습니다.
[01:47] 프로그래밍을 좀 해보세요. 왜냐하면
[01:49] 클로드의 대리인들, 혹은 심지어 그들조차도
[01:50] 그것들은 당신의 컴퓨터에서 실행되고, 그들만의 기능을 가지고 있습니다.
[01:52] 당신의 컴퓨터에서, 그들은 당신의 봇을 풀어놓습니다.
[01:53] 더 나아가기 위한 주요 기획자
[01:55] 글을 쓰는 대신 관리자에게
[01:56] 직접 코딩합니다. 주목할 만한 점은 다음과 같습니다.
[01:59] 이러한 모든 소프트웨어 공장에서
[02:01] 제가 많은 큰 것들을 다뤘습니다.
[02:02] Stripe, Vercel 등의 회사들
[02:04] 그들은 모두 슬랙을 선호하는 경향이 있습니다.
[02:06] 에이전트를 관리하기 위해서입니다. 그래서,
[02:08] 이 워크플로에서는 작업하거나
[02:10] GrokBot을 통해 직접 또는 다음 방법으로
[02:11] GrokBot을 Slack에 연결하여 관리하세요.
[02:13] 나머지 내용이 있는 스레드에서
[02:14] 그 팀은 잘 해낼 수 있을 것이다. 그래서 저는 선호합니다.
[02:16] 제 클로드 코드 구독을 이용하시거나
[02:19] Cursor Cloud 에이전트가 다음을 수행합니다.
[02:21] 진짜 일. 그리고 그 관점에서 보면
[02:23] 경제적인 GrokBot은 펀드를 활용하여 운영됩니다.
[02:24] Grok과 함께 매주 공동으로 사용하고 있습니다.
[02:26] 커서. 이제 그들은 통일된 계획을 세웠습니다.
[02:29] 크레딧이나 할당량이 바닥날 거예요.
[02:31] Grok을 사용하면 꽤 빠르게 할 수 있습니다.
[02:33] 모든 프로그래밍 작업.
[02:35] 저는 그 일을 다른 사람에게 위임하는 것을 훨씬 더 선호합니다.
[02:37] 저는 CloudCode 구독권을 가지고 있습니다.
[02:39] 오픈코드. 업무를 분담하면 다음과 같은 이점도 얻을 수 있습니다.
[02:41] 이는 고립을 초래합니다. 왜냐하면 각 노동자가...
[02:42] 그는 자신만의 컴퓨터를 갖게 된다.
[02:44] 컨텍스트와 그 자체의 스위치
[02:46] 끄다.
[02:46] 로컬에 환경이 구성되어 있습니다.
[02:48] 맥의 컨테이너 안에 있습니다. 나는 가지고 있다
[02:50] VPS에 구성된 환경입니다. 그리고
[02:52] GrokBot은 누구와도 협업할 수 있습니다.
[02:54] 그들. 좋아요, 그럼 누군가가 그럴 때 어떤 모습일까요?
[02:56] 이러한 유형의 워크플로를 실행합니다
[02:57] 매일? 이것이 순환 과정입니다
[02:59] 로렌의 일기이며, 다섯 부분으로 구성되어 있습니다.
[03:01] 단계. 첫 번째는 채널을 모니터링하는 것입니다.
[03:03] Slack은 다음 사항에 대한 피드백을 구하고 있습니다.
[03:04] 해당 애플리케이션. 채널이 생성되었습니다.
[03:06] 팀원들과 함께 논의할 주제는 다음과 같습니다.
[03:08] 개인 소유인데 누군가가 넘어뜨리고 있어요
[03:09] 해당 특정 애플리케이션에 대한 컨텍스트
[03:11] . GrokBot이 이를 감지하고 티켓을 생성합니다.
[03:14] 선의. 다음으로, 선형 또는
[03:16] Jira든 뭐든, 에이전트가 활성화됩니다.
[03:18] 커서 클라우드에서 플레이하러 가세요
[03:20] 본인 컴퓨터에서 발생하는 문제입니다. 그래서
[03:22] 네 번째 단계에서는 오류가 재현됩니다.
[03:24] 그런 다음 그녀는 자신이 '라고 부르는 것'을 출판합니다.
[03:26] "Fix and Fuzz" 추출 요청
[03:28] "소규모 요원 무리와 함께."
[03:30] 그래서 "fix and fuzz"는 서로 관련이 있습니다.
[03:31] 그의 몇 가지 기술을 활용하면
[03:33] Pystack에 대해서는 다른 영상에서 다뤘습니다.
[03:34] 이전에.
[03:36] 이곳은 에이전트 무리가 활동하는 곳입니다.
[03:38] 추출 요청을 열고
[03:40] 부숴보려고 해봐. 그것은 하는 것 중 하나입니다.
[03:42] 아무 데나 무작위로 클릭하거나 다음을 사용하세요
[03:44] 극작가 또는 이와 유사한 자격을 증명할 수 있는 사람
[03:45] 해결책이 옳다는 것은 다음과 같습니다.
[03:47] 사용자는 어떻게 해야 확실히 알 수 있을까요?
[03:49] 아무것도 고장나지 않아요. 이것이 바로 그 이유입니다
[03:51] 이러한 과정에서 검증은 필수적입니다.
[03:52] 단계. 5단계, " 테스트가 실패하면
[03:55] "Fuzz"는 깨끗하며, 알림을 보내드립니다.
[03:56] Slack을 사용하면 병합됩니다.
[03:58] 한 시간 후에 자동으로
[03:59] 그녀가 변경을 요청하지 않는 한. 자, 이제 뭔가를
[04:01] 인류의 모습을 살펴보면 제가 더 덧붙일 말이 뭐가 있겠습니까?
[04:04] 이 문제를 해결하기 위해 모든 경우에 이 방법을 적용해서는 안 됩니다.
[04:06] 오류 또는 문제 유형. 초록색이 될 거예요
[04:09] 반지름 기준으로 노란색과 빨간색
[04:10] 영향. 만약 어떤 것이 매우 중요하다면
[04:12] 마치 지불하는 것처럼, 당신은 그렇게 하지 않을 겁니다.
[04:14] 자동으로 병합되도록 허용합니다
[04:15] 그 단계에서. 당신은 모든 인간을 원합니다
[04:17] 개입하다. 하지만 많은 실수들, 많은
[04:19] 사소한 수정과 많은 작업
[04:20] 이런 유형에서는 비판이 효과적일 수 있습니다.
[04:22] 워크플로우. 우리 중 한 명
[04:24] 영상에 대해 그녀는 또한 그것이 그다지 좋지 않다고 말합니다.
[04:25] '소프트웨어 공장'이라는 용어에 광적으로 집착하는 사람
[04:27] . 그녀는 부엌을 비유로 사용합니다.
[04:30] 미슐랭. 그리고 그의 말에 따르면,
[04:31] 개발자 여러분, 저희는 여전히
[04:33] 최종 결과에 대한 책임이 있습니다. 그리고 그것은
[04:35] 이는 아디 에스마니가 제시한 개념입니다.
[04:37] 인류학 또한 그렇게 주장합니다. 그래서,
[04:38] 에이전트들과 함께라면, 당신은 기본적으로 다음과 같은 존재가 됩니다.
[04:40] 수석 셰프. 당신은 이제 매일 요리하지 않잖아요.
[04:42] 요리는 직접 하셔도 되지만, 그래도 여전히 당신의 것입니다.
[04:44] 나오는 모든 음식에 이름이 적혀 있어요, 심지어
[04:46] 만약 당신에게 팀이 있다면.
[04:48] 미슐랭 스타 주방의 상당 부분 또는
[04:50] 귀사의 소프트웨어 개발 공장은 알고 있습니다
[04:51] 충분히 신뢰할 수 있을 때
[04:53] 에이전트가 한 일
[04:54] 병합하세요. 좋아요, 하나 제거해 봅시다.
[04:56] 과장된 열정은 거의 없었다. 어느
[04:58] 우리가 배울 수 있는 것은 소수의 사람들이
[04:59] 협력하는 회사
[05:01] 순수 소프트웨어 팩토리 방법론
[05:03] 그들은 요원을 점점 더 많이 추가하는 방식으로 그렇게 하지 않습니다.
[05:05] . 그들이 하고 있는 일은 다음과 같이 시작하는 것입니다.
[05:07] 기본 인프라 및 신뢰
[05:09] . 50명을 어떻게 감당할 수 있겠어요?
[05:10] 에이전트를 믿을 수 없다면, 그들을 신뢰하지 마세요.
[05:12] 하나? 그래서 로렌의 대답은 다음과 같습니다.
[05:14] 이것이 그녀가 피라미드라고 부르는 것이다.
[05:15] 반전됨. 총 네 단계가 있으며, 여러분은 반드시
[05:17] 노력의 대부분을 여기에 쏟으세요
[05:18] 윗부분. 첫 번째는
[05:20] 코드베이스 수준. 즉,
[05:22] 더 나은 아키텍처, 더 강력한 타입 지정 및
[05:24] 명확한 경계. 그가 정확히 표현한 내용은 다음과 같습니다.
[05:27] 이건 에이전트들이 아주 좋아하는 점입니다.
[05:29] 기존 것을 복사하고 그 길을 따라가세요
[05:31] 더 짧은. 그러니 쉽게 만드세요
[05:33] 옳은 것.
[05:34] 두 번째는 정적 분석입니다.
[05:37] 즉, 결정론적 테스트를 의미합니다.
[05:38] 우리가 예전에 운영했던 전통적인 것들
[05:40] 훨씬 이전에
[05:41] 자치령 대표. 린트 규칙, 테스트,
[05:43] 지속적 통합(CI).
[05:46] 담당 에이전트가 여전히 연락이 닿지 않는다는 사실을 알게 되면
[05:47] 같은 실수를 계속해서 반복하는 것
[05:49] 다음으로, 이를 린트 규칙으로 변환하세요.
[05:51] 결정론적.
[05:52] 기본적으로, 만약 당신이 고치고 있다면
[05:54] 에이전트의 문제점은 점점 더 다음과 같은 이유로 발생하고 있습니다.
[05:56] 같은 주제인데 뭔가 잘못하고 있는 거예요.
[05:58] 그렇게 되지 않도록 프로그래밍해야 합니다.
[06:00] 이런 일이 다시 발생할 수도 있습니다. 숫자 3은 "
[06:02] 장점. 즉, 규칙 파일입니다. 저것
[06:04] 여러분의 agents.md, claw.md, 그리고 여러분의 계정이 될 것입니다.
[06:06] 스킬, 버그봇, 봇
[06:08] 보안. 그리고 네 번째는,
[06:10] 가장 근본적인 것은 인간의 검토입니다.
[06:12] . 그것은 우리 대부분이 경험하는 것입니다.
[06:13] 우리는 서로를 더욱 지지합니다. 그리고 다시 한번, 바로 그녀입니다.
[06:15] 크기 측정 없음. 앤트로픽에서는 상황을 주시하고 있습니다.
[06:17] 비슷한 것. 6월부터 9월까지, 그들의
[06:19] 병합 요청(풀 요청)
[06:21] 클로 코드(Claw code)는 두 배 이상 증가했습니다. 그리고
[06:23] 그들이 역전시켜야 했던 비율
[06:25] 40% 이상 하락했습니다. 네, 그랬습니다.
[06:27] 두 배 더 많은 요청을 하다
[06:28] 융합이지만, 이것들은 실제로 효과가 있었습니다.
[06:30] . 그들은 성공을 거두고 있었다. 그들은 깨지지 않았다
[06:32] . 마지막 영상도 시청하실 수 있습니다. 그리고
[06:33] 그들의 입장은 다음과 같습니다. "우리는 제거하지 않습니다."
[06:35] 검토는 했지만, 우리는 가장 큰 것을 옮겼습니다.
[06:37] 리뷰 읽기의 일부는 다음과 같습니다.
[06:38] 기계들." 제가 가진 모든 회사들
[06:40] 취재진들은 이 지점에 도달하기까지 여러 단계를 거쳤다고 인정합니다.
[06:42] 신뢰를 구축하려면 진정한 노력이 필요합니다.
[06:44] 처음부터. 예를 들어, 앨런
[06:46] 웰스는 세 명으로 구성된 팀을 이끌고 있습니다.
[06:48] 귀사 공장에서 요청을 보낼 수 있도록
[06:49] 인간의 검토 없이 추출
[06:51] 암호. 그들은 모든 작업을 중단했다
[06:53] 약 6주간의 신제품
[06:55] 모든 유효성 검사를 통합하기 위해서입니다.
[06:57] 그는 당시 매우 고통스러웠다고 말합니다.
[06:58] 잠깐이었지만, 그럴 만한 가치가 충분히 있었어요.
[06:59] 고통. 네, 제 공장을 기준으로 말씀드리자면,
[07:01] 각 영역별로 봇을 설정해 두었습니다.
[07:03] 저희 회사에서 제공하는 정보입니다. 그리고 저는 노력해 왔습니다.
[07:05] 서로 다른 봇을 50개 이상 만들지 않는 경우 최대 허용량
[07:07] 여기서는 업무량이 많기 때문입니다.
[07:09] 그것들을 관리하는 것은 과도한 부담이 된다. 에서
[07:10] 이상적인 세상이라면, 저는 단 한 명의 에이전트와 함께 일하고 싶습니다.
[07:12] 채팅하는 사람. 그리고 그게 바로 제가 원하는 거예요
[07:14] 주임 대리인, 책임자. 그는 위임하고
[07:16] 다른 봇들과도 연동됩니다. 그리고 당신은 심지어
[07:18] 그룹 채팅을 다음과 같이 구성합니다.
[07:19] 봇들은 서로 대화할 수 있습니다. 각각의
[07:21] 내 봇들은 제한된 권한을 가지고 있습니다.
[07:22] 무엇에 연결되는지, 그래서 그것이 할 수 있도록
[07:24] 다른 사람들과 공유하세요.
[07:25] 필요한. 이제 Rockbot은
[07:26] 모든 것을 저장하도록 진화했습니다.
[07:28] 신임장. 내가 얼마나 편안할지는 잘 모르겠어.
[07:29] 이 일에 대해 유감스럽게 생각합니다. 많은 것들
[07:31] Rockbot이 하는 일은 기본적으로 추상적인 것입니다.
[07:33] 복잡성의 상당 부분. 하지만 저는 무언가를 그리워합니다.
[07:35] 나는 어떤 기억들이 떠오르는지 거의 볼 수 없다.
[07:37] 저장, 어떤 기술, 어, 어떻게
[07:39] 내 금고가 관리되고 있습니다. 계속하려면
[07:41] Rockbot을 신뢰하는 것
[07:43] 우리는 앞으로 나아가고 있고, 저는 앞으로 더 많은 그런 모습을 보고 싶습니다.
[07:46] 하지만 지금으로서는 기꺼이 그 일을 맡겠습니다.
[07:47] Rockbot을 사용한 실험의 위험성
[07:49] 가능한 것의 한계는 단지 할 수 있다는 것뿐입니다.
[07:50] 당신과 공유하고 싶어요. 그래서,
[07:52] 예를 들어 제 프로젝트를 하나 들어보겠습니다.
[07:53] 마케팅 사이트. 서장님과 채팅하세요
[07:55] 이는 커서 에이전트를 시작합니다.
[07:57] 내 클라우드 또는 클로 코드 인스턴스
[07:59] 스코틀랜드 사람. 저도 VPS에 연결해서 사용하고 있습니다.
[08:01] . 사실 그 점은 아주 간단합니다.
[08:03] 구성. 기본적으로 그는 그냥...
[08:04] Rockbot에게 연결을 요청하면 됩니다.
[08:06] 어떻게 구현되기를 원하시는지 알고 있습니다.
[08:08] 그래서 이 경우에는 제가 이렇게 말했습니다.
[08:09] Rockbot, 이 파일을 실행해 주세요.
[08:10] 특정 Cursor Cloud 에이전트
[08:12] 기준. 아니면 제가 달리고 있다면
[08:13] 클라우드 코드 인스턴스는 항상
[08:15] 저는 기본 모델을 지정합니다.
[08:16] 사용해야 합니다. Rockbot은 간단히 저장합니다.
[08:18] 이건 분명 어딘가에 있는 기술일 거예요.
[08:19] 다시 말씀드리지만, 저는 그게 어디 있는지 찾을 수가 없어요.
[08:21] 기술이 필요한 건 아니지만, 잘 작동하는 것 같습니다.
[08:22] 나를 위한. 만약 당신이 불편함을 느낀다면
[08:24] 이러한 수준의 통제와 당신을 보지 못하는 것
[08:25] 물론 기술이죠, 할 수 있어요.
[08:27] 에이전트를 직접 구성하세요
[08:28] Rockbot과 비슷한 작업을 해보세요. 제 생각엔...
[08:29] 제가 락봇을 좋아하는 이유는 바로 이것입니다.
[08:31] 제 휴대폰에 설치되어 있는데 아주 잘 작동합니다.
[08:32] 쉽게. 저는 맥에 설치했어요
[08:34] 저는 데스크톱 컴퓨터를 별도의 PC에 설치해서 사용하고 있습니다.
[08:36] 그리고 그들은 모두 서로 협력할 수 있습니다.
[08:38] 다음과 같은 것으로도 똑같이 할 수 있습니다.
[08:39] 꼬리비늘. 그래서 각 폴더마다 또는
[08:41] Cursor CLI든 Cloud Code든 어떤 환경에서든 마찬가지입니다.
[08:43] 저는 저만의 권한 설정을 가지고 있습니다.
[08:45] 안전 수칙. 그래서, 록봇
[08:47] 클라우드 코드는 인터페이스 없이 시작됩니다.
[08:49] 제가 선택한 모델입니다. 저는 정확히 그것을 사용합니다
[08:51] 이 채널에도 동일한 설정이 적용됩니다.
[08:52] Opus 5.5가 나를 도와줄 때
[08:53] 시각적 요소. 여러 개를 시작하세요
[08:55] 에이전트와 기록이 서로 다릅니다.
[08:56] 단자 클립. Rockbot의 작동 방식
[08:59] 클라우드 에이전트의 오케스트레이터로서
[09:01] 또는 기계 에이전트는 취할 수 있습니다.
[09:03] 내 관여 없이 결정된 몇 가지 사항들.
[09:05] 내 슬랙 계정과 다른 여러 계정에 연결되어 있습니다.
[09:07] 기타 문서 자료
[09:09] 다른. 이런 식으로 하면,
[09:10] 이 하위 요원들을 잠금 해제하기 전에
[09:12] 궁금한 점이 있으시면 언제든지 말씀해 주세요. 테오는
[09:14] 유사한 워크플로우를 테스트합니다
[09:16] T3 코드. 그는 그 일부를 기록으로 남겼습니다.
[09:18] 짹짹. 그녀는 이제 모든 일을 처리할 수 있다고 말합니다.
[09:20] 그들의 기계 함대는 록봇(Rockbot)에서 제작되었습니다. 이것
[09:23] 밤에 편집된 영상인데 정말 좋아요.
[09:24] 곧 그렇게 되겠지만, 어디로 향하고 있는지 알 수 있을 겁니다.
[09:26] 이것. Chief가 Slack에서 수집하는 모든 것
[09:29] 또는 제 대화는 기본적으로 다음과 같은 방향으로 흘러갑니다.
[09:31] 밀린 업무. 그리고 저는 락봇이 저장하도록 만듭니다.
[09:33] 이 모든 것을 Notion에서 할 수 있습니다. 하지만 당신은 또한 할 수 있습니다
[09:35] 다른 도구를 사용하세요.
[09:37] Linear 또는 Jira. 제가 하나 더 설치했어요.
[09:38] Rockbot을 사용하여 분류하는 루틴
[09:41] RICE 점수를 사용한 백로그. 즉,
[09:43] 도달 범위, 영향력, 신뢰 및
[09:45] 각 문제 또는 기능에 필요한 노력
[09:47] 개선해야 할 부분입니다. 그리고 또한
[09:50] 저는 라디오 악보를 가지고 있습니다.
[09:51] 터지다. 이 구성에서는 하나가
[09:54] 많은 사람에게 도움이 되는 작은 일
[09:56] 조정치 위로 상승
[09:58] 미성년자. 그리고 종종 새로운 아이디어도 제시해 줍니다.
[10:00] 개량. 봇에게 그냥 요청하세요
[10:02] 다음에 무엇을 해야 할지 적극적으로 계획한다.
[10:04] 하지만 단지 해야 한다는 이유만으로 하지 마세요.
[10:06] 그렇게 하면 밀린 업무가 금방 쌓일 것이기 때문입니다.
[10:07] 불필요한 작업으로.
[10:09] 로렌도 비슷한 방식으로 행동합니다.
[10:12] 개선. Grokbot 루틴을 사용하여
[10:14] 오류 보고서에서 컨텍스트를 추출합니다.
[10:16] 슬랙에서 그는 명령에 대해 불평합니다.
[10:19] X에 넣고 그가 자신의 것이라고 부르는 것에 입력합니다.
[10:21] 외부 고리.
[10:22] 한 가지 경고: 그건 괜찮습니다.
[10:24] 로렌처럼 많은 것을 가진 사람
[10:26] 추론 및 사용 가능한 크레딧
[10:27] 이런 것들.
[10:29] 만약 당신이 비슷한 일을 혼자서 한다면
[10:31] 시간 단위로 계획을 세우면, 당신은 소비하게 될 것입니다.
[10:32] 토큰이 많습니다. 또 다른 것은
[10:34] 제가 하는 일은 변경 사항 하나하나를 표시하는 것이라고 말씀드렸습니다.
[10:36] 폭발 반경에 따라. 혹은 적어도
[10:38] 저는 안 할래요. 담당자에게 맡길게요.
[10:40] 이 사실이 알려지면 그만큼 큰 피해가 발생할 수 있다는 뜻입니다.
[10:42] 사악한. 에이전트가 정의하도록 할 수 있습니다.
[10:44] 임계 수준, 즉 수준
[10:46] 인간 또는 AI 수준의 검토
[10:48] 1, 2 또는 3이며, 이는 여러 단계를 의미합니다.
[10:50] 서로 다른 실행 테스트 및
[10:52] 보안. 당신이 절대 해서는 안 될 일은
[10:55] 신뢰라는 측면에서 보면, 그것은 관계를 끝내는 것입니다.
[10:56] 문. 모든 Grokbot이 공유합니다
[10:58] 클라우드에 있는 컴퓨터, 다음을 포함하여
[11:00] 파일, 브라우저 세션 및
[11:01] 명령줄 자격 증명. 그래서
[11:03] 여기서는 조심하세요. 로그인하시면
[11:05] 프로그래밍 CLI에서 키를 사용하여
[11:07] 컴퓨터 중 한 대의 API
[11:08] Grokbot을 사용하면 보유하고 있는 모든 봇을 활용할 수 있습니다.
[11:10] 그 열쇠요. 그래서 제가 제일 먼저 하겠습니다
[11:13] 정말 매력적인 무언가가 있다고 말하다
[11:15] 많은 것을 연결하는 데 있어 강력한 힘을 발휘합니다.
[11:17] 당신의 도구를 당신에게 주세요
[11:19] 에이전트가 모든 흐름에 액세스할 수 있습니다.
[11:21] 직업. 속도에는 아름다움이 있다.
[11:23] 빠르게 움직여서 물건을 부수지만,
[11:24] 필연적으로 그것은 다시 돌아올 것이고 당신은
[11:26] 엉덩이를 물어뜯을 것이다. 관심 있으시면,
[11:28] Docker와 여러 회사들이 함께
[11:30] 보안 관련 소식이 방금 게시되었습니다.
[11:31] 공장 참조 아키텍처
[11:33] 보안 소프트웨어이며, 핵심 아이디어는 다음과 같습니다.
[11:35] 즉, 자율성을 더 많이 부여할수록
[11:37] 에이전트일수록, 그 사람을 덜 신뢰할 수밖에 없습니다.
[11:39] 자제력을 발휘하세요. 제어 장치는 반드시
[11:41] 환경 속에 존재한다. 저는 100%입니다.
[11:43] 저도 동의합니다. 실제로는,
[11:45] 즉, 에이전트를 특정 환경에서 운영하는 것을 의미합니다.
[11:47] 고립된 환경에서 그들에게 자격을 부여하세요.
[11:48] 제한됨, 읽기 전용
[11:50] 가능하다면, 그들이 애플리케이션을 열 수 있도록 허용하십시오.
[11:52] 추출은 하되 병합은 하지 않음으로써,
[11:54] 적어도 스택을 신뢰할 때까지는요.
[11:55] 구현되었습니다. 이제 Grokbot은 다음과 같습니다.
[11:57] 오케스트레이터가 그 모든 문제를 해결해 줄 수는 없을 겁니다.
[11:58] 문제들. 이것들은 결정 사항입니다
[12:00] 각각의 기본 요소를 고려해야 합니다.
[12:02] 사용자가 설정한 코드
[12:03] 임계점. 좋아요, 그럼 원하시면
[12:05] 우선, 제 조언은 그러지 말라는 것입니다.
[12:07] 당신은 에이전트 50명을 만들 것입니다. 시작
[12:10] 반복문을 사용하여 이 규칙을 봇에 붙여넣으세요.
[12:12] . 자, 기본적인 규칙은 다음과 같습니다.
[12:14] Grokbot에 전달하고 싶은 내용입니다. 을 위한
[12:15] 질문이 아닌 모든 것
[12:17] 간단히 말해서, 코드를 직접 작성하지 마세요.
[12:18] 일정 담당자에게 전달하세요.
[12:20] 인수 테스트를 통해 검증합니다.
[12:22] 테스트는 요청을 엽니다.
[12:23] 결과 추출 및 보고.
[12:24] 그러면 수정할 때마다
[12:26] 에이전트에게, 해당 수정 사항을 다음 방향으로 이동하세요.
[12:28] 스택의 최상단: 코드 우선,
[12:29] 그다음에 린트 규칙, 그다음에
[12:31] 규칙 파일 그리고 마지막으로
[12:32] 개정.
