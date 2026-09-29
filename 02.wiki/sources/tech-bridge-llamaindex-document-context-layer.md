---
title: "Tech Bridge — AI 에이전트를 위한 문서 컨텍스트 레이어 (Jerry Liu · LlamaIndex, AI Engineer World's Fair 2026): 2026년의 RAG = 에이전트 하네스 + 컨텍스트 레이어"
type: source
tags: [rag, document-parsing, ocr, vlm, context-layer, agentic-search, benchmark, pareto, latency, extraction, llamaindex, ai-engineer, video]
source-url: https://www.youtube.com/watch?v=S-bRN-avZ4Q
source-type: video
author: Tech Bridge (한영자막 재배포) · 발표 [[jerry-liu]] ([[llamaindex|LlamaIndex]] 공동창업자·CEO — 자막은 "Jerry"뿐, 성·회사명은 제목·설명란) · [[ai-engineer|AI Engineer]] World's Fair 2026 (발화로 확정, 월·일 미확정)
date-published: 2026-09-28
ingested: 2026-09-29
created: 2026-09-29
updated: 2026-09-29
---

# Tech Bridge — AI 에이전트를 위한 문서 컨텍스트 레이어 (Jerry Liu · LlamaIndex)

[[tech-bridge|Tech Bridge]]가 재배포한 **20:33 무대 발표**(공식 챕터 11개). 화자는 RAG 프레임워크로 알려진 [[llamaindex|LlamaIndex]]의 공동창업자·CEO [[jerry-liu|Jerry Liu]]. 이 위키에 **RAG라는 말을 대중화한 프레임워크 쪽의 1인칭 소스가 처음 들어왔다** — 그리고 그 사람이 하는 말은 *"우리는 이제 RAG 프레임워크가 아니라 에이전트용 문서 인프라"* 다(01:02~01:07).

> **2026년의 RAG는 에이전트 하네스 + 컨텍스트 레이어로 분해된다. 검색의 복잡도는 에이전트 루프로 들어갔고, 남은 병목은 에이전트가 읽을 수 있는 형태의 컨텍스트 — 특히 PDF·PPT·Word·Excel에 갇힌 문서 — 이며, 그 파싱은 원샷 VLM이 아니라 하이브리드로, 그리고 에이전트 루프 안에서는 빠른 비-VLM 1차 파싱 + 필요한 페이지만 VLM으로 푼다.**

> *"RAG in 2026 … basically decomposes into an agent harness plus a context layer"* (00:30~00:36) · *"we do think context really is everything"* (05:20~05:24) · *"document understanding is definitely not 100% solved"* (14:39~14:41)

ASR·ko 보정: ko가 ***"extremely high accuracy, but also extremely low cost"* 를 "비용도 엄청나게 높습니다"로**(14:15~14:18), ***"not like terribly inaccurate"* 를 "몹시 부정확하기를 바라는군요"로**(15:42~15:44), ***"all the unstructured data"* 를 "모든 데이터는 아닙니다. 구조화되어"로**(06:03~06:07), *"changed quite dramatically"* 를 **"급격히 악화"** 로(02:04) 뒤집는다. *two and a half years* → **"1년 반"**(03:01), *claims* → **"불만을 제기할 때는 … 직접 처리하세요"**(07:37, 없던 명령문), *granular citations* → **"진료 예약"**(19:26), *reading order* → **"주문"**(09:34), *frontier models* → **"테두리 디자인"**(14:05), *scrolling* → **"배수량"**(19:53), *agentic* → **"작용제"**(15:26), *document* → **"다큐멘터리"**, *retrieval* → **"복구"**, *LLM* → **"법학 석사"**, *Gemini* → **"쌍둥이자리"**. 전체 목록은 raw 파일. **인용은 en-orig에서만** 했다(`en`은 *"documentary"*·*"parsbanch.ai"*·*"simple syntactic correction"* 에서 ko와 오류를 공유 — 독립 트랙 아님).

