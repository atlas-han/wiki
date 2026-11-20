---
title: "Tech Bridge — AI로 10배 빨라졌다면, 30년치 발전은 어디 갔나 | Jonathan Blow (한국어 해설): 10배 × 3년 = 30년치, 본 것은 대략 0년 · 엑셀 VBA 30줄 5시간 → 1시간 · 조각 사이의 선과 감으로 가는 AI · 말귀를 알아듣는 검색 · 더 많은 코드는 빚 · 1990년 워크스테이션과 systemd 171만 줄 · 쓰레기 매립지 · 규칙으로 배우는 코딩 AI 구상 · 멈춰서 갚는 시간"
type: source
tags: [jonathan-blow, software-complexity, technical-debt, ai-coding, developer-productivity, vibe-coding, sycophancy, systemd, alphazero, the-students, commentary-format, korean-narration, video]
source-url: https://www.youtube.com/watch?v=oCEJgCOLEIs
source-type: video
author: Tech Bridge (한국어 해설) · 바탕 Jonathan Blow의 The Students 대담 · 2019년 강연 Preventing the Collapse of Civilization · OX Security 글 · Phoronix 기사(모두 위키 미열람)
date-published: 2026-11-19
ingested: 2026-11-20
created: 2026-11-20
updated: 2026-11-20
---

# Tech Bridge — AI로 10배 빨라졌다면, 30년치 발전은 어디 갔나 (Jonathan Blow)

[[tech-bridge|Tech Bridge]]의 **12:10 한국어 해설, 공식 챕터 10.** *Braid* 와 *The Witness* 를 만든 게임 개발자 [[jonathan-blow|Jonathan Blow]]가 The Students 대담에서 던진 물음 — *AI 코딩이 정말 10배 빠르다면 3년 사이 30년치 소프트웨어 발전이 보여야 하는데, 쓰는 사람 눈에는 대략 0년* — 을 대담의 흐름대로 따라간다. raw: `01.raw/articles/2026-11-19_AI로 10배 빨라졌다면 30년치 발전은 어디 갔나 Jonathan Blow.md`.

테제(해설의 맺음):

> *"코드가 빨리 나오는 것과 소프트웨어가 나아지는 것은 다른 일이다."*(12:01~12:03)

> **트랙과 인용.** Korean original + 영어 더빙, `ko` = `ko-orig`(`variant=gemini`). 내레이션 인용은 ko-orig. `en-orig`는 **더빙의 ASR** 이라 내레이션 부분은 인용하지 않았다(판독 대조용).
>
> ⭐ **원 대담 발췌 구간에서는 en-orig에 Blow의 영어 원음이 잡힌다**(ko-orig는 그 구간이 무캡션). 아래 영어 인용은 전부 이 **en-orig에만 잡힌 원음 ASR** 이다 — 두 트랙 교차 확인이 없고, 화자 구분도 캡션에 없다(진행자의 말이 섞였을 수 있다). ASR이 뭉갠 대목은 인용하지 않았다.
>
> ⚠️ **두 트랙 모두 빈 구간의 내용은 적지 않았다** — 챕터 제목의 *다리 비유*(00:49~01:10) · Blow의 *질문 하나* 의 원문(01:30~01:36) · 컴파일러를 고칠 때의 얘기(11:35~11:47).
>
> ⚠️ **수치는 측정값이 아니다.** 설명란: *30년/0년, 5시간/1시간은 측정값이 아니라 Blow의 암산과 추정* 이다. 위키는 설명란의 네 출처를 열지 않았다.

## 1. 3년 만에 30년치, 그런데 0년 (00:00~00:31)

- *"AI 코딩이 정말 10배 빠르다면 나왔어야할 숫자입니다."*(00:02~00:04) — 3년 만에 30년치 발전. 프로그래머가 직접 세어 본 결과가 화면에 나온다(00:08~00:14 무캡션).
- 인물: *"조너선 블로, 브레이드와 더 위트니스를 만든 게임 개발자입니다."*(00:14~00:16)
- *"이 대담은 공개 사흘만에 24만번 가까이 재생됐습니다."*(00:18~00:20) ⚠️ 영어 더빙은 *four days*. 미확인.
- 영상의 물음: *"그럼 AI가 쏟아낸 그 많은 코드는 다 어디로 갔을까요?"*(00:22~00:24)

