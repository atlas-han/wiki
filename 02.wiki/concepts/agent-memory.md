---
title: Agent Memory
type: concept
category: pattern
tags: [memory, agent, experience, retrieval, cache]
aliases: [에이전트 메모리, Memory]
related: [retrieval-augmented-generation, agent-knowledge-sourcing, context-engineering, agent-distributed-systems, skill-self-improvement]
first-seen: tech-bridge-agent-knowledge-four-ways
sources: [tech-bridge-agent-knowledge-four-ways, tech-bridge-agents-as-distributed-systems, anthropic-managed-agents]
created: 2026-09-08
updated: 2026-09-08
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

## References

- [[tech-bridge-agent-knowledge-four-ways]] — 메모리를 RAG와 출처로 가른 첫 소스
- [[tech-bridge-agents-as-distributed-systems]] — 메모리=무효화 가능한 캐시
- [[anthropic-managed-agents]] — memory tool
- 관련: [[agent-knowledge-sourcing]] · [[retrieval-augmented-generation]] · [[context-engineering]] · [[skill-self-improvement]] · [[agent-distributed-systems]]
