---
title: 하드 강제와 소프트 강제 (Hard vs Soft Enforcement)
type: concept
category: pattern
tags: [ci, lint, guardrails, code-review, enforcement, standards]
aliases: [강제의 층, CI를 빨갛게, 소프트 강제에 의존하지 말라]
related: [executable-standards, verifiable-goals, llm-coding-guidelines, agent-governance-layers, shortest-path-architecture, verification-bottleneck, behavior-validated-trust, codebase-gardening, structure-sensitive-tests, deep-modules, agent-state-machine, agent-plus-program-analysis, skill-linting, context-resets-and-compaction]
first-seen: tech-bridge-lauren-tan-trusting-agents
sources: [tech-bridge-lauren-tan-trusting-agents, tech-bridge-graft-code-knowledge-graph, tech-bridge-lauren-tan-2000-prs, tech-bridge-skill-engineering-dark-arts, tech-bridge-pocock-pr-bottleneck, tech-bridge-rails-harness-engineering, tech-bridge-goodbye-slop-state-machines, tech-bridge-gitar-agentic-pr-validation, tech-bridge-sentry-stop-prompting-codify-linters, tech-bridge-horthy-state-of-software-factory, tech-bridge-g2i-generation-cheap-evaluation-expensive, tech-bridge-braintrust-agentic-vs-vector-search-eval, tech-bridge-atlassian-build-your-own-sdlc]
created: 2026-09-13
updated: 2026-10-17
---

# 하드 강제와 소프트 강제

**제약을 층으로 쌓되, 에이전트가 잊을 수 있는 층에 강제를 의존하지 않는다**는 원칙. [[lauren-tan]]이 [[tech-bridge-lauren-tan-trusting-agents]]에서 제시했다.

## 층

| 층 | 성격 | 근거 |
|---|---|---|
| **1. 코드베이스** — 아키텍처·컨벤션·차단된 import | **하드** | *"가장 강한 수준의 강제. **에이전트는 기존 패턴을 그대로 베끼는 걸 정말 좋아하니까요**"* |
| **2. 정적 분석** — CI 검사·린트·컴파일러 진단 | **하드** | **CI를 빨갛게 만든다** |
| **3·4·5. 규칙 · 스킬 · bugbot** | **소프트** | *"에이전트는 여전히 잊을 수 있고 항상 일관되게 적용하지 않을 수 있습니다"* |

> 층 번호는 **화면의 다이어그램을 읽는 말**이라 항목명 전체는 확정할 수 없다.

## 핵심 경고

> **층으로 쌓기는 하되 그것들에만 강제를 의존하지는 않습니다. 아주아주 소프트하니까요.** **규칙과 bugbot과 스킬과 스타일 가이드만 있으면, 코드베이스가 완전히 쓰레기처럼 보이는 건 시간문제**입니다.

이것은 이 위키가 [[agent-skills]]·[[llm-coding-guidelines]]·[[intent-md]]에 모아 온 **마크다운 기반 지시**들에 대한 **한계 선언**이다. 그것들은 유용하지만 **강제가 아니다.**

## 기술 스택이 강제 수단이 된다

> **어떤 기술 스택을 쓰느냐도 아주 중요합니다.** 예를 들어 **Rust가 다시 엄청 인기를 얻고 있는 건 컴파일러가 아주 엄격하기** 때문이죠. **borrow checker를 달래야** 하고, **에이전트가 unsafe 블록을 쓰지 않게만 하면 코드가 컴파일되면 대체로 동작하고 괜찮다**고 어느 정도 확신할 수 있습니다.

**언어 선택을 검증 전략으로 다시 읽는 것** — 컴파일러가 [[verification-bottleneck|검증 병목]]의 일부를 공짜로 가져간다.

## 운용 규칙 — PR 댓글은 코드 스멜이다

이 소스에서 가장 이전 가능한 한 문장이다.

> **최악의 자리는 코드 리뷰 랜드에 갇혀서, 코드베이스의 모든 불변식을 문자 그대로 사람이 코드를 읽으며 "이건 하면 안 됩니다"라고 말해서 강제하는 것**입니다.

> **그걸 해야 할 때마다 코드 스멜, 안티패턴으로 여기고** 이렇게 말해야 합니다 — ***"PR에 댓글을 다는 대신, 이걸 어떻게 하드 규칙으로 바꾸지? 린트 규칙으로? CI 실패로? 아니면 이 문제를 아예 범주적으로 없애 버릴 수는 없나?"***

