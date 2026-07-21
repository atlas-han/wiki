---
title: Verifiable Goals
type: concept
category: pattern
tags: [llm-coding, planning, verification, success-criteria]
related: [llm-coding-guidelines, surgical-edits, sprint-contract, ralph-wiggum-method, generator-evaluator-pattern, outcome-engineering, claude-code]
first-seen: multica-karpathy-skills-claude-md
sources: [multica-karpathy-skills-claude-md, charlychoi-claude-code-best-practices]
created: 2026-05-25
updated: 2026-07-21
---

# Verifiable Goals

모호한 task를 **검증 가능한 목표(verifiable goal)** 로 변환하는 LLM 코딩 원칙. *"Define success criteria. Loop until verified."* [[multica-karpathy-skills-claude-md]]의 4원칙 중 4번 (Goal-Driven Execution)을 별도 concept으로 추출.

## 핵심 명제

> Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.

강한 성공 기준이 있으면 LLM이 **independent loop**로 작업 가능. 약하면 매 단계마다 사람의 clarification이 필요 — 사실상 loop가 안 된다.

## 변환 예시

| 모호한 task | 검증 가능한 goal |
|-----------|----------------|
| "Add validation" | "Write tests for invalid inputs, then make them pass" |
| "Fix the bug" | "Write a test that reproduces it, then make it pass" |
| "Refactor X" | "Ensure tests pass before and after" |

공통 패턴: **(1) verifier를 먼저 만들고 (2) verifier를 통과시키는 코드를 작성**. 테스트 = goal의 인코딩.

## Task별 verifier 선택

[[charlychoi-claude-code-best-practices]]는 verifier를 단위 테스트보다 넓게 실무 task별로 매핑한다.

| Task | Verifier |
|---|---|
| 함수·API | unit/integration test, status code, sample response |
| UI | desktop/mobile screenshot, clickability, console error 없음 |
| Build·type issue | 실제 build·typecheck command 성공 |
| Refactoring | 변경 전후 regression test 통과 |
| 문서 | 필수 section·실제 command·link 유효성 |
| 데이터 처리 | 고정 input/output 비교 |

즉 goal은 “무엇을 만들 것인가”만이 아니라 **어떤 외부 evidence가 통과하면 멈출 것인가**까지 포함해야 한다.

## 멀티스텝 plan 형식

```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

각 step에 verify가 붙어야 — verify가 없는 step은 *작업의 정의가 빠진 step*.

## 위키 내 자매 개념

- [[sprint-contract]] — 다중 에이전트 코딩에서 generator·evaluator가 **sprint 시작 전** 합의하는 "done의 정의". 본 원칙의 multi-agent 변형.
- [[generator-evaluator-pattern]] — 검증을 별도 agent로 분리. verifiable goal을 evaluator가 들고 있는 형태.
- [[ralph-wiggum-method]] — `while :; do cat PROMPT.md | claude-code ; done` 무한 루프. PROMPT.md 안에 verifiable goal이 있어야 발산하지 않음.
- [[outcome-engineering]] — Nextdoor/Codex 사례의 조직 관점 framing. *"원하는 결과를 정의한다"*가 곧 verifier(테스트·스크린샷·성능 기준)를 먼저 정의하는 것 — 같은 원리의 외부(비-Anthropic) 서술.

## 왜 작동하는가

LLM은 **자기 평가 편향**(self-evaluation bias)이 있어 *"되었다"* 를 쉽게 선언함 ([[generator-evaluator-pattern]] 참조). 외부에서 통과 가능한 verifier가 있으면:

1. *"되었다"* 선언이 객관적 통과로 대체됨
2. 실패 시 구체적 fail signal → 재시도 방향이 정해짐
3. 사람의 clarification 없이도 loop 가능

## 약한 vs 강한 criteria

| | 약한 | 강한 |
|---|------|------|
| 예 | "make it work", "looks good" | 테스트 통과, schema validation, CI green |
| 의존성 | 사람의 매 단계 승인 | independent loop 가능 |
| 실패 처리 | 모호 → 재질문 | 구체 fail → 다음 시도 |

## [[surgical-edits]]와의 관계

[[surgical-edits|surgical-edits]]가 *what 외에는 손대지 말 것*을 못 박는다면, verifiable-goals는 *what이 달성되었는지*를 못 박는다. 두 원칙이 묶이면 **"검증 가능한 최소 변경"** 이라는 단일 작업 단위가 정의된다.

## References

- [[multica-karpathy-skills-claude-md]]
- [[charlychoi-claude-code-best-practices]]
- 관련: [[llm-coding-guidelines]] (상위 hub), [[surgical-edits]], [[sprint-contract]], [[ralph-wiggum-method]]
