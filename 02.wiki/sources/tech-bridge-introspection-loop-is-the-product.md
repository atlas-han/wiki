---
title: "Tech Bridge — 루프 자체가 제품이다 (Roland Gavrilescu · Introspection): 루프 · 시스템 증류 · valued work per watt"
type: source
tags: [agent-loop, auto-research, evals, llm-as-judge, taste, human-in-the-loop, ab-testing, agent-recipes, self-improvement, harness, video]
source-url: https://www.youtube.com/watch?v=cv2_Lzvd1mk
source-type: video
author: Tech Bridge (한영자막 재배포) · 발표 [[roland-gavrilescu]] ([[introspection-dev|Introspection]] 공동창업자, 전 xAI — 자막은 "Rowland"뿐, 성·회사 표기는 설명란) · 행사는 설명란상 AI Engineer World's Fair (⚠️ 자막에 행사명 없음, 미확정)
date-published: 2026-09-29
ingested: 2026-09-30
created: 2026-09-30
updated: 2026-09-30
---

# Tech Bridge — 루프 자체가 제품이다 (Roland Gavrilescu · Introspection)

[[tech-bridge|Tech Bridge]]가 재배포한 **18:15 무대 발표**(공식 챕터 18개). 화자는 xAI에서 에이전트 인프라를 하다 *"a few months ago"*(00:23) 나와 [[introspection-dev|Introspection]]을 세운 [[roland-gavrilescu|Roland Gavrilescu]]. 발표는 스스로를 *"auto research"* 의 청사진이라 부른다 — *"we think there's a blueprint for 2026 and beyond on how you should think about auto research. And it really comes down to three ideas"*(00:52~00:59).

> **① 루프가 제품이다 — 신호의 품질이 루프의 성공률을, 검증기의 품질이 그 성공의 진위를 정하고, 첫 루프의 산출물을 신호로 되먹이는 두 번째 루프가 개선을 만든다. ② 시스템 증류가 해자다 — 루프가 남긴 것(eval·judge·스킬·프롬프트·하네스 프로필)을 모델·제공자와 무관한 Git 저장소의 "에이전트 레시피"로 버전 관리한다. ③ 최적화할 점수는 valued work per watt — 먼저 가치를 재고, 그 가치를 싸게 얻는지 잰다. 그 사이를 잇는 것은 제작자의 taste: 에이전트가 eval을 만들고, 사람은 보정만 하고, 사용자가 A/B로 동의하는지 확인한다.**

> *"The loop is the product."* (01:04) · *"System distillation is the moat."* (04:11~04:14) · *"You don't need the human to actually build the evals. You need them to calibrate the evals."* (14:45~14:49)

ASR·ko 보정: ko는 ***"You don't need the human to actually build the evals"* 를 "평가는 사람이 하는 것이다"로**(14:47), ***"keep doing this over and over again"* 을 "한 번만 반복"으로**(15:52), **딜러끼리 *"outbid each other"* 를 "서로 협력하여 … 돕는"으로**(02:13~02:16), ***moat* 를 "모드"로**(04:14 · 05:47) 뒤집거나 지운다. *agnostic* → **"회의적"**(05:58), *Cognition* → **"인지 기능"**(09:12), *pi.recipes* → **"라마 파이 레시피"**(08:08), *evals* → **"이메일"**(08:20~08:26), *frontier* → **"국경"**(10:00~10:15), *Introspection* → **"자기 성찰"**(06:43), *It's not just tests* → **"단순히 맛의 문제만은 아닙니다"**(11:01). 그리고 **taste를 "기준"·"판단력"으로** 옮긴다(11:51 · 15:26 · 15:44 · 15:58 · 16:08) — [[taste-vs-judgment]]가 갈라 쓰는 두 말을 합친다. 전체 목록은 raw 파일. **인용은 en-orig에서만** 했다(`en`은 *"PyHarvester"*·*"Harbor for events"*·*"a mode"*·*"not just about taste"*·*"border"* 에서 ko와 오류를 공유 — 독립 트랙 아님).

