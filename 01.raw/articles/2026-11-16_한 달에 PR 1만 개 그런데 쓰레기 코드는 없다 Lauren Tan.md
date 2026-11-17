---
title: "한 달에 PR 1만 개, 그런데 쓰레기 코드는 없다 | Lauren Tan"
type: video
source: https://www.youtube.com/watch?v=nldpxmin-1M
site: youtube.com
author:
  - "[[Tech Bridge]]"
duration: 11:11
published: 2026-11-16
created: 2026-11-17
description: "Tech Bridge 한국어 해설 11:11, 공식 챕터 10, Korean original(ko-orig variant=gemini) + 영어 더빙. AI Engineer Code Summit에서 Lauren Tan(@poteto, 설명란 표기 SpaceXSI Grok Bot 팀)이 한 발표 All Code Is Slop (Except Mine) 정리. 10월 한 사람 PR 3,127개 · 팀 10,926개(설명란), 되돌린 커밋 비율 6월 0.98% → 10월 0.47%, 주석 65,824 → 1,227. 뒤집힌 피라미드, 코드는 기억이다, 타이머 183개 사건, 주석은 부채, 애매하면 금지, 토큰의 70%는 검증에, 석 달 뒤 성적표."
tags:
  - clippings/youtube
---

**Source URL**: https://www.youtube.com/watch?v=nldpxmin-1M
**Channel**: Tech Bridge · **Duration**: 11:11 · **Published**: 2026-11-16

> **게시일.** info.json `upload_date` **`20261116`**, `timestamp` 1794866431(= 2026-11-16 22:00:31 UTC = **2026-11-17 07:00 KST**), `availability`=`public`. 파일명 · `date-published`는 UTC 날짜(11-16)를 쓴다. 파일명에서 `,` · `|`는 뺐다.
>
> **오디오 트랙과 자막 — 인용 규칙.** 오디오는 `Korean original (default)`(low · medium) + 영어 더빙(`en` · `en-US`), 메타 `language`=`en`. 수동 자막 없음. `ko` = `ko-orig`(md5 동일, `kind=asr&lang=ko&variant=gemini`). `en-orig`(`lang=en&variant=timing-optimized`)는 **영어 더빙 ASR**이다. → **내레이션 인용은 ko-orig.** en-orig는 내용 존재 · 고유명사 대조에만 쓰고 인용하지 않는다. 429 없음(`--sleep-subtitles 8`).
>
> **무캡션 구간(`gaps.py` 4.5초 기준, en-orig).** 00:06~00:11 · 01:13~01:31 · 01:44~02:10 · 02:50~03:04 · 05:01~05:34 · 06:09~06:33 · 07:10~07:25 · 09:20~09:57 · 10:04~10:27. ko-orig도 같은 자리에 `[음악]` · `[웃음]` 표시만 남았다. → **두 트랙 모두 비어** 원음(Lauren Tan 발표) 발췌로 보인다 — **내용 미상.** 이번 편에는 Lauren 원음이 어느 트랙에도 캡션으로 남지 않았다.
> ⚠️ 발췌에 걸려 캡션으로 확인되지 않는 것: 챕터 *나쁜 루프를 자동화하지 마라*(09:13~)의 본론(09:20~09:57 — 캡션에는 *"텐의 답은 아직 아니다 입니다"* 까지만), *릴리스 날 벌어지는 일*(10:04~10:27 — 버그 50개를 무엇이 찾았는지), 06:33 *"제품 코드에서는 아예 못 쓰게 했고"* 의 목적어(06:09~06:33 발췌 안. tags에 `useEffect`가 있어 그것으로 추정).
>
> ⚠️ **팀 PR 수가 캡션 안에서 갈린다.** 설명란 · 제목: 한 사람 **3,127개**, 팀 전체 **10,926개**(제목 *PR 1만 개*). ko-orig 00:13 *1926개*(en-orig 더빙 `1,926`), ko-orig 08:42 *19,226개*(en-orig `19,226`). 위키는 **설명란의 10,926** 을 채택하고 두 캡션 값은 ASR 오독으로 본다(추정 — *만 구백이십육* 을 다르게 받아 적은 것).
>
> **ASR 판독(ko-orig).** *로런 텐 · 텐 · 테 · 테니*(00:39 등) → Lauren Tan(설명란 · tags), *포테이토*(00:41) → poteto(@poteto), *스페이스 엑스 AI*(00:49) → 설명란 표기는 `SpaceXSI`, en-orig 더빙은 `xAI`, *그록봇*(00:51) → Grok Bot(설명란), *에이전트 MD*(02:37) → AGENTS.md(tags), *셋 타임아웃*(04:01) → `setTimeout`(en-orig), *10월 3일을*(04:14) → 10월 3일, *피스택*(05:45) → pstack(설명란), *노 코멘트*(05:47) → no-comment 스킬(철자 추정), *리비전의 주석*(05:48), *듄*(05:55) → Dune, *넥스트 JS*(06:00) → Next.js, *되게 슬로우로 이어진다*(06:06) → 결국 슬롭으로 이어진다(추정 — en-orig 더빙은 `slowness`), *신디, 쓰리다라는*(08:07) → Cindy Sridharan의(설명란), *TLA 플러스*(07:53) → TLA+, *린*(07:57) → Lean, *에이전트 공정부터 지우면*(09:14~09:15) → 판독 불명(en-orig `remove the agent process`), *쓴 다*(10:53) → 쓴다, *처음에 수수께끼*(10:55) → 처음의 수수께끼.
>
> ⚠️ **해설과 발화를 구분.** 내레이션은 Tech Bridge 해설이고 Lauren Tan 본인 음성은 캡션에 없다. 수치는 해설이 슬라이드 · 발표에서 옮긴 값이며 설명란 스스로 *"숫자는 모두 발표자 팀이 직접 집계한 것이고, 슬라이드에 단위가 없는 숫자는 단위를 붙이지 않았습니다"* 라고 적는다. 위키는 원 발표(`O_zcc6Xl12g`) · X 게시물 · pstack 저장소를 열지 않았다.

