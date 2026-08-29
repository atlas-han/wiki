---
title: Spec-Driven Development
type: concept
category: pattern
tags: [spec, planning, agent, github, workflow]
related: [verifiable-goals, sprint-contract, harness-engineering, outcome-engineering, agent-org-adoption, model-context-protocol]
first-seen: tech-bridge-spec-driven-development
sources: [tech-bridge-spec-driven-development]
created: 2026-08-29
updated: 2026-08-29
---

# Spec-Driven Development

코딩 에이전트에게 **일회성 프롬프트** 대신, 저장·리뷰·재실행 가능한 **명세(spec)를 메인 아티팩트**로 주는 개발 방법. *무엇을 만들지*를 먼저 고정하고, 계획이 그 명세를, 태스크가 그 계획을 구현한다. 출처: [[tech-bridge-spec-driven-development]] (GitHub [[github-spec-kit|Spec Kit]] 워크플로).

> 프롬프트는 세션과 함께 사라지고, 스펙은 저장소에 남아 같은 입력에서 같은 결과를 기대하게 한다.

## 4단계 (Spec Kit 코어)

채널 설명이 적는 코어와 공식 문서가 일치하는 부분만:

| 단계 | 질문 | 산출 |
|---|---|---|
| **Constitution** | 비협상 원칙은? | `constitution.md` — 이후 모든 산출물이 이 원칙에 대해 평가됨 |
| **Spec** | 무엇을·왜? (스택 금지) | 사용자 대면 행동·목표 |
| **Plan** | 어떻게? | 프레임워크·인프라·제약, constitution 준수 여부 |
| **Task** | 에이전트가 집는 단위는? | 위상별 작업 목록 |

공식 문서는 이 위에 clarify / checklist / analyze / implement / converge를 품질 게이트로 얹을 수 있다고 한다. 영상 자막이 없어 채널이 어느 경로(짧은 경로 vs 전체 경로)를 데모했는지는 미기록.

## 위키 내 자매 개념

- [[verifiable-goals]] — spec의 acceptance는 verifier. 약한 spec("동작하게 해 줘")은 독립 루프가 안 된다.
- [[sprint-contract]] — generator/evaluator가 합의하는 "done의 정의". spec-driven은 그 계약을 **저장소 아티팩트**로 승격.
- [[outcome-engineering]] — how 프롬프팅 → 결과 정의. spec-driven은 그 결과를 마크다운 파이프라인으로 형식화.
- [[harness-engineering]] — Global Rules + Context Docs가 constitution/spec의 자리. Spec Kit는 그 층을 CLI·슬래시 커맨드로 제품화한 하니스.
- [[agent-org-adoption]] — Figma 쪽은 같은 원리를 *조직*에서 "프롬프팅 대신 기획"으로 서술.

## References

- [[tech-bridge-spec-driven-development]]
- [[github-spec-kit]]
- 공식: <https://github.github.io/spec-kit/>
