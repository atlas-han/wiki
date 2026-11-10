---
title: "Tech Bridge — 게리 탄, AI 에이전트는 2년 안에 모든 걸 바꿀 겁니다 (Garry Tan): 채팅이 아닌 에이전트, gstack, 다섯 왕과 개인 AI의 Linux"
type: source
tags: [personal-agent, y-combinator, garry-tan, gstack, openclaw, jobs, token-cost, social-media, platform-war, open-source, video]
source-url: https://www.youtube.com/watch?v=UIMTEGqP3ys
source-type: video
author: Tech Bridge (번역 재배포 + 한국어 내레이션) · 화자 [[garry-tan]](설명란 · tags · 내레이션 근거) · 진행자 이름 · 원본 링크 · 녹화일 미상
date-published: 2026-11-06
ingested: 2026-11-07
created: 2026-11-07
updated: 2026-11-10
---

# Tech Bridge — 게리 탄, AI 에이전트는 2년 안에 모든 걸 바꿀 겁니다

[[tech-bridge|Tech Bridge]]의 **12:50 인터뷰 발췌 + 한국어 내레이션, 공식 챕터 12.** 오디오는 `English (US) original (default)` + 더빙 7개 언어이고 `ko-orig`가 없다. ⭐ 이번 en-orig는 **영어 인터뷰와 한국어 내레이션을 한 트랙에 함께 담는다**(한국어 33줄). 영어 인용과 내레이션 인용 모두 en-orig를 근거로 하고, 내레이션은 Tech Bridge의 말로 구분한다. `upload_date` 20261106 = 2026-11-06 18:00 KST. raw: `01.raw/articles/2026-11-06_게리 탄 AI 에이전트는 2년 안에 모든 걸 바꿀 겁니다.md`.

[[garry-tan|Garry Tan]](Y Combinator 대표)이 팟캐스트로 보이는 대담에서 에이전트를 채팅이 아닌 운영체제로 보라고 말한다. 자기 데이터를 대부분 넘긴 사용 사례, 연 10만~20만 달러의 토큰 비용, [[gstack|gstack]], 일자리, 소셜 피드, 플랫폼 집중까지 다룬다. 정리(이 페이지의 말):

> **지금은 비싸서 소수만 쓰지만 2~3년이면 누구나 쓴다고 본다. 그때의 싸움은 어느 에이전트를 쓰느냐이고, 필요한 것은 개인 AI를 위한 Linux다.**

> ⚠️ **전망과 이해관계.** 2~3년은 근거 없는 전망이고, 내레이션도 *"2, 3년 안에 모두가 쓴다는 건 그의 전망이고"*(12:33)라고 표시한다. 화자는 스타트업에 투자하는 쪽이고 gstack의 제작자다. *400배*는 측정 방법이 없는 자기 수치다.

## 핵심 주장

1. **사람들이 가장 많이 틀리는 것은 채팅으로 보는 것이다.** *"they just think that AI is just chat,"*(00:51~00:53)
2. **차이는 작업 기억이다.** 사람은 *"seven plus or minus three things"*(01:23), 에이전트는 *"a stack of a thousand pages, like think like three Harry Potter books."*(01:36~01:38)
3. **2~3년이면 보편화된다.** *"it seems inevitable in about two to three years, I would say, everyone's going to do it"*(04:04~04:09) 막는 것은 비용이다.
4. **일자리는 단기엔 불확실하다.** *"That's certainly my hope, right? Uh in the short term, it may not."*(05:50~05:52)
5. **다음 전쟁은 에이전트 선택이다.** *"next year will be one of the defining years where there's the next browser war."*(10:54~10:58) 해법은 *"what I want is there to be Linux right for personal AI."*(12:15~12:17)

## 챕터별 요약

