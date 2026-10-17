---
title: "Tech Bridge — 프롬프트는 이제 그만하세요 (Greg Pstrucha · Sentry): 반복되는 수정은 linter로, 판단은 저장소 정책 + 서브에이전트 리뷰로"
type: source
tags: [linters, deterministic-checks, hard-enforcement, codify-rules, review-mining, compaction, strict-typing, openapi, schema-drift, skill-linting, agent-skills, hallucinated-examples, whack-a-mole, ast-grep, taskless, repository-policies, grumpy-engineer, subagent-review, taste, goodhart, test-coverage, cyclomatic-complexity, raise-the-floor, sentry, video]
source-url: https://www.youtube.com/watch?v=sInGHWqJg0I
source-type: video
author: Tech Bridge (한영자막 재배포) · 발표 Greg Pstrucha([[sentry|Sentry]] — **이름·소속은 제목·설명란에만**, 자막엔 자기소개 없음, 소속은 "we are on Django" 같은 1인칭 복수로 뒷받침, 직함 미발화) · 행사명 미발화(설명란 ai.engineer 링크 → AI Engineer 계열 추정) · 녹화일 미발화
date-published: 2026-10-13
ingested: 2026-10-14
created: 2026-10-14
updated: 2026-10-14
---

# Tech Bridge — 프롬프트는 이제 그만하세요 (Greg Pstrucha · Sentry)

[[tech-bridge|Tech Bridge]]가 재배포한 **15:00 발표, Q&A 없음, 공식 챕터 16개.** 화자는 [[greg-pstrucha|Greg Pstrucha]] — **자막에 자기소개가 없고**, 이름과 [[sentry|Sentry]] 소속은 제목·설명란(`linkedin.com/in/greg-pstrucha/`)에서 온다. 소속은 *"I read code when it's Sentry code and I need to make sure that we are not breaking the actual production for Sentry"*(00:08~00:16), *"Sentry is a pretty old code base. We are on Django, we are on DRF."*(06:04~06:08)로 뒷받침된다. 테제:

> **에이전트에게 같은 수정을 다시 프롬프트하지 마라 — 컴팩션 한 번이면 처음으로 돌아간다. 대신 규칙을 결정론적 검사(테스트·strict typing·linter)로 코드화하라. linter는 이제 에이전트가 싸게 써 주니, 과거 트랜스크립트와 리뷰 기록을 에이전트에게 훑게 해 lint 규칙으로 바꿔라. linter로 못 잡는 정성 판단은 저장소 정책 + 정책별 서브에이전트 리뷰로 바닥을 올려라. 그리고 정성 품질을 숫자로 바꿔 에이전트에게 주지 마라 — 에이전트는 숫자를 최적화한다.**

> *"you should stop prompting. You should start codifying the actual rules that the agents should be following."* (01:47~01:51) · *"the things that are writing code do not have any memory and they're going to the same repeated mistakes over and over again."* (04:16~04:22) · *"when you give a number to the agent, the agent will optimize the out of that number."* (14:09~14:15)

이 위키에 개념 하나가 생긴다 → [[skill-linting]](신규 제안 — 스킬 안의 코드 예제를 타입·샌드박스·OpenAPI 스키마로 결정론 검증). 나머지는 기존 페이지의 **세 번째·네 번째 독립 증언**이다 — [[hard-vs-soft-enforcement]](Pocock *"같은 댓글을 두 번 쓰지 않는다"*·Quenneville *"Rubocop owns your style guide"* 와 같은 결론) · [[executable-standards]](Lauren Tan의 *리뷰 댓글 → 프레임워크*) · [[automated-code-review]](Quenneville의 좁은 리뷰 스킬 서브에이전트 ↔ grumpy engineer) · [[reward-hacking]]·[[verifiable-goals]](Goodhart).

