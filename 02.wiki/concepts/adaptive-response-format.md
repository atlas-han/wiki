---
title: Adaptive Response Format
type: concept
category: pattern
tags: [agent, response, ux, evaluation, presentation, consumer]
related: [fuzzy-intent-discovery, multimodal-elicitation, generator-evaluator-pattern, agentic-sites, token-roles]
first-seen: tech-bridge-multimodal-commerce-agent
sources: [tech-bridge-multimodal-commerce-agent]
created: 2026-09-04
updated: 2026-09-04
---

# Adaptive Response Format

**응답의 형식을 고르는 것 자체를 모델의 일**로 보는 설계. 같은 내용이라도 의도에 따라 요약·비교표·무드보드 중 무엇으로 내놓을지가 달라지고, 그 선택이 채점 대상이 된다. [[nidhi-kaushik-vyas|Nidhi Kaushik Vyas]]의 3단계 루프 중 마지막 단계 ([[tech-bridge-multimodal-commerce-agent]]).

## 진단: 텍스트 덩어리로 끝난다

> 일반적으로 많은 시스템이 이 부분에서 실패하는데, **텍스트 위주의 응답만 제공하기 때문입니다.** 에이전트가 해야 할 일은 오히려 **사용자가 염두에 둔 질문에 맞춰 대응하는 것**입니다. 그럼 글머리 기호 목록 같은 걸 사용해야 할까요? 비교표를 사용해야 할까요? 시각적인 보드를 사용해야 할까요?

## 매핑

| 사용자가 원하는 것 | 형식 |
|---|---|
| 특정 제품의 **정책·리뷰 정보** | 요약 / 글머리 기호 목록 |
| **두 제품 비교** | **트레이드오프 비교표** — 사용자가 중요하게 여기는 축으로 |
| **스타일 영감·아이디어** | **시각적 참고 자료 · 제품 사진 · 무드보드** |

비교표에서 *축을 사용자가 신경 쓰는 것으로* 잡는다는 단서가 중요하다. 축은 [[fuzzy-intent-discovery]]의 working state에서 나온다 — 대화 중 파악된 메타데이터가 그대로 열이 된다.

## 형식은 지능의 일부다

강연의 세 번째 교훈.

> 사용자가 필요한 정보를 쉽게 찾을 수 있도록 **프레젠테이션 형식을 최적화**하는 데 집중하십시오. **모델 응답 구조를 갖는 방식 또한 지능의 중요한 부분입니다.**

이 문장이 이 개념의 전부다. 형식은 렌더링 계층의 후처리가 아니라 **모델이 내리는 판단**이고, 따라서 **틀릴 수 있고 채점될 수 있다.**

## 채점기

| rater | 기준 |
|---|---|
| **format accuracy** | 형식이 쿼리에 최적인가. *"사용자가 찾고 있는 정보가 **답변 속에 묻혀 있지 않고** 쉽게 찾을 수 있어야 합니다."* |
| **data fidelity** | *"모델이 잘못된 정보를 가져오지 않고"* 정확히 포착하는가 (환각 방지) |
| **user actionability** | 사용자가 **확신을 갖고 다음 행동으로 넘어가는가** |

**user actionability**가 이 세트에서 가장 특이하다. 응답의 품질을 텍스트 자체가 아니라 **그 뒤에 사용자가 한 행동**으로 정의한다. 커머스에서는 그 행동이 구매다.

> 응답 형식이 사용자가 매우 확신을 갖고 **다음 행동, 즉 제품 구매를 결정하도록 하는 방식**입니다.

이는 [[outcome-engineering]]의 소비자 대면판이다 — *how*가 아니라 결과로 채점하되, 결과가 테스트 통과가 아니라 **전환**이다.

> ⚠️ 여기에 이해충돌이 잠복해 있다. "사용자가 구매로 넘어갔는가"는 **판매자의 목표이기도 하다.** 소스는 이 지표가 사용자 이익과 어긋날 수 있는 가능성을 다루지 않는다. [[signal-layer]]가 말한 *"틀렸을 때의 비용은 음수"* 와 나란히 읽을 것.

## 형식 결정권은 플랫폼이 갖는다

Q&A에서 나온 정책 선언이고, 이 개념의 조직적 함의다.

> 지금 우리가 집중하고 있는 건 이 모든 정보가 **에이전트에게 전달되고 에이전트가 결정을 내리도록** 하는 것입니다. 왜냐하면 **모든 판매자를 아우르는 수평적 공통 층**을 구축하고 싶기 때문입니다. (…) **응답 형식은 에이전트의 지능과 매우 밀접한 관련이 있습니다. 그건 판매자가 결정할 수 있는 문제가 아닙니다.**

판매자가 주는 것은 [[multimodal-elicitation]]의 **온톨로지(무엇을 파는지)** 이고, **어떻게 보여줄지는 주지 않는다.** 웹에서 판매자가 자기 페이지 레이아웃을 통제하던 것과의 명확한 단절이다.

[[agentic-sites]]와 비교하면 대칭이 보인다 — 그쪽은 **사이트 소유자가** 방문자 의도에 맞춰 자기 블록을 재조립하고, 이쪽은 **플랫폼 에이전트가** 여러 판매자 위에서 형식을 정한다. 재조립의 주체가 다르다.

## References

- [[tech-bridge-multimodal-commerce-agent]] — [[nidhi-kaushik-vyas]] / [[google-deepmind]]
- 앞 단계: [[fuzzy-intent-discovery]] → [[multimodal-elicitation]]
- 관련: [[generator-evaluator-pattern]] · [[outcome-engineering]] · [[agentic-sites]] · [[signal-layer]]
