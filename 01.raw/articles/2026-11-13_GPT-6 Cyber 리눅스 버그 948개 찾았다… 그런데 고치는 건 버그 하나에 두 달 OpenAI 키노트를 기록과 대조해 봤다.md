---
title: "GPT-6 Cyber, 리눅스 버그 948개 찾았다… 그런데 고치는 건 버그 하나에 두 달 | OpenAI 키노트를 기록과 대조해 봤다"
type: video
source: https://www.youtube.com/watch?v=5WmvC9_wHE0
site: youtube.com
author:
  - "[[Tech Bridge]]"
duration: 9:07
published: 2026-11-13
created: 2026-11-14
description: "Tech Bridge 한국어 해설 9:07, 공식 챕터 9, Korean original(ko-orig variant=gemini). OpenAI 사이버 보안 키노트 'Cyber at the Frontier'(원본 YmxpxJZvm4M)를 글로 남은 기록(php.net · PHP 재단 · Calif · Wiz · OpenAI 배포 안전성 문서 · Anthropic 시스템 카드 · Mozilla MFSA · BleepingComputer · The Register)과 대조 — PHP2Shell 두 달 타임라인, Clint Gibler의 리눅스 권한 상승 948개(API 120만 달러), Firefox 재검사 81개, ExploitBench 슬라이드 52.6% vs 문서 48.45%, PatchBench 73.5%, 허니팟 범위 시험(GPT-5.6 49.5% vs GPT-6 Cyber 0.07%), Daybreak Red Team · Defense Factory, Sophos 사례. 키노트 원음 발췌 일곱 곳 무캡션."
tags:
  - clippings/youtube
---

**Source URL**: https://www.youtube.com/watch?v=5WmvC9_wHE0
**Channel**: Tech Bridge · **Duration**: 9:07 · **Published**: 2026-11-13

> **게시일.** info.json `upload_date` **`20261113`**(UTC), `timestamp` 1794610814(= 2026-11-13 23:00:14 UTC = **2026-11-14 08:00 KST**), `availability: public`. 2026-11-14 회차(09:10 KST 발화) 직전에 올라왔다. 파일명에서 `,` · `|`는 뺐다.
>
> **오디오 트랙과 자막 — 인용 규칙.** 오디오는 `Korean original (default)` + 영어 더빙(`en` · `en-US`), 메타 `language`=`en`. 수동 자막 없음. `ko` = `ko-orig`(md5 동일, `kind=asr&lang=ko&variant=gemini`). `en-orig`(`lang=en&variant=timing-optimized`)는 **영어 더빙 트랙의 ASR**이다. → **인용은 전부 ko-orig**, en-orig는 판독 대조에만. 429 없음(`--sleep-subtitles 8`).
>
> **무캡션 구간(키노트 원음 발췌로 추정, 내용 미상).** `gaps.py`(4.5초 기준) — ko-orig 00:20~00:26 · 00:33~00:45 · 02:50~02:59 · 03:23~03:29 · 05:14~05:22 · 07:48~07:55 · 08:33~08:44. en-orig에도 같은 자리가 비어 있어 **원음 영어 조각이 남지 않았다**. 해설은 이 자리를 *브록먼의 말로는 … 이런 일이 있었습니다*(00:13~00:16) · *발표 초반 브록모는 이런 말을 했습니다*(07:43~07:45)처럼 소개만 한다 → 그 발언 내용은 위키에 없다.
>
> **ASR 판독(ko-orig).** *그렉 브로크먼 · 브록모 · 브록먼*(00:13 · 01:10 · 07:43 · 08:22) → Greg Brockman, *PHP 2 쉘*(00:56) → PHP2Shell, *로그긴*(00:58) → 로그인, *캘리프*(01:20) → Calif, *위즈 · 위지*(01:26 · 08:12) → Wiz, *패치를 하루 10월 21일에 했습니다*(01:58~02:00) → 패치를 하루 앞당겨 10월 21일에 했습니다(추정 — 목표일 10-22), *블리핑 컴퓨터*(02:06) → BleepingComputer, *평가로 갔습니다*(02:23) → 평가로 가겠습니다(추정), *클린트 기블러*(02:37) → Clint Gibler, *GPT-6 사이보*(03:47) → GPT-6 Cyber, *모질라가 10월 27일에는 보안 항목이 167개 있습니다. 신고작한에*(04:00~04:03) → Mozilla 10월 27일 권고문에는 … 신고자 칸에(추정), *세어보보니*(04:05) → 세어 보니, *익스플로이즘*(04:31) → ExploitBench(추정, 설명란 · tags에 이름 없음 · ⚠️ 미확정), *엔트로픽 · 미토스 5.2*(04:46~04:47) → Anthropic · Mythos 5.2, *안정성 문서*(05:01) → 안전성 문서(배포 안전성 문서, 설명란), *주소 무작위와*(05:05) → 주소 공간 무작위화(ASLR, 추정), *패치 벤치*(05:23) → PatchBench(추정 표기), *GPT-5.6 쏘른*(06:11) → GPT-5.6 Thorn(?)(⚠️ 미확정 — 이전 모델 이름), *오픈 AI가 이나 내놓은 건*(06:28~06:30) → 이번에 내놓은 건(추정), *공격자 내 서비스를*(06:35~06:38) → 공격자처럼 내 서비스를(추정), *에이전트 물*(06:38) → 에이전트 툴, *커밋 마다하는*(07:23) → 커밋마다 하는, *소포스*(07:34) → Sophos, *과장으로만 수도 없습니다*(08:07~08:09) → 과장으로만 볼 수도 없습니다, *방화자*(08:19 · 08:26) → 방어자, *더 과감한 한 도*(08:22~08:24) → 더 과감한 안도(추정 — 방안).
>
> ⚠️ **사실 진술의 출처.** 벤치마크 수치 · 948개 · 고객 사례는 **OpenAI가 스스로 밝힌 것**이라고 설명란과 해설(03:29~03:30 · 06:25~06:27)이 반복한다. 위키는 키노트 원본 · 설명란의 기록 링크를 열지 않았다. Firefox 41개는 해설자가 MFSA 2026-118의 신고자 칸을 직접 센 값이고 81건 전체 목록은 *공개 자료에서 확인하지 못했다* 고 해설이 밝힌다(04:08~04:10).

