---
title: 지식 에이전트 vs 코딩 에이전트 (Knowledge Agents vs Coding Agents)
type: concept
category: framing
tags: [knowledge-work, agent-design, generalization, coding-agents]
aliases: [지식 에이전트, knowledge agents, 코딩은 특수 사례]
related: [knowledge-work-agent-gap, code-as-atypical-knowledge, orchestrator-searcher-split, tool-organization-loop, agent-org-adoption, workflow-vs-agent, assistance-vs-automation]
first-seen: tech-bridge-knowledge-agents-not-coding-agents
sources: [tech-bridge-knowledge-agents-not-coding-agents]
created: 2026-09-21
updated: 2026-09-21
---

# 지식 에이전트 vs 코딩 에이전트

**코딩 에이전트는 지식 노동의 특수 사례다. 거기서 일반화하면 틀린다.**

> **에이전트가 지식 기반 업무를 해야 한다**는 점에 대해 이야기하려고 합니다. 그러므로 **우리는 그들을 지식 근로자처럼 설계해야 합니다. 우리는 그것들을 코딩 에이전트가 아니라 지식 에이전트처럼 설계해야 합니다.** — [[benjamin-clavie]], [[tech-bridge-knowledge-agents-not-coding-agents]] (00:09~00:20)

화자 스스로 ***"조금 뜨거운 [hot take]"*** 이라 부른다(00:22~00:24).

## 지식 노동의 두 정의

소스가 두 가지를 나란히 놓고, **둘째를 스스로 동어반복이라고 인정한다.**

| | 정의 | 문장 |
|---|---|---|
| **①** | **입력이 정보이고 출력이 실행 가능한 판단** | *"주요 입력값은 정보입니다. (…) 주요 결과물은 실행 가능한 무언가입니다. 그것은 판단(judgment)입니다. 그것은 결정입니다"* (02:16~02:40) |
| **②** | **검색이 필요하면 지식 문제다** | *"탐색이 필요하다면 그것은 지식 문제이고, 지식 문제라면 탐색이 필요하다"* (02:56~03:00) |

①의 중간항이 중요하다 — **처리되는 정보는 "본질적으로 매우 모호하고 분산된(ambiguous, diffuse)"** 것이다(02:25~02:31). **모호함이 결함이 아니라 재료의 성질**로 놓인다.

②는 이 위키를 [[agentic-search]]와 바로 잇는다 — **지식 에이전트의 정의 안에 검색이 들어 있다.**

## 계보 — 세 단계

> **① 초기 에이전트들은 재미있는 잡다한 정보(fun trivia)를 제공해 주었죠.** (…) **2022년 당시** (…) **[RAG]밖에 없었고, 툴 콜조차 할 수 없었죠. 그저 `if` 문을 사용해서 검색하고, PDF와 대화하는 정도**였습니다. (00:26~00:43)

> **② 그 다음에는 프로그래밍 에이전트가 등장했고** (…) **이 자리에 있는 사람 중에 코딩 에이전트를 사용하지 않는 사람은 없을 겁니다.** (00:47~01:07)

> **③ 코딩 에이전트는 일종의 지식 노동이지만, 당시에는 에이전트가 지식 노동자가 아니었습니다.** (…) **하지만 이제 에이전트는 지식 노동자가 되어가고 있습니다.** (01:10~01:19)

그리고 범위를 넓힌다 — **변호사·재무·의약품 정보·자가 진단**이 전부 같은 범주다(01:28~01:44).

> 여기서 지식 노동자란 **지식 노동이라는 개념을 포괄적으로(superset) 의미하며, 우리가 생각해 본 모든 워크플로는 지식의 본질 때문에 일종의 지식 에이전트**라고 할 수 있습니다. (01:19~01:28)

## ⭐ 같은 현상, 두 개의 다른 원인 — [[knowledge-work-agent-gap]]과 나란히

**이 위키는 2026-09-09에 이미 같은 관측을 받았다.** [[karan-vaidya|Karan Vaidya]]([[composio|Composio]])의 [[knowledge-work-agent-gap]] — *"같은 모델이 코딩에서는 자율적으로 일하고 지원·영업·채용에서는 눈을 감고 일한다."* **진단이 다르다.**

