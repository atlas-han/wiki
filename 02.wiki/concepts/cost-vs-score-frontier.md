---
title: "비용 대비 점수 프런티어 (Cost-vs-Score Frontier) — 모델 선택을 '왼쪽 위'로 읽기"
type: concept
category: theory
tags: [model-selection, benchmark, pareto-frontier, cost, evaluation, leverage, thinking-modes]
aliases: [cost vs score, 비용 대비 점수, Pareto frontier of cost and score, 비용-점수 그래프, leverage]
related: [true-cost-to-perfect-answer, model-mixing-economics, pareto-surfing, fixed-budget-alpha, inference-speed-as-capability, value-maxing, document-parsing-for-agents, taste-vs-judgment]
first-seen: tech-bridge-nick-saraev-gpt-6-1-terra-vs-opus-5-5
sources: [tech-bridge-nick-saraev-gpt-6-1-terra-vs-opus-5-5]
created: 2026-11-02
updated: 2026-11-02
---

# 비용 대비 점수 프런티어

**벤치마크 점수를 단독 순위가 아니라 작업당 비용(x)과 점수(y)의 2차원 위에 놓고, '왼쪽 위'(싸고 높음) 경계선에 있는 모델을 고르는 읽기 방식이다. 그러면 질문이 "누가 1등인가"에서 "최고점의 몇 %를 몇 분의 1 비용에 얻는가"로 바뀐다.** 이 위키에서는 [[nick-saraev|Nick Saraev]](추정)가 [[tech-bridge-nick-saraev-gpt-6-1-terra-vs-opus-5-5]]에서 [[openai-terra|GPT-6.1 Terra]] 랜딩 페이지의 그래프를 시청자에게 풀어 주는 것으로 처음 나온다.

> *"what this is is cost versus score. It's basically the efficiency of a model per dollar to do the stuff that you're asking it to do."*(08:04~08:13) · *"anything in the top left-hand corner is cheaper and it scores higher."*(08:38~08:43)

## 읽는 법 (화자의 설명)

| 요소 | 내용 |
|---|---|
| x축 | 작업당 비용 — 이 그래프는 최대 $8(08:13~08:20) |
| y축 | 표준 벤치마크 점수 — Agents' Last Exam 35~65%(08:20~08:28, ⚠️ 표기 미확정) |
| 목표 | 왼쪽 위. *"GPT-6.1 Terra is basically leading what's called the Pareto frontier"*(08:55~09:00) |
| 모드 | 같은 모델의 사고 모드가 점 여러 개로 찍힌다 — *"there really isn't that big of a difference in cost between the lowest thinking mode and then the highest thinking mode."*(09:06~09:13) |
| 결론 단위 | 최고점 대비 비율 / 비용 비율 — *"90, I don't know, 7%[=97%] of performance for 1/9 or maybe 11% cost"*(10:04~10:12) |

같은 축을 뒤집은 변형도 있다: 사실 오류율 그래프는 y가 *"answers with any factual error"* 라 *"lower here is actually better."*(10:53~10:54) — 이때 목표는 왼쪽 아래다.

## 이 읽기가 만드는 결론 — "leverage"

> *"maybe you gain a couple percentage points of, you know, score, but at what cost, right? This is about a dollar and Opus 5.5 here is about nine."*(09:54~10:02) · *"That, ladies and gentlemen, is leverage."*(11:44~11:46)

최상단 모델([[claude-opus-5-5|Opus 5.5]])이 여전히 1등이어도, 몇 %p를 위해 9배를 내지 않는 선택이 *"a trade-off that a lot of people are willing to make"*(10:08~10:15)로 정당화된다. 같은 화자는 실사용 데모에서도 비용 배수를 기준선으로 쓴다 — *"definitely not 1/12 the quality"*(02:35~02:39), *"definitely not 12 times better"*(03:24~03:26).

## 이 읽기의 한계 — 같은 영상 안의 단서

- **벤치마크 자체의 가치**: *"the benchmarks themselves are not super valuable or important these days. It's virtually impossible to tell how a model really feels in your hands."*(07:43~07:51)
- **점수로 안 잡히는 품질**: 게임은 *"not really like quantitative, right? It's more like qualitative."*(04:50~04:55) — 그리고 그 게임에서는 비싼 쪽을 고른다(*"this is something that I would actually play"* 04:55~04:58). 상단의 작은 차이가 결정적인 작업에서는 frontier 읽기가 답을 주지 않는다 → [[taste-vs-judgment]]
- 하루 전 같은 화자도 반대 방향 단서를 달았다: *"the better you get at quality, the more even a slight percentage improvement makes to the end result."*([[tech-bridge-nick-saraev-kimi-k3-1-vs-opus-5-5]] 09:52~10:00)

## 이 위키의 다른 페이지와

- [[true-cost-to-perfect-answer]]: x축이 *작업당* 비용이면 이 페이지의 단위(쓸 수 있는 답 하나당 비용)에 가깝다. 그러나 점수(y)가 평균 정확도라면 **합격률을 분모에 넣은 진짜 비용**은 따로 계산해야 한다 — 3%p 차이가 재실행 횟수로 증폭될 수 있다. ⚠️ 화자의 그래프가 어떻게 계산됐는지 미상.
- [[pareto-surfing]]: 같은 *Pareto frontier* 단어지만, 그쪽은 **파이프라인 부품을 바꿔 가며 frontier를 밀어내는 일**이고, 이쪽은 **공개된 점들 가운데서 고르는 일**이다.
- [[model-mixing-economics]]: frontier에서 *"most like 90th percentile applications"*(11:18~11:23)는 싼 모델, *"upper echelons of quality"*(11:28~11:35)는 비싼 모델 — 화자의 결론이 사실상 작업 등급별 혼합이다.
- [[document-parsing-for-agents]]: 좁은 도메인에서 *"at the Pareto frontier of cost and accuracy"* 를 주장한 벤더 진술이 이미 있다 — 같은 그림을 벤더가 자기 위치 주장에 쓴다.
- [[inference-speed-as-capability]]: 이 2차원 그림에는 **속도 축이 없다.** 같은 영상의 데모에서 Terra는 절반 시간에 끝났다(00:57~01:03) — 세 번째 축은 따로 본다.

## ⚠️ 유보

- 근거는 사용자 1인이 **출처를 밝히지 않은 그래프**(Terra 랜딩 페이지 — OpenAI 자료로 추정)를 눈대중으로 읽은 것이다. 벤더 그래프는 비교 대상 · 조건 선택이 벤더 몫이다.
- "$1 vs $9", *"95 to 97%"*, *"11%"* 는 화자 진술이고 위키가 확인하지 않았다.
- 페이지 하나로 일반화하기엔 소스가 하나다 — 이후 소스로 보강 필요.

## References

- [[tech-bridge-nick-saraev-gpt-6-1-terra-vs-opus-5-5]] — first-seen
- [[openai-terra]] · [[claude-opus-5-5]] · [[nick-saraev]]
- 관련: [[true-cost-to-perfect-answer]] · [[pareto-surfing]] · [[model-mixing-economics]] · [[document-parsing-for-agents]] · [[inference-speed-as-capability]] · [[taste-vs-judgment]]
