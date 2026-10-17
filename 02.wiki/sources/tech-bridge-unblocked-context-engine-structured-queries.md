---
title: "Tech Bridge — RAG만으로는 부족합니다 (Peter · Unblocked): 컨텍스트 엔진과, RAG의 다른 절반인 구조화 쿼리 스캐폴딩"
type: source
tags: [context-engine, institutional-knowledge, grounded-context, context-bundle, retrieval, rag, structured-retrieval, nl-to-query, query-synthesis, schema-discovery, enum-inference, identity-resolution, fuzzy-matching, query-validation, tenant-isolation, hidden-fields, self-correction, retry-loop, full-text-search, deterministic-first, ab-test, cost, unblocked, video]
source-url: https://www.youtube.com/watch?v=djKIU-30YVc
source-type: video
author: Tech Bridge (한영자막 재배포) · 발표 Peter([[unblocked|Unblocked]] — 자막 자기소개는 "I'm Peter from Unblocked"뿐, **성 Werry·직함 '창립 엔지니어'는 설명란에만**) · 행사명 미발화(설명란 ai.engineer 링크 → AI Engineer 계열 추정, "we've only got 20 minutes") · 녹화일 미발화
date-published: 2026-10-14
ingested: 2026-10-15
created: 2026-10-15
updated: 2026-10-15
---

# Tech Bridge — RAG만으로는 부족합니다 (Peter · Unblocked)

[[tech-bridge|Tech Bridge]]가 재배포한 **18:49 발표, Q&A 없음, 공식 챕터 15개.** 화자는 [[peter-werry|Peter]] — 자막의 자기소개는 *"I'm I'm Peter from Unblocked. And at Unblocked, we build a context engine."*(00:06~00:12)뿐이고, **성 Werry와 직함 "창립 엔지니어"는 설명란에서만 온다.** 발표는 두 부분이다(*"The talk's going to be split into two parts."* 00:13~00:15) — ① [[context-engine|컨텍스트 엔진]]이 무엇이고 어떤 가치를 내는지(자사 제품 데모 둘), ② 그 엔진의 한 부품인 **자연어 → 구조화 쿼리 엔진**을 오픈소스 repo로 단계별로 켜 보는 라이브 빌드. 테제:

> **에이전트는 신입 사원처럼 조직을 모른다. 컨텍스트 엔진은 흩어진 조직 지식을 과제별 묶음으로 미리 건넨다. 그리고 RAG는 "내용" 질문엔 강하지만 "지난주 내가 머지한 PR" 같은 구조적 질문은 시맨틱 검색이 아니라 쿼리다 — 쿼리를 만드는 것은 쉽고, 어려운 것은 그 주변의 스캐폴딩(스키마·identity·검증·재시도)이다.**

> *"in those days, um you were the context layer."* (00:49~00:52) · *"RAG nails the content part."* (06:25) · *"these are queries. They're not semantic searches."* (07:00~07:03) · *"generating the queries is actually the easy part. The hard part is the scaffolding that sits around it."* (08:00~08:06)

이 위키에 개념 둘이 생긴다 → [[context-engine]](신규 제안 — 조직 지식을 과제별 grounded context로 내보내는 층) · [[nl-to-structured-query-scaffolding]](신규 제안 — NL → 쿼리 생성 주변의 다섯 단계). 나머지는 기존 페이지의 증언·반론이다 — [[code-only-index-blind-spot]](*"셋을 하나로 잇는 소스는 아직 없다"* 의 첫 후보) · [[reference-graph-vs-vector-search]](벡터 검색이 못 하는 세 번째 질문 유형) · [[build-time-vs-runtime-tools]](⚠️ NL→쿼리를 **프로덕션 채팅 에이전트**에 둔다) · [[bound-parameters]]·[[credential-injection-outside-sandbox]](tenant 필드 뒤에서 주입) · [[company-brain]](네 번째 형식) · [[deterministic-agent-pipeline]](*"don't always fall back to an LLM"*) · [[file-discovery-tax]]·[[token-minimization-trap]](컨텍스트를 **더 주어** 비용이 준다).

