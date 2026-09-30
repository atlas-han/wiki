---
title: "제작자의 taste를 eval로 (Taste-Encoded Evals) — 에이전트가 만들고, 사람은 보정하고, 사용자가 A/B로 승인한다"
type: concept
category: technique
tags: [evals, llm-as-judge, taste, human-in-the-loop, calibration, ab-testing, multi-armed-bandit, traces, agent-recipes]
aliases: [taste into evals, codify taste into evals, 안목을 평가 지표로, eval calibration, judge calibration, 판정관 보정, HITL calibration]
related: [taste-vs-judgment, agent-recipes, loop-is-the-product, valued-work-per-watt, generator-evaluator-pattern, skill-evals, skill-self-improvement, self-harness, verifiable-goals, production-trace-eval-flywheel]
first-seen: tech-bridge-introspection-loop-is-the-product
sources: [tech-bridge-introspection-loop-is-the-product]
created: 2026-09-30
updated: 2026-09-30
---

# 제작자의 taste를 eval로 (Taste-Encoded Evals)

**eval은 단순한 테스트가 아니라 "제작자의 taste"를 코드로 옮긴 것이고, 그 코드화는 에이전트가 한다 — 트레이스에서 행동 패턴을 찾고, 그 패턴을 판정하는 judge를 만들고, 사람은 "이 판단에 동의하는가"에만 답해 judge를 보정하며, 최종 검증은 프로덕션 A/B에서 사용자가 그 taste에 동의하는지로 한다.** [[roland-gavrilescu|Roland Gavrilescu]]([[introspection-dev|Introspection]])가 [[tech-bridge-introspection-loop-is-the-product]]에서 인재 발굴 에이전트 예시(가상)로 펼쳤다.

> *"It's not just tests. It's It's really what is the taste of the creator that agents should be able to reproduce and self-improve around."* (11:01~11:08)

> *"You don't need the human to actually build the evals. You need them to calibrate the evals. And agents should be the ones that really take the the the taste of the maker and and put them in into code."* (14:45~14:55)

> ⚠️ **가상 예시, 측정 없음.** *"Let's take a baseline um agent, which could be a talent sourcing agent"*(12:23~12:26). 보정에 필요한 사람의 질문 수, judge의 일치율, A/B의 표본·지표가 전혀 없다. 화자는 이 절차를 담는 제품(pi.recipes)을 판다.
>
> ⚠️ **ko가 이 페이지의 두 핵심 문장을 뒤집는다.** 14:47 *"평가는 사람이 하는 것이다"*(원문: 사람은 eval을 **만들 필요가 없다**), 11:01 *"단순히 맛의 문제만은 아닙니다"*(원문: 단순한 **테스트**가 아니라 taste다 — `en`도 *"not just about taste"*). 그리고 taste를 **"기준"·"판단력"** 으로 옮긴다(11:51 · 15:26 · 15:44 · 15:58 · 16:08).

## 절차 (12:18~15:55)

| # | 단계 | 누가 | en-orig |
|---|---|---|---|
| 0 | **베이스라인** — 웹 검색·LinkedIn 도구, 서브에이전트, 채용 담당자 시스템 지시 | 제작자 | 12:45~13:00 |
| 1 | **패턴** — 트레이스에서 공통 행동·사용자 불만을 뽑아 **클러스터**로 | 에이전트 | *"a way to look at the traces, extract some common um behaviors or common user frustrations, and turn them into like a cluster"*(13:05~13:16) |
| 2 | **judge** — 궤적을 보고 그 패턴을 판정하는 에이전트 | 에이전트 | *"did did this agent reach out to Google employees instead of trying to uh find hidden gems on GitHub?"*(14:12~14:19) |
| 3 | ⭐ **보정** — 사람은 judge의 판단에 동의하는지만 답한다 | **사람** | *"You just need a human in the loop to say, 'Hey, um this is the approach we're taking. Do you agree with this judgment?'"*(14:26~14:35) |
| 4 | **레시피 후보** — *"the diffs that you really want to taste"* + 오프라인 eval 세트 | 에이전트 | 14:57~15:08 |
| 5 | **프로덕션 A/B** — 사용자가 그 taste에 동의하는가. *"with a multi-arm bandit um scenario, for example"* | 사용자 | 15:08~15:41 |
| 6 | **승격** — *"I have great taste and my users believe uh I have great taste as well"* → 레시피 다음 버전 | — | 15:41~15:50 |

그리고 *"The secret is you keep doing this over and over again"*(15:54~15:55). → [[agent-recipes]]

