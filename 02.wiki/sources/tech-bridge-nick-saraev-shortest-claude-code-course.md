---
title: "Tech Bridge — 세상에서 가장 짧은 클로드 코드 강의 (Nick Saraev): 앱 설치부터 모드 · 모델 · CLAUDE.md · 세션 · 스킬 · 커넥터 · 서브에이전트 · 예약 · 아티팩트까지"
type: source
tags: [claude-code, beginner, desktop-app, permission-modes, auto-mode, effort, claude-md, session, context, agent-skills, connectors, subagents, scheduled-tasks, remote-control, artifacts, nick-saraev, video]
source-url: https://www.youtube.com/watch?v=uOcO1QNmJOA
source-type: video
author: Tech Bridge (번역 재배포, 내레이션 없음) · 화자 [[nick-saraev]](설명란 근거 — 발화 · 태그에 이름 없음) · 원본 링크 · 녹화일 미상
date-published: 2026-11-04
ingested: 2026-11-05
created: 2026-11-05
updated: 2026-11-05
---

# Tech Bridge — 세상에서 가장 짧은 클로드 코드 강의 (Nick Saraev)

[[tech-bridge|Tech Bridge]]의 **4:48 1인 입문 해설, 공식 챕터 9, 내레이션 없음.** 오디오는 `English (US) original (default)` + 더빙 7개 언어이고 **한국어 트랙 · `ko-orig`가 없어** 인용은 en-orig로만 한다. 제목의 "[한글자막]"과 달리 수동 자막은 없다. en-orig는 00:22에 시작한다(첫 챕터 대부분 무캡션). `upload_date` 20261104 = 2026-11-04 18:00 KST. raw: `01.raw/articles/2026-11-04_세상에서 가장 짧은 클로드 코드 강의 설치부터 실전 활용까지.md`.

[[nick-saraev|Nick Saraev]](설명란 근거)가 [[claude-code|Claude Code]]를 처음 켜는 사람에게 **데스크톱 앱 기준으로** 기능을 한 번씩 짚는다. 새 주장보다 **입문자에게 무엇을 어떤 순서로 알려 주는가**가 볼거리다. 정리(이 페이지의 말):

> **폴더를 하나 주고 결과를 말로 설명한다. 모드는 auto로 두고, 모델과 effort로 사용량을 조절한다. 기억은 CLAUDE.md에 두고 주제가 바뀌면 새 세션을 연다. 잘된 일은 스킬로 저장하고, 커넥터 · 서브에이전트 · 예약으로 넓힌다.**

> ⚠️ **입문 소개라 근거가 없다.** 사례(3D 아파트 시각화, 웹사이트 100개)는 화자의 1인칭 일화이고 측정이 아니다. 요금 · 화면은 설명란이 *"영상 속 화면과 요금은 원본 제작 시점의 설명입니다."* 라고 밝힌다. 위키는 어느 기능의 현재 동작도 공식 문서로 확인하지 않았다.

> ⚠️ **화자 귀속은 설명란 근거다.** 이름은 설명란에만 있고 발화 · `tags`에 없다. 원본 영상 링크도 없어 녹화일은 미상이다. 시점 단서는 약하다. *"now mods"*(03:53)와 Haiku · Sonnet · Opus 3단 구성뿐이고 모델 버전은 발화하지 않는다. 제목의 *(자막·마무리 수정)* 은 수정 전 판본을 시사하나 위키와 이번 목록에서 찾지 못했다.

## 챕터별 내용

### 00:00 소개
00:00~00:22 무캡션. 마무리의 *"Okay, check your timer."*(04:39)로 보아 여기서 시간 재기를 제안했을 것으로 추정한다(미확인).

