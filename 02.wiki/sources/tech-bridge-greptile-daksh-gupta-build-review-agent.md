---
title: "Tech Bridge — AI 코드 리뷰 에이전트, 직접 만들 때 놓치기 쉬운 것들 (Daksh Gupta · Greptile): 다섯 가지 실패, 사고 PR 데이터셋, 모델 뒤집기, living wiki, 비용 분배"
type: source
tags: [automated-code-review, review-agent, greptile, daksh-gupta, nitpicks, defensive-code, incident-pr-dataset, model-inversion, codebase-context, grep, living-wiki, intent, autonomous-testing, computer-use, model-routing, vendor-claim, video]
source-url: https://www.youtube.com/watch?v=6slamFlG96Q
source-type: video
author: Tech Bridge (번역 재배포, 내레이션 없음) · 발표자 [[daksh-gupta]](설명란 근거 — 발화에 이름 없음) · 소속 [[greptile]](설명란 · 태그 · 발화의 ASR 변형) · 행사명 · 원본 링크 · 녹화일 미상
date-published: 2026-11-03
ingested: 2026-11-04
created: 2026-11-04
updated: 2026-11-04
---

# Tech Bridge — AI 코드 리뷰 에이전트, 직접 만들 때 놓치기 쉬운 것들 (Daksh Gupta · Greptile)

[[tech-bridge|Tech Bridge]]의 **15:26 1인 발표 영상, 공식 챕터 9, 내레이션 없음.** 오디오는 `English (US) original (default)` + 더빙 7개 언어이고 **한국어 트랙 · `ko-orig`가 없어** 인용은 en-orig로만 한다. 제목의 "[한글자막]"과 달리 수동 자막은 없다. en-orig는 *"Fore"*(00:10, 잡음으로 추정) 뒤에 비었다가 **문장 중간인 *"companies writing lots of code."*(00:26)에서 시작한다.** `upload_date` 20261103 = 2026-11-04 07:00 KST. raw: `01.raw/articles/2026-11-03_AI 코드 리뷰 에이전트 직접 만들 때 놓치기 쉬운 것들.md`.

[[daksh-gupta|Daksh Gupta]](설명란 근거)가 코드 리뷰 제품 회사 [[greptile|Greptile]]의 공동창업자 입장에서, **리뷰 에이전트를 직접 만드는 법과 그때 깨지는 지점**을 순서대로 말한다. 테제(이 페이지의 정리):

> **샌드박스 · PR 웹훅 · 프롬프트만으로 리뷰 에이전트는 돌아간다. 그러나 그 뼈대는 버그를 놓치고, 맥락을 모르고, 비싸고, 잔소리가 많고, 돌릴 때마다 다른 것을 찾는다. 치명적 버그는 드물어서 프롬프트를 고쳐도 나빠졌는지 알 수 없다. 그래서 사고를 낸 과거 PR로 재고, 작성 모델과 다른 모델에게 리뷰시키고, 코드 · 문서 맥락을 주고, 실제로 실행해 보고, 작은 일은 싼 모델에게 넘긴다.**

> *"many people think that's actually all it takes to build a review agent."*(01:16~01:19) · *"bugs are fractally infinite"*(01:43~01:46) · *"You don't know the counterfactual."*(04:39~04:40) · *"you might be able to actually get quite far in building your own review agent."*(15:14~15:17)

### 세 층을 나눠 읽는다

| 층 | 무엇 | 근거의 성격 |
|---|---|---|
| **[조언]** | 뼈대 구성, 프롬프트 방향, 사고 PR 재생, 흐름 문서화 | 직접 해 볼 수 있는 절차. 효과 수치 없음 |
| **[수치]** | 1/1000 사고율, Claude · GPT 버그 차이(약 3배), 뒤집기 10%, PR당 $3~25, 프런티어 20%, 하위 작업 20개 | **Greptile 내부 진술** — 표본 · 기간 · 모델 버전 미발화, 공개 자료 링크 없음 |
| **[제품]** | 여러 회사 코드 코퍼스, living wiki, 의존성 갖춘 샌드박스 + computer use, forward deployed 팀 | **자사 소개.** 직접 만들기의 한계마다 자사의 답이 붙는 구조 |

