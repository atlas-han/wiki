---
title: "Tech Bridge — 스킬 엔지니어링의 dark arts (Paul Bakaus · Impeccable 워크숍): 프롬프트는 입문, 스킬은 하네스 확장 — 아홉 기법"
type: source
tags: [agent-skills, harness-engineering, subagents, generator-evaluator, divergence, hooks, cross-harness, weakest-model, skill-evals, ablation, taste, ai-slop, impeccable, claude-code, codex, video]
source-url: https://www.youtube.com/watch?v=LXdWUZYzins
source-type: video
author: Tech Bridge (한영자막 재배포) · 워크숍 [[paul-bakaus]] ([[impeccable|Impeccable]] 제작자 — 자막은 "Paul"뿐, 성은 설명란) · 행사명·촬영 시점 미확정
date-published: 2026-09-27
ingested: 2026-09-28
created: 2026-09-28
updated: 2026-09-28
---

# Tech Bridge — 스킬 엔지니어링의 dark arts (Impeccable 워크숍)

[[tech-bridge|Tech Bridge]]가 재배포한 **1:04:24 워크숍**(발표 약 50분 + Q&A 약 14분, 공식 챕터 19개). 화자는 디자인 스킬 [[impeccable|Impeccable]]의 제작자 [[paul-bakaus|Paul Bakaus]] — 이 위키의 **두 번째 Bakaus 소스**다. 첫째인 [[tech-bridge-impeccable-design-steering]](09-11, 15:30)이 **무엇을 조향하는가**(형용사·동사 어휘, auto 거부)를 말했다면, 이 워크숍은 **그 스킬이 왜 스크립트 폴더로 가득한가** — 즉 *"a lot of people have looked at the code of Impeccable and they see like a whole bunch of scripts in the scripts folder and they're like, 'What is all this stuff?'"*(02:37~02:44)에 대한 답이다. 한 줄 테제:

> **프롬프트는 입문 단계이고 하네스 엔지니어링이 도달점이다. 스킬은 포장한 프롬프트가 아니라 MCP처럼 사용자의 하네스를 확장하는 것이다 — 서브에이전트·스크립트·훅·인앱 브라우저·하네스별 빌드를 써서, 모델이 산문 규칙을 건너뛸 수 없게 만든다.**

> *"prompting is sort of like the starter level, but harness engineering is where you should end up"* (06:23~06:28) · *"if the gate can be skipped it will be"* (48:19~48:23)

ASR·ko 보정: ko가 ***"you can't really tune pixels through a chat box"* 를 "채팅에서 픽셀 크기를 조정할 수 있습니다"로**(34:25~34:29), ***"you're out of luck"* 을 "이점을 누릴 수 있습니다"로**(13:08~13:09), ***"keep you in the right lane"* 을 "곤경에 빠뜨리는"으로**(32:26) 뒤집는다. **3주 전 새 버전을 낸 주체**(Anthropic)가 ko에서 **"저는"** 으로 바뀌었다(20:59). *"500 issues"* → **"다섯 가지"**(09:37), *LLM* → **"법학 석사(LLM)"**(10:19), *lowest common denominator* → **"최소공배수"**(47:08), *gate* → **"문"**, *ablation* → **"절제술"**, *Gemini* → **"쌍둥이자리"**, *hook* → **"갈고리·낚싯바늘"**, *taste* → **"맛"**, *skill* → **"기술"**, *poller* → **"극지방·여론조사원·닭"**. 전체는 raw의 보정 표.

