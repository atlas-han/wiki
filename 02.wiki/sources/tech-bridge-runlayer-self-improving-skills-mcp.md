---
title: "Tech Bridge — 36%에서 100%로: 자기 개선 에이전트는 어떻게 스스로 스킬을 작성할까요? (Rafal Wilinski · Runlayer): 실행 트레이스 증류 + MCP 배포 = 조직 플라이휠"
type: source
tags: [agent-skills, self-improving-agents, skill-distillation, trace-distillation, mcp, skills-over-mcp, distribution-layer, progressive-disclosure, voyager, skill-library, organizational-flywheel, network-effects, moat, prompt-injection, skill-supply-chain, no-human-gate, runlayer, vendor-claim, video]
source-url: https://www.youtube.com/watch?v=jDdgfTp_PXw
source-type: video
author: Tech Bridge (한영자막 재배포) · 발표 Rafal Wilinski([[runlayer|Runlayer]] founding engineer — 직함 발화, 자막엔 이름 *"Rafal"* 만, 성은 제목·설명란에만) · 행사명 미발화(설명란 ai.engineer 링크 + *"expo"* 발화 → AI Engineer 계열 추정) · 녹화일 미발화
date-published: 2026-10-12
ingested: 2026-10-13
created: 2026-10-13
updated: 2026-10-13
---

# Tech Bridge — 36%에서 100%로: 자기 개선 에이전트는 어떻게 스스로 스킬을 작성할까요? (Rafal Wilinski · Runlayer)

[[tech-bridge|Tech Bridge]]가 재배포한 **17:37 발표, Q&A 없음, 공식 챕터 20개.** 화자는 [[runlayer|Runlayer]]의 founding engineer Rafal Wilinski — 자막엔 *"Hi, I'm Rafal. I'm a founding engineer at Rumlayer."*(01:24~01:31)까지만 있고 **성은 제목·설명란에만** 있다. 전직은 *"leading Zapier agents and different AI teams"*(01:34~01:36). **Runlayer는 이 위키에 처음 등장한다.** 테제:

> **스킬은 에이전트가 필요할 때 읽는 playbook이고, 에이전트가 오래 일할수록 초기 궤적을 잡아 주는 스킬의 값이 커진다. 그런데 스킬은 개발자 중심이고, 아무도 playbook을 남기지 않으며, 모든 클라이언트가 지원하지도 않는다. 그러니 MCP를 스킬의 배포 계층으로 쓰고(원격 MCP 서버 = 회사의 source of truth), 스킬은 사람이 아니라 실행 트레이스(성공과 실패 모두)에서 frontier LLM이 증류하게 하라. 이걸 회사 전체의 모든 에이전트·클라이언트로 곱하면 자는 동안 스스로 개선되는 조직 — 모델이 commodity가 된 시대에 경쟁사가 복제할 수 없는 moat가 된다.**

> *"exploration should be turned into reusable procedural knowledge"* (11:12~11:18) · *"We can use MCP as the distribution layer."* (07:49~07:51) · *"it all happens completely autonomously asynchronously without human in loop"* (12:29~12:33) · *"frontier intelligence is rented or borrowed. It can disappear."* (13:54~13:59)

이 위키에 개념 둘이 생긴다 → [[run-trace-skill-distillation]] · [[mcp-skill-distribution]] (둘 다 신규 제안). 그리고 [[skill-self-improvement]]의 경로 목록에 **"게이트 없음"을 명시적으로 설계 원칙으로 말하는** 경로가 붙는다.

