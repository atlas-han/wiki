---
title: 취향과 판단 (Taste vs Judgment)
type: concept
category: theory
tags: [taste, judgment, design, differentiation, learning, scarcity, ai-slop]
aliases: [taste, judgment, 취향, 판단력, amplified craft]
related: [signal-layer, ai-slop, decision-quality, cognitive-offloading, multimodal-elicitation, slop-probes, no-one-shot-design, sutton-bitter-lesson, dhh, lena-hall]
first-seen: tech-bridge-taste-labs-measuring-slop
sources: [tech-bridge-dhh-agent-productivity, tech-bridge-signal-layer, tech-bridge-multimodal-commerce-agent, tech-bridge-taste-labs-measuring-slop, tech-bridge-impeccable-design-steering, tech-bridge-lauren-tan-trusting-agents, tech-bridge-one-designer-plus-ai, tech-bridge-ai-engineer-three-tier-skill-stack]
created: 2026-09-12
updated: 2026-09-16
---

# 취향과 판단

**생성이 무료가 된 세계에서 사람에게 남는 것이 "취향(taste)"인가 "판단(judgment)"인가, 그리고 취향은 기계가 배울 수 있는가.** 이 위키가 [[dhh]]·[[lena-hall|Lena Hall]]에서 나란히 두기만 했던 논쟁이 2026-09-11 업로드 두 편([[tech-bridge-taste-labs-measuring-slop]]·[[tech-bridge-impeccable-design-steering]])으로 **네 입장**이 되어 페이지를 얻는다. 위키는 어느 입장도 채택하지 않는다.

## 네 입장

| 화자 | 소스 | 취향은 | 남는 것 | 처방 |
|---|---|---|---|---|
| **[[dhh]]** | [[tech-bridge-dhh-agent-productivity]] (08-30) | **병목** — 무한 프로그래머를 가진 조직도 매력적인 소프트웨어를 못 만든다 | 아이디어·비전·취향 (희소한 인간 능력) | 조직 밖에서 자기 5%를 다시 쓴다 |
| **[[lena-hall\|Lena Hall]]** | [[tech-bridge-signal-layer]] (09-01) | **피드백을 통한 선호도 — 학습 가능.** *"넓은 취향은 진정한 차별화 요소가 아니다"* | **판단** — 아직 일어나지 않은 일 · 모델이 관찰 못 한 관계 | 신호를 정의하고 왜곡 없이 전달 |
| **[[thais-castello-branco]]** | [[tech-bridge-taste-labs-measuring-slop]] (09-11) | *"취향이라는 말은 쓰고 싶지도 않다"* — 평생 걸리므로 **모두가 갖는 건 비현실적**. 단, 팔레트·대비·정렬처럼 **분해하면 거의 결정론적인 조각**은 모델에 훈련 가능 | **판단** — 분별하고 분해하는 능력. 사람의 판단 + 도구 | 슬롭을 측정하고 **바닥의 기준**부터 올린다 |
| **[[paul-bakaus]]** | [[tech-bridge-impeccable-design-steering]] (09-11) | **증폭될 수 있지만(amplified craft) 실험실에서 배양될 수 없다.** 맥락적·문화적·**희소** — 모두가 복제하면 취향이 아니다 | 사람의 **조향**(결정) | 도구는 취향을 날카롭게 할 뿐, *"내 도구로 취향을 풀려는 게 아니다"* |

부수 입장 — [[tech-bridge-multimodal-commerce-agent]]([[google-deepmind]]): 취향은 **본인이 정답을 안다**(말로 못 할 뿐)이므로 시뮬레이터를 세워 *발견 과정* 을 채점할 수 있다. → [[multimodal-elicitation]]

## 인용

> 생산 비용이 0으로 가면서, **비싸지고 그 어느 때보다 중요해지는 것은 판단(judgment)** 입니다. 여기서 **"취향(taste)"이라는 말은 쓰고 싶지도 않아요. 판단입니다.** 무엇이 옳은지 **분별하는** 능력, 문제를 **분해해서** 실제로 이해하고 해법을 만드는 능력. — Thais (08:41~08:59)

