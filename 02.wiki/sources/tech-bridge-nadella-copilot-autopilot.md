---
title: "Tech Bridge — Satya Nadella(Microsoft) × Deirdre Bosa 'DB Live': Copilot과 Autopilot, 한계비용이 생긴 소프트웨어, auto가 제품이 된 모델 선택"
type: source
tags: [microsoft, copilot, autopilot, agent-365, business-model, marginal-cost, model-routing, open-weights, us-china, embedded-evaluators, data-center, capex, human-control, interview, video]
source-url: https://www.youtube.com/watch?v=MsgkesEBZFc
source-type: video
author: Tech Bridge (한영자막 재배포) · 대담 [[satya-nadella]] ([[microsoft|Microsoft]] — 자막은 "Satya"뿐, 성·직함은 제목·설명란) × 진행자 Deirdre (성 Bosa는 설명란, 쇼 이름 "DB Live") · Microsoft "Copilot event" 현장 · 촬영 날짜 미확정
date-published: 2026-09-28
ingested: 2026-09-29
created: 2026-09-29
updated: 2026-09-29
---

# Tech Bridge — Satya Nadella: Copilot과 Autopilot, 그리고 다가올 제품 경쟁

[[tech-bridge|Tech Bridge]]가 재배포한 **25:47 대담**(공식 챕터 11개). [[microsoft|Microsoft]]의 [[satya-nadella|Satya Nadella]]가 진행자 Deirdre의 새 쇼 *"DB Live"* 첫 게스트로 나왔고, 장소는 Microsoft의 *"Copilot event"*(00:09~00:11)다. **이 위키 첫 Microsoft 1인칭 소스**이자, [[openai|OpenAI]]의 **최대 파트너 겸 경쟁자**가 말하는 첫 소스다. 한 줄 요약:

> **새 [[microsoft-copilot|Copilot]]은 chat·co-work·code·Autopilot을 한 묶음으로 낸다 — 어떤 폼팩터도 끝이 아니고 조합이 제품이다. 신뢰가 최대 이슈라 [[agent-365|Agent 365]](관찰·거버넌스·감사)가 핵심이다. 보조금이 끝나면 소프트웨어가 처음으로 한계비용을 갖는다. 사용자가 모델을 고르던 시대는 끝났고 "auto"가 제품이다.**

> *"software for the first time has marginal cost"* (05:47~05:49) · *"auto has become the product essentially"* (08:19~08:21) · *"anything that doesn't serve humans or is not in human control is not worth doing"* (24:25~24:30)

ASR·ko 보정: ko가 ***"But Open AI for us … especially with Astra now is again really seeing fantastic traction"* 을 "OpenAI는 그렇지 않습니다"로**(09:55), ***"both sides will care about the same set of things"* 를 "양쪽 모두의 생각이 다르다"로**(17:39), ***"not just … something that Sam and I sit around and decide"* 를 "샘과 나만이 … 대화를 통해 결정했습니다"로**(17:13~17:18) 뒤집는다. **insider risk의 대비**(과거 = 악의적 행위자, 이제 = 에이전트 자신)를 ko가 **"역사적으로 모든 것은 에이전트에 달려 있었다"** 로 지운다(14:03). *marginal cost* → **"가장자리 가의"**(05:49), *auto has become the product* → **"자동 조종 장치 자체"**(08:19), *embedded evaluators* → **"통합 평가자"**, *inference is revenue* → **"추론이란... 레시피"**, *income statement* → **"결과 시연"**, *Anthropic* → **"인류학"**, *harness* → **"환경"**, *Copilot* → **"부조종사"**, *12 X* → **"12번"**. 전체는 raw의 보정 표.

