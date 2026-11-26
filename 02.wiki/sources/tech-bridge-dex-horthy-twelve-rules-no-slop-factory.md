---
title: "Tech Bridge — AI 코딩 공장이 슬롭을 안 내보내는 12가지 규칙 | Dex Horthy (한국어 해설): 최고 모델 16% · 공장은 새것이 아니다 · 앞 압력과 뒤 압력 · 적을 알라 · 계획은 얼마나 · 보여 주고 직접 시험하게 · 기계가 잡을 건 기계에게 · 돈으로 못 사는 것 · 안티 슬롭 선언 · 그래도 검토하는 이유"
type: source
tags: [software-factory, ai-slop, slopcodebench, dex-horthy, factory-ai, humanlayer, ai-engineer-code-summit, back-pressure, forward-pressure, loops, expected-pain, planning, visual-alignment, show-me, anti-slop-lint, deterministic-tools, feature-flags, software-forge, no-ai-slop-manifesto, code-review, maintainability, faros-ai, commentary-format, korean-narration, english-dub, video]
source-url: https://www.youtube.com/watch?v=4NqFB60bh1U
source-type: video
author: Tech Bridge (한국어 해설) · 바탕 Dex Horthy AI Engineer Code Summit 발표(원본 `-NFMsM2y0Vk`) · *No AI Slop: A Manifesto* · Gabe Orlanski *Slop Is Moving Up the Stack* · Faros AI *The Acceleration Whiplash* (모두 위키 미열람)
date-published: 2026-11-25
ingested: 2026-11-26
created: 2026-11-26
updated: 2026-11-26
---

# Tech Bridge — AI 코딩 공장이 슬롭을 안 내보내는 12가지 규칙 (Dex Horthy)

[[tech-bridge|Tech Bridge]]의 **12:13 한국어 해설, 공식 챕터 11.** [[dex-horthy|Dex Horthy]]가 [[ai-engineer|AI Engineer]] Code Summit에서 한 발표를 따라간다. 뼈대는 셋이다 — [[slopcodebench|SlopCodeBench]]의 새 점수(최고 모델 16.33%), [[software-factory|소프트웨어 공장]]을 슬롭 없이 돌리는 규칙 12가지, 그리고 이 무대에서 공개된 [[no-ai-slop-manifesto|안티 슬롭 선언]](신규). **Horthy의 두 번째 본인 발표 소스** 다 — 첫 번째는 10-15에 ingest한 [[tech-bridge-horthy-state-of-software-factory]](16분 발표 재배포)이고, 그때 *"12 factor factories"* 라 부르고 아홉 개에서 멈췄던 목록이 여기서 열두 개로 채워졌다.

테제(해설의 맺음):

> *"그래서 덱스의 공장은 셋으로 정리됩니다. 앞에서 밀고 뒤에서 거는 루프, 기계가 잡을 건 기계에게 맡기는 도구, 그리고 사람이 끝까지 쥐는 판단."*(11:57~12:04)

> **트랙과 인용.** `ko` = `ko-orig`(`kind=asr&lang=ko&variant=gemini`)는 한국어 내레이션이다. `en-orig`(`kind=asr&lang=en&variant=timing-optimized`)는 **두 가지가 섞여 있다** — 내레이션 자리는 영어 **더빙의 ASR**(인용하지 않음, 판독 대조용)이고, 원 발표 발췌 자리에는 **Dex Horthy의 원음** 이 잡혔다. 한국어 인용은 전부 ko-orig 내레이션, 영어 인용은 전부 en-orig에 잡힌 Horthy 원음이다.
>
> ⚠️ **Horthy 원음은 en-orig 단일 트랙이다 — 교차 확인 없음.** ko-orig의 같은 자리는 `[음악]` 표시뿐이다. 원음 조각은 아홉 곳(00:57~01:14 · 02:07~02:13 · 03:10~03:40 · 04:42~05:00 · 05:52~06:25 · 08:07~08:15 · 08:36~08:47 · 09:42~10:01 · 11:04~11:12)이고, 원음인지 더빙인지는 메타가 아니라 **내용으로 판정** 했다(1인칭 · *Uh / Um* · ko-orig가 비는 자리). 문장 앞뒤가 잘린 조각이 많다. ⚠️ 이 회차에도 영상 포맷 목록을 받지 못해 오디오 트랙 구성을 info.json으로 확인하지 못했다.
>
> ⚠️ **두 트랙 모두 무캡션인 자리**(en-orig 기준 다섯 곳, 약 47초: 02:00~02:07 · 04:32~04:42 · 07:55~08:07 · 10:51~11:04 · 11:15~11:21)는 내용 미상이다. 적지 않는다.
>
> ⚠️ **해설이고 2차 전달이다.** 위키는 원본 발표도, 선언문(slopmanifesto.com)도, Orlanski의 글도, Faros AI 보고서도 열지 않았다. 벤치마크 수치 · 보고서 수치 · 선언의 문구는 내레이션이 옮긴 한국어다. 규칙 12가지 가운데 Horthy 본인의 말로 확인되는 것은 원음 조각이 걸친 몇 개뿐이고 나머지는 내레이션의 요약이다.

