---
title: "선택적 능력 억제 (Differential Capability Limitation)"
type: concept
category: technique
tags: [ai-safety, frontier-model, training, automated-ai-research, recursive-self-improvement, anthropic]
aliases: [일부러 덜 키운 능력, 과속 방지턱, capability limitation, 능력 억제]
related: [automated-ai-research, pacing-the-frontier, jagged-capability-frontier, fable-5-2, claude-mythos-preview, agent-sandboxing]
first-seen: tech-bridge-claude-fable-5-2-announcement
sources: [tech-bridge-claude-fable-5-2-announcement]
created: 2026-11-11
updated: 2026-11-11
---

# 선택적 능력 억제

**모델을 훈련할 때 특정 능력, 여기서는 AI 개발 자체를 가장 직접적으로 앞당길 연구 능력만 골라 덜 키우고, 나머지 능력은 그대로 키우는 조치.** [[anthropic|Anthropic]]이 [[fable-5-2|Claude Fable 5.2]] 발표문에서 밝혔다고 [[tech-bridge-claude-fable-5-2-announcement]]가 전한다. 해설자는 이것을 *"과속 방지턱"* 으로 부른다.

> ⚠️ **한 소스, 벤더 발표문의 2차 전달이다.** 조치의 방법(데이터 · 보상 · 평가 중 무엇을 바꿨는지)은 해설에 없다. 개념도 그래프도 *"발표문 설명을 옮긴 개념도"* 라고 설명란이 밝힌다. 이름은 위키가 붙였다.

## 무엇을 덜 키웠나

> *"훈련 과정에서 AI 개발을 가장 직접적으로 앞당길 수 있는 연구 능력은 덜 발전하도록 조치했다. 구체적으로는 가속기 커널 최적화 그리고 언어 모델 구조를 개선하는 능력입니다."*(05:56~06:07)

- 이 두 분야에서 Fable 5.2는 [[claude-opus-5-5|Opus 5.5]]와 비슷한 수준에 머문다(06:07~06:10).
- 반대로 *"에이전트 코딩, 하드웨어 개발, 기존 머신 러닝 연구에는 영향이 없도록 했다고 밝혔죠."*(06:10~06:16)
- 해설자의 요약: *"AI가 AI를 더 빨리 만드는 길목에만 과속 방지턱을 놓은 셈입니다."*(06:16~06:21)

## 다른 안전 층과의 구분

같은 발표에 안전 층이 셋 나온다. 이 개념은 그중 **훈련 층**이다(위키의 정리).

| 층 | 무엇을 나누나 | 이 발표의 형태 |
|---|---|---|
| **훈련** — 이 페이지 | 무엇을 키우는가 | AI R&D를 앞당기는 두 능력만 덜 키움 |
| 배포 | 누가 쓰는가 | Fable(안전장치) / Mythos(심사 통과 기관) — [[claude-mythos-preview]] |
| 평가 · 감시 | 무엇을 확인하는가 | 훈련 중 모니터링, 외부 기관 테스트, 해석 기법(06:53~07:01) — [[agent-sandboxing]] |

## 위키의 다른 페이지와 맞닿는 자리

- [[automated-ai-research]] — 이 위키는 에이전트가 *모델 훈련을 더 빠르게 만드는 방법* 을 찾는 시도를 기록해 왔다. 이 조치는 **바로 그 능력**을 프론티어 모델에서 억누른다. 같은 능력을 한쪽은 측정하고 한쪽은 억제한다.
- [[pacing-the-frontier]] — [[openai|OpenAI]]의 원칙어(능력의 속도를 안전 기준에 묶는다)와 같은 방향이다. 차이는 이쪽이 **특정 능력을 지목한다**는 점이다(위키의 읽기).
- [[jagged-capability-frontier]] — 들쭉날쭉한 경계가 보통은 *결과* 로 생긴다. 여기서는 **의도한 함몰**이다. 벤치마크 표만 보는 사용자는 두 경우를 구분하기 어렵다.

## ⚠️ 미해결

- 억제가 **얼마나 단단한지**(파인튜닝 · 스캐폴딩으로 되살릴 수 있는지)는 해설에 없다.
- 같은 발표가 *평가 인식* 증가를 고백한다 — *"시험인 줄 아는 모델이 실전에서도 똑같이 행동할지 판단하기가 더 어려워졌다는 뜻입니다."*(06:29~06:32) 억제 효과를 **평가로 확인하는 일**도 그만큼 어려워진다(위키의 읽기).

## References

- [[tech-bridge-claude-fable-5-2-announcement]] — 2026-11-10, §7 *일부러 덜 키운 능력*
