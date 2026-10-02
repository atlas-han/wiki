---
title: "Tech Bridge — 진짜 '소프트웨어 팩토리'를 만들려면 (Factory · Tereza Tížková): 비종속·자율·지속 개선의 3원칙과 Missions·라우팅·지연 컨텍스트"
type: source
tags: [software-factory, model-routing, prompt-caching, missions, orchestrator-worker-validator, validation-contract, computer-use, deferred-context, tool-bloat, agent-readiness, codebase-hygiene, plugins, factory-ai, vendor-claims, video]
source-url: https://www.youtube.com/watch?v=cHsunDt0QUc
source-type: video
author: Tech Bridge (한영자막 재배포) · 발표 [[tereza-tizkova]] ([[factory-ai|Factory]] — 자막엔 "Theresa/Teresa"·"factory.com", 성·도메인은 설명란) · 행사·촬영일 미확정
date-published: 2026-10-01
ingested: 2026-10-02
created: 2026-10-02
updated: 2026-10-02
---

# Tech Bridge — 진짜 '소프트웨어 팩토리'를 만들려면 (Factory · Tereza Tížková)

[[tech-bridge|Tech Bridge]]가 재배포한 **21:55 발표, Q&A 없음, 공식 챕터 28개.** 2026-09-28부터 **멤버십 전용**이었고(09-30 회차에 확인, ingest 보류) **2026-10-02 공개 전환을 확인**해 ingest했다 — 공개 후 `upload_date`는 2026-10-01. 화자는 [[factory-ai|Factory]](factory.ai)의 [[tereza-tizkova|Tereza Tížková]]. 이 위키에 **"software factory"가 처음으로 정의를 달고 들어왔다** — 지금까지는 [[tech-bridge-figma-coding-agents]]에서 따옴표 친 한 단어(*"계획만 있으면 그 위의 루프·워크플로·'software factory'는 무엇이든"*)였다. → [[software-factory]] (신규)

> **소프트웨어 팩토리는 코딩 에이전트도, 코딩 에이전트 수천 개의 스웜도 아니다. 신호 수집부터 우선순위·오케스트레이션·실행·검증·프로덕션 테스트·반복·학습까지 개발 생애주기 전체를 자율로 도는 루프다. 짓는 원칙은 셋 — 모델·도구·업무 방식에 비종속(agnostic), 오래 믿고 맡기는 자율(autonomous), 사람 조직처럼 계속 배우는 개선(always improving).**

> *"I would define the software factory as the whole loop the whole life cycle of developing software with autonomy which doesn't mean just coding and generating code"* (00:47~01:00) · *"generating code writing code that's the easy part compared to all the others"* (02:27~02:32) · *"We should be as a humans deciding what to build in the software not how to build it. uh because that's up for the agents"* (20:54~21:02)

ASR·ko 보정: ko가 **컴퓨터 사용·VM이 "전엔 별로, 지금은 아주 좋다"를 "전엔 좋았는데 지금은 별로"로 뒤집고**(14:23), **"엔지니어는 대부분의 시간을 코드 작성에 쓰지 않는다"를 "최고 수준 시험조차 통과하지 못한다"로 창작**하고(02:34), *nondeterministic* 의 *non-*을 잃어 **"결정론자들"로**(10:28), *LLM labs* 를 **"법학 석사(LLM) 과정"으로**(08:56), *automatic model routing in Factory* 를 **"라우팅이라고 불리는 공장 자동 모델들"로**(06:11), *power law* 를 **"법과 같아요. 힘."으로**(16:54), arena를 **"모래"로**(13:33, 14:27), 플러그인이 담는 *"can't really quantify"* 한 암묵지를 **"코딩을 할 수 있습니다"로**(19:29 — `en`도 같은 오류) 옮겼다. en-orig는 화자를 *"Theresa/Teresa"*, 회사를 *"factory.com"*(세 트랙 공통 — 설명란은 factory.ai), Ralph loop을 *"dal loop"*, AutoWiki를 *"auto which"* 로 들었다. 전체 목록은 raw. **인용은 en-orig에서만** 했다.

