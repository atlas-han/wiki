---
title: "Tech Bridge — 엉성한 원샷 SaaS 대체품은 이제 그만 (Railway 사내 마케팅 도구): 돌아가는 소프트웨어와 매일 쓰고 싶은 소프트웨어 사이의 격차, 에이전트가 묻지 않으면 안 하는 패턴, 그리고 end-to-end 검증 루프"
type: source
tags: [internal-tools, saas-replacement, one-shot, product-polish, ux-patterns, autosave, optimistic-updates, undo, archiving, url-state, infinite-scroll, codebase-abstractions, reference-pages, agent-skills, verification-loop, computer-use, railway, vendor-mention, video]
source-url: https://www.youtube.com/watch?v=3jtlfKL-N4A
source-type: video
author: Tech Bridge (한영자막 재배포) · 화자 Railway 직원(발화) — 이름 Mahmoud Abdelwahab은 ⚠️ **설명란 링크 slug에서만 *추정***(자막·설명란 본문 모두 이름 없음) · 행사 없음(혼자 찍은 야외 영상) · 녹화 시점 발화 "fall 2026. It's October."
date-published: 2026-10-18
ingested: 2026-10-19
created: 2026-10-19
updated: 2026-10-19
---

# Tech Bridge — 엉성한 원샷 SaaS 대체품은 이제 그만 (Railway 사내 마케팅 도구)

[[tech-bridge|Tech Bridge]]가 재배포한 **13:21 단독 영상 발표**다. 무대·청중·Q&A는 없다. 화자는 에든버러의 야외 벤치에서 찍었다고 말한다(*"Right now, I'm in Edinburgh, Scotland."* 01:38~01:41). 공식 챕터는 `meta.txt` 기준 8개다. 화자는 [[railway|Railway]]에서 사내 마케팅용 SaaS 여러 개를 에이전트로 만든 올인원 도구 하나로 바꾼 경험을 말한다. ⚠️ **화자는 이름을 말하지 않고 설명란 본문에도 이름이 없다.** 이름 [[mahmoud-abdelwahab|Mahmoud Abdelwahab]]은 설명란 링크 두 개(`linkedin.com/in/thisismahmoud`, `github.com/m-abdelwahab`)에서 **추정**한 것이다. 소속은 발화된다(00:31, 11:25). 발표는 **도구 소개 + 코드베이스 추상화 + "에이전트가 묻지 않으면 안 하는" 패턴 목록 + 참고 페이지 + 스킬 + 검증 루프**로 이루어진다. 테제는 다음과 같다.

> **"SaaS는 죽었다, 에이전트에게 시키면 된다"에서 빠진 조각은 원샷으로 돌아가는 소프트웨어와 매일 쓰고 싶은 다듬어진 소프트웨어 사이의 큰 격차다. 그 격차는 에이전트가 못 해서가 아니라 시키지 않아서 생긴다. 견고한 추상화가 있는 코드베이스를 주면 에이전트는 기존 패턴을 따른다. 자동 저장·낙관적 업데이트·삭제 취소·보관·URL 상태·무한 스크롤은 명시적으로 요청해야 한다. 좋은 페이지를 한 번 정의해 참고로 지정하고, 의견은 agent skill로 포장하며, 마지막으로 가장 중요한 단계는 실제 인프라에서 기능을 끝까지 써 보는 검증 루프다.**

> *"there's a gap, a big gap, between working software that got one-shotted and software I would actually use, software that sparks joy, that is polished, that feels good."* (00:16~00:25) · *"there are kind of like a bunch of patterns that I found that Asians[=agents] don't typically do unless you explicitly ask them to."* (04:46~04:54) · *"It's not difficult for the agent to build it. You just need to ask and know exactly what to ask for."* (07:14~07:20) · *"the final step and I think this is the most important step is verification."* (11:47~11:52)

이 위키에 개념 하나가 생긴다([[product-polish-patterns]]).
- [[product-polish-patterns]]: 에이전트가 원샷으로는 넣지 않는 일상 사용 UX 패턴 목록(자동 저장 + 탭 닫기 방지, 실시간 협업, 낙관적 업데이트, 삭제 취소, 보관, URL 상태, 무한 스크롤)과 "요청하면 어렵지 않다"는 진단. 위키의 슬롭·원샷 논의는 디자인(타이포·색)과 코드 품질 쪽이었고, **상호작용 흐름**을 다룬 페이지가 없었다.

