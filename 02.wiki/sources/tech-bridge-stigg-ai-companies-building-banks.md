---
title: "Tech Bridge — 모든 AI 기업이 어쩌다 보니 은행을 짓고 있다 (Dor Sasson · Stigg): 청구 뒤 검사에서 추론 전 승인으로, reserve → settle"
type: source
tags: [ai-pricing, metering, entitlements, reserve-then-settle, credits, budgets, concurrency, idempotency, subscription, subsidy, anthropic, openai, openclaw, stigg, vendor-claim, video]
source-url: https://www.youtube.com/watch?v=4JfLShdp92k
source-type: video
author: Tech Bridge (한영자막 재배포) · 발표 [[dor-sasson]] ([[stigg|Stigg]] co-founder & CEO — 직함은 발화, 이름은 설명란에만) · 행사명 미발화(설명란 ai.engineer 링크 → AI Engineer 계열 추정) · 녹화 연도 미발화(*"back in April"* 이후)
date-published: 2026-10-11
ingested: 2026-10-12
created: 2026-10-12
updated: 2026-10-12
---

# Tech Bridge — 모든 AI 기업이 어쩌다 보니 은행을 짓고 있다 (Dor Sasson · Stigg)

[[tech-bridge|Tech Bridge]]가 재배포한 **19:00 단독 발표, Q&A 없음, 공식 챕터 15개.** 화자는 [[stigg|Stigg]]의 co-founder & CEO — *"I'm the co-founder and CEO of Stigg."*(00:00~00:03). 이름 **[[dor-sasson|Dor Sasson]]** 은 **설명란에만** 있다(발화 없음). 이 위키에서 **AI 제품의 과금·권한(entitlement)·사용량 인프라를 정면으로 다루는 첫 소스**다 — 지금까지 토큰 비용은 *사는 쪽*(조직 예산·리더보드, [[overspending-underusing-loop]])이나 *사업 모델*([[software-marginal-cost]]) 쪽에서만 나왔다. 테제:

> **AI 가격 비상은 사업 모델 문제가 아니라 인프라 문제다. 지금의 AI 제품은 권한·한도 검사를 청구서 뒤에 하는데, 사용이 곧 원가인 시스템에선 너무 늦다. 은행·ATM처럼 hot path에서 먼저 동기로 검사·예약(reserve)하고 정산(settle)은 비동기로 해야 한다 — 그래서 모든 AI 회사가 어쩌다 보니 은행을 짓고 있다.**

> *"literally every AI company right now is accidentally building a bank."* (00:08~00:11) · *"what it seemed to be a business problem really was an infrastructure problem"* (03:08~03:13) · *"the checks for what you're entitled, what you're allowed to do (…) happened uh after uh the invoice and not before."* (04:32~04:46) · *"I don't think this is billing."* (09:19~09:21)

이 위키에 개념 하나가 생긴다 → [[reserve-then-settle]] (신규 제안, engineering/systems). 그리고 [[openclaw]]에 **처음으로 정책 사건**(Anthropic의 구독 사용 차단, 화자 주장)이, [[software-marginal-cost]]에 **보조금 크기에 대한 첫 수치 주장**이, [[bring-your-own-subscription]]에 **반대 방향의 사건**이 붙는다.

ASR·ko 보정: ko는 은행 비유의 핵심어를 흔든다 — *bank* → **"벤치"**(00:10, 첫 문장), **concurrency** → **"참석률"·"동의"·"출석"**(10:23, 10:46, 11:14 — 챕터 주제어가 본문에서 사라진다), *rate limitations* → **"이자율"**(08:28), *hold and settle* → **"보존 … 합의"**(11:24), *credit pools* → **"신용조합"**(13:04), *seven-digit contract* → **"수백만 명"**(13:31), *5 weeks* → **"5분 후에 … 몇 주 동안"**(01:10), *5x* → **"5번"**(01:55). ⭐ 화자가 대신 말한 청중의 반론 *"you're pitching this infrastructure"* 를 ko는 **"우리는 이것을 홍보하고 있었습니다"** 라는 1인칭 고백으로 뒤집었다(07:36). 그리고 핵심 진단 *API 사용자 대 구독 사용자* 에서 *subscription* 이 빠졌다(03:19). en-orig 판독: *"open flow"*(01:41) → OpenClaw(⚠️ 판독), *"claw claw max"* → Claude Max(⚠️ 판독, `en`·ko는 Max 탈락), *"hot bath"* → hot path, *"item potency"* → idempotency(여기선 ko *"멱등성"* 이 맞다). 전체 목록은 raw.