> ⚠️ **"직접 만드는 법"을 파는 쪽이 말한다.** 발표자는 직접 만들기를 말리지 않고 *"you can get decently far"*(06:30~06:31)라고 인정한다. 다만 한계 대목마다 자사 이야기로 넘어간다: 데이터셋(06:15) · 맥락(11:13) · 테스트(12:13). *"in ways that internal review agents can't."*(06:28~06:30) 위키는 어느 수치도 확인하지 않았다.

> ⚠️ **화자 귀속은 설명란 근거다.** 이름은 **설명란의 *"Greptile 공동창업자 닥시 굽타"* 에만 있고** 발화 · 태그에 없다(태그에는 `Greptile`만 있다). 라틴 표기 "Daksh Gupta"는 info.json 어디에도 없는 **로마자 표기**다. 회사 이름은 발화에 나오지만 ASR이 전부 뭉갰다 — *"Reptile"*(06:16 · 12:13) · *"Grapple"*(11:13) · *"graviles"*(12:26). 발화는 *"what we do at"* 식 1인칭 소속까지만 확인해 준다. 공동창업자라는 직함은 설명란에만 있다 → [[daksh-gupta]].

## 1. 소개 (00:00~00:26)

en-orig에 *"Fore"*(00:10) 한 큐만 있고 16초 비었다가 문장 중간으로 들어간다. 이 챕터의 내용은 쓰지 않는다.

## 2. 리뷰 에이전트의 기본 구조와 한계 (00:26~03:38)

- 배경: *"the new problem is the review bottleneck, the validation bottleneck."*(00:36~00:37) → [[verification-bottleneck]]
- **[조언] 뼈대** — *"you should get yourself a sandbox."*(00:42) *"You can also just use firecracker or something like that."*(00:45~00:48) 안에 에이전트를 둔다. *"Personally, I recommend going model independent for reasons that I will get into. So you can use something like Open Code or Pi as your harness."*(00:54~01:00) GitHub · GitLab을 연결해 *"have a PR web hook, send it the contents of a pull request."*(01:04~01:07) 결과는 GitHub 리뷰 API로 돌려보낸다(01:14~01:16). *"about 5 minutes later you will get some feedback on your pull request."*(01:28~01:32) → [[agent-sandboxing]]
- *"many many companies here that will sell you a sandbox."*(00:44~00:45) — "here"는 행사장의 스폰서를 가리키는 듯하다(추정, 행사명 미발화).

⭐ **뼈대에서 생기는 문제 다섯:**

| # | 문제 | en-orig |
|---|---|---|
| 1 | 버그를 놓친다 | *"you're going to miss a lot of bugs."*(01:35~01:38) 트윗 전달: *"bugs are fractally infinite"*(01:43~01:46) 그래도 최소한 *"prevent at least very catastrophic outages and incidents."*(01:54~01:56) |
| 2 | 맥락을 놓친다 | *"it's going to miss context"*(01:59) · *"one of those companies that never recovered from the microservices apocalypse of the 2010s."*(02:10~02:14) |
| 3 | 비싸다 | ⚠️ *"from people we've seen try to do this, they'll find that they're spending between three and up to $25 per poll[=pull] request on reviewing it using coding agents."*(02:26~02:35) |
| 4 | 잔소리(nitpick) | *"comments that are technically correct, but overly pedantic."*(02:45~02:47) 두 갈래 해악 — 사람에게는 *"like a boy that cries wolf."*(02:53), 코드에는 아래 |
| 5 | 돌릴 때마다 새로 찾는다 | *"every time you run a review agent on the same poll[=pull] request, you will somehow find new bugs"*(03:26~03:29) |

- ⭐ **잔소리가 코드베이스를 망가뜨리는 경로** — *"they will wreck your codebase because typically the way the review agents work is they leave comments on GitHub and your coding agent picks them up and resolves them."*(03:04~03:11) *"They're going to look at review comments and just address all of them and you'll end up with extremely painfully defensive code"*(03:12~03:18) 리뷰 잡음의 비용을 **사람의 주의**만이 아니라 **코드 품질**로 세는 대목이다 → [[automated-code-review]]
- 문제 5는 11-02 [[review-loop-termination]]의 Anthropic 기록(reviewer가 보고한 것의 약 59%가 첫 라운드부터 있던 것)과 **방향이 다르다.** 저쪽은 *옛 문제를 다시 찾는다*, 여기는 *새 것을 찾는다*다. 저쪽은 수정 후 반복이고 여기는 같은 PR 재실행이라 조건도 다르다.

