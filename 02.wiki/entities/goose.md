---
title: Goose
type: entity
category: tool
tags: [harness, open-source, block, acp, mcp, linux-foundation]
sources: [tech-bridge-acp-universal-remote]
created: 2026-09-13
updated: 2026-09-13
---

# Goose

[[block|Block]]에서 시작된 **오픈소스 에이전트 하네스**. Linux Foundation에 기증됐다. 본 위키 첫 등장은 [[tech-bridge-acp-universal-remote]].

## 위키에서 알려진 사실

- **내부 프로젝트 → 오픈소스 → Linux Foundation 기증**의 경로. IP는 재단에 있고 **Block 인력 다수가 계속 작업**한다.
- **[[agent-client-protocol|ACP]] 인터페이스를 구현**한다. 데모에서 [[zed|Zed]]가 클라이언트, Goose가 에이전트로 stdio 위에서 붙었고, **Poolside AI의 터미널 클라이언트**도 같은 Goose 프로세스에 붙어 **같은 경험**을 얻었다 — *"하네스 쪽 구현은 하나이고, 이제 어떤 클라이언트든 쓸 수 있습니다."*
- **원격 전송(HTTP + WebSocket 업그레이드)을 ACP에 명세한 것이 Goose 팀**이다. 동기는 *"에이전트는 클라우드에서 돌게 될 테니까."*
- Goose 팀의 아키텍처 관점이 [[agentic-stack-decomposition]]의 출처다 — **클라이언트 · 하네스 · 도구(MCP) · 모델**.
- 하네스의 정의를 한 줄로 준다 — **도구 호출 루프를 구현하는 프로그램**. → [[agent-harness-design]]

> ⚠️ 발표자가 Goose 메인테이너다. **기능·채택 서술은 당사자 진술**이고 수치가 없다.

## References

- [[tech-bridge-acp-universal-remote]] · [[block]] · [[alex-hancock]] · [[agent-client-protocol]] · [[agent-harness-design]] · [[agentic-stack-decomposition]]