## 설명란

AI Engineer Code Summit에서 Lauren Tan(@poteto, SpaceXSI Grok Bot 팀)이 한 발표 "All Code Is Slop (Except Mine)"을 정리했습니다. 발표에 따르면 지난 10월 한 사람이 프로덕션에 올린 PR이 3,127개, 팀 전체로는 10,926개였고, 되돌린 커밋의 비율은 6월 0.98%에서 10월 0.47%로 줄었습니다. 그런데 이 팀은 코드에서 주석을 거의 다 지웠습니다.

주석을 없앴는데 왜 품질이 올랐는지, 임시방편 타이머 한 줄이 183개로 퍼진 사건부터 따라갑니다. 에이전트를 고쳐 줄 일이 생기면 규칙 파일에 한 줄 더 적는 대신 린트·타입 같은 검사로 남긴다는 것이 발표의 중심입니다. 숫자는 모두 발표자 팀이 직접 집계한 것이고, 슬라이드에 단위가 없는 숫자는 단위를 붙이지 않았습니다.

타임라인
0:00 한 달에 PR 3,127개, 그런데 주석은 사라졌다
0:38 모든 코드는 슬롭이다, 내 것만 빼고
2:14 뒤집힌 피라미드
3:10 코드는 기억이다
3:54 타이머 183개
4:49 주석은 부채다
5:54 애매하면 금지한다
7:24 토큰의 70%는 검증에
8:37 석 달 뒤의 성적표
9:13 나쁜 루프를 자동화하지 마라

참고
원본 발표: https://www.youtube.com/watch?v=O_zcc6Xl12g
Lauren Tan, "your codebase is memory": https://x.com/poteto/status/2109699980248408574
Lauren Tan, "we just banned comments": https://x.com/poteto/status/2115644484226777581
Lauren Tan, "not a dark factory": https://x.com/poteto/status/2118904450106654888
Cindy Sridharan(5월): https://x.com/copyconstruct/status/2055413082105716740
Cindy Sridharan(11월): https://x.com/copyconstruct/status/2118529738532925725
pstack: https://github.com/cursor/plugins

#AI코딩 #코딩에이전트 #LaurenTan #AIEngineer

> info.json `tags`: AGENTS.md · AI Engineer · AI 에이전트 · AI 코딩 · All Code Is Slop · Code Summit · Cursor · Grok Bot · Lauren Tan · SpaceXSI · poteto · pstack · useEffect · 린트 · 바이브 코딩 · 코드 리뷰 · 코딩 에이전트

## 트랜스크립트 — ko-orig (Korean original, ASR variant=gemini)

