---
title: Continual Learning
type: concept
category: theory
tags: [learning, memory, catastrophic-forgetting, bayesian, agi]
related: [bayesian-inference, context-resets-and-compaction, in-context-learning, memex]
first-seen: tech-bridge-uncertainty-mathematics
sources: [tech-bridge-uncertainty-mathematics]
created: 2026-09-05
updated: 2026-09-05
---

# Continual Learning

**모델이 배포 이후에도 데이터 스트림을 받아 계속 갱신되는 학습.** [[zoubin-ghahramani|Zoubin Ghahramani]]가 AGI로 가는 길에 남은 과제 세 가지 중 첫째로 꼽는다 → [[tech-bridge-uncertainty-mathematics]].

## 현재 방식과의 대비

> 현재 우리가 모델을 학습시키는 방식은 **거대한 모델을 학습시킨 다음 제품에 사용하거나 출시하고, 몇 달 후에 또 다른 거대한 모델을 학습시키는** 식으로 반복하는 것입니다.

> 인간과 동물의 학습 방식과 비교해 보면, **우리는 끊임없이 학습합니다.** 우리는 기본적으로 끊임없이 **데이터 스트림을 받아들이고** 있으며, **뉴런 간의 연결 등을 끊임없이 조정**하고 있습니다.

진단이 한 단어로 나온다.

> 그들은 **심각한 기억상실증** 등과 같은 증상을 겪습니다.

## 베이즈와의 관계 — 이 페이지의 핵심

이 개념이 [[bayesian-inference]]와 이론적으로 연결된다는 주장이 소스의 가장 구체적인 기술적 진술이다.

> 학습을 분포라는 관점에서 생각해 보면, **사전 믿음이 있고, 데이터 포인트를 얻고, 그걸 업데이트하고, 사후 확률을 얻고, 또 다른 데이터 포인트를 얻고, 그걸 다시 업데이트**하는 과정이 반복되는 거죠.

> 알고 보니 그런 종류의 **Bayesian update는 continual learning이 가능하고, 이론상으로는 catastrophic forgetting을 겪지 않는다**고 합니다.

그리고 현재 기법들의 위치를 규정한다.

> 사실, 대규모 신경망에서 continual learning을 시도하는 **많은 방법들은 Bayesian update의 근사치에 불과**합니다.

즉 continual learning은 별개의 트릭이 아니라 **순차적 베이즈 갱신의 실용적 근사**라는 것이다. 이론적으로 옳은 절차는 이미 알려져 있고, 문제는 **계산 가능성**이다 — *"NP-complete 또는 NP-hard 문제처럼 풀기 어렵기 때문에 어떻게든 근사치를 구해야."*

## 함께 묶인 과제들

Ghahramani가 continual learning과 나란히 놓는 것이 둘 더 있다.

| 과제 | 소스의 근거 |
|---|---|
| **에너지 효율** | 사람 뇌는 약 **20와트**. ⚠️ 단 비교의 한계를 스스로 단다 — *"하나의 뇌는 **한 인간의 삶에서 얻은 단 하나의 경험**과 관련되어 있기 때문"* |
| **데이터 효율** | *"인간이나 동물의 학습 방식과 비교했을 때 **데이터 효율성이 엄청나게 떨어집니다.**"* |

아키텍처 가능성으로는 *"**매우 희소한(sparse) 신경망**을 포함하는 새로운 하드웨어 아키텍처"* 와 **소프트웨어·하드웨어의 공진화**를 든다. 현재의 두 도구는 *"**트랜스포머 모델과 확산 모델**"* 이라고 정리한다.

## 위키에서의 좌표

이 위키가 가진 "기억" 관련 페이지들은 **전부 추론 시점의 우회책**이었다.

| 페이지 | 어디서 기억을 다루는가 |
|---|---|
| [[context-resets-and-compaction]] | 컨텍스트 윈도 안 — 압축·재시작 |
| [[in-context-learning]] | 가중치를 바꾸지 않고 프롬프트로 |
| [[intent-md]] · [[ai-native-sdlc]] | 파일 시스템으로 외재화 |
| [[memex]] | 외부 지식 저장소 |
| **continual-learning** | **가중치 자체를 갱신** |

즉 이 개념은 나머지 넷이 **우회하고 있는 문제의 본체**다. 에이전트 엔지니어링이 컨텍스트·파일·메모리 상태로 메우는 자리를, 학습 이론 쪽에서 정면으로 다루면 이 이름이 된다.

⚠️ 다만 소스는 **연구 방향으로만** 제시한다. 구체적 기법·성과·타임라인은 나오지 않고, Ghahramani 본인도 새 아이디어에 대해 *"아직 완벽하게 구체화된 것은 아닙니다"* 라고 말한다.

## References

- [[tech-bridge-uncertainty-mathematics]] — first-seen
- [[zoubin-ghahramani]]
- 관련: [[bayesian-inference]] · [[context-resets-and-compaction]] · [[in-context-learning]] · [[memex]]