## 1. 슬롭 없는 AI 코드 공장, 최고 모델의 점수는? (00:00~00:25)

- 물음: *"슬롭없이 돌릴 수 있을까요?"*(00:02) — *"최고의 모델이 받은 점수부터 보시죠. 16%."*(00:04~00:06)
- 무엇의 점수인가: *"처음 짜는 건 잘하는데 요구사항이 바뀔 때마다 자기 코드를 고쳐 나가게 하면 무너집니다."*(00:08~00:12)
- 곁들인 사례: *"요즘 클라우드는 파이썬 2 시절 문법으로 돌아가기까지 했습니다."*(00:13~00:15)[=Claude — 더빙 *Claude*, 원음 조각 04:50~05:00이 같은 이야기]
- 예고: *"덱스 호시가 무대에서 내놓은 규칙 12가지와 끝까지 사람이 봐야 하는 이유를 따라가 봅니다."*(00:20~00:24)

## 2. 공장은 새것이 아니다 (00:25~01:50)

- 화자 소개: *"덱스 호시는 코딩 에이전트를 두고 꾸준히 발표해 온 개발자입니다. 휴먼 레이어를 공동 창업했고 최근 팩토리에 합류했습니다."*(00:26~00:32)[=[[humanlayer|HumanLayer]] · Factory] 설명란 표기는 *Dex Horthy(Factory, 전 HumanLayer CEO)*. ⚠️ **소속이 바뀌었다** — 10-15 소스에서 그는 HumanLayer의 CEO로 자기를 소개했다. 합류 시점과 HumanLayer의 그 뒤는 소스에 없다. *팩토리* 를 [[factory-ai|Factory(factory.ai)]]로 읽은 것은 설명란 · tags의 *Factory* 와 뒤의 문맥(Claude Code · Codex와 나란히 놓인 제품, ESLint 플러그인)에 따른 것이다.
- 앞선 발표: *"지난 6월 그는 소프트웨어 공장이 왜 실패하는가 라는 발표를 했습니다."*(00:33~00:35) *"요지는 그래도 코드를 읽으라는 것이었죠."*(00:37~00:39)
- 그 사이 쌓인 데이터(Faros AI 보고서 — 설명란 *The Acceleration Whiplash*, 내레이션 전달): *"개발자 22,000명을 분석한 파로스 보고서를 보면 리뷰 없이 넘어가는 PR이 31.3% 늘었습니다."*(00:41~00:48) *"PR 하나당 사고는 242%, 개발자 한 명당 버그는 54% 늘었습니다."*(00:48~00:52) ⚠️ 기준 기간 · 비교 대상은 캡션에 없다. 영어 더빙은 첫 수치를 *늘었다* 가 아니라 *PR의 31.3%가 리뷰 없이 통과* 로 옮긴다 — 어느 쪽인지 위키는 정하지 않았다(보고서 미열람).
- Horthy 원음(en-orig 단일 트랙) — 자기에게 붙은 딱지를 받아넘긴다: *"Dex is the anti-software factory guy. Dex hates software factories. I actually love software factories. I'm a huge fan"*(00:57~01:02) 앞 발표의 제목은 이런 뜻이었다고: *"there are certain things you could do in your software factory that would cause it to fail."*(01:06~01:11)
- 결론부터: *"그는 결론부터 꺼냅니다. 소프트웨어 공장은 그냥 좋은 엔지니어링이라는 겁니다."*(01:21~01:24)
- AI 이전의 회사(내레이션 01:25~01:36): 기획자와 엔지니어가 할 일을 트래커에 올리고, 누군가 만들고, 테스트를 돌리고, PR을 올리고, CI가 검사하고, 사람이 리뷰하고, 조금씩 배포하고, 새벽 3시에 장애가 나면 모니터링이 사람을 깨운다.
- 바뀌는 것: *"에이전트 시대에 바뀌는 건 딱 한 칸입니다. 사람이 만든다가 에이전트가 만든다로 바뀌는 거죠."*(01:38~01:42) *"트래커, 테스트, CI, 배포는 30년 전부터 있던 것들입니다. 공장을 새로 짓는 게 아니라 원래 공장의 한 칸을 바꾸는 겁니다."*(01:42~01:48)

