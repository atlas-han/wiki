---
title: "Tech Bridge — 벤더 락인 없는 AI의 미래 (Remy Guercio · Tailscale): 토큰맥싱 다음은 ROI 맥싱 — 네 층(LLM·데이터·인터페이스·샌드박스) 어디서나 고를 수 있게, 신원 기반 AI gateway로"
type: source
tags: [ai-gateway, vendor-lock-in, roi-maxing, token-maxing, value-maxing, ai-spend, budgets, identity-based-auth, mesh-network, mcp-gateway, auth-injection, model-switching, interface-decoupling, sandboxes, observability, agent-self-diagnosis, context-hygiene, tailscale, aperture, vendor-pitch, video]
source-url: https://www.youtube.com/watch?v=l3HyFh6Dg4w
source-type: video
author: Tech Bridge (한영자막 재배포) · 발표 Remy Guercio([[tailscale|Tailscale]] strategic projects team, AI gateway Aperture 담당 — **이름 "Remy"는 자막에서 자기소개, 성 "Guercio"는 설명란에만**) · **행사명 발화 — AI Engineer World's Fair**("the last talk on this stage", 그날 마지막 발표) · 연도·날짜·도시 미발화
date-published: 2026-10-15
ingested: 2026-10-16
created: 2026-10-16
updated: 2026-10-16
---

# Tech Bridge — 벤더 락인 없는 AI의 미래 (Remy Guercio · Tailscale)

[[tech-bridge|Tech Bridge]]가 재배포한 **19:09 단독 발표, Q&A 없음, 공식 챕터 6개.** 화자 [[remy-guercio|Remy Guercio]]는 자막에서 *"My name's Remy. I am on the strategic projects team at Tailscale and more specifically I actually work on our AI Gateway aperture"*(00:12~00:24)라고 자기소개한다(성은 설명란에만). 행사는 화자가 직접 말한다 — *"the last talk on this stage of the AI engineer world's fair this year"*(00:03~00:12). 측정·고객 수치는 없고, **진단(토큰맥싱의 비용·낭비·수직 통합) + 프레임(ROI 맥싱 = 네 층에서의 선택권) + 자사 제품 Aperture 소개(약 8분)** 다. 테제:

> **지난 12개월은 토큰맥싱이었고, 그건 비싸고 기본적으로 낭비를 부추기며 수직 통합 툴체인에 묶이게 했다. 청구서에 놀라 벤더 하나로 통합하는 건 답이 아니다. 다음 12개월은 ROI 맥싱 — 비용 절감만이 아니라 가치 증명 — 이고, 그 조건은 내부 AI 배포의 네 층(LLM · 데이터 커넥터 · 인터페이스 · 샌드박스) 어디서든 필요할 때 다른 것을 고를 수 있는 상태다. 그 선택권을 한곳에 모으는 자리가 AI gateway다.**

> *"We're not going to be token maxing. We're going to be ROI maxing."* (05:05~05:08) · *"it's really important to be able to make a choice at any given layer that you need at any given time."* (07:09~07:13) · *"ROI maxing really is all about maximizing choice to prevent lock-in"* (17:40~17:48) · *"it's not just lock-in, right? It's actually just experimentation and understanding"* (18:40~18:46)

이 위키에 시스템 페이지 하나가 생긴다 → [[ai-gateway]](신규 제안 — 에이전트·인터페이스와 LLM·MCP·API 엔드포인트 사이의 단일 통제·관측 지점, 신원 기반 인증·신원별 모델 예산·로그). 나머지는 기존 페이지의 **새 증언**이다 — [[value-maxing]](*"ROI maxing"* — 같은 전환을 **선택권**으로 정의), [[overspending-underusing-loop]](청구서 공황 → 벤더 통합이라는 긴축 반응), [[automatic-model-routing]](자동 라우팅이 아니라 **정책** — 싼 모델 무제한·프런티어 좁은 예산), [[agent-identity-separation]](네트워크 층 신원: 사용자 vs 태그된 기기·노드), [[credential-injection-outside-sandbox]](게이트웨이의 auth 주입), [[least-privilege-connectors]](팀별 GitHub 쓰기/읽기), [[model-context-protocol]](*"everybody follows a different version of that standard"*), [[context-rot]](아무도 컨텍스트를 비우지 않는 수천 메시지 세션), [[openclaw]](Tailscale 위에서 백그라운드로 돌리는 개인 사용자).

