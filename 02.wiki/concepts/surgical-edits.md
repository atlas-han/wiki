---
title: Surgical Edits
type: concept
category: pattern
tags: [llm-coding, code-review, minimal-diff, scope]
related: [llm-coding-guidelines, verifiable-goals]
first-seen: multica-karpathy-skills-claude-md
sources: [multica-karpathy-skills-claude-md]
created: 2026-05-25
updated: 2026-05-25
---

# Surgical Edits

LLM 코딩 어시스턴트가 코드를 **수정할 때** 적용하는 외과 수술적 변경 원칙. *"Touch only what you must. Clean up only your own mess."* [[multica-karpathy-skills-claude-md]]의 4원칙 중 3번 (Surgical Changes)을 별도 concept으로 추출.

## 핵심 테스트

> Every changed line should trace directly to the user's request.

변경된 모든 라인이 user request로 직선 traceable한가? No이면 그 라인은 빠져야 한다.

## 금지 (Do not)

기존 코드 수정 시:
- 인접 코드·주석·포맷 "개선"하지 말 것
- 깨지지 않은 것 리팩토링 금지
- 기존 스타일과 다르게 쓰지 말 것 (본인 취향이 더 좋아도)
- 무관한 dead code는 **언급만**, 삭제 금지

## 허용 (Do)

본인이 만든 mess 정리:
- **본인 변경으로 인해** 사용되지 않게 된 import 제거
- 본인 변경으로 unused가 된 변수·함수 제거
- 즉, *변경의 결과로 발생한 orphan*은 cleanup 책임

## 안티 패턴

| Anti-pattern | 증상 | 위반 |
|--------------|------|------|
| **Adjacent refactoring** | "옆 코드도 같이 깨끗하게" | scope creep |
| **Style hijacking** | 기존 코드를 본인 선호 스타일로 변환 | match-existing 위반 |
| **Speculative cleanup** | "이거 이상한데 같이 고쳤어요" | 기존 dead code 삭제 |
| **Comment thrashing** | 작동하는 주석을 본인 스타일로 재작성 | adjacent 손댐 |

## 왜 중요한가

- LLM은 *"개선" 강박*을 갖기 쉬움 — diff가 부풀고 review 비용↑
- 인접 변경은 별도 PR로 분리해야 reviewability 유지
- 무관한 변경이 섞이면 **본 작업의 실패가 cascade** — bisect·rollback 비용↑
- "이거 같이 고쳤어요"는 user가 요청하지 않은 작업 — judgment 영역을 침범

## [[verifiable-goals]]와의 관계

[[verifiable-goals|검증 가능한 목표]]가 작업의 **what**을 못 박는다면, surgical-edits는 **what 외에는 손대지 말 것**을 못 박는다. 같이 묶이면 *"goal을 달성하는 최소 diff"* 라는 단일 원칙이 된다.

## 위키 내 사례

- [[claude-code]]의 internal incident에서 *"오해된 지시로 원격 브랜치 삭제"* 같은 사고는 surgical 원칙의 부재가 빚어낸 형태 — over-active cleanup
- [[sprint-contract]]의 evaluator는 generator의 diff가 contract 외 변경을 포함했는지 점검할 수 있는 자연스러운 자리

## References

- [[multica-karpathy-skills-claude-md]]
- 관련: [[llm-coding-guidelines]] (상위 hub), [[verifiable-goals]]
