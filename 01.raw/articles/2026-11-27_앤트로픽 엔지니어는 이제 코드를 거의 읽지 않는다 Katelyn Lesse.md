---
title: "앤트로픽 엔지니어는 이제 코드를 거의 읽지 않는다 | Katelyn Lesse"
type: video
source: https://www.youtube.com/watch?v=sBIBmGO1nl0
site: youtube.com
author:
  - "[[Tech Bridge]]"
duration: 10:47
published: 2026-11-27
created: 2026-11-28
description: "Tech Bridge 한국어 해설 10:47, 공식 챕터 10, 한국어 내레이션(ko-orig) + 영어 더빙 ASR(en-orig — 인용하지 않음). Anthropic에서 Claude Platform 엔지니어링을 이끄는 Katelyn Lesse의 The Pragmatic Engineer 인터뷰를 따라간다 — CPU가 모자라 시작한 메시지 API의 Python → Rust 재작성(다섯에서 여섯 달), 프롬프트와 응답을 볼 수 없는 상태에서의 그림자 트래픽 검증, 사람이 봐야 할 변경을 고르는 Claude 분류기, 알림을 먼저 받는 Claude, 직접 배포하는 PM, 코딩 면접 폐지, 정체성 위기. ⚠️ Katelyn Lesse의 원음은 한 마디도 캡션에 잡히지 않았고 인터뷰 발췌 자리 다섯 곳(약 3분 57초)은 두 트랙 모두 무캡션 — PR 80% 대목의 본문 · 중간에 다 버린 것이 무엇인지 · 코딩 면접을 없앤 이유가 거기 든다."
tags:
  - clippings/youtube
---

**Source URL**: https://www.youtube.com/watch?v=sBIBmGO1nl0
**Channel**: Tech Bridge · **Duration**: 10:47 · **Published**: 2026-11-27