## 2. Jonathan Blow, 그리고 다리 비유 (00:31~01:18)

- 2019년 모스크바 강연 *문명의 붕괴를 막는 법*(설명란 *Preventing the Collapse of Civilization*): *"소프트웨어가 복잡해질수록 점점 못 믿을 물건이 된다는 내용이었습니다."*(00:35~00:39)
- 이번 대담의 출발점도 같다 — *"엔지니어는 현실의 제약을 이해하고 원하는 결과를 만들어내는 사람이라는 겁니다."*(00:42~00:46)
- ⚠️ 챕터 제목의 **다리 비유**(00:49~01:10)는 두 트랙 모두 무캡션 — 적지 않는다.
- *"버튼 하나를 눌러도 무슨 일이 생길지 모르는 웹페이지."*(01:10~01:11) *"블로가 보기에 소프트웨어는 AI 이전부터 이랬습니다. 그 위에 AI가 올라온 겁니다."*(01:11~01:17)

## 3. 30년은 어떻게 나온 숫자인가 (01:18~03:08)

- 배경: AI가 코드를 대신 써 준다는 얘기가 나온 지 3년쯤, 생산성 주장은 모델이 좋아질수록 늘었다(ASR *모두들 좋아질수록*).
- ⚠️ *"블로의 질문은 하나입니다."*(01:26) — 질문의 원문(01:30~01:36)은 무캡션.
- 암산. Blow 원음(en-orig): *"we should have had 30 years of software advancement."*(01:59~02:02) ⚠️ 바로 앞 *since 2003* 은 ASR — 2023으로 추정, 미확정.
- 해설의 요약: *"10배에 3년이면 30년치. 그런데 블로거가 본 건 대략 0년입니다."*(02:05~02:07)[블로거=블로]
- 후하게 쳤나 싶어 다시 센다 — *"1년 반 전부터 다섯 배만 올랐다고 쳐도 7, 8년치. 그것도 안 보인다고 합니다."*(02:12~02:16)
- ⭐ Blow가 먼저 긋는 선(en-orig 원음): *"So, I don't want people to like clip this and be like"*(02:29~02:31) … *"these AI systems are legitimate fundamental technological advancements"*(02:36~02:39) — 다만 실제 소프트웨어 생산에 적용했을 때는 얘기가 다르다는 쪽으로 이어진다(문장 끝은 ASR 조각).
- 해설: *"AI 기술은 진짜 발전이지만 쓰는 사람 눈에는 소프트웨어가 나아진 게 안 보인다는 겁니다."*(03:00~03:03) ⚠️ *"이건 통계가 아니라 블로거 한 사람의 관찰입니다."*(03:03~03:05)[블로거=블로]

## 4. Blow도 AI를 쓴다: 5시간 → 1시간 (03:08~04:22)

- 일: 프로그램이 뽑은 CSV를 엑셀로 열어 조건에 맞는 칸에 색과 굵은 글씨를 넣는다. *"AI는 30줄 좀 되는 비주얼 베이직 코드를 거의 한 번에 내놨습니다."*(03:17~03:22)
- Blow 원음(en-orig): *"It probably would have taken like 5 hours to do or something."*(03:35~03:36) … 반복한 것까지 쳐서 *"it probably took, uh, one hour or something."*(03:43~03:46)
- ⭐ 본인의 단서(en-orig 원음): *"we're still not talking about like an infinite speedup like people talk about and, and this is a rare case because how often are you learning a new programming language"*(03:47~03:56)
- 해설: *"블로는 사람들이 AI가 코딩을 잘한다고 믿게 되는 이유가 이런 경험이라고 봅니다."*(04:11~04:15)
- 조건 셋 — *"처음 보는 원어였고, 서른 줄이었고,"*(04:18)[원어=언어] *"쓰고 버릴 코드였습니다."*(04:20)

## 5. 30줄과 시스템은 무엇이 다른가 (04:22~05:39)

