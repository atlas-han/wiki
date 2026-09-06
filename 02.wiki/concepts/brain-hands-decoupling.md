---
title: Brain–Hands Decoupling
type: concept
category: architecture
tags: [agent-infrastructure, decoupling, sandbox, harness]
related: [agent-harness-design, pets-vs-cattle, context-resets-and-compaction, sutton-bitter-lesson, model-context-protocol, intelligence-as-infrastructure]
first-seen: anthropic-managed-agents
sources: [anthropic-managed-agents, tech-bridge-jensen-huang-g20-agi, tech-bridge-altman-astra-hardware]
created: 2026-05-25
updated: 2026-09-06
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

## hands가 몸이 된다 — 피지컬 AI (2026-09-06)

이 페이지의 *"The harness doesn't know whether the sandbox is a container, a phone, or a Pokémon emulator"* 가 같은 날 두 CEO에게서 **문자 그대로**의 뜻을 얻었다.

[[jensen-huang|Jensen Huang]] ([[tech-bridge-jensen-huang-g20-agi]]):

> 이 에이전트는 **물리적인 몸체 안에 구현**되어 갑자기 **로봇**이 되는 것입니다. 바퀴 네 개가 달린 자율주행차 (…) 매니퓰레이터 안에 넣으면 로봇 팔 (…) 수술 로봇 또는 자율형 신약 개발 연구실. 이 모든 다른 버전들은 기본적으로 **같은 아이디어**를 담고 있습니다. **에이전트 시스템을 갖춘 대규모 언어 모델.** 이 에이전트 시스템은 **디지털 도구든 물리적 도구든** 상관없이 작동할 수 있습니다.

[[sam-altman|Sam Altman]] ([[tech-bridge-altman-astra-hardware]]):

> 휴머노이드 로봇은 확실히 만들 겁니다. (…) 하지만 무엇보다 중요한 건 **로봇을 작동시키는 두뇌**를 개발하는 거라고 생각합니다.

| | 이 페이지 (Managed Agents) | Huang / Altman |
|---|---|---|
| brain | Claude + harness | LLM + 에이전트 하네스(외골격) |
| hands | 컨테이너·폰·에뮬레이터 | 로봇 팔·자율주행차·수술 로봇·**휴머노이드** |
| 인터페이스 | `execute(name, input) → string` | *"디지털 도구든 물리적 도구든"* — 소스에 명세 없음 |

**같은 분리 원칙의 물리 세계 확장**이고, 두 사람 모두 우선순위를 **brain**에 둔다. 다른 점은 hands의 실패 모드다 — 컨테이너가 죽으면 tool-call error로 변환해 재시도하면 되지만, 로봇 팔의 실패는 [[agent-distributed-systems]]가 말한 *"부작용은 되돌릴 수 없다"* 가 물리적으로 참이 된다. 소스는 이 문제를 다루지 않는다.

⚠️ 둘 다 제품 발표에 가까운 진술이고 아키텍처 세부는 없다.

## References

- [[anthropic-managed-agents]]
- 외부: [TAOUP §3](http://www.catb.org/esr/writings/taoup/html/ch03s01.html), [The Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html)
- [[tech-bridge-jensen-huang-g20-agi]] · [[tech-bridge-altman-astra-hardware]] — 피지컬 AI (2026-09-06)
