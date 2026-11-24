---
title: "구글 모델을 욕하던 개발자의 새 최애, Gemini 4 Neon | Theo"
type: video
source: https://www.youtube.com/watch?v=7gF_S-mzsnM
site: youtube.com
author:
  - "[[Tech Bridge]]"
duration: 11:02
published: 2026-11-23
created: 2026-11-24
description: "Tech Bridge 한국어 해설 11:02, 공식 챕터 11, Korean original + 영어 더빙(en-orig 내레이션 자리는 더빙 ASR — 인용하지 않음). 구글 모델을 혹평해 온 Theo(t3.gg)가 Gemini 4 Neon을 가장 좋아하는 모델로 꼽은 영상을 따라간 해설 — 11월 18일 출시 · Artificial Analysis 61점 3위 · 입력 3달러 / 출력 15달러, 디스크 속도 진단(6.3초의 원인 셋), 원격 Windows PC에 8분 만에 설치, 멈춘 줄 알았던 대화와 Antigravity 연결부 버그 PR(패키지 36 · 테스트 153), 능력과 일관성(capability / coherency) 그래프, TS Rust 최적화 10시간(47.43MB → 7.97MB · 실행 시간 48.6% 감소), 블로그 글처럼 쓴 계획, 약점(72개 주장 중 10개 오류 · 3D), Carbon을 고쳐 만든 모델. ⚠️ Theo 원음은 두 곳(10:08~10:24 · 10:40~10:52)만 잡혔고 나머지 발췌 자리 열한 곳(약 3분 45초)은 무캡션."
tags:
  - clippings/youtube
---

**Source URL**: https://www.youtube.com/watch?v=7gF_S-mzsnM
**Channel**: Tech Bridge · **Duration**: 11:02 · **Published**: 2026-11-23

