---
title: "Tech Bridge — Anthropic은 하루 코드 변경 3만 건을 어떻게 병합할까요? (Addy Osmani × Manish Kapur 추정): 검증 증거 · 다층 검증 · 사람 책임자"
type: source
tags: [software-factory, lights-on-factory, dark-factory, verification, verification-evidence, automated-code-review, claude-md, agents-md, layered-verification, zero-trust, supply-chain-security, agent-sandboxing, agent-identity, pr-labeling, accountability, anthropic, claude-code, circleci, vendor-claim, video]
source-url: https://www.youtube.com/watch?v=CmsICMUPtII
source-type: video
author: Tech Bridge (편집, 내레이션 없음) · 대담 [[addy-osmani]](발화 호명 · 제목 · 설명란, 1인칭 "at Anthropic, we") × [[manish-kapur]](설명란 근거만 · 소거법 추정, 소속 미상) · 행사 · 녹화일 미상 · 원본 링크 없음
date-published: 2026-10-30
ingested: 2026-10-31
created: 2026-10-31
updated: 2026-10-31
---

# Tech Bridge — Anthropic은 하루 코드 변경 3만 건을 어떻게 병합할까요? (Addy Osmani × Manish Kapur)

[[tech-bridge|Tech Bridge]]의 **11:06 대담 편집본, 공식 챕터 11, 한국어 내레이션 없음.** 제목에 "[한글자막]"이 붙었지만 수동 자막은 없다. 오디오는 영어 원본 하나(더빙 7개 언어)이고 `ko-orig`가 없다 — 10-27 Voss · 10-28 Parakhin · 10-29 Chase 편과 같은 구성이라 **인용은 en-orig로만** 한다. raw: `01.raw/articles/2026-10-30_Anthropic은 하루 코드 변경 3만 건을 어떻게 병합할까요 - Addy Osmani.md`.

테제:

> **코드를 쓰는 일은 풀렸고, 병목은 병합할 확신이다. 그 확신은 에이전트가 스스로 내는 검증(실제 사용자처럼 시험한 증거)과, 모든 루프에 깔린 여러 겹의 독립 검증에서 온다. 사람은 diff 대신 증거를 보고, 에이전트가 썼어도 책임은 이름이 붙은 사람이 진다. 자율성은 그렇게 얻어 낸다.**

> *"software factory is harnessing loops at scale"*(01:00~01:02) · *"you need to give your agents a way to verify that the work is correct"*(03:10~03:14) · *"people are responsible for checking on the agent's evidence"*(05:14~05:17) · *"I might have kicked off a Claude a Claude run to complete a piece of work, but I'm I'm still on the hook."*(09:37~09:41) · *"Fast to write is not fast to ship."*(10:37) · *"autonomy is earned"*(10:48~10:51)

> ⚠️ **화자 귀속의 강도.** [[addy-osmani]]는 발화에서 두 번 호명되고(*"Adi was talking about"* 07:11, *"the same point of view, Addy"* 09:10) 제목 · 설명란에도 있다 — **강함.** 소속은 본인 1인칭(*"at Anthropic, like we"* 08:42~08:43, *"we were merging about 2,500 changes"* 03:50)이다. [[manish-kapur]]는 **설명란에만** 이름이 있고, Addy를 부르고 질문하는 다른 목소리에 소거법으로 붙였다 — **추정.** 소속은 발화되지 않는다.
>
> ⚠️ **제목의 "하루 3만 건"은 진행 쪽(Manish 추정) 발화다.** Addy는 이 숫자를 되풀이하지 않는다(§3). 설명란의 Anthropic 글 · Addy 블로그 링크는 열어 보지 않았다(미확인).
>
> ⚠️ **회사 내부 증언 + 출처 없는 통계.** Anthropic 쪽 사람이 자기 회사 · 자기 제품([[claude-code]])의 관행을 말한다. 진행 쪽의 CircleCI · 85% · 76% 통계는 출처가 발화되지 않는다.