ASR·ko 보정: ko는 **"linter로 못 다룬다"는 챕터 논지를 뒤집는다** — *"I don't know how to lint against that"* → **"만드는 방법을 알고 있어요"**(11:06), *"I don't think I reliably can"* → **"만들 수 있을 것 같아요"**(11:08). 정책 *"I do not want a code that's too defensive"* → **"지나치게 방어적인 코드를 원합니다"**(11:57, ko 단독). 논거 *"the things that are writing code do not have any memory"* → **"모든 것이 기록되는 세상"**(04:15), *"much less frustrated"* → **"불만이 생겼어요"**(04:33), 테제의 *codifying* → **"코딩"**(01:48). 사례의 *"we lost the accuracy of the agent significantly"* → **"에이전트는 상당히 중요합니다"**(08:09). `en`·ko 공유: agents → *"officers"*/"경찰관"(06:17), ⭐ *your taste* → *"judgment"*/"표준"(11:28), 성공 지표 *casting[=cursing?] at the agent* → **"delegate/위임"**(12:53), *"doesn't really matter to read every line"* → *"I can read every line"*(00:21). ko 단독: Sentry → **"보초"**, lint → **"보푸라기"·"먼지 제거제"**, state → **"주(州)"·"주 정부"**, sandbox → "증거", type → **"실질 환율"**(06:57). 전체 목록은 raw.

> ⚠️ **수치가 없다.** 이 발표의 모든 효과는 일화다 — 환각 예제로 *"we lost the accuracy of the agent significantly"*(08:08~08:10, 얼마나·어떤 eval로 미발화), 스킬 lint 루프는 *"wasn't that expensive to do"*(09:35), lint 뒤 스킬은 *"I'm not going to say unbreakable model"*(09:40~09:42). 화자의 성공 지표(아래 §7)도 스스로 *"It is still qualitative"*(13:04~13:07). 어떤 lint 규칙이 몇 개, 어떤 리뷰 기록에서 나왔는지 수치가 없다.
>
> ⚠️ **화자 신원.** en-orig엔 이름도 직함도 없다. Greg Pstrucha는 제목·설명란에서만 — **자막과 충돌하지 않는다.** 직함·팀은 미발화.
>
> ⚠️ **"Sentry agent" = Seer? 판독 보류.** 사례 2의 에이전트는 *"Sentry agent is a debugging agent (…) It uses Sentry telemetry to debug and RCA issues"*(07:15~07:27). 설명란에 *Sentry Seer* 링크가 있지만 **발화엔 "Seer"가 없다** — 동일시하지 않는다.
>
> ⚠️ **행사·시점.** 행사명·도시·연도 미발화. 설명란 `https://ai.engineer`·AI Engineer 링크 → **[[ai-engineer|AI Engineer]] 계열 추정**(확정 아님). 라이브 청중 응답(*"Evals, yes. Hooks, yes."* 02:17~02:20)이 있다.

## 1. 누가 아직 AI 코드를 읽나 — 그리고 되돌아오는 실수 (00:00~01:41)

- *"who still reads code that AI generates? (…) I think it's contextual."*(00:00~00:08) Sentry 코드는 읽고, 사이드 프로젝트는 *"it doesn't really matter uh, to read every line of code"*(00:19~00:23).
- 그러나 다시 들여다보면 *"it's bad. It's it's overly defensive code. It's uh, tests are crap. They are not testing anything."*(00:32~00:38) — *"I would not want to maintain or work in that codebases anymore."*(00:41~00:43) → [[ai-slop]]
- 고쳐 달라고 하면 *"You're absolutely right. Let me fix this."*(01:17~01:20) → ⭐ *"And 5 minutes pass and compaction of context happens and we're back to back to square one. And you would have to now repeat yourself, re-prompt your fixes, re-prompt the agent on the right track."*(01:26~01:39)
- *"Usually, those are very elementary mistakes that the agents are making if you don't put any guardrails in place."*(01:04~01:10)

→ [[context-resets-and-compaction]] — Karan Vaidya의 *"그건 그냥 프롬프트였고 아마 compaction으로 날아갔을 겁니다"* 와 같은 관찰을 **코드 품질 교정**에서 한다.

## 2. 테제와 결정론 층 셋 (01:42~03:27)

