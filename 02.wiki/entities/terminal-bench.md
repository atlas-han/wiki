---
title: Terminal-Bench-2.0
type: entity
category: tool
tags: [benchmark, agent-eval, terminal, containerized, verifier]
aliases: [Terminal-Bench, Terminal-Bench-2.0, TB2]
sources: [self-harness-paper]
links:
  - https://arxiv.org/abs/2601.11868
created: 2026-06-14
updated: 2026-06-14
---

# Terminal-Bench-2.0

실제 명령줄(CLI) 환경에서 에이전트를 평가하는 **멀티턴 agentic 벤치마크** (Merrill et al., 2026, arXiv 2601.11868). 에이전트가 컨테이너화된 터미널 환경과 상호작용하며, **결정론적 verifier**가 최종 컨테이너 상태로 pass/fail을 판정. 본 위키에는 **[[self-harness|Self-Harness]] 논문**([[self-harness-paper]])의 평가대로 등장.

## 위키에서 알려진 사실

- **89개 컨테이너 터미널 task** — artifact 관리, 명령 사용, 검증 행동, 실행 오류 복구 등 general tool-based execution을 테스트.
- 판정은 task별 **deterministic verifier**가 최종 상태로 수행 → [[self-harness|Self-Harness]]의 *verifier-grounded failure signature* 클러스터링이 가능한 토대.
- 실행 환경으로 **Harbor** 사용. (Self-Harness 실험은 64-case 부분집합 — 불안정 외부 웹 의존·멀티모달 입력 task를 제외해 하니스 외 노이즈 축소.)

## Self-Harness에서의 역할

- 모델·평가자·예산을 고정한 채 하니스만 바꾸는 **within-model 비교**의 측정 기반.
- held-in(trace·실패증거 노출) / held-out(promotion gate 전용) 분할의 task 풀.
- pass 신호가 결정론적이라 [[generator-evaluator-pattern|generator/evaluator]]식 주관 평가와 달리 **non-regressive 채택 규칙**을 직접 적용 가능.

## 미해결 사항

- TB1 대비 2.0 변경점, 전체 task 분류, leaderboard (별도 소스 필요)

## References

- [[self-harness-paper]]
- [Terminal-Bench (arXiv 2601.11868)](https://arxiv.org/abs/2601.11868)