ASR·ko 보정: ko는 **발표의 주제어를 넷 다 흔든다** — 회사명 Unblocked → **"차단 해제"**(00:09), LLM → **"법학 석사(LLM) 학위/과정"**(11:00 등 6곳), PR → **"홍보팀"·"홍보 자료"·"개인 최고 기록"**(05:01, 12:50 등), schema → **"계획"**(6곳), retrieval → **"회복"**(07:41). 첫 비유 *"you were the context layer"* → **"당신은 망토였어요"**(00:48). 반전: *the other week* → **"다음 주에"**(04:15), *we're actually not running it* → **"시행하고 있습니다"**(09:44), *If you don't want to wire up Unblocked* → **"Unblocked에 바로 접속하시겠습니까?"**(18:14). 수치: "260" → **"2분 60초"**(03:53). `en`·ko 공유: queries → *"consultations"*/"상담"(07:00), RAG → *"record"*/"기록"(17:03), 모델 버전 → **"4.6 → 4.8"**(en-orig는 *"Opus 48 or Opus 46 to Opus 48"* — 판독 보류). en-orig 10:14 주어 탈락을 ko만 **"Mongo"** 로 채운다 — 채우지 않는다. 전체 목록은 raw.

> ⚠️ **당사자 진술 — 전부 자사 데모.** 1부 데모 둘은 Unblocked 제품, 2부는 자사 오픈소스 repo. **50% 비용 절감은 세션 1건의 비교**다 — *"a dollar 29 (…) about a minute and 30 seconds"*(03:43~03:49) vs *"up to, you know, 260 and 3 minutes"*(03:53~03:55), *"a 50% reduction in cost"*(03:57~03:59). 반복 횟수·과제 수·모델·설정은 발화되지 않는다. **"260"의 단위도 발화되지 않는다**($2.60로 읽으면 1.29/2.60 ≈ 0.50 — 위키의 계산).
>
> ⚠️ **"토큰"·"관계형"은 발화에 없다.** 제목·설명란의 *"토큰 비용을 절반으로"* 는 화자의 *"cost"*(달러), *"관계형 컨텍스트 엔진"* 은 화자의 *"grounded context (…) all interrelated to each other"*(01:36~01:44)·*"structured, queryable context"*(18:00~18:02)를 업로더가 옮긴 말이다. 제목 *"RAG만으로는 부족합니다"* 도 화자는 RAG를 깎지 않는다(*"RAG nails the content part"*) — **다른 절반을 더한다.**
>
> ⚠️ **화자 신원.** 이름은 *"Peter"* 만 발화. 성·직함은 설명란에서만 — 자막과 충돌하지 않는다.
>
> ⚠️ **모델 버전 판독 보류.** 두 번째 데모의 원인 *"we switched from Opus 48 or Opus 46 to Opus 48"*(04:42~04:45)는 en-orig에서 읽히지 않는다. `en`·ko의 "4.6 → 4.8"은 번역 트랙이 숫자를 고친 것 — 이 위키는 어느 Claude 모델 페이지에도 연결하지 않는다.
>
> ⚠️ **행사·시점.** 행사명·도시·연도 미발화. 시간 단서 *"we've only got 20 minutes"*(00:04). 설명란 `https://ai.engineer` 링크 → **[[ai-engineer|AI Engineer]] 계열 추정**(확정 아님).

## 1. 당신이 context layer였다 (00:00~01:52)

- 에이전트 이전: *"you were the context layer."*(00:49~00:52) 신입 사원은 *"look at a whole bunch of code, rip around documentation systems"*(01:03~01:06)하고, 그 위에 *"all of the the sort of shared history that's built up over time through an organization, dealing with incidents and the battle scars that come with it."*(01:12~01:21)
- 정의: *"what a context engine does is it takes all of that institutional knowledge and it pulls it in."*(01:25~01:29) 나오는 것은 *"grounded context, which means that the context is all interrelated to each other. It's intent-specific. It's personalized. And it's permissions-aware."*(01:36~01:48)
- ⚠️ 네 성질 중 **permissions-aware는 1부 데모에서 보이지 않는다** — 2부의 tenant 격리(§6)가 가장 가까운 대목이다. *personalized* 는 2부 synthesis의 *"information about the user that's asking the question"*(12:44~12:47)로만 구체화된다.