> ⚠️ **당사자(벤더) 진술 — 수치의 근거는 발화와 보이지 않는 슬라이드뿐.** 25% 비용 절감(*"our benchmark which is very conservative"* 06:56~06:58 — 과제·기준선 미발화), 50% 이상 토큰 절감(16:40~16:42 — 측정 조건 없음), 고객 미션 16시간 중 검증 40%(11:51~12:02 — 1건), 미션이 *"weeks"*(04:04~04:05), 에이전트가 *"a year or more"* 사람 없이 돈다는 **예측**(03:51~03:58 — 누구의 예측인지 없음), 기업 평균 *"hundreds tools"*(15:25~15:30), *"data from Stanford"*(17:21~17:23 — 연구 이름 없음). **독립 검증 없음.** 화자는 이 모든 기능을 파는 회사 사람이다.
>
> ⚠️ **행사·촬영일 미확정.** 행사명·연도 발화 없음. 시점 단서는 *"by history I mean 2023 in AI"*(01:29~01:35), Coinbase CEO 트윗 차트(05:14~05:20), *"one thing we launched for that is plugins"*(19:19~19:23) 정도.
>
> ⚠️ **챕터가 발화보다 앞서 간 자리.** 13:28 챕터 *"실제 웹 앱을 클릭하며 테스트하는 브라우저 검증자"* — 발화는 *"virtual computer"*(13:38~13:40)·*"computer use and the persistent environments virtual machines"*(14:15~14:20)이고 **browser·web app은 자막에 없다.** 00:08 의제 *"Should I build your own or outsource it?"*(00:20~00:22)에는 **명시적 답이 없다**(가장 가까운 것은 컨설팅 비판, §2).

## 1. 정의 — 그리고 왜 지금인가 (00:48~02:18)

**정의**(00:47~01:22): *"collecting all the signals reacting to user feedback to logs prioritizing what's important then orchestrating it all executing validating doing really good uh testing in production and then iterating on all this uh while also continuously improving in the process and gaining new knowledge and new skills"*(01:00~01:22). 대시보드 화면이 *"catching the whole cycle"*(01:26~01:29)이라 했으나 화면은 자막에 없다.

**왜 전엔 안 됐나**(01:29~02:18): 루프 발상은 *"from the beginning of CH GPT lounge[=ChatGPT launch]"* 부터 있었고 *"autog baby agi[=AutoGPT, BabyAGI]"*(01:44)도 있었다. 막힌 것은 환각, 컨텍스트 길이, 추론 품질, 그리고 *"we were missing good environments where the agents can actually work in the isolation"*(02:01~02:07). → [[long-context-agents]]

## 2. 소프트웨어 팩토리가 아닌 것 (02:18~03:13)

- **코딩 에이전트도, 그 스웜도 아니다** — *"it's not even a swarm of coding agents even thousands of agents"*(02:25~02:29). 코드 작성은 쉬운 부분이고 *"engineers don't even spend most of the time uh just writing code"*(02:32~02:37). → [[verification-bottleneck]]과 같은 진단
- **컨설팅·추상 전략이 아니다** — *"you can't invite a consultancy and just throw something in the middle of your organization. You should really be mindful and rebuild it from scratch"*(03:01~03:09). → [[agent-org-adoption]]

> 위키의 정리: 의제에 있던 **"직접 지을까, 외주를 줄까"** 에 대한 화자의 답은 이 컨설팅 비판이 전부다 — *조직을 처음부터 다시 지어라*. "Factory 제품을 쓰라"는 말은 하지 않지만 발표 전체가 자사 기능의 목록이다.

## 3. 3원칙 (03:13~04:33)

*"I think it's similar to building the real team of humans because there is a lot of agents (…) and it all can end up as a big chaos"*(03:18~03:31).

| 원칙 | 내용 | en-orig |
|---|---|---|
| **Agnostic** (비종속) | LLM 선택과 *"how you already work as the organization"* 에서 독립 | 03:33~03:44 |
| **Autonomous** (자율) | 신뢰·권한·거버넌스를 주고 *"trust it to run really for a long time"*. Missions는 이미 *"run for weeks"* | 03:44~04:07 |
| **Always improving** (지속 개선) | 새 팀원 온보딩처럼 코드베이스 이해·구조·문서를 주고, 과정에서 배운 지식을 팀에 공유하게 | 04:07~04:27 |

→ [[software-factory]]

## 4. Agnostic — 업무 방식·모델·비용 (04:33~09:33)

**업무 방식**(04:30~05:06): Slack·GitHub 등 기존 환경에 붙고, *"allow people to already bring subscriptions they are using"*(04:48~04:52) — 새 프런티어 모델·벤치마크가 계속 나와 *"difficult to catch up but also to predict what will be the winning"*(04:58~05:03).

