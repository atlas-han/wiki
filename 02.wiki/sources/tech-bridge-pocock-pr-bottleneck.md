---
title: "Tech Bridge — AI 시대에 쏟아지는 PR 병목, 어떻게 해결해야 할까요? (Matt Pocock · AI Hero): 브레이크 세 겹, 거짓말하는 테스트와 deep modules, 리뷰는 서브에이전트가 커밋으로, one-way door만 전부 리뷰"
type: source
tags: [pr-bottleneck, code-review, automated-code-review, software-factory, slop-cannon, testing, deep-modules, coding-standards, subagents, reversibility, agent-skills, retro, ai-engineer, video]
source-url: https://www.youtube.com/watch?v=8DRjkp_X8yY
source-type: video
author: Tech Bridge (한영자막 재배포) · 발표 [[matt-pocock]] (AI Hero — 이름·소속은 설명란에만, 자막엔 자기소개 없음) · 설명란상 AI Engineer Paris 2026(발화 "Thank you, Paris"), 날짜 미발화
date-published: 2026-10-05
ingested: 2026-10-09
created: 2026-10-09
updated: 2026-10-09
---

# Tech Bridge — AI 시대에 쏟아지는 PR 병목, 어떻게 해결해야 할까요? (Matt Pocock · AI Hero)

[[tech-bridge|Tech Bridge]]가 재배포한 **22:32 발표, Q&A 없음, 공식 챕터 없음.** 2026-10-01 회차부터 멤버 전용으로 대기하다 10-09에 공개 확인(`upload_date` 20261005). 화자는 설명란상 **AI Hero 창립자·TypeScript 교육자 [[matt-pocock|Matt Pocock]]** — ⚠️ **자막엔 자기소개가 없고**, 근거는 *"these are my skills. AIhero.dev/skills"*(22:14~22:16) 같은 정황뿐이다. **실무자 처방집**이다 — 측정치는 없고, 자기 스킬 저장소(AIhero.dev/skills)의 스킬 넷(코드베이스 설계 · 코드 리뷰 · PR · retro)을 축으로 *사람 리뷰를 어떻게 빠르게 만드나* 를 말한다. 일주일 전 [[tech-bridge-death-of-code-review|Laurie Voss 편]]이 *"리뷰 하네스를 지어라"* 로 끝났다면, 이 편은 **그 하네스를 한 사람이 실제로 어떻게 짰는지**에 가깝다.

> **소프트웨어 팩토리에 가속기만 달면 slop cannon이 된다 — 브레이크 세 겹(자동 검사 → 자동 리뷰 → 사람 리뷰)을 깔고, 앞의 두 겹에 기대 사람 리뷰를 빠르게 만든다. 검사는 거짓말을 하니(동어반복·구조 민감·실패할 수 없는 테스트) 코드베이스를 deep module로 설계해 거짓말하기 어렵게 하고, 코딩 표준은 과부하 걸린 구현 에이전트가 아니라 한가한 리뷰 서브에이전트에게 주며, 리뷰어는 댓글이 아니라 커밋을 남긴다. 사람은 PR이 one-way door인지 보고, 코드가 아니라 그 코드를 만든 시스템을 리뷰한다 — 같은 댓글을 두 번 쓰지 않게.**

> *"If you just have permanent acceleration pushing stuff through your factory, you're going to end up with a slop cannon"* (02:18~02:26) · *"Does a green CI mean that the code is ready for merge? No, it does not."* (04:50~04:55) · *"implementation is overloaded"* (12:19~12:21) · *"The reviewer should commit. It should make fixes."* (15:43~15:48) · *"when you do a human review, you're not just reviewing the code, you're reviewing the system that creates it"* (20:14~20:20) · *"You really don't need to review every single two-way door. Every single one-way door you do."* (22:06~22:12)