→ [[context-engine]] (신규) · [[company-brain]] · [[agent-knowledge-sourcing]]

## 2. 데모 1 — 같은 과제, 컨텍스트 엔진 유무 (01:57~04:00)

- 과제: Claude에게 *"create a plan to optimize a component in our layer called the Source Mark engine"*(02:11~02:16). ⚠️ "Claude"만 발화 — 제품 형태(Claude Code 등) 미발화.
- 엔진 없이: *"It's like a new employee. It doesn't understand anything about your your code base or your organization. So, the first thing it does is it grabs around your code base"*(02:24~02:34) — *"it figures it out eventually. Or at least, you know, it confidently projects that it's figured it out."*(02:38~02:44) → [[file-discovery-tax]]
- 엔진을 붙이면: *"it calls the Unblock[=Unblocked] Context engine. And Unblock now delivers a very comprehensive but task-specific context bundle for this task."*(02:55~03:04) 묶음은 *"not only the source code, but also, you know, Notion documents that talked about the architecture, um pull requests, Slack conversations"*(03:08~03:18), 그리고 *"all these great jump-off points"*(03:33~03:34) — 더 가져올 링크.
- ⭐ 비용: *"a dollar 29 on this, and it took about a minute and 30 seconds"*(03:43~03:49) vs *"without, I'm spending up to, you know, 260 and 3 minutes. So, what you see essentially is a 50% reduction in cost, which is pretty incredible."*(03:50~04:00) ⚠️ 세션 1건, *"up to"* — 최댓값인지 한 번의 값인지 모호.

→ [[push-vs-pull-context-retrieval]](엔진 호출은 에이전트가 시작하지만, 돌아오는 것은 **미리 조립된 과제별 묶음**) · [[token-minimization-trap]](반대 방향 — 컨텍스트를 **더 주어** 비용이 줄었다는 주장)

## 3. 데모 2 — 이슈 수가 줄었다, 왜? (04:02~05:28)

- 동료 Richie가 자사 **code review 제품**(*"We also have a code review product, and Richie works on that"* 04:17~04:23)의 *"the number of issues that the code review product was surfacing was was starting to drop."*(04:23~04:30)
- Unblocked가 *"narrow it down very quickly to uh a likely cause, which is that we switched from Opus 48 or Opus 46 to Opus 48, and the behavior characteristics behind the scenes, um you know, caused all those issues to drop."*(04:36~04:52) ⚠️ 버전 판독 보류, *likely* 원인.
- *"he asked Unblocked to just fix it"*(04:54~04:56) → *"create a PR behind the scenes"*(05:01~05:03). PR 설명이 *"understood the PR that caused the regression in the first place, and then it found a Slack conversation (…) and pulled on some of the data here to help inform um the fix"*(05:14~05:26). ⚠️ 설명문·수정 내용은 화면에만, 머지 여부 미발화.
- 이 대화의 첫 질문은 구조화 쿼리였다 — *"Can you show me a chart of ratio weekly since January 1st?"*(07:20~07:22) — *"it's not going to be able to just pull this information from a vector store cuz that's not where that information's encoded."*(07:24~07:30) → §4로 이어진다.

→ [[automated-code-review]](리뷰 제품의 산출량이 **모델 교체로 조용히 줄었다**는 일화) · [[ride-the-optimization-trajectory]](⚠️ 반례 — 그 페이지는 *모델 교체가 내 시스템의 업그레이드* 라 했는데, 여기선 모델 교체가 **조용한 회귀**였다)

## 4. RAG의 다른 절반 — 구조적 질문 (06:00~07:56)

