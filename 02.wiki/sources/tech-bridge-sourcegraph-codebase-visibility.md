---
title: "Tech Bridge — AI 코딩 에이전트가 거대한 코드베이스를 망가뜨리고 있습니다 (Dan Adler · Sourcegraph): 코드의 양이 문제다, 보이지 않는 것은 grep할 수 없다, Visibility is infrastructure"
type: source
tags: [codebase-scale, legacy, code-knowledge-graph, agentic-search, large-scale-code-changes, multi-repo, sourcegraph, vendor-pitch, anonymous-quotes, video]
source-url: https://www.youtube.com/watch?v=oeL0uP-NO-U
source-type: video
author: Tech Bridge (한영자막 재배포) · 발표 [[dan-adler]] ([[sourcegraph|Sourcegraph]] — 이름·직함 CEO는 제목·설명란에만, 자막엔 회사명 "source graph"만) · 행사명 미발화(설명란 링크로 AI Engineer 계열 추정), 녹화일 = Agentic Batch Changes 베타 공개일(날짜 미확인)
date-published: 2026-10-06
ingested: 2026-10-09
created: 2026-10-09
updated: 2026-10-09
---

# Tech Bridge — AI 코딩 에이전트가 거대한 코드베이스를 망가뜨리고 있습니다 (Dan Adler · Sourcegraph)

[[tech-bridge|Tech Bridge]]가 재배포한 **10:51 발표, Q&A 없음, 공식 챕터 15개, 앞뒤(자기소개·마무리)가 잘린 편집본.** 화자는 [[sourcegraph|Sourcegraph]]의 [[dan-adler|Dan Adler]](이름·CEO 직함은 제목·설명란에만). **문제 제기 + 자사 제품 소개**다 — 전반 2/3는 *대기업의 거대한 레거시 코드베이스가 에이전트가 쏟아내는 코드의 양에 무너지기 시작했다*는 진단, 후반 1/3은 그 해법으로 코드 그래프와 당일 베타 공개한 **Agentic Batch Changes**. 데이터는 없고, 근거는 72% 통계 하나(출처 미발화)와 익명 임원 인용 둘이다. 이 위키의 [[code-knowledge-graph]]에 **엔터프라이즈 규모(수만~수십만 저장소)라는 축**이 처음 들어왔고, 여러 저장소에 걸친 일괄 변경이 개념으로 생겼다 → [[large-scale-code-changes]] (신규).

> **세상을 돌리는 소프트웨어는 새롭지도 깨끗하지도 않은, 수천 명이 수십 년 쌓은 거대한 코드베이스다. 에이전트가 만든 코드의 해일 속에서 그 코드베이스들이 부패하기 시작했고 — 원인은 에이전트의 품질이 아니라 코드의 양이다. 에이전트는 grep으로 코드베이스를 이해하는데, 보이지 않는 것은 grep할 수 없다. 5만 저장소를 보고 이해하는 인프라는 모델 회사들이 만들지 않는다. 가시성이 인프라다.**

> *"The job of owning a codebase is harder today than it has ever been before."* (03:36~03:43) · *"the problem here is actually the volume of code. The call is coming from inside the house"* (03:46~03:54) · *"Sure, Claude Code can uh make this change, but I have 90,000 repositories to make it in."* (06:24~06:28) · *"But understanding is a context problem. You can't gp[=grep] what you literally cannot see."* (07:31~07:36) · *"Visibility is infrastructure."* (08:55~08:57)

ASR·ko 보정: ko가 챕터 제목이 된 핵심 인용 *"I don't know what this code does. AI wrote it for me."* 를 **"저는 이 코드가 무슨 일을 하는지 알고 있습니다. 일체 포함 …"으로 뒤집었고**(04:24~04:26, *AI* → "일체 포함"), *Few of your peers work at startups* 를 **"상당수가 스타트업에서 일하고 있습니다"로**(00:39~00:44), 인과의 핵심 *the tools that are creating the conditions* 를 **"절대로 생성되는 코드가 아닙니다"로**(03:56~04:05) 뒤집었다. *agentic coding tools* → **"자영업 여성들"**(00:11), *he ran this* → **"그는 그를 처형했다"**(10:19), 마지막 문장에 **없는 "이 책"**(10:45). `en`의 오류가 ko로 넘어간 자리가 넷 — *single prompt* → "알림"(09:20), *grep* → "AI"(02:50), *PR* → "추출 요청"(09:28), *agents.md* → ".mmd 파일"(07:18). en-orig는 grep을 *"GP"*, 해일(tidal wave)을 *"title wave"*, Mercari를 *"Merkari"* 로 들었다. 전체 목록은 raw. **인용은 en-orig에서만** 했다.