> ⚠️ **당사자 진술, 측정 없음.** 화자는 레시피 제품(pi.recipes)을 내놓은 회사의 공동창업자이고, 발표 말미는 *"Get in touch"*(18:07)로 끝나는 **영업 성격**이다. **수치·실험 결과가 하나도 없다.** Cursor·Cognition의 *제품 → eval → 모델* 경로(09:12~09:23)도 근거 없이 주장된다.
>
> ⚠️ **"실전 사례"는 가상 시나리오.** 챕터·설명란은 인재 발굴 에이전트를 *"실전 사례"* 라 하지만 자막은 *"Let's take a baseline um agent, which could be a talent sourcing agent"*(12:23~12:26), *"So let's say"*(13:17) — **배포 결과가 아니라 설명용 예시**다.
>
> ⚠️ **화자·행사.** 자막은 *"My name is Rowland"*(00:10)뿐 — **성 Gavrilescu, 철자 Roland, "공동 창업자" 직함은 설명란**(⚠️ 링크 안 열어 봄). 자막 안의 방증은 *"My co-founder and I were in this mythical place called XAI"*(00:10~00:12)와 *"we are introspection"*(06:43). **행사명은 자막에 없다** — 설명란의 "AI Engineer World's Fair"는 확인되지 않는다(→ [[ai-engineer]] 페이지에 연결하지 않고 여기 표시만). *"Are you guys ready for some more loops?"*(00:04~00:07)는 앞 발표들도 루프를 다뤘음을 시사할 뿐이다. 2025를 과거형으로 말하므로(*"skills uh used to be in 2025"* 08:10~08:13) 2026년 발표로 읽힌다(추정). 월·일 미확정.

## 1. 루프가 제품이다 (01:02~04:09)

→ [[loop-is-the-product]] (신규)

**계보**(01:10~01:28): *"everything goes down to RLHF for models"* → *"harnesses and how the model is a commodity and it's all about the harness"* → *"now we're talking about loops and how you should build these loops and not touch code anymore"*. → [[rlhf]] · [[harness-engineering]]

**첫 루프 — Clawbot의 자동차 협상**(01:35~02:43). *"Do you guys remember Clawbot? That was the original I original name of what is now now now known as Open Claw"*(01:35~01:42). *"this guy, AJ, built the first loop around Clawbot"*(01:45~01:47) — 딜러·Reddit 사용자와 대화해 차 할인을 받는 루프:

> *"Go on Reddit, find prices, find inventory, talk to the dealers, put dealers head-to-head and try to figure out how to make them outbid each other, have a verifiable way to know when the price is right, and then lock in. Get the car. And it worked."* (02:05~02:25)

화자는 이것을 *"the first real example of loop is the product and something that probably should be a startup"*(02:33~02:40)이라 부른다. ⭐ 루프 안에 **"가격이 맞는지 아는 검증 가능한 방법"** 이 들어 있다는 점이 뒤의 논지를 미리 보여 준다. → [[openclaw]] · [[verifiable-goals]]

**OODA**(02:50~03:19): *"models have been trained with this loop in mind. And it comes from this idea of OODA loops"*(02:50~02:55), 1970년대 미 공군의 전투기 조종 용어라는 화자의 설명(02:58~03:09, ⚠️ 외부 확인 안 함). *"If you think of models calling tools and taking observations, it's it's what we've been trained on uh as humans, but also as as agents now"*(03:12~03:19).

**신호와 검증기**(03:19~03:49):

> *"what matters here is the quality of the signal determines the uh success rate of the loop and the uh quality of the verifier um is able to calibrate uh if that success is actually correct or not."* (03:33~03:49)

