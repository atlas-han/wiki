---
title: Fuzzy Intent Discovery
type: concept
category: pattern
tags: [agent, intent, elicitation, state, information-gain, consumer]
related: [multimodal-elicitation, adaptive-response-format, context-engineering, generator-evaluator-pattern, verifiable-goals, outcome-engineering, signal-layer, intent-alignment, no-one-shot-design, ai-slop]
first-seen: tech-bridge-multimodal-commerce-agent
sources: [tech-bridge-multimodal-commerce-agent, tech-bridge-altman-frontier-rl-pause, tech-bridge-taste-labs-measuring-slop, tech-bridge-impeccable-design-steering]
created: 2026-09-04
updated: 2026-09-12
---

# Fuzzy Intent Discovery

사용자가 **자기가 원하는 것을 말로 표현하지 못한 채** 들어온다고 전제하고, 에이전트가 ① 그 격차를 진단하고 ② **구조화된 working state**로 아는 것을 적어두고 ③ **다음에 물을 질문 하나**를 고르는 단계. [[nidhi-kaushik-vyas|Nidhi Kaushik Vyas]]가 [[tech-bridge-multimodal-commerce-agent|강연]]에서 제시한 3단계 루프의 첫 단계(discovery).

## articulation gap — 문제의 이름

> 현재 우리가 사용하는 많은 에이전트는 **검색창을 감싸는 역할만 합니다.** 사용자가 명확한 의도를 가지고 있고, 적절한 키워드를 알고 있으며, 무엇을 찾고 있는지 이미 알고 있다고 가정합니다.

> 실제로 사용자가 방문할 때는 (…) **쇼핑을 하고 싶다는 막연한 느낌이나 예감(vibe)만 가지고 있는 경우가 대부분입니다.**

en-orig의 용어가 **articulation gap(표현력 격차)** 이다. 여기서 나오는 처방이 *"높은 실행력(high agency execution) · 적극적 이끌어내기(proactive elicitation) · 충분한 안내(handholding)"* 세 가지다.

이 위키가 그동안 다룬 에이전트 설계와 **전제가 반대**라는 점이 중요하다. [[verifiable-goals]]·[[outcome-engineering]]·[[spec-driven-development]]는 전부 *"목표를 검증 가능한 형태로 명확히 써라"* 를 요구한다. 그 전제는 **사용자가 엔지니어**라서 명세를 쓸 수 있다는 것이다. 소비자 대면에서는 그 전제가 깨진다 — **명세를 쓰게 하는 것이 아니라 명세를 함께 만들어내는 것**이 에이전트의 일이 된다.

## Working state — 대화 로그가 아니라 상태

discovery의 산출물은 텍스트 히스토리가 아니라 구조화된 상태다.

| 구성요소 | 내용 | 출처 |
|---|---|---|
| session history | 이전 대화 | 세션 |
| user context | 개인 맥락 | 프로필·과거 |
| **hard constraint** | 쿼리에서 그대로 뽑히는 확정 조건 (예산, 치수) | 텍스트 |
| **soft constraint** | 말로 표현 못 한 선호 | **참조 이미지 등 멀티모달 입력** |
| **confidence score** | soft constraint 추출에 대한 자기 확신도 | 에이전트 자체 평가 |
| **real-time variable** | 재고처럼 조회 시점에 갱신돼야 하는 값 | 외부 시스템 |

### soft constraint — 이미지에서 뽑는다

> 사용자는 자신이 원하는 것을 정확하게 설명하지 못할 수 있으며, (…) 참고 이미지를 제공하여 **"이게 제게 더 와닿는 디자인입니다"** 라고 전달하려고 할 수 있습니다. (…) 에이전트가 **참조 이미지에서 두드러진 신호(salient signal)를 추출하고** (…) **정신적 모델**을 개발하기 시작합니다.

### confidence를 상태에 함께 저장한다

