---
title: "AI 코딩 공장이 슬롭을 안 내보내는 12가지 규칙 | Dex Horthy"
type: video
source: https://www.youtube.com/watch?v=4NqFB60bh1U
site: youtube.com
author:
  - "[[Tech Bridge]]"
duration: 12:13
published: 2026-11-25
created: 2026-11-26
description: "Tech Bridge 한국어 해설 12:13, 공식 챕터 11, 한국어 내레이션(ko-orig) + en-orig(영어 더빙 ASR과 Dex Horthy 원음 조각이 섞임). Dex Horthy(Factory, 전 HumanLayer CEO)의 AI Engineer Code Summit 발표를 정리 — SlopCodeBench 최고 모델 16.33%(196개 중 32개), 소프트웨어 공장은 그냥 좋은 엔지니어링, 앞 압력 · 뒤 압력 루프, 적을 알라, 계획과 expected pain, 시각 정렬, 결정론적 린트 규칙, 슬롭도 도구다, 기능 플래그, 포지 통합, 돈으로 못 사는 검증까지 규칙 12가지, 그리고 안티 슬롭 선언(No AI Slop: A Manifesto)과 그래도 사람이 검토해야 하는 이유. ⚠️ Horthy 원음은 en-orig 단일 트랙(아홉 조각, 교차 확인 없음), 두 트랙 모두 무캡션 다섯 곳 약 47초."
tags:
  - clippings/youtube
---

**Source URL**: https://www.youtube.com/watch?v=4NqFB60bh1U
**Channel**: Tech Bridge · **Duration**: 12:13 · **Published**: 2026-11-25