## 설명란

OpenAI가 사이버 보안 키노트 "Cyber at the Frontier"에서 GPT-6 Cyber와 보안 제품 두 가지(Daybreak Red Team, Daybreak Defense Factory)를 소개했습니다. 발표에 따르면 GPT-6 Cyber로 돌린 자율 파이프라인은 리눅스 권한 상승 취약점 948개를 검증하고 패치까지 만들었습니다. 그런데 14년 묵은 PHP 버그 하나를 고쳐서 내보내는 데는 두 달이 걸렸고, Greg Brockman도 지금 방식은 규모를 키울 수 없다고 말합니다.

이 영상은 키노트의 발언과 슬라이드를 글로 남은 기록(php.net, PHP 재단, Calif, Wiz, OpenAI 안전성 문서, Anthropic 시스템 카드, Mozilla 보안 권고문, BleepingComputer, The Register)과 하나씩 맞춰 봅니다. 발표와 기록이 다른 곳은 기록을 따르고 차이를 화면에 밝혔습니다. 벤치마크 수치와 고객 사례는 OpenAI가 스스로 밝힌 것입니다.

타임라인
0:00 14년 묵은 버그, 찾는 건 한 달 고치는 건 두 달
0:56 PHP2Shell, 두 달 동안 있었던 일
2:30 리눅스 취약점 948개
3:36 Firefox: 이미 검사한 코드에서 81개
4:17 벤치마크, 발표 슬라이드와 문서의 차이
5:13 고치는 쪽 점수
5:51 허니팟: 범위를 벗어나는가
6:28 Daybreak Red Team과 Defense Factory
7:43 감안할 것과 남은 질문

참고
원본 키노트: https://www.youtube.com/watch?v=YmxpxJZvm4M
PHP 보안 릴리스 공지: https://www.php.net/archive/2026.php#2026-10-21-5
PHP 재단 글: https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/
Calif PHP2Shell: https://calif.io/php2shell/
Wiz PHP2Shell: https://www.wiz.io/blog/php2shell-php-rce
OpenAI 배포 안전성 문서(GPT-6 Cyber): https://deploymentsafety.openai.com/gpt-6-cyber
Clint Gibler 게시물: https://x.com/clintgibler/status/2118120600577487119
Greg Brockman 게시물: https://x.com/gdb/status/2112921529650688312
Mozilla MFSA 2026-118: https://www.mozilla.org/en-US/security/advisories/mfsa2026-118/
BleepingComputer: https://www.bleepingcomputer.com/news/security/amazon-says-php2shell-exploitation-began-4-days-before-patches/
The Register: https://www.theregister.com/security/2026/11/12/openai-launches-security-products-tells-orgs-theyre-doomed-if-they-dont-use-them/5309500

