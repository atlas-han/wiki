---
title: "Claude Code 만들던 개발자가 “받아들일 수 없다”고 한 것 | Thariq Shihipar"
type: video
source: https://www.youtube.com/watch?v=SBKLfp5NE4M
site: youtube.com
author:
  - "[[Tech Bridge]]"
duration: 11:22
published: 2026-11-22
created: 2026-11-23
description: "Tech Bridge 한국어 해설 11:22, 공식 챕터 10, Korean original + 영어 더빙(en-orig는 전부 더빙 ASR — 인용하지 않음). Anthropic에서 1년 넘게 Claude Code를 만들다 10월 말 떠난 Thariq Shihipar의 AI Engineer Code Summit 마지막 발표를 따라간 해설 — 틀렸다고 인정한 예언 셋(Bash면 충분하다 · React면 충분하다 · 확산 모델이 미술을 집어삼킨다), Sutton의 쓴 교훈과 쇼고스, 공장이면서 공방, 들쭉날쭉한 경계와 매끈한 안쪽, 눈 가린 Claude 12개의 세계지도, 바이브 코딩의 덫, 사람이 읽는 폴더(engine / human 분리, rock.ts 데모), 르네상스의 재료. ⚠️ 발표 원음은 두 트랙 모두 무캡션(열세 곳, 약 3분 33초) — Thariq 본인 인용 0."
tags:
  - clippings/youtube
---

**Source URL**: https://www.youtube.com/watch?v=SBKLfp5NE4M
**Channel**: Tech Bridge · **Duration**: 11:22 · **Published**: 2026-11-22

