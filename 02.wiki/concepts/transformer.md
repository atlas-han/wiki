---
title: Transformer
type: concept
category: architecture
tags: [architecture, deep-learning, attention, gpu, scaling]
aliases: [트랜스포머, Transformer 아키텍처]
related: [attention-mechanism, in-context-learning, sutton-bitter-lesson, nanogpt, context-resets-and-compaction]
first-seen: tech-bridge-karpathy-transformers-stanford
sources: [tech-bridge-karpathy-transformers-stanford, tech-bridge-uncertainty-mathematics]
created: 2026-09-03
updated: 2026-09-05
---

# Transformer

2017년 *Attention Is All You Need*가 제안한 신경망 아키텍처. 이 위키의 거의 모든 소스가 그 위에서 돌아가는 모델을 다루지만, **아키텍처 자체를 설명한 소스는 [[tech-bridge-karpathy-transformers-stanford]]가 처음**이다.

> ⚠️ 이 페이지의 서술은 ~2023년 강연에 근거한다. "5년간 안 바뀌었다" 같은 진술의 기준 시점은 2023년이다.

## 왜 이겼는가 — 세 속성의 동시 최적화

[[andrej-karpathy|Karpathy]]의 핵심 주장은 트랜스포머가 **하나를 잘해서가 아니라 셋을 동시에 만족**해서 이겼다는 것이다.

| # | 속성 | 무엇이 그것을 주는가 |
|---|---|---|
| 1 | **표현력 (expressive)** | forward pass가 아주 흥미로운 함수를, 심지어 [[in-context-learning\|meta-learning]]까지 구현 가능 |
| 2 | **최적화 가능성 (optimizable)** | residual connection, LayerNorm |
| 3 | **효율성 (efficient)** | 계산 그래프가 **shallow and wide** → GPU 병렬성에 부합 |

3번이 이 프레임의 요점이다.

> 3번이 덜 이야기되지만 극도로 중요합니다. 딥러닝에서는 스케일이 중요하고 (…) **현재 하드웨어에서 효율적이면 더 크게 만들 수 있습니다.**

> 저는 트랜스포머가 **GPU에서 효율적으로 돌아가도록 아주 의도적으로 설계**되었다고 생각합니다. (…) **하드웨어의 제약에서 거꾸로 생각하는** 방식이거든요.

### RNN과의 대비

세 속성을 한 번에 보여주는 대조군. RNN은 원리적으로 임의 프로그램을 표현할 수 있지만 — *"어느 정도 쓸모없는 진술"* — 최적화가 안 되고 효율적이지도 않다. **직렬 연산 장치**이기 때문이다.

| | 계산 그래프 | supervision→입력 hop | 병렬성 |
|---|---|---|---|
| **RNN** | 길고 가늘다 | 많다 | 없음 (순차) |
| **Transformer** | **얕고 넓다** | 적다 (residual 경유) | 전 토큰 동시 |

## 구조 — 통신과 연산의 교대

트랜스포머 블록은 두 단계를 번갈아 쌓은 것이다.

| 단계 | 연산 | 범위 |
|---|---|---|
| **통신 (communication)** | multi-head [[attention-mechanism\|attention]] | 노드 **사이** |
| **연산 (compute)** | MLP (2층 + GELU) | 각 노드 **안** |

> **Heads는 병렬 복사 붙여넣기, Layers는 직렬 복사 붙여넣기입니다.**

부속 요소들 — positional encoding(어텐션은 집합 위에서 작동하므로 필수), residual pathway, LayerNorm, MLP 확장 계수 **4x**.

## 세 변종은 한두 줄 차이

이것이 "그래프 통신" 관점의 실질적 이득이다. 아키텍처 선택이 **연결성 선택**으로 환원된다.

| 변종 | 예 | 구현 차이 |
|---|---|---|
| **Encoder-only** | BERT | causal 마스킹 **줄을 지운다** → 전 노드 완전 연결 |
| **Decoder-only** | GPT | 삼각 마스킹 유지 |
| **Encoder-decoder** | T5 | **cross-attention 한 줄 추가** (query는 자기, key·value는 인코더 top) |

> 인코더를 원하면 그냥 그 줄을 지우세요. 그게 다입니다.

BERT류는 autoregressive 대신 masking·denoising 목적함수로 학습한다.

## 아키텍처의 내구성

> 오늘날 여러분이 보고 있는 모든 것은 기본적으로 5년 전인 2017년 아키텍처입니다. **모든 사람들이 그것을 바꾸려 하고 있음에도 불구하고 놀라울 정도로 회복력이 강합니다.**

살아남은 유일한 변경으로 **pre-norm**(LayerNorm을 블록 앞으로)을 꼽는다. 예외적으로 positional encoding 계열(rotary, relative)은 실제로 교체됐다.

논문의 성격에 대한 관찰도 남길 만하다 — 보통 논문은 한 가지를 더하는 점진적 개선인데, 이 논문은 **여러 요소를 동시에 조합해 아키텍처 공간의 좋은 local minimum**에 도달했다. 저자들조차 *"당시 트랜스포머가 갖게 될 영향력을 몰랐습니다."*

## 모든 modality로 복사-붙여넣기

| 분야 | 방법 |
|---|---|
| **ViT** (이미지) | 패치로 썰어 노드로 투입 |
| **Whisper** (음성) | mel spectrogram을 조각으로 — *"copy-paste 트랜스포머"* |
| **Decision Transformer** (RL) | state·action·reward를 **언어인 척** 모델링 |
| **AlphaFold** (단백질) | 계산적 심장부에 트랜스포머 |

