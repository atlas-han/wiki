---
title: "Inner · Outer · Meta 루프 (소프트웨어 팩토리의 세 루프)"
type: concept
category: pattern
tags: [harness-engineering, software-factory, feedback-loops, autonomy, automation, quality, meta-loop]
aliases: [inner loop, outer loop, meta loop, 메타 루프, loop engineering]
related: [harness-engineering, software-factory, factory-engineering, loop-is-the-product, skill-self-improvement, self-harness, structure-sensitive-tests, agent-visual-qa, scheduled-agent-automations, agent-trust-curve, in-context-learning, feedforward-feedback-steering]
first-seen: tech-bridge-tessl-harness-engineering-factory
sources: [tech-bridge-tessl-harness-engineering-factory]
created: 2026-10-11
updated: 2026-10-11
---

# Inner · Outer · Meta 루프

**코딩 에이전트의 작업을 개발 단계별 세 루프로 나누고, 각 루프의 개선이 서로 다른 기둥(autonomy · automation · quality)을 끌어올린다는 틀.** [[tessl|Tessl]]의 [[dru-knox|Dru Knox]]가 [[tech-bridge-tessl-harness-engineering-factory]]에서 하네스 엔지니어링의 작업 대상으로 제시했다 — *"You are building the loops that automate and improve the quality of your factory."*(06:26~06:35)

| 루프 | 위치 | 비용·빈도 | 끌어올리는 것 | 예 (en-orig) |
|---|---|---|---|---|
| **inner** | PR을 올리기 *전*, 에이전트가 작업 중 | *"very fast iterative loops. You want them to be cheap. You're expecting the agent to run them all the time."*(06:55~07:00) | **autonomy** — 사람 개입 없이 잡고 고친다(07:00~07:09) | (발화 없음) |
| **outer** | PR이 올라간 *뒤* | *"more expensive exhaustive checks"* — PR당 한 번, 결과를 에이전트가 반복 수정(07:15~07:50) | **automation** — *"encode things that otherwise a human would have to verify to build confidence in the system"*(07:22~07:30) | *"agentic QA"*, *"mutation testing to check the quality of our test suite"*(07:36~07:45) |
| **meta** | 개발 프로세스 *바깥* | 상시 관찰 | **quality** — *"This is where you'll drive quality"*(07:53~07:59) | 에이전트 로그·PR·이슈 트래커·사용자 피드백을 보고 새어 나간/사람이 막은 실수를 찾아 *"feeds back into the inner and the outer loop to make sure that that mistake is not made again"*(08:01~08:26) |

## 핵심 주장

- **기둥의 순서와 루프의 순서가 맞물린다**: autonomy를 먼저(inner), 그다음 automation(outer), 품질은 유지하다가 meta로 올린다(04:11~04:20).
- **진척의 레버는 meta loop**: 세 루프의 인프라가 갖춰지면 *"you're going to be driving it up by investing in your metal[=meta] loop"*(08:27~08:44).
- **meta loop의 부품**(레이어 3 "improvement loops", 14:11~15:07): 매일·매주 repo 스윕, 플레이북, 반복 작업 자동화, 출력 품질 점검 → **스킬 갱신**(*"Let's update a skill (…) so it doesn't make this mistake again"* 14:56~15:07).
- meta loop를 돌리려면 신호가 **legible**해야 한다 — 로컬 로그·개인 머신·머릿속의 정보를 기록되는 표면으로(10:42~11:00) → control plane.

## 위키에서의 좌표

- **[[harness-engineering]]** — §3 System Evolution(*"every mistake becomes a rule"*)을 사람의 습관이 아니라 **meta loop라는 상시 장치**로 만든 것. 규칙의 목적지는 스킬·플레이북.
- **[[self-harness]] · [[skill-self-improvement]]** — meta loop의 자동화판(트레이스에서 규칙 합성, observer 에이전트가 스킬 수정).
- **[[loop-is-the-product]]** — Gavrilescu의 *두 번째 루프*(첫 루프의 산출물을 보고 무엇을 바꿀지 정한다)가 meta loop와 같은 자리.
- **[[feedforward-feedback-steering]]** — inner/outer의 검사는 feedback 센서, meta loop가 고치는 스킬·플레이북은 feedforward 가이드.
- **[[structure-sensitive-tests]]** — outer loop의 mutation testing은 *테스트 스위트의 품질* 을 재는 장치.

> ⚠️ **용어 충돌.** 같은 단어가 위키 안에서 다른 칸을 가리킨다.
> - [[lauren-tan|Lauren Tan]]: *"cursor projects are my inner loop and grabbot[=GrokBot] is my outer loop"*([[tech-bridge-lauren-tan-pocock-podcast-full]] 42:55~43:00) — outer = **Slack·Sentry 같은 외부 신호를 구독해 일을 시작하는 루프**. Knox 틀에선 외부 신호(로그·이슈·사용자 피드백)를 보는 것이 **meta**이고, outer는 **PR 뒤 검사**다.
> - [[in-context-learning]](Karpathy): inner = activation 안의 학습, outer = SGD. 모델 층위의 다른 개념.
> - [[assistance-vs-automation]]: *automation* = 사람을 빼는 것이 목표. Knox의 *automation* = 리뷰 없이 받아들일 수 있는 **신뢰의 정도**.
> 이 페이지의 inner/outer/meta는 **Knox의 정의**로만 쓴다.

> ⚠️ **한 화자, 한 벤더, 측정 없음.** 화자 스스로 레이어 이름을 *"aren't by any means standard terms"*(11:10~11:14)라 한다. 루프 개선이 기둥을 올린다는 대응은 화자의 틀이지 데이터가 아니다.

## References

- [[tech-bridge-tessl-harness-engineering-factory]] — first-seen (Dru Knox, Tessl)
- [[harness-engineering]] · [[software-factory]] · [[factory-engineering]] · [[loop-is-the-product]] · [[self-harness]] · [[skill-self-improvement]] · [[in-context-learning]]
