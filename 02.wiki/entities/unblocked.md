---
title: Unblocked
type: entity
category: org
tags: [context-engine, developer-tools, code-review, retrieval, vendor]
links:
  - "https://getunblocked.com"
  - "https://github.com/unblocked/document-query-engine"
  - "https://x.com/get_unblocked"
sources: [tech-bridge-unblocked-context-engine-structured-queries]
created: 2026-10-16
updated: 2026-10-16
---

# Unblocked

**[[context-engine|컨텍스트 엔진]]을 만드는 회사** — *"at Unblocked, we build a context engine."*(00:09~00:12). 이 위키의 유일한 소스는 [[tech-bridge-unblocked-context-engine-structured-queries]]([[peter-werry|Peter]] 발표).

> ⚠️ **당사자 진술.** 아래 기능·효과는 전부 자사 데모이고 독립 측정이 없다. 링크는 Tech Bridge 설명란에서 왔다(열어 보지 않았다).

## 위키에서 알려진 것

- **context engine** — 에이전트(데모에선 Claude)가 호출하면 *"a very comprehensive but task-specific context bundle"*(03:00~03:04)을 돌려준다. 묶음 재료: 소스 코드 · Notion 문서 · pull request · Slack 대화(03:08~03:18). 화자가 꼽는 성질: interrelated · intent-specific · personalized · permissions-aware(01:39~01:48).
- **비용 주장** — 세션 1건에서 $1.29·약 1분 30초 vs 엔진 없이 *"up to (…) 260 and 3 minutes"*, *"a 50% reduction in cost"*(03:43~03:59). ⚠️ "260" 단위 미발화, 반복 횟수 미발화.
- **code review 제품** — *"We also have a code review product"*(04:17~04:20). 모델 전환 뒤 검출 이슈 수가 줄었고, 엔진이 원인을 *"a likely cause"* 로 좁혀 수정 PR을 만들었다는 일화(04:23~05:26). ⚠️ 모델 버전은 en-orig 판독 불가.
- **identity resolution** — fuzzy matching + LLM tiebreaker가 *"more or less how we do it uh in underneath the hood at Unblocks"*(12:01~12:05) — 제품 내부에 대한 유일한 직접 진술.
- **오픈소스 둘** — ① *document query engine*(09:29~09:31, 설명란 `github.com/unblocked/document-query-engine`): NL → 검증된 문서 DB 쿼리, 단계별 데모 → [[nl-to-structured-query-scaffolding]]. ② **context engine simulator**(18:08~18:43, 이름·URL 미발화): Unblocked 없이 로컬에서 과제별 context bundle을 만들어 같은 과제를 A/B 테스트.

## References

- [[tech-bridge-unblocked-context-engine-structured-queries]] · [[peter-werry]] · [[context-engine]] · [[nl-to-structured-query-scaffolding]]
