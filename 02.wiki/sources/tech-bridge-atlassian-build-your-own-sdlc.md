---
title: "Tech Bridge — 직접 만드는 SDLC (Andy Wong · Andrei Bocan · Shane Wolf, Atlassian): 코드의 왼쪽과 오른쪽을 에이전트로 — Jira coding agent·AI reviewer·AutoDev·Context Engine, 그리고 Wi-Fi가 삼킨 워크숍"
type: source
tags: [atlassian, rovo-dev, jira, sdlc, left-and-right-of-code, jira-coding-agent, autodev, ai-reviewer, review-noise, standards, ai-planner, ai-sre, context-engine, teamwork-graph, agentic-search, monorepo, authority, verified-badge, stale-docs, decision-history, acceptance-criteria, sandbox, credits, model-routing, skills, harness, wip-limit, cost-limits, review-bottleneck, roi, organizational-steering, epic-breakdown, workshop, vendor-pitch, members-only, video]
source-url: https://www.youtube.com/watch?v=ks55L-DkLE8
source-type: video
author: Tech Bridge (한영자막 재배포) · 발표 [[andy-wong|Andy Wong]](자막에서 자기소개 — Atlassian 4년, AI 2.5년) · [[andrei-bocan|Andrei Bocan]](AutoDev — Andy가 "Andre"로 소개, 철자는 제목·설명란) · [[shane-wolf|Shane Wolf]]("manager", context engine/code chat — Andy가 소개) · [[atlassian|Atlassian]] · 행사 **AI Engineer World's Fair(발화)** · 녹화일 미발화
date-published: 2026-10-16
ingested: 2026-10-17
created: 2026-10-17
updated: 2026-10-17
---

# Tech Bridge — 직접 만드는 SDLC (Andy Wong · Andrei Bocan · Shane Wolf, Atlassian)

[[tech-bridge|Tech Bridge]]가 재배포한 [[atlassian|Atlassian]] 3인의 **[[ai-engineer|AI Engineer]] World's Fair 워크숍 57:21, 공식 챕터 22개**(*"Welcome to the AI engineers world's fair."* 00:00~00:02). **2026-10-14 멤버 전용으로 처음 보였고 2026-10-17 공개 전환**, `upload_date` 20261016. 앞 11분은 [[andy-wong|Andy Wong]]의 제품 개관, 그다음은 **Wi-Fi 장애로 실습이 무산되며 생긴 약 25분의 Q&A**, 뒤에 standards 데모 · [[andrei-bocan|Andrei Bocan]]의 AutoDev · AI Planner · [[shane-wolf|Shane Wolf]]의 context engine · 청중 Q&A가 온다. 벤더 워크숍이고 측정치는 리뷰 댓글 해결률 한 쌍뿐이다. 테제(재구성):

> **코딩 도구의 생산성 향상은 줄어들고 있으니, 기회는 코드의 왼쪽(계획·백로그·명세)과 오른쪽(리뷰·표준·운영)에 있다. 그 전부를 묶는 것은 조직 맥락이다 — Jira·Confluence·Bitbucket·Slack을 잇는 그래프 위의 agentic search. 자율 개발은 되지만, 리뷰가 병목이라 팀이 소화할 만큼만(WIP·비용 한도) 내보내고, 명세가 부족하면 사람에게 되묻고, 무엇이 참인지는 사람이 정한다.**

> *"as we have more AI curing[=coding] tools kind of productivity gains from those tools are kind of tapering"* (01:34~01:41) · *"our biggest opportunities are tapping on the on the everything left and right of code"* (01:45~01:51) · *"at the end of the day, you need a human to tell like yes, this is actually true"* (20:21~20:25) · *"the reviewing step is where things go to die"* (45:32~45:35) · *"historical information about why decisions were made are something that's often left out of um agent generated code"* (49:01~49:07)

이 위키에 새로 생기는 것은 **[[atlassian|Atlassian]]**(첫 조직 페이지 — 그동안 플러그인·MCP 맥락의 언급만 있었다)과 화자 3인, 그리고 개념 하나 [[review-wip-limit]](신규 제안 — 자율 에이전트가 내는 PR을 팀이 소화할 양으로 묶는 한도)이다. 나머지는 기존 페이지의 **새 증언**이다 — [[context-engine]](두 번째 벤더: Unblocked의 과제별 묶음 push와 달리 *"more agentic search"*), [[automated-code-review]](자체 학습 모델로 저가치 댓글 필터, 40% vs 45), [[executable-standards]]·[[hard-vs-soft-enforcement]](standards는 Markdown이고 *"pretty similar to linting (…) a lot more loose"*, CI check 매핑 없음), [[verification-bottleneck]](*"where things go to die"*), [[agent-roi-measurement]](ROI insights·크레딧), [[automatic-model-routing]](*"We currently don't have anything out (…) doing smart routing"*), [[agent-readiness]](*"get code bases agent ready in a fairly light touch way"*), [[spec-driven-development]](저명세 백로그는 사람에게 되묻기), [[plan-to-ticket-pipeline]](Epic 분할 + automation rules), [[context-rot]]·[[company-brain]](verified badge, 결정의 이유).