> ⚠️ **당사자 진술, 독립 확인 없음.** 화자는 Impeccable 제작자이고 오픈소스(Apache 2, 49:37~49:40)다. **수치 근거는 하나도 없다** — *"works significantly better"*(28:26~28:27)·*"marginally better than random"*(58:07~58:09) 같은 관찰 진술뿐이고, 근거로 내세우는 **eval 하네스는 비공개**다(*"That one is not open source yet"* 53:17~53:20).
>
> ⚠️ **화자 이름.** 자막은 *"my name is Paul"*(00:52~00:55)뿐. **Bakaus**는 제목·설명란(X `pbakaus` · LinkedIn `paulbakaus` · `paulbakaus.com`)에서 온다. *"jQuery UI"* 제작자라는 설명란 주장은 자막이 확인한다(05:43~05:48).
>
> ⚠️ **행사·촬영 시점 미확정.** 형식은 워크숍(*"while it is a workshop"* 00:38, 샘플 저장소 `pbakaus/impeccable-talks`로 읽히는 ASR 11:14 — 열어 보지 않음). 연도·행사명 발화 없음. 상대 앵커: Anthropic front-end design 스킬의 새 버전이 *"three weeks ago"*(20:55~20:59), *"GPD55"*(=GPT-5.5 추정) 사용, 훅은 *"shipped quite recently"*(29:31~29:34), Codex 데스크톱 인앱 브라우저(35:04~35:12). 09-11 편과 **같은 행사인지 판정할 단서 없음.**
>
> ⚠️ **데모는 대부분 보이지 않는다.** 기법 1 라이브 데모는 서브에이전트 생성을 보여 주지 못했고(16:23~16:26), 기법 6은 화자가 *"fake demo"*(33:38)라 밝힌다. Q&A의 eval 하네스 화면은 서버를 꺼 버려 음성 설명으로 대체됐다(52:13~52:19).

## 출발점 — 금지 목록은 모델을 옆 클러스터로 옮길 뿐 (00:00~07:45)

- **Impeccable의 기원**: 1년간 만든 대규모 엔터프라이즈 앱에서 에이전트가 만든 화면을 **디자인 시스템으로 되돌리는 일**이 어려워 첫 스킬 `normalize`를 만들었다(01:14~01:46). Anthropic의 front-end design 스킬을 쓰다가 확장 → 오픈소스(01:47~02:21, `impeccable.style`).
- **"Claude 베이지"** — italic serif, 대문자 히어로, eyebrow 텍스트, 베이지 배경(03:28~03:45). *"slop is a moving target"*(03:58~04:00) — 보라색 그라데이션에서 *"cloud[=Claude] beige"* 로 옮겨 왔다(04:02~04:06). → [[ai-slop]]
- **"a system prompt and a prayer"**(04:13~04:15): front-end design 스킬은 *"no scripts no routing pure pros[e]"*(04:23~04:26). 문제 둘 — *"it overapplies and then a ban just relocates the model to the next cluster"*(05:03~05:08). Inter를 금지하면 *"it just uses the next best font it finds in [its] latent space"*(05:13~05:16).
- **jQuery UI의 교훈** — Tailwind의 기본 보라색이 보라 그라데이션을 낳았듯, 자기가 만든 jQuery UI의 첫 기본 테마가 주황이어서 웹이 주황이 됐다(05:31~05:51). *"The median is the model's gravity. Even 250 lines of like artis[an]al, crafted, beautiful skill pros[e] cannot change this."*(05:58~06:09)
- **테제**: 스킬을 *"the same way as MCP is an extension to the coding harness"*(06:34~06:36)로 생각하라 — *"it's not just a prompt that you package"*(06:40~06:43). *"Prompting is a spell[,] harnessing [is] magic."*(06:56~06:59) → [[harness-engineering]] · [[agent-skills]]

## 아홉 기법

