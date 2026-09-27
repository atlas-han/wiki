---
title: "Tech Bridge — 스펙 주도 개발 풀코스 (JetBrains 협업 강좌): 헌법 → 기능 루프 → 재계획, 레거시 도입, 스킬 패키징, 에이전트 독립"
type: source
tags: [spec-driven-development, constitution, replanning, human-in-the-loop, cognitive-debt, ai-fatigue, brownfield, agent-skills, mcp, acp, spec-kit, openspec, jetbrains, claude-code, video]
source-url: https://www.youtube.com/watch?v=FJo7p9SPS9c
source-type: video
author: Tech Bridge (한영자막 재배포) · 강사 JetBrains developer advocate — 자막 표기 "Paul Everett"(en-orig) / "Paul Everitt"(en) / "폴 에버릿"(ko), 미확정 · 소개자 "Andrew"(성 발화 없음) · 여러 레슨을 이어 붙인 강좌
date-published: 2026-09-26
ingested: 2026-09-27
created: 2026-09-27
updated: 2026-09-27
---

# Tech Bridge — 스펙 주도 개발 풀코스 (JetBrains 협업 강좌)

[[tech-bridge|Tech Bridge]]가 재배포한 **1:01:33 강좌**(공식 챕터 없음). 도입부가 *"Welcome to this course on spec-driven development, built in partnership with JetBrains"*(00:00~00:03)로 시작하고, 기여자로 **JetBrains**와 **deeplearning.ai** 사람을 부른다(04:06~04:14). 여러 레슨이 한 영상에 들어 있다(*"lesson four"* 46:45, *"lesson 12"* 57:45). 이 위키의 **두 번째 [[spec-driven-development|SDD]] 영상 소스**다 — 첫째는 08-29 [[tech-bridge-spec-driven-development]](Microsoft 365 MVP의 [[github-spec-kit|Spec Kit]] 데모). 그 편이 **한 도구(Spec Kit)의 네 단계**를 시연했다면, 이 강좌는 **도구 없이 손으로 짠 프롬프트로 같은 흐름을 돌리고, 나중에 그것을 스킬로 묶는** 순서로 간다. Spec Kit은 끝부분에서 *"one attempt"* 로만 소개된다(54:43~54:49). 한 줄 테제:

> **스펙은 에이전트가 모르는 맥락을 적는 일이다. 프로젝트 수준의 헌법(mission · tech stack · roadmap)을 에이전트와의 대화로 쓰고, 기능마다 브랜치에서 plan → implement → validate를 돌고, 기능 사이에 재계획으로 헌법·로드맵·프로세스 자체를 고친다. 반복되는 프롬프트는 스킬로 묶고, 표준(MCP · AGENTS.md · skills · ACP)에 기대 특정 에이전트·IDE에서 독립한다.**

> *"The specs you write today become the memory of your projects tomorrow."* (1:00:59~1:01:04)

ASR·ko 보정: ko가 ***"Agents are stateless"* 를 "상태를 가지고 있다"로**(01:12~01:14), ***"3 or 4 minutes"* 를 "3~4시간"으로**(04:01), ***"back-and-forth conversation"* 을 "일방적인 대화"로**(43:59) 뒤집는다. *feature* → **"함수"**, *roadmap* → **"시트 경로"·"경로 지도"**, *tech stack* → **"배터리"**, *skill* → **"기술"·"능력"**, *brownfield* → **"오염된 부지"**, *main* 브랜치 → **"도메인"**, *SDD* → **"SSD"·"자기 주도 개발"**. **MCP → CLI+스킬 추세**(53:51)는 ko에서 **"MCP 서버에 CLI 기능을 더한다"** 로 방향이 바뀌었다. 전체 목록은 raw의 보정 표.

> ⚠️ **멤버 전용 → 공개 전환.** 2026-09-23 멤버 전용으로 처음 게시 → 2026-09-27 회차에 `public`, **`upload_date` 20260926**(`timestamp` 1790416830 = 2026-09-26 10:00:30 UTC). 현재 `upload_date`를 게시일로 쓴다. `vMlsLmKuFZk` · `XZuws4hFG4o` · `zkmvCDSxqdc`와 같은 패턴이며, 날짜가 바뀐 이유는 확인하지 않았다.