나머지는 기존 페이지에 붙는 **새 증언**이다.
- [[codebase-gardening]]: *"The agent doesn't need to reinvent the same like wheel (…) It will just essentially follow existing patterns."*(03:06~03:18) — "안티패턴은 바이러스처럼 퍼진다"의 **좋은 쪽 판본**
- [[design-system-as-agent-context]]: 기존 페이지를 참고로 지정해 *"define what good looks like once and then just reuse it"*(09:52~09:58) — 디자인 시스템 대신 **살아 있는 페이지**가 기준이 된다
- [[agent-skills]]: *"whenever you have opinions about something, they should be packaged as agent skills"*(10:45~10:48), 디자인 엔지니어링 스킬 둘 + 벤더 스킬(Railway)
- [[agent-verification-skill]]·[[agent-visual-qa]]: *"build pass, test pass, all good, right?"*(11:59) 뒤의 깨진 경험, 검증 루프의 *"night and day difference"*(12:14), 돌파 원인은 computer use(12:25~12:30)
- [[syntactically-correct-behaviorally-wrong]]: 빌드·테스트 통과와 실제 동작의 차이를 UI 쪽에서
- [[no-one-shot-design]]: 원샷 vs 다듬기를 **사내 도구**에 건다
- [[smarter-software-vs-cheaper-software]]: *"SaaS is dead"*로 시작해 *"become your company's SAS[=SaaS] layer"*(13:14~13:16)로 끝난다

ASR·ko 보정. ko는 **회사명 Railway를 내내 "철도"로 옮기고**(*"철도는 철도에서 운행됩니다"* 11:25), 도구가 Railway 위에서 돈다는 문장을 **"이 모든 것은 GPT-6를 기반으로 작동합니다"**(01:08)로 바꾼다. 요구도 뒤집힌다: *non-blocking action* → **"차단 기능입니다 … 타이핑하는 동안에는 차단됩니다"**(05:18~05:20), *it shouldn't feel that way* → **"그렇게 느껴야 마땅해요"**(04:44). 없는 수치가 생긴다: 지연 삭제 설명에 **"2초 안에"**(08:10). 검증 루프의 돌파 원인 *computer use*는 **"컴퓨터를 한 번 사용하면서"**(12:27, `en` 공유)가 되어 능력 이름이 사라진다. optimistic update는 "긍정적인 소식"(06:21), loading spinner는 "충전 표시등"(06:25), *tech stacks*는 "기술적인 배터리"(02:29, `en` 공유), infinite scroll은 "무한 변위"(09:14)다. en-orig는 agents를 *"Asians"*(04:48)로, SaaS를 *"SAS"*(13:16)로 적는다. 웹 라이브러리 선호 *"one tech stack libraries"*(03:28)는 TanStack으로 읽었다(⚠️ 판독). 전체 목록은 raw에 있다.

> ⚠️ **화자 이름은 추정이다.** 자막에 자기소개가 없고(*"let me (…) walk you through the principles I used"* 01:12~01:19 뒤로도 이름 없음), 설명란 본문도 *"Railway의 내부 마케팅 도구를 만들며 배운 …"*뿐이다. Mahmoud Abdelwahab은 링크 slug `thisismahmoud`·`m-abdelwahab`에서 나왔다. 링크는 열어 보지 않았다. 직함도 발화되지 않는다.
>
> ⚠️ **자사 제품이 섞인다.** *"all of this is running on Railway. Everything just auto-deploys"*(01:10~01:14), *"last but not least is the Railway agent skills, of course"*(11:18~11:21), *"everything that I built for us internally at Railway runs on Railway, of course. Like everything. So, like buckets, databases, the app itself, the server, everything."*(11:21~11:32). 다른 배포 플랫폼과의 비교는 없다.
>
> ⚠️ **측정이 없다.** 수치는 실시간 협업에 든 *"700 million tokens"*(06:07~06:09) 하나다. 모델·비용·기간은 발화되지 않는다. 대체한 SaaS의 이름·개수·절감액, 도구 사용자 수, 개발 기간, 패턴별 효과는 모두 없다. *"my success rate is higher whenever I tell the agent to (…) use an existing page as a reference"*(10:13~10:19)도 수치가 없다.
>
> ⚠️ **녹화 시점은 발화되지만 일반화는 화자가 먼저 유보한다.** *"anything I say might change completely in like the span of months. Who knows? (…) Consider this my disclaimer. Like but the time of recording is fall 2026. It's October."*(02:07~02:22)

