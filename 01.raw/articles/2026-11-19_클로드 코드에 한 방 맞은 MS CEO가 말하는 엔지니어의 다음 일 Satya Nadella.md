---
title: "클로드 코드에 한 방 맞은 MS CEO가 말하는 엔지니어의 다음 일 | Satya Nadella"
type: video
source: https://www.youtube.com/watch?v=l33zynXSBFs
site: youtube.com
author:
  - "[[Tech Bridge]]"
duration: 15:43
published: 2026-11-19
created: 2026-11-20
description: "Tech Bridge 한국어 해설 15:43, 공식 챕터 10, Korean original + 영어 더빙(en-orig는 내레이션 자리는 더빙 ASR · 인터뷰 발췌 자리는 Nadella 원음). Microsoft CEO Satya Nadella의 The Pragmatic Engineer 팟캐스트 인터뷰(진행 Gergely Orosz, 11-16 공개)를 Microsoft · GitHub 공식 글과 맞춰 본 해설 — 여섯 달 만에 IDE가 밀려났다는 인정(계기는 Claude Code), 코드는 입력에서 출력으로, 비싸진 것은 검증, 소프트웨어 팩토리 블로그 두 편(Copilot Cowork 9명 · 하루 PR 1,211개 / GitHub Copilot 런타임 Rust 80만 줄), 브라운필드의 빌드 · CI/CD 병목, 자발적 퇴직 제안, 신입과 토큰 예산, 모델을 갈아 끼워도 통과하는 사적 eval, 권한과 지능의 분리, 학생 모드."
tags:
  - clippings/youtube
---

**Source URL**: https://www.youtube.com/watch?v=l33zynXSBFs
**Channel**: Tech Bridge · **Duration**: 15:43 · **Published**: 2026-11-19

