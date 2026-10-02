---
title: "Tech Bridge — 공장이 아니라 오케스트라입니다 (Conductor · Charlie Holtz): 조직에서 가장 빠른 빌더의 여섯 원칙"
type: source
tags: [coding-agents, multi-agent, conductor, slop-free-zone, company-brain, cloud-sandbox, collaboration, software-factory, frontier, claude-md, agent-skills, video]
source-url: https://www.youtube.com/watch?v=WWUxQgAZTu4
source-type: video
author: Tech Bridge (한영자막 재배포) · 발표 [[charlie-holtz]] ([[conductor|Conductor]] 공동 창업자 — 자막엔 이름 없음, 설명란 표기) · 설명란상 AI Engineer World's Fair(자막엔 행사명 없음 — 촬영일 미확정)
date-published: 2026-10-01
ingested: 2026-10-02
created: 2026-10-02
updated: 2026-10-02
---

# Tech Bridge — 공장이 아니라 오케스트라입니다 (Conductor · Charlie Holtz)

[[tech-bridge|Tech Bridge]]가 재배포한 **16:56 무대 발표**(Q&A 없음, 공식 챕터 13개). 화자는 여러 코딩 에이전트를 한 데스크톱 앱에서 동시에 다루는 [[conductor|Conductor]]의 공동 창업자 [[charlie-holtz|Charlie Holtz]]. Conductor를 만들며 *"I've seen a lot of the best builders up close"*(01:03~01:07) — 그 관찰을 **"조직에서 가장 빠른 빌더가 되는 원칙" 여섯**으로 묶었다. 원칙 5 뒤에 이번 주 출시라는 **클라우드 버전 Conductor 데모**가 붙는다.

> **최전선 가까이 머물되 워크플로 다듬기에 빠지지 말고(모두에게 통할 것은 랩이 기본값으로 넣는다), 사람이 엄격히 지키는 '슬롭 없는 구역'을 정하고, 회사의 모든 기록을 DB 하나에 모아 에이전트에게 주고, 에이전트를 노트북 밖 샌드박스에 풀어놓아라. 그리고 이 모든 것을 '소프트웨어 공장'이 아니라 '오케스트라'로 생각하라 — 사람이 조립 라인 관리자가 아니라 지휘자로 가운데 서야 한다.**

> *"Staying near the frontier means you are always trying the latest things basically the day they come out."* (01:41~01:47) · *"why isn't this workflow the default"* (03:32~03:38) · *"a slot[=slop]-free zone is a part of the codebase or a part of the app that requires really strict human review"* (05:05~05:17) · *"the title of this talk is orchestras not factories"* (14:18~14:23) · *"I don't want to be in in my dark factory. Um I don't want to be a line manager."* (16:01~16:05)

ASR·ko 보정: ⭐ ko가 **결론의 부정 두 개를 둘 다 뒤집었다** — *"I don't want to be in my dark factory. I don't want to be a line manager"*(16:01~16:05)가 **"나는 어두운 내 공장에 있고 싶다 … 저는 라인 관리자가 되고 싶습니다"**. *30,000 **line** PRs*는 **"3만 건의 구매 요청(PR)"**(05:22, 단위가 줄 → 건으로, PR에 없는 풀이), *feature factories*는 **"함수"**(15:28 — `en`도 *"function factories"*), *zoom out*은 **"가끔씩 시간을 낸다"**(15:12, 빈도까지 반전), 요약의 *Create slop-free zones*는 **"개방적인 공간을 만드세요"**(16:30, 정반대), *database*는 **"받침대"**(08:05), *git worktree*는 **"전선이 나무에"**(10:07), *Ralph loops*는 **"추론 루프"**(03:39 — `en`도 같은 오류)가 됐다. Conductor는 **"Driver"·"운전기사"·"Coda"**로 14회 이상, frontier는 **"국경"**으로 10회 이상 바뀐다. en-orig 자체는 **slop을 "slot"으로** 여섯 번 들었고 공식 챕터("슬롭 없는 청정 구역")가 바로잡는다. 전체 목록은 raw. **인용은 en-orig에서만** 했다.

