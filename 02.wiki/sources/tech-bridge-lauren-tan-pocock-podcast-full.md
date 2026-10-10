---
title: "Tech Bridge — Lauren Tan × Matt Pocock 대담 풀버전: 2,500 PR의 메커니즘 — 미슐랭 주방, 두 루프와 코디네이터 에이전트, 표본 리뷰, '다크 팩토리냐? It kind of is'"
type: source
tags: [lauren-tan, matt-pocock, podcast, verification, cli, deterministic-vs-judgment, dune, codebase-gardening, outer-loop, coordinator-agent, cursor-projects, sampling-review, dark-factory, auto-merge, one-way-door, formal-verification, transcript-mining, pstack, grokbot, cursor, spacex, video]
source-url: https://www.youtube.com/watch?v=5tdMgKkX5dU
source-type: video
author: Tech Bridge (한영자막 재배포) · 게스트 [[lauren-tan|Lauren Tan]](발화 "Cursor which is now SpaceX AI" · 제목 "Cursor & Grok Bot 개발자" · 설명란 "pstack 개발자") · 진행 [[matt-pocock|Matt Pocock]](발화 "me and Matt"로 확인) · 2인 대담
date-published: 2026-10-09
ingested: 2026-10-10
created: 2026-10-10
updated: 2026-10-10
---

# Tech Bridge — Lauren Tan × Matt Pocock 대담 풀버전

[[tech-bridge|Tech Bridge]]가 한영자막을 입힌 **1:04:03 대담, 공식 챕터 12개.** 진행자 [[matt-pocock|Matt Pocock]]이 [[lauren-tan|Lauren Tan]]의 *"약 10일 전"* 강연(X에서 *"how I shipped 2,500 PRs last month"*, 진행자 말로 약 300만 뷰)을 **Q&A로 파고드는** 형식이다. [[lauren-tan]]의 **여섯 번째 소스**이자 **가장 긴 본인 발화**다. 그리고 **새 녹화가 아니다** — 10-03의 해설 영상 [[tech-bridge-lauren-tan-agent-dev-workflow]]가 발췌한 6구간이 이 영상에 문장 그대로 있다(아래 ⚠️). 그래서 이 페이지의 가치는 **(1) 해설 영상이 2차 요약으로만 전한 것을 발화로 확인하고, (2) 발췌에 없던 약 55분의 새 내용을 더하는 것**에 있다. 한 줄 테제:

> **월 2,000~2,500 PR은 내가 2,500번 채팅을 여는 게 아니라, 환경(칼·도구·제약)을 먼저 갈아 둔 주방 위에 두 루프를 이은 결과다 — 바깥 루프(GrokBot 커넥터·루틴)가 Slack·X·Linear의 맥락을 끌어와 안쪽 루프(Cursor projects의 코디네이터 에이전트)에 넘기고, 코디네이터가 서브에이전트에 일을 나눈다. 시작 질문은 "어떻게 하면 에이전트가 자기 코드를 머지할 수 있나"를 거꾸로 푸는 것이었고, 답은 검증 + 환경이다. 그래서 사람은 모든 접시를 맛보지 않고 표본을 엄격히 보며 환경을 고친다 — 그건 사실상 다크 팩토리다. 단, 검증할 수 없는 영역의 one-way door에는 나도 답이 없다.**

> *"I was the meat proxy between my agent and Chrome DevTools"* (04:09~04:14) · *"how do I make the easy thing the right thing?"* (05:14~05:17) · *"the bottleneck these days is is like the transfer of your intent"* (07:13~07:18) · *"I almost feel like the new job of the engineer is really to to spend time on the environment"* (25:10~25:15) · *"the big unlock for me for getting to 2,000 PRs is starting from the question and working backwards of how do I get to the point where my agent can merge its own code?"* (38:32~38:45) · *"It kind of is. Yeah, actually."* (50:49) · *"I think it's a great question that I don't really have the answer to"* (56:29~56:34) · *"everyone should have their own set of knives"* (1:00:21~1:00:28)

**트랙과 인용.** 세 트랙 모두 자동 자막. ko는 `en`의 번역이라 `en`의 오역을 공유한다. **인용은 en-orig에서만** 했다. ko의 대표 오류: **Pstack의 기원을 "피루스 법"**(02:37, `en` *"Pyrus Act"*), **judgment를 "재판"**(19:59·20:51), **개발 환경에 쓰는 시간을 "환경 보호"**(25:13), **parallelize를 "마비"**(37:55, `en` *"paralyze"* — 정반대), **chief of staff를 "인사부장"**(41:56), **proofs를 "테스트·시험 문제"**(57:00~57:09, `en` *"testing"*) — 형식 증명 이야기가 테스트 이야기로 바뀐다. **race condition을 "직업적 조건"**(57:47), **PR을 "홍보"·"지원서"·"추출 요청"**, **inner loop를 "체내 순환계"**(34:19), **harness를 "안전벨트"**(35:49), 진행자의 *"they probably have"*(TypeScript를 Go로 다시 썼을 것)를 **"그러지 않았을 가능성이 높지만"** 으로 뒤집었다(31:25, en·ko 공유). 전체 목록은 raw.

