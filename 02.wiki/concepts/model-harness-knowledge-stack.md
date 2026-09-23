---
title: 모델 · 하네스 · 지식 — 에이전트 개발 스택의 3계층 (Model–Harness–Knowledge Stack)
type: concept
category: architecture
tags: [agent-stack, model-selection, harness, skills, cost, loops, gemini, antigravity]
aliases: [3계층 에이전트 스택, 더 똑똑한 모델이 아니라 더 나은 스택, 모델·하네스·지식]
related: [harness-engineering, model-mixing-economics, agent-skills, antigravity, google-skills, generator-evaluator-pattern, orchestrator-searcher-split, voice-latency-thinking-tradeoff, three-tier-ai-skill-stack]
first-seen: tech-bridge-lopopolo-agent-harness
sources: [tech-bridge-lopopolo-agent-harness]
created: 2026-09-23
updated: 2026-09-23
---

# 모델 · 하네스 · 지식

**코딩 에이전트가 한계에 부딪혔을 때의 반사적 처방(더 무거운 모델)을 거부하고, 스택을 모델 · 하네스 · 지식 세 층으로 나눠 각 층을 따로 고르라는 프레이밍.** 스미타가 [[tech-bridge-lopopolo-agent-harness]] 3부(25:26~30:19)에서 각 층에 Google 제품 하나씩을 붙여 소개한다.

> **코딩 에이전트에 더 똑똑한 모델이 필요한 것은 아닙니다. 더 나은 스택이 필요합니다.** 개발자들이 코딩 에이전트가 한계에 부딪혔다고 느낄 때, **가장 먼저 떠오르는 생각은 더 강력한 기본 모델로 바로 넘어가는 것**입니다. (25:26~25:35)

> 진정으로 뛰어난 성능을 발휘하는 에이전트 기반 개발 스택은 **서로 연결된 세 가지 계층**으로 구성됩니다. **첫째는 모델, 둘째는 하네스, 셋째는 지식입니다.** (25:44~25:53)

## 세 층

### 1. 모델 — 루프가 비용을 곱한다

> **[에이전트]는 기존의 [단일 턴] 프롬프트 박스처럼 작동하지 않습니다. 그것들은 끊임없이 반복 실행됩니다.** 따라서 에이전트는 디렉터리를 검사하고, 함수를 업데이트하고, 단위 테스트를 실행한 다음, **하나의 작업을 완료하기 위해 해당 시퀀스를 20번, 40번 또는 심지어 60번 반복**할 수 있습니다. (26:21~26:37)

> 따라서 **연속적인 홉을 많이 사용하는 경우 속도와 비용이 급격히 증가합니다.** 따라서 **빠르고 비용 효율적인 모델은 결코 성능 저하를 의미하지 않습니다.** (26:37~26:50)

제품: **Gemini 3.8 Flash**. ⭐ **이 위키의 [[model-mixing-economics]]에 새 축**이다 — 지금까지 모델 선택은 *계획은 비싼 모델, 실행은 싼 모델* 식의 **단계 배분**이었는데, 여기서는 **루프 횟수가 곱해지는 비용·지연**이 기준이다. [[voice-latency-thinking-tradeoff]](실시간 제약이 thinking을 금지)와 같은 모양의 논증을 **코딩 루프**에 적용한 것.

### 2. 하네스 — 단일 모델을 팀으로

> **boost는 단일 모델을 조직적인 팀으로 변환하는 슬래시 명령어입니다.** (27:20~27:25)

제품: **[[antigravity|Antigravity]] `/boost`** — 오케스트레이터 · 병렬 하위 에이전트 · **독립 검증 패스**(27:25~27:44). **[[generator-evaluator-pattern]] + [[orchestrator-searcher-split]]의 제품화.** 사용 지침이 붙는다 — **일상 작업은 기본 에이전트**, Boost는 *"매우 복잡한 엔지니어링 문제"* 에만(27:46~28:03).

### 3. 지식 — 에이전트가 모르는 것

> 에이전트가 예를 들어 **클라우드 인프라를 구성하려고 할 때는 어떻게 해야 할까요? 그것은 어떻게 그것을 아는 걸까요?** (28:40~28:47)

> **스킬은 코딩 에이전트가 필요에 따라 불러오는, 엄선된 도메인 지식입니다.** (29:04~29:09)

제품: **[[google-skills|Google Skills]]** — 100+ 스킬(Google Cloud·Firebase·Flutter·Maps), 명령 하나로 설치, **하네스 무관**. → [[agent-skills]]

## 위키에서의 좌표

- **[[harness-engineering]]의 Cole Medin 3계층과 자르는 선이 다르다** — 그쪽은 Base LLM / Tool Harness / **AI Layer**(개발자가 만드는 층)였고 스킬은 AI Layer의 6요소 중 하나였다. 이쪽은 **지식을 독립 층**으로 세우고, **개발자가 만드는 층이 없다** — 세 층 모두 **고르는** 대상이다.
- [[tools-and-context-over-harness|Lopopolo]]와 같은 에피소드에 있지만 **강조가 반대다** — Lopopolo는 하네스를 고정하고 모델을 최신으로, 스미타는 **모델을 가볍게** 하고 하네스에서 **모드를 고른다.** ⚠️ 에피소드는 둘을 연결하지 않는다.
- 이름이 비슷한 [[three-tier-ai-skill-stack]]은 **사람이 배울 기술**의 3층이다. 혼동 주의.

## ⚠️ 유보

- **세 층 모두 한 회사의 제품이다.** 프레이밍 자체는 벤더 중립적으로 쓸 수 있지만 **소스는 그렇게 쓰지 않는다.**
- **수치가 하나도 없다** — Flash의 속도·비용·품질, 20~60회 루프에서의 누적 차이, Boost의 효과, Skills의 품질. Boost의 **세 실행 모드 비교 표는 화면에만** 있다(28:11~28:30).
- **Flash 논거의 반례를 다루지 않는다** — 약한 모델은 **루프 횟수 자체를 늘릴** 수 있다(같은 작업에 더 많은 홉). 비용이 홉 수 × 단가라면 단가만 보는 것은 반쪽이다.
- **보안** — *명령어 하나로 100+ 외부 스킬 설치*(29:34~29:39)의 공급망 문제를 말하지 않는다.

## References

- [[tech-bridge-lopopolo-agent-harness]]
- 제품: [[antigravity]] · [[google-skills]] · [[google-cloud]]
- 관련: [[model-mixing-economics]] · [[voice-latency-thinking-tradeoff]] · [[agent-skills]] · [[harness-engineering]] · [[generator-evaluator-pattern]] · [[orchestrator-searcher-split]] · [[tools-and-context-over-harness]]
