---
title: "자동화된 AI 연구 (Automated AI Research) — 스피드런을 벤치마크로"
type: concept
category: technique
tags: [automated-ai-research, recursive-self-improvement, speedrun, optimizer-speedrun, benchmark, research-agent, discovery-loop, prime-intellect]
aliases: [automated AI research, AI 연구 자동화, 자동화된 AI 연구, recursive self-improvement, 재귀적 자기 개선, optimizer speedrun, 옵티마이저 스피드런, research speedrun]
related: [generator-evaluator-pattern, verifiable-goals, self-harness, reward-hacking, context-resets-and-compaction, taste-vs-judgment, jagged-capability-frontier, claude-code, codex, nanogpt, prime-intellect]
first-seen: tech-bridge-agents-vs-humans-optimizer-speedrun
sources: [tech-bridge-agents-vs-humans-optimizer-speedrun]
created: 2026-09-28
updated: 2026-09-28
---

# 자동화된 AI 연구 (Automated AI Research)

**코딩 에이전트가 사람의 개입 없이 AI 연구 과제(여기서는 모델 훈련을 더 빠르게 만드는 방법 찾기)를 수행하게 하고, 그 능력을 규칙이 명확한 경쟁 과제로 측정하려는 시도.** [[prime-intellect|Prime Intellect]]의 [[elie-bakouch|Elie Bakouch]](설명란 기준)가 [[tech-bridge-agents-vs-humans-optimizer-speedrun]]에서 **optimizer speedrun**을 그 환경으로 제시했다. 목적은 빅랩이 말하는 **재귀적 자기 개선(recursive self-improvement)** — *"model training models without human intervention"*(00:47~00:51) — 을 **제3자가 정량화**하는 것이다.

> 빅랩들이 재귀적 자기 개선이 아주 곧 온다고 말하지만 (…) **이게 사실인지 정량화할 벤치마크가 없습니다.** 하물며 **빅랩이 아닌 제3자 벤치마크는 더 없습니다.** (00:38~01:10)

> ⚠️ 위키 용어로서의 첫 등장이다. 발표 한 편의 **진행 중인 작업** 보고이고, 세 트랙 벤치마크와 발견 루프는 화자 스스로 *"not released yet"*(11:22~11:25)·*"we didn't try it yet"*(16:53)이라 한다. 수치는 모두 **발표자 자신의 실험**이며 seed 반복·오차는 제시되지 않는다.

## 왜 스피드런인가

[[andrej-karpathy|Karpathy]]의 GPT-2 재현(목표 loss 도달, 약 90분) → Keller Jordan이 이끈 **modded-nanoGPT**가 **2년에 걸쳐 2분 미만**으로(01:40~02:48, → [[nanogpt]]). 화자는 이를 *"a very strong benchmark"*(02:51~02:54)라 부른다 — 재능 있는 사람들이 이미 기록을 쌓아 **인간 기준선**이 있다.

| 변형 | 바꿀 수 있는 것 | 성격 |
|---|---|---|
| **nanoGPT 스피드런** | 거의 전부(아키텍처·MoE·attention…). 제약은 **같은 검증·훈련 데이터**뿐(03:13~03:25) | 프로그램 최적화에 가깝다 |
| **optimizer speedrun** | **옵티마이저 관련 파라미터만**(Adam → Shampoo류, 03:25~03:54) | *"a bit more researchy"* — 계산 시간과 무관하게 **최선의 방법 찾기**(03:57~04:11) |

화자가 드는 네 이유(04:19~05:13):

1. **좋은 평가** — 발표의 주 초점.
2. **좋은 훈련 환경** — 기록을 깨면 양의 보상, 못 깨면 0 또는 음수. **RL 보상 신호로 바로 쓸 수 있다**(→ [[verifiable-goals]]).
3. **빠르다** — 이전 기록 약 2분, 한 번 실행 15~20분.
4. **규칙이 명확해 발견에 좋다** — *"there is those clear rule that you can verify or not"*(05:10~05:13).

