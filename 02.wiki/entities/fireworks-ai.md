---
title: Fireworks AI
type: entity
category: org
tags: [inference-provider, open-models, fine-tuning, training-platform, inference-engine, cuda-kernels, speculative-decoding, hot-loading, vendor-pitch]
aliases: [Fireworks, Fireworks AI, Firework, FireAttention, fire attention]
links:
  - "https://fireworks.ai"
  - "https://docs.fireworks.ai/fine-tuning/managed-finetuning-intro"
sources: [tech-bridge-fireworks-train-to-deploy-open-models]
created: 2026-10-18
updated: 2026-10-18
---

# Fireworks AI

오픈 모델의 **추론(호스팅)과 학습(fine-tuning)을 한 플랫폼에서** 파는 회사다. [[tech-bridge-fireworks-train-to-deploy-open-models]]에서 applied machine learning 팀 일부를 이끄는 [[jetashree-ravi|Jetashree Ravi]]가 소개했다. 자기 규정은 *"It makes the whole process of you having to go through the continuous journey of training these open-source models as well as hosting these open-source models at scale much more easier and also much more cost-effective as well."*(02:13~02:25)이다. 이 위키에 처음 들어오는 **추론 제공자·학습 플랫폼 벤더**다. 링크는 설명란에서 가져왔고 열어 보지 않았다.

> ⚠️ 이 페이지의 사실은 모두 당사자 발표에서 왔다. 수치는 기준선·지표·기간이 발화되지 않았고 고객 쪽 진술은 없다.

## 규모 (자사 주장)

- *"we serve about 30 trillion tokens and it's increasing"*(03:02~03:06). 시간 단위가 없다. 바로 뒤의 *"at least 5 trillion tokens a day now with the GLM 5.2 release"*(03:13~03:16)로 보아 하루 단위로 읽힌다.
- *"more than 10,000 companies globally and process about 200k requests a particular second"*(03:18~03:24)
- *"we have raised around 327 million CDC a while ago and we are about 200 people"*(04:48~04:56). 통화 단위 없음, *"CDC"* 판독 보류.
- GPU는 *"we do partner with different cloud and neo cloud providers"*(12:22~12:27)

## 고객 사례 (자사 주장)

| 고객 | 발화 | 결과 |
|---|---|---|
| [[cursor\|Cursor]] | Composer 2를 *"trained and also hosted on our platform"*(03:39~03:43). hot loading은 *"a feature we implemented specifically for cursor"*(12:39~12:43) | *"13x faster inference"*(03:46~03:48). 비교 대상 미발화 |
| [[vercel\|Vercel]] | *"fine tune and also host the model"*(03:59~04:03) | *"40x latency improvement"*(04:04~04:06) |
| GenSpark | RFT, data set 정리, evaluator function 정의(04:29~04:35) | *"12% quality improvement"*(04:39~04:41) |

## 추론 — FireAttention

- 자체 추론 엔진 FireAttention과 자체 CUDA 커널(05:13~05:27). 고객의 입력·출력 토큰 수, prompt cache hit rate, latency 목표에 맞춰 커널까지 최적화한다고 한다(05:41~06:08).
- *"speculative decoding, disaggregation, quantization"*(06:19~06:22). speculative decoding의 draft model을 고객이 플랫폼에서 직접 학습할 수 있다(06:25~06:49). → [[speculative-decoding]]
- 배포 템플릿 *"throughput, fast, minimal"*(17:52~17:56)

## 학습 — 세 형태

| 형태 | 대상 | 특징 |
|---|---|---|
| Training Agent | 최근 들어온 PM·빌더 | data set + 설명 → 모델 선택·data set 정리·hyperparameter. ⚠️ **RFT 미지원**(10:28~10:30). 데모는 Qwen3 8B를 골라 SFT |
| 관리형 학습 | *"most of our customers"* | API·UI, 모델·data set·hyperparameter → 버튼. loss 대시보드, [[weights-and-biases\|W&B]] 내보내기, job clone |
| Training API | ML 엔지니어 | 자체 training loop와 loss function. 데모 없음, cookbook |

방법은 SFT·RFT·DPO다. *"nowadays, I think RFT has become extremely extremely popular"*(10:04~10:09). → [[open-model-customization-loop]]

## 학습·서빙 통합이라는 판매 논리

- 한 번 클릭 배포, 모니터링(토큰 수·cache hit rate·speculator), 체크포인트에서 재학습(11:43~12:13)
- **hot loading**: 새 체크포인트를 *"without any downtime"*(12:53~12:56)으로 교체
- **numerical fidelity**: 다른 플랫폼에서 학습하고 서빙하면 *"numerics is not always compatible"*(13:26~13:30). 같은 플랫폼이라 *"you won't find any numerical differences"*(13:39~13:42)

> ⚠️ 이 논리는 학습과 서빙을 한 벤더에 묶는 쪽을 편든다. [[tailscale|Tailscale]]의 층별 선택권 주장, [[openhands|OpenHands]] Brennan의 lock-in 비판과 긴장한다 → [[open-model-customization-loop]] "갈리는 것".

## References

- [[tech-bridge-fireworks-train-to-deploy-open-models]] · [[jetashree-ravi]] · [[tech-bridge]]
