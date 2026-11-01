---
title: cmux
type: entity
category: product
tags: [agent-multiplexer, terminal, coding-agents, ssh, tmux, developer-tools]
aliases: [cmux.com, C marks (ASR 오역), C max (ASR 오역), C-Max (ko 오역)]
links: [https://cmux.com/]
sources: [tech-bridge-mehul-mohan-herdr-app-vs-cmux]
created: 2026-11-01
updated: 2026-11-01
---

# cmux

**AI 코딩 에이전트를 여러 터미널에서 돌리기 위한 터미널 앱.** 이 위키에는 [[mehul-mohan|Mehul Mohan]]이 [[herdr]]와 비교한 [[tech-bridge-mehul-mohan-herdr-app-vs-cmux]](2026-10-31 업로드)로 처음 등장한다. 그 영상에서 cmux는 **비교 대상**이다. 기능 설명은 화자가 겪은 문제 위주다.

> ⚠️ **사용자 1인의 비판적 진술만 있다.** 화자는 처음부터 herdr 쪽 선호를 밝힌다(*"why I prefer this over C marks[=cmux]"* 00:56~00:58). cmux 측 반론 · 버전 · 제작사 정보는 없다. 설명란 링크(cmux.com)는 열어 보지 않았다. ASR은 이름을 *"C marks"* · *"C max"* · *"Cmux"* 로, ko는 *"C 마크"* · *"C-Max"* 로 적는다.

## 화자가 cmux를 쓴 이유

예전 herdr는 터미널 안에서 돌아서 Cmd+K(터미널 지우기)에 망가졌다. 그래서 *"this was my whole point of using C marks[=cmux]"*(00:39~00:41)였다. herdr 앱이 나오며 이 차이가 사라졌다.

## 화자가 겪은 문제

- **여러 머신 관리**: herdr에 비해 *"somewhat challenging with C max[=cmux]"*(04:37~04:41)
- **SSH 세션이 앱과 함께 사라진다**: *"the SSH actually does not really work properly"*(13:07~13:10). `cmux ssh`로 붙은 뒤 터미널을 나눠도 *"if you quit Cmux now, there is no way to get this back"*(13:29~13:32)다. 이유는 *"it's actually not running in a tmux-like thing"*(13:34~13:36)이다.
- **우회책은 실험 기능**: *"Cmux SSH tmux"* 는 *"an experimental thing, and it's very frictional. It just breaks a lot."*(13:36~13:43) *"if you lose your internet connection, it'll just break your terminal emulator itself."*(13:43~13:46)
- **UI 커스터마이즈**: 에이전트에게 탭 설명 제거 등을 시켰지만 *"I was not able to get a wow factor from it"*(13:54~13:58)
- 총평: *"it's definitely much more frictional to use than what I've seen with Hurder[=herdr]"*(12:56~13:00)

> ⚠️ ko(기계 번역)는 이 총평을 *"C-Max는 확실히 비싸다"* 로 옮긴다. 원문은 가격이 아니라 마찰(*"frictional"*)이다.

## References

- [[tech-bridge-mehul-mohan-herdr-app-vs-cmux]] · [[mehul-mohan]]
- 관련: [[herdr]] · [[always-on-agent-architecture]]