ASR·ko 보정: ko가 **PR을 일관되게 "홍보"로**(*"친절한 홍보팀"* 16:31, ko 단독), 결론 *"don't need to review every single two-way door"* 를 캡션 경계에서 **"되돌릴 수 있는 모든 결정을 검토하십시오"** 로 쪼개 반대로 읽히게 하고(22:07~22:12), *blast radius* 를 **"라디오 폭발 현장"**·*merge danger* 를 **"녹을 위험"** 으로(18:12~18:27), *Opus 5* 를 **"작품 5"** 로(05:26), *seam* 을 **"생리 … 노조를 결성"** 으로(10:38), *underloaded* 를 **"과소평가되어 있다"** 로(13:16) 옮겼다. en-orig는 *brakes* 를 *"breaks"*, *tautological* 을 *"tortological"*, Ousterhout를 *"John ouster"*, AGENTS.md를 *"agents.mmd"* 로 들었다. 전체 목록은 raw. **인용은 en-orig에서만** 했다.

> ⚠️ **측정이 없다.** 효과 주장(*"it will make it better"*, *"very successful for me"*, *"a massive difference"*, *"amazing how many things this catches"*)은 **전부 화자 자신의 경험 진술**이고, 소개하는 스킬은 **화자 자신의 제품**이다. 예시 코드(280자 상수, 소스 파일을 읽는 UI 테스트, audio context stub)는 *"real code (…) from stuff that I found my agents doing"*(05:40~05:46)라는 화자 진술 외에 확인할 길이 없다(슬라이드는 자막에 없다).
>
> ⚠️ **행사·시점.** 행사명은 설명란에만(*"AI 엔지니어 파리 2026"*). 발화는 *"Thank you, Paris."*(22:28~22:30), *"previous AI engineer talks I've given"*(08:33~08:36). **도시가 발화된 이 위키의 첫 AI Engineer 계열 소스.** 날짜 미발화 — *"Opus 5 got addicted to these"*(05:27~05:29), *"I'll be shipping version 1.3 this week"*(22:19~22:21)뿐. 녹화는 멤버 전용 게시(늦어도 2026-10-01) 이전. **01:20~01:48 자막 공백**(세 트랙 공통, 약 23초) — 가속기 목록 앞부분이 비어 있다.

## 1. 팩토리의 가속기와 브레이크 (00:00~03:01)

- *"we have always had huge numbers of PRs just laying around that no one's bothered to review. And this has now increased massively"*(00:12~00:21) — PR 병목은 AI 이전부터 있었고 AI가 키웠다.
- **[[software-factory]]** — *"probably the biggest buzz word of the day"*(01:02~01:05). 화자의 정의: *"instead of the human initiating all of this work (…) Some of the initiation is going to be done by agents"*(01:10~01:20). ⚠️ 그 뒤 23초 자막 공백.
- **가속기**: *"a classifier like Jev come in and say, 'Okay, let's turn that into a fix or turn that into a reproduction.'"*(01:48~01:54), PlanetScale의 느린 쿼리 리포트가 다른 작업을 촉발(01:57~02:05). ⭐ *"All of this is not humans triggering it. It's uh deterministic code triggering it"*(02:06~02:12). → [[jev]] — LangChain 편 이후 **제3자가 Jev를 분류기 예로 든 첫 기록**.
- **브레이크**: 가속만 하면 *"a slop cannon (…) a ton of slop crappy PRs that you're not going to be able to touch or review or even freaking look at"*(02:23~02:32). 브레이크는 *"mechanisms that slow down, that increase quality"*(02:35~02:38) — 이유: *"code is the environment your agent operates in. And if you have bad code in your codebase, that is going to beget more bad code."*(02:42~02:51) 그리고 역설: 브레이크로 *"counterintuitively go faster"*(02:56~02:58).

→ [[slop-cannon]] · [[codebase-gardening]]

## 2. 브레이크 세 겹 (03:01~04:47)

| 겹 | 무엇 | 비용 (화자) |
|---|---|---|
| 1. **자동 검사** | *"linting and tests and type checking and code quality metrics (…) they all work the same every time"*(03:09~03:19) | ⭐ *"they don't cost tokens like automated review does. They don't cost human effort. They just cost CPU cycles."*(04:13~04:21) |
| 2. **자동 리뷰** | 에이전트가 *"the things that the tests didn't catch"* 와 코드베이스 구조를 본다(03:22~03:32) | 토큰 |
| 3. **사람 리뷰** | *"people looking at the PR"*(03:34~03:37) | 사람 |

목표: *"to make human review faster by leaning on those first two phases"*(03:47~03:50). 첫 원칙 *"we got to stop the slop"* — *"if you raise the quality of the code that you're shipping, you're going to end up doing less human review"*(03:50~04:03). 검사는 싸니 *"you're probably not using enough of them or not being creative enough"*(04:41~04:44).

