---
title: "Tech Bridge — 하네스 엔지니어링: 코딩 에이전트로 소프트웨어 팩토리 만들기 (Dru Knox · Tessl): inner·outer·meta 루프와 세 레이어"
type: source
tags: [harness-engineering, software-factory, inner-outer-meta-loop, control-plane, agent-readiness, skills-registry, autonomy-vs-automation, tessl, vendor-claim, video]
source-url: https://www.youtube.com/watch?v=sAu_4QuAI0w
source-type: video
author: Tech Bridge (한영자막 재배포) · 발표 [[dru-knox]] ([[tessl|Tessl]] head of product and design — 발화 "Drew Knox", 철자 Dru는 설명란) · 행사명 미발화(설명란 ai.engineer 링크 → AI Engineer 계열 추정) · 녹화일 미발화
date-published: 2026-10-10
ingested: 2026-10-11
created: 2026-10-11
updated: 2026-10-11
---

# Tech Bridge — 하네스 엔지니어링: 코딩 에이전트로 소프트웨어 팩토리 만들기 (Dru Knox · Tessl)

[[tech-bridge|Tech Bridge]]가 재배포한 **19:53 단독 발표, Q&A 없음, 공식 챕터 16개.** 화자는 [[tessl|Tessl]]의 head of product and design [[dru-knox|Dru Knox]] — *"My name is Drew Knox. I'm the head of product and design at Tessle. Tessle is an agent enablement platform."*(00:00~00:08). 이름 철자 Dru와 회사 철자 Tessl은 설명란 링크에서 왔다. 이 위키에서 Tessl은 지금까지 **설명란 링크와 도구 목록 속 이름**으로만 나왔고([[tech-bridge-sdd-enterprise-lessons]] · [[tech-bridge-anthropic-dreaming-memory]]), **Tessl 사람이 직접 말하는 첫 소스**다. 테제:

> **소프트웨어 팩토리는 사용자에게 내보내는 최종 산출물 전부를 에이전트가 만들고 엔지니어는 그 팩토리를 짓는 시스템이다. 거기로 가는 길이 하네스 엔지니어링 — 팩토리를 자동화하고 품질을 올리는 루프(inner·outer·meta)를 짓는 일 — 이고, 순서는 autonomy → automation, 품질은 유지하다가 마지막에 올린다. 팩토리의 진짜 보상은 속도가 아니라 품질이다.**

> *"a software factory is any agentic system where all of the end product of what you're building and shipping to users is created by agents and your software engineering teams effectively focus on building the factory."* (02:11~02:27) · *"You are building the loops that automate and improve the quality of your factory."* (06:26~06:35) · *"ultimately we think you can raise quality once you have a factory."* (04:22~04:29) · *"I promise it's worse than you think."* (13:10~13:12)

이 위키에 개념 하나가 생긴다 → [[inner-outer-meta-loops]] (신규 제안). 그리고 [[software-factory]]에 **세 번째 벤더 정의**, [[harness-engineering]]에 *"하네스 엔지니어링 = 팩토리의 루프를 짓는 일"* 이라는 **조직 단위 정의**가 붙는다.

ASR·ko 보정: ko는 핵심어 셋을 모두 흔든다 — **harness engineering**("배선 엔지니어링"·**"환경공학"** 4회, 08:52엔 없는 화자 표지 *"프랑코:"* 까지 창작), **PR**("추출 요청"·"홍보"·"보도자료"·"홍보 담당자들"), **Tessl**("테슬라" 5회). 그리고 의미를 뒤집은 자리: *high autonomy but low automation* → **"점차 나아졌다 … 신뢰하지 않기 때문에 자동화를 사용"**(03:34~03:39), *the idea of a backlog kind of goes away* → **"귀걸이가 거의 보이지 않아요"**(05:09~05:10), *every week* (스윕 빈도) → **"몇 주 걸린다"**(14:27~14:30), *workflows* → **"현금 흐름"**(10:53, 13:35), *improvement loops* → **"생리 주기"**(17:34), *Can be long running* → **"사형 집행일 수도"**(19:00), *human PR comments* → **"사람의 댓글 … 홍보 담당자들"**(19:29~19:33). en-orig 판독: *"metal loop"* → meta loop, *"Tesla/Tessle/TESL"* → Tessl, *"codeex cloud code gemini"* → Codex · Claude Code · Gemini(`en`·ko 공유 오류 *"Cloud Code"*), *"linear"* → Linear. 전체 목록은 raw.

