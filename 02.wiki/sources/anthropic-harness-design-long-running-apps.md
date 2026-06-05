---
title: "Anthropic — Harness design for long-running application development"
type: source
tags: [agent-harness, multi-agent, generator-evaluator, frontend-design, claude-agent-sdk]
source-url: https://www.anthropic.com/engineering/harness-design-long-running-apps
source-type: article
author: Prithvi Rajasekaran
date-published: 2026
ingested: 2026-05-25
created: 2026-05-25
updated: 2026-05-25
---

# Anthropic — Harness design for long-running application development

[[anthropic|Anthropic]] Labs의 Prithvi Rajasekaran이 두 가지 문제 — 고품질 frontend 디자인 생성과 자율 풀스택 앱 구축 — 을 동시에 풀기 위해 **GAN-스타일 generator + evaluator** 다중 에이전트 구조를 적용한 사례. [[claude-agent-sdk|Claude Agent SDK]] 위에서 [[playwright-mcp|Playwright MCP]]로 실제 페이지를 클릭하는 평가자가 핵심.

## 핵심 takeaways

1. **자기평가 문제**. Agent에게 자기 산출물을 평가시키면 거의 항상 후하게 점수를 매긴다. **외부 evaluator로 분리**하는 것이 두 자릿수의 lift를 준다. Evaluator도 LLM이라 처음엔 관대하지만, generator를 비판적으로 만드는 것보다 evaluator를 회의적으로 튜닝하는 게 훨씬 tractable.
2. **Frontend grading 4가지 기준** (생성기·평가기 양쪽 프롬프트에 동일하게 주입). 참고: [[generator-evaluator-pattern]]
   - **Design quality** — 색·타이포·레이아웃·이미지가 하나의 mood로 통합되는가
   - **Originality** — 커스텀 결정이 있는가; "purple gradients over white cards" 같은 AI 슬롭 명시적 페널티
   - **Craft** — 타이포 hierarchy, spacing, contrast 등 기술적 집행
   - **Functionality** — 미학과 무관한 사용성
   *"Design quality와 Originality를 craft·functionality보다 더 무겁게 weight했다."* — 디폴트의 평범함을 깨려고.
3. **평가자 caliberation**. Few-shot 예시 + 상세 점수 breakdown으로 평가자를 사용자 취향에 맞게 보정. *"museum quality"* 같은 prompt 표현이 평가 방향뿐 아니라 **생성 결과의 시각적 수렴 방향**까지 바꿈.
4. **Frontend 결과 — 창발적 도약 사례**. 네덜란드 미술관 사이트 prompt에서, 9번째 iteration까지는 깔끔한 다크 랜딩 페이지였으나 10번째에 갑자기 **CSS perspective로 3D 갤러리 룸**을 만들고 문 모양 navigation을 도입. *"a creative leap that I hadn't seen before from a single-pass generation."*
5. **풀스택용 three-agent 아키텍처**:
   - **Planner** — 1~4 문장 prompt를 풀 product spec으로 확장. AI 기능을 자연스레 weave하도록 지시. 디테일한 기술 구현은 의도적으로 비워둠 (틀리면 cascade error).
   - **Generator** — Sprint 단위로 구현 (React + Vite + FastAPI + SQLite/PostgreSQL). 각 스프린트 끝에 self-evaluation 후 QA로 넘김.
   - **Evaluator** — [[playwright-mcp|Playwright MCP]]로 UI·API·DB 상태를 사용자처럼 클릭/검증. 각 기준에 hard threshold; 하나라도 미달이면 sprint fail.
6. **Sprint contract**. 코드 작성 *전*에 generator와 evaluator가 "done의 정의"를 협상하고 파일에 기록. 높은 수준 spec과 testable 구현 사이의 다리. 예: 레트로 게임 메이커 Sprint 3은 단독으로 **27개 criteria**를 가짐. 참고: [[sprint-contract]]
7. **Solo vs Full harness 비교 (Opus 4.5 기준)**:

   | Harness | Duration | Cost |
   |---|---|---|
   | Solo | 20 min | $9 |
   | Full harness | 6 hr | **$200** (20×) |

   비용은 20배지만 solo run은 핵심 기능(엔티티가 입력에 반응)이 *작동하지 않았다*. Harness run은 16-feature spec / 10-sprint를 소화하고 실제 플레이 가능.
8. **Evaluator의 실 사례 — 구체적인 bug-finding** (블로그 표):
   - `fillRectangle` 함수는 있는데 mouseUp에서 trigger 안 됨
   - Delete key handler가 `selection && selectedEntityId`를 둘 다 요구; 엔티티 클릭은 후자만 set → 정확한 수정안 제시
   - FastAPI `/frames/reorder` 라우트가 `/{frame_id}` 뒤에 정의돼서 `"reorder"`를 int로 파싱 시도 → 422
9. **Harness simplification & Opus 4.6 effect**. [[claude-opus-4-6|Opus 4.6]] 출시 후 sprint construct와 [[context-resets-and-compaction|context resets]]을 제거할 수 있었다. *"Harness가 인코딩한 가정은 모델이 발전하면 dead weight가 된다."* DAW 실험에서는 builder가 sprint 없이 **2시간 7분 연속 코딩**을 견뎌냄. 참고: [[context-anxiety]]
10. **두 가지 lesson**:
    - 복잡한 task는 decompose + 전문화된 에이전트의 lift가 실재한다
    - 새 모델이 나오면 harness를 다시 뜯어보고, load-bearing 안 하는 부분을 떼어내라
11. **DAW (V2 harness) 결과**: 총 3시간 50분 / $124.70. Planner $0.46 → Build R1 $71 → QA R1 $3.24 → Build R2 $36.89 → QA R2 $3.09 → Build R3 $5.88 → QA R3 $4.06. QA가 라운드마다 실제 functionality gap을 잡아냄 (오디오 녹음이 stub뿐, clip resize 미구현 등).

## 핵심 인용

> Tuning a standalone evaluator to be skeptical turns out to be far more tractable than making a generator critical of its own work.

> The criteria explicitly penalized highly generic "AI slop" patterns, and by weighting design and originality more heavily it pushed the model toward more aesthetic risk-taking.

> Every component in a harness encodes an assumption about what the model can't do on its own, and those assumptions are worth stress testing.

> The space of interesting harness combinations doesn't shrink as models improve. Instead, it moves.

## 등장 개체·개념

- 조직: [[anthropic]] (Labs 팀)
- 저자: Prithvi Rajasekaran
- 모델: [[claude-opus-4-5]], [[claude-opus-4-6]], [[claude-sonnet-4-5]]
- 도구·SDK: [[claude-agent-sdk]], [[playwright-mcp]]
- 개념: [[agent-harness-design]], [[generator-evaluator-pattern]], [[sprint-contract]], [[context-anxiety]], [[context-resets-and-compaction]]

## References

- [원문](https://www.anthropic.com/engineering/harness-design-long-running-apps)
- 연관 글: [Building Effective Agents](https://www.anthropic.com/research/building-effective-agents), [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
- 시리즈: [[anthropic-claude-code-auto-mode]], [[anthropic-managed-agents]]
- 외부 참고: [Ralph Wiggum method (Geoff Huntley)](https://ghuntley.com/ralph/)
