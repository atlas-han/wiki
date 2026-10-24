---
title: Dots (OpenAI)
type: entity
category: product
tags: [openai, chatgpt, persistent-agent, always-on-agent, personal-agent, devday-2026]
aliases: [Dots, Dot, 닷, 도트, always-on agents in ChatGPT]
links: []
sources: [tech-bridge-altman-devday-dots, tech-bridge-brockman-start-building-before-ready, tech-bridge-claude-duet-proactive-assistant]
created: 2026-10-09
updated: 2026-10-24
---

# Dots (OpenAI)

[[openai|OpenAI]]가 **DevDay 2026에 출시한 상시 가동 개인 에이전트.** 제품명은 복수 *"dots"*, 사용자 각자의 인스턴스는 *"my dot"* 이고 이름은 사용자가 붙인다. 본 위키에는 출시 당일 [[sam-altman|Sam Altman]]의 대담 [[tech-bridge-altman-devday-dots]]로 첫 등장한다. 설명란 링크 slug는 *"Dots — always-on agents in ChatGPT"*. 슬러그의 `openai-` 는 일반 명사와의 혼동을 피하려는 위키의 선택이다.

> ⚠️ **전부 출시 당일 CEO의 무대 진술과 베타 사용자(진행자)의 체감이다.** 가격·권한 모델·연결 대상 목록·실패율 — **전부 없다.** 설명란의 Every *Vibe Check* 리뷰는 열어 보지 않았다.

## 소스에서 확인되는 것

| 항목 | 내용 (출처 [[tech-bridge-altman-devday-dots]], en-orig) |
|---|---|
| **무엇** | *"the dots the new thing we launched today"* (08:15~08:21). 일반론으로 먼저 — *"agents that are running in the background 24/7 connected to your systems doing stuff proactively for you"* (03:25~03:32) |
| **위치** | *"It has become the default way that I use chat"* — Altman, 진행자도 *"Me too"* (10:58~11:05) |
| **연구 측 조건** | *"maybe most important was Astra (…) getting the model over the intelligence bar was a key part"* (12:01~12:15) → [[openai-astra]] |
| **표면** | 모바일 등 여러 표면, *"its own cloud computer"* (11:15~11:19, ⚠️ 화자 미확정 — 진행자로 읽힘) |
| **성숙도** | 진행자: 베타에서 *"a little bit buggy"*. Altman: *"better rapidly each week (…) take some time to smooth it all out"* (11:07~11:31) |
| **사용 기간** | Altman *"the few weeks that I've been using dots"* (15:09~15:11) |

## 일화 (전부 1인칭 또는 전언)

1. **분류·보류** — *"I trust my dot to go have good judgment about what I need to think about, not think about if there's something very urgent, otherwise handle things for me"* (08:54~09:05). 아침의 깊은 작업 시간을 되찾았다.
2. **선제 경고** — 키노트 5분 전 Tibo의 Dot이 발표 자료(Space)를 보고 데모 실패를 예고, 고칠지 물었다. 고치지 못했고 *"maybe the next version we'll be able to go fix that in prod"* (09:41~10:11, ⚠️ 제3자 일화).
3. **일정 맥락** — 회의 사이 쉬는 시간에 볼 것 하나를 짚어 줌(10:27~10:37). 진행자: 캘린더에 없고 Slack에만 있던 회의를 항공편 변경 중에 짚음(11:32~11:41).
4. **밤새 반복 구현** — 메모·음성 메모로 던진 아이디어를 *"five or six versions"* 로 만들고(12:56~12:59), 아침이면 *"the next seven steps"* 까지(13:36~13:40).
5. **포기한 검색을 이어받음** — Codex로 10~20분 못 찾은 Slack 항목을 *"kept thinking about it overnight"*, 스크린샷 이미지를 전부 보고 찾음(14:20~14:43).
6. **이름** — Altman *"Doie"*(전엔 *"Alfred"*), 진행자 *"Boo"* (10:43~10:54) → [[agent-persona-naming]]

## 이 위키에서의 좌표

