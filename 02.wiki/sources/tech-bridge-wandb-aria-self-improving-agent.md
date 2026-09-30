---
title: "Tech Bridge — 스스로 개선되는 AI 에이전트는 어떻게 만들었나 (Weights & Biases · ARIA): 프로덕션 트레이스를 eval 태스크로 되돌리는 플라이휠"
type: source
tags: [evals, agent-harness, production-traces, eval-flywheel, observability, simulation, hill-climbing, self-improvement, yaml, sandbox, weights-and-biases, weave, video]
source-url: https://www.youtube.com/watch?v=kJj9sHyiRHI
source-type: video
author: Tech Bridge (한영자막 재배포) · 발표 [[zubin-aysola]] ([[weights-and-biases|Weights & Biases]], ARIA 에이전트 — 자막 ASR "Zuban Isaola", 표기는 설명란 LinkedIn 슬러그) · 행사명 미발화(미확정)
date-published: 2026-09-29
ingested: 2026-09-30
created: 2026-09-30
updated: 2026-09-30
---

# Tech Bridge — 스스로 개선되는 AI 에이전트는 어떻게 만들었나 (Weights & Biases · ARIA)

[[tech-bridge|Tech Bridge]]가 재배포한 **16:33 컨퍼런스 발표**(공식 챕터 19개). 화자는 [[weights-and-biases|Weights & Biases]](W&B)에서 에이전트 [[wandb-aria|ARIA]]를 만드는 [[zubin-aysola|Zubin Aysola]](설명란 기준 표기). 발표 절반이 라이브 데모다. 이 위키에 **에이전트 제품을 운영하는 쪽이 자기 eval 인프라를 1인칭으로 설명한 소스**가 처음 들어왔다 — 지금까지의 eval 페이지들([[skill-evals]] · [[field-level-unit-test-evals]])은 스킬 작성자·음성 에이전트 쪽이었다.

> **벤치마크·eval·에이전트·그 구성은 서로 공변(covariant)한다. 그러니 프로덕션과 오프라인을 같은 형식으로 기록하고, 두 환경에서 바이트 단위로 같은 에이전트를 돌리고, 프로덕션에서 나온 모든 실패(와 성공)를 오프라인 태스크로 되돌려 hill climb한다. 이제는 그 hill climbing을 에이전트 자신이 한다 — 사람은 개선의 방향과 가드레일을 생각한다.**

> *"benchmarks, evaluations, the agents, and how you configure them are all covariant"* (01:21~01:24) · *"every production miss or every production goodness as well (…) becomes a task for our agent framework"* (12:05~12:11) · *"it doesn't absolve yourself of the thought behind how we want to make improvements"* (14:38~14:41)

ASR·ko 보정: ko가 ***"weren't calling weave.log (…) properly in the sandbox"* 를 "샌드박스에서 올바르게 작동합니다"로**(ko 13:23~13:26 — 데모의 결론이 뒤집힘), ***"I wasn't entirely certain"* 을 "절대적으로 확신합니다"로**(ko 08:02~08:04), ***"offline metrics"* 를 "외부 지표 … 온라인"으로**(ko 02:11~02:12), 태스크 품질을 **제품팀이 검토한다는 문장을 "소비자들이 구매 여부를 결정"으로**(ko 11:31~11:32) 바꾼다. 플라이휠의 핵심 문장(12:05~12:12)은 *hill climb* → **"확장성"**, *agent framework* → **"자치령 대표"** 로 무너졌고 *eval flywheel* 은 **"평가 양식"** 이 됐다. run·execution은 반복해서 **"처형"**, Weave는 **"직조"**, multi-turn은 **"교대 근무"**, rehydrate는 **"수분 보충"**. 전체 목록은 raw 파일. **인용은 en-orig에서만** 했다(`en`은 *"qualified trajectories"*·*"evaluation form"*·*"1B agent"*·GA 시제 오류를 ko와 공유 — 독립 트랙 아님).