## 3. 앞에서 밀고, 뒤에서 거른다 (01:50~02:51)

- 공장을 키우는 두 방향. 첫째: *"첫째는 압, 압력. 일을 시작시키는 힘입니다."*(01:52~01:56)[=앞 압력 — 02:40의 *앞 압력* · 챕터 제목]
- Horthy 원음(en-orig 단일 트랙) — 앞 압력의 예: *"we take all the incidents that happen so that when I get page 3 in the morning, I'm looking at a pull request that we think is going to solve it."*(02:07~02:11) (ASR *page 3 in the morning* 은 새벽 3시의 호출로 읽힌다 — 10-15 소스의 *paged at 3:00 in the morning*.) ⚠️ 그 앞 02:00~02:07은 무캡션.
- 둘째: *"둘째는 뒤 압력입니다."*(02:22) *"이제 만드는 건 몇 분, 몇 시간이면 끝나는데 리뷰와 테스트는 여전히 며칠씩 걸립니다."*(02:22~02:27)
- 투자할 곳: *"그래서 에이전트 코드 리뷰, 에이전트 테스트, CRI와 린터에 투자합니다."*(02:27~02:31)[=CI와 린터 · 추정] *"사람이 끼지 않아도 에이전트가 스스로 더 나은 결과를 내게 하는 장치들입니다."*(02:33~02:37)
- **규칙 1 — 루프.** *"첫 번째 규칙은 루프입니다. 요즘 유행하는 루프라는 말을 그는 앞 압력과 뒤 압력이 맞물리는 것으로 봅니다."*(02:38~02:44) *"일은 자동으로 시작되고 사람 손에 닿을 때쯤엔 쉬운 문제는 이미 다 고쳐져 있어야 한다는 겁니다."*(02:44~02:49) → [[back-pressure]]

## 4. 적을 알라 (02:51~05:19)

