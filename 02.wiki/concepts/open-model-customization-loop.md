---
title: "오픈 모델 맞춤 학습 루프 (Open Model Customization Loop)"
type: concept
category: pattern
tags: [open-models, fine-tuning, sft, rft, dpo, evaluator-function, data-flywheel, hot-loading, train-serve-parity, numerical-fidelity, vendor-lock-in]
aliases: [train-to-deploy loop, 학습-배포 루프, train host train host, 오픈 모델 맞춤 학습, 데이터 flywheel(가중치), hot loading, numerical fidelity, RFT, reinforcement fine-tuning]
related: [model-mixing-economics, continual-learning, production-trace-eval-flywheel, post-training-northstars, rlhf, verifiable-goals, speculative-decoding, inference-speed-as-capability, ai-engineer-vs-ml-researcher, company-knowledge-moat]
first-seen: tech-bridge-fireworks-train-to-deploy-open-models
sources: [tech-bridge-fireworks-train-to-deploy-open-models]
created: 2026-10-18
updated: 2026-10-18
---

# 오픈 모델 맞춤 학습 루프

**폐쇄형 모델을 API로 쓰는 대신 오픈 모델을 자기 데이터로 학습(SFT·RFT·DPO)해 서빙하고, 배포 후 지표와 피드백으로 체크포인트에서 다시 학습하는 반복 구조.** [[fireworks-ai|Fireworks AI]]의 [[jetashree-ravi|Jetashree Ravi]]가 이것을 AI 스택의 변화로 제시했다: *"the AI stack itself for most of our customers and users is shifting from let's just serve a model once once and that's done to a more continuous loop that is improving from training to inferencing the same open-source model itself."*(01:51~02:08, [[tech-bridge-fireworks-train-to-deploy-open-models]])

> ⚠️ 현재 소스는 하나이고 **학습·서빙 플랫폼 벤더의 발표**다. 루프가 실제로 얼마나 퍼졌는지, 한 바퀴의 비용과 주기는 발화되지 않았다.

## 전제 — 세 가지 사실

1. *"open-source models for the most part are production-ready"*(01:23~01:26). 근거는 GLM 5.2의 코딩 사용 경험 한 문장이다.
2. *"if open-source models don't like beat or match the quality of closed-source models, the differentiating factor comes from how you customize, train, and improve these open-source models"*(01:35~01:48)
3. 위 인용의 연속 루프.

전환의 동기는 비용과 성능이고(00:24~00:30), 전환의 병목은 품질이다: *"their biggest bottleneck or the gap is quality"*(07:03~07:05).

## 루프의 칸

| 칸 | 발화 |
|---|---|
| 학습 | SFT · RFT · DPO(09:58~10:04) |
| 배포 | *"one click away from deploying these models into production"*(11:43~11:47) |
| 모니터링 | *"the number of tokens, cache hit rate, how your speculator is working"*(11:51~11:59) |
| 피드백 | *"collect gather feedback from all the all the metrics that you have collected"*(11:59~12:04) |
| 재학습 | *"retrain on the same platform (…) from the checkpoint that you were using to a new checkpoint"*(12:06~12:13) |
| 교체 | hot loading — 새 체크포인트를 *"without any downtime"*(12:53~12:56) |

⚠️ 피드백이 무엇이고 어떻게 학습 데이터가 되는지는 비어 있다. 모니터링 지표는 서빙 지표이고 품질 지표가 아니다.

## 학습 방법과 진입로

