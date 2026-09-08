---
title: Attention Mechanism
type: concept
category: architecture
tags: [attention, architecture, deep-learning, graph, message-passing]
aliases: [어텐션, Attention, self-attention, 셀프 어텐션]
related: [transformer, in-context-learning, nanogpt, dzmitry-bahdanau, sparse-attention, long-context-agents]
first-seen: tech-bridge-karpathy-transformers-stanford
sources: [tech-bridge-karpathy-transformers-stanford, tech-bridge-minimax-m3-long-context]
created: 2026-09-03
updated: 2026-09-08
---

# Attention Mechanism

[[transformer|트랜스포머]]의 통신 단계. [[tech-bridge-karpathy-transformers-stanford]]가 이 위키에 들여온 재해석은 **어텐션 = 방향 그래프 위의 데이터 의존적 메시지 전달**이라는 관점이다.

> ⚠️ 이 관점은 [[andrej-karpathy|Karpathy]] 본인이 강연 Q&A에서 *"오늘 아침에 생각해냈다 — 사실 어제"* 라고 농담한 **개인적 프레이밍**이다. 표준 교과서 설명이 아니라 이해를 돕는 틀로 읽어야 한다.

## 그래프 관점

기계 번역도 시퀀스도 잊고, **각 노드에 벡터를 저장하는 방향 그래프**만 생각한다. 노드는 private data vector를 갖고, 선형 변환으로 세 벡터를 내보낸다.

| 벡터 | 발표자의 정의 |
|---|---|
| **query** | 내가 **무엇을 찾고 있는가** |
| **key** | 내가 **무엇을 가지고 있는가** |
| **value** | 내가 **무엇을 전달할 것인가** |

한 라운드의 통신:

1. 노드가 자기 **query** Q를 얻는다
2. **이 노드를 가리키는 모든 입력**이 자기 **key**를 브로드캐스트한다
3. query·key **내적** → 정규화되지 않은 affinity(흥미도)
4. **softmax**로 정규화 → 합이 1인 확률 분포
5. 그 가중치로 **value들의 가중합** → 자신을 업데이트

> 저는 query를 가지고 있고, 그들은 key를 가지고 있고, 내적으로 affinity를 얻고, softmax로 정규화하고, 그 value들의 가중합이 저에게 흘러들어와 저를 업데이트합니다.

이것이 **헤드마다 병렬로, 레이어마다 직렬로**, 매번 다른 가중치로 일어난다.

## self / cross / multi-head

세 용어가 흔히 뒤섞이는데, 강연의 정리가 명료하다.

| 용어 | 무엇이 다른가 |
|---|---|
| **multi-head** | 같은 어텐션을 **독립적으로 여러 번 병렬** 적용. 헤드마다 query·key·value 가중치가 다름 |
| **self-attention** | key·query·value를 **자기 노드에서** 생성 |
| **cross-attention** | query는 자기 노드, **key·value는 외부(인코더)** 노드에서 생성 |

> cross-attention과 self-attention은 **key와 value가 어디에서 오는지에서만 차이**가 있을 뿐입니다. (…) 알고리즘적으로는 **동일한 수학적 연산**입니다.

multi-head의 직관: *"병렬적으로 여러 노드에서 **서로 다른 종류의 정보를 찾고**, 그 모든 정보를 하나의 노드에 모으는 것."*

## 연결성이 아키텍처를 정한다

그래프 관점의 실질적 이득. 어텐션 수식은 그대로 두고 **어떤 간선을 허용하느냐**만 바꾸면 아키텍처가 바뀐다.

| 연결성 | 결과 |
|---|---|
| 전 노드 완전 연결 | encoder (BERT류) |
| **삼각 구조** (자기 자신과 이전 노드만) | decoder / causal (GPT류) |
| 두 노드 풀 + 단방향 유입 | encoder-decoder |

decoder에서 삼각 구조가 필요한 이유는 정보 누설이다.

> 앞으로 올 토큰과의 통신을 원하지 않습니다. 왜냐하면 그렇게 하면 **이 단계에서 정답이 드러나기** 때문입니다.

cross-attention의 미묘한 점 — 디코더는 인코더의 **최상위 노드만** 본다. 인코더 안에서는 모든 토큰이 여러 층에 걸쳐 서로를 살핀 뒤, 그 결과만 디코더로 넘어간다.

## causal masking 구현

마스킹 자체는 한 줄이고, 어려움은 전부 배칭에서 온다.

```python
att = q @ k.transpose(-2, -1)                    # 배치·헤드·시간 병렬 내적
att = att.masked_fill(mask == 0, float('-inf'))  # 금지 간선
att = att.softmax(dim=-1)                        # -inf → 가중치 0
y   = att @ v                                    # affinity 가중합
```

> **negative infinity를 쓰는 이유는 곧 softmax를 할 것이기 때문**입니다.

발표자 본인이 5차원 텐서(batch·head·time·feature)를 *"정말 헷갈린다"*고 인정하며, 한 줄씩 짚어보길 권한다.

