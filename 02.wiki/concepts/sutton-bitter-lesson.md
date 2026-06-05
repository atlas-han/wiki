---
title: "The Bitter Lesson (Sutton, 2019)"
type: concept
category: theory
tags: [ai-research, scaling, computation, history-of-ai, sutton]
aliases: [Bitter Lesson]
related: [agent-harness-design, brain-hands-decoupling]
first-seen: anthropic-managed-agents
sources: [anthropic-managed-agents]
created: 2026-05-25
updated: 2026-05-25
---

# The Bitter Lesson

Rich Sutton의 2019년 3월 13일 에세이. 70년 AI 연구사의 **메타 패턴**을 한 문장으로 압축한 짧은 글로, 본 위키에서 자주 인용된다 ([[agent-harness-design]], [[brain-hands-decoupling]], [[anthropic-managed-agents]]).

## 핵심 주장 (오프닝 문장)

> The biggest lesson that can be read from 70 years of AI research is that the general methods that leverage computation are ultimately the most effective, and by a large margin.

근거: Moore's law와 단위 컴퓨테이션당 비용의 지수적 감소. 연구자들은 컴퓨테이션이 *상수*인 듯 설계하지만, 시간이 가면 막대한 추가 컴퓨트가 도착한다. 인간 도메인 지식을 모델에 박는 접근은 단기엔 이기지만 장기엔 **scaling되는 일반 방법**에 진다.

## 무엇이 scale하는가

두 가지가 임의로 scale함:
1. **Search**
2. **Learning**

이 둘은 컴퓨트가 늘수록 단조 증가하는 효용을 준다. 도메인 지식 주입은 그렇지 않다.

## 역사적 사례

| 분야 | 인간 지식 접근 | Scaling 접근 (이긴 쪽) |
|---|---|---|
| **체스** | grandmaster heuristic, 체스 구조 활용 | Deep Blue의 대규모 alpha-beta search + 전용 하드웨어 |
| **바둑** | 수십 년의 hand-crafted evaluation, 도메인 지식 | AlphaGo: deep neural network + MCTS, 데이터·연산으로 학습 |
| **음성 인식** | hand-engineered acoustic model | 대규모 음성 데이터셋으로 표현을 학습한 deep learning |
| **컴퓨터 비전** | hand-designed feature, 특정 구조 | 대규모 이미지셋으로 학습한 deep convnet |

## 메타 레슨

> The lesson is not about scaling up one method in particular, but about scaling up computation in learning systems generally.

연구자가 *짜낸 영리한 구조*는 시간이 가면 dead weight가 된다. 일반 search·learning 알고리즘에 컴퓨트가 흐르게 두는 것이 장기 정답.

## 본 위키에서의 적용

[[anthropic|Anthropic]] Engineering Blog 연작이 이 정신을 LLM agent harness에 적용:

> Harnesses encode assumptions about what the model can't do on its own — and those assumptions go stale as models improve.
> — [[anthropic-managed-agents]]

[[claude-sonnet-4-5|Sonnet 4.5]]를 위해 추가한 [[context-resets-and-compaction|context reset]]이 [[claude-opus-4-5|Opus 4.5]]에서 dead weight가 된 것이 구체적 사례. [[agent-harness-design]]의 일반 원리와 정합.

## References

- [원문 (incompleteideas.net, self-signed cert)](http://www.incompleteideas.net/IncIdeas/BitterLesson.html)
- 미러: [cs.utexas.edu PDF](https://www.cs.utexas.edu/~eunsol/courses/data/bitter_lesson.pdf)
- [Wikipedia: Bitter lesson](https://en.wikipedia.org/wiki/Bitter_lesson)
- 본 위키 내 적용: [[agent-harness-design]], [[brain-hands-decoupling]], [[anthropic-managed-agents]]