> **게시일.** info.json `upload_date` **`20261122`**, `timestamp` 1795341627(= 2026-11-22 10:00:27 UTC = **2026-11-22 19:00 KST**), `availability`=`public`. 2026-11-23 회차(09:10 KST)에서 처음 잡혔다. 파일명에서 `|` 와 따옴표는 뺐다.
>
> **오디오 트랙과 자막 — 인용 규칙.** 오디오는 **Korean original(default) + 영어 더빙**(audio language `ko` · `en` · `en-US`), 메타 `language`=`en`. 수동 자막 없음. `ko` = `ko-orig`(파일 동일, `kind=asr&lang=ko&variant=gemini`). `en-orig`(`kind=asr&lang=en&variant=timing-optimized`)는 **처음부터 끝까지 영어 더빙의 ASR** 이다 — 첫 줄부터 내레이션의 영어 번역이고(*"He says he doesn't know what the characters are doing in a game he built himself."*) 발표자 이름을 *Tareq Shabar* · *Tariq* 로, *Celeste* 를 *Celestia* 로 적는다. **인용하지 않았고 판독 대조용으로만 썼다.** 한국어 인용은 전부 ko-orig의 내레이션이다.
> ⚠️ **발표 원음(영어)은 두 트랙 어디에도 잡히지 않았다.** 발표 발췌가 들어간 자리는 두 트랙 모두 무캡션이다(11-20 Zechner 편 · 11-21 Pocock 편과 같은 배치). **Thariq Shihipar 본인의 말을 글자 그대로 인용한 것은 0건이다.** 429 없음(`--sleep-subtitles 8`).
>
> **무캡션 구간(`gaps.py` 4.5초 기준).** ko-orig 열세 곳: 00:11~00:18 · 00:57~01:10 · 01:22~01:33 · 01:35~01:44 · 02:54~03:23 · 03:54~04:08 · 04:10~04:19 · 05:22~05:36 · 07:03~07:24 · 07:43~08:04 · 08:33~08:47 · 09:27~10:01 · 10:40~10:56 — 합쳐 약 3분 33초, 전부 발표 발췌 자리로 보인다(01:33 · 04:08 · 05:20 · 10:37에 `[음악]` 표시만 있다). en-orig 열한 곳: 00:11~00:18 · 00:57~01:10 · 01:22~01:44 · 02:54~03:23 · 03:55~04:19 · 05:17~05:36 · 07:03~07:24 · 07:43~08:04 · 08:33~08:47 · 09:27~10:01 · 10:34~10:56 — 같은 자리다.
> ⚠️ **이 구간들은 내용 미상이다.** 여기에 드는 것: 도입의 고백 원음(00:11~00:18) · 맞힌 것 다음의 말(00:57~01:10) · *Bash면 충분하다* 가 왜 틀렸는지에 대한 원음(01:22~01:44) · **세 오답이 나온 *하나의 두려움* 이 무엇인지와 쇼고스 대목(02:54~03:23)** · 산업 혁명과 르네상스 원음(03:54~04:19) · *매끈한 안쪽* 원음(05:22~05:36) · 게임을 바이브 코딩할 때 생긴 *질문들* (07:03~07:24) · 07:43~08:04 · *사람이 읽는 폴더* 의 규칙 설명(08:33~08:47) · 데모 뒷부분(09:27~10:01) · 맺음말(10:40~10:56). 내레이션이 앞뒤로 받아 적은 한 줄씩만 남아 있다.
>
> **ASR 판독(ko-orig → 판독, 괄호는 근거).** *타리크 시바르*(00:04) · *타릭*(04:51) → Thariq Shihipar(제목 · 설명란), *엔트로픽*(00:05 · 00:34) → Anthropic(설명란 *앤트로픽*), *마침 것부터*(00:44) → 맞힌 것부터(더빙 *what he got right*), *배시 · 배쉬* → Bash, *비슷하겠습니다*(02:01) → 비슷하게 씁니다(추정 — 더빙 *similarly proficient*), *목업 판화를*(05:37) → 목업 하나를(추정 — 더빙 *a mockup*), *오비 까지나*(05:55) → 어디까지나(더빙 *of course, just his own outlook*), *셀레스티*(06:01) → Celeste(설명란), *안드레 카파시* → Andrej Karpathy, *AI 통째로 바뀌지 말라고*(06:54~06:56) → AI로 통째로 바꾸지 말라고(추정 — 더빙 *don't let AI replace it entirely*), *휴 원*(08:21~08:23) → 휴먼(human — 08:25는 *휴먼 폴더* 로 바로 적힌다), *록 점 티에스*(08:49) → rock.ts(더빙), *돌 모더기*(09:00~09:02) → 돌무더기, *코서의 탭*(09:18) → Cursor의 Tab(더빙 *Cursor's Tab autocomplete*), *줄 세워 돌라는*(09:21) → 줄 세워 두라는(추정 — 더빙 *queue the actions*), *뭐라는지*(10:56) → 뭘 하는지(추정 — 00:00의 *뭘 하는지* 와 짝).
> ⚠️ **판독하지 못한 것.** ① **세계지도의 첫 모델 이름.** ko-orig *손해 4.5는 60%*(06:17), 더빙 ASR *Sonnet 3.5 at 60%* — Sonnet인 것은 맞아 보이나 **버전 숫자가 두 트랙에서 다르다. 어느 쪽인지 정하지 않았다.** ② *최근에는 공장과 처음 보는 것을 만드는 공방*(04:19~04:21)의 첫머리 — 더빙도 *Recently, we have factories* 라 대조가 되지 않는다(*찍어내는* 따위로 들릴 수 있으나 추정하지 않았다). ③ *그 결과 오히려 진도가 더 나갔다고 털어놓았습니다*(07:31~07:33) — 앞 문장(*몰입이 안 됐습니다*)과 바로 뒤의 X 글(*실제로는 아무것도 진행되지 않는 상태*)을 보면 *덜 나갔다* 여야 뜻이 통하는데 더빙도 *he actually made more progress* 다. **글자 그대로 두고 표시만 했다.**
> ⚠️ 영어 더빙은 *무대는 11월 San Francisco* 를 *last November* 로 옮겼다 — 오역이다(발표는 2026년 11월).
>
> ⚠️ **해설이고 2차 전달이다.** 위키는 원본 발표(`xRJMiaUoD_8`)도, 설명란의 글 여섯(Sutton *The Bitter Lesson* 원문 · Dell'Acqua 외 논문 · Karpathy X · Celeste X · Thariq X 두 편)도 이번에 열지 않았다. 수치(650만 회 · 758명 · 40% · 19%포인트 · 16,200번 · 60% · 91% · 99% · 5년)는 내레이션이 슬라이드와 글에서 옮긴 값이다. 발표자가 한 말은 전부 한국어 내레이션의 간접 전달로만 남아 있다.


## 설명란

앤트로픽에서 1년 넘게 Claude Code를 만들다 떠난 Thariq Shihipar가 AI Engineer CODE Summit 마지막 무대에서 털어놓은 이야기입니다. 바이브 코딩으로 만든 자기 게임인데, 캐릭터가 정확히 뭘 하는지 모르겠다는 고백이었습니다. 그는 "이건 받아들일 수 없다"고 말합니다.

그가 틀렸다고 인정한 예언 셋(Bash면 충분하다, React면 충분하다, 확산 모델이 미술을 집어삼킨다)에서 출발해, 리처드 서튼의 쓴 교훈과 쇼고스, 들쭉날쭉한 경계와 매끈한 안쪽, 눈 가린 Claude 12개가 그린 세계지도를 거쳐, 그가 찾은 해법인 '사람이 읽는 폴더'를 실제 데모 코드로 따라갑니다.

타임라인
0:00 내 게임인데 캐릭터가 뭘 하는지 모른다
0:28 그가 틀린 세 가지
2:28 쓴 교훈과 쇼고스
3:34 공장이면서 공방
4:24 들쭉날쭉한 경계, 매끈한 안쪽
5:58 눈 가린 Claude 12개의 세계지도
6:44 바이브 코딩의 덫
8:16 사람이 읽는 폴더 (데모)
10:09 르네상스의 재료
10:56 처음 고백으로

참고
원본 발표: https://www.youtube.com/watch?v=xRJMiaUoD_8
Rich Sutton, The Bitter Lesson (2019.03.13): http://www.incompleteideas.net/IncIdeas/BitterLesson.html
Dell'Acqua 외, Navigating the Jagged Technological Frontier (HBS Working Paper 24-013, 2023): https://papers.ssrn.com/abstract=4573321
Andrej Karpathy X (2026.10.02): https://x.com/karpathy/status/2105909609487872075
Celeste X, How 12 blind Claudes see the Earth (2026.09.24): https://x.com/celestepoasts/status/2103232383139057950
Thariq X, 퇴사 글 (2026.10.24): https://x.com/trq212/status/2113844051938054167
Thariq X, 게임 공개 (2026.09.30): https://x.com/trq212/status/2105333496768319969

#ClaudeCode #바이브코딩 #Anthropic #AI에이전트 #코딩에이전트

> info.json `tags`: AI Engineer · AI 에이전트 · Anthropic · Bitter Lesson · Claude Code · Code Summit · Karpathy · Thariq Shihipar · vibe coding · 바이브 코딩 · 쓴 교훈 · 앤트로픽 · 코딩 에이전트 · 클로드 코드 · 타리크

## 트랜스크립트 — ko-orig (Korean original, ASR variant=gemini — 한국어 내레이션만 잡혔다. 발표 원음 자리 열세 곳(약 3분 33초)은 무캡션)

[00:00] 자기가 만든 게임인데 캐릭터가 뭘
[00:02] 하는지 모르겠다고 합니다. 말한
[00:04] 사람은 타리크 시바르.
[00:05] 얼마 전까지 엔트로픽에서 1년 넘게
[00:07] 클로드 코드를 만들던 개발자입니다.
[00:18] 그런데 그는 무대에서 이건 받아들일
[00:20] 수 없다고 했습니다. AI가 하자는
[00:22] 대로 일할까요? 내가 원하는 대로
[00:23] 시킬까요? 그가 찾은 답과 눈 가린
[00:26] 클로드 12개가 그린 세계 지도를
[00:27] 따라가 봅니다.
[00:29] 무대는 11월 San
[00:30] Francisco의 AI 엔지니어
[00:31] 코드 서밋. 그 마지막 순서였습니다.
[00:34] 그는 10월 말 엔트로픽을
[00:35] 떠났습니다. X에 올린 퇴사 글은
[00:37] 650만 번 넘게 읽혔습니다.
[00:40] 발표는 그 뒤 1년을 돌아보는
[00:41] 이야기였고 주제는 내가 틀렸던
[00:43] 것들이었습니다.
[00:44] 마침 것부터 꼽았습니다.
[00:46] 모델이 영상을 만들고 편집할 수
[00:48] 있다. HTML로 자기 작업을 보여줄
[00:50] 수 있다. 그리고 내가 모르는 것을
[00:52] 함께 찾아줄 수 있다. 여기까지는
[00:54] 맞았다고 했습니다.
[01:10] 첫 번째 오답은 배시면 충분하다.
[01:12] 클로드 코드는 배시 도구를 중심으로
[01:14] 만들어졌습니다. 그러니 모든 걸
[01:15] CLI로 바꾸면 된다는 말이
[01:17] 돌았습니다. [음악] MCP마저
[01:18] CLI로 감싸자는 이야기까지
[01:20] 나왔습니다.
[01:33] [음악]
[01:44] 지금 모델은 도구 호출과 스킬,
[01:46] 필요할 때만 꺼내 보는 점진적 공개,
[01:48] 코드 모드까지 고루고루 잘 씁니다.
[01:51] 두 번째는 리액트면 충분하다.
[01:53] 모델이 리액트를 워낙 잘 쓰니 모든
[01:55] 앱을 리액트로 만들게 될 거라는
[01:56] 생각이었습니다.
[01:58] 지금 모델은 HTML도,
[01:59] Swift도,
[02:01] 자체 제이슨 형식도 비슷하겠습니다.
[02:03] 리액트가 마지막 언어가 될 거라는
[02:05] 걱정은 빗나갔습니다.
[02:06] 오히려 자기 언어를 만드는 사람이
[02:08] 늘었다고 합니다.
[02:09] 세 번째는 확산 모델이 미술을
[02:11] 집어삼킨다는 걱정이었습니다. 사람이
[02:13] 손 댈 수 없는 그림만 쏟아질
[02:14] 거라고요.
[02:15] 실제로는 LLM이 코드로 그림을
[02:17] 그리고 블렌더나 포토샵, 피그마를
[02:20] 직접 조작합니다. 사람과 같은 도구로
[02:22] 그리는 겁니다.
[02:23] 배쉬, 리액트, 확산 모델. 세
[02:25] 오답은 사실 하나의 두려움에서
[02:27] 나왔습니다.
[02:29] 발표 제목에 쓴 교훈은 강화 학습의
[02:30] 대가 리처드 서튼이 2019년에 쓴
[02:32] 짧은 글입니다.
[02:34] 70년 AI 연구의 가장 큰 교훈은
[02:36] 계산을 쏟아붓는 일반적인 방법이 결국
[02:38] 큰 차이로 이긴다는 것.
[02:40] 사람이 생각하는 방식을 모델에
[02:41] 집어넣는 건 길게 보면 통하지
[02:42] 않는다는 겁니다. 사람에게는 쓴
[02:44] 교훈이죠.
[02:46] 그 옆에 붙은 그림이 쇼고스입니다.
[02:47] 웃는 얼굴 가면을 쓴 촉수 괴물로
[02:49] AI를 속을 알 수 없는 외계 지능에
[02:51] 빗댄 밈입니다.
[03:23] 그래서 그는 묻습니다. AGI를
[03:25] 믿으면서도 사람을 중심에 둘 수는
[03:27] 없을까?
[03:28] 개발자에게 이 질문이 먼저 닥친
[03:29] 이유도 됐습니다. [음악]
[03:30] 소프트웨어에서 일어난 일은 결국 다른
[03:32] 지식 노동으로 번진다는 겁니다.
[03:34] 그는 지금의 AI를 산업 혁명이면서
[03:37] 동시에 르네상스라고 봅니다.
[03:39] 올해는 산업 혁명 초기였습니다.
[03:41] 소프트웨어 공장이라는 말이 흔해졌고
[03:43] 소프트웨어 만들기는 더 이상 병목이
[03:45] 아니게 됐습니다.
[03:46] 산업화는 빠르고 믿을 수 있고 싸게
[03:49] 내 놓는 경쟁입니다.
[03:50] 르네상스는 아무도 본 적 없는 것을
[03:52] 내 놓는 일이고요.
[04:08] >> [음악]
[04:19] >> 최근에는 공장과 처음 보는 것을
[04:21] 만드는 공방. 지금은 둘이 동시에
[04:23] 돌아간다는 겁니다.
[04:24] AI 능력을 말할 때 흔히 쓰는 말이
[04:26] 들쭉날쭉한 경계입니다.
[04:28] 2023년 하버드 경영대학원 연구진이
[04:31] BCG와 함께 낸 논문에서
[04:32] 나왔습니다.
[04:34] 난이도가 비슷해 보여도 어떤 일은
[04:35] AI가 쉽게 하고 어떤 일은 아예 못
[04:37] 한다는 뜻입니다.
[04:39] 컨설턴트 758명을 실험했더니 경계
[04:41] 안의 과제에서는 품질이 40% 넘게
[04:44] 올랐습니다.
[04:45] 그런데 경계 밖의 과제에서는 AI를
[04:47] 쓴 쪽이 정답을 낼 확률이 19%
[04:49] 포인트 낮았습니다.
[04:51] 타릭도 이 경계부터 보여줬습니다.
[04:53] 함수 하나, 기능 하나, 할 일 앱,
[04:55] 슬랙 복제.
[04:56] 그리고 이제는 마리오 카트를 처음부터
[04:57] 만들어 달라는 수준입니다.
[04:59] 벤치마크에서 보는 건 늘 이
[05:01] 끝자락입니다.
[05:02] 그가 더 중요하게 본 건 경계
[05:04] 안쪽입니다.
[05:05] 그는 이걸 매끈한 안쪽이라고
[05:06] 불렀습니다.
[05:08] 리액트를 쓸 줄 알면 피그마 파일도,
[05:10] 제이슨도, 배시도 씁니다.
[05:12] 경계 아래는 들쭉날쭉하지 않고 고르게
[05:14] 넓어진다는 겁니다.
[05:20] [음악]
[05:35] 그래서 이제 원하는 방식대로 시킬 수
[05:37] 있습니다. 목업 판화를 HTML로,
[05:39] 리액트로, 피그마 파일로.
[05:41] 아니면 컴퓨터를 직접 조작해 애프터
[05:43] 이펙트로 영상을 만들게 할 수도
[05:44] 있습니다.
[05:45] 지금 모델을 씌우는 하네스와 비계도
[05:48] 대부분 머지않아 필요 없어질 거라고
[05:49] 그는 말합니다. 완벽한 모델이라면
[05:52] 보안 취약점을 따로 검사하지 않아도
[05:53] 처음부터 맞는 코드를 쓸 거라는
[05:55] 겁니다. 이건 오비 까지나 그의
[05:56] 전망입니다.
[05:58] 매끈한 안쪽을 보여주려고 그가 띄운
[06:00] 그림이 있습니다.
[06:01] 셀레스티라는 사용자가 올리고 안드레
[06:03] 카파시가 소개한 평가입니다.
[06:05] 모델에게 위도와 경도를 글자로만 주고
[06:07] 땅인지 물인지 묻습니다.
[06:09] 지구 전체를 16,200번 묻고 답을
[06:11] 점으로 찍습니다.
[06:12] 카파시는 이렇게 덧붙였습니다. 모델은
[06:14] 안다. 인터넷을 압축하면서.
[06:17] 왼쪽 위 손해 4.5는 60% 대륙이
[06:20] 제대로 보이지 않습니다.
[06:21] 오퍼스 4.6은 91%로 윤곽이
[06:24] 흐릿하게 잡히고 오퍼스 5.5는
[06:26] 99% 거의 실제 지도입니다.
[06:29] 이미지도 도구도 없이 글로만 배운
[06:31] 모델이 그린 지구입니다.
[06:32] 타리크가 이 지도에서 본 건 벤치마크
[06:34] 점수가 아니라 모델이 가진 일반
[06:36] 지식의 폭이었습니다.
[06:38] 그리고 이 문장을 띄웠습니다.
[06:39] [음악] 이제 지능을 써서 우리가
[06:41] 지능을 쓰는 방식을 이해하고 빚을 수
[06:43] 있다.
[06:45] 이제 처음에 게임으로 돌아갑니다.
[06:46] 그는 와이 콤비네이터 투자를 받은
[06:48] 게임 회사를 5년 동안 운영했던
[06:49] 사람입니다.
[06:50] 9월 말 게임을 처음 공개하며 이렇게
[06:52] 썼습니다. 게임 만드는 과정은
[06:54] 창의적인 일이니 AI 통째로 바뀌지
[06:56] 말라고.
[06:57] 2차원 아이소메트릭 격투 게임입니다.
[06:59] 상대를 원판 밖으로 밀어내면
[07:00] 이깁니다.
[07:24] 그 질문들에 모델이 알아서 답을
[07:26] 정해버립니다. 게다가 프롬프트를
[07:28] 보내놓고 딴 일을 하다 돌아오니
[07:29] 몰입이 안 됐습니다.
[07:31] 그 결과 오히려 진도가 더 나갔다고
[07:33] 털어놓았습니다.
[07:34] 발표 2주 전 엑스에도 비슷한 글을
[07:35] 남겼습니다.
[07:36] 코딩 에이전트에 빠지면 일을 많이
[07:38] 하는 것 같은데 실제로는 아무것도
[07:40] 진행되지 않는 상태가 온다고요.
[08:04] 좋은 작품이 결국 선택의 결과라고
[08:06] 봅니다. 무엇을 넣고 무엇을 뺐는지가
[08:08] 작품을 만든다는 겁니다.
[08:10] 그러려면 속속들이 아는 전문가여야
[08:11] 합니다.
[08:12] 그런데 바이브 코딩한 코드는
[08:13] 들여다봐도 무슨 일이 일어나는지
[08:15] 모르겠다는 겁니다.
[08:17] 그의 해법은 코드 베이스를 둘로
[08:19] 나누는 것이었습니다. 하나는 엔진,
[08:21] 다른 하나는 스펙 혹은 그냥 휴
[08:23] 원이라고 부르는 폴더입니다.
[08:25] 휴먼 폴더는 그가 직접 읽는
[08:26] 코드입니다. 린트를 걸고 클로드에게는
[08:29] 이 코드가 어떤 모양이어야 하는지
[08:30] 규칙을 줍니다.
[08:47] 데모에서 연 파일은 돌 던지기 기술
[08:49] 록 점 티에스입니다. 속도와 질량,
[08:51] 크기, 사거리가 적혀 있습니다.
[08:53] 엑스 0.5 같은 숫자 대신 [음악]
[08:55] 미터와 초 단위를 쓰고 줄마다 무슨
[08:57] 뜻인지 주석이 붙어 있습니다.
[08:59] 돌을 줍는 방법도 세 갈래로
[09:00] 나뉩니다. 바닥에서 뜯어내거나 돌
[09:02] 모더기에서 줍거나 자기가 세운 벽을
[09:05] 뚫고 던집니다.
[09:06] 엔진 속은 몰라도 이 캐릭터의 진짜
[09:08] 논리는 여기서 다 보입니다.
[09:10] 사실상 게임 전용 스크립트 언어를
[09:11] 만든 셈입니다.
[09:13] 돌을 더 크게 하고 싶으면 숫자
[09:14] 하나를 바꾸면 됩니다.
[09:15] 게임으로 돌아가 힘을 모아 던지니
[09:17] 커다란 바위가 날아갑니다.
[09:18] 요즘은 코서의 탭 자동 완성을 많이
[09:20] 쓴다고 합니다.
[09:21] 벽을 세우면 행동을 줄 세워 돌라는
[09:23] 주석을 쓰면 나머지는 탭이 채웁니다.
[10:01] 복잡한 기본 블록은 여전히 클로드가
[10:03] 만듭니다. 다만 그걸 어떻게 엮을지는
[10:05] 그가 읽고 고칩니다.
[10:07] 본인도 아직 초기 단계라고 했습니다.
[10:10] 그의 결론은 모델이 무엇을 잘 쓰는지
[10:12] 맞추지 말고 좋은 소프트웨어를 내놓는
[10:14] 최선의 방법을 고민하자는 것입니다.
[10:16] 그가 꼽은 르네상스 의 재료입니다.
[10:18] 빠르고 표현력 있고 고치는 즉시
[10:20] 반영되는 새 언어,
[10:22] 새로운 데이터베이스와 서버,
[10:23] 운영체제와의 새로운 상호작용, 다시
[10:26] 읽어볼 만해진 옛 HCI 연구,
[10:28] 새로운 미학,
[10:30] 그리고 쓰는 사람이 고쳐 쓸 수 있는
[10:32] 소프트웨어.
[10:37] [음악]
[10:56] 자기 게임의 캐릭터가 뭐라는지 몰랐던
[10:58] 개발자는 이제 돌 하나에 속도와
[11:00] 크기를 직접 읽고 고칩니다.
[11:02] 정리하면 모델은 한 가지 방식을
[11:04] 고집하지 않았고 할 줄 아는 범위는
[11:06] 고르게 넓어졌고 그래서 방식을 우리가
[11:08] 정할 수 있습니다.
[11:09] 물론 하네스가 필요 없어진다는 건
[11:11] 그의 전망이고 휴먼 폴더도 본인 말로
[11:13] 아직 초기 실험입니다.
[11:14] 여러분의 코드 베이스에는 여러분이
[11:16] 직접 읽는 폴더가 있나요? 아니면
[11:18] 전부 모델이 정한 대로 흘러가고
[11:19] 있나요?

## 트랜스크립트 — en-orig (처음부터 끝까지 영어 더빙 ASR — 인용하지 않음, 판독 대조용(발표 원음은 여기에도 없다))

[00:00] He says he doesn't know what the
[00:01] characters are doing in a game he built
[00:02] himself.
[00:03] The person who said this is Tareq Shabar
[00:05] .
[00:05] He is a developer who spent over a year
[00:07] at Anthropic building Claude Code until
[00:09] recently.
[00:18] But on stage, he declared that this is
[00:20] unacceptable. Should we work the way AI
[00:22] suggests? Or should we make it do what
[00:23] we want? Let’s follow the answer he
[00:25] found and the world maps drawn by twelve
[00:27] blindfolded Claudes.
[00:29] The stage was the AI Engineer Code
[00:30] Summit in San Francisco last November.
[00:32] He was the final speaker.
[00:34] He left Anthropic at the end of October
[00:36] . His resignation post on X was read
[00:38] over 6.5 million times.
[00:40] His talk reflected on the past year, and
[00:42] the theme was "things I got wrong."
[00:44] He started with what he got right.
[00:46] Models can create and edit videos. They
[00:48] can showcase their work in HTML.
[00:51] And they can help find things I don't
[00:53] know.
[00:53] He said he was right about these things
[00:55] .
[01:10] His first wrong answer was that Bash is
[01:11] enough.
[01:12] Claude Code was built centered around
[01:14] Bash tools. So, the word went around
[01:16] that we should just turn everything into
[01:17] a CLI. There was even talk of wrapping
[01:19] MCP in a CLI as well.
[01:44] Now, models use tool calling, skills,
[01:46] progressive disclosure, and code modes
[01:48] quite well across the board.
[01:51] The second was that React is enough.
[01:53] The thought was that since models are so
[01:55] good at React, every app would be built
[01:56] with it.
[01:58] Now, models are similarly proficient in
[02:00] HTML, Swift, and even their own JSON
[02:02] formats.
[02:03] The fear that React would be the final
[02:05] language missed the mark.
[02:06] In fact, he says more people are
[02:08] creating their own languages.
[02:09] The third was the worry that diffusion
[02:11] models would swallow up art.
[02:13] That only images untouchable by humans
[02:14] would flood the world.
[02:15] In reality, LLMs draw with code and
[02:17] directly manipulate Blender, Photoshop,
[02:20] and Figma. They are drawing with the
[02:22] same tools as humans.
[02:23] Bash, React, and diffusion models.
[02:25] These three wrong answers actually came
[02:27] from a single fear.
[02:29] The "lesson" in his talk title refers to
[02:30] a short essay by reinforcement learning
[02:32] expert Richard Sutton in 2019.
[02:34] The biggest lesson from 70 years of AI
[02:35] research is that general methods that
[02:37] leverage massive computation eventually
[02:38] win by a large margin.
[02:40] It means that forcing human ways of
[02:41] thinking into models doesn't work in the
[02:43] long run. It is a bitter lesson for
[02:45] humans.
[02:46] The image next to it is Shoggoth. It’s a
[02:48] meme of a tentacled monster wearing a
[02:49] smiling mask, comparing AI to an
[02:50] inscrutable alien intelligence.
[03:23] So, he asks. Can we keep humans at the
[03:25] center while still believing in AGI?
[03:28] This also explains why this question has
[03:29] reached developers first. What happens
[03:31] in software will eventually spread to
[03:32] other forms of knowledge work.
[03:35] He views current AI as both an
[03:36] industrial revolution and a renaissance
[03:38] .
[03:39] This year was the early stage of that
[03:40] industrial revolution.
[03:41] The term "software factory" has become
[03:43] common, and building software is no
[03:44] longer a bottleneck.
[03:46] Industrialization is about competing to
[03:48] deliver fast, reliable, and cheap
[03:49] products.
[03:50] A renaissance, on the other hand, is
[03:51] about creating something no one has ever
[03:52] seen before.
[04:19] >> Recently, we have factories and
[04:20] workshops creating novel things. The
[04:22] point is that both are now operating
[04:23] simultaneously.
[04:25] When discussing AI capabilities, the
[04:26] term "jagged frontier" is often used.
[04:29] It came from a 2023 study by Harvard
[04:30] Business School researchers in
[04:32] collaboration with BCG.
[04:34] It means that even if tasks look similar
[04:35] in difficulty, AI handles some easily
[04:37] but cannot do others at all.
[04:39] In an experiment with 758 consultants,
[04:41] quality rose by over 40%for tasks within
[04:43] the frontier.
[04:45] However, for tasks outside the frontier
[04:47] , those using AI were 19 percentage
[04:48] points less likely to get the right
[04:50] answer.
[04:51] Tariq also started by showing this
[04:52] frontier. A single function, a single
[04:54] feature, a to-do app, a Slack clone.
[04:56] And now, it’s at the level of asking to
[04:58] build Mario Kart from scratch.
[04:59] What we see in benchmarks is always just
[05:01] the edge of the frontier.
[05:02] What he focused on more was the inside
[05:04] of the frontier.
[05:05] He called this the "smooth interior."
[05:08] If it knows how to use React, it can
[05:09] also use Figma files, JSON, and Bash.
[05:12] It means that beneath the frontier, it
[05:13] isn't jagged but uniformly expansive.
[05:36] So now, you can have it perform tasks in
[05:37] the way you want. Converting a mockup
[05:39] into HTML, React, or a Figma file.
[05:41] Or you can have it operate the computer
[05:43] directly to create a video in After
[05:44] Effects.
[05:46] He says most of the harnesses and
[05:47] scaffolding we put around models today
[05:49] will soon become unnecessary.
[05:50] If the model is perfect, it will write
[05:52] correct code from the start without
[05:54] needing separate security audits. This
[05:56] is, of course, just his own outlook.
[05:58] He showed an image to illustrate this
[06:00] smooth interior.
[06:01] It is an evaluation uploaded by a user
[06:03] named Celestia and introduced by Andrej
[06:04] Karpathy.
[06:05] The model is given latitude and
[06:06] longitude coordinates in text and asked
[06:07] whether it is land or water.
[06:09] It is asked 16,200 times across the
[06:10] entire Earth, and the answers are
[06:11] plotted as dots.
[06:12] Karpathy added this. The model knows. By
[06:15] compressing the internet.
[06:17] On the top left, Sonnet 3.5 at 60%
[06:19] doesn't show the continents properly.
[06:21] Opus 4.6 at 91%captures blurry outlines
[06:24] , and Opus 5.5 at 99%is almost a real
[06:27] map.
[06:29] It is a globe drawn by a model that
[06:30] learned only from text, without images
[06:31] or tools.
[06:33] What Tariq saw in this map wasn't
[06:34] benchmark scores, but the breadth of the
[06:36] model's general knowledge.
[06:38] And he displayed this sentence.
[06:40] We can now use intelligence to
[06:41] understand and shape the way we use
[06:43] intelligence.
[06:45] Now, let's go back to the game we
[06:46] started with. He is someone who ran a
[06:47] game company funded by Y Combinator for
[06:49] five years.
[06:51] When he first unveiled the game at the
[06:52] end of September, he wrote this.
[06:53] That the game creation process is
[06:54] creative work, so don't let AI replace
[06:56] it entirely.
[06:57] It is a 2D isometric fighting game. You
[06:59] win by pushing your opponent off the
[07:00] circular platform.
[07:24] The model decides the answers to those
[07:26] questions on its own.
[07:27] Furthermore, I couldn't stay immersed
[07:28] because I’d send a prompt and come back
[07:29] after doing other work.
[07:31] He revealed that as a result, he
[07:32] actually made more progress.
[07:34] Two weeks before the announcement, he
[07:36] left a similar post on X. That if you
[07:37] get hooked on coding agents, you feel
[07:38] like you're doing a lot of work, but in
[07:40] reality, nothing is progressing.
[08:04] He believes a great work is ultimately
[08:05] the result of choices. It's about what
[08:07] you include and what you exclude that
[08:08] creates the work.
[08:10] To do that, you must be an expert who
[08:11] knows the ins and outs.
[08:12] But he says that even if you look at
[08:14] code written by "vibing," you have no
[08:15] idea what's happening.
[08:17] His solution was to split the codebase
[08:19] in two. One is the engine, and the other
[08:22] is a folder called "spec" or simply "
[08:23] human."
[08:25] The "human" folder is the code that he
[08:26] reads himself.
[08:27] He applies linting and gives Claude
[08:29] rules on what this code should look like
[08:30] .
[08:47] The file opened in the demo is the
[08:49] rock-throwing skill ` rock.ts`.
[08:51] Speed, mass, size, and range are all
[08:52] written there.
[08:53] Instead of numbers like "x 0.5," he uses
[08:55] meters and seconds, and every line has a
[08:57] comment explaining what it means.
[08:59] There are also three different ways to
[09:00] pick up a rock.
[09:01] You can tear it from the ground, pick it
[09:03] up from a pile, or break through a wall
[09:05] you built and throw it.
[09:06] Even without knowing the engine, the
[09:07] true logic of this character is all
[09:09] visible here.
[09:10] In effect, he has created a
[09:11] game-specific scripting language.
[09:13] If you want the rock to be bigger, you
[09:14] just need to change one number.
[09:15] Returning to the game, he charges up and
[09:17] throws, and a massive boulder flies out
[09:18] .
[09:18] He says he uses Cursor's Tab
[09:20] autocomplete a lot these days.
[09:21] If you write a comment saying, "When a
[09:22] wall is built, queue the actions," the
[09:24] Tab key fills in the rest.
[10:01] Complex basic blocks are still created
[10:03] by Claude. However, he is the one who
[10:05] reads and edits how they are woven
[10:06] together.
[10:07] He said he is also still in the early
[10:08] stages.
[10:10] His conclusion is not to guess what the
[10:12] model is good at writing, but to ponder
[10:14] the best way to release good software.
[10:16] These are the ingredients for the
[10:17] renaissance he identified.
[10:19] New languages that are fast, expressive
[10:21] , and instant; new databases and servers
[10:24] ; new interactions with OS; old HCI
[10:26] research worth re-reading; new
[10:28] aesthetics;
[10:29] and software that users can modify
[10:31] themselves.
[10:56] Developers who didn't know what their
[10:58] game characters were saying can now read
[10:59] and fix the speed and size of a single
[11:01] stone themselves.
[11:02] To sum up, the model didn't stick to one
[11:04] method, its range of capabilities
[11:05] broadened evenly, and that means we can
[11:07] decide the approach.
[11:09] Of course, the idea that harnesses will
[11:10] become unnecessary is his outlook, and
[11:12] by his own admission, the human folder
[11:13] is still an early experiment.
[11:15] In your codebase, is there a folder that
[11:16] you read yourself? Or is everything
[11:18] flowing exactly as the model has
[11:19] determined?
