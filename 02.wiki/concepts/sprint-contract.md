---
title: Sprint Contract
type: concept
category: pattern
tags: [agent, multi-agent, planning, verification]
related: [generator-evaluator-pattern, agent-harness-design, verifiable-goals]
first-seen: anthropic-harness-design-long-running-apps
sources: [anthropic-harness-design-long-running-apps]
created: 2026-05-25
updated: 2026-05-25
---

# Sprint Contract

다중 에이전트 코딩 harness에서 **각 sprint 시작 전에 generator와 evaluator가 합의하는 "done의 정의"**. 코드 작성 *전*에 검증 기준을 못 박아두는 인공물. [[anthropic-harness-design-long-running-apps]]에서 도입.

## 왜 필요한가

- Product spec은 의도적으로 high-level (planner가 구현 디테일을 박지 않음 — 틀리면 cascade error)
- User story → testable implementation 사이의 다리가 없음
- Generator가 자기 판단으로 "done"을 선언하면 [[generator-evaluator-pattern|self-evaluation bias]]에 빠짐

## 절차

1. **Generator가 제안**: "이 sprint에서 무엇을 빌드하고, 어떻게 verify할 것인가"
2. **Evaluator가 review**: "올바른 것을 빌드하려는가" 점검
3. **합의될 때까지 반복** (파일 기반 통신: 한 쪽이 쓰면 다른 쪽이 응답 파일을 작성)
4. Generator가 contract에 맞춰 빌드 → QA로 인계

## 규모 사례

레트로 게임 메이커 빌드 (Opus 4.5 풀 harness)에서 **Sprint 3 단독으로 27개 criteria**를 가짐. Evaluator의 fail 리포트는 코드 위치까지 구체:

| Contract criterion | Evaluator finding |
|---|---|
| Rectangle fill tool으로 영역 채우기 | `fillRectangle` 함수는 있는데 mouseUp에서 trigger 안 됨 |
| 배치된 entity spawn point 삭제 | Delete handler가 `selection && selectedEntityId` 둘 다 요구; 엔티티 클릭은 후자만 set |
| 애니메이션 프레임 reorder API | `PUT /frames/reorder`가 `/{frame_id}` 뒤에 정의 → `"reorder"`를 int 파싱 시도, 422 |

## Opus 4.6 이후의 변화

Sprint construct는 **work decomposition의 가정**을 인코딩 — "모델이 멀티-피처 일관성을 한 번에 못 유지한다". [[claude-opus-4-6]]에서는 이 가정이 약해져 sprint 자체가 dropped 가능. Evaluator만 single pass로 유지. DAW 빌드는 sprint 없이 2시간 7분 연속 코딩 후 QA 3 라운드.

→ [[agent-harness-design]]의 일반 원리: 컴포넌트는 stale될 가정의 인코딩이다.

## References

- [[anthropic-harness-design-long-running-apps]]
