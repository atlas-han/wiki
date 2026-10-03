---
title: DORA 지표 (DORA Metrics) — 그리고 AI가 키운 진폭
type: engineering
category: pattern
tags: [dora-metrics, deployment-frequency, change-failure-rate, delivery-performance, developer-productivity, proxy-metrics, pr-size, ai-adoption]
aliases: [DORA, DORA metrics, DORA 4대 지표, four key metrics, 배포 빈도, deployment frequency, 변경 실패율, change failure rate, CFR]
related: [ai-measurement-framework, perceived-vs-actual-productivity, agent-readiness, minimizing-reader-load, verification-bottleneck, trusted-throughput, ai-native-sdlc, spec-driven-development]
first-seen: tech-bridge-dx-ai-impact-trends
sources: [tech-bridge-dx-ai-impact-trends]
created: 2026-10-03
updated: 2026-10-03
---

# DORA 지표 (DORA Metrics)

**소프트웨어 전달 성과를 보는 업계 표준 "네 가지 핵심 지표(four key metrics)" — 이 위키에 등장한 것은 배포 빈도(deployment frequency)와 변경 실패율(change failure rate).** 처리 속도와 안정성을 함께 보려는 틀이다. 이 위키에서는 [[ai-native-sdlc]]·[[spec-driven-development]]가 *"DORA 지표 검증"* 을 거버넌스의 목적으로 이름만 들었고, [[tech-bridge-dx-ai-impact-trends]]([[getdx|DX]], [[justin-reock|Justin Reock]])에서 **AI 도입 1년의 실제 추세**와 함께 처음 들어왔다.

> *"this is one of the, you know, four key metrics that tries to understand directionally, you know, the speed of shipping work within an environment"* (01:50~01:59)

> ⚠️ **이 페이지의 범위.** 소스는 네 지표 중 **두 개만** 이름을 댄다(배포 빈도, 변경 실패율). 나머지 둘의 이름과 정의, DORA의 연원(연구 프로그램·보고서)은 소스에 없어 적지 않는다. 화자는 DX 플랫폼이 *"built from the same folks who worked on Dora metrics"*(00:31~00:35)라고 하나 자사 진술이다.

## 먼저 — 대리 지표라는 것

> *"these metrics are not perfect. They are proxy metrics for understanding the way that work flows through an organization. They're not fully representative of the value generation."* (01:24~01:35)

배포 빈도는 *"the creation uh of the PR to actually trying to deploy this into production"* 구간만 본다 — *"It doesn't tell us about revert rates. It doesn't tell us about defect ratios. It doesn't tell us about change failure rate. It just tells us about how much stuff are we now kind of pushing out"*(02:21~02:37). **속도 지표 하나로는 품질을 알 수 없어서 짝을 둔다.** → [[trusted-throughput]]의 *토큰은 LOC다* 와 같은 경고

## AI 도입 1년의 추세 (DX 플랫폼 데이터, ⚠️ 벤더 진술)

| 지표 | 추세 | en-orig |
|---|---|---|
| **배포 빈도** | 꾸준히 증가, 최근 둔화(*"tapering off a little bit"*). 초기 급증 일부는 PR을 더 자주 올린 탓. 북미 ↑, 유럽은 지난 분기 후퇴 | 01:59~02:54 |
| **변경 실패율** | **회사별 변동성이 극심** — 상단은 최대 2%p 상승, 업계 기준 약 4% 대비 *"potentially 50% more defects"* | 04:33~05:15 |

### ⭐ AI는 패턴을 만들지 않고 진폭을 키운다

> *"this pattern exists without AI, by the way. This has a lot to do, it's not purely causal with AI. A lot of this has to do with like your release pipeline, your automated testing, everything that's surrounding the way that you're releasing the code. The pattern remains the same. the amplitude has changed as a result of AI. We always see this type of shift in volatility, but not usually to these extremes."* (05:22~05:44)

읽기: CFR이 오르느냐 내리느냐를 가르는 것은 AI 도구가 아니라 **릴리스 파이프라인과 자동 테스트**다. AI는 그 차이를 증폭한다 — [[agent-readiness]]의 *"AI 도입은 power law — 크게 성공하거나 크게 실패한다"*([[tereza-tizkova|Tereza Tížková]])와 같은 그림을 **다른 회사의 다른 데이터**로 본 것. 처방도 같다: *"You want to start measuring this stuff"*(05:18~05:22).

### 짝 지표 — DORA 밖에서 같이 봐야 할 것

같은 발표가 DORA 옆에 둔 지표들(전부 DX 데이터, ⚠️ 표본·기간 미발화):

- **PR 크기** — 평균 44 → 72줄(06:56~07:02). *"one of the most important metrics that we look at this year"*. 원인 하나는 **느린 빌드**: 45분~1시간짜리 파이프라인 앞에서 AI가 함수 넷을 즉시 만들면 PR 넷 대신 하나에 몰아넣는다(07:28~07:46). → [[minimizing-reader-load]]
- **점진적 전달 체감** — 10% 하락(08:12~08:14). 롤백과 리뷰를 쉽게 하는 원칙이 흔들린다.
- **변경 확신(change confidence)** — 6% 하락, 반면 코드 유지보수성 체감은 약 4% 상승(06:00~06:29). → [[perceived-vs-actual-productivity]]

연결 고리: **빌드가 느리다 → PR이 커진다 → 리뷰·롤백이 어려워진다 → 변경을 덜 믿는다 → CFR 진폭이 커진다.** ⚠️ 이 인과 사슬은 위키의 정리다. 화자는 PR 크기 증가가 변경 확신 하락의 *"a lot of this is because"*(06:44~06:46)라고만 말한다.

## 측정에서의 자리

DORA는 [[ai-measurement-framework]]의 **impact** 차원에서 쓰는 "기초 지표(foundational metrics)" 중 하나다 — AI 사용 코호트를 나눠 이 지표 위에서 비교한다. 새 AI 지표를 만들기보다 *"trusted metrics that we've already been looking at"*(11:16~11:20)을 유지하라는 것이 화자의 요지.

## 미해결

- 네 지표 중 나머지 둘이 같은 기간에 어떻게 움직였는지 — 소스에 없다.
- CFR의 "2%" — 퍼센트포인트로 읽었다(업계 4% 대비 50%라는 계산과 맞도록).
- 진폭 증가가 **AI 사용량과 상관**하는지 — 그래프는 회사별 선뿐, 사용량 축은 발화되지 않는다.

## References

- [[tech-bridge-dx-ai-impact-trends]] — first-seen
- [[getdx]] · [[justin-reock]]
- [[ai-measurement-framework]] · [[perceived-vs-actual-productivity]] · [[agent-readiness]] · [[minimizing-reader-load]] · [[trusted-throughput]] · [[ai-native-sdlc]] · [[spec-driven-development]]