- Blow는 허공에 점을 찍어 가며 설명한다: *"프로그램 조각이 셋이면 그 사이에 그을 수 있는 선은 셋, 넷이면 여섯입니다."*(04:28~04:31) 조각보다 선이 더 빨리 는다(ASR *듭니다*).
- ⭐ 선의 정체: *"이 선은 코드에 적혀 있지 않습니다. 여기를 이렇게 짜면 저기가 어떻게 되는지 그 영향과 제약이 선입니다."*(04:34~04:38)
- Blow 원음(en-orig): *"so you build out this map of those things in your mind and every time you're trying to do something new, you're like charting your way through there"*(04:59~05:08)
- ⭐ 판정(en-orig 원음): *"they don't seem to actually reason well enough to do that."*(05:14~05:20) — 앞머리는 *"AI don't seem to, to me in 2026"* 로 잡혔다. 끝은 *"going on vibes"*(05:24~05:30, 앞 낱말은 ASR 판독 불가).
- 해설: *"감으로 간다. 블로의 표현입니다."*(05:31) *"서른 줄에서는 티가 안 나다가 프로그램이 어느 크기를 넘으면 드러난다는 겁니다."*(05:34~05:37)

## 6. AI는 "알아듣는 검색" (05:39~06:46)

- *"블로는 요즘 AI를 말귀를 알아듣는 검색 알고리즘으로 생각한답니다."*(05:40~05:45) 아주 큰 탐색을 아주 빠르게 해낸다. 대신 — *"이렇게 짜면 나중에 어떻게 될지를 가리는 판단에는 약하다는 겁니다."*(05:47~05:52)
- 근거로 든 사례는 코드가 아니다: 지난달 새 게임(ASR *셋 게임*)을 내기 전 AI에게 첫 달 판매량을 여러 번 예측시켰다. AI는 이유를 줄줄이 달아 숫자를 냈다 — 올해 GTA가 나온다는 것까지 챙기면서.
- Blow 원음(en-orig, 조각): 자기가 *언급 안 한 이유 하나* 를 들어 더 높아야 하지 않느냐고 하자 — *"Oh, you know what? You're right."*(06:19~06:20) *"Actually, the sales should be higher."*(06:22)
- 해설: *"더 높아야 한다고 해도 맞습니다. 더 낮아야 한다고 해도 맞습니다."*(06:37~06:39) 겉모양은 추론인데(ASR *그래 모양은*, 추정) *"들여다보면 구멍과 건너뛴 자리가 쉽게 보인다는 겁니다."*(06:41~06:45) → [[sycophancy]]

## 7. 더 많은 코드는 빚이다 (06:46~07:58)

- 진행자가 꺼낸 요즘의 주장: *"AI가 만든 기소 부채는 AI가 갚으면 되지 않느냐."*(06:46~06:48)[기소=기술]
- ⭐ Blow 원음(en-orig): *"and the AI will give you a lot more code just like the the mathematical proofs would be a lot longer than if a real mathematician had written the proof."*(07:11~07:20) — 같은 문제를 잘하는 사람 프로그래머와 AI에게 시키면, 이라는 전제 뒤다. *"and then that extra code is all technical debt that you have to"*(07:24~07:27) (문장은 여기서 끊긴다. *10배 더 길 때도* 라는 대목은 ASR이 뭉개 인용하지 않는다.)
- 해설이 옮긴 Blow의 계산(ASR *개선*): 코드가 늘면 줄마다 생기는 오류도 같이 늘고, 어느 선을 넘으면 더는 손을 못 댄다. *"코드를 보지 않는 순수한 바이브 코딩은 그 선에 꽤 빨리 닿는다고 봅니다."*(07:39~07:42)
- 선 전에 끝나는 일도 많다 — *"마사지 숍 홈페이지 같은 건 예전엔 돈을 주고 맡겨도 골치였는데 지금은 훨씬 쉬워졌다고 블로도 인정합니다."*(07:46~07:50)
- 단서: *"다만 그게 AI가 프로그래밍을 잘한다는 뜻은 아니라고 덧붙입니다."*(07:52~07:56)

## 8. 소프트웨어는 원래 쌓이기만 했다 (07:58~09:35)