ASR·ko 보정: ko는 **결론부를 세 번 뒤집는다** — *"the success rate is the easiest number to show"* → **"성공률이 가장 중요한 수치"**(13:22), *"without ever changing a model"* → **"모델을 절대 바꾸지 마세요"**(17:27), *"one thing that competitor can't copy"* → **"유일한 단점"**(17:31). 사례 문장 *"sometimes it succeeded"* → **"때로는 성공적이지 못하다"**(12:47), *"rented or borrowed"* → **"돈으로 살 수 있다"**(13:54), MCP 사망론의 *"not interested in dealing with oath"* → **"관심이 있습니다"**(07:22). 회사·화자: Runlayer → **"Runway"**(01:28)·⭐ **"PromptLayer"**(06:14, 다른 회사), 화자 → **"아마르 폴"**(`en` *"Ammar Fall"*) — `en`·ko 공유. run → **"사형 집행·처형"**, flywheel → **"핸들"**, prompt injection → **"신속 주사"**(15:24), Voyager → **"보이저호"**, *set its own goals* → **"자신의 회사를 설립"**(10:17). 전체 목록은 raw.

> ⚠️ **36% → 100% — 분모가 없다(제목의 수치).** *"we had uh this task of trying to run some chromium fork inside AWS Lambda and we were trying to do that using sonet 4.6 (…) it's not production ready to have 36% success rate. Um so what we did is we flipped the flag for self-improving agents. Um and once in one run the one of the agent invocations cracked the code our skill distiller create a reusable skill. It was uh then included in all the future runs and the success ratio went to 100%."*(12:36~13:16) — **사내 태스크 하나**, 공개 벤치마크 아님. **실행 횟수(36%의 분모, "all the future runs"의 수)·기간·증류 모델 미발화.** 같은 태스크에서 증류한 스킬을 같은 태스크에 다시 넣었으므로 이 수치가 보여 주는 것은 **일반화가 아니라 "한 번 푼 해법의 재사용"** 이다 — 화자의 테제(*"they don't have to figure out the solution from scratch"* 16:03~16:06) 그 자체이긴 하지만, 증류된 스킬이 *다른* 태스크에서 해가 되지 않는지는 보이지 않는다. 화자 스스로 *"the success rate is the easiest number to show"*(13:22~13:24)라는 단서를 단다. 토큰·비용 절감(13:24~13:42)은 **수치 없음.**
>
> ⚠️ **당사자 진술 — 벤더 발표.** Runlayer 직원이 *MCP 서버를 스킬 배포 계층으로* 와 *"our MCB[=MCP] gateway"*(15:31~15:33)를 처방한다 — 처방과 자사 구현이 겹친다. 자사 서술: 06:13~06:18(*"at run layer we are scanning thousands of skills every day"*) · 08:14~08:18(내부 6개월 운영) · **11:22~13:20**(증류·36%→100%) · **15:11~15:37**(조직 플라이휠). 고객 사례·측정 방법·통제 실험 없음.
>
> ⚠️ **화자 이름.** en-orig *"Rafal"*(01:26)뿐, `en` *"Ammar Fall"*·ko "아마르 폴"은 오인식. 성 Wilinski는 제목·설명란(*"Runlayer의 Rafal Wilinski"*)과 링크 슬러그(`rafwilinski`, `rafalwilinski`, `rwilinski.ai`)에서 — **자막과 충돌하지 않는다.** 회사명은 en-orig에서 *"Rumlayer"*·*"run layer"*·*"run later"* → 설명란 `runlayer.com` 으로 판독. *"introduce myself once again"*(01:23~01:24)의 "again"이 가리키는 앞 소개는 영상에 없다.
>
> ⚠️ **행사·시점.** 행사명·도시·연도 미발화. 설명란 `https://ai.engineer`·AI Engineer 링크 + *"so many people are walking today across the expo"*(16:45~16:49) → **[[ai-engineer|AI Engineer]] 계열 추정**(확정 아님). 시점 단서: Sonnet 4.6 사용(12:45), *"we all miss Fable"*(13:59), *"Opus is really dumb today"*(14:08~14:10), Runlayer 내부 MCP 스킬 배포 *"for the past 6 months"*(08:16~08:18).

## 1. 싱글 플레이어가 아니라 자기 개선하는 회사 (00:00~01:19)

