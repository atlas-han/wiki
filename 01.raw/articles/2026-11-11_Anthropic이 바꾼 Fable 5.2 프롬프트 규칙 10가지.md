---
title: "[한글자막] Anthropic이 바꾼 Fable 5.2 프롬프트 규칙 10가지 (완전 정리)"
type: video
source: https://www.youtube.com/watch?v=UZflKPqs514
site: youtube.com
author:
  - "[[Tech Bridge]]"
duration: 10:22
published: 2026-11-11
created: 2026-11-12
description: "Tech Bridge가 한국어 자막을 붙여 재게시한 Chase AI(Chase)의 10:22 1인 해설, 공식 챕터 13, 영어 원본 오디오만. Anthropic의 Claude Fable 5.2 공식 프롬프트 가이드 · 시스템 카드를 근거로 바뀐 프롬프트 규칙 10가지: 추론 강도 high부터(Frontier Code 2.0 high 45.3% · $6.72 ≈ Opus 5.5 max $12.82, medium 37.6% · $2.48), 결과를 증명하게(추론을 사실로 말함, 없는 파일 지어내기 2%, 지름길 6배), 끝까지 하라고(멈춤 약 절반), 옛 CLAUDE.md · 지침 정리(규칙을 거의 글자 그대로 따름), '생각하지 마'는 안 통함, 단계별 추론 설명 요구는 증류 분류기에 걸림, 코드의 주인을 알려 주면 중복 감소, 서브에이전트 위임은 모델에게, 긴 작업엔 중간 보고(매 호출마다면 토큰 +20%), 말투 · 길이는 강도와 무관."
tags:
  - clippings/youtube
---

**Source URL**: https://www.youtube.com/watch?v=UZflKPqs514
**Channel**: Tech Bridge · **Duration**: 10:22 · **Published**: 2026-11-11

> **게시일.** info.json 기준 `upload_date` **`20261111`**(UTC), `timestamp` 1794434418(= 2026-11-11 22:00:18 UTC = **2026-11-12 07:00 KST**), `availability: public`. UTC와 KST 날짜가 다르다. 파일명 · `published`는 관례대로 `upload_date`(2026-11-11)를 쓴다. 파일명에서 제목 앞의 `[한글자막]`과 `(완전 정리)`는 뺐다.
>
> **오디오 트랙과 자막 — 인용 규칙.** **영어 원본 오디오만** 있는 구성이다(`English (US) original (default)` + 더빙 7개 언어 de · es · fr · hi · id · it · pt). 메타 `language`=`en`. **수동 자막(`subtitles`)은 비어 있다**(번인 자막 여부는 영상을 보지 않아 미확인). `ko-orig`가 없고 ko는 `kind=asr&lang=en&tlang=ko` 기계 번역이다. `en`은 en-orig와 md5가 다르다(`en` 313줄 · en-orig 286줄). **인용은 en-orig로만 한다.** 429 없음.
>
> **형식.** Chase AI 채널의 Chase(설명란 근거 — 발화에 이름 없음)의 1인 해설을 Tech Bridge가 재게시. 원 영상 제목 · 게시일 · 링크는 설명란에 없다. **무캡션 간격**: en-orig는 00:00 *And* 한 단어 뒤 **00:23까지 비어 있다**(챕터 *소개*, 내용 미상 — `en` · ko는 00:01에 *Favor 5.2* 한 줄). 화면의 예시 프롬프트(03:16 · 03:57 · 09:24 등 *"a prompt like the one you see on screen"*)는 캡션에 없다.
>
> **ASR 판독(en-orig).** *cloud code*(00:49 · 01:46) → Claude Code, *claw.md*(04:17 · 04:26 · 04:58 · 07:56 · 09:51) → CLAUDE.md, *agent.mmd*(09:51) → AGENTS.md, *Enthropic*(03:00 · 08:31) → Anthropic, *Babel 5.2*(06:00) → Fable 5.2, *sub aents*(07:59 · 08:09 · 08:14) → sub agents, *$248*(01:56) → $2.48(설명란), *37.6% 6%*(01:50~01:52) → 37.6%, *to a te*(08:26) → to a T, *Ultra Code*(08:19) → Ultra Code(Ultracode). *Boris*(04:24)는 성이 발화되지 않는다(Boris Cherny로 추정, 위키의 읽기).
>
> ⚠️ **해석이 갈리는 곳.** *"get rid of those now if you're going to start using Fable 5.2 because of its cost"*(07:59~08:03) — *because of its cost* 가 무엇에 걸리는지 문장이 모호하다. *"they threw a bunch of resets. far away"*(10:08~10:11) — *far away* 미판독. *"only 50% of the usage"*(10:16) — 무엇의 50%인지 말하지 않는다.
>
> ⚠️ **사실 진술의 출처.** 수치(45.3% · $6.72 · $12.82 · 37.6% · $2.48 · 2% · 6배 · 절반 · 20%)와 *증류 분류기* · *코드 소유* 차이는 모두 **화자가 공식 가이드 · 시스템 카드 · 벤치마크 표를 읽어 준 것**이다. 위키는 원 문서를 열지 않았다.

## 설명란

Anthropic이 Claude Fable 5.2용 공식 프롬프트 가이드를 내놓으면서, 이전 모델에서 잘 통하던 프롬프트 습관 상당수가 달라졌습니다. Chase AI 채널의 Chase가 그중 가장 큰 변화 10가지를 공식 가이드와 시스템 카드를 근거로 정리한 영상을 한국어 자막으로 소개합니다.

