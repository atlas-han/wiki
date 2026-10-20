---
title: "지연 도구 컨텍스트 (Deferred Tool Context)"
type: concept
category: technique
tags: [tools, tool-bloat, progressive-disclosure, context-engineering, lazy-loading, mcp, tokens]
related: [toolbox-pattern, context-engineering, agent-skills, context-rot, context-resets-and-compaction, model-context-protocol, agent-tool-design-practices, software-factory, push-vs-pull-context-retrieval, harness-as-platform, codex-app-server, embedded-agent-harness, prompt-caching, context-failure-modes]
first-seen: tech-bridge-factory-software-factory
sources: [tech-bridge-factory-software-factory, tech-bridge-uber-debug-assist, tech-bridge-composio-dashboard-is-dead, tech-bridge-codex-app-server, tech-bridge-lee-robinson-always-on-agents, tech-bridge-context-engineering-four-failure-modes]
created: 2026-10-02
updated: 2026-10-20
---

# 지연 도구 컨텍스트 (Deferred Tool Context)

**연결된 도구의 전체 스키마를 처음부터 컨텍스트에 싣지 않고, 짧은 목록과 짧은 설명만 두었다가 에이전트가 실제로 필요로 할 때 그 도구를 호출해 전체 정의를 로드하는 방식.** 도구에 적용한 progressive disclosure. [[factory-ai|Factory]]는 이를 **deferred context engine**이라 부른다 — [[tech-bridge-factory-software-factory]] ([[tereza-tizkova|Tereza Tížková]]).

> *"we just progressively disclose what's in the context and what tools to use"* (16:00~16:05) · *"important thing is nothing is actually removed. is just hidden and not reachable until needed"* (16:23~16:29)

> ⚠️ **벤더 수치.** *"you can save 50% of tokens or more"*(16:40~16:42) — 도구가 많을수록 절감이 커진다는 말뿐, 측정 조건(도구 수, 과제, 기준선)이 없다.

## 문제 — 도구 bloat (15:07~15:52)

- 기업은 Figma·Notion·Gmail·Drive·Slack 등 *"hundreds tools on average"*(15:25~15:30, ⚠️ 출처 없음)
- 도구마다 *"specification in the code (…) schema and parameters and log[=long] descriptions"*(15:33~15:37)
- 결과 둘: ① **비슷한 이름의 도구를 잘못 고른다**(*"pick wrong tools if there are two tools that sound similar"* 15:41~15:45) ② **컨텍스트를 잃는다** — 창을 채워 *"need to compress"*(15:45~15:50) → [[context-rot]] · [[context-resets-and-compaction]]

*"there is this elephant in the room, context with agents"*(15:07~15:10) — 장기 미션을 도는 [[software-factory]]에서 특히.

## 메커니즘 (15:55~16:42)

1. 처음엔 *"short list of the tools and uh only a short descriptions"*(16:14~16:19)
2. 코드 작업 중 필요해지면 *"they can call the tool and fully load it"*(16:19~16:23)
3. 지워지는 것은 없다 — 숨겨져 있을 뿐(16:23~16:29)
4. 도구가 많을수록 절감이 커진다(16:32~16:42)

판독 미확정: *"we basically have a surprise tools uh that help later only if they are actually needed"*(16:05~16:11) — 세 자막 트랙 모두 *surprise tools*. "필요할 때만 나중에 꺼내는 도구" 정도로 읽는다.

## 같은 결론, 다른 메커니즘

| | **지연 도구 컨텍스트** (Factory) | **[[toolbox-pattern\|툴박스 패턴]]** (Oracle) | **[[agent-skills\|스킬]]** progressive disclosure |
|---|---|---|---|
| 상시 컨텍스트 | 도구 이름 + 짧은 설명 목록 | 없음 — 매 반복 검색 결과만 | 스킬 프런트매터 몇 줄 |
| 로드 트리거 | **에이전트가 도구를 호출**할 때 | 하네스가 **벡터 검색**으로 매 반복 조립 | 에이전트가 스킬을 고를 때 |
| 빼기 | 언급 없음(숨김 → 로드) | 필요 없어지면 뺀다 | 언급 없음 |
| 규모 대응 | *"hundreds tools"* | *"도구가 수천 개면?"* → 인덱스 | 스킬 수가 늘면 판단 흐림 우려 |

공통: **목록은 싸게, 본문은 필요할 때.** 차이: 누가 고르는가(에이전트 vs 검색 하네스)와, 한 번 로드한 정의를 다시 빼는가.

