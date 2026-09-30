---
title: "에이전트 레시피 (Agent Recipes) — 시스템 증류가 해자다"
type: concept
category: pattern
tags: [agent-recipes, system-distillation, evals, skills, harness-profiles, versioning, moat, provider-agnostic]
aliases: [agent recipe, agent recipes, 에이전트 레시피, system distillation, 시스템 증류, pi.recipes, recipes]
related: [loop-is-the-product, taste-encoded-evals, valued-work-per-watt, skill-self-improvement, query-to-skill-distillation, self-harness, company-knowledge-moat, cross-harness-skill-compilation, agent-skills, skill-evals, reward-hacking, harness-engineering]
first-seen: tech-bridge-introspection-loop-is-the-product
sources: [tech-bridge-introspection-loop-is-the-product]
created: 2026-09-30
updated: 2026-09-30
---

# 에이전트 레시피 (Agent Recipes)

**에이전트 루프가 돌면서 알게 된 것 — eval·judge, 스킬·프롬프트, 하네스 확장·메모리, 모델별 하네스 프로필, 그리고 "왜 그렇게 정했는가" — 를 모델·제공자와 무관한 Git 저장소 하나로 버전 관리하고, 그것을 회사의 해자로 삼는다는 패턴.** 이름은 RL 연구의 *데이터 레시피*에서 왔다. [[roland-gavrilescu|Roland Gavrilescu]]([[introspection-dev|Introspection]])가 [[tech-bridge-introspection-loop-is-the-product]]에서 *"System distillation is the moat"*(04:11~04:14)라는 두 번째 아이디어로 제시했고, 조기 공개 제품이 **pi.recipes**다.

> *"an agent recipe is really something that enables you to create reproducible frontier AI systems. It's something that allows you to have a moat that keeps getting better over time, which is not tied to any platform or any provider."* (05:38~05:54)

> ⚠️ **당사자 진술.** 화자는 이 패턴을 제품으로 판다. 레시피 파일의 형식·예시·효과 측정은 발표에 없다. ko는 *moat* 를 **"모드"** 로(04:14 · 05:47), *agnostic* 을 **"회의적"** 으로(05:58) 옮겨 이 페이지의 두 핵심어를 지운다(`en`도 *"a mode"*).

## 왜 "레시피"인가 — RL의 데이터 레시피 (04:49~05:31)

> *"If you think about data recipes in research, this is how RL started to work really well. You understood the recipes and how to continuously change the recipe to combat some of the behaviors that may happen around hallucinations, around reward hacking, and then you get to your stack, which is your final data recipe. We don't have that for harnesses."* (04:49~05:11)

필요한 것은 *"something that contains the evals and contains the tweaks and the human judgment and all these things that are not predetermined at the beginning, but they're defined as you learn more about your agent acting in the … environment"*(05:17~05:31). → [[reward-hacking]] · [[rlhf]]

## 무엇이 레시피가 되나 — 증류 표 (06:03~06:17)

*"Loops should be the way you distill these systems into recipes."*(06:03~06:07)

| 루프에서 관찰된 것 | 레시피 안에서 되는 것 | 이 위키의 짝 |
|---|---|---|
| **실패 패턴** | **judge·eval** | [[skill-self-improvement]](실패 → 스킬) · [[taste-encoded-evals]] |
| **반복되는 행동** | **스킬·프롬프트** | [[query-to-skill-distillation]](반복 질의 → 스킬) · [[agent-skills]] |
| **사용자 불만** | **하네스 확장·메모리** | [[agent-memory]] · [[self-harness]] |

루프가 남기는 정보의 범위는 *"harnesses, profiles, evals, models, resources, tools, and the environment"*(04:30~04:38). 원하는 성질은 *"portable … version … evolve it over time"*(04:42~04:46).

⭐ 이 위키에서 **세 증류 경로(실패·반복·불만)가 한 저장소의 세 칸으로 묶인 첫 서술**이다. 기존 페이지들은 각각 하나씩(실패 → [[skill-self-improvement]], 성공 질의 → [[query-to-skill-distillation]], 성공 세션 → Oracle의 스킬 승격)이었다.

## 성질

- **모델·제공자 무관** — *"It's something that you control, lives in your company, and is agnostic to the models and providers you use"*(05:54~06:02). 그런데 동시에 **모델별 하네스 프로필**을 담는다 — *"How do I have different profiles of the harness to work with different models?"*(08:34~08:38). 즉 **무관성은 저장소 수준이고, 내부는 모델마다 갈린다.** → [[cross-harness-skill-compilation]](하네스·모델별로 컴파일)과 같은 문제 인식.
- **Git 저장소 · 에이전트가 관리** — *"We baked it into uh Git repos. So, uh everything could be versioned and agents would have a way to continuously track how this change and why, and is meant to be owned by you, but managed by your agents."*(07:04~07:17)
- **taste를 옮긴다** — *"if I want to use someone else's recipe, I should be able to also bring that taste. It's not just the harness, it's not just the model, it's how did you arrive at this particular recipe and why?"*(07:42~07:53). 레시피는 **결과물이 아니라 결정의 이력**이다. → [[taste-encoded-evals]]
- **스킬의 다음 단계** — pi.recipes는 *"very similar to skills uh used to be in 2025, but it's going a step forward"*(08:10~08:13). 스킬이 *무엇을 하는가* 라면 레시피는 **eval·신호·모델별 도구·하네스 프로필까지** 담는다(08:16~08:41).
- **승격** — 레시피 후보(diff)는 오프라인 eval → 프로덕션 A/B를 거쳐 *"you go to to the next version of an agent recipe"*(15:48~15:50)로 승격된다. → [[taste-encoded-evals]]

## 해자인가

*"the faster you do it uh the the the faster you you build a defensible um approach to to becoming a vertical AI company"*(17:06~17:15).

- [[company-knowledge-moat]]([[andrew-qu|Andrew Qu]], Vercel)는 해자를 **회사 고유 맥락 지식**에 둔다. 레시피는 그 지식이 **루프를 통해 증류된 형태**다 — *"lives in your company"*(05:56~05:59). 같은 자산의 다른 층이라 모순은 아니다. ⚠️ 위키의 정리.
- [[agent-fleet-learning]]은 **제공자 쪽**에 학습을 모아 네트워크 효과를 만든다. 레시피는 반대로 **제공자와 무관하게 사용자 회사에** 둔다 — 누가 해자를 갖느냐가 정반대다.

## ⚠️ 유보

- **레시피 파일의 실체** — 디렉터리 구조·스키마·예시가 없다. pi.recipes는 *"still early"*(08:44).
- **"reproducible frontier AI systems"** — 같은 레시피로 **다른 모델에서** 같은 품질이 나온다는 근거가 없다. 모델별 프로필을 담는다는 것 자체가 재현이 자동이 아님을 인정한다.
- **Pi 하네스·Harbor** — 구현 기반(06:57~07:00). 정체는 [[introspection-dev]] 참고, 추정.
- **증류가 오염되는 경우** — [[skill-self-improvement]]의 원칙(*한 번의 우연이 영구 규칙이 되면 오염*)에 대한 답은 사람 보정 + A/B다. 그 게이트의 표본·기준은 말하지 않는다.

## References

- [[tech-bridge-introspection-loop-is-the-product]] (first-seen) · [[introspection-dev]]
- 관련: [[loop-is-the-product]] · [[taste-encoded-evals]] · [[skill-self-improvement]] · [[query-to-skill-distillation]] · [[company-knowledge-moat]] · [[cross-harness-skill-compilation]]
