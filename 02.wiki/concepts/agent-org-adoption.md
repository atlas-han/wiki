---
title: Agent Org Adoption
type: concept
category: pattern
tags: [agent, organization, verification, culture, figma]
related: [verifiable-goals, harness-engineering, spec-driven-development, sprint-contract, outcome-engineering]
first-seen: tech-bridge-figma-coding-agents
sources: [tech-bridge-figma-coding-agents]
created: 2026-08-29
updated: 2026-08-29
---

# Agent Org Adoption

코딩 에이전트를 **개인 생산성 팁이 아니라 조직 변화**로 다루는 패턴. [[eyal-blum|Eyal Blum]]([[figma|Figma]])이 [[tech-bridge-figma-coding-agents]]에서 제시. 희소 자원은 모델 capability가 아니라 **인간 주의력**.

## 3막 곡선

개인과 회사 공통 ([[tech-bridge-figma-coding-agents]] 00:00–02:15):

1. **1막** — 작은 것이 잘 된다. "10x faster."
2. **2막** — 같은 습관을 큰 문제에 적용하면 실패·버그·신뢰 붕괴.
3. **3막** — 가드레일·프롬프팅·컨텍스트라는 진짜 스킬.

조직에서는 막이 고르지 않다. 워크플로를 바꾼 팀과 신뢰를 잃은 팀이 같이 제품을 내야 하므로, 공존을 지원하면서 3막으로 데려가는 것이 과제.

발표 스스로 3막은 "아직 다 오지 않았다" (클라우드 에이전트 × 레거시 빌드 의존성).

## 네 가지 개입

| 개입 | 요지 | 위키 자매 |
|---|---|---|
| **검증 우선 (left-shift)** | generation보다 verification에 투자. 반복 패턴은 결정론적 플로우로 코드화. 테스트 먼저(red-green). 피라미드 아래를 자동화하고 인간 리뷰는 "이걸 만드는가"만 | [[verifiable-goals]], [[harness-engineering]] System Evolution |
| **프롬프팅 → 기획** | why가 맨 위인 계획서, 한 자리에 리뷰할 크기, 단계별 acceptance. 에이전트는 명세를 실행 | [[spec-driven-development]], [[sprint-contract]], [[outcome-engineering]] |
| **회의론자 = 로드맵** | 시니어 저항을 변환 대상이 아니라 검증 갭의 우선순위 목록으로 | (조직 운영, 기존 페이지 없음) |
| **주의력 소통** | PR/슬랙에서 사람 요약과 AI 생성을 분리 표시. 미표시는 모욕으로 읽힘 | 인간 주의력을 하니스 제약으로 취급 |

## 위키 합성

Anthropic 쪽 [[agent-harness-design]]은 *모델이 못하는 것에 대한 가정*을 하네스에 인코딩한다. 이 페이지는 *조직이 에이전트를 넣을 때 깨지는 것*(리뷰 부하, 시니어 맥락, 주의력)을 인코딩한다. 같은 루프의 조직면: 실패를 규칙으로 ([[harness-engineering]] "every mistake becomes a rule") — 다만 규칙은 훅/테스트만이 아니라 **소통 예절과 로드맵 소유권**이기도 하다.

## References

- [[tech-bridge-figma-coding-agents]]
- [[eyal-blum]] · [[figma]]
