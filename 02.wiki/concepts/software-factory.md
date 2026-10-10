---
title: "소프트웨어 팩토리 (Software Factory)"
type: concept
category: architecture
tags: [software-factory, autonomy, sdlc, orchestrator-worker-validator, model-routing, verification, continuous-improvement, agent-org, factory-engineering, skill-loop, data-plane, open-source]
related: [orchestras-not-factories, defense-factory, loop-is-the-product, automatic-model-routing, deferred-tool-context, agent-readiness, generator-evaluator-pattern, sprint-contract, agent-swarm, verifiable-goals, reward-hacking, agent-org-adoption, outcome-engineering, codebase-gardening, model-mixing-economics, verification-bottleneck, factory-engineering, build-in-the-open, skill-self-improvement, spec-driven-development, risk-proportional-human-review, slop-cannon, automated-code-review]
first-seen: tech-bridge-factory-software-factory
sources: [tech-bridge-factory-software-factory, tech-bridge-conductor-orchestras-not-factories, tech-bridge-warp-factory-engineering, tech-bridge-pocock-pr-bottleneck, tech-bridge-kent-beck-craft-augmented-development, tech-bridge-agentcraft-strategy-game, tech-bridge-lauren-tan-pocock-podcast-full]
created: 2026-10-02
updated: 2026-10-10
---

# 소프트웨어 팩토리 (Software Factory)

**코드 생성만이 아니라 신호 수집 → 우선순위 → 오케스트레이션 → 실행 → 검증 → 프로덕션 테스트 → 반복 → 학습까지, 소프트웨어 개발 생애주기 전체를 에이전트가 자율로 도는 루프.** 이 위키에서는 [[factory-ai|Factory]]의 [[tereza-tizkova|Tereza Tížková]]가 [[tech-bridge-factory-software-factory]]에서 처음 정의를 달았다.

> *"I would define the software factory as the whole loop the whole life cycle of developing software with autonomy which doesn't mean just coding and generating code by that I mean collecting all the signals reacting to user feedback to logs prioritizing what's important then orchestrating it all executing validating doing really good uh testing in production and then iterating on all this uh while also continuously improving in the process"* (00:47~01:18)

> ⚠️ **정의의 출처가 하나, 그것도 벤더다.** 화자는 "software factory"를 제품 이름 겸 범주로 파는 회사 소속이다. 용어 자체는 그보다 넓게 쓰인다(*"everyone is talking about software factory but only few people are actually building one"* 00:05~00:13). 이 페이지의 구조·수치는 **Factory의 정의**이고, 다른 화자가 같은 말을 다르게 쓰면 아래에 추가한다. → 두 번째 벤더 정의는 아래 **"두 번째 정의 — Warp"** 섹션([[tech-bridge-warp-factory-engineering]]).

## 아닌 것으로 정의하기

| 아닌 것 | 이유 (en-orig) |
|---|---|
| **코딩 에이전트** | *"generating code writing code that's the easy part compared to all the others"*(02:27~02:32) |
| **코딩 에이전트 스웜** | *"it's not even a swarm of coding agents even thousands of agents"*(02:25~02:29) — 수를 늘리는 것이 정의가 아니다 |
| **컨설팅·추상 전략** | *"you can't invite a consultancy and just throw something in the middle of your organization. You should really be mindful and rebuild it from scratch"*(03:01~03:09) |

## 왜 지금인가

2023년 무렵 AutoGPT·BabyAGI가 이미 *반복하는 루프*를 시도했지만 환각·컨텍스트 길이·추론 품질, 그리고 *"good environments where the agents can actually work in the isolation"*(02:03~02:07)이 없어서 안 됐다. 화자가 든 지금의 조건은 그 역 — 특히 **컴퓨터 사용과 에이전트용 영속 VM**(14:13~14:25)이 실행형 검증을 가능하게 했다.

## 3원칙

Tereza는 소프트웨어 팩토리 짓기를 **사람 팀을 꾸리는 일**에 빗댄다 — 에이전트가 많아지면 *"it all can end up as a big chaos"*(03:28~03:31).