핵심 내용
- 추론 강도는 high로 시작: FrontierCode 2.0 기준 high 45.3%($6.72), medium 37.6%($2.48), Opus 5.5 max 수준 성능을 약 절반 비용으로
- 결과를 증명하게 하고, 끝까지 하라고 명시하기
- 예전 CLAUDE.md·지침 정리: Fable 5.2는 주어진 규칙을 거의 그대로 따른다
- "생각하지 마"는 통하지 않고, 단계별 추론 설명 요구는 증류 시도로 차단될 수 있다
- 코드의 주인을 알려 주면 중복 코드가 줄어든다
- 서브에이전트 위임은 모델에 맡기고, 긴 작업엔 중간 보고를 요청
- 말투와 답변 길이는 추론 강도가 아니라 프롬프트로 정해진다

챕터
0:00 소개
0:23 Fable 5.2, 프롬프트 규칙이 바뀌었다
0:40 규칙 1 · 추론 강도는 high부터
2:33 규칙 2 · 결과를 증명하게 하라
3:29 규칙 3 · 끝까지 하라고 말하라
4:05 규칙 4 · 예전 프롬프트를 정리하라
5:20 규칙 5 · "생각하지 마"는 안 통한다
5:56 규칙 6 · 추론 과정을 캐묻지 마라
6:43 규칙 7 · 코드의 주인을 알려 줘라
7:46 규칙 8 · 서브에이전트는 알아서 쓰게
8:40 규칙 9 · 긴 작업엔 중간 보고를
9:27 규칙 10 · 말투와 길이는 프롬프트로
10:02 정리 · 강력하지만 사용량은 50%

관련 자료
- Claude 공식 문서(프롬프트 가이드): https://platform.claude.com/docs

원본 제작: Chase AI (영상 화면 좌측 상단 Source 표기)
수치와 평가는 원본 영상 제작자가 공식 가이드·시스템 카드를 인용해 설명한 내용이며, 영상 공개 시점 기준입니다.

#Claude #Fable #프롬프트엔지니어링 #ClaudeCode #AI코딩 #Anthropic #한글자막

> info.json `tags`: AI 코딩 · Anthropic · CLAUDE.md · Claude · Claude Code · Claude Fable · Fable 5.2 · 프롬프트 · 프롬프트 엔지니어링 · 한글자막

## 트랜스크립트 — en-orig (원음 영어 ASR — 인용 근거)

