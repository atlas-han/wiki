---
title: "Tech Bridge — 알렉산더 왕이 밝힌 Muse 제작기 (한국어 해설 + Alexandr Wang 인터뷰 발췌): 일상 개인 에이전트, 행동별 eval, '80/20은 부족했다', 작은 부탁이 쌓는 신뢰"
type: source
tags: [meta, muse, muse-wonder, alexandr-wang, personal-agent, consumer-ai, coding-agents, behavior-evals, launch-threshold, launch-blocking, first-use, trust, small-requests, jolly-bot, human-confirmation, virtual-machine, openclaw, commentary-format, secondhand-claims, video]
source-url: https://www.youtube.com/watch?v=6gakvEF9m20
source-type: video
author: Tech Bridge (한국어 해설, 내레이터 미상) · 발췌 출연 Alexandr Wang([[meta|Meta]] — 이력은 해설 소개, 발췌 속 자기소개 없음) · 원본 인터뷰 진행 David Senra(**이름은 설명란에만**) · 원본 인터뷰 S6l3aRsecuE(2026-10-11, 이 위키에 없음)
date-published: 2026-10-14
ingested: 2026-10-15
created: 2026-10-15
updated: 2026-10-15
---

# Tech Bridge — 알렉산더 왕이 밝힌 Muse 제작기 (해설 + 인터뷰 발췌)

[[tech-bridge|Tech Bridge]]가 올린 **9:10, 공식 챕터 7개** 영상. 제목에 `[한영자막]` 접두어가 없고, 형식은 [[tech-bridge-lauren-tan-agent-dev-workflow]](10-03)에 이은 **두 번째 "한국어 해설 + 원본 인터뷰 발췌"** 다 — 설명란: *"원음 인터뷰는 직접 번역 자막으로, 나머지는 테크브릿지의 한국어 해설로 구성했습니다."* 원본은 David Senra와 [[alexandr-wang|Alexandr Wang]]의 인터뷰(`S6l3aRsecuE`, 2026-10-11 — 이 위키에 없고 열어 보지 않았다). **자동 자막에 잡힌 원음 발췌는 다섯 구간, 합계 약 2분**이고 나머지는 해설이다. [[muse|Muse]]의 **세 번째 소스**이자 **[[mark-zuckerberg|Zuckerberg]]가 아닌 Meta 인물의 첫 소스**다.

> **(해설의 줄거리)** Muse는 자주 고장 나던 시제품에서 시작해 일곱 달 만에 출시됐다. 경쟁이 코딩 에이전트로 쏠릴 때 팀은 일상의 개인 에이전트를 택했고, 이상적인 개인 에이전트에 필요한 행동·능력을 하나씩 eval로 쟀다. 출시 판단은 행동별 eval이 문턱을 넘는 것과 직접 써 본 감각을 함께 봤다. 사용자의 신뢰는 작은 부탁이 성공하면서 다음 부탁이 커지는 방식으로 쌓인다.

> 원음: *"Consumer AI. It's not work. It's not coding. It's personal."* (03:12~03:27) · *"specific behaviors and capabilities that we knew the model needed to have to be able to build the ideal personal agent. Like it was very, very meticulous."* (04:12~04:21) · *"We had many checkpoints that like were like green on 80 of the rows but red on 20 of the rows. We knew that wasn't good enough."* (05:31~05:36) · *"you try to give it a little thing and it does it (…) And then you give it, like, a little bit bigger of a of a problem, and it's kind of this, like, trust."* (07:17~07:37)

이 위키에 생기는 것: [[alexandr-wang]] · [[david-senra]] · [[nat-friedman]] · [[muse-wonder]](신규 제안 — 인물 셋, 모델 하나) · [[launch-blocking-evals]](신규 제안 — 행동별 eval 문턱을 출시 차단 조건으로). 기존 페이지에는 [[muse]]의 **첫 실패 서술과 첫 이용자 수(해설 전언)**, [[agent-trust-curve]]의 **소비자 쪽 사다리**, [[knowledge-agents-vs-coding-agents]]의 **소비자 쪽 반대 선택**이 붙는다.

**트랙과 인용.** 세 트랙 모두 `automatic_captions`. **ko = 원음 혼합**(해설은 한국어 ASR, 발췌는 영어 ASR 조각). **en-orig의 해설 구간은 한국어 해설의 영어 대응문**이지 원음이 아니다 — ko ASR 오류 일부는 바로잡혀 있고(*"베타"* → *"Meta"*, *"식당"* → *"diets"*) 하나는 공유하며(*"The host cannot make that judgment either"* 05:09~05:11) 하나는 챕터와 어긋난다(*"OpenAI's tools"* vs 챕터 *OpenClaw*, 01:05). `en`은 ko의 번역(Wang → **"the King"**). 이 페이지의 인용은 **모두 en-orig**이고, **해설 구간 인용은 "(해설)"로 표시**한다 — 그것은 Wang의 말이 아니다. 전체 대조는 raw.

