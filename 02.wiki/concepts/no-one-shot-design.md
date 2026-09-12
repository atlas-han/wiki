---
title: 디자인은 원샷할 수 없다 (No One-Shot Design)
type: concept
category: pattern
tags: [design, iteration, elicitation, human-in-the-loop, auto-mode, intent]
aliases: [multi-shot design, no auto mode, 원샷 불가, 멀티샷 디자인]
related: [steering-altitude, adjective-verb-steering, fuzzy-intent-discovery, intent-md, decision-quality, ai-slop, generator-evaluator-pattern, privacy-auto-mode, anthropic-claude-code-auto-mode, no-silent-write]
first-seen: tech-bridge-impeccable-design-steering
sources: [tech-bridge-impeccable-design-steering, tech-bridge-taste-labs-measuring-slop]
created: 2026-09-12
updated: 2026-09-12
---

# 디자인은 원샷할 수 없다

**좋은 디자인은 맥락이 풍부해야 하고, 반복되어야 하며, 여러 사람의 의견을 통과해야 한다 — 그래서 "디자인해 줘" 한 번으로 나올 수 없고, 그래서 자동 모드는 만들지 않는다.** [[paul-bakaus]]의 *"오늘 세션의 첫 번째 hot take"*([[tech-bridge-impeccable-design-steering]]).

> **디자인은 원샷할 수 없습니다.** 많은 사람이 원하고, 언젠가 도달할지도 모르죠. 저는 지금은 가능하지 않다고 봅니다. **어쩌면 영원히.** (05:49~05:59)

## 세 가지 이유

> 효과적인 디자인을 만들려면, 무엇을 하려는지, 대상이 누구인지, 무엇을 만들려는지로 **맥락이 풍부하게(context-rich)** 채워진 것이 필요합니다. 그리고 **멀티샷**이어야 해요. 디자인을 **반복**해야 합니다. 1인 기업가가 아니라면 **의견이 다른 사람들**이 있고, **사용자도 의견이 있습니다.** 디자인은 **지저분(messy)** 해요. (06:02~06:32)

| 이유 | 결과 |
|---|---|
| **맥락** — 무엇을·누구에게·왜 | 먼저 물어야 한다 |
| **반복** — 멀티샷 | 한 번의 프롬프트로 끝나지 않는다 |
| **다수의 의견** — 이해관계자·사용자 | 검증이 사람 사이에서 일어난다 |

> 이 과정을 없는 셈 치고 *"에이전트야, 이 문제 풀어 줘"* 라고 하는 것은 유감스럽게도 문제를 풀지 못합니다. (06:32~06:37)

## 먼저 물어야 하는 네 질문

> **감정적 영역(emotional territory)은 무엇인가? 이것은 절대 어떻게 느껴져서는 안 되는가? 레퍼런스는? 대상은?** (07:02~07:13)

> 세계 최고의 디자인 스튜디오에 가서 디자인 디렉터에게 *"제 브랜드 디자인 원해요"* 라고 했는데 디자이너가 고개만 끄덕이고 *"알겠습니다"* 하고 걸어가 버리면 — 말이 안 되잖아요. (07:13~07:30)

이것은 [[fuzzy-intent-discovery]]의 *articulation gap* 처방을 디자인 의뢰에 적용한 것이고, [[intent-md]]([[ai-native-sdlc]])가 *에이전트가 사람을 인터뷰해 요구사항 이전 아티팩트를 만든다* 고 한 것과 같은 형태다. 두 번째 질문(*절대 이래선 안 되는 것*)은 [[signal-layer]]가 *"무엇 때문에 깨어나지 말아야 하는지"* 를 신호로 삼은 것과 같은 **부정형 명세**다.

## 원샷의 결과 — 결정의 부재

> 이런 **2026년 버전의 AI 슬롭** — 빠르게 바이브 코딩된 페이지 — 에서 **아무도 아무것도 결정하지 않았다**는 겁니다. 그냥 원샷한 거예요. (…) **유능해 보일지 몰라도 완전히 비어 있습니다.** (07:38~07:55)

같은 날 [[tech-bridge-taste-labs-measuring-slop|Taste Labs]]의 [[thais-castello-branco]]가 [[ai-slop|슬롭]]의 세 번째 특징으로 든 **낮은 의도** — *"많은 사람이 아주 빠르게 프롬프트하며 그냥 **원샷**하고 싶어 하는 것"*(05:37~05:41) — 와 정확히 같은 진단이다. 두 소스는 서로를 모른다.

## 제품 결정 — auto는 없다

> Impeccable을 **자동으로** 쓰는 방법에 대한 요청을 정말 많이 받았습니다. (…) **그게 요점이 아닙니다.** 요점은 **원하는 결과를 향해 조향할 방법을 주는 것**이에요. **디자인을 원샷하는 도구가 될 일은 결코 없습니다.** 지금 그 이유로 **닫으려는 PR이 하나 서 있습니다.** (13:57~14:28)

> **auto는 없고, 앞으로도 auto는 없을 겁니다.** (14:30~14:34)

## 이 위키에서의 자리 — auto의 반대 방향

이 위키는 *auto* 를 **확장되는 것**으로 봐 왔다.

| 소스 | auto의 방향 | 근거 |
|---|---|---|
| [[anthropic-claude-code-auto-mode]] | 권한 승인 → 분류기 | [[transcript-classifier]]가 위험 행동만 차단 |
| [[privacy-auto-mode]] ([[jean-denis-greze]]) | 사람 승인 → LLM 판단, 민감도 낮은 영역부터 | *"모델 용량과 함께 확장"* |
| [[goal-level-delegation]] | 감시 → 목표 위임 | 산출물 검증 |
| **이 개념** | **auto 없음, 앞으로도** | **결정하는 것이 디자인** |

차이는 **왜** 에 있다. 위 셋은 *모델이 충분히 좋아지면* auto가 넓어진다고 보고, 이 개념은 모델 능력과 **무관하게** auto를 거부한다 — 자동화되면 *"아무도 결정하지 않은"* 것이 되기 때문이다. [[no-silent-write]]([[promptql]])가 *에이전트는 제안만, 사람이 승인* 을 **물러서지 말 규칙**으로 둔 것과 같은 자리이되, 그쪽 이유는 *책임·귀속* 이고 이쪽은 *의도의 존재* 다.

⚠️ 화자가 *"지금은 가능하지 않다 — 어쩌면 영원히"* 와 *"auto는 없다"* 를 함께 말해, 원리적 거부인지 현재 능력 판단인지 **모호**하다. 위키는 두 진술을 그대로 둔다.

## [[generator-evaluator-pattern]]과의 관계

[[anthropic-harness-design-long-running-apps]]도 *멀티샷* 이다 — 5~15회 반복 후 plateau, 10번째에 창발적 도약. 그러나 그쪽의 반복은 **에이전트-에이전트**(생성기·평가기)이고 사람은 루프 밖이다. 이 개념의 반복은 **사람-에이전트**이고 사람이 매 회 형용사를 고른다. 같은 *"원샷은 안 된다"* 에서 **누가 반복을 돌리는가**가 갈린다 — 그리고 그 갈림이 [[steering-altitude]]다.

## References

- [[tech-bridge-impeccable-design-steering]] (first-seen) · [[paul-bakaus]] · [[impeccable]]
- [[tech-bridge-taste-labs-measuring-slop]] — 낮은 의도 = 원샷
- 관련: [[steering-altitude]] · [[adjective-verb-steering]] · [[fuzzy-intent-discovery]] · [[decision-quality]] · [[privacy-auto-mode]]
