---
title: "'두 번 확인해' 한 줄에 비용 48% 샜다 | 옛날 프롬프트가 Claude를 망치는 이유 (Anthropic Lance Martin)"
type: video
source: https://www.youtube.com/watch?v=BqUhlnVlEbo
site: youtube.com
author:
  - "[[Tech Bridge]]"
duration: 6:36
published: 2026-11-08
created: 2026-11-09
description: "Tech Bridge 한국어 해설 6:36, 공식 챕터 8, 전부 내레이션(영어 원음 발췌 없음). Anthropic Lance Martin의 AI Engineer 워크숍 *Your Old Prompts Are Making Claude Worse*와 Claude 블로그 두 글(위키 미열람)의 2차 전달: 모순된 규칙 두 줄로 환불 4건을 보류한 고객센터 AI, '두 번 검증' 한 줄 비용 +48%, 프롬프트에도 빚이 쌓인다(/claude-api prompt-audit, 비용 18% + 9% ↓), 프롬프트 캐시(10분의 1 단가, 타임스탬프가 캐시를 깸, 층 순서, τ²-bench 93% 캐시 · 73% ↓), 오를 수 있는 평가의 네 조건과 막힌 문제(build-eval), 학습/시험 분할 hillclimb(Claude API 스킬 66% → 87.9%), 비용 목표(4.6센트 → 1센트, 시험용 14건 78.6% → 90.5%), 똑똑한 모델을 덜 애쓰게, 4분 → 12시간 → 하루 이틀 작업과 Managed Agents 하네스 · 샌드박스 분리 · vault. 모델 버전 일부(오퍼스 5.0 · 5.1)는 ASR 미확정."
tags:
  - clippings/youtube
---

**Source URL**: https://www.youtube.com/watch?v=BqUhlnVlEbo
**Channel**: Tech Bridge · **Duration**: 6:36 · **Published**: 2026-11-08

