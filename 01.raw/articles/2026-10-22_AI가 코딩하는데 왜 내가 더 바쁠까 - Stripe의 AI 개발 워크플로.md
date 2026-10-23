---
title: "AI가 코딩하는데 왜 내가 더 바쁠까? | Stripe의 AI 개발 워크플로"
type: video
source: https://www.youtube.com/watch?v=m3g2EkMjpno
site: youtube.com
author:
  - "[[Tech Bridge]]"
duration: 10:00
published: 2026-10-22
created: 2026-10-23
description: "Tech Bridge 자체 해설 10:00, 공식 챕터 없음. Stripe CEO Patrick Collison과 Claude Code의 Boris Cherny 대담(설명란 기준, 원본 S_lzYIvtEaQ · claude.com/office-hours)을 바탕으로 한 한국어 내레이션에 영어 원음 발췌 두 구간이 끼어 있다. 작업별로 분리된 devbox · 가드레일(invariants와 hard barriers)과 자동 검증(Minions의 blueprint) · 코드베이스가 주는 맥락 · 계획 후 병렬 분담, 그리고 소규모 팀의 적용 순서."
tags:
  - clippings/youtube
---

**Source URL**: https://www.youtube.com/watch?v=m3g2EkMjpno
**Channel**: Tech Bridge · **Duration**: 10:00 · **Published**: 2026-10-22

> **게시일.** info.json 기준 `upload_date` **`20261022`**, `timestamp` 1792659628(= 2026-10-22 18:00 KST), `availability: public`. 2026-10-23 회차에 받았다. 멤버 전용을 거치지 않은 신규 업로드다.
>
> **오디오 트랙과 자막 — 인용 규칙.** 오디오 포맷은 **한국어 트랙 하나뿐**(`language: ko`, 포맷 노트 low/medium · DRC)이다 — 10-21·10-22 편의 `Korean original + English (US)` 2트랙 구성과 다르다. 수동 자막 없음, 공식 챕터 없음. `automatic_captions`에 **`ko-orig`는 있고 `en-orig`는 없다.** 받은 **ko는 `lang=ko`(tlang 없음) = 원 오디오 ASR**이다 — 내레이션은 자연스러운 한국어 ASR이고, 영어 원음 발췌는 **ko 트랙 안에 영어 ASR 조각**으로 들어 있다. **en = `lang=ko&tlang=en` 기계 번역**(ko의 번역, 발췌 구간은 ko의 영어 조각을 그대로 복사). → **내레이션은 ko로 인용**하고 "(해설)"로 표시한다. **발췌는 ko 트랙의 영어 ASR 조각으로만 인용**한다 — 대조할 독립 트랙이 없다.
>
> **원음 발췌 구간**(내레이션 전환으로 판정): ① **02:58~03:18** — 질문 끝부분 *"without trading off against[?]iability and quality like what are the specifics that you have"* 과 답 *"it does mostly come back to this idea of um relying on invariance[=invariants?] and uh hard barriers rather than um things that are somewhat more subjective or discretionary or um or probabilistic."* 내레이션은 직전(02:39~02:47)에 *"대담에서 콜리스[=Collison]는 … 시스템이 지켜야 할 조건과 단단한 제한을 강조합니다. 그 대목을 짧게 보겠습니다"* 라고 답을 **Collison에게 돌린다.** 질문 쪽 화자는 내레이션이 밝히지 않는다. ② **06:27~06:36** — *"10 different dev boxes um with different agents executing parts of the plan and they might work all day in the exeme[?]"*. **화자를 내레이션이 밝히지 않는다.** 직후 해설 *"숫자를 생산성이 열배라는 뜻으로 읽을 수는 없습니다"*(06:42).
>
> **무캡션 구간**(5초 이상): 02:49→02:58(9초, 발췌 ① 앞부분 추정) · 03:18→03:31(13초) · **05:01→05:08**(7초 — 05:08 ko에 `>>` 화자 전환 표지, 이어지는 해설 *"이 관점을 적용하면 저장소 정리도…"* 가 가리키는 **"관점"의 원음이 이 공백 안에 있을 가능성이 크지만 자막이 없다**) · **06:09→06:27**(18초, 발췌 ② 앞부분 추정) · 06:36→06:42. **무캡션 구간의 내용은 인용하지 않는다.**
>
> ⚠️ **ASR 판독.** ① *"againstiability"* — *against reliability* 로 읽히지만 확정하지 않는다. *"invariance"* — 내레이션 *"시스템이 지켜야 할 조건"* 과 맥락상 *invariants* 로 읽는다(판독). ② *"in the exeme"* — 판독 불가, 인용 시 `[?]`. ko 내레이션 오인식: 보리스천이 → Boris Cherny(설명란) · 대부박스 → devbox · 콜리스 → Collison · 미니언스/미니언즈 → Minions · 구스 → goose · 블록 → Block · "함께 됩니다"(03:59) → 둡니다 · "접고"(04:41) → 적고 · "프롱프트의 테스트를"(04:16) → 프롬프트로 테스트를 · "저 장소"(06:03) → 저장소 · "분명해야를 비교할 수"(07:23) → 문장 일부 탈락 · "줄이런"(07:39) → 줄이려는 · "제연 방법"(08:19) → 재현 방법 · "영향과 좁은 테스트"(08:21) → 영향이 좁은 · "권난"(08:32) → 권한 · "변경 이후"(08:34) → 변경 이력(추정) · "배보"(08:48) → 배포 · "처음 골은"(09:04) → 처음 고른 · "맞고"(09:21) → 맡고 · "작업길이"(09:33) → 작업끼리. **"새 에이전트에게 동시에"(06:54)** 는 *세* 에이전트(API·화면·테스트 셋)인지 *새* 에이전트인지 ASR만으로 갈리지 않는다 — 판정하지 않는다.
>
> **인물·출처.** 설명란: *"Stripe CEO Patrick Collison과 Claude Code의 Boris Cherny 대담"*. 내레이션 00:40: *"스트라이프 최고 경영자 패트릭 콜리슨과 클로드 코드를 만든 보리스천이의 대담"*. 원본 대담 링크 <https://www.youtube.com/watch?v=S_lzYIvtEaQ> · <https://claude.com/office-hours> — **열어 보지 않았다.** 보강 자료로 Stripe 개발자 블로그 *Minions* Part 1·2와 git-worktree 공식 문서 링크가 있다 — **열어 보지 않았다.** devbox · Minions · blueprint · goose 관련 서술은 모두 내레이션이 *"스트라이프 공식 기술"*(= 공식 기술 블로그로 판독)을 인용한 것이다. 내레이터는 이름이 없다.
>
> **해설과 원본의 구분(설명란 자체 고지).** *"영상 속 소규모 팀의 검색 기능·작업 분담 예시는 테크브릿지의 해설입니다. Stripe가 직접 제시한 사례와 구분해 설명합니다. Minions는 goose를 기반으로 만든 Stripe 자체 코딩 에이전트이며 Claude Code와 동일한 제품이 아닙니다. devbox 열 개를 생산성 열 배라는 뜻으로 해석하지 않습니다."* 내레이션도 00:32~00:38에서 로그인 예시가 *"스트라이프에서 실제로 벌어진 일을 옮긴 예시는 아닙니다"* 라고 밝힌다.

