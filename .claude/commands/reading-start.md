---
description: 책/논문 읽기 시작 — status를 reading으로 (CLAUDE.md §3.4)
argument-hint: <책 슬러그 또는 제목>
---

다음 reading 노트를 "읽기 시작" 상태로 변경: $ARGUMENTS

CLAUDE.md §3.4 워크플로:

1. `02.wiki/reading/books/` 또는 `02.wiki/reading/papers/` 에서 해당 노트 찾기. 모호하면 후보를 보여주고 확인.
2. frontmatter 수정:
   - `status: reading`
   - `started: YYYY-MM-DD` (오늘)
   - `updated: YYYY-MM-DD`
3. `02.wiki/reading/index.md`에서 항목을 **To Read** 섹션 → **In Progress** 섹션으로 이동.
4. `02.wiki/log.md`에 append: `## [YYYY-MM-DD] reading | start | <제목>`