## 1. 병합이 실패한다 (00:20~00:53)

- 진행: *"Circle CI analyzed 28 million CI workflows this year. And they noticed that the throughput jumped by about 59%. Uh but yet three in 10 attempts to merge that code into production are failing."*(00:20~00:32) — *"one independent stat from Circle CI"*(00:34~00:36). 자기 고객도 같다고 덧붙인다(00:40~00:44).
- 그리고 Addy의 문장을 슬라이드로 읽는다: *"A software factory is harnessing loops at scale."*(00:45~00:48)

→ [[mergeability-gap]](병합 실패율이라는 다른 측정) · [[verification-bottleneck]]

## 2. 두 공장 — lights-on과 dark (00:53~03:26)

- ⭐ Addy: *"A lights-on factory is one where you have agents that are helping you um with planning, building, checking, and shipping code again and again, but you as a person still apply your judgment and taste inside the picture."*(01:02~01:14)
- *"a dark software factory, which is a little bit closer to how, you know, a car factory with robotics might be working"*(01:16~01:22) — 사람은 *"thinking about intent"*로 물러나고 *"the greatest of exceptions"*에만 불려 온다(01:29~01:35).
- 대부분의 팀은 그 사이 스펙트럼 위에서 *"how do I get further and further into automation in a way that I can trust it"*(01:43~01:46)을 찾는 중이라고 한다.
- 진행: *"AI coding is now basically a solved problem"*(01:50~01:52), *"76% of the developers"*가 *"code is being produced at a speed that is impossible for them to verify it"*(02:00~02:09)라고 말한다는 통계(출처 미발화).
- Addy: 리더들의 질문은 *"how do we enable you to ship code faster um with confidence"*(02:29~02:34). ⭐ *"Agents can now generate ways for you to check your code much more cheaply than ever before."*(02:36~02:41) — 좋은 코드를 가능하게 하던 *"good tests, benchmarks, uh specs"*(02:50~02:54)를 에이전트가 더 싸게 만든다. 그래서 *"those checks are one of the most important things we should be spending our time on"*(03:02~03:06).
- *"you need to give your agents a way to verify that the work is correct. If you've got that in place and you can make sure that the code is both correct and complete, that can easily two to three by like the quality of your outcomes."*(03:10~03:23, ASR "two to three by" → 2~3배, 측정 없음)

→ [[software-factory]] · [[verification-cost-asymmetry]] · [[agent-verification-skill]]

## 3. 하루 3만 건을 리뷰하는 방법 (03:26~04:54)

- ⚠️ 진행: *"They are merging about 30,000 code changes every single day. They used to do about 3,000 or so, 2,500 or so code changes just a few months back. They've scaled from 2,500 code changes to 3,000 30,000 code changes per day."*(03:27~03:41) — 스스로 고쳐 말한다.
- Addy의 숫자는 다르다: *"we were merging about 2,500 changes all the way back in May"*(03:50~03:53, **기간 단위 미발화**). 그리고 Claude.ai 개편: *"we kind of three-byed the performance of it. That was accomplished by merging about 3,000 pull requests in a very short space of time with engineers, product designers, a number of different functions contributing"*(03:59~04:09). 3만은 확인도 부정도 하지 않는다.
- ⭐ **워크플로**: *"we first of all have Claude do a first pass review. What's very important in there is making sure that it has a way to actually try the experience out similar to a real user."*(04:15~04:24) — end-to-end 작업, 브라우저에서 확인, 도구 실행, 린팅(04:26~04:36).
- 버그 · 기능 공백이 나오면: *"we have hooks that will then go and run on any edits, they will study the diffs, and allow us to get this loop in place where we're correcting the PR as quickly as possible."*(04:44~04:53)

→ [[automated-code-review]] · [[trusted-throughput]]

## 4. 사람은 검증 증거를 본다 (04:54~05:46)

