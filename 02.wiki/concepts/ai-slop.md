---
title: AI 슬롭 (AI Slop)
type: concept
category: theory
tags: [ai-slop, design, quality, homogenization, generation, taste]
aliases: [slop, 슬롭, AI slop]
related: [taste-vs-judgment, slop-probes, intentional-out-of-distribution, structured-brand-context, no-one-shot-design, signal-layer, generator-evaluator-pattern, cognitive-offloading, adjective-verb-steering]
first-seen: tech-bridge-taste-labs-measuring-slop
sources: [tech-bridge-taste-labs-measuring-slop, tech-bridge-impeccable-design-steering]
created: 2026-09-12
updated: 2026-09-12
---

# AI 슬롭

**생성 비용이 0에 가까워지면서 쏟아지는, 반복적이고 맥락에 맞지 않고 의도가 없는 산출물.** 이 위키는 이 말을 [[anthropic-harness-design-long-running-apps]]의 평가 기준(*"AI slop 패턴 페널티"*)과 [[tech-bridge-figma-coding-agents]]의 *"sloppy한 글"* 에서 언급만 해 왔고, 2026-09-11 업로드 두 편([[tech-bridge-taste-labs-measuring-slop]]·[[tech-bridge-impeccable-design-steering]])이 처음으로 **정의**를 준다.

## 왜 정의할 수 있는가 — 훌륭함과의 비대칭

> **무엇이 훌륭한지 정의하기는 때로 어렵지만, 무엇이 슬롭인지 정의하기는 꽤 쉽습니다 — 대부분의 사람이 동의한다는 의미에서.** — [[thais-castello-branco]] (03:06~03:12)

수학에서는 *훌륭함 = 정확함* 이지만 디자인·글쓰기에서는 훌륭함이 *고유함·다름·주의를 끎·정성·진정성* 의 조합이라 전문가도 갈린다. 반면 그 **부재**는 모두가 알아본다 — *"반복, 그리고 영혼 없음(soullessness)의 느낌은 지금 AI를 쓰면서 우리 모두가 느끼는 것."* 이 비대칭이 [[slop-probes|측정]]의 근거다.

## 세 가지 특징 (Taste Labs)

| 특징 | 내용 | 처방 (같은 소스) |
|---|---|---|
| **반복(repetition)** | 같은 것을 수없이 본다 | [[intentional-out-of-distribution\|의도적 분포 이탈]] |
| **적합성 부족(lack of fit)** | *"애완동물 가게 웹사이트와 금융 회사 웹사이트가 수렴해서 똑같아 보인다"* — 특정 맥락·시점·사람에게 옳게 느껴지는 능력의 부재 | [[structured-brand-context\|브랜드를 구조화된 컨텍스트로]] |
| **낮은 의도(low intent)** | 원샷 프롬프트 + *"시스템에 빠진 **의도 해석** 조각"* | 판단·검증 게이트 ([[slop-probes]]) · [[fuzzy-intent-discovery]] |

세 특징 중 둘은 서로 묶인다 — 반복이 있으면 적합성이 없다(정성껏 만들었다면 수렴하지 않았을 것).

## 슬롭은 AI 이전부터 있었다 — AI는 가속기

> AI가 등장하기 전에도 인터넷에서 **일종의 붕괴(collapse)** 가 이미 나타나고 있었습니다 — 더 동질적이 되고, 더 비슷한 색상 팔레트, 더 비슷한 레이아웃. (…) 하지만 AI와 함께 이 반복이 훨씬 더 많이, 그리고 거의 **맥락과 무관하게** 나타났습니다. (06:53~07:22)

⚠️ 근거는 Taste Labs의 *10년치 웹사이트 200만 개 + 합성 AI 사이트* 분석이며 **수치가 없다.** 다만 [[signal-layer]]의 [[lena-hall|Lena Hall]]이 *"AI는 수렴 기계 — 모두가 같은 질문을 하기 때문에 모두에게 똑같은 답을 준다"* 라고 한 것과 독립적으로 같은 관찰이다. 원인의 층이 다르다 — Hall은 *질문의 동일성*, Thais는 *기성 모델이 평균으로 무너지는(collapse with the mean) 경향*.

## 슬롭은 움직이는 표적 (Impeccable)