[00:00] 지난 10월, 엔지니어 한 명이
[00:02] 프로덕션에 올린 PR이
[00:03] 3,127개입니다.
[00:11] 이 사람이 속한 팀 전체로는 한 달에
[00:13] 1926개가 머지됐습니다.
[00:17] 이 정도면 엉망이 됐을 법한데 되돌린
[00:19] 커밋의 비율은 6월 0.98%에서
[00:22] 10월 0.47%로 오히려
[00:23] 줄었습니다.
[00:24] 그런데 이 팀이 한 일 가운데 이상한
[00:26] 게 하나 있습니다.
[00:27] 코드에서 주석을 거의 다 지웠습니다.
[00:29] 65,000을 넘던 숫자가 지금은
[00:31] 1,200 남짓입니다.
[00:33] 주석을 없앴는데 왜 품질이
[00:34] 올랐을까요? 오늘은 이 팀이
[00:36] 에이전트를 믿게 된 과정을 따라가
[00:37] 보겠습니다.
[00:39] 발표자는 로런 텐입니다.
[00:41] 온라인에서는 포테이토라는 이름으로 더
[00:42] 알려져 있습니다.
[00:43] 메타와 넷플릭스, 커서를 거쳤고
[00:46] 리액트 코어 팀에서 리액트 컴파일러를
[00:48] 만들어 온 사람입니다.
[00:49] 지금은 스페이스 엑스 AI에서
[00:51] 그록봇이라는 제품을 만듭니다.
[00:53] 발표 제목은 이렇습니다.
[00:55] 모든 코드는 슬롭이다, 내 것만
[00:56] 빼고.
[00:57] 슬롭은 AI가 대충 찍어낸 질 낮은
[01:00] 결과물을 가리키는 말입니다.
[01:01] 첫 슬라이드가 [음악] 이 농담을
[01:03] 그림으로 보여줍니다.
[01:04] 우리의 영웅적인 4,000줄짜리
[01:05] PR, 저들의 야만적인
[01:07] 4,000줄짜리 PR.
[01:08] 똑같은 물건인데 남의 것만 슬롭으로
[01:10] 보인다는 겁니다.
[01:21] [웃음]
[01:28] [음악]
[01:31] 텐이 보기에 에이전트 덕분에 이제
[01:33] 누구나 코드를 쏟아낼 수 있습니다.
[01:35] 그러니 엔지니어의 일은 양을 크게
[01:37] 늘리면서 품질을 지키거나 더 올리는
[01:39] 방법을 찾는 것이라고 합니다.
[01:44] >> [음악]
[01:57] [음악]
[02:10] >> 여섯 달이 걸렸다고 합니다. 그 여섯
[02:11] 달 동안 뭘 했는지가 오늘의
[02:13] 내용입니다. [음악]
[02:14] 테는 시간을 어디에 쓸지 정할 때
[02:16] 거꾸로 선 피라미드 그림을 봅니다.
[02:18] 맨 위 가장 넓은 층이 코드
[02:20] 베이스입니다. API 설계와
[02:22] 아키텍처, 리팩토링이 여기에
[02:23] 들어갑니다.
[02:24] 그 아래가 정적 분석입니다. 린트
[02:26] 규칙, 타입, 컴파일러, [음악]
[02:28] 테스트입니다.
[02:29] 여기까지 두 층은 결정적입니다. 몇
[02:31] 번을 돌려도 같은 답이 나옵니다.
[02:33] 그 아래가 검증이고 그 다음이 글로
[02:35] 쓴 지시입니다. 규칙 파일, 스킬,
[02:37] 에이전트 MD 같은 것들입니다.
[02:39] 맨 아래에 가장 좁은 칸이 사람의
[02:41] 리뷰입니다.
[02:42] 보통은 반대로 합니다. 에이전트가
[02:44] 틀리면 지시문에 한 줄을 더
[02:46] 적습니다.
[02:47] 테는 그 순서를 뒤집으라고 합니다.
[03:04] 글은 에이전트가 읽고도 안 따를 수
[03:06] 있기 때문입니다. 코드로 만든 검사는
[03:08] 통과하지 못하면 거기서 멈춥니다.
[03:11] 왜 코드 베이스가 맨 위일까요?
[03:13] 에이전트는 입력을 보고 출력을
[03:14] 만듭니다.
[03:15] 그리고 가장 큰 입력 가운데 하나가
[03:17] 코드 베이스입니다. 테는 10월에
[03:19] x에 이렇게 적습니다. 코드 베이스는
[03:21] 기억이다.
[03:23] 테는 [음악] 2024년을
[03:24] 떠올립니다. 출근해서 동료가 쓴 PR
[03:26] 세 개를 리뷰하던 때입니다.
[03:28] 지금 그 숫자는 300개에 가깝다고
[03:30] 합니다.
[03:31] 엔지니어 한 명이 에이전트 수백,
[03:32] 수천을 거느린 팀이 됐고 코드는
[03:34] 끊이지 않는 물줄기처럼 들어옵니다.
[03:36] 그래서 테는 이 일을 정원 가꾸기에
[03:38] 빗댑니다.
[03:39] 이 정원의 잡초는 코드에 남은 임시
[03:41] 방편입니다. [음악] 임시 방편
[03:43] 하나, 낡은 패턴 하나가 코드에 남아
[03:45] 있으면 다음 에이전트는 그걸 이
[03:47] 저장소의 관례로 읽고 그대로
[03:48] 베낍니다. 슬라이드의 문장
[03:50] 대로입니다. 한 번 베낄 때마다
[03:52] 다음에 또 베낄 가능성이 커집니다.
[03:54] 테니 전에 일한 커서에서 이게 실제로
[03:56] 벌어진 적이 있습니다.
[03:58] 9월 9일 에이전트가 화면 깜빡임
[03:59] 하나를 고칩니다.
[04:01] 방법은 셋 타임아웃, 그러니까
[04:02] 타이머로 살짝 밀어주는 거였습니다.
[04:05] 그리고 주석을 한 줄 답니다. 나중에
[04:07] 해제한다. 혹시 다시 돌아올 수
[04:08] 있으니까. [음악]
[04:10] 제대로 고치지 않은 이유도
[04:11] 남겼습니다. 그건 더 큰 변경이 될
[04:13] 거라서.
[04:14] 10월 3일을 이 코드가 공용 모듈로
[04:16] 복사됩니다.
[04:17] 그리고 10월 17일 타이머는
[04:19] 183개가 돼 있었습니다.
[04:22] 텐의 설명으로는 원인이 더 깊은 데
[04:24] 있었습니다. [음악]
[04:25] VS 코드의 명령형 방식과 리액트의
[04:28] 선언형 방식이 부딪히는 [음악]
[04:29] 자리를 에이전트가 타이머로 덮고
[04:31] 있었던 겁니다.
[04:34] 타이머가 빠르게 생기고 사라지면
[04:35] 가비지 컬렉션이 크게 돌고 앱이
[04:37] 버벅거립니다. 실제로 성능이
[04:39] 나빠졌다고 합니다.
[04:40] [음악] 텐이 가장 나빴다고 꼽은 건
[04:42] 주석입니다.
[04:44] 주석이 이 임시방편은 괜찮다고 설명해
[04:46] 주니까 다음 에이전트가 안심하고
[04:48] 따랐다는 겁니다.
[04:50] 그래서 그록봇 팀은 주석의 99%를
[04:52] 금지하기로 합니다. 슬라이드의
[04:54] 숫자입니다. 7월 31일에
[04:55] 65,824.
[04:57] 발표 시점에는 1,227입니다.
[05:05] [음악]
[05:15] [음악]
[05:26] [음악]
[05:34] 주석 대신 들어간 건 린트
[05:35] 규칙입니다. [음악] 타이머를 쓰면
[05:36] 검사가 막습니다. 그리고 오류
[05:38] 메시지에는 에이전트가 읽을 지시가
[05:39] 적혀 있습니다. 덮지 말고 근본
[05:41] 원인을 고치라는 겁니다.
[05:43] 이 방식은 텐이 공개한 스킬 묶음
[05:45] 피스택에도 들어있습니다. 노
[05:47] 코멘트라는 스킬이 리비전의 주석을
[05:48] 걷어냅니다.
[05:49] 주석이 말하던 제약이 진짜라면 주석이
[05:51] 아니라 타입이나 검사로 옮겨 적으라는
[05:53] 겁니다.
[05:55] 그록봇 팀이 만든 프레임워크 듄에도
[05:57] 같은 원리가 들어있습니다.
[05:58] 텐의 표현으로는 일렉트론 앱을 위한
[06:00] 넥스트 JS 같은 겁니다.
[06:02] 듄에 담긴 교훈 하나. 잘 쓰려면
[06:05] 미묘한 판단이 필요한 건 되게
[06:06] 슬로우로 이어진다.
[06:13] >> [음악]
[06:27] [음악]
[06:33] >> 제품 코드에서는 아예 못 쓰게 했고
[06:35] 뷰 안쪽 몇 군데에서만 허용했습니다.
[06:37] 리뷰에서 이걸 잡아낼 일 자체가
[06:39] 없어졌습니다. 폴더 구조도
[06:40] 규칙입니다. 일렉트론 렌더러,
[06:42] 일렉트론 메인. 최상위 폴더 이름이
[06:44] 그대로 경계입니다.
[06:46] 둘 사이의 임포트는 [음악]
[06:47] 의존성 분석기와 린트가 막습니다.
[06:49] 메인 스레드 코드를 렌더러로 끌어와
[06:51] 화면이 버벅이던 커서 시절의 실수를
[06:53] 구조로 막은 겁니다.
[06:55] 에이전트를 고쳐 줄 때마다 이런
[06:57] 검사가 하나씩 쌓입니다. [음악]
[06:58] 슬라이드의 계단 그래프는 7월에
[07:00] 7에서 시작해 11월에 167까지
[07:03] 올라갑니다.
[07:04] 발표에서 단위는 말하지 않았지만
[07:05] 제목은 에이전트를 바로잡을 때마다
[07:08] 입니다.
[07:20] [음악]
[07:25] 그렇다고 아무것도 안 보는 건
[07:26] 아닙니다. 보는 대상이 바뀌었습니다.
[07:28] 코드 대신 검증 결과물을 봅니다.
[07:30] 영상, 스크린샷, 다이어그램입니다.
[07:33] 기본은 런타임 검증입니다. 에이전트가
[07:35] 앱을 직접 실행하고 사람이 쓰는
[07:37] 디버깅 도구를 그대로 쓰게 하는
[07:38] 겁니다.
[07:39] 여기에 기능 지도가 붙습니다. 앱에
[07:41] 어떤 기능이 있고 사용자가 거기까지
[07:43] 어떻게 가는지 적어 둔 문서입니다.
[07:45] 왼쪽 사이드바에 그거 라고만 해도
[07:47] 에이전트가 헤매지 않습니다.
[07:49] 최근에는 형식 검증도 씁니다. 여러
[07:51] 기기에 걸친 알림 같은 주요 흐름은
[07:53] TLA 플러스로 모델을 검사합니다.
[07:55] 직접 만든 가상화 라이브러리의
[07:57] 알고리즘은 린으로 증명합니다. 화면이
[07:59] 깜빡이거나 떨리지 않는지 확인하는
[08:00] 용도입니다.
[08:02] 테는 이걸로 버그를 꽤 찾았다고
[08:03] 하면서도 맞는 건 아니고 아직 실험
[08:05] 중이라고 선을 긋습니다.
[08:07] 테는 엔지니어 신디, 쓰리다라는 글
[08:09] 두 개를 나란히 놓습니다. 먼저
[08:11] 5월의 글입니다.
[08:12] AI가 만든 PR 여러 개가 미묘한
[08:14] 버그를 안고 머지됐고 고치는데 며칠이
[08:16] 더 들었다.
[08:20] 여섯 달 뒤 같은 사람이 씁니다.
[08:22] 그때 내게 없던 건 검증 과정이었다.
[08:24] 지금은 하루 토큰의 70%가 패치를
[08:26] 검증하는 데 들어간다.
[08:28] 텐도 자기 토큰 대부분이 검증에
[08:30] 들어간다고 말합니다.
[08:31] 새로운 기법은 없습니다. 예전에는
[08:33] 비싸서 못 하던 테스트를 에이전트가
[08:35] 싸게 만들어 준 겁니다.
[08:37] 이제 처음의 숫자로 돌아가겠습니다.
[08:39] 6월에는 809개였습니다. 그록봇
[08:41] 팀이 10월에 머지한 PR은
[08:42] 19,226개입니다. [음악]
[08:44] 안정 버전은 하루에 한 번 꼴로
[08:45] 나옵니다.
[08:46] 10월에 PR을 하나라도 올린 사람은
[08:48] 227명입니다. 맥락을 잘 모르는 채
[08:50] 지나가다 고친 사람도 많습니다.
[08:52] 그런데도 되돌린 커밋의 비율은 6 월
[08:54] 0.98%에서 8월 이후 0.47%
[08:57] 안팎에 머뭅니다.
[08:58] 성능표도 나왔습니다. 5월과 지금을
[09:00] 비교한 표에서 콜드 실행은 39%
[09:02] 빨라졌습니다.
[09:03] 다만 같은 표에 빨간 숫자도
[09:05] 있습니다. 대기 중 메모리는 12%,
[09:07] 대기 중 CPU는 100%
[09:08] 늘었습니다.
[09:09] 텐의 표현은 여러 면에서 나아졌다
[09:11] [음악] 였습니다. 전부는 아닙니다.
[09:14] 그럼 우리도 에이전트 공정부터 지우면
[09:15] 될까요?
[09:16] 텐의 답은 아직 [음악] 아니다
[09:18] 입니다.
[09:33] [음악]
[09:44] [음악]
[09:57] 이 기초가 깔리면 어떤 일이
[09:58] 가능해질까요?
[10:00] 텐은 릴리스 날 벌어지는 일을 예로
[10:01] 듭니다.
[10:10] >> [음악]
[10:22] [음악]
[10:27] >> 슬라이드에 나온 한 번의 결과입니다.
[10:29] 서로 다른 버그 50개, 새로 생긴
[10:31] 것 세 개, 원래 있던 것 47개.
[10:34] 다만 숫자는 모두 텐 팀이 직접
[10:36] 집계한 것이고 발표 끝에는 자사 제품
[10:38] 소개가 붙습니다.
[10:39] 텐 본인도 X에 이렇게 적었습니다.
[10:41] 이건 사람이 빠진 무인 공장이
[10:43] 아니다.
[10:44] 정리하겠습니다. [음악]
[10:45] 하나, 에이전트를 고쳐 줄 일이
[10:46] 생기면 글이 아니라 검사로 남긴다.
[10:49] 둘, 애매한 건 금지한다. 셋,
[10:51] 토큰은 만드는 데보다 확인하는 데 더
[10:53] 쓴 다.
[10:54] 주석을 지웠는데 품질이 올랐다는
[10:55] 처음에 수수께끼는 이렇게 풀립니다.
[10:58] 주석을 지운 게 아니라 주석에 적던
[11:00] 약속을 지킬 수 밖에 없는 검사로
[11:01] 옮긴 겁니다.
[11:04] 발표의 마지막 슬라이드는 제목을 살짝
[11:06] 바꿉니다.
[11:07] 모든 코드는 슬롭이다.
[11:09] 당신 것만 빼고.