> ⚠️ **당사자 진술, 독립 확인 없음.** 화자는 LlamaParse(상용)·Light Parse(오픈소스)·ParseBench를 만든 회사의 CEO다. **ParseBench의 결과 수치는 자막에 하나도 없다** — 그래프는 화면에만 있고(*"even if you look at this graph"* 14:33~14:36), 자사 제품의 순위도 말하지 않는다. *"the fastest open source parser"*·*"the most accurate like Markdown parser"*(17:02~17:14)·*"will always be like much more accurate and cheap"*(12:06~12:11)는 측정 조건 없는 주장이다. 벤치마크의 제작자와 판매자가 같다.
>
> ⚠️ **화자 이름·회사명은 설명란에서.** en-orig는 *"everyone, I'm Jerry, co-founder and CEO"*(00:00) 뒤 *"of"*(00:01)에서 **회사명이 통째로 빠졌다.** **Liu**·**LlamaIndex**는 제목·설명란(X `jerryjliu0`, LinkedIn `jerry-liu-64390071` — ⚠️ 열어 보지 않았다). 자막 안의 방증: *"You might have seen us as a RAG framework. We started in 2023"*(00:55~00:58), 자사 상용 서비스 *"Lama Parse"*(13:00~13:02).
>
> ✅ **행사·연도 확정.** *"Really big shout out to the AI Engineer World Fair for hosting"*(00:08~00:10) · *"the previous AI Engineer conferences"*(00:12~00:15) · *"today in 2026"*(00:24~00:26). **이 채널 소스 중 처음으로 "AI Engineer"와 "World's Fair"가 한 구절에 묶였다** → [[ai-engineer]]. 트랙 발표(*"this track"* 07:57~07:59), 부스 *"LG47"*(20:22). 월·일은 발화 없음.
>
> ⚠️ **발표가 잘렸다.** 화자가 시간 초과로 *"what's next"* 절과 미탐구 영역을 건너뛴다(18:31~18:38, 20:04~20:05, 20:19~20:21). **마지막 챕터 제목의 "문서 검색의 미래"는 자막에 내용이 없다.** 추출·검색은 각 한 문단이다.

## 1. 2026년의 RAG — 하네스 + 컨텍스트 레이어 (00:50~04:55)

**3년 전 스냅숏**(01:26~01:58): *"naive RAG"* 는 *"you have some corpus of documents, you chunk it up, embed it, and put it into a vector database. You do some naive top K retrieval, and then you generate some stuff with an LLM. All the steps are fixed"*(01:40~01:53). → [[retrieval-augmented-generation]]

그 뒤 바뀐 것 셋:

| # | 변화 | en-orig |
|---|---|---|
| 1 | **검색 복잡도가 에이전트 층으로** — top-k의 한계를 우회하는 해킹 대신 에이전트가 키워드·검색어를 스스로 추론 | *"the retrieval complexity has started to get baked into the agent layer"*(02:29~02:33) · *"Even if the retrieval tools are basic, uh the agent can input the right queries to basically loop upon itself"*(02:48~02:54) |
| 2 | **컨텍스트가 스택 위로** — 초기 2년 반의 화두였던 컨텍스트 창 관리(compaction·long context)에서 **어떤 MCP 서버·스킬을 붙이느냐**로 | *"context is moving up the stack"*(02:55~02:57) · *"how do you just hook up the right MCP servers and skills and tasks to the agent"*(03:15~03:21) |
| 3 | **프로그래밍이 영어로** — 2023~2025년엔 Python·TypeScript로 정의했지만 이제 엔지니어든 GTM이든 영어로 run book을 쓴다 | *"more and more people are just building stuff uh using English"*(03:45~03:49) |

"현대의 범용 에이전트"로 *"Claude code, Claude code work[=Cowork], open claw, codex"*(02:24~02:28)를 든다 → [[claude-code]] · [[openclaw]] · [[codex]].

전망: 앞으로는 과제를 영어로 정의하는 것조차 아니라 *"more of the goal and a scoring rubric and then the agent will use all available context available to it to actually solve the task"*(04:47~04:54). → [[verifiable-goals]]

## 2. 컨텍스트가 전부다 — 문서라는 컨테이너 (04:57~06:35)

*"you could have a infinitely smart agent but your ability to actually get value out of this infinitely smart agent … is actually you know giving it the right things to do"*(05:24~05:37) — 과제·목표와 함께 **조직 컨텍스트 접근**: 웹 검색, 도구·스킬·MCP 커넥터, Snowflake·Databricks 웨어하우스, 그리고 *"the 90% of documents that are stored within SharePoint, Box, Dropbox, S3"*(06:00~06:04, ⚠️ 90%의 근거 없음).

