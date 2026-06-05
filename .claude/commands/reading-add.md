---
description: 책/논문을 to-read 목록에 추가 (CLAUDE.md §3.4)
argument-hint: <책 또는 논문 제목 + 저자/URL 등>
---

다음을 reading to-read에 추가해줘: $ARGUMENTS

CLAUDE.md §3.4 워크플로:

1. 책이면 `02.wiki/reading/books/<slug>.md`, 논문이면 `02.wiki/reading/papers/<slug>.md` 생성.
2. frontmatter:
   ```yaml
   ---
   title: <정식 제목>
   type: reading
   category: book | paper | article | course
   status: to-read
   author: <저자>
   year: YYYY
   started:
   finished:
   rating:
   tags: [...]
   sources: []  # 01.raw/에 원문이 있으면 source-slug 연결
   created: YYYY-MM-DD
   updated: YYYY-MM-DD
   ---
   ```
3. 본문에 책 소개·읽으려는 동기 한두 줄.
4. `02.wiki/reading/index.md`의 **To Read** 섹션에 `- [[<slug>]] — 저자 (YYYY)` 추가.
5. 관련 topics가 있으면 `02.wiki/concepts/` 또는 `02.wiki/engineering/` 페이지와 cross-link.
6. `02.wiki/log.md`에 append: `## [YYYY-MM-DD] reading | add to-read | <제목>`
