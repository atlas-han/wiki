---
title: "에이전트가 자기 PR을 직접 머지한다 | Cursor 엔지니어 Lauren Tan이 에이전트를 믿게 된 방법 10분 정리"
type: video
source: https://www.youtube.com/watch?v=ezPSsVW92Mg
site: youtube.com
author:
  - "[[Tech Bridge]]"
duration: 10:14
published: 2026-11-13
created: 2026-11-14
description: "Tech Bridge 한국어 해설 10:14, 공식 챕터 9, Korean original(AI 음성 TTS · ko-orig variant=gemini). Lauren Tan의 Maven 워크숍 'How Cursor Turned AI Agents Into Better Engineers'(설명란 2026-08-12)와 본인 글(The Complete Guide to pstack Pt. 1 · Loops You Can Trust)을 바탕으로 신뢰 곡선을 한 계단씩 — 검증(control-glass), 피처 맵, 실패를 스킬로 · 스킬은 eval로, 클라우드 에이전트와 Benny, Dune, CI로 금지하기와 5단 강제 계층, 토큰 vs 사람 · PM이 머지하는 팀. Lauren 원음 발췌 다섯 곳 중 두 곳만 en-orig에 영어 조각이 남음."
tags:
  - clippings/youtube
---

**Source URL**: https://www.youtube.com/watch?v=ezPSsVW92Mg
**Channel**: Tech Bridge · **Duration**: 10:14 · **Published**: 2026-11-13

> **게시일 — 멤버 전용 → 공개 전환.** 처음 목록에 나온 것은 2026-11-10 회차(`upload_date` 20261109, `subscriber_only`)였고 11-13까지 멤버 전용이었다. 2026-11-14 회차에 **`public`** 이고 info.json `upload_date` **`20261113`**, `timestamp` 1794560410(= 2026-11-13 09:00:10 UTC = **2026-11-13 18:00 KST**) — 공개 전환 시점 쪽으로 날짜가 바뀌는 기존 패턴과 같다. 제목은 그대로다. 파일명 · `date-published`는 공개 기준 날짜(11-13)를 쓴다. 파일명에서 `|`는 뺐다.
>
> **오디오 트랙과 자막 — 인용 규칙.** 오디오는 `Korean original (default)`(low · medium) + 영어 더빙(`en` · `en-US`), 메타 `language`=`en`. 수동 자막 없음. `ko` = `ko-orig`(md5 동일, `kind=asr&lang=ko&variant=gemini`). `en-orig`(`lang=en&variant=timing-optimized`)는 **영어 더빙 ASR**이다(Lauren → `Rorōn X. Ten` · `Lo`, Grok 4 팀 → `Grok board team`). → **내레이션 인용은 ko-orig.** 429 없음(`--sleep-subtitles 8`).
>
> **원음 발췌.** ko-orig 무캡션 구간(`gaps.py` 4.5초 기준): 00:10~00:26 · 02:32~02:43 · 06:06~06:18(*[웃음]*만) · 08:27~08:40 · 09:20~09:28 · 09:34~09:48(*[음악]*). 이 중 **en-orig에 Lauren의 영어 원음 조각이 남은 곳은 두 곳**이다: 00:17~00:24 *"Like I woke up today and there were like 20 PRs landed and I just reviewed them on main like they were already landed and they were good."* · 06:10~06:16 *"Quality is actually not that good. And so I often joke that like you know before AI slop we had human slop."* (11-12 Karp 편과 같은 구성 — 원음 조각만 en-orig로 인용). 나머지(02:32~02:43 · 08:27~08:40 · 09:20~09:28)는 두 트랙 모두 비어 내용 미상.
>
> **ASR 판독(ko-orig).** *스페이스 엑스 에이아이*(00:26) → SpaceX AI, *로런 텐 · 로러 · 로퍼 · 로러이 · 로로 · 로론*(00:29 · 04:17 · 05:19 · 05:30 · 08:23 · 08:49) → Lauren Tan / Lauren(*로퍼에서* 05:19 → 로컬에서, 추정), *균 덕분에*(00:32) → (판독 불가 — 도구 이름으로 추정, ⚠️ 미확정), *자기 PR을 직접 보지 않는다고요. 리뷰는요.*(00:35~00:37) → 자기 PR을 직접 머지한다 · 리뷰는(추정 — 제목), *결정적 증거*(01:08), *CPU 트레이스를 iOS 시뮬레이터를 여는*(01:58~02:00) → CPU 트레이스를 뜨고 iOS 시뮬레이터를 여는(추정), *컨트롤 글래스*(02:54) → control-glass(챕터), *실체화된 기억*(03:44) → materialized memory(추정 — 09-26 소스의 *구체화된 기억*), *피스택 · 피스텍*(03:52 · 04:06) → pstack, *크리에이트 베리피케이션*(03:52~03:53) → create-verification, *게리 태닛의 플러그인 시스텍*(04:08~04:10) → Garry Tan의 gstack, *서원은 같지만*(04:12) → 성은 같지만(추정), *에발*(04:56) → eval, *조정 에이전트*(05:00) → 조정자(orchestrator) 에이전트, *루프 명령*(05:15) → loop 명령, *베니*(05:31) → Benny, *듄*(06:50) → Dune, *넥스트 JS*(06:52) → Next.js, *유즈 이펙트*(07:24) → `useEffect`, *그 PR 하나에 한 마리였는데요*(07:39) → (판독 불가), *규칙과 버그 고문*(08:10) → 규칙과 bugbot(추정 — 09-26 소스의 다섯 층), *그록 포 팀*(09:15) → Grok 4 팀(추정, en-orig `Grok board team`).
>
> ⚠️ **해설과 발화를 구분.** 내레이션은 AI 음성(설명란)이고 Lauren 본인 말로 확인되는 것은 위 영어 조각 두 개뿐이다. 수치(PR 20개 · 7월 PR 약 1,000 · 8월 커밋 2,000+ · 9월 PR 2,500 · 조회수 460만 · 메모리 4GB · PR 600+)는 해설 전달 · 자기 보고. 설명란: *"재현 화면에는 '예시'라고 표기했습니다."*

