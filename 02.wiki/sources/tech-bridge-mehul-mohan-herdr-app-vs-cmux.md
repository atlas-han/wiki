---
title: "Tech Bridge — AI 에이전트를 다루는 새 작업 환경 herdr app | cmux와 비교 (Mehul Mohan): CLI의 유연성 · 원격 worker와 작업 지속 · 에이전트 상태 · 로컬과 VM · cmux"
type: source
tags: [herdr, cmux, claude-code, codex, agent-multiplexer, terminal, cli, permissions, remote-machines, ssh, vm, notifications, remote-control, subagents, user-review, video]
source-url: https://www.youtube.com/watch?v=D2yA1--RoKQ
source-type: video
author: Tech Bridge (영어 원본 편집본, 내레이션 없음) · 화자 [[mehul-mohan]](발화 호명 + 설명란 근거) · 원본 영상 링크 없음 · 녹화일 미상(herdr 앱 발표 당일이라고 화자 발화)
date-published: 2026-10-31
ingested: 2026-11-01
created: 2026-11-01
updated: 2026-11-01
---

# Tech Bridge — AI 에이전트를 다루는 새 작업 환경 herdr app | cmux와 비교 (Mehul Mohan)

[[tech-bridge|Tech Bridge]]의 **14:10 편집본, 공식 챕터 10, 내레이션 없음.** 오디오는 `English (US) original (default)`와 7개 언어 더빙뿐이고 한국어 트랙이 없다. `ko-orig`도 없고 ko는 `tlang=ko` 기계 번역이다. 10-27 Voss 편부터 이어진 **영어 원본 오디오만 있는 구성**이라 **인용은 en-orig로만** 한다. `upload_date`는 20261031(UTC)이고 게시 시각은 **2026-11-01 08:00 KST**다. raw: `01.raw/articles/2026-10-31_AI 에이전트를 다루는 새 작업 환경 herdr app - cmux와 비교.md`.

한 개발자가 **herdr가 터미널 안 도구에서 GUI 앱으로 나온 날** 몇 시간 써 보고 찍은 1인칭 화면 시연이다. 테제를 정리하면 이렇다.

> **에이전트 작업 환경은 CLI의 유연성(권한 플래그, 해킹 가능성)을 버리지 않고 그 위에 최소한의 GUI를 얹어야 한다. 그 GUI가 할 일은 셋이다. 여러 머신(로컬 · SSH · VM)에 에이전트를 흩어 두고, 앱이 닫혀도 계속 돌게 하고, 에이전트 상태를 한눈에 보여 주는 것이다. 무거운 데이터와 사람이 직접 봐야 하는 피드백 루프는 로컬에 남기고, 나머지는 VM에 보낸다.**

> *"basically a GUI application combined with CLIs"*(00:32~00:35) · *"CLI means flexibility"*(02:55~02:57) · *"Even if I quit the app, if I lose the Wi-Fi connection, whatever. Why? Because this was running on the worker."*(05:31~05:36) · *"something like this, like a agent multiplexer or agent manager sort of screen"*(08:33~08:35)

> ⚠️ **화자 신원은 발화 호명 + 설명란 근거다.** 시청자 질문을 옮기며 자기 이름을 부른다: *"Then why, Mehul, why do you prefer like CLI AI harnesses?"*(01:15~01:20). 성 Mohan은 설명란(*"개발자 Mehul Mohan이"*)에만 있다. 태그에는 이름이 없다. → [[mehul-mohan]].
>
> ⚠️ **1인 사용자의 수 시간 체감이다.** *"I've been using Hurder, this application, for the last few hours"*(08:00~08:02). herdr · cmux · Anthropic 쪽 확인 · 버전 정보가 없다. 화자는 처음부터 *"why I prefer this over C marks[=cmux]"*(00:56~00:58)라고 선호를 밝힌다.
>
> ⚠️ **ASR이 제품 이름을 매번 다르게 적는다.** herdr → *"holder"* · *"Horder"* · *"Hodor"* · *"Hurder"* · *"Herder"* · *"harder"*, cmux → *"C marks"* · *"C max"* · *"Cmux"*, Claude Code → *"cloud code"*. 아래 인용은 원문 그대로 두고 `[=…]`로 판독을 단다(raw 헤더 참고).