**기록 검증에는 통계적 임계값**을 둔다 — *"to make sure that it's just not seed optimization and it's just not random"*(07:20~07:27). 에이전트가 **seed 운**을 기록으로 착각(또는 악용)하지 못하게 하는 장치다. 이 위키의 [[reward-hacking]] 사례(Hugging Face 사건: 막히자 온라인에서 답을 찾음)와 대조하면, 이 설계는 **판정 측**을 단단히 하고 **외부 기록 참조는 아예 허용**(전체 접근 트랙)하는 쪽이다.

## 첫 실험에서 드러난 것 — 에이전트의 연구 습관

Codex(GPT-5.5)와 Claude Code(Opus, 버전 미확정)를 goal.md + agents.md + Slurm 선점형 작업의 **단순한 하네스**로 커뮤니티와 경쟁시켰다(05:25~07:27). → [[codex]] · [[claude-code]]

| 관측 | Claude Code | Codex |
|---|---|---|
| **지속성** | 9~10시간마다 *"I cannot improve the record"* 로 멈춤, **시간의 1/3을 놀았다**(07:34~08:04) | *"almost never idle, never asked for question"*(08:13~08:15) |
| scratchpad | 적게, **이모지와 흥분** | 훨씬 많이, *"super robotic"* 결정 로그(08:34~09:15) |
| 서브에이전트·토큰 | 적음 | **훨씬 많음**(총 약 10억 토큰, 대부분 캐시 입력, 09:23~09:43) |
| compaction | 전체 실행에 약 1회 | 250k 윈도라 **잦음**(09:45~10:03) → [[context-resets-and-compaction]] |
| 결과 | 당시 최고 기록 **2,990 step을 50~60 step 앞섬** | *"20 step above"*(기준 모호) (11:02~11:15) |

⚠️ **"인간을 이겼다"의 해석 주의** — 모델은 **언제든 인간 기록을 가져올 수 있었고** Claude는 재시작 때 실제로 그렇게 했으며(10:43~10:56), V3는 *"최근 몇 주의 인간 기록을 가져와 개선하라"* 는 지시였다(06:04~06:13). 즉 **인간 기록 위에서의 +α** 다. 새로운 아이디어만 허용한 **novelty track은 더 어려웠다**(06:15~06:29).

## 핵심 관찰 — 조합은 했지만 발명은 없었다

> **새로운 옵티마이저나 메커니즘은 정말 하나도 없었습니다.** 서로 다른 논문을 조합하는 영리한 트릭, 여러 방법에 대한 **"+1" 개선**뿐이었습니다. (14:45~15:00)

> 간단하진 않지만 **사람 연구자라면 며칠·몇 주 들이면 접근 가능한** 문제에서조차 (…) 새 옵티마이저·메커니즘을 찾지 못한다. (15:03~15:21)

**기록 경신과 발견은 다른 축이다** — 이 페이지의 요지. 스피드런 점수는 올라가도 *새 아이디어* 는 나오지 않았다. [[jagged-capability-frontier]]의 *고르지 않은 역량*, [[taste-vs-judgment]]의 *무엇이 좋은 방향인지 아는 능력* 과 맞닿는다. 문헌 활용은 모델마다 달랐다 — **Claude가 다른 모델이 못 찾은 논문을 찾아 최고 결과로**(14:04~14:17). 즉 이 실험에서 에이전트의 강점은 **검색·조합·끈기**였다.

## 측정 설계 — 세 트랙 (작업 중)

*"a cool experiment (…) but it lack of structure"*(11:28~11:34). 진짜 벤치마크는 **여러 seed**, **모든 모델·하네스를 같은 조건**에(11:36~11:48).