- taste를 공유 파일로: *"codify what you consider best practice and taste in your team's shared like Claude.md, Agents.md, anywhere where the agent can then consult during code review"*(05:03~05:14, ASR → CLAUDE.md · AGENTS.md).
- ⭐ *"And then people are responsible for checking on the agent's evidence."*(05:14~05:17) — 브라우저 UI라면 *"maybe generated me a video of that experience where it's been clicking around"*(05:28~05:31), 모바일 · 데스크톱이면 *"screenshots or videos"*(05:37~05:38). *"you want to get to a place where the agent's giving you as much verification evidence as possible"*(05:38~05:43).

→ [[agent-change-evidence]] · [[taste-encoded-evals]] · [[taste-vs-judgment]]

## 5. 다음 개선은 검증에서 (05:46~06:24)

- *"the next gains are going to come from a combination of us really nailing verification, right? As well as model quality."*(05:46~05:52) — 모델은 [[claude-opus-5-5|Opus 5.5]]에서 이미 *"pretty good"*(05:57)이라 한다.
- 문제는 처방의 구체성: *"if you tell people yeah, just like verify the work, you know, their next question is what does that even mean"*(06:05~06:09). Anthropic이 기대는 것: *"end-to-end tasks, property tests, any visual verification tests, things that can help us just get that confidence to merge those changes in automatically."*(06:15~06:23)

## 6. 루프마다 여러 겹 (06:24~07:45) — Manish(추정)

- ⭐ *"each company should adopt a zero trust multi-layered verification approach. And verification should be done in every loop."*(06:27~06:33) — 에이전트 루프 · CI 검증 루프 · 코드 유지보수(06:33~06:42).
- 세 층, 각각 다른 결함을 겨냥:
  1. **결정론적 층** — 버그 · 보안 이슈, *"sequel injection, buffer overflow"*(06:55~07:03, ASR → SQL injection)
  2. **에이전트 리뷰 층** — *"they catch logic and intent issues which the deterministic layer is not well suited to catch"*(07:15~07:20)
  3. **소프트웨어 공급망 보안 층** — CVE · 악성코드 · 악성 패키지 탐지(07:27~07:38)
- *"each layer is tuned and optimized to catch a certain type of issue"*(07:42~07:45). 직후 *"in terms of"*(07:47~07:48)에서 끊긴다(편집 컷 추정).

→ [[layered-verification-every-loop]](신규) · [[swiss-cheese-defense-in-depth]]

## 7. 통제 · 권한 · 샌드박스 (07:45~08:28)

- Addy: 몇 달 전 기업들의 걱정 — 에이전트가 *"hundreds, thousands of agents in some cases and they just didn't know what they were doing"*(07:58~08:01), 시스템 · 데이터 접근 · 프로덕션 배포. 관심사는 *"agent identity and telemetry"*(08:15).
- *"the three biggest things for a lot of companies are how do we think about control, how do we think about permissions, and how do we think about the sandbox?"*(08:17~08:23)

→ [[agent-sandboxing]] · [[agent-identity-separation]] · [[agent-governance-layers]]

## 8. 에이전트가 써도 책임자는 사람 (08:28~09:46)

- 질문: *"Should agent-written code be labeled in the PR?"*(08:28~08:30). Addy: *"I personally think it should."*(08:32)
- ⭐ 소유 의식의 이동: *"at Anthropic, like we we think about this a little bit differently. We've evolved to the point where we don't really mind so much if Claude is like labeled as hey, I'm I'm the one that wrote this thing, because we're a little bit more focused on the outcomes"*(08:42~08:54). 라벨은 *"what are some of the constraints and extra checks that we need to keep in place"*(09:08~09:10)를 정하는 데도 쓴다.
- Manish(추정): *"in the foreseeable uh you know, 6 to 9 months, we should label the PRs till we are confident enough in our factories"*(09:12~09:20) — 금융권 고객의 감사 가능성(09:23~09:25) 때문.
- ⭐ Addy: *"The accountability is the most important part here. Like, we still label like who's the owner for this change. I might have kicked off a Claude a Claude run to complete a piece of work, but I'm I'm still on the hook. If something goes wrong, I have to go and fix it."*(09:33~09:44)

