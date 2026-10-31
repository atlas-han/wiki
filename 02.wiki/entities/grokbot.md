---
title: GrokBot
type: entity
category: product
tags: [persistent-agents, messaging-ui, agent-teams, cursor]
sources: [tech-bridge-grokbot-agent-teams, tech-bridge-cursor-legacy-refactoring, tech-bridge-lauren-tan-trusting-agents, tech-bridge-lauren-tan-2000-prs, tech-bridge-lauren-tan-agent-dev-workflow, tech-bridge-lauren-tan-pocock-podcast-full, tech-bridge-lee-robinson-always-on-agents, tech-bridge-jediah-katz-harness-whats-left, tech-bridge-anthropic-fold-subagents-into-skills, tech-bridge-dan-martell-grokbot-daily-automation]
created: 2026-09-01
updated: 2026-10-31
---

# GrokBot

[[cursor|Cursor]]의 지속형(persistent) 개인 에이전트 제품. [[tech-bridge-grokbot-agent-teams]] 인터뷰 **전날 베타 출시**(즉 2026-08-30 전후).

## 구성 요소

| 요소 | 내용 |
|---|---|
| **정체성** | 이름·아바타·성격. [[lauren-tan]]의 봇은 전부 고양이, 원조는 강아지 Benny |
| **자체 컴퓨터** | 사용자가 자리에 없어도 실행. 사용자의 도구에 로그인 (예: LinkedIn) |
| **팀 구조** | 비서실장(chief of staff) 코디네이터가 다른 봇에게 임무 배분·진행 확인 |
| **메시징 UI** | 동료에게 문자하듯. "iMessage처럼 보인다"는 평 |
| **루틴·자동화** | 피드백이 들어오면 자동 실행 → 사람은 코드만 리뷰 |

## 위키에서 알려진 사실

- 데모에서 확인된 것: 마케팅 봇의 LinkedIn 실시간 게시, 비서실장이 사내 "GrokBot wins" 채널 피드백을 모아 **Figma 슬라이드**로 조립, 엔지니어링 봇 팀이 버그를 나눠 받아 **검토용 PR** 반환.
- 사내 채택이 엔지니어링을 넘어 시장 진출·운영·제품 팀까지 확산 — 강한 내부 PMF가 외부 출시 신호가 됐다.
- **GrokBot의 상당 부분이 GrokBot 자체로 만들어졌다.** 에이전트가 문제를 분류하고 코드를 써서 클라우드 에이전트에 연결하는 피드백 루프.
- 로드맵 언급: **iMessage 지원**(봇에게 문자 보내기)이 흔한 요청. 아직 확정 아님.
- 초기 실사용 사례로 Odyssey IMAX 70mm 티켓 예매, 식료품 구매.
- 남은 과제로 자잘한 버그가 인정됐다.

## 두 번째 언급 (2026-09-08 편)

[[tech-bridge-cursor-legacy-refactoring]]의 마지막 답변에서 GrokBot이 다시 나온다. 질문은 *"스케줄로 도는 cloud agent가 **로컬 머신의** 무언가에 접근해야 하면?"* 이었고, 답은 레포에 커밋된 것(스킬·계획·파일)은 되지만 머신에 있는 것은 프라이빗 커넥티비티가 필요하다는 것이었다. 그 다음에:

> **`GrokBot`이라는 정말 멋진 도구가 있습니다. 일반 지식 제품이지만 코딩에도 쓸 수 있습니다.** 그것이 **클라우드와 로컬을 함께 써서 당신 머신에서 여러 가지를 작업하는 정말 좋은 해법**을 갖고 있습니다. **다음 주 목요일에 그걸로 워크샵을 합니다.**

→ 이 위키가 [[tech-bridge-grokbot-agent-teams]]에서 *지속형 개인 에이전트* 로 기록한 GrokBot이, **로컬 머신 접근이라는 [[cursor-cloud|Cursor Cloud]]의 구조적 한계를 메우는 자리**에 놓인다. 두 제품 축이 연결되는 두 번째 지점이다.

