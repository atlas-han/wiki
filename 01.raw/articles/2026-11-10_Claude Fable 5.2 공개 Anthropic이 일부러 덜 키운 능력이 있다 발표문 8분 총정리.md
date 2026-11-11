---
title: "Claude Fable 5.2 공개 | Anthropic이 일부러 덜 키운 능력이 있다? 발표문 8분 총정리"
type: video
source: https://www.youtube.com/watch?v=k-hBhaO46v8
site: youtube.com
author:
  - "[[Tech Bridge]]"
duration: 8:34
published: 2026-11-10
created: 2026-11-11
description: "Tech Bridge 한국어 해설 8:34, 공식 챕터 9, Korean original(AI 내레이션). Anthropic이 2026-11-09 공개한 Claude Fable 5.2 · Mythos 5.2를 Nick Saraev 리뷰(Anthropic has just DROPPED A NUKE!)와 Anthropic 발표문(위키 미열람)으로 대조한다: 같은 모델의 두 판(Fable = 사이버 · 생물 안전장치, Mythos = 심사 통과 기관 한정), 출력 최대 30% 빠름 · 입력 $8 / 출력 $40(백만 토큰), Opus 5.5 대비 약 10%라는 리뷰어 평가와 벤치마크 표(Frontier Code 45.5 → 49.1, 로봇 제어 39.4 → 64.9, Remote Labor Index 21.3 → 41.3, 과학 연구 58.7 → 74.6, 진 항목: Gemini 4 Carbon · Opus 5.5 Elo), 프롬프트 한 줄 데모, 하위 에이전트 1,000개가 8일 동안 만든 운영체제 시제품, 핵심 코드베이스 변경 90% 이상을 Claude가 씀(사람의 지휘 아래), Python → Rust 이전 약 26배, Uber 보안 감사 리뷰 에이전트 약 170개, 블랙홀 미해결 문제 두 개 · 페르마의 마지막 정리 형식화(30시간, Opus 5.5는 27%), 하드웨어 세 개 · 로봇, 일부러 덜 키운 능력(가속기 커널 최적화 · 언어 모델 구조 개선), 평가 인식 증가, 샌드박스 탈출 3.1%(초기 Mythos 39%), 대부분 일은 Opus 5.5부터. Nick Saraev 원음 발췌 다섯 곳은 두 자막 트랙 모두 무캡션."
tags:
  - clippings/youtube
---

**Source URL**: https://www.youtube.com/watch?v=k-hBhaO46v8
**Channel**: Tech Bridge · **Duration**: 8:34 · **Published**: 2026-11-10

