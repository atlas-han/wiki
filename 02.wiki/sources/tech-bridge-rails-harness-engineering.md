---
title: "Tech Bridge — Rails에서 하네스 엔지니어링을 활용하는 방법 (Joël Quenneville): 프롬프트하고 기도하기를 멈추고, 판단을 RuboCop·제너레이터·훅·좁은 리뷰 스킬로 옮겨 바닥을 올린다"
type: source
tags: [harness-engineering, rails, ruby, rubocop, hooks, generators, agents-md, automated-code-review, feedforward-feedback, goodhart, domain-specific-scripts, claude-code, video]
source-url: https://www.youtube.com/watch?v=xgPyzfDIrPY
source-type: video
author: Tech Bridge (한영자막 재배포) · 발표 [[joel-quenneville]] (이름은 제목에만, 소속 미발화) · Ruby/Rails 계열 컨퍼런스(행사명 미발화), 2026년 6월 무렵~10월 초 녹화 추정
date-published: 2026-10-05
ingested: 2026-10-09
created: 2026-10-09
updated: 2026-10-09
---

# Tech Bridge — Rails에서 하네스 엔지니어링을 활용하는 방법 (Joël Quenneville)

[[tech-bridge|Tech Bridge]]가 재배포한 **30:55 단독 발표, Q&A 없음, 공식 챕터 없음.** 화자 [[joel-quenneville|Joël Quenneville]]가 **자기 Rails 코드베이스에서 한 실천**을 말한다 — 측정은 없고 일화와 슬라이드 코드다. 이 위키의 [[harness-engineering]]이 *무엇인가* 를 여러 번 정의해 왔다면, 이 발표는 **한 언어 생태계(Rails)에서 하네스의 각 칸에 무엇을 꽂는가** 를 처음으로 구체적으로 보여 준다. 신규 개념 셋 → [[human-plumbing]] · [[feedforward-feedback-steering]] · [[domain-specific-scripts]].

> **에이전트는 블랙박스가 아니라 루프다. 더 나은 프롬프트(AGENTS.md 포함)는 "prompt and pray"라 천장이 있다. 판단을 결정론적 도구(RuboCop·제너레이터)로 옮기고, 훅으로 100%를 만들고, 결정론으로 못 잡는 것만 생성 *뒤에* 좁은 리뷰 스킬로 잡는다. 사람이 손으로 결과를 나르는 순간(human plumbing)마다 그것을 하네스에 넘겨라 — 실수를 고치지 말고 시스템을 고쳐라.**

> *"a model can't do anything. It's just a brain in a jar."* (04:14~04:17) · *"The loop plus the tests are what are going to steer the agent to the right choice."* (07:57~08:02) · *"agents.mmd[=AGENTS.md] is not the place for your style guide"* (08:59~09:03) · *"even though there's less intelligence involved, the system as a whole got smarter, more consistent."* (16:16~16:24) · *"don't just fix the mistake. (…) try to fix the system so that the next time it doesn't make that mistake again. That's at the heart of harness engineering"* (30:35~30:48)

ASR·ko 보정: en-orig는 AGENTS.md를 *"agents.mmd"* 등으로 **열 번 넘게**(09-08에 기록한 `.mmd` 습관), *prompt and pray* 를 *"prompt and prey"*, Birgitta Böckeler를 *"Brigita Bookler"*, Goodhart를 *"goodart"* 로 들었다. ⚠️ **en·ko 공유 오류 둘** — 결론 문장의 *harness engineering* 이 **"control engineering"/"제어공학"**(30:44~30:48), 도메인 스크립트 사례의 *find the root cause* 가 **"RuboCop"/"루보캅을 찾아라"**(25:22~25:24). ko는 결론의 두 교훈을 모두 뒤집었다 — *"No more prompt and pray"* → **"끝났어 기도해 보세요"**, *"don't just fix the mistake"* → **"단지 그것을 수정하는 것뿐"** — 그리고 *"how could this be the last time?"* → **"이게 마지막일 리가 없잖아?"**. *cop-shaped verifications* → **"증빙 서류는 사본 형태로"**, *human plumbing* → **"인체 배관에 관한 논문"**. 전체 목록은 raw. **인용은 en-orig에서만** 했다.