> 위키의 정리: Factory의 방식은 **에이전트가 짧은 설명만 보고 도구를 고를 수 있어야** 성립한다 — 그런데 화자가 든 첫 번째 실패가 *비슷한 이름의 도구를 잘못 고른다*였다. 짧은 설명이 그 혼동을 줄이는지 키우는지는 말하지 않는다. [[agent-tool-design-practices]]의 *도구 이름·설명 설계*가 여기서 더 중요해진다.

## 미해결

- **프롬프트 캐시와의 관계** — 로드할 때마다 도구 정의가 추가되면 캐시 접두가 바뀌는가. [[toolbox-pattern]]도 같은 질문(매 반복 재조립의 비용)을 미해결로 둔다.
  (2026-10-18) 한 가지 답: 이름만 싣고 **턴 중에는 도구 목록을 바꾸지 않는다**([[tech-bridge-lee-robinson-always-on-agents]] 25:23~25:28). 로드한 정의가 접두에 붙는지 뒤에 붙는지는 여전히 발화되지 않았다. → [[prompt-caching]]
- 짧은 설명을 누가 쓰는가(사람 vs 자동 요약).
- 50% 절감의 측정 조건.

## 같은 문제, 다른 답 — 에이전트 타입으로 미리 자르기 (2026-10-09 · [[tech-bridge-uber-debug-assist]])

[[uber|Uber]]도 같은 bloat를 겪었다: *"Uber has a skills marketplace which is huge. There are almost 3,000 plugins right now and we can't dump the context of all the plugins to an agent. It goes crazy."*(17:09~17:21) 답은 progressive disclosure가 아니라 **정적 범위 지정** — *"this is how we do it using the agent type parameter"*(17:23~17:27). 에이전트 타입이 실행 시 가져올 바이너리·런타임·스킬·플러그인을 정한다.

| | Factory (지연 도구 컨텍스트) | Uber (에이전트 타입) |
|---|---|---|
| 언제 고르나 | 실행 중, 에이전트가 필요할 때 | 실행 전, 에이전트 타입으로 |
| 누가 고르나 | 모델 | 플랫폼 설정 |
| 대가 | 목록·설명은 늘 컨텍스트에 | 타입 밖 도구는 아예 못 씀 |

⚠️ 둘 다 측정치 없음(Factory *"50% of tokens or more"* 는 조건 없음, Uber는 수치 없음). → [[harness-as-platform]]

## 세 번째 답 — 과제를 말하면 도구와 "계획"을 돌려준다 (2026-10-10 · [[tech-bridge-composio-dashboard-is-dead]])

[[composio|Composio]]의 [[sarah-simionescu|Sarah Simionescu]]: *"if you connect enough servers, you're dumping thousands of tool definitions straight into the context window. I mean, our GitHub like toolkit alone has over 200 tools. The model just drowns. it grabs the wrong tool or struggles to resolve dependencies and it can't figure out which one it needs to call first."*(03:58~04:17) — Factory가 든 실패(비슷한 도구 오선택) 위에 **의존성·호출 순서**를 더한다.

답은 **Composio search**: 에이전트가 먼저 *"to state the task it wants to accomplish"*(05:08~05:13, 데모에선 Slack 메시지·[[sentry|Sentry]] 이슈·Datadog 로그 셋), 서비스가 과제마다 *"not only the correct tools it needs, but actually a plan of how to use them"*(05:20~05:27)을 돌려준다 — 예: Slack은 채널 ID를 먼저 찾아야 메시지를 조회할 수 있다(05:27~05:33).

| | Factory | Oracle([[toolbox-pattern]]) | Uber | **Composio** |
|---|---|---|---|---|
| 상시 컨텍스트 | 짧은 도구 목록 | 없음 | 타입별 도구 | 검색 도구 하나(위키의 독해) |
| 고르는 주체 | 모델 | 하네스(벡터 검색) | 플랫폼 설정 | **도구 제공자(과제 진술 → 반환)** |
| 순서·의존성 | 언급 없음 | 언급 없음 | 고정 골격 | **계획으로 함께 반환** |

⚠️ 데모는 화자 스스로 **목업**(*"a mockup demo"* 04:42~04:45). 계획을 누가 어떻게 만드는지, 검색이 빗나갈 때의 폴백은 발화되지 않는다. → [[agent-native-interface]]

## 네 번째 답 — 하네스의 플래그: `deferred` + tool search (2026-10-14 · [[tech-bridge-codex-app-server]])

