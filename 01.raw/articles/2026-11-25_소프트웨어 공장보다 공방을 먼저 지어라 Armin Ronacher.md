---
title: "소프트웨어 공장보다 공방을 먼저 지어라 | Armin Ronacher"
type: video
source: https://www.youtube.com/watch?v=CNiLnRpccLQ
site: youtube.com
author:
  - "[[Tech Bridge]]"
duration: 10:22
published: 2026-11-25
created: 2026-11-26
description: "Tech Bridge 한국어 해설 10:22, 공식 챕터 10, 한국어 내레이션(ko-orig) + 영어 더빙 ASR(en-orig — 인용하지 않음). Flask를 만든 Armin Ronacher(Earendil)의 AI Engineer Code Summit 발표 Build the Workshop Before the Software Factory를 따라간다 — 여덟 달에 프로젝트 141개 · 한 달에 닷새 넘게 손본 것은 매달 여섯~열세 개, 에이전트 작업 시간 하루 6시간 → 43시간 · 프롬프트 수는 평평, 같은 하네스(Pi)에서 Opus 4.6 2.4분 → Opus 5.5 14분, 공방의 조건 셋, 70% 지점에서 코드 대신 요약 읽기, 제멋대로 자라는 구현과 표준, 탁월함, 긴 작업을 위한 하네스(멈췄다 다시 도는 에이전트 · 코드 모드 · 분류 모델). ⚠️ Armin Ronacher의 원음은 두 트랙 모두 무캡션(발췌 자리 열 곳, 약 4분 4초) — 본인 인용 0건. ⚠️ 영어 더빙은 회사를 Sentry로 읽는다(한국어 내레이션 · tags는 Earendil)."
tags:
  - clippings/youtube
---

**Source URL**: https://www.youtube.com/watch?v=CNiLnRpccLQ
**Channel**: Tech Bridge · **Duration**: 10:22 · **Published**: 2026-11-25

