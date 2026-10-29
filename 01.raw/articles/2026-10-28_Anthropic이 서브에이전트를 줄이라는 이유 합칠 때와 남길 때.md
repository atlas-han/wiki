---
title: "Anthropic이 서브에이전트를 줄이라는 이유: 합칠 때와 남길 때"
type: video
source: https://www.youtube.com/watch?v=kJGTHFZHLVg
site: youtube.com
author:
  - "[[Tech Bridge]]"
duration: 6:55
published: 2026-10-28
created: 2026-10-29
description: "Anthropic의 '서브에이전트를 스킬로 접기' 권고를 소개하는 영어 화자(이름 미상) 영상 발췌 + 한국어 해설(무캡션) 6:55, 공식 챕터 9. 한 에이전트 + 스킬이 거대 프롬프트 · 서브에이전트 팀을 이긴다는 주장, 조직도를 복제한 에이전트 팀(Conway's law)과 Franken-prompt, progressive disclosure, 접는 절차(10개 프롬프트 × 2회 기준선 → 서브에이전트 프롬프트를 SKILL.md 본문으로 → 같은 프롬프트로 재측정), 서브에이전트를 남길 세 경우(컨텍스트 팽창 · 도구 오선택 · 병렬 조사), 서로 의존하는 작업은 메인 에이전트에, 스킬이 만드는 busy work, 스킬을 줄여도 비용이 안 내려가는 반례. 원 블로그 · 논문 링크는 설명란에 없다."
tags:
  - clippings/youtube
---

**Source URL**: https://www.youtube.com/watch?v=kJGTHFZHLVg
**Channel**: Tech Bridge · **Duration**: 6:55 · **Published**: 2026-10-28

> **게시일.** info.json 기준 `upload_date` **`20261028`**(UTC), `timestamp` 1793224814(= **2026-10-29 07:00 KST**), `availability: public`. 2026-10-29 회차 목록에 처음 나왔다.
>
> **오디오 트랙과 자막 — 인용 규칙.** 오디오는 `Korean original (default)` + `English (US)`(더빙), 메타 `language`=`en`. 수동 자막 없음. `automatic_captions`에 **`ko-orig`가 없고**, 받은 **ko는 `lang=en&tlang=ko` 기계 번역**이다(10-28 TLC 편과 같은 패턴). `en`과 `en-orig`는 **md5 동일**(`lang=en` ASR). → **인용은 전부 en-orig**로 하고, ko는 참고용이다. `--sleep-subtitles 8`로 429 없음.
>
> **형식 — 영어 화자 발췌 + 무캡션 한국어 해설(추정).** en-orig는 한 영어 화자의 연속된 설명이고, 무캡션 간격 8곳 — 00:00~00:09 · 00:26~00:35 · 01:36~01:46 · 02:10~02:16 · 03:16~03:25 · 04:18~04:29 · 04:51~05:00 · 05:39~05:46 — 이 공식 챕터 경계(00:00 · 00:27 · 01:37 · 02:11 · 03:18 · 04:19 · 04:52 · 05:39)와 거의 겹친다. 설명란은 *"원음과 함께 따라갑니다"* 라고 하므로 **그 간격을 한국어 해설 구간으로 추정**한다. 해설 내용은 en-orig에도 ko에도 없어서 **쓰지 않는다.** 06:39 *정리와 마무리* 챕터도 en-orig는 06:39에서 끝난다.
>
> **화자.** 영어 화자의 이름 · 채널 · 원본 영상 링크가 발화 · 설명란 · 태그 어디에도 없다. 화자는 Anthropic을 3인칭으로(*"they're saying"*, *"Anthropic says"*) 인용하는 **해설자**다 — Anthropic 당사자가 아니다. → **Anthropic의 권고는 2차 진술로 다룬다.**
>
> ⚠️ **ASR 판독.** *"Tropic"* · *"Entropic"* · *"And Tropic"* → Anthropic. *"sub aent"* · *"multi- aent"* → sub agent · multi-agent. *"Franken prompt"* → Franken-prompt(Anthropic 용어라고 화자가 말함). *"Grockbot"* → GrokBot. *"claw code"* · *"clawed opus"* → Claude Code · Claude Opus. *"eternal evals"* → internal evals. *"agents.mmd"* → AGENTS.md. *"cash parts"* → cached parts. *"the agencies a short description"*(01:16) → *"the agent sees a short description"*(판독 추정). *"OpenClaw"*(00:51)는 원문 그대로.
>
> ⚠️ **끊긴 문장.** 03:14~03:23 *"keep the sub agent only if the folded version scores were [a]"* — 비교 기준(더 나쁠 때만 남긴다로 읽히지만)이 편집으로 잘렸다. 판정 기준을 추정해 쓰지 않는다.
>
> ⚠️ **수치 · 주장(전부 화자의 2차 진술, 원 출처 링크 없음).** 단일 루프가 멀티 에이전트보다 *"about twice as fast"*(한 고객 사례, 00:20~00:26) · Anthropic 멀티 에이전트 리서치 시스템이 단일 Claude Opus를 internal evals에서 *"by 90%"* 이김(04:00~04:07) · Cognition의 Flappy Bird 사례(04:35~04:45) · Microsoft Research와 두 대학의 논문(05:00~05:13) · *"A July paper shortens skills by up to 54%"*, 작업당 비용은 반드시 내려가지 않음(06:12~06:18). 화자 스스로 *"There's no pass rates or sample sizes"*(06:34~06:36)라며 Anthropic 가이드의 근거 부족을 지적한다.

