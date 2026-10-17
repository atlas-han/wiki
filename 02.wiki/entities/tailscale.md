---
title: Tailscale
type: entity
category: org
tags: [mesh-network, wireguard, identity-based-auth, ai-gateway, mcp-gateway, aperture, tsnet]
aliases: [Tailscale, Aperture, Tailscale Aperture, TSNet, tailnet, 테일스케일, 꼬리비늘 (ko 오역)]
links:
  - "https://tailscale.com"
  - "https://tailscale.com/docs/aperture"
  - "https://aperture.tailscale.com"
sources: [tech-bridge-tailscale-aperture-ai-without-lock-in]
created: 2026-10-17
updated: 2026-10-17
---

# Tailscale

**신원 기반 mesh network 회사다.** 화자의 말로는 *"Tailscale is an identity-based mesh network. It's built on WireGuard."*(09:37~09:41) 이 위키에는 [[remy-guercio|Remy Guercio]]의 발표 [[tech-bridge-tailscale-aperture-ai-without-lock-in]]로 처음 들어왔고, 그 위에 지은 AI gateway **Aperture** 가 주제다. 링크는 설명란에서 가져왔고 열어 보지 않았다. ko는 회사 이름을 "꼬리비늘"로 옮긴다.

## 네트워크 — 연결에 신원이 붙는다

- 클라이언트를 *"containers, laptops, GPU servers"*(09:53~09:55)에 깔면 *"every connection that's now made over that tailnet uh comes with the identity of the machine or the user on the other side."*(09:58~10:05)
- 기기 태그와 그 아래 인스턴스별 node ID(*"This is a PR review bot. (…) a separate node ID underneath that says the instantiation of that PR review bot."* 10:10~10:15), 그리고 사용자(*"it's just me using Cloud Code[=Claude Code] on my laptop"* 10:17~10:20). Entra·Okta 그룹 동기화도 언급된다(10:22~10:28). → [[agent-identity-separation]]
- **TSNet**: *"It's called TSNet. It's an open-source library. You can use it to build these sorts of apps. That is what we use to build Aperture."*(10:34~10:41)

## Aperture — AI gateway (⚠️ 전부 당사자 진술)

| 항목 | en-orig |
|---|---|
| 자리 | *"it sits in between your agents and that interface of that agent uh and you know, all of your endpoints"*(08:05~08:11) |
| 공급자 | *"It's got Anthropic, OpenAI, Vercel, you know, it's got even Anthropic OAuth, uh you know, Bedrock, Codex"*(11:20~11:26) |
| 신원별 모델·예산 | *"You get unlimited budget with a cheap model, and you get an extremely narrow budget with a frontier model"*(11:56~12:01) |
| LLM + MCP gateway | *"we're both an LLM gateway and an MCP gateway, and we even do off[=auth] like injection for just standard APIs and re-expose those as MCPs, too."*(12:33~12:43) |
| 팀별 커넥터 권한 | 마케팅은 Google Calendar·Gmail, 엔지니어링은 GitHub 쓰기 또는 읽기 전용(13:31~13:47) |
| 인터페이스 | *"we actually have a built-in chat UI. Surprise."*(14:47~14:51) APIs 위에 지어져 Slack bot·모바일·음성 인터페이스로 쓸 수 있다고 한다 |
| 예정 | pass-through auth(16:08~16:12), 샌드박스 orchestration layer(17:05~17:11) — **아직 없는 기능** |

범주로서의 AI gateway는 [[ai-gateway]]에 정리했다.

## ⚠️ 유보

- **설명란의 "오픈소스 AI 게이트웨이 Aperture"는 발화와 다르다.** 발화에서 open-source라 불리는 것은 TSNet이다. Aperture의 라이선스·가격·배포 형태·고객 수는 발화되지 않는다.
- 07:57 이후의 기능 소개는 화면 데모를 전제한다(*"as you can see here"* 12:48~12:50). 화면은 확인하지 않았다.

## References

- [[tech-bridge-tailscale-aperture-ai-without-lock-in]] · [[remy-guercio]] · [[ai-gateway]]
