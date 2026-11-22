---
title: "노트북을 열지 않고 개발하는 회사 | Walden Yan"
type: video
source: https://www.youtube.com/watch?v=VdX9fccu72E
site: youtube.com
author:
  - "[[Tech Bridge]]"
duration: 10:32
published: 2026-11-21
created: 2026-11-22
description: "Tech Bridge 한국어 해설 10:32, 공식 챕터 12, Korean original + 영어 더빙(en-orig의 내레이션 자리는 더빙 ASR — 인용하지 않음). Cognition 공동 창업자 Walden Yan의 AI Engineer Code Summit 발표(11-12)를 슬라이드와 글로 남은 기록에 맞춰 본 해설 — 엔지니어 2.7배 · 머지된 PR 40배, 기본값은 자율주행(소프트웨어 공장), 2~3명 포드, 슬랙에서 끝내는 개발, 에이전트가 혼자 테스트하는 코드베이스(Docker Compose · 매시간 새 가상 머신 · 테스트 스킬), 공장을 고치는 에이전트(세션 1,300여 개 → 테스트 시간 31%), 일감이 아니라 직무, NVIDIA Vera Rubin 추론 튜닝, 안드로이드 앱 44일(PR 1,134개 중 999개 사람 승인 없이 머지 · 메시지 183개), 발표의 정체 Devin Bots. ⚠️ 발표 원음은 세 조각만 캡션에 있고 발췌 자리 열한 곳은 두 트랙 모두 무캡션."
tags:
  - clippings/youtube
---

**Source URL**: https://www.youtube.com/watch?v=VdX9fccu72E
**Channel**: Tech Bridge · **Duration**: 10:32 · **Published**: 2026-11-21