> ⚠️ **근거가 얇고 이해관계가 있다.** 수치는 *"72% of software industry employment is in companies with more than 500 people"*(00:28~00:30) 하나이고 출처 미발화. 나머지는 **익명 인용**(상위 10위 자동차 제조사 임원, 상위 10위 미국 은행 기술 리더)과 자사 얼리 액세스 사용자 사례(Mercari)다. 코드베이스가 *"beginning to decay"*(02:42) 한다는 핵심 주장에 **측정치가 없다.** 그리고 *"The infrastructure to see and understand a 50,000 repo codebase is not being built or sold by OpenAI, by anthropic, by cursor"*(05:00~05:10)는 **자사 시장의 경쟁 구도 진술**이다 — 진단 전체가 자사 제품으로 수렴한다.
>
> ⚠️ **화자·행사·시점.** 자기소개가 잘려 이름 *Dan Adler*·직함 *CEO*는 **제목·설명란에만** 있다(자막엔 *"what we're working on as a company. This is what source graph is built around"* 07:56~08:01). 행사명 미발화 — *"around this room right now"*(02:11~02:13)와 설명란의 `ai.engineer` 링크로 **AI Engineer 계열 추정**. 시점 단서는 ⭐ *"just today we launched our new um our new agentic batch changes product into beta"*(09:03~09:08) 하나 — 녹화일은 그 베타 공개일인데 **이 위키는 공개일을 확인하지 않았다**(설명란 블로그 링크 미열람). 업로드는 2026-10-06. 연·월 발화 없음.

## 1. 세상을 움직이는 것은 오래된 코드다 (00:00~01:44)

- 주제: *"the unglamorous but loadbearing work of owning a large complex codebase and why AI and agentic coding tools today make that job more difficult and more important than ever before"*(00:00~00:14).
- *"the software that runs the world is not pretty. It's not new. It's not clean. It's how everything actually works."*(00:17~00:26)
- ⭐ *"72% of software industry employment is in companies with more than 500 people"*(00:28~00:30) — 수천 저장소·수십 년 이력을 관리하는 회사들. 스타트업·1인 창업자는 소수, *"Most of us work in large longived[=long-lived] code bases."*(00:51~00:54) ⚠️ 출처 미발화.
- 예시 나열 — 은행 실시간 거래 거절, 보험 이중 보장 환급률, 아마존 창고 스캐너, Uber 도착 예정 시간, 항공기 레이더 궤적, 급여, 사무실 에어컨(00:54~01:22).

→ [[legacy-code-modernization]] · [[greenfield-vs-brownfield-agent-risk]]

## 2. 코드의 해일과 코드베이스의 부패 (01:44~03:37)

- *"coding agents are writing more better code today, faster than we have ever seen before. A title wave[=tidal wave] of code is coming for you."*(01:44~01:52) — 화자는 **에이전트 코드의 품질을 탓하지 않는다.**
- AI 생성 코드의 홍수를 리뷰해야 하고 *"we're exhausted by it"*(02:02~02:09). 코드 리뷰 에이전트·코드베이스 건강 측정 도구·더 나은 모델은 ⭐ *"sandbags"* 이고 *"local maxima"* 다(02:09~02:31) → [[automated-code-review]]를 **국소 해법**으로 내린다.
- *"these code bases (…) are beginning to decay"*(02:35~02:42). 이유:
  - 규모 — *"millions of lines of code, tens of thousands of repositories, way too much to fit into a context window or even just to clone and GP[=grep] in real time"*(02:43~02:52)
  - 에이전트마다 다른 코딩 표준(03:00~03:04)
  - ⭐ 중복 코드 — *"You you already have a library that does this, but your agent doesn't know that."*(03:07~03:10) → [[duplicate-code]]
  - 서비스 간 의존성 취약화, 표준의 미세한 이탈이 만드는 숨은 문제(03:13~03:20)
  - 취약점 — *"new vulnerabilities being uncovered by agents every single day"*(03:23~03:26), 레거시 코드베이스의 *"constant oversight and upkeep"*(03:29~03:36)

