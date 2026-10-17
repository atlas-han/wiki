---
title: Uber
type: entity
category: org
tags: [ride-hailing, mobile, monorepo, debugging-agent, platform-engineering]
aliases: [우버, Uber Technologies]
links:
  - https://www.uber.com
sources: [tech-bridge-uber-debug-assist, tech-bridge-stigg-ai-companies-building-banks, tech-bridge-kimchi-cost-per-task-harness, tech-bridge-factory-bug-report-to-production]
created: 2026-10-09
updated: 2026-10-17
---

# Uber

차량 호출·배달(Uber Eats) 회사. 이 위키에는 [[tech-bridge-uber-debug-assist]]에서 **사내 디버깅 에이전트 [[debug-assist|Debug Assist]]를 운영하는 엔지니어링 조직**으로 처음 등장한다. 화자는 [[kriti-dangi|Kriti Dangi]].

> ⚠️ 아래는 전부 **화자의 자기 진술**이다. 이 위키는 원 자료를 확인하지 않았다.

## 소스에 나온 Uber 엔지니어링 (자막 근거)

- **버그 유입 도구 둘** — *Wisdom*(사내 직원·베타 테스터의 인앱 수동 신고, 로그·스크린샷·메타데이터 자동 첨부, 00:26~01:42) · *Healthline*(크래시·행·성능 저하를 자동 수집하는 앱 품질 분석 도구, 스택 트레이스·크래시 덤프 포함, 01:46~02:33)
- **규모** — 연 약 5만 건이 엔지니어에게 배정, 90% 고객 영향, 페이지 12,000건(02:37~02:50) · 해결에 평균 약 28일(04:22~04:28)
- **코드베이스** — 여러 **모노레포**에 많은 팀이 기여(03:49~04:01), *"billions and billions of lines of code"*(12:48~12:50, ⚠️ 수사) · 앱 하나에 활성 기능 플래그 *"at least tens of thousands"*(13:28~13:31) · 모듈 예: Rider · Driver · Uber Eats(26:41~26:45)
- **에이전트 플랫폼** — 에이전트 약 8개 · 모노레포 5개 · 단일 Python 코드베이스(PEX)(16:23~16:37) · 사내 스킬 마켓플레이스 플러그인 약 3,000개(17:09~17:16) · 시뮬레이터·에뮬레이터 전담 인프라 팀(23:02~23:11) → [[harness-as-platform]]

## 제3자가 말하는 AI 예산 소진 (2026-10-12 · [[tech-bridge-stigg-ai-companies-building-banks]] · [[tech-bridge-kimchi-cost-per-task-harness]])

두 벤더 발표가 Uber의 AI 사용 예산 소진을 든다 — ⚠️ 둘 다 출처 미제시, Uber 자신의 진술이 아니다.

- [[tech-bridge-kimchi-cost-per-task-harness]](Laura, [[cast-ai|Cast AI]]): Uber CTO가 *"in the last four months (…) used the entire budget of anthropic for the entire year"*(00:58~01:06).
- [[tech-bridge-stigg-ai-companies-building-banks]]([[dor-sasson|Dor Sasson]], [[stigg|Stigg]]): *"Uber saying they're basically torched down their entire uh AI usage consumption budget for the year in just a few weeks into the year."*(03:53~04:04)

> ⚠️ **Contradiction: 넉 달 대 몇 주.** 공급자도 한쪽만 말한다(Anthropic). 같은 보도의 다른 기억일 수 있으나 판정하지 않는다. → [[overspending-underusing-loop]]

## References

- [[tech-bridge-uber-debug-assist]] — first-seen
- [[debug-assist]] · [[kriti-dangi]]
- [[tech-bridge-stigg-ai-companies-building-banks]] · [[tech-bridge-kimchi-cost-per-task-harness]] — AI 예산 소진(제3자 주장)

## 세 번째 판본 — "by April" 헤드라인 (2026-10-17 · [[tech-bridge-factory-bug-report-to-production]])

[[davis-palmie|Davis Palmie]]([[factory-ai|Factory]]): *"We've all seen the headlines about Uber's CTO blowing through the year's AI budget by April"*(02:45~02:50). 기간은 Kimchi 편의 *"in the last four months"* 와 맞고(1~4월), Stigg 편의 *"just a few weeks into the year"* 와는 여전히 어긋난다. ⚠️ 출처 미제시(*"headlines"*), CTO 이름 미발화. 세 판본 모두 벤더 발표 안의 제3자 주장이다.