> **게시일.** info.json 기준 `upload_date` **`20261108`**(UTC), `timestamp` 1794128415(= 2026-11-08 09:00:15 UTC = **2026-11-08 18:00 KST**), `availability: public`. 2026-11-08 회차(09:10 KST 발화) 뒤에 올라와 2026-11-09 회차 목록 맨 위에 처음 나왔다.
>
> **오디오 트랙과 자막 — 인용 규칙.** 오디오는 `Korean original (default)` + 영어(`en` · `en-US`, 더빙) 두 계열이고, 메타 `language`=`en`이다. 수동 자막은 없다. `ko`와 `ko-orig`는 **md5가 같다**(`kind=asr&lang=ko&variant=gemini` 원 ASR). `en-orig`(`lang=en&variant=timing-optimized`)는 **영어 더빙 트랙의 ASR**이고, `en`(`lang=ko&tlang=en`)은 ko의 기계 번역이다. **이 영상엔 영어 원음 발췌가 없다** — en-orig는 처음부터 끝까지 내레이션의 번역 낭독이다. → **인용은 전부 ko-orig**로 하고, en-orig · `en`은 판독 대조에만 썼다. `--sleep-subtitles 8`로 429 없음.
>
> **형식 — Tech Bridge 한국어 해설, 공식 챕터 8.** 전부 내레이션이다. Lance Martin 본인의 목소리는 캡션에 없다 — 그의 말은 모두 해설자가 옮긴 것이다. 무캡션 간격은 네 곳이다(ko-orig · en-orig 둘 다 빈 구간): **00:49~00:59**(49.1→59.2초), **01:17~01:25**(77.0→85.0초), **03:10~03:14**(190.1→194.3초, 챕터 3:13 경계), **06:15~06:23**(375.2→383.7초). 무엇이 나오는지(음악 · 화면 · 무캡션 발췌)는 알 수 없다 — 내용을 추정하지 않는다. `[음악]` 표기가 04:18 · 05:31 · 06:27에 있다.
>
> **근거 자료.** 설명란 *참고* — Lance Martin, *Your Old Prompts Are Making Claude Worse*(AI Engineer, `ys6YQ2yfBpM`), Claude 블로그 *Reducing cost and improving performance with Claude Platform*, claude.dev *Automating eval design and hillclimbing with Claude*. **위키는 셋 다 열지 않았다.** 해설은 *"엔트로피가 직접 돌린 실험입니다. 블로그에 그대로 적혀 있죠."*(00:16~00:18)처럼 블로그를 여러 번 인용한다 — 수치는 전부 **Anthropic 자기 실험의 2차 전달**이다.
>
> ⚠️ **모델 이름 · 버전 — ASR과 더빙이 어긋난다, 확정하지 않는다.**
> - 01:58 *"오퍼스 4.8에서 5.5로"* — ko · en-orig(`Opus 4.8 to 5.5`) 일치.
> - 04:34 *"오퍼스 4.8 높은 노력"* · 04:40 *"오퍼스 5.0 낮은 노력"* · 04:46 *"소넷 5 낮은 노력"* — en-orig도 `Opus 4.8` · `Opus 5.0` · `Sonnet 5`. 01:58의 *5.5*와 04:40의 *5.0*이 같은 실험인지 다른 실험인지 발화되지 않는다. 위키에 Opus 4.8 · Opus 5.0 · Sonnet 5 페이지는 없다.
> - 05:14 *"페이블 5.1 낮은 노력이가 페이블 5 높은 노력과"* — `en`(ko 번역)은 `Fable`, **en-orig(영어 더빙)는 `Haiku 3.5` · `Haiku 3`** 로 전혀 다르다. 더빙 오류로 본다(위키 [[fable-5-1]]와 맞는 쪽은 ko).
> - 05:24 *"오퍼스 5.1 로우 부터"* — en-orig `Opus 3.5 "low"`(더빙 오류). 위키에 Opus 5.1은 없다. ASR이 *5.5*를 잘못 들었을 수 있으나 **오디오 확인 없이 고치지 않는다.**
>
> ⚠️ **ASR 판독(ko-orig).** *엔트로피*(00:16 · 00:35) → Anthropic(en-orig *Anthropic*), *렌스마틴* · *랜스 마틴* → Lance Martin, *정책 아니면 언제나 환불해라*(00:04) → 정책에 맞으면(추정, en-orig *if it meets the policy*), *조회할 환불 네 건*(00:12) → 줘야 할 환불 네 건(추정, en-orig *four refund requests*), *정확도를 9점 가깝고요*(00:28~00:30) → 9점 가깝게 깎았고요(문장 끊김, en-orig *lowered accuracy by nearly 9 points*), *고지곧대로* → 곧이곧대로, *클라우드 코드* → Claude Code, *슬래시 클라우드 API 프롬프트 오딧*(01:48~01:53) → `/claude-api prompt-audit`(설명란), *또는 체크업 프롬프트 오딧*(01:50) → 판독 불가(en-orig *check-up prompt-audit* 도 같은 소리를 옮긴 것), *스킬 클라우드 MD* → 스킬 · CLAUDE.md, *오디서* → auditor, *오퍼스 4.8에서 5.5로 해도* → 바꾸기만 해도(추정), *타우 투 벤치* → τ²-bench 추정(en-orig *Tao-bench*), *오피스 퀘이* → OfficeQA(en-orig *Office-QA*), *코스트 옵티마이즈* → cost-optimize 명령(설명란에 없음), *빌드, 이벨, 트레이스 같은 원본 데이터*(03:47) → `build-eval`(설명란)에 트레이스 같은 원본 데이터를(추정 — en-orig *builds, evals, and traces* 는 같은 소리를 나열로 옮겼다), *힐 클라임* → `hillclimb`(설명란), *규칙을 못 하자*(04:50) → 판독 불가(en-orig *setting rules*, 보완하자 · 추가하자 추정), *더 붙이기만 되는 기록*(05:50) → 덧붙이기만 되는(append-only), *금고에는 키를 참조만* → 금고(vault)의 키를 참조만(추정, en-orig *only references them in the vault*), *비밀번호를 지워주는 건*(06:01) → 쥐여주는 건(추정, en-orig *Giving a password*), *똑똑한 모델은 덜 쓰게*(06:10~06:12) → 덜 애쓰게(추정 — 05:02 원칙과 같은 말, en-orig *use smarter models less* 는 뜻이 다르다).
>
> ⚠️ **수치의 단위.** 04:46~04:50의 *"98.9%"* 는 실패 사례를 본 뒤의 점수라 **학습용** 점수로 읽힌다. 시험용(한 번도 안 본 티켓 14개)은 *78.6% → 90.5%*(04:53~04:57)다. 해설은 98.9%가 학습용이라고 명시하지 않는다. *"비용은 약 5분의 1"*(04:57~04:59)의 기준(4.6센트 → 1센트)도 명시되지 않는다.

