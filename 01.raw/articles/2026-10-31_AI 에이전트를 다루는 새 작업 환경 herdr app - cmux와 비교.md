---
title: "[한글자막] AI 에이전트를 다루는 새 작업 환경 herdr app | cmux와 비교"
type: video
source: https://www.youtube.com/watch?v=D2yA1--RoKQ
site: youtube.com
author:
  - "[[Tech Bridge]]"
duration: 14:10
published: 2026-10-31
created: 2026-11-01
description: "Mehul Mohan(발화 호명 · 설명란 근거)의 1인칭 화면 시연 · 사용기 14:10, 공식 챕터 10, 내레이션 없음 · 영어 원본 오디오만. herdr가 터미널 안에서 돌던 도구에서 'GUI application combined with CLIs'인 앱으로 나온 날의 첫인상. CLI를 쓰는 이유(Claude Code의 새 'even more dangerously skip permissions' 플래그 — 환경 변수 두 개로 끊기지 않는 세션, 데스크톱 앱은 설정 안에 숨김), 테마, 원격 머신(SSH · worker) 추가와 앱 종료 후에도 계속 도는 에이전트(로컬 Mac은 잠들면 멈춤), 에이전트 상태(idle · done · working) · 알림 · first-class 에이전트 통합, mission control · Slack · Google Meet 같은 레이아웃, 무거운 영상 편집은 로컬 · 나머지는 VM, Claude Code Remote Control로 모바일 제어, herdr의 서브에이전트 API, cmux 비교(SSH 세션이 앱 종료 시 사라짐 · 'cmux ssh tmux' 실험 기능 · UI 커스터마이즈)."
tags:
  - clippings/youtube
---

**Source URL**: https://www.youtube.com/watch?v=D2yA1--RoKQ
**Channel**: Tech Bridge · **Duration**: 14:10 · **Published**: 2026-10-31

> **게시일 — UTC/KST 날짜가 갈린다.** info.json 기준 `upload_date` **`20261031`**(UTC), `timestamp` 1793487636(= 2026-10-31 23:00:36 UTC = **2026-11-01 08:00 KST**), `availability: public`, `release_date` 없음. 이 채널 관례대로 파일명 · `published`는 `upload_date`(2026-10-31)를 쓴다. 한국 시간으로는 11-01 아침 게시다. 파일명에서 제목 앞의 `[한글자막]`은 빼고 `|`는 ` - `로 바꿨다.
>
> **오디오 트랙과 자막 — 인용 규칙.** 10-27 Voss · 10-28 Parakhin · 10-29 Chase · 10-30 Osmani 편과 같은 구성이다. 오디오는 **`English (US) original (default)`** 하나가 원본이고 나머지(de · es · fr · hi · id · it · pt)는 더빙이다. **한국어 오디오 트랙이 없다.** 메타 `language`=`en`. **수동 자막(`subtitles`)은 비어 있다** — 제목의 "[한글자막]"과 달리 YouTube에 올라간 한국어 자막 파일은 없다(번인 자막 여부는 영상을 보지 않아 미확인). `automatic_captions`의 en · ko 계열은 `en-orig` · `en` · `ko` 셋이고 **`ko-orig`가 없다.** en-orig URL은 `kind=asr&lang=en&variant=gemini`, ko 첫 URL은 `lang=en&variant=gemini&tlang=ko` **기계 번역**이다. 인용은 **en-orig로만** 한다.
>
> ⚠️ **`en` 파일은 en-orig와 다르다(json3 md5 불일치).** info.json의 `en` 첫 URL은 en-orig와 같은 파라미터인데, 받은 `en`은 원문을 고쳐 쓴 문장이다 — 예: en-orig *"I've been keeping an eye on C marks and holder, these two tools for quite some time"*(00:23~00:27) → en *"I've been keeping a close eye on C marks and holder, these two tools, for a long time"*, *"a software that fits you"*(00:32) → *"a software tailored to your needs"*. en과 ko는 줄 수(434)와 타임스탬프가 같다 → ko는 **en 계열을 옮긴 것으로 추정**(10-30 Osmani 편과 같은 양상). 둘 다 인용 근거가 아니다.
>
> **형식 — 1인칭 화면 시연 · 사용기, 내레이션 없음.** 한 화자가 자기 화면(herdr 앱, 터미널, 설정)을 보여 주며 말한다(*"look at this"* 02:08~02:10, *"as you can see"* 04:47). 다른 목소리는 없다. 원본 영상 링크는 설명란에 없다(설명란의 링크는 herdr · cmux · Claude Code Remote Control 문서 셋 — **열어 보지 않았다**).
>
> **화자.** 설명란 본문 *"개발자 Mehul Mohan이 herdr 앱으로 AI 에이전트 작업 환경을 직접 보여줍니다"* 에 이름이 있고, **발화 안에서도 이름이 나온다** — 시청자의 질문을 옮기며 자기를 부르는 대목: *"Then why, Mehul, why do you prefer like CLI AI harnesses?"*(01:15~01:20). 1인칭 단서: 자기 채널 시청자에게 말하고(*"if you have been following me"* 00:21~00:23), 이전 영상에서 herdr의 문제를 말한 적이 있다(*"remember, I told you like holder messes up if I'm pressing command K"* 00:43~00:47), 영상 편집 작업을 Claude에게 시킨다(*"my video editor project"* 05:42~05:44, 10:13~10:17). info.json `tags`에는 이름이 없다. → **Mehul Mohan, 발화 호명 + 설명란 근거.** 성(Mohan)은 설명란에만 있다. 소속 · 직함 · 채널명은 발화되지 않는다.
>
> **내부 시점 단서.** *"today, holder specifically announced something interesting. They announced the app"*(00:27~00:32) — 녹화일 = herdr 앱 발표 당일로 화자가 말한다. *"I've been using Hurder, this application, for the last few hours"*(08:00~08:02), *"I even did not plan to create this video"*(08:06~08:07). 발표 날짜 자체는 발화되지 않는다 → **녹화일 미상**(업로드 10-31 UTC 이전). Claude Code의 새 플래그도 *"now, finally"*(01:33~01:35)라고만 한다.
>
> **무캡션 간격.** en-orig 첫 큐는 **00:21**(21.9초)에 시작하고 마지막 줄은 **14:07**이다. **00:00~00:21**(첫 공식 챕터 *소개* 거의 전체)은 자막이 없다 — 한국어 오디오 트랙이 없으므로 한국어 해설이 아니라 **타이틀 · 음악 또는 무발화 훅으로 추정**(영상 미확인). 그 뒤로는 2.5초 이상 간격이 없다(json3 큐 기준). 공식 챕터 경계(00:22 · 01:24 · 03:39 · 04:37 · 06:37 · 08:38 · 09:59 · 11:35 · 12:55)는 모두 문장 흐름 안에 있고 편집 컷 흔적은 보이지 않는다. 14:07~14:10은 무발화.
>
> ⚠️ **ASR 판독 — 제품 이름이 매번 다르게 적힌다.**
> - **herdr**: *"holder"*(00:25 · 00:27 · 00:43 · 00:47), *"Horder"*(03:40 · 03:50), *"Hodor"*(04:28 · 04:47 · 05:22 · 05:48), *"Hurder"*(07:09 · 08:00 · 12:28 · 12:43 · 13:00 · 13:59), *"Herder"*(08:39 · 08:48), *"harder"*(11:47 · 12:07). 설명란 · 태그 · 제목의 `herdr`로 판독. *"I like Hodor setting"*(04:28~04:30)은 herdr 기본 테마/설정으로 읽히나 판독 보류.
> - **cmux**: *"C marks"*(00:23 · 00:37 · 00:41 · 00:58), *"C max"*(04:41), *"Cmux"*(12:54~13:48) → cmux. *"Cmux SSH tmux"*(13:36)는 `cmux ssh` + tmux 조합의 명령으로 읽힌다(정확한 명령 형식 미확인).
> - *"cloud code"*(02:19 · 02:37 · 02:45 · 03:04) · *"cloud desktop app"*(03:06 · 03:08) → Claude Code · Claude 데스크톱 앱(*"Claude code"* · *"Claude desktop app"*으로 바르게 적힌 곳도 있다). *"Deep Seek and Open Code"*(06:45~06:48) → DeepSeek · OpenCode. *"is sandbox one"*(01:48) · *"Set the sandbox environment as one, set this one as one"*(02:12~02:16) — 샌드박스 여부를 알리는 환경 변수를 1로 두는 것으로 읽히나 **변수 이름은 화면에만 있어 미확인.** *"another 98"*(04:05) — Windows 98풍 레트로 테마로 읽히나 판독 보류. *"RMRF"*(01:53) → `rm -rf`. *"user at the rate host"*(04:51) → `user@host`. *"command shift B"*(13:20) 원문 그대로.
>
> ⚠️ **ko(기계 번역)는 인용 근거가 아니다.** herdr를 *"홀더"* · *"호더"* · *"호르도르"*, cmux를 *"C 마크"* · *"C-Max"*, tmux를 *"티맥스"* · *"T-Max"* 로 옮긴다. *"Claude desktop app"* → *"클로드의 책상"*(01:14), *"local AI agent"* → *"지역 AI 상담원"*(04:55). 특히 *"Cmux is that it's definitely much more frictional to use"*(12:54~12:58)를 *"C-Max는 확실히 비싸다"* 로 옮겨 **마찰(friction)을 가격으로 바꾼다.**
>
> ⚠️ **제품 · 회사 주장은 1인 사용자의 진술이다.** (1) *"somebody working at Claude code in Anthropic posted this that now, finally, they have a Claude code even more dangerously skip permissions flag"*(01:31~01:39) — 게시자 이름 · 링크 · 플래그 정확한 이름이 없다. (2) 기존 dangerously skip permissions가 *"still blocks you many, many times with some RMRF commands"*(01:52~01:55)라는 것과 Anthropic이 그것을 *"weaker"*(02:00~02:02)하게 만들었다는 것은 화자 체감이다. (3) herdr의 *"complete API"*(12:30~12:32), 원격 worker의 지속 실행, 앱 종료 후 로컬 프로세스 유지, cmux SSH 문제는 화자가 수 시간 써 본 범위의 시연 · 진술이고 herdr · cmux 측 확인 · 버전 정보가 없다. (4) Remote Control이 *"works flawlessly at least for me"*(11:58~12:01)는 1인 체감이다. 화자가 *"why I prefer this over C marks"*(00:56~00:58)라고 처음부터 선호를 밝힌다.