> **게시일.** info.json `upload_date` **`20261121`**, `timestamp` 1795302034(= 2026-11-21 23:00:34 UTC = **2026-11-22 08:00 KST**), `availability`=`public`. 2026-11-22 회차(09:10 KST) 한 시간쯤 전에 올라왔다 — `upload_date`는 UTC 기준이라 하루 앞선다. 파일명에서 `|`는 뺐다.
>
> **오디오 트랙과 자막 — 인용 규칙.** 오디오는 **Korean original(default) + 영어 더빙**(audio language `ko` · `en` · `en-US`), 메타 `language`=`en`. 수동 자막 없음. `ko` = `ko-orig`(파일 동일, `kind=asr&lang=ko&variant=gemini`). `en-orig`(`kind=asr&lang=en&variant=timing-optimized`)는 내레이션 자리에서 **영어 더빙의 ASR** 이다 — 첫 줄부터 내레이션의 영어 번역이고(*"The number of engineers increased 2.7 times."*) 고유명사 · 숫자를 틀린다: *GB 300* → *GB200*(06:52~07:02 세 번 — 해설이 *GB 300* 과 *GB 200* 을 갈라 말한 구분이 사라진다), *데빈 보스[=Devin Bots]* → *Devin Boss*(09:12), *월드냐는 엑스에* → *Waldnia shared the story behind the XA announcement*(09:01). **인용하지 않고 판독 대조용으로만 쓴다.**
> **발표 원음(영어)은 세 조각이 두 트랙에 같은 글자로 잡혔다**: 08:05~08:20(*iOS application pixel for pixel … sends back to them.*) · 08:53~08:59(*it's not a slop application …*) · 10:10(*Uh I think the end message from all* — 끊김). 앞의 두 조각만 인용했다(08:05~08:08의 첫머리는 앞 문장이 잘려 인용하지 않음). ⚠️ 화자 표시는 `>>` 뿐이다 — 발표 발췌 자리라 Walden Yan으로 읽었다. 429 없음(`--sleep-subtitles 8`).
>
> **무캡션 구간(`gaps.py` 4.5초 기준).** ko-orig 열한 곳: 00:55~01:08 · 01:36~01:54 · 01:56~02:05 · 02:26~02:52 · 03:04~03:19 · 03:29~03:41 · 04:14~04:25 · 04:58~05:26 · 05:57~06:15 · 07:50~08:05 · 10:15~10:21 — 합쳐 약 2분 50초, 전부 발표 발췌 자리다(01:54에 `[음악]` 표시만 있다). en-orig 열 곳: 00:55~01:08 · 01:37~02:05 · 02:26~02:52 · 03:03~03:19 · 03:29~03:41 · 04:14~04:25 · 04:58~05:26 · 05:57~06:15 · 07:50~08:05 · 10:14~10:25 — **같은 자리가 빈다.**
> ⚠️ **이 구간들은 내용 미상이다.** 여기에 드는 것: 엔지니어 수에 대한 발표자의 말(00:55~01:08) · *자율주행* 을 설명한 원음(01:36~02:05) · 포드 설명(02:26~02:52) · 슬랙 흐름의 원음(03:04~03:19) · **제목의 *노트북을 열지 않고* 와 아이패드 이야기(04:14~04:25)** · 세션 분석 설명(04:58~05:26) · *직무* 에 대한 원음(05:57~06:15) · 안드로이드 사례 원음의 앞부분(07:50~08:05) · 발표의 맺음말(10:15~10:21). **위키는 이 구간에 대해 인용도 요약도 만들지 않는다** — 내레이션이 앞뒤에서 간추린 말과 설명란의 문장만 적는다.
>
> **ASR 판독(ko-orig → 판독, 괄호는 근거).** *뭐지된*(00:02 · 00:23 · 00:34) → 머지된(08:28 이후는 *머지된* 으로 바로 적힌다 · 더빙 *merged*), *월드 냰 · 월드냐는*(00:27 · 00:50 · 09:01) → Walden Yan(제목 · 설명란), *그 갖고 본 변화*(01:18) → 그가 꼽은 변화(추정 — 더빙 *the changes they made*), *포드*(02:20) → pod(설명란 *포드*), *도커 컴포저 이전*(04:06) → Docker Compose 이전(03:49는 *도커 컴포즈*), *계정 여러 서로*(04:34) → 계정 여럿으로(추정 — 더빙 *multiple accounts*), *슬라이드 돔 예시*(05:35) → 슬라이드 속 예시(추정 — 더빙 *an example from the slide*), *코어 위브*(06:26) → CoreWeave(설명란), *베라 루빈*(06:23) → Vera Rubin(설명란), *프로덕트 매니저처럼 맞는 것*(07:25~07:27) → 맡는 것(추정), *사람이 드린 품*(08:36) → 들인 품, *22날*(08:38) → 22일, *쓰었습니다*(08:34) → 썼습니다, *데빈 보스 발표했습니다*(09:12~09:14) → Devin Bots를 발표했습니다(챕터 제목 · 설명란), *보타나가*(09:14) → 봇 하나가(추정 — 더빙 *an agent leader*), *트리아즈 엔지니어*(09:34) → triage 엔지니어, *러셀 케플러*(09:42) → Russell Kaplan(설명란).
> ⚠️ **판독하지 못한 것.** 안드로이드 앱을 Devin에게 맡긴 엔지니어의 이름과 소속: *보팀의 엔지니어 36*(07:15) · *36이*(07:22 · 07:46) · *3욕은*(09:45) — 더빙 ASR도 *An engineer from the Bo team, 36* · *The 36 who built this bot* 이라 대조가 되지 않는다. **이름을 추정해 적지 않았다.** *안드로이드의 미학에 한 줄을 더했습니다*(09:42~09:44)도 뜻이 통하지 않는데(더빙 *the Android aesthetic*) 판독하지 못해 인용하지 않았다.
>
> ⚠️ **해설이고 2차 전달이다.** 위키는 원본 발표(`U92J5mCDLMc`)도, 설명란의 글 다섯 편(Devin Bots 출시 글 · Walden Yan X · Russell Kaplan X · CoreWeave 발표문 · Cognition 블로그 *Verifying Agentic Development at Scale*)도 열지 않았다. 수치(2.7배 · 40배 · 1,300여 개 · 31% · 27,336 토큰 · 34만 줄 · 1,134개 · 999개 · 183개 · 98.5%)는 내레이션이 슬라이드와 글에서 옮긴 값이고 Devin을 파는 회사의 자기 보고다. 설명란: *"슬라이드와 글로 남은 기록에 맞춰 따라갑니다."*


## 설명란

코그니션의 머지된 PR은 1년 사이 40배가 됐고, 같은 기간 엔지니어는 2.7배 늘었습니다. 코그니션 공동 창업자 월든 얀이 AI Engineer Code Summit에서 무엇을 바꿨는지 설명합니다. PR은 기본으로 에이전트가 끝까지 몰고 가고, 2–3명짜리 포드가 버그 신고부터 QA까지 맡고, 개발은 거의 슬랙 안에서 끝납니다. 에이전트가 직접 테스트할 수 있게 모든 서비스를 로컬에서 띄우고, 그 결과 코드 변경을 테스트하려고 노트북을 열 일이 없어져 아이패드로 개발하는 엔지니어도 생겼다고 합니다. 다음 단계는 에이전트에게 일감이 아니라 직무를 맡기는 것. 새 GPU(Vera Rubin)에서 추론 성능을 튜닝한 사례와, 사람 메시지 183개로 44일 동안 만든 안드로이드 앱 사례를 슬라이드와 글로 남은 기록에 맞춰 따라갑니다. 발표 나흘 뒤 이 발표가 신제품 Devin Bots의 예고편이었다는 것도 밝혀졌습니다.

타임라인
0:00 엔지니어 2.7배, PR 40배
0:27 40배는 무엇의 40배인가
1:23 기본값은 자율주행
2:10 팀을 2–3명 포드로 쪼갰다
2:52 슬랙에서 끝낸다
3:27 에이전트가 혼자 테스트하는 코드베이스 (노트북 대신 아이패드)
4:38 공장을 고치는 에이전트
5:30 일감이 아니라 직무
6:23 사례 1: NVIDIA Vera Rubin
7:09 사례 2: 안드로이드 앱 44일
9:00 발표의 정체: Devin Bots
9:50 처음 그래프로

참고
원본 발표: https://www.youtube.com/watch?v=U92J5mCDLMc
Introducing Devin Bots (2026.11.17): https://devin.ai/blog/introducing-devin-bots
Walden Yan X (2026.11.16): https://x.com/walden_yan/status/2122418892568227873
Russell Kaplan X (2026.11.17): https://x.com/russelljkaplan/status/2122771093920653493
CoreWeave 발표문 (2026.09.30): https://coreweave.com/news/coreweave-delivers-nvidia-vera-rubin-nvl72-performance-at-production-scale-starting-with-cognition
Verifying Agentic Development at Scale (2026.05.29): https://cognition.com/blog/testing-development

#Cognition #Devin #AI에이전트 #코딩에이전트 #소프트웨어공장

> info.json `tags`: AI Engineer · AI 에이전트 · Code Summit · Cognition · Devin · Devin Bots · Vera Rubin · Walden Yan · 개발 생산성 · 데빈 · 소프트웨어 공장 · 안드로이드 · 월든 얀 · 코그니션 · 코딩 에이전트

## 트랜스크립트 — ko-orig (Korean original, ASR variant=gemini — 발표 원음 세 조각(08:05~08:20 · 08:53~08:59 · 10:10)은 영어 그대로 잡혔다)

[00:00] 엔지니어는 2.7배 늘었습니다.
[00:02] 그런데 뭐지된 PR은 40배가
[00:03] 됐습니다.
[00:04] 코딩 에이전트 데빈을 만드는
[00:06] 코그니션이 무대에서 보여준
[00:07] 그래프입니다.
[00:08] 1년 사이 막대가 이렇게 자랐습니다.
[00:10] 엔지니어 한 명이 10배를 해낸다는
[00:12] 뜻입니다.
[00:13] 대체 무엇을 바꿨길래 이렇게
[00:14] 됐을까요?
[00:15] 답은 더 좋은 에이전트가
[00:16] 아니었습니다.
[00:18] 에이전트가 일하기 좋게 조직과 개발
[00:19] 환경을 다시 짰습니다.
[00:21] 끝에는 사람 승인 없이 PR
[00:23] 999개가 뭐지된 앱과 발표 나흘
[00:25] 뒤에 나온 뒷이야기도 있습니다.
[00:27] 발표자는 월드 냰. 코그니션의 공동
[00:30] 창업자이자 최고 제품 책임자로 11월
[00:32] 12일 샌프란시스코 무대에 섰습니다.
[00:34] 파란 막대는 한 달 동안 뭐지된 PR
[00:36] 수입니다. 작년 11월을 1로 놓고
[00:39] 잰 배수입니다.
[00:40] 바닥에 깔린 점선은 연구 개발
[00:42] 인력입니다. 같은 기간 2.7배가
[00:44] 됐습니다.
[00:45] 인원 2.7배는 글로 확인되는 자료가
[00:47] 없습니다. 단서는 하나. 올해 7월
[00:50] 월드 냰은 엔지니어가 70명 남짓이라
[00:52] 다들 놀란다고 썼습니다.
[01:08] 다만 여기서 세는 건 PR
[01:10] 개수입니다. PR 하나의 크기나
[01:11] 가치는 그래프에 나오지 않습니다.
[01:13] 품질이 그대로라는 것도 발표자의
[01:15] 말입니다. 데빈을 파는 회사의
[01:16] 발표라는 점도 감안해야 합니다.
[01:18] 그럼 그 갖고 본 변화를 하나씩
[01:20] 보겠습니다. [음악] 쉬운 거부터
[01:21] 시작해 어려운 쪽으로 갑니다.
[01:23] 첫째는 소프트웨어 공장이라는
[01:25] 생각입니다. 버그 신고가 들어오면
[01:27] 분류부터 구현, 테스트, 리뷰까지
[01:29] 데빈이 합니다. 배포와 장애 대응도
[01:31] 마찬가지입니다. 사람은 판단이 필요할
[01:33] 때만 불러옵니다.
[01:54] >> [음악]
[02:05] >> 설명할 수 있는 일은 결국
[02:06] 에이전트에게 갑니다.
[02:08] 그러면 엔지니어에게는 뭐가 남을까요?
[02:11] 코그니션의 답은 조직도에 있습니다.
[02:13] 예전에는 기획자, 엔지니어, QA와
[02:15] 온콜 담당이 역할별로 나뉘어
[02:17] 있었습니다.
[02:18] 지금은 두 세 명 짜리 작은 팀,
[02:20] 포드로 쪼갰습니다. 결제나 모바일
[02:22] 앱처럼 제품 한 조각을 통째로
[02:24] 맡습니다.
[02:52] 일하는 것도 바뀌었습니다. 고객이
[02:54] 슬랙으로 버그 영상을 보내면 그대로
[02:56] 사례 채널에 넘기고 데빈을 부릅니다.
[02:58] 데빈은 PR을 올리고 고친 화면을
[03:00] 녹화한 영상을 증거로 같이 보냅니다.
[03:19] IDE도, 깃허브도 열지 않고 개발
[03:22] 한 바퀴를 도는 것. 그는 이걸
[03:23] 도착점으로 꼽았습니다.
[03:25] 문제는 거기까지 가는 길입니다.
[03:41] 예전에는 클라우드의 스테이징 서버와
[03:43] 데이터베이스에 붙어서 테스트했고,
[03:45] 마지막엔 엔지니어가 직접 화면을
[03:46] 눌러봤습니다.
[03:48] 지금은 모든 서비스를 도커 컴포즈로
[03:49] 띄우고 외부 서비스는 흉내낸 가짜로
[03:51] 바꾸고 가상 머신 하나 안에서
[03:53] 돌립니다.
[03:54] 가상 머신은 매 시간 새로 만듭니다.
[03:56] 최신 코드를 받아 처음부터 빌드하고
[03:58] 빌드가 깨지면 데빈이 먼저 고칩니다.
[04:00] 테스트하는 방법도 데빈이 스크립트
[04:02] 파일로 직접 적어둡니다. 코드가
[04:03] 바뀌면 그 스킬도 데빈이 고칩니다.
[04:06] 도커 컴포저 이전이나 매시간 재빌드는
[04:08] 발표에서만 나온 이야기입니다.
[04:10] 테스트 스킬은 코그니션이 5월에
[04:11] 블로그에도 적어 두었습니다.
[04:25] 아이패드가 더 안전하다는 말도
[04:26] 덧붙였습니다. [음악] 비밀 키가
[04:28] 개발자 노트북 여기저기 흩어져 있지
[04:29] 않으니까요.
[04:31] 여러 사람이 함께 쓰는 기능도 이렇게
[04:32] 시험합니다. 데빈은 가상 머신
[04:34] 하나에서 계정 여러 서로 같은 줌
[04:36] 통화에 들어가 음성을 주고받았습니다.
[04:39] 다음은 공장이 스스로 나아지게 하는
[04:41] 단계입니다.
[04:42] 클라우드에서 돌린 세션은 코드 한 줄
[04:43] 결정 하나까지 기록에 남습니다.
[04:46] 그 기록 위에 다시 에이전트를
[04:47] 돌립니다. 슬라이드의 예에서는 지난
[04:49] 세션 1,300여 개를 분석했습니다.
[04:51] 테스트할 때마다 되풀이되던 로그인을
[04:53] 스킬로 저장해 테스트 시간을 31%
[04:55] 줄였습니다.
[05:26] 에이전트가 일을 하고 다른 에이전트가
[05:28] 그 일하는 방식을 고칩니다.
[05:30] 그가 다음 단계로 꼽은 건 이겁니다.
[05:32] 에이전트에게 일감이 아니라 직무를
[05:34] 준다.
[05:35] 슬라이드 돔 예시입니다. 사람은
[05:37] 원하는 것만 말합니다. 우리 API에
[05:39] P99 응답 시간을 빠르게 해 줘.
[05:41] [음악] 그러면 데빈이 목표를
[05:43] 정합니다. 지금 840 밀리초를
[05:45] 500 밀리초로
[05:46] 코드를 훑어 이슈 14개를 만들고
[05:48] 경보와 주간 보고를 겁니다.
[05:50] 그리고 아침마다 휴대폰으로
[05:51] 보고합니다. P99가 65% 줄었고
[05:54] 망가진 건 없다고.
[06:15] >> 숫자 하나로 줄일 수 있는 일이면
[06:17] 에이전트를 붙여 24시간 그 숫자를
[06:19] 밀게 하라는 겁니다.
[06:20] 그는 이걸 실제로 해본 사례 두 개를
[06:22] 보여줬습니다.
[06:23] 첫째는 엔비디아의 새 GPU 베라
[06:25] 루빈입니다.
[06:26] 코어 위브 발표문에 따르면 코그니션은
[06:28] 이 칩으로 실제 서비스를 돌린 첫
[06:30] 고객이었습니다.
[06:32] 받았을 때는 이 칩에 맞춘 커널이
[06:33] 아직 없어서 추론 환경을 처음부터
[06:35] 만들어야 했습니다.
[06:37] GPU 묶음을 따로 떼어 에이전트에게
[06:38] 맡기고 목표 하나만 줬습니다. GPU
[06:41] 하나가 1분에 내는 토큰 수를 끝까지
[06:43] 올려라.
[06:44] 9월 중순부터 일주일 남짓 에이전트가
[06:46] 찾은 방법이 아홉 단계로 쌓였습니다.
[06:48] [음악] 잘 먹힌 방법은 사람
[06:50] 엔지니어가 마지막에 확인했습니다.
[06:52] 출발점은 이전 세대 칩 GB 300의
[06:54] 최고 기록보다 낮았습니다. [음악]
[06:56] 끝에는 27,336 토큰.
[06:58] GB 300 최고치를 훌쩍
[07:00] 넘었습니다.
[07:01] 다만 GB 300과의 비교와
[07:02] 에이전트의 일주일은 이 슬라이드에만
[07:04] 있습니다. 글로 남은 비교는 GB
[07:06] 200 대비 최대 4.8배입니다.
[07:09] 둘째는 안드로이드 앱입니다.
[07:11] 코그니션은 엔지니어링 팀이 작아서
[07:13] 안드로이드 앱까지 맡을 사람이
[07:14] 없었습니다.
[07:15] 보팀의 엔지니어 36이 아이디어를
[07:17] 냈습니다.
[07:18] iOS 앱이 이미 있으니 그걸 설계도
[07:19] 삼아 데빈에게 안드로이드 앱을 맞춰
[07:21] 가게 하자.
[07:22] 9월 28일 36이 데빈에게 보낸 첫
[07:24] 지시입니다.
[07:25] 네 일은 안드로이드 앱을 프로덕트
[07:27] 매니저처럼 맞는 것. 앱 전체를 네가
[07:29] 알아서 만들게 된다.
[07:31] 데빈은 iOS 쪽 변경을 지켜보고
[07:33] 사용자 피드백이 올라오는 슬랙 채널을
[07:34] 듣고 [음악] 직접 QA까지
[07:36] 했습니다.
[07:37] 발표 화면의 타임랩스입니다. 5일째
[07:39] 누적 PR 154개, 17일째
[07:41] 469개, 29일째 887개,
[07:44] 41일째 1,118개. 그 사이
[07:46] 36이 보낸 메시지는 거의 없습니다.
[08:05] >> iOS application
[08:06] pixel for pixel, uh
[08:08] testing whether
[08:09] you know escalating
[08:10] only the most
[08:10] important decisions
[08:11] to a human at the
[08:12] end of the day.
[08:15] And most of the time
[08:16] our engineers don't
[08:17] even need to look
[08:17] open dev and they're
[08:18] just from Slack
[08:18] looking at the
[08:19] recordings that it
[08:20] sends back to them.
[08:21] >> 발표에서는 하루 4, 50개라고
[08:23] 했지만 44일 평균으로 치면 하루
[08:25] 26개 꼴입니다.
[08:26] 44일 뒤에 결과입니다. 코틀린
[08:28] 34만 줄, 머지된 PR
[08:30] 1,134개, 스크린샷 테스트
[08:31] 2,800여 [음악] 개,
[08:33] 커밋의 98.5%를 데빈이
[08:34] 쓰었습니다.
[08:36] 사람이 드린 품은 메시지
[08:37] 183개입니다.
[08:38] 44일 중 22날 딱 절반은 한 통도
[08:41] 보내지 않았습니다.
[08:42] 슬라이드의 표현으로는 메시지 하나에
[08:44] PR 여섯 개가 머지되었습니다.
[08:46] 그리고 1,134개 중 999개는
[08:48] 사람의 승인 없이 머지되었습니다.
[08:50] 앱은 지금 구글 플레이에서 공개
[08:51] 테스트 중입니다.
[08:53] >> And it's not a it's
[08:54] not a slop
[08:55] application. Uh this
[08:56] is actually
[08:56] something that we
[08:58] will be going live
[08:59] with very soon.
[09:01] >> 발표 나흘 뒤 월드냐는 엑스에 이
[09:03] [음악] 발표의 뒷이야기를 이렇게
[09:04] 털어놓았습니다.
[09:05] 그때는 말할 수 없었지만 사실 아직
[09:07] 내놓지 않은 신제품의 예고편이었다.
[09:08] [음악] 목표 하나로 PR
[09:10] 1,000개 넘게 머지했다는 말도
[09:11] 붙였습니다.
[09:12] 다음 날 코그니션은 데빈 보스
[09:14] 발표했습니다. 보타나가 에이전트 팀을
[09:16] 이끌고 일을 끝까지 해낸다는
[09:17] 제품입니다.
[09:18] 출시 글의 부제는 일감에서 결과로.
[09:21] 일감은 바꿀 내용을 말하고 책임은
[09:23] 결과를 말한다고 적었습니다.
[09:25] 예시도 그 안드로이드 앱입니다. 이
[09:26] 기능을 옮겨라가 아니라 안드로이드를
[09:28] iOS와 똑같이 유지하라.
[09:30] 발표 슬라이드를 다시 보면 휴대폰
[09:32] 화면에 이미 봇 목록이 떠
[09:33] 있었습니다.
[09:34] 트리아즈 엔지니어, QA 엔지니어,
[09:36] 안드로이드 엔지니어.
[09:38] 일감이 아니라 직무를 준다는 말이 이
[09:40] 제품의 설명이었다는 셈입니다.
[09:42] 코그니션의 러셀 케플러는 안드로이드의
[09:44] 미학에 한 줄을 더했습니다.
[09:45] 이 봇을 만든 3욕은 안드로이드 앱을
[09:47] 만들어본 적도 코틀린을 써본 적도
[09:49] 없다고요.
[09:51] 처음 그래프로 돌아가 보겠습니다.
[09:53] 엔지니어 2.7배, PR 40배.
[09:55] 그가 바꾼 건 셋입니다. 사람의
[09:57] 역할, 에이전트가 혼자 시험해 볼 수
[09:58] 있는 환경, 그리고 일감 대신 목표를
[10:00] 맡기는 방식.
[10:02] 물론 따져 볼 것도 남습니다. PR
[10:03] 개수는 일의 양이지 가치가 아닙니다.
[10:05] [음악] 사람 승인 없는 머지가
[10:07] 어디까지 안전한지도 이 발표에는
[10:08] 나오지 않았습니다.
[10:10] >> Uh I think the end
[10:12] message from all
[10:21] >> [음악]
[10:25] >> 여러분의 팀은 지금 무엇에 막혀
[10:26] 있나요? 모델인가요 아니면 에이전트가
[10:29] 혼자 시험해 볼 수 없는 환경인가요?

## 트랜스크립트 — en-orig (내레이션 자리는 영어 더빙 ASR — 인용하지 않음, 판독 대조용(발표 원음 세 조각은 ko-orig와 같은 글자))

[00:00] The number of engineers increased 2.7
[00:01] times. But the number of merged PRs grew
[00:03] 40 times.
[00:04] This is a graph shown on stage by
[00:06] Cognition, the creator of the coding
[00:07] agent Devin.
[00:08] The bars grew like this over a year.
[00:10] It means one engineer is accomplishing
[00:11] 10 times more.
[00:13] What on earth did they change to make
[00:14] this happen?
[00:15] The answer wasn't a better agent.
[00:17] They restructured the organization and
[00:19] development environment to help agents
[00:20] work better.
[00:21] At the end, there is an app with 999 PRs
[00:23] merged without human approval and the
[00:24] story that emerged four days after the
[00:26] announcement.
[00:27] The speaker is Walden Yan. As a
[00:29] co-founder and Chief Product Officer of
[00:31] Cognition, he stood on stage in San
[00:32] Francisco on November 12th.
[00:34] The blue bars represent the number of
[00:36] PRs merged per month. It is a multiple
[00:38] measured with last November set as 1.
[00:40] The dotted line at the bottom represents
[00:42] R&D personnel. It increased 2.7 times
[00:43] during the same period.
[00:45] There is no written record confirming
[00:47] the 2.7 x increase in personnel. There
[00:48] is one clue.
[00:49] In July this year, Walden Yan wrote that
[00:51] everyone is surprised that there are
[00:52] only about 70 engineers.
[01:08] However, what we are counting here is
[01:09] the number of PRs. The size or value of
[01:11] a single PR is not shown on the graph.
[01:13] The claim that quality remains the same
[01:14] also comes from the speaker. We must
[01:16] also keep in mind that this is a
[01:17] presentation by a company selling Devin
[01:18] .
[01:18] Now, let's look at the changes they made
[01:20] one by one. We will start with the easy
[01:21] ones and move to the difficult ones.
[01:23] The first is the idea of a software
[01:25] factory. When a bug is reported, Devin
[01:27] handles everything from classification
[01:28] to implementation, testing, and review.
[01:30] Deployment and incident response are the
[01:31] same. Humans are called in only when
[01:34] judgment is required.
[02:05] >> Work that can be explained eventually
[02:06] goes to the agent.
[02:08] Then what is left for the engineers?
[02:11] Cognition's answer lies in their
[02:12] organizational chart.
[02:13] In the past, planners, engineers, QA,
[02:15] and on-call staff were divided by role.
[02:18] Now, they are split into small teams of
[02:20] two or three called "pods."
[02:21] They take full ownership of a piece of
[02:22] the product, such as payments or the
[02:24] mobile app.
[02:52] The way they work has also changed. When
[02:54] a customer sends a bug video via Slack,
[02:55] it is forwarded to the case channel and
[02:57] Devin is called.
[02:58] Devin submits a PR and sends a video
[03:00] recording of the fixed screen as
[03:01] evidence.
[03:19] Completing a development cycle without
[03:21] opening an IDE or GitHub. He pointed to
[03:23] this as the destination.
[03:25] The problem is the path to get there.
[03:41] In the past, we tested by connecting to
[03:43] staging servers and databases in the
[03:44] cloud, and engineers manually clicked
[03:46] through the screens at the end.
[03:48] Now, we launch all services with Docker
[03:49] Compose, replace external services with
[03:51] fakes, and run everything within a
[03:52] single virtual machine.
[03:54] The virtual machine is recreated every
[03:56] hour. Devin pulls the latest code,
[03:57] builds it from scratch, and fixes it if
[03:59] the build breaks.
[04:01] Devin also writes the testing methods
[04:02] itself as script files. If the code
[04:04] changes, Devin updates those skills too
[04:05] .
[04:06] Things like Docker Compose migration or
[04:07] hourly rebuilds were just mentioned in
[04:09] the presentation.
[04:10] Cognition also wrote about their testing
[04:11] skills on their blog back in May.
[04:25] They added that iPads are more secure.
[04:27] That’s because secret keys aren't
[04:28] scattered across developers 'laptops.
[04:31] It tests features used by multiple
[04:32] people in this way as well. Devin used
[04:34] multiple accounts on a single virtual
[04:35] machine to join the same Zoom call and
[04:37] exchange audio.
[04:39] The next step is to make the factory
[04:40] improve itself.
[04:42] Sessions run in the cloud are recorded
[04:43] down to every line of code and every
[04:44] decision.
[04:46] Agents are then run again on top of
[04:47] those records.
[04:48] The example in the slide analyzed over
[04:50] 1,300 past sessions.
[04:52] It saved the repetitive login process as
[04:54] a skill, reducing test time by 31%.
[05:26] One agent does the work, and another
[05:27] agent refines how the work is done.
[05:30] This is what he pointed to as the next
[05:31] step. Give agents responsibilities, not
[05:34] just tasks.
[05:35] This is an example from the slide. The
[05:36] human only states what they want. "Make
[05:39] the P99 response time for our API faster
[05:41] ."
[05:42] Then Devin sets a goal. It scans the
[05:44] code to bring the current 840ms down to
[05:46] 500ms, creates 14 issues, and sets up
[05:48] alerts and weekly reports.
[05:50] Then it reports to your phone every
[05:51] morning.
[05:52] "P99 reduced by 65%, and nothing is
[05:55] broken."
[06:15] >> The idea is to assign agents to any job
[06:17] that can be measured by a single number
[06:18] and have them push that metric 24/7.
[06:20] He showed two examples where this was
[06:22] actually done.
[06:23] The first is Nvidia's new GPU, Vera
[06:25] Rubin.
[06:27] According to CoreWeave's announcement,
[06:28] Cognition was the first customer to run
[06:30] a live service on this chip.
[06:32] When they received it, there were no
[06:33] kernels optimized for the chip yet, so
[06:34] they had to build the inference
[06:35] environment from scratch.
[06:37] They isolated a cluster of GPUs,
[06:38] assigned them to an agent, and gave it
[06:40] one goal.
[06:41] "Maximize the number of tokens a single
[06:42] GPU produces per minute."
[06:44] In just over a week starting in
[06:45] mid-September, the agent found a method
[06:47] involving nine steps.
[06:48] A human engineer performed the final
[06:50] check on the methods that worked well.
[06:52] The starting point was lower than the
[06:53] peak record of the previous-generation
[06:55] GB200 chip.
[06:56] By the end, it reached 27,336 tokens.
[06:58] It far exceeded the peak of the GB200.
[07:01] However, the comparison with the GB200
[07:02] and the week-long agent timeline only
[07:04] appear in this slide.
[07:05] The official comparison noted is up to
[07:07] 4.8 times higher than the GB200.
[07:09] The second example is an Android app.
[07:11] Cognition’s engineering team was too
[07:13] small to have anyone take on the Android
[07:14] app.
[07:15] An engineer from the Bo team, 36, came
[07:16] up with an idea.
[07:18] Since we already have an iOS app, let's
[07:19] use it as a blueprint and have Devin
[07:20] build the Android app to match.
[07:22] This was the first instruction sent to
[07:24] Devin by 36 on September 28th.
[07:25] Your job is to build the Android app,
[07:27] just like a product manager would.
[07:28] You'll be responsible for building the
[07:29] entire app yourself.
[07:31] Devin monitored iOS changes, listened to
[07:33] the Slack channel for user feedback, and
[07:35] even handled QA directly.
[07:37] This is a time-lapse from the
[07:38] presentation. By day 5, 154 PRs; day 17
[07:41] , 469; day 29, 887; and by day 41, 1,118
[07:45] PRs. In that time, 36 sent almost no
[07:48] messages.
[08:05] >> iOS application pixel for pixel, uh
[08:07] testing whether you know escalating only
[08:09] the most important decisions to a human
[08:11] at the end of the day.
[08:15] And most of the time our engineers don't
[08:17] even need to look open dev and they're
[08:18] just from Slack looking at the
[08:19] recordings that it sends back to them.
[08:21] >> The presentation claimed 40 to 50 per
[08:23] day, but over the 44-day average, it's
[08:25] about 26 per day.
[08:26] Here is the result after 44 days.
[08:28] 340,000 lines of Kotlin, 1,134 merged
[08:30] PRs, around 2,800 screenshot tests, and
[08:33] Devin wrote 98.5%of the commits.
[08:36] The human effort involved was 183
[08:37] messages.
[08:38] Out of 44 days, for 22 days—exactly half
[08:40] —not a single message was sent.
[08:42] According to the slide, one message
[08:44] resulted in six PRs being merged.
[08:46] And out of the 1,134 PRs, 999 were
[08:48] merged without human approval.
[08:50] The app is currently in open testing on
[08:52] Google Play.
[08:53] >> And it's not a it's not a slop
[08:55] application. Uh this is actually
[08:57] something that we will be going live
[08:59] with very soon.
[09:01] >> Four days after the presentation,
[09:02] Waldnia shared the story behind the XA
[09:03] announcement like this.
[09:05] I couldn't say it then, but it was
[09:06] actually a trailer for a new product we
[09:08] haven't released yet.
[09:09] He added that they merged over 1,000 PRs
[09:11] for a single goal.
[09:12] The next day, Cognition announced Devin
[09:14] Boss.
[09:15] It’s a product where an agent leader
[09:16] manages a team of agents to see a task
[09:17] through to completion.
[09:18] The subtitle of the launch post was "
[09:20] From tasks to outcomes." It stated that
[09:21] tasks describe what to change, while
[09:23] responsibilities describe the outcome.
[09:24] The example used was that same Android
[09:26] app. Instead of "move this feature," it
[09:28] was "keep Android identical to iOS."
[09:31] Looking back at the presentation slides
[09:32] , the list of bots was already visible
[09:33] on the phone screen.
[09:34] Triage engineer, QA engineer, Android
[09:36] engineer.
[09:38] It turns out that "assigning a role, not
[09:39] a task" was the product's description
[09:40] all along.
[09:42] Cognition's Russell Kaplan added a line
[09:44] to the Android aesthetic.
[09:46] The 36 who built this bot had never
[09:47] built an Android app or used Kotlin
[09:49] before.
[09:51] Let's go back to the initial graph. 2.7
[09:53] times the engineers, 40 times the PRs.
[09:55] He changed three things. The role of
[09:57] humans, an environment where agents can
[09:59] test alone, and delegating goals instead
[10:01] of tasks.
[10:02] Of course, there are still things to
[10:03] consider. The number of PRs is the
[10:04] amount of work, not the value. How safe
[10:06] it is to merge without human approval
[10:07] was not covered in this presentation.
[10:10] >> Uh I think the end message from all
[10:25] >> What is holding your team back right now
[10:26] ? Is it the model, or an environment
[10:29] where agents cannot test on their own?