> ⚠️ 이 목록에 **데이터가 하나도 없다.** 설명란의 *"AI 생성 코드와 중복·표준 이탈·취약점의 관계"* 는 발화에선 나열이다.

## 3. 원인은 코드의 양, 그리고 "AI가 썼어요" (03:37~04:50)

- ⭐ *"the problem here is actually the volume of code. The call is coming from inside the house, right? The very tools that are speeding all of us up (…) are also the tools that are creating the conditions that will cause these massive code bases that run our world to begin to fail."*(03:46~04:05)
- 상위 10위 자동차 제조사 임원(익명): *"I want to give my devs the best tools possible. But just today, I overheard a dev say, 'I don't know what this code does. AI wrote it for me.'"*(04:17~04:26). 자율 주행(*"vehicle autopilot"*) 코드를 쓰는 수천 명 조직에서 *"this is terrifying"*(04:31~04:37). ⚠️ **이중 전언** — 개발자의 말을 임원이 엿듣고 화자에게 전했다.

→ [[cognitive-debt]] · [[ai-slop]]

## 4. 개발 도구 회사들에게 (04:50~06:13)

- *"these codebase owners deserve better. Today's agentic dev tools are not meeting the moment"*(04:50~04:58).
- ⭐ *"The infrastructure to see and understand a 50,000 repo codebase is not being built or sold by OpenAI, by anthropic, by cursor, by the rest of them."*(05:00~05:10) 그들의 에이전트는 대부분의 개발자가 매일 겪는 **소규모 문제**에 너무 뛰어나서 수요가 폭증하고, 큰 문제는 *"going unnoticed"*(05:10~05:28).
- 호소 둘: 코드베이스 소유자들에 대한 감사(05:30~05:45), 그리고 *"a call to dev tools companies out there, to the agent harness builders"* — 대규모 저장소를 보고 이해하는 능력을 에이전트에게 주라(05:47~06:04). → [[harness-engineering]]

## 5. 저장소 9만 개 (06:13~07:02) → [[large-scale-code-changes]] (신규)

- 상위 10위 미국 은행 기술 리더(익명, *"Tens of trillions of dollars in assets uh in custody or administration"* 06:16~06:22): ⭐ *"Sure, Claude Code can uh make this change, but I have 90,000 repositories to make it in."*(06:24~06:28) — 특정 npm 공급망 취약점에 관한 말(06:30~06:35, 사건 미발화).
- 에이전트가 취약점을 *"uncover and create"* 하는 속도(06:38~06:45) 앞에서 [[claude-code|Claude Code]]를 쓰라는 처방은 *"Good luck doing that in 90,000 repositories, mapping out how these code bases all come to together, what's actually living in production"*(06:49~06:59).

→ [[claude-code]] · [[ai-vulnerability-discovery]]

## 6. 에이전트는 검색으로 이해한다 — 보이지 않는 것은 찾을 수 없다 (07:02~08:04)

- ⭐ *"if we know anything about LLMs is that they just love to search. It's like a new hire getting up to speed on the codebase. It's how agents build models of the world."*(07:05~07:15)
- ⭐ *"The repo architecture that you're plugging into your agents.mmd[=AGENTS.md] files, like let's be real, that's barely moving the needle here. This agent is going to GP gp gp gp gp gp its way to codebase understanding."*(07:15~07:26)
- ⭐ *"But understanding is a context problem. You can't gp what you literally cannot see."*(07:31~07:36) 500·5,000·5만·50만 저장소 규모의 *"see and search and really deeply understand"* 인프라는 *"not being built by the agent builders today"*(07:38~07:51). → Sourcegraph가 하는 일(07:56~08:01).

→ [[agentic-search]] · [[file-discovery-tax]] · [[code-only-index-blind-spot]]

## 7. 코드는 더 늘어난다 · 코드 그래프 (08:04~09:03)