## 설명란

개발자 Mehul Mohan이 herdr 앱으로 AI 에이전트 작업 환경을 직접 보여줍니다.
원격 머신 연결과 작업 상태 관리, 앱 종료 후 작업이 이어지는 구조와 로컬 Mac이 잠들 때의 한계를 살펴봅니다. 마지막에는 화자가 사용해 본 cmux와 비교합니다.

00:00 소개
00:22 herdr와 CLI
01:24 CLI의 권한과 유연성
03:39 새 앱의 화면 구성
04:37 원격 머신과 작업 지속
06:37 에이전트 상태와 관리
08:38 바꿀 수 있는 작업 화면
09:59 로컬과 VM의 역할
11:35 모바일 제어와 하위 에이전트
12:55 cmux와 비교한 경험

관련 자료
herdr: https://herdr.dev/
cmux: https://cmux.com/
Claude Code Remote Control: https://code.claude.com/docs/en/remote-control

#AI에이전트 #ClaudeCode #Codex #herdr #cmux

> info.json `tags`: AI 에이전트 · Claude Code · Codex · cmux · herdr · 개발자 도구

## 트랜스크립트 — en-orig (원음 영어 ASR — 인용 근거)

[00:21] So, if you have been following me, you
[00:23] know I've been keeping an eye on C marks
[00:25] and holder, these two tools for quite
[00:27] some time. And today, holder
[00:29] specifically announced something
[00:30] interesting. They announced the app, a
[00:32] software that fits you, basically a GUI
[00:35] application combined with CLIs. Now, if
[00:37] this reminds you of C marks, you're
[00:39] probably right, because this was my
[00:41] whole point of using C marks. Because
[00:43] remember, I told you like holder messes
[00:45] up if I'm pressing command K for
[00:47] clearing the terminal. Because holder
[00:49] previously ran into terminal directly.
[00:52] In this video, I want to give you a look
[00:54] inside what I've been doing with this
[00:55] new application so far, and why I prefer
[00:58] this over C marks and some of the cracks
[01:00] and gaps I've started to see. All right,
[01:02] so first things first, you know, people
[01:04] ask me a lot of times like, why do you
[01:06] use CLI applications when there are so
[01:09] many good GUI applications available,
[01:11] including, you know, Codex desktop app,
[01:13] and you know, Claude desktop app as
[01:15] well. Then why, Mehul, why do you prefer
[01:17] like CLI AI harnesses? Now, it's not
[01:20] that I prefer or I only use CLI
[01:22] harnesses. It's just that there are a
[01:24] couple of things with which CLI makes
[01:27] possible, which is just not possible
[01:29] otherwise. Let me give you an example.
[01:31] So, somebody working at Claude code in
[01:33] Anthropic posted this that now, finally,
[01:35] they have a Claude code even more
[01:37] dangerously skip permissions flag. And
[01:39] this one is so important because I've
[01:41] been asking this for a long time, right?
[01:44] The problem with Claude code turns out
[01:46] to be that even if you're passing like
[01:48] is sandbox one and even the dangerously
[01:50] skip permissions flag, it still blocks
[01:52] you many, many times with some RMRF
[01:55] commands or something. Like, I don't
[01:56] know like why Anthropic did this, but
[01:58] they basically made this dangerously
[02:00] skip permissions weaker. But with this
[02:02] flag now, it makes it possible to run it
[02:04] in a similar way, right? Now, this is
[02:06] very easy for you to understand on CLI.
[02:08] The reason I say that is because look at
[02:10] this. This is all you have to do if
[02:12] you're running this on CLI, right? Set
[02:14] the sandbox environment as one, set this
[02:16] one as one, and just hit enter. And once
[02:18] you do, you are inside a cloud code
[02:20] window that you know for a fact would
[02:21] not be interrupted again. Like it'll
[02:23] just keep on working even if you just
[02:25] give it something and just go away,
[02:27] it'll just keep on working. This thing
[02:28] is very cumbersome to do in a GUI. Why?
[02:31] Because first of all, it depends whether
[02:33] the GUI harness, whatever you're using,
[02:35] supports this or not in the first place.
[02:37] The thing is that cloud code is one of
[02:39] the many harnesses, right? There might
[02:41] be a different harness with a different
[02:43] flag, with different level of, you know,
[02:45] permission mode. For example, cloud code
[02:47] supports auto mode, it supports this
[02:49] bypass permission mode, it supports like
[02:51] a bypass permission with an even more
[02:53] dangerous permission mode, right? So,
[02:55] what I'm trying to get here is that CLI
[02:57] means flexibility, right? Or more
[03:00] importantly, like native app means
[03:02] flexibility. Now, this native app could
[03:04] be like cloud code on CLI, it could be
[03:06] like cloud desktop app. But I'm pretty
[03:08] sure like even on cloud desktop app, it
[03:09] will be very challenging to find where
[03:11] this flag is, right? Desktop app has a
[03:14] bunch of features which are much more
[03:16] hidden than CLI. Like the even the
[03:18] dangerously bypass permission flag is
[03:21] hidden inside settings. You have to
[03:22] enable it, and then that is visible. I'm
[03:24] not saying that all of this, like this
[03:25] this single thing makes it like uh
[03:27] desktop apps are bad and CLI are good.
[03:29] I'm just saying that native apps and,
[03:31] you know, CLIs generally gives you a lot
[03:33] more flexibility and the ability to hack
[03:36] around compared to simple desktop apps.
[03:38] Now, with that being said, this is the
[03:40] preview of how the new Horder app looks
[03:42] like, and you can customize a bunch of
[03:44] these parts. Now, the customization is
[03:46] actually very less in terms of looks.
[03:48] You can either have like the typical
[03:50] Horder look, which has like the sidebar,
[03:52] which has these terminals. You can just
[03:54] have terminals as well, which converts
[03:56] it more or less into, you know,
[03:57] something like an iTerm or something
[03:59] like a
[04:01] um, you know, a regular terminal
[04:02] emulator. I don't prefer this look and
[04:05] then there is another 98. I don't know
[04:07] why this exists, but again like this is
[04:08] something for classics. I don't know
[04:10] like
[04:12] it just looks way too raw. I know like
[04:14] what they're trying to get here like
[04:16] creating that nostalgia and everything,
[04:18] but I guess like this is just way too
[04:21] this is like shiny for if you want to
[04:22] like take screenshots and stuff, but I'm
[04:25] pretty sure like this is not the way to
[04:26] work if you're doing like serious work
[04:28] day-to-day, right? I like I like Hodor
[04:30] setting and I like graphite as a theme
[04:32] as well. I'm zoomed in a little, but you
[04:33] can obviously keep this at 100 when
[04:36] you're actually working. The next thing
[04:37] that I like is that it's very easy to
[04:39] manage your multiple machines here which
[04:41] was somewhat challenging with C max.
[04:44] Over here what you can do is you can
[04:45] just click here to add a machine and as
[04:47] you can see like Hodor has first-class
[04:49] support. You just give it like a user at
[04:51] the rate host or you add it to your SSH
[04:53] config and you can just pick it up or
[04:55] you can ask your local AI agent itself
[04:57] to configure this and it'll do it for
[04:59] you. Now once you do this, you're going
[05:00] to see that you will have something like
[05:02] worker one here. So I named this worker
[05:03] one and you're going to see that this is
[05:05] available inside this machine as well.
[05:07] So you can have like multiple machines
[05:09] over here as well. Now all of this is
[05:11] async. What that means is let's say I
[05:13] start a process here and let's say I ran
[05:15] Claude and I said to Claude, "Hey, can
[05:18] you just count to 1 to 100 very very
[05:20] slowly?" And if I hit enter and let's
[05:22] just say I just quit Hodor, right? So
[05:24] I've quit the app right now. So I'm
[05:25] going to launch the app now and once I
[05:27] launch it, you can see like Claude is
[05:29] basically done, but it was able to run
[05:31] this in the background, right? Even if I
[05:32] quit the app, if I lose the Wi-Fi
[05:34] connection, whatever. Why? Because this
[05:36] was running on the worker. Similarly, if
[05:38] I'm running any agent on my computer
[05:40] itself, you know, let's say I start
[05:42] Claude inside my video editor project
[05:44] which is there, I can go ahead and start
[05:45] working here as well and I can just
[05:48] close this whole window because Hodor is
[05:50] maintaining a different process on this
[05:52] Mac OS which is keeping the processes
[05:54] keeping these terminals these agents
[05:56] alive. Now on Mac, you don't get the
[05:58] guarantee if the Wi-Fi stops working or
[06:00] if your computer actually goes to sleep.
[06:02] It would actually stop because that is
[06:04] how like computers work. But that is
[06:05] where these machines come into play,
[06:07] which is very, very important. Other
[06:09] than this, I can just ask it, for
[06:10] example, "Please look into item one
[06:14] carefully." Let's say I do this. You can
[06:16] see like it clearly separates like which
[06:18] agents are working. Let's say I just
[06:20] send this hello and, you know, just
[06:21] switch the tab. You can see like we have
[06:23] video editor, which is now done. Um and
[06:25] this is also dispatching notifications
[06:27] to me. So, if you have your headphones
[06:29] on or if you are listening to music or
[06:30] something, or you know, just managing my
[06:32] multiple agents, I think like this would
[06:34] be like a perfect way for you to work.
[06:36] Last but not the least, obviously, you
[06:37] can have multiple AI agents as well
[06:40] configured on this, right? So, as you
[06:42] can see, I would have like, you know, if
[06:44] I have a bunch of Codex agents, or if I
[06:45] have, let's say, Deep Seek and Open Code
[06:48] and and some of these agents running on,
[06:50] I can go ahead and launch them. These
[06:52] agents provide first-class integration
[06:54] directly into the software, right? So,
[06:56] it will know like which when it is idle,
[06:58] when it is done, when is it working, and
[06:59] so on. You can obviously use the agents
[07:02] which are not mentioned here as well.
[07:04] It's just that you might not have the
[07:05] best agents experience with those
[07:07] specific CLIs, right? So, I mean, I
[07:09] won't consider Hurder as, you know,
[07:12] looking at this video, I won't consider
[07:14] this as like a fully terminal-based
[07:17] system. It uses minimal GUI, which is
[07:20] something that I really like, but at the
[07:22] same time gives me like a full terminal
[07:24] interface, terminal emulator, SSH
[07:26] connections, virtual machines. I can add
[07:29] workers that I can maintain, and the
[07:31] notifications that I want. And with the
[07:33] split panels, you know, I can have these
[07:34] multiple panels. I can arrange them if I
[07:36] want, which is pretty sick, right? So,
[07:38] this gives me like an experience of how
[07:40] I work with terminals usually, but at
[07:42] the same time with all the goodies and
[07:44] everything that, you know, I expect from
[07:46] a software allowing me to orchestrate
[07:49] the all the agents. I know this field is
[07:52] super saturated and super like there are
[07:55] a lot of softwares, and you might find
[07:56] something which is actually useful for
[07:58] you. But I just found like I've been
[08:00] using Hurder, this application, for the
[08:02] last few hours. And I've been actually
[08:04] trying it, not just for for of building
[08:06] this video. I I even did not plan to
[08:07] create this video, right? But I've been
[08:09] trying it and I feel like more of you
[08:11] need to use CLI just because, you know,
[08:13] you guys are developers and you should
[08:15] know how to use command line. But at the
[08:17] same time, don't restrict yourself with
[08:19] just simple interfaces of iTerm, just a
[08:21] single interface, just, you know, using
[08:23] tmux all across for managing agents. All
[08:26] of them are good. There are real use
[08:27] cases of doing all of that. The thing is
[08:29] that you can be far more productive, in
[08:31] my opinion, if you're using something
[08:33] like this, like a agent multiplexer or
[08:35] agent manager sort of screen. In fact,
[08:37] this is like far more powerful. I think
[08:39] I would not need anything that Herder
[08:41] has
[08:42] over here. It's It's It seems almost
[08:44] like an overkill, but you can have very
[08:46] weird layouts, apparently, for some
[08:48] reason inside Herder, which includes
[08:50] like a mission control dashboard sort of
[08:52] thing. You can have almost like a
[08:53] Slack-like preview UI. I don't even know
[08:56] like how does this even work in the
[08:57] first place. You can have like a Google
[08:59] Meet-like a call sort of UI where agents
[09:01] are on call and their terminals are
[09:03] there. I don't know like
[09:05] Guys, let me know if any of these UI,
[09:07] like threads and stuff, if if this turns
[09:09] out to be like useful to you. It looks
[09:11] definitely a lot more powerful to me,
[09:13] but, you know, you can just go ahead and
[09:14] create these threads-like UIs and, you
[09:17] know, having like terminals and then a
[09:19] UI for sending the messages. It seems
[09:22] like this is extremely hackable, right,
[09:24] the new version that they have released.
[09:26] Now again, deliberately I'm not going
[09:28] and wiring this up and creating like
[09:30] something very weird because I know for
[09:32] a fact the screen that you're seeing
[09:34] right now, I'm not showing you all of my
[09:35] workflows, but when I start working on
[09:37] this, this is an extremely productive
[09:40] way of working with AI agents. And I
[09:42] don't think that you need anything more
[09:44] than what you're seeing on your screen
[09:45] right now. With multiple computers, your
[09:48] own computer for the sensitive workloads
[09:50] that you can't move to servers, and your
[09:52] agents which are just organized properly
[09:54] by the state, like where they are right
[09:56] now. How I expect you to drive your
[09:59] workload is in the following way, right?
[10:01] So, you should go ahead and keep on your
[10:03] computer certain workloads that you know
[10:06] are very data heavy or requires you
[10:09] often, right? So, the reason I'm saying
[10:11] this is because on my Mac OS right now,
[10:13] one of the workflows that I run locally
[10:15] is video editing, right? Maybe I would
[10:17] move it sometime in future on cloud, but
[10:19] the problem with moving this is that the
[10:21] files that Claude is editing and the AI
[10:24] are editing are north of like 8 10 GB
[10:26] files sometimes each, right? So, just
[10:28] uploading and downloading itself would
[10:30] take like a few minutes of time. And
[10:32] then, you know, when it makes a change,
[10:34] I have to watch the video because Claude
[10:36] and these AI agents also make make
[10:38] mistakes a lot of times often because
[10:39] they can't see. They are not like they
[10:41] don't have vision, right? And even if
[10:43] they have vision, like it it has vision,
[10:45] but just image vision.
[10:47] Um but even with that, they make a lot
[10:49] of mistakes because they're because
[10:50] they're not seeing each and every single
[10:51] frame, right? So, I have to be to be the
[10:53] one who has to watch the video. So,
[10:55] doing this whole feedback loop, it's
[10:57] going to take very a lot of data and
[10:59] would take a lot more time than if I
[11:01] just ask it to do it on my own computer,
[11:03] right? So, that is one of the workflows
[11:05] that works on my system. Apart from
[11:07] this, anything else, you know, your
[11:08] software engineering and, you know,
[11:10] regular feature development, bug fixes,
[11:11] all of that, that that can sit on a VM,
[11:14] right? So, I have this one virtual
[11:15] machine where I just put all the other
[11:17] projects that I have and I can dispatch
[11:19] the agents which I want to work
[11:22] with. So, for example, I have one
[11:24] upcoming project that I'm working on. I
[11:26] have a bunch of other projects that I've
[11:28] already worked on in the past. So,
[11:30] virtual machine, having like a VM in
[11:32] place helps manage these agents. And
[11:34] finally, at least for Claude code, the
[11:36] one thing that I use right now is remote
[11:38] control on my mobile phone. So, if it is
[11:39] running on virtual machine, I can
[11:41] remotely control the session using
[11:43] Anthropic's built-in feature. Now, it
[11:45] would be awesome if we also have a
[11:47] harder mobile app or something. I don't
[11:49] think like they have released anything
[11:50] which specifically ties the machines
[11:53] that you are working over here with
[11:54] mobile application, but I don't think
[11:56] like I need it right now because the
[11:58] Anthropic's remote control works
[12:00] flawlessly at least for me. I don't see
[12:01] like any bugs or anything at all with
[12:03] this. It works really good. So, yeah, I
[12:05] mean, you can go ahead and look inside
[12:07] harder. I'll leave all the links in the
[12:08] description. This looks like a very
[12:10] hackable
[12:11] UI-wise at least. You can even have your
[12:14] local computers, local systems, and you
[12:16] can have like all of these bunch of
[12:17] agents running up, which sounds like
[12:19] very exciting. But, in all honesty, like
[12:21] you would not have like 100 agents
[12:23] running, right? At least not by
[12:25] yourself. If your agents themselves
[12:27] invoke other agents, that's a different
[12:28] thing. And by the way, like Hurder
[12:30] actually supports a complete API for
[12:32] that as well, right? So, Claude code
[12:34] probably does not need it because they
[12:36] have like support first-class support
[12:38] for sub-agents, new new bits of agents
[12:41] themselves and so on. But, you can use
[12:43] Hurder itself for, you know, just
[12:46] running new sub-agents, steering them,
[12:48] and you know, just reporting it back to
[12:50] the main agent. So, again, like
[12:51] something that your agents can use
[12:53] directly. You don't have to worry about
[12:54] this. One thing I can say about Cmux is
[12:56] that it's definitely much more
[12:58] frictional to use than what I've seen
[13:00] with Hurder. Just a couple of closing
[13:02] notes because I mentioned like I would
[13:04] talk about Cmux over here. So, what one
[13:05] of the problems that I found with Cmux
[13:07] is that the SSH actually does not really
[13:10] work properly, right? So, you can like
[13:13] SSH,
[13:14] uh you know, do something like Cmux SSH
[13:16] and then do the command SSH root at the
[13:19] rate whatever. And then when you like
[13:20] press like command shift B, split the
[13:22] terminal, so you have like one terminal
[13:24] here, one terminal here. Both of them
[13:27] are inside SSH server directly. The
[13:29] problem here is that if you quit Cmux
[13:31] now, there is no way to get this back.
[13:32] So, you have lost like it's actually not
[13:34] running in a tmux-like thing. So, what
[13:36] you have to do is do Cmux SSH tmux,
[13:39] which is an experimental thing, and it's
[13:41] very frictional. It just breaks a lot.
[13:43] I've seen this. Like if you lose your
[13:44] internet connection, it'll just break
[13:46] your terminal emulator itself. Secondly,
[13:48] I tried to customize UI of Cmux. I even
[13:51] asked my agents to do like some parts of
[13:53] it like removing the description from
[13:54] the terminal's tabs. I was not able to
[13:56] get a wow factor from it, right? There
[13:59] is something about Hurder like it just
[14:00] overall by default looks pretty. I don't
[14:03] have to put a lot of effort. This is
[14:04] simple. This is nice. I can get started
[14:07] right away without making a lot of fuss.

