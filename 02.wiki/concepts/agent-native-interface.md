---
title: "에이전트 네이티브 인터페이스 (Agent-Native Interface)"
type: concept
category: pattern
tags: [agent-native-interface, mcp, tool-design, dashboards, agents-as-users, context-engineering, saas]
aliases: [에이전트용 인터페이스, interface designed for agents, 에이전트를 위한 인터페이스, new species of user]
related: [model-context-protocol, agent-tool-design-practices, deferred-tool-context, toolbox-pattern, knowledge-work-agent-gap, llm-as-search-user, model-rendered-interface, agentic-sites, retrieval-side-context-compression, push-vs-pull-context-retrieval, file-system-agent]
first-seen: tech-bridge-composio-dashboard-is-dead
sources: [tech-bridge-composio-dashboard-is-dead, tech-bridge-cooking-with-codex]
created: 2026-10-10
updated: 2026-10-11
---

# 에이전트 네이티브 인터페이스 (Agent-Native Interface)

**소프트웨어 제품이 사람의 눈과 클릭(대시보드·쿼리 언어·버튼) 대신 에이전트를 1차 사용자로 놓고 노출하는 인터페이스.** 연결 규약([[model-context-protocol|MCP]]) 자체가 아니라 **그 위에서 "에이전트에게 무엇을 어떤 순서로 어떤 크기로 줄지"를 설계하는 층**이다. 이 위키 첫 소스는 [[composio|Composio]]의 [[sarah-simionescu|Sarah Simionescu]]([[tech-bridge-composio-dashboard-is-dead]]).

> *"You are now serving a new species of user. They don't have eyes. They are not going to click your sparkle button. It shows up with a goal and a set of tools. And it judges you on exactly one thing, whether it can get the job done."* (09:30~09:47)

> ⚠️ **첫 소스가 이 층을 파는 회사다.** 정의·필요성·효과 주장(미공개 벤치마크) 모두 당사자 진술이다.

## 논리 — 번역 장치의 교체

1. **대시보드와 쿼리 언어는 번역 장치였다** — *"Every dashboard you've ever used, every weird obscure query language ever written was a translation device between you and your data because the machines on the other end could not understand what you actually wanted."*(02:02~02:15)
2. 번역의 자리에 LLM이 들어왔다: sparkle 버튼(2023, 앱 안의 LLM) → MCP(2024, 사용자의 에이전트가 직접 쿼리·실행).
3. 그런데 **MCP는 채널이지 설계가 아니다** — *"it's up to you, the service, to choose how to communicate with the agent. And it turns out that makes all the difference."*(03:22~03:31)
4. 그래서 사람용 UI가 사라진 자리에 **에이전트용 UI**가 필요하다 — *"a brand new interface specifically designed for agents"*(06:39~06:44).

## 무엇을 설계하나 — 소스가 보인 세 축

| 축 | MCP 기본 상태의 실패 | 에이전트 네이티브 쪽 답(Composio 서술) | 위키 연결 |
|---|---|---|---|
| **도구 노출량** | 도구 정의 수천 개가 창에, *"The model just drowns"*(04:08~04:11) | 에이전트가 **과제를 진술**하면 필요한 도구만 반환(*"state the task it wants to accomplish"* 05:08~05:13) | [[deferred-tool-context]] · [[toolbox-pattern]] |
| **사용 순서·의존성** | *"struggles to resolve dependencies and it can't figure out which one it needs to call first"*(04:11~04:17) | 도구와 함께 **사용 계획**을 반환 — Slack은 채널 ID를 먼저 찾아야 한다(05:20~05:33) | [[agent-tool-design-practices]] |
| **데이터 크기** | 결과를 통째로 창에 | 중간 결과를 **컨텍스트 밖에 저장**하고 참조하는 쿼리만 생성(07:58~08:03, 08:13~08:26) | [[retrieval-side-context-compression]] · [[file-system-agent]] |
| (앱 간 연결) | *"Each MCP server knows about itself and nothing else"*(04:20~04:25) | 여러 앱의 API를 *"cohesive, unified"* 한 층으로(06:52~07:01) | [[knowledge-work-agent-gap]](중앙화) |

그리고 이 층이 무엇 위에 서는지는 부차적이다 — *"we build on top of MCP, CLI, and native tools"*(06:52~06:55). MCP vs CLI 논쟁([[push-vs-pull-context-retrieval]] · [[tech-bridge-sdd-full-course]])을 **전송 계층의 선택**으로 내린다.

## GEO와는 다른 일

*"Many startups have begun making their landing pages and their websites AI friendly for GEO purposes. But so few have really prepared their applications to be used by agents."*(08:51~09:03) — **에이전트가 읽기 좋은 사이트**(GEO, [[agentic-sites]])와 **에이전트가 쓰기 좋은 앱**은 다른 층이다. 앞은 발견·인용, 뒤는 작업 수행.

## 이 위키의 인접 개념과의 관계