**Coinbase 차트**(05:09~06:06): Coinbase CEO가 트윗한 차트 — *"they started uh started saving money (…) but without reducing the token spend"*(05:20~05:26), *"they continue growing and token maxing but they stopped spending so much money"*(05:30~05:35). 화자가 꼽은 방법 넷: ① 사람마다 다른 **기본 모델**(*"stop pushing people to use only the frontier as a default"* 05:42~05:47) ② **캐싱**(*"to stop prefilling the stuff every time"* 05:49~05:51) ③ **지출 한도는 없되 결과를 보여야 함**(05:51~05:55) ④ **라우팅**(05:57~06:06). ⚠️ 차트 수치는 화면뿐. → [[model-mixing-economics]] · [[overspending-underusing-loop]]

**자동 모델 라우팅**(06:09~08:43) → [[automatic-model-routing]] (신규)

- 먼저 최적 모델을 정하고, 실패하거나 문제가 생기면 다른 모델로 전환 — *"but it usually doesn't happen"*(06:25~06:34)
- 비용만이 아니다 — *"It also helps with reliability or with speed because open source models are often faster and uh if one LM provider fails you can just switch to another one automatically"*(06:41~06:51)
- ⭐ **4단계**(07:09~08:01): ① **할당** — 조직은 사람별 권한·기본 모델을 줄 수 있다(마케팅·영업·엔지니어) ② **분류** — *"This is the magic of the routing"*: 프롬프트 구조·코드베이스·난이도·사용 도구로 **과제 난이도를 분류** ③ **임계값** — 과제를 끝내기에 충분한 수준 ④ **선택** — *"you choose the cheapest model above the threshold"*(07:54~07:59)
- **수치**: *"You can save for example 25% but even more probably"*(07:03~07:09) — ⚠️ 벤더 벤치마크, 구성 미발화
- **받은 질문**(08:04~08:43): 정말 되나, 모델이 놓치면, 더 느린가·비싼가, 업그레이드가 필요하면, 캐싱은? 답: 분류를 잘해 *"not to need to switch too often"*, 중간에 더 강한 모델로 올라가도 *"you still overall are faster probably"*(08:37~08:40) — ⚠️ 근거 없음

**캐싱과 오픈 모델**(08:44~09:28): *"open models can do this as well (…) host open models as well uh on dedicated compute and you can take the same advantage of the caching"*(09:00~09:12). ⭐ *"the final price for users is just a pricing decision. It's not a technical challenge because everyone can do caching"*(09:15~09:22).

> ⚠️ **답하지 않은 질문 — 라우팅과 캐시의 충돌.** 과제 중간에 모델을 바꾸면 이전 모델의 프롬프트 캐시는 새 모델에서 쓸 수 없다. 화자는 *"how do you handle caching?"*(08:17~08:19)을 **가격 정책 문제로** 답했을 뿐, 전환이 캐시 적중률에 주는 비용은 말하지 않는다. [[tech-bridge-nadella-copilot-autopilot]]은 같은 문제를 *"여러 모델 패밀리를 넘나들며 KV 캐시 적중률"* 최적화로 **명시적 난제**로 꼽았다.

## 5. Autonomous — 루프, 완료, Missions (09:33~14:43)

**루프의 문제는 완료다**(09:33~10:42): *"You probably heard about dal[=Ralph] loop and specifying the tasks and splitting to subtasks for agents"*(09:50~09:55) — ⚠️ en-orig *"dal loop"*, `en`·ko *"Ralph loop"* (→ [[ralph-wiggum-method]], 판독 추정). ⭐ *"the question is not the loop itself but the question is how how you define what it means to be done in the loop"*(09:58~10:05). 예전 프로그래밍의 루프는 종료 조건이 명확했지만 지금은 *"the criteria become open-ended because a lot of the tasks are very nondeterministic. It's basically open world"*(10:23~10:30) — 동료가 만든 **로고 3D 프린팅 루프** 사례. *"they just need to be verifiable"*(10:42). → [[verifiable-goals]]

**scary chart와 cheating**(10:45~11:25): 자율 실행 시간은 늘지만 *"Even if you can run for a very long time, it doesn't mean that it will be reliable in production"*(10:54~11:01) — 차트 출처는 미발화. *"if you write the what it means to be done in a wrong way, the agent can try to pass your test but not really (…) verify what you need"*(11:08~11:19). → [[reward-hacking]]

