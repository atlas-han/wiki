---
title: "Tech Bridge — Grok Bot은 매니저, Claude Code는 개발자 (Rob Shocks): first mile · last mile, Lauren Tan의 다섯 단계 루프, 신뢰의 역피라미드, 공유 컴퓨터의 자격 증명"
type: source
tags: [grokbot, claude-code, cursor-cloud, orchestration, manager-bot, first-mile, last-mile, lauren-tan, fix-and-fuzz, auto-merge, inverse-pyramid, hard-vs-soft-enforcement, blast-radius, risk-proportional-review, rice-scoring, backlog, agent-sandboxing, credentials, software-factory, rob-shocks, vendor-claim, video]
source-url: https://www.youtube.com/watch?v=ra5WyQ-hKN4
source-type: video
author: Tech Bridge (번역 재배포, 내레이션 없음) · 원 제작자 · 발표자 [[rob-shocks]](설명란 근거 — 발화에 이름 없음, 1인칭 "my own factory" · "this channel") · 원본 채널명 · 원본 링크 · 녹화일 미상
date-published: 2026-11-02
ingested: 2026-11-03
created: 2026-11-03
updated: 2026-11-03
---

# Tech Bridge — Grok Bot은 매니저, Claude Code는 개발자 (Rob Shocks)

[[tech-bridge|Tech Bridge]]의 **12:33 1인 해설 영상, 공식 챕터 8, 내레이션 없음.** 오디오는 `English (US) original (default)` + 더빙 7개 언어이고 **한국어 트랙 · `ko-orig`가 없다** — 10-27 Voss 편 이후 이어지는 영어 원본 오디오만 있는 구성이라 **인용은 en-orig로만** 한다. 제목의 "[한글자막]"과 달리 수동 자막은 없다. 00:00~00:21(첫 챕터 "소개" 전체)은 무캡션이고, **마지막 문장은 *"and review comes"*(12:30)에서 잘린다.** `upload_date` 20261102 = 18:00 KST. raw: `01.raw/articles/2026-11-02_Grok Bot은 매니저 Claude Code는 개발자 AI 에이전트를 함께 쓰는 법.md`.

[[rob-shocks|Rob Shocks]](설명란 근거)가 [[grokbot|GrokBot]]을 **코딩하지 않는 매니저**로 두고 실제 코드는 [[claude-code|Claude Code]] · [[cursor-cloud|Cursor Cloud]] agents에 넘기는 구성을 설명한다. [[lauren-tan|Lauren Tan]]의 글 · 영상을 두 번 요약하고(다섯 단계 루프 · 역피라미드), Anthropic 등 회사 사례를 한 문장씩 붙이고, 자기 구성을 보여 준다. 테제(발표자):

> **봇은 매니저다 — 무엇을 지을지(first mile)와 끝났는지 확인하기(last mile)만 맡고, 가운데의 코드 작성은 코딩 에이전트에게 넘긴다. 에이전트를 늘리기 전에 하나를 믿을 수 있게 만들고, 교정할 때마다 그 수정을 스택 위쪽(코드 → 린트 → 규칙 파일)으로 올린다. 통제는 에이전트가 아니라 환경에 둔다.**

> *"Your bot should be the manager here, not the coder."*(00:21~00:23) · *"how can you manage 50 agents if you can't even trust one?"*(05:09~05:11) · *"don't go building 50 agents. Start with one loop"*(12:07~12:10)

### 세 층을 나눠 읽는다