## 1. 소개 (00:00~00:22)

00:00~00:21은 자막이 없다. 한국어 트랙이 없으므로 타이틀이나 음악 구간으로 추정한다(영상 미확인). en-orig는 00:21 *"So, if you have been following me"* 로 시작한다.

## 2. herdr와 CLI (00:22~01:24)

- 화자는 두 도구를 오래 지켜봤다: *"I've been keeping an eye on C marks[=cmux] and holder[=herdr], these two tools for quite some time."*(00:23~00:27)
- 발표: *"today, holder[=herdr] specifically announced something interesting. They announced the app, a software that fits you, basically a GUI application combined with CLIs."*(00:27~00:35)
- 이전 herdr의 한계: *"holder[=herdr] messes up if I'm pressing command K for clearing the terminal. Because holder[=herdr] previously ran into terminal directly."*(00:43~00:49) — 화자가 cmux를 썼던 이유가 이것이었다(*"this was my whole point of using C marks[=cmux]"* 00:39~00:41). 새 앱은 그 점에서 cmux와 닮았다.
- 시청자 질문: 왜 [[codex|Codex]] 데스크톱 앱이나 Claude 데스크톱 앱 대신 CLI를 쓰나(01:02~01:17). 답: *"it's not that I prefer or I only use CLI harnesses. It's just that there are a couple of things with which CLI makes possible, which is just not possible otherwise."*(01:17~01:29)

## 3. CLI의 권한과 유연성 (01:24~03:39)

- 예시: *"somebody working at Claude code in Anthropic posted this that now, finally, they have a Claude code even more dangerously skip permissions flag."*(01:31~01:39)
- 화자의 불만: *"even if you're passing like is sandbox one and even the dangerously skip permissions flag, it still blocks you many, many times with some RMRF commands or something."*(01:46~01:55) · *"they basically made this dangerously skip permissions weaker."*(01:58~02:02)
- CLI에서는 환경 변수 두 개면 된다: *"Set the sandbox environment as one, set this one as one, and just hit enter."*(02:12~02:16) → *"you are inside a cloud code[=Claude Code] window that you know for a fact would not be interrupted again."*(02:18~02:22)
- ⭐ GUI에서는 번거롭다: *"This thing is very cumbersome to do in a GUI."*(02:27~02:28) 하네스마다 플래그와 권한 단계가 다르다 — *"cloud code[=Claude Code] supports auto mode, it supports this bypass permission mode, it supports like a bypass permission with an even more dangerous permission mode"*(02:45~02:53). 그래서 *"CLI means flexibility"*(02:55~02:57)다.
- 데스크톱 앱은 기능을 숨긴다: *"Desktop app has a bunch of features which are much more hidden than CLI. Like the even the dangerously bypass permission flag is hidden inside settings."*(03:11~03:21)
- 결론은 조심스럽다: *"I'm just saying that native apps and, you know, CLIs generally gives you a lot more flexibility and the ability to hack around compared to simple desktop apps."*(03:29~03:36)

> ⚠️ **플래그 주장은 미확인 2차 진술이다.** 게시자 이름, 링크, 플래그와 환경 변수의 정확한 이름이 발화에 없다(화면에만 있다). 기존 플래그가 *"weaker"* 해졌다는 것도 화자 체감이다. 위키의 [[anthropic-claude-code-auto-mode|auto mode]] 소스는 권한 단계를 **위험 행동을 걸러 내는 분류기** 쪽에서 설명했다. 이 화자는 같은 단계를 **끊기지 않는 자율 실행** 쪽에서 본다. 격리 환경 이야기 없이 *"even more dangerous"* 모드를 반기는 점은 [[agent-sandboxing]]의 Brennan 경고(skip permissions 에이전트는 *사용자가 가진 모든 것에 접근*)와 긴장한다. 다만 화자의 다른 작업은 VM에서 돈다(9장).

