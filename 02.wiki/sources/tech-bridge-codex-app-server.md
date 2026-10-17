---
title: "Tech Bridge — OpenAI가 직접 밝힌 Codex 하네스 위에 나만의 에이전트를 구축하는 법 (Dominik Kundel · OpenAI): Codex App Server = 하네스를 감싼 프로토콜"
type: source
tags: [codex, openai, app-server, agent-harness, embedded-harness, json-rpc, agent-client-protocol, developer-instructions, system-prompt, dynamic-tools, deferred-tools, tool-search, bring-your-own-subscription, codex-exec, version-pinning, doom, vendor-claim, video]
source-url: https://www.youtube.com/watch?v=GRMr7YdoJzo
source-type: video
author: Tech Bridge (한영자막 재배포) · 발표 Dominik Kundel([[openai|OpenAI]] Codex developer experience — 자막엔 *"Dom"* 만, 성과 "DevX 팀 리드"는 설명란에만) · 행사명 미발화(*"an AI engineer conference"* + 설명란 ai.engineer 링크 → AI Engineer 계열 추정) · 녹화일 미발화(*"the keynote yesterday"*)
date-published: 2026-10-13
ingested: 2026-10-14
created: 2026-10-14
updated: 2026-10-14
---

# Tech Bridge — OpenAI가 직접 밝힌 Codex 하네스 위에 나만의 에이전트를 구축하는 법 (Dominik Kundel · OpenAI)

[[tech-bridge|Tech Bridge]]가 재배포한 **17:40 발표, Q&A 없음, 공식 챕터 18개.** 화자는 [[openai|OpenAI]]에서 [[codex|Codex]]의 developer experience를 맡은 Dom — 자막엔 *"my name is Dom. I work at OpenAI on developer experience specifically for Codex."*(00:31~00:37)까지만 있고 **성 Kundel과 "DevX 팀 리드" 직함은 설명란에만** 있다. 같은 팀의 [[charlie-guo|Charlie Guo]]·[[gabriel-chua|Gabriel Chua]] 워크숍([[tech-bridge-cooking-with-codex]])이 마지막 3분(§6)에 소개만 했던 **App Server를 17분 전체로 푸는** 소스다. 테제:

> **에이전트 하네스를 밑바닥부터 만들 필요가 없다. Codex app·IDE 확장·서드파티 클라이언트가 이미 쓰는 같은 하네스를 [[codex-app-server|App Server]](JSON-RPC 스타일 프로토콜)로 감싸 열어 두었으니, 그 위에 원하는 인터페이스를 지어라 — 채팅 UI가 아니어도 된다(Doom 안이라도). 다만 셋을 지켜라: 하네스 버전을 직접 번들하고, 새 함수는 deferred로 노출하고, system prompt를 갈아엎지 말고 developer instructions를 덧붙여라.**

> *"the app server is actually the protocol that wraps the codeex[=Codex] harness"* (01:02~01:07) · *"both the codeex harness as well as the app server itself are open source"* (01:26~01:30) · *"you should actually ship your own version of the harness"* (15:54~15:58) · *"make sure that the actual prompt is in distribution"* (17:11~17:16)

이 위키에 페이지 셋이 생긴다 → [[dominik-kundel]] · [[codex-app-server]] · [[embedded-agent-harness]] (모두 신규 제안). [[deferred-tool-context]]에는 **하네스 제작사가 1인칭으로 말하는** deferred loading + tool search가 붙고, [[agent-client-protocol|ACP]]에는 처음으로 **경쟁 프로토콜 쪽의 비교**가 붙는다.

ASR·ko 보정: ko는 **결론 문장 넷을 뒤집는다** — BYO 구독이 *"goes off their codeex usage limit"*(사용자 한도에서 차감) → **"사용량 제한에 영향을 미치지 않습니다"**(06:29, ⭐ `en` 공유), *"not sure if I would recommend it"* → **"분명히 추천할 거라고"**(14:20), deferred 도구가 *"available for the agent"* → **"에이전트가 사용할 수 없음"**(16:50), *"not limited to (…) the classic agent chat interface"* → **"제한이 있습니다"**(11:27). 팁 ③의 *"in distribution"* → **"배포 중"**(17:14), ACP가 *"more generic"* → **"ACP로 가는 것은 더 나은 것"**(06:05). 제품명: App Server → "코덱스 적용 사례"(00:44)·"애플리케이션 서버", Codex → "사본", Doom → "파멸", Electron → "전자", 15 minutes → **"15년"**(17:32). 전체 목록은 raw의 보정 표.

