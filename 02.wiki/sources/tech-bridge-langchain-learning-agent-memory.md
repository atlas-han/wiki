---
title: "Tech Bridge — AI 에이전트에 학습하는 메모리를 (Jake Broekhuizen · LangChain): 관찰 ≠ 학습, 읽기·쓰기 순환과 세 교훈"
type: source
tags: [agent-memory, procedural-memory, semantic-episodic-procedural, working-vs-long-term-memory, read-write-cycle, trace-to-memory, observability, sleep-time-compute, human-in-the-loop, langchain, langsmith, context-hub, vendor-claim, video]
source-url: https://www.youtube.com/watch?v=0kVsv2WlL44
source-type: video
author: Tech Bridge (한영자막 재배포) · 발표 [[jake-broekhuizen]] ([[langchain|LangChain]] Labs 리드 — 이름·직함은 제목·설명란에만, 발화엔 "the lab team at Langchain") · 행사명 미발화(설명란 ai.engineer 링크 → AI Engineer 계열 추정) · 녹화일 미발화
date-published: 2026-10-11
ingested: 2026-10-12
created: 2026-10-12
updated: 2026-10-12
---

# Tech Bridge — AI 에이전트에 학습하는 메모리를 (Jake Broekhuizen · LangChain)

[[tech-bridge|Tech Bridge]]가 재배포한 **15:28 단독 발표, Q&A 없음, 공식 챕터 19개.** 화자는 설명란 기준 [[langchain|LangChain]] Labs 리드 [[jake-broekhuizen|Jake Broekhuizen]] — 자막에는 자기소개가 없고(*"And today I want to talk to you about a topic…"* 00:00로 시작), 소속은 *"the lab team at Langchain"*(00:28~00:30)으로만 확인된다. 이 위키에서 LangChain 사람이 직접 말하는 소스는 [[tech-bridge-jev-agent-harness]](오픈 소스 PM) 다음 **두 번째**이고, [[langsmith|LangSmith]]가 링크가 아니라 **발화로 설명되는 첫 소스**다. 테제:

> **관찰(observability)과 학습은 다르다. 트레이스는 무슨 일이 있었는지의 증거일 뿐이고, 그 교훈이 다음 실행이 참조하는 durable context로 바뀔 때만 메모리가 된다. 메모리가 실행을 만들고, 실행이 증거를 만들고, 증거를 걸러 신호를 만들고, 신호로 메모리를 갱신한다 — 이 순환에서 눈에 보이는 개선의 대부분은 procedural 메모리(지시·스킬·규칙)에서 나오며, 그래서 그 변경은 사람이 본다.**

> *"observing them and then turning those observations and those agent experiences into lessons for future runs are obviously very different things."* (02:21~02:30) · *"A trace, a transcript, or a log is evidence of what happened. It only becomes memory when that lesson is converted into durable context that the agent can reference on future runs."* (04:00~04:12) · *"Memory informs the run. The run makes the evidence. We filter that evidence to make signal and then we use that signal to update memory."* (09:26~09:37) · *"It's how experience becomes context."* (15:20~15:21)

이 위키에 개념 하나가 생긴다 → [[trace-to-memory-loop]] (신규 제안). [[agent-memory]]에는 **인지과학의 세 분류(semantic · episodic · procedural)** 와 **working vs long-term** 구분이 한 화자에게서 처음 완결된 형태로 들어오고, *"무엇을 저장할지 누가 정하는가"* 라는 오래된 미해결 항목에 **메모리 종류별로 답을 가르는**(procedural은 사람 검토) 답이 붙는다.

ASR·ko 보정: ko는 **run을 거의 매번 "사형 집행"·"처형"** 으로 옮겨 후렴 *"the next run should be better"* 를 깨뜨린다. 의미를 뒤집은 자리: *more signal and more traces than ever before* → **"신호와 기록은 결코 나타나지 않으며"**(02:41), *update the way that it behaves* → **"세금 정보를 업데이트"**(09:22, 환각), *third level* → **"3분의 1을 차지"**(14:53, 가짜 비율), *should have some level of human in the loop* → **"좀 먹어야 할 것 같아요"**(14:33), *long-running background agents* → **"오래가는 펀드"**(13:30, `en`과 공유), *Context Hub* → **"컨텍스트 센터"**·**"중심 … 정역학"**. en-orig 판독: *"Langmith"* → LangSmith, *"context sub"/"Contexthub"* → Context Hub, *"emails"* → evals. 전체 목록은 raw.

