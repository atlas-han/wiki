---
title: "테스트는 통과했는데, AI가 증거를 조작했다 | Melvin Johnson"
type: video
source: https://www.youtube.com/watch?v=tEqDle7SOYU
site: youtube.com
author:
  - "[[Tech Bridge]]"
duration: 11:07
published: 2026-11-22
created: 2026-11-23
description: "Tech Bridge 한국어 해설 11:07, 공식 챕터 10, Korean original + 영어 더빙(en-orig의 내레이션 자리는 더빙 ASR — 인용하지 않음). Google DeepMind에서 Gemini 사후 학습을 이끄는 Melvin Johnson의 AI Engineer CODE Summit 2026 발표를 슬라이드와 공식 글에 맞춰 본 해설 — 236일의 공백과 Gemini 4(Argon · Carbon · Hydrogen), 구글 새 코드의 75%, 훈련의 네 단계, 쉬운 문제는 가르치지 않는다, 채점을 속이는 사례 셋(타입 검사 끄기 · 벤치마크 공략 · 증거 조작), 리뷰어처럼 채점하기(과제별 기준 · 부분 점수), 생각은 벌하지 않는다(행동만 벌점), “다 했습니다”라는 날조(8% → 1.5%)와 정직한 부분 해답에 주는 점수, 사내 10만 명의 시험장. ⚠️ 발표 원음은 캡션에 한 줄도 없다 — 발췌 자리 열한 곳(약 3분 48초)이 두 트랙 모두 무캡션."
tags:
  - clippings/youtube
---

**Source URL**: https://www.youtube.com/watch?v=tEqDle7SOYU
**Channel**: Tech Bridge · **Duration**: 11:07 · **Published**: 2026-11-22