- **규칙 2 — 적을 알라.** *"두 번째 규칙은 적을 알라. 여기서 적은 모델의 약점입니다."*(02:51~02:53) *"아무도 지켜보지 않으면 모델은 코드베이스의 품질을 오래 지키고 개선하는 데 서툴다는 겁니다."*(02:55~02:58)
- 그가 그린 그림: *"한 번에 끝나는 문제를 푸는 실력은 해마다 쭉쭉 올라갔는데 코드베이스를 개선하는 실력은 그 사이 조금밖에 오르지 않았습니다."*(03:00~03:07)
- Horthy 원음(en-orig 단일 트랙) — 벤치마크가 재는 것: *"a model can clone all of Excel or Redis in a couple days, uh maybe even a couple hours now with, like, agent swarms. Uh, but that requires knowing the entire problem in advance. And most of us don't write software that way."*(03:15~03:25) *"Most of us ship a feature, and then ship another feature, and then ship another feature."*(03:27~03:30) 손으로 짤 때는 중간에 나쁜 추상화를 알아보고 모으고 걷어 낸다는 말에 이어: *"this is a benchmark that measures a model's ability to evolve a code base over time."*(03:36~03:40)
- **SlopCodeBench**(내레이션): 위스콘신대학교 연구실에서 나온 시험이다(03:43~03:44 — ASR *연구실 검증 시험* 의 정확한 말은 정하지 않았다). *"문제 36개를 체크포인트 196개로 쪼갰습니다."*(03:44~03:49) *"첫 명세로 프로그램을 짜고 명세가 바뀔 때마다 자기 코드를 고쳐 나갑니다. 숨은 테스트로 채점하고 슬롭이 얼마나 쌓였는지도 봅니다."*(03:50~03:56)
- 지표: *"엄격 기준은 앞선 체크포인트의 테스트까지 전부 통과해야 점수를 줍니다."*(03:58~04:02) *"그 기준으로 1등인 GPT-6 아스트라 엑스 하이가 16.33% 196개 중 서른 두개였습니다."*(04:02~04:08) 설명란도 *16.33%(196개 중 32개)*. → [[slopcodebench]] · [[openai-astra]] ⚠️ *엑스 하이* 가 가리키는 설정 이름은 정하지 않았다.
- 벤치를 이끄는 Gabe Orlanski의 정리(내레이션 전달 · 설명란 *Slop Is Moving Up the Stack*): 통과율로 보이는 수치는 오르고 슬롭은 줄었지만(04:12 — ASR *프리율*, 정하지 않음) *"슬롭은 사라진 게 아니라 설계 결정으로 자리를 옮겼다."*(04:14~04:16)
- 예 — 라이브러리: 같은 구현 에이전트에게 라이브러리를 주고 문제를 풀게 하면 *"라이브러리를 피해 우회하는 비율이 사람이 짠 라이브러리에선 27%, 에이전트가 짠 라이브러리에선 40%였습니다."*(04:22~04:28) ⚠️ 04:32~04:42는 무캡션.
- Horthy 원음(en-orig 단일 트랙, 앞이 잘림): *"it almost feels like we're like the, the slop is amplifying over time."*(04:46~04:48) 그리고 Python 2 문법 이야기 — *"per s format strings are back, and they will not use f strings by default anymore."*(04:54~04:58) ⚠️ 바로 앞 문장은 ASR이 *clot and glit Python 3 in Python 2 style* 로 적어 주어를 글자로 확인할 수 없다(내레이션은 *Claude* 라고 한다). *per s* 는 `%s` 로 보이나 추정이다.
- Anthropic의 안내: *"엔트로픽은 새 모델 페이블에게 코드 베이스의 주인이라고 알려 주면 깨끗하게 관리한다고 안내합니다."*(05:04~05:08)[=Anthropic · Fable] *"덱스는 아직 확인 중이라고 했습니다."*(05:10) ⚠️ Fable의 어느 판인지, 안내의 출처가 무엇인지는 캡션에 없다.
- 결론: 코드베이스가 오래 살아야 한다면 *"사람이 시스템과 코드를 계속 이해하고 있어야 한다는 겁니다."*(05:14~05:17)

## 5. 계획은 얼마나 (05:19~06:36)

- **규칙 3 — 만들기 전에 계획하라.** *"세 번째 규칙은 만들기 전에 계획하라."*(05:19~05:21) *"앞에서 30분을 쓰면 리뷰에서 몇 시간을 아낀다는 겁니다."*(05:22~05:24) AI 이전에도 아키텍처 리뷰와 스프린트 계획이 있었다(05:26~05:31). *"만드는 게 빨라져도 제대로 하는 리뷰는 여전히 느립니다."*(05:32~05:34)
- **규칙 4 — 과하게 하지 말라.** *"그런데 네 번째 규칙은 반대 방향입니다. 계획을 과하게 하지 말라."*(05:38~05:42) *"자신도 명세에 여섯 시간을 쓰고 나서 그냥 대충 시킬 걸 그랬다 싶었던 적이 있답니다."*(05:43~05:47)
- Horthy 원음(en-orig 단일 트랙, 첫 줄은 앞이 잘림) — 곡선: 짧은 프롬프트 쪽은 *50%* 라는 수만 남아 있고(05:52), *"You could spend 5 hours handwriting a detailed spec and maybe there's a 10% chance you have to change afterward."*(05:55~05:59) *"Or you could write all the code by hand in 20 hours and then there's like a 0% chance."*(06:01~06:04) 단서: *"You know, people still make mistakes too."*(06:07~06:09)
- ⭐ 기준: *"I think about this in terms of expected pain. Like, how likely will this have to change later, how hard will it be to change?"*(06:10~06:17) *"I don't argue with the model during planning about what color it is, but do make our database schemas right and stuff like that."*(06:20~06:25) → [[expected-pain-planning]]
- 내레이션의 정리: *"정리하면 바꾸기 어려운 것일수록 앞에서 공을 들이라는 겁니다."*(06:28~06:30) *"버튼 색은 나중에 바꿔도 되지만 데이터베이스 구조는 그렇지 않으니까요."*(06:32~06:34)

## 6. 보여 주고, 직접 시험하게 (06:36~07:05)

