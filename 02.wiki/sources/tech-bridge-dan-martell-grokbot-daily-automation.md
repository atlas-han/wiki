---
title: "Tech Bridge — Grok Bot으로 일상을 자동화하기 (Dan Martell 추정): 역할별 봇 프롬프트 · 초안 검토 루프 · 결제 전 승인 · 읽기 전용 재무 · team bot"
type: source
tags: [grokbot, persistent-agent-teams, chief-of-staff-bot, role-based-bots, natural-language-scheduling, draft-review-loop, style-learning, approval-gate, read-only-access, least-privilege, ask-dont-guess, team-bots, shared-channel, api-over-browser, skill-then-routine, task-recording, productivity, vendor-claim, video]
source-url: https://www.youtube.com/watch?v=mHwP7oANlnA
source-type: video
author: Tech Bridge (발췌 편집, 내레이션 없음) · 화자 [[dan-martell]] 추정(설명란 · 태그 근거, 발화엔 3인칭 이름 한 번 + "plug") · 원본 채널 · 녹화일 미상 · 원본 링크 없음
date-published: 2026-10-30
ingested: 2026-10-31
created: 2026-10-31
updated: 2026-10-31
---

# Tech Bridge — Grok Bot으로 일상을 자동화하기 (Dan Martell 추정)

[[tech-bridge|Tech Bridge]]의 **6:42 발췌 편집본, 공식 챕터 10, 한국어 내레이션 없음.** 오디오는 영어 원본 하나(더빙 7개 언어)이고 `ko-orig`가 없다. 10-27 Voss 편 · 10-28 Parakhin 편 · 10-29 Chase 편과 같은 구성이라 **인용은 en-orig로만** 한다. raw: `01.raw/articles/2026-10-30_Grok Bot으로 일상을 자동화하기.md`.

이 위키의 [[grokbot|GrokBot]] 소스는 지금까지 **만드는 쪽**([[lauren-tan]] · [[lee-robinson]] · [[jediah-katz]])의 말이었다. 이 편은 처음으로 **쓰는 쪽**, 그것도 비엔지니어의 개인 · 사업 운영 튜토리얼이다. 내용은 대부분 *chief of staff 봇에게 그대로 입력할 프롬프트* 를 읽어 주는 것이다.

테제:

> **AI 도구는 답하고, 봇은 일한다. 봇을 설정 화면이 아니라 말로 만들고(역할 · 연결 · 주기 · 출력 형식), 되돌릴 수 없는 행동 앞에는 승인을, 돈에는 읽기 전용을, 모르는 것엔 "추측하지 말고 물어라"를 박아 둔다. 초안은 사람이 고친 차이로 배우게 하고, 팀 봇은 공유 채널에 둬서 모두가 고친다.**

> *"Most AI tools just answer your question. Prompt, response. Grok Bot, you ask it to do something, it goes through everything and actually does the work."*(00:09~00:16) · *"I just talked to it like I would a team member"*(01:36~01:38) · *"ask for my okay before you pay"*(03:02~03:04) · *"give it read-only access to my accounting, banking, and email"*(04:37~04:41) · *"Do it once, save it as a skill, and then schedule it."*(06:14~06:16)

> ⚠️ **화자 신원은 설명란 · 태그 근거다.** 발화에는 이름이 3인칭으로 한 번 — *"following Dan Martell's email GPS system from Buy Back Your Time book, plug, or just whatever system you currently do"*(02:01~02:08). *"plug"* 는 자기 책 홍보로 읽히는 정황이다. 자기소개 · 직함 · 소속은 없다. → [[dan-martell]] **추정.**
>
> ⚠️ **제품 주장은 화자 발화뿐이다.** 24/7 가상 컴퓨터, 봇끼리의 그룹 채팅, team bot 메뉴, 녹화 → 스킬 모두 시연 결과 · 수치 · 실패 사례가 없다. **Grok Bot 제작사는 발화되지 않는다**(이 위키의 다른 소스는 [[cursor]] / [[spacex|SpaceX AI]] 쪽 제품으로 기록). 화자와 제작사의 관계(협찬 여부)도 미상.
>
> ⚠️ **마지막 챕터("사람의 시간을 되찾기" 06:25~06:42)는 무캡션이다.** 결론부는 자막으로 확인할 수 없다. 무캡션 9구간이 챕터 경계 직후와 겹친다(raw 참고).

## 1. 답하는 도구 vs 일하는 봇 (00:00~00:55)

