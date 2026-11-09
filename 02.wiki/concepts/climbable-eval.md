---
title: "오를 수 있는 평가 (Climbable Eval) — 네 조건, 막힌 문제, 학습/시험 분할로 과적합 없이 hill climbing"
type: concept
category: technique
tags: [evals, hill-climbing, overfitting, train-test-split, eval-design, self-improvement, anthropic, claude-code, cost-optimization]
aliases: [climbable eval, 오를 수 있는 평가, hill climbing, 힐 클라이밍, hillclimb, build-eval, 학습용 시험용 분할, eval overfitting]
related: [eval-experiment-anatomy, skill-evals, pareto-surfing, production-trace-eval-flywheel, self-harness, verifiable-goals, prompt-debt, model-mixing-economics, cost-vs-score-frontier]
first-seen: tech-bridge-lance-martin-old-prompts-make-claude-worse
sources: [tech-bridge-lance-martin-old-prompts-make-claude-worse]
created: 2026-11-09
updated: 2026-11-09
---

# 오를 수 있는 평가 (Climbable Eval)

**모델이 스스로 고쳐 가며 점수를 올릴 수 있도록(hill climbing) 설계된 평가, 그리고 그 오르기가 과적합이 되지 않게 하는 분할 규칙.** [[tech-bridge-lance-martin-old-prompts-make-claude-worse]]에서 해설자가 [[lance-martin|Lance Martin]]의 발표와 claude.dev 글 *Automating eval design and hillclimbing with Claude*(위키 미열람)를 전한다:

> *"클로드는 스스로 고치는 걸 잘 해서 잘 만든 평가만 주면 점수를 알아서 올라갑니다. 이걸 힐 클라이밍이라고 부르죠."*(03:16~03:22)

> ⚠️ **소스 하나, 벤더 2차 전달.** 이름 *climbable eval*은 해설의 *"오를 수 있는 평가"*(챕터 제목)를 위키가 옮긴 것이다. 명령(`build-eval` · `hillclimb`)은 설명란 표기다.

## 좋은 평가의 네 조건

> *"더 좋은 모델이 더 높은 점수를 받고, 더 많이 생각하면 점수가 오르고, 최고 모델도 만점과 거리가 있고, 돌릴 때마다 점수가 크게 흔들리지 않을 것."*(03:25~03:32)

1. **모델 순서를 지킨다** — 더 좋은 모델이 더 높다.
2. **생각에 반응한다** — 더 많이 생각하면 오른다.
3. **천장이 남아 있다** — 최고 모델도 만점이 아니다.
4. **안정적이다** — 실행마다 크게 흔들리지 않는다.

**함정 — 막힌 문제**: 어떤 모델도 못 푸는 문제가 20% 섞이면 여지가 있어 보여도 실제로는 막혀 있다. 블로그 권고는 *몇 번을 돌려도 매번 실패하는 문제를 의심하라*. → 조건 3(천장)과 구분해야 한다: 천장은 *오를 수 있는* 여지, 막힌 문제는 *오를 수 없는* 여지다.

**만들기 — `build-eval`**: 트레이스 같은 원본 데이터를 주면 문제와 채점 기준을 같이 만들고 중간중간 사람의 확인을 받는다 → [[production-trace-eval-flywheel]](운영 데이터 → 평가).

## 오르기 — `hillclimb`와 학습/시험 분할

- 가장 큰 적은 과적합. 예: 평가에 OCR이 필요하다고 하네스에 OCR 도구를 붙이면 점수는 오르지만 실제 서비스엔 쓸모없다.
- 분할: 평가를 학습용과 시험용으로 나누고, Claude는 **학습용 실패만** 보고 고칠 곳을 찾는다. 시험용은 보지 않는다.
- ⭐ 되돌림 규칙: 학습 점수만 오르고 시험 점수가 그대로면 과적합으로 보고 그 수정을 되돌린다.

## 해설이 전한 결과 (⚠️ 벤더 자기 실험)

- **품질 목표** — Claude API 스킬 자체: 66% → 24라운드 → 87.9%. 빠진 기능 8개 채움, Claude가 옛 API 모양으로 코드를 쓰는 문제 발견, **잘못된 채점기 수정**(평가 자체도 고쳐진다).
- **비용 목표** — *성능은 지키면서 비용만 줄여라*: Opus 4.8 높은 노력 74.4% · 4.6센트 → (audit + Opus 5.0(ASR) 낮은 노력) 87.8% · 1.9센트 → Sonnet 5 낮은 노력 1센트, 규칙 보완 후 98.9%(학습용으로 읽힘). **시험용 티켓 14개: 78.6% → 90.5%, 비용 약 5분의 1.**
- ⚠️ 시험 세트가 14건이라 1건이 약 7%p다. 해설은 신뢰 구간이나 반복 실행 수를 말하지 않는다 — 조건 4(안정성)를 이 결과 자체에 적용한 근거는 없다.

## 위키 안의 연결

- [[pareto-surfing]] — 다른 hill climber(Southbridge의 자기 최적화 파이프라인). 그쪽은 **비용-품질 프런티어**를, 이쪽은 **학습/시험 분할**을 안전장치로 둔다.
- [[eval-experiment-anatomy]] — 데이터셋 · 태스크 · 채점. 이 페이지는 *좋은 데이터셋의 조건*과 *분할*을 더한다.
- [[skill-evals]] — 스킬을 eval로 고친 사례가 여기 하나 더(Claude API 스킬).
- [[prompt-debt]] — audit로 지운 뒤 나빠지지 않았음을 보이는 장치가 이 평가다.
- [[cost-vs-score-frontier]] · [[model-mixing-economics]] — 비용을 목표 함수로 둔 hill climbing이 *더 싼 모델 · 낮은 노력*으로 내려간 결과.

## 미해결

- 시험 세트가 반복된 hill climbing에 간접적으로 새는 문제(되돌림 판단에 시험 점수를 쓰면 시험용도 선택에 쓰인다) — 해설은 다루지 않는다.
- 네 조건을 실제로 어떻게 재는지(몇 모델 · 몇 번 실행).

## References

- [[tech-bridge-lance-martin-old-prompts-make-claude-worse]] (4절 · 5절 · 6절) — first-seen
- [[lance-martin]] · [[anthropic]]
- 관련: [[eval-experiment-anatomy]] · [[skill-evals]] · [[pareto-surfing]] · [[production-trace-eval-flywheel]] · [[prompt-debt]]