> ⚠️ **당사자 진술, 측정 없음.** 화자는 멀티 에이전트 데스크톱 앱 회사의 공동 창업자이고 발표의 3분의 1(09:28~14:08)이 **자사 신제품 데모**다. *"three to six months behind"*(02:52~02:54), *"rewrite our whole app like a couple of times"*(05:44~05:46) 등 **수치는 전부 일화**다. 원칙 4의 근거는 *"I think this this tweet sums it up pretty well"*(08:01) — 트윗 원문·작성자는 자막에 없다.
>
> ⚠️ **행사·촬영일 미확정.** 설명란은 AI Engineer World's Fair라 하지만 자막엔 *"about AI engineering"*(00:18~00:20)과 *"The whole like talk track today is about software factories"*(14:23~14:30)뿐이다. 시점 단서 — *"back in February of last year"*(02:16~02:18), *"coming out this week"*(09:36~09:39), *"the two days of Fable"*(11:10~11:12) — 는 날짜를 주지 않는다.

## 0. Conductor와 관찰의 자리 (00:35~01:34)

*"Conductor is a desktop app for managing a team of coding agents all at the same time. So instead of having a bunch of terminal windows for your cloud[=Claude] codes or your codeexes[=Codex] or your uh whatever uh coding agent, you have one interface to manage them all."*(00:45~00:59) → [[conductor]] · [[claude-code]] · [[codex]]

이 발표의 모든 원칙은 **도구 판매자가 사용자를 관찰한 것**이다 — *"I've like watched their workflow. I've seen how they work. I've seen the things they do do and the things that they avoid doing."*(01:07~01:13)

## 1. 최전선 **가까이** 머물러라 (01:34~03:00)

새 도구는 **나온 날** 써 본다 — *"when uh uh ultra code comes out you're trying it. It means that when uh uh slashgo[=/goal?] comes out you're giving it a go"*(01:47~01:56). ⚠️ *ultra code*는 Claude Code 설정 [[ultracode]]일 수 있으나 화자는 제품을 밝히지 않고, *slashgo*는 `en`이 `/goal`로 판독했을 뿐 어느 제품의 명령인지 없다.

이유 둘:

- **스타트업이면 아이디어가 나온다.** Conductor 자신이 그 증거다 — Chorus라는 전혀 다른 앱을 만들다가 *"we were such power users of cloud[=Claude] code back in February of last year that we uh started building our whole workflow around cloud code and we started cloning our repo five times and then we discovered work trees and then bit by bit we had built conductor as an internal tool"*(02:14~02:30).
- **회사원이면 최신 워크플로를 아는 사람이 되어라.** 예전엔 소셜 그래프로 흘러 내려왔지만 *"things just like move way too fast now. You're you're always going to be three to six months behind if you do that."*(02:49~02:54) ⚠️ 3~6개월은 근거 없는 감각치.

## 2. 시장을 이기려 하지 마라 (03:00~04:58)

→ [[dont-beat-the-market]] (신규)

핵심어는 **near**다 — *"there is a danger if you are at the frontier. Um you can you can do what uh I call midw meing[=midwit memeing?] where you're spending all of your time working on your workflow and not doing actual work."*(03:00~03:12)

**휴리스틱**: *"you should ask yourself why isn't this workflow the default"*(03:32~03:38). 예 — [[ralph-wiggum-method|Ralph loop]]가 유행할 때 거기에 맞춰 워크플로를 다듬어야 하나? *"if Ralph loops work for everyone, like if they are the default, um then you probably should just wait for Anthropic or OpenAI or whatever to build the uh workflow into the into the default harness"*(03:50~04:05).

