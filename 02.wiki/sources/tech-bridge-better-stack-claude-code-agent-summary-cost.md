---
title: "Tech Bridge — Claude Code 에이전트 요약에 비용 12%? (Better Stack): 백그라운드 에이전트 상태 요약의 숨은 사용량 측정과 끄는 방법"
type: source
tags: [claude-code, anthropic, background-agents, agent-summary, hidden-harness-calls, fork-subagent, subagents, prompt-caching, opentelemetry, observability, usage-limits, token-cost, bun, supply-chain, better-stack, vendor-claim, video]
source-url: https://www.youtube.com/watch?v=Cz9vbmmBNTc
source-type: video
author: Tech Bridge (번역 재배포, 내레이션 없음) · 원 제작자 [[better-stack]](설명란 근거 — 발화에서는 텔레메트리 목적지로만 나옴) · 발표자 개인 미상 · 원본 영상 링크 없음 · 녹화 2026-10-28 이후 며칠 안(추정)
date-published: 2026-11-02
ingested: 2026-11-03
created: 2026-11-03
updated: 2026-11-03
---

# Tech Bridge — Claude Code 에이전트 요약에 비용 12%? (Better Stack)

[[tech-bridge|Tech Bridge]]의 **4:50 1인 해설 영상, 공식 챕터 8, 내레이션 없음.** 오디오는 `English (US) original (default)` + 더빙 7개 언어이고 **한국어 트랙 · `ko-orig`가 없다** — 10-27 Voss 편부터 이어지는 영어 원본 오디오만 있는 구성이라 **인용은 en-orig로만** 한다. 제목의 "[한글자막]"과 달리 수동 자막은 없다. 00:00~00:22(첫 챕터 "소개" 전체)는 무캡션이고, 마지막 문장은 *"keep you guys up to"* 에서 잘린다. `upload_date` 20261102(UTC)는 KST로 **11-03 07:00**이다. raw: `01.raw/articles/2026-11-02_Claude Code 에이전트 요약에 비용 12% 사용량 실험과 끄는 방법.md`.

[[claude-code|Claude Code]]는 일을 백그라운드 에이전트에 넘기면 에이전트 패널에 **상태 요약 한 줄**을 띄운다. 화자는 그 요약을 만드는 모델 호출을 OpenTelemetry로 따로 떼어 쟀다. 테제(화자):

> **에이전트 요약은 사용자가 부르지 않은 모델 호출이다. 일하는 에이전트마다 30초에 한 번 대화 전체를 보내고, 트랜스크립트에 안 남아 사용량 집계에서 빠지며, 끄는 스위치가 없다. 가치는 있지만 이 방식은 비싸다.**

> *"Each one of those calls is about 40,000 input tokens. All to get back about 130 tokens of output"*(01:04~01:09) · *"running it on the full conversation every 30 seconds with no switch to turn it off isn't great."*(04:28~04:32)

### 수치 한눈에 (⚠️ 전부 화자 측정 · 전달, 위키 미확인)

| 출처 | 조건 | agent summary 비중 |
|---|---|---|
| 화자 테스트 1 | 기본 설정, 백그라운드 에이전트 1개가 `sleep 20` × 8 | **세션 비용의 12%** |
| 화자 테스트 2 | Opus로 TanStack 사이트, 백그라운드 에이전트 3개 | **사용량의 약 8%** |
| Flamerix(설명란 gist) | 팀 단위 OpenTelemetry, 매일 백그라운드 에이전트 다수 | 15~20% |
| Claude Code 팀원(Hacker News 답글) | 전체 텔레메트리, 지난주 | 비용의 약 2%, 터미널에서 약 6% |
| HN 스레드의 다른 사용자 | 자기 사용량 | 약 8~10% |
| 8월 GitHub 이슈 | 한 세션 | 전체 **요청 수**의 거의 4분의 1 |