- 진행자의 가설: *"생산성은 정말 올랐는데 소프트웨어 산업이 그걸 블랙홀처럼 삼키는 건 아니냐고요."*(08:00~08:04)
- Blow의 답은 대학 시절 — *"1990년 그가 쓰던 유닉스 워크스테이션들은 메모리를 보호하고 화면에 창을 띄우고 마우스로 눌렀습니다."*(08:07~08:13) (원음은 *"1990 now 2026 36 years later."*(08:16~08:18) 뒤로 조각.)
- *"하는 일은 같은데 코드는 비교가 안 되게 들었습니다."*(08:35~08:36)[들었습니다=늘었습니다, 추정]
- 예: systemd. 초기 유닉스에서 부팅 때 할 일은 스크립트 대여섯 줄에서 열 줄이었다고 한다(Blow의 말, 해설 전달). 지금은 — *"포로닉스가 2022년 말 해성 저장소 기준으로 약 171만 줄입니다."*(08:47~08:51)[포로닉스=Phoronix] ⚠️ 이 수치는 Blow가 아니라 해설이 설명란의 Phoronix 기사에서 붙인 것이다.
- Blow가 화면에 띄워 달라고 한 그림: 위키백과의 리눅스 배포판 계보. *"블로는 이들이 하는 일이 대부분 겹친다고 말합니다."*(08:59~09:01)
- 사고: *"이번 달 5일 알파인 리눅스에서 아주 긴 비밀번호를 넣으면 로그인이 뚫리는 버그가 공개됐습니다."*(09:05~09:09) Blow가 대담에서 가장 황당한 사례로 꼽았다. 보안 업체 OX Security(ASR *옥스*)의 분석으로는 *"10년 넘는 기간에 따로 내려진 결정 세 개가 겹친 결과였습니다."*(09:13~09:17) *"하나하나는 다 이유가 있었습니다."*(09:19) (설명란: *OpenSSH 인증 우회 CVE-2026-123158*. ⚠️ 내레이션은 CVE 번호도 OpenSSH도 말하지 않는다.)
- ⭐ *"블로의 표현으로 우리는 거대한 쓰레기 매립지 위에 삽니다."*(09:21~09:23) 층은 계속 쌓이고 바닥까지 파 내려가기는 어렵다.
- 전망: AI가 소프트웨어 품질을 올릴 수도 있지만 *"반대로 갈 가능성이 더 크다는 게 블로의 전망입니다."*(09:30~09:32)

## 9. 그럼 영영 안 되나: Blow의 대안 (09:35~11:15)

- 영영 안 된다고 보지는 않는다. *추론 흉내를 계속 잘 내다 보면 진짜 추론과 같아진다* 는 주장에 — *"그는 가능성을 절반 아래로 봅니다."*(09:42~09:45) 0은 아니다.
- *"말한 대로 되는 코딩 AI를 만들면 아마 세계에서 가장 값진 회사가 될 것이라며 자기라면 이렇게 만들겠다고 합니다."*(09:47~09:52)
- Blow 원음(en-orig): *"Go back like 10 or more years in AI history, uh, to, um, Alpha Zero"*(09:59~10:02) … *"did to play Go in some other games without being taught the rules."*(10:08~10:10) 다른 종류의 시스템이었던 까닭 — 거의 전적으로 자기 경험으로 훈련됐고, *"just on rules and the operation of rules , which is what a program is."*(10:26~10:29) (⚠️ 이 줄은 *Yeah. Well, and also* 로 시작한다 — 진행자의 말일 수 있다.) *"in the end it doesn't make that much of a difference, but my suspicion is it does."*(10:34~10:38)
- 해설의 정리: *"사람과의 대화는 LLM에 맡기는 구조입니다."*(10:51~10:53) 코드는 규칙으로 배우는 쪽에 둔다. 둘을 잇는 방법은 — *"블로도 어떻게든이라고 말했습니다. 구상할 뿐 만든 건 아닙니다."*(10:55~10:59)
- ⚠️ **해설의 정정**: Blow는 *규칙을 배우지 않고* 라고 말했으나, 해설은 *"참고로 알파제로는 규칙은 받고 사람의 기부 없이 혼자 두면서 배운 시스템입니다."*(11:02~11:05)[기부=기보] 라고 바로잡는다(설명란도 *부정확한 대목(AlphaZero)은 영상 안에서 바로잡았습니다*). *10년 넘게 전* 이라는 연도는 해설이 건드리지 않았다.
- 지금 당장 쓸모 있다고 본 것: AI로 버그를 훑는 일. *"린터나 퍼저처럼 프로그램을 곁에 두는 도구로는 분명히 유용하다고 했습니다."*(11:08~11:12)