ASR·ko 보정: ko는 **제품명을 거의 지킨 적이 없다** — Jira coding agent → **"Jira 스케줄링 에이전트"**(25:08 이하, `en` 공유), AutoDev → **"자동차 개발"**, Confluence → **"합류점"**, monorepo → **"원숭이"**(18:34~18:52), Markdown → **"가격 인하"**(51:25), lint → **"먼지"**(40:55), CI check → **"IQ 검증"**(51:31, `en` 공유), agent → **"부동산 중개인"**(55:17)·"의약품"(03:53). 반전·수치: *you don't snapshot it* → **"스냅샷으로 저장했습니다"**(20:33), *the login are like very secure*(반어) → "매우 안전합니다"(34:24), *three five PRs a week* → **"세 명 … 5개의 PR"**(41:55), *less than a month ago* → **"한 달 만에 해냈어요"**(56:56), *decisions were made* → **"납치된"**(49:02). 전체 목록은 raw.

> ⚠️ **수치는 한 쌍, 정의 없음.** *"around 40% uh human code resolution rate which is rather close to human baseline of 45"*(06:11~06:20) — 무엇의 비율인지·분모·기간 미발화, **en-orig "45"에는 단위가 없다**(ko·`en` "45%"). *"15,000 repositories"*(47:42)는 *"I think"* 가 붙은 화자 기억이고, *"10,000 services"*(42:30)는 Rails 버전 이전 **가정 예시** 안에 있다.
>
> ⚠️ **실습은 영상에 없다.** 로그인 안내 뒤 *"Apologies, some Wi-Fi issues."*(11:48) — *"I don't think anybody's able to connect to the Wi-Fi."*(24:15~24:16). JCA를 실제로 돌리는 장면은 없고, 기능 설명은 슬라이드 설명·데모 한 번(standards, 36:49~38:19)·Q&A 답변에서 온다.
>
> ⚠️ **화자 귀속 일부 추정.** Wi-Fi 장애 중 Q&A(15:44~35:31)의 주 응답자는 이름으로 지목되지 않는다. 답 중 *"Shane who's currently working on Wi-Fi"*(17:49~17:50)라고 하므로 Shane은 아니고, 31:15 Andy가 Andrei를 부른 뒤의 말버릇(*"Sorry, the question was"*)과 같아 **Andrei로 추정**한다. 아래 §3~§6의 귀속은 그 추정 위에 있다.
>
> ⚠️ **과금 답이 엇갈린다.** *"the billing is through atlassian credits"*(26:33~26:36) → *"it uses your own API keys"*(26:39~26:42) → *"It's credits. (…) It's like pay as you go."*(27:07~27:11). 정리되지 않는다.
>
> ⚠️ **멤버 전용 → 공개.** 2026-10-14 멤버 전용으로 처음 보였고 2026-10-17 공개(오케스트레이터 전달). `upload_date` 20261016(`timestamp` 2026-10-16 03:00:33 UTC)이 어느 시점의 값인지는 해석하지 않는다. 녹화일은 발화되지 않는다(연도 단서 *"the great unsolved problem of uh 2026"* 24:19~24:22뿐).

## 1. 제품 지도 — 코드의 왼쪽과 오른쪽 (00:00~10:48, Andy Wong)

