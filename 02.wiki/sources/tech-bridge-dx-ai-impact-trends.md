---
title: "Tech Bridge — 400개 기업 데이터로 본 소프트웨어 개발 AI의 현주소 (DX · Justin Reock): 속도·품질·사람·측정·병목의 다섯 트렌드"
type: source
tags: [developer-productivity, developer-experience, dora-metrics, change-failure-rate, pr-size, incremental-delivery, perception-gap, ai-measurement, platform-readiness, theory-of-constraints, getdx, vendor-claims, video]
source-url: https://www.youtube.com/watch?v=xRZHLI5SPWo
source-type: video
author: Tech Bridge (한영자막 재배포) · 발표 [[justin-reock]] ([[getdx|DX]] deputy CTO — 자막엔 "Justin Rio", 이름은 설명란 링크) · 행사명 미발화 · 촬영 2026년 6~7월 추정
date-published: 2026-10-02
ingested: 2026-10-03
created: 2026-10-03
updated: 2026-10-03
---

# Tech Bridge — 400개 기업 데이터로 본 소프트웨어 개발 AI의 현주소 (DX · Justin Reock)

[[tech-bridge|Tech Bridge]]가 재배포한 **18:42 발표, Q&A 없음, 공식 챕터 14개.** 화자는 개발자 생산성 측정 플랫폼 [[getdx|DX]](getdx.com)의 deputy CTO [[justin-reock|Justin Reock]]. DX 플랫폼 데이터로 AI 도입 약 1년의 변화를 **다섯 트렌드**로 정리한다. 이 위키에 **DORA 지표와 조직 단위 집계 데이터가 처음 들어왔다** — 지금까지 생산성 수치는 거의 전부 개인 체감이나 한 회사의 자기 보고였다. → [[dora-metrics]] (신규) · [[perceived-vs-actual-productivity]] (신규) · [[ai-measurement-framework]] (신규)

> **배포 빈도는 늘었다. 하지만 변경 실패율의 진폭이 커졌고, PR은 44줄에서 72줄로 불었고, 개발자는 코드를 더 잘 고칠 수 있다고 느끼면서도 자기 변경을 덜 믿는다. PR 처리량 증가는 중앙값 7.7%, 2배에 간 곳은 없다. 이유는 코드 생성이 애초에 병목이 아니었기 때문이다.**

> *"code generation was never the bottleneck in the first place, right?"* (14:48~14:51) · *"Nobody hit 2x, nobody hit 5x, nobody hit 10x."* (15:27~15:32) · *"agents and assistants are making it easier for me to understand and modify the code that's in front of me, but I trust the outputs less."* (06:30~06:38) · *"it turns out that what's good for humans is also good for agents"* (13:56~14:00)

ASR·ko 보정: ko는 **조각 번역**(이벤트당 평균 약 4.5자)이라 거의 모든 문장이 깨졌고, **핵심 결론을 뒤집었다** — *"Nobody hit 2x, nobody hit 5x"* 가 **"어떤 사람은 2배, 어떤 사람은 5배로 곱했습니다"**(15:28). *10 million* 을 **"1억"으로**(10:55), *median 7.7%* 의 중앙값을 지우고(15:19), *"over the last year"* 를 **"2015년에"로**(00:12), *since the late 90s* 를 **"90년대생"으로**(07:14) 창작했다. ⚠️ **`en`은 중앙값과 평균을 뒤바꿨다**(*"average 7.7% (…) median of 13%"*, 15:17~15:22) — en-orig는 *"a median 7.7% increase (…) a 13% average"*(15:19~15:25). en-orig는 화자를 *"Justin Rio"*, METR을 *"MER"*, Goldratt를 *"Ellie Goldot"* 으로 들었다. 전체 목록은 raw. **인용·수치는 en-orig에서만** 했다.

