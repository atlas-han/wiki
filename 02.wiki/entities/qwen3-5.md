---
title: Qwen3.5-35B-A3B
type: entity
category: model
tags: [qwen, alibaba, moe, agent-model, terminal-bench, self-harness]
aliases: [Qwen3.5, Qwen3.5-35B-A3B]
sources: [self-harness-paper, tech-bridge-voice-agent-failure-modes]
links:
  - https://qwen.ai/blog?id=qwen3.5
created: 2026-06-14
updated: 2026-09-19
---

# Qwen3.5-35B-A3B

Qwen 팀(Alibaba)의 *"native multimodal agents"* 지향 모델 (2026-02 리포트). 이름의 `35B-A3B`는 총 35B 파라미터 중 활성 ~3B의 **MoE** 구성을 시사. 본 위키에는 **[[self-harness|Self-Harness]] 실험**([[self-harness-paper]])의 세 base 모델 중 하나로 등장 — 세 모델 중 초기 성능이 가장 낮아 가장 큰 상대 개선을 보였다.

## 위키에서 알려진 사실 (Self-Harness 맥락)

- [[terminal-bench|Terminal-Bench-2.0]]에서 [[self-harness|Self-Harness]] 적용 시: **Held-in Pass 15.1→36.0% (상대 +138%, 실험 중 최대), Held-out Pass 23.8→38.1% (+60%)**. 모델 고정, 하니스만 변경.
- 접근: 로컬 배포 — 4×NVIDIA H200, SGLang(`lmsysorg/sglang:v0.5.12-cu129` 기반 내부 이미지), concurrency 48.
- **노출된 실행 병리 & 채택된 하니스 edit**:
  - 의존성 미확인 → **dependency precheck**.
  - 동일 명령 반복 실패 → **재시도 규율**(exact command retry 완화).
  - 끝없는 탐색 cycle → loop breaking.
  - 도구 오류 후 필수 산출물 유실 → **tool-error-triggered 미들웨어**로 artifact 복구.
  - 대표 사례: `extract-elf` task에서 추출 스크립트를 만들고도 overwrite/edit 실패를 반복하다 `/app/extract.js`를 삭제해 verifier 실패 → edit 후 오류 트리거 프롬프트가 *산출물 재생성→JSON 검증→파일 보존* 으로 유도.

## 위치

- [[self-harness]] 실험의 3개 base 모델: [[minimax-m2-5]] · [[qwen3-5]] · [[glm-5]] (서로 다른 패밀리). 본 위키 첫 **Qwen 패밀리** entity.

## 미해결 사항

- 정확한 MoE 구성·컨텍스트 길이·멀티모달 범위 (별도 소스 필요)

## 보이스 에이전트에서의 자리 (2026-09-19 · [[tech-bridge-voice-agent-failure-modes]])

[[plivo|Plivo]]가 [[gemma-4|Gemma 4]]와 함께 **보이스 에이전트 LLM 층의 두 후보** 중 하나로 쓴다. *"현재 시장에 나와 있는 최첨단 오픈 소스 모델"*(09:33~09:47).

- **영어 전용이면 Gemma 4와 대등**하다. 갈리는 것은 **다국어**이고, 거기서는 [[token-fertility]] 기준으로 Gemma가 2.5~3배 낫다고 주장한다.
- 크기 권고가 이 모델의 MoE 구성과 맞물린다 — **MoE 3~4B는 기본 성능이 좋지만 파인튜닝이 어렵다**(*"모델이 망가지는 경우가 꽤 많다"*). 튜닝할 계획이면 **8B~12B 조밀 모델에서 시작**하라는 것이 소스의 권고다.
- 이 위키가 이 모델을 본 **두 번째 맥락**이다 — [[self-harness-paper]]에서는 *하니스만 바꿔도 크게 오르는 base 모델* 이었고, 여기서는 **자체 호스팅으로 300ms를 맞추는 실무 선택지**다.

⚠️ 벤치마크의 실체(데이터셋·과제·표본)가 없다. ⚠️ 양 트랙 자막에서 이름이 *"Quen"* 으로 깨져 있어 설명란 표기로 확정했다.

## References

- [[self-harness-paper]]
