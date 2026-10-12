---
title: "Tech Bridge — 평가 플랫폼 만들기가 생각보다 어려운 이유 (Hossein Niazmandi · Braintrust): eval 성숙 4단계와 'systems problem'"
type: source
tags: [evals, observability, eval-platform, production-traces, improvement-loop, agent-traces, llm-as-judge, multi-persona, braintrust, vendor-claim, video]
source-url: https://www.youtube.com/watch?v=S3knIZq7jM8
source-type: video
author: Tech Bridge (한영자막 재배포) · 발표 Hossein Niazmandi([[braintrust|Braintrust]], 이름은 설명란에만 — 자막에 자기소개 없음, 직함 미발화) · 행사명 미발화(설명란 ai.engineer 링크 → AI Engineer 계열 추정) · 녹화일 미발화
date-published: 2026-10-11
ingested: 2026-10-12
created: 2026-10-12
updated: 2026-10-12
---

# Tech Bridge — 평가 플랫폼 만들기가 생각보다 어려운 이유 (Hossein Niazmandi · Braintrust)

[[tech-bridge|Tech Bridge]]가 재배포한 **16:25 발표, Q&A 없음, 공식 챕터 15개.** 화자는 eval·observability 플랫폼 [[braintrust|Braintrust]]의 Hossein Niazmandi다 — **이름은 설명란에만** 있고 자막엔 자기소개가 없다(영상이 *"which we talked about earlier"*(00:22~00:24)로 시작해 앞부분이 잘린 것으로 보인다). 소속은 1인칭으로 확인된다 — *"this is the same problem that we ran into. I won't spend much time talking about Brain Trust"*(11:38~11:42), *"we built an abstraction layer called BTQL"*(12:25~12:27). **Braintrust는 이 위키에 처음 등장한다.** 테제:

> **eval 플랫폼은 "스프레드시트 위의 UI"가 아니다. 팀은 스프레드시트 → 맞춤 UI → 비기술 사용자의 실험 → 프로덕션 연결로 올라가며 프로덕션 실패 모드를 오프라인 테스트로 옮기는 개선 루프(flywheel)를 갖추려 하는데, 다 짓고 나면 거대한 반정형 에이전트 트레이스를 실시간·장기 두 워크로드로 쿼리해야 하는 systems problem이 남는다. 그리고 이제 그 루프를 코딩 에이전트가 돌고, 사람은 결과를 보고 무엇을 배포할지 정한다.**

> *"evals is just a UI on a spreadsheet, right?"* (02:59~03:02) · *"it's not necessarily that it's just a UI or UX problem, but building an eval platform truly becomes a systems problem."* (12:38~12:46) · *"agent traces are nasty. They are semi-structured JSON."* (11:13~11:18) · *"ultimately, the human's responsibility is to review the outcome."* (16:05~16:11)

이 위키에 개념 하나가 생긴다 → [[eval-platform-maturity-stages]] (신규 제안). 그리고 [[production-trace-eval-flywheel]]에 **두 번째 벤더의 같은 루프**(W&B 다음)가, 이번엔 *사람이 결정하는* 쪽으로 붙는다.

ASR·ko 보정: ko는 **production을 두 번 반대말로** 옮긴다 — observability의 자리 *"in production"* → **"현재 개발 중"**(00:46), *"reinforce that in your production scenario"* → **"오프라인 환경에서 이를 강화"**(00:57). North Star *"improve my agent quality without introducing new regressions"* → **"품질을 향상시키지 않고 새로운 회귀 분석을 도입"**(06:26~06:28), *"use natural language in a headless experience"* → **"자연어 없이"**(13:55), Braintrust 피치 *"Rather than you having to think about"* → **"생각해 봐야 한다"**(14:49~14:53) — 다섯 자리가 뒤집혔다. spreadsheet → **"종이에 … 계산"·"잎들이 계산은"**, PMs → **"총리들"**, *a movie's worth* → **"수백 개의 영상"**, long-running queries → **"장기 상담"**(`en` 공유), *full text* → **"전문을 보려면 클릭하세요"**(창작). en-orig 판독: *"Brain Trust"* → Braintrust, *"our back"*(15:32) → RBAC(⚠️ 문맥 판독). 전체 목록은 raw.

