---
title: AI가 여는 형식 검증
type: concept
category: technique
tags: [formal-verification, lean, proof, security, navier-stokes, verifiable-code]
related: [executable-standards, verifiable-goals, defense-factory, agent-swarm, verification-bottleneck, ai-vulnerability-discovery, agent-verification-skill]
first-seen: tech-bridge-brockman-agi-era-defender-window
sources: [tech-bridge-brockman-agi-era-defender-window, tech-bridge-altman-benioff-dreamforce, tech-bridge-lauren-tan-2000-prs, tech-bridge-altman-devday-dots, tech-bridge-kent-beck-craft-augmented-development]
created: 2026-09-20
updated: 2026-10-09
---

# AI가 여는 형식 검증

**형식 검증(formal verification)이 실패한 이유가 사람에게 다루기 어려웠기 때문이라면, 정리 증명을 하는 모델이 그 제약을 푼다는 주장.** [[greg-brockman|Greg Brockman]]과 진행자가 [[tech-bridge-brockman-agi-era-defender-window]]에서 주고받는다.

> 예를 들어 **AI로 가능해지는, 모든 소프트웨어를 형식적으로 검증한다(formally verifying)는 아이디어**도 있죠. — 네, 그건 늘 우리가 가졌던 꿈이었습니다. **형식 언어들이 있었지만 결코 제대로 뜨지 못했죠.** — 맞습니다, 그건 **사람에게는 그냥 다루기 어렵기(intractable) 때문**입니다. **그런데 우리에겐 이 미친 수학 문제들을 푸는 AI들이 있습니다.** (14:47~15:03)

**진단이 명확하다** — 형식 검증은 **틀려서가 아니라 인간의 처리량 때문에** 실패했다.

## 근거 — 이미 한 번 했다

> **나비에-스토크스 문제에 대해 알아야 할 것 중 하나는 우리가 그것을 형식화했다는 겁니다 — Lean으로 형식화했습니다.** — **그럼 AI들이 검증 가능한 코드를 쓸 수 있겠군요.** — **쓸 수 있습니다.** (15:03~15:22)

**주장이 아니라 사례에 붙어 있다는 것이 이 개념의 값이다.** 1만 개의 에이전트가 푼 결과가 **Lean 형식화**로 남았다(→ [[agent-swarm]]).

> ⚠️ **그러나 "형식화했다"와 "AI가 검증 가능한 코드를 쓸 수 있다"는 다른 주장이고, 후자는 *"쓸 수 있습니다"* 한 마디가 전부다.** 사례·규모·실패율·검증된 코드의 종류가 **전혀 없다.** 수학 정리의 형식화에서 **일반 소프트웨어의 명세 작성**으로 가는 간극을 소스가 다루지 않는다.

## 이 위키에서의 좌표

| 페이지 | 검증을 누가 쓰고 누가 확인하나 |
|---|---|
| [[executable-standards]] | **사람**이 실행 가능한 형태로 규범을 적는다 |
| [[verifiable-goals]] | **사람**이 검증 가능한 목표를 정의한다 |
| **이 페이지** | **기계가 쓰고 기계가 확인한다** |

**이 위키가 검증을 다뤄 온 방식의 마지막 칸이다.** [[verification-bottleneck]]은 *사람의 검증 처리량이 병목* 이라고 했고, [[embedded-external-evaluators]](09-16)는 그 병목을 **의도한 제어 장치**로 삼자고 했다. **이 페이지는 그 병목 자체를 제거하려 한다** — 그리고 그것이 [[embedded-external-evaluators]]와 **정면으로 반대 방향**이다.

[[defense-factory]]의 마지막 단계(validate)가 자동일 수 있는 근거이기도 하다.

## ⚠️ 유보

- **"쓸 수 있습니다" 외에 아무 증거가 없다.**
- **명세를 누가 쓰는가**가 다뤄지지 않는다 — 형식 검증의 고전적 난점은 증명이 아니라 **무엇을 증명할지 적는 것**인데, 소스가 이 문제를 언급조차 하지 않는다.
- **비용**(형식화에 드는 컴퓨트)이 없다.

## References

- [[tech-bridge-brockman-agi-era-defender-window]] — first-seen
- [[greg-brockman]] · [[openai]]
- 관련: [[executable-standards]] · [[verifiable-goals]] · [[defense-factory]] · [[agent-swarm]] · [[verification-bottleneck]] · [[embedded-external-evaluators]] · [[ai-vulnerability-discovery]]