> ⚠️ **당사자 진술, 독립 확인 없음.** 화자는 W&B 직원이고 발표는 **W&B Weave·ARIA 홍보**를 겸한다(*"the best observability platform for both production and offline tracing of agents"* 01:57~02:01 — *"in my opinion at least"* 단서 있음; *"I implore you to use weights and biases"* 14:51~14:53). **점수는 화면에만 있다** — 자막 수치는 *"about like 66% performance on some of the tasks"*(04:49~04:50)와 태스크 수 886(11:28)뿐, 무엇의 66%인지·어떤 태스크인지 없다.
>
> ⚠️ **화자 이름 미확정.** en-orig *"my name is Zuban Isaola"*(00:03), `en` *"Zubair Isola"*, ko *"주바이르 이솔라"*. 제목·설명란 본문엔 이름이 없고 **LinkedIn 슬러그 `zubin-aysola`** 만 있다(열어 보지 않았다). → [[zubin-aysola]]
>
> ⚠️ **행사·날짜 미확정.** *"at this conference"*(00:42~00:43), *"code mode here at this conference"*(07:51~07:53), 동료 Tim의 *"main stage yesterday"*(00:11~00:17), ARIA를 *"released to general availability on Monday"*(00:07~00:11) — **행사 이름도 연도도 발화되지 않는다.** 슬라이드 일부는 *"slides that I presented at Nurup's[=NeurIPS]"*(00:32~00:36). 이 채널의 다른 발표처럼 [[ai-engineer|AI Engineer]] 행사일 수 있으나 근거가 없어 연결하지 않는다.
>
> ⚠️ **"하네스를 만드는 이유" 챕터(00:34)는 비어 있다.** 화자가 *"why a software harness (…) Uh, but that's not for here"*(01:07~01:13)라며 넘긴다. 남는 것은 *"pretty strong differences in the way that you package these AI agents if you use them with different tool calls, etc. on a variety of different benchmarks"*(00:48~00:54) 한 문장.

## 1. 문제 — 공변성과 sim-to-real (01:14~01:49)

→ [[research-production-agent-parity]] (신규)

*"the thing that I go to bed thinking about every day"*(01:16~01:19): *"benchmarks, evaluations, the agents, and how you configure them are all covariant"*(01:21~01:24). 셋 중 하나를 바꾸면 나머지의 의미가 바뀐다 — 그래서 *"if you're trying to apply principled evaluations to any sort of system that dynamically changes, you need to have good measurement"*(01:24~01:30), 그리고 *"you really want to see how the system performs in both your production environment and your offline environment"*(01:32~01:38).

RL 쪽 비유: *"if you're RL pilled from a long time ago you might think about like the sim tore[=sim-to-real] gap"*(01:40~01:42) — 시뮬레이션 환경을 실제 환경으로 옮기는 문제.

## 2. Weave — 양쪽을 같은 형식으로 (01:49~02:39)

→ [[wandb-weave]] (신규)

팀이 둘로 나뉜다. 화자 쪽은 *"I build simulation environments, run the Arya agent over them and then track them in weave"*(02:03~02:08), 나머지 절반은 프로덕션 배포 — *"logging the same things in the exact same format so that I can rip those production traces into our environments and then hill climb on them or resolve our errors. And it's a pretty nice flywheel."*(02:16~02:25)

그리고 ARIA는 이제 그 플라이휠을 **스스로 돈다** — *"the thing that we use to now build itself because it's sophisticated enough that it can actually do that offline hill climbing uh by itself"*(02:29~02:35). → [[self-harness]]

## 3. 라이브 데모 ① — ARIA에게 자기 연구를 시킨다 (02:39~04:57)

데모 프로젝트 이름은 *"Arya Researches Arya"*(02:45~02:47). 다른 세션에서 ARIA가 만든 긴 프롬프트로 *"auto research for itself"*(02:51)를 시킨다:

1. W&B **artifact**로 기록된 화자의 코드베이스(= 오프라인 eval 프레임워크)를 가져와(03:00~03:01)
2. 그 코드베이스로 **training job**을 띄우고(03:03~03:09)
3. 프로덕션 트레이스를 검토해 *"add new tasks to hill climb against"*(03:10~03:12)
4. *"try to write a new variant for itself"*(03:21~03:23)

두 번째 탭(프로덕션 쪽, *"a sanitized view of internal customer traces or internal traces on Arya"* 03:27~03:31)에서는 트레이스 하나를 골라 *"hey, take this trace, log it into our offline evals"*(03:59~04:02), *"run the candidate and production agent on it"*(04:06~04:11). 화자는 이것이 *"the tight version of what I do basically every day"*(04:17~04:21)라고 한다. → [[production-trace-eval-flywheel]] (신규)

**야간 CI**: *"a bunch of traces that we have over the last seven weeks of our nightly uh, like CI jobs that run where we evaluate the agent in its production format and other candidate variants that we cut"*(04:34~04:42). *"for a while the CI broke we had Arya have to fix itself last night"*(04:46~04:47). 점수는 *"about like 66% performance on some of the tasks"*(04:49~04:50) — ⚠️ 분모·태스크 미상.

## 4. RL이 아니라 프롬프트·스킬 — 방법론만 RL에서 빌린다 (04:57~05:33)

*"I mostly prompt engineer these days because the sophisticated models are relatively good at performing tasks at weights and biases and so we're really working on building skills for the software agent more than doing reinforcement learning"*(05:09~05:19). 그래도 *"applying the same methodology to how you build the agent so the same robustness of how you simulate environments uh is really helpful"*(05:20~05:27). → [[agent-skills]] · ⚠️ ko는 이 비교(**RL보다 스킬 작성**)를 지웠다.

## 5. 연구·프로덕션 동일성 (05:27~06:23)

→ [[research-production-agent-parity]] (신규)

- *"we benchmark a bite-wise[=byte-wise] identical version of the agent in our production environment and our simulated environment"*(05:27~05:33)
- Weave 로깅과 시스템 설계 덕에 *"our research and production code are exactly the same"*(05:44~05:46)
- ⭐ *"there's like a 4-hour sync job that happens between production to our research environment so that we don't get any drift when you, you know, researchers are cutting new variants of the agent, new skills, etc."*(05:47~05:54)
- 두 층이 *"mirror each other on two sides of the stack from our deployment layer and our offline benchmarking layer"*(05:59~06:02)

⚠️ 설명란의 **"바이트 단위까지 100% 동일"** — "100%"는 발화에 없고, 동일성은 **4시간 주기 동기화**로 유지된다. 즉 연구 쪽 에이전트는 **최대 몇 시간 늦은 프로덕션 복제본**이다(위키의 해석 — 동기화 방향·범위는 말하지 않는다).

## 6. 트레이스를 대량으로 — 창발 속성을 잰다 (06:02~06:58)

팀 내부에 *"run eval commands to generate score trajectories"*(06:07~06:09)를 노출한다. 논지: *"generate a ton of traces and then decide what you're going to do with said ton of traces"*(06:28~06:33) — *"you're measuring emergent properties and then trying to align the agent in particular directions"*(06:35~06:40).

정렬 방법은 둘: 화자가 직접 태스크를 보거나, *"I would ask Arya to review the roll out that it generated for itself or review some other rollout and decide what went wrong or what went well and try to reinforce that behavior through prompting or anything else"*(06:46~06:54). → [[generator-evaluator-pattern]]

## 7. 모델 중립 하네스와 YAML 변형 (06:58~07:47)

→ [[yaml-agent-eval-pipeline]] (신규) · [[harness-engineering]]