## 트랜스크립트 — ko (`tlang=ko` 기계 번역 — 참고용, 인용하지 않음)

[00:22] 그러니까, 만약 그들이 나를 따라왔다면,
[00:23] 그들은 내가 면밀히 지켜보고 있었다는 것을 알고 있다.
[00:25] C 마크와 홀더, 이 두 가지
[00:26] 오랫동안 사용해 온 도구들입니다. 그리고 오늘,
[00:28] 홀더는 구체적으로 어떤 사실을 발표했습니다.
[00:30] 흥미로운. 그들은 앱을 발표했습니다.
[00:32] 기본적으로 사용자의 요구에 맞춘 소프트웨어입니다.
[00:34] 그래픽 인터페이스를 갖춘 애플리케이션
[00:36] CLI와 결합됨. 자, 만약 이것이...
[00:38] C 학점을 떠올리게 하네요. 아마 그럴 거예요.
[00:40] 그게 바로 제가 말하려던 요점이었기 때문입니다.
[00:42] C 마크를 사용할 때. 기억하세요, 그들은
[00:44] 내가 누르면 홀더가 고장난다고 계산해 봤어
[00:46] 터미널을 지우려면 K 키를 누르십시오.
[00:48] 이전 소유자가 처형되었기 때문에
[00:50] 터미널에서 바로. 이
[00:52] 이 영상에서 제가 무엇을 가지고 있는지 보여드리고 싶어요.
[00:54] 저는 이 새로운 것을 하고 있습니다.
[00:55] 지금까지의 적용 사례와 그 이유
[00:57] 저는 C 학점을 선호합니다.
[00:59] 제가 시작한 일에 몇 가지 결점과 부족한 점이 있습니다.
[01:01] 참고 사항. 자, 우선 가장 중요한 것부터 시작해 볼까요?
[01:03] 아시다시피, 사람들은 저에게 질문을 많이 해요.
[01:05] 저는 가끔 CLI 애플리케이션을 사용합니다.
[01:07] 좋은 앱이 너무 많은데
[01:08] 그래픽 사용자 인터페이스를 사용할 수 있습니다.
[01:10] 데스크톱 애플리케이션을 포함하여
[01:12] 코드 x로부터, 그리고 또한 적용
[01:14] 클로드의 책상. 그렇다면 왜
[01:16] 메훌, 왜 더 선호하세요?
[01:18] CLI를 통한 AI 도구? 음, 그렇지 않아요.
[01:20] 당신이 선호하는 것 또는 도구만 사용하는 것
[01:22] CLI를 통해. 다만 몇 가지 사항이 있습니다.
[01:25] CLI가 가능하게 해주는 것과
[01:27] 그렇지 않으면 불가능합니다.
[01:29] 방법. 예를 하나 들어보겠습니다.
[01:31] 클로드 코드에서 일하는 사람
[01:33] 앤트로픽이 이것을 발표했는데, 이제,
[01:35] 마침내 그들은 클로드로부터 명령을 받았다.
[01:36] 권한을 우회하는 코드
[01:38] 더 위험하다. 이것은 매우 중요합니다.
[01:40] 제가 한동안 계속 요청해왔기 때문입니다.
[01:42] 꽤 오랜 시간이네요, 그렇죠?
[01:44] 클로드 코드의 문제점은 다음과 같습니다.
[01:46] 샌드박스를 하나로 통과하더라도
[01:48] 그리고 심지어는 건너뛰기 허가증 깃발까지도
[01:50] 위험하게도, 그것은 여전히 ​​당신을 차단합니다.
[01:52] 여러 번 어떤 사람들과 함께
[01:54] RMRF 명령어 같은 거요. 나는 이유를 모르겠다
[01:56] 앤트로픽이 이걸 했지만, 기본적으로는
[01:58] 그들은 이러한 권한 변경을 가능하게 했습니다.
[02:00] 외부가 위험하고 약하다. 하지만 ~와 함께
[02:01] 이 깃발 덕분에 이제 가능해졌습니다.
[02:03] 비슷한 방식으로 실행하려면,
[02:05] 진실? 이건 아주 쉽게 할 수 있어요.
[02:07] CLI에서 이해합니다. 그 이유는
[02:09] 제가 이렇게 말하는 이유는, 이것을 보세요. 이것은
[02:11] 당신이 해야 할 모든 일
[02:12] CLI에서 실행하는 거죠? 구성
[02:14] 샌드박스 환경을 하나로 구성합니다.
[02:16] 이건 하나와 같고, 그냥 엔터 키를 누르면 됩니다. 그리고
[02:18] 그렇게 하시면 접속이 완료됩니다.
[02:19] 당신이 알고 있는 클로드 코드 창
[02:21] 다시는 중단되지 않을 확신
[02:23] . 당신이 그것을 주더라도 계속 작동할 것입니다.
[02:25] 어떤 일이 벌어지고 당신이 떠나더라도, 그것은 그냥 계속될 것입니다.
[02:27] 일하고 있는. 이건 너무 거추장스럽다
[02:29] 그래픽 인터페이스를 사용하여 작업을 수행합니다. 에 의해
[02:31] 저것? 첫째로, 그것은 ~에 달려있기 때문입니다.
[02:33] 사용 중인 그래픽 인터페이스가
[02:35] 이것과 호환되나요?
[02:37] 요점은 클로드 코드는 단지
[02:39] 여러 도구 중 하나일 뿐이죠, 그렇죠?
[02:41] 다른 도구가 있을 수도 있습니다.
[02:43] 다른 구성과 다른
[02:45] 권한 수준. 예를 들어, 클로드
[02:47] 이 코드는 자동 모드, 모드 등을 지원합니다.
[02:49] 권한 우회 및 모드까지
[02:51] 허가 누락은 훨씬 더 위험합니다.
[02:54] , 아니요?
[02:55] 제가 말씀드리고 싶은 것은 이렇습니다.
[02:57] CLI는 유연성(flexibility)의 약자 맞죠?
[02:59] 더 중요하게는, 애플리케이션이
[03:01] 네이티브는 유연성을 의미합니다. 이것
[03:03] 네이티브 애플리케이션은 Claude Code일 수 있습니다.
[03:05] CLI 또는 데스크톱 애플리케이션에서
[03:07] 클로드의. 하지만 저는 확신합니다.
[03:08] 데스크톱 애플리케이션에서도 마찬가지입니다.
[03:10] 클로드의 가게는 찾기가 매우 어려울 거예요.
[03:11] 그 설정이 어디에 있죠?
[03:12] 데스크톱 애플리케이션에는 많은 기능이 있습니다.
[03:15] 명령줄 인터페이스(CLI)보다 훨씬 더 숨겨진 기능들입니다.
[03:17] 예를 들어, 건너뛰기 옵션
[03:19] 위험한 허가증은 숨겨져 있습니다.
[03:20] 설정 내에서. 당신은 해야 합니다
[03:22] 활성화하면 보이게 됩니다. 나는 말하는 게 아니야
[03:24] 이 사소한 디테일이 모든 것을 바꿔놓는다는 것
[03:26] 데스크톱 애플리케이션은 나쁜 것이다.
[03:28] 그리고 CLI는 좋은 것입니다. 제가 말하고 싶은 건 그겁니다.
[03:30] 네이티브 애플리케이션 및 CLI, 작성자:
[03:32] 일반적으로 그들은 훨씬 더 많은 것을 제공합니다.
[03:34] 유연성과 능력
[03:35] 애플리케이션의 맞춤 설정
[03:37] 공용 책상. 하지만 이것은
[03:39] 새로운 버전이 어떻게 생겼는지 미리 보여드립니다.
[03:41] Horder 앱을 사용하면 맞춤 설정이 가능합니다.
[03:43] 그 구성 요소 중 여러 개. 사실, 있습니다
[03:46] 맞춤 설정 옵션이 거의 없습니다.
[03:47] 모습.
[03:49] 일반적인 스타일을 선택할 수 있습니다.
[03:50] Horder는 사이드바를 가지고 있습니다.
[03:52] 터미널.
[03:54] 터미널만 따로 설치할 수도 있습니다.
[03:56] 그래서 대략적으로
[03:59] iTerm이나 에뮬레이터와 비슷한 것
[04:01] 일반 단말기. 난 이게 더 마음에 안 들어.
[04:04] 외관이 다르고, 그다음이 98년형 모델입니다. 아니요
[04:07] 나는 그것이 왜 존재하는지 알지만, 아마도 그럴 것이다.
[04:09] 향수를 불러일으키는 무언가. 글쎄요, 그렇게 보이네요.
[04:11] 너무 기본적인 거야.
[04:14] 저는 그들이 그것을 만들어서 달성하려는 목표를 이해합니다.
[04:17] 향수이긴 하지만, 제 생각엔 그건 뭔가 다른 의미가 있는 것 같아요.
[04:19] 너무 화려해서 그냥 가져갈 수가 없어
[04:21] 스크린샷 같은 것들 말이에요.
[04:24] 하지만 이건 분명 아닐 거예요.
[04:26] 중요한 업무를 처리할 때의 작업 방식
[04:28] 매일 그렇죠, 그렇죠? 나는 좋아한다
[04:29] 호더 설정과 저도 마찬가지입니다
[04:31] 저는 흑연 테마가 마음에 들어요. 제가 가져왔습니다
[04:33] 이미지가 약간 흐릿하지만, 분명히 알아볼 수 있습니다.
[04:34] 100%로 유지하세요
[04:36] 진짜로 일하고 있어요. 다음 일
[04:38] 제가 좋아하는 점은 관리하기가 매우 쉽다는 것입니다.
[04:40] 여기 있는 여러 대의 기계는...
[04:42] 무언가 복잡한
[04:46] 여기에 기계를 추가하려면 다음과 같이 하세요.
[04:48] 보시다시피, 호더는 다음과 같은 곳에서 지원을 받고 있습니다.
[04:49] 일등. 그냥 그에게 뭔가를 주면 돼.
[04:51] 호스트의 사용자 또는 사용자 계정에 추가하세요.
[04:53] SSH 설정이 완료되었으면 가져가셔도 됩니다.
[04:55] 지역 AI 상담원에게 문의할 수 있습니다.
[04:57] 그가 모든 걸 준비하고 처리해 줄 거예요. 지금
[04:59] 이렇게 하면 다음과 같은 것을 확인할 수 있습니다.
[05:01] 여기에는 "작업자 1"과 같은 것이 있을 겁니다. 너
[05:03] 저는 제 이름을 '작업자 1'이라고 지었고, 곧 알게 되실 겁니다.
[05:05] 이 내용 내에서도 이용 가능합니다.
[05:06] 기계. 그래서 여러 개를 가질 수 있습니다.
[05:08] 여기에도 기계가 있습니다. 자, 이 모든 것
[05:10] 비동기식입니다. 이것은 다음을 의미합니다.
[05:13] 제가 여기서 어떤 과정을 시작한다고 가정해 보겠습니다.
[05:15] 내가 클로드를 처형하고 그에게 말했다고 가정해 보자.
[05:17] 클로드: "저기, 1부터 까지 세어볼 수 있어?"
[05:19] 100을 아주 아주 천천히?" 그리고 만약 내가 누르면
[05:21] 엔터 키를 누르고, 그냥 닫는다고 해두죠.
[05:23] 호더, 맞죠? 그래서 방금 닫았어요
[05:25] 지금 바로 신청하세요. 이제 저는 가겠습니다
[05:26] 애플리케이션을 시작하고 완료되면
[05:28] 클로드가 기본적으로 어떤 사람인지 알 수 있습니다.
[05:29] 끝났지만, 그는 이것을 계속 진행할 수 있었다.
[05:31] 배경이죠, 그렇죠? 설사
[05:32] 저는 애플리케이션을 종료합니다. 내가 잃으면
[05:34] 와이파이 연결 여부는 상관없습니다. 왜냐하면?
[05:35] 이것이 운영되고 있었기 때문에
[05:37] 노동자. 마찬가지로, 만약 내가
[05:38] 내가 직접 에이전트를 실행하고 있다
[05:40] 컴퓨터, 그러니까, 예를 들어
[05:41] 클로드에게 제 프로젝트를 소개합니다.
[05:43] 거기에 있는 비디오 편집기요. 할 수 있다
[05:45] 저도 여기서 일을 시작할 수 있어요.
[05:47] Horder 때문에 이 창 전체를 닫으세요
[05:50] 이 경우에는 다른 프로세스를 유지합니다.
[05:52] 이러한 프로세스를 유지하는 Mac OS 및
[05:54] 이러한 단말기, 이러한 에이전트, 자산
[05:56] . 맥에서는 다음과 같은 경우 보증이 적용되지 않습니다.
[05:59] 와이파이가 작동을 멈추거나
[06:00] 컴퓨터가 절전 모드로 들어갑니다.
[06:02] 그게 그들의 방식이니까 나는 멈출 거야
[06:04] 컴퓨터. 하지만 바로 그곳이
[06:06] 이러한 기계들이 작동하게 되는데,
[06:08] 그것은 매우, 매우 중요합니다. 이것 외에도,
[06:10] 예를 들어, 저는 그에게 이렇게 물어볼 수 있습니다. "부디,
[06:12] "첫 번째 항목을 꼼꼼히 확인하세요."
[06:14] 제가 이렇게 한다고 가정해 봅시다. 어떻게 보이는지 알 수 있습니다
[06:16] 어떤 에이전트가 어떤 에이전트인지 명확하게 구분하세요.
[06:18] 일하고 있는. 그냥 이렇게 말해두죠.
[06:20] 이 안부를 전하며, 아시다시피...
[06:21] 탭 변경. 볼 수 있듯이
[06:23] 저희는 이미 동영상 편집기를 보유하고 있습니다.
[06:24] 용어.
[06:25] 음, 그리고 이것도 저를 보내고 있어요
[06:27] 알림. 그래서, 만약 당신이 가지고 있다면
[06:29] 헤드폰을 착용했거나 듣고 있다면
[06:30] 음악이나 뭐 그런 거, 아니면 그냥 뭐랄까,
[06:32] 여러 명의 에이전트를 관리하는 것은 제 생각에...
[06:33] 이것이 완벽한 방법이 될 것이라는 점
[06:35] 당신이 일하는 것. 마지막으로 중요한 것은
[06:37] 중요하죠, 당연히 여러분도 할 수 있어요.
[06:39] 여러 개의 AI 에이전트를 보유하세요
[06:40] 여기서 설정된 거죠?
[06:42] 보시다시피, 저는 이미 가지고 있었을 겁니다.
[06:44] 아시다시피, 만약 저에게 요원 그룹이 있다면
[06:45] Codex, 또는 예를 들어 Deep Seek와 같은 프로그램을 가지고 있다면
[06:47] 오픈 코드와 이러한 에이전트 중 일부
[06:49] 일단 실행이 시작되면, 이제 실행을 진행할 수 있습니다.
[06:50] .
[06:51] 이러한 에이전트는 통합 기능을 제공합니다.
[06:53] 일등석으로 바로 진입
[06:55] 소프트웨어 맞죠? 그러면 그는 알게 될 것이다.
[06:56] 비활성화되었을 때, 종료되었을 때,
[06:58] 그가 일할 때 등
[07:00] 물론 에이전트를 사용할 수도 있습니다.
[07:02] 여기에 언급되지 않은 것들입니다. 그냥 그게
[07:04] 어쩌면 당신은 최고의 경험을 하지 못했을지도 모릅니다.
[07:06] 해당 라인 인터페이스를 가진 에이전트
[07:07] 구체적인 명령입니다. 이해하시겠습니까? 그래서
[07:09] 제 말은, 저는 고려조차 하지 않을 거라는 뜻이에요.
[07:11] 살인, 이 영상을 보고 나니, 아니, 그런 건 생각도 안 나네요.
[07:13] 저는 그것을 하나의 시스템으로 간주하겠습니다.
[07:15] 완전히 터미널 기반입니다.
[07:18] 최소한의 그래픽 인터페이스를 사용합니다.
[07:20] 제가 정말 좋아하는 것이지만,
[07:22] 동시에, 그것은 나에게 인터페이스를 제공합니다.
[07:24] 전체 터미널, 터미널 에뮬레이터
[07:25] SSH 연결 및 가상 머신.
[07:28] 제가 추가할 수 있는 작업자를 추가할 수 있습니다.
[07:30] 원하는 알림은 유지해 주세요
[07:32] . 그리고 분할 패널이 있으면, 아시잖아요.
[07:34] 저는 여러 개의 패널을 사용할 수 있습니다.
[07:35] 원한다면 정리할 수도 있어요.
[07:37] 정말 놀랍지 않나요?
[07:39] 그래서 이것은 제게 경험을 선사합니다.
[07:41] 제가 평소에 일하는 방식
[07:43] 터미널이지만 동시에
[07:45] 모든 장점과 제가 기대하는 모든 것
[07:47] 제가 오케스트레이션을 할 수 있게 해주는 소프트웨어
[07:49] 모든 에이전트.
[07:51] 이 분야가 이미 포화 상태라는 것을 알고 있습니다.
[07:54] 소프트웨어 프로그램은 많으며, 그럴 수도 있습니다.
[07:56] 당신에게 정말 잘 어울리는 것을 찾아보세요
[07:58] 유용한.
[07:59] 하지만 저는 제가 이미 그런 상태였다는 사실을 깨달았을 뿐입니다.
[08:00] Hurder라는 이 애플리케이션을 사용하는 동안
[08:02] 지난 몇 시간 동안. 그리고 저는 정말로 가지고 있어요
[08:04] 저는 단순히 이걸 만들기 위해서만 테스트를 한 게 아닙니다.
[08:06] 동영상. 저는 이걸 만들 계획조차 없었어요.
[08:08] 영상 말이에요, 아시죠? 하지만 저는...
[08:09] 테스트 중인데, 여러분 중 더 많은 분들이 그런 것 같아요.
[08:11] 그들은 그냥 CLI를 사용해야 합니다. 왜냐하면, 뭐랄까,
[08:13] 여러분은 개발자이시니, 마땅히 해야 할 일을 하셔야 합니다.
[08:15] 명령줄 사용법을 알고 있어야 합니다.
[08:16] 하지만 동시에, 스스로를 그 틀 안에만 가두지 마세요.
[08:19] iTerm의 간단한 인터페이스는 단지
[08:21] 단일 인터페이스, 그냥, 아시다시피, 사용하세요.
[08:23] tmux를 모든 곳에서 관리하세요
[08:25] 자치령 대표. 모두 훌륭해요. 있습니다
[08:27] 이 모든 것을 수행하는 데 있어 실제 사용 사례
[08:29] . 요점은, 당신은 여러 가지가 될 수 있다는 것입니다.
[08:31] 제 생각에는 사용하는 것이 더 생산적입니다.
[08:32] 이런 것, 예를 들어 멀티플렉서 같은 것
[08:34] 에이전트 또는 화면 유형
[08:35] 에이전트 매니저. 사실 이것은
[08:37] 훨씬 더 강력합니다. 저는 그렇게 생각하지 않아요.
[08:39] 헤르더가 가진 건 내게 필요 없어.
[08:42] 여기. 과한 것처럼 보일 수도 있지만
[08:44] 다양한 디자인을 가질 수 있는 것 같네요.
[08:46] 낯선 사람들이 무슨 이유인지 안에 있습니다.
[08:49] 헤르더는 패널과 같은 것을 포함합니다.
[08:51] 임무 관제 센터. 거의 다 가질 수 있어요
[08:53] 미리보기 인터페이스는 다음과 유사합니다.
[08:55] 느슨하게. 이게 어떻게 작동하는지 전혀 모르겠어요
[08:57] 가장 먼저. 당신은 가질 수 있습니다
[08:59] 구글 통화와 유사한 인터페이스
[09:00] 상담원들이 대기 중인 장소에서 만나세요.
[09:02] 그리고 그들의 단말기가 거기에 있습니다.
[09:04] 글쎄요, 여러분, 혹시 아시는 분 있으면 알려주세요.
[09:06] 스레드와 같은 이러한 인터페이스
[09:08] 그들은 그런 것들이 유용하다고 생각합니다.
[09:11] 제게는 훨씬 더 많은 것처럼 보입니다.
[09:12] 강력하지만, 아시다시피 그들은 할 수 있습니다.
[09:14] 그냥 바로 생성하세요
[09:16] 이러한 실과 같은 인터페이스, 그리고 아시다시피
[09:18] 터미널과 인터페이스를 갖추려면
[09:19] 메시지를 보내다.
[09:21] 이것은 매우 이상해 보입니다
[09:23] 수정 가능하죠?, 새 버전 말이에요.
[09:25] 그들이 출시한 것들. 다시,
[09:27] 저는 의도적으로 이것과 이것을 연결시키지 않을 것입니다.
[09:29] 내가 알기 때문에 아주 이상한 것을 만들어 보세요
[09:31] 그들이 보고 있는 화면이 확실하다는 것을.
[09:33] 자, 제가 여러분에게 제 모든 것을 보여주려는 건 아닙니다.
[09:35] 워크플로우인데, 제가 시작하면
[09:37] 이것을 위해 노력하는 것이 하나의 방법입니다.
[09:39] 매우 생산적인 업무
[09:41] AI 에이전트를 사용하여. 그리고 저는 그렇게 생각하지 않습니다.
[09:43] 그들은 이미 가진 것 외에는 아무것도 필요하지 않습니다.
[09:44] 지금 당신의 화면에서 보고 있는 것입니다. 와 함께
[09:46] 여러 대의 컴퓨터, 그들 자신의
[09:48] 작업 부하용 컴퓨터
[09:50] 움직일 수 없는 민감한
[09:51] 서버와 그 에이전트는 다음과 같습니다.
[09:53] 국가에 의해 적절하게 조직됨
[09:55] 예를 들어, 그들이 지금 있는 곳처럼요. 처럼
[09:57] 그들이 업무량을 잘 관리할 수 있기를 바랍니다.
[09:59] 이렇게 하는 거죠?
[10:01] 그러므로 그들은 마음속에 간직해야 합니다.
[10:03] 컴퓨터 특정 작업 부하
[10:05] 데이터 양이 매우 많다는 것을 아는 사람들 또는
[10:07] 그들이 자주 요구하는 것들이잖아요, 그렇죠?
[10:10] 제가 이렇게 말하는 이유는 다음과 같습니다.
[10:11] 지금 제 Mac OS에서는, 그중 하나가
[10:13] 제가 로컬에서 실행하는 워크플로
[10:15] 영상 편집 맞죠?
[10:17] 어쩌면 언젠가 옮길지도 몰라요
[10:19] 미래는 클라우드 컴퓨팅이지만, 문제점은 다음과 같습니다.
[10:21] 이렇게 이동하면 해당 파일들이 이동하게 됩니다.
[10:22] 클로드는 편집 중이며 AI가 편집하는 것들도 있습니다.
[10:24] 편집 중인 파일의 용량이 8GB에서 10GB가 넘습니다.
[10:26] 각각 몇 번씩이죠, 그렇죠?
[10:28] 그러므로 업로드와 다운로드에만 시간이 걸릴 것입니다.
[10:30] 몇 분 정도 걸립니다. 그런 다음,
[10:32] 아시다시피, 변화가 생기면 저는...
[10:34] 클로드와 이 친구들이 나오는 영상이니 꼭 보세요.
[10:36] AI 에이전트도 실수를 저지릅니다.
[10:38] 대개 그럴 수 없기 때문입니다.
[10:40] 보다. 그들에게 비전이 없는 것은 아닙니다.
[10:42] 진실? 설령 그들에게 시력이 있다 하더라도,
[10:44] 마치 시력을 가지고 있는 것 같지만, 오직 시력만 있는 것 같아요.
[10:46] 이미지. 음, 하지만 그럼에도 불구하고 그들은 저지릅니다.
[10:48] 많은 실수는 그들이 보지 못하기 때문에 발생합니다.
[10:50] 각 프레임마다 그렇죠? 그래서
[10:52] 내가 직접 봐야 한다는 것
[10:54] 영상. 그러니 이 모든 것을 하세요.
[10:56] 피드백 루프는 소모될 것입니다
[10:58] 데이터 양이 많아서 시간이 훨씬 더 오래 걸릴 것입니다.
[11:00] 내가 그에게 그냥 그렇게 해달라고 부탁하면...
[11:02] 제 컴퓨터에서 하는 거죠, 그렇죠? 그래서
[11:03] 그건 워크플로 중 하나예요.
[11:05] 제 시스템에서는 잘 작동합니다. 밖의
[11:07] 이것, 그 외의 모든 것, 아시잖아요,
[11:08] 소프트웨어 엔지니어링이요, 아시다시피요.
[11:10] 정상적인 기능 수행,
[11:11] 오류 수정 등 모든 것이 가능합니다.
[11:13] 가상 머신에 있는 거죠?
[11:15] 제게는 가상 머신이 하나 있는데...
[11:17] 나머지 프로젝트들도 모두 올리겠습니다.
[11:19] 저는 에이전트를 배정할 수 있습니다.
[11:21] 제가 작업하고 싶은 것들입니다.
[11:22] 예를 들어, 저는 곧 시작할 프로젝트가 있습니다.
[11:24] 제가 작업 중인 것입니다. 저는 가지고 있어요
[11:26] 제가 이미 참여하고 있는 다른 프로젝트들이 많이 있습니다.
[11:28] 저는 과거에 일한 경험이 있습니다. 그래서,
[11:30] 가상 머신, VM을 보유하는 것
[11:32] 이곳은 이러한 에이전트들을 관리하는 데 도움을 줍니다. 그리고
[11:34] 마지막으로, 적어도 클로드 코드에게는,
[11:36] 제가 지금 사용하는 유일한 것은 이것입니다.
[11:37] 내 휴대폰으로 원격 제어.
[11:39] 그러니까, 만약 그것이 실행 중이라면
[11:41] 가상 머신을 제어할 수 있습니다.
[11:42] 해당 기능을 사용하여 원격으로 세션을 진행합니다.
[11:44] Anthropic에서 통합되었습니다. 자, 그렇다면…
[11:45] 우리도 하나 있으면 정말 좋을 텐데.
[11:47] 호르도르 모바일 앱 같은 거요.
[11:48] 저는 그들이 그런 것을 출시했다고 생각하지 않습니다.
[11:50] 구체적으로 기계를 다음과 연결합니다.
[11:52] 여기서 앱을 사용해서 일하시는 분들
[11:54] 모바일 기기는 있지만, 필요 없을 것 같아요.
[11:56] 지금은 리모컨 때문에
[11:58] Anthropic은 완벽하게 작동합니다.
[12:00] 나만 빼고. 저는 어떤 오류도 발견하지 못했습니다.
[12:02] 이런 건 전혀 아니에요. 공장
[12:04] 정말 좋아요. 네, 저는 그러고 싶습니다.
[12:05] 즉, 그들은 가서 살펴볼 수 있습니다.
[12:07] 호르도르. 모든 링크는 여기에 남겨둘게요.
[12:08] 설명. 이것은 수정하기 매우 쉬워 보입니다.
[12:11] 적어도 인터페이스 측면에서는 그렇습니다.
[12:13] 개인용 컴퓨터를 가질 수도 있습니다.
[12:15] 로컬, 로컬 시스템, 그리고 당신은 할 수 있습니다
[12:16] 이 모든 에이전트를 갖기 위해
[12:18] 달리기, 아주 많이 들리네요
[12:19] 신나는. 솔직히 말하면, 아니에요.
[12:21] 그럼 에이전트 100명이 동시에 작동하겠죠?
[12:23] 진실? 적어도 혼자서는 안 돼. 만약 당신이
[12:26] 요원들이 다른 요원들에게 연락하는 것, 그게 전부입니다.
[12:28] 뭔가 색다른 것. 그리고 덧붙이자면, 호르도르
[12:30] 실제로 완전한 API를 지원합니다.
[12:32] 그것도 맞죠? 그래서, 클로드
[12:34] 코드는 아마 그것이 필요하지 않을 것입니다. 왜냐하면
[12:36] 그들은 최고 수준의 지원을 제공합니다.
[12:39] 하위 에이전트, 에이전트의 새로운 부분
[12:41] 그 자신 등. 하지만 사용할 수 있습니다.
[12:43] 호르도르 본인, 아시다시피, 간단히 말해서
[12:45] 새로운 하위 에이전트를 실행하고, 그들을 지휘하고
[12:47] 그럼, 모든 걸 보고하세요.
[12:49] 주요 대리인. 그러니까, 다시 말해, 그것은
[12:51] 에이전트가 사용할 수 있는 것
[12:52] 곧장. 걱정하지 않으셔도 돼요
[12:54] 그게 이유입니다. 한 가지 말씀드릴 수 있는 것은…
[12:56] C-Max는 확실히 비싸다
[12:58] 제가 가지고 있는 것보다 사용하기가 더 어렵습니다.
[13:00] 호르도르와 함께 목격됨. 몇 가지 참고 사항만 말씀드리겠습니다.
[13:02] 기말고사요. 제가 전에 얘기하겠다고 언급했었거든요.
[13:04] C-Max입니다. 그래서, 그중 하나는
[13:06] 제가 C-Max에서 발견한 문제는 다음과 같습니다.
[13:08] SSH는 제대로 작동하지 않습니다.
[13:10] 맞죠, 그렇죠? SSH를 사용할 수 있습니다.
[13:13] 음, 있잖아요, C-Max 같은 걸 해보는 건 어때요?
[13:15] SSH를 실행한 다음 SSH root 명령을 실행합니다.
[13:18] @ 무엇이든. 그리고 나서, 그때
[13:20] Command Shift B 같은 단축키를 누르면 됩니다.
[13:22] 터미널을 분할하면 다음과 같은 화면이 됩니다.
[13:24] 여기에도 터미널 하나, 여기에도 하나 더 있습니다. 둘 다
[13:27] SSH 서버에 직접 접속합니다. 그
[13:29] 여기서 문제는 C-Max를 닫으면 다음과 같은 일이 발생한다는 것입니다.
[13:31] 이제는 되돌릴 방법이 없습니다.
[13:33] 그러니까 당신은 그걸 잃어버렸군요. 설마
[13:34] 그것은 비슷한 것에서 실행되고 있습니다.
[13:36] 티맥스. 그러므로 당신이 해야 할 일은
[13:37] 해야 할 일은 C-Max SSH T-Max를 사용하는 것입니다.
[13:39] 실험적인 일인데 결과가 아주 좋았어요
[13:41] 문제가 있다. 정말 자주 고장나요.
[13:43] . 저는 그걸 봤어요. 예를 들어, 만약 당신이 진다면
[13:44] 인터넷 연결만 하면 됩니다.
[13:46] 그렇게 하면 터미널 에뮬레이터가 망가질 겁니다. ~ 안에
[13:47] 둘째로, 저는 맞춤 설정을 시도해 보았습니다.
[13:49] C-Max 인터페이스. 나는 심지어 내 가족에게 물어봤다.
[13:51] 일부 역할을 맡을 에이전트들,
[13:53] 설명을 삭제하는 방법
[13:54] 터미널 탭. 나는 할 수 없었다
[13:56] 놀라움을 주기 위해서 말이죠.
[13:58] 호르도르에는 뭔가 특별한 게 있어요, 그냥 느껴져요.
[14:01] 기본적으로 좋습니다. 없어요
[14:03] 내가 많은 노력을 기울여야 한다는 뜻이에요. 이건 간단합니다.
[14:05] 이거 좋네요. 저는 ~부터 시작할 수 있습니다.
[14:07] 별다른 소란 없이 즉시.
