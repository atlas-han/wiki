---
title: "Tech Bridge — 바이브 코딩, 이렇게 싸도 될까? GPT-6.1 Terra vs Opus 5.5 (Nick Saraev 추정): 같은 프롬프트 데모 5종 · computer use 사례 · 비용 대비 점수 벤치마크"
type: source
tags: [openai-terra, claude-opus-5-5, model-comparison, coding-agents, codex, claude-code, max-effort, computer-use, benchmark, pareto-frontier, cost-vs-score, factual-error-rate, taste, pricing, user-review, video]
source-url: https://www.youtube.com/watch?v=FwJ6Ae_-u4M
source-type: video
author: Tech Bridge (발췌, 내레이션 없음) · 화자 [[nick-saraev]] 추정(설명란 · 태그 근거 — 발화에 이름 없음) · 원본 영상 · 녹화일 미상
date-published: 2026-11-01
ingested: 2026-11-02
created: 2026-11-02
updated: 2026-11-02
---

# Tech Bridge — 바이브 코딩, 이렇게 싸도 될까? GPT-6.1 Terra vs Opus 5.5 (Nick Saraev 추정)

[[tech-bridge|Tech Bridge]]의 **11:48 발췌, 공식 챕터 15, 내레이션 없음.** 오디오는 `English (US) original (default)` + 더빙 7개(fr · de · hi · id · it · pt · es)이고 **한국어 트랙 · `ko-orig`가 없다** → **인용은 en-orig로만** 한다. 00:00~00:20(챕터 *"한국어 소개"*)은 en-orig 무캡션이다. raw: `01.raw/articles/2026-11-01_바이브 코딩 이렇게 싸도 될까 GPT-6.1 Terra vs Opus 5.5.md`.

하루 전 [[tech-bridge-nick-saraev-kimi-k3-1-vs-opus-5-5|Kimi K3.1 vs Opus 5.5]] 편과 **같은 형식**이다: 한 제작자가 **같은 프롬프트 · 같은 도구 · 각자의 하네스(max effort)** 로 [[openai-terra|GPT-6.1 Terra]]([[codex|Codex]])와 [[claude-opus-5-5|Claude Opus 5.5]]([[claude-code|Claude Code]])에게 데모를 만들게 하고 비교용 랜딩 페이지에서 하나씩 연다. 이번엔 후반 5분을 **남의 computer use 사례**와 **Terra 랜딩 페이지의 벤치마크 그래프** 읽기에 쓴다. 테제(화자 결론):

> **Terra는 일정 복잡도까지는 훌륭하고 절반의 시간 · 1/3의 토큰 · 약 1/12의 비용으로 끝낸다. 3D · 디자인 · 게임 같은 상위 수준에서는 Opus 5.5가 확실히 앞선다. 그래도 그래프상 Opus의 95~97%를 11% 비용에 내는 것 — 그것이 레버리지다.**

> *"it looks like GPT-6.1 Terra is great up to a certain level of complexity."*(06:06~06:14) · *"I think it's clear that at the higher levels of all of this, Opus 5.5 reigns supreme."*(06:25~06:31) · *"it scored about 95 to 97% of Claude Opus 5.5 at 11% of the cost. That, ladies and gentlemen, is leverage."*(11:38~11:46)

> ⚠️ **화자 신원은 설명란 · 태그 근거다.** 발화에 이름이 없다(01:35 *"What am I, freaking Nicholas Copernicus?"* 는 지구 · 태양 농담). 설명란 *"닉 사라예프가 같은 프롬프트와 도구, 최대 추론 강도로…비교했습니다"* 와 info.json `tags`의 `Nick Saraev`가 근거이고, Kimi 편과 형식 · 규칙 문장이 거의 같다는 것은 보조 정황이다. → [[nick-saraev]] **추정**.
>
> ⚠️ **한 제작자의 주관적 비교 + 출처 미표기 벤치마크.** 프롬프트 원문 · 채점 기준 · 반복 횟수가 없다. 시간 · 토큰 · 비용은 화자 진술이고, 벤치마크 수치는 화자가 그래프를 **눈대중으로** 읽은 값이다(*"maybe"*, *"I don't know"* 가 섞인다). 그래프는 *"a beautiful GPT-6.1 Terra landing page"*(07:37~07:41)에 있는 것으로 들려 **OpenAI 쪽 자료로 보이지만 미확인** — 벤더 자료일 가능성이 높다.
>
> ⚠️ **computer use는 화자가 직접 시험하지 않았다.** Paint 데모는 *"that's from Rohit over here"*(07:07~07:09), 평가는 [[greg-brockman|Greg Brockman]]의 말을 읽은 것이다.

