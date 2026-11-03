---
title: "Fork 서브에이전트 (Fork Subagent) — 대화 전체를 물려받는 서브에이전트 vs 과제만 받는 서브에이전트"
type: concept
category: pattern
tags: [subagents, context-inheritance, prompt-caching, background-agents, claude-code, delegation, token-cost]
aliases: [fork subagent, fork sub-agent, fork 서브에이전트, 포크 서브에이전트, forked subagent, fresh subagent, 대화 상속 서브에이전트]
related: [subagent-vs-thread-handoff, subagent-folding, prompt-caching, hidden-harness-calls, context-engineering, orchestrator-searcher-split, generator-evaluator-pattern]
first-seen: tech-bridge-better-stack-claude-code-agent-summary-cost
sources: [tech-bridge-better-stack-claude-code-agent-summary-cost]
created: 2026-11-03
updated: 2026-11-03
---

# Fork 서브에이전트 (Fork Subagent)

**서브에이전트를 띄울 때 부모의 대화 전체(와 그 prompt cache)를 복사해 주느냐, 부모가 건넨 과제만 주고 빈 컨텍스트에서 시작하게 하느냐의 구분.** [[claude-code|Claude Code]]에는 두 종류가 함께 있고, 앞의 것을 fork 서브에이전트라 부른다(화자 설명). [[tech-bridge-better-stack-claude-code-agent-summary-cost]]에서 agent summary 비용을 없애는 우회의 **대가**로 처음 나왔다.

> *"you lose fork sub agents, which are the ones that inherit your whole conversation. So, to be clear, you don't lose background agents. Claude can still spin up normal sub aents[=subagents] in the background. They just start fresh with only the task that Claude hands them instead of full copy of your conversation before it and its prompt cache."*(03:36~03:51)

## 두 종류 (화자 설명)

| | fork 서브에이전트 | 일반(fresh) 서브에이전트 |
|---|---|---|
| 시작 컨텍스트 | 부모 대화 전체의 사본 | 부모가 건넨 과제만 |
| prompt cache | 부모의 캐시를 물려받음 | 새로 시작 |
| 백그라운드 실행 | 가능 | 가능 — fork를 꺼도 남는다(03:30~03:34) |
| 숨은 비용 | ⚠️ agent summary가 함께 사라졌다(화자 실험) | — |

## 끄기와 그 절충

- 설정: *"the setting claude code fork sub agents. If you set this to zero, it disables fork sub agents and so the summaries go with them."*(03:22~03:28) — ⚠️ 정확한 이름 · 형식(환경 변수인지 settings 키인지)은 발화되지 않았다.
- 화자 재실행: *"agent summary did go to zero while the agents still ran in the background."*(03:30~03:34) → [[hidden-harness-calls]]
- 절충: *"So, there could be some trade-off when using this approach."*(03:51~03:53) — 화자는 무엇을 잃는지 구체 사례를 들지 않는다. 문맥상 잃는 것은 (1) 부모가 이미 쌓은 맥락, (2) 그 맥락의 캐시 적중이다(추정).

> ⚠️ **왜 fork를 끄면 요약까지 사라지는지는 설명되지 않는다.** 화자 관찰은 "그렇게 됐다"뿐이다. 요약 기능이 fork 메커니즘 위에서 구현돼 있다는 추정은 가능하지만 위키는 확인하지 않았다.

## 이 위키에서의 자리 — 상속은 장점이자 약점

- **상속이 약점인 쪽**: 리뷰 · 검증 서브에이전트는 일부러 맥락을 끊는다. [[generator-evaluator-pattern]]의 AI Labs review-loop는 *fresh context windows* 로 *"so they don't just agree with what the main agent did"*, [[code-blind-first-user-test]]는 코드 읽기까지 막는다. fork는 정반대 — 부모와 같은 판단을 물려받는다.
- **상속이 장점인 쪽**: 같은 맥락을 다시 설명하지 않아도 되고, 캐시된 접두를 그대로 쓴다 → [[prompt-caching]]. 부모와 같은 상태에서 다른 일을 병렬로 하려는 경우에 맞는다(추정).
- [[subagent-vs-thread-handoff]]가 위임을 **누구에게 보이게 할지**의 축이라면, 이 구분은 위임에 **무엇을 들려 보낼지**의 축이다. [[subagent-folding]]의 "서브에이전트를 남길 세 경우" 논의에도 같은 질문(맥락 격리가 필요한가)이 숨어 있다.

## ⚠️ 유보

- 출처는 화자 한 명의 설명 · 1회 실험이다. Claude Code 공식 문서와 대조하지 않았다.
- fork와 fresh의 품질 · 비용 차이를 잰 측정은 없다.

## References

- [[tech-bridge-better-stack-claude-code-agent-summary-cost]] — first-seen
- [[hidden-harness-calls]] · [[subagent-vs-thread-handoff]] · [[prompt-caching]] · [[claude-code]]
