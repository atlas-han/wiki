---
title: Agent Memory
type: concept
category: pattern
tags: [memory, agent, experience, retrieval, cache]
aliases: [에이전트 메모리, Memory]
related: [retrieval-augmented-generation, agent-knowledge-sourcing, context-engineering, agent-distributed-systems, skill-self-improvement, no-silent-write, company-brain, sweeper-agent]
first-seen: tech-bridge-agent-knowledge-four-ways
sources: [tech-bridge-agent-knowledge-four-ways, tech-bridge-agents-as-distributed-systems, anthropic-managed-agents, tech-bridge-knowledge-work-agent-infrastructure, tech-bridge-cursor-legacy-refactoring, tech-bridge-company-brain-security, tech-bridge-agent-to-agent-as-search]
created: 2026-09-08
updated: 2026-09-10
---

# Agent Memory

**에이전트가 스스로 겪고 저장한 경험**을 나중에 다시 쓰는 것. [[retrieval-augmented-generation|RAG]]와 메커니즘이 아니라 **출처**로 갈린다.

> **메모리란 에이전트가 스스로 수집하고 이전에 발생했던 일들을 나중에 사용하기 위해 저장해 둔 정보**입니다. — [[tech-bridge-agent-knowledge-four-ways]]

## 읽기와 쓰기의 순환

[[tech-bridge-agent-knowledge-four-ways]]의 500 에러 예제가 한 바퀴를 다 보여준다.

**읽기** — 지난번의 진짜 원인:

> 지난번에 똑같은 오류가 발생했을 때, **실제 원인은 여기 런북에 기록되지 않은 내용**이었을 수도 있습니다. 그리고 그 문제는 어쩔 수 없이 **어려운 과정을 거쳐 해결**해야 했습니다. 음, **그 기억은 우리에게 그 힘든 길이 무엇이었는지 알려줄 수 있죠.**

**쓰기** — 이번의 수정:

> 이 성가신 500 오류가 마침내 해결되면, 메모리는 **실제로 어떤 수정 사항이었는지도 기록**할 수 있습니다. 그래서 에이전트는 **다음번에 그 정보를 활용**할 수 있습니다. 그러니까 기본적으로 **경험이 에이전트의 기억 속에 축적되는 겁니다.**

**메모리가 값진 순간은 문서가 틀렸을 때**라는 점이 예제에 내장돼 있다 — 런북에 없던 것이 진짜 원인이었다. 이는 [[retrieval-augmented-generation|RAG]]의 보완재가 아니라 **경쟁 정보원**이 될 수 있다는 뜻이다.

## 이 위키의 다른 메모리 논의와의 관계

세 소스가 메모리를 서로 다른 층에서 본다.

| 소스 | 메모리를 무엇으로 보는가 |
|---|---|
| [[tech-bridge-agent-knowledge-four-ways]] | **지식의 한 출처** — 사람이 적은 것(RAG)과 대비되는 *겪은 것* |
| [[tech-bridge-agents-as-distributed-systems]] ([[agent-distributed-systems]]) | **무효화 가능한 캐시** — 낡으면 틀린다 |
| [[anthropic-managed-agents]] ([[context-engineering]]) | **memory tool** — 컨텍스트를 파일에 써서 세션 간 학습 |

**둘째 관점이 첫째의 빈 자리를 정확히 찌른다.** 경험을 축적하는 것이 좋다는 첫 소스의 서술에는 *언제 그 경험이 더 이상 참이 아닌가*가 없다. 500 에러의 원인이 **인프라가 바뀌어 달라졌다면**, 저장된 기억은 도움이 아니라 오답의 근거가 된다.

## [[skill-self-improvement]]와의 대비 — 사람 게이트의 유무

[[tech-bridge-six-agent-skills]]의 `task-observer`도 실패에서 배워 저장한다. 다른 것은 **승격 경로**다.

| | task-observer ([[skill-self-improvement]]) | 이 페이지의 메모리 |
|---|---|---|
| 무엇이 쌓이나 | 교훈 → `log.md` | 경험 → 메모리 저장소 |
| 반영 | **사람이 검토한 뒤** 스킬·규칙으로 승격 | **에이전트가 직접 쓰고 직접 읽는다** |
| 이유 | *"하나의 잘못된 결과가 (…) 영원히 따르는 규칙으로 자동 설정되는 것을 방지"* | (소스가 이 문제를 제기하지 않는다) |

즉 **자동 축적의 위험을 한쪽 소스는 설계로 다루고 다른 쪽은 다루지 않는다.** [[tech-bridge-agent-knowledge-four-ways]]가 메모리를 좋은 것으로만 그리는 대목은 이 대비 없이 읽으면 안 된다.

## 미해결 사항

- **무엇을 저장할지 누가 정하는가.** 소스에 없다.
- **틀린 기억**의 처리 — 검증·정정·삭제.
- **무효화** — [[agent-distributed-systems]]가 제기했고 [[tech-bridge-agent-knowledge-four-ways]]는 침묵한다.
- **RAG와 충돌할 때의 우선순위** → [[retrieval-augmented-generation]]의 같은 항목.
- 저장 형식·범위(세션/프로젝트/조직)와 여러 에이전트 간 공유.

## 조직 규모와 잡 규모 — 두 가지 새 형태 (2026-09-08)

이날 들어온 두 소스가 이 페이지에 서로 다른 크기의 메모리를 하나씩 더한다.

