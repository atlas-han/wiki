---
title: "Tech Bridge — 소프트웨어 엔지니어링은 소프트웨어 공장을 짓는 일이 된다 (Warp · Zach Lloyd): 공장 루프·공개 공장·skill loop"
type: source
tags: [software-factory, factory-engineering, sdlc, triage, spec-driven-development, code-review, verification, monitoring, skill-loop, data-plane, open-source, build-in-the-open, warp, vendor-claims, video]
source-url: https://www.youtube.com/watch?v=XyVUHSzKM2E
source-type: video
author: Tech Bridge (한영자막 재배포) · 발표 [[zach-lloyd]] ([[warp|Warp]] 창업자 — 이름·회사·이력 모두 자막에서 확인) · 행사·촬영일 미확정
date-published: 2026-10-02
ingested: 2026-10-03
created: 2026-10-03
updated: 2026-10-03
---

# Tech Bridge — 소프트웨어 엔지니어링은 소프트웨어 공장을 짓는 일이 된다 (Warp · Zach Lloyd)

[[tech-bridge|Tech Bridge]]가 재배포한 **20:09 발표(본 발표 ~16:50 + Q&A 3개), 공식 챕터 29개.** 2026-09-28부터 **멤버십 전용**이었고 2026-10-03 회차에 **공개 전환을 확인**해 ingest했다 — 공개 후 `upload_date`는 2026-10-02. 화자는 터미널에서 출발한 오픈소스 agentic development environment [[warp|Warp]]의 창업자 [[zach-lloyd|Zach Lloyd]](전 Google principal engineer, Google Docs 엔지니어링 리드). 같은 멤버 전용 묶음이던 [[tech-bridge-factory-software-factory|Factory 편]](10-01 공개)과 함께 [[software-factory]]의 **두 번째 벤더 정의**이고, 바로 전날 들어온 [[tech-bridge-conductor-orchestras-not-factories|Conductor 편]]의 "공장이 아니라 오케스트라"에 대해 **공장 은유를 정면으로 받아들이는 쪽**이다.

> **소프트웨어 엔지니어링은 "공장 공학"이 된다 — 엔지니어는 제품이 아니라 제품을 만드는 것을 짓고 관리한다. 그 공장은 특별한 게 아니라 SDLC 자체(입력 → triage → spec → 구현 → 리뷰 → 검증 → 출시 → 모니터링 → 다시 위로)를 에이전트로 돌리고 사람은 정해진 지점에서만 들어오는 그래프이며, CI/CD처럼 모든 프로젝트의 기본 인프라가 될 것이다. 공장은 측정하고(출시량 대비 사람 시간·토큰) skill loop으로 스스로 개선해야 한다.**

> *"the discipline of software engineering is going to become something more like factory engineering"* (01:24~01:31) · *"you're not just building the product, but you're building the thing that builds the product."* (14:48~14:54) · *"This loop could literally just say like the software development life cycle. It's the same thing."* (03:19~03:25) · *"everyone in here is going to code less, but they're going to ship more and that's going to be a trade-off."* (15:29~15:36)

ASR·ko 보정: ⭐ ko가 **채용 발언을 뒤집었다** — *"we're hiring more people than we've ever hired"*(18:25~18:30)가 **"저희는 지금까지 직원을 고용한 적이 없습니다"**, *"people not being hired because of AI. That's not the experience we've had"*가 **"인공지능 덕분에 사람을 고용합니다"**. ⭐ **발표의 테제 문장**(*"you're not just building the product, but you're building the thing that builds the product"* 14:48~14:54)도 ko에서 **"당신은 그저 제품을 만들고 있는 것뿐입니다"** 로 정반대가 됐다. control/data **plane**은 "계획"·"데이터 **요금제**"(12:37, 12:59), *sloppy PRs*는 "홍보가 허술해요"(07:06 — `en`도 *"public relations"*), *data mo[a]t*는 "유명 모델"(06:10 — `en`도 *"data model"*, en-orig는 *"data mode"*), agent는 "요원·상담원·담당자·대리인". **ko와 en이 오류를 공유하므로 en은 독립 확인이 아니다.** 전체 목록은 raw. **인용은 en-orig에서만** 했다.