[00:00] And
[00:23] you're prompting Fable 5.2 wrong.
[00:26] Anthropic has changed the rules. whether
[00:28] it's what effort level you should be
[00:29] using or how we approach sub agents. So
[00:32] today I'm going to be walking you
[00:34] through the 10 biggest prompting rule
[00:36] changes so you can get the most out of
[00:38] this insanely powerful model. Now the
[00:40] first prompting rule change has to do
[00:42] with effort level. You should be using
[00:44] Fable 5.2 on a high effort setting. Now
[00:47] this is what it defaults to in the API
[00:49] but in cloud code you will see it
[00:50] defaulting to medium. Now why do I say
[00:54] that we should be on high? Well, that's
[00:55] because high is where we are going to
[00:58] usually get the most bang for our buck
[01:00] with this new model. As we go from
[01:02] medium to high, we are going to get our
[01:04] biggest jump in terms of performance per
[01:07] dollar. And this kind of plays out
[01:09] across a number of different benchmarks.
[01:11] Here we are looking at the Agentic
[01:13] coding benchmark Frontier Code 2.0. If
[01:16] we look at high, we are getting a score
[01:19] of 45.3%
[01:21] at $6.72.
[01:23] This correlates to a better score than
[01:26] Opus 5.5 on extra high and essentially
[01:30] the same score as Opus 5.5 on a max
[01:33] setting. Yet on an Opus 5.5 max, it's
[01:35] $12.82
[01:37] and on high, it's about half that. So,
[01:39] we're getting Opus 5.5 max performance
[01:42] at half the cost. When we compare that
[01:44] to medium, which is where it's going to
[01:46] default to inside of the Cloud Code
[01:48] desktop app, we are dropping
[01:50] significantly in performance. So, 37.6%
[01:52] 6% versus 45.3. Yes, medium's at $248,
[01:58] but we do want some power if we are
[02:00] approaching problems that aren't in the
[02:03] scope of Opus 5.5. So, this is something
[02:05] that's very technically challenging or
[02:06] has a very long running agentic horizon.
[02:09] Well, what's the point of using Fable
[02:11] 5.2 on medium or low? I could probably
[02:13] get this done with Opus. So, in that
[02:15] case, I suggest by and large starting
[02:18] with a high setting. If that's not doing
[02:20] enough, then we can push it to extra
[02:22] high. And for the most part, I would
[02:23] stay away from the max effort level. We
[02:25] see this across a number of benchmarks
[02:27] where you just are paying a ton of money
[02:30] for sometimes a performance level that
[02:32] is below even extra high. Now, prompting
[02:33] rule number two is that you need to tell
[02:35] Fable 5.2 to prove its work. This model,
[02:39] more so than Fable 5.1 or Opus 5.5, will
[02:42] state inference as facts and will just
[02:45] make claims that the code doesn't
[02:46] necessarily support. So you're seeing a
[02:48] greater hallucination rate. Also, if
[02:50] you're someone who is using it at a
[02:51] lower medium setting for kind of general
[02:53] knowledge work, it will also run less
[02:55] tests than those previous models. If we
[02:58] take a look at the system card that
[02:59] Enthropic put out, if there was a file
[03:01] that was needed that was missing, 2% of
[03:03] the time, Fable 5.2 would kind of just
[03:05] make up a BS file to stand in its place
[03:08] instead of just saying it couldn't find
[03:09] it. And in these sort of scenarios, it
[03:11] would take shortcuts six times more
[03:14] often. So, how do we solve this? Simply
[03:16] give it a prompt that looks something
[03:17] like this where you're telling it to run
[03:19] tests on its output before it actually
[03:21] shows you what it created to confirm
[03:23] that what it's saying it completed is
[03:26] actually true. If you do that, you'll be
[03:28] just fine. Prompting rule number three,
[03:31] we need to tell Fable 5.2 to finish the
[03:34] job, especially when talking about
[03:36] longrunning agentic tasks. Again,
[03:38] compared to 5.1, it is more often going
[03:42] essentially going to stop its work
[03:43] before it reaches the finish line,
[03:45] especially if you have it on a low or
[03:47] medium setting. This becomes less
[03:50] apparent as we go up the effort chain,
[03:52] but it's still something we need to be
[03:53] aware of, even if you're on high or
[03:55] extra high. Now, to get around this,
[03:57] according to the system card, we just
[03:58] need to use a prompt like the one you
[04:00] see on screen. If you use that, you're
[04:02] going to run into these scenarios where
[04:03] it stops working about half as often.
[04:05] Now, prompting rule number four is
[04:06] arguably the most important, and it has
[04:09] to do with all of your old prompts. You
[04:11] need to go back and take a hard look at
[04:14] your current claw.md files and your
[04:17] instructions because chances are they
[04:19] are not built for Fable 5.2. We've heard
[04:22] a bunch of things from people like Boris
[04:24] saying, "Delete all your claw.md files
[04:26] or even delete your skills." And the
[04:27] idea also holds true here with Fable
[04:29] 5.2. we have a brand new very powerful
[04:33] model that just doesn't operate the same
[04:35] way as things like Opus 5.5 or Fable 5.1
[04:40] specifically and you'll see this with
[04:42] later rules is Fable 5.2 very diligently
[04:46] follows whatever rules you give it
[04:48] almost to a T. So if you have old files
[04:51] or old instructions that you just don't
[04:53] need, chances are you're actually
[04:55] hampering Fable 5.2's output. So, what
[04:57] specifically should you be looking to
[04:58] call from your old claw.md and rules
[05:01] files? Well, anything that gives it
[05:03] strict guidelines, unless you really,
[05:06] really need it. Anything that's very
[05:07] strict in regards to style because these
[05:10] new models are so powerful, you kind of
[05:12] need to give them space to breathe and
[05:14] do what they were designed to do. If you
[05:16] have rules or instructions that are
[05:17] overly prescriptive, you're just going
[05:19] to ruin their outputs. Now, rule number
[05:21] five has to do with what you cannot
[05:23] prompt Fable 5.2 to to do and that is
[05:26] you can't prompt it not to think. Now,
[05:29] with Fable 5.1, if you told it to do
[05:31] something like, "Hey, just give me an
[05:32] answer. Don't deliberate." It would
[05:34] actually bypass some of the thinking
[05:36] that's going on under the hood and give
[05:38] you a quick answer without burning
[05:39] tokens. That is not the case with Fable
[05:41] 5.2. It is always going to think. Now,
[05:44] how much it's going to think is going to
[05:45] be a function of your effort level. So,
[05:47] if you wanted to think less, you want it
[05:49] to be cheaper, throw it on low, throw it
[05:50] on medium. But it will always think. you
[05:52] are always going to incur that token
[05:54] cost no matter how you prompt it. Now,
[05:56] rule number six is a little tricky and
[05:58] has to do with distillation. So, you
[06:00] cannot give Babel 5.2 a prompt where you
[06:04] tell it to explain its reasoning step by
[06:07] step. It actually has a classifier
[06:08] working under the hood and it's going to
[06:10] grab that and assume you're trying to do
[06:12] some sort of distillation. So, you can
[06:14] have it explain essentially the logic
[06:17] behind the answer. But if you go beyond
[06:19] that, you're like, I want you to explain
[06:20] your step-by-step reasoning for how you
[06:22] got there. If it deems that that's some
[06:24] sort of distillation attack on your end,
[06:26] it's going to shut that down. And this
[06:28] is something we're seeing more and more
[06:30] of with these newer, more powerful
[06:31] models. Now, I know that's kind of murky
[06:33] as to where the line is. You can
[06:34] definitely ask it why it achieved its
[06:37] answer and give it a short response.
[06:38] Just be careful when you're like,
[06:40] explain your thinking exactly. It's
[06:42] going to flag it. Now, rule number seven
[06:44] is an interesting one. And here we need
[06:46] to prompt Fable 5.2 and tell it who owns
[06:50] the code. Because if you do not tell
[06:53] Fable 5.2 that it owns the codebase,
[06:55] well, it's going to approach its
[06:57] problems and how it approaches the code
[06:59] and how it writes it all a lot
[07:00] differently than if you say, "Hey,
[07:02] you're in charge of all of this."
[07:04] Specifically, if you don't tell it that
[07:06] it owns the codebase, you're going to
[07:07] see a lot of repeated code inside of the
[07:10] codebase. Versus, if you tell it it does
[07:13] own the codebase, you'll have a lot less
[07:14] repeated code, but it's going to add a
[07:16] lot of extra features and extra tests.
[07:19] And in general, you're going to get more
[07:21] output tokens spent for a better,
[07:24] leaner, more optimized result. So, if
[07:28] you are having Fable 5.2 to build
[07:30] something or you are giving it control
[07:32] of the codebase, make sure you
[07:33] explicitly tell it that there are
[07:35] significant differences between this.
[07:37] And if you take a look at the system
[07:38] card, it dives into this quite a bit.
[07:39] Now, on the other hand, if you want very
[07:41] minimal changes, don't tell it it's the
[07:43] owner. Just be very specific in your
[07:44] prompting of what you want it to
[07:46] actually do. Now, rule number eight has
[07:47] to do with prompting for sub agents.
[07:50] Now, this goes back to an earlier rule
[07:52] where we talked about get rid of some of
[07:54] your old claw.md files or some of the
[07:56] old rules you have in place. If you have
[07:57] rules that talk about sub aents and
[07:59] delegating sub agents, get rid of those
[08:01] now if you're going to start using Fable
[08:03] 5.2 because of its cost. Fable 5.2 is
[08:07] smart enough to start spawning sub aents
[08:09] when it needs to. Especially if we're
[08:11] talking about higher effort levels like
[08:13] extra high and max, it's going to spawn
[08:14] its own sub aents to check its own work.
[08:16] Almost like a miniature version of Ultra
[08:19] Code. But if you have rules that are
[08:20] like, "Hey, I want you to use sub agents
[08:22] for X, Y, and Z and always check your
[08:24] work." It's going to follow those rules
[08:26] to a te and you are going to rip through
[08:28] your usage and you're going to rip
[08:29] through all those resets that Enthropic
[08:31] is giving you. So in general, just let
[08:33] Fable 5.2 do its thing. It understands
[08:35] when it needs to delegate sub agents.
[08:38] You don't need to spell it out for it.
[08:40] Now, prompting rule number nine kind of
[08:42] has to do with personal preference and
[08:44] it has to do with really long tool
[08:45] calls. If you are telling Fable 5.2 to
[08:48] to do some sort of task that takes a ton
[08:50] of time, a ton of tool calls, it can
[08:51] sometimes kind of go silent as it just
[08:53] does all the work in the background. If
[08:55] you give it some sort of prompt that
[08:57] tells it to give you updates, it's going
[09:00] to do so. If you get a little nervous
[09:02] when you kind of just see it working in
[09:04] the background for 40 minutes with zero
[09:05] updates whatsoever. Now, if you tell it
[09:08] you want to speak after the first tool
[09:09] call every single time, that could
[09:11] increase token usage by 20%, which could
[09:13] be a bit much, but there definitely is a
[09:16] middle ground there. So, in general, it
[09:18] can be kind of silent during some of
[09:19] these very long tasks. So, if you wanted
[09:21] to actually talk to you and let you know
[09:23] what's going on, what the tool calls are
[09:24] looking like, just give it a simple
[09:26] prompt saying you want that. Now, last
[09:28] but not least, we have rule number 10,
[09:29] which has to do with Fable 5.2's tone
[09:32] and length of responses. This is not
[09:34] something that can be affected by the
[09:36] effort level. Whether you are on low or
[09:38] whether you are on max, it's going to
[09:39] give you the same tone, the same length
[09:41] for its outputs. So if you want to
[09:44] change that, understand that needs to be
[09:45] a prompt. And if you really like
[09:47] something done a specific way, that
[09:49] probably needs to go inside of a claw.md
[09:51] or an agent.mmd or some sort of rule. So
[09:53] if you expect that on low, you're just
[09:55] going to get quicker, shorter, and more
[09:56] succinct responses. Not the case. That
[09:58] is only affected by the prompts you
[10:00] would give it with Fable 5.2. So those
[10:02] are the most important prompting rule
[10:04] changes when it comes to Claude Fable
[10:06] 5.2. You should be really excited to use
[10:08] this model. Extremely powerful, and they
[10:11] threw a bunch of resets. far away, which
[10:13] sort of makes up for the fact a little
[10:14] bit that we're still kind of stuck with
[10:16] only 50% of the usage, which is still
[10:18] kind of a bummer.

