---
title: 선형 하네스 vs 폐루프 하네스 (Linear vs Closed-Loop Harness)
type: concept
category: pattern
tags: [harness, agent-loop, determinism, tests, guardrails, adk, memory]
aliases: [선형 하네스, 폐루프 하네스, closed loop harness, 하네스 설계의 세 결정]
related: [agent-harness-design, harness-engineering, verifiable-goals, generator-evaluator-pattern, ralph-wiggum-method, context-resets-and-compaction, agent-memory, tools-and-context-over-harness, workflow-vs-agent]
first-seen: tech-bridge-lopopolo-agent-harness
sources: [tech-bridge-lopopolo-agent-harness, tech-bridge-oracle-agent-memory-harness]
created: 2026-09-23
updated: 2026-09-24
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

## 루프 상한에 이름이 붙었다 — 인내심 예산 (2026-09-24 · [[tech-bridge-oracle-agent-memory-harness]])

이 페이지가 ⚠️로 남긴 *"루프 상한·메모리 크기·비용을 어떻게 정하는지 없다"* 에 한 실무자의 값이 들어왔다. [[ignacio-martinez|Ignacio Martinez]]([[oracle|Oracle]]):

> 물론 한계는 있습니다. **왜냐하면 우리에게는 무한한 돈이 없기 때문입니다.** (…) **만약 [생성]이 단지 환각**이죠 (…) 차단값은 (…) **Frontier LLM**[에 따라 다릅니다]. (52:23~52:39)

> [Grok 4.1 Fast reasoning — ⚠️ 미확정] (…) **8에서 12 사이의 값을 발견했습니다. 최대 [도구 호출] 횟수 포기하기 전에** (…) **모델의 정밀도와 정확도**[에 따라] (52:41~53:00)

> 제가 정의하고 싶은 것은 (…) **[히스테리시스] 변수** (…) **[하네스]가 모델에게 가질 인내심** (53:17~53:25)

| | 빌리의 폐루프 (09-23) | **Martinez (09-24)** |
|---|---|---|
| 상한 | 테스트 통과 또는 **~5회** | 도구 호출 **8~12회** |
| 근거 | (데모) | **모델별 경험값** — 모델의 정확도에 따라 조정 |
| 이름 | — | **"히스테리시스 변수" = 인내심** |

⭐ **상한을 모델마다 튜닝하는 하이퍼파라미터로 둔다**는 것이 새 점이다. 그리고 데모가 그 필요를 보여 준다 — 같은 질문을 한 번은 **16단계**(47:30), 다시 **2단계**(53:03~53:08)에 풀었다. **분산이 크면 평균이 아니라 꼬리를 자를 상한이 필요하다.** 루프 안쪽은 반대 요구다 — *"실패에 강해서 루프를 절대 빠져나가지 않게"*(33:53~33:59), 데모에서도 오류를 감지하고 *"계속 시도"*(47:35~47:44). **안에서는 버티고, 바깥에서 예산으로 끊는다.**

⚠️ 8~12는 **측정이 아니라 개인 경험**이다. ⚠️ *hysteresis* 는 공학에서 **이력 의존(되돌아올 때 다른 경로)** 을 뜻하는데 화자는 **상한값**의 뜻으로 쓴다 — 비표준 용법이고, 챕터 제목도 *"이력(Hysteresis) 변수"* 로 직역했다. 이 위키는 판정하지 않는다.