| 층 | 무엇 | 근거의 성격 |
|---|---|---|
| **[Lauren]** | 팀 엔지니어 봇 글, 다섯 단계 루프 · 1시간 자동 머지, 역피라미드 4층, 미슐랭 주방, GrokBot 루틴 | 발표자가 글 · 영상을 요약한 **2차 전달** — 원 글 링크 없음 |
| **[회사]** | Anthropic(녹색 · 노랑 · 빨강, 6~9월 수치, *"move most of the review reading to machines"*), Alan Wells(6주), Stripe · Vercel(Slack), Theo(T3 Code), Docker 등(참조 아키텍처) | 한두 문장씩의 전달, 출처 미발화 |
| **[Rob]** | 메인 에이전트 Chief, 봇별 좁은 권한, Mac 컨테이너 · VPS, RICE + blast radius 백로그, 리뷰 등급, 시작 규칙 | 발표자 자기 구성 — 시연 · 서술이고 측정 없음 |

> ⚠️ **화자 귀속은 설명란 근거다.** 발화 · 태그에 이름이 없고 원본 링크가 없다. 자기 언급 *"I covered a lot of that in Entropic's SDLC in a video while back"*(00:34~00:38) · *"some of her skills we covered on Pystack in another video previously"*(03:31~03:34)이 가리키는 주제는 이 위키에 **화자 미상**으로 들어온 두 편([[tech-bridge-ai-native-sdlc]] · [[tech-bridge-pstack-third-party-review]])과 겹친다. 같은 사람일 가능성만 있고 확인하지 않았다 → [[rob-shocks]].

## 1. 소개 (00:00~00:21)

en-orig에 발화가 없다(무캡션, 첫 큐 00:21.4). 이 챕터의 내용은 쓰지 않는다.

## 2. 봇은 매니저, 코딩은 에이전트 (00:21~02:55)

- ⭐ **first mile · last mile** — *"The first is what the Grok team call the first mile. And this is working out what to build."*(00:25~00:29) GrokBot은 *"connected to multiple different channels to manage intent. So, that's Slack, email, X, linear"*(00:40~00:44). *"The second is the last mile, which is checking the work. So, chasing up on it, telling you what's done, keeping an eye on the task list."*(01:00~01:06) 가운데: *"The bit in the middle really is doing the work, writing the code. And that's what coding agents like Claude code, Codex, and Crusher[=Cursor] are really built for."*(01:24~01:29)
  - ⚠️ "first mile"이 **Grok 팀의 용어**라는 것은 발표자 진술이다(설명란의 x.ai 가이드 링크는 열어 보지 않았다).
- **도구 중립** — *"you don't have to use GrokBot as your orchestrator. You can actually set up your own agents or use Claude projects or use Crusher[=Cursor] projects"*(01:09~01:17).
- **[Lauren]** *"Lauren has a post exactly on this. It's basically about making a team engineer bot. Then you add it to Slack and tag it whenever you want some coding done."*(01:38~01:47) — 클라우드 에이전트가 자기 컴퓨터를 가지므로 *"it frees up your main orchestrator bot to be more of a manager"*(01:51~01:55).
- **[회사]** *"all these software factories I've covered from lots of the big companies like Stripe, Vercel, etc. They all tend to use Slack as their way of managing their agents."*(01:58~02:07)
- ⭐ **[Rob] 나누는 이유 둘** — ① 비용: ⚠️ *"Grokbot runs on one weekly usage pool that's shared with Grok and Cursor. They have a unified plan now."*(02:22~02:28) → GrokBot에 코딩을 다 시키면 크레딧이 빨리 닳으니 *"I much prefer offload to the subscription that I have with Cloud Code[=Claude Code] or Open Code."*(02:34~02:38) ② 격리: *"Splitting the work also gives you isolation because every worker get its own computer, its own context, and its own kill switch."*(02:38~02:44) 실행 환경은 Mac의 컨테이너와 VPS(02:46~02:53).

→ [[manager-bot-coding-agent-split]](신규) · [[inner-outer-meta-loops]] · [[cloud-agent-delegation]]

## 3. 로런의 다섯 단계 작업 루프 (02:55~04:48) — [Lauren] 발표자 전달

