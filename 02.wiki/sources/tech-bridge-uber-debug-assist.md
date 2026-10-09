---
title: "Tech Bridge — Uber에서 디버깅 에이전트 하네스를 구축하는 방법 (Kriti Dangi · Uber): Debug Assist, 결정론 골격 + 런타임 스킬, 머지율 5%→48%"
type: source
tags: [debugging-agent, root-cause-analysis, uber, langgraph, mcp, deterministic-pipeline, agent-skills, harness-as-platform, feature-flags, subagents, max-turns, arize-ai, self-reported-metrics, video]
source-url: https://www.youtube.com/watch?v=6YuIp-MwPv4
source-type: video
author: Tech Bridge (한영자막 재배포) · 발표 [[kriti-dangi]] ([[uber|Uber]] — 이름·직함은 제목·설명란에만, 발화엔 자기소개 없음) · 행사 미발화(설명란 링크 "AGNTCon + MCPCon 안내" — 녹화 행사인지 미확정), 녹화일 미확정
date-published: 2026-10-08
ingested: 2026-10-09
created: 2026-10-09
updated: 2026-10-09
---

# Tech Bridge — Uber에서 디버깅 에이전트 하네스를 구축하는 방법 (Kriti Dangi · Uber)

[[tech-bridge|Tech Bridge]]가 재배포한 **27:58 영상 — 발표 약 21분 + Q&A 3개, 공식 챕터 없음**(아래 구간은 위키가 임의로 나눴다). 화자는 [[uber|Uber]] 엔지니어 [[kriti-dangi|Kriti Dangi]](이름은 제목·설명란에만). **사내 프로덕션 디버깅 에이전트 [[debug-assist|Debug Assist]]의 1인칭 운영 보고**다 — 버그 유입(Wisdom·Healthline) → 자동 트리아지 → 30분 안의 근본 원인 분석(RCA) → 완화·수정·검증 → PR까지. 이 위키에 **"에이전트가 만든 PR이 실제로 머지되는 비율"을 1년 단위로 보고한 첫 소스**(5% → 약 48%)이고, 두 개념이 생겼다 → [[deterministic-agent-pipeline]] (신규) · [[harness-as-platform]] (신규).

> **계획은 모델에게 맡기지 않는다 — LangGraph로 고정한 골격에 결정론 노드(데이터 수집·가지치기)와 LLM 노드(분류·RCA·수정)를 섞고, 노드마다 모델과 턴 예산을 정한다. 골격은 변하지 않고 바뀌는 것은 런타임에 가져오는 스킬·플러그인뿐이다. 플랫폼 팀은 하네스를 제공하고, 도메인 팀은 자기 스킬과 서브에이전트를 가져온다.**

> *"We give the plan to the agent (…) We control the plan."* (09:13~09:29) · *"because everything doesn't have to be via agents. It's simply fetching data."* (09:44~09:49) · *"if it's taking more than 20 turns, it's generally going in the wrong direction in a bad rabbit hole. And that's how you also put guardrails around your agent."* (12:29~12:38) · *"this is the basic skeleton of the agent. It never changes. What changes is the skills and plugins."* (14:56~15:04) · *"You bring your own specialization. And we provide the harness."* (16:18~16:23) · *"we are not the owners of domain, we are the providers of the harness."* (27:46~27:50)

ASR·ko 보정: 제목의 핵심어 **harness를 `en`이 "framework"·"structure"·"infrastructure"로 바꾸고 ko가 그대로 물려받아, 자막 본문에서 네 번 모두 사라진다**(15:54, 16:20, 17:02, 27:48 — en·ko 공유 오류). ko는 *PR creation* 을 **"파라나 주 대통령"으로**(17:32), *"40% (…) still in the right direction"* 을 **"경영상의 문제점이 여전히 남아 있습니다"로**(19:27), *roughly 10,000 by the end of next half* 를 **"약 2000%까지 급증 … 10,000부터 다음 해 말까지 학기"로**(27:52), *lovely question* 에 **"[욕설]"을 삽입**하고(24:52), LLM을 **"법학 석사"**, logs를 **"통나무"**, max turns를 **"최대 교대 근무"**, 제품명 Wisdom·Healthline을 **"지혜"·"건강"** 으로 옮겼다. en-orig는 *"basil test"*(→ Bazel test, 추정), *"a rise tracing"*(→ Arize tracing)으로 들었다. 전체 목록은 raw. **인용은 en-orig에서만** 했다.

