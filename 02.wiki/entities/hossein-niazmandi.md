---
title: Hossein Niazmandi
type: entity
category: person
tags: [braintrust, evals, observability, eval-platform, speaker]
aliases: [Niazmandi]
links:
  - "https://www.linkedin.com/in/hossein-niazmandi-20a184bb/"
sources: [tech-bridge-braintrust-eval-platform-systems-problem]
created: 2026-10-12
updated: 2026-10-12
---

# Hossein Niazmandi

[[braintrust|Braintrust]]의 화자(설명란 기준, 직함 미상). 이 위키의 유일한 소스는 [[tech-bridge-braintrust-eval-platform-systems-problem]] — eval 도구가 스프레드시트 → 맞춤 UI → 비기술 사용자의 실험 → 프로덕션 연결로 올라가고, 그 끝에서 eval 플랫폼이 **systems problem**이 된다고 주장한 16:25 발표다 → [[eval-platform-maturity-stages]].

> ⚠️ **신원 근거.** 자막 세 트랙 모두 이름이 없다 — 영상이 *"which we talked about earlier"*(00:22~00:24)로 발표 중간에서 시작해 자기소개가 잘린 것으로 보인다. 이름은 설명란 본문(*"Braintrust의 Hossein Niazmandi"*)과 LinkedIn 링크(`/in/hossein-niazmandi-20a184bb/`, 열어 보지 않았다)에서 왔다. 소속은 1인칭으로 확인된다(*"this is the same problem that we ran into"* 11:38~11:40, *"we built an abstraction layer called BTQL"* 12:25~12:27). 2026-09-02 원칙(설명란 표기를 따름)과 [[dan-adler]](자기소개 잘림, 이름 설명란에만)의 선례대로 페이지를 둔다 — [[tech-bridge-human-is-async-api]](Melanie Warrick)는 페이지를 만들지 않은 예외다.

## 위키에서 알려진 것

- 에이전트 품질의 두 기둥: evals(프로덕션 전) + observability(프로덕션 중) (00:18~01:19)
- *"spreadsheet-based evals are not wrong"*(04:08~04:12) — 그러나 *"returns diminish pretty quickly"*
- *"gone are the days where you build once with unit tests and regression tests"*(05:40~05:46) — drift 때문에 계속 hill climbing → [[production-trace-eval-flywheel]]
- *"agent traces are nasty. They are semi-structured JSON."*(11:13~11:18) — 실시간 vs 장기 쿼리, *"Two different workloads"*
- *"the human's responsibility is to review the outcome"*(16:05~16:11) — 코딩 에이전트가 headless로 eval을 돌고 사람은 배포 버전을 결정 → [[agent-native-interface]]

⚠️ 벤더 발표 — build vs buy 논지가 자사 제품으로 간다. 측정·고객 사례 없음.

## References

- [[tech-bridge-braintrust-eval-platform-systems-problem]] · [[braintrust]] · [[eval-platform-maturity-stages]]