ASR·ko 보정: ko는 **핵심 문장 셋을 뒤집는다** — *"doesn't matter if you're trying to switch models or providers, you can do that"* → **"모델을 변경하려고 하면 문제가 생깁니다"**(12:14~12:18), *"it's not just lock-in"* → **"봉쇄 문제일 뿐이죠"**(18:38~18:40), 벤더 통합이 *"not a great idea"* → **"큰 문제가 아닐 수도 … 아이디어는 좋지만"**(04:27~04:29). ROI 맥싱의 정의 *"I don't just mean cutting costs"* 는 **"비용 절감을 말씀하시는 거죠?"**(05:17)라는 되물음이 된다. 제목어 **lock-in은 끝까지 "봉쇄"·"차단"**(`en`도 *"blockage"*/*"blocking"* — 17:44만 *"lock-in"*), gateway는 "관문"·"출입구"·"문"·"AI 링크", **Aperture는 "구멍"·"조리개"**, **Tailscale은 "꼬리비늘"**, OpenClaw on Tailscale은 **"꼬리비늘에 발톱이 열려 있고"**(18:21), LLM은 **"LLM 학위"**, PR review bot은 **"홍보팀에서 온 리뷰 봇"**(10:08~10:09), 행사명 *World's Fair* 는 "세계 박람회 … 시나리오"(00:06)와 "공정하네요"(19:03). 전체 목록은 raw.

> ⚠️ **벤더 발표 — 화자가 밝힌다.** *"maybe no surprise that I'm here to talk a little bit about why an AI gateway uh will help you do that (…) And I don't just mean necessarily using our AI gateway. I think it's nice, but you know, just any AI gateway"*(07:44~07:56). 진단·프레임(00:00~07:40)이 자사 제품 카테고리(AI gateway)로 귀결되는 구조다. 07:57~17:35는 Aperture 기능 소개이고 화면 데모를 전제한다(*"as you can see here"* 12:48~12:50 — 화면은 확인하지 않았다).
>
> ⚠️ **수치가 없다.** *"hundreds or thousands of messages"* 세션(02:19~02:21), *"tens of millions of tokens of a session"*(02:32~02:34), *"hundreds and hundreds of folks"*(03:38~03:40)는 모두 화자가 자사 게이트웨이·고객 대화에서 본 **일화**다. 분모·비율·비용·절감액 없음. 청중 거수 결과도 발화되지 않는다(09:12~09:17).
>
> ⚠️ **설명란과 발화가 다른 자리.** ① *"오픈소스 AI 게이트웨이 Aperture"* — 발화에서 open-source라 불리는 것은 라이브러리 **TSNet**(*"It's called TSNet. It's an open-source library. (…) That is what we use to build Aperture."* 10:34~10:41)이다. Aperture의 라이선스는 발화되지 않는다. ② *"개발을 이끄는"* — 발화는 *strategic projects team* 소속, *"I actually work on"*. ③ *"무제한 AI 예산의 시대는 끝났습니다"* — 발화는 *"have maybe been marked by (…) unlimited AI budget Uh, and that's changed here in the last few months"*(01:52~01:58). ④ *"Claude Code, Cursor, Codex 등 (…) 통합 로깅과 추적성"* — 세 도구는 **인증·전환 비용** 맥락(13:56~14:17)에서 나온다. ⑤ *"ROI 극대화(Profit Maximization)"* — *profit maximization* 은 발화되지 않는다.
>
> ⚠️ **예정 기능.** pass-through auth(*"we're actually going to be adding"* 16:08~16:12)와 샌드박스 orchestration layer(17:05~17:11)는 **아직 없는 기능**이다.
>
> ⚠️ **행사·시점.** 행사명은 발화로 확정된다(*AI Engineer World's Fair*, 00:09·19:02). 같은 무대의 그날 마지막 발표(*"the last talk in here of the day"* 18:55~18:58). 연도는 *"this year"* 뿐이고 월·일·도시는 발화되지 않는다 → [[ai-engineer]]. 시간 단서는 *"the last 12 months"*·*"over the last 6 months"*·*"in the last few months"* 등 상대 표현뿐이다.

## 1. 토큰맥싱의 1년 (00:32~01:35)

- *"the last 12 months, (…) I think it can really be you know described quite a bit by the phrase token maxing"*(00:34~00:42). 부정적 의미가 아니다: *"it's been a year of trying to figure out you know what we can do with million token context windows. With the ability to get context from anywhere"*(00:52~01:02) — MCP와 *"coding tools (…) that are great at finding context, using the CLI"*(01:07~01:10).
- *"it's really made truly agentic coding possible having all of this"*(01:21~01:23). 코딩 밖의 agentic use case도 *"continue to take off"*(01:31~01:33).

→ [[value-maxing]](토큰맥싱이라는 명명 — 이 화자는 긍정적 맥락에서 시작한다) · [[context-engineering]]

## 2. 문제 — 비싸고, 낭비가 기본값이고, 수직 통합에 묶인다 (01:38~03:25)

- *"It's very expensive, right? It's it's it's an extremely expensive endeavor."*(01:44~01:47) *"the last 12 months are you know, have maybe been marked by hey, we have you know unlimited AI budget Uh, and that's changed here in the last few months"*(01:49~01:58)
- ⭐ 낭비가 기본값: *"it does incentivize what I would call like wasted tokens by default. I mean, I I work on an AI gateway. Uh, we use our AI gateway. I get to see all of the usage from the AI gateway. You would not believe the number of sessions that are hundreds or thousands of messages long where nobody clears the context. They just kind of keep going."*(02:07~02:26) *"tens of millions of tokens of a session uh where it's the cache is basically maxed out maxed out the entire time."*(02:32~02:39)
- 수직 통합: *"this has led to you know, in many cases very vertically integrated tool chains. Uh, Cloud Code[=Claude Code] is obviously, you know, a big one. Code X[=Codex] right? Everybody's kind of building up there, you know, from all the way from the model (…) all the way up at the top"*(02:46~03:00)
- 질문: *"how do we address the lock-in and (…) how do we actually improve uh how we use AI such that (…) we can use it for things that aren't just (…) essentially frontier task or where we're just kind of wasting wasting money, wasting tokens"*(03:12~03:23)

→ [[context-rot]](아무도 컨텍스트를 비우지 않는다 — 비용 쪽 증언) · [[overspending-underusing-loop]] · [[claude-code]] · [[codex]]

## 3. 오답 — 벤더 하나로 통합 (03:27~04:54)

- *"over the last 6 months, (…) I've literally been talking to hundreds and hundreds of folks about their AI spin[=spend], their AI usage"*(03:35~03:43). 그들의 말: *"I don't know what's going on. I know we're using a lot of AI. I get, you know, uh I get an Anthropic bill every day. Uh, I get a Codex bill every day."*(03:47~03:56)
- 흔한 해법: *"everybody seems to be using Claude code right now. So, we're just going to like consolidate on a single vendor. Maybe two vendors, right?"*(04:06~04:12) → *"that is not not a great idea."*(04:21~04:23)
- 왜 그렇게 되는가: *"when you're in that panic zone of we've spent a lot of money and we don't know how exactly, and we you know, finance is talking to you, IT is being like, 'What are you doing?' You know, like we said to you know, use AI, but maybe not use that much AI."*(04:28~04:44) *"it's a pretty natural response to be like, 'Okay, I'm going to consolidate everything down.'"*(04:45~04:50)

→ [[overspending-underusing-loop]](청구서 공황 → **통합이라는 형태의 긴축**) · [[reserve-then-settle]](검사가 청구서 뒤에 온다 — 같은 공황을 파는 쪽에서) · [[bring-your-own-subscription]]

## 4. ROI 맥싱 — 비용 절감이 아니라 가치, 그리고 열기 (04:55~05:42)

- ⭐ *"I think this is kind of peaking[=peeking] at what we're going to see the next 12 months (…) what I would like to call ROI maxing, right? We're not going to be token maxing. We're going to be ROI maxing."*(04:55~05:08) *"it's really just a necessity"*(05:12~05:14).
- ⭐ 정의: *"when I say ROI maxing, I don't just mean cutting costs, right? I mean actually proving some sort of value to the thing that you're doing."*(05:15~05:24)
- *"And not only that, but also kind of opening things up, right? So, if the only thing you have is like two frontier models and their entire stacked ecosystem, that's a certain cost level where (…) certain things untenable, right? You can't actually expand AI usage into the company if that's the only way you can use AI."*(05:24~05:42) — 비용 구조가 **사용 범위의 상한**을 정한다는 논증.

→ [[value-maxing]](같은 전환, 다른 이름 — IBM 편은 "결과", 이 화자는 "가치 증명 + 선택권") · [[agent-roi-measurement]](⚠️ 어떻게 증명하는지는 발화되지 않는다)

## 5. 내부 AI 배포의 네 층 — 각 층에서 고를 수 있어야 한다 (05:43~07:39)

- 범위: *"I'm not talking about like a hey, we've built this new AI feature in our app. I mean, you know, internal internal to your organization."*(05:48~05:55)
- ⭐ 네 층(05:57~06:46):
  1. **LLM** — *"There's the LLM or LLMs, right? There's that layer."*
  2. **데이터 커넥터** — *"this is MCP for a lot of people, but in reality it's, you know, CLI or APIs or really just any way that you get data uh could be reading a file, right? Into your (…) agentic system."*(06:03~06:13)
  3. **인터페이스** — *"I think people kind of forget about this sometimes"*(06:15~06:16). chat → TUI → IDE의 chat → 다시 휴대폰 → *"Claude tag"*(⚠️ 판독 보류) → Slack(06:16~06:38). *"it is a component that you can break out."*(06:40~06:42)
  4. **샌드박스** — *"sandboxes/just the environment in which the agent runs"*(06:43~06:46).
- ⭐ *"to be ROI maxing uh means to be maxing your, you know, every opportunity that you have uh for choice, to make a choice at one of those layers, right? You don't have to necessarily have (…) my bespoke special choice at every one of those layers, but it's really important to be able to make a choice at any given layer that you need at any given time."*(06:51~07:13)
- 팀마다 다르다: *"I don't totally imagine like an entire engineering team just coding via, you know, Slack thread. (…) but you know, the entire marketing team might be working entirely uh you know, in a Slack thread asking data questions"*(07:19~07:35)

→ [[ai-gateway]] (신규) · [[harness-as-platform]] · [[model-harness-knowledge-stack]] · [[agent-harness-design]]

## 6. AI gateway, 그리고 Aperture (07:40~09:29)

- 벤더 고지(위 ⚠️, 07:40~07:56). *"our AI AI gateway is uh called Aperture."*(07:56~07:58)
- ⭐ 자리: *"it sits in between your agents and that interface of that agent uh and you know, all of your endpoints uh as well both like LLM endpoints as and data, you know, kind of MCP endpoints, API endpoints (…) and sits in the middle and let you both control and monitor what's happening."*(08:05~08:21) 관점은 보안·비용·*"I want to learn about what somebody is doing or what an agent is doing"*(08:23~08:34).
- ⭐ 로그 = 에이전트의 사후 진단 재료: *"it ran out. (…) it didn't reach an answer. It just kind of spiraled out of control. (…) Happens with, you know, maybe cheaper models more often, too. Uh They're usually not great at stopping themselves, uh but they are great at analyzing where they went wrong after the fact. And so, when you have something like an AI gateway, it's really easy to point it back at what you were doing and say, what happened?"*(08:42~09:05)
- 기존 게이트웨이의 불만: *"I put all my keys on this gateway. Now I need to go create synthetic keys for everything that I have. (…) I've traded some keys for a bunch of other keys."*(09:19~09:28)

→ [[ai-gateway]] · [[trace-to-memory-loop]](트레이스를 에이전트에게 되먹이기) · [[production-trace-eval-flywheel]] · [[design-pattern-proxy]]

## 7. 신원이 연결에 붙는다 — Tailscale 위의 게이트웨이 (09:30~10:50)

- *"Aperture is built on Tailscale. (…) Tailscale is an identity-based mesh network. It's built on WireGuard."*(09:32~09:41) 클라이언트를 *"containers, laptops, GPU servers"*(09:53~09:55)에 깔면 *"every connection that's now made over that tailnet uh comes with the identity of the machine or the user on the other side."*(09:58~10:05)
- ⭐ 두 종류의 신원: 기기 태그 — *"Hey, this is a machine ID. This is a PR review bot. (…) a separate node ID underneath that says the instantiation of that PR review bot."*(10:07~10:15) — 와 사용자 — *"it's just me using Cloud Code[=Claude Code] on my laptop"*(10:17~10:20). Entra·Okta 그룹 동기화(10:22~10:28).
- *"We have this really cool library. It's called TSNet. It's an open-source library. You can use it to build these sorts of apps. That is what we use to build Aperture."*(10:33~10:41)

→ [[agent-identity-separation]](사용자·애플리케이션·에이전트 신원 — 이 소스는 **네트워크 연결 층**에서 붙인다, 에이전트 *인스턴스* 단위 node ID) · [[tailscale]] (신규)

## 8. 층별로 — LLM (11:07~12:19)

- 공급자: *"It's got Anthropic, OpenAI, Vercel, you know, it's got even Anthropic OAuth, uh you know, Bedrock, Codex"*(11:20~11:26). 키는 게이트웨이에 한 번.
- ⭐ *"Once I connect to the (…) gateway, it knows who I am. It knows what I am. And it's like, 'Oh, you have access to these models, this provider, right? You can use GLM 5.2. Uh you get this budget with GLM 5.2, right? You get unlimited budget with a cheap model, and you get an extremely narrow budget with a frontier model, right?'"*(11:43~12:01) *"there's no extra setting here. It's just add your add your API key and go."*(12:03~12:07)
- *"doesn't matter if you're trying to switch models or providers, you can do that."*(12:16~12:19) ⚠️ ko는 이 문장을 **"모델을 변경하려고 하면 문제가 생깁니다"** 로 뒤집는다.

→ [[automatic-model-routing]](라우터가 고르는 게 아니라 **관리자가 신원별 예산으로 정책화**) · [[glm-5]](⚠️ *"GLM 5.2"* 는 예시로만) · [[anthropic]] · [[openai]] · [[vercel]]

## 9. 층별로 — 데이터·MCP (12:19~14:43)

- *"we're both an LLM gateway and an MCP gateway, and we even do off[=auth] like injection for just standard APIs and re-expose those as MCPs, too."*(12:33~12:43) — 그래서 "LLM gateway"가 아니라 "AI gateway"라는 말을 골랐다(12:25~12:47).
- ⭐ MCP의 현실: *"there's a standard, but everybody follows a different version of that standard. Uh you know, you can tell exactly when an MCP server was built by exactly how they decided to do off[=auth]. (…) it's a great uh you know, kind of archaeology lesson"*(13:05~13:20)
- 신원으로 권한: *"the marketing team, you know, they get access to Google Calendar and Gmail, but the engineering team will also get access to GitHub. (…) this side of the engineering team gets access right[=write] access to GitHub. Or read-only access to GitHub."*(13:31~13:47)
- ⭐ 인증의 분리 = 전환 비용: *"all of the authentication happens here. So, if you have folks that want to use cursor or they want to use cloud code or they want to use code X or (…) some new hot thing (…) all they have to do is hit that endpoint. And if they're on the tailnet, everything's authenticated as them"*(13:51~14:15) *"We make the switching cost, right? Of like actually trying out tools (…) a lot a lot easier (…) It's all those little points of friction uh that lead to (…) people just don't try new use cases."*(14:23~14:38)

→ [[model-context-protocol]] · [[credential-injection-outside-sandbox]](자격증명이 에이전트·도구 밖, 게이트웨이에 있다) · [[least-privilege-connectors]] · [[cursor]]

## 10. 층별로 — 인터페이스 (14:44~16:27)

- *"with aperture, we actually have a built-in chat UI. Surprise. (…) however, it is built on top of APIs that you can also leverage yourself."*(14:47~15:00) Slack bot·chat UI·모바일·*"a voice-only interface"*(15:08~15:18). 커넥터는 chat UI가 아니라 게이트웨이에서 설정된다(15:26~15:34).
- 예정: OpenWebUI·*"Libre"*(⚠️ 판독 보류)류를 세우면 *"you always lose identity information and then suddenly all of the (…) everything's coming from the UI"*(16:01~16:06) → *"We're actually going to be adding a full like pass-through auth"*(16:08~16:12).

## 11. 층별로 — 샌드박스, 그리고 맺음 (16:27~19:06)

- 샌드박스는 이미 선택지가 많다: *"folks are doing pretty good. There's actually a lot of choice already."*(16:33~16:35) 정의가 사람마다 달라 *"we're kind of in that let a thousand flowers bloom phase"*(16:51~16:54).
- 예정: *"We're actually going to be adding kind of an orchestration layer as well for sandboxes to a gateway"*(17:05~17:11) — *"a place to sort of see them all and then a place that brings them all together (…) kind of a mostly universal translation layer in a way."*(17:26~17:35)
- ⭐ *"ROI maxing really is all about maximizing choice to prevent lock-in, right? So, you know, even if you don't use Aperture, I do highly recommend you start considering an AI gateway"*(17:40~17:53)
- 개인에게도: *"We have so many people who are just as an individual, they have their usage behind an an AI gateway just to have an idea as to what their agents are doing"*(18:08~18:17) — *"people are running something like Open Claw[=OpenClaw] with on Tailscale (…) running in the background and they're like, 'Oh my goodness, did it did something. I'm not sure what it did. It did something it was not supposed to do.'"*(18:22~18:32) → *"you can actually diagnose where it went wrong"*(18:36~18:40).
- *"it's not just lock-in, right? It's actually just experimentation and understanding"*(18:40~18:46). *"just short and sweet."*(18:52~18:53)

→ [[openclaw]] · [[agent-governance-layers]](§"보는 층") · [[credential-injection-outside-sandbox]]

## 이 위키와의 연결

### 이어지는 것

- **[[value-maxing]] — 같은 전환, 셋째 이름.** IBM 해설은 토큰맥싱 → *밸류맥싱*(결과를 물어라), Ironclad는 *"긴축이 아니라 ROI"*([[trusted-throughput]]), 이 화자는 **ROI 맥싱**이다. 새로 더하는 것은 정의의 둘째 절 — *가치 증명*에 더해 **선택권**(*"maximizing choice to prevent lock-in"*). 비용 구조가 사내 확산의 상한을 정한다는 논증(05:28~05:42)도 이 위키에서 처음이다.
- **[[overspending-underusing-loop]]** — 청구서 공황(*"finance is talking to you, IT is being like, 'What are you doing?'"* 04:36~04:40)의 반응이 **벤더 통합**이라는 형태로 나타난다. Piras의 "긴축"이 지출을 줄이는 것이라면, 여기서는 **선택지를 줄이는 것**이 긴축이다. 화자는 그것을 오답이라 한다.
- **[[automatic-model-routing]]** — Kimchi(결과로 고르는 라우터)·Not Diamond류와 달리, 이 소스의 모델 선택은 **신원별 접근·예산 정책**(싼 모델 무제한, 프런티어 좁은 예산, 11:56~12:01)이다. 라우팅의 결정 주체가 모델/라우터가 아니라 관리자다.
- **[[agent-identity-separation]] · [[credential-injection-outside-sandbox]]** — 신원과 자격증명을 에이전트 밖에 두는 처방이 **네트워크 층**에서 나왔다. 사용자 vs 태그된 기기, 기기 아래 **에이전트 인스턴스별 node ID**(10:07~10:15). API 키를 사람·에이전트에게 나눠 주지 않는다(*"there's no extra screen for create these API keys"* 11:38~11:41).
- **[[context-rot]]** — *"sessions that are hundreds or thousands of messages long where nobody clears the context"*(02:19~02:24): 품질이 아니라 **비용** 쪽에서 본 같은 현상(캐시가 꽉 찬 수천만 토큰 세션).
- **[[trace-to-memory-loop]] · [[production-trace-eval-flywheel]]** — 에이전트는 *"not great at stopping themselves (…) but they are great at analyzing where they went wrong after the fact"*(08:54~08:59) → 게이트웨이 로그를 에이전트에게 되돌려 묻는다. 트레이스를 사람이 아니라 **에이전트가 읽는** 사후 분석.
- **[[model-context-protocol]]** — *"everybody follows a different version of that standard"*(13:07~13:09), 서버의 auth 방식으로 제작 시기를 알 수 있다는 "고고학". MCP 게이트웨이는 [[tech-bridge-runlayer-self-improving-skills-mcp|Runlayer]]의 *"our MCB[=MCP] gateway"*, [[composio|Composio]] 설명란의 *"MCP 게이트웨이"*(발화 없음)에 이어 **세 번째** 벤더 언급이고, 기능(auth 주입·API → MCP 재노출·팀별 권한)이 발화된 것은 처음이다.
- **[[bring-your-own-subscription]]** — 설정에 *"Anthropic OAuth"*(11:24)가 공급자로 나온다. 구독 경로를 게이트웨이에 꽂는다는 뜻으로 읽히지만 **그 이상은 발화되지 않는다**.

### 갈리는 것

> ⚠️ **긴장: 수직 통합 vs 분리.** 이 위키의 여러 소스(예: [[harness-as-platform]], [[tech-bridge-codex-app-server|Codex App Server]])는 모델 회사가 하네스·인터페이스까지 수직으로 쌓는 흐름을 **기능의 원천**으로 다룬다. 이 화자는 같은 흐름(*"very vertically integrated tool chains"* 02:48~02:53)을 **락인의 원천**으로 보고 층을 떼어 내라고 한다. 다만 근거는 비용·선택권 주장뿐이고, 분리했을 때 잃는 것(통합 하네스의 품질)은 다루지 않는다. 그리고 처방은 자사 제품 카테고리다.

> ⚠️ **"비용"의 자리.** [[tech-bridge-kimchi-cost-per-task-harness|Kimchi 편]]은 *토큰을 무제한으로* 주고 작업당 비용을 보라 하고, [[token-minimization-trap]]은 자르면 재작업으로 옮겨 간다고 경고한다. 이 화자의 예시 정책(*싼 모델 무제한, 프런티어 좁은 예산*)은 **모델 단가 기준의 배급**이다 — 작업 결과 기준이 아니다. 어느 쪽이 나은지는 이 소스가 측정하지 않는다.

## 해소하지 않고 표시만 한 것

- Aperture의 라이선스(설명란 "오픈소스" vs 발화의 TSNet)·가격·배포 형태·고객 수.
- *"Claude tag"*(06:32~06:33)가 무엇인지, *"Libre"*(15:54)가 LibreChat인지.
- *"GLM 5.2"*(11:53) — 모델명 대조 안 함.
- 예정 기능 둘(pass-through auth, 샌드박스 orchestration)의 시기.
- ROI를 *어떻게* 증명하는지 — 게이트웨이 로그가 가치 측정으로 이어지는 경로는 발화되지 않는다.
- 행사 연도·날짜·도시, 같은 행사의 다른 소스와 같은 회차인지.

## 등장 개체

- 인물: [[remy-guercio|Remy Guercio]](신규 제안 — 이름은 자막 자기소개, 성은 설명란)
- 조직: [[tailscale|Tailscale]](신규 제안, Aperture·TSNet 섹션 포함) · [[anthropic|Anthropic]] · [[openai|OpenAI]] · [[vercel|Vercel]] · [[ai-engineer|AI Engineer]](행사명 발화) · Microsoft Entra·Okta·AWS Bedrock — 페이지 없음
- 제품·도구: Aperture(→ [[tailscale]]에 합침 제안) · TSNet · WireGuard · [[claude-code|Claude Code]](en-orig *"Cloud Code"*) · [[codex|Codex]](*"Code X"*) · [[cursor|Cursor]] · [[openclaw|OpenClaw]](*"Open Claw"*) · [[glm-5|GLM]](*"GLM 5.2"*, 예시) · Slack · Google Calendar·Gmail·GitHub · OpenWebUI · *"Libre"*(⚠️ 미확정) — 페이지 없는 것은 언급만
- 개념: [[ai-gateway]](신규 제안) · [[value-maxing]] · [[overspending-underusing-loop]] · [[automatic-model-routing]] · [[agent-identity-separation]] · [[credential-injection-outside-sandbox]] · [[least-privilege-connectors]] · [[model-context-protocol]] · [[context-rot]] · [[context-engineering]] · [[trace-to-memory-loop]] · [[production-trace-eval-flywheel]] · [[agent-governance-layers]] · [[agent-roi-measurement]] · [[token-minimization-trap]] · [[trusted-throughput]] · [[bring-your-own-subscription]] · [[harness-as-platform]] · [[model-harness-knowledge-stack]] · [[agent-harness-design]] · [[reserve-then-settle]] · [[design-pattern-proxy]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=l3HyFh6Dg4w> (19:09, `upload_date` 2026-10-15)
- raw: `01.raw/articles/2026-10-15_벤더 락인 없는 AI의 미래를 만드는 방법입니다.md`
- 설명란 링크: <https://tailscale.com/docs/aperture> · <https://aperture.tailscale.com> · <https://tailscale.com> · <https://twitter.com/remyguercio> · <https://github.com/remyguercio> · <https://ai.engineer> (⚠️ 열어 보지 않았다)
- 토큰맥싱 이후의 다른 이름: [[tech-bridge-tokenmaxxing-to-valuemaxxing]] · [[tech-bridge-kimchi-cost-per-task-harness]] · [[tech-bridge-mousepower-measuring-agents]]
- 사용량을 받치는 인프라 벤더: [[tech-bridge-stigg-ai-companies-building-banks]](과금) · [[tech-bridge-runlayer-self-improving-skills-mcp]](MCP gateway) · [[tech-bridge-composio-dashboard-is-dead]]
- [[tech-bridge]] · [[tailscale]] · [[remy-guercio]] · [[ai-gateway]]
