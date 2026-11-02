---
title: "[한글자막] Claude Code, 완료했다고 끝이 아니다 | 검증과 리뷰 루프 만들기"
type: video
source: https://www.youtube.com/watch?v=IGTdL4IPLq8
site: youtube.com
author:
  - "[[Tech Bridge]]"
duration: 14:00
published: 2026-11-01
created: 2026-11-02
description: "AI Labs(설명란 근거 — 발화에 이름 없음, 1인칭 복수 'we')가 Anthropic Claude Code 팀의 코드 리뷰 방식(설명란 링크 'solving-code-review-at-anthropic', 열어 보지 않음)을 소개하고 자기 구현을 붙인 해설 영상 14:00, 공식 챕터 11, 내레이션 없음 · 영어 원본 오디오만. Anthropic 쪽(발표자 전달): 리뷰할 변경 하루 약 2,500 → 30,000+(4개월), 질문을 '누가 읽었나'에서 '무엇이 잘못될 수 있고 어떻게 잡나'로, 빌드 중 검사, 완료 대신 증거(테스트 · 디자인 대비 스크린샷), 별도 리뷰어 에이전트(Team · Enterprise), 가벼운 판본 code review 명령(effort level), REVIEW.md, 반복 실수 → 지시문 수정, classifier로 위험 분류, 50회+ 왕복 · 59% 재보고 → 세 규칙(3라운드 후 재설계 · 변경분만 · 문제 종류 명시), 몇 분 안 되돌리기 · 매일 직접 사용. AI Labs 구현: write-eval 스킬(eval.md · 목업 · 사람 승인 · 완료 차단 훅), review.md를 CLAUDE.md에 링크, review-loop 스킬(orchestrator · builder · verifier · reviewer, state.md, 5라운드 · 2라운드 정체 종료), 학습 규칙 섹션, 위험 등급 스킬, 코드를 못 읽는 first-time user 에이전트, fix-a-bug 스킬 · Git 브랜치."
tags:
  - clippings/youtube
---

**Source URL**: https://www.youtube.com/watch?v=IGTdL4IPLq8
**Channel**: Tech Bridge · **Duration**: 14:00 · **Published**: 2026-11-01

> **게시일 — UTC/KST 날짜가 갈린다.** info.json 기준 `upload_date` **`20261101`**(UTC), `timestamp` 1793569526(= 2026-11-01 21:45:26 UTC = **2026-11-02 06:45 KST**), `availability: public`, `release_date` 없음, `live_status: not_live`. 이 채널 관례대로 파일명 · `published`는 `upload_date`(2026-11-01)를 쓴다. 한국 시간으로는 11-02 아침 게시다. 파일명에서 제목 앞의 `[한글자막]`과 `,`는 빼고 `|`는 ` - `로 바꿨다.
>
> **오디오 트랙과 자막 — 인용 규칙.** 10-27 Voss 편부터 이어진 **영어 원본 오디오만** 있는 구성이다. 오디오는 **`English (US) original (default)`** 가 원본이고 나머지(fr-FR · de-DE · hi · id · it · pt-BR · es-US)는 더빙이다. **한국어 오디오 트랙이 없다.** 메타 `language`=`en`. **수동 자막(`subtitles`)은 비어 있다** — 제목의 "[한글자막]"은 YouTube 자막 파일이 있다는 뜻이 아니다(번인 자막 여부는 영상을 보지 않아 미확인). `automatic_captions`(164키)에 **`ko-orig`가 없고**, ko는 `kind=asr&lang=en&variant=gemini&tlang=ko` 기계 번역이다. en-orig URL은 `kind=asr&lang=en&variant=gemini`. 더빙 트랙 쪽 `fr-orig` · `de-orig` · `hi-orig` · `id-orig` · `it-orig` · `pt-orig` · `es-orig` 키가 있다(받지 않았다). 인용은 **en-orig로만** 한다.
>
> ⚠️ **`en` 파일은 en-orig와 다르다(md5 불일치)** — info.json `en`의 첫 json3 URL 파라미터는 en-orig와 같은데(`lang=en&variant=gemini`, `tlang` 없음) 내용은 고쳐 쓴 문장이다(10-30 Osmani 편 이후 같은 현상). 뜻이 바뀌는 곳: en-orig *"Before a change goes anywhere, they ask Claude to run something that proves it works"*(02:23~02:26) → en *"Before implementing any changes, they ask Claude to run something that tests its functionality"* — **'변경을 내보내기 전'이 '구현하기 전'으로 바뀐다.** en은 feature를 "function", builder를 "construction (…) agents", change를 "switch"(10:07)로 옮긴다. en · ko는 462줄, en-orig는 416줄. 둘 다 인용 근거가 아니다.
>
> **형식 — 1인 해설 · 화면 시연 영상, 내레이션 없음.** en-orig 첫 큐는 **00:22.9**(*"As the models get better, reviewing what your agent builds matters even more…"*)이고 문장의 시작이다. **00:00~00:22(첫 공식 챕터 *"소개"* 00:00~00:23 거의 전체)는 무캡션**이다 — 타이틀 또는 한국어 훅으로 추정, 미확인. 그 뒤로는 끝까지 **3.5초를 넘는 큐 간격이 없다**(최대 3.44초: 00:46.5 · 03:17.7, 모두 문장 중간). 마지막 큐는 13:57(837.4초 시작, *"it and roll back to an earlier version."*)으로 문장이 끝나고, 영상 길이 14:00과 맞물린다 — 맺음말 · 구독 권유 없이 끝난다(원본에서 잘렸는지는 미확인). en-orig에 `[snorts]` 태그가 세 번(01:30 · 09:53 · 11:30) 있다.
>
> **화자 · 원 제작자.** 발화에 이름이 없다. **설명란**(*"AI Labs가 앤트로픽 Claude Code 팀의 코드 검토 방식을 바탕으로 구성한 평가·리뷰 워크플로"*)에만 AI Labs가 나온다 — info.json `tags`(AI 에이전트 · AI 코딩 · Anthropic · Claude Code · 개발 · 코드 리뷰)에는 없다. 발화 단서는 **1인칭 복수 채널 화법**이다: *"We've shown many ways to give Claude evals in our earlier videos."*(02:53~02:55), *"we turned that into a skill"*(02:59~03:00), *"In the demo app we were testing on"*(03:00~03:02), *"Our review loop works the same way"*(11:12~11:14). 위키의 이전 AI Labs 두 편(09-05 · 09-15)도 *"we"* 로만 말하고 개인 이름이 없었다. → **원 제작자 AI Labs(설명란 근거), 발표자 개인 미상.** 목소리 동일성은 확인하지 않았다. 원본 영상 링크는 설명란에 없다.
>
> ⚠️ **두 층의 주장 — Anthropic 팀 관행(발표자가 전달) vs AI Labs 구현.** 설명란도 *"AI Labs가 제안한 구현과 앤트로픽 팀의 실제 프로세스는 구분해 설명합니다"* 라고 단다. 발화에서는 *"The Claude code team …"* · *"Anthropic's article on this says …"* 가 Anthropic 쪽, *"we turned that into a skill"* · *"You can ask Claude to create a skill …"* · *"Our review loop …"* 가 AI Labs 쪽이다. **Anthropic 쪽 숫자 · 관행은 모두 발표자가 기사를 요약한 2차 전달**이고, 설명란 링크(`https://claude.dev/blog/solving-code-review-at-anthropic/` · `https://code.claude.com/docs/`)는 **열어 보지 않았다** — 위키는 기사 원문과 대조하지 않았다. 경계가 흐린 곳: 위험 3등급(낮음 · 중간 · 높음, 09:13~09:38)은 *"You can sort your own changes as well"* 뒤에 나와 Anthropic classifier의 기준인지 발표자 제안인지 불분명하다. *"People's main complaint about Anthropic's article was that it only works if you have unlimited tokens. So, the team added three rules"*(10:26~10:32)의 **인과(불만 → 규칙 추가)는 발표자 화법**이고, 세 규칙이 기사 원문에 있었는지 · 불만 이후 추가됐는지는 미확인이다.
>
> **시점.** 업로드일 ≠ 녹화일. 날짜 단서는 *"in just 4 months"*(00:49, 기간의 기준 시점 미발화)와, 기사에 대한 반응이 이미 있었다는 진술(10:26~10:30)뿐이다. 모델명은 나오지 않는다.
>
> ⚠️ **ASR 판독.** *"Claude code"* → [[claude-code|Claude Code]]. *"rd.md file that listed the requirements"*(03:10~03:13) → 요구사항 문서 파일 — **PRD.md · RD.md 중 무엇인지 미확정**(AI Labs의 이전 편은 PRD를 썼다). *"the right eval skill"*(07:12 · 07:49) · *"the right eval scale"*(09:47) → 앞에서 만든 **eval 작성 스킬(write-eval 추정)**. *"turn that question into a scale that rates each feature"*(09:38~09:39) · *"run the scale"*(09:43) → **skill**(scale/skill 혼동 추정 — 문맥상 스킬로 만드는 이야기). *"give it away to prove it did the work right"*(02:38~02:41) → *a way*. *"review.md"* → 설명란 표기 `REVIEW.md`. *"code review command"* → Claude Code의 코드 리뷰 명령(정확한 명령 문자열은 발화되지 않음). *"Claude code teams reviewer"*(08:18) → team's. *"it's guess"*(13:35~13:37) → its.
>
> ⚠️ **ko(기계 번역)는 인용 근거가 아니고 뜻을 바꾸는 곳이 있다.** 00:49 *"약 2,500명에서 30,000명 이상으로"* — en-orig는 **리뷰할 변경의 수**(*"the number of changes to review every day went from about 2,500 to over 30,000"* 00:44~00:49)이지 사람 수가 아니다. 03:50 훅을 *"독자의 관심을 끌 만한 '후크'"* 로 옮긴다(en-orig는 에이전트 훅, *"create a hook that makes sure agent doesn't mark the task as done"* 03:50~03:54). 05:49 *"이 파일은 생성되지 않습니다"* — en-orig는 *"isn't read"*(05:50)다. 10:29 Anthropic을 *"인류원리주의"* 로, 10:15 *"about 59%"* 를 *"59번째쯤"* 으로 옮긴다. agent를 *"요원"* 으로 옮기는 곳이 있다.
>
> ⚠️ **수치는 발표자 전달이다.** 리뷰할 변경 하루 약 2,500 → 30,000+(4개월, 00:44~00:49), 리뷰를 서두르면 *"twice as much time"*(01:14~01:16), 50회 넘게 왕복한 변경(10:06~10:08), 재보고의 약 59%가 첫 라운드부터 있던 문제(10:12~10:18), 세 규칙 뒤 *"more of their changes passed review on the very first try"*(11:10~11:12, 수치 없음), 별도 리뷰어 이후 *"far more of their changes get a review that catches something real"*(05:16~05:17, 수치 없음). **위키는 어느 수치도 확인하지 않았다.** 10-30 [[tech-bridge-anthropic-30k-merges-verification]]의 숫자(Addy Osmani *"2,500 changes all the way back in May"*, 진행 쪽 *"30,000 code changes every single day"*)와 같은 계열이지만 **단위가 다르다** — 저기는 *merging*, 여기는 *changes to review*.
>
> ⚠️ **AI Labs 구현은 시연이지 측정이 아니다.** write-eval · review-loop · first-time user · fix-a-bug 스킬은 *"You can ask Claude to create a skill …"* 프롬프트로 만든 것이고, 효과 측정 · 실패 사례 · 토큰 비용은 나오지 않는다. 5라운드 상한의 근거는 *"each of our rounds does more work"*(11:14~11:16)뿐이다. Team · Enterprise 한정 리뷰 에이전트, code review 명령의 effort level, *"By default, this file isn't read unless you ask Claude to do so"*(05:47~05:52)는 **제품 동작에 대한 발표자 진술**이고 위키는 확인하지 않았다.

