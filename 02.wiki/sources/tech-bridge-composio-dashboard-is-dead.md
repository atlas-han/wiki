---
title: "Tech Bridge — 대시보드는 끝났습니다 (Sarah Simionescu · Composio): MCP는 문이지 지도가 아니다, 에이전트를 위한 인터페이스"
type: source
tags: [agent-native-interface, mcp, tool-overload, cross-app, context-engineering, dashboards, composio, vendor-claim, video]
source-url: https://www.youtube.com/watch?v=5bg469hWGGc
source-type: video
author: Tech Bridge (한영자막 재배포) · 발표 [[sarah-simionescu]] ([[composio|Composio]], 팀이 Composio 대시보드 담당 · 직함 미발화) · 행사명 미발화(설명란 ai.engineer 링크 → AI Engineer 계열 추정) · 2026년 녹화
date-published: 2026-10-09
ingested: 2026-10-10
created: 2026-10-10
updated: 2026-10-10
---

# Tech Bridge — 대시보드는 끝났습니다 (Sarah Simionescu · Composio)

[[tech-bridge|Tech Bridge]]가 재배포한 **10:12 단독 발표, Q&A 없음, 공식 챕터 18개.** 화자는 [[composio|Composio]]의 [[sarah-simionescu|Sarah]] — 발화엔 이름 *"Sarah"*(00:00~00:03)와 *"my team is responsible for the Composio dashboard"*(01:00~01:06)뿐이고 성 Simionescu는 설명란 링크에만 있다. 이 위키의 **두 번째 Composio 발표**다(첫 번째는 CTO [[karan-vaidya|Karan Vaidya]]의 [[tech-bridge-knowledge-work-agent-infrastructure]]). 테제는 하나:

> **대시보드와 쿼리 언어는 사람과 데이터 사이의 번역 장치였고, 이제 그 자리를 에이전트가 차지했다. MCP는 에이전트에게 모든 앱으로 가는 문을 줬지만, 프로토콜일 뿐 "어떻게 말할지"는 서비스 몫이다 — 그래서 에이전트는 배우지 못하고, 도구에 익사하고, 앱 사이에서 길을 잃는다. 다음 시대는 에이전트가 쓰기 쉬운 제품의 것이다.**

> *"The dashboard is dead."* (00:52~00:55) · *"You never wanted a dashboard or it's cursed query language. You wanted the answer."* (02:12~02:20) · *"MCP is a protocol. It's a channel for communication between agents and your service. And it's up to you, the service, to choose how to communicate with the agent. And it turns out that makes all the difference."* (03:19~03:31) · *"MCP gave agents a door into every app. but it left them standing in thousands of separate rooms with no map and no memory of ever being there."* (04:32~04:42) · *"You are now serving a new species of user. They don't have eyes."* (09:30~09:36)

이 위키에 개념 하나가 생긴다 → [[agent-native-interface]] (신규).

ASR·ko 보정: ko는 네 핵심어를 전부 흔든다 — **Composio**("작곡가"·"침착함"·"Composure"·"콤포지아"), **dashboard**("제어판"·"패널"·"책"·"이사회"·"보드게임"), **agents**("상담원"·"경찰관"·"요원"·"자치령 대표"), **query**("상담"). 그리고 **부정·방향을 다섯 군데서 뒤집었다**: *they don't even agree on SQL* → **"SQL에 동의합니다"**(01:58), *does not require more than two joins* → **"언제나 답을 제공"**(02:34~02:38), *dumping … into the context window* → **"버리게 될 겁니다"**(04:01), *without loading the full results into its context* → **"모든 결과를 로드하세요"**(07:57~08:01), *They don't have eyes* → **"그들에게는 눈이 있다"**(09:32~09:34). 벤치마크의 *unreleased* 는 **"발표된"**(06:17~06:21), *GEO* 는 **"SEO"**(08:56, `en` 공유 오류), *For a decade* 는 **"수십 년"**(09:44). 결론 문장 *"the next era belongs to those that are easy for agents to use"* 는 **"다음 시대는 인류의 시대입니다"**(09:50~09:54)로 무너졌다. en-orig 판독: *"Century Data Dog"*(05:01) → Sentry, Datadog · *"post talk"*(01:27) → PostHog · *"Enthropic"* → Anthropic · *"clawed uh marketplace"* → Claude · *"reax string"* → regex. 전체 목록은 raw.

