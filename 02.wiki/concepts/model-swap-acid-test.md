---
title: 모델 교체 시금석 (Model-Swap Acid Test)
type: concept
category: pattern
tags: [model-portability, private-eval, lock-in, harness, context, learning-loop, enterprise-architecture]
aliases: [replace any model, 사적 eval 시금석, 모델을 갈아 끼워도 오르는 평가, private eval acid test]
related: [company-knowledge-moat, tools-and-context-over-harness, model-harness-knowledge-stack, model-mixing-economics, automatic-model-routing, cross-model-prior-intersection]
first-seen: tech-bridge-nadella-pragmatic-engineer-after-code-is-cheap
sources: [tech-bridge-nadella-pragmatic-engineer-after-code-is-cheap]
created: 2026-11-20
updated: 2026-11-20
---

# 모델 교체 시금석 (Model-Swap Acid Test)

**어떤 모델로 갈아 끼워도 회사의 사적 eval을 여전히 통과할 수 있는가 — 그럴 수 없다면 회사의 가치가 모델에 새어 나가 있다는 판정 기준.** [[satya-nadella|Satya Nadella]]가 The Pragmatic Engineer 인터뷰에서 *acid test* 라 부른 것이다([[tech-bridge-nadella-pragmatic-engineer-after-code-is-cheap]], 한국어 해설).

> *"you should be able to replace any model and still clear an eval—that's your private eval."*(12:24~12:31)
>
> *"If you can't do that, then you have to ask yourself, how are you a firm"*(12:32~12:35)

⚠️ 두 인용은 인터뷰 원음 발췌이지만 **en-orig 단일 트랙** 의 ASR이다(ko-orig는 이 구간이 비어 대조할 수 없다).

## 논리

1. **지식은 흩어져 있다** — Nadella는 Hayek을 끌어온다: *"It's all about knowledge being distributed."*(11:00~11:02) 그래서 세상의 지식을 다 가진 모델 하나가 나온다는 생각을 믿지 않는다. *"every firm needs to be in control of it"*(11:14)
2. **토큰이 자본이 된다** — *"사람과 함께 토큰이 회사의 자본이 된다는 거죠."*(11:25~11:26) 그 자본은 회사 지식을 담은 오픈 모델일 수도, 컨텍스트 층일 수도 있다.
3. **그러므로 떼어 놓는다** — *"그래서 하네스와 컨텍스트, 메모리, 행동 공간을 특정 모델과 떼어 놓으라고 합니다. 안 그러면 꼼짝없이 묶인다고요."*(11:32~11:38)
4. **학습 고리는 회사의 것** — *"You as a firm need to be in charge and control of your own learning loop."*(12:01~12:06)
5. **판정** — 위 넷이 지켜졌는지는 모델을 바꿔 보면 안다. 해설이 시청자에게 돌린 질문: *"내일 모델을 바꿔도 우리 만의 평가 점수는 계속 오를까요?"*(12:45~12:47)

## 위키에서의 좌표

- [[tools-and-context-over-harness]] — Lopopolo는 *하네스를 고정하고 최신 모델을 즉시 갈아 끼우라* 고 했다. 방향은 같고(모델은 교체 부품), Nadella는 여기에 **통과 조건** 을 단다: 갈아 끼운 뒤에도 사적 eval이 선다.
- [[company-knowledge-moat]] — 해자는 회사 고유 지식에 있다는 프레이밍. 이 시금석은 그 해자가 **실제로 회사 쪽에 있는지** 를 재는 절차다.
- [[model-mixing-economics]] · [[automatic-model-routing]] — 라우터가 모델을 고르는 설계는 이 시금석을 이미 전제한다. 09-29 대담의 *"The real model is my model that routes"* 가 제품 쪽의 같은 생각이다.
- [[cross-model-prior-intersection]] — 같은 인터뷰에서 Nadella는 검증을 *다른 모델 가문* 에 맡기라고도 한다. 모델을 여럿 쓸 수 있어야 가능한 일이다.

## ⚠️ 유보

- **파는 쪽의 말이다.** Microsoft는 여러 모델을 얹는 플랫폼(Foundry · Copilot의 라우터)을 판다 — 모델에 묶이지 말라는 권고는 자사 제품의 가치 제안과 겹친다.
- *사적 eval* 을 어떻게 만드는지, 통과선이 무엇인지는 소스에 없다. 해설의 한국어 문장은 *"계속 오를까요"* 이고 원음은 *"still clear an eval"* 이다 — 오르는 것과 통과하는 것은 다르다(원음을 따른다).
- 아키텍처 결정이 *둘* 이라고 하는데 내레이션은 첫째(학습 고리)만 센다.

## References

- [[tech-bridge-nadella-pragmatic-engineer-after-code-is-cheap]] — 출처
- [[satya-nadella]] · [[microsoft]] · [[company-knowledge-moat]] · [[tools-and-context-over-harness]]