- 예측: *"These massive code bases are not going away. In fact, there will be more code. There will be much much much more code"*(08:10~08:19).
- ⭐ 해법의 정의: *"having a graph that code graph in mind. The foundational graph of your codebase including search and then the actual compiler accurate output"*(08:36~08:44) → 에이전트가 변경을 효과적으로 하는 데 필수, ⭐ *"Visibility is infrastructure."*(08:55~08:57)

→ [[code-knowledge-graph]] · [[reference-graph-vs-vector-search]]

## 8. Agentic Batch Changes · Mercari (09:03~10:46)

- *"just today we launched our new um our new agentic batch changes product into beta. This is a frontier agent"*(09:03~09:11) — 거대한 코드베이스의 소유자가 *"execute code changes across hundreds or thousands of repositories at once starting with a single prompt"*(09:11~09:20).
- 동작(화자 진술, 09:22~09:41): 변경을 **반복적으로 롤아웃** · CI 상태와 PR 코멘트에 **자가 수정**(*"Self-heal"*) · ⭐ *"Use coding agents where it makes sense, where judgment is needed. Use deterministic scripts where it's not."* · *"tracking and auditability to be sure that you've covered 100% of the places where that patch is needed"*.
- **Mercari 얼리 액세스 사례**(10:00~10:44): 수백 개 마이크로서비스. GitHub 코드 인젝션 이슈(*"where you have to set environment variables correctly"*)를 아는 저장소 2곳에 먼저 돌리고 *"go explore the rest of our codebase"* → **잠재 취약점 80개** 추가 발견. *"This is like bas this is like config files"* — 결정론적 스크립트로 한 번에 일관되게 패치.
- 마지막: *"That is what confidence is all about in the agent coding era."*(10:44~10:46)

> ⚠️ **Mercari 수치.** 2곳 + 80 = 82인데 이어서 *"across 100 of the places where that risk exists"*(10:39~10:44). 09:37의 *"100% of the places"* 처럼 **"100%"의 ASR 탈락**일 수 있다 — 미확정. 그리고 80개는 *"potential"* 이며 설정 파일 수준이다. 사용자 이름 미발화, 자사 고객 사례.

## 이 위키와의 연결

### 이어지는 것

- **[[code-knowledge-graph]]** — 이 위키의 그래프 계보는 *사람이 보는 그래프*([[understand-anything]]) → *에이전트가 조회하는 인덱스*([[graft]], 단일 저장소)였다. Adler는 같은 구조를 **수만~수십만 저장소 규모의 인프라**로 놓고, 노드의 질을 *"compiler accurate"* 로 정의한다. [[james-ai-explorer-understand-anything|한국어 블로그]]가 Understand-Anything의 비교 대상으로 들었던 Sourcegraph가 **직접 화자로** 들어왔다.
- **[[agentic-search]] · [[file-discovery-tax]]** — *"LLMs (…) just love to search"*, *"GP gp gp gp its way to codebase understanding"* 는 탐색세의 서술과 같다. 다만 Graft 편은 **턴 수·토큰**을, Adler는 **애초에 검색 범위 밖에 있는 코드**(clone조차 안 되는 규모)를 문제 삼는다 — 비용의 문제가 아니라 **가시성의 문제**.
- **[[legacy-code-modernization]]** — *"아무도 완전히 이해하지 못하는 핵심 인프라"* 에 *"I don't know what this code does. AI wrote it for me."* 가 붙는다 — **새로 쓰인 코드가 처음부터 레거시가 되는** 경로.
- **[[codebase-gardening]]** — *"이미 라이브러리가 있는데 에이전트는 모른다"*, 에이전트마다 다른 표준은 Lauren Tan의 *"안티패턴은 바이러스처럼 퍼진다"* 와 같은 현상을 **저장소 경계 너머**에서 본 것이다.
- **[[verification-bottleneck]]** — 리뷰 피로를 인정하되(*"we're exhausted by it"*), 리뷰 에이전트를 *"sandbags"*·*"local maxima"* 로 내린다. 병목을 **리뷰 이전의 가시성**으로 옮기는 다섯 번째 진단.

### 갈리는 것