> ⚠️ *"일반 지식 제품(general knowledge product)"* 이라는 표현은 이 소스가 처음 쓴다. GrokBot이 코딩 특화가 아니라는 [[cursor]] 페이지의 서술과 일치한다.
> **"다음 주 목요일"** 은 이 소스의 촬영 시점 추정(2026-09-01 무렵)과 맞물리는 단서이며 날짜를 확정하지 않는다.

## 두 번째 소스 — 만들어진 방식과 재작성 (2026-09-12 편)

[[tech-bridge-lauren-tan-trusting-agents]]가 GrokBot의 **코드베이스 쪽 이야기**를 준다.

- **바이브 코딩된 그린필드로 시작했다** — *"아주 빠르게 바이브 코딩됐습니다. **사람은 코드를 전혀 읽지 않았습니다.**"* → [[organic-architecture]]
- **전체를 다시 짰다** — **PR 600건 이상**을 들여 [[dune-architecture|Dune]] 아키텍처로 리팩터링(자기 보고).
- 프레임워크의 명사가 GrokBot의 개념이다 — `feature` · `entry point` · **`transcript card`**(채팅에 보이는 카드).
- **가상화(virtualization)** 가 *"누군가 만든 새 라이브러리"* 로 돌아간다 — **이름은 자막에서 확정 불가.**
- **[[grokbot|Benny]]의 동작이 구체화됐다** — 버그 리포트를 받아 **클라우드에서 자기 데스크톱을 열고 Cursor를 돌려** control 스킬로 재현한다. 소스의 예에서 Benny는 **버그를 재현했으나 이미 main에서 고쳐져 있음을 확인**해 주었다.
- **비엔지니어의 기여 경로** — PM·디자이너가 직접 기능을 내보내고 엔지니어는 리뷰만 한다. 화자는 이를 *"Dune 아키텍처가 버티고 있다는 증거"* 로 읽는다.
- **위치 규정** — Cursor의 기존 표면(agents window·CLI·IDE)은 **파워 유저 도구**였고 GrokBot은 *"기술 분야가 아닌 사람들에게 결정적 순간"*, *"iMessage처럼 보인다"*.

> ⚠️ **출시일 기록을 정정할 근거가 생겼다(확정은 하지 않는다).** 위 *"인터뷰 전날 베타 출시(즉 2026-08-30 전후)"* 는 **[[tech-bridge-grokbot-agent-teams]]의 Tech Bridge 업로드 날짜(08-31)에서 끌어온 추정**이다. 그런데 같은 날 열린 이 워크숍에서 화자는 **GrokBot이 "어제" 출시됐고 [[grok-4-6|Grok 4.6]]이 "오늘" 발표됐으며 "이번 달은 아직 12일밖에 안 됐다"** 고 말한다(양 트랙 일치). **08-30·08-31은 12일이 아니다.**
>
> 이 위키는 2026-09-03에 **"업로드 날짜 ≠ 촬영 날짜"** 를 원칙으로 세웠는데 이 페이지에는 적용되지 않았다. **달을 확정할 근거가 없으므로 어느 쪽도 채택하지 않고 반증 증거만 표시한다.** 자세한 것은 [[tech-bridge-lauren-tan-trusting-agents]]의 시점 절.

## References

- [[tech-bridge-grokbot-agent-teams]] · [[persistent-agent-teams]] · [[cursor]] · [[lauren-tan]] · [[roshan-sadanani]]

## 세 번째 본인 소스 — "바깥 루프" (2026-09-26 · [[tech-bridge-lauren-tan-2000-prs]])

[[lauren-tan]]의 녹화 발표가 GrokBot과 Cursor의 **역할 분담을 처음 말로 정리**한다:

> **GrokBot과 Cursor는 함께 흥미로운 역할**을 합니다. **GrokBot은 제가 바깥 루프(outer loop)라고 부르는 것을 제공하는 데 아주 뛰어나요.** **Slack, Datadog, Sentry, PlanetScale** 등 여러 커넥터에 연결해 정보를 모으고 스스로 좋은 결정을 내리게 할 수 있으니까요. (32:34~33:05)