## 3. 프롬프트를 어떻게 개선할까 (03:38~05:20)

- **[조언] 첫 개선** — *"the lowest hanging fruit"*(03:40). 두 방향: *"Look for specific bug types and second, skip the nitpicks"*(03:52~03:54)
  - 버그 유형: *"do some internal data science on existing outages and incidents that have happened in your codebase"*(04:00~04:04) 자주 내는 유형의 목록을 만들어 프롬프트에 넣는다(04:07~04:11).
  - nitpick: *"expressly tell it what a nitpick is and not to look for them."*(04:13~04:14) 예: *"asking why there isn't three layers of defense on this particular thing or why error handling is done in this slightly shoddy way."*(04:17~04:25) ⚠️ 오류 처리 지적까지 nitpick에 넣는 것은 발표자의 선이다. 기준은 제시되지 않는다.
- ⭐ **프롬프트 민감도** — *"when you change a small thing in the prompt, it'll have a weirdly big impact on the number of comments that your agent is writing on your P request."*(04:29~04:35) *"You don't know the counterfactual."*(04:39~04:40)
- *"can tell you about the presence of bugs, but it fortunately can't tell you about the absence of bugs."*(04:44~04:48) — 문맥상 *unfortunately*다(ASR인지 실언인지 미확인, `en`도 같다). 테스트에 관한 Dijkstra의 격언과 같은 모양이지만 발표자는 출처를 대지 않는다(이 비교는 위키의 일반 지식).
- ⭐ **희소성 — 측정이 어려운 이유** — ⚠️ *"according to our data science, only about one out of every thousand pull requests has a genuinely catastrophic bug in it. One every thousand lines of code has a catastrophic bug in it."*(04:57~05:04) 그래서 *"you might release a version of your agent that you think is very good, but it secretly misses a catastrophic bug in a pull request."*(05:06~05:14)

> ⚠️ **같은 숫자를 두 단위로 말한다.** 1,000 PR당 1건과 1,000줄당 1건은 PR 크기가 한 줄이 아닌 한 전혀 다른 비율이다. 자기 정정인지 말실수인지 알 수 없고, 어느 쪽이 Greptile 측정값인지 확정할 수 없다. 이 페이지는 첫 문장(PR)을 앞세우되 둘 다 미확정으로 둔다. "catastrophic"의 기준도 발화되지 않는다.
>
> ⚠️ *"fractally infinite"* 와 *"bugs are extraordinarily rare"*(04:54)는 표면상 부딪친다. 뒤 문장의 맥락이 **치명적 버그**라서 양립은 가능하지만, 발표자가 둘을 구분해 설명하지는 않는다.

## 4. 과거 PR로 성능 검증 (05:20~06:36)

- ⭐ **[조언] 둘째 개선** — *"You will want a data set of historical PRs."*(05:20~05:23) 사고를 카탈로그해 둔 회사라면 *"a list of pull requests that have caused outages and incidents in the past."*(05:29~05:32) 그다음 *"have any version of your review agent run through those and see with what frequency it can catch those bugs."*(05:36~05:40) → [[production-trace-eval-flywheel]]
- 한계 셋: ① *"the topology and ontology of bugs changes over time."*(05:50~05:51) → *"you'll need to have a real-time updating data set."*(05:51~05:53) ② *"unless you have millions and millions of pull requests, it's actually hard to have reasonably high coverage of bug types."*(05:56~06:00) ③ ⚠️ *"about 80 or 90% of your bugs will be just repeats of prior mistakes"*(06:02~06:05)이지만 코딩 에이전트가 좋아질수록 *"they're going to start making novel mistakes."*(06:07~06:08)
- **[제품]** *"this is kind of what we do at Reptile[=Greptile], except we actually have a lot of code from a lot of different companies and we can test across a very, very large corpus of pull requests"*(06:15~06:22)

