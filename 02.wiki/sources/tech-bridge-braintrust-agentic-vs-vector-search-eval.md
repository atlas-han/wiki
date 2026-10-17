---
title: "Tech Bridge — 코딩 에이전트의 Agentic Search와 Vector Search, 직접 평가해봤습니다 (Jess Wang · Braintrust): eval의 네 요소, 그리고 같은 정확도에 4배 비용"
type: source
tags: [evals, eval-anatomy, datasets, scoring, experiments, observability, tracing, orphaned-traces, agentic-search, vector-search, code-search, embeddings, claude-code, disallowed-tools, prompting-is-not-enough, cost, small-n, single-trial, sycophancy, team-sport, braintrust, vendor, video]
source-url: https://www.youtube.com/watch?v=pLdgH-jLw5A
source-type: video
author: Tech Bridge (한영자막 재배포) · 발표 Jess Wang([[braintrust|Braintrust]] DevRel engineer — **"Jess"와 소속·직함은 자막에서 자기소개**, 성 Wang은 설명란·LinkedIn 슬러그에만) · 행사명 미발화(설명란 ai.engineer 링크 + #AIEngineer → AI Engineer 계열 추정) · 녹화일 미발화(*"about a year ago, so April of 2025"* → 2026년 봄 무렵으로 읽힘)
date-published: 2026-10-15
ingested: 2026-10-16
created: 2026-10-16
updated: 2026-10-16
---

# Tech Bridge — 코딩 에이전트의 Agentic Search와 Vector Search, 직접 평가해봤습니다 (Jess Wang · Braintrust)

[[tech-bridge|Tech Bridge]]가 재배포한 **17:46 단독 발표, Q&A 없음, 공식 챕터 20개.** 화자 [[jess-wang|Jess Wang]]은 자막에서 이름과 소속을 밝힌다 — *"Hey everyone, I'm Jess. I'm from Brainest[=Braintrust]. I'm a deval[=DevRel] engineer at Brainest."*(00:00~00:04) 성(Wang)은 설명란에만 있다. [[braintrust|Braintrust]]의 두 번째 소스다(첫 소스는 [[tech-bridge-braintrust-eval-platform-systems-problem|Hossein Niazmandi 편]], 10-11 업로드).

발표는 두 부분이다. **전반(00:00~08:26)은 eval 입문**이고, **후반(08:29~17:43)은 실제로 돌려 본 실험** — 코딩 에이전트의 버그 위치 찾기에서 agentic search(grep·find·ls·cat으로 탐색)와 vector search(임베딩 청크 검색)를 같은 Claude Code 하네스 위에서 비교했다. 테제:

> **출시 결정을 vibes로 하지 말고 질문에 데이터로 답하라. eval은 데이터셋·태스크·채점·실험 네 요소이고, 그 조합 하나가 실험 하나다. 실제로 코드 검색 두 방식을 eval해 보니 정확도는 같았고 vector search가 4배 비쌌다 — 청크는 코드 근처까지는 데려가지만(proximity) 로직을 잇는 연결 조직(connective tissue)이 없어서 검색을 반복했기 때문이다. 단, 20행·1회 시행·약한 vector 구현의 작은 실험이다.**

> *"these teams are making ship decisions based off of vibes"* (00:51~00:53) · *"every configuration of a specific data set a specific task and a specific scoring system equals to one experiment"* (04:02~04:10) · *"eval are a team sport"* (07:35~07:39) · *"prompting is never enough"* (12:47~12:50) · *"both got the same level of accuracy, but essentially vector search cost uh four times more than agentic search"* (14:51~15:01) · *"vector search gave a lot of proximity to the correct code, but agentic search had more of the connective tissue"* (15:59~16:06)

이 위키에 개념 하나가 생긴다 → [[eval-experiment-anatomy]](신규 제안 — 데이터셋·태스크·채점·실험). 나머지는 기존 페이지의 **새 증언**이다 — [[agentic-search]]·[[reference-graph-vs-vector-search]](이 위키 **첫 코드 검색 두 방식의 직접 비교 실험**), [[file-discovery-tax]](위치 찾기 비용이 검색 반복으로 4배), [[production-trace-eval-flywheel]](Braintrust의 두 번째 서술), [[eval-platform-maturity-stages]](팀 스포츠 — PM·SME·분석가), [[hard-vs-soft-enforcement]](프롬프트 금지 → disallowed tools 플래그), [[claude-code]](서브프로세스 trace).

ASR·ko 보정: **고유명사는 ko·`en`이 en-orig보다 정확하다** — en-orig *"Brainest"*·*"Anker"*·*"cqrant"*·*"GP find lscat"* 를 `en`은 Braintrust·Ankur·Qdrant·grep, find, ls, cat으로 적는다. 반면 ko는 용어를 일상어로 무너뜨린다 — LLM-as-a-judge → **"LLM 학위"**(03:49), team sport → "스포츠 / 장비"(07:35~07:37), multi-turn·turns → **"교대 근무"**(05:03, 14:05), traces orphaned → **"후속 조치는 아무런 도움도 되지 못했다"**(13:18), flag → **"국기"**(12:50), runs → **"처형"**(13:12), Pinecone → **"솔방울"**(10:08), `cat` → **"고양이"**(10:45), connective tissue를 가진 agentic search → **"수사관"**(16:03). 반전: *a year ago* → **"1년 후"**(02:17), *couldn't piece together how three functions interacted* → **"세 사람이 어떻게 상호작용했는지 연결할 수 있었다"**(15:34), 비용 원인 *made more searches* → **"더 많은 성과를 냈다"**(16:18), 맺음 *hopefully you learned a little bit* → **"거의 아는 바가 없습니다"**(17:35). `en` 단독: *"Cursor sent me this tweet"*(08:49 — 보낸 사람은 CEO). 수치(26·4배·20·100%/0%)는 세 트랙 모두 보존. 전체 목록은 raw.

> ⚠️ **작은 실험 — 화자가 먼저 말한다.** 데이터셋 *"like 20 different PRs"*(12:00~12:05)·*"like 20 different rows"*(17:09~17:11), 작업당 1회 시행(*"running multiple trials per task"* 를 놓친 모범 사례로 든다, 16:49~17:00), *"my vector search implementation was relatively weak"*(17:00~17:03), 저장소 하나(*"expand this uh to even different um different repos"* 17:11~17:16). **정확도는 숫자 없이 "same level"**, **"four times"의 비용 단위(달러·토큰·호출 수)는 미발화.** *"the point of this talk is not to create the best (…) eval ever, but it's more to illustrate to you the concept"*(17:18~17:27) — 화자 스스로 결과보다 **절차의 시연**으로 규정한다.
>
> ⚠️ **태스크와 채점이 맞물리는지 불명.** 태스크는 *"find the buggy code to locate where the logic the buggy logic lives"*(11:54~11:58)인데, 채점은 *"if the test uh passed the uh uh Microsoft TypeScript Go test suite, then it gets 100% and if it fails, it gets a 0%"*(14:34~14:45). 테스트 통과는 **수정**을 요구한다. 결과 해석도 *"how the agent should actually solve the bug"*(15:25~15:27)라고 한다. 에이전트가 수정까지 했는지는 발화되지 않는다.
>
> ⚠️ **Cursor 트윗 — 화자의 말이 자기 정의와 어긋난다.** *"cursor talks about how they used semantic search also known as agentic search um to significantly improve their coding agent uh performance"*(08:52~09:01). 그런데 화자 자신의 설명에서 semantic meaning을 담는 것은 **vector search의 임베딩**이다(*"embeddings basically represent the semantic meaning of that chunk of text or code"* 09:32~09:36). 말실수인지 트윗의 실제 내용인지 판단할 수 없다(트윗은 화면에만). **이 소스를 "Cursor가 X로 성능을 올렸다"의 근거로 쓰지 말 것.** 실험은 그 주장을 **재현하는 형태가 아니다** — CEO의 요청에서 출발한 별개의 비교다.
>
> ⚠️ **벤더 발표.** 04:36~05:51은 Braintrust UI·자연어 trace 질의·CLI·MCP 서버·SDK 소개다. 다만 **실험의 두 검색 방식은 Braintrust 제품이 아니고**, 결과는 Braintrust의 우열 주장이 아니다. Braintrust의 역할은 trace를 보는 도구(13:30~14:16)다.
>
> ⚠️ **행사·시점.** 행사명·도시 미발화. 설명란 `https://ai.engineer`·AI Engineer 링크·#AIEngineer → **[[ai-engineer|AI Engineer]] 계열 추정**(확정 아님). 손들기(00:20~00:28)로 현장 발표임을 알 수 있다. *"about a year ago, so April of 2025"*(02:14~02:17)는 화자의 어림이다.

## 1. 왜 eval인가 — vibes 대신 숫자 (00:00~02:46)

- 고객 통화에서 듣는 출시 근거: 엔지니어링이 준비됐다고 했거나 *"a PM said that they tried out a couple of prompts and they said it looked good"*(00:44~00:50). ⭐ *"essentially these teams are making ship decisions based off of vibes. Uh, which is not good."*(00:51~00:55)
- 듣고 싶은 문장: *"oh, I ran um 200 different test test cases and 94% of them passed and that's why we're shipping this feature."*(01:00~01:08) 또는 트레이드오프를 말하는 문장 — *"I shipped this feature that increased accuracy by 5% but actually decreased tone by 5%."*(01:10~01:14) ⚠️ 두 수치는 **예시 문장**이다.
- ⭐ 정의: *"it's just a way to answer questions about your AI system."*(01:20~01:24) 질문 목록 — 모델 선택(*"especially when there's new models dropping all the time"* 01:29~01:32), 언어·프로그래밍 언어별 차이(영어/일본어, Python/TypeScript, 01:38~01:51), *"cost efficiency (…) This is definitely becoming more topical now."*(01:51~01:56), 브랜드 일관성, 사용자 피드백, *"how do we know when something breaks or gets worse?"*(02:07~02:09)
- 사례: OpenAI의 2025년 4월 업데이트가 *"was supposed to make it more helpful, but actually made it sickopantic[=sycophantic] and therefore uh too agreeable and therefore less truthful."*(02:23~02:31) — eval이 그런 것을 *"catch"* 하게 돕는다(02:33~02:37), *"AI systems are so complex and undeterministic"*(02:37~02:43). ⚠️ 화자 진술, 출처 미제시.

→ [[skill-evals]](*"vibes based"* 에서 테스트로 — Bakaus) · [[verifiable-goals]]

## 2. eval의 네 요소 (02:49~04:20)

- *"eval comprised of four main things."*(02:54~02:56)
  1. **데이터셋** — *"the data that you're passing into your AI system and it usually includes things like uh your golden standard uh cases, your edge cases, your failure modes."*(02:59~03:11)
  2. **태스크** — *"a task defines how you want your AI system to behave when it takes in the input and produces an output. So concretely, this usually includes a system prompt and then the model"*(03:13~03:28)
  3. **채점** — *"a scoring system that will tell you whether the AI's output is good or bad"*(03:31~03:37), 기준은 보통 *"the PM or engineer"*(03:40~03:44)가 쓴다. 종류: *"deterministic scoring, LLM as a judge, human and review[=human review]"*(03:48~03:51)
  4. **실험** — *"the most fun part of writing evals"*(03:58~03:59). ⭐ *"every configuration of a specific data set a specific task and a specific scoring system equals to one experiment and as you are testing out different hypothesis for how to make your system better you're tweaking either your data set your task or your scoring system and these all lead to different experiments."*(04:02~04:20)
- 비교: 실험 1과 2를 놓고 *"improvements or regressions"*, 행 단위로 *"exactly which test cases have changed"*(04:26~04:36).

→ [[eval-experiment-anatomy]](신규) · [[eval-platform-maturity-stages]](Niazmandi의 "최소 eval 시스템 세 요소"와 대응 — 채점·실험이 분리된다)

## 3. Braintrust 제품 — 자연어 질의·CLI·MCP·SDK (04:36~05:51)

- *"this screenshot is from the brain trust UI"*(04:36~04:39). 자연어로 trace·실험 질의 — *"summarize my experiments for me (…) highlight the problems in these experiments"*(04:49~04:55). *"especially useful (…) traces with like long multi-turn conversations. It's good for um helping you catch things like hallucination or drift that's kind of hard to catch manually."*(04:55~05:10) 어느 실험이 가장 좋았는지도 묻는다(05:12~05:18).
- *"we also have a CLI and an MCP server if you prefer to do it that way"*(05:28~05:32).
- *"the last pillar of brain trust is just like regular observability"*(05:32~05:37) — SDK로 코드를 감싸 프로덕션 로그를 보내고 대시보드(05:37~05:51).

⚠️ 자사 제품 소개. 기능의 정확도·사례·수치는 없다. → [[braintrust]]

## 4. 관측과 eval의 순환, 팀 스포츠 (05:54~08:26)

- 예: AI 챗봇이 달린 새 문서 페이지를 어제 출시(06:08~06:22) → 프로덕션 로그 → *"sample a subset of them, maybe like 10 to 20 rows or something and create a kind of data set"*(06:35~06:42) → 태스크·채점을 바꿔 가며 eval → 배운 것으로 코드 변경 → 배포 → *"the whole flow repeats again because, uh, those changes will show up in your production logs"*(07:15~07:21).
- ⭐ *"I want to hammer into people that eval are a team sport."*(07:33~07:39) 역할: AI 엔지니어(코드 변경 + 데이터를 플랫폼으로), PM(*"I think they're they're usually spearhead eval at a company"* 07:55~07:59 — 성공의 가설, 프롬프트 조정), SME(*"insurance, medicine, law"* 08:12~08:15 — 라벨링·ground truth), 데이터 분석가.

→ [[production-trace-eval-flywheel]](Braintrust의 두 번째 서술 — 이번엔 사람이 도는 순환) · [[eval-platform-maturity-stages]](multi-persona) · [[taste-encoded-evals]]

## 5. 실험의 계기와 두 검색 방식 (08:29~11:08)

- 계기: *"my CEO Anker[=Ankur] sometimes goes on Twitter and sends me articles of things he wants me to eval."*(08:42~08:50) Cursor 트윗(⚠️ 위 박스 — *"semantic search also known as agentic search"*). *"I saw that there was a lot of uh discourse or discussion around this topic"*(09:08~09:12).
- **vector search**: 코드·텍스트를 임베딩으로 — *"embeddings basically represent the semantic meaning of that chunk of text or code"*(09:32~09:36), 늑대·개·고양이 vs 바나나·사과 그림(09:38~09:56), 벡터 DB(*"cqrant[=Qdrant] or pine cone[=Pinecone]"* 10:06~10:09), 질의 *"where does the database logic in my codebase live?"*(10:13~10:16)에 의미상 가까운 청크를 돌려준다.
- **agentic search**: *"works more like a human would"*(10:35~10:37) — *"you give an LLM tools like uh GP find lscat[=grep, find, ls, cat] um bash commands and it basically explores explores your codebase like a human would"*(10:39~10:51). 함수 이름 찾기 → 파일 열기 → 호출을 따라 다른 파일로 → *"until it's found what it's what it needs to"*(10:51~11:01).

→ [[agentic-search]] · [[reference-graph-vs-vector-search]] · [[retrieval-augmented-generation]](⚠️ 화자는 vector 쪽을 *"rag search"* 라고도 부른다, 11:52)

## 6. 데이터셋 · 태스크 · 채점 — 실험 설계 (11:11~14:47)

- **데이터셋**: *"Microsoft's TypeScript Go repo uh which is open source"*(11:20~11:23) → 제목에 *"fix"* 가 있는 머지 PR(11:25~11:31) → *"we basically checked out the parent commit. So essentially we checked out the commit to the point where it still has the bug in it."*(11:31~11:37) → *"we used Claude to generate a like a bug task or like a linear task based on the diff"*(11:37~11:45) → LLM이 *"rag search or a gentic search"* 로 버그 위치를 찾는다(11:50~11:58). 규모 *"like 20 different PRs"*(12:03~12:05).
- **태스크 = 하네스 고정**: agentic은 쉬웠다 — *"claude code uses agentic search by default. So we just set cloud code on these tasks."*(12:17~12:24) vector는 *"we still wanted to use the cloud code harness um to execute the vector search just to keep the experiment consistent"*(12:27~12:36). 두 가지로 기본 동작을 막았다:
  - 프롬프트에서 agentic search 금지(12:41~12:47) — ⭐ *"but if you've ever done this before, you know that prompting is never enough."*(12:45~12:50)
  - *"use the uh disallowed tools flag to prevent uh cloud code from calling certain things uh that it would normally use in a gentic search"*(12:50~12:58)
  - ⚠️ 막은 도구 목록, vector 검색을 Claude Code에 붙인 방식(MCP·커스텀 도구 등), 임베딩 모델·청크 크기는 발화되지 않는다.
- **고아 trace**: *"we ran the cloud code uh runs as subprocesses but it essentially mean meant that the traces were orphaned um and uh our solution was basically passing the parent span ids as environment variables."*(13:14~13:27) 고치기 전에는 *"run cloud agent"* 한 줄만 보이고 안이 보이지 않았다(13:40~13:52). 고친 뒤 *"all the turns, all the LLM calls uh every single terminal command that's being called like GP, bash, ls, fine[=find]"*(14:05~14:12). *"being able to have transparency into what's happening um is is important for debugging uh later on."*(14:19~14:27) ⚠️ 환경 변수 이름·SDK 쪽 처리는 발화되지 않는다(화면만).
- **채점**: TypeScript Go 테스트 스위트 통과 100%, 실패 0% — *"So it was very binary scoring here."*(14:34~14:47) ⚠️ 위 박스(위치 찾기 vs 수정).

→ [[hard-vs-soft-enforcement]](프롬프트 → 도구 차단) · [[claude-code]] · [[agent-harness-design]](같은 하네스로 변수 하나만 바꾸기) · [[field-level-unit-test-evals]](결정론적 채점)

## 7. 결과 — 같은 정확도, 4배 비용 (14:49~16:35)

- ⭐ *"vector search and as a aentic[=agentic] search both got the same level of accuracy, but essentially vector search cost uh four times more than agentic search."*(14:51~15:01)
- 해석은 trace를 손으로 읽어서 — *"when we looked at the actual traces and uh kind of manually like went through"*(15:04~15:09):
  1. ⭐ 청크가 맥락을 놓친다 — *"vector search uh returns back chunks of code but these chunks of code often miss things like um imports or tool calls or the calling code above it. Um and so as a result it's not enough it doesn't give enough context for how the agent should actually solve the bug."*(15:11~15:29) 한 행에서 *"the vector agent made 26 searches and still couldn't piece together how three functions interacted across the file."*(15:31~15:38)
  2. agentic은 사람처럼 — *"g[=grep] the function name, read the full function, uh spot the flaw and the logic and then follow the calling um calling logic uh into another file."*(15:44~15:54) ⭐ *"it felt like um, vector search gave a lot of proximity to the correct code, but agentic search had more of the connective tissue to connect the actual logic of those chunks of code."*(15:57~16:10)
  3. 비용의 원인 — *"it made more um searches because it was um constantly searching like returning a chunk of code and then searching again (…) and as a result um all of those LLM calls uh piled up"*(16:19~16:33)
- ⚠️ "26 searches"는 **한 행의 사례**이고, 평균 검색 횟수·agentic 쪽 호출 수는 발화되지 않는다. "same level of accuracy"는 몇 행 중 몇 행인지 없다.

→ [[file-discovery-tax]](고칠 자리를 찾는 비용이 방식에 따라 4배) · [[true-cost-to-perfect-answer]](비용 = 호출 누적) · [[reference-graph-vs-vector-search]](벡터가 못 주는 것 = 연결) · [[retrieval-not-reasoning-bottleneck]]

## 8. 한계 — 화자의 자기 평가 (16:36~17:43)

- *"you might be sitting here thinking, 'Oh, there's so many holes in this eval,' which is very fair."*(16:38~16:44)
- 놓친 것: 작업당 여러 번 시행(*"especially because LM[=LLMs] are so non-deterministic. It's good to run multiple trials to be able to trust the score"* 16:52~17:00), 더 나은 vector 구현(17:00~17:05), 데이터셋 확장(*"we only ran this on like 20 different rows"* 17:09~17:11, 다른 저장소로 17:11~17:16).
- *"the point of this talk is not to create the best uh off like the best eval ever, but it's more to illustrate to you the concept of the kind of how to create a eval to end[=end to end]."*(17:18~17:27)

## 이 위키와의 연결

### 이어지는 것

- **[[agentic-search]] · [[reference-graph-vs-vector-search]] — 첫 직접 비교.** 지금까지 "코딩 에이전트는 벡터를 안 쓴다"는 채택률 진술([[tech-bridge-graft-code-knowledge-graph|Graft 편]] — 당사자)과 정의·논증(Bergum·Clavié)이었다. 이 소스는 **같은 하네스, 같은 데이터셋, 검색 방식만 바꾼 실험**을 처음 내놓는다. 결과는 "벡터가 틀린다"가 아니라 **"같은 답에 더 비싸다"**이고, 이유로 든 것(*imports·calling code를 놓친다*, *connective tissue*)은 reference-graph 페이지 대비표의 *"답하지 못하는 것: 연결·방향·파급"* 과 같은 자리다. ⚠️ 20행·1회·약한 구현.
- **[[file-discovery-tax]]** — 태스크가 정확히 "고칠 자리를 찾는 것"이고, 비용 차이는 *찾는 단계의 반복*에서 왔다(16:19~16:33).
- **[[hard-vs-soft-enforcement]]** — *"prompting is never enough"*(12:47~12:50) → disallowed tools 플래그. 이 페이지의 원칙(잊을 수 있는 층에 강제를 맡기지 않는다)을 **eval 실험 통제**에 쓴 사례.
- **[[production-trace-eval-flywheel]] · [[eval-platform-maturity-stages]]** — 같은 회사의 두 번째 화자가 같은 순환(프로덕션 로그 → 10~20행 데이터셋 → eval → 배포)과 multi-persona(PM·SME)를 다시 말한다. Niazmandi가 *systems problem*(저장·쿼리)을 말했다면 Wang은 **입문 절차 + 손으로 trace 읽기**를 보여 준다.
- **[[skill-evals]]** — Bakaus의 *"it started you know vibes based"*(Impeccable)와 같은 출발점. eval을 *질문에 답하는 방법*으로 정의한다.

### 갈리는 것

> ⚠️ **긴장(약): 벡터 검색의 자리.** [[retrieval-primitive-repertoire]]·[[retrieval-augmented-generation]](2026-09-29 이후)은 벡터를 **도구 세트의 하나**로 남긴다. 이 실험은 벡터 *단독*(agentic 도구 차단)을 agentic *단독*과 비교했다 — **섞은 구성은 시험하지 않았다.** "벡터가 4배 비싸다"를 "벡터를 빼라"로 읽으면 실험 범위를 넘는다.

> ⚠️ **Cursor 쪽 주장과의 관계는 열려 있다.** 화자가 전한 Cursor 트윗은 *semantic search* 로 성능이 올랐다는 내용으로 소개되지만(08:52~09:01, 표현 자체가 혼동), 이 실험은 그것을 재현하지도 반박하지도 않는다 — 하네스(Claude Code)·저장소·태스크·지표가 다르다. [[cursor]] 페이지에 이 트윗을 사실로 적지 말 것.

## 해소하지 않고 표시만 한 것

- Cursor 트윗 원문·날짜, *"semantic search also known as agentic search"* 의 의도.
- 태스크가 위치 찾기인지 수정까지인지. 정확도 수치(몇 행 통과), 비용 단위(달러·토큰·호출 수), agentic 쪽 평균 검색 횟수.
- vector 구현 세부(임베딩 모델, 청크 단위, 벡터 DB, Claude Code에 붙인 방식), 차단한 도구 목록.
- 고아 trace 해결의 환경 변수 이름·SDK 쪽 처리(화면에만).
- OpenAI 2025년 4월 업데이트 서술의 출처.
- 행사명·도시·녹화일. CEO의 성(en-orig *"Anker"*, `en` *"Ankur"*).

## 등장 개체

- 인물: [[jess-wang|Jess Wang]](신규 제안 — 이름·소속·직함은 자막, 성은 설명란) · Braintrust CEO(en-orig *"Anker"*, ko·`en` "Ankur" — ⚠️ 성 미발화, 페이지 없음)
- 조직: [[braintrust|Braintrust]] · [[cursor|Cursor]](트윗 언급만) · [[openai|OpenAI]](아첨 업데이트 사례만) · [[microsoft|Microsoft]](TypeScript Go 저장소) · [[ai-engineer|AI Engineer]](⚠️ 설명란 링크만 — 추정)
- 제품·도구: [[claude-code|Claude Code]](하네스·disallowed tools 플래그) · Claude(태스크 생성) · TypeScript Go · Qdrant · Pinecone · Linear · grep/find/ls/cat — 페이지 없음
- 개념: [[eval-experiment-anatomy]](신규 제안) · [[agentic-search]] · [[reference-graph-vs-vector-search]] · [[retrieval-augmented-generation]] · [[retrieval-primitive-repertoire]] · [[retrieval-not-reasoning-bottleneck]] · [[file-discovery-tax]] · [[true-cost-to-perfect-answer]] · [[production-trace-eval-flywheel]] · [[eval-platform-maturity-stages]] · [[taste-encoded-evals]] · [[skill-evals]] · [[field-level-unit-test-evals]] · [[verifiable-goals]] · [[hard-vs-soft-enforcement]] · [[agent-harness-design]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=pLdgH-jLw5A> (17:46, `upload_date` 2026-10-15)
- raw: `01.raw/articles/2026-10-15_코딩 에이전트의 Agentic Search와 Vector Search, 직접 평가해봤습니다 — Braintrust.md`
- 설명란 링크: <https://www.braintrust.dev/> · <https://www.linkedin.com/in/jessica-wang-a1aa15ba/> · <https://x.com/daRubberDuckiee> · <https://ai.engineer> (⚠️ 열어 보지 않았다)
- 같은 회사의 앞 발표: [[tech-bridge-braintrust-eval-platform-systems-problem]]
- 코드 검색의 다른 증언: [[tech-bridge-graft-code-knowledge-graph]] · [[tech-bridge-bm25-agentic-search]] · [[tech-bridge-knowledge-agents-not-coding-agents]] · [[tech-bridge-sourcegraph-codebase-visibility]]
- [[tech-bridge]] · [[braintrust]] · [[jess-wang]]