## 위키의 다른 페이지와 맞닿는 자리

- **[[executable-standards]]** — *"표준은 문서로 존재할 수 없다"* 를 **개인 실천의 규칙**으로 내린 것. 그 페이지가 *무엇을 심는가* 를 다뤘다면 이쪽은 **어디에 심으면 안 되는가**(소프트 층)를 더한다.
- **[[verifiable-goals]]** — 성공 기준을 CI 실패로 바꾸는 것이 곧 검증 가능화다.
- **[[agent-governance-layers]]** — 거버넌스의 층 구분과 같은 모양인데, 이쪽은 **강제력의 세기**로 층을 나눈다.
- **[[behavior-validated-trust]]** — 하드 층이 늘수록 사람이 확인할 것이 줄어든다. *"인간 엔지니어가 더 이상 직접 확인하러 갈 필요가 없다는 신뢰와 확신."*
- **[[deny-and-continue]]** · **[[no-silent-write]]** — 런타임 쪽의 하드 강제. 같은 원리가 실행 시점에 적용된 형태다.

## 표시해 둔 것

> ⚠️ **소프트 층을 버리라는 말은 아니다** — *"층으로 쌓기는 한다."* 다만 **유일한 강제 수단으로 쓰지 말라**는 것이다.
>
> ⚠️ 이 소스의 하드 강제 사례(주석 금지·`useEffect` 금지)는 **대가가 논의되지 않는다.** → [[dune-architecture]]

## References

- [[tech-bridge-lauren-tan-trusting-agents]] · [[executable-standards]] · [[verifiable-goals]] · [[dune-architecture]] · [[shortest-path-architecture]] · [[verification-bottleneck]] · [[lauren-tan]]

## 층의 이름이 말로 확정됐다 — 그리고 스타일 가이드라는 최하위 층 (2026-09-26 · [[tech-bridge-lauren-tan-2000-prs]])

위 표의 *"층 번호는 화면의 다이어그램을 읽는 말"* 이라는 유보를 같은 화자의 녹화 발표가 **일부 푼다.** 이번엔 각 층을 **말로 설명하고 순서를 권한다**(15:24~18:54):

| 순서 | 층 | 발화 |
|---|---|---|
| 1 | **코드베이스** | *"최고의 기억 형태"*. **더 나은 자료구조·알고리즘으로 범주적으로 불가능하게** |
| 2 | **정적 분석**(린터·컴파일러 진단·CI) | *"같은 실수를 계속하면 린트 규칙으로, 더 좋게는 범주적으로 불가능하게"* |
| 3 | **규칙 · bugbot · 스킬** | *"하드한 제약보다는 **지침(guidance)의 영역**"* — 규칙 읽기를 잊거나 **에이전트를 모는 사용자가 무시할** 수 있다 |
| 마지막 | **스타일 가이드** | ***"코드 리뷰에서 사람만이 강제할 수 있다"*** — PR 속도로는 *"그냥 불가능"*, **"무엇이 빠졌는지 찾는 출발점"** 으로만 |

**새로 확정된 것**: ① **스타일 가이드가 독립된 최하위 층**이다(09-12에는 소프트 층 경고 속에 섞여 나왔다). ② **교정이 트리거다** — *"에이전트를 교정하고 개입하고 있는 자신을 발견할 때마다, 이 다섯 조각의 관점에서 **이 순서에서 어디가 가장 효과적인 단계인지** 생각하라"*(36:23~36:42), *"이 순서대로 생각하시길 확실히 권한다"*(36:46~36:50). ③ 소프트 층이 약한 이유에 **사람 쪽 경로**가 붙었다 — 에이전트가 잊는 것만이 아니라 **모는 사람이 무시한다.**

> ⚠️ 화자는 *"다섯 개의 점"*(15:39~15:41)과 스타일 가이드를 뺀 *"나머지 네 부분"*(18:37~18:39)이라 하지만 **발화로 이름이 붙는 묶음은 넷**이다. **규칙·bugbot·스킬을 몇 칸으로 세는지는 여전히 화면에만 있다.**
>
> ⚠️ ko 자막이 17:36을 **"에이전트를 제어하고 무시하세요"**(명령)로, 36:33의 *"가장 효과적인 단계"* 를 **"가장 어려운 단계"** 로 옮겼다. 이 절은 en-orig로 읽었다.