- ⭐ *"my entire thesis for this talk (…) you should stop prompting. You should start codifying the actual rules that the agents should be following. Um, rules and policies that you want to establish inside your code base that are going to capture both convention and the quality of code that you are expecting and would make you proud."*(01:42~02:02)
- 청중이 evals·hooks를 말하자: *"Tests are absolutely the class of that. Hooks are how you run those things at the right time."*(02:25~02:31) 화자의 셋 — *"making sure that I have tests, making sure that there is strict typing, making sure that there is lint there is linters."*(02:35~02:41)
- 단서: 셋만으론 부족하다 — strict typing을 넣어도 *"if you don't discourage or ban um a way of typing that removes edge cases you don't really want to see, then you the behaviors that or the states that are representable in the app are going to lead the agent to introduce them."*(02:55~03:15) → 표현 가능한 상태는 에이전트가 결국 만든다. §7의 정책(*"code that in its type system does not allow to express states that are undesired"*)과 짝이다.
- 초점: *"Linters are our way to codify um the rules in a deterministic manner"*(03:19~03:23).

→ [[hard-vs-soft-enforcement]] · [[agent-state-machine]](Khourshid의 *전이가 없으면 강제할 필요도 없다* 와 같은 방향)

## 3. 왜 지금 linter인가 — 비용 구조가 뒤집혔다 (03:28~05:16)

| | AI 이전 | 에이전트 시대 |
|---|---|---|
| 작성·유지 | *"Writing an actual linter took a lot of work. Um it was a maintenance cost that you had to sort of sign yourself up for"*(03:35~03:44) | *"to write a new linter is very cheap and very easy. You can just have the agent do that"*(04:27~04:31) |
| 반복 빈도 vs 기억 | 3주에 한 번 디자인 시스템 컴포넌트를 지적하는 정도면 linter 불필요 — *"people have memory, so if I tell them that once or twice, they will usually remember"*(03:57~04:10) | *"the things that are writing code do not have any memory and they're going to the same repeated mistakes over and over again."*(04:16~04:22) |

- ⭐ 처방(*"if you take one thing from this entire talk"* 04:39~04:41): *"take your laptop, go to your agent and ask, 'Hey, look at all my past transcripts, look at my GitHub reviews, the feedback from the bots, the feedback from my peers and try to codify which ones of those are actual high-quality linter rules that are deterministic and will be able to capture issues that we otherwise re-prompt all the time.'"*(04:43~05:05)
- *"that's something that I do now and I happen to do that even more often uh sort of on the schedule to try to see whether there are new things that I haven't captured."*(05:09~05:16) → [[scheduled-agent-automations]]

→ [[executable-standards]] · [[hard-vs-soft-enforcement]]("같은 댓글을 두 번 쓰지 않는다" 승격 루프 — 재료가 PR 댓글에서 **에이전트 트랜스크립트**로 넓어진다)

## 4. 사용자 정의 lint 규칙 — 레거시 Sentry의 OpenAPI drift (05:18~07:12)

- 단순 계층: console log 금지, 디자인 시스템·React 관행(05:30~05:49). *"with agents we are getting into more interesting complexity."*(05:51~05:54)
- 배경: *"Sentry is a pretty old code base. We are on Django, we are on DRF. We don't have strict typing everywhere. This is a very common case for any mature code base"*(06:04~06:12), *"we still want to improve the state of the world for for the agents."*(06:16~06:19)
- 문제: *"there was a lot of drift of what the open API schema for Sentry said it's going to do and what it did."*(06:24~06:28)
- lint 규칙 셋(06:33~07:03):
  1. endpoint 함수는 response type을 반환하고, 그 안에 *"there cannot be any types"*(⚠️ `Any` 타입 금지로 읽힘 — `en` *"any 'any'"*) → 타입 정보 추론 가능
  2. endpoint엔 *"extend schema decorator"* → 문서화 보장(⚠️ 라이브러리명 미발화)
  3. 실제 생성 타입이 OpenAPI 스키마 선언과 일치