> ⚠️ **당사자 진술 — 화자는 LangChain 사람이고 10:13~12:28은 자사 제품(LangSmith · Context Hub)이다.** 화자 스스로 *"I won't I won't claim it's the only implementation"*(10:13~10:16)로 앞의 일반론과 분리한다. 이 페이지도 **§1~§6(일반론)과 §7(LangSmith 구현)을 분리해서** 기록한다. 금융 도우미 사례에는 고객사 이름·전후 지표가 없다 — 결과는 *"see that its tone changes"*(12:18~12:22) 한 문장뿐.
>
> ⚠️ **화자 신원.** 이름 Jake Broekhuizen과 직함 "LangChain Labs 리드"는 **제목·설명란에만** 있다(LinkedIn 링크는 열어 보지 않았다). 발화로 확인되는 것은 *"the lab team at Langchain"*(00:28~00:30)과 *"my team"* 뿐.
>
> ⚠️ **행사·시점.** *"the reason why we're at this conference"*(02:16~02:20) — 컨퍼런스임은 확인, 이름·날짜는 미발화. 설명란 `https://ai.engineer`·AI Engineer 유튜브/X/LinkedIn 링크 → **AI Engineer 계열 추정**(확정 아님). 업로드 2026-10-11.

## 1. 문제 — 금융 도우미의 말투가 미끄러진다 (00:28~02:12)

- 고객: *"a company in the financial services sector who's building a uh spending, budgeting and non-investment advice agent"*(00:32~00:40). 규제 산업이라 *"strict tone guidelines"*(00:46~00:48)을 따라야 하고, 말투는 *"the context and (…) the memories and (…) the references that it has to its rules and policies"*(01:01~01:09)에서 나온다.
- 실패: *"it would move from being advisory and helpful to actually pointed and directive"*(01:18~01:24) — *"users in your similar situation would generally set a spending cap"* 대신 *"it looks like you need to cancel some subscriptions and move some money into savings"*(01:24~01:32).
- 기존 교정 경로는 수동: *"You have to have someone understand the traces and understand where its tone slipped, make those changes to the context (…) and then make sure that there are no regressions as well."*(01:40~01:53) → *"challenging to scale"*(01:55).
- 목표: *"the system around the agent should be a place where it can continuously learn and benefit from its interactions and its experiences."*(01:58~02:06) — 학습의 자리가 **모델이 아니라 에이전트 주변 시스템**이다.

→ [[continual-learning]](컨텍스트 층) · [[skill-self-improvement]]

## 2. 관찰 ≠ 학습 — 트레이스는 신호가 되어야 한다 (02:12~03:47)

- *"I think we've gotten very good at observing them"*(02:20~02:21) — 트레이스는 늘어나고(*"more signal and more traces than ever before"* 02:38~02:43) 도구 호출·추론·참조한 artifact를 보여준다(02:53~03:00). *"Observability is obviously a critical foundation"*(03:03~03:05).
- ⭐ 문제는 저장 *뒤*: *"If the future context that that agent references never changes, then a misguided skill or instruction will mean that (…) the mistake that the agent makes today will still persist in future runs."*(03:17~03:28)
- 목표: *"a trace stops just being a log and becomes a source of signal."*(03:32~03:37) · *"Agents that are observable tell you what happened. Agents that are adaptive are able to change (…) and guide themselves on the following runs."*(03:40~03:47)

→ [[trace-to-memory-loop]] · [[agent-action-record]](아래 "갈리는 것") · [[production-trace-eval-flywheel]]

## 3. 메모리의 정의와 세 분류 (03:47~05:44)

**정의**: *"the durable context that an agent references that will guide future runs."*(03:54~03:57) — 저장 위치나 출처가 아니라 **다음 실행을 이끄는 지속적 컨텍스트라는 기능**으로 정의한다.

슬라이드의 여섯 항목 *"Facts, preferences, patterns, previous examples, skills, and instructions"*(04:16~04:21)을 *"A taxonomy that we borrow from cognitive science"*(04:25~04:29)로 셋에 묶는다:

| 분류 | 정의 (en-orig) | 담는 것 |
|---|---|---|
| **semantic** | *"what the agent knows"*(04:36~04:37) | *"the facts and the preferences that guide the way that it responds"*(04:41~04:43) |
| **episodic** | *"what the agent has experienced"*(04:51~04:53) | *"the learned patterns that it's seen, past interactions and examples"*(04:55~04:57) |
| **procedural** | *"how the agent should behave"*(05:00~05:02) | *"the instructions, the skills that you're all probably very familiar with and the rules"*(05:05~05:09) |

