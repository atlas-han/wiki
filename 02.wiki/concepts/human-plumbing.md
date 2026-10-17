---
title: "인간 배관 (Human Plumbing)"
type: concept
category: pattern
tags: [harness-engineering, agent-loop, anti-pattern, automation, human-in-the-loop]
aliases: [human plumbing, 인간 배관, 사람이 배관 노릇, human plumbing loop]
related: [harness-engineering, linear-vs-closed-loop-harness, shift-left-interventions, hook-enforced-workflow, verifiable-goals, skill-self-improvement, tools-and-context-over-harness]
first-seen: tech-bridge-rails-harness-engineering
sources: [tech-bridge-rails-harness-engineering, tech-bridge-horthy-state-of-software-factory]
created: 2026-10-09
updated: 2026-10-16
---

# 인간 배관 (Human Plumbing)

**모델이 스스로 할 수 없는 일(코드 실행·린터·리뷰 호출)을 사람이 대신 돌리고 그 결과를 프롬프트에 복사해 넣으며 루프를 손으로 이어 주는 상태.** 동작은 하지만 사람의 시간을 기계적인 일에 쓰는 안티패턴이고, 처방은 **그 루프를 하네스에 넘기는 것**이다. [[joel-quenneville|Joël Quenneville]]의 반복 개념어, [[tech-bridge-rails-harness-engineering]].

> *"Now remember, a model can't run code on its own. So we could run it ourselves, pass the results into the prompt, and that works. But now we've put ourselves in the role of human plumbing. We're just doing that loop. And that's a waste of our time. That's a mechanistic sort of thing."* (06:15~06:34)

## 같은 모양이 세 번 나온다

| 자리 | 사람이 하는 배관 | 하네스로 넘기는 법 |
|---|---|---|
| 테스트 (06:15~06:46) | 스펙 실행 → 실패 출력 복사 | 하네스에 **루프** — 테스트가 통과할 때까지 자가 수정 |
| 린트 (10:06~10:15) | RuboCop 실행 → 결과 복사 | AGENTS.md 지시 한 줄 → **Stop 훅** |
| 리뷰 (17:50~18:04) | 코드 생성 뒤 리뷰 스킬을 손으로 호출 | **서브에이전트**로 리뷰 스킬을 자동 호출 |

공통 질문은 *"how would you have solved that by hand?"*(05:47~05:51) — 사람이 손으로 하던 확인 절차를 그대로 하네스에 준다.

## 탈출 규칙

> *"Anytime you find yourself in this human plumbing loop, try to get yourself out of it. Can the LLM get direct access to a tool and read or write something itself?"* (28:35~28:44)

회고 질문 중 하나가 정확히 이것이다 — *"Was there anything I had to manually copy back and forth?"*(28:54~28:56).

## 위키에서의 자리

- **[[linear-vs-closed-loop-harness]]** — human plumbing은 *사람이 닫아 주는 폐루프*다. 그 페이지의 폐루프 하네스가 사람을 대신한다.
- **[[shift-left-interventions]]** ([[ryan-lopopolo|Lopopolo]]) — *"게으른 프롬프터"* 가 되려는 것과 같은 동기, 다른 이름. Lopopolo는 **프롬프트에 넣는 손**을, Quenneville은 **결과를 나르는 손**을 줄인다.
- **[[verifiable-goals]]** — 루프가 돌려면 사람 없이 판정할 수 있는 종료 조건(테스트·cop)이 있어야 한다.
- **[[skill-self-improvement]]** — retro 스킬이 *"어디서 개입했나"* 를 세션 히스토리에서 찾아 자동화를 제안한다.
- (2026-10-15 · [[tech-bridge-horthy-state-of-software-factory]]) 팀 단위의 같은 모양: *"I'm talking to my agent and I copy something out and I paste it into Slack or Teams. My my teammate reads it, they paste it into their agent, they get an answer, they paste it back to me."*(13:39~13:49) — 해법을 하네스가 아니라 **세션·계획·프롬프트의 system of record**로 둔다 → [[agent-platform-layers]].

## ⚠️ 유보

- 측정 없음 — 배관을 하네스로 넘긴 뒤 시간이 얼마나 줄었는지 화자는 수치를 내지 않는다.
- ko 자막은 이 말을 **"인간 파이프 종이" · "인체 배관에 관한 논문" · "인간 유지 관리"** 로 매번 다르게 옮겼다(06:28 · 10:15 · 18:00). 검색 시 주의.

## References

- [[tech-bridge-rails-harness-engineering]] · [[joel-quenneville]] · [[harness-engineering]] · [[linear-vs-closed-loop-harness]] · [[shift-left-interventions]]