> ⚠️ **해설과 원음을 구분해 읽어야 한다.** 자막에 잡힌 Wang(로 보이는) 음성은 다섯 구간뿐이고, **팀을 꾸린 이야기, 이사회 시연, 새 사용자 관찰, eval 표가 초록으로 바뀐 뒤 직접 써 본 감각, Jolly Bot 홍보, 카피를 직접 쓴 일, Friedman의 OpenClaw 경험은 모두 해설 전언**이다. 해설 사이 **무캡션 구간 여덟 곳**(00:22→00:47 · 01:16→01:36 · 02:32→02:56 · 03:12→03:27 · 04:39→04:56 · 05:11→05:28 · 05:57→06:19 · 06:33→06:51, en-orig 캡션 시작 간격 15초 이상; ko도 같은 자리가 비어 있다)에 원음 발췌가 있을 가능성이 크지만 **화면·음향은 확인하지 않았다.**
>
> ⚠️ **"millions of users"는 해설 전언이다.** *"In an interview about a month after its launch, Alexander Wang said Muse has millions of users."*(00:04~00:11, 해설) — **그 원음은 자막에 없다.** 설명란도 *"집계 기준과 기간은 독립적으로 확인되지 않았습니다"* 라고 단서를 단다. 원본 인터뷰 제목의 *"The Fastest-Growing AI Product Since ChatGPT"* 는 **설명란에만** 있고 자막엔 없다 — 이 위키는 채택하지 않는다.
>
> ⚠️ **인물.** Alexandr Wang — 해설이 이름을 부르고(en-orig 철자 *"Alexander"* 00:09) 이력을 소개한다(*"Wang founded Scale AI and now leads Meta's AI research organization as Chief AI Officer"* 00:11~00:17, 해설). **발췌 속 자기소개는 없다.** **David Senra는 설명란에만** — 해설은 *"The host"*(05:09)라고만 한다. Nat Friedman은 해설에만(01:01~01:02).
>
> ⚠️ **수치.** 원음에 있는 수치는 **80/20 rows 하나**(05:31~05:35) — 단위(퍼센트인지 행 수인지)·eval 구성·체크포인트 시점 미발화. *"about a month after its launch"*·*"seven months"*·*"October 12"* 는 해설. 출시일 2026-09-08은 **설명란 출처 링크 날짜에서만** 온다.

## 1. 출발점 — 고장 나던 시제품, OpenClaw의 흥분과 불안 (00:00~02:33)

- (해설) *"Meta's Muse is a personal AI agent that opens a browser to handle tasks when you ask it via message."*(00:00~00:04) · *"the starting point for Muse was a prototype that kept breaking."*(00:17~00:22) · *"How did the prototype that kept breaking become a service where people entrust their tasks just seven months later?"*(00:49~00:54)
- (해설) 출발점에 [[nat-friedman|Nat Friedman]] — *"Friedman tried OpenAI's tools early on and described the experience as a mix of excitement and anxiety. The idea of an AI that understands a person's situation and takes actual action was both compelling and unfamiliar."*(01:02~01:16) ⚠️ **"OpenAI's tools"는 챕터 00:59 *"OpenClaw에서 시작된 가능성과 불안"* 및 ko *"오픈 컬로"* 와 어긋난다 — 이 위키는 [[openclaw|OpenClaw]]로 판독한다.** Friedman 이야기의 원음은 무캡션 구간(01:16→01:36)에 있을 수 있으나 미확인.
- (해설) *"Wang says he also formed the team after trying it out himself."*(01:16~01:39) · *"Wang immediately showed the first prototype he created at that time to the board of directors."*(01:41~01:45)
- ⭐ 원음 ①: *"It's like this very fast cycle, and many of the decisions that made its way into the final Muse product were present in the first prototype. The Jolly Bot was there. You know, the early version of the Muse charm was in that first of, that very first meeting."*(01:45~02:09) — ⚠️ *"Muse charm"* 판독 보류, *"Jolly Bot"* 철자 미확정(해설은 *"Jolie Bot"* 06:24).
- (해설) *"as mentioned at the beginning, it broke more often than it worked. The seven months Wang mentioned were the time spent transforming this prototype into a product people actually use."*(02:19~02:27)