| # | 화자의 이름 (07:09~07:43 예고) | 문제 | 기법 | 위키 페이지 |
|---|---|---|---|---|
| 1 | make it argue | 자기 작업을 자기가 리뷰하면 높게 매긴다 | 서로 못 보는 **두 서브에이전트** + 메인 스레드 종합 | [[generator-evaluator-pattern]] |
| 2 | force divergence | 금지는 클러스터 안에서만 옮긴다 | **anti-attractor** — 무작위 시드 | [[anti-attractor]] (신규) |
| 3 | routing like a model | 한 스킬에 다 넣으면 흐려진다 | 명령별 MD 로드 + brand/product **register** 전환 | [[agent-skills]] |
| 4 | give them memory | 스킬은 매번 0에서 시작 | 스킬 폴더·`.impeccable` 폴더에 산출물 저장 | [[agent-skills]] |
| 5 | scripts that talk back | 묻힌 규칙은 훑고 지나간다 | 스크립트 **stdout**으로 다음 행동 지시 | [[scripts-that-talk-back]] (신규) |
| 6 | hooks that fight back | 스킬 호출을 잊는다 | 편집마다 도는 디자인 린트 **훅** | [[hook-enforced-workflow]] |
| 7 | live wire the browser | 채팅으로 픽셀을 다듬을 수 없다 | 인앱 브라우저 + 폴러 + stdout | (이 페이지) |
| 8 | compile to every harness | "내 머신에선 됐는데" | 하네스·모델별 **빌드** | [[cross-harness-skill-compilation]] (신규) |
| 9 | design for the weakest model | 약한 모델은 규율을 잃는다 | Codex/GPT용 **gate**, 건너뛸 수 없게 | [[cross-harness-skill-compilation]] · [[hard-vs-soft-enforcement]] |

### 1. 논쟁시켜라 — 서로 못 보는 두 서브에이전트 (07:45~16:43)

*"if you ask codeex or claw code to review its own work, it will usually rate it as very high"*(08:02~08:08) — *"It's like grading your own homework"*(08:13~08:15), *"it anchors on what it already created"*(08:17~08:20).

Impeccable `critique`의 **두 실패 시나리오**가 핵심 관찰이다:

| 시나리오 | 무슨 일이 생기나 |
|---|---|
| **좋은 페이지 + 결정론적 오류 다수** | 같은 스킬·같은 모델 스레드에서 린터를 돌리면 모델이 출력을 보고 *"well I guess there's 500 issues therefore this design must be bad"*(09:37~09:42) |
| **끔찍한(혹은 빈) 페이지 + 검출 0** | *"we didn't find any issues so this must be great design"*(09:54~09:56) |

처방: *"It spawns two sub agents and they are blind to each other"*(10:08~10:11). ① **디자인 디렉터 역 LLM** — 위계·슬롭·휴리스틱을 브라우저 도구로 사람처럼 본다(10:19~10:35) ② **결정론적 디자인 린터**(대비·서체 수·가장자리 근접 등, 09:05~09:21) 실행 + 브라우저 증거 수집(10:35~10:40). *"the main thread synthesizes both into one critique"*(10:46~10:49). *"So two blind opinions beat one confident guess."*(12:12~12:15) 적용처: 코드 리뷰·보안 감사·계획/RFC 비평·출력 순위(12:17~12:32).

**Codex의 권한 모델** — *"In codeex, you have to explicitly as a user request the use of sub a[g]ents"*(12:56~13:02) → *"if you're distributing a skill, you're out of luck"*(13:07~13:10). 우회 두 줄: ① 서브에이전트 능력은 있는데 권한이 없으면 **멈추고 사용자에게 물어라**(13:13~13:24) ② *"if codeex realizes it can get away with something it will do it"*(13:59~14:03)이므로 *"if you cannot use sub agents you must say that you are giving the user a degraded experience and codeex hates that"*(14:16~14:23). → **벌칙 없는 지시는 건너뛴다** — 기법 9의 예고.

### 2. 발산을 강제하라 — anti-attractor (16:47~20:26)

*"a ban only moves the model around inside its own cluster"*(16:58~17:04). 대신 **무작위 시드** — 사용자 입력이나 스크립트에서 *"something that is completely unexpected to the model"*(17:14~17:23). 세 기법(쉬움 → 어려움): **상위 3개를 말하게 하고 버리기**(17:54~18:02, 한계: *"at some point you still get convergence"* 18:22~18:25) · **대량 생성 후 맥락 없는 서브에이전트가 순위**(radiant shaders 100개, 셀럽 시드 18:27~19:26) · **스크립트 시드**(`color.js`, 100개 넘는 손으로 고른 원색 19:36~19:51). 상세 → [[anti-attractor]]

### 3. 모델처럼 라우팅하라 (20:29~22:37)