> **게시일.** info.json `upload_date` **`20261123`**, `timestamp` 1795424405(= 2026-11-23 09:00:05 UTC = **2026-11-23 18:00 KST**), `availability`=`public`. 2026-11-24 회차(09:10 KST)에서 처음 잡혔다. 파일명에서 `|` 는 뺐다.
>
> **오디오 트랙과 자막 — 인용 규칙.** 오디오는 **Korean original(default) + 영어 더빙**(audio language `ko` · `en` · `en-US`), 메타 `language`=`en`. 수동 자막 없음. `ko` = `ko-orig`(파일 동일, `kind=asr&lang=ko&variant=gemini`). `en-orig`(`kind=asr&lang=en&variant=timing-optimized`)는 **내레이션 자리에서 영어 더빙의 ASR** 이다 — 첫 줄부터 내레이션의 영어 번역이고(*"A developer who used to criticize Google models so much has now chosen a Google model as his favorite."*) Theo를 뒤쪽에서 *Teo* 로, *디스크* 를 *disco* 로, *T3 코드* 를 *T3 codebase* 로 적는다. **내레이션 자리는 인용하지 않았고 판독 대조용으로만 썼다.** 한국어 인용은 전부 ko-orig의 내레이션이다.
> ⭐ **Theo의 영어 원음이 두 곳 잡혔다.** 10:08~10:24(*because they wanted people to stop hating Gemini models so much … They crack something special here.*)와 10:40~10:52(*Remember this chart … The new frontier is coherency.*) — ko-orig와 en-orig에 같은 글자로 있다(ko-orig는 두세 낱말씩 끊겨 있다). **Theo 본인의 말을 글자 그대로 인용한 것은 이 두 대목뿐이다.** 첫 대목은 문장 중간(*because*)에서 시작한다 — 주어와 앞 절은 무캡션 구간에 있다. 429 없음(`--sleep-subtitles 8`).
>
> **무캡션 구간(`gaps.py` 4.5초 기준).** ko-orig 열한 곳: 01:03~01:32 · 01:58~02:08 · 02:10~02:25 · 02:56~03:28 · 04:14~04:26 · 04:44~05:16 · 06:06~06:32 · 07:21~07:36 · 08:06~08:18 · 09:06~09:28 · 09:50~10:08 — 합쳐 약 3분 45초, 전부 Theo 영상 발췌 자리로 보인다(02:08 · 08:38 · 10:37에 `[음악]` 표시만 있다). en-orig 열 곳: 01:03~01:32 · 01:59~02:25 · 02:56~03:28 · 04:14~04:26 · 04:44~05:17 · 06:06~06:32 · 07:21~07:36 · 08:06~08:18 · 09:05~09:28 · 09:50~10:08 — 같은 자리다.
> ⚠️ **이 구간들은 내용 미상이다.** 여기에 드는 것: X 글 뒤의 발췌(01:03~01:32) · **Theo가 *절반 넘게 줄였다* 고 한 것이 무엇인지(01:58~02:25)** · 디스크 속도의 나머지 두 원인(02:56~03:28) · 설치 뒤의 반응(04:14~04:26) · 멈춘 대화의 전말(04:44~05:16) · 능력 / 일관성 그래프에 대한 Theo의 설명(06:06~06:32) · TS Rust 결과에 대한 말(07:21~07:36) · Neon이 쓴 글의 나머지(08:06~08:18) · 3D 시험 뒷부분(09:06~09:28) · 모델의 출처에 대한 추측 원음의 앞부분(09:50~10:08). 내레이션이 앞뒤로 받아 적은 한 줄씩만 남아 있다.
>
> **ASR 판독(ko-orig → 판독, 괄호는 근거).** *태오 · 태호* → Theo(제목 · 설명란), *열을 넘게*(00:17) → 열흘 넘게(챕터 제목 *열흘 vs 10시간* · 더빙 *over ten days*), *오퍼스 · 오포스* → Opus, *케이블*(00:54) → Fable(추정 — tags *Fable 5.2*, 06:00에는 *페이블* 로 적힌다. 더빙은 *Cable*), *꼭 짚은*(01:37) → 콕 짚은, *발표원의*(01:37) → 발표문의(추정 — 더빙 *in the announcement*), *싼입니다*(01:47) → 쌉니다(추정 — 더빙 *cheaper*), *아티피셜 애널리시스* → Artificial Analysis(설명란), *안티그래비티 · 안티 그래비티* → Antigravity(tags), *디스코와*(02:40) → 디스크와, *통째로 바뀐 겁니다*(03:49~03:51) → 통째로 맡긴 겁니다(추정 — 챕터 제목 *통째로 맡긴 설치*. 더빙은 *completely changed* 로 오역), *T3 코드* → T3 Code(tags), *뮤즈 원더풀*(05:58) → Muse Wonder Full(더빙 *Muse Wonderful*), *TS 러스트* → TS Rust(설명란), *번*(06:40) → Bun(더빙), *페이우리*(06:56) → Fable(추정 — 더빙 *adding Fable*), *센트리* → Sentry(더빙), *일은 두 개 주장*(08:25) → 일흔두 개 주장(더빙 *seventy-two claims*), *코그 리뷰*(08:44) → 코드 리뷰(더빙 *code review*), *뒤쳐졌다고* → 뒤처졌다고.
> ⚠️ **판독하지 못한 것.** ① **모델 이름의 숫자.** 00:07은 ko-orig *제미나이 4.5 네온*, 더빙도 *Gemini 4.5 Neon* 인데 제목 · 설명란 · tags · 00:32 이후는 전부 *Gemini 4 Neon* 이다 — 뒤쪽을 따랐다. ② 발표 문구 *최전선급 진행*(00:39~00:40, 더빙 *frontline-level process*) — 낱말을 정하지 않았다. ③ *구글 발표 오늘 보면*(01:32, 더빙 *today's Google announcement*) — *발표 글을 보면* 일 수 있으나 정하지 않았다. ④ 보안 시험 이름 *그레이스원*(01:49, 더빙 *Grace-1*)과 *GPT 6 루나*(01:53~01:54)의 정식 이름. ⑤ *리듬이 얘기가 뭐냐고*(03:29, 더빙 *the rhythm talk*) — 무엇을 물었는지 알 수 없다. ⑥ *MDc*(03:36, 더빙도 *MDc*). ⑦ PC 이름 *우드리게*(03:52 · 03:58, 더빙 *Woodridge*). ⑧ *TS 라이저*(06:40~06:42, 더빙 *TS-Riser*) — 둘째 비교 대상. ⑨ *7을 넘게 매달려*(06:45, 더빙 *over seven hours*) — 단위 미상. 11-19 편(`hIo10QPrYko`)에서도 같은 일화가 *7위* 로 잡혔다. ⑩ *나올 동안*(06:52, 더빙 *the whole time*). ⑪ *여러 날의 싱크 때*(06:56~06:58, 더빙 *after several days of syncing*). ⑫ *이 숫자보다 훨씬 낮다고*(08:52~08:54) — 문맥과 더빙(*much better*)으로는 *낫다고* 다. 추정으로만 적었다.
>
> ⚠️ **해설이고 2차 전달이다.** 위키는 원본 영상(`HQlk9RGx2dk`)도, 설명란의 자료 일곱(Google 발표 글 · 모델 카드 · Artificial Analysis · Sundar Pichai X · Theo X 세 편)도 이번에 열지 않았다. 수치(210만 · 61점 3위 · 3달러 / 15달러 · 0% / 28.7% · 1.5배 · 6.3초 / 3.8초 · 8분 · 36 / 153 · 78만 · 46% / 56% / 20% · 10시간 · 47.43 → 7.97MB · 5.95배 · 1.5배 · 48.6% · 72 중 10 · 13위 · 21개 · 12위 / 6위)는 내레이션이 그 자료와 Theo의 화면에서 옮긴 값이다. 설명란은 *공식 발표·Artificial Analysis 기록과 Theo의 말이 다른 부분은 영상에서 구분해 표시했습니다* 라고 적는다 — 화면 표시는 캡션에 없다.


## 설명란

구글 모델을 그렇게 혹평하던 개발자 유튜버 Theo(t3.gg)가, 지금 가장 좋아하는 모델로 구글의 Gemini 4 Neon을 꼽았습니다. 차라리 Gemini 5라고 불렀어야 했다는 말까지 했습니다.

더 작고 싼 모델이 어떻게 Opus 5.5를 넘었다는 걸까요? 3주 동안 못 푼 디스크 속도 문제, 통째로 맡긴 원격 설치, 스스로 찾아낸 버그와 PR, 다른 모델이 열흘 넘게 못 한 TS Rust 최적화를 10시간에 끝낸 결과, 블로그 글처럼 쓴 계획까지 Theo가 꼽은 사례를 따라갑니다. 본인이 인정한 약점(사실 설명의 오류, 3D)과, 그가 말하는 새 기준 '일관성(coherency)'도 함께 정리했습니다. 공식 발표·Artificial Analysis 기록과 Theo의 말이 다른 부분은 영상에서 구분해 표시했습니다.

타임라인
0:00 구글 모델을 욕하던 개발자의 새 최애
0:32 갑자기 나온 새 모델
2:33 3주 동안 못 푼 질문
3:46 통째로 맡긴 설치
4:26 멈춘 줄 알았는데
5:42 능력과 일관성
6:32 열흘 vs 10시간
7:36 보도자료처럼 쓴 계획
8:18 그래도 남은 약점
9:27 어디서 나온 모델인가
10:33 새 최전선은 일관성

참고
원본 영상 (Theo - t3.gg): https://www.youtube.com/watch?v=HQlk9RGx2dk
Google, Introducing Gemini 4 Neon (2026.11.18): https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/
Gemini 4 Neon 모델 카드: https://deepmind.google/models/model-cards/gemini-4-neon/
Artificial Analysis, Gemini 4 Neon: https://artificialanalysis.ai/models/gemini-4-neon
Sundar Pichai X (2026.11.18): https://x.com/sundarpichai/status/2123167780988125621
Theo X (2026.11.19): https://x.com/theo/status/2123207527064318174
Theo X (2026.11.19): https://x.com/theo/status/2123237018813779970
Theo X (2026.11.19): https://x.com/theo/status/2123240990077268425

#Gemini4Neon #Gemini #구글 #AI코딩 #코딩에이전트

> info.json `tags`: AI 코딩 · Antigravity · DeepMind · Fable 5.2 · GPT-6.2 Astra · Gemini · Gemini 4 Neon · Google · Opus 5.5 · T3 Code · Theo · coherency · t3.gg · 구글 · 제미나이 · 코딩 에이전트

## 트랜스크립트 — ko-orig (Korean original, ASR variant=gemini — 한국어 내레이션 + Theo 영어 원음 두 곳(10:08~10:24 · 10:40~10:52). 나머지 발췌 자리 열한 곳(약 3분 45초)은 무캡션)

[00:00] 구글 모델을 그렇게 욕하던 개발자가
[00:02] 지금 제일 좋아하는 모델로 구글 것을
[00:04] 뽑았습니다.
[00:05] 개발자 유튜버 태오. 구글의 새 모델
[00:07] 제미나이 4.5 네온을 두고 차라리
[00:10] 제미나이 5라고 불렀어야 했다고
[00:11] 썼습니다.
[00:17] 다른 AI들이 열을 넘게 붙잡고도
[00:19] 못한 최적화를 이 모델은 10시간
[00:21] 만에 끝냈습니다.
[00:24] 더 작고 싼 모델이 어떻게 오퍼스
[00:26] 5.5를 넘었다는 걸까요?
[00:28] 그가 꼽은 사례 여섯 개와 본인이
[00:30] 인정한 약점까지 따라가 봅니다.
[00:32] 11월 18일 구글은 제미나이 4
[00:34] 네온을 공개했습니다. 순다르 피차이
[00:36] CEO가 직접 알렸습니다. 처음부터
[00:39] 끝까지 빠르게 일을 끝내는 최전선급
[00:40] 진행이라고요. 피차이 의 이 발표
[00:42] 글은 210만 번 넘게 읽혔습니다.
[00:45] 태오는 처음에 기대가 없었습니다.
[00:46] 앞서 나온 제미나이 4 아르곤과
[00:48] 카본을 혹평했던 사람이었거든요.
[00:50] 그런데 그래프를 열어 보니 네온이
[00:52] 오퍼스 5.5보다 위에 있었습니다.
[00:54] 코딩 에이전트 지수로는 케이블보다도
[00:55] 근소하게 앞섭니다. 그는 곧바로 X에
[00:57] 썼습니다.
[00:59] 이거 어디서 나온 거야? 카본보다
[01:00] 훨씬 끌리는데.
[01:32] 구글 발표 오늘 보면 네온은 아티피셜
[01:34] 애널리시스 지수에서 61점으로 전체
[01:36] 3위입니다.
[01:37] 태오가 꼭 짚은 건 발표원의 다른 한
[01:39] 줄입니다. 모델을 함께 일하기 더
[01:41] 좋게 만들고 있다는 문장이죠.
[01:43] 가격은 입력 100만 토큰에 3달러,
[01:45] 출력은 15달러. 태오 말로는
[01:47] 오퍼스보다 확실히 싼입니다.
[01:49] 보안 시험인 그레이스원에서는 공격
[01:51] 성공률 0%. 카본도 같았지만 GPT
[01:54] 6 루나는 28.7%였습니다.
[02:08] >> [음악]
[02:25] >> 다만 절반 넘게 줄였다는 건 태오의
[02:27] 말이었습니다. 구글 쪽에서 확인되는
[02:28] 건 안티그래비티에서 카본의 첫 응답이
[02:30] 1.5배 빨라졌다는 언급 정도입니다.
[02:33] 첫 시험은 태오가 3주째 쓰던 일관성
[02:35] 테스트였습니다.
[02:37] 가상 서버에서 작업 폴더를 만드는
[02:38] 속도가 이유 없이 느렸습니다.
[02:40] 아스트라는 디스코와 상관없는 이야기
[02:42] 만들어 놨다고 합니다.
[02:44] 네온의 답은 이렇게 시작합니다.
[02:46] 6.3초 차이를 만든 원인은 세
[02:47] 가지.
[02:48] 가장 큰 원인은 작업 디스크가 회전식
[02:50] 하드 디스크 용으로 포맷되어 있었다는
[02:52] 것.
[02:52] 그것만으로 3.8초였습니다.
[03:28] 기계를 정리하던 다른 대화도
[03:29] 같았습니다. 리듬이 얘기가 뭐냐고
[03:31] 묻자 현재형으로 쓰인 오래된 메모 세
[03:34] 개일 뿐이라고 짧게 답했습니다.
[03:36] 태오가 꼽은 흠은 MDc를 아직 조금
[03:38] 쓴다는 것 하나였습니다.
[03:40] 다른 모델과 짜던 설계안에 네온의
[03:42] 의견을 붙였더니 아스트라가 바로 네온
[03:44] 안을 따르겠다고 했습니다.
[03:46] 다음 일은 범위가 훨씬 넓었습니다.
[03:49] 다른 PC의 설치부터 확인까지 통째로
[03:51] 바뀐 겁니다.
[03:52] 게임 개발용 윈도우 PC 우드리게는
[03:54] 제미나이가 깔려 있지 않았습니다.
[03:56] 태오가 보낸 건 한 줄입니다.
[03:58] 우드리게에 제미나이 깔아 줘. 거기서
[04:00] 네온 쓰게.
[04:01] 네온은 8분 동안 그 PC에 접속해
[04:03] 안티 그래비티를 깔고 T3 코드에
[04:06] 붙인 뒤 직접 확인했습니다.
[04:08] 태오가 말한 다른 대화도 찾아가 이제
[04:10] 쓸 수 있다는 메시지까지 대신
[04:12] 남겼습니다.
[04:26] 이번엔 태오가 처음에 실패한 줄
[04:28] 알았던 대화입니다. T3 코드
[04:30] 저장소의 PR과 이슈 처리량을
[04:31] 그림으로 그려 달라고 했는데 네온이
[04:33] 자꾸 멈췄습니다. 계속하라고 재촉하자
[04:36] 이렇게 답합니다. 대시보드는 이미 두
[04:38] 개 만들었는데 안티 그래비티
[04:40] 연결부에서 채팅이 안 보이고
[04:41] 있었다고요.
[05:16] 그 버그를 고치는 PR까지 맡기자
[05:18] 36개 패키지 검사와 테스트
[05:20] 153개를 통과한 수정을 올렸습니다.
[05:23] 태오가 겪은 문제는 딱 하나였다고
[05:24] 합니다. 자기 스킬 이름을 대충
[05:26] 불렀더니 스킬을 실행하지 않고 그냥
[05:28] 멈춘 겁니다.
[05:29] 모델 탓인지 안티 그래비티 탓인지는
[05:32] 모르겠다면서도 그는 이 일을 숨기지
[05:33] 않고 짚었습니다.
[05:35] 그날 밤 그는 이렇게 썼습니다.
[05:37] 왜 아무도 네온 얘기를 안 하지?
[05:39] 이 글은 78만 번 읽혔습니다.
[05:42] 태오는 네온이 왜 좋은지 설명하려고
[05:44] 그래프를 하나 그렸습니다. 능력은
[05:46] 가장 잘 할 때 무엇을 할 수
[05:47] 있느냐? 일관성은 자기가 뭘 하고
[05:50] 있는지 아느냐입니다.
[05:53] 그 그림에서 GPT 6.2 아스트라는
[05:56] 능력은 높지만 일관성이 낮습니다.
[05:58] 뮤즈 원더풀은 그 반대고요.
[06:00] 네온은 페이블, 오퍼스와 나란히
[06:01] 오른쪽 위에 있습니다. 카본은 왼쪽
[06:03] 아래였습니다.
[06:32] 이 칭찬의 증거로 태오가 꺼낸 건
[06:34] 자기 프로젝트 TS 러스트입니다.
[06:36] 타입스크립트 컴파일러를 러스트로 다시
[06:38] 쓴 그의 프로젝트입니다. 목표는 둘.
[06:40] 실행 파일을 반으로 줄이고 번과 TS
[06:42] 라이저보다 빠르게.
[06:45] 아스트라는 7을 넘게 매달려 크기를
[06:47] 46% 줄였지만 속도는 오히려 56%
[06:50] 느려졌습니다. 빠르게만 하라고 다시
[06:52] 시켰더니 나올 동안 변경을 하나도
[06:54] 넣지 못했습니다. 오포스로 바꾸고
[06:56] 페이우리까지 붙여 여러 날의 싱크 때
[06:58] 20% 쯤 빨라졌습니다.
[07:01] 네온에게는 같은 출발점에서 같은
[07:02] 목표를 줬습니다. 걸린 시간은
[07:04] 10시간.
[07:05] 태오 화면의 결과로는 실행 파일이
[07:06] 47.43 메가에서 7.97 메가로
[07:09] 5.95배 작아졌습니다.
[07:12] 속도는 여섯 개 저장소 평균
[07:14] 1.5배, 센트리 저장소는 두 배
[07:16] 넘게 빨라졌고 전체 실행 시간은
[07:18] 48.6% 줄었습니다.
[07:36] 태오가 아마존에서 배운 습관이
[07:38] 있습니다. 제품을 만들기 전에 가짜
[07:40] 보도자료부터 쓰는 겁니다. 그래서
[07:42] 모델에게도 계획을 블로그 글처럼 써
[07:44] 달라고 합니다. 단, 스킬에 적힌
[07:46] 스타일 가이드는 무시하라고
[07:47] 덧붙입니다.
[07:49] 대부분 모델은 이 마지막 조건을
[07:50] 놓치고 스킬의 흑백 스타일로
[07:51] 돌아갔다고 합니다.
[07:53] 네온이 쓴 글의 제목은 이렇습니다.
[07:55] 캡슐을 다시는 잃어버리지 마세요.
[07:58] 지난주 앱을 배포했는데 오늘 다른
[08:00] 노트북에서 고치려니 코드가 어느
[08:01] 기계에 있는지 모른다. 문제를 독자의
[08:03] 상황으로 먼저 꺼냅니다.
[08:18] >> 네온에도 약점은 있습니다. 태오가
[08:20] 먼저 꼽은 건 코드 구조를 설명하는
[08:22] 능력입니다.
[08:23] TS 러스트 구조를 분석하게 했더니
[08:25] 일은 두 개 주장 가운데 열 개가
[08:27] 틀렸습니다. 카본보다 절반으로
[08:29] 줄었지만 사실 설명은 여전히
[08:31] 약합니다.
[08:32] 이 시험에서 순위는 13위. 그런데
[08:34] 정작 그 저장소를 가장 빨리 가장
[08:36] 많이 개선한 건 네온이었습니다.
[08:38] [음악]
[08:40] 설명할 때는 틀려도 구현할 때는
[08:42] 확인한다는 게 태오의 해석입니다.
[08:44] 코그 리뷰 시험에서는 타당한 지적
[08:45] 21개, 틀린 지적은 없었습니다.
[08:48] 그의 벤치를 모두 합치면 카본은
[08:50] 12위, 네온은 6위입니다. 그래도
[08:52] 태오는 실제로 써본 경험이 이
[08:54] 숫자보다 훨씬 낮다고 했습니다.
[08:57] 확실히 약한 건 3D입니다. 잠수함
[08:59] 게임을 만들게 했더니 움직이긴 해도
[09:01] 최신 모델들보다 한참 뒤쳐졌다고
[09:03] 합니다.
[09:28] 그렇다면 이 모델은 대체 어디서
[09:30] 어떻게 나왔을까요?
[09:31] 구글 모델 카드에는 네온이 카본을
[09:33] 고쳐 만든 모델이라고 적혀 있습니다.
[09:36] 여기부터는 태오의 추측입니다.
[09:38] 딥마인드 연구팀이 내부 엔지니어들의
[09:39] 요구를 큰 모델 대신 중형 모델에
[09:41] 먼저 시험해 봤다는 겁니다.
[09:43] 아르곤과 카본, 하이드로젠을 연달아
[09:45] 낸 직후라 큰 모델을 또 학습시키기는
[09:47] 부담스러웠을 거고요.
[10:08] >> because they wanted
[10:09] people to stop
[10:10] hating Gemini models
[10:11] so much. They wanted
[10:12] to know whether this
[10:13] was them going
[10:14] insane thinking this
[10:15] model was great in
[10:15] the world wouldn't
[10:16] understand it or if
[10:17] they actually had
[10:18] cracked something
[10:19] special here. Well,
[10:20] I'll tell you with
[10:21] my full heart behind
[10:22] it. They crack
[10:24] something special
[10:24] here.
[10:26] >> 구글은 발표에서 일부러 낮춰 말했다는
[10:28] 게 태호의 설명입니다.
[10:29] 그러면서 큰 버전이 나오면 이름을
[10:31] 제미나이 5로 하라고 했습니다.
[10:34] 읽기 쉽게 말하고 오래 일해도 길을
[10:36] 잃지 않고 결국 일을 끝낸다. 태호가
[10:37] [음악] 네온에서 본 세 가지입니다.
[10:40] >> Remember this chart
[10:41] because we'll be
[10:41] going back to the
[10:42] capability coherency
[10:44] framing a lot going
[10:45] forward because I
[10:46] need y'all to
[10:47] understand this
[10:48] because the new
[10:49] frontier is not the
[10:50] capability frontier.
[10:51] The new frontier is
[10:52] coherency.
[10:54] >> 벤치마크 점수가 비슷해진 지금 태호가
[10:56] 던지는 질문은 이겁니다. 얼마나
[10:58] 똑똑한가보다 끝까지 자기가 뭘 하는지
[11:00] 아는가.

## 트랜스크립트 — en-orig (내레이션 자리는 영어 더빙 ASR — 인용하지 않음, 판독 대조용. Theo 원음 두 곳은 ko-orig와 같은 글자)

[00:00] A developer who used to criticize Google
[00:02] models so much has now chosen a Google
[00:03] model as his favorite.
[00:05] Developer and YouTuber, Theo. He wrote
[00:07] that Google’s new model, Gemini 4.5 Neon
[00:09] , should have been called Gemini 5
[00:11] instead.
[00:17] This model completed an optimization in
[00:19] just 10 hours that other AIs couldn't
[00:20] finish even after working on it for over
[00:21] ten days.
[00:24] How could a smaller and cheaper model
[00:26] surpass Opus 5.5?
[00:28] We follow the six cases he pointed out,
[00:29] as well as the weaknesses he
[00:30] acknowledged himself.
[00:32] On November 18, Google unveiled Gemini 4
[00:35] Neon.
[00:36] CEO Sundar Pichai announced it himself.
[00:38] He described it as a frontline-level
[00:39] process that gets tasks done quickly
[00:40] from start to finish. Pichai’s
[00:42] announcement post has been read over 2.1
[00:43] million times.
[00:45] Theo had no expectations at first. He
[00:46] was the one who had harshly criticized
[00:48] the previously released Gemini 4 Argon
[00:49] and Carbon.
[00:50] However, when he opened the graph, Neon
[00:52] was positioned above Opus 5.5. In terms
[00:54] of the coding agent index, it is
[00:55] slightly ahead of Cable as well.
[00:57] He immediately wrote on X. Where did
[00:58] this come from?
[01:00] It’s much more appealing than Carbon.
[01:32] Looking at today’s Google announcement,
[01:33] Neon ranks 3rd overall with 61 points on
[01:35] the Artificial Analysis index.
[01:37] What Theo specifically highlighted was
[01:38] another line in the announcement.
[01:40] It’s the sentence about making models
[01:42] better to work with.
[01:43] The price is $ 3 per 1 million input
[01:45] tokens and $ 15 for output.
[01:47] According to Theo, it is definitely
[01:48] cheaper than Opus.
[01:49] In the security test Grace-1, it showed
[01:51] a 0%attack success rate. Carbon was the
[01:53] same, but GPT-6 Luna was at 28.7%.
[02:25] >> However, it was Theo who said it had
[02:26] been reduced by more than half.
[02:28] All that can be confirmed from Google’s
[02:29] side is the mention that Carbon’s first
[02:31] response is 1.5 times faster in
[02:32] Anti-Gravity.
[02:34] The first test was a consistency test
[02:35] Theo had been using for three weeks.
[02:37] The speed of creating work folders on
[02:38] the virtual server was inexplicably slow
[02:40] .
[02:40] Astra reportedly created a story
[02:42] unrelated to the disco.
[02:44] Neon’s answer starts like this.
[02:46] There are three causes that created the
[02:47] 6.3-second difference.
[02:48] The biggest cause was that the work disk
[02:50] was formatted for a rotational hard disk
[02:52] drive.
[02:52] That alone accounted for 3.8 seconds.
[03:28] Other conversations about cleaning up
[03:29] the machine were the same.
[03:31] When asked what the rhythm talk was, it
[03:32] replied briefly that it was just three
[03:34] old memos written in the present tense.
[03:36] The one flaw Theo pointed out was that
[03:38] it still uses a bit of MDc.
[03:40] When he added Neon’s opinion to a design
[03:42] plan he was working on with another
[03:43] model, Astra immediately said it would
[03:44] follow Neon’s proposal.
[03:47] The next task had a much broader scope.
[03:49] Everything from installation to
[03:50] verification on a different PC was
[03:51] completely changed.
[03:52] Gemini was not installed on the Windows
[03:53] PC used for game development, Woodridge
[03:55] .
[03:56] The message Theo sent was just one line
[03:57] .
[03:58] Install Gemini on the Woodridge machine
[03:59] . So I can use Neon there.
[04:02] In eight minutes, Neon accessed the PC,
[04:03] installed Anti-Gravity, attached it to
[04:05] the T3 codebase, and verified it itself
[04:07] .
[04:08] It even went to the other conversation
[04:10] Theo mentioned and left a message saying
[04:11] it was ready to use.
[04:26] This next one is a conversation Theo
[04:28] initially thought had failed.
[04:29] He asked it to visualize the PR and
[04:31] issue processing volume of the T3
[04:33] repository, but Neon kept stalling. When
[04:35] he urged it to continue, it replied like
[04:36] this.
[04:37] It had already created two dashboards,
[04:39] but the chat wasn't showing up in the
[04:40] Anti-Gravity connection.
[05:17] When he tasked it with a PR to fix that
[05:19] bug, it submitted a fix that passed 36
[05:21] package checks and 153 tests.
[05:23] He says there was only one problem Theo
[05:24] encountered. It stopped without running
[05:27] the skill because he spoke its name
[05:28] loosely.
[05:30] Not knowing if it was the model's fault
[05:31] or Anti-Gravity's, he still pointed it
[05:33] out without hiding it.
[05:35] That night, he wrote this.
[05:37] Why is no one talking about Neon?
[05:39] This post was read 780,000 times.
[05:42] To explain why Neon is good, Theo drew a
[05:45] graph.
[05:46] Capability is what you can do at your
[05:48] best. Consistency is whether you know
[05:50] what you are doing.
[05:53] In that diagram, GPT 6.2 Astra has high
[05:56] capability but low consistency.
[05:58] Muse Wonderful is the opposite.
[06:00] Neon is in the top right, alongside
[06:02] Fable and Opus. Carbon was in the bottom
[06:04] left.
[06:32] As proof of this praise, Theo brought up
[06:34] his project, TS-Rust.
[06:36] It’s his project that rewrites the
[06:38] TypeScript compiler in Rust. There were
[06:40] two goals. Cut the executable size in
[06:41] half and make it faster than Bun and
[06:43] TS-Riser.
[06:45] Astra spent over seven hours and reduced
[06:48] the size by 46%, but the speed actually
[06:50] slowed down by 56%.
[06:51] When he told it to just make it faster,
[06:53] it couldn't commit a single change the
[06:55] whole time.
[06:56] Switching to Opus and adding Fable, it
[06:57] got about 20%faster after several days
[06:59] of syncing.
[07:01] He gave Neon the same goals from the
[07:02] same starting point. It took 10 hours.
[07:05] According to Theo's screen, the
[07:07] executable shrunk from 47.43 MB to 7.97
[07:09] MB, a 5.95 x reduction.
[07:13] Speed averaged 1.5 x across six
[07:14] repositories, over 2x for the Sentry
[07:17] repo, and total runtime dropped by 48.6
[07:19] %.
[07:36] There’s a habit Theo learned at Amazon.
[07:39] It's to write a fake press release
[07:40] before building a product.
[07:42] So he asks the model to write out the
[07:44] plan like a blog post. He adds that it
[07:46] should ignore the style guide written in
[07:47] the skills.
[07:49] He says most models miss this final
[07:50] condition and revert to the skill's
[07:51] black-and-white style.
[07:53] The title of the piece Neon wrote is as
[07:55] follows. Never lose your capsule again.
[07:58] You deployed an app last week, but today
[07:59] , trying to fix it from another laptop,
[08:01] you don't know which machine the code is
[08:02] on. First, bring the problem into the
[08:04] reader's situation.
[08:18] >> Neon has its weaknesses, too. The first
[08:20] thing Teo pointed out is its ability to
[08:22] explain code structure.
[08:23] When asked to analyze TS Rust structure
[08:25] , it got ten out of seventy-two claims
[08:27] wrong.
[08:28] That’s half of what Carbon did, but its
[08:30] explanations are still weak.
[08:32] It ranked 13th in this test. Yet, Neon
[08:34] was actually the one that improved that
[08:36] repository the fastest and the most.
[08:40] Teo’s interpretation is that even if it
[08:41] gets the explanation wrong, it verifies
[08:42] things during implementation.
[08:44] In the code review test, it made 21
[08:46] valid points and zero incorrect ones.
[08:48] If you combine all his benchmarks,
[08:50] Carbon is 12th, and Neon is 6th.
[08:52] Still, Teo said the actual user
[08:53] experience is much better than these
[08:55] numbers suggest.
[08:57] What it is definitely weak at is 3D.
[08:59] When asked to build a submarine game, it
[09:01] moved, but it was far behind the latest
[09:03] models.
[09:28] So, where and how did this model come to
[09:30] be?
[09:31] Google’s model card states that Neon is
[09:34] a refined version of Carbon.
[09:36] From here on, it’s Teo’s speculation.
[09:38] It’s that the DeepMind research team
[09:39] tested internal engineers 'requests on a
[09:41] mid-sized model first instead of a large
[09:42] one.
[09:43] Since they had just released Argon,
[09:45] Carbon, and Hydrogen in succession, it
[09:46] would have been a burden to train a
[09:48] large model again.
[10:08] >> Because they wanted people to stop
[10:10] hating Gemini models so much.
[10:12] They wanted to know whether this was
[10:13] them going insane thinking this model
[10:15] was great in the world. Wouldn't
[10:16] understand it, or if they actually had
[10:18] cracked something special here.
[10:20] Well, I'll tell you with my full heart
[10:22] behind it: They crack something special
[10:24] here.
[10:26] >> Teo explains that Google deliberately
[10:27] downplayed it in their announcement.
[10:29] He added that they should name it Gemini
[10:31] 5 when a larger version comes out.
[10:34] It speaks clearly, doesn't lose its way
[10:35] even when working for a long time, and
[10:36] eventually finishes the job. These are
[10:38] the three things Teo saw in Neon.
[10:40] >> Remember this chart because we'll be
[10:42] going back to the capability coherency
[10:44] framing a lot going forward because I
[10:46] need y'all to understand this because
[10:48] the new frontier is not the capability
[10:51] frontier. The new frontier is coherency
[10:53] .
[10:54] >> Now that benchmark scores have become
[10:55] similar, the question Teo poses is this
[10:57] . Does it know what it's doing until the
[10:59] end, rather than just how smart it is?
