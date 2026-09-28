---
title: Hook-Enforced Workflow
type: concept
category: pattern
tags: [hooks, harness, enforcement, agent-skills]
related: [agent-skills, agent-harness-design, hard-vs-soft-enforcement, self-harness, no-silent-write]
first-seen: tech-bridge-graft-code-knowledge-graph
sources: [tech-bridge-graft-code-knowledge-graph, tech-bridge-skill-engineering-dark-arts]
created: 2026-09-15
updated: 2026-09-28
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

## Pre 대 Post, 그리고 ignore 규칙 — 배포되는 훅 (2026-09-28 · [[tech-bridge-skill-engineering-dark-arts]])

[[impeccable|Impeccable]]도 [[graft]]처럼 **스킬 + 훅**을 함께 배포한다 — 설치 시 Claude Code·Cursor·Codex·GitHub Copilot에 **디자인 린트 훅**이 들어가고 *"It's a guardrail that fires on every edit"*(30:36~30:55). 동기는 이 페이지의 첫 문장 그대로다: 하나로 묶인 스킬을 하네스가 *"forget to simply call (…) when you don't explicitly mention it"*(30:00~30:06). *"passive guardrails beat a command no one remembers to run"*(32:18~32:21).

새로 더해지는 것 셋:

| 항목 | 내용 |
|---|---|
| **Pre 대 Post는 모델 강도의 함수** | 기본은 PostToolUse — 위반을 알리면 *"The model just course corrects and fixes itself"*(33:43~33:50). 그러나 *"slightly weaker models like composer and cursor"* 는 지시를 잘 안 따라 **PreToolUse로 쓰기 자체를 막았다** — *"a much more heavy-handed approach, but we needed to do that for certain models and certain har[ness]es"*(31:09~31:56) |
| **하네스마다 문법·동작이 다르다** | *"the hook syntax for codex and clot[Claude] code is not the same (…) the behavior is not the same"*(31:02~31:09) → [[cross-harness-skill-compilation]] |
| **ignore 규칙이 필수** | *"oftentimes these hooks have false positives as well and you want a way to configure those hooks. Um, otherwise gets really annoying very quickly"*(34:01~34:10). Impeccable은 파일 단위부터 CSS 규칙 안까지 여러 수준의 ignore를 준다(34:13~34:21) |

이 페이지의 기존 경고(*"훅이 강제하는 만큼 틀렸을 때도 강제한다"*)에 대한 **실무 처방이 처음 나왔다** — 오탐을 전제하고 사용자가 끌 수 있게 하라. 다만 PreToolUse 차단의 오탐은 **쓰기 자체를 막으므로** 비용이 더 크다는 점은 소스가 따로 말하지 않는다. ⚠️ **훅까지 설치하는 스킬**의 신뢰·업데이트 경로도 논의되지 않는다(화자는 자체 설치기가 *"the hooks in the right part of the system"* 에 넣는다고만 한다, 1:03:56~1:04:02).