> ⚠️ **en-orig 결손 셋** — 08:49~08:59 · 15:59~16:10 · 24:17~24:29 에는 en-orig 이벤트가 없고 en·ko에만 내용이 있다. 해당 구간은 **인용하지 않고 en 의역으로만** 적는다(⚠️ 표시). 영상은 문장 중간 *"of this year"* 에서 시작하고 *"raise the floor on your"* 에서 끝난다 — **자기소개 구간이 없다.**
>
> ⚠️ **화자·행사·시점.** 이름은 **제목에만**(자막엔 *"JoelQskills"*(29:32~29:33) 뿐), **소속 미발화** — 설명란 링크 shopify.engineering은 본문과 연결이 없어 쓰지 않는다. 청중은 Rubyist(03:45~03:48), *"Rachel's talk here yesterday"*(15:49~15:52) · *"Kinsey's talk earlier"*(22:49~22:54) — 여러 날짜 컨퍼런스, **행사명 미발화**. 연도 미발화(*"of this year"* · *"back in January"*). Claude Code의 *"dynamic workflow or ultraode"*(18:44~18:47)가 이 위키의 [[anthropic-dynamic-workflows]](2026-05-28)와 같은 것이라면 **2026년 5월 말 이후** 녹화 — 위키 교차 참조로 좁힌 추정. 업로드는 2026-10-05.
>
> ⚠️ **측정 없음.** 1시간 vs 이틀(00:26~01:49), 지시만으로 마이그레이션 *"maybe 90%"*(14:07~14:10), cop 생성 *"2 minutes"*(12:27~12:30), 자동화율 *"about 5%"*(24:13~24:17) — 전부 화자 경험 진술. 2차 인용 수치는 없다.

## 1. 1시간 생성, 이틀 다듬기 (00:00~02:52)

2일로 잡은 기능을 에이전트와 범위를 좁혀 돌리자 약 1시간 만에 동작하는 것이 나왔다. 그런데 내부 품질을 다듬느라 점심 → 저녁 → 다음 날 저녁 — *"I did two days worth of work in two days."*(01:46~01:49). 원인: *"I spent one hour building code and then two days playing whack-a-ole[=mole] with this, you might call it slop"*(02:03~02:12). → [[ai-slop]] · [[verification-bottleneck]]

선택지는 둘. 1시간 뒤 PR을 올려 *"shifted that burden onto everyone else. Don't do that. If you do that, you're a bad person."*(02:31~02:38), 아니면 ⭐ *"raise the floor on what the AI gives me so that I'm not spending two days reviewing it"*(02:41~02:49). **"바닥 올리기(raise the floor)"** 가 발표 전체의 구호다.

## 2. 프롬프트의 천장 — 에이전트 = 하네스 + 루프 (02:55~08:31)

- 더 나은 프롬프트, AGENTS.md에 규칙 — *"that will work to a certain extent, but (…) that's a trap. There is a ceiling here."*(03:07~03:14)
- FizzBuzz를 Anthropic API 원시 호출로 짜고 Ruby 래퍼로 감싼다 → ⭐ *"This wrapper is not just convenience. It's a thing called an agent harness. That is some code that wraps calls to an LLM model."*(03:58~04:09). 모델은 *"a brain in a jar. You put text in, you get text out."*(04:14~04:20), 하네스는 디스크를 읽고 쓰는 **그냥 Ruby 코드**라 무엇이든 덧붙일 수 있다.
- 결과물은 *"correctish"* — 15로 나누기 줄이 3으로 나누기 줄 뒤에 있어 영원히 안 걸리는 버그(04:44~04:56). *"더 나은 프롬프트"* 로 고치려는 것은 *"black box. Put a prompt in, get code out"* 멘탈 모델이고 *"kind of comes from the chat GPT era"*(05:21~05:35).
- ⭐ **손으로 하면 어떻게 하나?** 스펙을 돌리고, 실패하면 고치고, 다시 돌린다. 이것을 사람이 대신 해 주면 — *"we've put ourselves in the role of human plumbing. We're just doing that loop."*(06:27~06:31) → [[human-plumbing]] (신규)
- 하네스에 루프를 넣는다 = **agentic loop**: 하네스가 모델과 여러 번 오가고, 환경을 조회·조작하고, 종료 조건까지 돈다(06:59~07:23). *"a loop allows an agent to respond to failure. It means that the agent is now self-healing and that the first generation doesn't have to be perfect"*(07:27~07:38). *"a generic version of this loop is at the heart of all the commercial harnesses (…) cursor, claude code, or codeex"*(08:08~08:14). → [[linear-vs-closed-loop-harness]] · [[verifiable-goals]]