**두 번째 루프**(03:52~04:09): *"what happens when you take that and feed it back into the signal? … how do you generate these artifacts at the end of the first loop to then run a second loop on and have a way to continuously improve"*. → [[generator-evaluator-pattern]]

## 2. 시스템 증류가 해자다 — 에이전트 레시피 (04:11~09:02)

→ [[agent-recipes]] (신규)

*"the ability to understand what went well and wrong in the first loop and know how to process that in the second one"*(04:16~04:25). 루프마다 *"harnesses, profiles, evals, models, resources, tools, and the environment"*(04:32~04:38)에 관한 정보가 생기고, 원하는 것은 *"to keep this portable, to have a way to version this, and to evolve it over time"*(04:42~04:46).

**비유는 RL의 데이터 레시피**(04:49~05:14): 레시피를 계속 바꿔 *"hallucinations … reward hacking"* 을 잡고 최종 데이터 레시피에 이른다. *"We don't have that for harnesses."*(05:10) → [[reward-hacking]]

| 루프에서 나온 것 | 레시피에서 되는 것 | en-orig |
|---|---|---|
| 실패 패턴 | **judge·eval** | *"Failure patterns should become judges and evals."*(06:09~06:11) |
| 반복되는 행동 | **스킬·프롬프트** | *"Repeated behavior should become skills and prompts."*(06:11~06:15) |
| 사용자 불만 | **하네스 확장·메모리** | *"User frustration, extensions and memories to your harness"*(06:13~06:17) |

정의: *"an agent recipe is really something that enables you to create reproducible frontier AI systems"*(05:38~05:43), *"a moat that keeps getting better over time, which is not tied to any platform or any provider. It's something that you control, lives in your company, and is agnostic to the models and providers you use"*(05:49~06:02). 형태는 *"a Git repo"*(06:31~06:34), *"meant to be owned by you, but managed by your agents"*(07:14~07:17).

**구현**(06:54~07:00): *"we built our um approach to recipes on the Pie Harness[=Pi 하네스, 추정] and on Harbor for evals"*. ⚠️ **Harbor**는 이 위키에 [[terminal-bench|Terminal-Bench]]의 실행 환경으로 기록된 이름이다([[self-harness]] 논문) — 같은 것인지는 **추정**. **Pi**는 [[understand-anything]]의 지원 플랫폼 목록에 이름만 있다 — 같은 것인지 **미확정**.

**pi.recipes**(08:05~08:41, 조기 공개): *"It's very similar to skills uh used to be in 2025, but it's going a step forward"*(08:10~08:13) — taste를 eval로 코드화, eval 실행, eval을 개선하는 루프, 신호 처리, *"what are the right tools to work with certain models? How do I have different profiles of the harness to work with different models?"*(08:33~08:38). *"It's still early"*(08:44). → [[agent-skills]] · [[cross-harness-skill-compilation]]

⭐ **레시피는 taste를 옮긴다** — *"we think recipes should be basically encoding the taste of the makers into how you build these agents. And if I want to use someone else's recipe, I should be able to also bring that taste. It's not just the harness, it's not just the model, it's how did you arrive at this particular recipe and why?"*(07:37~07:53). 소유자는 *"the higher taste um personality in the room"*(07:26~07:30), 에이전트는 *"calibrate themselves to to the taste of the of the maker"*(07:32~07:34).

## 3. Valued work per watt (09:05~10:45)

→ [[valued-work-per-watt]] (신규)

> *"Think of how um Cursor and Cognition went from building the best product to then uh building the best evals for the product, and finally building the best models based on the previous two artifacts. We think this is like the recipe for everything going forward."* (09:09~09:27)

코드가 첫 도메인이었고 법률·연구 등으로 간다(09:27~09:38, 도메인 목록은 ASR이 깨져 판독 안 함). *"how much value am I getting per watt? Um how do I measure the value is the first step, and how do I know I'm getting a good deal on that value is the second"*(09:38~09:49).