## 설명란

'단계별로 생각해', '두 번 확인해'… 예전 모델에게 통하던 프롬프트 주문이 최신 Claude에서는 비용만 올리고 성능을 깎고 있었습니다.
Anthropic의 Lance Martin이 AI Engineer 워크숍에서 공개한 내용을 바탕으로, 모순된 규칙 두 줄 때문에 환불 4건을 보류한 고객센터 AI 실험에서 시작해 비용과 성능을 같이 잡는 다섯 가지 방법을 쉽게 풀어 봅니다. /claude-api prompt-audit, 프롬프트 캐시, 오를 수 있는 평가(build-eval), 과적합 없는 힐 클라이밍(hillclimb), 그리고 '똑똑한 모델을 덜 애쓰게' 하는 원칙까지.

타임라인
0:00 환불 4건을 안 준 고객센터 AI
0:40 프롬프트에도 빚이 쌓인다: prompt-audit
2:19 프롬프트 캐시: 타임스탬프 하나가 캐시를 깬다
3:13 클로드가 오를 수 있는 평가 만들기
3:54 과적합 없이 오르기: 66% → 87.9%
4:29 비용을 목표로: 4.6센트 → 1센트
5:27 며칠짜리 에이전트를 위한 하네스
6:04 정리

참고
Lance Martin, Your Old Prompts Are Making Claude Worse (AI Engineer): https://www.youtube.com/watch?v=ys6YQ2yfBpM
Reducing cost and improving performance with Claude Platform (Claude 블로그): https://claude.com/blog/reducing-cost-and-improving-performance-with-claude-platform
Automating eval design and hillclimbing with Claude (claude.dev): https://claude.dev/blog/automating-eval-design-and-hillclimbing/
썸네일 인물 사진: How founders build on Claude Managed Agents (Claude 공식 채널): https://www.youtube.com/watch?v=hm8NzEd5io0

#Claude #Anthropic #프롬프트엔지니어링 #ClaudeCode #AI에이전트

> info.json `tags`: AI 에이전트 · Anthropic · Claude · Claude Code · LLM 비용 · Lance Martin · eval · hill climbing · prompt audit · 프롬프트 엔지니어링 · 프롬프트 캐시

## 트랜스크립트 — ko (원 오디오 ASR, `lang=ko` — `ko-orig`와 바이트 동일 · 인용 근거)