| 단계 | 내용 (en-orig) |
|---|---|
| 1 | *"watch a Slack channel for feedback about the app"*(03:00~03:04) — 팀 채널에 누군가 맥락을 쏟아 놓는다 |
| (2) | *"Grokbot picks up on that and creates a ticket in linear."*(03:10~03:15) |
| (3) | *"from linear or Jira or whatever, a Cursor Cloud agent is triggered to go and reproduce the issue on its own computer."*(03:15~03:21) |
| 4 | 버그를 재현하고 *"what she calls a fix and fuzz pull request with a small swarm of agents"*(03:24~03:28) — *"a swarm of agents will open the pull request and try and break it"*(03:36~03:42), 무작위 클릭이나 Playwright(*"play route"*)로 *"like a user would"*(03:46~03:48) |
| 5 | ⭐ *"if the fuzz is clean, it will just ping her on Slack, and then it goes and auto merges after an hour unless she asks for changes."*(03:52~04:00) |

- 발표자는 *"five steps"* 라 하고 1 · 4 · 5만 번호를 붙인다. 2 · 3의 칸 나눔은 이 페이지의 읽기다.
- fix and fuzz는 *"relates back to some of her skills we covered on Pystack[=Pstack] in another video"*(03:28~03:34) → [[pstack]]. 위키에 기록된 Pstack *full autopilot*(검증 에이전트 여럿이 PR마다 fuzz, 10-09 [[tech-bridge-lauren-tan-pocock-podcast-full]])과 같은 계열로 보인다(추정 — 이 영상은 둘을 같은 것이라 말하지 않는다).
- ⚠️ **"1시간 뒤 자동 머지"는 이 위키에 처음 기록되는 조건이다.** Lauren 본인 소스들은 *"my agents are merging their own pull requests"*(10-09 풀버전)와 아침 커밋 이력 사후 리뷰까지만 말했다. 대기 시간 1시간은 발표자 요약이고 원 글과 대조하지 않았다.
- ⭐ **[회사 · Anthropic] 위험 등급 단서** — *"if you look at how Anthropic approach this, you wouldn't apply this to every single type of bug or issue. You'd have green, yellow, and red in terms of blast radius. If something is highly critical, if it deals with payments, you're not going to have it auto merge in the step."*(04:02~04:16) 나머지 *"a lot of small fixes, a lot of non-critical tasks can work in this kind of a workflow."*(04:18~04:22) ⚠️ Anthropic 출처 미발화.
- **[Lauren] 미슐랭 주방** — *"she's not really a fan of the term software factory. She uses the analogy of a Michelin kitchen."*(04:24~04:31) *"as developers, we're still responsible for the final outcome. And that's a concept that Adi Esmany[=Addy Osmani] from Anthropic also doubles down on."*(04:31~04:38) 발표자의 정리: *"it's still your name on every single plate that goes out"*(04:43~04:46). 기존 기록과 같다 → [[agent-manager-analogy]] · [[named-human-accountability]].

→ [[lauren-tan]] · [[grokbot]] · [[risk-proportional-human-review]]

## 4. 신뢰를 쌓는 역피라미드 (04:48~06:09) — [Lauren] 발표자 전달

- 출발점: *"the few companies that are working in a pure software factory methodology are not doing it by adding more and more agents. What they're doing is starting with the raw infrastructure and trust."*(04:58~05:09)
- ⭐ *"Lauren's answer to this is what she calls the inverse pyramid. There are four levels, and you want to put most of your effort at the top."*(05:11~05:18)

| 층 | 발표자 요약 (en-orig) |
|---|---|
| 1. **코드베이스** | *"better architecture, stronger typing, clear boundaries"*(05:22~05:24) · *"agents love to copy what exists and take the shortest path. So, make the easy thing the right thing."*(05:27~05:34) |
| 2. **정적 분석** | *"lint rules, tests, continuous integration CI"*(05:41~05:44) · *"If you're finding that your agent keeps making the same mistakes over and over, you turn this into a deterministic lint rule."*(05:44~05:50) |
| 3. **prose(규칙 파일)** | *"your agents.md, your Claude.md, your skills, your bug bot, your security bot"*(06:04~06:08) |
| 4. **사람 리뷰** | *"It's the one most of us lean on the hardest. And again, it's the one that doesn't scale."*(06:12~06:15) |