> ⚠️ **화자 이름이 트랙마다 다르다 — 해소하지 않는다.** 강사: en-orig *"Paul **Everett**, who's developer advocate at JetBrains"*(00:25~00:29) · en *"Paul **Everitt**"* · ko *"폴 **에버릿**"*. 소개자: *"Thank you, **Andrew**"*(00:30) — **성은 발화되지 않는다.** DeepLearning.AI 강좌 형식과 *"I'm definitely an advocate of lazy prompting"*(03:31~03:33)로 보아 [[andrew-ng|Andrew Ng]]일 개연성이 높지만 자막이 확인하지 않는다. 기여자 *"Konstantin **Chayka**"*(en-orig) / *"**Chicherin**"*(en · ko 치체린), Zina Smirnova, Isabel Zaro. 04:21 이후 레슨 본문 내레이터의 이름은 자막에 없다. [[paul-everitt]] 페이지는 **en 표기로 파일명을 정했을 뿐**, 철자를 확정하지 않는다.

> ⚠️ **공식 챕터 없음.** 아래 소제목은 이 위키가 붙인 것이다. 타임스탬프는 **en-orig 캡션의 실제 시작 시각**(구간 = 첫 캡션 시작 ~ 마지막 캡션 시작), 인용은 **en-orig 원문**이다. 데모의 화면(질문지, 생성 파일, diff)은 자막에 없다.

> ⚠️ **교육 콘텐츠이자 파트너 강좌.** 강사가 JetBrains 소속이고 데모는 WebStorm, 끝부분은 JetBrains IDE의 ACP registry 시연이다(58:35~59:09). 효과를 측정한 수치는 **하나도 없다** — 세 이점은 주장이고, MVP 데모의 성공은 *"a useful demo"*(45:30~45:34)라는 자기 평가다.

## 세 이점 — 두 번 말한다 (00:38~01:30 · 05:55~07:14)

| 이점 | 인트로 (강사) | 본문 레슨 |
|---|---|---|
| **작은 스펙 변경 → 큰 코드 변경** | *"One sentence like "Use SQLite with Prisma ORM" might affect hundreds of lines of code"*(00:49~00:54) | 외관을 설명한 몇 문장이 *"hundreds of lines of CSS"*(06:04~06:12). *"reduces the cognitive overhead"*(06:13~06:18) |
| **context decay 제거** | *"Agents are stateless, so loading them with the highest-quality context right when they boot up is important"*(01:11~01:18) | 컨텍스트 창이 차면 실수가 늘어난다. *"Specs persist between sessions and even agents"*(06:38~06:41) |
| **intent fidelity** | 문제·성공 기준·제약을 정의하면 에이전트가 *"elaborate to create a fuller plan"*(01:21~01:30) | 에이전트가 코드를 만들기 **전에** 문제·성공 기준·제약·user flow를 정의하게 강제한다(06:58~07:06) |

다른 비유 둘: **컴파일러** — SDD는 스펙을 소스 코드로 바꾸고, 스펙은 사람의 언어라 이해관계자가 읽는다(07:30~07:47). **건축가** — *"the agent is the muscle, but the spec is the brain"*(08:56~08:57), 사람은 설계도를 주고 시공을 감독하고 결과를 받아들이거나 변경을 요청한다(11:32~11:57).

소개자의 논거는 **비용 비교**다: 에이전트가 *"20 or 30 minutes"* 코드를 쓸 거라면 *"you're often better off sitting down for 3 or 4 minutes and writing it really clear instructions"*(03:53~04:05). 스펙이 없으면 결정이 *"the whims of the coding agent"*(02:01~02:03)에 맡겨지고, 스펙 없는 팀에서 여러 개발자의 에이전트가 *"building quickly but in contradictory ways"*(02:25~02:27)였다고 한다. *"Writing a spec requires thinking, and this is hard work"*(01:48~01:51).

**스펙의 세부 수준이 핵심 기술**이다: *"One key skill in SDD is knowing the right level of detail"*(09:28~09:32) — 목표·미션·대상·제약은 많이, 에이전트가 스스로 정할 수 있는 저수준 결정은 적게(09:39~09:49).

## 헌법 — mission · tech stack · roadmap (09:52~20:10)