→ [[hard-vs-soft-enforcement]]의 층(코드베이스 → 정적 분석 → 규칙·스킬·bugbot)과 같은 순서이되, 여기선 **비용**(CPU → 토큰 → 사람)으로 줄 세운다.

## 3. 검사는 거짓말을 한다 (04:47~08:12) → [[structure-sensitive-tests]] (신규)

*"But checks can lie. Does a green CI mean that the code is ready for merge? No, it does not."*(04:47~04:55) 위의 두 겹은 *"lie detectors"*(05:07~05:12)다. 화자가 자기 에이전트에서 찾은 거짓말 셋:

1. **동어반복 테스트(tautological test)** — *"a test that just reasserts the implementation. Opus 5 got addicted to these."*(05:21~05:29) 예: `X_POST_CHARACTER_LIMIT = 280` → `expect(X_POST_CHARACTER_LIMIT).toBe(280)`(05:31~05:46, ⚠️ 코드는 발화에서 복원). 문제는 **구조 민감성** — 상수를 바꿔도, 이름만 바꿔도 테스트가 깨진다(06:00~06:19).
2. **소스를 읽는 테스트** — UI 두 요소의 순서를 렌더링이 아니라 **모듈 파일을 메모리로 읽어 문자열 위치로** 검사(06:22~07:06). *"It's too sensitive to the structure of my codebase."*
3. **실패할 수 없는 테스트** — `useAudioBoost` 내부의 DOM audio context API를 가짜 메서드로 stub → 실제 오류 모드를 못 잡고 *"we're going to hit strange errors in production"*(07:13~07:53).

⭐ 진단: *"The AI isn't trying to write bad tests here. It's just taking our instructions and writing tests that are too tied into the structure instead of actually executing code."*(08:00~08:12) — [[reward-hacking]]이 아니라 **선의의 구조 결합**이라는 구분.

→ [[test-harness-vs-test-authoring]]의 *"생성자를 주면 생성자를 테스트"*(Dioxus)와 같은 관찰, [[mergeability-gap]]의 *테스트 통과 ≠ 머지 가능* 을 테스트 쪽에서 본 것.

## 4. 코드베이스 설계로 빠져나온다 — deep modules (08:12~11:11) → [[deep-modules]] (신규)

*"you can actually design your way out of these bad checks"*(08:25~08:30). **Deep module** = *"modules that hide complex behavior behind simple interfaces. This is a John ouster[=Ousterhout] idea from the philosophy of software design"*(08:38~08:44). 큰 구현 + 작은 인터페이스(A) vs 큰 인터페이스 + 얕은 함수들(B) — A는 *"fewer structure sensitive tests"*(09:07~09:12). ⭐ *"your job here is to force the agent to use that little interface instead of reaching into the implementation to test these weird implementation details"*(09:18~09:27).

- **스킬**: 코드베이스에서 *"opportunities for deepening modules"* 를 찾아 before/after HTML 문서로 보여 준다(09:30~10:12). *"the crappiest codebase that you've ever set your eyes on and you can run this skill on it and it will make it better"*(09:36~09:41 — ⚠️ 화자 진술).
- **어휘**: *"you're going to find 20 different approaches and they're all going to be called DDD"*(10:21~10:26) → 팀 공용어로 **locality**(변경이 한곳에 모여 있는가), **leverage**(호출자가 단순한 호출로 많은 가치를 얻는가), **seam**(*"I was using seams before they were cool"* 10:39~10:41 — 정의는 발화되지 않음). *"Both of those are very good in code bases and good for agents too, it turns out."*(11:03~11:08)

## 5. 코딩 표준은 구현이 아니라 리뷰에 (11:11~14:20)

⭐ *"don't put coding standards in your implement agent"*(11:34~11:39). 구현 에이전트의 한 컨텍스트 창은 **탐색 · 수정 · 디버깅(자동 검사 돌리기)** 으로 이미 차 있고(11:43~12:06), 여기에 표준까지 얹으면 *"it's going to perform worse"*(12:11~12:16) — *"implementation is overloaded. That's the mental model I want you to have."*(12:19~12:23)