- *"Today I want to talk about self-improving agents but not in a single player mode where just one agent gets smarter. I want to talk about how we can apply that concept and mix it with network effects to get a self-improving company or maybe even an enterprise that self-improves while you sleep."*(00:00~00:19)
- 비유: 어려운 문제를 풀 때마다 *"wrote down exactly how they did that and handed over the playbook to the team"*(00:31~00:33)하는 최고의 엔지니어·영업·변호사. 현실은 *"all that reasoning is just gone when you move on to the next the next task or close the session"*(01:05~01:14).
- *"we already have all the primitives in place to make it happen"*(01:17~01:19).

→ [[agent-fleet-learning]] — "싱글 플레이어"라는 같은 단어(Zuckerberg 편 *"싱글 플레이어 게임"*)를 **조직 내부**에서 푼다.

## 2. 스킬 = playbook, progressive disclosure (01:46~02:39)

- 에이전트를 개선하는 길은 많지만(*"better models (…) better prompting tools, harnesses"* 01:54~01:58) 오늘은 스킬만 — *"because they are super accessible, right? At least in theory."*(02:03~02:05)
- 정의: *"A skill to me is a playbook that essentially agent can read um when it thinks that the knowledge is relevant"*(02:08~02:15). *"progressive disclosure (…) at the very beginning the harness or a client sees just a summary of the skill (…) when it thinks that the knowledge inside the skill can be useful, it can read the whole of the skill, inject it to the main context and based on that knowledge, it can change the trajectory of the agent."*(02:17~02:39)

→ [[agent-skills]] · [[deferred-tool-context]]

## 3. 긴 작업 시간 = 깊은 rabbit hole → 초기 궤적이 중요 (02:41~04:14)

- METR 차트(*"meter benchmark"*, 03:03): *"It measures for how long agents can work independently while still having a decent chance of completing a task. And the word chance is essential here."*(03:06~03:13) ⚠️ 차트 수치는 화면에만, 자막에 없다.
- *"There's only one caveat if that frontier intelligence is not being taken from you. And I'm fable probably just like you."*(03:27~03:34) — ⚠️ en-orig 판독 불확실(아래 §8).
- ⭐ *"If an agent can reason for much longer, it also means that it can dig a really really uh deep rabbit hole. um it can spend hundreds of tool calls trying to defend a wrong thesis reason for hours and the next agent can do exactly the same thing"*(03:41~03:57) → *"the initial trajectory matters a lot and that's why skills are so important because they guide the agent towards the right target otherwise you'll waste time, you'll waste tokens and most importantly you'll also waste money."*(04:00~04:14)

## 4. 다시 알아내고 싶지 않은 지식 (04:17~05:00)

- *"valuable skills are the rituals that nobody wants rediscovered. That knowledge is often not glamorous. It's probably deeply embedded within your company."*(04:17~04:26) 예: 롤백을 위한 스크립트·feature flag 순서, 이탈 직전 엔터프라이즈 고객에게 쓸 정확한 말(04:30~04:42).
- *"That's why I believe so many AIPS PC's[=AI POCs] are failing because you're not giving agents the relevant context and the playbooks how to act within your company."*(04:51~05:00) ⚠️ 화자의 믿음, 근거 미제시.

→ [[company-knowledge-moat]]

## 5. 스킬의 세 문제 (05:03~07:09)