## 트랜스크립트 — en-orig (영어 더빙 ASR — 인용하지 않음)

[00:00] Last October, one engineer pushed 3,127
[00:03] PRs to production.
[00:11] The entire team this person belongs to
[00:13] merged 1,926 PRs in a single month.
[00:18] You’d expect a mess, but the revert rate
[00:20] actually dropped from 0.98%in June to
[00:22] 0.47%in October.
[00:24] However, there is something strange
[00:26] about what this team did.
[00:27] They deleted almost all the comments in
[00:28] their code. The number, which used to
[00:30] exceed 65,000, is now just over 1,200.
[00:33] Why did quality improve even after
[00:34] removing the comments?
[00:35] Today, we will trace the journey of how
[00:36] this team came to trust agents.
[00:39] The speaker is Lauren Tan.
[00:41] She is better known online by the name "
[00:42] Potato."
[00:43] She worked at Meta, Netflix, and Cursor
[00:45] , and helped build the React Compiler on
[00:47] the React Core team.
[00:49] She now builds a product called the Grok
[00:52] bot at xAI.
[00:53] The title of her talk is as follows.
[00:55] "All Code is Slop, Except for Mine."
[00:57] "Slop" refers to low-quality output
[00:59] hastily churned out by AI.
[01:01] The first slide illustrates this joke
[01:03] visually.
[01:04] "Our heroic 4,000-line PR" versus "
[01:06] Their barbaric 4,000-line PR."
[01:08] It means that while the work is
[01:09] identical, only others 'code looks like
[01:11] slop.
[01:31] In Tan’s view, thanks to agents, anyone
[01:32] can now churn out code. So, she says the
[01:35] engineer’s job is to find ways to
[01:38] maintain or improve quality while
[01:40] significantly increasing volume.
[02:10] >> She says it took six months. What they
[02:11] did during those six months is today’s
[02:13] topic.
[02:14] Tan looks at an inverted pyramid diagram
[02:16] when deciding where to spend her time.
[02:19] The top, widest layer is the codebase.
[02:21] This includes API design, architecture,
[02:23] and refactoring.
[02:24] Below that is static analysis. Lint
[02:26] rules, types, compilers, and tests.
[02:29] These two layers are deterministic. No
[02:31] matter how many times you run them, you
[02:32] get the same answer.
[02:33] Below that is validation, and then
[02:35] written instructions. Things like rule
[02:37] files, skills, and agent.md files.
[02:40] At the very bottom, in the narrowest
[02:41] section, is human review.
[02:42] Usually, people do it the other way
[02:43] around. When an agent makes a mistake,
[02:45] they add another line to the
[02:46] instructions.
[02:47] Tan says you should reverse that order.
[03:04] That is because an agent can read
[03:05] instructions and still choose not to
[03:06] follow them. Checks built into the code
[03:08] stop the process if they aren’t passed.
[03:11] Why is the codebase at the very top?
[03:13] Agents create output by looking at input
[03:15] .
[03:16] And one of the biggest inputs is the
[03:17] codebase.
[03:18] In October, Tan wrote this on X. "The
[03:20] codebase is memory."
[03:23] Tan reflects on the year 2024. There was
[03:25] a time when I would clock in and review
[03:27] three PRs written by colleagues.
[03:28] They say that number is now close to 300
[03:30] .
[03:31] One engineer has become a team managing
[03:33] hundreds or thousands of agents, and
[03:34] code flows in like a ceaseless stream.
[03:36] That is why Ten compares this work to
[03:38] gardening.
[03:40] The weeds in this garden are the
[03:41] workarounds left in the code.
[03:43] If one workaround or one outdated
[03:44] pattern remains in the code, the next
[03:46] agent reads it as a convention of the
[03:47] repository and copies it as is. It is
[03:49] exactly as the sentence on the slide
[03:50] says. Every time it is copied, the
[03:52] probability of it being copied again
[03:53] increases.
[03:54] This actually happened at Cursor, where
[03:56] Ten worked previously.
[03:58] On September 9, an agent fixed a screen
[03:59] flickering issue.
[04:01] The method was using setTimeout,
[04:02] essentially pushing it back with a timer
[04:04] .
[04:05] And it left a single line of comment. To
[04:06] be removed later.
[04:08] Just in case it might return.
[04:10] It also left the reason for not fixing
[04:11] it properly. Because that would have
[04:12] been a larger change.
[04:14] On October 3, this code was copied to a
[04:16] common module.
[04:17] And by October 17, there were 183 timers
[04:20] .
[04:22] According to Ten's explanation, the root
[04:24] cause was deeper.
[04:26] The agent was covering up the collision
[04:28] between VS Code's imperative style and
[04:29] React's declarative style with timers.
[04:34] If timers are created and destroyed
[04:35] rapidly, garbage collection runs heavily
[04:37] and the app stutters. They say the
[04:39] performance actually degraded.
[04:41] The thing Ten pointed out as the worst
[04:42] was the comment.
[04:44] Because the comment explained that this
[04:46] workaround was fine, the next agent
[04:47] followed it with peace of mind.
[04:50] So the Grok Bot team decided to ban 99%
[04:52] of comments.
[04:53] These are the numbers on the slide. On
[04:55] July 31, it was 65,824. At the time of
[04:57] the presentation, it is 1,227.
[05:34] What replaced the comments were lint
[05:35] rules. If you use a timer, the check
[05:37] blocks it. And the error message
[05:38] contains instructions for the agent to
[05:40] read. It tells them to fix the root
[05:41] cause rather than covering it up.
[05:43] This approach is also included in the
[05:45] skill bundle' Pistack 'that Ten released
[05:46] . A skill called' No Comment 'strips
[05:48] away comments from revisions.
[05:50] It means if the constraints mentioned in
[05:51] the comment are real, they should be
[05:52] moved to types or checks, not comments.
[05:55] The same principle is embedded in' Dune
[05:56] ', a framework created by the Grok Bot
[05:57] team.
[05:58] In Ten's words, it's like Next.js for
[06:01] Electron apps.
[06:02] One lesson contained in Dune.
[06:04] Anything that requires subtle judgment
[06:06] to use well leads to slowness.
[06:33] >> They made it completely unusable in
[06:34] production code, allowing it only in a
[06:35] few places inside the view.
[06:37] The need to catch this in reviews
[06:38] disappeared entirely. Folder structure
[06:40] is also a rule. Electron renderer,
[06:42] Electron main. The top-level folder
[06:44] names are the boundaries themselves.
[06:46] Imports between the two are blocked by
[06:47] dependency analyzers and linting.
[06:49] This structurally prevents the kind of
[06:51] mistakes from the early Cursor days,
[06:52] where dragging main thread code to the
[06:53] renderer caused screen stutters.
[06:55] Every time the agent is corrected, these
[06:57] checks accumulate one by one. The step
[06:59] graph on the slide starts at 7 in July
[07:01] and climbs to 167 by November.
[07:04] The presentation didn't specify the unit
[07:06] , but the title says "every time the
[07:07] agent is corrected."
[07:25] That doesn't mean nothing is being
[07:26] reviewed. What is being reviewed has
[07:28] changed. Instead of code, they look at
[07:29] verification results. Videos,
[07:31] screenshots, and diagrams.
[07:33] The foundation is runtime verification.
[07:35] The agent runs the app directly and uses
[07:36] the same debugging tools that humans use
[07:38] .
[07:39] A feature map is attached to this. It's
[07:41] a document describing what features the
[07:42] app has and how users navigate to them.
[07:45] Even if you just say "that" in the left
[07:46] sidebar, the agent doesn't get lost.
[07:48] Recently, they have also been using
[07:50] formal verification. Key workflows, like
[07:51] notifications across multiple devices,
[07:53] are checked using TLA + models.
[07:55] Algorithms in their custom
[07:56] virtualization library are proven with
[07:58] Lean. This is used to ensure the screen
[08:00] doesn't flicker or jitter.
[08:02] Te notes that while this found quite a
[08:03] few bugs, they draw the line by saying
[08:05] it's not perfect and still experimental
[08:06] .
[08:07] Te places two posts by engineer Cindy
[08:09] side-by-side. First, the post from May.
[08:12] "Several AI-generated PRs were merged
[08:14] with subtle bugs, taking days longer to
[08:17] fix."
[08:20] Six months later, the same person writes
[08:21] .
[08:22] "What I lacked back then was a
[08:23] verification process."
[08:24] "Now, 70%of my daily tokens go toward
[08:26] verifying patches."
[08:28] Ten also says that most of his tokens
[08:30] are spent on verification.
[08:31] There are no new techniques. Tests that
[08:33] were too expensive to run before have
[08:35] been made affordable by the agent.
[08:37] Now, let's return to the initial numbers
[08:38] . In June, it was 809. The Grok Bot team
[08:42] merged 19,226 PRs in October.
[08:44] Stable versions are released about once
[08:45] a day.
[08:46] There are 227 people who submitted at
[08:48] least one PR in October. Many of them
[08:49] were people passing by who made fixes
[08:51] without knowing the full context.
[08:52] Yet, the rate of reverted commits
[08:54] remains around 0.47%since August, down
[08:56] from 0.98%in June.
[08:58] Performance charts were also released.
[08:59] In the chart comparing May to now, cold
[09:01] starts are 39%faster.
[09:03] However, there are also red numbers on
[09:05] the same chart. Idle memory increased by
[09:07] 12%, and idle CPU increased by 100%.
[09:09] Ten's description was that it has
[09:11] improved in many aspects. Not in all.
[09:14] Should we then remove the agent process
[09:15] as well?
[09:17] Ten's answer is "not yet."
[09:57] Once this foundation is laid, what
[09:58] becomes possible?
[10:00] Ten uses what happens on release day as
[10:01] an example.
[10:27] >> It's a single result shown on the slide
[10:28] . 50 distinct bugs: three new ones, 47
[10:32] pre-existing ones.
[10:34] However, all the numbers were tallied by
[10:36] the Ten team, and a product pitch
[10:37] follows at the end.
[10:39] Ten himself also wrote this on X. This
[10:41] is not an unmanned factory without
[10:43] people.
[10:44] Let me summarize.
[10:45] First, when an agent needs a fix, leave
[10:47] it as a test, not text.
[10:49] Second, ambiguity is prohibited. Third,
[10:51] use more tokens for verification than
[10:52] for generation.
[10:54] The initial mystery of how quality rose
[10:55] after deleting comments is solved this
[10:57] way.
[10:58] You didn't delete the comments; you
[11:00] moved the promises in them to tests that
[11:01] must be kept.
[11:04] The final slide of the presentation
[11:05] slightly changes the title.
[11:07] All code is slop.
[11:09] Except for yours.