**Factory Missions**(11:26~12:58):

- 장시간 세션, *"we send the agent to the mission"*, 끝날 때까지 루프, *"even for weeks"*(11:28~11:40)
- **오케스트레이터 → 워커 → 검증자**: 오케스트레이터가 *"decides and writes the conditions what it needs to be done"*(12:05~12:08), 워커가 일하고, 검증자가 리뷰해 피드백을 처음으로 돌려보낸다(12:53~12:58)
- ⚠️ 고객 미션 **16시간**, 그중 검증이 **40%**(11:51~12:02) — 1건, 슬라이드
- ⭐ **스웜이 아니라 순차** — *"they work in a sequence. So they don't work in a swarm or parallel. (…) we actually found that if you do this you end up with more fresh context and kind of fresh head. Same with when with humans have like other colleagues verifying their code"*(12:17~12:37). 다만 각 워커는 웹 조사·파일 생성 같은 작은 일에 **병렬 서브에이전트**를 쓸 수 있다(12:42~12:53)

**검증자와 validation contract**(13:01~14:43) → [[generator-evaluator-pattern]] · [[sprint-contract]]

- ⭐ *"the validators judge code that they didn't write"*(13:01~13:07)
- ⭐ **validation contract** — 오케스트레이터가 *"that's written before any code is done"*(13:07~13:14)
- **scrutiny validator** — 코드베이스·*"liners[=linters], types, tests"*, *"really rigorous check of the code"*(13:16~13:27)
- **user testing validator** — *"really in the arena trying the things. So it doesn't care how it was made (…) It works in its virtual computer and it clicks on the stuff"*(13:33~13:43). 사례: 한 엔지니어가 Droid로 코드베이스를 마이그레이션 — 다른 제품은 *"created the product but it didn't work and was wasn't interactive. It was just a dummy result"*(13:55~14:03), 클릭해 보는 에이전트가 *"actually working and not just looking good in the code"*(14:09~14:13)임을 확인했다. 가능해진 이유: 컴퓨터 사용과 에이전트용 영속 VM의 진보(14:13~14:25). → [[agent-visual-qa]]
- 시각화: *"it's just a loop with smaller loops"*(14:47~14:49)

## 6. Always improving — 컨텍스트, 준비도, 암묵지 (14:43~19:43)

**도구 bloat**(15:07~15:52): 기업은 Figma·Notion·Gmail·Drive·Slack 등 *"hundreds tools on average"*(⚠️ 출처 없음). 도구마다 스키마·파라미터·긴 설명이 있어 에이전트가 **비슷한 이름의 도구를 잘못 고르거나**, 컨텍스트 창을 채워 *"need to compress"* — *"So this is really dangerous"*(15:41~15:52). → [[context-rot]] · [[context-resets-and-compaction]]

**deferred context engine**(15:52~16:42) → [[deferred-tool-context]] (신규)

- *"we just progressively disclose what's in the context and what tools to use"*(16:00~16:05)
- 처음엔 **도구의 짧은 목록과 짧은 설명만**, 필요할 때 *"they can call the tool and fully load it"*(16:14~16:23)
- ⭐ *"nothing is actually removed. is just hidden and not reachable until needed"*(16:23~16:29)
- ⚠️ *"you can save 50% of tokens or more"*(16:40~16:42) — 도구가 많을수록 절감이 커진다는 말뿐
- *"a surprise tools"*(16:08) — 세 트랙 모두 같은 말, 원래 단어 미확정

**AI 도입은 power law**(16:45~17:39): *"when adopting AI, you either succeed big or you can fail big (…) it's a bit of power law"*(16:49~16:57). 코드베이스가 준비되지 않으면 소프트웨어 팩토리로의 전환이 *"actually make you end up worse and make your code degrading"*(17:04~17:12), 생산성 격차가 커진다. ⚠️ *"another data from Stanford"*(17:21~17:30) — 연구 이름 없음. *"sometimes AI really makes a mess and this can really compound"*(17:32~17:39). → [[codebase-gardening]] · [[greenfield-vs-brownfield-agent-risk]]

