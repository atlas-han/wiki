---
title: LangChain
type: entity
category: org
tags: [agent-framework, open-source, integrations, evals, middleware, vendor]
aliases: [LangChain, 랭체인, LangChainAI]
links:
  - https://www.langchain.com/
  - https://www.langchain.com/langsmith
sources: [tech-bridge-jev-agent-harness, tech-bridge-uber-debug-assist, tech-bridge-goodbye-slop-state-machines]
created: 2026-09-26
updated: 2026-10-09
---

# LangChain

LLM 애플리케이션·에이전트 프레임워크를 만드는 회사이자 그 오픈소스 라이브러리. 이 위키에서는 오래 **다른 소스의 부수적 언급**(통합·프레임워크 이름)으로만 등장했고, [[tech-bridge-jev-agent-harness]](2026-09-25 업로드)가 **LangChain 사람이 직접 말하는 첫 소스**다 — 오픈 소스 팀 PM "Sydney"가 파트너 모델 [[jev|Jev]]의 통합을 소개한다.

> ⚠️ 그 소스는 **벤더의 제품 소개**다. 아래 LangChain 쪽 제품 서술은 전부 자기 서술이다.

## 이 위키에 나온 LangChain

| 무엇 | 내용 | 소스 |
|---|---|---|
| **LangChain Type-Safe 통합** | [[typesafe-ai\|TypeSafe]]의 [[jev\|Jev]]를 부르는 classifier. 상태 + 질문 → 질문별 답 (05:38~05:57). 패키지 `langchain-typesafe`(⚠️ ASR 기준 추정) | [[tech-bridge-jev-agent-harness]] |
| **auto mode 미들웨어** | *"사전 구축된 auto mode 미들웨어"* — 도구 호출의 위험을 분류해 런타임 차단 (06:50~07:00) | [[tech-bridge-jev-agent-harness]] |
| **내부 코딩 에이전트의 모델 라우팅** | 복잡도에 따라 빠른/강한 모델 전환을 *"탐색 중"* (06:17~06:30) | [[tech-bridge-jev-agent-harness]] |
| **Jev-as-a-judge 온라인 eval** | 블로그 *Jev-as-a-Judge for Agent Evals*(LangSmith 경로) — 구두로만 *"더 싸고 빠르고 더 일관적"* (08:31~08:42) | [[tech-bridge-jev-agent-harness]] |
| **LangChain Oracle DB** | 벡터 스토어 통합 | [[tech-bridge-oracle-agent-memory-harness]] · [[oracle]] |
| **프레임워크 이름** | 도구 정의 맥락에서 언급 (05:39) | [[tech-bridge-build-time-vs-runtime-tools]] |
| **[[deepagents\|DeepAgents]]** | LangChain의 에이전트 SDK — Self-Harness 실험의 초기 하네스 | [[self-harness-paper]] |

- **LangGraph를 프로덕션 에이전트 골격으로 쓰는 고객 사례**(2026-10-09, [[tech-bridge-uber-debug-assist]]) — [[uber|Uber]] [[debug-assist|Debug Assist]]는 *"built on a LangGraph pipeline. It is a mix of deterministic and LLM nodes"*(08:52~08:59). 고른 이유는 계획 단계 우회: *"What LangGraph or LangChain allows us to do is bypass that planning phase"*(09:08~09:13) → [[deterministic-agent-pipeline]]. Arize 트레이싱을 LangChain에 붙여 모든 LLM·도구 호출을 본다(25:28~25:35). ⚠️ 벤더가 아니라 **사용자 쪽 1인칭** — 이 위키의 LangChain 1인칭 소스([[tech-bridge-jev-agent-harness]])와 다른 시점.

## 이 위키에서의 자리

LangChain 편의 프레이밍은 **하네스 = 루프 + 루프 안의 결정 지점들**이고, 그 결정 지점(라우팅·안전 게이트·채점)을 **LLM이 아닌 분류 모델**에 맡기자는 것이다 → [[system-1-model]] · [[agent-harness-design]] · [[harness-engineering]].

## References

- [[tech-bridge-jev-agent-harness]] — first-seen (1인칭)
- [[tech-bridge-uber-debug-assist]] — LangGraph 고객 사례 (Uber Debug Assist) · [[uber]] · [[debug-assist]]
- [[tech-bridge-goodbye-slop-state-machines]] — LangGraph를 상태 머신 도구로 언급 · [[david-khourshid]]
- [[deepagents]] · [[jev]] · [[typesafe-ai]] · [[oracle]]
- 외부: <https://www.langchain.com/> · <https://www.langchain.com/langsmith> · <https://academy.langchain.com>

## LangGraph — 상태 머신 도구로 언급 (2026-10-09 · [[tech-bridge-goodbye-slop-state-machines]])

[[david-khourshid|David Khourshid]](XState 제작자)가 에이전트 워크플로의 전이 로직 구현 선택지로 *"You could use LangGraph, I guess, which actually is um one of the uh most popular tools for using state machines with agents."*(15:48~15:54) — 경쟁 도구 제작자의 지나가는 평가, 근거 수치 없음. → [[agent-state-machine]]