> **게시일.** info.json `upload_date` **`20261127`**, `timestamp` 1795770036(= 2026-11-27 09:00:36 UTC = **2026-11-27 18:00 KST**), `availability`=`public`. 2026-11-28 회차(09:10 KST)에서 처음 잡혔다 — 게시 열다섯 시간 뒤. 파일명에서 `|` 는 뺐다.
>
> **오디오 트랙과 자막 — 인용 규칙.** ⚠️ 이 회차에도 yt-dlp가 영상 포맷 목록을 받지 못해(info.json `formats` 비어 있음) **오디오 트랙 구성과 메타 `language`(`None`)를 확인하지 못했다.** 자막 트랙의 성격은 내용으로 판정했다. 수동 자막 없음. `ko` = `ko-orig`(파일 동일, `kind=asr&lang=ko&variant=gemini`) — **한국어 내레이션** 이다. `en-orig`(`kind=asr&lang=en&variant=timing-optimized`)는 **영어 더빙의 ASR** 이다 — 첫 줄부터 내레이션의 영어 번역이고(*This is how Anthropic builds code now.*) 문장 단위가 ko-orig와 같은 초에 맞물리며, 인터뷰이를 3인칭(*Caitlin says · Her point is*)으로 부른다. **en-orig의 더빙 문장은 인용하지 않았고 판독 대조용으로만 썼다.** 한국어 인용은 전부 ko-orig의 내레이션이다. 429 없음(`--sleep-subtitles 8`).
> ⭐ **Katelyn Lesse와 진행자의 원음은 한 마디도 잡히지 않았다.** 두 트랙 어디에도 영어 원음으로 볼 줄이 없다. ko-orig 06:02 줄 머리의 `>>`(화자 전환 표시)가 발췌가 끝나고 내레이션으로 돌아온 자리임을 알려 줄 뿐이다. **이 편에는 본인 인용이 없다** — *케이틀린은 … 라고 말합니다* 꼴의 문장은 전부 내레이션이 옮긴 말이다.
>
> **무캡션 구간(`gaps.py` 4.5초 기준).** en-orig 다섯 곳: 02:28~03:11 · 04:10~06:02 · 07:34~08:02 · 08:42~09:02 · 09:40~10:12 — 합쳐 약 3분 57초. ko-orig는 같은 자리이고 마지막 것만 09:50의 `[음악]` 표시로 둘로 나뉜다(여섯 조각).
> ⚠️ **이 구간들은 내용 미상이다.** 여기에 드는 것: *너무 느렸습니다* 뒤 — 조각내기 대신 무엇을 택했는지의 말(02:28~03:11, 챕터 제목은 *한 번에 전부, 그림자로 검증*) · **진행자의 *코드는 별로 들여다보지 않았다는 건가요* 에 대한 답과 챕터 *PR 80%는 꼼꼼히 읽지 않았다* 의 본문 전체, 그리고 챕터 *중간에 다 버리고 다시* 의 앞부분(04:10~06:02, 1분 53초)** — 80%는 도입부 요약으로만 있고, 무엇을 버리고 다시 했는지는 캡션에 없다 · 알림 잡음 거르기 뒤(07:34~08:02) · **코딩 면접을 없앤 이유(08:42~09:02)** — 도입부가 *이유까지 따라가 봅니다* 라고 예고하지만 이유의 말은 캡션에 없다 · 정체성 위기에 대한 블로그 글 또는 답의 본문(09:40~10:12).
>
> **ASR 판독(ko-orig → 판독, 괄호는 근거).** *엔트로픽* → Anthropic(제목 · 설명란), *케이틀린 · 케이트린* → Katelyn Lesse(제목 · 설명란 · tags — 더빙은 *Caitlin*), *클라우드의 모든 토큰 · 클라우드 앱 · 클라우드 코드 · 클라우드 분류기 · 클라우드들에게 · 클라우드에게 · 클라우드가 먼저 받아서* → Claude · Claude Code(설명란 *Claude의 모든 토큰이 지나가는 API* · *Claude 분류기* · *알림을 먼저 받는 Claude*, 02:15에는 *클로드* 로 바로 적힌다), *뭐라고 있었을까요* → 뭐 하고 있었을까요(더빙 *what were the engineers doing*), *C++로 하자고 있으면* → 하자고 했으면, *결과가 매번 달라지는 일할 때는* → 일을 할 때는, *단건*(07:21~07:25, 두 번) → 당번(추정 — 온콜 당번. 더빙은 *task*), *슬랙에서 콜로 도와 주고받으며* → Slack에서 Claude와 주고받으며(추정 — 더빙은 *by collaborating via Slack* 로 줄인다), *PM이 만들었던 사람 없는 에이전트가 고쳤든* → PM이 만들었든 사람 없이 에이전트가 고쳤든(더빙 *Whether built by a PM or fixed by an agent without human intervention*), *고 언어* → Go.
> ⚠️ **판독하지 못한 것.** ① *클라우드의 CPU를 더 달라고 하는 일이 어려운 대화가 됐습니다*(01:09~01:12) — Claude용 CPU인지 클라우드(cloud) CPU인지 캡션으로 가를 수 없다(더빙은 *cloud CPU*). ② **06:02의 잘린 문장** *는 일을 실행할 때만 띄우고 세션은 따로 저장합니다* — 주어가 무캡션 구간에 있다. 뒤따르는 자격증명 · 프록시 · 샌드박스 문장과 함께 **무엇을 설명하는 대목인지 알 수 없다**(챕터는 *중간에 다 버리고 다시*). ③ *CPU 사용량은 평균 1/3 정도로 줄었습니다*(06:13~06:15) — 무엇의 CPU인지, 1/3**로** 인지 1/3**만큼** 인지 문장만으로는 정할 수 없다(더빙 *dropped to about one-third*). ④ *그래서 기준은 결국 영역입니다*(09:26) — *영역* 이 무엇의 번역인지 모른다(더빙 *the scope of the work*). ⑤ 진행자의 이름은 캡션에도 설명란에도 없다.
>
> ⚠️ **직함.** 내레이션은 *플랫폼 엔지니어링 총괄*, 설명란은 *Claude Platform 엔지니어링을 이끄는*. 같은 뜻으로 읽었다.
>
> ⚠️ **해설이고 2차 전달이다.** 위키는 원본 인터뷰(The Pragmatic Engineer, `9oNvKMd7xJo`)와 설명란의 블로그 글(*The new set of problems for engineers to solve*, 2026.10.25)을 열지 않았다. 매체 이름과 글 제목 · 날짜는 설명란 표기다. *그림자 트래픽* 이라는 말은 설명란과 tags(`shadow traffic`)에 있고 내레이션은 *그림자처럼 · 그림자 시스템* 이라고만 한다.


## 설명란

