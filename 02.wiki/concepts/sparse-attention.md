---
title: Sparse Attention (MSA)
type: concept
category: architecture
tags: [attention, sparse, architecture, efficiency, minimax, msa]
aliases: [MSA, MiniMax Sparse Attention, 희소 어텐션]
related: [attention-mechanism, transformer, long-context-agents, minimax-m3]
first-seen: tech-bridge-minimax-m3-long-context
sources: [tech-bridge-minimax-m3-long-context]
created: 2026-09-08
updated: 2026-09-08
---

# Sparse Attention (MSA)

전체 컨텍스트에 어텐션을 전부 계산하지 않고 **중요한 블록만 골라** 계산하는 구조. [[minimax|MiniMax]]가 [[minimax-m3|M3]]의 100만 토큰 컨텍스트를 위해 만든 **MiniMax Sparse Attention (MSA)** 이 이 위키의 첫 사례다.

## 2단 구조

> 좀 더 높은 수준에서 설명하자면, **인덱스 브랜치**가 있어서 **컨텍스트에서 무엇이 더 중요한지 상위 수준에서 선택**하고, 그 다음에는 **스파스 어텐션 브랜치**가 있어서 **선택된 블록들에 대해 계산을 수행**하고 실제로 작업을 처리합니다. — [[olive-song]], [[tech-bridge-minimax-m3-long-context]]

| 브랜치 | 하는 일 |
|---|---|
| **인덱스 브랜치** | 상위 수준에서 **무엇이 중요한지 선택** |
| **스파스 어텐션 브랜치** | **선택된 블록에 대해서만** 실제 계산 |

**선택과 계산을 분리한 것**이 구조의 핵심이다. [[attention-mechanism]]이 *"query=찾는 것 · key=가진 것 · value=전달할 것"* 으로 정리한 한 단계 위에 **어디를 볼지 고르는 층**이 하나 더 붙는다.

설계 목표가 성능이 아니라 **확장성**으로 진술된다.

> 저희는 **길이를 확장할 수 있고, 향후 모델 크기도 확장할 수 있도록 우아한 구조**를 설계했습니다.

## 어텐션 효율화의 진자 운동

[[thomas-wolf]]가 이 작업을 연구사 안에 놓는데, 이 서술이 이 위키의 [[attention-mechanism]]·[[transformer]]에 곧장 붙는다.

> 어텐션에 대한 연구가 많이 이루어졌고 — 이 **n제곱** 문제 말이죠 — **linear attention**에 대한 연구도 많았습니다. 그러다가 **flash attention이 등장하면서 그 모든 것들이 어느 순간 사라져 버렸죠.** 우리는 **더 효율적인 [커널]** 이 필요할 뿐이라는 것을 알게 되었습니다. 자, 이제 우리가 다시 **제1원리로 돌아가서 어텐션이란 무엇이고 어떻게 하면 더 효율적으로 만들 수 있을지** 생각해 보는 게 좋네요.

세 국면이다:

1. **구조로 푼다** — n² 문제에 linear attention 등 아키텍처 변형이 쏟아진다.
2. **커널로 풀린다** — flash attention이 등장하자 그 변형들이 대부분 불필요해진다.
3. **다시 구조로** — 길이가 100만 규모로 가자 구조 문제가 되돌아온다.

[[tech-bridge-karpathy-transformers-stanford]]는 [[transformer]]가 이긴 이유를 **표현력·최적화 가능성·GPU 효율성** 세 항의 동시 충족으로 정리했다. 위 서술은 그 위에 시간 축을 얹는다 — **세 번째 항이 커널로 해결되고 나서야 첫 번째·두 번째 항을 다시 건드릴 여지가 생겼다.**

⚠️ *"더 효율적인 [커널]"* 은 en-orig가 *"camera"* 로 오인식한 자리이고, **소스가 단어를 확정하지 않는다.** 문맥상의 읽기다.

## ⚠️ 정량적 근거가 없다

이 페이지의 가장 큰 한계다. 소스에 있는 것은 **형용사뿐**이다 — *"우아하다"*, *"확장 가능하다"*, *"디자인이 간단하다"*, 그리고 M3가 *"저렴하다"*.

> M3에 대해 여전히 매우 흥미로운 점은 **가격이 저렴하다**는 것인데, 특히 **이 sparse attention 때문인지 아니면 크기가 작기 때문인지는 모르겠지만**, 효율성 또한 매우 뛰어납니다.

**진행자 본인이 인과를 확정하지 못한다.** 벤치마크·속도·비용·메모리 수치가 하나도 없고, 논문이나 기술 리포트 링크도 설명란에 없다.

## 설계자가 인턴이었다

> **저희 팀의 인턴이 작업한 것 같아요. 네, 인턴이요.** (…) 어떤 연구실에서는 **인턴에게 데이터나 업무에 대한 접근 권한이 제한**되어 있거든요. 하지만 저희는 **모델 개발에 기여하고 싶은 사람이라면 누구든 환영**합니다.

진행자가 *"에이전트가 아이디어를 낸 건가요, 아니면 사람이 직접 생각해낸 건가요?"* 라고 물어서 나온 답이다 — **사람이었다.** [[minimax]]의 프로젝트 제안 제도와 직접 이어진다.

## 미해결 사항

- **정량 근거 전부** (위 참조).
- 인덱스 브랜치가 **어떻게** 중요도를 고르는지 — 학습되는지, 블록 크기는 얼마인지.
- 선택에서 **빠진 블록의 정보 손실**을 어떻게 다루는지.
- MSA와 기존 sparse/linear attention 계열(Longformer·BigBird·NSA 등)의 관계 — 소스가 언급하지 않는다.

## References

- [[tech-bridge-minimax-m3-long-context]] · [[minimax-m3]] · [[olive-song]] · [[thomas-wolf]]
- 관련: [[attention-mechanism]] · [[transformer]] · [[long-context-agents]] · [[minimax]]
