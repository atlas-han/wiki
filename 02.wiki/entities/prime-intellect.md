---
title: Prime Intellect
type: entity
category: org
tags: [open-source, rl-environments, automated-ai-research, gpu-sandbox, training-infrastructure]
aliases: [프라임 인텔렉트, PrimeIntellect]
links:
  - https://www.primeintellect.ai
sources: [tech-bridge-agents-vs-humans-optimizer-speedrun]
created: 2026-09-28
updated: 2026-09-28
---

# Prime Intellect

**빅랩 바깥에서 AI 연구·훈련 인프라를 만드는 회사.** 이 위키에는 [[tech-bridge-agents-vs-humans-optimizer-speedrun]](연구 엔지니어 [[elie-bakouch|Elie Bakouch]]의 발표)으로 처음 들어왔다. 발표가 드러내는 자기 규정은 **"재귀적 자기 개선의 일부는 공개적으로 일어나야 한다"**(18:43~18:55)는 입장이다.

> ⚠️ **회사명은 설명란(`Prime Intellect`, `https://www.primeintellect.ai`)에만 온전하다.** 자막에서는 en-orig *"Primal director"*(00:16)·*"Timing the Lake"*(17:35), en·ko *"Primal Direct"*·*"Timing Direct"* 로 깨진다. 설립·규모·자금은 이 소스에 없다.

## 위키에서 알려진 사실 (발표 기준)

- **자동화된 AI 연구 벤치마크** — optimizer speedrun에서 Codex·Claude Code를 커뮤니티와 경쟁시켰고, 접근 범위를 달리한 **세 트랙 벤치마크**를 준비 중(발표 시점 미공개). → [[automated-ai-research]]
- **자체 Slurm 클러스터** — 에이전트가 **선점형(preemptible)** 권한으로 작업을 제출하게 했다(06:52~07:12).
- **개발 중(대부분 미공개, 17:39~17:44)**:
  - **GPU 샌드박싱** — 모델이 샌드박스에서 반복하게(17:44~17:52)
  - **자체 에이전트** — 파일 시스템에 정보를 쓰고 읽고, programmatic tool calling을 하는 프레임워크에 효율적인 것(프레임워크 이름은 트랙마다 *LM*/*RLM*, 미확정, 17:52~18:08)
  - **오픈소스 모델 위에서** 그 일을 잘하도록 모델 훈련(18:08~18:12)
- **이미 공개한 것** — *"어떤 하네스에서든 어떤 환경이든 훈련·평가"* 하는 라이브러리·제품 세트, 아주 큰 모델까지 훈련 가능(18:13~18:37). ⚠️ **이름이 깨져 있다**(en-orig *"Verifier Primary or State Training"*) — 이 위키는 *verifiers*·*prime-rl* 류로 **추정만** 하고 확정하지 않는다. 고객(*"our clients"*, 18:37)이 있다는 언급.
- **발견 루프 계획** — AlphaEvolve 영감의 멀티에이전트 루프, *"we are kind of trying it right now"*(16:56). 생성자에 **비용 효율적인 오픈소스 모델**을 명시적으로 넣는다.

## 위키 안의 자리

- **랩 바깥의 연구 자동화 측정자** — 랩 안쪽 사례인 [[minimax|MiniMax]]의 *자체 research harness*, [[self-harness]]와 대비.
- **오픈소스 편** — 발표가 Kimi·GLM을 Claude·Codex와 같은 판에 올리고 Kimi의 토큰 효율을 짚는다.

## References

- [[tech-bridge-agents-vs-humans-optimizer-speedrun]]
- [[elie-bakouch]] · [[automated-ai-research]]