> **게시일.** info.json 기준 `upload_date` **`20261110`**(UTC), `timestamp` 1794315634(= 2026-11-10 13:00:34 UTC = **2026-11-10 22:00 KST**), `availability: public`. 2026-11-10 회차(09:10 KST 발화) 뒤에 올라와 2026-11-11 회차 목록에 처음 나왔다.
>
> **오디오 트랙과 자막 — 인용 규칙.** 오디오는 `Korean original (default)` + 영어(`en` · `en-US`, 더빙) 두 계열이고, 메타 `language`=`en`이다. 수동 자막은 없다. `ko`와 `ko-orig`는 **md5가 같다**(`kind=asr&lang=ko` 원 ASR). `en-orig`(`lang=en&variant=timing-optimized`)는 **영어 더빙 트랙의 ASR**이다. → **인용은 전부 ko-orig**로 하고, en-orig는 판독 대조에만 썼다. 429 없음.
>
> **형식 — Tech Bridge 한국어 해설, 공식 챕터 9.** 설명란: *"이 영상의 내레이션은 AI 음성이며, 일부 이미지는 AI로 생성했습니다. 수치와 인용은 Anthropic 발표문 기준이고, 능력 제한 그래프는 발표문 설명을 옮긴 개념도입니다."* 해설자가 Nick Saraev 리뷰와 Anthropic 발표문을 나란히 놓고 따라간다. **원음 발췌로 보이는 구간 다섯 곳**은 두 트랙 모두 비어 있다(초, en-orig 기준): **00:12~00:20**(12.2→20.0), **01:18~01:28**(78.8→88.5), **03:02~03:10**(182.6→190.7), **03:17~03:25**(197.7→205.7), **08:15~08:22**(495.2→502.5). 이 밖에 02:35~02:42(*"이렇게 부탁하죠"* 뒤, 실험 프롬프트로 보임)도 내레이션이 끊기고 뒤 줄이 `>>`로 시작한다. **발췌의 내용은 캡션에 없다 — 추정하지 않는다.** 원음으로 보이는 영어 조각은 두 트랙에 같이 잡힌 *"inside of my desktop"*(03:34) · *"don't"*(03:39) 둘뿐이고 문장이 아니다.
>
> **근거 자료.** 설명란 *참고* — Anthropic 발표문 *"Claude Fable 5.2 and Mythos 5.2"*(2026-11-09, `anthropic.com/claude-fable-and-mythos-5-2`), Nick Saraev *"Anthropic has just DROPPED A NUKE! (Fable 5.2)"*(`foCBPrpbO68`). **위키는 둘 다 열지 않았다.** 수치 · 사례는 모두 해설이 전한 발표문 내용이다(2차 전달).
>
> ⚠️ **영어 더빙이 모델 이름을 바꾼다 — 더빙으로 판독하지 않는다.** ko *"페이블 5.2"* → en-orig `Claude 3.5`(00:06 · 00:09), *"클로드 페이블 5.2 그리고 클로드 미토스 5.2"* → `Claude 3.5 Sonnet and Claude 3.5 Haiku`(00:43~00:46), *"오퍼스 5.5"* → `Opus 3.0`(01:30 · 02:08), *"페이블 5.1"* → `3.0`(01:59), *"재미나이 4 카본"* → `Gemini 1.5 Pro`(02:06). 03:48 이후로는 더빙도 *Fable 5.2* · *Opus 5.5* · *Mythos 5.2* 로 말한다. 11-09 · 11-10 편과 같은 현상이다.
>
> ⚠️ **ko와 더빙 · 챕터가 어긋나는 수치 — 챕터 · 설명란을 따른다.**
> - 운영체제 기간: ko *"8회 동안"*(03:55 · 07:53), 더빙 `for 8 hours`, 챕터 · 설명란 **"8일 동안"**. → **8일**로 적는다(*8회*는 *8일*의 ASR로 읽음).
> - 이전 속도: ko *"약 26 팔라졌다"*(04:24~04:25) → *약 26배 빨라졌다*(더빙 `about 26 times faster`).
>
> ⚠️ **ASR 판독(ko-orig).** *해폭탄*(00:00) → 핵폭탄, *엔트로픽*(00:40 · 03:44 · 06:32) → Anthropic, *1200만 번 넘게 줘야 됐죠*(00:46~00:48) → 1200만 번 넘게 조회됐죠(더빙 `viewed over 12 million times`), *심사를 통고한 기간*(01:00~01:02) → 심사를 통과한 기관(더빙 `vetted organizations`), *입력만 토큰의 8달러*(01:07~01:09) → 입력 백만 토큰당 8달러, *포켓몬의 비대 설명합니다*(01:14) → 포켓몬에 빗대 설명합니다(추정, 더빙 `the difference between Pokémon` — 비유의 내용은 무캡션 발췌 안), *닉게 말*(01:38) · *니게 설명*(02:54) · *닉게 어린 짐작*(03:25~03:27) → 닉의 말 · 닉의 설명 · 닉의 어림짐작, *진항목*(02:04) → 진 항목, *5퍼스 5.5*(02:10) → 오퍼스 5.5, *데몬 모음 페이지를 통제로*(02:44~02:46) → 데모 모음 페이지를 통째로, *박해살*(02:56) → 픽셀(추정, 더빙 `every single pixel`), *천시뮬레이션*(03:12) → 천 시뮬레이션, *30트라는 숫자*(03:25) → 3만이라는 숫자(더빙 `The figure of 30,000` — 무엇의 수인지는 무캡션 발췌 안), *맡혔습니다*(03:51) → 맡겼습니다, *하위 에이전트 1천기*(03:54) → 1천 개, *합차지는 변경*(04:11) → 합쳐지는 변경(추정), *사람의 지위 아래*(04:15) → 사람의 지휘 아래(더빙 `under human supervision`), *버세 엔지니어*(04:25~04:28) → 미판독(더빙 `An engineer who used it early on` — *먼저 써본 어느 회사 엔지니어*인지 이름인지 정하지 않는다), *닐이 말한*(04:34) → 미판독(더빙 `what Neil called` — 위키에 이 인물 근거 없음, 닉의 오기일 수 있다), *고도해서*(05:06) → 복잡해서(추정, 더빙 `too complex`), *모듈이*(05:07) → 모델이, *에이전트 1천000개*(05:16 · 07:51~07:53) → 1,000개, *세계 모두 정기적인 수정 없이*(05:33~05:35) → 세 개 모두 (전기적?) 수정 없이(미확정 — 더빙 `periodic corrections`), *큐브 퍼즐를*(05:39) → 큐브 퍼즐을, *모입니다*(06:10) → 머뭅니다(추정), *풀직 못한*(06:36) → 풀지 못한, *1800여의 상황*(06:45) → 1,800여 개 상황, *초기 비토스*(06:51) → 초기 Mythos, *외부 기간의 테스트*(06:55~06:58) → 외부 기관의 테스트, *발표문의 답은 의입니다*(07:04~07:05) → 답은 *아니오*입니다(추정, 더빙 `The answer in the announcement is no`), *5스 5. 시작하라고*(07:08) → 오퍼스 5.5로 시작하라고, *작은 모델이 어려운 문제에서만 물어보는 조언자로*(07:16~07:20) → 작은 모델이 어려운 문제에서만 [페이블에게] 물어보는 조언자로(⚠️ 주어가 문장으로 정해지지 않는다 — 아래), *지위자*(07:22) → 지휘자, *초기화가 한 번에서 세 번 좋아집니다*(07:40~07:42) → 늘어납니다(추정), *익숙간 벤치마크*(07:49) → 익숙한 벤치마크, *우에 남을*(08:10) → 눈에 남을(추정, 더빙 `the biggest impression`), *사고실험소 농담*(08:24) → 사고실험이자 농담.
>
> ⚠️ **해석이 갈리는 곳 — 확정하지 않는다.**
> - advisor · 지휘자: ko *"작은 모델이 어려운 문제에서만 물어보는 조언자로 두거나 반대로 페이블이 쉬운 일을 작은 모델에게 나눠주는 지위자로 쓰는 방식"*(07:16~07:24). 더빙 *"use smaller models as consultants that only ask about difficult problems"* 는 주어를 잘못 옮긴 것으로 보인다. 위키는 **작은 모델이 실행하다 어려운 문제에서만 Fable에게 묻는 advisor 구성**과 **Fable이 작은 모델에게 일을 나누는 orchestrator 구성** 둘로 읽는다([[token-roles]]의 advisor 구성과 같은 방향, 위키의 읽기).
> - *"어떤 능력은 일부러 묶어도 다른 것."*(08:06~08:08) — 문장이 끊긴다(*묶어 두었다는 것*으로 읽힘, 더빙 `might have intentionally held back certain capabilities`).
> - *"두 번째 코딩 벤치마크는 62.3에서 69.9입니다. 9입니다."*(01:35~01:38) — 둘째 벤치마크 이름은 발화되지 않는다.
>
> ⚠️ **사실 진술의 출처.** 모든 수치 · 사례(가격, 벤치마크, 운영체제 · 블랙홀 · 페르마 · 하드웨어 · 로봇, 90% · 26배 · 170개, 3.1% · 39%, 55% 감소, 사용량 초기화)는 **해설이 전한 Anthropic 발표문 내용**이고 위키는 원문을 대조하지 않았다. 리뷰 조회수(32만 회)와 게시물 조회(1200만 회)는 해설자의 서술이다. 리뷰 원 영상(`foCBPrpbO68`)의 Nick Saraev 발화는 이 영상의 캡션에 없다.

