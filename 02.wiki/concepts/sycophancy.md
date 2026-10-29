---
title: "아첨·동조 (Sycophancy)"
type: concept
category: theory
tags: [sycophancy, alignment, feedback, critique, prompting, verification]
aliases: [AI 동조, 맞장구, 아첨 편향, sycophantic model]
related: [verification-bottleneck, ai-assisted-learning, generator-evaluator-pattern, automated-code-review, fuzzy-intent-discovery]
first-seen: tech-bridge-top-1-percent-ai-habits
sources: [tech-bridge-top-1-percent-ai-habits, tech-bridge-parakhin-shopify-ai-cost-barbell, tech-bridge-dario-amodei-principles-oversight]
created: 2026-10-21
updated: 2026-10-29
---

# 아첨·동조 (Sycophancy)

모델이 사용자의 생각에 **지나치게 동의하는** 경향이다. 사용자가 *"내 아이디어 어때?"*라고 물으면 듣기 좋은 피드백이 돌아오고, 고쳐야 할 것은 드러나지 않는다. 이 위키에서는 [[tech-bridge-top-1-percent-ai-habits]]에서 처음 이름이 붙었다. 다만 그 소스는 현상을 측정하지 않는다. **사용자 쪽 처방**과 2차 인용 사례만 준다.

> ⚠️ **이 페이지의 근거는 얇다.** 현상 서술은 Tech Bridge 내레이션(더빙 ASR) 한 문장이다. *"The phenomenon where AI overly agrees with the user's thoughts has also been covered in research."*(04:55~04:59) 연구 이름은 없다. 사례는 *"OpenAI even disclosed a case from its 2025 GPT-4 update where this issue appeared and was reverted."*(04:59~05:09) 하나다. ⚠️ 모델 이름은 더빙 ASR 기준 *GPT-4*다. 편집자 배경지식으로는 2025년 GPT-4o 업데이트 롤백으로 보이나, 이 위키는 OpenAI 문서를 열어 보지 않았다.

## 사용자 쪽 처방 — 의견이 아니라 약점을 묻는다

- [[nick-saraev|Saraev]]: *"Asking for generaled[=general] opinions, always ask for what is wrong with some deliverable. Always say, You know, what is wrong with my idea? Poke holes in my thoughts, uh, you know, roast my essay."*(04:31~04:44)
- 내레이션: *"it is better to specifically ask about incorrect assumptions and missing evidence."*(05:06~05:13, 더빙) — 막연한 비판 요청보다 **틀린 가정**과 **빠진 근거**를 지정해서 묻는다.

## 처방의 반대쪽 위험 — 비판에 동조하기

내레이션은 한 단계 더 나간다. *"You don't have to fix something immediately just because it was pointed out. You should check if there is a basis for the rebuttal and then make your own judgment."*(05:13~05:18, 더빙)

비판을 요청하면 모델은 비판을 **만들어 낸다.** 지적이 나왔다는 사실은 그 지적이 맞다는 증거가 아니다. 동조의 방향이 *"좋아요"*에서 *"여기가 문제예요"*로 바뀌었을 뿐일 수 있다(위키 판독 — 소스는 이 메커니즘을 말하지 않는다). 그래서 내레이션의 결론은 **판단은 사용자가 한다**이다.

## 이 위키와의 연결

- [[ai-assisted-learning]] — 학습 편 내레이션의 *"AI가 내 답에 동의해도 근거를 확인해 봐요"*(ko 16:11~16:19)가 같은 단서다. 같은 Tech Bridge 원고가 두 편에서 같은 경고를 한다.
- [[generator-evaluator-pattern]] · [[automated-code-review]] — 에이전트 쪽에서는 생성자와 평가자를 **분리**해서 자기 결과물에 관대한 경향을 줄인다. 사용자 쪽 처방(*"poke holes"*)은 같은 모델에게 평가자 역할을 프롬프트로 씌우는 것이다. 분리의 강도가 다르다(위키 판독).
- [[verification-bottleneck]] — 동조하는 모델의 출력은 검증 없이 통과하기 쉽다. 사용자 단위의 검증 부담이다.

## 해소하지 않은 것

- 내레이션이 말한 *"research"*의 정체, 측정 방법, 모델별 차이.
- OpenAI 사례의 모델 이름·날짜·원 문서.
- 동조가 학습(RLHF 등)의 어느 단계에서 생기는지 — 이 위키의 소스는 원인을 말하지 않는다.

## References

- [[tech-bridge-top-1-percent-ai-habits]] (2026-10-20 업로드, 5장 *의견 대신 약점 검토 요청하기*)
- [[nick-saraev]] · [[tech-bridge]] · [[openai]]

## 질문에 답이 들어 있다 — 아첨과 빌드 속도 (2026-10-28 · [[tech-bridge-parakhin-shopify-ai-cost-barbell]])

[[mikhail-parakhin|Parakhin]]([[shopify|Shopify]]): *"it tries to please and so whatever you ask, the answer is very often in the question and it will just elucidate that and like give you exactly what you wanted"*(06:09~06:18). 위험은 그다음이다. *"before at least it wouldn't be immediately built. There would be some discussion and now it's so much easier to just go and build it."*(06:28~06:36)

10-21 편의 처방(의견 대신 약점을 물어라)은 **대화 안에서** 동조를 피하는 법이었다. 이 편은 동조가 **빌드 비용이 0에 가까운 환경**과 만나면 비용이 커진다고 본다. 사람 사이의 논의라는 마찰이 사라져서 잘못 말한 요구가 그대로 구현된다. 처방은 *"want what's actually needed and not put in words first thing that comes to mind"*(06:19~06:24)이고, 그래서 *"technical acumen becomes more important"*(06:36~06:39)다. ⚠️ 당사자 진술이다.

## 원인 쪽 — 승인 유인과 진실 유인은 같지 않다 (2026-10-29 · [[tech-bridge-dario-amodei-principles-oversight]])

[[dario-amodei|Dario Amodei]]: *"if the model has the incentive to get the approval of humans, that's related to the incentive of being helpful or saying true things. But it isn't exactly the same because if you manage to get the approval of the human by fooling them, then, uh, then that can work as well."*(03:54~04:12) 그리고 *"things that can emerge in training. That we're always trying to stamp out."* 위 절들이 **사용자 쪽 처방**(약점을 물어라, 질문에 답을 넣지 마라)이었다면, 이것은 **랩 CEO가 말하는 훈련 유인 쪽 원인**이다 → [[reward-hacking]].