→ [[claude-code]] · [[deny-and-continue]]

## 4. 새 앱의 화면 구성 (03:39~04:37)

- 레이아웃 선택지: herdr 기본형(*"the sidebar, which has these terminals"* 03:50~03:52), 터미널만 보이는 형태(*"something like an iTerm"* 03:54~03:59), 레트로 테마(*"another 98"* 04:05 — Windows 98풍으로 추정).
- 레트로 테마 평: *"this is not the way to work if you're doing like serious work day-to-day"*(04:25~04:28). 화자는 graphite 테마를 쓴다(04:30~04:32).
- 외형 커스터마이즈 폭은 좁다: *"the customization is actually very less in terms of looks"*(03:44~03:46). 레이아웃은 7장에서 다시 나온다.

## 5. 원격 머신과 작업 지속 (04:37~06:37)

- ⭐ 여러 머신: *"it's very easy to manage your multiple machines here which was somewhat challenging with C max[=cmux]."*(04:37~04:41) `user@host`를 넣거나 SSH config에서 고르거나, *"you can ask your local AI agent itself to configure this"*(04:55~04:57). 화자는 원격 머신을 *"worker one"* 으로 이름 붙였다(05:00~05:03).
- ⭐ 비동기: *"Now all of this is async."*(05:09~05:11) 시연은 이렇다. worker에서 Claude에게 1부터 100까지 천천히 세게 하고 앱을 끈 뒤 다시 켜니 *"Claude is basically done"*(05:27~05:29)이었다. *"Even if I quit the app, if I lose the Wi-Fi connection, whatever. Why? Because this was running on the worker."*(05:31~05:36)
- 로컬도 앱 창과 분리된다: *"Hodor[=herdr] is maintaining a different process on this Mac OS which is keeping the processes keeping these terminals these agents alive."*(05:48~05:56)
- 로컬의 한계: *"Now on Mac, you don't get the guarantee if the Wi-Fi stops working or if your computer actually goes to sleep."*(05:56~06:02) → *"that is where these machines come into play, which is very, very important."*(06:04~06:07)
- 상태와 알림: *"it clearly separates like which agents are working"*(06:16~06:18), *"this is also dispatching notifications to me"*(06:25~06:27). 헤드폰을 끼고 음악을 듣는 중에도 쓸 만하다고 한다(06:27~06:34).

→ [[always-on-agent-architecture]] · [[cloud-agent-delegation]] · [[agent-attention-management]]

## 6. 에이전트 상태와 관리 (06:37~08:38)

- 여러 하네스: Codex 에이전트, *"Deep Seek and Open Code"*(06:45~06:48)를 띄울 수 있다.
- ⭐ 상태 통합: *"These agents provide first-class integration directly into the software, right? So, it will know like which when it is idle, when it is done, when is it working, and so on."*(06:52~06:59) 목록에 없는 에이전트도 쓸 수는 있지만 *"you might not have the best agents experience with those specific CLIs"*(07:04~07:07).
- 정체성: *"It uses minimal GUI, which is something that I really like, but at the same time gives me like a full terminal interface"*(07:17~07:24) — 터미널 에뮬레이터, SSH, VM, worker, 알림, 분할 패널.
- 시장: *"I know this field is super saturated"*(07:49~07:52).
- ⭐ 권고: *"don't restrict yourself with just simple interfaces of iTerm, just a single interface, just, you know, using tmux all across for managing agents."*(08:17~08:26) → *"you can be far more productive, in my opinion, if you're using something like this, like a agent multiplexer or agent manager sort of screen."*(08:29~08:35)

## 7. 바꿀 수 있는 작업 화면 (08:38~09:59)