- ⭐ *"Procedural memory is where actually most of the visible gains come from."*(05:12~05:17) 금융 도우미의 교정도 procedural이었다 — *"We weren't giving it a new fact or we weren't telling it not to use a banned word. We were giving it a rule to follow as it engages with its users."*(05:29~05:38) ⚠️ "대부분"의 근거는 제시되지 않는다.
- 즉 이 화자에게 **스킬·지시도 메모리다**. 사람이 쓴 규칙과 에이전트가 겪은 것을 같은 "메모리" 아래 둔다 — 이 위키의 [[agent-memory]] 첫 정의(출처로 RAG와 가름)와 갈린다(아래).

→ [[agent-memory]] · [[agent-skills]] · [[files-vs-database-agent-memory]](Oracle의 일화·절차 분류)

## 4. working vs long-term (05:44~07:29)

- **working(short-term)**: *"what the agent is referencing in its current run"* — *"intermediate scratch pads (…) tool results (…) the files retrieved"*(05:56~06:05)
- **long-term**: *"what exists typically in some data structure or some store somewhere else that has instructions and skills"*(06:12~06:20)
- 주입 방식은 하네스마다 다르다 — *"Some inject it directly into the prompt. Some will use tools to retrieve that. Some will (…) pull it directly from a store. Some load it through files or some change the runtime state."*(06:38~06:49) 구현이 아니라 **구분**이 중요하다(06:49~07:01).
- ⭐ *"A trace isn't just a record of the final output. It's a record of how our working memory changed over the course of the run. Some part of that should stay as history. Some part of that should become durable long-term context."*(07:11~07:24)

→ [[context-engineering]] · [[push-vs-pull-context-retrieval]] · [[context-resets-and-compaction]]

## 5. 읽기·쓰기 순환과 필터 (07:29~09:46)

- *"It's a readwrite[=read-write] cycle."*(07:44~07:46) — ⚠️ *"you might have heard of sleeptime compute or dreaming. Those terms refer to the way that memory is updated or pulled from long-term into short-term whilst the agent is doing work or actually in some cases while the agent is also not doing work. That's the sleeptime compute."*(07:46~08:03) — 화자는 dreaming을 **작업 중 갱신까지 포함하는 넓은 말**로 쓴다(아래 "갈리는 것").
- **읽기**: 실행 시작 시 장기 → 단기. *"you've probably seen progressive disclosure with agents that actually pull in the relevant skills for a certain task. That's that phase"*(08:18~08:27)
- **증거**: 실행이 트레이스를 남긴다 — 컨텍스트 검색, 도구 호출, 결정, 서브에이전트(08:29~08:42).
- ⭐ **필터**: *"most evidence should stay as history. (…) if we turned all of that evidence into long-term memory, then it would make the agent struggle and it would make it harder to reason over future tasks. And so what I think is really interesting is the filter step."*(08:44~08:59) · *"How do you how do you decide what is useful signal and what should become durable long-term context and how do you decide what should stay as history?"*(09:00~09:08)
- **쓰기**: 신호를 durable context에 다시 쓴다(09:11~09:16). 금융 도우미에서는 *"be measured and not pointed or not directive"*(09:19~09:24)라는 규칙.
- 플라이휠: *"If you can build that flywheel, then we trend towards a place where we can build very reliable and very powerful agents that just feel like they get better with time."*(09:35~09:46) ⚠️ 측정 없음.

→ [[trace-to-memory-loop]] · [[agent-dreaming]] · [[context-rot]](전부 넣으면 추론이 어려워진다)

## 6. 더 단순한 세 칸 — capture · analyze · update (09:46~10:13)

*"capturing what happened, analyzing what might matter and then updating the context so that future runs can use this."*(09:52~10:01) 구현은 *"still evolving"*, 하지만 *"this three-part shape is a really useful starting point."*(10:03~10:10)

## 7. LangSmith · Context Hub 구현 (10:13~12:28) — ⚠️ 당사자 진술

| 칸 | LangSmith 쪽 구성 (en-orig) |
|---|---|
| capture | *"is where our observability comes in"* — 도구 호출·서브에이전트 호출·검색된 컨텍스트(10:24~10:38) |
| analyze | *"something new that I'm really excited about"*(10:41~10:44) — *"that intelligent process that's doing the background analysis (…) to extract signal from traces based on the things that matter to you"*(10:44~10:51) |
| update | *"promoting that signal to the memory store or the point of reference that the agent will use for future runs and that is Langmith's[=LangSmith's] context hub"*(10:51~10:59) — *"a remote store where you can now go and update what's in that so that the agent can pull that down the next time it runs"*(11:08~11:14) |