> ⚠️ **당사자 진술 — 화자는 Tessl의 제품 책임자이고 후반 4분(15:09~19:24)은 자사 제품이다.** 화자 스스로 앞부분을 *"everything I've said before here are just techniques. You could go do them all yourself if you wanted."*(15:15~15:19)로 분리한다. 이 위키도 **①~⑤절(기법)과 ⑥절(Tessl 제품)을 분리해서** 기록한다. 기법 쪽도 측정 근거는 없다 — 화자의 경험·권고다.
>
> ⚠️ **en-orig 공백 01:49~02:11.** *"They're mostly techniques. Tesla,"*(01:47~01:51) 다음이 02:11이다(약 22초 무자막). `en`·ko에는 *"Tessl이 제공하지만 우리 전용은 아니다 … 1부, 소프트웨어 팩토리. 무엇인가? 엄격한 정의는 없다. 용어가 얼마나 빨리 바뀌는지 모두 나만큼 답답할 것"* 이 있다 — **en-orig로 확인할 수 없어 인용하지 않는다.**
>
> ⚠️ **행사·시점.** 행사명·도시·연도 미발화. 설명란 `https://ai.engineer`·AI Engineer 유튜브/X/LinkedIn 링크 → **AI Engineer 계열 추정**(확정 아님). 앞선 Tessl 연관 두 편은 설명란이 *tessl.co*(AI DevCon으로 보임)였는데 이 편은 ai.engineer다 — **같은 행사인지 알 수 없다.** 시점 단서는 *"started to be called loop engineering over the last couple weeks"*(06:09~06:13)뿐(상대 시점). 업로드 2026-10-10.

## 1. 전제 — 누구를 위한 발표인가 (00:30~01:49)

- *"this is a bit of an advanced talk in the sense that like if you aren't already using coding agents what I'm about to walk through is probably not where you want to get started."*(00:33~00:43)
- 적정 지점: 동시에 세션 두어 개를 굴리고, 쉬운·중간 난이도 과제에서 에이전트가 *"frequently do the right thing"*(00:45~01:02) — *"you're sort of at the sweet spot for starting to think about harness engineering"*(01:02~01:07).
- 대부분은 *"work with any stack. They're mostly techniques."*(01:45~01:49)

→ [[agent-trust-curve]](병렬 세션이 신뢰의 함수라는 Lauren Tan의 곡선 — Knox는 그 곡선의 *중간쯤* 을 출발점으로 잡는다)

## 2. 소프트웨어 팩토리 — 정의와 세 기둥 (02:11~04:20)

**정의**: 최종 산출물 전부를 에이전트가 만들고, 엔지니어링 팀은 팩토리를 더 autonomous·automated하게, 산출 품질을 높이게 만든다(02:11~02:34). ⭐ *"everyone on your team effectively becomes internal tool builders and then you're building a system that produces your product."*(02:38~02:45) — [[factory-engineering|Zach Lloyd의 "building the thing that builds the product"]]와 같은 문장.

**세 기둥 — 순서가 있다**(02:47~04:20):

| 기둥 | 정의 (en-orig) | 측정 |
|---|---|---|
| **Autonomy** | *"how much human intervention do you need to get to the right answer. So how many times you need to correct the code or provide a nudge"*(03:00~03:09) | 사람의 수정·넛지 횟수 |
| **Automation** | *"how much can you let them run, right? How much do you need to review or build trust in the solution before you accept it?"*(03:21~03:27) | 리뷰·수동 검증의 양 |
| **Quality** | *"how good is the product that you're actually producing for your users?"*(03:58~04:01) | *"your usual user analytics, your uh test quality, your test coverage"*(04:03~04:08) |

