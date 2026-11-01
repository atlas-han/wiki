---
title: "Tech Bridge — AI가 코딩하면 개발자는 뭘 해야 할까? 앤드루 응의 답 (Andrew Ng 대담 발췌): AI engineering 네 역량 · 맥락 우위 · error analysis · 기본기와 trade-off · shaping the build · 단계 의존 · cognitive offloading"
type: source
tags: [andrew-ng, deeplearning-ai, ai-engineering, skills-map, coding-agents, software-engineering-fundamentals, trade-offs, error-analysis, evals, shaping-the-build, product-sense, full-stack, one-way-door, prototyping, spec, cognitive-offloading, learning, interview, video]
source-url: https://www.youtube.com/watch?v=2tEchomcjk4
source-type: video
author: Tech Bridge (대담 발췌 편집, 내레이션 없음) · 화자 [[andrew-ng|Andrew Ng]](제목 · 설명란 · 태그 근거 — 발화에 이름 없음) · 대담 상대 "폴 코플스톤"(설명란 근거만, 철자 · 소속 미상) · 원본 영상 · 녹화일 미상
date-published: 2026-10-31
ingested: 2026-11-01
created: 2026-11-01
updated: 2026-11-01
---

# Tech Bridge — AI가 코딩하면 개발자는 뭘 해야 할까? 앤드루 응의 답

[[tech-bridge|Tech Bridge]]의 **10:26 대담 발췌, 공식 챕터 8, 내레이션 없음.** 오디오는 `English (US) original (default)` + 더빙 7개이고 **한국어 트랙이 없다** — 10-27 Voss · 10-30 Osmani 편과 같은 구성이라 **인용은 en-orig로만** 한다(ko는 `tlang=ko` 기계 번역, `en`은 en-orig와 md5가 다른 고쳐 쓴 문장). 캡션의 `>>` 화자 전환은 05:09 질문 한 번뿐이고 나머지는 Ng의 답이다. raw: `01.raw/articles/2026-10-31_AI가 코딩하면 개발자는 뭘 해야 할까 앤드루 응의 답.md`.

테제:

> **AI가 코드를 많이 써 줘도 개발자의 일은 줄지 않고 위치가 바뀐다. 남는 것은 사람이 근본적인 맥락 우위를 가진 결정 — 무엇을 만들지, 지금 어떤 단계인지 — 과, 에이전트가 몰래 내리는 trade-off를 알아볼 기본기다. 다만 에이전트로 일을 끝내는 것과 배우는 것은 별개다.**

> *"I think the most exciting profession to be that's growing rapidly at this moment in time is AI engineering."*(00:21~00:27) · *"as building has become easier, the bottleneck is less building, but deciding what to build."*(05:19~05:28) · *"The answer is stage-dependent"*(07:16~07:18) · *"chatbots are terrible for learning"*(09:05~09:08)

> ⚠️ **화자 신원.** 발화에 이름이 없다. **Andrew Ng**은 제목(*"앤드루 응의 답"*) · 설명란 · 태그(`Andrew Ng` · `DeepLearning.AI`) 근거이고, 발화로는 1인칭 *"my team"* 의 skills map 작업(00:42~00:52)과 08-30 [[tech-bridge-andrew-ng-ai-opportunity]]의 같은 논지(skills map 작업 · cognitive offloading · 숙제와 시험)가 정황으로 맞는다. **대담 상대**는 설명란의 *"폴 코플스톤"* 뿐 — 발화 · 태그에 이름이 없고 영문 철자 · 소속도 없어 **페이지화하지 않고 귀속도 하지 않는다.**
>
> ⚠️ **"my team at the Y Combinator I"**(00:42~00:45)는 **DeepLearning.AI로 판독 추정**(태그 · 설명란 링크 근거). en 변종은 *"Droid AI"*. Y Combinator로 읽지 않는다.
>
> ⚠️ **편집본이다.** 주제 전환 지점(02:02 · 03:12 · 07:16 · 09:02 · 10:05)에 이음매가 보이고, 07:16의 *"The answer is stage-dependent"* 는 캡션에 없는 질문에 대한 답이다. 녹화일 · 행사 · 원본 링크 미상.