## 설명란

AI가 코드를 완성했다고 말했을 때 무엇을 확인해야 할까요? AI Labs가 앤트로픽 Claude Code 팀의 코드 검토 방식을 바탕으로 구성한 평가·리뷰 워크플로를 살펴봅니다.

기능별 eval과 목업, 별도 리뷰어, REVIEW.md, 위험도에 따른 검토와 반복 종료 조건, 첫 사용자 테스트 및 Git 복구 방법을 다룹니다. AI Labs가 제안한 구현과 앤트로픽 팀의 실제 프로세스는 구분해 설명합니다.

챕터
00:00 소개
00:23 왜 검토가 병목이 될까
02:09 구현 전에 검증 기준 만들기
04:55 별도 리뷰어의 역할
05:41 REVIEW.md로 검토 규칙 지정
06:35 구현·검증·리뷰 반복하기
08:08 반복되는 실수에서 배우기
08:55 위험도에 맞춰 검토하기
09:53 끝나지 않는 루프 막기
11:33 처음 쓰는 사용자처럼 시험하기
13:03 문제 재현과 변경 되돌리기

관련 자료
Claude Code 팀의 코드 리뷰 방식: https://claude.dev/blog/solving-code-review-at-anthropic/
Claude Code 문서: https://code.claude.com/docs/

#ClaudeCode #AI코딩 #코드리뷰 #AI에이전트

> info.json `tags`: AI 에이전트 · AI 코딩 · Anthropic · Claude Code · 개발 · 코드 리뷰

## 트랜스크립트 — en-orig (원음 영어 ASR — 인용 근거)