> ⚠️ **당사자 진술 — 화자는 Composio 직원이고 결론은 자사 제품이다.** *"the dashboard is dead"* 를 말하는 사람의 팀이 *"responsible for the Composio dashboard"*(01:00~01:06)라는 자조로 시작하지만, 발표 후반 3분은 Composio 제품 서술이다. *MCP만으로는 부족하다* 는 진단과 *그 부족을 Composio가 메운다* 는 처방은 분리해서 읽어야 한다.
>
> ⚠️ **벤치마크 — 수치가 발화되지 않는다.** *"early unreleased uh results comparing Composio against each app's own native MCP that's listed in the clawed[=Claude] uh marketplace. So it's the same tasks is the same model and we see a clear difference."*(06:16~06:32). 지표·수치·과제 수·모델명은 슬라이드에만 있고 **자막엔 없다.** 비교 대상은 경쟁 MCP 서버다. 이 위키는 **"미공개 초기 결과, 우위 주장만 있음"** 으로만 기록한다.
>
> ⚠️ **첫 데모는 목업이다.** *"I'm going to show you a mockup demo here"*(04:42~04:45), *"So imagine in this mockup"*(04:49~04:54). 설명란의 *"5분 컷"* 은 목업 속 서술(*"less than five minutes"* 05:48~05:53)이다. 두 번째 데모는 목업이라는 말이 없고 *"live version"* 은 부스에서(08:37~08:43).
>
> ⚠️ **행사·시점.** 행사명 미발화. *"come visit us at the Composio booth"*(08:39~08:43) + 설명란 `https://ai.engineer` 링크 → **AI Engineer 계열 추정**(확정 아님). 연도는 *"how I would solve it in 2026"*(04:47~04:52) → 2026년 녹화. 업로드 2026-10-09.

## 1. 고백 — 매일 쓰면서 한 번도 열지 않은 대시보드 (00:00~01:06)

- 6개월간 매일 Datadog을 썼다(00:06~00:10). 동료가 알림을 같이 보자고 해서 열었더니 로그아웃 상태, 로그인하고 대시보드를 열자 *"I just froze. I had no idea where anything was."*(00:31~00:35)
- *"this is actually not a knock on data dog. The problem was I had genuinely never opened the dashboard. I'd been using it every day without ever looking at it."*(00:35~00:48) — 사용은 전부 에이전트를 거쳤다는 뜻(06:00~06:12에서 확인: Claude를 여는 게 *"muscle memory"*).
- ⭐ *"The dashboard is dead. And I think that's great news for everyone in this room except probably for me because I am my team is responsible for the Composio dashboard."*(00:52~01:06)

## 2. 회고 ① 2022 — 도구 다섯, UI 다섯, 쿼리 언어 다섯 (01:06~02:20)

- Slack에서 *"I get this error when I try and search for prod"*(01:17~01:22) → 창 다섯: Slack에서 맥락 읽기 · Datadog 쿼리 · PostHog 세션 확인 · VS Code에서 수정 · GitHub PR(01:22~01:33). *"That is five tools and five UIs I have to learn and relearn every time they ship a new redesign."*(01:33~01:39)
- 더 큰 문제는 쿼리 언어: Datadog 쿼리 구문, Jira의 JQL, Slack 검색 수정자 — *"even when these tools claim to speak the same language, let's say SQL, they don't even agree on SQL."*(01:52~02:02)
- ⭐ *"Every dashboard you've ever used, every weird obscure query language ever written was a translation device between you and your data because the machines on the other end could not understand what you actually wanted."*(02:02~02:15) → **대시보드 = 번역 장치**라는 정의가 [[agent-native-interface]]의 출발점이다.

## 3. 회고 ② 2023 sparkle 버튼, 2024 MCP (02:20~03:15)

- 2023: *"The sparkle button was born"*(02:28~02:30) — LLM이 *"a sometimes correct query"* 를 써 준다, *"That is if your question does not require more than two database joins."*(02:30~02:42) 곳곳에 퍼져 *"dashboards became AI native. Problem solved, right? Well, not quite."*(02:44~02:52)
- 2024년 11월 Anthropic이 MCP를 발표(02:52~02:57) → sparkle 버튼 대신 *"your own agent, Claude, whom you've already been using every day, could generate the query for you, execute it on your behalf, and give you the answer directly."*(03:01~03:12)

→ [[model-context-protocol]] · [[anthropic]]

## 4. MCP만으로는 부족한 세 이유 (03:15~04:42)

⭐ 전제: *"MCP is a protocol. It's a channel for communication (…) And it's up to you, the service, to choose how to communicate with the agent. And it turns out that makes all the difference."*(03:19~03:31) *"If you've ever actually wired up a dozen MCP servers, you will know the reality is a mess for three reasons."*(03:29~03:41)