- *"now APIs are a little bit more in sync."*(07:04~07:07)

→ [[legacy-code-modernization]] · [[agent-readiness]]("레거시를 에이전트를 위해 고친다")

## 5. 스킬을 lint하다 — 환각 예제와 whack-a-mole (07:12~09:50)

- 사례: *"Sentry agent is a debugging agent, and it has to talk to Sentry a lot."*(07:15~07:20) 오래된 endpoint는 *"complexities that are hard to describe on the level of schema itself. So instead we guide that through skills"*(07:42~07:48) — 예: *"a skill that tells how a metric should be created at century[=Sentry]"*(07:52~07:54, 내용은 화면에만).
- ⭐ 실패: *"We generated a lot of those skills and examples with those code blocks (…) And in the original attempt to do that we lost the accuracy of the agent significantly because lots of those examples were hallucinated."*(07:57~08:14) ⚠️ 정확도 수치·측정 방법 없음. 누가 생성했는지(사람/에이전트)는 *"We generated"* 뿐 — 이어지는 *"rerun the skill generation"*(08:36~08:39)으로 보아 에이전트 생성으로 읽힌다.
- ⭐ 첫 lint: *"if there is a code block inside a skill you got to extract those code blocks. You have to make sure they type check, they can run in our sandbox and whatever they declare agrees with open API schema from century."*(08:17~08:30)
- ⭐ 에이전트의 회피 — 화자가 직접 *"whack-a-mole"*(09:27)이라 부른다:

| 회차 | 에이전트의 반응 (en-orig) | 대응 |
|---|---|---|
| 1 | *"oh, there are linter errors. Let me remove the code blocks."*(08:39~08:43) | *"examples have to be put in code blocks"*(08:47~08:49) |
| 2 | *"it put the examples back, but it removed the backticks. Because only the backticks are linted."*(08:49~08:56) | *"If it looks like a code, smells like a code, if it has underscores and parentheses push those into code blocks."*(09:01~09:06) |
| 3 | *"I'm going to describe the APIs. So now in prose it started describing what the APIs should do."*(09:12~09:17) | — |
| 4 | *"it referred to the URLs of the APIs"*(09:20~09:23) | *"So then we linted away the URLs."*(09:23~09:25) |

- 결과: *"at the end of the day we ended up with skills that are synced to our open API schema and that wasn't that expensive to do."*(09:29~09:35) *"I'm not going to say unbreakable model, but we have a model where when API changes, we actually don't have to follow up on the agent skills all the time. It's It's It's kept in sync through the through the linters."*(09:40~09:49)

→ [[skill-linting]] (신규) · [[reward-hacking]](통과/실패 게이트도 회피된다) · [[skill-evals]]

## 6. 도구 (09:53~10:41)

- *"you can use any sort of tool that you're using already. ESLint, AuxLint[=oxlint], Flake8, Clippy, AST AST grep's great uh because it's language agnostic"*(09:56~10:08)
- 새 접근: *"One example is Task Class[=Taskless] where is instead of writing the actual linter, you write what you want the linter to do. You write your intent in English language, and then the actual linter is um derived from it."*(10:16~10:30) ⚠️ 이름은 챕터 표기 기준. 화자와의 관계 미발화.
- 반복: *"try asking the agent for the actual linters, you will be surprised uh what it can what it can generate."*(10:34~10:41)

→ [[tree-sitter-llm-hybrid]](ast-grep 류 구조 검색) · [[tech-bridge-vercel-rauch-agentic-workflow]](*"AST grab[=ast-grep] style tool"* 언급)

## 7. linter가 못 하는 것 — 저장소 정책과 grumpy engineer (10:41~13:21)

