---
title: 인재 밀도 (Talent Density)
type: concept
category: theory
tags: [research-org, team-size, meta, llm-training, management]
aliases: [가장 작은 팀, talent density]
related: [meta-superintelligence-labs, compute-constrained-growth, agent-manager-analogy, harness-pruning]
first-seen: tech-bridge-zuckerberg-muse-personal-agent
sources: [tech-bridge-zuckerberg-muse-personal-agent]
created: 2026-09-14
updated: 2026-09-14
---

# 인재 밀도

**프론티어 모델 훈련은 인원을 늘려 푸는 문제가 아니라, 전체를 머릿속에 담을 수 있는 가장 작은 팀으로 푸는 문제라는 입장.** [[mark-zuckerberg]]가 **Llama 4의 실패 뒤에 내린 결론**으로 제시한다.

> **이건 천 명이 실험을 돌리는 시스템이 아닙니다. 어떤 면에서는 **모든 것을 머릿속에 담고 하나의 과학 프로젝트처럼 함께 일할 수 있는 가능한 한 가장 작은 그룹**을 원하게 됩니다. **자리가 몇 개뿐이라면 각 자리에 최고의 사람을 앉히는 게 엄청나게 중요**해집니다.** — [[tech-bridge-zuckerberg-muse-personal-agent]] (42:55~43:23)

## 무엇의 결론인가 — 실패가 앞에 있다

이 개념은 추상적 조직론이 아니라 **구체적 실패에 대한 응답**으로 제시된다.

> **LLM이 주목받기 시작했을 때 우리에게는 FAIR라는 랩이 있어 Llama의 초기 작업을 했지만, 그것을 프로덕션화하고 **산업적 공정**으로 만들어야 했습니다. 그때 **제가 실수를 했다**고 생각합니다 — 우리가 **다른 종류의 머신러닝을 잘하니 LLM을 만들고 스케일하는 접근도 비슷할 거라고 가정**한 것이죠. 실제로는 아주 다른 역학이 많습니다.** (41:56~42:36)

> **첫 접근은 Llama 4를 통해서였고 (…) 막상 내놓았을 때 우리가 있어야 할 궤도에서 벗어나 있었다고 봅니다. 뭔가 바꿔야 했죠.** (42:37~42:54)

**진단의 핵심은 "잘하던 것의 방법론을 그대로 옮긴 것"** 이다 — 피드 랭킹·광고·integrity 시스템에서 통하던 **대규모 병렬 실험 조직**이 LLM에는 맞지 않았다는 것.

## 따라온 세 가지 결정

| 결정 | 내용 |
|---|---|
| **CEO의 시간 배분** | *"**제 개인 시간을 엄청나게 썼습니다**"* — 채용에 |
| **기술적 근접** | *"**업무에 기술적으로 더 가까이** 가고 싶었습니다 — 회사를 더 잘 이해하고 방향을 제시하려고"* |
| **물리적 배치** | *"랩을 **말 그대로 사무실에서 제가 앉는 자리 주변에** 지었습니다. 그룹이 그 주위에 있는 셈이죠"* |

**세 번째가 이 위키에서 처음 보는 형태다** — 연구 조직의 성과를 **물리적 좌석 배치**로 설명하는 진술.

## 이 위키의 연구 조직 축에서

| 조직 | 원리 | 근거 |
|---|---|---|
| [[minimax\|MiniMax]] ([[tech-bridge-minimax-m3-long-context]]) | **누구나 제안하는 연구 문화** — 인턴이 MSA 아키텍처를 설계했다 | 개방적 제안 |
| [[anthropic\|Anthropic]] ([[tech-bridge-claude-platform-agent-era]]) | Claude Platform **200명 팀** | 규모 명시만 |
| **[[meta-superintelligence-labs\|MSL]]** | **좌석 수 최소화 + 최고 인재 + 물리적 근접** | 밀도 |

**MiniMax와 정면으로 반대 방향이다.** 둘 다 *"규모가 아니라 조직"* 이라 말하지만 한쪽은 **제안의 폭**을, 다른 쪽은 **밀도**를 택한다. ⚠️ **양쪽 다 당사자 진술이고, 어느 쪽도 성과와의 인과를 제시하지 않는다.**

## 컴퓨팅과의 관계 — 순서가 있다

> **작업 품질에 대한 확신이 커지면서 컴퓨팅 투자를 크게 늘렸습니다.** (43:46~43:52)

**인재 → 확신 → 컴퓨팅** 순서다. 이 위키의 [[compute-constrained-growth]](성장이 컴퓨팅 배분에 묶인다, [[sam-altman]])와 **방향이 반대** — 저쪽은 컴퓨팅이 제약이고, 여기서는 **컴퓨팅이 결과**다.

재원 논리도 명시적이다 — *"다른 랩들과 달리 우리는 **극도로 수익성 있는 사업**이라 이런 투자를 하는 데 매우 도움이 됩니다."*

## 열려 있는 것

- ⚠️ **"가장 작은 팀"의 크기가 없다.** 숫자가 한 번도 나오지 않는다.
- ⚠️ **Llama 4가 무엇이 어떻게 궤도를 벗어났는지 없다.**
- ⚠️ **재편의 비용**(채용 경쟁·기존 팀의 이동)이 다뤄지지 않는다.
- ⚠️ **성과와의 인과가 없다.** 진행자가 인용한 외부 평가(SemiAnalysis·Artificial Analysis)는 **화자가 확인하지 않는다.**

## References

- [[tech-bridge-zuckerberg-muse-personal-agent]] · [[meta-superintelligence-labs]] · [[meta]] · [[mark-zuckerberg]]
- 관련: [[compute-constrained-growth]] · [[minimax]] · [[anthropic]] · [[agent-manager-analogy]]
