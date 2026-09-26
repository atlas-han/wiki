---
title: "System 1 모델 (분류형 결정 모델을 하네스 부품으로)"
type: concept
category: architecture
tags: [system-1-model, classifier, typed-output, structured-decisions, agent-harness, model-routing, guardrails, llm-as-judge, latency, cost]
aliases: [System 1 model, 시스템 1 모델, typed decision model, 분류형 결정 모델]
related: [jev, typesafe-ai, agent-harness-design, harness-engineering, model-mixing-economics, transcript-classifier, generator-evaluator-pattern, slop-probes, post-training-northstars, privacy-auto-mode]
first-seen: tech-bridge-jev-agent-harness
sources: [tech-bridge-jev-agent-harness]
created: 2026-09-26
updated: 2026-09-26
---

# System 1 모델

**텍스트를 생성하지 않고, 상태(state)와 질문을 받아 타입이 지정된 답(choice · score · Boolean)과 확률을 즉시 돌려주는 모델 — 그리고 그런 모델을 에이전트 하네스 안의 결정 지점(라우팅 · 안전 게이트 · 채점)에 끼워 LLM 호출을 대신하게 하는 설계.** 이름은 카너먼의 System 1(빠르고 싼 직관) / System 2(느리고 비싼 추론)에서 왔고, 표준 LLM을 System 2에 둔다. 이 위키에는 [[tech-bridge-jev-agent-harness]]([[langchain|LangChain]]이 소개한 [[typesafe-ai|TypeSafe]]의 [[jev|Jev]])로 들어왔다.

> 그들의 문서에 따르면, **System 1 모델은 소프트웨어가 바로 사용할 수 있는 빠르고 구조화된 결정을 내리도록 만들어진 AI 모델 [부류]**입니다. **System 1 모델은 상태(state)와 질문을 평가하고 타입이 지정된 답변(typed answers)과 확률을 반환합니다.** — [[tech-bridge-jev-agent-harness]] (01:52~02:06)

> ⚠️ **이 개념의 유일한 소스는 벤더 영상 한 편**이고, 용어 자체가 **한 회사(TypeSafe)의 제품 범주 이름**이다. 이 위키는 이것을 일반 개념으로 올리되, "System 1 모델"이라는 범주에 Jev 외의 사례가 있다는 근거는 **없다.**

## 구조를 어디서 얻는가 — 세 단계

| 단계 | 방법 | 모델의 출력 |
|---|---|---|
| 1 | **도구 호출** — 구조화된 요청 | 텍스트 + 구조화된 요청 |
| 2 | **구조화된 출력** — 출력 타입 바인딩, JSON 스키마 준수 | 스키마에 맞춘 텍스트 |
| 3 | **System 1 모델** | **텍스트 없음 — 타입이 지정된 답 + 확률** |

소스의 서사(00:39~01:34 → 01:38~02:20)가 이 순서다: LLM은 *text in / text out* 이라 **구조를 바깥에서 덧대 왔고**, System 1 모델은 **처음부터 구조로 답한다.** *"LLM의 drop-in 대체가 아니다"*(02:35) — 열린 문제의 단계별 추론은 여전히 LLM(System 2)의 몫이다.

## 인터페이스

- **입력**: 상태(텍스트 한 덩어리) + 질문 여러 개
- **질문 유형 셋**: **choice**(하나 고르기, 예: 어느 팀이 처리하나) · **score**(척도, 예: 얼마나 화났나) · **Boolean**(예/아니오, 예: 긴급한가)
- **출력**: 질문별 타입 답 + 확률/점수
- **병렬**: *"하나의 상태에 많은 질문을 보낼 수 있고 (…) 병렬로 답한다"*(05:16~05:22)

→ 이 모양이 [[post-training-northstars]]에서 [[diogo-almeida]]가 말한 *"API의 모양조차 다르다"* 의 한 구체형일 **수는 있지만**, 두 소스 모두 이 연결을 하지 않는다. ⚠️ 위키의 관찰일 뿐이다.

## 하네스 안의 세 자리

에이전트 루프에는 **"LLM에게 시키고 있지만 사실은 분류인 결정"** 이 많다는 것이 전제다(*"현재 우리가 에이전트에게 LLM으로 시키는 분류·의사 결정 [스타일] 작업 중에는 속도와 비용 면에서 더 최적일 수 있는 것이 많다"*, 03:58~04:07).

| 자리 | 질문 | 위키의 인접 페이지 |
|---|---|---|
| **라우터** | 이 프롬프트는 빠른 모델로 충분한가 | [[model-mixing-economics]] — *"난이도를 누가 판정하나"* 의 한 답 |
| **안전 게이트** | 이 도구 호출은 위험한가 | [[transcript-classifier]] · [[privacy-auto-mode]] |
| **judge** | 이 답은 루브릭 항목 각각을 만족하나 | [[generator-evaluator-pattern]] · [[slop-probes]] |

세 자리의 공통점: **매 스텝(또는 매 트레이스)마다 호출되므로 지연과 단가가 곱해진다.** 그래서 이 설계의 논거는 정확도가 아니라 **속도·비용**이다.

## 지연이 게이트를 끄게 만든다

> **최근 제 코딩 에이전트에서 auto mode를 껐었습니다. 주어진 [도구 호출]이 위험한지 분류하는 단계가 너무 느려서** (…) **하지만 Jev가 이렇게 빨리 결정할 수 있으니 [지금은 다시 켜 두었습니다].** — [[tech-bridge-jev-agent-harness]] (07:02~07:16)

이 위키가 안전 분류기를 다룬 자리([[transcript-classifier]])는 FPR/FNR만 봤다. 여기서 **지연이 채택률을 결정한다**는 축이 추가된다 — 느린 게이트는 정확해도 **꺼진다.** 09-19 [[model-mixing-economics]]의 *기준이 지연일 때*(음성 에이전트)와 같은 방향의 관찰이다.

## ⚠️ 유보

- **정확도가 비어 있다.** 소스는 속도·비용만 비교하고 **분류 품질을 LLM과 비교하지 않는다**(judge 쪽의 *"더 신뢰할 수 있고 일관적"* 은 블로그의 구두 전언). 안전 게이트에서 속도를 얻고 **놓친 위험(FNR)** 이 늘었는지 알 수 없다.
- **확률의 의미.** *"확률을 반환한다"* 는데 그것이 **보정(calibrated)** 되어 있는지는 주장되지 않았다 — 게이트 임계값을 정하려면 필수인 정보다. → [[decision-quality]]
- **수치.** *"20~200배 빠르고 40~400배 저렴"*(02:22~02:34)의 기준 LLM·작업·하드웨어가 없다.
- **LLM은 순차적이라는 대조**(05:28~05:32)는 벤더의 성격 규정이다. LLM도 한 호출에서 여러 필드를 구조화된 출력으로 채울 수 있다 — 차이는 **생성 비용**이지 병렬 가능성이 아닐 수 있다(⚠️ 위키의 추정).
- **텍스트 없는 답의 감사 가능성.** 게이트가 *왜* 막았는지 설명이 남지 않는다. [[transcript-classifier]]의 2단계 CoT와 대조되지만 소스는 이를 다루지 않는다.

## References

- [[tech-bridge-jev-agent-harness]] — first-seen
- [[jev]] · [[typesafe-ai]] · [[langchain]]
- 관련: [[agent-harness-design]] · [[harness-engineering]] · [[model-mixing-economics]] · [[transcript-classifier]] · [[generator-evaluator-pattern]] · [[slop-probes]] · [[post-training-northstars]] · [[decision-quality]]
