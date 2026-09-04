---
title: "Tech Bridge — 차세대 커머스를 위한 멀티모달 협업 에이전트 설계법"
type: source
tags: [agent, multimodal, commerce, elicitation, evaluation, auto-rater, ontology, video]
source-url: https://www.youtube.com/watch?v=UoU8_gkaXI4
source-type: video
author: Tech Bridge (한영자막 재배포) · 발표자 Nidhi Kaushik Vyas (Google DeepMind)
date-published: 2026-09-03
ingested: 2026-09-04
created: 2026-09-04
updated: 2026-09-04
---

# Tech Bridge — 차세대 커머스를 위한 멀티모달 협업 에이전트 설계법

[[tech-bridge|Tech Bridge]]가 한영자막을 입힌 20:37 컨퍼런스 강연. 발표자는 [[nidhi-kaushik-vyas|Nidhi Kaushik Vyas]], 소속은 [[google-deepmind|Google DeepMind]]. 한 줄 테제:

> 사용자는 **키워드가 아니라 분위기(vibe)** 를 갖고 온다. 에이전트의 일은 검색하는 게 아니라 **그 격차를 협업으로 메우는 것**이다.

본문은 ko 자막을 채널 공식 12개 챕터 순서로 재구성했고 용어·인용은 en-orig로 교차 확인했다. → [[2026-09-03_차세대 커머스를 위한 멀티모달 협업 에이전트 설계법|raw 캡처]]

이 소스는 이 위키에 **두 가지 첫 사례**를 들여온다. 첫째, [[google-deepmind|Google DeepMind]]가 조직 엔티티로 처음 등장한다 — 지금까지 [[tech-bridge]] 소스 16편은 [[anthropic]]·[[openai]]·[[cursor]]·[[adobe]]·[[tiktok]]·[[ironclad]] 축이었고 Google 축은 [[gemma-4]]·[[flutter]] 같은 제품으로만 스쳤다. 둘째, **소비자 대면(consumer-facing) 에이전트**가 처음이다. 기존 소스는 전부 개발자·조직 내부용 에이전트(코딩·리뷰·워크플로)였고, "상대가 엔지니어가 아니라 **자기가 뭘 원하는지 모르는 일반 사용자**"인 설계 문제는 비어 있었다.

> ⚠️ **촬영 시점 미확정.** [[tech-bridge]]에 아카이브 재배포 전례가 있어([[tech-bridge-karpathy-transformers-stanford]]) 내부 시점 단서를 확인했다. **과거 강연이라는 증거는 없지만 확정할 근거도 없다** — 유일한 앵커는 Q&A의 *"최근에 출시한 UCP"* 뿐이고, 행사명은 소스 어디에도 없다. 업로드 날짜를 발화 날짜로 가정하지 않는다.

## 문제: articulation gap

강연의 출발점은 진단이다.

> 현재 우리가 사용하는 많은 에이전트는 **검색창을 감싸는 역할만 합니다.** 사용자가 명확한 의도를 가지고 있고, 적절한 키워드를 알고 있으며, 무엇을 찾고 있는지 이미 알고 있다고 가정합니다.

> 하지만 실제로 사용자가 방문할 때는 (…) **쇼핑을 하고 싶다는 막연한 느낌이나 예감(vibe)만 가지고 있는 경우가 대부분입니다.**

en-orig의 이름이 **articulation gap**이다. → [[fuzzy-intent-discovery]]

범위에 대한 발표자 본인의 단서: 프레임워크는 커머스에 grounded 돼 있지만 *"금융, 교육 등 다른 소비자 분야에도 충분히 적용될 수 있습니다."*

## 3단계 루프

| 단계 | 하는 일 | 위키 페이지 |
|---|---|---|
| **Discovery(탐색)** | 맥락을 모아 **working state**를 만들고, 다음에 물을 질문 **하나**를 고른다 | [[fuzzy-intent-discovery]] |
| **Research(조사)** | 선호를 **어떻게** 이끌어낼지 정하고, 백그라운드에서 비교·요약을 대신 한다 | [[multimodal-elicitation]] |
| **Response(응답)** | 의도에 맞게 **응답 형식 자체**를 고른다 | [[adaptive-response-format]] |

세 단계 **각각에** auto-rater가 붙는다는 것이 이 강연의 구조적 특징이고, 이 위키에서 가장 값진 부분이다(아래 "채점기" 절).

## Working state — soft constraint와 confidence score

discovery의 산출물은 대화 로그가 아니라 **구조화된 상태**다. 거실 리모델링 예시에서: session history, user context, **hard constraint**(예산), **soft constraint**(참조 이미지에서 추출), confidence score, real-time variables(재고).

soft constraint가 이 설계의 중심이다.

