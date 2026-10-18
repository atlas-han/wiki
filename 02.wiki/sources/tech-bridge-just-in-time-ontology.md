---
title: "Tech Bridge — 적시형 온톨로지 (Hrishi Olickel · Southbridge): 보편 스키마는 없다, 결정의 순간에 병합하고 근거와 함께 재사용하라 — 그리고 Jev를 넣은 오하이오 entity resolution $10,000 → $795"
type: source
tags: [just-in-time-ontology, ontology, universal-schema, data-transformation, entity-resolution, campaign-finance, model-priors, silent-data-errors, cross-model-prior-intersection, correlated-errors, decision-models, system-1-model, model-roles, model-mixing, pareto-surfing, self-optimizing-pipelines, failure-surface, bounded-experiments, budget-enforcement, verification-cost, harness, hankweave, jev, vendor-pitch, video]
source-url: https://www.youtube.com/watch?v=8uG4ZY7G2r8
source-type: video
author: Tech Bridge (한영자막 재배포) · 발표 Hrishi Olickel([[southbridge|Southbridge]] 창업자 — ⚠️ **이름은 설명란에만**, 회사명은 자막에서 발화) · 행사명 미발화 · 녹화일 미발화
date-published: 2026-10-17
ingested: 2026-10-18
created: 2026-10-18
updated: 2026-10-18
---

# Tech Bridge — 적시형 온톨로지 (Hrishi Olickel · Southbridge)

[[tech-bridge|Tech Bridge]]가 재배포한 **20:54 단독 발표**다. Q&A는 없다. 공식 챕터는 `meta.txt` 기준 10개다. 화자는 자막에서 이름을 말하지 않는다. 이름 [[hrishi-olickel|Hrishi Olickel]]은 설명란에서 왔다. 회사는 직접 말한다: *"I talked about a single universal schema when I founded Southbridge 2 years ago."*(01:56~02:01) 발표는 **자기 철회(보편 스키마) + 스키마 넷 + 모델의 세 역할 + Jev 사례 수치 + prior 오류 + 자기 최적화 조건 넷**으로 이루어진다. 테제는 다음과 같다.

> **데이터 인프라는 변환이 비싸다는 전제 위에 섰는데, 판단(judgment)이 Pareto frontier 전 구간에서 싸졌다. 보편 스키마는 없다. 데이터에는 출처(source)·저장(storage)·결정(decision)의 스키마와 모델이 가져오는 prior까지 넷이 있고, 넷을 동시에 아는 것은 결정의 순간뿐이다. 그 순간에 병합하는 것이 just-in-time ontology다. 그렇게 만든 온톨로지는 근거(receipts)와 함께 남겨 다음 일에 재사용한다. 모델은 파이프라인에서 설계자·작업자·hill climber 세 역할을 맡는다. 안정된 배포 표면·제한된 실험·노하우·failure surface가 갖춰지면 파이프라인은 비용·속도·정확도를 스스로 최적화한다.**

> *"All of our data infrastructure today is built on the idea that transformation is expensive. What if that wasn't true anymore?"* (00:26~00:35) · *"This is why I was wrong. There is no universal schema."* (04:33~04:37) · *"Doing that merge when the decision space is known instead of ahead of time is what I mean by a just-in-time ontology."* (04:54~05:03) · *"It's built when the job needs it, kept with its receipts, and reused when the next job needs the same thing."* (20:03~20:10)

이 위키에 개념 셋이 생긴다(모두 신규 제안).
- [[just-in-time-ontology]]: 스키마 넷, 결정 시점 병합, receipts와 재사용. 위키에 "온톨로지"를 정면으로 다룬 페이지가 없었다.
- [[cross-model-prior-intersection]]: 모델의 prior가 만드는 조용한 데이터 오류와, 계열이 다른 모델의 일치·불일치로 오류 면을 줄이는 기법. 그리고 그것으로도 못 잡는 "종 수준" 공통 오류.
- [[pareto-surfing]]: 자기 최적화 파이프라인의 조건 넷과 단계 여섯. 기준선을 잡고 모델·부품을 싸고 빠른 것으로 바꾸며 frontier를 민다.