### 00:23 설치하고 첫 작업 시작하기
- *"First go to Claude.com/download and download the app."*(00:22~00:25) *"Right now it's available for Mac or Windows."*(00:25~00:26)
- ⭐ **채팅과 Claude Code를 쓰기 권한으로 가른다.** 채팅은 *"it can't actually change any of your files."*(00:37~00:39) *"Claude Code can, and that's the one we want to use today."*(00:41~00:43) 위키의 [[claude-code]] 정의는 CLI에서 출발하는데, 이 영상은 **터미널을 말하지 않는다.**
- ⚠️ 요금: *"Claude Code will cost about $20 a month and it'll be the best $20 you've ever spent."*(00:44~00:48) 칭찬은 화자의 평가이고 금액은 제작 시점 기준이다.
- 빈 폴더를 만들어 *local* → *open folder*로 고른다(00:50~01:00).
- ⭐ **결과를 말하라.** *"In general, you want to describe the outcome and not the steps to get there."*(01:06~01:09) *"Claude can usually figure that part out."*(01:09~01:10) → [[outcome-engineering]]
- 사례: 평면도와 매물 사진으로 3D 시각화를 시켰더니 *"It ended up even finding a bunch of products on Amazon that I could one-click order"*(01:18~01:21). ⚠️ 1인칭 일화.
- 잘못되면 stop을 누르거나 정정을 입력한다(01:25~01:31).

### 01:32 작업 모드 선택
- *"This decides how much Claude works on its own before asking you."*(01:32~01:34)
- *"Manual will ask you every time it wants to make a change."*(01:37~01:39)
- *"Plan means Claude will look around, do a bunch of research, make a really in-depth road map, but won't proceed until you approve it."*(01:39~01:45)
- *"auto will let it work almost completely on its own, but it will have a second AI constantly checking to see if Claude is up to no good."*(01:45~01:52) → [[anthropic-claude-code-auto-mode]]의 classifier 설명과 같은 방향이다.
- ⭐ ⚠️ *"I recommend sticking with auto for virtually everything."*(01:56~01:58) 바로 앞에서 위험을 *"like potentially deleting files on your computer."*(01:55~01:56)라고 말했는데, 입문자에게도 auto를 권한다. 어떤 경우에 예외를 둘지는 말하지 않는다.

### 02:00 모델과 사용량
- *"Haiku is the cheapest, Sonnet is sort of your middle ground, Opus is the most expensive, but also the most powerful."*(02:04~02:10) 버전 번호는 발화하지 않는다.
- *"There's also an effort setting, which corresponds to how long Claude will think about your problem before answering it."*(02:10~02:14) *"I usually set mine to medium or high across the board."*(02:14~02:16)
- 모델과 effort는 사용량과 연결된다: *"you only have a certain amount of it before Claude cuts you off."*(02:19~02:21) → [[hidden-harness-calls]]의 사용량 논의와 함께 읽는다.

### 02:24 기억과 세션 관리
- *"a new session doesn't remember what you talked about in the last one unless you have some sort of memory."*(02:25~02:28)
- *"creating a file called Claude.md, which stores information that Claude can read at the beginning of any individual session."*(02:30~02:35) *"by typing {slash}init, and it'll automatically create a Claude.md for you based off what you've done in the workspace so far."*(02:37~02:41) → [[agent-memory]]
- ⭐ *"Claude is forced to reread literally the whole thing every single time you have a conversation with it."*(02:44~02:47) *"That means long sessions get slower, more expensive, and usually lower quality."*(02:47~02:51) *"if you're switching a topic or you're building something new, always start a new session."*(02:51~02:55) → [[context-resets-and-compaction]]
  - ⚠️ 입문용 단순화다. [[prompt-caching]]과 compaction은 말하지 않아서 "다시 읽는 비용"이 그대로 청구되는 것처럼 들린다. "lower quality"의 근거도 없다.

### 02:58 변경 내역과 스킬
- 변경 카운터: *"These are the lines that it has added or removed to the files that it's changed."*(03:01~03:04) 대개 몰라도 된다고 한다(03:04~03:08). ⚠️ 입문자에게 diff 검토를 권하지 않는 대목이다. 위키의 [[verification-bottleneck]]과 긴장한다.
- 오른쪽 브라우저 패널: *"you have a right-hand side browser pane"*(03:09~03:10)로 앱을 보며 피드백한다.
- ⭐ *"A skill is a saved set of instructions for the jobs that you're doing."*(03:18~03:22) 만드는 법: *"Easiest way to do this right is just do the thing you want to do and tell Claude"*(03:33~03:37) *"make this into a skill."*(03:38) → [[agent-skills]]
- 자기 스킬 예시: YouTube 영상 편집, 고객 제안서 발송, 팟캐스트 게시, 시각화, 게임 제작(03:25~03:35). ⚠️ 품질 · 검증은 말하지 않는다.