## 설명란

Cursor와 Grok Bot을 만드는 SpaceX AI 엔지니어 Lauren Tan은 자고 일어나면 에이전트가 머지해 둔 PR을 main에서 확인합니다. 한 달에 PR 2,500개를 배포하기까지, 에이전트를 어떻게 믿게 됐을까요?

2026년 8월 워크숍과 본인이 쓴 글·게시물을 바탕으로, 에이전트를 믿게 되기까지의 단계를 정리했습니다: 검증 스킬, 피처 맵, 실패에서 만든 스킬과 eval, 클라우드 에이전트, 에이전트용 아키텍처 Dune, 그리고 리뷰 댓글 대신 CI 규칙.

타임라인
0:00 자고 일어났더니 PR 20개가 main에
1:01 신뢰가 먼저다: 신뢰 곡선
1:53 첫 계단, 검증 (control-glass)
3:12 피처 맵: 에이전트에게 앱 지도 주기
4:06 실패를 스킬로, 스킬은 eval로
5:19 클라우드 에이전트와 Benny
5:55 Dune: 에이전트용 아키텍처
7:17 CI로 금지하기와 5단 강제 계층
8:48 토큰 vs 사람, 그리고 PM이 머지하는 팀

참고
- 워크숍 "How Cursor Turned AI Agents Into Better Engineers" (Maven, 2026-08-12): https://maven.com/p/e23d9c/how-cursor-turned-ai-agents-into-better-engineers
- 인용 클립 원본 영상: https://www.youtube.com/watch?v=04FAVmmLSGc
- Lauren Tan, "The Complete Guide to pstack Pt. 1": https://x.com/poteto/status/2094457600259842065
- Lauren Tan, "Loops You Can Trust": https://x.com/poteto/status/2069824386283319343
- pstack (cursor/plugins): https://github.com/cursor/plugins/tree/main/pstack

이 영상의 내레이션은 AI 음성(TTS)이며, 일부 이미지는 AI로 생성했습니다. 재현 화면에는 "예시"라고 표기했습니다.

#AI에이전트 #Cursor #개발자 #AI코딩 #pstack

> info.json `tags`: AI 에이전트 · AI 코딩 · CI · Cursor · Grok Bot · Lauren Tan · Tech Bridge · pstack · 에이전트 검증 · 코드 리뷰

## 트랜스크립트 — ko-orig (원 오디오 ASR, `lang=ko&variant=gemini` — `ko`와 바이트 동일 · 인용 근거)