> 제공된 멀티모달 입력에서 이러한 정보를 추출하는 데 **얼마나 확신하는지를 나타내는 신뢰도 점수**를 산출합니다.

이 한 칸이 설계 전체를 지탱한다. 확신도가 상태에 있으면 **"신뢰도를 올리는 것" 자체가 질문의 목표**가 될 수 있고([[multimodal-elicitation]]의 micro signal이 갱신하는 대상이 바로 이것), 채점기가 **보정(calibration)** 을 잴 수 있다.

### hard / soft / real-time의 분리가 왜 필요한가

셋의 **갱신 주기와 신뢰 성격이 다르기 때문**이다. hard는 확정이고, soft는 확률적이라 대화 중 갱신되며, real-time은 **에이전트가 믿으면 안 되고 매번 다시 조회해야 한다**.

> 재고처럼 실시간으로 업데이트해야 하는 변수일 수 있습니다. 왜냐하면 사용자에게 제공하는 정보가 **오래된 정보라면 아무 의미가 없기 때문**입니다.

[[context-engineering]] 관점에서 이것은 **컨텍스트를 통짜 텍스트가 아니라 신뢰 등급별로 슬롯을 나눠 관리하는 것**이다. [[agent-distributed-systems]]가 *"에이전트 메모리는 캐시다"* 라고 한 것과 같은 문제를 상태 스키마 층위에서 다룬다.

## Intent gap — 모르는 것 중 하나만 고른다

아는 것을 정리한 다음 *더 알아야 할 것*을 찾는다. 이것을 **intent gap(의도 격차) 발견**이라 부른다.

핵심은 욕심내지 않는 것이다.

> 에이전트는 **사전에 모든 미지 변수를 찾아낼 필요가 없습니다.**

> 가능한 모든 움직임을 비교한 다음, 그 시점에서 **최대의 정보 이득(information gain)** 을 얻을 수 있도록 우선시해야 할 미지의 변수가 무엇인지 파악합니다.

선택 기준이 "중요해 보이는 것"이 아니라 **"답이 대화의 방향을 바꾸는 것"** 이다.

> 다음에 해야 할 최선의 조치는 **방의 너비**를 파악하는 것입니다. 왜냐하면 추천하는 제품이 **방에 맞지 않으면** 아무 의미가 없기 때문입니다. 이는 **대화의 방향을 의미 있게 바꿀 수 있는 변수**입니다.

즉 information gain을 **엔트로피가 아니라 결과 뒤집힘(outcome flip)** 으로 근사한다. 답이 무엇이든 추천이 같다면 물을 가치가 없다.

## 채점기

이 단계에도 auto-rater가 붙는다 ([[generator-evaluator-pattern]] 참조).

| 대상 | rater | 기준 |
|---|---|---|
| working state | **fact retention** | 맥락에 언급된 사실이 상태에 누락 없이 표현됐는가 |
| working state | **confidence calibration** | 신뢰도가 정해진 오차 범위 안인가 |
| working state | **counterfactual sensitivity** | 쿼리를 뒤집으면 제약도 바뀌고 **무관한 것은 그대로인가** |
| 협업 전략 | **blocker 식별** | 의미 있는 답 이전에 풀려야 할 장애물을 전부 찾았는가 |
| 협업 전략 | **over-asking** | 같은 질문을 반복하지 않는가 |
| 협업 전략 | **question utility** | 그 질문이 실제로 선호를 이끌어내는가 |

counterfactual sensitivity를 **양방향**으로 재는 것이 정교한 지점이다.

> 쿼리를 **뒤집어서** (…) 제약 조건도 함께 변경되도록 하고, **관련성이 없는 제약 조건은 그대로 유지**되도록 합니다. **양방향으로 민감도를 측정**하고 싶습니다.

한쪽만 재면 "아무 입력에나 반응하는" 과민한 추출기가 통과해버린다. 두 번째 방향이 **가짜 상관을 잡아내는 장치**다.

