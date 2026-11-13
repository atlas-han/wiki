---
title: "Fable·Opus·Sonnet·Haiku, 어떤 Claude 모델로 만들어야 할까? | 모델 선택 가이드 9분 총정리"
type: video
source: https://www.youtube.com/watch?v=M_yjL9qgwDo
site: youtube.com
author:
  - "[[Tech Bridge]]"
duration: 9:01
published: 2026-11-12
created: 2026-11-13
description: "Tech Bridge 한국어 해설 9:01, 공식 챕터 9, Korean original(AI 내레이션 · AI 배경 음악). Addy Osmani의 claude.dev 블로그 글 'Which Claude model should you build with? Fable, Opus, Sonnet, or Haiku'(2026-11-09)를 온라인 상점 백로그 네 장에 빗대어 정리 — 기본값 Opus 5.5 medium, 네 모델 가격(Haiku 5.5 $0.10/$0.50 · Sonnet 5.5 $2/$10 · Opus 5.5 $4/$20 · Fable 5.2 $8/$40, 컨텍스트 모두 100만), 작업별 배정, 모델보다 effort 먼저(SWE-bench Pro · Frontier Code 2.0 · Terminal-Bench 3.0 수치), low 후 실패만 high 재실행, 속도 · 컨텍스트 비용(캐시 읽기), 서브에이전트 · 워커 · 어드바이저, 모델 전환 전 호환성(400 오류 세 가지), 내 작업으로 측정하기. 무캡션 구간 없음."
tags:
  - clippings/youtube
---

**Source URL**: https://www.youtube.com/watch?v=M_yjL9qgwDo
**Channel**: Tech Bridge · **Duration**: 9:01 · **Published**: 2026-11-12

> **게시일.** info.json 기준 `upload_date` **`20261112`**(UTC), `timestamp` 1794474035(= 2026-11-12 09:00:35 UTC = **2026-11-12 18:00 KST**), `availability: public`. 2026-11-12 회차(09:10 KST 발화) 뒤에 올라와 2026-11-13 회차 목록에 처음 나왔다. 파일명에서 `|` · `?` · `,`는 뺐다.
>
> **오디오 트랙과 자막 — 인용 규칙.** 오디오는 `Korean original (default)` + 영어 더빙(`en` · `en-US`), 메타 `language`=`en`. 수동 자막 없음. `ko`와 `ko-orig`는 **md5가 같고** `kind=asr&lang=ko&variant=gemini`다(11-12 Karp 편에 이어 두 번째). `en-orig`(`lang=en&variant=timing-optimized`)는 **영어 더빙 트랙의 ASR**이다. → **인용은 전부 ko-orig**, en-orig는 판독 대조에만. 429 없음(`--sleep-subtitles 8`).
>
> **형식.** 설명란: *"이 영상의 내레이션은 AI 음성이고 배경 음악은 AI로 생성했습니다. 수치는 원문 기준이며, 측정 그래프의 점과 일부 비용 막대는 비율만 나타낸 예시입니다."* 원음 발췌가 없는 **순수 내레이션** 이고 `gaps.py`(4.5초 기준)로 무캡션 구간이 없다.
>
> ⚠️ **더빙이 모델 이름 · 버전을 바꾼다**(11-09 · 11-11과 같은 패턴): en-orig에 `Opus 3.5`(6회) · `Sonnet 3.5`(6회) · `Haiku 3.5`(6회) · `Fable 2024`가 나오고 `Opus 5.5` · `Sonnet 5.5` · `Fable 5.2`는 일부만 맞다. Addy Osmani도 `Eddie Osman`(00:14)으로 적는다. **모델 버전은 ko-orig · 설명란 · tags로만 읽는다.**
>
> **ASR 판독(ko-orig).** *네 장사여 있습니다*(00:00~00:02) → 네 장 쌓여 있습니다, *클라우드*(00:10 · 00:13 · 00:31 · 00:56 · 08:37) → Claude, *에디 오스만이 가*(00:13) → Addy Osmani가, *에포트*(00:27 등) → effort, *슬래시 에포트 스테이터스*(01:00~01:02) → `/effort` status(정확한 명령 형식 미확정), *티켓 네 장 받기 일도 같은 나눕니다*(01:57~01:59) → 티켓 밖의 일도 같은 식으로 나눕니다(추정), *대량 수출*(01:49) → 대량 추출(추정), *맞는 서브 에이전트*(01:53) → 맡는 서브에이전트, *페이들*(03:18) → Fable, *토크는*(03:42 · 03:45) → 토큰은, *95.3%의 29센트*(04:19) → 95.3%에 29센트, *20센트로 갔습니다*(05:10~05:11) → 20센트로 같습니다, *생각복록*(06:05 · 07:50) → 생각 블록(thinking block), *익스플로러 · 다룹니다*(06:39~06:42) → Explore 서브에이전트 · 따릅니다, *그런 신중합니다*(07:18) → 그건 신중히(추정), *1.7.5 오르는데*(07:23) → 1.7포인트 오르는데(추정, ⚠️ 미확정), *버짓 토큰*(07:46) → budget tokens, *덧붙이기 만하고*(08:10) → 덧붙이기만 하고, *슬래시 유시지*(08:44) → `/usage`.
>
> ⚠️ **사실 진술의 출처.** 가격 · 기본 effort · 벤치마크 수치 · 호환성 규칙은 모두 **해설자가 옮긴 Addy Osmani 글의 내용**이고 위키는 원 글 · 공식 문서를 열지 않았다(설명란 링크). 그래프의 점 · 일부 비용 막대는 *비율만 나타낸 예시* 라고 설명란이 밝힌다.