### 00:17 에이전트를 운영체제로 · 00:39 Straylight와 작업 기억
- 진행자의 전제: Tan은 에이전트를 기능으로 보는 회사에 투자하지 않는다고 말했다(00:24~00:35). 이 전제는 진행자의 말이다.
- YC 사내 에이전트: *"We now have an internal AI agent, for instance, named Straylight"*(00:56~00:59) 그리고 *"it has a company brain."*(01:04) 범위는 *"every founder we've ever backed, anyone who's ever emailed us, like all the applications."*(01:10~01:14) → [[company-brain]]
- 진행자가 되묻는다: *"that's just data retrieval."*(02:28~02:30)

### 02:20 무엇이 에이전트인가: OpenClaw와 반복 가능성
- 답으로 [[peter-steinberger|Peter Steinberger]]의 [[openclaw|OpenClaw]]를 든다. Claude Code · Codex에 대해: *"they're so worried about sort of repeatability and safety that they actually trade off"*(02:41~02:47) 사람과 일하는 듯한 느낌을 내주고 있다는 평가다. ⚠️ 편집으로 이 답은 03:01에서 끊기고 그 뒤를 내레이션이 잇는다. *무엇이 에이전트인가*의 정의는 끝까지 나오지 않는다.

### 03:15 맡기는 일과 토큰 비용
- 넘긴 데이터: *"it's read all of my email and all of my Dropbox."*(03:19~03:21) Apple 메모, 그리고 *"even my therapy notes going back 20 years."*(03:26~03:28) → [[confidential-vm]]
- 예: 대담 직전 15분 사이에 진행자의 팟캐스트를 받아 정리했다. *"download and transcribe your your top ten podcasts"*(03:40~03:42)
- 앞으로의 모습: *"think of it as a Jiminy Cricket on your shoulder at all times."*(04:13~04:15) 먼저 나서서 *"it'll help you see around corners."*(04:26) → [[personal-agent-four-forces]]
- ⭐ 비용: *"I spend about maybe a hundred to two hundred thousand dollars a year on tokens."*(04:37~04:41) 스스로 *"a crazy privilege"*(04:41~04:43)라 부른다. *"a lot of like CEOs that I know um are doing it and they have wings."*(04:46~04:51)

### 05:01 일자리 · 05:45 gstack · 06:32 재교육과 바닥 · 천장
- 처음엔 불확실성을 말한다: *"My hope I mean, I don't know for certain"*(05:14) 규제 쪽은 기술을 막지 말고 *"going after the abuses"*(05:37)여야 한다는 입장이다.
- [[gstack|gstack]]: *"my open source project G Stack is literally uh working backwards from"*(05:59~06:04) YC 창업자들이 *"get 400 times the amount of output that they had before"*(06:07~06:10) 내도록 가르치려는 것이다. *"just drop into Claude code and get exactly the stack that I used to get that."*(06:14~06:19)
- 실직도 인정한다: *"there will be people who lose their jobs"*(06:39~06:42) *"there's a big retraining issue here"*(06:49~06:50)
- 처방은 분야 전문가(예: *"a medical dealer"*(07:02), `en` `medical biller`)가 *"pair up with a 22 year old"*(07:09~07:11)하거나 직접 배워 창업하는 것이다. 요구 조건은 *"an increase in the amount of agency."*(07:40) 질문은 *"what do you uniquely know"*(07:47)이고 결론은 *"raising the floor and then on the flip side like the ceiling is sky high."*(08:04~08:06) → [[ai-jobs-impact]]

### 08:25 개인 AI가 소셜 미디어를 바꾼다면
- *"You don't download the Facebook app or the Instagram app."*(08:56~09:01) 플랫폼은 *"that's just an API"*(09:01~09:03)이고 피드는 *"your own cognitive filter."*(09:09)를 거친다. *"put control of what goes in your brain back into your own hands"*(09:26~09:29) → [[personal-ai-platform-war]] · [[agent-attention-management]]
- 진행자의 반론: *"the algorithms have a business model that works best when they enrage or divide us."*(10:22~10:28) 답: *"the business model is uh hosted by someone else, by a big tech company"*(10:31~10:34) ⚠️ 개인 AI 쪽의 수익 구조는 말하지 않는다.