- **대비**: 질문-응답 도구 vs *"actually does the work"*(00:16). 봇마다 *"its own virtual computer and login that's on 24/7"*(00:18~00:22).
- **로컬 에이전트 비판**: *"you close that laptop, the thing stops working. Or you needed to buy a Mac Mini to make it work. Not anymore."*(00:24~00:31) — 제품명은 없지만 [[persistent-agent-teams]]에 기록된 Mac mini · 공유 VM 이야기(OpenClaw 유행)와 같은 지점을 가리킨다(해석).
- **트리거**: *"My bots run on a schedule so that they can monitor Slack or if a message comes in, it can pick it up"*(00:29~00:35) — 예약 + 이벤트 두 가지.
- **오케스트레이션**: ChatGPT · Claude에서는 *"you copy and paste between projects"*(00:39~00:41)이지만 Grok Bot은 *"coordinate all the different handoffs, group chat with each other (…) and then check in to make sure that everybody's got what they need"*(00:45~00:54). → [[human-plumbing]](사람이 복사-붙여넣기 배관이 되는 문제)

## 2. chief of staff에게 말로 스케줄 맡기기 (00:55~01:42)

- 프롬프트: *"Connect to my calendar. Every weekday at 5:00 a.m., check that my mornings are spent doing deep work (…) Send me one short brief, today's meetings, who they're with, and what I need to prep, and any conflict or double bookings, and the top three things I should get done."*(01:04~01:21) + *"keep it under one page, and ask me any question you need before you start."*(01:24~01:29)
- ⭐ **설정 없이 말로 예약**: *"Notice that I didn't have to go in and configure a reoccurring schedule. I just talked to it like I would a team member and it understands"*(01:31~01:40). → [[scheduled-agent-automations]]
- 패턴: 프롬프트마다 **연결 대상 · 주기 · 출력 형식(길이 제한) · 시작 전 질문**이 들어간다.

## 3. inbox manager와 "review mode only" (01:42~02:42)

- 봇 생성도 chief of staff에게 시킨다: *"build me an inbox manager, name it something fun, and connect your Gmail and Slack"*(01:49~01:56). 매일 6시 폴더 분류 — 기준은 화자의 email GPS 체계 *"or just whatever system you currently do, cuz it'll be able to see your inbox and just mirror to that"*(02:06~02:11).
- 초안: *"Draft replies for anything that needs me in my voice using past emails sent as context (…) then send me a short list of what needs my decision."*(02:11~02:19)
- ⭐ **사람이 고친 차이로 배우는 루프**(*"pro tip"*): *"At first, have it draft everything for a few weeks."*(02:22~02:24) 그 다음 *"Every Friday, compare the drafts you wrote to this week's of what I actually sent. Look at what I changed, like the words I cut, how long my replies are, and how I sign off, and update how you write emails for me, so next week's drafts need fewer edits."*(02:26~02:40) — *"I call this review mode only."*(02:40)
  - 초안은 **보내지 않는다**(사람이 보낸 것만 정답). 피드백 신호는 별도 평가가 아니라 **사람이 실제로 보낸 메일과 초안의 diff**다. → [[skill-self-improvement]] · [[no-silent-write]]
  - ⚠️ 효과(편집량이 줄었는지)는 발화되지 않는다.

## 4. travel bot — 결제 전 승인 (02:42~03:11)

- *"remember my travel preferences. I'm talking airline seats, hotels, the style, the budget, food."*(02:51~02:56) → 후보 *"top three options"*(02:58~03:00) → ⭐ *"Once I pick one, fill in the booking and ask for my okay before you pay."*(03:00~03:04) → 캘린더에 링크 · 확인 번호 추가(03:04~03:08).
- 사람의 결정 지점은 둘 — **선택**과 **결제 승인**. 채우기는 봇이 한다. → [[action-reversibility]]

## 5. people bot · family bot — 추측 금지와 제출 전 승인 (03:11~03:59)

- people bot: 이름(*"exact spelling"*) · 만난 경위 · 연결 · 날짜 저장, 이메일 · 캘린더로 맥락 보강, ⭐ *"Never guess at spelling, and if you're not sure, just ask me."*(03:33~03:37)
- family bot: 메일에서 아이 일정 · 학교 행사 · 운동 일정을 뽑아 캘린더에, 전날 밤 알림, ⭐ *"Fill out the forms when I ask, and get me the okay before you submit anything."*(03:54~03:58)

## 6. constraint bot — 병목 하나와 숫자 (03:59~04:29)

- CRM · 매출 보고 · 분석 · 이메일을 연결하고 *"Learn the theory of constraints and every Sunday night look at my funnel"*(04:12~04:16) → *"Find the one step holding back growth and show me the numbers behind it and suggest the next test to fix it."*(04:21~04:25)
- ⭐ *"If data is missing, tell me instead of guessing."*(04:25~04:27) — people bot의 *"Never guess at spelling"* 과 같은 지시가 사업 데이터에 반복된다.

## 7. finance bot(읽기 전용) · leadership bot (04:29~05:15)

- ⭐ *"Build me a finance bot and give it read-only access to my accounting, banking, and email."*(04:37~04:41) 매일 7시 잔고 · 전날 매출 · 지출 · 이상 거래 · 이번 주 청구서 보고(04:41~04:51), 그리고 *"And never move money or pay anything."*(04:51~04:53)
  - **권한(읽기 전용)과 지시(돈을 옮기지 마라)를 둘 다** 건다. 지시만으로 막지 않는다. → [[least-privilege-connectors]]