- 모델: *"both models offered through coreweave inference models offered through you know the foundation model players"*(07:00~07:07)
- 하네스: *"relatively agnostic software stack for how we treat compaction and how we prepare context and how we assemble UI payloads"*(07:10~07:15)
- ⭐ *"make it very very simple to have lots of mutations of the exact same configuration. You want to basically YAML define different configurations of the agent to sort of get multiple parallel uh variants and then test them all and see what happens"*(07:20~07:31)
- *"if we take an adage from old reinforcement learning training or just simple model training, it's just better to run more experiments than fewer"*(07:34~07:41) — *"that's the thesis behind the agent harness itself too"*(07:41~07:44)

## 8. 제약 없는 샌드박스 (07:47~08:27)

고객에게 *"a sandbox environment that they can do anything they wanted"*(07:59~08:01). 일화: *"prior to yesterday I wasn't entirely certain that Arya was going to be able to do a bunch of parallel executions of itself"*(08:03~08:08) — 그래서 ARIA에게 *"create the sandbox environment uh for itself to run a bunch of parallel executions of its own research loop"*(08:14~08:18)를 시켰다. *"having that unconstrained environment is really useful for getting the agent to do emergent things"*(08:20~08:25). ⚠️ ko는 "확신 없었다"를 **"절대적으로 확신"** 으로 뒤집었다.

> ⚠️ **보안 이야기는 없다.** "무엇이든 할 수 있는 샌드박스"에서 에이전트가 스스로 병렬 실행 환경을 만든다는 말을 하면서 권한·격리·비용 한도는 한 번도 나오지 않는다 → [[credential-injection-outside-sandbox]] · [[prompt-injection]].

## 9. eval 파이프라인 DAG와 채점 (08:37~10:30)

→ [[yaml-agent-eval-pipeline]] (신규)

*"a relatively agnostic DAG"*(08:40) — ML 파이프라인처럼:

| 단계 | 내용 | en-orig |
|---|---|---|
| **구성** | YAML 파일 | 08:42~08:46 |
| **hydrate** | 필요한 라이브 데이터 로드 | *"We hydrate them. So we load the live data that we need to."*(08:46~08:49) |
| **환경 준비** | W&B에선 비싸다 — 프로덕션 데이터, *"full machine learning training logs"*, auto research면 GPU 실행 시뮬레이션까지 → 병렬화 | 08:49~09:04 |
| **rehydrate** | YAML로 못 담는 런타임 구성을 *"hot patch that data back into the config"* | 09:06~09:13 |
| **실행** | *"running the agent is trivial"* — 프로덕션과 byte-wise 동일 버전으로 | 09:13~09:21 |
| **채점** | ⭐ *"scoring is where I spend a lot of my time"* — 측정의 견고성 | 09:21~09:25 |
| **teardown** | 병렬로 돌리니 *"you don't want to clobber your teammates's work"* | 10:17~10:22 |

동료가 하루를 *"thinking about the health of our evaluations and the drift between our evaluations and production"*(09:43~09:47)에 썼다는 Slack 메시지가 화자를 기쁘게 했다 — *"why are things working well why are things not working well what are the gaps that we see in these two patterns"*(09:50~09:53).

**채점 두 방식**(09:55~10:16): **규범적**(*"normatively which gives us basically did we pass a task or not"* 09:59~10:03) + **상대적**(*"relativistically"* — 사용자에게 **질문하는 변형과 안 하는 변형**을 비교해 *"which one behaves better uh with a relative scoring"* 10:03~10:13). *"a pretty traditional formulation from a reinforcement learning standpoint"*(10:13~10:16).

## 10. 태스크 — YAML, 886개 (10:30~11:40)