- ⭐ **autonomy ≠ automation**: *"You can have high autonomy in the sense that agents frequently are oneshotting the problems you're giving them, but low automation because you don't trust it yet. And so you're reviewing all of the code directly."*(03:30~03:43) — *"You have to build up autonomy first before you can move to automation."*(03:47~03:52)
- 경로: *"improving autonomy, then improving automation, all while keeping quality constant."*(04:11~04:20)
- ⚠️ 화자가 슬라이드 순서와 말을 한 번 뒤바꿨다가 정정했다(03:11~03:16). 정의는 정정 전후 같다.

→ [[software-factory]] · [[agent-trust-curve]] · [[assistance-vs-automation]](다른 축의 "automation"이다 — 아래 "갈리는 것")

## 3. 진짜 보상은 품질이다 (04:20~06:01)

- ⭐ *"I think most folks look at factories as a way to ship faster. They'll say like, "Oh yeah, you'll get a little bit of slop, but my god, you'll you'll launch so much more features (…)" I think that's a very shortterm phenomenon"*(04:29~04:49)
- 논거: *"every team has backlogs of bug fixes or improvements that they wish they could be making (…) With a software factory, the idea of a backlog kind of goes away. And so, you actually just have much more capacity to work on test quality improvements, architectural refactors."*(04:54~05:18)
- 전환기: *"at first as you transition, you will want to keep quality constant or maybe like a very small dip, but that the ultimate payoff is you should see better quality"*(05:19~05:30) — ⚠️ *"at Tesla[=Tessl], we believe"* — 신념 진술, 데이터 없음.
- 협업: *"it's much easier for people who aren't in technical roles to contribute ideas"*(05:38~05:44), 엔지니어링은 *"building the underlying system that everyone is using to push features out"*(05:50~05:54) → *"a more dynamic and inclusive uh development experience"*(05:56~06:01).

→ [[ai-slop]] · [[codebase-gardening]] · [[verification-bottleneck]]

## 4. 하네스 엔지니어링 = 루프를 짓는 일 · inner / outer / meta (06:04~08:47)

- ⭐ *"Harness engineering uh as a sign of how fast terms evolve. It's also started to be called loop engineering over the last couple weeks."*(06:06~06:13) — [[roland-gavrilescu|Gavrilescu]]의 *RLHF → 하네스 → 루프* 계보([[loop-is-the-product]])와 같은 이동을 **이름의 변화**로 증언한다.
- 정의: *"I mentioned the software factory is building your product. You are building the loops that automate and improve the quality of your factory."*(06:24~06:35)

| 루프 | 언제 | 성격 | 끌어올리는 기둥 | 예 (en-orig) |
|---|---|---|---|---|
| **inner** | 에이전트가 PR을 올리기 *전* | *"very fast iterative loops. You want them to be cheap. You're expecting the agent to run them all the time."*(06:55~07:00) | **autonomy** — *"Improvements here will drive better autonomy"*(07:00~07:05) | (구체 예 미발화) |
| **outer** | PR이 올라간 *뒤* | *"more expensive exhaustive checks that don't make sense to run over and over again (…) but they do encode things that otherwise a human would have to verify to build confidence in the system"*(07:15~07:30) | **automation**(사람 리뷰 시간을 대신) | *"agentic QA"*, *"run mutation testing to check the quality of our test suite"*(07:36~07:45) |
| **meta** | 개발 프로세스 *바깥* | *"It observes your coding agent logs. It looks at PRs, your issue tracker, user feedback."*(08:01~08:10) — 사용자에게 새어 나간 실수, 사람이 막아야 했던 실수를 찾는다 | **quality** — *"This is where you'll drive quality"*(07:53~07:59) | *"it feeds back into the inner and the outer loop to make sure that that mistake is not made again."*(08:18~08:26) |

- meta loop가 **진척의 레버**: *"once you have the infrastructure for each of these loops, (…) the metal[=meta] loop is where you're going to be actually driving from a certain percentage of like how AI native am I? You're going to be driving it up by investing in your metal loop."*(08:27~08:44) ⚠️ "AI native 퍼센트"는 정의·측정 없음.