> **GrokBot 루틴**은 **Slack 스레드나 Sentry 알림을 구독해서 자동으로 일을 시작**하게 해 줍니다. (…) GrokBot은 **바깥 루프에서 오는 이벤트에 자동으로 반응해서 cloud agent를 띄울** 수 있습니다. (33:50~34:20)

- **구도**: GrokBot = **바깥 루프**(외부 신호·이벤트) → Cursor **cloud agents** = 실행 → **코드베이스·규칙·스킬** = 공유 인프라. 여기에 **Cursor automations**와 **SDK**로 *"세팅한 에이전트 인프라를 재사용하는 추가 봇"*(34:23~34:39). 결과 사례(스크린샷): **버그 리포트 자동 재현, PR 자동 오픈**(34:48~35:04).
- 위 구성 요소 표의 **루틴·자동화** 행에 **구독 대상(Slack 스레드·Sentry 알림)** 과 **커넥터 목록**이 처음 채워졌다.
- *"어떤 사람들은 이걸 **회사 두뇌**라고 부르는데 저는 그렇게 정교한 게 필요하다고 생각하지 않는다"*(33:05~33:16) → [[company-brain]]
- **Dune의 host는 "GrokBot 가상 머신에서 돈다"**(27:31~27:36) — 위 *"자체 컴퓨터"* 행과 맞물린다. → [[dune-architecture]]
- 화자 소개가 *"**SpaceX AI에서** GrokBot을 만든다"*(00:03~00:07)로 바뀌었다. ⚠️ 이 페이지 첫 줄의 *"Cursor의 … 제품"* 은 고치지 않는다 — 화자는 *"Cursor가 SpaceX AI의 일부가 되었다"* 는 취지로만 말한다(→ [[cursor]]).

> ⚠️ **당사자의 제품 권유**이고 커넥터·루틴의 가용 범위, 비용, 실패 사례는 없다. ko·en-orig 모두 제품명을 여러 번 틀린다(en-orig *graphbot·Rockbot·Grockbots* / ko *"GraphBot"·"성장봇"*).

## 첫 버전은 god file 8개, 그리고 두 루프의 연결 (2026-10-09 · [[tech-bridge-lauren-tan-agent-dev-workflow]])

- **재작성 전 상태가 구체화됐다** — *"the very first versions of Grokbot were composed of like eight god files"*(05:47~05:53). 위 *"바이브 코딩된 그린필드 → PR 600건+ Dune 재작성"* 의 출발점이다. → [[dune-architecture]]
- **바깥 루프를 도구 중립으로** — *"maybe you have the Slack MCP, right? Or you have your own harness that you've built a Slack subscription into for a particular Slack channel"*(07:04~07:15) → 제보마다 검증 스킬로 재현하고 *"verify that it still exists on main, and confirm it wasn't something like the user's setup, their data, or maybe they didn't install a dependency"*(07:43~07:56). *"creating those two loops and connecting them is a really important part of the job these days"*(07:56~08:06).
- ⚠️ 바깥 루프를 자동화하는 도구를 꼽는 자리가 *"tools likeot"*(ko 트랙 영어 구간 06:42)로 **잘렸다.** 문맥상 GrokBot일 개연성이 높으나 판독하지 않는다.

## 풀버전 대담 — god file 10,000줄, 바깥 루프 ↔ Cursor projects (2026-10-10 · [[tech-bridge-lauren-tan-pocock-podcast-full]])

위 절의 해설 영상이 발췌한 대담의 1:04:03 판본. ⚠️ 당사자 진술, 독립 확인 없음.

