---
title: "Tech Bridge — 버그 리포트에서 배포까지: '소프트웨어 팩토리'가 바꿀 개발의 미래 (Davis Palmie · Factory): 코딩은 병목이 아니었다 — 기둥을 하나씩 자동화하고, 에이전트 준비도 8기둥을 깔고, 토큰이 아니라 결과를 잰다"
type: source
tags: [software-factory, governing-agents, abstraction-ladder, input-signal-to-production, coding-not-bottleneck, incident-triage, incremental-rollout, model-agnostic, sovereign-deployment, air-gapped, sdlc-integration, surface-agnostic, o-n-to-o-1, governance-standardization, tribal-knowledge, agent-readiness, eight-pillars, agents-md, observability, rbac, least-privilege, validation-gates, outcomes-not-tokens, goodharts-law, token-leaderboards, signal-to-production-time, human-intervention-count, cost-per-pr, model-mixing, uber, microsoft, factory-ai, vendor-pitch, video]
source-url: https://www.youtube.com/watch?v=lnLqwKTPTYU
source-type: video
author: Tech Bridge (한영자막 재배포) · 발표 Davis Palmie([[factory-ai|Factory]] member of technical staff — **자막에서 직접 자기소개**(en-orig *"Davis Palmey"*), 철자 Palmie는 설명란) · 행사명 미발화(설명란 ai.engineer 링크 + #AIEngineer → AI Engineer 계열 추정) · 녹화일 미발화
date-published: 2026-10-15
ingested: 2026-10-16
created: 2026-10-16
updated: 2026-10-16
---

# Tech Bridge — 버그 리포트에서 배포까지: '소프트웨어 팩토리'가 바꿀 개발의 미래 (Davis Palmie · Factory)

[[tech-bridge|Tech Bridge]]가 재배포한 **18:02 단독 발표, Q&A 없음, 공식 챕터 22개.** 화자 [[davis-palmie|Davis Palmie]]는 자막에서 스스로 소개한다. *"I'm Davis Palmey, uh member of technical staff here at Factory. Uh before this, I co-founded Lumetric, which was an agent platform for investment teams that we took through Y Combinator and was acquired by Factory."*(00:00~00:15) 철자 Palmie는 설명란에만 있다. 이 위키에서 [[factory-ai|Factory]] 화자는 두 번째다. 첫 번째는 [[tech-bridge-factory-software-factory|Tereza Tížková 편]](10-01 업로드)이다. 측정 데이터는 거의 없고, **원칙 선언, 자사 기능, 점검표, 지표 이름**으로 이루어진 발표다. 테제는 다음과 같다.

> **엔지니어는 코드를 타이핑하는 사람에서 에이전트를 다스리는(governing) 사람이 되고, 그 에이전트들을 엮은 시스템이 입력 신호(버그 리포트·사용자 피드백)를 프로덕션 코드로 바꾸는 소프트웨어 팩토리다. 코딩은 처음부터 병목이 아니었다. 병목은 리뷰·재현·문서·테스트와 팀 사이의 단절이다. 그러니 한 번에 다 하지 말고 좁고 검증 가능한 기둥(incident triage)부터 자동화해 신뢰를 쌓은 뒤 루프로 묶는다. 바탕에는 모델 비종속·주권적 배포·SDLC 통합, 그리고 사람과 에이전트가 함께 쓰는 길을 포장하는 에이전트 준비도 8기둥이 있다. 잴 것은 토큰이 아니라 결과다.**

> *"Engineers are going from typing code to governing agents."* (01:54~01:59) · *"coding was the easy part. This actually was never the bottleneck."* (04:48~04:53) · *"if your agents and your human engineers are going to walk the same roads, paving them well is doubly useful."* (14:23~14:29) · *"you want to measure outcomes, not tokens."* (16:18~16:22) · *"And don't token max."* (17:43)

새 개념 페이지는 제안하지 않는다. 이 발표의 내용은 대부분 기존 페이지를 보강하는 **새 증언**이다. [[software-factory]]에는 같은 회사의 두 번째 정의가 들어간다. 3원칙이 Tereza와 다르고, 사람의 자리도 다르다. [[agent-readiness]]에는 **8기둥** 목록이 들어간다. Tereza의 5항목, DX의 4항목보다 넓다. 그 밖에 [[trusted-throughput]]·[[effort-output-outcome-mission]]·[[overspending-underusing-loop]](Goodhart, 토큰 리더보드, *"don't token max"*), [[model-mixing-economics]](GPT 5.2와 Opus, 오픈소스 10~30x), [[agent-trust-curve]](좁게 시작해 신뢰를 쌓는다), [[dora-metrics]], [[uber]]·[[microsoft]](제3자 일화)에 들어갈 내용이 있다.

ASR·ko 보정: ko는 **맺음 문장을 뒤집는다**. *"And don't token max."* → **"그리고 아닙니다 / 토큰을 최대화하세요."**(17:40~17:44). *"you can't govern what you can't see"* → **"보이지 않는 것을 다스릴 수 있다"**(14:29~14:33). *"pulled to the highest bar, not the lowest common denominator"* → **"최고 수준으로 격상된 것이 아니라 최소공배수"**(11:48~11:52). *"having to back the right horse is a false choice"* → **"내기를 해야 한다고 생각했어요"**(03:33). *"scanning for secrets or vulnerabilities"* → **"비밀이나 취약점을 만들고"**(10:21~10:23). *"your teams will not have time to build trust in this system"* → **"이 시스템을 믿으세요"**(07:03). 루프 전 단계 조건(*"before you even think about letting the the pipeline loop"*)은 사라진다(07:41). 용어 오역은 이렇다. agent readiness → **"약제 준비"**(13:24), governing agents → **"자치령 대표"**(01:58), sovereign → **"주권 국가"**(08:49), judgment → **"재판"**(15:35), transitive → **"타동사"**(10:58), signal to production time → **"이제 시작할 시간이에요 / 생산에 대한 신호"**(17:01~17:03), Factory → "공장". ko·`en` 공유 오역: *agent readiness* → *"agent preparation"*, *median* → *"mean"*(17:05), *air-gapped* → *"isolated"*(09:10), *self-improvement* → *"improvement"*(07:50). 전체 목록은 raw에 있다.

> ⚠️ **벤더 발표다.** *"At Factory"* 가 들어간 문장이 일곱 곳(02:58, 08:31, 09:00, 12:46, 13:23, 14:50, 16:59)이다. 원칙 셋과 agent readiness가 모두 자사 제품의 기능으로 소개된다. 분리된 피치 구간은 없다.
>
> ⚠️ **수치는 모두 출처·조건이 없다.** *"We found"* GPT 5.2 = 최신 Opus(code review), *"half the price"*(08:13~08:22), 과제·벤치마크·Opus 버전 미발화. 오픈소스 *"10 to 30x cheaper"*(08:23~08:30). Uber CTO *"by April"*·Microsoft 라이선스 회수(02:45~02:56)는 출처 없는 *"headlines"* 다. O(N) → O(1)은 *"In tech terms (…) conservatively"*(11:24~11:30)라는 비유다. 지표 다섯 개(17:02~17:10)는 **이름만** 있고 정의·값·사례가 없다.
>
> ⚠️ **설명란이 발화보다 앞서 간다.** *"들어오는 순간 (…) 자동으로 완성되는"* 은 발화에 없다. 화자는 반대로 점진을 권한다(06:54~07:05, 15:07~15:17). *"벤치마크 점수가 아닌"*, *"결정론적 린터"* 도 발화되지 않는다. 설명란의 *"인간 개입률(Interventions)"* 은 발화에서 *"human intervention count"*(17:04~17:06)다. 전체 대조는 raw에 있다.
>
> ⚠️ **행사·시점.** 행사명·도시·연도는 발화되지 않는다. 설명란의 `https://ai.engineer`·#AIEngineer로 보아 **[[ai-engineer|AI Engineer]] 계열로 추정한다**(확정 아님). 시점 단서는 Uber CTO의 *"by April"* 헤드라인(과거형)과 *"GPT 5.2"* 다.

## 1. 세 시대와 추상화 사다리 — typing code에서 governing agents로 (00:28~02:30)

- 의제: *"the software factory and how you can move towards an autonomous system that translates input signals into production code."*(00:30~00:40)
- 세 시대(00:43~01:19)는 다음과 같다. ① tab autocomplete·token prediction, *"the engineer was still firmly in the driver seat"* ② 파일 생성, *"the software engineer became a bit of a discerning copy paster"* ③ 에이전트, *"They could gather their own context, call tools, and debug their own output."*
- *"You want to look at the speed at which AI engineering is climbing the abstraction ladder. From tokens to files to context, now to entire systems."*(01:27~01:38) ⭐ *"each move up the abstraction ladder has made engineers more valuable, not less."*(01:43~01:49)
- ⭐ *"Engineers are going from typing code to governing agents. And eventually, you'll organize those agents into a system. That's your software factory."*(01:54~02:05)
- 엔지니어의 역할은 *"keeping guardrails tight, catching code drift, and setting the high-level priorities and direction"*(02:08~02:17)이 된다. 그사이 시스템은 *"ingesting input signals like bug reports or user feedback, and outputting production code."*(02:19~02:30)

→ [[software-factory]](§"사람의 자리"의 추상화 사다리, Tereza와 같은 비유) · [[outcome-engineering]]

## 2. 모두가 묻는 네 질문 (02:30~04:46)

1. **비용 폭증**: *"We've all seen the headlines about Uber's CTO blowing through the year's AI budget by April, or Microsoft clawing back cloud code[=Claude Code] licenses to try and cut down on spend."*(02:45~02:56) 답은 다음과 같다. *"At Factory, you're not locked into a single model provider."*(02:58~03:01) *"You want the maximum uh cost efficiency and the minimum effectiveness necessary for each task."*(03:08~03:15) CEO의 말(이름 미발화)도 인용한다. *"if your kid needs a algebra tutor, you can definitely find someone cheaper than Albert Einstein."*(03:19~03:26)
2. **최고 모델 접근**: *"we think that having to back the right horse is a false choice."*(03:35~03:40) 이유는 오픈소스 모델의 성능 향상이다. *"choose the right tool for the right job, or even now have it dynamically routed."*(03:45~03:51)
3. **엔지니어의 미래**: *"the line between product and engineering is blurry. Engineers will now build and maintain the system that's responsible for building your production code"*(04:02~04:14)
4. **조직**: *"team boundaries are also starting to blur, and context needs to flow seamlessly across these boundaries. Information can't be siloed. That was true for humans, but it's especially true for AI agents."*(04:23~04:38) *"Everyone across all your teams will have a shared responsibility for the pillars of the software factory."*(04:39~04:46)

→ [[uber]] · [[microsoft]] · [[claude-code]](⚠️ ASR *"cloud code"*) · [[model-mixing-economics]] · [[automatic-model-routing]](*"dynamically routed"* 한 구절) · [[overspending-underusing-loop]]

## 3. 코딩은 병목이 아니었다 (04:47~06:10)

- ⭐ *"coding was the easy part. This actually was never the bottleneck. Your context is laid out in natural language."*(04:48~04:56)
- 질문을 이어서 던진다. *"what's the median time to review a PR? How long does it take you to reproduce user bug reports or go through and debug code? Who keeps your docs current with every PR, and who keeps it current with every strategy meeting? Who maintains your test suites?"*(05:01~05:19) *"the testing teams and the engineering teams and the product teams are each on their own continent."*(05:19~05:25)
- *"If you pull your Dora metric, the time from code written to time in production, I would bet dwarfs the time actually making those engineering changes."*(05:25~05:35) ⚠️ 화자의 내기(*"I would bet"*)이고 데이터는 없다.
- *"The real need you have today is cohesion across all of these surfaces. Right now, docs will go stale, dead code lingers"*(05:37~05:46) *"this is hard for human engineers, but it is especially more pronounced for agents."*(05:52~05:58)

→ [[verification-bottleneck]] · [[dora-metrics]] · [[software-factory]](Tereza의 *"writing code that's the easy part"* 와 같은 진단)

## 4. 정의와 첫걸음 — incident triage (06:11~07:54)

- 정의: *"the software factory, which is the system of agents that will take you from input signal to production deployment."*(06:11~06:20) 에이전트는 *"customer support, product, engineering, deployment ops"*(06:25~06:31)를 맡고, *"triaging incidents, making plans, creating and updating docs, actually executing the code, reviewing it, testing it, rolling it out, and then monitoring that release."*(06:35~06:47)
- ⭐ 한꺼번에 하지 말라고 한다. *"you don't want to jump into that all at once. For one, it's too heavy of an undertaking, but for two, your teams will not have time to build trust in this system."*(06:54~07:05)
- ⭐ 첫걸음: *"start with something narrow and verifiable, like incident triage. Let your agent read a sentry alert, pull the traces and other context, and then post in Slack, but keep it so your engineers can review this and decide what to do."*(07:06~07:22) *"as more correct diagnoses roll in (…) your team can start to build trust"*(07:24~07:30)
- ⭐ *"each step in the software factory needs careful ownership and monitoring before you even think about letting the the pipeline loop, but once you can tie the output of this system back to the input signal, that's when you unlock organizational self-improvement."*(07:34~07:54)

→ [[agent-trust-curve]] · [[software-factory]] · [[loop-is-the-product]](출력을 입력 신호에 다시 묶는 루프)

## 5. 3원칙 — 모델 비종속·주권적 배포·SDLC 통합 (07:55~09:46)

| 원칙 | 내용 (en-orig) | 자막 |
|---|---|---|
| **model agnostic** | *"different models excel at different tasks and with very different cost efficiencies."* ⚠️ *"We found (…) the same performance on code review with GPT 5.2 as with the latest Opus models, but at half the price."* 오픈소스는 *"10 to 30x cheaper"*. *"Not being locked into a single lab means you unlock the entire Pareto frontier of LLMs."* | 08:01~08:44 |
| **sovereign deployment** | *"You shouldn't have to compromise on your security architecture or your policies to try and fit your AI deployment model in."* *"We support everything from fully managed to bring your own machine to entirely air-gapped."* | 08:46~09:11 |
| **SDLC 통합** | *"These are no longer separate uncoupled concerns. Docs changing should inform your code and vice versa. Planning goals should inform what you test for, not however many communication layers there are"* *"weakness in one means a weakness in the entire system."* | 09:12~09:46 |

→ [[model-mixing-economics]] · [[software-factory]](⚠️ Tereza의 3원칙과 다르다. 아래 "갈리는 것")

## 6. AI-native 조직의 실제 — 하위 팀의 융합과 O(N) → O(1) (09:47~12:21)

- *"the fusion and the incremental automation of many sub-teams under the umbrella of one software factory."*(09:55~10:04)
- 흔한 패턴: Sentry 알림 triage, *"having the agent make diagnosis before the human can even answer the page"*(10:13~10:18). 보안 선제 테스트(secrets·vulnerabilities 스캔). 테스트를 만들고 유지하면서 *"monitoring the ones that are becoming brittle or unneeded"*. 문서를 코드와 회의 채널에 동기화. 코드 리뷰·PR 코멘트·롤아웃·릴리스 모니터링(10:06~10:44).
- 사람의 역할: *"responding, to exercising judgment, and correcting the AI in such a way that it can learn from these mistakes."*(10:49~10:58) *"everything is transitive across sub-teams. An improvement to one group means an improvement to the entire system."*(11:00~11:08)
- ⭐ *"the larger and the more fragmented you are, the more you feel the linear pain of managing teams. In tech terms, your software factory should take this pain from O of N to O of 1 conservatively."*(11:16~11:30) 방법은 다음과 같다. *"You can define your guardrails, your agents, your docs, testing policies, really governance, just one time, and then standardize it across the organization."*(11:32~11:44) 기준은 *"everyone is pulled to the highest bar, not the lowest common denominator."*(11:49~11:53)
- 에이전트가 표면을 가로지르면 *"one place where context can be unified, and you can have executive visibility into how the entire SDLC is performing."*(12:09~12:19)

→ [[harness-as-platform]](한 번 정의해 조직 전체에) · [[shift-left-security]] · [[company-brain]]

## 7. 표면 비종속 — 같은 하네스, 같은 컨텍스트 (12:22~13:03)

- *"just like model agnosticism removes lock-in, your agents should also be surface agnostic."*(12:23~12:31) *"Your teams should not have to compromise on their processes or their tooling to try and fit your AI provider in."*(12:37~12:44)
- *"At Factory, we have agents available everywhere, from remote machines to the CLI to Slack, any tool your teams use."*(12:46~12:54)
- ⭐ *"even though humans and agents may use different surfaces, everything should share the same underlying harness and context."*(12:54~13:02)

→ [[harness-as-platform]] · [[context-engineering]]

## 8. 에이전트 준비도 — 8기둥 (13:04~14:31)

- *"the undertaking of building the Factory will expose tribal knowledge, manual processes, and outdated info. Unblocking these is not only going to help your agents, but it's also going to help your engineering teams."*(13:05~13:21)
- *"At Factory, we have the concept of agent readiness, and we evaluate this based on eight pillars."*(13:23~13:28)

| # | 기둥 | en-orig (13:30~14:18) |
|---|---|---|
| 1 | validation | *"Do you have guardrails like linters and formatters in place?"* |
| 2 | build system | *"Are your build commands in CI well documented?"* |
| 3 | feedback loops | *"Do you have unit and integration tests tight?"* |
| 4 | docs | *"do you have docs like read me's, agents.md files?"* |
| 5 | dev environment | *"Are your dev environments cleanly reproducible such that an agent can use them?"* |
| 6 | code modularity | *"Is your code modular with clear boundaries and rules against sprawl?"* |
| 7 | observability | *"How long does it take you to find out why something went wrong?"* |
| 8 | security | *"are you proactively security scanning so that you don't have to worry about leaked secrets or vulnerabilities?"* |

⚠️ 기둥 이름은 1·2·3·7만 발화된다(*validation*, *build system*, *Feedback loops*, *observability*). 4·5·6·8의 이름은 질문 내용에서 위키가 붙인 것이다. 점수화 방식은 발화되지 않는다.

- ⭐ *"if your agents and your human engineers are going to walk the same roads, paving them well is doubly useful."*(14:23~14:29)

→ [[agent-readiness]] · [[executable-standards]] · [[hard-vs-soft-enforcement]] · [[company-brain]](tribal knowledge)

## 9. 거버넌스·점진 롤아웃·사람의 자리 (14:32~16:10)

- ⭐ *"you can't govern what you can't see, and that's true for agents and human engineers."*(14:33~14:38) *"your engineers must monitor agent performance and control behavior."*(14:43~14:49)
- *"At Factory, every action is auditable. It operates under your standards with role-based access control and least privilege, for example."*(14:50~14:57)
- ⭐ *"That's why you should roll this out incrementally. You want to automate the individual pillars first before you turn this system into a loop."*(15:07~15:17)
- ⭐ *"precise execution does not prevent poor design. It never has. You still heavily need humans in the loop for architecture, for strategy, and for setting direction. Engineers will not be replaced, but judgment and prioritization now beat mechanical implementation skill."*(15:20~15:45)
- *"There will be guardrails to tighten, code that drifts. Humans need to stand as validation gates in this factory, but just like we don't have to feed punch cards into the machine anymore, code does not have to be written by hand."*(15:46~16:03) *"Your team should be able to set the strategy and their risk parameters, and then let agents execute."*(16:04~16:10)

→ [[agent-governance-layers]] · [[least-privilege-connectors]] · [[agent-trust-curve]] · [[taste-vs-judgment]] · [[architecture-as-remaining-art]] · [[risk-proportional-human-review]](*risk parameters*)

## 10. 토큰이 아니라 결과를 잰다 (16:11~17:59)

- ⭐ *"you want to measure outcomes, not tokens. Lines of code and tokens generated are gameable metrics. These are not actually associated with outcomes."*(16:18~16:31)
- ⭐ *"Token leaderboards at big companies just encourage profligate spending. It's Goodhart's law in real time. If you decide to measure token usage, engineers are going to optimize for token usage, and then it's no longer a good metric."*(16:32~16:49)
- *"It's not about who spends the most on tokens. It's about who can get the highest leverage outcomes from that spent."*(16:50~16:58)
- ⭐ Factory가 쓰는 지표: *"signal to production time, human intervention count, median time to repair, shelf life of code, and cost per PR. These are real tangible outcomes."*(16:59~17:13) ⚠️ 정의·값·사례는 없다.
- 맺음: *"agent readiness is really a precursor to effective engineering, whether it's an agent or a human that ends up in that system. Your agents need the exact same careful governance as your engineers, tooling, access levels, systems for review. Don't just turn them loose in your code base. And don't token max. Measure what actually matters."*(17:19~17:48) *"Your end users don't care about how much you're spending on AI."*(17:49~17:53)

→ [[trusted-throughput]] · [[effort-output-outcome-mission]] · [[overspending-underusing-loop]] · [[value-maxing]] · [[dora-metrics]](*median time to repair*)

## 이 위키와의 연결

### 이어지는 것

- **[[software-factory]]: 같은 회사의 두 번째 화자.** 정의의 골격은 Tereza와 같다. 입력 신호에서 프로덕션까지 가고, 코딩은 쉬운 부분이며, 추상화 사다리를 오른다. Palmie가 새로 더하는 것은 셋이다. **도입 순서**(좁은 기둥 → 신뢰 → 루프), **조직 축의 효익**(O(N) → O(1), 하위 팀 융합), **표면 비종속**(같은 하네스·컨텍스트)이다.
- **[[agent-readiness]]: 8기둥.** Tereza의 점검표(재현 환경·테스트·문서·스타일·린터)와 [[tech-bridge-dx-ai-impact-trends|DX]]의 4항목에 **build system(CI 명령 문서화)·observability·security scanning·모듈 경계(rules against sprawl)** 가 더해진다. *"paving them well is doubly useful"*(14:27~14:29)은 Reock의 *"what's good for humans is also good for agents"* 와 같은 결론이다. 세 번째 화자, 두 번째 회사다(Factory는 두 번).
- **[[trusted-throughput]] · [[effort-output-outcome-mission]] · [[overspending-underusing-loop]]: Goodhart의 명시적 인용.** *"It's Goodhart's law in real time."*(16:39~16:41) 토큰 리더보드 비판은 Amazon 리더보드 일화, IBM 해설, Kent Beck의 노력·산출 구분에 이어진다. 지표 쪽의 새 증거는 **이름 다섯 개**다. 그중 *human intervention count* 는 [[tech-bridge-tessl-harness-engineering-factory|Tessl(Knox)]]의 *manual takeovers*·*human PR comments* 와 같은 계열로, **사람의 개입을 세는** 지표다.
- **[[agent-trust-curve]]: 좁고 검증 가능한 곳에서 시작한다.** incident triage에서는 에이전트가 진단하고 사람이 결정한다. 맞은 진단이 쌓이면 신뢰가 쌓이고, 기둥별로 자동화한 뒤 루프로 묶는다(07:06~07:54, 15:07~15:17).
- **[[model-mixing-economics]]: 벤더의 수치 한 쌍이 추가된다.** code review에서 GPT 5.2와 최신 Opus가 같은 성능에 반값이고, 오픈소스는 10~30x 저렴하다고 한다(⚠️ 조건 미발화). Tereza의 라우팅 4단계는 이번엔 *"dynamically routed"*(03:48~03:51) 한 구절로만 나온다.
- **[[uber]] · [[microsoft]]: 제3자 일화.** Uber CTO의 *"by April"* 은 [[tech-bridge-kimchi-cost-per-task-harness|Kimchi 편]]의 *"in the last four months"* 와 기간이 맞는다(1~4월). [[tech-bridge-stigg-ai-companies-building-banks|Stigg 편]]의 *"just a few weeks into the year"* 와는 여전히 어긋난다. Microsoft의 Claude Code 라이선스 회수는 이 위키에 처음 나온다. ⚠️ 셋 다 출처 미제시다.
- **[[dora-metrics]]**: *"the time from code written to time in production"* 이 코드 작성 시간을 *"dwarfs"* 한다는 화자의 내기(05:25~05:35)는 [[verification-bottleneck]]의 조직판이다.

### 갈리는 것

> ⚠️ **Contradiction(같은 회사 안): 3원칙이 다르다.** [[tech-bridge-factory-software-factory|Tereza Tížková]](10-01 업로드)의 3원칙은 **agnostic · autonomous · always improving**이다. Palmie(10-15 업로드)의 3원칙은 **model agnostic · sovereign deployment · SDLC 통합**이다. 겹치는 것은 비종속 하나뿐이다. Tereza의 *autonomous*(*"trust it to run really for a long time"*, *"a year or more"* 무인 예측) 자리에 Palmie는 **배포 주권**을 놓고, *always improving* 자리에 **SDLC 통합**을 놓는다. 두 발표 모두 *"principles"* 라고 부르며 서로를 언급하지 않는다. 회사의 공식 프레임이 바뀐 것인지, 청중(엔터프라이즈 보안·조직)에 맞춘 것인지는 알 수 없다.

> ⚠️ **긴장: 사람은 루프 밖인가 게이트인가.** Tereza는 사람을 *"monitor and decide what to build"* 하는 루프 밖 감독자로 둔다. Palmie는 *"Humans need to stand as validation gates in this factory"*(15:51~15:55)라고 하고, 기둥별 자동화 전에 루프를 돌리지 말라고 한다. 이것은 [[software-factory]]의 Factory·Warp 대비(*"사람 게이트의 위치"*)에서 **Warp 쪽에 더 가깝다.** 다만 Palmie는 *"code does not have to be written by hand"*(16:01~16:03)라고 할 뿐, **코드를 읽으라고는 하지 않는다.** 이 점에서 하루 전 업로드된 [[tech-bridge-horthy-state-of-software-factory|Horthy 편]]의 *"for now we should probably read the code"*(09:01~09:07)와 갈린다. 둘 다 측정은 없다.

> **G2i 편과 같은 문장, 다른 처방.** 하루 전 [[tech-bridge-g2i-generation-cheap-evaluation-expensive|G2i 편]]의 Martinez는 토큰 리더보드를 LOC의 반복으로 풍자하고 *"the future is orchestration with judgment"* 로 맺는다. Palmie도 *"judgment and prioritization now beat mechanical implementation skill"*(15:38~15:43)이라고 하고 토큰 지표를 Goodhart로 부정한다. 차이는 처방에 있다. Martinez는 **사람이 리뷰할 면을 줄이라**고 하고, Palmie는 **결과 지표와 거버넌스 표준화**를 내놓는다. 둘 다 자사 도구로 맺는 벤더 발표다.

## 해소하지 않고 표시만 한 것

- GPT 5.2 대 Opus 비교의 과제·벤치마크·Opus 버전. 오픈소스 10~30x의 기준 모델.
- 지표 다섯 개의 정의(*signal to production time* 의 시작점, *shelf life of code* 의 측정법)와 Factory 고객의 값.
- agent readiness 8기둥의 점수화 방식, Tereza 판본(10-01)과 같은 제품인지 개정판인지.
- Uber·Microsoft 일화의 원 보도. *"As our CEO likes to say"*(03:17)의 CEO 이름.
- Lumetric(철자는 en-orig에만)의 인수 시점. 화자의 Factory 내 역할 범위.
- 회사 도메인: 이번 설명란은 `factory.com`, [[factory-ai]] 페이지는 `factory.ai`(10-02 설명란)를 쓴다. 둘 다 열어 보지 않았다.
- 행사명·도시·녹화일, 슬라이드 내용.

## 등장 개체

- 인물: [[davis-palmie|Davis Palmie]](신규 제안. 자막에서 자기소개, 철자는 설명란) · Factory CEO(⚠️ 이름 미발화) · Uber CTO(⚠️ 이름 미발화, 헤드라인 경유) · Albert Einstein(비유) — 페이지 없음
- 조직: [[factory-ai|Factory]] · Lumetric(화자 전 회사, Factory에 인수 — [[davis-palmie]] 페이지에 합침) · Y Combinator · Slalom(Innovation Lab) — 페이지 없음 · [[uber]] · [[microsoft]] · [[ai-engineer|AI Engineer]](⚠️ 설명란 링크만, 추정)
- 제품·도구: [[claude-code|Claude Code]](⚠️ en-orig *"cloud code"*, 문맥 판독) · GPT 5.2 · Opus(버전 미발화) · Sentry · Slack · CLI · agents.md · READMEs — 대부분 페이지 없음
- 개념: [[software-factory]] · [[agent-readiness]] · [[trusted-throughput]] · [[effort-output-outcome-mission]] · [[overspending-underusing-loop]] · [[value-maxing]] · [[model-mixing-economics]] · [[automatic-model-routing]] · [[agent-trust-curve]] · [[verification-bottleneck]] · [[dora-metrics]] · [[harness-as-platform]] · [[agent-governance-layers]] · [[least-privilege-connectors]] · [[shift-left-security]] · [[company-brain]] · [[executable-standards]] · [[hard-vs-soft-enforcement]] · [[context-engineering]] · [[loop-is-the-product]] · [[outcome-engineering]] · [[taste-vs-judgment]] · [[architecture-as-remaining-art]] · [[risk-proportional-human-review]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=lnLqwKTPTYU> (18:02, `upload_date` 2026-10-15)
- raw: `01.raw/articles/2026-10-15_버그 리포트에서 배포까지 - '소프트웨어 팩토리'가 바꿀 개발의 미래.md`
- 설명란 링크: <https://factory.com> · <https://x.com/FactoryAI> · <https://www.linkedin.com/in/davispalmie/> · <https://x.com/davispalmie> · <https://davispalmie.com> · <https://ai.engineer> (⚠️ 열어 보지 않았다)
- 같은 회사의 첫 발표: [[tech-bridge-factory-software-factory]]
- 소프트웨어 팩토리의 다른 정의·반론: [[tech-bridge-warp-factory-engineering]] · [[tech-bridge-tessl-harness-engineering-factory]] · [[tech-bridge-pocock-pr-bottleneck]] · [[tech-bridge-kent-beck-craft-augmented-development]] · [[tech-bridge-horthy-state-of-software-factory]] · [[tech-bridge-conductor-orchestras-not-factories]]
- 같은 점검표: [[tech-bridge-dx-ai-impact-trends]] · 같은 Goodhart 비판: [[tech-bridge-tokenmaxxing-to-valuemaxxing]] · [[tech-bridge-g2i-generation-cheap-evaluation-expensive]]
- Uber 예산 일화의 다른 판본: [[tech-bridge-kimchi-cost-per-task-harness]] · [[tech-bridge-stigg-ai-companies-building-banks]]
- [[tech-bridge]] · [[factory-ai]] · [[davis-palmie]]