> 사용자는 자신이 원하는 것을 정확하게 설명하지 못할 수 있으며, (…) 참고 이미지를 제공하여 에이전트에게 **"이게 제게 더 와닿는 디자인입니다"** 라고 전달하려고 할 수 있습니다. (…) 에이전트가 **참조 이미지에서 두드러진 신호를 추출하고** (…) **정신적 모델**을 개발하기 시작합니다.

그리고 **자기 확신도를 상태에 함께 저장한다** — *"제공된 멀티모달 입력에서 이러한 정보를 추출하는 데 얼마나 확신하는지를 나타내는 **신뢰도 점수**"*. 이것이 뒤에서 "신뢰도를 올리는 것" 자체를 **질문의 목표**로 만들 수 있게 하는 장치다.

실시간 변수는 별도로 취급한다 — 재고처럼 *"오래된 정보라면 아무 의미가 없기 때문"*.

## 다음 질문 하나를 고르는 법 — information gain

이 강연에서 가장 이식성 높은 아이디어다.

> 에이전트는 **사전에 모든 미지 변수를 찾아낼 필요가 없습니다.**

> 가능한 모든 움직임을 비교한 다음, 그 시점에서 **최대의 정보 이득(information gain)** 을 얻을 수 있도록 우선시해야 할 미지의 변수가 무엇인지 파악합니다.

판정 기준은 "무엇을 모르는가"가 아니라 **"무엇이 대화의 방향을 바꾸는가"** 다.

> 어쩌면 다음에 해야 할 최선의 조치는 **방의 너비**를 파악하는 것입니다. 왜냐하면 추천하는 제품이 **방에 맞지 않으면** 아무 의미가 없기 때문입니다. 이는 **대화의 방향을 의미 있게 바꿀 수 있는 변수**입니다.

## 보여주고 묻기 — visual board와 micro signal

research 단계는 먼저 **bridge**를 놓는다 — 제약 조건을 판매자 **온톨로지/제품 카탈로그**에 *"임시적으로"*, *"거의 실시간으로"* 매핑한다. 검색을 시작하려면 제약을 지식 베이스 어휘로 번역해야 하기 때문이다.

그다음 형식을 고른다.

> 이것이 일종의 **주관적인 제약 조건**이기 때문에 텍스트를 통한 정보 추출이 최선의 방법이 아닐 수도 있다고 판단한 것입니다. 그래서 (…) **시각적인 선호도 보드**를 사용하는 것입니다.

보드는 장식이 아니라 **측정 장치**다.

> **마우스 커서가 특정 방향으로 이동하거나 클릭이 발생하는 등의 미세한 신호를 감지**하여 (…) **신뢰도 모델을 업데이트**할 수 있습니다.

즉 사용자가 *말한 것*이 아니라 *반응한 것*으로 soft constraint의 confidence를 올린다. → [[multimodal-elicitation]]

## 형식은 지능의 일부다

> 일반적으로 많은 시스템이 이 부분에서 실패하는데, **텍스트 위주의 응답만 제공하기 때문입니다.**

| 사용자가 원하는 것 | 형식 |
|---|---|
| 정책·리뷰 정보 | 요약 / 글머리 기호 |
| 두 제품 비교 | **트레이드오프 비교표** (사용자가 중요하게 여기는 축으로) |
| 스타일 영감 | **시각적 참고 자료 · 무드보드** |

> **모델 응답 구조를 갖는 방식 또한 지능의 중요한 부분입니다.**

→ [[adaptive-response-format]]

## 채점기 — 단계마다 하나씩

이 소스가 이 위키에 주는 가장 큰 기여다. [[generator-evaluator-pattern]]이 지금까지 **산출물 하나**를 채점하는 패턴이었다면, 여기서는 **루프의 모든 단계**에 채점기가 붙는다.

| 단계 | auto-rater | 무엇을 보는가 |
|---|---|---|
| working state | **fact retention** | 맥락의 사실이 누락 없이 상태에 표현됐는가 |
| working state | **confidence calibration** | 신뢰도가 오차 범위 안인가 |
| working state | **counterfactual sensitivity** | 쿼리를 뒤집으면 제약도 바뀌고 **무관한 것은 그대로인가** |
| 협업 전략 | **blocker 식별** | 풀어야 할 장애물을 전부 찾았는가 |
| 협업 전략 | **over-asking** | 같은 질문을 반복하지 않는가 |
| 협업 전략 | **question utility** | 그 질문이 실제로 선호를 이끌어내는가 |
| elicitation | **hidden preference 효율** | **사용자 시뮬레이터**로 측정 |
| elicitation | **turn efficiency** | 몇 턴 만에 숨은 선호를 밝혔는가 |
| elicitation | **format selection accuracy** | 질문을 맞는 형식으로 했는가 |
| 응답 | **format accuracy** | 정보가 *"답변 속에 묻혀 있지 않은가"* |
| 응답 | **data fidelity** | 환각 없이 정확히 포착했는가 |
| 응답 | **user actionability** | 사용자가 **다음 행동으로 넘어가는가** |