## 3. 결정론으로 옮기기 — RuboCop과 훅 (08:33~12:54)

- *"agents.mmd is not the place for your style guide"*(08:59~09:03) — 하네스는 AGENTS.md를 프롬프트 앞에 붙일 뿐이라 *"just another form of prompt and prey"*(09:07~09:11), 그리고 *"probabilistic"*, *"as your context gets fuller and fuller, the odds of it not following it go up"*(09:29~09:40). ⚠️ 08:49~08:59(*"AGENTS.md에 규칙을 잔뜩 넣으면? 될 수도"*)는 en-orig 결손, en 의역.
- 사람 팀은 오래전부터 린터·RuboCop으로 풀었다(09:58~10:03). 단계 ①: AGENTS.md에 *"after changing Ruby files, run rubocop"* 한 줄(10:27~10:34) — 여전히 확률적이지만 ⭐ *"We've taken all of that knowledge, all of that judgment that used to live in agents. MD, moved it into something deterministic. Rubocop owns your style guide."*(10:40~10:53)
- 단계 ②: **훅** — *"If we want to get to 100%"*(10:59~11:02). Claude의 **stop 이벤트**(루프를 빠져나가려 할 때)에 RuboCop을 걸고, 실패하면 *"you're not allowed to exit. You must run again."*(11:22~11:44). 훅 코드는 하네스마다 다르고 자주 바뀌니 *"the idea"* 가 중요하다(11:05~11:14). → [[hook-enforced-workflow]] · [[hard-vs-soft-enforcement]]
- ⭐ **야심 차게**: *"lots of quality problems have copshaped verifications"*(12:01~12:04). 예: 파인더를 테넌트로 스코프하지 않는 **멀티테넌트 버그**를 잡는 커스텀 cop(12:07~12:21), *"we have LLMs now. We can generate this in 2 minutes."*(12:27~12:30). *"anytime you're feeling frustrated by something that LLM does (…) ask yourself, is there a way to catch that using a cop?"*(12:42~12:51) → [[executable-standards]]

## 4. 제너레이터와 거부 사유 (12:57~16:29)

- 린터로 안 잡히는 것: Rails 마이그레이션 파일명 — 에이전트는 모양을 흉내 내지만 무엇이 그것을 만드는지 모른다(13:07~13:16). 알고리즘을 AGENTS.md에 산문으로? *"just more prompt and pray"*(13:29).
- 사람은 그 숫자를 치지 않는다 — *"We use Rails generators for this. So, why not have the model do it?"*(13:47~13:51). 지시 한 줄은 *"maybe 90% of the time"*(14:07~14:10).
- 100%로: **새 파일 쓰기 훅**이 Ruby 스크립트를 불러 `db/migrate` 쓰기를 막고(14:17~14:34), ⭐ **거부 사유**를 준다 — *"Instead of writing here, I want you to run the generator."*(14:42~14:45). 이유: *"agents have a goal. And if they know they need a migration (…) and you block them, they're going to try to find a way to hack around it"*(14:48~14:57) → *"making its easy path the right thing to do"*(15:00~15:02), *"because agents want to take the easy path"*(15:12~15:14). → [[deny-and-continue]] · [[reward-hacking]]
- 제너레이터에 담을 **불변식**: 특정 디렉터리의 컨트롤러는 다른 베이스 클래스, 모든 컨트롤러에 권한 정책 객체(15:21~15:45).
- 요약(⚠️ 15:59~16:10 첫 문장은 en-orig 결손, en 의역: *"우리가 한 일은 논리와 판단을 LLM에서 꺼내 결정론적 도구로 옮긴 것"*) → ⭐ *"even though there's less intelligence involved, the system as a whole got smarter, more consistent."*(16:16~16:24)

## 5. 결정론의 한계 — 좁은 리뷰 스킬과 서브에이전트 (16:30~20:12) → [[automated-code-review]]

