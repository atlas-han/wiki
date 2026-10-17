---
title: Cognitive Offloading
type: concept
category: technique
tags: [education, llm, learning]
related: [regulatory-capture, retrieval-practice, ai-assisted-learning, ai-flipped-classroom]
first-seen: tech-bridge-andrew-ng-ai-opportunity
sources: [tech-bridge-andrew-ng-ai-opportunity, tech-bridge-ai-engineer-three-tier-skill-stack, tech-bridge-learn-anything-with-ai, tech-bridge-hassabis-fry-creativity-future]
created: 2026-08-31
updated: 2026-10-16
---

# Cognitive Offloading

인지 작업을 도구에 넘겨 당장은 성과가 나지만 인간 쪽 retention·숙달이 떨어지는 현상. [[andrew-ng|Andrew Ng]]([[tech-bridge-andrew-ng-ai-opportunity]]): 통상의 LLM 사용은 숙제 점수는↑, 장기 성과는↓ — "일을 대신 시키기" 때문.

Wikipedia/검색은 사실 도구로 괜찮지만, 모델에게 일을 시켜 버리면 학습에 해롭다. 학습에 좋은 사용법이 없다고는 하지 않음. 본인조차 6개월 전 AI로 푼 front/back을 기억 못 해 다시 물은 경험이 있다.

제품 응답이 [[learnvector|LearnVector]](1:1 개인화). 자녀 교육 논의에서도 같은 축: 계산기 없이 곱셈 연습은 가능하나, 나이가 들면 AI 오프로딩이 retention을 해칠까 우려.

## References

- [[tech-bridge-andrew-ng-ai-opportunity]] · [[andrew-ng]] · [[learnvector]]

## 어디까지 오프로드해도 되는가 — 읽기는 남긴다 (2026-09-16 · [[tech-bridge-ai-engineer-three-tier-skill-stack]])

이 페이지는 *무엇이 손상되는가* 만 갖고 있었다. [[cedric-clyburn|Cedric Clyburn]]([[ibm|IBM Technology]])이 **하한선**을 긋는다: *"Python 마법사가 될 필요는 없고, **에이전트가 쓰는 코드를 읽고 이해할 수 있을 정도로만** 유창하면 된다"*(03:10~03:20). **쓰기는 오프로드하고 읽기는 남긴다** — Ng의 우려에 대한 *무엇을 남기면 되는가* 형의 답이다. ⚠️ 두 소스는 서로를 모르고, Ng의 사례(학생의 숙제)와 이 소스의 대상(AI 엔지니어 지망자)은 다르다. → [[read-fluency-for-agent-output]]

## 어떻게 쓰면 손상되지 않는가 — 역할을 나눈다 (2026-10-09 · [[tech-bridge-learn-anything-with-ai]])

세 번째 답은 **절차**다. [[nick-saraev|Nick Saraev]] 클립 + [[tech-bridge|Tech Bridge]] 내레이션: 기억은 정보를 다시 읽을 때가 아니라 **꺼낼 때** 남는다([[retrieval-practice]] — 다시 읽기 4회는 일주일 뒤 40%, 1회 읽고 3회 시험은 61%; ⚠️ 61%와 정정은 내레이션에만, 원 연구는 설명란에만). AI 설명을 읽는 것은 재학습 쪽이라 Saraev는 그것을 *"a passive consumption mechanism. You're just reading."*(02:37~02:42)이라 부른다. 처방은 [[ai-assisted-learning|역할 분담]] — **준비·정리는 AI에게, 인출·풀이·설명은 나에게**. 내레이션이 Ng의 우려를 그대로 옮긴다: *"막힌 문제를 고민하는 시간을 전부 AI의 답으로 채우는 거죠. 결과는 얻어도 내가 할 수 있는 일은 늘지 않을 수 있어요."*(ko 15:58~16:06). Ng = 증상, Clyburn = 하한선(읽기는 남긴다), 이 소스 = 역할별 분업표. ⚠️ 세 소스는 서로를 모른다.

> ⚠️ **Contradiction (약) — 2026-10-13 · [[tech-bridge-hassabis-fry-creativity-future]].** [[demis-hassabis|Demis Hassabis]]는 암기(*rote learning*)를 *"out of class with the help of AI tools because I think that's exactly what AI tools are good for"*(38:17~38:23)라고 한다. Ng의 *"일을 대신 시키기"* 우려와 방향이 다르다. 다만 하사비스의 도구는 약한 부분의 문제를 더 내주는 개인 교사(38:24~38:33)이고 *"in a very intentional way again that helps with the learning"*(38:05~38:09)을 조건으로 단다 — 정면 충돌은 아니다. → [[ai-flipped-classroom]]