| # | 문제 (en-orig) | 비고 |
|---|---|---|
| ① | *"they are local first and defcentric[=dev-centric]"*(05:10~05:14) — markdown·JSON·CLI·git 저장소. *"the challenge here is how nontechnical people can actually create and share uh the skills."*(05:40~05:45) | 독자는 *"VP of AI or AI adoption lead"*(05:27~05:32) |
| ①' | ⭐ 설치의 위험: `npx skills` — *"That's the only command I know that installs just uh not just a skill but also free prompt injections. um a wild script that requires root permissions and someone else's API key all in one run. Trust me at run layer we are scanning thousands of skills every day and there is really weird stuff inside."*(05:58~06:18) | ⚠️ 스캔 규모·발견 사례 수치 없음 |
| ② | *"often times there's there's no playbook, right? Because it time it takes time and effort and intention and energy to reflect on a problem and leave something useful for posterity behind."*(06:30~06:42) | 저작 비용 |
| ③ | *"not every LLM client support skills"*(06:44~06:50) — *"If you're in cloud[=Claude] ecosystem, it's probably great"*, 그러나 마케팅·HR·법무·재무는 *"probably still using chat GPT or some other weird LM client"*(07:01~07:09) | 클라이언트 파편화 |

→ [[prompt-injection]](스킬 공급망 벡터) · [[agent-org-adoption]]

## 6. MCP = 스킬의 배포 계층 (07:13~09:29)

- MCP 사망론: *"some people proclaimed that thank god MCP is finally dead because I'm not interested in dealing with oath[=OAuth]. I can now hardcode a bunch of CLI commands um hardcode my API key inside markdown file and call it a progress right um but I think everyone missed the point."*(07:17~07:35)
- ⭐ *"Skills can be delivering um the knowledge how to do something and tools gives us capabilities. (…) But MCP can be also used as a protocol to deliver the knowledge to deliver the skills. We can use MCP as the distribution layer."*(07:33~07:51)
- 구조: *"instead of installing skills locally, you can create a remote MCP server which can become the source of truth across your whole company. Clients can connect to that. They can they can search for the right skills. uh server can enforce the policy and make sure that everyone gets the best version of the skill possible depending on a query and for instance the role that they have assigned."*(07:54~08:14) — Runlayer 내부 6개월(08:14~08:18).
- 생태계: *"there's already a working group called skills over MCP and while the exact API is not final direction is clear"*(08:28~08:36). *"while the official spec is leaning towards MCP resources the support for resources is also mixed. So we are going with tools."*(08:43~08:51)
- 효과: ①·③ 해결 — *"it's unified in and works in almost every single client not just developer clients"*(09:07~09:13), 그리고 *"one place to govern and manage what's the knowledge that's getting shared and distributed across your company"*(09:24~09:29).
- ⚠️ ②(아무도 playbook을 남기지 않는다)의 해법을 화자는 **명시적으로 매핑하지 않는다** — 다음 절의 자동 증류가 그 자리로 읽힐 뿐이다.

→ [[mcp-skill-distribution]] (신규) · [[model-context-protocol]]

## 7. 자기 개선 에이전트 — Voyager에서 트레이스 증류로 (09:33~12:33)

- Voyager(2023, *"right after GPT4 was released, so ages ago"* 10:02~10:06): *"they dropped the agent into Minecraft with no instructions. they set its own goals. It just just kept getting better without even touching the weights or or model and the prompts."*(10:12~10:24) 핵심은 skill library — *"when the agent figured out something um it saved the recipe as a code that uh that consisted of the tool calls that lead it (…) to the discovery"*(10:41~10:51), 나중엔 *"retrieve it as a code as a recipe um that can be reused"*(11:03~11:08).
- ⭐ 화자가 가져가는 한 줄: *"exploration should be turned into reusable procedural knowledge"*(11:12~11:18).
- Runlayer: *"we let the agents do the real work and when the run succeeds and when there is something interesting in this run there's multiple tool calls um we just take that trace and we ask frontier LLM to simply distill a skill"*(11:23~11:41).
- ⭐ 실패가 더 많이 가르친다: *"The real sharpening happens when the agent fails. Um so a roundout[=run that] goes sideways is actually the richest signal that you can get because it exposes the missing guardrail, the missing library, some kind of edge case that you haven't thought about up front."*(11:50~12:05) 성공은 스킬을 *"more trustworthy"*, 실패는 *"more robust"*(12:16~12:29).
- ⭐⚠️ *"it all happens completely autonomously asynchronously without human in loop"*(12:29~12:33) — **게이트 부재가 설계 원칙으로 발화된다.**
- ⚠️ 제목은 *"에이전트가 스스로 스킬을 작성"* 이지만 쓰는 것은 일한 에이전트가 아니라 **별도 증류기(frontier LLM, 미특정)** 다.

