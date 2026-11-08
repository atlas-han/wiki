---
title: "AI끼리 밤새 50번 싸웠다 | Anthropic은 AI가 쓴 코드를 어떻게 리뷰할까"
type: video
source: https://www.youtube.com/watch?v=Fxy8Jr77nKc
site: youtube.com
author:
  - "[[Tech Bridge]]"
duration: 7:13
published: 2026-11-07
created: 2026-11-08
description: "Tech Bridge 한국어 해설 7:13, 공식 챕터 7, John Kim(설명란 · en 더빙 근거) 발췌 2곳(하나는 무캡션). Anthropic Claude Code 팀의 코드 리뷰 방식(claude.dev 블로그 — 위키 미열람): AI 둘이 밤새 50번 넘게 리뷰를 주고받은 사건, 코드 90% AI · 코드 2배 · 되돌림 40%+ 감소, 하루 변경 2,500 → 3만+, 질문의 전환(누가 읽었나 → 무엇이 잘못될 수 있나), 사람의 주의력이 희소 자원, 7겹 리뷰(PR 전 자기 검증 + 새 맥락 에이전트 · 투표하는 AI 리뷰 16% → 54% · 보안 · 필수 검사 · 위험도별 사람 승인 · 기능 플래그 · 빠른 롤백), 59%는 첫 리뷰부터 있던 코드, 세 라운드 규칙 · 변경분만 · 버그 종류 · 반복 금지(65% → 78%, 8.9% → 1.5%), 사고 PR 시험지, 사람의 일, you land it you own it(추정), CLAUDE.md · REVIEW.md."
tags:
  - clippings/youtube
---

**Source URL**: https://www.youtube.com/watch?v=Fxy8Jr77nKc
**Channel**: Tech Bridge · **Duration**: 7:13 · **Published**: 2026-11-07