> ⚠️ **"여러 회사의 코드로 시험한다"** 는 벤더의 강점 주장이자 데이터 취급에 관한 진술이다. 고객 동의 · 범위 · 격리 조건은 말하지 않는다. 이 위키는 Greptile의 약관을 확인하지 않았다.

## 5. 모델을 교차해 검토하기 (06:36~08:26)

⭐ 이 영상에서 위키에 가장 새로운 부분이다 → [[review-model-inversion]](신규)

- **[수치] 모델마다 버그가 다르다** — *"the types of bugs produced by cloud[=Claude] models or codex models are actually quite different from each other."*(06:38~06:42) *"cloud[=Claude] models are something like three times more likely to produce one-off errors than GBT[=GPT] models."*(06:45~06:51) *"GBT[=GPT] models on the other hand are significantly more likely to produce off[=auth] bypasses than cloud[=Claude] models."*(06:51~06:55) 원인: *"these are all just artifacts of the post training as far as I understand."*(06:55~06:58) (본인 유보)
- **[조언] 뒤집기** — 같은 모델이 쓰고 같은 모델이 리뷰하면 *"they fail in the same ways during review that they do during code generation."*(07:09~07:12) *"you'll want to invert the model. If you've used cloud[=Claude] code to write the code, you'll want to use a GPT model to review it"*(07:12~07:16)
- **작성 모델 알아내기** — *"straightforward for the 80th percentile and quite tricky for the last 20."*(07:22~07:24) 지문: *"codecs[=Codex] will name branches in a codec[=codex]/branch name format"*(07:32~07:34), *"claude is going to write a co-authored by claude in the PR description and commit message."*(07:37~07:39) 나머지는 휴리스틱, 사내 카탈로그, 개발 기기 텔레메트리(07:53~08:04).
- ⭐ **[수치]** ⚠️ *"We found that there's a 10% higher cache[=catch] rate if you flip models."*(08:06~08:08) 이어서 *"That means that there's a 10% higher chance that something will go wrong if you're not using model inversion"*(08:14~08:18)

> ⚠️ **"10%"의 해석이 한 문장 사이에 바뀐다.** 잡아내는 비율이 10% 높다는 말과 사고가 날 확률이 10% 높다는 말은 같지 않다. 상대값인지 퍼센트포인트인지, 어떤 모델 쌍 · 버그 등급 · 표본인지 말하지 않는다.
>
> ⚠️ *"one-off errors"* 는 off-by-one 오류의 ASR 또는 말버릇으로 보이지만 확정할 수 없다. *"off bypasses"* 는 09:38~09:49의 설명(*"authenticated environment"*(09:47))을 근거로 auth bypass로 읽었다. 모델 버전은 없다. ⚠️ `en`은 이 핵심 문장을 바꾼다 — `"unique errors"`(06:50) · `"omissions"`(06:55) · `"model versioning"`(08:19). ko도 같이 *"버전 관리"*(08:17)로 옮긴다. `en` · ko만 읽으면 이 절의 뜻이 사라진다.

## 6. 코드와 문서의 맥락 (08:26~11:48)

- **[조언] 셋째 개선 — 코드베이스 맥락** — *"Before we were doing code validation, we were doing codebase context."*(08:29~08:32) 회사의 출발점이라는 말이다.
- ⭐ **grep 비판** — *"people consider GP[=grep] to effectively solved all of codebase context. I actually think that's not true"*(08:38~08:42) *"GP[=grep] is extremely imprecise. And second, it's very expensive."*(08:43~08:46) 규모 논증: ⚠️ *"singledigit percentage points of GDP growth last year were inference."*(08:48~08:51) 그중 큰 비중이 코딩 에이전트이고, 트레이스를 보면 *"the vast majority of tokens used by coding agents are all the same. GP[=grep], file read, cache, write for the file contents."*(08:56~09:03) → *"a non-trivial percent of GDP growth is GP[=grep], file read, cach[=cache] write. That's very bad."*(09:03~09:06) 토큰 단위로 돈 받는 회사의 *"adverse incentives"*(09:13)도 넌지시 말한다.