## 설명란

Fable 5.2, Opus 5.5, Sonnet 5.5, Haiku 5.5. 네 가지 Claude 모델 가운데 무엇으로 만들어야 할까요? Claude 개발자 블로그에 올라온 Addy Osmani의 모델 선택 가이드를 온라인 상점 프로젝트의 백로그 네 장에 빗대어 정리했습니다. 기본값은 왜 Opus 5.5 medium인지, 모델을 바꾸기 전에 effort부터 조정해야 하는 이유, 토큰 단가가 아니라 완료한 작업당 비용으로 봐야 하는 사례, 서브에이전트와 워커에 작은 모델을 쓰는 방법, 모델을 옮기기 전 호환성 확인까지 다룹니다.

타임라인
0:00 이 일, 어떤 모델에 맡길까
0:23 기본값: Opus 5.5 medium에서 시작
1:05 작업별 배정: 네 모델에 일 나누기
2:28 모델보다 effort 먼저
4:23 속도와 컨텍스트 비용
5:43 모델 섞어 쓰기: 서브에이전트와 워커
7:30 모델을 옮기기 전 확인할 것
8:20 내 작업으로 직접 측정하기
8:48 정리

참고
- Addy Osmani, "Which Claude model should you build with? Fable, Opus, Sonnet, or Haiku" (claude.dev, 2026-11-09): https://claude.dev/blog/which-claude-model-should-you-build-with/
- Choosing a model: https://platform.claude.com/docs/en/about-claude/models/choosing-a-model
- Effort: https://platform.claude.com/docs/en/build-with-claude/effort
- Claude Code 모델 설정: https://code.claude.com/docs/en/model-config

이 영상의 내레이션은 AI 음성이고 배경 음악은 AI로 생성했습니다. 수치는 원문 기준이며, 측정 그래프의 점과 일부 비용 막대는 비율만 나타낸 예시입니다. 배경 화면은 Claude·Anthropic 공식 영상을 흐리게 처리해 사용했습니다.

#Claude #Anthropic #ClaudeCode #AI #클로드

> info.json `tags`: AI 모델 · AI 에이전트 · Anthropic · Claude · Claude Code · Fable 5.2 · Haiku 5.5 · Opus 5.5 · Sonnet 5.5 · effort · 모델 선택 · 서브에이전트 · 앤트로픽 · 클로드

## 트랜스크립트 — ko-orig (원 오디오 ASR, `lang=ko&variant=gemini` — `ko`와 바이트 동일 · 인용 근거)