- 결정론으로 못 잡는 휴리스틱(16:30~16:41). AGENTS.md에 코드 휴리스틱을 넣는 것은 *"a particularly poor track record, at least in my code basis"*(16:56~17:00).
- *"I really like leaning on LLM review skills"*(17:05~17:07) — 하네스 내장 리뷰도 괜찮지만, 직접 만들면 ⭐ **좁게**: *"Don't just try to dump a bunch of like random programming wisdom into a skill file. Instead, focus it on a particular theory of what good code is."*(17:15~17:24). 화자의 세 스킬 = 자기 PR 리뷰 순서: **구조**(해법이 문제에 맞나) → **메서드 단위** → **폴리시**(가독성·문서화)(17:27~17:47).
- 매번 손으로 부르면 다시 human plumbing(17:59~18:00) → 스킬을 **서브에이전트**로 — *"That helps with bias"*(18:08~18:13). *"This is not real orchestration"* — 다섯 줄짜리 스킬이 서브에이전트를 차례로 부른다(18:20~18:38). 진짜 오케스트레이션은 Claude Code의 [[dynamic-workflows|dynamic workflow]]·[[ultracode]](18:42~18:47). → [[generator-evaluator-pattern]] · [[agent-skills]]
- ⭐ **스킬에 휴리스틱을 넣는 것은 AGENTS.md와 뭐가 다른가?** AGENTS.md는 *"pluck a program for the like entire universe of possible programs"*(19:28~19:32) — *"you're steering from behind the starting line"*(19:45). 대신 *"steer from the middle of the path"*(19:49~19:52): *"apply them backwards to a concrete program I've already generated. It's much easier to find violations in a program I've written now than for all possible programs I could generate in the future."*(20:00~20:12)

## 6. Böckeler의 2×2와 Goodhart 경고 (20:16~23:40) → [[feedforward-feedback-steering]] (신규)

*"a mental model that I really like that comes from Brigita Bookler[=Birgitta Böckeler]"*(20:20~20:24) — 조향 메커니즘을 **feedforward(생성 전) / feedback(생성 후)** × **computational(결정론) / inferential(LLM)** 로 나눈다(20:31~20:50).

| | **computational** | **inferential** |
|---|---|---|
| **feedforward** | 제너레이터 · 셋업 스크립트 · 템플릿 | 프롬프트 · AGENTS.md · 정적 문서 · 근처 소스 코드 |
| **feedback** | RuboCop · Reek · Flog · Code Climate · 보안 스캐너 · 테스트 · 로그 · Playwright 브라우저 | 에이전틱 리뷰 · 에이전트 주도 분석 |

(표는 20:52~22:58 발화를 위키가 칸에 놓은 것 — 슬라이드 자체는 화면에만 있다.)

⭐ *"In general, I find it's good to move judgment out of that feed forward inferial quadrant and into the other three. Personally, I like to have my agents in D[=AGENTS.md] be a very thin almost routing layer rather than be a dump of my brain."*(21:30~21:43) — 그러나 그 칸은 *"a really valid part of the story (…) It's just not the only one."*(21:23~21:27)

⚠️ **경고 — Goodhart**: *"When a measure becomes a target, it ceases to be a good measure. (…) developed for managing humans, but it also applies to agents."*(23:08~23:17). *"when I constrain my agents too tightly, that's when they start trying to hack around things"*(23:19~23:23) — Code Climate 점수를 너무 조이면 *"your agents are going to find a way to satisfy your score in a way that's not going to satisfy you. So, give them a little bit of breathing room"*(23:31~23:40). → [[trusted-throughput]] · [[reward-hacking]]

## 7. 도메인 전용 스크립트 (23:44~27:48) → [[domain-specific-scripts]] (신규)

문서를 들여와 처리·연결·내부 게시하는 파이프라인 프로젝트, 자동화율 *"only about 5%"*(24:13~24:17). ⚠️ 24:17~24:29(*"100%로 올려야 한다, LLM을 시스템에 붙였고 실제 프로덕션 데이터까지 다 본다"*)는 en-orig 결손, en 의역. 결과는 나빴다 — *"It misses the big picture"*, 원인을 물을 때마다 *"contradictory answers"*(24:29~24:50).

화자의 멘탈 모델은 **새는 깔때기(leaky funnel)** — 그래서 문서 모집단을 *파이프라인 어디까지 갔고 어디서 떨어졌는지* 로 분류하는 스크립트를 쓰고 LLM에게 그 스크립트를 주자 *"wow, it got so much better"*(25:09~25:27). 이유 셋(25:30~26:27): ① **안정된 정의** — *"its populations are now comparable"*, 전에는 *"successfully exited the pipeline"* 의 정의조차 일관되지 않아 에이전트 둘의 이야기가 충돌했다 ② **더 높은 수준의 어휘** — 컬럼·코드 줄이 아니라 *"buckets and bales[=bails?] and pipelines and exit points"*, *"a richer set of primitives for thinking and communicating"* ③ **분류 자체** — 같은 이유로 실패한 버킷에서 조사를 시작.

