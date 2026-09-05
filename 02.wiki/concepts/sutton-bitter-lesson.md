---
title: "The Bitter Lesson (Sutton, 2019)"
type: concept
category: theory
tags: [ai-research, scaling, computation, history-of-ai, sutton]
aliases: [Bitter Lesson]
related: [agent-harness-design, brain-hands-decoupling, signal-layer, agentic-sites, agent-distributed-systems, verifiable-goals, agent-skills, flutter, transformer, in-context-learning]
first-seen: anthropic-managed-agents
sources: [anthropic-managed-agents, tech-bridge-signal-layer, tech-bridge-agents-as-distributed-systems, tech-bridge-flutter-ai-workflow, tech-bridge-karpathy-transformers-stanford]
created: 2026-05-25
updated: 2026-09-03
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

## 범위 한정: 채점기가 있는 곳에서만 (2026-09-01)

[[signal-layer]]가 이 위키에서 가장 정밀한 유효 범위 한정을 제시한다. "스케일이 이긴다"를 부정하지 않고, **어디서** 이기는지를 자른다.

> **컴파일러는 무료 채점 도구입니다. 테스트 스위트는 무료 채점 도구입니다.** (…) 작업이 스스로 점수를 매길 수 있게 되는 순간, 모델을 그 점수에 맞춰 계속 개선해 나가면 **결국에는 이기게 되는 거죠.**

따름정리 — **코드 자동화가 가장 먼저 온 것은 우연이 아니라 검증 용이성 때문**이다. 그리고 자동 채점기가 없는 영역(문제 선택·신뢰)은 스케일이 접수하지 못한다.

> 모델은 사용자가 **가리키는 대상을 생성**하지만, **어디를 가리켜야 하는지에 대해서는 아무런 정보도 제공하지 않습니다.**

## 다른 형태의 반례들

같은 주에 들어온 소스들이 서로 다른 축에서 스케일의 한계를 지적한다. 셋을 나란히 두면 반례의 **종류**가 구별된다.

| 소스 | 축 | 논증 |
|---|---|---|
| [[agentic-sites]] | 지연 예산 | 작업을 **선택**으로 좁히면 작은 모델로 충분해진다 — 문제 정의를 줄여 스케일 요구를 낮춤 |
| [[signal-layer]] | 검증 가능성 | 자동 채점기가 **없는** 영역에는 스케일이 도달하지 않는다 |
| [[agent-distributed-systems]] | 환경 불확실성 | 모델 개선은 **에이전트의 오류율**을 낮추지만 네트워크 오류·stale 데이터·악의적 입력은 제거하지 못한다 |
| [[flutter]] ([[tech-bridge-flutter-ai-workflow]]) | 학습 데이터 격차 | *"Flutter는 Python이나 JavaScript에 비해 한참 뒤떨어지기 때문에"* 강한 모델도 Row·Column 대신 컨테이너+패딩을 고른다 — 데이터가 적은 도메인에서는 사람이 쓴 작은 [[agent-skills|스킬]]이 아직 이긴다 |

세 번째가 특히 구조적이다 — 실패 원인이 모델 안이 아니라 **환경 안**에 있으므로, 모델을 아무리 키워도 남는다.

네 번째는 성격이 다르다 — 에세이의 논리 **안에서** 생기는 일시적 반례다. 학습이 이기려면 데이터가 있어야 하고, 데이터가 적은 프레임워크에서는 도메인 지식 주입이 여전히 싸다. 다만 이 반례는 데이터가 쌓이면 사라지는 종류이고, 발표자도 그것을 *"반복해서 입력해야 한다"*는 불편으로만 기술한다.

## 당사자 증언 — 2012년 이전은 실제로 어땠는가

위 표의 "컴퓨터 비전: hand-designed feature vs 대규모 학습" 항목은 에세이의 요약이다. [[tech-bridge-karpathy-transformers-stanford]]가 **그 시절을 통과한 사람의 1인칭 진술**을 준다. [[andrej-karpathy|Karpathy]]는 2011년 비전 파이프라인을 이렇게 회고한다.

> 논문에는 온갖 종류의 다양한 특징 기술자(feature descriptor)를 설명하는 세 페이지 분량의 내용이 있을 거고 (…) 모든 특징 기술자를 추출한 다음, 그 위에 SVM을 적용하는 거죠. (…) 여기저기서 코드를 모아서 실행했는데, **정말 악몽 같았어요.**

> 게다가 그것도 **효과가 없었어요.**

그리고 2012년 AlexNet의 교훈을 에세이와 거의 같은 문장으로 정리한다.

> 그전까지는 **알고리즘에 많은 관심이 쏠렸지만**, 이 연구는 신경망 자체가 **확장성이 매우 뛰어나다**는 것을 보여주었습니다. 이제 **컴퓨팅과 데이터**를 걱정해야 합니다.

이 증언이 더하는 것은 **비용의 질감**이다. 에세이는 도메인 지식 주입이 장기적으로 진다고 말하지만, 이 소스는 그것이 당시 연구자에게 *무엇이었는지* — 여기저기서 코드를 긁어모으는 노동, 그리고 틀려도 어깨를 으쓱하던 정확도 — 를 기록한다. 부수적으로 **어휘의 분열**이라는 두 번째 비용도 드러난다. 분야마다 용어가 달라 논문을 서로 읽을 수 없었고, 수렴은 성능뿐 아니라 **연구자의 이동성**을 돌려줬다.

