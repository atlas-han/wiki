---
title: Jake Broekhuizen
type: entity
category: person
tags: [langchain, agent-memory, langsmith, speaker]
links:
  - "https://www.linkedin.com/in/jake-broekhuizen/"
sources: [tech-bridge-langchain-learning-agent-memory]
created: 2026-10-12
updated: 2026-10-12
---

# Jake Broekhuizen

[[langchain|LangChain]] Labs의 리드(설명란 기준). 이 위키의 유일한 소스는 [[tech-bridge-langchain-learning-agent-memory]] — *관찰(observability)과 학습은 다르다*는 전제에서 에이전트 메모리의 분류(semantic · episodic · procedural, working vs long-term)와 **트레이스 → 메모리 순환**을 정리한 15:28 발표다.

> ⚠️ **신원 근거.** 이름과 직함 "LangChain Labs 리드"는 **영상 제목·설명란에만** 있다(LinkedIn 링크는 열어 보지 않았다). 자막에는 자기소개가 없고, 발화로 확인되는 소속은 *"the lab team at Langchain"*(00:28~00:30)과 *"I and and the team at Langchain"*(07:33~07:38)뿐이다.

## 위키에서 알려진 것

- 메모리 정의: *"the durable context that an agent references that will guide future runs"*(03:54~03:57) — 트레이스는 증거일 뿐, 교훈이 durable context로 바뀔 때만 메모리 → [[agent-memory]] · [[trace-to-memory-loop]]
- *"Procedural memory is where actually most of the visible gains come from"*(05:12~05:17) — 금융 도우미 말투 교정은 새 사실이 아니라 **규칙**이었다
- 순환: *"Memory informs the run. The run makes the evidence. We filter that evidence to make signal and then we use that signal to update memory."*(09:26~09:37) — 대부분의 증거는 history로 남긴다
- 세 교훈: 트레이스 대부분은 history(일부는 오프라인 eval 데이터셋) · 장시간 백그라운드 에이전트의 캐시/hot path 함정 · procedural 변경은 사람 검토 + eval로 보호(⚠️ *"about 75%"* 는 화자 추정)
- LangSmith(capture) → 분석 엔진(analyze) → Context Hub(update) 구현 소개 → [[langsmith]] (⚠️ 당사자 진술)

## 이 위키에서의 자리

[[lamis-mukta|Lamis Mukta]]([[anthropic|Anthropic]], dreaming) · [[ignacio-martinez|Ignacio Martinez]]([[oracle|Oracle]], 메모리 엔지니어링)에 이은 **세 번째 "메모리 인프라 벤더" 화자**. 셋 다 학습을 **컨텍스트 층**에서 한다([[continual-learning]]). 차별점은 사람 게이트를 **메모리 종류**(procedural)로 가른다는 것.

## References

- [[tech-bridge-langchain-learning-agent-memory]] · [[langchain]] · [[langsmith]] · [[agent-memory]] · [[trace-to-memory-loop]]