> ⚠️ **당사자 진술 — 벤더 발표, build vs buy에서 buy 쪽 이해관계.** 화자는 eval 플랫폼을 파는 회사 사람이고 논지 자체가 *"직접 만들기는 생각보다 어렵다"* 다. 명시적 자사 홍보는 ① 00:00~00:17 소개 ② 11:38~12:35 *"the same problem that we ran into"* + BTQL ③ **14:45~15:21** unknown unknowns 자동 발굴 ④ 15:26~15:45 자사 구현 목록(DB·RBAC·data masking). 이 위키는 **①~⑥절(일반론)과 ⑦절(Braintrust 기능)을 분리해서** 기록한다. 일반론 쪽도 측정·고객 사례는 없다 — 화자의 관찰(*"the eval platforms that we see"* 05:58)이다.
>
> ⚠️ **화자 이름.** 자막 세 트랙 모두 이름이 없다. 설명란 본문 *"Braintrust의 Hossein Niazmandi"* 와 LinkedIn 링크 슬러그 `hossein-niazmandi-…` 만 근거다 — **자막과 충돌하지는 않는다.** [[tech-bridge-human-is-async-api]](Melanie Warrick, 이름 설명란에만)의 선례대로 인물 페이지를 만들지 않으려 했으나, 통합 단계에서 다수 선례([[dan-adler]] 등 — 2026-09-02 원칙)에 맞춰 [[hossein-niazmandi]]를 두었다(같은 날 [[dor-sasson]] · [[jake-broekhuizen]]과 일관).
>
> ⚠️ **행사·시점.** 행사명·도시·연도 미발화. 설명란 `https://ai.engineer`·AI Engineer 유튜브/X/LinkedIn 링크 → **[[ai-engineer|AI Engineer]] 계열 추정**(확정 아님). 현장 청중 단서는 손들기(*"show of hands (…) Okay, I see one or two"* 03:05~03:15). 시점 단서는 *"when the ChatGPT boom happened a few years ago"*(12:50~12:54)·*"more recently"*(13:44)뿐. 업로드 2026-10-11.

## 1. 에이전트 품질의 두 기둥 — evals와 observability (00:18~01:19)

| 기둥 | 언제 | 무엇 (en-orig) |
|---|---|---|
| **Evals** | 프로덕션 *전* | *"Evals is what you do before your agent reaches production. This is when teams experiment, they test the behavior, and they build the confidence that they want to have before they ship to production."*(00:24~00:40) |
| **Observability** | 프로덕션 *중* | *"once your agent is in production and is interfacing with real-life users (…) the goal is to take that hypothesis that you built in your offline development process and then reinforce that in your production scenario through continuous monitoring."*(00:43~01:05) |

- *"Evals and observability are closely related to the same problem. One happens in production, the other one happens in development"*(01:05~01:14).
- ⚠️ ko는 바로 이 구분을 뒤집었다 — observability = "현재 개발 중"(00:46), 프로덕션 강화 = "오프라인 환경에서"(00:57).

→ [[production-trace-eval-flywheel]] · [[research-production-agent-parity]]

## 2. 왜 eval인가 — 비결정성은 힘이자 위험 (01:30~02:53)

- *"evals matter because LLMs by nature are non-deterministic, they are highly variable. That variability is exactly what makes them so powerful."*(01:33~01:46) — *"But that same flexibility also creates risk."*(01:54~01:56)
- *"agentic experiences are starting to become the primary way in which users will interact with companies."*(02:02~02:08)
- 위험 셋(02:24~02:41): **브랜드**(*"inconsistent behaviors"*) · **컴플라이언스**(*"if the agent says or does the wrong thing"*) · **비용·유지보수**(*"if the systems are hard or unreliable to debug or control"*).
- 목표: *"reduce that uncertainty before launch"*(02:44~02:49).