> ⚠️ **GDP 논증은 수사다.** 출처 · 연도 · 국가가 없고, 중간 단계의 비율에도 수치가 없다.
>
> ⚠️ **Contradiction(약): grep은 비싼가.** 10-15 [[tech-bridge-braintrust-agentic-vs-vector-search-eval]]의 약 20행 실험에서는 grep 계열 agentic search가 벡터 검색과 정확도가 같고 비용이 4분의 1이었다. 비교 상대가 다르다(저쪽은 벡터, 여기는 사전 구축한 지식 베이스). 그리고 이 발표자는 인덱스를 파는 쪽이다 → [[agentic-search]]

- **[제품] 지식 베이스** — *"we produce an internal knowledge base where we essentially check across the entire codebase all the different parts, catalog them, and then index"*(09:23~09:31) 항목 예: *"this is authentication. Here's how it works. Here are the flows. Here's a diagram of the flows. Here's every file that's involved."*(09:32~09:36)
- 왜 필요한가의 예: *"It's actually very difficult to figure out if an off[=auth] bypass has occurred"*(09:41~09:44) 그 지점이 인증된 환경인지 알아야 하기 때문이다(09:45~09:49).
- ⭐ **버그가 아니어도 틀린 코드 — 의도** — *"code can be very very bad even if it's not buggy."*(10:00~10:02) *"it can just not fulfill the expressed intent of the author."*(10:06~10:08) Slack을 IDE로 쓴다는 글을 인용하며(*"Recently, I saw a post"*(10:10)) *"there's not that much expressed intent in a Slack message."*(10:16~10:20) → *"your correct code can actually still be quite wrong."*(10:35~10:37) → [[intent-md]]
- **[조언] 줄 맥락** — *"the two types of context that matter most are docs and tickets and then of course the codebase from your codebase indexer or knowledge base."*(10:42~10:49) Jira · Linear · Confluence · Notion 연결(10:53~10:56). *"there's a lot of tribal knowledge that is subconsciously helping you produce better code."*(10:58~11:01)
- ⭐ **[제품] living wiki** — *"we actually disintermediate all of these context sources with a living wiki. This wiki is essentially a sort of world model of how your company works."*(11:15~11:23) 재료: 코드베이스, *"production telemetry, through logs"*(11:28), 문서 · Linear 티켓. 효과 주장: ⚠️ *"it will never read a file that it didn't need to read."*(11:42~11:44) → [[context-engine]] · [[llm-wiki-pattern]]
  - ⚠️ 10-02 [[tech-bridge-death-of-code-review]]에서 [[laurie-voss|Voss]]는 Greptile을 **저장소 전체 그래프**로 소개했다(13:48~13:56). 여기서 발표자가 고른 말은 **knowledge base · wiki**이고 "graph"는 나오지 않는다. 내부 구조가 같은지는 미확인.
  - ⚠️ "never"는 절대 표현이고 측정이 없다. 위키가 사람 승인 없이 자동 갱신될 때 틀린 내용이 권위를 갖는 문제(10-17 Atlassian, [[context-engine]])도 다루지 않는다.

## 7. 샌드박스에서 자율 테스트 (11:48~12:59)

- 넷째 개선 — *"The last thing that you should do or this might be four out of five. The next thing that you should do is autonomous testing."*(11:48~11:52)
- ⭐ 왜: *"for UI changes, you might be able to read through a bunch of change files for React code and conclude that there's nothing wrong with the code, but in fact when you render it, it might be for instance hidden on an iPhone."*(11:54~12:07)
- **[제품]** *"we essentially build these dependency rich sandboxes which are completely configurable virtual machines"*(12:13~12:19) 고객 스택을 그 안에 띄우고 *"graviles[=Greptile's] agent uses computer use to test them end to end."*(12:26~12:28)
- ⚠️ *"For the first time I think endtoend QA is nearly solved."*(12:37~12:40) — 바로 앞에서 *"one of the more technically difficult problems"*(12:10~12:11)라 했고, 곧이어 조건 둘이 붙는다.
- **[조언] 조건 둘** — *"you have to document all the flows through your application."*(12:42~12:43) 그리고 *"a sufficiently simple build script"*(12:44~12:46). *"We have a team of forward deployed engineers that help companies do this."*(12:51~12:54) 사람을 붙여야 하는 일이라는 뜻이기도 하다.

→ [[agent-visual-qa]] · [[agent-sandboxing]]