## 1. 한국어 소개 (00:00~00:20)

en-orig에 발화가 없다(무캡션, 첫 큐 00:20.6). 챕터 이름으로 보아 한국어 소개로 추정 — 영상을 보지 않아 미확인. 이 구간의 내용은 쓰지 않는다. Kimi 편과 달리 en-orig는 **문장 처음**(*"What I have here is I have a landing page"*)에서 시작한다.

## 2. 같은 프롬프트로 비교한 두 모델 (00:20~00:47)

- 비교용 랜딩 페이지를 직접 만들었다(00:20~00:28).
- 규칙: *"My constraints here were that both models needed to get the same prompt. They also needed to use the same tools and they got to use their own coding harness at max effort."*(00:28~00:37) · *"GPT 6.1 Terra gets to use Codex, Claude Opus 5.5 gets to use Claude code, and they're actually running at the same time."*(00:37~00:45)

> ⚠️ **하네스가 다르다** — Kimi 편과 같은 한계. 이 실험은 Terra + [[codex|Codex]] vs Opus + [[claude-code|Claude Code]], 즉 **모델 + 하네스 쌍**의 비교다([[model-harness-knowledge-stack]]).

## 3. 제작 시간과 토큰은 얼마나 다를까 (00:47~01:20)

- ⭐ *"GPT 6.1 Terra took 23 minutes and 43 seconds on average versus Claude Opus 5.5's 43 minutes and 52 seconds."*(00:48~00:57) — *"about half that of Opus 5.5"*(01:00~01:03).
- ⭐ 토큰: *"number of total output tokens here was a third. And so, in addition to finishing far faster, it also finished for about a third of the tokens."*(01:03~01:12)
- 비용: *"Keeping in mind, GPT 6.1 Terra's cost is also a fraction of Opus 5.5's. This puts it at, I believe, less than 8/12 of the total kind of a dollar usage."*(01:09~01:21) — ⚠️ *"8/12"* 는 **"a twelfth"의 ASR 오인식으로 읽는다**(en *"one-twelfth"*, 곧이어 *"costing 1/12 of this"* 02:33~02:37 등 화자가 계속 "12배"를 쓴다).

> ⚠️ 평균의 표본 수 · 토큰 실측값 · 1/12의 계산 근거는 미발화. Kimi 편의 Opus 평균(47분 2초)과 이번(43분 52초)이 다른 것은 **데모 세트가 다르기** 때문으로 보인다(마인크래프트 · 랜딩 페이지만 겹치는 이름이다). Terra의 토큰 단가도 이 영상에서는 말하지 않는다 — 10-29 첫인상 리뷰어는 *"$1 per million in and $5 per million out"* 이라 했다([[tech-bridge-gpt-6-1-terra-first-look]], 미확인).

→ [[inference-speed-as-capability]] · [[true-cost-to-perfect-answer]]

## 4. 태풍 지도에서 갈린 취향과 기능 (01:20~02:38)

- Terra *"Storm Watch"*: 지구의 폭풍을 실시간으로 보여 주고, 클릭하면 예상 경로 · 내용을 보여 준다(01:21~01:44). *"I would definitely watch this versus the news weather report any day."*(01:54~01:58)
- Opus: ⭐ *"I would say honestly, I probably like the globe of 6.1 Terra more."*(01:58~02:06) 디자인도 Terra 쪽이 좋다 — 그러나 *"you can zoom way in, which is certainly something to behold"*(02:08~02:14), 소용돌이 · 효과 처리가 조금 낫고 레이어를 끌 수 있다.
- 판정 유보: *"Tough for me to say which one's better."*(02:30~02:31) · *"I think they're offering slightly different levels of functionality here"*(02:31~02:35) · ⭐ *"I will say 6.1 Terra costing 1/12 of this, definitely not 1/12 the quality."*(02:33~02:39)