발표자 본인이 이 방식을 *"솔직히 좀 우스꽝스럽다"*고 평가하면서도 작동한다고 인정한다.

### 이질적 입력을 섞는 법

Tesla 경험에서 나온 실무 관찰. ConvNet에 radar·지도·차종을 넣으려면 *"어디에 넣지? concat하나? 더하나? 어느 단계에?"* 가 매번 설계 문제였다.

> 원하는 걸 뭐든 조각으로 썰어 기존 집합과 함께 넣고, **self-attention이 어떻게 소통해야 할지 알아내게 두면 됩니다.**

> 이건 신경망을 **Euclidean 공간의 부담에서 해방**시킵니다. (…) 어텐션에서는 **모든 게 그냥 집합**입니다.

출처를 알리려면 **학습 가능한 특수 임베딩 토큰**을 붙인다. 위치는 하드와이어(sin·cos)할 수 있지만 학습되는 벡터가 낫다.

## 범용 컴퓨터라는 재명명

발표자는 논문 제목을 바꾸고 싶다고 말한다 — **"범용의, 효율적이고, 최적화 가능한 컴퓨터"**.

> 이전의 신경망들은 **특정 과제를 위해 설계된 특수 목적 컴퓨터**입니다. **GPT는 런타임에 재구성되어 자연어 프로그램을 실행하는 범용 컴퓨터입니다. 프로그램은 프롬프트로 주어지고, GPT는 문서를 완성함으로써 그 프로그램을 실행합니다.**

이 위키가 [[context-engineering]]·[[token-roles]]에서 다루는 "프롬프트 설계"가 왜 프로그래밍처럼 느껴지는지에 대한 아키텍처 층위의 답이다.

## 두 번의 수렴

역사 서술의 구조. 2012년 AlexNet이 **툴킷**을 수렴시켰고(모두가 신경망·옵티마이저를 씀 → 분야 간 논문을 읽게 됨), 2017년 트랜스포머가 **아키텍처**를 수렴시켰다(하나를 복사해 어디든 붙임 → 바뀌는 건 데이터 써는 방식뿐).

추측이지만 발표자가 흥미로워하는 힌트: 대뇌 피질이 청각·시각을 가리지 않고 균일하다는 점이 *"우리가 뇌가 하는 어떤 일로 수렴하고 있다"* 는 신호일 수 있다는 것. 세부 차이는 *"트랜스포머의 하이퍼파라미터처럼"* 느껴진다.

## 알려진 한계 (강연 기준)

- **유한한 컨텍스트 길이** — block size를 넘으면 crop. 순진한 구현에서는 아키텍처가 아니라 학습 조건이 상한을 정한다. → [[context-resets-and-compaction]], scratch pad 논의
- **autoregressive 커밋** — *"토큰을 샘플링하고 거기에 커밋해 버리는 게 이상하다"*. 발표자는 diffusion 하이브리드를 선호한다고 밝힌다
- **full attention의 비효율** — 국소/전역 통신 레이어를 교대 배치하는 트릭들이 쓰인다

## 앞선 층 — 1980년대 신경망 혁명 (2026-09-05 · [[tech-bridge-uncertainty-mathematics]])

[[zoubin-ghahramani|Zoubin Ghahramani]]가 이 페이지의 계보에 **한 층 앞을** 붙인다. 그는 트랜스포머 혁명이라는 프레이밍 자체에 유보를 단다.

> 우리는 **트랜스포머 혁명** 같은 이야기를 많이 하지만, 사실 **1980년대 중반에 일어난 일은 진정한 혁명**이었고, 인지과학·컴퓨터과학·심리학·신경과학·경제학 분야의 사람들을 끌어들였습니다.

기준점은 **1986년**이다 — *Parallel Distributed Processing* 두 권과 역전파 논문이 같은 해에 나왔고, 당시 지배 패러다임이던 **전문가 시스템**의 규칙 기반 접근은 *"상당히 취약"* 했다. 신경망이 이긴 이유는 *"**데이터로부터 학습**"* 이었다.

그의 1989년 학부 논문은 신경망 자연어 처리였다.

> 만약 발표했더라면 **아주 초기의 언어 모델 논문**이 되었을 겁니다. 우리 모델이 아주 작으니까, **작은 언어 모델(small language model)** 이라고 부르자.

하드웨어는 **Connection Machine**(65,000 프로세서)이었고, 훗날 *"제 주머니의 **픽셀 폰보다 실제로 느립니다**"* 라고 비교한다.

### 현대 AI의 두 도구, 그리고 그 다음

> 현대 인공지능의 두 가지 핵심 도구는 **트랜스포머 모델과 확산 모델**입니다. 그것들은 훌륭하지만, **매우 희소한(sparse) 신경망**을 포함하는 **새로운 하드웨어 아키텍처**와 같이 **소프트웨어와 하드웨어의 완전히 다른 공진화** 양상이 있을 수도 있습니다.

위 "아키텍처의 내구성" 절이 트랜스포머가 오래 버틴 이유를 다뤘다면, 이 소스는 **무엇이 그것을 대체할 수 있는지**에 대한 후보를 제시한다. ⚠️ 방향 제시일 뿐 구체적 결과는 없다. → [[continual-learning]] · [[sutton-bitter-lesson]]

## References

- [[tech-bridge-karpathy-transformers-stanford]]