## 3. 스프레드시트도 좋은 첫걸음 — 최소 eval 시스템 (02:57~04:16)

- 청중 손들기: 스프레드시트에 eval 결과를 기록해 본 사람 *"one or two"* — *"there's no shame in that (…) It's actually the a good first step."*(03:12~03:18)
- ⭐ **최소 eval 시스템의 세 요소**(03:30~03:54): ① *"a way to execute agents against test inputs"* ② *"a way to view the outputs or the scores, even if those are being logged in a spreadsheet"* ③ *"a set of test inputs or examples that can invoke the agent"*. 입력 예시 = *"whatever information is needed to start the agent run. It could be a prompt, a request, or context"*(03:55~04:05).
- *"spreadsheet-based evals are not wrong. However, they're often the first step"*(04:08~04:15).

## 4. 빙산 아래 — 데이터·채점·사람·프로세스 (04:19~05:52)

- *"if evals were only, you know, run the agent, view the output, and then score it in a spreadsheet, this talk would be over right now."*(04:26~04:35)
- 결국 지어야 할 것: *"better data sets, scoring systems, review process, debugging tools, and the way to connect pre-production testing with production behavior."*(04:47~04:57)
- ⭐ **multi-persona**: *"Agent quality is a multi-persona problem. It's not just software engineers and AI engineers. There are PMs who used to build PRDs that are now running evals. There are SMEs who have the domain expertise of the product that you're building."*(05:16~05:30)
- *"gone are the days where you build once with unit tests and regression tests, you ship to production, and you don't think about it. Evals are a way for you to continue hill climbing against one target, which is agent quality."*(05:40~05:52)

→ [[skill-evals]] · [[field-level-unit-test-evals]](아래 "갈리는 것")

## 5. North Star — 개선 루프 (06:02~06:43, 10:00~10:52)

*"this is the North Star for many teams. They want to build the improvement loop"*(06:02~06:10):

1. 프로덕션의 기능·앱에서 *"observe the failure modes that happen based on dimensions that I define"*(06:12~06:16)
2. *"grab those failure modes and create test cases so that I can iterate offline"*(06:16~06:25)
3. *"improve my agent quality without introducing new regressions"*(06:25~06:31)
4. 계속 반복 — *"because just like in classical ML, drift becomes a real thing. The way users interact with your agents will change over time. The way you build your agents will change over time."*(06:31~06:43)

10:00~10:52에 *flywheel* 로 다시 그린다: *"log every input output, every step of your trace execution that your agent takes, analyze, understand what went wrong. You create the dimensions of failure and success because you know the outcomes."*(10:09~10:22) → 사용자 경험이 나빴던 시나리오로 오프라인 eval 생성 → 회귀 없이 개선 → 배포 → *"hill climbing against this"*(10:41~10:43).

→ [[production-trace-eval-flywheel]] — W&B(Aysola)와 **칸이 같다.** 차이는 아래 "이어지는 것".

## 6. eval 플랫폼의 성숙 4단계 (06:45~09:56)

⚠️ 번호는 챕터(업로더)의 것이다. 화자는 *"phase one"*(06:45)만 번호를 붙이고 나머지는 *"Then (…)"* 으로 잇는다.