> **게시일.** info.json 기준 `upload_date` **`20261107`**(UTC), `timestamp` 1794020427(= 2026-11-07 03:00:27 UTC = **2026-11-07 12:00 KST**), `availability: public`. 2026-11-08 회차 목록에 처음 나왔다.
>
> **오디오 트랙과 자막 — 인용 규칙.** 오디오는 `Korean original (default)` + 영어(`en` · `en-US`, 더빙)이고 메타 `language`=`en`이다. 수동 자막은 없다. `ko`와 `ko-orig`는 **md5가 같다**(`lang=ko` 원 ASR). `en-orig`(`lang=en&variant=timing-optimized`)는 영어 트랙 ASR — 내레이션은 영어 더빙, 발췌는 원음이다. → **내레이션 인용은 ko-orig**로 한다. 영어 발췌는 아래처럼 en-orig에 캡션이 없어 **ko-orig의 영어 ASR로만** 남아 있다. `--sleep-subtitles 8`로 429 없음.
>
> **형식 — Tech Bridge 한국어 해설 + 영어 발췌 2곳(둘 다 캡션이 온전하지 않다).** 근거는 설명란 *참고* 두 링크 — claude.dev 블로그 *How the Claude Code team does code review*(`claude.dev/blog/solving-code-review-at-anthropic/`)와 John Kim의 영상 *How Anthropic Engineers Review AI Code*(`4m8mq42M_3E`) — 이고 **위키는 둘 다 열어 보지 않았다.** 11-02 [[tech-bridge-ai-labs-claude-code-verification-review-loop]]가 같은 블로그 글을 AI Labs가 요약한 영상이었다.
> - **발췌 ①(01:58~02:15) 무캡션.** 내레이션 *"글을 소개한 개발자 종[=John]은 오히려 이렇게 말합니다."*(01:56~01:59) 뒤로 ko-orig는 `[음악]`(02:09)뿐이고, en-orig는 121.7→135.4초 간격이다. **John Kim이 무엇을 말했는지 자막에 없다.** 쓰지 않는다.
> - **발췌 ②(06:01~06:13) ko-orig의 영어 ASR만 있다.** en-orig는 360.6→375.4초가 비어 있다. ko-orig: *"AI did not fault"*(06:01) · *"AI helped all this and honestly expected now. But if you're the one who shipped it, if you're the one who put it into production, then it's your fault at the end of the day."*(06:04~06:13). 한국어 ASR이 잡은 영어라 낱말이 틀렸을 수 있다(*"AI did not fault"* 는 문장이 안 된다). 내레이션 *"종도[=John도]이 부분을 가장 강조합니다"*(05:55~05:58) 직후라 **John Kim의 발언으로 추정**한다. 인용할 때 이 사정을 함께 적는다.
> - 무캡션 간격(ko-orig 기준): 02:02~02:09 · 02:11~02:15(발췌 ①). en-orig는 그 밖에 06:00~06:15(발췌 ②)도 비어 있다.
>
> **화자.** 내레이션만 있고, 발췌 화자는 내레이션이 *"글을 소개한 개발자 종"*(ko-orig) · en 더빙 *"Developer John Kim, who introduced this post"*(01:56~01:58)이라 부른다. 성 *Kim*은 en 더빙과 설명란(*John Kim, How Anthropic Engineers Review AI Code*)에 있다 — ko-orig에는 *종*뿐이다. 소속 · 직함은 없다. *"글을 소개한"* 이라는 말과 설명란 링크로 보아 블로그 글의 저자가 아니라 **소개 영상을 만든 사람**이다(추정).
>
> ⚠️ **기간 — "딸 만에" 판독 미확정.** ko-orig *"5월엔 2,500권[=건] 정도였어요. 그런데 9월에는 3만 건을 넘었습니다. 딸 만에 10배 넘게"*(00:55~01:02). en 더빙 *"in just three months"*(01:02) → **석 달**로 읽힌다. 그런데 5월 → 9월은 넉 달이고, 11-02 AI Labs 편은 같은 글을 *"in just 4 months"* 로 전했다. 해설의 석 달 · AI Labs의 넉 달 · 달력의 4개월 — **어느 쪽도 정하지 않는다.** 단위(리뷰할 변경 · 저장소 전체에 들어가는 변경)도 10-30 Osmani 편(merging)과 다르다.
>
> ⚠️ **"You land it, you own it" — 원음 판독.** ko-orig *"유랜드 유오운"*(06:15~06:18)은 영어 구호의 한국어 음차로 읽힌다(*you land it, you own it* 추정). 바로 뒤 풀이는 *"내가 머지했으면 내가 고친다"*(06:18~06:20)다. en 더빙은 `If I broke it, I fix it.`(06:19)로 바꿔 말한다. 영어 원문을 확인하지 않았으므로 구호의 철자는 추정이다.
>
> ⚠️ **수치는 전부 해설자의 2차 전달이고, 원 출처는 Anthropic 당사자다.** 코드의 90% · 코드 2배 · 되돌림 40% 넘게 감소 · X 260만 회 · 2,500 → 3만 · 16% → 54% · 2~3배 · 59% · 65% → 78% · 8.9% → 1.5% — 위키는 블로그와 대조하지 않았다. 11-02 AI Labs 편에 같은 숫자 일부(2,500 → 30,000+ · 50회 · 59%)가 있었다.
>
> ⚠️ **ASR 판독(ko-orig).** *지원낸* → 지어낸, *엔트로픽* · *앤트로픽* · *엔드로픽* → Anthropic(en 더빙은 *Entropy* — 더빙 ASR 오류), *AI 갔습니다* → AI가 씁니다(en *uses AI to write 90%*), *들었는데* → 늘었는데, *줘야 됐어요* → 조회됐어요(en *viewed*), *2,500권* → 2,500건, *피아* · *피* → PR, *맥락게* → 맥락이, *스타일지금* → 스타일 지적은, *세 기능* → 새 기능, *롤백기* → 롤백이, *기블레임* → git blame, *천 리뷰* → 첫 리뷰(en *the first review*), *닛* = nit, *AI 작성은* → AI 작성자는, *커미의* → 커밋, *부부만* → 부분만, *이성* → 이상, *8.9%에서 9%에서 1.5%* → 8.9% → 1.5%(말더듬, en *8.9% to 1.5%*), *종* → John, *클로드.md* → CLAUDE.md, *리뷰.md MD* → REVIEW.md, *시내* → 시대.

## 설명란

AI가 코드의 90%를 쓰는 팀은 코드 리뷰를 어떻게 할까요?
Claude Code를 만드는 Anthropic 팀이 공개한 코드 리뷰 방식을 정리했습니다. AI 둘이 밤새 50번 넘게 리뷰를 주고받은 실제 사건에서 시작해, 코드 한 줄이 배포되기까지 거치는 7겹의 리뷰, 리뷰가 끝없이 이어지지 않게 만든 규칙, 그리고 AI 시대에도 사람이 맡아야 하는 일까지 쉽게 풀어 봅니다.