→ [[named-human-accountability]]

## 9. 리더와 주니어, 안전한 병합 기준 (09:46~10:29)

- 리더: *"push your teams to really think hard about what verification means"*(09:54~09:57) — 지금의 테스트와 *"the agents being able to sign off on the code being good enough to merge on their own"*(10:05~10:08) 사이의 간격을 찾는 것.
- 주니어: *"actually getting more experience in the different flavors of tests, whether it's like end-to-end tests, property tests"*(10:13~10:17).
- *"the agent opened the PR. It is safe to merge when"* — Addy: *"You have full confidence nothing's going to go wrong, or that you've mitigated that as much as possible."*(10:25~10:28)

## 10. 빨리 쓰는 것 ≠ 빨리 내놓는 것 (10:29~11:06) — 진행 쪽 정리(추정)

- *"writing code is the fastest part, and that is solved. Strong review and verification for all teams uh is what will will help you maintain that speed. Fast to write is not fast to ship."*(10:29~10:37)
- *"Verify everything. And autonomy is earned."*(10:48~10:51) · *"We will get to software factories very soon, if not next year."*(10:51~10:54) · *"you need to put in independent automated verification inside each loop of your factory"*(10:56~11:00).

## 등장 개체

- 인물: [[addy-osmani]](신규) · [[manish-kapur]](신규, 추정)
- 조직 · 제품: [[anthropic]] · [[claude-code]] · [[claude-opus-5-5]](한 번 언급) · CircleCI(통계 출처로만, 페이지 없음) · Claude.ai(개편 사례, 페이지 없음)
- 개념: [[software-factory]] · [[verification-bottleneck]] · [[verification-cost-asymmetry]] · [[agent-verification-skill]] · [[agent-change-evidence]] · [[layered-verification-every-loop]](신규) · [[named-human-accountability]] · [[trusted-throughput]] · [[automated-code-review]] · [[mergeability-gap]]

## 이 위키에서의 좌표

- [[software-factory]]의 **lights-on / dark** 구분이 정의로 나온 첫 소스다. Pocock의 *"the lights are on"*(10-10) · Horthy의 *"lights-off software factory"*(10-15)가 이름만 쓰던 구분을 여기서는 *사람의 판단과 taste가 루프 안에 있는가* 로 가른다.
- [[verification-bottleneck]]의 답 중 *에이전트가 증거를 낸다*(10-09 [[tech-bridge-prompt-to-production]])와 같은 편이고, Claude Code 팀 대담(09-03 [[tech-bridge-claude-code-team-workflow]]의 *"PR을 생성하면 (…) 스크린샷"*)과도 맞는다 — **같은 회사의 두 번째 진술.**
- PR 라벨 문제는 [[named-human-accountability]]에 *작성자 표기와 책임자 표기는 다르다* 는 구분을 붙인다.

## ⚠️ 유보

- Manish Kapur 귀속은 설명란 + 소거법. 행사 · 녹화일 · 원본 링크 없음. 00:00~00:20 무캡션(첫 챕터 전체).
- "하루 3만 건"은 진행 쪽 발화로, 3,000 → 30,000 자기 정정이 있고 Addy는 확인하지 않았다. Addy의 2,500은 기간 단위가 없다.
- CircleCI · 85% · 76% · *"three-byed the performance"* · *"two to three by"* 모두 출처 · 측정 미발화.
- en 파일은 en-orig를 고쳐 쓴 문장이고 ko도 그 계열로 추정 — 인용하지 않았다.

## References

- raw: `01.raw/articles/2026-10-30_Anthropic은 하루 코드 변경 3만 건을 어떻게 병합할까요 - Addy Osmani.md`
- https://www.youtube.com/watch?v=CmsICMUPtII
- 설명란 링크(미확인, 열어 보지 않음): https://www.anthropic.com/research/redesigning-source-control · https://addyosmani.com/blog/software-factories/
