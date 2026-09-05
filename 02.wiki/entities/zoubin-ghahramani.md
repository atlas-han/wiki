---
title: Zoubin Ghahramani
type: entity
category: person
tags: [bayesian, uncertainty, deepmind, cambridge, machine-learning]
sources: [tech-bridge-uncertainty-mathematics]
created: 2026-09-05
updated: 2026-09-05
---

# Zoubin Ghahramani

케임브리지 대학 교수이자 [[google-deepmind|Google DeepMind]] 소속 연구자. **불확실성의 수학**에 기반한 지능을 30년간 주장해 왔다. [[tech-bridge-uncertainty-mathematics]]의 화자.

> ⚠️ **직함이 소스 안에서 갈린다.** 오프닝 내레이션은 *"a professor at Cambridge and **co-lead of frontier AI** at Google DeepMind"*, 채널 설명란은 *"케임브리지대 교수이자 **Google DeepMind Research VP**"* 라고 쓴다. **케임브리지 교수라는 부분만 두 곳이 일치**한다. 해소하지 않고 불일치를 기록한다.

## 위키에서 알려진 사실

### 이력 (소스에서 밝힌 것)

- 14~15세에 이미 AI를 하고 싶어했다. 학부는 **컴퓨터 과학 + 인지 과학**.
- 대학 1학년 여름, UPenn 전산학과장이자 전산언어학자 **Aravind Joshi**에게 아르바이트를 구하러 갔고, *Parallel Distributed Processing* 두 권을 읽고 설명하는 일을 받았다. **1986년** — 역전파 논문이 나온 해다.
- 1989년 학부 논문은 신경망 자연어 처리. *"만약 발표했더라면 아주 초기의 언어 모델 논문이 되었을 겁니다. 우리 모델이 아주 작으니까, **작은 언어 모델**이라고 부르자."*
- 하드웨어는 **Connection Machine**(65,000 프로세서). 훗날 *"제 주머니의 **픽셀 폰보다 실제로 느립니다**"* 라고 비교한다.
- 1990년대 초 신경망을 떠나 확률 모델로 갔다. **이유가 아이러니하다 — 이해했다고 생각했기 때문이다.** *"우리는 신경망을 이해했다고 생각했습니다. 훌륭한 **함수 근사기**라고 생각했습니다."* 본인 평가: *"**그러다 내가 일을 망쳐버렸어.**"*
- **Geoff Hinton**과 여러 해 함께 일했다 — *"딥러닝을 시도했지만, 단순한 신경망 대신 **확률 모델**을 사용했습니다. 우리는 **대규모 데이터에서 어떤 일이 발생하는지 제대로 파악하지 못했기 때문에 상황을 지나치게 복잡하게 생각**했습니다."*
- **2015년 Nature 논문** — 지능의 여러 측면이 *"**불확실성에 대한 신중한 확률적 표현**에 결정적으로 의존"* 한다는 주장.

### 입장

- **지능 → 의사결정 → 불확실성**이라는 순서로 논증한다. 불확실성은 정직함의 문제가 아니라 **의사결정의 전제조건**이다. → [[bayesian-inference]] · [[aleatoric-epistemic-uncertainty]]
- AGI 논쟁에서 **"새로운 아키텍처가 필요하다"** 진영. 단 상대 진영을 깎지 않는다 — *"그들의 생각이 **완전히 틀린 건 아니에요. 저도 완전히 맞는 건 아니고요.**"* → ⚠️ [[sutton-bitter-lesson]]과 정면 대비된다.
- 판돈으로 선을 긋는다 — 챗봇은 괜찮지만 **자율주행·의료 진단**에서는 *"확률을 정확하게 계산하는 것이 매우 중요"*.
- 목표는 인간 흉내가 아니다 — *"이상적으로는 그들이 **인간보다 훨씬 더 이성적**이었으면. **제 계산기가 큰 수를 곱하는 데 정말 능숙하길 바라는 것처럼.**"*
- 남은 과제 셋: **[[continual-learning]] · 에너지 효율(뇌 20W) · 데이터 효율**.
- 스스로 semantic entropy의 한계를 지적한다 — 데이터 분포를 신뢰도로 읽는 것은 *"일종의 **속임수**"*, *"**계산기를 속이고 싶지는 않겠죠.**"*

### 남긴 문장

> 중요한 모든 문제에 있어서, **오만하고 지나치게 자신만만한 AI 시스템보다는 자신이 모를 때를 아는 AI 시스템을 더 선호합니다.**

> 우리는 **트랜스포머 혁명** 같은 이야기를 많이 하지만, 사실 **1980년대 중반에 일어난 일은 진정한 혁명**이었습니다.

## 미해결 사항

- ⚠️ 이름 표기가 en-orig에서 네 갈래로 오인식된다("Zuben Garammani"/"Zubin"/"Zven"/"Zen"). 정확한 표기는 **채널 설명란**에서 왔다.
- 직함 불일치(위 참조) 미해소.
- 2015년 Nature 논문의 정확한 제목·공저자 미확인.
- 그가 *"지금 검토 중"* 이라 말한 새 아이디어의 내용은 소스에 없다 — *"아직 완벽하게 구체화된 것은 아닙니다."*

## References

- [[tech-bridge-uncertainty-mathematics]] · [[google-deepmind]]
- 관련: [[bayesian-inference]] · [[aleatoric-epistemic-uncertainty]] · [[continual-learning]] · [[sutton-bitter-lesson]]
