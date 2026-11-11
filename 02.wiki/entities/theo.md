---
title: Theo
type: entity
category: person
tags: [youtuber, developer, t3-code, t3-chat, twitch, codebase-gardening, agentic-coding]
aliases: [Theo, t3.gg, Theo - t3.gg, 태오, 테오, Tae-o, Teo, T3 Code, T3 Chat, 티스리챗, 티슈리 코드]
links:
  - https://www.youtube.com/watch?v=GtJKFhztgdM
  - https://github.com/pingdotgg/t3code
sources: [tech-bridge-theo-coding-is-gardening, tech-bridge-codex-app-server, tech-bridge-pstack-third-party-review, tech-bridge-rob-shocks-grokbot-manager-coding-agents, tech-bridge-better-stack-claude-code-agent-summary-cost]
created: 2026-11-11
updated: 2026-11-11
---

# Theo

개발자이자 유튜버(채널 *Theo - t3.gg*). **T3 Code**(오픈소스 코딩 에이전트 앱, 저장소 `pingdotgg/t3code`)와 **T3 Chat**을 만든 쪽으로 이 위키에 나온다. 위키에는 네 소스에서 이름이나 제품으로만 스쳐 오다가, 2026-11-10 [[tech-bridge-theo-coding-is-gardening]]에서 처음으로 그를 다루는 소스가 들어왔다.

> ⚠️ **본인 음성은 캡션에 없다.** 11-10 소스는 Theo의 영상 *"Coding Isn't About Code Anymore"*(`GtJKFhztgdM`)를 한국어 해설자가 옮긴 2차 전달이다(AI 내레이션). 원음 발췌 다섯 곳은 두 자막 트랙 모두 무캡션이다. 이름은 설명란 · tags 근거다(ko ASR *태오* · *태우* · *헤오*, 더빙 *Tae-o* · *Teo*). T3 Code 저장소 경로는 설명란 PR 링크에서 왔다. 위키는 원 영상 · PR을 열지 않았다.

## 해설이 전하는 이력 (2026-11-10 · 2차 전달)

- 2017년부터 4년 동안 Twitch에서 일했다. 제품 팀 소속이었지만 플랫폼 팀 회의에 늘 끼어 있었다(00:55~01:09).
- Twitch를 나와 회사를 차렸다 — *"직원 1500명 회사에서 혼자인 회사로 간 거죠."*(01:58~02:00)
- T3 Chat의 데이터 동기화 엔진을 손으로 짰다가 한 달 들여 다른 구현으로 옮겼다(2만 5천 줄 PR, 02:15~02:30).
- 지금은 세 명짜리 팀을 위해 TypeScript를 [[rust|Rust]]로 다시 쓰고 있다(03:26~03:30).
- 원래 개발을 *레고*(블록 놀이)처럼 사랑했고 AI 코딩이 그 재미를 없앨까 두려웠지만, 지금은 *"일주일에 한두 번 새벽 6시에 잠들만큼 재밌다고 합니다."*(00:48~00:52)

## 입장 — 개발자는 정원사

*"모든 팀에는 정환사가 필요하다. 뽑은 잡조 하나하나가 규칙이 되어 다시는 자하지 못하게 하는 사람 말입니다."*(05:43~05:50)[=정원사 · 잡초 · 자라지] → [[codebase-gardening]]

- **잡초**: T3 Code PR 하나로 테스트 약 1만 1천 개(약 43%) 삭제 — Claude Haiku 에이전트들이 판정했다(04:13~04:46).
- **지지대**: PR마다 실제 대화 데이터로 전송량을 재서 댓글로 남기는 검사(04:56~05:24).
- **거름**: 시간의 절반은 사용자가 못 느끼는 플랫폼 작업(02:02~02:13).
- **마찰**: *"마찰은 사람보다 에이전트를 훨씬 세게 막습니다."*(03:34~03:36) → [[agent-friction-multiplier]]
- **슬롭**: *"그는 에이전트보다 먼저 슬롭을 쓰고 있었던 겁니다."*(02:37~02:39) → [[ai-slop]]

해설은 [[lauren-tan|Lauren]](React 컴파일러 팀, 설명란 *@poteto*)이 같은 이야기를 했다고 덧붙인다(05:42~05:43, *비율 / 비유* 미확정).

## 다른 소스에 스친 이름 (2026-09 ~ 11)

| 소스 | 언급 |
|---|---|
| [[tech-bridge-pstack-third-party-review]](09-13) | 화자: *"우리 친구 Theo"* 가 [[pstack]](Lauren Tan의 스킬) 딥다이브를 했다 → [[lauren-tan]] |
| [[tech-bridge-codex-app-server]](10-14) | *"open source projects like Theos T3 code"*(02:22~02:27) — T3 Code가 [[codex-app-server]] 위에서 돈다, 사용자의 Codex 구독으로 차감 → [[bring-your-own-subscription]] |
| [[tech-bridge-rob-shocks-grokbot-manager-coding-agents]](11-02) | *"Theo is trying out a similar workflow with T3 Code"*(09:13~09:20) — [[grokbot]]으로 기기들을 몬다(트윗, 미확인) |
| [[tech-bridge-better-stack-claude-code-agent-summary-cost]](11-02) | 화자가 터미널 Claude Code 대신 T3 Code를 쓴다, T3 Code는 요약을 자기 방식으로 처리한다 → [[hidden-harness-calls]] |

→ T3 Code는 **여러 하네스(Codex · Claude Code)를 감싸는 앱**으로 그려진다(위키의 읽기, 제품 페이지는 따로 만들지 않았다).

## References

- [[tech-bridge-theo-coding-is-gardening]] — 2026-11-10 한국어 해설(6:21), 원 영상 `GtJKFhztgdM`의 2차 전달
- https://github.com/pingdotgg/t3code (설명란 PR 링크의 저장소, 위키 미열람)