> ⚠️ **모든 수치가 Uber 내부 자기 보고다**(측정 방법·분모 미발화). Stripe 보고서(*"developers spend 40% of time debugging"* 04:31~04:37)만 2차 인용이고 제목·연도가 없다. **이 위키는 어떤 원 자료도 확인하지 않았다.**
>
> ⚠️ **화자 발언이 말 그대로면 거꾸로인 자리.** *"the Jira resolution time has increased. It has almost um increased by twofold, which is a huge improvement"*(19:46~19:54), 마무리의 *"we hope to increase the Jira resolution further, as well as the mean time to resolve"*(20:34~20:42) — **해결 시간·MTTR이 늘면 악화**다. 해결률(처리량)이 두 배라는 뜻인지, 시간이 반으로 줄었다는 뜻인지 **미확정**. 이 위키는 고쳐 읽지 않고 "Jira 해결 지표가 약 2배 개선(방향 미확정)"으로만 적는다.
>
> ⚠️ **화자·행사·시점.** 자기소개 없음 — 이름 *Kriti Dangi*·직함 *시니어 소프트웨어 엔지니어* 는 제목·설명란에만. 발화된 자기 정보는 *"I work in observability space"*(25:18~25:20) 하나. 행사명 미발화 — 설명란 *"AGNTCon + MCPCon 안내"* 링크가 녹화 행사인지 광고인지 미확정. 시점 단서는 *"back when we started this 1 year ago"*(19:59~20:05)와 *"by the end of next half"*(27:53~27:55)뿐, **절대 날짜·연도·모델 버전은 한 번도 발화되지 않는다**(*"Sonnet"*, *"Opus"* 만 — 설명란의 "Claude"도 자막엔 없다). 업로드는 2026-10-08.

## 1. 문제 — 버그는 넘치고, 디버깅은 원래 어렵다 (00:00~04:53)

- **버그가 들어오는 두 길.** **Wisdom** — 사내 직원과 베타 테스터가 앱에서 *"Oh, my screen is blank"* 한 줄로 신고하면 앱·버전·OS·도시 같은 메타데이터, 네트워크·분석·콘솔·GraphQL·UI 상태 로그, 스크린샷을 함께 잡는다(00:26~01:42). **Healthline** — 크래시·행·지터·성능 저하를 **자동으로** 잡는 앱 품질 분석 도구, 스택 트레이스와 크래시 덤프까지(01:46~02:33).
- 둘을 합쳐 *"almost 50,000 issues are assigned to engineers every year. 90% of these are customer impacting"*, 페이지 12,000건(02:37~02:50). ⚠️ 5만 × 90%와 1.2만 페이지의 관계는 설명 없음.
- 현실의 디버깅: 오류는 불명확하고(*"Something went wrong."*), 컨텍스트는 코드·로그·설정·데이터에 흩어져 있고 도구도 많다. 모노레포에 많은 팀이 기여하니 *"to figure out who caused the problem is another problem in itself"*(04:04~04:07), 찾아도 팀 간 의존(03:22~04:18). → 엔지니어 한 명이 이슈 하나 해결에 **평균 약 28일**(04:22~04:28). Stripe 보고서 *"40% of time debugging"*(⚠️ 2차 인용).

## 2. 파이프라인과 두 데모 (04:53~08:46)

