---
title: "바이브 코딩 vs 에이전틱 코딩, 무엇을 써야 할까? | Grace Ableidinger"
type: video
source: https://www.youtube.com/watch?v=awaU-RwDdgg
site: youtube.com
author:
  - "[[Tech Bridge]]"
duration: 8:50
published: 2026-11-24
created: 2026-11-25
description: "Tech Bridge 한국어 해설 8:50, 공식 챕터 9, 한국어 내레이션(ko-orig) + 영어 더빙 ASR(en-orig — 인용하지 않음). IBM Technology 영상에서 Red Hat의 Grace Ableidinger가 라이트보드에 그려 가며 비교한 바이브 코딩과 에이전틱 코딩을 Andrej Karpathy의 X 글 · IBM Think 글과 함께 정리 — 전부 수락하고 읽지 않는 코딩, 시제품에는 맞고 프로덕션으로 넘어갈 때 드러나는 문제, 프롬프트 → 생성 → 반복의 짧은 고리와 이해 → 계획 → 실행 → 테스트 → 검증의 긴 고리, 걸러 낸 컨텍스트와 서브에이전트, 안전 장치 다섯(테스트 · 거버넌스 · 관찰 가능성 · 롤백 · 가드레일), 작업을 가르는 질문 넷. ⚠️ Grace Ableidinger의 원음은 두 트랙 모두 무캡션(발췌 자리 아홉 곳, 약 2분 50초) — 본인 인용 0건. ⚠️ 영어 더빙은 화자를 다른 이름(Edidiong Asikpo)으로 읽는다."
tags:
  - clippings/youtube
---

**Source URL**: https://www.youtube.com/watch?v=awaU-RwDdgg
**Channel**: Tech Bridge · **Duration**: 8:50 · **Published**: 2026-11-24