나머지는 기존 페이지에 붙는 **새 증언**이다.
- [[jev]]·[[system-1-model]]: **이 위키 첫 Jev 프로덕션 규모 사용 보고**(90,000 호출). 첫 실패 양상(*confidently said no*)과 그 처방(임계값이 아니라 질문의 정의를 고친다)
- [[model-mixing-economics]]: 설계자(*"Opus or up"*) vs 작업자(싸고 빠르고 전문화된) vs hill climber의 세 역할
- [[verification-cost-asymmetry]]·[[verification-bottleneck]]: 검증에 든 돈이 첫 답의 약 4배
- [[fixed-budget-alpha]]: 미리 정한 $800 예산 안에서 $795
- [[self-harness]]: 에이전트가 10일 동안 아키텍처 십수 개를 스스로 시도
- [[harness-as-platform]]: Claude Code·Pi 같은 *"fast-moving surface"* 위에 안정된 하네스 층(Hank Weave)
- [[verifiable-goals]]: failure surface를 시작 전에 정한다

ASR·ko 보정. ko는 **결론 넷을 뒤집는다.** *there is no super schema* → **"그러한 초거대 계획이 존재한다"**(02:28), *Today though, it is worse* → **"그렇지 않습니다"**(08:03), *went from no … to yes* → **"아니라고 … 아니라고"**(11:41), *you can solve this just by not vibing* → **"해결할 수 없습니다"**(15:13)다. 핵심 정의도 무너진다. *instead of ahead of time*이 **"고급"**(05:00)이 되어 just-in-time ontology의 정의가 사라진다. 단위도 바뀐다: $545·$128 → **"545건·128건"**(12:28~12:33), 10 days → **"10년"**(12:59), *agreed on 194* → **"194년에 만났습니다"**(15:52). schema는 내내 **"계획"**이고, runs는 **"사형 집행"**(14:49), sign(부호)은 **"표지판"**(14:54), pilots는 **"조종사"**(19:01), frontier는 **"국경"**(19:43)이다. en-orig는 Jev를 *"Jeff"*로 섞어 적고, Pareto surfing을 *"Pareto serving"*으로 적는다(판독). 전체 목록은 raw에 있다.

> ⚠️ **모든 수치는 화자 자기 보고다.** $10,000 예상 → $795(예산 $800), 10일, 203,317 케이스, 실행 4,000회 이상, Jev 호출 90,000회, 약 60억 토큰, 200 held-out families 중 194 일치는 모두 발표에서 나왔다. 데이터셋을 *"download it for yourself"*(10:53)할 수 있다고 하지만 위치는 발화되지 않고 이 위키는 확인하지 않았다. 비용 내역 $545 + $128 = $673이고 총액 $795와의 차이 $122는 설명되지 않는다.
>
> ⚠️ **자사 하네스 소개가 섞인다.** Hank Weave는 *"our open-source harness for data work"*(07:03~07:06)이고, *"for headless data work, Hank Weave, I would say, is still the oldest, most stable, and the most open."*(17:09~17:15)라고 한다. 비교 대상의 이름은 없다. 정식 표기는 자막만으로 확정하지 않는다(*Hank Wave*·*Hank Weave*).
>
> ⚠️ **Jev는 제3자 사용자의 보고다.** 화자는 [[typesafe-ai|TypeSafe]] 소속이 아니다(발화 기준). 이 위키의 Jev 서술은 TypeSafe 본인·파트너(LangChain)·TypeSafe 자료를 재진술한 IBM 해설·사용자 언급 위주였다. 이 발표는 **수치가 붙은 첫 외부 프로덕션 사용 보고**다. 다만 Jev 출시 시점의 사용이라는 것(*"Jev launched on a Tuesday when we were deep into an entity resolution pipeline"* 10:36~10:42)과 화자가 Jev에 우호적이라는 것은 감안해야 한다.
>
> ⚠️ **행사와 시점.** 행사명·도시·날짜는 발화되지 않고 설명란에도 행사 링크가 없다. 시점 단서는 Jev 출시 직후 10일이다(01:31, 13:01).

## 1. 도입 — 변환이 싸지면 (00:00~01:41)

- 출발점은 DuckDB의 Hannes가 쓴 글이다: *"he asks if we lost a decade chasing distributed architectures that presumed compute and storage were slow and expensive."*(00:01~00:08) ⚠️ 글 제목·링크는 발화되지 않고 이 위키는 확인하지 않았다.
- *"Capability in every era, though, defines architecture and tooling, and the tooling lags behind consistently."*(00:10~00:15)
- ⭐ *"All of our data infrastructure today is built on the idea that transformation is expensive. What if that wasn't true anymore? I believe we've solved the final bottleneck in transformation, general intelligence or judgment, and we've made it accessible on tap all along the Pareto frontier."*(00:26~00:47)
- 예고한 순서: *"why single ontologies always fail, the three roles models play in pipelines, intersecting model priors for better results, and Pareto serving[=surfing]"*(00:50~01:01)
- 사례 예고: Jev가 나왔을 때 이미 돌던 오하이오 선거자금 entity resolution 파이프라인(*"whether they belong to the same person, company, or committee"* 01:14~01:19)은 약 $10,000로 예상됐다. *"Our systems took that new model, worked out where it fit, tested over a dozen approaches, and integrated it. 10 days after that first call, we had final ground truth for every donor case in Ohio under $800."*(01:23~01:36)

