---
title: LLM Coding Guidelines (4원칙)
type: concept
category: pattern
tags: [llm-coding, claude-code, system-prompt, anti-pattern]
related: [surgical-edits, verifiable-goals, sprint-contract, ralph-wiggum-method, context-engineering, harness-engineering, claude-code]
first-seen: multica-karpathy-skills-claude-md
sources: [multica-karpathy-skills-claude-md, charlychoi-claude-code-best-practices, tech-bridge-six-agent-skills]
created: 2026-05-25
updated: 2026-09-05
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

## 규칙을 어디에 둘 것인가

[[charlychoi-claude-code-best-practices]]의 실무 구분은 긴 `CLAUDE.md`에 모든 것을 넣는 anti-pattern을 피하게 한다.

| Rule 성격 | 위치 |
|---|---|
| 모든 session에 필요한 project-specific 규칙 | 짧은 `CLAUDE.md` |
| 특정 반복 업무·domain convention | Skills |
| 반드시 실행되어야 하는 lint·test·secret/protected-path guard | Hooks |
| GitHub·cloud·monitoring·design system 연결 | CLI / MCP |

판단 질문은 **“이 줄을 지우면 agent가 실제로 더 자주 실수하는가?”**다. 아니라면 global context에서 제거하고, 강제해야 한다면 자연어 지침보다 결정론적 Hook으로 승격한다. 이는 [[harness-engineering]]의 AI Layer를 context cost와 enforcement strength로 배치하는 방식이다.

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

## 두 번째 소스의 독립 재발견 (2026-09-05 · [[tech-bridge-six-agent-skills]])

[[ai-labs]]가 같은 repo(`multica-ai/andrej-karpathy-skills`)를 소개하며 네 규칙을 그대로 제시했다. **이 위키에서 서로 다른 소스 두 개가 같은 아티팩트에 도달한 첫 사례**다([[multica-karpathy-skills-claude-md]]는 2026-05-25 ingest).

| 영상의 규칙 | 이 페이지의 이름 |
|---|---|
| 불명확할 때 추측 금지 → 가정 밝히고 선택지 보여주고 **방향을 바꿀 결정 전에 질문** | Think Before Coding |
| *"아직 발생하지 않은 문제를 해결하기 위해"* 기능·설정·시스템을 더하지 않기 | Simplicity First |
| **자기가 만든 문제만** 정리하고 다른 문제는 **고치지 말고 알리기** | [[surgical-edits]] |
| 시작 전에 결과와 **확인 방법**을 정하고 **모든 검사가 통과될 때까지** | [[verifiable-goals]] |

문제 진단의 표현이 특히 좋다.

> **문제의 대부분은 코드 자체에서 발생하지 않습니다. 에이전트가 사용자가 요청하지 않은 결정을 내린 결과입니다.**

### 새로운 것 — 계층적 CLAUDE.md 상속

위 "규칙을 어디에 둘 것인가" 절에 실제 배포 사례가 하나 추가된다. **스킬로 설치하지 않는다.**

> 저희는 맥에서 모든 코딩 프로젝트를 **하나의 개발자 폴더** 안에 보관합니다. (…) 네 가지 규칙을 폴더의 **최상위 `CLAUDE.md`에 복사**합니다.

작동 원리는 [[claude-code]]의 파일 탐색 규칙이다 — *"프로젝트 내의 `CLAUDE.md`와 **그 상위 폴더에 있는 모든 `CLAUDE.md`를 읽습니다.**"*

**요점은 범위 제어다.**

| 배치 | 문제 |
|---|---|
| 전역 `~/.claude` | 무관한 세션까지 오염 |
| 프로젝트마다 복사 | 갱신이 흩어짐 |
| **개발자 폴더의 `CLAUDE.md`** | **한 곳에서 관리 + 그 폴더 밖에는 무영향** |

소스가 이 의도를 명시한다 — *"컴퓨터의 **다른 부분에서 실행되는 관련 없는 세션에는 해당 규칙이 적용되지 않습니다.**"*

## References

- [[multica-karpathy-skills-claude-md]]
- [[charlychoi-claude-code-best-practices]]
- 관련: [[surgical-edits]], [[verifiable-goals]]
