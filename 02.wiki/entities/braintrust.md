---
title: Braintrust
type: entity
category: org
tags: [evals, observability, eval-platform, tracing, llm-ops, vendor]
aliases: [Brain Trust, 브레인트러스트, 브레인 트러스트, braintrust.dev]
links:
  - "https://www.braintrust.dev"
  - "https://x.com/braintrust"
sources: [tech-bridge-braintrust-eval-platform-systems-problem]
created: 2026-10-12
updated: 2026-10-12
---

# Braintrust

**AI 에이전트의 eval·observability 플랫폼 회사.** 이 위키에는 [[tech-bridge-braintrust-eval-platform-systems-problem]]으로 처음 들어왔다. 발표자는 설명란 기준 [[hossein-niazmandi|Hossein Niazmandi]](자막엔 이름·직함 없음).

> *"Braintrust as a platform is focused around agent quality. And the core idea is helping teams build and maintain confidence with the AI features or the AI agents that they're shipping."* (00:02~00:17)

⚠️ 표기: en-orig는 *"Braintrust"*(00:02, 14:45, 14:57)와 *"Brain Trust"*(11:42)로 흔들린다 — 설명란 `braintrust.dev` 로 판독. ko는 "브레인트러스트"·"브레인 트러스트".

## 소스에서 확인되는 것 (⚠️ 전부 당사자 진술)

| 항목 | en-orig |
|---|---|
| 포지셔닝 | 에이전트 품질의 두 기둥 — **evals**(프로덕션 전)와 **observability**(프로덕션 중) (00:18~01:19) |
| 자사가 겪은 문제 | *"this is the same problem that we ran into"*(11:38~11:40) — 반정형 JSON 트레이스, 상호작용당 수백 MB, 일반 클라우드 DW의 붕괴, 실시간 쿼리 vs 장기 쿼리 |
| **BTQL** | *"we built an abstraction layer called BTQL, which is a another form of complexity, because you want an interface for people to be able to query that data."*(12:25~12:33) — ⚠️ 문법·구현은 발화되지 않는다. 설명란에 `braintrust.dev/docs/reference/sql` 링크가 있으나 BTQL과의 관계는 자막에 없다(링크 열어 보지 않음) |
| **unknown unknowns** | *"Braintrust can surface these insights automatically. Because we log your tracing data into our platform, we can run inference on them, and we can tell you the unknown unknowns."*(14:57~15:12) — 조용한 실패, 같은 요청 반복으로 드러나는 사용자 좌절 |
| 언급만 된 구현 | *"the underlying database that powers it, or having to build our back[=RBAC] into the system to manage controls and permissions, or data masking"*(15:27~15:36) |

## 이 위키에서의 위치

- **eval 도구 회사의 두 번째 1인칭 소스** — [[weights-and-biases|W&B]]([[wandb-weave|Weave]], [[tech-bridge-wandb-aria-self-improving-agent]]) 다음. 같은 [[production-trace-eval-flywheel]]을 그리지만, W&B는 *자사 에이전트가 스스로 루프를 돈다* 를, Braintrust는 *사용자의 코딩 에이전트가 headless로 돌고 사람이 배포를 결정한다* 를 말한다.
- 관측·eval 도구 시장의 다른 이름: [[arize-ai|Arize AI]]([[tech-bridge-death-of-code-review]] · [[tech-bridge-uber-debug-assist]]) · [[langsmith|LangSmith]]([[tech-bridge-langchain-learning-agent-memory]], 같은 날 ingest — 트레이스를 eval이 아니라 메모리 갱신으로도 보낸다).
- 화자가 이 위키에 들여온 틀 → [[eval-platform-maturity-stages]].

> ⚠️ **build vs buy 이해관계.** 발표 논지("eval 플랫폼은 직접 만들기 생각보다 어렵다")가 곧 자사 제품의 존재 이유다. 측정·고객 사례·가격은 발화되지 않는다.

## 미해결 사항

- BTQL의 정체(SQL 방언인지, 별도 언어인지), 저장소(*"the underlying database"*)의 정체.
- unknown unknowns 발굴의 방법·정확도.
- 화자 직함(설명란에도 없음).

## References

- [[tech-bridge-braintrust-eval-platform-systems-problem]] · [[hossein-niazmandi]]
- <https://www.braintrust.dev> · <https://www.braintrust.dev/docs/reference/sql> · <https://x.com/braintrust> (⚠️ 열어 보지 않았다)