## 1. 소개: AI가 코드를 짜 주면? (00:00~00:21)

무캡션(en-orig 첫 큐 20.9초). 이 챕터의 내용은 쓰지 않는다.

## 2. AI 시대 개발자의 네 가지 역량 (00:21~02:02)

- 직함이 아니라 역량: *"by that I don't mean people that will take on an AI engineering job title, but rather people in all sorts of job roles, including software engineering, front-end, back-end, DevOps, mobile, that will benefit from here having AI engineering skills."*(00:27~00:42)
- 방법(화자 진술): *"we looked at over 10,000 job descriptions and your job postings, did dozens of structured interviews"*(00:56~01:03), 자체 설문 · 파트너 대화 종합(01:03~01:08). ⚠️ 문서 · 링크 없음.
- ⭐ 결론: *"there are four key skills needed to do AI engineering well."*(01:10~01:13)

| # | 역량 | en-orig |
|---|---|---|
| 1 | AI 앱 빌드 · 배포 | *"the ability to build and deploy AI applications. And the difference between AI and non-AI applications is they're uncertain."*(01:13~01:19) |
| 2 | 소프트웨어 공학 기본기 | *"even if AI writes a lot of code for us, people that understand software engineering fundamentals understand what's the read-write ratio, what's a transaction"*(01:25~01:36) |
| 3 | 코딩 에이전트 활용 | *"Third is the ability to use coding agents."*(01:40~01:42) |
| 4 | shaping the build | *"developers are no longer playing a role where someone tells them what to do and they just implement it, but instead are participating in deciding what to build and also influencing the process by which something gets built."*(01:48~01:58) |

→ [[ai-engineering-skills-map]](신규) · [[ai-engineer-vs-ml-researcher]](직무 정의와의 대비) · [[three-tier-ai-skill-stack]]

## 3. AI가 모르는 맥락을 가진 사람 (02:02~03:13)

- ⭐ 기준: *"one of the key things that distinguishes whether AI will take this over or not is whether or not humans have a fundamental context advantage."*(02:02~02:11)
- 예: *"we know a ton of stuff that AI agents do not know. You may remember a conversation with a customer, you know, where you said something and there was a funny expression on their face"*(02:13~02:23), 5년 전 읽은 시장 보고서(02:25~02:31).
- *"humans have a bewildering vast range of context and remarkably good at pulling out this context and make key decisions."*(02:31~02:40) — 모든 대화의 표정을 카메라로 기록하는 날이 오기 전까지는(02:45~02:53, 반농담).
- *"there's a large set of tasks where humans have a fundamental context advantage that we'll want humans to do for a long time."*(02:54~03:00) → 그 일을 할 역량을 주어 *"complement the wonderful work that coding agent is doing"*(03:04~03:10).

→ [[ai-engineering-skills-map]] · [[ai-jobs-impact]](task 단위 보완론의 개발자 판) · [[tech-bridge-laurie-voss-product-engineer]]의 *"It is in the mind of the person who runs that business"* 와 같은 방향

## 4. 실력 차이는 평가와 오류 분석에서 (03:13~03:54)

- *"the key differentiator for AI applications compared to traditional software applications is they are uncertain."*(03:20~03:27) *"Whether you prompt an LLM or train a supervised learning algorithm, you don't know in advance what outcome you get."*(03:30~03:36)
- *"the skilled AI developers have come up with or are familiar with a set of techniques to monitor the performance of these systems."*(03:36~03:44) — 그리고 *"error analysis and eval's loop to make progress in a systematic way"*(03:47~03:52).
- ⚠️ 03:44~03:50(*"Often it's this go way. Um and to drive a distant"*)은 판독 보류. 기법의 구체 내용은 이 발췌에 없다.

→ [[production-trace-eval-flywheel]] · [[eval-experiment-anatomy]]

## 5. 도구가 바뀌어도 기본기는 남는다 (03:54~05:09)

