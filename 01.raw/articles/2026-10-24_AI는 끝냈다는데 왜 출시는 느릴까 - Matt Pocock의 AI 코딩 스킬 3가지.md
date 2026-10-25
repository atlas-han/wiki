---
title: "AI는 끝냈다는데 왜 출시는 느릴까? Matt Pocock의 AI 코딩 스킬 3가지"
type: video
source: https://www.youtube.com/watch?v=vbdubFaBmfo
site: youtube.com
author:
  - "[[Tech Bridge]]"
duration: 5:28
published: 2026-10-24
created: 2026-10-25
description: "Tech Bridge 자체 해설 5:28, 공식 챕터 7. 설명란: 'Eric Tech가 소개한 Matt Pocock의 세 가지 스킬' — /implement-spec(의존 관계를 보고 일을 나눠 병렬로) · /pr(요약 · 근거 · 위험을 담은 검토 요청서) · /retro(다음 작업의 환경을 고친다). 발췌 화자는 Eric Tech로 추정(발화에 이름 없음), 원본 영상 링크는 없고 스킬 저장소 github.com/mattpocock/skills만 있다."
tags:
  - clippings/youtube
---

**Source URL**: https://www.youtube.com/watch?v=vbdubFaBmfo
**Channel**: Tech Bridge · **Duration**: 5:28 · **Published**: 2026-10-24