> **게시일.** info.json `upload_date` **`20261119`**, `timestamp` 1795057221(= 2026-11-19 03:00:21 UTC = **2026-11-19 12:00 KST**), `availability`=`public`. 2026-11-19 회차(09:10 KST) 뒤에 올라왔다. 파일명에서 `|`는 뺐다.
>
> **오디오 트랙과 자막 — 인용 규칙.** 오디오는 **Korean original(default) + 영어 더빙**(audio language `ko` · `en` · `en-US`), 메타 `language`=`en`. 수동 자막 없음. `ko` = `ko-orig`(파일 동일, `kind=asr&lang=ko&variant=gemini`). `en-orig`(`kind=asr&lang=en&variant=timing-optimized`)는 **두 가지가 섞여 있다.**
> ① **내레이션 자리는 영어 더빙의 ASR** — 첫 줄부터 내레이션의 영어 번역이다(*"The CEO of the company that created VS Code has admitted it."*). 더빙은 고유명사를 틀린다: *커서가 나온 뒤에도* → *Even after ChatGPT came out*(00:48), *거게이가 묻습니다* → *GitHub is asking* / *GitHub asks* / *GitHub confesses*(05:56 · 07:15 · 07:43), *코파일럿 코어 코드 팀*(= Copilot Cowork) → *the GitHub Copilot Core team*(04:09), *프레이즈*(= PRAISE) → *Praxis*(14:31), *자발적 퇴직 제안* → *voluntary retirement plan*(08:26). **인용하지 않고 판독 대조용으로만 쓴다.**
> ② **인터뷰 발췌 자리는 Nadella 원음으로 판정했다.** 근거 넷: ⓐ ko-orig가 비는 바로 그 구간에만 나온다(한국어 ASR은 영어 원음을 버린다) ⓑ 1인칭의 더듬는 구어다(*you know* · *right?* · *I mean*) — 더빙 문장은 매끈한 3인칭이다 ⓒ 발췌가 끝나면 더빙이 *He means …* · *Satya says …* 로 받는다 ⓓ **맺음 발췌(14:51~15:31)는 ko-orig에도 같은 영어가 잡혔다** — 더빙 트랙이 발췌 자리에 원음을 그대로 싣는다는 직접 증거다.
> → **한국어 인용은 ko-orig.** 영어 인용은 맺음 발췌만 두 트랙 확인이고(ko-orig의 글자로 인용) **나머지 영어 인용은 en-orig 단일 트랙** 이다. ⚠️ ASR 한 벌뿐이라 낱말이 틀릴 수 있다 — 맺음 발췌에서 두 ASR은 *mid-career*(ko-orig) / *a manager*(en-orig), *to sort of learn, to do, be in teams*(ko-orig) / *to learn and be on teams*(en-orig)로 갈린다. 조각으로만 잡힌 발췌(06:13~06:21 · 07:46~08:06 · 10:08~10:30 · 11:38~11:47)는 인용하지 않았다. 429 없음.
>
> **무캡션 구간(`gaps.py` 4.5초 기준).** ko-orig 열여덟 곳: 00:07~00:15 · 01:00~01:25 · 01:33~02:07 · 02:33~03:27 · 04:45~05:07 · 05:21~05:45 · 06:12~06:34 · 06:47~07:08 · 07:47~08:15 · 08:49~09:05 · 09:10~09:37 · 09:52~10:33 · 10:54~11:25 · 11:40~11:52 · 11:58~12:31 · 12:33~12:40 · 12:57~13:34 · 14:08~14:31 — 합쳐 약 7분 40초, 대부분 인터뷰 발췌 자리다(12:31 · 12:40에는 *Yeah.* 만 잡혔다). en-orig 아홉 곳: 00:08~00:12 · 02:34~02:45 · 03:21~03:27 · 08:49~09:06 · 09:11~09:23 · 09:53~10:08 · 13:28~13:34 · 14:09~14:25 · 14:53~15:01.
> ⚠️ **두 트랙 모두 빈 곳 — 내용 미상:** 00:07~00:12(첫 발췌) · 02:33~02:45(*검증* 답의 앞머리) · 08:49~09:05(*선택권* 답의 원음) · 09:10~09:23(불안에 관한 답의 앞머리) · 09:52~10:08(신입 채용 답의 앞머리) · 14:08~14:31(*꿈의 다음 직업* — en-orig에 *Microsoft.* 한 낱말뿐). ⚠️ 00:12~00:14 *밀어낸 것은 Anthropic의 Claude Code* 라는 내레이션은 **더빙 ASR에만** 있고 ko-orig에는 없다(제목 · 설명란이 같은 말을 한다). **이 구간들에 대해 위키는 인용도 요약도 만들지 않는다.**
>
> **ASR 판독(ko-orig → 판독, 괄호는 근거).** *귀가 꼽은*(00:18) → 그가 꼽은, *거게이 오로스 · 거게이 · 거기 · 거기 애가 · 거기에는*(00:32 · 00:42 · 05:56 · 07:15 · 07:42 · 08:37) → Gergely Orosz(설명란의 The Pragmatic Engineer · 더빙 *Gergely Orosz*), *엔지니어러*(00:38) → 엔지니어로, *파이선*(03:58) → 파이썬, *바스 의 글, 코파일럿 코어 코드 팀*(04:08~04:10) → Bas(Brekelmans)의 글, Copilot Cowork 팀(설명란), *이를 경유하고*(04:17~04:19) → 이끌고(추정 — 더빙 *guiding them*), ⚠️ *RSI가 자기한테는 이퀄*(05:11~05:13) → **미확정**(eval / quality — 더빙 *essentially quality*. RSI의 풀이도 캡션에 없다), *페이엑스 단말기*(07:22) → VAX 단말기(추정 — 더빙은 *terminals* 뿐), *코파일럿 이전의 아이디*(08:21) → IDE(더빙 *an IDE before Copilot*), *해고의 전조니 하는 겁니다*(08:29) → 전조냐 하는 겁니다(추정), *AI는 이티 회사*(10:32) → AI 네이티브 회사(추정 — 더빙 *AI-native*), *더 하죠*(10:37) → 더하죠, *있다고고요*(11:30) → 있다고요, *엑셀에 올린 같은 글*(13:40) → X에 올린(더빙 *shared on X*), *로시노비치와 헨슬먼*(14:31) → Russinovich와 Hanselman(설명란), *프레이즈*(14:33) → PRAISE(설명란), *ID를 밀어낸*(15:33) → IDE를. en-orig 원음 쪽: *ID kind of faded away*(01:53) → IDE, *Scott Henselman, you know, percepts*(02:45) → Scott Hanselman · preceptors, *showed up to work and get up*(06:57) → GitHub(추정), *knowledge being tassed*(11:09) → tacit(추정), *reverse information paradox*(11:59) → 판독 그대로 둠.
>
> ⚠️ **해설이고 2차 전달이다.** 위키는 원 인터뷰(`0NE89Nzfk20`)도 설명란의 공식 글 여덟 편도 열지 않았다. 수치(1,211개 · 80만 줄 · 40% · 17% · 1,400만 회 · 20만 명)는 내레이션이 옮긴 값이다. 설명란: *"인터뷰 속 기억이 공식 글과 다른 곳(Rust 이전의 원래 언어, 롤백한 팀)은 공식 글을 따라 바로잡았습니다."* — 바로잡은 내용은 03:58~04:00과 04:22~04:27에 있고, **Nadella의 원래 발화는 캡션에 남지 않았다.**


## 설명란

마이크로소프트 CEO 사티아 나델라가 The Pragmatic Engineer 팟캐스트에서 인정했습니다. 코딩 도구의 무게중심이 IDE에서 터미널로 옮겨 간 계기는 앤트로픽의 Claude Code였고, 여섯 달 만에 IDE가 뒤로 밀려났다고요. 그가 꼽은 다음 문제는 코드가 아니라 검증입니다.

이 영상은 인터뷰에서 사티아가 한 말을 마이크로소프트·깃허브의 공식 글과 맞춰 봅니다. 엔지니어 9명이 하루에 PR 1,211개를 머지한 Copilot Cowork 팀, 깃허브 코파일럿 런타임의 Rust 이전, 자발적 퇴직 제안, AI가 찾아내는 취약점, "모델을 아무거나 갈아 끼워도 우리 평가 점수가 오르는가"라는 시금석, 에이전트를 내부자 위험으로 다루는 신뢰 아키텍처까지. 인터뷰 속 기억이 공식 글과 다른 곳(Rust 이전의 원래 언어, 롤백한 팀)은 공식 글을 따라 바로잡았습니다.

타임라인
0:00 6개월 만에 IDE가 밀려났다
0:27 왜 놓쳤나
2:26 싸진 것과 비싸진 것: 검증
3:48 소프트웨어 팩토리
5:51 빈 땅이 아닌 곳: 윈도우와 깃허브
7:39 사람은: 전문성, 자발적 퇴직 제안, 불안
9:44 신입은
10:44 모델은 누가 쥐나
12:49 신뢰 아키텍처
14:00 학생 모드