> **취향은 증폭될 수 있다**고 생각해요. 저는 이걸 **amplified craft**라고 부릅니다. (…) 하지만 **실험실에서 배양(lab grown)될 수 있다고는 정말로 생각하지 않습니다.** 취향은 정의상 **맥락적**이고, **문화적**이고, **희소**해요. 모두가 같은 것을 복제하기 시작하면 아주 흐려지고 우리는 더 이상 그것을 취향으로 생각하지 않습니다. — Paul (14:41~15:10) *(⚠️ 14:38에 "증폭될 수 없다"고 했다가 곧바로 정정)*

> **취향(taste)은 사실 피드백을 통한 선호도**일 뿐이며, 피드백을 통한 선호도가 바로 이러한 시스템이 **학습할 수 있는 것**입니다. — Hall

## 위키의 정리 — 같은 말, 다른 범위

네 입장이 다투는 것은 취향의 **가치**가 아니라 *taste* 라는 말이 가리키는 **범위**다.

| 범위 | 학습 가능? | 누가 그렇게 보나 |
|---|---|---|
| **분해 가능한 조각** — 팔레트·대비·정렬 | 가능 (거의 결정론적) | Thais |
| **넓은 선호** — 무엇이 좋아 보이는가 | 가능 (피드백 데이터) | Hall · DeepMind(시뮬레이터) |
| **미학** — 전문가가 갈리는 것 | 데이터에 의존, 확정 불가 | Thais |
| **아직 일어나지 않은 일 · 관찰 못 한 관계** | 불가 (데이터 없음) | Hall |
| **희소성 그 자체** — 배워서 모두가 가지면 사라짐 | 정의상 불가 | Paul |

Paul의 것이 가장 구조적이다 — 학습 가능 여부의 문제가 아니라 **취향의 정의에 희소성이 들어 있어서**, [[sutton-bitter-lesson|스케일]]이 그것을 배우는 순간 그것은 더 이상 취향이 아니게 된다. Hall의 *"넓은 취향은 차별화 요소가 아니다"* 와 결론이 같고 이유가 반대다(Hall: 배울 수 있어서 / Paul: 배우면 사라져서).

그리고 **처방에서 넷이 수렴하는 지점**이 있다 — 추론 시점에 **사람의 판단·결정이 남는다.** DHH의 *취향*, Hall의 *판단*, Thais의 *판단*, Paul의 *조향* 은 이름이 다르지만 자리가 같다. → [[decision-quality]]([[ibm]])가 코드에서 같은 말을 했다.

## 두 09-11 소스의 반대 방향

같은 날 올라온 두 편은 **하려는 일이 정반대**다 — Taste Labs는 *안목을 모델에 훈련시키는* 회사이고, Paul은 *"취향은 배양될 수 없다"* 며 *"다음 발표자들 중 일부에게는 어색하겠지만"* 이라고 예고한다(같은 행사라면 그 다음 발표자가 Thais일 수 있으나 **확정 근거 없음**). 그런데 둘 다 **바닥**을 겨냥한다 — Thais: *"정점의 취향을 논할 자격조차 없다, 기준이 바닥에 있다"*, Paul: *"마지막 5~20%는 사람"*. 즉 Thais가 훈련하려는 것은 Paul이 *취향* 이라 부르는 희소한 부분이 아니라 **바닥의 기준**이고, 그렇다면 둘은 충돌하지 않을 수 있다. ⚠️ 위키의 정리.

## ⚠️ 미해결

- 넷 다 **측정치가 없다.** DHH·Hall은 관찰, Thais·Paul은 당사자.
- [[cognitive-offloading]]([[andrew-ng]])의 질문 — *판단을 기를 동기가 사라지면* — 은 어느 소스도 다루지 않는다. Thais의 *"평균적인 사람도 훌륭한 것을 만들게"* 는 판단을 **대신하는** 것인지 **기르는** 것인지 모호하다.

## 다섯 번째 입장 — 판단은 "에이전트를 신뢰할지 정하는 일" (2026-09-12 Lauren Tan 편)

[[tech-bridge-lauren-tan-trusting-agents]]가 이 페이지의 네 입장(DHH · Hall · Thais · Paul)에 **다섯 번째**를 더한다. [[lauren-tan]]에게 취향과 판단은 **미학이 아니라 위임 결정**에 쓰인다.