→ [[intelligence-abundance]](변환 비용 측면의 풍요) · [[jev]] · [[model-mixing-economics]](Pareto frontier)

## 2. 보편 스키마는 없다 — 스키마 넷 (01:47~04:31)

- *"Ontologies are the enterprise version of mind maps. It's this carpet[=?] that sucks us all in, including me."*(01:47~01:55)
- 흔한 설명(buy-in 부족, 중도 포기)은 *"100%"* 맞지만 주된 이유가 아니다(02:01~02:18). ⭐ *"Say if you could integrate and migrate all of your information into a single super schema in the blink of an eye, you still have to contend with the truth that there is no super schema. There actually are four schemas."*(02:18~02:32)

| 스키마 | 발화 (온도를 적어 달라는 예) |
|---|---|
| **source** | *"whatever you have access to"* — 휴대폰의 지역 온도, 책상 센서(덜 정확하지만 더 국지적), 시계. *"even your patience in following through on my request"*(02:41~02:54) |
| **storage** | *"There's only so much you can write down."* 기기 펌웨어도, 초 단위 시각도 못 적는다(02:56~03:13) |
| **decision** | *"Why do I need you to write the temperature down?"* 쾌적함을 알려면 하루 종일 같은 사람의 측정이, 기상 이동 지도라면 정확한 위치·시각·기기가, 민감 장비 설치라면 측정자 자신이 상쇄할 변수가 된다(03:14~03:47) |
| **prior** (넷째) | *"which we'll get to when we talk about priors. It's a recent addition."*(03:48~03:52) → 13:57 *"the one the model brings with it"* |

- ⭐ *"The true problem is that you will never know all four schemas at the same time except at the moment that the decision is being made."*(03:53~04:00) *"most of the data being recorded has little idea of what it's going to be used for."*(04:02~04:06)
- 고객 예: *"To building[=billing], a customer is whoever pays. To support, it's whoever calls. To compliance, it's whoever we're on the hook for."*(04:12~04:19) 결정(환불할까? 신용 한도를 늘릴까?)이 정해지면 *"what you need to know, how and to what degree, becomes extremely clear."*(04:21~04:30)

→ [[just-in-time-ontology]](신규) · [[multimodal-elicitation]](질의 시점에 제약 → 온톨로지 연결을 *"임시로"* 만든다는 같은 방향)

## 3. Just-in-time ontology의 정의 (04:33~05:03)

- ⭐ *"This is why I was wrong. There is no universal schema. There is no concept of a customer that's divorced from the question that you want to answer."*(04:33~04:42)
- *"pulling these schemas together is the process of transformation, of making information actually useful. Taking the context that it was recorded in and merging it with the context of the decision. And that takes discernment."*(04:42~04:56)
- ⭐ *"Doing that merge when the decision space is known instead of ahead of time is what I mean by a just-in-time ontology."*(04:55~05:03)
- 정의의 나머지 절반은 끝(19:53~20:10)에 나온다. 아래 9절.

→ [[just-in-time-ontology]]

## 4. 회사와 세 가지 작업 체제 (05:14~07:25)

- *"We are best described as obsessives. Obsessives who embed intelligence into pipelines."*(05:16~05:22). 파이프라인은 *"can mature in cost, performance, and speed all on their own"*(05:29~05:31)
- 체제 셋: ① **write once, run once** — *"monster scale immediately invoked functions"*(05:43~05:46), 데이터셋 조인·정보 채굴·한 질문 답하기 뒤 철거 ② **write many, run once** — 대형 마이그레이션처럼 *"Lots of workloads built for one rule and verified individually at source"*(06:09~06:14) ③ **write many, run many** — *"bread and butter"*, 정보를 더하며 유지되는 반복 파이프라인(06:18~06:29)
- *"Almost everything we do in the modern world is a transformation of data, or it's bottlenecked by how hard it is to transform data. And in all of these cases, our job is simple. Make sure people can rely on the results."*(06:40~06:53)
- 이력: *"early 3.5 turbo level models"*를 헬스케어 등에서 믿을 만하게 만드는 일에서 *"Hank Wave, our open-source harness for data work"*, 그리고 *"terabyte scale"*로(06:53~07:10)
- ⭐ *"Today, we have systems that can self-optimize. You give them the problem, a way to fail safely, a place to work, and they find the shape of the solution. They pick the right models, they run the pilots, they scale up, and they Pareto surf their way to the best option they can find."*(07:10~07:25)

