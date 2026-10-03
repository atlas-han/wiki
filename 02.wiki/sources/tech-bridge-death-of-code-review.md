---
title: "Tech Bridge — 코드 리뷰의 종말: 데이터가 보여주는 진짜 현실 (Laurie Voss · Arize AI): 741% vs 30%, 테스트 통과 ≠ 머지 가능, 리뷰는 시스템으로 재건된다"
type: source
tags: [code-review, verification-bottleneck, mergeability, automated-code-review, human-on-the-loop, prompt-injection, benchmarks, swe-bench, frontiercode, metr, bun, arize-ai, secondhand-claims, video]
source-url: https://www.youtube.com/watch?v=-TeOEuplMrQ
source-type: video
author: Tech Bridge (한영자막 재배포) · 발표 [[laurie-voss]] ([[arize-ai|Arize AI]] — 자막엔 "Lori"·"Arise AI", 성·도메인은 설명란) · AI Engineer 계열 행사, 2026년 6월 이후 녹화(회차 미확정)
date-published: 2026-10-02
ingested: 2026-10-03
created: 2026-10-03
updated: 2026-10-03
---

# Tech Bridge — 코드 리뷰의 종말: 데이터가 보여주는 진짜 현실 (Laurie Voss · Arize AI)

[[tech-bridge|Tech Bridge]]가 재배포한 **24:11 발표, Q&A 없음, 공식 챕터 21개.** 화자는 [[arize-ai|Arize AI]]의 DevRel 책임자이자 npm Inc. 공동 창업자 [[laurie-voss|Laurie Voss]]. **산업 현황 서베이**다 — 화자 자신의 실험은 없고, 연구·벤더 발표·사례를 줄 세워 *"사람 리뷰를 뺄 수 있는가"* 를 따진다. 이 위키의 [[verification-bottleneck]]에 **처음으로 정량 근거 묶음**(741% vs 30%, Cisco 400줄, METR 절반, FrontierCode 88 vs 29)이 들어왔고, 그 위에 두 개념이 생겼다 → [[mergeability-gap]] (신규) · [[automated-code-review]] (신규).

> **코드 생성은 싸졌고 신뢰는 여전히 비싸다. 더 열심히 리뷰하는 것은 산수상 불가능하고, 리뷰를 빼 본 곳들은 모두 리뷰를 지운 게 아니라 사람이 지은 시스템으로 옮겼다. 테스트 통과는 머지 가능을 뜻하지 않으며, 그 간극을 기계가 채점할 수 있게 되는 순간 그것이 다음 모델의 학습 신호가 된다. 사람은 코드를 줄 단위로 읽는 엔진에서, 리뷰 시스템을 설계하는 조종사로 올라간다 — "stop reviewing PRs", 리뷰 하네스를 지어라.**

> *"Producing code is suddenly a whole lot cheaper. Knowing whether to trust it is still very expensive"* (02:06~02:10) · *"The bet there is that loop design substitutes for inspection"* (06:07~06:10) · *"They didn't delete review, they moved it."* (17:21~17:23) · *"the teams that win the next few years won't be the ones that generate the most code. They'll be the ones who can say with evidence why they trust what they shipped."* (23:03~23:10)

ASR·ko 보정: ko가 OpenAI의 *internal product* 를 **"국내총생산"으로**(05:07), *a million lines of code* 를 **"백만 명에 가까운 돈"으로**(05:16), *Anthropic's code reviewer* 를 **"인류는 확신할 수 있다"로**(20:48), *you can't skip … production* 을 **"제작 과정을 건너뛰세요"로 뒤집고**(21:51), Copilot 리뷰 *60 million* 을 **"60개"로**(11:03), *mergeability* 를 **"용량 … 합병"으로**(09:15~09:17 — `en`도 *"fusion capability"*, 공유 오류), pull request를 일관되게 **"추출 요청"으로** 옮겼다. en-orig는 화자를 *"Lori"*, 회사를 *"Arise AI"*, METR을 *"Meter"*, Greptile을 *"Grapile"*, Dex Horthy를 *"Dexter Horthy"* 로 들었다. 전체 목록은 raw. **인용은 en-orig에서만** 했다.