단계: 기본 하네스·기본 eval → 프런티어(*"you only go through that by running the systems in prod. There's no way you you know what frontier is before you uh you start"* 10:02~10:09) → **경제성**(*"once you've reached frontier, how do we make this … economically viable"* 10:15~10:23). 파인튜닝 API 등 인프라는 이미 추상화됐고 *"It's just that the know-how that uh is not there yet"*(10:42~10:44). → [[cursor]] · [[cognition]]

## 4. 제작자의 taste를 eval로 (10:46~12:15)

→ [[taste-encoded-evals]] (신규)

> *"you didn't really think of them of like, what are they? It's It's not just tests. It's It's really what is the taste of the creator that agents should be able to reproduce and self-improve around."* (10:59~11:08)

*"How How do I make my taste as an artist or as a software developer um something that anyone can download in their brain and be able to be a one-to-one replica to me"*(11:14~11:26). RL은 이제 *"how do we uh turn these um tastemakers into environments and evals around them so then we can move them into the weights"*(11:28~11:39).

세 겹: **worker = 내부 루프**(산출물 생성) · **taste = 산출물을 보고 무엇을 바꿀지 아는 것**(변경 후보 생성) · **experiments = 프로덕션 사용자로 taste를 자기 보정**(11:42~12:15). *"not only the maker is happy through the um offline evals, but the end users are happy as well and they agree with what we consider good"*(12:06~12:15).

## 5. 예시 — 인재 발굴 에이전트 (12:18~16:33, 가상)

| 단계 | 내용 | en-orig |
|---|---|---|
| **베이스라인** | 웹 검색·LinkedIn 도구, [[codex|Codex]]·[[claude-code|Claude Code]]가 대중화한 서브에이전트, 채용 담당자 시스템 지시 | 12:47~13:00 |
| **패턴** | 트레이스에서 공통 행동·사용자 불만을 뽑아 클러스터로. 예: 에이전트가 **빅테크 직원에게 연락**한다 — *"You don't want to try to hire John Carmack, but an agent would think that's oh, John Carmack is great"*(13:25~13:32). *"a behavior that you you'd never think of codifying, but you discover the agent tends to be that"*(13:34~13:42) | 13:05~13:47 |
| **judge·eval 보정** | 궤적을 보고 *"did this agent reach out to Google employees instead of trying to uh find hidden gems on GitHub?"* 를 판정하는 에이전트(14:06~14:19). ⭐ *"the calibration bit and the eval generation bit is not that hard. It it should be doable by agents to build. You just need a human in the loop to say … Do you agree with this judgment?"*(14:20~14:35) | 13:52~14:55 |
| **레시피 후보** | *"the diffs that you really want to taste"*(15:01~15:03), 오프라인 eval 세트 | 14:57~15:08 |
| **프로덕션 A/B** | *"the test here is when you go to prod"*(15:08~15:11) — 사용자가 그 taste에 동의하는가. *"with a multi-arm bandit um scenario, for example"*(15:36~15:39) | 15:09~15:46 |
| **승격** | *"once you validate, 'Okay, I have great taste and my users believe uh I have great taste as well.' That's when you promote"*(15:41~15:48) → 레시피 다음 버전 | 15:42~15:50 |

*"The secret is you keep doing this over and over again"*(15:54~15:55). 비유는 *"Miranda from uh The Devil Wears Prada, right? What would Miranda do uh in certain cases?"*(16:23~16:27).

> **이 발표의 가장 구체적인 문장은 분업이다** — *"You don't need the human to actually build the evals. You need them to calibrate the evals. And agents should be the ones that really take the the the taste of the maker and and put them in into code."*(14:45~14:55). ⚠️ ko는 이 문장을 *"평가는 사람이 하는 것이다"* 로 **정반대로** 옮겼다.

## 6. 맺음 (16:36~18:12)