→ [[run-trace-skill-distillation]] (신규) · [[skill-self-improvement]] · [[query-to-skill-distillation]]

## 8. 36% → 100%, 그리고 "빌린 지능" (12:36~14:25)

- 사례(12:36~13:16)와 ⚠️ 분모 문제는 위 경고 블록. 비유: *"It's like a developer with better attitude towards documentation."*(13:16~13:20)
- *"good skill is narrowing the search space (…) agents starts doing uh stops doing tool calls and it's exploring less branches. it's wast wasting less tokens and and less money."*(13:24~13:42) — ⚠️ 수치 없음.
- ⭐ 더 깊은 이유: *"frontier intelligence is rented or borrowed. It can disappear. I think yeah, we all miss Fable. It was a great model, right? It can deprecate it or it can get dumber. Like we complain every single day on Twitter, on Slack that Opus is really dumb today, right?"*(13:54~14:10) → *"So while we have the access to the best version of that intelligence, we should be using that to discover and persist those useful procedures. We should be building a catalog of how the works gets done inside our company as a collective subconscious."*(14:10~14:25)
- ⚠️ **Fable.** 화자는 [[fable-5-1|Fable]]을 **과거형**(*"It was a great model"*)으로, 빼앗길 수 있는 프런티어 지능의 예로 부른다. 03:31의 *"And I'm fable probably just like you"* 는 같은 맥락(*"if that frontier intelligence is not being taken from you"*)에 있어 *"I miss Fable"* 로 읽힐 여지가 있다(`en` *"fallible"* 은 다른 판독) — **판독 보류.** 위키의 다른 소스([[tech-bridge-death-of-code-review]])는 *"Fable 5 before it got pulled and then unpulled"* 를 말한다. 어떤 사건인지 이 소스도 말하지 않는다.

## 9. 조직 플라이휠 — 네트워크 효과 (14:28~16:17)

- 퍼즐 조각: 스킬(절차 보존·에이전트 개선·모델 안내) · MCP(통합 배포 계층) · 중앙 저장소(지식 베이스, 계속 갱신) · *"the continuous learning flywheel for one agent"*(14:33~14:59).
- *"what happens when you multiply that by every agent and every single client in the entire company?"*(15:05~15:07)
- ⭐ *"At run later[=Runlayer], we called it self-improving organizational flywheel. Um, we group a bunch of similar runs and try to distill a skill. It passes through our various series of checks like whether it's not containing some kind of prompt injection or maybe PII um and bunch of other stuff. Once it's good, it's landing in our skill library and thanks to our MCB[=MCP] gateway, it's being served to each and every client and agent within the company."*(15:11~15:37)
- 결과: *"a constantly evolving knowledge base which is always up to date"*(15:38~15:42) — 누가 DB를 재시작하고 프로덕션을 롤백하는 *"magical commands"* 를 몰라도 *"simply um reach out to the playbook"*(16:06~16:16).
- ⚠️ 단일 실행 증류(§7)와 달리 여기선 **"similar runs"를 묶는다** — 둘의 관계(언제 한 실행으로, 언제 묶어서)는 발화되지 않는다.

## 10. moat — 복제할 수 없는 것 (16:19~17:35)