→ [[inner-outer-meta-loops]] (신규) · [[harness-engineering]] · [[structure-sensitive-tests]](mutation testing) · [[agent-visual-qa]](agentic QA) · [[skill-self-improvement]] · [[self-harness]]

## 5. 왜 어려운가 — 사람의 심리 세 가지 (08:47~11:00)

*"raw unassisted harness engineering is hard for a few specific reasons that basically come down to human psychology."*(08:56~09:04)

1. **지식이 매주 바뀐다** — *"you basically become an AI researcher just to try and keep up"*(09:16~09:20), 모범 사례가 다음 주에 낡고 *"at some point they become antiatterns[=anti-patterns]"*(09:23~09:31). 화자는 이건 *"hopefully (…) will go away over time"*(09:07)이라 본다.
2. ⭐ **계획되지 않은 일이라 출시와 경쟁한다**(화자: *"more durable"*) — *"harness engineering is fundamentally unplanned work. (…) You either don't do it and you get stuck in the local maxima of the agent never improves or you do it and you miss your deadline for the feature and you get in trouble and so no one ever does it."*(09:56~10:30)
3. **신호가 숨어 있다** — *"it's hidden away in local coding agent logs or it is on someone's machine somewhere. It's in someone's head."*(10:42~10:50) → 작업을 *"surfaces where everything is saved and publicly available for later optimization loops"*(10:55~11:00)로 옮겨야 한다.

→ [[agent-org-adoption]] · [[company-brain]] · [[human-plumbing]]

## 6. 지어야 할 세 레이어 (11:03~15:07)

*"These aren't by any means standard terms, though if you want to help me make them so, I would be forever grateful."*(11:10~11:19) — **화자의 coinage.** 순서대로 해야 한다(11:19~11:25).

### 레이어 1 — Control plane: 모든 접점을 legible하게 (11:19~12:38)

- Tessl의 사내 흐름(⚠️ 자사 서술): *"all work starts as an issue on the issue tracker. It gets sent to a headless agent running in a sandbox. The agent puts up a PR and then engineers engage with comments on the PR. So it still has manual correction. It still has manual interface but now all of your touch points with the agent are legible."*(11:40~12:03)
- 흔한 세 요소(12:08~12:38): ① 이슈 추적 → 에이전트 작업 착수 ② 리뷰 — *"GitHub PR review is probably like the easiest"* ③ 워크플로·플레이북의 표준화·배포 — *"something like a skills registry or a shared GitHub repo where you push skills that improve agent quality"*(12:29~12:38)

→ [[cloud-agent-delegation]] · [[agent-skills]] · [[automated-code-review]]

### 레이어 2 — "agent it" (챕터명: 에이전트 레디 인프라) (12:39~14:08)

- *"a massive grabag that I call agent it"*(12:39~12:45) — ⚠️ 명칭 판독 불가(raw 참조). 로컬 설정이 많은 프로젝트를 남에게 넘길 때 *"you realize with horror all of the dependencies that you thought were cleanly isolated and are not"*(12:49~12:55) — 에이전트에게도 같은 일이 일어난다.
- ⭐ *"I I promise it's worse than you think. Like there's no one who has come in thinking like, yeah, yeah, yeah, it's not going to be that hard for us has left saying that at the end."*(13:10~13:19)
- 항목: CLI·API 접근, 제품을 클릭해 볼 방법(13:01~13:09) · *"writing down in your company brain how you get work done, what are your workflows"*(13:32~13:40) · 내부 서비스 접근 → 거버넌스·API 접근 문제(13:40~13:45) · 프로덕션 로그 → *"what's your compliance stance"*(13:47~13:54) · 코드 실행 환경(13:56~13:59). *"the most unplannable"* — 권고는 *"spend a week, spend two weeks and just get it done"*(13:23~13:30).

→ [[agent-readiness]](Factory의 코드베이스 위생 점검과 겹치되 축이 다르다 — 아래) · [[company-brain]]

