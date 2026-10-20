---
title: "Tech Bridge — 컨텍스트 엔지니어링: AI 에이전트가 피해야 할 네 가지 실패 유형 (Martin Keen, IBM Technology): context rot, 유한한 attention budget, poisoning·distraction·confusion·clash와 validate·compact·curate·prune"
type: source
tags: [context-engineering, context-rot, context-window, attention-budget, context-poisoning, context-distraction, context-confusion, context-clash, validation, compaction, offloading, tool-curation, tool-sprawl, pruning, agent-memory, long-running-agents, ibm, explainer, video]
source-url: https://www.youtube.com/watch?v=E8zCcv2HcbI
source-type: video
author: Tech Bridge (한영자막 재배포) · 제작 [[ibm|IBM Technology]](설명란 기준) · 화자 [[martin-keen|Martin Keen]](⚠️ 설명란 본문에만, 자막에는 이름 없음)
date-published: 2026-10-19
ingested: 2026-10-20
created: 2026-10-20
updated: 2026-10-20
---

# Tech Bridge — 컨텍스트 엔지니어링: AI 에이전트가 피해야 할 네 가지 실패 유형 (Martin Keen, IBM Technology)

[[tech-bridge|Tech Bridge]]가 한영자막을 입힌 **10:11 1인 해설이고, 공식 챕터는 10개다.** 원어는 영어이고 ko는 기계 번역이다. 화자 [[martin-keen|Martin Keen]]의 이름은 **설명란 본문에만** 있다(*"IBM Technology의 Martin Keen이 …"*). 자막에는 이름도 소속도 IBM도 나오지 않는다. 형식은 가상의 **마이그레이션 에이전트** 하나를 따라가는 입문 해설이다. 이 에이전트는 낡은 코드베이스를 새 DB 드라이버로 옮긴다. 테제는 다음과 같다.

> **컨텍스트 창은 백만 토큰 이상으로 커졌지만, 창이 클수록 모델은 그 안의 토큰을 덜 믿을 만하게 쓴다(context rot). 창이 아무리 커도 attention은 유한하기 때문이다. 긴 작업에서 창은 네 가지 방식으로 망가진다. 틀린 결론이 사실로 굳는 poisoning, 긴 자기 이력이 행동을 끌고 가는 distraction, 도구가 너무 많아 고르지 못하는 confusion, 서로 다른 버전이 공존하는 clash다. 처방은 각각 validate · compact · curate · prune이고, 넷 모두 무언가를 버린다. 에이전트는 덜 들고 있을 때 긴 작업을 더 잘한다.**

> *"The more tokens in the window the less reliably the model uses any of them"* (00:50~00:58) · *"Context engineering is deciding what actually goes into this context window at each step of an agent's run."* (01:04~01:12) · *"The window might hold a million tokens, but the attention spread across those tokens is finite."* (04:20~04:31) · *"And all four fixes work by throwing something away. An agent can get better at long tasks by holding less."* (09:46~09:59)

이 위키에 개념 하나가 생긴다([[context-failure-modes]]).
- [[context-failure-modes]]: 실패 네 가지(poisoning · distraction · confusion · clash)와 처방 네 가지(validate · compact · curate · prune)를 **1:1로 짝지은 분류**다. 이 위키에는 실패 쪽 개별 조각이 흩어져 있었다. [[context-rot]](희석), [[deferred-tool-context]]·[[toolbox-pattern]](도구 bloat), [[llm-wiki-pattern]]·[[tech-bridge-agent-to-agent-as-search|Greze 편]]의 *영구 오염*, [[context-engineering]]의 *쏟아붓기의 세 가지 실패 양상*(IBM, 09-08)이 그것이다. 하지만 **한 창 안의 실패를 유형별로 나누고 처방을 짝지은 페이지**는 없었다.

