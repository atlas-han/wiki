---
title: "eval 플랫폼 성숙 단계 (Eval Platform Maturity Stages) — 스프레드시트에서 프로덕션 연결까지, 그리고 systems problem"
type: concept
category: pattern
tags: [evals, observability, eval-platform, maturity-model, production-traces, multi-persona, build-vs-buy, agent-traces]
aliases: [eval maturity, eval 성숙도, 평가 플랫폼 4단계, spreadsheet to production evals, evals is just a UI on a spreadsheet, eval platform is a systems problem]
related: [production-trace-eval-flywheel, taste-encoded-evals, skill-evals, field-level-unit-test-evals, research-production-agent-parity, yaml-agent-eval-pipeline, agent-action-record, agent-native-interface, trace-to-memory-loop]
first-seen: tech-bridge-braintrust-eval-platform-systems-problem
sources: [tech-bridge-braintrust-eval-platform-systems-problem]
created: 2026-10-12
updated: 2026-10-12
---

# eval 플랫폼 성숙 단계

**팀의 eval 도구는 스프레드시트 → 맞춤 UI → 비기술 사용자의 실험 → 프로덕션 연결 순으로 올라가고, 마지막 단계에서 [[production-trace-eval-flywheel|프로덕션 트레이스 → 오프라인 eval]] 루프가 완성된다. 그 뒤에 남는 것은 UI가 아니라 거대한 반정형 트레이스를 두 워크로드로 쿼리하는 systems problem이다.** [[braintrust|Braintrust]] 발표([[tech-bridge-braintrust-eval-platform-systems-problem]], [[hossein-niazmandi|Hossein Niazmandi]])가 제시한 틀이다.

> *"it's not necessarily that it's just a UI or UX problem, but building an eval platform truly becomes a systems problem."* (12:38~12:46)

⚠️ **벤더의 틀.** 화자는 eval 플랫폼을 파는 회사 사람이고, 이 틀은 "직접 만들기 어렵다"는 결론으로 간다. 단계 번호 2~4는 챕터(업로더)의 것이고 화자는 *"phase one"*(06:45)만 번호를 붙인다.

## 출발점 — 최소 eval 시스템

세 요소(03:30~03:54): ① 테스트 입력에 에이전트를 실행하는 방법 ② 출력·점수를 보는 방법(*"even if those are being logged in a spreadsheet"*) ③ 에이전트를 호출할 입력 예시 세트(프롬프트·요청·컨텍스트). *"spreadsheet-based evals are not wrong"*(04:08~04:12).

## 네 단계

| 단계 | 핵심 | 누가 들어오나 | 막히는 곳 |
|---|---|---|---|
| ① 스프레드시트 | *"a for loop with a set of input examples"*(07:00~07:02), 진입 장벽 0 | 엔지니어 | *"only documenting"*, 분석·사람 채점·협업 약함, *"domain experts are usually boxed out"*(07:48~07:51) |
| ② 맞춤 UI | product engineer가 bespoke UI(08:00~08:10) | **PM** | *"Still just a reporting tool."*(08:54), 장기 분석 불가 |
| ③ 실험 | 비기술 사용자가 시스템 프롬프트·모델·파라미터를 바꿔 *"side-by-side comparison"*(09:18~09:22) | PM·SME | 테스트 케이스가 오프라인 *"curated set"* |
| ④ 프로덕션 연결 | *"once I ship it to the production, I'm operating in the blind"*(09:45~09:50) → 트레이스 기록 → 실패 모드 → 오프라인 eval → 배포 | (+ 코딩 에이전트, 아래) | 이제 **유지**가 문제 — *"You own this this product that you've built."*(11:02~11:05) |

## 왜 systems problem인가 (11:13~13:30)

- 데이터 모양: *"agent traces are nasty. They are semi-structured JSON."* 상호작용당 *"hundreds of megabytes"*, 전통적 heartbeat 관측은 *"just kilobytes"* — ⚠️ 사례 묘사, 분포 없음.
- 저장: *"your typical cloud data warehouses kind of collapse under this type of volume and load."*(11:30~11:34)
- ⭐ **두 워크로드**: 실시간(사용자가 지금 나쁜 경험을 하는가) vs 장기 실행 쿼리(fine-tune, judge 결과 주석으로 하는 alignment) — *"Two different workloads."*(12:23~12:25)
- 읽기 패턴: 대량 집계 + 시점 스냅샷. 그리고 RBAC·data masking 같은 거버넌스(15:27~15:36, 자사 구현 나열).

## 다섯 번째 사용자 — 에이전트

*"agents have become a first-class citizen of these eval platforms"*(13:47~13:52) — 코딩 에이전트에 자연어로 *"Find me all traces in the last 24 hours where the user had a poor experience. Run the evals for me."* 사람의 몫은 *"review the outcome"* 하고 어떤 버전을 배포할지 정하는 것(16:05~16:23). → [[agent-native-interface]]

## 이 위키에서의 좌표

- [[production-trace-eval-flywheel]] — 이 틀의 ④단계가 그 페이지의 루프다. W&B는 *루프의 칸* 을, Braintrust는 *루프에 이르는 도구의 진화* 와 *루프를 받치는 인프라* 를 말한다.
- [[skill-evals]] · [[field-level-unit-test-evals]] — ①~③단계의 **단위·방법**(무엇을 어떻게 재나). 이 페이지는 **도구·조직**(어디에 기록하고 누가 보나)의 축.
- [[taste-encoded-evals]] — ③·④단계에서 사람(PM·SME)이 하는 일이 judge 보정으로 수렴한다.
- [[agent-action-record]] — ④단계의 전제(모든 입력·출력·스텝 기록)와 그 저장 비용.
- [[trace-to-memory-loop]] — 같은 날 ingest된 LangChain 발표는 트레이스의 목적지를 eval 하나가 아니라 history · eval 데이터셋 · 메모리 갱신 셋으로 나눈다.

> ⚠️ **Contradiction (약)**: [[field-level-unit-test-evals]]는 *유닛 테스트형 eval이 통과하면 에이전트가 안정적* 이라 하고, 이 틀은 *"gone are the days where you build once with unit tests and regression tests, you ship to production, and you don't think about it"*(05:40~05:46)이라 한다 — 앞은 해상도, 뒤는 drift와 지속 관측을 겨눠 정면 충돌은 아니다.

## ⚠️ 유보

- 단계 구분의 근거는 화자의 관찰(*"the eval platforms that we see"* 05:58)뿐 — 조사·표본 없음.
- build vs buy 이해관계: 결론이 자사 제품으로 간다.
- 스프레드시트 단계를 *"no shame"* 이라 하면서도 *"returns diminish pretty quickly"* — 언제 다음 단계로 가야 하는지 기준은 없다.

## References

- [[tech-bridge-braintrust-eval-platform-systems-problem]] (first-seen) · [[braintrust]]
- 관련: [[production-trace-eval-flywheel]] · [[taste-encoded-evals]] · [[skill-evals]] · [[field-level-unit-test-evals]]