### ① Agnostic — 모델·도구·업무 방식에 비종속

- 기존 환경(Slack·GitHub)에 붙고 기존 구독을 가져오게 한다 — 누가 이길지 예측할 수 없으니까(04:40~05:03)
- 모델 비종속의 구현이 [[automatic-model-routing]] — 난이도 분류 → 임계값 → **임계값 위 최저가 모델**, 실패·공급자 장애 시 전환. ⚠️ *"for example 25%"* 절감(07:03~07:07, 벤더 벤치마크)
- 비용 쪽 레버: 사람별 기본 모델, 캐싱, 한도 대신 결과 확인, 라우팅(Coinbase 사례, 05:36~06:06) → [[model-mixing-economics]]

### ② Autonomous — 오래 믿고 맡긴다

- 권한·거버넌스를 주고 *"trust it to run really for a long time"*(03:49~03:53). ⚠️ *"a year or more years without the human in the loop"* 는 출처 없는 **예측**(03:53~03:58)
- 핵심 난제는 루프가 아니라 **완료의 정의** — *"how you define what it means to be done in the loop"*(10:03~10:05), 과제가 비결정적·열린 세계라서. 잘못 정의하면 테스트만 통과하는 **cheating**(11:08~11:23) → [[verifiable-goals]] · [[reward-hacking]]
- 구현: **Missions** (아래)

### ③ Always improving — 사람 조직처럼 배운다

- 새 팀원 온보딩처럼 코드베이스 이해·구조·문서를 주고, 배운 것을 팀에 공유하게(04:09~04:27)
- 도구 bloat → [[deferred-tool-context]] (⚠️ *"50% of tokens or more"*)
- 준비 안 된 코드베이스는 AI로 더 나빠진다(power law) → [[agent-readiness]] · [[codebase-gardening]]
- 관찰로만 배우는 암묵지 → plugins(스킬+컨텍스트 패키지)·AutoWiki(문서 자동 갱신) → [[agent-skills]] · [[llm-wiki-pattern]]

## 실행 구조 — Missions (orchestrator → sequential workers → validators)

```
오케스트레이터 ── validation contract(코드 전에 작성) ──┐
   │                                                    │
   ▼                                                    ▼
워커 1 → 워커 2 → 워커 3 …  (순차, 각자 병렬 서브에이전트)  →  검증자
   ▲                                                    │  scrutiny: 코드·린터·타입·테스트
   └──────────────── 피드백, 처음으로 ───────────────────┘  user testing: 가상 컴퓨터에서 클릭
```

- **순차** — *"they don't work in a swarm or parallel"*, 이유는 *"more fresh context and kind of fresh head"*(12:17~12:32). 동료가 코드를 봐 주는 것과 같다
- **검증자는 남이 쓴 코드를 판정** — *"the validators judge code that they didn't write"*(13:01~13:07) → [[generator-evaluator-pattern]]
- **validation contract** — 오케스트레이터가 *"written before any code is done"*(13:07~13:14) → [[sprint-contract]]
- **두 검증자** — 정적(scrutiny)과 실행형(user testing). 실행형은 *"doesn't care how it was made"*(13:35~13:38) — 결과만 본다 → [[agent-visual-qa]]
- ⚠️ 고객 미션 16시간 중 **검증 40%**(11:51~12:02, 1건) — 검증이 비용의 큰 몫이라는 [[verification-bottleneck]]과 같은 방향의 일화
- *"it's just a loop with smaller loops"*(14:47~14:49)

## 사람의 자리

추상화 사다리 — 사람이 계산기였던 시절 → 프로그래밍 언어 → 코딩 에이전트(가까이서 감시) → 소프트웨어 팩토리(*"we just monitor and decide what to build"* 20:48~20:51). ⭐ **사람은 what, 에이전트는 how**(20:54~21:02). 에이전트가 가져가는 것은 멋진 일이 아니라 정렬·회의·상태 공유(21:15~21:39). → [[outcome-engineering]]

## 비슷한 이름과의 구분

