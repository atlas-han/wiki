---
title: "AI로 10배 빨라졌다면, 30년치 발전은 어디 갔나 | Jonathan Blow"
type: video
source: https://www.youtube.com/watch?v=oCEJgCOLEIs
site: youtube.com
author:
  - "[[Tech Bridge]]"
duration: 12:10
published: 2026-11-19
created: 2026-11-20
description: "Tech Bridge 한국어 해설 12:10, 공식 챕터 10, Korean original + 영어 더빙(en-orig는 더빙의 ASR이되 원 대담 발췌 구간에서는 Blow의 영어 원음이 잡힌다 — ko-orig는 그 구간이 무캡션). Braid · The Witness 개발자 Jonathan Blow의 The Students 대담을 따라간 정리 — 10배 × 3년 = 30년치인데 본 것은 대략 0년, 엑셀 VBA 30줄 5시간 → 1시간, 조각 사이의 선(영향과 제약)과 감으로 가는 AI, 말귀를 알아듣는 검색, 더 많은 코드는 기술 부채, 1990년 유닉스 워크스테이션과 systemd 약 171만 줄, Alpine Linux 로그인 버그, 쓰레기 매립지, 규칙으로 배우는 코딩 AI 구상(AlphaZero), 버그 훑기는 유용. 수치는 Blow의 암산과 추정(설명란)."
tags:
  - clippings/youtube
---

**Source URL**: https://www.youtube.com/watch?v=oCEJgCOLEIs
**Channel**: Tech Bridge · **Duration**: 12:10 · **Published**: 2026-11-19