- 배포 · 모니터링 · 갱신의 기본 지식은 *"actually changing much slower than the PR hype says."*(04:07~04:09)
- trade-off: *"cost latency uh and then uh speed, reliability"*(04:20~04:25)
- ⭐ *"until you understand the fundamentals, you often don't even know what trade-offs exist to be made, which is why when someone write code without understanding, very often the coding agent will make a bunch of trade-offs that you didn't even know it made a trade-off and just bites you later."*(04:28~04:45)
- *"people that are good engineers understand the fundamentals in many, many parts of the skills needed just make much better decisions."*(04:45~04:55) 동시에 *"I'm also encouraged at what's now possible to do, you know, when you write code without understanding"*(04:55~05:00) — 이해 없이 짜는 코딩을 깎아내리지는 않는다. 비교 대상 *"any series engineers"*(05:07)는 판독 보류.

→ [[ai-engineering-skills-map]] · [[three-tier-ai-skill-stack]](기초를 건너뛰면 나중에 청구된다) · [[read-fluency-for-agent-output]]

## 6. 이제는 무엇을 만들지 결정할 때 (05:09~07:18)

- 질문(대담 상대, 캡션에 남은 유일한 질문): *"as part of the skills map you talk about shaping the build. I found this kind of an interesting concept. Maybe you can explain what what you mean by shaping the build?"*(05:11~05:18)
- ⭐ *"as building has become easier, the bottleneck is less building, but deciding what to build."*(05:19~05:28)
- 1단계 — 역할의 폭: 프런트엔드 개발자가 AI로 백엔드까지(05:30~05:39). 본인은 백엔드가 강한데 *"frankly, I'm a maybe like a bad front-end developer with AI assistance."*(05:43~05:48) → *"a lot of developers have gone from a more narrow role to being a full-stack developer."*(05:48~05:54)
- 2단계 — 무엇을 만들지: PM의 고객 피드백을 기다리는 것은 *"much slower than the developer themselves has a little bit of product insight, little bit of product gut."*(06:02~06:10)
- 선 긋기: *"it does not mean engineers should become product managers"*(06:26~06:31)
- 3단계 — 과정을 정하기: *"we call this shaping the build"*(06:44~06:46). *"Like, is this a good time to build an MVP? Or is it a good time to invest in building really robust architecture and thinking about scale? Or is this a good time to go out to customers to get feedback?"*(06:53~07:04) → *"developers that can steer the building process end up contributing much more to the overall um company or project."*(07:08~07:16)

→ [[shaping-the-build]](신규) · [[tech-bridge-laurie-voss-product-engineer]](product engineer) · [[taste-vs-judgment]]

## 7. 빠른 실험과 치밀한 설계의 기준 (07:18~09:02)

- ⭐ *"The answer is stage-dependent and it depends a lot on, you know, what Jeff Bezos calls one-way doors versus two-way doors."*(07:16~07:23) — 앞 질문은 캡션에 없다.
- 초기: *"whatever idea you have, write type it in the coding agent, build it, see what you get."*(07:27~07:34) 단 안전하게, 민감 데이터를 흘리지 않게(07:36~07:39).
- *"one of the challenges about AI engineering is the right decision is very stage-dependent."*(07:43~07:47)
- *"for early stage projects, so long as you can do it in a responsible, safe way, build a quick and dirty prototype, see what happens, throw it away, build another quick and dirty prototype, see what happens, and drive rapid learnings."*(07:47~08:01)
- 그리고 *"there's also a time and place to thinking carefully about architecture"*(08:01~08:05) — read-write 비율, 고객 요구, 민감 데이터, 보안 인프라(08:05~08:12).
- 사람의 축: 0→1 스타트업 단계에 강한 엔지니어와 성숙한 체계적 단계에 강한 엔지니어가 따로 있다(08:16~08:22). 단계에 따라 *"how to think about velocity versus protecting from downside risk shifts"*(08:31~08:35).
- 코딩 에이전트 사용에도: *"you should always plan it out, write a long spec, and there is a place for that."*(08:41~08:46) 그리고 *"if you know you're going to go to bed in 20 minutes, just bang out some stuff, have a coding agent work for a few hours and see what you get the next morning."*(08:48~08:54)
- *"that stage-dependent answer has been very tricky for people to learn."*(08:54~08:59)

→ [[shaping-the-build]] · [[action-reversibility]](one-way / two-way door) · [[disposable-vs-durable-software]] · [[spec-driven-development]]

## 8. AI가 일을 해줘도 실력은 별개다 (09:02~10:26)