참고
원본 인터뷰: https://www.youtube.com/watch?v=0NE89Nzfk20
The Pragmatic Engineer 에피소드 글: https://newsletter.pragmaticengineer.com/p/software-engineering-after-code-becomes
Copilot Cowork (Bas Brekelmans): https://commandline.microsoft.com/how-we-built-copilot-cowork-python-to-rust-migration/
GitHub Copilot 런타임 Rust 이전 (Stephen Toub): https://github.blog/ai-and-ml/generative-ai/migrating-the-github-copilot-runtime-to-rust-using-copilot/
PRAISE 프리셉터십 (Mark Russinovich, Scott Hanselman): https://commandline.microsoft.com/praise-preceptor-ai-accelerated-software-engineering-cmu/
자발적 퇴직 제안 (Amy Coleman): https://blogs.microsoft.com/blog/2026/10/26/introducing-a-voluntary-exit-offer/
MSRC Patch Tuesday 공지: https://www.microsoft.com/en-us/msrc/blog/2026/05/a-note-on-patch-tuesday
GitHub Octoverse: https://github.blog/news-insights/octoverse/octoverse-commits-pushes-reach-new-highs-in-2026-as-developers-build-with-agents/
Models as Insider Risks (Satya Nadella): https://snscratchpad.com/posts/models-as-insider-risks/

#SatyaNadella #마이크로소프트 #ClaudeCode #GitHubCopilot #AI코딩

> info.json `tags`: AI 코딩 · Anthropic · Claude Code · GitHub Copilot · Microsoft · Pragmatic Engineer · Satya Nadella · 검증 · 깃허브 코파일럿 · 마이크로소프트 · 사티아 나델라 · 소프트웨어 팩토리 · 앤트로픽 · 클로드 코드

## 트랜스크립트 — ko-orig (Korean original, ASR variant=gemini)