*"First, we specify the constitution. What is the mission, the tech stack, the road map?"*(09:55~10:00). 이 강좌의 **헌법 정의가 기존 위키와 다르다**(아래 대조).

- **AGENTS.md와의 관계**: *"Many developers use a top-level agents.md file for this purpose, but a project constitution is agent agnostic and more structured."*(10:05~10:15) — 헌법을 **AGENTS.md의 구조화된 대체물**로 둔다.
- **합의 문서**: 사람과 에이전트 사이의 합의이자 *"the agreement between the humans"*(10:17~10:24).
- **세 파일**: 대화가 끝나면 `specs/` 디렉터리에 `mission.md` · `techstack.md` · `roadmap.md`(18:59~19:04). mission = why(비전·대상·범위), tech stack = 엔지니어링 팀의 공통 이해(개발·배포 기술과 제약), roadmap = *"a living document with a sequence of phases, each implemented with their own feature spec process"*(10:47~10:52).
- **에이전트와의 대화로 쓴다**: *"But we don't write it alone. We write it in a conversation with the agent."*(15:43~15:45). 데모는 Claude Code의 **AskUserQuestion 도구**를 프롬프트에 직접 언급한다 — *"totally optional, but we just like the way it looks"*(17:25~17:35). 에이전트가 mission 어조, 백엔드 언어, 로드맵 granularity를 묻는다(18:02~18:29).
- **로드맵은 작은 단계로**: *"Spec-driven development works best with a human-in-the-loop approach, where you review small changes. So, tell the agent to organize the roadmap in small steps."*(17:45~17:53)
- **직접 편집하지 말고 에이전트에게 고치게 한다**: *"To keep all artifacts consistent, it is better practice to ask the agent to make changes to them. Manually, and you might miss updating related documents."*(19:26~19:34) — 27:53~28:04에 같은 원칙이 다시 나온다: IDE의 Move 도구로 파일을 옮기자 *"Not so fast. This can lead to drift where other artifacts, specs, readmes get out of sync."*
- **커밋해서 living document로**(19:56~20:00).

## 기능 루프 — 브랜치 · plan → implement → validate (20:12~29:11)

인트로의 요약: 기능마다 **자기 브랜치**에서 plan · implement · verify를 돌아 *"leave a clean slate between features"*(02:36~02:50).

**1. 기능 스펙(plan)** — 로드맵의 1단계 기능 *"Hello Hono"*(20:24~20:27). **새 컨텍스트에서 시작**(*"The agent can get what it needs from the official source, the Constitution"* 20:41~20:45), 브랜치를 에이전트에게 알리고, 대화로 *"a plan for tasks, collect requirements, and a scorecard for validation"*(20:57~21:03)을 만든다. 결과는 **plan · requirements · validation 세 문서**(21:46~22:43). requirements에는 중요한 기술 요구·제약을 적되 *"don't state minor technical details like variable names here. We want to control the process, but not oversteer the agent."*(22:25~22:33) 스펙을 커밋한다 — *"The changes you make here in the specs will expand downstream into hundreds of lines of code. So, time spent here is well spent."*(23:02~23:11)

**2. 구현** — *"clear out your context with a slash clear command"*(23:37~23:41) 후 모든 태스크 그룹 구현. 보안·DB처럼 **작은 실수가 복리로 커지는 곳**은 태스크 그룹을 하나씩(23:49~24:01). 개발자의 역할: *"to act as an architect or supervisor and ensure that the agent is provided with a clear contract"*(24:21~24:30).

**3. 검증** — *"don't merge yet"*(25:14~25:16). 리뷰는 **고수준으로**: 기능이 동작하고 스펙을 반영하는가이지, 어떤 CSS 클래스인가가 아니다(25:36~25:43). 코드의 실수가 **계획의 실수에서 흘러나왔다** — *"this mistake in the code flowed from a mistake in the plan"*(26:05~26:07) → 에이전트에게 고치게 해 **스펙과 구현을 함께** 바로잡는다(26:12~26:15). 이것이 human in the loop(26:18~26:24).

**스펙 버전 관리는 열린 문제**라고 강좌가 스스로 말한다: *"How to handle versioning of the specs and how to associate which specs created which code changes is an evolving topic in the community."*(28:34~28:42) 규칙: 로드맵 체크 같은 **작은 헌법 변경은 기능 브랜치에**, 복잡한 헌법 변경은 **별도 브랜치에**(28:43~28:55).