**효율적 시장 가설** 비유 — *"unless you have like real alpha, uh, you shouldn't be optimizing your workflow too much"*(04:06~04:14). **real alpha** = *"some kind of information about either your users or your codebase that the models might not know about"*(04:16~04:23). Conductor의 예: 채팅 앱이라 아주 긴 채팅을 빨리 렌더링해야 하고, 그래서 React 쿼리 최적화에 시간을 쓰고 **다른 부분을 희생할 의지가 있다**(04:23~04:42). 맺음: *"Don't don't be the person who has an amazing Emac[=Emacs] setup but like doesn't actually get stuff done."*(04:54~04:58)

> 위키의 정리: [[harness-pruning]]이 *만드는 쪽*에서 "모델이 좋아지면 하네스 기능을 지운다"를 말했다면, 이것은 **쓰는 쪽**의 같은 결론이다 — 범용 워크플로는 곧 기본값에 흡수되니 **흡수되지 않을 것(모델이 모르는 내 정보)에만 투자하라.** [[ride-the-optimization-trajectory]]와는 짝이 맞는다(랩의 궤적 위에 얹고, 궤적이 해 줄 것은 직접 하지 않는다).

## 3. 슬롭 없는 구역을 만들어라 (04:59~06:58)

→ [[slop-free-zone]] (신규)

*"a slot-free[=slop-free] zone is a part of the codebase or a part of the app that requires really strict human review"*(05:05~05:17). 오해에 대한 반박으로 시작한다 — *"a lot of people assume that we are pure token maxers and we are like ripping through like 30,000 line PRs, but we're actually not. We're actually quite careful with certain parts of our codebase and then very loose with other parts"*(05:18~05:31). → [[value-maxing]]

**대가를 치르고 배웠다**: *"We we've had to rewrite our whole app like a couple of times because we weren't careful about slot[=slop] free zones."*(05:42~05:48) → [[slop-cannon]]

구역의 구체:

| 구역 | 장치 | en-orig |
|---|---|---|
| **migrations 파일** | ⭐ *"in our CI uh any change to migrations file requires the a uh a human to review it"* — **유일하게 강제 게이트로 말해진 것** | 05:51~06:02 |
| **Slack** | *"we also assume that anything written in Slack is slop free. It's it's not written by the AI, it's written by a human"* — **가정** | 06:02~06:07 |
| **docs · CLAUDE.md · 스킬** | *"we put a ton of time into making them good"* — 최고 빌더들도 *"put an unusual amount of time into the CloudMD[=CLAUDE.md] or their skill files"* | 06:07~06:23 |

**인턴 비유**(06:26~06:58): 새 인턴이 일을 시작할 때마다 — 매일, 앉을 때마다 — 귀에 무언가를 속삭일 수 있다면 무엇을 속삭일지 많이 고민할 것이다. *"And this is what the cloud MD or agents uh MD is. It's like information that gets loaded into the agents context every time they start working."*(06:45~06:52) → [[context-engineering]] · [[agent-skills]] · [[claude-code]]

## 4. 괴물에게 먹이를 줘라 (06:58~08:13)

→ [[company-brain]]

사내 도구 **Conductor Internal Agent = "CIA"**(07:03~07:13)가 *"the centralized database of everything that's happening in the organization"*(07:16~07:21)다. Slack 새 메시지 → CIA가 집어 *"save it to a Postgress[=Postgres] uh uh table"*(07:28~07:31), Discord의 사용자 버그 요청도 같게, 회의는 녹음해 CIA로(07:31~07:40). 이유: *"you want them to have as much information and as much context as they can have about the way you guys specifically work. And the best way to do that is by having a centralized place for all the information to go."*(07:48~07:58) 처방: *"it's really effective to just put everything in a database and then give your agent a SQL tool and let it handle uh uh handle the rest"*(08:01~08:13).

## 5. 방목형 에이전트 (08:16~09:26)

→ [[cloud-agent-delegation]]

