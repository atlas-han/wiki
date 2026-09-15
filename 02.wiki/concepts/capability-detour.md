---
title: Capability Detour
type: concept
category: pattern
tags: [model-limits, workaround, pipeline, design, benchmarks]
related: [no-one-shot-design, intentional-out-of-distribution, sutton-bitter-lesson, model-mixing-economics, agent-harness-design]
first-seen: tech-bridge-one-designer-plus-ai
sources: [tech-bridge-one-designer-plus-ai]
created: 2026-09-15
updated: 2026-09-15
---

# Capability Detour

**모델이 못 하는 일을 기다리지 않고, 그 능력이 필요 없는 경로로 돌아간다.**

[[tech-bridge-one-designer-plus-ai]]의 사례가 깔끔하다. [[simon-willison|Simon Willison]]의 **"자전거를 탄 펠리컨 SVG"** 테스트를 화자가 직접 다시 돌려 보고 결론을 낸다 — *"기본 모델들은 여전히 이 모양이고 디자이너인 저한테는 쓸 수가 없습니다."* 그리고 곧바로:

> **디자이너는 틀 밖에서 생각해야 합니다.** 그냥 **GPT에게 PNG 같은 정지 이미지로 만들어 달라고 하고, 그다음 [[figma|Figma]]에서 벡터화하면 지금 바로 출시할 수 있습니다.** 그러니 **LLM의 역량과 무관하게 틀 밖에서 생각해야 합니다.** (04:10~04:33)

## 구조

| | 직행 | 우회 |
|---|---|---|
| 요구 | 모델이 **벡터를 직접 생성** | 모델이 **래스터를 생성**, 벡터화는 **결정론적 도구** |
| 실패 지점 | 모델의 약한 능력에 전부 걸림 | 약한 능력이 **경로에서 빠진다** |
| 품질 판정 | 벤치마크가 정한다 | **출시 가능한가** 가 정한다 |

핵심은 **벤치마크 결과를 부정하지 않는다**는 것이다. 화자는 판정에 동의하고 **결론만 다르게 낸다.** 벤치마크는 *모델이 무엇을 못 하는지* 를 말하지 *일이 되는지* 를 말하지 않는다.

## 인접 입장과의 대비

- [[no-one-shot-design]]([[impeccable|Impeccable]], 2026-09-12): *"원샷은 안 된다 — 조향하라."* **같은 능력 위에서 반복**한다.
- **이 페이지**: *"안 되는 능력은 빼라."* **경로를 바꾼다.**
- [[sutton-bitter-lesson]]: *"기다리면 모델이 한다."* → **우회는 그 사이를 메우는 공학**이고, 모델이 따라잡으면 **폐기될 수 있는 종류의 작업**이다. 소스는 이 긴장을 다루지 않는다.

## References

- [[tech-bridge-one-designer-plus-ai]] · [[vincent-wendy]] · [[simon-willison]]