> ⚠️ **같은 대담의 두 번째 소스다.** [[tech-bridge-lauren-tan-agent-dev-workflow]](OLYuAekOBeA, 11:36 해설)의 Lauren 발화 6구간이 이 영상에 그대로 있다 — 검증 *"single most important skill"*(15:16~15:21), CLI의 gradient(19:50~20:52), Dune *"only one way"*(29:20~30:08), 두 루프(35:21~36:50), 품질 감독관의 표본(48:40~49:19), *"very hard to get to this point"*(50:13~50:41). ASR 흔적(*"PAC"*, *"restrictive lit rules"*)도 같다. **그 해설 영상이 원본으로 링크한 `MN9dGgmLyso`가 이 영상의 무삭제 원본인지는 미확정**(이 위키는 그 영상을 열어 보지 않았다; 이 영상은 문장 중간에서 시작하고 끝난다). [[tech-bridge-lauren-tan-2000-prs]](1인 강연)·[[tech-bridge-lauren-tan-trusting-agents]](Colin 진행 워크숍)는 **다른 녹화**다.
>
> ⚠️ **당사자 진술, 독립 확인 없음.** 화자는 자기 도구(Pstack·GrokBot)와 회사 제품(Cursor projects·automations)을 쓰는 법을 말하고, 진행자도 자기 스킬(*grill me*·*wayfinder*)을 판다(*"if you trust us both, of course, use our skills"* 1:01:13~1:01:16). PR 수·chief of staff 수·verifier 에이전트 수·자동 머지의 결과(회귀·되돌림 비율) 어느 것도 측정이 제시되지 않는다.
>
> ⚠️ **소속.** 발화: *"before I joined cursor uh which is now SpaceX AI"*(00:58~01:04), *"every app that cursor has or spaceexai has"*(18:04~18:09). 제목: *"Cursor & Grok Bot 개발자"*. 설명란: *"pstack 개발자"*, *"SpaceX에서 … 매달 수천 개의 PR"*. **"Cursor는 이제 SpaceX AI다"는 09-25 강연의 *"SpaceX AI의 일부가 되기 전"* 보다 한 걸음 더 나간 표현**이지만 형태(인수·합병·브랜드)는 여전히 말하지 않는다 → **발화만 기록.** 설명란의 *"SpaceX에서 매달 수천 개"* 는 **개인의 지난달 PR 수**를 조직 수치처럼 바꿔 쓴 것이다.
>
> ⚠️ **녹화 시점 — 미확정.** 앵커: 진행자 *"about 10 days ago"* 강연(00:04), Lauren *"I joined Cursor in March"*(04:20~04:23), *"I love Opus 5.5"*(06:07~06:11). **3월 합류**는 이 위키의 앞선 본인 진술(09-12 워크숍 *"약 5개월"*, 09-25 강연 *"6개월 전"*)과 정합한다(→ 각각 8월·9월 무렵 녹화를 시사, ⚠️ 어림수에 기댄 추정이라 채택하지 않음). *"10일 전 강연"* = [[tech-bridge-lauren-tan-2000-prs]]일 개연성은 높지만(설명란 링크·주제 일치) **수치가 다르다**(아래 Contradiction).

## 1. 신뢰 사다리의 기원 — 번아웃, 사이드 프로젝트, "meat proxy" (00:00~05:20)

**새로 나온 기원 이야기.** Meta React 팀을 나와 *"I took a month off uh because I was feeling kind of burnt out"*(01:10~01:14), 사이드 프로젝트를 하다 *"I was spending like so many hours just micromanaging one agent"*(01:29~01:34). 때는 *"back in February, maybe February, early February or January"*(01:36~01:41), 다들 커스텀 오케스트레이터에 빠져 있던 시기(01:41~01:58). 스킬을 만들었지만 *"finding it quite difficult to measure the output or the the result the impact of the skill (…) I was kind of flying blind"*(02:23~02:32) — 그 프로젝트가 *"eventually sort of became the basis of PAC[=Pstack]"*(02:37~02:42). 저장소는 *"still open source (…) on my GitHub like potato noodle"*(02:50~02:56, `poteto/noodle` 로 판독 — ⚠️ 열어 보지 않음), *"some skills and a brain directory"*(03:00~03:02). 동기: *"how do I (…) extract my own ability (…) and give it to the agent"*(03:07~03:12).

Cursor 합류(3월) 후 **agents window 성능 작업**(*"early early April probably"* 04:23~04:26)에서 다시 같은 깨달음 — ***"I was sort of the meat proxy (…) between my agent and Chrome DevTools"***(04:07~04:14). 09-25 강연의 기원 이야기와 **같은 사건, 새 표현**이다. 그리고 원칙 하나가 처음 말로 나온다:

> *"agents from my experience even the the frontier ones tend to (…) tend to take shortcuts. Uh they tend to do the easy thing. Uh so uh a lot of the skills that I've built have been around how do I make the easy thing the right thing?"* (04:55~05:17)

09-25 강연의 *"쉬운 길이 옳은 길"*(Dune)과 같은 말이지만, 여기서는 **스킬 설계 전반의 원칙**으로 일반화된다. → [[shortest-path-architecture]] · [[agent-trust-curve]]

## 2. 도메인 전문성은 그 어느 때보다 중요하다 — 병목은 의도 전달 (05:20~09:30)

해설 영상이 발췌 없이 요약했던 대목(*"도메인 전문성이 더 중요해졌다"*)의 **원 발화**:

> *"I actually feel like domain expertise is is more important than ever"* (05:48~05:54) · *"as the models get really, really, really good, it almost becomes like the bottleneck is no longer the agent, right? it becomes your ability to express your intent and your goals in a clear way that the Asian[=agent] can understand"* (06:11~06:29)

예: 의사·변호사처럼 비엔지니어링 전문성이 있고 *"just a little bit techsavvy"* 한 사람이 *"really really great products"* 를 만들 수 있다(06:44~07:02). 진행자는 **언어**로 받는다 — 에이전트가 붙잡아 사고 흔적에서 재사용하는 단어(*TDD*, *grilling*), Lauren은 진행자의 팁 **동어반복 테스트 제거**를 베꼈다며(08:21~08:38) *"you compress a lot of intent and meaning into words"*(08:56~08:58). → [[adjective-verb-steering]] · [[structure-sensitive-tests]] · [[intent-alignment]]

## 3. 미슐랭 주방 — 전체판 (09:30~14:06)

09-25 강연의 한 줄 비유가 여기서 **완전한 구조**로 나온다.

- *"I've never really liked the term software factory. Not because you know it's not accurate"*(10:14~10:22) — 공장은 *"quality or craft"* 를 떠올리게 하지 않을 뿐, *"while I do think software factory is an apt term it also (…) conjures up negative (…) connotations"*(10:42~10:50). ⚠️ 09-25 강연에서 슬라이드의 그 말에 **줄을 그은** 것보다 **훨씬 부드럽다** — 용어가 틀렸다는 게 아니라 **함의**가 싫다는 것.
- 홈 쿡은 *"the one man or one woman show"*(11:53~11:58) → 가족이 주방에 들어오면 스트레스(*"They have no no idea where all the utensils are"* 12:17~12:21) → 수셰프 몇 명으로 **일을 나누는 법** → 셰프는 *"almost like the tech lead right for the kitchen"*, *"the CEO of the kitchen"* — 재료 주문·보관·준비 시점까지(13:10~13:30).
- ⭐ *"you as the human are still responsible for the final outcome, right? your name still is associated with the work that you do, your reputation (…) how you set up your kitchen right and how you set up your skills your environment your codebase I think are ultimately the new ingredients that go into um building product"*(13:41~14:04)

→ [[agent-manager-analogy]] · [[software-factory]] · [[named-human-accountability]]

## 4. 검증 — "hands and eyes", 그리고 hill climbing (14:06~18:18)

발췌로 이미 위키에 있는 부분(*"single most important skill"*, *"hands and eyes"*, *"first skill I built when I joined Cursor"*)에 **새로 붙은 것**:

- 다른 스킬(*"the how skill the Y skill the unslap skill"* 16:12~16:17, ⚠️ unslop으로 판독)로는 사다리를 못 올랐던 이유 — *"I was still relying on me right as the proxy between my agent and the output"*(16:17~16:22).
- ⭐ ***"the most important part of a loop that allows it to be a loop is the verification part"***(16:44~16:50) — "에이전트 루프"의 정의를 검증으로 한다.
- 첫 용도는 agents window 성능의 **hill climbing**: *"you have some kind of rubric or a way to judge or score something and now because you have a loop (…) an agent continually try to make improvements"*(17:17~17:28). Karpathy의 *"auto research"* 를 같은 계열로 든다(17:29~17:36, ⚠️ 정체 미확인).
- 규모: *"every app that cursor has or spaceexai has has a uh verification skill that is automaintained as well (…) it's become critical infrastructure for our team"*(18:04~18:18). 09-25 강연의 *"팀의 핵심 인프라"* 의 반복이지만 **"모든 앱에 하나씩, 자동 유지"** 가 새 정보다(⚠️ 당사자 진술).

→ [[agent-verification-skill]] · [[verifiable-goals]] · [[automated-ai-research]]

## 5. CLI의 기원 — 컨텍스트 창 걱정에서 결정론/판단 gradient로 (18:18~23:47)

발췌로 위키에 있는 gradient 발언의 **앞뒤가 새로 붙었다**:

- **출발점은 컨텍스트 창**: *"back in January or or late last year the thing that people were concerned about was context window"*(18:40~18:48), 한 번 compaction되면 *"it would become sort of stupid right for the rest of your session"*(19:04~19:12)이라는 밈 → CLI가 그 영감. *"now it's less so about context because (…) harnesses have gotten a lot better with summarization"*(19:28~19:36). → [[context-resets-and-compaction]]
- **진짜 이유는 일관성과 속도**: CLI가 없을 때 *"the agent would try to verify his work but it would basically rebuild the world each time and then every agent did it differently"*(21:56~22:05), *"the last agent did it and it worked but it discarded it"*(22:18~22:22) → *"turn this into a CLI and put that inside of the skill uh so that every agent that uses it now benefits"*(22:24~22:32).
- CLI는 *"your wrapper (…) with some light instructions"*(20:55~21:00), 그 자체는 *"just something that interacts with like Playright and the Chrome DevTools protocol and calls a bunch of APIs. It's like it's just a bunch of glue"*(21:10~21:18).
- 확장: *"how much of your skills and rules could actually be deterministic"*(22:38~22:42) — **마이그레이션**은 codemod·AST 변환처럼 *"a script does it for you instead of the agent"*(23:30~23:44). → [[large-scale-code-changes]]
- 진행자의 재진술: *"it's a way of hiding information from the skill (…) keeping the skill quite small"*(21:18~21:25).