## 1. 도입 — SaaS는 죽었다, 그런데 (00:00~02:23)

- *"People have been saying that SaaS is dead for a while now. It's not even a hot take at this point. Why pay someone to build and maintain the tools you use when you could just do it yourself? Just ask your agent to do it."*(00:00~00:10)
- ⭐ *"there's one missing piece that rarely gets mentioned, and it's the fact that there's a gap, a big gap, between working software that got one-shotted and software I would actually use, software that sparks joy, that is polished, that feels good."*(00:12~00:25)
- 만든 것: *"replace a bunch of SaaS providers we were using internally at Railway for marketing purposes, and I just built an all-in-one tool"*(00:27~00:35). 기능은 웹사이트·changelog·블로그 콘텐츠 관리, 이메일 발송, 모든 소셜 플랫폼 동시 게시, 웹사이트 미디어 관리, 외부 크리에이터용 *"mini CRM"*, 작업 추적, 출시 계획, 캘린더, 댓글, 실시간 편집이다(00:35~01:04). *"it's all built using agents."*(01:01~01:04)
- *"I would say I felt the breakthrough when GPT-6 came out"*(01:04~01:10). ⚠️ GPT-6의 등급·용도는 더 말하지 않는다. → [[openai-astra]](위키의 미해결 *Astra ↔ GPT-6*에 이 발화를 근거로 쓰지 않는다)
- 목표: 기능을 더할 때 *"actually polished and matches the rest of the app"*(01:22~01:24)이 되게 하는 원칙, 그리고 듣는 사람이 자기 도구에 쓸 원칙(01:27~01:32).

→ [[smarter-software-vs-cheaper-software]] · [[no-one-shot-design]] · [[railway]](신규)

## 2. 스택은 덜 중요하다, 추상화는 중요하다 (02:26~03:59)

- 첫 원칙의 제목은 *"tech stacks don't matter"*(02:28~02:31)다. 화자는 *"while I agree to some extent"*(02:40~02:42)로 받는다.
- ⭐ *"when you give the agent a proper code base with solid abstractions, what ends up happening is whenever you're working, let's say, on a new feature, you end up with a much more consistent result that is similar to what you've already built before."*(02:48~03:02)
- 이유: *"The agent doesn't need to reinvent the same like wheel every time it tries to add a new feature or it doesn't need to introduce new patterns. It will just essentially follow existing patterns."*(03:06~03:18)
- 선호: *"my go-to choice today is one tech stack[=TanStack?] libraries for anything when building on the web"*(03:27~03:34), 콘텐츠라면 *"definitely go with Payload. Solid experience, great abstraction."*(03:34~03:40) CMS를 비교하다 *"I don't believe that I should uh build it from scratch, even though I can."*(03:44~03:49) ⚠️ TanStack은 위키의 판독이다.

→ [[codebase-gardening]](코드베이스는 기억이다 — 에이전트는 있는 패턴을 따른다) · [[llm-coding-guidelines]]

## 3. 쓸 때는 안 보이는 것 — 에이전트가 묻지 않으면 안 하는 패턴 (04:03~09:33)

- *"When you use like a lot of SaaS products out there that you actually love that you use every day, when you're a user, there's like a lot of things you don't notice. But, when you actually try to like replicate an experience, you quickly find out how much care and thought goes into different flows."*(04:03~04:20)
- 이메일 발송·게시 같은 기능은 *"server-side rendered app with like forms that you submit"*로 쉽게 되지만, 매일 쓸 것이라면 *"Oh, it shouldn't feel that way."*(04:29~04:45)
- ⭐ *"there are kind of like a bunch of patterns that I found that Asians[=agents] don't typically do unless you explicitly ask them to. And this is my list."*(04:46~04:57)

