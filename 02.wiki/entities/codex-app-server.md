---
title: "Codex App Server"
type: entity
category: product
tags: [codex, openai, protocol, json-rpc, agent-harness, open-source, client-server, embedded-harness]
aliases: [App Server, app server, Codex app-server, codex app server]
links:
  - "https://developers.openai.com/codex/app-server"
  - "https://github.com/openai/codex"
sources: [tech-bridge-codex-app-server, tech-bridge-cooking-with-codex, tech-bridge-ben-davis-codex-product-cohesion]
created: 2026-10-16
updated: 2026-10-31
---

# Codex App Server

**[[codex|Codex]] 하네스를 감싸는 JSON-RPC 스타일 프로토콜.** 클라이언트(내가 만드는 앱)와 서버(App Server)가 메시지를 주고받아 동작을 시키고 이벤트를 받는다. Codex app·VS Code 확장 같은 [[openai|OpenAI]] 1st party 인터페이스와 Xcode·JetBrains·T3 Code·Claude Code용 Codex 플러그인 같은 3rd party 인터페이스가 **같은 하네스, 같은 App Server** 위에서 돈다. 하네스와 App Server 모두 오픈소스다(Apache 2). 1차 소스: [[tech-bridge-codex-app-server]]([[dominik-kundel|Dominik Kundel]]). 처음 언급: [[tech-bridge-cooking-with-codex]] §6.

> *"the app server is actually the protocol that wraps the codeex[=Codex] harness"* (01:02~01:07) · *"we use to power the codeex app, the IDE extension, our VS code extension. So all of our firstparty interfaces, but also thirdparty ones"* (02:10~02:20)

> ⚠️ **전부 당사자 진술**(OpenAI developer experience 직원 두 소스). 독립 사용자의 평가는 아직 이 위키에 없다.

## 구성 (화자 서술)

| 항목 | 내용 |
|---|---|
| 형식 | JSON-RPC 스타일. 클라이언트 메시지 *"over 120"*(05:17~05:24): 초기화, thread·turn, goal, 플러그인 목록, 파일 검색·파일 시스템 수정 |
| 이벤트 | thread 시작·config read·delta 스트리밍 등 — *"we're really exposing anything that is really in the app um key functionality"*(04:53~04:57) |
| 맞춤 | **developer instructions**(Codex system prompt 위에 덧붙임) · **dynamic tools**(직접 정의, `deferred` 표시 → tool search) · 스레드별 모델 공급자·모델·샌드박스(네트워크·파일) |
| 인증 | **Sign in with ChatGPT** — 사용자의 ChatGPT 구독과 Codex 사용 한도로 과금(06:18~06:31) → [[bring-your-own-subscription]] |
| 모델 | Responses API 호환 공급자 누구든, LM Studio·Ollama 편의 설정(01:52~02:03) |
| 배포 | Codex CLI와 **같은 바이너리**(08:34~08:38). Codex app 번들에 포함되고 앱 버전마다 바뀐다. Windows는 Linux·Windows 바이너리 둘(WSL) |
| 바인딩 | 버전별 TypeScript 바인딩 / JSON schema 생성 — *"this uh protocol regularly changes between versions"*(09:38~09:42) |
| 전송 | stdio · WebSocket |
| SDK | Python SDK(*"recently"* 출시, 수명 주기 관리 + sign in with ChatGPT) — 또는 *"you just ask Codex"*(10:39~10:41) |

## 알려진 사용처

- 1st party: Codex app, IDE 확장(VS Code)
- 3rd party(발화): Xcode, JetBrains IDE, T3 Code(⚠️ ASR *"Theos T3 code"*), *"remoteex"*(미판독)
- **Claude Code 안의 Codex 플러그인**(*"earlier this year"*, 코드 리뷰·작업 위임, 02:35~02:55, ⚠️ ASR *"cloud code"*) → [[claude-code]]
- 데모: Retrodex(Gabriel Chua, [[tech-bridge-cooking-with-codex]]), 이벤트 인스펙터·Visual Basic 클라이언트·**Doom 안의 Codex**(Kundel)

## codex exec와의 구분

**codex exec**는 비대화형이고 스크립팅용이다(CI/CD, PR 자동 수정). App Server는 에이전트를 보여 주는 클라이언트를 만들거나, 여러 thread를 병렬로 돌릴 때(자체 eval 하네스, `/goal`) 쓴다 — *"you have that full control over the harness"*(15:26~15:32).

## ACP와의 관계

화자는 *"a very similar concept"*(01:10)라 하면서 차이를 **일반성 vs 깊이**로 든다(06:04~06:13). App Server가 ACP를 지원하거나 대체하는지는 발화되지 않았다 → [[agent-client-protocol]]

## ⚠️ 미해결

- 120개 메시지 목록(화면에만), 인증·권한 모델(sign in with ChatGPT 외), WebSocket 원격 노출 시의 보안.
- 프로토콜 안정화 계획 — 화자는 *breaking changes* 를 전제로 **하네스 버전 번들**을 권한다.
- tool search의 동작(*"tomorrow in the other session"* 으로 미뤄짐).

## References

- [[tech-bridge-codex-app-server]] — 1차 소스
- [[tech-bridge-cooking-with-codex]] — first mention (§6, Retrodex)
- [[codex]] · [[openai]] · [[dominik-kundel]] · [[embedded-agent-harness]] · [[agent-client-protocol]] · [[deferred-tool-context]] · [[bring-your-own-subscription]]

## 프로토콜은 같아도 제품 단위는 다르다 — 사용자 비판 (2026-10-31 · [[tech-bridge-ben-davis-codex-product-cohesion]])

[[ben-davis|Ben Davis]](추정)는 *"A Coda[=Codex] thread should become the base building block for everything. That should be the building block for the CLI, for the desktop app, for the web app, everything."*(05:20~05:30)이라고 요구한다. 이 페이지가 정리한 당사자 설명(App Server = Codex app · CLI · VS Code 확장의 공통 프로토콜)과 **층이 다르다** — 하네스 · 프로토콜 층은 이미 공통이라는 것이 OpenAI의 말이고, 화자는 **사용자가 보고 다루는 thread 단위**가 표면마다 어긋난다고 말한다(Spaces 안의 thread와 일반 thread). 모순은 아니다. ⚠️ 화자는 App Server를 언급하지 않는다. → [[primitives-before-features]]