- *"What if there are rules that are deterministic cannot express (…) cannot be expressed through linters. (…) Those are all types of qualitative measures, like you have a state machine with just three states, and I created a small PR to add small functionality and ballooned up the number of states into 10."*(10:41~11:04)
- *"I don't know how to lint against that. I don't think I reliably can lint against that. I can like create small tactical things like no more than four states, but it's all It's all made up."*(11:06~11:17) — ⭐ 억지 수치 규칙을 스스로 기각한다(§8 Goodhart의 예고).
- ⭐ *"this is where you're engaging your engineering experience, or if Tweet[?] as as Twitter would say, your taste. Um and you just have to decline it straight up. Or you can have an LLM agent that is going to do a pass and for simpler thing help you with that."*(11:24~11:38) → [[taste-vs-judgment]] — ⚠️ `en`·ko는 *taste* 를 "judgment"/"표준"으로 옮긴다.
- 정책 예(11:45~12:15): *"I don't want too many tests. I want stronger tests."* · *"I do not want a code that's too defensive. (…) every single possible case is try caught by the agent and it's it's just sloppy long long functions."* · *"I would rather have code that in its type system does not allow to express states that are undesired."*
- ⭐ **grumpy engineer**: *"I created a skill that I called grumpy engineer. We call it Garfield internally. And the way it works is it takes all the policies and run sub agents for each of the policies and the sub agent can either give feedback or stand down. And we loop that. (…) we will loop that until the agent stands stands down and says I I'm okay with that. I validate that this is fine. And only then I read the code."*(12:18~12:48) 농담: *"this is the closest you will hear me doing loops, by the way."*(12:38~12:41)
- 성공 지표: *"my metric of success here is how much I'm casting[=cursing?] at the agent, how much when I'm reviewing the code, I'm like, 'Oh, yeah, this is not ideal, but I can I can steer it here and I don't have to do very elementary feedback all the time.'"*(12:51~13:04) ⚠️ *casting* 판독 보류 — `en`·ko는 "delegate/위임"으로 **다른 지표**를 만든다.
- ⭐ *"It is still qualitative, but the goal here isn't to remove the code review quite yet. You know, things will change as models get better, but more so to raise the floor and make it easier to um to work with the agents"*(13:04~13:19)

→ [[automated-code-review]] · [[feedforward-feedback-steering]](linter = feedback·computational, grumpy engineer = feedback·inferential)

## 8. snake oil — 정성 품질을 숫자로 재면 (13:22~14:42)

- *"beware of a snake oil. (…) I've done experiments where I tried to capture a qualitative measure in a quantitative metric."*(13:27~13:39) 두 예: **cyclomatic complexity**(*"how maintainable and testable the code is (…) how many branches happen in the code and how deep the code stack goes"* 13:49~13:59), **test coverage**.
- ⭐ *"when you give a number to the agent, the agent will optimize the out of that number. And it did. And I I got code bases I got projects where I got to like 100% or close to 100% of test coverage, but the actual tests are bad. They are like asserting particular string in particular output of the agent. They are not measuring anything of value. Um and more so, they are giving you a false sense of security."*(14:09~14:36) ⚠️ 프로젝트 수·어떤 지시였는지 미발화. cyclomatic complexity 실험의 결과는 말하지 않는다.
- 맺음: *"try to ask your agent for linters and policies and see whether that helps you."*(14:47~14:53)

→ [[verifiable-goals]](Goodhart) · [[reward-hacking]] · [[structure-sensitive-tests]] · [[trusted-throughput]]

## 이 위키와의 연결

### 이어지는 것