*"If you cram every[thing] into one skill, it kind of blurs them. The instruction following becomes not very good enough anymore."*(20:31~20:38) 예: front-end design 스킬 구버전의 *"avoid system fonts"* 는 랜딩 페이지엔 맞지만 **제품 UI는 네이티브 느낌이 필요해 시스템 서체가 정답**이다(21:02~21:14). 거대한 if-else 블록은 *"convoluted wastes a lot of tokens and uh honestly doesn't work very well"*(21:27~21:30).

Impeccable은 여러 하위 스킬에서 출발해 지금은 **MoE처럼 내부 라우팅**한다(21:32~21:41, MoE는 비유): ① **명령별** — `critique`·`polish`마다 *"a different MD file loaded behind the scenes"*(21:43~21:50), *"not just one giant skill MD"*(21:52) ② **register별** — 브리프를 보고 *"brandy"*(랜딩 페이지)인지 실제 제품인지 판단해 *"switches registers and then loads completely different rules"*(22:00~22:19). 적용처: 큰 multi-tool 스킬·context-on-demand·청중별 행동·에이전트 툴킷(22:29~22:37).

### 4. 기억을 줘라 — 실행이 누적되게 (22:39~25:07)

*"Skills by default don't have long-term memory"*(22:41~22:43). 스킬 폴더에 저장할 수 있고, Claude에는 그 디렉터리를 가리키는 환경 변수가 있다 — *"no other harness supports this right now I believe"*(22:52~23:04). Impeccable은 **저장소 루트의 `.impeccable` 폴더**를 쓴다(23:07~23:11). `critique` 결과가 기본 git-ignore된 파일로 남고(23:22~23:29), 다른 세션의 `polish`가 **이전 비평들을 신호로** 읽어 페이지의 변천을 본다(23:32~23:48). 사용자가 비평에 반대하면(*"I really like my instrument fonts"*) 그것을 **선호로 기록해 이후 존중**한다(23:50~24:12). 화자는 이를 *"compound engineering"*(24:15)이라 부르고, 세션마다 **파일 하나씩** 리팩터링하며 맥락을 쌓는 자기 스킬을 예로 든다(24:36~25:06). → [[agent-memory]] · [[skill-self-improvement]]

### 5. 말을 되돌려주는 스크립트 (25:09~29:25)

*"buried rules get skimmed"*(25:12). 자기만 쓰는 스킬이면 모델을 알지만, 배포하면 Sonnet·Haiku·Grok·Gemini 사용자가 있다(25:42~25:58) — *"GPT5 mini is not a very good rule follower"*(26:18~26:21), Impeccable의 일부는 GPT-5 mini에서 동작하지 않는다(26:24~26:35). 처방: Impeccable은 *"really not just pros[e]. It is a combination of scripts that run in line within the skill"*(26:49~26:56). 매 호출에 `context.mjs`가 돌아 `product.md`·`design.md`를 모아 세션에 넣고, 없으면 **구조화된 JSON으로 "없다, 이렇게 하라"** 를 돌려주고, 새 버전이 있으면 **업데이트할지 사용자에게 물어라**고 지시한다(27:03~28:15). *"it will always tell the model the exact instructions on what to do next"*(28:17~28:22). 대가는 **프롬프트 캐싱**(28:57~29:23). 상세 → [[scripts-that-talk-back]]

### 6. 되받아치는 훅 (29:31~34:21)

하네스가 **명시하지 않으면 Impeccable 호출을 잊는다**(30:00~30:06). 그래서 스킬과 함께 **디자인 린트 훅**을 배포한다 — 설치 시 Claude Code·Cursor·Codex·GitHub Copilot에 들어가고(30:36~30:45) *"It's a guardrail that fires on every edit"*(30:52~30:55).

- **Pre 대 Post** — 훅 문법·동작이 하네스마다 다르다(31:02~31:08). *"slightly weaker models like composer and cursor"* 에는 **PreToolUse로 쓰기 자체를 막는** 훅이 필요했다 — *"a much more heavy-handed approach, but we needed to do that for certain models and certain har[ness]es"*(31:09~31:56). 기본 경험은 PostToolUse: 위반을 알리면 *"The model just course corrects and fixes itself"*(33:43~33:50).
- *"passive guardrails beat a command no one remembers to run"*(32:18~32:21).
- ⭐ **ignore 규칙이 필수** — *"oftentimes these hooks have false positives as well"*(34:01~34:06). Impeccable은 파일 단위부터 CSS 규칙 안까지 여러 수준의 ignore를 준다(34:13~34:21).