| # | 이유 | en-orig | 위키 연결 |
|---|---|---|---|
| 1 | **에이전트는 학습하지 않는다** — 매 대화가 0에서 시작, 어제 Slack 링크 서식을 틀린 걸 기억 못 해 오늘 또 틀린다 | *"Agents don't learn. Every conversation starts from zero."* (03:37~03:43), 03:43~03:49 | [[agent-memory]] |
| 1′ | **스킬은 반창고** — 컨텍스트가 늘수록 에이전트는 멍청해지고, 도구·스킬을 더 실으면 컨텍스트가 더 든다 | *"we patch this with skills. But skills is just a band-aid because agents become dumber with the more context you provide."* (03:49~03:58) | [[agent-skills]] · [[context-rot]] |
| 2 | **도구가 너무 많으면 익사한다** — 서버를 충분히 붙이면 도구 정의 수천 개가 창에. 잘못된 도구를 잡고, 의존성을 못 풀고, 무엇을 먼저 부를지 모른다 | *"our GitHub like toolkit alone has over 200 tools. The model just drowns."* (04:03~04:11), 04:11~04:17 | [[deferred-tool-context]] · [[toolbox-pattern]] |
| 3 | **모든 앱이 고립돼 있다** — MCP 서버는 자기만 안다. 과제가 두 앱에 걸치는 순간(늘 그렇다) 이어 붙이는 건 사람 몫 | *"Each MCP server knows about itself and nothing else."* (04:20~04:25), 04:25~04:32 | [[knowledge-work-agent-gap]](중앙화) |

⭐ *"MCP gave agents a door into every app. but it left them standing in thousands of separate rooms with no map and no memory of ever being there."*(04:32~04:42) — 문(door) = 프로토콜, 지도(map) = 앱 간 계획, 기억(memory) = 학습. 세 이유를 한 문장에 접었다.

> 위키의 주석: 이유 2의 *"200개 넘는 도구"* 는 **Composio 자신의 툴킷**이다 — 즉 도구 과부하는 Composio가 만든 문제이기도 하고, 아래 *Composio search* 는 그 문제를 자기 쪽에서 푸는 장치다.

## 5. 데모 ① (목업) — Slack 버그 리포트 → 수정 PR (04:42~06:15)

1. Claude + Composio MCP. Slack 메시지 링크를 붙이고 *"Please use Century[=Sentry] Data Dog, find the root cause, create a draft PR, make no mistakes."*(04:57~05:06)
2. ⭐ 첫 호출은 **Composio search** — *"to state the task it wants to accomplish"*(05:06~05:13). 여기선 셋: Slack 메시지 가져오기 · Sentry 이슈 검색 · Datadog 로그 검색(05:13~05:20).
3. ⭐ *"for each of these three, Composio returns not only the correct tools it needs, but actually a plan of how to use them. So, for example, for Slack, you actually have to find the Slack channel ID before you can start querying for messages."*(05:18~05:33) — **도구 + 사용 순서(의존성)를 함께 반환.** 이유 2의 *"struggles to resolve dependencies"* 에 대한 답.
4. Slack 메시지로 사용자 불만 확인 → Datadog·Sentry **병렬** 조회 + 코드베이스 스캔 → 근본 원인 → *"PR is up with a fix in less than five minutes"*(05:33~05:53).
5. *"I didn't have to build a workflow or write a skill to teach it how to do this. This is literally just Claude using Composio's MCP."*(05:51~06:02)

⚠️ 목업이다(위 헤더). → [[deferred-tool-context]] · [[toolbox-pattern]]

## 6. 벤치마크와 "에이전트를 위한 새 인터페이스" (06:15~07:06)

- *"the impact of designing for agents is measurable"*(06:15~06:18) — 그러나 수치는 자막에 없다(⚠️ 헤더).
- ⭐ *"at Composeio we are developing a brand new interface specifically designed for agents. We translate messy, sparsely documented, everchanging APIs from all of the apps that you live in every day into something that agents really love to use. So, we build on top of MCP, CLI, and native tools to deliver a cohesive, unified, and excellent experience for your agents"*(06:37~07:01)
- 위키의 독해: 이 문장은 **MCP를 전송 계층으로 내리고, 그 위에 "인터페이스 설계" 층을 따로 세운다.** MCP·CLI·네이티브 도구가 **같은 층의 대안**으로 나란히 놓였다 — [[push-vs-pull-context-retrieval|Graft의 CLI vs MCP]], [[tech-bridge-sdd-full-course|SDD 강좌의 "MCP → CLI+스킬"]] 논쟁을 *"무엇 위에 짓느냐는 중요하지 않고 그 위의 설계가 중요하다"* 로 비켜 간다.