## 재계획 — 기능 사이에 멈춘다 (29:14~35:45)

*"Don't rush into it. Take a step back and reflect with some replanning. You have to run slow to run fast."*(29:19~29:27) 재계획의 대상은 세 층이다(11:08~11:15, 33:09~33:21): **기능**, **프로젝트**(헌법·로드맵), 그리고 **SDD 워크플로 자체**(*"across projects, across your organization"*).

- **헌법 변경은 자기 브랜치에서**: *"The constitution is a living document. It's good practice to make updates to it in its own separate branch, so you can keep track of which versions of it produced which code."*(29:48~29:57) — 테스트 선호를 tech stack에 추가 → 기존 기능 스펙·구현도 그 변경에 맞춰 갱신 → 테스트 작성 → 디버거로 테스트를 밟아 본다(29:59~31:05).
- **제품 방향 변경**: PM이 *"40% of our users are on mobile"*(31:21~31:24)라며 반응형을 요구 → 작은 변경이면 재계획 중에 바로, 크면 로드맵의 **별도 기능 단계로**(31:38~31:54). *"we want the specs to capture decisions, not just the code"*(31:57~31:59).
- **로드맵 정리**: 기능 2~5가 *"kind of hang together"* → 한 단계로 묶는다(32:53~33:02).
- **프로세스 개선 = 스킬**: 비기술 이해관계자를 위한 **changelog 스킬**을 에이전트의 스킬 작성 스킬로 만든다(33:23~34:22). 에이전트는 그것을 **global skills area**에 만들었다 — *"This skill will now be usable across all projects"*(34:57~35:04). 프로젝트 전용이냐 전 프로젝트 표준이냐는 *"a style choice"*(34:15~34:26). validation 단계(README 갱신 · lint · format · 테스트)를 **validation skill**로 묶을 수 있다(34:29~34:47).

*"Now that most of your work as a developer is in planning and validation, rather than implementing, make time between features to replan."*(35:32~35:40)

## AI fatigue와 cognitive debt (25:14~29:11 · 35:47~42:30)

강좌가 붙인 이름 두 개 → [[cognitive-debt]] (신규).

- **cognitive debt**: *"Because agents are so fast at writing code, software developers have lately been talking about cognitive debt. The mental load of tracking what your code is doing and how it has evolved."*(26:26~26:37) 처방은 **변경을 감당할 크기로**(26:40~26:48). 두 번째 기능의 검증에서는 **앱 실행**과 별도로 *"prevent cognitive debt by validating that we understand these changes"* — 테스트를 읽고 **디버거로 실행**해 본다(40:31~40:43).
- **AI fatigue**: *"Agents can generate a lot of code with a lot of changes. This massive amount of code makes the human in the loop validation exhausting."*(36:02~36:10) 처방은 **기능 단계 사이의 깨끗한 경계** — 시작 전 체크리스트: 미완 작업? 지난 기능 브랜치를 main에 병합했나? 다음 로드맵 항목이 맞나? **에이전트 컨텍스트를 비웠나** — *"to ensure the specs capture the intent instead of memory snapshots"*(36:32~36:38).
- **리뷰 기준**: *"stick to higher-level requirements. Avoid nitpicking stuff like variable names. Just make sure it creates code that you can commit under your name."*(39:17~39:27)
- **스펙의 누락은 실패가 아니다**: props 타입을 분리하라는 결정은 스펙에 없었다 — *"an omission such as extracted prop types isn't a failure. You are evolving the spec as you discover new details"*(39:51~39:58).
- **서브에이전트 deep review**: *"Sometimes you need to validate that you weren't lied to."*(40:50~40:52) 여러 서브에이전트에게 프로젝트 전체를 리뷰시키면 생각할 공간이 늘고 *"using sub-agents preserves the main agent's context window rather than polluting it"*(41:08~41:16). *"The agent can usually find important issues during a second look."*(41:36~41:41) → [[generator-evaluator-pattern]]
- **계획/기능 단계의 분리**가 *"not overflow context, ours and agents"*(38:29~38:34) — 컨텍스트 과부하를 **사람과 에이전트 양쪽**의 문제로 본다.