- **발견**(Healthline·Wisdom) → **자동 트리아지**(우선순위·심각도·소유자·온콜) → **심층 RCA** *"in under 30 minutes"*(05:20~05:26) → **해결** — *"we don't just want to provide a big dump of data to the developers. We want to make it actionable."*(05:32~05:38)
- ⭐ **데모 ① 배터리.** 한 개발자가 출근 차를 기다리다 휴대폰이 뜨거워져 *"Uber app is responsible for nearly 30% of my battery usage. My phone is heating up."* 만 적어 신고했다. *"In those 20 minutes, Debug Assist had already created a fix without him clicking a single button. All the developer had to do was review it and deploy it."*(06:20~06:31) RCA: 백그라운드에서 돌아야 할 코드 경로가 포그라운드 루프로 취급된 **hot loop** → CPU·배터리 회귀, 앱은 17분간 백그라운드(07:12~07:40). 오른쪽에 **증거 타임라인** — *"So, we know that the agent is not hallucinating and we are somewhat confident in our fixes."*(07:45~07:54) ⚠️ 위키의 표시: 증거 타임라인은 근거를 *보여 줄* 뿐 환각이 없음을 *증명* 하지 않는다 — 화자도 *"somewhat confident"* 로 물러선다.
- **데모 ② 푸시 알림 크래시(P1).** 나쁜 롤아웃으로 푸시 알림을 아주 빠르게 누르면 앱이 죽었다. 코드를 짚고 수정안을 Slack으로 보냈고 *"the fix was merged and deployed the same day. So, we ended up catching the crash at a 5% roll out"*(08:29~08:39).

## 3. 아키텍처 — 계획은 우리가 쥔다 (08:46~14:52)

⭐ *"the agent is built on a LangGraph pipeline. It is a mix of deterministic and LLM nodes."*(08:52~08:59) 왜 [[langchain|LangChain]]/LangGraph인가: 에이전트는 보통 계획 단계와 실행 단계를 갖는데, *"What LangGraph or LangChain allows us to do is bypass that planning phase. (…) So, it removes certain levels of hallucination from the agent. We are not totally dependent on the LLM to come up with a good plan"*(09:08~09:26). → [[deterministic-agent-pipeline]] · [[workflow-vs-agent]]

| 노드 | 종류 | 하는 일 | 모델·예산 |
|---|---|---|---|
| **컨텍스트 수집** (09:31) | 결정론 | Healthline·Wisdom·로그 수집, **파싱·전처리·가지치기**(로그는 *"megabytes and megabytes and gigabytes"*) — 컨텍스트 비대·지연·비용을 피한다 | LLM 아님 |
| **분류·RCA** (10:22) | LLM | Uber 문제인가, 서드파티 라이브러리·인프라·네트워크인가, PR이 필요한가 → **신뢰도 점수** → 부족하면 [[model-context-protocol|MCP]]로 Jaeger 트레이싱·로깅·인시던트 데이터 조회 → **병렬 서브에이전트**로 RCA 후 통합 | *"a lower model, Sonnet, with limited number of turns"*(12:11~12:16) |
| **완화·수정** (12:41) | LLM | 수정 전에 **완화부터**: 기능 플래그 MCP로 크래시와 플래그(앱 하나에 *"at least tens of thousands"*)의 상관을 찾고, 강하면 *"it simply goes and rolls the feature flag back and the issue is mitigated"*(13:41~13:47). 노드 간 상태 전달 | *"Opus with a higher number of max turns"*(13:53~13:57) |
| **검증** (13:58) | — | *"It's actually called basil test for legacy reasons"*(13:59~14:01, Bazel로 판독 ⚠️) — 유닛 테스트 또는 모바일 E2E(시뮬레이터·에뮬레이터)로 **재현해 자기 수정을 검증** | — |
| **PR** (14:34) | — | diff/PR을 Jira·Healthline·Wisdom 이슈에 붙이고 Slack으로 전달 | — |

- 서브에이전트 예: **breadcrumb 분석**(세션 데이터로 사용자 타임라인 재구성 — RCA와 재현에 모두 쓰인다), **crash correlation**(크래시를 특정 릴리스 버전에 귀속)(11:28~11:57).
- ⭐ **턴 예산 = 표류 감지기.** RCA 노드는 *"mostly looking at the data and gathering information and summarizing it"* 이라 작은 모델로 충분하고, *"with trial and error we figured out that if it's taking more than 20 turns, it's generally going in the wrong direction"*(12:29~12:34). Q&A에서도 통제의 *"biggest contributor"* 는 *"the number of max turns"*(25:52~25:57).
- ⚠️ **위키의 표시 — 자율 완화의 권한.** 기능 플래그 롤백은 **프로덕션 상태를 바꾸는 쓰기 행동**인데, 상관이 *"very strong"* 이면 에이전트가 *"simply goes and rolls"* 한다. 승인 게이트·임계값·감사 기록은 발화되지 않는다. → [[risk-proportional-human-review]]