[00:00] 고객센터 AI의 프롬프트에 몇 달
[00:02] 간격으로 규칙 두 줄이 붙었습니다.
[00:04] 정책 아니면 언제나 환불해라.
[00:06] 그리고 에스컬레이션 없이는 절대
[00:08] 환불하지 마라.
[00:10] 모델을 최신으로 바꾸자 이 AI는
[00:12] 조회할 환불 네 건을 붙잡고 고객에게
[00:14] 확인만 계속 요청했습니다.
[00:16] 엔트로피가 직접 돌린 실험입니다.
[00:18] 블로그에 그대로 적혀 있죠.
[00:21] 다른 주문도 있습니다.
[00:22] 답하기 전에 두 번 검증하라는 한
[00:23] 줄은 티켓당 비용을 48% 올렸는데
[00:26] 정확도는 그대로였어요.
[00:28] 모순된 규칙 한 쌍은 정확도를 9점
[00:30] 가깝고요.
[00:31] 예전 모델에게 통하던 주문이 이제는
[00:33] 돈을 쓰고 성능까지 깎는 겁니다.
[00:35] 오늘은 엔트로피 렌스마틴의 발표를
[00:37] 따라 이 빚을 갚는 다섯 가지 방법을
[00:39] 보겠습니다.
[00:41] 보통 비용과 품질은 맞바꾸는 관계라고
[00:43] 생각하죠. 더 잘하려면 더 써야 하고
[00:45] 아끼려면 성능을 포기해야 한다고요.
[00:59] 렌스마틴은 프롬프트에도 코드처럼 빚이
[01:01] 쌓인다고 말합니다.
[01:02] 몇 세대 전 모델에겐 단계별로
[01:04] 생각해라, 두 번 확인해라, 최대한
[01:06] 꼼꼼하게 같은 말이 필요했어요.
[01:08] 지금 모델은 언제 생각할지 스스로
[01:10] 고르고 알아서 검증합니다. 그런데 이
[01:12] 말이 남아 있으면 문자 그대로
[01:13] 따르느라 토큰을 더 쓰죠.
[01:25] 블로그 표현으로는 최신 모델은 이런
[01:26] 지시를 고지곧대로 받아들여서 토큰을
[01:28] 낭비합니다.
[01:30] 같은 주문 조회를 환불마다 두 번씩
[01:31] 했다고 해요.
[01:33] 더 심한 경우도 있었어요.
[01:34] 옛날 생각 설정이 남은 프롬프트는
[01:36] API가 요청을 전부 거절해 버렸고
[01:39] 직접 짜 놓은 스크래치패드는 모델의
[01:40] 내장 생각과 부딪혀서 티켓 세 건에선
[01:43] 도구 호출을 생각 속에만 쓰고
[01:44] 실행하지 않았습니다.
[01:46] 해결책은 명령어 하나입니다. 클라우드
[01:48] 코드에서 슬래시 클라우드 API
[01:50] 프롬프트 오딧 또는 체크업 프롬프트
[01:53] 오딧
[01:54] 스킬 클라우드 MD 프롬프트 도구
[01:56] 설명까지 훑어서 이런 패턴을
[01:57] 지워줍니다.
[01:58] 오퍼스 4.8에서 5.5로 해도
[02:00] 비용이 18%쯤 줄었는데 오디서를
[02:02] 한번 돌리자 9%가 더 줄었습니다.
[02:05] 정확도는 2% 포인트쯤 올랐고요.
[02:07] 랜스 마틴이 이 팁을 올린 게시물은
[02:09] 29만 회 넘게 조회됐습니다.
[02:11] 최신 모델의 발목을 잡는 패턴을
[02:12] 지워준다고요.
[02:14] 한 개발자는 자기 클로드 코드
[02:15] 설정에서 고칠 곳을 70개쯤 찾았다고
[02:17] 했죠.
[02:20] 두 번째는 프롬프트 캐시입니다.
[02:21] 에이전트는 턴마다 앞 부분을 거의
[02:23] 그대로 다시 보내요. 반복되는 앞
[02:25] 부분을 캐시에서 읽으면 랜스 마틴
[02:27] 말로는 기본 입력의 10분의 1
[02:29] 정도만 냅니다.
[02:30] 문제는 앞 부분이 바이트 하나까지
[02:32] 똑같아야 캐시가 맞는다는 거예요.
[02:34] 시스템 프롬프트에 현재 시각 하나만
[02:36] 넣어도 매번 처음부터 다시
[02:37] 계산합니다.
[02:39] 블로그에도 그대로 나옵니다. 시스템
[02:40] 프롬프트에 든 타임스탬프나 아이디가
[02:42] 캐시를 깬다고요.
[02:44] 그래서 순서가 중요합니다.
[02:45] 모두가 같이 쓰는 시스템 지시와
[02:47] 도구를 맨 앞에, 그다음 프로젝트별
[02:49] 클로드 MD, 세션 상태, 그리고 매
[02:51] 턴 늘어나는 메시지를 맨 뒤에.
[02:54] 앤트로픽이 비용 최적화 명령어 코스트
[02:56] 옵티마이즈를 벤치마크에 돌려봤더니
[02:58] 타우 투 벤치는 프롬프트의 93%를
[03:00] 캐시할 수 있었습니다. 통과율 변화
[03:02] 없이 비용은 73% 줄었죠.
[03:04] 문서 질의 응답 벤치마크 오피스
[03:06] 퀘이도 72% 가까이 줄었고요.
[03:14] 세 번째부터는 조금 더 근본적인
[03:15] 이야기입니다.
[03:16] 클로드는 스스로 고치는 걸 잘 해서
[03:18] 잘 만든 평가만 주면 점수를 알아서
[03:20] 올라갑니다. 이걸 힐 클라이밍이라고
[03:22] 부르죠.
[03:23] 좋은 평가는 네 가지를 만족합니다.
[03:25] 더 좋은 모델이 더 높은 점수를
[03:26] 받고, 더 많이 생각하면 점수가
[03:28] 오르고, 최고 모델도 만점과 거리가
[03:30] 있고, 돌릴 때마다 점수가 크게
[03:32] 흔들리지 않을 것.
[03:34] 함정은 애매한 문제입니다. 어떤
[03:36] 모델도 못 푸는 문제가 20% 섞여
[03:38] 있으면 올라갈 여지가 있어 보여도
[03:39] 실제로 막혀 있죠.
[03:41] 블로그는 몇 번을 돌려도 매 번
[03:42] 실패하는 문제를 의심하라고 합니다.
[03:45] 평가 만들기에도 명령어 가 있습니다.
[03:47] 빌드, 이벨, 트레이스 같은 원본
[03:49] 데이터를 주면 문제와 채점 기준을
[03:51] 같이 만들고 중간중간 사람에게 확인을
[03:53] 받습니다.
[03:54] 힐 클라이밍의 가장 큰 적은 과
[03:56] 적합입니다. 평가 문제에 OCR이
[03:58] 필요하다고 하네스의 OCR 도구를
[03:59] 붙이면 점수는 오르지만 실제
[04:01] 서비스에선 아무 소용이 없죠.
[04:03] 그래서 힐 클라임 명령은 평가를
[04:05] 학습용과 시험용으로 나눕니다.
[04:07] 클로드는 학습용 실패만 보고 고칠
[04:08] 곳을 찾고 시험용은 한 번도 보지
[04:10] 않아요.
[04:11] 학습 점수만 오르고 시험 점수가
[04:13] 그대로면 과적합을 의심하고 그 수정을
[04:15] 되돌립니다.
[04:16] 랜스 마틴은 이걸 클로드 API 스킬
[04:18] 자체에 돌렸습니다. [음악]
[04:19] 처음 점수는 66%. 빠진 기능 여덟
[04:21] 개를 채우고 클로드가 옛날 API
[04:23] 모양으로 코드를 쓴다는 걸 찾아내고
[04:25] 잘못된 채점기까지 고쳐서
[04:26] 24라운드만에 87.9%가 됐습니다.
[04:30] 힐 클라임은 비용을 목표로 둘 수
[04:31] 있습니다. 성능은 지키면서 비용만
[04:33] 줄여라.
[04:34] 출발은 오퍼스 4.8 높은 노력,
[04:36] 정확도 74.4%에 티켓당
[04:39] 4.6센트였죠.
[04:40] 프롬프트를 오딧하고 오퍼스 5.0
[04:42] 낮은 노력으로 바꾸자 87.8%에
[04:44] 1.9센트.
[04:46] 한 단계 아래 소넷 5 낮은 노력은
[04:48] 1센트였고 실패 사례를 보고 규칙을
[04:50] 못 하자 98.9%까지 올라갔습니다.
[04:53] 중요한 건 한 번도 안 본 시험용
[04:54] 티켓 14개입니다. 78.6%였던
[04:57] 정확도가 90.5%로 비용은 약
[04:59] 5분의 1로 줄었습니다.
[05:01] 여기서 나온 원칙이 하나 있습니다.
[05:02] 똑똑한 모델을 덜 애쓰게 하는 쪽이
[05:05] 덜 똑똑한 모델을 오래 고민시키는
[05:06] 것보다 싸고 잘한다는 거예요.
[05:14] 블로그 예시로는 커서 벤치에서 페이블
[05:16] 5.1 낮은 노력이가 페이블 5 높은
[05:18] 노력과 같은 성능을 3분의 1
[05:19] 비용으로 냈습니다.
[05:21] 그래서 랜스 마틴의 조언은
[05:22] 단순합니다. 맥스로 시작하지 말고
[05:24] 오퍼스 5.1 로우 부터 시작해
[05:26] 보라.
[05:27] 마지막은 앞으로 이야기입니다. 클로드
[05:29] 3 오퍼스가 혼자 할 수 있던 일은
[05:31] 사람 기준 4분 남짓이었는데 [음악]
[05:33] 발표 그래프에선 12시간까지 올라갔고
[05:35] 랜스 마틴은 이제 하루 이틀짜리 일을
[05:37] 넘보는 구간에 들어섰다고 말합니다.
[05:40] 며칠씩 도는 에이전트라면 밤사이
[05:41] 샌드박스가 죽어도 이어갈 수 있어야
[05:43] 합니다.
[05:44] 그래서 클로드 매니지드 에이전트는
[05:45] 두뇌인 하네스와 손인 샌드박스를 떼어
[05:47] 놓았어요.
[05:48] 작업 기록인 세션 로그는 둘과 따로
[05:50] 더 붙이기만 되는 기록으로 남습니다.
[05:52] 무엇이 죽든 로그에서 다시 살아나죠.
[05:55] 보안도 챙겼습니다. 클로드는 API
[05:57] 키를 직접 보지 못하고 금고에는 키를
[05:59] 참조만 해요.
[06:00] 며칠씩 혼자 일하는 에이전트에게
[06:01] 비밀번호를 지워주는 건 좀
[06:03] 무섭잖아요.
[06:04] 정리해
[06:05] 오래된 주문은 지우고 캐시로 지키고
[06:08] 오를 수 있는 평가를 만들고 과적합을
[06:10] 경계하며 오르고 똑똑한 모델은 덜
[06:12] 쓰게.
[06:23] 처음에 고객센터 AI로 돌아가 보면
[06:25] 문제는 모델이 아니었습니다.
[06:27] 몇 달 간격으로 덧붙인 규칙 [음악]
[06:29] 두 줄이었죠.
[06:30] 여러분의 클로드 MD에도 그런 두
[06:32] 줄이 있을지 모릅니다. 오늘 한번
[06:34] 오딧을 돌려 보세요.