## 8. 앱 흐름을 직접 테스트 (12:59~13:21)

- *"oh, this is the diagram I meant to show you"*(12:57~12:59) — 슬라이드를 넘기다 나온 말이다(강연 형식의 단서, 화면 미확인).
- 재료 셋: *"you'll need a dev box. You'll need PR branch and dependencies where you're running the app and you'll need some type of flow map"*(13:01~13:05) 결과 예: *"this button technically appears, but it actually is hidden on iPhones"*(13:13~13:15)

## 9. 모델을 나눠 비용 줄이기 (13:21~15:26)

- ⚠️ *"It can cost you anywhere from three bucks to 15 to 20 to do a single pull request review."*(13:22~13:28) (02장의 $3~25와 범위가 조금 다르고, 맥락과 테스트를 다 붙인 뒤의 값이라고 한다.)
- **프런티어와 작은 모델** — *"to me, Frontier models are still, generally speaking, more capable than open source models. This has been true for some time even though the rubber band is tightening."*(13:32~13:40)
- ⭐ **[수치]** ⚠️ *"our share today is about 20% frontier models for the most critical tasks."*(13:42~13:45) 나머지 *"long tail of tokens which is exploratory file reads and so on we use a variety of smaller models."*(13:46~13:50) 예시: 작은 모델은 맥락 찾기, 가벼운 computer use 모델은 사용자 흐름 시험, 프런티어는 버그 분석 · 리뷰 적용 · 제출(14:01~14:12). *"we have actually 20 different subtasks and each of them has a very specific set of models"*(14:12~14:17) 하고 작은 연구 팀이 계속 고친다(14:18~14:21). 직접 하면 *"You can probably get 70 to 80% of the way there"*(14:21~14:23).
  - ⚠️ 20%의 단위(토큰 · 비용 · 작업)가 발화되지 않는다. 절감 폭도 *"quite drastically"*(13:57)뿐이다. 슬라이드는 *"illustrative example"*(13:59)라고 본인이 밝힌다.
- ⭐ **다시 데이터셋** — 좋은 데이터셋이 없으면 *"you might be able to h trigger happily replace a lot of different sub aents[=agents] with smaller, faster models"*(14:34~14:40) *"you'll only find out when it misses something that then causes an outage or incident."*(14:43~14:46) 비용 절감의 안전장치를 §4의 데이터셋으로 되돌린다 → [[model-mixing-economics]]
- **컨텍스트 선별** — *"combat this problem of overactive file reads using a cheap model"*(14:52~14:54) 이론상: *"In theory, you should be able to use a decision model for this, something like JV or the decisions API to do effective ranking"*(14:59~15:05) 로드 여부를 판단하는 대상은 *"Frontier Model Cache, which is in some ways your most expensive and most scarce resource."*(15:08~15:11)
  - ⚠️ *"JV"* 는 [[jev|Jev]]로 읽었다(추정 — `en`은 `"Java"`(15:03), ko는 *"자바"*). *"decisions API"* 는 위키의 DevDay 2026 기록([[system-1-model]])과 이름이 같다. 발표자는 "in theory"라 하고, Greptile이 쓴다고 말하지 않는다.
- 맺음: *"If you do all of these things, you might be able to actually get quite far in building your own review agent. And if you do, please let me know."*(15:11~15:19) *"thank you so much."*(15:23)

> ⚠️ **번호가 맞지 않는다.** 발표자의 표시는 첫째(프롬프트) · *"the second improvement"*(05:19~05:20)(데이터셋) · *"The third improvement"*(08:23~08:26)(맥락) · *"four out of five"*(11:49)(테스트)다. 모델 뒤집기는 둘째와 셋째 사이에 번호 없이 들어가고 비용까지 세면 여섯 항목이다. 이 페이지의 "첫째~넷째"는 발표자 표시를 따른다.

## 등장 개체

