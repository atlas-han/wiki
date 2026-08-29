---
title: "Tech Bridge — 프롬프트 대신 명세(Spec)를 작성할 때"
type: source
tags: [spec-driven-development, spec-kit, github, copilot, mcp, video]
source-url: https://www.youtube.com/watch?v=F_smvU3oqbU
source-type: video
author: Tech Bridge (한국어 자막 재배포)
date-published: 2026-08-29
ingested: 2026-08-29
created: 2026-08-29
updated: 2026-08-29
---

# Tech Bridge — 프롬프트 대신 명세(Spec)를 작성할 때

[[tech-bridge|Tech Bridge]] 채널이 한국어·영어 자막을 입혀 재배포한 22:07 영상. 프롬프트를 일회성 지시로 쓰는 대신 **명세(spec)를 메인 아티팩트**로 삼는 [[spec-driven-development|스펙 주도 개발]]을 소개하고, GitHub [[github-spec-kit|Spec Kit]](`specify` CLI) + Copilot 연동을 실전 워크플로로 보여 준다.

> ⚠️ 2026-08-29 ingest 시 YouTube timedtext HTTP 429로 **영상 자막 전문을 받지 못함**. 아래 takeaway는 채널 설명(1차 메타데이터)과 Spec Kit 공식 문서(complementary)의 교차다. MCP 데모·엔터프라이즈 3원칙의 세부는 자막이 확보되면 보강.

## 핵심 takeaways

1. **프롬프트 중심 vs 스펙 중심**. 프롬프트는 세션이 끝나면 사라지는 지시. 스펙은 저장·리뷰·재실행 가능한 계약이라 같은 입력에서 같은 결과를 기대할 수 있다. 본 위키의 [[verifiable-goals]]·[[sprint-contract]]와 같은 자리 — *done의 정의를 코드 작성 전에 문서로 고정*.

2. **4단계 코어 구조** (채널 설명): **Constitution → Spec → Plan → Task**.
   - Constitution: 프로젝트 비협상 원칙. 이후 spec/plan/task가 이 원칙에 대해 평가된다.
   - Spec: *무엇을·왜* (사용자 대면 행동). 스택은 여기 두지 않는다.
   - Plan: *어떻게* (프레임워크·인프라·제약).
   - Task: 에이전트가 집어서 실행할 위상별 작업 목록.

3. **도구**. GitHub Spec Kit(`specify` CLI)가 템플릿·슬래시 커맨드( `/speckit.constitution` 등)를 제공하고 Copilot 등 코딩 에이전트와 붙는다. 채널 설명은 Microsoft Build 세션의 **세션 플래너 MCP 서버 구축 데모**도 포함한다고 적는다 — 데모 세부는 자막 없이 기록하지 않음.

4. **위키 합성**. 스펙을 메인 아티팩트로 두는 것은 [[harness-engineering]]의 Context Docs / Global Rules 층을 *저장되는 계약*으로 승격한 형태. [[outcome-engineering]]의 "how 프롬프팅 → 결과 정의"와도 동형.

## 등장 개체·개념

- 채널: [[tech-bridge]]
- 도구: [[github-spec-kit]]
- 개념: [[spec-driven-development]] (메인), [[verifiable-goals]], [[sprint-contract]], [[harness-engineering]], [[model-context-protocol|MCP]], [[outcome-engineering]]

## References

- [원문 영상](https://www.youtube.com/watch?v=F_smvU3oqbU)
- 원문 캡처: `01.raw/articles/2026-08-29_프롬프트 작성은 그만두세요. 이제 명세(Spec)를 작성할 때입니다.md`
- Spec Kit 공식: <https://github.github.io/spec-kit/> · <https://github.com/github/spec-kit>
- Microsoft: [Diving Into Spec-Driven Development With GitHub Spec Kit](https://developer.microsoft.com/blog/spec-driven-development-spec-kit)