> ⚠️ **원 제작자 귀속은 설명란 근거다.** 설명란은 *"Better Stack이 두 차례 측정한 결과"* 라고 쓴다. 발화에서 Better Stack은 *"sent it to Better Stack"*(00:38~00:39) — 텔레메트리 목적지로만 나오고, 측정은 1인칭 단수 *"I"* 다. 자사 관측 도구를 측정 도구로 쓰는 구성이라 [[better-stack|Better Stack]] 자체 채널 영상으로 추정한다. 발표자 개인 이름은 없다.

## 1. 소개 (00:00~00:22)

en-orig에 발화가 없다(무캡션, 첫 큐 00:22.3). 첫 문장이 *"So,"* 로 시작해 앞에 도입이 있었을 수 있다. 이 챕터의 내용은 쓰지 않는다.

## 2. 에이전트 요약의 비용 (00:22~01:19)

- **무엇인가**: *"if you haven't seen this bar before, it's the one that claude code uses when work is handed off to background agents."*(00:22~00:25) 상태 줄 논란을 바로잡는다 — *"it's the status line of the agents in the agent panel and not the main clawed one."*(00:28~00:32)
- **측정 방법**: *"I turned on Claude Code's open telemetry export and sent it to Better Stack where every request comes through tagged with a query source saying what it was for."*(00:36~00:43) — 요청마다 붙은 **query source** 태그로 비용을 용도별로 묶는다.
- **테스트 1**: 특별 설정 없는 세션에서 *"just asked a background agent to run sleep 20 eight times."*(00:47~00:49)
  - ⭐ *"After about 3 minutes, I had five requests with a query source of agent summary almost exactly 30 seconds apart."*(00:49~00:55)
  - *"the debug log shows the context growing every time from 18 messages to 42 because each recall[=call] sends the whole conversation so far."*(00:55~01:04)
  - ⭐ 호출당 약 40,000 입력 토큰 → 약 130 출력 토큰, 레이블은 *"running 7th 20 second sleep"* 같은 것(01:04~01:11).
  - ⭐ *"Once you group these by query source, you see the agent summary was 12% of the whole session's cost."*(01:11~01:18)

→ [[hidden-harness-calls]](신규)

## 3. 실제 작업에서의 측정 (01:19~01:58)

- **테스트 2**: *"use opus to build a tan stack site with three background agents. This run came out to about 8% of my usage for the agent summary."*(01:20~01:28)
- ⭐ **요약도 큰 모델로 돈다**: *"every one of those summary calls run on Opus as well and not a cheaper model like Haiku."*(01:28~01:34)
- 비교: *"a bit lower than the 15 to 20% that Flamerix found"*(01:36~01:38), 그 수치는 *"figures actually came from a whole team's open telemetry data running lots of background agents every day."*(01:42~01:45)
- ⭐ **집계에서 빠진다**: *"none of these summaries actually get logged in Claude codes JSONL transcripts. So, anything that works out your usage from those files, like CC usage, never actually sees these costs."*(01:47~01:56)

## 4. 앤스로픽 수치와 차이 (01:58~02:32)

- **[Anthropic 쪽, 화자 전달]** *"Someone on the claw code team did reply on Hacker News saying that across all of their telemetry, it was about 2% of the cost last week and about 6% in the terminal."*(02:00~02:08)
- 다른 사용자들: *"landed around 8 to 10% right where my Tanstack test did as well."*(02:09~02:14)
- ⭐ **편차의 이유 — wall-clock 주기**: *"it runs on wall clock time. Any agent that's working and whose transcript gets changed gets summarized every 30 seconds. So lots of longrunning agents add up pretty fast."*(02:15~02:24) 테스트 1은 *"an agent taking a tiny step every 20 seconds is pretty much close to worst case scenario."*(02:26~02:30)

> ⚠️ 2%(Anthropic 전체)와 12%(화자 최악 사례)는 **같은 것을 다른 분모로 잰 값**으로 보인다 — 전체 사용자 평균 vs 한 세션. 화자도 테스트 1을 최악에 가깝다고 인정한다. 위키는 HN 답글 원문을 찾지 않았다.

