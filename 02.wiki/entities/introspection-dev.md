---
title: Introspection
type: entity
category: org
tags: [startup, agent-infra, evals, agent-recipes, auto-research]
aliases: [Introspection, introspection.dev, pi.recipes]
links:
  - https://www.introspection.dev/blog
sources: [tech-bridge-introspection-loop-is-the-product]
created: 2026-09-30
updated: 2026-09-30
---

# Introspection

xAI 출신 [[roland-gavrilescu|Roland Gavrilescu]]와 (이름이 나오지 않는) 공동창업자가 세운 회사. **에이전트 루프가 남긴 것을 "에이전트 레시피"로 증류하는 도구**를 만든다고 스스로 설명한다 — *"we are introspection, but you can think of introspection as the way you generate these recipes. So, they're recipes for introspecting on your on your system"*(06:43~06:49). 본 위키 첫 등장([[tech-bridge-introspection-loop-is-the-product]]).

> ⚠️ **슬러그를 `introspection-dev`로 둔 이유.** "introspection"은 모델 내성(interpretability) 연구 등 일반명사로도 쓰이므로 설명란의 도메인(`introspection.dev`)을 붙였다. 회사명은 자막에 한 번(*"we are introspection"* 06:43, 소문자 ASR) 나오고, ko는 이를 **"자기 성찰"** 로 옮겨 회사명이 사라진다. 설립 시점은 *"we left a few months ago"*(00:23, xAI를 떠난 시점)뿐이다.

## 제품 — pi.recipes (조기 공개)

*"we have an early release of recipes. It's called pi.recipes. It's very similar to skills uh used to be in 2025, but it's going a step forward"*(08:05~08:13). 담는 것(08:16~08:41):

- taste를 eval로 코드화하는 법, eval 실행, eval을 계속 개선하는 루프
- 어떤 신호를 쓸지와 신호 처리
- 특정 모델과 맞는 도구, **모델별 하네스 프로필**

설계 원칙: *"portable and provider agnostic"*(06:54~06:55), *"we built our um approach to recipes on the Pie Harness and on Harbor for evals"*(06:57~07:00), Git 저장소에 담아 *"everything could be versioned"*(07:07~07:10), *"meant to be owned by you, but managed by your agents"*(07:14~07:17). → [[agent-recipes]]

> ⚠️ **"Pie Harness"** 는 en-orig ASR — 제품명 *pi*.recipes와 같은 이름의 **Pi 하네스**로 읽는다(추정). [[understand-anything]]의 지원 플랫폼 목록에 있는 *Pi* 와 같은 것인지 **미확정**. **Harbor**는 이 위키에 [[terminal-bench|Terminal-Bench]]의 실행 환경으로 기록된 이름이다 — 같은 것인지 **추정**. *"It's still early"*(08:44). 형식·예시·라이선스는 말하지 않았고, 이 위키는 사이트를 열어 보지 않았다.

## 겨냥하는 고객

맺음말: *"vertical SaaS companies"* 와 *"agent labs"* — *"creating these like auto research labs around their their own products"*(17:53~18:05). *"we're building some very interesting products around how to deploy this in production"*(17:41~17:45). → [[automated-ai-research]]

## References

- [[tech-bridge-introspection-loop-is-the-product]] · [[roland-gavrilescu]] · [[agent-recipes]]
