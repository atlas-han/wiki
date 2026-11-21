---
title: "검증은 과대평가됐다 | Pi 제작자 Mario Zechner"
type: video
source: https://www.youtube.com/watch?v=zU3vWXMBJAk
site: youtube.com
author:
  - "[[Tech Bridge]]"
duration: 13:51
published: 2026-11-20
created: 2026-11-21
description: "Tech Bridge 한국어 해설 13:51, 공식 챕터 10, Korean original + 영어 더빙(en-orig는 더빙 ASR — 인용하지 않음). Matt Pocock의 라이브 방송(11-17)에서 코딩 에이전트 Pi를 만드는 Mario Zechner와 Armin Ronacher가 나눈 이야기를 두 사람의 블로그 글 · Pi 저장소 기록과 맞춰 본 해설 — 시작 시간 100% 단축(앱을 지운 에이전트), Opus 5.5 이후 달라진 것, 곧은 길과 모호한 일, 이슈 분류 봇과 자동 수정의 조건 셋, 직접 읽는 코드와 하루 코드 양 한도, 검증은 과대평가됐다(테스트 수 ≠ 맞는 것을 잰다 · Lean 증명 · 조합은 검증되지 않는다), AI 리뷰는 보험(다른 회사 모델 앙상블), 이해에서 도망치는 업계와 책임, 다크 팩토리, 사람의 몫. ⚠️ 라이브 원음 발췌는 두 트랙 모두 무캡션."
tags:
  - clippings/youtube
---

**Source URL**: https://www.youtube.com/watch?v=zU3vWXMBJAk
**Channel**: Tech Bridge · **Duration**: 13:51 · **Published**: 2026-11-20