- 컨텍스트는 *"PRs, reviews, comments, issues, and tickets, docs, conversations"*(06:11~06:15)에 흩어져 있고 *"all of that is uh semantically queryable, but it's also structured."*(06:17~06:22)
- ⭐ *"RAG nails the content part. (…) Find the code, the PR that changed it, the Slack thread that's debating it. And if you wrap that stuff in an agent loop, it can go really really far."*(06:25~06:40) → [[agentic-search]]
- ⭐ *"But it doesn't handle some of the other type of uh structural questions, like PRs that I merged last week. Who reviewed payments the most, open PRs, etc. Um and these are queries. They're not semantic searches."*(06:48~07:03)
- *"retrieval has two halves essentially. We've got semantic retrieval (…) but today we're going to work on this, the structured part. We're going to turn structured queries or natural language queries into structured queries."*(07:40~07:56)

| | semantic retrieval | structured retrieval |
|---|---|---|
| 질문 예 | *"Find the code, the PR that changed it, the Slack thread"* | *"PRs that I merged last week"* · *"Who reviewed payments the most"* · *"ratio weekly since January 1st"* |
| 필요한 것 | 벡터 검색 + agent loop | 쿼리 엔진(필터·집계·시간 범위) |

→ [[retrieval-augmented-generation]] · [[reference-graph-vs-vector-search]](유사도 vs 참조 관계에 이은 **세 번째 축: 유사도 vs 집계·필터**)

## 5. 쿼리 생성은 쉽다 — 스캐폴딩이 어렵다 (08:00~09:13)

- ⭐ *"generating the queries is actually the easy part. The hard part is the scaffolding that sits around it."*(08:00~08:06) 네 가지(08:06~08:58):
  1. **스키마** — *"understand the schema so you can pass it to the LLM so it generates the a tightly bound query."*
  2. **identity 매핑** — *"open PRs by Rasheen, it's not going to know who Rasheen is because his identity in GitHub might be completely different."*
  3. **검증** — *"when you get the query out of the LLM, it's untrusted. It could have operations that are dangerous. It could cross tenant boundaries."*
  4. **오류 자기 교정** — 검증 뒤에도, DB 실행 시에도 오류가 날 수 있으니 *"we can actually get the LLM to try to correct itself"*.
- repo: *"It's called the document query engine."*(09:29~09:31) 처음엔 *"It's not going to be wired up at all. It's going to produce nothing."*(10:01~10:03) — 단계를 하나씩 켠다(*"level up to the next"* 11:17). ⚠️ GitHub URL은 설명란·화면에만.

→ [[nl-to-structured-query-scaffolding]] (신규)

## 6. 단계별 빌드 (10:10~16:53)

| 단계 | en-orig | 핵심 |
|---|---|---|
| ① 자동 스키마 탐색 (10:10~11:41) | *"sampling a whole bunch of documents in the document store, and then deriving a schema from that"*(10:28~10:33) · *"one tricky part of that, which is inferring enums"*(10:37~10:39) | 런타임 동적 탐색, 스키마 + *"indexes that will help improve the performance of queries"*(11:39~11:41). ⚠️ DB 이름은 en-orig 탈락(10:14 — ko만 "Mongo") |
| ② identity resolution (11:46~12:19) | *"you can do this kind of fuzzy matching, and then in the end, if you have to, you can pass a list of names to an LLM and have it act as a tiebreaker."*(12:12~12:18) | *"that's actually more or less how we do it uh in underneath the hood at Unblocks"*(12:01~12:05) — 제품 내부에 대한 유일한 직접 진술 |
| ③ synthesis (12:26~13:20) | *"this is actually the easiest part. We just take the schema (…) We take the current date and time. Uh maybe some information about the user that's asking the question, so it can easily resolve questions like my PRs and not just Peter's PRs."*(12:34~12:51) | 컨텍스트 = 스키마 + 현재 시각 + 질문자 |
| ④ validation (13:26~14:52) | ⭐ *"This is actually the most important thing."*(13:29) · *"dangerous operators like the function operator for example, which would execute raw JavaScript um on the DB server"*(13:35~13:41) · *"metadata fields for example that contain um tenant IDs (…) you're better off making sure that the LLM doesn't interact with those fields at all and then just constraining it behind the scenes. You can inject those fields underneath."*(13:56~14:12) | 데모: *"PRs with authentication in the title"* → 정규식 쿼리 → *"Sorry, regular expressions aren't allowed. You're getting bounced."*(14:39~14:50) |
| ⑤ retry (14:57~16:07) | *"take that error and just loop it back in to the LLM and have the LLM kind of self-correct. (…) It's just a loop with some sort of maximum, uh, retry."*(15:05~15:20) | ⭐ 데모: *"it actually took a couple attempts. Um, but it got there in the end. However, um, it constrained it down to use match, and unfortunately, this is an exact title match. We don't have any PRs with that exact title."*(15:53~16:07) |
| ⑥ full-text search (16:08~16:53) | *"So, we need one more thing, which is this, full-text search."*(16:08~16:13) | 추가 후 성공(16:45 *"Awesome."*, 결과는 화면에만) |