### 레이어 3 — Improvement loops: 시간 대부분이 여기 간다 (14:11~15:07)

*"this is where you'll end up spending most of your time"*(14:11~14:14) — meta loop의 부품들(14:18~14:23):

- **repo 유지보수** — *"things that sweep your codebase every day, every night, every week"*(14:24~14:32)
- **플레이북** — *"how to add a feature to your CLI"*(14:32~14:38)
- **반복 작업 발굴·자동화** — *"ideally as quickly and easily as possible because otherwise people won't do it"*(14:38~14:47)
- **출력 품질 점검 → 학습 반영** — *"oh, I saw the agent made this mistake. Let's update a skill on add like the playbook you have for adding features to the CLI. Let's update that so it doesn't make this mistake again in the future."*(14:54~15:07)

→ [[scheduled-agent-automations]] · [[skill-self-improvement]] · [[codebase-gardening]]

## 7. Tessl 제품 (15:09~19:24) — ⚠️ 당사자 진술

- **포지셔닝**(15:27~16:30): *"a bunch of small lifts rather than one massive snake eating the moose all at once"* · *"batteries included"* — harness engineering 모범 사례를 대신 따라간다(지식 격차 = 어려움 1에 대한 답) · *"modular and open. So we don't think every component of a factory is going to be best-in-class with a single company"*(15:58~16:05) · 점진적이라 *"six months later like, oh wow, we're like 40% there to a software factory. We never had to stop. and delay shipping"*(16:21~16:28) — ⚠️ 가상의 고객 반응, 측정 아님(어려움 2에 대한 답).
- **Control plane**(16:31~17:21): 스킬 레지스트리 — *"publish and version the workflows and the automations (…) with built-in governance things like security reviews, quality reviews, controls for who can publish and update what"*(16:35~16:50) · 이슈 트래커 → GitHub 커넥터, *"Right now we're focused on linear[=Linear] to GitHub"*(16:52~16:56) · 에이전트 코드 리뷰 도구. 레지스트리 스캔 화면의 *"how much it actually improves the agent's output"*(17:18~17:21) — ⚠️ 수치는 자막에 없다.
- **Tessl Agent**(17:25~18:34): ⚠️ 재생된 영상은 자막에 없다. 발화된 기능: PR·이슈를 *mine* 해 반복 작업을 찾는다 — *"every week you do a hunt for flaky tests. Why don't we just set that up as a skill for the workflow and then we'll put it in automation on a GitHub action."*(17:55~18:05) · 기성 유지보수 작업(아키텍처 품질·코드 중복·테스트 스위트·보안 취약점 주간 스캔, *"oneclick install"* 18:14~18:32).
- **tessl launch**(18:34~19:10): *"take a sk a skill that codifies a workflow. You can then pick a particular coding agent that you want to handle it. Tesla[=Tessl] agent can be one of them but for most coding tasks you probably want to use something like codeex cloud code gemini[=Codex, Claude Code, Gemini]."*(18:41~18:56) — 권한이 맞춰진 샌드박스, 장시간 실행, GitHub 토큰으로 PR·코멘트 응답(18:56~19:08). 자사 에이전트를 코딩 기본값으로 밀지 않는 점이 특이하다.
- 요약 루프: *"find an improvement, take a workflow, turn it into a skill, ship it to everyone, and then get your improvement loops going."*(19:15~19:26)

→ [[tessl]] · [[codex]] · [[claude-code]] · [[agent-skills]] · [[scheduled-agent-automations]]

## 8. 추적할 지표 (19:26~19:50)

| 방향 | 지표 (en-orig) | 기둥 |
|---|---|---|
| ↓ | *"manual takeovers"*(19:30~19:32) | autonomy |
| ↓ | *"human PR comments"*(19:32~19:34) | autonomy·automation |
| ↑ | *"more PRs initiated without human input. That's a sign that you're automating more."*(19:40~19:46) | automation |
| 유지 → ↑ | *"first hold quality constant and then aim to drive it up after that."*(19:46~19:50) | quality |

