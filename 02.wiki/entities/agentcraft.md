---
title: AgentCraft
type: entity
category: product
tags: [coding-agents, multi-agent, orchestration-ui, game-design, visibility, review, collaboration, developer-tools]
aliases: [Agent Craft, AtomCraft (ASR 오역), Loopers (가칭 단순판)]
links: []
sources: [tech-bridge-agentcraft-strategy-game]
created: 2026-10-09
updated: 2026-10-09
---

# AgentCraft

**코딩 에이전트를 RTS 게임의 유닛처럼 지도 위에 놓고 감독하는 "게임에서 영감을 받은 오케스트레이터"(game-inspired orchestrator).** 개발자 [[ido-salomon|Ido Salomon]]이 [[tech-bridge-agentcraft-strategy-game]]에서 시연했다. 본 위키 첫 등장.

> *"So, I took this concept, uh, too far and I created AtomCraft[=AgentCraft], uh, which is a game-inspired orchestrator, uh, that tries to bring all that good stuff together into work."* (01:42~01:53)

## 기능 (화자 서술 — 화면은 자막으로 확인 불가)

| 층 | 기능 | en-orig |
|---|---|---|
| 기본 | 에이전트 = 지도 위 유닛. [[claude-code\|Claude Code]](*"cloud code"*)·[[openclaw\|OpenClaw]]·[[codex\|Codex]]·OpenCode 등을 기기에서 **감지**하거나 직접 **생성** | 02:16~02:39 |
| 기본 | 사이드 패널 프롬프트 + **음성**(multimodality) | 02:43~02:53 |
| 기본 | **건물 = 기능** — 플러그인·스킬 관리, 통합 터미널, 통합 Git | 03:02~03:19 |
| 가시성 | 에이전트별 과제·마지막 행동·현재 행동 사이드 패널 | 03:32~03:44 |
| 가시성 | 파일 시스템을 지도에 투영(파일 = 룬), 에이전트별 작업 위치·시점, **히트맵** | 03:47~04:25 |
| 가시성 | **스페이스바**로 주의가 필요한 가장 가까운 곳으로 점프 — 질문 답하기·계획 승인 | 04:27~04:55 |
| 할 일 | **퀘스트** — 에이전트가 코드베이스를 훑어 다음 과제를 만들고 사람은 수락 | 05:39~05:52 |
| 자율성 | **오케스트레이터**가 의도를 쪼개 **로컬 컨테이너**에서 격리 실행 | 06:20~06:36 |
| 자율성 | **루프** — Twitter·GitHub를 훑어 백그라운드로 기능 생성 | 06:37~06:54 |
| 리뷰 | **review kit** — 파일별 변경, 또는 변경의 **영상·사진**, 또는 병렬 인스턴스 중 최선 선택 | 07:12~07:36 |
| 협업 | **방(room)** — 로컬 호스팅, 터널로 사람 초대·승인, hand off·fork, 사람·에이전트 공용 채팅·게시판 | 08:21~09:48 |
| 협업 | 모바일·Telegram 접근 | 09:53~09:59 |

## Loopers (가칭) — 단순판

*"currently named TBD, um potentially loopers"*(11:15~11:21). AgentCraft의 *"Warcraft"* 급 복잡함 대신 *"more of a mobile game level"* — 파일 단위를 숨기고, 돌아오고 싶은 프로젝트와 루프에 기대 *"I prompt, I get a result, I don't really care perhaps about the way, I can see it if I want to"*(12:00~12:09). 목적은 *"lower the floor"*(10:59). *"a very very early draft"*(12:44~12:48). 별도 페이지는 만들지 않는다.

## ⚠️ 표시

- **이름** — en-orig·`en`·ko 모두 첫 소개(01:46)를 *"AtomCraft"* 로 적었다. 제목·설명란·이후 발화(02:08, 02:32, 08:21)가 AgentCraft라 ASR로 판독.
- **자율 실행 기능의 이력** — *"Now it's called software factories, but at the time it was just doing stuff autonomously."*(06:13~06:18) — [[software-factory]]라는 말 이전에 만들었다는 화자의 진술.
- 가격·라이선스·공개 여부·지원 OS·`>>` 음성 효과(*"At your command."* 02:39)의 정체는 발화되지 않거나 추정이다. 설명란 링크(`mcp-ui.dev` 포함)는 열어 보지 않았다.
- 당사자 데모, 사용 지표 없음. 사용자 반응은 화자가 받은 피드백 일화(10:15~10:52).

## References

- [[tech-bridge-agentcraft-strategy-game]] · [[ido-salomon]]
- 관련: [[agent-attention-management]] · [[conductor]] · [[claude-code]] · [[openclaw]] · [[codex]] · [[agent-visual-qa]] · [[multiplayer-agent-context]] · [[software-factory]] · [[loop-is-the-product]]
