---
title: "프로그래밍 언어 대신 배워야 할 것 | Matt Pocock"
type: video
source: https://www.youtube.com/watch?v=T8ccKI9Wn2E
site: youtube.com
author:
  - "[[Tech Bridge]]"
duration: 13:37
published: 2026-11-23
created: 2026-11-24
description: "Tech Bridge 한국어 해설 13:37, 공식 챕터 10, Korean original + 영어 더빙(en-orig는 내레이션 자리에서 더빙 ASR — 인용하지 않음). TypeScript 강사 Matt Pocock이 NetworkChuck과 나눈 2시간 대담의 작업 방식을 따라간 해설 — Ousterhout의 전술 / 전략 구분(AI는 전술, 전략은 사람), 그릴링 · 용어집 · 결정 기록(ADR 31개), 15만 토큰과 스마트 존 / 덤 존, 노력 수준, 스펙 → 티켓 → 서브 에이전트(워크트리), 머지 위험으로 하는 리뷰와 회고, 신뢰의 사다리와 피드백 루프(타입 · 테스트 · 린터), 딥 모듈과 불을 꺼도 되는 방, 언어 대신 배울 단어와 책 다섯 권. ⚠️ 대담 원음은 두 트랙 모두 무캡션(열다섯 곳, 약 4분 32초) — Matt Pocock 본인 인용 0."
tags:
  - clippings/youtube
---

**Source URL**: https://www.youtube.com/watch?v=T8ccKI9Wn2E
**Channel**: Tech Bridge · **Duration**: 13:37 · **Published**: 2026-11-23