## 5. 캐시와 사용량 논란 (02:32~03:16)

- **반론과 재반론**: *"most of these input tokens are going to be prompt cash[=cache] reads since it only sends over a small difference each time."*(02:32~02:37) *"on the API, they are about a tenth of the normal price. But on a subscription, Anthropic only says they still draw usage and not how much."*(02:39~02:44) *"usage is still usage."*(02:46)
- **맥락**: 이번 주 사용량 한도가 빨리 닳는다는 불만이 많았다(02:49~02:57). *"On October 28th, Claude codes lead actually said they found no single root cause and pointed at heavy sessions with lots of agents."*(02:55~03:03) *"about 4 hours later, this gist hit the front page of hacker news."*(03:03~03:07)
- ⚠️ **새 발견이 아니다**: *"A GitHub issue from August measured it at almost a quarter of all requests in one session and it's still open with no reply from Anthropic."*(03:08~03:16)

→ [[prompt-caching]] · [[hidden-harness-calls]]

> ⚠️ 리드의 이름, HN 스레드 · GitHub 이슈 번호는 발화되지 않았다. "4시간 뒤 gist가 1면"은 시간 순서일 뿐 인과는 화자도 말하지 않는다. 8월 이슈의 "4분의 1"은 **요청 수** 비율이라 비용 비율(12% 등)과 단위가 다르다.

## 6. 설정을 끌 때의 절충 (03:16~03:55)

- *"So, can you actually turn this off? Well, not easily. There is no setting for this."*(03:16~03:20)
- **우회 1 — fork 서브에이전트 끄기**: *"One workaround that I've seen is the setting claude code fork sub agents. If you set this to zero, it disables fork sub agents and so the summaries go with them."*(03:20~03:28) 화자 재실행: *"agent summary did go to zero while the agents still ran in the background."*(03:30~03:34)
- ⭐ **대가**: *"you lose fork sub agents, which are the ones that inherit your whole conversation. So, to be clear, you don't lose background agents."*(03:36~03:41) 일반 서브에이전트는 *"They just start fresh with only the task that Claude hands them instead of full copy of your conversation before it and its prompt cache."*(03:44~03:51)

> ⚠️ 설정의 **정확한 이름 · 형식은 발화되지 않았다**(ASR *"claude code fork sub agents"*, 환경 변수로 추정). 왜 fork를 끄면 요약까지 사라지는지는 설명되지 않는다 — 화자 관찰은 "그렇게 됐다"뿐이다.

→ [[fork-subagent]](신규)

## 7. 타이머 우회법의 주의점 (03:55~04:22)

- **우회 2 — Flamerix**: *"They used a bun preload script which hooks set timeout and blocks the summary timer."*(03:57~04:03)
- ⭐ **설치 경고**: *"It hooks into every claw code process and the install command curls whatever the latest version is. So, make sure you read it and pin your own copy."*(04:06~04:13) — *"there seems to be an hourly critical CVE and daily massive attacks."*(04:16~04:20)

> ⚠️ 설명란 gist는 열어 보지 않았다. preload가 Claude Code 프로세스에 걸린다는 말은 Claude Code가 [[bun|Bun]] 런타임으로 돈다는 뜻으로 읽히지만, 화자는 그렇게 말하지 않는다(추정).

## 8. 요약 기능의 가치와 한계 (04:22~04:50)

- 화자 결론: 요약에는 가치가 있다 — *"Anthropic actually says that Claude uses these summaries itself to understand what the agent is doing"*(04:23~04:28) — 그러나 대화 전체 · 30초 · 스위치 없음은 문제다(04:28~04:32).
- *"I do hope that the cheaper version they're apparently working on does fix this."*(04:34~04:38) ⚠️ 출처 미발화.
- 화자 자신은 고치지 않는다 — *"I don't use clawed code much in the terminal anymore. I actually use T3 code, which handles summaries its own way."*(04:41~04:47) 영상은 *"keep you guys up to"* 에서 끝난다(캡션 잘림).