## 설명란

AI가 코드를 작성해도 검토와 통합까지 저절로 끝나는 것은 아닙니다. Stripe CEO Patrick Collison과 Claude Code의 Boris Cherny 대담을 바탕으로, 개발자가 AI의 작업 환경을 어떻게 설계할지 살펴봅니다.

작업마다 분리된 devbox, 가드레일과 자동 검증, 코드베이스가 다음 작업에 주는 맥락, 계획을 세운 뒤 병렬로 일을 나누는 방식을 다룹니다. 원본의 필요한 발언에는 한국어 번역 자막을 붙이고, 소규모 개발팀에 적용할 예시와 분석을 더했습니다.

영상 속 소규모 팀의 검색 기능·작업 분담 예시는 테크브릿지의 해설입니다. Stripe가 직접 제시한 사례와 구분해 설명합니다. Minions는 goose를 기반으로 만든 Stripe 자체 코딩 에이전트이며 Claude Code와 동일한 제품이 아닙니다. devbox 열 개를 생산성 열 배라는 뜻으로 해석하지 않습니다.

원본 대담 및 공식 소개
https://www.youtube.com/watch?v=S_lzYIvtEaQ
https://claude.com/office-hours

보강 자료
Stripe 개발자 블로그 — Minions, Part 1
https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents
Stripe 개발자 블로그 — Minions, Part 2
https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents-part-2
Git worktree 공식 문서
https://git-scm.com/docs/git-worktree

한국어 해설·번역·편집: 테크브릿지
원본 발언과 테크브릿지의 해설·적용 예시는 구분되어 있습니다.

#AI코딩 #ClaudeCode #개발자 #Stripe #테크브릿지

