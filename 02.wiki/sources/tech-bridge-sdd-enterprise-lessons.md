---
title: "Tech Bridge — AI 시대, 스펙 기반 개발(SDD)을 실무에 적용하며 배운 교훈들 (Simon Martinelli): system use case + entity model, plan/task 생략, self-contained system, requirements engineering으로 shift left"
type: source
tags: [spec-driven-development, ai-unified-process, use-cases, entity-model, requirements-engineering, shift-left, self-contained-systems, microservices, legacy-modernization, reverse-engineering, agent-skills, mcp, claude-md, risk-based-review, trunk-based-development, enterprise, video]
source-url: https://www.youtube.com/watch?v=T3SWxxQFr4o
source-type: video
author: Tech Bridge (한영자막 재배포) · 발표 [[simon-martinelli]](스위스 Java 컨설턴트 — 자막엔 "Simon"만, 성은 설명란) · 행사명은 자막에 없음(설명란 링크상 Tessl AI DevCon으로 보임 — 촬영일 미확정)
date-published: 2026-10-01
ingested: 2026-10-02
created: 2026-10-02
updated: 2026-10-02
---

# Tech Bridge — AI 시대, 스펙 기반 개발(SDD)을 실무에 적용하며 배운 교훈들 (Simon Martinelli)

[[tech-bridge|Tech Bridge]]가 재배포한 **30:41 발표 + Q&A**(공식 챕터 없음). 화자는 스위스에서 17년째 보험·도매·소매·정부의 **비즈니스 애플리케이션**을 만드는 Java 컨설턴트 [[simon-martinelli|Simon Martinelli]] — *"I don't do tools, I don't do products, I do business applications."*(01:58~02:02). 이 위키의 **세 번째 [[spec-driven-development|SDD]] 영상 소스**이며, 앞의 둘([[tech-bridge-spec-driven-development]] Spec Kit 데모 · [[tech-bridge-sdd-full-course]] JetBrains 강좌)이 **개발자 한 명의 기능 루프**를 다뤘다면 이 발표는 **역할이 나뉜 엔터프라이즈 팀과 레거시 현대화**에서 SDD를 본다. → [[ai-unified-process]] (신규)

> **스펙은 요구공학자가 쓰는 system use case + entity model이다. plan·task 단계를 건너뛰고 스펙에서 바로 코드를 만들며, 그 빈자리를 스킬·MCP·가이드라인(=하네스)이 채운다. 레거시는 코드에서 스펙을 역설계해 다시 생성한다. AI가 일할 컨텍스트를 한 곳에 모으려면 아키텍처는 self-contained system이어야 하고, 구현이 몇 분이 되면 모든 일이 requirements engineering으로 shift left한다.**

> *"but they are all in my opinion at least too developer centric"* (03:20~03:24) · *"I skip the plan task phase I just use SIS[=system] use cases and entity model and generate code directly"* (06:01~06:07) · *"So everything shifts left to requirements engineering in my opinion"* (26:43~26:45)

ASR·ko 보정: ko가 **경력 17년을 "17살"로**(01:47~01:50), **대회 운영 인원 12~15명을 "나이 12~15살"로**(00:32), **Jacobson의 1988년을 "1980년부터 1987년까지"로**(04:48~04:51 — `en`도 같은 오류), *"in a minute in a demo"* 를 **"데모 버전에서는 1분 만에 완료"로**(08:57 — 없던 수치), **"PowerPoint가 싫다"를 "좋다"로**(22:06), **waterfall을 "단계적"으로**(28:37), **Anthropic을 "인류학"으로**(10:38), *harness* 를 **"기회를 활용하세요"로**(25:12), *markdown* 을 **"가격 인하"로**(27:47) 옮겼다. ⭐ **설명란의 "SysML 유스케이스"는 ko·`en` 번역 트랙의 표기다** — en-orig는 *"system use cases"*(04:39~04:48). 도입 일화의 AI 도구는 en-orig *"Ventsurf"*(01:10, Windsurf로 추정)인데 ko·`en`은 **"Cursor"** — 미확정. 전체 목록은 raw. **인용은 en-orig에서만** 했다.

