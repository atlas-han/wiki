---
title: Hook-Enforced Workflow
type: concept
category: pattern
tags: [hooks, harness, enforcement, agent-skills]
related: [agent-skills, agent-harness-design, hard-vs-soft-enforcement, self-harness, no-silent-write]
first-seen: tech-bridge-graft-code-knowledge-graph
sources: [tech-bridge-graft-code-knowledge-graph]
created: 2026-09-15
updated: 2026-09-15
---

# Hook-Enforced Workflow

**스킬은 에이전트에게 무엇을 할지 *알려 준다*. 훅은 하지 않을 선택지를 *없앤다*.**

[[tech-bridge-graft-code-knowledge-graph]]에서 [[graft]]의 `init`은 프로젝트에 **스킬 하나 + 훅 셋**을 함께 설치한다.

| 훅 | 시점 | 하는 일 |
|---|---|---|
| 세션 시작 | 세션이 열릴 때 | 모델에게 **인덱스 사용 지침** 주입 |
| 프롬프트 | 메시지를 보낼 때마다 | 단어를 인덱스와 맞춰 **최대 3개 위치 첨부** |
| 편집 후 | 파일이 수정된 뒤 | **인덱스 갱신** → [[incremental-index-freshness]] |

화자의 표현이 이 패턴의 정의다 — ***"이 훅들이 에이전트가 [그] 워크플로를 따르도록 강제합니다."***

## 왜 스킬만으로는 부족한가

스킬·플레이북·`CLAUDE.md`는 전부 **컨텍스트에 놓이는 지시**다. 모델은 그것을 **무시할 수 있고**, 컨텍스트가 길어지면 **잊는다**([[context-resets-and-compaction]]). 훅은 **하네스가 실행하는 코드**라서 모델의 협조에 의존하지 않는다.

이 위키의 [[hard-vs-soft-enforcement]]가 **정책 층**에서 세운 구분 — 규칙을 말해 두는 것과 통과하지 못하게 막는 것 — 이 **하네스 층에서 그대로 반복된다.**

## 세 훅의 성격이 다르다

- **세션 시작·편집 후**는 **불변식 유지**다(지침이 늘 있고, 인덱스가 늘 최신이다).
- **프롬프트 훅은 조달이다** — 그리고 **낭비를 감수하는 쪽**이다. 에이전트가 필요로 했든 아니든 붙인다 → [[push-vs-pull-context-retrieval]].

> ⚠️ 훅이 강제하는 만큼 **틀렸을 때도 강제한다.** 프롬프트 훅이 엉뚱한 위치를 붙였을 때 무슨 일이 생기는지 **소스는 말하지 않는다.** 매 메시지에 자동으로 내용을 주입하는 구조가 [[prompt-injection]]·[[lethal-trifecta]] 관점에서 어떤 표면을 여는지도 **논의되지 않는다.**

## References

- [[tech-bridge-graft-code-knowledge-graph]] · [[graft]] · [[agent-skills]] · [[hard-vs-soft-enforcement]]