## 트랜스크립트 — ko (원 오디오 ASR, `lang=ko`)

> 타임스탬프는 json3 이벤트 시작 시각(초 단위 내림). 연속 중복 줄만 제거했고 오인식은 고치지 않았다 — 판독은 위 헤더.

[00:00] AI가 코드를 다 짰다는데 왜 나는  
[00:02] 더 바빠졌을까요?이 이 영상에서는  
[00:05] 스트라이프의 사례를 통해 작업 환경을  
[00:07] 분리하고 검증을 자동화하고 병렬  
[00:10] 작업을 설계하는 세 가지 방법을  
[00:12] 살펴봅니다. 보고 나면 내  
[00:14] 프로젝트에서 무엇부터 바꿀지 정할 수  
[00:16] 있을 겁니다. 예를 들어 보겠습니다.  
[00:19] AI에게 로그인 기능을 고쳐 달라고  
[00:21] 했더니 코드와 테스트까지 돌아옵니다.  
[00:24] 그런데 우리 서비스의 권한 규칙과  
[00:26] 맞는지 다른 화면을 깨뜨리지는 않는지  
[00:29] 확인하다 보면 어느새 저녁입니다.  
[00:32] 이런 검토와 통합의 부담은 AI를  
[00:34] 쓰는 개발자가 겪을 수 있는  
[00:36] 상황입니다. 스트라이프에서 실제로  
[00:38] 벌어진 일을 옮긴 예시는 아닙니다.  
[00:40] 오늘 살펴볼 자료는 스트라이프 최고  
[00:43] 경영자 패트릭 콜리슨과 클로드 코드를  
[00:46] 만든 보리스천이의 대담입니다.  
[00:48] 스트라이프는 결제 인프라를 만드는  
[00:50] 회사입니다. 개발 속도를 높이면서  
[00:52] 서비스의 신뢰성도 지켜야 합니다.  
[00:54] 대담의 내용을 스트라이프 공식 기술과  
[00:57] 함께 살펴보겠습니다.  
[00:59] AI가 코드를 작성한 시점과 우리가  
[01:01] 그 코드를 배포할 수 있는 시점  
[01:03] 사이에는 간격이 있습니다. 요구  
[01:05] 사항이 맞는지 테스트가 충분한지 다른  
[01:08] 변경과 합쳤을 때도 동작하는지  
[01:10] 확인해야 합니다.이 간격을 그대로 둔  
[01:13] 채 코드만 더 빨리 만들면 검토를  
[01:15] 기다리는 변경이 쌓일 수 있습니다.  
[01:18] 먼저 AI가 작업할 공간부터  
[01:20] 보겠습니다. 스트라이프의 공식 기술에  
[01:23] 등장하는 대부박스는 코드와 개발 중인  
[01:25] 서비스를 담은 클라우드 개발  
[01:27] 환경입니다. 미니언즈라는 자체  
[01:29] 에이전트도이 환경에서 일합니다.  
[01:31] 사람이 쓰던 개발 기반을 에이전트에도  
[01:33] 활용한 겁니다. 여기서 두 이름을  
[01:36] 구분하겠습니다. 클로드 코드와  
[01:38] 미니언즈는 같은 시스템이 아닙니다.  
[01:40] 미니언즈는 블록의 구스를 바탕으로  
[01:43] 스트라이프가 만든 자체  
[01:44] 에이전트입니다. 지금부터 설명할  
[01:46] 미니언즈의 처리 순서를 클로드 코드의  
[01:48] 내부 구조로 받아들이시면 안 됩니다.  
[01:51] 작업 환경을 나누면 무엇이  
[01:52] 달라질까요? 설명을 위해 한  
[01:55] 에이전트는 검색 API를 고치고 다른  
[01:57] 에이전트는 관리 화면을 만든다고 해  
[01:59] 보겠습니다. 같은 작업 폴더에서  
[02:01] 동시에 파일을 바꾸면 누가 만든  
[02:03] 변경인지부터 확인해야 할 수  
[02:05] 있습니다. 각자 독립된 환경에서  
[02:07] 일하면 변경과 실행 기록을 작업별로  
[02:10] 살펴보기 쉬워집니다. 작은 팀이라면  
[02:12] 우선 작업별 브랜치와 워크 트리로  
[02:15] 파일을 분리해 볼 수 있습니다. 다만  
[02:17] 워크트리는 파일 작업 공간을 나누는  
[02:19] 도구입니다. 접근 권한이나  
[02:21] 데이터베이스까지 자동으로 격리해  
[02:23] 주지는 않습니다. 테스트 데이터,  
[02:25] 환경 변수, 실행 포트, 외부 서비스  
[02:28] 권한은 따로 정해야 합니다. 실패한  
[02:30] 작업을 버리고 같은 조건에서 다시  
[02:32] 시작할 수 있는지도 확인해 보시면  
[02:34] 좋겠습니다. 환경을 나눴다면 그  
[02:37] 안에서 어디까지 할 수 있는지 정할  
[02:39] 차례입니다. 대담에서 콜리스는 모델이  
[02:42] 올바르게 행동할 가능성에만 기대기보다  
[02:44] 시스템이 지켜야 할 조건과 단단한  
[02:47] 제한을 강조합니다. 그 대목을 짧게  
[02:49] 보겠습니다.  
[02:58] without trading off  
[02:59] againstiability and  
[02:59] quality like what  
[03:00] are the specifics  
[03:01] that you have it  
[03:02] does mostly come  
[03:03] back to this idea of  
[03:05] um relying on  
[03:07] invariance and uh  
[03:10] hard barriers rather  
[03:12] than um things that  
[03:14] are somewhat more  
[03:15] subjective or  
[03:16] discretionary or um  
[03:18] or probabilistic.  
[03:31] 이 말을 우리 팀의 작업으로  
[03:32] 옮겨보겠습니다. 운영 데이터를  
[03:34] 건드리지 말라고 적어두는 것과 개발  
[03:37] 환경에서 운영 데이터에 접근할 수  
[03:38] 없게 만드는 것은 다릅니다. 전자는  
[03:40] 요청이고 후자는 시스템의 제한입니다.  
[03:43] 어떤 파일을 수정할 수 있는지, 어떤  
[03:46] 자격 증명을 쓸 수 있는지, 어디에  
[03:48] 배포할 수 있는지 경계를 먼저 정하는  
[03:50] 겁니다. 코드 검증도 같은 방식으로  
[03:53] 생각할 수 있습니다. 스트라이프는  
[03:55] 미니언스의 흐름에 모델이 판단하는  
[03:57] 단계와 정해진 코드가 실행하는 단계를  
[03:59] 함께 됩니다. 구현에는 에이전트를  
[04:02] 쓰고 정해둔 검사에는 일반 코드를  
[04:04] 쓰는 방식입니다. 공식 기술  
[04:06] 글에서는이를 블루프린트라고 부릅니다.  
[04:09] 예를 들어 우리 팀에서는 변경이  
[04:11] 생기면 포맷 검사, 타입 검사, 관련  
[04:14] 테스트를 순서대로 돌리도록 만들 수  
[04:16] 있습니다. 매번 프롱프트의 테스트를  
[04:18] 부탁하는 데서 끝내지 않고 검사  
[04:21] 결과가 없으면 다음 단계로 넘어가지  
[04:23] 않게 하는 겁니다. 검사에 실패했다면  
[04:25] 어떤 명령이 실패했고 어떤 오류가  
[04:28] 나왔는지 에이전트가 확인할 수 있어야  
[04:30] 합니다. 물론 테스트가 통과했다고  
[04:32] 요구 사항까지 맞다는 뜻은 아닙니다.  
[04:35] 로그인 버튼이 잘 눌리는 것과 다른  
[04:37] 사람의 계정으로 들어갈 수 없는 것은  
[04:39] 서로 다른 확인 항목입니다. 팀이  
[04:41] 지켜야 할 동작을 구체적으로 접고  
[04:44] 사람이 검토할 항목도 남겨야 합니다.  
[04:46] 모델에게 결과를 물어보는 것에 더해  
[04:48] 우리가 확인할 수 있는 증거를 함께  
[04:50] 받는 방식입니다. 그런데 환경과  
[04:53] 검사만 갖췄는데도 AI가 계속 엉뚱한  
[04:56] 방식을 고집한다면 어떨까요? 이번에는  
[04:58] AI가 읽는 코드를 살펴볼 필요가  
[05:01] 있습니다.이  
[05:08] >> 관점을 적용하면 저장소 정리도 AI와  
[05:11] 함께 일하는 준비가 됩니다. 새  
[05:14] API를 만들어 달라고 할 때 같은  
[05:16] 일을 하는 코드가 세 가지 방식으로  
[05:18] 흩어져 있다면 어떤 방식을 따라야  
[05:20] 할까요? 오래된 예제를 먼저 읽었다면  
[05:23] 이미 버린 설계를 다시 가져올 수도  
[05:24] 있습니다. 팀에서 권장하는 구현  
[05:27] 예제와 테스트 실행 방법을 찾기 쉽게  
[05:29] 두면 이런 혼선을 줄이는데 도움이  
[05:31] 됩니다. 여기서 제가 권하는 방법은  
[05:34] 모든 규칙을 긴 문서 하나에 넣는  
[05:36] 것보다 작업하는 디렉토리에서 필요한  
[05:39] 안내를 발견하게 하는 겁니다. 예를  
[05:41] 들어 결제 코드에는 금액 처리 규칙을  
[05:44] 화면 코드에는 컴포넌트 사용 예제를  
[05:46] 연결하는 식입니다. 문서에는 하면 안  
[05:49] 되는 일만 적지 말고 무엇을 쓰면  
[05:51] 되는지도 보여 주면 좋겠습니다. 새  
[05:53] 인증 로직을 만들지 말라는 문장 옆에  
[05:56] 기존 인증 모듈의 위치를 적어 두는  
[05:58] 겁니다. AI가 같은 실수를  
[06:00] 반복한다면 프롬포트를 다시 쓰기 전에  
[06:03] 잘못된 예제나 오래된 설명이 저  
[06:05] 장소에 남아 있는지 확인해 보십시오.  
[06:07] 다음은 여러 일을 동시에 맡기는  
[06:09] 방법입니다.  
[06:27] 10 different dev  
[06:28] boxes um  
[06:30] with different  
[06:32] agents executing  
[06:33] parts of the plan  
[06:34] and they might work  
[06:36] all day in the exeme  
[06:42] 숫자를 생산성이 열배라는 뜻으로 읽을  
[06:45] 수는 없습니다. 먼저 볼 것은 어떤  
[06:47] 계획으로 일을 나눴느냐입니다.  
[06:50] 작은 팀의 예를 들어 보겠습니다. 새  
[06:52] 검색 기능의 API와 화면 테스트가  
[06:54] 필요합니다. 새 에이전트에게 동시에  
[06:57] 검색 기능을 만들려고 하면 응답  
[06:59] 형식부터 서로 다르게 정할 수  
[07:01] 있습니다. 그래서 시작 전에 입력과  
[07:03] 출력, 오류 형식, 각자 바꿀 파일을  
[07:06] 맞춰 줍니다. API가 아직 없어도  
[07:08] 화면 작업을 할 수 있도록 임시  
[07:10] 응답도 합의할 수 있습니다. 이렇게  
[07:13] 독립적으로 진행할 수 있는 일을 찾고  
[07:15] 다른 결과를 기다려야 하는 일은  
[07:17] 순서를 정합니다. 계획에는 완료  
[07:19] 조건도 들어갑니다. 코드 작성  
[07:21] 완료인지, 테스트 통과인지, 리뷰  
[07:23] 요청까지인지가 분명해야를 비교할 수  
[07:25] 있습니다. 계획을 자세히 쓴다고 처음  
[07:28] 예상이 모두 맞는 것은 아닙니다.  
[07:30] 작업 중 전제가 달라졌다면 멈춰서  
[07:33] 다시 나눌 기준도 필요합니다.  
[07:34] 에이전트가 서로 다른 방식으로 같은  
[07:37] 문제를 해결한 뒤 사람이 마지막에  
[07:39] 전부 고쳐 붙이는 상황을 줄이런  
[07:41] 겁니다. 그렇다면 내 프로젝트에서는  
[07:43] 무엇부터 바꾸면 좋을까요? 방금 본  
[07:46] 세 가지를 기준으로 지금 가장 자주  
[07:49] 막히는 곳을 찾아보시면 됩니다. 여러  
[07:52] 작업의 파일이나 실행 환경이  
[07:53] 뒤섞인다면 작업 공간 분리부터  
[07:56] 시작합니다. 같은 검사와 오류 확인을  
[07:59] 사람이 매번 반복한다면 검증  
[08:01] 자동화부터 손봅니다. 각자 만든  
[08:04] 코드는 잘 돌아가는데 합칠 때 문제가  
[08:06] 생긴다면 병렬 작업의 계획부터  
[08:09] 점검합니다. 입력과 출력, 수정  
[08:12] 범위, 완료 조건이 서로 맞는지  
[08:14] 확인하는 겁니다. 우선 순위를  
[08:16] 골랐다면 작고 범위가 분명한 작업  
[08:19] 하나로 시험해 보시길 권합니다. 제연  
[08:21] 방법이 있는 버그 수정이나 영향과  
[08:24] 좁은 테스트 보강이 좋겠습니다. 고칠  
[08:27] 문제와 바꿔도 되는 범위, 완료를  
[08:29] 확인할 명령을 함께 적습니다. 별도  
[08:32] 작업 공간에서 필요한 권난만 주고  
[08:34] 결과에는 변경 이후와 실행한 명령,  
[08:37] 남은 문제를 붙이도록 합니다. 사람은  
[08:40] 그 자료를 보고 요구 사항과 위험을  
[08:42] 판단합니다. 테스트가 이미 있는  
[08:45] 동작만 확인하고 있지는 않은지 실패한  
[08:48] 경우도 다루는지 살펴봅니다. 배보  
[08:50] 판단과 문제가 생겼을 때 되돌릴  
[08:52] 책임자도 정해둡니다.이 실험에서는  
[08:55] 코드가 처음 나온 시간과 사람이  
[08:57] 검토해서 받아들인 시간을 함께 기록해  
[09:00] 보십시오. 프롬프트 수정, 테스트,  
[09:02] 실패 해결, 병합 충돌 정리에 쓴  
[09:04] 시간을 보면 처음 골은 우선 순위가  
[09:06] 맞았는지 판단할 수 있습니다. 잘된  
[09:09] 작업 하나를 기준으로 범위를 넓히면  
[09:12] 에이전트를 늘리기 전에 우리 팀의  
[09:14] 준비 상태를 확인할 수 있습니다.  
[09:16] AI가 코드를 다 짰는데 왜 나는 더  
[09:18] 바빠졌을까요? 코드 작성 뒤에 남아  
[09:21] 있던 검토와 통합을 우리가 계속 맞고  
[09:24] 있기 때문일 수 있습니다. 오늘은  
[09:26] 스트라이프의 사례를 통해 작업 환경  
[09:28] 분리, 검증 자동화 병렬 작업 설계를  
[09:31] 살펴봤습니다. 이제 다음 작업을  
[09:33] 떠올려 보십시오. 작업길이  
[09:35] 간섭하는지, 같은 검사를 반복하는지,  
[09:38] 결과를 합칠 때 막히는지에 따라 먼저  
[09:40] 바꿀 것을 고를 수 있습니다. 한  
[09:43] 번에 모두 바꾸려 하지 않아도  
[09:44] 됩니다. 가장 자주 막히는 한 곳을  
[09:46] 골라 작은 작업으로 시험하고 검토까지  
[09:49] 걸린 시간이 줄었는지 확인해  
[09:51] 보십시오. 이번 영상은  
[09:52] 여기까지입니다. 도움이 되셨다면  
[09:54] 구독과 좋아요 부탁드립니다.  

