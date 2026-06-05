---
title: Deny-and-Continue
type: concept
category: pattern
tags: [agent-safety, claude-code, permission-system]
related: [transcript-classifier, agentic-misbehavior, agent-harness-design]
first-seen: anthropic-claude-code-auto-mode
sources: [anthropic-claude-code-auto-mode]
created: 2026-05-25
updated: 2026-05-25
---

# Deny-and-Continue

권한 게이트가 action을 차단했을 때 **세션을 끊지 않고** 차단 사유와 함께 agent에게 결과를 돌려보내는 패턴. Agent는 다른 안전한 path를 시도한다. [[anthropic-claude-code-auto-mode]]의 핵심 UX 결정.

## 동기

Auto mode의 목적은 *`--dangerously-skip-permissions`를 대체하되 interruption은 안 가져오는 것*. 매 block마다 인간에게 묻는다면 manual mode로 되돌아간다. 그러나 block을 무시할 수도 없다.

## 동작

- [[transcript-classifier]]가 block하면 **tool result**로 사유가 돌아감 + "boundary를 in good faith로 받아들이고 우회를 시도하지 말라"는 지시
- Agent는 ① 다른 안전한 접근을 시도하거나, ② 사용자에게 물어볼 결정
- **Backstop**: 3 연속 denial 또는 20 누적이면 human escalation; 헤드리스(`claude -p`)는 process 종료 — 무한 우회 시도 방지

## False positive의 비용 회수

> A 0.4% FPR sounds small, but if every false positive killed the session it would be a serious usability problem for long-running tasks.

대신 한 retry로 비용을 흡수: agent가 nudge를 받고 재고 후 대개 다른 path 발견.

## 멀티 에이전트 handoff

- **Outbound** subagent 위임: classifier가 **deny 가능** (작업 자체가 의심스러우면 시작도 안 함)
- **Inbound** subagent 리턴: classifier는 **경고만 prepend** — 결과는 보존, orchestrator가 어떻게 다룰지 결정

## References

- [[anthropic-claude-code-auto-mode]]
