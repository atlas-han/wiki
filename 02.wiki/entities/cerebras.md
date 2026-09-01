---
title: Cerebras
type: entity
category: org
tags: [inference, accelerator, low-latency]
links:
  - https://www.cerebras.ai
sources: [tech-bridge-agentic-sites]
created: 2026-09-01
updated: 2026-09-01
---

# Cerebras

초고속 추론용 대형 칩을 만드는 하드웨어·추론 서비스 기업. 본 위키에서는 [[agentic-sites]]의 지연 예산을 성립시키는 구성 요소로 등장한다.

## 위키에서 알려진 사실

- [[adobe|Adobe]] [[tech-bridge-agentic-sites]] 측정 (예시 사이트 프롬프트 15개, promptfoo):
  - Cerebras + [[gemma-4|Gemma 4]] → 페이지 생성 평균 지연 **1.1초**
  - 2위 구성 → **4.6초**
- 라이브 디버그 판독: LLM 왕복 **1초**, **2,200–2,300 tok/s**.
- 의미: 이 정도 지연이면 **페이지 생성을 요청-응답 경로 안**에 넣을 수 있다. 사전 생성으로 도망갈 필요가 없어진다.

## References

- [[tech-bridge-agentic-sites]] · [[agentic-sites]] · [[gemma-4]]