- *"I believe like 50% of us probably already had an existential crisis thanks to the models"*(16:23~16:27) — ⚠️ 수사, 측정 아님. *"models are becoming commodity. (…) cost of software is going to zero"*(16:30~16:39), expo의 모두가 *"everyone's building the same thing"*(16:49~16:51).
- ⭐ *"I believe the mode[=moat] can be in building this flywheel and distilling the knowledge through this flywheel because it's like your own hard one[=hard-won] lessons distilled governed of how your company uh does things"*(16:55~17:09) — *"raising the floor for everyone across the company"*(17:11~17:15).
- *"it is also a way to be resistant against model intelligence deprecation and it's a great way to lowers your costs without ever changing a model."*(17:19~17:29) *"that's probably one thing that competitor can't copy your internal culture and your identity."*(17:30~17:35)

→ [[company-knowledge-moat]]

## 이 위키와의 연결

### 이어지는 것

- **[[skill-self-improvement]] — 열 번째 경로, 게이트를 지운 쪽.** 이 페이지의 아홉 경로는 실패 관찰·성공 질의·성공 세션·트레이스 분석 엔진 등 **입력**이 달랐다. Runlayer는 입력으로 **성공과 실패를 모두** 쓰고(*"every run or or pass or fail just feeds our distiller mechanism"* 12:07~12:14), 승격은 **자동 검사(프롬프트 인젝션·PII)만** 거친다. Voyager를 계보로 명시한 첫 소스.
- **[[query-to-skill-distillation]]** — Vercel D0은 *실제 질의*, Runlayer는 *실행 트레이스*를 증류한다. 둘 다 사람 게이트 없음. Runlayer는 여기에 **전사 배포(MCP)** 를 붙여 증류의 반경을 한 에이전트 → 회사 전체로 넓힌다.
- **[[agent-fleet-learning]]** — Zuckerberg(Muse)의 *"업계 대부분은 에이전트를 싱글 플레이어 게임처럼 생각한다"* 와 Wilinski의 *"not in a single player mode"*(00:01~00:04)가 같은 프레임이다. Muse는 **사용자 간**(익명화 통찰), Runlayer는 **한 조직 안**(스킬 라이브러리)의 네트워크 효과.
- **[[company-knowledge-moat]]** — Vercel(Andrew Qu)의 *"회사 고유 지식이 수직 에이전트와의 차이"* 를 Runlayer는 **증류 플라이휠 자체가 moat** 로 밀고 간다. ⚠️ 둘 다 그 플랫폼을 파는 쪽이다.
- **[[prompt-injection]] — 스킬 공급망 벡터의 두 번째 증언.** Kaceviča([[tech-bridge-flutter-ai-workflow]])의 *"스킬은 프롬프트 인젝션에 취약"* 에 Runlayer는 `npx skills` 의 *"free prompt injections (…) root permissions and someone else's API key"* 와 *"thousands of skills every day"* 스캔을 더한다(⚠️ 수치·사례 없음). 그리고 **자동 증류 스킬에도 같은 검사를 건다**(15:20~15:27) — 공급망 검사를 *내부에서 생성된* 스킬로 확장한 첫 사례.
- **[[trace-to-memory-loop]]** — LangChain의 *"트레이스는 증거, 걸러야 메모리"* 와 같은 순환. 출력이 메모리 대신 **스킬 파일**이다.
- **[[production-trace-eval-flywheel]]** — W&B·Braintrust는 프로덕션 실패를 **eval 태스크**로, Runlayer는 **스킬**로 되돌린다. 실패를 무엇으로 바꾸는지가 다르다(Introspection의 *"Failure patterns should become judges and evals. Repeated behavior should become skills"* 와 비교하면 Runlayer는 실패도 스킬로 보낸다).

### 갈리는 것