*"We see documents as universal containers for unstructured context"*(06:17~06:22) — *"over 10 trillion plus pages of human native knowledge locked up within PDFs, PowerPoints, Word documents, and Excel sheets"*(06:22~06:27, ⚠️ 출처 없음). 동시에 에이전트는 *"more agent native formats in terms of markdown and HTML"*(06:33~06:34)을 기하급수적으로 만들어 낸다.

## 3. 에이전트 네이티브 문서 플랫폼의 세 층 (06:38~08:20)

→ [[document-context-layer]] (신규)

| 층 | 무엇 | en-orig |
|---|---|---|
| **파싱** | PDF·PPT·Word를 *"accurate, token-efficient context"* 로 — 마크다운·메타데이터 등 | 06:42~06:58 |
| **시맨틱·저장** | *"document management for humans and agents"* — 사람이 Word·파일 시스템을 여는 대신 **에이전트 인터페이스**가 문서를 담고 관리 | 07:01~07:20 |
| **반복 가능한 문서 워크플로** | 송장 처리·KYC·(보험) 청구 — *"instead of always offloading it to a generalized agent, how do you actually develop some sort of specialized workflow for it and really carefully tune cost and accuracy"* | 07:23~07:45 |

미해결 영역으로 **에이전트 네이티브 문서 포맷 · 문서 버전 관리 · 문서 편집 · *"hill climbing as a service"*** 를 든다(08:02~08:10) — 전부 시간 관계로 건너뛰었다.

## 4. 문서 OCR이 어려운 이유 (08:22~10:40)

→ [[document-parsing-for-agents]] (신규)

- **PDF는 표시용이다** — *"it's rendered for kind of like display purposes, um and not really for uh you know, machine consumption"*(08:48~08:54), *"they're designed for printing"*(08:57~08:58).
- **텍스트는 좌표 붙은 글리프** — *"text are represented as almost like individual glyphs with coordinates"*(08:58~09:03).
- **표는 표가 아니다** — *"they're represented as like typically line segments uh drawn with various types of borders, and also text drawn at certain cell positions"*(09:05~09:11).
- **읽기 순서 보장 없음** — 다단 레이아웃에서 PDF 안의 순서가 사람이 읽는 순서와 맞는다는 보장이 없다(09:37~09:50).
- **Word·PPT도 어렵다** — 구조는 더 있지만 *"custom bespoke XML format"*(09:59~10:01)에 *"a ton of like fluff"*(10:07~10:09). 태그를 무시하고 렌더링된 구조를 보게 해야 하며, *"a lot of uplift you can get by actually parsing it into a more interpretable format instead of just using the native uh, OXM[=OOXML]"*(10:32~10:37).

## 5. 파이프라인 · 원샷 VLM · 하이브리드 (10:41~13:00)

| 접근 | 화자의 평가 |
|---|---|
| **휴리스틱·파이프라인** — 텍스트를 군집화해 표·문단 식별, PyPDF·PyMuPDF 등(10:46~11:14) | 기본 기법 |
| **원샷 VLM** — *"using a VL[M] to one-shot a document um, into text"*(11:16~11:19) | 시각 구조를 읽는 이득은 있지만 *"It can hallucinate on text only pages. It costs a ton of money."*(11:34~11:36), *"it still lacks a lot of the semantics and grounding"*(11:38~11:41) |
| **하이브리드** — 파일 컨테이너·바이너리를 깊이 이해하는 파이프라인 + 비전 | *"at the Pareto frontier of cost and accuracy"*(11:56~11:59) — **당사자 주장** |

**"항상"이라는 주장**: *"the Pareto frontier for document OCR will always be like much more accurate and cheap compared to the Pareto frontier for, you know, wherever the frontier models are"*(12:06~12:15). 근거는 *"it's a very specific data type and there's always ways to kind of like distill the latest visual understanding capabilities from, you know, Gemini, GPT, Opus into kind of a carefully tailored workflow"*(12:15~12:28). ⚠️ [[ride-the-optimization-trajectory]](*프런티어가 최적화하는 방향 위에 시스템을 얹으면 모델이 바뀔 때마다 공짜로 좋아진다*)와 **같은 궤적을 다르게 쓰는** 논증이다 — 프런티어 위에 **얹는** 대신, 프런티어를 **증류해 특화 계층이 늘 한발 앞선다**고 본다. 프런티어가 올라가면 증류할 원천도 같이 올라간다는 것. 측정은 없다.

