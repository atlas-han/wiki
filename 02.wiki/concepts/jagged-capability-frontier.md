---
title: 들쭉날쭉한 역량 경계 (Jagged Frontier)
type: concept
category: theory
tags: [capability, evaluation, astra, agi, unevenness]
related: [agi-definition, all-or-nothing-accuracy, skill-evals, ai-slop, openai-astra, capability-detour]
first-seen: tech-bridge-brockman-agi-era-defender-window
sources: [tech-bridge-brockman-agi-era-defender-window]
created: 2026-09-20
updated: 2026-09-20
---

# 들쭉날쭉한 역량 경계 (Jagged Frontier)

**모델의 역량이 도메인마다 고르지 않게 앞서고 뒤처지는 상태.** [[greg-brockman|Greg Brockman]]이 [[tech-bridge-brockman-agi-era-defender-window]]에서 [[openai-astra|Astra]]의 남은 한계를 설명하며 쓴다.

> 누군가 트위터에 올린 그래프를 봤는데 **들쭉날쭉한 프론티어(jagged frontier)** 같은 것이었고, **우리가 정말 있어야 할 곳은 전 범위에 걸쳐 훨씬 더 고른 상태**입니다. (39:00~39:16)

> ⚠️ 출처는 *"누군가 트위터에 올린 그래프"* 뿐이다. 이 위키는 원 출처를 확인하지 못했다.

## 왜 이 위키에 필요한가

이 개념이 **AGI 논쟁의 형태를 바꾼다**:

> **AGI는 시점(point in time)이라기보다는 일종의 흐릿한 스펙트럼(fuzzy spectrum)으로 드러났다고 생각합니다.** (38:26~38:45)

**"들쭉날쭉하다"는 것이 곧 "시점이 없다"는 것**이다 — 축마다 다른 시점에 넘어가므로 단일한 문턱이 성립하지 않는다. → [[agi-definition]]

그래서 이 페이지는 [[agi-definition]]에 **네 번째 입장의 메커니즘**을 제공한다. [[andrew-ng]]는 정의를 높게 잡아 *decades*, [[sam-altman]]은 용어가 무의미, [[jensen-huang]]은 도달 후에도 남는 일 — 여기서는 **경계의 모양 자체가 점이 아니다.**

## 구체적으로 어디가 뒤처지는가

> 예를 들어 **글쓰기가 그렇습니다. 꽤 괜찮은 글입니다. [슬롭(slop)]이 아닌 건 이번이 처음이에요.** — **하지만 훌륭한 글은 아닙니다.** (38:47~39:00)

> **몇몇 영역에서 조금만 다듬으면 환상적일 것 같은데 딱 거기까지는 아직 못 갔다고 느낍니다.** (39:00~39:16)

**[[openai-astra]] 페이지가 2026-09-06 이후 처음으로 구체적인 한계를 받는 자리**이고, **[[ai-slop]]이 모델 제작사 쪽에서 평가 어휘로 쓰인 첫 사례**다 — 이 위키에서 *슬롭* 은 09-12 [[taste-labs]]의 **측정 대상**이거나 09-14 [[jonathan-kelley|Kelley]]의 **불만**이었다.

> ⚠️ **ko 자막이 이 문장을 파괴한다** — *"경사가 없는 건 이번이 처음이에요"*. en-orig의 *"not sloping"* 자체가 *slop* 의 오인식이고 ko가 그것을 기울기로 읽었다. **한쪽만 읽으면 품질 평가가 사라진다.**

## 이 위키에서의 좌표

| 페이지 | 다루는 것 |
|---|---|
| [[all-or-nothing-accuracy]] | **한 과제 안**에서 100%가 아니면 실패 |
| **이 페이지** | **과제 사이**에서 고르지 않음 |
| [[skill-evals]] | 그 불균일을 어떻게 잴 것인가 |
| [[capability-detour]] | 뒤처진 축을 우회하는 실무 대응 |

**[[capability-detour]](09-14, 펠리컨 SVG가 안 되면 PNG→벡터화)가 이 개념의 현장 판본**이다 — 들쭉날쭉함을 인정하고 **뾰족한 부분을 골라 쓰는 것**.

그리고 화자의 처방은 그 반대다 — *"전 범위에 걸쳐 훨씬 더 고른 상태"*. **사용자는 우회하고 제작자는 평탄화하려 한다.**

## ⚠️ 유보

- **측정이 없다.** 어느 축이 얼마나 앞서고 뒤처지는지 수치가 없고, *"글쓰기"* 하나만 예로 든다.
- **원 그래프의 출처 불명.**
- *"이런 도약을 한 모델은 우리가 정말 본 적이 없다"*(39:16~39:33)는 **자기 보고**다.

## References

- [[tech-bridge-brockman-agi-era-defender-window]] — first-seen
- [[greg-brockman]] · [[openai-astra]]
- 관련: [[agi-definition]] · [[all-or-nothing-accuracy]] · [[skill-evals]] · [[ai-slop]] · [[capability-detour]]