세 요지를 되풀이한다 — *"You try to automate yourself as the uh as the um higher level judge"*(16:37~16:43), *"the faster you do it uh the the the faster you you build a defensible um approach to to becoming a vertical AI company"*(17:06~17:15), 그리고 가격 차이는 *"basically what people would would switch away from cloud code[=Claude Code] to to something you provide"*(17:31~17:38). 수직 SaaS 회사와 *"agent labs"* 에게 *"auto research labs around their their own products"*(17:57~18:05)를 제안하며 끝난다. → [[automated-ai-research]]

## 기존 위키와의 대조

### 합치하는 것

- **실패에서 judge로, 반복에서 스킬로** — [[skill-self-improvement]](실패 관찰 → 스킬 개선, 사람 게이트)와 [[query-to-skill-distillation]](반복 질의 → 스킬)의 두 경로가 **한 표 안에** 들어 있다(06:09~06:17). 이 소스는 거기에 **사용자 불만 → 하네스 확장·메모리**를 더하고, 셋을 한 Git 저장소로 묶는다.
- **트레이스에서 하네스 개선을 뽑는다** — [[self-harness]]의 *실행 트레이스 → 약점 → 수정안 → 회귀 검증*과 같은 골격. 다른 점은 **승격 게이트가 회귀 테스트가 아니라 사람의 보정 + 프로덕션 A/B**라는 것.
- **평가자 분리** — [[generator-evaluator-pattern]]. 새로운 것은 **judge를 누가 만드느냐**다: 에이전트가 만들고 사람은 *"Do you agree with this judgment?"* 에 답한다.
- **검증 가능한 끝** — 첫 루프(자동차)부터 *"a verifiable way to know when the price is right"*(02:18~02:21). → [[verifiable-goals]]
- **토큰이 아니라 가치** — [[value-maxing]]의 *최적화 대상은 결과*와 같은 방향. 분모를 **토큰이 아니라 와트**로 잡는다. → [[valued-work-per-watt]]

### 갈리는 것

> ⚠️ **Contradiction: taste는 코드화·이식 가능한가.** [[paul-bakaus|Paul Bakaus]]는 *"I don't think taste can be solved at a model level"*([[tech-bridge-skill-engineering-dark-arts]] 56:28~56:34), 취향은 **희소**해서 모두가 쓰면 사라진다고 했다. Gavrilescu는 정반대로 제작자의 taste를 eval로 코드화해 *"anyone can download in their brain and be able to be a one-to-one replica to me"*(11:22~11:26), 레시피로 **남에게 옮기고**(07:44~07:47), RL로 **가중치에 넣는다**(11:28~11:39)고 본다. 둘 다 측정이 없다. [[taste-vs-judgment]]에 여섯 번째(혹은 일곱 번째) 입장으로 기록.

> ⚠️ **Contradiction: 누가 eval을 쓰는가.** [[skill-evals]]([[lauren-tan|Lauren Tan]])·[[skill-self-improvement]]는 **사람이 eval·반영을 관리**하는 쪽이다. 이 소스는 *"the calibration bit and the eval generation bit is not that hard. It it should be doable by agents to build"*(14:20~14:28) — 사람은 **판단에 동의하는지만** 답한다. [[query-to-skill-distillation]]의 *게이트가 없다* 유보와 달리 게이트는 있다(사람 보정 + A/B). 하지만 사람 보정이 **judge 한 개당 질문 하나**로 충분하다는 근거는 없다.

- **해자는 어디 있나** — [[company-knowledge-moat]]([[andrew-qu|Andrew Qu]])는 해자를 **회사 고유 맥락 지식**에 둔다. Gavrilescu는 **맥락이 아니라 그것을 증류하는 과정·산출물(레시피)** 에 둔다 — *"lives in your company"*(05:56~05:59)라는 점은 같다. 모순이라기보다 **같은 자산의 다른 형태**. ⚠️ 위키의 정리.
- **"loops … not touch code anymore"**(01:25~01:28) — [[harness-engineering]]의 *RLHF → 하네스 → 루프* 서사를 화자가 한 줄로 요약한다. 이 위키의 [[tools-and-context-over-harness]](하네스는 고정)와는 **초점이 다르다** — 여기서 하네스는 **레시피 안의 버전 관리 대상 하나**(프로필별)다.

