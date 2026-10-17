---
title: Dominik Kundel
type: entity
category: person
tags: [openai, codex, developer-experience, app-server, speaker]
aliases: [Dom, Dominik, dkundel, 도미닉 쿤델]
links:
  - "https://x.com/dkundel"
sources: [tech-bridge-codex-app-server]
created: 2026-10-16
updated: 2026-10-16
---

# Dominik Kundel

[[openai|OpenAI]]에서 [[codex|Codex]]의 **developer experience**를 맡는다. 이 위키의 유일한 소스는 [[tech-bridge-codex-app-server]] — Codex 하네스를 감싼 프로토콜 [[codex-app-server|App Server]] 위에 자기 에이전트 인터페이스를 짓는 법을 다룬 17:40 발표다. 같은 팀(developer experience)의 [[charlie-guo|Charlie Guo]]·[[gabriel-chua|Gabriel Chua]] 워크숍([[tech-bridge-cooking-with-codex]])이 App Server를 소개만 했다면, 이 발표는 그것을 17분 전체로 푼다.

> ⚠️ **신원 근거.** en-orig엔 *"my name is Dom. I work at OpenAI on developer experience specifically for Codex."*(00:31~00:37)까지만 있다. **성 Kundel과 "Codex 개발자 경험(DevX) 팀 리드" 직함은 설명란**(*"도미닉 쿤델(Dominik Kundel)"*)과 링크 `x.com/dkundel` 에서 나온다(링크는 열어 보지 않았다). 자막과 충돌하지 않는다. **"리드"는 발화되지 않았다.**

## 위키에서 알려진 것 (전부 당사자 진술)

- App Server = *"the protocol that wraps the codeex[=Codex] harness"*(01:02~01:07). ACP와 *"a very similar concept"* 이지만 ACP는 *"a more more uh generic protocol"* 이고 App Server는 *"more control over the individual parts of the harness"*(06:04~06:13) → [[agent-client-protocol]]
- 직접 만든 이벤트 인스펙터(03:20~03:28), Visual Basic 클라이언트를 *"largely in one shot"*(11:11~11:13), **Doom 안의 Codex**(Electron + Cloudflare Doom Wasm, dynamic tools로 게임 조작, 11:55~14:28)
- 팁 셋: 하네스 버전을 직접 번들하라 · 새 함수는 deferred로 노출하라 · base instructions를 바꾸지 말고 developer instructions를 덧붙여라(*"make sure that the actual prompt is in distribution"* 17:11~17:16) → [[embedded-agent-harness]] · [[deferred-tool-context]]
- 발표 단서: *"the keynote yesterday"*(00:49), *"we're going to both dive tomorrow in the afternoon"*(01:35~01:37), 끝나고 *"the OpenAI booth"*(17:34~17:36) — 이틀 이상 이어지는 행사의 둘째 날 이후로 읽힌다(행사명 미발화 → [[ai-engineer]] 추정)

## References

- [[tech-bridge-codex-app-server]] · [[codex-app-server]] · [[codex]] · [[openai]] · [[embedded-agent-harness]]