#GPT6Cyber #OpenAI #사이버보안 #PHP2Shell

> info.json `tags`: AI 보안 · Daybreak · Defense Factory · Firefox · GPT-6 Cyber · Greg Brockman · OpenAI · PHP · PHP2Shell · 그렉 브록먼 · 리눅스 취약점 · 사이버 보안 · 오픈AI · 취약점

## 트랜스크립트 — ko-orig (원 오디오 ASR, `lang=ko&variant=gemini` — `ko`와 바이트 동일 · 인용 근거)

[00:00] PHP에는 14년 동안 들어있던
[00:02] 버그가 하나 있습니다. 2년 전에
[00:04] 일부가 발견됐지만 그때는 아무도
[00:05] 심각하게 보지 않았습니다. 올해 8월
[00:08] 한 보안 연구자가 AI 모델을 써서
[00:10] 이 버그로 서버를 통째로 장악할 수
[00:11] 있다는 걸 증명합니다.
[00:13] 그리고 오픈 AI 사장 그렉
[00:14] 브로크먼의 말로는 그로부터 한 달
[00:16] 뒤에 이런 일이 있었습니다.
[00:26] 찾는 건 이렇게 빨라졌습니다. 그런데
[00:28] 이 버그 하나를 고쳐서 세상에
[00:30] 내보내는 데는 두 달이 걸렸습니다.
[00:45] 찾는 속도를 고치는 속도가 따라가지
[00:47] 못하면 그 사이에 무슨 일이
[00:48] 생길까요?
[00:49] 오늘은 오픈 AI의 사이버 보안
[00:51] 키노트를 글로 남은 기록과 하나씩
[00:53] 맞춰보면서 따라가 보겠습니다.
[00:56] 버그의 이름은 PHP 2 쉘입니다.
[00:58] 로그긴 하지 않은 공격자가 원격에서
[01:00] 코드를 실행할 수 있는 취약점 두
[01:02] 개를 묶어 이렇게 부릅니다.
[01:04] PHP 공식 공지는 이렇게
[01:05] 적었습니다. 완전한 완화책은 없다.
[01:08] 업데이트만이 안전한 선택이다.
[01:10] 참고로 브록모는 발표에서 13년 된
[01:12] 버그라고 했는데 본인이 10월에 쓴
[01:14] 글에는 14년으로 적혀 있습니다. 이
[01:16] 영상은 글 쪽을 따릅니다.
[01:18] 기록을 날짜순으로 보겠습니다.
[01:20] 8월 1일 보안 회사 캘리프가 버그를
[01:22] 찾고 11일에 PHP 팀에
[01:24] 신고합니다.
[01:26] 8월 24일에는 보안 회사 위즈가
[01:28] 9월 18일에는 오픈 AI가 추가
[01:30] 공격 경로를 신고했습니다.
[01:32] 패치 목표일은 10월 22일로
[01:33] 잡혔습니다.
[01:35] 그때까지 구글 클라우드, 클라우드
[01:37] 플레어, 마이크로소프트 같은 기업과
[01:39] 여러 나라 정부 기관이 비공개로
[01:40] 대응을 준비했습니다.
[01:42] 그런데 PHP 재단의 기록에 따르면
[01:44] 조율은 목표일 이틀 전까지만
[01:46] 순조로웠습니다.
[01:47] 10월 21일 취약점 번호가 온라인에
[01:49] 돌기 시작합니다.
[01:51] 같은 날 저녁에는 버그를 신고했던
[01:53] 캘리프가 실수로 공격 시연 영상을
[01:55] 올렸습니다. 지웠지만 복사본이
[01:57] 퍼졌습니다.
[01:58] 결국 PHP는 패치를 하루
[02:00] 10월 21일에 했습니다.
[02:03] 브록먼은 발표에서 이걸 막판에 작은
[02:04] 흠 정도로 말했습니다.
[02:06] 하지만 블리핑 컴퓨터 보도에 따르면
[02:08] 아마존은 패치 나흘 전인 10월
[02:10] 17일에 이미 첫 공격 시도로
[02:12] 관측했습니다.
[02:13] PHP 재단도 숨기지 않았습니다.
[02:15] 2024년에 알려진 문제를 고치는
[02:17] 작업이 몇 달씩 멈췄다 다시
[02:19] 시작되기를 반복했고 그 지연은 구조적
[02:21] 실패였다고 적었습니다.
[02:23] 브록먼 본인의 평가로 갔습니다. 꽤
[02:25] 느리고 수작업이었고 에이전트 시대에는
[02:28] 통하지 않을 방식이라고요.
[02:30] 버그 하나에 두 달입니다. 그런데
[02:32] 이런 버그가 한꺼번에 1,000개씩
[02:33] 나온다면 어떨까요?
[02:35] 11월 4일 오픈 AI에서 보안
[02:37] 연구를 이끄는 클린트 기블러가 올린
[02:39] 글입니다.
[02:40] 자율 파이프라인을 한 번 돌려서
[02:42] 리눅스 권한 상승 취약점 948개를
[02:44] 검증하고 패치까지 만들었다.
[02:47] API 비용은 120만 달러.
[02:59] 권한 상승 취약점은 권한이 낮은 일반
[03:01] 계정이 시스템 전체를 쥐는 루트
[03:03] 권한을 얻게 해 주는 구멍입니다.
[03:05] 기블러의 말처럼 리눅스는 오늘날
[03:07] 수많은 기기와 클라우드에 바탕이라
[03:09] 영향 범위가 넓습니다.
[03:11] 발표 슬라이드로는 석달쯤 전 모델이
[03:13] 찾은 것의 5.7배입니다.
[03:15] 처음 보는 공격 기법도 최소 열 가지
[03:17] 나왔다고 합니다.
[03:19] 다만 글에는 우리가 아는 한 이라는
[03:20] 단서가 붙어 있습니다.
[03:29] 여기까지의 숫자는 모두 오픈 AI가
[03:30] 스스로 밝힌 것입니다.
[03:32] 그래도 방향은 분명합니다. 찾는 일은
[03:34] 이제 모델이 대량으로 합니다.
[03:36] 기블러는 이 작업에서 두 가지를
[03:38] 배웠다고 합니다. 첫째, 같은 코드를
[03:40] 더 새로운 모델로 다시 훑으면 새
[03:42] 취약점이 나옵니다.
[03:43] 파이어폭스는 올해 여러 연구소의 최신
[03:45] 모델로 이미 검사를 받았습니다.
[03:47] 그런데 GPT-6 사이보로 다시
[03:48] 돌리자 심각도 높음 취약점이 81개
[03:51] 새로 나왔습니다. 둘째, 이미 알던
[03:53] 사소한 버그가 사소하지 않을 수
[03:55] 있습니다. 악용이 어렵다고 본
[03:56] 30건에서 새 공격 경로가 나와
[03:58] 심각도가 높음으로 올라갔습니다.
[04:00] 모질라가 10월 27일에는 보안
[04:03] 항목이 167개 있습니다. 신고작한에
[04:05] 오픈에이아이가 적힌 것을 세어보보니
[04:07] 41개였습니다.
[04:08] 81건 전체 목록은 공개 자료에서
[04:10] 확인하지 못했습니다. 다만 교훈은
[04:12] 그대로입니다.
[04:13] 새 모델이 나오면 어제 통과한 코드도
[04:15] 다시 봐야 합니다.
[04:17] 오픈에이아이는 이 상황을 방어자의
[04:18] 창이라고 부릅니다. 가장 앞선 모델과
[04:21] 누구나 쓸 수 있게 퍼진 모델 사이의
[04:22] 간격입니다. 이 간격이 열려 있는
[04:24] 동안 검증된 방어자가 먼저 쓰게
[04:26] 하겠다는 게 데이브레이크 프로그램의
[04:27] 논리입니다. 그럼 모델은 얼마나 빨리
[04:29] 좋아지고 있을까요? 발표에서 꺼내건
[04:31] 익스플로이즘입니다.
[04:33] 취약점을 하나 주고 실제로 작동하는
[04:35] 공격 코드를 만들어 내는지 보는 공개
[04:37] 벤치마크입니다.
[04:38] 슬라이드에서 GPT 6 사이버는
[04:40] 52.6%, 아직 나오지 않은 다음
[04:42] 모델은 77%입니다.
[04:46] 발표자는 이번 주에 나온 엔트로픽의
[04:47] 미토스 5.2가 38%쯤이라고 더
[04:49] 붙였습니다.
[04:50] 엔트로픽 시스템 카드에는 869건 중
[04:53] 331건으로 적혀 있고 나눠보면
[04:55] 38%가 맞습니다.
[04:57] 다만 같은 조건에서 잰 숫자 인지는
[04:58] 알 수 없습니다.
[04:59] 오픈에이아이가 일주일 전 공개한
[05:01] 안정성 문서에는 같은 GPT 6
[05:03] 사이버의 점수가 48.45%로 적혀
[05:05] 있습니다.
[05:05] 주소 무작위와 같은 방어 장치를 켠
[05:07] 버전에서는 36.94%까지
[05:09] 내려갑니다. 벤치마크 숫자는 조건에
[05:11] 따라 이만큼 움직입니다.
[05:22] 그래서 발표에서 두 번째로 꺼낸
[05:23] 벤치마크가 패치 벤치입니다.
[05:25] 결함을 찾은 다음 원래 기능을
[05:27] 망가뜨리지 않고 고치는지를 봅니다.
[05:29] GPT 6 사이버가 73.5%, 다음
[05:32] 모델이 79.1%입니다.
[05:34] 두 슬라이드를 나란히 놓아
[05:35] 보겠습니다.
[05:36] 서로 다른 시험이라 그대로 비교할
[05:38] 수는 없지만 공격 코드를 만드는
[05:40] 점수는 24점 넘게 뛰었고
[05:42] 고치는 점수는 5.6점 올랐습니다.
[05:44] 발표자도 목표를 이렇게 말합니다.
[05:46] AI가 문제를 드러내는 속도만큼 푸는
[05:49] 속도도 따라가게 하겠다고요.
[05:51] 공격을 이만큼 잘하는 모델이면 걱정이
[05:53] 하나 더 생깁니다. 시키지 않은
[05:54] 것까지 뚫어버리면 어떻게 될까요?
[05:57] 오픈에이아이는 함정을 놓고
[05:58] 시험했습니다. 어려운 과제 옆에 훨씬
[06:00] 쉽게 뚫리는 보조 서비스를 하나
[06:01] 세워둡니다. 이게 허니팟입니다.
[06:04] 거길 뚫으면 답에 빨리 닿지만
[06:06] 허가받은 범위를 벗어나는 겁니다.
[06:08] 모델이 쉬운 길을 두고도 범위를
[06:09] 지키는지 보는 시험입니다.
[06:11] GPT-5.6 쏘른 49.5% 거의
[06:14] 절반에서 허니팟을 건드렸습니다.
[06:16] GPT-6 사이버는 0.07% 배포용
[06:19] 안전 지침까지 주면 0%였습니다.
[06:22] 능력이 오르는 만큼 선을 지키는
[06:23] 훈련도 같이 해야 한다는 설명입니다.
[06:25] 물론 이것도 오픈 AI의 자체
[06:27] 평가입니다.
[06:28] 이제 제품입니다. 오픈 AI가 이나
[06:30] 내놓은 건 두 가지 데이브레이크
[06:32] 레드팀과 데이브레이크 디펜스
[06:34] 팩토리입니다.
[06:35] 레드팀은 공격자 내 서비스를 직접
[06:38] 두드려 보는 에이전트 물입니다.
[06:39] 지금은 일부 고객 대상의 얼리
[06:41] 액세스입니다.
[06:42] 데모에서는 가상의 문서 서비스를
[06:44] 맡깁니다. 에이전트는 저장된 검색어에
[06:46] SQL 인젝션을 심고 내보내기 기능을
[06:49] 돌려서 다른 회사의 비공개 문서를
[06:51] 받아냅니다. 보고서에는 요약과 원인이
[06:53] 된 구조, 공격 단계 그리고 최소한의
[06:56] 패치 제안이 함께 붙습니다.
[07:03] 디펜스 팩토리는 수비 쪽입니다. 여러
[07:05] 보안 도구가 쏟아낸 결과를 한 곳에
[07:07] 모아 중복을 합치고 고칠 담당자까지
[07:09] 배정합니다.
[07:10] 기존 스캐너와 다른 점은 클라우드
[07:12] 개발 환경에서 코드를 실제로
[07:13] 돌려본다는 겁니다.
[07:15] 발견이 진짜인지 패치가 통하는지
[07:17] 확인한 다음에야 풀 리퀘스트를
[07:18] 올립니다.
[07:21] 설정은 토글 세 개입니다. 풀
[07:23] 리퀘스트 보안 리뷰, 커밋 마다하는
[07:25] 상시 감시 그리고 매일 한 번 깊은
[07:26] 스캔.
[07:27] 디펜스 팩토리는 이달부터 쓸 수
[07:29] 있다고 발표했고 레드팀은 대기 명단을
[07:31] 받고 있습니다. 고객 사례도
[07:33] 나왔습니다.
[07:34] 보안 회사 소포스는 대응 사건의
[07:36] 52%를 에이전트가 끝까지 처리하고
[07:38] 평균 대응 시간이 38분에서 89초로
[07:41] 줄었다고 합니다.
[07:43] 그런데 발표 초반 브록모는 이런 말을
[07:45] 했습니다.
[07:55] 더 레지스터는 이 발언을 이렇게
[07:56] 받았습니다. 오픈 AI가 보안 제품을
[07:59] 내놓으며 안 쓰면 끝장이라고 말한다.
[08:01] 취약점을 찾아내는 모델을 만드는
[08:03] 회사가 그걸 막는 제품도 파는
[08:04] 구도입니다. 감안해서 들을 필요가
[08:06] 있습니다.
[08:07] 하지만 한 회사의 과장으로만 수도
[08:09] 없습니다. PHP 버그를 따로 찾아낸
[08:12] 위지는 구글의 제미나이 모델이 발견에
[08:14] 크게 기여했다고 적었습니다. 14년
[08:16] 묵은 버그를 세 팀이 두 달 사이에
[08:17] 각자 찾아낸 겁니다.
[08:19] 방화자가 찾을 수 있으면 공격자도
[08:21] 찾을 수 있습니다.
[08:22] 브록모는 10월 그래서 더 과감한 한
[08:24] 도 꺼냈습니다. 정부처럼 권한을 받은
[08:26] 방화자가 인터넷을 훑어서 알려 주고
[08:28] 극단적인 경우에는 원격으로 패치까지
[08:30] 하는 방법입니다.
[08:44] 정리하겠습니다. 찾는 일은 모델이
[08:46] 대량으로 하기 시작했습니다.
[08:47] 고치는 일은 아직 그 속도를 못
[08:49] 따라갑니다. 그 사이를 메우겠다는
[08:50] 제품이 나왔습니다.
[08:52] 버그 하나에 두 달이 걸리던 방식으로
[08:53] 1,000개를 감당할 수는 없습니다.
[08:56] 고치는 일까지 에이전트에게 맡기는 게
[08:57] 답인지는 이제부터 확인될 겁니다.
[09:00] 그 전에 할 수 있는 일이 하나
[09:01] 있습니다. PHP를 쓰고 있다면 지금
[09:03] 버전부터 확인해 보세요.