| 단계 | 모습 (en-orig) | 얻는 것 | 한계 (en-orig) |
|---|---|---|---|
| **① 스프레드시트** | *"It's a for loop with a set of input examples and a way to execute the agent."*(07:00~07:04) | *"accessibility and time (…) basically zero barrier to entry"*(07:15~07:21) | *"the returns diminish pretty quickly. At this stage, you're pretty much only documenting."*(07:23~07:29) · 분석 수작업, *"human scoring is valuable but difficult to do, collaboration is very weak, (…) and domain experts are usually boxed out"*(07:38~07:51) |
| **② 맞춤 UI** | *"usually a product engineer (…) I can build a nice UI, a bespoke UI"*(08:00~08:10) | 다른 persona 합류 — *"This allows PMs to now kind of get into the loop of doing evals."*(08:21~08:26) | *"still collaboration becomes difficult"*, 장기 분석 불가(*"long horizon analytics"* 08:48~08:51) — *"Still just a reporting tool."*(08:54) |
| **③ 비기술 사용자의 실험** | *"I want my non-technical users to have an interface, where not that they just log the results, but they should be able to experiment."*(08:58~09:08) — 시스템 프롬프트·기반 모델·파라미터 변경 | *"side-by-side comparison"*(09:18~09:22) | 테스트 케이스가 *"still a curated set that arise in your offline e-vals"*(09:32~09:41) |
| **④ 프로덕션 연결** | (gap으로 제시) *"once I ship it to the production, I'm operating in the blind. So, I have no idea what steps my agent is taking and when those failures are actually happening in my live environment."*(09:45~09:56) | → §5의 flywheel이 플랫폼 안에서 완성 — *"You get that entire development cycle inside of your platform"*(10:54~10:58) | 다음 절 — *"you have to maintain it. You own this this product that you've built."*(11:00~11:05) |

→ [[eval-platform-maturity-stages]] (신규)

## 7. 다 짓고 나면 — systems problem (11:00~13:30)

- *"this is easy to do when it comes to smaller scale or POC and demo environments, but agent traces are nasty. They are semi-structured JSON. In some cases, we see teams that are logging a movie's worth of data in each interaction, hundreds of megabytes."*(11:05~11:27)
- *"your typical cloud data warehouses kind of collapse under this type of volume and load."*(11:30~11:34)
- ⭐ **두 워크로드**(11:46~12:25): **실시간** — *"you want to be able to query that data in real time as it lands in there. Because if your users are having poor experiences, you want to be able to know in real time"* · **장기 실행 쿼리** — 에이전트 경험 fine-tune, *"or even have humans who are doing alignment by annotating your your judges' outcomes. Two different workloads."*(12:10~12:25)
- ChatGPT 붐 이후의 새 문제들(12:50~13:30): *"real-time ingest"* · 페이로드 *"tens of megabytes, hundreds of megabytes in size sometimes, compared to traditional heartbeat observability, which are just kilobytes in size"* · *"deeply nested semi-structured full text is difficult to query"* · 읽기 패턴 — *"aggregate in large volumes, but also be able to do snapshots of of of in-time data"*.
- 결론: *"it's not necessarily that it's just a UI or UX problem, but building an eval platform truly becomes a systems problem."*(12:38~12:46) 그리고 그 시스템은 *"not only empower the AI engineer, but also the PMs, as well as the SMEs"*(13:34~13:47)여야 한다.
- ⚠️ 수치(수백 MB, KB 대비)는 사례 묘사이고 분포·출처가 없다.

→ [[agent-action-record]] · [[eval-platform-maturity-stages]]

## 8. 에이전트가 eval 플랫폼의 first-class citizen (13:44~14:20)

- *"more recently, we've seen that agents have become a first-class citizen of these eval platforms, where you want to be able to use natural language in a headless experience, where you can tell your coding agent of choice, "Find me all traces in the last 24 hours where the user had a poor experience. Run the evals for me.""*(13:44~14:10)
- 이유: *"because these coding agents have access to all of your underlying infrastructure and your code base, they become the mechanism to run the evals and log those results."*(14:08~14:20)

→ [[agent-native-interface]] · [[production-trace-eval-flywheel]](W&B ARIA는 *자사 에이전트* 가 돌고, 여기선 *사용자의 코딩 에이전트* 가 돈다)

## 9. Braintrust 피치 — unknown unknowns (14:21~15:45) — ⚠️ 당사자 진술