- 출발점: *"as we have more AI curing[=coding] tools kind of productivity gains from those tools are kind of tapering. um as we have more and more tools coming out and thus us at Atlastian we believe that what our biggest opportunities are tapping on the on the everything left and right of code. So everything involving planning orchestration uh the code review process as well as the operations part"*(01:34~01:58) ⚠️ "tapering"의 근거 데이터는 발화되지 않는다(슬라이드에만 있었을 수 있음).
- 목록: *"the teamwork graph (…) AI planner, AI autodev, reviewer, s sur[=SRE] um and and central of all that is something we call the AI context machine[=engine]"*(02:06~02:22).
- ⭐ **Jira coding agent(JCA)** — *"the Elastian coding agent natively uh that has deep organizational knowledge within the Atlassian ecosystem"*(02:30~02:36), Jira 티켓·Confluence 문서·*"email, Slack"*(02:46~02:48)을 읽어 티켓을 계획·구현한다. PR을 Jira 안에서 다룬다(03:00~03:10).
- **타사 에이전트 할당**: *"you are able to assign to uh agents such as claude, cursor, codeex, whatever agent you personally prefer"*(03:25~03:32) → [[claude-code|Claude]] · [[cursor|Cursor]] · [[codex|Codex]].
- **SDLC automations**: Jira 자동화 조건이 맞으면 JCA나 다른 에이전트로 코드를 생성(03:39~03:56) → [[scheduled-agent-automations]]
- **AI reviewer**: *"catch bugs enforce standards and verify requirements every time you do make a pull request"*(04:18~04:24), *"review does go beyond the code"* — Jira·Confluence·SCM·Slack 맥락으로 *"a holistic view of what your code PR needs to implement"*(04:24~04:43).
- **중앙 관리 standards**: 조직·팀별 기준을 저장소마다 적용, *"GitHub, GitLab, Bitbucket Cloud"*(05:15~05:22) 모두.
- ⭐ **잡음 필터**: *"some of the code review processes (…) provide a little bit too many comments that are not of a high value. So we what we've been doing at Devi is we uh train a few models ourselves filter those"*(05:35~05:51) → *"around 40% uh human code resolution rate which is rather close to human baseline of 45"*(06:11~06:20). ⚠️ 정의·분모 미발화(위).
- **AutoDev**: *"it goes through your jur jura board. Uh identifies which (…) tickets are I would say able to be able to be autonomously ran. Um applies all the standards initiatives um and then creates a poll request ready for review"*(06:50~07:08). 설정: *"maximum number of credits you want to use per month (…) maximum number of like tickets you want per per user"*(07:14~07:22), 대상 저장소. 대시보드(07:32~07:50), Slack 연동(07:55~08:12), *"ROI insights"*(08:15~08:25).
- **AI SRE**: 이전 incident·Jira·Confluence 맥락으로 *"root cause why an incident is happening and provide suggestions of how to (…) remediate"*(08:42~08:52), 영향 범위 요약·완화 단계를 Slack으로(08:56~09:28). ⚠️ 이름은 en-orig에 또렷이 나오지 않는다(*"AIR"* 08:37 — 챕터·ko 기준 "AI SRE").
- **AI Context Engine**: *"many of us have been working in large monor repos and all that context is scattered"*(09:39~09:44) → *"create you know like a standardized context for you uh for all of your agents"*(09:58~10:02), *"semantic code search"*(10:24~10:26). *"That's the biggest thing we're trying to do in the last year."*(10:08~10:09) 도구를 *"browser (…) IDE or (…) CLI"*(10:43~10:46) 플러그인으로.

→ [[ai-native-sdlc]] · [[software-factory]](같은 "SDLC 전체" 지도, 벤더 다름) · [[automated-code-review]] · [[context-engine]]

## 2. 실습 무산 (10:52~15:23)

계정 번호를 나눠 주고(*"that is going to be your account number"* 11:12~11:15) 로그인을 안내하던 중 *"Apologies, some Wi-Fi issues."*(11:48). 이후 4분가량 연결 시도 잡담(*"Oh, the Wi-Fi is quite slow."* 13:23). 실습 저장소는 Bitbucket의 *"Atlassian swag"*(22:29~22:35). 세션 중반의 농담 — *"I think that was like the the the great unsolved problem of uh 2026. And I think if if anything's going to save us from uh AGI, it's going to be the Wi-Fi."*(24:17~24:28)

## 3. Context Engine — 그래프 위의 agentic search, 모노레포 대신 (16:06~19:19, ⚠️ Andrei 추정)

- *"we have a number of I guess graph databases inside of Atlassian that connect to all of the data that you end up plugging into (…) your Atlassian products (…) Confluence, um Jira, Bitbucket"*(16:11~16:30). 연결은 *"through inferences as you use the product or you can like have the connections be explicit"*(16:37~16:42) — 예: Jira 티켓 ↔ Confluence 스펙 문서. Notion·Slack 같은 서드파티도(16:48~16:58) → *"this whole tapestry of context"*.
- ⭐ *"so it's it's a gentic[=agentic] search on top of all of all of that context"*(17:10~17:14). 용도: 다른 팀의 플랫폼 문서나 *"some other initiative that's happening on the other side of the organization that somehow happens to impact"*(17:28~17:37) 것을 *"your current agentic coding session"*(17:41~17:45)으로.
- ⭐ **모노레포의 대안**: *"we've seen a lot of teams (…) opt for monor repos in order to like have all their their agents like have the context available at all times that has some shortcomings"*(18:13~18:27) — *"opting for a monor repo ends up meaning that you're opting for the debt of having a monor repo, building the tooling around it"*(18:34~18:40). *"with a code context engine, we've been able to like just have product repos feel like monor repos because you can pull in that engine at hawk[=ad hoc]. It's super fast."*(18:46~18:57)
- *"conflence document is just a snapshot of a thing that happens once but like the truth is in the code"*(19:05~19:10)