나머지는 기존 페이지에 붙는 **입문 수준의 새 증언**이다.
- [[context-rot]]: 이름 없는 *"recent study"* 하나를 근거로 든다(18개 frontier 모델, 00:36~00:46). 메커니즘은 **유한한 attention budget**이다(04:02~04:31). n² 비용(Oracle 편 ②)이 아니라 희석(①) 쪽 설명이다.
- [[context-engineering]]: *"deciding what actually goes into this context window at each step"* — **매 단계**라는 시간축이 정의에 들어간다
- [[context-resets-and-compaction]]: *"compaction is lossy. A summary of a summary can start to drift like a photocopy of a photocopy."*(08:13~08:23). prune의 끝 형태로 *"start a fresh window just restating the current corrected state"*(09:17~09:28), 곧 reset을 든다
- [[deferred-tool-context]]·[[toolbox-pattern]]: 46 vs 19 도구(06:37~06:52, 출처 미상), *"tool sprawl"*, *"it can always go and fetch others if it actually needs them"*(08:50~09:02)
- [[files-vs-database-agent-memory]]·[[agent-memory]]: 창 밖 *"permanent files"*로 빼낸 뒤 *"only when it's actually needed"* 다시 꺼낸다(08:20~08:41). 에이전트의 **자기 메모**가 poisoning의 진원지가 된다(03:38~03:50)
- [[behavior-validated-trust]]: *"Before a conclusion gets written down into this context window, check it against something real."*(07:39~07:46). IBM 계열이 *"생성이 아니라 결과를 믿어라"*를 **컨텍스트 쓰기**에 적용한 형태다

ASR·ko 보정. ko는 **처방 이름을 잃는다.** *curate*는 **"치유"**(08:45~08:48, `en` *"cure"* 공유)가 되고 요약에서는 "선택하세요"(09:41)가 된다. 두 번째 처방 앞의 *"What about distraction?"*은 **"혼란?"**(07:51~07:54, ko 단독)이 되어 compact가 confusion의 처방처럼 읽힌다. *compaction*은 "다짐"(08:15)이 된다. 수치도 망가진다. *"offered 46 tools"*는 **"46번의 임무"**(06:40)가 되고, *"a million or more"*(토큰)는 "백만 명 이상"(00:08)이 된다. 결론으로 이어지는 질문 *"how does an agent get better (…) by holding less context?"*는 **"상담원이 고객 유지율을 높이는 방법"**(01:39)이 된다. driver는 "컨트롤러"(03:41, 04:54), *"don't bother"*는 "화내지 마세요"(03:50), *keep … lean*은 "밝혀줍니다"(10:02, `en` *"light"* 공유)다. ⚠️ ko는 poisoning을 **"맥락 왜곡"**(04:38)으로 옮기는데, 이 말은 [[context-rot]]의 aliases에 *rot*의 ko 역어로 이미 올라 있다. 이 위키는 챕터의 번역어(오염 · 산만함 · 혼란 · 충돌)를 쓴다. 전체 보정표는 raw 헤더에 있다.