> ⚠️ **벤더 데이터.** 화자는 측정 플랫폼을 파는 회사의 부CTO이고, 모든 통계는 **DX 플랫폼 데이터에 대한 화자의 진술**이다. 그래프는 화면뿐, 표본 구성·기간·통제는 발화되지 않는다. 표본 진술은 *"about 200,000 engineers in this study"*(06:05~06:08)와 *"Each line on this graph represents a single company"*(04:45~04:52)뿐 — **"400개 기업"은 자막에 없고 제목·설명란의 숫자다.** 사례 셋(Morgan Stanley·Zapier·Spotify)은 **타사 공개 자료의 전언**이다. 화자는 측정의 필요를 말하면서 자사 프레임워크·백서·리포트를 안내한다(11:43~12:00, 18:18~18:34).
>
> ⚠️ **촬영 시점 — 2026년 6~7월 추정.** *"our Q2 report is coming out in just a few weeks (…) by midish end of July"*(18:20~18:32), *"in 2024 we gave everybody a coding assistant. In 2025 we started building agents. Now…"*(13:17~13:27), METR 후속 발표가 *"back in February"*(03:55~03:58). ⚠️ 그러나 PR 처리량 연구 기간은 *"from November to to 2024 to February this year"*(15:15~15:19) — "올해"가 2026이면 15개월 창, 2025면 다른 단서와 어긋난다. **예전 연구 수치를 재사용했을 가능성**, 판독하지 않는다. 행사명은 발화·설명란 어디에도 없다(*"the 345[=3:45] session (…) in the leadership room"* 00:58~01:03, *"the vendors that are here"* 13:27~13:29 → 리더십 트랙과 전시가 있는 컨퍼런스).

## 1. 속도 — 배포 빈도와 체감 (01:14~04:24)

**지표의 한계부터**: PR 처리량·배포 빈도는 *"proxy metrics for understanding the way that work flows through an organization. They're not fully representative of the value generation."*(01:28~01:35)

- **DORA 배포 빈도**: *"we're seeing it steadily increase. Um, it's tapering off a little bit"*(01:59~02:04). 초기 급증의 일부는 PR을 더 자주 올린 탓. 이 지표는 PR 생성부터 배포까지의 *"one small part of the SDLC PDLC"* 이고 *"It doesn't tell us about revert rates. It doesn't tell us about defect ratios. It doesn't tell us about change failure rate."*(02:25~02:33) → [[dora-metrics]]
- **지역**: 북미는 상승, *"We've seen Europe actually pull back a little bit just in the last quarter"*(02:47~02:54). 이유 추정 — 일하는 방식, 토큰 지출 여력, 규제(02:54~03:06). ⚠️ 수치 미발화.
- **체감 전달 속도**: *"This number shows an increase of about four and a halfish percent"*(03:32~03:37) — 1년간의 투자를 생각하면 *"it's interesting that this perceived rate has not (…) crept up a little bit more"*(03:41~03:47).
- **METR과의 대비**: *"obviously infamous flawed MER[=METR] study"*(03:49) — 16명, *"the productivity went down by about 19% but the perception went up by about 20%. So there was like a 40% spread"*(04:08~04:15). *"But here when we look at this on more of an aggregate things interestingly stay uh sort of flat."*(04:17~04:23) → [[perceived-vs-actual-productivity]]

## 2. 품질 — 변동성, 확신, PR 크기 (04:25~08:28)

**변경 실패율(CFR)**(04:33~05:44): *"It's very volatile the impact that we've seen on quality"*(04:41~04:45). 회사마다 한 줄인 그래프에서 상단은 *"increasing as much as 2%. which doesn't sound like much until you realize that the industry benchmark is about 4%. So that means shipping potentially 50% more defects"*(05:05~05:15) — 즉 **2%p 상승**. ⭐ AI가 원인의 전부는 아니다:

> *"this pattern exists without AI, by the way. (…) it's not purely causal with AI. A lot of this has to do with like your release pipeline, your automated testing (…) The pattern remains the same. the amplitude has changed as a result of AI."* (05:22~05:38)

→ [[dora-metrics]]의 "AI는 진폭을 키운다" · [[agent-readiness]]의 power law와 같은 그림

**유지보수성 ↑ vs 변경 확신 ↓**(05:47~06:44): 보통 같이 움직이던 두 설문 지표가 갈라졌다 — 코드 유지보수성 체감 *"gone up almost 4%"*(06:00~06:05), 변경 확신(change confidence) *"gone down 6%"*(06:24~06:29). ⭐ *"I'm more afraid now of breaking things than I was a year ago."*(06:35~06:41) → [[perceived-vs-actual-productivity]] · [[verification-bottleneck]]

**PR 크기 44 → 72줄**(06:44~08:00): *"This is going to be one of the most important metrics that we look at this year"*(06:46~06:50), 약 1년 사이 *"from uh around 44 lines on average per PR up to 72"*(06:56~07:02). 이유 둘:

1. 모델은 평균으로 훈련된다 — *"the code that's being generated is going to be essentially mediocre because it's law of averages"*(07:24~07:28). 화자: 90년대 말엔 *"as little code as possible"* 이 좋은 개발자의 표시였다(07:16~07:21)
2. ⭐ **빌드 파이프라인** — 빌드가 45분~1시간인데 AI가 함수 넷을 즉시 만들면 *"Am I going to push four different PRs (…) or I'm just going to cram all that code into a single PR?"*(07:36~07:46)

*"every extra line of code is a potential bug, a potential vulnerability. It's mortar[=more to] review. It makes the code less portable."*(07:50~07:57) **점진적 전달(incremental delivery) 체감은 10% 하락**(08:12~08:14) — 롤백과 리뷰를 쉽게 하는 원칙이 흔들린다. → [[minimizing-reader-load]]

## 3. 사람과 규모 (08:29~10:24)

- **주니어가 가장 많이 쓴다** — *"there's less to unlearn when you're coming into the industry"*(08:48~08:54)
- **agent experience** — *"literally we're we're asking agents about their experience working with humans"*(09:15~09:21), 사용 사례와 토큰 수를 함께 본다. 같은 사용 사례에 **주니어가 토큰을 더 쓴다**(09:27~09:33, *"just a learning curve"*)
- ⭐ **staff+는 같은 시간 절약, 더 적은 토큰** — *"staff plus or more senior engineers saving about the same amount of time, right? And and burning less tokens"*(09:43~09:50). 이유: *"an easier time spotting hallucinations, understanding the architecture"*(09:59~10:04)
- **작은 회사가 시간 절약에서 앞선다** — 릴리스 파이프라인이 단순하고 마찰이 적다(10:07~10:24). ⚠️ 수치 없음

## 4. 측정 — 프레임워크, 준비도, 에이전트의 피드백 (10:24~14:43)

*"measuring developer productivity and measuring developer experience was a challenge before AI and we we never completed that conversation before kind of throwing accelerant on this"*(10:33~10:43). 그런데 올해 모두 답해야 한다 — *"Spent 10 million or way more (…) on tokens. uh where's our 10x productivity?"*(10:53~11:02)

**AI Measurement Framework**(11:02~13:13) → [[ai-measurement-framework]] (신규)

- 기초 지표를 버리지 말 것 — *"Our foundational developer experience and developer productivity metrics are still what matter the most"*(11:08~11:14)
- 도구 API 텔레메트리로 **사용자 코호트**를 나누고, 코호트를 기초 지표 위에서 비교한다(11:20~11:42)
- 세 차원: **utilization**(DAU·WAU) · **impact**(어떤 지표가 움직이길 기대하나) · **cost**(*"15 years after the last major hype cycle and we're still trying to figure out cloud cost"* 12:23~12:28)
- 성숙도 곡선: 대부분 utilization에서 시작해 impact로(12:29~12:52)
- 예: 두 코호트를 *"PR cycle time or PR size or push back and review"*(12:59~13:05)로 비교

**플랫폼 AI 준비도**(13:13~14:05) → [[agent-readiness]]: *"Now we're realizing that our infrastructure wasn't ready for any of this."*(13:23~13:27) 항목 — *"clear and accurate, well structured documentation, data structures with straightforward relations, manageable modular code, reliable local CI and non-flaky test suites"*(13:41~13:50). ⭐ *"we used to just call this good developer experience"*(13:52~13:56), *"So we may finally paradoxically be making those investments that we should have been making over the last couple of decades."*(13:59~14:05)

**에이전트의 피드백**(14:05~14:41): 에이전트가 *"where they ran into issues with steering with the human, the the context that was provided for them, the the feedback cycles"*(14:16~14:24)를 질적으로 보고하고, 이를 사용 사례별로 나눠 *"which use cases are giving us the most efficient token spend"*(14:35~14:39)를 본다. ⚠️ 방법(어떻게 묻는지) 미발화.

## 5. 코드 생성은 병목이 아니었다 (14:43~16:14)

- ⭐ *"Even if engineers are getting like 100% accurate instant code coming from the models, which they are not, you would still only be attacking anywhere from maybe 14 to 16% of the overall value stream."*(14:51~15:03) ⚠️ 14~16%의 출처 미발화
- ⭐ **수치**: PR 처리량 증가 *"a median 7.7% increase in this velocity metric, a 13% average, but even our top performers were in the 70% range. Nobody hit 2x, nobody hit 5x, nobody hit 10x."*(15:19~15:32)
- 이유: AI의 시간 절약이 *"outweighed by other nonAI factors"*(15:34~15:39) — *"meeting heavy days and context switching and other sources of interruption, the cumulative effects of the dev environment and friction"*(15:45~15:53)
- **Goldratt**: *"as Ellie Goldot[=Eliyahu Goldratt] from the theory of constraints and the goal and (…) the Phoenix project would tell us that an hour saved on something that isn't the bottleneck is worthless"*(15:55~16:05) → [[verification-bottleneck]]

