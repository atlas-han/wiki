---
description: 책/논문 완독 처리 + 핵심 인사이트 정리 (CLAUDE.md §3.4)
argument-hint: <책 슬러그 또는 제목> [rating 1-5]
---

다음 reading 노트를 완독 처리: $ARGUMENTS

CLAUDE.md §3.4 워크플로:

1. 해당 reading 노트 찾기. 모호하면 후보 확인.
2. frontmatter 수정:
   - `status: completed`
   - `finished: YYYY-MM-DD` (오늘)
   - `rating: <1-5>` (인자에 있으면 사용, 없으면 사용자에게 묻기)
   - `updated: YYYY-MM-DD`
3. 본문에 정리:
   - 핵심 인사이트 3~5개
   - 인상 깊은 인용 (원어 그대로)
   - 영향받은 생각 / 바뀐 관점
   - 후속 행동 항목이 있다면 별도 섹션
4. 관련 `02.wiki/concepts/` 또는 `02.wiki/engineering/` 페이지에 반영:
   - 책에서 배운 내용을 해당 페이지에 추가
   - 새로 다룰 만한 개념이면 신규 페이지 제안
5. `02.wiki/reading/index.md`에서 **In Progress** → **Completed** 섹션으로 이동.
6. 충분히 중요하면 `01.raw/books/`에 원문 저장 후 `/ingest`로 흡수할지 사용자에게 제안.
7. `02.wiki/log.md`에 append: `## [YYYY-MM-DD] reading | done | <제목> (rating: N)`

**DNF 처리**: 만약 사용자가 "중단"을 원하면 `status: dnf`, 본문 마지막에 중단 이유 한 줄 기록.