→ [[build-a-lever]] · [[scripts-that-talk-back]] · [[domain-specific-scripts]]

## 6. 엔지니어의 새 직업 = 환경 — 무딘 칼, 타입 좁히기, Dune (23:47~31:53)

- ⭐ *"I almost feel like the new job of the engineer is really to to spend time on the environment"*(25:10~25:15). 신뢰가 낮으면 *"the only way to cope (…) is just to kind of lock in and micromanage your agents"*(25:37~25:46) — 그러면 생산성을 높일 여유가 없다. 비유: VS Code·Vim·Git을 모르고 메모장만 쓰는 개발자, *"you haven't spent the time sharpening your own knives"*(26:19~26:24), 마늘 다지기 대신 마늘 프레스(27:00~27:14).
- **타입 좁히기 ↔ 코드베이스 제약** (새로 나옴): TypeScript Conf 발표 경험, *"one of my most favorite things about Typescript is actually type narrowing"*(28:12~28:18) → *"there's a lot of parallels I think to that with constraints in your codebase where is that you're you're constraining the space"*(28:41~28:48), *"you're saying there's only one type"*(28:59~29:01).
- **Dune** — *"it's kind of like a internal nex.js[=Next.js] for our electron apps"*(29:09~29:16), *"not an open source framework"*(29:07~29:09). 나머지(feature 디렉터리·레지스트리·린트)는 발췌로 이미 위키에 있다.
- ⭐ **god file의 크기가 확정됐다**: *"the very first couple of versions of Grockbot were composed of like eight god files which were like at least 10,000 lines long if not longer"*(30:21~30:34). 해설 영상의 en-orig *"at least 100 lines long"* 은 **같은 문장의 잘린 ASR**이었다 — 그 페이지가 의심했던 자릿수 문제가 해소된다.
- *"observing how agents fail and then every time you see a mistake (…) how do I turn this into a lint rule how do I make it so that the codebase makes this impossible"*(30:41~30:57). 진행자의 요약: 환경에 넣으면 에이전트가 규칙을 기억할 필요 없이 *"it stumbles into the rules (…) and hits them at the right moment"*(31:47~31:53).

→ [[dune-architecture]] · [[hard-vs-soft-enforcement]] · [[codebase-gardening]] · [[executable-standards]]

## 7. 2,500 PR의 메커니즘 — 체인 레스토랑과 두 루프 (31:53~39:04)

진행자: *"Are you um initiating 2500 like chats per month? That can't be right."*(32:11~32:16)

- **전제는 환경**: *"I definitely would not have been able to do this if I had not spent the time (…) thinking about the kitchen"*(32:42~32:47). 비유가 **체인 레스토랑**으로 넓어진다 — 진행자의 *"you're Gordon Ramsay"*(33:13), Lauren의 *"each big chat is sort of like a restaurant (…) I'm sort of like helicoptering between them"*(33:33~33:46).
- **안쪽 루프의 정의** (새로 정밀해짐): *"my inner loop is like basically my engineers my agent engineers working on the code to an building towards an intent or snapshot of my intent right and the thing about that is that the snapshot can go stale"*(34:29~34:46) — 그 스냅샷을 새 정보로 갱신하는 일을 사람이 *"proxy"* 로 하고 있었다(34:46~35:21).
- 바깥 루프 연결(*"tools like Grockbot"* 35:23~35:26 — 해설 영상에서 잘렸던 이름이 **GrokBot으로 확인**된다), Slack MCP 또는 자체 하네스의 Slack 구독, 재현의 판정 항목 — 발췌로 위키에 있다.
- ⭐ **회사 두뇌에 대한 반론의 원형**: *"a lot of people talk about this idea of a company brain, right? Or a context graph. I feel like those terms are unnecessarily complex uh or even abstract. To me, it's just about um how do I take information that my agent needs that I would otherwise have to go and pass it myself and just teach it how to do it"*(37:13~37:39). 09-25 강연(*"그렇게 정교한 게 필요 없다"*)과 같은 입장에 **"context graph"** 까지 포함된다. → [[company-brain]]
- ⭐ **Cursor projects = 코디네이터 에이전트** (새로 나옴): *"cursor has a new feature called projects which are these like coordinator agents (…) really good at sort of delegating and not doing work of their own but they manage and supervise like almost a list of tasks and they spawn sub agents"*(38:04~38:22).
- ⭐ **시작 질문을 거꾸로**: *"the big unlock for me for getting to 2,000 PRs is starting from the question and working backwards of how do I get to the point where my agent can merge its own code?"*(38:32~38:45)

## 8. 안쪽 루프 = Cursor projects, 바깥 루프 = GrokBot (39:04~44:51)