→ [[southbridge]](신규) · [[pareto-surfing]](신규) · [[deterministic-agent-pipeline]]

## 5. 숫자가 존재하는 순간 — 그리고 에이전트는 언제나 답한다 (07:29~08:22)

- 이전 직장(*"thousands of vessels on the platform"* 07:40~07:41, 회사명 미발화)에서 가장 많이 들은 질문은 *"Can we make this decision data-led?"*였다. 50명 사용자로 A/B 테스트를 하면 *"Not because you're not going to get a result, but because you will."*(07:51~07:56)
- ⭐ *"the only real option was to do not produce a number at all because the moment a number exists, it argues for a result."*(07:56~08:04)
- *"Today though, it is worse. Interactive agents will always give you an answer. They'll give it to you quickly. (…) you get a confident yes, sir. What this means is mistakes add up quickly. Moment in chat can be a prod nightmare forever just waiting to be discovered."*(08:05~08:22)

→ [[ai-slop]] · [[verification-bottleneck]] · [[model-calibration]](자신 있는 답이 근거가 되는 문제)

## 6. 모델의 세 역할 (08:23~10:31)

*"intelligence, as it relates to data work today, occupies three separate roles that coding agents kind of mash into one context window."*(08:25~08:34)

| 역할 | 하는 일 | 원하는 모델 |
|---|---|---|
| **설계** | *"breaking down the problem, writing the early specs, authorizing spend"*(08:43~08:48) | *"slower models with heavier, thicker tokens. Models that can think more (…) predict how something will do before it even starts, right? Opus or up."*(09:07~09:22) |
| **작업** | *"Reading the PDF, writing to databases, checking results."*(08:56~09:00) — *"usually confused with the first and given to the same models"*(08:50~08:54) | *"cheaper, faster, specialized, good at following instructions, repeatable workers with noble[=known] defects."*(09:28~09:33) |
| **hill climber** | *"Models that can take a first one and self-optimize. (…) they can try new things, vary budgets to limit cost exposure, debug quickly, take notes, surf their way, not just to the right solution, but the optimal one."*(10:09~10:27) | 조건: *"the right knowledge, instructions, and an incredibly stable surface to stand on"*(10:14~10:18) |

- 비유: 잎꾼개미 군집은 *"four different sizes of worker, right? Small, medium, high, extra high."*(09:34~09:42). ⚠️ high·extra high는 추론 effort 등급명을 빌린 말장난으로 보인다(위키 판독).
- ⭐ *"Because we had this distinction, bringing in Jev in this newly exploding class of decision models was very easy, cuz they're workers. They're built for quick contact with information, and they're deployed at the bottom end of large workloads."*(09:51~10:04)
- *"We call that Pareto surfing."*(10:29~10:30)

→ [[model-mixing-economics]](계획 vs 실행 분할에 셋째 역할을 더한다) · [[system-1-model]](decision model = 작업자 층) · [[self-harness]](hill climber)

## 7. Jev 사례 — 오하이오 entity resolution (10:33~13:43)

### 설계 셋과 정의 고쳐 쓰기

- *"Here are all of the architectures we tried. We started with three designs on a small development set. A cheap reasoning model on its own, Jev with a reasoning model for anything it wasn't sure about, and a reasoning model proposing answers with Jev checking them."*(11:02~11:18)
- *"On about 200 held out families, the cheap reasoning model on its own did as well as Fable for about 2% of the cost."*(11:18~11:26) ⚠️ cheap reasoning model의 이름과 [[fable-5-1|Fable]]의 버전은 발화되지 않는다.
- ⭐ *"Jev first got the core answers right, but it missed nine household links because it had confidently said no to every one of them. So, we rewrote the questions. Without touching the models of[=or] the thresholds, the household question now said what counts as enough evidence, and Jeff[=Jev] went from no on all 13 development questions to yes."*(11:26~11:45)
- *"we ran over a dozen rounds of such qualification. Each round fixed a definition, what a committee is, what a filer means, when two people live at one address, what does that mean."*(11:47~11:57)
- ⭐ *"Every one of Ohio's 203,317 cases now has a label that says what the answer rests on, and how far it was checked."*(11:57~12:07)

