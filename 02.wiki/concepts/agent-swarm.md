---
title: 에이전트 스웜 (Agent Swarm)
type: concept
category: pattern
tags: [parallelism, sub-agents, context-window, pstack, aggregation]
aliases: [swarm, 겁 없는 병렬성, fearless parallelism]
related: [agent-arena, dynamic-workflows, sweeper-agent, context-engineering, multiplayer-agent-context]
first-seen: tech-bridge-pstack-third-party-review
sources: [tech-bridge-pstack-third-party-review]
created: 2026-09-14
updated: 2026-09-14
---

# 에이전트 스웜

**문제를 조각내 병렬 작업자에게 나눠 주고, 결과를 하나의 종합 보고서로 다시 끌어모으는 패턴.** [[pstack|Pstack]]의 스킬 중 하나로 [[tech-bridge-pstack-third-party-review]]에서 관찰된다.

> **역시 병렬 작업자인데, 이번에는 **문제의 서로 다른 조각**을 각자에게 주고 결과를 **하나의 종합 보고서**로 다시 끌어모읍니다.** (03:04~03:14)

[[agent-arena|아레나]]가 *같은 문제에 여럿* 이라면 스웜은 *쪼갠 문제에 여럿* 이다.

## 겁 없는 병렬성

이 패턴에 붙은 약속이 이 소스의 가장 큰 주장이다.

> **Pstack은 "겁 없는 병렬성(fearless parallelism)"을 얻도록 설계돼 있습니다.** 피처 브랜치·워크트리를 오가며 작업하더라도 **아레나나 스웜을 쓰고 있어도 작업 전부를 한데 모아 겹침이 없게 관리합니다.** (03:14~03:26)

> ⚠️ **리뷰어 본인이 곧바로 유보한다** — *"뭐, 원칙적으로는 그렇다는 얘기고 — **대담한 주장**입니다. 제가 **충분히 써 보지 않아서 실제로 그런지는 확신할 수 없습니다.**"*(03:26~03:33) **이 위키는 이것을 설계 의도로만 기록한다.**

*"fearless"* 라는 단어 선택은 Rust 커뮤니티의 *fearless concurrency* 를 그대로 따온 것으로 읽히지만 **소스가 그렇게 말하지는 않는다.**

## 컨텍스트 창과의 관계

스웜의 근거는 Pstack의 일곱 번째 원칙에 있다.

> **컨텍스트 창을 지키고, 사람을 절대 막지 마라.** (…) **중앙 컨텍스트 창이 핵심입니다. 어떻게 작업의 조각을 서브에이전트에게 넘길 것인가? 그들은 자기 고유의 컨텍스트 창을 갖고 일한 뒤 중앙 스레드로 보고합니다.** (10:28~10:44)

→ [[context-engineering]] · [[context-resets-and-compaction]]

**스웜은 병렬화 기법이기 전에 컨텍스트 예산 관리 기법이다.** 이 위키의 [[harness-pruning]]·[[context-anxiety]]가 *한 스레드 안에서* 다루던 문제를, **여러 스레드로 나눠** 푼다.

09-03 [[tech-bridge-claude-code-team-workflow|Claude Code 팀]]이 *fan-out의 reduce 병목* 을 지적한 것이 그대로 남는다 — **조각을 모으는 쪽이 다시 중앙 컨텍스트에 들어온다.** 소스는 이 문제를 다루지 않는다.

## 열려 있는 것

- ⚠️ **조각을 나누는 규칙이 없다.** 누가, 무엇을 기준으로 쪼개는지 소스에 없다.
- ⚠️ **겹침 방지의 메커니즘이 없다.** *"한데 모아 겹침이 없게 관리한다"* 는 주장뿐이고 **어떻게** 가 없다.
- ⚠️ **reduce 단계의 비용**(집계 보고서가 중앙 컨텍스트를 얼마나 먹는지)이 논의되지 않는다.
- ⚠️ **실패 처리가 없다.** 한 작업자가 실패하거나 환각하면 어떻게 되는지.

## References

- [[tech-bridge-pstack-third-party-review]] · [[pstack]] · [[lauren-tan]]
- 관련: [[agent-arena]] · [[context-engineering]] · [[context-resets-and-compaction]] · [[harness-pruning]] · [[dynamic-workflows]] · [[sweeper-agent]] · [[multiplayer-agent-context]]
