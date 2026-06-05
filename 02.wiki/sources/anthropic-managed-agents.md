---
title: "Anthropic — Scaling Managed Agents: Decoupling the brain from the hands"
type: source
tags: [managed-agents, meta-harness, infrastructure, sandbox, mcp, security]
source-url: https://www.anthropic.com/engineering/managed-agents
source-type: article
author: Lance Martin, Gabe Cemaj, Michael Cohen
date-published: 2026
ingested: 2026-05-25
created: 2026-05-25
updated: 2026-05-25
---

# Anthropic — Scaling Managed Agents: Decoupling the brain from the hands

[[anthropic|Anthropic]]의 **Managed Agents** — Claude Platform이 장기 horizon agent를 호스팅해주는 서비스 — 의 설계 철학을 정리한 글. 핵심 비유: 운영체제가 하드웨어를 `process`·`file` 같은 추상으로 가상화해서 **"programs as yet unthought of"** 에 대비한 것처럼, agent를 **session / harness / sandbox** 3개 인터페이스로 가상화한다.

## 핵심 takeaways

1. **Harness는 가정의 다발이고 가정은 stale해진다**. 예: [[claude-sonnet-4-5|Sonnet 4.5]]의 [[context-anxiety|context anxiety]]를 위해 추가했던 context reset이 [[claude-opus-4-5|Opus 4.5]]에서는 dead weight가 됐다. Bitter Lesson 인용. 메타-harness는 특정 harness를 강요하지 말아야 한다.
2. **OS-style 가상화 — 3개 추상**:
   - **Session** = 일어난 모든 일의 append-only 로그
   - **Harness** = Claude를 호출하고 tool call을 인프라로 라우팅하는 loop
   - **Sandbox** = 코드 실행·파일 편집 환경

   각각 독립적으로 fail/replace 가능. `read()`가 1970년대 디스크팩과 현대 SSD에 똑같이 동작하듯, 인터페이스가 구현보다 오래 산다.
3. **Pets → Cattle**. 초기에는 session·harness·sandbox를 한 컨테이너에 묶었다. 컨테이너가 죽으면 세션 손실, hang 시 nursing 필요, 디버깅 불가. 게다가 customer VPC 연결 시 network peering 강요. 참고: [[pets-vs-cattle]]
4. **Brain leaves the container**. Harness가 컨테이너 밖에서 `execute(name, input) → string`으로 컨테이너를 호출. 컨테이너 사망 = tool-call error로 변환되어 Claude에게 전달. 새 컨테이너는 표준 recipe로 `provision({resources})`.
5. **Harness도 cattle**. Session log가 harness 밖에 있으니, harness crash 시:
   - `wake(sessionId)`로 새 harness 부팅
   - `getSession(id)`로 event log 회복
   - 마지막 이벤트에서 resume
   - 진행 중에는 `emitEvent(id, event)`로 durable 기록
6. **Session ≠ Claude의 context window**. 장기 task는 context window를 초과한다. Compaction/trimming은 비가역적 결정. Managed Agents는 session을 **context object that lives outside the context window**로 둔다.
   - `getEvents()`로 positional slice (특정 시점 직전으로 rewind, 특정 액션 직전 재독 등)
   - Harness에서 fetched event를 자유롭게 transform (prompt cache 히트율 최적화 등)
   - *"session은 durable·interrogable만 보장, context engineering은 harness 영역."*
   참고: [[context-resets-and-compaction]], [[context-engineering]]
7. **Security boundary — token이 sandbox에 절대 없게**. 두 가지 패턴:
   - **Bundled with resource**: Git access token으로 sandbox init 시 repo clone + local remote에 wire. push/pull은 sandbox 내부에서 작동하지만 agent는 토큰을 결코 안 만진다.
   - **Vault + Proxy**: 커스텀 도구는 MCP로 묶고 OAuth token은 secure vault에 보관. Claude는 dedicated proxy를 통해 호출; proxy가 session token으로 vault에서 자격증명을 가져와 외부 호출.
   - **Harness는 자격증명을 절대 알지 못한다.**
8. **Many brains**. Brain을 컨테이너에서 빼면 컨테이너는 "필요할 때만" 띄운다. Sandbox를 안 쓰는 세션은 컨테이너 부팅 비용을 안 낸다. 결과: **p50 TTFT ~60% 감소, p95 TTFT 90%+ 감소**.
9. **Many hands**. 각 hand가 `execute(name, input) → string`이라는 동일 인터페이스. Sandbox이든 폰이든 Pokémon emulator이든 상관 없음. 어떤 hand도 brain에 coupling되어 있지 않아 brain끼리 hand를 주고받을 수 있음.
10. **Meta-harness 선언**. 인터페이스만 opinionated, *어떤 harness/sandbox가 들어올지*는 비opinionated. [[claude-code|Claude Code]] 같은 범용 harness, task-specific harness 모두 수용. 참고: [[brain-hands-decoupling]], [[agent-harness-design]]

## 핵심 인용

> A common thread across this work is that harnesses encode assumptions about what Claude can't do on its own. However, those assumptions need to be frequently questioned because they can go stale as models improve.

> If a container failed, the session was lost. If a container was unresponsive, we had to nurse it back to health.

> The harness is never made aware of any credentials.

> The harness doesn't know whether the sandbox is a container, a phone, or a Pokémon emulator.

> Meta-harness design means being opinionated about the interfaces around Claude.

## 인터페이스 시그니처 (블로그 인용)

| Surface | 호출 |
|---|---|
| Sandbox tool | `execute(name, input) → string` |
| Sandbox provision | `provision({resources})` |
| Session 이벤트 기록 | `emitEvent(id, event)` |
| Session 회복 | `getSession(id)`, `getEvents()` |
| Harness 복귀 | `wake(sessionId)` |

## 등장 개체·개념

- 조직: [[anthropic]]
- 제품: [[managed-agents]], [[claude-code]]
- 모델: [[claude-sonnet-4-5]], [[claude-opus-4-5]]
- 저자: Lance Martin, Gabe Cemaj, Michael Cohen
- 개념: [[agent-harness-design]], [[brain-hands-decoupling]], [[context-anxiety]], [[context-resets-and-compaction]], [[context-engineering]], [[pets-vs-cattle]]

## References

- [원문](https://www.anthropic.com/engineering/managed-agents)
- 외부 참고: [Building Effective Agents](https://www.anthropic.com/research/building-effective-agents), [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents), [The Bitter Lesson (Sutton)](http://www.incompleteideas.net/IncIdeas/BitterLesson.html), [TAOUP §3](http://www.catb.org/esr/writings/taoup/html/ch03s01.html), [Pets vs Cattle (Cloudscaling)](https://cloudscaling.com/blog/cloud-computing/the-history-of-pets-vs-cattle/)
- 시리즈: [[anthropic-claude-code-auto-mode]], [[anthropic-harness-design-long-running-apps]]
