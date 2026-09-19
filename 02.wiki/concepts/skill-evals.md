---
title: 스킬 eval (Skill Evals)
type: concept
category: technique
tags: [evals, testing, subagents, judge, blinding, hill-climbing]
aliases: [에이전트 유닛 테스트, eval playbook, 눈가림 서브에이전트]
related: [skill-self-improvement, generator-evaluator-pattern, agent-verification-skill, verification-cost-asymmetry, agent-skills, transcript-classifier]
first-seen: tech-bridge-lauren-tan-trusting-agents
sources: [tech-bridge-lauren-tan-trusting-agents, tech-bridge-voice-agent-failure-modes, tech-bridge-vercel-eve-filesystem-agent]
created: 2026-09-13
updated: 2026-09-19
---

# 스킬 eval

**스킬을 고칠 때마다 그것이 실제로 의도한 일을 하는지 서브에이전트로 시험하는 절차.** [[lauren-tan]]이 [[tech-bridge-lauren-tan-trusting-agents]]에서 [[pstack|Pstack]]의 `eval playbook`으로 소개했다.

> **eval은 에이전트를 위한 유닛 테스트**입니다. 직접 만들 수 있고 **특별한 프레임워크가 필요 없습니다.**

## 절차

1. **메인 코디네이터 에이전트**가 그 스킬이 무엇을 해야 하는지 **루브릭**을 만든다
2. **서브에이전트를 여럿 띄우고 각각 개별 디렉터리**를 준다
3. **디렉터리 이름을 교묘하게 지어 서브에이전트가 평가받는 중임을 모르게** 한다
4. **여러 모델에 걸쳐** 돌려 행렬로 본다
5. **다른 모델의 판정 에이전트(judge agent)** 로 교차 참조해 첫 모델의 편향을 확인
6. **언덕 오르기** — `/loop` 로 *"전부 10점 만점이 될 때까지"* 반복

## 눈가림 — 이 위키에 처음 등장하는 기법

> 디렉터리 이름은 **서브에이전트가 자기가 평가받고 있다는 걸 모르도록** 교묘하게 지어집니다 — **에이전트는 실제로 알아챌 수 있고, 알아채면 행동을 바꾸기** 때문입니다.

**평가 사실 자체가 관찰 대상을 바꾼다**는 문제를 실무 절차로 다룬 첫 사례다. 이 위키의 [[training-time-risk]]·[[agentic-misbehavior]]가 다뤄 온 *모델이 평가 상황을 인지한다* 는 논의가 **개인 워크플로 층**에 내려온 형태다.

> ⚠️ **근거는 관찰 진술뿐이다.** 얼마나 자주 알아채는지, 눈가림이 얼마나 효과가 있는지 **수치가 없다.**

## 언덕 오르기가 성립하는 조건

eval이 점수를 내놓기 때문에 루프를 돌릴 수 있다. 이는 [[verification-cost-asymmetry]]의 사례다 — **스킬의 좋음을 판정하는 비용이 스킬을 고치는 비용보다 싸야** `/loop`가 성립한다.

→ [[generator-evaluator-pattern]] · [[ralph-wiggum-method]]

## 유지의 조건은 도구가 아니다

> **스킬을 유지하는 건 꽤 어렵습니다. 취향과 관찰이 많이 필요**합니다. **뒷좌석 운전자 노릇을 아주 잘해야** 해요.

→ [[agent-manager-analogy]] · [[taste-vs-judgment]] · [[skill-self-improvement]]

## 표시해 둔 것

> ⚠️ **작성자=검증자 문제가 닫히지 않는다.** 판정 에이전트는 다른 모델이지만 **루브릭을 만드는 것은 여전히 코디네이터 에이전트**다. 2026-09-09 Cursor 편에서 처음 표시한 빈자리의 **세 번째 반복**이다.
>
> ⚠️ **10점 만점이 무엇을 뜻하는지**(루브릭의 항목·가중치)가 소스에 없다.

## 해상도의 축 — 어느 단위로 재는가 (2026-09-19)

[[tech-bridge-voice-agent-failure-modes]]가 eval에 **세 번째 질문**을 붙인다.

| 질문 | 다루는 페이지 |
|---|---|
| **무엇을 재는가** (합격 기준) | [[all-or-nothing-accuracy]] |
| **어떻게 세는가** (진짜 비용) | [[true-cost-to-perfect-answer]] |
| **어느 단위로 재는가** | **[[field-level-unit-test-evals]]** ← 새로 |

> **여러분의 모든 평가(eval) 도구는 이러한 필드들을 단위 테스트처럼 취급해야 합니다.** … **단지 하나의 필드 수집에 문제가 있다는 것을 알아내기 위해 수백 건의 엔드 투 엔드 에이전트 테스트 케이스를 실행하지는 않잖아요.** (20:32~21:12)

E2E는 통과/실패만 주고 **어디가 깨졌는지 주지 않는다.** [[all-or-nothing-accuracy]]가 *80%는 쓸모없다* 고 했는데, **80%가 왜 80%인지** 를 알려면 이 해상도가 필요하다.

그리고 처방이 프롬프트도 파인튜닝도 아니다:

> 이런 사고방식이 **모든 것을 더 체계적으로 만들어준다**고 생각해요. **프롬프트를 잔뜩 넣고 매번 몇 글자씩 바꿔가면서 … LLM이 마법처럼 … 따르기 시작할 거라고 기대하는 대신에요.** (21:12~21:30)

**같은 날 ingest한 [[tech-bridge-vercel-eve-filesystem-agent|Vercel 편]]이 eval의 다른 실패를 보여준다** — 점수가 아니라 **분포**다. eval 30%를 통과하던 에이전트가 첫 배포에서 *"끔찍하다"* 는 반응을 받았고, 이유는 *예상치 못한 질문* 이었다. 두 소스를 겹치면: **eval은 어느 단위로 재는가(해상도)와 무엇을 재는가(분포) 양쪽에서 실패할 수 있다.** 서로를 모르는 두 소스다.

## References

- [[tech-bridge-lauren-tan-trusting-agents]] · [[pstack]] · [[generator-evaluator-pattern]] · [[verification-cost-asymmetry]] · [[skill-self-improvement]] · [[agent-skills]] · [[lauren-tan]]