- GrokBot류는 *"connectors (…) a lot of people call them personal agents"*(40:02~40:09) — 이메일·캘린더·Slack·*"Plaid"*(⚠️ 판독 미확정) 등. Netflix 관리 원칙 **"context, not control"**(40:36~40:39)이 에이전트 세계로 넘어온다: *"what you want is to provide context instead, right? Like teach the agent, teach your engineers how to be self-sufficient"*(40:53~41:01). → [[agent-manager-analogy]]
- 구체: *"I have some Groth[=Grok] bots that look at my Slack channels, look at my X, uh, or my emails, uh, or or linear, and (…) they have routines that subscribe"*(41:09~41:21), 예: GrokBot 데스크톱 앱 버그를 찾으면 *"send it to my cursor project"*(41:26~41:36).
- 코디네이터: *"a coordinator agent that's in the cloud. It has its own computer and all it really does is like it's a manager of agents. It's like your executive chef, right? Your your chief of staff. It doesn't do the work itself."*(41:47~42:00)
- ⭐ ***"cursor projects are my inner loop and grabbot[=GrokBot] is my outer loop"***(42:55~43:00). 09-25의 *"GrokBot = 바깥 루프"* 에 **안쪽 루프의 이름**이 붙었다.
- ⭐ **왜 버그 하나에 에이전트 하나가 아닌가**: 관련된 버그 묶음에 *"you can certainly go off and just spawn one agent per task, but then you've lost that sort of thread between them (…) you may duplicate work or you may not really think about the higher level problem"*(43:31~43:43). 여러 제보를 함께 보면 *"when I looked at this one report, I thought the bug was here, but (…) is actually up here"*(43:52~44:00). 해설 영상의 **"조정자" 요약에 발화 근거가 생긴다.**

→ [[grokbot]] · [[cursor]] · [[persistent-agent-teams]] · [[cloud-agent-delegation]] · [[scheduled-agent-automations]]

## 9. 코드베이스를 가꾸는 루틴 — 2,500 PR은 2,500 기능이 아니다 (44:51~48:09)

- ⭐ *"the 2,500 PRs, they're not obviously like 2,500 features, right? (…) a lot of the work actually is spent on gardening"*(44:55~45:06). 좋은 환경은 에이전트뿐 아니라 **신입**을 *"productive from day one"* 으로 만든다(45:26~45:36). → [[codebase-gardening]] · [[trusted-throughput]]
- ⭐ **나쁜 패턴은 곧바로 고치지 않는다** (해설 영상의 2차 요약이 **발화로 확인**됨): React의 *"foot guns"* 를 찾는 에이전트 — *"I don't actually tell it to fix the issue first. I tell it to append it to a document and then every couple of days I look at it and I say actually these are all the same thing"*(46:45~46:55), *"you almost want like a buffer a cue[=queue] sometimes that's actually more effective than just spawning off (…) a lot of sub agents to fix every single thing"*(46:58~47:06). 이유: *"when you are in kind of pure execution mode (…) you sometimes miss the big picture"*(47:06~47:19). 코디네이터의 이점도 같다 — *"it can see the forest"*(47:49~47:53).

## 10. 표본 리뷰, 그리고 "다크 팩토리냐? — It kind of is" (48:09~54:38)

- 진행자: *"did you taste all 2500 of those dishes as they swept past you?"*(48:15~48:18). Lauren: *"you don't want to be in a position where you're not tasting your food ever again. Uh but (…) you cannot be tasting every single dish"*(48:28~48:38) → 그다음이 발췌로 위키에 있는 **공장 품질 감독관의 표본**이다. 해설 영상이 이를 **주방 비유**로 소개했던 이유가 풀린다 — **질문은 주방, 답의 핵심은 공장.**
- ⭐ **고치는 대상은 에이전트가 아니라 환경**: *"you think about how to course correct the environment, right? Not not that single agent. (…) if it was a one-off incident, it's fine (…) But if you actually notice that multiple agents are are having the same issue (…) They're propagating the same workaround everywhere"*(49:17~49:43).
- 진행자: *"this isn't a dark factory, right? This the lights are on, right?"*(50:44~50:49). ⭐ **Lauren: *"It kind of is. Yeah, actually."*(50:49)** — *"if my agents are merging their own pull requests it's sort of become dark where I go to sleep my agents now work 24/7"*(50:56~51:05).
  - *"I have the equivalent of like more than 10 chief of staff right each working on a different area"*(51:05~51:12) — GrokBot 데스크톱 성능, 사용자 버그 수정, *"exploring rewriting it in a different language just for fun (…) a native app. It's just a toy"*(51:22~51:32).
  - ⭐ **Pstack "full autopilot"**: *"that will trigger off this very intense rigorous verification loop where it'll spawn a bunch of verifier agents for every pull request and it will fuzz right fuzzing meaning that it will actually run the application. It's going to click around and try to use it like a real human"*(51:47~52:05) → 문제를 찾아 스스로 고치고 반복해 *"get the PR to a state where it can land"*(52:13~52:21).
  - **토큰 인정**: *"it is quite token intensive. You can tune this of course (…) instead of like 10 verifier agents you might do like one"*(52:21~52:31). 해설 영상의 *"토큰 비용"* 요약의 원 발화.
  - 사후 리뷰: *"I'll review it in the morning by looking at my commit history and if I see problems, I go and course correct (…) revert or modify, add new lint rules"*(52:51~53:02). 09-12 워크숍의 *"main에서 사후 리뷰"* 와 같은 구도.
  - 첫날: *"very scary because I was like, 'Ooh, what if I call the SE[=cause a SEV, 추정], right? What if I break something overnight?'"*(53:18~53:25) — *"it took a lot of uh bravery"*(53:27~53:30), 지금은 *"I'm sleeping so much better now"*(53:10~53:12).
