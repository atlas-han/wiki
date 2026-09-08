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
updated: 2026-09-08
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


## 만든 회사와 다음 세대 (2026-09-08)

2026-09-08 ingest로 **[[minimax|MiniMax]] 조직 페이지**와 **[[minimax-m3|M3]]** 가 이 위키에 생겼다. 이 페이지가 오래 *"아키텍처·파라미터·학습 세부 (별도 소스 필요)"* 로 비워둔 자리가 **M2.5에 대해서는 여전히 비어 있지만**, 같은 회사의 다음 모델에 대해서는 당사자 설명이 들어왔다.

| 모델 | 이 위키의 근거 |
|---|---|
| MiniMax-01 · M1 | [[tech-bridge-minimax-m3-long-context]] — **1천만 토큰** 컨텍스트, 비에이전트 |
| **M2.5 (이 페이지)** | [[self-harness-paper]] — 2026-02 모델 리포트, Terminal-Bench 실험 base |
| [[minimax-m3\|M3]] | [[tech-bridge-minimax-m3-long-context]] — 100만 토큰 + [[sparse-attention\|MSA]] + [[native-multimodal-pretraining\|native multimodality]] |

⚠️ **새 소스는 M2.5를 언급하지 않는다.** M1 → M3로 건너뛴다. 따라서 이 페이지와 [[minimax-m3]] 사이의 관계(계보상 어디에 놓이는지, 아키텍처가 이어지는지)는 **여전히 미확인**이다.

이 위키가 M2.5를 통해 본 것이 **바깥에서의 하니스 실험**이었다면, [[minimax]]는 이제 **자체 research harness로 자기 모델을 개선한다**고 말한다 — *"M3가 M3.1을 만들고 있습니다"*. → [[self-harness]]

## References

- [[self-harness-paper]]
- [[tech-bridge-minimax-m3-long-context]] · [[minimax]] · [[minimax-m3]] (2026-09-08)