## 4. 골격은 고정, 스킬은 런타임에 — 플랫폼은 하네스를 준다 (14:52~17:30)

- ⭐ *"this is the basic skeleton of the agent. It never changes. What changes is the skills and plugins."*(14:56~15:04) LLM 노드마다 자기 스킬 — *"How to create a good PR at Uber"*, 테스트 계획 관행, 안드로이드 수정법(*"Do I want to do lazy loading always?"*)(15:04~15:19). 비즈니스 로직은 골격 밖에 있고 런타임에 가져온다 → *"tomorrow if I want to add a new agent, it's a matter of crowd sourcing the skills"*(15:33~15:37). → [[agent-skills]]
- ⭐ **플랫폼/도메인 분업.** *"we have provided the harness to the developers. We have provided the steps to follow. We have provided the runtime environments, the dependencies"*(15:52~16:01) — 팀은 자기 전문 스킬만 가져오고, 플랫폼 팀은 모두의 스킬을 유지할 필요가 없다. → [[harness-as-platform]]
- 규모: **에이전트 약 8개 · 모노레포 5개 · 단일 코드베이스**(16:23~16:29). Python 모노레포를 PEX 바이너리로 패키징해 공용 아티팩트 저장소에 올리고, 실행 시 **에이전트 타입**에 맞는 바이너리·Docker 런타임·파이프라인을 가져온다(16:30~16:58).
- ⭐ **플러그인은 다 넣지 않는다.** *"Uber has a skills marketplace which is huge. There are almost 3,000 plugins right now and we can't dump the context of all the plugins to an agent. It goes crazy. So, you need to limit the agent in some way and this is how we do it using the agent type parameter."*(17:09~17:27) → [[deferred-tool-context]]와 같은 문제, 다른 답(아래 "이 위키와의 연결").

## 5. PR 이후 — 사람이 다듬는 자리 (17:30~19:05)

*"we don't stop at PR creation and forget about it"*(17:30~17:34):
- **diff fixer** — 유닛 테스트 추가·리팩터·변수명 같은 작은 증분 수정을 *"a click of a button and a single line prompt"*(17:45~18:05)
- **Ask AI** — RCA와 이슈를 묻고 교정할 수 있다. *"as soon as you provide corrections, you also build a feedback loop to the agent which helps improve its own prompts and skills"*(18:20~18:27). ⚠️ 교정이 프롬프트·스킬에 **자동 반영되는지, 사람이 승격하는지** 미발화 → [[skill-self-improvement]]
- **내 머신에서 열기** — 로컬 또는 원격 머신 풀에서 환경이 미리 세팅된 채로, *"Um I would also encourage you to do so."*(18:30~18:39)

## 6. 지표 (19:05~20:42)

| 지표 | 발화 | 비고 |
|---|---|---|
| RCA 처리량 | *"almost 9,000 issues every month"*(19:09~19:14) | 자기 보고 |
| RCA 정확도 | *"50% as compared to exact developer fixes"*(19:18~19:25) | 기준 = 개발자가 실제로 한 수정 |
| 부분 정답 | *"out of the remaining 50%, almost 40% of those issues are still in the right direction"*(19:25~19:31) — 맞는 모듈이지만 파일이 틀리거나, 맞는 파일이지만 함수가 틀림 | ⚠️ 나머지의 40%(전체 약 20%)인지 40%포인트인지 미확정 |
| Jira 해결 | *"resolution time has increased (…) by twofold, which is a huge improvement"*(19:46~19:54) | ⚠️ 방향 미확정(위 헤더) |
| ⭐ **PR 머지율** | *"back when we started this 1 year ago (…) the merge rate was only 5%. And now that number has increased to almost 48%."*(19:59~20:18) | 분모·추이 미발화 |

다음 목표: 커버리지·사용 사례·정확도(*"ideally 100%"*)(20:19~20:42).

## 7. Q&A (20:56~27:55)