## 설명란

서브에이전트를 많이 쓰면 AI가 일을 더 잘할까요?

Anthropic이 여러 서브에이전트를 하나의 에이전트 루프와 스킬로 합치라고 권하는 이유를 살펴봅니다. 같은 자료를 주고받는 구조에서 정보가 사라지는 문제와, 필요한 지침만 불러오는 방법을 원음과 함께 따라갑니다.

문맥 분리, 도구 제한, 병렬 조사처럼 서브에이전트를 남길 이유도 있습니다. 스킬과 상시 지침이 불필요한 절차를 만들 수 있는 경우, 문서를 줄여도 비용이 내려가지 않는 반례까지 함께 짚습니다.

작은 평가 과제를 준비하고, 하나씩 합친 뒤 같은 과제로 비교하는 방법을 소개합니다.

00:00 서브에이전트를 줄이면 더 잘할까
00:27 조직도처럼 나누면 생기는 문제
01:37 모델이 발전하면 하네스도 달라진다
02:11 스킬로 합쳐서 비교하는 방법
03:18 서브에이전트를 남겨야 할 때
04:19 내부 평가 수치와 서로 의존하는 작업
04:52 스킬과 상시 지침도 점검하기
05:39 줄인다고 비용도 줄어들까
06:39 정리와 마무리

#서브에이전트 #AI에이전트 #ClaudeCode #Anthropic #테크브릿지

## 트랜스크립트 — en-orig (영어 화자 ASR — 인용 근거)