- 진행자의 대비: 다크 팩토리를 *"the original definition of Kapathy's vibe coding (…) the code almost doesn't exist"*(53:45~53:53)로 읽으면 Lauren의 방식은 정반대 — 코드와 환경이 본질(53:55~54:05). Lauren: *"maybe there's a dimmer switch or something (…) some parts of dark, some parts are light"*(54:13~54:18). 진행자: *"the idea of sampling instead of blocking I think is really important"*(54:35~54:37).

→ [[verification-bottleneck]] · [[software-factory]] · [[agent-trust-curve]] · [[risk-proportional-human-review]]

## 11. 되돌릴 수 없는 변경 — "답이 없다" (54:38~58:39)

진행자가 **one-way / two-way door**(자기 발표 [[tech-bridge-pocock-pr-bottleneck]]의 틀)로 묻는다: 의료·법률·금융처럼 PR 대부분이 one-way door라면?(54:38~55:21)

- *"it all comes back to me to the quality of the verification"*(55:24~55:32). ⭐ *"for domains where the work is verifiable, this is easier, right? and the the oneway doors become two-way doors in a sense"*(55:36~55:47) — **검증 가능성이 가역성을 대신한다**는 주장.
- 검증이 어려운 영역에선 *"it's very hard to get to that point"*(55:55~55:59). 소프트웨어는 *"quite verifiable in in a lot of cases maybe not totally"*, 수학도 증명을 쓰면 일부(56:06~56:26).
- ⭐ ***"I think it's a great question that I don't really have the answer to"***(56:29~56:34) — 해설 영상의 *"모든 상황에 대한 답을 갖고 있지는 않다"* 의 원 발화.
- 예측: *"we'll see more and more interesting new agentoriented programming languages"*(56:44~56:50), 예로 *"bend"*(56:53, ⚠️ 판독 미확정 — 설명이 알려진 Bend와 맞지 않음) — *"marries programming with proofs"*(56:59~57:03), 예전엔 Lean·TLA+(*"ta plus"*) 같은 별도 언어로 증명하고 solver로 *"you don't have like a race condition"*(57:29~57:50). 결론: *"if it compiles, right, if it if the proofs show you that it's correct, then why wouldn't you just merge it? Um but of course, yeah, not all domains are verifiable."*(58:10~58:20)

09-25 강연의 *"형식 검증은 스펙트럼의 먼 끝, 여전히 열린 문제"* 와 같은 결이고, 여기서는 **자동 머지의 전제 조건**으로 놓인다. → [[action-reversibility]] · [[ai-formal-verification]] · [[verifiable-goals]]

## 12. 자신만의 스킬 — 트랜스크립트를 캐라, 스킬은 작아진다 (58:39~1:04:03)

- 진행자: 스킬은 *"processes turned into words"*(59:13~59:16) — Pstack과 내 스킬을 어떻게 섞나?
- Lauren은 진행자의 팁을 받는다 — 과거 트랜스크립트에서 **교정·개입한 자리**를 찾아 *"take that higher level learning and turn that into a a reusable skill"*(59:44~59:56). ⭐ *"The the past chats I I often say is like a a treasure trove of context because (…) it's like the process materialized"*(1:01:33~1:01:46).
- ⭐ **Pstack `recall` 스킬**의 기원: Cursor 앱 **virtualization** 작업에서 버그가 많아 새 채팅마다 지난 채팅의 맥락을 가져오고 싶었고, *"recall was just a way for me to collapse collapse and compress that workflow into a skill"*(1:02:26~1:02:33).
- ⭐ **스킬은 작아진다**: *"skills from last year were really more about like almost like implementation details like here are the exact script commands (…) with the latest models you can just delete those parts and just really focus on the workflow"*(1:02:47~1:03:03), *"over time we'll see that skills get smaller and smaller"*(1:03:10~1:03:14). ⚠️ §5의 *"결정론적 부분은 CLI로"* 와 함께 읽으면 — **스킬 문서는 워크플로만, 결정론은 스킬 안의 코드로** 갈라진다(위키의 독해).
- *"everyone should have their own set of knives (…) every chef when they go to a different job (…) they bring their knives with them"*(1:00:21~1:00:39), ***"trust to me is really about trust in your own tools"***(1:00:39~1:00:43). 조합 예: 진행자의 *grill me with docs*·*wayfinder* + Pstack 실행 스킬(1:00:53~1:01:02), *"Combine Wfinder[=wayfinder] with potato mode"*(1:03:26~1:03:28).

→ [[skill-self-improvement]] · [[query-to-skill-distillation]] · [[agent-skills]] · [[pstack]]

## 앞선 소스와의 대조 — 무엇이 새롭고 무엇이 반복인가

### 해설 영상([[tech-bridge-lauren-tan-agent-dev-workflow]])의 미해결 항목 — 이 소스로 풀린 것

