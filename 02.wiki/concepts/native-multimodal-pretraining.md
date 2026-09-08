---
title: Native Multimodal Pretraining
type: concept
category: technique
tags: [multimodal, pretraining, vision, adapter, scaling, minimax]
aliases: [native multimodality, 네이티브 멀티모달]
related: [minimax-m3, sutton-bitter-lesson, transformer, long-context-agents, multimodal-elicitation]
first-seen: tech-bridge-minimax-m3-long-context
sources: [tech-bridge-minimax-m3-long-context]
created: 2026-09-08
updated: 2026-09-08
---

# Native Multimodal Pretraining

텍스트 사전학습이 끝난 뒤 **어댑터를 붙여** 비전을 가르치지 않고, **첫 스텝부터 텍스트와 비전을 함께** 사전학습하는 방식. [[minimax|MiniMax]]가 [[minimax-m3|M3]]에서 *native multimodality* 라 부른다.

> 모델 랩에서는 **텍스트 사전 학습이 끝난 뒤에** 비전 이해 기능을 학습시키는 게 일반적입니다. **어댑터를 장착한 다음 해당 부분을 훈련**시키죠. — [[olive-song]], [[tech-bridge-minimax-m3-long-context]]

## 세 가지 선택지와 각각의 문제

| 방식 | 문제 |
|---|---|
| 텍스트 사전학습 후 **어댑터** | **텍스트 성능을 해치고**, 모델이 텍스트 쪽으로 수렴해 **비전이 잘 수렴하지 않는다** |
| 사전학습 **중간부터** (continued pre-training) | **레시피에 매우 민감** — 아키텍처·데이터 혼합·학습률마다 결과가 달라진다 |
| **첫 스텝부터** (M3의 선택) | 많은 랩이 **몇 스텝 만에 붕괴(collapse)** 한다 |

## 반대 이유가 성능이 아니라 확장 가능성이다

두 번째 줄에 대한 진술이 이 개념에서 가장 이식성 높은 부분이다.

> 아키텍처마다, 데이터 혼합 방식마다, 학습률마다 결과가 다르기 때문에 **제어하기 어렵고 확장하기도 어렵습니다.** **실험 결과와 결론을 더 큰 모델에 적용하기가 사실상 불가능합니다.**

기각의 근거가 *결과가 나쁘다*가 아니라 **작은 실험의 결론이 큰 모델로 옮겨가지 않는다**는 것이다. 즉 **연구 절차로서 쓸모가 없다.**

[[sutton-bitter-lesson]]이 *"스케일에 태우지 못하는 것은 결국 진다"* 를 **성능 축**에서 말했다면, 여기서는 같은 논리가 **방법론 축**에서 나온다 — 스케일에 태워지지 않는 것은 성능 이전에 **알 수 없다**. 이 위키에서 bitter lesson이 실험 설계 기준으로 쓰인 첫 사례다.

⚠️ 소스는 [[sutton-bitter-lesson]]을 언급하지 않는다. 연결은 위키가 놓는다.

## 붕괴를 넘긴 방법 (제시된 것)

> 저희는 **ViT에 대해 많은 작업**을 했고, **실제로 훈련에 사용하는 데이터에 대해서도 많은 작업**을 했습니다. 예를 들어, 저희는 **interleaved data**를 씁니다 — 사실 **자연스러운 데이터인데, 이미지와 비디오를 마스킹해서 빼지 않고 그대로 남겨두는** 것입니다. 저희는 데이터에 대한 **꽤 좋은 클리닝과 마스킹**을 수행하고, **매우 좋은 보상 모델링(reward modeling)** 을 합니다.

셋이 나열될 뿐 **각각이 붕괴의 어느 부분을 막았는지는 없다.** *"interleaved data"* 의 정의만이 구체적이다 — 웹 문서에서 이미지·비디오를 **빼지 않고 남긴** 자연 데이터.

## 무엇을 위해서인가

같은 대담에서 멀티모달의 쓸모가 **에이전트 사용 사례**로 제시된다.

> 모델이 **PowerPoint를 읽도록** 하는 기능이죠. 혹은 **체계적이지 않은 보고서**를 읽고 싶거나, **아주 긴 영상을 이해**하고 싶을 때도 있겠죠. 긴 동영상을 넣고 **모델이 그것을 이해한 뒤 도구를 써서 행동하도록** 하고 싶다고 가정해 보세요.

이것이 [[long-context-agents]]와 곱해진다 — **긴 영상·비정형 문서를 이해하려면 길이도 함께 필요하다.** 소스가 두 주장을 나란히 두지만 명시적으로 잇지는 않는다.

진행자는 이 영역이 **아직 덜 쓰이고 있다**고 보고, 게스트도 동의한다 — *"이번이 처음으로 두 가지를 결합하는 것이기 때문에 (…) 현재는 다소 미흡한 부분이 있을 수 있지만"*.

이 위키의 [[multimodal-elicitation]]([[tech-bridge-multimodal-commerce-agent]])이 **사용 쪽**에서 멀티모달을 다뤘다면(이미지로 선호를 끌어낸다), 이 페이지는 **학습 쪽**이다.

## 미해결 사항

- **붕괴 해결의 내용** — ViT·데이터·보상 모델링 각각의 역할.
- **텍스트 성능 손실의 크기** — 어댑터 방식이 얼마나 해치는지 수치가 없다.
- 어느 벤치마크로 확인했는지. 소스 전체에 수치가 없다.

## References

- [[tech-bridge-minimax-m3-long-context]] · [[minimax-m3]] · [[olive-song]]
- 관련: [[long-context-agents]] · [[sparse-attention]] · [[sutton-bitter-lesson]] · [[multimodal-elicitation]] · [[transformer]]