## 트랜스크립트 — en-orig (영어 더빙 트랙 ASR — 전 구간 번역 낭독 · 대조용, 인용하지 않음)

[00:00] Two rules were added to a customer
[00:02] service AI's prompt a few months apart.
[00:04] Always issue a refund if it meets the
[00:05] policy.
[00:06] And never issue a refund without an
[00:08] escalation.
[00:10] When the model was updated to the latest
[00:11] version, this AI got stuck on four
[00:13] refund requests and kept asking the
[00:14] customer for verification.
[00:16] This is an experiment conducted by
[00:17] Anthropic. It's written exactly like
[00:18] that on their blog.
[00:21] There are other instructions as well.
[00:22] A single line telling it to verify twice
[00:24] before answering increased the cost per
[00:25] ticket by 48%, while accuracy remained
[00:27] the same.
[00:28] A pair of contradictory rules lowered
[00:29] accuracy by nearly 9 points.
[00:31] Instructions that worked for older
[00:33] models now waste money and even degrade
[00:34] performance.
[00:36] Today, we’ll look at five ways to pay
[00:37] off this debt, following the
[00:38] presentation by Anthropic’s Lance Martin
[00:40] .
[00:41] People usually think that cost and
[00:42] quality are a trade-off. That you have
[00:44] to spend more to do better, and
[00:45] sacrifice performance to save money.
[00:59] Lance Martin says that, like code,
[01:00] technical debt also accumulates in
[01:01] prompts.
[01:02] Models from a few generations ago needed
[01:04] phrases like "think step-by-step,""
[01:05] check twice," or "be as meticulous as
[01:07] possible."
[01:08] Today's models choose when to think and
[01:10] verify on their own. However, if those
[01:12] instructions remain, the model follows
[01:13] them literally and uses more tokens.
[01:24] In the blog's words, the latest models
[01:26] take these instructions too literally
[01:28] and waste tokens.
[01:30] It reportedly checked the same order
[01:31] twice for every refund.
[01:33] There were even worse cases.
[01:35] Prompts with old thinking setups caused
[01:37] the API to reject all requests, and
[01:38] custom scratchpads clashed with the
[01:40] model's built-in reasoning, causing it
[01:41] to only "think" about tool calls without
[01:43] executing them in three cases.
[01:46] The solution is a single command.
[01:48] In Claude Code, using "/
[01:49] claude-api-prompt-audit" or "check-up
[01:52] prompt-audit" scans your skill,
[01:54] Claude.md, and tool descriptions to
[01:56] remove these patterns.
[01:58] Moving from Opus 4.8 to 5.5 reduced
[02:00] costs by about 18%, and running the
[02:02] auditor reduced them by another 9%.
[02:05] Accuracy also increased by about 2
[02:06] percentage points.
[02:07] The post where Lance Martin shared this
[02:09] tip has been viewed over 290,000 times.
[02:11] It removes patterns that hold back the
[02:12] latest models.
[02:14] One developer said they found about 70
[02:15] things to fix in their Claude Code
[02:17] configuration.
[02:20] The second is prompt caching. Agents
[02:22] resend the beginning part almost exactly
[02:23] as it is every turn. If you read the
[02:25] repeating part from the cache, Lance
[02:27] Martin says you only pay about one-tenth
[02:28] of the base input cost.
[02:30] The problem is that the beginning must
[02:31] be identical down to the very last byte
[02:33] for the cache to hit.
[02:34] Even adding just the current time to the
[02:36] system prompt forces it to recalculate
[02:37] from scratch every time.
[02:39] It’s explicitly mentioned on the blog as
[02:40] well. Time stamps or IDs in the system
[02:42] prompt break the cache.
[02:44] That’s why order is important.
[02:46] Put shared system instructions and tools
[02:48] first, followed by project-specific
[02:49] Claude MD, session state, and the
[02:51] growing message history at the very end
[02:52] .
[02:54] When Anthropic ran their
[02:55] cost-optimization prompts against
[02:57] benchmarks, they were able to cache 93%
[03:00] of the Tao-bench prompt. The cost
[03:02] decreased by 73%without any change in
[03:03] the pass rate.
[03:04] The document Q&A benchmark, Office-QA,
[03:06] also saw costs reduced by nearly 72%.
[03:14] From the third point on, we are talking
[03:15] about more fundamental concepts.
[03:16] Claude is good at self-correction, so if
[03:18] you provide a well-designed evaluation,
[03:19] its score will naturally improve. We
[03:21] call this "hill climbing."
[03:23] A good evaluation must satisfy four
[03:24] conditions. Better models should get
[03:26] higher scores, more "thinking" should
[03:27] improve scores, even the best models
[03:29] should not reach a perfect score, and
[03:31] scores should not fluctuate
[03:32] significantly between runs.
[03:34] The pitfall lies in ambiguous problems.
[03:36] If 20%of the questions are impossible
[03:37] for any model to solve, you might think
[03:38] there is room for improvement, but you
[03:40] are actually blocked.
[03:41] The blog suggests being suspicious of
[03:42] questions that fail every single time,
[03:43] no matter how many runs you perform.
[03:45] There are also commands for creating
[03:46] evaluations. If you provide raw data
[03:48] like builds, evals, and traces, it
[03:50] creates problems and grading criteria,
[03:51] getting human verification along the way
[03:53] .
[03:54] The biggest enemy of hill climbing is
[03:56] overfitting. If an evaluation requires
[03:58] OCR and you add an OCR tool to the
[04:00] harness, the score goes up, but it is
[04:01] useless in actual service.
[04:03] That is why the "hill climb" command
[04:05] splits evaluations into training and
[04:06] testing sets. Claude only looks at
[04:08] training failures to find areas for
[04:09] improvement and never sees the test set
[04:10] .
[04:11] If the training score rises while the
[04:12] test score stays the same, it suspects
[04:14] overfitting and reverts those changes.
[04:16] Lance Martin applied this to Claude API
[04:17] skills themselves. The initial score was
[04:20] 66%. By adding eight missing features,
[04:22] discovering that Claude was writing code
[04:24] using old API patterns, and even fixing
[04:26] the incorrect grader, it reached 87.9%
[04:28] in just 24 rounds.
[04:30] Hill climbing can also target cost. The
[04:32] goal is to reduce costs while
[04:33] maintaining performance.
[04:34] It started with Opus 4.8 at high effort
[04:37] , achieving 74.4%accuracy at 4.6 cents
[04:39] per ticket.
[04:40] After auditing the prompt and switching
[04:42] to Opus 5.0 at low effort, it hit 87.8%
[04:44] at 1.9 cents.
[04:46] One step down, Sonnet 5 at low effort
[04:48] was 1 cent, and after reviewing failure
[04:50] cases and setting rules, it rose to 98.9
[04:52] %.
[04:53] What matters are the 14 test tickets
[04:54] that were never seen before.
[04:56] Accuracy went from 78.6%to 90.5%, and
[04:58] the cost was reduced to about one-fifth
[05:00] .
[05:01] One principle emerged from this. It is
[05:03] cheaper and more effective to have a
[05:04] smarter model exert less effort than to
[05:06] make a less smart model think for a long
[05:07] time.
[05:14] The blog example shows that on the
[05:15] Cursor bench, Haiku 3.5 "low effort"
[05:17] matched Haiku 3 "high effort"
[05:18] performance at one-third the cost.
[05:21] So, Lance Martin’s advice is simple.
[05:23] Don't start with the max; start with
[05:25] Opus 3.5 "low."
[05:27] Finally, a look at what’s ahead. Claude
[05:29] 3 Opus could originally handle tasks
[05:31] taking about four minutes for a human,
[05:33] but the new graph shows up to 12 hours,
[05:35] and Lance Martin says we’re now entering
[05:37] the territory of one-to-two-day tasks.
[05:40] If an agent runs for days, it must be
[05:41] able to continue even if the sandbox
[05:42] crashes overnight.
[05:44] That’s why Claude Managed Agents have
[05:45] separated the "brain"—the harness—from
[05:47] the "hands"—the sandbox.
[05:48] The session log, which tracks the work,
[05:50] remains a separate record that can be
[05:51] reattached to either.
[05:52] No matter what crashes, it comes back to
[05:54] life from the logs.
[05:55] Security is covered, too. Claude cannot
[05:56] see the API keys directly and only
[05:58] references them in the vault.
[06:00] Giving a password to an agent working
[06:02] alone for days is a bit scary, right?
[06:05] To summarize: delete old prompts, keep
[06:07] things cached, build evaluators you can
[06:09] climb, watch out for overfitting, and
[06:11] use smarter models less.
[06:23] Going back to the customer service AI
[06:25] from the beginning, the problem wasn't
[06:26] the model.
[06:27] It was two lines of rules added over the
[06:29] course of several months.
[06:30] Your Claude MD might have those two
[06:32] lines as well.
[06:33] Run an audit on it today.
