---
title: 동적 키워드 부스팅 (Dynamic Keyword Boosting)
type: concept
category: pattern
tags: [stt, asr, context, call-state, voice-agents]
aliases: [상태별 키워드 부스팅]
related: [transcription-brittleness, voice-agent-pipeline, context-engineering, push-vs-pull-context-retrieval]
first-seen: tech-bridge-voice-agent-failure-modes
sources: [tech-bridge-voice-agent-failure-modes]
created: 2026-09-19
updated: 2026-09-19
---

# 동적 키워드 부스팅

**전사 엔진에 키워드를 통화 내내 고정해 두지 말고, 대화가 그 단어를 기대하는 순간에만 넣는다.** [[tech-bridge-voice-agent-failure-modes]]가 [[transcription-brittleness|전사 취약성]]의 첫 번째 처방으로 제시한다.

> 고유명사의 경우 **키워드 부스팅뿐만 아니라 다른 방법도** 사용하는 것을 권장합니다. **많은 전사 엔진들이 특정 단어를 입력하여 키워드 부스팅을 할 수 있도록 해주지만, 동적 키워드 부스팅은 좀 더 복잡하고 어렵습니다.** (15:44~16:04)

> **즉, 통화가 진행되는 동안 [전체 상태에] 키워드를 계속 유지하지 말라는 뜻입니다. 정확도를 높이려면 해당 답변이 필요하다고 생각될 때 동적으로 추가하기만 하면 됩니다. 즉, 통화의 여러 단계에 따라 [전사] 엔진은 각 단계에서 서로 다른 키워드를 강조 표시하게 됩니다.** (16:04~16:22)

## 왜 전부 넣으면 안 되는가

> 그게 저희가 확인한 바로는 가장 효과적인 방법입니다. 왜냐하면 **전사 엔진의 컨텍스트에 키워드를 너무 많이 넣으면 엔진이 다시 [환각]을 일으키기 시작하거든요.** (16:22~16:41)

**전사 엔진에도 컨텍스트 예산이 있다.** 부스팅된 단어가 많아지면 엔진이 **듣지 않은 것을 그 목록에서 골라낸다** — 부스팅이 정확도를 올리다가 어느 지점부터 내린다.

## 이 위키에서의 좌표

**[[context-engineering]]의 논리가 LLM 바깥에서 그대로 반복되는 자리다.**

| | LLM 컨텍스트 | **STT 키워드 부스팅** |
|---|---|---|
| 다 넣으면 | 성능 저하·[[context-anxiety\|불안]] | **환각** |
| 해법 | 지금 필요한 것만 | **통화 상태별로** |
| 축 | [[push-vs-pull-context-retrieval\|push vs pull]] | 상태 기계가 push |

이 위키가 LLM 층에서 세운 원칙 — *컨텍스트는 많을수록 좋지 않고, 지금 하는 일에 맞춰 고른다* — 이 **다른 모델 종류에서 독립적으로 재발견됐다.** 그리고 여기서는 *지금 하는 일* 이 명확하다: 통화의 상태. 에이전트가 **전화번호를 물은 직후**라면 숫자를, **이름을 물은 직후**라면 고객 명부를 부스팅한다.

이것은 [[typed-field-collection]]과 짝을 이룬다 — 지금 어떤 **타입의 필드**를 수집 중인지 알면, 그것이 곧 **무엇을 부스팅할지**를 정한다. 두 처방이 같은 상태 기계를 공유한다.

## ⚠️ 유보

- **"복잡하고 어렵다"** 고만 하고 **구현이 없다** — 상태를 어떻게 정의하고, 키워드 목록을 어떻게 만들고, 엔진에 실시간으로 어떻게 밀어 넣는지.
- **어느 엔진이 이것을 지원하는지** 이름이 없다.
- **임계값이 없다** — 몇 개부터 환각이 시작되는지.
- **효과 수치가 없다.** *"가장 효과적"* 뿐이다.
- **전환 지연**(상태가 바뀔 때 키워드를 갈아 끼우는 비용)이 [[time-to-first-audio]] 예산과 연결되지 않는다.
- 상태 판정이 틀렸을 때(에이전트가 대화의 위치를 오해할 때) **부스팅이 오히려 해로운 경우**가 다뤄지지 않는다.

## References

- [[tech-bridge-voice-agent-failure-modes]] — first-seen
- [[venky-b]] · [[plivo]]
- 관련: [[transcription-brittleness]] · [[typed-field-collection]] · [[voice-agent-pipeline]] · [[context-engineering]] · [[push-vs-pull-context-retrieval]] · [[context-anxiety]]