| 패턴 | 발화 | 화자의 단서 |
|---|---|---|
| **자동 저장** | *"auto save is kind of like a table stakes feature"*(05:03~05:08). 백그라운드에서, *"a non-blocking action"*(05:18~05:23) | 문서 편집기라면 |
| **미저장 탭 닫기 방지** | *"prevent the browser tab from closing if there are unsaved changes"*(05:34~05:39). 자동 저장과 함께 *"these two layers that kind of guarantee that whatever it is that you're working on is you just not going to be lost"*(05:39~05:46) | |
| **실시간 협업** | *"add like real-time collaboration so that you can have like concurrent edits"*(05:51~05:55). *"my agent didn't struggle at all (…) asking about it, reviewing how it would work, and then once that's done, just 700 million tokens later and I had real time."*(05:56~06:09) | ⚠️ 토큰 수 외 수치 없음 |
| **낙관적 업데이트** | 로딩 스피너 대신 *"show them the success state (…) optimistically, and in the background you're going to sync"*(06:25~06:33), 실패하면 *"roll it back"*(06:38~06:40) | *"you shouldn't blindly have optimistic updates for everything"*(06:43~06:46). 프롬프트 예: *"I would like to implement optimistic updates where it makes sense. Let's come up with a plan."*(07:08~07:11) |
| **삭제 취소** | 버튼 → 확인 대화상자 → 삭제가 에이전트의 기본값(07:29~07:40). 더 나은 것은 UI에서 바로 지우고 *"you have like a couple of seconds where you could change your mind"*(07:54~07:58), 아무것도 안 하면 그때 실제로 삭제. *"It's just kind of a delayed action"*(08:12~08:16) | 낙관적 업데이트의 확장(07:22~07:26) |
| **보관/보관 해제** | *"you shouldn't force your user to be like, 'Well, if you don't want to see this, you have to delete it.'"*(08:32~08:37) | UI·검색 결과에서 숨기기(08:25~08:32) |
| **URL 상태** | *"persist data in the URL whenever it makes sense"*(08:48~08:51). 필터·정렬 조건을 URL에 두면 *"another team member is just going to be able to see exactly what you want them to see"*(09:07~09:11) | |
| **무한 스크롤** | *"I don't want to be clicking on load more over and over"*(09:14~09:19), 끝에서 *"Oh, I've reached the end."*(09:26~09:28) | *"It's a very minor thing, but also when you use something every day, I think it makes a huge difference."*(09:28~09:33) |

- 진단은 능력이 아니라 요청이다: ⭐ *"Again, it's like it's not difficult for the agent to build it. You just need to ask and know exactly what to ask for."*(07:14~07:20) 앞 절에서도 *"this is the first thing that I find agents just don't do well from a product experience perspective"*(06:09~06:16)라고 했다.
- ⚠️ 목록은 화자의 경험에서 나온 것이고 어떤 에이전트·모델에서 관찰했는지 말하지 않는다.

→ [[product-polish-patterns]](신규) · [[action-reversibility]](삭제 취소·보관 = 되돌릴 수 있는 행동) · [[ai-slop]]

## 4. 참고 페이지 — "좋은 것"을 한 번 정의한다 (09:33~10:44)

- ⭐ *"telling the agent explicitly to use existing pages as references. When it comes to the UI, the data fetching and how it works, and how the thing is overall structured, and that made it possible for me to essentially define what good looks like once and then just reuse it for more features."*(09:38~09:58)
- 한계도 말한다: *"sometimes even when you tell the agent like, 'Hey, use page X as a reference.' Sometimes it just doesn't follow it. I don't know if models like get dumber or sometimes, but sometimes it does happen."*(09:58~10:13)
- *"if two parts of the app are essentially lists of records that you can create, update, and delete, and like list, well, both of these parts should be pretty much identical."*(10:30~10:42)

→ [[design-system-as-agent-context]] · [[codebase-gardening]]

## 5. 의견은 스킬로 (10:44~11:42)

- ⭐ *"whenever you have opinions about something, they should be packaged as agent skills. And then this way, your agent, whenever it's building something, it will actually follow those skills pretty closely."*(10:45~10:56)
- 쓴 스킬 셋(10:56~11:21): ① 디자인 엔지니어링 — *"better UI, better typography, better layouts, as well as like better error messages"* ② 디자인 엔지니어링 — *"better animations and other things like that"* ③ *"the Railway agent skills, of course"*. ⚠️ ①②의 이름은 발화되지 않는다.
- *"for the agent to effectively work with Railway and be able to deploy everything, we just give it the AI agent skills and it was just able to do it."*(11:32~11:42) ⚠️ 자사 제품.