상세 → [[hook-enforced-workflow]]

### 7. 브라우저에 전선을 연결하라 — 라이브 모드 (34:25~39:52)

*"you can't really tune pixels through a chat box"*(34:28~34:30). 스킬을 하네스 엔지니어링으로 보면 질문은 *"what capabilities of that harness that you can exploit"*(34:52~34:57)이다. Codex 데스크톱의 **인앱 브라우저**(35:04~35:12)에 개발 서버 페이지를 띄우고, **MCP 없이**(*"it's not using MCP"* 35:47~35:50) 작은 **폴러** 서버가 페이지에 스니펫을 넣는다. 페이지의 조작이 SSE로 폴러에 가고, **폴러가 종료하며 stdout에 메시지를 남기면** 모델이 *"oh, something happened"* 하고 깨어난다(35:53~36:33) — 기법 5의 재사용. *"a direct connection between one harness capability and another harness capability"*(36:53~36:58). 데모: 요소 선택 → 하위 명령·변형 수 선택 → 세 변형 → accept/escape(37:29~38:40), 주석·드로잉·받아쓰기로 페이지 전체 조향(38:53~39:17). *"Tariq's blog post"*(HTML이 마크다운보다 좋은 소통 수단, 39:22~39:28 — [[thariq-shihipar]]인지 미확인)에 동의하며 **`design.md`도 HTML로 시각화**한다(39:31~39:39).

### 8. "내 머신에선 됐는데" — 하네스별 컴파일 (39:56~47:04)

*"hey bro just sim link just you know sim link .cloud[.claude]"*(40:15~40:18)은 자기용 스킬엔 좋지만 배포에는 아니다(40:35~40:39). *"Anthropic[] has still not adopted agents.md"*(40:51~40:54). 하네스 차이(서브에이전트 생성 주체 · ask-user 도구가 Codex에선 plan mode 한정 · 백그라운드 작업 완료 시 모델이 깨어나는지 · 감시자 throttle · 훅 문법)와 **모델별 과적합 tell**(Gemini의 이미지 hover 애니메이션, Codex의 나쁜 자간·과한 둥근 모서리·hairline border)을 보고 **하네스·모델별 빌드**를 만든다. *"every line of impeccable is ablation tested"*(45:00~45:04). 상세 → [[cross-harness-skill-compilation]]

### 9. 가장 약한 모델을 위해 설계하라 (47:06~48:40)

*"a weaker model has opinions just fine, but what it loses is the discipline to follow yours"*(47:10~47:14). Codex/GPT는 **"gate"라는 단어를 좋아한다** — 왜 지시를 안 따랐냐고 물으면 *"I think we need a gate"*(47:16~47:33). 그래서 **Codex·GPT에게만** 즉석 로드되는 Codex MD에 *"here are your eight gates you have to pass every single gate and you are not allowed to compress those gates"*(47:40~47:57), 각 gate의 결과를 남기게 한다(48:10~48:13, en-orig *"lock"* — *log* 로 읽힘, 미확정). *"if the gate can be skipped it will be"*(48:19~48:23) → *"make it unskippable"*(48:38~48:40). → [[hard-vs-soft-enforcement]]

맺음: *"We went from prompting all the way to building a monster"*(48:43~48:46), *"Nine things a prompt can't do"*(49:10~49:12), 설치 `npx impeccable skills install`(ASR *"MPX"*, 49:42~49:45).

## Q&A