> ⚠️ **당사자 진술, 측정 없음.** 화자는 자기 회사가 이 공장의 플랫폼을 판다(*"This uses Warp's uh agent platform as part of it, but you honestly don't have to use it. I'm not trying to like push into our product"* 16:13~16:23). 수치 — *"over 60,000 GitHub stars"*(00:56~01:00), *"a couple hundred people contributing"*(01:00~01:03), *"over 800,000 active developers"*(01:01~01:06), *"I haven't written a line of code in the last 6 months"*(00:31~00:34), *"5 years of building closed"*(06:29~06:33), *"we're hiring more people than we've ever hired"*(18:25~18:30) — **전부 화자 진술, 독립 검증 없음.** 공장의 성능·비용 효과를 보여 주는 측정치는 **하나도 없다**; build.warp.dev도 *"It's not working perfectly, but it is working"*(04:44~04:49)이라는 자평뿐.
>
> ⚠️ **행사·촬영일 미확정.** 행사명·날짜 발화 없음. 단서: *"We open sourced it a couple months ago"*(00:48~00:52), *"I went to a talk earlier that my friend Adam gave where Uber has built an internal version of this"*(11:53~11:58 — 같은 행사에 Uber 발표가 있었다), 발표 원제가 *self-improving software factories, the new open source model* 계열(00:05~00:12). [[tech-bridge-conductor-orchestras-not-factories]]의 *"The whole like talk track today is about software factories"* 와 **같은 트랙일 수 있으나 미확인**(이 영상의 자막·설명란엔 행사명이 없다).
>
> ⚠️ **챕터가 발화보다 15~35초 늦다**(전 구간 일관). 이 페이지의 시각은 en-orig 발화 기준이다. 구간 대조표는 raw.

## 1. 테제 — 공장 공학 (00:00~02:12)

- 화자: *"I am still shipping frequently, but I haven't written a line of code in the last 6 months."*(00:27~00:34) — 이 발표 전체의 1인칭 근거.
- Warp: *"open source agentic development environment. You may know us as a terminal"*(00:39~00:46), *"basically a terminal that has agents built in"*(00:46~00:51). 관심은 터미널·대화형 개발보다 *"how do you automate development?"*(01:13~01:18). → [[warp]]
- **세 단계**: *"chat and AI auto complete to cursor copilot to the phase that we're in now, which I consider to be mostly interactive agents"*(01:43~01:57) — [[claude-code|Claude Code]]·Warp에 말로 시키는 단계 — 다음은 *"over the next 6 months, a year, hard to predict the pace"*(02:04~02:08)에 **자동화**. ⚠️ 예측, 근거 없음.
- 테제: *"the discipline of software engineering is going to become something more like factory engineering"*(01:24~01:31). → [[factory-engineering]] (신규)

청중 손들기(02:14~03:02): 에이전트로 개발 *"100%"*, 여러 에이전트 동시 *"almost everyone"*, 클라우드에서 에이전트 *"less than half, but still significant"*, SDLC 전체 자동화 시스템 *"some hands"*. ⚠️ 화자 눈대중, 청중은 AI 행사 참가자.

## 2. 공장 루프 — 사람의 자리가 명시된 SDLC (03:02~04:06)

*"every project of significant size, I believe, is going to have something like this"*(03:04~03:10). 그리고 바로 낮춘다 — *"There's nothing that complicated about loops. (…) This loop could literally just say like the software development life cycle. It's the same thing."*(03:15~03:25)

| 단계 | 누가 | en-orig |
|---|---|---|
| 아이디어 유입 | — | *"ideas are going to come in at the top"* (03:25~03:30) |
| triage · (복잡하면) spec 작성 | 에이전트 | *"Agents are going to do triage. If something is complicated, they will write a spec."* (03:28~03:35) |
| spec 리뷰 | **사람** | *"these little blue boxes are where humans step in. Humans will review the spec."* (03:35~03:40) |
| 구현 | 에이전트 | (03:38~03:42) |
| 코드 리뷰 | **사람 + 에이전트** | *"A human and agent will review the code."* (03:40~03:44) |
| 검증 | 에이전트 | *"Agents will verify."* (03:42~03:44) |
| 제품 리뷰 | **사람** | *"Human will review the product."* (03:44~03:47) |
| 출시 → 모니터링 → 다시 | — | *"You ship, and then you monitor, and round and round you go."* (03:44~03:50) |

→ *"software engineers are going to be the ones who end up building and managing these factories."*(03:58~04:06)

> 위키의 정리: Factory 편의 정의(*신호 수집 → … → 학습*)와 골격은 같지만, Warp 그림은 **사람이 들어오는 세 칸(spec·코드·제품 리뷰)을 다이어그램에 박아 둔다.** → §7 Contradiction

## 3. 오픈소스와 공개 공장 (04:07~07:45)

→ [[build-in-the-open]] (신규)

