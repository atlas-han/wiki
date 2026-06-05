---
description: Today I Learned 추가 (CLAUDE.md §3.5)
argument-hint: <오늘 배운 내용>
---

다음 내용을 TIL로 기록해줘: $ARGUMENTS

CLAUDE.md §3.5 워크플로:

1. 적절한 슬러그를 정해 `02.wiki/til/YYYY-MM-DD-<topic>.md` 생성 (오늘 날짜).
2. frontmatter:
   ```yaml
   ---
   title: <정식 제목>
   type: til
   date: YYYY-MM-DD
   tags: [...]
   related: [<연결 slug들>]
   sources: []
   created: YYYY-MM-DD
   updated: YYYY-MM-DD
   ---
   ```
3. 본문은 **짧게 (3~10줄)**. 길어지면 `02.wiki/concepts/` 또는 `02.wiki/engineering/`로 옮길 것을 제안.
4. 관련 개념/도구가 있으면 `[[링크]]`로 연결. 관련 페이지가 없으면 새로 만들 것인지 사용자에게 묻기.
5. `02.wiki/til/index.md`에 한 줄 추가: `- [[YYYY-MM-DD-topic]] — 한 줄 요약`
6. `02.wiki/log.md`에 append: `## [YYYY-MM-DD] til | <주제>`

카테고리(선택): language | tool | concept | system | workflow | other