## 등장 개체

- 조직 · 제작자: [[better-stack]](신규, 설명란 근거 원 제작자 + 측정에 쓴 관측 플랫폼) · [[anthropic]] · [[tech-bridge]]
- 제품: [[claude-code]](백그라운드 에이전트 · agent panel · OpenTelemetry export · JSONL 트랜스크립트 · fork 서브에이전트) · [[bun]](preload 스크립트) · Opus · Haiku(버전 미발화, 링크 안 함) · ccusage · T3 Code · Hacker News · GitHub(페이지 없음)
- 인물: Flamerix(gist 작성자, 신원 미상) · Claude Code 리드 · HN 답글 팀원(이름 미발화) — 페이지 없음
- 개념: [[hidden-harness-calls]](신규) · [[fork-subagent]](신규) · [[prompt-caching]] · [[subagent-vs-thread-handoff]]

## 이 위키에서의 좌표

- [[prompt-caching]]은 지금까지 "캐시를 지키면 싸다"는 하네스 설계 쪽이었고 *"적중률 · 절감액 수치는 이 위키의 어느 소스에도 없다"* 고 적혀 있었다. 이 편은 **캐시 읽기도 구독 사용량을 먹는다**는 반대쪽 시선과, API에서 약 1/10이라는 화자 수치를 준다.
- [[subagent-folding]](10-29)과 [[subagent-vs-thread-handoff]]는 서브에이전트를 *언제 쓰나*였다. 이 편은 같은 Claude Code 안에서도 서브에이전트가 **fork(대화 · 캐시 상속)와 fresh(과제만)** 로 갈리고, 그 선택이 비용 구조를 바꾼다는 것을 보인다 → [[fork-subagent]].
- 11-02 [[tech-bridge-ai-labs-claude-code-verification-review-loop]]의 review-loop는 *"every one of those rounds uses up your limits"* 를 루프 종료 이유로 들었다. 이 편은 사용자가 만든 루프가 아니라 **하네스가 스스로 부르는 호출**이 한도를 먹는 경우다.

## ⚠️ 유보

- 원 제작자 Better Stack은 설명란 근거(+ 자사 제품 사용 정황), 발표자 개인 미상, 원본 링크 없음. 00:00~00:22 무캡션, 마지막 단어 잘림.
- 수치(12% · 8% · 40,000/130 토큰 · 18 → 42 메시지 · 15~20% · 2%/6% · 8~10% · 4분의 1)는 화자 측정(각 1회) · 전달이고, "cost"와 "usage"의 단위 · 캐시 할인 반영 여부는 발화되지 않았다.
- Anthropic 쪽 진술(HN 답글, 10-28 리드 발언, 구독에서 캐시 읽기 사용량 미공개, Claude가 요약을 스스로 쓴다, 더 싼 판본 작업 중)은 전부 화자 전달이고 원문을 찾지 않았다.
- 설정 이름 미발화, fork를 끄면 요약이 사라지는 이유 미설명, Flamerix gist 미열람.
- ASR: *"clawed"* · *"claw code"* = Claude, *"prompt cash"* = cache, *"recall"* = call(추정), *"CC usage"* = ccusage(추정). en은 `variant=gemini` 없이도 다시 쓴 문장이고(*"We've seen this problem before"* · *"derived sub-agents"*), ko는 그 en의 번역이라 background agents를 "신원조회 담당자"로, *"about 6% in the terminal"* 을 "6% 할인"으로 옮겨 인용하지 않았다.

## References

- raw: `01.raw/articles/2026-11-02_Claude Code 에이전트 요약에 비용 12% 사용량 실험과 끄는 방법.md`
- https://www.youtube.com/watch?v=Cz9vbmmBNTc
- 설명란 관련 자료(⚠️ 열어 보지 않았다): https://gist.github.com/flamerix-ai/c3905705cc4205e5de3011fa2e74efce
