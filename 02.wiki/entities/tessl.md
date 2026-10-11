---
title: Tessl
type: entity
category: org
tags: [agent-enablement, harness-engineering, software-factory, skills-registry, vendor]
links:
  - "https://tessl.io"
  - "https://x.com/tessl_io"
sources: [tech-bridge-tessl-harness-engineering-factory, tech-bridge-sdd-enterprise-lessons, tech-bridge-anthropic-dreaming-memory]
created: 2026-10-11
updated: 2026-10-11
---

# Tessl

자신을 **"agent enablement platform"** 으로 소개하는 회사 — *"We help you go from scaling skills to building your own software factory."*(00:04~00:16, [[tech-bridge-tessl-harness-engineering-factory]]). 이 위키에서는 오래 **이름으로만** 나왔고(SDD 도구 목록, 행사 설명란 링크), 2026-10-10 업로드된 [[dru-knox|Dru Knox]](head of product and design)의 발표가 **Tessl 사람이 직접 말하는 첫 소스**다.

> ⚠️ **철자.** 자동 자막은 *"Tessle"*·*"Tesla"*·*"TESL"* 로 흔들리고 ko·`en`은 *"Tesla Agent"*·*"Tesla Launch"* 로 적는다. 설명란 링크 `tessl.io`·`@tessl_io` 로 **Tessl** 로 판독한다.

## 제품 (자사 서술 — ⚠️ 당사자 진술, 수치 없음)

[[tech-bridge-tessl-harness-engineering-factory]] 15:09~19:24에서 화자가 설명한 것:

| 제품 | 하는 일 (en-orig) | 대응하는 레이어 |
|---|---|---|
| **skills registry** | *"publish and version the workflows and the automations (…) with built-in governance things like security reviews, quality reviews, controls for who can publish and update what"*(16:35~16:50) | control plane |
| **이슈 트래커 → GitHub 커넥터** | *"Right now we're focused on linear[=Linear] to GitHub"*(16:52~16:56) | control plane |
| **코드 리뷰 도구** | 에이전트 코드 리뷰 기준 + 타깃 검사(17:03~17:12) | control plane |
| **Tessl Agent** | PR·이슈를 훑어 반복 작업을 찾아 스킬 + GitHub Action으로(17:41~18:09), 주간 기성 유지보수 스캔(18:09~18:32) | improvement loops |
| **`tessl launch`** | 스킬을 자동화 워크플로로 — 코딩 에이전트 선택(Tessl Agent 또는 *"codeex cloud code gemini"*), 샌드박스, 장시간 실행, GitHub 토큰으로 PR·코멘트 응답(18:34~19:10) | improvement loops |

포지셔닝: 작은 단계(*"rather than one massive snake eating the moose all at once"*), *"batteries included"*(모범 사례를 대신 따라감), *"modular and open"* — *"we don't think every component of a factory is going to be best-in-class with a single company"*(15:58~16:05). 자사 코딩 에이전트를 기본값으로 밀지 않는다(18:48~18:56).

사내 작업 방식(⚠️ 자사 서술): 모든 작업이 이슈 → 샌드박스의 headless 에이전트 → PR → 엔지니어 코멘트(11:40~11:56).

## 이 위키에 이름으로 나온 자리

- [[tech-bridge-sdd-enterprise-lessons]] — [[simon-martinelli|Martinelli]]가 SDD 도구 목록에 *"Tessl"* 을 [[kiro|Kiro]]·[[github-spec-kit|Spec Kit]]·BMAD와 함께 *"too developer centric"* 으로 묶음(03:07~03:24), Tessl의 AI Native Dev 사이트에서 Simon Maple의 글로 SDD를 접했다(02:07~02:20).
- [[tech-bridge-anthropic-dreaming-memory]] · [[tech-bridge-sdd-enterprise-lessons]] — 설명란 링크가 `tessl.co`(AI DevCon으로 보임). ⚠️ 행사 주최 여부는 확인되지 않았다.
- ⚠️ 위 두 소스가 말한 *spec 도구로서의 Tessl* 과 이번 발표의 *agent enablement platform / 스킬 레지스트리* 가 같은 제품 계열인지는 소스에 없다.

## References

- [[tech-bridge-tessl-harness-engineering-factory]] · [[dru-knox]] · [[harness-engineering]] · [[software-factory]] · [[inner-outer-meta-loops]] · [[agent-skills]]
- [[tech-bridge-sdd-enterprise-lessons]] · [[tech-bridge-anthropic-dreaming-memory]] · [[spec-driven-development]]