> ⚠️ **Contradiction(약): 층의 수와 최하층.** 09-25 [[tech-bridge-lauren-tan-2000-prs]]에서 Lauren 본인은 *"다섯"* 층이라 했고(발화로 이름이 붙는 묶음은 넷), 최하층은 **"사람만 강제할 수 있는" 스타일 가이드**였다. 이 영상은 **넷**으로 세고 최하층을 **사람 리뷰**로 부른다. 층의 순서와 *"교정할 때마다 위로 올린다"* 는 운용은 같다. "inverse pyramid"라는 이름은 이 위키에 처음 나오며, Lauren 본인 발화로는 아직 확인되지 않았다.
>
> ⚠️ *"Her exact line on this"*(05:24~05:27)라 하지만 이어지는 문장은 **Lauren 본인 발화 두 개를 합친 모양**이다 — 09-12 *"기존 패턴을 그대로 베끼는 걸 정말 좋아한다"* 와 10-09 *"how do I make the easy thing the right thing?"*. *"take the shortest path"* 는 위키의 [[shortest-path-architecture]]와 같은 말이다. 축자 인용으로 쓰지 않는다.

→ [[hard-vs-soft-enforcement]] · [[agent-trust-curve]] · [[codebase-gardening]]

## 5. 사람의 리뷰와 검증 투자 (06:09~07:00) — [회사] 발표자 전달

- ⭐ **[Anthropic]** *"From June to September, their merged pull requests to Claude code more than doubled. And the share that they had to revert fell by more than 40%."*(06:18~06:26) 발표자 해석: *"they were doing double the amount of pull requests, but these pull requests were actually working."*(06:27~06:30) 인용: *"We didn't remove review, but we did move most of the review reading to machines."*(06:33~06:38)
- **[Alan Wells]** *"Alan Wells runs a team of three to get his factory shipping pull requests without human code review. They stopped all new product work for about 6 weeks just to build all the validation in."*(06:46~06:56) — *"very painful in the moment, but totally worth it"*(06:57~06:58).
- 발표자 정리: *"all of the companies that I have covered admit that getting to this point of trust takes real work up front."*(06:39~06:45)

> ⚠️ **Anthropic 수치의 네 번째 전달 — 단위 · 범위가 또 다르다.** 10-30 [[tech-bridge-anthropic-30k-merges-verification]]은 *"30,000 code changes every single day"*(merging), 11-01 [[tech-bridge-ai-labs-claude-code-verification-review-loop]]은 *"Across Anthropic, the number of changes to review every day went from about 2,500 to over 30,000 in just 4 months"*, 여기는 **Claude Code에 머지된 PR이 6~9월 2배 이상** + **revert 비율 40% 넘게 감소**다. 6~9월은 "4개월"과 길이가 비슷하지만 **배율(2배 vs 12배)과 범위(Claude Code vs Anthropic 전체)가 달라** 같은 숫자로 읽을 수 없다. 설명란 링크(Anthropic 코드 리뷰 글)는 열어 보지 않았다. revert 비율은 **이 위키에 처음 나오는 품질 쪽 수치**지만 분모 · 기준이 발화되지 않는다.
>
> ⚠️ Alan Wells는 소속 · 출처 미발화, 이 위키에 다른 기록이 없다.

→ [[automated-code-review]] · [[verification-bottleneck]] · [[trusted-throughput]]

## 6. 한 대화창에서 여러 봇 관리 (07:00~09:27) — [Rob]

