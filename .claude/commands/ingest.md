---
description: raw/ 신규 소스를 wiki로 흡수 (CLAUDE.md §3.1)
argument-hint: <소스 파일 경로 또는 URL>
---

다음 소스를 LLM-WIKI에 ingest 해줘: $ARGUMENTS

CLAUDE.md §3.1 워크플로를 정확히 따라:

1. 소스 정독 (이미지 포함). raw/는 절대 수정 금지.
2. 핵심 takeaway 3~5개를 먼저 사용자에게 제시하고, **강조점·관점을 협의한 후** 진행.
3. `02.wiki/sources/<slug>.md` 생성 — frontmatter `type: source`, source-url/type, ingested 날짜 포함. 요약·핵심 인용·등장 개체 목록.
4. 관련 `02.wiki/entities/` 페이지 갱신 또는 신규 생성 (person/org/model/product/tool).
5. 관련 `02.wiki/concepts/` 또는 `02.wiki/engineering/` 페이지 갱신 또는 신규 생성.
6. 책·논문이면 `02.wiki/reading/books/` 또는 `02.wiki/reading/papers/`와 cross-link.
7. `02.wiki/overview.md`에 한 줄 추가.
8. `02.wiki/index.md` 카테고리별 섹션 갱신.
9. `02.wiki/log.md`에 append: `## [YYYY-MM-DD] ingest | <소스 제목>`

규칙:
- 파일명은 kebab-case
- frontmatter `created`/`updated` 정확히
- `[[교차링크]]` 적극 사용
- 모순 발견시 `> ⚠️ Contradiction: ...` 표시
- 한국어 우선, 기술 용어 영어 병기
- 한 소스가 보통 10~15개 페이지를 건드림 — 빠뜨리지 말 것