> ⚠️ **Contradiction: 브라운필드는 에이전트에게 안전한가.** [[greenfield-vs-brownfield-agent-risk]]의 Lauren Tan — *대기업 인프라는 이미 가드레일이라 레거시 코드베이스가 오히려 안전하다.* Adler — *바로 그 대기업의 거대한 레거시 코드베이스가 에이전트 코드의 양에 부패하기 시작했다.* 둘의 전제가 다르다: Tan은 **잘 세팅된 단일 저장소의 가드레일**, Adler는 **수만 저장소에 걸친 가시성 부재**. 위키의 독해: Tan의 조건(*"이미 잘 세팅돼 있다면"*)이 저장소 하나 안에서는 성립해도 **저장소 사이**에서는 아무도 보지 못한다 — 화자 둘 다 이 경계를 말하지 않는다.

> ⚠️ **Contradiction: AGENTS.md는 효과가 있는가.** Adler — *"that's barely moving the needle"*(07:20~07:22). 이 위키의 [[code-only-index-blind-spot]]은 반대 방향 — 코드 인덱스만으로는 PRD·`learnings.md` 같은 **산문 맥락이 빠진다**고 적었고, [[llm-coding-guidelines]]·[[intent-md]]는 그런 파일이 행동을 바꾼다는 소스들이다. Adler의 말은 **측정 없는 단언**이고 자사 제품(코드 인덱스)의 반대편을 깎는 진술이다.

> ⚠️ **"모델 회사는 이걸 만들지 않는다".** 05:00~05:10 · 07:44~07:51의 주장은 이 위키 안에서 반박도 확인도 안 된다 — [[graft]]·[[understand-anything]]는 소규모 독립 도구이고, [[cursor]]·[[claude-code]]·[[codex]]의 저장소 간 기능을 다룬 소스는 없다. **경쟁사 비교로 읽고 사실로 적지 않는다.**

## 해소하지 않고 표시만 한 것

- **화자 이름·직함** — 자막 근거 없음(제목·설명란만).
- **녹화일** — Agentic Batch Changes 베타 공개일(블로그 미열람), 행사명 미발화.
- **72%의 출처**, 자동차 회사·은행 이름, npm 공급망 취약점이 무엇인지.
- **Mercari 수치** — 82 vs 100, "100%" ASR 탈락 가능성. GitHub 코드 인젝션 이슈가 어느 기능인지(⚠️ Actions로 짐작되나 미발화).
- **"코드베이스가 부패하기 시작했다"** — 측정 없음.

## 등장 개체

- 인물: [[dan-adler]] (신규) · 익명의 자동차 제조사 임원 · 익명의 은행 기술 리더 · 익명의 Mercari 얼리 액세스 사용자
- 조직: [[sourcegraph]] (신규) · [[openai]] · [[anthropic]] · [[cursor]] · [[amazon]](예시) · Uber(예시) · Mercari(페이지 없음) · [[ai-engineer]](설명란 링크만)
- 제품: Agentic Batch Changes([[sourcegraph]] 페이지에) · [[claude-code]] · npm
- 개념: [[large-scale-code-changes]] (신규) · [[code-knowledge-graph]] · [[agentic-search]] · [[file-discovery-tax]] · [[code-only-index-blind-spot]] · [[legacy-code-modernization]] · [[greenfield-vs-brownfield-agent-risk]] · [[codebase-gardening]] · [[duplicate-code]] · [[cognitive-debt]] · [[verification-bottleneck]] · [[automated-code-review]] · [[ai-vulnerability-discovery]] · [[harness-engineering]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=oeL0uP-NO-U> (10:51, `upload_date` 2026-10-06)
- raw: `01.raw/articles/2026-10-06_AI 코딩 에이전트가 거대한 코드베이스를 망가뜨리고 있습니다 — Sourcegraph Dan Adler.md`
- 설명란 링크: <https://sourcegraph.com> · <https://sourcegraph.com/blog/introducing-agentic-batch-changes> · <https://www.linkedin.com/in/danielnealadler/> · <https://ai.engineer> (⚠️ 열어 보지 않았다)
- 같은 주제: [[tech-bridge-graft-code-knowledge-graph]] · [[tech-bridge-legacy-code-modernization-ai]] · [[tech-bridge-lauren-tan-trusting-agents]] · [[tech-bridge-lauren-tan-2000-prs]] · [[tech-bridge-death-of-code-review]]
- [[tech-bridge]] · [[dan-adler]] · [[sourcegraph]]
