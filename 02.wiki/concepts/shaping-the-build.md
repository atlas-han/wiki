---
title: "Shaping the Build — 무엇을, 어느 단계에 맞게 만들지 정하는 개발자"
type: concept
category: pattern
tags: [shaping-the-build, product-sense, product-gut, full-stack, stage-dependent, prototyping, mvp, one-way-door, spec, coding-agents, andrew-ng]
aliases: [shaping the build, 빌드 형성, 무엇을 만들지 결정, product gut, 단계 의존, stage-dependent, quick and dirty prototype]
related: [ai-engineering-skills-map, action-reversibility, disposable-vs-durable-software, spec-driven-development, taste-vs-judgment, ai-jobs-impact, primitives-before-features]
first-seen: tech-bridge-andrew-ng-ai-engineering-skills-map
sources: [tech-bridge-andrew-ng-ai-engineering-skills-map]
created: 2026-11-01
updated: 2026-11-01
---

# Shaping the Build

**빌드가 쉬워지면 병목은 "무엇을 만들지"로 옮겨 가고, 그 결정과 "지금 어떤 방식으로 만들지"(프로토타입 · 견고한 아키텍처 · 고객 피드백 · 기술 조사)를 함께 정하는 개발자가 더 많이 기여한다**는 역할 정의. [[andrew-ng|Andrew Ng]](제목 · 설명란 · 태그 근거)의 [[ai-engineering-skills-map|네 역량]] 중 넷째이고, [[tech-bridge-andrew-ng-ai-engineering-skills-map]]에서 대담 상대의 질문에 답하며 풀어 말한다.

> *"as building has become easier, the bottleneck is less building, but deciding what to build."*(05:19~05:28)

## 세 겹의 확장

1. **역할의 폭 — full-stack.** 프런트엔드 개발자가 AI 보조로 백엔드까지 한다. Ng 본인은 백엔드 쪽이라 *"I'm a maybe like a bad front-end developer with AI assistance."*(05:43~05:48) → *"a lot of developers have gone from a more narrow role to being a full-stack developer."*(05:48~05:54)
2. **무엇을 만들지 — product gut.** PM이 고객 피드백을 받아 오기를 기다리는 것은 *"much slower than the developer themselves has a little bit of product insight, little bit of product gut."*(06:02~06:10) 단 *"it does not mean engineers should become product managers"*(06:26~06:31).
3. **어떻게 만들지 — 과정의 조향.** *"is this a good time to build an MVP? Or is it a good time to invest in building really robust architecture and thinking about scale? Or is this a good time to go out to customers to get feedback?"*(06:53~07:04) 백엔드 기술 스택을 조사할 때인가도 같은 질문이다(07:04~07:08).

## 답은 단계에 달려 있다

> *"The answer is stage-dependent and it depends a lot on, you know, what Jeff Bezos calls one-way doors versus two-way doors."*(07:16~07:23)

| 단계 | 처방 (en-orig) |
|---|---|
| 초기 | *"build a quick and dirty prototype, see what happens, throw it away, build another quick and dirty prototype, see what happens, and drive rapid learnings."*(07:54~08:01) — 조건: *"so long as you can do it in a responsible, safe way"*(07:49~07:54), 민감 데이터 유출 금지 |
| 성숙 | *"there's also a time and place to thinking carefully about architecture"*(08:01~08:05) — read-write 비율, 고객 요구, 민감 데이터, 보안 인프라 |

같은 축이 **코딩 에이전트 사용법**에도 적용된다: *"you should always plan it out, write a long spec, and there is a place for that."*(08:41~08:46) 그러나 *"if you know you're going to go to bed in 20 minutes, just bang out some stuff, have a coding agent work for a few hours and see what you get the next morning."*(08:48~08:54)

사람도 단계별로 강점이 다르다 — 0→1 단계에 강한 엔지니어와 성숙한 체계적 단계에 강한 엔지니어(08:16~08:22). 단계에 따라 *"velocity versus protecting from downside risk"*(08:33~08:35)의 저울이 움직인다. *"that stage-dependent answer has been very tricky for people to learn."*(08:54~08:59)

## 이 위키에서의 좌표

- [[action-reversibility]] — one-way / two-way door가 **PR · 에이전트 행동** 단위로 쓰였다(Pocock · Tan). Ng은 같은 은유를 **프로젝트 단계** 단위로 쓴다.
- [[disposable-vs-durable-software]] — Kanat-Alexander의 네 기준이 *얼마나 엄격해야 하나* 를 **소프트웨어의 수명**으로 정했다면, Ng은 같은 질문을 **프로젝트의 시점**으로 정한다. 둘 다 *"quick and dirty"* 의 조건으로 **민감 데이터 격리**를 단다.
- [[spec-driven-development]] — 이 위키의 SDD 소스들(09-27 강좌의 소개자 "Andrew" 포함)은 스펙을 **기본값**으로 말했다. 여기서 Ng은 스펙을 **단계의 함수**로 둔다. ⚠️ 09-27 소개자가 Ng인지는 미확정이라 자기 모순으로 읽지 않는다.
- [[tech-bridge-laurie-voss-product-engineer]] — Voss의 product engineer(*사람들이 무엇이 필요한지 알아내고 좋음을 정의하고 에이전트로 출시*)와 같은 방향. Voss는 새 직함을 붙이고, Ng은 *PM이 되라는 뜻은 아니다* 라고 선을 긋는다.
- [[taste-vs-judgment]] — *product gut* 은 이 페이지의 판단 · 취향 축의 개발자판이다.
- [[tech-bridge-andrew-ng-ai-opportunity]] — 08-30 인터뷰에서 Ng은 같은 병목을 **product management bottleneck** 이라 불렀다. 이 편에서는 PM이 아니라 **개발자가 그 병목을 메운다**는 쪽으로 이름이 바뀐다.

## ⚠️ 유보

- 단계 판정 기준(언제 초기에서 성숙으로 넘어가나)은 말하지 않는다. one-way / two-way door 은유를 꺼냈지만 적용 예는 없다.
- *"The answer is stage-dependent"* 는 캡션에 없는 질문에 대한 답이다(편집).
- 1인 전망이고 측정 · 사례는 없다.

## References

- [[tech-bridge-andrew-ng-ai-engineering-skills-map]] — first-seen
- [[andrew-ng]] · [[ai-engineering-skills-map]]
- 관련: [[action-reversibility]] · [[disposable-vs-durable-software]] · [[spec-driven-development]] · [[taste-vs-judgment]]
