---
title: Managed Agents
type: entity
category: product
tags: [anthropic, agent-infrastructure, meta-harness, claude-platform]
aliases: [Claude Managed Agents]
sources: [anthropic-managed-agents, anthropic-dynamic-workflows, tech-bridge-claude-platform-agent-era]
links:
  - https://platform.claude.com/docs/en/managed-agents/overview
created: 2026-05-25
updated: 2026-09-02
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

## 왜 session / harness / sandbox로 갈렸나 (1차 진술)

[[tech-bridge-claude-platform-agent-era]]에서 [[katelyn-lesse]]가 이 분할의 **이유**를 직접 설명했다. 문서가 *무엇을* 기술했다면 이쪽은 *왜*다.

> 문제는 **샌드박스를 구동하는 기술 자체가 대개 일시적(ephemeral) 용도로 설계되었다**는 점입니다. 그것들은 반드시 장기적인 인프라를 목적으로 만들어진 것은 아닙니다.

> 에이전트의 핵심 기능인 **하네스는 내구성이 뛰어난 서버에서 실행**되고, 실제 작업을 수행해야 할 때 **샌드박스를 생성**하여 (…) 완료되면 **삭제**하는 방식입니다. 이렇게 하면 샌드박스에 문제가 생기거나 연결이 끊어지더라도 **전체 에이전트가 다운되지 않습니다.**

즉 분할의 기준은 추상화 취향이 아니라 **수명 주기의 불일치**다 — 오래 사는 것(하네스)과 짧게 사는 것(샌드박스)을 같은 프로세스에 두면 후자의 실패가 전자를 죽인다. [[agent-distributed-systems]]의 부분 실패 격리 원칙이 제품에 구현된 형태.

## `outcomes` — 채점자를 프로비저닝하는 기능

같은 대담에서 밝혀진 기능. 사용자가 **루브릭**("좋은 결과는 이렇다")을 주면 플랫폼이 그것을 채점하는 **두 번째 에이전트를 프로비저닝**한다.

> 첫 번째 담당자가 시도해보고 (…) '좋아, 해봤는데 아직 충분하지 않네. 다시 해보자'라고 하는 거죠. (…) **채점자와 실행자가 함께** 일을 처리하기 때문이죠.

[[generator-evaluator-pattern]]을 플랫폼 기능으로 승격시킨 것이고, [[token-roles]]의 세 전략 중 grading에 해당한다. 노출되는 다른 제어 지점은 **시스템 프롬프트 · 스킬([[agent-skills]]) · [[model-context-protocol|MCP]] 연결**이다.

내부에서도 같은 이유로 쓴다고 밝힌다 — *"프롬프트 캐싱이나 컨텍스트 관리 같은 분야의 **최고 전문가라 할지라도 매번 똑같은 코드를 새로 작성하는 건 시간 낭비**"*.

## 디자인 원칙

- *Programs as yet unthought of*에 대비. 인터페이스만 opinionated, 구현은 swappable.
- [[pets-vs-cattle]] 분리: 컨테이너·harness 모두 cattle화.
- [[brain-hands-decoupling]] (이 글의 메인 모티프) → "many brains, many hands".

## 관련 — Dynamic workflows

[[claude-code|Claude Code]]의 [[dynamic-workflows|dynamic workflows]]는 동일 사상을 *제품 표면*에서 구현: **coordination이 대화 바깥**에서 돌고 진행상황이 **resumable checkpoint**로 저장됨 — 본 페이지의 session-log 외부화([[context-resets-and-compaction]]) 및 stateless harness 원칙과 동형. "many brains, many hands"가 한 세션의 10s~100s parallel subagent로 나타난 형태.

## References

- [[anthropic-managed-agents]]
- [[anthropic-dynamic-workflows]]
- [[tech-bridge-claude-platform-agent-era]] — 설계 이유·`outcomes`에 대한 팀 1차 진술
- [공식 문서](https://platform.claude.com/docs/en/managed-agents/overview)