- ⭐ *"I'm going to say something obvious but may be sound controversial, but chatbots are terrible for learning"*(09:04~09:08) — 본인은 LLM을 많이 쓴다(09:11~09:13).
- *"students that use LLMs do better on homeworks but worse on final exam."*(09:19~09:24) 엄밀한 연구가 나오고 있다(09:30~09:32, ⚠️ 연구명 없음). 정리: *"you get more work done, but you learn less."*(09:36~09:42)
- ⭐ 새 대상: *"I think people still underestimate the degree to which this is happening among working adults."*(09:49~09:55) 자기 이야기로: *"I love my coding agents, helps you do a ton of work, but the reduced thinking I have to do"*(09:55~10:03) — 문장이 끊긴다(편집).
- 단서: *"there are ways to use LLMs that do improve learning."*(10:05~10:10) TikTok 비유 → *"the vast majority of ways that the vast majority of people use LLMs does not result in learning."*(10:20~10:23)

→ [[cognitive-offloading]] · [[ai-assisted-learning]]

## 등장 개체

- 인물: [[andrew-ng]](제목 · 설명란 · 태그 근거) · 대담 상대 "폴 코플스톤"(설명란만, 페이지 없음) · Jeff Bezos(one-way/two-way door 출처로 언급, 페이지 없음)
- 조직: DeepLearning.AI(태그 · 설명란 링크, 발화는 ASR *"Y Combinator I"* 로 깨짐 — 페이지 없음)
- 개념: [[ai-engineering-skills-map]](신규) · [[shaping-the-build]](신규) · [[cognitive-offloading]] · [[action-reversibility]] · [[disposable-vs-durable-software]] · [[spec-driven-development]] · [[three-tier-ai-skill-stack]] · [[ai-engineer-vs-ml-researcher]]

## 이 위키에서의 좌표

- 08-30 [[tech-bridge-andrew-ng-ai-opportunity]]에서 Ng은 *팀이 AI engineering skills map을 작업 중* 이라 했고 병목을 *product management bottleneck* 이라 불렀다. 이 편은 **그 skills map의 네 역량**을 직접 말하고, 병목을 개발자 쪽 이름 — **shaping the build** — 으로 다시 붙인다.
- 09-16 [[cedric-clyburn|Clyburn]]의 [[three-tier-ai-skill-stack]]이 *기초 · AI 특화 · 배포* 의 **학습 순서**였다면, Ng의 네 역량은 **AI 앱 · 기본기 · 에이전트 · 무엇을 만들지 결정** 으로 넷째 칸에 **판단**을 둔다. 둘 다 *기본기를 건너뛰면 대가를 치른다* 는 데서 겹친다.
- 10-27 [[laurie-voss|Voss]]의 product engineer(*"finds out what people need, defines what good looks like, and ships it"*)와 Ng의 *product gut* 가진 엔지니어는 같은 방향이다. 단 Ng은 *"it does not mean engineers should become product managers"* 라고 선을 긋는다.
- [[cognitive-offloading]]은 지금까지 **학생 · 학습자**의 문제로 쌓였다. 이 편은 Ng 본인이 **일하는 어른과 자기 코딩 에이전트 사용**으로 범위를 넓힌다.

## ⚠️ 유보

- 화자 신원은 제목 · 설명란 · 태그 근거. 대담 상대는 설명란 한글 표기뿐. 원본 영상 · 녹화일 · 행사 미상.
- skills map의 방법론(1만 건 넘는 공고 · 수십 건 인터뷰 · 설문)과 학습 연구는 출처가 제시되지 않았다.
- *"Y Combinator I"* → DeepLearning.AI, *"rewrite ratio"* → read-write ratio는 판독 추정. 03:44~03:50, 05:07, 09:13, 07:40~07:41은 판독 보류.
- 편집본이라 질문 대부분과 일부 문장(10:03~10:07)이 빠졌다. ko · en은 인용하지 않았다.

## References

- raw: `01.raw/articles/2026-10-31_AI가 코딩하면 개발자는 뭘 해야 할까 앤드루 응의 답.md`
- https://www.youtube.com/watch?v=2tEchomcjk4
- 설명란 링크(열어 보지 않음): https://www.deeplearning.ai/resources