| | [[knowledge-work-agent-gap]] (Vaidya, 09-09) | **이 페이지** (Clavié, 09-20) |
|---|---|---|
| 왜 코딩만 되나 | **인프라가 코딩 주변에만 깔려 있다** — 중앙화·히스토리·맥락·검증·거버넌스·가역성 **여섯 primitive** | **도메인과 과제 형태가 다르다** — 견고한 단서·`grep` 가능성·**그리고 사람이 이미 문제를 쪼개 준다** |
| 무엇을 지어야 하나 | **없는 primitive를 짓는다** (도구·권한·감사) | **조직을 짓는다** — 오케스트레이터/서처 분업 |
| 어디서 배우나 | 소프트웨어 엔지니어링의 인프라 | **인류의 지식 노동사** — 도서관·로펌·병원 |
| 화자의 인센티브 | ⚠️ 인프라를 판다 | ⚠️ 검색·에이전트를 판다 |

**둘은 배타적이지 않고 층이 다르다.** Vaidya는 *에이전트가 손댈 수 있는 세계가 없다*, Clavié는 *손댈 수 있어도 문제를 쪼개 주지 않으면 못 한다*. **겹쳐 읽으면 코딩 에이전트의 성공에는 세 겹의 보조바퀴가 있었다**: 인프라(Vaidya) · 도메인의 명시성([[code-as-atypical-knowledge]]) · **사람의 사전 분해**(이 소스의 가장 새로운 지적).

## 세 번째 겹이 이 위키에서 가장 새롭다

> 우리가 인지하지 못하는 사이에 **코딩 에이전트와 상호작용할 때, 에이전트에게 매우 [좁은] 작업만 부여하기 때문입니다. 우리는 에이전트에게 많은 것을 기대하지 않죠. 모든 것이 항상 특정 티켓의 기능이나 당면 과제에 관한 것입니다.** (04:24~04:41)

> **코드에서는, [Claude Code]를 사용할 때 여러분이 그 작업을 직접 하고 있습니다. 여러분은 이미 쿼리를 쪼개 놓았고, 무엇을 하고 싶은지 알고 있으며, [Linear] 티켓 같은 걸 가지고 있죠.** (12:06~12:19)

**이 위키의 위임 논의 전체가 이 문장 아래로 들어간다.** [[goal-level-delegation]]은 *지시 수준에서 목표 수준으로 올라갔다*고 기록했는데, **여기서는 그 "목표"조차 사람이 이미 한 번 쪼갠 결과**라고 말한다. [[plan-to-ticket-pipeline]]·[[sprint-contract]]·[[intent-md]]가 전부 **사람이 하는 분해 작업의 산출물**이다.

→ [[orchestrator-searcher-split]]이 그 분해를 **에이전트 안으로 옮기는** 처방이다.

## 이 위키의 다른 축들과

- [[assistance-vs-automation]] (09-19, [[diogo-almeida|Almeida]]) — **목적함수**로 가른다. 이 페이지는 **도메인**으로 가른다. **축이 다르고 겹칠 수 있다**: 지식 에이전트도 보조일 수 있다.
- [[workflow-vs-agent]] — *경로가 미리 정해져 있는가*. 역시 다른 축이다.
- [[agents-as-patient-specialists]] · [[agent-manager-analogy]] — **인간 조직 비유**를 쓴 선례. 다만 그쪽은 **관리**의 비유였고, 여기서는 **분업 구조 자체가 아키텍처**다.

## References

- [[tech-bridge-knowledge-agents-not-coding-agents]] · [[benjamin-clavie]] · [[mixedbread]]
- 하위: [[code-as-atypical-knowledge]] · [[tool-organization-loop]] · [[tools-are-not-neutral]] · [[orchestrator-searcher-split]] · [[oracle-gap]] · [[retrieval-primitive-repertoire]]
- 같은 현상 다른 진단: [[knowledge-work-agent-gap]] · [[agent-org-adoption]]
- 다른 축: [[assistance-vs-automation]] · [[workflow-vs-agent]] · [[goal-level-delegation]]