→ [[taste-vs-judgment]](취향은 Terra, 기능 깊이는 Opus — 화자가 둘을 나눠 말한다)

## 5. 폭풍 시뮬레이션의 디테일 (02:38~03:26)

- Terra *"The Long Night"*: 배 · 등대 · 강풍, 시네마틱 카메라, 파도 세기 조절(02:39~02:57). 한계: *"I don't think this is going to win any awards for that water because it clearly has a grid pattern on it."*(02:57~03:03)
- Opus: *"If I compare and contrast that with Opus 5.5, you'll see it didn't really do that good of a job either."*(03:05~03:13) — 화자는 프롬프트 탓으로 본다: *"Presumably, this is limited to, you know, whatever the prompt was for this."*(03:10~03:16)
- *"definitely looks a little bit better, but again, definitely not 12 times better."*(03:22~03:26)

## 6. 마인크래프트는 둘 다 잘 만든다 (03:26~03:57)

- Terra: *"pretty solid"*, 자유롭게 지을 수 있다(03:26~03:39). Opus: 횃불 같은 것을 놓는데 *"Not really sure if that's like intended functionality"*(03:47~03:52).
- ⭐ *"I'd say Minecraft bench is probably fully saturated now cuz virtually all models can do like a really stand-out job."*(03:50~03:57)

> Kimi 편에서는 같은 이름의 데모에서 **Opus 캐릭터가 움직이지 못했다**(06:59~07:01 그 편). 이번엔 둘 다 작동했고, 화자는 이 테스트 자체가 **변별력을 잃었다**고 판정한다. ⚠️ 같은 프롬프트였는지는 미발화.

## 7. 게임은 돌아가기만 하면 될까 (03:57~05:07)

- *"Neon Drift"* — *"kind of like a Mario Kart style game"*(04:04~04:09).
- Terra: *"I will say the UX is kind of weird."*(04:06~04:12) 너무 쉽고, *"why am I in a freaking rocket ship?"*(04:24~04:28) — *"games like this aren't really well thought out"*(04:21~04:24).
- ⭐ Opus: *"Not going to lie, I think Opus 5.5 did a far better job."*(04:30~04:36) · *"we also have way better interactions."*(04:35~04:39) — 부스트, 이기기 어려움, *"this is actually very fun"*(04:39~04:41).
- ⭐ 품질의 측정 가능성: *"I won't say it's 12 times the quality, but with a game, it's not really like quantitative, right? It's more like qualitative."*(04:47~04:55) · *"Despite this costing, you know, significantly more, this is something that I would actually play."*(04:53~04:58) · *"Probably would never play that uh Terra game."*(05:00~05:03)

→ [[taste-vs-judgment]] · [[cost-vs-score-frontier]](게임 품질은 점수 축에 잘 올라가지 않는다는 화자 자신의 단서)

## 8. 시계 웹사이트의 디자인 격차 (05:07~06:05)

- Terra *"Meridian"* 시계 랜딩 페이지: 자산을 모두 Terra가 만들었다(05:15~05:19). *"the scroll animation is something that would have been impressive like 4 years ago. Now it's kind of overplayed."*(05:24~05:30) 톱니바퀴가 도는 것은 좋다.
- Opus: 처음엔 *"not seeing the watch on the right hand side. Don't know if that's intentional or if maybe something is broken."*(05:34~05:42) — 그러나 ⭐ *"This though is far higher quality such to the point where it's not even funny."*(05:40~05:46) 3D 레이아웃, 더 많은 구성 요소, 시각적 충실도, 색 변경. *"Opus really outdid itself with with Terra cannot even compare to something like this."*(05:59~06:06)

> ⚠️ Opus 페이지의 시계 누락이 결함인지 의도인지는 화자도 판단하지 않는다. Kimi 편의 *"두 번 작동하지 않았다"* 와 달리 이번 다섯 데모에서 **명확한 작동 실패는 보고되지 않는다.**

## 9. Terra를 쓸 곳과 Opus가 앞선 곳 (06:05~06:42)