- **① 검증 단계는 어떻게 테스트하나**(20:56~23:50). 답: *"yes as well as no"* — **가장 짧고 단순한 재현 경로부터**: 유닛 테스트 → 통합·컴포넌트 테스트 → 코드로 재현이 안 되면 자동화 테스트. 사례: 공항 근처 **약한 네트워크에서만** 나던 문제 — 코드로 네트워크를 흉내 낼 수 없어, 별도 인프라 팀(*"similar to (…) browser stack or Kobiton"*)이 띄운 시뮬레이터·에뮬레이터에 사용자 로그의 네트워크 세기·배터리·기능 플래그를 그대로 모킹하고 APK/IPA를 빌드해 통과할 때까지 반복, **재시도 횟수는 고정**(22:03~23:48). → [[agent-verification-skill]] · [[linear-vs-closed-loop-harness]]
- **② 병렬 서브에이전트를 어떻게 추적·통제하나**(24:08~26:53). 추적: *"we do have built-in tracing (…) it's called a rise tracing"*(25:12~25:28, → [[arize-ai|Arize]] 트레이싱) — LangChain과 모든 LLM 호출에 붙여 *"every tool call (…) all the MCPs that we call, every bash command that the agent runs"*(25:35~25:46)를 본다. 통제: ① **max turns**(20~30턴이면 정상, 넘으면 이상) ② **입력 가지치기** — 문제 커밋을 찾는 서브에이전트에게 전체 Git 이력을 주지 않고 *깨끗한 버전/나쁜 버전* 사이, Rider·Driver·Uber Eats 모듈로 걸러 준다: *"you also control the input to those sub agents"*(26:09~26:53). ⚠️ 화자가 관측 쪽 사람이라고 스스로 말한 직후의 도구 언급 — 이해관계 표시만 한다.
- **③ 전략(서브에이전트)은 몇 개인가**(26:55~27:55). *"all in all 30 sub agents, 30 unique sub agents"* → **domain extensions**로 도메인 소유자가 자기 서브에이전트와 지식 베이스를 붙이면 *"roughly 10,000 by the end of next half"*. ⭐ 근거: *"Because we are not the owners of domain, we are the providers of the harness."*(27:46~27:50) ⚠️ 30 → 10,000은 약 333배 — **계획치**이고, 10,000개 서브에이전트 중 RCA 노드가 무엇을 언제 부르는지는 말하지 않는다(4절의 *"It goes crazy"* 문제가 서브에이전트 층에서 다시 생길 자리).

## 이 위키와의 연결

### 이어지는 것

- **[[workflow-vs-agent]]** — 그 페이지가 유보로 남긴 *"하이브리드(워크플로 안의 에이전트)를 다루지 않는다"* 에 **실제 운영 사례**가 들어왔다. 바깥은 LangGraph로 고정한 워크플로, 안은 턴 예산이 걸린 LLM 노드와 병렬 서브에이전트. 이유가 [[tech-bridge-vercel-eve-filesystem-agent|Vercel]]의 *"컨텍스트 손실"* 과 반대 방향이다 — Uber는 **계획을 모델에게서 빼앗는 것을 환각 감소 장치**로 쓴다. → [[deterministic-agent-pipeline]]
- **[[mergeability-gap]] · [[automated-code-review]]** — Voss가 *"is a human accepting my answer"* 를 업계 공통 성공 지표로 꼽았다면, Uber는 그 지표의 **1년 궤적**을 준다(머지율 5% → 약 48%). RCA 정확도의 기준도 *"exact developer fixes"* — 사람의 실제 수정이 정답지다. ⚠️ 같은 Goodhart 경고가 적용된다(사람이 받아들이기 쉬운 PR로 최적화될 수 있다).
- **[[deferred-tool-context]]** — 같은 문제(플러그인 약 3,000개, *"It goes crazy"*), 다른 답. Factory는 **필요할 때 펼친다**(progressive disclosure), Uber는 **에이전트 타입으로 미리 자른다**(정적 범위 지정). 두 소스 모두 측정치는 없다.
- **[[agent-skills]] · [[harness-engineering]]** — *"we are the providers of the harness"* 는 하네스를 **사내 플랫폼 제품**으로, 스킬을 **도메인 팀의 기여물**로 나누는 조직 설계다. → [[harness-as-platform]]
- **[[model-context-protocol]]** — MCP가 **관측 데이터 조회**(Jaeger·인시던트)뿐 아니라 **프로덕션 완화 행동**(기능 플래그 롤백)의 통로가 됐다.
- **[[production-trace-eval-flywheel]] · [[wandb-weave]]** — Arize 트레이싱으로 모든 도구 호출을 보지만, 트레이스를 **eval 태스크로 되돌리는 루프는 발화되지 않는다.** 피드백 루프는 Ask AI 교정 → 프롬프트·스킬 개선 쪽에만 있다.
- **[[verification-bottleneck]]** — 데모의 결말 *"All the developer had to do was review it and deploy it"*(06:28~06:31). 수정 생성은 20분이 됐고, 남은 사람의 칸은 리뷰와 배포다. 검증 노드(재현 테스트)가 그 리뷰의 부담을 앞단에서 줄이려는 장치.