> **게시일.** info.json `upload_date` **`20261123`**, `timestamp` 1795471226(= 2026-11-23 22:00:26 UTC = **2026-11-24 07:00 KST**), `availability`=`public`. 2026-11-24 회차(09:10 KST)에서 처음 잡혔다 — 게시 두 시간 뒤다. `upload_date`는 UTC 기준이라 파일명 날짜는 11-23이다. 파일명에서 `|` 는 뺐다.
>
> **오디오 트랙과 자막 — 인용 규칙.** 오디오는 **Korean original(default) + 영어 더빙**(audio language `ko` · `en` · `en-US`), 메타 `language`=`en`. 수동 자막 없음. `ko` = `ko-orig`(파일 동일, `kind=asr&lang=ko&variant=gemini`). `en-orig`(`kind=asr&lang=en&variant=timing-optimized`)는 **내레이션 자리에서 영어 더빙의 ASR** 이다 — 첫 줄부터 내레이션의 영어 번역이고(*"Do we really need to learn programming languages now?"*) *그릴* 을 *skill … drilling* 으로, *그릴링* 을 *Grit-ring* 으로, *울트라 싱크* 를 *Ultra-sync* 로 적는다. **인용하지 않았고 판독 대조용으로만 썼다.** 한국어 인용은 전부 ko-orig의 내레이션이다.
> ⚠️ **대담 원음(영어)은 두 트랙 어디에도 잡히지 않았다.** 대담 발췌가 들어간 자리는 두 트랙 모두 무캡션이다(11-20 Zechner 편 · 11-21 Pocock 편 · 11-22 Thariq 편과 같은 배치). **Matt Pocock과 진행자 본인의 말을 글자 그대로 인용한 것은 0건이다.** 429 없음(`--sleep-subtitles 8`).
>
> **무캡션 구간(`gaps.py` 4.5초 기준).** ko-orig 열다섯 곳: 00:18~00:23 · 00:51~00:57 · 00:59~01:03 · 01:05~01:10 · 01:12~01:37 · 02:08~02:36 · 03:15~03:59 · 05:30~06:01 · 07:20~08:10 · 09:29~09:44 · 10:55~11:21 · 11:35~11:44 · 11:50~11:57 · 11:59~12:13 · 13:12~13:17 — 합쳐 약 4분 32초, 전부 대담 발췌 자리로 보인다(00:56 · 01:03 · 01:10 · 11:44 · 11:48 · 11:57에는 `[음악]` 표시만 있다). en-orig 아홉 곳: 00:18~00:23 · 00:51~01:37 · 03:11~04:00 · 05:26~06:01 · 07:20~08:10 · 09:29~09:44 · 10:55~11:21 · 11:35~12:14 · 13:12~13:17 — 같은 자리다. ⚠️ en-orig는 02:01~02:36에서 타이밍이 밀린다(한 문장이 02:01 · 02:13 · 02:27 세 줄로 늘어져 있다).
> ⚠️ **이 구간들은 내용 미상이다.** 여기에 드는 것: **제목 물음에 대한 답의 원음(00:02~00:08 — 설명란은 *"아니요"* 라고 적는다. 이 자리는 4.5초 기준에 걸리지 않으나 캡션 글자가 없다)** · 바이브 코딩에 대한 평(00:18~00:23 — 설명란 *한 번도 제대로 된 적이 없다*) · **AI가 전술은 하고 전략은 못한다는 본인 설명(00:51~01:37)** · 02:08~02:36(영상 편집기 시연의 첫머리) · 그릴링 시연의 문답(03:15~03:59) · **높은 노력 수준이 왜 모델을 멍청하게 만드는지(05:30~06:01)** · **머지 위험을 매기는 방법(07:20~08:10)** · 09:29~09:44 · 아키텍처 보고서의 나머지(10:55~11:21) · **무엇을 배워야 하느냐는 물음에 대한 답과 *이런 단어* 의 예(11:35~12:13)** · *케어* 원음(13:12~13:17). 내레이션이 앞뒤로 받아 적은 줄만 남아 있다.
>
> **ASR 판독(ko-orig → 판독, 괄호는 근거).** *맷 턱*(00:08) · *메트 · 매트* → Matt Pocock(제목 · 설명란), *존 오스터하우트*(00:33) · *오스트아웃트*(10:23) → John Ousterhout(더빙 *Ousterhout*), *그릴*(02:57) → grill, *일하는 수서*(03:00) → 일하는 순서(더빙 *workflow*), *같은 환부를*(04:14) → 같은 환불을(더빙 *refund*), *결정기로 ADR*(04:27) → 결정 기록 ADR(챕터 제목), *용어를 하나씩 제한하고*(04:45) → 제안하고(추정 — 더빙 *defines terms one by one*), *붙잡고 있는 물량*(04:54~04:55) → 분량(추정), *덱소 씨*(05:13) → Dex Horthy(추정 — 더빙 *Dexo*, 성은 캡션에 없다. 11-21 업로드 편과 같은 판독), *나눠 봤습니다*(06:32) → 나눠 맡습니다(추정 — 더빙 *take the tickets and handle them*), *싶었습니다*(07:00) → 짚었습니다(추정), *울트라 싱크*(07:04) → ultrathink(추정), *뭐지 위험*(07:16) → 머지 위험(챕터 제목), *리뷰의 세계를*(08:10) → 리뷰의 세기를(추정), *양쪽 문 · 한쪽 문*(08:11) → 양방향 문 · 일방향 문(추정 — 앞선 Pocock 소스의 two-way / one-way door), *회고 스키*(08:23 · 09:23) → 회고 스킬, *실뢰*(08:34) → 신뢰, *공장을 싫다고*(10:34) → 공장은 싫다고, *임프루브 코드베이스 아키텍처*(10:41) → improve-codebase-architecture(추정 철자), *의료에 비었다면*(11:24) → 의료였다면(추정), *초기 솔직하게*(11:28) → 척이 솔직하게(추정 — 더빙은 *I asked him honestly at the beginning* 으로 달리 옮겼다), *대답 내내*(13:06) → 대담 내내.
> ⚠️ **판독하지 못한 것.** ① *맷은 오히려 안 말에 안 된다고 했습니다*(01:58~02:00) — 더빙은 *Matt actually said the opposite* 뿐이라 대조가 되지 않는다. ② *PR 스기니스는 설명물에는 세 칸이 있습니다*(07:13) — *PR 설명문* 으로 보이나 첫머리는 미상(더빙 *The PR description has three sections*). ③ **신뢰의 사다리를 말한 사람의 이름.** ko-orig *도런 테네마를 빌립니다*(08:38), 더빙 ASR *Doron Tenne* — *한 달에 PR 2,500개* 와 *신뢰의 사다리* 로 보면 Lauren Tan으로 추정되나 **두 트랙 모두 이름이 깨져 확정하지 않았다.** ④ *탐색은 파일을 많이 읽는다고 잘 듣는 일이 아닙니다*(06:01~06:03) · *이것저것 오리 시도해야 하는 일*(06:07~06:09) — 뜻은 통하나 글자가 불확실해 인용하지 않았다. ⑤ *어려운 단어는 티치 스킬 루프입니다*(12:34~12:36) — teach 스킬로 보이나 문장 전체가 불확실하다.
> ⚠️ 내레이션의 사실 표기 둘은 글자 그대로 두었다: *트윗 글자수가 240*(10:08) · *레거시 코드 활용 전략 … 2003년에 나온 책*(12:23~12:25 — 통상 2004년 출간으로 알려져 있다. 위키는 확인하지 않았다).
>
> ⚠️ **해설이고 2차 전달이다.** 위키는 원본 대담(`mU8WKII1gpk`)도 `mattpocock/skills` 저장소도 이번에 열지 않았다. 수치(100만 토큰 · 15만 토큰 · ADR 31개 · PR 2,500개 · 150줄 · 다섯 개에 하나 · 6년 · 2015년)는 내레이션이 대담과 화면에서 옮긴 값이다. 진행자의 이름 NetworkChuck은 설명란과 info.json `tags`에만 있고 캡션에는 *척* 으로만 나온다.


## 설명란

타입스크립트를 가르치는 Matt Pocock은 "프로그래밍 언어를 꼭 배워야 하냐"는 질문에 "아니요"라고 답합니다. 같은 사람이 바이브 코딩은 한 번도 제대로 된 적이 없다고도 말합니다. 그럼 언어 대신 무엇을 배워야 할까요?

NetworkChuck과 나눈 2시간 대담에서 Matt가 직접 보여 준 작업 방식을 따라갑니다. AI는 오늘 문제를 푸는 전술은 잘하지만 코드베이스를 길게 가꾸는 전략은 못합니다. 그래서 전략은 사람이 쥐어야 합니다. AI가 먼저 질문하게 하는 그릴링, 용어집과 결정 기록, "최선을 다해"라고 시키면 오히려 멍청해지는 이유와 대화 창을 작게 쓰는 법, 스펙에서 티켓·서브 에이전트로 일을 쪼개는 순서, 코드를 한 줄씩 읽는 대신 머지 위험으로 하는 리뷰, 에이전트를 믿게 해 주는 피드백 루프와 딥 모듈까지 다룹니다.