- ⭐ 데모 결론: *"it looks like GPT-6.1 Terra is great up to a certain level of complexity."*(06:06~06:14) · *"3D complexity in particular, Opus 5.5 just wiped the floor with Terra on."*(06:11~06:18)
- 설계 의도: *"the idea of this demonstration was to give you guys a look at both like 1D stuff, uh, 2D stuff, and then ultimately 3D stuff, as well as game design."*(06:16~06:27) → *"at the higher levels of all of this, Opus 5.5 reigns supreme."*(06:27~06:31)
- 그래도 Terra의 자리: *"specifically in computer use, given the costs and also the speed with which it can do its job."*(06:33~06:43)

> ⚠️ "1D · 2D · 3D"는 화자의 분류이고, 어느 데모가 어느 층인지는 명시하지 않는다.

## 10. 컴퓨터 조작에서 드러난 가능성 (06:42~07:37)

- *"Lots of really cool examples of Terra being used primarily for computer use, which I think aligns with my expectations."*(06:41~06:49)
- Paint 데모: *"This is not a sped up video at all."*(06:47~06:52) · *"Terra was told to make an image of Sam Altman on this Paint app."*(06:52~06:55) — high 모드, 클릭 · 드래그가 빠르다. 출처: *"that's from Rohit over here."*(07:07~07:09, ⚠️ 신원 미상).
- ⭐ Brockman 인용(화자가 읽음): *"One of the founders of OpenAI, Greg Brockman over here"*(07:07~07:12) *"says computer use with Terra has crossed a qualitative threshold where it feels faster using a computer than what I can do unassisted, and I would agree with him on most cases."*(07:10~07:19)
- 이어 *"Sam Altman and co. are onto something here"*(07:19~07:23) 뒤에 *"It really is great at a lot of things, but we're super excited about computer use."*(07:21~07:27) — ⚠️ **화면의 OpenAI 쪽 게시물을 읽은 것으로 보이나 누구의 글인지 미발화**(바로 뒤 *"I'm excited about computer use, too"* 로 화자 자신과 구분된다).
- 화자 해석: *"I think this is honestly one of the things that's been kind of clunky with a lot of models."*(07:27~07:34) · ⭐ *"computer use being effectively solved means a lot of knowledge work applications open up."*(07:32~07:37)

> ⚠️ **Contradiction(약):** 10-29 첫인상 리뷰는 Terra의 computer use를 *"decent (…) for that price"* 라 하면서도 Blender에서 카메라 뷰만 바꾸고 *"Done"* 한 실패를 보여 주고, 패턴으로 *"it gives up very easily"* 를 짚었다([[tech-bridge-gpt-6-1-terra-first-look]]). 이번 편은 *"effectively solved"* 라고까지 말한다 — 그러나 근거는 **남의 데모 한 편과 OpenAI 공동 창업자의 말**이고 화자의 직접 시험이 아니다. *"effectively solved"* 는 화자의 과장으로 둔다.

→ [[openai-terra]] · [[greg-brockman]] · [[agent-native-interface]]

## 11. 벤치마크와 실제 사용감 (07:37~08:02)

- ⭐ 화자의 단서: *"the benchmarks themselves are not super valuable or important these days. It's virtually impossible to tell how a model really feels in your hands."*(07:43~07:51) 그래도 *"just to understand where it ranks relative to other models on standardized evals, it is kind of informative and valuable to go through these at least at high levels."*(07:51~08:00)

## 12. 비용 대비 점수로 읽는 성능 (08:02~10:14)