[00:00] 아침에 일어났더니 밤사이 PR
[00:02] 20개가 이미 메인 브랜치에 들어가
[00:03] 있습니다. 사람이 머지 버튼을 누른
[00:05] 적은 없습니다. 에이전트가 직접
[00:07] 올리고 직접 합쳤죠.
[00:26] 이 말을 한 사람은 스페이스 엑스
[00:28] 에이아이에서 커서와 그록 봇을 만드는
[00:29] 엔지니어 로런 텐입니다.
[00:31] 8월에 로런은 엑스에 이렇게
[00:32] 썼습니다. 균 덕분에 이제 에이전트가
[00:35] 자기 PR을 직접 보지 않는다고요.
[00:37] 리뷰는요. 자리를 비우거나 자는 동안
[00:39] 메인에 들어간 걸 나중에 봅니다.
[00:41] 숫자도 있습니다. 7월엔 PR이 거의
[00:43] 1,000개, 8월엔 한 달 커밋이
[00:45] 2,000개를 넘었습니다.
[00:46] 9월에 PR 2,500개를 배포한
[00:48] 방법을 공개한 게시물은 조회수
[00:49] 460만 회를 넘겼죠.
[00:51] 우리는 에이전트 하나가 쓴 코드도 한
[00:53] 줄씩 다시 읽습니다. 그런데 어떻게
[00:54] 이게 가능할까요?
[00:56] 오늘은 로런이 한 시간짜리 워크숍에서
[00:57] 풀어놓은 방법을 신뢰라는 곡선을 따라
[01:00] 한 계단씩 올라가 보겠습니다.
[01:02] 로런이 가장 먼저 꺼낸 단어는 의외로
[01:04] 기술이 아니라 신뢰였습니다.
[01:06] 에이전트는 추측하고 환각을 보고
[01:08] 100번째로 결정적 증거를 찾았다고
[01:10] 자신있게 말하죠.
[01:11] 그런데 그게 진짜 원인이 아니면
[01:13] 신뢰는 무너집니다.
[01:15] 로런은 이걸 팀 관리에 비유합니다.
[01:17] 팀원을 못 믿는 관리자는 결국
[01:19] 마이크로매니징을 하게 돼 있으니까요.
[01:21] 어깨 너머로 일일이 들여다보면서
[01:22] 버그가 나가지 않는지 확인하는 거죠.
[01:24] 그래서 로런이 그린 그래프가
[01:26] 이겁니다.
[01:27] 가로축은 동시에 돌리는 에이전트 수,
[01:29] 세로축은 [음악] 신뢰입니다.
[01:31] 1년쯤 전엔 에이전트 몇 개를 붙잡고
[01:33] 모든 출력을 지켜봤습니다. 하나도 못
[01:35] 믿는데 100개를 띄울 순
[01:36] 없으니까요.
[01:37] 지난 다섯 달 동안 로런은 이 곡선을
[01:39] 올라 지금은 에이전트가 PR을 스스로
[01:41] 머지하는
[01:43] 지름길은 없다고 합니다. 아직 여기
[01:45] 있으면서 갑자기 수천 개를 띄우면
[01:47] 토큰만 날린다고요. 그럼 이 곡선의
[01:48] 첫 계단은 뭘까요? 로런의 답은 한
[01:51] 단어였습니다.
[01:52] 검증.
[01:54] 검증이란 에이전트가 자기 작업을 직접
[01:56] 확인하는 겁니다. 코드를 실제로
[01:58] 실행하고 CPU 트레이스를
[02:00] iOS 시뮬레이터를 여는 거죠.
[02:02] 로런의 말로는 이게 좋은 코드를
[02:04] 보장하진 않지만 적어도 맞는 코드는
[02:06] 쓰게 해준다는 겁니다.
[02:07] 이 깨달음에는 사연이 있습니다.
[02:09] 커서에 입사한 둘째 날 매니저에게서
[02:11] 메시지가 옵니다. 에이전트 창 성능이
[02:13] 별로인데 리액트 좀 아시죠?
[02:15] 도와줄래요? 아 그리고 며칠 뒤에
[02:17] 출시예요.
[02:18] 코드 베이스는 처음 보는 상태
[02:20] 크롬 개발자 도구로 트레이스를 띄워
[02:21] 해도 메모리가 4GB 한도에 걸려
[02:24] 앱이 먼저 죽곤 했습니다.
[02:25] 에이전트에게 물어도 소용없었습니다.
[02:27] 자신있게 원인을 짚었지만 고쳐보면
[02:29] 그게 아니었죠.
[02:43] 에이전트가 코드를 쓰면 사람이 빌드를
[02:45] 열어봅니다. 안 되면 스크린샷과 콘솔
[02:47] 오류를 복사해서 다시 붙여 주죠. 이
[02:49] 고리 안에 사람이 끼어 있는 한
[02:51] 에이전트를 여러 개 돌릴 방법이
[02:52] 없습니다.
[02:53] 그래서 로런이 처음 만든 스킬이
[02:54] 컨트롤 글래스입니다.
[02:56] 글래스는 에이전트 창의 사내
[02:57] 코드명이에요.
[02:58] 크롬 개발자 도구 프로토콜로 개발
[03:00] 빌드를 띄워서 클릭하고 입력하고
[03:02] 스크린샷과 영상을 찍고 CPU
[03:04] 프로파일과 힙 스냅샷까지 뜹니다.
[03:06] [음악] 이제 에이전트가 직접
[03:07] 재현하고 측정하고 고치고 같은 측정을
[03:09] 다시 돌립니다. 사람 없이 고리가
[03:11] 닫힌 거죠.
[03:13] 근데 앱을 조정할 수 있게 되자 새
[03:14] 문제가 생겼습니다.
[03:16] 에이전트가 앱을 모른다는 거였죠.
[03:18] 누가 왼쪽 사이드바가 버벅인다고 하면
[03:20] 에이전트는 그 기능이 어디 있는지
[03:21] 찾느라 한참을 헤맸습니다.
[03:23] 사내 제보 채널엔 이런 것도 옵니다.
[03:25] 스크린샷 한 장에 물음표 세 개
[03:27] 그래서 만든 게 피처 맵입니다. 앱의
[03:29] 모든 기능을 사용자 입장서 무엇이고
[03:31] 어떻게 가는 지 정리한 지도죠.
[03:33] 이 지도가 있으면 물음표 세 개짜리
[03:35] 제보도 어느 기능 이야기인지 짚어낼
[03:37] 수 있습니다.
[03:38] 실제 화면에 보면 기능마다 가는 길과
[03:40] 단축키, 자동화로 누를 때 쓸 돔
[03:42] 속성까지 적혀 있습니다.
[03:44] 로런은 이걸 실체화된 기억이라고
[03:45] 부릅니다.
[03:46] 코드 베이스를 토큰이 덜 들게 압축해
[03:48] 둔 기억이라는 거죠.
[03:50] 이 과정을 자동으로 해주는 게 로런이
[03:52] 공개한 플러그인 피스택의 크리에이트
[03:53] 베리피케이션 스킬입니다.
[03:55] 저장소를 살펴서 앱을 띄우고 조작하고
[03:58] 증거를 남기는 검증 스킬과 피처 맵
[04:00] 초안을 만들어 줍니다.
[04:01] 그리고 한 번도 실행해 보지 않은
[04:02] 스킬은 초안일 뿐 완성품이 아니라고
[04:04] 못박아둡니다.
[04:06] 피스텍이라는 이름도 재밌습니다. Y
[04:08] 콤비네이터 대표 게리 태닛의 플러그인
[04:10] 시스텍을 살짝 놀린 이름이거든요.
[04:12] 서원은 같지만 아무 관계도 없고
[04:14] 피스텍의 피는 포테이토, 감자
[04:15] 자루라는 뜻이랍니다.
[04:17] 로러는 처음부터 피스텍을 만들 생각이
[04:19] 없었습니다. 시작은 에이전트를 지켜본
[04:21] 관찰이었죠.
[04:22] 버그를 물으면 에이전트는 이게
[04:24] 원인이라고 단정했는데 도구 호출
[04:26] 기록을 열어보니 관련 코드를 읽지도
[04:28] 않았던 겁니다.
[04:29] 여기서 다시 관리자 비유가 나옵니다.
[04:31] 실력은 좋은데 회사 맥락은 하나도
[04:33] 모르는 5초 전에 입사한 신입이라고
[04:35] 생각해 보라는 거죠.
[04:36] 그런 신입을 가르치는 도구가
[04:37] 스킬입니다.
[04:38] 그냥 마크다운이지만 좋은 지침을 주면
[04:41] 에이전트에게서 더 좋은 실력을 끌어낼
[04:42] 수 있습니다.
[04:44] 그래서 실패를 볼 때마다 스킬로
[04:45] 만들었습니다. 코드부터 찾아 읽어라,
[04:47] 서브 에이전트를 많이 써라, 추측하지
[04:49] 마라.
[04:50] 로러의 글에는 이 목록이 더 길게
[04:51] 나옵니다. 코드를 건드리기 전에
[04:53] 버그부터 재현하고 실패하는 테스트를
[04:55] 먼저 쓰는 식이죠.
[04:56] 스킬이 정말 효과가 있는지는 에발로
[04:58] 확인합니다. 로러는 에이전트를 위한
[05:00] 유닛 테스트라고 설명합니다. 조정
[05:02] 에이전트가 채점 기준을 만들고 서브
[05:04] 에이전트 여러 개에게 같은 일을
[05:05] 시킵니다. 재밌는 건 폴더
[05:07] 이름입니다. 평가받는 중이란 걸
[05:09] 눈치채지 못하게 지었습니다.
[05:10] 에이전트도 시험인 걸 알면 행동이
[05:12] 달라지거든요.
[05:13] 채점은 다른 모델이 한 번 더 교차
[05:15] 확인하고 루프 명령으로 10점 만점이
[05:17] 될 때까지 계속 돌립니다.
[05:19] 로퍼에서 충분히 지켜보고 믿을 수
[05:21] 있게 되면 그다음은 클라우드입니다.
[05:23] 커서의 클라우드 에이전트는 각자 진짜
[05:25] 컴퓨터를 받습니다. 의존성을 설치하고
[05:27] 앱을 실행하고 사용자처럼 화면을
[05:29] 다루죠.
[05:30] 로러이 자주 소개하는 에이전트가
[05:31] 있습니다. 이름은 베니.
[05:33] 버그 제보를 받으면 클라우드에 커서를
[05:35] 띄우고 직접 재현해 봅니다.
[05:37] 이 스레드에서 베니는 버그를
[05:38] 재현했지만 이미 메인에서 고쳐졌다고
[05:40] 알려줍니다. 남은 일은 새 빌드를
[05:42] 내보내는 것뿐이죠.
[05:44] 한 시간 동안 에이전트와 씨름해야
[05:45] 알던 정보를 그냥 받는 겁니다.
[05:47] 그리고 이건 로러 혼자가 아니라 팀
[05:49] 전체가 누립니다.
[05:50] 그래서 로러는 이렇게까지 썼습니다.
[05:52] 워크트리는 끝났다. 클라우드
[05:54] 에이전트가 미래다.
[05:56] 여기까지가 검증과 스킬이었다면 세
[05:58] 번째 이야기는 좀 논증적입니다. 앱을
[06:00] 다시 짜야 하느냐는 문제죠.
[06:02] 로러는 메타에서 일했습니다. 수만
[06:04] 명의 엔지니어가 거대한 모노레포에
[06:06] 코드를 밀어넣던 곳이죠.
[06:12] >> [웃음]
[06:18] >> 그래서 빅테크엔 이미 가드레일이
[06:20] 가득합니다. 프레임워크, 관례, 권한
[06:22] 제한까지. 가장 경험 적은 엔지니어도
[06:24] 사고를 못 치게 해요.
[06:26] 그런 곳에서는 에이전트도 꽤 잘
[06:27] 해냅니다.
[06:28] 정작 위험한 건 새로 시작한 앱,
[06:30] 그린필드입니다.
[06:31] 그록봇이 그랬습니다. 프로토타입을
[06:33] 바이브 코딩으로 빠르게 만들었고
[06:35] 코드를 읽는 사람은 아무도 없었죠.
[06:37] 가드레일이 없으면 에이전트는 그때그때
[06:39] 가장 편한 방법으로 문제를 풉니다.
[06:41] 그렇게 쌓인 코드는 아무도 이해 못
[06:43] 하는 쪽으로 불어나죠.
[06:44] 그래서 로러는 그록봇 전체를 새
[06:46] 아키텍처로 옮겼습니다. 세어보니
[06:48] PR만 600개가 넘었다고 합니다.
[06:50] 그 아키텍처의 이름이 듄입니다.
[06:52] 일렉트론 앱을 위한 넥스트 JS 같은
[06:54] 것인데 처음부터 에이전트가 쓰도록
[06:56] 설계했죠.
[06:57] 듄 문서는 에이전트를 이렇게
[06:58] 묘사합니다.
[06:59] 가장 가까운 패턴을 베끼고 이미 열린
[07:01] 파일을 고치고 컴파일 되는 가장 짧은
[07:03] 길을 고른다.
[07:05] 그래서 핵심 원칙은 하나입니다. 가장
[07:07] 짧은 길이 가장 좋은 길이 되게
[07:08] 만든다. 지름길을 정답으로 만드는
[07:10] 거죠.
[07:11] 예를 들어 기능 하나는 폴더 하나에
[07:13] 모여 있어서 에이전트는 여기저기 뒤질
[07:15] 필요 없이 그 폴더 안에서만 일하면
[07:16] 됩니다.
[07:18] 그리고 에이전트가 자주 틀리는 건
[07:20] 전부 CI로 막았습니다.
[07:21] 예를 들어 리액트의 대표적인 함정,
[07:24] 유즈 이펙트.
[07:25] 듄에서는 금지라서 쓰면 CI가
[07:27] 실패하고 소리를 지릅니다.
[07:29] 코드 주석도 금지했습니다.
[07:30] 에이전트가 쓰는 주석의 대부분이 지금
[07:32] 코드와 상관없는 지난 이야기였거든요.
[07:35] 로러가 절대 이렇게 하지 말랬음.
[07:37] 같은 주석이 코드에 박히는 식이죠.
[07:39] 그 PR 하나에 한 마리였는데요.
[07:41] 로러는 이런 주석을 잡초에
[07:42] 비유합니다.
[07:43] 에이전트는 있는 걸 베끼니까 임시방편
[07:45] 주석 하나가 금방 코드베이스 전체로
[07:47] 번진다고요.
[07:49] 앱 구조도 강제합니다.
[07:50] UI를 그리는 렌더러와 나머지 일을
[07:52] 하는 메인 프로세스를 폴더로 [음악]
[07:54] 나누고 서로 잘못 가져오면 CI가
[07:56] 의존성 그래프를 보고 막습니다.
[07:58] 초당 60프레임을 내려면 [음악] 한
[08:00] 프레임을 16밀리초에 그려야 하는데
[08:02] 무거운 코드가 렌더러로 새어 들어오면
[08:04] 화면이 버벅이니까요.
[08:05] 로러는 이런 강제 장치를 다섯 층으로
[08:07] 나눕니다. 코드 베이스, 정적 분석,
[08:10] 규칙과 버그 고문, 스킬, 그리고
[08:12] 스타일 가이드.
[08:13] 이 중 위에 두 층만 CI를 빨갛게
[08:15] 만듭니다.
[08:16] 나머지는 에이전트가 잊어버릴 수 있는
[08:18] 부드러운 장치죠.
[08:20] 부드러운 장치에만 기대면 코드
[08:21] 베이스가 엉망이 되는 건 시간
[08:23] 문제라고 로로는 꽤 직설적으로
[08:24] 말합니다.
[08:40] 사람이 PR에 댓글로 이러지
[08:42] 마세요라고 다는 순간을 코드 냄새로
[08:44] 보라는 겁니다. 그 지적을 린트
[08:46] 규칙이나 CI 실패로 바꾸라는 거죠.
[08:49] 물론 공짜는 아닙니다. 로론도 자신의
[08:51] 토큰이 사실상 무제한인 AI 연구소에
[08:53] 있다는 걸 인정합니다.
[08:54] 코드 베이스를 리팩토링하고 이런
[08:56] 장치를 다는 데는 처음에 토큰이 많이
[08:58] 듭니다.
[08:59] 그래서 이건 거래라고 말합니다.
[09:01] 사람을 더 뽑을지, 토큰을 써서 가장
[09:03] 단순한 에이전트도 잘 해내는 코드
[09:05] 베이스를 만들지.
[09:06] 혼자서 이 프레임워크를 만들고
[09:08] 리팩토링하고 검증했다면 몇 년은
[09:10] 걸렸을 일이라고요.
[09:12] 그 그 보상은 엔지니어가 아닌
[09:13] 사람들에게서 먼저 보였습니다.
[09:15] 그록 포 팀에선 PM과 디자이너도
[09:17] 코드를 보냅니다.
[09:28] 엄격한 제약이 있으니 엔지니어링
[09:30] 전문가가 아니어도 높은 수준으로
[09:31] 기여할 수 있다는 겁니다.
[09:42] [음악]
[09:48] 처음 장면으로 돌아가 볼까요?
[09:50] 자고 일어났더니 메인에 들어가 있던
[09:52] PR 20개.
[09:53] 그건 더 똑똑한 모델의 마법이
[09:54] 아니었습니다.
[09:56] 스스로 검증하는 에이전트, 실패해서
[09:58] 만든 스킬, 그리고 나쁜 코드를 쓸
[10:00] 수 없는 코드 베이스였죠.
[10:02] 워크숍 진행자도 자기는 아직 로컬에서
[10:04] 두 세 개 돌리는 단계라고 했습니다.
[10:05] 아마 대부분이 그렇겠죠.
[10:07] 여러분은 지금 신뢰 곡선의 어디쯤에
[10:09] 계실까요?
[10:10] 그리고 오늘 어떤 리뷰 댓글 하나를
[10:12] 규칙으로 바꿀 수 있을까요?