타임라인
0:00 프로그래밍 언어, 꼭 배워야 할까?
0:31 AI는 전술, 전략은 사람
2:31 AI와 말 맞추기: 그릴링·용어집·결정 기록
4:48 "최선을 다해"가 AI를 멍청하게 만든다
6:17 스펙 → 티켓 → 서브 에이전트
7:08 줄 단위가 아니라 머지 위험으로 리뷰
8:33 에이전트를 믿게 해 주는 피드백 루프
9:59 테스트와 딥 모듈
11:27 언어 대신 배울 것
13:06 결국 신경 쓰기

참고
원본 영상: https://www.youtube.com/watch?v=mU8WKII1gpk
Matt Pocock skills: https://github.com/mattpocock/skills

#AI코딩 #바이브코딩 #MattPocock #ClaudeCode #코딩에이전트

> info.json `tags`: AI 에이전트 · AI 코딩 · Claude Code · Matt Pocock · NetworkChuck · TypeScript · vibe coding · 매트 포칵 · 바이브 코딩 · 서브 에이전트 · 컨텍스트 엔지니어링 · 코드 리뷰 · 코딩 에이전트 · 클로드 코드 · 프로그래밍 공부

## 트랜스크립트 — ko-orig (Korean original, ASR variant=gemini — 한국어 내레이션만 잡혔다(대담 원음 없음, `>>` 하나(08:10)는 내레이션 복귀 표시))