## 10. 다시 30년과 0년 (11:15~12:10)

- 30년치가 안 보이는 까닭을 해설이 이으면: *"AI는 같은 문제에 코드를 더 많이 내고 그 코드는 비즈로 남고 소프트웨어는 원래부터 쌓이기만 해 왔습니다."*(11:20~11:26)[비즈로=빚으로]
- Blow 자신은 — *"가끔 멈춥니다. 본인의 컴파일러를 고칠 때의 얘기입니다."*(11:29~11:31) ⚠️ 그 얘기(11:35~11:47)는 무캡션.
- 해설이 꼽은 가져갈 것 셋: (1) 서른 줄짜리 쓰고 버릴 코드(ASR *스코버를 코드*)에는 AI를 마음껏 쓴다, (2) *"오래 살 시스템이라면 조각 사이에 선을 그린 지도는 사람이 주고 있습니다."*(11:52~11:55)[주고=쥐고, 추정], (3) *"그리고 코드가 늘어난 만큼 멈춰서 갚는 시간을 따로 잡습니다."*(11:56~11:58)

## 위키의 읽기

- ⭐ **생산성 주장에 대한 바깥쪽 검산.** 위키가 모은 반론은 지금까지 *안쪽* 측정이었다 — [[perceived-vs-actual-productivity]]의 METR(느려졌는데 빨라졌다고 느낀다) · DX 집계. Blow의 물음은 방향이 다르다: 개발자가 아니라 **소프트웨어를 쓰는 사람 눈에** 30년치(혹은 5배 × 1년 반 = 7, 8년치)가 보이느냐. ⚠️ 측정이 아니라 한 사람의 관찰이고(해설 · 설명란이 모두 그렇게 표시), *소프트웨어 발전 몇 년치* 는 단위가 정의되지 않은 수사다.
- ⭐ **Blow 자신의 5배.** 5시간 → 1시간은 그가 내세운 반증이 아니라 **조건을 밝히는 사례** 다 — 처음 보는 언어 · 서른 줄 · 쓰고 버릴 코드. [[disposable-vs-durable-software]]의 스펙트럼에서 일회용 끝에 놓인 일이고, 11-18 Karpathy 편의 *크고 버려도 되는 소프트웨어를 마음껏 주문하라* 와 같은 자리를 훨씬 좁게 그린다(Karpathy는 앱 하나, Blow는 30줄).
- ⭐ **조각 사이의 선.** *선은 코드에 적혀 있지 않다 — 영향과 제약이 선이다* 는 [[cognitive-debt]]가 *코드를 소유하는 사람의 이해* 라 부른 것의 다른 그림이다. 조각 n개에 선 n(n−1)/2개라는 산수(셋 → 셋, 넷 → 여섯)가 *서른 줄에서는 티가 안 난다* 의 근거다. 해설의 둘째 권고(*지도는 사람이 쥔다*)는 [[verification-bottleneck]] 계열 소스들이 *검증* 쪽에서 말한 것을 *설계* 쪽에서 말한다(위키의 연결).
- **[[technical-debt]]에 양의 축이 붙는다.** 그 페이지는 부채를 *미룬 구조 개선* 으로 정의한다. Blow는 **같은 문제에 대한 코드의 양 자체** 를 부채로 센다 — 수학 증명이 진짜 수학자가 쓴 것보다 길어지는 것에 견준다. *AI가 만든 부채는 AI가 갚는다* 는 주장에 대한 답은 *갚을 것이 더 빨리 는다* 다.
- ↔ **11-16 Lauren Tan 편과 나란히.** [[tech-bridge-lauren-tan-all-code-is-slop]]은 *한 달 PR 1만 개, 되돌림은 줄었다* 를 검증 층으로 설명했다. Blow의 *어느 선을 넘으면 손을 못 댄다* 와 정면으로 부딪치는 것은 아니다 — Blow가 그 선에 *꽤 빨리 닿는다* 고 한 것은 **코드를 보지 않는 순수한 바이브 코딩** 이고, Tan 쪽은 검증에 투자한 팀이다. 다만 Blow의 일반 명제(AI는 추론이 아니라 감으로 간다 · 품질은 내려갈 가능성이 더 크다)는 위키의 다수 소스(에이전트 중심 팀의 성과 보고)와 방향이 반대다. 양쪽 다 자기 보고이고 위키는 어느 쪽도 측정으로 확인하지 못했다.
- **[[sycophancy]]의 사례.** 판매량 예측 — 더 높아야 한다 해도 *맞다*, 더 낮아야 한다 해도 *맞다*. Blow는 이것을 아첨이 아니라 **추론의 부재** 의 증거로 쓴다(겉모양은 추론인데 구멍과 건너뛴 자리). ⚠️ 어느 모델인지, 몇 번 시켰는지는 말하지 않는다.
- **인정한 쓸모 둘.** 선 전에 끝나는 일(마사지 숍 홈페이지) · 버그 훑기(린터 · 퍼저처럼). 뒤쪽은 [[ai-vulnerability-discovery]]가 모아 온 벤더 쪽 주장과 같은 방향이다 — 회의적인 화자가 인정한 용도라는 점만 적어 둔다.
- ⚠️ **AlphaZero 대목.** 원음은 *규칙을 배우지 않고*, 해설의 정정은 *규칙은 받고 기보 없이* 다. 위키는 정정을 따른다. Blow의 구상(코드는 규칙으로 배우는 쪽 · 대화는 LLM)은 구상일 뿐이고 잇는 방법은 *어떻게든* 이다.
- ⚠️ **Alpine Linux 버그.** 날짜(이번 달 5일) · 원인(10년 넘게 따로 내려진 결정 셋)은 해설이 OX Security 글에서 옮긴 것이고 위키는 열지 않았다. 설명란 제목은 *OpenSSH 인증 우회* 인데 내레이션은 *알파인 리눅스 로그인* 이라고만 한다 — 둘의 관계는 캡션으로 확인되지 않는다.
- ⚠️ **빠진 것.** 다리 비유 · 질문의 원문 · 컴파일러 얘기는 두 트랙 모두 무캡션이다. 대담 진행자의 이름은 나오지 않는다. 새 게임의 이름도 나오지 않는다.
- 페이지화하지 않음: The Students(대담 채널) · *Braid* · *The Witness* · *Preventing the Collapse of Civilization* · systemd · Phoronix · OX Security · Alpine Linux · AlphaZero · GTA · 바이브 코딩(독립 페이지 없음).