→ [[agent-skills]](벤더가 자사 플랫폼 지식을 스킬로 유통하는 사례 하나 더) · [[impeccable]](디자인 스킬 계열, 화자가 이름을 말하지 않으므로 같은 것인지는 모른다)

## 6. 검증 — 가장 중요한 마지막 단계 (11:42~12:59)

- ⭐ *"the final step and I think this is the most important step is verification. So, the agents typically, whenever you ask it to build something, it's going to be like, 'Okay, I implemented the feature, build pass, test pass, all good, right?' But what I found is when you actually try out what happens, you sometimes end up with just like a very broken experience."*(11:47~12:08)
- ⭐ *"once you have like a verification loop in place, it's like a night and day difference because the agent, you can literally see it be like, 'Okay, I built this thing. I tried it. It failed. I'm going to fix it.' And it just keeps going and then in the end it's like, 'Okay, I fully tested it.'"*(12:08~12:25)
- 돌파 원인: *"I felt this breakthrough with computer use once it got really, really good."*(12:25~12:30)
- 매번 붙이는 지시: *"you should verify that the feature works end to end and use it by actually running infrastructure and to test things end to end."*(12:36~12:44) *"the agents are very capable of doing this. You just have to tell them."*(12:44~12:49)

→ [[agent-verification-skill]] · [[agent-visual-qa]] · [[syntactically-correct-behaviorally-wrong]] · [[linear-vs-closed-loop-harness]]

## 7. 맺음 — 회사의 SaaS 층이 되라 (12:49~13:20)

- *"once you have all of those pieces, I would say you will end up with solid internal tools that you can build quickly, that work properly, and work in a consistent way."*(12:49~12:59)
- *"I hope that you too can become your company's SAS[=SaaS] layer."*(13:11~13:16)

## 이 위키와의 연결

### 이어지는 것

- **[[agent-verification-skill]]: 두 번째 실무자가 같은 순위를 매긴다.** [[lauren-tan|Lauren Tan]]은 *"the single most important skill that should be in your tool kit is verification"*이라 했고([[tech-bridge-lauren-tan-agent-dev-workflow]]), 이 화자는 *"the most important step is verification"*(11:49~11:52)이라 한다. 둘 다 **실제로 앱을 띄워 써 보는 것**을 말한다(Tan의 *"hands and eyes"*, 여기서는 computer use와 *"actually running infrastructure"*). 차이는 형식이다. Tan은 검증을 **스킬로 만든다**. 이 화자는 매 기능 끝에 **한 문장 지시**를 붙인다.
- **[[codebase-gardening]]: 같은 메커니즘의 좋은 쪽.** 그 페이지는 *코드베이스는 기억이고 안티패턴은 바이러스처럼 퍼진다*를 말한다. 이 화자는 같은 성질을 긍정적으로 쓴다: 견고한 추상화가 있으면 에이전트는 *"follow existing patterns"*(03:15~03:18)해서 결과가 일관된다. 참고 페이지 지정(4절)은 그 성질을 의도적으로 겨냥하는 방법이다.
- **[[design-system-as-agent-context]]: 정의해 두지 않은 자리에서 슬롭이 나온다는 같은 진단, 다른 재료.** [[vincent-wendy|Vincent Wendy]]는 디자인 시스템(타이포·색·간격)을 정의해 두라고 했다. 이 화자는 **작동하는 기존 페이지**를 정의로 쓴다. UI뿐 아니라 *"the data fetching and how it works"*(09:43~09:48)까지 포함한다.
- **[[no-one-shot-design]]: 원샷 vs 반복을 사내 도구에.** [[kent-beck|Kent Beck]]은 *"If I'm writing a little app, one shot is fine."*이라 했다. 이 화자는 사내 도구도 **매일 쓰는 것이면** 원샷으로는 부족하다고 한다. 기준이 크기가 아니라 **사용 빈도**다(*"when you use something every day, I think it makes a huge difference"* 09:30~09:33).
- **[[agent-skills]]: 의견의 포장.** *"whenever you have opinions about something, they should be packaged as agent skills"*는 [[impeccable]] 계열의 "스킬은 취향·어휘를 담는다"와 같은 방향이다. 벤더 스킬(Railway)은 [[tech-bridge-lopopolo-agent-harness|Google Skills]]처럼 플랫폼 회사가 자기 배포 지식을 스킬로 내놓는 사례다.

