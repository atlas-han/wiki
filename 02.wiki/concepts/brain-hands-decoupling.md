---
title: Brain–Hands Decoupling
type: concept
category: architecture
tags: [agent-infrastructure, decoupling, sandbox, harness]
related: [agent-harness-design, pets-vs-cattle, context-resets-and-compaction, sutton-bitter-lesson, model-context-protocol]
first-seen: anthropic-managed-agents
sources: [anthropic-managed-agents]
created: 2026-05-25
updated: 2026-05-25
---

# Brain–Hands Decoupling

LLM 에이전트 시스템을 **brain**(Claude + harness, 결정 주체)과 **hands**(sandbox·외부 도구, 실행 주체)로 분리하고, 둘이 좁은 인터페이스를 통해서만 통신하게 만드는 설계 원칙. [[anthropic-managed-agents]]의 메인 모티프.

## 단일 컨테이너 모델의 문제

초기 [[managed-agents|Managed Agents]]는 session·harness·sandbox를 한 컨테이너에 묶었다. 결과:

- 컨테이너가 죽으면 **세션 손실** — 컨테이너가 [[pets-vs-cattle|pet]]이 됨
- Hang 시 nursing 필요. 디버깅 채널이 WebSocket 이벤트뿐이라 harness 버그, 패킷 드롭, 컨테이너 offline이 *동일하게 보임*
- Customer VPC와 연결하려면 network peering 강요 — harness가 "리소스가 옆에 있다"는 가정을 인코딩

## 분리 후 구조

| 컴포넌트 | 인터페이스 | 특성 |
|---|---|---|
| **Brain** (Claude + harness) | session·sandbox에 외부 호출 | stateless, cattle |
| **Hand** (sandbox/tool) | `execute(name, input) → string` | cattle, swappable |
| **Session** | `emitEvent`, `getSession`, `getEvents` | durable, interrogable |

> The harness doesn't know whether the sandbox is a container, a phone, or a Pokémon emulator.

## 얻은 것

### 1. Cattle화
- 컨테이너 사망 = tool-call error로 변환 → Claude가 retry 결정. 새 컨테이너는 `provision({resources})`로 표준 recipe.
- Harness 크래시 = `wake(sessionId)` + `getSession(id)`로 마지막 event부터 resume.

### 2. TTFT 개선
"Brain in a container" 시절에는 모든 세션이 부팅 비용을 선불 — 컨테이너를 안 쓰는 세션도. 분리 후 brain은 **필요할 때만** 컨테이너를 provision.

- **p50 TTFT ~60% 감소**
- **p95 TTFT 90%+ 감소**

### 3. Security boundary
Token이 sandbox 안에 들어가지 않음:
- **Git**: clone 시 access token으로 wire-in, sandbox 안에서 push/pull 가능, agent는 token 자체를 안 만짐
- **커스텀 도구**: MCP + secure vault + dedicated proxy. Proxy가 session token으로 vault에서 자격증명을 가져와 외부 호출. **Harness는 자격증명을 절대 알지 못함.**

### 4. Many brains, many hands
- Hands가 brain과 coupling되어 있지 않으므로 brain끼리 hand를 주고받기 가능
- Brain이 stateless라 횡으로 무한 확장 가능
- Hand는 컨테이너든 폰이든 emulator든 동일 인터페이스

## OS 메타포

> Operating systems solved [programs as yet unthought of] by virtualizing hardware into abstractions— process, file —general enough for programs that didn't exist yet.

`read()`가 1970s 디스크팩과 모던 SSD에 똑같이 동작하듯, brain-hands 인터페이스도 구현보다 오래 산다.

## 관련 일반 패턴

- [[pets-vs-cattle]] — 인프라 일반 원칙의 LLM-agent 적용
- [[agent-harness-design]] — meta-harness로서의 Managed Agents

## References

- [[anthropic-managed-agents]]
- 외부: [TAOUP §3](http://www.catb.org/esr/writings/taoup/html/ch03s01.html), [The Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html)