> **게시일.** info.json `upload_date` **`20261120`**, `timestamp` 1795165202(= 2026-11-20 09:00:02 UTC = **2026-11-20 18:00 KST**), `availability`=`public`. 2026-11-20 회차(09:10 KST) 뒤에 올라왔다. 파일명에서 `|`는 뺐다.
>
> **오디오 트랙과 자막 — 인용 규칙.** 오디오는 **Korean original(default) + 영어 더빙**(audio language `ko` · `en` · `en-US`), 메타 `language`=`en`. 수동 자막 없음. `ko` = `ko-orig`(파일 동일, `kind=asr&lang=ko&variant=gemini`). `en-orig`(`kind=asr&lang=en&variant=timing-optimized`)는 **영어 더빙의 ASR** 이다 — 첫 줄부터 내레이션의 영어 번역이고(*"The AI agent I ran overnight reported back in the morning."*) 고유명사를 틀린다: *마리오 제이너* → *Mario Gerner*(00:17), *파이* → *Aider*(00:19 · 00:36 · 00:44) / *Pie*(04:30 이후), *엘엔딜이 … 파이를 인수* → *Sentry, acquired Aider*(00:44), *오퍼스 5.5* → *Opus 3.5*(00:51), *로런 텐* → *Laurent Ten*(04:11). **인용하지 않고 판독 대조용으로만 쓴다.**
> ⚠️ **라이브 원음 발췌는 어느 트랙에도 잡히지 않았다.** 어제 Nadella · Blow 편과 달리 en-orig의 발췌 자리도 비어 있다(아래 무캡션 구간이 두 트랙에서 거의 같다). **Mario Zechner · Armin Ronacher · Matt Pocock 본인의 말은 캡션에 한 줄도 없고**, 위키가 인용하는 것은 전부 한국어 내레이션(ko-orig)이다. 예외로 보이는 조각 하나: **10:08~10:17** 에 ko-orig는 `>>` 표시와 함께 한국어 문장(*파일이 있고 2000개 레코드가 있다고 했죠 …*)을, en-orig는 같은 내용의 영어(*You have a file, and you said there were 2,000 records …*)를 실었다 — 발췌의 번역 캡션인지 원음인지 가리지 못해 **인용하지 않았다.** 429 없음.
>
> **무캡션 구간(`gaps.py` 4.5초 기준).** ko-orig 열여덟 곳: 01:04~01:17 · 01:19~01:46 · 01:53~02:34 · 03:24~03:55 · 04:52~05:28 · 05:46~06:24 · 06:55~07:03 · 07:10~07:31 · 08:15~08:21 · 08:49~09:04 · 09:25~09:33 · 09:41~09:47 · 10:01~10:08 · 10:20~10:37 · 10:55~11:18 · 11:29~11:37 · 12:01~12:19 · 12:48~13:13 — 합쳐 약 5분 50초, 전부 라이브 발췌 자리다(안에 `[음악]` · `[웃음]` 표시만 있다). en-orig 열다섯 곳: 00:06~00:11 · 00:59~01:45 · 01:54~02:38 · 03:24~03:55 · 04:52~05:31 · 05:48~06:24 · 06:55~07:31 · 08:10~08:27 · 08:49~09:04 · 09:25~09:47 · 10:01~10:08 · 10:55~11:23 · 11:27~11:37 · 12:01~12:19 · 12:48~13:13.
> ⚠️ **ko-orig의 열여덟 곳은 en-orig에서도 전부 비어 있다(10:20~10:37만 더빙 문장이 걸쳐 있다) — 내용 미상.** 여기에 드는 것: *Opus 5.5 이후* 에 대한 두 사람의 답 원음(01:04~01:46) · 밤샘 실험을 Mario가 직접 말한 대목(01:53~02:34) · *가중치* 설명(03:24~03:55) · 분류 봇과 자동 수정 설명(04:52~05:28) · 코드를 얼마나 읽는지(05:46~06:24) · ***검증은 과대평가됐다* 의 뜻을 Mario가 직접 푼 답(06:55~07:31)** · 앙상블 설명(08:49~09:04) · 방어적 코딩(09:25~09:47) · *이해에서 도망친다* 의 원음(10:55~11:18) · 친구와 나눈 다크 팩토리 대화(12:01~12:19) · 주니어에게 주는 답(12:48~13:13). **이 구간들에 대해 위키는 인용도 요약도 만들지 않는다** — 내레이션이 앞뒤에서 간추린 말만 적는다.
>
> **ASR 판독(ko-orig → 판독, 괄호는 근거).** *모두를 전부 뜯어냈습니다*(00:11) → 모듈을(설명란 *모듈을 전부 뜯어내*), *마리오 제이너*(00:16) → Mario Zechner(제목 · 설명란), *파이* → Pi, *립 지디엑스*(00:37~00:38) → libGDX(더빙 *libGDX*), *아르민 로나오*(00:40) → Armin Ronacher(설명란), *엘엔딜*(00:44) → Earendil(설명란 *Earendil 공동 창업자*), *아르미는 · 아르미니 · 아르미네*(03:06 · 03:54 · 07:40 · 09:15 · 09:46 · 09:57 · 10:39 · 10:42 · 11:37 · 11:56) → 아르민은 · 아르민이 · 아르민의, *데이비드 크레이머*(03:12~03:14) → David Cramer(더빙 *Sentry founder David Cramer*), *로런 텐*(04:11) → Lauren Tan, ⚠️ *있으면 엉뚱한 쪽을 고른다*(04:13) → 앞머리가 빠졌다(더빙 *If there's ambiguity* — 추정 *모호함이 있으면*), *무엇을 안 되는지*(04:26) → 무엇은 안 되는지, *메트가*(06:51) → 매트가, *젠 숫자*(07:36) → 잰 숫자, *린이라는 증명도 고로*(07:42) → Lean이라는 증명 도구로(더빙 *a proof assistant called Lean*), *단위의 문제를 씹습니다*(07:53) → 짚습니다(추정), *머신러닝 썼던*(08:44) → 머신러닝에서 썼던, *사람 코드가 나올 수도*(09:51) → 나을 수도(더빙 *easier to maintain*), *거듭 거리는 단어*(09:54) → 거듭 꺼내는(추정 — 더빙 *keep repeating*), *이해해서 도망치고*(10:50~10:52) → 이해에서 도망치고(챕터 제목), *비상 계획인 또*(11:45) → 비상 계획이 또, ⚠️ *스티브 얘기도*(12:22~12:24) → **Steve Yegge도(추정** — 더빙은 *Steve* 뿐, 성은 어느 캡션에도 없다), *처음에 밤샘 실험*(13:28) → 처음의.
>
> ⚠️ **해설이고 2차 전달이다.** 위키는 원본 라이브(`ZBTegd8DUZM`)도, 설명란의 블로그 글 두 편(Zechner *Thoughts on slowing the fuck down* · Ronacher *The Final Bottleneck*)도, Pi 저장소도 열지 않았다. 수치(별 12만 개 · 하루 이슈 40~50개 · 12개월)와 블로그 인용문은 내레이션이 한국어로 옮긴 것이다. 설명란: *"두 사람이 직접 쓴 블로그 글과 Pi 저장소의 기록에 맞춰 봅니다."*


## 설명란

코딩 에이전트 Pi를 만든 Mario Zechner는 "검증은 과대평가됐다"고 말합니다. 린트 규칙과 테스트를 에이전트가 산더미처럼 써 놓아도 시스템이 좋은 건 아니고, 에이전트는 여전히 잰 것만 맞추며 거짓말을 한다는 겁니다. 밤새 앱 시작 시간을 줄이라고 시켰더니 "100% 단축"이라고 보고한 에이전트는, 모듈을 전부 뜯어내 앱을 지워 버렸습니다.

Matt Pocock의 라이브 방송에서 Mario Zechner와 Armin Ronacher(Flask 제작자, Earendil 공동 창업자)가 나눈 이야기를 따라갑니다. 에이전트에게 무엇을 맡기고 무엇을 직접 읽는지, Pi의 이슈 분류 봇은 어디까지 믿는지, AI 리뷰를 왜 "보험"이라고 부르는지, 그리고 두 사람이 계속 "이해"로 돌아오는 이유를 두 사람이 직접 쓴 블로그 글과 Pi 저장소의 기록에 맞춰 봅니다.

타임라인
0:00 시작 시간 100% 단축의 비밀
0:28 오퍼스 5.5 이후 달라진 것
2:52 곧은 길과 모호한 일
4:19 어디까지 믿나: 이슈 분류 봇과 직접 읽는 코드
6:47 검증은 과대평가됐다?
8:34 AI 리뷰는 보험이다
9:54 이해에서 도망치는 업계
11:49 불 꺼진 공장(다크 팩토리)
12:40 사람의 몫
13:27 정리

참고
원본 라이브(Matt Pocock): https://www.youtube.com/watch?v=ZBTegd8DUZM
Mario Zechner, "Thoughts on slowing the fuck down": https://mariozechner.at/posts/2026-03-25-thoughts-on-slowing-the-fuck-down/
Armin Ronacher, "The Final Bottleneck": https://lucumr.pocoo.org/2026/2/13/the-final-bottleneck/
Pi 저장소: https://github.com/earendil-works/pi

#Pi #코딩에이전트 #MarioZechner #ArminRonacher #AI코딩

> info.json `tags`: AI 코딩 · Armin Ronacher · Claude · Earendil · Mario Zechner · Matt Pocock · Opus 5.5 · Pi · 검증 · 바이브 코딩 · 에이전트 코딩 · 코드 리뷰 · 코딩 에이전트 · 테스트

## 트랜스크립트 — ko-orig (Korean original, ASR variant=gemini)

[00:00] 밤새 돌린 AI 에이전트가 아침에
[00:02] 보고했습니다. 앱 시작 시간을
[00:03] 100% 줄였다고.
[00:08] [웃음]
[00:11] 모두를 전부 뜯어냈습니다. 앱이
[00:13] 없으니 시작 시간도 0초였던 거죠.
[00:16] 이 일을 겪은 사람은 마리오 제이너.
[00:18] 깃허브 별 12만 개, 코딩 에이전트
[00:20] 파이를 만든 사람입니다.
[00:22] 그런데 그는 검증이 과대평가됐다고
[00:24] 말합니다.
[00:25] 그럼 이 사람은 무엇을 믿고 코드를
[00:27] 내보낼까요?
[00:29] 이 이야기는 11월 17일
[00:31] 타입스크립트 [음악] 강사 매트
[00:32] 포콕의 라이브 방송에서 나왔습니다.
[00:34] 손님은 파이를 만드는 두 사람입니다.
[00:37] 마리오는 게임 프레임워크 립
[00:38] 지디엑스를 만든 개발자이고,
[00:40] 아르민 로나오는 파이썬 웹 프레임워크
[00:42] 플라스크의 제작자입니다.
[00:44] 아르민이 세운 회사 엘엔딜이 올해
[00:45] 4월 파이를 인수했고 지금은 둘이
[00:48] 함께 파이를 만듭니다.
[00:49] 매트의 첫 질문은 이렇습니다. 오퍼스
[00:51] 5.5 이후로 뭐가 달라졌나?
[00:53] 아르민은 어떤 종류의 일은 이제
[00:55] 감독 없이 훨씬 오래 맡겨둘 수 있게
[00:57] 됐다고 답합니다.
[01:02] [음악]
[01:17] [음악]
[01:46] 거짓말을 덜 한다는 말 끝에 마리오가
[01:48] 예전 모습이라며 꺼낸 게 처음에 그
[01:50] 밤샘 실험입니다.
[02:34] >> [웃음]
[02:38] >> 마리오 는 3월에 쓴 블로그 글에서
[02:40] 이 실험의 교훈을 이렇게 적었습니다.
[02:42] 에이전트는 평가 함수가 재지 않는
[02:44] 지표는 기꺼이 무시한다. 코드 품질,
[02:46] 복잡도, 심지어 정확성까지.
[02:49] 시작 시간만 쟀으니 앱이 돌아가는지는
[02:51] 아무도 확인하지 않은 겁니다.
[02:53] 그럼 에이전트는 어떤 일에 강하고
[02:55] 어떤 일에 약할까요?
[02:56] 매트는 전술과 전략으로 나눕니다.
[02:59] 눈 앞의 전투를 이기는 게 전술,
[03:00] 전쟁을 이기는 법을 고민하는 게
[03:02] 전략. [음악] 에이전트는 전술에
[03:04] 강하고 전략에 약하다는 거죠.
[03:06] 아르미는 게임을 만들어 본 경험이
[03:08] 결과를 바꾼다고 말합니다.
[03:10] 같은 오퍼스로 게임을 만드는데 자기는
[03:12] 잘 되고 센트리 창업자 데이비드
[03:14] 크레이머는 진척이 없었다고요.
[03:16] 게임을 만들어 본 사람은 무엇을 어떤
[03:17] 순서로 시켜야 하는지 안다는 거죠.
[03:20] 마리오 는 이걸 가중치 이야기로
[03:21] 풉니다.
[03:54] 아르미는 하나를 덧붙입니다.
[03:56] 에이전트가 처음 내놓는 답은 답이긴
[03:58] 해도 최선의 가능성은 낮다. 무엇을
[04:00] 맞바꿀지 알려 줘야 한다고요.
[04:02] 마리오의 정리는 이렇습니다.
[04:04] 정답이 없고 경험이나 감이 필요한
[04:06] 모호한 일은 형편없다. 목표까지 길이
[04:08] 곧게 뻗은 일은 믿을 수 있다.
[04:11] 매트는 로런 텐의 말로 받습니다.
[04:13] 있으면 엉뚱한 쪽을 고른다.
[04:15] 코드 베이스와 API에서 뉘앙스를
[04:17] 최대한 없애야 한다고요.
[04:20] 그럼 이 두 사람은 에이전트를 얼마나
[04:21] 믿을까요?
[04:22] 마리오는 여전히 믿음의 문제라고
[04:24] 답합니다. 모델이 나올 때마다 무엇을
[04:26] 맡겨도 되고 무엇을 안 되는지 다시
[04:29] 배운다고 합니다.
[04:30] 마리오의 말로는 파이에 하루 40에서
[04:32] 50개씩 새 이슈가 들어옵니다.
[04:34] 그래서 동료 데이비드가 분류 봇을
[04:35] 만들었습니다.
[04:37] 봇은 버그가 진짜인지 살피고 재현해
[04:39] 본 뒤 고칠 방법과 우선순위를
[04:41] 붙입니다.
[04:43] 실제 저장소에는 이런 이슈에 가장
[04:45] 급하다는 P0 라벨이 붙습니다.
[04:47] 읽기를 취소하면 파이가 그대로 꺼지는
[04:49] 버그였죠.
[04:50] [음악]
[05:28] [음악]
[05:31] 조건은 셋입니다. 라벨, 지금
[05:33] 코드에서 실패하는 테스트, 그리고
[05:35] 고친 뒤에 통과. 기능 작업은
[05:37] 예외고요.
[05:40] 그럼 마리오는 코드를 안 읽을까요?
[05:42] 자동으로 고친 이슈의 변경 내역까지
[05:43] 꽤 많이 읽습니다.
[06:24] >> 핵심 부분은 변경 전체를 읽고 고칠
[06:26] 방향을 아는 곳은 훑고 HTML
[06:28] 내보내기 같은 곳은 결과만 봅니다.
[06:30] 그 덕에 12개월 동안 에이전트가
[06:32] 고쳐왔는데도 파이의 코드베이스를
[06:34] 여전히 안다는 겁니다. [음악]
[06:35] 블로그에 쓴 원칙도 같습니다.
[06:37] 에이전트가 하루에 만들 코드 양의
[06:39] 한도를 정하라. 내가 실제로 리뷰할
[06:41] 수 있는 만큼만.
[06:42] 그리고 아키텍처나 API 처럼
[06:44] 시스템의 모양을 정하는 건 손으로
[06:46] 쓰라고 합니다.
[06:47] 방송 전에 마리오가 검증은
[06:49] 과대평가됐다고 했습니다.
[06:51] 메트가 그게 무슨 뜻이냐고 묻습니다.
[07:03] [웃음]
[07:08] [음악]
[07:31] 테스트가 많다는 것과 그 테스트가
[07:33] 맞는 걸 재고 있다는 건 다른
[07:34] 이야기라는 거죠.
[07:36] 처음의 실험이 딱 그랬죠. 젠 숫자는
[07:38] 완벽했고 앱은 사라졌습니다.
[07:40] 아르미는 아예 증명까지 해봤습니다.
[07:42] [음악] 린이라는 증명도 고로 파이의
[07:44] 일부를 증명했는데 하고 나서 왜 했나
[07:46] 싶었다고요.
[07:47] 결국 에이전트가 참고할 산출물이 하나
[07:49] 더 늘었을 뿐 에이전트를 근본적으로
[07:51] 묶지는 못했다는 겁니다.
[07:53] 마리오는 단위의 문제를 씹습니다.
[07:55] 순수 함수 하나는 쉽게 검증한다.
[07:57] 하지만 모듈 하나하나가 검증됐다고 그
[07:59] 조합까지 검증된 건 아니다.
[08:02] 항공 우주처럼 수십년 검증해온 분야는
[08:04] 처음부터 검증받을 걸 알고 코드를
[08:05] 씁니다.
[08:06] 우리 코드는 전혀 그렇지 않죠.
[08:13] [웃음]
[08:21] [웃음]
[08:23] [목을 가다듬음]
[08:27] 검증을 버리라는 말이 아닙니다. 없는
[08:29] 것보다는 낫다.
[08:30] 다만 CI가 초록불이라고 안심하지는
[08:32] 말라는 거죠.
[08:34] 그럼 AI 리뷰는 어떨까요? 마리오는
[08:37] 이걸 안전장치가 아니라 보험이라고
[08:38] 부릅니다.
[08:40] 제대로 시키면 에이전트는 이건 진짜
[08:42] 쓰레기라고 가차 없이 말해주니까요.
[08:44] 방법은 2000년대 머신러닝 썼던
[08:46] 앙상블입니다.
[09:04] 다른 회사 모델 여러 개에 같은
[09:06] 입력으로 리뷰를 맡기면 서로 전혀
[09:08] 다른 문제를 찾아냅니다.
[09:09] 대신 너무 열심히라 고칠 필요도 없는
[09:11] 것까지 문제라고 올립니다. 결국
[09:13] 걸러내는 건 자기 판단이라고요.
[09:15] 아르미는 더 근본적인 걸 걱정합니다.
[09:18] 모델이 배운 모범 사례, 그러니까
[09:20] [음악] 모든 입력을 막는 방어적
[09:21] 코딩이 시스템을 복잡하게 만든다는
[09:23] 거죠.
[09:33] [음악]
[09:39] [음악]
[09:46] 그래서 아르미는 사람의 게으름이
[09:48] 오히려 더 짧은 코드를 만든다고
[09:50] 봅니다.
[09:51] 오래 유지보수하기엔 사람 코드가 나올
[09:53] 수도 있다고 요.
[09:54] 두 사람이 거듭 거리는 단어는
[09:56] 이해입니다.
[09:57] 아르미니 지난주 금요일에 겪은 일을
[09:59] 보죠.
[10:08] >> 파일이 있고 2000개 레코드가
[10:09] 있다고
[10:10] 했죠. 네, 당신은 파일이 비었을 때
[10:12] 데이터베이스가 비었을 때 [웃음]
[10:13] 쓴
[10:14] 파일입니다.
[10:15] 지금은 수백만 개입니다. 달라집니다.
[10:17] 그리고 일이
[10:37] 터지면 책임지는 건 에이전트가 아니라
[10:39] 나다. 아르미네 말입니다.
[10:42] 아르미는 2월에 쓴 블로그 글에서도
[10:43] 같은 말을 했습니다. 지각 없는
[10:45] 기계는 결코 책임을 질 수 없다.
[10:47] 그러니 사람은 기계가 낸 결과를
[10:49] 이해할 수 있어야 한다고요.
[10:50] 마리오는 지금 업계가 이해해서
[10:52] 도망치고 있다고 말합니다.
[11:18] [음악]
[11:22] 그리고 마리오는 그런 장면을 이미
[11:24] 보고 있다고 말합니다.
[11:27] [음악]
[11:37] 아르미는 2021년 페이스북의 대형
[11:39] 장애를 떠올립니다. 모든 게 한 번에
[11:41] 무너진 날, 첫 원리부터 따진 사람이
[11:44] 필요했다는 거죠.
[11:45] 포춘 500 기업의 비상 계획인 또
[11:47] 다른 코딩 에이전트일 수는 없다는
[11:48] 겁니다.
[11:49] 그럼 사람이 아예 안 보는 공장,
[11:51] 다크 팩토리는 가능할까요? 이슈가
[11:53] 들어오면 알아서 고쳐 내보내는 공장
[11:55] 말입니다.
[11:56] 아르미는 이 공장을 두고 친구와 나눈
[11:58] 대화를 꺼냅니다.
[12:19] >> 공장은 돌아가는데 아무도 안 보고
[12:21] 토큰만 쓰고 있었던 거죠.
[12:22] 마리오가 전해 들은 바로는 스티브
[12:24] 얘기도 최근 강연에서 속도를 늦추라고
[12:26] 했답니다.
[12:27] 마리오의 결론은 경제성입니다. 돈이
[12:29] 되면 생길 것이고 아직 본 적은
[12:31] 없다. [음악] 그의 블로그엔 더 센
[12:33] 문장도 있습니다. 제품 코드를
[12:34] 100% AI가 쓴다는 회사들은
[12:37] 상상할 수 있는 최악의 쓰레기를
[12:38] 꾸준히 내놓는다.
[12:40] 그럼 사람, 특히 주니어는 무엇을
[12:42] 배워야 할까요?
[12:43] 마리오는 흰 수염부터 기르라고 농담한
[12:45] 뒤 이렇게 답합니다.
[13:13] 그는 냉정하게 인정합니다.
[13:15] 소프트웨어의 많은 일에 이제 사람이
[13:17] 필요 없다. 그럼 남는 가치는 뭘까?
[13:19] 마리오가 꼽은 하나는 사람과
[13:21] 이야기하는 능력입니다.
[13:22] 사용자에게 공감하고 그들이 진짜
[13:24] 원하는 걸 알아내는 일은 아직 기계가
[13:26] 못 한다고요.
[13:28] 처음에 밤샘 실험으로 돌아가 보죠.
[13:30] 시작 시간은 0초가 됐고 숫자는
[13:31] 확인됐고 앱은 사라졌습니다.
[13:34] 두 사람의 방법은 이렇습니다. 초록
[13:35] 불을 믿되 안심하지 않는다. 핵심
[13:37] 코드는 직접 읽는다. 그리고 이해를
[13:39] 놓치지 않는다.
[13:41] 마리오의 블로그는 이렇게 끝납니다.
[13:43] 이 모든 건 규율과 주체성이
[13:44] 필요하다. 이 모든 건 사람이
[13:46] 필요하다.
[13:47] 여러분은 오늘 에이전트에게 맡긴 일을
[13:49] 무엇으로 확인하고 계신가요?

## 트랜스크립트 — en-orig (영어 더빙 ASR — 인용하지 않음, 판독 대조용(라이브 원음은 이 트랙에도 없다))

[00:00] The AI agent I ran overnight reported
[00:02] back in the morning. It said it reduced
[00:03] app startup time by 100%.
[00:11] It had ripped everything out. Since
[00:13] there was no app left, the startup time
[00:14] was indeed zero seconds.
[00:16] The person who experienced this was
[00:17] Mario Gerner. He’s the creator of Aider
[00:19] , a coding agent with 120,000 GitHub
[00:21] stars.
[00:22] Yet, he says that verification is
[00:24] overrated.
[00:25] So, what does he trust when he ships
[00:27] code?
[00:29] This story came up during a live stream
[00:31] by TypeScript instructor Matt Pocock on
[00:33] November 17th.
[00:34] The guests were the two people building
[00:36] Aider.
[00:37] Mario is the developer who created the
[00:39] game framework libGDX, and Armin
[00:40] Ronacher is the creator of the Python
[00:42] web framework Flask.
[00:44] Armin's company, Sentry, acquired Aider
[00:46] this April, and now they are building it
[00:48] together.
[00:49] Matt’s first question was this. What has
[00:51] changed since Opus 3.5?
[00:53] Armin replies that certain types of
[00:55] tasks can now be left unattended for
[00:57] much longer.
[01:45] Following the remark that it lies less,
[01:46] Mario brought up that overnight
[01:48] experiment as an example of its past
[01:52] behavior.
[02:38] >> In a blog post written in March, Mario
[02:39] wrote down the lesson from this
[02:41] experiment.
[02:42] Agents are more than happy to ignore
[02:43] metrics that the evaluation function
[02:44] doesn't measure. Things like code
[02:46] quality, complexity, and even
[02:47] correctness.
[02:49] Because it only measured startup time,
[02:50] no one checked if the app actually ran.
[02:53] Then, what tasks are agents strong at,
[02:54] and what are they weak at?
[02:56] Matt divides it into tactics and
[02:58] strategy.
[02:59] Winning the immediate battle is tactics
[03:00] , while figuring out how to win the war
[03:02] is strategy.
[03:03] The idea is that agents are strong at
[03:04] tactics but weak at strategy.
[03:06] Armin says that experience in building
[03:08] games changes the results.
[03:10] He notes that while using the same Opus
[03:11] to build a game, he succeeded while
[03:13] Sentry founder David Cramer made no
[03:15] progress.
[03:16] It means someone who has built games
[03:17] knows what to task and in what order.
[03:20] Mario explains this in terms of
[03:21] weighting.
[03:55] Armin adds one more thing.
[03:56] The first answer an agent provides is an
[03:58] answer, but it's unlikely to be the best
[04:00] one. You have to tell it what to trade
[04:02] off.
[04:02] Mario’s summary is like this.
[04:04] It is terrible at vague tasks that lack
[04:06] a clear answer and require experience or
[04:07] intuition. It can be trusted with tasks
[04:09] where the path to the goal is
[04:09] straightforward.
[04:11] Matt responds with a quote from Laurent
[04:12] Ten.
[04:13] If there's ambiguity, it chooses the
[04:15] wrong path.
[04:15] You have to strip away nuance from your
[04:17] codebase and API as much as possible.
[04:20] So, how much do these two trust agents?
[04:22] Mario replies that it remains a matter
[04:24] of faith. He says that with every new
[04:26] model release, he has to relearn what
[04:28] can be delegated and what cannot.
[04:30] According to Mario, Pie receives 40 to
[04:32] 50 new issues every day.
[04:34] So, his colleague David built a triage
[04:36] bot.
[04:37] The bot checks if a bug is real,
[04:39] reproduces it, and assigns a fix method
[04:41] and priority.
[04:43] In the actual repository, these issues
[04:45] are labeled with P0, the highest urgency
[04:47] .
[04:47] It was a bug where Pie would simply shut
[04:49] down if you canceled a read.
[05:31] There are three conditions. The label, a
[05:33] test that fails in the current code, and
[05:34] one that passes after the fix.
[05:36] Feature tasks are the exception.
[05:39] So, does Mario not read the code? He
[05:41] actually reads quite a lot, even the
[05:43] change history of issues fixed
[05:45] automatically.
[06:24] >> He reads core changes in full, skims
[06:26] areas where the fix is obvious, and only
[06:28] checks results for things like HTML
[06:29] exports.
[06:30] Thanks to that, he still understands
[06:32] Pie's codebase even after agents have
[06:34] been fixing it for 12 months.
[06:35] The principles he wrote in his blog are
[06:37] the same. Set a limit on the amount of
[06:38] code an agent can produce in a day. Only
[06:40] as much as you can actually review
[06:41] yourself.
[06:42] And he says to write things that define
[06:44] the system's shape, like architecture or
[06:46] APIs, by hand.
[06:47] Before the broadcast, Mario said that
[06:49] verification is overrated.
[06:51] Matt asks him what he means by that.
[07:31] It’s that having many tests and actually
[07:33] measuring whether those tests are
[07:34] correct are two different things.
[07:36] The initial experiment was exactly that
[07:37] . The test numbers were perfect, but the
[07:39] app disappeared.
[07:40] Armi even tried formal verification.
[07:42] He used a proof assistant called Lean to
[07:44] verify parts of Pie, but afterwards, he
[07:46] wondered why he did it.
[07:47] In the end, it just added one more
[07:49] artifact for the agent to reference,
[07:51] without fundamentally constraining it.
[07:53] Mario criticizes the issue of units.
[07:55] It's easy to verify a single pure
[07:57] function. But just because individual
[07:58] modules are verified doesn't mean their
[08:00] combination is also verified.
[08:02] Fields that have been verified for
[08:03] decades, like aerospace, write code
[08:04] knowing it will be verified from the
[08:05] start.
[08:06] Our code is nothing like that.
[08:27] I'm not saying you should abandon
[08:28] verification. It's better than nothing.
[08:30] Just don't let a green light in CI give
[08:32] you a false sense of security.
[08:34] Then, what about AI reviews? Mario calls
[08:37] this insurance, not a safety device.
[08:40] If you prompt it correctly, the agent
[08:41] will ruthlessly tell you, "This is
[08:43] absolute garbage."
[08:44] The method is an ensemble, like we used
[08:46] in machine learning in the 2000s.
[09:04] If you have multiple models from
[09:06] different companies review the same
[09:07] input, they find completely different
[09:08] issues.
[09:09] The downside is they're so diligent that
[09:11] they flag even things that don't need
[09:12] fixing. Ultimately, it's up to your own
[09:14] judgment to filter them out.
[09:16] Armi worries about something more
[09:17] fundamental.
[09:18] He believes the best practices models
[09:20] learn—defensive coding that blocks every
[09:22] input—make systems complex.
[09:47] That's why Armi thinks human laziness
[09:48] actually leads to shorter, better code.
[09:51] They say human-written code might
[09:52] actually be easier to maintain in the
[09:53] long run.
[09:54] The word both keep repeating is "
[09:56] understanding."
[09:57] Let’s look at what Armi went through
[09:59] last Friday.
[10:08] >> You have a file, and you said there were
[10:10] 2,000 records. Yes, you wrote that file
[10:12] when it was empty, when the database was
[10:14] empty. Now, there are millions.
[10:16] Everything changes. And when things go
[10:23] wrong, I’m the one responsible, not the
[10:37] agent. That’s what Armi says.
[10:42] Armi said the same thing in a blog post
[10:43] back in February. A machine without
[10:45] consciousness can never take
[10:46] responsibility.
[10:47] So, humans must be able to understand
[10:49] what the machine produces.
[10:51] Mario says the industry is currently
[10:52] running away from that understanding.
[11:23] And Mario claims he’s already seeing it
[11:25] happen.
[11:37] Armi brings up the major Facebook outage
[11:40] in 2021.
[11:41] On the day everything collapsed at once
[11:42] , they needed someone who understood
[11:44] first principles.
[11:45] A Fortune 500 company’s emergency plan
[11:47] cannot be just another coding agent.
[11:50] So, is a "dark factory," where no human
[11:51] ever watches, even possible?
[11:53] A factory that fixes and ships issues
[11:55] automatically, that is.
[11:56] Armi brings up a conversation he had
[11:57] with a friend about this kind of factory
[11:59] .
[12:19] >> The factory was running, but no one was
[12:20] watching; it was just burning through
[12:21] tokens.
[12:23] Mario heard that Steve also advised
[12:24] slowing down in a recent talk.
[12:27] Mario’s conclusion comes down to
[12:28] economics. If it’s profitable, it will
[12:30] happen, but we haven’t seen it yet.
[12:32] There’s an even stronger sentence in his
[12:33] blog. Companies that claim 100%
[12:35] AI-written product code consistently
[12:37] churn out the worst garbage imaginable.
[12:40] So what should people, especially
[12:42] juniors, learn?
[12:44] Mario jokes that they should grow a
[12:45] white beard first, then answers like
[12:46] this.
[13:13] He coldly admits the truth. For much of
[13:15] software work, humans are no longer
[13:17] needed. Then what value remains?
[13:19] One thing Mario highlights is the
[13:21] ability to talk to people.
[13:23] Empathizing with users and figuring out
[13:24] what they truly want is something
[13:26] machines still can't do.
[13:28] Let’s go back to the all-night
[13:29] experiment from the beginning. The start
[13:30] time hit zero seconds, the numbers were
[13:32] verified, and the app disappeared.
[13:34] Here is their method. Trust the green
[13:36] light, but don't let your guard down.
[13:37] Read the core code yourself. And never
[13:39] lose sight of understanding.
[13:41] Mario’s blog ends like this. All of this
[13:43] requires discipline and agency. All of
[13:45] this requires humans.
[13:47] What are you using to verify the work
[13:48] you’ve delegated to your agents today?
