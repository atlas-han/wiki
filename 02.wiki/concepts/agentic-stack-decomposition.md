---
title: 에이전트 스택 분해 (Agentic Stack Decomposition)
type: concept
category: architecture
tags: [architecture, harness, mcp, acp, deployment, remote]
aliases: [네 구성 요소, agentic stack, 클라이언트-하네스-도구-모델]
related: [agent-client-protocol, model-context-protocol, agent-harness-design, cloud-agent-delegation, harness-engineering, self-harness]
first-seen: tech-bridge-acp-universal-remote
sources: [tech-bridge-acp-universal-remote]
created: 2026-09-13
updated: 2026-09-13
---

# 에이전트 스택 분해

**에이전트 시스템은 네 개의 구성 요소로 나뉘고, 각각에 원격 전송이 있으면 넷을 서로 독립적으로 배치할 수 있다**는 관점. [[goose|Goose]] 팀의 정리이고 [[tech-bridge-acp-universal-remote]]에서 제시됐다.

| 구성 요소 | 정의 | 표준 |
|---|---|---|
| **클라이언트** | 사용자가 쓰는 앱, 또는 어느 기계에서 도는 헤드리스 앱 | [[agent-client-protocol\|ACP]] |
| **하네스** | **도구 호출 루프를 구현하는 프로그램** | [[agent-client-protocol\|ACP]]의 서버 쪽 |
| **도구** | 흔히 [[model-context-protocol\|MCP]] | MCP (원격 전송 있음) |
| **모델** | — | responses API 등 원격 엔드포인트 |

## 논지

> **ACP에 원격 전송이 생기고**, MCP에는 도구 호출용 원격 전송이 있고, 모델은 오래전부터 원격 엔드포인트를 가지고 있었습니다. 이제 **이 네 구성 요소를 전부 자유롭게 옮길 수 있습니다.** 전부 같은 기계에 있을 수도 있고, **하네스가 클라이언트와 다른 기계**에 있을 수도 있고, **모델만 원격**일 수도, **도구만 원격**일 수도 있습니다.

> **표준에 정렬하고 그 표준이 좋은 전송 스토리를 갖게 하는 것**이 이 에이전트 스택의 조각들을 옮길 수 있게 해 줍니다.

## 왜 중요한가

이 위키가 다뤄 온 개념들이 이 분해에서 **각자 어느 칸의 이야기인지** 정리된다:

- **[[agent-harness-design]] · [[harness-engineering]] · [[self-harness]]** — 하네스 칸. 이 소스는 하네스를 *"도구 호출 루프를 구현하는 프로그램"* 이라는 **한 줄 정의**로 못 박고, 동시에 **교체·이전 가능한 배포 단위**로 승격시킨다.
- **[[cloud-agent-delegation]]** — *"에이전트는 클라우드에서 돌게 될 테니 원격이 돼야 한다"* 는 클라우드 에이전트를 **제품 기능이 아니라 전송 계층의 귀결**로 다시 놓는다.
- **[[build-time-vs-runtime-tools]]** — 도구 칸의 구분. 그 소스가 *어떤 도구를 언제 묶는가* 를 다뤘다면 이쪽은 *도구가 어디서 도는가* 다.
- **[[model-mixing-economics]]** — 모델 칸만 따로 원격일 수 있다는 것은 **모델 교체 비용을 낮춘다.**

## 표시해 둔 것

> ⚠️ **분해는 보안 경계도 함께 늘린다.** 네 칸이 서로 다른 기계에 있을 수 있다는 말은 **세 개의 네트워크 경계**가 생긴다는 뜻인데, 원 소스는 **인증·인가를 전혀 다루지 않는다.** → [[lethal-trifecta]] · [[agent-identity-separation]]

## References

- [[tech-bridge-acp-universal-remote]] · [[agent-client-protocol]] · [[model-context-protocol]] · [[agent-harness-design]] · [[cloud-agent-delegation]] · [[goose]]