**LlamaParse**(13:00~13:04, 상용)의 구성(12:34~12:57): ① PDF 엔진 + Word·PPT 최적화 ② *"an agentic harness that's like carefully tuned for auto routing between cheaper specialized models to frontier models"*(12:41~12:47) ③ *"specialized fine-tuned document VLMs that are parameter efficient"* — 표·차트 등 요소 클래스별(12:48~12:57). → [[llamaindex]]

## 6. ParseBench (13:04~14:50)

기업의 문서 롱테일(금융·보험·제조·법률·정부, 13:15~13:19) 앞에서 *"most of the models are not up for the task"*(13:28~13:29). 그래서 만든 벤치마크:

- *"2,000 human verified pages. It measures tables, charts, content faithfulness, semantic formatting"*(13:39~13:46)
- ⭐ **평가 기준이 구문이 아니라 에이전트의 이해** — *"optimized for just how AI agents are actually able to understand these documents instead of like syntactic correctness"*(13:47~13:53). ⚠️ ko(와 `en`)는 이 대비를 *"간단한 구문 오류 수정"* 으로 뒤집었다.
- 공개: *"parsebench.ai"*(13:55), Hugging Face·Kaggle(14:02~14:03) → [[hugging-face]]
- 대상: *"probably like 50 different frontier models, open way[=weight] models, specialized OCR solutions"*(14:04~14:08). ⚠️ 설명란·챕터의 *"50개 이상 최신 모델"* 은 자막보다 세다 — **"아마 50개 정도", OCR 솔루션 포함.**
- 목표: 곡선이 *"towards the left and up"* — *"extremely high accuracy, but also extremely low cost"*(14:10~14:17). 문서 난이도 분포가 다양하므로 **곡선 위의 모든 점을 덮어야** 한다(14:20~14:31).

## 7. 세 처리 영역 (14:54~16:44)

*"accuracy cost latency Pareto curve"*(14:56~14:58) 위의 세 점. → [[document-parsing-for-agents]]

| 영역 | 누가 | 화자의 말 |
|---|---|---|
| **고정확도** | 보험·금융 등 규제 산업 — *"99 to almost 100% accuracy"*(15:04~15:06) | 오추출의 대가가 재무 모델 붕괴·사기 플래그(15:06~15:15). 페이지당 더 내고 *"deeper agentic reasoning"*(15:22~15:25) |
| **저비용** | SharePoint에서 매일 갱신되는 *"million plus documents uh per day"* 를 RAG 지식 베이스용으로 인덱싱(15:32~15:41) | ⭐ *"even if it's a little bit messed up, it's okay, too, because in the end if you have a sufficiently good agent, it can always dive deeper into the document and surface the right information with the right citations and grounding"*(15:44~15:54) |
| **초저지연** | 실시간 업로드 — *"let's say you're using Cloud Co-work[=Claude Cowork], you upload a thousand documents and you need to process it within a minute"*(16:13~16:18) | VLM으로는 *"really tough for basically every single OCR service out there. Um, and and to be fair, that includes ours, too"*(16:23~16:28) |

> **저비용 영역의 논리가 이 발표의 가장 흥미로운 문장이다.** 인덱싱 품질의 부족을 **에이전트가 원문으로 다시 들어가 메운다** — 파싱 품질과 에이전트 능력이 **대체재**라는 주장이다. → [[tiered-document-parsing]] · [[agentic-search]]

## 8. 에이전트 루프 안의 파서 — "Light Parse" (16:44~18:10)

*"that's what I call kind of being in the agent loop"*(16:44~16:46). LlamaParse 외에 **Light Parse**(en-orig 표기, 설명란 *"LightParse"*, ⚠️ 공식 철자 미확인)를 만들었다:

- *"it is Rust based. Um, it is the fastest open source parser out there. It is completely free"*(16:59~17:04), *"I think it's like MIT or Apache license"*(17:07~17:09, 화자도 불확실)
- *"the most accurate like Markdown parser out there that doesn't use a VLN[=VLM] or any sort of kind of like deeper model"*(17:10~17:16) — ⚠️ 당사자 주장, 측정 없음