### 돈이 간 곳

| 항목 | 발화 |
|---|---|
| 총액 | *"$795 on an $800 budget that was set ahead of time"*(12:19~12:25) |
| 검증 | *"Checking cost about four times as much as doing, 545 on second opinions, settling disagreements, and the audit"*(12:26~12:33) |
| 첫 답 | *"against 128 for first answers"*(12:33~12:36) |
| 이전 예상 | *"Before Jeff[=Jev], we expected this work to cost about $10,000."*(12:36~12:40) |
| 다음 주 | *"we expect the audit budget for the next state to be close to zero."*(12:40~12:45) ⚠️ 예측 |

⚠️ $545 + $128 = $673. 총액 $795와의 차이 $122는 발화되지 않는다(개발 세트·파일럿 비용일 수 있다).

### 에이전트가 스스로 찾았다

- ⭐ *"The most amazing thing is that our agent 4A[=?], running on Astra and then later on Opus, found most of these approaches incrementally on its own. By building the system, running it, debugging it, and trying new things."*(12:46~13:00) → [[openai-astra|Astra]]
- *"It ran for 10 days, tried over a dozen architectures, its hangs[=hanks?] ran for more than 4,000 times, alongside 90,000 calls to Jeff[=Jev], tried practically every model on the Pareto frontier, and the models inside those runs went through roughly 6 billion tokens."*(13:01~13:16)
- 배운 것은 부품 라이브러리로 되돌린다: *"we wrote what we learned back into our library of gigantic parts[=?]. This work leaned on these existing ones, and we're adding new tested ones like the checking letter[=?]."*(13:18~13:28)
- *"every single one of these iterations was a version controlled Hank. They were easy to revert, understand, debug, and critique."*(13:35~13:43)

→ [[jev]] · [[system-1-model]] · [[verification-cost-asymmetry]] · [[fixed-budget-alpha]] · [[self-harness]] · [[action-reversibility]](버전 관리된 반복 = 되돌릴 수 있는 실험)

## 8. Prior — 모델이 가져오는 넷째 스키마 (13:43~16:40)

- *"So, can models do this natively now? Not quite. They're missing four things (…) And there's something that doesn't go away though as models get bigger and more capable, the prior."*(13:43~13:57)
- ⭐ *"Just like humans, models bring their own priors, their beliefs about what should be in the world to every task. This is the fourth schema that I mentioned before, the one the model brings with it."*(13:57~14:07)
- *"Bigger models, in a strange way, are worse at this sometimes. They hold onto their beliefs and argue for them even more vehemently."*(14:10~14:16)

### 조용한 오류 셋

| 사례 | 발화 | 결과 |
|---|---|---|
| in-kind 표기 | *"One pipeline looked for in-kind spelled with an underscore. The file spelled with a capital I and a hyphen."*(14:20~14:27) | *"the model counted 15,658 in-kind contributions as ordinary money, didn't double-check. The loan payment repayments also disappeared the same way."*(14:26~14:36) |
| 날짜 형식 | *"Another one tried four date formats when the file used the fifth."*(14:37~14:41) | *"99.4% of the transaction dates then came out empty, and every row count and dollar so[=sum] matched, so the agent moved on."*(14:42~14:50) |
| 대출 부호 | *"Several runs noticed that loan amounts were negative, decided that the sign was redundant, and stored the absolute value."*(14:50~14:58) | ⭐ *"And net of 784,000 became $5.3 million of debt in the end, validated by multiple models."*(14:58~15:05) |

- *"this is quickly becoming the largest class of error I see across companies at Data Work as models take over."*(15:07~15:12)
- 처방 1, 사람: *"Sometimes you can solve this just by not vibing, by checking results and applying human intuition. And what you're actually doing there (…) You're intersecting your priors with the models."*(15:12~15:25) 그러나 *"humans (…) are expensive. They are slow, they pause timelines, they're even more non-deterministic than models, and they hate interruptions."*(15:32~15:44)
- 처방 2, 모델: ⭐ *"it turns out you can also get really far with cross-model prior intersection. On our 200 held-out families, Jev and Luna agreed on 194. And none of those shared answers was wrong. Every error sat in the six families where they disagree."*(15:45~16:01)
- *"Models from different families, different pedigrees, tend to disagree more and have different priors than models in the same group. For example, the exception, I'm not going to say who, are models that are distilled outside the same company."*(16:01~16:15) ⚠️ 마지막 문장은 판독 보류. 증류 관계를 암시하지만 누구인지 말하지 않는다.
- 한계: ⭐ *"you can shrink the surface quite a bit, and the errors along with it down to a much smaller but persistent class of problems that apply to LLMs as a species. So, in one benchmark, four different model families produced the same total down to the cent because they all shared a sign convention that the answer key didn't."*(16:15~16:34) *"the only way forward is to list them, look out for them, and apply specific solutions."*(16:36~16:40)
- ⚠️ *"Luna"*는 모델 이름으로 읽히지만 이 위키에 페이지가 없다. [[tech-bridge-altman-devday-dots]]에도 *"Luna(⚠️ 미판독 모델명)"*가 OpenAI 쪽 맥락으로 나왔다. 같은 것인지는 확인하지 않는다.