> ⚠️ **당사자 진술 — 화자는 이 인프라를 파는 회사의 CEO다.** 화자 스스로 *"Like you're you're pitching this infrastructure, sounds like you have something to do with this. But guys, this is not just me."*(07:35~07:43)라고 선을 긋고 OpenAI 사례로 넘어간다. 마무리 1분(17:56~18:59)은 Stigg 팀의 관점(*"our team likes to say"*, *"a lot of excitement from our team"*)이다. **Stigg 제품 이름·기능은 발화되지 않는다** — 이 소스에서 벤더 피치는 *문제 정의 자체*(이 계층이 빠져 있다, Stripe moment가 없다)의 형태로 온다. 이 위키는 ①~⑤절(진단·패턴)과 ⑥절(피치)을 구분해 기록한다.
>
> ⚠️ **타사 내부에 대한 주장은 전부 화자의 진술이고 출처가 없다** — Anthropic의 보조 규모와 API/구독 구분 불능, OpenAI financial engineering 팀의 2월 공개물, OpenAI 4월 변경의 성격, 이름 없는 회사·Uber·Replit 사례. **이 위키는 어느 원 자료도 열어 보지 않았다.**
>
> ⚠️ **설명란과 자막이 다른 자리 — 자막을 따른다.** ① 설명란 *"사용자당 150~750배 적자 보조금"* — 발화는 *"150s to even 750 subsidized"*(02:55~03:01)로 **배(×)도 사용자당도 없다**(`en`·ko도 단위 없음). ② *"2026년 4월"* — 발화는 *"in April"* 만, **연도 미발화.** ③ 설명란 *"Anthropic의 OpenClaw 차단"* — 발화된 차단 범위는 *"open flow and other third-party agents"*(01:41~01:45)이고 그 대상은 *"the subscriptions plans"* 사용이다(제품 자체 차단이 아니다). ④ *"네 가지 핵심 집행 패턴"* — 넷째가 발화로 특정되지 않는다(⑤절).
>
> ⚠️ **행사·시점.** 행사명·도시 미발화. 현장 단서 *"I flew all the way over to make a kind of a funky statement on an AI conference"*(00:01~00:08), *"I'm the first talk today, so the clicker is not working"*(00:44~00:47). 설명란 AI Engineer 링크 → **추정**. 시점은 *"As I was working through this talk back in April"*(00:54~01:02) — 4월 이후 녹화, 연도 미발화. 업로드 2026-10-11.

## 1. 4월의 가격 비상 — "단 한 달에" (00:47~02:25)

*"in just a you know, matters like 5 weeks everything felt like pricing emergency one after the other"*(01:11~01:18) — 화자는 이것을 *"really are infrastructure emergencies"*(01:27~01:29)로 부른다.

| 회사 | 화자가 말한 사건 (en-orig) | ⚠️ |
|---|---|---|
| [[anthropic|Anthropic]] | *"eliminating access for open flow and other third-party agents to basically use the subscriptions plans"*(01:38~01:47) | *"open flow"* → OpenClaw 판독(02:35 *"open claw"* 와 설명란) |
| [[openai|OpenAI]] | *"changing how the product here is being priced, bumping the price overnight 5 5x, which is quite intense"*(01:48~01:57) | 제품 미특정(*"the product here"* — 슬라이드). 17:20의 *"didn't change the pricing"* 과 긴장(⑤절) |
| GitHub | *"freezing and then completely eliminating access trial access free access to their (…) free plans for for for co-pilot"*(01:57~02:10) | 페이지 없음(지나가는 언급) |

*"all these companies all at once in a single month experienced what it means to actually sell on scale AI and what actually happens when you don't have the fundamentals in place."*(02:13~02:22) — ⚠️ 같은 묶음을 *"5 weeks"* 와 *"a single month"* 로 부른다.