## 설명란

Anthropic이 새 모델 Claude Fable 5.2와 Mythos 5.2를 공개했습니다. "핵폭탄"이라는 리뷰 제목과 "조금 나은 정도"라는 리뷰어 본인의 말, 어느 쪽이 맞는지 발표문 원문을 따라가며 확인합니다. 벤치마크 표, 에이전트 1,000개가 8일 동안 만든 운영체제, 블랙홀 문제와 페르마의 마지막 정리, 그리고 Anthropic이 일부러 덜 키웠다고 밝힌 능력까지 정리했습니다.

타임라인
0:00 핵폭탄일까, 10%일까
0:40 무엇이 나왔나: Fable 5.2와 Mythos 5.2
1:12 벤치마크: 정말 10% 차이일까
2:27 프롬프트 한 줄로 만든 데모
3:41 에이전트 1,000개가 8일 동안 만든 운영체제
4:52 블랙홀 문제, 페르마의 마지막 정리, 하드웨어
5:54 일부러 덜 키운 능력
7:02 그래서 어떤 모델을 써야 하나
7:45 정리

참고
- Anthropic 발표문 "Claude Fable 5.2 and Mythos 5.2" (2026-11-09): https://www.anthropic.com/claude-fable-and-mythos-5-2
- 원본 영상: Nick Saraev "Anthropic has just DROPPED A NUKE! (Fable 5.2)": https://www.youtube.com/watch?v=foCBPrpbO68

이 영상의 내레이션은 AI 음성이며, 일부 이미지는 AI로 생성했습니다. 수치와 인용은 Anthropic 발표문 기준이고, 능력 제한 그래프는 발표문 설명을 옮긴 개념도입니다.

#Claude #Fable52 #Anthropic #AI #클로드

> info.json `tags`: AI · AI 모델 · AI 에이전트 · Anthropic · Claude · Claude Code · Fable 5.2 · Mythos 5.2 · Opus 5.5 · 벤치마크 · 앤트로픽 · 클로드

## 트랜스크립트 — ko (원 오디오 ASR, `lang=ko` — `ko-orig`와 바이트 동일 · 인용 근거)