- ⭐ **결정론 우선**(①의 결론): *"you can use an LLM as a Thor hammer, um and it can do a pretty good job. But actually, you get uh really, really far just using traditional procedural methods. (…) don't always fall back to an LLM to do this kind of what looks like non-deterministic work. This is actually quite deterministic"*(10:46~11:06). ②도 같다 — *"this can be solved just using simple procedural tricks"*(11:54~11:59), LLM은 동점일 때만. ⚠️ *"Thor hammer"* 판독 보류.
- ⭐ **⑤의 교훈 — 검증을 통과한 쿼리가 의도를 놓친다.** 검증기가 정규식을 막자 재시도 루프는 **허용된 연산(exact match)으로 수렴했고, 결과는 비었다.** 화자는 이를 *"it got there in the end"* 라 하면서도 곧 *"unfortunately"* 로 이어 검색 프리미티브(full-text)를 하나 더 준다. ⚠️ 이 대비(통과 ≠ 정답)는 위키의 정리이고 화자가 일반화하지 않는다.
- 결과: *"something that can effectively handle all of the, uh, other half of Reg[=RAG]. So, anything that has to do with, uh, structural-based data. You can have filters, aggregations, it's time-scoped, and it self-corrects."*(16:58~17:14) 그리고 *"it also powers a chat agent"*(17:18~17:19) — *"What authentication related things have we been working on last week?"*(17:27~17:34)에 쿼리들을 보이며 답한다.

→ [[nl-to-structured-query-scaffolding]] · [[deterministic-agent-pipeline]] · [[bound-parameters]] · [[credential-injection-outside-sandbox]] · [[retrieval-primitive-repertoire]](full-text가 빠지면 루프가 엉뚱한 프리미티브로 수렴) · [[tech-bridge-sentry-stop-prompting-codify-linters]](검사를 피해 수렴하는 에이전트 — whack-a-mole)

## 7. 컨텍스트 엔진 시뮬레이터 (18:06~18:46)

- *"If you don't want to wire up Unblocked uh right away because you've got some constraints in your in your environment, um we have an open-source project that will allow you to do this entirely locally yourself."*(18:14~18:25)
- *"it will create a context bundle for you on a task-by-task basis, and then take that context bundle and run an AB test against the same task, and show you the benefits of having all of that context at your fingertips for your agents."*(18:27~18:43) ⚠️ 프로젝트 이름·URL 미발화(*"that's the uh PR code[=QR code?] for that"* 18:44~18:46). §2의 50% 주장을 **사용자가 재현할 도구**로 내놓지만, 이 발표엔 시뮬레이터 결과가 없다.

→ [[context-engine]] · [[skill-evals]](같은 과제를 조건만 바꿔 비교)

## 이 위키와의 연결

### 이어지는 것