[00:09] So, they're saying one agent with a set
[00:11] of skills was frequently beating both
[00:14] one giant prompt and a team of sub
[00:16] agents on quality. And it was often
[00:18] cheaper and faster, too. And who doesn't
[00:20] want fast and cheap? In one case, a
[00:22] customer tested their multi- aent setup
[00:24] against a single loop, and the single
[00:26] loop ran about twice as fast.
[00:35] Well, when it comes to software
[00:37] factories and running processes for
[00:39] companies, each team is building out its
[00:41] own set of agents and then someone holds
[00:43] an orchestrator on top to manage all
[00:45] these agents. And before long, you've
[00:47] got this agent team that is a copy of
[00:49] your org chart. We saw this a lot with
[00:51] OpenClaw. People were building in
[00:53] hundreds of agents and it just got way
[00:54] too complicated. So, this is called
[00:56] Conway's law. So the problem here is
[00:58] when agents are communicating, every
[01:00] handoff loses detail and then every team
[01:03] or every agent you're adding is going to
[01:04] add a system and a little bit more
[01:06] complexity to the system prompt. And
[01:07] Tropic actually have a word for this
[01:09] called the Franken prompt. So the fix
[01:11] for this is progressive disclosure. And
[01:13] we've seen this baked into how skills
[01:14] have been built for the last couple of
[01:16] months. So the agencies a short
[01:18] description of the skill and tools and
[01:20] then only loads the full thing only when
[01:22] it needs it. And this is a big part of
[01:24] how they cut down Claude codes prompt.
[01:26] So essentially, why would you load in
[01:28] all of the information if it's not
[01:30] necessarily going to be needed? Just
[01:32] give an indication that it's there and
[01:33] the agent can go look it up when it's
[01:35] required. And that keeps the context
[01:36] window nice and tidy.
[01:46] So why is all this simplification
[01:48] happening now? A lot of what we build
[01:50] around the model, like the sub agents
[01:52] and these long system prompts, is
[01:54] scaffolding for the models that we had
[01:55] like 6 months ago. With a lot of the
[01:58] newer models we're getting, all that
[01:59] complexity we've added has kind of
[02:01] stopped paying off. And in fact, it can
[02:03] actually be quite dangerous and distract
[02:05] the model from what it needs to be
[02:06] doing. And Tropic are saying you should
[02:08] only add complexity when it really
[02:10] demonstrates it improves the outcomes.
[02:16] So, how do you fold a sub agent? Well,
[02:18] Entropic says start with the sub aents
[02:20] that chain on each other's output. The
[02:22] ones that are touching the same data or
[02:24] get called together. Now, if a sub aent
[02:26] exists because its tools are locked down
[02:28] to a certain process, you want to leave
[02:30] that alone. Restricted tools are a
[02:31] reason to keep it. So, first of all, get
[02:34] your baseline. Use 10 varied prompts
[02:36] that should fire the sub aent and run
[02:38] each one twice. Track whether the right
[02:40] sub aent actually gets called with your
[02:42] prompt and whether it actually passes
[02:44] the test. So when it actually comes to
[02:45] folding it in in claw code, a sub aent
[02:48] file is a description plus a system
[02:50] prompt. Remember this is all just
[02:51] natural language. And then a skill is
[02:53] its description plus some instructions.
[02:56] So basically the sub aent prompt becomes
[02:58] the body of a new skill MD. And then you
[03:01] rewrite the description to say what it
[03:03] does and when to use it. Essentially,
[03:05] you're getting rid of the sub aent and
[03:06] just folding its functionality into a
[03:08] skill. So then move the old sub aent
[03:10] file aside instead of deleting it and
[03:12] then rerun the same prompts in a fresh
[03:14] session. And then keep the sub agent
[03:16] only if the folded version scores were
[03:23] a
[03:25] so when does a sub agent still earn its
[03:28] place? So entropic gives us three cases.
[03:30] So the first scenario is with context
[03:32] bloat. If you don't want your context
[03:34] window to get overloaded by all the
[03:36] research and content that's being
[03:37] flooded in, it might measurably hurt the
[03:39] main agent. What you can do there
[03:41] instead of course is use parallel sub
[03:43] agents who've got their own fresh
[03:45] context window and you can throw them
[03:46] away and they will summarize their
[03:48] findings and give it to the main agent.
[03:49] Another case is where one agent keeps
[03:51] picking the wrong tools. So in that
[03:53] case, you might split agents by context
[03:55] but not necessarily by org chart. The
[03:57] biggest win for sub agents is parallel
[04:00] research. In this case, Entropic's
[04:01] multi-agent research system beats single
[04:04] agent clawed opus by 90% on their
[04:07] eternal evals. Sub agents are also great
[04:09] for searching code bases and noisy side
[04:11] task like digging through logs and
[04:13] reviewers that are only going to read
[04:15] content. Of course, the downsides here
[04:16] is you're going to use a hell of a lot
[04:18] more tokens in this process.
[04:29] [music] And when it comes to writing or
[04:31] building something, uses of sub aent
[04:34] isn't always the best case. In an
[04:35] example from Cognition, they had one sub
[04:37] agent build a flappy bird background
[04:39] that looks a lot like Super Mario, and
[04:41] then another sub agent went and built a
[04:43] bird that did not match the background
[04:45] whatsoever. So, if you have steps that
[04:47] depend on each other, there's quick
[04:49] changes, lots of back and forth with
[04:51] you, then keep them in the main agent.
[05:00] So skills can also make busy work. A
[05:02] paper from Microsoft research and two
[05:04] universities [music] found that what
[05:07] ends up happening with skills is you're
[05:08] turning these validation checklists and
[05:10] construction recipes into mandatory
[05:13] work. If your skill says always run the
[05:16] full test suite, it might do that even
[05:18] if there's like a oneline change to a
[05:20] button in your code. You need to give
[05:21] the model a little bit of flexibility to
[05:23] decide when that's going to be overcare
[05:25] and then go and read your claude.md file
[05:28] or your agents.mmd file and ask yourself
[05:30] would the current model I'm using do
[05:33] this anyway without being told and if
[05:35] yes just cut it out and if you have time
[05:37] of course just run the eval after to
[05:39] test.
[05:46] Now, it's not straightforward. On the
[05:47] other side, harnesses don't always need
[05:50] to shrink. For an example, with
[05:51] Grockbot, it will run a coordinator bot
[05:54] and then have a fleet of workers. And
[05:57] because these bots are doing things that
[05:58] fall outside the realm of coding where
[06:01] our models have getting really good,
[06:02] they're actually adding certain guard
[06:04] rails back because these are areas that
[06:06] the models just really haven't nailed
[06:08] yet. Now, as a counterpoint, also
[06:09] trimming skills won't always fix your
[06:12] bill and reduce it either. [music] A
[06:13] July paper shortens skills by up to 54%
[06:17] and the cost per task didn't necessarily
[06:18] drop. In some cases, skills are small,
[06:21] mostly cash parts of what the agent
[06:23] reads. Cash, meaning that when they're
[06:24] brought in in the initial prompt, you're
[06:26] charged a lot less for them in
[06:27] subsequent turns of the agent. Also,
[06:30] Anthropic's guide here is just a pattern
[06:32] they're seeing from their customer work.
[06:34] There's no pass rates or sample sizes,
[06:36] so we can test it on our own setup. We
[06:38] just have to feel our way through this
[06:39] ourselves.