- **코드 리뷰 스킬**: diff를 받고 저장소의 **coding standards 파일**을 읽어 준수 여부를 검사, **서브에이전트로** 돌아 자기 컨텍스트·예산을 가진다(12:30~12:54). 약간의 탐색만 하고 구현·디버깅은 안 하니 *"while implementation is overloaded review is actually underloaded"*(13:13~13:18) → 표준을 *"pile in"* 할 수 있다.
- *"implement, you make it work, and then code review, you actually make it good"*(13:38~13:45) — *"essentially a red green refactor approach"*, 컨텍스트 창 둘(13:48~13:58).
- 그래서 표준은 **전역(AGENTS.md)에 두지 않는다** — *"because then they sort of drown out your implement. It may read them, it may not."*(14:07~14:14) → coding standards 파일에 두고 리뷰 에이전트만 읽는다(14:14~14:18). ⚠️ 파일명 표기는 자막으로 확정되지 않는다(raw).

→ [[generator-evaluator-pattern]](생성·평가 분리)의 **컨텍스트 예산 논거**판: 분리의 이유가 *자기 평가 편향* 이 아니라 **한 창에 들어갈 일의 양**이다. [[context-engineering]]과 [[agent-skills]]의 progressive disclosure와도 같은 방향.

## 6. 자동 리뷰 — 외주하지 말고, 커밋하게 하라 (14:20~16:17)

- *"we just use a third party service. We use cursor bug bot. We use code rabbit"*(14:31~14:36) 라는 말에 대해: 범용 리뷰 스킬은 *"too general and it just gives you false positives (…) or you make it too specific (…) and then Rust people can't use it"*(14:49~15:01). ⭐ *"don't outsource automated review. Build your own. Build up your own coding standards over time. Share them across your team."*(15:01~15:11) 읽히지 않는 문서가 있으면 *"this is the place to put them"*(15:13~15:18).
- ⭐ **리뷰어는 커밋한다**: PR에 댓글을 다는 리뷰 에이전트는 *"providing more work for the human reviewer"*(15:35~15:39). *"The reviewer should commit. It should make fixes."*(15:43~15:48) 질문이 있을 때만 댓글, *"the default should be commits"*(15:58~16:00).
- *"Stop trying to oneshot good code."*(16:02~16:05)

→ [[automated-code-review]] — Voss가 정리한 *리뷰 + 수정 융합*(Cursor의 수정 에이전트)과 같은 결론을 **개인 스킬 수준**에서. [[hard-vs-soft-enforcement]]의 *"PR 댓글은 코드 스멜"* 과도 겹친다.

## 7. 사람 친화 PR — one-way door, blast radius, 다이어그램 (16:17~19:41)

새 **PR 스킬**(*"currently in progress, but I'll be releasing it soon"* 16:37~16:42), 방법은 *"steal all the best ideas that everyone's got"*(16:49~16:53).

- 원칙 ① *"some reviews are more important than others"*(17:02~17:07). 분류 기준은 *"this AWS terminology, which is is it a one-way door or is it a two-way door?"*(17:21~17:29). *"most PRs that you have will be two-way doors"*(17:29~17:31) — 소프트웨어 엔지니어의 *"glorious benefit"*, 토목 기사라면 *"that bridge is going down"*(17:36~17:46). 단 단순한 변경이 *"accidentally blasts out an email to 60,000 people"* 이면 one-way door, *"expensive migrations or data loss"* 도 — *"Review the hell out of that PR"*(17:54~18:11).
- **blast radius** — *"What can go wrong? And if things do go wrong, how bad is it?"*(18:12~18:19). 모든 PR 하단에 **merge danger** 요약: *"this one is a two-way door. Its blast radius is localized"* → *"I'm just going to sort of review it a little"*(18:22~18:36).
- 원칙 ② PR이 무엇을 하는지 — *"the best thing I've come up with is using pseudo code"*(18:44~18:49), 그리고 Dex의 **show me** 스킬(*"the human layer skills repo"*, 18:51~18:58)처럼 텍스트 대신 이미지·다이어그램(Mermaid·UML, 새 CLI 명령·플래그 요약). *"you're trying to like make understanding the why as fast as possible"*(19:34~19:37). ⚠️ 의사 코드와 다이어그램의 관계는 정리되지 않는다.

