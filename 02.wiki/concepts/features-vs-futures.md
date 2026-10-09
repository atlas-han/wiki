---
title: "Features vs Futures — 기능을 낼 때마다 미래 선택권을 태운다"
type: concept
category: framing
tags: [optionality, refactoring, technical-debt, augmented-development, software-economics, kent-beck]
aliases: [features vs futures, futures versus features, 기능 vs 미래 선택권, optionality, 옵션 가치]
related: [refactoring, technical-debt, cognitive-debt, spec-driven-development, software-factory, no-one-shot-design, effort-output-outcome-mission]
first-seen: tech-bridge-kent-beck-craft-augmented-development
sources: [tech-bridge-kent-beck-craft-augmented-development]
created: 2026-10-09
updated: 2026-10-09
---

# Features vs Futures

**소프트웨어의 가치는 지금 가진 기능(features)과 다음에 할 수 있는 일의 선택권(futures) 두 축의 합이다. 기능을 하나 낼 때마다 futures를 태우므로, 기능 사이에 멈춰 futures를 되돌리는(리팩터링·정리·재구현) 왕복이 필요하다 — AI 코딩은 이 소진을 극단적으로 빠르게 만든다.** [[kent-beck|Kent Beck]]이 [[tech-bridge-kent-beck-craft-augmented-development]]에서 그림으로 설명했다.

> *"the economic value of a project is the sum of the features that it currently has and the futures all the options that for what it could do next."* (25:17~25:31)

## 그림

| 단계 | 화자 설명 |
|---|---|
| 시작 | *"a wide variety of things that we could do, but we have no features"*(21:00~21:05) |
| 기능 1 | *"we burn some of our futures in order to realize that feature"* — 하위 호환, 철회한 기능의 제약(21:08~21:30) |
| 반복 | *"we burn some more futures in order to get our next feature"*(21:35~21:42) |
| 끝 | *"no options for change at all because everything is such a big mess"*(21:48~21:53) → project 2, 3, 4 |

- 축 이름: *"sometimes I call it optionality, sometimes I call it futures"*(20:35~20:40).
- 기능 진척 곡선은 *"goes fast at first and then it goes slower and slower"*(20:16~20:21).

## AI가 바꾼 것 — 소진 속도

> *"it used to take us a hundred people 10 years to get to this absolute zero state where we can't make any changes without breaking something else. And now with AI, I can do this in the privacy of my own office. One person, one week"* (22:04~22:26)

지니가 끼면 *"the whole thing ramps up. The timelines are shorter"*(26:55~27:03). 화자 자신도 *"I couldn't fix one bug without breaking something else"*(19:20~19:25)로 프로젝트를 다시 시작한다.

## 처방 — 기능 사이의 순간

- Casals의 *"I rest between the notes"*(23:35, ⚠️ 화자 스스로 지어낸 이야기라고 밝힘). 지니가 *"Do you want me to implement the next thing?"*(24:12~24:14) 할 때 *"take a breath and say, huh, maybe I'm not ready"*(24:21~24:24).
- 그 순간에 할 것: 리팩터링, 중복 제거, 가독성 최적화, *"throw away what I just did and implement it again in a different way"*(24:42~25:06). → [[refactoring]]
- 동시에 하지 말고 **왕복**한다 — *"You can't wipe the knife while you're cutting."*(29:01~29:03)
- 멀리서 보면 기능과 옵션이 함께 늘어나는 한 줄로 보인다(28:19~28:35).

## 왜 어려운가 — 가독성(legibility)

기능은 *"visible legible in that seeing like a state sense"*(25:51~25:55), futures는 *"harder to account for"* — *"gilding the lily"* 로 보인다(26:05~26:25). *"It's not written in any spec"*(27:32~27:35). 화자의 기준: *"finished like I don't want to change this software is a failure."*(27:47~27:52)

## 이 위키에서의 자리

- [[technical-debt]] — 같은 현상을 **부채(이자)** 대신 **옵션(자산)** 쪽에서 본다. 부채는 줄일 비용이고, futures는 늘릴 가치다.
- [[cognitive-debt]] — 사람 쪽의 소진. futures는 코드 쪽의 소진.
- [[spec-driven-development]] — *"It's not written in any spec"*: 변경 가능성은 스펙에 적히지 않는다는 것이 Beck의 SDD 비판 한 축.
- [[software-factory]] — 피드백 없이 기능만 내는 다크 팩토리는 futures를 0까지 태우는 가장 빠른 길(화자 경험, 측정 없음).

> ⚠️ **측정 없음.** 그림은 화자의 경험·직관이고 수치 근거가 없다. *"a hundred people 10 years"* vs *"One person, one week"* 는 수사적 대비다.

## References

- [[tech-bridge-kent-beck-craft-augmented-development]] · [[kent-beck]]