[00:00] 프로그래밍 언어, 지금 꼭 배워야
[00:02] 할까요?
[00:08] 이렇게 답한 사람은 맷 턱
[00:10] 타입스크립트 강의로 이름을 알린
[00:12] 개발자입니다.
[00:13] 그런데 같은 사람이 바이브 코딩에
[00:15] 대해선 이렇게 말합니다.
[00:23] 그럼 언어 대신 무엇을 배워야
[00:25] 할까요?
[00:26] 답은 AI가 멍청해지는 설정, 그리고
[00:28] 그가 매일 돌리는 작업 순서에
[00:30] 있습니다.
[00:31] 맷이 먼저 꺼낸 건 오래된 책입니다.
[00:33] [음악] 존 오스터하우트의 소프트웨어
[00:35] 설계의 철학.
[00:36] 이 책은 프로그래밍을 둘로 나눕니다.
[00:38] 오늘 전투를 이기려는 하사관의 전술,
[00:40] 그리고 전쟁 전체를 보는 장군의
[00:42] 전략입니다.
[00:44] 예전 개발자는 둘을 늘 섞어서
[00:45] 했습니다. 이 수정이 오늘 일을
[00:47] 끝내는지, 길게 보면 득이 되는지
[00:49] 함께 따졌죠. [음악]
[00:56] [음악]
[01:03] [음악]
[01:10] [음악]
[01:37] 바이브 코딩만 하면 코드는 조금씩
[01:39] 나빠집니다. 그런데 코드는 에이전트,
[01:42] 그러니까 혼자 코드를 고치는 AI가
[01:44] 일하는 환경이기도 합니다.
[01:46] 집이 불타는데 괜찮다며 앉아 있는
[01:47] 개, 그 밈처럼요.
[01:49] 에이전트는 집이 무너지는 걸 보면서도
[01:51] 눈 앞의 일만 합니다.
[01:52] 그래서 집을 돌볼 사람이 필요하고
[01:54] 지금은 그게 바로 사용자라는 겁니다.
[01:57] 그렇다고 AI를 덜 쓰라는 말은
[01:58] 아닙니다. 맷은 오히려 안 말에 안
[02:00] 된다고 했습니다. 예전 개발자의 일은
[02:02] 대부분 전술이었고 이제 그 일을
[02:04] 최저임금보다 싸게 맡길 수
[02:05] 있으니까요.
[02:36] 열었습니다.
[02:37] 직접 만든 영상 편집기 코드입니다.
[02:39] 입력한 건 막연한 한 줄.
[02:41] 텔레프롬프터 화면이 지저분해졌으니
[02:43] 정리를 도와달라는 겁니다.
[02:45] 보통은 여기서 AI가 바로 코드를
[02:46] 짭니다.
[02:47] 그런데 이번에는 질문부터 합니다.
[02:49] 텔레프롬프터가 무엇을 읽어 오는지,
[02:51] 지금 화면에 뭐가 뜨는지.
[02:53] 그리고 질문마다 자기 추측을
[02:54] 붙입니다. 아마 이쪽일 것 같다고요.
[02:57] 이게 그릴 몰아세운다는 뜻의
[02:58] 스킬입니다. [음악] 스킬은 AI의
[03:00] 일하는 수서를 적어 준 짧은
[03:02] 문서입니다.
[03:03] 규칙은 둘입니다.
[03:04] 이해가 같아질 때까지 끈질기게
[03:05] 묻는다. 그리고 코드에서 찾을 수
[03:07] 있는 사실은 묻지 말고 직접 찾는다.
[03:13] [음악]
[03:59] [음악] 여기에 하나가 더 붙습니다.
[04:01] 용어집입니다.
[04:02] 코스, 섹션, 레슨, 버전 같은 말이
[04:04] 이 앱에서 무슨 뜻인지 적어둔
[04:06] 문서입니다.
[04:07] 피해야 할 말까지 적혀 있습니다.
[04:09] 반 년 동안 AI와 함께 다듬은
[04:10] 단어라 AI가 처음부터 이 앱의 말로
[04:12] 대화한다고 합니다.
[04:14] 반대 경우도 있습니다. 같은 환부를
[04:16] 화면은 리버설, 이메일은 차지백,
[04:18] 데이터베이스는 리펀드라고 부르는
[04:20] 앱입니다. [음악] 사람도 헷갈리고
[04:21] AI도 헷갈립니다. 말을 하나로
[04:23] 맞추면 AI가 내 머릿속에 들어온 것
[04:25] 같다고 했습니다.
[04:27] 마지막은 결정기로 ADR입니다.
[04:29] 되돌리기 어렵고 비싼 결정을 짧은
[04:31] 문서로 남깁니다. 이 저장소에만
[04:33] 31개가 있습니다.
[04:34] 코드는 지금 모습만 보여줍니다. 왜
[04:36] 그렇게 정했는지는 남지 않아서 기록이
[04:38] 없으면 AI는 같은 실수를
[04:40] 되풀이합니다.
[04:41] 처음부터 다 갖출 필요는 없습니다.
[04:43] 질문을 주고받다 보면 AI가 용어를
[04:45] 하나씩 제한하고 지금 손대는 곳부터
[04:47] 넓혀가면 됩니다.
[04:49] 질문이 끝나면 만들 차례입니다. 그
[04:51] 전에 메트는 이 일이 대화 하나에
[04:52] 들어가는지부터 따집니다. [음악]
[04:54] AI가 한 번에 붙잡고 있는 물량을
[04:55] 컨텍스트 창이라고 합니다. 오퍼스는
[04:57] 100만 토큰까지 담을 [음악] 수
[04:58] 있습니다. 그런데 메트는 15만
[05:00] 토큰쯤부터 불안해진다고 했습니다.
[05:02] 진행자가 너무 이르다며 놀랄
[05:03] 정도로요.
[05:04] 토큰이 쌓이면 토큰 사이의 관계는
[05:06] 제곱으로 늘어납니다. 꽉 찬 방에서
[05:08] 가장 중요한 말만 골라 듣기 어렵듯
[05:10] 모델의 판단이 흐려집니다.
[05:12] 메트는 이걸 스마트 존과 덤 존으로
[05:13] 나눠 부릅니다. 덱소 씨가 만든
[05:15] 말이라고 출처도 [음악] 밝혔습니다.
[05:17] 첫 머리에 꺼낸 최선 이야기도 여기서
[05:18] 나옵니다. 진행자 척은 AI가 매번
[05:21] 최선을 다하길 바라서 노력 수준을
[05:23] 최고에 가깝게 둔다고 했습니다.
[05:28] [웃음]
[06:01] 탐색은 파일을 많이 읽는다고 잘 듣는
[06:03] 일이 아닙니다. 맞는 파일을 읽으면
[06:04] 되죠. 높은 단계는 조사나 성능
[06:07] 측정, 디버깅처럼 이것저것 오리
[06:09] 시도해야 하는 일에 맞습니다.
[06:11] 모델을 바꿔가며 비교하지도 않습니다.
[06:12] 다음 모델이 다 고쳐주길 기다리지
[06:14] 말고 지금 내 문제를 고치라는
[06:16] 겁니다.
[06:17] 작은 일이면 바로 구현 스킬로
[06:18] 넘어갑니다. 대화 하나를 넘길 만큼
[06:21] 크면 다른 길로 갑니다.
[06:22] 먼저 대화를 스펙, 그러니까 목표를
[06:24] 적은 문서로 바꿉니다.
[06:25] 그걸 다시 티켓으로 쪼갭니다.
[06:27] 티켓 하나가 대화 하나. 대략 15만
[06:29] 토큰 안에 끝나게요.
[06:30] 그다음 서브 에이전트들이 티켓을 나눠
[06:32] 봤습니다.
[06:33] 각자 워크 트리, 즉 따로 떨어진
[06:35] 작업 폴더에서 동시에 일하고 끝나면
[06:37] 합쳐서 PR 하나를 만듭니다.
[06:38] [음악] PR이 나오면 코드 리뷰
[06:40] 스킬이 두 가지를 봅니다. 스펙대로
[06:41] 만들었는지, 그리고 코딩 표준을
[06:43] 지켰는지. [음악] 코딩 표준은
[06:45] 매트가 직접 쓴 문서입니다.
[06:47] 사람이든 에이전트든 코드를 쓰고
[06:48] 리뷰할 때 머릿속에 늘 규칙이
[06:49] 빽빽합니다.
[06:51] 타입스크립트에서 애니 타입을 쓰면
[06:52] 구멍이 생긴다. 이런 식의
[06:53] 규칙입니다.
[06:55] 척은 표준을 AI에게 만들라고 하고
[06:57] 들여다보지 않는다고 했습니다.
[06:58] [음악]
[06:59] 매트는 그게 바로 바이브 코딩이라고
[07:00] 싶었습니다.
[07:01] 잘하라고는 하는데 어떻게 잘하는지는
[07:03] 관심이 없는 거죠.
[07:04] 울트라 싱크 하라고, 안 그러면
[07:06] 해고라고 외치는 밈과 같다고요.
[07:08] 그다음은 사람 차례입니다. 그런데
[07:10] 매트는 모든 코드를 한 줄씩 읽지
[07:11] 않습니다.
[07:13] PR 스기니스는 설명물에는 세 칸이
[07:14] 있습니다. 바뀐 것의 요약,
[07:16] 작동한다는 증거, 그리고 뭐지
[07:18] 위험입니다.
[08:10] >> 리뷰의 세계를 위험에 맞추는 겁니다.
[08:11] 양쪽 문은 훑어보고 한쪽 문은 천천히
[08:13] 엽니다. 사람의 눈은 되돌릴 수 없는
[08:15] 곳에 있습니다.
[08:17] 리뷰에서 지적한 내용도 고치고 끝내지
[08:19] 않습니다. 같은 말을 다시 쓰지
[08:20] 않으려면 환경을 어떻게 바꿀지
[08:22] 생각합니다.
[08:23] 그래서 회고 스키를 돌립니다.
[08:24] [음악] 세션과 리뷰를 돌아보고
[08:25] 다음엔 무엇을 바꿀지 제안하게
[08:27] 합니다.
[08:28] 여기까지가 매트의 하루 루프입니다.
[08:30] 그릴링, 스펙과 티켓, 구현, 코드
[08:32] 리뷰, 그리고 회고.
[08:34] 다음 질문은 실뢰입니다. 매트는 한
[08:36] 달에 PR을 2,500개쯤 낸다는
[08:38] 개발자 도런 테네마를 빌립니다.
[08:40] 신뢰의 사다리를 올라야 한다고요.
[08:42] 에이전트를 못 믿으면 하나하나
[08:44] 지켜보느라 네 개 넘게 돌리기도
[08:46] 어렵습니다. 믿을 수 있으면 수백
[08:48] 개를 함께 돌릴 수 있고요.
[08:50] 그 신뢰는 좋은 코드 베이스에서
[08:51] 나옵니다. 매트가 책장에 고전들에서
[08:54] 뽑은 정의는 바꾸기 쉬운 코드
[08:55] 베이스입니다.
[08:57] 바꿔도 뭔가 망가질 걱정이 적은 곳.
[08:59] [음악] 그러려면 에이전트가 자기
[09:01] 작업을 스스로 채점할 피드백 루프가
[09:02] 많아야 합니다.
[09:04] 타입이 있으면 실수를 바로
[09:05] 알려줍니다. 테스트는 [음악]
[09:06] 실제로 돌려서 확인하고 린터는 위험한
[09:08] 패턴을 잡습니다.
[09:10] 애니 타입을 막는 규칙도 그래서
[09:11] 있습니다. 매트는 애니를 타입 검사를
[09:14] 피해 가는 꼼수라고 불렀습니다.
[09:16] [음악] 높은 노력 단계를 쓰는 곳도
[09:17] 바로 여깁니다. 앱을 실제로 클릭해
[09:19] 보고 성능을 재면서 자기 작업을
[09:21] 검증할 때요.
[09:23] 회고 스키는 리뷰에서 나온 지적을
[09:24] 다음엔 자동 검사로 막을 방법을
[09:26] 찾습니다. [음악]
[09:44] 규칙을 AI에게 지키라고 맡길지 린트
[09:46] 규칙으로 만들지 고를 수 있다면 늘
[09:48] 후자입니다. 매번 똑같이 도는 결정론
[09:50] 쪽이요. 배포도 그렇습니다.
[09:52] 에이전트가 직접 서버에 올리게 하지
[09:53] 않고 깃허브에 합쳐지면 자동으로
[09:55] 배포되게 둡니다. 토큰도 안 들고
[09:57] 매번 같으니까요.
[09:59] 테스트는 AI가 얼마든지 써줍니다.
[10:01] 그런데 매트는 테스트가 원래 어려운
[10:03] 일이라고 했습니다.
[10:05] 구현을 그대로 따라하는 테스트가 쉽게
[10:07] 나오기 때문입니다.
[10:08] 트윗 글자수가 240이라는 코드에 그
[10:10] 숫자가 240인지 확인하는
[10:12] 테스트처럼요.
[10:13] 이러면 코드 한 줄을 고칠 때마다
[10:15] 테스트도 같이 고쳐야 합니다.
[10:17] 대신 큰 덩어리를 모듈 하나로 묶고
[10:19] 바깥에 좁은 입구 하나만 냅니다.
[10:21] 테스트는 그 입구로 말합니다.
[10:23] [음악] 오스트아웃트가 딥 모듈이라
[10:25] 부른 구조입니다.
[10:26] 그러면 모듈 안은 마음껏 바꿔도
[10:27] 됩니다.
[10:28] 메트 표현으로는 그 방은 불을 꺼도
[10:30] 되는 거죠.
[10:32] 다만 불을 전부 끈 채 에이전트만
[10:34] 일하는 공장을 싫다고 했습니다.
[10:36] 대신 방마다 밝기를 조절하는 스위치를
[10:38] 달자는 겁니다.
[10:39] 코드베이스를 이런 모양으로 바꿔주는
[10:41] 스킬이 임프루브 코드베이스
[10:42] 아키텍처입니다. 대담 중에 직접
[10:44] 돌려보았습니다.
[10:45] [음악] 보고서의 첫 지적은 두
[10:47] 기능에 거의 똑같은 코드가 150줄
[10:49] 겹친다는 것.
[10:50] 흩어진 경로를 깊은 모듈 하나 뒤로
[10:52] 모으자고 제안합니다.
[11:21] 이런 자동 피알은 다섯 개에 하나쯤만
[11:23] 직접 확인합니다. [음악]
[11:24] 금융이나 의료에 비었다면 달랐을
[11:26] 거라고 덧붙였습니다.
[11:28] 초기 솔직하게 물었습니다. 이
[11:29] 보고서를 봐도 무슨 말인지
[11:31] 모르겠다고. 그럼 뭘 배워야 하냐고.
[11:44] [음악]
[11:48] [음악]
[11:57] [음악]
[12:13] [음악] 배워야 할 건 프로그래밍
[12:15] 언어가 아니라 이런 단어입니다. 같은
[12:17] 문제를 말할 단어가 있으면 AI에게
[12:19] 훨씬 정확하게 시킬 수 있습니다.
[12:21] 그 단어는 책에서 배우라고 했습니다.
[12:23] 마이클 페더스의 레거시 코드 활용
[12:25] 전략. 2003년에 나온 책입니다.
[12:27] 책장에서 비닐도 안 뜯고 꽂혀 있던
[12:29] 책인데 펼쳐 보니 에이전트에게 시키던
[12:31] 일이 그대로 있었답니다.
[12:32] 아키텍처 개선 스킬도 거기서
[12:34] 나왔습니다. 어려운 단어는 티치 스킬
[12:36] 루프입니다. [음악] 모르는 보고서를
[12:38] 넘기면 내가 아는 것을 기억하면서
[12:39] 퀴즈와 HTML 수업을 만들어
[12:41] 줍니다.
[12:42] 매트는 이걸로 루빅스 큐브도 배웠다고
[12:44] 했습니다.
[12:46] [음악]
[12:46] 그가 꼽은 책은 소프트웨어 설계의
[12:48] 철학, 실용주의 프로그래머, 페더스의
[12:50] 책 리팩토링, 익스트림
[12:52] 프로그래밍입니다. [음악] 실제로
[12:54] 읽기만 해도 이 분야 대부분의
[12:55] 사람보다 앞서게 된다고 했습니다.
[12:57] 매트 자신도 컴퓨터 공학 전공이
[12:59] 아닙니다. 연극을 전공하고 6년 동안
[13:01] 발성 코치로 일하다 2015년에
[13:03] 독학으로 넘어왔습니다.
[13:06] 대답 내내 매트가 가장 많이 한 말은
[13:08] 케어, 신경 쓴다는 말이었습니다.
[13:17] [음악] 모델은 아직 전략을 신경
[13:18] 쓰지 않습니다. 언어 대신 배울 것은
[13:21] 그 빈자리를 채울 단어와 습관입니다.
[13:23] 바이브 코딩이 통하지 않았던 것도
[13:25] AI가 모자라서라기보다 집을 돌보는
[13:27] 사람이 없었기 때문입니다.
[13:29] 루프를 한 번에 다 따라할 필요는
[13:30] 없습니다. 매트의 권유처럼 다음 기능
[13:33] 하나를 시작할 때 AI가 먼저
[13:34] 질문하게 시키는 데서 시작해 보세요.