- **왜 오픈소스로**: *"one of the main reasons that Warp open source was to build, uh, build a public factory"*(04:19~04:25). **build.warp.dev**가 *"all of the issues that are flowing through our system and what state they're in, what agents are working on them, what contributors are working on them"*(04:32~04:41)를 보여 준다 — *"a proto-factory done at scale"*(04:41~04:44).
- **복제가 공짜인 시대**: 만들기가 싸지면 *"it's becoming trivial to clone software"*(05:08~05:14), *"it's very hard to build a software business if it's free to build software. It's hard to capture the value, especially if a competitor can clone."*(05:21~05:30) 농담 — *"the first thing you should do is patent your code. I'm kidding."*(05:32~05:38)
- **제품 밖의 우위**: *"a great product probably was never enough"*(05:50~05:55), *"you need advantages beyond the product"*(06:02~06:05) — distribution·ecosystem·brand·data mo[a]t·capital(06:07~06:16). 스타트업엔 없다 → **공개 개발**이 돌파구.
- **효과**: 생태계, *"it can take you from being like hated on Hacker News to like tolerated"*(06:42~06:47), 브랜드, 커뮤니티. 결정에 *"5 years of building closed"*(06:29~06:33)가 걸렸다.
- **오픈소스의 전통적 고통** — *"noisy issues"*, *"sloppy PRs"*, *"code review hell"*, 변경 검증에 드는 시간(07:01~07:14) — 을 *"we built a whole set of automations, really a software factory, around managing the open source project"*(07:23~07:33)로 감당한 것이 **결정의 계기**였다.

## 4. 공장의 구성요소와 공장 바닥 (07:45~11:51)

**네 가지**(07:45~08:13): *"You need a set of automations. You need a way of providing context and skills. You need a way of bringing humans in at the correct time. It's sort of like when things get stuck on the factory. And then a really important thing is you need some set of self-improvement capabilities. So, think of this as loops."*(07:51~08:13) → [[agent-skills]] · [[skill-self-improvement]]

**예측**: *"every company every open-source project will have at its core a software factory, kind of like the way that CI/CD became just like, "Oh, of course you have that.""*(08:33~08:44)

**공장 바닥 = 단계 그래프**(08:47~09:16): *"the factory floor is basically a graph um of steps where you are defining like, "Okay, how does software get built for my product?" And it looks pretty similar for every product."*(08:56~09:11)

| 단계 | 내용 | en-orig |
|---|---|---|
| **입력** | 팀·사용자에게서 오는 아이디어. 채널은 task tracker·Slack·Teams·터미널/IDE·모니터링 시스템 | 09:20~09:48 |
| **triage** | ⭐ *"if this is easy, and this is unambiguous, just implement it. And this is how you can actually get going with a factory."* — 공장의 **시작점** | 09:50~10:09 |
| **spec** | 어려우면 spec 에이전트. Warp는 **product spec + tech spec** 두 장 — *"Product spec describes the product invariants that you're building towards. Tech spec describes the architecture and the shape of the code."* → [[spec-driven-development]] | 10:09~10:41 |
| **구현** | *"a coding agent that runs somewhere in the cloud. It makes a diff."* 에이전트 종류는 무관 → [[cloud-agent-delegation]] | 10:41~10:50 |
| **리뷰** | *"in many ways the most painful part"*. 에이전트가 먼저 리뷰하고, *"it becomes over time like a risk management exercise of like when do you bring in humans to do code review"* → [[risk-proportional-human-review]] | 10:50~11:15 |
| **검증** | *"for certain types of apps"* — computer use로 *"having the computer actually use the code that the agent produced, and producing videos and screenshots"*. CI/CD도 여전히 → [[agent-visual-qa]] | 11:15~11:33 |
| **모니터링** | *"agents don't stop in your factory when code is shipped. They should observe what's been shipped. Is it crashing? Is it being used?"* → 출력을 공장 맨 위로 되먹임 | 11:33~11:51 |

## 5. 지을까 살까, 그리고 아키텍처 (11:51~13:11)

- Uber는 내부 버전을 지었다(친구 Adam의 발표, 11:53~12:01). 그러나 *"you'll be able to build a simple version of this easily, but to build a thing that actually scales is probably like you should probably focusing on your own product, not building this infrastructure"*(12:06~12:18). ⚠️ 무엇을 사라는지는 말하지 않지만 화자는 그 인프라를 파는 쪽이다.
- **아키텍처**(12:22~13:07): ① 일을 공장에 넣는 여러 입구 ② *"a sort of control plane for figuring out how work gets distributed across your factory floor"*(12:37~12:41) ③ 실제 일이 일어나는 **클라우드 샌드박스** — *"what agent to run, so what's the harness? What's the model?"*(12:49~12:56) → [[agent-harness-design]] ④ ⭐ 그 아래 **data plane** — *"something that lets agents remember what they've done, learn, um improve over time"*(13:01~13:11). 

