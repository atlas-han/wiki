---
title: "모델 기질로 고르기 (Model Temperament Routing) — 꼼꼼한 모델과 틀을 의심하는 모델"
type: concept
category: pattern
tags: [model-selection, fable-5-2, claude-opus-5-5, code-review, verification, routing]
aliases: [모범생과 뒷자리, 앨런과 브래드, model temperament, model personality routing, 모델 성향]
related: [reasoning-effort-levels, automatic-model-routing, generator-evaluator-pattern, verifiable-goals, automated-code-review, true-cost-to-perfect-answer]
first-seen: tech-bridge-theo-fable-vs-opus-when-to-use
sources: [tech-bridge-theo-fable-vs-opus-when-to-use]
created: 2026-11-16
updated: 2026-11-16
---

# 모델 기질로 고르기 (Model Temperament Routing)

**모델을 *작업 난이도* 나 *가격* 이 아니라 *일하는 기질* — 시킨 틀 안에서 꼼꼼한가, 틀 자체를 의심하는가 — 로 배치하는 방식.** [[theo|Theo]]가 [[claude-opus-5-5|Opus 5.5]]와 [[fable-5-2|Fable 5.2]]를 비교하며 세운 틀이고, 위키에는 [[tech-bridge-theo-fable-vs-opus-when-to-use]](2026-11-15 한국어 해설)로 들어왔다. ⚠️ 해설 스스로 *한 사람의 해석* 이라 두 번 표시한다.

## 두 기질 (Theo의 비유, 해설 전달)

| | Opus 5.5 — 모범생 · 앨런 | Fable 5.2 — 뒷자리 · 브래드 |
|---|---|---|
| 강점 | 시킨 일은 끝까지, 두세 번 확인, 놓치는 게 드묾 | 틀을 의심하고 다른 안을 냄, *이 정도면 됐다* 고 말함 |
| 약점 | 시킨 일 자체는 의심하지 않음 — 기능 · 스펙이 부풂 | 꼼꼼함이 덜함 — Opus라면 안 했을 실수 |
| 리뷰어로 | 작은 PR에도 댓글 여덟 개, 완벽해야 할 변경에 | 고치기 어려운 위험만 보고 *LGTM*, 빨리 내보낼 때 |
| 시험지 비유 | *끝까지 읽고 시작하라 · 17번 백지로 낼 것* 통과 | 떨어짐 |

보완책: Opus에게 *"좋은 생각 같으면 하고 아니면 다른 방법을 제안해라"* 한 줄을 붙이면 결과가 눈에 띄게 좋아졌다(Theo).

## 배치 규칙

- **검증 가능한 일은 꼼꼼한 쪽.** 정답을 확인할 수 있는 일(TypeScript → Rust 재작성)은 Opus로 충분 → [[verifiable-goals]].
- **정답이 없는 일은 틀을 의심하는 쪽.** 그래픽 다듬기 · 인프라 구조 새로 짜기에서 Fable이 Opus가 못 내는 안을 낸다.
- **둘을 엮는다.** T3 Code 사례 — Opus가 꼼꼼히 깐 테스트 환경을 Fable이 검증해 *할 일 목록이 끝나지 않으면 기록 전체가 딸려 간다* 는 구조 문제를 짚었다. 반대로 같은 환경을 Fable이 만들면 빠진 경우가 더 많았다 → [[generator-evaluator-pattern]]의 *생성은 꼼꼼한 모델, 검토는 틀을 의심하는 모델* 배치.
- 시작은 Opus, Opus의 선택지가 뻔하거나 같은 자리를 맴돌 때 Fable로 — 공식 가이드의 *Opus가 아쉬워지는 순간에 Fable* 과 같은 결론을 다른 근거로.

## 위키의 읽기

- [[reasoning-effort-levels]] · [[automatic-model-routing]]은 *얼마나 생각하게 할까 · 어느 모델이 싸고 충분할까* 를 다룬다. 이 페이지는 같은 가격대 · 같은 점수대 모델 사이에서도 **실패의 모양이 다르다** 는 축이다.
- 리뷰 평가에서 *문제 있는 코드를 통과시킨다* 는 결과가 실제로는 *안 고쳐도 되는 지적을 거른 것* 이었다는 재해석 — 평가 기준 자체가 꼼꼼한 쪽으로 기울 수 있다 → [[automated-code-review]].
- ⚠️ Theo 자체 평가판 · 개인 사용 경험이고 *지금까지는 그랬다* 는 단서가 붙는다. 모델이 바뀌면 기질도 바뀔 수 있다.

## References

- [[tech-bridge-theo-fable-vs-opus-when-to-use]] · [[theo]]
