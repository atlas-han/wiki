---
title: Harrison Chase
type: entity
category: person
tags: [langchain, agent-framework, evals, traces, vendor]
aliases: [Harrison Chase, 해리슨 체이스]
links: []
sources: [tech-bridge-harrison-chase-agent-improvement-loop]
created: 2026-10-30
updated: 2026-10-30
---

# Harrison Chase

[[langchain|LangChain]] 쪽 화자. 이 위키에는 [[tech-bridge-harrison-chase-agent-improvement-loop]](2026-10-29 업로드)로 처음 등장한다.

> ⚠️ **신원은 태그 근거다.** 그 영상의 발화 · 제목 · 설명란에는 이름이 없고 info.json `tags`에만 `Harrison Chase` · `LangChain`이 있다. 발화 단서는 하네스 예시 *"deep agents"*(LangChain 제품명)와 traces · evals를 두고 한 *"it's where we spend a lot of time"* 정도다. 직함(공동창업자 · CEO 등)은 어느 소스에서도 발화되지 않아 적지 않는다.

## 위키에서의 진술

- **에이전트 = 모델 + 하네스 + 컨텍스트**, 셋 다 개선 대상. 모델은 SFT, 하네스는 코드 · 프롬프트 · 도구(전파 범위 때문에 사람 검토), 컨텍스트는 텍스트(사용자 · 조직 단위 메모리) → [[model-harness-knowledge-stack]] · [[continual-learning]]
- 공통 토대는 **트레이스와 eval**. *"evals are the new PRD"* (인용한 격언), 판정 대상은 최종 답 · 환경 최종 상태 · 도구 호출 순서 → [[production-trace-eval-flywheel]]
- *"We don't have a universal judge for correctness."* — 믿을 만한 판정기가 있다면 이미 에이전트 루프 안에 있을 것이라는 논리.
- 에이전트가 스스로 eval을 만들고 고치는 루프는 *"very much a North Star vision"* → [[skill-self-improvement]]

## References

- [[tech-bridge-harrison-chase-agent-improvement-loop]]
- 관련: [[langchain]] · [[jake-broekhuizen]](같은 회사, 메모리 편)