## 트랜스크립트 — ko (`tlang=ko` 기계 번역 — 참고용, 인용하지 않음)

[00:01] 현재 Favor 5.2 버전을 사용 중입니다.
[00:10] 모양
[00:25] 잘못된. 인간 활동은 변화를 가져왔습니다.
[00:27] 규칙, 노력의 정도와 상관없이
[00:29] 사용해야 합니다 또는 다음과 같은 방법을 사용해야 합니다
[00:30] 우리는 하위 담당자들에게 접근했습니다. 그래서 오늘
[00:32] 가장 큰 변화 10가지를 설명해 드리겠습니다.
[00:35] 신청 규칙에서 다음과 같이
[00:36] 이를 통해 최대한의 효과를 얻을 수 있습니다.
[00:38] 엄청나게 강력한 모델입니다. 첫 번째
[00:40] 신청 규칙이 변경되었습니다.
[00:42] 이는 노력의 정도와 관련이 있습니다.
[00:43] Favor 5.2를 레벨과 함께 사용해야 합니다.
[00:46] 많은 노력이 필요합니다. 이것이 값입니다
[00:48] 클로드의 코드에서 기본값
[00:49] API 버튼에서; 그러면 그것이 무엇인지 알게 될 겁니다.
[00:50] 기본적으로 구성됩니다.
[00:52] 반. 내가 왜 우리가 그래야 한다고 말하는 걸까?
[00:54] 상위 레벨을 사용하시겠습니까? 음, 왜냐하면
[00:56] 높은 수준은 우리가 일반적으로 얻는 수준입니다.
[00:58] 가격 대비 최고의 성능
[01:00] 이 새로운 모델과 함께.
[01:02] 중급 수준에서 다음 수준으로 넘어감에 따라
[01:03] 높이 올라가면 가장 큰 도약을 할 수 있을 거예요.
[01:05] 달러당 수익률 측면에서.
[01:07] 그리고 이는 여러 측면에서 드러납니다.
[01:09] 서로 다른 참고 자료. 여기 우리가 있습니다
[01:12] 벤치마크 분석
[01:13] 에이전트 코딩, 프론티어 코드
[01:15] 2.0. 우리가 하늘을 올려다보면, 우리는…
[01:19] 45.3%의 점수와 6.72달러의 가격을 기록했습니다.
[01:24] 이는 더 나은 결과와 관련이 있습니다.
[01:26] 오푸스는 최고 등급에서 5.5점을 받았습니다.
[01:28] 기본적으로 점수는 동일합니다.
[01:30] 최대 구성에서 Opus 5.5보다
[01:32] .
[01:33] 하지만 최대 Opus 5.5에서는 다음과 같습니다.
[01:35] 12.82달러 이상이며, 대략적인 금액입니다.
[01:38] 반.
[01:39] 그래서 우리는 최고의 성능을 얻습니다.
[01:41] Opus 5.5를 반값에 만나보세요.
[01:44] 중간 지점과 비교해 보면, 그곳은 바로 그곳입니다.
[01:45] 기본값으로 설정됩니다
[01:47] 데스크톱 애플리케이션 내에서
[01:48] 클로드 코드, 우리가 지고 있어요
[01:49] 성능이 크게 향상되었습니다. 그래서
[01:52] 37.6% 대 45.3%입니다. 네, 중간 크기입니다.
[01:56] 가격은 2.48달러지만, 저희는 일부를 원합니다.
[01:58] 우리는 권력과 관련된 문제들을 해결하고 있습니다.
[02:01] Opus의 범위에 속하지 않는 것들
[02:03] 5.5. 그러니까 이건 ~을 포함하는 일입니다.
[02:05] 또는 기술적으로 매우 어려운 과제를 안고 있거나
[02:07] 매우 장기적인 의제 관점.
[02:09] 그럼 Fable 5.2를 쓸 이유가 뭐죠?
[02:11] 중간 또는 낮음? 아마 할 수 있을 거예요
[02:13] Opus를 이용해 보세요. 그렇다면,
[02:16] 높은 설정부터 시작하는 것을 추천합니다. 응
[02:19] 그것만으로는 부족해요, 더 나아가서 할 수 있어요.
[02:21] 매우 높은 수준. 그리고 일반적으로 저는
[02:23] 노력의 정도와 관계없이 멀리 떨어져 있게 할 것입니다.
[02:25] 최고. 우리는 이것을 일련의 사건들에서 볼 수 있습니다.
[02:26] 비교 테스트에서
[02:28] 당신은 그저 많은 돈을 지불할 뿐입니다.
[02:29] 때때로 나타나는 성능 수준의 경우
[02:31] 최고 수준보다도 낮습니다.
[02:33] 자, 이제 참조 규칙에 대해 알아보겠습니다.
[02:34] 두 번째는 말해야 한다는 것입니다.
[02:36] Fable 5.2의 작동 방식을 보여주는 예시입니다. 이것
[02:38] 모델, Fable 5.1이나 Opus 5.5보다 더 나은,
[02:41] 추론을 사실로 확립할 것입니다.
[02:43] 코드가 하지 않는 주장만 할 것입니다.
[02:46] 반드시 뒷받침해야 합니다. 그러므로,
[02:48] 더 높은 비율을 보고 계십니다.
[02:49] 환각. 또한, 만약 당신이 누군가라면
[02:51] 이는 낮음-중간 설정에서 사용됩니다.
[02:52] 지식 노동의 한 유형
[02:54] 일반적으로 테스트 횟수도 더 적습니다.
[02:56] 이전 모델보다.
[02:58] 자, 그럼 한번 살펴보겠습니다.
[02:59] 게시된 시스템 카드
[03:01] 인류의 경우, 파일이 누락되었다면
[03:02] 그게 필요했던 경우는 2% 정도였어요. 페이블 5.2
[03:04] 저는 단순히 BS 파일을 만들었습니다.
[03:06] 그냥 바꾸는 대신
[03:07] 찾을 수 없었다고 말하는 것입니다.
[03:10] 이런 상황이라면 저는 다음과 같이 하겠습니다.
[03:12] 지름길을 여섯 배 더 자주 이용합니다.
[03:14] 그렇다면 이 문제를 어떻게 해결할까요?
[03:15] 다음과 비슷한 경고를 해주세요:
[03:17] 이건 실행하라고 지시하는 부분이에요.
[03:20] 저에게 보여주기 전에 출력 부분에서 먼저 테스트해 보세요.
[03:22] 그가 그것을 확인하기 위해 실제로 만들어낸 것은 무엇인가?
[03:24] 그가 완료했다고 말하는 것은 사실
[03:26] 진실. 그렇게 하면 괜찮을 거예요.
[03:29] 세 번째 경고 규칙: 우리는 반드시
[03:31] Fable 5.2에게 완료하라고 말하세요
[03:33] 일, 특히 우리가 이야기할 때
[03:35] 장기간 실행되는 에이전트 작업의
[03:37] .
[03:38] 다시 말해, 5.1과 비교하면 더 높습니다.
[03:41] 그는 그 전에 일을 그만둘 가능성이 높습니다.
[03:43] 결승선에 도달하기 위해, 특히
[03:45] 만약 낮은 설정으로 해 놓았다면 또는
[03:47] 평균. 이는 점점 덜 분명해집니다.
[03:49] 우리가 그 사슬을 따라 앞으로 나아가면서
[03:51] 노력이 필요하지만, 여전히 무언가가 있습니다.
[03:52] 우리는 당신이 설령 그렇다 하더라도 이를 고려해야 합니다.
[03:54] 높은 수준 또는 매우 높은 수준으로. 지금
[03:56] 자, 그럼 해결하려면, 다음과 같이 하면 됩니다.
[03:57] 시스템 카드만 있으면 됩니다.
[03:59] 다음과 같은 공지사항을 사용하세요.
[04:00] 화면. 사용해 보시면 알게 될 것입니다.
[04:02] 작동이 멈추는 상황
[04:04] 대략 절반 정도 그렇습니다. 지금
[04:06] 자, 공지사항 작성 규칙 4번입니다.
[04:07] 아마도 가장 중요한 요소일 것입니다.
[04:09] 그것은 당신이 보낸 모든 공지사항과 관련이 있습니다.
[04:10] 고대의.
[04:12] 다시 돌아가서 확인해야 합니다.
[04:14] claw.md 파일을 자세히 살펴보세요.
[04:15] 현재 및 귀하의 지침은 다음과 같습니다.
[04:17] 아마 그런 용도로 설계된 것은 아닐 겁니다.
[04:19] 페이블 5.2.
[04:21] 우리는 여러 사람들로부터 많은 이야기를 들었습니다.
[04:23] 보리스가 모든 사람을 삭제하라고 말하는 것과 같습니다.
[04:24] claw.md 파일이나 심지어 그것조차도
[04:26] 당신의 기술을 없애버리세요. 그리고 그 아이디어
[04:28] Fable 5.2에서도 마찬가지입니다.
[04:30] 저희는 새롭고 매우 강력한 모델을 보유하고 있습니다.
[04:33] 그것은 단순히 같은 방식으로 작동하지 않는다는 것입니다.
[04:37] Opus 5.5나 Fable 같은 것들 말이죠.
[04:40] 5.1.
[04:41] 구체적으로, 그리고 규칙들을 통해 이를 확인할 수 있을 겁니다.
[04:43] 이후 Fable 5.2에서는 많은 내용이 이어집니다.
[04:45] 당신이 거의 모든 사람에게 주는 규칙을 성실히 따르세요
[04:48] 그대로.
[04:49] 따라서 파일이 있거나
[04:51] 단순히 오래된 지침
[04:52] 그럴 필요 없어요, 아마도 당신은
[04:54] 당신은 결과 도출을 방해하고 있습니다.
[04:56] 페이블 5.2. 그렇다면 당신은 무엇을 해야 할까요?
[04:58] 특히 다음 항목에서 제거하려고 노력하십시오.
[05:00] 예전 claw.md 파일과 규칙 파일들 말인가요? 잘
[05:02] 가이드라인을 제공하는 모든 것
[05:04] 정말 그렇지 않다면 엄격하지 마세요.
[05:06] 당신에게 필요한 것. 아주
[05:08] 스타일 면에서 엄격합니다. 왜냐하면
[05:09] 이 새로운 모델들은 매우 강력합니다.
[05:11] 그들에게 공간을 주어야 한다는 것입니다.
[05:13] 숨을 쉬고 당신이 해야 할 일을 하세요
[05:15] 설계되었습니다. 규칙이 있다면 또는
[05:17] 지나치게 구체적인 지침,
[05:19] 그렇게 하면 그들의 결과를 망칠 뿐이에요.
[05:20] 자, 다섯 번째 규칙은 다음과 같습니다.
[05:23] 그건 당신이 요구할 수 없는 것과 관련이 있어요.
[05:25] Fable 5.2는 그렇지만, 그 이유는 불가능합니다.
[05:27] 그녀에게 생각하지 말라고 부탁하세요. 이제, 함께
[05:29] Fable 5.1, 만약 당신이 그에게 하라고 했다면
[05:31] "이봐, 그냥 대답해 줘" 같은 거 말이야.
[05:33] "고려하지 마십시오"는 사실상 생략될 것입니다.
[05:34] 그것은 사고의 일부입니다.
[05:36] 백그라운드에서 제작 중이며, 여러분에게 제공할 것입니다.
[05:38] 칩을 소모하지 않고 빠르게 답변할 수 있는 방법.
[05:40] 하지만 Fable 5.2는 그렇지 않습니다. 언제나
[05:43] 그는 생각할 것이다. 그렇다면 얼마일까요?
[05:45] 사고력은 당신의 사고 수준에 따라 달라질 것입니다.
[05:46] 노력. 그러므로, 만약 당신이 원한다면
[05:48] 생각을 줄이세요, 그러면 더 많은 것을 얻을 수 있을 겁니다.
[05:49] 싸게, 낮게, 중간으로 설정하세요.
[05:51] 하지만 그는 언제나 생각할 것이다.
[05:52] 그 비용은 항상 발생할 것입니다.
[05:54] 어떻게 말하든 토큰은
[05:56] . 자, 여섯 번째 규칙은 다음과 같습니다.
[05:58] 그리 복잡하지 않고, 다음과 관련이 있습니다.
[05:59] 증류. 그러므로 당신은 할 수 없습니다
[06:02] Fable 5.2에게 그 이유를 설명하도록 지시합니다.
[06:05] 단계별 추론. 실제로,
[06:07] 분류기가 작동 중입니다
[06:09] 배경을 바탕으로, 그것을 받아들이고 가정하겠습니다.
[06:11] 혹시 어떤 일을 하려고 하시는 건가요?
[06:12] 증류. 그러므로 당신은 할 수 있습니다
[06:15] 그것이 바로 그 논리를 설명하는 것입니다.
[06:16] 그 답에는 어떤 의미가 숨겨져 있지만, 만약 당신이 간다면
[06:18] 이어서 당신은 이렇게 말합니다. "설명해 주셨으면 합니다."
[06:20] 단계별 추론 과정을 설명해 주세요.
[06:22] "그 정도까지는 왔으니,"라고 생각한다면 말이죠.
[06:24] 이건 일종의 공격이에요
[06:26] 당신이 증류 작업을 하면 그것이 차단될 것입니다.
[06:28] 그리고 이것은 우리가 매일 목격하고 있는 현상입니다.
[06:30] 이러한 새로운 모델들이 등장하면서 그 경향이 점점 더 커지고 있습니다.
[06:31] 강한. 어디인지 명확하지 않다는 것을 알고 있습니다.
[06:33] 한계가 있습니다. 물론 가능합니다
[06:35] 그에게 왜 그걸 얻었는지 물어보세요
[06:36] 간략하게 답변해 주세요.
[06:38] "설명해 주세요"라고 말할 때는 조심하세요.
[06:40] 당신의 추론이 정확합니다." 그러면 표시될 것입니다.
[06:43] . 자, 일곱 번째 규칙은 다음과 같습니다.
[06:45] 흥미롭네요. 그리고 여기서 우리는...
[06:47] Fable 5.2에게 누가
[06:49] 코드 소유자. 그렇지 않으면,
[06:52] Fable 5.2에게 그것이 소유자라고 알려줍니다.
[06:54] 코드베이스에서 문제를 해결할 것입니다.
[06:56] 그가 코드를 접근하는 방식과 코드를 작성하는 방식
[06:58] 그는 평소와는 전혀 다른 방식으로 글을 쓴다.
[07:01] 당신은 "이봐, 네가 모든 걸 책임져."라고 말합니다.
[07:03] 이것".
[07:04] 구체적으로 말하자면, 만약 당신이 그에게 그것이 무엇인지 말하지 않는다면
[07:07] 코드베이스 소유자,
[07:09] 코드 내부에 반복되는 부분이 많이 보일 겁니다.
[07:11] 코드베이스에 대해 이야기하는 반면, 그에게 말하면
[07:13] 그렇다면 코드 양이 훨씬 줄어들 겁니다.
[07:16] 반복되는 내용이지만, 많은 내용을 추가할 것입니다.
[07:18] 추가 기능 및 테스트 및
[07:20] 일반적으로 다음에서 더 많은 토큰을 얻을 수 있습니다.
[07:22] 더 나은 결과를 위해 마모된 출력을 사용하십시오.
[07:24] 더욱 민첩하고 최적화되었습니다.
[07:27] 그러므로, 만약 당신이 Fable 5.2를 만든다면
[07:29] 무언가를 컴파일하거나 제어권을 넘겨주다
[07:31] 코드베이스에 대해 꼭 알려주세요.
[07:33] 명시적으로. 차이점이 있습니다
[07:35] 이것과 만약 당신이 시전한다면 사이에는 상당한 차이가 있습니다.
[07:37] 시스템 카드를 살펴보세요.
[07:38] 그는 이 주제에 대해 꽤 자주 이야기합니다. 자, 그럼
[07:40] 반면에, 변경을 원한다면
[07:41] 최소 금액이야, 그에게 말하지 마
[07:42] 사장님, 다음 사항을 아주 구체적으로 말씀해 주세요.
[07:44] 당신이 원하는 것에 대한 지침
[07:45] 실제로 그렇습니다. 자, 규칙은 다음과 같습니다.
[07:47] 8번은 다음과 관련이 있습니다.
[07:49] 하위 약제에 대한 적응증. 이것은
[07:51] 이는 이전 규칙으로 거슬러 올라갑니다.
[07:52] 우리는 당신의 일부를 없애는 것에 대해 이야기하고 있습니다.
[07:54] 오래된 claw.md 파일이나 기타 파일들
[07:55] 당신이 가지고 있는 기존 규칙들
[07:56] 활기. 규칙에 다음과 같은 내용이 포함되어 있다면
[07:59] 하위 대리인 및 위임된 하위 대리인,
[08:01] 시작할 거라면 지금 당장 없애버리세요.
[08:03] Fable 5.2를 사용하려면 비용이 많이 든다는 점 때문에 사용하지 않습니다.
[08:06] Fable 5.2면 충분합니다.
[08:07] 하위 에이전트를 생성할 만큼 지능적입니다.
[08:09] 필요할 때, 특히 다음과 같은 경우
[08:11] 우리는 더 높은 수준의 노력을 이야기하고 있는 겁니다.
[08:12] 매우 높음, 최대와 같은 높은 값은 생성합니다.
[08:14] 그들 자신의 하위 대리인을 통해 그들의 진위를 확인합니다.
[08:16] 자신의 작품, 거의 버전과 같은 것
[08:18] 울트라 코드 썸네일. 하지만 만약 당신이 가지고 있다면
[08:20] "이봐, 난 원해"와 같은 규칙들
[08:22] X, Y, Z에 대해 하위 에이전트를 사용한다는 것, 그리고
[08:24] 항상 자신의 작업을 확인하세요. 그러면 계속 진행될 것입니다.
[08:26] 그 규칙들을 글자 그대로 따르고
[08:27] 사용 내역을 검토하고 이 모든 사항을 검토하게 될 것입니다.
[08:29] Anthropic이 제공하는 재부팅 기능입니다.
[08:32] 그래서 일반적으로 Fable 5.2를 사용하세요.
[08:34] 하고 싶은 대로 해. 언제 필요한지 이해하세요
[08:36] 위임받은 하위 대리인.
[08:38] 굳이 자세히 설명할 필요는 없어요. 자, 그럼,
[08:40] 응용 규칙 9번은 다음과 같습니다.
[08:42] 그것은 개인적인 선호와 관련이 있습니다.
[08:44] 그리고 도구 호출과 관련해서 정말
[08:45] 긴. Fable 5.2에게 다음과 같이 하라고 지시하면
[08:47] 오랜 시간이 걸리는 작업
[08:49] 시간, 많은 전화
[08:50] 도구는 가끔씩 작동이 멈출 수 있습니다.
[08:52] 침묵은 모든 일을 다 처리하기 때문입니다.
[08:54] 배경.
[08:55] 만약 당신이 그에게 어떤 종류의 경고라도 한다면
[08:58] 업데이트를 받으라고 하세요.
[09:00] 약간 긴장하면 그런 일이 일어날 거예요.
[09:02] 백그라운드에서 작동하는 모습을 지켜보세요.
[09:04] 40분 동안 아무것도 없이
[09:05] 업데이트.
[09:07] 자, 만약 당신이 그에게 당신이 원하는 것을 말한다면
[09:08] 첫 통화 후에 이야기하세요
[09:10] 매번 도구를 사용하면, 그것은 가능할 수 있습니다.
[09:12] 토큰 사용량을 20% 증가시키기 위해,
[09:13] 다소 과한 표현일 수도 있지만
[09:15] 분명히 중간 지점이 있습니다.
[09:17] 대개는 조용할 수 있습니다.
[09:18] 이러한 작업 중 일부 동안
[09:20] 긴. 그러므로 만약 정말로
[09:21] 당신과 이야기를 나누고 싶고, 알려드리고 싶은 것이 있습니다.
[09:23] 무슨 일이야? 통화 내용은 어떤가요?
[09:25] 도구의 경우, 그냥 주면 됩니다.
[09:26] 당신이 그것을 원한다는 간단한 메시지입니다.
[09:27] 자, 마지막으로, 하지만 결코 중요하지 않은 것은 아닙니다.
[09:29] 중요한 것은, 우리에게는 10번 규칙이 있다는 것입니다.
[09:30] 음색과 관련이 있습니다.
[09:32] Fable 5.2 응답 길이
[09:33] . 이것은 눈으로 볼 수 있는 것이 아닙니다.
[09:35] 노력의 정도에 영향을 받습니다. 너무
[09:37] 만약 당신이 낮은 레벨에 있다면, 예를 들어
[09:39] 기껏해야 같은 음색, 같은 느낌만 줄 뿐입니다.
[09:41] 결과가 나오는 데 걸리는 시간입니다. 그래서 만약
[09:43] 바꾸고 싶다면, 그것이 가지고 있는 것을 이해해야 합니다.
[09:45] 그것이 경고가 되어야 한다는 것입니다.
[09:46] 그리고 만약 당신이 어떤 일이 진행되는 것을 정말 좋아한다면
[09:48] 특정한 방식으로, 아마도
[09:50] 클로.md 또는 a 안에 들어가야 합니다.
[09:51] agent.md 또는 어떤 종류의 규칙. 그래서
[09:53] 낮은 수준에서만 그렇게 예상한다면,
[09:55] 더 빠르고 간결한 답변을 받으실 수 있습니다.
[09:57] 간결할 거라고 생각했지만, 사실은 그렇지 않습니다. 그게 다예요
[09:58] 그것은 당신이 주는 경고의 영향을 받습니다.
[10:01] Fable 5.2와 함께. 그래서 이것들이 바로 그것들입니다.
[10:03] 규칙의 주요 변경 사항
[10:05] 클로드 페이블과 관련된 주의사항
[10:06] 5.2.
[10:07] 사용하게 되어 매우 기쁘실 겁니다.
[10:08] 이 모델. 매우 강력하고
[10:10] 우리는 수많은 재설정을 겪었습니다.
[10:12] 이는 어느 정도 다음과 같은 사실을 상쇄합니다.
[10:14] 우리는 여전히 단지 ~에만 갇혀 있습니다
[10:16] 사용량의 50%는 여전히...
[10:18] 폐가 되는 행위. 언젠가는 없어지길 바라요.
[10:20] 그 제한 사항.