## 트랜스크립트 — en-orig (내레이션 자리는 영어 더빙 ASR — 인용하지 않음, 판독 대조용(02:01~02:36 타이밍 밀림))

[00:00] Do we really need to learn programming
[00:01] languages now?
[00:08] This was said by Matt Pocock, a
[00:10] developer famous for his TypeScript
[00:12] courses.
[00:13] But the same person has this to say
[00:15] about "vibe coding."
[00:23] Then, what should we learn instead of
[00:25] languages?
[00:26] The answer lies in how to keep AI from
[00:28] getting "dumb," and the workflow he runs
[00:29] every day.
[00:31] The first thing Matt pulled out was an
[00:33] old book. John Ousterhout's*A Philosophy
[00:34] of Software Design*.
[00:36] This book divides programming into two
[00:38] parts. The tactical maneuvers of a
[00:39] sergeant trying to win today’s battle,
[00:40] and the grand strategy of a general
[00:42] looking at the whole war.
[00:44] Developers in the past always did both
[00:45] together. They weighed whether a fix
[00:47] finished today's job and whether it
[00:48] would be beneficial in the long run.
[01:37] If you only do "vibe coding," your code
[01:39] will gradually get worse.
[01:40] Because code is also the environment
[01:42] where agents—AI that can fix code on its
[01:44] own—work.
[01:46] Like that meme of the dog sitting in a
[01:47] burning house saying it’s fine.
[01:49] The agent keeps working on the task at
[01:50] hand even while the house is collapsing
[01:51] .
[01:52] So, someone is needed to look after the
[01:54] house, and now that person is the user.
[01:57] That doesn't mean we should use AI less
[01:58] .
[01:59] Matt actually said the opposite.
[02:01] Most of a developer's past work was
[02:13] tactical, and now you can delegate that
[02:27] for less than minimum wage. He opened it
[02:36] . It's the code for a video editor he
[02:38] built himself.
[02:39] He entered one vague line.
[02:41] He asked for help cleaning up the
[02:42] teleprompter screen, which had become
[02:43] cluttered.
[02:45] Usually, this is where the AI starts
[02:46] writing code immediately.
[02:47] But this time, it starts with questions
[02:48] .
[02:49] Asking what the teleprompter reads and
[02:50] what is currently showing on the screen
[02:52] .
[02:53] And for every question, it adds its own
[02:54] hypothesis. Suggesting it's likely this
[02:56] or that.
[02:57] This is what he calls "skill," as in
[02:58] drilling the AI.
[02:59] "Skill" is a short document outlining
[03:01] the AI's workflow.
[03:03] There are two rules.
[03:04] Ask persistently until you share the
[03:05] same understanding. And for facts you
[03:07] can find in the code, don't ask—look for
[03:08] them yourself.
[04:00] One more thing is added here. A glossary
[04:02] . A document defining what words like "
[04:04] course,""section,""lesson," and "
[04:05] version" mean in this app.
[04:07] It even lists words to avoid.
[04:09] Since these terms were refined with the
[04:10] AI over six months, the AI talks using
[04:12] the app's vocabulary from the start.
[04:14] There are cases of the opposite, too. An
[04:16] app where the same refund screen is
[04:17] called "reversal," the email "
[04:18] chargeback," and the database "refund."
[04:21] Humans get confused, and so does the AI
[04:22] . He said that when you align the
[04:24] terminology, it feels like the AI has
[04:25] entered your mind.
[04:27] The last part is the decision-maker, or
[04:28] ADR. You record expensive decisions that
[04:30] are hard to reverse in a short document
[04:31] . There are 31 of them in this
[04:33] repository alone.
[04:34] Code only shows its current state.
[04:36] Without a record of why decisions were
[04:38] made, AI will repeat the same mistakes.
[04:41] You don't need to have everything ready
[04:42] from the start.
[04:43] As you exchange questions, AI defines
[04:45] terms one by one, and you can expand
[04:47] from there.
[04:49] Once the questions are done, it is time
[04:50] to build. But before that, Matt checks
[04:52] if the task fits into a single
[04:53] conversation.
[04:54] The amount of data an AI can hold at
[04:55] once is called the context window. Opus
[04:57] can hold up to 1 million tokens. However
[04:59] , Matt said it starts to get unreliable
[05:01] around 150,000 tokens. The host was even
[05:03] surprised at how early that was.
[05:04] As tokens pile up, the relationships
[05:06] between them increase exponentially.
[05:07] Just as it's hard to hear the most
[05:09] important words in a crowded room, the
[05:10] model's judgment gets clouded.
[05:12] Matt calls these the "smart zone" and
[05:13] the "dumb zone." He credited the term to
[05:16] Dexo.
[05:17] The "best effort" topic mentioned at the
[05:18] beginning also comes from here.
[05:20] Host Chuck said he sets the effort level
[05:21] to near-maximum because he wants the AI
[05:23] to do its best every time.
[06:01] Searching isn't about reading many files
[06:02] ; it’s about reading well. You just need
[06:04] to read the right files.
[06:05] Higher stages are for tasks that require
[06:07] trial and error, like research,
[06:08] performance measurement, or debugging.
[06:11] He doesn't switch models to compare them
[06:12] either. He says don't wait for the next
[06:14] model to fix everything; fix your
[06:15] current problem now.
[06:17] If it's a small task, move straight to
[06:18] implementation skills. If it's too big
[06:20] for one conversation, take a different
[06:21] path.
[06:22] First, convert the conversation into a
[06:23] spec—a document that writes out the
[06:25] goals.
[06:25] Then, break that down into tickets.
[06:27] One ticket per conversation. So it fits
[06:29] within roughly 150,000 tokens.
[06:31] Then, sub-agents take the tickets and
[06:32] handle them.
[06:33] Each works in a separate work tree, and
[06:35] when done, they merge them into a single
[06:38] PR.
[06:39] Once a PR is out, the code review skill
[06:40] checks two things. Whether it was built
[06:42] to spec, and whether it followed coding
[06:43] standards. The coding standards are
[06:45] documents Matt wrote himself.
[06:47] Whether it's a human or an agent, when
[06:48] writing or reviewing code, the mind
[06:49] should be packed with rules.
[06:51] Like "using the 'any' type in TypeScript
[06:52] creates a loophole." It’s rules like
[06:54] that.
[06:55] Chuck said people tell AI to create
[06:56] standards but then never look at them.
[06:59] Matt wanted to call that "vibe coding."
[07:01] They say to do it well, but they aren't
[07:03] interested in how to do it well.
[07:04] It’s like that meme that shouts "
[07:06] Ultra-sync or you're fired!"
[07:08] Then it's the human's turn. But Matt
[07:10] doesn't read every line of code.
[07:13] The PR description has three sections. A
[07:15] summary of changes, proof that it works
[07:17] , and potential risks.
[08:10] >> Align the world of reviews with the
[08:11] level of risk. Scan both doors, then
[08:13] slowly open one.
[08:14] Human eyes are reserved for irreversible
[08:16] points.
[08:17] Don't just fix what was pointed out in
[08:18] the review and call it a day. Think
[08:19] about how to change the environment to
[08:21] avoid repeating the same feedback.
[08:23] That’s why we run a retrospective skill
[08:24] . Reflect on sessions and reviews, and
[08:26] suggest what to change next.
[08:28] This is the daily loop of Matt.
[08:30] Grit-ring, specs and tickets,
[08:31] implementation, code review, and
[08:32] retrospective.
[08:34] The next question is about trust.
[08:36] Matt cites Doron Tenne, a developer who
[08:38] submits around 2,500 PRs a month. You
[08:40] have to climb the ladder of trust.
[08:43] If you don't trust the agents, it's hard
[08:44] to run more than four while watching
[08:46] each one.
[08:47] If you can trust them, you can run
[08:48] hundreds at the same time.
[08:50] That trust comes from a good codebase.
[08:52] The definition Matt drew from the
[08:54] classics on his shelf is a codebase that
[08:55] is easy to change.
[08:57] A place where you worry less about
[08:58] breaking things when you make changes.
[08:59] For that, agents need many feedback
[09:01] loops to grade their own work.
[09:04] Types notify you of mistakes immediately
[09:05] . Tests verify by actually running, and
[09:08] linters catch dangerous patterns.
[09:10] That’s also why there are rules to block
[09:11] the 'any' type. Matt called 'any' a
[09:13] loophole to bypass type checking.
[09:16] This is also where the high-effort steps
[09:18] are applied.
[09:19] When verifying work by actually clicking
[09:20] through the app and measuring
[09:21] performance.
[09:23] Retrospective skills find ways to use
[09:24] automated checks to prevent issues
[09:26] raised in reviews.
[09:44] If you can choose between asking AI to
[09:45] follow a rule or creating a lint rule,
[09:47] always choose the latter. Because it’s
[09:49] deterministic and runs the same way
[09:50] every time. Deployment is the same.
[09:52] Don't let agents upload to the server
[09:53] directly; let it deploy automatically
[09:55] once merged into GitHub. It costs no
[09:57] tokens and is consistent every time.
[09:59] AI can write as many tests as you want.
[10:02] But Matt said testing is inherently
[10:04] difficult.
[10:05] Because it’s easy to write tests that
[10:06] just mirror the implementation.
[10:08] Like a test that checks if the tweet
[10:10] limit is 240, just because the code says
[10:12] 240.
[10:13] This forces you to update the test every
[10:15] time you change a line of code.
[10:17] Instead, group large chunks into a
[10:19] single module and leave only a narrow
[10:20] entrance.
[10:21] Tests communicate through that entrance
[10:23] .
[10:23] This is the structure Ousterhout called
[10:25] a "deep module."
[10:26] Then, you can change the inside of the
[10:27] module as much as you want.
[10:29] In Matt’s words, you can turn the lights
[10:30] off in that room.
[10:32] However, he said he dislikes factories
[10:33] where agents work with all the lights
[10:35] off.
[10:36] Instead, he suggests installing light
[10:37] switches in every room to adjust the
[10:38] brightness.
[10:39] The skill that changes a codebase into
[10:41] this shape is "Improve Codebase
[10:42] Architecture." I ran it myself during
[10:44] the interview.
[10:46] The report first pointed out that 150
[10:47] lines of nearly identical code overlap
[10:49] in the two features.
[10:50] It suggests consolidating the scattered
[10:52] paths behind a single deep module.
[11:21] I only check these automated PRs myself
[11:23] about once every five times.
[11:24] He added that it would have been
[11:25] different if it were in finance or
[11:26] healthcare.
[11:28] I asked him honestly at the beginning.
[11:29] That I didn't know what this report
[11:30] meant even after reading it. And what I
[11:32] should learn instead.
[12:14] What you need to learn isn't a
[12:15] programming language, but these terms.
[12:16] If you have words to describe the same
[12:18] problem, you can instruct the AI much
[12:20] more accurately.
[12:21] He said I should learn those words from
[12:22] books. Michael Feathers '"Working
[12:24] Effectively with Legacy Code." It’s a
[12:25] book published in 2003.
[12:27] It was a book sitting on his shelf,
[12:28] still wrapped in plastic, but he said
[12:30] opening it revealed exactly what he was
[12:31] asking his agent to do.
[12:32] His skills for improving architecture
[12:34] also came from there. The difficult term
[12:36] is the "Teach Skill Loop." If you pass
[12:37] it a report you don't understand, it
[12:39] remembers what you know and creates
[12:40] quizzes and HTML lessons for you.
[12:42] Matt said he even learned how to solve a
[12:44] Rubik's Cube with this.
[12:46] The books he recommended are "A
[12:48] Philosophy of Software Design,""The
[12:49] Pragmatic Programmer," Feathers' book, "
[12:51] Refactoring," and "Extreme Programming.
[12:53] "
[12:53] He said that just reading them would put
[12:55] you ahead of most people in this field.
[12:57] Matt himself doesn't have a computer
[12:59] science degree. He majored in theater,
[13:01] worked as a vocal coach for six years,
[13:02] and then switched to self-taught coding
[13:04] in 2015.
[13:07] Throughout the interview, the word Matt
[13:09] used most was "care."
[13:17] Models still do not care about strategy
[13:19] . Instead of languages, what you need to
[13:21] learn are the words and habits to fill
[13:22] that gap.
[13:23] "Vibe coding" didn't work not because
[13:25] the AI was lacking, but because there
[13:26] was no one taking care of the house.
[13:29] You don't have to follow the whole loop
[13:30] at once.
[13:31] As Matt suggests, start by having the AI
[13:33] ask you questions first when you begin
[13:35] your next feature.