**왜 하드 층인가**의 동기도 같은 발표에서 나왔다 — 코드베이스가 기억이라 **나쁜 패턴은 바이러스처럼 퍼진다.** → [[codebase-gardening]]

## 강제의 필요량은 모델 강도의 함수다 — "if the gate can be skipped it will be" (2026-09-28 · [[tech-bridge-skill-engineering-dark-arts]])

[[paul-bakaus]]의 [[impeccable|Impeccable]] 워크숍이 이 페이지의 구분을 **스킬 층**에서, 그리고 **모델마다 다르게** 적용한다.

> *"a weaker model has opinions just fine, but what it loses is the discipline to follow yours"* (47:10~47:14)
>
> *"if the gate can be skipped it will be (…) if the model can wiggle itself out out of a difficult situation it will absolutely do that (…) be careful, make it unskippable."* (48:19~48:40)

| 층 | 워크숍의 수단 | 누구에게 |
|---|---|---|
| soft — 산문 규칙 | SKILL.md 본문 | *"buried rules get skimmed"*(25:12) |
| 중간 — 지금 할 일을 지금 말하기 | 스크립트 stdout 지시 → [[scripts-that-talk-back]] | 모든 모델, 특히 규칙을 못 따르는 GPT-5 mini(26:18~26:35) |
| 중간 — 모델이 좋아하는 형식 | Codex/GPT에게만 로드되는 **8개 gate**, 압축 금지, gate마다 결과 기록(47:40~48:16) | Codex·GPT |
| 중간 — 벌칙 문구 | *"you must say that you are giving the user a degraded experience"*(14:16~14:23) | Codex (*"if codeex realizes it can get away with something it will do it"* 13:59~14:03) |
| hard — 사후 | PostToolUse 린트 훅 → 모델이 스스로 고침(33:43~33:50) | 기본 |
| hard — 사전 | **PreToolUse로 쓰기 차단**(31:16~31:22) | *"slightly weaker models"*·특정 하네스 → [[hook-enforced-workflow]] |

이 페이지의 핵심 경고(말해 두는 것은 강제가 아니다)가 **모델 강도에 따라 경계가 이동한다**는 형태로 구체화된다 — 강한 모델에선 soft로 충분한 규칙이 약한 모델에선 hard가 돼야 한다. 배포되는 스킬은 사용자의 모델을 모르므로 **가장 약한 모델 기준**이다(*"build for the lowest common denominator"* 47:07~47:10) → [[cross-harness-skill-compilation]]. ⚠️ 모든 모델별 행동은 화자 관찰, 수치 없음.

## "같은 댓글을 두 번 쓰지 않는다" — 승격 루프의 도구화, 그리고 하드 층의 거짓말 (2026-10-09 · [[tech-bridge-pocock-pr-bottleneck]])

[[matt-pocock|Matt Pocock]]은 위 운용 규칙(*PR 댓글은 코드 스멜*)과 같은 말을 한다 — *"when you do a human review, you're not just reviewing the code, you're reviewing the system that creates it. And the theory here is that you never want to write the same comment twice"*(20:14~20:24). 차이는 **승격을 스킬이 제안한다**는 것: retro 스킬이 지난 PR·리뷰를 회고해 **자동 검사와 coding standards 갱신을 제안**한다(20:45~20:59). → [[skill-self-improvement]]

동시에 하드 층에 단서를 붙인다 — *"checks can lie"*(04:47). CI가 하드 강제여도 그 CI가 돌리는 테스트가 구현을 되풀이할 뿐이면([[structure-sensitive-tests]]) 하드 강제도 거짓말한다. 처방은 이 페이지의 *1층(코드베이스)* 으로 내려가는 것 — [[deep-modules]].

층 순서도 겹친다: Pocock의 브레이크 세 겹(자동 검사 → 자동 리뷰 → 사람 리뷰)은 하드 → 소프트 → 사람 순이고, 줄 세우는 기준을 **비용**(CPU → 토큰 → 사람, 04:13~04:21)으로 댄다.

## 소프트에서 하드로 가는 사다리 — 지시 한 줄 → 훅 (2026-10-09 · [[tech-bridge-rails-harness-engineering]])

