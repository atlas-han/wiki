---
title: 억눌린 쿼리 수요 (Suppressed Query Demand)
type: concept
category: principle
tags: [retrieval, search, product, telemetry, user-behavior, evaluation]
aliases: [묻지 않은 질문, suppressed demand, 억눌린 수요]
related: [llm-as-search-user, search-as-recommendation-engine, agentic-search, agent-roi-measurement, capability-discovery-burden]
first-seen: tech-bridge-exa-perfect-search-for-agents
sources: [tech-bridge-exa-perfect-search-for-agents]
created: 2026-09-22
updated: 2026-09-22
---

# 억눌린 쿼리 수요

**사용자가 도구의 한계에 맞춰 질문을 미리 줄인다. 그래서 그 수요는 로그에 남지 않고, 로그를 보는 쪽은 그런 수요가 없다고 결론 내린다.**

> *"싱가포르에서 AI 검색을 연구하는 모든 사람과 그들이 쓴 블로그 글이나 논문을 찾아 줘."* — **장담컨대 여러분은 이런 걸 구글에 쳐 본 적이 없을 겁니다. 안 될 걸 아니까요.** — [[will-bryk]], [[tech-bridge-exa-perfect-search-for-agents]] (03:05~03:16)

**화자는 이 문장을 그냥 지나가지만**, 이것은 제품 계측(telemetry)에 대한 일반적 주장이다: **실패할 것이 예상되는 요청은 시도되지 않으므로, 실패율에도 요청량에도 잡히지 않는다.**

## ⭐ "사용자가 바뀌었다"의 두 번째 읽기

[[llm-as-search-user]]는 [[jo-bergum|Bergum]]의 **AOL 쿼리 로그 대조** 위에 서 있다 — 사람은 예나 지금이나 **몇 단어**를 치는데 [GPT-5]는 *"순식간에 아주 긴 질문을 작성"* 한다. 그 페이지의 결론은 **사용자가 더 강력해졌다**는 것이다.

**이 소스를 겹치면 같은 관측에 다른 해석이 붙는다.**

| | 읽기 A ([[jo-bergum\|Bergum]], 09-21) | 읽기 B (이 소스, 09-22) |
|---|---|---|
| 사람이 짧게 치는 이유 | 사람의 **자연스러운 크기** | **긴 쿼리가 안 통하는 걸 학습했다** |
| LLM이 길게 치는 이유 | 능력이 더 크다 | **학습된 체념이 없다** |
| 따라서 워크로드 변화는 | **새 사용자의 등장** | **제약이 풀린 것** |

**⚠️ 두 읽기는 배타적이지 않고, 어느 쪽도 증거를 갖고 있지 않다.** Bergum은 로그를 갖고 있지만 **왜 짧은지**는 묻지 않았고, Bryk은 **"장담컨대"** 가 전부다.

**구분이 중요한 이유**: 읽기 B가 맞다면 **사람용 검색의 수요 추정치 전체가 하한**이고, 에이전트 트래픽 증가의 일부는 새 수요가 아니라 **원래 있었으나 표현되지 못한 수요**다.

## 이 위키의 인접 페이지와

[[capability-discovery-burden]]([[greg-brockman|Brockman]], 09-20)이 *"약속받았던 AI는 텍스트 상자가 아니었다"* 와 **써 보고 떠난 15억 명**을 말할 때, 그것은 **사용자가 능력을 발견하지 못하는 문제**였다. 이쪽은 한 칸 더 간다 — **발견하지 못하는 것이 아니라, 없다고 학습해서 더 이상 시도하지 않는 상태.**

그리고 평가 쪽으로는 [[agent-roi-measurement]]·[[ir-evaluation-obsolescence]]에 **분모의 문제**를 하나 더한다: **시도되지 않은 작업은 성공률의 분모에도 들어가지 않는다.**

## ⚠️ 미해결

- **크기를 재는 방법이 없다.** 억눌린 수요는 정의상 관측되지 않는다. 소스도 이 문제를 인지하지 않는다.
- **소스에 증거가 없다** — *"I bet"* 한 마디.
- 에이전트 트래픽 중 얼마가 **새 수요**이고 얼마가 **풀린 제약**인지 아무도 구분하지 않는다.

## References

- [[tech-bridge-exa-perfect-search-for-agents]] · [[will-bryk]] · [[exa]]
- 인접: [[llm-as-search-user]] · [[search-as-recommendation-engine]] · [[capability-discovery-burden]]
- 평가: [[agent-roi-measurement]] · [[ir-evaluation-obsolescence]]
- 관련: [[agentic-search]] · [[bm25]]