> **게시일.** info.json 기준 `upload_date` **`20261024`**(UTC), `timestamp` 1792832413(= **2026-10-24 18:00 KST**), `availability: public`. 2026-10-25 회차에 받았다. 멤버 전용을 거치지 않은 신규 업로드다.
>
> **오디오 트랙과 자막 — 인용 규칙.** 오디오 `Korean original (default)` + `English (US)` 2트랙, 메타 `language`는 `en`. 수동 자막 없음. 받은 **ko = `lang=ko` 원 오디오 ASR** — `ko`·`ko-orig` 바이트 동일(md5 `bda8f1c0…`). 영어 원음 발췌는 ko 트랙 안의 영어 ASR 조각. **en-orig = 영어(US) 트랙 ASR**(내레이션 더빙 추정, 발췌 구간은 원음). en = ko의 기계 번역. → **해설은 ko로 인용**, **발췌는 두 트랙 대조**. 더빙 내레이션은 인용하지 않는다. `--sleep-subtitles 8`로 429 없음.
>
> **원음 발췌 구간**(내레이션 전환으로 판정): ① **00:18~00:33** — *"Ale"*(00:30) 조각뿐, 사실상 **무캡션**. ② **00:56~01:27** /implement-spec — 01:07 이전 **무캡션**, 이후 *"[—] Pick dependencies to work them. This way we're going to have multiple different AI agents here working at the same times and it's going to process all the tickets much faster compared to what we had before. And eventually we going to have all those meringle[?] branch and it's going to [review? / process] it."*(끝: ko *"process it"*, en-orig *"toeview it"* — 미판정). ③ **01:49~02:15** /pr 다이어그램 — 02:03 이전 **무캡션**, 이후 *"[—] other summaries that we seen what my will do is in that skill it will basically just try to create diagrams rather than just bunch of words that we have to read through and understandations[?]"*. ④ **02:41~03:17** 근거와 merge danger — *"[—] AI here to actually look at the performance actually improve the performance at all. Do we have a screenshot? Do we have testing passing? Right? Do we have any proof that this is actually working? rather than be like ok well should be fine. So the second part here is evidence and the third part here is the merge danger. Let's say if this po quest[=pull request] breaks what is impact in production can we actually roll back if something happen and also what is the blast radius how much this change impacts if something goes wrong and worse before[?]"*. ⑤ **03:37~04:25** /retro 컨텍스트 — 03:54 이전 **무캡션**, 이후 *"[—] for our AI agents. Now let's start with the context. Essentially the way how it works is let's say we have AI agents try to complete a bug fix or complete a feature. Sometimes it might take long time for AI agent here to finding the right information. So maybe we to create a uh AGMD[?] file and this AGMD file contains a list of key files on exactly where they are and how to find them more quickly. Right?"* ⑥ **04:47~05:03** — **두 트랙 모두 무캡션**(발췌인지 미판정).
>
> **화자.** 설명란 *"Eric Tech가 소개한 Matt Pocock의 세 가지 스킬"*, 내레이션 00:07~00:11 *"에릭테크가 소개한 매트 포[콕]의 세 가지 스킬"*. **발췌 속 화자는 이름을 말하지 않는다** — 발췌 ③의 *"what my will do is in that skill"*(Matt's will? 판독 불가)로 보아 **스킬을 만든 사람이 아니라 소개하는 사람**의 목소리로 읽힌다 → **Eric Tech로 추정**. Matt Pocock 본인 목소리로 확정되는 구간은 없다. Eric Tech 원본 영상의 제목·날짜·링크는 **설명란에 없다** — 링크는 스킬 저장소 <https://github.com/mattpocock/skills> 하나(열어 보지 않았다).
>
> **해설이 스스로 가른 것.** 02:33~02:38 *"이 예시는 저희가 이해를 돕기 위해 든 거예요"*(로그인 수정 전 실패/수정 후 성공 예시). 05:13 *"저희가 주목한 건"* — 맺음은 Tech Bridge의 관점이다.
>
> ⚠️ **ASR 판독.** ko 내레이션: "출신은"(00:03) → 출시는 · "매트 포의" → Matt Pocock · "에릭테크" → Eric Tech · **"much은"(00:33) → PR은**(en-orig 더빙 *"A pull request is a procedure to request a review"*) · "앞작업" → 앞 작업 · "한갈래" → 한 갈래 · "해요.이"(02:33) → 해요. 이 · "위해든" → 위해 든 · **"진한 작업"(03:37) → 지난 작업** · **"세스를"(05:03) → [프로]세스를** · 끝 *"M."* 판독 불가. 발췌: *"meringle"*(merge? 판독 불가) · *"po quest"* → pull request · *"AGMD"* — AGENTS.md 또는 agent.md 류로 보이나 **확정하지 않는다** · *"understandations"* · *"worse before"* 판독 불가.

## 설명란

AI가 코드를 빨리 짜 주는데, 왜 출시는 여전히 느릴까요?

Eric Tech가 소개한 Matt Pocock의 세 가지 스킬을 바탕으로, 구현부터 검토와 회고까지 이어지는 흐름을 쉽게 풀어봅니다. /implement-spec은 의존 관계를 보고 작업을 나누고, /pr은 변경 내용의 근거와 위험을 보여 주며, /retro는 다음 작업에서 같은 실수를 줄일 방법을 찾습니다.

챕터
00:00 AI는 끝냈다는데 왜 출시는 느릴까?
00:33 /implement-spec · 먼저 시작할 수 있는 일부터
01:27 /pr · 사람이 빠르게 검토하려면
02:20 완료했다는 말 옆에 확인한 결과를
03:16 /retro · 반복되는 실수를 줄이는 방법
04:25 자동 검사와 사람이 판단할 기준
05:03 만들기 → 확인하기 → 다음에 반영하기

Matt Pocock의 스킬 저장소
https://github.com/mattpocock/skills

#AI코딩 #MattPocock #ClaudeCode #테크브릿지

> info.json `tags`: AI 에이전트 · AI 코딩 · Claude Code · Matt Pocock · PR · implement-spec · retro · 코드 리뷰 · 테크브릿지

## 트랜스크립트 — ko (원 오디오 ASR, `lang=ko`)

> 타임스탬프는 json3 이벤트 시작 시각(초 단위 내림). 연속 중복 줄만 제거했고 오인식은 고치지 않았다 — 판독은 위 헤더.

[00:00] AI가 코드를 빨리 짜 주는데 왜
[00:03] 출신은 여전히 느릴까요? 완성됐다는
[00:06] 말만으로는 안심할 수 없기
[00:07] 때문이에요. 오늘은 에릭테크가 소개한
[00:11] 매트 포의 세 가지 스킬을
[00:12] 살펴볼게요. 작업을 나누고 결과를
[00:16] 확인하고 같은 실수를 줄이는
[00:18] 방법이에요.
[00:30] Ale
[00:33] much은
[00:34] 바꾼 코드를 합치기 전에 검토를
[00:37] 요청하는 절차예요. 코드가 쌓이면
[00:40] 확인하는 사람이 기다림의 원인이 될
[00:42] 수 있어요. 그런데 확인할 코드가
[00:45] 나오기 전에도 기다림이 있죠. 일감을
[00:48] 하나씩 골라 AI에게 넘기는
[00:50] 일이에요. 첫 번째 스킬은 먼저
[00:53] 끝나야 할 일이 있는지 살피고 바로
[00:56] 시작할 수 있는 일을 나눠줘요.
[01:07] Pick dependencies
[01:10] to work them. This
[01:11] way we're going to
[01:12] have multiple
[01:12] different AI agents
[01:13] here working at the
[01:14] same times and it's
[01:15] going to process all
[01:15] the tickets much
[01:16] faster compared to
[01:17] what we had before.
[01:18] And eventually we
[01:19] going to have all
[01:19] those meringle
[01:21] branch and it's
[01:23] going to
[01:26] process it.
[01:27] >> 동시에 일한다고 모든 일을 한꺼번에
[01:30] 시작하는 건 아니에요. 앞작업이
[01:32] 끝나야 시작할 수 있는 일은 기다려야
[01:34] 하죠. 서로 독립적인 일부터 진행하고
[01:38] 결과를 한갈래에 모으는 거예요. 이제
[01:41] 검토할 사람이 바뀐 내용을 빠르게
[01:43] 이해해야 해요. 두 번째 스킬은 검토
[01:46] 요청서에 요약, 근거, 위험을
[01:49] 담아요.
[02:03] other summaries that
[02:03] we seen what my will
[02:05] do is in that skill
[02:06] it will basically
[02:07] just try to create
[02:07] diagrams rather than
[02:08] just bunch of words
[02:10] that we have to read
[02:10] through and
[02:11] understandations
[02:14] diagram here that
[02:15] way
[02:23] 줘요. 하지만 그림이 깔끔하다고
[02:25] 코드가 제대로 작동하는 건 아니죠.
[02:28] 예를 들어 로그인을 고쳤다면 수정
[02:31] 전에는 실패했고 수정 후에는
[02:33] 성공했다는 결과를 보여 줘야 해요.이
[02:36] 예시는 저희가 이해를 돕기 위해든
[02:38] 거예요. 검토자는 확인한 결과를 보고
[02:41] 판단할 수 있어야 해요.
[02:45] AI here to actually
[02:46] look at the
[02:47] performance actually
[02:48] improve the
[02:48] performance at all.
[02:49] Do we have a
[02:50] screenshot? Do we
[02:51] have testing
[02:52] passing? Right? Do
[02:53] we have any proof
[02:54] that this is
[02:55] actually working?
[02:56] rather than be like
[02:56] ok well should be
[02:57] fine. So the second
[02:58] part here is
[02:59] evidence and the
[03:00] third part here is
[03:01] the merge danger.
[03:02] Let's say if this po
[03:03] quest breaks what is
[03:04] impact in production
[03:05] can we actually roll
[03:06] back if something
[03:07] happen and also what
[03:08] is the blast radius
[03:09] how much this change
[03:10] impacts if something
[03:11] goes wrong
[03:13] and worse before
[03:17] >> 잘못됐을 때 되돌릴 수 있는지
[03:19] 어디까지 영향을 주는지도 중요해요.
[03:22] 위험을 적는다고 검토가 없어지는 건
[03:24] 아니에요. 어디를 더 꼼꼼히 봐야
[03:26] 할지 알려 주는 거죠. 그런데 작업이
[03:29] 끝나도 남는 문제가 있어요. 다음
[03:32] 작업에서 똑같은 곳을 헤매고 같은
[03:34] 실수를 반복하는 거예요. 세 번째
[03:37] 스킬은 진한 작업을 돌아봐요.
[03:54] for our AI agents.
[03:55] Now let's start with
[03:56] the context.
[03:57] Essentially the way
[03:58] how it works is
[03:59] let's say we have AI
[04:00] agents try to
[04:01] complete a bug fix
[04:02] or complete a
[04:03] feature. Sometimes
[04:04] it might take long
[04:05] time for AI agent
[04:06] here to finding the
[04:07] right information.
[04:08] So maybe we to
[04:09] create a uh AGMD
[04:11] file and this AGMD
[04:12] file contains a list
[04:13] of key files on
[04:15] exactly where they
[04:16] are and how to find
[04:17] them more quickly.
[04:19] Right?
[04:25] 파일 위치를 알려주면 다음에는 찾는
[04:28] 시간을 줄일 수 있어요. 실수도
[04:30] 종류를 나눠 봐야 해요. 금지된
[04:33] 함수를 썼는지처럼 기계가 확인할 수
[04:35] 있는 일은 자동 검사로 막을 수
[04:37] 있죠.
[04:38] 판단이 필요한 기준은 사람이 읽을
[04:40] 규칙으로 남겨요. 다만 회고를 계속
[04:44] 자동으로 돌리면 기능보다 정리 작업만
[04:47] 늘어날 수 있어요.
[05:03] 세스를 한 줄로 이어볼게요. 의존
[05:06] 관계를 보고 일을 나누고 검토할
[05:09] 근거와 위험을 모으고 다음 작업의
[05:11] 환경을 고쳐요.
[05:13] 저희가 주목한 건 더 많은 코드를
[05:16] 만드는 속도만이 아니에요. 사람이
[05:18] 확인하고 다음에는 덜 헤매게 만드는
[05:20] 흐름이에요. 지금 쓰는 AI는
[05:23] 완료했다는 말 뒤에 어떤 근거를
[05:26] 보여주나요? M.


## 트랜스크립트 — en-orig (영어(US) 트랙 ASR — 내레이션은 더빙 추정, 발췌 구간은 원음 · 발췌만 대조 인용)

[00:00] AI writes code quickly, so why is the
[00:03] output still slow? Because you can't be
[00:06] at ease just because it's "finished."
[00:09] Today, we’ll look at the three skills
[00:11] of Metaphor introduced by Eric Tech.
[00:14] It’s about dividing tasks, verifying
[00:16] results, and reducing repetitive
[00:18] mistakes. Ale A pull request is a
[00:34] procedure to request a review before
[00:37] merging changed code. When code piles
[00:40] up, the person reviewing it can become
[00:42] a bottleneck. But there is also waiting
[00:45] before the code to be reviewed even
[00:47] appears. It’s the job of picking
[00:49] tasks one by one and handing them to
[00:51] the AI. The first skill checks for
[00:53] prerequisites and separates tasks that
[00:56] can start immediately. Pick
[01:08] dependencies to work them. This way
[01:12] we're going to have multiple different
[01:13] AI agents here working at the same
[01:14] times and it's going to process all the
[01:16] tickets much faster compared to what we
[01:17] had before. And eventually we going to
[01:20] have all those meringle branch and it's
[01:22] going toeview it.
[01:27] >> Working simultaneously doesn't mean
[01:29] starting everything all at once. Tasks
[01:32] that require previous work to be
[01:34] completed must wait. We proceed with
[01:36] independent tasks first and merge the
[01:38] results into one branch. Now, the
[01:41] reviewer must quickly understand what
[01:43] has changed. The second skill includes
[01:47] a summary, evidence, and risks in the
[01:49] review request. other summaries that we
[02:04] seen what my will do is in that skill
[02:06] it will basically just try to create
[02:08] diagrams rather than just bunch of
[02:09] words that we have to read through and
[02:11] understandations The diagram here shows
[02:17] the path of what has changed rather
[02:21] than just text. But just because the
[02:25] diagram is neat doesn't mean the code
[02:27] works properly. For instance, if you
[02:30] fixed a login, you should show results
[02:32] proving it failed before and succeeded
[02:34] after. We provided this example to help
[02:37] with your understanding. The reviewer
[02:40] needs to be able to make a judgment
[02:41] based on the verified results. AI here
[02:46] to actually look at the performance
[02:47] actually improve the performance at all
[02:49] . Do we have a screenshot? Do we have
[02:51] testing passing? Right? Do we have any
[02:54] proof that this is actually working?
[02:56] Rather than be like, Ok, well, should
[02:57] be fine. So, the second part here is
[02:59] evidence, and the third part here is
[03:01] the merge danger. Let's say if this po
[03:03] quest breaks, what is impact in
[03:04] production? Can we actually roll back
[03:06] if something happen? And also, what is
[03:08] the blast radius? How much this change
[03:11] impacts if something goes wrong and
[03:14] worse before?
[03:17] >> It is also important to know if you can
[03:19] roll back and how far the impact
[03:20] reaches if things go wrong. Writing
[03:22] down risks doesn't mean the review
[03:24] process disappears. It tells you where
[03:26] you need to look more closely. But
[03:28] there is a problem that remains even
[03:30] after the work is done. You end up
[03:32] wandering in the same places and
[03:34] repeating the same mistakes in the next
[03:36] task. The third skill is to look back
[03:38] on past tasks. For our AI agents. Now,
[03:55] let's start with the context. Now,
[03:57] essentially, the way how it works is,
[03:59] let's say we have AI agents try to
[04:01] complete a bug fix or complete a
[04:02] feature. Sometimes, it might take long
[04:05] time. for AI agent here to finding the
[04:07] right information. So maybe we to
[04:09] create a uh AGMD file and this AGMD
[04:12] File contains a list of key files on
[04:14] exactly where they are and how to find
[04:17] them more quickly. Right? If you
[04:25] provide the file locations, you can
[04:27] reduce the time spent searching next
[04:29] time. You also need to categorize the
[04:31] types of mistakes. Issues a machine can
[04:33] verify, like using a forbidden function
[04:35] , can be blocked by automated checks.
[04:38] For criteria that require judgment,
[04:39] leave them as rules for humans to read.
[04:42] However, if you keep running
[04:43] retrospectives automatically, you might
[04:45] end up with more cleanup work than
[04:47] actual features. Let's connect these
[05:04] processes into a single line. Analyze
[05:06] dependencies, divide the work, gather
[05:08] grounds and risks for review, and
[05:10] improve the environment for the next
[05:12] task. What we focused on is not just
[05:15] the speed of producing more code. It is
[05:18] a workflow where humans verify the
[05:20] results, leading to less wandering next
[05:21] time. What kind of evidence does the AI
[05:24] you currently use provide after saying
[05:26] it's finished?

