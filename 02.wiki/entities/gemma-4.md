---
title: Gemma 4
type: entity
category: model
tags: [google, open-weights, small-model, inference]
sources: [tech-bridge-agentic-sites, tech-bridge-voice-agent-failure-modes]
created: 2026-09-01
updated: 2026-09-19
---

# Gemma 4

Google의 Gemma 계열 모델. [[tech-bridge-agentic-sites]] 강연 시점 기준 **"지난주 발표"** 로 소개된다 (강연 업로드 2026-08-31).

## 위키에서 알려진 사실

- [[cerebras|Cerebras]] 칩에서 실행해 [[agentic-sites]] 페이지 생성 **평균 1.1초**, **2,200–2,300 tok/s**.
- 이 사용 사례의 논점은 크기가 아니라 **작업의 좁음** — 텍스트 생성 + 블록 배치 선택에는 프론티어 모델이 필요 없다는 [[carlos-sanchez]]의 주장을 뒷받침하는 자리.
- [[sutton-bitter-lesson]]의 스케일 우위와 대비해 읽을 수 있으나, 대상 작업이 **선택**이라는 단서가 붙는다.

## 다국어 음성 에이전트의 선택 근거 (2026-09-19 · [[tech-bridge-voice-agent-failure-modes]])

[[plivo|Plivo]]가 보이스 에이전트의 LLM 층으로 **Gemma 4를 다국어 기본값**으로 쓴다. 근거가 성능이 아니라 **토크나이저**다.

> 우리는 **token fertility 평가**를 봤습니다. … **그 언어에서 단어 하나를 생성하는 데 몇 개의 토큰이 필요한지** … **Gemma는 [Qwen] 3.5보다 최소 2.5배에서 3배는 더 낫다**고 할 수 있죠. 따라서 … **다국어 환경에서 Gemma 4를 사용하면 단어 처리 속도가 훨씬 빠릅니다.** (10:07~10:55)

- **영어만이면 [[qwen3-5|Qwen 3.5]]와 둘 다 괜찮다.** 갈리는 것은 다국어다.
- 목표는 **300ms 미만** — 프런티어 API의 꼬리 지연(P90·P95 1.2~1.3초)과 [[cerebras]]·[[groq]]의 전용 용량 조달을 둘 다 피한 선택이다.
- → [[token-fertility]] · [[time-to-first-audio]] · [[voice-agent-pipeline]]

**이 위키가 Gemma 4를 고른 이유를 기록한 두 번째 자리**이고 이유가 다르다 — [[tech-bridge-agentic-sites]]에서는 *작업이 좁아서* 소형 모델이면 됐고, 여기서는 **다국어 토큰 효율**이다.

⚠️ 어떤 언어들에서 어떻게 쟀는지, 2.5~3배의 측정 조건이 없다. ⚠️ fertility와 **응답 품질**이 분리되지 않는다.

## References

- [[tech-bridge-agentic-sites]] · [[cerebras]] · [[agentic-sites]]