⚠️ 위키의 주석: 첫 셋은 **사람의 개입을 세는** 지표다 — 줄이는 방법에는 *에이전트가 나아지는 것* 과 *사람이 덜 보는 것* 둘 다 있다. 화자가 품질을 넷째 조건으로 묶어 둔 것이 그 구멍을 막는 장치인데, 품질 측정은 §2의 *"usual user analytics, test quality, test coverage"* 이상으로 구체화되지 않는다. → [[trusted-throughput]](Goodhart 경고) · [[agent-roi-measurement]]

## 이 위키와의 연결

### 이어지는 것

- **[[software-factory]] — 세 번째 벤더 정의.** Factory(Tížková)는 *신호 수집부터 학습까지의 생애주기 루프*, Warp(Lloyd)는 *SDLC를 짓는 일*, **Tessl(Knox)은 *최종 산출물 전부를 에이전트가 만든다* 는 산출물 기준 + autonomy → automation → quality의 순서.** 세 화자 모두 팩토리 인프라를 판다.
- **[[factory-engineering]]** — *"everyone on your team effectively becomes internal tool builders"*(02:38~02:43)는 Lloyd의 *"building the thing that builds the product"* 와 같은 직무 정의. Knox는 그 일의 이름을 **harness engineering**으로 부른다 — 이 위키에서 *factory engineering* 과 *harness engineering* 이 같은 일을 가리키게 되는 첫 소스.
- **[[harness-engineering]] — "every mistake becomes a rule"의 조직판.** meta loop의 *"make sure that mistake is not made again"*(08:21~08:26)과 레이어 3의 *"Let's update a skill"*(14:56~15:05). 실수의 목적지가 **AGENTS.md가 아니라 스킬·플레이북**이라는 점에서 [[joel-quenneville|Quenneville]]·[[simon-martinelli|Martinelli]] 쪽에 선다(네 번째 소스).
- **[[loop-is-the-product]]** — Gavrilescu의 두 번째 루프(첫 루프의 산출물을 보고 무엇을 바꿀지 정한다)는 Knox의 **meta loop**와 같은 자리다. *"loop engineering"* 이라는 이름도 Knox가 증언한다.
- **[[agent-readiness]]** — Factory의 점검은 *코드베이스 위생*(테스트·린터·문서), Knox의 레이어 2는 *접근·권한·실행 환경*(CLI·API·내부 서비스·프로덕션 로그·company brain). 같은 "준비" 문제의 두 면.
- **[[agent-skills]]** — 스킬 레지스트리 + 거버넌스(보안·품질 리뷰, 게시 권한)를 control plane의 셋째 요소로. [[tech-bridge-ai-native-skills]]의 registry 논의와 같은 방향.
- **[[scheduled-agent-automations]]** — 매일·매주 repo 스윕, 주간 기성 스캔, flaky test 사냥을 GitHub Action으로.

### 갈리는 것

> ⚠️ **Contradiction: 팩토리는 품질을 올리는가.** Knox: *"ultimately we think you can raise quality once you have a factory"*(04:22~04:29), 속도는 *"a very shortterm phenomenon"*. [[kent-beck|Kent Beck]]([[tech-bridge-kent-beck-craft-augmented-development]]): 다크 팩토리는 *"always goes off the rails"*, 산출물은 *"complete crap"*. 다만 Knox의 팩토리는 **사람 코멘트·수동 인수를 지표로 남겨 두는** 구조라 Beck이 겨눈 *"no human (…) no feedback"* 이 아니다. 둘 다 측정은 없다. [[matt-pocock|Pocock]]([[tech-bridge-pocock-pr-bottleneck]])은 품질을 **브레이크**(느리게 하는 장치)에서 찾고, Knox는 **백로그가 사라져 생긴 여력**에서 찾는다 — 품질의 원천이 다르다.