## 스케일 조건부 단서 — "어느 스케일에 있느냐"

같은 소스가 에세이를 **부정하지 않으면서 적용 조건을 명시**한다. Q&A에서 inductive bias를 언제 넣어야 하냐는 질문에:

> **데이터가 무한하면 실제로 점점 더 적게 인코딩하고 싶어지고 그게 더 잘 작동합니다.** 데이터가 아주 적으면 오히려 편향을 좀 인코딩하고 싶어집니다. 데이터셋이 훨씬 작다면 **convolution이 좋은 아이디어**일 수 있습니다.

> 그래서 **어느 스케일에 있는지에 달려 있습니다.**

이것은 위 [[flutter]] 반례(학습 데이터 격차)와 같은 논리이며, 그 반례가 **일시적인 종류**라는 판정을 뒷받침한다. 데이터가 적은 국면에서는 지식 주입이 이기고, 데이터가 쌓이면 진다.

실무적으로 더 쓸모 있는 부분은 **어디에 넣느냐**다. [[transformer]]에서 inductive bias는 코어에 박히지 않고 두 군데로 factor out되어 있다 — **노드의 연결성**(어텐션 마스크)과 **positional encoding**. 즉 아키텍처가 "지식 주입을 나중에 뺄 수 있는 자리"를 따로 마련해 둔 셈이고, 이는 Bitter Lesson을 아는 설계자가 취할 만한 형태다.

## ⚠️ 정면 반대 입장 — Ghahramani (2026-09-05 ingest)

[[tech-bridge-uncertainty-mathematics]]에서 [[zoubin-ghahramani|Zoubin Ghahramani]]([[google-deepmind]])가 **이 에세이와 정면으로 갈리는 입장**을 편다. 대립 구도를 그가 직접 명시한다.

> AGI 구축에 관해서는 크게 두 가지 입장이 있는데, 하나는 **규모만 키우면 된다**는 것 (…) 다른 하나는 **현재 우리가 할 수 없는 일들을 더 잘 수행할 수 있는 새로운 아키텍처가 필요**하다는 것입니다.

그가 넣자고 하는 구조는 **명시적 확률 표현**이다 → [[bayesian-inference]]. Bitter Lesson의 관점에서 이것은 전형적인 "인간의 구조적 통찰 주입"이고, 따라서 계산량 증가에 밀릴 후보다.

**해소하지 않는다.** 둘 다 소스가 있고, Ghahramani 본인이 대립을 인정하면서 상대를 깎지 않는다.

> 첫 번째 캠프에서는 **많은 진전을 이뤘다**고 생각합니다. (…) 그들의 생각이 **완전히 틀린 건 아니에요. 저도 완전히 맞는 건 아니고요.**

**다만 그가 긋는 선이 이 위키에 유용하다 — 판돈에 따라 답이 갈린다는 것이다.**

> 문제는 **특이한 사례들을 길게 늘어뜨리다 보면(long tail) 몇 가지 허점이 드러날 수 있다**는 점입니다. (…) **챗봇**과 상호작용하는 경우라면, 그 결정들이 그렇게 중대한 결과를 가져오지는 않을 겁니다. 하지만 **신뢰할 수 있는 자율주행 자동차나 진단 결정을 돕는 의료 AI**를 만들려고 한다면, **확률을 정확하게 계산하는 것이 매우 중요**합니다.

이는 위의 "어느 스케일에 있느냐" 단서와 **같은 형태의 조건부**다. 그쪽이 *데이터 양*으로 조건을 걸었다면, 이쪽은 *오류의 비용*으로 건다. 두 조건부를 합치면 Bitter Lesson은 "언제나 참"이 아니라 **데이터가 충분하고 실패 비용이 낮은 국면에서 참**이라는 형태로 좁혀진다.

⚠️ 이것은 이 위키의 정리이지 어느 소스의 주장도 아니다.

그리고 Ghahramani 쪽 반론의 근거는 계산량이 변했다는 것이다 — 학부 시절 최첨단이던 **Connection Machine**이 *"제 주머니의 픽셀 폰보다 실제로 느립니다."* 진행자가 여기에 날린 반박도 함께 기록해 둘 만하다.

> **80년대에도 신경망에 대해 그런 말이 나왔었죠. 당신은 그 실수를 두 번 다시 반복하지 않을 거예요.**

## References

- [원문 (incompleteideas.net, self-signed cert)](http://www.incompleteideas.net/IncIdeas/BitterLesson.html)
- 미러: [cs.utexas.edu PDF](https://www.cs.utexas.edu/~eunsol/courses/data/bitter_lesson.pdf)
- [Wikipedia: Bitter lesson](https://en.wikipedia.org/wiki/Bitter_lesson)
- 본 위키 내 적용: [[agent-harness-design]], [[brain-hands-decoupling]], [[anthropic-managed-agents]]
- ⚠️ 반대 입장: [[tech-bridge-uncertainty-mathematics]] · [[bayesian-inference]] · [[zoubin-ghahramani]]