## 등장 개체

- 인물: [[jonathan-blow]](신규) · 대담 진행자(이름 미상)
- 조직 · 자료 · 제품: The Students · Phoronix · OX Security · DeepMind(원음 *Deep Mind*, → [[google-deepmind]]) · AlphaZero · systemd · Alpine Linux · 위키백과 리눅스 배포판 계보 · Excel · Visual Basic(페이지화하지 않음)
- 개념: [[technical-debt]] · [[perceived-vs-actual-productivity]] · [[disposable-vs-durable-software]] · [[sycophancy]] · [[cognitive-debt]] · [[verification-bottleneck]] · [[ai-vulnerability-discovery]]

## References

- 영상: https://www.youtube.com/watch?v=oCEJgCOLEIs
- raw: `01.raw/articles/2026-11-19_AI로 10배 빨라졌다면 30년치 발전은 어디 갔나 Jonathan Blow.md`
- 앞선 관련 소스: [[tech-bridge-lauren-tan-all-code-is-slop]] · [[tech-bridge-karpathy-hackertube-two-hours-five-words]] · [[tech-bridge-kanat-alexander-disposable-vs-durable]] · [[tech-bridge-dx-ai-impact-trends]]
- 설명란 참고(위키 미열람): 원본 대담(The Students) https://www.youtube.com/watch?v=IRK8h67ol7Q · 2019년 강연 *Preventing the Collapse of Civilization* https://www.youtube.com/watch?v=pW-SOdj4Kkk · OX Security, OpenSSH 인증 우회 CVE-2026-123158 https://www.ox.security/blog/openssh-authentication-bypass-cve-2026-123158/ · Phoronix, systemd 저장소 통계(2022) https://www.phoronix.com/news/systemd-Git-Stats-2022