→ [[context-engine]] · [[agentic-search]] · [[code-only-index-blind-spot]] · [[agent-knowledge-sourcing]] · [[code-knowledge-graph]]

## 4. 무엇이 참인가 — 사람이 정하는 권위 (19:57~21:34, 34:52~36:07)

- 질문 ① 맥락을 즉석에서 만드나 ② 충돌하는 정보는(19:57~20:07). ⭐ *"you have agents that derive knowledge from like a bunch of different sources, but like at the end of the day, you need a human to tell like yes, this is actually true. this thing is like incidentally true or like it's true for like this specific case."*(20:18~20:27)
- 즉석 조회: *"you don't snapshot it to some extent because of that (…) you have the information on the fly (…) if you cache it then like it risks being stale"*(20:34~20:49)
- 권위: *"the way that we we've historically dealt with um authoritiveness (…) has been to provide that as a feature for like the the human in the loop to like be able to say like yes cool this is verified this has higher authority than this other piece of content"*(20:55~21:12). Jira work item에는 더 어렵고, ⭐ *"the risk by automating that stuff is like oh you end up like having things automated automatically end up being authoritative which is weird"*(21:22~21:32).
- 오래된 문서(10~15년 쓴 조직, 35:14~35:31): *"our experience has mostly been okay with this by in in large part because we tend to favor like more recent results"*(35:34~35:43), 10년 된 문서가 여전히 기준이면 *"we (…) shipped a thing a while back in in um conference[=Confluence] that's the verified badge like that's basically the thing that we use internally to say like yes cool this is like still the latest and greatest"*(35:53~36:05).

→ [[company-brain]](사람 승인 쪽) · [[context-rot]] · [[agent-memory]](*"a bunch of talks at the conference about about memory"* 20:10~20:13) · [[named-human-accountability]]

## 5. 수락 기준 검증·샌드박스·과금 (24:55~29:00, ⚠️ Andrei 추정)

- *"we expect the work item to have a checklist of hey these are the (…) acceptance criteria and as the juro coding agent uh generates the code (…) it'll go in and like verify those specific things once it thinks it's done"*(25:15~25:30)
- 샌드박스: *"it has a full sandbox. It can install things, it can run things"*(25:34~25:38) — 저장소에 실행 방법이 있으면 *"it can pop open a browser and then like go and like run that those verification steps"*(25:41~25:48). 호스팅, BYO 불가: *"We don't have that ability yet. (…) it's a proprietary Atlassian sandbox. Uh it's again it's a container. (…) it has Docker enabled"*(26:03~26:13).
- 과금·모델: 위 ⚠️(답이 엇갈림). *"all the anthropic models all the openi models"*, Gemini는 *"I don't remember"*(26:52~27:00). JCA는 *"it's out now. It's been out for for a hot minute."*(27:22~27:25)
- 크레딧 보고는 *"split split out by product"*(28:08~28:10), 작업 단위 보고는 *"No, no, not yet."*(28:28) — ⭐ *"you want to make sure that like the ROI is there (…) when somebody is (…) going to spend like I don't know uh 1 billion tokens on a thing then you want to make sure that like that is something that you actually want to have done as opposed to like somebody's open claw running somewhere off in the uh in the periphery"*(28:42~28:58)

→ [[verifiable-goals]] · [[agent-roi-measurement]] · [[openclaw]](⚠️ *"open claw"* 판독)

## 6. 모델 라우팅·스킬·하네스 (31:13~33:12, Andrei)

- *"with uh the jer coding agent currently I think we let you select which model like you want to route to"*(31:26~31:31). 스킬·서브에이전트별로 모델 지정 가능(31:35~31:46). ⭐ *"We currently don't have anything out uh that would do be doing like doing smart routing. That is something that we're working on with uh in in autodev"*(31:46~31:58) — 성공 사례 지표를 보여 주고 *"make sure that that's a policy that you want to enforce or not"*(32:03~32:07).
- *"with the juro coding agent that's essentially we uh give you a harness and there's a model selection at the top level of the harness and then with the skills you can figure out like right cool like this is for this specific task (…) I want this model this sub agent needs to be using"*(32:49~33:05)

→ [[automatic-model-routing]](아직 없음 — 사람이 정책으로) · [[agent-skills]] · [[harness-engineering]]

## 7. Standards — Markdown 규칙, 느슨한 lint (36:29~38:19, 40:42~41:31, 51:20~52:08)

