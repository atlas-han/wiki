---
title: "기대 고통으로 계획 깊이 정하기 (Expected-Pain Planning)"
type: concept
category: technique
tags: [planning, spec, rework, code-review, software-factory, cost-model]
aliases: [expected pain, 기대 고통, plan before you build]
related: [spec-driven-development, plan-to-ticket-pipeline, risk-proportional-human-review, verification-bottleneck, sprint-contract, action-reversibility]
first-seen: tech-bridge-horthy-state-of-software-factory
sources: [tech-bridge-horthy-state-of-software-factory, tech-bridge-dex-horthy-twelve-rules-no-slop-factory]
created: 2026-10-16
updated: 2026-11-26
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

## 2026-11-26 — 규칙 3과 4로 갈라졌다: 계획하라, 과하게는 말라 ([[tech-bridge-dex-horthy-twelve-rules-no-slop-factory]])

Code Summit 발표의 해설에서 같은 곡선이 다시 나온다. 10-15 소스에서 한 항목 안의 단서였던 *don't over plan* 이 독립된 네 번째 규칙이 됐다.

- 규칙 3: *"앞에서 30분을 쓰면 리뷰에서 몇 시간을 아낀다는 겁니다."*(05:22~05:24) *"만드는 게 빨라져도 제대로 하는 리뷰는 여전히 느립니다."*(05:32~05:34)
- 규칙 4: *"계획을 과하게 하지 말라."*(05:40~05:42) 본인의 경험으로 전해진 것: *"자신도 명세에 여섯 시간을 쓰고 나서 그냥 대충 시킬 걸 그랬다 싶었던 적이 있답니다."*(05:43~05:47)
- Horthy 원음(en-orig 단일 트랙) — 수치는 10-15와 같다: *"You could spend 5 hours handwriting a detailed spec and maybe there's a 10% chance you have to change afterward."*(05:55~05:59) *"Or you could write all the code by hand in 20 hours and then there's like a 0% chance."*(06:01~06:04) (짧은 프롬프트 쪽은 앞이 잘려 *50%* 만 남았다.)
- 정의의 두 번째 표현: *"I think about this in terms of expected pain. Like, how likely will this have to change later, how hard will it be to change?"*(06:10~06:17)
- ⭐ 예가 짝을 이뤘다 — 버튼 색의 반대편에 스키마: *"I don't argue with the model during planning about what color it is, but do make our database schemas right and stuff like that."*(06:20~06:25) 내레이션의 정리: *"버튼 색은 나중에 바꿔도 되지만 데이터베이스 구조는 그렇지 않으니까요."*(06:32~06:34) → [[action-reversibility]]

⚠️ 수치는 여전히 직관이다. 두 발표의 원음이 서로 다른 트랙 품질로 잡혀 문구가 조금 다르다(*how painful is that change* / *how hard will it be to change*).