- 인물: [[daksh-gupta]](신규, 설명란 근거) · [[laurie-voss]](위키 측 비교만) · [[tech-bridge]]
- 조직: [[greptile]](신규) · [[openai]] · [[anthropic]](모델 공급자로만, 조직 언급 없음)
- 제품 · 모델: [[claude-code]] · [[codex]] · [[jev]](ASR *"JV"*, 추정) · Firecracker · OpenCode · Pi · GitHub · GitLab · Jira · Linear · Confluence · Notion · Slack · React(언급 수준)
- 개념: [[review-model-inversion]](신규) · [[automated-code-review]] · [[cross-model-prior-intersection]] · [[review-loop-termination]] · [[production-trace-eval-flywheel]] · [[context-engine]] · [[agentic-search]] · [[agent-visual-qa]] · [[model-mixing-economics]] · [[agent-sandboxing]] · [[verification-bottleneck]] · [[intent-md]] · [[llm-wiki-pattern]] · [[system-1-model]]

## 이 위키에서의 좌표

- **리뷰 제품 회사 쪽의 첫 내부 진술.** Greptile은 10-02 Voss 편에서 표의 한 줄이었다. 10-13 [[tech-bridge-gitar-agentic-pr-validation]]과 같은 벤더 당사자 영상이지만, 이번에는 **자사 제품 대신 직접 만드는 절차**의 형식을 띤다.
- **평가 기준이 다르다.** Voss는 리뷰 제품들의 성공 지표가 *사람의 수락*이라고 정리했다([[automated-code-review]]). 이 발표자는 **사고를 낸 과거 PR을 얼마나 잡는가**를 제시하고 수락률은 말하지 않는다. Greptile이 실제로 무엇을 지표로 쓰는지는 이 영상만으로는 알 수 없다.
- **이질 모델 검증에 코드 리뷰 수치가 붙었다.** [[cross-model-prior-intersection]]은 데이터 파이프라인의 사례였다. 여기는 코드 리뷰에서 작성 · 리뷰 모델을 가른다. 수치의 질은 낮다(위 ⚠️).
- [[cross-lab-peer-review]]는 같은 "경쟁사가 채점한다" 어휘지만 **회사 단위 안전 검증**이라 이 영상과 다른 문제다. [[three-level-agent-review]] · [[risk-proportional-human-review]] · [[compressed-review-surface]]의 주제(위험 등급, 사람의 자리, 리뷰 표면)는 이 영상에서 다뤄지지 않는다.

## ⚠️ 유보

- 화자 이름 · 직함은 설명란 근거, 회사 이름은 설명란 · 태그 + 발화 ASR 변형. 행사 · 원본 링크 · 녹화일 없음. 첫 16초 뒤 문장 중간 시작.
- 시점 단서는 약하다: *"last year"*(GDP 대목, 연도 미상), *"new generation of GBT[=GPT] models and opus models"*(12:34~12:35)(버전 미발화), Decisions API 언급(위키 기록상 DevDay 2026 이후로 읽을 수 있으나 이름이 같다는 근거뿐이다). 정확한 녹화일은 미상.
- 수치 전부(1/1000, 3배, 10%, 80%, 80~90%, $3~25, 20%, 20개, 70~80%)는 발표자 진술이고 출처 · 표본이 없다. 위 두 곳은 발화 안에서 단위가 흔들린다.
- 설명란 링크 https://www.greptile.com/ 은 열어 보지 않았다.
- ASR: *"Reptile"* · *"Grapple"* · *"graviles"*(Greptile), *"cloud"*(Claude), *"Codeex"* · *"codecs"*(Codex), *"GBT"*(GPT), *"GP"*(grep), *"off"*(auth), *"cache rate"*(catch rate), *"poll request"* · *"P request"*(pull request), *"guidance"* · *"units"* · *"industry"*(agents, 추정), *"heristic"*, *"O code"*(auth code, 추정), *"JV"*(Jev, 추정). ko는 Greptile을 "파충류", firecracker를 "폭죽", agent를 "부동산 중개인", forward deployed engineers를 "엔지니어 4명"으로 옮겨 인용하지 않았다. en은 sandbox를 `"isolated environment"`, computer use를 `"computer vision"`, 뒤집기를 `"model versioning"`으로 바꾼다.

## References

- raw: `01.raw/articles/2026-11-03_AI 코드 리뷰 에이전트 직접 만들 때 놓치기 쉬운 것들.md`
- https://www.youtube.com/watch?v=6slamFlG96Q
- 설명란 관련 자료(⚠️ 열어 보지 않았다): https://www.greptile.com/
