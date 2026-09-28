---
title: nanoGPT
type: entity
category: tool
tags: [gpt, training, education, pytorch, open-source]
aliases: [나노GPT, nano GPT]
sources: [tech-bridge-karpathy-transformers-stanford, tech-bridge-agents-vs-humans-optimizer-speedrun]
links:
  - https://github.com/karpathy/nanoGPT
created: 2026-09-03
updated: 2026-09-28
---

# nanoGPT

[[andrej-karpathy|Andrej Karpathy]]가 작성한 **최소 GPT 구현**. 이전 작업 minGPT를 다시 쓴 것으로, [[tech-bridge-karpathy-transformers-stanford]] 강연에서 [[transformer]]를 코드로 설명하는 교보재로 쓰인다.

> ⚠️ 아래 수치는 ~2023년 강연 시점 기준이다.

## 위키에서 알려진 사실

- **300줄**짜리 decoder-only 트랜스포머. *"읽기도 아주 쉽습니다. 300줄이니까 누구나 볼 수 있을 거예요."*
- **8-GPU 노드 1대 × 38시간**으로 open web text에서 **GPT-2를 재현**한다. 장난감이 아니라 *"상당히 진지한 구현"*.
- 순수 PyTorch. 강연에서는 청중이 Stanford CS231n 수준을 안다고 가정하고 빠르게 훑는다.
- 토이 데이터셋으로 **tiny Shakespeare**(전집을 이어붙인 1MB 파일)를 쓴다. 발표자가 가장 좋아하는 데이터셋 중 하나 — *"무한한 셰익스피어를 얻을 수 있죠."*
- 강연 시점에 발표자가 **"지금 하고 있는 일"** 로 지목한 프로젝트다. 컴퓨터 비전 제품에서 언어 도메인으로 옮겨가는 중이라고 밝힌다.

## 코드가 가르치는 것

강연이 nanoGPT를 통해 전달하는 요점들 — 자세한 인용은 [[tech-bridge-karpathy-transformers-stanford]] 참조.

| 요점 | 내용 |
|---|---|
| **what + where는 더한다** | token embedding + positional embedding을 가산 결합 |
| **한 배치는 보이는 것보다 많다** | 4×8 배치의 실질 크기는 `b × t`. 모든 접두사가 동시에 학습됨 |
| **문서 경계는 학습된다** | end-of-text 토큰은 모델링 장치가 아니라, 역전파로 "메모리를 지우라"고 배우는 신호 |
| **causal masking은 한 줄** | `masked_fill(-inf)` + softmax. 복잡한 건 오직 배칭과 5차원 텐서 |
| **컨텍스트 상한은 학습 조건** | block size를 넘으면 crop한다 |
| **세 아키텍처는 한두 줄 차이** | 마스킹 줄을 지우면 encoder, cross-attention 줄을 더하면 encoder-decoder |

## 미해결 사항

- 강연 이후(2023~2026)의 저장소 변화, nanoGPT speedrun 계열 파생 작업 미반영 — 별도 소스 필요
- 이 위키의 다른 도구들([[claude-code]], [[codex]] 등)과 달리 **에이전트 도구가 아니라 학습용 레퍼런스**다. 혼동 주의

## References

- [[tech-bridge-karpathy-transformers-stanford]]

## modded-nanoGPT 스피드런 — 벤치마크가 된 재현 (2026-09-28 · [[tech-bridge-agents-vs-humans-optimizer-speedrun]])

[[prime-intellect|Prime Intellect]] 발표가 전하는 계보: [[andrej-karpathy|Karpathy]]의 GPT-2 재현 영상(약 **90분** — ⚠️ en-orig 후속 발화는 *19분* 으로 들림, 01:47~02:06) → 커뮤니티가 repo를 가져다 **modded-nanoGPT**(Keller Jordan 주도, 02:23~02:33)를 만들고 **45분 → 2분 미만**, *"it took like 2 years"*(02:36~02:50). 규칙은 **목표 loss(GPT-2의 validation loss)에 가장 빨리 도달**, 제약은 **같은 검증·훈련 데이터**뿐(03:05~03:25). 화자는 이를 *"a very strong benchmark"*(02:51~02:54)라 부르고, 파생인 **optimizer speedrun**(옵티마이저 관련 파라미터만 변경)을 코딩 에이전트의 연구 능력 측정 환경으로 쓴다. → [[automated-ai-research]]

> ⚠️ 이 페이지 위쪽의 *"8-GPU 노드 1대 × 38시간"*(~2023 강연)과 이 소스의 *90분*·*2분 미만* 은 **시점·하드웨어·구현이 다른 수치**다. 이 소스는 하드웨어를 말하지 않는다.