**금융 도우미에 적용**(11:27~12:28): 실행 시 Context Hub에서 *"its instructions, its skills, relevant markdown files that matter to it, policies and rules"*(11:42~11:51)를 로드 → 트레이스가 *"failed tool calls or user corrections or in this case it flagged where our tone strayed"*(11:55~12:02)를 보여줌 → (엔진이) *"looks for patterns and then identifies where different static skill markdown files that are based in Contexthub need to be changed or promoted and it'll make that change"*(12:02~12:13) → 다음 실행에서 말투 변화 확인(12:16~12:23).

- ⚠️ 분석 단계 *"engine"* 의 제품명·출시 상태는 발화되지 않는다(*"something new"* 뿐). 변경을 **누가 승인하는지도 이 구간에서는 말하지 않는다** — *"it'll make that change"*. 교훈 3(§8)의 사람 검토와 이 구간의 자동 반영이 어떻게 맞물리는지는 미발화.
- 저장 형식은 **마크다운 스킬 파일**(*"static skill markdown files"*) — [[agent-dreaming]](Anthropic, 디렉터리의 마크다운)과 같은 형식, 위치는 원격 스토어.

→ [[langsmith]] (신규 제안) · [[langchain]] · [[agent-skills]]

## 8. 세 교훈 (12:28~14:59)

**① 대부분은 history로** — agents produce *"so much we call it exhaust or (…) feedback. Not everything should become a memory update."*(12:41~12:47) *"most trace data actually should stay as history, as referenceable history. Some some might become data sets to do offline evaluations (…) A small (…) subset should end up becoming what changes your agent's memory."*(12:57~13:13) → 트레이스의 **세 갈래 경로**(history · eval 데이터셋 · 메모리).

**② 캐시와 hot path — 갱신이 안 보이는 함정** — *"particularly for longunning[=long-running] background agents (…) you make some memory updates in the beginning of its operation, but because of the runtime state and because of the way that it's accessing memory, you don't actually access that or that's not available to it for future runs."*(13:30~13:47) → *"understanding what you can cache, what you can't cache to be able to make sure that memory updates are available for future runs, very important."*(13:47~13:55) 화자 본인의 경험담(*"I was banging my head on a wall for a while"* 13:55~13:58).

**③ 무엇을 self-update로, 무엇을 사람 검토로** — *"open core[?] and you know Hermes agent and (…) a lot of agents that are becoming widely popular that sort of do this self update process"*(14:06~14:16) → *"what do you make self-updatable as opposed to what do you make something that needs human review?"*(14:19~14:21)
- ⭐ *"if we're talking about procedural memory with instructions and policies and tone guidelines, those are probably going to drive about 75% of the behavior of my agent. And so that actually probably should have some level of human in the loop"*(14:23~14:37) — ⚠️ **75%는 화자 자신의 에이전트에 대한 추정**(*"probably"·"about"*), 측정 없음.
- 방식: *"surface the changes that you make to the parts of the agent's memory that are procedural before actually committing those and (…) putting those in the (…) agent sort of like hot reload path."*(14:37~14:47)
- *"So protecting important behavior with emails[=evals] is I guess another really important (…) third (…) level"*(14:50~14:55).

→ [[no-silent-write]] · [[skill-evals]] · [[risk-proportional-human-review]] · [[agent-distributed-systems]](캐시) · [[openclaw]](⚠️ "open core" 판독 미확정)

## 9. 마무리 (14:59~15:28)

*"the next run should be better. Memory allows us to do this."*(15:01~15:05) · *"it's more than just a place to store information. It's how experience becomes context. And then that context is how our next runs get the chance to improve."*(15:16~15:25)

## 이 위키와의 연결

### 이어지는 것

