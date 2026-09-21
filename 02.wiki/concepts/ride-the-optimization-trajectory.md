---
title: 모델이 최적화되는 방향에 올라타기 (Ride the Optimization Trajectory)
type: concept
category: patterns
tags: [agent-design, harness, tool-design, frontier-models, bet]
aliases: [편법, hack, 프론티어의 궤적에 올라타기]
related: [corpus-as-filesystem-workspace, file-system-agent, harness-pruning, agent-harness-design, llm-as-search-user, retrieval-primitive-repertoire, sutton-bitter-lesson]
first-seen: tech-bridge-bm25-agentic-search
sources: [tech-bridge-bm25-agentic-search]
created: 2026-09-21
updated: 2026-09-21
---

# 모델이 최적화되는 방향에 올라타기

**프론티어 랩이 무엇에 맞춰 모델을 최적화하고 있는지 알면, 그 위에 시스템을 얹어 두는 것만으로 모델이 바뀔 때마다 공짜로 좋아진다.**

> **그리고 이것도 일종의 편법(hack)이잖아요. 현재 모델이 잘하는 부분을 최적화하기 위해서겠죠? 모든 최첨단 LLM 기업들이 코딩, Bash, 도구 사용에 맞춰 모델을 최적화하고 있기 때문입니다. 그러니까, 여러분이 처음부터 끝까지 수행하는 작업을 그런 방향으로 진행시키면, 새로운 모델이 나올 때마다 그 모델이 더 나은 성능을 보여줄 거라는 걸 알 수 있잖아요?** — [[jo-bergum]], [[tech-bridge-bm25-agentic-search]] (14:01~14:22)

**화자가 자기 제안을 스스로 "편법"이라고 부른다.** 이 위키의 설계 논의에서 드문 정직함이다.

## 왜 이것이 이 위키에 필요한 페이지인가

이 위키는 **왜 파일 시스템·bash·`grep`이 에이전트에게 먹히는가**를 여러 소스에서 봐 왔지만, 대부분 **결과만** 기록했다.

| 페이지 | 관측 | 이유를 댔나 |
|---|---|---|
| [[file-system-agent]] (09-19) | 도구를 깎지 말고 **바닥을 줘라** | *"모델이 이미 안다"* 수준 |
| [[corpus-as-filesystem-workspace]] (09-20) | 검색 결과를 **파일로 펼친다** | 이 페이지가 댄다 |
| [[ralph-wiggum-method]] | 단순 루프가 먹힌다 | — |
| [[llm-as-search-user]] | 모델이 **`grep`·BM25를 강하게 만든다** | 일반 지식으로 설명 |

**이 페이지는 그 이유를 *모델의 성질*이 아니라 *랩의 인센티브*에 둔다.** 파일 시스템이 본질적으로 우월해서가 아니라, **모두가 코딩 에이전트를 팔고 있어서 코딩·bash·툴 사용이 모든 릴리스에서 개선되기 때문**이다.

## 베팅의 구조

| | 내용 |
|---|---|
| **무엇에 거나** | 프론티어 랩들의 **공통 최적화 목표**(코딩·bash·도구 사용) |
| **왜 유리한가** | 모델 교체가 **내 시스템의 업그레이드**가 된다 — 내가 한 일 없이 |
| **무엇을 포기하나** | 그 목표에서 벗어난 인터페이스(정교한 전용 도구·DSL) |
| **언제 깨지나** | 랩의 최적화 목표가 바뀌거나, **모델이 그 우회를 아예 필요로 하지 않을 때** |

화자가 마지막 줄을 직접 말한다:

> **인공 일반 지능(AGI)이 등장하면 그들은 그냥 브라우저를 사용할 수도 있겠죠. 두고 보면 알 겁니다.** 하지만 **현재로서는** 이것이 (…) **매우 강력한 방법**입니다. (14:24~14:36)

**즉 이것은 영구적 설계 원칙이 아니라 명시적으로 한시적인 베팅**이다.

## [[harness-pruning]]의 반대면

[[agent-harness-design]]의 중심 문장 — *"하니스는 모델이 못 하는 것에 대한 가정을 담고, 그 가정은 낡는다"* — 은 **낡음을 비용**으로 본다. 이 페이지는 같은 사실을 **레버**로 쓴다: **어차피 낡을 거라면, 낡으면서 좋아지는 방향에 가정을 걸어라.**

| | [[harness-pruning]] | **이 페이지** |
|---|---|---|
| 모델 진화는 | 하니스를 **dead weight로 만든다** | 시스템을 **공짜로 개선한다** |
| 대응 | 주기적으로 **덜어낸다** | 처음부터 **궤적 위에 얹는다** |
| 위험 | 덜어내지 않으면 짐이 된다 | **궤적이 바뀌면 통째로 틀린다** |

## ⚠️ 그리고 같은 날 반대 방향의 경고가 있다

[[benjamin-clavie|Clavié]]는 **모델이 학습 데이터에서 얻은 습관에 기대는 것의 대가**를 말한다:

> 자주 보게 되는 한 가지는 **에이전트가 [`grep`] 쿼리를 쓰려고 한다는 것입니다. [`grep`]은 학습 데이터 어디에나 있고 BM25도 데이터 어디에나 있으니까요. 그리고 그게 항상 필요한 것은 아닙니다.** (…) **PDF는 [`grep`] 할 수 없습니다.** — [[tech-bridge-knowledge-agents-not-coding-agents]] (16:02~16:23)

**같은 성질이 한쪽에서는 레버이고 다른 쪽에서는 편향이다.** 궤적에 올라타면 **모델이 그 궤적 밖을 잘 못 본다**는 것도 같이 받는 것이다. → [[retrieval-primitive-repertoire]]

## ⚠️ [[sutton-bitter-lesson|쓴 교훈]]과의 관계는 소스에 없다

표면적으로 **쓴 교훈의 실무판**처럼 읽힌다 — *일반적이고 규모를 타는 것에 걸어라*. 하지만 **여기서 걸라고 하는 대상은 연산이 아니라 "랩들이 마침 최적화 중인 인터페이스"** 이고, 그것은 **우연적이고 상업적인 사실**이다. **소스는 이 연결을 하지 않는다. 이 위키도 하지 않고 표시만 한다.**

## References

- [[tech-bridge-bm25-agentic-search]] · [[jo-bergum]]
- 개념: [[corpus-as-filesystem-workspace]] · [[file-system-agent]] · [[llm-as-search-user]] · [[retrieval-primitive-repertoire]]
- 반대면: [[harness-pruning]] · [[agent-harness-design]]
- ⚠️ 연결하지 않은 곳: [[sutton-bitter-lesson]]
