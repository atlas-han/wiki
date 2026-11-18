---
title: Orca
type: entity
category: product
tags: [agent-development-environment, coding-agents, open-source, mit-license, git-worktree, built-in-browser, remote-agents, mobile, telemetry, developer-tools]
aliases: [Orca, 오르카, stablyai/orca, orca.dev]
links:
  - https://github.com/stablyai/orca
  - https://orca.dev
sources: [tech-bridge-rob-shocks-orca-review-vs-records]
created: 2026-11-18
updated: 2026-11-18
---

# Orca

**Claude Code · Codex 같은 CLI 코딩 에이전트를 여러 개 띄워 놓고 한곳에서 굴리는 오픈 소스(MIT) 작업대.** [[stably-ai|Stably AI]]가 만든다. 새 모델도 새 코딩 에이전트도 아니다 — *"오르카는 새로운 AI 모델이 아닙니다. 새로 나온 코딩 에이전트도 아닙니다."*(01:09~01:13) 위키에는 [[rob-shocks|Rob Shocks]]의 리뷰를 공식 기록과 맞춰 본 한국어 해설 [[tech-bridge-rob-shocks-orca-review-vs-records]](2026-11-17)로 처음 등장한다. → [[agent-development-environment]]

> ⚠️ **근거는 해설 하나다.** 기능 설명은 해설이 README · 릴리스 노트 · orca.dev 문서에서 옮긴 것이고 수치는 채널이 2026-11-15에 GitHub API로 집계한 값이다. 위키는 저장소 · 문서 · 원 리뷰를 열지 않았다. ko ASR 표기는 *오르카*.

## 무엇인가 (해설 전달)

- 소개 글: *"터미널에서 돌아가는 에이전트라면 오르카에서도 돌아간다."*(01:20~01:21)
- **모델을 대신 부르지 않는다** — 사용자 컴퓨터에 이미 깔린 [[claude-code|Claude Code]]를 그대로 실행한다. *"그래서 요금도 오르카가 아니라 원래 쓰던 구독에서 나갑니다."*(01:52~01:54) 기업용 페이지: *"오르카는 중간에 끼지 않는다."*(01:58~02:00) → [[bring-your-own-subscription]]
- 화면: 왼쪽 프로젝트 목록, 가운데 터미널.

## 기능 (해설 전달)

| 기능 | 내용 | 기록(해설이 든 날짜) |
|---|---|---|
| 채팅 화면 | 에이전트 세션을 보는 방식 가운데 하나 — 같은 에이전트를 터미널로 보느냐 채팅으로 보느냐. 기본값은 터미널 | 릴리스 기록에 6월 말부터, 11월 4일 릴리스부터 첫 설치 때 선택 |
| 워크트리 | 에이전트마다 작업 폴더 · 브랜치를 따로. GitHub 이슈 · Jira · Linear 항목의 시작 버튼 → 워크트리 생성. 칸반 보드(할 일 · 진행 중 · 리뷰 중 · 완료) | — |
| 내장 브라우저 | 에이전트가 만든 화면을 앱 안에서 열고, 고칠 곳에 표시 · 메모 → 한 묶음으로 에이전트에게 전달 | Chrome 호환 비밀번호 관리 11월 5일, 확장 프로그램 기본 켜짐 11월 13일 |
| 원격 | 빌린 서버에서 에이전트 실행(노트북을 덮어도 계속). 채팅 화면은 입력 창이 로컬에 있어 타자 지연이 느껴지지 않는다. 문서: SSH 세션은 터미널 기반 채팅 | — |
| 모바일 | *"모바일 앱은 내 컴퓨터의 오르카를 조종하는 리모컨입니다."*(06:17~06:21) 알림 → 밖에서 답 | — |
| 플러그인 | 아직 알파(정리에서만 언급, 본론은 무캡션) | — |

## 저장소 통계 (해설 집계, 2026-11-15)

저장소가 생긴 지 여덟 달. 릴리스 1,012개(시험판 · 모바일 앱 포함), 10월 15일부터 31일 동안 정식 릴리스 25(챕터 제목 *31일 중 25일*), 머지된 PR 2,525, 열린 이슈 4,750, 머지되지 않은 PR 3,761, GitHub 별 12만 5천+. 소개 글의 자기 진술: *"우리는 매일 배포한다. 그래서 이 기능 목록은 늘 뒤쳐져 있다. 진짜 기능 목록은 변경 기록이다."*(00:03~00:07)

> ⚠️ 열린 PR이 머지된 PR보다 많다 — 해설이 전한 값 그대로이고 위키는 검증하지 않았다.

## 오픈 소스와 회사

- MIT 라이선스 — *"회사가 방향을 틀어도 그 시점까지의 코드는 남습니다."*(07:47~07:48)
- 만드는 곳은 회사([[stably-ai]], Y Combinator 투자). 앱은 무료지만 계정 로그인이 필요한 기능이 있다(모바일 연결 · 공유 링크).
- 텔레메트리 — 공식 문서: *"이 식별자는 익명이 아니라 가명이다."*(08:06~08:08) 파일 내용 · 프롬프트 · 에이전트 응답은 수집하지 않도록 설계했고 설정에서 끌 수 있다(문서에 따르면).

## 미해결

- 원격 실행에서도 워크트리를 쓰는지, 원격 서버를 누가 제공하는지(사용자 서버인지 Orca의 서비스인지).
- 유료 요금제의 내용 — *기업용 소개 페이지* 가 있다는 것만 나온다.
- 지원 에이전트의 범위(발화는 Claude Code · Codex 둘).

## References

- [[tech-bridge-rob-shocks-orca-review-vs-records]] · [[rob-shocks]] · [[stably-ai]]
- 같은 범주: [[conductor]] · [[herdr]] · [[cmux]] · [[warp]] · [[agentcraft]]
- 설명란 링크(위키 미열람): https://github.com/stablyai/orca · https://orca.dev/docs/agents/native-chat · https://orca.dev/docs/telemetry · https://orca.dev/enterprise