> ⚠️ **Contradiction: 자동 증류 스킬에 사람 게이트가 필요한가.** [[skill-self-improvement]]의 핵심 원칙 — *"하나의 잘못된 결과가 에이전트가 영원히 따르는 규칙으로 자동 설정되는 것을 방지"* (관찰은 자동, 승격은 수동). [[tech-bridge-langchain-learning-agent-memory|LangChain 편]] 교훈 3 — procedural 메모리(지시·스킬) 변경은 커밋 전에 사람에게 보이고 eval로 보호. [[tech-bridge-tessl-harness-engineering-factory|Tessl]] 레지스트리 — *"security reviews, quality reviews, controls for who can publish and update what"*. Runlayer — *"completely autonomously asynchronously without human in loop"*(12:31~12:33), 승격은 인젝션·PII 자동 검사뿐(15:20~15:31), 그리고 결과는 **회사의 모든 클라이언트·에이전트**에 배포된다. 실패 실행에서 증류한 스킬이 틀렸을 때의 회수·롤백, [[skill-evals|회귀 eval]], 스킬 간 충돌 해소는 **발화되지 않는다.** 반경이 가장 큰 경로에 게이트가 가장 적다.

> ⚠️ **Contradiction: MCP는 스킬로 대체되는가, 스킬의 운반체인가.** [[tech-bridge-sdd-full-course|SDD 강좌]](JetBrains)는 *"MCP → CLI + 스킬"* 을 추세로 가르치고, [[tech-bridge-composio-dashboard-is-dead|Composio]]는 스킬을 *"band-aid"* 라 부른다. Wilinski는 MCP 사망론을 *"everyone missed the point"*(07:33~07:35)로 기각하고 **MCP를 스킬의 배포 계층**으로 세운다 — 스킬(지식)과 도구(능력)는 대체 관계가 아니라는 [[tech-bridge-agent-knowledge-four-ways]]의 분업과 같은 쪽이되, 한 걸음 더 가서 *지식 자체도* MCP로 운반한다. ⚠️ 화자는 MCP gateway 벤더 쪽이다.

> ⚠️ **긴장: 스킬은 모델 교체를 견디는가.** Wilinski — 증류는 *"resistant against model intelligence deprecation"*(17:19~17:25), 지능을 빌린 동안 절차를 남겨라. [[harness-pruning]](Anthropic Claude Code 팀) — 하네스 기능은 *"현재 모델이 가지고 있는 몇 가지 오류 모드를 보완하기 위한 것"* 이고 모델이 좋아지면 지운다. 한 모델(Sonnet 4.6)의 실패에서 증류한 스킬이 다음 모델에서 **불필요하거나 방해가 되는지**는 이 소스가 다루지 않는다 — 스킬의 노후화·은퇴 경로가 없다([[tech-bridge-oracle-agent-memory-harness|Oracle]]은 옛 버전 은퇴를 말했다).

> ⚠️ **긴장: 남의 스킬은 위험, 내 에이전트의 스킬은?** 같은 발표가 `npx skills` 로 들어오는 *"someone else's API key"*(06:11~06:13)와 *"hardcode my API key inside markdown file"*(07:25~07:28)를 조롱하는데, 증류 재료인 **실행 트레이스는 자격증명·고객 데이터를 담기 쉽다.** PII 검사(15:24)가 그 자리를 일부 덮지만, 비밀(secret) 검사·권한 범위는 *"bunch of other stuff"*(15:27)에 묻혀 있다.

> **스킬은 누가 쓰나 (2026-09-10 충돌의 연장).** [[agent-skills]]의 Gopal(*"아무도 다른 사람을 위한 스킬을 쓰지 않는다"*) vs Greze(*"에이전트가 궤적 인센티브를 갖는 한"*) — Wilinski의 문제 ②(*"it takes time and effort and intention and energy (…) to leave something useful for posterity"* 06:34~06:42)는 Gopal과 같은 진단이고, 처방은 Greze 쪽(에이전트가 쓴다)이되 **Gopal의 사람 승인 단계는 뺐다.**

## 해소하지 않고 표시만 한 것

