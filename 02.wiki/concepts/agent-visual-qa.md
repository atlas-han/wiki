---
title: Agent Visual QA
type: concept
category: technique
tags: [qa, verification, multimodal, completeness, design]
related: [generator-evaluator-pattern, agent-verification-skill, verification-bottleneck, skill-evals, multimodal-elicitation, design-handoff-friction]
first-seen: tech-bridge-one-designer-plus-ai
sources: [tech-bridge-one-designer-plus-ai]
created: 2026-09-15
updated: 2026-09-15
---

# Agent Visual QA

**에이전트에게 최종 산출물을 *보게* 해서 빠진 것을 찾는 검증.** 코드가 아니라 **그림**이 대상이고, 묻는 질문이 *"맞는가"* 가 아니라 ***"빠진 게 있는가"*** 다.

[[tech-bridge-one-designer-plus-ai]]의 두 사례:

| 과제 | 방식 | 화자의 평가 |
|---|---|---|
| **사진 ↔ 발표자 매칭** | *"이 사람 누구야?"* — *"일종의 틴더 같은 판정"*(동일 인물인지) | *"꽤 정확한 것 같다"* |
| **스폰서 로고 누락 검수** | 140곳 배너에서 *"빠진 로고가 있는지 비교해 줄 수 있어?"* · 티셔츠에도 동일 | ***"제가 해 본 테스트 기준 정확도 100%"*** |

> **사람은 실수를 하거든요 — "어, 작은 게 하나 빠졌네" 하는 식으로요. 사람 + AI를 합치면 여러분만의 QA 팀이 생기는 겁니다.** (13:45~14:03)

## 왜 이 과제 형태가 잘 맞는가

**열거 검사는 사람이 가장 약한 종류의 일이다** — 140개를 한 눈에 훑으며 하나가 빠졌는지 판정하는 것은 주의력의 문제이지 판단력의 문제가 아니다. 반대로 **판정 기준이 명확**해서(원본 목록 vs 그래픽) **모델의 취향이 개입할 여지가 없다.** 이 위키가 [[taste-vs-judgment]]에서 다뤄 온 *취향이 필요한 판정* 과는 정반대 끝이다.

## 위키의 검증 논의에서의 자리

[[generator-evaluator-pattern]]·[[agent-verification-skill]]·[[skill-evals]]는 지금까지 거의 **코드**의 검증이었다. 이 페이지는 **최종 산출물의 시각적 완전성**을 더한다 — [[verification-bottleneck]]이 말하는 *병목이 검증으로 옮겨갔다* 가 **디자인 조직에서도 성립**한다는 첫 사례다.

> ⚠️ **"100%"는 자기 보고다.** 표본 수·시행 횟수·오탐 여부가 소스에 없다. 그리고 **배너를 만든 사람이 검수도 시킨다** — 2026-09-09 이래 이 위키가 네 번째로 마주치는 **작성자 = 검증자** 구도다. 로고 매칭의 근거 자료(스폰서 원본 목록)가 어디서 오는지도 소스에 없다.

## References

- [[tech-bridge-one-designer-plus-ai]] · [[vincent-wendy]] · [[devin]]
