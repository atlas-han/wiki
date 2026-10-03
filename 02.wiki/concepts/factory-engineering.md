---
title: "공장 공학 (Factory Engineering) — 제품을 만드는 것을 짓는 엔지니어링"
type: concept
category: framing
tags: [software-factory, meta-engineering, developer-role, process-engineering, skill-loop, measurement, future-of-work]
aliases: [factory engineering, 공장 공학, meta-engineering, 메타 엔지니어링, building the thing that builds the product]
related: [software-factory, orchestras-not-factories, skill-self-improvement, harness-engineering, outcome-engineering, taste-vs-judgment, frontier-engineering, risk-proportional-human-review]
first-seen: tech-bridge-warp-factory-engineering
sources: [tech-bridge-warp-factory-engineering]
created: 2026-10-03
updated: 2026-10-03
---

# 공장 공학 (Factory Engineering)

**소프트웨어 엔지니어의 일이 제품을 직접 만드는 것에서 "제품을 만드는 에이전트 공장"을 설계·운영·측정·개선하는 것으로 옮겨 간다는 테제.** [[warp|Warp]]의 [[zach-lloyd|Zach Lloyd]]가 [[tech-bridge-warp-factory-engineering]]에서 발표 전체의 논지로 세웠다.

> *"the discipline of software engineering is going to become something more like factory engineering"* (01:24~01:31) · *"you're not just building the product, but you're building the thing that builds the product. And that's like it's just different. It's more like process engineering or manufacturing or something like that."* (14:48~15:00)

## 무엇이 바뀌나

| | 지금까지 | 공장 공학 |
|---|---|---|
| 만드는 것 | 제품(코드) | 제품을 만드는 것 — [[software-factory\|공장]] |
| 일의 모습 | 코드 작성 → 대화형 에이전트에게 지시 | 에이전트 그래프를 짓고, 사람이 들어올 지점을 정하고, 튜닝 |
| 성과 | 기능 | 효율 — *"how much software did you ship, how much did it cost in terms of human time and token time"*(13:32~13:40) |
| 개선 | 코드 리팩터링 | 루프 — observer 에이전트가 스킬을 고친다 → [[skill-self-improvement]] |

화자의 단계 구분: chat·자동완성 → Cursor·Copilot → **대화형 에이전트**(지금, *"telling Claude Code to do something"*) → **자동화**(6개월~1년, ⚠️ 예측 02:04~02:12).

## meta-engineering

*"You could almost think of it as like meta-engineering, like how do you engineer your system of agents to be the best possible engineering that I think is a very compelling and interesting set of challenges to solve."*(15:47~15:59)

남는 엔지니어링 과제는 **공장의 튜닝**이다 — *"are these the right skills for my domain? Is this factory building my product in the right way?"*(17:09~17:17). 공장 인프라 자체는 대부분 조직이 직접 짓지 말고 핵심 제품에 집중하라는 것이 화자의 권고(12:06~12:18, 17:22~17:34) — 화자는 그 인프라를 파는 쪽이다.

## 대가 — 코드를 덜 쓰고 더 출시한다

*"everyone in here is going to code less, but they're going to ship more and that's going to be a trade-off."*(15:29~15:36) 기쁨이 코드 작성에 있으면 아쉬울 것이고(*"maybe that's a bummer"* 15:03~15:06), 출시에 있으면 *"it's never been a better time"*(15:23~15:25).

## 사람이 남는 자리

- **루프의 고정 칸** — spec 리뷰 · 코드 리뷰(사람+에이전트) · 제품 리뷰(03:35~03:47). 코드 리뷰의 사람 투입은 *"risk management exercise"*(11:05~11:10) → [[risk-proportional-human-review]]
- **taste** — 은유가 *"mechanizing or dehumanizing"* 으로 들릴 수 있음을 인정하고(19:14~19:23), *"human taste, human input, human product sense"*(19:36~19:40)가 자동화할 수 없는 touch point에서 필수라고 한다 → [[taste-vs-judgment]]
- **기본기** — 졸업생에게: 적응력·비판적 사고·학습 속도, 그리고 *"understanding like the underlying systems and architecture"* — 에이전트가 쓴 코드와 spec을 이해·추론할 수 있어야(17:54~18:21)

## 위키에서의 좌표

- **[[harness-engineering]]** — 하네스 엔지니어링이 *에이전트 하나의 실행 환경*을 다룬다면, 공장 공학은 그것을 **SDLC 전체 그래프**로 넓힌 직무 정의다. 화자의 아키텍처에서 harness·model 선택은 샌드박스 층의 한 칸이다(12:49~12:56).
- **[[outcome-engineering]]** · Factory의 *"humans decide what, agents decide how"* — 같은 방향. 공장 공학은 거기에 **"how를 정하는 시스템을 짓는 일"이 엔지니어에게 남는다**를 더한다.
- **[[frontier-engineering]]** — 생산 코드의 대부분을 에이전트가 쓰는 개발자상. 공장 공학은 그 개발자의 산출물이 **코드가 아니라 공장**이라고 본다.

> ⚠️ **Contradiction: 은유.** [[orchestras-not-factories]]는 사람을 *"factory line managers like pushing buttons"* 로 만드는 은유 자체를 거부한다(Conductor). 공장 공학은 같은 우려를 인정하면서 **사람을 라인 관리자가 아니라 공장을 짓는 엔지니어로** 놓는다. 둘 다 측정 근거는 없다.

> ⚠️ **근거는 한 명의 진술.** 화자의 6개월 무코딩, Warp의 역대 최다 채용, 6개월~1년 안의 자동화 — 전부 당사자 진술·예측이다. 공장 공학이 엔지니어 수요를 줄이는지 늘리는지에 대한 데이터는 이 소스에 없다.

## References

- [[tech-bridge-warp-factory-engineering]] — first-seen (Zach Lloyd, Warp)
- [[software-factory]] · [[orchestras-not-factories]] · [[skill-self-improvement]] · [[zach-lloyd]] · [[warp]]