**사용 패턴** → [[tiered-document-parsing]] (신규):

> *"what these agents will do is they'll do like a fast pass over all the documents first kind of like just scan through all the contents extremely efficiently. And then if actually needs to dive into a page with like tables, with like charts, and actually needs to more deeply understand the values, it'll use a VLM based tool, slower processing"* (17:37~17:57)

Claude Code·Claude Cowork·Codex에 PDF 천 개를 올리는 상황(17:22~17:31), 기본값으로 Light Parse, VLM 기반 파서(LlamaParse 또는 프런티어 모델)는 **도구로** 장착(17:31~17:37). *"available as a one-click installable skill"*(17:59~18:01) → [[agent-skills]]

## 9. 추출과 검색 — 한 문단씩 (18:41~20:03)

- **추출**: 송장·경비·영수증·청구 백만 건에서 구조화 출력(18:45~19:00), 사람의 서류 스캔·데이터 입력 자동화(19:02~19:17). LlamaParse 안에서 *"granular citations all the way back to the source document for every extracted output"*(19:28~19:31), *"confidence scores"*(19:35), 값이 확실한지 **플래그한 뒤 시스템에 넣을지 결정**(19:39~19:43).
- **검색**: *"basically expanded tool set as I mentioned around retrieval, BM25, grep, vector search, reading and scrolling"*(19:48~19:52) → [[retrieval-primitive-repertoire]] · [[bm25]]

## 기존 위키와의 대조

### 합치하는 것

- **검색은 에이전트 루프 안으로** — [[agentic-search]]([[jo-bergum|Bergum]], 09-21)의 정의와 같은 방향. Liu는 한 걸음 더 가서 *"retrieval tools are basic"* 이어도 된다고 본다(02:48). **엔진 품질**을 병목으로 본 [[will-bryk|Bryk]]([[exa|Exa]], 09-22)와는 반대편이다.
- **RAG의 역사 서술** — [[tech-bridge-agent-to-agent-as-search]]의 *수동 → RAG → 에이전틱 검색* 3단계와 합치한다. 이번엔 **RAG를 만든 쪽**의 서술이다.
- **컨텍스트에 투자하라** — [[tools-and-context-over-harness]]([[ryan-lopopolo|Lopopolo]])의 *하네스는 고정, 도구·컨텍스트에 투자*와 같은 분해. Liu는 그 **컨텍스트 쪽을 파는** 벤더다.
- **워크플로는 남는다** — [[workflow-vs-agent]]: 반복 가능한 문서 처리는 범용 에이전트가 아니라 비용·정확도를 조율한 전용 워크플로로(07:33~07:45).
- **지연이 설계를 가른다** — [[search-latency-tiers]]의 200ms/분 단위 티어에 **파싱 쪽 짝**이 생겼다. 해법은 빠른 VLM이 아니라 **VLM을 빼고, 필요할 때만 부른다**.

### 갈리는 것

> ⚠️ **Contradiction: PDF를 비전으로 읽으면 되는가.** [[mixedbread|Mixedbread]]([[benjamin-clavie|Clavié]], 09-21)는 PDF를 **OCR 없이 비전으로** 읽어 표까지 검색에 넣으면 정확도가 *"크게 뛴다"* 고 했다(13:17~13:38). Liu는 원샷 VLM이 **텍스트 전용 페이지에서 환각하고, 비싸고, grounding이 부족하다**며(11:34~11:41) 하이브리드를 판다. **둘 다 당사자**이고 층이 다르다(Mixedbread는 **검색**용 표현, Liu는 **파싱 출력**). 어느 쪽도 상대 방식과 비교한 수치를 자막에 내지 않는다.

> ⚠️ **Contradiction: 인덱싱 품질은 얼마나 중요한가.** [[retrieval-side-context-compression]]([[exa|Exa]])는 엔진이 **한 번에 압축된 답**을 주는 쪽에 건다. Liu의 저비용 영역은 반대로 *"a little bit messed up"* 인덱스를 **에이전트가 원문으로 되돌아가** 메운다고 본다(15:44~15:54). 앞쪽은 에이전트를 **소비자**로, 뒤쪽은 **재조사자**로 둔다 — [[agentic-search]]의 09-22 절 *"이 소스에는 궤적이 없다"* 와 같은 축.