- 데모(Andy): standards 페이지에서 새 standard *"design token enforcement"*(37:11~37:19)를 만들고 설명·규칙을 넣고, *"repositories matching a pattern"*(37:37~37:39)으로 적용 범위를 정한다. 그러면 *"the robo dev[=Rovo Dev] jur like the coding agent itself will be running through the pull request process and adding (…) comments to see if (…) your poll request isn't adhering to all the standards"*(38:05~38:17). ⚠️ *"unfortunately, the standards aren't built into the demo itself"*(36:34~36:35) — 데모 화면은 standards 설정까지.
- ⭐ Andrei: *"standards are to some extent pretty similar to linting to some degree but they're a lot more uh loose uh when you have the uh agents uh enforce them"*(40:50~41:04). 두 방향 — 리뷰어가 *"any code that will end up landing in your codebase going forward"*(41:13~41:18), AutoDev가 *"scan existing (…) codebase and then figure out how we land uh PRs progressively in order to get all of your existing stuff into compliance"*(41:20~41:31).
- 청중: standards가 Markdown인지(*"That's correct. Yes."* 51:27~51:28), *"Do you have any way to map those to something like a CI check?"*(51:28~51:33) → *"I don't think we can pro we provides that out of box but I will relay that over to the standards team"*(51:58~52:03). 청중: *"that really need to make it a little bit more deterministic"*(52:05~52:07).

→ [[executable-standards]] · [[hard-vs-soft-enforcement]](soft의 벤더 제품판, 청중이 hard를 요구) · [[tech-bridge-sentry-stop-prompting-codify-linters|Sentry 편]](리뷰 기록 → lint 규칙)

## 8. AutoDev — 팀이 소화할 만큼만 (38:54~46:15, Andrei Bocan)

- ⭐ *"this is essentially our forign[=foray] to like the AISDLC orchestration space. Um the thought process is to basically get you back some capacity (…) in order to let your engineering team focus on feature work"*(39:25~39:43). 첫 릴리스: *"grabbing work items from your backlog and grabbing the ones that we feel confident that uh the agents can handle autonomously and then just putting up PRs for your team to review"*(39:48~40:02), *"iterating on your harness as well so that we can get code bases agent ready in a fairly light touch way"*(40:03~40:12).
- ⭐ **리뷰 부담 한도**: *"nobody's going to approve a PR that's like change half your code base because now you have a new standards (…) with autod we want to be mindful of how much work we're actually hoisting on your team uh nobody wants to spend time reviewing uh 50 PRs a day so like we have configuration for letting you say cool like my team wants to get assigned I don't know each individual gets assigned three five PRs a week"*(41:32~42:01). 다시: *"the work in progress limit (…) where you want to make sure that like your team isn't getting inundated with PRs"*(43:50~43:58).
- **organizational steering**: *"everybody's trying to move from whatever some version of Rails to a different version of Rails and it's a big thing and we have like 10,000 services"*(42:25~42:30) — 한 팀에 집중해 *"the agents essentially do the do the work and then you only have a human do the coordination"*(42:45~42:50), 그 고리를 *"some sort of memory"*(42:52)로 묶는다. *"that's sort of the vision"*(42:54~42:56) — ⚠️ 비전 진술, 출시 기능 아님.
- 가시성: Jira 보드에 두는 이유 — *"that's the thing that most people stare at like it or not"*(43:36~43:41). 잘못 집거나 잘못 배정하면 개입하고 *"we will learn from that experience"*(43:33~43:36).
- **비용 한도**: *"you want to be able to set limits for how much we want to spend per ticket how much we want to spend per week all that stuff seems like it's uh just table stakes at this point"*(44:18~44:28)
- ⭐ **저명세 항목은 사람에게**: 백로그에는 *"one summary line that says is do the thing"*(44:56~44:58) 같은 항목이 많고, *"we don't have the confidence that we can work on them because we don't know exactly what the goals of them are. And that's where like we will pull it pull in a human in the loop and say (…) can you help me specify it?"*(45:02~45:18)
- ⭐ **리뷰가 병목**: *"the other bit that we've also noticed with some of these autonomous workflows is the the the reviewing step is where things go to die. Um because people again are uh busy with other things."*(45:28~45:40) → *"reach out to people at the opportune time"*(45:43~45:46), 수단은 *"Slack for for the the initial release"*(45:58~46:00).
- ROI: *"you're not overpaying for the amount of work that we're doing and then it's work that you actually want to get done"*(46:05~46:12)

→ [[review-wip-limit]](신규) · [[verification-bottleneck]] · [[spec-driven-development]] · [[human-as-async-api]](Slack 호출) · [[agent-readiness]] · [[legacy-code-modernization]](Rails 버전 이전) · [[agent-fleet-learning]](⚠️ memory 구현 미발화)

