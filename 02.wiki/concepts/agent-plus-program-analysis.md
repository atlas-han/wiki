---
title: 에이전트 + 프로그램 분석 (Agent + Program Analysis)
type: concept
category: pattern
tags: [verification, static-analysis, program-analysis, taint-analysis, data-flow, sca, automated-code-review, hybrid, vendor-claim]
aliases: [agentic validation + program analysis, 에이전트형 검증과 정적 분석의 결합, agents + SonarQube]
related: [automated-code-review, hard-vs-soft-enforcement, executable-standards, behavior-validated-trust, tree-sitter-llm-hybrid, deterministic-agent-pipeline, shift-left-security, verification-bottleneck]
first-seen: tech-bridge-gitar-agentic-pr-validation
sources: [tech-bridge-gitar-agentic-pr-validation]
created: 2026-10-16
updated: 2026-10-16
---

# 에이전트 + 프로그램 분석 (Agent + Program Analysis)

**코드 검증에서 LLM 에이전트와 전통적 프로그램 분석(taint·control flow·data flow·software composition analysis)을 합치면 어느 한쪽만 쓸 때보다 precision과 coverage가 낫다는 주장이다.** [[ali-reza|Ali-Reza]]([[gitar|Gitar]] → [[sonar|Sonar]])가 [[tech-bridge-gitar-agentic-pr-validation]]에서 제시했다. ⚠️ **측정이 아니라 전망이다.** 화자는 *"we think"* 라고 말하고, 통합은 진행 중이다.

> *"There's a ton of opportunity here in combining an agentic approach to validation with program analysis. So combining agents with things like um taint analysis, control flow analysis, data flow analysis, software composition analysis."* (08:53~09:09)

> *"the combination of using agents uh doing a gentic[=agentic] validation plus an algorithmic program analysis will give you something that that I think is going to be much better than either alone."* (10:40~10:52)

## 주장의 구성

- **무엇과 무엇을**: 에이전트형 검증(리뷰·CI 실패 분석·자동 수정, [[automated-code-review]])과, 화자가 *"all the traditional approaches"*(09:09~09:11)라 부르는 알고리즘적 분석.
- **기대 효과**: *"much better precision, much better coverage at a really great price point"*(09:16~09:23). 셋 중 precision·coverage는 화자가 자체 harness로 최적화한다고 말한 지표와 같다(*"token cost, precision, and coverage of the agent itself"* 08:24~08:27).
- **맥락**: Sonar의 Gitar 인수 이후 *"integrating guitar with Sonar Cube[=SonarQube]"*(08:47~08:53).

## 위키의 다른 페이지와

- [[tree-sitter-llm-hybrid]]: 결정론적 정적 분석은 구조적 사실을, LLM은 의미 해석을 맡기는 분업 패턴이다. 이 페이지는 같은 방향의 **검증(보안·품질) 쪽** 판본이다. 다만 화자는 어떻게 분업하는지 말하지 않는다.
- [[hard-vs-soft-enforcement]]: 프로그램 분석은 하드 층, 에이전트 리뷰는 소프트 층에 가깝다. 이 주장은 두 층을 **한 검증 단계 안에서** 겹치자는 것이다.
- [[deterministic-agent-pipeline]]: 결정론 노드와 LLM 노드를 나누는 설계와 같은 축 위에 있다.
- [[behavior-validated-trust]] · [[executable-standards]]: 정적 분석이 주는 결정론적 신뢰를 에이전트 검증에 더하는 쪽이다.
- [[shift-left-security]]: taint·SCA는 보안 검증 도구다. 그 페이지에는 도구 이름이 없었는데, 이 소스는 분석 종류를 명시한다(그러나 시점을 왼쪽으로 옮기자는 말은 아니다).

## ⚠️ 유보

- **결합 방식이 발화되지 않는다.** 분석 결과를 에이전트의 입력(컨텍스트)으로 주는지, 에이전트 발견을 분석으로 걸러 내는지(사후 필터), 아니면 둘을 병렬로 돌리는지 알 수 없다.
- 수치·비교 실험·출시 여부가 없다. 단일 소스이고 인수 직후 벤더가 한 전망이다.
- 설명란의 "결합 시너지"는 업로더 표기다.

## References

- [[tech-bridge-gitar-agentic-pr-validation]]