> **게시일.** info.json `upload_date` **`20261119`**, `timestamp` 1795125623(= 2026-11-19 22:00:23 UTC = **2026-11-20 07:00 KST**), `availability`=`public`. 2026-11-20 회차(09:10 KST) 두 시간쯤 전에 올라왔다. 파일명에서 `|` · 쉼표는 뺐다.
>
> **오디오 트랙과 자막 — 인용 규칙.** 오디오는 **Korean original(default) + 영어 더빙**(audio language `ko` · `en` · `en-US`), 메타 `language`=`en`. 수동 자막 없음. `ko` = `ko-orig`(파일 동일, `kind=asr&lang=ko&variant=gemini`). `en-orig`(`kind=asr&lang=en&variant=timing-optimized`)는 **영어 더빙 트랙의 ASR** 이다 — 첫 줄부터 내레이션의 영어 번역이 나온다(*"30 years of progress in just 3 years."*). → **내레이션 인용은 ko-orig 하나.** 더빙 부분은 인용하지 않고 판독 대조용으로만 쓴다.
> ⭐ **다만 이 편은 원 대담(The Students) 발췌가 길고, 그 구간에서 en-orig에 Blow의 영어 원음이 잡힌다.** ko-orig는 같은 구간이 `[음악]` 표시뿐이거나 비어 있다(ko ASR이 영어를 받아쓰지 않음). 발췌로 판정한 근거: (1) ko-orig의 무캡션 구간과 겹친다 — 그 시간에 한국어 내레이션이 없다, (2) 더빙이 다시 시작하는 줄에 화자 전환 표시 `>>`가 붙는다, (3) 더빙의 다듬어진 문장과 달리 *um* · *right?* · 말 고침이 있는 구어다. **이 발췌는 "en-orig에만 잡힌 원음 ASR"로 표시하고 인용한다** — 두 트랙 교차 확인은 없다(11-18 Astra 편은 발췌가 두 트랙에 같은 영어로 잡혔고, 이 편은 그렇지 않다). ⚠️ 화자 구분은 캡션에 없다 — 대담이라 진행자의 말이 섞였을 수 있다(예: 07:07 *Yeah.* · 10:25 *Yeah. Well, and also …*). 429 없음.
>
> **en-orig에 원음이 잡힌 발췌 구간.** 01:57~02:02 · 02:22~02:55 · 03:30~04:04 · 04:51~05:30 · 06:12~06:31(조각) · 07:03~07:27 · 08:16~08:25(조각) · 09:59~10:46.
>
> **두 트랙 모두 무캡션인 구간(`gaps.py` 4.5초 기준) — 내용 미상.** 00:08~00:14(*"직접 세어본 결과는 이렇습니다"* 뒤) · **00:49~01:10**(챕터 제목의 *다리 비유* 자리 — **비유의 내용이 캡션에 없다**) · **01:30~01:36**(*"블로의 질문은 하나입니다."* 뒤 — **질문의 원문이 없다**) · 01:41~01:57(암산의 앞부분) · 03:25~03:30 · 04:43~04:51 · 06:07~06:12 · 06:55~07:03 · 08:25~08:35 · 09:55~09:59 · **11:35~11:47**(*"본인의 컴파일러를 고칠 때의 얘기입니다."* 뒤 — **그 얘기가 없다**). 발췌 구간 안에서도 03:23~03:30 · 06:25~06:37 · 08:21~08:25 · 10:38~10:51은 조각만 잡혔다(*"Redory."* · *"numbers because / other"* · *"LM"*).
>
> **ASR 판독(ko-orig → 판독, 괄호는 근거).** *블로거*(02:07 · 03:05 · 03:08) → 블로, *모두들 좋아질수록*(01:23~01:25) → 모델이 좋아질수록(en-orig 더빙 *as the models improved*), *처음 보는 원어*(04:18) → 처음 보는 언어(en-orig *a language*), *뭐와 다를까요*(04:22~04:24) → 뭐가 다를까요, *선이 더 빨리 듭니다*(04:31~04:33) → 빨리 늡니다(en-orig *grow faster*), *셋 게임*(05:55) → 새 게임(en-orig *a new game*), *그래 모양은*(06:41) → 겉모양은(추정 — en-orig *It looks like reasoning*), *기소 부채*(06:46) → 기술 부채(tags · en-orig *technical debt*), *블로의 개선으로는*(07:33) → 블로의 계산으로는(en-orig *calculations*), *어느 선을 넣으면*(07:35~07:37) → 어느 선을 넘으면(en-orig *cross a certain threshold*), *시스템 D*(08:39 · 08:45) → systemd(tags), *포로닉스*(08:47) → Phoronix(설명란), *해성 저장소*(08:49) → 해당 저장소(추정 — en-orig *the repository*), *옥스*(09:13) → OX Security(설명란), *규칙으로 배우는 적에*(10:51) → 배우는 쪽에(추정), *사람의 기부 없이 혼자 두면서*(11:02~11:05) → 사람의 기보 없이 혼자 두면서(en-orig *by playing on its own without human input*), *처음 숫자으로*(11:15) → 처음 숫자로, *비즈로 남고*(11:22) → 빚으로 남고(en-orig *remains as debt*), *스코버를 코드*(11:49) → 쓰고 버릴 코드(en-orig *throwaway code*), *사람이 주고 있습니다*(11:54~11:55) → 사람이 쥐고 있습니다(추정 — en-orig 더빙은 *humans must provide the map*).
> **en-orig 원음 발췌의 ASR 판독.** *since 2003*(01:57) → **2023으로 추정**(내레이션 *3년쯤*, 10배 × 3년 = 30년) — 미확정, *as server*(02:55) · *Even though programmed in many languages*(03:30) · *They kind of being it*(05:24) · *Redory*(08:25) · *sometimes like you know 10 times longer times longer*(07:22~07:24) → 판독 불가 또는 조각. en-orig 더빙은 Blow를 중간부터 *Bloh* 로 적는다.
>
> ⚠️ **두 트랙이 갈리는 곳.** 재생 수 — ko-orig *"공개 사흘만에 24만번 가까이"*(00:18~00:20), en-orig 더빙 *within four days*. 위키는 ko(원 내레이션)를 따르되 미확인으로 둔다.
>
> ⚠️ **해설이고 2차 전달이다 — 수치는 측정값이 아니다.** 설명란: *"30년/0년, 5시간/1시간은 측정값이 아니라 Blow의 암산과 추정입니다. 대담에서 부정확한 대목(AlphaZero)은 영상 안에서 바로잡았습니다."* 위키는 설명란의 네 출처(원본 대담 `IRK8h67ol7Q` · 2019년 강연 `pW-SOdj4Kkk` · OX Security 글 · Phoronix 기사)를 **열지 않았다.** systemd 줄 수 · Alpine Linux 버그의 날짜와 원인은 해설이 그 글들에서 옮긴 것이다.

## 설명란

AI로 코딩 생산성이 10배가 됐다면, 3년 동안 30년치 소프트웨어 발전이 보여야 합니다. Braid와 The Witness를 만든 개발자 Jonathan Blow가 The Students 대담에서 본 숫자는 "대략 0년"이었습니다. 그 많은 코드는 다 어디로 갔을까요?