**Agent Readiness**(17:41~18:38) → [[agent-readiness]] (신규): *"I don't like the word framework but take it as a hygiene check of your code base"*(17:48~17:53). 코드베이스 상태와 AI 도입 성과 사이의 *"nice correlation"*(17:55~18:03 ⚠️ 수치 없음). 점검 항목: 개발 환경의 **재현성**, 좋은 **테스트**, **문서화**, 코드 **스타일**, 테스트와 **린터**(18:08~18:20). 큰 고객들이 점검 후 *"recommended actions"*(18:28~18:37)를 따른다.

**암묵지 — plugins와 AutoWiki**(18:40~19:41): *"you keep repeating to agents how how do you want the things done"*(18:52~18:56). 새 회사에 들어가면 *"a lot of rules that are not really codified anywhere"*(19:04~19:08)를 관찰로 배운다. 그래서 **plugins** — *"packaged reusable skills and context and the things behind the scenes that you can't really quantify"*(19:23~19:31) — 와 **AutoWiki**(en-orig *"auto which"*, 챕터·`en`으로 판독) — *"automatically updating our documentations and (…) reviewing and documenting what you have"*(19:31~19:41). → [[agent-skills]] · [[llm-wiki-pattern]] · [[company-brain]]

## 7. 인간의 자리 (19:42~21:51)

*"will humans just lose jobs and go to permanent underclass? I think they will not"*(19:47~19:53). 추상화의 사다리: *human computers* → 프로그래밍 언어 → 코딩 에이전트(가까이서 모니터링) → 소프트웨어 팩토리, *"where we manage these agents (…) orchestrator agents and workers and validators (…) and we just monitor and decide what to build"*(20:34~20:51). ⭐ **what, not how**(20:54~21:02). 경고 차트(21:11, 내용 미발화) 뒤에: AI는 멋진 일이 아니라 *"the annoying stuff"* — 정렬·회의·상태 공유·동기화를 가져간다(21:17~21:39). *"Go touch some grass and let your agents uh build for you"*(21:46~21:48). → [[outcome-engineering]]

## 이 위키와의 연결

### 이어지는 것

- **[[defense-factory]]** (OpenAI, 09-20) — 같은 "factory" 은유지만 **범위가 다르다**: 방어 공장은 *발견 → 분류 → 교정 → 배포 → 검증* 의 **보안 파이프라인**이고 트리거가 모델 릴리스다. 소프트웨어 팩토리는 **개발 생애주기 전체**이고 트리거가 사용자 피드백·로그다. 둘 다 *검증으로 끝나는 무인 루프*라는 골격은 같다. → [[software-factory]]에 구분 정리.
- **[[loop-is-the-product]]** (Introspection, 09-30) — *신호 → 행동 → 검증* 루프, 두 번째 루프가 지속 개선. Tereza의 정의(신호 수집 → … → 검증 → 지속 개선)와 거의 겹친다. *"loop with smaller loops"*(14:47)는 그 두 겹을 여러 겹으로.
- **[[model-mixing-economics]]** — 라우터가 하네스 안으로 들어가는 흐름(Oracle 09-24, Jev 09-26, Nadella *"auto가 제품"* 09-29)에 **4단계 메커니즘(분류 → 임계값 → 임계값 위 최저가)** 과 **조직의 사람별 기본 모델**이 더해졌다.
- **[[sprint-contract]] · [[generator-evaluator-pattern]]** — *코드 전에 done을 못 박는다*, *남이 쓴 코드를 판정한다*. Factory는 이를 **두 종류의 검증자**(정적 scrutiny vs 실행형 user testing)로 나눴다.
- **[[toolbox-pattern]]** (Oracle) — *도구를 전부 싣지 않는다*는 같은 결론, **다른 메커니즘**: Oracle은 매 반복 벡터 검색으로 넣고 빼고, Factory는 짧은 목록을 상시 두고 호출 시 로드한다.
- **[[codebase-gardening]]** (Lauren Tan) — *코드베이스가 에이전트의 기억이고 안티패턴이 복제된다* 는 진단에 대한 **조직용 점검표** 버전.

### 갈리는 것

> ⚠️ **Contradiction: 스웜인가 순차인가.** [[agent-swarm]]은 *문제를 쪼개 병렬 작업자에게* 주는 것을 패턴으로 다루고, [[tech-bridge-brockman-agi-era-defender-window]]는 에이전트 1만 개를 말한다. Tereza는 소프트웨어 팩토리를 **스웜이 아니라고 정의**하고(02:25~02:29), Missions의 워커를 **순차로** 돌린다 — 이유는 **신선한 컨텍스트**(12:27~12:32). 다만 워커 안에선 병렬 서브에이전트를 허용하므로(12:42~12:53) **층위의 차이**일 수 있다: 상위 흐름은 순차, 하위 잡일은 병렬. ⚠️ 순차가 더 낫다는 측정은 없다.