→ [[software-marginal-cost]] · [[bring-your-own-subscription]]

## 2. Anthropic × OpenClaw — 보조금, 그리고 "구분할 방법이 없었다" (02:25~03:30)

- ⭐ 보조금(화자 주장): *"effectively Anthropic was subsidizing every consumption of every user using open claw within the claw claw max[=Claude Max] subscription. So, effectively what the customers were paying daily was, you know, dollars and cents. But on the on the cost side for Anthropic, it was like 150s to even 750 subsidized, which is effectively not an economics that you can scale even for the company at at the size at the scale of Anthropic"*(02:38~03:05) — ⚠️ **150~750의 단위 미발화.**
- ⭐ 진단(화자 주장): *"what it seemed to be a business problem really was an infrastructure problem because Anthropic didn't have a an effective way to delineate between users who are using their APIs and users are using their subscription programs. And so, they had to immediately seize[=cease] and stop access"*(03:08~03:25)
- 위키의 독해: 화자의 논리는 **"가격을 올렸어야 했다"가 아니라 "채널별로 다른 권한을 런타임에 적용할 계층이 없어서 끄는 것 말고 선택지가 없었다"** 이다. 같은 모델을 API(사용량 과금)와 구독(정액)으로 팔면, 서드파티 에이전트가 구독 경로로 들어올 때 그것을 식별·제한하는 것이 entitlement 문제가 된다.

→ [[openclaw]] · [[anthropic]] · [[reserve-then-settle]]

## 3. 사는 쪽의 예산 소진 — "청구서 뒤에 검사한다" (03:30~05:57)

화자가 든 세 사례(⚠️ 전부 출처 미제시, 이 위키 미확인):

- 이름 없는 회사 — *"burning through like half a billion of their AI cloud credits just merely having like a few employees burning through the entire organization contract."*(03:42~03:53)
- [[uber|Uber]] — *"they're basically torched down their entire uh AI usage consumption budget for the year in just a few weeks into the year."*(03:53~04:04)
- Replit — *"giving an example of what could happen if uh a single org has three users that are basically burning down the entire credit pool for Replit for the entire org."*(04:04~04:17) ⚠️ *could happen* — 실제 사건이 아니라 **예시**로 발화됐다.

공통 원인: *"the checks for what you're entitled, what you're allowed to do, whether you're an agent or a user via AI product, happened uh after uh the invoice and not before."*(04:32~04:46) → *"it's sticker shock"*(05:06~05:08). *"none of these companies had in place the financial infrastructure that allows, exactly like banks, guys, to check before we draw down, before we consume"*(05:12~05:25).

→ [[overspending-underusing-loop]] (사는 쪽의 같은 증상) · [[tech-bridge-kimchi-cost-per-task-harness]] (같은 일화의 다른 판본 — 아래 "갈리는 것")

## 4. 사전 검사, 사후 정산 — ATM과 OpenAI의 decision waterfall (05:57~10:04)

- 지금(슬라이드 왼쪽): *"the check and the settlements are happening after after the inference, after the usage is being logged. And that's typically too late."*(06:09~06:18) — 사용자에게 나쁘고, *"also bad for the vendor"* — 자원을 배정하지 않았다면 *"a margin problem"*(06:25~06:35).
- 제안(오른쪽): *"we actually need to enforce and and do this synchronously before we actually update the balances and reconcile and settle in in async way after after effects. So, hot bath[=hot path] actually get checked synchronously, and everything that comes after is basically reconciled after."*(06:48~07:06)
- ⭐ ATM(화자 자신의 비유): *"When you draw the cash, it does the check if you're allowed to draw it doesn't happen after you get the cash. It happens before you draw the cash."*(07:10~07:21)
- OpenAI(⚠️ 화자의 요약, 원문 미확인): *"in February, OpenAI (…) their team called financial engineering. And these guys basically (…) published how they think about the architecture and what they had to build for this to work at the scale of OpenAI."*(07:43~07:59) 내용은 *"a decision waterfall that needs to consider in runtime what is the client, the user, the agent is allowed to do"*(08:06~08:14) — 조건 예: 기능·제품 접근, *"rate limitations under your plan"*, *"in a trial or in a certain promotional program"*(08:21~08:33).
- 화자가 뽑은 세 가지(08:53~09:32): ① *"a single synchronous evaluation. It happens at the request."* ② *"the priority is deterministic"* — 어떤 규칙이 적용되는지 미리 안다 ③ ⭐ *"this is my opinionated view, you can disagree. I don't think this is billing. (…) This is a financial system that actually make decisions ahead of any invoice, ahead of any billing element."*(09:17~09:32)