## 9. AI Planner (46:17~47:08, Andy)

*"if you have a spike or project managers or say you're a manager that wants to see if something is feasible for your current repository"*(46:34~46:42) → context engine을 거쳐 *"what is in your repository what is your plan and is it feasible"*(46:51~46:56)를 판단하고, 구현 분해와 *"a few ways to execute it"*(47:08)를 준다. 데모 없음(*"I don't know if we have a full demo"* 38:41~38:42).

→ [[plan-to-ticket-pipeline]]

## 10. Code Chat — 결정의 이유를 맥락으로 (47:30~51:15, Shane Wolf)

- *"I think we have 15,000 repositories across the company and asking a simple question like where do I implement this change or where is X Y and Z implemented or what services are using this other service are really really complicated"*(47:40~47:54)
- ⭐ *"at the core of the context engine it is narrowing down the retrieval and the search space to scope it to like where this answer is most likely uh lives within the code and then reaching out from there and like digging into the code"*(47:54~48:09), 그 위에 teamwork graph 정보.
- ⭐ *"documentation historically out ofd and inaccurate. If you're searching only across documentation, you're going to get something that was true at some point in time. Um but it's also a lot of really valuable information. (…) the reason why those things are decided at the time are valuable for making changes in the future."*(48:15~48:41) → *"historical information about why decisions were made are something that's often left out of um agent generated code, but it's really important um historical context for like not re remaking mistakes of the past."*(49:01~49:14)
- 쓰임(⚠️ Shane 추정): AI Planner가 많이, AutoDev도, *"AI reviewer doesn't use it a lot today"*(49:54~49:56). **Rovo Chat**: *"we're in early access with a few customers now. We just announced it a couple months ago"*(50:05~50:11) — 지금은 Confluence 검색·GitHub/Bitbucket search API로 답하고, code context를 켜면 *"a more cohesive understanding of the code grounded in the truth today the historical decisions that went into it"*(50:32~50:38).
- 외부 노출: *"the teamwork graph CLI (…) that's where we're starting to expose a lot of these capabilities"*(50:50~50:54), *"the context engine itself is more agentic search is the way to think about it"*(50:56~51:00), *"Team graph CLI has access to all the um code context skills."*(51:12~51:15)

→ [[context-engine]] · [[decision-quality]] · [[code-only-index-blind-spot]] · [[tech-bridge-sourcegraph-codebase-visibility|Sourcegraph 편]](같은 "수만 저장소" 문제)

## 11. 청중 Q&A 끝 (52:11~57:15)

- **Epic 분할 → 에이전트 웨이브**(⚠️ Andy 추정): *"with JCA what you can do you can take an epic (…) can you break this down into like smaller issues for me"*(53:03~53:09), 이어 *"automation rules"* 로 분할 후 JCA 세션을 자동 시작(53:17~53:36). 다른 화자: *"I don't think there's anything that would prevent you from kind of extrapolating that further"*(53:36~53:40) — V0·V1·V2 Epic으로. *"I'm not sure if Robo[=Rovo] directly could do it, but I definitely think you can do with automations"*(54:05~54:10), *"autodev might be able to do some of that"*(54:10~54:13).
- 로컬 IDE와의 관계: *"it is isolated very much the agent sessions"*(54:56~54:58), 클라우드 VS Code 인스턴스 변경은 실시간, *"whatever changes you make on the ID it's a separate kind of like a separate instance"*(55:12~55:15). 개발 환경은 *"It is docker."*(56:20)
- 스킬: *"we actually just started uh supporting skills, I think, just not too long ago"*(56:31~56:35), AI reviewer는 *"less than a month ago"*(56:54~56:56).

## 이 위키와의 연결

### 이어지는 것

