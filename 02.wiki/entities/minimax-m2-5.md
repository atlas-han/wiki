---
title: MiniMax M2.5
type: entity
category: model
tags: [minimax, agent-model, terminal-bench, self-harness]
aliases: [M2.5]
sources: [self-harness-paper]
links:
  - https://www.minimax.io/news/minimax-m25
created: 2026-06-14
updated: 2026-06-14
---

# MiniMax M2.5

MiniMax가 *"real-world productivity"* 를 표방하며 공개한 에이전트형 LLM (2026-02 모델 리포트). 본 위키에는 **[[self-harness|Self-Harness]] 실험**([[self-harness-paper]])의 세 base 모델 중 하나로 등장.

## 위키에서 알려진 사실 (Self-Harness 맥락)

- [[terminal-bench|Terminal-Bench-2.0]]에서 [[self-harness|Self-Harness]] 적용 시: **Held-in Pass 43.0→50.0%, Held-out Pass 40.5→61.9%** (상대 +53%). 모델 가중치는 고정, [[deepagents|DeepAgents]] 기반 하니스만 변경.
- 접근: MiniMax 호스티드 API.
- **노출된 실행 병리 & 채택된 하니스 edit**:
  - 필수 산출물(answer artifact)을 **늦게 생성** → "create output early" 부트스트랩 지시로 교정.
  - 구조화 도구 출력(content tag)이 schema-invalid → 신중 처리 지시.
  - 길어지는 도구 루프 → runtime policy로 **total tool message 상한** 부여해 재유도.
  - 대표 사례: `count-dataset-tokens` task에서 메타데이터를 찾고도 탐색을 계속하다 timeout → edit 후 *식별→계산→`/app/answer.txt` 작성→재확인* 워크플로로 전환.

## 위치

- [[self-harness]] 실험의 3개 base 모델: [[minimax-m2-5]] · [[qwen3-5]] · [[glm-5]] (서로 다른 패밀리).

## 미해결 사항

- 아키텍처·파라미터·학습 세부 (별도 소스 필요)

## References

- [[self-harness-paper]]
