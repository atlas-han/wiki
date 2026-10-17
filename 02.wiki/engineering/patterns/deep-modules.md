---
title: "깊은 모듈 (Deep Modules)"
type: engineering
category: pattern
tags: [software-design, modularity, interfaces, testing, ousterhout, coding-agents]
aliases: [deep module, 딥 모듈, 얕은 모듈, shallow module, locality, leverage, seam]
related: [structure-sensitive-tests, codebase-gardening, refactoring, technical-debt, test-harness-vs-test-authoring, self-contained-systems]
first-seen: tech-bridge-pocock-pr-bottleneck
sources: [tech-bridge-pocock-pr-bottleneck, tech-bridge-g2i-generation-cheap-evaluation-expensive]
created: 2026-10-09
updated: 2026-10-16
---

# 깊은 모듈

**복잡한 동작을 단순한 인터페이스 뒤에 숨기는 모듈.** John Ousterhout의 *A Philosophy of Software Design* 의 개념이고, 이 위키에는 [[matt-pocock|Matt Pocock]]이 [[tech-bridge-pocock-pr-bottleneck]]에서 **에이전트가 좋은 테스트를 쓰게 만드는 설계 수단**으로 가져오며 들어왔다.

> *"These are modules that hide complex behavior behind simple interfaces. This is a John ouster[=Ousterhout] idea from the philosophy of software design."* (08:38~08:44)

## 깊은 모듈 vs 얕은 모듈

| | A — 깊은 모듈 | B — 얕은 모듈 |
|---|---|---|
| 인터페이스 | **작다** | 크다 — 호출할 함수가 많다 |
| 구현 | **크다** | 함수 하나하나가 하는 일이 적다 |
| 테스트 | 인터페이스에서만 → *"fewer structure sensitive tests"* | 구현 세부에 닿기 쉽다 |

(08:47~09:12, 화자의 슬라이드 설명)

## 에이전트 시대에 왜 다시 중요한가

화자의 논거는 **테스트 품질**이다. 에이전트가 쓰는 테스트가 구현 구조에 붙는 것([[structure-sensitive-tests]])을 막으려면, 붙을 구조를 인터페이스 뒤로 숨기면 된다.

> *"your job here is to force the agent to use that little interface instead of reaching into the implementation to test these weird implementation details."* (09:18~09:27)

즉 **설계가 검증의 하드 강제가 된다** — [[hard-vs-soft-enforcement]]의 *코드베이스가 가장 강한 층* 과 같은 자리.

## 팀 어휘 — locality · leverage · seam

*"you're going to find 20 different approaches and they're all going to be called DDD"*(10:21~10:26)이라 팀에 일관된 말이 필요하다며 화자가 스킬에 넣은 정의:

- **locality** — 코드가 얼마나 한곳에 모여 있는가, 한 모듈의 작은 변경이 얼마나 번지는가(10:41~10:53).
- **leverage** — 깊은 모듈에서 얻는 것: 호출자가 단순한 함수 호출로 많은 가치를 얻는다(10:53~11:03).
- **seam** — 이름만 나온다(*"I was using seams before they were cool"* 10:39~10:41). ⚠️ 정의는 발화되지 않는다.

> *"Both of those are very good in code bases and good for agents too, it turns out."* (11:03~11:08)

## 도구화 (화자 진술)

화자의 **코드베이스 설계 스킬**은 코드베이스에서 모듈을 깊게 만들 기회를 찾아 before/after가 담긴 HTML 문서로 보여 준다(09:30~10:12). *"the crappiest codebase that you've ever set your eyes on and you can run this skill on it and it will make it better"*(09:36~09:41) — ⚠️ 측정 없는 자기 제품 진술.

## 위키의 다른 페이지와 맞닿는 자리

- [[codebase-gardening]] — *코드베이스는 에이전트의 기억*, 나쁜 패턴이 번진다. 깊은 모듈은 **번질 표면(인터페이스)을 줄이는** 쪽의 처방.
- [[self-contained-systems]] — 수직 분할로 *AI가 필요한 코드가 한곳에* — locality의 시스템 수준판.
- [[refactoring]] · [[technical-debt]] — 얕은 모듈을 깊게 만드는 일은 행동 보존 리팩터링이다.
- [[compressed-review-surface]] (2026-10-15): *"implementation details pushed to the leaves"*(12:51~12:53). 같은 원리의 **리뷰 쪽 판본**으로, 사람은 주 흐름을 보고 구현은 잎에 둔다.

## ⚠️ 유보

- 원전(Ousterhout의 책)을 이 위키는 읽지 않았다 — 정의는 화자의 요약이다.
- 깊은 모듈이 에이전트의 테스트 품질을 실제로 올린다는 측정은 없다.

## References

- [[tech-bridge-pocock-pr-bottleneck]] · [[matt-pocock]]
- John Ousterhout, *A Philosophy of Software Design* (원전, ⚠️ 미확보)
- 관련: [[structure-sensitive-tests]] · [[codebase-gardening]] · [[self-contained-systems]] · [[refactoring]] · [[hard-vs-soft-enforcement]]