타임라인
0:00 AI 둘이 밤새 50번 싸운 사건
0:50 하루 3만 건, 코드 홍수
1:33 진짜 부족한 자원: 사람의 주의력
2:14 코드 한 줄의 여정: 7겹의 리뷰
4:20 다시 그날 밤: 50라운드의 원인과 해결
5:32 그럼 사람은 뭘 하나
6:28 우리 팀에 적용하려면

참고
How the Claude Code team does code review (claude.dev 블로그): https://claude.dev/blog/solving-code-review-at-anthropic/
John Kim, How Anthropic Engineers Review AI Code: https://www.youtube.com/watch?v=4m8mq42M_3E

#ClaudeCode #Anthropic #코드리뷰 #AI코딩 #개발자

> info.json `tags`: AI 에이전트 · AI 코딩 · Anthropic · Claude Code · code review · 개발자 · 소프트웨어 엔지니어링 · 코드 리뷰

## 트랜스크립트 — ko (원 오디오 ASR, `lang=ko` — `ko-orig`와 바이트 동일 · 내레이션 인용 근거, 06:01~06:13 영어 발췌는 이 트랙에만 있음)

[00:00] 어느 날 밤 AI 두 개가 서로
[00:02] 싸웠습니다.
[00:04] 한쪽이 코드를 고치면 다른 쪽이 또
[00:06] 문제를 찾아내어 고치고 지적하고 또
[00:09] 고치고 결국 사람이 직접 멈출 때까지
[00:12] 리뷰는 무려 50번 넘게 돌았습니다.
[00:15] 지원낸 이야기가 아닙니다. 클로드
[00:17] 코드를 만드는 엔트로픽 팀이 직접
[00:19] 공개한 실제 사례예요.이
[00:22] 팀은 이제 코드의 90%를 AI
[00:24] 갔습니다.
[00:26] 그런데 이상한 숫자가 하나 있어요.
[00:28] 코드는 두 배로 들었는데 문제가
[00:30] 생겨서 되돌림 비율은 오히려 40%
[00:32] 넘게 줄었습니다.
[00:35] AI가 쓴 그 많은 코드를 사람이 다
[00:37] 읽었을까요? 아닙니다.이
[00:40] 방법을 정리한 글은 X에서만 260만
[00:43] 번 넘게 줘야 됐어요.
[00:45] 오늘은 코드 한 줄이 세상에
[00:47] 나가기까지 그 여정을 따라가
[00:49] 보겠습니다.
[00:50] 먼저 상황부터 볼게요. 앤트로픽 전체
[00:53] 저장소에 하루 동안 들어가는 코드
[00:55] 변경은 5월엔 2,500권
[00:57] 정도였어요. 그런데 9월에는 3만
[01:00] 건을 넘었습니다. 딸 만에 10배
[01:02] 넘게 늘어난 거죠. [음악] 이쯤
[01:05] 되면 사람이 한 줄씩 읽는 리뷰는
[01:07] 사실상 불가능합니다.
[01:09] 그래서이 [음악] 팀은 질문부터
[01:11] 바꿨어요. 사람이이 코드를 읽었나가
[01:14] 아니라이 변경에서 뭐가 잘못될 수
[01:17] 있고 그걸 잡아낼 가장 좋은 검사는
[01:19] 뭘까로
[01:21] 그러면서 리뷰하는 시점도 바뀝니다.
[01:23] 예전엔 코드를 다 쓰고 나서 마지막에
[01:25] 통과하는 관문이었다면 이제는 글을
[01:28] 쓰는 동안 계속 돌아가는 맞춤법
[01:30] 검사처럼 코드를 쓰는 내내 리뷰가
[01:32] 돌아가요.
[01:34] 이렇게까지 하는 이유는 하나예요.이
[01:35] [음악] 팀이 가장 아끼는 자원은
[01:37] 컴퓨터가 아니라 사람의 시간과
[01:39] 주의력이거든요.
[01:40] [음악]
[01:41] 그래서 목표는 이렇습니다. 대부분의
[01:43] PR은 사람 최대 한 명. 그것도
[01:46] 작성자 본인이면 충분하게 단,
[01:48] [음악] 되돌리는 일이나 사고는 늘지
[01:49] 않게요. 사고가 늘어난다면 시간을
[01:52] 아낀게 아니라 리뷰하던 시간을 고치는
[01:54] 시간으로 옮겨 놓은 것뿐이니까요.이
[01:55] [음악]
[01:56] 글을 소개한 개발자 종은 오히려
[01:59] 이렇게 말합니다. [음악]
[02:09] >> [음악]
[02:15] >> 그럼 이제 코드 한 줄을 따라가
[02:17] 볼게요. 엔지니어가 버그 하나를
[02:19] 고쳤다고 해봅시다.이 변경은 일곱
[02:21] 개의 층을 지나갑니다.
[02:23] 첫 번째 층은 피아를 올리기도 전에
[02:25] 시작됩니다. 클로드가 직접 테스트와
[02:28] 빌드, 린터를 돌리고 다 했어요라는
[02:30] 말 대신 실행 결과를 보여 줘야
[02:32] 하죠. 그다음엔 맥락게 깨끗한 두
[02:34] 번째 에이전트가 처음 보는 눈으로이
[02:36] 변경을 다시 리뷰합니다.
[02:39] 클로드 코드를 만든 보리스 체르니는
[02:41] 이걸 가장 중요한 [음악] 비법으로
[02:42] 꼽았어요. AI에게 스스로 검증할
[02:44] 방법을 주면 결과물이 두 세 배
[02:46] 좋아진다고요.
[02:48] 두 번째 층은 모든 피에 붙는 AI
[02:50] 리뷰예요. 여러 에이전트가 동시에
[02:52] 버그를 찾고 [음악]
[02:54] 다른 에이전트 그룹이 그 지적
[02:55] 하나하나에 투표를 합니다. 충분히
[02:57] 동의를 얻은 지적만 살아남아요.
[03:00] 그 단순한 스타일지금 버리고 남은 건
[03:02] 심각도순으로 정리되죠.
[03:04] >> [음악]
[03:04] >> 이걸 도입한 뒤 실질적인 리뷰
[03:06] 코멘트를 받는 PR은 16%에서
[03:08] 54%로 늘었습니다.
[03:11] 세 번째는 보안 리뷰,네 번째는
[03:13] 린트와 타입, 테스트, 빌드 같은
[03:16] 필수 자동 검사예요. 열린 지적이
[03:18] 하나라도 남아 있거나 빨간 불이
[03:19] 켜지면 머지할 수 없습니다.
[03:22] 다섯 번째 층이 재밌어요. 사람의
[03:24] 승인을 위험도에 따라 다르게
[03:26] 요구합니다. 문서 수정처럼 위험이
[03:28] 낮으면 사람 승인이 필요 없고 보통의
[03:30] 기능 변경은 한 명. 가장 위험한
[03:32] 코드는 두 명이 봐야 해요. 등급은
[03:35] 누가 썼느냐가 아니라 무엇을
[03:37] 바꿨느냐를 보고 분류기가 정합니다.
[03:39] 그리고 [음악] AI의 승인은 절대
[03:41] 사람의 승인으로 쳐주지 않아요. 여섯
[03:44] 번째는 머지와 기능 플래그. 세
[03:46] 기능은 엔드로픽 직원들이 먼저 써
[03:48] 보고 그다음에 단계적으로 배포됩니다.
[03:51] [음악] 마지막 일곱 번째는 빠른
[03:53] 감지와 빠른 롤백이에요. 문제가
[03:55] 생기면 배포 없이 플래그를 끄고 바로
[03:57] 되돌립니다.이 [음악]
[03:59] 일곱 겹은 하나의 거대한 관문이
[04:01] 아니에요. 각층이 일부 문제를 잡고
[04:04] 일부는 놓칩니다. 끝까지 뚫고 나가는
[04:06] 건 아주 적고 그건 롤백기 처리하죠.
[04:08] [음악]
[04:09] 한 동료의 말이 핵심을 찌릅니다.
[04:11] 천천히 가면 에러율이 낮아지긴 하지만
[04:14] 그건 그냥 일을 덜하기 때문이라고요.
[04:16] 그래서이 [음악] 팀은 더 빨리
[04:17] 발견하고 더 빨리 고치는 쪽을
[04:19] 택했습니다.
[04:21] 자, 이제 처음 그 이야기로 돌아가
[04:22] 볼까요? AI 두 개가 밤새 50번
[04:25] 싸운 사건이요.
[04:27] 팀이 기블레임으로 리뷰가 계속 지적한
[04:30] 코드를 추적해 봤더니 그중 59%는
[04:33] 천 리뷰 때부터 이미 있던
[04:34] 코드였어요. [음악]
[04:36] 새 버그를 찾은게 아니라 원래 있던
[04:38] 버그를 매번 조금씩 더 찾아낸 거죠.
[04:40] [음악]
[04:41] 여기서 중요한 포인트. 사람은 사소한
[04:44] 지적 닛을 1초만에 넘길 수 있지만
[04:46] AI 작성은 그걸 그대로 고칩니다.
[04:48] 그럼 또 커미의 또 리뷰가 시작되죠.
[04:50] [음악]
[04:51] 그래서 규칙을 바꿨어요. 세 번 돌면
[04:54] 리뷰어가 접근 방식부터 다시 생각해
[04:55] 보라고 하고 그다음부턴 바뀐 부부만
[04:58] 다시 봅니다. 한 줄이 아니라 버그의
[05:00] 종류를 짚어서 같은 실수를 한 번에
[05:02] 고치게 하고 이미 한 지적은 반복하지
[05:04] 않아요. 결과는 숫자로 나왔습니다.
[05:08] 한 번에 통과하는 PR은 65%에서
[05:10] 78%로 늘고 [음악] 다섯 번 이성
[05:12] 도는 PR은 8.9%에서 9%에서
[05:14] 1.5%로 줄었어요.
[05:17] 리뷰어를 키우는 방법도 독특합니다.
[05:19] 과거에 사고를 냈던 PR에 모아 시험
[05:21] 문제로 만들고 리뷰어가 매일이 시험을
[05:23] 봐요. 리뷰어의 프롬프트나 도구
[05:26] 모델을 바꾸면 점수가 올랐는지
[05:27] 확인하고 아니면 버립니다. 사고
[05:30] 하나하나가 그대로 교재가 되는
[05:32] 셈이죠. [음악]
[05:33] 그럼 사람은 이제 뭘 할까요? 오히려
[05:35] 더 중요한 일이 남았습니다. [음악]
[05:37] 이걸 만들지 결정하는 일. 결제나
[05:40] 자동 업데이트처럼 위험한 코드를 보는
[05:42] 일.
[05:42] >> [음악]
[05:42] >> 남들이 따라할 아키텍처를 정하는 일.
[05:45] 그리고 테스트 결과나 스크린샷 같은
[05:47] 증거를 [음악] 직접 읽고 판단하는
[05:49] 일이요.
[05:50] 무엇보다 결과에 대한 책임은 사람에게
[05:53] 있습니다. 누가 타이핑했든 배포한
[05:55] 사람이 책임져요. 종도이 부분을 가장
[05:58] 강조합니다.
[06:01] AI did not fault
[06:02] [음악]
[06:04] AI helped all this
[06:06] and honestly
[06:07] expected now. But if
[06:09] you're the one who
[06:10] shipped it, if
[06:10] you're the one who
[06:11] put it into
[06:11] production, then
[06:12] it's your fault at
[06:13] the end of the day.
[06:15] 이 팀의 원칙도 똑같아요. 유랜드
[06:18] 유오운. [음악] 내가 머지했으면
[06:20] 내가 고친다. 대신 변경은 작게
[06:23] 쪼개고 무엇이든 몇 분 안에 되돌릴
[06:25] 수 있게 만들어서 책임이 두려움이
[06:27] 되지 않도록 했죠. [음악] 우리
[06:29] 팀에 적용한다면 이렇게 시작해 볼 수
[06:30] 있어요. AI가 직접 돌려볼 수 있는
[06:33] [음악] 검사를 짧은 클로드.md
[06:34] 파일에 적어주고 반복되는 리뷰 지적은
[06:37] 리뷰.md MD 파일로 옮기세요.
[06:39] 리뷰 라운드에는 상한을 두고 위험
[06:41] 등급은 작성자가 아니라 변경 내용으로
[06:43] 정하세요. 그리고 사고와 되돌림
[06:45] 코드를 모아서 리뷰어를 채점하는
[06:47] 시험지로 만드는 거죠. [음악]
[06:49] 정리하면이 팀은 리뷰를 없애지
[06:51] 않았습니다. 코드를 읽는 일은
[06:53] 기계에게 넘기고 사람의 주의력은 정말
[06:55] 위험한 곳에 쓰도록 옮겼을 뿐이죠.
[06:58] 목표는 하나예요. 변경 하나에 드는
[07:01] 사람의 시간은 줄이고 되돌리는 일은
[07:03] 늘리지 않는 것.
[07:05] AI가 코드를 쓰는 시내. 여러분
[07:07] 팀의 리뷰는 지금 어디에 사람의
[07:09] 시간을 쓰고 있나요? [음악]

