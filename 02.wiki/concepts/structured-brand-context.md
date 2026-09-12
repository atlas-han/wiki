---
title: 구조화된 브랜드 컨텍스트 (Structured Brand Context)
type: concept
category: pattern
tags: [brand, context, design, retrieval, adherence, agent, ai-slop]
aliases: [Brand API, brand adherence, 브랜드 준수, 브랜드 API]
related: [ai-slop, agentic-sites, context-engineering, agent-knowledge-sourcing, retrieval-augmented-generation, multimodal-elicitation, slop-probes, adjective-verb-steering]
first-seen: tech-bridge-taste-labs-measuring-slop
sources: [tech-bridge-taste-labs-measuring-slop, tech-bridge-impeccable-design-steering]
created: 2026-09-12
updated: 2026-09-12
---

# 구조화된 브랜드 컨텍스트

**모호한 브랜드를 에이전트가 따를 수 있을 만큼 구체적인 구성 요소로 추출하고, 같은 구조를 사람이 대조해 판단하는 기준으로도 쓴다. 브랜드가 없는 사용자에게는 생성 대신 미리 설계된 브랜드 시스템을 검색해 준다.** [[taste-labs|Taste Labs]]의 첫 공개 제품 *Brand API*([[tech-bridge-taste-labs-measuring-slop]])가 first-seen.

## 문제 — 이미 해 놓은 일을 안 쓴다

> 훌륭한 브랜드는 수십 명의 디자이너가 많은 장인정신과 생각과 정성을 들인 결과죠. 그래서 우리는 이미 **그 회사에 무엇이 훌륭한지 정의하는 일을 미리 해 놓고는, 그걸 잘 쓰지 않고 있는** 겁니다. — [[thais-castello-branco]] (11:15~11:29)

[[ai-slop]]의 세 특징 중 **적합성 부족(lack of fit)** 에 대한 처방이다. 슬롭이 *애완동물 가게와 금융 회사의 사이트가 수렴하는 것* 이라면, 브랜드는 **이미 존재하는 맥락**이고 그것을 에이전트에게 주지 않은 것이 문제다.

## 두 방향 — 따르게 하고, 판단하게 한다

> 브랜드처럼 모호한 것을 **에이전트가 따르기 쉽고, 또 여러분이 그것에 대조해 판단할 수 있을 만큼** 구조화된 것으로 바꾸는 거죠. 여기서 잊으면 안 되는 조각이 **판단과 검증**입니다. (12:07~12:19)

| 방향 | 누가 | 무엇을 |
|---|---|---|
| **생성 측** | 에이전트 | 추출된 구성 요소를 **따른다** |
| **검증 측** | 사람(또는 게이트) | *"에이전트가 실제로 궤도에 있는가? 이 브랜드를 잘 준수하고 있는가? 어떻게, 어디서 실패하고 있는가?"* |

같은 구조가 프롬프트이자 루브릭이다 — [[generator-evaluator-pattern]]이 *생성기·평가기 양쪽 프롬프트에 같은 기준을 주입* 한 것과 같은 형태이되, 기준이 사람이 쓴 것이 아니라 **브랜드에서 추출된 것**이다.

## 생성 대신 검색 — 브랜드 인덱스

> 그 앱을 쓰는 사람이 **브랜드가 없다**면 — 평균적인 소비자라면? (…) **몽환적인(dreamy)** 느낌을 원하면 — 그 순간 생성적 접근으로 만들었다가 별로거나 다시 슬롭의 기둥에 빠지는 대신 — 이미 **응집력 있게 설계된 몽환적인 브랜드 시스템을 검색해** 오면 왜 안 되겠어요? (12:43~13:09)

이것은 [[agent-knowledge-sourcing]]의 4갈래 중 **RAG**(적어둔 것을 필요할 때 가져온다)를 미학에 적용한 것이고, [[multimodal-elicitation]]이 *사용자가 어휘를 갖고 있지 않아도 이미지에 마우스를 올릴 수는 있다* 고 한 것의 **공급 측** 대응물이다 — 감성 키워드 하나로 **응집된 시스템 전체**를 가져온다.

## 시연 (⚠️ 슬라이드)

*General Intelligence Compute of New York*(ASR, 회사명 미확정)의 브랜드로 슬라이드 덱을 만들 때 — 왼쪽 원본 / 가운데 *"Claw Design"*(Claude Design 추정)의 기본 출력 / 오른쪽 추출 적용. *"원본에 훨씬 충실도가 높고, 디테일까지 맞는 느낌"* — **화자의 평가이며 자막으로 검증 불가.**

## 이 위키에서의 자리

- **[[agentic-sites]]**([[adobe]])와 같은 문제, 다른 형태. 그쪽은 *"브랜드 가이드라인이 환각 예산을 정한다"* 며 **사이트 전체를 RAG 코퍼스로** 써서 생성물이 정의상 기존 사이트에 근거하게 했다. 여기서는 **브랜드를 추출된 구성 요소로** 만들어 에이전트에게 준다. 코퍼스 vs 구조 — 후자가 검증 루브릭으로 재사용된다는 점이 다르다. ⚠️ 두 소스는 서로를 모른다.
- **[[adjective-verb-steering]]**([[impeccable]])의 *"bolder는 **디자인 시스템을 깨지 않으면서** 위계·스케일·타이포를"* 은 같은 제약을 **어휘 정의 안에** 넣은 것이다. Brand API가 제약을 *데이터로* 준다면 Impeccable은 *단어의 뜻으로* 준다.
- **[[context-engineering]]** — 브랜드는 [[agent-skills|스킬]](절차)도 [[agent-memory|메모리]](겪은 것)도 아닌 **제약 컨텍스트**이고, 이 소스는 그것을 *추출 가능한 산출물* 로 본 첫 사례다.

## ⚠️ 미해결

- **구성 요소의 형식** — 토큰인지 규칙인지 예시인지 없음.
- **검증의 주체** — 사람이 보는지 [[slop-probes|프로브]]가 재는지 없음.
- **베타** — 디자인 파트너 수·결과 없음. 당사자 진술.
- 브랜드 인덱스의 **저작권·출처** — 미리 설계된 시스템을 누가 만들었는지 없음.

## References

- [[tech-bridge-taste-labs-measuring-slop]] (first-seen) · [[taste-labs]]
- [[tech-bridge-impeccable-design-steering]] — 디자인 시스템 제약을 어휘에 넣은 대응물
- 관련: [[ai-slop]] · [[agentic-sites]] · [[agent-knowledge-sourcing]] · [[multimodal-elicitation]]
