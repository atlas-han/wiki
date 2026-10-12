---
title: LangSmith
type: entity
category: product
tags: [observability, tracing, agent-memory, context-hub, langchain, vendor]
aliases: [Langsmith, 랭스미스, LangSmith Context Hub, Context Hub, 컨텍스트 허브]
links:
  - "https://www.langchain.com/langsmith"
sources: [tech-bridge-langchain-learning-agent-memory, tech-bridge-jev-agent-harness]
created: 2026-10-12
updated: 2026-10-12
---

# LangSmith

[[langchain|LangChain]]의 에이전트 관측(observability)·평가 제품. 이 위키에서는 [[tech-bridge-jev-agent-harness]]의 설명란 링크(*Jev-as-a-Judge for Agent Evals*, LangSmith 경로)로만 있었고, [[tech-bridge-langchain-learning-agent-memory]](2026-10-11 업로드)가 **기능이 발화로 설명되는 첫 소스**다.

> ⚠️ 아래는 전부 **LangChain 사람([[jake-broekhuizen]])의 자사 제품 서술**이다. 화자 스스로 *"I won't I won't claim it's the only implementation"*(10:13~10:16)로 일반론과 분리했다. 효과 수치·고객사 이름은 없다.

## capture · analyze · update 의 세 칸 (10:13~11:27)

| 칸 | 구성 | en-orig |
|---|---|---|
| capture | 트레이싱 — 도구 호출, 서브에이전트 호출, 검색된 컨텍스트 | *"is where our observability comes in"*(10:28~10:30) |
| analyze | 트레이스에서 신호를 뽑는 백그라운드 분석 — *"something new that I'm really excited about"*(10:41~10:44) | *"that intelligent process that's doing the background analysis (…) to extract signal from traces based on the things that matter to you"*(10:44~10:51) |
| update | **Context Hub** — 에이전트가 다음 실행 때 내려받는 원격 스토어 | *"a remote store where you can now go and update what's in that so that the agent can pull that down the next time it runs"*(11:08~11:14) |

Context Hub에 담기는 것: *"its instructions, its skills, relevant markdown files that matter to it, policies and rules"*(11:42~11:51). 분석 엔진은 *"identifies where different static skill markdown files that are based in Contexthub need to be changed or promoted and it'll make that change"*(12:04~12:13).

- ⚠️ 분석 엔진의 제품명·출시 상태는 발화되지 않는다. 변경 승인 흐름도 이 구간엔 없다 — 같은 발표 끝의 *procedural 변경은 사람 검토*(14:23~14:47) 권고와 어떻게 맞물리는지 미발화.
- ⚠️ ASR: en-orig *"Langmith"*(10:22, 10:58), *"context sub"*(11:42), *"Contexthub"*(12:09). ko는 Context Hub를 **"컨텍스트 센터"**, *LangSmith's* 를 **"랭스미스 지음"** 으로 옮겼다.

## 이 위키에서의 자리

[[trace-to-memory-loop]]의 벤더 구현 하나. 같은 자리의 다른 구현: [[agent-dreaming]](Anthropic, 세션 밖 배치 + 사람 수락) · [[production-trace-eval-flywheel]](W&B Weave, 트레이스 → eval 태스크). 같은 날 ingest된 eval·관측 벤더 [[braintrust|Braintrust]]는 트레이스 저장·쿼리 자체를 systems problem으로 본다 → [[eval-platform-maturity-stages]]. [[uber|Uber]] [[debug-assist|Debug Assist]]는 LangChain 위에서 **Arize** 트레이싱을 썼다([[tech-bridge-uber-debug-assist]]) — LangChain 사용자가 LangSmith만 쓰는 것은 아니다.

## References

- [[tech-bridge-langchain-learning-agent-memory]] — first-seen (기능 설명, 1인칭)
- [[tech-bridge-jev-agent-harness]] — 설명란 링크만
- [[langchain]] · [[jake-broekhuizen]] · [[trace-to-memory-loop]]
- 외부: <https://www.langchain.com/langsmith> (⚠️ 열어 보지 않았다)
