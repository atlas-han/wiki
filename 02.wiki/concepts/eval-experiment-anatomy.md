---
title: eval 실험의 구성 (Eval Experiment Anatomy) — 데이터셋·태스크·채점, 그 조합 하나가 실험 하나
type: concept
category: pattern
tags: [evals, datasets, scoring, experiments, llm-as-judge, regression-testing, observability]
aliases: [eval anatomy, eval 네 요소, 평가의 네 가지 요소, dataset task scorer experiment, eval experiment]
related: [eval-platform-maturity-stages, production-trace-eval-flywheel, taste-encoded-evals, field-level-unit-test-evals, skill-evals, verifiable-goals, generator-evaluator-pattern, agent-harness-design]
first-seen: tech-bridge-braintrust-agentic-vs-vector-search-eval
sources: [tech-bridge-braintrust-agentic-vs-vector-search-eval]
created: 2026-10-17
updated: 2026-10-17
---

# eval 실험의 구성 (Eval Experiment Anatomy)

**eval은 데이터셋·태스크·채점·실험 네 요소로 이루어지고, 특정 데이터셋 × 특정 태스크 × 특정 채점의 조합 하나가 실험 하나다. 가설을 시험할 때는 셋 중 하나를 바꿔 새 실험을 만들고, 실험끼리 행 단위로 비교한다.** [[jess-wang|Jess Wang]]([[braintrust|Braintrust]])이 [[tech-bridge-braintrust-agentic-vs-vector-search-eval]]에서 eval 입문으로 제시했다.

> *"every configuration of a specific data set a specific task and a specific scoring system equals to one experiment and as you are testing out different hypothesis for how to make your system better you're tweaking either your data set your task or your scoring system and these all lead to different experiments."* (04:02~04:20)

## 네 요소

| 요소 | 화자의 정의 | 들어가는 것 |
|---|---|---|
| **데이터셋** | *"the data that you're passing into your AI system"*(02:59~03:04) | *"golden standard uh cases, your edge cases, your failure modes"*(03:06~03:11) |
| **태스크** | *"how you want your AI system to behave when it takes in the input and produces an output"*(03:16~03:21) | *"a system prompt and then the model"*(03:24~03:28) |
| **채점** | *"whether the AI's output is good or bad"*(03:34~03:37) | 기준은 보통 PM이나 엔지니어가 쓴다(03:40~03:44). *"deterministic scoring, LLM as a judge, human (…) review"*(03:48~03:51) |
| **실험** | 위 셋의 조합 하나(04:02~04:10) | 실험끼리 *"improvements or regressions"*, *"exactly which test cases have changed"*(04:26~04:36) |

eval의 목적은 *"a way to answer questions about your AI system"*(01:20~01:24)이다. 화자는 출시 근거로 *"200 different test test cases and 94% of them passed"* 같은 문장을 원하고(01:00~01:06, 예시), *"making ship decisions based off of vibes"*(00:51~00:53)를 피하라고 한다.

## 실제로 적용한 예 — 코드 검색 비교

같은 소스의 실험이 이 틀을 그대로 쓴다.

- **데이터셋**: Microsoft TypeScript Go 저장소의 *"fix"* 머지 PR 약 20개. 부모 커밋을 체크아웃하고 Claude가 diff로 버그 태스크를 만들었다(11:17~12:05).
- **태스크**: 하네스(Claude Code)를 고정하고 검색 방식만 바꿨다. vector 쪽은 프롬프트 금지에 더해 disallowed tools 플래그로 agentic 도구를 막았다(*"prompting is never enough"* 12:47~12:50).
- **채점**: 테스트 스위트 통과 100%, 실패 0%의 이진 채점(14:34~14:47).
- **실험 두 개의 비교**: 정확도는 같은 수준, 비용은 vector가 4배(14:51~15:01). 원인은 trace를 손으로 읽어 찾았다(15:04~16:35).

⚠️ 이 예는 이 틀의 **함정**도 보여 준다. 태스크(위치 찾기, 11:54~11:58)와 채점(테스트 통과는 수정을 요구, 14:34~14:43)이 맞물리는지 발화로는 확인되지 않는다. 또 화자가 놓쳤다고 인정한 것(작업당 여러 번 시행, 16:49~17:00)은 이 표에 칸이 없는 **반복 차원**이다.

## 위키의 다른 페이지와

- [[eval-platform-maturity-stages]]: 같은 회사 Niazmandi의 "최소 eval 시스템 세 요소"(입력 세트 · 실행 방법 · 출력/점수 보기)와 대응한다. 이쪽은 **채점과 실험을 분리하고 실험을 비교 단위로 세운다**.
- [[production-trace-eval-flywheel]]: 데이터셋의 출처를 프로덕션 로그 샘플(*"maybe like 10 to 20 rows"* 06:37~06:39)로 두면 순환이 된다.
- [[field-level-unit-test-evals]] · [[taste-encoded-evals]]: 채점 칸의 두 끝(결정론적 vs 취향·판단).
- [[agent-harness-design]]: 태스크 칸에서 하네스를 고정하고 변수 하나만 바꾸는 통제.
- [[skill-evals]]: Bakaus의 *"vibes based"* 에서 테스트로 옮겨 간 과정과 같은 출발점.

## ⚠️ 유보

- 단일 소스, 벤더 DevRel의 입문 설명이다. 틀 자체는 새로운 주장이라기보다 표준적인 정리로 보이지만, 이 위키에서는 이 소스가 처음 명시했다.
- 반복 시행·통계적 유의성·데이터셋 크기의 기준은 다루지 않는다(화자가 한계로만 언급).

## References

- [[tech-bridge-braintrust-agentic-vs-vector-search-eval]] · [[jess-wang]] · [[braintrust]]