- leadership bot: 회의 녹취 · 팀 Slack 전 채널을 연결, 매주 일요일 *"what each team is talking about this week, what decisions were made, and where it does or doesn't match up with my top priorities"*(05:05~05:10). 우선순위 목록은 사람이 준다(05:10~05:11). ⭐ *"Then link the source of anything important and tell me what you couldn't read."*(05:11~05:14) — **출처 링크 + 읽지 못한 것의 보고**.

## 8. team bot — 공유 방에 두고 모두가 고친다 (05:15~06:02)

- ⭐ *"The key thing is is put the team bots in a shared room. (…) put them in a Slack channel. And then everybody can talk to the bot in the Slack channel. And then if the bot is not smart, then they go fix the bot inside of their bot structure and then everybody wins because of it."*(05:24~05:38)
- 효과 주장: *"nobody has to wait to ask a question to a person if they're available or in a meeting. It's just the information flows."*(05:38~05:44) 예: product management bot · revenue leader bot → *"scale horizontally and have everybody get access to the knowledge of your bot"*(05:49~05:55).
- UI: *"click the plus icon and at the very bottom it says team bot"*(05:56~05:58).
- → [[multiplayer-agent-context]] · [[company-brain]](사람에게 묻는 대신 봇에게 묻는 사내 지식 — 다만 "두뇌" 같은 구조는 말하지 않는다)

## 9. API · skill then routine · 녹화 (06:02~06:25)

- ⭐ **웹 대신 API**: *"if there's an API for a website or a service I'm using, use that instead of trying to navigate a webpage. It's cheaper and way faster."*(06:03~06:11)
- ⭐ **skill then routine**: *"Do it once, save it as a skill, and then schedule it."*(06:14~06:16) → [[agent-skills]] · [[scheduled-agent-automations]]
- **녹화 → 스킬**: *"You can actually use the computer use and record a task and it'll create a skill using the recorded video of you doing something to automate it over and over again."*(06:16~06:24) — 이 위키에서 *시연 영상으로 스킬을 만든다* 는 첫 언급(제품 주장, 미확인).

## 10. 사람의 시간을 되찾기 (06:25~06:42)

자막 없음(06:27~06:42 무캡션). 내용 미상.

## 등장 개체

- 인물: [[dan-martell]](추정, 신규)
- 제품 · 조직: [[grokbot|Grok Bot]] · ChatGPT · Claude(대비 언급만) · Gmail · Slack(연결 대상) · Mac Mini(언급만) — 제작사 미발화
- 개념: [[persistent-agent-teams]] · [[scheduled-agent-automations]] · [[skill-self-improvement]] · [[action-reversibility]] · [[least-privilege-connectors]] · [[multiplayer-agent-context]]
- 책: *Buy Back Your Time*(제목만 발화, 페이지 없음)

## 이 위키에서의 좌표

- [[grokbot]]의 **사용자 쪽 첫 소스**다. 만드는 쪽이 말한 구성 요소(자기 컴퓨터 · chief of staff 코디네이터 · 루틴 · 메시징 UI)가 사용 설명서로 다시 나온다. 다만 만드는 쪽이 강조한 *바깥 루프 → Cursor projects* 같은 코딩 연결은 전혀 없다 — **비엔지니어의 개인 · 사업 운영**이 전부다.
- 승인 게이트의 동사가 [[claude-duet]]의 *"sends a message, makes a payment, signs a document, or deletes anything"* 과 겹친다(결제 · 제출). 다만 Duet은 제품 기본값, 이 편은 **사용자가 프롬프트로 직접 거는** 게이트다.
- 초안 diff 루프는 [[skill-self-improvement]]의 여러 경로 중 **사람이 실제로 한 행동(보낸 메일)을 정답으로 쓰는** 판본이다.

## ⚠️ 유보

- 화자 신원 추정(설명란 · 태그 + "plug" 정황), 원본 · 녹화일 미상, 원본 링크 없음.
- 제품 기능 · 효과 주장은 모두 발화뿐. 수치 · 실패 사례 · 비용 없음. 승인 게이트 · 읽기 전용이 **프롬프트 지시**로만 걸리는지 제품 권한으로 강제되는지는 finance bot(*"give it read-only access"*)을 빼면 발화되지 않는다.
- 번호 목록의 1번 · 3번, 마지막 챕터, 각 챕터 첫 2~7초가 무캡션.
- ko는 기계 번역이라 인용하지 않았다. `en`도 en-orig와 다른 역번역이라 인용하지 않았다.

## References

- raw: `01.raw/articles/2026-10-30_Grok Bot으로 일상을 자동화하기.md`
- https://www.youtube.com/watch?v=mHwP7oANlnA
