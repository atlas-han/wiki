---
title: "Anti-attractor — 금지 대신 무작위 시드로 발산을 강제한다"
type: concept
category: technique
tags: [divergence, sampling, ai-slop, agent-skills, subagents, creativity, homogenization]
aliases: [anti-attractor, 안티 어트랙터, force divergence, 발산 강제, random seed, 창의적 시드]
related: [ai-slop, agent-skills, generator-evaluator-pattern, adjective-verb-steering, intentional-out-of-distribution, slop-probes, scripts-that-talk-back]
first-seen: tech-bridge-skill-engineering-dark-arts
sources: [tech-bridge-skill-engineering-dark-arts]
created: 2026-09-28
updated: 2026-09-28
---

# Anti-attractor

**모델에게 "X를 쓰지 마라"고 하면 X의 옆자리 — 같은 클러스터의 다음 후보 — 로 옮겨 갈 뿐이다. 모델을 중앙값에서 떼어 내려면 금지가 아니라 모델이 예측할 수 없는 입력(무작위 시드)을 넣어야 한다.** [[paul-bakaus]]가 [[impeccable|Impeccable]]과 다른 스킬들에 쓴 기법의 이름이다(*"what I call an anti-attractor"* 17:07). 출처는 [[tech-bridge-skill-engineering-dark-arts]] 한 편이고, 화자의 조어다.

## 문제 — 금지는 옮길 뿐이다

> *"The first one it overapplies and then a ban just relocates the model to the next cluster."* (05:03~05:08)
>
> *"you tell it not to use In[ter] it just uses the next best font it finds in [its] latent space. And so it doesn't actually make it more creative."* (05:13~05:18)
>
> *"The median is the model's gravity. Even 250 lines of like artis[an]al, crafted, beautiful skill pros[e] cannot change this."* (05:58~06:09)

예는 Anthropic front-end design 스킬의 금지 목록이다 — *"never use generic AI aesthetics, overused fonts like Inter, Roboto, Arial, system fonts (…) never converge on common choices like Space Grotesk"*(04:42~04:58, en-orig 표기 교정). 그래서 [[ai-slop|슬롭]]이 **움직이는 표적**이 된다(보라색 그라데이션 → "Claude 베이지").

## 세 기법 (쉬움 → 어려움)

> *"a ban only moves the model around inside its own cluster"* (16:58~17:04) — 대신 *"a random seed of sorts (…) from user input or (…) from a script (…) that is completely unexpected to the model"* (17:14~17:23)

| 기법 | 방법 | 한계·조건 |
|---|---|---|
| **① 안전한 선택 깎기** | *"name your top three fonts"* → *"now throw them away"*(17:54~18:02). 다음 토큰 예측을 세 번 깎아 잠재 공간의 **더 먼 곳**으로 간다 | *"at some point you still get convergence"*(18:22~18:25) — 제한적 |
| **② 대량 생성 + 서브에이전트 순위** | radiant shaders 라이브러리에서 셰이더 ~100개를 만들 때 매번 같은 아이디어가 반복 → **셀럽 시드**(*"what would Rihanna look like as a shader"* 18:59~19:03)로 100개 생성 → **서브에이전트가 순위** | 순위자는 **반드시 서브에이전트** — *"the sub agent doesn't know anything uh from the prior context of the session"*(19:20~19:26) |
| **③ 스크립트 시드** | 프로젝트 시작 시 `color.js`가 **100개 넘는 손으로 고른 원색** 중 하나를 준다 — 완성 팔레트가 아니라 출발점(19:36~19:51). 모델은 그것을 *"creative spark"* 로 팔레트를 짓는다 | 사용자가 거절할 수 있다(20:01~20:07). 결정론적 난수를 모델 밖에서 만든다 → [[scripts-that-talk-back]] |

결과: *"the same brief depending on the users input and (…) color script that runs etc can produce vastly different results"*(20:14~20:23) — *"I didn't want to have the whole internet look like uh everything else"*(20:24~20:26).

## 이 위키에서의 자리

- **[[ai-slop]]의 처방 층.** 09-15에 정리된 처방(어휘 정의·디자인 시스템·[[slop-probes|탐침]])이 **무엇을 원하는지 말하는** 쪽이었다면, anti-attractor는 **어디서 출발할지를 흔드는** 쪽이다. [[adjective-verb-steering]]이 방향을, 시드가 출발점을 준다.
- **[[intentional-out-of-distribution]]** 과 같은 방향이지만 수단이 다르다 — 사람의 의도가 아니라 **모델 밖의 무작위성**으로 분포 밖을 만든다.
- **② 기법의 순위자**가 맥락 없는 서브에이전트여야 하는 이유는 [[generator-evaluator-pattern]]의 분리 원칙과 같다(생성 세션의 맥락이 판단을 끌고 간다). ⚠️ 위키의 연결.

## ⚠️ 표시해 둔 것

- **효과 측정 없음.** "vastly different results"는 화자 진술. 다양성이 **품질**을 유지하는지(무작위 원색이 브랜드에 맞는지)는 사용자 거절(20:01~20:07)에 맡긴다.
- ① 기법의 *"shave the save[=safe] picks"*(17:51~17:54)는 en-orig ASR — 이름 표기 미확정.
- radiant shaders(18:35)는 ASR. [[tech-bridge-impeccable-design-steering]]의 *"radian shaders"* 와 같은 라이브러리로 보이나 확정하지 않는다.
- 슬롭의 **판정**은 [[taste-vs-judgment]]에 남는다 — 화자 자신이 *"I don't think taste can be solved at a model level"*(56:28~56:32).

## References

- [[tech-bridge-skill-engineering-dark-arts]] (기법 2, 16:47~20:26)
- [[paul-bakaus]] · [[impeccable]] · [[ai-slop]] · [[scripts-that-talk-back]]