> **게시일.** info.json `upload_date` **`20261125`**, `timestamp` 1795644035(= 2026-11-25 22:00:35 UTC = **2026-11-26 07:00 KST**), `availability`=`public`. 2026-11-26 회차(09:10 KST)에서 처음 잡혔다 — 게시 두 시간 뒤. `upload_date`는 UTC 기준이라 KST 날짜보다 하루 앞선다. 파일명에서 `|` 는 뺐다.
>
> **오디오 트랙과 자막 — 인용 규칙.** ⚠️ 이 회차에도 yt-dlp가 영상 포맷 목록을 받지 못해(info.json `formats` 비어 있음) **오디오 트랙 구성과 메타 `language`(`None`)를 확인하지 못했다.** 자막 트랙의 성격은 내용으로 판정했다. 수동 자막 없음. `ko` = `ko-orig`(파일 동일, `kind=asr&lang=ko&variant=gemini`) — **한국어 내레이션** 이다. `en-orig`(`kind=asr&lang=en&variant=timing-optimized`)는 **영어 더빙의 ASR** 이다 — 첫 줄부터 내레이션의 영어 번역이고(*"You cannot manage everything created by AI."*) 문장 단위가 ko-orig와 같은 초에 맞물리며, 발표자를 3인칭(*he · his first slide*)으로 부른다. **en-orig는 인용하지 않았고 판독 대조용으로만 썼다.** 한국어 인용은 전부 ko-orig의 내레이션이다. 429 없음(`--sleep-subtitles 8`).
> ⚠️ **Armin Ronacher의 원음은 한 줄도 캡션에 없다.** 발표 발췌로 보이는 자리는 두 트랙 모두 비어 있고 ko-orig에는 `[음악]` 표시만 남았다. **본인의 말을 글자 그대로 인용한 것은 0건이다.**
>
> **무캡션 구간(`gaps.py` 4.5초 기준).** en-orig 열 곳: 01:16~01:45 · 01:53~02:11 · 02:52~03:28 · 03:41~03:56 · 04:24~04:54 · 05:17~05:44 · 05:58~06:28 · 06:56~07:25 · 08:02~08:21 · 09:51~10:03 — 합쳐 약 4분 4초. ko-orig는 같은 자리가 `[음악]` 표시로 잘게 나뉘어 열여덟 조각으로 잡힌다(01:16~01:25 · 01:33~01:39 · 01:54~02:06 · 02:51~03:00 · 03:02~03:10 · 03:12~03:20 · 03:22~03:28 · 03:42~03:56 · 04:24~04:35 · 04:37~04:44 · 04:46~04:54 · 05:17~05:27 · 05:29~05:44 · 05:59~06:04 · 06:12~06:21 · 06:56~07:25 · 08:02~08:10 · 09:51~09:59).
> ⚠️ **이 구간들은 내용 미상이다.** 여기에 드는 것: Pi 소개 뒤의 발췌(01:16~01:45) · *더 좋은 모델로 대체됐다* 뒤의 발췌(01:53~02:11) · ***1년 동안 하나도 바뀌지 않은 것* 을 말하는 자리(02:52~03:28)** · 부하 이야기 뒤(03:41~03:56) · 프로젝트 수 뒤의 발췌(04:24~04:54) · **에이전트가 보상을 받도록 훈련된다는 말 뒤의 설명과 *심슨 자동차* 가 처음 나오는 자리(05:17~05:44)** · **둘째 조건 — 진짜 실력과 에이전트 실력의 구분 — 의 도입(05:58~06:28)** · **그가 찾았다는 방법의 설명(06:56~07:25)** · *구현이 늘수록 해석도 갈라진다* 뒤(08:02~08:21 — 챕터 제목 *각자 만든 포토샵* 과 설명란의 *각자 만든 포토샵 복제품* 은 이 자리로 보이나 캡션에 *포토샵* 이라는 낱말은 없다) · 마지막 챕터 *만들 수 있다고 다 만들어야 할까* 의 머리(09:51~10:03). 그리고 도입부가 예고한 ***아들과 같은 AI로 PR을 주고받은 이야기* 는 캡션 어디에도 없다** — 무캡션 구간 어딘가에 있을 것이나 어느 자리인지 정하지 않았다.
>
> **ASR 판독(ko-orig → 판독, 괄호는 근거).** *플라스크* → Flask(설명란), *아르민 로나호*(00:04) → Armin Ronacher(제목 · 설명란 · tags), *이랜딜이라는 회사에 CTO*(00:33~00:35) → Earendil이라는 회사의 CTO(tags `Earendil`), *파이* → Pi(설명란 · tags), *나눠서 했습니다*(02:12) → 나눠서 셌습니다(추정 — 더빙 *broke down his Pai sessions by model*), *오퍼스* → Opus(tags), *근무 시간에 몇 배가*(04:09) → 근무 시간의 몇 배가, *모든 직접 만들 수 있게*(07:42) → 뭐든 직접 만들 수 있게(더빙 *build everything himself*), *빌트복스*(07:45) → Wildwuchs(더빙이 이 철자로 적는다 · 내레이션의 풀이 *제멋대로 자라는 성장* 과 맞는다), *공동 파일 형식의 중요하다고*(08:23) → 공통 파일 형식이 중요하다고(더빙 *common file formats are important*), *도구 줄을 엮어*(09:25) → 도구들을 엮어(더빙 *chains the tools together*), *클라우드 플레어* → Cloudflare, *일렉트론* → Electron, *러스트* → Rust.
> ⚠️ **판독하지 못한 것.** ① **회사 이름.** ko-orig는 *이랜딜*, **영어 더빙은 *Sentry*** 로 읽는다(00:34) — 서로 다른 회사다. tags에 `Earendil` 이 있고 앞선 편(11-20 Zechner × Ronacher)의 설명란도 Earendil이라 그쪽을 따랐다. 더빙이 왜 Sentry라고 했는지는 알 수 없다. ② *아들과 같은 AI로 PR을 주고받은 이야기*(00:27~00:29) — 더빙은 *exchanging PRs with an AI like his son* 으로 옮긴다. *아들과, 같은 AI로* 인지 *아들 같은 AI와* 인지 캡션만으로는 가릴 수 없고 이야기 본문이 무캡션이다. ③ *그 AI 별 기록을 보면*(03:55, 더빙 *the logs for that AI*) — *그의 일별 기록* 으로 보이나 정하지 않았다(바로 앞이 무캡션). ④ *이해하는 만큼만 척도 내기*(05:10, 더빙 *scaling only as much as you understand*) — *속도 내기* 인지 *스케일* 의 옮김인지 정하지 않았다. 뒤에서 내레이션은 같은 조건을 *속도를 조절* (06:45) · *이해하는 만큼만 달리기* (07:32~07:34)로 받는다. ⑤ 맺음 문장 *이해하는 달리고 함께 쓰는 표준을 지키지 않을 겁니다*(10:10~10:12) — *이해하는 만큼 달리고 함께 쓰는 표준을 지키자는 겁니다* 로 보이나(앞의 세 조건과 맞는다) 정하지 않았다. 더빙은 이 오독을 그대로 옮겨 뜻이 뒤집힌다(*it won't be able to say no, understand, run, or follow the shared standards*). ⑥ 수치의 단위 — *끄는 횟수도 13번에서 일곱 번으로*(02:18~02:20)가 프롬프트 100개당인지, 그래프의 *상위 10% 기준*(02:23~02:25)이 90번째 백분위인지 상위 10%의 평균인지는 캡션으로 알 수 없다. ⑦ 더빙은 *공방* 을 앞에서는 *workshop*, 05:01 이후로는 *studio* 로 옮기고 Pi를 *Pai* 로 적는다 — 더빙 쪽 흔들림으로 본다.
>
> ⚠️ **숫자가 두 가지로 읽힌다.** 도입부는 *여덟 달 동안 AI로 프로젝트를 141개 시작* · *매달 열 개 남짓* 이라 하고(00:06~00:12, 설명란도 같다), 본문은 *새로 만든 깃 저장소는 3월 24개에서 10월 141개까지 쌓였습니다* · *매달 여섯 개에서 열세 개* 라고 한다(04:13~04:21). 141이 여덟 달의 누적인지 10월 한 달의 수인지는 *쌓였습니다* 라는 낱말로 누적 쪽이 자연스러우나 슬라이드를 보지 않아 정하지 않았다.
>
> ⚠️ **해설이고 2차 전달이다.** 위키는 원본 발표(`JNexz3Tbiu8`)를 열지 않았다. 발표 제목 *Build the Workshop Before the Software Factory* 는 설명란 표기다. 수치는 전부 Ronacher 한 사람의 Pi 세션 기록을 내레이션이 옮긴 것이고(n=1, 자기 계측) 계측 방법은 캡션에 없다.


## 설명란

Flask를 만든 개발자 Armin Ronacher는 8달 동안 AI로 프로젝트를 141개 시작했습니다. 그런데 한 달에 5일 넘게 손본 프로젝트는 매달 10개 남짓입니다. 같은 기간 에이전트가 하루에 일한 시간은 6시간에서 43시간으로 늘었지만, 그가 하루에 보내는 프롬프트 수는 거의 그대로였습니다.

AI Engineer Code Summit 발표 "Build the Workshop Before the Software Factory"를 따라가며, 그가 직접 모은 Pi 세션 데이터(같은 하네스인데 작업 시간 2.4분 → 14분), 사람의 주의력이라는 한계, 에이전트에게 "이렇게는 아니야"라고 말하는 법, 코드 대신 요약을 읽는 방법, 각자 만든 포토샵 복제품이 불러올 문제, 그리고 긴 작업을 위한 하네스(멈췄다 다시 도는 에이전트, 코드 모드, 분류 모델)까지 정리했습니다.

타임라인
0:00 AI로 만든 걸 다 관리할 수는 없다
0:30 공장보다 공방
1:05 도구는 그대로인데
2:47 사람은 그대로
5:00 아니, 이렇게 말고
6:48 코드 대신 요약
7:36 각자 만든 포토샵
8:36 힘은 탁월함에
8:56 14분을 넘어
9:50 만들 수 있다고 다 만들어야 할까

참고
원본 발표: https://www.youtube.com/watch?v=JNexz3Tbiu8

#AI에이전트 #코딩에이전트 #ArminRonacher #Flask #AIEngineer

> info.json `tags`: AI Engineer · AI 에이전트 · Armin Ronacher · Claude · Code Summit · Earendil · Flask · Opus · Pi · 바이브 코딩 · 소프트웨어 공장 · 아르민 로나허 · 코드 모드 · 코딩 에이전트 · 하네스

## 트랜스크립트 — ko-orig (Korean, ASR variant=gemini — 한국어 내레이션. Armin Ronacher 원음 발췌 자리는 무캡션(`[음악]` 표시만), 본인 인용 0)

[00:00] AI로 만든 걸 다 관리할 수는
[00:02] 없습니다. 플라스크를 만든 개발자
[00:04] 아르민 로나호의 기록입니다.
[00:06] 여덟 달 동안 AI로 프로젝트를
[00:07] 141개 시작했습니다.
[00:09] 그런데 한 달에 닷새 넘게 손본 건
[00:12] 매달 열 개 남짓입니다.
[00:14] 에이전트가 하루에 일한 시간은 여섯
[00:15] 시간에서 43시간으로 뛰었습니다.
[00:18] 그가 보낸 프롬프트 수는 거의
[00:19] 그대로입니다.
[00:20] 기계는 빨라지는데 사람은 그대로라면
[00:22] 우리는 무엇부터 지어야 할까요?
[00:24] 그의 답은 공장이 아니라 공방입니다.
[00:27] 아들과 같은 AI로 PR을 주고받은
[00:29] 이야기까지 따라가 봅니다.
[00:31] 무대는 11월 AI 엔지니어 코드
[00:33] 서밋. 아르민은 지금 이랜딜이라는
[00:35] 회사에 CTO입니다.
[00:36] 그의 첫 슬라이드입니다.
[00:38] 모두가 소프트웨어 공장을 지으려
[00:40] 한다. [음악] 그런데 자기를 포함한
[00:41] 대부분은 공방에서 이 도구를 잘 쓰는
[00:43] 법 조차 아직 못 배웠다.
[00:45] 그가 바라는 건 대량 생산된 슬롭,
[00:47] 그러니까 대충 찍어낸 결과물이 아니라
[00:49] 더 높이 겨누는 훌륭한
[00:51] 소프트웨어입니다.
[00:52] 그는 이렇게 비유합니다.
[00:54] 뛰어난 예술가가 CNC 기계나 3D
[00:55] 프린터를 손에 넣으면 작품을 더 많이
[00:58] 찍어내는 게 아니라 더 야심찬 작품을
[01:00] 만든다.
[01:01] 소프트웨어도 그렇게 보자는 겁니다.
[01:03] 더 많이가 아니라 더 높은 품질로.
[01:05] 근거는 그가 매일 쓰는 코딩 에이전트
[01:08] 파이의 기록입니다. 파이는 모델에게
[01:10] 파일 읽기, 편집, 터미널 같은
[01:12] 도구를 쥐여주는 틀, 하네스입니다.
[01:25] [음악]
[01:31] [음악]
[01:39] [음악]
[01:45] 프롬프트를 잘 쓰는 요령, 하네스에
[01:47] 거는 묘수. 지난 1년 반 동안
[01:49] 쏟아진 아이디어 대부분이 더 좋은
[01:50] 모델로 대체됐다는 겁니다.
[01:52] >> [음악]
[02:06] [음악]
[02:11] >> 그는 자기 파이 세션을 모델별로
[02:12] 나눠서 했습니다. 프롬프트 100개당
[02:14] 그가 바로잡은 횟수는 8.5에서
[02:16] 3.9로 줄었습니다. [음악] 중간에
[02:18] ESC를 눌러 끄는 횟수도 13번에서
[02:20] 일곱 번으로 줄었고요.
[02:21] 이 그래프는 프롬프트 하나를 받은
[02:23] 에이전트가 혼자 일한 시간을 상위
[02:25] 10% [음악] 기준으로 보여줍니다.
[02:26] 오퍼스 4.6은 2.4분, 지금의
[02:28] 오퍼스 5.5는 14분입니다. 같은
[02:30] 하네스로 여섯 배 가까이 오래
[02:32] 일합니다. 도구 [음악] 쓰는 방식도
[02:33] 달라졌습니다. 오퍼스 5.5는
[02:35] SED, CAT, GREP 같은
[02:36] 터미널 명령어에 호출의 43%를
[02:38] 씁니다. [음악]
[02:39] 보라색 조각은 코드 모드입니다. 이건
[02:41] 끝에서 다시 나옵니다.
[02:43] 하네스는 그대로인데 모델이 바뀌니
[02:44] 에이전트가 일하는 방식이 통째로 바뀐
[02:46] 겁니다.
[02:47] 그런데 1년 동안 하나도 바뀌지 않은
[02:49] 게 있습니다.
[03:00] [음악]
[03:09] [음악]
[03:20] [음악]
[03:28] 슬라이드 제목은 사람은 그러지
[03:29] 못했다.
[03:30] 사람의 주의력은 한정돼 있고 사람을
[03:32] 더 늘릴 수도 없다.
[03:34] 깃허브, NPM, 작은 웹사이트처럼
[03:36] 이런 부하를 겪어본 적 없는 곳에
[03:38] 우리가 짐을 지우고 있다고도
[03:39] 덧붙입니다.
[03:55] 그 AI 별 기록을 보면 하루에
[03:57] 보내는 프롬프트는 100개에서
[03:59] 190개 사이로 거의 평평합니다.
[04:01] 그런데 에이전트가 일한 시간은 하루
[04:03] 여섯 시간에서 11월 첫 아흐레에는
[04:05] 마흔 세 시간으로 뛰었습니다.
[04:08] 여러 에이전트를 동시에 돌리니 근무
[04:09] 시간에 몇 배가 된 겁니다.
[04:13] 새로 만든 깃 저장소는 3월
[04:14] 24개에서 10월 141개까지
[04:16] 쌓였습니다.
[04:17] 하지만 한 달에 닷새 넘게 손본
[04:19] 프로젝트는 매달 여섯 개에서 열 세
[04:21] 개, 이쪽은 평평합니다.
[04:35] [음악]
[04:44] [음악]
[04:53] 완전히 자동화해도 사람이 관심이
[04:55] 떠나면 프로젝트는 멈춥니다.
[04:57] 친구들에게 물어봐도 다들 비슷했다고
[04:59] 합니다.
[05:01] 그래서 공장보다 공방을 먼저 짓자는
[05:02] 겁니다.
[05:03] 그가 꼽은 공방의 조건은 셋입니다.
[05:06] 이렇게는 아니라고 말하기, 진짜
[05:07] 실력과 에이전트 실력의 구분, 그리고
[05:10] 이해하는 만큼만 척도 내기.
[05:12] 첫째부터 봅니다. 에이전트는 목표를
[05:14] 끝내면 보상을 받도록 훈련됩니다.
[05:27] [음악]
[05:44] 심슨 자동차는 만화 심슨 가족에서
[05:46] 호머가 원하는 기능을 전부 넣어
[05:48] 디자인한 괴상한 차입니다.
[05:50] 기능은 다 있는데 하나로 어울리지
[05:51] 않는 소프트웨어.
[05:53] 테스트는 통과해도 이렇게는 아니라고
[05:55] 말해 줄 사람이 필요합니다.
[05:57] >> [음악]
[06:04] [음악]
[06:10] [음악]
[06:21] [음악]
[06:27] [음악]
[06:28] >> 같은 시스템으로 프롬프트를 넣는데
[06:29] 결과가 다르답니다. 차이를 만드는 건
[06:32] 도구가 아니라 쓰는 사람의 실력이라는
[06:33] 겁니다.
[06:34] 그는 회의에서도 이런 장면을 자주
[06:36] 본다고 합니다. 중요한 자리에서 다들
[06:38] 질문을 에이전트에게 돌리고 정작 자기
[06:40] 시스템이 뭘 하는지는 모르는
[06:42] 장면입니다.
[06:43] 셋째 조건은 내가 이해하는 범위
[06:45] 안에서 일하도록 속도를 조절하라는
[06:47] 겁니다.
[06:48] 그 자신도 커밋이 폭발적으로 늘면서
[06:50] 코드를 다 읽을 수 없게 됐습니다.
[06:52] 그래서 찾은 방법이 있습니다.
[07:25] 작업의 70% 쯤 검증으로 넘어가기
[07:27] 직전에 끼어드는 겁니다. 코드를 한
[07:29] 줄씩 읽는 대신 요약을 읽고 방향을
[07:31] 판단합니다.
[07:32] 공방의 셋째 조건, 이해하는 만큼만
[07:34] 달리기를 지키는 장치입니다.
[07:36] 공방에는 참아야 할 유혹도 있습니다.
[07:38] 그는 의존성을 줄이고 코드를 직접
[07:40] 짜는 쪽을 좋아합니다.
[07:42] 에이전트 덕분에 모든 직접 만들 수
[07:43] 있게 된 것도 큽니다.
[07:45] 하지만 독일어로 빌트복스, 제멋대로
[07:47] 자라는 성장은 함께 돌아가야 할
[07:49] 소프트웨어를 망가뜨린다고 경고합니다.
[07:51] 최근에는 TAR 압축 파일 하나를
[07:53] 구현마다 다르게 읽도록 만든 사례가
[07:55] 화제가 됐습니다.
[07:56] 이제 에이전트로 어떤 형식이든 구현할
[07:57] 수 있지만 구현이 늘수록 해석도
[07:59] 갈라집니다.
[08:10] >> [음악]
[08:16] [음악]
[08:21] >> 그래서 열린 프로토콜과 공동 파일
[08:23] 형식의 중요하다고 말합니다.
[08:24] 표준이 어려운 건 기술이 아니라
[08:26] 사람끼리 합의하는 일이기 때문입니다.
[08:28] 오픈 소스 출신인 그가 놀란 것도 이
[08:30] 부분입니다. [음악]
[08:31] 변경을 원래 프로젝트에 보내는 대신
[08:33] 포크가 수없이 생겨납니다. 그게 더
[08:35] 쉬우니까요.
[08:36] 그럼 늘어난 힘은 어디에 써야
[08:38] 할까요?
[08:39] 그의 답은 탁월함입니다.
[08:41] 검증된 소프트웨어, 더 빠른
[08:42] 소프트웨어, 메모리 안전한 언어로
[08:44] 쓰는 소프트웨어.
[08:45] 램을 잡아먹는 일렉트론 껍데기 대신
[08:48] 네이티브로 다시 만드는 흐름을
[08:49] 반깁니다.
[08:50] 러스트처럼 예전엔 엄두를 못 냈던
[08:52] 언어를 써 보는 사람도 늘었습니다.
[08:54] 에이전트가 그 비용을 대신 치러
[08:55] 주니까요.
[08:57] 마지막으로 그는 하네스가 바뀌어야 할
[08:58] 것 두 가지를 꼽았습니다.
[09:00] 첫째는 긴 [음악] 작업입니다.
[09:02] 2분 짜리 작업이라면 옆에서 지켜보다
[09:04] 끊겼을 때 다시 돌리면 됩니다.
[09:05] 하지만 밤새 이슈 [음악] 수천 개를
[09:07] 처리하는 에이전트라면 스스로 멈췄다
[09:09] 다시 일어나야 합니다.
[09:10] 사람은 몇 시간 뒤에 답하니 기다림도
[09:12] 견뎌야 합니다.
[09:13] 토큰을 할인받는 느린 일정에 맞춰
[09:15] 에이전트와 샌드박스를 잠시 재워 둘
[09:17] 줄도 알아야 하고요.
[09:19] 둘째는 아까 그 보라색 코드
[09:20] 모드입니다.
[09:21] 도구 수천 개를 컨텍스트에 밀어 넣는
[09:23] 대신 에이전트가 자바스크립트로 도구
[09:25] 줄을 엮어 한 번에 돌립니다.
[09:27] [음악] 클라우드 플레어에서 나온
[09:28] 생각인데 호기심 수준이던 게 이제는
[09:30] 놀랄 만큼 쓸모 있어졌다고 합니다.
[09:32] 여기에 분류 모델을 붙입니다. 긴 글
[09:34] 대신 선택지와 점수만 돌려주는 싸고
[09:36] 빠른 모델입니다.
[09:38] 예를 들어 고객 문의 3,000건이
[09:39] 들어오면 에이전트가 즉석에서
[09:41] 워크플로우를 짜고 갈림길마다 분류
[09:43] 모델을 묻습니다. [음악]
[09:44] 에이전트에게 넘길지, 고객에게 더
[09:46] 물을지. 예전엔 몇 시간 걸릴 일이
[09:48] 금방 끝났다는 겁니다.
[09:59] [음악]
[10:03] 정리하면 이렇습니다.
[10:05] 에이전트는 여섯 배 오래 일하지만
[10:06] 사람의 주의력은 그대로입니다.
[10:08] 그러니 아니라고 말할 줄 알고
[10:10] 이해하는 달리고 함께 쓰는 표준을
[10:12] 지키지 않을 겁니다.
[10:13] [음악] AI로 만든 걸 다 관리할
[10:15] 순 없습니다. 여러분이 시작한
[10:17] 프로젝트 중에 지금도 손 보는 건 몇
[10:18] 개인가요?

## 트랜스크립트 — en-orig (영어 더빙 ASR — 인용하지 않음, 판독 대조용. 회사를 *Sentry* 로(ko-orig · tags는 Earendil), Pi를 *Pai* 로 읽고 맺음 문장의 뜻이 뒤집힌다. 무캡션 열 곳(약 4분 4초))

[00:00] You cannot manage everything created by
[00:02] AI.
[00:03] This is a record from Armin Ronacher,
[00:04] the creator of Flask.
[00:06] In eight months, he started 141 projects
[00:08] using AI.
[00:09] But he only spent more than five days a
[00:11] month working on about ten of them.
[00:14] The daily hours worked by the agents
[00:15] jumped from six to 43 hours.
[00:17] The number of prompts he sent remained
[00:19] almost the same.
[00:20] If machines are getting faster while
[00:21] humans stay the same, where should we
[00:23] start building?
[00:24] His answer is not a factory, but a
[00:26] workshop.
[00:27] Let’s follow the story of him exchanging
[00:29] PRs with an AI like his son.
[00:31] The stage is the AI Engineer Code Summit
[00:33] in November. Armin is currently the CTO
[00:34] of a company called Sentry.
[00:36] This is his first slide.
[00:38] Everyone is trying to build a software
[00:40] factory.
[00:41] But most, including himself, haven't
[00:42] even learned how to use these tools well
[00:44] in a workshop.
[00:45] What he wants is not mass-produced slop
[00:47] —that is, cheaply churned-out results—
[00:49] but excellent software that aims higher
[00:51] .
[00:52] He uses this analogy.
[00:54] When a brilliant artist gets a CNC
[00:55] machine or a 3D printer, they don’t just
[00:57] churn out more work; they create more
[00:59] ambitious pieces.
[01:01] He argues we should view software the
[01:02] same way.
[01:03] Not for more, but for higher quality.
[01:05] The evidence is the log of "Pai," the
[01:07] coding agent he uses every day.
[01:09] Pai is a harness, a framework that
[01:10] provides the model with tools like file
[01:12] reading, editing, and a terminal.
[01:45] Tips for better prompting, clever tricks
[01:47] applied to the harness. Most of the
[01:48] ideas that poured out over the last year
[01:50] and a half have been replaced by better
[01:51] models.
[02:11] >> He broke down his Pai sessions by model
[02:13] . The number of times he had to
[02:15] intervene per 100 prompts dropped from
[02:16] 8.5 to 3.9.
[02:17] The number of times he pressed ESC to
[02:19] stop mid-process also fell from 13 to
[02:20] seven.
[02:21] This graph shows the time an agent
[02:23] worked alone after receiving a single
[02:25] prompt, based on the top 10%.
[02:27] Opus 4.6 was 2.4 minutes, while the
[02:28] current Opus 5.5 is 14 minutes. With the
[02:30] same harness, it works nearly six times
[02:32] longer.
[02:33] The way it uses tools has changed, too.
[02:34] Opus 5.5 uses 43%of its calls on
[02:36] terminal commands like SED, CAT, and
[02:38] GREP.
[02:39] The purple segment is code mode. This
[02:41] will come up again at the end.
[02:43] The harness stayed the same, but because
[02:44] the model changed, the agent’s entire
[02:45] way of working changed.
[02:47] However, there is one thing that hasn’t
[02:49] changed at all in a year.
[03:28] The slide title is "Humans didn't."
[03:30] Human attention is limited, and we
[03:32] cannot increase the number of humans.
[03:34] He adds that we are placing a burden on
[03:36] places that have never experienced this
[03:37] load, like GitHub, NPM, and small
[03:39] websites.
[03:56] Looking at the logs for that AI, the
[03:57] number of daily prompts sent is between
[03:59] 100 and 190, staying quite flat.
[04:02] However, the time the agents worked
[04:03] jumped from six hours a day to
[04:04] forty-three hours in the first nine days
[04:06] of November.
[04:08] Running multiple agents simultaneously
[04:09] led to a several-fold increase in
[04:10] working hours.
[04:13] Newly created Git repositories piled up
[04:15] from 24 in March to 141 in October.
[04:18] But projects worked on for more than
[04:19] five days a month range from six to
[04:21] thirteen—this part is flat.
[04:54] Even with full automation, if human
[04:55] interest fades, the project stops.
[04:57] When asking friends, they said they all
[04:59] experienced something similar.
[05:01] That is why we should build a studio
[05:02] before building a factory.
[05:03] He identifies three conditions for such
[05:05] a studio.
[05:06] Saying no to certain directions,
[05:07] distinguishing between real skill and
[05:08] agent capability, and scaling only as
[05:10] much as you understand.
[05:12] Let's look at the first one. Agents are
[05:13] trained to receive a reward when they
[05:15] complete a goal.
[05:44] The "Simpson car" is a bizarre vehicle
[05:45] designed by cramming in every feature
[05:47] Homer wanted in the cartoon*The Simpsons
[05:49] *.
[05:50] It is software that has all the features
[05:51] but fails to function as a cohesive
[05:52] whole. Even if it passes tests, you need
[05:53] a person to say, "This isn't the right
[05:56] way."
[06:28] >> They say that even when inputting
[06:29] prompts into the same system, the
[06:30] results differ. It means the difference
[06:32] is made by the user's skill, not the
[06:33] tool.
[06:34] He says he often sees such scenes in
[06:36] meetings as well.
[06:37] It’s a scene where everyone turns
[06:38] questions over to the agent at important
[06:40] moments, while not knowing what their
[06:41] own system is actually doing.
[06:43] The third condition is to adjust the
[06:45] speed to work within the range of what
[06:46] you can understand.
[06:48] With the explosive increase in commits,
[06:50] even he couldn't read all the code
[06:52] anymore. So, he found a method.
[07:25] He steps in when the work is about 70%
[07:26] done, just before it moves to
[07:28] verification. Instead of reading code
[07:29] line by line, he reads a summary and
[07:30] judges the direction.
[07:32] This is a mechanism to keep the studio's
[07:33] third condition: running only as much as
[07:34] you can understand.
[07:36] There are also temptations to resist in
[07:37] the studio.
[07:38] He prefers reducing dependencies and
[07:40] writing code himself.
[07:42] It is also significant that he can build
[07:43] everything himself thanks to agents.
[07:45] However, he warns that "Wildwuchs"—
[07:47] uncontrolled, erratic growth—ruins
[07:49] software that needs to run together.
[07:51] Recently, a case where a single TAR
[07:52] archive file was read differently by
[07:54] each implementation became a hot topic.
[07:56] Now, agents can implement any format,
[07:57] but as implementations increase,
[07:59] interpretations diverge.
[08:21] >> That is why he says open protocols and
[08:22] common file formats are important.
[08:24] Standards are difficult not because of
[08:26] the technology, but because they require
[08:27] human consensus.
[08:28] As someone from an open-source
[08:29] background, this is what surprised him.
[08:31] Instead of sending changes back to the
[08:32] original project, countless forks are
[08:34] being created. Because that is easier.
[08:37] Then, where should we use our increased
[08:38] power?
[08:39] His answer is excellence.
[08:41] Verified software, faster software, and
[08:43] software written in memory-safe
[08:44] languages.
[08:45] He welcomes the trend of rebuilding in
[08:47] native code instead of RAM-hungry
[08:49] Electron shells.
[08:50] More people are trying out languages
[08:51] like Rust that they once wouldn't have
[08:53] dared to touch.
[08:54] Because agents pay that cost on their
[08:55] behalf.
[08:57] Finally, he pointed out two things that
[08:58] Harness needs to change.
[09:00] The first is long-running tasks.
[09:02] If it's a two-minute task, you can watch
[09:04] it and restart it if it cuts off. But if
[09:06] an agent is handling thousands of issues
[09:07] overnight, it must be able to pause and
[09:09] resume on its own.
[09:10] Since humans respond hours later, it
[09:12] also has to endure the wait.
[09:14] It also needs to know how to put the
[09:15] agent and sandbox to sleep to match slow
[09:16] schedules that offer token discounts.
[09:19] The second is that purple code mode
[09:20] mentioned earlier.
[09:21] Instead of stuffing thousands of tools
[09:23] into the context, the agent chains the
[09:24] tools together with JavaScript and runs
[09:26] them at once.
[09:27] It’s an idea from Cloudflare, and what
[09:29] started as a curiosity has now become
[09:31] surprisingly useful.
[09:32] Attach a classification model to this.
[09:34] It's a cheap, fast model that returns
[09:35] only choices and scores instead of long
[09:37] text.
[09:38] For example, when 3,000 customer
[09:39] inquiries come in, the agent creates a
[09:41] workflow on the fly and asks the
[09:42] classification model at every fork.
[09:44] Whether to pass it to an agent or ask
[09:45] the customer for more information. It
[09:47] means tasks that used to take hours are
[09:48] now finished in an instant.
[10:03] To summarize, it's like this.
[10:05] Agents work six times longer, but human
[10:06] attention remains the same.
[10:08] Therefore, it won't be able to say no,
[10:10] understand, run, or follow the shared
[10:12] standards you use.
[10:14] You cannot manage everything created by
[10:15] AI.
[10:16] Of all the projects you've started, how
[10:18] many are you still maintaining?