> ⚠️ **거의 모든 수치가 화자의 2차 인용이다.** 경제학자 3인의 연구(이름 없음), Cisco 연구(*"two decades ago"*), Stripe(Anthropic의 Fable 출시 자료), Bun(분석자 없음), OpenAI 2월 글(제목 없음), METR, Cognition FrontierCode, Sarah Guo의 글, CriticGPT, GitHub·Cursor·CodeRabbit 벤더 수치, 베이징대 연구, 3월 프롬프트 인젝션 연구(이름 없음). **이 위키는 원 자료를 하나도 열어 보지 않았다.** 화자가 스스로 계산한 두 곳은 맞지 않는다 — *"51 points less"*(08:33~08:35)는 88−29 = **59**, *"three orders of magnitude"*(16:46)는 13,044/74 ≈ **176배**.
>
> ⚠️ **행사·시점.** 행사명 미발화. *"Swix decided it would be funny for those two to be backtoback"*(00:10~00:15) — **같은 제목 세션이 바로 앞에 있었다**(그 세션은 이 위키에 없다). *"AIE last year"*(18:38), *"this conference"*(22:16) → AI Engineer 계열. 언급된 사건이 *"February / March this year"*, FrontierCode *"launched it in June"*(07:58~08:00), *"2026"*(23:23) → **2026년 6월 이후 녹화.** 업로드는 2026-10-02.

## 1. 문제 — 741% vs 30% (00:00~03:09)

- *"the speed at which humans can review code has stayed exactly the same"*(00:47~00:51) → *"a new bottleneck"*.
- ⭐ 경제학자 3인이 GitHub 개발자 10만+ 명을 AI 사용 시점 텔레메트리와 맞춰 봤다: 자율 에이전트를 켠 개발자는 *"wrote 741% more code but only 30% more software shipped"*(01:35~01:41). 저자들은 *"blunt that review was the bottleneck"*(01:52~01:54). ⚠️ 논문 미특정.
- 생성은 더 이상 병목이 아니다: Stripe 5천만 줄 Ruby 코드베이스를 하루에(팀 추정 2개월+, Anthropic Fable 출시 자료 — 02:30~02:43), [[bun|Bun]](*"now part of Anthropic"*) Zig → Rust 100만 줄+ 6일(02:44~02:51).
- 그리고 모두의 일상: *"we're just sort of hitting the merge button and feeling guilty about the fact that we haven't read these code diffs"*(02:57~03:02).

→ [[verification-bottleneck]] · [[trusted-throughput]]

## 2. "더 열심히 리뷰"는 산수상 안 된다 (03:09~04:36)

Cisco 연구(*"two decades ago"*, 10개월, 리뷰 2,500건, 320만 줄): 한 번에 **400줄**을 넘기면 결함 발견이 떨어지고, 시간당 **450줄**을 넘기면 *"falls off a cliff"*(03:42~03:57). → 1만 줄 에이전트 PR 하나 = *"three or four working days"*(03:59~04:05), 그리고 개발자는 에이전트 열두 개를 동시에 돌린다(04:18~04:21). 리뷰 전담은 지루하고 사람이 *"burn out really fast"*(03:22~03:26). → [[minimizing-reader-load]]

## 3. 리뷰를 빼는 쪽 — 루프 설계가 검사를 대신할 수 있나 (04:36~06:29)

- [[openclaw|OpenClaw]] 제작자 Peter Steinberger: 에이전트에게 프롬프트하지 말고 *"designing the loops that prompt your agents"*(04:44~04:48). [[andrej-karpathy|Karpathy]]도 *"the human in the loop is holding the system back"*(04:54~04:59) 취지. ⚠️ 두 사람 모두 화자의 요약.
- ⭐ **[[openai|OpenAI]] 2월 글** — 빈 저장소에서 *"no manually written code"*, 5개월 뒤 약 100만 줄·머지된 PR 약 1,500개·엔지니어 3명(05:05~05:25). *"humans may review pull requests but they are not required to. (…) we've pushed almost all review effort towards being handled agent to agent"*(05:31~05:41).
- 화자의 의심: *"they did not tell us what the product did and (…) did not release an open source product (…) which suggests to me that there are still holes in that strategy"*(05:43~05:55).
- 요점: *"whether you can build a loop that is good enough uh to review all of your code for you depends entirely on what the loop can see"*(06:10~06:17).

→ [[harness-engineering]] · [[loop-is-the-product]]. ⚠️ 글 저자 미발화 — [[ryan-lopopolo]]의 2026년 2월 Codex 자율화 글과 같은 글인지 **확인하지 않았다.**

