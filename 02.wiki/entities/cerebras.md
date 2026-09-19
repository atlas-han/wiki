---
title: Cerebras
type: entity
category: org
tags: [inference, accelerator, low-latency]
links:
  - https://www.cerebras.ai
sources: [tech-bridge-agentic-sites, tech-bridge-voice-agent-failure-modes]
created: 2026-09-01
updated: 2026-09-19
---

# Cerebras

초고속 추론용 대형 칩을 만드는 하드웨어·추론 서비스 기업. 본 위키에서는 [[agentic-sites]]의 지연 예산을 성립시키는 구성 요소로 등장한다.

## 위키에서 알려진 사실

- [[adobe|Adobe]] [[tech-bridge-agentic-sites]] 측정 (예시 사이트 프롬프트 15개, promptfoo):
  - Cerebras + [[gemma-4|Gemma 4]] → 페이지 생성 평균 지연 **1.1초**
  - 2위 구성 → **4.6초**
- 라이브 디버그 판독: LLM 왕복 **1초**, **2,200–2,300 tok/s**.
- 의미: 이 정도 지연이면 **페이지 생성을 요청-응답 경로 안**에 넣을 수 있다. 사전 생성으로 도망갈 필요가 없어진다.

## 조달의 벽 (2026-09-19 · [[tech-bridge-voice-agent-failure-modes]])

앞 항목이 **속도가 되는가**의 증거였다면, [[plivo|Plivo]] 편은 **조달이 되는가**를 묻고 두 개의 벽을 세운다. [[groq|Groq]]와 한 묶음으로 언급된다.

> 이러한 플랫폼들은 잘 작동하지만, **최적의 지연 시간이나 첫 토큰 생성 시간을 확보하려면 전용 용량(dedicated capacity)이 필요하며, 이는 매우 비쌉니다.** … **최소 12개월 전에 예약해야 한다**고 말할 것입니다. **향후 12개월 동안 예약이 꽉 찼습니다.** (08:15~08:52)

1. **전용 용량의 가격** — 공유 용량으로는 최적 지연이 안 나온다.
2. **12개월 선예약**, 그리고 *"12개월 뒤 그 모델이 아직 쓸 만한가"* 라는 **모델 수명의 문제**.

두 번째가 [[harness-pruning]]의 **하드웨어 판본**이다 — 계약 기간이 모델 세대보다 길면 인프라 투자가 모델의 진화에 발목을 잡는다. Plivo의 결론은 **오픈소스 소형 모델 자체 호스팅**이었다.

⚠️ 가격·대기 기간은 **전언**이고 출처·시점이 없다. ⚠️ 양 트랙 자막에서 이름이 *"Cerebris"* 로 깨져 문맥 근거의 판독이다.

## References

- [[tech-bridge-agentic-sites]] · [[agentic-sites]] · [[gemma-4]]