> ⚠️ **당사자 진술, 독립 확인 없음.** 화자는 자기 회사 행사장에서 자기 제품 출시일에 말한다. **수치는 셋뿐이고 모두 검증 불가**다 — Quincy 세수 *"something like 12 X"*(18:52~18:54), 고용 *"close to a thousand people"*(19:06~19:08), 사례로 든 *"what took 12 months is now taking 3 months"*(21:58~22:02, 고객명 없음). *"Agent 365 … the product that is getting the fastest adoption in the enterprise"*(04:41~04:46)에는 **채택 수치가 없다.**
>
> ⚠️ **화자·진행자 이름.** 자막은 *"Satya"*(00:00)뿐이고 화자가 *"Microsoft was founded on"*(01:09~01:11)이라 말한다. **Nadella**·**CEO**는 제목·설명란에서 온다. 진행자는 *"Deidra"*(00:05)·*"Deirdre"*(25:44), 성 **Bosa**와 *"테크 저널리스트"* 는 **설명란에만**. 소속 매체는 발화되지 않는다. 설명란의 *"단독 대담"* 도 자막에 없다.
>
> ⚠️ **촬영 날짜 미확정.** 절대 날짜 발화 없음. 상대 앵커: *"a big meeting this week between President Trump and President Xi Jinping"*, 화자가 *"the dinner on Thursday evening"* 에 간다(13:16~13:24), *"tomorrow night at dinner"*(17:31~17:33) → **목요일 만찬 전날**. OpenClaw 붐은 *"earlier this year"*(03:53~03:56, 진행자). [[tech-bridge-jensen-huang-cbs-interview]]의 *"다음 주"* 시진핑 국빈 만찬과 **같은 회담일 수 있으나 판정하지 않는다.**
>
> ⚠️ **편집본.** en-orig에서 답변 첫머리가 여러 번 잘려 있다(05:23 · 06:04 · 08:15 · 09:31 · 22:21 · 25:08). ko·en에는 en-orig에 없는 말이 몇 군데 있다(18:22 호명, 24:17, 25:07~25:08) — **인용하지 않는다.**

## 1. 새 Copilot — 하나가 아니라 조합 (00:00~05:18)

- **진화 순서**: chat(정보 검색의 새 방법) → co-work(*"task delegation"*) → 오늘 **code**(00:48~01:08). *"what's the real difference between creating a website, an app, or a document. Guess what? There is not."*(01:11~01:16) — 앱을 만들어 *"hosted like I would on OneDrive a document"*(01:18~01:24).
- **Autopilot** — *"a long-running business process agent, right? Where it completes the job, but you are still the human in the loop both at the input and at the output"*(01:34~01:44). PC 시대에 Office가 그랬듯 *"Copilot in the AI era is the coming together … of all of these functions"*(01:54~02:01).
- **왜 Autopilot만 내지 않나** — 진행자는 *"the real star of the show is Autopilot"* 이라며 Meta의 [[muse|Muse]]·*"Instinct"*·*"Grok Bot"* 같은 소비자 개인 에이전트를 이미 쓴다고 한다(02:02~02:15). 답: *"Autopilot's a fantastic until you have to do something with the output of an Autopilot"*(02:54~02:59), *"I don't think of any one form factor as the be-all end-all"*(03:02~03:04). Excel 비유 — *"there's an outer loop that's kind of Co-work. The inner loop is the agent loop inside of Excel"*(03:17~03:22). *"I think of Autopilot as something that has an identity, it does complete jobs, but then when it hands off or when I'm trying to instruct it, I need my Copilot and my Co-work"*(03:24~03:33) — *"it's the composition"*(03:38). → [[microsoft-copilot]] · [[assistance-vs-automation]]
- **신뢰가 최대 이슈** — *"can I really trust it with all of my credentials?"*(04:20~04:22), *"I'm in control, I can audit. And in the enterprise, this is everything"*(04:29~04:33). 그래서 [[agent-365|Agent 365]]가 *"probably the most important"*, *"the fastest adoption in the enterprise"*(04:41~04:46): *"observe everything, govern everything, set policy, have security, have the finops"*(04:46~04:50). → [[agent-governance-layers]]

## 2. 한계비용이 생긴 소프트웨어 — 좌석 + 사용량 (04:54~08:05)

*"once the subsidy stop[s] for everybody, … there's marginal cost to tokens"*(04:55~05:02). *"there's a certain amount of subsidy anyone can do"*(05:07~05:09), 그러나 결국 사용자가 얻는 **수익(return)** 의 문제다(05:12~05:16). 상시 가동 에이전트가 너무 비싸냐는 물음에(05:17~05:21) — 사업 모델은 *"finite"*: 구독 · 종량제 · 광고 같은 양면 시장 · 거래(05:28~05:43), 전부 *"account for the fact that software for the first time has marginal cost"*(05:43~05:49).