## 4. 테스트 통과 ≠ 머지 가능 (06:29~10:53) → [[mergeability-gap]] (신규)

- **METR**(3월): SWE-bench 대상 프로젝트의 현역 관리자 4명에게 **SWE-bench 채점기를 통과한 PR**을 보여 줬더니 *"only good enough to merge about half of the time"*(07:07~07:11). 실패는 정확성이 아니라 *"code quality and (…) changes that quietly broke other code, things external to the test suite"*(07:17~07:23). 에이전트에게 피드백 반복 기회가 없었다는 단서 — 화자는 *"that's just putting a human in the loop"*(07:42~07:45)라 무관하다고 본다.
- ⭐ **FrontierCode**([[cognition|Cognition]], 6월): 관리자 20명+가 자기 저장소에서 만든 과제 150개(각 40시간+), 채점 항목 *"behavioral correctness, regression, safety, scope, discipline, test quality, and maintainability"* — *"a human review rubric uh made machine checkable"*(08:08~08:16). [[fable-5-1|Fable 5]]는 *"88% on Sweetbench Pro, but only 29% on the hardest slice"*(08:24~08:30), GPT 5.5는 *"under 6%"*(08:48). ⚠️ 29%는 **최난도 구간**이다(챕터·설명란은 생략).
- ⭐ **Sarah Guo** — 진짜 머지 가능성 벤치마크를 푸는 것이 코딩 모델의 전환점. 모델이 코드에서 빨랐던 이유: *"a compiler is a free verifier. A test suite is a free verifier and anything that you can verify cheaply you can train against until you beat it"*(09:31~09:41) — [[tech-bridge-signal-layer]]의 [[lena-hall|Lena Hall]]이 인용한 그 문장. 그래서 *"whoever writes today's review standard is writing next year's default model behavior"*(10:07~10:09).
- **선례 CriticGPT**(2024): 모델이 쓴 코드의 버그를 잡는 모델, 사람+모델이 각자 단독보다 낫고 그 신호가 학습에 들어갔다(10:16~10:36 — ⚠️ *"almost instantly"* 는 화자 평가).

→ [[verifiable-goals]] · [[reward-hacking]] · [[syntactically-correct-behaviorally-wrong]]

## 5. 지금 돌고 있는 자동 리뷰 (10:53~14:47) → [[automated-code-review]] (신규)

| 누구 | 무엇 (화자 진술) | en-orig |
|---|---|---|
| GitHub Copilot 리뷰어 | 리뷰 6천만 건, GitHub 전체 코드 리뷰의 *"more than one in five"* | 11:02~11:10 |
| [[cursor\|Cursor]] 1세대 | diff마다 **8패스**, 리뷰어 순서를 **셔플**(순서가 결과를 바꿔서) — 목적은 **오탐 걸러내기** | 11:32~11:57 |
| 베이징대 연구 | 여러 패스를 돌려 **합의한 것만** 남기면 리뷰 품질 *"up to 44%"* | 12:05~12:18 |
| Cursor 재구축 | 모델이 diff를 추론·도구 호출·어디를 팔지 결정. ⭐ *"they had to tell the model to be more suspicious of the code"* | 12:26~12:58 |
| Cursor 다음 | 리뷰어가 **수정 에이전트**를 띄워 패치를 돌려줌, 다음은 **코드를 실행해 버그 보고를 증명** | 13:06~13:33 |
| CodeRabbit | 전용 리뷰어 최대, PR 1,300만+ | 13:43~13:47 |
| Greptile | 저장소 전체 그래프 → 먼 코드에 닿는 변경을 본다 | 13:48~13:56 |
| Graphite | 자기 제안의 **수락/거절**로 eval 세트 | 13:56~14:03 |

⭐ 공통점: *"all of them are using the same metric as their definition of success which is is a human accepting my answer"*(14:06~14:14) — Cursor는 이를 **resolution rate**라 부르고 52% → 70%+로 올렸다(14:15~14:22). *"That is a preview of what the models are going to do except these companies have already shipped it"*(14:31~14:36). 현 상태: 생성도 자동, 리뷰도 자동, **사람은 리뷰를 리뷰한다**(14:38~14:45).

## 6. 사람을 아예 빼 본 두 사례 (14:47~17:17)