Blow 자신도 AI를 씁니다. 5시간 걸릴 엑셀 작업을 1시간에 끝냈다고 말합니다. 그런데도 AI가 코딩을 잘한다고는 보지 않습니다. 이 영상은 대담의 흐름을 따라 30줄짜리 코드와 시스템의 차이, AI를 "알아듣는 검색"이라고 부르는 이유, 더 많은 코드가 빚이 되는 과정, 소프트웨어가 원래부터 쌓이기만 한 산업이라는 주장, 그리고 Blow가 그리는 대안까지 정리합니다.

30년/0년, 5시간/1시간은 측정값이 아니라 Blow의 암산과 추정입니다. 대담에서 부정확한 대목(AlphaZero)은 영상 안에서 바로잡았습니다.

타임라인
0:00 3년 만에 30년치, 그런데 0년
0:31 Jonathan Blow, 그리고 다리 비유
1:18 30년은 어떻게 나온 숫자인가
3:08 Blow도 AI를 쓴다: 5시간 → 1시간
4:22 30줄과 시스템은 무엇이 다른가
5:39 AI는 "알아듣는 검색"
6:46 더 많은 코드는 빚이다
7:58 소프트웨어는 원래 쌓이기만 했다
9:35 그럼 영영 안 되나: Blow의 대안
11:15 다시 30년과 0년

참고
원본 대담 (The Students): https://www.youtube.com/watch?v=IRK8h67ol7Q
2019년 강연 "Preventing the Collapse of Civilization": https://www.youtube.com/watch?v=pW-SOdj4Kkk
OX Security, OpenSSH 인증 우회 CVE-2026-123158: https://www.ox.security/blog/openssh-authentication-bypass-cve-2026-123158/
Phoronix, systemd 저장소 통계(2022): https://www.phoronix.com/news/systemd-Git-Stats-2022

#JonathanBlow #AI코딩 #소프트웨어 #기술부채

> info.json `tags`: AI 생산성 · AI 코딩 · AlphaZero · Braid · Jonathan Blow · LLM · The Students · The Witness · systemd · 개발자 · 기술 부채 · 바이브 코딩 · 소프트웨어 복잡도 · 조너선 블로

## 트랜스크립트 — ko-orig (오디오 ko(Korean original), ASR variant=gemini — 내레이션)