- **[[context-engine]] — 두 번째 벤더.** [[unblocked|Unblocked]]는 과제별 *grounded context* 묶음을 **push**하는 쪽이었다. Atlassian은 같은 이름을 쓰면서 *"the context engine itself is more agentic search"*(50:56~51:00)라고 한다 — 그래프 DB(추론 연결 + 명시 연결) 위에서 에이전트가 검색 공간을 좁혀 들어간다(47:54~48:09). 새로 더하는 것 둘: ① **모노레포 대체 논거**(*"product repos feel like monor repos"* 18:52~18:54), ② **권위(authority)를 사람이 표시**하고 자동화하지 않는다(21:22~21:32, verified badge 35:55~36:05). 둘 다 효과 수치는 없다.
- **[[automated-code-review]]** — 잡음(저가치 댓글) 필터를 **자체 학습 모델**로(05:46~06:00). 성공 지표가 *"human code resolution rate"* 인 것은 이 페이지의 *"is a human accepting my answer"*(Voss) 계열이다. ⚠️ Cursor의 resolution rate 52%→70%+([[tech-bridge-death-of-code-review]])와 **정의·분모가 달라 비교하지 않는다**. "human baseline 45"도 정의 미발화.
- **[[verification-bottleneck]]** — *"the reviewing step is where things go to die"*(45:32~45:35). 답은 리뷰 자동화가 아니라 **흐름 제어**(1인당 주 3~5 PR, WIP 한도) + **사람 호출**(Slack). → [[review-wip-limit]]
- **[[executable-standards]] · [[hard-vs-soft-enforcement]]** — standards = Markdown, *"a lot more uh loose"* 한 lint(40:52~41:04). 청중이 CI check(결정적 검사) 매핑을 묻자 **기본 제공 없음**(51:58~52:03). 이 위키의 hard 쪽 사례들([[tech-bridge-sentry-stop-prompting-codify-linters|Sentry 편]]의 lint 규칙화)과 반대 위치의 제품이다.
- **[[spec-driven-development]]** — 저명세 백로그 항목은 *"can you help me specify it?"*(45:16~45:18)로 사람에게 되묻고, 명세가 *"a good level of specification"*(45:19~45:20)에 이르러야 작업한다. 수락 기준 체크리스트를 JCA가 스스로 검증(25:15~25:30). → [[verifiable-goals]]
- **[[agent-roi-measurement]]** — ROI insights 대시보드(08:15~08:25, 46:02~46:15), 크레딧 보고는 제품별까지(28:08~28:28), *"1 billion tokens"* 가정(28:48~28:50). 지표 정의는 없다.
- **[[automatic-model-routing]]** — *"We currently don't have anything out (…) doing smart routing"*(31:49~31:53). 모델 선택은 하네스 최상위 + 스킬별(32:52~33:05), 즉 **사람이 정책으로** — [[tech-bridge-tailscale-aperture-ai-without-lock-in|Tailscale 편]]의 "라우터가 아니라 정책"과 같은 쪽.
- **[[agent-readiness]]** — *"iterating on your harness as well so that we can get code bases agent ready in a fairly light touch way"*(40:03~40:12). Factory의 점검 프레임워크와 달리 **자율 개발을 돌리면서** 하네스를 고친다는 진술(방법 미발화).
- **[[software-factory]] · [[ai-native-sdlc]]** — "코드의 왼쪽과 오른쪽"(01:45~01:51)은 Factory·Tessl의 SDLC 전체 루프와 같은 지도를 **기존 협업 도구(Jira·Confluence) 안에서** 그린다. 차이는 **신호의 출처가 백로그**라는 점(*"grabbing work items from your backlog"* 39:48~39:53).

### 갈리는 것

> ⚠️ **긴장(약): 맥락을 어디에 모으나.** [[company-brain]]은 조직 맥락을 **에이전트가 읽을 파일**(링크된 마크다운)로 한곳에 둔다. Atlassian 응답자는 저장소를 한곳에 모으는 모노레포를 *"the debt of having a monor repo, building the tooling around it"*(18:37~18:40)로 보고, 저장소는 흩어 둔 채 **원격 code context를 즉석 조회**한다(18:46~18:57, *"you don't snapshot it"* 20:34~20:37). 근거는 *"Internally, it's been"* 수준의 내부 경험(18:32~18:34)이고 수치가 없다. 이 위키에서 모노레포를 맥락 전략으로 직접 다룬 다른 소스는 아직 없다([[tech-bridge-uber-debug-assist|Uber 편]]은 모노레포를 *환경*으로만 언급).

> ⚠️ **긴장: 문서는 낡았는가, 결정의 기록인가.** 응답자는 *"conflence document is just a snapshot (…) the truth is in the code"*(19:05~19:10)라 하고, Shane은 문서가 *"out of date and inaccurate"* 이지만 **결정의 이유**가 가치 있다(48:15~48:41)고 한다. 같은 회사 안에서 문서의 지위가 "낡은 스냅샷"과 "결정 이력" 사이에 놓인다 — [[context-rot]](낡은 맥락의 해)과 [[decision-quality]](결정 근거 보존) 양쪽에 걸친다.

> **"더 많은 AI"가 아니라 "덜 내보내기".** [[tech-bridge-gitar-agentic-pr-validation|Gitar 편]]은 리뷰 병목에 *"more AI"* 로, [[tech-bridge-g2i-generation-cheap-evaluation-expensive|G2i 편]]은 리뷰 면을 줄이는 쪽으로 답했다. AutoDev는 **생성 쪽 유량을 팀의 리뷰 용량에 맞춘다**(41:43~42:01, 43:50~43:58) — 세 번째 답. 단 셋 다 벤더 발표다.