## 트랜스크립트 — ko (`tlang=ko` 기계 번역 — 참고용, 인용하지 않음)

[00:09] 그러니까, 특정 기술을 가진 한 명의 요원이
[00:14] 거대한 프롬프트 하나와 여러 하위
[00:16] 요원 팀을 모두 제치고 더 높은 품질의 결과를 자주 냈다는 거죠.  게다가
[00:18] 더 저렴하고 빠른 경우도 많았습니다.
[00:20] 빠르고 저렴한 걸 싫어하는 사람이 어디 있겠어요?  한 사례에서,
[00:22] 고객은 다중 구성 요소 설정을
[00:24] 단일 루프와 비교 테스트했는데, 단일
[00:26] 루프가 약 두 배 더 빠른 속도로 작동했습니다.
[00:35] 소프트웨어
[00:37] 개발 환경이나 기업 운영 프로세스에 있어서는
[00:39] 각 팀이
[00:41] 자체 에이전트 세트를 구축하고, 그 위에 오케
[00:43] 스트레이터를 설치하여 이러한 모든
[00:45] 에이전트를 관리하는 방식입니다.  그러다 보면 어느새
[00:49] 여러분의 조직도를 그대로 복사한 듯한 상담원 팀이 생겨나 있을 겁니다.  오픈클로에서 이런 현상을 많이 봤습니다
[00:51] .  사람들이
[00:53] 수백 개의 에이전트를 구축하면서 상황이 너무
[00:54] 복잡해졌습니다.  이것을
[00:56] 콘웨이의 법칙이라고 합니다.  문제는
[00:58] 상담원들이 서로 소통할 때, 인수인계 과정에서
[01:00] 세부 정보가 손실되고, 팀
[01:03] 이나 상담원을 추가할 때마다
[01:06] 시스템 관련 설명이 더 복잡해진다는 점입니다.  그리고
[01:07] 트로픽에서는 이것을 '
[01:09] 프랑켄 프롬프트'라고 부르는 용어를 사용합니다.
[01:11] 이 문제에 대한 해결책은 점진적 정보 공개입니다.  그리고
[01:13] 우리는
[01:14] 지난 몇
[01:16] 달 동안 스킬 개발 방식에 이러한 점이 반영되어 있는 것을 보아왔습니다.  그래서 에이전시는
[01:18] 기술과 도구에 대한 간략한 설명을 제공하고,
[01:22] 필요할 때만 전체 자료를 불러옵니다.  그리고 이것이 바로
[01:24] 그들이 클로드 코드 프롬프트를 줄이는 데 있어 큰 부분을 차지하는 방식입니다.
[01:26] 그러니까 본질적으로,
[01:30] 꼭 필요하지도 않은 정보를 왜 다 입력하겠어요?  해당 정보가 있다는
[01:32] 사실만 알려주시면,
[01:35] 필요할 때 상담원이 직접 확인해 볼 수 있습니다.  그렇게 하면 컨텍스트
[01:36] 창이 깔끔하게 유지됩니다.
[01:46] 그렇다면 왜 지금 이 모든 단순화가
[01:48] 일어나고 있는 걸까요?  우리가 모델을 중심으로 구축하는 많은 것들
[01:50] , 예를 들어 하위 에이전트
[01:52] 나 이러한 긴 시스템 프롬프트는
[01:55] 약 6개월 전에 우리가 가지고 있던 모델을 위한 뼈대 역할을 합니다.  최근 출시되는 많은 신형
[01:58] 모델에서는
[01:59] 우리가 추가했던 모든 복잡성이 더 이상 효과를 발휘하지 못하는 것 같습니다
[02:01] .  사실, 이는
[02:03] 상당히 위험할 수 있으며 모델이 해야 할 일에서 주의를 분산시킬 수 있습니다
[02:06] .  트로픽은
[02:08] 복잡성을 추가하는 것은 그것이
[02:10] 결과 개선에 실제로 도움이 된다는 것이 입증될 때만 해야 한다고 말합니다.
[02:16] 그렇다면 하위 에이전트는 어떻게 접는 걸까요?  엔트
[02:18] 로픽 이론에 따르면,
[02:20] 서로의 출력에 연결되는 하위 요소부터 시작하라고 합니다.
[02:22] 같은 데이터에 접근하거나
[02:24] 함께 호출되는 것들입니다.  만약 하위 엔티티가
[02:28] 특정 프로세스에 맞춰 도구가 제한되어 있기 때문에 존재하는 것이라면, 그것은
[02:30] 그대로 두는 것이 좋습니다.  사용이 제한된 도구는 해당 도구를
[02:31] 유지해야 하는 이유 중 하나입니다.  우선,
[02:34] 기준점을 정하세요.  하위 프로세스를 실행할 수 있는 10개의 다양한 프롬프트를 사용하고
[02:38] 각 프롬프트를 두 번씩 실행하세요.  프롬프트에
[02:40] 따라 올바른 하위 에이전트가 실제로 호출되는지,
[02:42] 그리고
[02:44] 테스트를 통과하는지 여부를 추적합니다.  그래서 실제로
[02:45] 클로 코드에 통합할 때, 하위 항목
[02:48] 파일은 설명과 시스템
[02:50] 프롬프트로 구성됩니다.  이 모든 것은 자연어라는 점을 기억하세요
[02:51] .  그리고 스킬이란 그 스킬에 대한
[02:53] 설명과 몇 가지 지침이 합쳐진 것입니다.
[02:56] 그러니까 기본적으로 하위 프롬프트가
[02:58] 새로운 스킬 MD의 본문이 되는 겁니다.  그런 다음
[03:01] 설명을 다시 작성하여 해당 기능이 무엇
[03:03] 이고 언제 사용해야 하는지 명시합니다.  기본적으로
[03:05] 하위 항목을 없애고
[03:06] 해당 기능을 스킬에 통합하는 것입니다
[03:08] .  그러면 기존 하위 항목
[03:10] 파일을 삭제하는 대신 다른 곳으로 옮긴
[03:12] 다음 새 세션에서 동일한 프롬프트를 다시 실행하십시오
[03:14] .  그리고 접힌 버전의 점수가 일정할 경우에만 하위 요원을 유지한다면,
[03:25] 하위 요원은 언제 여전히 그
[03:28] 자리를 차지할 수 있을까요?  따라서 엔트로피는 세 가지 경우를 제시합니다.
[03:30] 첫 번째 시나리오는 컨텍스트
[03:32] 블로트(context bloat)가 발생하는 경우입니다.  컨텍스트
[03:34] 창이 쏟아져 들어오는 모든
[03:36] 연구 자료와 콘텐츠로 과부하되는 것을 원하지 않는다면
[03:37] , 이는
[03:39] 메인 에이전트에 상당한 악영향을 미칠 수 있습니다.  물론, 그 대신에
[03:43] 자체적으로 새로운 컨텍스트 창을 가진 병렬 하위 에이전트를 사용할 수 있습니다. 이렇게 하면 하위 에이전트를
[03:45] 폐기할 수 있고, 하위 에이전트는 조사
[03:48] 결과를 요약하여 메인 에이전트에 전달할 수 있습니다.
[03:49] 또 다른 경우는 한 요원이 계속해서
[03:51] 잘못된 도구를 선택하는 경우입니다.  그런
[03:53] 경우에는 조직도 기준이 아니라 상황별로 담당자를 나눌 수도 있습니다
[03:55] .
[03:57] 하위 담당자에게 가장 큰 이점은 병행
[04:00] 조사입니다.  이 경우, 엔트로픽의
[04:01] 다중 에이전트 연구 시스템은 단일
[04:04] 에이전트 기반 시스템보다 영구 평가에서 90% 더 우수한 성능을 보였습니다
[04:07] .  서브 에이전트는
[04:09] 코드베이스 검색이나
[04:11] 로그 분석과 같은 번거로운 부가 작업, 그리고 콘텐츠
[04:13] 만 읽는 리뷰어 작업에도 매우 유용합니다
[04:15] .  물론, 단점은
[04:18] 이 과정에서 훨씬 더 많은 토큰을 사용하게 된다는 것입니다.
[04:29] [음악] 그리고
[04:31] 무언가를 쓰거나 만들 때, 하위 개념을 사용하는 것이
[04:34] 항상 최선의 선택은 아닙니다.
[04:35] Cognition의 한 예시에서, 한 하위
[04:37] 에이전트는 슈퍼 마리오와 매우 흡사한 플래피 버드 배경을 만들었고,
[04:41] 다른 하위 에이전트는 그
[04:43] 배경과 전혀 어울리지 않는 새를 만들었습니다
[04:45] .  따라서 단계들이
[04:47] 서로 의존적이거나, 변경 사항이 빠르게 발생하거나, 주고받는 작업이 잦다면
[04:51] , 해당 단계들을 메인 에이전트에 보관하세요.
[05:00] 따라서 기술은 때때로 단순한 단순 반복 작업이 될 수도 있습니다.
[05:02] 마이크로소프트 연구소와 두
[05:04] 대학(음악 분야)의 공동 연구 논문에 따르면,
[05:07] 기술 습득 과정에서 결국 발생하는 문제는
[05:08] 이러한 검증 체크리스트와
[05:10] 구성 방식이 의무적인
[05:13] 작업으로 변질된다는 것입니다.  스킬 설정이 '항상
[05:16] 전체 테스트 스위트 실행'으로 되어 있으면, 코드에서 버튼 하나
[05:18] 에 한 줄 정도의 변경 사항이 있더라도 전체 테스트 스위트를 실행할 수 있습니다
[05:20] .
[05:21] 모델이 과잉 대응이 될 시점을 스스로 판단할 수 있도록 약간의 유연성을 부여해야 합니다. 그런
[05:25] 다음 claude.md 파일
[05:28] 이나 agents.mmd 파일을 읽고
[05:30] 현재 사용 중인 모델이 별도의
[05:33] 지시 없이도 이러한 동작을 수행하는지 자문해 보세요. 만약 그렇다면 해당 부분을
[05:35] 삭제하고, 시간이 있다면
[05:37] 평가판을 실행하여
[05:39] 테스트하는 것이 좋습니다.
[05:46] 하지만 상황이 그렇게 간단하지는 않습니다.  반면에
[05:47] , 안전벨트가 항상 줄어들 필요는 없습니다
[05:50] .  예를 들어,
[05:51] Grockbot은 코디네이터 봇을 실행한
[05:54] 다음 여러 작업자 봇으로 구성된 팀을 운영합니다.  그리고
[05:57] 이 봇들은
[06:01] 우리 모델이 이미 상당히 발전한 코딩 영역 밖의 일들을 수행하기 때문에,
[06:06] 모델이
[06:08] 아직 완벽하게 파악하지 못한 부분에 대해 일종의 안전장치를 다시 추가하는 역할을 합니다.  하지만 반대로,
[06:09] 기술을 다듬는다고 해서 항상
[06:12] 청구서 금액이 줄어드는 것은 아닙니다.  [음악]
[06:13] 7월에 발표된 한 논문에 따르면 기술 습득 시간이 최대 54% 단축되었지만,
[06:17] 작업당 비용은 반드시
[06:18] 감소한 것은 아닙니다.  어떤 경우에는 기술이 사소하고,
[06:21] 주로 에이전트가 읽는 내용 중 현금과 관련된 부분에 불과합니다
[06:23] .  현금 결제는
[06:24] 초기 결제 시에 해당 품목을 가져오면
[06:27] 이후 에이전트와의 상담 시 훨씬 적은 금액이 청구된다는 것을 의미합니다.  또한,
[06:30] 앤트로픽의 이 가이드는
[06:32] 고객 작업에서 관찰된 패턴일 뿐입니다.
[06:34] 합격률이나 표본 크기에 대한 기준이 없으므로,
[06:36] 저희 자체 환경에서 테스트할 수 있습니다.  우리는 그저 직접 감각을 더듬어가며 이 상황을 헤쳐나가야 할 뿐이야
[06:39] .
