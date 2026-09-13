---
title: ACP (Agent Client Protocol)
type: concept
category: architecture
tags: [protocol, harness, client, interoperability, json-rpc, standards]
aliases: [Agent Client Protocol, 에이전트 클라이언트 프로토콜]
related: [model-context-protocol, agentic-stack-decomposition, standards-as-market-makers, agent-harness-design, cloud-agent-delegation, goose, zed]
first-seen: tech-bridge-acp-universal-remote
sources: [tech-bridge-acp-universal-remote]
created: 2026-09-13
updated: 2026-09-13
---

# ACP (Agent Client Protocol)

**클라이언트 소프트웨어가 에이전트 하네스를 제어하기 위한 개방형 표준.** [[model-context-protocol|MCP]]가 *에이전트 → 도구* 방향을 표준화했다면 ACP는 **그 반대 방향 — 클라이언트 → 에이전트** 를 맡는다. [[tech-bridge-acp-universal-remote]]에서 [[alex-hancock]]([[block|Block]] · [[goose|Goose]])이 소개했다.

## 왜 필요한가

문제는 하네스가 부족해서가 아니라 **접근 경로가 하나씩이라서**다.

> 좋은 하네스가 정말 많습니다 — 랩에서 나온 것, 여러 회사에서 나온 것… 그런데 **그것들에 접근하는 인터페이스가 대개 맞춤형이거나 주문 제작**입니다. 최악의 경우, 어떤 하네스는 **그것을 제어할 수 있는 클라이언트 애플리케이션이 문자 그대로 하나뿐**일 수도 있죠.

> **모든 웹사이트에 접속하는 데 단 하나의 브라우저, 단 하나의 프로토콜만 써야 한다면** 어떻겠습니까. **브라우저의 현실이 그랬다면 개방형 웹 같은 건 없었을 겁니다.**

## 출처와 동기

**[[zed|Zed]]와 JetBrains가 공동 제안**했다. 에디터 제작자의 동기는 단순하다 — **고품질 클라이언트 구현을 하나만 작성해 모든 하네스를 제어**하는 것. [[goose|Goose]] 팀의 판단은 **그 쓸모가 에디터에 갇히지 않는다**는 것이었다(프로토콜이 *"비교적 중립적이고 에디터 전용 기능이 별로 없다"*).

## 구성

| 요소 | 내용 |
|---|---|
| 전송 | **JSON-RPC**. stdio + **HTTP / WebSocket 업그레이드**(원격, *"지금 막 도입 중"*) |
| 연결 | **capability 집합**이 딸린 클라이언트↔하네스 연결 |
| 세션 | 사용자 메시지 송신, 에이전트의 **텍스트·이미지·오디오** 응답, 진행 상황 업데이트 |
| 알림 | **도구 호출 알림** — 어떤 도구가 호출됐고 메타데이터가 무엇인지 |
| 권한 | **권한 요청** — 클라이언트가 *"이 도구 호출을 할까요?"* 를 사용자에게 보여줄 수 있게 |
| 확장 | **`_` 접두 커스텀 메서드** |

## 표준화의 순서를 뒤집는다

이 프로토콜의 가장 이전 가능한 설계 결정은 확장 규칙이다.

> **충분히 많은 하네스 프로젝트나 클라이언트 프로젝트가 이걸 채택하면, 우리가 다 같이 똑같이 하고 있는 게 뭔지 보이기 시작**합니다. (…) **생태계에서 무엇이 떠오르는지, 무엇을 표준화 궤도에 올려 프로토콜 자체에 들여올 만한지** 볼 수 있습니다.

즉 **먼저 표준을 정하고 구현하게 하는 것이 아니라, 각자 확장하게 두고 겹치는 것을 표준으로 승격**시킨다. → [[standards-as-market-makers]]

## 파급

원격 전송이 붙으면서 **[[agentic-stack-decomposition|에이전트 스택의 네 구성 요소]]가 각각 독립적으로 배치 가능**해진다. 이것이 이 소스가 주장하는 실질적 효과다.

그리고 시장 효과 — **클라이언트가 하나의 카테고리가 되면 UX 품질 경쟁이 붙는다**(*"클라이언트가 자기 요구를 못 맞출 때 사용자는 발로 투표한다"*).

## 위키가 표시해 둔 빈자리

> ⚠️ **보안 모델이 없다.** 원격 전송을 명세했다면서 **인증·인가·신원**을 한 마디도 다루지 않는다. [[tech-bridge-build-time-vs-runtime-tools]]가 제기한 **세 신원** 문제와 [[confused-deputy-attack]]·[[lethal-trifecta]]가 정확히 이 조합(원격 + 도구 + 권한 요청)을 가리킨다.
>
> ⚠️ **`_` 커스텀 메서드의 충돌 처리와 표준화 거버넌스**도 없다. *사용이 표준을 형성한다* 는 것은 **누가 무엇을 승격시킬지 결정하는가**에 답하지 않는다.
>
> ⚠️ **당사자 진술.** 경쟁 표준·대안 검토 없음, 채택 수치 없음.

## References

- [[tech-bridge-acp-universal-remote]] · [[model-context-protocol]] · [[agentic-stack-decomposition]] · [[standards-as-market-makers]] · [[agent-harness-design]] · [[goose]] · [[zed]] · [[alex-hancock]] · [[lethal-trifecta]]