### 03:40 도구 연결과 병렬 작업
- *"A connector just lets Claude use any other app just like yourself."*(03:43~03:46) 예: GitHub · Slack · Linear · Asana · Trello(03:46~03:48). ⚠️ 권한 범위는 말하지 않는다 → [[least-privilege-connectors]]
- *"You can also install custom plugins and now mods"*(03:51~03:53). 뜻은 *답을 만드는 방식을 바꾼다*는 것까지만 나온다(03:55~03:57).
- *"The way Claude does this is by handing side jobs to sub agents."*(03:59~04:04) ⚠️ *"I built these 100 websites in approximately the same amount of time it took me to build one using sub agents."*(04:10~04:15) 1인칭 일화이고 품질 · 비용은 말하지 않는다. → [[agent-swarm]] · [[subagent-folding]]

### 04:16 예약·원격 제어와 아티팩트
- *"let Claude work while you're away by clicking on scheduled and then creating a task that runs without you."*(04:15~04:21) → [[scheduled-agent-automations]]
- Remote control: *"download Claude on your phone and now you can chat with it while you're at the gym"*(04:24~04:27).
- *"An artifact is a simple static web page that allows you to visualize what it worked on."*(04:31~04:35) 친구 · 동료와 공유할 수 있다고 한다(04:35~04:38).

### 04:40 마무리
*"Okay, check your timer."*(04:39) *"I cover all this sort of stuff on my channel."*(04:41~04:42) 끝인사와 구독 요청으로 닫는다.

## 등장 개체

- 인물: [[nick-saraev]](설명란 근거) · [[tech-bridge]]
- 조직: [[anthropic]]
- 제품 · 모델: [[claude-code]] · ChatGPT · Haiku · Sonnet · Opus(버전 미발화) · GitHub · Slack · Linear · Asana · Trello · Amazon(언급 수준)
- 개념: [[outcome-engineering]] · [[agent-memory]] · [[context-resets-and-compaction]] · [[agent-skills]] · [[scheduled-agent-automations]] · [[anthropic-claude-code-auto-mode]] · [[prompt-caching]] · [[least-privilege-connectors]] · [[agent-swarm]] · [[verification-bottleneck]]

## 이 위키에서의 좌표

- **입문자가 보는 Claude Code 표면을 한 번에 적은 소스다.** 앞선 소스들은 만드는 팀의 운영이나 숙련자의 비교를 다뤘다. 여기서는 앱의 탭 · 모드 선택기 · 더하기 버튼이 기준이다.
- **숙련자 소스와의 대비.** [[nick-saraev]]의 앞선 두 비교 편은 max effort로 모델을 시험했는데, 여기서 본인 설정은 medium 또는 high다. [[tech-bridge-better-stack-claude-code-agent-summary-cost]] · [[tech-bridge-ai-labs-token-economizer]]가 측정한 사용량 문제는 여기서 "한도가 있다" 한 문장으로 줄어든다.
- 새 개념 페이지는 만들지 않았다. 모든 항목이 기존 페이지에 있고, 이 영상은 입문 수준의 증언을 더한다.

## ⚠️ 유보

- 화자 이름은 설명란뿐이다. 목소리 동일성 · 원본 영상 · 녹화일은 미확인이다.
- 요금 · 플랫폼 · 메뉴 이름은 제작 시점 설명이고, 공식 문서를 열어 확인하지 않았다. *mods*의 실제 동작도 미확인이다.
- 사례(3D 시각화, 100개 웹사이트)는 1인칭 일화다. 설명 없이 화면에만 있는 내용은 영상을 보지 않아 다루지 못했다.
- ASR: *"{slash}init"*(`/init`), *"Claude.md"*(`CLAUDE.md`), *"skill.mds"*(`SKILL.md`), *"Thank you very much for your day"*(time 오인식 추정). `en`은 auto를 `a car`, Manual을 `The manual`로 바꾸고, ko는 auto를 "자동차", tabs를 "속눈썹", workspace를 "우주"로 옮겨 인용하지 않았다.

## References

- raw: `01.raw/articles/2026-11-04_세상에서 가장 짧은 클로드 코드 강의 설치부터 실전 활용까지.md`
- https://www.youtube.com/watch?v=uOcO1QNmJOA
- 설명란 관련 자료(⚠️ 열어 보지 않았다): https://claude.com/download · https://code.claude.com/docs/en/overview