- *"the email[=eval] tasks are just YAML specifications that we define as a starting condition of an environment with a bunch of user configurations as well as then an ending condition that we sort of want to get to"*(10:33~10:42) → [[verifiable-goals]]
- *"tasks are flows from users"*(10:42~10:45). *"we simulate them in three ways"*(10:45~10:47)라 하고 **두 가지만 설명**: ① 단순 텍스트 지시 ② *"we simulate a language model that has a persona from a user and we ask it, hey, pretend to be this user, ask certain questions in a particular order"*(11:16~11:22) — 다중 턴 시뮬레이션. ⚠️ 세 번째는 자막에 없다.
- ⭐ *"So, we have 886 tasks. We categorize them by levels."*(11:28~11:30) — 설명란 수치와 일치. *"We expose them to our product team so that they can decide whether or not the tasks are good enough or they reflect things that we care about from our benchmarks"*(11:30~11:36). *"And then we just run them a bunch of times."*(11:38~11:39)

## 11. 궤적과 eval 플라이휠 (11:40~12:34)

→ [[production-trace-eval-flywheel]] (신규)

*"the trajectory is like the meat and the data that I live behind"*(11:42~11:44). 프로덕션 트래픽의 트레이스와 오프라인 트레이스 양쪽에서 *"I really try to exploit the behavior patterns from both of those"*(11:44~11:52), 그걸 위해 *"we build tooling ourselves to understand our traces"*(11:53~11:56) — *"behavior trace project"*(11:57).

> *"that's the eval flywheel. So you know fundamentally every production miss or every production goodness as well because I think it's useful to hill climb in a positive direction uh becomes a task for our agent framework."* (12:02~12:11)

**실패만이 아니라 성공도** 태스크가 된다 — 양의 방향으로도 hill climb한다. 점수 화면(12:17~12:31): *"I think the agent is really good at conceptually guiding you. We want to make it better at doing some error analysis for projects"*(12:22~12:26), *"we try to make these as difficult as possible for the agent"*(12:27~12:29).

## 12. 데모 결과 (12:34~14:26)

ARIA가 W&B Reports로 쓴 보고서(12:51~12:53)에 따르면:

1. 방금 기록된 프로덕션 트레이스로 *"It wrote itself a new task, ran it, and then scored it"*(13:00~13:02)
2. *"it ran a real womb[=W&B?] agent trace, turned it into a WBAF regression task. WBAF is the factory that I build, which is the weights and biases agent factory"*(13:10~13:19) — 오프라인 벤치마킹의 이름
3. ⭐ *"It identified that the problem was that we weren't calling weave.log, one of our SDK calls, properly in the sandbox."*(13:22~13:27)
4. *"It replicates the source trace"*(13:27~13:29), *"runs a bunch of variants of the agent to see how it makes itself better"*(13:30~13:33), *"it added a hill climb target uh which was basically like here's what to do to fix it"*(13:35~13:38)
5. 마지막(15:40~16:04): Weave 트레이스의 *"predict and score column"*(15:48~15:49)과 도구 호출들, 그리고 *"the candidate variant just had a tight little prompt that we injected into the system prompt or in one of the skills to sort of solve that exact SDK error uh and mitigate it"*(15:55~16:02)

⚠️ **"스스로 버그를 해결"(챕터·설명란)은 자막으로 확인되지 않는다.** *"how did the prod versus candidate variant perform"*(13:45~13:48)의 답은 화면에만 있다. 자막이 확정하는 것은 **문제 진단 + 완화용 후보 변형(프롬프트 한 조각) 생성 + prod와의 비교 실행**까지다. 또 설명란의 *"SDK 버그"* 와 달리 자막은 **SDK를 샌드박스에서 제대로 호출하지 않은 문제**다. ⚠️ ko는 이 진단을 **"올바르게 작동합니다"** 로 뒤집었다.

> 이 데모의 개선 단위가 **시스템 프롬프트나 스킬에 넣은 짧은 프롬프트**라는 점이 흥미롭다 — 하네스 코드도 가중치도 아니다. [[self-harness]]의 *bounded edit* 과 같은 크기이고, [[automated-ai-research]]의 *"조합·+1은 하지만 발명은 없다"* 와도 어긋나지 않는다. ⚠️ 위키의 정리.