- **캐싱**(50:50~51:34): 스크립트 결과는 *"a dynamic shell execution"* 이라 그 부분만 캐시되지 않는다. *"the skill will still be cached"*(51:17~51:21).
- **평가·반복 절차**(51:46~55:54) → [[skill-evals]]: 저장소의 E2E 테스트(LLM 기반 + Playwright, 52:57~53:07) · **비공개 eval 하네스** — Claude Code SDK 등으로 **관심 하네스(Claude Code·Codex·Gemini)의 조건과 도구를 재현**(52:27~53:40), 초기 인터뷰를 위한 **사용자 역 LLM**(53:43~54:06), **MoE 디자인 judge**(54:09~54:16), **20개 니치**(예: 이탈리안 레스토랑) × GPT-5.5·Opus·Sonnet × 릴리스마다 **5~10회**, 경쟁 스킬(front-end design)과 비교(54:20~54:48). 그리고 **줄 단위 ablation** — 규칙마다 고유 ID를 가진 XML 태그, 그 줄을 빼고 전 모델로 eval을 돌려 **결정론적 검출 엔진**으로 변화를 본다(54:50~55:44). *"it started you know vibes based uh and now it's really uh truly um well tested"*(55:48~55:54).
- **취향도 eval할 수 있나**(56:04~58:12) → [[taste-vs-judgment]]: *"I don't think taste can be solved at a model level"*(56:28~56:32), 취향은 희소하고(en-orig *"scars"*, ko·en *"희귀/rare"*) 모두가 쓰면 흔해진다(56:34~56:43). 모델은 *"particularly bad at evaluating taste"*(56:48~56:53) — 첫 뷰포트 judge에서 **Gemini는 더 채울수록 높게 매긴다**(57:18~57:33), *"the models are often maximalist"*(57:37). 그래서 **모델의 응답을 뒤집는 judge**를 만든다(57:41~57:49). 그의 도구는 *"marginally better than random"* — 1차 통과용, 이후 **사람의 눈으로 평가·주석**(58:02~58:12).
- **스킬의 미래**(58:20~1:00:08): Impeccable은 *"definitely outgrowing the skill platform"*(58:44~58:48) — 라이브 모드는 *"Jurassic Park experiment"*(58:55~59:01)이고 *"first party harness integration"* 이 낫겠다(59:10~59:13). **hot take**: *"most skills should probably be written by the individual users"*(59:25~59:29), 배포하는 사람은 **더 투자해야** 한다(59:29~59:36) — *"skills that are distributed that uh do not work well in a model that the author didn't use"*(59:41~59:49). *"I would rather see less skills in the ecosystem that are really battle tested and proven"*(59:57~1:00:04), 지금은 *"wide west"*(1:00:07~1:00:08). 청중이 **스킬을 테스트하는 공통 방법이 없다**를 기회로 짚자(1:00:24~1:00:28) 자기 도구·설치기/컴파일러를 따로 공개할 수 있겠다고 답한다(1:00:30~1:00:53).
- **MCP 서버의 스킬**(1:01:05~1:01:53): 아직 안 써 봤다. *"I worry greatly about context pollution"*(1:01:22~1:01:26), MCP를 잘 안 쓰는 이유(1:01:33~1:01:38). 질문 일부는 en-orig에 캡션이 없다.
- **패키징·배포**(1:02:14~1:04:06) → [[cross-harness-skill-compilation]]: Codex 플러그인 마켓플레이스·Claude Code 마켓플레이스가 있지만 *"the claude code one for sure doesn't work particularly well"*(1:02:38~1:02:40) — 업데이트가 안 되고 캐싱 문제(1:02:42~1:02:50). skills.sh·npx skills는 하네스별 컴파일을 허용하지 않아 PR을 냈고 *"Andrew"* 와 논의 중(1:03:13~1:03:29). *"there's definitely no no industry standard for distribution yet"*(1:03:46~1:03:47) — 그래서 **자체 CLI 설치기**를 유지한다(1:03:50~1:04:02).

## 기존 위키와의 대조

### 합치하는 것