## 6. 사례 — 병목을 찾은 조직들 (16:09~18:18, 전부 화자 전언)

| 조직 | 무엇을 | 수치(화자 진술) | en-orig |
|---|---|---|---|
| **Morgan Stanley** | *DevGen AI* — 레거시 코드(mainframe Natural, COBOL, Perl) 해석 에이전트가 **PRD를 만들어** 엔지니어에게 넘긴다 → 역공학 단계 제거 | *"about 300,000 hours a year"* | 16:11~16:34 |
| **Zapier** | 행정 업무용 에이전트 생태계 — 에이전트 요약으로 스탠드업 **주 5회 → 2회**, 온보딩 *"about a two-eek[=two-week] period"*(업계 기준 *"over a month"*) | 엔지니어당 **15%** 추가 가치 창출 → 역대 최대 채용 | 16:34~17:28 |
| **Zapier** | PR 트리거 자동 1차 리뷰 — 피상적 항목만, 코멘트가 PR에 남아 다음 리뷰어가 참고 | *"about 3,000 of their code reviews a week"* | 17:28~17:52 |
| **Spotify** | SRE용 에이전트 — 런북의 조치 단계와 인시던트 컨텍스트를 모아 SRE 채널에 | 수치 없음 | 17:52~18:18 |

⭐ Zapier에 대한 화자의 해석: *"This is the right attitude. This is a throughput story. This is an increased innovative capacity story. This is not a headcount replacement story."*(17:20~17:28) → [[trusted-throughput]]

→ Morgan Stanley 사례는 [[legacy-code-modernization]], Zapier 리뷰는 [[risk-proportional-human-review]]와 이어진다.

## 이 위키와의 연결

### 이어지는 것

- **[[verification-bottleneck]]** — *생성은 병목이 아니다*에 동의한다. 데이터 쪽 증거도 같은 방향이다: PR이 커지고(44 → 72줄) 변경 확신이 떨어진다(−6%). 다만 Reock이 꼽는 **다음 병목은 검증이 아니라 조직 마찰**(회의·컨텍스트 전환·개발 환경)이다 — 아래 "갈리는 것".
- **[[agent-readiness]]** (Factory, 10-02) — Tereza의 *"hygiene check"* 와 Reock의 *"platform's AI readiness"* 는 **거의 같은 점검표**(문서·테스트·모듈성·CI)다. Reock은 이것을 *"good developer experience"* 라고 부른다 — **에이전트 준비도 = 옛 DevEx 투자**.
- **[[agent-roi-measurement]] · [[value-maxing]] · [[trusted-throughput]]** — *"where's our 10x productivity?"* 의 답을 활동량(토큰·DAU)이 아니라 **기존 결과 지표 위의 코호트 비교**에서 찾는다. 이 위키의 측정 페이지들이 *방향*만 있던 자리에 **구체적 틀**(utilization → impact → cost)이 들어왔다.
- **[[minimizing-reader-load]]** — 그 페이지의 미해결 *"측정 방법이 없다. PR 줄 수?"* 에 **집계 수치**가 생겼다(평균 PR 44 → 72줄).
- **[[codebase-gardening]] · [[ai-slop]]** — *"law of averages"* 로 평범한 코드가 늘고 PR이 커진다는 진단과 같은 축.

### 갈리는 것

> ⚠️ **Contradiction: 배수(x)인가 퍼센트인가.** [[frontier-engineering]](Amazon, 08-29)은 사내 파일럿에서 프로덕션 배포 속도가 *절반은 3x 미만, 다른 절반은 중앙값 4.5x, 일부 10x+* 라고 했다. Reock의 집계는 PR 처리량 증가 **중앙값 7.7%, 상위도 70%대, "Nobody hit 2x"**(15:19~15:32). 지표(배포 속도 vs PR 처리량)와 모집단(선별된 파일럿 vs 플랫폼 전체)이 달라 직접 비교는 안 된다 — 그러나 **"step function"과 "아무도 2배에 못 갔다"는 같은 시기의 업계 진술로 정면 충돌**한다. 둘 다 당사자 진술.