| | **소프트웨어 팩토리** (Factory) | **[[defense-factory\|방어 공장]]** (OpenAI) |
|---|---|---|
| 범위 | 개발 생애주기 전체 | 보안 — 발견·분류·교정·배포·검증 |
| 트리거 | 사용자 피드백·로그 등 신호 | **새 모델 릴리스**(새 사이버 역량) |
| 끝 | 프로덕션 테스트 → 반복 → 학습 | 검증 → 다음 모델 세대에서 다시 |
| 공통 | 사람 없이 **검증으로 닫히는** 상시 루프, "기계 속도" 지향 | 〃 |

방어 공장은 소프트웨어 팩토리의 **한 전문화된 라인**으로 볼 수도 있지만, 두 소스는 서로를 언급하지 않는다. → 둘을 같은 개념으로 묶지 않는다.

**[[loop-is-the-product]]**(Introspection)도 *신호 → 행동 → 검증 + 두 번째 개선 루프*로 거의 같은 골격을 말한다 — 차이는 단위: 그쪽은 **에이전트 제품 하나의 루프**, 이쪽은 **조직의 개발 공정 전체**.

## 긴장과 미해결

> ⚠️ **Contradiction: 스웜 대 순차.** [[agent-swarm]]은 문제를 쪼개 병렬로 주는 패턴을 다루고, OpenAI는 에이전트 1만 개를 말한다([[tech-bridge-brockman-agi-era-defender-window]]). Factory는 정의상 스웜을 배제하고 상위 흐름을 **순차**로 둔다(하위 잡일은 병렬 허용). 측정 비교는 어느 쪽도 없다.

- **"직접 지을까, 외주를 줄까"** — 화자가 의제로 꺼냈지만 답은 *"rebuild from scratch"* 뿐.
- **비용** — 의제 *"how much is this all going to cost?"*(00:26~00:29)에 대한 답은 라우팅·캐싱·지연 로딩의 **절감률**이지 총비용이 아니다. 검증 40%가 비용에서 차지하는 몫도 없음.
- **검증자의 독립성** — 다른 모델·다른 프롬프트인지 미발화.
- **사람이 루프에 언제 들어오는가** — *"monitor and decide what to build"* 외 승인 게이트·중단 조건이 없다. → [[risk-proportional-human-review]]

## 반론 — "공장이 아니라 오케스트라" (2026-10-02 · [[tech-bridge-conductor-orchestras-not-factories]])

[[charlie-holtz|Charlie Holtz]]([[conductor|Conductor]])는 같은 행사의 software factory 트랙 안에서 *"I honestly kind of hate the term. I think it's the wrong way of thinking about these new tools"*(14:26~14:34)라 하고, 사람이 *"factory line managers like pushing buttons"*(15:20~15:24)가 아니라 지휘봉을 든 지휘자로 사람·에이전트 혼성 팀을 이끌며 원할 때만 줌인하는 그림을 제시한다 → [[orchestras-not-factories]]. 근거는 측정이 아니라 10년 전 *"feature factories (…) just doesn't work"*(15:28~15:33)라는 일화와 도구 제작자의 언어 책임이다. ⚠️ 화자 회사명이 곧 그 은유(Conductor)이고, 그의 제품도 병렬 에이전트 관리 도구다. 같은 날 ingest된 이 페이지의 first-seen 소스(Factory)와 **같은 날 업로드**됐지만 서로를 언급하지 않는다.

## 두 번째 정의 — Warp: "SDLC 그 자체" (2026-10-03 · [[tech-bridge-warp-factory-engineering]])

[[warp|Warp]]의 [[zach-lloyd|Zach Lloyd]]는 같은 말을 **더 낮게** 정의한다 — *"There's nothing that complicated about loops. (…) This loop could literally just say like the software development life cycle. It's the same thing."*(03:15~03:25) 그리고 **채택 예측**을 붙인다: *"every company every open-source project will have at its core a software factory, kind of like the way that CI/CD became just like, "Oh, of course you have that.""*(08:33~08:44) ⚠️ 이 화자도 공장 인프라(Warp 에이전트 플랫폼)를 파는 쪽이고, 측정치는 없다.

