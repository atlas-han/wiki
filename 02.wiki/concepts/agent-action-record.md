---
title: 에이전트 행동 기록 (Agent Action Record)
type: concept
category: pattern
tags: [logging, memory, trust, observability, skills]
aliases: [행동 기록, the record]
related: [agent-memory, agent-knowledge-sourcing, knowledge-work-agent-gap, behavior-validated-trust, skill-self-improvement, named-human-accountability, black-box-agent-approach]
first-seen: tech-bridge-knowledge-work-agent-infrastructure
sources: [tech-bridge-knowledge-work-agent-infrastructure, tech-bridge-company-brain-security, tech-bridge-agent-to-agent-as-search]
created: 2026-09-09
updated: 2026-09-10
---

# 에이전트 행동 기록

**에이전트가 모든 앱에 걸쳐 한 모든 행동을 한곳에 로깅하면, 하나의 로그가 세 가지 서로 다른 문제를 동시에 푼다**는 패턴.

전제는 중앙화다 — 모든 것이 한 지점을 지나가야 그 위에 기록 층을 쌓을 수 있다.

## 한 로그, 세 산출

| 산출 | 무엇이 해결되는가 |
|---|---|
| **기억** | 에이전트가 *비슷한 작업이 전에 어떻게 됐는지* 되돌아본다 → 매번 백지 상태로 시작하지 않는다 |
| **신뢰** | *"에이전트가 하는 말을 믿는 대신 그 앱들에 직접 가서 무엇을 했는지 볼 수 있다"* |
| **스킬** | 충분히 쌓이면 패턴이 보이고 **조직이 어떻게 일하는지의 증류**가 된다 |

> **기록은 더 이상 무슨 일이 있었는지의 역사가 아니라 당신 회사가 어떻게 작동하는지의 그림입니다.** — [[tech-bridge-knowledge-work-agent-infrastructure]]

## 세 층위

기록에서 나온 지식은 적용 범위가 다르다:

1. **도구가 일반적으로 어떻게 작동하는가** — 모든 사람에게 적용
2. **회사가 일을 어떻게 하는가** — 조직 범위
3. **당신이 어떻게 선호하는가** — 개인 범위

## [[agent-knowledge-sourcing]]과의 관계

두 페이지는 **직교한다.** [[agent-knowledge-sourcing]]은 *지식이 어디서 왔는가* 로 가른다 — 사람이 적어둔 것([[retrieval-augmented-generation|RAG]])인가 에이전트가 겪은 것([[agent-memory|메모리]])인가. 이 페이지는 **겪은 것을 누구의 범위로 집계하는가**를 가른다.

즉 행동 기록은 [[agent-memory]]의 **조직 규모 버전**이고, 그래서 [[agent-memory]]가 가진 성질(쓰기 방향을 갖는다)을 그대로 물려받는다.

## 신뢰가 점증한다는 주장

> 점점 더 옳은 일을 하는 것을 보면서 **신뢰가 쌓이고 더 많은 일을 넘기게 됩니다.**

이것은 [[trusted-throughput]]이 조직 운영에서 말한 것과 같은 구조이고, [[behavior-validated-trust]]가 코드에서 말한 것과 같은 원리다 — **주장이 아니라 관측 가능한 증거가 신뢰의 근거가 된다.**

## ⚠️ 미해결

- **로깅 자체의 비용·지연**이 소스에서 다뤄지지 않는다.
- **기록의 프라이버시 문제 미논의** — 모든 앱의 모든 행동을 한곳에 모으는 것의 위험이 언급되지 않는다.
- **"패턴이 보이기 시작한다"의 메커니즘이 없다** — 무엇이 로그를 스킬로 증류하는지 설명되지 않는다.

## 감사 로그의 둘째 열 — 그리고 로그가 없는 설계 (2026-09-10)

[[tech-bridge-company-brain-security]]의 [[named-human-accountability]]는 이 개념의 로그에 **둘째 열**을 더한다 — Composio가 *에이전트가 무엇을 했는가* 를 기록한다면, PromptQL은 *어느 사람이 승인했는가* 를 기록한다(*"Claude가 추가했다"* 는 허용되지 않는다).

반대로 [[tech-bridge-agent-to-agent-as-search]]의 [[black-box-agent-approach|블랙박스]]는 **트레이스에 아무도 접근할 수 없다**는 것을 전제로 삼는다 — 이 개념의 처방과 정면 충돌한다. 화자 자신이 그것을 인정한다: *"진짜 블랙박스일 수는 없습니다. CISO 조직 어딘가에 모든 데이터에 접근하는 사람이 있어야 합니다."* 즉 이 개념이 말하는 기록은 블랙박스에서도 **누군가에게는** 있어야 하고, 그 순간 블랙박스가 아니다. 이 개념의 미해결 항목 *기록의 프라이버시 문제* 가 반대편에서 다시 나타난 것이다.

## References

- [[tech-bridge-knowledge-work-agent-infrastructure]] · [[composio]]
- [[tech-bridge-company-brain-security]] · [[tech-bridge-agent-to-agent-as-search]] — 사람 이름 열 · 블랙박스와의 충돌 (2026-09-10)