> ⚠️ **원음과 해설의 강조가 다르다.** 해설·제목은 *고장* 을 앞세우지만, 원음 ①은 **첫 시제품에 최종 결정 다수가 이미 있었다**는 연속성을 말한다. "고장이 잦았다"는 원음은 자막에 없다.

## 2. 코딩 에이전트 대신 개인 에이전트 (02:34~04:04)

- (해설) *"To Wang's eyes, the competition at the time was leaning toward coding agents. He set the starting point of the Muse app as a personal agent that integrates into daily life. Meta was already reaching people through Instagram and WhatsApp."*(02:32~03:06)
- ⭐ 원음 ②: *"Consumer AI. It's not work. It's not coding. It's personal. Yeah, exactly. Personal agents and personal and consumer AI. Always."*(03:12~03:34) — ⚠️ *"Yeah, exactly"* 로 보아 **진행자와 Wang의 말이 섞였을 수 있다** — 어느 문장이 누구 것인지 자막으로 가를 수 없다.
- (해설 — Meta 공식 제품 소개 요약) 인스타그램에 저장한 요리 영상 → 장보기 목록, *"even considering the diets of the people you're eating with"*(03:48~03:51) · *"Muse also operates in the browser based on requests received in Messenger"*(03:54~03:56). ⚠️ ko는 *식단* 을 **"식당"** 으로 바꾼다.

→ [[knowledge-agents-vs-coding-agents]] · [[personal-superintelligence]]

## 3. 행동별 eval과 출시 문턱 (04:05~05:57)

- (해설) *"To connect these small tasks seamlessly, one must verify what actions the agent can perform one by one."*(03:56~04:03)
- ⭐ 원음 ③: *"But more like specific behaviors and capabilities that we knew the model needed to have to be able to build the ideal personal agent. Like it was very, very meticulous."*(04:03~04:21) — 발췌가 *"But more like"* 로 시작해 **무엇과 대비하는지는 자막에 없다**(편집으로 잘렸을 수 있다). ⚠️ ko 트랙에만 이어지는 영어 조각(*"and then over time we buil evs for all those…"* 04:22~04:28)이 있으나 **en-orig에 없어 이 위키는 쓰지 않는다.**
- (해설) 첫 사용 관찰: *"What does someone try first after downloading the app? Wang says he watched new users interact with Muse many times."*(04:32~04:39) · *"It’s a flow of thinking of what to tell the agent, checking the results, and assigning the next task."*(04:56~05:03) — 원음은 무캡션 구간(04:39→04:56)에 있을 수 있으나 미확인.
- ⭐ 원음 ④ (출시 문턱): *"Threshold is launch blocking above what threshold is good. We had many checkpoints that like were like green on 80 of the rows but red on 20 of the rows. We knew that wasn't good enough."*(05:11~05:36)
- (해설) *"Wang mentions that after the evaluation charts turned green, he felt it had improved through his own use. The decision to launch was based on both behavior-based evaluation and personal experience."*(05:36~05:52) — ⚠️ "직접 써 본 감각"은 **해설 전언**이다.

> **읽기.** 원음 ③·④만으로 확인되는 구조: (a) 이상적 개인 에이전트에 필요한 **행동·능력 목록**을 먼저 정하고 (b) 그것을 **행(row) 단위로 초록/빨강 판정**하는 표로 체크포인트를 쟀으며 (c) **대부분 초록이어도 빨강이 남으면 출시를 막았다**(*"launch blocking"*). 문턱이 몇이었는지, 행이 몇 개였는지, 마지막에 전부 초록이었는지는 **말하지 않는다.** → [[launch-blocking-evals]](신규) · [[taste-encoded-evals]](eval + 사람 감각의 겹 판정)

## 4. 관심을 얻고 신뢰를 쌓기 (05:58~08:03)

- (해설) *"Wang jumped directly into the work of promoting the product himself. He explains that he made the character Jolie Bot visible when people share their Muse screens. It was a choice intended to make people remember the product’s name. He was so immersed in this task that he even wrote the copy himself."*(05:57~06:33) — 원음은 무캡션 구간(05:57→06:19, 06:33→06:51)에 있을 수 있으나 미확인. → [[agent-persona-naming]](Zuckerberg 편의 Agrippa·Pip에 이은 **제품 단위 캐릭터**)
- (해설) *"Wang explains that the result changes the scale of the next request."*(06:52~06:56)
- ⭐ 원음 ⑤: *"you try to give it a little thing and it does it, like Oh wow, it did that! And then you try to give it a little bit something, like a little bit more, and then it does it, and you're like, Oh wow, can do that! It could do that first thing and do the second thing. And then you give it, like, a little bit bigger of a of a problem, and it's kind of this, like, trust."*(07:17~07:37) — 앞의 *"On their cycle, that people who who really love the app and, and we even, like we back in February had...which is"*(07:00~07:19)는 잘려 뜻이 이어지지 않는다(2월에 무엇이 있었는지 미상).
- (해설 — Meta 공식 소개 요약) *"For small requests to build up, the user must retain the power to decide. Meta introduces that Muse is designed to use a browser on a separate virtual machine and ask for user confirmation before sending emails or making purchases. It is a structure where users also define the access permissions for required apps."*(07:37~07:57)

