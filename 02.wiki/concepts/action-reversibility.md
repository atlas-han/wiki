---
title: 행동 가역성 (Action Reversibility)
type: concept
category: framing
tags: [reversibility, blast-radius, sandbox, trust, undo]
aliases: [가역성, undo 없음, 폭발 반경]
related: [agent-governance-layers, knowledge-work-agent-gap, agentic-misbehavior, trusted-throughput, deny-and-continue]
first-seen: tech-bridge-knowledge-work-agent-infrastructure
sources: [tech-bridge-knowledge-work-agent-infrastructure]
created: 2026-09-09
updated: 2026-09-09
---

# 행동 가역성

**되돌릴 수 있는지 여부가 에이전트를 신뢰하는 *시점* 을 결정한다**는 프레이밍.

## 신뢰의 시점이 앞으로 이동한다

| | 코드 | 지식 노동 |
|---|---|---|
| 되돌리기 | `revert` · `bisect` | 발송된 메일 · 송금 · hard delete — **없다** |
| 신뢰의 시점 | **사후** — 돌려보고, 확인하고, 틀렸으면 되돌린다 | **사전** — 행동하기 *전에* 신뢰해야 한다 |
| 실패의 성질 | 나쁘지만 **영구적이지 않다** | **영원하다** |

> 그게 이 에이전트들이 코딩 에이전트는 결코 그렇지 않았던 방식으로 위험하게 느껴지는 이유입니다. **자주 실패해서가 아니라, 저기서는 실패가 영원하기 때문입니다.** — [[tech-bridge-knowledge-work-agent-infrastructure]]

그리고 가역성이 있다는 사실 자체가 **에이전트를 풀어놓을 수 있게 하는 조건**으로 제시된다:

> 그게 **에이전트를 마음껏 풀어놓을 자신감을 주는 것**입니다 — 망가뜨려도 **돌아올 길이 있기** 때문입니다.

## 샌드박스가 undo의 대체물이다

되돌릴 수 없는 행동(hard delete 등)에 대한 처방은 **실제 도구를 흉내 낸 샌드박스**다. 에이전트가 먼저 샌드박스에서 실행하고, 사람이 검토하고, 그 다음 현실로 간다.

> **코드에서는 실수가 일어난 뒤에 되돌립니다. 여기서는 일어나기 전에 잡습니다. 타이밍은 다르지만 결과는 같습니다 — 달라붙지 않는 실수.**

메일 200통 사건에 적용하면: 되돌릴 수 있는 행동에는 되돌리기 버튼을, 그럴 수 없는 것은 샌드박스를 먼저 때리고 **"당신의 메일 200통이 삭제되려고 합니다. 하시겠습니까?"** 라는 알림이 갔을 것이다.

## 폭발 반경이 게이트의 크기를 정한다

[[agent-governance-layers]]의 *게이트마다 크기가 다르다* 는 서술과 같은 축이다 — **되돌릴 수 있는 행동에는 얇은 게이트, 되돌릴 수 없는 행동에는 두꺼운 게이트.** 이 위키의 [[deny-and-continue]]가 다룬 *막되 멈추지 않기* 도 같은 계열의 처방이다.

## ⚠️ 발표자 본인이 인정하는 한계

> **가역성은 지식 노동에서 복제하기 가장 어렵습니다.** 코드에 있는 방식의 진짜 undo는 아마 지식 노동의 **모든 시나리오에 존재하지 않을 것입니다.**

> **아직 다 되지는 않았습니다.**

**샌드박스의 충실도 문제가 다뤄지지 않는다** — 모의 환경과 실제 환경의 차이에서 오는 오검증 위험이 논의되지 않는다. 어떤 행동이 되돌릴 수 있는지의 분류를 *수십억 건의 행동에서 배우고 있다* 고만 말하고 그 분류 기준은 제시되지 않는다.

## References

- [[tech-bridge-knowledge-work-agent-infrastructure]] · [[composio]] · [[karan-vaidya]]
