---
title: "Tech Bridge — Codex로 요리하기 (Charlie Guo · Gabriel Chua, OpenAI): 컨텍스트 → 만들기 → 행동 → 장기 작업 → 시간 → 어디에나"
type: source
tags: [codex, openai, coding-agent, workshop, long-running-agents, subagents, thread-handoff, goals, hooks, automations, app-server, computer-use, vendor-claim, video]
source-url: https://www.youtube.com/watch?v=RVnSsolR3uE
source-type: video
author: Tech Bridge (한영자막 재배포) · 발표 [[charlie-guo|Charlie]] · [[gabriel-chua|Gabriel]] ([[openai|OpenAI]] developer experience 팀 · 성은 제목·설명란에만) · [[ai-engineer|AI Engineer]] World's Fair 워크숍 · 2026-06-29(월) 녹화
date-published: 2026-10-10
ingested: 2026-10-11
created: 2026-10-11
updated: 2026-10-11
---

# Tech Bridge — Codex로 요리하기 (Charlie Guo · Gabriel Chua, OpenAI)

[[tech-bridge|Tech Bridge]]가 재배포한 **2시간 워크숍의 앞 1시간(1:07:05), 공식 챕터 20개**(설명란 타임라인은 22줄). [[openai|OpenAI]] developer experience 팀의 [[charlie-guo|Charlie]]와 [[gabriel-chua|Gabriel]]이 [[ai-engineer|AI Engineer World's Fair]] 첫날 아침에 연 *"cooking with Codeex[=Codex] workshop"*(00:13~00:16)이다. **이 위키가 받은 첫 OpenAI 직원의 [[codex|Codex]] 사용법 소스** — 지금까지 Codex는 CEO의 1인칭([[tech-bridge-altman-devday-dots]]), 고객 사례, 제3자 관찰([[tech-bridge-skill-engineering-dark-arts]], [[tech-bridge-agents-vs-humans-optimizer-speedrun]])로만 들어왔다. 뼈대는 *"six steps to cooking with Codex"*(05:15~05:17):

> **① 컨텍스트를 줘라 → ② 그냥 만들어라 → ③ 행동하게 하라(컴퓨터 사용) → ④ 복잡한 장기 작업을 함께하라 → ⑤ 시간에 걸쳐 일하게 하라(자동화) → ⑥ 어디에나 넣어라(App Server).** 그리고 마무리: 개별 요청에서 **루프**로, 하나에서 **여럿**으로, *"why does this process need a human at all"* 로, **기계를 만드는 기계**로.

> *"Number one you got to give Codex your context."* (05:19~05:21) · *"In so far as the instructions are clear, it still matters. Like I can't read your mind, Codex can't read your mind."* (30:02~30:10) · *"be really specific with the criteria that you're giving the model to to know when it's done (…) you want that criteria to be as verifiable as possible."* (43:32~43:43) · *"when the the delegation of work needs to be visible to you, the user versus when it just needs to be visible to the model."* (45:49~45:59) · *"how do we figure out how to build the machine that builds the machine"* (1:03:53~1:03:59)

이 위키에 개념 하나가 생긴다 → [[subagent-vs-thread-handoff]] (신규). 인물 둘 → [[charlie-guo]] · [[gabriel-chua]] (신규).

ASR·ko 보정: ko는 **단위·존재·부정을 일곱 군데서 뒤집는다** — *nearly 300 subagents* → **"300명"**(00:55), *15 hours* → **"15년"**(43:20), *every 5 minutes* → **"5초마다"**(52:09), *context is not just about best practices* → **"맥락이 중요하지 않다"**(15:13), *the in-app browser which I think we did not demo* → **"저희 앱에는 없는 것 같습니다"**(26:20), *housekeeping … you want a language model to do* → **"모델에게 맡기고 싶지 않아요"**(49:44), *approved white list* → **"백인들이 승인한"**(48:24~48:26). `en`과 공유하는 오류: *"In November 19"* → **"2019년 11월"**(42:21), *"my gaps remote"* → **"GKE"**(33:17), 성 없는 *"Gabriel"* → **"Gabriel Chua"**(52:46). 제품명도 흔들린다 — Codex → "사본"·"Cortex"·"대뇌피질"·"법전", compaction → **"다짐"**, App Server → **"섬기는 사람"**, AGENTS.md → "에이전트 SDK". en-orig의 ⭐ *"site thread"*·*"slash site"* 는 **side thread · `/side`** 다(35:53 *"side threads … ephemeral"*) — 제품 **Sites**와 다르다. 전체 목록은 raw.

> ⚠️ **당사자 진술 — OpenAI 직원이 자사 제품을 시연한다.** 수치는 전부 화자 서술이거나 화면 설명(자막엔 없다): 번역 앱 *"4 minutes and two seconds"*(12:51~12:57), appshot *"90 plus% of the time"*(18:24~18:28), 장기 과제 15시간·5시간·7시간(29:08~31:33), compaction을 *"natively train"* 했다는 서술(42:28~42:35). 남의 사례(*"nearly 300 sub aents"* 00:54, Tama의 40시간 Doom 재구현 44:18~44:28, compaction 칭찬 트윗 42:40~43:05)는 화면의 트윗 인용이고 출처는 자막에 없다.
>
> ⚠️ **녹화 시점 = 2026-06-29(월), 업로드보다 약 3개월 이르다.** *"from like the 1st of June to today which is the 29th of June"*(22:38~22:43) + *"9:00 a.m. on a Monday"*(1:04:30~1:04:35), 2026-06-29는 월요일. 행사: *"AI engineer world's fair"*(57:43~57:45). 따라서 *"지난주 출시"*·*"새 기능"* 은 **2026년 6월 기준**이다. 영상은 2026-10-06 멤버 전용으로 처음 보였고 2026-10-11 공개 확인(`upload_date` 20261010은 공개 전환 쪽 값).
>
> ⚠️ **화자 신원.** 발화엔 *"my name is Charlie"*(00:16)·*"my name is Gabriel"*(00:22)뿐, **성 Guo·Chua는 제목·설명란에만**. 어느 구간을 누가 말했는지는 넘김 발화(*"I'll let Charlie take the stage"* 08:50, *"Thanks Gabe"* 43:17, *"Thanks, Charlie"* 49:18)로 나눈 **추정**이다(raw 헤더에 구간표).
>
> ⚠️ **실습(2시간째)은 영상에 없다.** 설명란의 *"65:53 — 실습 세션 시작"* 뒤는 크레딧 안내와 음악뿐.

## 0. 무엇이 "새로운가" — 2026년 6월의 Codex 표면 (00:00~05:00)

- 커뮤니티 사례(트윗, ⚠️ 출처 미발화): 서브에이전트 ~300개 세션(00:54~01:01), Ableton 신스 플러그인(01:08~01:13), 팀원 Brent가 *"video editing with codeex driving premiere"*(01:19~01:28), 게임(스레드·서브에이전트로 오디오·아트·메커니즘·난이도 분담, 01:33~01:56), 자율주행 골프 카트(02:00~02:08), 일본 사용자가 신칸센에서 모바일로(02:37~02:47), e-ink 기기 셋에 넣은 사례(03:05~03:08).
- 신기능 세 개(03:53~04:26): **record and replay**(*"Maybe just show codeexc by doing it. It builds on sort of our technology with computer use"* 04:05~04:12) · **thread handoff**(*"push things from the cloud to the remote to your local and vice versa"* 04:14~04:18) · **모바일 앱 GA**(*"onetoone device pairing, a much more secure way"* 04:22~04:26).
- *"it's been 2026. This slide barely summarizes everything we've shipped and we're only 50% literally 50% of the year."*(04:30~04:38) — plugins · computer use · multimodality · 모바일 · **appshots**.
- 다른 에이전트 설정을 그대로 가져와 시작할 수 있다(03:17~03:24).

## 1. 컨텍스트를 줘라 (05:19~19:11)

| 장치 | 발화 | 위키 연결 |
|---|---|---|
| **appshot** | Slack 창을 단축키로 찍으면 *"it's like a screenshot, but all the text is embedded as well"*(07:24~07:31). Charlie: *"I don't copy and paste, you know, anything from Slack anymore"*(18:13~18:17) | [[context-engineering]] |
| **받아쓰기** | *"dictation to me is a really underutilized feature because we speak so much faster than we can type"*(17:41~17:48), *"we're beyond the the era where you have to make sure every single word is correct"*(17:48~17:53) | [[cognitive-offloading]] |
| **plugins** | *"bundle together skills which are best practices, external prompts (…) apps which have the configuration and provide the connectivity to external services and MCP servers which provide the tools"*(10:58~11:17) — 즉 **스킬 + 앱(커넥터) + MCP 묶음** | [[agent-skills]] · [[model-context-protocol]] |
| 플러그인 만들기 | Charlie: 어려운 대화 끝에 *"make this a skill or even better make this a plugin so that to next time I need to do this you can just invoke the plugin"*(12:41~12:48) | [[query-to-skill-distillation]] |
| **memories** | *"it is off by default"*(15:28~15:31). 안전 옵션: *"skip uh generating memories in chats that involve tools because sometimes the tools might return information that you might not want persisted"*(16:16~16:26). 비용: *"memories, uh, and Chronicle will use up a little bit more of your token budget"*(18:39~18:44) | [[agent-memory]] · [[prompt-injection]] |
| **Chronicle** | Pro 구독자용 *"research preview"* — 화면 맥락(GitHub 파이프라인을 보고 있으면 *"why is this failing"* 에 답한다, 15:46~16:02) | [[agent-memory]] |
| custom instructions | *"it's like setting the agents.mmockdown[=AGENTS.md] in the home directory. It applies to all conversations"*(16:37~16:43) | [[intent-md]] |

데모 ①: 금요일 오후 4:44에 데모 아이디어가 없었다 → Slack 브레인스토밍(*"GPT realtime translate. It's one of our latest models"* 06:39~06:42)을 appshot → *"Hey, can you just build this?"*(07:13) → **macOS 실시간 번역 앱**(*"build Mac OS plugin"* 의 AppKit·liquid glass·서명 스킬 + *"OpenAI developers plugin"* 이 API 키를 직접 만든다, 11:35~12:08). Gabriel은 *"I've never built a Mac OS app"*(06:46), *"not the best at like sort of working with like a web RTC websockets"*(13:16~13:20). ⚠️ 라이브 테스트는 오디오 장비 문제로 여러 번 반복됐고 **번역 결과는 자막에 없다**(13:31~15:01).

## 2. 그냥 만들어라 (06:17~10:46 · 19:13~20:53)

- **Codex Remote** — *"now available in chatbt[=ChatGPT] a mobile app and allows us to connect to a, you know, laptop or remote server"*(09:10~09:21). 데모: 휴대폰에서 *"visualization of this repository in the style of an IKEA instruction manual"*(09:41~09:49). *"everyone's become a manager"*(10:30~10:33) → [[agent-manager-analogy]] · [[cloud-agent-delegation]]
- **Sites** — *"launched earlier in the month in June for in preview for enterprise and business plans"*(07:57~08:03), 공유용 산출물(Agents SDK 변경 요약 사이트, 08:09~08:30; 행사 요약·오프사이트 장소 비교, 19:23~19:49). ChatGPT 워크스페이스 인증으로 팀 안에만 공개(41:21~41:27). → [[agentic-sites]]와는 다른 것(위키의 주석: 저쪽은 *에이전트가 읽는 사이트*, 이쪽은 *에이전트가 만든 사내 사이트*)
- **`/code review`** — *"review against uncommitted changes"*(19:58~20:03), 수셰프의 맛보기 비유 → [[automated-code-review]]
- 이미지 생성 스킬, 스프레드시트·문서·슬라이드 산출물(20:14~20:51).

## 3. 행동하게 하라 — 세 가지 브라우저/컴퓨터 제어 (21:08~28:23)

데모: API 없는 대시보드에서 커밋·PR 데이터를 기간별로 CSV/JSON으로 내려받기(21:26~23:15), Google Docs의 질문으로 Google Forms 피드백 양식 만들기(23:47~25:21, *"remember to make mark each question as mandatory"*). macOS에서 **커서를 빼앗지 않는다**(Charlie, 23:29~23:43).

Charlie의 선택 기준(26:05~28:15):

| 표면 | 언제 | en-orig |
|---|---|---|
| **in-app browser** | 로컬 웹앱을 만들며 상호작용·렌더링을 깊이 테스트할 때 | *"Codex has really deep hooks into that browser engine uh deeper than it has at the Chrome extension"* (26:36~26:42) |
| **computer use** | 프로그래매틱 인터페이스가 없는 데스크톱·레거시 앱 | *"it really shines when you have applications that otherwise don't have a programmatic interface"* (27:07~27:13) |
| **Chrome extension** | 로그인 상태·권한을 넘길 때 | *"the most useful for when you need to hand off um state or authorization to the agent"* (27:43~27:48); headless Chromium의 무한 캡차 대신 *"borrow your credentials"* (28:01~28:14) |

→ [[agent-native-interface]](세 번째 입장, 아래 "갈리는 것") · [[credential-injection-outside-sandbox]]

## 4. 복잡한 장기 작업을 함께하라 (28:27~49:16)

### 밤새 돌린 과제 셋(+하나)

| 과제 | 성격 | 시간(화자) |
|---|---|---|
| 400명 행사용 **라이브 Q&A 사이트**(관리자·참가자·무대 뷰, AI 태그, moderation API) | 그린필드 | *"15 hours, 30 minutes, and 55 seconds"* (29:08~29:11), 원격 인스턴스 |
| 오픈소스 **폼 빌더**를 Sites용 사내 도구로 개조(*"I don't want to spend money on SAS[=SaaS]"* 40:50~40:52) | 기존 저장소 개조 | *"5 hours and 57 seconds"* (30:58~31:00) |
| 대학원 시절 논문(Julia·R)을 **Rust 백엔드 Python 패키지**로 재구현, *"I don't want to use dynamic programming you got to use like some heruristics"*(31:46~31:51) | 연구 코드 이식 | *"7 hours 1 minute and 40 seconds"* (31:29~31:33) |
| (넷째) App Server 위 자체 UI **Retrodex** | §6 | 미발화 |

⚠️ 42:14~42:17엔 *"the other one is like 12 hours"* — 어느 과제인지 불명.

프롬프트에 대해: *"one misconception (…) does prompt engineering matter? In so far as the instructions are clear, it still matters (…) But it's prompt engineering where you see as oh I got to use this magic phrase. I don't think we're in that state anymore. Reasoning models are really intelligent and (…) the real thing is about context."*(29:59~30:22) 그리고 그 프롬프트 자체를 휴대폰에서 *"yapping"* 하고 Codex에게 다듬게 했다(30:25~30:33).

### 장치들

1. ⭐ **goal + goals.md + 진행 대시보드** — OpenAI skills 저장소의 *"define goal"* 스킬로 *"don't create one goal create a series of goals and put it in a goals.mmuckdown[=goals.md] file"*, 그리고 *"progress dashboard.html"*(32:05~32:26). 이유: *"in this seven hours, you don't really know what's going on"*(32:26~32:30). 대시보드는 마일스톤(완료·진행·대기)과 **스레드별 역할**(오케스트레이터·커뮤니케이션·visual UX·app server protocol)과 작업 흐름(auth·testing·UI polish)을 보여 줬다(38:34~39:05). → [[verifiable-goals]]
2. ⭐ **목표 감사(goal audit) 스레드** — 메인 스레드가 마일스톤마다 코드 리뷰와 *"goal audit"* 를 별도 스레드로 띄우고, 이탈하면 *"it will nudge back the main thread. Hey remember this or do we need to rethink the plan"*(32:45~33:04). → [[generator-evaluator-pattern]]
3. ⭐ **원격 스레드 → 로컬 스레드** — 원격 세션엔 사용자의 Chrome이 없으니 *"you can spawn a local thread on my machine and use the Chrome extension to then inspect it"*(33:21~33:25), 로컬 스레드가 QA 후 결과를 원격 스레드로 돌려보낸다(33:33~33:44). *"while it's working in the cloud locally on my laptop like me at 3:00 a.m. while sleeping Codex opened Chrome it went through the form building flow"*(36:54~37:03). → [[agent-visual-qa]] · [[cloud-agent-delegation]]
4. **Slack으로 보고받기** — Slack 플러그인으로 *"give me like a summary of what's done, what's not yet done, and are there any blockers?"*(34:11~34:16). 일요일에 친구들과 나가서 *"is there anything I can help unblock Codex"*(34:24~34:29). → [[human-as-async-api]]
5. **side thread(`/side`)** — 메인 스레드를 멈추지 않고 옆에서 묻는다: *"what you've done so far (…) what do you plan to do next is there anything I can do to unblock you"*(35:29~35:37), 방향이 틀리면 거기서 고쳐 메인으로 전달. ⚠️ Charlie: *"Those are ephemeral. So if there is any context that you want to keep longterm in your project, make sure you're communicating that back to the main thread"*(35:53~36:02).
6. **막힘(blocked) 처리** — Convex·Vercel 인증이 없어 *"I marked it as blocked because the critical path"* 이되 *"it still like did everything it could up till that point"*(39:13~39:25). 아침에 side chat으로 *"explain step by step what I can do to unblock you"* → Vercel은 CLI 로그인 흐름, Convex 배포 키는 *"I'm not going to paste that into the chat. So I asked Codex give me a secure way"* → 붙여 넣을 bash 코드(39:42~40:25). → [[credential-injection-outside-sandbox]]
7. **서브에이전트에게 메시지** — 사용자가 *"not very good"* 과 스크린샷을 메인에 보내자 메인이 이미 떠 있던 서브에이전트에 *"update your verification task with this new user screenshot and directive"* 를 보냈고(37:24~37:48), Codex가 스스로 QA해 피드백을 확인했다(37:53~38:08).

### compaction (42:09~43:08)

*"In November 19 when we released GPT 5.1 Codeex Max (…) we natively train the model on multiple uh context windows through a process called compaction."*(42:21~42:35) ⚠️ 연도 미발화(ko·`en`의 "2019"는 오류), **당사자 진술**. 사용자 트윗 둘: *"did open Aai basically solve compaction I pretty much never had issue with 5.5 and codecs across ultra long threads spanning many compactions"*(42:42~42:51), 일본 사용자 *"it only remembers the good stuff. There's some token efficiency to that"*(43:01~43:05). → [[context-resets-and-compaction]]

### goal (Charlie, 43:17~44:43)

- ⭐ *"be really specific with the criteria (…) you want that criteria to be as verifiable as possible."*(43:32~43:43)
- ⭐ *"goal is is kind of like a genie in the sense that when it works well, it is insanely magical. uh and when it doesn't sometimes I feel like I've entered into a monkeykey's paw type situation where you know it has done the thing technically that I asked it to do but like very much not in the way that I was expecting."*(43:45~43:59) → [[reward-hacking]]의 사용자 쪽 표현
- 동작: *"it'll keep evaluating itself against the success criteria (…) at each turn it'll check hey did this actually complete um and if not should I keep going"*(44:02~44:13).
- 용도: 코드 마이그레이션, 대규모 리팩터링, 재시도 루프, 실험, 게임, *"full oneshotting apps with fairly detailed specs"*(44:31~44:41). 사례: Tama의 `/goal` 40시간 Doom → Swift 재구현(44:18~44:28, ⚠️ 트윗).

### 서브에이전트 vs 스레드 간 핸드오프 (44:45~47:34) → [[subagent-vs-thread-handoff]]

- 서브에이전트는 *"by default will get used out of the box"*(44:49~44:52), 이름·프롬프트·모델(가볍게/똑똑하게)을 별도 `.toml`로 지정(45:00~45:31, *"sub aents.totml"* 판독 미확정).
- 스레드 간 핸드오프는 *"quite new. I think we just released it in the last week. Two, three weeks"*(45:36~45:42) — *"an even higher level of abstraction"*.
- ⭐ 기준: *"when the the delegation of work needs to be visible to you, the user versus when it just needs to be visible to the model."*(45:49~45:59) 서브에이전트 = 하청(*"I don't really care what they're talking about. I just want to make sure that the work comes back good"* 46:08~46:13), 컨텍스트 분리. 핸드오프 = *"when you still want to be in the loop (…) you are mentally thinking about separating these two"*(46:34~46:42).
- 사례: Charlie의 게임 — **creative director 스레드**와 아트·음악·애니메이션·메커니즘 스레드, AGENTS.md에 *"Go check with the creative director and get sign off before you consider this task done"*(47:21~47:27).

### hooks (47:38~50:01)

- 위치: *"in your config.toml file uh in your codeex home directory"*(47:44~47:49). 용도: *"introducing uh deterministic behavior at specific checkpoints"*(47:50~47:55) — 대화를 로깅 엔진으로, 입출력 스캔, API 키 유출 검사, 도구 허용 목록 확인, 턴이 끝날 때 맞춤 검증(48:00~48:50).
- ⭐ AGENTS.md로 린터를 시키는 것과의 구분: *"it's really good about doing that, but if there are things that are a little bit more sophisticated (…) you can use hooks"*(48:43~48:51).
- Gabriel: Agents SDK 저장소의 훅이 턴마다 정리용 Python 스크립트를 돈다 — *"some of these housekeeping that maybe you want a language model to do you can run it deterministically with a hook"*(49:35~49:48). ⭐ *"you're giving the agent more autonomy it's going to work off work longer and longer without your supervision (…) hooks become useful in getting the guardrail."*(49:52~50:01)
- Charlie: *"you want to give the model as many boundaries as it can as you can and let it fill in the lines"*(49:02~49:09).

→ [[hook-enforced-workflow]] · [[hard-vs-soft-enforcement]]

## 5. 시간에 걸쳐 일하게 하라 — 두 종류의 자동화 (50:03~58:15)

| 종류 | 사는 곳 | 사례 |
|---|---|---|
| ⭐ **heartbeat** (in-thread) | 한 스레드 안, 타이머로 반복 *"until they're they're done"*(57:03~57:10). Charlie: *"the more powerful one these days"* | DigitalOcean 플러그인(*"just uh released last week"* 50:50~50:52)으로 droplet 프로비저닝 → *"I set a codex heartbeat to resume this track in about five minutes"*(51:27~51:31) → 준비되면 SSH 설정 딥링크. 이벤트 기반 배포 파이프라인 폴링(52:03~52:17). 발표 슬라이드를 5분마다 찍어 *"to what extent are we going to overrun"* 추정(55:21~55:47). Charlie: Slack·이메일·Linear를 훑어 **로컬 Obsidian vault**의 일일 노트·작업 흐름 노트 갱신(57:19~57:51) |
| **scheduled** (새 스레드) | Codex 앱 *"scheduled page"* 에서 매번 새 스레드로(57:53~58:00) | 직속 부하들의 주간 요약, 분석 일회성 검토 후 아카이브(58:02~58:15) |

⭐ 데모 ⑤ — Slack 피드백 → PR: 번역 앱 채널의 피드백(*"a bunch of users all called Gabriel"* 52:42~52:47)을 30분마다 칭찬·버그·기능 요청으로 분류해 답하고, 보내고 나서 **중간에 방향을 틀어**(*"I don't have to wait for codeex to finish. I can sort of steer it midway"* 54:16~54:20) 버그·기능 요청이면 *"spin a new thread in a work tree and actually address that and then open a PR and then like request Dom to review it (…) within like 24 hours. If not, just keep reminding him"*(53:55~54:09). *"imagine then you wake up and this is a bit like that software factory where all the PRs are ready"*(54:40~54:45) → [[software-factory]]

Gabriel의 자동화 두 개(56:06~56:43): ① **매주 금요일 대화 스레드를 훑어** *"are there skills that you could improve? (…) things you could add to the agents markdown or are there skills you could just remove?"* ② 이메일 초안 자동화 옆에 **두 번째 자동화**를 두고 *"cross validates against the eventual reply you send because that is the ground truth"* → 마크다운 모범 사례 파일 갱신 → *"the email drafting automation can get better over time"*. → [[skill-self-improvement]] · [[scheduled-agent-automations]]

## 6. 어디에나 넣어라 — App Server (58:18~1:01:50)

- ⭐ *"the app server protocol (…) the core protocol that underpins the Codex app, the Codex CLI, uh, the Codex VS code extension"*(58:25~58:37) — 도구 호출·플러그인·compaction을 하네스와 잇는다(58:42~58:48).
- ⭐ *"it brings the ability for your users to uh use their chat GBT subscription and perhaps more importantly use their Chat GBT token budget uh to power the products that you're building."*(59:12~59:20) → [[bring-your-own-subscription]] (⚠️ 녹화 6월 — DevDay 발표보다 앞선 서술)
- 같은 기능(compaction, steering)이 있되 *"the ones that need to live on your computer like computer use are, you know, not going to be there"*(59:26~59:31).
- 데모: Gabriel이 밤새 만든 **Retrodex** — 모델(*"5.5 5.4 mini"* 1:00:02)·추론 노력 선택(낮음은 반짝임, 높음은 더 요란하게), 같은 App Server라 Codex 앱의 같은 프로젝트에 스레드가 보인다(59:39~1:00:46). 쓰임: 여러 에이전트 공급자를 묶는 *"unified layer"*(1:00:54~1:01:05).
- 오픈소스: *"git clone openi/codex, you can just ask Codex about Codex"*(1:01:09~1:01:15). Windows 샌드박스(*"first of its kind"*)·에이전트 루프 엔지니어링 블로그 언급(1:01:31~1:01:36).

→ [[harness-as-platform]]

## 7. 마무리 — 질문의 사다리 (Charlie, 1:01:54~1:04:21)

1. *"have I tried asking Codex to do it?"* — 사무실에서 *"more frequently than ever now is, have you asked Codex?"*(1:02:12~1:02:20)
2. 개별 턴에서 **루프**로 — *"We've all heard about loop maxing. That is the new thing."*(1:02:28~1:02:31), *"what is it that the loop needs to be checking at each turn"*(1:02:34~1:02:38) → [[loop-is-the-product]]
3. *"what blocked Codeex from actually getting to the answer (…) was there context that it needed? Were there permissions that it needed? Are there ways to build that context into repeatable tools like skills or plugins"*(1:02:44~1:02:58)
4. *"how do I start scaling kind of from one agent to many?"*(1:02:58~1:03:02) — 암묵적 위임, 여러 스레드 조율
5. ⭐ *"why does this process need a human at all"*(1:03:18~1:03:23) — API 키를 사람이 받아 붙여 넣던 일을 developers plugin이 한다. *"we do still want humans in the loop like where they need to be but uh for everything that's not that like how do we figure out how to take the human out of the process to unblock ourselves"*(1:03:44~1:03:55) → [[human-plumbing]]
6. ⭐ *"it is one thing to sit with a coding agent and build a single piece of software is another thing to start zooming out and say actually I want to build a software factory right I want to build a system that um that then builds individual pieces of software on an assembly line"*(1:03:57~1:04:14) → [[software-factory]]

이후 일정 안내(내일 기조연설, Jason의 Codex 활용 발표·워크숍, Dom의 *"building on the Codex harness"*, 하네스 해설, 음성 에이전트, LLM 추론 세션, 1:04:40~1:05:40)와 **Codex 크레딧 100달러 + API 크레딧 100달러**(1:06:03~1:06:06).

## 이 위키와의 연결

### 이어지는 것

- **[[codex]]** — 지금까지 Codex 페이지는 *외부에서 본 행동*(지속성·scratchpad·compaction 잦음, 스킬 배포자의 하네스 관찰)이었다. 이 소스는 **제품 표면의 목록을 만든 쪽이 직접** 준다: appshot · record & replay · thread handoff · Remote · plugins · memories/Chronicle · Sites · `/code review` · computer use/Chrome/in-app browser · goal · subagents · side thread · hooks · heartbeat/scheduled automations · App Server.
- **[[verifiable-goals]]** — Karpathy 원칙(*"Define success criteria. Loop until verified"*)이 **제품 기능 `/goal`** 이 됐다. *"genie / monkey's paw"* 는 검증 기준이 약할 때의 실패를 사용자 언어로 말한다.
- **[[scheduled-agent-automations]]** — Cursor의 automations(예약·이벤트·메시지)에 **heartbeat = 스레드 안 폴링** 이라는 형태가 붙는다. Brockman이 말한 *"48시간 뒤 DMARC 완료를 위한 자동화를 스스로 예약"*([[tech-bridge-brockman-agi-era-defender-window]])의 제품 쪽 이름으로 읽힌다(위키의 독해 — 같은 기능이라는 발화는 없다).
- **[[hook-enforced-workflow]]** — 이 위키의 훅 사례(Graft, Impeccable, Rails)에 **하네스 제작사의 권고**가 붙는다: 자율이 길어질수록 훅이 가드레일.
- **[[skill-self-improvement]]** — 여덟 번째 경로 후보: **실제로 보낸 답장(ground truth)과 초안을 대조하는 두 번째 자동화.**
- **[[context-resets-and-compaction]]** — compaction을 *하네스 기능*이 아니라 **모델 학습 대상**(*"natively train"*)으로 놓는 첫 당사자 서술.
- **[[agent-manager-analogy]]** — *"everyone's become a manager"*(10:30), 그리고 워크숍 전체가 **주방 비유**(셰프·수셰프·맛보기) — [[lauren-tan|Lauren Tan]]의 미슐랭 주방과 같은 그림.
- **[[software-factory]]** — 하네스 제작사 직원이 *"machine that builds the machine"* · *"software factory … assembly line"* 을 목표로 놓는다. Factory·Warp의 정의 옆에 **세 번째 화자**.
- **[[tech-bridge-conductor-orchestras-not-factories]]** · **[[tech-bridge-agents-vs-humans-optimizer-speedrun]]** — 거기서 미해결이던 *"slashgo"*·`/goal` 의 정체: 이 소스에서 **Codex에 goal 기능이 있음**이 확인된다(*"I'm running a goal"* 29:06, *"SLGO"* 44:22). ⚠️ 그 화자들이 Codex를 가리켰는지는 여전히 미확정.

### 갈리는 것

> ⚠️ **Contradiction: Codex는 서브에이전트를 스스로 쓰는가.** [[paul-bakaus|Paul Bakaus]]([[tech-bridge-skill-engineering-dark-arts]], 시점 미확정): Codex는 **서브에이전트를 사용자가 명시적으로 요청해야 쓴다** — *"if you're distributing a skill, you're out of luck"*. Charlie(2026-06-29): *"sub aents in codeex um you know by default will get used out of the box"*(44:49~44:52), *"the model is great at figuring out when it should be um handing off into sub agents"*(46:13~46:16). 시점 차이(버전 변화)일 수도, 스킬 배포 맥락과 대화 맥락의 차이일 수도 있다. 이 위키는 판정하지 않는다.

> ⚠️ **Contradiction(약): 스킬은 반창고인가 정답인가.** [[sarah-simionescu|Simionescu]]([[tech-bridge-composio-dashboard-is-dead]]): *"skills is just a band-aid because agents become dumber with the more context you provide"*. 이 소스: 어려운 대화의 끝은 *"make this a skill or even better make this a plugin"*(12:41~12:48), 그리고 매주 스킬을 **정리·삭제**하는 자동화(56:06~56:20). 후자는 전자의 비용(컨텍스트 증가)을 **가지치기**로 관리하는 쪽이다 → [[harness-pruning]].

> ⚠️ **컴퓨터 사용 vs 에이전트 전용 인터페이스 — 세 번째 입장.** [[agent-native-interface]]에 기록된 Brockman(사람 화면으로 가는 컴퓨터 사용) vs Simionescu(에이전트 전용 층) 대립에, Charlie는 **용도별 분업**을 놓는다: 컴퓨터 사용은 *"applications that otherwise don't have a programmatic interface"*(27:09~27:13)에서 빛나고, API를 역공학할 수 있으면 그게 낫다(*"it's great if it's a web app and you can reverse engineer the API calls"* 27:13~27:17). 목적지 논쟁이 아니라 **폴백 순서**로 읽힌다(위키의 독해).

> ⚠️ **"마법 주문" 프롬프트는 끝났나.** Gabriel: *"oh I got to use this magic phrase. I don't think we're in that state anymore"*(30:14~30:17). 같은 위키의 Bakaus 관찰 — **Codex/GPT는 "gate"라는 단어를 좋아한다**, Codex 전용 8-gate MD([[cross-harness-skill-compilation]]) — 은 모델별 어휘가 여전히 결과를 바꾼다는 쪽이다. 화자는 *명확성*을, Bakaus는 *모델 버릇*을 말하므로 완전한 충돌은 아니다.

## 해소하지 않고 표시만 한 것

- 장기 과제의 *"12 hours"*(42:16)가 어느 것인지, 폼 빌더 팀 규모 7명 vs 5명.
- 서브에이전트 설정 파일 이름(*"sub aents.totml"*), side thread 명령 이름(*"slash site"* → `/side` 판독).
- *"In November 19"* — 연도 미발화(위키 밖 지식으로 채우지 않는다).
- *"codex mixing"*(02:25, 03:08), *"pretty quoted"*(43:08), *"send retroex visible okay"*(38:03).
- 트윗 사례의 출처·작성자(Tama 등), 동료 Dom·Jason·Christine·Brent·Cory의 성.
- 번역 앱 라이브 시연의 실제 출력.

## 등장 개체

- 인물: [[charlie-guo]] (신규) · [[gabriel-chua]] (신규) · 동료(페이지 없음): Christine · Dom · Jason · Brent · Cory(⚠️ [[cory-dolphin]]과 동일인 근거 없음)
- 조직: [[openai]] · [[ai-engineer]] · [[vercel]](배포 대상) · DigitalOcean · Convex(페이지 없음)
- 제품: [[codex]] (Codex app · CLI · VS Code 확장 · Remote · App Server · Sites · Chronicle · plugins) · OpenAI Agents SDK · GPT realtime translate · GPT-5.1-Codex-Max · GPT-5.5 · GPT-5.4 mini · [[obsidian]] · Slack · Gmail · Linear · Ableton · Premiere(페이지 없음)
- 개념: [[subagent-vs-thread-handoff]] (신규) · [[verifiable-goals]] · [[scheduled-agent-automations]] · [[hook-enforced-workflow]] · [[context-resets-and-compaction]] · [[skill-self-improvement]] · [[bring-your-own-subscription]] · [[software-factory]] · [[loop-is-the-product]] · [[agent-native-interface]] · [[agent-manager-analogy]] · [[cloud-agent-delegation]] · [[agent-visual-qa]] · [[agent-memory]] · [[human-plumbing]] · [[harness-as-platform]] · [[agent-skills]] · [[automated-code-review]] · [[generator-evaluator-pattern]] · [[credential-injection-outside-sandbox]] · [[human-as-async-api]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=RVnSsolR3uE> (1:07:05, `upload_date` 2026-10-10 = 공개 전환 값, 2026-10-06 멤버 전용 첫 확인)
- raw: `01.raw/articles/2026-10-10_Codex로 요리하기 — OpenAI의 Charlie Guo와 Gabriel Chua.md`
- 설명란 링크: <https://x.com/charlierguo> · <https://www.linkedin.com/in/charlierguo> · <https://www.ignorance.ai/> · <https://x.com/gabrielchua> · <https://github.com/gabrielchua> · <https://gabrielchua.me/> · <https://github.com/openai/codex> (⚠️ 열어 보지 않았다)
- 같은 제품의 다른 시선: [[tech-bridge-altman-devday-dots]] · [[tech-bridge-skill-engineering-dark-arts]] · [[tech-bridge-agents-vs-humans-optimizer-speedrun]] · [[tech-bridge-brockman-agi-era-defender-window]] · [[tech-bridge-death-of-code-review]]
- [[tech-bridge]] · [[openai]] · [[codex]] · [[charlie-guo]] · [[gabriel-chua]]