**루프와 사람 칸**(03:25~03:50):

```
아이디어 → [에이전트] triage ─(쉽고 모호하지 않음)→ 바로 구현
                 └─(어려움)→ [에이전트] product spec + tech spec → [사람] spec 리뷰
→ [에이전트] 구현(클라우드) → [사람+에이전트] 코드 리뷰 → [에이전트] 검증(computer use·영상·스크린샷)
→ [사람] 제품 리뷰 → 출시 → [에이전트] 모니터링(크래시? 쓰이나?) → 맨 위로
```

**구성요소 넷**(07:51~08:13): 자동화 · 컨텍스트와 스킬 · 적시에 사람(*"when things get stuck on the factory"*) · 자기개선 루프.

**아키텍처**(12:22~13:11): 여러 입구(task tracker·Slack·Teams·터미널/IDE·모니터링) → **control plane**(일 분배) → **클라우드 샌드박스**(어느 harness·어느 model) → 그 아래 ⭐ **data plane** — *"something that lets agents remember what they've done, learn, um improve over time"*(13:01~13:11).

**측정과 skill loop**(13:11~14:35): 효율 = 출시량 대비 *"human time and token time"*(13:32~13:40). 루프의 전형은 **skill loop** — 공장 에이전트가 스킬을 돌리고 **observer 에이전트**가 적용을 지켜보며 스킬을 고친다; 예: 시니어가 리뷰 에이전트의 코멘트를 교정하면 observer가 다음 실행을 위해 리뷰 에이전트를 개선(14:17~14:33). → [[skill-self-improvement]]

**지을까 살까**: Uber는 내부 버전을 지었다(11:53~12:01, 같은 행사의 다른 발표). 그러나 *"to build a thing that actually scales is probably like you should probably focusing on your own product, not building this infrastructure"*(12:09~12:18) — 엔지니어링은 **튜닝**(*"are these the right skills for my domain?"* 17:09~17:14)에 남는다. → [[factory-engineering]]

**오픈소스 운영에 쓰기**: Warp는 5년 closed 끝에 오픈소스로 전환했고, 이유 하나가 **공개 공장** build.warp.dev였다(04:19~04:49). 노이즈 이슈·sloppy PR·리뷰 지옥을 공장으로 감당한다. → [[build-in-the-open]]

### Factory 정의와 비교

| | **Factory** (Tereza Tížková) | **Warp** (Zach Lloyd) |
|---|---|---|
| 정의의 높이 | 조직을 *"rebuild it from scratch"* | *"the software development life cycle. It's the same thing"* |
| 사람의 자리 | 루프 밖 — *"monitor and decide what to build"*, *"a year or more"* 무인 예측 | **루프 안 세 칸** — spec·코드·제품 리뷰. 코드 리뷰 투입은 리스크 관리(11:05~11:10) |
| spec | 오케스트레이터의 **validation contract**(코드 전) | 어려운 이슈만 **product spec(불변식) + tech spec(아키텍처)** |
| 검증 | scrutiny + user testing validator(가상 컴퓨터 클릭) | computer use로 영상·스크린샷, CI/CD |
| 개선 | deferred context · Agent Readiness · plugins/AutoWiki | **data plane** + **skill loop**(observer 에이전트) |
| 출시 후 | 프로덕션 테스트 → 반복 | **모니터링 에이전트**가 크래시·사용을 보고 맨 위로 |
| 짓기 | 처음부터 다시 | 대부분은 사서 **튜닝** |
| 측정 | 벤더 수치(25%·50%·40%) | 없음 — 효율 지표의 *정의*만 |

> ⚠️ **Contradiction: 사람 게이트의 위치.** 같은 "software factory" 아래 Factory는 사람을 **루프 밖 감독자**로(무인 1년 이상 예측), Warp는 **루프 안 고정 리뷰 칸**으로 둔다. 어느 쪽이 결과가 나은지 측정은 양쪽 다 없다.

> ⚠️ **Contradiction: 직접 지을까.** Factory: *"rebuild it from scratch"*(조직 재설계). Warp: 공장 인프라는 짓지 말고 핵심 제품에 집중, 튜닝만. 둘 다 그 인프라를 파는 회사다.