- **Nicholas Carlini**(Anthropic, 2월): 에이전트 16개가 Rust로 C 컴파일러를 처음부터, Linux 커널 컴파일, 약 2,000 세션, *"no human in the loop"* — 그러나 ⭐ *"there was absolutely a human on the loop"*(15:15~15:17): 리뷰·검사 시스템, 테스트 하네스, 피드백 시스템은 사람이 썼다. Carlini 본인의 경고 — *"it is easy to watch the tests pass and assume that the job is done uh and that it rarely is"*(15:37~15:45). → [[test-harness-vs-test-authoring]]
- **[[bun|Bun]] Zig → Rust**: 약 100만 줄, 6일, 게이트는 기존 테스트 스위트 99.8% 통과(15:52~16:04). 여담 — Zig 코드를 전부 지운 PR을 *"another robot"* 이 *"this is AI slop"* 으로 플래그(16:09~16:22). ⭐ 그러나 포팅된 코드에 **unsafe 블록 13,044개**, 비슷한 크기의 사람 Rust 코드는 약 74개(16:32~16:46). *"the test suite can certify behavior at the public interface. um it cannot certify 13,000 assertions that the test suite was never designed to look for"*(16:55~17:04).

> ⚠️ **Contradiction: Bun 포팅의 규모·기간.** 이 위키의 [[bun]] 페이지(← [[anthropic-dynamic-workflows]])는 **Rust 약 75만 줄, 첫 커밋 → 머지 11일**이다. Voss는 *"over a million lines of Zigg uh to Rust in six days"*(02:46~02:51), *"about a million lines of code by agents in six days"*(15:52~15:56). 줄 수는 Zig 원본 기준일 수 있고 6일은 에이전트 작업 기간, 11일은 머지까지일 수 있다 — **미확정.** 99.8%는 양쪽이 같다.

## 7. OpenAI는 리뷰를 옮겼다 · Dex Horthy의 철회 (17:17~19:42)

- [[codex|Codex]]가 자기 변경을 리뷰하고, 더 많은 에이전트를 불러 그 리뷰를 리뷰하며 *"in a loop until every agent reviewer is satisfied"*(17:23~17:34). 변경마다 Codex를 **부팅 가능**하게 해 UI를 직접 보고, 로깅 스택 전체를 에이전트에 노출(17:34~17:48). 실패 시 처방은 *"almost never to try harder"*(17:51~17:56 — Cisco 결론과 같은 말). 한동안 *"every Friday cleaning up AI slop uh by hand"* → 나중엔 슬롭 청소 에이전트(18:01~18:17). ⭐ *"review didn't disappear (…) it got rebuilt as a system and that system is built by humans"*(18:17~18:25). → [[ai-slop]]
- **Dex Horthy**: 6개월간 코드를 리뷰하지 말라고 말했고(*"at AIE last year"*), 3월 무대에서 철회 — *"I was wrong. Please please read the code. We tried not reading the code for like six months. It did not end well. We had to rip out and replace large parts of that system."*(18:46~18:56). *"That is not a benchmark"*(18:56~18:58). ⚠️ 이어지는 *"OpenAI is running uh lived with the results um and reversed in public"*(19:06~19:12)은 문맥상 Horthy에 대한 말 — **OpenAI가 번복했다고 읽지 않는다**(raw 보정 목록).
- **테스트가 못 보는 맥락**(Sarah Guo): 이 모듈엔 외부 사용자 셋이 있다, *"there's this cron job that nobody will admit to writing that relies on that module existing"*(19:29~19:34).

## 8. 사람이 남는 자리, 그리고 리뷰어의 리뷰 (19:42~21:51)

⭐ 사람 체크포인트는 움직이지만 **예측 가능한 곳에서 살아남는다**(19:42~20:08): ① *"where correctness isn't cheaply checkable"* ② *"where uh the blast radius is large"* — 보안 민감 환경은 즉답이 *"no"* ③ *"wherever someone has to put their name on the result"*. 사람의 역할은 *"moving up the stack (…) from inspecting the code directly to designing and tuning the systems that inspect the code and designing the definition of good"*(20:10~20:22). → [[risk-proportional-human-review]] · [[named-human-accountability]]

**누가 리뷰어를 리뷰하나** — 답은 사람(20:23~20:32):

