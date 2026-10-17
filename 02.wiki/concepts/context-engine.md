---
title: "컨텍스트 엔진 (Context Engine)"
type: concept
category: pattern
tags: [context-engine, institutional-knowledge, grounded-context, context-bundle, retrieval, organization]
aliases: [context engine, 컨텍스트 엔진, context bundle, grounded context]
related: [company-brain, agent-knowledge-sourcing, code-only-index-blind-spot, retrieval-augmented-generation, nl-to-structured-query-scaffolding, push-vs-pull-context-retrieval, file-discovery-tax, context-engineering, token-minimization-trap, agentic-search, review-wip-limit]
first-seen: tech-bridge-unblocked-context-engine-structured-queries
sources: [tech-bridge-unblocked-context-engine-structured-queries, tech-bridge-atlassian-build-your-own-sdlc]
created: 2026-10-16
updated: 2026-10-17
---

# 컨텍스트 엔진 (Context Engine)

**조직 곳곳에 흩어진 지식(코드·문서·PR·대화·이슈)을 끌어와, 에이전트가 과제를 시작할 때 그 과제에 맞춘 "grounded context" 묶음으로 내보내는 층.** [[unblocked|Unblocked]]의 [[peter-werry|Peter]]가 [[tech-bridge-unblocked-context-engine-structured-queries]]에서 자사 제품 범주로 제시했다.

> *"what a context engine does is it takes all of that institutional knowledge and it pulls it in. And what you get the scattered context that goes into the context engine and out the other end, you get grounded context, which means that the context is all interrelated to each other. It's intent-specific. It's personalized. And it's permissions-aware."* (01:25~01:48)

## 출발점 — 사람이 context layer였다

*"in those days, um you were the context layer."*(00:49~00:52) 신입 사원은 코드와 문서 시스템을 뒤지고, 조직이 쌓은 *"shared history (…) dealing with incidents and the battle scars"*(01:12~01:21)를 몸으로 배운다. 에이전트는 매 과제가 첫 출근이다 — *"It's like a new employee. It doesn't understand anything about your your code base or your organization."*(02:24~02:30) → [[file-discovery-tax]]

## 네 성질 (화자의 목록)

| 성질 | 소스에서 구체화된 정도 |
|---|---|
| interrelated | 묶음이 코드·Notion·PR·Slack을 함께, 링크(*"jump-off points"*)와 함께 준다(03:08~03:34) |
| intent-specific | *"task-specific context bundle for this task"*(03:02~03:04) |
| personalized | 2부 쿼리 synthesis에 *"information about the user that's asking the question"*(12:44~12:47) |
| permissions-aware | ⚠️ 1부 데모에선 보이지 않음. 2부의 tenant 필드 주입(14:01~14:12)이 가장 가까움 |

## 두 절반

화자는 엔진의 검색을 *"retrieval has two halves"*(07:40~07:42)로 나눈다 — 내용을 찾는 semantic retrieval([[retrieval-augmented-generation|RAG]] + agent loop)과, *"PRs that I merged last week"* 같은 질문에 답하는 structured retrieval([[nl-to-structured-query-scaffolding]]).

## 주장된 효과 — ⚠️ 세션 1건

같은 과제(Claude에게 컴포넌트 최적화 계획)를 엔진 유무로: $1.29·약 1분 30초 vs *"up to (…) 260 and 3 minutes"* → *"a 50% reduction in cost"*(03:43~03:59). "260" 단위 미발화. 검증 도구로 오픈소스 **context engine simulator**(과제별 묶음 → 같은 과제 A/B 테스트, 18:27~18:43)를 내놓지만 결과는 발표에 없다.

## 이 위키에서의 자리

- [[company-brain]] — 같은 문제(조직 지식을 에이전트에게)의 **다른 형식**: PromptQL(링크된 마크다운, 사람 승인) · Vercel(grep 가능한 파일) · Conductor CIA(원천 기록을 Postgres에) · **컨텍스트 엔진(원천 시스템에서 과제별로 조립해 push)**.
- [[code-only-index-blind-spot]] — *"셋을 하나로 잇는 소스는 아직 없다"* 의 첫 후보. 단 조립 방법은 공개되지 않았다.
- [[push-vs-pull-context-retrieval]] — 호출은 에이전트가 시작(pull)하지만 결과는 **미리 조립된 묶음**이다. 두 축의 중간.
- [[agent-knowledge-sourcing]] — 라우팅 표의 갈래를 고르는 일을 엔진이 대신 한다(코드·문서·대화를 한 호출로).
- [[token-minimization-trap]] — 반대 방향의 같은 주장: 컨텍스트를 깎지 말고 **더 잘 주면** 총비용이 준다.

## ⚠️ 미해결

- 묶음을 만드는 방법(인덱싱·랭킹·중복 제거·권한 필터)이 발화되지 않는다 — 제품 시연이지 설계 공개가 아니다.
- 효과 수치는 벤더 데모 1건. 독립 재현 없음.
- *permissions-aware* 의 구현.

## 두 번째 벤더 — "more agentic search" (2026-10-17 · [[tech-bridge-atlassian-build-your-own-sdlc]])

[[atlassian|Atlassian]]도 같은 이름을 쓴다(AI Context Engine). 다만 형태가 다르다. [[unblocked|Unblocked]]는 과제별 grounded context 묶음을 **push**한다. Atlassian은 *"the context engine itself is more agentic search is the way to think about it"*(50:56~51:00)이라고 말한다.

- **그래프 위의 검색**: *"a number of I guess graph databases inside of Atlassian that connect to all of the data"*(16:14~16:20)가 있다. 연결은 *"through inferences as you use the product or (…) explicit"*(16:37~16:42)로 생긴다. 그 위에서 *"narrowing down the retrieval and the search space to scope it to like where this answer is most likely uh lives within the code"*(47:56~48:07).
- **모노레포의 대안**: *"product repos feel like monor repos because you can pull in that engine at hawk[=ad hoc]"*(18:52~18:55). 스냅샷이 아니라 즉석 조회다(*"you don't snapshot it"* 20:34~20:37).
- **권위는 사람이 표시한다**: *"you need a human to tell like yes, this is actually true"*(20:23~20:25). Confluence verified badge(35:55~36:05)가 그 표시이고, *"the risk by automating that stuff is (…) things automated automatically end up being authoritative which is weird"*(21:22~21:32).
- **결정의 이유**: [[shane-wolf|Shane Wolf]]는 *"historical information about why decisions were made (…) often left out of um agent generated code"*(49:01~49:07)라고 말한다.
- ⚠️ 이 위키의 "네 성질" 중 permissions-aware는 이 소스에서도 발화되지 않는다. 효과 수치도 없다. 화자 귀속 일부는 추정이다(Wi-Fi 장애 중 Q&A).

## References

- [[tech-bridge-unblocked-context-engine-structured-queries]] · [[unblocked]] · [[peter-werry]]