> ⚠️ **실무자 진술, 측정 없음.** 데모 구현 *"one and a half minute or so"*(22:09~22:12), 팀 규모 5~7명 → 1~2명(21:28~21:30), 스펙 2주 vs 구현 *"five minutes"*(26:59~27:00), *"near deterministic"*(24:06~24:10)은 모두 화자의 관찰이고 측정 방법·조건은 없다. 화자는 자기 프로세스(AI Unified Process)의 저자다. 데모 화면·슬라이드는 자막에 없다.
>
> ⚠️ **행사·촬영일 미확정.** 자막은 행사명을 말하지 않는다. 설명란의 *"AI DevCon 등록"*·*"Tessl"* 링크(tessl.co, 열어 보지 않았다)는 [[tech-bridge-anthropic-dreaming-memory]](자막 *"here at AI DevCon"*)와 같은 쌍이다. 같은 방 직전 발표가 CLAUDE.md를 다뤘다는 말(*"what you heard in the last talk if you were here in that room"* 16:04~16:06)이 있지만 그 발표가 무엇인지는 확인할 수 없다. 시점 하한: AI 도구 사용 *"around fall 2024"*(01:10), Tessl 도구 *"early 2025"*(03:16~03:20).

## 1. 출발 — 무엇을 구현했는지 모른다 (00:00~02:04)

스포츠 클럽의 자원봉사자 관리 시스템을 2024년 가을 AI 코딩 도구로 *"relatively fast"*(01:14) 만들었다. 문제는 음악 축제 쪽이 같은 시스템을 원했을 때다 — *"I had no clue what I was implementing and I had no is no clue how I could change the features so that it will fulfill the requirements of this music festival"*(01:28~01:38). **빨리 만든 코드는 있는데 요구사항 표현이 없다** — 이것이 SDD로 간 이유다. → [[cognitive-debt]]와 같은 자리(무엇을 만들었는지 사람이 모른다).

## 2. SDD의 flavor — 도구 중심 vs 프로세스 중심 (02:04~03:42)

Tessl의 AI Native Dev 사이트에서 Simon Maple의 글로 SDD를 접했다(02:07~02:20). *"the term spectriven[=spec-driven] development is very old right that's from the 2000s or maybe late 90s but the spectrum development with AI was relatively new"*(02:29~02:36).

| | 도구 | 화자의 프로세스 |
|---|---|---|
| 예 | [[kiro|Amazon Kiro]] · [[github-spec-kit|GitHub Spec Kit]] · BMAD Method · Tessl 도구(03:07~03:20) | **AI Unified Process** (*"my process I created"* 03:00~03:05) |
| 대상 | *"too developer centric"*(03:24) | *"the whole software development life cycle especially for enterprises where you not are a soloreneur"*(03:26~03:37) |
| 흐름 | PRD → plan → tasks → implement(Kiro 예, 05:49~06:01) | 스펙(use case + entity model) → **바로 코드** |

> Tessl·BMAD Method 페이지는 이 위키에 없다. BMAD는 [[ai-native-sdlc]]·[[tech-bridge-pstack-third-party-review]]에서 이름만 나왔다.

## 3. AI Unified Process — 스펙 = system use case + entity model (03:42~09:53)

→ [[ai-unified-process]] (신규)

다이어그램(화면은 자막에 없음): vision → requirements → **스펙** → code·test → review. 요구 단계 참고로 IREB(*"international requirements engineering board"*)가 *"AI for requirements engineering"* micro credential을 막 만들었다고 소개한다(04:06~04:19).

- **system use case** — *"what could be good specs that a[=AI] understands but also all stakeholders in the project can understand"*(04:29~04:36). Ivar Jacobson이 *"back in 1988"*(04:48, ⚠️ 화자 진술) 만든 것, 화자가 2000년대 초 스위스 철도에서 *"communication specification between stakeholders and developers"*(05:10~05:14)로 썼다.
- **entity model** — *"more like a domain model"*(05:23~05:25), DDD를 하든 안 하든.
- 행위(use case)만으로는 부족하다 — UI는 **Figma 디자인을 MCP 서버로**(06:22~06:29), API는 API 스펙.
- **테스트 순서는 산출물에 따라** — UI가 있으면 TDD가 어렵고(먼저 UI 모습을 정해야), API면 *"I would always go for test-driven development"*(06:51~06:55).
- **리뷰 양은 위험 관리** — ERP의 재고 모듈이 멈추면 *"they can just go and grab a coffee"*(07:39~07:41), 주문 관리가 멈추면 *"the company probably will lose money"*(07:47~07:50). *"that's not different from AI or manual driven development"*(07:58~07:59). → [[risk-proportional-human-review]]

