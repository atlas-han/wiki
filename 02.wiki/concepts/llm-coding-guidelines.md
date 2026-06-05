---
title: LLM Coding Guidelines (4원칙)
type: concept
category: pattern
tags: [llm-coding, claude-code, system-prompt, anti-pattern]
related: [surgical-edits, verifiable-goals, sprint-contract, ralph-wiggum-method, context-engineering]
first-seen: multica-karpathy-skills-claude-md
sources: [multica-karpathy-skills-claude-md]
created: 2026-05-25
updated: 2026-05-25
---

# LLM Coding Guidelines (4원칙)

LLM 코딩 어시스턴트의 흔한 실패 모드를 줄이기 위한 **CLAUDE.md 헤더용 행동 규약**. [[multica-karpathy-skills-claude-md]]가 4가지 원칙으로 정리. *"속도보다 신중함(caution > speed) 편향"* 을 명시적으로 인정 — trivial task에는 judgment 허용.

## 4원칙 요약

| # | 원칙 | 한 줄 정의 | 대응 anti-pattern |
|---|------|---------|-----------------|
| 1 | **Think Before Coding** | 가정을 표면화하고 불확실하면 멈춰서 질문 | hidden confusion, silent interpretation |
| 2 | **Simplicity First** | 요청된 최소 코드만, 미요청 기능 금지 | over-engineering, speculative abstraction |
| 3 | **Surgical Changes** ([[surgical-edits]]) | 손댈 곳만 손대고, 자기가 만든 mess만 청소 | scope creep, adjacent refactoring |
| 4 | **Goal-Driven Execution** ([[verifiable-goals]]) | 모호한 task → 검증 가능한 goal로 변환 | weak success criteria, infinite clarification |

## 1. Think Before Coding — 가정 표면화

> Don't assume. Don't hide confusion. Surface tradeoffs.

- 가정은 명시적으로 진술 (uncertain → ask)
- 다중 해석이 가능하면 **모두 제시**, 침묵 선택 금지
- 더 단순한 대안이 있으면 push back (warranted할 때)
- 불명확한 것은 **이름 지어** 질문 — *"X가 모호하다"*

→ [[sprint-contract]]의 사상과 유사 — 코드 *전*에 합의를 못 박는다.

## 2. Simplicity First — 최소주의

> Minimum code that solves the problem. Nothing speculative.

금지 목록:
- 요청 외 feature
- single-use 코드의 추상화
- 미요청 flexibility / configurability
- 발생 불가능한 시나리오의 error handling

자가 점검:
- *"200줄을 50줄로 줄일 수 있나?"* → yes면 다시 써라
- *"시니어가 overcomplicated라 할까?"* → yes면 단순화

## 3. Surgical Changes — 외과적 수정

[[surgical-edits]] 참조. 핵심 테스트:

> Every changed line should trace directly to the user's request.

- 인접 코드·주석·포맷 손대지 말 것
- 깨지지 않은 것 리팩토링 금지
- 기존 스타일 일치 (본인 취향과 달라도)
- 무관한 dead code는 **언급만**, 삭제 금지
- 단, **본인 변경으로 인해** 발생한 unused import/var/func는 정리

## 4. Goal-Driven Execution — 검증 가능한 목표

[[verifiable-goals]] 참조. Task → goal 변환 예시:

| 모호한 task | 검증 가능한 goal |
|-----------|----------------|
| "Add validation" | "Write tests for invalid inputs, then make them pass" |
| "Fix the bug" | "Write a test that reproduces it, then make it pass" |
| "Refactor X" | "Ensure tests pass before and after" |

멀티스텝은 `step → verify: check` 형식 plan으로:
```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

→ 강한 success criteria가 **independent loop**를 가능케 함. 약하면 매번 clarification 필요.

## 효과 측정 지표

가이드라인이 작동 중이라는 신호:
- diff 내 **불필요한 변경 감소**
- overcomplication으로 인한 **재작성 감소**
- 사후 수정보다 **사전 질문 비중 증가** ("after mistakes" → "before implementation")

## 위키 내 좌표

- [[llm-wiki-pattern]]이 *"LLM이 위키를 만들고 유지"* 하는 메타라면, 본 원칙은 *"LLM이 코드를 만들고 유지할 때의 메타"*
- [[anthropic-claude-code-auto-mode]]가 **권한 게이트**로 위험 행동을 차단한다면, 본 원칙은 **system prompt**로 *선의의 과잉 행동*(over-engineering, scope creep)을 줄임 — 보완 관계
- [[ralph-wiggum-method]] 같은 autonomous loop는 본 원칙의 *strong success criteria*가 없으면 발산 — 4번 원칙이 loop를 가능케 하는 전제

## 적용 메모 (옵션)

이 vault의 `CLAUDE.md` (LLM-WIKI 운영 규칙)는 본 4원칙과 **호환**되지만 직접 인용하지는 않음. 만일 도입한다면 §3 작업 정의와 함께 §0 일반 가이드라인으로 추가할 수 있음 (사용자 결정).

## References

- [[multica-karpathy-skills-claude-md]]
- 관련: [[surgical-edits]], [[verifiable-goals]]
