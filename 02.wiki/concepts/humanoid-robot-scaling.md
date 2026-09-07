---
title: Humanoid Robot Scaling (휴머노이드 로봇 — 곱셈과 재귀)
type: concept
category: theory
tags: [robotics, physical-ai, humanoid, dexterity, recursive-manufacturing, tesla]
related: [brain-hands-decoupling, agent-harness-design, ai-jobs-impact, power-shortfall, intelligence-as-infrastructure]
first-seen: tech-bridge-elon-musk-g20-ai-future
sources: [tech-bridge-elon-musk-g20-ai-future]
created: 2026-09-07
updated: 2026-09-07
---

# Humanoid Robot Scaling (휴머노이드 로봇 — 곱셈과 재귀)

**범용 로봇의 유용성을 세 항의 곱으로 두고, 로봇이 로봇을 만드는 재귀 효과로 그 곱이 폭발한다고 보는 [[elon-musk|Elon Musk]]의 프레이밍.** → [[tech-bridge-elon-musk-g20-ai-future]]

> ⚠️ **휴머노이드 로봇을 만드는 회사([[tesla]])의 CEO가 각국 장관에게 하는 말**이며, 아래 수치에는 근거가 제시되지 않는다.

## 곱셈

> 범용 로봇의 **유용성** = **AI 소프트웨어** × **로봇에 탑재된 AI 칩** × **손의 전기기계적 정밀도**
> **지금 그 세 가지 모두 기하급수적으로 개선되고 있습니다.**

| 항 | 원 발언 | 이 위키의 대응 |
|---|---|---|
| **AI 소프트웨어** | *"AI 소프트웨어가 얼마나 좋은가"* | [[agent-harness-design]]의 brain |
| **AI 칩** | *"로봇에 탑재된 AI 칩의 성능"* | 온디바이스 추론 — 이 위키에 선례 없음 |
| **손의 정밀도** | *"특히 **손**의 전기기계적 정밀도"* | [[brain-hands-decoupling]]의 hands, 그러나 **물리적 의미** |

**곱셈이라는 것이 이 프레임의 내용이다** — 어느 한 항이 0에 가까우면 전체가 0이다. 세 항이 각각 기하급수적이면 곱은 세 지수의 합만큼 빠르다.

### [[brain-hands-decoupling]]과의 관계

그 페이지는 *"하네스는 샌드박스가 컨테이너인지 폰인지 포켓몬 에뮬레이터인지 모른다"* 며 brain과 hands의 **분리 가능성**을 말했다. [[jensen-huang]]은 그것을 *"에이전트를 물리적 몸체에 넣으면 로봇"* 으로 물리 세계까지 확장했다([[tech-bridge-jensen-huang-g20-agi]]).

Musk의 곱셈은 **모순이 아니라 그 다음 칸**이다: 인터페이스는 분리되지만 **성능은 분리되지 않는다.** 아무리 좋은 brain도 손이 무디면 유용성이 곱으로 깎인다. 이 위키의 하네스 논의가 지금까지 소프트웨어 층에만 있었기 때문에, *"hands의 품질이 상한을 만든다"* 는 관찰은 여기서 처음 나온다.

## 재귀

> 그러면 로봇을 만들면, **로봇들이 스스로 로봇을 생산하기 시작**할 겁니다. 그래서 **재귀적인 효과**가 나타납니다. **처음에는 아주 아주 느리게 시작하지만, 그 후에는 폭발적인 속도로 성장**합니다.

이것은 [[compute-constrained-growth]]·[[sutton-bitter-lesson]]이 다룬 소프트웨어 쪽 재귀(더 나은 모델이 더 나은 모델을 만든다)의 **제조업 판**이다. 차이는 **원자**다 — Musk 본인이 그 제약을 먼저 인정한다:

> **물리적인 것은 무엇이든 디지털적인 것보다 항상 시간이 더 오래 걸립니다.** (…) **엄청나게 큰 공급망 전체를 구축**해야 합니다. **아주 많은 원자들을 움직여야** 합니다.

## 수치

> **10년 후** (…) 인간형 로봇이 **10억 대**를 훨씬 넘을 거라고 예상합니다. (…) **로봇 한 대당 생산성은 아마도 인간의 다섯 배** (…) 즉, **10억 대의 휴머노이드 로봇이 모든 인류를 합친 것보다 더 생산적**일 것이라는 뜻입니다.

> 이는 **보수적인 추정치**라고 생각합니다. (…) 이건 제가 **큰돈을 걸고라도 믿고 걸 수 있는** 겁니다.

## ⚠️ 유보

- **세 항이 "기하급수적으로 개선 중"이라는 주장에 측정치가 없다.** 특히 손의 정밀도는 벤치마크도 제시되지 않는다.
- **10억 대 · 5배 · 10년의 근거가 없다.** 본인이 공급망 제약을 인정하고도 그 산수를 소스에서 보여주지 않는다. *"보수적"* 이라는 자기 평가도 마찬가지다.
- **생산성 "5배"의 정의가 없다** — 어떤 작업에서, 어떤 측정으로인지 없다. [[trusted-throughput]]이 경고한 대로 배수 주장은 분모가 없으면 읽을 수 없다.
- 재귀 효과의 **시작 조건**(로봇이 로봇을 만들 수 있게 되는 역량 수준)이 명시되지 않는다.
- 전력([[power-shortfall]])이 이 곱셈의 네 번째 제약일 수 있는데 소스는 두 화제를 연결하지 않는다.

## References

- [[tech-bridge-elon-musk-g20-ai-future]] — first-seen
- [[elon-musk]] · [[tesla]]
- 관련: [[brain-hands-decoupling]] · [[agent-harness-design]] · [[ai-jobs-impact]] · [[power-shortfall]]