- **규칙 5 — 눈으로 맞춰 보라.** *"다섯 번째는 눈으로 맞춰 보라."*(06:36) 글로 된 긴 계획 대신 *"HTML 목업, 표, 차트를 보면서 에이전트와 방향을 맞추라는 겁니다."*(06:39~06:43) *"그가 공개한 쇼미라는 스킬이 그런 용도입니다. 사람은 수백만 년을 눈으로 살아왔고 글을 읽은 건 5,000년쯤이라면서요."*(06:44~06:50)[=show me 스킬]
- **규칙 6 — 직접 시험하게 하라.** *"여섯 번째 규칙. 에이전트가 자기 일을 직접 시험하게 하라. 스크린샷, 브라우저, 영상, 콜 뭐든 좋습니다."*(06:52~06:56) (ASR *콜* 은 curl로 보인다 — 10-15 소스의 *let them use curl*. 추정.) *"iOS 앱을 만든다면 에이전트가 그 앱을 직접 빌드하고 실행하고 테스트할 수 있어야 한다는 거죠."*(06:59~07:03) → [[agent-verification-skill]] · [[agent-visual-qa]]

## 7. 기계가 잡을 건 기계에게 (07:05~08:18)

- **규칙 7 — 결정론적인 도구.** *"일곱 번째 규칙은 결정론적인 도구로 슬롭과 싸우라는 겁니다. 같은 코드에는 늘 같은 판정을 내리는 린트 규칙 같은 것들입니다."*(07:05~07:11) 재료 셋: *"클라우드 플레어의 수석 엔지니어 딜런 몰로이가 만든 안티 슬롭 저장소에는 에이전트가 슬롭을 못 만들게 막는 규칙이 100개쯤 들어있습니다."*(07:11~07:18)[=[[cloudflare|Cloudflare]] · 10-15 소스의 *Dylan Mulroy*(en-orig ASR 표기 — 철자 미확인)] *"팩토리도 ES 린트 플러그인을 냈고 슬롭 코드 벤치의 파이썬 품질 규칙도 가져다 쓸 수 있습니다."*(07:18~07:24)[=ESLint] → [[hard-vs-soft-enforcement]]
- **규칙 8 — 슬롭도 도구다.** *"슬롭도 도구다."*(07:25) *"바이브 코딩이나 프로토타입처럼 사람들이 원하기는 하는지부터 알아봐야 할 땐 대충 만든 코드도 괜찮습니다."*(07:25~07:31) → [[disposable-vs-durable-software]] · [[vibe-vs-agentic-coding]]
- **규칙 9 — 모델이 실험하게 하라.** *"모델이 실험하게 하라. 포스트 호그, 스태시그 같은 기능 플래그 시스템을 지워주면 이것저것 켜 보고 더 나은 쪽을 고를 수 있습니다."*(07:33~07:40)[=PostHog · Statsig(추정) · *지워주면* 은 *쥐여 주면* 으로 보인다(추정)]
- **규칙 10 — 쌓이게 하라.** *"열 번째로 시간이 갈수록 쌓이게 하라. 전부 평가하고 지난 세션에서 배우라는 겁니다."*(07:40~07:44) → [[trace-to-memory-loop]]
- **규칙 11 — 포지를 하나로.** *"열 한 번째는 포즈를 하나로 모으라. 코드는 깃허브에 모였는데 계획과 결정은 아직 여기저기 흩어져 있다고"*(07:46~07:50)[=포지(forge) — 설명란 *포지 통합* · 더빙 *Forge*] ⚠️ 07:55~08:07은 무캡션. Horthy 원음(en-orig 단일 트랙): *"centralizing all of your designs and decisions, and like whatever you have, like Notion and Google Docs, and whatever it is, you should try to bring those things as close as possible together."*(08:08~08:15) → [[agent-platform-layers]]

## 8. 돈으로 못 사는 것 (08:18~09:02)

- **규칙 12 — 전부 살 수는 없다.** *"마지막 12번째 규칙은 전부 살 수는 없다."*(08:05~08:09) 층마다 다르다: *"샌드박스같은 인프라는 사거나 만들면 되고,"*(08:11~08:14) 하네스는(ko-orig에는 낱말이 빠져 있다 — 더빙 *for HANS*, 추정) *"클라우드 코드나 코덱스, 팩토리 같은 제품을 사거나 가볍게 직접 짤 수 있습니다."*(08:25~08:29)[=Claude Code · Codex · Factory] *"개발 환경은 팀마다 너무 달라서 직접 갖고 있지 않으면 마찰이 큽니다."*(08:30~08:32)
- ⭐ Horthy 원음(en-orig 단일 트랙) — 살 수 없는 것: *"Don't think anyone can sell you verification of your code."*(08:36~08:37) *"You know how to test your code."*(08:44~08:45) *"Not just a black box you can buy."*(08:47) (첫 문장은 ASR이 주어 없이 적는다.)
- 공장의 목적: *"공장의 목적은 사람의 지렛대를 키우는 것, 우리 시간을 가장 값지게 쓰는 것이라고 했습니다."*(08:55~08:59)

