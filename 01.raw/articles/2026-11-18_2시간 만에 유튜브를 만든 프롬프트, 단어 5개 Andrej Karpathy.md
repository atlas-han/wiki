---
title: "2시간 만에 유튜브를 만든 프롬프트, 단어 5개 | Andrej Karpathy"
type: video
source: https://www.youtube.com/watch?v=OV9By_UspTk
site: youtube.com
author:
  - "[[Tech Bridge]]"
duration: 10:19
published: 2026-11-18
created: 2026-11-19
description: "Tech Bridge 한국어 해설 10:19, 공식 챕터 9, Korean original + 영어 더빙(en-orig는 더빙의 ASR). Andrej Karpathy가 토요일 아침 2시간 만에 만든 HackerTube(Hacker News 20년 치 댓글에서 고른 영상 6,454개)를 그의 블로그 · X · Hacker News 댓글 · 강연 기록으로 따라간다 — 0.2% 냅킨 계산, 2시간의 순서와 토큰 양, 짧고 멍청한 프롬프트, 이해의 사다리, 루프에서 빠지기, 스킬 위약 대조, 코드 대신 데이터 공개."
tags:
  - clippings/youtube
---

**Source URL**: https://www.youtube.com/watch?v=OV9By_UspTk
**Channel**: Tech Bridge · **Duration**: 10:19 · **Published**: 2026-11-18

> **게시일 — 멤버 전용에서 공개로.** 2026-11-17 회차에서 목록 줄로 처음 보였을 때는 `upload_date` `20261116` · `availability`=`subscriber_only`(멤버 전용)였고 11-18 회차에도 그대로였다. **2026-11-19 회차에서 `public` 전환 확인.** info.json `upload_date`는 **`20261118`** 로 바뀌어 있었다 — `timestamp` 1795006824(= 2026-11-18 13:00:24 UTC = **2026-11-18 22:00 KST**). 공개 전환 시점 쪽으로 날짜가 옮겨 가는 앞선 사례들과 같은 패턴이다. 제목은 그대로. 파일명에서 `|`는 뺐다.
>
> **오디오 트랙과 자막 — 인용 규칙.** 오디오는 **Korean original(default) + 영어 더빙**(audio language `ko` · `en` · `en-US`), 메타 `language`=`en`. 수동 자막 없음. `ko` = `ko-orig`(md5 동일, `kind=asr&lang=ko&variant=gemini`). ⚠️ **`en-orig`(`kind=asr&lang=en&variant=timing-optimized`)는 Karpathy의 음성이 아니라 영어 더빙 트랙의 ASR이다** — 첫 줄부터 내레이션과 같은 내용이 영어로 나온다(*"Friday, 11 PM. A weary developer opened YouTube"*). → **인용은 ko-orig 하나.** en-orig는 ASR 판독의 대조용으로만 쓰고 아래에 싣되 인용하지 않는다(더빙이 ko 캡션에서 만들어진다면 독립된 확인이 아니다 — 추정). 429 없음(`--sleep-subtitles 8`).
>
> **무캡션 구간(`gaps.py` 4.5초 기준, 두 트랙 공통).** 02:16~02:48 · 06:09~06:31 · 08:27~08:57(08:49에 `[음악]` 표시만). **세 곳 모두 원 영상 발췌로 추정되며 내용 미상이다.**
> ⚠️ 그래서 다음은 캡션으로 확인되지 않는다: ① *"무엇이 바뀌었는지는 올해 3월 팟캐스트에서 이렇게 말했습니다."*(02:11~02:13) 뒤 — **Karpathy가 팟캐스트(설명란의 No Priors 인터뷰로 추정)에서 한 말.** ② *"카파씨의 답은 아예 자리를 비우라는 겁니다."*(06:04~06:06) 뒤 — **루프에서 빠지라는 대목의 본론.** ③ MenuGen 소개(08:19~08:24) 뒤 — **Sequoia 행사에서 그 앱에 대해 한 말.** → **이 영상에는 Karpathy 본인 발화가 캡션으로 한 줄도 없다.** 그의 글 · 댓글은 전부 내레이션의 한국어 옮김이다.
>
> **ASR 판독(ko-orig).** *안드레이 카파시 · 카파씨* → Andrej Karpathy, *밸브 코딩*(00:31) → 바이브 코딩(tags · 07:49 *바이브 코딩*. ⚠️ 영어 더빙 ASR은 같은 자리를 *coined the term "software 2.0"* 로 읽는다 — 더빙 쪽을 따르지 않았다), *엔트로픽* → Anthropic, *이름 바*(01:15) · *이런바*(07:39) → 이른바, *먼저 줬습니다*(01:57) → 판독 보류(더빙 *first emerged*), *손수 세기 분에*(03:02~03:04) → Sonnet 서브에이전트에(추정 — 03:48 · 11-08 Saraev 편의 *sends it to Sonnet … using Claude code workflows* 와 맞춤. 더빙은 이 낱말을 옮기지 않는다), *정액 코드*(03:35) → 정액 요금제(추정), *소래도 주*(03:48) → Sonnet 작업(추정), *해커 초부*(04:22) → 해커 튜브, *답 골라*(04:46) → 답글로(추정), *척하는 글*(05:23~05:25) → 첫 칸은 글(추정 — 더빙은 *a post about how to prompt* 로 다르게 읽는다. 판독 미확정), *단순 기술 용으로*(05:28) → 단순 기술 영어로(추정 — 11-08 Saraev 편의 ASD-STE100), *손을 때려면*(06:31) → 떼려면, *인 키코딩 에이전트 스킬*(07:03~07:06) → 인기 코딩 에이전트 스킬(추정), *길이만 갖고*(07:06) → 길이만 같고, *사와 세코이아 행사*(08:15) → 판독 보류(Sequoia 행사 — 설명란 *Sequoia AI Ascent 강연*), *메뉴 제*(08:19) → MenuGen(더빙 *Menugen*), *예소넷 4.5*(09:24) → Sonnet 4.5(⚠️ 더빙 ASR은 *Sonnet 3.5* — 버전 미확정), *숨을 쉴 c 있겠다*(10:10) → 쉴 수 있겠다, *트리스탄 튜브*(08:08~08:09) → 표기 미상(더빙 *Tristan Tube*).
> ⚠️ **더빙 ASR은 Opus의 버전을 일관되게 *Opus 3.5* 로 읽는다**(03:50 · 04:57 · 05:04 · 07:53 · 09:24). ko-orig는 전부 *오퍼스 5.5* 이고 tags도 `Opus 5.5` 다 — ko를 따랐다.
> ⚠️ **"단어 다섯 개"인데 캡션에는 넷이 나온다**: *업데이트, 배포, 보안 강화, 최적화*(04:29~04:31). 11-08 Saraev 편(영어 원음)은 *"update, deploy, secure, harden, and optimize"* 로 다섯을 센다 — *보안 강화* 가 secure · harden 두 낱말을 합친 옮김으로 보인다(추정).
>
> ⚠️ **전부 2차 전달이다.** 설명란: *"카파시가 블로그, X, Hacker News 댓글, 강연에 직접 남긴 기록을 따라가며 … 정리했습니다."* 위키는 설명란의 열한 개 링크(블로그 · X 글 셋 · HN 스레드 · No Priors · Sequoia AI Ascent · Boris Cherny 글 · skill-placebo · Chroma · 원본 요약 영상 `3BFMS3Wirq8`)를 열지 않았다. 수치(영상 6,454 · 댓글 4,300만 · 조회 587만 · 토큰 5억 400만 / 760만 · 60억 / 2,000만 / 5,000 등)는 해설이 옮긴 값이다.

