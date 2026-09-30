---
title: "Valued Work per Watt — 가치를 재고, 그 가치를 싸게 얻는가"
type: concept
category: theory
tags: [metrics, economics, value, efficiency, fine-tuning, evals, vertical-ai]
aliases: [valued work per watt, value of work per watt, valuable work per watt, 와트당 가치 있는 작업량, 와트당 가치]
related: [value-maxing, token-minimization-trap, mousepower, agent-roi-measurement, model-mixing-economics, loop-is-the-product, agent-recipes, taste-encoded-evals, cursor, cognition]
first-seen: tech-bridge-introspection-loop-is-the-product
sources: [tech-bridge-introspection-loop-is-the-product]
created: 2026-09-30
updated: 2026-09-30
---

# Valued Work per Watt

**에이전트 시스템이 최적화할 점수는 "와트당 가치 있는 일"이고, 순서는 두 단계 — 먼저 가치를 측정하고(무엇이 좋은 일인가), 그다음 그 가치를 필요 이상으로 비싸게 얻고 있지 않은지 확인한다 — 라는 프레이밍.** [[roland-gavrilescu|Roland Gavrilescu]]([[introspection-dev|Introspection]])가 [[tech-bridge-introspection-loop-is-the-product]]에서 세 번째 아이디어로 제시했다.

> *"how much value am I getting per watt? Um how do I measure the value is the first step, and how do I know I'm getting a good deal on that value is the second."* (09:38~09:49)

> ⚠️ **표기.** en-orig는 *"valued work per watt"*(09:05~09:07)와 *"value of work per watt"*(17:16~17:18) 두 가지, `en`은 17:18에 *"valuable work per watt"*, 설명란은 *"와트당 가치 있는 작업량"*. 이 위키는 첫 발화를 따른다. **와트를 실제로 어떻게 재는지는 말하지 않는다** — 맺음말에서는 **가격 차이**로 바뀐다(아래). 전력 단위인지 비용의 비유인지 미확정. ko는 09:45~09:47의 두 번째 단계를 **"그 정도의 가치를 가진 기업은 두 번째로 큰 기업입니다"** 로 창작했다.

## 모델 경로 — 제품 → eval → 모델 (09:09~09:27)

> *"Think of how um Cursor and Cognition went from building the best product to then uh building the best evals for the product, and finally building the best models based on the previous two artifacts. We think this is like the recipe for everything going forward."*

코드가 첫 성공 도메인이었고, 법률·연구 등도 *"everything is going to come down to this idea"*(09:35~09:38)라고 본다. → [[cursor]] · [[cognition]]

⚠️ **근거 없는 사례 서술.** 이 위키의 [[cursor]] 페이지에는 자체 모델 Composer가 있어 *"최고의 모델"* 단계와 방향은 맞지만, **"최고의 eval" 단계를 뒷받침하는 기록은 없다.** [[cognition]]의 자체 모델에 대한 기록도 이 위키에 없다.

## 세 지점 — 기본 → 프런티어 → 경제성 (09:51~10:44)

| 지점 | 어떻게 가나 | en-orig |
|---|---|---|
| **기본** | 기본 하네스 + 기본 eval | *"We've all started from a base uh harness and a base set of evals"*(09:53~10:00) |
| **프런티어** | 프로덕션에서 돌려야만 안다 | *"you only go through that by running the systems in prod. There's no way you you know what frontier is before you uh you start"*(10:02~10:09) |
| **경제성** | 같은 가치를 덜 쓰고 | *"once you've reached frontier, how do we make this um uh economically viable, which is how do we not spend more than than uh we need for generating this amount of value"*(10:15~10:26) |

마지막 단계는 *"what is requiring a lot of research"*(10:11~10:15)라고 한다. 도구는 이미 있다 — *"all these uh fine-tuning APIs, all the infrastructure that has been uh abstracted away"*(10:36~10:40) — *"It's just that the know-how that uh is not there yet"*(10:42~10:44). 그 know-how가 *"how to codify taste into evals and how to validate that in experiments"*(10:50~10:55)이다 → [[taste-encoded-evals]].

## 맺음말의 판정 기준 (17:16~17:38)

> *"value of work per watt is how you should measure um Am I making progress or not? So, first, make sure that the the the work you're generating is valuable. Second, make sure that the economics make sense. And the the the difference in price is is basically what people would would switch away from cloud code to to something you provide."*

즉 실무 척도는 **범용 에이전트([[claude-code|Claude Code]] — en-orig *"cloud code"*, 추정) 대비 가격 차이**다. 수직 에이전트가 범용 코딩 에이전트보다 **같은 가치를 더 싸게** 줄 때 사람들이 옮겨 온다는 논리. ⚠️ 이 문장은 ASR이 더듬어 뜻이 완전하지 않다.

## 이 위키의 다른 지표 논의와

- [[value-maxing]] — *토큰맥싱도 토큰 최소화도 같은 함정, 최적화 대상은 결과*. 순서가 같다: **가치(결과)를 먼저**. 차이는 분모 — value-maxing은 분모를 따로 두지 않고 결과 질문(배포·개발자 시간·재작업)을 던지고, 이 페이지는 **분모(와트·가격)를 명시**한다.
- [[token-minimization-trap]] — 분모만 줄이면 비용이 옮겨 간다. 이 페이지는 **분자(가치)를 먼저 고정한 뒤** 분모를 줄이라는 순서라 그 함정을 피하는 구조다. ⚠️ 위키의 정리 — 화자는 이 함정을 언급하지 않는다.
- [[mousepower]] — [[james-watt|와트]]의 마력 선례를 빌려 *정밀하지 않아도 가치를 전달하는 단위*를 찾는다. 이 페이지도 **와트**를 쓰지만 **전달용 은유가 아니라 최적화 점수**로 쓴다(*"the score to really optimize for"* 09:07~09:09). 둘 다 측정 장치는 없다.
- [[model-mixing-economics]] — 단계별 모델 선택을 예산 문제로. *경제성* 단계의 구체 수단 중 하나.
- [[agent-roi-measurement]] — 에이전트의 가치를 전달할 척도가 없다는 문제 제기. 이 페이지는 척도의 **이름**을 주지만 측정법은 주지 않는다.

## ⚠️ 유보

- **와트의 측정** — 전력·토큰·가격 중 무엇인지 없다.
- **"가치"의 측정** — 첫 단계라 하면서 방법은 [[taste-encoded-evals]](제작자 taste + 사용자 A/B)로 넘긴다. 즉 가치 = **제작자와 사용자가 동의하는 좋음**이다.
- **Cursor·Cognition 경로** — 근거 없음.

## References

- [[tech-bridge-introspection-loop-is-the-product]] (first-seen)
- 관련: [[value-maxing]] · [[mousepower]] · [[token-minimization-trap]] · [[agent-recipes]] · [[taste-encoded-evals]] · [[cursor]] · [[cognition]]