*"Give them give them a sandbox where they that won't get killed, where they can explore your codebase, where they can work on really hard tasks, where they can they know that they're not going to get shut down when you close your laptop lid."*(08:25~08:36) 그리고 **스스로를 더 만들 기회**(*"opportunities to create more of themselves"* 08:39~08:40), **다른 에이전트·사람과의 협업**(08:44~08:46). 이유는 추세 — *"the models are getting better and they are able to run for much longer and they're going to be many more of them. And so if they are confined to your laptop, then the they're not going to be nearly as effective"*(08:53~09:08). 노트북 밖으로 나오면 *"there's a bunch of really cool stuff that you can build on top"*(09:16~09:18).

## 6. 데모 — 클라우드 Conductor (09:28~14:08)

| 장면 | 내용 | en-orig |
|---|---|---|
| **클라우드 샌드박스** | 이번 주 출시 버전은 *"centered around collaboration in the cloud"*. 워크스페이스마다 구름 아이콘 → 샌드박스 정보. 노트북을 덮어도 계속 돈다. ⭐ *"Up until basically this week, every uh every task in conductor was built on a git work tree, but now they're in a cloud sandbox."* | 09:36~10:14 |
| **실시간 협업** | 동료(Caden·Lewis·Tywin·Jackson — ASR 철자)가 무엇을 하는지 목록으로 보고 들어가 실시간으로 본다. 동료 워크스페이스의 변경을 리뷰하고 *"can we actually use tabs, not spaces?"* 를 남기면 그가 실시간으로 보고 같은 워크스페이스에서 채팅한다 | 10:22~12:29 |
| **스스로 띄우는 API** | *"we can give the agents APIs to spawn themselves"* — 화자의 [[openclaw\|OpenClaw]] "Lord Crandon"이 Conductor API를 갖고 있어 휴대폰·Telegram·Slack에서 *"create a new workspace for me that makes uh yeah makes all the buttons blue"* 를 보내면 워크스페이스를 만들고 일을 시작한다 | 12:55~14:03 |

협업이 왜 중요한가 — *"collaboration is the the one one of the most important new concepts uh in these tools that no one is really talking about right now"*(10:49~10:56). 이유 둘: *"all great things are built with teams of people"*(11:02~11:05), 그리고 *"as the models get better, um, as we've seen this with the two days of Fable, you can get a lot more ambitious (…) you're going to need more people and more agents to work on those things"*(11:07~11:19). → [[multiplayer-agent-context]] · [[fable-5-1]]

> ⚠️ 데모는 **동료의 실시간 응답을 기다리다 끝난다** — *"Seems like he's typing a lot."*(12:07), *"Okay, come back. The agents have escaped."*(12:37~12:38). 협업 기능의 실제 결과(그 동료가 무엇을 바꿨는지)는 보이지 않는다.

## 7. 공장이 아니라 오케스트라 (14:15~16:19)

→ [[orchestras-not-factories]] (신규) · [[software-factory]]

**행사 트랙 자체에 대한 반론**이다 — *"The whole like talk track today is about software factories and I honestly kind of hate the term. I think it's the wrong way of thinking about these new tools that are emerging."*(14:23~14:34) 자동화의 효율은 인정하되 *"I don't want the future to be built around factories"*(14:47~14:52).

**지휘자 이미지**: *"I want to be like in front of an orchestra like waving my baton and and like I wave it this way and this this team of agents starts working and then this intermingling of humans and agents starts working as I go here and I when I want to I can zoom in on the details but most of the time I can zoom out"*(14:57~15:14).

**거부하는 이미지**: *"I don't think the future should be we are like managing swarms of agents and we are like factory line managers like pushing buttons getting the agents to like pump out the next feature like we we we tried this like 10 years ago with the term feature uh feature factories and it just doesn't work."*(15:14~15:33) — ⭐ **10년 전 "feature factory"의 실패**를 지금의 "software factory"에 겹친다.

**근거는 효율이 아니라 경험과 책임이다**: *"I want my software to feel human and crafted. Um I want to feel like a human at the center of it all. And I think because we're all building these tools, we actually have a responsibility to make the tools um great for humans. I think it's really important to like use the words that make us feel excited"*(15:30~15:50). 맺음 — *dark factory*도 *line manager*도 아니라 *"I want to feel like I'm Steve Jobs designing the Mac with a team of amazing humans and AI agents all in the same place"*(16:09~16:17).