[00:00] VS 코드를 만드는 회사의 CEO가
[00:02] 인정했습니다. 여섯 달 만에 IDE가
[00:04] 밀려났다고요.
[00:15] 터미널에서 일을 통째로 맡기는
[00:16] 방식이죠.
[00:18] 귀가 꼽은 다음 문제는 검증입니다.
[00:20] 코드가 싸진 뒤 엔지니어는 무슨 일을
[00:22] 하게 될까요?
[00:23] 끝에는 CEO 본인이 들어가고 싶다는
[00:25] 팀도 나옵니다.
[00:27] 이 대화는 11월 16일 개발자
[00:29] 뉴스레터 프래그머틱 엔지니어의
[00:31] 팟캐스트에 올라왔습니다. 진행자
[00:32] 거게이 오로스는 마이크로소프트에서
[00:34] 일했던 엔지니어입니다. 사티아
[00:36] 나델라는 썬 마이크로시스템즈
[00:38] 엔지니어러 출발한 CEO고요. 녹화
[00:40] 는 레드먼드 본사에서 했습니다.
[00:42] 거게이는 마이크로소프트가 누구보다
[00:43] 빨랐다고 짚습니다. 챗 GPT보다
[00:45] 먼저 깃허브 코파일럿을 내놨으니까요.
[00:48] 커서가 나온 뒤에도 코파일럿은 나란히
[00:49] 달렸습니다. 그런데 2025년 클로드
[00:52] 코드가 나옵니다.
[00:54] 거게이가 묻습니다. 개발자 DNA가
[00:55] 몸에 밴 회사가 이 변화를 어떻게
[00:57] 놓쳤냐고요.
[01:25] 모델이 계단처럼 뛰면 제품의 형태도
[01:28] 곧바로 바뀌어야 한다. 만든 것과
[01:29] 사랑에 빠지지 말라는 거죠.
[02:07] >> 예전에는 사람이 코드를 넣었다면 이제
[02:09] 코드는 나오는 쪽입니다. 사람이 넣는
[02:11] 건 스펙과 마크다운이고요.
[02:15] 다만 사티아는 IDE가 끝났다고 보진
[02:17] 않습니다. 새 종류의 모델이 오면
[02:19] IDE가 다시 태어날 수도 있다고요.
[02:21] 형태가 하나로 붙는 게 아니라 모델의
[02:23] 능력에 맞춰 여러 형태가 함께 간다는
[02:25] 겁니다.
[02:26] 그럼 코드가 싸진 세상에서 비싸진 건
[02:29] 뭘까요? 사티아의 답은 검증입니다.
[03:27] 실패 하나가 테스트 하나가 되고 그
[03:29] 순서가 쌓여 팀의 새 노하우가
[03:30] 됩니다. 그리고 방금 사티아가 들어가
[03:32] 보고 싶다던 프리셉터십. 이 이야기는
[03:34] 끝에서 다시 나옵니다.
[03:36] 검증을 누가 하느냐도 중요합니다.
[03:38] 사티아는 모델 가문을 따로 두고 다른
[03:40] 가문에게 비평을 맡기라고 합니다.
[03:42] 한 모델 가문의 약점이 내 제품의
[03:44] 약점이 되지 않게 다른 가문의 눈으로
[03:45] 한 번 더 보는 겁니다.
[03:48] 요즘 자주 듣는 말이 소프트웨어
[03:50] 팩토리입니다. 사티아도 아직 감을
[03:52] 잡는 중이라며 블로그 두 편을
[03:53] 가리킵니다.
[03:55] 하나는 깃허브 코파일럿 런타임을
[03:56] 러스트로 옮긴 글입니다.
[03:58] 사티아는 파이선이라 했지만 원래는
[04:00] 타입스크립트였습니다. 80만 줄이
[04:02] 넘는 러스트 코드를 주로 개발자 한
[04:03] 명이 몇 달 만에 옮겼다고
[04:05] 적었습니다. 혼자만의 일은 아니었다고
[04:07] 덧붙이면서요.
[04:08] 다른 하나가 사티아가 말한 바스 의
[04:10] 글, 코파일럿 코어 코드 팀입니다.
[04:12] [음악] 엔지니어 아홉 명이 하루에
[04:14] 풀 리퀘스트 1,211개를 머지했다고
[04:16] 요.
[04:17] 코드는 대부분 에이전트가 썼지만 이를
[04:19] 경유하고 결과를 판단하는 건 엔지니어
[04:21] 몫이었다고 합니다.
[04:22] 앞서 사티아가 말한 되돌려야 했던
[04:24] 러스트 이전도 사실 이 팀의
[04:25] 일입니다. 파이썬에서 러스트로 옮기다
[04:27] 첫 시도를 되돌렸다고 적혀 있습니다.
[04:30] 그가 정리한 변화는 셋입니다.
[04:32] 코드는 입력에서 출력이 됐고 그래서
[04:34] 스펙과 의도가 중요해졌습니다.
[04:36] 공장에서는 모든 게 문서로 남아서
[04:38] 신입의 온보딩이 오히려 쉬워졌다고요.
[04:40] 그가 특히 반기는 건 운영에서
[04:42] 돌아오는 로그입니다.
[05:07] 운영 로그로 고치고 모든 테스트를
[05:08] 통과했는지 확인한 뒤 배포까지.
[05:11] 남들이 말하는 RSI가 자기한테는
[05:13] 이퀄이라는 겁니다.
[05:14] 사티아가 가장 아낀다는 사례도
[05:15] 있습니다. 전 세계 광 케이블 망을
[05:17] 운영하는 애저 네트워크 팀입니다.
[05:45] 일을 직접 하던 팀이 이제 일을 하는
[05:47] 공장을 지었습니다. 그래도 그 역시
[05:49] 일이라고 사티아는 덧붙입니다.
[05:51] 그런데 대부분의 팀은 빈 땅에서
[05:53] 시작하지 않습니다. 고객이 쓰는
[05:55] 제품이 이미 돌아가고 있죠. 거기
[05:56] 애가 묻는 것도 이거입니다.
[05:59] 사티아가 드는 예는 윈도우입니다.
[06:01] 마이크로소프트 보안 팀은 올해 패치
[06:03] 규모가 당분간 계속 커질거라고
[06:05] 공지했습니다.
[06:06] 고급 AI 모델이 취약점을 찾는
[06:08] 속도를 끌어올리고 있다는 겁니다.
[06:34] 새 공장을 지어도 바닥의 빌드와
[06:36] CICD는 그대로입니다.
[06:37] 브라운필드에서는 거기가 가장 풀기
[06:39] 어려운 병목이라고 사티아는 말합니다.
[06:42] 깃허브는 더 극적입니다. 공장
[06:43] 밑바닥까지 다시 깔고 있다고요.
[07:08] 깃허브 옥토버스 보고서로는 9월에 풀
[07:10] 리퀘스트의 40% 넘게가 에이전트
[07:12] 초안에서 시작했습니다. 3월에
[07:14] 17%였고요.
[07:15] 거기가 한 번 더 묻습니다.
[07:17] 리액트가 나왔을 때도 새 기능부터
[07:19] 섞었었는데 이번엔 뭐가 다르냐고요.
[07:22] 사티아는 대학에서 페이엑스 단말기로
[07:24] 일을 배웠고 썬의 워크스테이션을 거쳐
[07:26] 마이크로소프트로 왔습니다.
[07:27] 그동안 프레임워크와 런타임은 바뀌어도
[07:29] IDE에서 코드를 쓰는 일은
[07:31] 그대로였죠. 이번엔 그게 한꺼번에
[07:33] 바뀝니다.
[07:34] 게다가 새 모델이 언제 나올지
[07:35] 모릅니다. 판이 언제든 다시 바뀔 수
[07:37] 있다는데 대비하라고 사티아는
[07:38] 말합니다.
[07:40] 그럼 수십 년 동안 코딩을 갈고 닦은
[07:42] 사람은 어떻게 될까요? 거기 본인도
[07:44] 받아들이기 어려웠다고 털어놓습니다.
[08:15] >> 전문성이 값을 잃는 게 아니라 그
[08:16] 전문성을 새 지렛대로 쓰는 법을
[08:18] 익혀야 한다는 겁니다.
[08:19] 작년 깃허브 유니버스에서 그는
[08:21] 코파일럿 이전의 아이디를 모르고 자란
[08:22] 첫 졸업생들을 만났다고 합니다.
[08:25] 그 다음 질문은 민감합니다.
[08:26] 마이크로소프트는 10월 26일 자발적
[08:28] 퇴직 제안을 발표했습니다. 해고의
[08:29] 전조니 하는 겁니다.
[08:31] 공지에는 캐나다, 인도, 영국,
[08:33] 미국의 참여 팀이 대상이라고만 있고
[08:35] 인원수나 AI 이야기는 없습니다.
[08:37] 거기에는 전례없는 일이라고 했지만
[08:39] 4월에 자발적 은퇴 프로그램에 이어
[08:40] 올해 두 번째입니다.
[08:42] 사티아의 답은 선택권입니다. 회사
[08:44] 안에서 바뀌는 팀으로 옮겨가거나
[08:45] 원하면 떠날 수 있게 한다는 거죠.
[09:05] 업계가 사람들에게 큰 불안을
[09:07] 만들었다는 것도 인정합니다.
[09:37] 그러면서 빠르게 늘어나는 직무로
[09:39] 포워드 디플로이드 엔지니어, FDE를
[09:40] 꼽습니다.
[09:41] 고객 곁에서 직접 만드는 엔지니어죠.
[09:44] 신입 채용은 어떨까요? 많은 회사가가
[09:47] AI는 경력자가 제일 잘 쓴다며 신입
[09:49] 채용을 줄이고 있습니다.
[10:32] >> AI는 이티 회사는 토큰 예산과 사람
[10:34] 한 명으로 시작합니다. 그 사람이
[10:36] 예산을 다 쓰면 다음 사람을 더
[10:37] 하죠.
[10:38] 지금은 그 공장을 짓느라 채용이
[10:40] 느려진 것이고 장기 추세로 읽기엔
[10:42] 이르다는 게 사티아의 전망입니다.
[10:45] 이제 회사 쪽 이야기입니다. 사티아는
[10:47] 세상의 지식을 다 가진 모델 하나가
[10:49] 나온다는 생각을 믿지 않습니다.
[10:50] 그리고 하이에크를 꺼냅니다.
[11:25] 사람과 함께 토큰이 회사의 자본이
[11:26] 된다는 거죠. 그 토큰 자본은 회사
[11:28] 지식을 담은 오픈 모델일 수도
[11:30] 컨텍스트 층일 수도 있다고고요.
[11:32] 그래서 하네스와 컨텍스트, 메모리,
[11:34] 행동 공간을 특정 모델과 떼어
[11:36] 놓으라고 합니다. 안 그러면 꼼짝없이
[11:38] 묶인다고요.
[11:52] 회사가 내려야 할 아키텍처 결정은 두
[11:54] 가지라고 합니다. 첫째는 학습 고리를
[11:56] 지키는 일입니다.
[12:31] >> Yeah.
[12:40] Yeah.
[12:43] >> 우리 팀에 던져 볼 만한 질문입니다.
[12:45] 내일 모델을 바꿔도 우리 만의 평가
[12:47] 점수는 계속 오를까요?
[12:50] 마지막 경고는 신뢰입니다. 모델은
[12:52] 점점 유능해지는데 그만큼
[12:54] 믿을만해지지는 않는다는 거죠.
[13:34] 이 생각은 사티아가 10월에 자기
[13:36] 블로그에 먼저 썼습니다. 지능의
[13:37] 공급과 그 위에 권한을 떼어 놓아야
[13:39] 한다고요.
[13:40] 엑셀에 올린 같은 글은 조회수
[13:42] 1,400만 회를 넘겼습니다.
[13:44] 닫힌 모델이든 오픈 모델이든 내부자
[13:46] 위험처럼 다루자는 글이죠.
[13:49] 생각의 사슬은 사람이 읽을 수 있는
[13:50] 말로 손댈 수 없게 기록해 둬야
[13:52] 한다고도 말합니다.
[13:53] 반가운 소식도 있습니다.
[13:55] 작년에 최전선 모델이 이제 노트북에서
[13:57] 돈다는 거죠. 그는 이걸 계량기 없는
[13:59] 지능이라고 부릅니다.
[14:01] 그럼 엔지니어는 뭘 해야 할까요?
[14:03] 그 전에 사티아가 대화 중간에
[14:04] 털어놓은 꿈의 다음 직업부터
[14:06] 듣겠습니다.
[14:31] >> 로시노비치와 헨슬먼이 10월에 소개한
[14:33] 프로그램 프레이즈입니다. 신입
[14:34] 엔지니어를 선배 프리셉터와 짝지어
[14:36] 주는 제도죠.
[14:37] 프리셉터십은 간호 분야에서 빌려온
[14:39] 개념이고 카네기 멜론 대학과 함께
[14:41] 운영합니다.
[14:44] 직원 20만 명이 넘는 회사의
[14:45] CEO가 신입처럼 그런 팀에 들어가
[14:47] 배우고 싶다는 겁니다.
[14:49] 마지막 조언도 같은 방향입니다.
[14:51] >> Experience it
[14:52] firsthand. That's,
[14:52] you know, quite
[14:53] frankly, that's kind
[14:54] of what I would even
[14:54] say for me. If I
[14:56] could change the
[14:57] ratio of my, you
[14:59] know, talk to do, I
[15:01] would do it. This is
[15:02] the time if one
[15:03] piece of advice,
[15:03] whether you're
[15:04] mid-career or even a
[15:05] CEO like me or or a
[15:08] fresh college grad.
[15:10] The more you can
[15:11] take the time to
[15:13] sort of learn, to
[15:15] do, be in teams that
[15:17] are doing,
[15:18] the better it is
[15:20] versus
[15:22] I think anything
[15:22] else. Because at
[15:23] times like some some
[15:25] level I sometimes
[15:25] think about it and
[15:26] when am I at my
[15:27] best? It's when I'm
[15:28] in this school mode.
[15:30] So let's get back to
[15:31] school.
[15:33] >> 여섯 달 만에 ID를 밀어낸 변화
[15:35] 앞에서 CEO가 고른 자리는 배우는
[15:37] 쪽이었습니다.
[15:38] 코드가 싸진 지금 여러분 팀에서 가장
[15:40] 먼저 지어 볼 공장은 무엇인가요?