## 설명란

안드레 카파시(Andrej Karpathy)는 금요일 밤 11시, 추천 알고리즘이 쏟아내는 "슬롭의 벽"에 질려 다음 날 아침 2시간 만에 자기만의 유튜브 HackerTube를 만들었습니다. Hacker News 20년 치 댓글에서 사람들이 추천한 영상 6,454개만 골라낸 사이트입니다. 그때 쓴 프롬프트의 핵심은 단어 다섯 개였습니다.

카파시가 블로그, X, Hacker News 댓글, 강연에 직접 남긴 기록을 따라가며 상위 0.2% 사용자가 AI를 쓰는 방식을 정리했습니다. 짧게 말하고, 루프에서 손을 떼고, 사람은 결과를 이해하는 데 시간을 씁니다.

타임라인
0:00 금요일 밤 11시, 슬롭의 벽
1:03 0.2%의 사람들
2:47 두 시간 동안 한 일
3:58 짧고 멍청한 프롬프트
5:11 사람의 일은 이해
6:00 루프에서 빠져라
6:57 남의 스킬 팩
7:46 앱은 버려도 된다
9:33 정리

참고
HackerTube (카파시 블로그): https://karpathy.bearblog.dev/hacker-tube/
X 발표 글: https://x.com/karpathy/status/2116957135661945283
Hacker News 스레드: https://news.ycombinator.com/item?id=50319510
0.2% 글: https://x.com/karpathy/status/2109361546505966046
이해의 사다리 글: https://x.com/karpathy/status/2105819303471976479
No Priors 인터뷰: https://www.youtube.com/watch?v=kwSVtQ7dziU
Sequoia AI Ascent 강연: https://www.youtube.com/watch?v=96jN2OCOfLs
Boris Cherny 팁: https://x.com/bcherny/status/2007179861115511237
skill-placebo: https://github.com/simonether/skill-placebo
Context Rot (Chroma): https://research.trychroma.com/context-rot
원본 요약 영상: https://www.youtube.com/watch?v=3BFMS3Wirq8

#Karpathy #카파시 #ClaudeCode #AI코딩 #바이브코딩

> info.json `tags`: AI 코딩 · Andrej Karpathy · Claude Code · Hacker News · HackerTube · No Priors · Opus 5.5 · 바이브 코딩 · 안드레 카파시 · 카파시 · 코딩 에이전트 · 클로드 코드 · 프롬프트

## 트랜스크립트 — ko-orig (Korean original, ASR variant=gemini)