## 트랜스크립트 — en-orig (영어 더빙 트랙 ASR — 대조용, 단 00:17~00:24 · 06:10~06:16은 Lauren 원음 영어 조각 · 그 두 곳만 인용)

[00:00] I woke up this morning, and the PRs from
[00:02] last night were already merged into the
[00:03] main branch. No human ever pressed the
[00:05] merge button. The agent uploaded and
[00:07] merged them itself. Yeah.
[00:17] Like I woke up today and there were like
[00:20] 20 PRs landed and I just reviewed them
[00:22] on main like they were already landed
[00:24] and they were good. The person who said
[00:26] this is Rorōn X. Ten, an engineer at xAI
[00:29] who builds Cursor and the Grok bot. In
[00:31] August, Rorōn wrote this on X. "Thanks
[00:34] to Gyun, agents now merge their own PRs
[00:36] .""And reviews too.""I just look at what
[00:39] made it into main while I was sleeping.
[00:41] " There are numbers, too. In July, there
[00:43] were nearly 1,000 PRs, and in August,
[00:45] monthly commits exceeded 2,000. His post
[00:47] revealing how he deployed 2,500 PRs in
[00:49] September surpassed 4.6 million views.
[00:51] We still read every single line of code
[00:53] written by an agent. But how is this
[00:55] even possible? Today, we’ll climb up the
[00:57] curve of trust, step by step, using the
[00:59] method Rorōn laid out in a one-hour
[01:01] workshop.
[01:02] Surprisingly, the first word Rorōn
[01:04] brought up wasn't technology; it was
[01:06] trust. Agents guess, hallucinate, and
[01:08] confidently claim they've found the
[01:09] definitive evidence for the hundredth
[01:11] time. But if that’s not the real cause,
[01:13] trust collapses. Rorōn compares this to
[01:16] team management. A manager who can't
[01:18] trust their team members ends up
[01:20] micromanaging. They watch over
[01:21] everyone's shoulders, checking
[01:22] constantly to make sure no bugs slip
[01:24] through. So, this is the graph Rorōn
[01:26] drew. The horizontal axis is the number
[01:28] of agents running simultaneously, and
[01:30] the vertical axis is trust. About a year
[01:31] ago, we were stuck with a few agents,
[01:33] watching every single output. You can’t
[01:35] run 100 agents if you don't trust a
[01:36] single one. Over the past five months,
[01:38] Rorōn has climbed this curve, and now,
[01:40] he’s at the point where agents merge PRs
[01:42] on their own. He says there are no
[01:44] shortcuts. If you try to jump to
[01:45] thousands of agents while still at the
[01:47] bottom, you’ll just waste tokens. Then,
[01:48] what is the first step on this curve?
[01:50] Rorōn’s answer was one word.
[01:52] Verification.
[01:54] Verification means the agent checks its
[01:56] own work. It actually executes the code
[01:59] , captures CPU traces, and opens the iOS
[02:01] simulator.
[02:02] According to Rorōn, this doesn't
[02:04] guarantee great code, but it at least
[02:06] ensures the code is correct. There’s a
[02:08] backstory to this realization. On his
[02:10] second day at Cursor, he got a message
[02:11] from his manager. "The agent window
[02:13] performance is bad; you know React,
[02:15] right?""Can you help?""Oh, and we're
[02:17] launching in a few days." He was looking
[02:19] at the codebase for the first time.
[02:20] Even trying to trace it with Chrome
[02:22] DevTools, the 4GB memory limit caused
[02:24] the app to crash first. Asking the agent
[02:27] was no use. It confidently pinpointed
[02:29] the cause, but fixing it proved
[02:30] otherwise.
[02:43] >> When the agent writes code, a human
[02:45] opens the build. If it fails, they copy
[02:47] the screenshot and console logs back. As
[02:49] long as a human is in this loop, you
[02:51] can't run multiple agents. That’s why
[02:54] the first skill Loro encountered was
[02:55] Control Glass. Glass is the codename for
[02:57] the agent's window management.
[02:59] Developers launch a dev build via
[03:00] protocol, click, input, take screenshots
[03:03] and videos, and grab CPU profiles and
[03:05] heap snapshots. Now the agent reproduces
[03:07] , measures, fixes, and runs the same
[03:09] measurements again. The loop is closed
[03:11] without a human.
[03:13] But once the app could be controlled,
[03:14] three problems arose. The agent didn't
[03:16] know the app at all. If someone said the
[03:19] left sidebar was laggy, the agent would
[03:20] search for where that feature was and
[03:22] wander for a long time. In the internal
[03:24] report channel, things like this arrive
[03:25] . Just a single screenshot with three
[03:26] question marks. So, we created the
[03:28] Feature Map. It’s a map that organizes
[03:30] every app feature from the user's
[03:32] perspective. With this map, even a
[03:34] report with three question marks can be
[03:36] traced to a specific feature.
[03:39] Looking at the actual screen, it lists
[03:40] paths to features, hotkeys, and
[03:42] automation templates.
[03:44] Loro calls this "materialized memory."
[03:47] It’s memory where the codebase is
[03:48] compressed to consume fewer tokens. This
[03:50] process is automated by Loro's
[03:52] open-source plugin, P-stack's Create
[03:54] Verification Skill.
[03:56] It scans the repository, launches the
[03:57] app, operates it, records evidence, and
[03:59] creates a draft of the feature map.
[04:01] It also emphasizes that a skill that
[04:03] hasn't been executed is just a draft,
[04:05] not a finished product. The name "
[04:07] P-stack" is also quite amusing. It’s a
[04:09] playful nod to the G-stack plugin by Y
[04:11] Combinator's Garry Tan. Same surname, no
[04:13] relation, and the "P" in P-stack stands
[04:16] for "Potato." Loro didn't intend to
[04:18] create P-stack from the very beginning.
[04:20] It started with observing the agent.
[04:23] When a bug was reported, the agent
[04:24] identified the cause, but looking at
[04:26] tool logs, it hadn't even read the
[04:28] relevant code.
[04:29] This brings us back to the manager
[04:31] perspective. Think of it as a talented
[04:32] new hire who joined five seconds ago and
[04:34] knows nothing about the company context
[04:36] .
[04:36] The tool that teaches such a new hire is
[04:38] the "Skill." It's just markdown, but
[04:40] with good instructions, you can pull
[04:42] better performance from the agent. So,
[04:44] every time it failed, it was turned into
[04:46] a skill. Read the code first. Use plenty
[04:48] of sub-agents. Do not guess. This list
[04:50] appears much longer in Loro's post. It's
[04:52] a method of reproducing the bug and
[04:54] writing a failing test first, before
[04:55] touching the code.
[04:56] They verify if the skill is truly
[04:58] effective through development. Lo
[04:59] describes this as unit testing for
[05:01] agents. A coordinator agent sets the
[05:03] grading criteria and assigns the same
[05:05] task to multiple sub-agents. The funny
[05:07] part is the folder name. They name it in
[05:08] a way that the agent doesn't realize
[05:09] it's being evaluated. Agents change
[05:11] their behavior if they know they are
[05:12] being tested.
[05:14] The grading is cross-checked once by
[05:15] another model, and it loops until it
[05:17] gets a perfect score.
[05:19] Once you’ve observed it enough locally
[05:21] and can trust it, the next step is the
[05:23] cloud. Cursor’s cloud agents each get
[05:25] their own real computer. They install
[05:27] dependencies, run the app, and navigate
[05:29] the screen like a user. There is an
[05:31] agent that Lo often introduces. His name
[05:32] is Benny. When a bug report comes in, he
[05:35] launches Cursor in the cloud and tries
[05:36] to reproduce it himself. In this thread
[05:38] , Benny reproduces the bug but informs
[05:40] us it’s already fixed in main. The only
[05:42] thing left to do is to ship a new build
[05:43] .
[05:44] It’s getting information instantly that
[05:45] would otherwise take an hour of
[05:46] struggling with an agent. And this is
[05:48] something the entire team enjoys, not
[05:50] just Lo. That’s why Lo went as far as to
[05:52] say this. Worktrees are finished. Cloud
[05:54] agents are the future.
[05:56] If that was about verification and
[05:57] skills, the third story is a bit more
[05:59] controversial. It’s the question of
[06:01] whether you need to rebuild your app. Lo
[06:02] worked at Meta. It was a place where
[06:05] tens of thousands of engineers pushed
[06:06] code into a massive monorepo.
[06:10] Quality is actually not that good.
[06:13] And so I often joke that like you know
[06:16] before AI slop we had human slop.
[06:19] That’s why big tech is already full of
[06:20] guardrails. Frameworks, conventions, and
[06:22] even restricted permissions. All to
[06:23] ensure that even the least experienced
[06:25] engineer can't cause a disaster. In
[06:26] those environments, agents perform quite
[06:28] well. What’s really dangerous are new
[06:30] apps, the "greenfield" projects. That
[06:32] was the case for Grok Bot. The prototype
[06:33] was built quickly through vibe coding,
[06:35] and no one was reading the code.
[06:37] Without guardrails, agents solve
[06:39] problems in the easiest way available at
[06:41] the moment. And the code that piles up
[06:42] grows in a way that no one can
[06:44] understand. So Lo moved the entire Grok
[06:46] Bot to a new architecture. He said he
[06:48] counted and there were over 600 files.
[06:50] The name of that architecture is Nii.
[06:53] It’s like Next.js for Electron apps,
[06:55] designed from the start for agents to
[06:56] use.
[06:57] The documentation describes agents like
[06:59] this. They copy the nearest pattern, fix
[07:01] already open files, and pick the
[07:03] shortest path that compiles. So the core
[07:05] principle is simple. Make the shortest
[07:08] path the best path. It’s about making
[07:10] the shortcut the correct answer. For
[07:11] example, a single feature is contained
[07:13] within one folder, so the agent doesn't
[07:15] need to search around and only works
[07:16] within that folder.
[07:18] And we used CI to block everything the
[07:20] agents frequently get wrong. For
[07:22] instance, React's common pitfall,
[07:24] useEffect. It’s banned in Duo, so if you
[07:27] use it, the CI fails and yells at you.
[07:29] Code comments were also banned. Most
[07:31] comments written by agents were outdated
[07:33] stories irrelevant to the current code.
[07:35] "Lauren said never to do this." That
[07:37] kind of comment would get stuck in the
[07:38] code. There was even one per PR. Loro
[07:41] compares these comments to weeds. Since
[07:44] agents just copy what's there, one
[07:45] makeshift comment quickly spreads
[07:47] throughout the entire codebase. App
[07:49] structure is also enforced. The renderer
[07:51] for UI and the main process for other
[07:53] tasks are separated into folders, and if
[07:54] they import each other incorrectly, CI
[07:56] checks the dependency graph and blocks
[07:58] it. To maintain 60 frames per second,
[08:00] each frame must be drawn in 16ms; if
[08:02] heavy code runs on the renderer, the
[08:04] screen stutters. Loro divides these
[08:06] enforcement layers into five levels.
[08:08] Codebase, static analysis, rules and bug
[08:11] torture, skills, and style guides. Only
[08:14] the top two layers make the CI turn red
[08:16] .
[08:17] These are soft measures that agents can
[08:19] forget. Loro says quite bluntly that if
[08:21] you only rely on soft measures, it's
[08:23] only a matter of time before the
[08:24] codebase becomes a mess.
[08:41] He suggests seeing the moment a human
[08:42] comments "don't do this" as a code smell
[08:44] .
[08:45] He says you should turn that feedback
[08:47] into a lint rule or a CI failure.
[08:49] Of course, it's not free. Loro admits
[08:51] that he is at an AI lab where tokens are
[08:53] effectively unlimited. Refactoring the
[08:55] codebase and adding these mechanisms
[08:57] takes a lot of tokens initially. So he
[09:00] calls it a trade-off. Should you hire
[09:02] more people or use tokens to create a
[09:04] codebase where even the simplest agents
[09:06] perform well? Doing this alone—building
[09:08] , refactoring, and verifying this
[09:10] framework—would have taken years. The
[09:12] reward was first seen in non-engineers.
[09:15] On the Grok board team, PMs and
[09:17] designers also submit code.
[09:28] Because there are strict constraints,
[09:30] even those who aren't engineering
[09:31] experts can contribute at a high level.
[09:48] >> Shall we go back to the beginning? The
[09:50] 20 PRs that were merged into main when I
[09:52] woke up. That wasn't the magic of a
[09:55] smarter model. It was self-verifying
[09:57] agents, skills built through failure,
[09:59] and a codebase where bad code cannot be
[10:01] written. The workshop host also said he
[10:03] is still at the stage of running two or
[10:04] three things locally. Most people are
[10:06] probably the same. Where are you
[10:08] currently on the learning curve? And
[10:10] what review comment can you turn into a
[10:13] rule today? Ah.