- 화자 스스로 *"It seems almost like an overkill"*(08:44~08:46)라고 하면서 레이아웃을 보여 준다. *"a mission control dashboard sort of thing"*(08:50~08:52), *"a Slack-like preview UI"*(08:53~08:55), *"a Google Meet-like a call sort of UI where agents are on call and their terminals are there"*(08:59~09:03).
- *"It seems like this is extremely hackable, right, the new version that they have released."*(09:22~09:26) 화자는 이 레이아웃들을 일부러 연결해 보지 않았다(09:26~09:30).
- ⭐ 화자의 기준: *"I don't think that you need anything more than what you're seeing on your screen right now. With multiple computers, your own computer for the sensitive workloads that you can't move to servers, and your agents which are just organized properly by the state, like where they are right now."*(09:42~09:56)

## 8. 로컬과 VM의 역할 (09:59~11:35)

- ⭐ 원칙: *"you should go ahead and keep on your computer certain workloads that you know are very data heavy or requires you often"*(10:01~10:09)
- 예는 영상 편집이다. 파일이 *"north of like 8 10 GB files sometimes each"*(10:24~10:26)라 올리고 내리는 데만 몇 분이 걸린다. 게다가 에이전트가 영상을 제대로 못 본다. *"they make a lot of mistakes because they're because they're not seeing each and every single frame, right? So, I have to be to be the one who has to watch the video."*(10:47~10:55) 그래서 *"doing this whole feedback loop"*(10:55~10:57)는 로컬이 빠르다.
- 나머지: *"your software engineering and, you know, regular feature development, bug fixes, all of that, that that can sit on a VM"*(11:08~11:14) — VM 하나에 프로젝트를 다 두고 에이전트를 보낸다.

> 위키 연결: [[cloud-agent-delegation]]의 Rauch(*"you still want to be able to pull things down"*)와 Lauren Tan은 **로컬 = 관찰의 자리**라고 했다. 이 화자는 같은 결론을 **데이터 무게와 사람이 직접 보는 루프**라는 다른 근거로 낸다.

## 9. 모바일 제어와 하위 에이전트 (11:35~12:55)

- ⭐ Claude Code 원격 제어: *"the one thing that I use right now is remote control on my mobile phone. So, if it is running on virtual machine, I can remotely control the session using Anthropic's built-in feature."*(11:36~11:43) herdr 모바일 앱은 아직 없다고 본다(11:45~11:53). 그래도 *"the Anthropic's remote control works flawlessly at least for me"*(11:58~12:01)라서 필요하지 않다고 한다.
- 규모 감각: *"you would not have like 100 agents running, right? At least not by yourself. If your agents themselves invoke other agents, that's a different thing."*(12:21~12:28)
- herdr의 API: *"Hurder[=herdr] actually supports a complete API for that as well"*(12:28~12:32). Claude Code는 *"first-class support for sub-agents"*(12:36~12:38)가 있어 필요 없을 수 있다. 다른 에이전트는 herdr로 *"running new sub-agents, steering them, and you know, just reporting it back to the main agent"*(12:46~12:50)할 수 있다.

> ⚠️ Remote Control 링크는 설명란에 있으나 열어 보지 않았다. *"flawlessly"* 는 1인 체감이다. herdr API의 범위 · 형식은 발화되지 않는다.

## 10. cmux와 비교한 경험 (12:55~14:10)

- 총평: *"One thing I can say about Cmux is that it's definitely much more frictional to use than what I've seen with Hurder[=herdr]."*(12:54~13:00)
- ⭐ SSH: *"the SSH actually does not really work properly"*(13:07~13:10). `cmux ssh`로 서버에 붙어 터미널을 나눠도 *"if you quit Cmux now, there is no way to get this back"*(13:29~13:32)다. 이유는 *"it's actually not running in a tmux-like thing"*(13:34~13:36)이다. 우회책 *"Cmux SSH tmux"* 는 *"an experimental thing, and it's very frictional. It just breaks a lot."*(13:36~13:43) *"if you lose your internet connection, it'll just break your terminal emulator itself."*(13:43~13:46)
- UI: 에이전트에게 탭 설명 제거 같은 커스터마이즈를 시켜 봤지만 *"I was not able to get a wow factor from it"*(13:54~13:58)이었다. herdr는 *"overall by default looks pretty"*(14:00~14:02)고 *"I can get started right away without making a lot of fuss."*(14:04~14:07)라고 한다.