## MVP — 헌법과 스펙의 극한 시험 (42:32~45:47)

경영진이 MVP를 요구 → 나머지 로드맵 전체를 한 번에 구현시킨다. 조건을 단다: *"you should only implement such a large chunk if you feel confident in the quality of your constitution and spec"*(43:11~43:18), 그리고 리뷰·검증을 감당할 수 있어야 한다(43:27~43:28). 결과가 어긋나면 *"very responsibly carry out another replanning phase to eliminate whatever led the agent astray"*(43:44~43:51). MVP 뒤에는 코드 대신 **스펙을 검증**시킨다 — 에이전트가 *"places where the MVP found holes in our planning"*(45:13~45:16)을 보여 줬다.

## 레거시(brownfield) 도입 — 헌법을 역설계한다 (45:51~49:56)

*"People say spec-driven development and even AI are only good for greenfield projects. But SDD is also good for existing legacy projects."*(45:51~46:02)

- **데모의 한계**: 레거시는 **방금 만든 Agent Clinic MVP에서 `specs/` 폴더를 뺀 것**이다(46:06~46:21). 진짜 레거시가 아니라 **AI가 만든 지 얼마 안 된 작은 코드베이스**다.
- **같은 프롬프트, 다른 입력**: lesson four의 헌법 프롬프트를 거의 그대로 쓰되 **기존 아티팩트(to-do 파일)에서 로드맵 항목을 찾게** 한다(46:43~46:50). 실제 프로젝트라면 이슈 트래커·스프레드시트·워드 문서(46:31~46:36).
- **역설계**: *"the agent will discover and, in a sense, reverse engineer the SDD artifacts from the existing codebase"*(46:53~46:58). 헌법은 앞으로의 변경을 기존 코드와 정렬한다(47:01~47:06). 대화는 코드·커밋·문서가 있어 *"richer"*(47:21~47:29). 결과: mission에 대상과 아이디어, tech stack에 **파일 구조·프레임워크 버전**, roadmap은 to-do와 맞는 단계(47:35~48:00).
- **이후는 동일한 루프** — 1단계 feedback form 기능을 plan → implement → validate(48:18~49:23). 도입 직후 재계획에 시간을 주라 — *"you may find a lot of things to tune"*(49:32~49:38).
- 맺음: *"The spec is now the memory of the project"*(49:53~49:56).

위키의 레거시 소스들과 비교하면 이 절은 **가장 얇다** — [[tech-bridge-legacy-code-modernization-ai]]의 **아무도 완전히 이해하지 못하는 코드와 은퇴하는 사람의 지식**, [[tech-bridge-cursor-legacy-refactoring]]의 **감사 → 코드 없는 전략 plan → 티켓 분해** 같은 문제를 다루지 않는다. 역설적으로 데모의 "레거시"는 **방금 에이전트가 만든 코드베이스**라서, [[greenfield-vs-brownfield-agent-risk]]가 가장 위험하다고 본 쪽(새로 시작한 바이브 코딩 프로젝트)에 가깝다 — 다만 이 강좌의 코드는 헌법·스펙 아래에서 만들어졌다.

## 스킬로 자동화 — "faster and lighter weight" (49:59~56:53)

