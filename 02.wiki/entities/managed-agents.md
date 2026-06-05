---
title: Managed Agents
type: entity
category: product
tags: [anthropic, agent-infrastructure, meta-harness, claude-platform]
aliases: [Claude Managed Agents]
sources: [anthropic-managed-agents, anthropic-dynamic-workflows]
links:
  - https://platform.claude.com/docs/en/managed-agents/overview
created: 2026-05-25
updated: 2026-06-01
---

# Managed Agents

[[anthropic|Anthropic]]의 Claude Platform 호스티드 서비스. 장기 horizon 에이전트를 사용자 대신 실행하면서, 특정 구현보다 오래 살아남도록 설계된 작은 인터페이스 셋을 제공하는 **메타-하네스**.

## 위키에서 알려진 사실

- 세 가지 추상으로 가상화: **session / harness / sandbox**. 각각 독립적으로 fail·replace.
- 인터페이스 (블로그 인용):
  - `execute(name, input) → string` (sandbox tool 호출)
  - `provision({resources})`
  - `emitEvent(id, event)`, `getSession(id)`, `getEvents()`
  - `wake(sessionId)`
- Brain(Claude+harness)을 컨테이너 *밖*으로 빼서 stateless로. 결과: **p50 TTFT ~60%↓, p95 90%+↓**.
- Session log를 context window *밖*에 두어 compaction의 비가역 손실 회피. ([[context-resets-and-compaction]])
- Token이 sandbox에 **절대** 안 들어감 — bundled-with-resource (Git) 또는 vault + MCP proxy 패턴.
- [[claude-code|Claude Code]] 같은 범용 harness, task-specific harness 모두 수용.

## 디자인 원칙

- *Programs as yet unthought of*에 대비. 인터페이스만 opinionated, 구현은 swappable.
- [[pets-vs-cattle]] 분리: 컨테이너·harness 모두 cattle화.
- [[brain-hands-decoupling]] (이 글의 메인 모티프) → "many brains, many hands".

## 관련 — Dynamic workflows

[[claude-code|Claude Code]]의 [[dynamic-workflows|dynamic workflows]]는 동일 사상을 *제품 표면*에서 구현: **coordination이 대화 바깥**에서 돌고 진행상황이 **resumable checkpoint**로 저장됨 — 본 페이지의 session-log 외부화([[context-resets-and-compaction]]) 및 stateless harness 원칙과 동형. "many brains, many hands"가 한 세션의 10s~100s parallel subagent로 나타난 형태.

## References

- [[anthropic-managed-agents]]
- [[anthropic-dynamic-workflows]]
- [공식 문서](https://platform.claude.com/docs/en/managed-agents/overview)