> ⚠️ **5장과 이 장이 같은 축이다.** herdr를 고른 결정적 이유는 **앱 · 연결이 끊겨도 세션이 남는가**다(원격은 worker, 로컬은 별도 프로세스). cmux 비판도 같은 축(SSH 세션이 앱과 함께 죽는다)이다. cmux 측 반론 · 버전 정보는 없다.

## 등장 개체

- 인물: [[mehul-mohan]](신규) · *"somebody working at Claude code in Anthropic"*(이름 없음)
- 제품 · 도구: [[herdr]](신규) · [[cmux]](신규) · [[claude-code]](권한 모드 · Remote Control · 서브에이전트) · [[codex]](데스크톱 앱 · 에이전트, 언급) · Claude 데스크톱 앱 · DeepSeek · OpenCode · iTerm · tmux(언급 수준, 페이지 연결 안 함)
- 조직: [[anthropic]](플래그 · Remote Control 제공자로 언급)
- 개념: [[always-on-agent-architecture]] · [[cloud-agent-delegation]] · [[agent-attention-management]] · [[agent-sandboxing]] · [[deny-and-continue]]
- 같은 범주의 다른 도구: [[conductor]] · [[agentcraft]] · [[warp]]

## 이 위키에서의 좌표

- *여러 코딩 에이전트를 한 화면에서* 다루는 도구로 [[conductor]] · [[agentcraft]]가 있었다. 둘 다 **만든 쪽의 발표**였고 **사용자가 둘을 비교한 소스**는 이 편이 처음이다. 비교 축도 다르다. Conductor는 worktree와 클라우드 샌드박스, AgentCraft는 게임 지도였다. 이 편은 **터미널과 SSH 세션이 살아남는가**를 본다.
- [[always-on-agent-architecture]]의 *노트북은 잠든다*(Katz)와 [[cloud-agent-delegation]]의 *노트북을 닫아도 돈다*가 **개인 개발자의 도구 선택 기준**으로 내려온다. 서버 하네스가 아니라 SSH worker와 로컬 데몬 프로세스로 같은 성질을 얻는다.
- [[agent-attention-management]]의 *무엇을 언제 보여 줄까*에 대한 가장 단순한 답이 나온다. idle · done · working 상태와 알림이다.

## ⚠️ 유보

- 녹화일 미상(화자: herdr 앱 발표 당일). 원본 영상 링크 없음.
- 화자 이름은 발화 호명(이름만) + 설명란(성). 소속 미상.
- Claude Code 새 플래그, 기존 플래그가 약해졌다는 주장, 환경 변수 이름은 모두 미확인이다.
- herdr · cmux 기능은 몇 시간 써 본 1인 체감이고 버전 정보가 없다. 설명란 링크 3개는 열어 보지 않았다.
- ASR 판독(herdr 6가지 표기, cmux 3가지, *"98"*, *"Hodor setting"*)은 raw 헤더 참고. ko는 기계 번역이라 인용하지 않았다. ko는 cmux의 *"frictional"* 을 *"비싸다"* 로 옮겼다.

## References

- raw: `01.raw/articles/2026-10-31_AI 에이전트를 다루는 새 작업 환경 herdr app - cmux와 비교.md`
- https://www.youtube.com/watch?v=D2yA1--RoKQ
- 설명란 링크(미열람): https://herdr.dev/ · https://cmux.com/ · https://code.claude.com/docs/en/remote-control