> ⚠️ **화자 이름은 설명란에만 있다.** 자막의 1인칭은 *"I'm going to cover four of them"*(01:14~01:21), *"because I'm feeling nice I'll also suggest how to fix each one"*(01:28~01:32)뿐이다. 제작 채널 판정 근거는 설명란 본문의 *"IBM Technology"*, `ibm.biz` 링크 둘(설명 문구 없음, 열어 보지 않음), @IBMTechnology · @IBM · @IBMDeveloperAdvocates 링크다. 해시태그에는 IBM이 없다.
>
> ⚠️ **수치 두 개 모두 출처가 없다.** *"a recent study looked at 18 frontier models and it turned out that they all got less reliable as the context window got bigger"*(00:36~00:46), *"in one benchmark, a model failed a task when it was offered 46 tools, but it then passed the very same task when it was only offered 19 tools"*(06:37~06:52). 연구·벤치마크·모델 이름은 발화되지 않고 설명란에도 없다. 네 실패 유형의 **이름과 분류의 출처**도 밝히지 않는다. 위키 판독으로는 Drew Breunig의 2025년 글 *How Long Contexts Fail*과 이름이 같고, "18개 모델" 연구는 Chroma의 context rot 보고서일 가능성이 있다. ⚠️ 둘 다 편집자의 배경지식이고 이 회차에서 확인하지 않았다. 확인 전까지 이 위키는 네 이름을 **이 영상의 분류**로만 기록한다.
>
> ⚠️ **예시는 가상이다.** 마이그레이션 에이전트, 틀린 재시도 메모, 버전 관리 · DB 콘솔 · 티켓 시스템 도구(06:09~06:25)는 모두 설명용 설정이다. 실제 에이전트·하네스·모델 이름은 없다. 처방의 효과도 측정되지 않는다. *"one quick connection test and our agent would never have written this no retry code note"*(07:43~07:53)는 가정이다.
>
> **벤더 프레이밍 — 약하다.** 자막에 IBM 제품(watsonx 등)은 나오지 않는다. 처방 넷은 모두 일반 기법이다. 벤더 색은 설명란 링크(`ibm.biz` 둘)에만 있다. 이 위키의 다른 IBM 편들처럼 **자사 제품 없는 화이트보드 입문 해설**이다(→ [[ibm]]).
>
> ⚠️ **녹화 시점 단서가 없다.** 연도 · 모델명 · 행사 언급이 없다. *"a recent study"*는 시점을 고정하지 않는다. `upload_date` 20261019는 Tech Bridge의 재배포일이고, IBM Technology 원본의 게시일은 `meta.txt`에 없다.

## 1. 도입 — 창이 커지면 더 똑똑해지는가 (00:00~01:50)

- *"Context windows have grown from well a few thousand tokens to well a lot bigger like a million or more"*(00:00~00:12). 그렇다면 에이전트는 긴 작업을 더 잘해야 하지 않느냐는 물음(00:17~00:35)에 화자는 아니라고 답한다.
- ⭐ *"Well a recent study looked at 18 frontier models and it turned out that they all got less reliable as the context window got bigger."*(00:36~00:46) ⚠️ 연구 이름 없음.
- *"Researchers have taken to giving this thing a name and that is context rot. The more tokens in the window the less reliably the model uses any of them and this is the problem that context engineering is there to solve."*(00:43~01:04)
- ⭐ 정의: *"Context engineering is deciding what actually goes into this context window at each step of an agent's run."*(01:04~01:12)
- 예고: 네 실패 유형과 각각의 처방. *"the funny thing about those fixes is they involve deliberately throwing away information."*(01:29~01:39)

→ [[context-rot]] · [[context-engineering]]

## 2. 창 안에 무엇이 들어 있나 — 마이그레이션 에이전트 (01:50~04:31)

예시는 *"an AI agent was given the job to migrate an aging code base over to a new database driver"*(01:50~01:57)다. 창의 구성을 앞에서부터 그린다.

| 띠 | 발화 | 크기 |
|---|---|---|
| 시스템 프롬프트 | *"That's the standing instructions for how the agent operates in general."*(02:11~02:18) | — |
| 과제 | *"just as a prompt on its own. And it might not be very big. It might only be a couple of lines."*(02:24~02:30) | 몇 줄 |
| 프로젝트 지시 | *"many agent harnesses also pull in a bunch of project instructions"*(02:30~02:36), 예: *"an agents.md file explaining how this particular project is built"*(02:36~02:43) | — |
| 도구 정의 | *"a description of every tool the agent can call"*(02:47~02:51) | — |
| 메시지 이력 | *"every step the the agent has taken. And after, let's say, an hour of running, well, this could get pretty big."*(03:00~03:09) | 시간에 비례 |
| 도구 결과 | *"the biggest band is probably the tool results"*(03:11~03:17): 파일 내용 · 테스트 출력 · 오류 로그 · 스키마 덤프 | 가장 큼 |