[00:22] As the models get better, reviewing what
[00:25] your agent builds matters even more than
[00:27] it ever did before. They've gotten so
[00:29] good that you can just give them a whole
[00:30] list of features and let them work on
[00:32] their own for hours. When you come back,
[00:34] every feature is built without you
[00:36] watching any of it. The Claude code team
[00:38] sees that as a problem because more
[00:40] features being built faster also means
[00:42] there's way more to review. Across
[00:44] Anthropic, the number of changes to
[00:46] review every day went from about 2,500
[00:49] to over 30,000 in just 4 months. But
[00:52] even though the agents are good enough,
[00:54] you still need to check that things are
[00:56] working right. And with the amount of
[00:57] code they're writing each day, the
[00:59] chance of a mistake slipping through
[01:01] gets higher, too. So, with this much to
[01:03] review in so little time, you need a way
[01:05] to make reviewing easier. Review is
[01:07] really important because if a mistake
[01:09] gets to your app's real users without a
[01:11] check, it becomes a much bigger problem.
[01:13] The team says that instead of saving
[01:14] time, you end up spending twice as much
[01:16] time as you would on the review itself,
[01:18] first checking the changes and then
[01:20] fixing the bugs that slip through. If
[01:22] you rush the checks, you just push that
[01:23] time to later when the fix costs more.
[01:26] So, review is a step you can't skip, and
[01:28] the real question is who does it? To
[01:30] [snorts] answer that, the team first
[01:31] changed the question they ask when they
[01:33] review. Instead of asking whether
[01:35] someone read the code, they started
[01:37] asking what could go wrong with the
[01:38] change and how to catch it. That puts
[01:40] the focus on how the thing you're
[01:42] building should work. The Claude code
[01:44] team also changed when the checks run.
[01:46] Now, they happen while Claude is
[01:47] building instead of waiting until the
[01:49] end. You can already see this when you
[01:51] build with Claude code because it goes
[01:52] through some steps to check that your
[01:54] app is working before it tells you the
[01:56] task is done. So, So, the time you look
[01:58] at a change, it's already been checked
[02:00] and fixed at least once. With that in
[02:02] place, you can spend your time on the
[02:04] parts that are most likely to break, and
[02:05] the rest of the team's process is about
[02:07] how to do exactly that. Now, the checks
[02:09] Claude runs while it's building are much
[02:11] smaller. You need deeper checks to see
[02:13] that the app doesn't only work the way
[02:15] you'd expect, but it also holds up when
[02:17] people use it in different ways. That's
[02:19] why deeper checks are the first step in
[02:20] the Claude code team's own process.
[02:23] Before a change goes anywhere, they ask
[02:25] Claude to run something that proves it
[02:26] works and to show them the result
[02:28] instead of just saying it's done. That
[02:30] can be the app's tests or a screenshot
[02:32] compared with the design. Boris Cherny,
[02:34] who is the creator of Claude code, says
[02:36] that the best way to get Claude to work
[02:38] well is to give it away to prove it did
[02:41] the work right. And the team's advice is
[02:43] to give your agent a list of checks it
[02:45] can run. Each of those checks is called
[02:47] an eval, and it is a fixed test that
[02:49] tells you whether the work is done. It
[02:51] has to be strict enough that bad work
[02:53] fails it. We've shown many ways to give
[02:55] Claude evals in our earlier videos.
[02:57] Claude code's team mentions their own
[02:59] way to set up these checks, and we
[03:00] turned that into a skill. In the demo
[03:02] app we were testing on, we had a specs
[03:04] folder with all the features in it. Each
[03:06] feature had its own folder named after
[03:08] the feature itself, and inside each
[03:10] folder we had an rd.md file that listed
[03:13] the requirements for that feature. You
[03:15] can ask Claude to create a skill that
[03:17] turns each feature into an eval.md file.
[03:21] This is the file that has the actual
[03:22] method the agent will use to check its
[03:25] work. If the feature has a design, it
[03:27] should first make it as a simple web
[03:29] page called a mock-up instead of
[03:30] building straight on the app. Then it
[03:32] saves that page as the design the app
[03:34] gets checked against. Claude can keep
[03:36] working on the real app until it matches
[03:38] that page, and we can quickly see how
[03:40] the feature will look without wasting
[03:42] too many tokens. You should also tell it
[03:44] that once it has written the evals, it
[03:46] needs to get them reviewed by you, and
[03:48] without that review, it shouldn't build
[03:50] anything. Then ask it to create a hook
[03:52] that makes sure agent doesn't mark the
[03:54] task as done until the evals have
[03:56] passed. Claude then creates the skill
[03:58] for you. It writes the skill in your
[03:59] .claude folder and creates a template
[04:02] next to it that gives all the eval files
[04:04] the same structure. So, for each new
[04:06] feature, it starts by running the skill.
[04:08] It opens the folder for that feature and
[04:10] writes the requirements document along
[04:12] with the eval file. Then it uses the
[04:14] hook to check whether the requirements
[04:16] are set up properly. It goes back and
[04:18] forth several times checking whether the
[04:20] evals are written properly and it
[04:22] creates a mock-up that you can look at.
[04:24] After it has finished everything and
[04:25] checked the evals, it changes the
[04:27] feature status from draft to in review.
[04:29] Then it tells you every decision it made
[04:31] on its own and opens the files for you
[04:33] to check. You can check how the design
[04:35] looks on there. It also shows every
[04:37] other screen the app can be in along
[04:39] with the same design on mobile, so you
[04:40] can check the smaller screen layout as
[04:42] well. You need to review both the
[04:44] eval.md and the mock-ups. If you have
[04:47] any changes at this point, you can make
[04:49] them by asking Claude. If you don't, you
[04:51] can just approve them and it will mark
[04:53] the feature as reviewed and ready for
[04:54] building. Even after Claude builds the
[04:56] feature based on the evals, you still
[04:58] need to review it. And the agent that
[05:00] reviews it shouldn't be the same one
[05:02] that built it because that agent made
[05:04] every decision in the change and ends up
[05:06] agreeing with itself. So, the Claude
[05:08] code team's second check is a separate
[05:10] reviewer agent. The reviewer checks
[05:12] every change before a person looks at
[05:14] it. Since the team started doing this,
[05:16] far more of their changes get a review
[05:17] that catches something real. That review
[05:20] agent is only available on the team and
[05:22] enterprise plans for now, but a lighter
[05:24] version already comes with Claude code
[05:26] as the code review command. When you run
[05:28] it, a separate agent reads everything
[05:30] that changed and reports back the
[05:32] mistakes that would break your app. You
[05:33] can also choose how deep it checks with
[05:35] an effort level. At low effort, it only
[05:37] reports what it's most sure about and
[05:39] the higher levels check more of your
[05:41] app. To tell that command what matters
[05:43] in your app, Anthropic's article on this
[05:45] says to write your rules in a file
[05:47] called review.md. By default, this file
[05:50] isn't read unless you ask Claude to do
[05:52] so. So, if you want the code review
[05:53] command on your computer to follow your
[05:55] rules, they need to be part of your
[05:57] Claude.md. But instead of adding them
[05:59] directly to that file, it's better to
[06:01] put them in another file. Then you need
[06:03] to link that file inside Claude.md. This
[06:06] way, whenever you open a new session,
[06:08] the review.md is also loaded along with
[06:10] the Claude.md file. This file should
[06:13] have what counts as a real failure in
[06:15] the app and how serious each problem is.
[06:17] It should also say what to ignore and
[06:19] how to report the review along with all
[06:20] the ways you want the app tested. You
[06:22] can ask Claude to create this file for
[06:24] you and you'll end up with a review.md
[06:26] file in your project's main folder.
[06:28] Every review you run on your app starts
[06:30] from it and since it's linked from your
[06:32] Claude .md, the code review command
[06:34] reads it, too. With the review rules
[06:36] written down, the next step is a loop
[06:38] that builds the feature and reviews it.
[06:40] You can ask Claude to create a review
[06:42] loop skill that builds a feature and
[06:44] then checks it with its eval.md. It uses
[06:47] sub-agents with fresh context windows.
[06:49] This way, they don't have the same
[06:50] context as the main agent, so they don't
[06:52] just agree with what the main agent did.
[06:54] It should keep looping until all the
[06:56] evals have passed. From that prompt,
[06:58] Claude makes the skill along with three
[07:00] agents and the main agent runs them. The
[07:02] main agent acts as the orchestrator,
[07:04] which runs the loop and starts each
[07:06] agent in its own context window. The
[07:08] first agent is the builder, which builds
[07:10] the feature from the requirements
[07:12] document that the right eval skill
[07:14] wrote. After the builder is done, the
[07:16] verifier starts and checks the app
[07:18] against the eval's from that same skill.
[07:20] It checks whether everything the evals
[07:22] cover has been built and marks each eval
[07:24] as passed or failed. Then the reviewer
[07:26] goes through the app to find anything
[07:28] the evals missed and it uses the rules
[07:30] in your review.md. To use the skill, you
[07:33] run the review loop command and then
[07:35] name the feature you want to build. It
[07:37] starts by writing a state.md file that
[07:40] keeps track of the loop. This file shows
[07:42] which round the loop is on and what's
[07:44] still failing. After that, the first
[07:45] round starts and the builder builds the
[07:47] feature. While the builder works, the
[07:49] hook from the right eval skill stops the
[07:51] main agent from calling the feature done
[07:53] too early. Then the verifier and the
[07:55] reviewer start and the loop keeps fixing
[07:58] issues in rounds. When it hits a
[07:59] decision it can't make on its own, it
[08:01] shows you a progress report and asks
[08:03] you. The loop only stops when all all
[08:05] evals pass and the review doesn't find
[08:07] anything new, but fixing each issue
[08:09] doesn't stop it from coming back because
[08:11] Claude doesn't remember mistakes from
[08:13] earlier sessions. So, it makes the same
[08:14] mistake on the next feature and you have
[08:16] to fix it all over again. That's why
[08:18] when the Claude code teams reviewer
[08:20] keeps finding the same mistake, they
[08:22] change the instructions Claude reads and
[08:24] Claude stops making it. We do the same
[08:26] with the review.md file from earlier. At
[08:28] the bottom of it, there's a section for
[08:30] rules learned over time. When a review
[08:32] misses a bug that shows up later, a new
[08:35] rule goes into that section. It also
[08:37] adds a rule when the review keeps
[08:38] flagging something that turns out not to
[08:40] be a real problem. That way the next
[08:42] review doesn't make the same mistake
[08:44] again. The review loop keeps track of
[08:46] this for you. When the same problem
[08:47] comes up in a later round, the loop
[08:49] matches it to the earlier one. At the
[08:51] end, it suggests a one-line rule for
[08:53] that part and only adds it if you
[08:55] approve. But, a careful review on every
[08:57] change costs time and usage. So, the
[09:00] Claude code teams rule is that a change
[09:02] needs to get checked harder when a
[09:04] mistake in that feature could do more
[09:05] damage. And they don't choose on their
[09:07] own if a feature needs a full review or
[09:09] a quick one. They have an agent that
[09:11] sorts every change for them, which they
[09:13] call a classifier. You can sort your own
[09:15] changes as well and all it takes is one
[09:17] question, which is what happens to a
[09:18] customer if a feature breaks. A mistake
[09:20] that only makes something look wrong is
[09:22] low risk. If it stops a feature from
[09:24] working, but nobody loses anything,
[09:26] that's medium because you can still fix
[09:28] it later. But, some mistakes can make a
[09:30] customer lose money or get locked out
[09:32] and some can show them another person's
[09:34] data. You can't take those back once
[09:36] they happen. So, those changes are high
[09:38] risk. You can also turn that question
[09:39] into a scale that rates each feature on
[09:42] this scale for you. Before you build a
[09:43] feature, you need to run the scale to
[09:45] check whether it's low, medium, or high.
[09:47] Then, when you use the right eval scale,
[09:49] you pass it that rating, too. So, a
[09:51] high-risk feature gets stricter evals
[09:53] than a low-risk one. But, even [snorts]
[09:55] on the changes that do need the full
[09:57] review, there's one more problem. The
[09:59] builder and the reviewer agents don't
[10:00] know when to stop, so they can keep
[10:02] going back and forth trying to find and
[10:04] fix issues. The Claude code team once
[10:06] had a change that went back and forth
[10:08] more than 50 times like this. The agents
[10:10] kept going until someone manually
[10:12] stopped the loop. When the team looked
[10:14] at what the reviewer kept reporting,
[10:15] about 59% of it had been there since the
[10:18] very first round. So, the reviewer was
[10:20] mostly finding the old problems again
[10:22] and again. And on your plan, every one
[10:24] of those rounds uses up your limits.
[10:26] People's main complaint about
[10:28] Anthropic's article was that it only
[10:30] works if you have unlimited tokens. So,
[10:32] the team added three rules, and the
[10:33] first one is that after three rounds,
[10:35] the reviewer stops listing more problems
[10:38] and tells the builder to rethink how
[10:39] it's building the feature. If the
[10:41] feature is still failing after three
[10:42] rounds of fixes, more work in the same
[10:44] way wouldn't get it there. The second is
[10:46] that after the first round, the reviewer
[10:48] only checks what the last fixes changed
[10:51] and doesn't report anything it has
[10:53] already reported. That stops it from
[10:54] checking the whole feature again and
[10:56] finding the old problems one at a time.
[10:58] And the third is that when the reviewer
[11:00] finds a problem, it says what kind of
[11:02] problem it is. That way, the builder
[11:04] fixes that kind of problem everywhere it
[11:06] shows up and not only in the one spot
[11:08] the reviewer found. With those three
[11:10] rules in place, more of their changes
[11:12] passed review on the very first try. Our
[11:14] review loop works the same way, but each
[11:16] of our rounds does more work. It builds
[11:18] the feature and checks every eval in the
[11:20] browser, and then it reviews the code.
[11:22] That's why we set it to stop after five
[11:24] rounds instead of three. The loop can
[11:26] also stop before it gets to five when
[11:28] the same problem is still there after
[11:30] two rounds of fixes. But even [snorts]
[11:32] when the loop finishes and every eval
[11:34] passes, some mistakes will still get
[11:36] through. So, you need two more things,
[11:38] which are a way to find those mistakes
[11:40] and a way to undo them fast. The Claude
[11:42] code team can undo almost anything they
[11:44] release in minutes, and that's what lets
[11:46] them read less. To find the mistakes,
[11:48] they use the product themselves every
[11:50] day, so they often spot a problem before
[11:52] their customers do. You can do the same
[11:54] by using every new feature yourself the
[11:57] way a customer would. But you already
[11:59] know how the feature works, so you'll
[12:00] miss some things. To catch those, you
[12:02] can send a fresh agent that never saw
[12:04] the app being built to use the live app
[12:06] like a first-time customer. To set up
[12:08] that fresh agent, you can ask Claude to
[12:10] create a skill that shows you the app
[12:12] from a new user's point of view. It
[12:14] should use sub agents that are blocked
[12:16] from reading the app's code, so they
[12:17] don't know what the app is about. They
[12:19] should go through the app the way a
[12:21] first-time user would and find every
[12:23] place where someone might get stuck.
[12:24] From this prompt, Claude creates a
[12:26] first-time user skill and the agent that
[12:28] the skill sends to use the app. It also
[12:30] gives the test a temporary database, so
[12:33] it doesn't touch your real data and it
[12:35] creates a hook that stops the agent from
[12:37] reading the app's code. The agent would
[12:39] normally get around that block with
[12:40] terminal commands. So, the hook stops it
[12:42] from reading the code that way, too. To
[12:44] run the test, you just use the skill's
[12:46] command and tell it which feature you
[12:48] want it to check. Based on your prompt,
[12:50] it opens the app and starts an agent
[12:52] that knows nothing about how the app was
[12:54] built and then it waits for that agent
[12:56] to finish. When the agent is done, the
[12:58] skill reports everything the agent found
[13:00] and suggests fixes you can apply to make
[13:02] your app better. Finding the mistakes is
[13:04] one half and the other half is undoing
[13:06] the changes that caused them. For that,
[13:08] you can use Git, which basically saves
[13:10] every version of your app. With Git,
[13:12] each feature gets its own copy of the
[13:14] project, which is called a branch. If
[13:16] any feature in your app causes issues
[13:17] later on, you can just undo it from Git.
[13:20] To find and undo the change that broke
[13:22] something, you can ask Claude to create
[13:24] a skill called fix a bug. Basically,
[13:26] when a feature isn't working the way you
[13:28] need it to, you give this skill the
[13:30] problem and it finds the cause and how
[13:32] to fix it. It tries to make the bug
[13:33] happen again by going through the same
[13:35] steps and then checks whether it's guess
[13:37] about the cause was right. After that,
[13:39] it reports the problem and fixes it. For
[13:41] this skill to work, you also need to
[13:43] tell Claude in your Claude.md to use Git
[13:46] and make its own branch for each
[13:48] feature. It should also save every
[13:50] version that works. That way, when a
[13:51] feature isn't working as expected,
[13:53] Claude can go back through the saved
[13:55] versions to find the change that caused
[13:57] it and roll back to an earlier version.