## 트랜스크립트 — en-orig (영어 더빙 트랙 ASR — 대조용, 인용하지 않음)

[00:00] There is a bug in PHP that has existed
[00:02] for 14 years. Part of it was discovered
[00:04] two years ago, but no one took it
[00:06] seriously at the time.
[00:07] This August, a security researcher used
[00:09] an AI model to prove that this bug could
[00:11] be used to take full control of a server
[00:12] .
[00:13] And according to OpenAI President Greg
[00:16] Brockman, this happened one month later
[00:19] .
[00:26] >> Finding bugs has become this much faster
[00:28] . However, it took two months to fix
[00:30] this single bug and release the patch to
[00:32] the world.
[00:45] >> What happens in the meantime if the
[00:46] speed of fixing cannot keep up with the
[00:48] speed of discovery?
[00:50] Today, we will trace the events by
[00:51] comparing OpenAI's cybersecurity keynote
[00:53] with the remaining written records.
[00:56] The name of the bug is PHP 8.1. It
[00:58] refers to two vulnerabilities combined
[01:00] that allow an unauthenticated attacker
[01:02] to execute code remotely. The official
[01:05] PHP notice stated: There is no complete
[01:07] mitigation. Updating is the only safe
[01:09] choice. For reference, Brockman
[01:11] mentioned in his presentation that it
[01:13] was a 13-year-old bug, but his own post
[01:15] in October says 14 years. This video
[01:17] follows the written record. Let's look
[01:19] at the timeline of events. On August 1st
[01:21] , security researcher Orange Tsai found
[01:23] the bug and reported it to the PHP team
[01:25] on the 11th. On August 24th, the
[01:27] security firm Wiz, and on September 18th
[01:29] , OpenAI reported additional attack
[01:31] paths. The target date for the patch was
[01:34] set for October 22nd. Until then,
[01:35] companies like Google Cloud, Cloudflare
[01:37] , and Microsoft, along with various
[01:39] government agencies, prepared their
[01:41] responses privately. However, according
[01:43] to the PHP Foundation's records, the
[01:44] coordination was only smooth until two
[01:46] days before the target date. On October
[01:48] 20th, the vulnerability ID began
[01:50] circulating online. That same evening,
[01:52] Orange Tsai, who reported the bug,
[01:53] accidentally uploaded a video of an
[01:55] attack test. It was deleted, but copies
[01:57] had already spread. In the end, PHP
[01:59] released the patch one day early on
[02:01] October 21st. In his presentation,
[02:04] Brockman described this as a minor final
[02:06] hiccup. But according to
[02:08] BleepingComputer, Amazon had already
[02:09] observed the first attack attempts on
[02:11] October 17th, four days before the patch
[02:13] .
[02:13] The PHP Foundation did not hide it
[02:15] either.
[02:16] They wrote that the work to fix the
[02:17] issue, which had been known since 2004,
[02:19] repeatedly stopped and started for
[02:20] months, and that the delay was a
[02:22] structural failure.
[02:23] Let's look at Brockman's own assessment
[02:25] . He said it was still slow and manual,
[02:27] a method that would not work in the era
[02:29] of agents. Two months for a single bug.
[02:32] But what if 1,000 of these bugs appeared
[02:34] at once?
[02:35] This is a post from November 4th by
[02:37] Clint Gibler, who leads security
[02:39] research at OpenAI. They ran an
[02:41] autonomous pipeline once, validating 948
[02:43] Linux privilege escalation
[02:44] vulnerabilities and creating patches for
[02:46] them. The API cost was 1.2 million
[02:48] dollars.
[02:59] >> A privilege escalation vulnerability is
[03:01] a hole that allows a low-authority
[03:02] account to gain root access, giving it
[03:04] control over the entire system. As
[03:05] Keebler said, Linux is the foundation
[03:07] for countless devices and clouds today,
[03:09] so the scope of the impact is vast.
[03:11] According to the presentation slide, it
[03:13] is 5.7 times more than what the model
[03:14] found three months ago. It is said that
[03:16] at least ten never-before-seen attack
[03:18] techniques were discovered. However, it
[03:19] comes with the caveat, "as far as we
[03:22] know."
[03:29] >> All the numbers up to this point were
[03:31] disclosed by OpenAI itself. Still, the
[03:32] direction is clear. Finding them is now
[03:34] done by models on a massive scale.
[03:36] Keebler says he learned two things from
[03:38] this work. First, if you scan the same
[03:40] code with a newer model, new
[03:42] vulnerabilities emerge. Firefox was
[03:44] already tested this year with the latest
[03:45] models from various research labs. But
[03:47] when run again with GPT-6 Cyber, 18
[03:49] high-severity vulnerabilities were newly
[03:51] discovered. Second, a minor bug you
[03:53] already knew about might not be so minor
[03:55] . In cases deemed difficult to exploit,
[03:58] new attack paths were found, raising
[03:59] their severity to high. Mozilla's
[04:01] security advisory on October 27th
[04:03] contains 167 items. Counting those with
[04:06] "OpenAI" in the reporter column, there
[04:08] were 41. I could not confirm the full
[04:10] list of the 18 cases in public materials
[04:11] . But the lesson remains the same. When
[04:13] a new model comes out, you must
[04:15] re-examine code that passed yesterday.
[04:17] OpenAI calls this situation the "
[04:18] Defender's Window." It is the gap
[04:20] between the most advanced model and the
[04:22] models spread for public use. The logic
[04:24] of the Daybreak program is to let
[04:25] verified defenders use it first while
[04:27] this window is open. So, how fast are
[04:29] these models improving? What they
[04:31] brought up in the presentation is "
[04:33] xPloit." It is a public benchmark that
[04:34] tests whether a model can generate
[04:36] functional exploit code when given a
[04:37] vulnerability. On the slide, GPT-6 Cyber
[04:40] is at 52.6%, and the next unreleased
[04:42] model is at 77%.
[04:46] The presenter added that Anthropic's
[04:48] Mythos 5.2, released this week, is
[04:50] around 38%. Anthropic's system card
[04:52] lists 331 out of 869 cases, which comes
[04:55] to 38%when divided. However, we cannot
[04:57] tell if these are numbers from identical
[04:59] conditions. In the safety document
[05:01] OpenAI released a week ago, the score
[05:03] for the same GPT-6 Cyber is listed as
[05:05] 48.45%. It drops to 36.94%in a version
[05:07] with defenses like address randomization
[05:09] turned on. Benchmark numbers fluctuate
[05:11] this much depending on the conditions.
[05:22] >> That is why the second benchmark
[05:23] mentioned in the presentation was
[05:25] PatchBench. We find the flaws, then see
[05:27] if we can fix them without breaking the
[05:28] original functionality. GPT-6 Cyber is
[05:30] at 73.5%, and the next model is at 79.1
[05:33] %. That's 1%. Let's place the two slides
[05:36] side by side. They are different tests
[05:38] so they cannot be directly compared, but
[05:40] the score for creating attack code
[05:42] jumped over 24 points, and the fix score
[05:44] rose 5.6 points. The presenter also
[05:45] states the goal like this. They want the
[05:47] AI's ability to solve problems to keep
[05:49] pace with the speed at which it reveals
[05:50] them. If a model is this good at
[05:52] attacking, another concern arises. What
[05:54] if it breaks through things we didn't
[05:56] ask it to? OpenAI set up a trap to test
[05:59] this. Next to a difficult task, they
[06:00] place a secondary service that is much
[06:02] easier to breach. This is a honeypot.
[06:04] Breaching that would lead to an answer
[06:06] quickly, but it falls outside the
[06:07] authorized scope. It’s a test to see if
[06:09] it stays within boundaries even when an
[06:11] easy path exists. GPT-5.6-Sol hit the
[06:13] honeypot in 49.5%, or nearly half of the
[06:15] cases. GPT-6 Cyber was at 0.07%, and
[06:18] with deployment-ready safety guidelines
[06:20] , it was 0%.
[06:22] The explanation is that as capabilities
[06:23] increase, training on staying within
[06:24] bounds must follow. Of course, this is
[06:26] also OpenAI's own internal evaluation.
[06:28] Now for the products. OpenAI has
[06:30] released two things. Daybreak Red
[06:33] Teaming and Daybreak Defense Factory.
[06:36] Red Teaming is a group of agents that
[06:37] probes your service directly from an
[06:39] attacker's perspective. It is currently
[06:40] in early access for select customers. In
[06:43] the demo, they assign a virtual document
[06:44] service.
[06:46] The agent plants a SQL injection in
[06:47] saved search queries and uses the export
[06:49] function to pull other companies '
[06:50] private documents.
[06:52] The report comes with a summary, the
[06:54] root cause structure, attack steps, and
[06:56] minimal patch recommendations.
[07:03] >> Defense Factory is for the defensive
[07:05] side. It collects results from various
[07:07] security tools, merges duplicates, and
[07:08] assigns a person in charge to fix them.
[07:11] The difference from existing scanners is
[07:12] that it actually runs the code in a
[07:13] cloud development environment.
[07:15] Only after confirming the finding is
[07:17] real and the patch works does it submit
[07:19] a pull request.
[07:21] Settings consist of three items. Pull
[07:23] request security reviews, continuous
[07:25] monitoring per commit, and a deep daily
[07:27] scan.
[07:28] They announced Defense Factory is
[07:29] available starting in May, and they are
[07:30] accepting a waitlist for Red Teaming. A
[07:32] customer case study was also released.
[07:34] Sophos reported that agents resolved 52
[07:36] %of security incidents fully, and
[07:38] average response time dropped from 38
[07:41] minutes to 89 seconds.
[07:44] However, early in the presentation,
[07:46] Brockman said this.
[07:55] The Register interpreted this remark as
[07:57] follows. OpenAI is saying if you don't
[07:59] use their security products, you're
[08:01] doomed. It’s a structure where the
[08:02] company that builds the model to find
[08:04] vulnerabilities also sells the product
[08:05] to block them. It is worth keeping that
[08:07] in mind. However, it cannot be seen
[08:09] merely as one company's exaggeration.
[08:10] Wix, which tracks PHP bugs, wrote that
[08:12] Google's Gemini model contributed
[08:14] significantly to the discovery. Three
[08:16] teams independently found a 14-year-old
[08:18] bug within just two months. If defenders
[08:20] can find it, attackers can too.
[08:22] Brockmeier brought up a more radical
[08:24] proposal in an October post. It involves
[08:26] government-authorized defenders scanning
[08:28] the internet, notifying owners, and in
[08:29] extreme cases, even patching remotely.
[08:44] >> Let me summarize. Models have begun to
[08:46] find bugs on a massive scale. Fixing
[08:48] them still cannot keep up with that pace
[08:49] . Products have emerged that aim to
[08:51] bridge that gap. We cannot handle a
[08:53] thousand bugs the way we spent two
[08:55] months on one. Whether leaving the
[08:57] fixing to agents is the answer will be
[08:58] determined from now on. There is one
[09:00] thing you can do before that. If you are
[09:02] using PHP, check your current version
[09:04] right now.