## 트랜스크립트 — en-orig (내레이션 자리는 영어 더빙 ASR(인용하지 않음) · 인터뷰 발췌 자리는 Nadella 원음(단일 트랙))

[00:00] The CEO of the company that created VS
[00:02] Code has admitted it. Did the IDE get
[00:04] pushed aside in just six months?
[00:12] >> The one that pushed it out was
[00:14] Anthropic’s Claude Code. It’s a method
[00:16] where you hand everything over in the
[00:17] terminal. The next problem he pointed
[00:19] out is verification. What will engineers
[00:21] do once code becomes cheap?
[00:23] At the end, he even mentions a team he
[00:25] wants to join himself. This conversation
[00:28] was released on the Pragmatic Engineer
[00:30] newsletter podcast on November 16th. The
[00:32] host, Gergely Orosz, is an engineer who
[00:34] used to work at Microsoft. Satya Nadella
[00:36] is a CEO who started out as an engineer
[00:38] at Sun Microsystems. The recording took
[00:40] place at the headquarters in Redmond. He
[00:42] acknowledges that Microsoft there was
[00:43] faster than anyone else. After all, they
[00:46] released GitHub Copilot before ChatGPT.
[00:48] Even after ChatGPT came out, Copilot ran
[00:49] right alongside it. But then, in 2025,
[00:52] Claude Code arrived. Gergely asks him
[00:54] this. How did a company with developer
[00:56] DNA in its bones miss this change?
[01:00] One of the keys of building with models
[01:02] is when model jumps happen nonlinearly,
[01:05] the form factor has to change quickly,
[01:07] right?
[01:09] That's the, you know, what is AI first
[01:10] product building.
[01:12] In that sense, is unforgiving because
[01:15] when you have to be basically build
[01:17] everything around and be ready for the
[01:19] next capabilities and,
[01:26] When models jump like a staircase, the
[01:27] product's form must change immediately.
[01:29] It means don't fall in love with what
[01:30] you've built.
[01:34] Truly made the CLI as a form factor, and
[01:37] then you could even just say just
[01:40] complete full handling of, you know,
[01:42] code went from input to output
[01:44] effectively, right?
[01:46] I mean, that I think was the
[01:48] transformation in 6 months or so.
[01:50] We went primarily that, to your point
[01:53] about IDEs, ID kind of faded away, and
[01:55] then you really had this new way of
[01:57] thinking about code as input.
[02:00] And that's why if I look at the new IDE
[02:02] , it's more
[02:07] In the past, humans input the code, but
[02:10] now code is the output. What humans
[02:12] input are specs and Markdown.
[02:15] However, Satya does not believe the IDE
[02:17] is finished. He says when new types of
[02:19] models arrive, the IDE could be reborn.
[02:21] It’s not about sticking to one form, but
[02:23] having various forms coexist based on
[02:25] model capabilities.
[02:26] Then, in a world where code is cheap,
[02:28] what has become expensive? Satya’s
[02:30] answer is verification.
[02:45] Scott Henselman, you know, percepts or
[02:47] whatever they call because I kind of
[02:49] feel like I got to learn because I've
[02:51] not worked in a team that is mostly now
[02:53] code is output, right?
[02:55] But the code is output has a particular
[02:57] order of operations.
[02:59] It's not like code is output means
[03:01] everybody is just generating all sorts
[03:03] of random code like the way you got to
[03:04] build the verification stuff.
[03:07] How do you take every failure and then
[03:09] build the test case and make sure you
[03:11] truly verify the test, right?
[03:13] I mean there's just so much I would say
[03:16] new type of tribal knowledge people are
[03:18] building up in many ways.
[03:27] Each one becomes a test, and as that
[03:29] sequence accumulates, it becomes the
[03:30] team's new know-how. And there's the
[03:31] preceptorship that Satya just mentioned
[03:33] wanting to look into. This story will
[03:34] come back at the end. Who performs the
[03:37] verification is also important. Satya
[03:38] suggests keeping model families separate
[03:40] and having them critique one another.
[03:42] It’s about having another set of eyes
[03:43] check your work so one model family’s
[03:45] weaknesses don't become your product’s
[03:47] weaknesses.
[03:48] A term we hear often these days is "
[03:50] software factory." Satya points to two
[03:52] blog posts, saying he is still getting
[03:54] the hang of it himself. One is about
[03:56] moving the GitHub Copilot runtime to
[03:58] Rust. Satya mentioned Python, but it was
[04:00] originally TypeScript. It notes that a
[04:02] single primary developer migrated over
[04:04] 800,000 lines of Rust code in just a few
[04:05] months. Adding, of course, that it
[04:07] wasn't just a one-person job.
[04:09] The other is the GitHub Copilot Core
[04:11] team that Satya mentioned.
[04:13] Nine engineers merged 1,211 pull
[04:15] requests in a single day. Most of the
[04:17] code was written by agents, but guiding
[04:19] them and judging the results was the
[04:21] engineers 'responsibility. The Rust
[04:22] migration that Satya mentioned earlier—
[04:24] the one that had to be rolled back—was
[04:25] actually this team's work as well. It
[04:26] was noted that their first attempt to
[04:28] move from Python to Rust had to be
[04:29] reverted. He summarized the changes into
[04:31] three points. Code has shifted from
[04:33] input to output, which is why specs and
[04:35] intent have become critical. He says
[04:36] that in a factory, everything is
[04:38] documented, which actually makes
[04:39] onboarding for new hires easier. What he
[04:41] particularly welcomes are the logs
[04:42] returning from operations.
[04:47] RSI right which is it's sort of the
[04:49] ability to take my production logs and
[04:52] then to be able to verify the fix in
[04:55] fact that verifiability loop is great
[04:57] that you can then deploy the fix andy
[05:00] all the way through that passed all the
[05:03] testful
[05:06] and
[05:07] >> He says that for him, what others call "
[05:09] RSI"—fixing issues in operations,
[05:10] verifying they pass all tests, and then
[05:12] deploying—is essentially quality. There
[05:14] is also a case study that Satya
[05:16] cherishes the most. It is the Azure
[05:17] network team that operates cable
[05:18] networks all around the world.
[05:23] Fiber operators all over the world for
[05:25] our global network, and you know, always
[05:27] it's a physical asset, something or the
[05:29] other goes wrong. You know, the fancy
[05:32] word for managing all that is devops,
[05:34] but the reality is emails and you know
[05:37] all sorts of processes. And so, they
[05:39] went
[05:45] The team builds a factory to work in
[05:47] directly. But Satya adds that it is
[05:50] still work, nonetheless. However, most
[05:52] teams do not start on empty ground. The
[05:54] products customers use are already
[05:56] running. This is what GitHub is asking,
[05:58] too.
[05:59] The example Satya gives is Windows.
[06:02] The Microsoft security team predicted
[06:03] that the scale of patches will continue
[06:05] to grow for the time being.
[06:06] Advanced AI models are accelerating the
[06:09] speed of finding vulnerabilities.
[06:13] CV
[06:15] because you have AI mods that are
[06:19] and so we need to go fix them all and so
[06:21] there's a new pipeline.
[06:23] in fact if I look at the windows from
[06:26] crash traces all the way to fixes they
[06:29] are building
[06:34] >> Even if you build a new factory, the
[06:36] underlying build and CICD remain the
[06:37] same. Satya says that in brownfield
[06:39] sites, that is the hardest bottleneck to
[06:41] solve. GitHub is even more dramatic. Are
[06:44] they relaying the very foundation of the
[06:45] factory?
[06:50] the amount of change underneath even
[06:51] GitHub right which is if you think about
[06:53] it right you know weve had I mean
[06:55] suddenly all these coding agents showed
[06:57] up to work and get up and the scale has
[06:59] gone through the superhuman level and so
[07:01] we have to change the entire
[07:05] so are working on part of
[07:08] >> According to the GitHub Octoverse report
[07:10] , over 40%of pull requests in September
[07:12] started with agent drafts. It was 17%
[07:14] back in March.
[07:15] GitHub asks one more time. When React
[07:18] came out, we incorporated new features
[07:20] too, so what makes this time different?
[07:22] Satya learned to work on terminals in
[07:24] college and came to Microsoft after
[07:26] passing through Sun workstations.
[07:27] Meanwhile, while frameworks and runtimes
[07:29] changed, the act of writing code in an
[07:31] IDE remained the same. This time,
[07:32] everything is changing all at once.
[07:34] Furthermore, we don't know when new
[07:35] models will be released. Satya says to
[07:37] be prepared for the landscape to change
[07:39] at any moment.
[07:40] Then what happens to those who have
[07:41] honed their coding skills for decades?
[07:43] GitHub confesses that it was difficult
[07:44] for him to accept as well.
[07:46] and
[07:49] prodctions are requir
[07:57] of oper tool ch
[08:04] reasons where i don't think about
[08:06] devaluing the experti
[08:10] and making sure that you can exercise
[08:13] that with new leverage, meaning you
[08:15] shouldn't devalue your expertise, but
[08:17] learn how to use it as a new lever. He
[08:19] says that at last year's GitHub Universe
[08:21] , he met the first graduates who grew up
[08:23] without knowing an IDE before Copilot.
[08:25] The next question is sensitive.
[08:26] Microsoft announced a voluntary
[08:28] retirement plan on October 26th. They
[08:30] say it is a precursor to layoffs. The
[08:31] notice only mentions that teams in
[08:33] Canada, India, the UK, and the US are
[08:35] subject to it, with no mention of
[08:36] headcount or AI. Although they called it
[08:38] an unprecedented event, it is the second
[08:39] one this year following the voluntary
[08:41] retirement program in April. Satya’s
[08:42] answer is choice. He means allowing
[08:44] people to move to changing teams within
[08:45] the company or to leave if they want to
[08:47] .
[09:06] He also acknowledges that the industry
[09:07] has created significant anxiety for
[09:09] people.
[09:23] Because the way we have talked about
[09:26] this AI revolution is yeah you know
[09:28] people say hey this maybe you know the
[09:31] singularity is here and maybe we are
[09:33] building company or be jobs
[09:37] >> He points to Forward Deployed Engineers
[09:39] (FDE) as a rapidly growing job role.
[09:41] They are engineers who build things
[09:43] directly alongside the customer. What
[09:44] about hiring new graduates? Many
[09:46] companies are reducing entry-level
[09:48] hiring, claiming that experienced
[09:50] workers use AI the best.
[10:08] industry high or a new col you add to
[10:12] this and so little of what happening i
[10:15] think is the slowd may be a slowd to get
[10:19] those qu and qu new factories of
[10:22] software engineing built such that new
[10:26] inputs not to hum can come and in newage
[10:33] >> AI-native budgets start with a token
[10:34] budget and one person. When that person
[10:36] uses up the budget, you add the next
[10:37] person. Satya’s outlook is that hiring
[10:39] has slowed down because we are currently
[10:41] building those factories, and it is too
[10:42] early to view it as a long-term trend.
[10:45] Now, let’s talk about the company side.
[10:46] Satya does not believe in the idea that
[10:48] one model will emerge containing all the
[10:50] knowledge in the world. And he brings up
[10:52] Hayek.
[10:54] after all if you go back to actually his
[10:57] description of what an economy is.
[11:00] It's all about knowledge being
[11:02] distributed. Right?
[11:04] In fact, you know his entire thing about
[11:06] pricing is a beautiful of explanation of
[11:09] he because of knowledge being tassed and
[11:12] distributed throughout the economy and
[11:14] every firm needs to be in control of it
[11:16] .
[11:18] And if so, then I would even say every
[11:22] human capal and cap.
[11:25] >> He means that alongside humans, tokens
[11:26] are becoming a company’s capital. That
[11:28] token capital could be an open model
[11:29] containing company knowledge, or it
[11:31] could be a context layer. That is why he
[11:33] says to decouple your harness, context,
[11:35] memory, and action space from any
[11:36] specific model. Otherwise, you’ll be
[11:38] trapped with no way out. how are you
[11:41] migrate your memory out if your memory
[11:45] iss of
[11:47] comp 가
[11:52] He says there are two architectural
[11:54] decisions that must be made. The first
[11:55] is to protect your learning loop.
[11:57] And there are two are how do you avoid
[11:59] this reverse information paradox which
[12:01] is don't leak your value. You as a firm
[12:03] need to be in charge and control of your
[12:06] own learning loop. What's the
[12:07] architectural approach?
[12:09] How are you making sure your context is
[12:11] separate from the models and you're
[12:13] using multiple models, and your harness
[12:15] is separate from the context and the
[12:16] models?
[12:17] Because that I think is the only way you
[12:20] can assure yourself that you can replace
[12:22] any model.
[12:24] In fact, my acid test for that is you
[12:26] should be able to replace any model and
[12:28] still clear an eval—that's your private
[12:31] eval.
[12:32] If you can't do that, then you have to
[12:35] ask yourself, how are you a firm, right
[12:38] ? Like, that means you do not have...
[12:43] >> This is a question worth throwing at
[12:45] your team. Even if we change models
[12:46] tomorrow, will our proprietary
[12:48] evaluation scores continue to rise?
[12:50] The final warning is about trust. Models
[12:52] are becoming increasingly capable, but
[12:54] they aren't necessarily becoming more
[12:55] reliable.
[12:57] In a world where you now know scaling
[13:00] laws work, except with scaling comes new
[13:02] capability but not alignment.
[13:05] In fact, no mechanistic understanding
[13:07] that hopefully someday there is a
[13:08] science breakthrough, but right now we
[13:10] are getting more and more capable and
[13:12] less and less reliable, which is the
[13:14] most dangerous place to be in.
[13:16] And so that means you have to separate
[13:18] out architecturally authority from
[13:20] intelligence. If your intelligence has
[13:22] authority and is unreliable, again,
[13:24] you're taken, right? You have a...
[13:34] Satya wrote about this idea on his blog
[13:36] back in October. He argued that we must
[13:38] decouple the supply of intelligence from
[13:39] the authority granted to it. The same
[13:41] post he shared on X surpassed 14 million
[13:43] views. It is a post arguing that we
[13:45] should treat both closed and open models
[13:47] like insider threats.
[13:49] He also states that chains of thought
[13:51] should be recorded in human-readable,
[13:52] tamper-proof formats. There is also some
[13:54] welcome news. Models that were at the
[13:56] frontier last year can now run on a
[13:57] laptop. He calls this "unmetered
[13:59] intelligence."
[14:01] So, what should engineers do?
[14:03] But first, let's hear about the dream
[14:05] job Satya mentioned during our
[14:06] conversation.
[14:25] Microsoft.
[14:31] It is the "Praxis" program introduced by
[14:33] Russinovich and Hanse in October. It is
[14:34] a system that pairs new engineers with
[14:36] senior preceptors.
[14:37] "Preceptorship" is a concept borrowed
[14:39] from the nursing field, and it is
[14:40] operated in collaboration with Carnegie
[14:42] Mellon University.
[14:44] The CEO of a company with over 200,000
[14:46] employees is saying he wants to join
[14:47] such a team to learn like a recruit. His
[14:49] final piece of advice points in the same
[14:50] direction.
[15:01] I would do it.
[15:02] If there is one piece of advice, whether
[15:06] you're a manager or even a CEO like me
[15:09] or a fresh college grad, the more you
[15:12] can take the time to learn and be on
[15:15] teams that are doing, the better it is,
[15:18] versus I think anything else.
[15:22] Because at some level, I sometimes think
[15:25] about it, I'm at my best when I'm in
[15:27] school mode.
[15:30] So, let's get back to...
[15:33] Faced with changes that pushed aside IDs
[15:35] in just six months, the CEO chose the
[15:37] seat of a learner. Now that code has
[15:39] become cheaper, what is the first
[15:40] factory your team will build? M.