- 그래프 읽는 법: *"what this is is cost versus score. It's basically the efficiency of a model per dollar to do the stuff that you're asking it to do."*(08:04~08:13) x축 비용(최대 $8), y축 **Agents' Last Exam** 점수 35~65%(08:13~08:28, ⚠️ 이름 ASR *"Agents Last Exam V1"* · *"Agent's Last Exam"*). *"anything in the top left-hand corner is cheaper and it scores higher."*(08:38~08:43)
- 이전 세대: *"the old variant of GPT-5.6 Terra here scored kind of low across both score and cost."*(08:44~08:52) — 약 $4에 약 50%.
- ⭐ *"GPT-6.1 Terra is basically leading what's called the Pareto frontier"*(08:55~09:00)
- ⭐ 사고 모드 간 비용 차이가 작다: *"there really isn't that big of a difference in cost between the lowest thinking mode and then the highest thinking mode."*(09:06~09:13) · *"cost barely goes up."*(09:14~09:16) — 약 10센트에 50~55%대, 약 $1.25에 약 60%(09:16~09:26, 화자 눈대중).
- 같은 회사의 상위 모델과: *"this is actually better than GPT-6.1 Soul at most tasks."*(09:28~09:36) 단 *"there are situations where max max GPT-6.1 Soul is going to outperform maybe low mode Terra."*(09:33~09:42) — max 사고의 Terra가 *"at least for OpenAI models"* 그래프 최상단(09:42~09:49).
- ⭐ Opus와: *"The only situation in which it gets beat is by Opus 5.5."*(09:49~09:54) · *"maybe you gain a couple percentage points of, you know, score, but at what cost, right? This is about a dollar and Opus 5.5 here is about nine."*(09:54~10:02) → *"you get about, you know, 90, I don't know, 7% of performance for 1/9 or maybe 11% cost. And that's a trade-off that a lot of people are willing to make."*(10:02~10:15, *"90 … 7%"* → 97%로 판독)

> ⚠️ **모두 화자의 그래프 읽기다.** 그래프 원자료 · 작성 주체 · 측정 조건(하네스 · 반복)이 없다. "$1 vs $9" 는 **작업당 비용 축의 값**이라 이 위키의 [[true-cost-to-perfect-answer]] 단위(쓸 수 있는 답 하나당 비용)에 가깝지만, 그 그래프가 합격률을 어떻게 반영하는지는 알 수 없다. 데모의 *"1/12"* 와 그래프의 "1/9 · 11%" 는 다른 측정이다.
>
> ⚠️ **GPT-6.1 Soul · GPT-5.6 Terra는 이 위키에 페이지가 없다.** Soul은 10-29 리뷰의 *"distilled Astra or Soul"* 에 이어 두 번째 등장이고, 여기서 처음 **"GPT-6.1"** 번호가 붙는다(화자 발화). Terra에 GPT-5.6 세대 *"old variant"* 가 있었다는 것도 화자 발화뿐이다.

→ [[cost-vs-score-frontier]](신규) · [[pareto-surfing]] · [[model-mixing-economics]]

## 13. 이미지를 이해하는 능력 (10:14~10:37)

- *"It's also really good at vision."*(10:13~10:18) *"GPT-6.1 Terra over here again scores the top left of the Pareto frontier across the board"*(10:15~10:22) — 전작 GPT-5.6 Terra 대비, 이미지 입력 · *"coordination to do between, I don't know, 3D designs"*(10:31~10:35)에 권한다. ⚠️ 수치 · 벤치마크 이름 미발화.

> 3D 데모에서 Opus가 *"wiped the floor"* 했다는 9절과 *"3D designs"* 에 Terra를 권하는 이 절은 **결이 다르다** — 화자는 둘을 연결하지 않는다(비전 *이해* vs 3D *생성*으로 읽을 수 있다).

## 14. 사실 오류는 낮을수록 좋다 (10:37~11:15)

- x축 비용 0~약 60센트, y축 *"answers with any factual error"*(10:44~10:51), *"lower here is actually better."*(10:53~10:54)
- ⭐ *"you can see that Terra actually performs the best out of all models right now on its factual reporting."*(11:00~11:07) → *"this is the model you're going to want to use as your daily driver for most conversations, especially for initial research and initial creation of reports."*(11:07~11:16)

> ⚠️ *"out of all models"* 가 그래프에 어떤 모델들이 있었는지에 달려 있다(미발화). 벤더 그래프일 가능성.

## 15. 비용을 아낄 때, 품질이 필요할 때 (11:15~11:48)

- ⭐ *"I would absolutely use 6.1 Terra for computer use as well as probably most like 90th percentile applications."*(11:13~11:23) · *"You're going to stretch significantly more out of your Codex budget"*(11:23~11:26)
- ⭐ *"on upper echelons of quality, you know, it doesn't really hold a candle to Opus 5.5, especially in some design applications."*(11:28~11:35)
- 맺음: *"it scored about 95 to 97% of Claude Opus 5.5 at 11% of the cost. That, ladies and gentlemen, is leverage."*(11:38~11:46)

## 등장 개체