[00:00] 온라인 상점 프로젝트에 할 일이 네
[00:02] 장사여 있습니다. 코드 전체를
[00:04] 타입스크립트로 옮기는 일, 월 구독
[00:06] 기능, 상품 페이지, 그리고 고객
[00:08] 메시지 분류. 이 일들을 어떤
[00:10] 클라우드 모델에 맡겨야 할까요?
[00:13] 이 영상은 에디 오스만이 가 클라우드
[00:14] 개발자 블로그에 쓴 모델 선택
[00:16] 가이드를 정리한 것입니다.
[00:18] 페이블, 오퍼스, 소넷, 하이쿠. 네
[00:20] 모델을 언제 쓰는지 차례로
[00:21] 살펴보겠습니다.
[00:25] 먼저 결론부터 말하면 잘 모르겠을
[00:27] 때는 오퍼스 5.5를 에포트
[00:29] 미디엄으로 시작하면 됩니다.
[00:31] 클라우드 코드의 기본 모델이고 토큰
[00:32] 가격은 페이블 5.2의 절반입니다.
[00:36] 네 모델의 가격부터 보겠습니다.
[00:38] 입력과 출력 100만 토큰 기준으로
[00:39] 하이쿠 5.5는 10센트와 50센트,
[00:42] 소넷 5.5는 2달러와 10달러,
[00:44] 오퍼스 5.5는 4달러와 20달러,
[00:46] 페이블 5.2는 8달러와
[00:47] 40달러입니다. 컨텍스트는 네 모델
[00:49] 모두 100만 토큰입니다.
[00:52] API 기본 에포트도 모델마다
[00:54] 다릅니다. 하이쿠와 오퍼스는 미디엄,
[00:56] 소넷과 페이블은 하이입니다. 클라우드
[00:58] 코드에서는 소넷과 페이블도 미디엄으로
[01:00] 시작합니다. 지금 설정은 슬래시
[01:02] 에포트 스테이터스로 확인할 수
[01:03] 있습니다.
[01:07] 이제 티켓을 배정해 보겠습니다.
[01:09] 자바스크립트를 타입스크립트로 옮기는
[01:11] 대규모 전환은 페이블 5.2의
[01:13] 몫입니다.
[01:14] 큰 리팩토링과 마이그레이션, 아키텍처
[01:16] 설계, 사람이 지켜보지 않는 긴
[01:18] 실행에 맞는 모델입니다.
[01:21] 월 구독 기능은 오퍼스 5.5가
[01:23] 맞습니다. 여러 풀 리퀘스트에 걸친
[01:25] 기능 개발과 일상적인 디버깅에서
[01:27] 비용과 성능의 균형이 좋습니다.
[01:30] 스크린샷을 많이 다루는 컴퓨터 사용
[01:31] 작업도 오퍼스에서 시작합니다.
[01:35] 상품 페이지는 소넷 5.5입니다.
[01:36] 버그 수정이나 스펙이 분명한 기능처럼
[01:38] 범위가 정해진 일을 오퍼스 토큰
[01:40] 가격의 절반으로 처리합니다. [음악]
[01:42] 채팅, 문서와 슬라이드 작업에도 잘
[01:44] 맞습니다.
[01:46] 고객 메시지 분류는 하이쿠
[01:47] 5.5입니다. 분류, 라우팅, 대량
[01:49] 수출처럼 단순하고 양이 많은 일에서
[01:52] 가장 빠르고 저렴합니다.
[01:53] 큰 모델의 부수 작업을 맞는 서브
[01:55] 에이전트로도 좋습니다.
[01:57] 티켓 네 장 받기 일도 같은
[01:59] 나눕니다.
[02:00] 채팅과 대화형 세션은 소넷 5.5를
[02:02] 로우나 미디엄으로, 단순한 대량
[02:04] 채팅이면 하이쿠로 보냅니다.
[02:06] 조사와 리뷰, 초안 작성처럼 반복해서
[02:09] 실행하는 에이전트 작업도 소넷
[02:11] 미디엄이면 충분합니다.
[02:13] 심층 리서치와 과학 정량 분석은
[02:15] 페이블 5.2에서 시작합니다.
[02:17] 문서 작업은 소넷이 기본이지만 복잡한
[02:19] 재무 모델이나 방대한 원자료에서
[02:21] 만드는 문서는 오퍼스에서 시작합니다.
[02:23] 스펙이 분명해도 마이그레이션이나 성능
[02:25] 최적화는 오퍼스가 필요할 수
[02:26] 있습니다.
[02:30] 여기서 중요한 원칙이 하나 있습니다.
[02:31] 모델을 바꾸기 전에 에포트부터 조정을
[02:34] 하는 것입니다. 에포트는 비용과
[02:36] 성능을 더 세밀하게 조절하는
[02:37] 다이얼입니다. 다만 에포트를 올려도
[02:39] [음악] 모델에 없는 지식이나 능력이
[02:41] 생기지는 않습니다.
[02:43] 에포트를 올리면 모델이 [음악] 더
[02:45] 오래 생각하고, 도구를 더 많이
[02:46] 호출하고, 자기 결과를 더 많이
[02:48] 검증합니다. 그만큼 응답은
[02:50] 느려집니다.
[02:51] 에포트와 지연 시간은 대략 비례하기
[02:53] 때문에 늘어난 정확도가 기다릴 만한
[02:55] 값인지 따져봐야 합니다.
[02:57] 오퍼스 5.5의 SWE 벤치 프로
[02:59] 결과를 보겠습니다. 하이를 기준으로
[03:01] 미디엄은 [음악] 약 2.5 포인트
[03:03] 낮지만 비용은 약 70%입니다.
[03:05] 로우는 약 8 포인트 낮고 비용은
[03:07] 1/3 정도입니다. [음악]
[03:08] 엑스트라 하이는 1.4 포인트 높지만
[03:10] 비용이 2.5배입니다.
[03:13] 그래서 하이를 넘겨야 할 때는 한
[03:15] 단계 위 모델을 더 낮은 에포트로
[03:17] 시험해 봐야 합니다.
[03:18] 프론티어 코드 2.0에서 페이들
[03:21] 5.2 하이는 45.3%, 오퍼스
[03:24] 5.5 맥스는 45.5%였습니다.
[03:27] 점수는 거의 같은데 작업당 비용은
[03:29] 페이블 쪽이 절반 정도였습니다.
[03:32] 반대 방향의 사례도 있습니다.
[03:34] [음악] 터미널 벤치 3.0에서 이전
[03:36] 모델인 페이블 5.1은 맥스로
[03:38] 58.0%였는데
[03:39] 오퍼스 5.5는 하이로 58.9%를
[03:42] 기록하면서 토크는 절반만 썼습니다.
[03:45] 토크는 단가가 아니라 완료한 작업당
[03:46] 비용을 봐야 하는 이유입니다.
[03:49] 모델이 일을 해내지 못할 때는 세
[03:51] 단계를 순서대로 밟습니다. 첫째,
[03:53] [음악] 테스트나 빌드처럼 모델이
[03:55] 스스로 결과를 검증할 수단을 줍니다.
[03:58] 둘째, 에포트를 한 단계 올립니다.
[04:00] 셋째, 한 단계 [음악] 위 모델로
[04:02] 옮기되 더 낮은 에포트로 시작합니다.
[04:06] 결과를 자동으로 확인할 수 있다면 더
[04:07] 좋은 방법이 있습니다. 전부 로우로
[04:09] 돌리고 실패한 [음악] 작업만 하이로
[04:11] 다시 돌리는 것입니다.
[04:12] 오퍼스 5.5에서 이 방식은 약
[04:14] 97%를 통과했고 작업당 약
[04:17] 17센트가 들었습니다. 전부 하이로
[04:19] 돌리면 95.3%의 29센트였습니다.
[04:24] 사람이 응답을 기다리는 경우에는 소넷
[04:26] 5.5를 로우나 미디엄으로
[04:28] 시작합니다. 같은 모델에서 속도만 더
[04:30] 필요하면 빠른 모드가 있습니다.
[04:32] 오퍼스 5.5와 페이블 5.2가
[04:33] 지원하고 가격은 더 높습니다.
[04:37] 세대가 바뀌면 속도도 달라집니다.
[04:39] 페이블 5.2는 페이블 5.1보다
[04:41] 출력이 최대 30% 빠르고 소넷
[04:43] 5.5는 소넷 5보다 30%
[04:45] 빠릅니다.
[04:47] 컨텍스트도 비용입니다. 큰 컨텍스트는
[04:50] 매 턴마다 다시 전송되기 때문입니다.
[04:52] 한 턴의 캐시 읽기 비용은 컨텍스트가
[04:54] 15만 토큰이면 약 3센트, 2만
[04:56] 토큰이면 약 0.4센트입니다.
[04:58] 비싼 모델의 컨텍스트는 판단에 쓰고
[05:00] 긴 읽기는 저렴한 서브 에이전트에
[05:02] 맡기는 편이 좋습니다.
[05:05] 긴 실행에서는 입력 대부분이 캐시
[05:06] 읽기로 청구됩니다.
[05:08] 캐시 읽기 가격은 오퍼스 5.5와
[05:10] 페이블 5.2가 100만 토큰당
[05:11] 20센트로 갔습니다.
[05:13] 그래서 두 모델의 차이는 캐시되지
[05:14] 않은 입력과 출력에서 생기고 여기서
[05:17] 페이블은 토큰당 두 배입니다.
[05:19] 하이쿠 5.5는 프롬프트 길이에 따라
[05:21] 가격이 달라지는 유일한 모델입니다.
[05:23] 프롬프트가 10만 토큰을 넘으면
[05:25] 요금이 다섯 배가 됩니다. 그래도
[05:27] 소넷 5.5 토큰 가격의
[05:28] 1/4입니다.
[05:30] 비교할 때는 가장 어려운 작업의
[05:32] 비용도 계산해야 합니다.
[05:33] 어려운 작업이 지출의 대부분을
[05:35] 차지하기 때문입니다.
[05:36] 20문제짜리 검색 벤치마크에서는
[05:38] [음악] 단 두 문제가 전체 지출의
[05:40] 43%를 차지했습니다.
[05:45] 이제 여러 모델을 섞어 쓰는
[05:46] 방법입니다.
[05:47] 프롬프트 캐시는 그 캐시를 만든
[05:49] 모델에 묶여 있어서 모델을 바꾸면 첫
[05:52] 턴의 전체 대화를 다시 캐시에 써야
[05:54] 합니다.
[05:55] 그래서 전환은 작업의 경계에서 하고
[05:57] 클로드 코드에서는 먼저 슬래시
[05:59] 컴팩트를 실행합니다.
[06:02] 생각 블록도 따라오지 않을 수
[06:03] 있습니다. 상위 모델은 하위 모델의
[06:05] 생각복록을 읽을 수 있지만 아래로
[06:07] 내려가면 이전 추론은 버려집니다.
[06:09] 요청은 성공하지만 새 모델은 그 추론
[06:11] 없이 일하게 됩니다.
[06:12] API에서는 전체 기록 대신
[06:14] 지금까지의 요약으로 새 대화를
[06:16] 시작하는 편이 낫습니다.
[06:18] 서브 에이전트는 작은 모델에
[06:20] 맡깁니다. 파일 찾기, 테스트 실행,
[06:22] 로그 읽기처럼 틀리면 금방 드러나는
[06:24] 일이 대상입니다.
[06:25] 서브 에이전트 정의에 모델을 하이쿠나
[06:27] 소넷으로 지정하면 됩니다. 코드
[06:29] 수정과 판단은 메인 모델에
[06:30] 남겨둡니다.
[06:32] 주의할 점도 있습니다. 작은 모델이
[06:34] 검색 결과를 잘못 읽으면 메인 모델이
[06:36] 엉뚱한 파일을 열어 토큰을
[06:37] 낭비합니다.
[06:39] 그리고 클로드 코드의 내장 익스플로러
[06:40] 서브 에이전트는 기본적으로 세션
[06:42] 모델을 다룹니다. 비용을 낮추려면
[06:44] 모델을 하이쿠로 지정한 익스플로러를
[06:46] 직접 정의합니다.
[06:48] 한 컨텍스트에 담기지 않은 큰 작업은
[06:50] 상위 모델이 쪼개서 여러 워커에
[06:51] 나눠줍니다.
[06:52] 약 2,200만 토큰 규모의 결함
[06:54] 탐색에서 오퍼스 5.5가 지휘하고
[06:56] 소넷 5.5 워커가 일한 구성은
[06:58] 오퍼스 단독보다 약 1/3 저렴했고
[07:01] 성능은 거의 같았습니다.
[07:03] 다만 이 방식이 맞지 않는 경우도
[07:05] 있습니다. 앞 단계에 의존하는 한
[07:07] 줄짜리 작업이거나 한 컨텍스트에
[07:09] 들어가는 작업이면 계획하고 합치는
[07:11] 비용이 절감액보다 큽니다.
[07:14] 저렴한 모델이 일하다가 더 강한
[07:15] 모델의 조언을 구하는 어드바이저
[07:17] 도구도 있습니다. [음악]
[07:18] 다만 그런 신중합니다. 오퍼스
[07:21] 5.5에 페이블 5.1 어드바이저를
[07:23] 붙인 사례는 1.7.5 오르는데
[07:25] 비용이 약 2.1배 들었습니다. 먼저
[07:28] 측정해 보라는 뜻입니다.
[07:32] 모델을 옮기기 전에 호환성도 확인해야
[07:34] 합니다. [음악] 소넷 5.5,
[07:35] 오퍼스 5.5, 페이블 5.2에서는
[07:37] 도구 사용을 강제하는 설정이 400
[07:39] 오류를 냅니다.
[07:40] 오퍼스와 페이블은 항상 생각을 켠
[07:42] 채로 동작합니다. 하이쿠 4.5에서
[07:44] 5.5로 옮길 때는 버짓 토큰을
[07:46] 에포트 수준으로 바꿔야 합니다.
[07:49] 페이블 5.2에는 한 가지가 더
[07:50] 있습니다. 생각복록 앞에 내용, 즉
[07:53] 시스템 프롬프트나 도구, 이전
[07:55] 메시지를 바꾸면 400 오류가
[07:56] 납니다.
[07:57] 클로드 코드나 에이전트 SDK를
[07:59] 쓴다면 바꿀 것이 없지만 기록을 직접
[08:01] 편집한다면 덧붙이기만 하도록 유지해야
[08:03] 합니다.
[08:05] 여러 모델을 함께 쓴다면 가장 엄격한
[08:07] 모델을 맞춰 요청을 구성합니다.
[08:10] 대화 기록은 덧붙이기 만하고 도구
[08:11] 선택은 자동으로 두고 응답 블록은
[08:14] 타입으로 읽습니다. 그러면 코드를
[08:16] 고치지 않고도 단계를 위 아래 모델로
[08:18] 옮길 수 있습니다.
[08:22] 마지막으로 공개 벤치마크는 출발점일
[08:24] 뿐입니다. 실제 작업을 모아 통과
[08:26] 기준을 정하고 후보 모델을 에포트 두
[08:28] 세 단계로 돌려 작업마다 비용을
[08:30] 기록합니다. 점수와 지출을 그래프로
[08:33] 그린 다음 이긴 구성을 실제 트래픽
[08:35] 일부에 먼저 적용합니다.
[08:37] 클라우드 코드에서는 더 간단히 확인할
[08:39] 수 있습니다. 백로그의 작업 하나를
[08:41] 슬래시 모델 명령으로 두 모델에서
[08:43] 돌려보고 [음악]
[08:44] 슬래시 유시지가 보고하는 값을
[08:46] 비교하면 됩니다.
[08:48] 정리하겠습니다. 오퍼스 5.5
[08:50] 미디엄에서 시작합니다. 모델을 바꾸기
[08:52] [음악] 전에 에포트를 먼저
[08:54] 조정합니다. 그리고 토큰 단가가
[08:55] 아니라 완료한 작업당 비용으로
[08:57] 고릅니다.