## 9. 안티 슬롭 선언 (09:02~10:43)

- 공개: *"이 무대에서 덱스는 안티 슬롭 선언을 공개했습니다. 코드 서밋의 연사와 참가자들이 함께 쓴 글입니다."*(09:03~09:07) 설명란 표기는 *No AI Slop: A Manifesto*(slopmanifesto.com, 위키 미열람). → [[no-ai-slop-manifesto]](신규)
- 본보기: *"2001년 엔지니어 17명이 스키 산장에 모여 애자일 선언을 썼던 것처럼 이번엔 AI 슬롭에 맞서는 선언을 쓰자는 겁니다."*(09:09~09:15)
- **다섯 가치**: *"산출물보다 결과, 속도보다 이해, 모델의 첫 초안보다 내 생각, 쉬운 일보다 더 나은 일, 출력을 땜질하기 보다 시스템을 고치는 것."*(09:18~09:25)
- **슬롭의 정의**: *"만드는 데 들인 노력보다 받는 사람에게 이해하라고 요구하는 노력이 더 큰 것."*(09:29~09:32) *"AI를 썼다고 다 슬롭은 아닙니다. 품질과 읽는 사람의 경험을 책임지지 않고 AI 출력을 넘길 때 슬롭이 됩니다."*(09:33~09:39)
- Horthy 원음(en-orig 단일 트랙, 앞이 잘림): *"It can only amplify our judgment, or uh maybe perhaps our lack of judgment in certain cases."*(09:45~09:49) *"the slop is asymmetric."*(09:51) ⚠️ 이어지는 비용 문장은 ASR이 깨져 있어(*the cost of producing line PR 10-page doc is approaching the cost of constant*) 옮기지 않는다.
- 첫 믿음(선언): 에이전트는 *"한 사람이 평생 리뷰할 수 있는 양보다 많은 일을 하루만에 만들어냅니다."*(10:06~10:09) (주어는 ASR *에이전트 때는* — *떼* 인지 정하지 않았다.)
- **슬롭이 생기는 이유**: *"빼기보다 더하기에 쏠린 도구, 사람의 한계를 넘으라고 몰아붙이는 압박, 그리고 복리."*(10:13~10:17) 복리의 뜻: 지식 베이스와 채팅, 코드의 *"슬롭이 쌓일수록 다음 에이전트가 그걸 읽고 베낍니다."*(10:19~10:21) *"그러다 팀은 슬롭과 싸울 의지마저 잃습니다."*(10:23~10:24)
- **서명자의 다짐**: *"모델과 일해도 생각은 내가 하고 AI가 얼마나 도왔든 내 보낸 것은 내가 책임진다."*(10:27~10:31) *"에이전트가 쓴 걸 보낼 땐 그렇다고 밝히고 중요한 부분은 확인한다."*(10:32~10:34) *"슬롭을 받으면 친절하게 말해주고 먼저 검토해 달라고 한다."*(10:36~10:39)
- *"덱스는 자기도 그런 말을 들어본 적이 있다고 털어놨습니다."*(10:40~10:42)

## 10. 그래도 검토하는 이유 (10:43~11:50)

