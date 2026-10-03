---
title: "머지 가능성 격차 (Mergeability Gap)"
type: concept
category: theory
tags: [code-review, benchmarks, verification, swe-bench, frontiercode, metr, training-signal, goodhart]
aliases: [테스트 통과 ≠ 머지 가능, mergeability, 머지 적합성]
related: [verification-bottleneck, automated-code-review, verifiable-goals, reward-hacking, syntactically-correct-behaviorally-wrong, signal-layer, test-harness-vs-test-authoring, sutton-bitter-lesson]
first-seen: tech-bridge-death-of-code-review
sources: [tech-bridge-death-of-code-review]
created: 2026-10-03
updated: 2026-10-03
---

# 머지 가능성 격차

**"테스트를 통과했는가"와 "관리자가 이걸 머지하겠는가"는 다른 질문이고, 둘 사이의 격차가 크다.** 업계가 코딩 품질의 대리 지표로 써 온 테스트 통과율(SWE-bench류 채점기)이 실제 머지 판단을 절반 정도밖에 설명하지 못한다는 진단. [[laurie-voss|Laurie Voss]]가 [[tech-bridge-death-of-code-review]]에서 METR·FrontierCode·Sarah Guo를 엮어 제시했다.

> *"For years, the industry's proxy for uh reliable for quality has been whether the tests passed uh because that is what the benchmarks measured."* (06:24~06:37)

## 증거 (모두 화자의 2차 인용)

| 출처 | 설계 | 결과 | en-orig |
|---|---|---|---|
| **METR** (2026-03) | SWE-bench 대상 프로젝트의 현역 관리자 4명이 **SWE-bench 채점기를 통과한 PR**을 다시 판정 | *"only good enough to merge about half of the time"* — 실패는 정확성이 아니라 **코드 품질**과 **테스트 밖의 다른 코드를 조용히 깨뜨린 변경** | 06:35~07:23 |
| **FrontierCode** ([[cognition\|Cognition]], 2026-06) | 관리자 20명+가 자기 저장소에서 과제 150개(각 40시간+). 채점: 동작 정확성·회귀·안전·범위 규율·테스트 품질·유지보수성 — *"a human review rubric uh made machine checkable"* | [[fable-5-1\|Fable 5]] SWE-bench Pro **88%** vs FrontierCode 최난도 구간 **29%**, GPT 5.5 **6% 미만** | 07:50~08:54 |

> *"the strongest models we have are nowhere near uh passing human review reliably."* (08:51~08:57)

⚠️ METR 쪽 단서: 에이전트에게 **피드백을 받고 다시 시도할 기회가 없었다**(07:26~07:36). 화자는 그게 곧 사람을 루프에 넣는 것이라 무관하다고 본다. ⚠️ 화자의 *"51 points less"*(08:33~08:35)는 88−29 = 59와 맞지 않는다. ⚠️ 29%는 FrontierCode **전체가 아니라 최난도 구간**이다.

## 왜 격차가 생기는가 — 테스트가 못 보는 맥락

Sarah Guo의 예(Voss 인용): 테스트 통과는 *"this module exists because there are three external users of this module"*, 또는 *"this cron job that nobody will admit to writing that relies on that module existing"* 을 알려 주지 않는다(19:19~19:37). → *"There is context outside of the test suite that the tests don't uh can't find."* [[bun|Bun]] 포팅의 **unsafe 블록 13,044개**(vs 사람 코드 약 74)도 같은 구조 — *"the test suite can certify behavior at the public interface (…) it cannot certify 13,000 assertions that the test suite was never designed to look for"*(16:55~17:04). → [[syntactically-correct-behaviorally-wrong]]

## 왜 중요한가 — 격차는 곧 학습 신호가 된다

Sarah Guo의 논리(Voss 인용, 09:09~09:56):

1. 모델이 코드에서 빨리 좋아진 이유는 *"a compiler is a free verifier. A test suite is a free verifier"* — 싸게 검증할 수 있는 것은 이길 때까지 학습할 수 있다.
2. 그러므로 **머지 가능성을 기계가 채점할 수 있게 되는 순간**, 그것은 측정이 아니라 *"would immediately become a training signal for the frontier models"*.
3. ⭐ *"whoever writes today's review standard is writing next year's default model behavior."* (10:07~10:09)

선례로 CriticGPT(2024, [[openai|OpenAI]])를 든다 — 모델 코드의 버그를 잡는 모델이 학습 신호가 되어 모델에 들어갔다(10:13~10:36). 그리고 지금의 자동 리뷰 업체들은 이미 *사람 수락률* 로 하네스를 학습시키고 있다 — *"a preview of what the models are going to do"*(14:31~14:36) → [[automated-code-review]].

> *"mergeability standards are still in the future right now. We do not have a good rubric that captures everything that a human decides"* (10:38~10:50)

## 이 위키에서의 좌표

- **[[verifiable-goals]]** · **[[signal-layer]]** — *검증할 수 있는 것은 학습할 수 있다* 의 코드 리뷰판. [[tech-bridge-signal-layer]]의 [[lena-hall|Lena Hall]]이 **같은 Sarah Guo 문장**을 *"왜 코드가 먼저 자동화됐나"* 의 근거로 썼다면, 여기서는 **다음 경계가 어디인가**(머지 가능성)의 근거다.
- **[[reward-hacking]]** — 테스트만 통과하는 코드는 *대리 지표를 최적화한* 결과. 격차의 존재가 곧 대리 지표 최적화의 흔적이다.
- **[[verification-bottleneck]]** — 사람 리뷰가 병목인 이유 중 하나가 이 격차다: 테스트 통과를 믿을 수 없으니 사람이 읽어야 한다.
- **[[sutton-bitter-lesson]]** — 채점기가 생기면 규모가 이긴다는 같은 논리가 *머지 가능성* 에도 적용된다는 예측.

## ⚠️ 유보

- **원 자료를 열어 보지 않았다** — METR 연구, FrontierCode, Sarah Guo의 글 모두 화자의 요약이다.
- 머지 가능성 루브릭이 학습 신호가 되면 **그 루브릭 자체가 Goodhart 대상**이 된다 — Voss는 이를 언급하지 않는다(*"benchmark scaffolds have been caught leaking answers"* 21:41~21:44만).
- 한 소스. 같은 격차를 직접 측정한 두 번째 소스가 들어오면 갱신한다.

## References

- [[tech-bridge-death-of-code-review]] · [[laurie-voss]]
- 관련: [[automated-code-review]] · [[verification-bottleneck]] · [[verifiable-goals]] · [[signal-layer]] · [[syntactically-correct-behaviorally-wrong]] · [[cognition]] · [[fable-5-1]]