## 트랜스크립트 — en-orig (영어 더빙 트랙 ASR — 대조용, 인용하지 않음 · 모델 버전이 틀림)

[00:00] There are four tasks for the online
[00:02] store project. Migrating the entire code
[00:04] to TypeScript, a monthly subscription
[00:06] feature, product pages, and customer
[00:07] message classification.
[00:09] Which Claude model should handle these
[00:11] tasks?
[00:13] This video summarizes the model
[00:14] selection guide written by Eddie Osman
[00:16] on the Claude developer blog.
[00:18] Fable, Opus, Sonnet, and Haiku. We will
[00:20] look at when to use each of the four
[00:22] models in turn.
[00:25] To start with the conclusion, when
[00:27] you're unsure, you can begin with Opus
[00:29] 3.5 at medium effort.
[00:30] It is the default model for Claude Code
[00:32] , and its token price is half that of
[00:34] Fable 3.5.
[00:36] Let's first look at the pricing for the
[00:37] four models. Based on 1 million input
[00:39] and output tokens, Haiku 3.5 is 10 cents
[00:42] and 50 cents, Sonnet 3.5 is $ 2 and $ 10
[00:44] , Opus 3.5 is $ 4 and $ 20, and Fable
[00:47] 2024 is $ 8 and $ 40. The context window
[00:49] for all four models is 1 million tokens
[00:50] .
[00:52] The default API effort also differs by
[00:54] model. Haiku and Opus are set to medium
[00:56] , while Sonnet and Fable are set to high
[00:57] .
[00:58] In Claude Code, Sonnet and Fable also
[00:59] start at medium.
[01:01] You can check your current settings with
[01:02] the/effort status command.
[01:07] Now, let's assign the tickets.
[01:09] The large-scale migration from
[01:10] JavaScript to TypeScript is the task for
[01:12] Fable 2024.
[01:14] It is the right model for major
[01:15] refactoring, migrations, architectural
[01:17] design, and long-running tasks without
[01:19] human supervision.
[01:21] The monthly subscription feature is best
[01:23] suited for Opus 3.5. It offers a great
[01:24] balance of cost and performance for
[01:26] developing features across multiple pull
[01:27] requests and daily debugging.
[01:30] Computer use tasks that involve many
[01:31] screenshots should also start with Opus
[01:33] .
[01:34] Product pages are for Sonnet 3.5. It
[01:36] handles well-defined tasks like bug
[01:38] fixes or features with clear
[01:39] specifications at half the token price
[01:41] of Opus.
[01:42] It is also well-suited for chat, as well
[01:43] as working with documents and slides.
[01:46] Customer message classification is for
[01:47] Haiku 3.5. It is the fastest and
[01:49] cheapest option for simple, high-volume
[01:51] tasks like classification, routing, and
[01:52] bulk exports.
[01:53] It is also excellent as a sub-agent
[01:54] handling auxiliary tasks for larger
[01:56] models.
[01:57] Handling the four tickets is divided in
[01:59] the same way.
[02:00] For chats and interactive sessions, use
[02:02] Sonnet 3.5 at low or medium effort, or
[02:04] send simple bulk chats to Haiku.
[02:06] Repetitive agent tasks like research,
[02:08] reviews, and drafting can be handled
[02:10] sufficiently with Sonnet at medium
[02:11] effort.
[02:14] In-depth research and scientific
[02:15] quantitative analysis should start with
[02:16] Fable 2024.
[02:17] While Sonnet is the default for document
[02:19] work, documents based on complex
[02:20] financial models or vast raw data should
[02:22] start with Opus.
[02:23] Even with clear specifications,
[02:25] migrations or performance optimizations
[02:26] may require Opus.
[02:30] There is one important principle here.
[02:32] Adjust the effort before changing the
[02:34] model.
[02:35] Effort is a dial that lets you fine-tune
[02:36] the balance between cost and performance
[02:38] . However, increasing the effort does
[02:39] not give the model knowledge or
[02:41] capabilities it doesn't already have.
[02:44] Raising the effort makes the model think
[02:45] longer, call more tools, and verify its
[02:47] results more thoroughly. This makes the
[02:49] response time correspondingly slower.
[02:51] Since effort is roughly proportional to
[02:53] latency, you must weigh whether the
[02:54] increased accuracy is worth the wait.
[02:57] Let's look at the SWE-bench Pro results
[02:59] for Opus 5.5. Compared to High, Medium
[03:02] is about 2.5 points lower, but the cost
[03:04] is roughly 70%.
[03:05] Low is about 8 points lower, and the
[03:07] cost is about one-third.
[03:08] Extra High is 1.4 points higher, but it
[03:10] costs 2.5 times as much.
[03:13] Therefore, when you need to go beyond
[03:15] High, you should test a more advanced
[03:16] model with a lower effort setting.
[03:19] In Frontier Code 2.0, Fable 5.2 High
[03:22] scored 45.3%, while Opus 5.5 Max scored
[03:25] 45.5%.
[03:27] The scores were nearly identical, but
[03:29] the cost per task for Fable was about
[03:30] half.
[03:32] There are also cases in the opposite
[03:33] direction.
[03:34] In Terminal Bench 3.0, the previous
[03:37] model, Fable 5.1, scored 58.0%at Max,
[03:39] while Opus 5.5 reached 58.9%at High
[03:41] while using only half the tokens.
[03:45] This is why you should look at the cost
[03:46] per completed task, not the unit price
[03:47] of tokens.
[03:49] When the model fails to complete a task
[03:51] , follow these three steps in order.
[03:53] First, give the model a way to verify
[03:55] its own results, such as through tests
[03:57] or builds.
[03:58] Second, increase the effort by one level
[04:00] . Third, move to a more advanced model
[04:02] but start with a lower effort setting.
[04:06] If results can be verified automatically
[04:07] , there is an even better method. Run
[04:09] everything on Low and re-run only the
[04:11] failed tasks on High.
[04:13] With Opus 5.5, this method achieved
[04:14] about a 97%pass rate at a cost of about
[04:17] 17 cents per task.
[04:18] Running everything on High resulted in a
[04:20] 95.3%pass rate at 29 cents.
[04:25] When a human is waiting for a response,
[04:26] start with Sonnet 5.5 on Low or Medium.
[04:29] If you only need more speed from the
[04:30] same model, there is a Fast mode.
[04:32] It is supported by Opus 5.5 and Fable
[04:34] 5.2, but at a higher price.
[04:37] When generations change, speeds also
[04:38] change.
[04:39] Fable 5.2 is up to 30%faster in output
[04:42] than Fable 5.1, and Sonnet 5.5 is 30%
[04:44] faster than Sonnet 5.
[04:47] Context is also a cost. This is because
[04:49] large contexts are re-sent with every
[04:51] turn.
[04:52] The cache read cost for one turn is
[04:54] about 3 cents for a 150,000-token
[04:55] context, and about 0.4 cents for 20,000
[04:57] tokens.
[04:59] It is better to use expensive model
[05:00] context for reasoning and leave long
[05:02] readings to cheaper server agents.
[05:05] In long runs, most of the input is
[05:06] billed as a cache read.
[05:08] The cache read price for Opus 3.5 and
[05:10] Fable 2024 is the same at 20 cents per
[05:12] million tokens.
[05:13] So the difference between the two models
[05:15] lies in uncached input and output, where
[05:16] Fable is twice the price per token.
[05:19] Haiku 3.5 is the only model where the
[05:21] price changes based on the prompt length
[05:23] . If the prompt exceeds 100,000 tokens,
[05:25] the rate increases by five times. Even
[05:27] then, it is one-fourth the token price
[05:28] of Sonnet 3.5.
[05:30] When comparing, you must also calculate
[05:32] the cost of the most difficult tasks.
[05:33] This is because difficult tasks account
[05:35] for the majority of the expenditure.
[05:37] In a 20-question search benchmark, just
[05:39] two questions accounted for 43%of total
[05:41] spending.
[05:45] Now, here is how to use multiple models
[05:46] together.
[05:48] Prompt cache is tied to the model that
[05:49] created it, so changing models requires
[05:51] rewriting the entire conversation of the
[05:52] first turn to the cache.
[05:55] Therefore, perform switches at task
[05:57] boundaries, and in Claude Code, run/
[05:59] compact first.
[06:02] Thinking blocks may not carry over
[06:03] either. Higher-tier models can read the
[06:05] thinking blocks of lower-tier models,
[06:06] but moving down, previous reasoning is
[06:08] discarded.
[06:09] The request will succeed, but the new
[06:10] model will work without that reasoning.
[06:12] In the API, it is better to start a new
[06:14] conversation with a summary of the
[06:15] progress so far instead of the full
[06:16] history.
[06:18] Assign sub-agents to smaller models.
[06:21] Target tasks where errors are
[06:22] immediately apparent, such as finding
[06:23] files, running tests, or reading logs.
[06:25] You can simply designate the model as
[06:27] Haiku or Sonnet in the sub-agent
[06:28] definition. Leave code modifications and
[06:30] judgments to the main model.
[06:32] There are also things to be aware of. If
[06:34] a small model misreads search results,
[06:35] the main model will open the wrong file
[06:37] and waste tokens.
[06:39] And Claude Code's built-in Explorer
[06:40] sub-agent uses the session model by
[06:42] default.
[06:43] To lower costs, define your own Explorer
[06:45] with the model specified as Haiku.
[06:48] For large tasks that do not fit into one
[06:49] context, the higher-tier model breaks
[06:50] them down and distributes them among
[06:51] several workers. In a bug search of
[06:53] about 22 million tokens, a configuration
[06:55] where Opus 3.5 directed and Sonnet 3.5
[06:57] workers worked was about 1/3 cheaper
[06:59] than Opus alone, with almost identical
[07:01] performance.
[07:03] However, this method is not suitable for
[07:05] all cases. If it is a one-line task that
[07:07] depends on the previous step or a task
[07:08] that fits into one context, the cost of
[07:10] planning and merging is greater than the
[07:12] savings.
[07:14] There is also an Advisor tool where a
[07:15] cheaper model can seek advice from a
[07:17] stronger model while working. However,
[07:19] be cautious with that.
[07:20] In a case where a Fable 2024 advisor was
[07:23] attached to Opus 3.5, it cost about 2.1
[07:25] times more to improve by 1.75%. This
[07:28] means you should measure it first.
[07:32] You must also check for compatibility
[07:33] before switching models.
[07:34] In Sonnet 3.5, Opus 3.5, and Haiku 3.5,
[07:37] the setting to force tool use will
[07:38] trigger a 400 error.
[07:40] Opus and Haiku always operate with
[07:42] thinking enabled.
[07:43] When moving from Haiku 3.5 to 3.5, you
[07:45] must change your budget tokens to the
[07:47] Haiku level.
[07:49] There is one more thing for Haiku 3.5.
[07:51] Modifying content before the thinking
[07:53] block, such as system prompts, tools, or
[07:55] previous messages, will cause a 400
[07:56] error.
[07:57] If you use Claude Code or the Agent SDK
[07:59] , there's nothing to change, but if you
[08:01] edit the history directly, you must
[08:03] ensure you only append.
[08:05] If you use multiple models together,
[08:07] configure your requests to match the
[08:08] most restrictive model.
[08:10] Only append to conversation history,
[08:11] leave tool selection to automatic, and
[08:13] read response blocks by type.
[08:15] This allows you to move steps to higher
[08:17] or lower models without changing your
[08:18] code.
[08:22] Lastly, public benchmarks are just a
[08:24] starting point. Collect real tasks, set
[08:26] pass criteria, run candidate models
[08:28] through two or three steps, and record
[08:30] the cost per task.
[08:32] Graph the scores and spending, then
[08:33] apply the winning configuration to a
[08:35] portion of real traffic first.
[08:38] In Claude Code, you can verify this more
[08:39] simply.
[08:40] Run a single task from your backlog on
[08:42] two models using the/model command, then
[08:44] compare the values reported by/usage.
[08:48] Let's summarize. Start with Opus 3.5
[08:51] medium. Adjust your budget before
[08:53] changing the model. And choose based on
[08:55] the cost per completed task, not the
[08:57] token unit price.