## 적용 범위

발표자 본인이 커머스 밖으로 넓힌다.

> 프레임워크는 쇼핑이나 상거래에 기반을 두고 있습니다. (…) 하지만 이러한 패턴은 **금융, 교육 등 다른 소비자 분야에도 충분히 적용될 수 있습니다.**

> ⚠️ 한 강연에서 제시된 **사내 프레임워크**이고, 효과에 대한 수치·벤치마크는 제시되지 않았다.

## 공급자 측 진술 — 의도 이해가 병목 (2026-09-06 · [[tech-bridge-altman-frontier-rl-pause]])

이 페이지가 소비자 대면 에이전트의 설계 문제로 다룬 **articulation gap**을, [[sam-altman|Sam Altman]]은 모델 공급자의 **현재 병목**으로 말한다.

> 사람들이 **1년 전처럼 모델의 지능에 의해 제한받는다고 느끼지는 않지만**, **모델이 사용자의 의도를 이해하고 안정적으로 실행하는 능력에 의해 점점 더 제한받고 있다**고 생각합니다.

그리고 그것을 **정렬**의 정의로 삼는다 — *"우리가 정렬에 대해 이야기할 때, 의도를 따르는 것에 대해 이야기하잖아요. 사용자의 의도요."* → [[intent-alignment]]

이 페이지의 처방(working state · information gain 질문 하나)이 *에이전트가 의도를 끌어내는 절차*라면, Altman의 진술은 *모델이 그 절차 없이도 의도를 읽어야 한다*는 요구다. 같은 문제의 두 층 — 하네스 층과 모델 층 — 이고, [[harness-pruning]]대로라면 전자는 후자가 좋아질수록 얇아진다. ⚠️ 그가 근거로 드는 것은 기업 고객의 체감뿐이며 측정치는 없다.

## 디자인에서의 articulation gap (2026-09-12)

2026-09-11 업로드 두 편이 이 개념의 진단을 **디자인**에서 독립적으로 반복한다.

- [[tech-bridge-taste-labs-measuring-slop]] — [[ai-slop|슬롭]]의 세 번째 특징 **낮은 의도(low intent)**: *"많은 사람이 아주 빠르게 프롬프트하며 그냥 원샷하고 싶어 하는 것도 있겠지만, 우리가 만드는 시스템에 **의도 해석(intent interpretation)** 조각이 빠져 있다. 사용자가 자기가 가진 의도를 더 잘 이해하도록 어떻게 도울 것인가."* 이 페이지의 *proactive elicitation* 과 같은 자리.
- [[tech-bridge-impeccable-design-steering]] — [[paul-bakaus]]의 네 질문: **감정적 영역은? 절대 이래선 안 되는 것은? 레퍼런스는? 대상은?** *"디자인 디렉터가 고개만 끄덕이고 걸어가 버리면 말이 안 된다."* 디자인 의뢰의 discovery 단계이고, 두 번째 질문은 **부정형 제약**(hard constraint의 배제형)이다. → [[no-one-shot-design]]

둘 다 결론이 같다 — 원샷은 *"아무도 아무것도 결정하지 않은"* 산출물을 낳는다. 이 개념이 소비자 상거래에서 세운 *명세를 함께 만들어내는 것이 에이전트의 일* 이 디자인에도 그대로 걸린다.

## References

- [[tech-bridge-multimodal-commerce-agent]] — [[nidhi-kaushik-vyas]] / [[google-deepmind]]
- 다음 단계: [[multimodal-elicitation]] → [[adaptive-response-format]]
- 관련: [[context-engineering]] · [[generator-evaluator-pattern]] · [[verifiable-goals]] · [[outcome-engineering]]
- [[tech-bridge-altman-frontier-rl-pause]] — 의도 이해가 병목 (Sam Altman, 2026-09-06)
