---
title: Conductor
type: entity
category: product
tags: [coding-agents, multi-agent, desktop-app, cloud-sandbox, collaboration, worktree, developer-tools]
aliases: [conductor.build, 컨덕터, Driver (ASR 오역), Coda (ASR 오역)]
links: [https://www.conductor.build]
sources: [tech-bridge-conductor-orchestras-not-factories]
created: 2026-10-02
updated: 2026-10-02
---

# Conductor

**여러 코딩 에이전트를 한 인터페이스에서 동시에 관리하는 데스크톱 앱이자 그것을 만드는 회사.** 공동 창업자 [[charlie-holtz|Charlie Holtz]]가 [[tech-bridge-conductor-orchestras-not-factories]]에서 소개했다. 본 위키 첫 등장.

> *"Conductor is a desktop app for managing a team of coding agents all at the same time. So instead of having a bunch of terminal windows for your cloud[=Claude] codes or your codeexes[=Codex] or your uh whatever uh coding agent, you have one interface to manage them all."* (00:45~00:59)

## 이력 (자막에서)

| 단계 | 내용 | en-orig |
|---|---|---|
| 전신 | 팀은 *"a totally different app called Chorus"* 를 만들고 있었다 | 02:09~02:14 |
| 탄생 | [[claude-code|Claude Code]] 파워 유저로서 워크플로 전체를 그 위에 짜다가 *"cloning our repo five times and then we discovered work trees and then bit by bit we had built conductor as an internal tool"* | 02:14~02:30 |
| 아키텍처 1 | *"every uh every task in conductor was built on a git work tree"* — 작업 = git worktree | 10:06~10:11 |
| 아키텍처 2 (발표 시점 "이번 주") | *"now they're in a cloud sandbox"* — 노트북을 덮어도 에이전트가 계속 돈다 | 10:01~10:14 |

## 발표에서 시연된 기능

- **클라우드 샌드박스** — 워크스페이스마다 구름 아이콘, 클릭하면 샌드박스 정보(09:51~10:01). → [[cloud-agent-delegation]]
- **실시간 협업** — 팀원별로 진행 중인 워크스페이스 목록, 들어가서 실시간으로 보기, 동료 워크스페이스의 변경 리뷰와 채팅(10:22~12:29). *"we're rolling this out to uh all conductor users this week"*(12:43~12:44). → [[multiplayer-agent-context]]
- **Conductor API** — 에이전트가 스스로 워크스페이스를 띄운다. 화자의 [[openclaw|OpenClaw]]가 Telegram·Slack 메시지를 받아 워크스페이스를 생성(12:58~13:53).

## 사내 관행 (화자 진술)

- **[[slop-free-zone]]** — CI에서 migrations 파일 변경은 사람 리뷰 필수(05:51~06:02). docs·CLAUDE.md·스킬에 공을 들인다.
- **CIA (Conductor Internal Agent)** — Slack 메시지·Discord 버그 요청·회의 녹음을 Postgres 테이블에 모으는 사내 에이전트(07:03~07:40). → [[company-brain]]
- 스스로를 *"a chat app"* 으로 부르며, 긴 채팅 렌더링 성능을 위해 React 쿼리 최적화에 시간을 쓴다(04:23~04:37) — [[dont-beat-the-market]]의 *real alpha* 예시.

## ⚠️ 표시

- 이름 **"Conductor"는 [[orchestras-not-factories]]의 지휘자 비유와 맞물린다** — 발표의 결론이 제품명과 같은 은유다. 당사자 발표로 읽을 것.
- ko 자막에서 제품명이 **"Driver"·"운전자"·"운전기사"·"드라이버"·"운전사"·"Coda"** 로 14회 이상 바뀐다(`en`도 *"Driver"*). 검색 시 주의.
- 가격·지원 에이전트 목록·클라우드 인프라는 발화되지 않는다. 설명란 링크는 열어 보지 않았다.

## References

- [[tech-bridge-conductor-orchestras-not-factories]] · [[charlie-holtz]]
- 관련: [[claude-code]] · [[codex]] · [[openclaw]] · [[cloud-agent-delegation]] · [[multiplayer-agent-context]] · [[company-brain]] · [[slop-free-zone]]