- 문제 제기: *"everything that I've shown you so far, it requires the humans, the the engineer, the PM, to be deeply involved in this process. And it can be laborious at times."*(14:28~14:43)
- ⭐ *"Rather than you having to think about these dimensions and of success and failure for your AI agent, Braintrust can surface these insights automatically. Because we log your tracing data into our platform, we can run inference on them, and we can tell you the unknown unknowns."*(14:52~15:12) — 예: *"scenarios in when my agent is failing silently"* · *"scenarios that my users are experiencing frustration by prompting my agent for the same request over and over again."*(15:12~15:21)
- 안 다룬 자사 구현: *"the underlying database that powers it, or having to build our back[=RBAC] into the system to manage controls and permissions, or data masking"*(15:27~15:36) → *"this is not just a UI and a spreadsheet, but rather it is a a systems problem"*(15:38~15:45).
- ⚠️ 정확도·재현율·사례 없음. 그리고 **화자 안의 긴장**: §5에서는 *"You create the dimensions of failure and success because you know the outcomes"*(10:17~10:22)라 했는데 여기선 플랫폼이 그 차원을 대신 찾는다. 두 진술을 조정하지 않는다.

→ [[braintrust]] · [[taste-encoded-evals]](judge를 트레이스에서 자동 생성하는 pi.recipes와 같은 방향의 벤더 주장)

## 10. 에이전트가 반복하고 사람이 결정한다 (15:49~16:23)

*"I said this earlier where humans were doing the improvement loop, and now we see coding agents where they could iteratively make changes and suggest what kind of improvements you should be making to your application. And ultimately, the human's responsibility is to review the outcome. If I have different iterations of these e-vals that are run by my coding agent, I can look at the outcome and make the decision of which version of it is the best for what I want to ship to production."*(15:52~16:23)

→ [[verification-bottleneck]] · [[agent-trust-curve]] · [[self-harness]]

## 이 위키와의 연결

### 이어지는 것

- **[[production-trace-eval-flywheel]] — 두 번째 벤더, 같은 칸.** W&B(Aysola)의 *프로덕션 트레이스 → 회귀 태스크 → hill climb → 배포* 와 Braintrust의 *실패 모드 관측 → 테스트 케이스 → 회귀 없이 개선 → 배포* 는 순환이 같다. 다른 점 셋: ① Braintrust는 루프의 시작을 **실패 모드**로만 말한다(W&B는 *"every production goodness as well"*) ② 루프를 도는 주체가 **사용자의 코딩 에이전트**(headless)다 ③ 마지막 칸에 **사람의 배포 결정**을 명시한다 — W&B 페이지가 표시해 온 *작성자 = 검증자* 빈자리에 대한 한 답(단, 측정 없음).
- **[[taste-encoded-evals]]** — *"humans who are doing alignment by annotating your your judges' outcomes"*(12:12~12:22)는 *"You need them to calibrate the evals"*(pi.recipes)와 같은 사람의 자리 — **judge 보정**. Braintrust는 이걸 **장기 실행 쿼리 워크로드**의 사례로 든다(인프라 쪽에서 본 같은 일).
- **[[tech-bridge-death-of-code-review]]** — [[laurie-voss|Laurie Voss]]([[arize-ai|Arize]])의 *"watching what the code actually does becomes the last reviewer standing"* 과 Braintrust의 *"once I ship it to the production, I'm operating in the blind"* 는 같은 결론(프로덕션 궤적 관측). ⚠️ 둘 다 관측·eval 도구 회사 사람이다.
- **[[agent-native-interface]]** — eval 플랫폼도 *"headless experience"* 로 에이전트가 직접 쓰는 표면이 된다.
- **[[agent-action-record]]** — 트레이스(*"every input output, every step"*)를 남기는 것이 전제. Braintrust는 그 기록의 **저장·쿼리 비용**을 문제 삼는 첫 소스다.

### 갈리는 것