- 36% 사례의 실행 횟수·기간·증류 모델·비용 수치. "all the future runs"가 몇 번인지.
- 단일 실행 증류(§7)와 "similar runs" 묶음 증류(§9)의 관계.
- 자동 검사의 *"bunch of other stuff"*, 검사 실패 시 처리, 스킬 버전·롤백·충돌 해소.
- *"I'm fable probably just like you"*(03:31)의 원문, *"pray"*(06:28), *"new alpha"*(15:44).
- *"introduce myself once again"*(01:23)의 앞 소개. 화면의 METR 차트·meme·Voyager 영상(*"you cannot see the video"* 09:56).
- skills over MCP 워킹 그룹의 소속(공식 MCP 프로젝트인지)·현재 상태. Voyager 논문의 저자·출처(화자 미언급).
- Runlayer 제품명·가격·고객. 행사명·도시·녹화일.

## 등장 개체

- 인물: [[rafal-wilinski|Rafal Wilinski]](신규 제안 — 자막엔 *"Rafal"* 만)
- 조직: [[runlayer|Runlayer]](신규 제안) · Zapier(전직, 페이지 없음) · METR(벤치마크 차트, 페이지 없음) · [[ai-engineer|AI Engineer]](⚠️ 설명란 링크 + expo 발화 — 추정) · [[anthropic|Anthropic]](Opus·Fable·Sonnet의 제조사, 간접)
- 모델: [[claude-sonnet-4-6|Sonnet 4.6]](36% 사례의 실행 모델) · [[fable-5-1|Fable]](⚠️ 버전 미발화, "그리워한다") · Opus(버전 미발화, *"really dumb today"* 불평) · GPT-4(Voyager 시점)
- 제품·도구·연구: Voyager(Minecraft 에이전트, skill library — 페이지 없음) · `npx skills`(스킬 설치 CLI) · MCP gateway(Runlayer) · ChatGPT(비개발 부서 클라이언트) · AWS Lambda·Chromium fork(사례 환경)
- 개념: [[run-trace-skill-distillation]](신규 제안) · [[mcp-skill-distribution]](신규 제안) · [[agent-skills]] · [[skill-self-improvement]] · [[query-to-skill-distillation]] · [[agent-fleet-learning]] · [[company-knowledge-moat]] · [[model-context-protocol]] · [[prompt-injection]] · [[deferred-tool-context]] · [[harness-pruning]] · [[trace-to-memory-loop]] · [[production-trace-eval-flywheel]] · [[skill-evals]] · [[agent-org-adoption]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=jDdgfTp_PXw> (17:37, `upload_date` 2026-10-12)
- raw: `01.raw/articles/2026-10-12_36%에서 100%로 - 자기 개선 에이전트는 어떻게 스스로 스킬을 작성할까요? — Runlayer Rafal Wilinski.md`
- 설명란 링크: <https://www.runlayer.com> · <https://x.com/runlayer> · <https://www.linkedin.com/in/rafwilinski> · <https://x.com/rafalwilinski> · <https://rwilinski.ai> · <https://ai.engineer> (⚠️ 열어 보지 않았다)
- 스킬 자동 갱신 비교: [[tech-bridge-six-agent-skills]] · [[tech-bridge-vercel-eve-filesystem-agent]] · [[tech-bridge-oracle-agent-memory-harness]] · [[tech-bridge-langchain-learning-agent-memory]] · [[tech-bridge-tessl-harness-engineering-factory]]
- 자기 개선 에이전트: [[tech-bridge-wandb-aria-self-improving-agent]]
- 네트워크 효과: [[tech-bridge-zuckerberg-muse-personal-agent]]
- MCP vs 스킬: [[tech-bridge-agent-knowledge-four-ways]] · [[tech-bridge-sdd-full-course]] · [[tech-bridge-composio-dashboard-is-dead]]
- 스킬 공급망: [[tech-bridge-flutter-ai-workflow]] · [[tech-bridge-company-brain-security]] · [[tech-bridge-agent-to-agent-as-search]]
- [[tech-bridge]] · [[runlayer]]