가격 구조(진행자 정리 05:50~05:59: **Co-work·Autopilot은 사용량, Chat은 좌석**): *"seats are nothing other than entitlements to usage"*(06:16~06:21) — 좌석은 *"a more convenient way to budget and buy"*(06:21~06:27). 구독은 *"deliver more value every day of the week as models … improve"*(06:40~06:48), 그 위에 *"usage-based functionality that any user at any time can use with no limits"*(06:48~06:53). 모두가 Autopilot을 원하게 되면? *"Autopilot will start with a certain cost footprint and it'll only reduce after that"*(07:35~07:38), 앞으로의 신제품도 *"some set of usage rights that come right at the seat and then some that are going to be usage based"*(07:46~07:50). → [[software-marginal-cost]] (신규)

## 3. "auto가 제품이다" — 에이전트가 모델을 고른다 (08:06~10:26)

*"the last time I picked a model has been a long time because in an interesting way auto has become the product"*(08:15~08:21). 모델을 고르는 것은 *"pretty passe both … in GitHub co-pilot as well as in co-pilot"*(08:26~08:31). *"we are even not just doing model routing, but … we have learned routers, right? So the the real model is my model that routes"*(08:33~08:41). 진행자 *"Hard model for hard tasks"* → *"Correct"*(08:42~08:44). 스웜·서브에이전트에서는 더 동적이고, 여러 모델 패밀리를 넘나들며 *"KB[=KV] cache hit ratios"* 를 다뤄야 한다 — 코딩에서는 쉽고 지식 노동·사이버에서도 풀고 싶다(08:45~09:02). *"it's about sort of the intensity of the task that then really picks the model. So it's not the user. … your agent picks the model"*(09:10~09:17).

사용량 대시보드: 오픈 웨이트 쪽은 *"the MAI models"*(09:34) — **자체 모델이 더 강한 모델에 넘기는 역할**, *"the model router plus a model that we have trained together in a harness. And our harness is capable of calling all the other models"*(09:45~09:53) → 구조상 사용량이 가장 많다. OpenAI는 *"especially with Astra now … really seeing fantastic traction"*(09:56~10:01) → [[openai-astra]]. Anthropic 모델, *"Grok in there in Excel"*(10:03~10:08). *"every model … needs to compete … for handling tasks inside of the Copilot system"*(10:19~10:25). → [[model-mixing-economics]]

## 4. 오픈 웨이트와 중국 모델 (10:27~12:03)

진행자가 *"Chinese models hosted here that have become very efficient and very capable"*(10:27~10:33)를 묻자 — Foundry에 오픈 웨이트가 많지만 **Copilot은** *"most of these are all American close[d] source models … right now"*(10:38~10:45). 오픈 웨이트 모델을 가진 누구든 *"whether it's western or others"* 유통시킬 수 있게 하고 싶다(10:49~10:56). *"given the open harness we have … we're not locked into any one model"* — 고객이 *"bring their own model to … Copilot"*(11:01~11:10). 점유율: *"on the API side in our case, they are slow[?] on … a growth basis, yes. But in absolute terms, we are dominated still by what is happening with Open AI"*(11:18~11:29) — ⚠️ 앞 절이 빠르다는 뜻인지 느리다는 뜻인지 불명(아래). 1년 뒤는 *"how rapidly do these things converge in capability"*(11:35~11:41)에 달렸고, 파레토는 가격이며, 기업에서 오픈 웨이트는 **고객이 특정 비즈니스 프로세스에 맞춰 fine-tune할 때** 유용하다(11:46~12:03).

## 5. OpenAI·Anthropic의 엔터프라이즈 진입 (12:04~13:16)

진행자: OpenAI와 Anthropic이 점점 엔터프라이즈에 집중한다, 기업이 그들의 제품을 원하게 될까 걱정하나(12:17~12:29). 답: *"open clock[=OpenClaw] came out and I think inspired … all of us … to say wow there is a way … to think about these autopilots"*(12:33~12:40) → [[openclaw]]. MS가 한 일은 *"really make sure that there's trust in their runtime environments"*(12:44~12:49) — Agent 365로 **Autopilot 활동의 감사 가능성**을 갖춘 호스팅 환경(12:51~13:00). *"Of course there's going to be fierce competition"*(13:03~13:05), *"a golden era of product making"*(13:12~13:14). ⚠️ **경쟁사 이름을 받아 놓고 경쟁사에 대해서는 한 마디도 하지 않는다** — 답의 대상은 OpenClaw와 자기 제품이다.