→ [[reserve-then-settle]] (신규) · [[agent-distributed-systems]]

## 5. 은행에서 빌려 올 특성들 (10:04~14:17)

| 특성 | 화자의 서술 (en-orig) | 위키 메모 |
|---|---|---|
| **동시성 · double spend** | 두 사람이 같은 $10 계좌에서 동시에 인출하는 문제는 은행에선 풀렸다. *"with the AI and agents, it's not that case. You could have whatever, like 10,000 agents trying to reach out to the same dollar pool"*(10:24~10:35) — 잔액이 있어 보여도 동시에 인출하면 *"concurrency become an issue"*(10:46~10:48) | ⚠️ 화자는 이것을 *"a classic double double spend problem. It comes from the accounting world. It's a double entry bookkeeping"*(10:55~11:01)으로 잇는다 — **double spend(동시성)와 double-entry(원장 기록)는 다른 개념**이다 |
| **hold & settle · 멱등성 · 감사** | *"can you basically introduce traits like hold and settle? Think about item potency[=idempotency] and auditability of those um requests"*(11:22~11:32) | [[agent-distributed-systems]]의 멱등성이 **돈의 경로**에 그대로 온다 |
| **출처가 다른 크레딧의 차감 순서** | *"say I have a pool of (…) 1,700 credits, uh, but they're not the same (…) Each one of them is sourced from a different, uh, source."*(12:04~12:16) 먼저 받은 것부터? 프로모션 것부터?(12:19~12:26) *"Most companies today try to solve it like a single integer, uh, databases, and that's not really going to work"*(12:30~12:37) | 은행의 직불·현금·저축 계좌 비유(11:50~12:01) |
| **계층적 크레딧 풀 · 예산 · 지출 한도** | 예전 소프트웨어 소비는 사용자·조직뿐인 *"flat"* 구조였다. *"today, I think, effectively, credit pools are no longer flat"*(13:03~13:08) — *"governance, different logics, allocations, budgets, spend caps"*(13:14~13:18). 연간 선약정 계약의 승인자는 *"They want to know who actually used them, which team, which users, uh which agents"*(13:39~13:46) | 사는 쪽의 요구가 **파는 쪽의 인프라 요구**로 바뀐다 |

## 6. 패턴과 마무리 (14:17~18:59)

*"four patterns that keep repeating themselves, and they're very very much alike (…) to the idea of, you know, banking systems."*(14:25~14:31)

1. **추론 전 예약, 사후 정산** — *"being able to reserve before inference and settle actuals after"*(14:34~14:42), 회계·동시 작업 처리에 파급.
2. **VPC 안의 원장·계량** — 지연·비용·데이터 주권 때문에 *"rather to keep the events data inside their VPC"*(15:10~15:15) → *"deploying this this architecture, this ledger, this metering within their VPC"*(15:17~15:23).
3. **에이전트 실행 중 잔액 검사** — *"when agent does something, you don't know in advance what they're ultimately going to do, how that how that task is going to basically cost."*(15:33~15:42) → 일하는 동안 잔액을 계속 검사하고 *"reserve an account for them in advance, and then asynchronously after effect reconcile"*(15:46~15:53).
4. ⚠️ **(미특정)** — 이어지는 것은 *"what you really gain out of it is visibility"*(16:00~16:06): CFO·CIO가 모델·기능·제품별 소비를 보는 것이 *"becoming a table stakes"*(16:15~16:29). 가시성이 넷째 패턴인지 앞 셋의 결과인지 발화로 정해지지 않는다. *"high cardinality graphs and dimensions"*(14:02~14:08)는 *"probably interesting to to talk about"* 하고 넘어갔다.