- **[[llm-as-search-user]]** — *"검색 기술이 아니라 사용자가 바뀌었다"* 를 검색에서 **SaaS 전반**으로 넓힌 형태. 둘 다 *사용자 교체* 프레임이다.
- **[[agent-tool-design-practices]]** — 도구 하나하나의 품질(결과 중심·조치 가능한 오류). 에이전트 네이티브 인터페이스는 **도구 집합의 노출 방식**(무엇을 언제 보여 주나)까지 포함한다.
- **[[model-rendered-interface]]** — 정반대 방향: 모델이 **사람을 위해** UI를 그린다. 여기서는 사람의 UI가 사라지고 **에이전트를 위해** 인터페이스를 짓는다. 둘 다 *고정 대시보드의 종말* 을 말하지만 최종 소비자가 다르다.
- **[[knowledge-work-agent-gap]]** — 같은 회사(Composio)의 앞선 프레이밍. 코딩 주변은 *"말 그대로 에이전트를 위해 설계"* 돼 있고 지식 노동 앱은 아니라는 진단의 **인터페이스 쪽 처방**.

> ⚠️ **Contradiction: 에이전트 전용 층을 지을 것인가, 사람의 화면으로 갈 것인가.** [[greg-brockman|Brockman]]([[tech-bridge-brockman-agi-era-defender-window]])은 MCP·CLI 층을 *"거의 뻣뻣한 방식"* 의 과도기로 보고 **컴퓨터 사용**(사람용 화면을 에이전트가 직접 조작)을 목적지로 놓는다. Simionescu는 **사람용 화면이 죽었고** 에이전트 전용 층을 더 깊이 지어야 한다고 한다. 둘 다 자기가 파는 쪽(범용 모델 vs 통합 계층)을 목적지로 본다 — 이 위키는 판정하지 않는다. [[model-context-protocol]]의 *"세상을 다시 도구화"* 절 참조.

## ⚠️ 미해결

- **효과의 근거** — *"early unreleased"* 벤치마크, 수치 미발화(06:16~06:32). 같은 과제·같은 모델이라는 조건만 있다.
- **계획을 누가 만드나** — 도구 제공자가 돌려주는 *"plan of how to use them"* 이 사람이 쓴 레시피인지, LLM 생성인지, 사용 로그에서 증류한 것인지. 이것이 화자의 이유 1(*"Agents don't learn"*)에 대한 답이라면 **학습이 에이전트가 아니라 제공자 쪽에 쌓이는** 구조다(위키의 독해).
- **보안·권한** — 앱 여러 개를 *"unified"* 한 층으로 묶으면 그 층이 [[lethal-trifecta]]의 교차점이 된다. 발표는 다루지 않는다(같은 회사의 [[agent-governance-layers]]가 다른 발표에서 다룬다).
- **사람이 다시 봐야 할 때** — 대시보드가 사라지면 에이전트의 답을 검증할 사람의 창은 무엇인가. 화자의 일화(로그아웃된 Datadog 앞에서 얼어붙음)는 바로 그 비용의 예이기도 하다.

## 세 번째 입장 — 목적지가 아니라 폴백 순서 (2026-10-11 · [[tech-bridge-cooking-with-codex]])

위 Brockman(컴퓨터 사용) vs Simionescu(에이전트 전용 층) 대립에, [[openai|OpenAI]]의 [[charlie-guo|Charlie Guo]]는 [[codex|Codex]]의 세 제어 표면을 **용도별로** 나눈다(26:05~28:15): in-app browser는 로컬 웹앱의 깊은 테스트, **computer use**는 *"applications that otherwise don't have a programmatic interface"*(27:09~27:13) — *"it's great if it's a web app and you can reverse engineer the API calls, but (…) there's a lot of legacy software out there which doesn't easily expose that kind of interface to an agent"*(27:13~27:24), **Chrome extension**은 로그인 상태·권한을 넘길 때(27:43~27:48). [[gabriel-chua|Gabriel Chua]]의 데모 동기도 같다 — *"not everything had an API"*(21:31~21:33).

→ 위키의 독해: 프로그래매틱 인터페이스가 있으면 그것, 없으면 사람 화면. **에이전트 네이티브 인터페이스가 있는 곳에선 그것이 우선**이라는 점에서 Simionescu 쪽과 양립하고, 없는 곳의 폴백으로 컴퓨터 사용을 둔다는 점에서 Brockman 쪽과 양립한다. ⚠️ 하네스 제작사의 진술 — 컴퓨터 사용은 자사 기능이다.

## References

- [[tech-bridge-composio-dashboard-is-dead]] — first-seen · [[sarah-simionescu]] · [[composio]]
- [[model-context-protocol]] · [[deferred-tool-context]] · [[toolbox-pattern]] · [[agent-tool-design-practices]] · [[knowledge-work-agent-gap]] · [[llm-as-search-user]] · [[model-rendered-interface]] · [[agentic-sites]]