[00:00] 금요일 밤 11시. 피곤한 몸으로
[00:02] 유튜브를 켠 한 개발자가 그 화면을
[00:04] 보고 이렇게 적었습니다.
[00:05] 망가질대로 망가진 슬롭의 벽,
[00:07] 터무니없이 부풀린 썸네일에 늘 같은
[00:09] 추천 뿐이었다고요.
[00:11] 다음 날 토요일 아침, 그는
[00:12] 클로드에게 일을 하나 맡깁니다.
[00:14] 해커 뉴스에서 추천된 영상만 모아서
[00:16] 우리만의 유튜브를 만들자.
[00:18] 두 시간 뒤, 정말로 유튜브가 하나
[00:19] 생겼습니다.
[00:20] 이름은 해커 튜브. 해커 뉴스
[00:22] 20년치 댓글에서 골라낸 영상
[00:24] 6,454개가 들어 있습니다.
[00:26] 만든 사람은 안드레이 카파시입니다.
[00:29] 오픈 AI를 함께 세웠고 테슬라에서
[00:31] AI를 이끌었고 밸브 코딩이라는 말을
[00:33] 처음 쓴 사람 이죠.
[00:34] 올해 5월에는 엔트로픽에
[00:35] 합류했습니다.
[00:37] 이 해커 튜브 발표 글은 조회수
[00:38] 587만회를 넘겼습니다.
[00:40] 그런데 정작 눈에 띄는 건 글 아래에
[00:42] 덧붙인 문단입니다. 자기는 이제
[00:44] 전통적인 엔지니어링 비슷한 일을
[00:46] 하나도 하지 않는다고 했습니다.
[00:48] 코드를 읽지도 쓰지도 않고 터미널
[00:50] 명령도 치지 않는다.
[00:52] 클로드와 대화만 하고 모든 일을
[00:54] 클로드가 하게 한다.
[00:55] 코드를 한 줄도 치지 않는 사람이
[00:57] 어떻게 두 시간만에 서비스를 하나
[00:58] 띄웠을까요?
[00:59] 오늘은 카파시가 직접 남긴 글과
[01:01] 댓글로 두 시간을 하나씩
[01:02] 뜯어보겠습니다.
[01:04] 왜 추천이 그 모양이냐는 질문에
[01:06] 카파시는 알고리즘이 보통 사람들의
[01:08] 취향으로 학습되니 자기 같은 사람은
[01:10] 반올림 오차일 뿐이라고 답했습니다.
[01:12] 그 집단이 얼마나 작은지 카파시가
[01:14] 10월에 대충 계산해 본 글이
[01:15] 있습니다. 이름 바 냅킨 계산입니다.
[01:19] 약 60억 명은 AI를 거의 써 본
[01:21] 적이 없습니다.
[01:23] 10억에서 20억 명은 무료 챗봇을
[01:25] 조금 나은 구글 검색처럼 씁니다.
[01:27] 그리고 약 2000만 명, 0.2%가
[01:29] 있습니다.
[01:30] 몇 주, 몇 달 걸리던 큰 프로젝트를
[01:32] 에이전트가 프롬프트 하나로 끝내는 걸
[01:34] 지켜보는 사람들입니다.
[01:36] 맨 꼭대기에는 약 5000명이 더
[01:37] 있습니다. 연구소 안에서 최전선
[01:39] 시스템을 쓰는 사람들입니다.
[01:41] 왜 이렇게 벌어질까요?
[01:43] 카파시는 이유를 셋으로 꼽았습니다.
[01:45] [음악] 첫째는 야망입니다.
[01:47] 한 문단짜리 답을 묻는 질문으로는
[01:49] 시스템이 거의 힘을 쓰지 않습니다.
[01:51] 둘째는 들쭉날쭉합니다.
[01:53] AI의 실력은 디지털이고 검증할 수
[01:55] 있고 돈이 되는 분야에서 먼저
[01:57] 줬습니다. 수학과 코드가 그렇습니다.
[02:00] 셋째는 접근입니다.
[02:01] 무료 요금제냐, 유료냐, 연구소
[02:03] 내부냐에 따라 보는 세상이 다릅니다.
[02:06] 같은 그래서 카파시는 자기도 1년
[02:08] 전만 해도 코드를 한 글자씩 손으로
[02:10] 쳤다고 적었습니다.
[02:11] 무엇이 바뀌었는지는 올해 3월
[02:13] 팟캐스트에서 이렇게 말했습니다.
[02:47] 그럼 그 2시간 동안 실제로 무슨
[02:49] 일이 있었을까요?
[02:50] 카파시의 글과 댓글을 이어 붙이면
[02:52] 순서가 이렇습니다.
[02:53] 먼저 클로드 가 해커 뉴스 20년치
[02:55] 댓글 4,300만 개를 내려
[02:57] 봤습니다. 허깅페이스에 공개된
[02:59] 데이터가 있었다고 합니다.
[03:00] 주소와 정규식으로 거르고 스팸을 버린
[03:02] 다음 남은 댓글만 손수 세기 분에
[03:04] 하나하나 읽었습니다.
[03:06] 클로드 코드의 워크플로우 기능으로요.
[03:08] 그렇게 영상을 추천하는 댓글 약 4만
[03:10] 개, 영상 6,454개가 남았습니다.
[03:13] 사이트 소개 페이지에는 기준도 적혀
[03:14] 있습니다.
[03:15] 서로 다른 세 사람이 서로 다른 세
[03:17] 달에 걸쳐 진지하게 추천한 영상만
[03:19] 남긴다. [음악]
[03:20] 이 과정에서 카파시가 손으로 한 일은
[03:21] 딱 세 가지였습니다.
[03:23] 구글 클라우드에서 유튜브 API 키를
[03:25] 만들고 서버를 하나 켜고 도메인을
[03:27] 샀습니다. 그것도 클로드가 일하는
[03:29] 틈틈이 했습니다. 그래서 여전히
[03:30] 조금은 팀으로 일하는 느낌이라고
[03:32] 적었습니다.
[03:33] 들어간 토큰 양도 공개했습니다.
[03:35] 카파시는 정액 코드로 했다며
[03:37] 클로드에게 토큰을 합산시켜 댓글에
[03:38] 올렸습니다. [음악]
[03:40] 입력 토큰 5억 400만 개, 출력
[03:42] 760만 개였습니다.
[03:46] 그중 90% 넘게가 댓글에 이름표를
[03:48] 붙이는 소래도 주였습니다.
[03:50] 앱을 만들고 배포한 진짜 작업은
[03:52] 오퍼스 5.5 토큰 약 100만 개.
[03:55] 카파시는 요즘 기준으로 아주 작은
[03:56] 프로젝트라고 했습니다.
[03:58] 그럼 클로드에게는 뭐라고 말했을까요?
[04:01] 해커 뉴스에서 누군가 모델을 어떻게
[04:02] 지휘하느냐고 묻자 카파시는 이렇게
[04:04] 답했습니다.
[04:05] 내 프롬프트는 점점 짧고 멍청해진다.
[04:08] 말을 덜해도 모델이 내가 뭘 하려는지
[04:10] 알아듣기 때문이다.
[04:12] 너무 많이 주면 오히려 요구 사항으로
[04:13] 모델을 묶어버린다고 했습니다. 내버려
[04:15] 뒀으면 더 똑똑하게 했을 텐데
[04:17] 말이죠.
[04:18] 그래서 프롬프트의 요령은 적은 정보를
[04:20] 딱 맞게 주는 쪽으로 가고 있다고
[04:21] 봤습니다.
[04:22] 해커 초부에서도 그렇게 했습니다.
[04:24] 서버가 켜지자 카파시는 클로드에게
[04:26] 서버 주소를 주고 단어 다섯 개를
[04:28] 말했습니다.
[04:29] 업데이트, 배포, 보안 강화,
[04:31] 최적화.
[04:32] 그러자 클로드가 전부 해냈다고
[04:33] 적었습니다.
[04:36] 보안도 비슷합니다. 가끔은 최근
[04:38] 사이버 쪽 좀 확인해 줘 정도로만
[04:39] 말한다고 했습니다. 그러면 클로드가
[04:41] 하위 에이전트 몇 개를 보내 알아서
[04:43] 처리한다고 요.
[04:44] 소스 코드를 공개해 달라는 요청에는
[04:46] 농담 반으로 이런 프롬프트를 답 골라
[04:48] 달았습니다.
[04:49] 안녕 클로드, 좋은 아침이야.
[04:51] 해커뉴스에서 오랫동안 반복해서 추천된
[04:53] 영상만 모은 유튜브 같은 사이트
[04:55] 만들어 줘. 실수하지 말고. [음악]
[04:57] 다만 조건이 하나 붙습니다. 이렇게
[04:58] 짧게 맡기는 건 오퍼스 5.5
[05:00] 이상에서만 한다고 했습니다. 더 약한
[05:02] 모델은 이만큼 믿지 않겠다고요.
[05:04] 카파시가 밝힌 기본 설정도
[05:06] 단순합니다. 맥용 클로드 코드
[05:08] 데스크톱 앱에 오퍼스 5.5. 노력
[05:10] 수준은 중간입니다.
[05:12] AI가 일을 다 하면 사람은 무엇을
[05:14] 할까요?
[05:15] 카파시는 10월 초에 이런 글을
[05:16] 올렸습니다. 앞으로는 언어 모델의
[05:18] 결과물을 이해하는 데 훨씬 많은
[05:20] 시간을 쓰게 될 거라고요.
[05:22] 그래서 결과물을 받아보는 방법을
[05:23] 사다리처럼 정리했습니다. 척하는
[05:25] 글입니다.
[05:26] 항공기 정비 문서 용으로 만든 단순
[05:28] 기술 용으로 설명해 달라고 합니다.
[05:30] 더 좋은 건 그림입니다.
[05:32] 다이어그램으로 그려 달라고 하면 훨씬
[05:33] 빨리 읽힙니다.
[05:34] 그보다 좋은 건 HTML입니다.
[05:36] 움직이고 눌러 볼 수 있는 웹페이지로
[05:38] 받는 거죠.
[05:40] 그리고 카파시가 가장 기대한다고 한
[05:41] 형식은 주제마다 새로 만드는 설명
[05:43] 영상입니다. 실제로 되기 시작했다고
[05:45] 적었습니다.
[05:46] 글의 결론은 이렇습니다. 모델이
[05:48] 잡일을 더 많이 맡을수록 사람의 일은
[05:50] 감독과 이해 쪽으로 올라간다.
[05:52] 그리고 지능과 코드가 흔해진 만큼
[05:54] 예전 같으면 만들 이유가 없던 크고
[05:57] 버려도 되는 소프트웨어를 마음껏
[05:58] 주문하라고 했습니다.
[06:00] 짧게 말하고 결과를 이해한다. 그럼
[06:03] 그 사이에는 무엇을 할까요?
[06:04] 카파씨의 답은 아예 자리를 비우라는
[06:06] 겁니다.
[06:31] 물론 손을 때려면 믿을 수 있어야
[06:32] 합니다. 클로드 코드를 만든 보리스
[06:35] 체르니는 올해 1월에 이렇게
[06:36] 썼습니다. 가장 중요한 팁은
[06:38] 클로드에게 자기 작업을 검증할 방법을
[06:40] 주는 것이다. 그럼 피드백 고리가
[06:42] 있으면 최종 결과물의 품질이 두 세
[06:44] 배가 된다.
[06:45] 해커 튜브를 공개한 날 밤에도
[06:46] 그랬습니다. 스레드에 기능 요청
[06:48] 댓글이 달리면 카파씨는 금세
[06:50] 추가했다고 답했습니다. 검색 필터,
[06:52] 정렬, 재생 목록 같은 기능이 공개
[06:54] 두 시간도 안 돼 한꺼번에
[06:56] 들어갔습니다.
[06:57] 요즘은 이런 요령을 스킬 파일로 묶어
[06:59] 내려받는 사람이 많습니다. 정말
[07:01] 효과가 있을까요?
[07:02] 9월 말에 이걸 직접 재본 사람이
[07:03] 있습니다. 인 키코딩 에이전트 스킬
[07:06] 아홉 개를 길이만 갖고 쓸모는 없는
[07:08] 글과 비교했습니다. 약으로 치면 위약
[07:10] 대조군입니다.
[07:11] 결과는 아홉 개 중 두 개만 위약보다
[07:13] 나았습니다. 그것도 품질이 아니라
[07:15] 같은 일을 더 싸게 했다는
[07:16] 뜻이었습니다.
[07:17] 여섯 개는 차이가 없었고 하나는
[07:19] 오히려 통과율이 떨어졌습니다.
[07:23] 이 아홉 개 중에는 카파씨라는 이름이
[07:24] 붙은 스킬도 하나 들어 있었습니다.
[07:26] 카파씨 본인이 아니라 다른 사람이
[07:27] 만든 것인데 판정은 위약과 차이
[07:30] 없음이었습니다. [음악] 길게 많이
[07:32] 넣는다고 좋은 게 아니라는 연구도
[07:33] 있습니다. 크로마는 작년 7월 모델
[07:35] 18개를 시험했습니다. 입력이
[07:37] 길어질수록 성능이 점점
[07:39] 불안정해졌습니다. 이런바 [음악]
[07:40] 컨텍스트 부패입니다. 카파씨는 그
[07:43] 반대로 모델에게 점점 덜 말하는
[07:44] 방식을 택했습니다.
[07:46] 해커 튜브의 코드를 공개해 달라는
[07:48] 사람이 많았지만 카파씨는 서버 코드는
[07:49] 공개하지 않았습니다. 바이브 코딩으로
[07:51] 만든 엉망 진창이라서요.
[07:53] 대신 댓글을 분석한 데이터를 압축
[07:55] 파일 하나로 올렸습니다. 이걸 오퍼스
[07:57] 5.5에게 주고 유튜브 같은 사이트를
[07:58] 만들어 달라고 하면 거의 바로
[08:00] 나온다. 이 부분은 3분쯤
[08:01] 걸렸다고요.
[08:03] 엿새 뒤에는 실제로 그렇게 했습니다.
[08:04] 다른 개발자가 올린 유튜브 채널
[08:06] 목록을 보고 클로드 코드로 3분만에
[08:08] 영상 47,000개 짜리 트리스탄
[08:09] 튜브를 만들었습니다.
[08:11] 앱을 만드는게 이렇게 쉬워지면 앱
[08:13] 자체는 얼마나 가치가 있을까요?
[08:15] 카파시는 사와 세코이아 행사에서 자기
[08:17] 앱 이야기를 꺼냈습니다.
[08:19] 메뉴 제는 식당 메뉴판 사진을 올리면
[08:20] 글자를 읽어서 요리마다 그림을
[08:22] 만들어주는 앱입니다. 카파시가 직접
[08:24] 코딩해서 만들었죠.
[08:49] [음악]
[08:57] 앱이 이렇게 쉽게 나오면 해커
[08:58] 튜브에서 진짜 귀한 건 20년치
[09:00] 댓글에서 걸러낸 영상 목록입니다.
[09:03] 카파시가 코드 대신 공개한 것도 바로
[09:04] 그 데이터였습니다.
[09:06] 무엇이 더 나은지 고르는 일도
[09:08] 사람에게 남습니다. 카파시는 요즘
[09:10] 벤치마크가 아주 나쁜 상태라 사실상
[09:12] 믿지 않는다고 했습니다.
[09:14] 대신 남이 만든 재미있는 평가를
[09:15] 공유했습니다. 위도와 경도만 주고
[09:18] 육지냐 바다냐를 16,200번
[09:20] 묻습니다.
[09:21] 답을 점으로 찍으면 세계 지도가
[09:22] 나옵니다.
[09:24] 예소넷 4.5는 60% 남짓, 오퍼스
[09:26] 5.5는 99%를 맞췄습니다.
[09:29] 카파시의 말로는 모델이 인터넷을
[09:31] 압축하면서 지구를 안다는 겁니다.
[09:33] 카파시는 해커 튜브 발표 글을 이렇게
[09:35] 끝냈습니다. 몇 주, 몇 달 걸렸을
[09:38] 멋진 프로젝트를 이제 아침밥 먹으면
[09:40] 해치울 수 있다.
[09:41] 우리가 아직 생각하지 못한 건 또
[09:42] 뭘까?
[09:44] 정리하면 이렇습니다. 첫째, 짧게
[09:46] 말합니다. 모델이 알아들을 만큼만 딱
[09:48] 맞게.
[09:49] 둘째, 자리를 비웁니다. 검증할
[09:52] 방법을 주고 다음 프롬프트를 기다리게
[09:54] 하지 않습니다.
[09:55] 셋째, [음악] 남는 시간은 이해하는
[09:57] 데 씁니다. 결과물을 그림과 페이지와
[09:59] 영상으로 받아보고 무엇이 나은지
[10:01] 스스로 고릅니다.
[10:04] 금요일 밤에 슬롭의 벽으로 돌아가
[10:05] 볼까요? 카파시는 불평하는 대신
[10:07] 2시간을 썼고 글 끝에 이렇게
[10:09] 적었습니다.
[10:10] 이제야 숨을 쉴 c 있겠다.
[10:12] 여러분이 요즘 화면을 보며 답답했던
[10:14] 건 무엇인가요? 두 시간이면 그걸
[10:16] 직접 고칠 수 있을지도 모릅니다.