## 6. 미·중 정상회담 — 통보 체계와 insider risk (13:16~16:10 · 17:31~18:04)

- **권고**: 장관(en-orig *"Blinken"*, ko·en *"Bessent"* — 판독 안 함)이 말한 **통보(notification)** 가 좋은 출발(13:31~13:45). 진행자 *"The hotline?"*(13:46) → *"if there's a cyber incident or something"*(13:48~13:51).
- ⭐ **왜 통보인가 — 에이전트가 insider가 된다**: *"for the first time … with these powerful AI agents, you kind of have an insider risk"*(13:53~13:58). *"historical cyber risk was all about the bad actor using cyber capability to attack. And the question now is, in fact, the attack can just come from the agent itself"*(14:00~14:13). 그래서 *"having notifications between these two states is a fantastic start"*(14:15~14:17). → [[agentic-misbehavior]]
- **안전의 세 층**(14:27~14:53): ① *"bad actors using AI"* ② *"an environment that needs to be contained that is not contained"* — *"That is where the notifications"* ③ **정렬** — *"it's an experimental science. We don't yet have the science for really thinking about … alignment"*(14:44~14:51). 셋 다 *"first-class topics"*.
- 이번 주 회담보다 중요한 것은 **미국이 세 층 모두에 정책 해법을 찾는 것**, 그리고 업계도 제 몫을 하는 것(15:04~15:21). *"building out that containment is a solid engineering problem"*(15:27~15:31) — Autopilot 실행 환경이 그 *"heavy lifting"*(15:33~15:43).
- **미·중이 합의할 한 가지**(17:31~18:03): *"both sides will care about the same set of things"* — 시민에게 가치, **확산(diffusion)**, 그리고 안전하게. 규범을 세울수록, *"the US in particular can lead"*. → [[ai-arms-limitation-lens]]

## 7. 규제 — embedded evaluators와 식품 안전 (15:46~17:30)

- **이미 있는 것**: *"OpenAI and we have been doing quite frankly for all these years is we have a joint safety board where we really do a lot of the testing internally on both sides. Essentially, we have had, you can call it embedded evaluators, OpenAI and Microsoft"*(15:48~16:05).
- **사후가 아니라 사전**: *"it's not about trying to come up with regulation after something bad happens, but to be able to really anticipate the risks"*(16:34~16:42) — 먼저 출시 과정의 엔지니어링을 다하고, 그다음 규제(16:42~16:52). *"we have after all things like food safety laws for a reason … we want the same trust in our AI supply chain"*(16:54~17:03).
- **새 규제가 필요한가** → *"I think so. I think in time we will need some new way"*(17:07~17:09): embedded evaluators가 *"not just … something that Sam and I sit around and decide about"*, 업계 전체라면 *"we should actually have a very diverse group of people who are doing it"*(17:12~17:30). → [[embedded-external-evaluators]]

## 8. 데이터센터 — 지역 사회의 허가 (18:05~20:39)

진행자: 데이터센터 반대가 커졌고 MS는 **NDA를 없애는 등** 지역 사회와 일하는 방식을 바꿨다(18:05~18:19). 답: *"we have to get the permission from the communities"*(18:21~18:25), 전력·물을 쓰니 *"we have to earn that permission"*(18:27~18:36). 근거는 **워싱턴주 Quincy** — *"I'll call it a 20 year longitudinal study"*(18:45~18:47): 세수 *"something like 12 X"*(18:52~18:54), 카운티·농촌 공동체 성장, 새 병원·학교·시내 중심가(18:56~19:05), *"close to a thousand people there"*(19:06~19:08). 데이터센터는 짓고 나면 자동으로 돌아간다는 통념과 달리 *"you're constantly refurbishing a building"*(19:10~19:17). 약속 — *"paying our way through"*, 물 사용(19:38~19:47), *"I don't think of anything that we do as building a data center and get out"*(19:51~19:54). 경쟁 조건이 *"to be more welcome in … the communities"* 로 바뀐다면 좋은 일(20:06~20:19), *"We want that to become a new standard … and everyone should adopt it"*(20:36~20:38). → [[data-center-local-backlash]]

⚠️ **NDA는 진행자만 말한다** — 화자는 NDA를 한 번도 직접 설명하지 않는다.

## 9. 과잉 대 과소 구축 — 손익계산서의 물리 법칙 (20:40~23:43)

