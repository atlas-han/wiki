---
title: "모델 보정 (Model Calibration)"
type: concept
category: theory
tags: [calibration, probability, confidence, post-training, rlcd, rlhf, rlvr, thresholds, human-in-the-loop, system-1-model]
aliases: [calibration, 보정, 신뢰도 보정, calibrated probabilities, RLCD, reinforcement learning for calibrated decisions]
related: [bayesian-inference, aleatoric-epistemic-uncertainty, post-training-northstars, preference-reward-asymmetry, rlhf, verifiable-goals, system-1-model, jev, risk-proportional-human-review, decision-quality]
first-seen: tech-bridge-jev-calibrated-decisions
sources: [tech-bridge-jev-calibrated-decisions, tech-bridge-uncertainty-mathematics, tech-bridge-rlhf-assistance-vs-automation]
created: 2026-10-09
updated: 2026-10-09
---

# 모델 보정 (Model Calibration)

**모델이 "p의 확률로 맞다"고 할 때, 그런 답들 중 실제로 약 p만큼이 맞는 성질.** 보정된 확률은 정답 여부와 별개로 **"얼마나 믿어도 되는가"를 숫자로 전하고**, 그래서 코드가 임계값으로 자동 처리 / 사람 호출 / 무시를 나눌 수 있게 한다. 이 위키에는 사람의 예측 원칙으로 먼저 들어왔고([[bayesian-inference]], 09-05), 모델의 학습 목표로는 [[tech-bridge-jev-calibrated-decisions]](10-03 업로드, [[ibm|IBM]] 계열 해설)에서 **RLCD**라는 이름과 함께 들어왔다.

> *"when we say that there is a 80% probability that 80% probability is going to be correct about 80% of the time. That's calibration."* — [[tech-bridge-jev-calibrated-decisions]] (10:19~10:35)

> ⚠️ **모델 쪽 서술은 전부 한 회사([[typesafe-ai|TypeSafe]])의 주장을 거친 것이다.** 이 위키는 어떤 모델의 보정 곡선도 실측으로 본 적이 없다. 보정 품질 지표(ECE 등)·보정 실패 사례는 어느 소스에도 없다.

## 정의 — 대각선

x축에 모델이 말한 확률, y축에 실제 적중률을 그리면 **잘 보정된 모델은 대각선** 위에 놓인다(*"a wellc[=well-] calibrated model is going to have kind of a diagonal line"*, 10:12~10:19). 같은 정의가 사람의 예측에도 쓰인다 — *"비가 올 확률이 70%라고 예측했을 때 (…) 그중 70%는 실제로 비가 왔고"* ([[bayesian-inference]] · [[tech-bridge-uncertainty-mathematics]]).

**정확도와 다르다.** 오답을 낼 수 있는 모델도 보정될 수 있다 — *"the model can still pick the wrong options (…) but the probability tells us how likely that is"*(06:38~06:48).

## 왜 지금의 LLM은 보정되지 않는가 — post-training의 세 갈래

| 갈래 | 무엇을 보상하나 | 확신에 대해 | 출처 |
|---|---|---|---|
| **RLHF** | 사람이 고른 응답(reward model) | *"People tend to like answers that sound confident"* → **틀려도 확신에 찬 말투** | IBM 편 08:21~08:30 · Almeida의 [[preference-reward-asymmetry]](*확신 없음만 벌받는다*) |
| **RLVR** | 최종 답의 정오(수학 정답, 단위 테스트) | *"doesn't reward the model for knowing how sure it should be"* | IBM 편 09:02~09:09 · ⚠️ Almeida는 *"정확성의 로그 오류율"* — 아래 유보 |
| **RLCD** | **확률이 맞았을 때** | 확신의 크기 자체가 보상 대상 | IBM 편 09:21~09:48 — *"what they[=TypeSafe] have said"* |

그리고 LLM에게 확신도를 **말로 물어도** 소용없다 — *"whatever it responds with wouldn't necessarily actually match the real probabilities the model used to come up with its answer"*(03:54~04:02). → [[bayesian-inference]]의 *LLM은 왜 이것을 하지 못하는가* 와 같은 자리.

이 표는 [[post-training-northstars]]의 세 북극성(RLHF = 인간 선호 / RLVR = 정확성 / 제3 = 보정된 의사결정)과 **같은 셋**이다.

## 보정이 있으면 생기는 것 — 임계값이 오류율이 된다

> *"Because the numbers are calibrated, the threshold also tells us roughly how often the automatic path will be wrong. So the more a mistake is going to cost, the higher we would set the threshold."* (12:05~12:20)

[[tech-bridge-jev-calibrated-decisions]]의 예: 지원 이메일이 환불 요청일 확률 **> 0.9 → 환불 큐로 자동**, **0.1~0.9 → 사람 호출**, **< 0.1 → 무시**(10:45~12:05, 값은 화자의 예시). 확률이 보정돼 있지 않으면 같은 코드가 **임계값이 무엇을 보장하는지 모른 채** 돌아간다 — 09-26 [[system-1-model]] 페이지가 *"게이트 임계값을 정하려면 필수인 정보"* 로 비워 둔 칸이 이것이다.

→ [[risk-proportional-human-review]] — *위험이 큰 결정 곁에 사람을* 이 **실수 비용에 맞춰 올리는 임계값 하나**로 구현된다.

## ⚠️ 유보

- **실측이 없다.** RLCD의 손실 함수·데이터·보정 곡선 실측은 공개되지 않았다(*"TypeSafe haven't published much about Jev's architecture"*, 09:30~09:33).
- **RLVR과 확신 — 표현 충돌.** Almeida(09-19, ko 번역 기준)는 RLVR이 *"순수 정확성의 로그 오류율"* 을 최적화한다고 했다. 로그 손실은 원래 보정을 보상하는 채점 규칙(proper scoring rule)이므로, 문자 그대로면 IBM 편의 *"doesn't reward (…) how sure it should be"* 와 맞지 않는다. 두 화자가 TypeSafe의 같은 서사를 다르게 옮겼을 수 있다 — **미해소.**
- **보정 ≠ 분포 이동에 강함.** 학습 분포 밖 입력에서도 보정이 유지되는지, 프롬프트 인젝션(*"it can be tricked by instructions hidden in the data"*, 12:52~12:54)에서 확률이 어떻게 되는지 — 소스 없음. → [[aleatoric-epistemic-uncertainty]]
- **임계값 설계의 나머지 절반.** 화자는 *오류율 ↔ 임계값* 만 말하고, 사람 호출 구간(0.1~0.9)의 **물량**(사람이 감당할 수 있는가)은 말하지 않는다 — [[verification-bottleneck]]과 맞닿는 자리(⚠️ 위키의 관찰).

## References

- [[tech-bridge-jev-calibrated-decisions]] — first-seen (모델 학습 목표로서의 보정, RLCD)
- [[tech-bridge-uncertainty-mathematics]] · [[bayesian-inference]] — 사람의 예측 원칙으로서의 보정
- [[tech-bridge-rlhf-assistance-vs-automation]] · [[post-training-northstars]] · [[preference-reward-asymmetry]] — 제3의 북극성
- 관련: [[jev]] · [[typesafe-ai]] · [[system-1-model]] · [[rlhf]] · [[verifiable-goals]] · [[risk-proportional-human-review]] · [[aleatoric-epistemic-uncertainty]] · [[decision-quality]]
