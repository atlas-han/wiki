---
title: "Scripts that talk back — 스크립트 stdout으로 다음 행동을 지시한다"
type: concept
category: technique
tags: [agent-skills, harness, instruction-following, scripts, prompt-caching, weakest-model]
aliases: [scripts that talk back, 스크립트 stdout 지시, stdout steering, 말을 되돌려주는 스크립트]
related: [agent-skills, hook-enforced-workflow, cross-harness-skill-compilation, hard-vs-soft-enforcement, anti-attractor, harness-engineering]
first-seen: tech-bridge-skill-engineering-dark-arts
sources: [tech-bridge-skill-engineering-dark-arts]
created: 2026-09-28
updated: 2026-09-28
---

# Scripts that talk back

**스킬 본문(산문)에 묻힌 규칙은 모델이 훑고 지나간다. 같은 지시를 스킬 안에서 실행되는 스크립트의 표준 출력(stdout)으로 — 지금 상태에 맞춰, "다음에 정확히 이것을 하라"는 형태로 — 돌려주면 훨씬 잘 따른다. 대가는 프롬프트 캐싱이다.** [[paul-bakaus]]의 [[impeccable|Impeccable]] 워크숍 기법 5([[tech-bridge-skill-engineering-dark-arts]], 25:09~29:25).

## 문제 — buried rules get skimmed

> *"buried rules get skimmed"* (25:12)

자기만 쓰는 스킬이면 모델을 안다(Opus든 Codex든). **배포**하면 Sonnet·Haiku·Grok·Gemini 사용자가 생긴다(25:42~25:58) — *"you need to build for the lowest common denominator and ideally for (…) the one model that is the weakest a[t] instruction following"*(26:10~26:18). *"GPT5 mini is not a very good rule follower"*(26:18~26:21) — Impeccable에서도 특정 MD 파일을 로드하지 않고 라이브 모드를 띄우지 못한다(26:24~26:35). *"it gets especially bad with longer skills that have lots of rules"*(26:40~26:45).

## 기법 — 스킬을 "bionic"으로

> *"impeccable really is kind of bionic of sorts. It's really not just pros[e]. It is a combination of scripts that run in line within the skill at certain times uh and then pros[e] around it."* (26:47~27:00)

Impeccable은 호출마다 `context.mjs`를 실행한다(27:00~27:05):

| 상황 | 스크립트가 돌려주는 것 |
|---|---|
| `product.md`(대상·목표 등 제품 전략 — *"almost like design MD but it is for product strategy"* 27:14~27:18)·`design.md`가 있음 | 두 파일을 모아 세션에 넣는다(27:33~27:41) |
| 없음 | **구조화된 JSON** — *"by the way there is no product MD and here's exactly what you should do about it"*(27:45~27:56) |
| 새 버전 있음 | 업데이트할지 **사용자에게 물어라**는 지시(27:59~28:15) — 자기 업데이트, 사용자 허락 하에 |

> *"it will always tell the model the exact instructions on what to do next. And the really interesting thing about this is that I found that that works significantly better than some random rule in the pros[e] of the main s[kill]"* (28:17~28:30)
>
> *"when you put something out (…) from the standard out of a script uh somehow the model will follow it a lot uh more than before"* (28:33~28:43)

적용처(화자): 환경 인식 설정 · 동적 온보딩 · 저장소 상태 게이팅 · 적응형 흐름(28:46~28:50).

**재사용 — 라이브 모드.** 기법 7에서 폴러 서버가 종료하며 stdout에 메시지를 남기면 모델이 *"oh, something happened. I better do something"* 하고 깨어나 스킬의 이벤트 처리 지시를 따른다(36:16~36:40). **stdout이 하네스 이벤트를 모델에게 전달하는 통로**가 된다. 그리고 [[anti-attractor]]의 `color.js`도 같은 모양(스크립트가 모델에게 시드를 준다)이다.

## 대가 — 프롬프트 캐싱

> *"it does so at the expense of prompt caching (…) if you run the skill many many times (…) this is not a good technique to use, but I found it to be very useful in really interactive scenarios."* (29:10~29:25)

Q&A에서 보충: 결과가 매번 다르면 *"a dynamic shell execution"* 이라 그 부분은 캐시되지 않지만 *"the skill will still be cached"*(51:12~51:21) — **정적 인라인 콘텐츠 대 동적 호출**의 구분이다(51:25~51:34).

## 이 위키에서의 자리

- **[[hard-vs-soft-enforcement]]의 중간 층.** 산문 규칙(soft)과 훅의 차단(hard) 사이에 **"지금 할 일을 지금 말해 주기"** 가 있다. 강제는 아니지만 **위치**(컨텍스트 맨 끝, 도구 결과)와 **구체성**(상태에 맞춘 한 가지 지시)으로 따를 확률을 높인다. ⚠️ 위키의 정리 — 화자는 *"somehow"* 라며 이유를 모른다고 한다.
- **[[hook-enforced-workflow]]와의 차이** — 훅은 하네스가 부르고, 이 스크립트는 **스킬이 부른다**(모델이 스킬을 불러야 동작). 그래서 화자는 기법 6에서 *"the harnesses forget to simply call impeccable"*(30:02~30:06)을 따로 훅으로 푼다.
- **progressive disclosure의 동적 판** — [[agent-skills]]의 *필요할 때 파일을 로드* 가 정적 파일이 아니라 **실행 결과**로 바뀐다.
- [[cross-harness-skill-compilation]] — 가장 약한 모델을 기준으로 삼는 이유가 이 기법의 출발점이다.

## ⚠️ 표시해 둔 것

- **"significantly better"의 측정 없음.** 화자의 eval 하네스(비공개)로 확인했는지 말하지 않는다.
- **자기 업데이트 경로의 보안** — 스크립트가 *"there's an update available"* 를 알리고 사용자 허락으로 갱신한다. 무엇을 어디서 받는지·검증은 논의되지 않는다. [[prompt-injection]] 관점에서 **스크립트 stdout은 모델이 특히 잘 따르는 채널**이라는 이 페이지의 전제 자체가 공격 표면의 서술이기도 하다. ⚠️ 위키의 지적, 소스는 다루지 않는다.

## References

- [[tech-bridge-skill-engineering-dark-arts]] (기법 5 · 기법 7 · Q&A 캐싱)
- [[impeccable]] · [[paul-bakaus]] · [[agent-skills]] · [[hook-enforced-workflow]] · [[hard-vs-soft-enforcement]]