- **목표는 확산**: *"the market is still a lot more concentrated. It's about the hit app or … the consumption of compute by those hit apps"*(20:53~21:04). *"there will never be a way … to say there's a perfect line of under build over build"*(21:06~21:13) — 목표는 기업이 토큰으로 **실질 ROI**를 얻고 *"economic output that shows up in real GDP growth"*(21:17~21:25). *"whether that will be a linear line, I don't know"*(21:28~21:29).
- **남과의 차이**(진행자: 다른 하이퍼스케일러는 크게 빌려서 짓는다, 22:06~22:19): *"Some folks may be catching up because remember, we we've had like a more gradual ramp"*(22:24~22:28), AI 컴퓨트 배분이 *"first showed up in Redmond … a long before it showed up in other hyperscalers"*(22:30~22:38). *"we feel pretty confident about our compute ramp, and others will … decide on what compute ramp they want"*(22:49~22:53).
- ⭐ **추론 = 매출, 훈련 = R&D**: *"Ultimately, inference has to dominate because otherwise … what are you training for?"*(22:58~23:01). *"what percentage of your revenue is R&D? Training is like R&D, right? Is it 10? Is it 15? Is it 20?"*(23:05~23:11). *"that is the laws of physics of the income statement that all of us are going to be subject to"*(23:29~23:34). 한동안은 짓고 훈련할 수 있지만 *"A percentage of revenue is R&D"*(23:39~23:41). → [[inference-revenue-training-rnd]] (신규) · [[compute-constrained-growth]]

## 10. 인간 통제 원칙 (23:44~25:47)

진행자: 지난 몇 주 안전·정렬이 주류 담론이 됐고 Mustafa Suleyman이 안전과 AI 개발에 관한 글과 *"code of conduct"* 를 냈다 — 인간 통제 논쟁이 MS가 만들고 내놓을 것을 무엇을 바꿨나(23:44~24:08). 답: *"it centered all of us on saying some obvious things"*(24:10~24:14). *"anything that doesn't serve humans or is not in human control is not worth doing is sort of the core principle you have to stand by"*(24:23~24:31). *"as this experimental science develops, we should not launch into the world anything that we don't believe has those two attributes"*(24:36~24:43) — 회사 단위와 업계 단위의 기준이고, *"the political economy is not going to give permission to anybody"* 가 어기는 쪽을(24:54~25:03). 무언가를 늦추거나 제한했나(25:05~25:08) → *"take more and more time … around … the testing of it. And then also phased rollout"*(25:14~25:21), *"run the experiments in safe environments"*(25:27~25:29).

⚠️ **질문에 대한 구체적 답은 없다** — 어떤 제품을 늦췄는지, 테스트 기간이 얼마나 늘었는지 말하지 않는다.

## 기존 위키와의 대조

### 합치하는 것

- **세 CEO가 같은 회담에 바란 것** — [[dario-amodei|Amodei]]는 **생물무기협약 확장**과 **속도 제한**(검증이 핵심, [[ai-arms-limitation-lens]]), [[jensen-huang|Huang]]은 **"제품 기대치" 글로벌 표준**([[tech-bridge-jensen-huang-cbs-interview]]), Nadella는 **사고 통보 체계**(격리 실패 시). 층이 모두 다르다 — **무기 · 소비자 제품 · 사이버 사고 대응**. Nadella의 층이 가장 작고 가장 실무적이며, 근거로 든 **"에이전트 자체가 insider"** 는 이 위키 [[agentic-misbehavior]]의 관찰을 **국가 간 위험**으로 올린 첫 발언이다.
- **embedded evaluators — 같은 단어, 같은 비유** — [[embedded-external-evaluators]]의 Amodei(*"식품 검사관"*)와 Nadella(*"food safety laws"*, *"embedded evaluators"*)가 **같은 용어와 같은 식품 비유**를 쓴다. 둘 다 **사전**(*"anticipate the risks"*)이다.
- **OpenClaw가 기업 제품의 영감** — 이 위키가 [[openclaw]]를 "지나가는 언급을 모은 자리"로 두어 왔는데, 처음으로 **대기업 CEO가 자기 제품(Autopilot)의 영감으로 명시**한다(12:33~12:40).
- **Astra의 견인력** — [[openai-astra]]에 **파트너 CEO**의 서술이 더해진다. 수치는 없다.
- **모델 선택이 사용자에게서 떠난다** — [[model-mixing-economics]]가 모아 온 *개발자가 예산으로 모델을 섞는다*(Cursor·Oracle 등)에서 한 걸음 더: **"auto가 제품"**, 라우터가 학습되고 에이전트가 고른다. [[jev|Jev]] 편의 *"라우터가 LLM이 아닐 때"* 와 방향이 같다.