- **잘렸던 이름이 확인된다** — *"tools like Grockbot are really good because they help you automate the outer loop as well"*(35:23~35:29). 위 ⚠️의 *"tools likeot"* 은 **GrokBot**이다.
- **god file의 크기** — *"the very first couple of versions of Grockbot were composed of like eight god files which were like at least 10,000 lines long if not longer"*(30:21~30:34). 해설 영상 en-orig의 *"100 lines"* 는 잘린 ASR이었다.
- ⭐ **역할 분담이 완성된다** — *"cursor projects are my inner loop and grabbot[=GrokBot] is my outer loop. Grabbot takes all the context, external context, gives it to the projects because it can actually just send messages to those projects"*(42:55~43:08). GrokBot류는 *"connectors (…) a lot of people call them personal agents"*(40:02~40:09) — 이메일·캘린더·Slack·Linear·X. 본인 사용: *"I have some Groth[=Grok] bots that look at my Slack channels, look at my X (…) they have routines that subscribe"*(41:09~41:21), 예: GrokBot 데스크톱 앱 버그를 찾으면 Cursor project로 보낸다(41:26~41:36). → [[cursor]] · [[persistent-agent-teams]]
- **GrokBot 데스크톱 앱**이 자동 머지 작업 대상으로 나온다 — chief of staff 하나는 그 성능을, 하나는 사용자 버그를, 하나는 *"rewriting it in a different language just for fun (…) a native app. It's just a toy"*(51:12~51:32)를 맡는다.
- ASR: en-orig가 이번엔 *"grockbot"·"graphbot"·"Grabbot"·"Groth bots"·"grapot"*, `en`·ko는 *"Rockbot"*(35:24)과 *"Graphbot"*(42:54)을 공유한다.

## 안쪽 설계 — 개발자의 강의 (2026-10-18 · [[tech-bridge-lee-robinson-always-on-agents]])

[[lee-robinson|Lee Robinson]]([[spacex|SpaceX]])이 스탠퍼드 강의에서 GrokBot 하네스를 1인칭으로 설명한다. 지금까지 이 페이지는 사용자 쪽(봇 팀·바깥 루프)만 기록했다. 이번에는 **안쪽**이다. ⚠️ 당사자 진술, 수치 없음. → [[always-on-agent-architecture]]

- **"자체 컴퓨터"의 정체**: *"this is running a firecracker virtual machine"*(12:24~12:27). snapshot으로 재우고 깨운다. live view로 사용자가 직접 조작할 수 있고, virtual desktop으로 봇마다 브라우저를 둔다(12:36~13:13). 위 구성 요소 표의 "자체 컴퓨터" 행, 그리고 Lauren Tan의 *"Dune의 host는 GrokBot 가상 머신에서 돈다"*와 맞물린다.
- **루프는 VM 밖 서버에**: *"if you put the agent loop on the virtual machine, then you can't shut down the virtual machine independently"*(14:53~15:06).
- ⭐ **클라이언트-서버 도구는 하나**: *"The biggest difference with the Grockbot[=GrokBot] harness (…) there's only one tool that communicates between the client and the server and it's just send user."*(18:21~18:39) 클라이언트는 사인인 폼(1Password), 결제(Stripe Link·X Money), 되돌릴 수 없는 메시지의 초안 승인, 이모지 반응으로 그린다(19:24~19:58). "iMessage처럼 보인다"는 기존 평과 같은 방향이다(*"we all know how to text"* 05:52~05:54).
- **플러그인·루틴**: *"in Grockbot[=GrokBot] there is a whole system of plugins. So basically any tool that you want to use there's a plugin you can install which uses skills or servers and then also routines which if you're familiar with cron jobs"*(09:45~09:56). 위 "루틴·자동화" 행에 **플러그인 = 스킬 또는 서버**가 더해진다.
- **durable workflow**: 실패에 Temporal을 쓴다(17:08~17:11). helper 서브에이전트마다 durable workflow다(24:37~24:52).
- **오픈 판본**: *"I'm pretty sure there's like open grobbot[=GrokBot] on GitHub somewhere where somebody's like, you know, slotforked[=?] our code"*(44:11~44:15). ⚠️ 이 위키는 확인하지 않았다.
- ASR: en-orig *"Grockbot"*·*"open grobbot"*. 이번에는 ko·`en`이 *"Grokbot"*·*"Grok Bot"*으로 바르다.