- **메인 에이전트 하나** — *"I've tried my very best not to create 50 different bots here because the overhead of managing them becomes too much. In an ideal world, I'd have one agent to chat with. And that's what my main agent Chief is for."*(07:03~07:17) 봇끼리 그룹 채팅(07:17~07:20). *"Each one of my bots then has narrow permissions about what it connects to so that I can share those with other people if I need to."*(07:20~07:25)
- ⚠️ **불편 — 보이지 않는 상태** — *"Rockbot[=GrokBot] has evolved to store all your credentials. I don't know how comfortable I feel about this."*(07:26~07:29) *"I kind of miss being able to see what memories are being stored, what skills, um how my vault is being managed."*(07:35~07:41) 설정도 프롬프트로 하고 *"Rockbot just basically saves this to a skill somewhere. Again, I can't see where that skill is"*(08:17~08:20). 그래도 *"I'm happy to take the risk with Rockbot and experiment on the edge of what's possible just so I can share it with you guys."*(07:47~07:50)
- **위임 경로** — 마케팅 사이트 예: Chief가 *"spins up either a cursor cloud agent or a Claude code instance on my Mac"*(07:55~07:58), VPS에도 연결. Claude Code는 기본 모델을 지정해 *"Rockbot will kick off Cloud Code[=Claude Code] headless with the model that I picked."*(08:46~08:48) 폴더 · 환경마다 *"my own set of permissions and rules for security"*(08:42~08:46). 폰 · Mac 데스크톱 · 별도 PC가 *"all able to coordinate together. You could do the same with something like Tailscale."*(08:34~08:39) → [[tailscale]]
- **채널 제작에도** — *"I use very same setup for this channel when I'm having Opus 5.5 helping with visuals. It spins up multiple different agents and records different terminal clips."*(08:48~08:57) → [[claude-opus-5-5]](시점 단서)
- **매니저가 막힘을 푼다** — GrokBot이 Slack · 문서 소스에 연결돼 있어 *"it can unblock these sub-agents in any questions that we they have."*(09:09~09:13)
- **[Theo]** *"Theo is trying out a similar workflow with T3 Code. He documented some of it in a tweet. He's saying he can now drive his whole fleet of machines from Rockbot."*(09:13~09:20) — *"it's on the nightly build and it's very early"*(09:22~09:24). ⚠️ 무엇이 nightly build인지(T3 Code · GrokBot 연동) 불분명, 트윗 미확인.

→ [[manager-bot-coding-agent-split]] · [[persistent-agent-teams]] · [[grokbot]]

## 7. 백로그와 변경 영향 범위 (09:27~10:53) — [Rob] + [Lauren]

- **[Rob] 백로그** — Chief가 Slack · 대화에서 주운 것은 백로그로, Notion에 저장(09:27~09:35). *"I've set up a another routine with Rockbot to triage the backlog with Rice[=RICE] scoring. So, that's the reach, impact, confidence, and effort"*(09:38~09:45) *"And I also have a blast radius score as well."*(09:48~09:50) 결과: *"a small job that helps a lot of people rises to the top"*(09:52~09:54). 선제 제안도 받되 *"it'll quickly fill up your backlog with tasks just for the sake of it."*(10:05~10:08)
- **[Lauren]** *"She uses Grokbot routines to farm context from bug reports on Slack and then complains to command on X, and then she feeds that into what she calls her outer loop."*(10:12~10:20) — ⚠️ *"complains to command on X"* 판독 불가. 바깥 루프는 Lauren 본인 소스와 같은 말이다 → [[grokbot]].
- ⚠️ **토큰 경고** — *"that's something fine for someone like Lauren who has a ton of inference and credits to throw at these kind of things. If you're doing something similar like this yourself on an hourly schedule, you're going to burn a ton of tokens."*(10:22~10:32) Lauren 본인의 *"quite token intensive"*(10-09 풀버전)와 같은 방향.
- ⭐ **[Rob] 변경마다 blast radius** — *"I mark every change by blast radius or at least I don't, I get the agent to do that, which is how much could break if this goes wrong."*(10:34~10:40) *"You can get the agent to define the level of criticality, so the review level, whether that's human, AI level 1, 2, or 3, and this involves various different levels of playwright testing and security testing."*(10:40~10:52)