## CEO의 서술 — "7대 난제 중 하나" (2026-09-23 · [[tech-bridge-altman-benioff-dreamforce]])

[[sam-altman|Altman]]: *"올여름, 저희는 수학에서 가장 풀리지 않은 7대 난제 중 하나를 증명할 수 있는 모델을 개발했습니다"*(13:38~13:47), 그리고 서두에서 *"밀레니엄 프라이즈 문제까지 증명할 수 있는 모델"*(02:30). **나비에-스토크스(밀레니엄 문제 중 하나)에 대한 09-20 [[greg-brockman|Brockman]]의 서술과 같은 사건으로 보인다** — ⚠️ Altman은 **어느 문제인지 말하지 않고 Lean 형식화도 언급하지 않는다.** 이 위키는 같은 사건으로 **추정만** 한다.

**2026-10-09 보강 ([[tech-bridge-altman-devday-dots]]).** DevDay 대담에서 진행자가 **나비에-스토크스를 이름으로** 꺼내고(01:56~01:59), Altman(⚠️ 문맥 판독)이 *"10,000 agents worked super hard for 4 days"* 로 받는다(02:03~02:09) — 09-20 Brockman의 *1만 개 에이전트·나비에-스토크스* 와 09-23 Altman의 *"7대 난제 중 하나"* 가 **한 대화 안에서 이어졌다.** 같은 사건이라는 추정이 강해졌지만 ⚠️ **Altman이 직접 문제 이름을 말한 것은 아니고, Lean 형식화는 여전히 Brockman 편에만 있다.**

## 실무자의 위치 — "스펙트럼의 먼 끝, 여전히 열린 문제" (2026-09-26 · [[tech-bridge-lauren-tan-2000-prs]])

[[lauren-tan]]이 에이전트 검증을 **스펙트럼**으로 놓으며:

> **반대쪽 끝은 훨씬 훨씬 어렵고 여전히 열린 문제**인데, **형식 검증**입니다. **형식 기법이나 Lean, TLA+ 같은 언어**에 기대서 **비즈니스 로직 불변식이 항상 참인지 확인**하고 (…) 하지만 **형식 기법을 돌릴 능력이 없더라도 — 실제로 그런 사람은 아주 적습니다 — 검증 스킬만으로도 아주 멀리 갈 수 있습니다.** (07:44~08:37)

이 페이지의 CEO 서술(Brockman·Altman — *모델이 형식 검증의 제약을 푼다*)과 **온도가 다르다.** 앞의 둘이 **수학 난제의 증명**을 말했다면, 이쪽은 **애플리케이션의 비즈니스 불변식**을 말하고, 결론은 **"아직 없어도 된다"** 다. 싼 쪽 끝은 [[agent-verification-skill]]. ⚠️ 한 문단의 언급이고 사례·도구 경험은 없다.

## 써 본 사람의 두 한계 — 원샷성과 명세–구현 간극 (2026-10-09 · [[tech-bridge-kent-beck-craft-augmented-development]])

[[kent-beck|Kent Beck]](정확성 증명 과목 조교 출신)은 1년 전 Lean을 지니(AI)와 써 봤다(37:31~37:46). 이 페이지의 *"사람에게 다루기 어려워서 실패했다"* 진단과 달리, AI를 붙여도 남는 **구조적 한계 두 가지**를 든다.

1. **원샷성** — *"it's still feels like a oneshot process"*(37:54~38:00). 요소 하나를 바꾸면 되감아야 하고 *"even if it's faster because I have the genie helping, it's still a drag on my ability to change"*(38:16~38:27).
2. **명세–구현 간극** — *"there's still a gap between this mathematical model and implementation"*(38:40~38:45), *"I don't know how to how to bridge that"*(39:07~39:11), *"hasn't been fully bridged"*(40:15~40:19).

대신 *"low defect densities with a combination of examples, automated tests, carefully chosen, and foolproofing uh of the design"*(40:25~40:38) — 단 지니는 *"doesn't want to foolproof the design"*(40:51~40:55).

> ⚠️ **Contradiction(관점).** Brockman 쪽(처리량 문제 → AI가 푼다) vs Beck(구조 문제 → AI로도 남는다). Lauren Tan의 *"여전히 열린 문제"* 와 같은 편. 청중 질문(36:46)에 대한 즉답이며 사례·측정은 없다.