### 갈리는 것

> ⚠️ **Contradiction(약): 계획을 누가 쥐는가.** [[tech-bridge-vercel-eve-filesystem-agent]]는 역할별 체인에서 **자기 상태를 관리하는 단일 에이전트**로 옮겨 갔고(*단계 경계에서 정보가 샌다*), Uber는 반대로 **계획을 고정한 그래프**에 머문다(*계획을 모델에 맡기면 환각이 는다*). Uber는 노드 간 *"all the states are passed between each node (…) It has not forgotten anything"*(12:58~13:03)이라며 Vercel의 문제를 상태 전달로 풀었다고 주장하지만, 두 소스 모두 비교 측정은 없다. 과제 차이(반복 가능한 디버깅 파이프라인 vs 개방형 질의)로 화해될 수 있다 — [[workflow-vs-agent]]의 Jerry Liu *"반복 가능한 워크플로는 남긴다"* 와 같은 축.

## 해소하지 않고 표시만 한 것

- **Jira 해결 *시간* 이 2배 "늘었다"·MTTR을 "늘리겠다"** — 말 그대로면 악화. 방향 미확정.
- **"나머지 50% 중 약 40%"** 의 분모, **머지율 48%** 의 분모·측정 구간, **5만 건 vs 페이지 12,000건** 의 관계.
- **기능 플래그 자동 롤백의 승인 경로** — 미발화.
- **Ask AI 교정 → 프롬프트·스킬 개선** 이 자동인지 사람 승격인지 — 미발화.
- **"basil test"** 의 정체(Bazel 추정), **"common artifactry"** 가 제품 Artifactory인지 — 미확정.
- **Stripe 보고서**(40% 디버깅)의 제목·연도.
- **행사·녹화일·모델 버전** — 미발화. 설명란 AGNTCon + MCPCon 링크는 열어 보지 않았다.

## 등장 개체

- 인물: [[kriti-dangi]] (신규) · 질문자 2명(이름 없음)
- 조직: [[uber]] (신규) · [[langchain]] · [[arize-ai]] · Stripe(보고서 인용) · BrowserStack · Kobiton(비교 대상으로만)
- 제품·도구: [[debug-assist]] (신규) · Wisdom · Healthline(Uber 사내 도구, 페이지 없음) · LangGraph · Jaeger · Jira · Slack · PEX · Docker · Sonnet · Opus(버전 미발화)
- 개념: [[deterministic-agent-pipeline]] (신규) · [[harness-as-platform]] (신규) · [[workflow-vs-agent]] · [[agent-skills]] · [[deferred-tool-context]] · [[model-context-protocol]] · [[harness-engineering]] · [[mergeability-gap]] · [[automated-code-review]] · [[verification-bottleneck]] · [[agent-verification-skill]] · [[linear-vs-closed-loop-harness]] · [[skill-self-improvement]] · [[production-trace-eval-flywheel]] · [[risk-proportional-human-review]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=6YuIp-MwPv4> (27:58, `upload_date` 2026-10-08)
- raw: `01.raw/articles/2026-10-08_Uber에서 디버깅 에이전트 하네스를 구축하는 방법 - Kriti Dangi.md`
- 설명란 링크: <https://hubs.la/Q04gbXLb0> (*"AGNTCon + MCPCon 안내"*, ⚠️ 열어 보지 않았다)
- 같은 주제: [[tech-bridge-death-of-code-review]] · [[tech-bridge-factory-software-factory]] · [[tech-bridge-vercel-eve-filesystem-agent]] · [[tech-bridge-wandb-aria-self-improving-agent]] · [[tech-bridge-jev-agent-harness]]
- [[tech-bridge]] · [[kriti-dangi]] · [[uber]] · [[debug-assist]]