## 6. 측정·skill loop·엔지니어의 자리 (13:11~16:00)

- **공장은 마음가짐**: *"The factory is not just like a product, it's also a mindset."*(13:11~13:16) 효율 = *"how much software did you ship, how much did it cost in terms of human time and token time"*(13:32~13:40) — 측정하고 개선. ⚠️ 지표의 정의(출시량을 무엇으로 셀지)는 없다.
- **skill loop**(13:44~14:33): *"you're going to have your factory agents that are running skills, and then you'll have observer agents that are seeing how those skills are being applied, looking for issues and trying to improve the skills."*(14:06~14:17) 예 — 코드 리뷰 에이전트의 코멘트를 시니어 엔지니어가 고치면 *"you'd want an observer agent that would look at that and basically uh improve the code review agent for the next run."*(14:25~14:33) → [[skill-self-improvement]]
- **엔지니어의 자리**(14:35~15:59): 테제 반복 — *"you're building the thing that builds the product"*(14:51~14:54), *"more like process engineering or manufacturing"*(14:56~15:00). 기쁨이 코드 작성이면 아쉬울 것, 출시라면 *"it's never been a better time"*(15:23~15:25). *"meta-engineering, like how do you engineer your system of agents to be the best possible engineering"*(15:47~15:54). → [[factory-engineering]]
- **스타터 저장소**(16:01~16:39): QR 코드의 오픈소스 GitHub 저장소 — triage·spec 에이전트를 세우는 예제. Warp 에이전트 플랫폼을 쓰지만 필수는 아니라고. ⚠️ 저장소 URL은 자막·설명란 어디에도 없다.

## 7. Q&A (16:50~20:05)

| 질문 | 답 (en-orig) |
|---|---|
| **짓지 말라면서 당신은 공장을 짓는다 — 선은 어디?** (16:50~16:57) | *"I said something that's almost contradictory."*(16:57~17:01) 모두가 공장을 배치하되 *"the tuning of the factory, the like, are these the right skills for my domain? Is this factory building my product in the right way?"*(17:07~17:17)에 엔지니어링 과제가 남는다. 대부분은 핵심 제품에 집중(17:22~17:34) |
| **지금 졸업한다면?** (17:39~17:47) | *"the most important skills in this new world are adaptability. I think that that's critical thinking. It's like this the speed at which you can learn."*(17:54~18:05) + *"understanding like the underlying systems and architecture"*, 에이전트가 쓴 코드·spec을 이해·추론하는 능력(18:08~18:21). ⭐ *"we're hiring more people than we've ever hired"*(18:25~18:30), AI 때문에 채용이 안 된다는 건 *"misdirection"* — *"That's not the experience we've had so far."*(18:30~18:37) 찾는 사람: *"really adaptable product-focused thinkers"*(18:39~18:44) |
| **제품 발견·비전·taste는?** (18:53~18:59) | *"the problem with the factory metaphor, even though I'm like leaning into it (…) is that it can kind of sound like uh mechanizing or dehumanizing."*(19:14~19:23) 그러나 *"the only thing that matters is like are you building something useful?"*(19:26~19:29) — *"human taste, human input, human product sense, um humans like guiding at those touch points where you can't automate stuff is absolutely like essential"*(19:36~19:49) → [[taste-vs-judgment]] |

## 이 위키와의 연결

### 이어지는 것

- **[[software-factory]]** — Factory(Tereza)에 이은 **두 번째 벤더 정의**. 골격(전 생애주기 루프 + 지속 개선)은 같고, Warp는 **SDLC와 같은 것**이라고 낮추며 **사람 칸**과 **data plane**을 명시한다.
- **[[spec-driven-development]]** — triage가 "어려움"으로 분류한 것만 spec으로 가고, spec은 **product(불변식) / tech(아키텍처·코드 모양)** 두 장.
- **[[skill-self-improvement]]** — **사람의 교정을 관찰하는 observer 에이전트**라는 다섯 번째 경로.
- **[[risk-proportional-human-review]]** — 코드 리뷰의 사람 투입을 *"risk management exercise"*(11:05~11:10)로 본다.
- **[[agent-visual-qa]]** — 검증 단계의 computer use + 영상·스크린샷.
- **[[cloud-agent-delegation]]** — 구현이 *"runs somewhere in the cloud"*, 실행 장소가 클라우드 샌드박스.