### 10:16 다음 브라우저 전쟁과 다섯 왕 · 11:56 개인 AI를 위한 Linux
- *"there will probably be a Mac. There will probably be a PC."*(11:07~11:09) 진행자: *"it'll consolidate to just two or three? Wouldn't that be pretty horrible?"*(11:13~11:19) 답: *"I think we're already there."*(11:20)
- *"our friends inside some of the uh AI labs talk about uh the Five Kings"*(11:24~11:26) 상업 활동 전부가 *"could potentially collapse into Five Kings."*(11:36~11:38) 다섯이 누구인지는 말하지 않는다.
- 조건: *"easy enough to use and cheap enough to use that everyone uses it"*(12:22~12:26) → [[personal-ai-platform-war]]

## 등장 개체

- 인물: [[garry-tan]] · [[peter-steinberger]] · Steve Jobs(언급 수준) · [[tech-bridge]]
- 조직: Y Combinator · [[meta]] · [[anthropic]] · [[openai]] · IBM(언급 수준)
- 제품: [[gstack]] · [[openclaw]] · [[claude-code]] · [[codex]] · Straylight(YC 사내, [[garry-tan]]에 기록) · Gemini · Dropbox · Facebook · Instagram(언급 수준)
- 개념: [[personal-ai-platform-war]] · [[personal-superintelligence]] · [[personal-agent-four-forces]] · [[agent-attention-management]] · [[company-brain]] · [[ai-jobs-impact]] · [[confidential-vm]] · [[lethal-trifecta]]

## 이 위키에서의 좌표

- **데이터 경계에서 어제 소스와 정반대다.** [[tech-bridge-sandeep-swadia-personal-ai-agent|Swadia]]는 건강 · 금융 정보를 주지 않는다고 했고, Tan은 20년치 상담 기록까지 읽혔다. Tan은 보안 모델을 언급하지 않는다. → [[confidential-vm]] · [[lethal-trifecta]]
- **[[personal-superintelligence]]와 같은 낱말을 반대쪽에서 쓴다.** Meta는 개인 초지능을 판매하는 쪽이고, Tan은 그런 회사의 알고리즘을 벗어날 수단으로 개인 AI를 말한다. *개인*이 누구의 플랫폼에서 도는지가 쟁점이다(위키의 읽기).
- **[[gstack]]은 이 위키에 [[pstack|Pstack]]의 놀림 대상으로 먼저 나왔다.** 제작자의 설명은 이 영상이 처음이다.

## ⚠️ 유보

- 발췌 편집본이다. 진행자 이름 · 원본 대담 · 녹화일이 설명란에 없다. *next year*는 녹화 연도 기준이라 언제인지 정할 수 없다. 앞뒤 맥락도 잘렸다.
- *seven plus or minus three*는 화자의 표현이다. *"a thousand pages"*(01:36)와 Harry Potter 세 권의 분량 비교도 확인하지 않았다.
- 토큰 비용 · 400배 · *CEO들도 쓴다*는 모두 화자 진술이고 내역이 없다. gstack 저장소를 열지 않았다.
- Straylight의 실제 권한 · 지원자 데이터 처리 방식은 말하지 않는다.
- 트랙: en-orig 06:19~06:33은 무캡션이다. *"a medical dealer"*(07:02)는 `en` `medical biller`와 다르며 오디오로 확인하지 않아 정하지 않았다. ASR *"Open Claw"* · *"G Stack"*은 설명란 표기로 읽었다. 내레이션의 *게리타*(12:29) · *게리 탄*은 같은 사람이다. ko는 400배를 `400점` · `400배의 금액`으로, *therapy notes*를 `치료 기록`으로 옮겨 인용하지 않는다.

## References

- raw: `01.raw/articles/2026-11-06_게리 탄 AI 에이전트는 2년 안에 모든 걸 바꿀 겁니다.md`
- https://www.youtube.com/watch?v=UIMTEGqP3ys