→ [[cross-model-prior-intersection]](신규) · [[generator-evaluator-pattern]](평가자가 같은 prior를 공유하면 무력하다) · [[cross-lab-peer-review]](랩 간 검증의 다른 층) · [[model-calibration]]

## 9. 자기 최적화의 조건 넷과 단계 여섯 (16:42~20:11)

### 조건 넷

| # | 조건 | 발화 |
|---|---|---|
| 1 | **stable deployment surface** | *"We use Hank Weave for this, a harness that takes the fast-moving surface of agent runtimes like Cloud Code[=Claude Code] and Pi, and then exposes a consistent, well-tested log and API interface with checkpointing, rollback, budget enforcement, everything built in."*(16:50~17:04) |
| 2 | **bounded experiments** | *"You can't test unless you can control cost, time, and access as resources."*(17:20~17:25) |
| 3 | **know-how·methodology** | *"this new class of models can take everything we've learned from two years of deployment, agentic patterns, debugging techniques, prompting, and apply it to complex problems. With the right abstraction layer, you can express it very token efficiently"*(17:30~17:44) |
| 4 | ⭐ **failure surface** | *"The fourth and the most important one is a failure surface. Archimedes said, 'Give me a place to stand, and I will move the earth.' (…) we haven't met a problem or a constraint that we couldn't iterate ourselves to solving given a stable stack to build on and a failure surface to iterate against."*(17:46~18:02) |

- *"That last one has been the hardest to put into words and into tooling and instructions that helps models get there. The current best models are still only barely good at this, sparks of intelligence, so to speak."*(18:02~18:15)

### 단계 여섯

화자는 *"six stages"*(18:16~18:17)라고 한다. 아래 번호 경계(4와 5)는 위키의 판독이다.

1. **명세와 분할** — *"For Jeff[=Jev], that means splitting some 800,000 rows into 200,000 smaller, specialized cases, and each of those cases into typed questions."*(18:21~18:30)
2. **failure surface 정하기** — *"we ran good models on a small slice of the data, with some of it being manually checked, to set a baseline that we can fail against."*(18:37~18:44) 다른 경우에는 자동 실패 시스템·스키마 검사·행동 측정. *"it's very important to have to define a failure surface before you ever start."*(18:53~18:57)
3. **minimal, bounded pilots** — *"to test architecture"*(19:01~19:05)
4. **rig로 옮기기** — *"once something starts working, we move those checks into rigs, code that runs between bounded work segments that we call codons."*(19:05~19:11)
5. **codon 재사용** — *"These codons are then reused, looped independently, validated, and placed in sequence."*(19:13~19:17)
6. **프로덕션 배포** — *"working pipelines get deployed to production, where they can slowly mature."*(19:20~19:24)

- ⭐ *"that middle part is where the surfing happens. We find an architecture that gives a solid result. We use it as a baseline. Then we swap models and some other parts for faster, cheaper options, compare against known intermediates, tighten the requirement for success each time, moving closer and closer to the ideal, and you just watch the frontier move."*(19:25~19:43)
- *"Being able to break a complex problem into pieces means each piece can move its own to its own best position, as Adam Smith would say."*(19:44~19:52)
- ⭐ 정의의 나머지 절반: *"In a system like this, ontologies exist as intermediates between intelligence and result, which makes them easier to reuse. That's the other half of what I mean by just-in-time ontologies. It's built when the job needs it, kept with its receipts, and reused when the next job needs the same thing."*(19:53~20:10)

→ [[pareto-surfing]](신규) · [[harness-as-platform]] · [[fixed-budget-alpha]] · [[verifiable-goals]] · [[deterministic-agent-pipeline]](rig = 결정론 검사 코드) · [[just-in-time-ontology]]