- **자기 평가 편향** — [[generator-evaluator-pattern]]의 *"Separating the agent doing the work from the agent judging it"*. 이 워크숍은 한 걸음 더 간다: 평가자를 **LLM 판정자와 결정론적 검출기 둘로** 나누고, **둘이 서로를 못 보게** 한다. 이유는 편향이 아니라 **앵커링** — 같은 스레드에서 린터 출력이 LLM 판단을 끌고 간다(09:27~09:56). [[skill-evals]]의 *눈가림*(평가 사실을 숨김)과는 다른 눈가림이다(**다른 평가자의 결과**를 숨김).
- **슬롭은 움직이는 표적** — [[ai-slop]]의 09-11 기록과 같은 말을 이번엔 **처방의 근거**로 쓴다: 고정 금지 목록은 옆 클러스터로 옮길 뿐이므로 → 무작위 시드. [[ai-slop]]이 *"고정된 슬롭 목록은 낡는다"* 로 정리한 것을 **제작자가 직접** 확인한다.
- **훅은 선택지를 없앤다** — [[hook-enforced-workflow]]([[graft]] 편)와 같은 구조(스킬 + 훅 동봉). 새로 더해지는 것: **Pre/Post 선택이 모델 강도에 달렸다**, **ignore 규칙**, **하네스별 훅 문법**.
- **progressive disclosure의 실패** — [[tech-bridge-sdd-full-course]]의 *"judgment isn't always perfect"* 에 대해 SDD 강좌는 *"name it"* 을, 이 워크숍은 **훅**을 처방한다.
- **MCP 재고** — [[tech-bridge-sdd-full-course]]의 MCP → CLI+skills 흐름과 같은 방향. 화자는 **컨텍스트 오염**을 이유로 MCP를 잘 안 쓴다고 말한다(1:01:22~1:01:38).

### 갈리는 것

> ⚠️ **Contradiction: 스킬은 누가 써야 하나.** [[agent-skills]]의 09-10 절(Gopal: *"아무도 남을 위해 스킬을 쓰지 않는다"* · Greze: *"공유 스킬을 누구나 더 좋게"*)과 09-23 절(벤더가 100+ 외부 스킬을 권함)에 **세 번째 입장**이 더해진다 — **스킬 배포자** 자신이 *"most skills should probably be written by the individual users"*, 배포한다면 여러 모델에서 검증하라(59:25~1:00:04). 이 위키가 09-23·09-27에 표시한 *외부 스킬의 검토·버전 고정* 문제에 **"더 적고, 전투 검증된 스킬"** 로 답하지만, 검증 방법(자기 eval 하네스)은 비공개다.

> ⚠️ **Contradiction: AGENTS.md와 심링크.** [[tech-bridge-sdd-full-course]]는 AGENTS.md를 에이전트 독립의 **표준** 중 하나로 두었다. 이 워크숍은 *"Anthropic[] has still not adopted agents.md"*(40:51~40:54)라며 **심링크로는 배포 가능한 스킬을 만들 수 없다**고 본다 — 규칙 파일이 아니라 **하네스 동작**(서브에이전트 권한·ask-user·백그라운드 작업)이 다르기 때문이다. 두 소스는 층이 다르다(규칙 파일 대 실행 동작).

- **자동화 거부와의 관계** — 09-11 편의 *"auto는 없다"* 와 이 워크숍의 **스크립트·훅·gate로 모델을 강제**하는 설계는 모순이 아니다: 사람의 **결정**은 남기고(라이브 모드의 accept/escape, 비평 반대를 선호로 기록), 모델의 **규율**은 강제한다. ⚠️ 위키의 정리.
- **"Codex/GPT는 벌칙 없는 지시를 건너뛴다"** — [[agentic-misbehavior]]·[[reward-hacking]] 계열의 관찰이 **스킬 작성 층**에서 나온 것이다. 화자의 처방은 벌칙 문구(*"degraded experience"*)와 gate 로그다. 모델별 행동 차이의 근거는 비공개 eval이다.

## 해소하지 않고 표시만 한 것

