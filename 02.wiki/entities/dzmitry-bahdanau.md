---
title: Dzmitry Bahdanau
type: entity
category: person
tags: [researcher, attention, machine-translation, deep-learning]
aliases: [드미트리 바흐다나우, Bahdanau]
sources: [tech-bridge-karpathy-transformers-stanford]
created: 2026-09-03
updated: 2026-09-03
---

# Dzmitry Bahdanau

*Neural Machine Translation by Jointly Learning to Align and Translate*(2014)의 제1저자. [[attention-mechanism|어텐션]]을 처음 제안한 사람으로, [[tech-bridge-karpathy-transformers-stanford]]에서 [[andrej-karpathy|Karpathy]]와 주고받은 이메일이 인용되며 이 위키에 등장한다.

> ⚠️ ko 자막은 이 이름을 "디미트리"·"데메트리"로 옮긴다. 표기는 채널 설명란의 **드미트리 바흐다나우**를 따랐다.

## 위키에서 알려진 사실

- **인코더 병목**(가변 길이 문장을 단일 고정 벡터에 욱여넣는 문제)을 풀려다 어텐션에 도달했다.
- 커서가 시퀀스를 훑는 아이디어들을 먼저 시도했으나 잘 되지 않았다.
- 돌파구는 **디코더 RNN이 커서를 어디 둘지 스스로 학습하게 하자**는 착상이었고, 그 착상의 출처가 개인적 경험이다.

  > 이건 제가 **중학교 때 영어를 배우면서 했던 번역 연습**에서 영감을 받은 거예요. 번역하는 동안 **시선은 원본 시퀀스와 번역 대상 시퀀스 사이를 오가게** 됩니다.

- 구현은 soft search를 **softmax + BiRNN 상태의 가중 평균**으로 표현한 것이었고 — *"놀랍게도 **첫 시도부터 제대로 작동했습니다.**"*
- 원래 이름은 **RNNsearch**였다. 더 나은 이름 *attention*은 공저자 **Yoshua Bengio**가 최종 교정 과정에서 붙였다.

Karpathy의 논평: 영어가 모국어가 아니라는 점이 **기계 번역 연구에서 오히려 유리하게 작용**했다는 것. 번역 학습자의 시선 이동이라는 신체적 경험이 아키텍처가 됐다.

## 미해결 사항

- 이후 경력·소속 미확인 — 이 위키에는 2014년 논문과 위 이메일 일화만 있다
- 이메일 전문은 공개되지 않았고, 강연에 인용된 발췌만 확인 가능

## References

- [[tech-bridge-karpathy-transformers-stanford]]