- 요약: *"the job description, the prompt is a few lines near the front, and pretty much everything else is the stuff that the agent kind of piles up along the way."*(03:23~03:33)
- 복선: *"This is a note the agent wrote itself. It says that the new driver retries failed connections automatically, so the old retry code can be deleted."*(03:38~03:50)
- ⭐ 핵심 메커니즘: *"a model doesn't look things up in its context the way a database looks up a row. Every token in the window is competing for a finite amount of attention. Essentially, an attention budget."*(04:02~04:20) *"And to me, this is kind of the crux of it. The window might hold a million tokens, but the attention spread across those tokens is finite."*(04:17~04:31)

→ [[context-rot]](① 희석 쪽 설명, 측정 없음) · [[attention-mechanism]] · [[context-window-as-floppy-disk]]

## 3. 네 가지 실패 유형 (04:31~07:28)

| # | 유형 (챕터 역어) | 정의 (발화) | 예시 속 증상 |
|---|---|---|---|
| ① | **poisoning** (오염) | *"A mistake gets into this context window somewhere, and then gets treated as fact because to the AI model, its own notes, they look like the ground truth."*(04:58~05:13) | 에이전트가 *"skimmed the driver's documentation, it misread it, and then it's written down a false conclusion"*(04:50~04:58). 그 결과 *"file after file our agent has been deleting perfectly good retry code"*(05:11~05:17) |
| ② | **distraction** (산만함) | *"This is where the sheer size of the history starts steering the agent."*(05:23~05:29). *"a language model at its heart is just a pattern continuation machine"*(05:29~05:34)이므로 *"that history becomes pretty much the strongest pattern around, stronger than the reasoning it picked up in training"*(05:36~05:46) | *"instead of asking what the job needs next, the model might drift into doing more of what it has already done"*(05:46~05:55). *"Agents in this state can get stuck just kind of going over old ground."*(05:53~06:00) |
| ③ | **confusion** (혼란) | *"this one comes from the tools"*(06:05~06:09). *"each of these tool definitions is in the window whether it actually gets used or not. And having more of them makes choosing the right tool a bit harder."*(06:26~06:39) | ⭐ *"in one benchmark, a model failed a task when it was offered 46 tools, but it then passed the very same task when it was only offered 19 tools. That is tool sprawl at work."*(06:37~06:52) ⚠️ 출처 미상 |
| ④ | **clash** (충돌) | *"context clash, which is when the window contains information that disagrees with itself"*(06:54~07:02) | 에이전트가 재시도가 일어나지 않는 것을 보고 메모가 틀렸음을 알아채 정정을 적는다(07:02~07:14). 그러면 *"we now have both versions sitting in the window that are presenting conflicting information"*(07:14~07:22) |

- ①과 ④는 **같은 메모의 두 시점**이다. 틀린 메모가 쓰일 때가 poisoning이고, 정정이 덧붙어 둘이 공존할 때가 clash다. 같은 사건에서 두 유형이 이어진다는 점이 예시의 설계다.
- ②의 근거는 메커니즘 주장(*"pattern continuation machine"*)이고 측정은 없다.

→ [[context-failure-modes]](신규) · [[deferred-tool-context]] · [[tools-are-not-neutral]] · [[llm-wiki-pattern]](영구 오염)

## 4. 네 가지 처방 (07:28~09:51)

