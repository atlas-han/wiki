---
description: wiki/ 건강 점검 — 모순·고아·누락·frontmatter 불일치 (CLAUDE.md §3.3)
---

LLM-WIKI 건강 점검을 진행해줘. CLAUDE.md §3.3의 점검 항목을 모두 검사:

1. **모순(Contradictions)**: `02.wiki/` 페이지 간 충돌 내용 (특히 같은 entity/concept를 다루는 페이지들)
2. **고아 페이지(Orphans)**: 어디서도 `[[링크]]`되지 않은 페이지
3. **누락 개체**: 본문에서 자주 언급되지만 페이지가 없는 entity/concept
4. **frontmatter 불일치**:
   - `updated` 필드가 최근 수정과 안 맞는 경우
   - 필수 필드(title, type, tags, created, updated) 누락
   - type별 추가 필드(category, status 등) 누락
5. **Reading 상태 불일치**:
   - `status: completed`인데 `finished` 없음
   - `status: reading`인데 `started` 없음
   - `status: completed`인데 `rating` 없음
6. **index.md 동기화**: 실제 페이지와 `02.wiki/index.md` 항목 일치 여부
7. **파일명 컨벤션**: kebab-case 위반, TIL은 `YYYY-MM-DD-topic.md` 형식

결과를 `02.wiki/lint-report-YYYY-MM-DD.md`에 임시 작성. 항목별로:
- 발견된 이슈 목록
- 자동 수정 가능한 것 / 사람 판단 필요한 것 구분
- 사용자에게 어떤 것부터 처리할지 묻기

자동 수정 동의를 받은 항목은 처리하고, 완료되면 lint-report 파일 삭제.
`02.wiki/log.md`에 `## [YYYY-MM-DD] lint | <요약>` append.