- 인물: [[nick-saraev]](추정, 네 번째 등장) · [[greg-brockman]](화자가 그의 말을 읽음) · [[sam-altman]](Paint 데모의 그림 대상 · *"Sam Altman and co."*, 연결만) · Rohit(데모 출처, 신원 미상 — 페이지 없음)
- 조직: [[openai]]
- 모델 · 제품: [[openai-terra]] · [[claude-opus-5-5]] · [[codex]] · [[claude-code]] · GPT-6.1 Soul · GPT-5.6 Terra(그래프 비교 대상, 페이지 없음)
- 개념: [[cost-vs-score-frontier]](신규) · [[inference-speed-as-capability]] · [[true-cost-to-perfect-answer]] · [[taste-vs-judgment]] · [[model-mixing-economics]] · [[model-harness-knowledge-stack]] · [[pareto-surfing]] · [[agent-native-interface]]

## 이 위키에서의 좌표

- **같은 화자 · 같은 형식의 연속 비교 두 편째**다([[tech-bridge-nick-saraev-kimi-k3-1-vs-opus-5-5]], 10-31 업로드). 공통: 같은 규칙 문장, 싼 쪽이 약 절반 시간에 끝남, 상위 완성도는 Opus. **차이**: ① Kimi 편에서 Opus는 두 데모가 작동하지 않았지만 이번엔 **명확한 작동 실패가 없다**. ② Kimi 편의 결론이 *"double the cost (…) is it double the quality?"* 라는 **질문**이었다면, 이번엔 *"95 to 97% (…) at 11% of the cost"* 라는 **벤치마크 기반 답**으로 끝난다. ③ 비용 배수가 ×2(Kimi, 단가표)에서 ×9~12(Terra, 실사용 · 그래프)로 커졌고 화자가 그 배수를 데모마다 기준선으로 쓴다(*"definitely not 12 times better"*).
- [[tech-bridge-gpt-6-1-terra-first-look]](10-29)과 짝: 그 리뷰의 **"빠르고 싸지만 쉽게 포기한다"** 는 이번 다섯 데모에서 관찰되지 않았다 — 같은 하네스 max effort 조건, 23분 넘게 돌았다. 대신 **"일정 복잡도까지"** 라는 다른 한계가 붙는다. computer use 평가는 10-29(*decent*, Blender 실패)보다 훨씬 강하다(*"effectively solved"*) — 다만 근거가 2차다(위 10절).
- [[cost-vs-score-frontier]]: 사용자 영상이 **"비용 대비 점수" 그래프를 읽는 법**을 시청자에게 설명하고, 그 그래프로 *"leverage"* 결론을 내리는 첫 소스다. 화자 스스로 벤치마크가 *"not super valuable"* 하다 하고, 게임 품질은 *"qualitative"* 라고 한 단서와 같이 둔다.

## ⚠️ 유보

- 화자 신원은 설명란 · 태그 근거(형식 유사성은 보조), 원본 영상 · 녹화일 미상, 첫 20초 무캡션.
- 프롬프트 · 채점 기준 없음, 반복 1회로 보임, 하네스까지 묶인 비교, 평균의 표본 수 미발화.
- 시간 · 토큰 · 1/12는 화자 진술. 벤치마크 수치는 출처 미표기 그래프의 눈대중 읽기(OpenAI 자료로 추정).
- computer use 구간은 남의 데모 + Brockman 인용. *"It really is great at a lot of things…"* 의 작성자 미발화.
- ASR 판독: *"8/12"* → 1/12, *"90, I don't know, 7%"* → 97%, *"GBD"* → GPT, Agents' Last Exam 표기 미확정. ko는 04:49 · 11:42 · 10:08을 **뜻을 뒤집거나 주어 · 대상을 바꿔** 옮겨 인용하지 않았다(Opus → "작품번호" 오역도 반복).

## References

- raw: `01.raw/articles/2026-11-01_바이브 코딩 이렇게 싸도 될까 GPT-6.1 Terra vs Opus 5.5.md`
- https://www.youtube.com/watch?v=FwJ6Ae_-u4M
- 설명란 관련 자료: https://openai.com/ko-KR/index/introducing-gpt-6-1-terra/ · https://developers.openai.com/api/docs/models/gpt-6.1-terra (⚠️ 열어 보지 않았다)