**은유에 대해**: Zach Lloyd는 공장 은유가 *"mechanizing or dehumanizing"* 으로 들릴 수 있음을 인정하면서도 *"leaning into it"*(19:14~19:23) — 핵심은 *"are you building something useful?"* 이고 taste가 들어가는 touch point는 사람 몫이라 한다. 위 Conductor 반론과 **사람이 중심**이라는 결론은 같고, 은유의 선택만 갈린다. → [[orchestras-not-factories]]

## 가속기와 브레이크 — Pocock (2026-10-09 · [[tech-bridge-pocock-pr-bottleneck]])

[[matt-pocock|Matt Pocock]]은 이 말을 *"probably the biggest buzz word of the day"*(01:02~01:05)로 부르며 두 축으로 나눈다. **가속기** — 사람이 아니라 결정론적 코드가 작업을 촉발한다(*"a classifier like Jev"* 가 이슈를 fix·reproduction으로 분류, PlanetScale의 느린 쿼리 리포트가 다른 작업을 띄움 — 01:48~02:05; *"All of this is not humans triggering it. It's uh deterministic code triggering it"* 02:06~02:12). **브레이크** — *"mechanisms that slow down, that increase quality"*(02:35~02:38), 세 겹: 자동 검사(CPU) → 자동 리뷰(토큰) → 사람 리뷰. 브레이크가 없으면 [[slop-cannon]](02:18~02:26).

| | Factory (Tížková) | Warp (Lloyd) | **Pocock** |
|---|---|---|---|
| 정의의 축 | 생애주기 전체의 자율 루프 | SDLC 그 자체를 짓는 일 | **가속기 vs 브레이크** |
| 리뷰 칸 | validators | *"the most painful part"* — 에이전트 먼저, 사람은 리스크 관리 | **발표 전체** — 브레이크 세 겹, one-way door만 전부 사람 |

⚠️ 01:20~01:48 자막 공백 — 가속기 목록 앞부분이 비어 있다.

## 반론 2 — "다크 팩토리는 언제나 탈선한다" (2026-10-09 · [[tech-bridge-kent-beck-craft-augmented-development]])

[[kent-beck|Kent Beck]]: *"anytime I've tried fully agentic the dark factory the dark software factory (…) there's no human involved There's no feedback. And that always goes off the rails. Always."*(30:46~31:17) 그리고 *"It's amazing while it's going off the rails"*(31:19~31:23) — 산출량은 인상적이지만 *"it's still complete crap"*(31:34).

- 이유는 피드백: 더 빠른 도구는 *"can create opportunities for feedback faster than we're prepared to gather that feedback or analyze that feedback"*(30:23~30:32).
- 다크 팩토리에서 배우는 것은 *"how unreliable the genie really is. But we already knew that."*(34:14~34:20)
- [[features-vs-futures]]로 보면 피드백 없는 기능 연속 = futures를 0까지 태우는 가장 빠른 길.

> ⚠️ **Contradiction.** Factory·Warp의 자율 루프(검증자·validator 포함)와 Beck의 *"no human (…) no feedback"* 은 **같은 것을 말하지 않을 수 있다** — Factory의 Missions는 validator를 둔다. Beck은 특정 제품을 겨누지 않고 **본인 경험 일반화**만 말한다(측정 없음). [[orchestras-not-factories]]와 같은 편, 근거는 다르다(역할·즐거움 vs 피드백 부재).

## 이름이 기능을 따라잡다 (2026-10-09 · [[tech-bridge-agentcraft-strategy-game]])

[[agentcraft|AgentCraft]]의 [[ido-salomon|Ido Salomon]]: *"Now it's called software factories, but at the time it was just doing stuff autonomously."*(06:13~06:18) — 오케스트레이터가 의도를 쪼개 로컬 컨테이너에서 격리 실행하고, 루프가 Twitter·GitHub를 훑어 백그라운드로 기능을 만드는 것(06:20~06:54). Factory·Warp의 정의(신호 수집부터 검증·학습까지의 SDLC 루프)보다 **훨씬 좁은 용법**이다 — *사람이 babysit하지 않는 자율 실행* 정도. ⚠️ 이 용법이 퍼지면 이 페이지의 *"아닌 것으로 정의하기"* 가 더 중요해진다(위키의 관찰).

