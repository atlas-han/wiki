---
title: Martin Keen
type: entity
category: person
tags: [ibm, explainer, context-engineering, context-failure-modes]
aliases: [Martin Keen]
links:
  - "https://www.youtube.com/@IBMTechnology"
sources: [tech-bridge-context-engineering-four-failure-modes]
created: 2026-10-20
updated: 2026-10-20
---

# Martin Keen

[[ibm|IBM Technology]] 채널의 화이트보드 해설자다. 이 위키에는 [[tech-bridge-context-engineering-four-failure-modes]]로 처음 등장한다. 이 편에서 긴 에이전트 실행에서 컨텍스트 창이 망가지는 네 가지 방식과 처방을 정리했다 → [[context-failure-modes]]. ⚠️ **이름과 소속은 설명란 본문에만 있다**(*"IBM Technology의 Martin Keen이 …"*). 자막에는 자기소개도 IBM도 나오지 않는다. 직함은 미상이다.

## 위키에서 알려진 사실

- 창이 백만 토큰 이상으로 커졌어도 모델은 더 긴 작업을 더 잘하지 못한다고 본다. 근거로 이름 없는 연구 하나를 든다: *"a recent study looked at 18 frontier models and it turned out that they all got less reliable as the context window got bigger"*(00:36~00:46). → [[context-rot]]
- 정의: *"Context engineering is deciding what actually goes into this context window at each step of an agent's run."*(01:04~01:12) → [[context-engineering]]
- 메커니즘은 유한한 *"attention budget"*(04:02~04:20)이다.
- 실패 넷(poisoning · distraction · confusion · clash)과 처방 넷(validate · compact · curate · prune)을 짝짓고, *"all four fixes work by throwing something away. An agent can get better at long tasks by holding less."*(09:46~09:59)로 맺는다. → [[context-failure-modes]] · [[long-context-agents]](⚠️ Contradiction)

## ⚠️ 유보

- 이름·소속은 설명란 기준이다. 수치 둘(18개 모델, 46 vs 19 도구)과 네 유형 이름의 출처를 발화하지 않는다. 통합자가 외부에서 확인한 대응 자료는 [[context-failure-modes]]의 ⚠️ 절에 있다.
- 원본(IBM Technology) 게시일과 녹화 시점은 알 수 없다.

## References

- [[tech-bridge-context-engineering-four-failure-modes]] — first-seen
- [[ibm]] · [[context-failure-modes]] · [[context-rot]] · [[context-engineering]]