| 실패 | 처방 | 발화 |
|---|---|---|
| poisoning | **validate** | ⭐ *"Before a conclusion gets written down into this context window, check it against something real."*(07:39~07:46) *"one quick connection test and our agent would never have written this no retry code note."*(07:43~07:53) |
| distraction | **compact** | *"the agent can summarize it, which is to say it throws the full log away and starts again from the summary"*(08:02~08:10). 한계: ⭐ *"Now, compaction is lossy. A summary of a summary can start to drift like a photocopy of a photocopy."*(08:13~08:23). 보완: *"consider moving as much out of the context window as possible and put them into permanent files instead. Detailed information can be retained in those files and then it can be pulled into the context window only when it's actually needed."*(08:20~08:41) |
| confusion | **curate** | *"Well, that is a curation problem."*(08:44~08:46) *"The agent doesn't need 46 tools for database migration. So, just give it the handful that the job calls for and then it can always go and fetch others if it actually needs them."*(08:50~09:02) |
| clash | **prune** | *"when information gets superseded, just delete the old version rather than leaving both in the window."*(09:10~09:16) 더 나아가면 *"Or go further and start a fresh window just restating the current corrected state of the job and leave the poison stuff behind."*(09:17~09:28) |

- 요약 반복(09:28~09:51): *"if a false conclusion gets saved, that's poisoning. So, you can validate. If the history has taken over, that's distraction, so compact. If the agent has more tools than the task needs, that's confusion, so curate. And if the context disagrees with itself, that's a clash, and the fix is prune."*
- ⭐ 맺음: *"And all four fixes work by throwing something away. An agent can get better at long tasks by holding less."*(09:46~09:59)
- ⚠️ compact 칸은 사실 **처방 둘**이다. 요약(compaction)과, 창 밖 파일로 빼내기(offloading)다. 화자는 둘째를 compaction의 손실에 대한 보완으로 소개하고 따로 이름 붙이지 않는다.
- ⚠️ validate는 넷 중 유일하게 **버리지 않는** 처방이다. 쓰기 전에 거르는 것이다. *"all four fixes work by throwing something away"*는 validate를 *틀린 결론을 애초에 넣지 않는 것*으로 읽을 때만 성립한다(위키 판독).

→ [[behavior-validated-trust]] · [[context-resets-and-compaction]] · [[files-vs-database-agent-memory]] · [[agent-memory]] · [[deferred-tool-context]] · [[toolbox-pattern]] · [[harness-pruning]]

## 5. 맺음 (09:59~10:11)

- *"Now, I'd love to know how you keep an agent's context lean. Do you have your own context engineering fixes? Let me know in the comments."*(09:59~10:11)

## 이 위키와의 연결

### 이어지는 것

