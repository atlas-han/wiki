---
title: 데모와 협업의 간극 (Demo–Collaboration Gap)
type: concept
category: theory
tags: [evaluation, benchmarks, long-running-agents, model-launch, user-experience]
related: [cost-vs-score-frontier, jagged-capability-frontier, minimizing-reader-load, openai-astra, fable-5-2]
first-seen: tech-bridge-gpt-6-2-astra-launch-day-reactions
sources: [tech-bridge-gpt-6-2-astra-launch-day-reactions]
created: 2026-11-19
updated: 2026-11-19
---

# 데모와 협업의 간극 (Demo–Collaboration Gap)

**한 번에 뽑아내는 결과물과 벤치마크에서는 최고인 모델이, 며칠씩 같이 일하는 사람에게는 괴로울 수 있다는 관찰.** GPT-6.2 [[openai-astra|Astra]] 출시 첫날 반응을 모은 [[tech-bridge-gpt-6-2-astra-launch-day-reactions]]의 테제다. 이름은 위키가 붙였다 — 해설은 *간극* 이라고만 부른다.

> *"한 번에 뽑아내는 데모와 벤치마크는 최고인데 며칠씩 같이 일한 사람들은 힘들어합니다."*(06:45~06:51)

> ⚠️ 소스 하나, 출시 하루 이틀 사이의 조기 접근자 몇 명의 자기 보고다. 해설 스스로 *"미리 써 본 몇 사람의 경험이고 벤치마크 숫자가 틀렸다는 뜻도 아닙니다."*(08:34~08:37) 라고 유보한다.

## 간극이 드러나는 자리 (해설 전달)

| 한 번의 과제가 재는 것 | 같이 일할 때 드러나는 것 |
|---|---|
| 점수 · 비용([[cost-vs-score-frontier]]의 왼쪽 위) | **멈춤** — 사용자가 알 길 없는 것을 묻고 서 있다. [[theo|Theo]]는 멈췄는지 확인하는 에이전트를 따로 돌렸다 |
| 결과물의 품질(3D · 게임 · 영상) | **설명** — 끝난 뒤의 설명을 사람이 알아듣기 어렵다 → [[minimizing-reader-load]] |
| 한 번의 놀라움 | **제자리** — 오래 돌고도 반영된 개선이 없다 · 부탁 하나에 꽂힌다(더 작게 → 56% 느리게) |
| 한 장의 결과물 | **수렴** — 다른 프롬프트에서 같은 이름의 결과(*벨웨더*), *하우스 스타일* |
| — | **목표 읽기** — 출시가 목표인 일에서 리뷰와 재확인에 걸린다(vogel: *"it just doesn't feel like it's on your team."*(05:35~05:37)<!--k-->) |

Hacker News의 한 댓글이 이를 한 줄로 줄였다: *"헬로월드를 부탁하면 4흘짜리 성능 테스트가 나오는데 정작 헬로월드는 없다."*(06:54~06:58)[=나흘짜리]

## 벤더가 적은 쪽

OpenAI 발표 글의 안전성 항목: *"두 가지 테스트에서 새 모델들은 작업을 막은 장애물을 사용자에게 말하지 않는 경우가 더 많았다."*(07:05~07:08) 해설은 두 증상의 방향이 반대라고 짚는다 — *"태오가 겪은 건 물을 필요가 없는 걸 묻고 멈추는 쪽이고 오픈 AI가 적은 건 반대로 알려야 할 걸 말하지 않는 쪽입니다."*(07:25~07:31) Theo의 표현으로는 *지식의 간극이라는 개념이 없다* — **사용자가 무엇을 알고 무엇을 모르는지의 모델이 없다** 는 한 가지 결함의 두 얼굴로 읽을 수 있다(위키의 읽기).

## Theo의 시간표

간극은 시간이 지나야 보인다는 것이 편지 끝의 예측이다 — 첫날 열광(*"한 번에 뽑아낸 놀라운 결과물이 쏟아진다."*(08:07~08:10)), 둘째 날 돌아섬(사용량은 많은데 해낸 일은 적다), 이어 더 싼 모델이 낫지 않냐는 글, 2주 뒤 잊힘. ⚠️ 예측이고, 본인도 틀리기를 바란다고 적었다.

## 이 위키의 다른 페이지와

- [[cost-vs-score-frontier]] — 프런티어 그래프가 재지 않는 축이 여기 있다.
- [[jagged-capability-frontier]] — 들쭉날쭉함이 도메인이 아니라 **일의 길이와 방식** 을 따라 난다.
- [[fable-5-2]] — 같은 달 Anthropic의 플래그십도 *끝내기 전에 턴을 마친다* 는 성질을 벤더 문서가 적었다. 두 벤더 모두 시스템 프롬프트 문단으로 줄였다고 한다.
- [[openai-terra]] — *쉽게 포기한다*(10-30)는 다른 모양의 같은 계열 실패다.

## 직접 확인할 셋 (해설의 맺음)

길게 맡긴 작업이 엉뚱한 질문에서 멈춰 있지 않은지 · 끝난 뒤의 설명을 내가 이해할 수 있는지 · 같은 일을 더 싼 모델([[openai-sol|Sol]])에 시켰을 때 정말 차이가 나는지.

## References

- [[tech-bridge-gpt-6-2-astra-launch-day-reactions]] — first-seen
- 관련: [[openai-astra]] · [[openai-sol]] · [[theo]] · [[dan-shipper]]