| 트랙 | 접근 | 측정하려는 것 |
|---|---|---|
| ① | **없음** | *"only the model weights knowledge"* 로 연구하는 능력(11:53~12:05) |
| ② | **arXiv 논문만** | 문헌을 읽고 적용하는 능력 |
| ③ | **전체**(최신 인간 기록 포함) | 실전 조건 |

nanoGPT 트랙과, 옵티마이저가 **새로워야만** 하는 optimizer speedrun 둘 다(12:15~12:28). **접근 범위를 통제 변수로** 삼는 설계라서, 첫 실험의 *"인간 기록 위에서의 +α"* 문제를 트랙 ①②가 분리해 낸다.

6일(화자 *"almost 5 days"*) 예비 실험: Codex·Kimi·Claude 효과적, GLM 미완, **Kimi가 4일째 계단식 도약으로 Codex 추월**, Claude는 점진적(12:37~13:21). **x축을 출력 토큰으로 바꾸면 이야기가 달라진다** — max mode Claude가 훨씬 많이 쓰고 **Kimi가 토큰 대비 효율적**(13:25~13:51). ⚠️ **시간 축과 토큰 축 중 무엇으로 순위를 매길지**는 열어 둔다. 첫 실험에선 Codex가 토큰을 더 썼고 여기선 Claude가 더 쓴다 — **실험·설정이 달라** 모순으로 보지 않는다.

## 처방 — 평가에서 발견으로 (계획 단계)

Google의 **AlphaEvolve**와 후속 논문에서 영감받은 **멀티에이전트 발견 루프**(15:23~16:50):

1. **생성자 여럿** — 폐쇄 모델 + *"super effective for the cost"* 한 오픈소스 모델이 아이디어 제안
2. **스피드런 실행 → 보상**
3. **judge의 품질 피드백** — 방법의 좋고 나쁨에 대한 **taste**
4. **규모 확장 선별** — 스피드런 커뮤니티에서 *"많은 방법이 대규모에선 안 통한다"* 는 말이 잦으므로 **scale 요소를 루프 안에**
5. **사람이 아이디어를 판단·조향**

그리고 **목표·제약을 바꾼 여러 스피드런**으로 다양성을 만들고 모델을 특정 방향으로 제약한다(17:04~17:31). 구조는 [[generator-evaluator-pattern]]의 **연구 버전**이고, 이 위키에서 처음으로 **판정자가 실측 보상(스피드런) + LLM taste + 사람** 세 겹이다.

## 왜 공개적으로

> 재귀적 자기 개선의 일부가 **공개적으로 일어나는 것**이 아주 중요합니다 — **빅랩에 있지 않은 사람들이 실제로 많이 일하고 있으니까요.** (18:43~18:55)

이 위키에서 **랩 내부의 연구 자동화**는 [[minimax|MiniMax]]의 *"자체 research harness"*(실체 미공개)와 [[self-harness]]로 들어와 있었다. 이 소스는 **랩 바깥에서 측정하는 쪽**이다.

## 열려 있는 것

- **통계적 임계값의 구체**(몇 seed, 어떤 검정) — 말하지 않는다.
- **Claude의 "포기"가 모델 성향인지 하네스·설정 탓인지** — 단일 실험, 통제 없음.
- **세 트랙·발견 루프의 결과** — 발표 시점에 미공개·미시도.
- **스피드런 개선이 대규모로 이전되는가** — 화자 스스로 문제로 든다.
- 모델 버전(Opus 1.8/4.8, Kimi K2.7?), 발표 시점.

## References

- [[tech-bridge-agents-vs-humans-optimizer-speedrun]] (first-seen)
- [[prime-intellect]] · [[elie-bakouch]] · [[claude-code]] · [[codex]] · [[nanogpt]] · [[andrej-karpathy]]
- 관련: [[generator-evaluator-pattern]] · [[verifiable-goals]] · [[reward-hacking]] · [[self-harness]] · [[context-resets-and-compaction]]