## 해소하지 않고 표시만 한 것

- *"human code resolution rate"* 40%와 *"human baseline of 45"* 의 정의·분모·측정 범위.
- 과금: Atlassian credits vs 자기 API 키(26:33~27:11).
- Wi-Fi 장애 중 Q&A 응답자의 이름(Andrei 추정), 49:26~51:15의 화자(Shane 추정), 51:35~53:36(Andy 추정).
- *"Devi"*(00:18 외)의 정체·철자. *"between like and devs"*(32:45~32:47 — Rovo/Rovo Dev 추정).
- AutoDev의 *"some sort of memory"*(42:52)·*"we will learn from that experience"*(43:33~43:36) 구현. 스마트 라우팅 계획의 기준.
- AI SRE·AI Planner의 실제 동작(데모 없음). verified badge 외 권위 신호의 랭킹 방식(*"favor like more recent results"* 35:41~35:43).
- *"10,000 services"*(42:30)가 Atlassian 실제 수치인지 가정인지.
- 녹화일. 청중 질문 원문 다수(en-orig 공백).

## 등장 개체

- 인물: [[andy-wong|Andy Wong]](신규 제안 — 자막에서 자기소개) · [[andrei-bocan|Andrei Bocan]](신규 제안) · [[shane-wolf|Shane Wolf]](신규 제안 — [[thomas-wolf|Thomas Wolf]](Hugging Face)와 다른 사람)
- 조직: [[atlassian|Atlassian]](신규 제안) · [[ai-engineer|AI Engineer]](World's Fair — 발화) · [[anthropic|Anthropic]] · [[openai|OpenAI]](지원 모델로만)
- 제품(→ [[atlassian]] 페이지의 섹션으로 제안): Rovo Dev · Jira coding agent(JCA) · AI reviewer · standards · AutoDev · AI Planner · AI SRE · AI Context Engine · Teamwork Graph(CLI) · Code Chat / code context · Rovo Chat · Confluence verified badge · Jira automations — 개별 페이지 없음
- 타사 제품: [[claude-code|Claude]] · [[cursor|Cursor]] · [[codex|Codex]](할당 대상으로만) · [[openclaw|OpenClaw]](⚠️ *"open claw"* 판독, 한 번) · GitHub · GitLab · Bitbucket · Slack · Notion · Docker · VS Code · Gemini — 페이지 없음
- 개념: [[review-wip-limit]](신규 제안) · [[context-engine]] · [[agentic-search]] · [[automated-code-review]] · [[executable-standards]] · [[hard-vs-soft-enforcement]] · [[verification-bottleneck]] · [[spec-driven-development]] · [[verifiable-goals]] · [[agent-roi-measurement]] · [[automatic-model-routing]] · [[agent-skills]] · [[harness-engineering]] · [[agent-readiness]] · [[software-factory]] · [[ai-native-sdlc]] · [[plan-to-ticket-pipeline]] · [[scheduled-agent-automations]] · [[human-as-async-api]] · [[company-brain]] · [[context-rot]] · [[agent-memory]] · [[decision-quality]] · [[code-only-index-blind-spot]] · [[agent-knowledge-sourcing]] · [[code-knowledge-graph]] · [[named-human-accountability]] · [[legacy-code-modernization]] · [[agent-fleet-learning]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=ks55L-DkLE8> (57:21, `upload_date` 2026-10-16, 2026-10-14 멤버 전용 첫 노출 → 2026-10-17 공개)
- raw: `01.raw/articles/2026-10-16_직접 만드는 SDLC — Andy Wong, Andrei Bocan, Shane Wolf (Atlassian).md`
- 설명란 링크: <https://www.atlassian.com/software/rovo-dev> · 화자 LinkedIn 3개 (⚠️ 열어 보지 않았다)
- 다른 context engine: [[tech-bridge-unblocked-context-engine-structured-queries]] · 수만 저장소 문제: [[tech-bridge-sourcegraph-codebase-visibility]]
- 리뷰 병목의 다른 답: [[tech-bridge-gitar-agentic-pr-validation]] · [[tech-bridge-g2i-generation-cheap-evaluation-expensive]] · [[tech-bridge-death-of-code-review]] · [[tech-bridge-sentry-stop-prompting-codify-linters]]
- 같은 World's Fair 워크숍 형식: [[tech-bridge-cooking-with-codex]]
- [[tech-bridge]] · [[atlassian]] · [[andy-wong]] · [[andrei-bocan]] · [[shane-wolf]]