- **[[agent-memory]] — 분류의 완결판.** [[tech-bridge-oracle-agent-memory-harness|Oracle(Martinez)]]는 단기/장기 + 일화·절차를 **저장 위치**(파일 vs DB)와 묶었고, 이 소스는 **semantic · episodic · procedural** 셋을 다 놓고 *어느 것이 행동을 바꾸는가*(procedural)로 무게를 준다. 미해결 *"무엇을 저장할지 누가 정하는가"* 에 **필터 단계**(대부분 history)와 **종류별 게이트**(procedural → 사람)라는 답이 붙는다.
- **[[skill-self-improvement]] — 아홉 번째 경로(벤더 제품형).** 트레이스 → 분석 엔진 → Context Hub의 스킬 마크다운 변경. 대상이 스킬 파일이라는 점에서 Tessl의 meta loop(*"Let's update a skill"*, [[tech-bridge-tessl-harness-engineering-factory]])·Warp observer와 같은 자리이고, **사람 게이트를 메모리 종류로 가른다**는 점이 새롭다.
- **[[agent-dreaming]]** — Anthropic dreaming의 *"propose → 사람 수락"* 과 교훈 3의 *"surface the changes (…) before actually committing"* 이 같은 게이트다. 둘 다 마크다운 파일을 쓴다.
- **[[production-trace-eval-flywheel]]** — W&B는 트레이스 → eval 태스크 **하나의 경로**, 이 소스는 트레이스를 **history · offline eval 데이터셋 · 메모리 갱신** 셋으로 나눈다(12:57~13:13). eval 플라이휠은 그중 한 갈래다.
- **[[agent-distributed-systems]]** — *"메모리 = 무효화 가능한 캐시"* 의 반대편 사례. 거기선 **낡은 기억이 남아** 틀리고, 여기선 **새 기억이 캐시·런타임 상태 때문에 안 보여** 행동이 안 바뀐다. 둘 다 캐시 일관성 문제다.
- **[[continual-learning]]** — 학습 자리를 *"the system around the agent"*(01:58~02:00)에 둔다 — Oracle·Anthropic에 이어 **컨텍스트 층** 쪽 세 번째 벤더 화자.
- **[[context-engineering]]** — progressive disclosure를 *장기 → 단기 읽기 단계* 로 위치시킨다(08:18~08:27).

### 갈리는 것

> ⚠️ **Contradiction: 메모리는 무엇인가 — 출처 vs 기능.** [[agent-memory]]의 first-seen([[tech-bridge-agent-knowledge-four-ways]])은 메모리를 *"에이전트가 스스로 수집하고 (…) 저장해 둔 정보"* 로 정의해 **사람이 적은 것(RAG)** 과 출처로 갈랐다. Broekhuizen은 *"the durable context that an agent references that will guide future runs"*(03:54~03:57)로 정의하고 **instructions · skills · rules(procedural)까지 메모리에 넣는다** — 금융 도우미의 교정도 *"We were giving it a rule"*(05:33~05:36)이었다. 같은 낱말이 한쪽에선 *겪은 것만*, 다른 쪽에선 *다음 실행을 이끄는 모든 지속 컨텍스트*다.

> ⚠️ **Contradiction: "로그가 곧 메모리"인가.** [[agent-action-record]]([[tech-bridge-knowledge-work-agent-infrastructure]])는 모든 행동 로그를 한곳에 모으면 *"에이전트가 기억을 얻는다"* 고 했다. Broekhuizen은 *"A trace (…) is evidence of what happened. It only becomes memory when that lesson is converted into durable context"*(04:00~04:12)이고 *"If we turned all of that evidence into long-term memory, then it would make the agent struggle"*(08:46~08:53)라고 한다 — **로그는 메모리가 아니라 메모리의 원료이고, 대부분은 history로 남아야 한다.** 행동 기록 쪽에도 "증류"가 있으므로 정면 충돌이라기보다 **필터 단계의 유무**에서 갈린다.

> ⚠️ **용어 충돌: "dreaming".** [[agent-dreaming]]의 dreaming([[lamis-mukta|Mukta]], [[anthropic|Anthropic]])은 **세션 밖·배치·비동기**의 second-order 과정이고 세션 안 메모리(인밴드)와 명시적으로 구분된다. Broekhuizen은 *"sleeptime compute or dreaming"* 을 메모리가 갱신·적재되는 방식 전반으로 쓰며 *"whilst the agent is doing work or actually in some cases while the agent is also not doing work"*(07:57~08:01)라고 해 **작업 중 갱신까지 포함**한다. 같은 낱말의 범위가 다르다.