### 갈리는 것

> **[[smarter-software-vs-cheaper-software]]와의 긴장(위키 판독).** [[diogo-almeida|Almeida]]는 SaaS가 2019년 이후 거의 변하지 않았고 에이전트는 *소프트웨어를 쓰는 비용*만 낮춘다고 불평했다. 이 화자는 SaaS를 사내 도구로 바꾸고 *"become your company's SaaS layer"*를 권한다. 그런데 화자가 공들인 목록(자동 저장·낙관적 업데이트·삭제 취소·URL 상태·무한 스크롤)은 **기존 SaaS가 이미 갖춘 UX를 다시 만드는 것**이다(*"when you actually try to like replicate an experience"* 04:13~04:15). 이 발표는 Almeida의 관찰을 반박하지 않고 **사례로 뒷받침하는 쪽**에 가깝다. 만드는 사람은 바뀌었지만 만들어진 것의 성질은 같다. 화자는 이 질문을 다루지 않는다.

> **스킬은 band-aid인가.** [[agent-skills]]의 2026-10-10 절에는 *"skills is just a band-aid"*([[tech-bridge-composio-dashboard-is-dead|Composio 편]])라는 컨텍스트 비용 쪽 반론이 있다. 이 화자는 스킬 셋으로 충분했다고 하지만 컨텍스트 비용은 말하지 않는다. 같은 화자가 참고 페이지를 지정해도 *"Sometimes it just doesn't follow it"*(10:06~10:08)이라고 인정하는 것은, 지시형 컨텍스트가 강제력이 없다는 [[hard-vs-soft-enforcement]]의 soft 쪽 증언이다.

## 해소하지 않고 표시만 한 것

- 화자 이름(설명란 링크 slug에서만 추정)과 직함.
- *"one tech stack"*(03:28)의 판독(TanStack?). *"an item bench"*(01:49)의 판독.
- 디자인 엔지니어링 스킬 두 개의 이름. [[impeccable]]과 같은 계열인지.
- GPT-6가 어떤 모델·등급인지. 도구 개발에 쓴 에이전트·하네스 이름(발화 없음).
- *"700 million tokens"*의 모델·비용·기간. 대체한 SaaS의 이름·개수·절감액.
- 이 패턴 목록을 관찰한 에이전트·모델·시점. *"models like get dumber"*(10:08~10:11)가 무엇을 가리키는지.

## 등장 개체

- 인물: [[mahmoud-abdelwahab|Mahmoud Abdelwahab]](⚠️ 이름은 설명란 링크 slug에서만 *추정*)
- 조직: [[railway|Railway]](화자 소속, 도구의 실행 기반) · [[openai|OpenAI]](GPT-6, 회사명은 발화되지 않음)
- 모델·제품: GPT-6(페이지 없음, [[openai-astra]] 미해결 항목 참조) · Payload(CMS, 페이지 없음) · TanStack(⚠️ 판독, 페이지 없음) · Railway agent skills
- 개념: [[product-polish-patterns]](신규) · [[codebase-gardening]] · [[design-system-as-agent-context]] · [[agent-skills]] · [[agent-verification-skill]] · [[agent-visual-qa]] · [[syntactically-correct-behaviorally-wrong]] · [[no-one-shot-design]] · [[smarter-software-vs-cheaper-software]] · [[action-reversibility]] · [[ai-slop]] · [[llm-coding-guidelines]] · [[linear-vs-closed-loop-harness]] · [[hard-vs-soft-enforcement]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=3jtlfKL-N4A> (13:21, `upload_date` 2026-10-18)
- raw: `01.raw/articles/2026-10-18_엉성한 원샷 SaaS 대체품은 이제 그만 만드세요.md`
- 설명란 링크: <https://www.linkedin.com/in/thisismahmoud/> · <https://github.com/m-abdelwahab> (⚠️ 열어 보지 않았다)
- 검증 순위의 다른 증언: [[tech-bridge-lauren-tan-agent-dev-workflow]] · [[tech-bridge-factory-software-factory]]
- 원샷 논의: [[tech-bridge-impeccable-design-steering]] · [[tech-bridge-kent-beck-craft-augmented-development]] · [[tech-bridge-one-designer-plus-ai]]
- [[tech-bridge]] · [[mahmoud-abdelwahab]] · [[railway]]
