---
title: Managed Agents
type: entity
category: product
tags: [anthropic, agent-infrastructure, meta-harness, claude-platform]
aliases: [Claude Managed Agents]
sources: [anthropic-managed-agents, anthropic-dynamic-workflows, tech-bridge-claude-platform-agent-era, tech-bridge-tokens-should-have-jobs, tech-bridge-anthropic-dreaming-memory, tech-bridge-claude-managed-agents-workshop-1, tech-bridge-claude-managed-agents-workshop-2]
links:
  - "https://platform.claude.com/docs/en/managed-agents/overview"
created: 2026-05-25
updated: 2026-10-19
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
  - ⚠️ 팀 리드의 워크숍 발화는 *"bring down the time to first token by about 90%"*(백분위 없음)다 → [[tech-bridge-claude-managed-agents-workshop-1]]. 위 p50/p95 표기를 유지한다.
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
- [[tech-bridge-claude-managed-agents-workshop-1]] — 팀 리드의 워크숍 구두 판본·API 객체 넷
- [[tech-bridge-claude-managed-agents-workshop-2]] — 워크숍 2부: 리소스 모델·Vault·Outcome·아직 없는 것 넷
- [공식 문서](https://platform.claude.com/docs/en/managed-agents/overview)

## 메타 하네스 층 — 회고와 `outcomes`가 기본 제공 (2026-09-18 · [[tech-bridge-tokens-should-have-jobs]])

[[angela-jiang]]이 [[ai-engineer|AI Engineer]] 발표에서 이 제품의 **층 구조**를 준다.

> 저희는 **개별 에이전트를 위한 정말 훌륭한 하네스**를 만들기 위해 많은 노력을 기울였습니다. (…) 이것이 바로 저희가 **Claude Managed Agents**에 사용한 아키텍처입니다. (10:35~10:48)

> 그리고 우리는 이 위에 더 나아가 **메타 하네스 수준, 즉 다중 에이전트 오케스트레이션 및 실행 수준**으로 진입하여 (…) **회고(dreaming)와 `outcomes`는 Claude Managed Agents에서 기본적으로 제공**됩니다. (10:52~11:12)

| 층 | 이 페이지의 기존 항목 | 이번에 더해진 것 |
|---|---|---|
| 하네스 (개별 에이전트) | session / harness / sandbox, `execute`/`provision`/`emitEvent` | *"개별 에이전트를 위한 하네스"* 로 확인 |
| **메타 하네스** (역할 간 조정) | 09-01의 *"어떤 사람들은 메타 하네스라 부른다"* (말) | **제품 층** — 실행자·조언자·채점자·드리머 조정 |
| 기본 제공 전략 | `outcomes` (= grading, 09-01) | **+ 회고(dreaming)** |

→ [[strategy-primitives]]. *"이러한 것들 중 **일부**"* 라고 하므로 **조언(advising)이 기본 제공인지는 소스가 말하지 않는다.** ⚠️ 화면의 아키텍처 그림은 자막에 없다. ⚠️ ko가 *Claude Managed Agents* 를 **"클라우드 관리형 에이전트"** 로, *outcomes* 를 **"결과"** 로 옮겼다 — 설명란(*"Claude Managed Agents 아키텍처"*)으로 판독.

장기 목표도 이 제품에 걸린다 — *"여러분이 업무를 수행하는 동안 이러한 전략을 동적으로 구성할 수 있도록 모델과 플랫폼을 더욱 개선"*(12:16~12:23). [[dynamic-workflows]]·[[self-harness]]와 같은 방향의 **선언**이고 실체는 없다.

## memory and dreaming API — 응용 AI 팀의 설명 (2026-10-01 · [[tech-bridge-anthropic-dreaming-memory]])

[[lamis-mukta|Lamis Mukta]](Anthropic 응용 AI 팀)가 Q&A에서 메모리 스토어 구현을 묻는 질문에 이 제품을 가리킨다 — *"we're not allowed to make product call to actions but given that you asked"*(27:51~27:55):

> *"a lot of this references the architecture that we used in our memory uh our memory infrastructure for our managed agent solutions and so when I talk about these things about productionizing um memory so everything like versioning uh hashing etc that's all available within our memory in[=and] dreaming API through claude manage[=Managed] agents"* (27:59~28:21)

- 09-18의 *"회고(dreaming)는 기본 제공"* 과 일치한다. 이번에 더해진 것은 **메모리 쪽 보장** — 버전 관리·해시 기반 동시성(→ [[production-memory-guardrails]])과 dreaming의 구조(→ [[agent-dreaming]]).
- dreaming 권한: *"when you set up a dreaming procedure you decide exactly which session transcripts to attach"*(29:20~29:25).
- ⚠️ API 이름은 ASR(*"memory in dreaming API"*)과 설명란(*"Memory & Dreaming API"*)으로 판독. ko·`en`은 둘 다 **"스트리밍 API … 클라우드 관리형 에이전트"** 로 깨졌다. 엔드포인트·사용법은 발화되지 않았다(설명란의 "실전 적용 가이드"는 자막에 없다).

## 워크숍 1부 — 만든 팀이 말하는 진화와 API 객체 넷 (2026-10-19 · [[tech-bridge-claude-managed-agents-workshop-1]])

[[priyanka-phatak|Priyanka Phatak]](엔지니어링 팀 리드)와 [[gabe-cemaj|Gabe Cemaj]]의 [[ai-engineer|AI Engineer]] 워크숍 1부. 설계 서술은 [[anthropic-managed-agents]]와 대부분 같다. 새로 나온 것은 셋이다.

- **첫 아키텍처의 시점과 실패 이유.** *"This was in December of last year where we shipped our first architecture to our early access customers, got a bunch of feedback, and then actually pivoted"*(04:32~04:42). 실패 이유는 장애가 구분되지 않음(*"a dropped packet, a dead container would show up very similarly"* 06:18~06:22), 고객 데이터 때문에 들어갈 수 없음(*"customer data would live on these containers"* 06:33~06:36), VPC peering이다. [[katelyn-lesse]]의 *수명 주기 불일치*와 같은 결정의 다른 면이다. ⚠️ 연도 미발화.
- **API 객체 넷**(발화 표기 그대로, 문서 미대조):

| 객체 | 설정 |
|---|---|
| environment (*"V1 environments"*) | sandbox 템플릿 — 네트워킹(무제한 / 도메인·MCP 제한), 설치 패키지 |
| agent | 이름, 모델(Opus·Haiku·Sonnet), 시스템 프롬프트, 도구(*"agent tool set"* = bash·read·write·grep 등) |
| session | agent ID + environment ID. *"task unit of work"*. 이벤트를 받기 전에는 idle |
| events | *"user.message"*, custom tool use → custom tool result(사용자가 처리), *"session.error"*, status idle, interrupt |

- **custom tool의 흐름.** Claude가 custom tool use 이벤트를 스트림에 올리고, 사용자가 처리해 custom tool result로 돌려준다(13:09~13:25). 도구 실행이 **사용자 쪽 hands**가 되는 자리다 → [[brain-hands-decoupling]].

> ⚠️ **Contradiction(표현): TTFT.** 위 *"p50 TTFT ~60%↓, p95 90%+↓"*(글)와 달리 발화는 *"about 90%"*(09:43~09:47)이고 백분위가 없다.

⚠️ ko는 harness를 "테스트 환경"·"환경"으로, Claude를 "클라우드"로 옮긴다. 1부는 콘솔 Quick Start 직전에 끊기고 다중 에이전트·메모리는 2부([[tech-bridge-claude-managed-agents-workshop-2]])로 넘어간다.

## 워크숍 2부 — 만지는 단위와 아직 없는 것 넷 (2026-10-19 · [[tech-bridge-claude-managed-agents-workshop-2]])

같은 팀의 워크숍 2부(핸즈온·Q&A). *"All you have to do is start a session with the agent, send events, get back events. Everything else is managed by us."*(03:00~03:05) — 관리 범위는 *"the infrastructure, the hosting, the harness, the sandbox management, the scaling, the storage of your event log"*(03:07~03:14).

| 단위 | 워크숍에서 나온 것 |
|---|---|
| **agent** | 프롬프트·모델·도구·스킬·하위 에이전트. 설명을 바꾸면 *"a new version of that agent"*(14:53~14:55). 콘솔 Quick Start는 *"V1 agents endpoint"*(01:44~01:47)를 부른다 |
| **environment** | *"the template for the sandbox"*. 네트워크는 unrestricted 또는 도메인·MCP 서버 허용 목록(02:10~02:18). 패키지는 *"creation time and then we'll cache it"*(34:27~34:36), NPM·Cargo·pip만(내부 패키지는 파일·GitHub 저장소 업로드로) |
| **session** | 이벤트 스트림 — `user.message`를 보내고 SSE로 받는다(11:54~12:43). 실행 중 `user.message`로 조종, 큐잉(*"like 10 messages at a time"* 28:27~28:31) |
| **skill** | *"live artifacts"* — 갱신은 그 스킬을 참조하는 **새 세션**에 전파(22:30~22:46) |
| **sub-agent** | 자체 프롬프트·도구·권한. **자기 참조** 가능 — 트랜스크립트는 복사하지 않고 프롬프트·도구·스키마만(15:37~15:47). 콘솔에서 thread 하나 = 하위 에이전트 작업 하나 |
| **custom tool** | 클라이언트 쪽 오케스트레이션 훅(dispatch analysis → 세션 N개, 이 편에서는 미시연) |
| **memory store** | 세션 간 공유, 세션당 여러 개(사용자 + 조직), API로 반출 |
| **outcome** | 과제 + 루브릭 + max iterations → 채점 하위 에이전트, 실패 시 재시도. 세션 수준만 |
| **vault** | 비밀은 env에 placeholder로, egress에서 허용 도메인에만 진짜 값으로. MCP auth·OAuth 묶음 |

실행 위치: Anthropic 1P · Claude Platform on AWS(⚠️ en-orig *"cloud platform on AWS"* 판독) · 자체 호스팅 샌드박스(Vercel·Modal·Daytona·Google Cloud·AWS). 비공개 데이터는 MCP + vault, **MCP tunnels**, 고객 네트워크에 peer한 자체 호스팅 샌드박스(33:22~34:12).

**아직 없는 것**(워크숍 시점, 팀 진술):
1. 세션당 돈·토큰 상한 — *"we are exploring (…) but that's not something we offer today"*(27:33~27:44). 반복 폭주 방지는 *"we leave up to you"*. → [[fixed-budget-alpha]]
2. rewind / roll forward — 없음(28:31~28:36). session forking은 로드맵(28:40~28:48).
3. 메모리 밖 dreaming — *"Today the dreaming's constrained to memory stores"*(32:21~32:24). 아래 Contradiction.
4. 외부 메모리 공급자 — *"We don't currently support out of the box other memory providers in the session"*(30:40~30:44). MCP·맞춤 도구로.
(+ sub-outcome 정의 없음 31:59~32:06)

하네스: *"we have our own harness that's heavily inspired by Cloud[=Claude] Code's harness"*(26:48~26:52), Agent SDK의 *"sort of a fork"*. → [[claude-agent-sdk]] · [[agent-harness-design]]

> ⚠️ Contradiction(약): 이 페이지의 *"[[claude-code|Claude Code]] 같은 범용 harness, task-specific harness 모두 수용"*(엔지니어링 글 기반)과 달리, 워크숍은 **호스팅 하네스 하나**를 말하고 사용자의 *"custom harness"*는 맞춤 도구로 세션들을 바깥에서 조율하는 층이다. 글은 설계 원칙, 워크숍은 현재 제품.

> ⚠️ Contradiction: dreaming의 출력. 09-01([[tech-bridge-claude-platform-agent-era]])은 *"메모리에 쓰고 스킬을 작성"*, 워크숍은 메모리 스토어 전용이고 스킬·프롬프트·에이전트 정의는 *"you can imagine that we can continue to expand"*(미래형). → [[agent-dreaming]]

⚠️ 벤더 당사자 워크숍. *"hours, days, weeks, and even months"*(13:14~13:18)는 근거 없음. Nvidia 데모는 사전 실행분이고 결과 수치 없음. deployments API·map-reduce·dreaming 시연은 3/4·4/4 대기.