### 갈리는 것

> ⚠️ **Contradiction: 보조금은 끝나는가.** [[transaction-cut-monetization]]의 [[mark-zuckerberg|Zuckerberg]]는 **주당 1억 토큰 무료 + 가상 머신**을 주고 거래 상대에게서 몫을 뗀다. Nadella는 *"once the subsidy stop[s] for everybody … there's marginal cost to tokens"*(04:55~05:02)라며 **보조금은 일시적**이라고 본다 — 단 거래 수수료·광고도 그의 *"finite number of business models"* 목록(05:28~05:43)에 들어 있다. 둘은 **"누가 한계비용을 대는가"** 에서 갈린다(Meta는 상대 기업, MS는 좌석+사용량으로 사용자 기업). 어느 쪽도 비용 수치를 대지 않는다.

> ⚠️ **Contradiction: 새 규제가 필요한가.** [[tech-bridge-jensen-huang-cbs-interview|Huang]]: *"새 법 전에 현행 법"*, *"무엇이 빠졌는지 알기 전까지 왜 법을 더?"*. Nadella: *"it's not about trying to come up with regulation after something bad happens, but to … anticipate the risks"*(16:34~16:42), *"I think in time we will need some new way"*(17:07~17:09). **같은 주(추정)에 공급자 CEO와 하이퍼스케일러 CEO가 반대 방향**이다. ⚠️ 단 Nadella도 **"먼저 엔지니어링, 그다음 규제"**(16:42~16:52) 순서를 두어 즉시 규제를 요구하지는 않는다.

- **"embedded evaluators"의 뜻이 다르다** — Amodei의 평가자는 **제3자 비영리·정부**다. Nadella가 *"있어 왔다"* 고 하는 것은 **OpenAI와 MS가 서로의 안에서 하는 테스트**(joint safety board)다 — 제3자가 아니라 **이해관계가 얽힌 두 파트너**다. Nadella 자신도 그 한계를 짚어 업계 단위라면 *"a very diverse group of people"* 이어야 한다고 한다. 이 위키는 두 용법을 **같은 개념의 다른 단계**로 기록하되 **독립성 수준이 다르다**고 표시한다.
- **컴퓨트 거품의 위치** — [[compute-constrained-growth]]의 [[sam-altman|Altman]]: *"우리 계획은 걱정 안 한다, 세계의 계획이 걱정"*. Nadella도 같은 구조다 — *"we feel pretty confident about our compute ramp, and others will … decide"*, 다른 이들은 *"catching up"*. **두 CEO 모두 거품의 위험을 남에게 둔다.** 차이는 Nadella가 **판단 규칙**(추론 매출 대비 훈련 R&D 비율)을 준다는 것 — 그러나 **비율 자체(10·15·20%)는 질문형**이다.
- **데이터센터 대응** — [[data-center-local-backlash]]의 Huang은 **사과 + 물은 신화 + 최소 기준**. Nadella는 **이름 있는 사례(Quincy) + 허가의 언어**. Nadella는 물·전기 요금 반론을 하지 않고 *"commitments around water use"* 만 말한다. 운영자(하이퍼스케일러)의 첫 목소리지만 여전히 **반대 측 1차 목소리는 없다.**

## 해소하지 않고 표시만 한 것