### √d 스케일링은 초기화 문제

> 랜덤 가중치로 초기화하면 차원이 커질수록 **분산이 커지고 softmax가 one-hot 벡터처럼 됩니다.** (…) 거의 **초기화 문제**에 가깝습니다.

## 계보 — 인코더 병목에서 나왔다

어텐션은 추상적 발명이 아니라 **구체적 고장에 대한 수리**였다. 2014년 seq2seq는 영어 문장 전체를 인코더에서 디코더로 넘기는 **단일 벡터**에 욱여넣었다.

> 이는 단일 벡터에 저장하기에는 너무 많은 정보입니다. **그건 옳지 않아 보였다.**

[[dzmitry-bahdanau|Bahdanau]] et al.이 이를 **soft-search**로 풀었다 — 디코딩하면서 인코더의 단어들을 되돌아본다. 컨텍스트 벡터 = 인코더 은닉 상태들의 가중합, 가중치 = 현재 디코딩 상태와의 호환성에 대한 softmax. 발표자는 이 논문을 **"attention"이라는 단어가 이 메커니즘에 쓰인 최초 사례**로 지목한다.

이름의 유래: 원래 **RNNsearch**였고, *attention*은 **Yoshua Bengio**가 최종 교정에서 붙였다.

2017년 논문의 주장은 여기서 한 걸음 더 나간다 — *"이 아키텍처가 잘 작동하는 핵심은 **어텐션 그 자체**이므로 나머지를 전부 삭제해도 된다."*

## graph neural network와의 관계

> 오늘날에는 어쩌면 **모든 게 graph neural network**인 것 같아요. **트랜스포머가 graph neural network 프로세서**이고, 트랜스포머가 다루는 네이티브 표현이 **방향 간선으로 연결된 집합**이기 때문입니다.

단, 연결성은 **정적**이다. 질문자가 데이터에 따라 간선이 바뀌는 경우를 묻자:

> 저는 **연결성이 데이터의 함수로 동적으로 바뀌는 예를 단 하나도 본 적이 없습니다.**


## 효율화의 진자 운동 (2026-09-08 · [[tech-bridge-minimax-m3-long-context]])

이 페이지는 어텐션을 **무엇인가**(방향 그래프 위의 메시지 전달)로 설명해 왔다. [[thomas-wolf]]가 [[olive-song]]에게 [[sparse-attention|MSA]]를 물으며 놓는 프레이밍은 **어텐션 효율화의 역사**다.

> 어텐션에 대한 연구가 많이 이루어졌고 — 이 **n제곱** 문제 말이죠 — **linear attention**에 대한 연구도 많았습니다. 그러다가 **flash attention이 등장하면서 그 모든 것들이 어느 순간 사라져 버렸죠.** 우리는 **더 효율적인 [커널]** 이 필요할 뿐이라는 것을 알게 되었습니다. 자, 이제 우리가 다시 **제1원리로 돌아가서 어텐션이란 무엇이고 어떻게 하면 더 효율적으로 만들 수 있을지** 생각해 보는 게 좋네요.

세 국면이다:

1. **구조로 푼다** — n² 비용에 linear attention 등 아키텍처 변형이 쏟아진다.
2. **커널로 풀린다** — flash attention이 등장하자 그 변형들이 대부분 필요 없어진다.
3. **다시 구조로** — 길이가 100만 규모로 가면서 구조 문제가 돌아온다 → [[sparse-attention]].

**같은 문제가 두 층(아키텍처 / 커널) 사이를 오간다**는 관찰이다. [[transformer]] 페이지가 *"표현력·최적화 가능성·GPU 효율성을 동시에 만족해서 이겼다"* 로 정리한 세 항 중 **세 번째가 구현으로 해결되자 앞의 둘을 다시 건드릴 여지가 생겼다**는 이야기이기도 하다.

[[sparse-attention|MSA]]가 이 페이지의 어휘에 더하는 것은 **선택 층**이다 — query/key/value 위에 *어디를 볼지 고르는* 인덱스 브랜치가 하나 더 붙는다. 이 페이지가 [[andrej-karpathy|Karpathy]]를 따라 어텐션을 *"정적 연결성 위의 데이터 의존적 메시지 전달"* 로 정리했는데, MSA는 **연결성 자체를 데이터에 따라 줄인다**. ⚠️ 다만 Karpathy가 *"연결성이 데이터의 함수로 동적으로 바뀌는 예를 단 하나도 본 적이 없다"* 고 한 것과 같은 층위인지는 **두 소스 어느 쪽도 다루지 않는다** — 위키는 판정하지 않는다.

⚠️ *"더 효율적인 [커널]"* 은 en-orig가 *"camera"* 로 오인식한 자리이고 **소스가 단어를 확정하지 않는다.** ⚠️ MSA의 정량적 근거도 소스에 없다.

## References

- [[tech-bridge-karpathy-transformers-stanford]]
- [[tech-bridge-minimax-m3-long-context]] — 효율화의 진자 운동 · [[sparse-attention]] (2026-09-08)