> ⚠️ **Contradiction (약): 유닛 테스트형 eval로 충분한가.** [[field-level-unit-test-evals]]([[tech-bridge-voice-agent-failure-modes]]): *"단위 테스트가 제대로 통과하기만 한다면, 여러분의 에이전트는 안정적이고 반복 가능한 성능을 보여줄 것입니다"*(20:32~20:52, ko 인용). Niazmandi: *"gone are the days where you build once with unit tests and regression tests, you ship to production, and you don't think about it"*(05:40~05:46) — drift 때문에 프로덕션 관측과 계속된 hill climbing이 필요하다. 다만 앞쪽은 **평가의 해상도**(E2E vs 필드)를, 뒤쪽은 **한 번 짓고 끝내는 태도**를 겨눈다 — 정면 충돌은 아니다.

> ⚠️ **누가 실패의 차원을 정하나.** 이 소스 안에서도 갈린다(§9). 위키의 다른 소스: [[skill-evals]](Lauren Tan)는 사람이 실패를 보고 테스트를 쓰고, [[taste-encoded-evals]]는 에이전트가 judge를 만들고 사람이 보정하며, [[production-trace-eval-flywheel]](W&B)은 에이전트가 태스크를 쓰고 채점까지 한다. Braintrust의 피치는 **플랫폼이 차원을 발굴**하는 쪽 — 사람의 몫은 §10의 *결과 검토·배포 결정* 으로 좁아진다.

> ⚠️ **"evals" 경계.** Niazmandi는 evals = *프로덕션 전*, observability = *프로덕션 중* 으로 나눈다(00:22~01:14). W&B([[production-trace-eval-flywheel]])는 프로덕션 트레이스 자체를 eval 태스크로 만드는 쪽이라 이 경계를 흐린다. 같은 루프를 다른 이름으로 자른다 — 용어 충돌이지 주장 충돌은 아니다.

## 해소하지 않고 표시만 한 것

- 화자 이름·직함(설명란에만), 영상 앞부분(*"which we talked about earlier"*)의 내용.
- BTQL의 문법·구현, 설명란 `braintrust.dev/docs/reference/sql` 과의 관계(자막에 SQL 언급 없음).
- *"our back"*(15:32)의 RBAC 판독 — 문맥 기반.
- unknown unknowns 자동 발굴의 방법·정확도, *"underlying database"* 의 정체.
- 행사명·도시·녹화일.

## 등장 개체

- 인물: [[hossein-niazmandi|Hossein Niazmandi]](설명란에만)
- 조직: [[braintrust|Braintrust]] (신규 제안) · [[ai-engineer|AI Engineer]](⚠️ 설명란 링크만 — 추정) · [[openai|OpenAI]](ChatGPT 붐 언급만)
- 제품·도구: BTQL(Braintrust 쿼리 추상화, 페이지 없음) · ChatGPT(시점 언급만)
- 개념: [[eval-platform-maturity-stages]] (신규 제안) · [[production-trace-eval-flywheel]] · [[taste-encoded-evals]] · [[skill-evals]] · [[field-level-unit-test-evals]] · [[research-production-agent-parity]] · [[agent-action-record]] · [[agent-native-interface]] · [[verification-bottleneck]] · [[agent-trust-curve]] · [[self-harness]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=S3knIZq7jM8> (16:25, `upload_date` 2026-10-11)
- raw: `01.raw/articles/2026-10-11_평가 플랫폼 만들기가 생각보다 어려운 이유 — Braintrust.md`
- 설명란 링크: <https://www.braintrust.dev> · <https://www.braintrust.dev/docs/reference/sql> · <https://x.com/braintrust> · <https://www.linkedin.com/in/hossein-niazmandi-20a184bb/> · <https://ai.engineer> (⚠️ 열어 보지 않았다)
- eval 루프 비교: [[tech-bridge-wandb-aria-self-improving-agent]] · [[tech-bridge-introspection-loop-is-the-product]] · [[tech-bridge-lauren-tan-trusting-agents]] · [[tech-bridge-voice-agent-failure-modes]]
- 프로덕션 관측: [[tech-bridge-death-of-code-review]]
- [[tech-bridge]] · [[braintrust]]
