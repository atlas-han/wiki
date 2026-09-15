---
title: Design System as Agent Context
type: concept
category: pattern
tags: [design-system, context-engineering, constraints, slop, brand]
related: [structured-brand-context, ai-slop, atomic-design, llm-coding-guidelines, no-one-shot-design, adjective-verb-steering]
first-seen: tech-bridge-one-designer-plus-ai
sources: [tech-bridge-one-designer-plus-ai]
created: 2026-09-15
updated: 2026-09-15
---

# Design System as Agent Context

**디자인 시스템은 사람들 사이의 합의이기 전에, 모델의 출력 공간을 좁히는 장치다.**

[[tech-bridge-one-designer-plus-ai]]에서 [[vincent-wendy|Vincent Wendy]]가 기초를 먼저 세우는 이유를 **에이전트 쪽에서** 댄다.

> **Claude든 다른 어떤 LLM이든 아무 폰트 크기나 던지기를 좋아합니다. 우리가 정의해 두지 않으면 그냥 [[ai-slop|슬롭]]을 내놓습니다.** (06:17~06:28)

그래서 에이전트에게 주는 지시가 짧아진다 — *"우리는 이 데스크톱 타이포그래피, 이 모바일 타이포그래피를 쓴다"* 한 줄이면 된다.

## 무엇이 새로운가

[[structured-brand-context]]([[taste-labs|Taste Labs]]의 Brand API, 2026-09-12)는 **브랜드를 기계가 읽을 수 있는 형식으로 새로 만들자**는 제안이었다. 이 페이지는 다르다 — **이미 있던 디자인 시스템이 그 역할을 겸한다.** 새 산출물이 아니라 **원래 하던 일의 산출물이 그대로 컨텍스트가 된다.**

코드 쪽의 대응물은 [[llm-coding-guidelines]]다. **`CLAUDE.md`가 코드에 하는 일을 디자인 시스템이 디자인에 한다.**

## 슬롭 논의에서의 자리

이 위키의 [[ai-slop]] 축이 셋이 됐다.

| 소스 | 슬롭을 어떻게 다루나 |
|---|---|
| [[taste-labs]] | **측정한다** — 슬롭 = 결정의 부재, [[slop-probes|프로브]]로 잰다 |
| [[impeccable]] | **조향한다** — 원샷은 안 되고 [[adjective-verb-steering|형용사·동사]]로 고도를 낮춘다 |
| **이 페이지** | **예방한다** — 정의해 두지 않은 자리에서 슬롭이 나온다 |

셋은 경쟁하지 않는다. **정의 → 조향 → 측정** 순서로 붙는다.

> ⚠️ 어떤 항목까지 정의해야 충분한지, 정의가 과하면 무엇을 잃는지는 **소스에 없다.** 화자가 드는 항목은 타이포그래피·색상·컴포넌트·간격·폰트 크기뿐이다.

## References

- [[tech-bridge-one-designer-plus-ai]] · [[vincent-wendy]] · [[atomic-design]] · [[ai-slop]]