- **[[context-rot]]: 처음으로 "연구"가 근거로 붙는다. 다만 이름이 없다.** 그 페이지의 Oracle 편([[ignacio-martinez|Martinez]])은 측정 없이 희석과 n² 비용을 한 흐름으로 말했다. 이 화자는 n² 이야기를 하지 않고 **attention budget**(희석) 하나로 설명한다. 그리고 *"18 frontier models"*라는 수치를 든다. ⚠️ 이 수치로 그 페이지의 *"정량 — 미해결"*을 닫을 수는 없다. 출처를 확인해야 한다.
- **[[context-engineering]]: IBM 계열 세 번째 컨텍스트 편.** 09-08 [[tech-bridge-agent-knowledge-four-ways]]는 *다 쏟아붓기*의 실패를 세 갈래로 나눴다(길을 잃음 · 막다른 길 · 일반론으로 후퇴). 09-23 [[tech-bridge-tokenmaxxing-to-valuemaxxing]]은 *비용 때문에 잘라내기*의 실패를 말했다. 10-16 [[tech-bridge-five-concepts-coding-with-ai-agents|Clyburn 편]]은 컨텍스트를 자원 한계로 정의했다. 이번 편은 **한 실행 안에서 창이 어떻게 망가지는가**를 네 유형으로 나눈다. 앞의 세 갈래(09-08)는 *지식 조달* 축이고, 이번 넷은 *창 위생* 축이다. 둘을 하나의 목록으로 합치지 않는 것이 맞다(위키 판독).
- **[[deferred-tool-context]]·[[toolbox-pattern]]: 같은 처방, 처음으로 수치가 붙은 판본(출처 미상).** Factory([[tereza-tizkova|Tížková]])는 도구 bloat가 잘못된 도구 선택을 부른다고 했지만 수치는 *"50% of tokens"*(벤더)뿐이었다. 이 화자는 **정확도 쪽 수치**(46개 도구에서 실패, 19개에서 통과)를 든다. curate의 *"it can always go and fetch others"*는 deferred loading을 이름 없이 말한 것이다.
- **[[context-resets-and-compaction]]: "all compression is lossy"의 두 번째 증언.** 같은 페이지의 다른 강의는 *"all compression is lossy"*라고 했다. 이 화자는 그 손실이 **반복될 때 누적된다**고 덧붙인다(*"photocopy of a photocopy"*). prune의 끝 형태(*"start a fresh window just restating the current corrected state"*)는 structured handoff를 쓰는 **context reset**과 같은 모양이다.
- **[[behavior-validated-trust]]: IBM 계열이 같은 원리를 또 말한다.** [[ibm]] 페이지는 *"사람이 썼기 때문에 → 행동을 검증했기 때문에"*가 IBM 편들에서 되풀이된다고 기록했다(09-08, 09-17, 09-18). 이번엔 그 대상이 **에이전트가 자기 컨텍스트에 쓰는 결론**이다. 검증을 출력 쪽이 아니라 **기억에 쓰기 전**에 둔다.
- **[[llm-wiki-pattern]]·[[agent-memory]]: 자기 메모가 오염원이 된다.** Greze 편의 *"정보 하나가 틀리면 영원히 오염된다"*는 공유 지식 층의 이야기였다. 이 화자는 같은 일을 **한 세션의 자기 메모**에서 보인다(*"its own notes, they look like the ground truth"*). 처방(쓰기 전 검증, 정정 시 옛 버전 삭제)은 [[no-silent-write]]와 같은 방향이다.

### 갈리는 것

> ⚠️ Contradiction: **[[long-context-agents]]와 정면으로 갈린다.** MiniMax([[olive-song|Olive Song]], 09-08)는 *"모든 도구 응답을 받고 여러 라운드를 거치는 상황에서는 짧은 컨텍스트로는 복잡한 작업을 수행하기에 충분하지 않다"*며 긴 창으로 이력을 받으라고 처방했다. 이 화자는 같은 상황(*"after (…) an hour of running"*, 도구 결과가 가장 큰 띠)을 **문제**로 보고 *"An agent can get better at long tasks by holding less"*(09:54~09:59)라고 결론짓는다. 이 대립은 [[context-rot]]에 이미 기록된 Oracle ↔ MiniMax 대립과 같은 축이고, 이 영상은 **줄이는 쪽**에 한 표를 더한다. ⚠️ 어느 쪽에도 대조 측정은 없다. 이 화자의 "18개 모델" 연구는 출처가 확인되지 않았다.

> **[[token-minimization-trap]]과의 긴장(위키 판독).** 같은 IBM 계열의 09-23 편은 비용 때문에 잘라내다 보면 *작업 설명 · 도메인 제약 · 아키텍처 컨텍스트*까지 지우게 된다고 경고했다. 이번 편은 *"all four fixes work by throwing something away"*를 결론으로 삼는다. 두 편은 모순되지 않는다. 이번 편이 버리라는 것은 틀린 결론 · 대체된 버전 · 안 쓰는 도구 · 요약 가능한 이력이고, 과제 프롬프트(*"a few lines near the front"*)는 손대지 않는다. 다만 이번 편은 **무엇을 버리면 안 되는지**를 말하지 않는다. compact가 그 경계를 넘는 경우(요약의 표류)는 화자 스스로 인정한다(08:13~08:23).