- [[anthropic|Anthropic]]의 자동 보안 리뷰어 README: *"this action is not hardened against prompt injection attacks uh and should only be re used to review trusted PRs"*(20:39~20:47) → *"can be talked out of its findings by the very thing that it is reviewing"*(20:47~20:51).
- ⭐ 3월 연구: 무해한 커밋 메시지로 포장한 취약 코드가 *"fooled an autonomous review agent in 88% of attempts"*, 사람 리뷰어는 35%(20:59~21:12). *"you don't just lose a reviewer, you lose the thing that was hard to fool"*(21:15~21:19). 그리고 *"confidently framed bad code is exactly the kind of code that agents are very good at producing"*(21:24~21:28). → [[prompt-injection]]
- 채점기를 채점할 합의도 없다 — *"benchmark scaffolds have been caught leaking answers"*(21:41~21:44).

## 9. 마지막 리뷰어는 프로덕션 · 결론 (21:51~24:11)

- *"once the premerge review is all machines, watching what the code actually does becomes the last reviewer standing"*(21:55~22:00). 출시 후에는 테스트 결과가 아니라 **궤적**(*"what the system actually did step by step uh when it ran against the real world"* 22:08~22:13)이 중요하다. 화자는 Arize 홍보는 하지 않겠다고 한다(22:13~22:16). → [[production-trace-eval-flywheel]]
- ⭐ *"code review isn't completely dead, but it is changing an enormous amount. uh it is being rebuilt as an engineered system. Humans are moving from being the engine that drives a code review uh reading code line by line uh to its pilots."*(22:35~22:50)
- *"Every layer of that system, the benchmark, the classifier, the rubric, the test suite, the eval is itself unreed[=unreviewed] until somebody decides that that is their job"*(22:52~23:03).
- ⭐ **처방**: *"stop reviewing PRs. Um, it is the wrong level of abstraction for 2026."*(23:19~23:25) → *"pour your precious time into building uh a reliable review harness. Codify your definitions of good, your company context, your domain knowledge"*(23:31~23:43), 리뷰어·규칙·eval의 위층에 노력을 모으라(23:47~23:52).

## 이 위키와의 연결

### 이어지는 것

- **[[verification-bottleneck]]** — 09-12의 두 소스(마우스파워 *"천 개의 PR에 치여 죽고 있다"*, Lauren Tan *"여러분이 병목"*)가 진단만 했던 것에 **처음으로 측정치**(741% vs 30%, Cisco 400줄)가 붙었다. 처방은 *"작업을 고른다 / 역량을 짓는다 / 일을 쪼갠다"* 에 이은 **네 번째 답 — 리뷰 자체를 시스템으로 재건한다.**
- **[[tech-bridge-signal-layer]]** · [[lena-hall]] — *"컴파일러는 무료 채점 도구"* 를 같은 Sarah Guo에게서 인용한다. Lena Hall은 이를 **코드 자동화가 먼저 온 이유**로, Voss는 **다음에 올 것(머지 가능성 벤치마크 → 학습 신호)** 의 근거로 쓴다.
- **[[agent-trust-curve]] · [[hard-vs-soft-enforcement]]** (Lauren Tan) — 사람 리뷰(스타일 가이드)를 최하위 층으로 내리고 강제를 CI로 옮긴다는 것과 같은 방향. Voss의 *"stop reviewing PRs"* 는 그 끝점.
- **[[test-harness-vs-test-authoring]]** — Carlini 사례의 *human on the loop* 는 *"무엇을 검증할지는 사람이, 장치는 에이전트가"* 의 실례. 다만 Voss는 Carlini의 하네스를 **사람이 썼다**고 강조한다.
- **[[code-knowledge-graph]]** — Greptile의 저장소 그래프는 *먼 코드에 닿는 변경* 이라는 METR의 실패 유형(*"quietly broke other code"*)을 겨냥한 같은 발상.
- **[[generator-evaluator-pattern]]** — Cursor의 *"suspicious by default"* 는 평가자를 생성자와 다르게 프롬프트해야 한다는 같은 결론.

### 갈리는 것