> ⚠️ **Contradiction: Coinbase 차트의 평가.** [[tech-bridge-mousepower-measuring-agents]](09-12)는 같은 회사의 CEO 차트를 *"좋은 출발이지만 문제는 여전히 토큰에 너무 집중돼 있다"* 로 유보했다([[overspending-underusing-loop]]). Tereza는 *"continue growing and token maxing but they stopped spending so much money"*(05:30~05:35)로 **성공 사례로** 든다 — 토큰 소비가 계속 느는 것을 문제로 보지 않는다. 같은 차트인지는 화면이 없어 미확정.

> ⚠️ **캐싱은 "누구나 할 수 있다" vs 캐시 적중률은 난제.** 위 §4 표시 참조 — [[tech-bridge-nadella-copilot-autopilot]]과 긴장.

## 해소하지 않고 표시만 한 것

- **수치 전부** — 25%(벤치마크 구성), 50%(측정 조건), 16시간·40%(1건), *"a year or more"*(예측 출처), *"hundreds tools"*, Stanford 데이터, Agent Readiness 상관관계, 라우팅 중간 전환 시 *"overall faster"*.
- **"직접 지을까, 외주를 줄까"** — 의제에만 있고 답 없음.
- **"browser" 검증자** — 챕터·설명란의 말, 발화는 *virtual computer*.
- **"dal loop"** — `en`·ko는 Ralph loop. 판독 추정.
- **"surprise tools"**(16:08) — 원래 단어 미확정.
- **scary chart·warning chart** — 출처·내용 미발화. 특정 연구(METR 등)로 연결하지 않는다.
- **validator가 다른 모델인지** — 검증자가 *남이 쓴 코드* 를 본다는 것만, 모델·프롬프트 분리 여부는 없다.
- **EY·Adobe** — *"possible to build this in production for enterprises like EY or Adobe"*(00:45~00:47)까지. 무엇을 구축했는지 없음.

## 등장 개체

- 인물: [[tereza-tizkova]] (신규) · Coinbase CEO(이름 미발화) · 화자의 동료(3D 프린팅 루프, 이름 미발화)
- 조직: [[factory-ai]] (신규) · Coinbase(페이지 없음) · EY(페이지 없음) · [[adobe]] · Stanford(연구 미특정)
- 제품·도구: Droid · Factory Missions · automatic model routing · deferred context engine · Agent Readiness · plugins · AutoWiki · Slack · GitHub · Figma · Notion · Gmail · Drive · AutoGPT · BabyAGI · ChatGPT
- 개념: [[software-factory]] (신규) · [[automatic-model-routing]] (신규) · [[deferred-tool-context]] (신규) · [[agent-readiness]] (신규) · [[model-mixing-economics]] · [[overspending-underusing-loop]] · [[generator-evaluator-pattern]] · [[sprint-contract]] · [[agent-swarm]] · [[verifiable-goals]] · [[reward-hacking]] · [[ralph-wiggum-method]] · [[agent-visual-qa]] · [[toolbox-pattern]] · [[context-engineering]] · [[codebase-gardening]] · [[defense-factory]] · [[loop-is-the-product]] · [[outcome-engineering]]

## References

- 원본 영상: <https://www.youtube.com/watch?v=cHsunDt0QUc> (21:55, `upload_date` 2026-10-01 — 멤버십 전용 → 공개 전환)
- raw: `01.raw/articles/2026-10-01_진짜 '소프트웨어 팩토리'를 만들려면 무엇이 필요할까요 — Factory Tereza.md`
- 설명란 링크: <https://factory.ai> · <https://x.com/tereza_tizkova> · <https://www.terezatizkova.com> (⚠️ 열어 보지 않았다)
- 같은 주제: [[tech-bridge-mousepower-measuring-agents]] · [[tech-bridge-nadella-copilot-autopilot]] · [[tech-bridge-oracle-agent-memory-harness]] · [[tech-bridge-introspection-loop-is-the-product]] · [[tech-bridge-figma-coding-agents]] · [[tech-bridge-lauren-tan-2000-prs]]
- [[tech-bridge]] · [[tereza-tizkova]] · [[factory-ai]]