## 13. 사람은 어디에 — "auto mode"의 함정 (13:50~15:40)

*"instead of going back to my cloud[=Claude] code and writing offline benchmarks and trying to think about what I want the agent to do, I'm just going to live in this platform instead"*(13:56~14:02) — 프로덕션 트레이싱 프로젝트와 오프라인 eval 프로젝트 사이를 오간다.

> *"it's really easy to go like auto mode for some of these tasks where you want to just see the agent do everything. And I haven't written a line of code in maybe eight months because I just tell Claude to write all my code for me. And that's a really nice pattern, but it doesn't absolve yourself of the thought behind how we want to make improvements."* (14:27~14:41)

도구가 스스로를 개선하게 하면 *"you get to spend more of your time in the gray of actually trying to think how we make this system better"*(14:44~14:49). 맺음: *"now I get to spend all of my time thinking about how I can make this system reinforce itself better. The tight little guard rails that I can put around it"*(15:27~15:33). → [[verification-bottleneck]] · [[taste-vs-judgment]]

다른 데모 언급(한 문장): ARIA가 *"training machine learning models on H200s running on Corey[=CoreWeave] infrastructure and doing auto research for Karpathy's nanohat[=nanochat]"*(14:59~15:05). → [[andrej-karpathy]] · [[automated-ai-research]]

맺는 말: *"that kind of replication from production to simulation to agent then defining the improvement pattern is the thing that I really would like to leave everybody with"*(16:04~16:11). 그리고 *"So that's coreweave Arya. Uh welcome to Weights and Biases."*(16:14~16:17) — ⚠️ 화자가 ARIA를 **CoreWeave의 것**으로도 부른다(07:04 *"coreweave inference"*, 15:03 *"Corey infrastructure"*). 두 회사의 관계는 자막에 설명이 없고 이 위키는 확인하지 않았다 → [[weights-and-biases]].

## 기존 위키와의 대조

### 합치하는 것

- **[[self-harness]]** — 고정 모델이 **자기 실행 트레이스**에서 약점을 찾고, 하네스(프롬프트·스킬)에 bounded edit을 제안하고, **회귀 태스크**로 검증한다. ARIA 데모는 논문 루프의 **제품판**에 가깝다. 다만 채택(배포)은 사람 팀이 하고, 평가자(태스크·채점)도 ARIA가 일부 만든다(아래 ⚠️).
- **[[skill-evals]] · [[generator-evaluator-pattern]]** — 후보 변형 vs 프로덕션 변형을 같은 태스크에 돌려 비교. [[impeccable|Impeccable]]의 *사용자 역 LLM*(09-28)과 같은 **페르소나 사용자 시뮬레이션**이 여기도 있다(11:16~11:22).
- **[[verifiable-goals]]** — 태스크 = *시작 조건 + 종료 조건* 의 YAML(10:33~10:42).
- **[[automated-ai-research]]** — "auto research"라는 말이 **연구 과제**(nanochat)와 **자기 개선**(ARIA Researches ARIA) 양쪽에 쓰인다. 결과물은 짧은 프롬프트 패치다.
- **[[agent-skills]]** — 화자는 RL보다 **스킬 작성**에 시간을 쓴다(05:16~05:19). 데모의 개선도 스킬/시스템 프롬프트에 들어간다.

### 갈리는 것

> ⚠️ **Contradiction: 하네스를 만들 것인가.** [[tools-and-context-over-harness]]([[ryan-lopopolo|Lopopolo]], 09-23)는 *하네스는 고정하고 도구·컨텍스트에 투자하라*, *"저는 하네스를 만들어 본 적이 없습니다"*. W&B는 **자체 하네스를 만든다** — 에이전트를 어떻게 포장하느냐에 따라 벤치마크 결과가 크게 달라진다는 관찰에서 *"inspired by that"*(00:48~00:59). 다만 **ARIA의 하네스는 곧 제품**이고, 그 하네스도 *"relatively agnostic"*(07:10)이며, 실제 개선은 **프롬프트·스킬(=컨텍스트)** 에 들어간다 — 층을 나눠 보면 충돌은 "누가 하네스를 소유하느냐"에 가깝다. ⚠️ 위키의 정리.

