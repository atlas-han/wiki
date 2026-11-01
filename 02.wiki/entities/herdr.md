---
title: herdr
type: entity
category: product
tags: [agent-multiplexer, terminal, cli, coding-agents, remote-machines, ssh, notifications, developer-tools]
aliases: [herdr app, herdr.dev, 허더, holder (ASR 오역), Hodor (ASR 오역), Hurder (ASR 오역), Herder (ASR 오역), Horder (ASR 오역)]
links: [https://herdr.dev/]
sources: [tech-bridge-mehul-mohan-herdr-app-vs-cmux]
created: 2026-11-01
updated: 2026-11-01
---

# herdr

**터미널 기반 AI 코딩 에이전트 여럿을 한 화면에서 띄우고 관리하는 도구.** 원래 터미널 안에서 돌았고, 앱 버전은 화자 표현으로 *"basically a GUI application combined with CLIs"*(00:32~00:35)다. 이 위키에는 [[mehul-mohan|Mehul Mohan]]의 사용기 [[tech-bridge-mehul-mohan-herdr-app-vs-cmux]](2026-10-31 업로드)로 처음 등장한다. 화자는 이것을 *"a agent multiplexer or agent manager sort of screen"*(08:33~08:35)의 하나로 본다.

> ⚠️ **모든 내용은 1인 사용자가 몇 시간 써 본 시연 · 진술이다**(*"for the last few hours"* 08:00~08:02). 제작사 · 가격 · 버전 · 라이선스는 발화되지 않는다. 설명란 링크(herdr.dev)는 열어 보지 않았다. ASR은 이름을 *"holder"* · *"Horder"* · *"Hodor"* · *"Hurder"* · *"Herder"* · *"harder"* 로 적는다.

## 시연된 기능 (화자 진술)

| 기능 | 내용 | en-orig |
|---|---|---|
| 이전 형태의 한계 | *"holder[=herdr] previously ran into terminal directly"* — Cmd+K로 터미널을 지우면 망가졌다 | 00:43~00:49 |
| 레이아웃 · 테마 | 사이드바 + 터미널 기본형, 터미널만, 레트로(*"another 98"*) 테마, graphite 테마. 외형 커스터마이즈 폭은 좁다 | 03:39~04:32 |
| 여러 머신 | `user@host` · SSH config로 원격 머신(worker)을 추가한다. *"you can ask your local AI agent itself to configure this"* | 04:37~05:07 |
| 작업 지속 | *"Now all of this is async."* 앱을 꺼도 worker에서 계속 돈다. 로컬은 *"a different process on this Mac OS"* 가 터미널 · 에이전트를 살려 둔다 | 05:09~05:56 |
| 상태 · 알림 | 통합된 에이전트는 *"it will know like which when it is idle, when it is done, when is it working"*. 알림을 보낸다 | 06:16~06:59 |
| 지원 에이전트 | Claude Code · Codex · DeepSeek · OpenCode 등. 목록에 없는 CLI도 쓸 수 있지만 경험이 덜하다 | 06:37~07:07 |
| 레이아웃 실험 | mission control 대시보드, Slack 같은 미리보기, *"Google Meet-like a call sort of UI where agents are on call"*. *"extremely hackable"* | 08:38~09:26 |
| 서브에이전트 API | *"Hurder[=herdr] actually supports a complete API for that as well"*. 서브에이전트를 띄우고 조종하고 메인 에이전트에 보고한다 | 12:28~12:50 |
| 모바일 | 전용 모바일 앱은 아직 없다고 화자가 본다 | 11:45~11:53 |

## 화자가 고른 이유 — 세션이 살아남는가

[[cmux]]와 비교한 결정적 차이는 **앱이나 연결이 끊겨도 세션이 남는가**다. herdr는 원격 worker와 로컬 별도 프로세스로 세션이 남는다. cmux는 *"if you quit Cmux now, there is no way to get this back"*(13:29~13:32)다. 로컬 Mac은 *"if your computer actually goes to sleep"*(06:00~06:02) 멈추므로 원격 머신이 *"very, very important"*(06:04~06:07)하다. → [[always-on-agent-architecture]] · [[cloud-agent-delegation]]

## 같은 범주의 다른 도구

[[conductor]](worktree → 클라우드 샌드박스) · [[agentcraft]](게임 지도 · 로컬 컨테이너) · [[warp]](터미널 기반 ADE) · [[cmux]]. 앞의 셋은 **만든 쪽의 발표**로 들어왔다. herdr는 **사용자 비교**로 들어온 첫 도구다. 화자도 *"I know this field is super saturated"*(07:49~07:52)라고 한다. → [[agent-attention-management]]

## References

- [[tech-bridge-mehul-mohan-herdr-app-vs-cmux]] · [[mehul-mohan]]
- 관련: [[cmux]] · [[claude-code]] · [[codex]] · [[conductor]] · [[agentcraft]]