→ [[agent-native-interface]]

## 7. 데모 ② — PostHog × Metabase, 컨텍스트에 싣지 않는 교차 분석 (07:06~08:43)

1. 온보딩에서 사용자가 고른 버티컬(업종) 분포 → Composio search → PostHog 쿼리 작성·실행(07:12~07:28).
2. 이커머스 세그먼트가 어떤 **toolkit**(*"Toolkits is another word for apps we like to use at composio"* 07:38~07:41)을 쓰는지 — PostHog의 사용자 ID로 Metabase를 조회해야 한다(07:28~07:50).
3. ⭐ *"It queries the user ids of those who selected e-commerce from post hog and it actually saves it without loading the full results into its context."*(07:53~08:03)
4. Metabase 스키마 조회·샘플링으로 구조 파악(08:03~08:10).
5. ⭐ *"once it's confident, it actually uses a very cool tool called Composio remote workbench to dynamically generate an SQL query with a reax[=regex] string to search for all those user IDs again without ever loading the entire thing into its context window."*(08:10~08:26)
6. *"in less than a few minutes"*, 두 소스의 데이터(08:30~08:39).

위키의 독해: 중간 결과(사용자 ID 목록)를 **모델 컨텍스트가 아니라 실행 환경 쪽에 두고, 모델은 그것을 참조하는 쿼리만 쓴다.** [[retrieval-side-context-compression]](검색 쪽이 토큰을 줄여 준다)·[[file-system-agent]](결과를 파일로 두고 탐색)와 같은 계열 — *데이터는 창 밖에, 모델은 조작만.* ⚠️ *remote workbench* 가 코드 실행 샌드박스인지, ID를 어디에 저장했는지는 발화되지 않는다.

→ [[context-engineering]] · [[agent-native-interface]]

## 8. 모든 제품이 마주할 미래 — 새로운 종의 사용자 (08:43~10:12)

- *"Many startups have begun making their landing pages and their websites AI friendly for GEO purposes. But so few have really prepared their applications to be used by agents."*(08:51~09:03) — **사이트를 AI가 읽기 좋게(GEO)** 와 **앱을 에이전트가 쓰기 좋게** 는 다른 일.
- Composio는 *"a tool to help developers"*(09:03~09:05)로 시작했다 — 인기 앱을 에이전트용 도구로. 이제 *"the humans are tired of dashboards and their agents are tired of poorly designed MCP servers"*(09:15~09:21), 그리고 *"we're getting requests from startups saying their clients are begging for a way to use their services through their agents."*(09:19~09:28) ⚠️ 요청 건수·회사명 없음.
- ⭐ *"You are now serving a new species of user. They don't have eyes. They are not going to click your sparkle button. It shows up with a goal and a set of tools. And it judges you on exactly one thing, whether it can get the job done."*(09:30~09:47)
- ⭐ *"For a decade, we've built pro uh we've built products to be easy for humans to use. And the next era belongs to those that are easy for agents to use."*(09:44~09:59)
- 마무리: 얼어붙었던 Datadog 앞의 순간을 *"falling behind"* 가 아니라 *"a preview of what's to come"*(10:02~10:07)으로.

→ [[agent-native-interface]] · [[llm-as-search-user]]

## 이 위키와의 연결

### 이어지는 것

- **[[tech-bridge-knowledge-work-agent-infrastructure]] (Composio CTO)** — 같은 회사의 두 번째 발표. Vaidya는 여섯 primitive 중 **중앙화**(*"한 거래가 5개 앱에 흩어짐"*)를 말했고, Simionescu의 이유 3(*"Each MCP server knows about itself and nothing else"*)은 같은 결손을 **MCP 층에서** 다시 말한 것이다. 2022년의 *창 다섯* 도 같은 그림. 다만 Vaidya는 거버넌스·가역성을, Simionescu는 **인터페이스 설계·컨텍스트 절약**을 판다.
- **[[deferred-tool-context]] · [[toolbox-pattern]]** — 도구 과부하에 대한 **세 번째 메커니즘**: 에이전트가 **과제를 진술**하면(*"state the task"*) 서비스가 도구 **+ 사용 계획**을 돌려준다. Factory(목록에서 에이전트가 고름)·Oracle(하네스가 벡터 검색)·Uber(에이전트 타입으로 미리 자름)와 달리 **선택과 순서 결정을 도구 제공자 쪽이 맡는다.**
- **[[llm-as-search-user]]** — *"검색을 쓰는 쪽이 바뀌었다"* 를 검색 너머 **모든 SaaS 앱**으로 넓힌 형태: *"a new species of user"*.
- **[[agent-skills]]** — *"skills is just a band-aid"*(03:51~03:54). 이 위키가 줄곧 키워 온 스킬을 **컨텍스트 비용** 쪽에서 깎는 벤더 발언. 처방은 스킬을 더 쓰는 게 아니라 *계획을 도구 쪽에서 돌려주는 것.*
- **[[model-context-protocol]]** — *"MCP is a protocol (…) it's up to you, the service, to choose how to communicate"* — 이 위키가 MCP를 *연결 표준* 으로 다뤄 온 것에 **"표준 ≠ 좋은 인터페이스"** 라는 구분을 더한다.