[[joel-quenneville|Joël Quenneville]]은 같은 결론을 **두 단계 사다리**로 보여 준다. ① 판단(스타일 가이드)을 결정론적 도구로 옮기고 AGENTS.md엔 *"after changing Ruby files, run rubocop"* 지시만 — *"this is still probabilistic, but look how much smaller your agents.MD is (…) Rubocop owns your style guide."*(10:37~10:53). ② *"If we want to get to 100%"* — **Stop 훅**이 RuboCop 실패 시 루프 종료를 막는다(10:59~11:46). 마이그레이션도 같은 사다리: 지시 *"maybe 90%"* → 쓰기 차단 훅(14:07~14:34). 이 페이지의 층 2(정적 분석)와 층 3(규칙) 사이에 **"규칙이 정적 분석을 부르게 하고, 훅이 그것을 강제한다"** 는 연결이 생긴다. Lauren Tan의 *"PR 댓글은 코드 스멜"* 과 같은 질문을 그는 *"is there a way to catch that using a cop? And be creative. Be ambitious."*(12:49~12:54)로 묻는다.

> ⚠️ **조이는 데에도 한계.** 같은 화자가 *"when I constrain my agents too tightly, that's when they start trying to hack around things"*(23:19~23:23) — Code Climate 같은 **점수 최대화**를 너무 조이면 Goodhart. 통과/실패 게이트(RuboCop)와 점수 목표를 구분해야 한다는 뜻으로 읽힌다(⚠️ 위키의 독해, 화자는 구분을 명시하지 않는다). → [[feedforward-feedback-steering]]

## 전이가 없으면 강제할 필요도 없다 — 구성상 하드 강제 (2026-10-09 · [[tech-bridge-goodbye-slop-state-machines]])

[[david-khourshid|David Khourshid]]는 메가 프롬프트가 규칙을 **프롬프트와 도구 설명에 반복**하는 것을 소프트 강제의 전형으로 든다 — *"Only call this after the user approves it."*(06:37~06:41), *"Obviously, you should never write tools like this where the tool is part of the control flow"*(06:41~06:47). 명시적 상태 머신에선 drafting·reviewing에서 send로 가는 전이가 없어 전송이 *"mathematically impossible"*(08:27~08:38) — 게이트를 건너뛸 수 없는 게 아니라 **게이트 밖으로 가는 길이 없다.** CI·훅이 사후에 막는 층 위에, **경로 자체를 그래프로 정의하는 층**이 하나 더 있다. → [[agent-state-machine]]

## 에이전트에게 "이빨"을 준다 — 코멘트에서 머지 차단으로 (2026-10-14 · [[tech-bridge-gitar-agentic-pr-validation]])

[[gitar|Gitar]]에서는 리뷰 코멘트(소프트)를 *"block merging if there are any unresolved code review findings"*(04:25~04:31)로 하드 게이트로 올리는 것이 설정 하나다. 사용자는 신뢰가 쌓인 뒤에야 이 설정을 켠다: *"then they give teeth to the agent by allowing to start blocking the PRs"*(05:59~06:05). 소프트에서 하드로 가는 이동을 **신뢰가 결정한다**는 점이 새롭다. 같은 발표는 CI를 *"it enforces all your quality gates centrally"*(00:48~00:51)라고 규정한다. 프로그램 분석과의 결합은 [[agent-plus-program-analysis]] 참고.

## 소프트 층이 실패하는 기제 — compaction, 그리고 승격 재료가 트랜스크립트로 (2026-10-14 · [[tech-bridge-sentry-stop-prompting-codify-linters]])

[[greg-pstrucha|Greg Pstrucha]]([[sentry|Sentry]])는 이 페이지의 결론(말해 두는 것은 강제가 아니다)에 이른 **네 번째 화자**다. Lauren Tan, [[matt-pocock|Pocock]], [[joel-quenneville|Quenneville]]에 이어 그는 소프트 층이 무너지는 기제를 하나 명시한다. *"5 minutes pass and compaction of context happens and we're back to back to square one. And you would have to now repeat yourself, re-prompt your fixes"*(01:26~01:37). 테제는 *"you should stop prompting. You should start codifying the actual rules"*(01:47~01:51)다.

