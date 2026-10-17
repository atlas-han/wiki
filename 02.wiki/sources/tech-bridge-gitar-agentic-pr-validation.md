---
title: "Tech Bridge — AI가 코드를 쏟아내는 시대, 검증은 대체 누가 해야 할까요? (Ali-Reza · Gitar/Sonar): 에이전트형 PR 검증 — 리뷰 → 차단 → autofix → 자동 머지, 그리고 에이전트 + 프로그램 분석"
type: source
tags: [verification-bottleneck, automated-code-review, ci, flaky-tests, autofix, auto-merge, trust-ladder, agent-harness, llm-proxy, program-analysis, static-analysis, sonarqube, platform-team, gitar, sonar, acquisition, vendor-claim, video]
source-url: https://www.youtube.com/watch?v=gnXwThtDnIo
source-type: video
author: Tech Bridge (한영자막 재배포) · 발표 Ali-Reza([[gitar|Gitar]] 공동 창업자, 약 한 달 전까지 CEO — [[sonar|Sonar]]에 인수. 자막엔 이름 *"Ali"* 만, *"Ali-Reza"* 는 설명란, 성은 어디에도 없음) · 행사명 미발화(설명란 ai.engineer 링크 + #AIEngineer → AI Engineer 계열 추정) · 녹화일 미발화
date-published: 2026-10-13
ingested: 2026-10-14
created: 2026-10-14
updated: 2026-10-14
---

# Tech Bridge — AI가 코드를 쏟아내는 시대, 검증은 대체 누가 해야 할까요? (Ali-Reza · Gitar/Sonar)

[[tech-bridge|Tech Bridge]]가 재배포한 **10:54 발표, Q&A 없음, 공식 챕터 17개.** 화자는 [[gitar|Gitar]]의 공동 창업자 [[ali-reza|Ali-Reza]] — 자막엔 *"I'm Ali and um, I'm one of the founders of guitar.ai and previously the CEO up until about a month ago where we were acquired by Sonar and now we are part of Sonar."*(00:02~00:17)까지만 있고, **"Ali-Reza"는 설명란, 성은 어디에도 없다.** 회사명은 en-orig ASR이 *"guitar"* 로 받는다(설명란 `sonarsource.com/products/gitar` 로 Gitar 판독). **Gitar·Sonar는 이 위키에 처음 등장한다.** 테제:

> **CI + 코드 리뷰는 모든 변경이 지나는 중앙 검증 단계이고, 여기서의 실패는 시간·일 단위의 outer loop를 만든다. AI는 PR을 더 많이·더 크게 만들어 이 단계를 마찰점으로 바꾼다 — 팀은 속도를 늦추거나 rubber stamp를 하거나 둘 중 하나다. 답은 검증 단계 전체를 에이전트로 자동화하는 것(리뷰 → 머지 차단 → CI 실패 분석·flaky 탐지 → green까지 자동 수정 → 규칙 기반 자동 승인·머지)이고, 사용자는 신뢰가 쌓이는 만큼 자동화 단계를 올린다. 그리고 에이전트에 전통적 프로그램 분석(taint·control flow·data flow·SCA)을 합치면 어느 한쪽보다 낫다.**

> *"Either you slow down and ask developers to review every PR very carefully or you rubber stamp PRs and you risk incidents in production."* (03:09~03:16) · *"So, what's the answer here? Of course, it's more AI."* (03:27~03:31) · *"as they build trust in the system, they unlock more levels of automation"* (06:27~06:33) · *"AI turns validation into a friction point"* (10:17~10:25)

이 위키에 개념 하나가 생긴다 → [[agent-plus-program-analysis]](신규 제안). 그리고 [[verification-bottleneck]]에 **CI 쪽**에서 온 답(리뷰만이 아니라 CI 실패·flaky·머지까지 한 에이전트로)이, [[agent-trust-curve]]에 **제품 기능으로 구현된 사다리**(리뷰 → 차단 → autofix → 자동 머지)가 붙는다.

ASR·ko 보정: ko는 **결론 문장을 뒤집는다** — *"AI turns validation into a friction point"* → **"AI는 검증을 가능하게 합니다"**(10:19). 머지 차단 조건 *"block merging if there are any unresolved code review findings"* → **"합병이 성사되지 않을 경우 이를 막는"**(04:25, merge → M&A "합병"). CI → **"지능지수(IQ)"**(04:52, 06:56), PR → **"보도자료"**(03:11)·**"홍보 자금"**(07:38), Gitar → **"기타"**(07:50, 악기), *PR당* 고정 가격 → "고정 가격"(08:31, 과금 단위 소실), *by developers* → **"더 나이가 많은 쪽 개발자들"**(09:42), *you lose developer time* → **"개발자들 때문에"** 악화(02:04), *good afternoon* → **"오전"**(00:00). `en`·ko 공유: autofix 단계 → *"automatically approved"*/"PR 승인"(06:07). 전체 목록은 raw.

> ⚠️ **당사자 진술 — 벤더 발표, 수치 0개.** 03:27 이후 거의 전부가 자사 제품 설명이다(*"which is essentially what we built at guitar um that we're now also shipping uh as part of sonar"* 03:33~03:41). **수치·고객 이름·측정 방법·통제 비교가 하나도 없다** — 노이즈(오탐률), flaky 탐지 정확도, autofix 성공률, 자동 머지 비율, 자동 머지 후 회귀율, *"much better quality much better security"*(09:27~09:31)의 근거 모두. 사용자 궤적(05:31~06:39)은 *"we're seeing actually a very interesting trend in our users"* 라는 관찰 진술이다. *"essentially guarantee outcomes at a fixed PR price"*(08:30~08:36)의 가격·보장 범위도 미발화.
>
> ⚠️ **화자 이름.** en-orig *"Ali"*(00:02)뿐. *"Ali-Reza"* 는 설명란 본문(*"Gitar(Sonar)의 공동 창업자 알리레자(Ali-Reza)"*), 성은 **어디에도 없다** — 링크 핸들(`linkedin.com/in/aliadl`, `x.com/aadltaba`)은 성이 *Adl-* 로 시작함을 시사할 뿐이다(⚠️ 추정, 링크는 열어 보지 않았다). 자막과 설명란은 충돌하지 않는다. 현재 Sonar에서의 직함 미발화.
>
> ⚠️ **인수 시점은 상대 시각.** *"up until about a month ago where we were acquired by Sonar"*(00:08~00:14) — 발표일이 발화되지 않으므로 인수 날짜는 이 소스로 정할 수 없다. 금액·조건 미발화. 통합 상태: *"we've been integrating guitar with Sonar Cube[=SonarQube]"*(08:47~08:53) — **진행 중**.
>
> ⚠️ **행사·시점.** 행사명·도시·연도 미발화. 설명란 `https://ai.engineer` 링크 + `#AIEngineer` → **[[ai-engineer|AI Engineer]] 계열 추정**(확정 아님). 현장 단서: *"good afternoon everyone"*(00:00~00:02), *"you've heard a lot in the past few days about the importance of verification in the age of AI"*(00:19~00:24) — 며칠째 이어진 행사에서 검증이 반복 주제였다.

## 1. CI + 코드 리뷰 = 중앙 검증 단계 (00:29~01:43)

- *"in almost all software teams there is this centralized validation phase that is basically CI plus code review."*(00:31~00:36)
- 역할: *"it enforces all your quality gates centrally. So these are security compliance code quality gates. It's on the critical path of getting your changes into production. So the faster is always the better."*(00:48~01:01)
- 규모가 커질수록 느려진다 — *"longer running builds and tasks"*, *"asynchronous team review flows across sides[=sites] and geographies"*(01:05~01:17). 비싸다 — *"a lot of developer infrastructure dollars"*(01:20~01:25), 그래서 *"the main focus of your platform organization team or your platform team"*(01:37~01:43).

→ [[hard-vs-soft-enforcement]](CI = 하드 게이트) · [[harness-as-platform]](플랫폼 팀의 몫)

## 2. 실패의 비용 — outer loop (01:43~02:38)

- ⭐ *"any kind of failure in this phase is very expensive. It introduces failures introduce an outer loop that are typically measured in hours and days."*(01:47~01:59) — *"you lose developer time and that's compounded by disruptions to your flow state."*(02:00~02:10)
- 최적화도 비싸다: *"a lot of fragmented systems that have been integrated together with bespoke configuration and scripting"*, *"headcount restricted constrained platform organization"*(02:10~02:26). AI로 풀려 해도 *"complex workflow orchestration involving various inter asynchronous interaction team workflows integrations across tools"*(02:28~02:38).

→ [[inner-outer-meta-loops]] — Tessl의 *outer loop*(PR 뒤의 비싼 검사)와 **같은 자리, 다른 가치 부호**. Tessl은 outer loop를 *설계해서 키울* 대상으로, Ali-Reza는 실패가 *만들어 내는* 비용으로 쓴다.

## 3. AI가 악화시킨다 — 두 나쁜 선택 (02:43~03:25)

- *"AI kind of makes the problem even worse. Uh, you've got a lot of PRs now being generated, more PRs than before, uh, thanks to AI, and bigger PRs, uh, all of which can have defects. And so, your costs in your development life cycle are kind of shifting to the right."*(02:43~03:00)
- *"Either you slow down and ask developers to review every PR very carefully or you rubber stamp PRs and you risk incidents in production. Either way, you've got less happy developers, lower sentiment, and much less productivity than than you'd expect."*(03:09~03:25)

→ [[verification-bottleneck]] · [[trusted-throughput]](병목의 이동: 생성 → 리뷰·CI). ⚠️ "shift right"는 [[shift-left-security]]의 처방(왼쪽으로)과 **같은 축의 반대 방향 진단**이다 — 다만 화자의 처방은 검증을 왼쪽으로 옮기는 것이 아니라 **오른쪽 단계를 자동화**하는 것이다.

## 4. 에이전트형 검증 파이프라인 (03:27~05:29)

*"an agent that fully automates all the validation steps and as outcomes it delivers for you green PRs that are ready to merge or merge automatically."*(03:43~03:55)

| 단계 | en-orig | 비고 |
|---|---|---|
| **리뷰** | *"it reviews your PR and posts issues and inline comments. No surprise there. But our goal has been to really make this experience as noisefree as possible, both in the way we handle the UX as well as posting issues that are real and really matter."*(03:57~04:15) | ⚠️ 노이즈는 **목표**, 오탐률 미발화 |
| **커스터마이즈** | *"customize your review with your own rules (…) add your own custom checks (…) trigger your own custom workflow automations"*(04:15~04:22) | |
| **머지 차단** | *"configure the system to block merging if there are any unresolved code review findings."*(04:24~04:31) | 소프트(코멘트) → 하드(차단) |
| **CI 실패 분석** | *"analyzes CI failures and posts a summary of the root causes of those failures. And in particular, it's really good at catching flaky tests. And you can even set up rules that automatically retry flaky tests if you want. That's a very popular feature."*(04:31~04:47) | ⚠️ 정확도·인기의 근거 미발화 |
| **자동 수정 루프** | *"automatically fix any code review issues or any CI failures (…) or more interestingly, you can set it up to automatically loop until all the fish[=] issues have been fixed in your PR and you have a green PR ready to merge."*(04:48~05:11) | 리뷰어 = 수정자 |
| **자동 승인·머지** | *"you can automatically approve and merge PRs that are green. you can define rules and conditions that control when uh PRs get automatically approved by the agent and merged automatically."*(05:14~05:31) | ⚠️ 규칙의 예시·기본값 미발화 |

→ [[automated-code-review]] — Laurie Voss가 정리한 *"오탐이 리뷰어를 죽인다"* · *"리뷰 + 수정 융합"* 과 같은 설계 방향을 **CI 실패·flaky·머지까지** 넓힌다. 자동 수정 루프는 [[linear-vs-closed-loop-harness|폐루프]]의 PR 단위 사례.

## 5. 신뢰가 쌓이는 만큼 자동화 단계를 올린다 (05:31~06:39)

- *"There's a clear trajectory towards fully automated PRs. uh as users use the system and as they build trust in the accuracy of the AI what we see is they work towards full automation"*(05:36~05:50)
- 순서: ① 리뷰를 받으며 정확도와 중요도를 확인 → ② *"then they give teeth to the agent by allowing to start blocking the PRs"*(05:59~06:05) → ③ *"start using the autofix capabilities to automatically turn[⚠️] PRs and fix all the issues that were raised by code review or any CI failures"*(06:05~06:15) → ④ ⭐ *"where the real interesting leap is beginning to happen now is users setting up rules that define when the agent automatically approves and merges PRs."*(06:15~06:27)
- *"So over time as they build trust in the system, they unlock more levels of automation. And with the additional levels of automation and with the trust, they're getting more value out of the system."*(06:27~06:39)

→ [[agent-trust-curve]] — 같은 사다리가 **제품의 설정 단계**로 구현된 첫 소스. ⚠️ 단계별 사용자 비율·기간·되돌림(신뢰를 잃고 내려온 사례)은 미발화. 4단은 *"beginning to happen now"* — 도달이 아니라 시작이다.

## 6. 부산물 — 모든 PR을 AI가 보니 생기는 인사이트 (06:41~07:44)

- 플랫폼 팀: *"a categorization of the top CI failures"*(06:55~06:58) — *"Are these flakiness issues that you (…) need to address by improving the reliability of the tests or are there infrastructure issues"*(07:04~07:12).
- 리더십: *"categorization of PRs (…) what amount of PRs are going to feature development versus fixing issues, chores, refactors"*(07:24~07:44).

→ [[trusted-throughput]] — PR 분류는 이 페이지가 경고한 PR 수·LOC 계열 지표와 이웃하지만, **양이 아니라 구성**(기능 vs 수리 vs 잡일)을 본다. ⚠️ 분류 정확도·검증 방법 미발화.

## 7. 내부 아키텍처 (07:46~08:45)

| 구성 요소 | en-orig |
|---|---|
| **control plane** | *"the control plane that acts as this orchestration layer for handling PR workflows."*(07:52~07:59) |
| **자체 agent runtime / harness** | *"We built our own harness here that handles multi- aent[=multi-agent] execution, context management, memory management, um tool calling, all the integrations"*(08:01~08:13). ⭐ *"having our own agent harness has really allowed us to optimize specifically for the validation use case. And it's allowed us to optimize for token cost, precision, and coverage of the agent itself. So that allows us to essentially guarantee outcomes at a fixed PR price while giving really good quality results."*(08:13~08:37) |
| **LLM proxy** | *"an NLM[=LLM] proxy that handles the routing across different models as well as things like failover."*(08:37~08:45) |

→ [[agent-harness-design]] · [[automatic-model-routing]](라우팅 + failover). **PR당 고정 가격**은 [[tech-bridge-kimchi-cost-per-task-harness|Kimchi]]의 *같은 품질의 작업당 비용*과 같은 계열의 과금 단위 전환이다 — 토큰이 아니라 **검증된 작업 단위**로 판다. ⚠️ 가격·보장 조건·초과 비용 처리 미발화.

## 8. 에이전트 + 프로그램 분석 (08:47~09:21)

- *"Now that we're part of Sonar, we've been integrating guitar with Sonar Cube[=SonarQube]. There's a ton of opportunity here in combining an agentic approach to validation with program analysis. So combining agents with things like um taint analysis, control flow analysis, data flow analysis, software composition analysis."*(08:47~09:11)
- *"So all the traditional approaches combined with agents, we think there's a ton of opportunity here and that together you can get much better precision, much better coverage at a really great price point."*(09:09~09:23)
- 결론 문장으로 반복: *"the combination of using agents uh doing a gentic[=agentic] validation plus an algorithmic program analysis will give you something that that I think is going to be much better than either alone."*(10:40~10:52)

→ [[agent-plus-program-analysis]](신규 제안) · [[hard-vs-soft-enforcement]](2층 정적 분석) · [[executable-standards]](상시 정적 분석) · [[behavior-validated-trust]](*"정적 분석·컴파일러가 같은 신뢰를 준다"*). ⚠️ **기대이지 측정이 아니다** — *"we think"*, 통합은 진행 중.

## 9. 결과 주장과 요약 (09:23~10:52)

- *"much better quality much better security especially with AI generated code faster delivery times through all the automation going from PRs straight to approved and merged PRs much higher productivity and sentiment by developers so less time spent on actually reviewing code and worrying about what's happening in production"*(09:27~09:51), 플랫폼 팀에 *"a lot more leverage"*(10:00~10:03). ⚠️ 전부 수치 없음.
- 요약: *"PR validation is really critical, even more so in AI. But AI turns validation into a friction point. And guitar, what we've built, allows you to automate this step, fully automate PR validation, go from created PRs all the way to merge, completely eliminating this friction, and helps you keep up with the rate at which you're generating code from AI."*(10:12~10:40)

## 이 위키와의 연결

### 이어지는 것

- **[[verification-bottleneck]] — CI까지 포함한 답.** 이 페이지의 답들은 대부분 *리뷰*를 다시 짜는 것이었다(Voss: 시스템으로 재건, Pocock: 싼 층 + one-way door, Lauren Tan: 에이전트가 자기 코드를 머지). Gitar는 **리뷰·CI 실패·flaky·머지를 한 에이전트 파이프라인으로** 묶는다. 진단(*"천 개의 pull request에 치여 죽고 있다"*, 마우스파워 편)에 **두 나쁜 선택**(*slow down* vs *rubber stamp*)이라는 이름을 붙인다 — rubber stamp는 사람이 병목이 되기를 거부할 때의 결과다.
- **[[automated-code-review]]** — Voss의 업계 목록(Copilot·CodeRabbit·Greptile·Graphite·Cursor)에 **Gitar(→ Sonar)** 가 붙는다. 설계 교훈 중 *오탐이 리뷰어를 죽인다*(→ *"noisefree"*)와 *리뷰 + 수정 융합*(→ autofix 루프)을 **그대로 제품 기능으로** 말한다. 다만 성공 지표(*"a human accepting my answer"*)에 해당하는 수치는 내지 않는다.
- **[[agent-trust-curve]]** — Lauren Tan의 *지름길 없음*, Dru Knox의 *autonomy ≠ automation* 에 이어 **설정 화면으로 구현된 사다리**(리뷰 → 차단 → autofix → 자동 승인·머지). 승급 조건은 *"as they build trust in the accuracy of the AI"* — Huang의 *능력*·Lauren Tan의 *행동* 중 **관찰된 정확도** 쪽이다.
- **[[trusted-throughput]] — flaky 테스트.** 이 페이지는 flaky 테스트를 방치하면 *AI 에이전트의 반복 재시도가 토큰을 낭비한다* 고 경고했다. Gitar는 ① flaky를 **탐지·분류해 플랫폼 팀이 고치게** 하고(07:04~07:16) ② 동시에 **자동 재시도 규칙**을 *"very popular feature"*(04:41~04:47)로 판다. ②는 경고된 증상을 자동화하는 쪽일 수도 있다 — 화자는 이 긴장을 다루지 않는다.
- **[[inner-outer-meta-loops]]** — *outer loop* 라는 같은 단어가 같은 자리(PR 뒤)를 가리킨다. 플랫폼 팀용 CI 실패 분류(§6)는 Tessl의 **meta loop**(로그·PR을 보고 반복 실수를 inner/outer로 되먹임)에 해당하는 부품이다.
- **[[automatic-model-routing]]** — LLM proxy(라우팅 + failover)가 **검증 제품 내부의 하네스 부품**으로 등장한다. 이 페이지의 Factory·Kimchi 라우터가 *라우터 자체*를 말했다면 여기선 **부품 하나**로 지나간다 — 라우팅 기준은 미발화.

### 갈리는 것

> ⚠️ **Contradiction: 자동 머지의 조건을 누가 정하나 — "rules and conditions" vs one-way door.** [[risk-proportional-human-review]]의 Pocock은 *"You really don't need to review every single two-way door. Every single one-way door you do."* 로 사람이 반드시 볼 PR을 **되돌릴 수 있느냐**로 가른다([[action-reversibility]]). Gitar는 자동 승인 조건을 *"you can define rules and conditions"*(05:18~05:29)로 **사용자 설정에 넘기고**, 어떤 PR이 자동 머지에서 빠져야 하는지·사람이 어디 남는지는 **말하지 않는다.** 제목의 질문(*"검증은 대체 누가?"*)에 대한 발화의 답은 *"more AI"* 뿐이다. 자동 머지 후 회귀·롤백 비율도 없다 — [[verification-bottleneck]]의 Lauren Tan 섹션이 지적한 공백과 같다.

> ⚠️ **긴장: 자체 하네스 vs 남의 하네스.** Gitar는 *"We built our own harness"* 로 **검증 용도 최적화**(토큰 비용·precision·coverage → PR당 고정 가격)를 얻었다고 말한다(08:03~08:36). 같은 날 ingest되는 OpenAI Codex 편(`GRMr7YdoJzo`, 설명란 *"자체적인 코딩 에이전트 하네스를 밑바닥부터 만드는 대신, 이미 (…) 검증된 오픈소스 하네스를 그대로 활용"*)은 반대 방향을 권한다. [[harness-as-platform]]·[[tools-and-context-over-harness]]의 build vs reuse 축 위의 두 점이다. ⚠️ 둘 다 자기 하네스를 파는 쪽이다.

> ⚠️ **긴장: 검증자와 판매자가 같다.** 리뷰·수정·승인·머지를 같은 벤더의 에이전트가 하고, *"outcomes"* 를 **PR당 고정 가격으로 보장**한다(08:30~08:36). [[generator-evaluator-pattern]]이 요구하는 *생성자와 다르게 튜닝된 평가자* 는 리뷰 에이전트와 수정 에이전트 사이에서 지켜지는지 발화되지 않는다(멀티 에이전트라는 말뿐, 08:05). *"guarantee outcomes"* 의 outcome이 *green PR* 인지 *프로덕션 무결함* 인지도 미발화 — 전자라면 [[mergeability-gap]]의 *테스트 통과 ≠ 머지 가능* 이 그대로 남는다.

> **flaky 재시도는 숨김인가 처리인가.** 위 [[trusted-throughput]] 항목 참고 — 해소하지 않는다.

## 해소하지 않고 표시만 한 것

- 화자의 성(surname)과 현재 직함. 인수 날짜·조건(*"about a month ago"* 의 기준일).
- 노이즈·flaky 탐지·autofix·자동 머지의 어떤 수치도. 단계별 사용자 비율. 자동 머지 후 회귀율.
- 자동 승인 *"rules and conditions"* 의 예시·기본값. 사람 승인이 남는 경로.
- *"fixed PR price"* 의 가격과 *"guarantee outcomes"* 의 정의.
- *"automatically turn PRs"*(06:08)의 원래 단어.
- SonarQube 통합의 현재 상태·출시 여부, 프로그램 분석과 에이전트를 **어떻게** 합치는지(입력으로 주는지, 사후 필터인지).
- 화면 슬라이드(아키텍처 다이어그램·인사이트 대시보드). 행사명·도시·녹화일.

## 등장 개체

- 인물: [[ali-reza|Ali-Reza]](신규 제안 — 자막엔 *"Ali"* 만, 성 미확정)
- 조직: [[gitar|Gitar]](신규 제안 — 자막 ASR *"guitar"*) · [[sonar|Sonar]](신규 제안 — 인수자, SonarSource) · [[ai-engineer|AI Engineer]](⚠️ 설명란 링크·해시태그 — 추정)
- 제품·도구: SonarQube(Sonar 페이지 안에서 다룸) · Gitar의 control plane · agent harness · LLM proxy
- 개념: [[agent-plus-program-analysis]](신규 제안) · [[verification-bottleneck]] · [[automated-code-review]] · [[agent-trust-curve]] · [[trusted-throughput]] · [[inner-outer-meta-loops]] · [[hard-vs-soft-enforcement]] · [[risk-proportional-human-review]] · [[action-reversibility]] · [[automatic-model-routing]] · [[agent-harness-design]] · [[harness-as-platform]] · [[tools-and-context-over-harness]] · [[linear-vs-closed-loop-harness]] · [[generator-evaluator-pattern]] · [[mergeability-gap]] · [[executable-standards]] · [[behavior-validated-trust]] · [[shift-left-security]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=gnXwThtDnIo> (10:54, `upload_date` 2026-10-13)
- raw: `01.raw/articles/2026-10-13_AI가 코드를 쏟아내는 시대, 검증은 대체 누가 해야 할까요?.md`
- 설명란 링크: <https://www.sonarsource.com/products/gitar/> · <https://www.sonarsource.com> · <https://x.com/SonarSource> · <https://www.linkedin.com/in/aliadl/> · <https://x.com/aadltaba> · <https://ai.engineer> (⚠️ 열어 보지 않았다)
- 리뷰 병목·자동 리뷰: [[tech-bridge-death-of-code-review]] · [[tech-bridge-pocock-pr-bottleneck]] · [[tech-bridge-lauren-tan-pocock-podcast-full]]
- 신뢰 사다리·루프: [[tech-bridge-tessl-harness-engineering-factory]] · [[tech-bridge-lauren-tan-trusting-agents]]
- CI·flaky·지표: [[tech-bridge-trusted-throughput]]
- 작업 단위 과금·라우팅: [[tech-bridge-kimchi-cost-per-task-harness]]
- [[tech-bridge]] · [[gitar]] · [[sonar]]