Claude의 모든 토큰이 지나가는 API를 Python에서 Rust로 통째로 다시 짰습니다. 그런데 에이전트가 연 PR의 80%는 꼼꼼히 읽지 않았다고 합니다. 앤트로픽에서 Claude Platform 엔지니어링을 이끄는 Katelyn Lesse가 The Pragmatic Engineer 인터뷰에서 들려준, 2026년 앤트로픽이 소프트웨어를 만드는 방식입니다.

CPU가 모자라 시작된 Rust 재작성, 프롬프트와 응답을 볼 수 없는 상태에서 새 시스템을 검증한 그림자 트래픽, 사람이 봐야 할 변경을 고르는 Claude 분류기, 새벽 장애 알림을 먼저 받는 Claude, 직접 배포하는 PM, 그리고 코딩 면접을 없앤 이유까지 따라갑니다.

타임라인
0:00 앤트로픽은 이제 코드를 이렇게 만든다
0:27 CPU가 모자랐다
1:22 러스트를 아는 사람이 없어도
2:20 한 번에 전부, 그림자로 검증
4:02 PR 80%는 꼼꼼히 읽지 않았다
5:24 중간에 다 버리고 다시
6:23 사람이 빠지는 자리
7:21 새벽 장애는 Claude가 먼저
8:34 코딩 면접을 없앴다
9:29 코드를 안 치면 나는 누구인가

참고
원본 인터뷰: https://www.youtube.com/watch?v=9oNvKMd7xJo
Katelyn Lesse, The new set of problems for engineers to solve (2026.10.25): https://www.katelynlesse.com/blog/new-problems-for-engineers-to-solve

#Anthropic #ClaudeCode #Rust #AI에이전트 #코딩에이전트

> info.json `tags`: AI 에이전트 · Anthropic · Claude · Claude Code · Katelyn Lesse · Pragmatic Engineer · Python · Rust · shadow traffic · 그림자 트래픽 · 러스트 · 앤트로픽 · 코드 리뷰 · 코딩 면접 · 코딩 에이전트 · 클로드

## 트랜스크립트 — ko-orig (Korean, ASR variant=gemini — 한국어 내레이션. Katelyn Lesse · 진행자의 원음은 한 마디도 잡히지 않았다(발췌 자리 무캡션, 09:50에 `[음악]` 표시 하나))