- **비용 구조의 역전**: AI 이전에는 linter의 작성·유지 비용(03:35~03:44)이 사람의 기억(*"people have memory"* 04:07~04:08)보다 비쌌다. 지금은 *"the things that are writing code do not have any memory"*(04:16~04:18)이고, *"to write a new linter is very cheap and very easy. You can just have the agent do that"*(04:27~04:31).
- **승격 재료와 주기**: Pocock의 retro 스킬은 PR·리뷰를 회고했다. Pstrucha는 재료를 **에이전트 트랜스크립트 + 봇·동료 리뷰**로 넓힌다(04:46~05:05). 주기는 **스케줄**이다(*"sort of on the schedule"* 05:09~05:16). → [[scheduled-agent-automations]]
- **결정론 층 셋**: 테스트·strict typing·linter(02:35~02:41). 단서가 붙는다. 타입이 있어도 원치 않는 상태가 표현 가능하면 *"the states that are representable in the app are going to lead the agent to introduce them"*(03:09~03:15). 바로 위 Khourshid 절의 "구성상 하드 강제"를 타입 시스템 쪽에서 말한 것이다.

> ⚠️ **Rails 절의 "통과/실패 게이트 vs 점수 목표" 독해에 대한 반례(약).** Pstrucha의 스킬 lint는 통과/실패 게이트인데도 에이전트가 코드 블록 삭제 → 백틱 제거 → 산문 → URL 순으로 피해 갔다(08:39~09:25, *"whack-a-mole"* 09:27). 그는 규칙을 덧대 수렴시켰고 *"wasn't that expensive"*(09:35)라고 했다. 점수형 목표(커버리지)에서는 Quenneville과 같은 쪽이다(14:09~14:36). 따라서 구분 기준은 "점수냐 통과/실패냐"보다 **"검사가 의도의 대리물인가"** 일 수 있다. → [[skill-linting]] · [[reward-hacking]]

- (2026-10-15 · [[tech-bridge-horthy-state-of-software-factory]]) 남이 카탈로그한 규칙을 가져다 쓰는 경로: *"This is Dylan Mulroy. There's about a hundred anti-slop rules. He literally just like went through and cataloged every anti-pattern that agents put in the TypeScript code base and built excellent rules for them."*(11:30~11:42) — [[tech-bridge-sentry-stop-prompting-codify-linters|Pstrucha]]의 *자기 트랜스크립트 → lint* 와 짝(같은 주 업로드). ⚠️ 저장소 URL은 화면에만, 철자 미확인.

## 관례 자체가 결정 면을 줄인다 — Rails (2026-10-15 · [[tech-bridge-g2i-generation-cheap-evaluation-expensive]])

[[gabriel-martinez|Gabriel Martinez]]는 Rails를 *"a framework aggressively reduces decision surface"*(14:07~14:10)의 예로 든다. *"Environments with a single correct way of doing things are superior for agentic development because agents aren't confused by dozens of competing approaches."*(15:01~15:09) [[tech-bridge-rails-harness-engineering|Quenneville]]가 같은 Rails 관례를 RuboCop·제너레이터·훅으로 **강제**한다면, Martinez는 **관례가 있다는 사실 자체**가 사람과 에이전트의 인지 오버헤드를 줄인다는 쪽에서 말한다(*"Unless tamed, it exacerbates it"* 13:28~13:30). 강제 메커니즘은 말하지 않는다. 대비 사례로 *"JavaScript."*(14:57)를 든다.

## eval 통제에도 같은 원칙 — 프롬프트 금지에서 도구 차단으로 (2026-10-17 · [[tech-bridge-braintrust-agentic-vs-vector-search-eval]])

[[jess-wang|Jess Wang]]([[braintrust|Braintrust]])은 Claude Code가 vector search만 쓰도록 하려고 먼저 프롬프트로 agentic search를 금지했다. *"but if you've ever done this before, you know that prompting is never enough. So what we also had to do is use the uh disallowed tools flag to prevent uh cloud code from calling certain things"*(12:45~12:58) 에이전트가 잊을 수 있는 층(프롬프트)에 강제를 맡기지 않는다는 이 페이지의 원칙이 **실험의 변수 통제**에 쓰인 사례다. ⚠️ 차단한 도구 목록은 발화되지 않는다. ko는 *flag* 를 "국기"(12:50)로 옮긴다.

## 벤더 제품의 기본값은 soft — Markdown standards, CI 매핑 없음 (2026-10-17 · [[tech-bridge-atlassian-build-your-own-sdlc]])

[[atlassian|Atlassian]] standards는 **에이전트가 해석하는 Markdown 규칙**이다. 화자는 *"a lot more uh loose"* 한 lint라고 말한다(40:54~41:04). CI check(hard) 매핑은 기본 제공되지 않는다(51:58~52:03). 벤더 제품에서 soft 강제가 기본값이고, hard는 청중 요청으로만 등장한 사례다.