## 해소하지 않고 표시만 한 것

- **행사** — 설명란 AI Engineer World's Fair, 자막 없음. [[ai-engineer]]에 소스로 올리지 않았다.
- **AJ가 누구인지, "첫 루프"라는 주장** — 성·링크 없음. OpenClaw의 옛 이름 **"Clawbot"** 철자도 en-orig ASR 그대로이고 확인하지 않았다.
- **OODA의 기원**(02:58~03:01) — 화자 발화 그대로.
- **Pi 하네스 · Harbor의 정체** — *"Pie Harness"* 는 ASR, pi.recipes와 이름이 같다는 것까지. Harbor가 Terminal-Bench의 Harbor와 같은지 추정.
- **pi.recipes의 실체** — 형식·예시·라이선스를 말하지 않는다. *"It's still early"*. 이 위키는 사이트를 열어 보지 않았다.
- **Cursor·Cognition의 경로** — 근거 없음. [[cursor]]의 자체 모델 Composer와 방향은 맞지만 *"best evals"* 단계는 이 위키에 기록이 없다.
- **"per watt"의 측정 방법** — 와트를 실제로 어떻게 재는지(전력인지 비용의 비유인지) 말하지 않는다. 17:31~17:38에서는 **가격 차이**로 바뀐다.
- **A/B의 설계** — 멀티암 밴딧이라는 단어뿐. 표본·지표·기간 없음.
- **"the first two artifacts"로 모델을 만든다** — 파인튜닝 경로의 비용·데이터 조건 없음.

## 등장 개체

- 인물: [[roland-gavrilescu]] (신규) · AJ(미확인) · John Carmack(예시) · Miranda(*The Devil Wears Prada*, 비유)
- 조직: [[introspection-dev|Introspection]] (신규) · xAI(자막 *"XAI"*, → [[spacex]] 참고) · [[cursor]] · [[cognition]] · 미 공군(OODA) · Reddit · LinkedIn · Google · GitHub
- 제품·도구: pi.recipes (→ [[introspection-dev]]) · Pi 하네스(추정) · Harbor · [[openclaw]](Clawbot) · [[claude-code]] · [[codex]] · Mac mini
- 개념: [[loop-is-the-product]] (신규) · [[agent-recipes]] (신규) · [[valued-work-per-watt]] (신규) · [[taste-encoded-evals]] (신규) · [[taste-vs-judgment]] · [[generator-evaluator-pattern]] · [[verifiable-goals]] · [[self-harness]] · [[skill-self-improvement]] · [[query-to-skill-distillation]] · [[skill-evals]] · [[harness-engineering]] · [[rlhf]] · [[reward-hacking]] · [[value-maxing]] · [[company-knowledge-moat]] · [[automated-ai-research]] · [[agent-skills]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=cv2_Lzvd1mk> (18:15, `upload_date` 2026-09-29)
- raw: `01.raw/articles/2026-09-29_루프 자체가 제품입니다 — xAI 출신 창업자가 밝히는 차세대 AI 에이전트의 핵심.md`
- 설명란 링크: <https://x.com/rolandgvc> · <https://www.linkedin.com/in/roland-gavrilescu/> · <https://www.introspection.dev/blog> (⚠️ 열어 보지 않았다)
- 같은 주제: [[tech-bridge-agents-vs-humans-optimizer-speedrun]] · [[tech-bridge-skill-engineering-dark-arts]] · [[tech-bridge-lauren-tan-trusting-agents]] · [[self-harness-paper]]
- [[tech-bridge]] · [[roland-gavrilescu]] · [[introspection-dev]]