→ [[agent-trust-curve]] · [[least-privilege-connectors]] · [[goal-level-delegation]]

## 5. Muse Wonder (08:04~08:33, 해설 — Meta 공식 자료)

- *"The day after this interview was released, on October 12, Meta announced a new model, Muse Wonder. It is a model that handles personal agent tasks while also assisting with coding projects. Developers can now use Wonder in the Meta model API and Muse Code, and Wonder Full is provided to Muse Code subscribers. Meta has announced that Wonder is scheduled to be included in the Muse app as well in the future."*(08:05~08:28)
- ⚠️ **Wang의 발화가 아니다** — 설명란도 *"인터뷰 공개 다음 날의 별도 공식 자료"* 라고 구분한다. 벤치마크·가격·[[muse-spark|Muse Spark]]와의 관계 **없음**. *"Muse Code"* 는 이 위키에 처음 나오는 제품명이다(설명 없음). → [[muse-wonder]](신규)

## 6. 맺음 — 작은 부탁에서 시작 (08:34~09:10, 해설)

- *"They set the direction for an everyday agent, evaluated necessary actions one by one, and observed the product in the hands of first-time users."*(08:43~08:51) · *"whether you entrust the next task to the Muse app is determined by the experience of having completed smaller tasks beforehand."*(08:55~09:02)

## 이 위키와의 연결

### 이어지는 것

- **[[muse]] — 첫 실패 서술, 첫 출시 문턱.** 기존 두 편(Zuckerberg)은 *"두 편 합쳐도 실패·오작동 사례가 0건"* 이었다. 이 편은 **고장 나던 시제품**(해설)과 **80/20에서 출시를 막았다**(원음 ④)를 준다 — 둘 다 *과거의* 실패이고 출시 후 실패는 여전히 없다.
- **[[muse]] — 첫 이용자 수, 그러나 2차 전언.** 기존 페이지의 *"사용자 수·가격·성능 수치가 하나도 없다"* 에 **"millions"(해설 전언, 원음 없음, 집계 기준 미확인)** 가 붙는다.
- **[[agent-trust-curve]] — 소비자 쪽 사다리.** [[lauren-tan|Lauren Tan]]의 곡선이 *병렬 에이전트 수* 를, [[jensen-huang|Huang]]이 *권한의 경계* 를 늘렸다면, Wang의 원음 ⑤는 **부탁의 크기**를 늘린다 — *little thing → a little bit more → a little bit bigger of a problem → trust*. 승급 조건은 Lauren 쪽(관찰된 성공)에 가깝다.
- **[[least-privilege-connectors]] · [[muse]]의 보안 층** — 해설이 요약한 Meta 공식 소개(별도 VM의 브라우저, 이메일 발송·구매 전 확인, 앱 접근 권한은 사용자가 정함)는 Zuckerberg 편의 *"로그인·결제·민감 정보 전송은 매번 승인"*·*"이메일은 읽기 전용으로 시작"* 과 **어긋나지 않는다.** 다만 이 편의 서술은 **Meta 자료의 2차 요약**이다.
- **[[taste-encoded-evals]]** — 출시 판단 = 행동별 eval + 직접 써 본 감각(해설). eval 표 위에 **제작자의 사용감**을 한 겹 더 두는 구조는 그 페이지의 *세 겹의 판정* 과 같은 방향이다. ⚠️ 감각 쪽은 해설 전언.
- **[[agent-org-adoption]]의 "도입 문제" 절** — Zuckerberg 편이 *"뭘 해야 할지 모른다"* 를 문제로 올렸다면, 이 편은 그 답을 **새 사용자의 첫 사용을 반복 관찰**하는 제품 절차로 준다(해설 04:32~05:05).

### 갈리는 것