> ⚠️ **Contradiction: 개인 사례의 배수 vs 집계.** [[tech-bridge-lauren-tan-2000-prs|Lauren Tan]]의 *"지난달 PR 2,000개"* 같은 개인 처리량 서사와, 처리량 증가 중앙값 7.7%라는 집계는 같은 세계를 말하지 않는다. Reock은 그 차이를 *비AI 요인*으로 설명한다 — 개인의 생성 속도는 조직의 병목을 지나지 않는다.

> ⚠️ **다음 병목은 어디인가.** [[verification-bottleneck]]은 *생성 → 검증* 으로 옮겨갔다고 보고, Reock은 **회의·컨텍스트 전환·개발 환경의 누적 마찰**을 꼽는다(15:45~15:53). 자기 데이터(PR 크기 ↑, 변경 확신 ↓, 점진적 전달 ↓)는 검증 병목을 지지하는데 결론에서는 그것을 말하지 않는다 — **같은 데이터의 두 읽기**.

## 해소하지 않고 표시만 한 것

- **"400개 기업"** — 제목·설명란만. 자막엔 200,000명과 "회사마다 한 줄" 그래프뿐.
- **모든 퍼센트의 표본·기간·통제** — 체감 +4.5%, CFR 2%p·업계 기준 약 4%, 유지보수성 +4%, 변경 확신 −6%, PR 44 → 72, 점진적 전달 −10%, 14~16%, 7.7%·13%·70%대.
- **PR 처리량 연구 기간** — *"November to to 2024 to February this year"*. 연도 미확정.
- **CFR "2%"** — 화자는 *percent* 라고 했지만 업계 기준 4%와 비교해 "50% 더 많은 결함"이라 했으므로 **퍼센트포인트**로 읽었다.
- **METR 후속 발표(2월)** — 화자의 전언. 이 위키에 METR 페이지는 없고 원문을 확인하지 않았다.
- **"one of the lowest qualitative developer experience drivers"**(08:07~08:12) — 문장이 꼬였다. −10%만 취한다.
- **에이전트 피드백 수집 방법** — 무엇을 어떻게 묻는지 미발화.
- **사례 셋** — 타사 공개 자료의 전언. *DevGen AI* 의 정확한 표기 미확인.
- **챕터 "좋은 DevEx가 좋은 AX"** — "AX"는 자막에 없다(편집자 요약).

## 등장 개체

- 인물: [[justin-reock]] (신규) · Anton(DX 동료, 성 미발화) · Eliyahu Goldratt(*The Goal*, 제약 이론 — 페이지 없음)
- 조직: [[getdx|DX]] (신규) · METR(페이지 없음) · Morgan Stanley · Zapier · Spotify(모두 페이지 없음 — 사례 전언)
- 제품·도구·문헌: DX 플랫폼 · AI Measurement Framework(백서) · State of AI / AI Impact 분기 리포트(Q1·Q2) · DevGen AI(Morgan Stanley) · *The Goal* · *The Phoenix Project* · Spotify model
- 개념: [[dora-metrics]] (신규) · [[perceived-vs-actual-productivity]] (신규) · [[ai-measurement-framework]] (신규) · [[agent-readiness]] · [[verification-bottleneck]] · [[agent-roi-measurement]] · [[value-maxing]] · [[trusted-throughput]] · [[minimizing-reader-load]] · [[frontier-engineering]] · [[codebase-gardening]] · [[ai-slop]] · [[legacy-code-modernization]] · [[risk-proportional-human-review]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=xRZHLI5SPWo> (18:42, `upload_date` 2026-10-02)
- raw: `01.raw/articles/2026-10-02_400개 기업 데이터로 본 소프트웨어 개발 AI의 현주소입니다.md`
- 설명란 링크: <https://getdx.com> · <https://www.linkedin.com/in/justinreock/> · <https://substack.com/@jreock> · <https://x.com/DeveloperXM> (⚠️ 열어 보지 않았다)
- 같은 주제: [[tech-bridge-factory-software-factory]] · [[tech-bridge-frontier-engineering]] · [[tech-bridge-lauren-tan-2000-prs]] · [[tech-bridge-mousepower-measuring-agents]] · [[tech-bridge-tokenmaxxing-to-valuemaxxing]] · [[tech-bridge-trusted-throughput]]
- [[tech-bridge]] · [[justin-reock]] · [[getdx]]