| 그 페이지의 표시 | 이 소스 |
|---|---|
| 진행자 Matt Pocock은 판독(태그·ASR) | **발화로 확인** — *"me and Matt"*(1:01:13), *"total TypeScript"*(27:54), *"I did a drama degree"*(09:21) |
| *"tools likeot"* — 이름이 잘림 | *"tools like Grockbot"*(35:23~35:26) — **GrokBot** |
| god file *"at least 100 lines long"* — 자릿수 의심 | ***"at least 10,000 lines long if not longer"***(30:30~30:34) |
| 조정자 역할 — 2차 요약 | Cursor projects 코디네이터, 버그 묶음의 실(thread)을 잃지 않으려고(38:04~44:00) |
| 나쁜 패턴을 곧바로 고치지 않고 문서에 모은다 — 2차 요약 | **발화 확인**(46:45~47:06) — 버퍼·큐, 큰 그림을 보려고 |
| 토큰 비용 — 2차 요약 | *"quite token intensive"*, verifier 10 → 1로 조절(52:21~52:31) |
| 되돌리기 어려운 변경 *"모든 답은 없다"* — 2차 요약 | *"I don't really have the answer to"*(56:29~56:34) + 검증 가능성이 one-way를 two-way로 |
| 도메인 전문성 — 2차 요약 | *"more important than ever"*(05:48~05:54), 병목 = 의도 전달 |
| 주방(해설) vs 공장(발화) | 질문(진행자)이 주방, 답(Lauren)이 *"you cannot be tasting every single dish"* → 공장 감독관 |
| *"setting ups and constraints"* | *"setting up guard rails and constraints so that they do the right thing by default"*(50:33~50:41) |

### 반복된 것 (이미 위키에 있음)

검증 = 가장 중요한 스킬·*hands and eyes*·Cursor 첫 스킬 · 판단/결정론 gradient와 CLI · Dune의 *"only one way"*·feature 디렉터리·레지스트리 · 두 루프 연결·Slack MCP·main 재현 · 공장 품질 감독관의 표본 · *"very hard to get to this point"* — 모두 [[tech-bridge-lauren-tan-agent-dev-workflow]]에 발췌로. 미슐랭 주방·*"소프트웨어 공장"* 이라는 말에 대한 거리감·*"회사 두뇌까지는 필요 없다"*·GrokBot 바깥 루프·검증 스킬 = 팀 인프라 — [[tech-bridge-lauren-tan-2000-prs]]에. 자동 머지와 main 사후 리뷰 — [[tech-bridge-lauren-tan-trusting-agents]]에.

### 새로 나온 것

기원(번아웃·사이드 프로젝트·`noodle` 저장소 → Pstack) · **3월 Cursor 합류** · *"meat proxy"* · *"easy thing the right thing"* · 도메인 전문성/의도 전달 · 미슐랭 주방 전체판(*"the new ingredients"*) · 루프의 정의 = 검증, hill climbing · **모든 앱에 자동 유지되는 검증 스킬** · CLI의 첫 동기 = 컨텍스트 창, 에이전트가 *"rebuild the world each time"* · 마이그레이션 codemod · *"the new job of the engineer is (…) the environment"* · 타입 좁히기 ↔ 제약 · Dune = *"internal Next.js for our electron apps"* · god file **10,000줄+** · 안쪽 루프 = **의도의 스냅샷이 낡는다** · *"context graph"* · **Cursor projects(코디네이터 에이전트)** · *"working backwards from (…) merge its own code"* · Netflix *"context not control"* · **2,500 PR ≠ 2,500 기능, 대부분 gardening** · 패턴 버퍼 · **다크 팩토리 수용**, chief of staff 10+, **Pstack full autopilot**(verifier 에이전트 퍼징) · 첫날의 두려움 · **검증 가능성이 one-way door를 two-way로** · 에이전트 지향 언어(Bend? ⚠️) · 트랜스크립트 마이닝·**Pstack `recall`**·스킬은 작아진다 · *"trust in your own tools"*.

### 갈리는 것

> ⚠️ **Contradiction: PR 수치 — 2,000인가 2,500인가.** [[tech-bridge-lauren-tan-2000-prs]]의 강연 발화는 *"지난달 PR 2,000개"*. 이 대담에서 진행자가 인용한 X 게시물 제목은 *"how I shipped 2,500 PRs last month"*(00:09~00:12)이고, Lauren 본인도 한 대화 안에서 *"2,000 PRs"*(38:34~38:38)·*"2,000 and 2,500 pull requests last month"*(38:49~38:53)·*"the 2,500 PRs"*(44:55~44:58)를 섞는다. 해설 영상의 내레이터는 2,500을 *"X 프로필"* 출처로 댔다. **어느 달의 어느 값인지, X 게시물과 강연이 같은 것인지 화자가 가르지 않는다** — 이 위키는 해소하지 않는다. 자기 보고 계열: 1,000(09-12) → 2,000(09-25 강연) → 2,000/2,500(이 대담).

> ⚠️ **Contradiction: "소프트웨어 공장"에 대한 거리.** 09-25 강연은 슬라이드의 그 말에 **줄을 그었다**. 이 대담은 *"Not because you know it's not accurate"*(10:19~10:22), *"I do think software factory is an apt term"*(10:42~10:45)이고, 다크 팩토리냐는 질문엔 *"It kind of is"*(50:49). 같은 사람의 같은 비유인데 **강연(정돈된 서사)에선 거부, 대담(질문에 대한 답)에선 수용**이다. 위키의 독해: 거부의 대상은 **함의(품질·장인정신 부재)**, 수용의 대상은 **구조(사람 없는 야간 가동 + 표본 품질 관리)** — 층이 다르다.