### 갈리는 것

> ⚠️ **Contradiction: 사람용 인터페이스로 갈 것인가, 에이전트용 인터페이스를 따로 지을 것인가.** [[greg-brockman|Brockman]]([[tech-bridge-brockman-agi-era-defender-window]])은 MCP·CLI를 *"거의 뻣뻣한 방식"* 의 **과도기적 재도구화**로 보고 컴퓨터 사용(사람의 화면)을 목적지로 놓는다. Simionescu는 정반대로 **사람의 화면(대시보드)이 죽었고**, MCP조차 부족하니 **에이전트 전용 인터페이스를 더 깊이 지어야 한다**고 한다. 두 소스는 서로를 모르고, 각자 자기가 파는 쪽(범용 모델 vs 통합 계층)을 목적지로 본다. 이 위키는 판정하지 않는다 → [[agent-native-interface]].

> ⚠️ **"에이전트는 학습하지 않는다" vs 이 위키의 메모리·자기 개선 페이지들.** [[agent-memory]]·[[skill-self-improvement]]·[[agent-dreaming]]은 에이전트가 경험을 축적하는 장치를 다룬다. 화자의 *"Every conversation starts from zero"* 는 **기본 MCP 연결 상태**에 대한 서술이지 불가능성 주장은 아니다 — 그리고 화자의 처방(서비스가 계획을 돌려준다)은 학습을 에이전트 쪽이 아니라 **도구 제공자 쪽에 축적**하는 것으로 읽힌다(위키의 독해).

## 해소하지 않고 표시만 한 것

- **벤치마크 수치·지표·과제·모델** — 자막에 없다, *"early unreleased"*.
- **Composio search·remote workbench의 실제 구조** — 계획을 누가(LLM? 사람이 쓴 레시피?) 만드는지, ID를 어디에 저장하는지.
- **화자 직함, 행사명·도시** — 발화 없음.
- *"search for prod"*(01:17~01:19)의 *prod*.
- 설명란의 *"MCP 게이트웨이"* — 발화에 없는 말.

## 등장 개체

- 인물: [[sarah-simionescu]] (신규) · [[karan-vaidya]](같은 회사, 언급 없음)
- 조직: [[composio|Composio]] · [[anthropic|Anthropic]] · [[ai-engineer|AI Engineer]](⚠️ 추정)
- 제품·도구(페이지 없음): Datadog · Sentry · PostHog · Metabase · Slack · Jira(JQL) · GitHub · VS Code · Claude 마켓플레이스 · Composio search · Composio remote workbench
- 개념: [[agent-native-interface]] (신규) · [[model-context-protocol]] · [[deferred-tool-context]] · [[toolbox-pattern]] · [[agent-skills]] · [[context-rot]] · [[agent-memory]] · [[knowledge-work-agent-gap]] · [[llm-as-search-user]] · [[retrieval-side-context-compression]] · [[file-system-agent]] · [[context-engineering]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=5bg469hWGGc> (10:12, `upload_date` 2026-10-09)
- raw: `01.raw/articles/2026-10-09_대시보드는 끝났습니다 - AI 에이전트가 소프트웨어를 쓰는 법.md`
- 설명란 링크: <https://composio.dev/> · <https://composio.dev/mcp-gateway> · <https://www.linkedin.com/in/sarah-simionescu/> · <https://github.com/sarahsimionescu> · <https://www.sarahsimionescu.com/> · <https://ai.engineer> (⚠️ 열어 보지 않았다)
- 같은 회사: [[tech-bridge-knowledge-work-agent-infrastructure]] · 반대 방향: [[tech-bridge-brockman-agi-era-defender-window]] · 도구 과부하: [[tech-bridge-factory-software-factory]] · [[tech-bridge-oracle-agent-memory-harness]] · [[tech-bridge-uber-debug-assist]]
- [[tech-bridge]] · [[composio]] · [[sarah-simionescu]]