[00:00] 엔트로픽은 이제 코드를 이렇게
[00:02] 만듭니다.
[00:03] 클라우드의 모든 토큰이 지나가는
[00:04] API를 통째로 새로 짰는데
[00:06] 에이전트가 올린 PR의 80%는
[00:08] 꼼꼼히 읽지 않았습니다.
[00:10] 파이썬으로 된 핵심 층을 러스트로
[00:12] 옮기는 데 걸린 시간은 다섯에서 여섯
[00:14] 달.
[00:14] 핵심 팀은 몇 명 뿐이었습니다.
[00:16] 코드를 다 읽지도 않고 무엇을 믿고
[00:18] 배포했을까요? 그리고 그동안
[00:20] 엔지니어들은 뭐라고 있었을까요?
[00:22] 플랫폼 엔지니어링 총괄 케이틀린의
[00:24] 이야기로 코딩 면접을 없앤 이유까지
[00:26] 따라가 봅니다.
[00:28] 케이틀린의 팀은 클라우드의 모든
[00:29] 토큰이 지나가는 메시지 API를 맡고
[00:31] 있습니다. 요청이 들어오면 먼저
[00:33] 인증을 거치고 코어 API에서
[00:34] 토큰화, 과금, 안전 검사를 한 뒤
[00:37] GPU로 내려갑니다.
[00:38] 클라우드 앱도, 클라우드 코드도 전부
[00:40] 외부 고객과 같은 이 API 위에서
[00:42] 돌아갑니다. 문제는 이 층이 파이썬
[00:44] 모놀리스였다는 겁니다.
[00:45] 처음엔 Google Cloud 한
[00:46] 리전에서만 돌았습니다. 3년쯤 전
[00:48] API를 처음 만든 건 연구 팀과
[00:50] 섞여 일하던 아주 작은 팀이었고
[00:52] 연구자들의 언어가 파이썬이었습니다.
[00:54] 그런데 요청이 폭증했습니다. 올해
[00:56] 초에는 슈퍼볼 광고까지 내보냈습니다.
[00:58] 광고를 보고 바로 API를 붙이는
[00:59] 사람은 없겠지만 앱을 깔아보는 사람은
[01:01] 많고 그 요청도 전부 이 API를
[01:03] 지납니다. 케이틀린은 커리어 내내
[01:05] CPU는 돈만 내면 얼마든지 늘릴 수
[01:07] 있는 자원이었다고 말합니다.
[01:09] 그런데 처음으로 클라우드의 CPU를
[01:11] 더 달라고 하는 일이 어려운 대화가
[01:12] 됐습니다. 다른 리전을 늘리고 작은
[01:14] 효율과 인프라 최적화도 찾았습니다.
[01:17] 그래도 부족했습니다.
[01:18] 결국 한 엔지니어가 말을 꺼냈습니다.
[01:20] 완전히 다른 걸 해 보자고. 러스트를
[01:21] 써 보자고요.
[01:23] 그런데 팀에는 러스트를 많이 써 본
[01:24] 사람이 거의 없었습니다. 사실
[01:26] 엔트로픽은 작년부터 새 서비스를 고
[01:28] 언어로 만들고 있었습니다. 효율과
[01:30] 개발 경험 사이의 절충이었습니다.
[01:32] 그때는 모델이 언어 차이를 다 메워
[01:34] 줄 만큼은 아니어서 사람이 다루기
[01:36] 편한 언어가 여전히 중요했습니다.
[01:38] 그런데 올해 모델이 좋아지면서 계산이
[01:39] 바뀌었습니다. 구현 세부는 모델이 더
[01:41] 맡을 수 있게 됐으니까요.
[01:43] 케이틀린은 C++로 하자고 있으면
[01:45] 그만둔 엔지니어가 꽤 나왔을 거라며
[01:47] 웃습니다.
[01:48] 러스트에는 장점이 하나 더
[01:49] 있었습니다. 컴파일할 때 잡아내는
[01:51] 검사가 아주 많습니다. 사람이 손으로
[01:53] 짤 때는 이게 답답한 장벽이었지만
[01:55] 에이전트가 짤 때는 오히려 믿을
[01:57] 근거가 됩니다.
[01:58] 케이틀린의 말로는 결과가 매번
[02:00] 달라지는 일할 때는 검증할 수 있게만
[02:02] 만들어두면 크게 유리합니다.
[02:04] 그럼 엔지니어는 러스트를 얼마나
[02:06] 알아야 했을까요? 케이틀린은 75대
[02:08] 25라고 답합니다. 75는 모델이
[02:10] 짜고 문법은 몰라도 되는 부분,
[02:12] 25는 궁금해서 모델에게 물어보며
[02:14] 배우는 부분입니다.
[02:15] 클로드가 코드를 짜주는 게 절반,
[02:17] 무슨 코드인지 가르쳐 주는 게 나머지
[02:19] 절반이라고 했습니다.
[02:21] 처음 계획은 시스템을 조각조각 내어
[02:23] 러스트로 옮기는 것이었습니다.
[02:25] 너무 느렸습니다.
[03:11] 새 구조에서 요청은 얇은 파이썬
[03:13] 앞문으로 들어와 원래 파이썬
[03:14] 시스템에서 처리됩니다.
[03:16] 동시에 같은 요청이 러스트 시스템에도
[03:18] 그림자처럼 흘러가고 두 결과를
[03:20] 비교합니다.
[03:21] 비교에는 걸림돌이 하나 있었습니다.
[03:23] 엔트로픽은 사용자의 프롬프트도,
[03:25] 모델의 응답도 들여다보지 않습니다.
[03:27] 결과가 달라도 무엇이 왜 다른지 원본
[03:29] 데이터를 열어볼 수가 없는 겁니다.
[03:31] 그래서 두 군데만 비교했습니다.
[03:33] 추론으로 내려가기 직전까지의 처리가
[03:34] 같은지, 그리고 돌아올 때 토큰 수가
[03:36] 같은지.
[03:37] 그리고 매일 모델에게 묻습니다. 오늘
[03:39] 파이썬과 러스트의 결과가 다른 요청이
[03:41] 몇 건이었나.
[03:43] 그 차이를 줄이고 줄이고 또 줄여서
[03:45] 거의 완벽해졌을 때 러스트를 실제로
[03:47] 켜기 시작했습니다.
[03:50] 그 뒤에도 한 동안 파이썬 앞문을
[03:51] 남겨뒀습니다. 러스트가 에러를 내면
[03:53] 파이썬으로 돌아가게요.
[03:55] 조금 느려도 응답이 아예 없는
[03:57] 것보다는 낫다는 판단이었습니다.
[03:59] 충분히 믿게 된 뒤에야 앞문을
[04:00] 뜯어냈습니다.
[04:02] 진행자가 물었습니다. 그러면 생성된
[04:04] 코드는 별로 들여다보지 않았다는
[04:06] 건가요?
[06:02] >> 는 일을 실행할 때만 띄우고 세션은
[06:04] 따로 저장합니다.
[06:06] 자격증명은 볼트에 두고 요청이 밖으로
[06:08] 나가는 순간에만 프록시가
[06:09] 끼워넣습니다. 샌드박스에는 들어가지
[06:11] 않습니다.
[06:13] CPU 사용량은 평균 1/3 정도로
[06:15] 줄었습니다.
[06:16] 프로젝트 중간에 처음부터 다시 하자는
[06:18] 결정은 이전엔 하기 힘든
[06:19] 일이었습니다. 구현이 빨라지니 감당할
[06:22] 만한 선택이 된 겁니다.
[06:24] 팀이 일하는 방식도 바뀌었습니다. 팀
[06:26] 크기는 여전히 다섯에서 열 명쯤인데
[06:28] 더 시니어 쪽으로 기울었습니다.
[06:30] 테크 리드가 설계하고 여러 명이
[06:31] 구현하던 구조 대신 누구나 설계와
[06:33] 조율을 고민하고 클라우드들에게 구현을
[06:35] 맡깁니다.
[06:37] 코드 리뷰도 바뀌었습니다. 모든
[06:39] 변경마다 클라우드 분류기가 돌면서
[06:41] 사람이 봐야 하는지 판단합니다. 봐야
[06:43] 한다면 몇 명이 어느 팀이 봐야
[06:45] 하는지까지 정하고 아니면 사람 없이
[06:47] 바로 병합합니다.
[06:49] 예를 들면 새 모델이 나올 때마다
[06:50] SDK 버전을 올리는 일처럼 수없이
[06:53] 해본 기계적인 변경입니다.
[06:55] 깨진 테스트 때문에 CI가 빨갛게
[06:56] 되면 에이전트가 알아서 고칩니다.
[06:59] 대부분 아무도 들여다보지 않습니다.
[07:01] 위험한 변경은 아직 사람이 봅니다.
[07:03] 다만 사람이 필요없는 비율을 조금씩
[07:05] 올리는 게 목표입니다.
[07:07] 온보딩도 달라졌습니다. 화이트보드
[07:09] 앞에 선배를 붙잡는 대신 클라우드에게
[07:11] 이 시스템이 어떻게 도는지 묻습니다.
[07:14] 그러면 클릭해 가며 볼 수 있는
[07:15] 인터랙티브 앱을 만들어 주기도
[07:17] 합니다.
[07:17] 모든 시스템이 MCP 서버로 연결돼
[07:19] 있어서 가능한 일입니다.
[07:21] API 온콜은 가장 무거운
[07:23] 단건입니다. 몇 달째 클라우드가 이
[07:25] 단건을 옆에서 따라하고 있습니다.
[07:26] 알림이 오면 클라우드가 먼저 받아서
[07:29] 잡음인지 진짜인지 가립니다. 잡음이면
[07:31] 아무도 깨우지 않습니다.
[08:02] 물론 진짜 장애에서 사람을 아예 안
[08:04] 깨우는 단계는 아직 아닙니다. 지금은
[08:06] 잡음을 거르는 첫 관문까지입니다.
[08:09] 제품 매니저도 직접 배포합니다. 최근
[08:11] 개발자 콘솔에 나온 프롬프트 캐시
[08:13] 진단 대시보드가 그 예입니다.
[08:15] 캐시가 왜 빗나갔는지 알려주는 이
[08:17] 기능을 PM 한 명이 슬랙에서 콜로
[08:19] 도와 주고받으며 만들어 프로덕션에
[08:21] 올렸습니다.
[08:22] 문제가 생기면 누가 책임질까요?
[08:24] 답은 예전과 같습니다. 그 시스템을
[08:26] 맡은 팀이 호출을 받습니다. PM이
[08:28] 만들었던 사람 없는 에이전트가 고쳤든
[08:31] 시스템을 지키는 건 결국 사람으로 된
[08:33] 팀이라는 겁니다. [음악]
[08:34] 채용도 바뀌었습니다. 엔트로픽은
[08:36] 제품과 플랫폼 조직 전반에서 코딩
[08:39] 면접을 단계적으로 없앴습니다.
[09:02] 대신 코딩 에이전트를 쓰는 면접을
[09:03] 시험하고 있습니다.
[09:05] 에이전트가 짠 코드나 설계를
[09:06] 리뷰하거나 에이전트로 직접 만들어
[09:08] 보는 식입니다.
[09:09] 설계 면접과 지난 프로젝트를 묻는
[09:11] 면접은 그대로입니다. 바뀐 건
[09:12] 손코딩을 보던 자리 하나입니다.
[09:15] 레벨 기준도 흔들립니다. 예전에 2년
[09:17] 걸린 프로젝트를 이끌었다면 그 자체로
[09:19] 복잡한 일을 했다는 증거였습니다.
[09:22] 그런데 2년 짜리로 보이던 이번
[09:23] 이전은 다섯에서 여섯 달에
[09:25] 끝났습니다.
[09:26] 그래서 기준은 결국 영역입니다.
[09:29] 마지막으로 진행자는 엔지니어들의
[09:31] 정체성 위기를 물었습니다. 케이틀린은
[09:33] 지난 10월 블로그에 이렇게
[09:34] 썼습니다. 많은 소프트웨어 엔지니어가
[09:36] 정체성 위기를 겪고 있다고요.
[09:50] [음악]
[10:11] 케이틀린의
[10:12] 수천 개의 에이전트가 함께 일하는
[10:14] 시스템이 제대로 돌려면 사람이 먼저
[10:16] 풀어야 할 문제가 많다는 겁니다.
[10:18] 보안, 인프라, 인증 같은 바탕을
[10:20] 제대로 깔지 않으면 좋은 결과보다
[10:22] 나쁜 사고가 먼저 난다고 했습니다.
[10:24] 코드를 다 안 읽어도 됐던 건 결과를
[10:26] 비교하는 그림자 시스템을 사람이 먼저
[10:28] 만들었기 때문입니다.
[10:30] 엔지니어의 시간은 구현에서 다른
[10:32] 팀과의 조율로 옮겨갔습니다.
[10:34] 그리고 남는 힘은 더 큰 문제에
[10:35] 쓰라는 것.
[10:36] 케이트린의 표현으로는 야망의 수준을
[10:38] 올리라는 겁니다.
[10:39] 여러분의 일에서 결과를 검증하는
[10:41] 장치는 무엇인가요?
[10:43] 그게 있어야 에이전트가 짠 코드를 다
[10:45] 읽지 않아도 됩니다.