→ [[risk-proportional-human-review]] · [[scheduled-agent-automations]]

## 8. 보안과 첫 번째 운영 규칙 (10:53~12:33)

- ⭐ **[Rob] 공유 컴퓨터** — *"The last thing you need to do in terms of trust is lock the doors. All of your Grokbots share one cloud computer, that's including files, browser sessions, command line credentials."*(10:52~11:02) *"If you log a coding CLI in with an API key on one of Grokbot's computers, every bot you have can use that key."*(11:04~11:10)
  - > ⚠️ **Contradiction: 봇마다 컴퓨터인가, 하나를 공유하나.** 10-30 [[tech-bridge-dan-martell-grokbot-daily-automation]]: *"Every Grok Bot comes with its own virtual computer and login that's on 24/7"*. 10-18 [[tech-bridge-lee-robinson-always-on-agents]]은 봇마다 virtual desktop · 브라우저를 둔다고 했다. 이 영상은 **모든 GrokBot이 컴퓨터 하나와 자격 증명을 공유**한다고 한다 — 같은 문단 안에서도 *"one of Grokbot's computers"* 라 해 복수형이 섞인다. 제품 설정 · 시점에 따라 다를 수 있고 위키는 확인하지 않았다. 10-17 [[tech-bridge-openhands-sandboxing-coding-agents]]의 *한 기계에 모인 봇들* 비판과 같은 지점을 가리킨다.
- **[Rob] 빠름의 대가** — *"There's a beautiful speed in moving fast and breaking things, but inevitably that will come back and bite you in the butt."*(11:20~11:26)
- ⭐ **[Docker 등]** *"Docker and a group of security companies just published a secure software factory reference architecture, and the central idea is this: the more autonomy you give the agent, the less you can rely on it to police itself. The controls have to live in the environment."*(11:27~11:41) 발표자: *"I 100% agree with this."* 실천: *"running your agents in a sandbox, giving them scoped credentials, read only where you can, and letting them open pull requests but not merge them, at least until you trust the stack that's in place."*(11:43~11:55) ⚠️ 문서 이름 · 참여사 미확인.
- *"Grokbot as an orchestrator isn't going to solve all those problems. These are decisions you need to make in each of the codebases that you have set up based on their criticality."*(11:55~12:02)
- ⭐ **[Rob] 시작 규칙** — *"don't go building 50 agents. Start with one loop and paste this rule into your bot."*(12:07~12:12) 규칙: *"For anything more than a short question, don't write the code yourself. Hand it to a coding agent with an acceptance test, check the proof, open a pull request, and report back."*(12:14~12:24) 그리고 *"every time you have to correct an agent, move that fix up the stack, code first, then a lint rule, then a rules file, and review comes"*(12:24~12:30) — **영상이 여기서 끊긴다.**
  - ⚠️ en은 *"and finally the review."* 로 문장을 마무리한다. en은 고쳐 쓴 판본이라 근거로 쓰지 않는다. 다만 문맥(역피라미드 4층의 마지막이 사람 리뷰)과는 맞는다.

→ [[agent-sandboxing]] · [[least-privilege-connectors]] · [[action-reversibility]] · [[hard-vs-soft-enforcement]]

## 등장 개체

