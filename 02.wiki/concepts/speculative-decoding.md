---
title: "Speculative Decoding (추측 디코딩)"
type: concept
category: technique
tags: [inference-optimization, latency, throughput, draft-model, speculator, serving]
aliases: [speculative decoding, 추측 디코딩, draft model, speculator, 드래프트 모델]
related: [inference-speed-as-capability, open-model-customization-loop, model-mixing-economics]
first-seen: tech-bridge-fireworks-train-to-deploy-open-models
sources: [tech-bridge-fireworks-train-to-deploy-open-models]
created: 2026-10-18
updated: 2026-10-18
---

# Speculative Decoding

**작은 draft model(speculator)이 다음 토큰들을 먼저 제안하고 main model이 그것을 검증해, 출력 분포를 유지하면서 생성 속도를 올리는 추론 최적화 기법.** 이 위키에는 [[tech-bridge-fireworks-train-to-deploy-open-models]]에서 처음 나왔다. 화자 [[jetashree-ravi|Jetashree Ravi]]([[fireworks-ai|Fireworks AI]])는 이것을 disaggregation·quantization과 함께 *"the very well-known techniques in the AI field"*(06:14~06:22)로 묶는다.

> ⚠️ 위 정의의 원리(제안 → 검증)는 **소스에서 발화되지 않았다.** 일반적인 설명이고 이 위키의 다른 소스로 확인하지 않았다. 소스가 말하는 것은 아래의 운영 측면이다.

## 소스가 더하는 것 — draft model도 학습 대상이다

- *"In terms of speculative decoding itself, we also allow customers to train their draft models on our platform. Uh so they can even upload the data set very similar to how they do for fine-tuning for training a draft model"*(06:22~06:37)
- 효과는 조건부다: *"which helps them uh make the model the main model perform much faster, uh meet latency requirements, also gives you better throughput if the draft model is trained uh very well."*(06:37~06:49)
- 배포 후 모니터링 지표에 *"how your speculator is working if you've trained a speculator"*(11:55~11:59)가 들어간다.

즉 speculative decoding이 서빙 쪽 스위치가 아니라 **워크로드별로 학습·관측하는 부품**으로 다뤄진다. draft model이 main model의 출력을 잘 맞힐수록 이득이 커지므로, main model을 맞춤 학습하면 draft도 따라 학습하는 것이 자연스럽다 → [[open-model-customization-loop]].

## 이 위키에서의 좌표

- [[inference-speed-as-capability]]: Altman은 속도를 모델 공급자의 새 축으로 말했다. 이 기법은 **같은 모델을 더 빠르게** 내는 서빙 층의 수단이다.
- [[model-mixing-economics]]: 작은 모델과 큰 모델을 함께 쓰지만, 작업을 나누는 라우팅이 아니라 **한 생성 안에서** 작은 모델이 큰 모델을 보조한다.

## ⚠️ 유보

- 가속 배율, 수용률(acceptance rate), 어떤 워크로드에서 이득이 큰지는 발화되지 않았다.
- disaggregation·quantization은 이름만 나왔다.

## References

- [[tech-bridge-fireworks-train-to-deploy-open-models]] · [[fireworks-ai]]
