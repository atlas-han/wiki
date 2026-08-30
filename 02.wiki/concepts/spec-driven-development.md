---
title: Spec-Driven Development
type: concept
category: pattern
tags: [spec, planning, agent, github, workflow]
related: [verifiable-goals, sprint-contract, harness-engineering, outcome-engineering, agent-org-adoption, model-context-protocol, frontier-engineering]
first-seen: tech-bridge-spec-driven-development
sources: [tech-bridge-spec-driven-development, tech-bridge-frontier-engineering]
created: 2026-08-29
updated: 2026-08-30
---

# Spec-Driven Development

코딩 에이전트에게 **일회성 프롬프트** 대신, 저장·리뷰·재실행 가능한 **명세(spec)를 메인 아티팩트**로 주는 개발 방법. *무엇을 만들지*를 먼저 고정하고, 계획이 그 명세를, 태스크가 그 계획을 구현한다. 출처: [[tech-bridge-spec-driven-development]] (GitHub [[github-spec-kit|Spec Kit]] 워크플로).

> 프롬프트는 세션과 함께 사라지고, 스펙은 저장소에 남아 같은 입력에서 같은 결과를 기대하게 한다.

## 4단계 코어 (영상 데모) + 공식 게이트

[[tech-bridge-spec-driven-development]] 데모가 도는 시작용 네 단계. 전체 목록은 아니다.

| 단계 | 질문 | 산출 (데모) |
|---|---|---|
| **Constitution** | 깨지지 않는 뿌리는? | `.specify/memory/constitution.md`. 프로젝트·팀보다 클 수 있음 |
| **Spec** | 무엇을·왜? (how 금지) | `specs/` 사용자 스토리. 모호하면 질문/표시 |
| **Plan** | 어떻게? | 같은 폴더에 스택·배포·버전. 버전을 안 적으면 모델이 채움 — 명시할 것 |
| **Task → Implement** | 어떤 순서로 집을까? | 페이즈·스토리 마크다운 → 코드+테스트 |

공식 문서는 그 위에 `/speckit.clarify` · `checklist` · `analyze` · `converge`를 둔다. 발표자도 implement 전에 analyze/clarify를 권하지만 바로 implement도 가능하다고 한다.

데모 constitution 예 (세션 플래너 MCP, 범용 아님): grounded only · time-aware · agent-safe · HTTP-safe · testable by design · privacy by default.

## 운영 규칙 (영상)

- 메인 아티팩트는 프롬프트가 아니라 스펙. 프롬프트는 사적·일시적·리뷰 불가.
- AI가 뱉은 constitution/spec/plan을 팀이 읽고 동의할 것.
- Spec Kit는 마법이 아니라 마크다운 + 스크립트 + 에이전트별 슬래시 커맨드.
- 워크플로 전체를 내일 바꾸지 말고, 작고 의미 있는 실제 기능 하나에 spec-first + 규칙 2–5개 + 전 문서 리뷰.

Amazon 현장([[tech-bridge-frontier-engineering]] 습관 4): 사내 spec-driven이 [[kiro|Kiro]]에 들어가 있어 채택이 자연스럽다. vibe coding은 높은 수준 프롬프트 후 "그게 아니야"로 코드를 고친다. **의도가 틀린 코드**를 왕복하는 것보다 스펙 문서를 왕복하는 편이 싸다. 모델이 스펙 초안을 써도 된다.

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
