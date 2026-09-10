---
title: 프라이버시 auto mode (Privacy Auto Mode)
type: concept
category: pattern
tags: [auto-mode, privacy, policy, disclosure, human-in-the-loop, scaling, sensitivity-zones]
aliases: [프라이버시 자동 모드, 민감도 낮은 영역]
related: [transcript-classifier, deny-and-continue, agent-governance-layers, sweeper-agent, no-silent-write, sutton-bitter-lesson, agent-collaboration-as-search, black-box-agent-approach]
first-seen: tech-bridge-agent-to-agent-as-search
sources: [tech-bridge-agent-to-agent-as-search, anthropic-claude-code-auto-mode]
created: 2026-09-10
updated: 2026-09-10
---

# 프라이버시 auto mode

**정보 공개의 위험 판단을 — 코딩에서 도구 호출의 위험 판단이 그랬듯 — 사람의 승인에서 LLM의 판단으로 옮기되, 민감도 낮은 영역부터 시작해 모델 용량과 함께 그 영역을 넓히는 것.** [[jean-denis-greze]]의 전망.

> **프런티어는 auto라고 생각합니다.** 코딩에서 우리는 모든 걸 승인하다가, *"YOLO, 위험하게 살자"* 가 됐다가, 이제 **Anthropic이 auto mode를 내려줬죠.** auto mode는 우리가 좀 바보 같은 짓을 할 때를 알아내 말해 줍니다. **사일로를 가로지르는 A2A도 같을 거라고 생각합니다.** — [[tech-bridge-agent-to-agent-as-search]]

## 세 단계의 유비

| 단계 | 코딩 ([[anthropic-claude-code-auto-mode]]) | 프라이버시 (이 개념) |
|---|---|---|
| 1 | 모든 도구 호출을 승인 | 모든 공유를 사람이 승인 → [[no-silent-write]] |
| 2 | YOLO (`--dangerously-skip-permissions`) | 전략 1 — 신뢰 경계 안 전체 접근 |
| 3 | **auto mode** — [[transcript-classifier]]가 위험한 것만 차단, [[deny-and-continue]] | **민감도 낮은 영역**은 LLM이 판단, 나머지는 *"사람 검토나 항상 사람 승인"* |

이 위키의 auto mode 지식은 **행동**(파일 삭제·외부 전송·자격증명 노출)의 위험 분류다. 이 개념은 같은 구조를 **정보 공개**(무엇을 누구에게 드러내는가)에 적용하자는 것이다.

## 경로와 처방

> 우리는 **민감도 낮은 정보가 꺼내져 공용 공간에 놓이는 것에 익숙해질** 것이고, 그다음 **사람 검토나 항상 사람 승인**인 자리가 있을 것이고, 시간이 지나며 LLM이 더 강력해지고, 우리는 **안전한 정책을 그 안에 인코딩**하는 데 더 능숙해지고 (…) 때로는 **사람을 개입시킬지 결정하는 것까지** auto가 될 겁니다.

예: 협력업체·재무팀 주간 통화 노트 요청 → LLM이 *"당신의 역할을 보면 허락 없이 공유해도 돼"* 라고 **위험 관점에서 판단.**

> **auto의 멋진 점은, 시스템을 그렇게 설계하면 모델 용량과 함께 확장된다**는 겁니다. (…) **LLM이 판단해도 괜찮은 민감도 낮은 영역을 확실히 정의하고 그것을 받아들이세요.** 그러면 시간이 지나며 마법처럼 그 영역이 커집니다.

→ [[sutton-bitter-lesson]]의 처방을 프라이버시 아키텍처에 적용한 것이다. 발표자의 판정 기준 두 질문(*사람이 줄어드는가 / 모델이 좋아지면 좋아지는가*)에 '예'로 답하는 유일한 전략이 이것이다.

## 어디부터 — 그리고 어디는 아직

- **작은 회사부터** — *"10~50명 규모의 신뢰도 높은 작은 회사, 공유 못 할 데이터가 뭔지(재무·인사) 명확한 곳"*. **포춘 500은 한동안 아님.** *"6개월 안에"* 많이 볼 것(⚠️ 근거 없음).
- 같은 날 [[tech-bridge-company-brain-security|PromptQL 편]]은 정확히 그 **포춘 은행**을 고객으로 두고 접근 제어를 **전부 결정론적**으로 놓는다. 두 소스의 차이는 **고객이 다르다**는 것으로 상당 부분 설명된다.

## ⚠️ 이 개념이 답하지 않는 것

- **정책을 집행하는 LLM은 프롬프트와 같은 취약성을 갖지 않는가** — [[agent-governance-layers]]가 Composio 편에 던진 질문이 그대로 남는다. 발표자는 *"안전한 정책을 인코딩하는 데 더 능숙해질 것"* 이라고만 한다. 코딩 auto mode가 이 문제를 **분류기를 reasoning-blind로 만들어**([[transcript-classifier]]) 다룬 것과 달리, 이쪽에는 구조적 처방이 없다.
- **민감도의 정의** — 누가 어떤 정보를 낮은 민감도로 분류하는가. *재무·인사는 아니다* 외에 없다.
- **오공개의 비가역성** — 한 번 드러난 정보는 되돌릴 수 없다([[action-reversibility]]). 코딩 auto mode는 되돌릴 수 있는 행동이 많다는 점에서 유비가 어긋난다. 소스는 이를 다루지 않는다.
- 화자 자신의 유보 — *"에이전트가 프라이버시 결정을 전부 내리는 미래를 신뢰하는가? 잘 모르겠다. 좋든 나쁘든 그 방향으로 간다고 생각할 뿐."*

## References

- [[tech-bridge-agent-to-agent-as-search]] (first-seen) · [[jean-denis-greze]]
- [[anthropic-claude-code-auto-mode]] — 유비의 원본 · [[transcript-classifier]] · [[deny-and-continue]]
- 관련: [[sweeper-agent]] · [[no-silent-write]] · [[sutton-bitter-lesson]] · [[agent-governance-layers]] · [[black-box-agent-approach]]