## 트랜스크립트 — en-orig (영어 더빙 ASR — 인용하지 않음)

[00:00] Friday, 11 PM. A weary developer opened
[00:02] YouTube and wrote this after looking at
[00:04] the screen.
[00:05] He lamented a feed ruined by slop,
[00:07] absurdly exaggerated thumbnails, and the
[00:09] same old recommendations.
[00:11] The next morning, Saturday, he gave
[00:13] Claude a task.
[00:14] "Let’s build our own YouTube, featuring
[00:16] only videos recommended on Hacker News.
[00:17] "
[00:18] Two hours later, a new YouTube actually
[00:19] existed.
[00:20] Its name is HackerTube. It contains
[00:22] 6,454 videos curated from 20 years of
[00:24] Hacker News comments.
[00:26] The creator is Andrej Karpathy.
[00:29] He co-founded OpenAI, led AI at Tesla,
[00:31] and coined the term "software 2.0."
[00:34] He joined Anthropic this past May.
[00:37] His announcement post for HackerTube
[00:38] surpassed 5.87 million views.
[00:40] However, what really stood out was the
[00:42] paragraph he added at the bottom.
[00:44] He stated that he no longer does
[00:45] anything resembling traditional
[00:47] engineering.
[00:48] He doesn't read or write code, nor does
[00:50] he type terminal commands.
[00:52] He only talks to Claude and lets Claude
[00:53] do all the work.
[00:55] How did someone who didn't write a
[00:56] single line of code launch a service in
[00:58] two hours?
[00:59] Today, we will break down those two
[01:01] hours using the posts and comments
[01:02] Karpathy left himself.
[01:04] To the question of why recommendations
[01:06] are so poor, Karpathy replied that
[01:07] algorithms learn from the average
[01:09] person's tastes, so people like him are
[01:10] just a rounding error.
[01:12] There is a post from October where
[01:14] Karpathy roughly calculated how small
[01:15] that group is. It’s called "napkin math
[01:17] ."
[01:19] About 6 billion people have almost never
[01:21] used AI.
[01:23] 1 to 2 billion people use free chatbots
[01:24] like a slightly better Google search.
[01:27] Then there are about 20 million people,
[01:29] or 0.2%.
[01:30] These are people watching agents finish
[01:32] big projects that used to take weeks or
[01:34] months with a single prompt.
[01:36] At the very top, there are about 5,000
[01:37] more people. These are the people using
[01:39] frontline systems inside research labs.
[01:41] Why is there such a gap?
[01:43] Karpathy pointed to three reasons.
[01:45] First is ambition.
[01:47] Systems exert very little power when
[01:48] asked questions that only require a
[01:49] one-paragraph answer.
[01:51] Second is its jagged nature.
[01:53] AI's proficiency first emerged in fields
[01:55] that are digital, verifiable, and
[01:57] profitable.
[01:58] Math and coding are examples of this.
[02:00] Third is access.
[02:02] Depending on whether you use a free plan
[02:03] , a paid plan, or work inside a lab, you
[02:04] see a different world.
[02:06] That is why Karpathy noted that even he
[02:08] was typing code character by character
[02:09] by hand just a year ago.
[02:11] He explained what changed in a podcast
[02:13] this past March.
[02:48] So, what actually happened during those
[02:49] two hours?
[02:50] If you piece together Karpathy's posts
[02:51] and comments, the sequence goes like
[02:53] this.
[02:54] First, Claude went through 43 million
[02:55] comments from 20 years of Hacker News.
[02:58] He says there was public data available
[02:59] on Hugging Face.
[03:00] After filtering with URLs and regex to
[03:03] remove spam, he had the rest read one by
[03:05] one.
[03:06] Using Claude Code's workflow feature.
[03:08] That left about 40,000 comments
[03:10] recommending videos, totaling 6,454
[03:12] videos.
[03:13] The site's intro page also lists the
[03:14] criteria.
[03:15] Only videos seriously recommended by
[03:17] three different people over three
[03:18] different months remain.
[03:20] In this process, there were only three
[03:21] things Karpathy did manually.
[03:23] He created a YouTube API key on Google
[03:25] Cloud, started a server, and bought a
[03:27] domain.
[03:28] He even did that in the spare time while
[03:29] Claude was working. So he wrote that it
[03:31] still feels a bit like working as a team
[03:32] .
[03:33] He also disclosed the amount of tokens
[03:34] used. Karpathy had Claude sum up the
[03:36] tokens and posted them in the comments,
[03:37] saying he did it with a flat-rate code.
[03:40] It was 504 million input tokens and 7.6
[03:42] million output tokens.
[03:46] Over 90%of that was just the task of
[03:48] labeling the comments.
[03:50] The actual work of building and
[03:51] deploying the app was about 1 million
[03:53] Opus 3.5 tokens.
[03:55] Karpathy called it a very small project
[03:56] by today's standards.
[03:58] So, what did he say to Claude?
[04:01] When someone on Hacker News asked how he
[04:02] orchestrates the model, Karpathy replied
[04:04] like this.
[04:05] My prompts are getting shorter and
[04:07] dumber.
[04:08] That's because the model understands
[04:09] what I'm trying to do even if I say less
[04:11] .
[04:12] He said that giving too much info
[04:13] actually ties the model down with
[04:14] requirements. When it could have done a
[04:16] smarter job if left alone.
[04:18] So he saw the trick to prompting as
[04:19] moving toward giving just the right
[04:21] amount of information.
[04:22] He did the same for Hacker Tube. Once
[04:24] the server was up, Karpathy gave Claude
[04:26] the server address and said five words.
[04:29] Update, deploy, secure, optimize.
[04:32] And he wrote that Claude handled it all
[04:34] .
[04:36] Security is similar.
[04:37] He said he occasionally just tells it to
[04:38] check the recent cybersecurity side of
[04:40] things.
[04:41] Then Claude sends a few sub-agents to
[04:42] take care of it on its own.
[04:45] To the request for the source code, he
[04:47] jokingly picked this prompt as the
[04:48] answer.
[04:49] Hi Claude, good morning. Make me a site
[04:52] like YouTube that collects only the
[04:53] videos repeatedly recommended on Hacker
[04:54] News for a long time. Don't make any
[04:56] mistakes.
[04:57] However, there is one condition. He said
[04:59] he only delegates things this briefly
[05:00] with Opus 3.5 or higher.
[05:02] He wouldn't trust weaker models this
[05:03] much.
[05:04] The basic setup Karpathy revealed is
[05:06] also simple. Claude Code desktop app for
[05:08] Mac with Opus 3.5. The effort level is
[05:10] set to medium.
[05:12] When AI does all the work, what will
[05:14] humans do?
[05:15] Karpathy posted this in early October.
[05:17] He said that in the future, we will
[05:19] spend much more time understanding the
[05:20] output of language models.
[05:22] So, he organized the methods for
[05:23] receiving outputs like a ladder. It’s a
[05:25] post about how to prompt.
[05:26] Ask it to explain using simple technical
[05:28] terms, like those used for aircraft
[05:29] maintenance manuals.
[05:30] Pictures are even better.
[05:32] If you ask it to draw a diagram, it
[05:33] reads much faster.
[05:34] Better than that is HTML.
[05:36] You receive it as a web page that you
[05:38] can move and click around.
[05:40] And the format Karpathy said he is most
[05:41] excited about is a video explanation
[05:43] created for each topic. He wrote that it
[05:44] has actually started to become possible
[05:45] .
[05:46] The conclusion of the post is this. As
[05:48] models take on more chores, human work
[05:49] shifts toward supervision and
[05:51] understanding.
[05:52] And since intelligence and code have
[05:54] become abundant, he said to freely order
[05:56] large, disposable software that would
[05:57] have been pointless to build before.
[06:00] Speak briefly and understand the results
[06:02] . Then, what do we do in the meantime?
[06:05] Karpathy's answer is to step away
[06:06] entirely.
[06:31] Of course, to let go, you have to be
[06:32] able to trust it.
[06:33] Boris Cherny, who created Claude Code,
[06:35] wrote this in January of this year.
[06:37] The most important tip is to give Claude
[06:39] a way to verify its own work.
[06:41] With a feedback loop, the quality of the
[06:43] final output becomes two to three times
[06:44] better.
[06:45] It was the same on the night he released
[06:46] HackerTube. When feature request
[06:48] comments appeared on the thread,
[06:49] Karpathy replied that he had added them
[06:51] immediately.
[06:52] Features like search filters, sorting,
[06:53] and playlists were all added in under
[06:55] two hours of the release.
[06:57] These days, many people bundle these
[06:59] tips into "skill files" to download. Are
[07:01] they really effective?
[07:02] In late September, someone actually
[07:03] measured this.
[07:04] They compared nine coding agent skills
[07:06] against text that had length but no
[07:08] actual utility. In pharmaceutical terms
[07:10] , it’s a placebo control group.
[07:11] The result was that only two out of the
[07:13] nine were better than the placebo. And
[07:14] that didn't mean higher quality, just
[07:15] that it did the same job more cheaply.
[07:18] Six showed no difference, and one
[07:19] actually had a lower success rate.
[07:23] Among these nine was a skill named after
[07:25] Karpathy. It wasn't made by Karpathy
[07:27] himself but by someone else, and the
[07:29] verdict was "no difference from placebo
[07:30] ."
[07:31] There is also research suggesting that
[07:32] putting in a lot of long text isn't
[07:33] necessarily good. Chroma tested 18
[07:35] models in July of last year.
[07:37] As the input got longer, performance
[07:39] became increasingly unstable. This is
[07:40] called context corruption.
[07:42] Karpathy chose the opposite approach of
[07:44] telling the model less and less.
[07:46] Many people asked him to release the
[07:48] HackerTube code, but Karpathy did not
[07:49] release the server code. Because it was
[07:51] a mess created through "vibe coding."
[07:53] Instead, he uploaded the data from his
[07:54] comment analysis as a single compressed
[07:56] file. If you give this to Opus 3.5 and
[07:58] ask it to build a YouTube-like site,
[07:59] it's finished almost instantly. He said
[08:01] this part took about three minutes.
[08:03] Six days later, he actually did just
[08:04] that. Using a list of YouTube channels
[08:06] uploaded by another developer, he built
[08:07] "Tristan Tube," with 47,000 videos, in
[08:09] just three minutes with Claude Code.
[08:11] If building apps becomes this easy, how
[08:13] much is the app itself actually worth?
[08:15] Karpathy brought up his own app at a
[08:17] Sequoia event.
[08:19] "Menugen" is an app that reads a photo
[08:20] of a restaurant menu and generates an
[08:22] image for every dish. Karpathy coded it
[08:24] himself.
[08:57] When apps are this easy to create,
[08:58] what’s truly valuable in HackerTube is
[09:00] the list of videos filtered from 20
[09:01] years of comments.
[09:03] That data is exactly what Karpathy
[09:04] released instead of the code.
[09:06] Choosing what is better also remains a
[09:08] task for humans.
[09:09] Karpathy stated that benchmarks are in
[09:10] such a poor state these days that he
[09:12] practically doesn't trust them.
[09:14] Instead, he shared an interesting
[09:15] evaluation created by someone else. It
[09:16] gives only latitude and longitude and
[09:18] asks whether it's land or sea 16,200
[09:20] times.
[09:21] If you plot the answers as dots, a world
[09:22] map appears.
[09:24] Sonnet 3.5 got about 60%right, while
[09:26] Opus 3.5 nailed 99%.
[09:29] According to Karpathy, the model learns
[09:30] about the Earth while compressing the
[09:32] internet.
[09:34] Karpathy ended his HackerTube
[09:35] announcement post like this.
[09:36] Fantastic projects that would have taken
[09:38] weeks or months can now be finished
[09:39] before breakfast.
[09:41] What else have we not even thought of
[09:43] yet?
[09:44] To summarize, it's like this. First,
[09:46] keep it brief. Just enough for the model
[09:48] to understand.
[09:50] Second, step away. Give it a way to
[09:52] verify its work and don't make it wait
[09:53] for the next prompt.
[09:55] Third, use the extra time to understand
[09:57] .
[09:58] Receive the results as images, pages, or
[10:00] videos, and choose for yourself what is
[10:02] better.
[10:04] Shall we go back to the wall of slop on
[10:05] a Friday night? Instead of complaining,
[10:07] Karpathy spent two hours and wrote this
[10:09] at the end of his post.
[10:10] Now I can finally breathe.
[10:12] What has been frustrating you while
[10:13] looking at your screen lately?
[10:15] With two hours, you might just be able
[10:17] to fix it yourself.