> ⚠️ **Contradiction(약): "코딩이 아니다" vs "결국 코딩으로 환원된다".** 원음 ②는 *"It's not work. It's not coding. It's personal."*(03:12~03:27)이고 해설은 *경쟁이 코딩 에이전트로 쏠릴 때 개인 에이전트를 택했다* 고 정리한다. 반면 [[muse]]에 기록된 Zuckerberg는 *"개인 에이전트에서 말하는 것 상당수가 결국 코딩으로 환원된다"* 고 했고, 이 영상의 마지막 절에서 Meta는 **코딩도 돕는 Muse Wonder와 Muse Code**를 내놓는다(해설 08:09~08:23). 둘은 층이 다를 수 있다 — Wang의 말은 **제품 포지셔닝(누구에게 무엇으로 보이는가)**, Zuckerberg의 말은 **필요한 모델 능력**. 화자들은 이 차이를 말하지 않는다(위키의 관찰). 원음 ②의 어느 문장이 Wang 것인지도 확정되지 않았다.

> ⚠️ **긴장: 출시 판단의 근거.** 원음 ④는 **eval 문턱**(*"launch blocking"*)을, 해설은 거기에 **직접 써 본 감각**을 더한다. 둘이 충돌한 경우(eval은 초록인데 써 보니 나쁘거나 그 반대) 어떻게 했는지는 자막에 없다.

## 해소하지 않고 표시만 한 것

- 무캡션 구간 여덟 곳의 내용 — 이용자 수 발화, Friedman의 OpenClaw 경험, 팀 구성, 새 사용자 관찰, 홍보·카피 이야기의 원음.
- 원음 ②의 화자 구분, 원음 ⑤의 *"back in February"* 가 가리키는 것, *"Muse charm"*.
- 80/20의 단위, eval 행의 수와 구성, 최종 출시 체크포인트의 점수.
- *"The host cannot make that judgment either"*(05:09~05:11)의 원 한국어(진행자가 *묻는다* 는 뜻일 가능성).
- Friedman이 써 본 것이 OpenClaw인지(챕터·ko) "OpenAI's tools"인지(en-orig) — 챕터 기준으로 판독.
- Muse Wonder와 Muse Spark의 관계, Muse Code의 정체, Wonder Full의 차이.
- Wang의 직함·조직이 [[meta-superintelligence-labs|MSL]]과 같은지 — 해설은 *"Meta's AI research organization"* 이라고만 한다.
- 출시일(2026-09-08)·Wonder 발표일은 설명란 링크와 해설에만 — 이 위키는 Meta 자료를 열어 보지 않았다.

## 등장 개체

- 인물: [[alexandr-wang|Alexandr Wang]](신규 제안 — 이름은 해설·설명란, 발췌 속 자기소개 없음) · [[david-senra|David Senra]](신규 제안 — **이름은 설명란에만**) · [[nat-friedman|Nat Friedman]](신규 제안 — 해설에만) · [[mark-zuckerberg]](이 편엔 등장하지 않음, 비교 대상)
- 조직: [[meta|Meta]] · Scale AI(해설 소개만 — 페이지 없음) · [[meta-superintelligence-labs]](⚠️ 이름 미발화)
- 제품·모델: [[muse|Muse]] · [[muse-wonder|Muse Wonder]](신규 제안) · Wonder Full · Muse Code · Meta model API(모두 해설만) · [[muse-spark]](비교) · [[openclaw|OpenClaw]](⚠️ 챕터·ko 판독) · Jolly Bot(캐릭터 — [[muse]]에 기록 제안) · Instagram · WhatsApp · Messenger
- 개념: [[launch-blocking-evals]](신규 제안) · [[agent-trust-curve]] · [[knowledge-agents-vs-coding-agents]] · [[personal-superintelligence]] · [[taste-encoded-evals]] · [[least-privilege-connectors]] · [[goal-level-delegation]] · [[agent-persona-naming]] · [[agent-org-adoption]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=6gakvEF9m20> (9:10, `upload_date` 2026-10-14)
- raw: `01.raw/articles/2026-10-14_알렉산더 왕이 밝힌 Muse 제작기 - 고장 나던 AI는 어떻게 출시됐나.md`
- 설명란 출처(⚠️ 열어 보지 않았다): 원본 인터뷰 <https://www.youtube.com/watch?v=S6l3aRsecuE> · <https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/> · <https://www.meta.com/about/leadership/alexandr-wang/> · <https://about.fb.com/news/2026/10/introducing-muse-wonder-models/>
- 같은 제품의 다른 소스: [[tech-bridge-zuckerberg-muse-personal-agent]] · [[tech-bridge-zuckerberg-muse-in-daily-use]]
- 같은 형식(해설 + 발췌)의 선례: [[tech-bridge-lauren-tan-agent-dev-workflow]]
- [[tech-bridge]] · [[muse]] · [[meta]] · [[alexandr-wang]]