- **특화 계층은 모델 발전에 먹히는가** — 위 5절. Liu는 *"will always be"* 라며 증류로 앞선다고 본다. [[ride-the-optimization-trajectory]]가 *범용 프리미티브(bash·grep) 위에 얹어라* 라고 할 때, Liu는 **파싱만큼은 범용 모델이 아니라 특화 계층**이라고 한다 — 모순이라기보다 **어느 층을 특화로 남기느냐의 긴장**이다. 둘 다 측정이 없다. ⚠️ 위키의 정리.

## 해소하지 않고 표시만 한 것

- **ParseBench 결과 전부** — 순위·수치·LlamaParse의 위치가 자막에 없다(그래프는 화면). 벤치마크 제작자 = 판매자.
- **"Light Parse" 철자** — en-orig *"Light Parse"*, 설명란 *"LightParse"*. 공식 이름(Light/Lite)과 저장소를 확인하지 않았다. 라이선스는 화자도 *"MIT or Apache"* 로 불확실.
- **"fastest"·"most accurate"·"always more accurate and cheap"** — 측정 조건 없음.
- **"10 trillion plus pages"**(06:22) · **"90% of documents"**(06:00) — 출처 없음.
- **"We started in 2023"**(00:56) — 화자 발화 그대로. 외부 확인 안 함.
- **"a blog post that we put out a few months ago"**(08:32~08:34) — 제목·링크 없음, 열어 보지 않았다.
- **시맨틱·저장 층의 실체** — 정의 한 문단(07:01~07:20)과 추출·검색 한 문단씩이 전부. *"agent interface"* 가 무엇인지(MCP인지, 파일 시스템인지) 말하지 않는다 → [[corpus-as-filesystem-workspace]]와의 관계 미확정.
- **"hill climbing as a service"·에이전트 네이티브 문서 포맷·버전 관리·편집** — 이름만, 내용은 생략.
- **"what's next"** — 건너뜀. 슬라이드는 *"I'll share the full set of slides online"*(18:38~18:39) — 이 위키는 찾지 않았다.
- **보안·권한** — SharePoint·Box·Dropbox·S3의 문서를 에이전트에 여는 이야기를 하면서 접근 제어·[[prompt-injection]](문서에 심긴 지시)은 한 번도 나오지 않는다.
- **월·일** — 연도(2026)와 행사(AI Engineer World's Fair)만 확정.

## 등장 개체

- 인물: [[jerry-liu]] (신규)
- 조직: [[llamaindex]] (신규) · [[ai-engineer]] · Snowflake · Databricks · Microsoft(Word·PowerPoint·SharePoint) · Box · Dropbox · [[hugging-face]] · Kaggle
- 제품·도구: LlamaParse · "Light Parse" · ParseBench (→ [[llamaindex]]) · [[claude-code]] · Claude Cowork · [[codex]] · [[openclaw]] · PyPDF · PyMuPDF · Gemini · GPT · Opus · S3
- 개념: [[document-context-layer]] (신규) · [[document-parsing-for-agents]] (신규) · [[tiered-document-parsing]] (신규) · [[retrieval-augmented-generation]] · [[agentic-search]] · [[retrieval-primitive-repertoire]] · [[bm25]] · [[search-latency-tiers]] · [[workflow-vs-agent]] · [[tools-and-context-over-harness]] · [[context-engineering]] · [[model-context-protocol]] · [[agent-skills]] · [[verifiable-goals]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=S-bRN-avZ4Q> (20:33, `upload_date` 2026-09-28)
- raw: `01.raw/articles/2026-09-28_AI 에이전트를 위한 문서 컨텍스트 레이어 구축하는 법 — Jerry Liu, LlamaIndex.md`
- 설명란 링크: <https://x.com/jerryjliu0> · <https://www.linkedin.com/in/jerry-liu-64390071/> (⚠️ 열어 보지 않았다)
- 같은 주제: [[tech-bridge-bm25-agentic-search]] · [[tech-bridge-knowledge-agents-not-coding-agents]] · [[tech-bridge-exa-perfect-search-for-agents]] · [[tech-bridge-agent-to-agent-as-search]]
- [[tech-bridge]] · [[jerry-liu]] · [[llamaindex]] · [[ai-engineer]]