### 갈리는 것

> ⚠️ **Contradiction: 공장 은유 — 받아들일까, 버릴까.** [[orchestras-not-factories]]의 Charlie Holtz([[conductor|Conductor]])는 *"I honestly kind of hate the term"* 이라며 사람이 *"factory line managers like pushing buttons"* 가 되는 미래를 거부했다. Zach Lloyd는 같은 위험(*"mechanizing or dehumanizing"* 19:20~19:23)을 **인정하면서도 은유에 기댄다**(*"leaning into it"* 19:16~19:17) — 사람은 라인 관리자가 아니라 **공장을 설계·튜닝하는 엔지니어**이고, taste가 들어가는 touch point를 지킨다. 두 사람 모두 **사람의 taste·리뷰가 중심**이라는 데서는 만난다 — 갈리는 것은 운영 모습보다 **은유의 선택**이다. 둘 다 측정은 없다.

> ⚠️ **Contradiction: 사람이 루프 안 어디에 있나.** [[tech-bridge-factory-software-factory|Factory]]는 에이전트가 *"a year or more years without the human in the loop"* 돌 것이라는 예측(03:51~03:58)과 *"we just monitor and decide what to build"*(20:48~20:51)로 사람을 **루프 밖 감독자**에 둔다. Warp의 루프는 **spec·코드·제품 리뷰 세 칸**에 사람을 고정하고(03:35~03:47), 코드 리뷰에서 사람을 빼는 시점을 *리스크 관리*로 정한다. 같은 "software factory"라는 말 아래 **사람 게이트의 위치가 다르다.**

> ⚠️ **Contradiction: 직접 지을까.** Factory는 *"rebuild it from scratch"*(조직을 다시 짓는다)라 했고, Warp는 *"you should probably focusing on your own product, not building this infrastructure"*(12:12~12:18) — 공장 인프라는 들여오고 **튜닝만** 하라. 둘 다 그 인프라를 파는 회사다.

## 해소하지 않고 표시만 한 것

- **수치 전부** — 60,000 stars, 수백 명 기여자, 800,000 활성 개발자, 6개월 무코딩, 5년 closed, 역대 최다 채용. 화자 진술.
- **"6개월~1년 안에 자동화로"** — 예측.
- **"data mode"** — data moat로 판독(raw 보정 목록).
- **"identical slop"**(10:57~11:01) — 원래 단어 미확정.
- **스타터 저장소 URL** — QR 코드뿐, 자막·설명란에 없다.
- **Adam / Uber 발표** — 성·제목 없음. 이 위키에 해당 소스 없음.
- **효율 지표** — *출시량 / (사람 시간 + 토큰)* 을 무엇으로 세는지 없음.

## 등장 개체

- 인물: [[zach-lloyd]] (신규) · Adam(Uber 발표자, 성 미발화 — 페이지 없음)
- 조직·제품: [[warp]] (신규, 제품 겸 회사 — build.warp.dev 포함) · Google(Google Docs, 이력) · Uber(내부 공장, 일화) · [[cursor|Cursor]] · Copilot · [[claude-code|Claude Code]] · GitHub · Slack · Teams · Hacker News
- 개념: [[factory-engineering]] (신규) · [[build-in-the-open]] (신규) · [[software-factory]] · [[spec-driven-development]] · [[skill-self-improvement]] · [[agent-skills]] · [[risk-proportional-human-review]] · [[agent-visual-qa]] · [[cloud-agent-delegation]] · [[agent-harness-design]] · [[orchestras-not-factories]] · [[taste-vs-judgment]] · [[ai-slop]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=XyVUHSzKM2E> (20:09, `upload_date` 2026-10-02 — 09-28~10-02 멤버십 전용)
- raw: `01.raw/articles/2026-10-02_소프트웨어 엔지니어링은 이제 소프트웨어 공장을 짓는 일이 될 것입니다 — Zach Lloyd (Warp).md`
- 설명란 링크: <https://www.warp.dev> · <https://build.warp.dev> · <https://x.com/zachlloydtweets> · <https://www.linkedin.com/in/zachlloyd/> (⚠️ 열어 보지 않았다)
- 같은 주제: [[tech-bridge-factory-software-factory]] · [[tech-bridge-conductor-orchestras-not-factories]] · [[tech-bridge-sdd-enterprise-lessons]]
- [[tech-bridge]] · [[zach-lloyd]] · [[warp]]
