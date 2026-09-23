---
title: 선형 하네스 vs 폐루프 하네스 (Linear vs Closed-Loop Harness)
type: concept
category: pattern
tags: [harness, agent-loop, determinism, tests, guardrails, adk, memory]
aliases: [선형 하네스, 폐루프 하네스, closed loop harness, 하네스 설계의 세 결정]
related: [agent-harness-design, harness-engineering, verifiable-goals, generator-evaluator-pattern, ralph-wiggum-method, context-resets-and-compaction, agent-memory, tools-and-context-over-harness, workflow-vs-agent]
first-seen: tech-bridge-lopopolo-agent-harness
sources: [tech-bridge-lopopolo-agent-harness]
created: 2026-09-23
updated: 2026-09-23
---

# 선형 하네스 vs 폐루프 하네스

**하네스를 직접 짤 때 내리는 세 결정 — 루핑(몇 번 도는가) · 도구(무엇을 언제 어떻게) · 메모리(얼마나 중요하고 언제 불러오나) — 의 조합으로 하네스를 분류한다.** 결정론이 필요하면 루프 없는 **선형**, 코드 수정처럼 끝 상태가 있는 일이면 **폐루프**. 빌리의 코드 데모, [[tech-bridge-lopopolo-agent-harness]] (19:44~25:10).

> **모든 상황에 맞는 최고의 하네스는 하나로 정해져 있지 않습니다.** (…) **한 문제에서 중요한 것이 다른 문제에서는 중요하지 않을 수도 있습니다.** 따라서 각 하네스마다 **루핑에 관해** 몇 가지 결정을 내릴 수 있습니다. **몇 번 반복될까요? 도구. 어떤 도구를 사용해야 할까요? 언제 사용해야 할까요? (…) 그리고 기억력.** (20:55~21:27)

출발점 — *"모델은 **파일을 검사해야 한다는 텍스트만** 출력합니다. **하네스는 그 의도를 행동으로 연결하는 역할을 해야 합니다.**"*(20:28~20:38)

## 세 패턴

| | **선형** | **폐루프** | **가드레일 + ADK** |
|---|---|---|---|
| 흐름 | 파일 검사 → 권장 출력 → 종료 (또는 검사 없이 답) | 코드 수정 → 테스트 → 실패면 반복 | 폐루프 + 안전장치 + 메모리 압축 |
| 종료 | 항상 한 번 | **테스트 통과** 또는 ~5회 | 〃 |
| 메모리 | 불필요 | **실패 출력을 메모리에 되먹임** | **압축(compaction) 내장** |
| 좋은 곳 | *"결정론이 어느 정도 필요한 경우"*(21:52~21:57) | *"코드 편집 등에서 매우 흔하게"*(22:35) | 처음부터 짜기는 싫고 기성품보다 맞춤이 필요할 때(23:31~23:54) |

⭐ **폐루프의 핵심은 통과 여부가 아니라 실패 이유다.**

> 단순히 통과 여부만 확인하는 것이 아닙니다. **우리는 왜 실패했는지 확인하고, 그 오류를 메모리에 다시 저장한 다음, 테스트가 통과될 때까지 반복할 것입니다.** (23:12~23:22)

세 번째 패턴의 안전장치는 **명령 블록리스트** 하나다 — *"파괴적인 명령을 차단하는 기능 (…) 파일을 삭제하거나 데이터베이스를 삭제하거나 GitHub에 푸시하는 등의 위험한 명령"*(23:54~24:08). 도구는 Google **Agent Development Kit(ADK)**.

## 위키에서의 좌표

- **선형 vs 폐루프 = [[workflow-vs-agent]]의 하네스 쪽 표현** — 고정 흐름(결정론) vs 끝 상태까지 도는 루프.
- **폐루프 = [[verifiable-goals]] · [[generator-evaluator-pattern]]의 가장 작은 구현.** [[harness-engineering]]의 *stop validation 훅*(완료 선언 시 테스트 강제, 실패 시 재반복)과 같은 동작을 **훅이 아니라 루프 코드로** 짠 것. [[ralph-wiggum-method|Ralph Loop]]의 단일 세션판.
- **메모리 압축** → [[context-resets-and-compaction]].
- ⚠️ **같은 에피소드의 [[tools-and-context-over-harness|Lopopolo]]는 하네스를 만들지 말라고 한다.** 빌리의 정당화는 **이해**다 — *"직접 하네스를 제작하는 것은 [뭔가] 고장 났을 때 내부적으로 어떤 일이 일어나는지 이해하는 방법"*(19:53~19:56).

## ⚠️ 유보

- **데모는 장난감 규모다** — 파일 하나 읽기, 테스트 5회 반복. 루프 상한·메모리 크기·비용을 어떻게 정하는지 없다.
- **보안이 블록리스트뿐이다** — 블록리스트는 우회가 쉽고, [[prompt-injection]]·권한 경계는 다루지 않는다.
- **"어떤 하네스가 어떤 용도에 좋은가"** 를 묻고(24:30~24:37) **답하지 않는다.**

## References

- [[tech-bridge-lopopolo-agent-harness]]
- 관련: [[agent-harness-design]] · [[harness-engineering]] · [[workflow-vs-agent]] · [[verifiable-goals]] · [[generator-evaluator-pattern]] · [[ralph-wiggum-method]] · [[context-resets-and-compaction]] · [[agent-memory]]
- 반대 입장: [[tools-and-context-over-harness]]
