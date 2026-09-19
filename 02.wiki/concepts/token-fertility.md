---
title: 토큰 다산성 (Token Fertility)
type: concept
category: metric
tags: [tokenizer, multilingual, latency, model-selection, voice-agents]
aliases: [token fertility, 단어당 토큰 수]
related: [time-to-first-audio, voice-latency-thinking-tradeoff, gemma-4, qwen3-5, voice-agent-pipeline]
first-seen: tech-bridge-voice-agent-failure-modes
sources: [tech-bridge-voice-agent-failure-modes]
created: 2026-09-19
updated: 2026-09-19
---

# 토큰 다산성 (Token Fertility)

**어떤 언어에서 단어 하나를 만드는 데 토큰이 몇 개 드는가.** 토크나이저 평가의 지표이고, [[tech-bridge-voice-agent-failure-modes]]가 이 위키에 **모델 선택 기준으로** 들여왔다.

> 우리는 **token fertility 평가**를 봤습니다. 본질적으로 그 말은 — 전문 용어를 풀어서 설명한다면 — **그 언어에서 단어 하나를 생성하는 데 몇 개의 토큰이 필요한지 묻는 것**과 같다는 뜻입니다. (10:07~10:35)

*(⚠️ ko 자막은 이것을 "토큰식 출산율 평가"로 직역했다 — raw 헤더 참조.)*

## 왜 지연의 문제인가

토큰 생성 속도(tok/s)가 같아도 **같은 문장을 말하는 데 드는 토큰 수가 다르면 첫 소리까지의 시간이 다르다.** 그래서 다국어 음성 에이전트에서는 토크나이저가 **[[time-to-first-audio|TTFA]] 예산의 일부**가 된다.

> 그런 관점에서 보면 **Gemma는 [Qwen] 3.5보다 최소 2.5배에서 3배는 더 낫다**고 할 수 있죠. 따라서 다른 모든 조건이 동일하다면, **다국어 환경에서 Gemma 4를 사용하면 단어 처리 속도(time to words)가 훨씬 빠릅니다.** (10:35~10:55)

**결론이 조건부다:**

| 상황 | 권고 |
|---|---|
| **영어만** | [[qwen3-5\|Qwen 3.5]]·[[gemma-4\|Gemma 4]] **둘 다 괜찮다** |
| **다국어** | **Gemma 4** — token fertility가 2.5~3배 낫다 |

## 이 위키에서의 좌표

**토큰이 시간의 단위가 되는 첫 자리다.** 이 위키에서 토큰은 지금까지 **예산**이었다 — [[token-roles]]는 토큰을 역할로 나눴고, [[true-cost-to-perfect-answer]]는 합격률로 나눈 비용으로 쟀고, [[fixed-budget-alpha]]는 예산을 고정했다. 셋 다 **토큰 = 돈**이다.

여기서 토큰은 **초**다. 그리고 그 환산율이 **언어마다 다르다** — 같은 모델이 영어로는 예산 안에 들어오고 다른 언어로는 나간다.

이것은 [[gemma-4]] 페이지가 이미 가진 기록([[cerebras]] 위에서 페이지 생성 1.1초)과 **다른 이유로 같은 모델을 고른 두 번째 사례**다. 저기서는 *작업이 좁아서* 소형 모델이면 됐고, 여기서는 **토크나이저가 다국어에서 효율적이라서** 골랐다.

## ⚠️ 유보

- **어떤 언어들에서 쟀는지 없다.** 화자는 힌디어를 예로 들지만 fertility 수치가 어느 언어 집합의 평균인지 말하지 않는다.
- **2.5~3배의 측정 조건**(토크나이저 버전·코퍼스·단어 정의)이 없다.
- **모델 품질과 분리되지 않는다** — fertility가 낮아도 그 언어에서 응답 품질이 낮으면 의미가 없는데, 품질 비교는 없다.
- **출력만 다루고 입력을 다루지 않는다** — 프롬프트·전사 입력 쪽의 토큰 수도 지연과 비용에 들어간다.
- 이 지표가 **비용**에도 그대로 곱해진다는 점(API 과금은 토큰 단위)이 소스에서 연결되지 않는다.

## References

- [[tech-bridge-voice-agent-failure-modes]] — first-seen
- [[venky-b]] · [[plivo]] · [[gemma-4]] · [[qwen3-5]]
- 관련: [[time-to-first-audio]] · [[voice-latency-thinking-tradeoff]] · [[voice-agent-pipeline]] · [[token-roles]] · [[true-cost-to-perfect-answer]]