[[dominik-kundel|Dominik Kundel]]([[openai|OpenAI]] Codex): [[codex-app-server|App Server]]로 도구를 직접 정의할 때 *"you can actually mark them as deferred loading, which means that rather than injecting them into the system prompt, it uh allows Codex to use a tool search tool (…) but allows it to find these tools through tool search rather than polluting the uh overall context window."*(07:47~08:07) 그리고 팁 ②로 다시 — *"expose new um functions (…) But mark them as deferred. That way you're not polluting the context window unnecessarily (…) and instead still have them available for the agent without um necessarily confusing it."*(16:24~16:53) Codex app 자신도 자기 제어 함수(자동화 띄우기 등)를 이렇게 노출한다(16:30~16:40).

| | Factory | Oracle | Uber | Composio | **Codex(OpenAI)** |
|---|---|---|---|---|---|
| 누가 만든 장치 | 하네스 사용자(제품) | 하네스 사용자 | 사내 플랫폼 | 도구 공급자 | **하네스 제작사 — 도구 정의의 플래그** |
| 상시 컨텍스트 | 짧은 목록 | 없음 | 타입별 | 검색 도구 | tool search 도구(위키의 독해) |
| 고르는 주체 | 모델 | 하네스 | 설정 | 공급자 | 모델(tool search 호출) |

- ⚠️ tool search의 동작(검색 방식, 짧은 설명을 쓰는지, 찾지 못할 때)은 *"we'll cover more tomorrow in the other session"*(07:56~07:58)으로 미뤄져 이 소스에 없다. 측정치도 없다.
- 이 페이지의 첫 우려(*비슷한 이름의 도구를 잘못 고른다*)에 대해 화자는 *"without um necessarily confusing it"* 이라고만 말한다.
- ⚠️ ko는 *"available for the agent"* 를 **"에이전트가 사용할 수 없음"**(16:50)으로 뒤집는다. `en`은 deferred를 *"lazy-loaded"*, tool search를 *"tool lookup tool"* 로 옮긴다.

## 다섯 번째 목소리 — "tool search tool", 그리고 캐시 (2026-10-18 · [[tech-bridge-lee-robinson-always-on-agents]])

[[lee-robinson|Lee Robinson]]([[grokbot|GrokBot]]): *"one kind of context engineering or harness trick um that a lot of the the popular harnesses now use is uh it's called dynamic context or I think uh some other folks call it the tool search tool which is a fun name (…) you're only putting the names of the tools into the every message"*(20:51~21:11). 문제 서술은 이 페이지와 같다. Google Drive·Gmail·YouTube 커넥터를 깔수록 블록이 찬다(20:29~20:44). 메커니즘은 Codex 편의 `deferred` + tool search와 같은 쪽이다. 새로 더하는 것은 둘이다.
- **캐시**: *"ideally you don't add or remove new tools during turns"*(25:23~25:28). → [[prompt-caching]]
- **"가장 싼 것부터" 사다리**: 대화 기록 → 플러그인·MCP·API → 웹 검색 → 브라우저 → 데스크톱 → 사용자(21:30~22:25). 도구를 고르는 순서를 비용·신뢰도로 정한다.

## References

- [[tech-bridge-factory-software-factory]] — first-seen
- [[toolbox-pattern]] · [[agent-skills]] · [[context-engineering]] · [[model-context-protocol]] · [[push-vs-pull-context-retrieval]] · [[software-factory]]
- [[factory-ai]] · [[tereza-tizkova]]

## 정확도 쪽 수치 하나 — 46개에서 실패, 19개에서 통과 (2026-10-20 · [[tech-bridge-context-engineering-four-failure-modes]])

[[martin-keen|Martin Keen]]([[ibm|IBM Technology]])은 도구 bloat를 *context confusion*이라 부르고 수치를 든다: *"in one benchmark, a model failed a task when it was offered 46 tools, but it then passed the very same task when it was only offered 19 tools. That is tool sprawl at work."*(06:37~06:52) Factory의 *"50% of tokens"*(벤더, 비용 쪽)와 달리 **정확도 쪽** 수치다. 처방 curate는 이 페이지의 메커니즘을 이름 없이 말한다: *"The agent doesn't need 46 tools for database migration. So, just give it the handful that the job calls for and then it can always go and fetch others if it actually needs them."*(08:50~09:02) → [[context-failure-modes]]

⚠️ 벤치마크·모델 이름은 발화되지 않는다. 통합자 확인으로는 Drew Breunig의 *"How Long Contexts Fail"*(2025-06)이 같은 46 vs 19 사례(GeoEngine 벤치마크, 양자화한 Llama 3.1 8B)를 인용한다. 소형 양자화 모델 하나의 단일 과제라면 일반화 범위는 좁다. 화자가 이 사례를 가리킨 것인지는 확인되지 않았다.