### 1번의 요점 — 코드화할 생각도 못 한 행동

에이전트가 빅테크 직원에게 연락하는 경향: *"You don't want to try to hire John Carmack, but an agent would think that's oh, John Carmack is great. Why would I not reach out to him?"*(13:25~13:34). *"this is a behavior that you you'd never think of codifying, but you discover the agent tends to be that"*(13:34~13:42). 즉 **taste의 조항은 사전에 쓰는 것이 아니라 트레이스에서 발견된다.** *"Patterns is how you discover the signals and inform you what you should do next."*(13:44~13:47)

## 세 겹의 판정 (11:42~12:15)

> *"you can think of the worker as the inner loop and it generates all these artifacts. But how you look at the artifacts and know what to change is the taste. … And experiments is what how you self-calibrate that okay, my taste is actually validated in production with users."*

| 층 | 역할 |
|---|---|
| **worker** (내부 루프) | 산출물 생성 |
| **taste** (제작자 → judge) | 산출물을 보고 **무엇을 바꿀지** — 변경 후보 생성 |
| **experiments** (사용자) | 제작자의 taste가 **사용자에게도 옳은지** 보정 |

*"not only the maker is happy through the um offline evals, but the end users are happy as well and they agree with what we consider good"*(12:06~12:15). 비유: *"What would Miranda do"*(16:25~16:27, *The Devil Wears Prada*).

## taste는 이식 가능한가 — 이 소스의 입장

> *"How How do I make my taste as an artist or as a software developer um something that anyone can download in their brain and be able to be a one-to-one replica to me."* (11:14~11:26)

그리고 RL은 *"how do we uh turn these um tastemakers into environments and evals around them so then we can move them into the weights"*(11:28~11:39). → [[taste-vs-judgment]]

> ⚠️ **Contradiction: taste는 모델 수준에서 풀 수 있는가.** [[paul-bakaus|Paul Bakaus]]: *"I don't think taste can be solved at a model level"*([[tech-bridge-skill-engineering-dark-arts]] 56:28~56:34), 취향은 **희소**해서 보급되면 사라진다. 이 소스: taste를 eval로 코드화해 **남에게 내려받게 하고**, 가중치로 옮긴다. 다만 이 소스도 **최종 판정을 사용자 A/B에 넘긴다** — 즉 코드화된 taste가 옳은지는 사람(사용자)이 정한다. 둘 다 측정이 없다.

## 이 위키의 다른 eval 절차와

- [[skill-evals]]([[lauren-tan|Lauren Tan]]) — 스킬을 고칠 때마다 서브에이전트로 시험, 판정자 편향을 사람이 다룬다. 이 페이지는 **eval 생성까지 에이전트**에 맡기고 사람의 몫을 **동의/비동의 한 질문**으로 줄인다. ⚠️ 그 축소가 충분하다는 근거는 없다.
- [[generator-evaluator-pattern]] — 평가자 분리. 이 페이지의 새 점은 평가자(judge)를 **트레이스의 패턴에서 자동 생성**하고 **사람이 보정**한다는 것.
- [[self-harness]] — 트레이스 → 약점 → 수정안 → **회귀 테스트**로 채택. 이 페이지의 채택 게이트는 **사람 보정 + 사용자 A/B**.
- [[verifiable-goals]] — 주관 영역에 verifier를 세우는 문제(09-12 절). 이 페이지의 답: **verifier = 제작자 taste의 코드화 + 사용자 실험으로의 보정.**
- [[production-trace-eval-flywheel]] — 같은 날(09-29) 업로드된 W&B ARIA 편의 *프로덕션 트레이스 → 오프라인 eval* 플라이휠. 트레이스에서 eval을 뽑는 방향이 같다. ⚠️ 비교는 그 페이지 쪽을 볼 것 — 이 페이지는 내용을 확인하지 않고 링크만 건다.

## ⚠️ 유보

- **보정의 비용** — judge 하나에 사람 질문 하나로 되는가? 불일치 시 절차는? 없다.
- **사용자가 동의하지 않으면** — 제작자 taste를 버리는가, 사용자를 고르는가? 말하지 않는다.
- **A/B 지표** — 무엇을 "동의"로 세는지(답장률·채용 성사?) 없다.
- **"one-to-one replica"** — 비유이며 검증 방법 없음.

## References

- [[tech-bridge-introspection-loop-is-the-product]] (first-seen)
- 관련: [[taste-vs-judgment]] · [[agent-recipes]] · [[loop-is-the-product]] · [[skill-evals]] · [[generator-evaluator-pattern]] · [[self-harness]]
