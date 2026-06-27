---
title: GLM-5
type: entity
category: model
tags: [glm, zhipu, agent-model, terminal-bench, self-harness]
aliases: [GLM-5]
sources: [self-harness-paper]
links:
  - https://arxiv.org/abs/2602.15763
created: 2026-06-14
updated: 2026-06-14
---

# GLM-5

GLM 팀의 *"from vibe coding to agentic engineering"* 를 표방한 모델 (GLM-5 Team, 2026, arXiv 2602.15763). 본 위키에는 **[[self-harness|Self-Harness]] 실험**([[self-harness-paper]])의 세 base 모델 중 하나로 등장 — 세 모델 중 초기 성능이 가장 높았다.

## 위키에서 알려진 사실 (Self-Harness 맥락)

- [[terminal-bench|Terminal-Bench-2.0]]에서 [[self-harness|Self-Harness]] 적용 시: **Held-in Pass 47.7→57.0% (상대 +20%), Held-out Pass 42.9→57.1% (+33%)**. 모델 고정, 하니스만 변경.
- 접근: OpenRouter 호스티드, concurrency 32.
- **노출된 실행 병리 & 채택된 하니스 edit**:
  - 설치한 도구/PATH 변경이 셸 명령 간 유실 → **환경 persist** (세션 간 설정 유지 + 변경 후 접근성 검증).
  - 탐색에 budget을 과소비하고 산출물을 늦게 냄 → **탐색→구현·테스트 전환** 유도 (탐색만 길면 구현 단계로 넘어가라는 verification-stage 제약).
  - 대표 사례: `build-pov-ray` task에서 긴 외부 다운로드에 budget을 쏟고 실패한 sanity check를 합리화 → edit 후 *bounded staged 작업·외부 아카이브 증거 선확인·실패 check 수리 후 finalize* 로 전환.

## 위치

- [[self-harness]] 실험의 3개 base 모델: [[minimax-m2-5]] · [[qwen3-5]] · [[glm-5]] (서로 다른 패밀리). 본 위키 첫 **GLM 패밀리** entity.

## 미해결 사항

- 아키텍처·파라미터·coding/agentic 벤치마크 전반 (별도 소스 필요)

## References

- [[self-harness-paper]]