> **대부분의 프론티어 모델에는 더 이상 보라색 그라데이션이 없습니다.** (…) 하지만 **이것도 슬롭**입니다. **움직이는 표적**일 뿐이에요. — [[paul-bakaus]] (05:09~05:26)

| 시기 | 슬롭의 모습 (Paul의 관찰) |
|---|---|
| ~2022 | **보라색 그라데이션**, 전형적 AI 패턴 |
| 2026 | **"Claude 베이지"** — Instrument Serif 서체, 이탤릭. *"꼭 나쁜 디자인은 아니다. 그냥 전부 그렇게 생겼을 뿐"* |

그리고 세부의 흔적(tell) — **섹션 번호**(*"GPT가 아주 좋아하고 Claude도 좋아한다"*). 이 관찰이 이 위키의 [[generator-evaluator-pattern]]에 직접 걸린다: [[anthropic-harness-design-long-running-apps]]의 originality 기준이 페널티로 명시한 *"purple gradients over white cards"* 는 Paul에 따르면 **이미 낡은 예**다. → **고정된 슬롭 목록은 낡는다.** 채점 기준에 시간 축이 있다는 뜻이고, [[harness-pruning]]이 하네스 기능에 대해 말한 것이 **평가 기준에도** 적용된다. ⚠️ 위키의 정리.

## 슬롭 = 결정의 부재

Paul의 정의는 Thais의 *낮은 의도* 를 한 문장으로 압축한다.

> 빠르게 바이브 코딩된 페이지 — **아무도 아무것도 결정하지 않았습니다.** 그냥 원샷한 거예요. (…) **유능해 보일지 몰라도 완전히 비어 있습니다.** (07:43~07:55)

두 소스가 서로 모른 채 같은 자리에 닿는다 — 슬롭은 **품질이 낮은 것**이 아니라(*"유능해 보일지 몰라도"*, *"꼭 나쁜 디자인은 아니다"*) **의도·결정·맥락이 없는 것**이다. 이것이 [[decision-quality]]([[ibm]])의 *"구현 품질은 쉬워지고 결정 품질이 차별화"* 의 디자인 판이다.

## 비용 구조 — 생성은 0, 안목은 평생

> 갑자기 **생성 비용이 사실상 0으로** 갑니다. 그런데 평균적인 사람은 자기 취향을 갈고닦지 않았죠. (03:35~03:41)

그리고 *"모두가 취향을 갖는 것"* 은 비현실적이니(디자이너는 평생 걸린다) 처방은 **바닥의 기준을 올리는 것**이다 — → [[taste-vs-judgment]]. 이것이 [[cognitive-offloading]]([[andrew-ng]])의 우려와 만나는 자리다 — 생성이 무료가 되면 판단을 기를 동기도 사라진다.

## 처방의 두 층

| 층 | Taste Labs | Impeccable |
|---|---|---|
| 모델 층 | post-training 데이터·환경 (프론티어 랩과) | — |
| **추론 시점** | 창의성 API · Brand API · 프로브 게이트 | 형용사·동사 조향 · **auto 없음** |
| 사람의 자리 | **판단**(*"그 어느 때보다 가치 있다"*) | **조향**(*"결정하는 것이 요점"*) |

둘 다 *"모델만 좋아지면 된다"* 를 거부한다 — Thais: *"모델만 더 좋게 만들고 이걸 무시하면 슬롭은 계속 존재할 것"*, Paul: *"디자인을 원샷하는 도구가 될 일은 결코 없다."* [[sutton-bitter-lesson]]의 반례 표에 **추론 시점의 사용자 상호작용**이라는 축을 더한다.

## ⚠️ 미해결

- **측정치 없음** — 200만 사이트 분석의 수치, 프로브 정확도, Impeccable 전후 비교 모두 없다.
- 두 소스 모두 **당사자**(평가·데이터 판매자 / 도구 제작자)이고 서로를 모른다.
- *슬롭* 이라는 말 자체의 범위 — Thais는 디자인·글쓰기, Paul은 웹 디자인. 코드의 슬롭은 어느 소스도 다루지 않는다.

## References

- [[tech-bridge-taste-labs-measuring-slop]] (first-seen) · [[thais-castello-branco]] · [[taste-labs]]
- [[tech-bridge-impeccable-design-steering]] · [[paul-bakaus]] · [[impeccable]]
- 관련: [[signal-layer]] · [[generator-evaluator-pattern]] · [[decision-quality]] · [[taste-vs-judgment]]