→ [[action-reversibility]] · [[risk-proportional-human-review]] — 위험도 기준을 **PR마다 적는 한 줄**로.

## 8. 시스템을 리뷰한다 — retro (19:41~21:54)

원칙 ③: 모두가 같은 스킬·steering 파일로 에이전트 환경을 함께 짓고 있으니 *"You should think of the process that produces your code as just as important as the code itself"*(20:07~20:13) → ⭐ *"when you do a human review, you're not just reviewing the code, you're reviewing the system that creates it. And the theory here is that you never want to write the same comment twice"*(20:14~20:24).

**retro 스킬**(retrospective): 에이전트 세션 하나, PR + 세션, 또는 *"all of the PRs that we've done over the last week, all of the reviews"*(20:45~20:51)를 회고해 **자동 검사와 coding standards 갱신을 제안**한다(20:54~20:59). *"by doing human review you're making the quality of the next human review higher"*(21:04~21:08). 그 밖에 **navigation pointers**(에이전트가 정보를 얼마나 쉽게 찾았나, AGENTS.md에 포인터를 둘 수 있나 21:21~21:29), **tool economy**(더 토큰 효율적인 도구 21:31~21:38), **bloat**(비대한 steering 파일·스킬 21:43~21:51).

→ [[skill-self-improvement]](여섯 번째 경로 — 사람의 **리뷰**를 원천으로) · [[hard-vs-soft-enforcement]]

## 9. 정리 (21:54~22:32)

*"we make the human review as painless, as simple, and as kind of optional as we need it to. You really don't need to review every single two-way door. Every single one-way door you do."*(22:01~22:12) 스킬은 *"AIhero.dev/skills"*, *"I'll be shipping version 1.3 this week"*(22:14~22:21).

## 이 위키와의 연결

### 이어지는 것

- **[[verification-bottleneck]]** — Voss 편의 *네 번째 답*(리뷰를 시스템으로 재건)을 **실행 단위로 쪼갠 것**: 사람 리뷰는 남기되 그 앞에 싼 층 둘을 깔고, 사람은 one-way door만 전부 본다.
- **[[tech-bridge-death-of-code-review]]** — 같은 결론의 다른 높이. Voss: *"stop reviewing PRs"*, 리뷰 하네스를 지어라(산업 서베이). Pocock: 하네스의 부품(coding standards 파일 · 리뷰 서브에이전트 · 커밋하는 리뷰어 · merge danger · retro). Voss가 인용한 Dex Horthy(*"Please read the code"*)와 Pocock이 인용한 Dex의 show me 스킬이 **같은 사람일 가능성**(⚠️ 미확정).
- **[[codebase-gardening]]** (Lauren Tan) — *"code is the environment your agent operates in (…) bad code (…) beget[s] more bad code"*(02:42~02:51)는 *"코드베이스는 기억이다"* 와 같은 전제. Pocock의 처방은 정원사가 아니라 **설계(deep modules)와 리뷰어의 커밋**.
- **[[hard-vs-soft-enforcement]]** — *"PR 댓글은 코드 스멜"*(Tan) ↔ *"never write the same comment twice"* + retro가 자동 검사를 제안(Pocock). 둘 다 **사람 댓글을 하드 규칙으로 승격**시키는 루프.
- **[[slop-cannon]]** — Dioxus(당사자의 고백) · Conductor(재작성)에 이어 **팩토리의 브레이크 부재**라는 구조적 정의.
- **[[software-factory]]** — Factory·Warp의 정의에 **가속기/브레이크** 축을 더한다. Warp가 *"가장 고통스러운 칸"* 이라 한 코드 리뷰 칸을 이 편은 통째로 다룬다.

### 갈리는 것

> ⚠️ **Contradiction: 자동 리뷰를 사서 쓸 것인가.** [[tech-bridge-death-of-code-review]]는 Copilot 리뷰(6천만 건)·CodeRabbit(1,300만 PR)·Cursor를 **업계 기본값**으로 서술하고 Voss는 벤더 리뷰어 자체엔 반대하지 않는다. Pocock은 *"don't outsource automated review. Build your own"*(15:01~15:07) — 이유는 범용 리뷰어의 **오탐 vs 범용성** 딜레마(14:47~15:01). Voss 편의 Cursor도 오탐을 1세대 리뷰어의 핵심 문제로 꼽았다 — **문제 인식은 같고 처방(벤더의 다중 패스 vs 팀 고유 표준)이 갈린다.**