## 10. 맺음 — 사과 (20:19~20:50)

- *"I close with an apology, right? That the answer is there is no ontology. Not a universal one, at least. There never was one. The good news is that this makes every ontology and schema valid, as long as you can label and preserve the context around it."*(20:19~20:34)
- *"we're rapidly approaching a future where any information, in any format, is made as useful as it can be."*(20:39~20:46)

## 이 위키와의 연결

### 이어지는 것

- **[[jev]]·[[system-1-model]]: 첫 외부 프로덕션 규모 보고와 첫 실패 양상.** 지금까지 Jev는 TypeSafe·LangChain·IBM 해설의 설명, Altman·Shipper·Pocock의 언급, Khourshid의 데모 한 번이었다. 이 발표는 **90,000 호출·203,317 케이스**라는 규모와 함께 Jev의 실패를 처음 기록한다. 실패는 *"confidently said no"*였고, 고친 것은 모델도 임계값도 아닌 **질문의 정의**(*"what counts as enough evidence"*)였다. Jev의 자리는 *"the bottom end of large workloads"*의 작업자다(10:02~10:04).
- **[[model-mixing-economics]]: 셋째 역할.** 기존 서술은 계획 모델과 실행 모델의 분할이었다(Cursor·Factory·Kimchi 등). 이 발표는 그 둘이 *"pull in very different directions"*(09:03~09:05)라고 하고, 그 위에 **hill climber**(파이프라인을 스스로 최적화하는 모델)를 더한다. 그리고 *"coding agents kind of mash [them] into one context window"*(08:31~08:34)라고 코딩 에이전트를 비판한다.
- **[[verification-bottleneck]]·[[tech-bridge-g2i-generation-cheap-evaluation-expensive|G2i 편]]**: G2i의 *"Generation is cheap, but evaluation is expensive"*에 **돈으로 매긴 비율**이 붙는다. 검증에 $545, 첫 답에 $128로 약 4배다.
- **[[multimodal-elicitation]]**: 커머스 에이전트 쪽 화자는 사용자 제약과 카탈로그 온톨로지 사이에 *"임시적인 연결 고리"*를 먼저 놓으라고 했다. 결정 시점에 스키마를 병합한다는 just-in-time ontology와 같은 방향이다.
- **[[deterministic-agent-pipeline]]**: rig(*"code that runs between bounded work segments"*)는 모델 단계 사이의 결정론 검사다. 같은 골격이다.
- **[[intelligence-abundance]]**: 판단이 싸지면 데이터 변환의 경제가 바뀐다는 이야기다. Jev 이름의 유래(Jevons paradox, [[jev]] 페이지)와 같은 그림이지만 화자는 Jevons를 말하지 않는다.

### 갈리는 것

> ⚠️ **Contradiction(약): 검증은 실행보다 싼가.** [[verification-cost-asymmetry]]는 *"에이전트가 경제적으로 성립하는 작업은 검증이 실행보다 싼 작업이다"*(Piras, NP형)를 축으로 삼는다. 이 발표에서는 *"Checking cost about four times as much as doing"*(12:26~12:28)인데도 작업 전체는 예상의 약 8%로 끝났다. 층은 다르다. Piras는 한 결과를 검증하는 단가를 말하고, 여기서 checking은 second opinion·불일치 해소·감사를 합친 **파이프라인 단계의 총액**이다. 그래도 "검증이 실행보다 비싸면 만들지 말라"는 귀결과는 갈린다. 여기서 검증이 비쌀 수 있었던 것은 첫 답이 Jev 같은 싼 모델이었기 때문이다.

> ⚠️ **긴장: 보정된 확률 vs "confidently said no".** [[jev]] 페이지의 IBM 해설은 TypeSafe 자료를 재진술해 *"Because the numbers are calibrated"*라고 했다. 이 발표에서 Jev는 가구 연결 9건에 *"confidently"* 아니라고 답했다. 정의를 고친 뒤에는 13개 개발 질문 모두 yes로 바뀌었다. 질문이 바뀌자 답이 바뀐 것이므로 보정 실패라고 단정할 수는 없다. 다만 **보정은 질문의 정의가 결정과 맞을 때만 의미가 있다**는 제약이 처음 기록된다. 화자는 확률값을 말하지 않는다.

> **화자 자신의 철회.** *"I talked about a single universal schema when I founded Southbridge 2 years ago."*(01:56~02:01) → *"This is why I was wrong."*(04:33) 회사의 출발 명제를 스스로 뒤집는다는 점에서 [[tech-bridge-horthy-state-of-software-factory|Horthy 편]]의 자기 철회와 같은 형식이다.