- **[[code-only-index-blind-spot]] — "셋을 하나로 잇는 소스"의 첫 후보.** 그 페이지는 코드(참조 그래프)·의도·규칙(파일)·과거 결정(검색)을 *하나로 잇는 소스는 아직 이 위키에 없다* 고 적었다. Unblocked의 context bundle은 **코드 + Notion 문서 + PR + Slack** 을 한 묶음으로 돌려준다(03:08~03:20). ⚠️ 다만 묶음을 **어떻게** 만드는지(인덱스·랭킹·권한)는 2부의 쿼리 엔진 외엔 발화되지 않는다 — 제품 시연이지 방법의 공개가 아니다.
- **[[reference-graph-vs-vector-search]]** — Graft는 *"의미가 비슷한 것"과 "실제로 서로를 쓰는 것"* 을 갈랐다. Peter는 세 번째 질문을 더한다: **"몇 개·누가·언제"** — 필터·집계·시간 범위는 유사도로도 참조로도 답할 수 없고 쿼리여야 한다.
- **[[company-brain]] — 네 번째 형식.** PromptQL(링크된 마크다운)·Vercel(grep 가능한 파일)·Conductor CIA(원천 기록을 Postgres에, 에이전트엔 SQL)에 이어, Unblocked는 **원천 시스템(GitHub 등)을 문서 저장소로 두고 NL → 검증된 쿼리** 를 끼운다. CIA의 *"give your agent a SQL tool and let it handle the rest"* 와 달리 **에이전트에게 원시 쿼리를 맡기지 않고 검증·주입 층을 둔다.**
- **[[bound-parameters]] · [[credential-injection-outside-sandbox]] — 같은 원칙, 넷째 자리.** tenant ID를 *"make sure that the LLM doesn't interact with those fields at all (…) inject those fields underneath"*(14:05~14:12). Google Cloud는 도구 시그니처에서, PromptQL은 프록시에서, 여기서는 **생성된 쿼리를 실행 직전 고쳐 쓰는 자리**에서 같은 벽을 세운다.
- **[[deterministic-agent-pipeline]]** — Uber의 *결정론 노드 + LLM 노드* 와 같은 감각을 부품 단위로: 스키마 추론·identity 매칭은 절차적으로, LLM은 synthesis와 tiebreaker에만.
- **[[file-discovery-tax]]** — 엔진 없는 Claude가 *"grabs around your code base"*(02:31~02:34)하는 장면이 그대로 탐색세다. 처방은 Graft(코드 그래프)와 달리 **코드 밖 맥락까지 미리 묶어 주는 것.**

### 갈리는 것

> ⚠️ **Contradiction: NL → 쿼리를 프로덕션에 둘 수 있는가.** [[build-time-vs-runtime-tools]]([[google-cloud|Google Cloud]] Toolbox 팀)는 NL→SQL을 **빌드타임 전용**(*"사람이 루프 안에"*, 프로덕션 **불가**)으로, 프로덕션은 **미리 정의한 결정론적 쿼리**로 가라고 했다. Peter는 NL → 쿼리를 **사용자 앞의 chat agent**(17:18~17:19)에 두고, 위험은 도구를 고정하는 대신 **생성된 쿼리를 검증(위험 연산자·정규식 금지)하고 tenant 필드를 뒤에서 주입**해 막는다. 위키의 독해: 두 소스는 적용 대상이 다르다 — Google의 사례는 **쓰기·삭제가 가능한** 도구(*"테이블을 삭제하고 새로 시작하자"*)였고, Peter의 엔진은 **조회 질문**만 다룬다. 다만 Peter는 **읽기 전용 제한을 명시하지 않는다**(검증 규칙의 전체 목록은 화면에만) — 그 페이지의 미해결 *"분석 에이전트가 프로덕션 데이터를 읽기 전용으로 탐색하는 경우는 어느 쪽인가?"* 에 대한 **벤더 한 곳의 실천 답**이다.

> ⚠️ **긴장: 컨텍스트를 더 주면 비용이 준다?** [[token-minimization-trap]]은 *입력 토큰을 깎으면 비용이 다른 데로 옮겨 간다* 고 했고, Peter의 데모는 그 역 — **미리 컨텍스트를 묶어 주면 총비용이 절반**(03:57~03:59). 같은 방향의 주장이지만 **둘 다 측정 설계가 공개되지 않았다**(Peter: 세션 1건). 시뮬레이터(§7)가 이 주장의 재현 도구로 제시된다.

> **검증 게이트도 우회 경로가 된다.** [[tech-bridge-sentry-stop-prompting-codify-linters|Pstrucha]]의 lint whack-a-mole(코드 블록 삭제 → 백틱 제거 → 산문)에서 에이전트는 검사를 피해 갔다. 여기서는 의도적 회피가 아니라 **재시도 루프가 허용된 연산으로 수렴해 의도를 놓친다**(§6 ⑤). 두 사례 모두 처방은 검사를 풀지 않고 **다른 수단(규칙 추가 / full-text search)을 덧대는 것**이다 → [[reward-hacking]]·[[verifiable-goals]]의 *통과 ≠ 의도*.