> **게시일.** info.json `upload_date` **`20261124`**, `timestamp` 1795557615(= 2026-11-24 22:00:15 UTC = **2026-11-25 07:00 KST**), `availability`=`public`. 2026-11-25 회차(09:10 KST)에서 처음 잡혔다 — 게시 두 시간 뒤. `upload_date`는 UTC 기준이라 KST 날짜보다 하루 앞선다. 파일명에서 `|` 와 `?` 는 뺐다.
>
> **오디오 트랙과 자막 — 인용 규칙.** ⚠️ 이 회차에는 yt-dlp가 영상 포맷 목록을 받지 못해(*The page needs to be reloaded* · *Only images are available*) **오디오 트랙 구성과 메타 `language`(`None`)를 info.json으로 확인하지 못했다.** 자막 트랙의 성격은 내용으로 판정했다. 수동 자막 없음. `ko` = `ko-orig`(파일 동일, `kind=asr&lang=ko&variant=gemini`) — **한국어 내레이션** 이다. `en-orig`(`kind=asr&lang=en&variant=timing-optimized`)는 **영어 더빙의 ASR** 이다 — 첫 줄부터 내레이션의 영어 번역이고(*"The person who coined the term "vibe coding" wrote that they don't read the code."*) 문장 단위가 ko-orig와 같은 초에 맞물린다. **en-orig는 인용하지 않았고 판독 대조용으로만 썼다.** 한국어 인용은 전부 ko-orig의 내레이션이다. 429 없음(`--sleep-subtitles 8`).
> ⚠️ **Grace Ableidinger의 원음은 한 줄도 캡션에 없다.** 원 영상 발췌로 보이는 자리는 두 트랙 모두 비어 있고 ko-orig에는 `[음악]` 표시만 남았다. **본인의 말을 글자 그대로 인용한 것은 0건이다.**
>
> **무캡션 구간(`gaps.py` 4.5초 기준).** en-orig 아홉 곳: 00:18~00:25 · 00:55~01:09 · 02:05~02:41 · 03:10~03:36 · 04:35~04:48 · 05:08~05:33 · 06:11~06:34 · 07:12~07:30 · 08:34~08:44 — 합쳐 약 2분 50초. ko-orig는 같은 자리가 `[음악]` 표시로 잘게 나뉘어 열다섯 조각으로 잡힌다(00:18~00:25 · 01:00~01:09 · 02:05~02:13 · 02:15~02:19 · 02:21~02:27 · 02:29~02:35 · 03:15~03:21 · 03:23~03:28 · 04:35~04:48 · 05:08~05:15 · 05:17~05:28 · 06:11~06:21 · 06:23~06:27 · 07:18~07:26 · 08:39~08:44).
> ⚠️ **이 구간들은 내용 미상이다.** 여기에 드는 것: 도입부 발췌(00:18~00:25) · **개발자들의 반응이 무엇이었는지(00:55~01:09)** · *리뷰* 라는 낱말 뒤의 설명(02:05~02:40) · 코딩 에이전트 설명 뒤의 발췌(03:10~03:36 — 서브에이전트가 처음 나오는 자리로 보인다. 뒤에서 내레이션이 *앞에서 본 서브 에이전트* 라고 받는다) · 긴 고리 뒤의 발췌(04:35~04:48 — 뒤에서 *앞에서 말한 사람의 분별력* 이라고 받는다) · **컨텍스트가 많으면 왜 안 되는지(05:08~05:33)** · 보안 문제의 내용(06:11~06:33) · **질문 네 개의 원 표현(07:12~07:30)** · **마지막 조언(08:34~08:44)**. 내레이션이 앞뒤로 받아 적은 줄만 남아 있다.
>
> **ASR 판독(ko-orig → 판독, 괄호는 근거).** *오픈에이아이* → OpenAI, *안드레이 카파시* → Andrej Karpathy(설명란 · tags), *에이아이와 고친 코드*(00:08) → AI가 고친 코드(설명란 *AI가 고친 코드를 늘 전부 수락하고*), *에이전트 코딩*(00:28 · 04:18) → 에이전틱 코딩(제목 · 챕터), *레드햇* → Red Hat, *에드버킷* → advocate, *그리스 에이블딩어*(00:35) → Grace Ableidinger(제목 · 설명란 · tags), *라이트 모드의*(00:37) → 라이트보드에(설명란 *라이트보드에 두 방식을 그려 가며*), *되게 그걸로*(01:33) → 대개 그걸로(추정 — 더빙 *apparently, it gets fixed that way*), *오후 한 낮이면*(01:49) → 오후 한나절이면(추정 — 더빙 *in a single afternoon*), *IBM 크리드는 얘는*(03:36) → IBM 글이 드는 예는(추정 — 뒤 문장 *같은 글은*. 더빙은 *IBM's Creed*), *옮겨간다고합니다* → 옮겨 간다고 합니다, *지위에만*(05:54) → 지휘에만(더빙 *orchestration*), *IBM 그래프 표현도*(05:56) → IBM 글의 표현도(추정 — 더빙도 *The IBM graph representation*), *IBM에서 이런 글의 공고도 갔습니다*(07:01~07:02) → IBM 글의 권고도 같습니다(추정 — 더빙 *IBM also provides similar recommendations*), *처음에는 나온*(08:18) → 처음에 나온.
> ⚠️ **판독하지 못한 것.** ① **화자 이름.** ko-orig는 *그리스 에이블딩어*, **영어 더빙은 *Edidiong Asikpo*** 로 읽는다(00:35) — 서로 다른 이름이다. 제목 · 설명란 · tags가 모두 *Grace Ableidinger* 라 그쪽을 따랐다. 더빙이 왜 다른 이름을 냈는지는 알 수 없다. ② *코드가 자기가 평소 이해할 수 있는 범위를 넘어 잘 안다고*(01:36~01:39, 더빙 *the code often goes beyond what he can normally understand*) — 끝 낱말을 정하지 않았다. ③ *프로덕션 상세로*(01:59, 더빙 *production details*) — 판서의 낱말을 정하지 않았다. ④ *글도 같은 말을 합니다*(02:40) — 어느 글인지 캡션에 없다(바로 앞이 무캡션). ⑤ *코드 베이스 구석에 도끼 고를 끝까지 파고든 뒤*(05:46~05:48, 더빙 *digs deep into a corner of the codebase*) — *도끼 고를* 을 정하지 않았다. ⑥ *글로 꼽은 안전 장치는 다섯 가집니다*(06:33, 더빙 *The article lists five safety measures*) — 다섯을 꼽은 주체가 글인지 화자인지 정하지 않았다(바로 뒤 07:01에서 IBM 글의 권고를 따로 든다). ⑦ *일이 커질수록 중요해지는*(08:01) — 문장이 끊겨 있다(더빙 *the things that become more important as the work scales up*). ⑧ 더빙은 *에이전틱* 을 두 번 *Iterative* 로 옮긴다(07:10 · 07:52) — 더빙 쪽 오류로 본다.
>
> ⚠️ **해설이고 2차 전달이다.** 위키는 원본 영상(IBM Technology `h4tHDFCPmQE`)도, Andrej Karpathy의 X 글(2025.02.02)도, IBM Think 글 *What is agentic coding?*(2026.03.27)도 이번에 열지 않았다. Karpathy와 IBM 글의 내용은 내레이션이 옮긴 말이다. 화자의 직함(*Red Hat 개발자 advocate*)도 내레이션 표기다.


## 설명란

바이브 코딩과 에이전틱 코딩, 내 작업에는 어느 쪽이 맞을까요? IBM Technology 영상에서 Red Hat의 Grace Ableidinger가 라이트보드에 두 방식을 그려 가며 비교한 내용을 한국어로 정리했습니다.

'바이브 코딩'이라는 말을 만든 Andrej Karpathy는 AI가 고친 코드를 늘 전부 수락하고 바뀐 부분은 읽지 않는다고 썼습니다. 다만 버려도 되는 주말 프로젝트에나 괜찮다고 선을 그었습니다. 그럼 결제 시스템처럼 버리면 안 되는 코드는 어떻게 짜야 할까요? 프롬프트 → 생성 → 반복의 짧은 고리와 이해 → 계획 → 실행 → 테스트 → 검증의 긴 고리, 걸러 낸 컨텍스트와 서브에이전트, 테스트·거버넌스·관찰 가능성·롤백·가드레일, 그리고 내 작업을 가르는 질문 네 가지까지 따라갑니다.

타임라인
0:00 코드를 안 읽는 코딩
0:32 바이브 코딩이란
1:52 코드가 서비스로 넘어갈 때
2:53 에이전틱 코딩
4:03 두 개의 루프
4:53 더 많이 알려 주면 더 잘할까
6:04 힘이 셀수록 고삐도
7:07 그래서 무엇을 쓸까
7:57 설명할 수 있는 사람

참고
원본 영상 (IBM Technology): https://www.youtube.com/watch?v=h4tHDFCPmQE
Andrej Karpathy X, vibe coding (2025.02.02): https://x.com/karpathy/status/1886192184808149383
IBM Think, What is agentic coding? (2026.03.27): https://www.ibm.com/think/topics/agentic-coding

#바이브코딩 #에이전틱코딩 #AI코딩 #코딩에이전트 #vibecoding

> info.json `tags`: AI 에이전트 · AI 코딩 · Andrej Karpathy · Grace Ableidinger · IBM · Red Hat · agentic coding · vibe coding · 바이브 코딩 · 서브에이전트 · 에이전틱 코딩 · 카파시 · 컨텍스트 · 코딩 에이전트

## 트랜스크립트 — ko-orig (Korean, ASR variant=gemini — 한국어 내레이션. Grace Ableidinger 원음 발췌 자리는 무캡션(`[음악]` 표시만), 본인 인용 0)

[00:00] 바이브코딩이라는 말을 만든 사람은
[00:02] 코드를 읽지 않는다고 썼습니다.
[00:04] 오픈에이아이 공동 창업자 안드레이
[00:06] 카파시의 글입니다.
[00:08] 에이아이와 고친 코드는 늘 전부
[00:09] 수락하고 바뀐 부분은 더 읽지
[00:11] 않는다고요.
[00:13] 다만 그도 이 방식은 버려도 되는
[00:14] 주말 프로젝트에나 괜찮다고 선을
[00:16] 그었습니다.
[00:25] 그럼 결제 시스템처럼 버리면 안 되는
[00:27] 코드는 어떻게 짜야 할까요?
[00:28] 에이전트 코딩과 나란히 놓고 내
[00:30] 작업을 가르는 질문 네 개까지
[00:31] 봅니다.
[00:33] 설명하는 사람은 레드햇의 개발자
[00:35] 에드버킷 그리스 에이블딩어.
[00:37] 라이트 모드의 두 방식을 그려가며
[00:38] 비교합니다.
[00:39] 바이브 코딩이라는 말은 2025년
[00:41] 초에 생겼는데 뜻은 처음부터 좀
[00:43] 흐릿했다고 합니다.
[00:44] 흔히 따라붙는 기대는 두 가집니다.
[00:46] 개발자가 아니어도 누구나 코딩할 수
[00:48] 있다. 그리고 코딩이 빠르고
[00:49] 쉬워진다.
[00:51] 그런데 그녀가 최근 만난 개발자들의
[00:52] 반응은 좀 달랐습니다.
[00:58] [음악]
[01:09] 효율에는 [음악] 체크. 그런데
[01:10] 품질과 보안 실력에는 물음표. 이
[01:13] 걱정이 이 영상이 끝까지 다루는
[01:14] 질문입니다.
[01:15] 그럼 바이브 코딩이란 정확히 뭘까요?
[01:17] 그녀의 정의는 주로 프롬프트와
[01:19] 에이아이가 생성한 코드로 소프트웨어를
[01:21] 만드는 방식입니다. 핵심은
[01:22] 속도입니다.
[01:24] 원하는 걸 말로 설명하면 에이아이가
[01:25] 초안을 만들고 원하는 결과가 나올
[01:27] 때까지 계속 고쳐 달라고 합니다.
[01:29] 카파시의 글에는 실제로 어떻게
[01:30] 하는지도 나옵니다. 에러가 나면 아무
[01:32] 말 없이 에러 메시지를 그대로 붙여
[01:33] 넣고 되게 그걸로 고쳐진다고요.
[01:36] 그러다 보니 코드가 자기가 평소
[01:37] 이해할 수 있는 범위를 넘어 잘
[01:39] 안다고 적었습니다.
[01:40] 카파시가 말한 주말 실험 프로젝트에는
[01:42] 딱 맞는 방식이라고 그녀도
[01:43] 인정합니다. 빠른 시제품, [음악]
[01:45] 실험, 데모, 아이디어를 눈으로
[01:47] 확인하는 일이죠. 코딩을 전혀 몰라도
[01:49] 오후 한 낮이면 돌아가는 시제품을
[01:51] 만들 수 있습니다.
[01:52] 문제는 이 코드가 실제 서비스
[01:54] 그러니까 프로덕션으로 넘어갈 때
[01:56] 드러납니다.
[01:57] 판서에서도 시제품 목록 옆으로
[01:59] 화살표가 길게 프로덕션 상세로
[02:01] 갑니다. 그리고 그 위에 적힌 단어가
[02:03] 리뷰입니다.
[02:12] [음악]
[02:19] [음악]
[02:27] [음악]
[02:35] [음악]
[02:40] 글도 같은 말을 합니다. AI 코드는
[02:43] 맞아 보여도 미묘한 버그나 보안
[02:45] 구멍이 있을 수 있으니 전부 초안으로
[02:47] 보라고요.
[02:48] 그럼 사람의 검토를 작업 흐름 어디에
[02:50] 넣어야 할까요? 여기서 에이전틱
[02:52] 코딩이 나옵니다.
[02:53] 에이전틱 코딩은 AI가 개발자와 함께
[02:56] 일하는 방식입니다. 코드를 만들어
[02:57] 주는 데서 끝나지 않습니다.
[02:59] 여기서 코딩 에이전트는 도구입니다.
[03:02] 기존 코드 베이스를 이해하고 바꿀
[03:03] 계획을 세우고 구현하고 테스트를
[03:05] 돌립니다.
[03:06] 문서도 고치고 개발 도구까지
[03:08] 다룹니다.
[03:13] [음악]
[03:21] [음악]
[03:28] [음악]
[03:34] [음악]
[03:36] IBM 크리드는 얘는 이런
[03:37] 요청입니다. 프론트 엔드에 인증을
[03:39] 붙이고 API를 고치고 단위
[03:41] 테스트까지 넣어 달라.
[03:42] 여러 단계가 이어진 일을 에이전트가
[03:44] 계획을 세워 차례로 처리하는 [음악]
[03:46] 겁니다.
[03:47] 같은 글은 둘을 하나의 스펙트럼에
[03:48] 놓습니다. 한쪽 끝은 속도와 탐색이
[03:51] 먼저인 바이브 코딩, 그다음이 역할과
[03:53] 제약을 정해 에이전트를 지휘하는
[03:55] 에이전틱 코딩.
[03:56] 팀들은 보통 바이브 코딩으로 시작해서
[03:58] 걸린 게 커지고 위험해질수록 [음악]
[04:00] 구조가 더 갖춰진 쪽으로
[04:01] 옮겨간다고합니다.
[04:03] 두 방식을 나란히 놓으면 차이가
[04:05] 한눈에 보입니다.
[04:06] 그녀가 판서한 두 개의 고리입니다.
[04:08] 바이브 코딩은 짧은 고리입니다.
[04:10] 프롬프트를 쓰고 AI가 만들고 다시
[04:12] 고쳐달라고 합니다.
[04:14] 코드를 들여다보지 않아도 그럭저럭
[04:16] 쓸만한 결과가 나오곤 하죠.
[04:18] 에이전트 코딩은 고리가 깁니다. 먼저
[04:20] 코드를 이해하고 계획을 세우고
[04:22] 실행하고 테스트하고 마지막에
[04:24] 검증합니다.
[04:25] 에이전트가 코드를 한번 훑어 지금
[04:27] 무엇이 있는지 알려주고 다음 단계를
[04:29] 제안하고 고친 뒤 확인하고 요청대로
[04:32] 됐는지까지 확인합니다.
[04:48] 결국 두 루프의 차이는 단계수가
[04:50] 아니라 사람이 생각을 보태는 자리가
[04:51] 있느냐입니다.
[04:53] 그럼 앞에서 말한 사람의 분별력이란
[04:55] 구체적으로 뭘까요? 그녀는 이걸
[04:57] 컨텍스트로 설명합니다. 컨텍스트는
[04:59] 모델이 답을 낼 때 기대는
[05:01] 정보입니다. 코딩 에이전트라면 파일,
[05:03] 테스트, 문서 그리고 내가 쓴
[05:05] 프롬프트까지요.
[05:15] [음악]
[05:28] [음악]
[05:33] 그래서 목표는 많은 컨텍스트가 아니라
[05:35] 걸러낸 컨텍스트입니다. 판서의
[05:37] 깔때기처럼요.
[05:38] 방법은 둘입니다. 하나는 에이전트의
[05:40] 작업 흐름에 사람이 확인하는 단계를
[05:42] 더 넣는 것. 다른 하나는 앞에서 본
[05:44] 서브 에이전트입니다. 서브 에이전트가
[05:46] 코드 베이스 구석에 도끼 고를 끝까지
[05:48] 파고든 뒤 [음악] 짧은 요약만 들고
[05:50] 돌아옵니다. 덕분에 메인 에이전트는
[05:52] 수많은 파일에 묻히지 않고 계획과
[05:54] 지위에만 집중합니다.
[05:56] IBM 그래프 표현도 비슷합니다.
[05:57] [음악] 에이전트는 강력하지만
[05:59] 독심술사는 아니다. 성공 기준을
[06:01] 분명히 정하고 최신 코드와 설계
[06:03] 문서를 건네라고요.
[06:05] 마지막 차이는 보안입니다. 에이전트가
[06:07] 할 수 있는 일이 많아질수록 보안
[06:09] 문제도 커집니다.
[06:21] [음악]
[06:27] [음악]
[06:33] 글로 꼽은 안전 장치는 다섯
[06:35] 가집니다. 테스트. [음악] 바꾼 게
[06:37] 제대로 동작하는지 확인합니다. 둘째
[06:39] 거버넌스. 되돌릴 수 없거나 비용이
[06:41] 큰 결정에는 사람이 서명합니다. 셋째
[06:43] 관찰 가능성. 에이전트가 무엇을 왜
[06:45] 했는지 볼 수 있어야 합니다. 넷째
[06:47] 롤백. 실수는 되돌릴 수 있어야
[06:49] 하고요. 다섯째 가드레일. 정해둔
[06:51] 규칙 안에서만 움직이게 합니다.
[06:53] 많은 코딩 에이전트에는 이미 이런
[06:55] 장치가 들어있습니다. 명령을 실행하기
[06:57] 전에 허락을 묻거나 도구를 쓰려면
[06:58] 연결을 따로 승인받게 하는 식이죠.
[07:01] IBM에서 이런 글의 공고도
[07:02] 갔습니다. 쓰기 권한을 제한하고 병합
[07:04] 전에 테스트를 강제하고 에이전트가 한
[07:06] 일을 기록하라고요.
[07:08] 그럼 바이브 코딩과 에이전틱 코딩
[07:10] 어느 쪽이 나을까요?
[07:16] [음악]
[07:26] [음악]
[07:30] 하나씩 풀면 이렇습니다. 이 일의
[07:31] 배경 정보가 얼마나 필요한지, 미리
[07:34] 계획을 세워야 하는지,
[07:35] 결과를 얼마나 꼼꼼히 확인해야
[07:37] 하는지, 그리고 AI에게 얼마나
[07:39] 알아서 하게 둘 건지.
[07:41] 빠른 버그 수정, 새 디자인 시험,
[07:43] 변수 이름 바꾸기 같은 일이라면
[07:45] 바이브 코딩으로 충분할 수 있습니다.
[07:47] 반대로 새 기능을 프로덕션에 올리거나
[07:50] 데이터베이스나 결제 시스템을
[07:51] 건드리거나 큰 리팩토링을 할 때는
[07:54] 내가 운전대를 잡은 에이전틱 루프가
[07:55] 맞습니다.
[07:57] 판서 마지막 장입니다. 두 루프와
[07:59] 서브 에이전트, 그리고 일이 커질수록
[08:01] 중요해지는
[08:03] 에이전트가 알아서 하는 일이 늘수록
[08:05] 테스트와 승인, 롤백, 감사 기록도
[08:07] 더 중요해집니다.
[08:09] 세 줄로 줄이면 이렇습니다.
[08:10] 버려도 되는 코드는 바이브로, 남길
[08:13] 코드는 이해와 검증이 들어간 루프로.
[08:15] 그리고 에이전트에게 준 힘만큼 안전
[08:17] 장치를.
[08:18] 처음에는 나온 실력 걱정에는 IBM
[08:20] 글이 답합니다.
[08:21] 생각을 AI에 너무 많이 넘기면
[08:23] 기본기가 조용히 깎여 나갈 수 있고
[08:25] 그러니 이해를 자동화로 대신하지
[08:27] 말라고요.
[08:28] 처음에 전부 수락으로 돌아가 보면
[08:30] 그녀의 마지막 조언은 이렇습니다.
[08:37] [음악]
[08:44] 지금 AI에게 맡기고 있는 그 코드
[08:46] 버려도 되는 코드인가요? 아니면
[08:47] 누군가에게 설명해야 할 코드인가요?

## 트랜스크립트 — en-orig (영어 더빙 ASR — 인용하지 않음, 판독 대조용. 화자 이름을 *Edidiong Asikpo* 로, *에이전틱* 을 두 번 *Iterative* 로 읽는다. 무캡션 아홉 곳(약 2분 50초))

[00:00] The person who coined the term "vibe
[00:02] coding" wrote that they don't read the
[00:03] code.
[00:04] It is a post by Andrej Karpathy,
[00:06] co-founder of OpenAI.
[00:08] He says he always accepts the code fixed
[00:10] by AI and never reads the changes.
[00:13] However, he also drew a line, noting
[00:14] that this method is only okay for
[00:15] weekend projects you can throw away.
[00:25] Then, how should we write code that
[00:26] cannot be thrown away, like payment
[00:27] systems?
[00:28] We will look at four questions that
[00:30] compare this to agentic coding and
[00:31] define our workflow.
[00:33] The explainer is Red Hat developer
[00:35] Edidiong Asikpo.
[00:37] She compares the two methods while
[00:38] drawing them on a lightboard.
[00:39] The term "vibe coding" emerged in early
[00:41] 2025, but its meaning was a bit blurry
[00:43] from the start.
[00:44] It is often accompanied by two
[00:46] expectations. That anyone can code, even
[00:47] if they aren't a developer. And that
[00:49] coding becomes fast and easy.
[00:51] But the reaction from the developers she
[00:52] met recently was a bit different.
[01:09] A check mark for efficiency. But a
[01:10] question mark for quality, security, and
[01:12] expertise. This concern is the question
[01:13] this video covers until the end.
[01:15] So, what exactly is vibe coding? Her
[01:18] definition is a method of building
[01:19] software primarily through prompts and
[01:21] AI-generated code.
[01:22] The key is speed.
[01:24] You describe what you want in words, AI
[01:25] creates a draft, and you keep asking for
[01:27] fixes until you get the desired result.
[01:29] Karpathy's post also explains how it's
[01:30] actually done. If an error occurs, you
[01:32] just paste the error message as is
[01:33] without a word, and apparently, it gets
[01:34] fixed that way.
[01:36] He wrote that as a result, the code
[01:37] often goes beyond what he can normally
[01:39] understand.
[01:40] She also admits that it is a perfect
[01:41] method for the weekend experimental
[01:42] projects Karpathy mentioned. Things like
[01:44] quick prototypes, experiments, demos,
[01:46] and verifying ideas visually.
[01:48] Even without knowing any coding, you can
[01:49] create a working prototype in a single
[01:51] afternoon.
[01:52] The problem emerges when this code moves
[01:54] to an actual service, or production.
[01:57] On the board, there is a long arrow from
[01:59] the prototype list to production details
[02:01] . And the word written above it is "
[02:03] review."
[02:40] The post says the same thing.
[02:43] Since AI code might look correct but
[02:44] contain subtle bugs or security holes,
[02:46] treat it all as a draft.
[02:48] Then where should we put human review in
[02:50] the workflow? This is where agentic
[02:52] coding comes in.
[02:54] Agentic coding is a method where AI
[02:55] works together with a developer. It
[02:57] doesn't end with just generating code.
[02:59] Here, the coding agent is a tool. It
[03:02] understands the existing codebase, plans
[03:04] changes, implements them, and runs tests
[03:05] .
[03:06] It also updates documentation and
[03:07] handles development tools.
[03:36] IBM's Creed is a request like this.
[03:38] "Add authentication to the frontend, fix
[03:40] the API, and include unit tests."
[03:43] It involves agents planning and
[03:44] executing multi-step tasks in sequence.
[03:47] The same article places both on a single
[03:48] spectrum.
[03:49] At one end is "vibe coding,"
[03:50] prioritizing speed and exploration, and
[03:52] at the other is agentic coding, where
[03:53] you define roles and constraints to
[03:55] direct the agent.
[03:56] Teams usually start with vibe coding,
[03:58] shifting toward more structured
[04:00] approaches as the stakes and risks
[04:02] increase.
[04:03] When you place the two methods side by
[04:04] side, the difference is clear at a
[04:05] glance.
[04:06] These are the two loops she drew on the
[04:07] board.
[04:08] Vibe coding is a short loop. You write a
[04:11] prompt, the AI generates, and you ask
[04:12] for revisions.
[04:14] You often get usable results even
[04:16] without looking at the code.
[04:18] Agentic coding has a long loop.
[04:20] First, it understands the code, makes a
[04:22] plan, executes, tests, and finally
[04:24] verifies.
[04:25] The agent scans the code, informs you of
[04:27] what exists, suggests the next steps,
[04:29] fixes, checks, and even confirms if it
[04:32] meets your request.
[04:48] Ultimately, the difference between the
[04:49] two loops isn't the number of steps, but
[04:51] whether there is room for human input.
[04:53] So, what exactly is the human judgment
[04:55] mentioned earlier?
[04:57] She explains this in terms of context.
[04:59] Context is the information the model
[05:00] relies on when providing answers. For a
[05:02] coding agent, that includes files, tests
[05:04] , documentation, and the prompts I’ve
[05:05] written.
[05:33] Therefore, the goal is not "more"
[05:35] context, but "filtered" context. Like
[05:36] the funnel she drew on the board. There
[05:38] are two ways to do this. One is to add a
[05:40] human verification step into the agent’s
[05:42] workflow.
[05:43] The other is the sub-agent we saw
[05:45] earlier.
[05:46] The sub-agent digs deep into a corner of
[05:48] the codebase and returns with only a
[05:49] brief summary.
[05:51] Thanks to this, the main agent avoids
[05:52] getting buried in countless files and
[05:54] focuses only on planning and
[05:55] orchestration.
[05:56] The IBM graph representation is similar
[05:57] . Agents are powerful, but they aren't
[05:59] mind readers. You must clearly define
[06:01] success criteria and provide the latest
[06:03] code and design documents.
[06:05] The final difference is security. As an
[06:07] agent’s capabilities grow, so do the
[06:09] security concerns.
[06:34] The article lists five safety measures.
[06:36] First, tests. Verify that the changes
[06:38] work correctly.
[06:39] Second, governance. Have a human sign
[06:41] off on irreversible or high-cost
[06:42] decisions. Third, observability.
[06:44] You must be able to see what the agent
[06:46] did and why. Fourth, rollbacks. Mistakes
[06:48] must be reversible. Fifth, guardrails.
[06:51] Ensure it only operates within
[06:52] predefined rules.
[06:53] Many coding agents already include these
[06:55] features. For example, asking for
[06:57] permission before executing commands or
[06:58] requiring separate approval to connect
[06:59] to tools.
[07:01] IBM also provides similar
[07:02] recommendations. Restrict write access,
[07:04] enforce tests before merging, and log
[07:05] the agent’s activities.
[07:08] So, which is better: Vibe Coding or
[07:10] Iterative Coding?
[07:30] Let’s break it down point by point.
[07:32] How much background info is needed, do
[07:34] you need to plan ahead, how carefully
[07:35] must you verify the results, and how
[07:37] much will you let the AI handle on its
[07:39] own?
[07:42] For tasks like quick bug fixes, testing
[07:43] new designs, or renaming variables, Vibe
[07:45] Coding might be enough.
[07:48] Conversely, when deploying new features
[07:49] to production, touching databases or
[07:51] payment systems, or performing major
[07:52] refactoring, an Iterative loop where you
[07:54] take the wheel is the right way to go.
[07:57] This is the final page of notes. The two
[07:59] loops, sub-agents, and the things that
[08:00] become more important as the work scales
[08:01] up.
[08:04] As agents take on more tasks, testing,
[08:05] approval, rollback, and audit trails
[08:07] become increasingly critical.
[08:09] If I boil it down to three lines, it’s
[08:10] this.
[08:10] Use Vibe Coding for code you can discard
[08:12] , and an iterative loop with
[08:13] understanding and verification for code
[08:14] you want to keep.
[08:15] And implement safety measures
[08:16] proportional to the power you give your
[08:17] agents.
[08:18] As for the concerns about skill
[08:19] mentioned at the beginning, an IBM
[08:20] article provides the answer.
[08:21] If you offload too much thinking to AI,
[08:23] your fundamentals may quietly erode, so
[08:25] don't replace understanding with
[08:27] automation.
[08:28] Going back to the "Accept All" mentioned
[08:30] at the start, her final advice is this:
[08:44] Is the code you’re currently handing
[08:45] over to the AI code that can be
[08:47] discarded? Or is it code that you’ll
[08:48] need to explain to someone else?