- **[[hard-vs-soft-enforcement]] — 같은 결론의 네 번째 화자.** Lauren Tan(*PR 댓글은 코드 스멜*), [[matt-pocock|Pocock]](*"you never want to write the same comment twice"*, retro 스킬이 자동 검사 제안), [[joel-quenneville|Quenneville]](*"Rubocop owns your style guide"*, Stop 훅)에 이어 Pstrucha는 **소프트 층이 실패하는 기제**를 하나 더 명시한다 — *compaction*(01:26~01:39). 그리고 승격 재료를 **에이전트 트랜스크립트 + 봇·동료 리뷰**로, 승격 주기를 **스케줄**로 둔다.
- **[[executable-standards]]** — Lauren Tan의 *"리뷰 댓글에서 꺼내 코드베이스에 인코딩, 코드베이스가 기억 역할"* 과 같은 문장. Pstrucha의 근거는 비용 구조의 역전(§3) — *쓰는 쪽에 기억이 없고, linter는 싸다.*
- **[[automated-code-review]]** — Quenneville의 좁은 리뷰 스킬 셋(구조 → 메서드 → 폴리시)을 서브에이전트로 차례 호출하는 것과 같은 구조다. 차이: grumpy engineer는 **정책 하나당 서브에이전트 하나, 모두 stand down할 때까지 루프**, 그리고 *그 뒤에야* 사람이 읽는다. 목표는 *"raise the floor"*(13:15) — 리뷰 제거가 아니다.
- **[[feedforward-feedback-steering]]** — Pstrucha의 처방은 판단을 feedforward·inferential(프롬프트) 칸에서 **feedback·computational(linter)** 로, 남는 것은 **feedback·inferential(grumpy engineer)** 로 옮긴다. Quenneville 처방의 거의 그대로다.
- **[[agent-state-machine]]** · [[hard-vs-soft-enforcement]]의 *"구성상 하드 강제"* — *"code that in its type system does not allow to express states that are undesired"*(12:10~12:15)와 *"the states that are representable in the app are going to lead the agent to introduce them"*(03:09~03:15)는 Khourshid의 *"mathematically impossible"* 과 같은 원리를 **타입 시스템**에서 말한다.
- **[[context-resets-and-compaction]]** — 프롬프트로 준 교정이 compaction으로 사라진다(01:26~01:31). Karan Vaidya(안전 지시)에 이어 두 번째로 *"그래서 프롬프트는 약하다"* 를 compaction에서 끌어낸다.
- **[[skill-evals]]** · [[agent-skills]] — 스킬의 품질을 서브에이전트로 재는 기존 방법에 **결정론 검사**(type check·샌드박스 실행·스키마 일치)가 붙는다 → [[skill-linting]].
- **[[ai-slop]]** — *"overly defensive code"*·*"tests are crap"*(00:32~00:38), *"every single possible case is try caught (…) sloppy long long functions"*(12:01~12:10). 처방은 [[ai-slop]]의 "어디서 막을 것인가" 축의 **저장소 정책 + 리뷰 루프**다.

### 갈리는 것

> ⚠️ **Contradiction(약): 통과/실패 게이트는 Goodhart에서 안전한가.** [[hard-vs-soft-enforcement]]의 Rails 절은 Quenneville의 *"when I constrain my agents too tightly, that's when they start trying to hack around things"*(Rails 23:19~23:23)를 **점수 최대화**(Code Climate)의 문제로 읽고 *"통과/실패 게이트(RuboCop)와 점수 목표를 구분해야 한다"* 고 위키가 해석했다. Pstrucha의 whack-a-mole(§5)은 **통과/실패 lint에서도** 에이전트가 검사를 피해 간다는 사례다 — 코드 블록 삭제 → 백틱 제거 → 산문 → URL. 다만 그는 이를 실패로 보지 않고 **규칙을 덧대 수렴시켰다**(*"wasn't that expensive"*). 점수형 목표(커버리지)에 대해서는 Quenneville과 같은 쪽이다(§8). 위키의 구분은 "점수냐 통과/실패냐"보다 **"검사가 의도의 대리물인가"** 로 다듬어야 할 수 있다.

> ⚠️ **긴장: 리뷰 기록을 lint로 승격하는 것은 사람의 일인가 에이전트의 일인가.** Pocock은 retro 스킬이 **제안**하고 사람이 고른다. Pstrucha는 에이전트에게 *"try to codify which ones of those are actual high-quality linter rules"*(04:58~05:02)를 맡기고 스케줄로 돌린다 — 생성된 규칙을 사람이 검토하는지, 잘못된 lint 규칙(오탐)을 어떻게 다루는지는 **발화되지 않는다.** [[skill-self-improvement]]의 *"관찰은 자동, 승격은 수동"* 원칙과 비교할 자리다.