> ⚠️ **Contradiction: Kent Beck의 "다크 팩토리는 언제나 탈선한다"와.** [[software-factory]]의 Beck(*"there's no human involved There's no feedback. And that always goes off the rails. Always."*)과 Lauren의 *"It kind of is"* 는 정면으로 갈린다. 다만 Lauren의 다크 팩토리는 **verifier 에이전트 퍼징 + 아침의 사람 사후 리뷰 + 환경 교정**이라는 피드백을 가진다 — Beck이 겨눈 *"no feedback"* 상태가 아니다. 진행자도 *"dimmer switch"* 로 받는다. **어느 쪽도 측정을 내놓지 않는다.**

> ⚠️ **Contradiction(약): 싹을 빨리 자르기 vs 버퍼에 모으기.** [[codebase-gardening]]의 09-25 발화 *"퍼지기 시작하기 전에 가능한 한 빨리 싹을 잘라야"* 와 이 대담의 *"I don't actually tell it to fix the issue first. I tell it to append it to a document"*(46:45~46:51). 해설 영상 페이지가 2차 요약이라 해소를 미뤘던 자리가 **이제 둘 다 본인 발화**다. 위키의 독해: 버퍼는 **며칠 단위**(*"every couple of days"*)이고 목적이 **같은 원인 묶기**라, 09-25의 *"린트 규칙으로 출혈부터 멈춘다"* 와 결합하면 양립한다 — 하지만 화자가 둘을 잇지 않았다.

## 해소하지 않고 표시만 한 것

- **`MN9dGgmLyso`와의 관계** — 이 영상이 그 원본 대담의 무삭제본인지, Tech Bridge가 앞뒤를 자른 것인지.
- **"10일 전 강연"** 의 정체(zkmvCDSxqdc일 개연성), X 게시물의 날짜·실제 제목·300만 뷰.
- **2,000 vs 2,500**의 달·측정.
- **Cursor projects** — 공개 기능인지, 이름이 그대로인지. 이 위키에 독립 기록이 없다.
- **Pstack full autopilot**의 verifier 기본 수(*"10"* 이 기본값인지 예시인지), 퍼징의 범위.
- **"Cursor which is now SpaceX AI"** 의 법적·조직적 형태.
- 언어 **"bend"**, **"auto research"**(Karpathy), 커넥터 **"Plaid"**, 저장소 **`noodle`** 과 *"brain directory"*, 스킬 이름 *how/why/unslop*, *"potato mode"*.
- 자동 머지 이후의 **회귀·되돌림 비율** — 말하지 않는다.
- 진행자의 TypeScript *"25,000line type file"*.

## 등장 개체

- 인물: [[lauren-tan]] · [[matt-pocock]] · [[andrej-karpathy]](*auto research*·*vibe coding* 언급) · Gordon Ramsay(비유)
- 조직: [[cursor]] · [[spacex]](*"SpaceX AI"*) · [[meta]](React 팀 이력) · Netflix(이력·*context not control*, 페이지 없음) · [[tech-bridge]]
- 제품·도구: [[pstack]](`create verification`·`recall`·full autopilot) · [[grokbot]] · Cursor projects(코디네이터 에이전트, 페이지 없음 — [[cursor]]) · [[dune-architecture|Dune]] · [[claude-opus-5-5|Opus 5.5]](선호 발언) · Chrome DevTools Protocol · Playwright · TypeScript · Electron · [[nextjs|Next.js]](비유) · Slack · Linear · Slack MCP([[model-context-protocol]]) · Lean · TLA+ · Bend(⚠️ 판독)
- 개념: [[agent-trust-curve]] · [[agent-verification-skill]] · [[build-a-lever]] · [[codebase-gardening]] · [[hard-vs-soft-enforcement]] · [[company-brain]] · [[persistent-agent-teams]] · [[verification-bottleneck]] · [[software-factory]] · [[action-reversibility]] · [[ai-formal-verification]] · [[verifiable-goals]] · [[skill-self-improvement]] · [[query-to-skill-distillation]] · [[agent-manager-analogy]] · [[context-resets-and-compaction]] · [[large-scale-code-changes]] · [[trusted-throughput]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=5tdMgKkX5dU> (1:04:03, `upload_date` 2026-10-09)
- raw: `01.raw/articles/2026-10-09_SpaceX에서 매달 수천 개의 PR을 반영하는 방법 - Lauren Tan(poteto) 팟캐스트 풀버전.md`
- 설명란 링크: Lauren의 강의 <https://youtu.be/zkmvCDSxqdc> (= [[tech-bridge-lauren-tan-2000-prs]])
- **같은 녹화의 발췌·해설**: [[tech-bridge-lauren-tan-agent-dev-workflow]] (OLYuAekOBeA, 원본 대담 링크 `MN9dGgmLyso` — ⚠️ 열어 보지 않았다)
- 같은 화자: [[tech-bridge-lauren-tan-trusting-agents]](09-12 워크숍) · [[tech-bridge-lauren-tan-2000-prs]](09-25 강연) · [[tech-bridge-grokbot-agent-teams]] · 제3자: [[tech-bridge-pstack-third-party-review]]
- 진행자 본인의 발표: [[tech-bridge-pocock-pr-bottleneck]]
- [[lauren-tan]] · [[matt-pocock]] · [[pstack]] · [[grokbot]] · [[cursor]] · [[tech-bridge]]
