---
title: "적시형 온톨로지 (Just-in-Time Ontology)"
type: concept
category: theory
tags: [ontology, schema, data-transformation, universal-schema, decision-context, provenance, reuse, data-engineering]
aliases: [just-in-time ontology, JIT ontology, 적시형 온톨로지, 적시 온톨로지, 보편 스키마는 없다, no universal schema, four schemas]
related: [cross-model-prior-intersection, pareto-surfing, multimodal-elicitation, deterministic-agent-pipeline, intelligence-abundance, system-1-model, document-context-layer]
first-seen: tech-bridge-just-in-time-ontology
sources: [tech-bridge-just-in-time-ontology]
created: 2026-10-18
updated: 2026-10-18
---

# 적시형 온톨로지 (Just-in-Time Ontology)

**보편 스키마는 없으니, 데이터가 기록된 맥락과 결정의 맥락을 결정 공간이 알려진 순간에 병합하고, 그렇게 만든 온톨로지를 근거(receipts)와 함께 남겨 다음 일에 재사용하라는 주장이다.** [[hrishi-olickel|Hrishi Olickel]]([[southbridge|Southbridge]])이 [[tech-bridge-just-in-time-ontology]]에서 제시했다. 전제는 판단(judgment)이 싸졌다는 것이다: *"All of our data infrastructure today is built on the idea that transformation is expensive. What if that wasn't true anymore?"*(00:26~00:35)

> *"Doing that merge when the decision space is known instead of ahead of time is what I mean by a just-in-time ontology."* (04:55~05:03)
>
> *"It's built when the job needs it, kept with its receipts, and reused when the next job needs the same thing."* (20:03~20:10)

## 왜 보편 스키마는 실패하는가 — 스키마 넷

흔한 설명(buy-in 부족, 중도 포기)은 맞지만 주된 이유가 아니다. 모든 정보를 한순간에 슈퍼 스키마로 옮길 수 있어도 *"there is no super schema. There actually are four schemas."*(02:28~02:32)

| 스키마 | 무엇이 정하나 | 온도 예 |
|---|---|---|
| source | 정보가 어디서 왔나 | 휴대폰의 지역 온도 · 책상 센서 · 시계 · 요청을 따른 사람의 인내심 |
| storage | 무엇을 적을 수 있나 | 기기 펌웨어도 초 단위 시각도 못 적는다 |
| decision | 왜 필요한가 | 쾌적함(같은 사람의 하루 측정) · 기상 지도(위치·시각·기기) · 장비 설치(측정자가 상쇄할 변수) |
| prior | 모델이 가져오는 믿음 | *"the one the model brings with it"*(14:05~14:07) → [[cross-model-prior-intersection]] |

*"The true problem is that you will never know all four schemas at the same time except at the moment that the decision is being made."*(03:53~04:00) 고객이라는 *"the first box in every ontology"*도 청구(누가 내나)·지원(누가 전화하나)·컴플라이언스(누구에 대해 책임지나)마다 다르다(04:06~04:19). *"There is no concept of a customer that's divorced from the question that you want to answer."*(04:38~04:42)

## 두 절반

1. **결정 시점 병합.** 변환은 *"Taking the context that it was recorded in and merging it with the context of the decision"*(04:48~04:54)이고 *"that takes discernment"*다. 그것을 미리 하지 않고 결정 공간이 알려졌을 때 한다.
2. **근거와 함께 재사용.** 파이프라인 안에서 온톨로지는 *"intermediates between intelligence and result, which makes them easier to reuse"*(19:53~20:01)다. 오하이오 사례에서는 정의(위원회란, filer란, 한 주소의 두 사람이란)를 라운드마다 고정했고, *"Every one of Ohio's 203,317 cases now has a label that says what the answer rests on, and how far it was checked."*(11:57~12:07)

맺음: *"there is no ontology. Not a universal one, at least. (…) this makes every ontology and schema valid, as long as you can label and preserve the context around it."*(20:21~20:34)

## 위키의 다른 페이지와

- [[multimodal-elicitation]]: 커머스 에이전트가 사용자 제약과 카탈로그 온톨로지 사이에 *"임시적인 연결 고리"*를 먼저 놓는다. 질의 시점 매핑이라는 같은 방향이다.
- [[system-1-model]]: 정의를 질문으로 바꿔 싼 결정 모델에 묻는 것이 병합의 실행 수단이다. Jev의 오답은 모델이 아니라 질문의 정의를 고쳐 바로잡았다(11:34~11:45).
- [[deterministic-agent-pipeline]]: 단계 사이 결정론 검사(rig)가 근거 라벨을 남기는 자리다.
- [[intelligence-abundance]]: 변환 비용 하락이 전제다.
- [[pareto-surfing]]: 재사용되는 온톨로지가 다음 최적화의 기준선이 된다.

## ⚠️ 유보

- 근거는 소스 하나(화자 회사의 사례)다. "온톨로지를 미리 설계하는 쪽"의 반론을 이 위키는 아직 듣지 않았다.
- receipts의 형식(어떤 필드, 어디에 저장)은 발화되지 않는다. 라벨이 *"what the answer rests on, and how far it was checked"*를 담는다는 것까지다.
- 넷째 스키마(prior)를 "스키마"로 부르는 것은 화자의 용어 확장이다.

## References

- [[tech-bridge-just-in-time-ontology]] — first-seen
- [[hrishi-olickel]] · [[southbridge]]
- 관련: [[cross-model-prior-intersection]] · [[pareto-surfing]] · [[multimodal-elicitation]] · [[system-1-model]] · [[deterministic-agent-pipeline]] · [[intelligence-abundance]]
