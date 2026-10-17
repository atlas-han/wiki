---
title: "Feedforward·Feedback 조향 사분면 (Feedforward/Feedback × Computational/Inferential)"
type: concept
category: pattern
tags: [harness-engineering, steering, agents-md, static-analysis, generators, code-review, determinism]
aliases: [feedforward feedback quadrant, 2x2 조향 사분면, Böckeler 2x2, computational vs inferential, 피드포워드 피드백]
related: [harness-engineering, hard-vs-soft-enforcement, shift-left-interventions, automated-code-review, hook-enforced-workflow, executable-standards, llm-coding-guidelines, generator-evaluator-pattern, domain-specific-scripts]
first-seen: tech-bridge-rails-harness-engineering
sources: [tech-bridge-rails-harness-engineering, tech-bridge-sentry-stop-prompting-codify-linters, tech-bridge-horthy-state-of-software-factory]
created: 2026-10-09
updated: 2026-10-16
---

# Feedforward·Feedback 조향 사분면

**에이전트를 조향하는 메커니즘을 두 축으로 나눈다 — 언제(생성 전 *feedforward* / 생성 후 *feedback*) × 무엇으로(결정론적 *computational* / LLM *inferential*).** 프롬프트와 AGENTS.md는 네 칸 중 한 칸(feedforward·inferential)일 뿐이며, 판단을 나머지 세 칸으로 옮기라는 처방이 따라온다. [[joel-quenneville|Joël Quenneville]]가 Birgitta Böckeler의 모델로 소개했다, [[tech-bridge-rails-harness-engineering]] (20:16~22:58).

> *"There's a mental model that I really like that comes from Brigita Bookler[=Birgitta Böckeler] and she imagines various mechanisms for steering agents to sort of fit in this 2x two quadrant system. you have uh mechanisms that can either steer by feed forward that is uh before generation happens or through feed back uh after generation has happened and those mechanisms can either be deterministic computational or they can be LLMs they're inferial[=inferential]"* (20:20~20:50)

## 사분면 (발화를 칸에 놓은 것)

| | **computational (결정론)** | **inferential (LLM)** |
|---|---|---|
| **feedforward (생성 전)** | Rails 제너레이터 · 셋업 스크립트 · 템플릿 | 프롬프트 · AGENTS.md · 정적 문서 · 근처 소스 코드 |
| **feedback (생성 후)** | RuboCop · Reek · Flog · Code Climate · 보안 스캐너 · 테스트 · 로그 확인 · Playwright | 에이전틱 리뷰 · 에이전트 주도 분석 |

(⚠️ 슬라이드는 화면에만 있다 — 표는 20:52~22:58 발화를 위키가 정리한 것.)

## 처방 — 판단을 한 칸에서 세 칸으로

> *"In general, I find it's good to move judgment out of that feed forward inferial quadrant and into the other three. Personally, I like to have my agents in D[=AGENTS.md] be a very thin almost routing layer rather than be a dump of my brain."* (21:30~21:43)

그러나 버리라는 말은 아니다 — *"quadrant is a really valid part of the story when it comes to steering your agents. It's just not the only one."*(21:23~21:27)

## 왜 feedback·inferential이 feedforward·inferential보다 나은가

같은 LLM 휴리스틱이라도 **언제** 적용하느냐가 다르다. 생성 전 규칙은 *"pluck a program for the like entire universe of possible programs"*(19:28~19:32) — *"steering from behind the starting line"*(19:45). 생성 후 리뷰는 *"apply them backwards to a concrete program I've already generated. It's much easier to find violations in a program I've written now than for all possible programs I could generate in the future."*(20:00~20:12) — 화자의 말로 *"steer from the middle of the path"*(19:49~19:52).

## 위키에서의 자리

- **[[hard-vs-soft-enforcement]]** — 그 페이지의 하드/소프트는 이 표의 **computational/inferential 축**과 거의 겹친다. 이 모델은 거기에 **시간 축**(생성 전/후)을 더한다 — 소프트 층(리뷰 스킬)도 *생성 후*로 옮기면 쓸모가 커진다는 것이 새 주장.
- **[[shift-left-interventions]]** — 프롬프트 → AGENTS.md → 정적 검증기 → eval 스펙트럼은 이 표의 feedforward·inferential에서 feedback·computational로 가는 대각선 이동과 같은 방향이다(⚠️ 위키의 대응).
- **[[harness-engineering]]** — 그 페이지는 System Evolution을 *"인간이 steering하는 feed-forward 시스템"* 이라 불렀다. 이 모델에선 그것도 네 칸 중 하나다.
- **[[automated-code-review]]** · **[[generator-evaluator-pattern]]** — feedback·inferential 칸.
- **[[domain-specific-scripts]]** — 화자는 칸에 넣지 않았지만, 결정론적 분류를 LLM 분석에 먹이는 것이라 computational이 inferential을 받치는 혼합형이다(⚠️ 위키의 배치).
- **[[tech-bridge-sentry-stop-prompting-codify-linters|Sentry 편]]** (2026-10-14): [[greg-pstrucha|Greg Pstrucha]]의 처방은 Quenneville과 같은 이동이다. 반복 교정을 feedforward·inferential(re-prompt)에서 **feedback·computational(linter)** 로 옮기고, 남는 정성 판단은 **feedback·inferential(정책별 서브에이전트 루프 grumpy engineer)** 로 옮긴다. 두 번째 화자다(Böckeler 모델은 언급하지 않는다).
- ⚠️ (2026-10-15) [[back-pressure]]의 *forward pressure*([[dex-horthy|Horthy]])는 이 페이지의 *feedforward* 와 **다르다** — 일을 시작시키는 trigger(스케줄·자동화·webhook)이지 행동 전 안내가 아니다. *back pressure* 는 feedback 칸(computational: 브라우저·curl·테스트, 사람/사용자: UI 실험)과 겹친다.

## ⚠️ 유보

- **원 글 미확보.** Böckeler의 2×2가 실린 글의 제목·게재처는 발화되지 않았고 이 위키에 없다. 위 정의는 **Quenneville의 요약**이다.
- en-orig 표기는 *"Brigita Bookler"*, *"inferial"* — 이름은 `en`·ko(*"비르기타 뵈켈러(Birgitta Böckeler)"*)로 판독.
- Goodhart 경고(23:01~23:40)는 feedback·computational 칸에도 한계가 있다는 단서다 — 점수형 게이트를 너무 조이면 에이전트가 해킹한다.

## References

- [[tech-bridge-rails-harness-engineering]] · [[joel-quenneville]] · [[hard-vs-soft-enforcement]] · [[shift-left-interventions]] · [[harness-engineering]]