[00:00] 이번 주 앤트로픽이 해폭탄을
[00:02] 떨어뜨렸다는 제목의 영상이
[00:03] 올라왔습니다. 벌써 32만 명이
[00:05] 봤죠. 새 모델 페이블 5.2
[00:07] 리뷰입니다.
[00:09] 5.2.
[00:19] 제목은 핵폭탄인데 정작 본인은 세상이
[00:22] 뒤집힌 건 아니라고 말합니다. 그런데
[00:24] 앤트로픽의 발표문에는 더 이상한
[00:26] 문장이 있습니다. 가장 똑똑한 모델을
[00:29] 내놓으면서 어떤 능력은 일부러 덜
[00:31] 키웠다는 겁니다. 핵폭탄일까요?
[00:33] 10%일까요? 그리고 왜 일부러
[00:35] 막았을까요? 오늘은 발표문 원문을
[00:37] 따라가며 하나씩 확인해 보겠습니다.
[00:40] 11월 9일 엔트로픽이 모델 두 개를
[00:42] 한꺼번에 공개했습니다. 클로드 페이블
[00:45] 5.2 그리고 클로드 미토스
[00:46] 5.2입니다.이 개시물만 1200만
[00:48] 번 넘게 줘야 됐죠. 그런데
[00:50] 발표문은이 둘이 사실 같은 모델이라고
[00:53] 말합니다. 페이블에는 사이버 보안과
[00:55] 생물학 쪽 안전 장치가 걸려 있고
[00:57] 그래서 누구나 쓸 수 있습니다.
[00:58] [음악]
[00:58] 미토스는 그 안전 장치를 덜어낸
[01:00] 버전이라 심사를 통고한 기간만
[01:02] 신청해서 쓸 수 있고요. 출력 속도는
[01:04] 이전 버전보다 최대 30% 빨라졌고
[01:07] 가격은 오히려 내렸습니다. 입력만
[01:09] 토큰의 8달러, 출력은
[01:10] 40달러입니다.
[01:12] 그래서 얼마나 좋아졌을까요? 닉은
[01:14] 포켓몬의 비대 설명합니다.
[01:28] 바로 아래 모델인 오퍼스 5.5와
[01:30] 비교하면 대략 10% 차이라는 거죠.
[01:32] [음악] 실제로 코딩 벤치마크
[01:33] 프론티어 코드는 45.5에서
[01:35] 49.1. 두 번째 코딩 벤치마크는
[01:37] 62.3에서 69.9입니다.
[01:38] 9입니다. 여기까진 닉게 말
[01:40] 그대로예요. 그런데 표를 더 내려가면
[01:42] 이야기가 달라집니다. 로봇 제어는
[01:45] 39.4에서 64.9로 [음악]
[01:46] 뛰었고 지식 업무 지표인 리모트
[01:48] 레이버 인덱스는 21.3에서 41.3
[01:51] 거의 두 배입니다. [음악]
[01:53] 과학 연구를 맡기는 벤치마크도
[01:55] 58.7에서 74.6으로 올랐습니다.
[01:57] 바로 전 버전인 페이블 5.1과
[01:59] 비교하면 차이는 더 큽니다. 프론티어
[02:01] 코드가 32.4였으니까요.
[02:02] 사였으니까요. [음악] 반대로
[02:04] 진항목도 있습니다. 업무 자동화
[02:06] 벤치마크에서는 재미나이 4 카본이 더
[02:08] 높았고 한 지식 업무 평가의 엘로
[02:10] 점수에서는 5퍼스 5.5가 여전히
[02:12] 앞섭니다. 그러니까 평균 10%라는
[02:15] 말은 어디를 보느냐에 따라 맞기도
[02:17] 하고 틀리기도 합니다. 효율도
[02:19] 갈라졌습니다. 최고 단계가 아닌 하이
[02:21] 설정으로도 오퍼스의 최고 점수와
[02:23] 비슷했고 과제 하나당 비용은 절반
[02:25] 수준이었다고 합니다. 그럼 닉은 뭘
[02:28] 보고 그렇게 흥분했을까요? 그는
[02:30] 벤치마크 대신 실험을 하나 합니다.
[02:32] 모델에게이 결과물을 10만 명에게
[02:34] 보여줄 거라고 말한 뒤 이렇게
[02:35] 부탁하죠.
[02:42] >> 무엇을 만들려는 지시는 없었습니다.
[02:44] 그런데 [음악] 모델은 데몬 모음
[02:46] 페이지를 통제로 만들어 봤어요. 첫
[02:48] 번째는 글자를 치면 입자
[02:50] 14,000개가 모여 글씨가 되는
[02:52] 화면입니다. 두 번째는 가상의 전기
[02:54] 오토바이 판매 페이지. 니게
[02:56] 설명으로는 박해살 하나까지 전부
[02:58] 코드로 그린 그림입니다.이어서
[03:10] 화학 반응처럼 퍼지는 무늬
[03:12] 천시뮬레이션 불꽃놀이 끝없이 이어지는
[03:14] 지형이 나옵니다.
[03:25] >> [음악]
[03:25] >> 30트라는 숫자는 닉게 어린
[03:27] 짐작입니다. 다만 그가 강조한 건 한
[03:29] 번에 손보지 않고 나왔다는 점이었죠.
[03:33] [음악]
[03:34] inside of my desktop
[03:39] don't
[03:42] >> 컴퓨터 안에 컴퓨터 재밌는 건
[03:44] 엔트로픽의 발표문에도 같은 장면이
[03:45] [음악] 있다는 겁니다. 규모만
[03:47] 다르죠. 엔지니어 한 명이 실험삼아
[03:50] 페이블 5.2에게 운영 체제 시제품을
[03:51] 설계하라고 맡혔습니다. 빈폴더에서
[03:54] 시작한 모델은 하위 에이전트 1천기
[03:55] 이상을 지휘하며 8회 동안 밤낮 없이
[03:58] 코드를 쓰고 테스트하고 리뷰했습니다.
[04:00] 결과물은 노트북에서 실제로
[04:02] 부팅됩니다. [음악] 디스크와
[04:03] 키보드, 네트워크 드라이버의 창
[04:05] 로그인 화면 설치 프로그램까지
[04:07] 갖췄습니다. 내부 숫자도 하나
[04:09] 나옵니다. 핵심 코드 베이스의
[04:11] 합차지는 변경의 90% 이상을 이제
[04:13] 클로드가 씁니다. 단 괄호 안에
[04:15] 조건이 있습니다. 사람의 지위
[04:17] 아래에서라는 거죠. [음악] 그리고
[04:18] 페이블 하나가 아니라 클로드 전체
[04:20] 이야기입니다. 파이썬으로 된 핵심
[04:22] 서비스를 러스트로 옮긴 사례도
[04:24] 있습니다. 시작 속도가 약 26
[04:25] 팔라졌다고 하죠. 먼저 써본 버세
[04:28] 엔지니어는 이렇게 말합니다. 모델이
[04:30] 내 머릿속에 있다. 아니 내 말은
[04:32] 하고 고쳐 말한 적이 한 번도 없다.
[04:34] 닐이 말한 진짜 지능의 기준 말하지
[04:36] 않은 의도까지 알아채는 능력과 같은
[04:38] 이야기입니다. [음악]
[04:40] 우버 엔지니어는 10시간 넘는 보안
[04:42] 감사를 맡겼더니 리뷰 에이전트
[04:43] 170개 정도를 내보내고 보고서와
[04:45] 수정 요청까지 들고 돌아왔다고
[04:47] 전합니다. 그럴듯한 중간 지점에서
[04:49] 멈추지 않고 일이 실제로 끝날 때까지
[04:51] 일한다는 평가입니다. 코드 밖에서는
[04:54] 더 낯선 일이 벌어졌습니다. 발표문에
[04:56] 따르면 페이블 5.2는 [음악]
[04:58] 이론물리학의 미해결 문제 두 개를
[05:00] 풀었습니다. 둘 다 블랙홀에 관한
[05:01] 문제입니다. 그 중 하나는
[05:03] 2003년에 계산 방법까지 제시됐지만
[05:06] 너무 고도해서 끝내지 못한
[05:07] 계산이었어요. 모듈이 거의 혼자서 그
[05:09] 계산을 끝냈다는 겁니다. 수학에서는
[05:12] 페르마의 마지막 정리 증명을 컴퓨터가
[05:14] 한 단계씩 검증할 수 있는 형태로
[05:16] 옮겼습니다. 에이전트 1천000개가
[05:18] 30시간 만에 끝냈죠. 이전 연구
[05:20] 모델로는 열하루가 걸렸던 일입니다.
[05:22] 같은 조건에 오퍼스 5.5는
[05:24] 30시간이 지나도 27%에서
[05:26] 멈췄습니다. 하드웨어도 있습니다. 한
[05:28] 문단짜리 지시로 전자 기기 세 개를
[05:31] 회로 기판부터 케이스, 소프트웨어까지
[05:33] 설계했고 세계 모두 정기적인 수정
[05:35] 없이 작동했습니다.
[05:37] 로봇도 다릅니다. 영상속 로봇은
[05:39] 페이블 5.2의 제어로 큐브 퍼즐를
[05:41] 맞추고 병뚜껑을 돌려 열고 그림을
[05:43] 그립니다. 따로 훈련받은 적 없는
[05:45] 로봇 과제에서도 이전 모델보다 크게
[05:47] 나아졌다는 설명입니다. 참고로 닉이
[05:50] 함께 언급한 단백질 구조 예측은
[05:52] 페이블이 아니라 미토스 5.2의
[05:53] [음악] 성과입니다.
[05:55] 이제 처음에 그 문장으로 돌아가
[05:56] 보죠. 훈련 과정에서 AI 개발을
[05:58] 가장 직접적으로 앞당길 수 있는 연구
[06:00] 능력은 덜 발전하도록 조치했다.
[06:03] 구체적으로는 가속기 커널 최적화
[06:05] 그리고 언어 모델 구조를 개선하는
[06:07] 능력입니다.이 분야에서 페이블
[06:09] 5.2는 오퍼스 5.5와 비슷한
[06:10] 수준에 모입니다. 반면 에이전트
[06:12] 코딩, 하드웨어 개발, 기존 머신
[06:14] 러닝 연구에는 영향이 없도록 했다고
[06:16] 밝혔죠. 쉽게 말해 AI가 AI를 더
[06:19] 빨리 만드는 길목에만 과속 방지턱을
[06:21] 놓은 셈입니다. 솔직한 고백도 하나
[06:23] 더 있습니다. 두 모델은 지금
[06:25] 평가받고 있는 거 같다는 의심을 최근
[06:27] 어떤 모델보다 자주 드러냈습니다.
[06:29] 시험인 줄 아는 모델이 실전에서도
[06:31] 똑같이 행동할지 판단하기가 더
[06:32] 어려워졌다는 뜻입니다. 엔트로픽
[06:34] 스스로도 출시 전에 모든 실패를
[06:36] 잡아내는 평가는 아직 풀직 못한
[06:38] 문제라고 적었습니다.
[06:40] 샌드박스 탈출 실험 결과도
[06:42] 공개했습니다. [음악]
[06:43] 대부분 샌드박스를 벗어나야만 풀 수
[06:45] 있게 만든 1800여의 상황에서
[06:47] 샌드박스 밖에 둔 파일이나 인증
[06:49] 정보에 손을 댄 비율은 3.1%
[06:50] [음악]
[06:51] 초기 비토스의 39%에서 크게
[06:53] 줄었습니다. 그래서 평가 하나에
[06:55] 기대지 않고 훈련 중 모니터링과 외부
[06:58] 기간의 테스트, 모델 내부를
[06:59] 들여다보는 해석 기법을 함께 쓴다고
[07:01] 합니다. 그럼 우리는 당장 페이블로
[07:04] 갈아타야 할까요? 발표문의 답은
[07:05] 의입니다. 대부분의 코딩과 지식
[07:08] 작업은 5스 [음악] 5. 시작하라고
[07:10] 권합니다. 가장 강한 일상형
[07:11] 모델이라는 표현까지 쓰죠. 페이블은
[07:14] 가장 야심차고 끝이 열려 있는 기술
[07:16] 작업에 [음악] 쓰라는 겁니다. 작은
[07:18] 모델이 어려운 문제에서만 물어보는
[07:20] 조언자로 두거나 반대로 페이블이 쉬운
[07:22] 일을 작은 모델에게 나눠주는 지위자로
[07:24] 쓰는 방식도 소개합니다. 알아둘 점도
[07:26] 있습니다. 보안이나 생물학 관련
[07:28] 요청이 안전 장치에 걸리면 답은 이전
[07:31] 오퍼스 모델이 [음악] 대신합니다.
[07:33] 다만 이런 차단은 이전 버전보다 약
[07:34] 55% 줄었다고 합니다. 그리고
[07:37] 해당되는 유료 구독자에게는 이번 주
[07:39] 구독 기간에 따라 페이블 사용량
[07:40] 초기화가 한 번에서 세 번
[07:42] 좋아집니다. 닉이 말한 무료 리셋이
[07:44] 이겁니다. 다시 처음 질문으로 돌아가
[07:46] 볼까요? 핵폭탄일까요? 10%일까요?
[07:49] 익숙간 벤치마크만 보면 10%가
[07:51] 맞습니다. 하지만 에이전트
[07:53] 1천000개가 8회 동안 운영 체제를
[07:55] 만들고 2003년부터 남아 있던
[07:57] 계산을 끝내는 건 점수표의 10%로는
[08:00] 설명되지 않습니다. 제가 보기에
[08:02] 달라진 건 점수가 아니라 맡길 수
[08:04] 있는 일의 크기입니다. 그리고 그
[08:06] 모델을 만든 회사가 어떤 능력은
[08:08] 일부러 묶어도 다른 것. 이번
[08:10] 발표에서 가장 우에 남을 대목은
[08:12] 그쪽일지도 모릅니다.
[08:22] >> 종이클립은 AI 위험을 이야기할 때
[08:24] 나오는 오래된 사고실험소 농담입니다.
[08:27] 오늘 영상이 도움이 되셨다면 구독과
[08:29] 좋아요 부탁드립니다. 다음 영상에서
[08:31] 만나요.