## 트랜스크립트 — en-orig (영어 더빙 ASR — 더빙 문장은 인용하지 않음, 판독 대조용. 인터뷰이를 *Caitlin* 으로 적는다. 무캡션 다섯 곳(약 3분 57초))

[00:00] This is how Anthropic builds code now.
[00:03] They completely rebuilt the API that
[00:04] every Claude token passes through, and
[00:06] 80%of the PRs submitted by agents
[00:08] weren't even read thoroughly.
[00:10] It took five to six months to migrate
[00:12] the core layer from Python to Rust.
[00:14] The core team consisted of only a few
[00:15] people.
[00:16] How could they trust the code enough to
[00:18] deploy it without reading it all?
[00:19] And what were the engineers doing during
[00:21] that time?
[00:22] Let’s follow the story of Caitlin, Head
[00:24] of Platform Engineering, to find out why
[00:25] they even eliminated coding interviews.
[00:28] Caitlin’s team is responsible for the
[00:29] Messages API, through which all of
[00:30] Claude’s tokens pass. When a request
[00:32] comes in, it’s authenticated, tokenized
[00:34] , billed, and safety-checked in the core
[00:36] API before heading down to the GPU.
[00:38] Claude’s apps and code all run on the
[00:40] same API as external customers.
[00:42] The problem was that this layer was a
[00:44] Python monolith.
[00:45] Initially, it ran only in one Google
[00:47] Cloud region.
[00:48] The API was first built about three
[00:49] years ago by a tiny team working
[00:50] alongside researchers, and Python was
[00:52] the researchers 'language of choice.
[00:54] But then, requests skyrocketed. They
[00:56] even aired a Super Bowl commercial
[00:57] earlier this year.
[00:58] While no one is likely to hook into the
[00:59] API immediately after seeing an ad, many
[01:01] people install the app, and every
[01:02] request goes through this API.
[01:04] Caitlin says that throughout her career
[01:06] , CPU has always been a resource you
[01:07] could just pay to scale up.
[01:09] But for the first time, asking for more
[01:11] cloud CPU became a difficult
[01:12] conversation.
[01:13] They added more regions and found small
[01:14] efficiency gains and infrastructure
[01:16] optimizations. It still wasn't enough.
[01:18] Eventually, an engineer brought up an
[01:19] idea. To try something completely
[01:20] different. To use Rust.
[01:23] However, almost no one on the team had
[01:24] much experience with Rust.
[01:26] In fact, Anthropic had been building new
[01:27] services in Go since last year.
[01:29] It was a compromise between efficiency
[01:31] and developer experience.
[01:32] Back then, models weren't good enough to
[01:34] bridge language gaps, so
[01:35] developer-friendly languages were still
[01:36] important.
[01:38] But this year, as models improved, the
[01:39] math changed.
[01:40] Because models could now take on more of
[01:42] the implementation details.
[01:43] Caitlin laughs, saying if they had
[01:45] suggested C ++, quite a few engineers
[01:46] might have quit.
[01:48] Rust had one more advantage. It has a
[01:50] vast number of checks caught at compile
[01:52] time.
[01:53] When humans wrote code, this was a
[01:54] frustrating barrier, but when agents
[01:56] write it, it becomes a basis for trust.
[01:58] According to Caitlin, when working on
[02:00] tasks where results vary, it’s a huge
[02:01] advantage if you can just make them
[02:03] verifiable.
[02:04] So, how much did the engineers need to
[02:06] know about Rust?
[02:07] Caitlin answers, "75 to 25." 75%is what
[02:09] the model writes without needing to know
[02:11] the syntax, and 25%is what I learn by
[02:13] asking the model out of curiosity.
[02:16] He said that half is Claude writing the
[02:17] code, and the other half is teaching him
[02:19] what that code means.
[02:21] The initial plan was to break the system
[02:22] into pieces and migrate them to Rust.
[02:25] It was too slow.
[03:11] In the new structure, requests enter
[03:12] through a thin Python front door and are
[03:14] processed by the original Python system
[03:15] .
[03:16] Simultaneously, the same request flows
[03:18] into the Rust system like a shadow, and
[03:19] both results are compared.
[03:21] There was one hurdle to this comparison
[03:22] .
[03:23] Anthropic does not look at user prompts
[03:25] or model responses.
[03:27] Even if the results differ, we cannot
[03:28] open the raw data to see what is
[03:30] different or why.
[03:31] So, we compared only two things. Whether
[03:33] the processing before reaching inference
[03:35] is the same, and whether the token count
[03:36] upon return is the same.
[03:38] And we ask the model every day. How many
[03:39] requests today resulted in different
[03:41] outcomes between Python and Rust?
[03:43] We reduced those discrepancies over and
[03:45] over until it was nearly perfect, and
[03:46] only then did we start turning on Rust.
[03:50] Even after that, we kept the Python
[03:51] front door for a while. To revert to
[03:53] Python if Rust threw an error.
[03:55] We judged that being a bit slow was
[03:57] better than having no response at all.
[03:59] Only after we gained enough trust did we
[04:00] tear out the front door.
[04:02] The host asked. So, you didn't really
[04:04] look at the generated code?
[06:02] >> We spin it up only when running tasks,
[06:04] and sessions are stored separately.
[06:06] Credentials stay in the vault, and a
[06:08] proxy injects them only the moment a
[06:09] request goes out. Nothing enters the
[06:11] sandbox.
[06:13] CPU usage dropped to about one-third on
[06:15] average.
[06:16] Deciding to restart a project from
[06:18] scratch used to be a difficult choice.
[06:20] With faster implementation, it has
[06:22] become a manageable option.
[06:24] The way the team works has changed as
[06:25] well.
[06:26] The team size is still about five to ten
[06:27] people, but it has skewed toward being
[06:29] more senior.
[06:30] Instead of a structure where a tech lead
[06:31] designs and many implement, everyone
[06:33] thinks about design and coordination,
[06:34] and entrusts the implementation to
[06:36] Claude.
[06:37] Code reviews have also changed. For
[06:39] every change, a Claude classifier runs
[06:40] to judge whether a human needs to look
[06:42] at it.
[06:43] If a human review is needed, it even
[06:44] decides how many people and which team
[06:46] should look at it, otherwise it merges
[06:47] automatically.
[06:49] For instance, these are mechanical
[06:50] changes we've done countless times, like
[06:52] bumping the SDK version whenever a new
[06:53] model is released.
[06:55] If the CI turns red due to broken tests
[06:57] , an agent fixes it on its own.
[06:59] Most of the time, no one even looks at
[07:00] it.
[07:01] Dangerous changes are still reviewed by
[07:03] humans. However, the goal is to
[07:04] gradually increase the ratio of changes
[07:05] that don't require human intervention.
[07:07] Onboarding has changed too.
[07:09] Instead of grabbing a senior colleague
[07:10] in front of a whiteboard, we ask Claude
[07:12] how this system works.
[07:14] It even creates interactive apps that
[07:15] you can click through and explore.
[07:18] This is possible because all systems are
[07:19] connected via MCP servers.
[07:21] API on-call is the most burdensome task
[07:23] .
[07:24] For several months, Claude has been
[07:25] shadowing this task.
[07:27] When an alert arrives, Claude receives
[07:28] it first to filter out noise from real
[07:30] issues. If it is just noise, it doesn't
[07:31] wake anyone up.
[08:02] Of course, we aren't at the stage yet
[08:04] where humans are never woken up for real
[08:05] incidents. For now, it acts as the first
[08:07] gate for filtering out noise.
[08:09] Product managers also handle deployments
[08:10] themselves. The prompt cache diagnostic
[08:12] dashboard recently added to the
[08:13] developer console is one example.
[08:15] A PM built this feature, which explains
[08:17] why a cache miss occurred, and deployed
[08:19] it to production by collaborating via
[08:21] Slack.
[08:22] Who is responsible if a problem arises?
[08:24] The answer is the same as before. The
[08:26] team in charge of that system gets the
[08:27] call. Whether built by a PM or fixed by
[08:29] an agent without human intervention,
[08:31] it’s ultimately the human team that
[08:33] guards the system.
[08:34] Hiring has changed as well. Anthropic
[08:36] has phased out coding interviews across
[08:38] its product and platform organizations.
[09:02] Instead, they are testing interviews
[09:03] that involve using coding agents.
[09:05] This includes reviewing code or designs
[09:06] written by agents, or building something
[09:08] directly using an agent.
[09:09] Design interviews and interviews about
[09:11] past projects remain in place. The only
[09:12] thing that changed is the session where
[09:13] candidates had to code by hand.
[09:15] Evaluation criteria for levels are also
[09:16] shifting. In the past, leading a
[09:17] two-year project was proof in itself
[09:19] that you had handled complex work.
[09:22] However, this recent migration, which
[09:23] looked like a two-year task, was
[09:24] finished in five to six months.
[09:26] So, the standard ultimately becomes the
[09:27] scope of the work.
[09:29] Finally, the host asked about the
[09:31] identity crisis faced by engineers.
[09:32] Caitlin wrote this on her blog last
[09:34] October.
[09:35] That many software engineers are
[09:36] experiencing an identity crisis.
[10:11] Her point is that there are many
[10:13] problems humans must solve first for a
[10:15] system with thousands of agents to work
[10:17] properly.
[10:18] She noted that if you don't lay the
[10:19] foundation right—like security,
[10:21] infrastructure, and authentication—
[10:22] you'll have bad accidents before you get
[10:23] good results.
[10:24] We didn't have to read all the code
[10:26] because humans had already built a
[10:27] shadow system to compare the results.
[10:30] An engineer's time has shifted from
[10:31] implementation to coordination with
[10:32] other teams.
[10:34] And use your remaining energy for bigger
[10:35] problems.
[10:36] In Caitlin’s words, it is time to raise
[10:38] the level of your ambition.
[10:40] What mechanisms do you have in your work
[10:41] to verify results?
[10:43] You need those so you don't have to read
[10:44] every line of code an agent writes.