## 트랜스크립트 — en-orig (영어 트랙 ASR — 내레이션은 더빙 · 대조용, 발췌 구간 무캡션)

[00:00] One night, two AIs started fighting each
[00:02] other.
[00:04] One would fix the code, and the other
[00:06] would find a problem, fix it, point it
[00:08] out, and then fix it again.
[00:10] The review went on for over 50 rounds
[00:11] until a human eventually had to step in
[00:13] and stop it.
[00:15] This isn't some made-up scenario.
[00:17] It's a real case shared by the Entropy
[00:19] team, the creators of Claude Code.
[00:22] This team now uses AI to write 90%of
[00:23] their code.
[00:26] But there is one strange figure.
[00:28] Even though the code doubled, the
[00:30] rollback rate due to issues actually
[00:32] dropped by over 40%.
[00:35] Did a human read all that code written
[00:37] by AI?
[00:38] No. The post detailing this method has
[00:41] been viewed over 2.6 million times on X
[00:43] alone.
[00:45] Today, we'll follow the journey of a
[00:47] single line of code as it enters the
[00:49] world.
[00:50] First, let's look at the situation.
[00:52] In May, the number of code changes
[00:54] hitting the Entropy repository daily was
[00:56] around 2,500.
[00:58] By September, that number exceeded
[01:00] 30,000. It increased more than tenfold
[01:02] in just three months.
[01:04] At this point, a human reading every
[01:06] line for review is practically
[01:08] impossible.
[01:09] So, this team changed the core question
[01:11] .
[01:12] Instead of "Did a human read this code?
[01:14] ", they asked "What could go wrong with
[01:16] this change, and what's the best test to
[01:19] catch it?"
[01:21] This also changed the timing of the
[01:22] reviews. While it used to be a final
[01:25] gate to pass after finishing the code,
[01:28] now reviews run constantly, just like a
[01:30] spell checker while you type.
[01:33] There is one reason they go to such
[01:35] lengths.
[01:35] The resource this team values most is
[01:37] not computer power, but human time and
[01:39] attention.
[01:41] So, their goal is simple. Most PRs
[01:43] should require at most one person—and
[01:45] the author themselves should be enough.
[01:47] But rollbacks and accidents must not
[01:49] increase.
[01:51] If accidents increase, they haven't
[01:52] saved time; they've just shifted time
[01:53] from reviewing to fixing.
[01:56] Developer John Kim, who introduced this
[01:58] post, puts it this way.
[02:15] Now, let's follow a single line of code
[02:17] .
[02:17] Let's say an engineer fixed a bug.
[02:20] This change passes through seven
[02:21] different layers.
[02:23] The first layer begins even before the
[02:25] PR is submitted.
[02:26] Claude must run tests, builds, and
[02:28] linters itself, and show the execution
[02:30] results instead of just saying "I'm done
[02:32] ."
[02:33] Then, a second agent with a clean
[02:35] context reviews the change again with
[02:37] fresh eyes.
[02:39] Boris Cherny, who created Claude Code,
[02:41] cited this as the most important secret
[02:42] .
[02:43] Giving AI a way to verify its own work
[02:45] improves the output by two to three
[02:46] times.
[02:48] The second layer is an AI review
[02:50] attached to every PR. Multiple agents
[02:52] find bugs simultaneously, and another
[02:54] group of agents votes on each of those
[02:56] findings. Only the findings that receive
[02:58] enough agreement survive.
[03:00] Simple style-related feedback is
[03:01] discarded, and the rest are organized by
[03:03] severity.
[03:04] After introducing this, the percentage
[03:06] of PRs receiving substantive review
[03:08] comments rose from 16%to 54%.
[03:11] The third layer is a security review,
[03:12] and the fourth involves essential
[03:14] automated checks like linting, typing,
[03:16] tests, and builds.
[03:17] If even one open issue remains or a red
[03:19] light is lit, you cannot merge.
[03:22] The fifth layer is quite interesting. It
[03:24] requires human approval based on the
[03:25] level of risk.
[03:27] Low-risk tasks like documentation
[03:29] updates don't need human approval,
[03:30] regular feature changes need one, and
[03:32] the riskiest code requires two.
[03:35] The risk level is determined by a
[03:36] classifier based on what was changed,
[03:38] not who wrote it.
[03:40] And AI approval is never counted as
[03:41] human approval.
[03:44] The sixth layer is merge queues and
[03:45] feature flags.
[03:46] New features are first used by Anthropic
[03:48] employees and then rolled out in stages
[03:50] .
[03:51] The final, seventh layer is fast
[03:53] detection and quick rollback.
[03:55] If a problem arises, we turn off the
[03:56] flag without a new deployment and revert
[03:57] it immediately.
[03:59] These seven layers are not one massive
[04:01] gateway. Each layer catches some issues
[04:04] and misses others. Very few make it all
[04:06] the way through, and those are handled
[04:07] by rollback.
[04:09] A colleague’s words hit the core of the
[04:11] issue. Moving slowly might lower the
[04:13] error rate, but that’s only because
[04:14] you’re doing less work.
[04:16] So, this team chose to discover faster
[04:19] and fix faster.
[04:21] Now, shall we return to that initial
[04:22] story? The incident where two AIs fought
[04:24] 50 times overnight.
[04:27] The team used git blame to track the
[04:29] code that the reviews kept flagging, and
[04:31] 59%of it had been there since the first
[04:33] review.
[04:36] They weren’t finding new bugs; they were
[04:37] just uncovering bits of the original bug
[04:39] each time.
[04:41] Here is the important point. A human can
[04:43] dismiss a minor nitpick in a second, but
[04:45] an AI author will fix it exactly as
[04:47] requested. Then another commit, and
[04:49] another review begins.
[04:51] So, they changed the rules. After three
[04:53] rounds, the reviewer asks to rethink the
[04:55] approach, and from then on, they only
[04:57] look at the changed parts.
[04:59] They point out the type of bug rather
[05:01] than just a single line to fix similar
[05:02] mistakes at once and never repeat the
[05:04] same feedback.
[05:06] The results appeared in the numbers. PRs
[05:08] that pass on the first try increased
[05:10] from 65%to 78%, and PRs that loop more
[05:13] than five times dropped from 8.9%to 1.5
[05:15] %.
[05:17] Their method for training reviewers is
[05:18] also unique. We collect PRs that caused
[05:20] incidents in the past to create test
[05:21] sets, which reviewers take every day.
[05:24] When we change the reviewer’s prompt,
[05:26] tools, or model, we check if the score
[05:27] improves; if not, we discard it.
[05:30] In a way, every single incident becomes
[05:31] a study guide.
[05:33] So, what is left for humans to do?
[05:35] Actually, more important tasks remain.
[05:37] Deciding if something is worth building
[05:40] , reviewing risky code like payments or
[05:42] auto-updates, defining architecture for
[05:44] others to follow, and directly assessing
[05:46] evidence like test results or
[05:48] screenshots.
[05:50] Above all, the responsibility for the
[05:52] outcome lies with the human.
[05:54] Whoever deployed it is responsible,
[05:55] regardless of who typed it.
[05:56] John Kim emphasizes this part the most.
[06:15] >> The team’s principle is exactly the same
[06:16] .
[06:19] If I broke it, I fix it.
[06:22] Instead, they keep changes small and
[06:23] ensure anything can be rolled back in
[06:25] minutes so that responsibility doesn't
[06:26] become fear.
[06:28] If you want to apply this to your team,
[06:30] you can start like this.
[06:31] Write checks that the AI can run itself
[06:33] in a short cloud.md file, and move
[06:35] repetitive review feedback into a
[06:37] review.md file.
[06:39] Set a limit on review rounds, and
[06:41] determine risk levels based on the
[06:42] changes, not the author.
[06:44] Then, collect past incidents and
[06:45] rollbacks to create an exam for scoring
[06:47] the reviewer.
[06:49] In short, this team didn't get rid of
[06:51] reviews.
[06:52] They simply handed off code reading to
[06:54] machines and shifted human attention to
[06:56] where it’s truly needed.
[06:58] The goal is simple. Reduce the human
[07:01] time spent per change without increasing
[07:02] the number of rollbacks.
[07:05] In an era where AI writes code, where is
[07:07] your team spending its human time during
[07:09] reviews?