> ⚠️ **용어 충돌: "outer loop".** [[lauren-tan|Lauren Tan]]([[tech-bridge-lauren-tan-2000-prs]] · [[tech-bridge-lauren-tan-pocock-podcast-full]])의 outer loop는 **Slack·Sentry 같은 외부 신호를 구독해 일을 시작하는 루프**(GrokBot)다. Knox의 outer loop는 **PR이 올라간 뒤의 비싼 검사**이고, 외부 신호(로그·이슈·사용자 피드백)를 보는 것은 **meta loop**다. 같은 단어가 다른 칸을 가리킨다. [[in-context-learning]]의 inner/outer loop(Karpathy: activation vs SGD)는 또 다른 층위다. → [[inner-outer-meta-loops]]

> ⚠️ **"automation"의 두 뜻.** [[assistance-vs-automation]](Almeida)의 automation은 *사람을 루프에서 없애는 목적함수*, Knox의 automation은 *리뷰 없이 맡길 수 있는 정도(신뢰)* 다. 방향은 같지만 Knox는 autonomy(정답률)와 분리해 **신뢰의 축**으로 정의한다 — [[agent-trust-curve]]에 더 가깝다.

## 해소하지 않고 표시만 한 것

- en-orig 공백 01:49~02:11의 실제 발화(`en`·ko만 있음).
- *"agent it"*(12:41~12:45)의 정체 — 챕터명 "에이전트 레디 인프라"는 업로더 해석.
- inner loop의 구체 예 — 발화되지 않는다(outer·meta만 예가 있다).
- Tessl Agent 영상 내용, 레지스트리 스캔의 개선 수치, *"40% there"*·*"how AI native am I"* 의 측정 방법.
- 행사명·도시·녹화일. 설명란이 ai.engineer인데 앞선 Tessl 연관 편들은 tessl.co(AI DevCon으로 보임) — 관계 미확정.

## 등장 개체

- 인물: [[dru-knox]] (신규 제안)
- 조직: [[tessl|Tessl]] (신규 제안) · [[ai-engineer|AI Engineer]](⚠️ 설명란 링크만 — 추정)
- 제품·도구: [[codex]] · [[claude-code]] · Gemini(페이지 없음) · Linear(페이지 없음) · GitHub·GitHub Actions(페이지 없음) · Tessl skills registry · Tessl Agent · `tessl launch`
- 개념: [[inner-outer-meta-loops]] (신규 제안) · [[software-factory]] · [[harness-engineering]] · [[factory-engineering]] · [[agent-trust-curve]] · [[agent-readiness]] · [[company-brain]] · [[agent-skills]] · [[scheduled-agent-automations]] · [[skill-self-improvement]] · [[self-harness]] · [[loop-is-the-product]] · [[structure-sensitive-tests]] · [[agent-visual-qa]] · [[cloud-agent-delegation]] · [[automated-code-review]] · [[codebase-gardening]] · [[verification-bottleneck]] · [[ai-slop]] · [[trusted-throughput]] · [[agent-roi-measurement]] · [[assistance-vs-automation]] · [[agent-org-adoption]] · [[human-plumbing]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=sAu_4QuAI0w> (19:53, `upload_date` 2026-10-10)
- raw: `01.raw/articles/2026-10-10_하네스 엔지니어링 - 코딩 에이전트로 '소프트웨어 팩토리'를 만드는 방법.md`
- 설명란 링크: <https://tessl.io> · <https://x.com/tessl_io> · <https://www.linkedin.com/in/dru-knox-6b57b830/> · <https://x.com/drufball> · <https://github.com/drufball> · <https://ai.engineer> (⚠️ 열어 보지 않았다)
- 팩토리 정의 비교: [[tech-bridge-factory-software-factory]] · [[tech-bridge-warp-factory-engineering]] · 반론: [[tech-bridge-kent-beck-craft-augmented-development]] · 브레이크: [[tech-bridge-pocock-pr-bottleneck]]
- 하네스·루프: [[tech-bridge-harness-engineering]] · [[tech-bridge-introspection-loop-is-the-product]] · [[tech-bridge-rails-harness-engineering]]
- Tessl 이름이 나온 앞선 소스: [[tech-bridge-sdd-enterprise-lessons]] · [[tech-bridge-anthropic-dreaming-memory]]
- [[tech-bridge]] · [[tessl]] · [[dru-knox]]
