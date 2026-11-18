---
title: "에이전트 개발 환경 (Agent Development Environment, ADE) — 에이전트는 그대로 두고 바깥의 작업대를 바꾼다"
type: concept
category: pattern
tags: [agent-development-environment, ade, agent-multiplexer, coding-agents, git-worktree, remote-agents, developer-tools]
aliases: [ADE, 에이전트 개발 환경, agent multiplexer, agent manager, 에이전트 작업대]
related: [agent-attention-management, cloud-agent-delegation, bring-your-own-subscription, always-on-agent-architecture, orchestras-not-factories]
first-seen: tech-bridge-rob-shocks-orca-review-vs-records
sources: [tech-bridge-rob-shocks-orca-review-vs-records]
created: 2026-11-18
updated: 2026-11-18
---

# 에이전트 개발 환경 (Agent Development Environment, ADE)

**코딩 에이전트 자체가 아니라, 여러 에이전트 세션을 띄우고 지켜보고 합치는 바깥의 작업대.** 모델도 에이전트도 바꾸지 않는다 — [[tech-bridge-rob-shocks-orca-review-vs-records]]의 정리로는 *"하나, 에이전트와 구독은 그대로 두고 그 바깥의 작업대만 바꾼다."*(08:45~08:49) 이 위키에는 2026-10-02 [[conductor|Conductor]]부터 같은 범주의 도구가 하나씩 들어왔고, 여섯 번째인 [[orca|Orca]] 편에서 범주 이름(*에이전트 개발 환경*, tags `ADE`)과 함께 묶을 만큼 쌓여 페이지로 세운다. [[mehul-mohan|Mehul Mohan]]은 같은 것을 *agent multiplexer* · *agent manager* 라 불렀다([[herdr]]).

> ⚠️ **이름과 경계는 위키의 묶음이다.** 소스들은 서로를 같은 범주로 부르기도 하지만(*"this field is super saturated"* — [[herdr]]) 정의를 준 소스는 없다. 아래 표의 칸은 각 도구 페이지에 적힌 것만 옮겼고, 빈칸은 *소스가 말하지 않음* 이다.

## 위키에 들어온 도구

| 도구 | 들어온 경로 | 격리 · 실행 위치(각 페이지 기준) |
|---|---|---|
| [[conductor]] | 만든 쪽 발표(10-02) | git worktree → 클라우드 샌드박스로 **이동** |
| [[agentcraft]] | 만든 쪽 발표 | 게임 지도 · 로컬 컨테이너 |
| [[warp]] | 만든 쪽 발표 | 에이전트 내장 터미널에서 출발한 오픈 소스 *agentic development environment* — 이 범주 이름에 가장 가까운 자기 표현 |
| [[herdr]] | 사용자 사용기(10-31) | 원격 worker(SSH) + 로컬 별도 프로세스 — 세션이 살아남는다 |
| [[cmux]] | 같은 사용기의 비교 대상 | 앱을 끄면 세션을 되살릴 수 없다(화자 진술) |
| [[orca]] | 제3자 리뷰 + 공식 기록 대조(11-17) | 로컬은 에이전트마다 worktree, 원격은 빌린 서버 — **둘 다 둔다** |

## 되풀이되는 구성 요소 (Orca 편 기준)

- **격리** — *"둘, 에이전트 하나에 워크트리 하나."*(08:51) 한 폴더에서 여럿이 고치면 서로 덮어쓴다는 문제의 답. ⚠️ 워크트리는 파일 작업 공간만 나눈다 — 권한 · 데이터베이스는 나누지 않는다는 한계가 [[agent-sandboxing]]에 적혀 있다.
- **보는 방식** — 터미널과 채팅은 같은 세션의 두 화면이다. *"채팅 화면은 에이전트 세션을 보는 방식 가운데 하나다."*(02:34~02:36)
- **일감 연결** — 이슈 트래커 항목에서 바로 작업 공간을 만들고, 칸반으로 상태를 본다.
- **눈으로 보는 피드백** — 내장 브라우저에서 고칠 곳을 짚어 묶음으로 넘긴다.
- **원격과 알림** — 노트북을 덮어도 계속 돌고, 사람이 필요하면 휴대폰으로 부른다. → [[cloud-agent-delegation]] · [[agent-attention-management]]
- **요금은 에이전트 쪽** — 작업대가 모델 호출 사이에 끼지 않는다. → [[bring-your-own-subscription]]

## 고를 때 볼 것 (Orca 편의 해설이 든 기준)

기능 목록보다 **기록** 을 본다 — 릴리스 노트(무엇이 언제 들어왔나), 열린 이슈 수, 라이선스, 만드는 곳, 텔레메트리 문서. *"플러그인은 아직 알파이고 열린 이슈가 수천 개이며 도구가 거의 매일 바뀝니다."*(08:58~09:02)

## 미해결

- 이 층이 오래 남는가. [[dont-beat-the-market]]은 범용 워크플로가 결국 기본 하네스에 들어간다고 보는 쪽이고, Conductor 자신이 그 반대 사례로 적혀 있다.
- *워크트리는 끝났다*(Lauren Tan, 11-14)와 *에이전트 하나에 워크트리 하나*(이 편)가 같은 주에 나란히 있다. → [[cloud-agent-delegation]]

## References

- [[tech-bridge-rob-shocks-orca-review-vs-records]] — 첫 근거(범주 이름 · 구성 요소)
- 도구 페이지: [[conductor]] · [[agentcraft]] · [[warp]] · [[herdr]] · [[cmux]] · [[orca]]
