---
title: "제품 완성도 패턴 — 에이전트가 묻지 않으면 안 하는 것 (Product Polish Patterns)"
type: concept
category: pattern
tags: [product-polish, ux-patterns, one-shot, autosave, optimistic-updates, undo, archiving, url-state, infinite-scroll, internal-tools, agents]
aliases: [polish patterns, 원샷 vs 다듬어진 소프트웨어, "agents don't do unless you ask", 제품 완성도 체크리스트]
related: [no-one-shot-design, ai-slop, design-system-as-agent-context, codebase-gardening, agent-verification-skill, action-reversibility, smarter-software-vs-cheaper-software, agent-skills, primitives-before-features]
first-seen: tech-bridge-railway-polished-internal-tools
sources: [tech-bridge-railway-polished-internal-tools, tech-bridge-ben-davis-codex-product-cohesion]
created: 2026-10-19
updated: 2026-10-31
---

# 제품 완성도 패턴 (Product Polish Patterns)

**원샷으로 돌아가는 소프트웨어와 매일 쓰고 싶은 소프트웨어를 가르는 상호작용 패턴들. 에이전트는 이것을 만들 수 있지만, 명시적으로 요청하지 않으면 넣지 않는다.** [[mahmoud-abdelwahab|Mahmoud Abdelwahab]](⚠️ 이름 추정, [[railway|Railway]])이 [[tech-bridge-railway-polished-internal-tools]]에서 사내 마케팅 도구를 만들며 정리했다.

> *"there's a gap, a big gap, between working software that got one-shotted and software I would actually use, software that sparks joy, that is polished, that feels good."* (00:16~00:25)
> *"there are kind of like a bunch of patterns that I found that Asians[=agents] don't typically do unless you explicitly ask them to."* (04:46~04:54)

## 왜 보이지 않는가

> *"When you use like a lot of SaaS products out there that you actually love that you use every day, when you're a user, there's like a lot of things you don't notice. But, when you actually try to like replicate an experience, you quickly find out how much care and thought goes into different flows."* (04:03~04:20)

폼을 제출하는 서버 렌더링 앱으로도 기능은 된다. 매일 쓸 것이라면 *"Oh, it shouldn't feel that way."*(04:43~04:45)

## 목록

| 패턴 | 요청할 것 | 단서 |
|---|---|---|
| 자동 저장 | 백그라운드, *"non-blocking"*(05:18~05:23) | 문서 편집기라면 *"table stakes"*(05:05~05:08) |
| 미저장 탭 닫기 방지 | *"prevent the browser tab from closing if there are unsaved changes"*(05:34~05:39) | 자동 저장과 함께 작업물을 잃지 않는 *"two layers"*(05:39~05:46) |
| 실시간 협업 | *"concurrent edits"*(05:53~05:55) | *"700 million tokens later"*(06:07) ⚠️ 유일한 수치 |
| 낙관적 업데이트 | 성공 상태를 먼저 보여 주고 백그라운드 동기화, 실패하면 롤백(06:25~06:43) | *"you shouldn't blindly have optimistic updates for everything"*(06:43~06:46). 에이전트에게 *"where it makes sense. Let's come up with a plan."*(07:08~07:11) |
| 삭제 취소 | UI에서 바로 지우고 몇 초 유예 후 실제 삭제(07:42~08:07) | 확인 대화상자가 에이전트의 기본값(07:34~07:40). *"a delayed action"*(08:14~08:16) |
| 보관/보관 해제 | 숨기려면 지워야 하는 상황을 없앤다(08:16~08:41) | |
| URL 상태 | 필터·정렬 조건을 URL에(08:46~09:11) | 동료에게 그대로 공유 |
| 무한 스크롤 | load more·다음 페이지 버튼 대신(09:13~09:28) | *"when you use something every day, I think it makes a huge difference"*(09:30~09:33) |

## 진단 — 능력이 아니라 요청

> *"it's not difficult for the agent to build it. You just need to ask and know exactly what to ask for."* (07:14~07:20)

실시간 협업도 *"my agent didn't struggle at all"*(05:56~05:58)이었다. 그러니 목록은 **에이전트에게 줄 체크리스트**다. 같은 화자는 이 요청을 반복하지 않으려고 두 장치를 더 쓴다. 좋은 페이지를 한 번 만들어 참고로 지정하고([[design-system-as-agent-context]]), 의견을 스킬로 포장한다([[agent-skills]]). 끝에는 실제로 써 보는 검증 루프를 둔다([[agent-verification-skill]]).

## 이 위키에서의 자리

- **[[ai-slop]]·[[no-one-shot-design]]의 상호작용 판본.** 위키의 슬롭 논의는 디자인(타이포·색·간격, [[design-system-as-agent-context]]·[[impeccable]])과 코드 품질([[codebase-gardening]]) 쪽이었다. 이 페이지는 **흐름**(저장·실패·취소·공유·탐색)을 다룬다. 원샷 결과에서 빠지는 것은 "결정의 부재"([[no-one-shot-design]])라는 진단과 같은 방향이다. 여기서 빠진 결정은 *실패하면 어떻게 되나, 실수하면 되돌릴 수 있나, 이 화면을 남에게 줄 수 있나*다.
- **[[action-reversibility]]**: 삭제 취소와 보관은 사용자의 행동을 two-way door로 만든다. 그 페이지는 에이전트의 행동을 다뤘다. 여기서는 에이전트가 만든 **제품의 사용자** 행동이다.
- **[[smarter-software-vs-cheaper-software]]와의 긴장(위키 판독)**: 목록은 기존 SaaS가 이미 갖춘 UX를 다시 만드는 것이다. 만드는 사람은 바뀌어도 소프트웨어의 성질은 같다는 Almeida의 관찰과 맞닿는다.

## ⚠️ 유보

- 한 사람의 경험 목록이다. 어떤 에이전트·모델·시점에서 관찰했는지 발화되지 않는다. 패턴별 효과 측정은 없다.
- 화자도 면책을 먼저 둔다: *"anything I say might change completely in like the span of months"*(02:07~02:13).

## References

- [[tech-bridge-railway-polished-internal-tools]] — first-seen
- [[mahmoud-abdelwahab]] · [[railway]]
- 관련: [[no-one-shot-design]] · [[ai-slop]] · [[design-system-as-agent-context]] · [[codebase-gardening]] · [[agent-verification-skill]] · [[action-reversibility]] · [[smarter-software-vs-cheaper-software]]

## 화면 안이 아니라 기능 사이 — 사용자가 본 rough edges (2026-10-31 · [[tech-bridge-ben-davis-codex-product-cohesion]])

[[ben-davis|Ben Davis]](추정)의 Codex Spaces 평: *"basically notion with a bunch of AI stuff built into it with a lot of rough edges around it."*(03:14~03:18) 예로 든 것은 이 페이지 목록(autosave · undo · URL state …)에 없는 종류다 — 모델이 page를 고칠 때 *"it will force your view, your entire computer back onto that page"*(03:25~03:29), 같은 thread가 두 곳에 보임. 즉 **개별 화면의 완성도가 아니라 기능 사이의 일관성**이고, 화자의 진단은 같은 방향이다: 모델은 *"not going to do it in the best possible way, and a lot of weird edges are going to naturally start to form"*(04:42~04:47). → [[primitives-before-features]]