- **SFT · RFT · DPO**가 모두 제품 옵션이다. *"nowadays, I think RFT has become extremely extremely popular"*(10:04~10:09).
- **RFT의 어려운 자리는 평가 함수다.** 벤더가 직접 돕는 일이 *"define a good evaluator function, clean the data set, (…) choose the right hyper parameters especially for RFT"*(10:12~10:26)이다. 고객 사례(GenSpark)도 같은 세 가지(data set 정리, evaluator function, RFT)였다(04:29~04:41, ⚠️ *"12% quality improvement"*는 지표 미발화). → [[verifiable-goals]] · [[post-training-northstars]](검증 가능한 보상)
- **진입로가 사용자층으로 나뉜다**: 에이전트(입문 PM·빌더) → 관리형 학습(대부분의 고객) → Training API(ML 엔지니어가 loop·loss를 직접). → [[ai-engineer-vs-ml-researcher]]
- ⚠️ 가장 인기 있다는 RFT는 가장 쉬운 진입로(Training Agent)에서 지원되지 않는다(10:28~10:30). 공백은 사람의 지원이 메운다.

## 루프를 받치는 서빙 쪽 조건

- **hot loading**: *"when you have a new checkpoint, uh you you can directly go to live deployment without any downtime itself"*(12:48~12:56). Cursor용으로 만든 뒤 일반에 열었다고 한다(12:39~12:46).
- **train-serve 수치 일치(numerical fidelity)**: *"customers use platform A for training and host on platform B. But what happens when you do that is you'll have issues in quality of the model. And the reason you have those issues is numerics is not always compatible"*(13:16~13:30). ⚠️ 원인·사례·크기는 발화되지 않았다.
- **draft model도 루프에 든다**: speculative decoding의 draft model을 같은 방식으로 학습하고 모니터링한다. → [[speculative-decoding]]

## 이 위키에서의 좌표

- [[model-mixing-economics]]: 기존 사례는 오픈 모델을 **골라서 싼 실행 모델로** 쓴다(Kimchi *"open source for the rest"*, Factory *"10 to 30x cheaper"*). 이 패턴은 오픈 모델을 **학습해서 품질 격차를 닫는다**. 고르기에서 고치기로 한 걸음 더 간다.
- [[continual-learning]]: 이론 쪽 continual learning은 데이터 스트림으로 가중치를 계속 갱신하는 것이다. 이 루프는 **체크포인트 단위의 주기적 재학습**이고 forgetting을 다루지 않는다. 그 사이의 실무 근사다.
- [[production-trace-eval-flywheel]]: 같은 flywheel이지만 그쪽은 트레이스를 **eval 태스크**로 바꿔 하네스를 고친다. 이쪽은 피드백을 **가중치**로 되돌린다. RFT의 evaluator function이 두 루프를 이을 수 있는 자리다(소스는 말하지 않는다).
- [[company-knowledge-moat]]: "자기 데이터로 학습한 모델"은 회사 고유 지식을 컨텍스트가 아니라 가중치에 넣는 쪽이다.

## 갈리는 것

> ⚠️ **긴장: 루프를 한 벤더 안에 닫을 것인가.** numerical fidelity와 한 번 클릭 배포는 학습과 서빙을 같은 플랫폼에 두라는 논리다(13:09~13:58). [[tech-bridge-tailscale-aperture-ai-without-lock-in|Tailscale 편]]은 층마다 선택권을 지키라 하고 벤더 통합을 오답으로 놓았다. [[tech-bridge-openhands-sandboxing-coding-agents|OpenHands 편]]은 GitHub Actions를 *"proprietary standard"*라고 비판했다. 오픈 모델로의 전환이 폐쇄형 공급자에게서 벗어나는 것이라면, 이 패턴은 **학습·서빙 층에서 다시 묶일 수 있다.** 수치 불일치 주장은 검증되지 않았다.

## ⚠️ 유보

- 소스 하나, 벤더 발표. 고객 수치(13x·40x·12%)는 기준선·지표가 없다.
- 루프 한 바퀴의 비용·주기, 재학습이 회귀를 낳을 때의 처리(롤백·eval 게이트)는 발화되지 않았다.

## References

- [[tech-bridge-fireworks-train-to-deploy-open-models]] · [[fireworks-ai]] · [[jetashree-ravi]]