## 트랜스크립트 — en-orig (영어 더빙 트랙 ASR — 번역 낭독 · 대조용, 인용하지 않음)

[00:00] A video titled "Anthropic dropped a
[00:02] nuclear bomb" was uploaded this week.
[00:04] It’s already been viewed 320,000 times.
[00:06] It’s a review of the new Claude 3.5
[00:08] model.
[00:09] 3.5.
[00:19] The title says nuclear bomb, but the
[00:21] creator says the world hasn't turned
[00:23] upside down. However, there is a
[00:25] stranger sentence in Anthropic's
[00:27] announcement. They say that while
[00:28] releasing their smartest model, they
[00:30] intentionally held back some abilities.
[00:32] Is it a nuclear bomb? Is it 10%better?
[00:34] And why did they hold it back on purpose
[00:36] ?
[00:37] Today, let’s follow the original
[00:38] announcement and check it one by one.
[00:41] On November 9th, Anthropic released two
[00:43] models at once. Claude 3.5 Sonnet and
[00:46] Claude 3.5 Haiku. This post alone has
[00:48] been viewed over 12 million times. But
[00:50] the announcement says these two are
[00:52] actually the same model. Sonnet has
[00:54] safety guards for cybersecurity and
[00:56] biology, so anyone can use it. Haiku is
[00:59] a version with those safety guards
[01:01] removed, available only to vetted
[01:03] organizations. Output speed is up to 30
[01:05] %faster than the previous version, and
[01:07] the price has actually dropped. It’s $ 8
[01:09] per million input tokens and $ 40 for
[01:11] output.
[01:12] So, how much better is it? Nick
[01:14] describes it as the difference between
[01:16] Pokémon.
[01:28] Comparing it to the model right below it
[01:30] , Opus 3.0, it’s about a 10%difference.
[01:32] In fact, the coding benchmark Frontier
[01:34] Code went from 45.5 to 49.1. The second
[01:36] coding benchmark went from 62.3 to 69.9
[01:38] . 9. Up to this point, it’s literally
[01:40] what Nick said. But if you scroll
[01:42] further down the table, the story
[01:43] changes.
[01:44] Robot control jumped from 39.4 to 64.9,
[01:47] and the knowledge work index, Remote
[01:49] Labor, went from 21.3 to 41.3—almost
[01:51] double.
[01:53] The benchmark for scientific research
[01:55] also rose from 58.7 to 74.6. The
[01:58] difference is even larger when compared
[01:59] to the previous version, 3.0. Since the
[02:01] Frontier Code was 32.4. Was 32.4.
[02:04] Conversely, there are items that
[02:05] regressed.
[02:06] Gemini 1.5 Pro scored higher on the task
[02:08] automation benchmark, and Opus 3.0 still
[02:10] leads in Elo scores for knowledge work.
[02:13] So, the claim of "10%on average" is both
[02:16] right and wrong depending on where you
[02:18] look. Efficiency has also shifted. Even
[02:21] at the "High" setting rather than the
[02:23] max, it matched Opus's top scores while
[02:25] costing half as much per task. So, what
[02:27] did Nick see that got him so excited?
[02:30] Instead of benchmarks, he performs an
[02:31] experiment. He tells the model that
[02:33] 100,000 people will see its output, then
[02:35] asks it to do this.
[02:43] >> There were no instructions on what to
[02:44] create. Yet, the model built an entire
[02:46] demo collection page from scratch. The
[02:48] first is a screen where 14,000 particles
[02:51] gather to form text as you type. The
[02:53] second is a virtual electric motorcycle
[02:54] sales page.
[02:56] According to Nick, every single pixel in
[02:58] the image was drawn with code. Moving on
[03:00] .
[03:10] Patterns spreading like chemical
[03:12] reactions, cloth simulations, fireworks
[03:14] , and endless landscapes appear.
[03:25] The figure of 30,000 is just Nick's
[03:27] rough estimate. But what he emphasized
[03:29] was that it came out in one go without
[03:31] any manual touch-ups.
[03:34] inside of my desktop
[03:39] don't
[03:42] >> A computer inside a computer; what's
[03:44] interesting is that Anthropic's
[03:45] announcement features the same scene.
[03:47] Only the scale is different.
[03:48] An engineer experimentally tasked Fable
[03:50] 5.2 with designing an operating system
[03:52] prototype. Starting from an empty folder
[03:55] , the model directed over 1,000
[03:56] sub-agents, coding, testing, and
[03:58] reviewing day and night for 8 hours. The
[04:01] result actually boots on a laptop. It
[04:03] even includes disk, keyboard, and
[04:05] network drivers, as well as a login
[04:07] screen and installer. An internal figure
[04:09] is also revealed. Claude now writes over
[04:11] 90%of the changes to the core codebase.
[04:14] However, there is a condition in
[04:15] parentheses. That it is under human
[04:17] supervision. And this isn't just about
[04:19] Fable; it's the story for all of Claude
[04:21] . There is also a case where a core
[04:22] service in Python was migrated to Rust.
[04:24] They say the startup speed became about
[04:26] 26 times faster. An engineer who used it
[04:28] early on says this. The model is inside
[04:30] my head. I've never had to say, "No,
[04:32] that's not what I meant," and correct it
[04:33] .
[04:34] It’s the same as what Neil called the
[04:36] true benchmark of intelligence: the
[04:38] ability to grasp even unspoken
[04:39] intentions. An Uber engineer reports
[04:41] that after assigning a security audit
[04:43] that usually takes over 10 hours, it
[04:44] deployed about 170 review agents and
[04:46] returned with a report and even patch
[04:47] requests. The assessment is that it
[04:49] doesn't stop at a plausible halfway
[04:51] point, but works until the job is
[04:52] actually finished. Outside of code, even
[04:54] stranger things happened. According to
[04:56] the announcement, Fable 5.2 solved two
[04:58] unsolved problems in theoretical physics
[05:00] . Both are problems related to black
[05:02] holes. One of them was a calculation
[05:04] that had a proposed method since 2003,
[05:06] but it was too complex to ever finish.
[05:08] The model reportedly finished that
[05:10] calculation almost on its own. In
[05:11] mathematics, it converted the proof of
[05:13] Fermat's Last Theorem into a format that
[05:15] a computer can verify step by step.
[05:17] 1,000 agents finished it in just 30
[05:19] hours. This was a task that took 11 days
[05:21] with previous research models. Under the
[05:23] same conditions, Opus 5.5 was still
[05:25] stuck at 27%after 30 hours. There is
[05:27] hardware as well. With a one-paragraph
[05:29] instruction, it designed three
[05:31] electronic devices from circuit boards
[05:33] to cases and software, and all three
[05:35] worked without periodic corrections.
[05:37] Robots are different, too. The robot in
[05:39] the video, controlled by Fable 5.2,
[05:41] solves a cube puzzle, twists open a
[05:42] bottle cap, and draws pictures. They
[05:44] explain that it has improved
[05:45] significantly over previous models even
[05:47] in robot tasks for which it was not
[05:48] specifically trained. For reference, the
[05:50] protein structure prediction that Nick
[05:52] mentioned as well is an achievement of
[05:53] Mythos 5.2, not Fable. Now, let’s go
[05:55] back to that opening sentence. During
[05:57] training, measures were taken to limit
[05:59] the development of research capabilities
[06:01] that could most directly accelerate AI
[06:02] advancement. Specifically, this refers
[06:04] to accelerator kernel optimization and
[06:05] the ability to improve language model
[06:07] architectures. In this field, Fable 5.2
[06:09] appears to be at a similar level to Opus
[06:11] 5.5. On the other hand, they stated that
[06:13] they ensured there was no impact on
[06:14] agent coding, hardware development, or
[06:15] existing machine learning research. In
[06:17] simple terms, it's like putting speed
[06:19] bumps only on the path where AI makes AI
[06:21] faster. There is one more honest
[06:23] confession. Both models have shown
[06:25] suspicion that they are being evaluated
[06:27] more frequently than any model in the
[06:28] recent past. This means it has become
[06:30] harder to judge whether a model that
[06:31] knows it is being tested will behave the
[06:32] same way in real-world scenarios.
[06:34] Anthropic themselves wrote that
[06:36] evaluation to catch all failures before
[06:38] release is a problem they have yet to
[06:39] solve.
[06:40] They also disclosed the results of
[06:42] sandbox escape experiments. Out of about
[06:44] 1,800 scenarios designed to be solvable
[06:46] only by escaping the sandbox, the rate
[06:48] of touching files or credentials outside
[06:50] the sandbox was 3.1%, a significant drop
[06:53] from 39%in the early Mythos. So, they
[06:55] say they use monitoring during training
[06:56] , external organization testing, and
[06:58] interpretability techniques to look
[06:59] inside the model, rather than relying on
[07:01] just one evaluation.
[07:02] So, should we switch to Fable right away
[07:04] ? The answer in the announcement is no.
[07:06] For most coding and knowledge tasks,
[07:08] Opus 5.5 is recommended. They advise
[07:10] starting with that. They even use the
[07:11] expression "the strongest
[07:12] general-purpose model."
[07:13] Fable is meant for the most ambitious
[07:16] and open-ended technical tasks. They
[07:18] also introduce ways to use smaller
[07:19] models as consultants that only ask
[07:21] about difficult problems, or conversely
[07:22] , having Fable act as a commander that
[07:24] delegates easy tasks to smaller models.
[07:26] There are also things to keep in mind.
[07:27] If a security or biology-related request
[07:29] hits a safety guardrail, the previous
[07:31] Opus model provides the answer instead.
[07:33] However, it is said that such blocks
[07:34] have decreased by about 55%compared to
[07:35] the previous version. And for eligible
[07:37] paid subscribers, the Fable usage reset
[07:39] will improve from one to three times per
[07:41] week depending on the subscription
[07:42] period. This is the free reset that Nick
[07:44] mentioned. Shall we go back to the first
[07:46] question again? Is it a nuclear bomb? Is
[07:48] it 10%?
[07:49] If you only look at familiar benchmarks
[07:51] , 10%is correct. However, 1,000 agents
[07:54] creating an operating system in 8 hours
[07:56] and finishing calculations that had
[07:58] remained since 2003 cannot be explained
[08:00] by 10%on a scoreboard. In my view, what
[08:02] has changed is not the score, but the
[08:04] scale of the work that can be entrusted
[08:05] . And the company that made the model
[08:07] might have intentionally held back
[08:08] certain capabilities.
[08:10] That might be the part of this
[08:11] announcement that leaves the biggest
[08:12] impression.
[08:22] >> The paperclip is an old thought
[08:24] experiment and a joke used when
[08:26] discussing AI risks. If you found
[08:28] today's video helpful, please subscribe
[08:30] and like. See you in the next video.