[00:00] 3년만에 30년치 발전.
[00:02] AI 코딩이 정말 10배 빠르다면
[00:04] 나왔어야할 숫자입니다.
[00:06] 그런데 이 프로그래머가 직접 세어본
[00:08] 결과는 이렇습니다.
[00:14] 조너선 블로, 브레이드와 더
[00:16] 위트니스를 만든 게임 개발자입니다.
[00:18] 이 대담은 공개 사흘만에 24만번
[00:20] 가까이 재생됐습니다.
[00:22] 그럼 AI가 쏟아낸 그 많은 코드는
[00:24] 다 어디로 갔을까요?
[00:26] 블로 본인이 AI로 5시간짜리 일을
[00:28] 1시간에 끝낸 얘기까지 따라가
[00:30] 봅니다.
[00:31] 블로는 2019년 모스크바에서
[00:33] 문명의 붕괴를 막는 법이라는 강연을
[00:35] 했습니다. 소프트웨어가 복잡해질수록
[00:38] 점점 못 믿을 물건이 된다는
[00:39] 내용이었습니다.
[00:40] 이번 대담도 같은데서 시작합니다.
[00:42] 엔지니어는 현실의 제약을 이해하고
[00:44] 원하는 결과를 만들어내는 사람이라는
[00:46] 겁니다.
[00:51] [음악]
[01:10] 버튼 하나를 눌러도 무슨 일이 생길지
[01:11] 모르는 웹페이지. [음악] 블로가
[01:13] 보기에 소프트웨어는 AI 이전부터
[01:15] 이랬습니다. 그 위에 AI가 올라온
[01:17] 겁니다.
[01:18] AI가 코드를 대신 써준다는 얘기가
[01:20] 나온지 3년쯤 됐습니다. 생산성이
[01:23] 올랐다는 주장도 모두들 좋아질수록
[01:25] 늘었죠.
[01:26] 블로의 질문은 하나입니다.
[01:36] 그러고는 그 자리에서 직접 암산을
[01:38] 해봅니다.
[01:47] >> [음악]
[02:05] >> 10배에 3년이면 30년치. 그런데
[02:07] 블로거가 본 건 대략 0년입니다.
[02:10] 너무 후하게 쳤나 싶어 다시 셉니다.
[02:12] 1년 반 전부터 다섯 배만 올랐다고
[02:14] 쳐도 7, 8년치. 그것도 안
[02:16] 보인다고 합니다.
[02:17] 다만 오해하지 말라며 본인이 먼저
[02:19] 선을 긋습니다.
[02:29] [음악]
[02:38] [음악]
[02:48] [음악]
[03:00] AI 기술은 진짜 발전이지만 쓰는
[03:02] 사람 눈에는 소프트웨어가 나아진 게
[03:03] 안 보인다는 겁니다. 이건 통계가
[03:05] 아니라 블로거 한 사람의 관찰입니다.
[03:08] 블로거가 AI를 안 쓰는 건
[03:09] 아닙니다.
[03:10] 얼마 전에는 남에게 줄 엑셀 표에
[03:11] 색을 입혀야 했습니다.
[03:13] 프로그램이 뽑은 CSV 파일을 엑셀로
[03:15] 열어 조건에 맞는 칸에 색과 굵은
[03:17] 글씨를 넣는 일입니다. AI는 30줄
[03:20] 좀 되는 비주얼 베이직 코드를 거의
[03:22] 한 번에 내놨습니다.
[03:34] >> [음악]
[03:47] [음악]
[04:08] >> 다섯 시간이 한 시간으로
[04:10] 다섯 배입니다.
[04:11] 블로는 사람들이 AI가 코딩을
[04:13] 잘한다고 믿게 되는 이유가 이런
[04:15] 경험이라고 봅니다.
[04:16] 다만 조건이 셋 붙어 있었습니다.
[04:18] 처음 보는 원어였고, 서른 줄이었고,
[04:20] [음악]
[04:20] 쓰고 버릴 코드였습니다.
[04:22] 서른 줄짜리와 큰 프로그램은 뭐와
[04:24] 다를까요? 블로는 허공에 점을 찍어
[04:26] 가며 설명합니다.
[04:28] 프로그램 조각이 셋이면 그 사이에
[04:30] 그을 수 있는 선은 셋, 넷이면
[04:31] 여섯입니다. 조각보다 선이 더 빨리
[04:33] 듭니다.
[04:34] 이 선은 코드에 적혀 있지 않습니다.
[04:36] 여기를 이렇게 짜면 저기가 어떻게
[04:38] 되는지 그 영향과 제약이 선입니다.
[04:41] [음악]
[05:11] [목을 가다듬음]
[05:14] [음악]
[05:22] [음악]
[05:28] [콧방귀]
[05:31] 감으로 간다. 블로의 표현입니다.
[05:34] 서른 줄에서는 티가 안 나다가
[05:35] 프로그램이 어느 크기를 넘으면
[05:37] 드러난다는 겁니다.
[05:39] 그럼 AI가 실제로 하는 일은
[05:40] 뭘까요? 블로는 요즘 AI를 말귀를
[05:43] 알아듣는 검색 알고리즘으로
[05:45] 생각한답니다.
[05:46] 아주 큰 탐색을 아주 빠르게 [음악]
[05:47] 해냅니다. 대신 이렇게 짜면 나중에
[05:50] 어떻게 될지를 가리는 판단에는
[05:52] 약하다는 겁니다.
[05:53] 근거로 든 사례는 코드가 아닙니다.
[05:55] 지난 달 셋 게임을 내기 전 AI에게
[05:57] [음악] 첫 달 판매량을 여러 번
[05:59] 예측시켜 봤답니다.
[06:00] AI는 이유를 줄줄이 달아 숫자를
[06:02] 내놨습니다. [음악] 올해 GTA가
[06:04] 나온다는 것까지 챙기면서요.
[06:37] 더 높아야 한다고 해도 맞습니다. 더
[06:39] 낮아야 한다고 해도 맞습니다.
[06:41] 그래 모양은 추론인데 들여다보면
[06:43] 구멍과 건너뛴 자리가 쉽게 보인다는
[06:45] 겁니다.
[06:46] AI가 만든 기소 부채는 AI가
[06:48] 갚으면 되지 않느냐.
[06:50] 진행자가 요즘 자주 듣는 주장을
[06:51] 꺼내자 블로는 이렇게 답합니다.
[07:07] [음악]
[07:14] [음악]
[07:21] [음악]
[07:30] [음악]
[07:33] 블로의 개선으로는 코드가 늘면 줄마다
[07:35] 생기는 오류도 같이 늘고 어느 선을
[07:37] 넣으면 더는 손을 못 댑니다.
[07:39] 코드를 보지 않는 순수한 바이브
[07:40] 코딩은 그 선에 꽤 빨리 닿는다고
[07:42] 봅니다.
[07:43] 반대로 그 선 전에 끝나는 일도
[07:45] 많습니다.
[07:46] 마사지 숍 홈페이지 같은 건 예전엔
[07:48] 돈을 주고 맡겨도 골치였는데 지금은
[07:50] 훨씬 쉬워졌다고 블로도 인정합니다.
[07:52] [음악] 다만 그게 AI가
[07:54] 프로그래밍을 잘한다는 뜻은 아니라고
[07:56] 덧붙입니다.
[07:58] 여기서 진행자가 가설을 하나 냅니다.
[08:00] 생산성은 정말 올랐는데 소프트웨어
[08:02] 산업이 그걸 블랙홀처럼 삼키는 건
[08:04] 아니냐고요.
[08:05] 블로는 대학 시절 얘기로 답합니다.
[08:07] 1990년 그가 쓰던 유닉스
[08:09] 워크스테이션들은 메모리를 보호하고
[08:11] 화면에 창을 띄우고 마우스로
[08:13] 눌렀습니다.
[08:15] [음악]
[08:33] [음악]
[08:35] 하는 일은 같은데 코드는 비교가 안
[08:36] 되게 들었습니다. 블로가 꼽는 예가
[08:39] 시스템 D입니다. [음악]
[08:40] 초기 유닉스에서 부팅 때 할 일은
[08:42] 스크립트 대여섯 줄에서 열 줄이었다고
[08:44] 합니다.
[08:45] 지금 그 자리에 있는 시스템 D는
[08:47] 리눅스 매체의 포로닉스가 2022년
[08:49] 말 해성 저장소 기준으로 약 171만
[08:51] 줄입니다.
[08:52] 블로가 화면에 띄워 달라고 한 그림도
[08:54] 있습니다. 위키백과의 리눅스 배포판
[08:56] 계보입니다.
[08:57] 하나가 갈라지고 또 갈라집니다.
[08:59] 블로는 이들이 하는 일이 대부분
[09:01] 겹친다고 말합니다. 이렇게 층이
[09:03] 쌓이면 사고도 납니다.
[09:05] 이번 달 5일 알파인 리눅스에서 아주
[09:06] 긴 비밀번호를 넣으면 로그인이 뚫리는
[09:09] 버그가 공개됐습니다.
[09:10] 블로가 대담에서 가장 황당한 사례로
[09:12] 꼽은 버그입니다.
[09:13] 보안 업체 옥스의 분석을 보면 10년
[09:15] 넘는 기간에 따로 내려진 결정 세
[09:17] 개가 겹친 결과였습니다.
[09:19] 하나하나는 다 이유가 있었습니다.
[09:21] 블로의 표현으로 우리는 거대한 쓰레기
[09:23] 매립지 위에 삽니다. [음악] 층은
[09:25] 계속 쌓이고 바닥까지 파 내려가기는
[09:27] 어렵습니다.
[09:28] AI가 소프트웨어 품질을 올릴 수도
[09:30] 있지만 [음악] 반대로 갈 가능성이
[09:32] 더 크다는 게 블로의 전망입니다.
[09:35] 그럼 블로는 AI 코딩이 영영 안
[09:37] 된다고 볼까요?
[09:38] 그렇지는 않습니다. 추론 흉내를 계속
[09:40] 잘 내다보면 진짜 추론과 같아진다는
[09:42] 주장에 그는 가능성을 절반 아래로
[09:45] 봅니다. [음악] 영은 아닙니다.
[09:47] 말한 대로 되는 코딩 AI를 만들면
[09:49] 아마 세계에서 가장 값진 회사가 될
[09:50] 것이라며 자기라면 이렇게 만들겠다고
[09:52] 합니다.
[09:53] >> [음악]
[10:02] [음악]
[10:09] [음악]
[10:25] [음악]
[10:32] [음악]
[10:51] >> 코드는 규칙으로 배우는 적에 사람과의
[10:53] 대화는 LLM에 맡기는 구조입니다.
[10:55] 둘을 잇는 방법은 블로도
[10:57] 어떻게든이라고 말했습니다. 구상할 뿐
[10:59] 만든 건 아닙니다.
[11:02] 참고로 알파제로는 규칙은 받고 사람의
[11:04] 기부 없이 혼자 두면서 배운
[11:05] 시스템입니다. [음악] 지금 당장
[11:06] 쓸모 있다고 본 것도 있습니다.
[11:08] AI로 버그를 훑는 일입니다. 린터나
[11:10] 퍼저처럼 프로그램을 곁에 두는
[11:12] 도구로는 분명히 유용하다고 했습니다.
[11:15] 처음 숫자으로 돌아가 보겠습니다.
[11:16] 30년치가 왜 안 보이는지 블로의
[11:19] 말을 이으면 이렇습니다. [음악]
[11:20] AI는 같은 문제에 코드를 더 많이
[11:22] 내고 그 코드는 비즈로 남고
[11:25] 소프트웨어는 원래부터 쌓이기만 해
[11:26] 왔습니다.
[11:27] [음악] 그럼 블로 자신은 어떻게
[11:28] 할까요?
[11:29] 가끔 멈춥니다. 본인의 컴파일러를
[11:31] 고칠 때의 얘기입니다.
[11:38] [음악]
[11:47] 가져갈 건 세 가지만 서른 줄짜리
[11:49] 스코버를 코드에는 AI를 마음껏
[11:51] 씁니다.
[11:52] 오래 살 시스템이라면 조각 사이에
[11:54] 선을 그린 지도는 사람이 주고
[11:55] 있습니다.
[11:56] 그리고 코드가 늘어난 만큼 멈춰서
[11:58] 갚는 시간을 따로 잡습니다.
[12:01] 코드가 빨리 나오는 것과 소프트웨어가
[12:03] 나아지는 것은 다른 일이다.
[12:05] 30년치와 0년 사이에서 블로가 한
[12:07] 얘기는 결국 이것이었습니다.