- 물음(10:44 — ASR *코드를 전부 밀라는 걸까요* 는 판독하지 못했다): *"마지막 대목은 조금 더 현실적입니다."*(10:47) ⚠️ 10:51~11:04는 무캡션.
- Horthy 원음(en-orig 단일 트랙, 조각): *"AI agent reviewers, lters, verifiers useful , excuse me, they are not sufficient."*(11:04~11:12) — 에이전트 리뷰어 · 린터 · 검증기는 쓸모 있지만 충분하지 않다는 말로 읽힌다(ASR *lters* → linters, 추정). ⚠️ 왜 충분하지 않은지 — 챕터 제목이 말하는 *이유* 자체 — 는 앞뒤 무캡션 구간에 있어 내용 미상이다.
- 재는 것: *"중요한 건 코드 줄수나 머지한 PR 수, 동시에 돌리는 에이전트 수가 아니라 무엇을 내보냈고 누가 쓰고 그게 어떻게 돕는가입니다."*(11:20~11:26)
- 검토하지 않은 것도 다 나쁘지는 않다: *"검토하지 않은 출력이 다 나쁜 것도 아닙니다. 한 번에 던지는 프롬프트나 바이브 코딩은 지렛대가 큰 도구입니다."*(11:28~11:33)
- 선을 긋는 자리: *"슬롭이 나쁜 건 결과를 망칠 때입니다. 쓸모 있는 제품, 유지보수할 수 있는 시스템, 서로의 시간을 아끼는 일을 망칠 때요."*(11:35~11:40)
- 선언의 마지막 문장: *"우리 중 누구도 이걸 다 알아내지 못했다. 각자 무엇을 받아들이고 무엇을 거절할지 다시 배우는 중이다."*(11:44~11:48)

## 11. 처음 숫자로 (11:50~12:13)

- *"최고의 모델도 코드를 계속 고쳐 나가는 시험에서는 16%였습니다."*(11:52~11:54)
- 맺음 물음: *"여러분의 공장에서 사람이 마지막으로 보는 건 무엇인가요? 코드인가요, 계획인가요? 아니면 아무것도 없나요?"*(12:06~12:09)

## 규칙 12가지 (내레이션의 번호)

| # | 규칙 | 근거 트랙 |
|---|---|---|
| 1 | 루프 — 앞 압력과 뒤 압력이 맞물리는 것 | 내레이션 + 원음 조각(앞 압력의 예) |
| 2 | 적을 알라 — 감독 없는 모델은 코드베이스 품질을 지키지 못한다 | 내레이션 + 원음 조각 |
| 3 | 만들기 전에 계획하라 | 내레이션 |
| 4 | 계획을 과하게 하지 말라 | 내레이션 + 원음 조각(expected pain) |
| 5 | 눈으로 맞춰 보라 | 내레이션 |
| 6 | 에이전트가 자기 일을 직접 시험하게 하라 | 내레이션 |
| 7 | 결정론적인 도구로 슬롭과 싸우라 | 내레이션 |
| 8 | 슬롭도 도구다 | 내레이션 |
| 9 | 모델이 실험하게 하라 | 내레이션 |
| 10 | 시간이 갈수록 쌓이게 하라 | 내레이션 |
| 11 | 포지를 하나로 모으라 | 내레이션 + 원음 조각 |
| 12 | 전부 살 수는 없다 | 내레이션 + 원음 조각(검증은 못 산다) |

## 위키의 읽기

- **아홉에서 열둘로.** 10-15 소스의 *"12 factor factories"* 는 화자 스스로 아홉 개라고 세었다. 이 편의 목록과 맞춰 보면 그때의 것(계획 · 시각 정렬 · 자기 테스트 · anti-slop 규칙 · 실험 · 루프 · 누적)이 그대로 남았고, 그때 목록 밖에 있던 것이 번호를 받았다 — *적을 알라*(그때는 테제였다) · *포지 통합*(그때는 별도 절) · *전부 살 수는 없다*(그때는 네 층 표의 *buy or build*). **새로 들어온 것은 *슬롭도 도구다* 와 *과하게 계획하지 말라* 의 독립 번호** 다. 그때 번호가 있던 *사용자 피드백 · 인시던트를 에이전트 PR로* 는 이 편에서 앞 압력의 예로 들어갔다. ⚠️ 번호는 내레이션이 매긴 것이고 원 발표의 슬라이드는 확인하지 않았다.
- **검증은 살 수 없다.** 10-15 소스의 네 층은 전부 *buy or build* 였다. 이 편은 한 가지를 뺀다 — 자기 코드의 검증이다. [[verification-bottleneck]]이 말하는 병목이 왜 조직 밖으로 넘겨지지 않는지에 대한 한 줄이고, 화자가 코딩 에이전트 제품 회사(Factory)에 있으면서 한 말이라는 점이 눈에 띈다.
- **슬롭의 정의가 비용의 비대칭으로 옮겨 갔다.** [[ai-slop]]의 앞선 정의들은 물건의 성질(평균으로 쏠림 · 누적)이나 주의 포획을 말했다. 선언의 정의는 **만든 쪽과 받는 쪽의 노력의 비** 다 — AI를 썼는지가 아니라 책임을 졌는지가 기준이다. → [[no-ai-slop-manifesto]] · [[verification-cost-asymmetry]]
- **같은 행사의 다른 발표들.** [[lauren-tan|Lauren Tan]]의 [[tech-bridge-lauren-tan-all-code-is-slop]](판정을 사람 눈에서 검사로) · [[tech-bridge-walden-yan-cognition-no-laptop-development]](사람 승인 없는 머지) · [[tech-bridge-thariq-shihipar-human-folder-unacceptable]](공장이면서 공방)이 같은 Code Summit 발표의 해설이다. Horthy는 그 가운데 **사람이 끝까지 쥐는 판단** 쪽에 선다. 다만 *검토하지 않은 출력이 다 나쁜 것도 아니다* 라는 단서를 달아 10-15의 *for now we should probably read the code* 보다 자리를 나눠 말한다.
- **수치가 이어진다.** 10-15 소스에서 GPT-5.5는 14.8%, Astra는 그보다 1~1.5%p 높다고 했다. 이 편의 16.33%는 그 범위와 맞는다(같은 지표라는 전제에서 — 그때는 지표 이름이 발화되지 않았다).

