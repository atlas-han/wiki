---
title: Pets vs. Cattle
type: engineering
category: pattern
tags: [infrastructure, operations, cloud, reliability]
related: [brain-hands-decoupling, agent-harness-design]
first-seen: anthropic-managed-agents
sources: [anthropic-managed-agents]
created: 2026-05-25
updated: 2026-05-25
---

# Pets vs. Cattle

인프라 운영의 비유. **Pet**은 이름 붙은, 손으로 돌보는 개체로 잃을 수 없다. **Cattle**은 서로 교체 가능한 무리로 한 마리가 죽으면 새 마리로 대체한다. 클라우드 컴퓨팅의 표준 mental model.

## LLM 에이전트 인프라에서의 적용

[[anthropic-managed-agents]]가 이 비유를 명시적으로 사용. 초기에 session·harness·sandbox를 한 컨테이너에 묶었더니 컨테이너가 **pet**이 됐다:

- 컨테이너 사망 → 세션 손실
- Unresponsive → "nursing" 필요
- 디버깅 시 사용자 데이터가 있는 컨테이너에 shell로 접속해야 함 → 디버깅 사실상 불가
- WebSocket 이벤트 스트림이 유일한 관찰 채널이라 harness 버그·패킷 드롭·컨테이너 offline이 *동일하게 보임*

해결: **brain–hands 분리** ([[brain-hands-decoupling]]). 모든 컴포넌트를 cattle화:

| 자원 | 사망 시 회복 |
|---|---|
| Sandbox 컨테이너 | tool-call error → Claude가 retry 결정 → `provision({resources})` 새 컨테이너 |
| Harness | `wake(sessionId)` + `getSession(id)`로 마지막 event부터 resume |
| Session log | 외부 durable storage — fail unit이 아님 |

## 일반 원칙

- 서비스 instance에 *고유 이름*과 *고유 state*를 결합시키지 말 것
- State는 별도 durable layer로
- 정상 회복 절차가 reboot/recreate여야 함 — fix-in-place 아님
- 모든 instance가 동일 recipe로 provision 가능해야 함

## 인용

> In our case, the server became that pet; if a container failed, the session was lost. If a container was unresponsive, we had to nurse it back to health.

## References

- [[anthropic-managed-agents]]
- 외부: [Pets vs Cattle, Cloudscaling (2012)](https://cloudscaling.com/blog/cloud-computing/the-history-of-pets-vs-cattle/)