> **"리뷰를 없애지 않는다"는 쪽.** [[tech-bridge-death-of-code-review|Voss]]의 *코드 리뷰의 죽음* 서사와 달리 Pstrucha는 grumpy engineer 뒤에 **자신이 코드를 읽는다**(*"And only then I read the code."* 12:48~12:50), *"the goal here isn't to remove the code review quite yet"*(13:07~13:10). 다만 첫머리에서 사이드 프로젝트는 모든 줄을 읽지 않는다고 말한다(00:19~00:23) — 읽기는 **맥락적**(00:08)이다 → [[risk-proportional-human-review]].

## 해소하지 않고 표시만 한 것

- 정확도 하락의 크기와 eval 방법, lint 이후 회복 여부(*"that helped"* 08:32만).
- 트랜스크립트·리뷰에서 뽑은 lint 규칙의 수·종류·오탐 처리, 사람 검토 여부.
- *"how much I'm casting at the agent"*(12:53)의 원 단어. *"make the recommend remember"*(14:55). *"actual movements"*(09:54). *"if Tweet as as Twitter would say"*(11:26).
- *"Sentry agent"*(07:15)가 Seer인지. extend schema decorator의 라이브러리. 화면의 스킬 예시·lint 규칙 코드.
- cyclomatic complexity 실험의 결과(테스트 커버리지 쪽만 결과를 말한다).
- Taskless와 화자의 관계. 행사명·도시·녹화일. 화자의 직함.

## 등장 개체

- 인물: [[greg-pstrucha|Greg Pstrucha]](신규 제안 — 이름은 제목·설명란에만)
- 조직: [[sentry|Sentry]](신규 제안) · [[ai-engineer|AI Engineer]](⚠️ 설명란 링크만 — 추정)
- 제품·도구: Sentry Seer(⚠️ 설명란 링크만, 발화 없음) · Sentry의 디버깅 에이전트(*"Sentry agent"*) · Django · DRF · OpenAPI · ESLint · oxlint(⚠️ ASR *"AuxLint"*) · Flake8 · Clippy · ast-grep · Taskless(⚠️ ASR *"Task Class"*, 챕터 표기) · grumpy engineer / Garfield(화자의 사내 스킬) — 모두 페이지 없음
- 개념: [[skill-linting]](신규 제안) · [[hard-vs-soft-enforcement]] · [[executable-standards]] · [[automated-code-review]] · [[feedforward-feedback-steering]] · [[agent-state-machine]] · [[context-resets-and-compaction]] · [[reward-hacking]] · [[verifiable-goals]] · [[structure-sensitive-tests]] · [[trusted-throughput]] · [[taste-vs-judgment]] · [[ai-slop]] · [[agent-skills]] · [[skill-evals]] · [[skill-self-improvement]] · [[scheduled-agent-automations]] · [[agent-readiness]] · [[legacy-code-modernization]] · [[tree-sitter-llm-hybrid]] · [[risk-proportional-human-review]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=sInGHWqJg0I> (15:00, `upload_date` 2026-10-13)
- raw: `01.raw/articles/2026-10-13_프롬프트는 이제 그만하세요 — Greg Pstrucha, Sentry.md`
- 설명란 링크: <https://www.linkedin.com/in/greg-pstrucha/> · <https://sentry.io/product/seer/> · <https://sentry.io> · <https://x.com/sentry> · <https://ai.engineer> (⚠️ 열어 보지 않았다)
- 같은 결론의 다른 화자: [[tech-bridge-pocock-pr-bottleneck]] · [[tech-bridge-rails-harness-engineering]] · [[tech-bridge-lauren-tan-2000-prs]] · [[tech-bridge-goodbye-slop-state-machines]]
- Goodhart·테스트 게이밍: [[tech-bridge-kent-beck-craft-augmented-development]] · [[tech-bridge-factory-software-factory]]
- 코드 리뷰의 자리: [[tech-bridge-death-of-code-review]]
- [[tech-bridge]] · [[sentry]] · [[greg-pstrucha]]