> ⚠️ **Contradiction: 사람 리뷰를 빼도 되는가.** [[tech-bridge-lauren-tan-trusting-agents]]의 신뢰 곡선 오른쪽 끝은 **자동 병합 + main에서 사후 리뷰**, OpenAI 2월 글은 *"humans (…) are not required to"*. Voss는 OpenAI 사례를 *"there are still holes"* 로 유보하고 Dex Horthy의 철회를 근거로 든다 — 그러나 그의 처방도 *"stop reviewing PRs"* 다. **갈리는 지점은 사람을 빼느냐가 아니라 사람을 어디에 두느냐**다: PR(아래) vs 리뷰 시스템·정의(위). Voss는 *"please read the code"* 를 인용하면서도 PR 읽기를 그만두라고 한다 — **두 주장을 화해시키는 말은 없다**(⚠️ 위키의 독해: Horthy의 철회는 *아무도 보지 않음*에 대한 것, Voss의 처방은 *보는 층의 이동*).

> ⚠️ **Contradiction: Bun 포팅 수치** — §6 참조, [[bun]] 페이지와 줄 수·기간이 다르다.

> ⚠️ **사람 수락률을 성공 지표로 쓰는 문제.** [[trusted-throughput]]의 Goodhart 경고와 같은 자리 — 자동 리뷰어가 *사람이 받아들이는 것* 을 최적화하면, 88% vs 35% 연구가 보여 주듯 *사람도 속는* 방향은 측정되지 않는다. Voss는 이 긴장을 지적하지 않는다(위키의 표시).

## 해소하지 않고 표시만 한 것

- **모든 수치의 원 출처** — 경제학자 3인 연구, Cisco, Stripe, Bun unsafe 분석자, OpenAI 2월 글, METR, FrontierCode, Sarah Guo 글, CriticGPT, 베이징대, 3월 프롬프트 인젝션 연구(*"reinforced"* 가 이름인지 동사인지 미확정), 벤치마크 답 유출.
- **화자 산수** — *"51 points"*(실제 59), *"three orders of magnitude"*(실제 약 176배), *"nearly eight times"*(741% 증가 = 약 8.4배).
- **"Fable 5 before it got pulled and then unpulled"**(08:20~08:24) — 어떤 사건인지 이 위키에 1차 기록 없음.
- **Dex Horthy** 표기(챕터 *"덱스 호시"*, en-orig *"Dexter Horthy"*)와 소속 — 미발화.
- **바로 앞 세션**(같은 제목) — 이 위키에 없음.

## 등장 개체

- 인물: [[laurie-voss]] (신규) · [[andrej-karpathy]] · Peter Steinberger([[openclaw]] 제작자, 페이지 없음) · Sarah Guo(투자자, 페이지 없음) · Nicholas Carlini(Anthropic, 페이지 없음) · Dex Horthy(페이지 없음) · swyx(⚠️ 판독 추정, 페이지 없음)
- 조직: [[arize-ai]] (신규) · [[openai]] · [[anthropic]] · [[cognition]] · [[cursor]] · METR(페이지 없음) · Cisco · Stripe · GitHub · CodeRabbit · Greptile · Graphite · 베이징대(Peking University) · npm Inc.
- 제품·모델·벤치마크: [[codex]] · [[bun]] · [[fable-5-1|Fable 5]] · GPT 5.5 · GitHub Copilot 리뷰어 · CriticGPT · SWE-bench / SWE-bench Pro · FrontierCode · [[devin]](*"Devon"*)
- 개념: [[mergeability-gap]] (신규) · [[automated-code-review]] (신규) · [[verification-bottleneck]] · [[risk-proportional-human-review]] · [[named-human-accountability]] · [[prompt-injection]] · [[ai-slop]] · [[harness-engineering]] · [[test-harness-vs-test-authoring]] · [[production-trace-eval-flywheel]] · [[verifiable-goals]] · [[trusted-throughput]] · [[agent-trust-curve]] · [[code-knowledge-graph]] · [[generator-evaluator-pattern]] · [[minimizing-reader-load]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=-TeOEuplMrQ> (24:11, `upload_date` 2026-10-02)
- raw: `01.raw/articles/2026-10-02_코드 리뷰의 종말 - 데이터가 보여주는 진짜 현실입니다.md`
- 설명란 링크: <https://x.com/seldo> · <https://github.com/seldo> · <https://arize.com> (⚠️ 열어 보지 않았다)
- 같은 주제: [[tech-bridge-mousepower-measuring-agents]] · [[tech-bridge-lauren-tan-trusting-agents]] · [[tech-bridge-lauren-tan-2000-prs]] · [[tech-bridge-signal-layer]] · [[tech-bridge-lopopolo-agent-harness]] · [[anthropic-dynamic-workflows]]
- [[tech-bridge]] · [[laurie-voss]] · [[arize-ai]]