**① 조직 규모 — 행동 기록** ([[tech-bridge-knowledge-work-agent-infrastructure]])

모든 앱에 걸친 에이전트 행동을 한곳에 로깅하면 그 로그가 곧 메모리가 된다.

> 이를 통해 첫째, **에이전트가 기억을 얻습니다.** 비슷한 작업이 전에 어떻게 되었는지, 무엇이 성공적이었는지 되돌아보고 다시 재현할 수 있습니다.

지식 노동에서 이것이 없을 때의 상태가 명시된다 — *"에이전트에게는 기억이 없습니다. 거의 매번 백지 상태에서 시작합니다."* → [[agent-action-record]]. 여기서 메모리는 **개인이 아니라 조직 단위로 집계되고 세 층위**(도구 일반 / 회사 / 개인)를 갖는다.

**② 잡 규모 — `memories.md`** ([[tech-bridge-cursor-legacy-refactoring]])

[[cursor-cloud|Cursor]]의 automation은 각각 **`memories.md` 파일**을 갖는다.

> 이것이 automation이 **실행할 때마다 더 나아지는 방법**입니다. 무언가를 놓쳤거나 *"Slack에 이렇게 표현한 게 마음에 안 들었어"* 라고 후속으로 말해야 했다면 **그 피드백에서 배우고 다음 실행마다 더 나아집니다.**

이 위키가 본 메모리 구현 중 **반복 실행되는 잡에 귀속된 것은 처음**이다 — 사용자에게도 세션에도 아니고 *스케줄된 작업* 에 붙는다. → [[scheduled-agent-automations]] · [[skill-self-improvement]]

같은 소스가 팀 학습용 **`continual learning` 플러그인**도 언급한다 — `AGENTS.md`에 작업·글쓰기·코딩 스타일을 축적하며 **팀 플러그인 또는 개인 플러그인**으로 범위를 고를 수 있다.

> ⚠️ 어느 쪽도 **잘못 학습했을 때의 정정 경로**를 제시하지 않는다. 무효화·망각 정책은 이 위키의 어떤 소스에서도 아직 다뤄지지 않았다.

## 자동 저장의 조직적 실패와 첫 정정 실패 사례 (2026-09-10)

2026-09-09 업로드 두 소스가 이 페이지의 미해결 항목 둘에 각각 답과 사례를 준다.

**"무엇을 저장할지 누가 정하는가"** — [[tech-bridge-company-brain-security]]가 답을 놓는다: **에이전트가 제안, 사람이 이름을 걸고 결정.** 그 근거는 자동 저장이 조직에서 두 가지로 실패한다는 관찰이다.

> [팀 에이전트가 메모리를 자동 저장하면] 여전히 격리돼 있어서 회사 두뇌가 아니라는 겁니다. **사일로가 하나 더** 생긴 거죠. 예를 들어 Claude Tag는 **채널당 메모리**가 있어요. (…) 이제 그 한 채널의 또 다른 사일로입니다.

> 자동 추가하게 두면 **무슨 일이 있었는지 전혀 알 수 없습니다.** (…) **그 에이전트의 메모리 안에 있으면 운이 좋은** 세계.

→ [[no-silent-write]]. 이 페이지가 [[skill-self-improvement]]와 대비해 *자동 축적의 위험을 한쪽만 설계로 다룬다* 고 적은 자리에, **조직 규모에서는 자동 축적 자체를 금지**하는 소스가 들어왔다. 그리고 [[claude-tag]]의 채널당 메모리는 이 위키가 그 제품에 대해 아는 첫 **메모리 구조** 사실이다.

**"틀린 기억의 처리"** — [[tech-bridge-agent-to-agent-as-search]]가 **첫 실사례**를 준다.

> 제 개인 위키는 제 에이전트 이름을 지금 **Apex**로 알고 있는데, 한 달 전에 **Ivy**로 바꿨어요. 제 설정의 메모리 뱅크 어딘가에 Apex가 살아 있어서 **없앨 수가 없습니다.** Apex야 괜찮고 웃긴 얘기지만, **사업에 대한 정말 틀린 정보라면 훨씬 어렵습니다.**

*"영원히 오염된다"* 는 표현이 붙는다. 이 페이지가 미해결로 둔 무효화·정정이 **왜 어려운지**의 구체 — 어디에 남았는지 모른다 — 가 처음 기록됐다. ⚠️ 여전히 해법은 어느 소스에도 없다.

같은 소스의 [[sweeper-agent|청소부 에이전트]]는 이 페이지의 *여러 에이전트 간 공유* 항목에 대한 첫 구체적 답이다 — 개인 사일로의 메모리를 정책에 따라 조직 공유 지식으로 **승격**한다.

## References

- [[tech-bridge-agent-knowledge-four-ways]] — 메모리를 RAG와 출처로 가른 첫 소스
- [[tech-bridge-agents-as-distributed-systems]] — 메모리=무효화 가능한 캐시
- [[anthropic-managed-agents]] — memory tool
- 관련: [[agent-knowledge-sourcing]] · [[retrieval-augmented-generation]] · [[context-engineering]] · [[skill-self-improvement]] · [[agent-distributed-systems]]
- [[tech-bridge-company-brain-security]] — 자동 저장 금지, 제안→사람 승인 (2026-09-10)
- [[tech-bridge-agent-to-agent-as-search]] — Apex/Ivy 영구 오염 사례, 청소부 에이전트 (2026-09-10)