## 트랜스크립트 — en-orig (영어 더빙 트랙의 ASR — 내레이션 부분은 더빙, 원 대담 발췌 구간은 Blow의 영어 원음)

[00:00] 30 years of progress in just 3 years.
[00:02] That’s the number we should have seen if
[00:04] AI coding were truly ten times faster.
[00:06] But here is the result this programmer
[00:08] calculated for himself.
[00:14] >> Jonathan Blow, the game developer who
[00:16] created Braid and The Witness. This talk
[00:18] reached nearly 240,000 views within four
[00:21] days of its release. So, where did all
[00:23] that code poured out by AI go?
[00:26] We follow the story of how Blow himself
[00:28] finished a five-hour task in one hour
[00:30] using AI.
[00:31] In 2019, Blow gave a lecture in Moscow
[00:33] titled "Preventing the Collapse of
[00:35] Civilization." It argued that as
[00:37] software becomes more complex, it
[00:39] becomes increasingly untrustworthy. This
[00:40] discussion starts from that same point.
[00:42] An engineer is someone who understands
[00:44] real-world constraints and produces
[00:46] desired results.
[01:10] A webpage where you don't know what will
[01:11] happen when you press a single button.
[01:13] In Blow's view, software was already
[01:14] like that even before AI. And now, AI
[01:16] has been layered on top of it.
[01:18] It's been about three years since people
[01:20] started saying AI could write code for
[01:22] us. Claims that productivity has
[01:23] increased have also grown as the models
[01:25] improved. Blow’s question is simple.
[01:36] Then, he performs a mental calculation
[01:38] on the spot.
[01:57] So since 2003 and the system started
[01:59] appearing, we should have had 30 years
[02:02] of software advancement.
[02:05] >> Ten times speed over three years equals
[02:06] thirty years of progress. But what Blow
[02:08] observed is roughly zero years.
[02:10] Wondering if he was too generous, he
[02:12] recalculates. He says that even if we
[02:13] assume productivity only went up
[02:14] fivefold starting a year and a half ago
[02:15] , we still don't see seven or eight
[02:17] years of progress. However, he draws a
[02:19] line first, asking not to be
[02:20] misunderstood.
[02:22] itself is very impressive, right? That
[02:25] is that is a legitimate advancement,
[02:27] right? Many advancements strung together
[02:29] , right? So, I don't want people to like
[02:31] clip this and be like, "Oh, you saying
[02:33] no."
[02:34] Um
[02:36] these AI systems are legitimate
[02:39] fundamental technological advancements,
[02:42] but um as applied to
[02:47] actual software production and creation
[02:55] as server.
[03:00] AI technology is a genuine advancement,
[03:02] but to those who use it, the software
[03:03] improvements are not visible. This isn't
[03:05] a statistic; it's the observation of one
[03:07] man, Blow. It's not that Blow doesn't
[03:09] use AI. Not long ago, he had to apply
[03:11] colors to an Excel sheet he was giving
[03:12] to someone else. It involved opening a
[03:14] CSV file generated by a program in Excel
[03:16] and applying colors and bold text to
[03:17] cells meeting certain conditions. AI
[03:19] produced about 30 lines of Visual Basic
[03:22] code almost instantly.
[03:30] Even though programmed in many languages
[03:32] , I've made a number of languages.
[03:35] It probably would have taken like 5
[03:36] hours to do or something. And, um,
[03:41] with the iterations that I did and all
[03:43] that, it probably took, uh,
[03:46] one hour or something.
[03:47] So again, we're already we're still not
[03:50] talking about like an infinite speedup
[03:52] like people talk about and, and this is
[03:54] a rare case because how often are you
[03:56] learning a new programming language or
[03:58] whatever, but this was a context in
[04:00] which was useful time
[04:04] anyway.
[04:09] >> Five hours turned into one hour, a
[04:10] fivefold increase.
[04:12] Blow believes this kind of experience is
[04:14] why people think AI is good at coding.
[04:16] However, there were three conditions
[04:18] attached. It was a language I’d never
[04:20] seen, it was 30 lines, and it was
[04:21] throwaway code. What is the difference
[04:23] between a 30-line snippet and a large
[04:25] program?
[04:25] Blow explains by marking points in the
[04:28] air. If there are three program pieces,
[04:29] the lines you can draw between them are
[04:31] three; if there are four, it's six. The
[04:32] lines grow faster than the pieces. These
[04:34] lines are not written in the code. If
[04:37] you build this here, how that affects
[04:38] things over there—those influences and
[04:40] constraints are the lines.
[04:51] and minimize them. Sure, but there's
[04:53] always a bunch and they grow as the
[04:55] program grows. And
[04:59] so you build out this map of those
[05:01] things in your mind
[05:04] and every time you're trying to do
[05:06] something new, you're like charting your
[05:08] way through there, right?
[05:10] And
[05:14] AI don't seem to, to me in 2026, they
[05:17] don't seem to actually reason well
[05:20] enough to do that.
[05:24] They kind of being it and going on
[05:30] vibes.
[05:31] >> Going on vibes. That is Blow’s
[05:33] expression. It doesn’t show in thirty
[05:35] lines, but it becomes apparent once the
[05:37] program exceeds a certain size.
[05:39] Then what is it that AI is actually
[05:41] doing? Blow says he thinks of modern AI
[05:43] as a search algorithm that understands
[05:45] natural language. It performs very large
[05:47] searches very quickly. But on the flip
[05:49] side, it is weak at judging how things
[05:51] will turn out later if you build them
[05:52] this way. The example he used as
[05:54] evidence isn't code. He said he had AI
[05:56] predict the initial sales volume of a
[05:58] new game several times before its
[05:59] release last month. The AI churned out
[06:01] numbers with a long list of reasons
[06:03] attached. Even taking into account that
[06:05] GTA is coming out this year.
[06:12] I feel like according to this one reason
[06:14] that you didn't mention the sales should
[06:17] be higher.
[06:19] And it says, "Oh, you know what? You're
[06:20] right.
[06:22] Actually, the sales should be higher.
[06:25] numbers because
[06:31] other
[06:37] If you say they should be higher, it
[06:38] agrees. If you say they should be lower
[06:40] , it also agrees. It looks like
[06:41] reasoning, but if you look closely, the
[06:43] holes and skipped steps are easily seen
[06:46] .
[06:47] Can’t the AI just pay off the technical
[06:49] debt that the AI created? When the host
[06:51] brought up an argument often heard these
[06:53] days, Blow replied like this.
[07:03] AI is very productive or whatever. It's
[07:05] like, no, for a given problem statement
[07:07] . Yeah.
[07:09] You have a human programmer do it who's
[07:11] good, and an AI do it, and the AI will
[07:13] give you a lot more code just like the
[07:16] the mathematical proofs would be a lot
[07:18] longer than if a real mathematician had
[07:20] written the proof.
[07:22] sometimes like you know 10 times longer
[07:24] times longer and then that extra code is
[07:27] all technical debt that you have to
[07:33] >> According to Bloh's calculations, as
[07:34] code increases, errors per line also
[07:36] increase, and once you cross a certain
[07:37] threshold, you can no longer manage it.
[07:39] He believes that pure" vibe coding "
[07:41] without reviewing the code hits that
[07:42] threshold quite quickly. Conversely,
[07:44] there are also many tasks that end well
[07:45] before reaching that line. Bloh admits
[07:47] that things like massage shop websites,
[07:49] which used to be a headache even when
[07:50] paying someone else, have become much
[07:52] easier now.
[07:53] However, he adds that this doesn't mean
[07:55] AI is good at programming.
[07:58] Here, the host puts forward a hypothesis
[08:00] . Is it possible that productivity has
[08:02] indeed risen, but the software industry
[08:03] is swallowing it up like a black hole?
[08:05] Bloh answers with a story from his
[08:07] college days.
[08:08] The Unix workstations he used around
[08:09] 1990 protected memory, displayed windows
[08:11] on the screen, and allowed mouse
[08:13] interaction.
[08:16] 1990
[08:18] now 2026 36 years later.
[08:21] You sit down of a computer. What is it?
[08:25] Redory.
[08:35] >> The tasks are the same, but the amount
[08:36] of code has increased incomparably. The
[08:38] example Bloh cites is systemd. In early
[08:41] Unix, the boot process required only
[08:43] five to ten lines of script.
[08:45] Systemd, which now occupies that role,
[08:47] contains about 1.71 million lines of
[08:49] code based on a Phoronix count of the
[08:51] repository at the end of 2022. There is
[08:53] also an image that Bloh asked to be
[08:54] displayed on the screen. It shows a
[08:55] Wikipedia map of Linux distributions.
[08:57] One splits and splits again. Bloh says
[09:00] that the work they do overlaps
[09:02] significantly. When layers pile up like
[09:03] this, accidents happen. On the 5th of
[09:05] this month, a bug was revealed in Alpine
[09:07] Linux where entering a very long
[09:09] password would bypass the login. This is
[09:11] the bug Bloh cited during the interview
[09:12] as the most absurd example. According to
[09:14] the security firm Ox's analysis, it was
[09:16] the result of three separate decisions
[09:17] made over a period of more than 10 years
[09:19] . Each one had its own reason for being
[09:21] . In Bloh's words, we are living on top
[09:23] of a massive landfill. The layers keep
[09:25] piling up, and it is difficult to dig
[09:27] down to the bottom. Bloh's outlook is
[09:29] that while AI might improve software
[09:31] quality, the possibility of it going the
[09:33] other way is much greater.
[09:35] So, does Bloh think AI coding is
[09:37] completely hopeless? That is not the
[09:39] case. Regarding the argument that
[09:41] mimicking reasoning well enough will
[09:42] eventually lead to true reasoning, he
[09:44] puts the probability at less than 50
[09:45] percent. But it’s not zero. He says that
[09:47] if you could create a coding AI that
[09:49] does exactly what you say, it would
[09:50] probably become the most valuable
[09:51] company in the world, and he shares how
[09:53] he would build it.
[09:59] Go back like 10 or more years in AI
[10:02] history, uh, to, um, Alpha Zero, which
[10:05] was a thing that, you know, Deep Mind
[10:08] did to play Go in some other games
[10:10] without being taught the rules.
[10:14] And that was just a different kind of a
[10:17] system because it was being trained on,
[10:20] um,
[10:23] what's almost exclusively trained on its
[10:25] own experience. Yeah. Well, and also
[10:26] just on rules and the operation of rules
[10:29] , which is what a program is. And so
[10:31] maybe
[10:34] in the end it doesn't make that much of
[10:36] a difference, but my suspicion is it
[10:38] does.
[10:46] LM
[10:51] The structure is to have the code
[10:52] learned through rules, while leaving
[10:54] conversations with people to the LM. As
[10:56] for how to connect the two, he simply
[10:57] said," somehow. "It's just a concept,
[10:59] not something already built.
[11:02] For reference, Alpha Zero is a system
[11:03] that learned by playing on its own
[11:04] without human input, after being given
[11:06] the rules. There is something he sees as
[11:07] useful right now. It's using AI to scan
[11:09] for bugs. He said it is clearly useful
[11:11] as a tool to keep alongside the program
[11:13] , like a linter or a fuzzer. Let's
[11:15] return to the initial numbers. If we
[11:17] follow his logic as to why thirty years
[11:19] 'worth isn't visible, it's like this.
[11:21] AI produces more code with the same
[11:23] problems, that code remains as debt, and
[11:25] software has always just piled up.
[11:28] Then what does he himself do? Sometimes
[11:30] , he stops. He's talking about when he
[11:32] fixes his own compiler.
[11:47] >> There are three things to take away. For
[11:49] thirty-line throwaway code, use AI as
[11:51] much as you want. If it's a long-lived
[11:53] system, humans must provide the map that
[11:55] draws the lines between the pieces. And
[11:57] as much as the code grows, you must set
[11:58] aside time to stop and pay off that debt
[12:00] .
[12:02] Producing code quickly and improving
[12:03] software are two different things. The
[12:05] conversation about the gap between
[12:07] thirty years and zero years ultimately
[12:08] came down to this.