> ⚠️ **Contradiction: 누가 기억의 변경을 승인하는가.** [[nightly-memory-consolidation|Muse]]는 *"대체로는 그것이 스스로 정합니다"*, Cursor `memories.md`·Anthropic 인밴드 memory tool(*"autonomy proved to work really well"*)은 에이전트가 직접 쓴다. Broekhuizen은 **procedural 변경은 사람이 보고 커밋**해야 한다고 한다(14:23~14:47). [[no-silent-write]]([[tech-bridge-company-brain-security]])도 사람 승인을 요구하지만 기준이 **범위**(공유 지식이냐)이고, 이 소스는 기준이 **메모리 종류**(procedural이냐)다 — 같은 결론, 다른 축. 한편 같은 발표의 §7 Context Hub 데모는 *"it'll make that change"*(12:11~12:13)로 승인 단계 없이 서술된다(⚠️ 발표 내부의 긴장 — 미해결).

> ⚠️ **분류 칸의 차이(모순 아님).** [[tech-bridge-oracle-agent-memory-harness|Oracle]]의 일화 기억 = *이전 대화*, 절차 기억 = *대화 전체 → 반복 가능한 워크플로*. OAMP 컨텍스트 카드는 *"사실 · 선호 · 기억"* 과 *일화 기억*(답 안 나온 질문)을 따로 둔다. Broekhuizen은 **선호를 semantic**, **패턴·예시를 episodic**, **스킬을 procedural**에 둔다. 이름은 같고 칸의 경계가 다르다.

## 해소하지 않고 표시만 한 것

- *"open core"*(14:06)의 정체 — OpenClaw의 ASR일 가능성(이 위키에서 OpenClaw와 Hermes가 나란히 불린 전례) — 세 트랙 모두 "open core"라 미확정.
- 분석 단계 *"engine"* 의 제품명·출시 상태, Context Hub 변경의 승인 흐름.
- *"most of the visible gains"*(05:15~05:17)·*"about 75%"*(14:30~14:32)의 근거.
- 금융 서비스 고객사 이름, 말투 개선의 측정 결과.
- 화자의 직함(설명란 "LangChain Labs 리드")과 행사명·녹화일 — 발화 없음.
- semantic·episodic 메모리의 쓰기 경로 — 화자는 procedural 위주로만 예를 든다.

## 등장 개체

- 인물: [[jake-broekhuizen]] (신규 제안)
- 조직: [[langchain|LangChain]] (LangChain Labs) · [[ai-engineer|AI Engineer]](⚠️ 설명란 링크만 — 추정)
- 제품·도구: [[langsmith|LangSmith]] (신규 제안 — Context Hub 포함) · Hermes agent(페이지 없음, 지나가는 언급) · "open core"(⚠️ 판독 미확정, [[openclaw]]일 가능성)
- 개념: [[trace-to-memory-loop]] (신규 제안) · [[agent-memory]] · [[agent-skills]] · [[skill-self-improvement]] · [[agent-dreaming]] · [[continual-learning]] · [[context-engineering]] · [[production-trace-eval-flywheel]] · [[agent-action-record]] · [[agent-distributed-systems]] · [[no-silent-write]] · [[nightly-memory-consolidation]] · [[files-vs-database-agent-memory]] · [[push-vs-pull-context-retrieval]] · [[context-resets-and-compaction]] · [[context-rot]] · [[skill-evals]] · [[risk-proportional-human-review]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=0kVsv2WlL44> (15:28, `upload_date` 2026-10-11)
- raw: `01.raw/articles/2026-10-11_AI 에이전트에 학습하는 메모리를 제공해 보세요 — Jake Broekhuizen, LangChain.md`
- 설명란 링크: <https://www.linkedin.com/in/jake-broekhuizen/> · <https://www.langchain.com/blog/introducing-langchain-labs> · <https://x.com/LangChain> · <https://ai.engineer> (⚠️ 열어 보지 않았다)
- 메모리 분류·저장: [[tech-bridge-oracle-agent-memory-harness]] · [[tech-bridge-agent-knowledge-four-ways]] · [[tech-bridge-agents-as-distributed-systems]]
- 쓰기 경로·게이트: [[tech-bridge-anthropic-dreaming-memory]] · [[tech-bridge-zuckerberg-muse-in-daily-use]] · [[tech-bridge-company-brain-security]] · [[tech-bridge-knowledge-work-agent-infrastructure]]
- 트레이스 → 개선: [[tech-bridge-wandb-aria-self-improving-agent]] · [[tech-bridge-tessl-harness-engineering-factory]]
- LangChain 1인칭 앞선 소스: [[tech-bridge-jev-agent-harness]]
- [[tech-bridge]] · [[langchain]] · [[langsmith]] · [[jake-broekhuizen]]