> **게시일.** info.json `upload_date` **`20261125`**, `timestamp` 1795597229(= 2026-11-25 09:00:29 UTC = **2026-11-25 18:00 KST**), `availability`=`public`. 2026-11-26 회차(09:10 KST)에서 처음 잡혔다. 파일명에서 `|` 는 뺐다.
>
> **오디오 트랙과 자막 — 인용 규칙.** ⚠️ 이 회차에도 yt-dlp가 영상 포맷 목록을 받지 못해(info.json `formats` 비어 있음) **오디오 트랙 구성과 메타 `language`(`None`)를 확인하지 못했다.** 자막 트랙의 성격은 내용으로 판정했다. 수동 자막 없음. `ko` = `ko-orig`(파일 동일, `kind=asr&lang=ko&variant=gemini`) — **한국어 내레이션** 이다. `en-orig`(`kind=asr&lang=en&variant=timing-optimized`)는 **두 가지가 섞여 있다**: ① 내레이션 자리는 **영어 더빙의 ASR** 이다 — 첫 줄부터 내레이션의 번역이고(*Let's start by looking at the score received by the best model*) 문장이 ko-orig와 같은 초에 맞물린다. ② ko-orig가 `[음악]` 으로 비는 원 발표 발췌 자리에는 **Dex Horthy의 원음** 이 잡혔다 — 1인칭이고 *Uh / Um* 이 섞이며 ko-orig에 대응하는 줄이 없다. **더빙 ASR은 인용하지 않았고 판독 대조용으로만 썼다.** 한국어 인용은 전부 ko-orig 내레이션, 영어 인용은 전부 en-orig의 Horthy 원음이다. 429 없음(`--sleep-subtitles 8`).
> ⚠️ **Horthy 원음은 en-orig 단일 트랙이다 — 교차 확인 없음.** 원음으로 판정한 조각 아홉 곳: 00:57~01:14 · 02:07~02:13 · 03:10~03:40 · 04:42~05:00 · 05:52~06:25 · 08:07~08:15 · 08:36~08:47 · 09:42~10:01 · 11:04~11:12. 08:36 줄처럼 더빙 문장과 원음이 한 줄에 붙어 잡힌 곳이 있고, 조각의 앞뒤가 잘린 곳이 많다(05:52 · 09:42 · 11:04).
>
> **무캡션 구간(`gaps.py` 4.5초 기준).** en-orig 다섯 곳: 02:00~02:07 · 04:32~04:42 · 07:55~08:07 · 10:51~11:04 · 11:15~11:21 — 합쳐 약 47초. **이 다섯 곳은 두 트랙 모두 비어 있어 내용 미상이다.** ko-orig는 열세 곳: 00:56~01:17 · 02:05~02:22 · 03:10~03:43 · 04:32~05:04 · 05:49~06:09 · 06:11~06:25 · 07:54~08:05 · 08:16~08:25 · 08:36~08:55 · 09:41~09:57 · 09:59~10:04 · 10:51~11:06 · 11:08~11:20 — 합쳐 약 3분 44초(대부분 en-orig에 원음이 잡힌 자리).
> ⚠️ **내용 미상인 것.** 앞 압력 설명의 앞머리(02:00~02:07) · 라이브러리 수치 뒤의 발췌 앞머리(04:32~04:42) · 포지 이야기의 앞머리(07:55~08:07) · **에이전트 리뷰어만으로는 왜 충분하지 않은지 — 챕터 *그래도 검토하는 이유* 의 본론(10:51~11:04 · 11:15~11:21).**
>
> **ASR 판독(ko-orig → 판독, 괄호는 근거).** *요즘 클라우드는*(00:13) → Claude(더빙 *Claude* · 원음 04:50~05:00이 같은 이야기), *덱스 호시* → Dex Horthy(제목 · 설명란 · tags), *휴먼 레이어* → HumanLayer, *팩토리* → Factory(설명란 · tags), *파로스 보고서*(00:43) → Faros AI(설명란), *압, 압력*(01:54) → 앞 압력(02:40 · 챕터 제목 *앞에서 밀고*), *CRI와 린터*(02:31) → CI와 린터(추정 — 01:32 · 01:43에는 *CI*), *슬롭 코드 벤치* → SlopCodeBench(설명란 · tags), *게이브 올란스키*(04:09) → Gabe Orlanski(설명란), *엔트로픽* → Anthropic, *페이블* → Fable, *쇼미*(06:44) → show me(10-15 소스의 스킬 이름), *콜 뭐든*(06:56) → curl(추정 — 10-15 소스 *let them use curl*), *클라우드 플레어* → Cloudflare, *딜런 몰로이*(07:12) → 10-15 소스 en-orig의 *Dylan Mulroy* 와 같은 사람으로 읽음(철자 미확인), *ES 린트* → ESLint, *포스트 호그, 스태시그*(07:35) → PostHog · Statsig(추정), *지워주면*(07:37) → 쥐여 주면(추정 — 문맥), *포즈를 하나로*(07:46) → 포지(forge)를 하나로(설명란 *포지 통합* · 더빙 *Forge*), *클라우드 코드나 코덱스*(08:25) → Claude Code · Codex(더빙), *뒤에서 거는 루프*(11:58) → 뒤에서 거르는 루프(챕터 제목 *뒤에서 거른다*).
> ⚠️ **판독하지 못한 것.** ① *위스콘신대학교 연구실 검증 시험*(03:43~03:44, 더빙 *an exam developed in collaboration with the University of Wisconsin lab*) — 낱말을 정하지 않았다. ② *GPT-6 아스트라 엑스 하이*(04:03) — 설정 이름을 정하지 않았다(더빙 *GPT 6 Astra X-Ha*). ③ *프리율은 오르고*(04:12, 더빙 *The free rate increased*) — 통과율로 보이나 정하지 않았다. ④ Faros 첫 수치 — ko-orig는 *31.3% 늘었습니다*, 더빙은 *31.3% of PRs were passed without review*. 증가율인지 비율인지 정하지 않았다. ⑤ *덱스는 아직 확인 중이라고 했습니다*(05:10) — 더빙은 *Dex said it was day* 로 깨져 대조할 수 없다. ko-orig를 따랐다. ⑥ 12번째 규칙의 08:14~08:25 — ko-orig에 *하네스* 라는 낱말이 없다(더빙 *for HANS*). 추정으로만 적었다. ⑦ *흩어져 있다고 싶습니다*(07:50~07:51) — 끝 낱말이 깨져 있다. ⑧ *에이전트 때는*(10:06) — *떼* 인지 정하지 않았다. ⑨ *코드를 전부 밀라는 걸까요*(10:44, 더빙도 깨짐) — 정하지 않았다. ⑩ 원음 쪽: *page 3 in the morning*(02:08) → paged at 3(추정), *clot and glit Python 3 in Python 2 style*(04:50) → 주어 미상, *per s format strings*(04:54) → `%s`(추정), *lters*(11:07) → linters(추정), *the cost of producing line PR 10-page doc is approaching the cost of constant*(09:53~10:01) → 깨져 있어 옮기지 않음. ⑪ 더빙은 화자를 *Dex Tosh*, 선언을 *sailor's*, 애자일을 *Agja* 로 읽는다 — 더빙 쪽 오류로 본다.
>
> ⚠️ **해설이고 2차 전달이다.** 위키는 원본 발표(`-NFMsM2y0Vk`)도, *No AI Slop: A Manifesto*(slopmanifesto.com)도, Gabe Orlanski의 글도, Faros AI 보고서도 이번에 열지 않았다. 벤치마크 · 보고서의 수치와 선언의 문구는 내레이션이 옮긴 한국어다. 규칙의 번호 열둘도 내레이션이 매긴 것이다. 화자의 소속(*Factory, 전 HumanLayer CEO*)은 설명란 표기다.


## 설명란

AI 에이전트에게 코드를 맡기는 '소프트웨어 공장', 슬롭 없이 돌릴 수 있을까요? 코딩 에이전트를 꾸준히 연구해 온 Dex Horthy(Factory, 전 HumanLayer CEO)가 AI Engineer Code Summit에서 내놓은 답을 정리했습니다.

요구사항이 바뀔 때마다 자기 코드를 고쳐 나가게 하는 SlopCodeBench에서 최고 모델도 16.33%(196개 중 32개)에 그쳤습니다. 그는 소프트웨어 공장이 새것이 아니라 원래 좋은 엔지니어링이라고 말하고, 앞 압력·뒤 압력 루프부터 '적을 알라', 계획, 시각 정렬, 린트 규칙, 기능 플래그, 포지 통합, 돈으로 못 사는 검증까지 12가지 규칙을 꼽습니다. 마지막으로 안티 슬롭 선언과, 그래도 사람이 검토해야 하는 이유를 다룹니다.

타임라인
0:00 슬롭 없는 AI 코드 공장, 최고 모델의 점수는?
0:25 공장은 새것이 아니다
1:50 앞에서 밀고, 뒤에서 거른다
2:51 적을 알라
5:19 계획은 얼마나
6:36 보여 주고, 직접 시험하게
7:05 기계가 잡을 건 기계에게
8:18 돈으로 못 사는 것
9:02 안티 슬롭 선언
10:43 그래도 검토하는 이유
11:50 처음 숫자로

참고
원본 발표: https://www.youtube.com/watch?v=-NFMsM2y0Vk
No AI Slop: A Manifesto: https://slopmanifesto.com
Gabe Orlanski, Slop Is Moving Up the Stack: https://gabeorlanski.github.io/posts/slop-moves-up/
Faros AI, The Acceleration Whiplash: https://www.faros.ai/research/ai-acceleration-whiplash

#AI코딩 #코딩에이전트 #슬롭 #SlopCodeBench #소프트웨어공장

> info.json `tags`: AI Engineer · AI slop · AI 코딩 · Claude · Code Summit · Dex Horthy · Factory · HumanLayer · No AI Slop Manifesto · SlopCodeBench · software factory · 덱스 호시 · 소프트웨어 공장 · 슬롭 · 코딩 에이전트

## 트랜스크립트 — ko-orig (Korean, ASR variant=gemini — 한국어 내레이션. 원 발표 발췌 자리는 `[음악]` 표시만(열세 곳 약 3분 44초))

[00:00] AI에게 코드를 맡기는 공장.
[00:02] 슬롭없이 돌릴 수 있을까요?
[00:04] 최고의 모델이 받은 점수부터 보시죠.
[00:06] 16%.
[00:08] 처음 짜는 건 잘하는데 요구사항이
[00:10] 바뀔 때마다 자기 코드를 고쳐 나가게
[00:12] 하면 무너집니다.
[00:13] 요즘 클라우드는 파이썬 2 시절
[00:15] 문법으로 돌아가기까지 했습니다.
[00:17] 그럼 슬롭을 안 내보내는 공장은
[00:19] 어떻게 만들까요?
[00:20] 덱스 호시가 무대에서 내놓은 규칙
[00:22] 12가지와 끝까지 사람이 봐야 하는
[00:24] 이유를 따라가 봅니다.
[00:26] 덱스 호시는 코딩 에이전트를 두고
[00:28] 꾸준히 발표해 온 개발자입니다. 휴먼
[00:30] 레이어를 공동 창업했고 최근 팩토리에
[00:32] 합류했습니다.
[00:33] 지난 6월 그는 소프트웨어 공장이 왜
[00:35] 실패하는가 라는 발표를 했습니다.
[00:37] [음악] 요지는 그래도 코드를
[00:39] 읽으라는 것이었죠.
[00:41] 그사이 데이터가 쌓였습니다. 개발자
[00:43] 22,000명을 분석한 파로스
[00:44] 보고서를 보면
[00:45] 리뷰 없이 넘어가는 PR이 31.3%
[00:48] 늘었습니다. [음악] PR 하나당
[00:50] 사고는 242%, 개발자 한 명당
[00:52] 버그는 54% 늘었습니다.
[01:17] [음악]
[01:21] 그는 결론부터 꺼냅니다. 소프트웨어
[01:22] 공장은 그냥 좋은 엔지니어링이라는
[01:24] 겁니다.
[01:25] AI 이전의 회사를 떠올려 보면
[01:27] 기획자와 엔지니어가 할 일을 트래커에
[01:29] 올리고 누군가 만들고 테스트를 돌리고
[01:31] [음악] PR을 올립니다. CI가
[01:32] 검사하고 사람이 리뷰하고 조금씩
[01:34] 배포하고 새벽 3시에 장애가 나면
[01:36] 모니터링이 사람을 깨웁니다.
[01:38] 에이전트 시대에 바뀌는 건 딱 한
[01:39] 칸입니다. 사람이 만든다가 에이전트가
[01:42] 만든다로 바뀌는 거죠. 트래커,
[01:43] 테스트, CI, 배포는 30년 전부터
[01:45] 있던 것들입니다. 공장을 새로 짓는
[01:47] 게 아니라 원래 공장의 한 칸을
[01:48] 바꾸는 겁니다.
[01:50] 그 한 칸을 바꾸고 나면 공장을 두
[01:52] 방향으로 키웁니다. [음악] 첫째는
[01:54] 압, 압력. 일을 시작시키는
[01:56] 힘입니다.
[02:03] >> [음악]
[02:22] >> 둘째는 뒤 압력입니다. [음악] 이제
[02:23] 만드는 건 몇 분, 몇 시간이면
[02:25] 끝나는데 리뷰와 테스트는 여전히
[02:27] 며칠씩 걸립니다. 그래서 에이전트
[02:29] 코드 리뷰, 에이전트 테스트,
[02:31] CRI와 린터에 투자합니다.
[02:33] 사람이 끼지 않아도 에이전트가 스스로
[02:35] 더 나은 결과를 내게 하는
[02:37] 장치들입니다. [음악]
[02:38] 첫 번째 규칙은 루프입니다. 요즘
[02:40] 유행하는 루프라는 말을 그는 앞
[02:42] 압력과 뒤 압력이 맞물리는 것으로
[02:44] 봅니다. 일은 자동으로 시작되고 사람
[02:47] 손에 닿을 때쯤엔 쉬운 문제는 이미
[02:49] 다 고쳐져 있어야 한다는 겁니다.
[02:51] 두 번째 규칙은 적을 알라. 여기서
[02:53] 적은 모델의 약점입니다. [음악]
[02:55] 아무도 지켜보지 않으면 모델은
[02:57] 코드베이스의 품질을 오래 지키고
[02:58] 개선하는 데 서툴다는 겁니다.
[03:00] 그가 그린 그림입니다. [음악] 한
[03:02] 번에 끝나는 문제를 푸는 실력은
[03:04] 해마다 쭉쭉 올라갔는데 코드베이스를
[03:06] 개선하는 실력은 그 사이 조금밖에
[03:07] 오르지 않았습니다.
[03:43] 슬롭 코드 벤치는 위스콘신대학교
[03:44] 연구실 검증 시험입니다. 문제
[03:47] 36개를 체크포인트 196개로
[03:49] 쪼갰습니다.
[03:50] 첫 명세로 프로그램을 짜고 명세가
[03:52] 바뀔 때마다 자기 코드를 고쳐
[03:53] 나갑니다. 숨은 테스트로 채점하고
[03:56] 슬롭이 얼마나 쌓였는지도 봅니다.
[03:58] 엄격 기준은 앞선 체크포인트의
[04:00] 테스트까지 전부 통과해야 점수를
[04:02] 줍니다. 그 기준으로 1등인
[04:03] GPT-6 아스트라 엑스 하이가
[04:05] 16.33% 196개 중 서른
[04:08] 두개였습니다.
[04:09] 벤치를 이끄는 게이브 올란스키의
[04:11] 정리는 이렇습니다.
[04:12] 프리율은 오르고 슬롭은 줄었지만
[04:14] 슬롭은 사라진 게 아니라 설계
[04:16] 결정으로 자리를 옮겼다. [음악]
[04:18] 대표적인 게 라이브러리입니다.
[04:20] 같은 구현 에이전트에게 라이브러리를
[04:22] 주고 문제를 풀게 하면 라이브러리를
[04:24] 피해 우회하는 비율이 사람이 짠
[04:26] 라이브러리에선 27%, 에이전트가 짠
[04:28] 라이브러리에선 40%였습니다.
[05:04] 엔트로픽은 새 모델 페이블에게 코드
[05:07] 베이스의 주인이라고 알려 주면
[05:08] 깨끗하게 관리한다고 안내합니다.
[05:10] 덱스는 아직 확인 중이라고 했습니다.
[05:12] 그래서 그가 내린 결론은 코드
[05:14] 베이스가 오래 살아야 한다면 사람이
[05:16] 시스템과 코드를 계속 이해하고 있어야
[05:17] 한다는 겁니다.
[05:19] 세 번째 규칙은 만들기 전에
[05:21] 계획하라.
[05:22] 앞에서 30분을 쓰면 리뷰에서 몇
[05:24] 시간을 아낀다는 겁니다.
[05:26] AI 이전에도 아키텍처 리뷰와
[05:28] 스프린트 계획이 있었습니다. 다시
[05:29] 만드는 일을 줄이려고 미리 맞춰 본
[05:31] 거죠.
[05:32] 만드는 게 빨라져도 제대로 하는
[05:34] 리뷰는 여전히 느립니다.
[05:35] 그러니 계획은 지금도 필요하다는
[05:37] 겁니다.
[05:38] 그런데 네 번째 규칙은 반대
[05:40] 방향입니다. 계획을 과하게 하지
[05:42] 말라.
[05:43] 자신도 명세에 여섯 시간을 쓰고 나서
[05:45] 그냥 대충 시킬 걸 그랬다 싶었던
[05:47] 적이 있답니다.
[06:09] >> [음악]
[06:25] [음악]
[06:28] >> 정리하면 바꾸기 어려운 것일수록
[06:30] 앞에서 공을 들이라는 겁니다.
[06:32] 버튼 색은 나중에 바꿔도 되지만
[06:33] 데이터베이스 구조는 그렇지
[06:34] 않으니까요.
[06:36] 다섯 번째는 눈으로 맞춰 보라. 글로
[06:39] 된 긴 계획 대신 [음악] HTML
[06:40] 목업, 표, 차트를 보면서 에이전트와
[06:43] 방향을 맞추라는 겁니다.
[06:44] 그가 공개한 쇼미라는 스킬이 그런
[06:46] 용도입니다. 사람은 수백만 년을
[06:48] 눈으로 살아왔고 글을 읽은 건
[06:50] 5,000년쯤이라면서요.
[06:52] 여섯 번째 규칙. 에이전트가 자기
[06:54] 일을 직접 시험하게 하라. 스크린샷,
[06:56] 브라우저, 영상, 콜 뭐든 좋습니다.
[06:59] iOS 앱을 만든다면 에이전트가 그
[07:01] 앱을 직접 빌드하고 실행하고 [음악]
[07:03] 테스트할 수 있어야 한다는 거죠.
[07:05] 일곱 번째 규칙은 결정론적인 도구로
[07:07] 슬롭과 싸우라는 겁니다. 같은
[07:09] 코드에는 늘 같은 판정을 내리는 린트
[07:11] 규칙 같은 것들입니다. 클라우드
[07:12] 플레어의 수석 엔지니어 딜런 몰로이가
[07:14] 만든 안티 슬롭 저장소에는 에이전트가
[07:16] 슬롭을 못 만들게 막는 규칙이
[07:18] 100개쯤 들어있습니다. 팩토리도
[07:20] ES 린트 플러그인을 냈고 슬롭 코드
[07:22] 벤치의 파이썬 품질 규칙도 가져다 쓸
[07:24] 수 있습니다. 여덟 번째는
[07:25] 의외입니다. 슬롭도 도구다. 바이브
[07:28] 코딩이나 프로토타입처럼 사람들이
[07:29] 원하기는 하는지부터 알아봐야 할 땐
[07:31] 대충 만든 코드도 괜찮습니다.
[07:33] 아홉 번째. 모델이 실험하게 하라.
[07:35] 포스트 호그, 스태시그 같은 기능
[07:37] 플래그 시스템을 지워주면 이것저것 켜
[07:39] 보고 더 나은 쪽을 고를 수
[07:40] 있습니다. 열 번째로 시간이 갈수록
[07:42] 쌓이게 하라. 전부 평가하고 지난
[07:44] 세션에서 배우라는 겁니다.
[07:46] 열 한 번째는 포즈를 하나로 모으라.
[07:48] 코드는 깃허브에 모였는데 계획과
[07:50] 결정은 아직 여기저기 흩어져 있다고
[07:51] 싶습니다.
[07:52] >> [음악]
[08:05] >> 마지막 12번째
[08:09] 규칙은 전부 살 수는 없다.
[08:11] 샌드박스같은 인프라는 사거나 만들면
[08:14] 되고,
[08:25] 클라우드 코드나 코덱스, 팩토리 같은
[08:27] 제품을 사거나 가볍게 직접 짤 수
[08:29] 있습니다.
[08:30] 개발 환경은 팀마다 너무 달라서 직접
[08:32] 갖고 있지 않으면 마찰이 큽니다.
[08:55] 공장의 목적은 사람의 지렛대를 키우는
[08:57] 것, 우리 시간을 가장 값지게 쓰는
[08:59] 것이라고 했습니다.
[09:00] 이야기는 여기서 슬롭 자체로
[09:01] 넘어갑니다.
[09:03] 이 무대에서 덱스는 안티 슬롭 선언을
[09:05] 공개했습니다. 코드 서밋의 연사와
[09:07] 참가자들이 함께 쓴 글입니다.
[09:09] 2001년 엔지니어 17명이 스키
[09:11] 산장에 모여 애자일 선언을 썼던
[09:13] 것처럼 이번엔 AI 슬롭에 맞서는
[09:15] 선언을 쓰자는 겁니다. [음악]
[09:17] 다섯 가지 가치는 이렇습니다.
[09:18] 산출물보다 결과, 속도보다 이해,
[09:21] 모델의 첫 초안보다 내 생각,
[09:23] 쉬운 일보다 더 나은 일, 출력을
[09:25] 땜질하기 보다 시스템을 고치는 것.
[09:27] 선언에 슬롭의 정의가 나옵니다.
[09:29] 만드는 데 들인 노력보다 받는
[09:31] 사람에게 이해하라고 요구하는 노력이
[09:32] 더 큰 것.
[09:33] AI를 썼다고 다 슬롭은 아닙니다.
[09:35] 품질과 읽는 사람의 경험을 책임지지
[09:37] 않고 AI 출력을 넘길 때 슬롭이
[09:39] 됩니다.
[09:57] [음악]
[10:04] 선언의 첫 믿음도 같은 얘깁니다.
[10:06] 에이전트 때는 한 사람이 평생 리뷰할
[10:08] 수 있는 양보다 많은 일을 하루만에
[10:09] 만들어냅니다.
[10:11] 슬롭이 생기는 이유도 꼽습니다.
[10:13] 빼기보다 더하기에 쏠린 도구, 사람의
[10:15] 한계를 넘으라고 몰아붙이는 압박,
[10:17] 그리고 복리.
[10:18] [음악] 지식 베이스와 채팅, 코드의
[10:19] 슬롭이 쌓일수록 다음 에이전트가 그걸
[10:21] 읽고 베낍니다.
[10:23] 그러다 팀은 슬롭과 싸울 의지마저
[10:24] 잃습니다.
[10:25] 그래서 서명한 사람들은 다짐합니다.
[10:27] 모델과 일해도 생각은 내가 하고
[10:29] AI가 얼마나 도왔든 내 보낸 것은
[10:31] 내가 책임진다.
[10:32] 에이전트가 쓴 걸 보낼 땐 그렇다고
[10:34] 밝히고 중요한 부분은 확인한다.
[10:36] 슬롭을 받으면 친절하게 말해주고 먼저
[10:39] 검토해 달라고 한다.
[10:40] 덱스는 자기도 그런 말을 들어본 적이
[10:42] 있다고 털어놨습니다. [음악]
[10:44] 그럼 코드를 전부 밀라는 걸까요?
[10:47] 마지막 대목은 조금 더 현실적입니다.
[10:49] [음악]
[11:06] [음악]
[11:20] 중요한 건 코드 줄수나 머지한 PR
[11:22] 수, 동시에 돌리는 에이전트 수가
[11:24] 아니라 무엇을 내보냈고 누가 쓰고
[11:26] 그게 어떻게 돕는가입니다.
[11:28] [음악] 검토하지 않은 출력이 다
[11:29] 나쁜 것도 아닙니다. 한 번에 던지는
[11:31] 프롬프트나 바이브 코딩은 지렛대가 큰
[11:33] 도구입니다.
[11:35] 슬롭이 나쁜 건 결과를 망칠
[11:36] 때입니다. 쓸모 있는 제품,
[11:38] 유지보수할 수 있는 시스템, 서로의
[11:40] 시간을 아끼는 일을 망칠 때요.
[11:42] 그리고 선언의 마지막 문장입니다.
[11:44] 우리 중 누구도 이걸 다 알아내지
[11:45] 못했다. 각자 무엇을 받아들이고
[11:48] 무엇을 거절할지 다시 배우는 중이다.
[11:51] 처음 숫자로 돌아가 보겠습니다.
[11:52] 최고의 모델도 코드를 계속 고쳐
[11:54] 나가는 시험에서는 16%였습니다.
[11:57] 그래서 덱스의 공장은 셋으로
[11:58] 정리됩니다. 앞에서 밀고 뒤에서 거는
[12:00] 루프, 기계가 잡을 건 기계에게
[12:02] 맡기는 도구, 그리고 사람이 끝까지
[12:04] 쥐는 판단.
[12:06] 여러분의 공장에서 사람이 마지막으로
[12:07] 보는 건 무엇인가요? 코드인가요,
[12:09] 계획인가요? 아니면 아무것도 없나요?

## 트랜스크립트 — en-orig (English, ASR timing-optimized — 내레이션 자리는 영어 더빙 ASR(인용하지 않음, 판독 대조용), 발췌 자리 아홉 곳은 Dex Horthy 원음(단일 트랙, 교차 확인 없음). 두 트랙 모두 무캡션 다섯 곳 약 47초)

[00:00] Can Slop, the factory that delegates
[00:02] code to AI, really handle this? Let's
[00:04] start by looking at the score received
[00:06] by the best model. It performs well at
[00:08] first, but if you force it to fix its
[00:10] own code every time requirements change
[00:12] , it collapses. Recently, Claude has
[00:14] even gone so far as to revert to syntax
[00:16] from the Python 2 era. So, how do we
[00:17] build a factory that doesn't send Slop?
[00:20] Let's follow the 12 rules Dex Tosh
[00:22] presented on stage and the reasons why
[00:23] humans must review code until the very
[00:25] end.
[00:26] Dex Tosh is a developer who has
[00:27] consistently given presentations on
[00:29] coding agents. He co-founded Human Layer
[00:31] and recently joined Factory. Last June,
[00:34] he gave a presentation titled "Why
[00:36] Software Factories Fail." The main point
[00:38] was that you should still read the code
[00:40] . In the meantime, data has accumulated
[00:42] . According to a PASS report analyzing
[00:45] 22,000 developers, 31.3%of PRs were
[00:47] passed without review. The number of
[00:50] incidents per PR increased by 242%, and
[00:52] the number of failures per developer
[00:54] increased by 54%.
[00:57] Dex is the anti-software factory guy.
[00:59] Dex hates software factories. I actually
[01:02] love software factories. I'm a huge fan
[01:04] . Uh, the title was probably more along
[01:06] the lines of, you know, there are
[01:08] certain things you could do in your
[01:09] software factory that would cause it to
[01:11] fail. And here's what those things might
[01:14] be.
[01:15] And please, he starts with the
[01:19] conclusion.
[01:22] A software factory is simply good
[01:24] engineering.
[01:25] If you think about companies before AI,
[01:27] planners and engineers would put their
[01:29] tasks on a tracker, someone would build
[01:30] it, run tests, and upload it. C inspects
[01:33] it, humans review it, and deploy it in
[01:34] small increments; if a failure occurs at
[01:36] 3 AM, monitoring wakes people up. In the
[01:38] era of agents, only one element changes
[01:40] . It shifts from humans building to
[01:42] agents building. Trackers, tests, and C
[01:44] deployment have been around for 30 years
[01:46] . You aren't building a new factory; you
[01:48] are changing just one element in the
[01:49] existing one.
[01:50] Once you change that one element, you
[01:52] expand the factory in two directions.
[01:54] The first is forward, pressure, and the
[01:56] force that initiates it.
[02:07] And we take all the incidents that
[02:08] happen so that when I get page 3 in the
[02:10] morning, I'm looking at a pull request
[02:11] that we think is going to solve it. Not
[02:13] just uh, stack trace about nothing.
[02:16] The
[02:22] second is back pressure. Now, building
[02:24] it takes only a few minutes or hours,
[02:26] but reviews and testing still take days
[02:29] . So, we invest in agent code reviews,
[02:31] agent testing, C, and linters. These are
[02:34] mechanisms that enable agents to produce
[02:36] better results on their own without
[02:37] human intervention. The first rule is
[02:39] the loop. He views the currently
[02:41] trending term "loop" as the interplay
[02:43] between front pressure and back pressure
[02:45] . The idea is that work starts
[02:46] automatically, and by the time it
[02:48] reaches human hands, all problems should
[02:50] already be fixed. The second rule is
[02:52] know the enemy. Here, the enemy is the
[02:54] model's weakness. If no one is watching
[02:56] , the model will be clumsy at
[02:57] maintaining and improving the quality of
[02:59] the codebase for a long time. This is
[03:01] the picture he drew. The ability to
[03:03] solve problems in a single go has
[03:04] steadily increased year after year, but
[03:06] the ability to improve the codebase has
[03:07] only increased slightly during that time
[03:09] .
[03:10] I didn't have a benchmark. Now I have a
[03:11] benchmark, uh, that basically has the
[03:13] model solve problems and checkpoints.
[03:15] Like, a model can clone all of Excel or
[03:17] Redis in a couple days, uh maybe even a
[03:19] couple hours now with, like, agent
[03:21] swarms. Uh, but that requires knowing
[03:23] the entire problem in advance. And most
[03:25] of us don't write software that way.
[03:27] Most of us ship a feature, and then ship
[03:28] another feature, and then ship another
[03:30] feature. And if you're building by hand
[03:32] without AI along the way, you say, "Oh,
[03:33] that's a bad abstraction. We need to
[03:34] centralize this. We need to remove this
[03:36] . And so, this is a benchmark that
[03:38] measures a model's ability to evolve a
[03:40] code base over time. The
[03:43] >> Slop Code Benchmark is an exam developed
[03:44] in collaboration with the University of
[03:46] Wisconsin lab. We will break down 36
[03:48] problems into 196 checkpoints. You write
[03:50] a program based on the initial
[03:51] specification and modify your code
[03:53] whenever the specification changes. It
[03:54] is graded using hidden test questions
[03:56] and also checks how many 'slop'(slopes)
[03:57] have accumulated. The strict standard
[03:59] requires passing all tests up to the
[04:01] previous checkpoint to receive a score.
[04:02] Based on that standard, the top-ranked
[04:05] GPT 6 Astra X-Ha had 16.33%(33%),
[04:07] passing 32 out of 196 questions. Gey Bo
[04:09] Olansky, who leads the benchmark,
[04:10] summarizes it as follows: The free rate
[04:12] increased and slopes decreased, but
[04:14] slopes did not disappear; they simply
[04:15] moved to a different position due to
[04:17] design decisions. A prime example is
[04:19] libraries. You give a library to the
[04:21] same implementation agent and have them
[04:23] solve the problems In this case, the
[04:25] rate of bypassing libraries was 27%for
[04:27] human-written libraries and 40%for
[04:29] agent-written libraries.
[04:42] Way, you know, six months ago models are
[04:44] better than they are in today's models.
[04:46] So it almost feels like we're like the,
[04:48] the slop is amplifying over time.
[04:50] Um, and clot and glit Python 3 in Python
[04:54] 2 style. So we have, you know, per s
[04:56] format strings are back, and they will
[04:58] not use f strings by default anymore. So
[05:00] , things to be aware of.
[05:04] Antropic advises that if you let the new
[05:06] model, Fable, know that it is the owner
[05:08] of the codebase, it will keep it clean.
[05:10] Dex said it was day. Therefore, his
[05:13] conclusion is that if the codebase is to
[05:15] live a long time, humans must continue
[05:17] to understand the system and the code.
[05:19] The third rule is to plan before
[05:21] building. Spending 30 minutes beforehand
[05:24] saves several hours in reviews. Even
[05:26] before AI, there were architecture
[05:28] reviews and sprint planning. They
[05:29] aligned in advance to reduce rebuilding
[05:31] . Even if building becomes faster,
[05:33] proper reviews still feel slow.
[05:35] ...so, the point is that planning is
[05:37] still necessary. However, the fourth
[05:39] rule goes in the opposite direction: do
[05:42] not over-plan. He himself once said that
[05:44] after spending six hours on a
[05:45] specification, he regretted not just
[05:47] having it done roughly.
[05:52] 50%chance you send a couple more promps
[05:54] and then it's good.
[05:55] You could spend 5 hours handwriting a
[05:57] detailed spec and maybe there's a 10%
[05:59] chance you have to change afterward.
[06:01] Or you could write all the code by hand
[06:03] in 20 hours and then there's like a 0%
[06:04] chance. Well, the 0%chance you have to
[06:06] rework it because of something the agent
[06:07] did. You know, people still make
[06:09] mistakes too.
[06:10] Um, but I think about this in terms of
[06:12] expected pain. Like, how likely will
[06:14] this have to change later, how hard will
[06:17] it be to change?
[06:20] I don't argue with the model during
[06:21] planning about what color it is, but do
[06:23] make our database schemas right and
[06:25] stuff like that.
[06:27] To summarize, the more difficult a place
[06:29] is to change, the more effort you should
[06:31] put into it upfront. You can change a
[06:33] button later, but the database structure
[06:34] ...Because that is not the case. The
[06:36] fifth rule is to align with the agent
[06:38] visually. Instead of a long-term,
[06:39] labor-intensive plan, you should align
[06:41] your direction with the agent by looking
[06:43] at HTML mockup sheets. The" Show Me "
[06:45] skill he revealed serves this purpose.
[06:47] He noted that humans have lived with
[06:48] their eyes for millions of years, while
[06:50] reading text has only been around for
[06:51] about 5,000 years.
[06:53] The sixth rule: Have the agent test
[06:54] their own work. Screens, browsers,
[06:57] videos, files—anything is fine. If you
[06:59] are creating an iOS app, the agent must
[07:01] be able to build, run, and test that app
[07:04] themselves.
[07:05] The seventh rule is to fight the slope
[07:07] with deterministic tools. These are
[07:09] things like lint rules that always make
[07:11] the same judgment on the same code. The
[07:13] Anti-Slope Place, created by Cloud
[07:14] Player's chief engineer Diller Molloy,
[07:16] contains about 100 rules that prevent
[07:18] agents from creating slopes.
[07:19] Factory has also released an ES plugin,
[07:21] and you can use the Python quality rules
[07:23] from Slope Code Bench. The eighth rule
[07:25] is [unclear]. The slope is also a tool.
[07:28] Like Vibe Coding or Prototype, you must
[07:29] first find out if people want it. At
[07:31] that time, even roughly made code is
[07:33] fine. Let the ninth model experiment. If
[07:36] you clear out a feature-based system
[07:37] like Post Hog Stash, you can turn
[07:39] various things on and choose the better
[07:41] one. Tenth, let it accumulate over time
[07:43] . This means evaluating everything and
[07:45] learning from the previous session.
[07:46] Eleventh, consolidate the Forge into one
[07:48] place. The code is gathered in the Turbo
[07:50] , but it seems that plans and decisions
[07:51] are still scattered here and there.
[08:07] Maybe we get the answer. So, like
[08:08] centralizing all of your designs and
[08:10] decisions, and like whatever you have,
[08:11] like Notion and Google Docs, and
[08:12] whatever it is, you should try to bring
[08:14] those things as close as possible
[08:15] together. Finally, the twelfth point is
[08:16] that you cannot buy everything.
[08:22] Infrastructure like a sandbox can be
[08:24] bought or built, and for HANS, you can
[08:26] buy products like Claude Code, Codex, or
[08:28] Factory, or lightly write it yourself.
[08:33] If you have developed it yourself, it
[08:34] varies so much from team to team that
[08:35] friction is significant if you do not
[08:36] possess it directly. Don't think anyone
[08:37] can sell you verification of your code.
[08:41] Only you know if you have hundreds of
[08:42] engineers and hundreds of repos; you
[08:44] have those opinions and You know how to
[08:45] test your code.
[08:47] Not just a black box you can buy.
[08:55] It was said that the purpose of the
[08:56] factory is to increase human leverage
[08:58] and to make the most valuable use of our
[09:00] time. From here, the story shifts to the
[09:02] slop itself. At this unit, Dex released
[09:04] the Anti-Slop Manifesto. It is a text
[09:07] written jointly by speakers and
[09:08] participants from Code Service. Just as
[09:10] 17 engineers gathered at a ski lodge in
[09:12] 2001 to write the Agja Manifesto, the
[09:13] idea is to write a declaration this time
[09:15] to stand against AI slop. The five
[09:17] values are as follows: Results over
[09:19] output, understanding over speed, my
[09:20] thoughts over the first few seconds of a
[09:22] model, doing better work over easy work
[09:24] , and fixing the system rather than
[09:26] patching up the output.
[09:27] A sailor's definition of slop appears:
[09:29] when the effort required of the
[09:30] recipient to understand is greater than
[09:32] the effort put into making it.
[09:33] Just because AI is used does not mean it
[09:35] is slop.
[09:38] It becomes slop when AI output is handed
[09:39] over without taking responsibility for
[09:40] quality and the reader's experience.
[09:42] cannot replace human judgment.
[09:45] It can only amplify our judgment, or uh
[09:47] maybe perhaps our lack of judgment in
[09:49] certain cases.
[09:51] Um, and the slop is asymmetric.
[09:53] Um, the cost of producing line PR 10-
[09:56] page doc is approaching the cost of
[10:01] constant.
[10:04] The sailor's initial belief is the same
[10:06] story. As an agent, one person produces
[10:08] more work in a single day than can
[10:09] review in a lifetime. The reasons for
[10:12] slops were also cited. Tools skewed
[10:14] toward addition rather than subtraction
[10:15] , pressure pushing beyond human limits,
[10:17] and compound interest, Zizic Base and
[10:19] chat. As code slops accumulate, the next
[10:21] agent loses them and cuts them off.
[10:23] Eventually, the team loses even the will
[10:24] to fight against the slops. Therefore,
[10:26] those who signed make a pledge: I do the
[10:27] thinking, even if it involves the model
[10:29] , and I take responsibility for what is
[10:31] sent out, regardless of how much the AI
[10:32] does. When sending what the agent wrote
[10:34] , I state that and verify the important
[10:36] parts. When receiving slops, I explain
[10:38] them kindly and ask them to review them
[10:40] first. Dex said he was on the side that
[10:41] had heard such things himself; is he
[10:42] suggesting that the entire
[10:45] discussion code should be handled by
[10:46] Will Gra?
[10:47] The last part is a bit more realistic.
[11:04] AI
[11:07] agent reviewers, lters, verifiers useful
[11:10] ,
[11:12] excuse me, they are not sufficient.
[11:21] Important It is not about the number of
[11:22] lines of code, the remaining ones, or
[11:24] the number of agents running
[11:25] simultaneously, but what was sent out,
[11:26] who wrote it, and how it helps.
[11:28] Not all unreviewed output is bad.
[11:31] Prompts thrown all at once or vibe
[11:33] coding are tools with great leverage.
[11:35] Slop is bad when it ruins the results.
[11:38] When it ruins a useful product, a
[11:39] maintainable system, and work that saves
[11:41] each other's time.
[11:42] And here is the last sentence of the
[11:44] declaration: None of us have figured
[11:46] this all out. Each of us is relearning
[11:48] what to accept and what to reject.
[11:51] Let's go back to the initial numbers.
[11:53] Even the best model scored 16%in the
[11:54] test of continuously fixing code.
[11:57] So, Dex's factory is organized
[11:58] vertically. A loop that pushes from the
[12:00] front and filters from the back. Tools
[12:01] that leave what the machine should catch
[12:03] to the machine. And judgment that humans
[12:04] hold onto until the end.
[12:06] What is the last thing humans look at in
[12:08] your factory? The code? The plan? Or
[12:11] nothing at all? M.
