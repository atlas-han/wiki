---
title: Taste Labs
type: entity
category: org
tags: [design, ai-slop, evaluation, post-training, brand, startup]
aliases: [테이스트 랩스]
links: []
sources: [tech-bridge-taste-labs-measuring-slop]
created: 2026-09-12
updated: 2026-09-12
---

# Taste Labs

**AI 슬롭을 끝내는 것**을 사명으로 하는 스타트업. 창업자 [[thais-castello-branco]]의 발표([[tech-bridge-taste-labs-measuring-slop]]) 기준 *"몇 주 전에 스텔스에서 나왔다"*. 첫 기둥은 **디자인**(다음은 글쓰기). 이 위키에 회사 URL은 없다 — 설명란에 창업자 링크만 있다.

> ⚠️ 이 페이지의 모든 내용은 **창업자의 자기 진술**이다. 수치·논문·독립 검증 없음.

## 두 방식으로 일한다

| 층 | 고객 | 하는 일 |
|---|---|---|
| **모델 층** | 프론티어 랩 | 모델 평가 → 어디서 깨지는지 → **post-training 데이터·환경** 구성. 디자인을 *거의 결정론적인 조각*(팔레트·대비·정렬)과 *전문가가 갈리는 조각*(미학 → 데이터)으로 분해 |
| **앱 층** | 에이전트·앱 회사 | 기성 모델이 **평균으로 무너지는** 문제를 컨텍스트·판단·검증으로 |

## 연구

- **웹사이트 200만 개**(지난 약 10년, Wayback Machine 방식) + **합성 AI 사이트** 비교 → AI 이전부터의 동질화, AI 이후의 맥락 무관 반복. → [[ai-slop]]
- **프로브** — 특징(색·타이포·레이아웃·대상) 마이닝 → 소형 분류기 → 결합으로 슬롭 예측. *"LLM-as-a-judge보다 낫다."* → [[slop-probes]]

## 제품

| 이름 | 상태 | 내용 |
|---|---|---|
| **창의성 API** | 별명, *"공식 이름이 될지 모르겠다"* | 에이전트를 위한 *영감 기계* — 의도적 분포 이탈 → [[intentional-out-of-distribution]] |
| **Brand API** | **첫 공개 제품, 디자인 파트너와 베타** | 브랜드 URL → 에이전트가 따르고 사람이 판단할 구성 요소 → [[structured-brand-context]] |
| **브랜드 인덱스** | 만드는 중 | 브랜드 없는 소비자를 위한 미리 설계된 브랜드 시스템 저장소 (생성 대신 검색) |
| **프로브 게이트** | (용도 언급) | *"에이전트가 슬롭을 출시하지 못하게"* |

## 이 위키에서의 자리

[[anthropic-harness-design-long-running-apps]]가 *AI slop 패턴 페널티* 를 평가자 프롬프트에 쓴 것을 **회사의 사업**으로 만든 첫 조직. 그리고 [[signal-layer]]가 *AI는 수렴 기계* 라 한 관찰을 데이터로 뒷받침했다고 주장한다. 같은 날 [[impeccable]]([[paul-bakaus]])과 취향의 훈련 가능성에서 반대편 → [[taste-vs-judgment]].

## References

- [[tech-bridge-taste-labs-measuring-slop]] · [[thais-castello-branco]]
- 관련: [[ai-slop]] · [[slop-probes]] · [[structured-brand-context]] · [[intentional-out-of-distribution]]
