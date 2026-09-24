---
title: 컨텍스트 부패 (Context Rot)
type: concept
category: theory
tags: [context-window, attention, long-context, degradation, context-engineering]
aliases: [context rot, 문맥 부패, 컨텍스트 열화, context degradation, 맥락 왜곡]
related: [context-engineering, context-anxiety, long-context-agents, context-resets-and-compaction, attention-mechanism, sparse-attention, toolbox-pattern, agent-memory]
first-seen: tech-bridge-oracle-agent-memory-harness
sources: [tech-bridge-oracle-agent-memory-harness]
created: 2026-09-24
updated: 2026-09-24
---

# 컨텍스트 부패 (Context Rot)

**컨텍스트 창에 넣는 것이 많아질수록 항목 하나하나가 받는 주의가 줄어, 대화가 길어질수록 모델이 궤도를 잃는 현상.** 그래서 창을 키우는 것은 메모리 문제의 답이 아니고, **창은 가능한 한 작게 유지하라**는 처방으로 이어진다. [[ignacio-martinez|Ignacio Martinez]]([[oracle|Oracle]]), [[tech-bridge-oracle-agent-memory-harness]].

> 이러한 맥락을 (…) **"[context rot]" 또는 시간이 지남에 따라 맥락이 저하됨** (…) [컨텍스트 창에] 물건을 많이 놓을수록 (…) **[어텐션]을 덜 받게 될 것입니다. 각각의 것들에 대해** (25:29~25:48)

(ko는 *rot* 을 **"맥락 왜곡"** 으로 옮기고 문장 끝에 **없던 "날씨"** 를 붙였다. 챕터 제목은 *"문맥 부패"*.)

## 논증 — 두 갈래

**① 주의의 희석(품질).** 사람의 대화 비유:

> 30분 동안 (…) 여러분의 주의 (…) 아주 높을 거예요. 왜냐하면 저는 방금 대화를 시작[했으니까요]. 하지만 만약 **대화는 8시간 동안 지속됩니다. 날 때리고 싶겠지**, 그렇지? (…) 결국 거의 너는 아무것도 배우지 못했어. (26:08~26:25)

**② 어텐션 행렬의 제곱 비용(계산).**

> **주의 매트릭스** 신경망 또한 성능이 저하될 것입니다. 그리고 **제곱에 비례하여 증가합니다.** 주의 행렬은 (…) **나머지 토큰 각각에 대해 토큰 하나씩** (…) 창문이 클수록 (…) 행렬은 두 가지 측면에서 모두 확장됩니다. **행의 수** (…) **컬럼**이 문제입니다. (26:35~26:57)

**처방:**

> [컨텍스트 창을] 가능한 한 [작게 유지해] **맥락의 저하를 피하십시오.** (27:00~27:03)

⚠️ **①과 ②는 같은 주장이 아니다.** 화자는 둘을 한 흐름으로 잇지만, **n² 비용은 계산량·지연의 문제**이고 그 자체가 *항목당 주의가 줄어 품질이 떨어진다* 는 것을 보여 주지는 않는다(softmax 정규화로 인한 희석이 ①의 더 가까운 설명이지만 **화자는 그렇게 말하지 않는다**). 이 위키는 **①을 context rot의 정의로, ②를 별개의 비용 논거로** 기록한다. 그리고 **어느 쪽에도 측정은 없다** — 몇 토큰부터 얼마나 떨어지는지 수치가 없다.

## "1500만 토큰 창"에 대한 반론

> 사람들은 "그럼 왜?"라고 묻습니다. "이 모든 게 정말 필요할까?" (…) **"그럼, 넣어봅시다." 1500만 컨텍스트 윈도우 아직은 불가능하지만**, 어떤 사람들은 [그것이 해결책이라고] 실제로 믿습니다. (…) [컨텍스트 창은] **단기 기억의 한 유형**입니다. (25:02~25:24)

즉 context rot는 **메모리 엔지니어링이 필요한 이유**로 제시된다 — 창은 단기 기억일 뿐이고, 커져도 장기 기억을 대신하지 못하며, 커질수록 썩는다. → [[agent-memory]] · [[files-vs-database-agent-memory]]

> ⚠️ Contradiction: **창을 늘리는 쪽 소스.** 이 위키의 [[long-context-agents]]([[tech-bridge-minimax-m3-long-context|MiniMax]], 09-08)는 에이전트의 긴 도구 호출 이력을 **긴 창으로 받는 것**을 처방했고, [[sparse-attention]]은 바로 ②(제곱 비용)를 줄이는 기술이다. 두 입장은 **서로 다른 문제를 푼다** — MiniMax는 *이력을 버리면 잃는 것*, Martinez는 *이력을 다 넣으면 흐려지는 것*. **② 비용 논거는 sparse attention이 약화시키지만 ① 희석 논거는 그렇지 않다.** 이 위키는 어느 쪽이 맞는지 판정하지 않는다 — **두 소스 모두 측정이 없다.**

## 이 위키의 이웃 개념과

| 개념 | 무엇이 문제인가 | 누구의 행동인가 |
|---|---|---|
| **context rot (이 페이지)** | 많이 넣을수록 **각 항목의 주의가 희석** | 모델의 **성능 저하** |
| [[context-anxiety]] | 한계가 가깝다고 **느끼면 조기 종료** | 모델의 **행동 편향** |
| lost in the middle([[tech-bridge-lopopolo-agent-harness]], 09-23) | 긴 컨텍스트의 **중간부 망각** | 모델의 **위치 편향** |
| [[context-window-as-floppy-disk]] | 창이 작다는 **용량** 비유 | — |

처방 쪽: [[context-resets-and-compaction]](창을 비우거나 압축), [[toolbox-pattern]](도구·스킬을 **필요할 때만** 넣고 매 반복마다 뺀다), [[context-engineering]](무엇을 넣을지 고른다), OAMP 컨텍스트 카드([[oracle]] — 스레드를 주제·요약·사실·선호·미해결 질문으로 압축).

## ⚠️ 미해결

- **정량** — 어느 길이부터, 어떤 과제에서, 얼마나.
- **① 희석의 메커니즘** — 화자는 제곱 비용으로 설명하고 멈춘다.
- **작게 유지하라** vs **긴 이력이 필요하다**([[long-context-agents]]) — 과제별 경계선.

## References

- [[tech-bridge-oracle-agent-memory-harness]] · [[ignacio-martinez]]
- [[context-anxiety]] · [[long-context-agents]] · [[sparse-attention]] · [[attention-mechanism]] · [[context-resets-and-compaction]] · [[context-engineering]] · [[toolbox-pattern]] · [[agent-memory]] · [[context-window-as-floppy-disk]]