- 인물 · 제작자: [[rob-shocks]](신규, 설명란 근거) · [[lauren-tan]](2차 전달) · [[addy-osmani]](ASR *"Adi Esmany"*, 한 문장) · Alan Wells · Theo(페이지 없음) · [[tech-bridge]]
- 조직: [[anthropic]] · [[cursor]] · [[stripe]] · [[vercel]](Slack 관리, 한 문장) · Docker(페이지 없음)
- 제품: [[grokbot]] · [[claude-code]] · [[cursor-cloud]] · [[pstack]] · [[codex]] · [[tailscale]] · [[claude-opus-5-5]] · Linear · Notion · Jira · OpenCode · T3 Code(페이지 없음)
- 개념: [[manager-bot-coding-agent-split]](신규) · [[hard-vs-soft-enforcement]] · [[risk-proportional-human-review]] · [[agent-sandboxing]] · [[automated-code-review]] · [[agent-manager-analogy]] · [[inner-outer-meta-loops]] · [[cloud-agent-delegation]] · [[persistent-agent-teams]] · [[agent-trust-curve]]

## 이 위키에서의 좌표

- **GrokBot 소스의 세 번째 시점.** 만드는 쪽(Lauren Tan · Lee Robinson · Jediah Katz) → 비엔지니어 사용자(10-30 Dan Martell 추정) → **엔지니어 사용자**(이 편). 사용자로서의 **불편**(자격 증명 저장, 메모리 · 스킬 · vault가 보이지 않음, 컴퓨터 공유)이 처음 나온다.
- **Lauren Tan 이야기의 2차 요약.** 본인 소스 다섯 편(09-12 · 09-25 · 10-03 · 10-09 · 08-31 인터뷰)을 다시 짚되 **새 세부 둘**(1시간 대기 자동 머지, "inverse pyramid"라는 이름)과 **어긋남 하나**(층 수 · 최하층 이름)가 생긴다.
- **Anthropic 리뷰 수치의 네 번째 전달**(09-03 팀 대담 · 10-30 Osmani · 11-01 AI Labs · 이 편). 발표자마다 단위가 달라 합치지 않는다.
- 위키의 [[hard-vs-soft-enforcement]] "교정할 때마다 층을 고른다"가 **봇에게 붙여 넣는 규칙 한 줄**로 내려온다.

## ⚠️ 유보

- 화자는 설명란 근거, 원본 링크 · 녹화일 없음. 00:00~00:21 무캡션, 마지막 문장이 잘린다.
- Lauren 쪽(1시간 자동 머지 · 4층 · *"exact line"*), Anthropic 쪽(녹색 · 노랑 · 빨강, 2배 · 40%, 인용문), Alan Wells(6주), Theo, Docker 참조 아키텍처는 모두 출처 미발화 2차 전달이다. 설명란 링크 셋(x.ai 가이드 · Pstack 저장소 · Anthropic 글)은 열어 보지 않았다.
- 제품 진술(주간 사용량 풀 공유 · 통합 요금제, 자격 증명 저장, 컴퓨터 공유)은 미확인이고 마지막은 이전 소스와 충돌한다.
- 발표자 구성은 서술이지 측정이 아니다. 비용 · 실패율 · 효과 수치 없음.
- ASR: *"Rockbot"* · *"Crusher"* · *"Entropic"* · *"Cloud Code"* · *"Pystack"* · *"play route"* · *"pros"* · *"Adi Esmany"*. ko는 Linear를 "선형", PR을 "추출 요청", *"Hand it to a coding agent"* 를 "일정 담당자에게 전달하세요"로 옮겨 인용하지 않았다. en은 *"on its own computer"* 를 "your own computer"로, *"merged pull requests"* 를 "pull requests"로 바꾸고 잘린 마지막 문장을 완성한다.

## References

- raw: `01.raw/articles/2026-11-02_Grok Bot은 매니저 Claude Code는 개발자 AI 에이전트를 함께 쓰는 법.md`
- https://www.youtube.com/watch?v=ra5WyQ-hKN4
- 설명란 관련 자료(⚠️ 열어 보지 않았다): https://x.ai/bot/guides/grok-bot-for-engineering · https://github.com/cursor/plugins/tree/main/pstack · https://claude.dev/blog/solving-code-review-at-anthropic/