**가격 변경 = 인프라 변경**(17:19~17:56): *"One of the changes in April that OpenAI did is really they didn't change the pricing. All they did was change the pace in which tokens get burned. So effectively use the same model, we pay the same cost per unit, but we burn more tokens. So that effectively was a pricing change."*(17:20~17:36) → *"it's not just financial changes, it's an infrastructure change."*(17:38~17:42) ⚠️ 01:53의 *"bumping the price overnight 5 5x"* 와 같은 사건인지 화자는 잇지 않는다.

**⚠️ 벤더 피치 — Stripe moment**(17:56~18:59): 2010년대 초 *"this Stripe moment where every company wanted to ship product into the internet and you need to check out"*(18:07~18:14). 지금은 *"feels like the industry really misses that Stripe moment where all these constructs just exist and it's they're so easy to use."*(18:41~18:51) — *"a lot of excitement from our team when it comes to the potential of having such systems ready"*(18:51~18:56). Stigg의 자리(이 계층을 파는 회사)는 설명란과 직함에서만 알 수 있다.

## 이 위키와의 연결

### 이어지는 것

- **[[software-marginal-cost]] — 보조금의 크기에 대한 첫 수치 주장.** [[satya-nadella|Nadella]]는 *"once the subsidy stop[s] for everybody"* 라고만 했고 그 페이지의 유보는 *"누가 지금 보조하고 있는지 말하지 않는다"* 였다. Sasson은 **주체(Anthropic)·경로(Claude Max 구독 안의 OpenClaw)·크기(150~750, 단위 미발화)** 를 말한다. ⚠️ 경쟁 관계 없는 제3자이지만 이 문제를 파는 벤더다.
- **[[overspending-underusing-loop]] — 사는 쪽 증상의 파는 쪽 원인.** 그 페이지의 *청구서에 놀라 긴축* 을 Sasson은 *검사가 청구서 뒤에 오는 구조* 의 결과로 본다(*"sticker shock"*, 05:06~05:08).
- **[[agent-distributed-systems]]** — [[salman-munaf|Munaf]]의 멱등성·부작용 논의가 **돈을 쓰는 부작용**에 그대로 적용된다. 10,000 에이전트가 한 풀에서 동시에 인출하는 그림은 그 페이지의 *확률적 코디네이터* 문제의 재무판이다.
- **[[openclaw]]** — 이 위키에서 OpenClaw는 늘 *사용 사례* 로만 나왔다. 이 소스는 처음으로 **OpenClaw가 Claude 구독으로 돌았고 그 경로가 끊겼다**는 *정책 사건*을 말한다(⚠️ 화자 주장, *"open flow"* 판독 포함). 여전히 제품 자체는 설명하지 않는다.

### 갈리는 것

> ⚠️ **Contradiction: Uber의 예산 소진 기간.** Sasson: *"torched down their entire uh AI usage consumption budget for the year in just a few weeks into the year"*(03:53~04:04). [[tech-bridge-kimchi-cost-per-task-harness]]의 Laura([[cast-ai|Cast AI]]): Uber CTO가 *"in the last four months (…) used the entire budget of anthropic for the entire year"*(00:58~01:06). **몇 주 대 넉 달**, 그리고 Sasson은 공급자를 말하지 않는다(Laura는 Anthropic). 둘 다 출처 미제시 — 같은 보도의 다른 기억일 가능성이 있지만 이 위키는 판정하지 않는다.

> ⚠️ **"5억" 일화 — 세 번째 판본.** Sasson: 이름 없는 회사가 *"half a billion of their AI cloud credits"* 를 *"a few employees"* 때문에 소진, *"the entire organization contract"*(03:42~03:53). Laura: 인도의 한 회사가 *"$500 million on anthropic alone in one months"*. [[mingsheng-hong|Hong]]([[tech-bridge-trusted-throughput]]): *"한 달에 Claude에 5억 달러"*. 세부(국가·공급자·기간·원인)가 서로 다르다 — 같은 사건인지 미확인.