**greenfield 흐름**(08:05~09:53): 요구공학자·PO·BA가 entity model과 use case를 만들고 → **definition of done**을 소프트웨어 엔지니어·AI·요구공학자가 함께 정하고(08:37~08:47) → 에이전트. ⭐ *"because we don't do the plan and task phase, we need that in the middle. That is probably the most important thing of the whole process. So that means the skills must match the outcome."*(09:03~09:17) — 고객 6곳의 스킬이 전부 다르다(React+Spring Boot · Vaadin+Spring Boot · Angular+Quarkus · 사내 프레임워크, 09:23~09:48). → [[agent-skills]]

## 4. brownfield — 역설계해서 다시 만든다 (09:53~11:41)

화자의 주업은 greenfield가 아니라 **현대화**(*"about eight years now"* 10:02~10:05). 코드·테스트·문서에서 **use case와 entity model을 추출** → 업무 담당자가 검토 → 새 코드 생성(10:09~10:32).

> ⭐ *"there are a lot of ids[=ideas?] that we can directly transform maybe from cobalt[=COBOL] to Java. So that's also something that anthropic is is telling us but that never worked. So we did that like 30 years ago cobalt to C or cobalt to C++"* (10:32~10:46) · *"modernization is not lift and shift modernization is rethinking how people are working with the software"* (10:52~10:59)

역설계를 거치기 때문에 **새 기능을 넣을 수 있다** — 2년 전 현대화 시작 때의 원칙은 *"we want to have the exact same system just in another technology and you don't add new features because we don't want to introduce new box[=bugs]"*(11:25~11:36)였는데, 이제 *"we just change um the specification"*(11:38~11:41). 사용자 반응도 긍정적이었다(11:07~11:10, ⚠️ 정량 없음). → [[legacy-code-modernization]]

## 5. 왜 use case인가 (11:41~12:34)

use case는 *"very well defined and even AI knows how to write use cases because it's around for a very long time"*(11:52~11:56) — precondition · postcondition · main success scenario · alternative flows. **user story는 use case의 한 flow**(12:15~12:23), *"use cases are better than user stories because they are simply bigger"*(12:29~12:31). postcondition은 *"kind of acceptance criteria … that can be verified in tests"*(15:10~15:17).

## 6. 데모 — Spring PetClinic (12:34~16:58, 21:43~22:23)

Spring PetClinic을 **역설계**: use case UML 다이어그램(actor 2: visitor · clinic user = 시스템 역할, 모듈별 묶음), DB 모델에서 유도한 entity model, use case 문서(actor · precondition · scenario · postcondition). 그다음 *implement* 한 마디.

- ⭐ *"in those projects we don't prompt. So we have skills for everything and we iterate on the skills."*(15:30~15:34) 스킬을 조직에 공유하지만 *"not everybody in the organization is maybe using the same agent. So we need some skill distribution"*(15:42~15:49) → [[cross-harness-skill-compilation]]
- 도구는 en-orig *"flow code"*(15:47, ASR — [[claude-code|Claude Code]]로 판독), IDE 밖에서 실행은 데모용.
- **CLAUDE.md는 거의 비어 있고** 가이드라인(아키텍처·패키지 구조·도구)을 참조할 뿐, *"most of the things are in the skills"*(16:31).
- 프로세스의 스킬은 **두 층** — 스펙용 스킬 + 스택별 스킬. 스택 조합이 너무 많아 *"that's probably a thing that the company has to do"*(16:52~16:58).
- 결과: 의사 목록 화면, *"It took one and a half minute or so"*(22:09~22:12, ⚠️ 화자 진술).

## 7. 아키텍처 — 컨텍스트를 한 곳에 (17:07~20:25)

→ [[self-contained-systems]] (신규)

- 고객 다수가 마이크로서비스를 *"in a very naive way"*(17:24~17:28) — *"they were focusing on the micro in microservices"*(17:30~17:32) → *"distributed big ball of mud"*(17:36~17:38). 한 보험사는 마이크로서비스 약 500개 + 마이크로 프런트엔드 약 500개, n:m 관계(17:40~17:56).
- 왜 AI에게 최악인가: *"you need the code that the AI should work on in a single place at least on your machine"*(18:07~18:14).
- 그렇다고 모놀리스로 돌아가지 말라 — *"I would say stop here don't do that"*(18:30~18:33). 현재 ERP는 *"thousands of database tables"*(18:42~18:45), *"the context is too big"*(18:48~18:50).
- **self-contained system**: *"We create verticals"* — UI·비즈니스 로직·DB를 한 저장소/프로젝트에(19:07~19:18). 그러면 *"the AI can exactly work on that"*(19:22~19:26), SCS마다 다른 기술(재고 = Vaadin, 주문 = React)과 다른 스킬.
- **한 스택**이면 가드레일·스킬을 한 번만 만든다. React/Angular + Spring Boot/Quarkus면 *"they have to create this twice and also maintain that twice"*(20:15~20:20).