- **feature-spec 스킬**: 기능 스펙을 시작할 때마다 같은 프롬프트(*"Do this, do that, write these three files"* 50:22~50:24)를 반복하므로, 에이전트의 **skill creator**로 대화하며 스킬을 만든다(50:27~50:35). 커뮤니티에 이런 스킬이 많다(50:37~50:42). 스킬은 **프로젝트별 또는 global**(51:07~51:10).
- **호출**: 프롬프트에서 스킬을 먼저 부르거나, **스킬이 다른 스킬을 부르게** 한다(51:16~51:27). ⭐ progressive disclosure의 한계를 명시한다: *"agents use the skill description to decide when to call it in a process called progressive disclosure, but their judgment isn't always perfect, especially as the context window gets larger."*(51:29~51:44) 처방: *"Use the same heuristic as file tagging. If you know you want a skill used, name it."*(51:45~51:51)
- **슬래시 커맨드 → 스킬**: *"many agents are moving from custom {slash} commands over to skills"*(52:05~52:10).
- **MCP → CLI + 스킬**: MCP는 지금까지 *"the universal way to extend an agent"*(52:21~52:27). 예: 패키지 최신 문서를 주는 **Context7**. 그러나 *"skills that use code tools like a CLI (…) often accomplish the same purpose more elegantly"*(52:49~52:58) — Context7 설치 화면이 **MCP 서버 대 CLI+skills**를 고르게 하고 강좌는 후자를 고른다(53:14~53:21). *"People are rethinking MCP because CLI tools can take action with less setup and less context usage."*(53:56~54:02) → [[model-context-protocol]] · [[push-vs-pull-context-retrieval]]
- **plugins**: Claude Code 등의 *"collection of agent extensions that can be installed and updated"*(54:16~54:23). ⚠️ *"plugins are not yet a cross-agent standard. Like apps or dependencies, plugins can execute code. So, make sure you trust them on install and update."*(54:31~54:42)
- **Spec Kit · OpenSpec**: [[github-spec-kit|GitHub Spec Kit]]은 *"one attempt at formalizing a spec-driven development workflow with agents"*(54:43~54:49), 슬래시 커맨드 *"SpecKit.constitution, plan, tasks, and implement"*(54:59~55:01). **OpenSpec**(Fission AI)은 propose · explore · apply · archive — *"propose and explore match with the plan step, apply matches with implement, and archive matches with replanning"*(55:10~55:20), quick feature용 canonical pattern도 있다. 둘 다 브랜치 관리·검증 스크립트·*"opinionated spec document formats"*(55:26~55:34). 권고: 이 오픈소스 워크플로로 **자기 것을 다듬는 데** 실험하라(55:35~55:39).
- **리서치 backlog**: 기능 작업 중 떠오른 아이디어(예: DB 선택)는 로드맵에 넣지 않고 에이전트에게 **잘 알려진 위치에 보고서를 쓰게** 해 보관 → 나중에 링크와 함께 로드맵에 올린다(55:40~56:34).
- 정리: *"You can adopt an existing STD[=SDD] framework or tool, then customize it using skills"*(56:40~56:50).

## 에이전트 독립 — 네 표준 (56:54~1:00:24)

*"Since agents and models progress so fast, you don't want your workflow tied to just one choice."*(56:56~57:05) 네 표준: *"MCP for external tools, agents.md for rules, agent skills for capturing repeatable workflows with extra context, and ACP for connecting agents to clients."*(57:14~57:31)

- **Codex로 이식**: lesson 12의 feature-spec 스킬을 Codex의 다른 경로에 복사 — *"It runs just fine once migrated."*(57:45~57:53) 같은 프로젝트에서 에이전트를 오가며 SDD 워크플로를 유지한다.
- **ACP**: *"ACP makes it easy to connect agents and editors"*(58:11~58:13). **ACP registry**가 *"finding, installing, and connecting agents within clients"*(58:20~58:28)를 자동화한다. 데모: JetBrains IDE의 AI 채팅 창 → registry → **OpenCode** 설치(필요하면 OpenCode 자체 설치까지) → IDE 네이티브 통합(58:35~59:09). 프로토콜은 *"matches what's used in LSP"*(59:33~59:34), *"next edit suggestion in the editor and plan mode"*(59:40~59:43)까지 덮고, 로컬 커스텀 에이전트도 쓸 수 있다(59:45~59:51). → [[agent-client-protocol]]
- **에이전트 선택**: 리더보드는 빨리 바뀌니 자기 기준으로(59:53~1:00:09). *"Our specs work at a higher level, not tied to any one agent or IDE."*(1:00:11~1:00:13)

## 기존 위키와의 대조

### 합치하는 것