## 트랜스크립트 — en (`lang=ko&tlang=en` 기계 번역 · 참고용, 인용하지 않음)

[00:00] Why have I become busier when AI wrote all the code  
[00:02] ? In this video,  
[00:12] we explore three ways to separate work environments, automate verification, and design parallel tasks using the example of Stripe.  After reading it, you will be able to  
[00:14] decide what to change first in your project  
[00:16] .  Let me give you an example.   I  
[00:21] asked the AI ​​to fix the login function, and it returned the code and tests.  
[00:24] However, while checking whether it complies with our service's permission rules and  
[00:26] doesn't break other screens, it is already  
[00:29] evening.   The  
[00:32] burden of such review and integration is a situation that  
[00:34] developers using AI may face  
[00:36] .  This  
[00:38] is not an example of what actually happened at Stripe.  
[00:40] The material we will be looking at today is a conversation between Stripe  
[00:43] CEO Patrick Collison and  
[00:46] Boris Chen, the creator of Claude Code.  
[00:48] Stripe is a company that builds payment infrastructure  
[00:50] .  We must accelerate development while  
[00:52] maintaining the reliability of the service.   Let's  
[00:57] take a look at the content of the discussion along with the official Stripe technology.  
[01:03] There is a gap between the time AI writes the code and the time we can deploy that code.  You must verify that the  
[01:05] requirements are met, that testing is sufficient, and that it  
[01:08] works even when combined with other changes  
[01:10] . If you  
[01:13] simply write code faster while leaving this gap as is,  
[01:15] changes waiting for review may pile up.  
[01:18] First, let's look at the space where the AI ​​will work  
[01:20] .  The Loan Box featured in Stripe's official technology  
[01:27] is a cloud development environment containing code and services under development.  Agents called Minions also  
[01:29] work in this environment.   We  
[01:33] utilized the development infrastructure that humans used for agents as well.  I will distinguish the two names here  
[01:36] .  Claude Code and  
[01:38] Minions are not the same system.  
[01:40] Minions are the original agents created by Stripe based on Block's Goose  
[01:44] .  You should not accept the  
[01:46] processing order of the Minions that I am about to explain  
[01:48] as the internal structure of Claude's code.  
[01:51] What changes if we divide the work environment  
[01:52] ?  For the sake of explanation, let's assume one  
[01:55] agent fixes the search API and another  
[01:57] agent creates the administration screen  
[01:59] .  If you replace files simultaneously in the same working folder, you may  
[02:03] need to check who made the change first  
[02:05] .  
[02:07] Working in independent environments makes it easier to review change and execution history by task  
[02:10] .  If you have a small team, you  
[02:15] can start by separating files into task-specific branches and work trees.  However,  
[02:17] WorkTree is a tool for dividing file workspaces  
[02:19] .  It does not automatically isolate access rights or the  
[02:21] database  
[02:23] .  Test data,  
[02:25] environment variables, execution ports, and external service  
[02:28] permissions must be set separately.  I would also like you to check if you can  
[02:30] discard the failed task and start over under the same conditions  
[02:34] .  If you have divided the environment, it is  
[02:39] time to decide how far you can go within it.  In the interview, Collis emphasizes the conditions and rigid limits that the system must adhere to,  
[02:42] rather than relying solely on the possibility that the model will behave correctly  
[02:47] .  Let's take a brief look at that part  
[02:49] .  
[02:58] without trading off  
[02:59] againstiability and  
[02:59] quality like what  
[03:00] are the specifics  
[03:01] that you have it  
[03:02] does mostly come  
[03:03] back to this idea of  
[03:05] um relying on  
[03:07] invariance and uh  
[03:10] hard barriers rather  
[03:12] than um things that  
[03:14] are somewhat more  
[03:15] subjective or  
[03:16] discretionary or um  
[03:18] or probabilistic.   Let's  
[03:32] apply this to our team's work.  There is a difference between writing down that operational data should not be  
[03:34] touched and making  
[03:37] operational data inaccessible in the development environment  
[03:38] .  The former is a  
[03:40] request, and the latter is a system limitation.   The  
[03:48] first step is to define the boundaries of which files can be modified, which credentials can be used, and where they can be distributed  
[03:50] .  You can think of code verification in the same way  
[03:53] .  Stripe  
[03:59] combines the model's decision-making phase and the predefined code execution phase in the flow of the Minions.  It is a method that uses an agent for implementation and  
[04:02] regular code for predefined checks  
[04:04] .  In official technical  
[04:06] articles, this is called a blueprint.  
[04:09] For example, our team can set it up to run  
[04:11] format checks, type checks, and related  
[04:14] tests in sequence whenever a change occurs  
[04:16] .  It does  
[04:18] not stop at simply requesting a test from Prongft every time, but prevents  
[04:21] moving on to the next step if there are no test results  
[04:23] .  If the inspection fails,  
[04:28] the agent must be able to identify which command failed and what error occurred  
[04:30] .  Of course, just because the test passed  
[04:32] does not mean that the requirements have been met.   Being able to  
[04:35] press the login button properly and being  
[04:37] unable to access another person's account are  
[04:39] different verification items.  You must  
[04:41] specifically define the actions the team must follow and  
[04:44] leave items for human review.   It is a  
[04:50] method where, in addition to asking the model for results, we also receive verifiable evidence.  However, what if  
[04:53] the AI ​​continues to insist on the wrong approach even though the environment and inspection are in place  
[04:56] ?  This time, we  
[04:58] need to examine the code that AI reads  
[05:01] .  
[05:08] Applying this perspective prepares repository cleanup to work with AI as well  
[05:11] .  
[05:14] When asked to create a new API, if  
[05:16] the code performing the same task is scattered across three different methods,  
[05:18] which method  
[05:20] should you follow?  If you read the old examples first, you might be able to  
[05:23] bring back designs that you have already discarded  
[05:24] .  Keeping the implementation  
[05:27] examples and test execution methods recommended by the team easy to find  
[05:29] helps reduce this confusion  
[05:31] .  My recommendation here is to let you  
[05:39] find the necessary guidance in your working directory rather than putting all the rules into one long document.  
[05:41] For example, it involves linking amount processing rules to the payment code and  
[05:44] component usage examples to the screen code  
[05:46] .  
[05:51] I would like the document to show what should be written, rather than just listing what should not be done.  It is to write down the location of the existing authentication module  
[05:53] next to the sentence stating not to create new authentication logic  
[05:58] .  If the AI  
[06:00] repeats the same mistake, check to see if any  
[06:03] incorrect examples or outdated explanations  
[06:05] remain in that place before rewriting the prompt.  
[06:07] The following is a method for assigning multiple tasks simultaneously  
[06:09] .  
[06:27] 10 different dev  
[06:28] boxes  
[06:30] with different  
[06:32] agents executing  
[06:33] parts of the plan  
[06:34] and they might work  
[06:36] all day in the exeme. You  
[06:45] cannot interpret the number as meaning that productivity is ten times higher.  The first thing to look at is how the  
[06:47] work was divided according to the plan.   Let me give you an  
[06:50] example of a small team.  
[06:52] API and screen testing for the new search function are  
[06:54] required.  If you intend to create a search function for new agents simultaneously, you  
[06:59] can set the response formats differently  
[07:01] .  So, before starting, match the input,  
[07:03] output, error format, and the file to be changed for each person  
[07:06] .  You can also agree on a  
[07:08] temporary response to enable screen operations even if the API is not yet available  
[07:10] .  We  
[07:17] prioritize tasks that can be handled independently and those that require waiting for other results.  The plan  
[07:19] also includes completion conditions.  It must be clear whether the code is  
[07:21] complete, tests have passed, or a review  
[07:23] request has been made in order to make a comparison  
[07:25] .  Writing a detailed plan  
[07:28] does not mean that all initial predictions are correct.  
[07:30] If the premise changes during the work, you  
[07:33] also need criteria to stop and divide again.   It is to  
[07:39] reduce the situation where agents solve the same problem in different ways, and then a human fixes everything at the end  
[07:41] .  In that case,  
[07:43] what should I change first in my project?  You just need to find the place that gets congested  
[07:46] most frequently based on the three things you just saw  
[07:49] .  If  
[07:52] files or execution environments for multiple tasks are  
[07:53] mixed up, start by separating the workspaces  
[07:56] .  If humans are repeating the same checks and error verification  
[07:59] every time, start by overhauling the verification  
[08:01] automation.  If  
[08:04] the code written individually runs well but problems  
[08:06] arise when merging, start by checking the parallel task plan  
[08:09] .  It is to check if the input, output, modification  
[08:12] range, and completion conditions match each other  
[08:14] .  
[08:16] If you have selected a priority, I  
[08:19] recommend testing it out with a small, clearly defined task.  It would be good to have  
[08:21] bug fixes with smoke control methods or reinforcement of impact and  
[08:24] narrow testing.  Write  
[08:29] down the problem to be fixed, the scope to be changed, and the command to verify completion.  
[08:32] In a separate workspace, provide only the necessary permissions, and  
[08:37] attach the results, the changes made, the executed commands, and the remaining issues.  People  
[08:40] look at the data and judge the requirements and risks  
[08:42] .  We examine whether the test is  
[08:45] only verifying existing behaviors or if it  
[08:48] handles cases of failure.  Designate a person responsible for distribution  
[08:50] judgments and reverting code if problems arise  
[08:52] . In this experiment, please  
[08:57] record the time the code was first released and the time it was reviewed and accepted by a human  
[09:00] .  You can determine if the initial goal was prioritized by looking at the time spent on fixing prompts, testing,  
[09:02] resolving failures, and cleaning up merge conflicts  
[09:06] .  By  
[09:09] expanding the scope based on a single successful task, we  
[09:14] can check our team's readiness before increasing the number of agents.  
[09:16] Why did I get busier when the AI ​​finished writing the code  
[09:18] ?  This may be because  
[09:21] we are continuing to handle the review and integration that remained after writing the code  
[09:24] .  Today,  
[09:26] through the example of Stripe, we looked at work environment  
[09:28] separation, verification automation, and parallel task design  
[09:31] .  Now, think about the next task  
[09:33] .  You can choose what to change first depending on whether the work length  
[09:35] interferes, whether the same check is repeated, or whether there is a  
[09:38] blockage when merging results  
[09:40] .  You do  
[09:43] n't have to try to change everything at once  
[09:44] .  Select the one that gets stuck most frequently,  
[09:46] test it with a small task, and  
[09:49] check if the time taken to review has decreased  
[09:51] .  That's all for this video  
[09:52] .  If this was helpful, please  
[09:54] subscribe and like.  
