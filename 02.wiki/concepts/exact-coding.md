---
title: "EXACT 코딩 (EXACT Coding) — 예시 매핑, 테스트 목록, 예측형 TDD"
type: concept
category: pattern
tags: [tdd, example-mapping, predictive-tdd, test-list, vibe-coding, subagents, human-in-the-loop, code-quality]
aliases: [EXACT, exact coding, 예시 매핑, example mapping, 예측형 TDD, predictive TDD, 테스트 목록, test list, example guided development]
related: [spec-driven-development, shift-left-interventions, context-rot, subagent-folding, structure-sensitive-tests, harness-pruning, risk-proportional-human-review, verifiable-goals]
first-seen: tech-bridge-emily-bache-exact-coding-tdd
sources: [tech-bridge-emily-bache-exact-coding-tdd]
created: 2026-11-07
updated: 2026-11-07
---

# EXACT 코딩 (EXACT Coding)

codecentric의 Marco Emrich · Ferdinand Ade(설명란 근거)가 만든 에이전트 코딩 워크플로. **무엇을 만들지는 사람들이 예시로 정하고, 어떻게 만들지는 에이전트가 TDD로 따른다.** 출처는 [[emily-bache|Emily Bache]]의 인터뷰 [[tech-bridge-emily-bache-exact-coding-tdd]] 하나다. 이름은 바이브 코딩에 대비한 말장난이다: *"we want to get exactly what we want, not what you get with VIP coding."*(01:52~01:56)

## 흐름

| 단계 | 누가 | 내용 |
|---|---|---|
| **예시 매핑** | 사람들 | 이해관계자와 사용자 스토리를 예시로 푼다. *"is made for humans"*(03:26) |
| **테스트 목록** | 사람 + 에이전트 | 자연어 테스트 후보를 모은다. 에이전트는 *"the LLM is checking if we are missing any obvious permutations"*(03:50~03:55) |
| **안쪽 TDD 루프** | 에이전트 | *"one item from the list at a time, going through red, green, refactor"*(03:08~03:10) |

진행자의 요약: *"build the right thing with example mapping"*(16:30~16:32) · *"build the thing right with predictive test-driven development"*(16:37~16:40)

## 예측형 TDD (Predictive TDD)

*"before you do any TDD step, you have to predict what the result would be."*(12:58~13:04) 테스트가 어떤 이유로 실패할지 먼저 말하게 한다. 이들은 LLM 이전에도 사람에게 썼다. 효과의 설명은 가설이다: *"the prediction brings the problem to the front of the context for the LLM"*(13:37~13:42)

## 실험에서 말한 것

- **평가 장치.** 학습 데이터에 없는 새 코드 카타와 *"a complete test suite of acceptance tests which they don't show the LLM"*(05:02~05:07)
- **예시 매핑.** 산문 요구 대비 *"the correctness increases by 60 70% 80% even in some cases"*(05:43~05:50)
- **TDD 방식.** 지시 없는 TDD는 *"is much cheaper in token cost"*(09:10~09:12), EXACT는 *"much higher code quality, much better unit tests, although at a higher cost in tokens."*(09:34~09:42)
- **서브에이전트.** Opus 5.5에서는 *"better results with two agents. The main agent doing most of the TDD workflow and a separate sub agent for the refactoring step."*(11:37~11:44) 이득은 *"not by much"*(11:49)이고 Opus 4.6에서 더 컸다. → [[subagent-folding]]

## 긴장

- **속도 · 비용.** 품질과 토큰을 맞바꾼다. 값은 화면 표에 있어 이 위키가 확인하지 못했다.
- **사람의 위치.** *"there is no clear answer to this question right now."*(14:18~14:20) 그래서 자율 수준을 고르게 한다. 그러나 경험담은 사람이 볼수록 낫다는 쪽이다. → [[risk-proportional-human-review]]
- **[[spec-driven-development]]와의 관계.** 비판 대상은 명세 자체보다 긴 문서를 *"looks good to me"*(07:52~07:55)로 넘기게 되는 경험이다. 예시 매핑도 명세를 얻는 일의 한 형태다(위키의 읽기).

## ⚠️ 유보

- **제작자의 자체 실험이고 영상 하나가 출처다.** 표본, 카타 수, 통계 처리, 외부 재현이 발화에 없다.
- 작은 신규 카타의 결과가 큰 기존 코드베이스로 옮겨진다는 근거가 없다.
- `en`에만 있는 카타별 수치 · 오픈소스 공개 · 집필 소식 · 자율 수준 3단계는 인용하지 않았다. 저장소도 확인하지 않았다.
- 발화자가 구분되지 않는 곳이 많아 Emrich · Ade 개인 페이지를 따로 만들지 않았다.

## References

- [[tech-bridge-emily-bache-exact-coding-tdd]] · [[emily-bache]]
- 관련: [[spec-driven-development]] · [[shift-left-interventions]] · [[context-rot]] · [[subagent-folding]] · [[structure-sensitive-tests]] · [[kent-beck]]