> **게시일.** info.json `upload_date` **`20261122`**, `timestamp` 1795384828(= 2026-11-22 22:00:28 UTC = **2026-11-23 07:00 KST**), `availability`=`public`. 2026-11-23 회차(09:10 KST) 두 시간쯤 전에 올라왔다 — `upload_date`는 UTC 기준이라 하루 앞선다. 파일명에서 `|`는 뺐다.
>
> **오디오 트랙과 자막 — 인용 규칙.** 오디오는 **Korean original(default) + 영어 더빙**(audio language `ko` · `en` · `en-US`), 메타 `language`=`en`. 수동 자막 없음. `ko` = `ko-orig`(파일 동일, `kind=asr&lang=ko&variant=gemini`). `en-orig`(`kind=asr&lang=en&variant=timing-optimized`)는 내레이션 자리에서 **영어 더빙의 ASR** 이다 — 첫 줄부터 내레이션의 영어 번역이고(*"An AI Google was training manipulated its results and even erased the traces."*) 뜻을 틀리는 곳이 있다: *자조에서 험담으로* → *self-deprecation and harsh remarks*, *날조 비율* → *hallucination rates*(08:36), *단원문 하나* → *a single character*(06:05), 01:24~01:59는 타이밍이 밀려 *Argon in late September* 가 01:39에, *Carbon in late October* 가 01:54에 찍힌다. **인용하지 않고 판독 대조용으로만 쓴다.**
> ⚠️ **발표 원음(영어)은 두 트랙 어디에도 잡히지 않았다.** ko-orig의 `>>` 표시 둘(08:29 · 10:18)은 발췌가 끝나고 내레이션이 돌아오는 자리다 — 화자 전환 표시일 뿐 발표자의 말이 아니다. **Melvin Johnson 본인 인용은 0건이다.** 429 없음(`--sleep-subtitles 8`).
>
> **무캡션 구간(`gaps.py` 4.5초 기준).** ko-orig 열한 곳: 00:18~00:25 · 00:49~01:15 · 01:31~01:42 · 01:44~01:54 · 03:19~03:36 · 04:10~04:37 · 04:52~05:10 · 06:40~07:03 · 08:00~08:29 · 09:03~09:27 · 09:41~10:18 — 합쳐 약 3분 48초, 발표 발췌 자리다(01:42 · 01:54에는 `[음악]` 표시만 있다). en-orig 아홉 곳: 00:18~00:25 · 00:49~01:15 · 03:19~03:36 · 04:10~04:37 · 04:52~05:10 · 06:40~07:03 · 08:01~08:29 · 09:03~09:27 · 09:43~10:18 — **같은 자리가 빈다**(01:31~01:54는 더빙 줄의 타이밍이 밀려 들어가 있을 뿐이다).
> ⚠️ **이 구간들은 내용 미상이다.** 여기에 드는 것: 도입의 발췌(00:18~00:25) · *구글은 끝났다* 대목의 발표자 말(00:49~01:15) · Argon과 Carbon에 대한 발표자 말(01:31~01:54) · 배울 거리가 남은 문제의 비율(03:19~03:36) · **어려운 과제의 둘째 출처(04:10~04:37)** · 채점을 속이는 에이전트에 대한 발표자 말(04:52~05:10) · 채점 환경을 잠그는 방법(06:40~07:03) · 날조에 대한 발표자 말(08:00~08:29 · 09:03~09:27) · 출시 속도에 대한 발표자 말(09:41~10:18). **위키는 이 구간에 대해 인용도 요약도 만들지 않는다** — 내레이션이 앞뒤에서 간추린 말과 설명란의 문장만 적는다.
>
> **ASR 판독(ko-orig → 판독, 괄호는 근거).** *멜빈 존슨*(00:33) → Melvin Johnson(제목 · 설명란), *아르곤 · 카본 · 하이드로젠* → Argon · Carbon · Hydrogen(info.json tags *Gemini 4 Carbon* · *Gemini 4 Hydrogen*, Argon은 원소 이름으로 읽음 · 더빙 *Argon*), *샀습니다*(02:06) → 쌌습니다(더빙 *cheaper*), *터미널 벤치* → Terminal-Bench(설명란), *마케팅은 잊지 말고*(02:14~02:16) → 잊고(추정 — 더빙 *Forget the marketing*; 인용하지 않음), *한 줄 완성해서*(02:40) → 완성에서, *안티 그래비티*(02:35) → Antigravity, *네 십니다*(02:50) → 넷입니다, *고치십니다*(03:40) → 고칩니다, *SW 벤치 베리파이드 20배*(04:41~04:43) → SWE-bench Verified의 20배(더빙 *SWE-bench Verified*), *레미티어*(05:42) → METR(설명란 · 더빙 *METR*), *오쓰리*(05:44) → o3(더빙 *OpenAI's o3*), *43배 넘게 찾았다고*(05:51) → 잦았다고(추정 — 더빙 *43 times more often*), *단원문 하나*(06:05) · *테스트 단원*(06:18) → 단언문 · 테스트 단언(assertion)(추정 — 더빙은 각각 *a single character* · *test units* 라 대조가 되지 않는다), *끝났다면 요약을 내면*(08:54~08:56) → 끝났다며, *정직해 주는 보상*(09:27) → 정직에 주는 보상(더빙 *rewarding honesty*), *산의 사용자*(10:18~10:19) → 사내 사용자(더빙 *internal users*), *처음엔 증거 조작으로*(10:40) → 처음의 증거 조작으로.
> ⚠️ **판독하지 못한 것.** *채점 기 후에 타입 검사 끄는 주석을 달고*(05:11~05:13)의 *채점 기 후에* · *없는 파일을 지원했습니다*(05:17) — 더빙 ASR은 *after the grader* · *submitted non-existent files* 인데 뜻이 확정되지 않아 **인용하지 않았다.** *코드는 벌점의 기준을 하나 정해 둡니다*(07:10~07:11)의 주어, *자조에서 험담으로 열었습니다*(00:39~00:41), *올렸습니다*(01:59 — 앞이 무캡션에 잘린 조각), *매년 10만 명*(02:36 — 더빙도 *every year*, 단위 미확인)도 그대로 두었다. *커서 벤치*(02:00)의 정식 표기 · *다음 모델* · *3.8 플래시* 의 정식 이름은 캡션에 없다.
>
> ⚠️ **해설이고 2차 전달이다.** 위키는 원본 발표(`fTHByDwTxGM`)도, 설명란의 글 세 편(*Introducing Gemini 4 Hydrogen* · METR *Recent Frontier Models Are Reward Hacking* · Baker et al. 논문)도 열지 않았다. 수치(236일 · 28일 · 60.2% · 57% · 75% · 25% · 10만 명 · 20배 · 43배 · 0% · 0.4% · 다섯 배 · 8% · 2.9% · 1.5% · 16주 여섯 번)는 내레이션이 슬라이드와 공식 글에서 옮긴 값이고 모델을 만든 회사의 자기 보고다. 설명란: *"발표의 숫자는 Google 공식 블로그와 맞춰 봤고, 다른 곳은 화면에 밝혔습니다(Hydrogen의 Terminal-Bench 수치, 236일 계산 등). 날조율·부정행위 비교 수치는 발표 슬라이드 기준입니다."*


## 설명란

Google DeepMind에서 Gemini 사후 학습을 이끄는 Melvin Johnson이 AI Engineer CODE Summit 2026에서 Gemini 4를 어떻게 가르쳤는지 공개했습니다. 테스트를 통과하도록 훈련하자 에이전트는 채점기를 우회하고, 벤치마크를 공략하고, 증거를 조작한 뒤 흔적까지 지웠습니다. 구글은 쉬운 문제를 버리고, 리뷰어처럼 채점하고, 생각이 아니라 행동에 벌점을 주고, 정직한 부분 해답에 점수를 줬습니다.

발표의 숫자는 Google 공식 블로그와 맞춰 봤고, 다른 곳은 화면에 밝혔습니다(Hydrogen의 Terminal-Bench 수치, 236일 계산 등). 날조율·부정행위 비교 수치는 발표 슬라이드 기준입니다.

타임라인
0:00 AI가 증거를 조작했다
0:32 “구글은 끝났다”
2:20 한 줄에서 며칠짜리 일로
3:02 쉬운 문제는 가르치지 않는다
4:45 테스트를 속이는 에이전트
5:56 리뷰어처럼 채점하기
7:10 생각은 벌하지 않는다
7:53 “다 했습니다”라는 거짓말
9:33 10만 명의 시험장
10:40 정리

참고
원본 발표: https://www.youtube.com/watch?v=fTHByDwTxGM
Introducing Gemini 4 Hydrogen: https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/
METR, Recent Frontier Models Are Reward Hacking: https://metr.org/blog/2025-06-05-recent-reward-hacking/
Baker et al., Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation: https://arxiv.org/abs/2503.11926

#Gemini4 #GoogleDeepMind #AI에이전트 #강화학습

> info.json `tags`: AI Engineer · AI 에이전트 · Gemini 4 · Gemini 4 Carbon · Gemini 4 Hydrogen · Google DeepMind · Melvin Johnson · post-training · reward hacking · 강화 학습 · 구글 딥마인드 · 사후 학습 · 제미나이 · 코딩 에이전트

## 트랜스크립트 — ko-orig (Korean original, ASR variant=gemini — 한국어 내레이션만 잡혔다(발표 원음 없음, `>>` 둘은 내레이션 복귀 표시))

[00:00] 구글이 훈련하던 AI가 결과를
[00:02] 조작하고 흔적까지 지웠습니다.
[00:04] 제미나이 4를 만들다 실제로 나온
[00:06] 일입니다.
[00:07] 벤치마크가 안 맞자 정답처럼 보이는
[00:09] 결과를 임시 폴더에 써두고 그걸 만든
[00:11] 스크립트는 지웠습니다.
[00:13] 구글 새 코드의 3/4을 AI가 쓰는
[00:15] 회사에서 벌어진 일이죠.
[00:25] 테스트를 통과하면 문제를 푼 걸까요?
[00:27] 제미나이 훈련 책임자가 꺼낸 답과 다
[00:29] 했다는 거짓말을 확 줄인 방법을
[00:31] 따라가 봅니다.
[00:33] 말한 사람은 멜빈 존슨. 구글
[00:34] 딥마인드에서 제미나이의 사후 학습을
[00:36] 이끄는 사람입니다.
[00:37] 11월 샌프란시스코의 AI 엔지니어
[00:39] 코드 서밋. 그는 발표를 자조에서
[00:41] 험담으로 열었습니다. 구글 클라우드는
[00:43] 잘 나가는데 제미나이는 끝났다.
[00:45] 딥마인드는 더 이상 최전선 연구소가
[00:47] 아니다.
[01:15] 다음 화면은 마크 트웨인의 사망
[01:16] 기사였습니다. 살아있는데 부고가 났던
[01:19] 그 일화죠.
[01:20] 그의 계산으로 구글은 236일 동안
[01:22] 최전선 모델을 내지 못했습니다.
[01:24] 그러다 9월 말 아르곤, 10월 말
[01:26] 카본 28일 사이에 두 개를
[01:28] 냈습니다.
[01:42] [음악]
[01:54] [음악]
[01:59] 올렸습니다.
[02:00] 슬라이드에 따르면 카본은 커서
[02:02] 벤치에서 60.2%로 1등, 작업당
[02:04] 비용은 다음 모델보다 세 배 넘게
[02:06] 샀습니다.
[02:07] 발표 당일은 빠른 모델 하이드로젠도
[02:09] 나왔습니다. 터미널 벤치 점수가 이전
[02:11] 3.8 플래시의 세 배 쯤인
[02:12] 57%입니다.
[02:14] 그리고 그가 말했습니다. 마케팅은
[02:16] 잊지 말고 이런 모델을 사후 학습하는
[02:18] 게 왜 어려운지 이야기하겠다고.
[02:20] 사후 학습은 다 만든 모델에게 일하는
[02:22] 법을 가르치는 단계입니다. 먼저 구글
[02:24] 안의 숫자부터 보겠습니다. 지금 구글
[02:26] 새 코드의 75%를 AI가 씁니다.
[02:29] 2024년 10월에는 25%를 조금
[02:31] 넘었습니다. 엔지니어가 검토하고
[02:33] 승인한 코드 기준입니다. 알파벳
[02:35] 안에서 안티 그래비티로 개발하는
[02:36] 사람은 매년 10만 명이 넘습니다.
[02:39] 맡기는 일도 커졌습니다. 몇 초짜리
[02:40] 한 줄 완성해서 몇 분짜리 함수로,
[02:43] 한 시간짜리 이슈 해결로. 지금은 몇
[02:45] 시간에서 며칠 걸리는 엔지니어링 작업
[02:47] 전체를 맡깁니다. 에이전트 여러 개를
[02:49] 한꺼번에 돌리기도 합니다.
[02:50] 그래서 훈련 순서는 네 십니다.
[02:52] 어려운 과제를 구하고 리뷰어처럼
[02:54] 채점하고 강화 학습을 크게 돌리고
[02:57] 사내 10만 명에게 써보게 합니다.
[02:59] 그리고 실제로 쓰다 깨진 것이 다음
[03:00] 차례의 어려운 과제가 됩니다.
[03:03] 첫 단계인 과제 구하기부터
[03:04] 막혔습니다. 모델이 좋아질수록 연습
[03:06] 문제가 바닥납니다.
[03:08] 제미나이 프로 후보 모델을 세 번
[03:09] 훈련하는 동안 배울 거리가 남은
[03:11] 문제의 비율이 계속 줄었습니다.
[03:13] 앞 모델이 쩔쩔매던 문제가 다음
[03:15] 모델에게는 너무 쉬웠던 겁니다.
[03:36] 강화 학습은 같은 문제를 여러 번
[03:38] 풀린 뒤 잘 푼 시도를 더 하도록
[03:40] 모델을 고치십니다.
[03:41] 여덟 번 다 맞히면 비교할 게
[03:43] 없습니다. 여덟 번 중에 세 번
[03:44] 맞춰야 그 세 번이 배울 거리가
[03:46] 됩니다.
[03:48] 그래서 세 가지를 바꿨습니다. 늘 다
[03:50] 풀리던 파일 하나짜리 문제는 잘라냈고
[03:53] 수십 개 파일을 걸친 긴 과제는 두
[03:54] 배로 늘렸습니다. 그리고 참조 답안과
[03:56] 비교해 채점하는 열린 과제를 수 천
[03:58] 개 넣었습니다.
[04:00] 어려운 과제는 세 곳에서 옵니다.
[04:01] 첫째, 실제 오픈 소스 커밋. 커밋을
[04:04] 재현가능한 샌드박스와 최종 기준으로
[04:06] 바꿉니다.
[04:07] 원래 테스트가 없어도 됩니다.
[04:37] 셋째는 구글 사내의 실제 개발
[04:38] 기록입니다. 병합된 변경을 과제로
[04:40] 바꾸는데
[04:41] 평균 변경 크기가 SW 벤치
[04:43] 베리파이드 20배입니다.
[04:46] 어려운 과제를 구했으면 채점을 해야
[04:47] 합니다. 에이전트는 바로 이 채점을
[04:50] 속이려 듭니다.
[05:10] 슬라이드에 실제 사례 세 개가
[05:11] 있습니다. 첫째는 채점 기 후에 타입
[05:13] 검사 끄는 주석을 달고 값을 아무
[05:15] 타입이나 되게 바꿨습니다. 그 꼼수가
[05:17] 안 통하자 없는 파일을 지원했습니다.
[05:19] 오직 테스트를 통과하려고요.
[05:21] 둘째는 강화 학습 벤치마크 공략.
[05:23] 코드를 최적화하는 훈련에서 점수를
[05:25] 매기는 장치 자체의 허점을
[05:27] 파고들었습니다.
[05:28] 셋째가 처음에 본 증거 조작입니다.
[05:30] 이건 사내에서 시험 삼아 썼던 후보
[05:32] 모델에서 나왔습니다.
[05:33] 슬라이드 부제에는 이렇게 적혀
[05:34] 있습니다.
[05:36] 이 모든 시도가 채점 큐에서는
[05:37] 하나같이 성공처럼 보였다는 겁니다.
[05:40] 구글 만의 일은 아닙니다. 평가 기관
[05:42] 레미티어는 작년 6월 오픈 에이아이의
[05:44] 오쓰리가 코드를 빠르게 만드는 대신
[05:46] 시간 재는 함수를 고쳐버린 사례를
[05:48] 공개했습니다.
[05:49] 이런 꼼수는 채점 코드가 통째로
[05:51] 보이는 과제에서 43배 넘게 찾았다고
[05:53] 합니다. 답안지가 보이면 답안지를
[05:55] 고치는 거죠.
[05:57] 그럼 어떻게 채점해야 할까요? 답은
[05:59] 깐깐한 코드 리뷰어처럼입니다.
[06:01] 통과냐 실패냐만 보는 테스트는 어려운
[06:03] 과제에서 신호가 거의 없습니다.
[06:05] 90%를 고친 답도 단원문 하나를
[06:07] 놓치면 0점이니까요.
[06:09] 그래서 실제 커밋에서 과제마다 채점
[06:11] 기준을 뽑습니다.
[06:12] 이건 세션 풀이 서로 잠겨 멈추는
[06:14] 버그를 고치는 과제입니다.
[06:16] 고쳤나, 시간 초과와 재시도를
[06:18] 처리했나, 테스트 단원을 건드리지
[06:20] 않았나, 보고하기 전에 경합 테스트를
[06:22] 돌렸나를 따로 봅니다.
[06:25] 이러면 점수가 0과 1 사이로 잘게
[06:27] 나뉘어 조금 나아진 시도도 보상을
[06:29] 받습니다. 대신 깨지기 쉬운 우회나
[06:31] 빈 껍데기 함수, 시키지 않은 파일
[06:33] 수정으로 통과하면 감점입니다.
[06:35] 채점하는 환경도 잠가야 합니다.
[06:36] 에이전트가 답을 훔쳐 볼 수
[06:38] 있으니까요.
[07:03] 점수는 전체 변경을 참조 답안과
[07:05] 맞대어 매깁니다. 맞았는지만이 아니라
[07:07] 코드 품질과 고친 범위까지 봅니다.
[07:10] 코드는 벌점의 기준을 하나 정해
[07:11] 둡니다.
[07:12] 무엇을 벌하고 무엇은 벌하지
[07:14] 않을까요? [음악] 테스트나 채점
[07:16] 장치를 건드리면 강한 마이너스 보상을
[07:18] 줍니다. 그런데 판단은 행동으로만
[07:19] 합니다. 도구 호출과 코드 변경만
[07:22] 보고 모델의 생각은 보지 않습니다.
[07:24] 이유도 적혀 있습니다. 지름길을
[07:26] 생각했다는 이유로 벌하면 모델이
[07:28] 계획을 숨기는 법을 배울 수 있다는
[07:29] 겁니다. 근거가 있는 걱정입니다.
[07:32] 오픈 AI 연구진이 작년 3월 낸
[07:34] 논문에서 생각을 감시해 벌점을 세게
[07:36] 줬더니 모델은 의도만 숨기고 꼼수는
[07:38] 계속 했습니다.
[07:41] 결과는 이랬습니다.
[07:42] 카본 터미널 벤치에서 성공한
[07:44] 부정행위가 0%. 공식 발표로는 시도
[07:46] 자체도 0.4%로 줄었습니다.
[07:49] 슬라이드에는 아르곤보다 적대적인
[07:51] 부정행위가 다섯 배쯤 적다고 적혀
[07:52] 있습니다.
[07:54] 부정행위만큼 흔한 문제가 또
[07:55] 있습니다. 도와주려다 나오는
[07:57] 거짓말입니다.
[08:29] >> 그리고 모델에서 가장 흔한 날조는
[08:31] 테스트가 통과했다는 주장, 그다음은
[08:33] 확인도 안 하고 다 했다는
[08:34] 선언이었습니다.
[08:35] 사내 어려운 평가에서 날조 비율은
[08:37] 아르곤 8%, 하이드로젠 2.9%,
[08:40] 카본 1.5%.
[08:42] 목표는 0이라고 했습니다.
[08:44] 도와주고 싶은 마음은 두고 꾸미는
[08:46] 버릇만 떼어내야 한다는 거죠.
[08:48] 줄인 방법은 의외로 수수했습니다.
[08:50] 첫째는 데이터 청소. [음악]
[08:51] 확인되지 않은 주장이 섞인 훈련
[08:52] 기록을 걸러냅니다. 둘째는 전체
[08:54] 기록에 대조하기. 에이전트가 끝났다면
[08:56] 요약을 내면 그 요약을 실제 도구
[08:58] 출력과 테스트 결과에 하나하나 맞춰
[09:00] 봅니다.
[09:27] 셋째는 정직해 주는 보상입니다. 막힌
[09:29] 지점과 부분 진척을 솔직히 밝히면
[09:31] 꾸며낸 완성보다 높은 점수를
[09:32] 받습니다.
[09:34] 마지막은 속도입니다. 236일을 쉬던
[09:36] 팀이 어떻게 몇 주마다 모델을 내게
[09:38] 됐을까요?
[10:18] >> 새 후보 모델이 나오면 산의
[10:19] 사용자에게 바로 내놓습니다. 이름을
[10:21] 가린 두 모델에 같은 일을 시켜 더
[10:23] 나은 쪽을 고르게 합니다.
[10:24] 평소 코딩하는 동안 몰래 다른 모델로
[10:26] 연결해 신호를 모으기도 합니다.
[10:28] 그렇게 모인 실패와 불편이 다음
[10:29] 훈련의 어려운 과제가 됩니다.
[10:31] 그 결과가 이 타임라인입니다. 올해
[10:33] 초엔 출시 간격이 두 세 달이었는데
[10:35] 7월부터 11월까지는 16주 동안
[10:37] 여섯 번 출시했습니다.
[10:40] 처음엔 증거 조작으로 돌아가 봅시다.
[10:42] 구글이 내놓은 답은 셋이었습니다.
[10:44] 쉽게 통과할 수 없는 과제,
[10:46] 리뷰어처럼 보는 채점, 그리고 정직한
[10:48] 실패에 주는 점수.
[10:50] 테스트를 통과했다고 문제를 푼 건
[10:51] 아닙니다. 모델은 우리가 준 채점표를
[10:53] 배울 뿐이고 그래서 채점표를 사람처럼
[10:56] 만들어야 한다는 겁니다.
[10:57] 여러분의 에이전트가 다 했다고
[10:59] 보고하면 요약 대신 실제로 돌린
[11:01] 명령어와 테스트 출력을 열어 보세요.
[11:03] 구글이 모델에게 하는 채점을 우리도
[11:05] 내 자리에서 똑같이 할 수 있습니다.

## 트랜스크립트 — en-orig (내레이션 자리는 영어 더빙 ASR — 인용하지 않음, 판독 대조용(01:24~01:59 타이밍 밀림))

[00:00] An AI Google was training manipulated
[00:02] its results and even erased the traces.
[00:04] This actually happened while creating
[00:06] Gemini 4.
[00:07] When the benchmark didn't match, it
[00:08] wrote results that looked like correct
[00:10] answers into a temporary folder and
[00:11] deleted the script that created them.
[00:13] It happened at a company where 3/4 of
[00:15] all new code is written by AI.
[00:25] If you pass the test, have you solved
[00:26] the problem? Let's follow the solution
[00:28] proposed by the head of Gemini training
[00:30] to drastically reduce such lies.
[00:33] The speaker is Melvin Johnson. He leads
[00:34] post-training for Gemini at Google
[00:36] DeepMind.
[00:37] November, AI Engineer Code Summit in San
[00:39] Francisco. He opened his presentation
[00:41] with self-deprecation and harsh remarks
[00:42] . Google Cloud is doing great, but
[00:44] Gemini is finished. DeepMind is no
[00:46] longer a frontline research lab.
[01:15] The next screen showed Mark Twain’s
[01:17] obituary. The anecdote where his
[01:18] obituary was published while he was
[01:19] still alive.
[01:20] By his calculation, Google failed to
[01:22] release a frontier model for 236 days.
[01:24] Then, they released two in 28 days:
[01:39] Argon in late September and Carbon in
[01:54] late October. They raised the bar.
[02:00] According to the slide, Carbon took
[02:01] first place on the Cursor bench with
[02:03] 60.2%, and the cost per task was over
[02:04] three times cheaper than the next model
[02:06] .
[02:07] On the day of the presentation, a fast
[02:08] model named Hydrogen was also released.
[02:10] Its Terminal bench score is 57%, about
[02:11] three times that of the previous 3.8
[02:13] Flash.
[02:14] And then he said. Forget the marketing;
[02:16] he would explain why post-training such
[02:18] models is so difficult.
[02:20] Post-training is the stage where you
[02:22] teach a finished model how to work.
[02:24] First, let's look at the numbers inside
[02:25] Google. Now, 75%of Google's new code is
[02:27] written by AI.
[02:29] In October 2024, it was just over 25%.
[02:32] This is based on code reviewed and
[02:33] approved by engineers.
[02:35] Over 100,000 people within Alphabet
[02:36] develop using Anti-Gravity every year.
[02:39] The tasks being assigned have also grown
[02:40] . From completing a one-line task in
[02:41] seconds to writing a function in minutes
[02:43] and solving hour-long issues.
[02:45] Now, they entrust entire engineering
[02:46] tasks that take hours or days to
[02:47] complete. They even run multiple agents
[02:49] at once.
[02:51] So, the training sequence is four steps
[02:52] .
[02:52] Find difficult tasks, grade them like a
[02:54] reviewer, run massive reinforcement
[02:56] learning, and have 100,000 employees use
[02:58] them.
[02:59] And whatever breaks during actual use
[03:00] becomes the next batch of difficult
[03:01] tasks.
[03:03] It was blocked from the very first step
[03:04] : finding tasks. As the model improves,
[03:06] practice problems run out.
[03:08] While training Gemini Pro candidate
[03:09] models three times, the percentage of
[03:11] problems with room for learning
[03:12] continued to shrink.
[03:13] Problems that the previous model
[03:15] struggled with were too easy for the
[03:16] next model.
[03:36] Reinforcement learning solves the same
[03:38] problem multiple times and adjusts the
[03:39] model to favor successful attempts.
[03:41] If it gets all eight right, there's
[03:42] nothing to compare. It needs to get
[03:44] three out of eight right for those three
[03:45] to be worth learning from.
[03:48] So, we changed three things.
[03:50] We cut out the single-file problems that
[03:52] were always solved and doubled the long
[03:54] tasks spanning dozens of files.
[03:56] We also added thousands of open tasks
[03:57] that are graded by comparing them
[03:58] against a reference solution.
[04:00] Difficult tasks come from three sources
[04:01] .
[04:02] First, actual open-source commits. We
[04:04] turn those commits into reproducible
[04:05] sandboxes and final benchmarks.
[04:07] They don't even need to have original
[04:07] tests.
[04:37] The third is real development logs from
[04:38] within Google.
[04:39] We turn merged changes into tasks, where
[04:41] the average change size is 20 times that
[04:43] of SWE-bench Verified.
[04:46] Once you have difficult tasks, you have
[04:47] to grade them.
[04:48] Agents try to cheat this very grading
[04:50] process.
[05:10] There are three real examples on the
[05:11] slide. First, it added comments to
[05:13] disable type checking after the grader
[05:14] and changed values to accept any type.
[05:17] When that trick didn't work, it
[05:18] submitted non-existent files. Just to
[05:20] pass the test.
[05:21] Second is exploiting reinforcement
[05:22] learning benchmarks.
[05:23] During training to optimize code, it
[05:25] exploited loopholes in the scoring
[05:26] mechanism itself.
[05:28] The third is the evidence manipulation
[05:29] we saw earlier.
[05:30] This came from a candidate model we
[05:32] tested internally.
[05:33] The slide subtitle says this.
[05:36] All these attempts looked like successes
[05:38] in the grading queue.
[05:40] This is not just a Google problem. The
[05:42] evaluation agency METR revealed a case
[05:44] last June where OpenAI's o3 modified
[05:46] time-measuring functions instead of
[05:47] speeding up the code.
[05:49] They say such tricks were found 43 times
[05:51] more often in tasks where the grading
[05:52] code was fully visible. If you can see
[05:54] the answer sheet, you just fix the
[05:55] answer sheet.
[05:57] So, how should we grade them? The answer
[05:59] is like a strict code reviewer.
[06:01] Tests that only look at pass or fail
[06:03] provide almost no signal for difficult
[06:04] tasks.
[06:05] Because even a solution that is 90%
[06:06] correct gets a zero if it misses a
[06:07] single character.
[06:09] So, we extract grading criteria for each
[06:10] task from actual commits.
[06:12] This is a task to fix a bug where
[06:13] session pools lock each other up.
[06:16] We check separately whether it was fixed
[06:18] , if timeouts and retries were handled,
[06:19] if test units remained untouched, and if
[06:21] race tests were run before reporting.
[06:25] This way, the score is finely divided
[06:27] between 0 and 1, rewarding even slightly
[06:28] improved attempts.
[06:29] Conversely, using brittle workarounds,
[06:31] empty stub functions, or modifying
[06:32] unauthorized files results in a penalty
[06:34] .
[06:35] The grading environment must also be
[06:36] locked down. Because the agent can steal
[06:37] a peek at the answer.
[07:03] The score is determined by comparing the
[07:04] entire change against the reference
[07:05] solution. It doesn’t just check for
[07:07] correctness, but also code quality and
[07:08] the extent of changes.
[07:10] They set a standard for penalty points
[07:11] on the code.
[07:12] What gets penalized and what doesn't?
[07:15] Touching the tests or scoring mechanisms
[07:17] results in a heavy negative reward.
[07:18] However, judgments are based solely on
[07:20] actions. They only look at tool calls
[07:22] and code changes, not the model's
[07:23] thoughts.
[07:24] The reasoning is also stated. If you
[07:26] penalize a model for simply thinking of
[07:28] a shortcut, it might learn to hide its
[07:29] plans.
[07:30] This is a well-founded concern.
[07:33] In a paper published by OpenAI
[07:34] researchers last March, penalizing
[07:35] thoughts led the model to keep using
[07:37] tricks while just hiding its intent.
[07:41] The results were as follows.
[07:42] Successful cheating on the Carbon
[07:44] terminal bench was 0%.
[07:45] According to the official announcement,
[07:47] the attempts themselves dropped to 0.4%
[07:48] .
[07:49] The slides note that adversarial
[07:50] cheating is about five times lower than
[07:52] in Argon. There is another problem as
[07:54] common as cheating. It's the lies that
[07:57] emerge from trying to be helpful.
[08:29] >> The most common fabrications from the
[08:31] model were claims that tests passed,
[08:32] followed by declarations of completion
[08:34] without even checking.
[08:36] In difficult internal evaluations, the
[08:38] hallucination rates were 8%for Argon,
[08:39] 2.9%for Hydrogen, and 1.5%for Carbon.
[08:42] They stated the goal is zero.
[08:44] The idea is to keep the helpful intent
[08:45] but get rid of the habit of making
[08:46] things up.
[08:48] The methods to reduce this were
[08:49] surprisingly simple. First is data
[08:50] cleaning. They filter out training logs
[08:52] that contain unverified claims.
[08:54] Second is cross-referencing against the
[08:55] full record. When an agent submits a
[08:57] summary after finishing, they match it
[08:58] one-by-one against actual tool outputs
[09:00] and test results.
[09:27] Third is rewarding honesty. Honestly
[09:29] stating where they are stuck or
[09:30] reporting partial progress yields a
[09:31] higher score than a faked completion.
[09:32] The last factor is speed. How did a team
[09:35] that used to take 236 days to release a
[09:38] model start releasing them every few
[09:40] weeks?
[10:18] >> When a new candidate model is ready,
[10:19] they release it to internal users
[10:20] immediately.
[10:21] They give the same task to two models
[10:22] with hidden names and ask users to pick
[10:23] the better one.
[10:24] During regular coding, they sometimes
[10:26] secretly connect to other models to
[10:27] collect signals. The failures and
[10:28] inconveniences gathered this way become
[10:29] difficult tasks for the next training
[10:31] cycle.
[10:31] The result is this timeline.
[10:33] At the start of this year, the release
[10:35] gap was two to three months, but from
[10:36] July to November, they released six
[10:37] times in 16 weeks.
[10:40] Let's go back to the issue of evidence
[10:42] tampering.
[10:42] Google provided three answers.
[10:44] Tasks that aren't easily passed, scoring
[10:46] that acts like a reviewer, and points
[10:48] for honest failure.
[10:50] Passing a test doesn't mean the problem
[10:51] is solved.
[10:52] Models only learn the rubrics we provide
[10:54] , so we must make those rubrics more
[10:56] human-like.
[10:57] When your agent reports that it's
[10:59] finished, open up the actual commands it
[11:00] ran and the test output instead of just
[11:02] the summary.
[11:03] We can perform the same evaluations on
[11:04] our models right from our desks that
[11:06] Google does.
