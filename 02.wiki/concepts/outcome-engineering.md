---
title: Outcome Engineering
type: concept
category: pattern
tags: [agent, workflow, llm-coding, productivity, codex]
related: [verifiable-goals, sprint-contract, harness-engineering, agent-harness-design, context-engineering]
first-seen: openai-nextdoor-codex
sources: [openai-nextdoor-codex]
created: 2026-06-27
updated: 2026-06-27
---

# Outcome Engineering

**Outcome engineering**은 [[cory-dolphin|Cory Dolphin]](Nextdoor Head of Engineering)이 [[openai-nextdoor-codex|OpenAI Codex 케이스 스터디]]에서 제시한 프레이밍으로, *에이전트를 반복적으로 프롬프팅(iteratively prompting)하는 작업 방식에서 벗어나, **원하는 결과(outcome)를 정의하고 에이전트와 함께 그 결과를 engineer**하는 방식*으로의 전환을 가리킨다.

> "away from iteratively prompting an agent, and towards **outcome engineering**, where engineers start to think about the result they want to see and work with an agent to engineer that result." — Cory Dolphin

> ⚠️ 이 용어는 OpenAI 마케팅 케이스 스터디에서 나온 **현장 coinage**다. 학술·업계 표준 용어가 아니라 한 조직의 framing이며, 아래 연결은 본 위키의 기존 개념과의 *해석적* 매핑이다.

## 핵심 전환

| 기존 (prompt engineering 루프) | Outcome engineering |
|---|---|
| *어떻게(how)* 만들지를 에이전트에 단계별 지시 | *무엇을(what/result)* 원하는지를 정의 |
| 프롬프트를 반복 수정하며 수렴 | 결과물(스크린샷·영상·성능·테스트 통과)을 목표로 에이전트가 수렴 |
| 엔지니어 = 특정 시스템/프레임워크 전문가 | 엔지니어 = 제품을 end-to-end 소유 |

원하는 outcome의 구체적 형태(원문): **스크린샷이나 영상**(에이전트가 그쪽으로 빌드), **특정 성능·테스트 결과**, 또는 **새로운 기능 아이디어**.

## 조직적 귀결 — "스택 위로 이동"

- 엔지니어가 시스템/프레임워크 전문가에 묶이지 않고 제품 경험을 거의 end-to-end로 소유 (mobile·frontend·backend 경계를 넘나듦).
- 사례: 과거 3개 팀 협업이 필요해 백로그에 묻혔을 기능("지도에 서비스 제공자 표시")을 **한 명이 end-to-end 구축**.
- **병목 이동**: 생산성이 가속되면서 병목이 *엔지니어링*에서 *"무엇을 만들지"라는 전략적 질문*으로 이동.

## 위키 내 자매 개념

- [[verifiable-goals]] — *"원하는 결과를 정의한다"* 는 곧 **verifier를 먼저 정의**하는 것. outcome engineering의 *result*(스크린샷/테스트 통과)는 verifiable-goals의 *verifier* 와 같은 자리에 있다. 두 framing이 사실상 같은 원리를 조직 관점(Nextdoor) vs 코딩 원칙 관점(multica CLAUDE.md)에서 서술.
- [[sprint-contract]] — 코드 작성 *전에* "done의 정의"를 못 박는 다중 에이전트 인공물. outcome을 계약으로 형식화한 형태.
- [[harness-engineering]] — 원문은 Nextdoor가 에이전트에 *"clean environment and harness for investigation"* 를 제공한다고 언급. outcome을 향한 작업도 결국 harness 위에서 일어난다.
- [[agent-harness-design]] — outcome engineering은 *모델이 더 잘하게 되면서* 사람의 역할이 how→what으로 올라가는 사례. "harness가 인코딩한 가정이 stale된다"는 일반 원리의 인적(human-role) 버전.

## 대비 — context/prompt engineering과의 관계

[[context-engineering]]·prompt 반복이 *입력*을 정교화하는 영역이라면, outcome engineering은 *목표(출력 명세)*를 정교화하는 영역으로 프레이밍된다. 모델 capability가 올라갈수록 작업 무게중심이 입력 튜닝 → 결과 명세로 이동한다는 주장.

## 한계·주의

- 출처가 **벤더 케이스 스터디**라 정량 근거 없이 생산성·역할 변화를 *주장*한다. "병목이 엔지니어링이 아니다" 같은 진술은 Nextdoor 1개 조직의 경험담.
- "스택 위로 이동"이 모든 조직·도메인에 일반화되는지는 미검증.

## References

- [[openai-nextdoor-codex]] — 원 출처 (OpenAI 고객 사례, 2026-06-09)
- 자매 개념: [[verifiable-goals]] · [[sprint-contract]] · [[harness-engineering]]