> 위키의 정리: 이 원칙은 **측정 주장이 아니라 언어 선택의 주장**이다 — *"use the words that make us feel excited"*. 화자는 공장 모델이 덜 생산적이라는 증거를 대지 않는다. 그리고 **사람이 "대부분 줌아웃"한 채 에이전트 팀을 움직인다**는 그의 그림은, 공장 은유와 운영상 무엇이 다른지(누가 무엇을 리뷰하는가)를 발표 안에서 **원칙 3(슬롭 없는 구역)으로만** 답한다.

## 8. 요약 (16:22~16:50)

*"stay near the frontier. Don't try and beat the market. Create slot[=slop] free zones. Feed the beast freerange agents and think about orchestras, not factories."*(16:26~16:40) 약어 *"Stickfo"*(16:40~16:42) — ⚠️ 여섯 원칙의 머리글자와 맞지 않는다, 원래 철자 미확정.

## 이 위키와의 연결

### 이어지는 것

- **[[company-brain]]** — 원칙 4는 **세 번째 형식**이다: PromptQL의 *사람이 승인하는 링크된 마크다운*, Vercel의 *에이전트가 grep하는 시맨틱 레이어*에 이어 **원천 기록(Slack·Discord·회의 녹음)을 자동 수집한 Postgres + SQL 도구**.
- **[[cloud-agent-delegation]]** — *노트북을 덮어도 계속 도는 샌드박스*가 다시 나온다. Conductor는 이 전환을 **git worktree → 클라우드 샌드박스**라는 제품 이력으로 증언한다(10:06~10:12).
- **[[multiplayer-agent-context]]** — 그 페이지는 *여러 사람이 에이전트 하나*, [[persistent-agent-teams]]는 *사람 하나가 에이전트 여럿*. Conductor 데모는 **여러 사람 × 여러 에이전트 워크스페이스를 실시간 공유**한다.
- **[[harness-pruning]] · [[ride-the-optimization-trajectory]]** — 원칙 2가 **사용자 쪽**의 같은 논리(범용 워크플로는 기본값에 흡수된다).
- **[[ai-slop]] · [[slop-cannon]]** — 원칙 3은 슬롭 논의에 **"어디서" 축**을 더한다: 전부를 막는 게 아니라 구역을 정해 엄격하게, 나머지는 느슨하게. 앱을 두어 번 다시 썼다는 고백은 [[slop-cannon]]의 Dioxus 사례와 같은 결.
- **[[risk-proportional-human-review]]** — *결정의 위험도*로 사람 자리를 정하는 원칙의 **코드베이스 구역판**: migrations처럼 되돌리기 어려운 곳에 CI 게이트.
- **[[openclaw]]** — 개인 에이전트가 다른 에이전트 제품의 API를 호출해 일을 위임하는 사례(Lord Crandon → Conductor API).

### 갈리는 것

> ⚠️ **Contradiction: 사람은 루프 밖인가, 가운데인가.** [[frontier-engineering]](Amazon, 08-30)의 frontier developer는 *생산 코드의 1~2%만 사람*, *드문 개입*, *여러 에이전트 병렬로 유휴 최소화*다. 이 발표는 *"managing swarms of agents (…) like factory line managers"*(15:17~15:22)를 **거부하고** *"a human at the center of it all"*(15:35~15:39)을 요구한다. 다만 화자도 *"most of the time I can zoom out"*(15:12~15:14)이라 하고 자기 제품이 에이전트 팀 관리 도구다 — **운영 모습보다 은유와 사람의 자리에 대한 태도가 갈린다.** 어느 쪽이 더 빠른지 측정은 양쪽 다 없다.