- **장관 이름** — en-orig *"Blinken"*(13:31, 13:43) vs ko·en *"Bessent"*. 대담 문맥(트럼프 행정부)에는 후자가 맞아 보이나 `en`은 ko와 같은 원천이라 **독립 확인이 아니다.** 어느 부처인지도 발화되지 않는다.
- **오픈 웨이트 점유율이 빠르게 느는가 느리게 느는가** — *"they are slow on … a growth basis, yes. But in absolute terms, we are dominated still by … Open AI"*(11:18~11:29). *"But"* 구조상 앞 절이 "성장률로는 빠르다"로 읽히지만 세 트랙 모두 *slow*.
- **"Instinct"**(02:15, 12:10) — 진행자가 쓰는 소비자 에이전트. 무엇인지 모름. **"Grok Bot"**(02:15) — [[grokbot|Cursor의 GrokBot]]인지 xAI 제품인지 모름.
- **"Copilot tasks"**(02:44~02:46) — 제품명으로 읽히나 설명 없음. OpenClaw와 *"just around the same time"* 출시.
- **"MAI models"**(09:34) — Microsoft 자체 모델로 읽히나 풀어 말하지 않는다. 오픈 웨이트냐는 물음에 MAI로 답한 이유도 불명.
- **Agent 365의 "fastest adoption"** — 수치 없음. 무엇 대비 가장 빠른지 없음.
- **Quincy 수치** — *"something like 12 X"*, *"close to a thousand"*, *"I'll call it a 20 year longitudinal study"* — 화자가 붙인 이름이지 연구가 아니다. 출처 없음.
- **NDA 폐지의 범위** — 진행자 서술뿐. 언제, 어느 지역, 무엇을 공개하게 됐는지 없음.
- **"12개월 → 3개월"**(21:58~22:02) — 공급망 프로젝트의 **예시**로 말해진 것이고 고객·측정 조건이 없다.
- **R&D 비율 10·15·20%** — 질문형. MS 자신의 훈련/추론 비율은 말하지 않는다.
- **"The memo … first showed up in Redmond"**(22:30~22:37) — *memo* 가 실제 문서인지 오인식인지 불명.
- **Suleyman의 글**(23:55~24:00) — 제목·날짜 없음. *"code of conduct"* 의 내용 없음.
- **무엇을 늦추거나 제한했나** — 질문은 잘렸고(25:05~25:08) 답은 일반론(테스트 시간·단계적 출시).
- **"frontier ecosystem"**(21:13) — en-orig 표기 그대로이나 문맥상 불확실.
- **보안 모델** — Autopilot이 *"all of my credentials"*(04:22)를 쥔다는 신뢰 문제를 스스로 꺼내지만, 격리·권한 설계의 구체는 **Agent 365라는 이름**으로만 대신된다. [[prompt-injection]]·[[lethal-trifecta]]는 한 번도 나오지 않는다.

## 등장 개체

- 인물: [[satya-nadella]](신규) · Deirdre Bosa(진행자, 성은 설명란 — 페이지 없음) · Sam Altman(*"Sam and I"* 17:17 → [[sam-altman]]) · Mustafa Suleyman(진행자 언급 — 페이지 없음) · Trump · Xi Jinping · "Secretary Blinken/Bessent"(미확정)
- 조직: [[microsoft]](신규) · [[openai]] · [[anthropic]] · [[meta]] · xAI(Grok)
- 제품·모델: [[microsoft-copilot]](신규 — chat · co-work · code · Autopilot · Copilot tasks) · [[agent-365]](신규) · GitHub Copilot · Microsoft Foundry · OneDrive · Excel · Office 365 / Microsoft 365 · MAI 모델 · [[openai-astra]] · Grok · [[muse]] · [[openclaw]] · "Instinct" · "Grok Bot"(→ [[grokbot]]?)
- 개념: [[software-marginal-cost]](신규) · [[inference-revenue-training-rnd]](신규) · [[model-mixing-economics]] · [[assistance-vs-automation]] · [[agent-governance-layers]] · [[embedded-external-evaluators]] · [[ai-arms-limitation-lens]] · [[agentic-misbehavior]] · [[data-center-local-backlash]] · [[compute-constrained-growth]] · [[transaction-cut-monetization]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=MsgkesEBZFc> (25:47, `upload_date` 2026-09-28)
- raw: `01.raw/articles/2026-09-28_MS 사티아 나델라가 밝힌 AI 미래 — 코파일럿과 오토파일럿, 그리고 다가올 제품 경쟁.md`
- 같은 회담 주제: [[tech-bridge-dario-amodei-cbs-interview]] · [[tech-bridge-jensen-huang-cbs-interview]] · 같은 주제(OpenAI 쪽): [[tech-bridge-altman-benioff-dreamforce]] · [[tech-bridge-brockman-agi-era-defender-window]] · 사업 모델 대비: [[tech-bridge-zuckerberg-muse-personal-agent]]
- [[tech-bridge]] · [[satya-nadella]] · [[microsoft]]