## 8. 팀과 프로세스 (20:25~21:43, 24:16~25:04)

- 스펙은 스토리처럼 입력이지만 *"we are way faster. So we cannot wait two weeks"*(20:57~21:02) — 스펙엔 2주가 걸려도 구현엔 아니다.
- **SCS당 개발자 1~2명**(둘을 선호 — 지식 교환), 5~7명에서 줄였다(21:15~21:30). 스프린트 없이 **continuous flow**, use case를 칸반 카드처럼(21:33~21:38).
- ⭐ **PR 없음** — *"We do trunkbased development and we do kind of an ongoing review process"*(24:40~24:46), 두 개발자가 서로 설명하며 peer review(24:49~24:59).
- 리뷰 양은 다시 위험에 비례(24:18~24:35).

## 9. 왜 됐나 — 가드레일 (22:23~24:16)

1. ⭐ **"never let AI create a project"**(22:33~22:36) — 토큰 낭비이고 *"you probably end up with an outdated application"*(22:42~22:44). start.spring.io 같은 CLI를 쓰라.
2. **규칙은 작게** — *"you don't put everything in cloud empty[=CLAUDE.md] or in the agents empty[=AGENTS.md] because there's a study from the ETH university in Sururik[=Zürich] and they say the bigger the system prompt the more hallucinations you get probably. So it's maybe even better to have none of those files than a big one."*(23:05~23:23) ⚠️ **연구명·저자·수치 미발화, 화자도 "probably"** — 이 위키는 원 연구를 확인하지 않았다.
3. 아키텍처 문서(**arc42**, 23:33~23:36)
4. **스킬**, 그리고 스킬이 커지지 않도록 사내 프레임워크의 큰 문서는 **vector search가 있는 MCP 서버**로(23:44~23:56) → [[model-context-protocol]]
5. 결과: *"if you do a good job and iterate on that, you really get probably um a near deterministic solution. So what I did before I can delete everything do it again and will get more or less the same outcome"*(24:00~24:15, ⚠️ 측정 없음).

## 10. 결론 — specs are not enough, shift left (25:04~27:24)

- *"specs reduce non investment[=?] but not specs are not enough. So you need to harness you need all the context around that that this really works."*(25:04~25:15) — ⚠️ *non investment* 는 판독 불가(ko·`en` "부채 투자", 문맥상 non-determinism일 수 있음 — 추정). → [[harness-engineering]]
- **스펙의 지속 가능성** — 역설계한 스펙으로 *"generate the same application in different technology with a different UI maybe we don't have even a UI we have chat"*(25:34~25:42), 업무 담당자가 *"directly change the way the systems should behave without developers"*(25:46~25:49).
- 스위스 의회 사례관리 소프트웨어 PoC — 코드 쪽은 화자 혼자, 요구공학자/PO 두 명이 스펙을 쓰는데 *"they have much more work to do than I have"*(26:26~26:29). markdown을 바꾸면 자동 생성되는 파이프라인을 만드는 중(26:31~26:37).
- ⭐ *"So the kind of the work moves or shifts left. So everything shifts left to requirements engineering"*(26:41~26:45) — *"Now you have two weeks and then five minutes and two weeks"*(26:59~27:00). → [[shift-left-interventions]](같은 단어, 다른 대상)
- *"the most important thing is you should know your architecture and domain"*(27:04~27:08) — 주니어 개발자 논의는 시간상 생략. → [[architecture-as-remaining-art]]

## 11. Q&A (27:24~30:41)

1. **PlantUML 다이어그램 → 마크다운 요구사항인가?** — greenfield면 요구 카탈로그/PRD → use case 다이어그램(모듈 분할의 단서도) → use case 문서(27:51~28:17). 요구공학자·PO는 AI로 **중복·누락을 검증**(28:22~28:31). ⭐ *"a lot of people say spectrum development is waterfall and that's simply not true"*(28:36~28:40) — *"we don't do big upfront design. We just go use case by use case."*(28:50~28:51)
2. **스펙이 틀렸으면?** — use case를 고치고(데모: 전문 분야 구분자를 쉼표 → @) 다시 *implement*(29:28~29:52). 코드를 버리고 재생성할 수도 있지만 *"then my git history wouldn't look nice and it would be harder to review the changes"*(30:01~30:06) — 지금은 사람이 코드를 읽기 때문이다. *"opinions of some people is AI doesn't need the source code"*(30:09~30:14), AI 친화적이고 덜 human-readable한 언어가 나올지도 — *"I don't know"*(30:28~30:30).