> ⚠️ **작성자 = 검증자 문제의 네 번째 반복.** [[skill-evals]]가 09-12부터 표시해 온 빈자리 — ARIA는 *"wrote itself a new task, ran it, and then scored it"*(13:00~13:02). 태스크·실행·채점이 한 에이전트다. **완화 장치로 말해진 것**은 886개 태스크를 **제품팀이 검토**한다는 것(11:30~11:36)과 사람이 궤적을 직접 본다는 것(06:42~06:46)뿐이고, ARIA가 새로 쓴 태스크가 그 검토를 거치는지는 말하지 않는다.

## 해소하지 않고 표시만 한 것

- **점수 전부** — 7주 CI 그래프, 카테고리별 점수, prod vs candidate 결과가 화면에만 있다. *"about like 66%"*(04:49)의 분모 없음.
- **"스스로 해결"** — 후보 변형이 prod를 이겼는지, 배포됐는지 자막에 없다.
- **4시간 동기화의 방향·범위** — *"between production to our research environment"* 만. 무엇이(코드·스킬·구성) 동기화되는지 없음.
- **세 번째 태스크 시뮬레이션 방식** — *"three ways"* 중 둘만 설명.
- **"levels"** — 태스크 레벨의 기준 없음.
- **ARIA가 쓴 태스크의 검토 여부** — 위 ⚠️.
- **샌드박스의 보안·비용 한도** — 언급 없음.
- **화자 이름·행사·날짜** — 미확정(위). *"Tim"* 미확정.
- **"womb agent"·"WBAF"** — W&B agent 추정, WBAF 공식 표기 미확인.
- **W&B와 CoreWeave의 관계** — 자막은 *"coreweave Arya"* 라고만.

## 등장 개체

- 인물: [[zubin-aysola]] (신규) · Tim(W&B 동료, 미확정) · [[andrej-karpathy]](nanochat 언급)
- 조직: [[weights-and-biases]] (신규) · CoreWeave · NeurIPS
- 제품·도구: [[wandb-aria]] (신규) · [[wandb-weave]] (신규) · W&B Artifacts · W&B Reports · WBAF(weights and biases agent factory) · [[claude-code]] · Claude · H200 · nanochat
- 개념: [[production-trace-eval-flywheel]] (신규) · [[research-production-agent-parity]] (신규) · [[yaml-agent-eval-pipeline]] (신규) · [[self-harness]] · [[skill-evals]] · [[generator-evaluator-pattern]] · [[verifiable-goals]] · [[automated-ai-research]] · [[harness-engineering]] · [[agent-skills]] · [[tools-and-context-over-harness]] · [[verification-bottleneck]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=kJj9sHyiRHI> (16:33, `upload_date` 2026-09-29)
- raw: `01.raw/articles/2026-09-29_스스로 개선되는 AI 에이전트는 어떻게 만들었을까요 — Weights & Biases.md`
- 설명란 링크: <https://www.linkedin.com/in/zubin-aysola> · <https://wandb.ai> · <https://wandb.ai/site/weave> (⚠️ 열어 보지 않았다)
- 같은 주제: [[tech-bridge-skill-engineering-dark-arts]] · [[tech-bridge-agents-vs-humans-optimizer-speedrun]] · [[tech-bridge-lauren-tan-trusting-agents]] · [[tech-bridge-voice-agent-failure-modes]]
- [[tech-bridge]] · [[zubin-aysola]] · [[weights-and-biases]] · [[wandb-aria]] · [[wandb-weave]]