> ⚠️ **방향이 반대인 두 구독 정책.** [[bring-your-own-subscription]]: [[openai|OpenAI]]는 DevDay에서 *ChatGPT 구독을 제3자 앱에 들고 가게* 한다. Sasson이 말하는 [[anthropic|Anthropic]]의 4월 조치는 *서드파티 에이전트의 구독 사용을 끊는 것* 이다(⚠️ 화자 주장). 사실 충돌은 아니지만, Sasson의 진단(*API 대 구독을 구분할 인프라가 없었다*)을 받아들이면 **BYO 구독은 바로 그 구분 — 어떤 채널·앱이 어떤 구독의 토큰을 얼마나 쓰는지 — 을 런타임에 하는 계층을 전제로 한다.** BYO 페이지의 ⚠️ *"메커니즘이 없다"* 에 대한 간접 단서.

> ⚠️ **배급할 것인가.** [[tech-bridge-kimchi-cost-per-task-harness|Kimchi]]의 Laura: *"Our job is to make sure they can use it as much as they want (…) in a completely unlimited fashion"* — 사용 제한은 틀렸다. Sasson: 기업 구매자는 팀·사용자·에이전트별 *"fine-grained control"*·*"spend caps"* 를 원하고(13:14~13:48) 그것이 판매의 기본 요건이다. 층위가 다르다(Laura = 사내 개발자 정책, Sasson = 공급자가 제공할 통제 기능) — 하지만 *통제가 답인가* 에서 정반대에 선다. 둘 다 벤더다(작업당 비용 하네스 vs 과금 인프라).

> ⚠️ **"보조금은 끝난다" 대 무료 토큰.** [[transaction-cut-monetization]]의 [[mark-zuckerberg|Zuckerberg]]는 사용자 쪽 토큰을 대량 무료로 두는 모델을 말했다. Sasson의 Anthropic 사례는 **정액 구독 안의 무제한에 가까운 사용이 지속 불가능했다**는 주장이다 — Nadella 쪽에 선다.

## 해소하지 않고 표시만 한 것

- 150~750의 단위(배수? 달러?) · *"5 5x"* 의 대상 제품과 17:20 *"pace in which tokens get burned"* 변경과의 관계.
- OpenAI financial engineering 팀 2월 공개물의 실체(제목·URL).
- 이름 없는 회사·Uber·Replit 사례의 출처, 다른 두 소스와 같은 사건인지.
- "네 가지 패턴"의 넷째.
- Stigg 제품 기능(발화 없음). 행사명·도시·연도.

## 등장 개체

- 인물: [[dor-sasson]] (신규 제안 — 이름은 설명란에만)
- 조직: [[stigg|Stigg]] (신규 제안) · [[anthropic]] · [[openai]] · [[uber]] · GitHub(페이지 없음) · Replit(페이지 없음) · Stripe(비유, 페이지 없음) · [[ai-engineer|AI Engineer]](⚠️ 설명란 링크만 — 추정)
- 제품: [[openclaw]] · Claude Max(⚠️ ASR 판독, 페이지 없음) · GitHub Copilot(페이지 없음 — [[microsoft-copilot]]과 다른 제품)
- 개념: [[reserve-then-settle]] (신규 제안) · [[software-marginal-cost]] · [[overspending-underusing-loop]] · [[bring-your-own-subscription]] · [[agent-distributed-systems]] · [[transaction-cut-monetization]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=4JfLShdp92k> (19:00, `upload_date` 2026-10-11)
- raw: `01.raw/articles/2026-10-11_모든 AI 기업이 어쩌다 보니 은행을 짓고 있는 이유입니다.md`
- 설명란 링크: <https://www.stigg.io> · <https://x.com/GetStigg> · <https://www.linkedin.com/in/datapm/> · <https://ai.engineer> (⚠️ 열어 보지 않았다)
- 토큰 비용·예산: [[tech-bridge-kimchi-cost-per-task-harness]] · [[tech-bridge-trusted-throughput]] · [[tech-bridge-mousepower-measuring-agents]] · [[tech-bridge-nadella-copilot-autopilot]]
- 구독: [[tech-bridge-altman-devday-dots]] · [[tech-bridge-cooking-with-codex]]
- 분산 시스템: [[tech-bridge-agents-as-distributed-systems]]
- [[tech-bridge]] · [[stigg]] · [[dor-sasson]]