> ⚠️ **Contradiction: 회사 지식에 사람 게이트가 필요한가.** [[company-brain]]의 PromptQL 설계는 **자동 추가 금지**(에이전트는 제안만, 사람이 이름을 걸고 수락 → [[no-silent-write]]). Conductor의 CIA는 Slack·Discord·회의 녹음을 **자동으로 전부** Postgres에 쌓는다. 화자의 구분은 **원천 기록 vs 큐레이션 문서**로 보인다 — Slack은 *사람이 쓴 것이라 슬롭 없음*으로 가정하고, 사람 손을 거치는 것은 docs·CLAUDE.md·스킬이다. ⚠️ 이 구분은 위키의 정리이며 화자가 명시하지 않는다. CIA의 **접근 권한·민감 정보 처리**는 발화되지 않는다.

> ⚠️ **"Slack은 슬롭이 없다"는 가정이다.** *"we also assume"*(06:02). 사람이 AI 출력을 Slack에 붙여 넣는 경우는 다뤄지지 않는다 — [[ai-slop]]의 *"인간 슬롭"* 논의와 부딪힌다.

## 해소하지 않고 표시만 한 것

- **수치 전부** — 3~6개월 뒤처짐, 저장소 5회 복제, 앱 재작성 두어 번, 10년 전 feature factory. 전부 일화.
- **원칙 4의 근거 트윗** — 원문·작성자 없음(08:01).
- **"ultra code"·"slashgo"** — 제품·명령 특정 불가. [[ultracode]] 연결은 추정.
- **"the two days of Fable"** — 출시 직후인지, 이틀 써 본 경험인지, 버전이 무엇인지 미확정 → [[fable-5-1]]에 기록만.
- **"Stickfo"** — 철자 미확정.
- **CIA의 권한·보존·민감 정보** — 없음.
- **클라우드 샌드박스의 구현** — 어느 인프라인지, 비용, 격리 수준 없음.
- **화자 이름(Charlie Holtz)·행사(AI Engineer World's Fair)** — 설명란에만.

## 등장 개체

- 인물: [[charlie-holtz]] (신규) · 동료 Caden(ASR 변이 Kaden·Cadence·Ken) · Lewis · Tywin · Jackson (철자 미확정, 페이지 없음) · Steve Jobs (비유)
- 조직: [[conductor]] (신규, 제품 겸 회사) · [[anthropic]] · [[openai]] · [[ai-engineer]] (설명란의 행사)
- 제품·도구: [[claude-code]] · [[codex]] · [[openclaw]] ("Lord Crandon") · [[fable-5-1|Fable]] · [[ultracode]](추정) · CLAUDE.md / AGENTS.md · git worktree · Postgres · Slack · Discord · Telegram · Emacs · React · Chorus(Conductor 팀의 이전 앱)
- 개념: [[orchestras-not-factories]] (신규) · [[slop-free-zone]] (신규) · [[dont-beat-the-market]] (신규) · [[software-factory]] · [[company-brain]] · [[cloud-agent-delegation]] · [[multiplayer-agent-context]] · [[ralph-wiggum-method]] · [[ai-slop]] · [[slop-cannon]] · [[frontier-engineering]] · [[harness-pruning]] · [[ride-the-optimization-trajectory]] · [[risk-proportional-human-review]] · [[value-maxing]] · [[context-engineering]] · [[agent-skills]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=WWUxQgAZTu4> (16:56, `upload_date` 2026-10-01)
- raw: `01.raw/articles/2026-10-01_공장이 아니라 오케스트라입니다 — 최고 속도로 개발하는 사람들의 일하는 방식.md`
- 설명란 링크: <https://x.com/charlieholtz> · <https://www.conductor.build> (⚠️ 열어 보지 않았다)
- 같은 주제: [[tech-bridge-frontier-engineering]] · [[tech-bridge-company-brain-security]] · [[tech-bridge-lauren-tan-2000-prs]] · [[tech-bridge-ambitious-software-agent-era]] · [[tech-bridge-introspection-loop-is-the-product]]
- [[tech-bridge]] · [[charlie-holtz]] · [[conductor]]