## References

- [[tech-bridge-factory-software-factory]] — first-seen (Tereza Tížková, Factory)
- [[tech-bridge-figma-coding-agents]] — 이전에 한 단어로만 등장(*"계획만 있으면 그 위의 루프·워크플로·'software factory'"*)
- [[factory-ai]] · [[tereza-tizkova]] · [[defense-factory]] · [[loop-is-the-product]] · [[automatic-model-routing]] · [[deferred-tool-context]] · [[agent-readiness]]
- [[tech-bridge-conductor-orchestras-not-factories]] — 반론(Charlie Holtz, Conductor)
- [[tech-bridge-warp-factory-engineering]] — 두 번째 정의(Zach Lloyd, Warp) · [[warp]] · [[zach-lloyd]] · [[factory-engineering]] · [[build-in-the-open]]
- [[tech-bridge-pocock-pr-bottleneck]] — 가속기 vs 브레이크(Matt Pocock) · [[slop-cannon]]
- [[tech-bridge-kent-beck-craft-augmented-development]] — 반론 2(Kent Beck, 다크 팩토리)
- [[tech-bridge-agentcraft-strategy-game]] — 좁은 용법(Ido Salomon, AgentCraft)
- [[tech-bridge-lauren-tan-pocock-podcast-full]] — 다크 팩토리 수용(Lauren Tan, *"It kind of is"*)

## 다크 팩토리 수용 — "It kind of is" (2026-10-10 · [[tech-bridge-lauren-tan-pocock-podcast-full]])

[[matt-pocock|Matt Pocock]]: *"this isn't a dark factory, right? This the lights are on, right?"*(50:44~50:49) — [[lauren-tan|Lauren Tan]]: ***"It kind of is. Yeah, actually."***(50:49). ⚠️ 당사자 진술, 독립 확인 없음.

- **어떤 의미에서 어두운가**: *"if my agents are merging their own pull requests it's sort of become dark where I go to sleep my agents now work 24/7"*(50:56~51:05). 영역별 chief of staff(코디네이터) *"more than 10"*(51:05~51:10), PR마다 verifier 에이전트가 앱을 퍼징하는 [[pstack|Pstack]] *full autopilot*(51:42~52:21), 사람은 *"I'll review it in the morning by looking at my commit history"*(52:49~52:52) 후 되돌리거나 린트 규칙을 더한다.
- **이름에 대한 태도**: 같은 대담 초반 *"I've never really liked the term software factory. Not because you know it's not accurate"*(10:14~10:22) — 싫은 것은 품질·장인정신을 떠올리지 않는 **함의**다. 대안 비유는 미슐랭 주방([[agent-manager-analogy]]), 표본 리뷰에서만 *"the factory analogy is a bit more apt"*(48:47~48:52).
- **진행자의 구분**: 다크 팩토리를 Karpathy의 원래 *vibe coding*(코드가 거의 존재하지 않는 것)으로 읽으면 Lauren의 방식은 반대 — 코드와 환경이 본질(53:45~54:05). Lauren: *"maybe there's a dimmer switch"*(54:11~54:15).

> ⚠️ **Contradiction: 위 "반론 2"(Kent Beck)와.** Beck은 *"no human involved There's no feedback. And that always goes off the rails. Always."* Lauren은 다크 팩토리를 **받아들이고 잘 잔다**(*"I'm sleeping so much better now"* 53:10~53:12). 다만 Lauren의 구조엔 **verifier 에이전트 + 아침의 사람 사후 리뷰 + 환경 교정**이라는 피드백이 있다 — Beck이 겨눈 *"no feedback"* 이 아니다. 둘 다 측정은 없다. 그리고 Lauren 스스로 *"it's very hard to get to this point"*(50:15~50:18), 첫날은 *"very scary"*(53:18~53:20)였다고 한다.