> ⚠️ 이 페이지 첫 줄의 *"[[cursor|Cursor]]의 … 제품"*은 고치지 않는다. 화자는 *"We're working on at SpaceX"*(00:17~00:19)라고 한다. 조직 관계는 [[spacex]]의 원칙대로 추정하지 않는다.

## 다시 넣은 프롬프트와 가드레일 (2026-10-24 · [[tech-bridge-jediah-katz-harness-whats-left]])

[[jediah-katz|Jediah Katz]]: Cursor에서는 모델이 좋아지며 prompting·guard rails를 지웠는데 *"curiously in Grockbot[GrokBot] we've actually found ourselves putting back a lot of these things, adding new prompting, adding new guard rails. And that's because there's a lot of new tasks in this new way of working."*(03:50~04:09) → [[harness-pruning]]. ASR은 이번에도 *"Grockbot"*.
- [[tech-bridge-claude-duet-proactive-assistant]] 발췌의 *"Grockbot dots all"*(02:33)은 GrokBot · [[openai-dots|Dots]] 비교로 읽힐 수 있으나 판독 불가 — 해석하지 않는다.

## 하네스가 늘 줄지는 않는 사례로 재인용 (2026-10-29 · [[tech-bridge-anthropic-fold-subagents-into-skills]])

영어 해설자가 *"Grockbot"* 의 코디네이터 봇 + 워커 함대를 반례로 든다. 코딩 밖의 영역이라 *"adding certain guard rails back"* 한다는 것이다(05:46~06:08). 10-24 [[tech-bridge-jediah-katz-harness-whats-left|Katz 편]]과 같은 사실의 재인용이고 새 정보는 없다 → [[subagent-folding]].

## 사용자 쪽 첫 소스 — 역할별 봇을 말로 만든다 (2026-10-31 · [[tech-bridge-dan-martell-grokbot-daily-automation]])

지금까지 이 페이지의 소스는 전부 **만드는 쪽**이었다. [[dan-martell|Dan Martell]](⚠️ 설명란 · 태그 근거 추정)의 튜토리얼 발췌가 처음으로 **비엔지니어 사용자**의 쓰임을 준다. 코딩 · Cursor 연결은 한 번도 나오지 않는다.

- **구성 요소 표의 재확인**: *"Every Grok Bot comes with its own virtual computer and login that's on 24/7"*(00:18~00:22), 봇끼리 *"group chat with each other"*(00:47~00:49), 예약 · Slack 감시 트리거(00:29~00:35).
- **chief of staff가 봇을 만든다** — 사용자는 *"build me an inbox manager, name it something fun"*(01:49~01:54)처럼 말로 지시하고, 반복 일정도 설정 없이 말로 건다(01:31~01:40). 예시 봇: inbox manager · travel · people · family · constraint · finance · leadership · team bot.
- **사용자가 프롬프트로 거는 게이트** — *"ask for my okay before you pay"*(03:02~03:04), *"get me the okay before you submit anything"*(03:56~03:58), finance bot은 *"read-only access"*(04:39) + *"never move money or pay anything"*(04:51~04:53). → [[action-reversibility]] · [[least-privilege-connectors]]
- **team bot** — 플러스 아이콘 맨 아래 *"team bot"*(05:56~05:58), Slack 공유 채널에 두고 모두가 고친다(05:24~05:38). → [[multiplayer-agent-context]]
- **웹보다 API**(06:03~06:11), *"skill then routine"*(06:11), **computer use로 작업을 녹화하면 스킬이 된다**(06:16~06:24) — 위 Lee Robinson 절의 *"plugins (…) skills or servers (…) routines"* 에 **녹화 → 스킬** 경로가 사용자 발화로 붙는다.

> ⚠️ 제작사 미발화, 시연 결과 · 수치 없음, 녹화 → 스킬 기능은 미확인. 이번 en-orig는 *"Grok Bot"* 표기가 대체로 바르다(*"Grok bot"* 06:03~06:05).
