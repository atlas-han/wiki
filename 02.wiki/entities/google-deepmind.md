---
title: Google DeepMind
type: entity
category: org
tags: [frontier-lab, google, commerce, multimodal, agent]
links:
  - https://deepmind.google/
sources: [tech-bridge-multimodal-commerce-agent, tech-bridge-uncertainty-mathematics]
created: 2026-09-04
updated: 2026-09-05
---

# Google DeepMind

Google의 AI 연구·제품 조직. 본 위키에 **Google 계열 조직 페이지로는 처음** 등장한다 — 그동안 Google은 [[gemma-4]](모델)·[[flutter]](프레임워크)처럼 **제품으로만** 스쳐 지나갔고 조직 축이 비어 있었다. 첫 등장은 [[tech-bridge-multimodal-commerce-agent]] ([[nidhi-kaushik-vyas]], 업로드 2026-09-03).

이 위키의 frontier lab 축에서 [[anthropic]]·[[openai]]·[[shanghai-ai-lab]]에 이어 네 번째다.

## 위키에서 알려진 사실

지금까지 확보한 것은 **커머스 에이전트 한 편**에서 나온 것뿐이다. 모델·연구 축은 아직 비어 있다.

- **소비자 대면 커머스 에이전트**를 만들고 있다. 대상은 *"모호한 의도(fuzzy intent)"* 로 들어오는 쇼핑 사용자. → [[fuzzy-intent-discovery]]
- 설계 원칙이 **협업**이다 — 검색 결과를 주는 게 아니라 선호를 **끌어내고** 가능성을 보여준 뒤 추천으로 수렴.
- **평가를 단계마다 붙인다.** working state·협업 전략·elicitation·응답 네 지점에 auto-rater 12종이 걸려 있다. → [[generator-evaluator-pattern]]
- 선호 추출 평가에 **사용자 시뮬레이터**를 쓴다(정답 제약을 심어두고 몇 턴에 찾아내는지 측정).
- **플랫폼 포지션이 명확하다**: 판매자는 자기 카탈로그의 **온톨로지**를 제공하고, **응답 형식은 에이전트가 정한다.**
  > 모든 판매자를 아우르는 **수평적 공통 층(horizontal common layer)** 을 구축하고 싶기 때문입니다. (…) 그건 판매자가 결정할 수 있는 문제가 아닙니다.
- 판매자–에이전트 공통 언어로 **UCP**를 최근 출시했다고 언급된다.
  > ⚠️ **약어의 뜻은 확정하지 않는다.** en-orig 자막은 *"the UCP stuff that we launched recently"* 라고만 말한다. ko 자막이 "Unified Communications Platform"으로 풀어 썼으나 이는 **자막이 만들어낸 확장**이고 문맥(커머스)과 맞지 않는다.
- 에이전트↔에이전트 상거래는 **아직 도달하지 않았다**고 밝힌다. 인터페이스로는 [[model-context-protocol|MCP]]를 예상.
- 사용자 연구에서 얻은 관찰: **upper funnel은 사용자가 직접, lower funnel은 에이전트**.

## 연구 축 (2026-09-05 ingest · [[tech-bridge-uncertainty-mathematics]])

커머스 에이전트에 이어 **연구 조직으로서의 면**이 처음 들어왔다. 출처는 **Google DeepMind 공식 팟캐스트**이고 화자는 [[zoubin-ghahramani|Zoubin Ghahramani]]다.

- **자체 팟캐스트를 운영한다.** 진행자는 "Hannah"(⚠️ 성은 소스에 없다).
- **GenCast** — 기상 예측 모델. **15일 이상** 예측을, *"거대한 슈퍼컴퓨터에서 몇 시간씩 걸리는 작업"* 을 **8분**에. 핵심 장치는 **diffusion model**로 만드는 **예측 앙상블**이고, 새 관측이 오면 앙상블을 갱신한다 — *"이것이 바로 **Bayesian update**의 기본 개념을 이러한 문제에 적용하는 것."* 허리케인 진로 예측이 사례로, *"도시를 대피시킬지, 긴급 구조대에 연락할지"* 가 걸린 결정이다. → [[bayesian-inference]]
- **AlphaFold** — 예측한 단백질 접힘 구조를 **모델의 확신도에 따라 색으로** 칠하고, 분자 위치의 불확실성을 **구름(cloud)** 으로 표현한다.
- **불확실성이 조직의 연구 축 중 하나다.** 두 제품 모두 불확실성을 산출물에 명시적으로 담고, Ghahramani는 이를 *"인공지능에 있어 매우 중요한 통찰"* 이라 부른다 — **불확실성을 넣으면 정확도가 올라간다.**
- AGI 노선에 대해 **조직 내부에 이견이 있다는 것이 드러난다.** Ghahramani는 *"새로운 아키텍처가 필요하다"* 진영이고, *"그 분야에 종사하는 **많은 사람들**"* 이 스케일링만으로 충분하다고 본다고 말한다. → ⚠️ [[sutton-bitter-lesson]]

> 규모·조직 구조·모델 라인업(Gemini 등)에 대한 정보는 이 위키에 **아직 없다.** 별도 소스 ingest 필요.

## References

- [[tech-bridge-multimodal-commerce-agent]] — [[nidhi-kaushik-vyas]], 2026-09-03
- [[tech-bridge-uncertainty-mathematics]] — [[zoubin-ghahramani]], 2026-09-03
- <https://deepmind.google/>
