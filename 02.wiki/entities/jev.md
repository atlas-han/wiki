---
title: Jev (TypeSafe AI)
type: entity
category: model
tags: [typesafe, system-1-model, classifier, typed-output, structured-decisions, vendor]
aliases: [Jev, 제브, Jev-as-a-judge]
links:
  - https://typesafe.ai/
sources: [tech-bridge-jev-agent-harness]
created: 2026-09-26
updated: 2026-09-26
---

# Jev (TypeSafe AI)

[[typesafe-ai|TypeSafe AI]]의 **"System 1 모델"**. 텍스트를 생성하지 않고, **상태(state)와 질문을 받아 타입이 지정된 답(typed answers)과 확률을 반환**한다(TypeSafe 문서를 인용한 [[langchain|LangChain]] 쪽 설명). 이 위키에서 Jev가 **실제로 서술되는 첫 소스**는 [[tech-bridge-jev-agent-harness]](2026-09-25 업로드)다. → [[system-1-model]]

> ⚠️ **모든 정보가 파트너(LangChain)의 제품 소개 영상 한 편에서 왔다.** TypeSafe 자신의 문서·논문·모델 카드를 이 위키는 읽지 않았다. 09-19 [[tech-bridge-rlhf-assistance-vs-automation|Diogo Almeida 편]]은 제목·설명란에만 이 이름이 있고 **자막에는 한 번도 없었다.**

## 소스에서 확인되는 것

| 항목 | 내용 (출처 [[tech-bridge-jev-agent-harness]]) |
|---|---|
| **정의** | *"소프트웨어가 바로 사용할 수 있는 빠르고 구조화된 결정을 내리도록 만들어진 AI 모델 [부류]"* — *"그들의 문서에 따르면"* (01:52~01:59) |
| **입출력** | 상태 + 질문 → **타입이 지정된 답과 확률** (02:01~02:06). *"텍스트를 입력받아 텍스트를 생성하지 않는다"* (02:14~02:20) |
| **질문 유형** | **choice**(하나 고르기) · **score**(척도) · **Boolean**(예/아니오) (04:28~05:13) |
| **병렬** | 한 상태에 여러 질문 → *"병렬로 답한다"* (05:16~05:25) |
| **위치** | *"LLM의 drop-in 대체가 아니다"* — 전문화된(분류형) 작업만 (02:35~02:43) |
| **주장된 성능** | 분류형 작업에서 LLM 대비 *"20~200배 빠르고 40~400배 저렴할 수 있다"* (02:22~02:34) — ⚠️ **출처·측정 조건 없음** |
| **데모** | PII 판정: LLM *"약 5초"* vs Jev *"거의 즉시"*, 98% (03:40~03:50) — ⚠️ 1회 시연 |
| **접근** | typesafe.ai에서 API 키 · LangChain 통합(`langchain-typesafe`, ⚠️ ASR 기준 표기) (05:38~05:49 · 08:51~09:00) |

## 소스가 든 용도 (LangChain 쪽)

1. **모델 라우팅** — 프롬프트를 기준에 비추어 빠른 모델/강한 모델 중 선택 → [[model-mixing-economics]]
2. **auto mode** — 도구 호출의 위험을 분류해 런타임에 차단. 화자는 *"기존 분류 단계가 너무 느려서 auto mode를 껐다가 Jev 덕에 다시 켰다"*(07:02~07:16) → [[transcript-classifier]]
3. **Jev-as-a-judge** — 루브릭 항목별로 에이전트 답을 채점하는 온라인 eval → [[generator-evaluator-pattern]]

## 이름

카너먼 『Thinking, Fast and Slow』의 **System 1(빠르고 싼 직관) / System 2(느리고 비싼 추론)** 에서 왔고, 표준 LLM을 System 2 쪽에 두는 **"의도적 대조"** 라고 한다(02:46~03:25). ⚠️ *"Jev"* 라는 단어 자체의 유래는 말하지 않는다.

## ⚠️ Diogo Almeida의 "제3의 목표"와의 관계 — 미확정

[[diogo-almeida]]는 TypeSafe가 *"보정된 의사결정(calibrated decision-making)에 최적화된 세 번째 것"* 을 한다고 했다(→ [[post-training-northstars]]). Jev가 그 목표로 학습된 모델인지는 **어느 소스도 말하지 않는다** — Almeida 편에는 Jev라는 이름이 없고, LangChain 편에는 Almeida·보정·학습 목표가 없다. *"확률을 반환한다"* 와 *"API의 모양이 다르다"* 가 **양립한다는 정황**뿐이다. 반환되는 확률이 **보정(calibrated)되어 있는지도 주장되지 않았다.**

## 미해결 사항

- 모델 크기·아키텍처·학습 방식·학습 데이터 — 전무.
- 정확도·보정 품질·실패 사례 — 전무(PII 98% 한 건).
- 20~200배 / 40~400배의 기준 LLM·작업·하드웨어.
- 출시일(*"방금 나온"* 뿐).
- choice 응답의 *score 0.84 / confidence 0.596* 이 각각 무엇인지.

## References

- [[tech-bridge-jev-agent-harness]] — first-seen (실질 서술)
- [[tech-bridge-rlhf-assistance-vs-automation]] — 제목·설명란에만 이름이 있던 09-19 소스
- [[typesafe-ai]] · [[langchain]] · [[diogo-almeida]]
- 관련: [[system-1-model]] · [[model-mixing-economics]] · [[transcript-classifier]] · [[generator-evaluator-pattern]] · [[post-training-northstars]]
- 외부: <https://typesafe.ai/>