- [[persistent-agent-teams]] — 09-06 *"능동적 컴퓨터"*, 09-23 *"세 번째 단계의 문턱"* 의 **출시된 형태**. 봇 팀이 아니라 1인 1 Dot, 그러나 [[chatgpt-space|Space]]에서는 여러 사람의 Dot이 함께 일한다.
- [[muse]] — Meta의 같은 범주 제품. 이름 짓기 · [[proactive-idea-feed]] · [[nightly-memory-consolidation]] 과 겹친다. ⚠️ Dot의 *"overnight"* 는 기억 정리가 아니라 **미해결 작업의 계속**이다.
- [[multiplayer-agent-context]] — *"seven people's dots can working together"*(17:04~17:08).

## ⚠️ 유보

- **권한·감사·승인 경계가 한 마디도 없다** — Slack 전체·캘린더·발표 자료를 읽고, 다음 버전 목표가 *"fix that in prod"* 다. 같은 CEO의 [[ai-privilege]] 제안(09-06)도 나오지 않는다.
- 가격, 어떤 시스템에 연결되는지, 실패 사례 — 없음.
- 제품 정식 표기(Dots / Dot)와 ChatGPT와의 경계 — 설명란 slug 외 근거 없음.

## 사장의 사용기와 권유 (2026-10-11 · [[tech-bridge-brockman-start-building-before-ready]])

출시 당일 CEO 다음으로 들어온 **두 번째 1인칭 출처**다([[greg-brockman|Brockman]]).

| 항목 | 내용 (en-orig) |
|---|---|
| **녹화 직전의 실례** | 며칠 무시한 이메일 → 조사 → 답장 초안 → *"Do you approve?"*. *"it's not theoretical. With dots, I actually got that (…) right before we we started this podcast"* (02:21~02:45) |
| **모델** | ⭐ *"It's powered by GPT-6 Astra"* (27:14~27:17) → [[openai-astra]] |
| **실행 환경** | *"It has its own cloud computer and it can optionally hook to your local computer"* (26:30~26:34). 출시일 대담의 *"its own cloud computer"* 를 화자를 확정해 재확인하고, **로컬 연결 옵션**이 새로 나온다 |
| **대비** | *"task-based system that you kind of micromanage that lives on your laptop. You close your laptop, it stops working"* (26:39~26:43) |
| **권하는 시작법** | 작은 과제(*"go buy something for you"*), *"I really like texting mine"*, 커넥터 설정, 반복 과제·조사 (26:51~27:10) |
| **능동 연결** | 지역 질문을 기억했다가 새 뉴스가 나오면 먼저 알린다 (27:26~27:41) |
| **모닝 브리핑 4단계** | 사람을 대신해 연락을 마치고 구매 주문 승인만 받는 단계는 *"not quite there yet"*, 그러나 *"with dots, we actually have the technology for it"* (18:44~19:10) |

⚠️ 가입처로 *"sign up for chat.openai.com"* (26:18~26:20)이라고 발화되는데, Dots 전용 주소의 ASR인지는 판독하지 않았다. 권한·승인 경계는 여전히 *"Do you approve?"* 와 *"approve this purchase order"* 두 장면뿐이다. 위 유보는 그대로 유효하다. ⚠️ ko는 Dots를 "점들"·"도트"·"점이"로 옮긴다.

## References

- [[tech-bridge-altman-devday-dots]] — first-seen
- [[openai]] · [[sam-altman]] · [[openai-astra]] · [[chatgpt-space]] · [[dan-shipper]]
- 관련: [[persistent-agent-teams]] · [[agent-persona-naming]] · [[proactive-idea-feed]] · [[nightly-memory-consolidation]] · [[muse]] · [[ai-privilege]]

## 같은 범주의 Anthropic 제품 (2026-10-24 · [[tech-bridge-claude-duet-proactive-assistant]])

[[claude-duet|Claude Duet]] — 선제 알림 · 클라우드 실행 · 승인 게이트. 발췌의 *"Grockbot dots all"* 이 Dots를 가리킬 수 있으나 판독 불가.