## 트랜스크립트 — ko (`tlang=ko` 기계 번역 — 참고용, 인용하지 않음)

[00:22] 모델이 개선됨에 따라,
[00:24] 담당 에이전트가 작성한 내용을 검토하는 것은 더욱 중요합니다.
[00:27] 그 어느 때보다 중요합니다. 그들은 그렇게 되었습니다
[00:29] 그들에게 줄 수 있는 좋은 것들의 목록을 만들어 보세요.
[00:30] 기능을 완성하고 작동하도록 하세요.
[00:32] 몇 시간 동안 혼자 있었다. 돌아오시면,
[00:34] 각 기능은 없이 완료됩니다.
[00:35] 당신은 그 과정을 전혀 보지 못했어요. 팀
[00:37] 클로드 코드는 이를 문제로 여긴다.
[00:39] 더 많은 함수가 생성되기 때문에
[00:41] "빠르다"는 것은 그 이상의 의미를 담고 있습니다.
[00:43] 검토. 앤트로픽에서, 금액은
[00:46] 매일 검토하는 변경 사항은 다음과 같습니다.
[00:49] 약 2,500명에서 30,000명 이상으로 단 4개월 만에 증가
[00:51] 개월. 하지만 설령 그 요원들이
[00:53] 충분히 좋지만, 여전히 필요한 것이 있습니다.
[00:55] 모든 것이 제대로 작동하는지 확인하십시오.
[00:56] 바르게. 그리고 그 양으로
[00:58] 그들이 매일 작성하는 코드,
[00:59] 오류 누출 가능성
[01:01] 또한 증가합니다. 그래서, 그 많은 것들과 함께,
[01:03] 이렇게 짧은 시간 안에 검토하려면 다음이 필요합니다.
[01:05] 검토를 용이하게 하는 방법. 그만큼
[01:07] 검토는 필수적입니다. 왜냐하면 만약
[01:08] 해당 오류는 실제 사용자에게 영향을 미칩니다.
[01:10] 검증되지 않은 신청서,
[01:11] 그것은 훨씬 더 큰 문제가 됩니다. 그
[01:13] 팀 측은 저축하는 대신
[01:15] 그렇게 하면 결국 두 배의 비용을 쓰게 됩니다.
[01:16] 그러면 검토 자체가 진행될 것입니다. 첫째,
[01:18] 변경 사항을 검토한 후 수정합니다.
[01:20] 유출된 오류들. 응
[01:22] 검토 속도를 높이는 방법은 검토를 연기하는 것뿐입니다.
[01:23] 그 시간은 나중에, 그때
[01:25] 수정 비용이 더 많이 듭니다. 그러므로
[01:26] 검토는 할 수 없는 단계입니다.
[01:28] 그 부분은 넘어가고, 진짜 질문은 다음과 같습니다.
[01:29] 누가 만드는 건가요? 그 질문에 답하자면,
[01:31] 팀은 먼저 질문을 바꿨습니다.
[01:33] 그들은 확인할 때 그렇게 합니다. 묻는 대신에
[01:35] 누군가 그 코드를 읽으면, 그들은 다음과 같은 반응을 보이기 시작했습니다.
[01:37] 무엇이 잘못될 수 있는지 물어보세요
[01:38] 변화와 그 변화를 감지하는 방법. 그렇게 되면
[01:40] 무엇이 어떻게 작동해야 하는지에 집중하세요
[01:42] 당신은 건설하고 있습니다. 클로드의 팀
[01:44] 해당 코드는 또한 그 시점을 변경했습니다.
[01:45] 그들은 검토를 수행합니다. 이제 그런 일이 일어납니다
[01:46] 클로드가 건축하는 동안,
[01:48] 끝까지 기다리지 않고. 이미
[01:50] 빌드할 때 이를 확인할 수 있습니다.
[01:51] 클로드 코드, 왜냐하면 그는 몇 가지를 수행하기 때문입니다.
[01:53] 신청서가 올바른지 확인하는 단계
[01:54] 제가 그 일에 대해 말씀드리기 전에 먼저 일을 하세요.
[01:56] 용어. 그래서 살펴보면
[01:58] 해당 변경 사항은 이미 검증되었습니다.
[02:00] 적어도 한 번은 수정되었습니다. 그렇게 해서
[02:02] 일단 구현되면, 당신은 시간을 온전히 거기에 집중할 수 있습니다.
[02:03] 가장 가능성이 높은 부분
[02:05] 실패하면 나머지 과정은 실패합니다.
[02:07] 팀의 목표는 어떻게 해야 하는지에 관한 것입니다.
[02:08] 바로 그거예요. 자, 이제 리뷰를 살펴보겠습니다.
[02:09] 클로드가 건설하는 동안 실행하는 것
[02:11] 크기가 훨씬 작습니다. 당신은 필요합니다
[02:12] 더 자세한 검토를 통해 다음을 확인할 수 있습니다.
[02:14] 이 애플리케이션은 예상대로 작동하지 않습니다.
[02:15] 하지만 다음과 같은 상황에서도 견뎌낼 수 있어야 합니다.
[02:17] 사람들은 그것을 다양한 방식으로 사용합니다. 에 의해
[02:18] 그래서 가장 심층적인 리뷰가 나오는 겁니다.
[02:20] 그 과정 자체의 첫 번째 단계
[02:22] 클로드 코드 팀. 전에
[02:23] 변경 사항을 적용하려면 다음과 같이 요청합니다.
[02:25] 클로드, 그의 능력을 증명할 만한 무언가를 실행해 봐.
[02:26] 어떻게 작동하는지 보여주고 그들에게 보여주세요.
[02:28] 그냥 그렇게 말하는 대신 결과를 내놓는 것
[02:29] 준비됐습니다. 이는 다음을 통해 가능합니다.
[02:31] 애플리케이션 테스트 또는 캡처
[02:32] 화면과 디자인을 비교한 결과입니다.
[02:34] 클로드 코드의 창시자 보리스 체르니
[02:36] 클로드에게 가장 좋은 방법은 다음과 같다고 말합니다.
[02:37] 잘한다는 것은 그에게 그것을 증명할 수 있는 수단을 제공하는 것을 의미합니다.
[02:39] 일을 제대로 한 사람.
[02:41] 팀의 조언은 다음과 같습니다.
[02:43] 담당 에이전트에게 체크리스트를 주세요.
[02:44] 실행할 수 있다는 것입니다. 각각의 것들
[02:46] 검증 과정을 "eval"이라고 하며, 이는 다음과 같습니다.
[02:48] 작업이 완료되었는지 여부를 나타내는 고정 테스트
[02:50] 끝났습니다. 그래야만 한다
[02:51] 충분히 엄격하다
[02:52] 힘든 직장 때문에 그녀가 좌절하지 않도록 하세요. 우리는 가지고 있습니다
[02:54] 평가하는 다양한 방법을 보여주었습니다.
[02:55] 이전 영상에서 클로드에게 했던 말입니다.
[02:57] 클로드 코드 팀은 다음과 같이 언급합니다.
[02:58] 이러한 테스트를 구성하는 자신만의 방식
[03:00] 그리고 우리는 그것을 기술로 발전시켰습니다. ~ 안에
[03:02] 데모 애플리케이션
[03:03] 저희가 테스트해봤습니다. 우리는 폴더 하나를 가지고 있었어요.
[03:04] 전체 사양
[03:06] 내부에. 각 기능에는 고유한 특징이 있었습니다.
[03:08] 폴더 이름은 당신의 이름으로 되어 있고, 그 안에는 각각 무엇이 들어있나요?
[03:10] 저희에게는 rd.md 파일이 있었습니다.
[03:13] 그 목록에는 해당 직책에 필요한 요건들이 나열되어 있었습니다.
[03:15] . 클로드에게 하나 만들어달라고 요청할 수 있습니다.
[03:17] 모든 기능을 바꿔주는 기술
[03:19] eval.md 파일. 이것이 파일입니다
[03:21] 실제 메서드가 포함된
[03:23] 담당자는 이를 사용하여 그들의 업무를 확인할 것입니다.
[03:25] 함수에 설계가 있다면, 먼저
[03:27] 웹페이지 형식으로 만들어야 합니다.
[03:28] 간단하게 "모형"이라고 부르는 대신
[03:30] 직접 제작하세요
[03:31] 애플리케이션. 그런 다음 해당 페이지를 저장하세요.
[03:33] 예를 들어 비교 대상이 될 디자인 같은 것 말입니다.
[03:35] 해당 애플리케이션. 클로드는 계속할 수 있습니다
[03:36] 실제 애플리케이션 작업을 진행하는 동안
[03:38] 해당 페이지와 일치하는 것,
[03:39] 이를 통해 우리는 어떻게 되는지 빠르게 확인할 수 있습니다.
[03:41] 그 기능은 낭비 없이 빛을 발할 것입니다
[03:42] 많은 토큰. 당신도 그렇게 해야 합니다
[03:44] 그에게 일단 "
[03:46] "평가"는 여러분이 검토해야 합니다.
[03:48] 그 검토 없이는 아무것도 만들어서는 안 됩니다.
[03:50] . 그런 다음, 그에게 독자의 관심을 끌 만한 "후크"를 만들어 달라고 요청하세요.
[03:52] 에이전트가 표시하지 않도록 하십시오.
[03:54] 작업이 완료된 것으로 간주합니다.
[03:55] 평가가 통과되었습니다. 클로드
[03:57] 그런 다음 직접 스킬을 만들어 보세요.
[03:58] 폴더에 스킬을 적어주세요
[04:00] .claude를 입력하고 옆에 템플릿을 만드세요.
[04:02] «의 모든 파일을 제공하는 그녀
[04:03] "eval"은 동일한 구조를 평가합니다. 따라서,
[04:05] 각각의 새로운 함수는 실행으로 시작됩니다.
[04:07] 그 기술. 해당 폴더를 열어보세요
[04:09] 기능을 수행하고 문서를 작성합니다.
[04:11] « 파일과 함께 제공되는 요구 사항
[04:13] "평가". 그다음, "갈고리"를 사용하여
[04:15] 요구 사항이 충족되는지 확인하십시오
[04:16] 올바르게 설정되었습니다. 그것은 왔다가 사라진다.
[04:18] "평가"가 제대로 되었는지 여러 번 확인했습니다.
[04:20] 글이 잘 쓰여졌고 모형을 만들어냅니다.
[04:22] 확인할 수 있습니다. 끝낸 후에
[04:25] "평가"를 확인한 후에도 변경됩니다.
[04:26] "초안" 기능의 상태를 "
[04:28] "검토 중입니다." 그러면 각각에 대해 알려줍니다.
[04:30] 그는 스스로 내린 결정이며 이를 공개합니다.
[04:32] 검토하실 파일들을 준비했습니다.
[04:34] 디자인이 어떻게 생겼는지 확인해 볼 수 있습니다.
[04:35] 거기. 또한 다른 모든 사람들도 보여줍니다.
[04:37] 애플리케이션 화면과 함께
[04:39] 모바일에서도 동일한 디자인입니다.
[04:41] 작은 화면에서 형식을 확인하세요
[04:43] . 두 파일 모두 검토해야 합니다.
[04:45] eval.md는 모델과 같습니다. 만약 당신이 가지고 있다면
[04:47] 이 시점에서 변경 사항이 있으면 다음과 같이 하세요.
[04:48] 클로드에게 물어보세요. 하지만
[04:50] 간단히 승인하시면 됩니다.
[04:52] 그러면 해당 기능이 검토 완료 및 준비된 것으로 표시됩니다.
[04:54] 그 발전을 위해서. 그 후에도
[04:56] 클로드가 함수를 생성하는 것은 다음을 기반으로 합니다.
[04:58] 평가는 여전히 검토해야 합니다. 그리고
[05:00] 그걸 확인하는 담당자는 그 사람이 아니어야 합니다.
[05:02] 그것을 만든 바로 그 사람, 왜냐하면 그 에이전트가
[05:04] 그는 모든 결정을 내렸고 결국...
[05:06] 자기 자신과의 합의. 그러므로
[05:08] 장비의 2차 검증
[05:09] 클로드 코드(Claude Code)는 검토 담당자입니다.
[05:10] 독립적인. 검사관은 각각을 확인합니다.
[05:12] 다른 사람이 보기 전에 수정해요.
[05:14] 팀이 이 일을 시작한 이후로
[05:16] 그들의 변화 중 훨씬 더 많은 부분이 영향을 받습니다.
[05:17] 실제 문제를 감지하는 검토.
[05:19] 그 검토 담당자는 단지
[05:21] 팀 플랜에서 이용 가능합니다.
[05:22] 현재로서는 엔터프라이즈 버전이지만, 향후 버전이 출시될 예정입니다.
[05:24] 더 가벼운 버전에는 이미 클로드 코드가 포함되어 있습니다.
[05:26] 코드 검토 명령. 그것이
[05:28] 실행하면 독립적인 에이전트가 읽습니다.
[05:30] 변경된 모든 사항과 그에 대한 보고서
[05:31] 앱을 작동 불능 상태로 만들 수 있는 오류
[05:33] . 깊이도 선택할 수 있습니다.
[05:35] 어느 정도 노력을 들여 검증해야 합니다.
[05:36] . 낮은 수준에서는 다음 내용만 보고합니다.
[05:38] 더 안전하고, 수치도 더 높습니다.
[05:39] 그들은 지원서의 더 많은 부분을 검토합니다.
[05:41] 그 명령에게 그것이 무엇인지 알려주기 위해
[05:43] 지원서 작성에 중요한 기사입니다.
[05:45] Anthropic은 자신만의 규칙을 만들라고 제안합니다.
[05:47] review.md라는 파일에 있습니다. 의
[05:49] 기본적으로 이 파일은 생성되지 않습니다.
[05:50] 클로드에게 부탁하지 않는 한 네가 읽어라.
[05:52] 그러니까 만약 명령어를 원한다면
[05:54] 컴퓨터에서 코드 검토
[05:56] 자신이 세운 규칙을 따르세요. 그 규칙들은 당신 삶의 일부가 되어야 합니다.
[05:58] 클로드.md. 하지만 그것들을 더하는 대신에
[06:00] 해당 파일로 바로 이동하는 것이 더 좋습니다.
[06:01] 그것들을 다른 파일에 넣어두세요. 그렇다면 당신은 반드시
[06:03] Claude.md 파일 안에 있는 해당 파일을 링크하세요.
[06:06] . 이렇게 하면, 매번 열 때마다
[06:08] 새 세션, review.md 파일
[06:09] 해당 파일과 함께 업로드됩니다.
[06:11] 클로드.md. 이 파일에는 다음 내용이 포함되어야 합니다.
[06:13] 이는 실제적인 실패로 간주됩니다.
[06:15] 지원서의 내용과 각 지원서의 중요도
[06:16] 문제. 무엇을 무시해야 하는지도 명시해야 합니다.
[06:18] 그리고 리뷰를 신고하는 방법과 함께
[06:20] 당신이 원하는 모든 방식으로
[06:21] 앱을 사용해 보세요. 질문하실 수 있습니다
[06:23] 클로드, 이 파일을 만들어줘.
[06:25] 결과적으로 review.md 파일이 생성됩니다.
[06:26] 프로젝트의 메인 폴더입니다.
[06:28] 귀하가 실행하는 각 검사
[06:30] 신청은 거기서부터 시작되며,
[06:31] Claude.md에서 링크되어 있습니다.
[06:33] 코드 검토 명령도
[06:35] 읽다. 검토 규칙에 따라
[06:36] 초안이 작성되면 다음 단계는 다음과 같습니다.
[06:38] 함수를 생성하고 확인하는 루프입니다.
[06:40] 클로드에게 하나 만들어달라고 요청할 수 있습니다.
[06:42] 검토 루프 기능
[06:43] 함수를 구성한 다음
[06:45] eval.md 파일을 통해 확인해 주십시오. 사용
[06:47] 컨텍스트 창이 있는 하위 에이전트
[06:48] 새로운. 이런 식으로 그들은 그것을 가지지 않습니다.
[06:50] 주요 에이전트와 동일한 맥락에서,
[06:52] 그래서 그들은 단순히 있는 그대로를 받아들이지 않습니다.
[06:53] 수사 책임자가 그랬습니다. 계속 진행하셔야 합니다
[06:55] 모든 것이 될 때까지 반복합니다.
[06:56] 평가가 승인되었습니다. 에게
[06:57] 그 명령에 따라 클로드는 다음을 생성합니다.
[06:59] 세 명의 요원과 함께 기술을 발휘하며
[07:00] 주 에이전트가 이를 실행합니다. 에이전트
[07:02] 교장은 지휘자 역할을 합니다.
[07:04] 루프를 실행하고 각 에이전트를 초기화합니다.
[07:06] 자체 컨텍스트 창. 첫 번째
[07:08] 에이전트는 생성자이며, 생성자는 다음을 만듭니다.
[07:10] 문서에 기반한 함수
[07:12] 능력이 요구하는 사항
[07:13] 정확한 평가. 그 후에
[07:15] 생성자가 끝나면 검증자가 나타납니다.
[07:17] 애플리케이션을 시작하고 확인하세요
[07:19] 동일한 능력에 대한 평가
[07:20] . 모든 내용이 포함되는지 확인하세요
[07:22] 평가 시스템이 구축되고 브랜딩되었습니다.
[07:24] 각 평가는 통과 또는 불합격으로 판정됩니다.
[07:26] . 다음으로, 검토자는 다음을 분석합니다.
[07:27] 무엇이든 찾을 수 있는 앱
[07:29] 평가에서 간과된 점과
[07:31] review.md의 규칙을 따르세요. 을 위한
[07:32] 해당 스킬을 사용하려면 명령어를 실행하십시오.
[07:34] 검토 루프를 실행한 다음 이름을 지정합니다.
[07:36] 만들고자 하는 기능입니다. 시작
[07:37] state.md 파일을 작성하는 중
[07:39] 루프를 추적합니다. 이것
[07:41] 이 파일은 몇 라운드인지 보여줍니다.
[07:43] 루프와 계속 실패하는 이유. 후에
[07:45] 자, 이제 1라운드가 시작됩니다.
[07:46] 생성자는 함수를 생성합니다. 반면
[07:48] 건축업자가 일하고, 갈고리가
[07:50] 정확한 평가 능력은 다음과 같은 것을 피합니다.
[07:51] 주 담당자가 표시하는
[07:52] 기능이 너무 일찍 완료되었습니다.
[07:54] . 그다음, 검증자와 검토자
[07:56] 그들은 시작하고, 그 과정은 계속해서 문제를 해결해 나갑니다.
[07:58] 라운드별 문제. 그것이 도달하면
[08:00] 그가 스스로 내릴 수 없는 결정
[08:01] 진행 상황 보고서를 보여줍니다.
[08:03] 묻다. 루프는 멈춥니다.
[08:05] 모든 평가가 완료되었을 때
[08:06] 승인되었으며 검토 결과 발견되지 않았습니다.
[08:08] 새로운 건 없지만, 모든 문제를 해결하세요.
[08:10] 클로드가 그러지 않기 때문에 그가 돌아오는 것을 막지는 못합니다.
[08:12] 이전 세션의 오류를 기억합니다.
[08:13] . 그러고 나서 그는 똑같은 실수를 저지른다.
[08:15] 다음 함수이고 당신은 해야 합니다.
[08:16] 모든 것을 다시 수정하세요. 그래서,
[08:18] 장비 검사관이
[08:20] 클로드의 코드는 계속해서 다음을 찾아냅니다.
[08:21] 같은 오류인데, 지침이 바뀌었어요.
[08:23] 클로드가 그 글을 읽고 나서는 그만둔다.
[08:25] . 우리는 파일에 대해서도 같은 작업을 합니다.
[08:27] 이전 review.md 파일입니다. 결국에는 하나가 남는다.
[08:29] 학습한 규칙에 대한 섹션
[08:31] 시간. 리뷰가 진행될 때
[08:33] 멈추세요, 나중에 오류가 발생합니다.
[08:35] 해당 섹션에 새 규칙을 추가하세요.
[08:36] 또한 다음과 같은 규칙을 추가합니다.
[08:38] 이 리뷰는 결국 드러나는 한 가지 사실을 계속해서 강조하고 있습니다.
[08:40] 별문제 없을 거예요. 그런 식으로,
[08:42] 다음 검토에서는 책임을 지지 않습니다.
[08:44] 또 같은 실수를 했네요. 루프
[08:45] 이 리뷰는 다음을 통해 이를 추적합니다.
[08:46] 너. 같은 문제가 발생할 때
[08:48] 다음 단계에서 루프는 이를 비교합니다.
[08:50] 이전 것과 함께. 결론적으로, 그것은 다음을 시사합니다.
[08:52] 해당 부분에 대한 단선 규칙 및
[08:54] 사용자가 승인해야만 추가됩니다.
[08:56] 하지만 각각을 꼼꼼히 검토해 보면
[08:58] 변화에는 시간과 노력이 필요합니다. 그러므로
[09:00] 클로드 코드의 팀 규칙은 다음과 같습니다.
[09:02] 변경 사항에 대해 추가적인 검토가 필요합니다.
[09:03] 해당 함수에 오류가 있을 경우
[09:05] 더 큰 피해를 초래한다. 그리고 그들은 결정하지 않습니다
[09:07] 기능에 계정이 필요한 경우
[09:08] 자세한 리뷰 또는 간단한 리뷰. 가지다
[09:10] 각 변화를 분류하는 에이전트
[09:12] 그들은 분류기라고 부릅니다. 너
[09:14] 직접 분류할 수도 있습니다.
[09:16] 변화가 있고, 단 하나의 질문만 필요합니다.
[09:17] 고객에게 어떤 일이 발생하면 어떻게 될까요?
[09:19] 기능 오류. 실수는 오직...
[09:21] 무언가가 보기 안 좋다는 사실은 위험도가 낮다는 것을 의미합니다.
[09:23] 만약 그것이 기능 작동을 방해한다면,
[09:25] 누구도 손해 보는 게 없어요. 난이도는 중간 정도입니다.
[09:26] 나중에 고칠 수 있으니까요.
[09:29] 하지만 몇 가지 실수는 문제를 야기할 수 있습니다.
[09:30] 고객은 손해를 보지만, 남습니다.
[09:32] 차단했거나 심지어 그에게 데이터를 보여주지도 않았습니다.
[09:34] 다른 사람. 돌이킬 수 없어.
[09:35] 그 일이 발생할 때마다. 그래서 그러한 변화들
[09:37] 그들은 고위험군입니다. 또한 다음과 같은 방법도 있습니다.
[09:39] 그 질문을 척도로 바꿔보세요
[09:41] 각 기능에 대한 평가를 부탁드립니다. 전에
[09:43] 함수를 생성하려면 다음을 실행해야 합니다.
[09:45] 낮음, 중간인지 확인하기 위한 척도입니다.
[09:47] 또는 높음. 그런 다음, 척도를 사용할 때
[09:49] 적절한 평가를 내리면 그 결과도 전달됩니다.
[09:50] 그 평점. 그러므로,
[09:52] 고위험 기능이 수신합니다
[09:53] 다음 중 하나보다 더 엄격한 평가
[09:54] 위험도가 낮습니다. 하지만, 심지어 그 안에서도
[09:56] 검토가 필요한 변경 사항
[09:57] 완료됐습니다. 그런데 문제가 하나 더 있습니다. 그만큼
[09:59] 건설 및 검사 담당자들은 모릅니다
[10:00] 언제 멈춰야 할지 알아야 그들이
[10:02] 계속 왔다갔다 하면서 시도해 봤어요
[10:03] 문제를 찾아 해결하세요. 그
[10:05] 클로드 코드의 팀은 한때 다음과 같은 것을 가지고 있었습니다.
[10:07] 50번 넘게 나타났다 사라진 변화.
[10:09] 이런 식으로. 요원들은 계속해서
[10:11] 누군가가 루프를 멈출 때까지
[10:12] 수동으로.
[10:13] 팀이 관찰한 내용은 다음과 같습니다.
[10:15] 리뷰어는 59번째쯤에서 계속해서 보고했습니다.
[10:17] %는 1차 라운드부터 이미 존재했습니다.
[10:19] 그래서 리뷰어는 주로
[10:21] 기존의 문제점을 찾아내고
[10:22] 다시. 그리고 당신의 계획에는 그 각각의 것들이 포함되어 있습니다.
[10:25] 라운드를 진행할수록 제한이 줄어듭니다. 주요한 것
[10:27] 기사에 대한 사람들의 불만
[10:29] 인류원리주의는 그것이 오직 다음과 같은 경우에만 작동한다는 것이었습니다.
[10:30] 토큰은 무제한입니다.
[10:32] 그래서 팀은 세 가지 규칙을 추가했습니다.
[10:34] 첫째는 3라운드 후에
[10:35] 리뷰어는 더 이상 항목을 나열하지 않습니다.
[10:37] 문제점을 지적하고 건축업자에게 알려줍니다.
[10:38] 기능을 개발하는 방식을 다시 생각해 보세요.
[10:40] 만약 그 후에도 함수가 계속해서 실패한다면
[10:42] 세 차례의 준비, 더 많은 작업
[10:44] 같은 방법을 써서는 해결되지 않을 겁니다.
[10:46] 두 번째는 1차 라운드 이후에
[10:48] 검토자는 변경 사항만 확인합니다.
[10:50] 완료되었으며 이미 완료된 사항은 보고하지 않습니다.
[10:52] 앞서 언급했듯이.
[10:54] 이로 인해 저는 전체 내용을 재검토할 수 없게 되었습니다.
[10:56] 기존 문제를 감지하고 해결하는 기능입니다.
[10:58] 하나씩. 그리고 세 번째는, 언제
[11:00] 검토자는 문제를 발견했습니다.
[11:01] 유형을 명시하십시오. 이런 식으로
[11:03] 개발자가 해당 유형을 수정합니다.
[11:05] 오류가 나타나는 모든 곳에서, 단지 그뿐만이 아닙니다.
[11:07] 검토자가 발견한 지점에서. 와 함께
[11:09] 이 세 가지 규칙과 그 변경 사항
[11:11] 그들은 첫 시도에 심사를 통과했습니다.
[11:14] . 저희의 검토 주기는 다음과 같습니다.
[11:15] 똑같지만, 각 라운드마다 더 많은 일을 합니다.
[11:17] 직업. 함수를 컴파일하고 검증합니다.
[11:19] 브라우저에서 각 평가를 수행한 다음
[11:21] 코드를 검토하세요. 그래서
[11:23] 우리는 그것이 일정 시간 후에 멈추도록 설정했습니다.
[11:24] 세 라운드 대신 다섯 라운드. 주기
[11:26] 도착하기 전에 멈출 수도 있습니다.
[11:28] 같은 문제가 계속되면 5로 늘립니다.
[11:30] 두 차례의 수정 끝에. 하지만
[11:32] 그 주기가 끝나고 모든 것이 끝나더라도
[11:34] 평가는 통과했지만 몇 가지 오류가 있었습니다.
[11:35] 그들은 계속해서 몰래 들어올 것입니다. 그러므로
[11:37] 두 가지가 더 필요합니다. 하나는 방법을 찾는 것입니다.
[11:39] 그 오류들을 찾고 또 다른 오류를 찾으세요
[11:40] 빠르게 되돌리세요. 팀
[11:42] 클로드는 거의 모든 것을 되돌릴 수 있습니다.
[11:44] 몇 분 만에 실행 가능하며, 그게 전부입니다.
[11:46] 이는 그들이 읽는 양을 줄이도록 해줍니다. 찾으려면
[11:48] 오류가 발생하더라도 그들은 직접 제품을 사용합니다.
[11:50] 매일 감지하기 때문에 보통 감지합니다.
[11:52] 고객보다 먼저 문제가 발생합니다. 할 수 있다
[11:54] 새로운 함수를 사용할 때마다 동일한 작업을 수행하십시오.
[11:56] 마치 고객처럼 직접 판단해 보세요. 하지만
[11:58] 함수의 작동 방식은 이미 알고 계시겠지만,
[12:00] 당신은 몇 가지 세부 사항을 놓칠 것입니다. 을 위한
[12:02] 이를 감지하려면 에이전트를 보낼 수 있습니다.
[12:03] 앱을 한 번도 본 적 없는 새로운 사람
[12:05] 사용자가 사용할 수 있도록 하기 위함입니다.
[12:07] 처음이에요. 해당 에이전트를 구성하려면,
[12:09] 클로드에게 하나 만들어달라고 요청할 수 있습니다.
[12:11] 앱이 보여주는 스킬
[12:12] 신규 사용자의 관점. 반드시
[12:14] 차단된 하위 에이전트를 사용하십시오
[12:16] 그들이 알지 못하도록 코드를 읽는 것입니다.
[12:18] 이 애플리케이션은 무엇에 관한 것인가요? 그들은 항해해야 합니다
[12:20] 앱을 통해 신규 사용자로 등록하고
[12:22] 누군가가 있는 모든 지점을 찾으세요
[12:23] 끼일 수도 있어요. 이 지침에 따라,
[12:25] 클로드는 사용자 스킬을 생성합니다.
[12:27] 처음 이용하는 사람과 이를 사용하는 에이전트
[12:29] 앱을 사용해 보세요.
[12:31] 또한 이는 테스트에 기초를 제공합니다.
[12:33] 임시 데이터이므로 원본 파일을 건드릴 필요가 없습니다.
[12:34] 실제 데이터를 생성하고 이를 방지하는 후크를 만듭니다.
[12:36] 에이전트에게 코드를 읽어달라고 하세요.
[12:38] 일반적으로 담당자는 그러한 상황을 피할 것입니다.
[12:40] 터미널 명령어를 이용한 잠금. 에 의해
[12:42] 또한, 그 후크는 읽기를 방해합니다.
[12:43] 그런 식으로 코드를 작성하세요. 실행하려면
[12:45] 한번 해보세요. 명령어를 사용하면 됩니다.
[12:46] 기술과 당신은 그에게 어떤 기능인지 말해줍니다.
[12:48] 확인해 드릴까요? 당신의 것을 바탕으로
[12:50] 지침: 애플리케이션을 열고 시작하세요.
[12:52] 어떻게 해야 하는지 전혀 모르는 에이전트
[12:54] 그는 그것을 짓고 나서 완성되기를 기다렸다.
[12:56] . 에이전트가 완료되면, 해당 능력은
[12:58] 발견한 모든 내용을 보고하고 제안 사항을 제시하십시오.
[13:00] 개선하기 위해 적용할 수 있는 수정 사항
[13:02] 당신의 앱. 오류를 찾는 것은
[13:04] 절반은 그렇고, 나머지 절반은 되돌리는 것입니다.
[13:06] 그 변화를 야기한 요인들. 그게 바로 이 제품의 용도입니다.
[13:08] Git을 사용하면 기본적으로 저장이 저장됩니다.
[13:10] 애플리케이션의 각 버전. Git을 사용하면
[13:12] 각 함수는 자체 복사본을 갖습니다.
[13:14] 프로젝트, 즉 브랜치라고 불리는 것입니다. 응
[13:16] 애플리케이션의 일부 기능이 문제를 일으킵니다.
[13:17] 나중에 문제가 생기면 간단히 해결됩니다.
[13:19] Git에서 되돌릴 수 있습니다. 을 위한
[13:20] 변경 사항을 찾아서 되돌리세요
[13:22] 뭔가 고장 났으면 클로드에게 물어보세요.
[13:23] fix a라는 스킬을 만드세요
[13:25] 실수. 기본적으로 함수가 실행될 때
[13:27] 원하는 방식으로 작동하지 않으면 이렇게 하세요.
[13:29] 능력에 문제가 있고 그것을 찾을 수 있습니다.
[13:31] 원인과 해결 방법. 노력하다
[13:33] 동일한 방법으로 오류를 재현하세요
[13:35] 단계를 거친 다음 가정이 맞는지 확인하십시오.
[13:37] 원인은 옳았습니다. 후에
[13:39] 그게 다입니다. 문제를 신고하고 해결하세요.
[13:41] . 이 기능이 작동하려면,
[13:43] 클로드에게도 알려줘야 해요
[13:45] Claude.md는 Git을 사용하고 자체적으로 생성합니다.
[13:47] 각 함수별로 분기합니다. 저도 그래야 해요
[13:49] 작업 중인 버전을 모두 저장하세요. 의
[13:51] 그런 식으로 함수가 작동하지 않을 때
[13:52] 예상대로 작동합니다, 클로드
[13:54] 저장된 버전을 검토하세요
[13:56] 그 변화를 야기한 원인을 찾아라
[13:58] 이전 버전으로 되돌립니다.
