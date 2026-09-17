---
title: 매일 밤의 메모리 압축 (Nightly Memory Consolidation)
type: concept
category: pattern
tags: [memory, compaction, agents, personal-agent, meta, muse]
aliases: [메모리 압축, 밤의 정리, nightly compaction]
related: [agent-memory, context-resets-and-compaction, agent-governance-layers, proactive-idea-feed, muse-spark, long-context-agents, skill-self-improvement]
first-seen: tech-bridge-zuckerberg-muse-in-daily-use
sources: [tech-bridge-zuckerberg-muse-in-daily-use, tech-bridge-zuckerberg-muse-personal-agent]
created: 2026-09-17
updated: 2026-09-17
---

# 매일 밤의 메모리 압축

**에이전트가 하루가 끝나면 그날의 모든 활동을 훑어 메모리로 압축하는 주기적 정리.** [[muse|Muse]]의 동작이고, 두 소스에 걸쳐 나온다.

> **매일 저녁 그날 한 모든 것을 살펴보고 그것을 메모리로 압축(compact)합니다. 그리고 이건 사람이 잘 때 생각하고 압축하는 방식과 비슷합니다.** — [[mark-zuckerberg]], [[tech-bridge-zuckerberg-muse-in-daily-use]] (20:43~20:57)

앞 편에서는 같은 것이 **"밤 공부"** 로 서술됐다 — *"성찰을 메모리로 굳힌다(consolidate)"*([[tech-bridge-zuckerberg-muse-personal-agent]], 진행자 표현 *"밤에 공부한다"*). **이 편이 그 메커니즘에 시각과 대상을 준다.**

## 무엇이 들어가고 무엇이 빠지는가

**빠지는 것 — 자격증명:**

> **자격증명 같은 건 Muse 에이전트의 데이터베이스나 메모리가 아니라 그 안전한 자격증명 저장소에 둡니다.** (20:34~20:42)

메모리와 [[credential-injection-outside-sandbox|자격증명 저장소]]가 **다른 저장소**라는 선언이다. → [[one-time-virtual-card]] · [[least-privilege-connectors]]

**남는 것 — 모델이 정한다:**

> **대체로는 그것이 스스로 정합니다.** (20:29~20:31)

> ⚠️ **판정 주체가 모델이고, 판정을 검증하는 서술이 없다.** 사용자가 압축 결과를 보거나 되돌릴 수 있는지도 소스에 없다.

## compaction이 실패가 아니라 기능으로 놓이는 자리

이 위키에서 compaction은 지금까지 **손실**의 이름이었다.

| 페이지 | compaction을 무엇으로 보는가 |
|---|---|
| [[context-resets-and-compaction]] | 컨텍스트 관리 문제 — 무엇이 지워지는가 |
| [[agent-governance-layers]] | **거버넌스 실패 원인** — 프롬프트에 넣은 안전 지시가 지워진다 |
| **이 페이지** | **설계 기능** — 압축 품질이 모델 개선의 지표 |

차이는 **주체와 시점**이다. 앞의 둘은 컨텍스트 윈도가 차서 **불가피하게** 일어나는 절삭이고, 이쪽은 **하루 경계에서 의도적으로** 도는 정리다. 즉 *어쩔 수 없이 버리는 것*과 *골라서 남기는 것*이다.

⚠️ **그러나 [[agent-governance-layers]]가 제기한 위험은 그대로 남는다** — 무엇을 *"무관한 것"* 으로 판정할지가 모델에 달려 있다면, **사용자가 중요하다고 여긴 것이 밤새 사라질 수 있다.** 소스는 이 가능성을 다루지 않는다.

## 모델이 좋아지면 압축이 좋아진다

> **기저 AI 모델의 다른 부분들처럼 이것도 시간이 지나며 개선될 겁니다 — 매달 우리는 더 유능한 새 모델을 출하하고 있고, 그게 이것의 흥미로운 부분이 될 겁니다.** (20:57~21:13)

> 방금 **[[muse-spark|Muse Spark 1.3]]** 을 출하했고, 당신의 Muse 에이전트도 며칠 안에 그 모델로 업그레이드될 겁니다. 그러면 **메모리를 압축하는 것도 더 잘하게 되고 — 맞는 것을 기억하고 무관한 것은 기억하지 않는 데 더 효율적이 될 겁니다.** (21:13~21:36)

**압축 품질을 모델 능력의 지표로 쓴다.** 이 위키의 [[harness-pruning]]이 *모델이 좋아지면 하네스 기능을 지운다*고 말한 것과 같은 형태다 — **능력 향상이 주변 장치의 요구를 줄인다.**

## 무엇을 가능하게 하는가

압축된 메모리가 없으면 [[proactive-idea-feed|아이디어 피드]]의 **두 번째 제안**(자기가 만든 산출물 위에 쌓는 제안)이 성립하지 않는다. 그리고 맥락 교차 알림(*건강을 묻는 중에 아들 진료 예약을 꺼내는 것*)도 마찬가지다.

→ [[agent-memory]] · [[long-context-agents]]

## 미해결 사항

- **압축이 버리는 것** — 무엇을 버리는지, 로그는 남는지.
- **사용자 가시성·편집·되돌리기** — 전부 없음.
- **"무관한 것" 판정의 검증** — 작성자=검증자 문제가 메모리 층에서 반복된다.
- **압축 시각·소요·실패 처리**(밤에 기기가 꺼져 있으면).
- **[[confidential-vm|기밀 VM]] 안에서 도는가** — 소스가 연결하지 않는다.
- **[[agent-fleet-learning|함대 학습]]과의 관계** — 압축된 메모리가 익명화 통찰의 재료인지 이 편에 없다.

## References

- [[tech-bridge-zuckerberg-muse-in-daily-use]] · [[tech-bridge-zuckerberg-muse-personal-agent]] · [[muse]] · [[muse-spark]]
- 관련: [[agent-memory]] · [[context-resets-and-compaction]] · [[agent-governance-layers]] · [[proactive-idea-feed]] · [[harness-pruning]] · [[long-context-agents]] · [[skill-self-improvement]]
