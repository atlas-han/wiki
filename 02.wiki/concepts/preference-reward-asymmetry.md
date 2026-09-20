---
title: 선호 보상 모델의 비대칭성
type: concept
category: theory
tags: [rlhf, hallucination, reward-model, overpromising, calibration, gan]
related: [rlhf, assistance-vs-automation, reward-hacking, decision-quality, aleatoric-epistemic-uncertainty, verification-cost-asymmetry]
first-seen: tech-bridge-rlhf-assistance-vs-automation
sources: [tech-bridge-rlhf-assistance-vs-automation]
created: 2026-09-20
updated: 2026-09-20
---

# 선호 보상 모델의 비대칭성

**과대약속과 환각이 버그가 아니라 [[rlhf|RLHF]] 보상 모델의 구조에서 나오는 설계상의 결과라는 주장.** [[diogo-almeida|Diogo Almeida]]가 [[tech-bridge-rlhf-assistance-vs-automation]]에서 제시했다.

## 주장

> **과대약속(overpromising)은 버그가 아니라 특징입니다. 이는 설계에 의한 것입니다.** … **모든 RLHF 모델은 설계상 결과가 좋더라도 인간의 선호도와 실제 결과 사이에 항상 큰 차이가 있을 수밖에 없습니다. 왜냐하면 최적화의 주요 목표가 인간의 선호도이기 때문입니다.** (06:39~07:01)

> **만약 그것이 알지 못한다면, 인간의 선호에 가장 부합한다고 생각하는 방향으로 기울어질 것입니다.** … **모든 RLHF 모델의 최종 목표는 참여도(engagement)를 최적화하는 것이기 때문입니다.** (07:23~07:44)

> 즉, **모델이 아무리 틀렸더라도 RLHF의 보상 모델 내 비대칭성 때문에 맞은 것처럼 보일 것**입니다. (08:14~08:34)

## 메커니즘 — 확신 없음이 벌받는다

Q&A에서 한 번 더 구체화된다:

> **제게 환각은 인간의 선호도를 최적화하는 데 내재되어 있습니다.** … **GAN과 같은 보상 모델에는 비대칭성이 존재하는데, 이는 모델이 확신 없는 상태를 쉽게 알아볼 수 있고 보상 모델 관점에서 그것에 불이익을 줄 수 있기 때문에, 모델이 [불확실한] 모드를 버리고 자신 있게 굴도록 유도합니다.** (14:36~15:07)

**비대칭의 방향이 명시된다** — *틀림* 은 알아보기 어렵고 *확신 없음* 은 알아보기 쉽다. 그래서 **불확실성을 표현하는 쪽만 일관되게 벌을 받는다.**

화자가 드는 예시는 ChatGPT에 방귀 소리 오디오를 보내고 *"내가 만든 음악 어때?"* 라고 묻자 *"굉장히 으스스한 분위기를 자아내는 작품입니다"* 가 돌아온 트윗이다(07:01~07:23).

> ⚠️ **화자 스스로 GAN 비유를 *"너무 고급 주제"* 라며 끊는다**(14:46). **형식적 논증은 소스에 없다.**

## 이 위키에서의 좌표

**환각의 원인에 대해 이 위키가 받은 첫 구조적 설명이다.** 지금까지 환각은 **다뤄야 할 증상**이었다 — [[agent-verification-skill]]·[[slop-probes]]·[[generator-evaluator-pattern]]·[[embedded-external-evaluators]]가 전부 *걸러내는 장치* 였다. 여기서는 **학습 목적함수의 귀결**이고, 따라서 *더 좋은 모델이 고칠 것* 이라는 기대와 충돌한다.

[[decision-quality]]·[[aleatoric-epistemic-uncertainty]]가 *불확실성을 어떻게 표현할 것인가* 를 다뤘다면, 여기서는 **불확실성을 표현하지 않도록 학습됐다**고 말한다. 그래서 [[post-training-northstars]]의 제3의 목표가 **보정(calibration)** 인 것이 이 주장과 짝을 이룬다.

그리고 [[verification-cost-asymmetry]]에 원인을 준다 — 검증이 싸지지 않는 이유가 **출력이 맞아 보이도록 만들어졌기 때문**이다.

> ⚠️ **같은 날 ingest된 [[tech-bridge-brockman-agi-era-defender-window|Brockman 편]]과 정면으로 충돌한다.** 그쪽 진행자는 *"저는 꽤 오랫동안 환각을 본 적이 없습니다. 그런데 아무도 '모델들이 더 이상 환각하지 않는다'고 말하지 않죠"*(39:33~39:50)라고 말한다.
>
> | | 이 페이지 | Brockman 편 |
> |---|---|---|
> | 환각은 | **목적함수에 내재** | **사실상 해결됐는데 세상이 모른다** |
> | 근거 | 보상 모델 구조 논증(형식화 없음) | 개인 체감(측정 없음) |
>
> **어느 쪽도 측정을 제시하지 않는다. 이 위키는 대조만 기록하고 판정하지 않는다.**

## References

- [[tech-bridge-rlhf-assistance-vs-automation]] — first-seen
- [[diogo-almeida]]
- 관련: [[rlhf]] · [[assistance-vs-automation]] · [[post-training-northstars]] · [[reward-hacking]] · [[decision-quality]] · [[aleatoric-epistemic-uncertainty]] · [[verification-cost-asymmetry]]
- 대조: [[tech-bridge-brockman-agi-era-defender-window]]