⭐ *"this is not just for agents"*(26:31~26:33) — 제너레이터·cop·도메인 스크립트 모두 개발자 경험도 올린다, *"We set out to raise the floor for the LLM, but at the same time, we raise the floor for all of the developers on our team"*(26:52~26:59). 특히 *"It's all tacet[=tacit] knowledge."*(27:10~27:13). 같은 스크립트 출력으로 파이프라인 상태 시각화(27:16~27:32). Rails에선 rake·shebang 스크립트로 쉽다(27:36~27:48).

## 8. 지속 개선과 retro 스킬 · 결론 (27:52~30:52)

- 모든 메커니즘을 한꺼번에 들이지 말고 *"drive it with lived pain"*(28:14~28:18). ⭐ *"Anytime you have to correct an LLM, ask yourself, how could this be the last time?"*(28:17~28:23) — 다음엔 사람 없이 자가 수정하도록 하네스에 도구를 주라. *"Anytime you find yourself in this human plumbing loop, try to get yourself out of it."*(28:35~28:39)
- 회고 질문: 어디서 개입했나 · 어떤 신호가 빠졌나 · 손으로 복사한 것 · *"anything in my agents MD that could have been better done deterministically?"* · 대화가 열화했나, 나눌 수 있었나 · 반복되는 실수(28:47~29:09).
- 이것을 **retro 스킬**로 묶었다 — 긴 세션 뒤 히스토리를 분석해 자동화를 제안(29:18~29:29), *"JoelQskills"*. Matt Pocock도 *"I think last week"* 같은 이름(*Retro*)의 스킬을 냈다(29:41~29:49). → [[skill-self-improvement]]
- 결론 둘: ① *"No more prompt and prey. Instead, remember that an agent is a loop"*(30:17~30:23) ② ⭐ 실수를 고치지 말고 시스템을 고쳐라 — *"That's at the heart of harness engineering"*(30:46~30:48).

## 이 위키와의 연결

### 이어지는 것

- **[[harness-engineering]]** — 06-03 Cole Medin 편의 *"every mistake becomes a rule"* 과 **같은 System Evolution 루프**를 말하되, 규칙의 **목적지**가 다르다: AGENTS.md가 아니라 **결정론적 도구 → 훅 → 좁은 리뷰 스킬**. 10-02 Martinelli 편의 *"규칙 파일은 작게"* 와 같은 방향의 **세 번째 소스**.
- **[[hard-vs-soft-enforcement]]** ([[lauren-tan|Lauren Tan]]) — 코드베이스·정적 분석이 하드, 규칙·스킬이 소프트라는 층과 같은 결론. Quenneville은 그 사이에 **훅**이라는 단계(*소프트 지시를 100%로*)를 명시하고, 소프트 층에도 **좁은 리뷰 스킬**이라는 쓸모를 남긴다.
- **[[shift-left-interventions]]** ([[ryan-lopopolo|Lopopolo]]) — 프롬프트 → AGENTS.md → 정적 검증기의 스펙트럼과 같은 방향. 두 화자 모두 *사람이 손으로 하는 것을 줄인다*(게으른 프롬프터 ↔ human plumbing 탈출).
- **[[hook-enforced-workflow]]** · **[[deny-and-continue]]** — *막고 끝내지 말고 사유와 함께 돌려보내 쉬운 길을 옳은 길로*. Auto mode의 *"우회하지 말라"* 지시 대신 **대안 행동(제너레이터)을 명시**하는 쪽.
- **[[scripts-that-talk-back]]** ([[paul-bakaus|Bakaus]]) — 스크립트 출력으로 에이전트를 조향한다는 같은 발상의 두 갈래: Bakaus는 *다음 행동 지시*, Quenneville은 *도메인 어휘·정의 제공*.
- **[[automated-code-review]]** — Cursor의 다중 패스·*"suspicious by default"* 가 벤더 규모의 이야기라면, 이쪽은 **개인 규모**: 자기 리뷰 순서를 스킬 셋으로, 서브에이전트로 편향 줄이기.
- **[[skill-self-improvement]]** — retro 스킬은 *세션 히스토리 → 자동화 제안* 의 또 다른 경로(사람이 수락).