> [신뢰를 쌓는 데는] **취향과 판단이 많이 듭니다.**

두 자리에서 구체화된다:

- **곡선을 오르는 판정** — 어디까지 자동화할지는 *"여러분 개인의 에이전트 신뢰 수준"* 이고 **지름길이 없다.** → [[agent-trust-curve]]
- **스킬을 유지하는 관찰** — *"스킬을 유지하는 건 꽤 어렵습니다. **취향과 관찰이 많이 필요**합니다. **뒷좌석 운전자 노릇을 아주 잘해야** 해요."* → [[skill-evals]] · [[agent-manager-analogy]]

그리고 **취향이 닿지 않는 곳의 경계**를 긋는다 — 검증은 *올바름* 까지이고 *좋음* 은 사람이 남는다(→ [[agent-verification-skill]]). 이는 09-12 두 편이 도달한 *"추론 시점에 사람이 남는다"* 와 같은 자리다.


## 2026-09-15 — 다섯 번째 입장: 취향을 논하지 않고 굳혀 둔다

[[tech-bridge-one-designer-plus-ai]]의 [[vincent-wendy|Vincent Wendy]]는 **취향이 무엇인지 묻지 않는다.** 대신 이미 가진 취향을 **디자인 시스템으로 못 박아** 모델과 다른 팀이 그 안에서만 움직이게 한다([[design-system-as-agent-context]]).

| 입장 | 취향을 어떻게 다루나 |
|---|---|
| [[dhh]] | 취향은 사람의 것이고 위임되지 않는다 |
| [[lena-hall]] | 판단이 남는 층이 따로 있다 |
| [[thais-castello-branco]] | *"취향이 아니라 판단"* — 측정 가능한 것으로 바꾼다 |
| [[paul-bakaus]] | 조향의 고도를 사람이 정한다 |
| **[[vincent-wendy]]** | **자산으로 굳혀 두고 실행을 위임한다** |

다섯 번째가 앞의 넷과 다른 점은 **논쟁을 피한다**는 것이다 — 취향의 소재를 따지는 대신 **취향이 이미 박혀 있는 산출물(디자인 시스템)을 컨텍스트로 넘긴다.** [[self-serve-asset-generation]]에서 위임되는 것이 실행뿐이고 결정은 디자이너에게 남는 구조가 이 입장의 귀결이다.

## References

- [[tech-bridge-dhh-agent-productivity]] · [[tech-bridge-signal-layer]] · [[tech-bridge-multimodal-commerce-agent]]
- [[tech-bridge-taste-labs-measuring-slop]] (first-seen) · [[tech-bridge-impeccable-design-steering]]
- 관련: [[signal-layer]] · [[ai-slop]] · [[decision-quality]] · [[multimodal-elicitation]] · [[dhh]] · [[lena-hall]]

## 2026-09-16 — 진입 전의 사람에게: "어려운 건 코드가 아니라 판단, 만들어 보며 배운다"

[[tech-bridge-ai-engineer-three-tier-skill-stack]]([[cedric-clyburn|Cedric Clyburn]], [[ibm|IBM Technology]])이 같은 말을 **아직 AI 엔지니어가 아닌 사람**에게 한다 — 이 페이지의 입장들이 전부 *이미 일하는 사람* 의 것이었던 것과 다른 자리다.

> **AI 코딩 도구 덕분에 코드 생성이 쉬워졌으므로, 이제 어려운 부분은 코드 자체가 아니라 판단력입니다.** (…) **수업에서 항상 배울 수 있는 건 아니지만, 직접 만들어 보면서 확실히 배울 수 있습니다.** (00:36~01:07)

*판단* 의 내용은 **구조화·무엇을 만들지·왜 이 접근인지**이고, 처방은 **건설**이다 — 신호 정의(Hall)·슬롭 측정(Castello Branco)·조향(Bakaus)과 달리 **학습 경로**를 말한다. 그리고 그 판단이 서기 위한 최소 조건을 같은 소스가 정한다 — [[read-fluency-for-agent-output|에이전트가 쓴 것을 읽을 만큼]]. ⚠️ 취향(taste)이라는 말은 이 소스에 없다. → [[ai-engineer-vs-ml-researcher]]