counterfactual sensitivity가 특히 정교하다 — **양방향**으로 잰다.

> 쿼리를 **뒤집어서** (…) 제약 조건도 함께 변경되도록 하고, **관련성이 없는 제약 조건은 그대로 유지**되도록 합니다. **양방향으로 민감도를 측정**하고 싶습니다.

그리고 채점기 자체의 성장에 대한 단서:

> 이런 auto-rater를 개발하는 것은 거의 **진화하는 시스템과 같습니다.** 처음에는 **아주 간단하게 시작**하지만 (…) **채점기도 시스템과 함께 점진적으로 성장**해야 합니다.

## Q&A에서 건진 것

**판매자 온톨로지는 판매자가 채운다.** 앞서 나온 bridge가 조직 간 인터페이스가 된다 — *"판매자 측의 지능이 흘러 들어오기를 기대합니다."* 그리고 *"최근에 출시한 **UCP**"* 가 판매자–에이전트 **공통 언어** 역할을 한다고 언급된다.

> ⚠️ **UCP의 뜻은 확정하지 않는다.** en-orig는 약어만 말한다. ko 자막이 "Unified Communications Platform"으로 풀어 썼지만 **원문에 없는 자막의 확장**이고 문맥과 맞지 않는다.

**응답 형식은 판매자가 정하지 못한다.** 플랫폼 전략이 드러나는 대목이다.

> **모든 판매자를 아우르는 수평적 공통 층**을 구축하고 싶기 때문입니다. (…) **응답 형식은 에이전트의 지능과 매우 밀접한 관련이 있습니다. 그건 판매자가 결정할 수 있는 문제가 아닙니다.**

**에이전트 대 에이전트는 아직 아니다.** *"**MCP가 이 둘 사이의 인터페이스 역할**을 확실히 할 거라고 예상합니다. (…) 아직 우리 에이전트가 다른 에이전트와 상호작용하는 단계에는 이르지 못했습니다."* → [[model-context-protocol]]

**퍼널 위치가 사람과 에이전트를 가른다.** 이 소스에서 가장 반직관적인 관찰이다.

> 사용자들은 **선택 과정이나 다양한 가능성을 탐색하는 과정에 더 적극적으로 참여하는 것을 좋아**합니다. 따라서 **여정의 초기 단계** — 발견·영감 — 에서는 자기 에이전트보다 **시스템과 직접 상호작용하는 것을 선호**합니다. 에이전트가 개입하는 시점은 **여정의 하단**, 즉 **가격을 비교하거나 협상**하려는 시점입니다.

즉 위임이 늘어나는 방향이 *"모든 걸 에이전트가 대신한다"* 가 아니라 **재미없는 아래쪽부터**라는 것이다. ⚠️ 근거는 언급된 사용자 연구뿐이고 수치는 제시되지 않았다.

## 이 소스가 남긴 것

**새 개념 3개** — [[fuzzy-intent-discovery]], [[multimodal-elicitation]], [[adaptive-response-format]]. 3단계 루프에 1:1 대응한다.

**새 엔티티 2개** — [[nidhi-kaushik-vyas]], [[google-deepmind]](위키 첫 Google 조직 페이지).

**보강된 기존 페이지** — [[generator-evaluator-pattern]](단계별 채점기 12종 · 채점기의 점진적 성장), [[signal-layer]](채점기 경계선에 대한 **반례성 증거** — 주관적 취향 영역에 채점기를 만든 사례), [[model-context-protocol]](에이전트↔에이전트 인터페이스 기대), [[context-engineering]](working state = 구조화된 컨텍스트), [[tech-bridge]].

**⚠️ 표시한 것** — 촬영 시점 미확정, 행사명 없음, UCP 확장 미확정(ko 자막의 창작), en-orig의 *"wives"*=**vibes** 오인식, ko 자막의 agent→"상담원/부동산 중개인/요원" 일관 오역, 퍼널 관찰의 수치 부재.

## References

- 원본: <https://www.youtube.com/watch?v=UoU8_gkaXI4> (20:37)
- raw: [[2026-09-03_차세대 커머스를 위한 멀티모달 협업 에이전트 설계법]]
- [[nidhi-kaushik-vyas]] · [[google-deepmind]] · [[tech-bridge]]
- 관련: [[fuzzy-intent-discovery]] · [[multimodal-elicitation]] · [[adaptive-response-format]] · [[generator-evaluator-pattern]] · [[signal-layer]]
