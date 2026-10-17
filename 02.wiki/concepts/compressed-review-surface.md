---
title: 압축된 리뷰 표면 (Compressed Review Surface)
type: concept
category: pattern
tags: [code-review, verification, diagrams, declarative-code, architecture, human-in-the-loop, ai-slop]
aliases: [compressed review surface, reviewable surface, 리뷰 표면, 검토 접점]
related: [verification-bottleneck, deep-modules, agent-state-machine, risk-proportional-human-review, cognitive-debt, read-fluency-for-agent-output, architecture-as-remaining-art, ai-slop, hard-vs-soft-enforcement]
first-seen: tech-bridge-g2i-generation-cheap-evaluation-expensive
sources: [tech-bridge-g2i-generation-cheap-evaluation-expensive]
created: 2026-10-16
updated: 2026-10-16
---

# 압축된 리뷰 표면 (Compressed Review Surface)

**에이전트가 구현 세부를 수천 줄씩 만들어 내는 상황에서, 사람이 검토하는 면을 구현이 아니라 구조(서비스 경계·데이터 흐름·상태 전이·실패 모드)로 압축하자는 원칙이다.** 다이어그램과 선언적 코드로 주 흐름을 리뷰 면에 남기고 구현은 "잎"으로 밀어낸다. [[gabriel-martinez|Gabriel Martinez]]([[g2i|G2i]])가 [[tech-bridge-g2i-generation-cheap-evaluation-expensive]]에서 제시했다.

> *"When a agents can generate thousands of lines of implementation detail, humans need a compressed review surface, service boundaries, data flows, state transitions, and failure modes."* (12:31~12:42)

> *"We can leave the main process or workflow as the reviewable surface with implementation details pushed to the leaves. That is why I vouch for declarative code and architecture patterns that create layers humans can actually reason about."* (12:47~12:57)

## 전제: 모든 줄을 읽는 것이 아니라 논리를 이해한다

- *"I'm not saying every line of code needs to be personally read, blessed, and understood in isolation. That has never really been the standard."*(03:06~03:13)
- *"But the logic has to be understood. The main flows, the boundaries, the data model, and product behaviors have to be understood."*(03:19~03:25)
- 다이어그램은 *"not as decorative documentation after the fact, but as a way of making systems legible"*(12:23~12:30)이다.

## 같은 처방 묶음

화자는 리뷰 표면을 관례와 한 묶음으로 둔다. *"conventions, standards, documented flows, small reviewable surfaces, and clear ownership boundaries and definitions of done. The more obvious the path, the less room there is for slop to hide."*(13:46~13:58) 관례는 리뷰어가 의도를 역설계하는 비용을 줄인다(*"reverse-engineer not just the code, but the intent behind it"* 13:35~13:41).

## 위키의 다른 페이지와

- [[verification-bottleneck]]의 답 가운데 **리뷰할 면 자체를 줄이는** 쪽이다. 리뷰를 자동화하는 쪽([[automated-code-review]])과 다르다.
- [[deep-modules]]: 복잡함을 단순한 인터페이스 뒤로 숨기는 일이 리뷰 쪽에서는 "구현을 잎으로" 보내는 일이 된다.
- [[agent-state-machine]]: Khourshid의 명시적 상태·전이는 화자가 꼽은 리뷰 면(*state transitions*)의 구체적인 형태다.
- [[risk-proportional-human-review]]: 그쪽은 리뷰 범위를 위험도로 가르고, 이쪽은 층(구조와 구현)으로 가른다.
- [[cognitive-debt]] · [[read-fluency-for-agent-output]]: 사람의 이해를 보존하는 쪽이다.

## ⚠️ 유보

- 화자가 예시 다이어그램이나 선언적 코드를 보여 주는 대목은 자막에 없다(화면은 확인하지 않았다). 효과 측정도 없다.
- 구현이 리뷰 면(다이어그램)과 어긋날 때 어떻게 탐지하는지는 발화되지 않는다. diagram-code drift 문제는 열려 있다([[tech-bridge-sentry-stop-prompting-codify-linters|Sentry 편]]의 OpenAPI drift와 비교할 자리).

## References

- [[tech-bridge-g2i-generation-cheap-evaluation-expensive]]