## 해소하지 않고 표시만 한 것

- Faros 보고서의 첫 수치가 *증가율* 인지 *비율* 인지(내레이션과 더빙이 갈린다).
- *지난 6월* 발표가 10-15에 ingest한 발표와 같은 것인지 — 그 소스는 행사명을 말하지 않았고(AGNTCon NA 추정) 화자가 *"this talk from June"* 을 따로 가리켰다. 정하지 않았다.
- Code Summit의 날짜 · 장소는 이 소스에 없다. 설명란 표기는 *AI Engineer Code Summit*.
- 선언의 서명자 수 · 작성 과정은 *연사와 참가자들이 함께 쓴 글* 이라는 한 줄뿐이다.
- 왜 에이전트 리뷰어만으로는 충분하지 않은지(무캡션).

## 등장 인물 · 조직 · 개념

- 사람: [[dex-horthy]] · Gabe Orlanski(SlopCodeBench를 이끄는 사람으로 — 페이지화하지 않음, → [[slopcodebench]]) · Dylan Mulroy(안티 슬롭 저장소 — 페이지화하지 않음)
- 조직: [[factory-ai]](화자의 새 소속 · ESLint 플러그인) · [[humanlayer]](공동 창업 · 전 소속) · [[ai-engineer]](Code Summit) · [[anthropic]](Fable 안내 한 문장 — 보강 없음) · [[cloudflare]](Mulroy의 소속으로만 — 보강 없음) · Faros AI(보고서 — 페이지화하지 않음) · PostHog · Statsig(기능 플래그의 예 — 페이지화하지 않음)
- 모델 · 도구: [[slopcodebench]] · [[openai-astra]] · show me 스킬(→ [[humanlayer]])
- 개념: [[no-ai-slop-manifesto]](신규) · [[software-factory]] · [[ai-slop]] · [[back-pressure]] · [[expected-pain-planning]] · [[hard-vs-soft-enforcement]] · [[agent-platform-layers]] · [[agent-visual-qa]] · [[verification-bottleneck]]

## References

- 영상: https://www.youtube.com/watch?v=4NqFB60bh1U
- raw: `01.raw/articles/2026-11-25_AI 코딩 공장이 슬롭을 안 내보내는 12가지 규칙 Dex Horthy.md`
- 앞선 관련 소스: [[tech-bridge-horthy-state-of-software-factory]] · [[tech-bridge-death-of-code-review]] · [[tech-bridge-lauren-tan-all-code-is-slop]] · [[tech-bridge-walden-yan-cognition-no-laptop-development]] · [[tech-bridge-thariq-shihipar-human-folder-unacceptable]]
- 설명란 참고(위키 미열람): 원본 발표 https://www.youtube.com/watch?v=-NFMsM2y0Vk · *No AI Slop: A Manifesto* https://slopmanifesto.com · Gabe Orlanski, *Slop Is Moving Up the Stack* https://gabeorlanski.github.io/posts/slop-moves-up/ · Faros AI, *The Acceleration Whiplash* https://www.faros.ai/research/ai-acceleration-whiplash
- 같은 회차(2026-11-26)에 ingest한 같은 행사(AI Engineer Code Summit) 발표 해설: [[tech-bridge-armin-ronacher-workshop-before-software-factory|소프트웨어 공장보다 공방을 먼저 지어라(Armin Ronacher)]]