### 갈리는 것

> ⚠️ **Contradiction: 실수를 어디에 기록하나.** [[harness-engineering]]의 System Evolution 예시는 *"컨벤션 위반 ➡️ agents.md에 규칙 추가"* 다. Quenneville은 바로 그것을 *"prompt and pray"* 라 부르며 **스타일 가이드를 AGENTS.md에서 빼고** AGENTS.md를 *"a very thin almost routing layer"*(21:39~21:43)로 둔다. 두 소스 모두 *"모든 실수를 하네스 개선으로"* 에는 동의하고, 갈리는 것은 **목적지**다.

> ⚠️ **Contradiction(약): 조일 것인가.** [[hard-vs-soft-enforcement]]·[[executable-standards]]는 하드 강제를 늘리라고 한다. Quenneville은 하드 강제를 권하면서도 *"when I constrain my agents too tightly, that's when they start trying to hack around things"*(23:19~23:23) — 점수형 게이트에 **숨 쉴 여지**를 남기라고 한다. 화자 안에서는 *게이트(통과/실패, RuboCop)* 와 *점수 최대화(Code Climate)* 를 구분하는 것으로 보인다(⚠️ 위키의 독해 — 화자는 이 구분을 명시하지 않는다).

## 해소하지 않고 표시만 한 것

- **화자 소속**(설명란 shopify.engineering 링크만, 발화 없음) · **행사명** · Rachel·Kinsey의 성·발표.
- **촬영 시점** — 연도 미발화, *dynamic workflow / ultracode* 위키 교차 참조로 2026년 5월 말 이후 추정.
- **Böckeler 2×2의 원 글** — 제목·게재처 미발화, 이 위키에 없다.
- **retro 스킬 저장소**(*"JoelQskills"*) · Matt Pocock *Retro* 출시일 — 열어 보지 않았다.
- **en-orig 결손 3구간** — en 의역으로만 적었다.
- *"bales"* — bails(이탈)로 판독, ⚠️ 추정.

## 등장 개체

- 인물: [[joel-quenneville]] (신규) · Birgitta Böckeler(2×2 출처, 페이지 없음) · Matt Pocock(retro 스킬, 페이지 없음) · Rachel · Kinsey(같은 행사 발표자, 페이지 없음)
- 조직·제품: [[anthropic]](API) · [[claude-code]] · [[cursor]] · [[codex]] · ChatGPT(*"chat GPT era"*) · RuboCop · Reek · Flog · Code Climate · Playwright · Ruby on Rails(제너레이터·rake)
- 개념: [[human-plumbing]] (신규) · [[feedforward-feedback-steering]] (신규) · [[domain-specific-scripts]] (신규) · [[harness-engineering]] · [[hard-vs-soft-enforcement]] · [[hook-enforced-workflow]] · [[deny-and-continue]] · [[shift-left-interventions]] · [[executable-standards]] · [[automated-code-review]] · [[generator-evaluator-pattern]] · [[agent-skills]] · [[skill-self-improvement]] · [[linear-vs-closed-loop-harness]] · [[verifiable-goals]] · [[reward-hacking]] · [[trusted-throughput]] · [[ai-slop]] · [[verification-bottleneck]] · [[dynamic-workflows]] · [[ultracode]] · [[scripts-that-talk-back]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=xgPyzfDIrPY> (30:55, `upload_date` 2026-10-05)
- raw: `01.raw/articles/2026-10-05_Rails에서 하네스 엔지니어링을 활용하는 방법 — Joël Quenneville.md`
- 설명란 링크: <https://shopify.engineering/> (⚠️ 열어 보지 않았다, 화자와의 관계 미발화)
- 같은 주제: [[tech-bridge-harness-engineering]] · [[tech-bridge-lauren-tan-trusting-agents]] · [[tech-bridge-lauren-tan-2000-prs]] · [[tech-bridge-lopopolo-agent-harness]] · [[tech-bridge-skill-engineering-dark-arts]] · [[tech-bridge-sdd-enterprise-lessons]] · [[tech-bridge-death-of-code-review]] · [[anthropic-dynamic-workflows]]
- [[tech-bridge]] · [[joel-quenneville]]