> **합의는 충분한가.** 설명란은 *"여러 모델의 합의만으로는 오류를 막기 어렵습니다"*를 앞세운다. 발화는 두 방향을 다 말한다. 194건의 일치에는 오류가 0이었고(15:52~15:57), 네 계열이 같은 틀린 합계를 냈다(16:26~16:34). 앞의 것은 *"different families"*, 뒤의 것은 *"LLMs as a species"*의 공통 prior다. 대출 부호 사례(*"validated by multiple models"* 15:03~15:05)도 뒤쪽이다.

## 해소하지 않고 표시만 한 것

- 에이전트 이름 *"4A"*(12:49), *"library of gigantic parts"*(13:21), *"checking letter"*(13:28), *"carpet"*(01:51)의 판독.
- *"Luna"*가 어느 회사의 어떤 모델인지. 세 설계의 *"cheap reasoning model"*과 같은지. [[tech-bridge-altman-devday-dots]]의 Luna와 같은지.
- *"distilled outside the same company"*(16:12~16:15)의 뜻과 대상.
- Fable의 버전, cheap reasoning model의 이름, *"about 2% of the cost"*의 기준.
- 데이터셋·프롬프트 공개 위치(*"download it for yourself"*). 비용 내역의 $122 차이. *"four different model families"* 벤치마크의 이름.
- Hank Weave의 정식 표기와 저장소. hank·codon·rig의 정확한 정의(자막은 codon = *"bounded work segments"*, rig = 그 사이에서 도는 코드까지).
- DuckDB Hannes 글의 제목·출처. 이전 회사(선박 플랫폼)의 이름.
- 행사명·도시·녹화일. 슬라이드 내용(아키텍처 계층도, *"everything we learned"* 목록).

## 등장 개체

- 인물: [[hrishi-olickel|Hrishi Olickel]](신규 제안 — ⚠️ 이름은 설명란에만) · Hannes(DuckDB, 페이지 없음) · 아르키메데스·Adam Smith(인용)
- 조직: [[southbridge|Southbridge]](신규 제안 — en-orig *"Southbridge"*·*"South Ridge"*) · [[typesafe-ai|TypeSafe]](Jev 제작사, 발화되지 않음) · DuckDB(페이지 없음)
- 모델·제품: [[jev|Jev]](en-orig *"Jeff"* 혼용) · [[fable-5-1|Fable]](버전 미발화) · [[openai-astra|Astra]] · Opus(버전 미발화, [[anthropic|Anthropic]]) · Luna(⚠️ 미판독, 페이지 없음) · *"3.5 turbo"* · [[claude-code|Claude Code]](en-orig *"Cloud Code"*) · Pi(에이전트 런타임, 페이지 없음) · Hank Weave(⚠️ 표기 미확정, [[southbridge]] 섹션으로)
- 개념: [[just-in-time-ontology]](신규) · [[cross-model-prior-intersection]](신규) · [[pareto-surfing]](신규) · [[system-1-model]] · [[model-mixing-economics]] · [[verification-cost-asymmetry]] · [[verification-bottleneck]] · [[fixed-budget-alpha]] · [[self-harness]] · [[harness-as-platform]] · [[verifiable-goals]] · [[deterministic-agent-pipeline]] · [[generator-evaluator-pattern]] · [[cross-lab-peer-review]] · [[model-calibration]] · [[multimodal-elicitation]] · [[intelligence-abundance]] · [[action-reversibility]] · [[ai-slop]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=8uG4ZY7G2r8> (20:54, `upload_date` 2026-10-17)
- raw: `01.raw/articles/2026-10-17_적시형 온톨로지 - 저렴해진 지능은 데이터에 어떤 의미일까요?.md`
- 설명란 링크: <https://github.com/hrishioa> · <https://www.linkedin.com/in/hrishioa/> (⚠️ 열어 보지 않았다)
- Jev의 다른 서술: [[tech-bridge-jev-agent-harness]] · [[tech-bridge-jev-calibrated-decisions]] · [[tech-bridge-altman-devday-dots]] · [[tech-bridge-pocock-pr-bottleneck]] · [[tech-bridge-goodbye-slop-state-machines]]
- 검증 비용: [[tech-bridge-g2i-generation-cheap-evaluation-expensive]] · [[tech-bridge-mousepower-measuring-agents]]
- [[tech-bridge]] · [[hrishi-olickel]] · [[southbridge]]