- **프롬프트가 아니라 스펙이 남는다** — [[tech-bridge-spec-driven-development]]의 *"the specification as that main artifact"* 와 같은 축. 이 강좌는 vibe coding의 대화 이력이 *"will not even be saved"*(04:56~05:00)라고 말하고, 스펙을 *"a permanent technical artifact"*(05:19~05:22)라 부른다.
- **AI가 만든 문서를 전부 리뷰** — 08-29 편의 *"review every single document"* 와 같다. 이 강좌는 매 단계 human-in-the-loop 리뷰 후 커밋을 반복한다.
- **헌법은 living document** — 08-29 편과 같은 표현(19:59~20:00, 29:48).
- **에이전트가 사람을 인터뷰한다** — [[tech-bridge-ai-native-sdlc]]의 [[intent-md|`intent.md`]]를 에이전트가 인터뷰로 만드는 것과 같은 동작. 다만 이 강좌에는 intent 층이 따로 없다.
- **스킬로 반복 작업을 묶는다** — [[agent-skills]]의 *"definable, repeatable workflows"*(33:44~33:49) 정의가 위키의 기존 정의와 맞는다. **스킬 이름을 직접 부르라**는 처방은 progressive disclosure의 실패 조건(컨텍스트가 커질 때)을 짚는다.
- **MCP의 재고** — [[tech-bridge-graft-code-knowledge-graph]]의 CLI 대 MCP 측정, [[tech-bridge-brockman-agi-era-defender-window]]의 *"세상을 다시 도구화"* 에 **교육 콘텐츠 쪽의 "CLI+스킬로 옮겨 간다"** 가 더해졌다. ⚠️ 근거(설정·컨텍스트 사용이 적다)는 주장이고 측정이 없다.

### 갈리는 것

> ⚠️ **Contradiction: 헌법에 무엇이 들어가나.** [[tech-bridge-spec-driven-development]](Spec Kit)의 constitution은 **깨지지 않는 규칙**(testable by design · 보안 · privacy by default 등 must-have)이고, 기술 스택은 **기능별 plan**에 들어간다(*"Spec = what만, how/스택 금지"*). 이 강좌의 헌법은 **mission · tech stack · roadmap** 세 파일이고, **기술 스택이 프로젝트 수준 헌법**에 있다(10:39~10:45, 18:59~19:04). 로드맵(기능 목록과 순서)도 헌법 안이다. 두 소스는 같은 단어(constitution)로 **다른 문서**를 가리킨다. 이 위키는 어느 쪽도 정답으로 두지 않고 [[spec-driven-development]]에 두 정의를 나란히 둔다.

> ⚠️ **Contradiction: 헌법은 불변인가 가변인가 — 강좌 안에서.** 인트로는 *"a constitution at the project level to define the **immutable** standards"*(02:31~02:36)라고 하고, 본문은 *"living document"*(19:59~20:00, 29:48~29:50)로 두고 재계획마다 고친다. 이 위키는 **본문의 운영(가변, 별도 브랜치로 버전 관리)** 이 강좌의 실제 주장이라고 읽지만, 두 표현이 한 영상에 있다는 것만 표시한다.

> ⚠️ **Contradiction: 계획을 믿는가.** [[tech-bridge-pstack-third-party-review]]가 전한 [[lauren-tan|Lauren Tan]]의 입장은 *"나는 계획을 믿지 않는다. 최고의 사양은 코드다"* 이고, Pstack은 **BMAD·Superpowers·OpenSpec 같은 사양·계획 도구가 아니라고** 스스로 구분한다. 이 강좌는 정반대로 **계획·스펙을 개발자의 주 업무**로 둔다(*"most of your work as a developer is in planning and validation, rather than implementing"* 35:32~35:38). 두 소스가 **OpenSpec을 서로 반대 방향에서** 언급한다. 대상이 다르다는 점은 짚어 둔다 — Pstack은 *"이미 자리 잡은 코드베이스 위에서 운영"*, 이 강좌는 greenfield부터 시작해 레거시를 **역설계로 헌법 위에 올린다.**

- **기능 스펙의 모양**: Spec Kit은 spec(what) → plan(how) → tasks, 이 강좌는 기능마다 **plan · requirements · validation** 세 문서다. **validation(성공 기준·스코어카드)이 처음부터 1급 문서**라는 점이 [[verifiable-goals]]·[[sprint-contract]]에 더 가깝다.
- **재계획이 명시적 단계**다. 08-29 편에는 없었다. OpenSpec의 *archive*를 재계획에 대응시키는 것(55:18~55:20)도 이 강좌의 해석이다.
- **도구 중립성**: 08-29 편은 Spec Kit 한 도구의 시연이었고, 이 강좌는 Spec Kit을 **"one attempt"** 로 낮추고 **표준(MCP · AGENTS.md · skills · ACP)을 중립성의 근거**로 둔다. 다만 강좌 스스로 헌법을 *"agent agnostic"* 이라 부르면서 AGENTS.md를 네 표준 중 하나(*"agents.md for rules"* 57:20)로 드는데, **헌법과 AGENTS.md의 역할 분담**은 설명하지 않는다.
- **[[kiro|Kiro]]는 나오지 않는다.** [[tech-bridge-frontier-engineering]]의 Amazon 현장 SDD와 연결할 발화는 없다.

