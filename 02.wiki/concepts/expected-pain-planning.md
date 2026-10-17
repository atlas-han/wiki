---
title: "기대 고통으로 계획 깊이 정하기 (Expected-Pain Planning)"
type: concept
category: technique
tags: [planning, spec, rework, code-review, software-factory, cost-model]
aliases: [expected pain, 기대 고통, plan before you build]
related: [spec-driven-development, plan-to-ticket-pipeline, risk-proportional-human-review, verification-bottleneck, sprint-contract]
first-seen: tech-bridge-horthy-state-of-software-factory
sources: [tech-bridge-horthy-state-of-software-factory]
created: 2026-10-16
updated: 2026-10-16
---

# 기대 고통으로 계획 깊이 정하기

**에이전트에게 맡기기 전 계획에 얼마나 시간을 쓸지는 "바꿔야 할 확률 × 그 변경이 얼마나 아픈가"(expected pain)로 정한다 — 계획은 기대 고통을 없애는 일이다.** [[dex-horthy|Dex Horthy]]의 "12 factor factories" 1번 항목([[tech-bridge-horthy-state-of-software-factory]]).

> *"Number one is plan before you build. 20 minutes 30 minutes up front can save you hours during review."* (09:19~09:24)
>
> *"I think of this in terms of expected pain, right? How how likely will you have to change something and how painful is that change?"* (10:26~10:32) · *"But planning is about eliminating expected pain."* (10:48~10:52)

## 곡선 (화자의 직관 수치)

| 투입 | 재작업 확률 |
|---|---|
| 두 문장 프롬프트(*"YOLO"*) | *"probably a 50% chance you're going to be doing more prompting later"*(09:59~10:04) |
| 손으로 쓴 상세 스펙 5시간 | *"maybe there's only a 10% chance (…) You just do a little bit of polish at the end."*(10:05~10:14) |
| 코드 전부를 손으로 20시간 | *"there's a 0% chance you have to rework it because of something the agent did. Uh, you might still have to fix stuff. Uh, this is why we had code review before."*(10:14~10:26) |

- 아픈 변경만 계획에서 다툰다 — 버튼 색은 *"I know I can go change that later. That's not going to be hard."*(10:38~10:42)
- *"don't over plan though. You can easily put too much time planning."*(09:55~09:59) — *"you got to find your way up and down this curve depending on the task and depending on the code base"*(10:42~10:46).
- 이것은 AI 이전부터 팀이 배운 것이다: *"if it takes hours or days to build something, and if it takes hours or days to review something, then we better get together as a team and talk about it before we start building"*(09:27~09:39).

## 위키에서의 자리

- [[spec-driven-development]] — 스펙을 *항상* 메인 아티팩트로 두는 쪽과 달리, 계획 깊이를 **과제별로 고르는** 비용 모델이다.
- [[risk-proportional-human-review]] — 리뷰 깊이를 위험에 비례시키는 것과 같은 구조를 **계획 단계**에 적용.
- [[verification-bottleneck]] — 앞단 계획이 뒷단 리뷰 시간을 줄인다(*"save you hours during review"*).

## ⚠️ 유보

- 50%·10%·0%는 측정값이 아니다(*"I think of this is like"*). 설명란의 *"수십 시간의 디버깅과 전면 재작업을 막아줍니다"* 는 발화보다 강하다. ko 자막은 *5 hours* 를 **"5일"** 로 옮긴다.

## References

- [[tech-bridge-horthy-state-of-software-factory]]
