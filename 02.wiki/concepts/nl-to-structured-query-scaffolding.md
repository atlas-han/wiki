---
title: "자연어 → 구조화 쿼리 스캐폴딩 (NL-to-Structured-Query Scaffolding)"
type: concept
category: pattern
tags: [structured-retrieval, nl-to-query, text-to-sql, schema-discovery, enum-inference, identity-resolution, query-validation, tenant-isolation, self-correction, retry-loop, full-text-search, deterministic-first]
aliases: [document query engine, structured retrieval, NL to query, text-to-query scaffolding, 구조화 검색]
related: [context-engine, retrieval-augmented-generation, reference-graph-vs-vector-search, build-time-vs-runtime-tools, bound-parameters, credential-injection-outside-sandbox, secure-tool-evolution, deterministic-agent-pipeline, retrieval-primitive-repertoire, company-brain, reward-hacking]
first-seen: tech-bridge-unblocked-context-engine-structured-queries
sources: [tech-bridge-unblocked-context-engine-structured-queries]
created: 2026-10-16
updated: 2026-10-16
---

# 자연어 → 구조화 쿼리 스캐폴딩

**"지난주 내가 머지한 PR" 같은 구조적 질문은 시맨틱 검색이 아니라 쿼리다. LLM에게 쿼리를 만들게 하는 것은 쉽고, 어려운 것은 그 주변 — 스키마를 알려 주고, 사람 이름을 시스템 계정으로 풀고, 생성된 쿼리를 신뢰하지 않고 검증하고, 실패를 되먹여 고치게 하는 스캐폴딩이다.** [[peter-werry|Peter]]([[unblocked|Unblocked]])가 [[tech-bridge-unblocked-context-engine-structured-queries]]에서 오픈소스 *document query engine* 을 단계별로 켜 보이며 제시했다.

> *"generating the queries is actually the easy part. The hard part is the scaffolding that sits around it."* (08:00~08:06)

## 왜 필요한가 — RAG의 다른 절반

*"RAG nails the content part"*(06:25) — *"Find the code, the PR that changed it, the Slack thread"*. 그러나 *"PRs that I merged last week. Who reviewed payments the most, open PRs"* 는 *"queries. They're not semantic searches."*(06:48~07:03) 주간 비율 차트 같은 질문은 *"it's not going to be able to just pull this information from a vector store cuz that's not where that information's encoded."*(07:24~07:30)

## 여섯 단계 (데모 순서)

| # | 단계 | 내용 (en-orig) | LLM의 역할 |
|---|---|---|---|
| 1 | 자동 스키마 탐색 | 문서 샘플링 → 스키마 도출, enum 추론, 인덱스 정보(10:26~11:41) | **없음** — *"you get uh really, really far just using traditional procedural methods"* |
| 2 | identity resolution | *"open PRs by Rasheen"* → GitHub 계정. fuzzy matching(12:12~12:13) | **tiebreaker만**(12:15~12:18) |
| 3 | synthesis | 스키마 + 현재 날짜·시각 + 질문자 정보 → LLM(12:34~12:56). *"the easiest part"* | 쿼리 생성 |
| 4 | ⭐ validation | *"the most important thing"*(13:29). 위험 연산자(raw JavaScript를 DB 서버에서 실행하는 function operator), hidden fields, **tenant ID는 LLM이 아예 다루지 않게 하고 뒤에서 주입**(13:32~14:12). 데모: 정규식 금지 | 없음(결정론 게이트) |
| 5 | retry | 오류를 LLM에 되먹여 self-correct, *"just a loop with some sort of maximum, uh, retry"*(15:05~15:20) | 교정 |
| 6 | full-text search | retry가 exact title match로 수렴해 결과 0 → 프리미티브 추가(15:59~16:13) | — |

## 원칙 둘

1. **결정론 우선.** *"don't always fall back to an LLM to do this kind of what looks like non-deterministic work. This is actually quite deterministic"*(10:58~11:06). LLM은 synthesis와 동점 처리에만 → [[deterministic-agent-pipeline]].
2. **LLM 출력은 untrusted.** *"when you get the query out of the LLM, it's untrusted. It could have operations that are dangerous. It could cross tenant boundaries."*(08:30~08:40) 격리는 프롬프트가 아니라 **실행 직전의 쿼리 재작성**에서 → [[bound-parameters]] · [[credential-injection-outside-sandbox]]의 넷째 자리.

## ⭐ 관찰 — 검증을 통과한 쿼리가 의도를 놓친다

정규식이 막히자 재시도 루프는 *"it got there in the end. However, um, it constrained it down to use match, and unfortunately, this is an exact title match. We don't have any PRs with that exact title."*(15:56~16:07) — **검증기는 통과, 답은 빔.** 처방은 검증을 풀지 않고 맞는 프리미티브(full-text search)를 주는 것 → [[retrieval-primitive-repertoire]]. ⚠️ "통과 ≠ 의도" 일반화는 위키의 정리(화자는 일반화하지 않음) — [[tech-bridge-sentry-stop-prompting-codify-linters|Pstrucha]]의 lint whack-a-mole과 나란히 놓을 자리 → [[reward-hacking]].

## ⚠️ Contradiction — [[build-time-vs-runtime-tools]]

Google Cloud Toolbox 팀은 NL→SQL을 **빌드타임 전용**(사람 루프 필수, 프로덕션 불가)으로 두고 런타임엔 미리 정의한 결정론적 쿼리를 쓰라 했다. 이 패턴은 NL → 쿼리를 **사용자 앞의 chat agent**(17:18~17:19)에 두고 위험을 **검증 + 주입**으로 막는다. 위키의 독해: Google 사례는 쓰기·삭제가 가능한 도구였고 여기는 조회만 다룬다 — 다만 **읽기 전용 제한은 발화되지 않는다.** 그 페이지의 미해결(*읽기 전용 프로덕션 탐색은 어느 쪽인가*)에 대한 벤더 한 곳의 실천 답이다.

## ⚠️ 미해결

- 검증 규칙 전체 목록·읽기 전용 여부·재시도 최대 횟수(화면에만).
- 대상 DB — en-orig 10:14 주어 탈락(ko만 "Mongo"). function operator·collection·document store 어휘가 문서형 DB를 가리키지만 확정하지 않는다.
- identity 매칭 알고리즘, 오매칭 처리.
- 정확도·지연 수치 없음(데모 성공 사례만).

## References

- [[tech-bridge-unblocked-context-engine-structured-queries]] · [[unblocked]] · [[context-engine]]
- 대비: [[build-time-vs-runtime-tools]] · [[secure-tool-evolution]] · [[mcp-toolbox-for-databases]] · [[company-brain]](Conductor CIA의 *"give your agent a SQL tool"*)