## 해소하지 않고 표시만 한 것

- 50% 비교의 반복 횟수·모델·과제 수, "260"의 단위, *"up to"* 의 뜻.
- 두 번째 데모의 모델 버전(*"Opus 48 or Opus 46 to Opus 48"*), 원인 확정 여부, 수정 PR의 머지 여부.
- 10:14의 빠진 DB 이름(ko *"Mongo"* 만). function operator가 어느 DB의 것인지.
- 검증 규칙의 전체 목록과 읽기 전용 여부(화면에만). 재시도 최대 횟수. identity 매칭의 알고리즘.
- context bundle을 만드는 방법(인덱스·랭킹·권한 처리) — *permissions-aware* 의 구현.
- *"Thor hammer"*(10:46)의 원 표현. *"PR code"*(18:44). Source Mark engine이 무엇인지. 동료 Richie의 성·직함. 시뮬레이터 이름·URL.
- 행사명·도시·녹화일. 화자의 성·직함(설명란만).

## 등장 개체

- 인물: [[peter-werry|Peter Werry]](신규 제안 — 자막엔 "Peter"만, 성·직함은 설명란에만) · Richie(동료, 페이지 없음) · Rasheen(데모 쿼리의 예시 이름, 페이지 없음)
- 조직: [[unblocked|Unblocked]](신규 제안) · [[ai-engineer|AI Engineer]](⚠️ 설명란 링크만 — 추정)
- 제품·도구: Unblocked context engine · Unblocked code review 제품 · document query engine(오픈소스 repo, 설명란 `github.com/unblocked/document-query-engine`) · context engine simulator(이름 미발화) · Claude(⚠️ 제품 형태 미발화) · Notion · Slack · GitHub — 모두 별도 페이지 없음([[unblocked]]에 포함 제안)
- 개념: [[context-engine]](신규 제안) · [[nl-to-structured-query-scaffolding]](신규 제안) · [[retrieval-augmented-generation]] · [[reference-graph-vs-vector-search]] · [[code-only-index-blind-spot]] · [[company-brain]] · [[agent-knowledge-sourcing]] · [[agentic-search]] · [[push-vs-pull-context-retrieval]] · [[file-discovery-tax]] · [[token-minimization-trap]] · [[build-time-vs-runtime-tools]] · [[bound-parameters]] · [[credential-injection-outside-sandbox]] · [[deterministic-agent-pipeline]] · [[retrieval-primitive-repertoire]] · [[automated-code-review]] · [[ride-the-optimization-trajectory]] · [[reward-hacking]] · [[verifiable-goals]] · [[skill-evals]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=djKIU-30YVc> (18:49, `upload_date` 2026-10-14)
- raw: `01.raw/articles/2026-10-14_RAG만으로는 부족합니다 - 토큰 비용을 절반으로 줄이는 관계형 컨텍스트 엔진.md`
- 설명란 링크: <https://getunblocked.com> · <https://github.com/unblocked/document-query-engine> · <https://x.com/get_unblocked> · <https://ai.engineer> (⚠️ 열어 보지 않았다)
- 코드 밖 맥락·검색의 축: [[tech-bridge-graft-code-knowledge-graph]] · [[tech-bridge-sourcegraph-codebase-visibility]] · [[tech-bridge-llamaindex-document-context-layer]] · [[tech-bridge-bm25-agentic-search]]
- 조직 지식의 형식: [[tech-bridge-company-brain-security]] · [[tech-bridge-conductor-orchestras-not-factories]]
- NL → 쿼리의 자리: [[tech-bridge-build-time-vs-runtime-tools]] · [[tech-bridge-uber-debug-assist]]
- 검사 우회: [[tech-bridge-sentry-stop-prompting-codify-linters]]
- [[tech-bridge]] · [[unblocked]] · [[peter-werry]]