> **[[context-resets-and-compaction]]의 Managed Agents "제3의 길"과의 긴장(위키 판독).** [[anthropic-managed-agents]]는 세션 로그를 창 밖에 durable하게 두고 *"irreversible한 compaction/trimming 결정을 미룰 수 있다"*고 했다. 이 화자의 compact는 *"throws the full log away"*(08:06~08:10)이고, prune은 *"just delete the old version"*(09:10~09:16)이다. 버리는 범위가 **창**인지 **기록 전체**인지 화자는 구분하지 않는다. 08:20~08:41의 영구 파일 보완은 Managed Agents 쪽에 가깝다.

## 해소하지 않고 표시만 한 것

- *"a recent study looked at 18 frontier models"*의 이름 · 연도 · 측정 과제. Chroma 보고서인지(편집자 추정, 미확인).
- *"in one benchmark"* 46 vs 19 도구의 벤치마크 · 모델 · 과제.
- 네 유형 이름(poisoning · distraction · confusion · clash)의 출처. Drew Breunig의 *How Long Contexts Fail*과 같은 분류인지(편집자 배경지식, 미확인). 화자는 출처를 밝히지 않는다.
- 원본(IBM Technology) 게시일. 화면(화이트보드)의 내용.
- `ibm.biz` 링크 두 개의 목적지(열어 보지 않았다).
- **통합자 외부 확인 (2026-10-20).** Drew Breunig, *"How Long Contexts Fail"*(2025-06-22, <https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html>)은 같은 네 이름(Context Poisoning · Distraction · Confusion · Clash)을 쓰고, 46개 도구에서 실패·19개에서 성공한 사례(GeoEngine 벤치마크, 양자화한 Llama 3.1 8B)를 인용한다. Chroma *"Context Rot: How Increasing Input Tokens Impacts LLM Performance"*(Hong · Troynikov · Huber, 2025-07-14, <https://www.trychroma.com/research/context-rot>)는 18개 LLM을 평가했다. 이름·수치는 일치하지만 **화자가 이 자료를 근거로 삼았는지는 여전히 발화되지 않았다.** → [[context-failure-modes]]

## 등장 개체

- 인물: [[martin-keen|Martin Keen]](⚠️ 이름은 설명란 본문에만, 신규)
- 조직: [[ibm|IBM Technology]](설명란 기준, 자막에는 없음) · [[tech-bridge]](재배포)
- 제품·형식: agents.md(*"an agents.md file"* 02:36~02:40, 페이지 없음)
- 개념: [[context-failure-modes]](신규) · [[context-rot]] · [[context-engineering]] · [[context-resets-and-compaction]] · [[deferred-tool-context]] · [[toolbox-pattern]] · [[files-vs-database-agent-memory]] · [[agent-memory]] · [[behavior-validated-trust]] · [[long-context-agents]] · [[token-minimization-trap]] · [[attention-mechanism]] · [[llm-wiki-pattern]] · [[no-silent-write]] · [[tools-are-not-neutral]] · [[harness-pruning]] · [[context-window-as-floppy-disk]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=E8zCcv2HcbI> (10:11, `upload_date` 2026-10-19, Tech Bridge 재배포)
- raw: `01.raw/articles/2026-10-19_컨텍스트 엔지니어링 - AI 에이전트가 피해야 할 네 가지 실패 유형.md`
- 설명란 링크: <https://ibm.biz/~5YM1VAeG0> · <https://ibm.biz/~D9ApFMnpA> (⚠️ 열어 보지 않았다)
- 같은 IBM 계열 컨텍스트 편: [[tech-bridge-agent-knowledge-four-ways]] · [[tech-bridge-tokenmaxxing-to-valuemaxxing]] · [[tech-bridge-five-concepts-coding-with-ai-agents]]
- 대립·이웃 소스: [[tech-bridge-oracle-agent-memory-harness]](context rot) · [[tech-bridge-minimax-m3-long-context]](긴 창) · [[tech-bridge-factory-software-factory]](도구 bloat) · [[tech-bridge-agent-to-agent-as-search]](영구 오염)
- [[tech-bridge]] · [[ibm]] · [[martin-keen]]