## 이 위키와의 연결

### 이어지는 것

- **[[spec-driven-development]]** — 08-29 편(Spec Kit), 09-27 풀코스에 이어 **세 번째 flavor**: 스펙 작성자가 개발자가 아니라 **요구공학자**, 스펙 형식이 user story가 아니라 **use case + entity model**, plan/tasks 없음. [[tech-bridge-ai-native-skills]]([[imad-touil]])의 *"SDD는 기업 SDLC의 product increment 한 칸"* 에 대해 이 발표는 SDD 자체를 SDLC 전체로 넓히려는 쪽이다.
- **[[agent-skills]]** — *"skills must match the outcome"* · *"we don't prompt"* · 스펙 스킬/스택 스킬 두 층 · 에이전트가 달라 스킬 배포가 문제. 풀코스(09-27)의 *"반복되는 프롬프트는 스킬로"* 의 실무판.
- **[[risk-proportional-human-review]]** — IBM 편이 *예시 없이* 말한 "가장 위험한 결정"에 **ERP 모듈 criticality**(재고 vs 주문)라는 구체 예가 붙었다.
- **[[greenfield-vs-brownfield-agent-risk]]** — 화자는 *"I'm rarely on green field projects"*(03:57~03:59). 브라운필드를 **스펙 역설계로 가드레일을 먼저 만드는** 방식으로 다룬다.
- **[[context-rot]] · [[llm-coding-guidelines]]** — *"짧은 CLAUDE.md"* 처방과 같은 방향. ETH 연구 인용은 근거 미확인.
- **[[architecture-as-remaining-art]]** — *"you should know your architecture and domain"*, 그리고 아키텍처가 AI의 **컨텍스트 경계**를 정한다는 구체화(SCS).

### 갈리는 것

> ⚠️ **Contradiction: plan/tasks는 필요한가, 스펙은 user story인가.** [[spec-driven-development]]의 Spec Kit 코어는 Spec(**사용자 스토리**) → **Plan → Tasks** → Implement이고, [[kiro|Kiro]]도 PRD → plan → tasks(화자 설명 05:49~06:01). 이 발표는 **plan·task 단계를 건너뛰고**(06:01~06:04) 그 자리를 스킬로 채우며, 스펙은 **user story보다 큰 use case**다(12:29~12:31). 화자는 그 차이가 가능한 이유를 *스킬이 산출물과 맞아야 한다*에 둔다 — 스킬이 약한 팀에서도 같은 결과인지는 말하지 않는다.

> ⚠️ **Contradiction: 스펙을 직접 고치는가.** [[tech-bridge-sdd-full-course]]는 *"스펙은 에이전트를 통해 고친다 — 직접 편집하면 관련 문서가 어긋난다(drift)"*. 이 발표에서는 요구공학자가 **markdown을 직접 고치고** 파이프라인이 재생성하며(26:33~26:37), Q&A에서도 use case를 고친 뒤 *implement*(29:28~29:52). 화자의 스펙은 use case + entity model 두 종류뿐이라 drift 표면이 작을 수 있다 — ⚠️ 위키의 추정.

> ⚠️ **Contradiction: COBOL→Java 직역.** [[legacy-code-modernization]]([[ibm|IBM]], 09-18)은 AI의 두 자리 중 하나로 **번역**(COBOL→Java, *"논리와 의도는 유지"*)을 든다. 화자는 같은 예를 들어 *"that never worked"*(10:36~10:41) — 30년 전 COBOL→C/C++ 변환과 같은 **lift and shift**라고 한다. 다만 IBM 편도 *"현대화 ≠ 번역"* 이라 결론은 가깝고, 갈리는 것은 **번역이 쓸모 있는 중간 단계인가**다. 화자가 지목한 *"anthropic is telling us"* 의 출처(어떤 글·제품인지)는 발화되지 않는다.