> ⚠️ **당사자 진술 — OpenAI 직원의 자사 프로토콜 소개.** App Server·Codex app·Python SDK·plugins는 전부 자사 것이다. *"over 120 (…) client messages"*(05:17~05:24)는 화자 서술(목록은 화면에만). *"Codex is incredibly good at implementing this protocol"*(10:43~10:46), Visual Basic 클라이언트 *"largely in one shot"*(11:11~11:13)은 1인칭 경험이고 측정·실패 사례가 없다. ACP 비교(06:04~06:13)는 경쟁 프로토콜에 대한 한쪽 서술이다.
>
> ⚠️ **화자 이름.** en-orig는 *"Dom"*(00:33)뿐이다. 성 Kundel(*"도미닉 쿤델(Dominik Kundel)"*)과 직함 "Codex 개발자 경험(DevX) 팀 리드"는 설명란, 링크 `x.com/dkundel` 에서 온다(열어 보지 않았다). 자막과 **충돌하지 않는다**. "리드"는 발화되지 않았다.
>
> ⚠️ **행사·시점.** 행사명은 일반명사뿐 — *"we are at an AI engineer conference"*(10:35~10:37). 단서: *"if you attended the keynote yesterday"*(00:48~00:51) · *"you probably didn't listen to Roman"*(00:54~00:56, 신원 미판독) · *"Before I let you all go to the keynote"*(15:44~15:46) · 내일 오후 다른 세션(01:35~01:40, 07:56~07:59) · OpenAI 부스(17:34~17:36). [[tech-bridge-cooking-with-codex]](같은 팀, World's Fair 2026-06-29 월요일, *"tomorrow we have our opening keynote"*)와 **같은 행사일 가능성**이 있으나 확정하지 않는다 → [[ai-engineer]]. 모델 *"5.5"*(13:26~13:29)는 계열명 미발화.

## 1. 오프닝 — 하네스는 무섭다 (00:00~00:59)

- 손들기 둘: *"How many of you have built your own agent harness?"*(00:04~00:06) · *"How many of you um feel like it's way too intimidating to build an agent harness?"*(00:08~00:12)
- 목표: *"how you can actually build on top of the codeex harness and hopefully make it a bit easier and less daunting for you to, um, actually build your own interfaces on an on an agent harness"*(00:17~00:31)
- 세 번째 손들기(App Server를 들어 봤나)는 *"a bit of a trick question"* — 어제 기조연설에서 언급됐기 때문(00:44~00:56). 그러나 *"we didn't really explain what the app server is"*(00:58~01:00).

## 2. App Server = 하네스를 감싼 프로토콜, 오픈소스 (01:00~02:04)

- ⭐ *"the app server is actually the protocol that wraps the codeex harness. Um, if you've ever looked into something like agent client protocol, this is a very similar concept where basically we have a protocol that allows you to directly build on top of the uh harness and deeply integrate into it."*(01:00~01:17)
- ⭐ *"both the codeex harness as well as the app server itself are open source"*(01:26~01:30) · *"you can also always just ask codeex to read the repo and dive really deep into it. It's Apache 2 licensed, so feel free to fork it"*(01:40~01:49)
- 모델 공급자: *"You can even connect it to any other model provider as long as they have a responses API cap[=Responses API–]compatible API. Uh we even have uh convenience settings to connect it easily to LM studio or lama[=Ollama]."*(01:52~02:03)

→ [[codex-app-server]] (신규) · [[agent-client-protocol]]

## 3. 누가 이미 쓰나 — 1st party와 3rd party (02:05~02:56)

- *"a JSON RPC style protocol that we actually use to power the codeex app, the IDE extension, our VS code extension. So all of our firstparty interfaces, but also thirdparty ones."*(02:07~02:20)
- 서드파티: *"codeex through Xcode, Jet Brains idees um or even some open source projects like Theos T3 code or remoteex"*(02:22~02:27) → *"all of these are powered by the same harness, the same app server"*(02:30~02:33). ⚠️ *"Theos T3 code"* = Theo's T3 Code(판독), *"remoteex"* 미판독.
- ⭐ 경쟁사 하네스 안으로: *"We even used it earlier this year to put codeex into cloud code[=Claude Code] um using that same app server. So if you're still on cloud code uh and you want to use codeex from there either to have it review your code or um you know pass off task to codeex to handle it you can actually use that plugin"*(02:35~02:52) — ⚠️ *cloud code* → Claude Code는 문맥 판독(*"if you're still on"*). → [[claude-code]]

## 4. 구조와 이벤트 — 인스펙터 데모 (02:57~05:15)

- *"we're going to send messages between the client, which is the application you're building, and the server, which the Codex app server, uh to perform different actions and receive events."*(03:05~03:14)
- 데모: *"I went a bit overboard and actually built a little inspector that intercepts all of the events between the real Codex app and the uh Codex app server"*(03:20~03:28) — Codex app의 in-app browser에 띄웠다(03:39~03:42). 보이는 이벤트: thread 시작(설정·프로젝트), configuration read, *"delta messages of like data actually being streamed in"*(04:22~04:44). ⚠️ 이벤트 이름은 화면에만.
- ⭐ 유연성의 이유: *"we're really exposing anything that is really in the app um key functionality. Meaning if we're streaming and things, we're doing file search, all of that information is actually handed back and forth between the app server and the and the app. And so if you're building (…) your own client, you can actually leverage uh the same capabilities."*(04:53~05:14)

## 5. 120개 이상의 클라이언트 메시지, 그리고 ACP와의 차이 (05:17~06:15)

- *"we have right now over 120 um so different client uh client messages that we continuously add more to"*(05:17~05:27) — 초기화(클라이언트별 설정), thread 수정, turns(*"the most classic things"*), *"setting a goal if you want to implement your own version of goal mode"*, 플러그인 목록, 파일 검색·파일 시스템 수정까지(05:28~05:58). ⚠️ 120은 화자 서술.
- ⭐ ACP와의 차이: *"we also try to make it easy so that you can uh configure the underlying agent and that's a bit different to ACP where it's a more more uh generic protocol we can actually give you more control over the individual parts of the harness"*(05:58~06:13).

| | [[agent-client-protocol\|ACP]] (Zed·JetBrains 제안, [[goose\|Goose]] 채택) | **Codex App Server** (이 소스) |
|---|---|---|
| 범위 | 여러 하네스 ↔ 여러 클라이언트 — *"more generic"* | **한 하네스**(Codex)의 거의 모든 기능 |
| 제어 깊이 | capability 집합 + `_` 커스텀 메서드 | *"more control over the individual parts of the harness"* — developer instructions·도구·스레드별 모델·샌드박스 |
| 전송 | JSON-RPC, stdio + HTTP/WebSocket | JSON-RPC 스타일, stdio · WebSocket(09:57~10:04) |
| 통합 예 | JetBrains AI 채팅에 OpenCode | Codex app·VS Code·Xcode·JetBrains·T3 Code·Claude Code 플러그인 |

→ 위키의 정리: 둘은 **같은 방향(클라이언트 → 하네스)** 의 프로토콜이고 갈리는 것은 **일반성 vs 깊이**다. ACP의 *"모든 웹사이트에 브라우저 하나"* 비유로 보면 App Server는 **한 하네스 전용의 풍부한 API** 쪽이다. ⚠️ 화자는 Codex가 ACP를 지원하는지 말하지 않는다.

## 6. Sign in with ChatGPT — 구독을 들고 오기 (06:15~06:36)

- ⭐ *"if you're using this protocol you can have signin with chat GPT as part of that meaning that if someone is using your app they can still bring their own chat GPT subscription and it goes off their codeex uh use usage limit. So if you've used something like T3 code or similar, you're actually using that."*(06:18~06:36)
- ⚠️ **`en`·ko 공유 반전** — *"this won't affect your Codex usage limits"* / "사용량 제한에 영향을 미치지 않습니다". 원문은 **사용자 자신의 Codex 사용 한도에서 차감**된다는 뜻이다. 비용이 앱 개발자가 아니라 사용자 구독에 귀속된다는 BYO의 요점이 자막 번역에선 정반대로 읽힌다.

→ [[bring-your-own-subscription]] — Charlie Guo(6월)의 *"use their Chat GBT token budget"* 에 **두 번째 OpenAI 1인칭**과 **실제 사용 사례(T3 Code)** 가 붙는다.

## 7. 에이전트 맞춤 — developer instructions와 dynamic·deferred tools (06:38~08:28)

- 둘: *"developer instructions as a way for you to augment the instruction, the system instructions of the actual app as well as uh bringing tools"*(06:44~06:55)
- ⭐ **덧붙이기, 교체 아님**: *"with developer instructions, we're actually appending on top of the system prompt of codeex. You can look at the actual system prompt of Codex as well. It's in the repo. Um, but we generally recommend that you actually append to that using the developer instructions. That way, you're still leveraging all of the work that we put into tweaking the prompts for the individual models while still customizing it for your specific use case"*(06:55~07:18). Codex app도 그렇게 한다 — 앱 전용 기능을 IDE 확장·CLI와 구분(07:20~07:29).
- ⭐ **dynamic tools + deferred loading**: *"You could use MCP or other things similar to what you would do in like the agent client protocol, but you can also just straight up define tools and you can actually mark them as deferred loading, which means that rather than injecting them into the system prompt, it uh allows Codex to use a tool search tool (…) but allows it to find these tools through tool search rather than polluting the uh overall context window."*(07:39~08:07) — tool search는 *"we'll cover more tomorrow in the other session"*(07:56~07:58), 이 소스엔 세부가 없다.
- 스레드별 설정: *"on a per thread basis modify any other configuration (…) setting a different model provider choosing a different model or even doing fine grain control on the sandbox like what network connections uh it should have access to or what files it can modify."*(08:07~08:27)

→ [[deferred-tool-context]] · [[embedded-agent-harness]] (신규) · [[model-context-protocol]]

## 8. 배포 — 같은 바이너리, 앱마다 번들 (08:29~09:22)

- *"the app server actually comes as part of the codec[=Codex] CLI. It's the same binary. So if you have the codeex CLI already on your system, you can just uh use that to spin up the app server right now."*(08:34~08:45)
- Codex app: *"the CEX[=Codex] app has the uh binary as part of the actual bundle (…) And it changes with every version of the app that you're updating. We're shipping a new version of the CLI behind the scenes."*(08:50~09:06)
- Windows: *"we actually ship with two versions of the binary, both the Linux compiled one and the Windows one, so that if you're loading the app in WSL mode, it uses uh the Linux one and otherwise it starts up the app server in Windows native."*(09:06~09:19)
- ⚠️ 설명란의 *"Rust 바이너리 임베딩"* — **"Rust"는 발화되지 않는다.**

## 9. 바인딩·전송·SDK, 또는 "Codex에게 시켜라" (09:23~11:22)

- ⭐ 바인딩: *"you can have codeex generate you for that particular version of the app server the TypeScript bindings or the um JSON schema which is incredibly helpful since this uh protocol regularly changes between versions which is also why you actually want to bundle it with your application"*(09:28~09:46)
- 전송: stdio 또는 WebSocket — *"the easiest way to figure out what works better for you is probably to just ask codeex"*(09:57~10:10)
- 통합 두 길: ① *"the Python SDK that we recently re uh released. It handles a lot of the life cycle management for you"*(10:18~10:25) + sign in with ChatGPT 편의 ② *"you just ask Codex. So unsurprisingly, Codex is incredibly good at implementing this protocol. And you largely just have to point it at um the documentation."*(10:39~10:51)
- 1인칭 사례: *"I used it, for example, to build a client using, um, Visual Basic, uh, to have a like truly Windows native app. Um, and it did it largely in one shot."*(11:04~11:13) → *"without you having to learn all the nitty-gritty parts of bu building an agent"*(11:17~11:21). ⚠️ 측정 없음.

## 10. 채팅 UI가 아니어도 된다 — Doom 안의 Codex (11:24~14:28)

- ⭐ *"you're not limited to sort of the classic agent chat interface. You can really be creative."*(11:28~11:34) — UI 안 트리거, 백그라운드 실행, *"weird hardware like Maddie does all the time"*(11:44~11:46, Maddie 미판독), 비디오 게임.
- *"how can I actually run codecs inside of Doom rather than running Doom inside of Codeex"*(11:55~12:01)
- 구성: *"an Electron app that has uh uses Cloudflare's Doom Wasm renderer"*(12:41~12:47), 엔진은 C, *"it loads the freedom[=Freedoom] game except that I actually manipulate had codeex change the game file"*(12:56~13:00) → UI가 게임 엔진 안에서 네이티브로 렌더링 → *"passes it to the app server using Electron's um IPC protocol"*(13:14~13:22). 모델 *"5.5"*(13:26~13:29).
- dynamic tools: 갑옷·체력, *"all the weapons with all ammo"* — 게임 조작 함수를 도구로 노출(13:29~13:57).
- ⭐ 여전히 진짜 하네스: *"remember this is still an app server actually running on my machine"*(13:57~14:02) — *"what's the directory"* → zsh로 작업 디렉터리 조회(14:06~14:13). *"you can vibe code directly into code in inside doom uh not sure if I would recommend it uh I think the app the codeex app is slightly better for this"*(14:15~14:24)
- ⚠️ 데모 중 듀얼 모니터로 컨트롤 캡처가 꼬였다(12:24~12:38). 결과의 정확성은 화면 의존.

→ [[cloudflare]](Doom Wasm 렌더러 — 지나가는 언급)

## 11. App Server vs codex exec (14:30~15:42)

- *"one question that came up a lot of times is what's the difference with Codex exec"*(14:38~14:42)

| | **codex exec** | **App Server** |
|---|---|---|
| 형태 | *"a non-interactive interface for you to uh pass to kick off tasks"*(14:48~14:55) | 클라이언트 ↔ 하네스 양방향 프로토콜 |
| 맞는 일 | *"great for scripting"* — CI/CD, *"autofixing a PR"*(14:55~15:04) | *"a more comprehensive client (…) where you're showing the agent"*(15:05~15:13) |
| 병렬 | exec 호출을 직접 병렬화해야 함 | *"spinning up a bunch of different uh codeex threads at the same time"* — *"your own like eval harness"*, `/goal`(⚠️ ASR *"slashgo"*)(15:13~15:28) — *"just sending off a bunch of like new thread events"*(15:36~15:42) |

- ⭐ *"that's where the app server really shines because you have that full control over the harness"*(15:26~15:32)

## 12. 세 가지 팁 (15:44~17:25)

| # | 팁 | 이유 (en-orig) |
|---|---|---|
| ① | ⭐ *"you should actually ship your own version of the harness"*(15:54~15:58) | *"If you're relying on the user's installed CLI, you're going to constantly run into things from uh like breaking changes even though we are trying to minimize them. But if you're relying on experimental features, that might happen."*(15:58~16:12) + 사용자가 업데이트했는지 신경 쓸 필요가 없다(16:12~16:22) |
| ② | ⭐ *"you should absolutely expose new um functions as part of your interface (…) But mark them as deferred."*(16:24~16:42) | Codex app도 자기 자신을 제어하는 함수(자동화 띄우기 등)를 노출한다(16:30~16:40). *"That way you're not polluting the context window unnecessarily (…) and instead still have them available for the agent without um necessarily confusing it."*(16:42~16:53) |
| ③ | ⭐ *"try to start with over uh like adding developer instructions rather than changing the base instructions"*(16:56~17:01) | *"there's a lot of different things that we constantly have to think about when we're building a harness to make sure that the actual prompt is in distribution and make sure that the agent performs well. And you're losing out on all of that if you're actually jumping in and like writing your own system prompt."*(17:06~17:21) |

→ [[embedded-agent-harness]] (신규) — 셋 다 **하네스 제작사의 투자를 깎아 먹지 않는 법**이라는 한 원칙으로 묶인다(위키의 독해).

## 이 위키와의 연결

### 이어지는 것

- **[[tech-bridge-cooking-with-codex]] — 같은 팀의 예고편을 본편으로.** Charlie·Gabriel의 §6(58:18~1:01:50)은 App Server를 *"the core protocol that underpins the Codex app, the Codex CLI, uh, the Codex VS code extension"*, BYO 토큰 예산, 오픈소스, Retrodex 데모까지만 말했다. 이 소스는 그 위에 **ACP와의 차이 · 120개 메시지 · developer instructions · deferred tools · 번들·바인딩 · exec 비교 · 팁 셋**을 더한다. 충돌은 없다. 다만 Charlie는 App Server가 **Codex CLI를 받친다**고 했고, Dom은 App Server가 **CLI와 같은 바이너리에 들어 있다**(08:34~08:38)고 한다 — 같은 사실의 두 서술로 읽힌다.
- **[[harness-as-platform]] — 조직 안 플랫폼 팀에서 벤더로.** Uber(Kriti Dangi)는 *"we are the providers of the harness"* 를 **사내 플랫폼 팀**의 역할로 말했다. 여기선 **하네스 제작사(OpenAI)가 외부 개발자에게** 같은 말을 한다. ⚠️ **10-12 Vercel CEO 편 제안과 겹친다** — [[tech-bridge-vercel-rauch-agentic-workflow]]의 Guillermo Rauch는 [[v0]]에서 *"like 90% of the engineering time"* 이 하네스에 들었고 지금이라면 *"pick a harness off the shelf"* 하겠다고 했다(그 편의 PROPOSAL B8이 harness-as-platform에 "하네스를 사서 앱에 박는다" 절을 제안). 이 소스는 **그 "선반 위 하네스"를 파는 쪽의 사용 설명서**다. → [[embedded-agent-harness]]로 두 소스를 묶자고 제안한다.
- **[[deferred-tool-context]] — 네 번째 답, 하네스에 내장된 deferred loading.** Factory(deferred context engine), Oracle([[toolbox-pattern]]), Uber(에이전트 타입), Composio(과제 → 도구 + 계획)에 이어, **Codex 하네스가 도구 정의를 `deferred` 로 표시하면 system prompt에 넣지 않고 tool search로 찾게 한다**(07:47~08:07). 차이: 앞의 넷은 하네스 *사용자*·도구 *공급자*가 만든 장치였고, 이것은 **하네스 자체의 플래그**다. ⚠️ tool search의 동작(검색 방식, 찾지 못할 때)은 *"tomorrow in the other session"* 으로 미뤄져 이 소스에 없다.
- **[[agent-client-protocol]] — 처음으로 다른 프로토콜 쪽에서 본 ACP.** 지금까지 ACP 페이지의 소스는 ACP를 *채택한 쪽*(Goose, JetBrains)뿐이었다. App Server는 *"a very similar concept"*(01:10~01:12)이면서 *"more control over the individual parts of the harness"* 를 차이로 든다. → ACP의 ⚠️ *"보안 모델이 없다"* 빈자리는 App Server 쪽에서도 채워지지 않는다(인증은 *sign in with ChatGPT* 만 발화).
- **[[bring-your-own-subscription]] — 메커니즘의 두 번째 OpenAI 1인칭 + 실제 사례.** T3 Code가 이미 그렇게 쓴다(06:33~06:36). 차감 대상은 *"their codeex (…) usage limit"* — Charlie의 *"Chat GBT token budget"* 과 같은 방향.
- **[[harness-engineering]] · [[agent-harness-design]]** — 손들기 *"way too intimidating to build an agent harness"*(00:08~00:12)는 이 위키가 쌓아 온 하네스 설계의 무게를 **사지 말고 빌려 쓰라**는 쪽으로 돌린다.
- **[[tools-and-context-over-harness]]** — *하네스는 고정, 노력은 도구·컨텍스트에*. 이 소스의 팁 ②·③은 같은 결론을 **하네스 제작사가 직접** 준다: 도구는 더하되(deferred로), 프롬프트는 덧붙이기만 하라.
- **[[claude-code]]** — OpenAI가 App Server로 **Codex를 Claude Code 안에 넣는 플러그인**을 *"earlier this year"* 냈다(02:35~02:55). 이 위키에서 한 회사의 코딩 에이전트가 **경쟁사 하네스 안의 플러그인**으로 들어간 첫 1인칭 서술이다(⚠️ *cloud code* 판독).

### 갈리는 것

> ⚠️ **긴장: system prompt는 건드리지 말라 vs 하네스를 직접 짜라.** Dom의 팁 ③ — base instructions 교체는 *"in distribution"* 을 잃는다(17:06~17:21). [[self-harness]]·[[harness-engineering]] 계열 소스는 하네스(프롬프트 포함)를 **과제에 맞게 고쳐 쓰는 것**을 성과의 원천으로 본다. 둘은 사실 충돌이 아니라 **누가 그 모델을 학습시켰나**의 차이다 — 모델 제작사의 하네스는 *그 모델이 학습된 분포*에 맞춰져 있다는 주장이고, 그 근거(어떤 프롬프트가 분포 밖인지, 얼마나 나빠지는지)는 이 소스에 없다. ⚠️ 당사자 진술.

> ⚠️ **긴장: 하네스 버전을 직접 번들하라 vs 사용자 CLI.** 팁 ①은 *breaking changes* 를 이유로 든다(15:58~16:12). 그 말은 **프로토콜이 아직 안정 계약이 아니다**(*"this uh protocol regularly changes between versions"* 09:38~09:42)는 자인이기도 하다. 번들한 하네스의 **보안 패치·모델 업데이트를 누가 언제 따라가는지**는 이 소스가 말하지 않는다.

> ⚠️ **ko·`en` 반전이 이 소스의 BYO 서술을 뒤집는다.** 06:29 *"goes off their codeex usage limit"* → "영향을 미치지 않습니다". 이 위키의 다른 BYO 서술과 충돌하는 것처럼 보이는 자막 번역 문장은 **en-orig로 확인하면 충돌이 아니다.**

## 해소하지 않고 표시만 한 것

- 120개 클라이언트 메시지의 목록·이름(화면에만), 인스펙터의 이벤트 이름.
- tool search의 동작 — *"tomorrow in the other session"* 으로 미뤄짐.
- App Server가 ACP를 지원하는지, 둘의 관계(경쟁 vs 병존).
- 인증·권한 모델(*sign in with ChatGPT* 외), 원격(WebSocket) 노출 시 보안.
- 번들한 하네스의 업데이트 책임, 프로토콜 안정화 계획.
- *"remoteex"*(02:26), *"codeex pad"*(04:18), *"Roman"*(00:56), *"Maddie"*(11:45)의 정체.
- 행사명·도시·녹화일, Cooking with Codex와 같은 회차인지.
- *"5.5"* 의 계열명. Python SDK의 출시 시점(*"recently"* 10:20).

## 등장 개체

- 인물: [[dominik-kundel|Dominik Kundel]](신규 제안 — 자막엔 *"Dom"* 만) · "Roman"(기조연설 화자, 신원 미판독 — 페이지 없음) · Maddie(미판독 — 페이지 없음) · Theo(T3 Code, ⚠️ 판독 — 페이지 없음)
- 조직: [[openai|OpenAI]] · [[jetbrains|JetBrains]](IDE 통합) · [[cloudflare|Cloudflare]](Doom Wasm 렌더러) · [[ai-engineer|AI Engineer]](⚠️ 일반명사 발화 + 설명란 링크 — 추정)
- 제품·도구: [[codex|Codex]](app · CLI · VS Code 확장 · plugins · `/goal` · codex exec) · [[codex-app-server|Codex App Server]](신규 제안) · Codex Python SDK · [[claude-code|Claude Code]](Codex 플러그인의 호스트) · Xcode · T3 Code · LM Studio · Ollama · Electron · Doom/Freedoom · Visual Basic(페이지 없음)
- 모델: *"5.5"*(⚠️ 계열명 미발화)
- 개념: [[embedded-agent-harness]](신규 제안) · [[agent-client-protocol]] · [[deferred-tool-context]] · [[bring-your-own-subscription]] · [[harness-as-platform]] · [[tools-and-context-over-harness]] · [[harness-engineering]] · [[agent-harness-design]] · [[model-context-protocol]] · [[self-harness]] · [[verifiable-goals]](`/goal`)

## References

- 원본 영상: <https://www.youtube.com/watch?v=GRMr7YdoJzo> (17:40, `upload_date` 2026-10-13)
- raw: `01.raw/articles/2026-10-13_OpenAI가 직접 밝힌 Codex 하네스 위에 나만의 에이전트를 구축하는 법.md`
- 설명란 링크: <https://developers.openai.com/codex/app-server> · <https://github.com/openai/codex> · <https://developers.openai.com/codex/sdk> · <https://x.com/dkundel> · <https://ai.engineer> (⚠️ 열어 보지 않았다)
- 같은 팀·같은 제품: [[tech-bridge-cooking-with-codex]]
- 기성 하네스 임베드: [[tech-bridge-vercel-rauch-agentic-workflow]] · [[tech-bridge-uber-debug-assist]]
- 클라이언트 ↔ 하네스 프로토콜: [[tech-bridge-acp-universal-remote]] · [[tech-bridge-sdd-full-course]]
- deferred 도구: [[tech-bridge-factory-software-factory]] · [[tech-bridge-composio-dashboard-is-dead]]
- BYO 구독: [[tech-bridge-altman-devday-dots]] · [[tech-bridge-stigg-ai-companies-building-banks]]
- [[tech-bridge]] · [[openai]] · [[codex]]