## 해소하지 않고 표시만 한 것

- **강사 이름의 철자** — Everett(en-orig) / Everitt(en) / 에버릿(ko). **소개자 "Andrew"의 성** — 발화 없음. **기여자 Chayka/Chicherin.**
- **레슨 본문의 내레이터** — 04:21 이후 누가 말하는지 자막이 밝히지 않는다. 1:01:22 *"I really care about finding the joy and purpose in all things"* 의 "I"가 강사인지도 확인되지 않는다.
- **"nano"** — *"Must have been the nano"*(21:38), *"we said nano"*(25:02), *"Nano really meant nano"*(25:51). 무엇의 이름인지(로드맵 granularity 선택지인지 모델인지) 자막은 말하지 않는다.
- **"React 9.2 … React 9.0"**(52:44~52:47) — 두 트랙 모두 이 숫자. 보정하지 않는다.
- **"each merge domain"**(33:33) — *merge to main*의 ASR일 개연성, 미확정.
- **"Take it sleazy."**(1:01:29) — en *"Behave badly"*, ko *"나쁘게 행동해"*. 미확정.
- **세 이점의 근거** — 측정 없음. MVP의 성공은 자기 평가.
- **스펙 버전 관리** — 강좌 스스로 *"evolving topic"* 이라 했다(28:34~28:42). 어떤 스펙이 어떤 코드를 만들었는지 추적하는 방법은 **브랜치 분리 규칙** 외에 제시되지 않는다.
- **플러그인 신뢰** — *"make sure you trust them"* 이 처방의 전부다. 무엇을 기준으로 신뢰하는지는 없다.
- **설명란 링크**(`bit.ly/4ArdsT3`) — 열어 보지 않았다. 원 강좌의 공식 제목·플랫폼 페이지도 확인하지 않았다.

## 등장 개체

- 인물: [[paul-everitt]](강사, 표기 미확정) · "Andrew"(→ [[andrew-ng]] 추정, 미확인) · Konstantin Chayka/Chicherin · Zina Smirnova · Isabel Zaro (페이지 없음)
- 조직: [[jetbrains]] · DeepLearning.AI(페이지 없음) · Fission AI(페이지 없음) · GitHub · [[openai]]
- 제품·도구: [[claude-code]](AskUserQuestion · `/clear` · skill creator · global skills · plugins) · WebStorm · [[github-spec-kit]] · OpenSpec · [[codex]] · OpenCode · [[zed]](13:20 언급) · VS Code · Gemini · ChatGPT · Context7 · Hono · Next.js · React · Pico CSS · SQLite · Prisma · MongoDB
- 개념: [[spec-driven-development]] · [[cognitive-debt]](신규) · [[agent-skills]] · [[model-context-protocol]] · [[agent-client-protocol]] · [[context-rot]] · [[generator-evaluator-pattern]] · [[verifiable-goals]] · [[sprint-contract]] · [[greenfield-vs-brownfield-agent-risk]] · [[verification-bottleneck]] · [[intent-md]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=FJo7p9SPS9c> (1:01:33, `upload_date` 2026-09-26 — 09-23 멤버 전용으로 처음 게시)
- raw: `01.raw/articles/2026-09-26_AI 에이전트와 함께하는 스펙 주도 개발 풀코스 강의.md`
- 설명란 링크: <https://bit.ly/4ArdsT3> (⚠️ 이 위키는 열어 보지 않았다)
- 같은 주제: [[tech-bridge-spec-driven-development]](08-29, Spec Kit) · [[tech-bridge-ai-native-sdlc]] · [[tech-bridge-frontier-engineering]] · 반대 입장 [[tech-bridge-pstack-third-party-review]]
- [[tech-bridge]] · [[jetbrains]] · [[paul-everitt]]
