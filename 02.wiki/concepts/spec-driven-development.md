---
title: Spec-Driven Development
type: concept
category: pattern
tags: [spec, planning, agent, github, workflow]
related: [verifiable-goals, sprint-contract, harness-engineering, outcome-engineering, agent-org-adoption, model-context-protocol, frontier-engineering]
first-seen: tech-bridge-spec-driven-development
sources: [tech-bridge-spec-driven-development, tech-bridge-frontier-engineering, tech-bridge-ai-native-skills, tech-bridge-ai-native-sdlc]
created: 2026-08-29
updated: 2026-09-05
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

[[tech-bridge-ai-native-skills]]([[imad-touil]]): Specify→Plan→Tasks→Implement는 기업 SDLC에서 **product increment 한 칸**일 뿐. 앞뒤로 전략·디스커버리·데이터·플랫폼·런치가 깔린다. 스펙 파이프라인을 전사 "무엇이든 만드는 단일 워크플로"로 오해하지 말 것. 조직 know-how의 실행 단위는 [[agent-skills]].

## 위키 내 자매 개념

- [[verifiable-goals]] — spec의 acceptance는 verifier. 약한 spec("동작하게 해 줘")은 독립 루프가 안 된다.
- [[sprint-contract]] — generator/evaluator가 합의하는 "done의 정의". spec-driven은 그 계약을 **저장소 아티팩트**로 승격.
- [[outcome-engineering]] — how 프롬프팅 → 결과 정의. spec-driven은 그 결과를 마크다운 파이프라인으로 형식화.
- [[harness-engineering]] — Global Rules + Context Docs가 constitution/spec의 자리. Spec Kit는 그 층을 CLI·슬래시 커맨드로 제품화한 하니스.
- [[agent-org-adoption]] — Figma 쪽은 같은 원리를 *조직*에서 "프롬프팅 대신 기획"으로 서술.

## 체인이 앞뒤로 늘어난다 — AI-Native SDLC (2026-09-05 · [[tech-bridge-ai-native-sdlc]])

[[anthropic|Anthropic]]의 *AI-Native SDLC Playbook*은 spec을 **체인의 한 고리**로 재배치한다.

**앞** — spec 이전에 [[intent-md|`intent.md`]]가 붙는다. 에이전트가 사람을 **인터뷰**해서 만들고, 승인되면 **hook으로 `spec.md`가 자동 생성**된다. spec은 이제 사람이 쓰는 첫 문서가 아니라 **파생물**이다.

**뒤** — `spec.md` → `plan.md` → 빌드 → 테스트 → 배포 → 유지보수로 이어지고, 유지보수에서 Claude가 로그·티켓을 근거로 **스스로 intent를 만들어 1단계로 되돌린다.** 체인이 닫힌 고리가 된다.

### 왜 문서가 필요한가에 대한 새 근거

이 페이지의 기존 논거는 "명세가 있으면 산출물이 정확해진다"였다. 여기서는 다른 이유가 나오고, 더 강하다.

> **소프트웨어 개발 수명주기의 모든 단계를 한 에이전트가 모두 수행할 수는 없습니다. 컨텍스트 창이 나타날 것입니다.** (…) 담당자는 **이전 대화 내용을 이해하지 못한 채 처음부터 다시 시작**할 수 있습니다.

즉 아티팩트는 품질 장치이자 **에이전트 간 인계 프로토콜**이다. `plan.md`의 합격 기준도 여기서 나온다 — 받은 사람이 *"설계 의도나 사양 문서를 참조하지 않고도"* 구현할 수 있어야 한다.

### 추가되는 것

- **거버넌스** — 아티팩트마다 **버전과 수정자**를 남긴다. 목적은 DORA 지표 검증. ⚠️ *"제가 함께 일해 본 회사들은 **이 부분을 특히 어려워**합니다."*
- **Continuous evals** — 해결한 문제 20개와 예상 결과를 모아 두고 **새 모델·새 스킬마다** 돌려 퇴보를 본다.
- **결정론 층의 분리** — lint는 *"예 또는 아니오, 이분법적인 답변"* 이고, hook이 그 경계를 강제한다.

→ [[ai-native-sdlc]]

⚠️ 이 위키는 **원문서를 직접 ingest하지 않았다.** 위 내용은 [[switch-dimension]] 해설을 통한 것이고, 해설에 나온 *"두 배 더 빠릅니다"* 는 근거가 확인되지 않았다.

## References

- [[tech-bridge-spec-driven-development]]
- [[github-spec-kit]]
- 공식: <https://github.github.io/spec-kit/>