> ⚠️ **Contradiction: 모놀리스에서 어디로.** [[legacy-code-modernization]]의 아키텍처 축은 *긴밀히 결합된 모놀리스 → 독립 서비스*. 화자는 순진한 마이크로서비스(500개)도, 그 반동인 모놀리스 회귀도 아닌 **수직 분할(SCS)** 을 권한다. 기준은 *AI가 한 번에 볼 컨텍스트 크기*다 — IBM 편엔 없는 기준.

> ⚠️ **긴장: 컨텍스트 파일은 키울 것인가.** [[harness-engineering]]의 System Evolution은 *"every mistake becomes a rule"* → `agents.md`에 규칙 추가, [[tech-bridge-anthropic-dreaming-memory]]는 CLAUDE.md가 *"unreasonably effective"*(동시에 *context bloat* 경고). 이 발표는 *"maybe even better to have none of those files than a big one"* — 규칙은 **스킬·가이드라인 문서로 빼고** CLAUDE.md는 참조만 둔다. 셋 다 측정치가 없다.

> ⚠️ **대비: 계획을 믿는가.** [[lauren-tan|Lauren Tan]]([[tech-bridge-pstack-third-party-review]])은 *"최고의 사양은 코드"*. 화자는 반대로 **코드에서 스펙을 역설계**해 스펙을 지속 자산으로 삼는다 — 둘 다 자리 잡은 코드베이스에서 출발한다는 점에서 대상이 겹친다.

## 해소하지 않고 표시만 한 것

- **도입 일화의 도구** — en-orig *"Ventsurf"*(Windsurf 추정) vs ko·`en` *"Cursor"*.
- **"SysML" vs "system use case"** — en-orig 04:39~04:48은 system use case, 06:04 *"SIS"*·06:19 *"sysma"* 는 모호. 설명란은 SysML.
- **"UML and OOP"(04:53)** — ko·`en`은 RUP. AI *Unified* Process라는 이름으로 보아 RUP일 개연성, 미확정.
- **"specs reduce non investment"(25:08)** — 판독 불가.
- **ETH Zurich 연구** — 이름·수치 없음, 확인하지 않음.
- **"anthropic is telling us"(10:38)** — 무엇을 가리키는지 미발화.
- **"Hey Sam"(00:55)** — 애칭/ASR 미확정. 성(Martinelli)은 설명란에만.
- **행사(Tessl AI DevCon으로 보임)·촬영일·직전 발표** 미확정.
- **효과 수치 전부** — 1분 30초, 5~7명 → 1~2명, near deterministic.

## 등장 개체

- 인물: [[simon-martinelli]] (신규) · Simon Maple(Tessl AI Native Dev 글, 페이지 없음) · Ivar Jacobson(use case 창시자로 언급, 페이지 없음) · 사회자 · 청중 질문자 2명
- 조직: Tessl(페이지 없음) · [[anthropic]](COBOL→Java 언급) · [[amazon]] · ETH Zurich · IREB · 스위스 철도·스위스 의회·최대 도매업체·보험사(고객, 이름 없음)
- 제품·도구: [[claude-code]] · CLAUDE.md · AGENTS.md · [[kiro|Amazon Kiro]] · [[github-spec-kit]] · BMAD Method · [[figma]](MCP) · Spring PetClinic · start.spring.io · Vaadin · Spring Boot · React · Angular · Quarkus · PlantUML · arc42 · [[model-context-protocol|MCP]]
- 개념: [[ai-unified-process]] (신규) · [[self-contained-systems]] (신규) · [[spec-driven-development]] · [[agent-skills]] · [[harness-engineering]] · [[legacy-code-modernization]] · [[risk-proportional-human-review]] · [[greenfield-vs-brownfield-agent-risk]] · [[shift-left-interventions]] · [[architecture-as-remaining-art]] · [[context-rot]] · [[cognitive-debt]] · [[cross-harness-skill-compilation]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=T3SWxxQFr4o> (30:41, `upload_date` 2026-10-01)
- raw: `01.raw/articles/2026-10-01_AI 시대, 스펙 기반 개발(SDD)을 실무에 적용하며 배운 교훈들.md`
- 설명란 링크: <https://tessl.co/5re> · <https://tessl.co/6gq> (⚠️ 열어 보지 않았다)
- 같은 주제: [[tech-bridge-spec-driven-development]] · [[tech-bridge-sdd-full-course]] · [[tech-bridge-ai-native-sdlc]] · [[tech-bridge-legacy-code-modernization-ai]] · [[tech-bridge-pstack-third-party-review]] · [[tech-bridge-anthropic-dreaming-memory]]
- [[tech-bridge]] · [[simon-martinelli]]