- **행사명·촬영 시점** — 발화 없음. 09-11 편과 같은 행사인지 모름.
- **"GPD55"**(25:34, 54:28) — GPT-5.5로 읽지만 en-orig ASR. ko는 한 번은 "GPT-5", 한 번은 "GPT-5.5".
- **"Tariq"**(39:22) · **"Ben from Contra"**(56:19~56:22) · **"Andrew"**(1:03:19) — 성·소속 미발화. Tariq가 [[thariq-shihipar]]인지, Andrew가 누구인지 확인하지 않았다. Microsoft의 배포 프로젝트는 화자도 이름을 잊었다(1:03:38~1:03:44).
- **"Ten watch"**(43:37) — 무엇인지 모름.
- **"lock every single result"**(48:10~48:13) — *log* 로 읽히나 미확정.
- **"55 lines of named bands"**(04:20~04:23) — 무엇의 55줄인지 불명확.
- **radiant shaders**(18:35) — 09-11 편의 *"radian shaders"* 와 같은 라이브러리로 보이나 두 번 다 ASR.
- **Claude의 스킬 디렉터리 환경 변수**(22:52~23:00) — 변수 이름을 말하지 않았다. *"no other harness supports this right now I believe"* 는 화자의 믿음.
- **모든 효과 주장** — 수치 없음. eval 하네스 비공개. *"works significantly better"*(stdout 지시)의 측정 방법 미공개.
- **훅 동봉의 보안 표면** — 스킬 설치가 **네 하네스에 훅을 설치**한다(30:36~30:45). 설치된 훅이 매 편집마다 코드를 실행하는데, 신뢰·검토·업데이트 경로는 논의되지 않는다(Claude Code 마켓플레이스의 업데이트 실패 1:02:42~1:02:50만 언급). [[prompt-injection]] · [[tech-bridge-sdd-full-course]]의 *"plugins can execute code"* 경고와 같은 자리.
- **설명란의 "사후 점검 대신 원천 차단"** — 자막보다 세다(Pre 훅은 약한 모델·특정 하네스용).

## 등장 개체

- 인물: [[paul-bakaus]] · "Tariq"(→ [[thariq-shihipar]]?, 미확인) · "Ben from Contra" · "Andrew"(npx skills) (페이지 없음)
- 조직: [[anthropic]] · [[openai]] · Microsoft · Tailwind
- 제품·도구: [[impeccable]](`normalize` · `critique` · `polish` · live mode · `context.mjs` · `color.js` · design hooks · 자체 CLI 설치기/컴파일러) · [[claude-code]](서브에이전트 · AskUserQuestion · 백그라운드 작업 · 훅 · 마켓플레이스 · SDK) · [[codex]](서브에이전트 권한 · plan mode 한정 ask-user · 인앱 브라우저 · 플러그인 마켓플레이스) · [[cursor]](Composer) · GitHub Copilot · Gemini · GPT-5.5 · GPT-5 mini · Opus · Sonnet · Haiku · Grok · Anthropic front-end design 스킬 · jQuery UI · skills.sh / npx skills · Playwright · radiant shaders
- 개념: [[anti-attractor]](신규) · [[scripts-that-talk-back]](신규) · [[cross-harness-skill-compilation]](신규) · [[agent-skills]] · [[harness-engineering]] · [[generator-evaluator-pattern]] · [[skill-evals]] · [[hook-enforced-workflow]] · [[hard-vs-soft-enforcement]] · [[ai-slop]] · [[taste-vs-judgment]] · [[agent-memory]] · [[model-context-protocol]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=LXdWUZYzins> (1:04:24, `upload_date` 2026-09-27)
- raw: `01.raw/articles/2026-09-27_스킬 엔지니어링의 숨겨진 비기(Dark Arts)를 소개합니다 — Paul Bakaus (Impeccable).md`
- 설명란 링크: <https://x.com/pbakaus> · <https://linkedin.com/in/paulbakaus> · <https://www.paulbakaus.com/> (⚠️ 이 위키는 열어 보지 않았다)
- 같은 화자: [[tech-bridge-impeccable-design-steering]](09-11) · 같은 주제: [[tech-bridge-sdd-full-course]] · [[tech-bridge-graft-code-knowledge-graph]] · [[tech-bridge-lauren-tan-trusting-agents]]
- [[tech-bridge]] · [[paul-bakaus]] · [[impeccable]]