> ⚠️ **사람 리뷰를 어디에 둘 것인가 — 두 편의 차이.** Voss는 *"stop reviewing PRs. Um, it is the wrong level of abstraction for 2026"*(Voss 편 23:19~23:25). Pocock은 PR을 계속 리뷰하되 **사람 친화 PR**로 만들고 one-way door는 *"Review the hell out of that PR"*. 둘 다 *시스템을 리뷰하라* 에 동의하지만(Pocock 20:14~20:20), **PR 단위 사람 리뷰를 남기느냐**에서 갈린다. Voss의 *사람이 남는 세 자리*(폭발 반경이 큰 곳 등)와 Pocock의 one-way door 기준은 사실상 같은 선이다(위키의 독해).

> ⚠️ **"리뷰어가 커밋한다"의 비용은 다뤄지지 않는다.** 리뷰어가 고친 코드는 **누가 리뷰하나** — Voss 편의 *"who reviews the reviewer"* 질문이 여기서는 열려 있다. 리뷰 서브에이전트의 커밋이 다시 자동 검사를 통과하는지도 발화되지 않는다.

## 해소하지 않고 표시만 한 것

- **화자 신원** — 이름·소속은 설명란에만, 자막엔 정황(AIhero.dev/skills, *"my skills"*, *"previous AI engineer talks"*)뿐.
- **01:20~01:48 자막 공백**의 내용.
- **Dex Holley / Hadley / 해들리** 와 *human layer* — Dex Horthy·HumanLayer로 판독할 근거는 이름 앞부분과 저장소 이름뿐.
- **coding standards 파일명** — *"coding standards.mmd"*(14:14), *"coding standstandards.mmd"*(21:19), 설명란 `coding_standards.md`.
- **seam의 정의**, **leverage의 정의 범위**, *"highuting"*(11:12) — 미발화·미판독.
- PR 스킬·retro 스킬이 v1.3에 포함되는지, 60,000명 이메일이 실제 사건인지.
- **Opus 5** — 이 위키에 모델 페이지 없음(지나가는 언급).

## 등장 개체

- 인물: [[matt-pocock]] (신규) · John Ousterhout(*A Philosophy of Software Design*, 페이지 없음) · Dex(*"Holley"* — ⚠️ Dex Horthy 추정, 페이지 없음)
- 조직·제품: AI Hero(aihero.dev, 화자의 스킬 배포처 — [[matt-pocock]] 페이지에서 다룸) · [[jev]] · PlanetScale · [[cursor|Cursor]] Bugbot · CodeRabbit · AWS(*one-way/two-way door* 용어의 출처로만) · Opus 5(모델, 페이지 없음)
- 개념: [[structure-sensitive-tests]] (신규) · [[deep-modules]] (신규) · [[software-factory]] · [[slop-cannon]] · [[automated-code-review]] · [[verification-bottleneck]] · [[hard-vs-soft-enforcement]] · [[codebase-gardening]] · [[generator-evaluator-pattern]] · [[action-reversibility]] · [[risk-proportional-human-review]] · [[skill-self-improvement]] · [[agent-skills]] · [[test-harness-vs-test-authoring]] · [[mergeability-gap]] · [[reward-hacking]] · [[context-engineering]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=8DRjkp_X8yY> (22:32, `upload_date` 2026-10-05, 2026-10-01부터 멤버 전용으로 확인)
- raw: `01.raw/articles/2026-10-05_AI 시대에 쏟아지는 PR 병목, 어떻게 해결해야 할까요.md`
- 설명란 링크: <https://x.com/mattpocockuk> · <https://www.linkedin.com/in/mapocock/> · <https://aihero.dev> (⚠️ 열어 보지 않았다)
- 같은 주제: [[tech-bridge-death-of-code-review]] · [[tech-bridge-lauren-tan-trusting-agents]] · [[tech-bridge-lauren-tan-2000-prs]] · [[tech-bridge-warp-factory-engineering]] · [[tech-bridge-factory-software-factory]] · [[tech-bridge-ambitious-software-agent-era]] · [[tech-bridge-jev-agent-harness]]
- [[tech-bridge]] · [[matt-pocock]] · [[ai-engineer]]
