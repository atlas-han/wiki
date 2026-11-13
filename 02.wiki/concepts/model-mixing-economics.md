---
title: 모델 혼합의 경제학 (Model Mixing Economics)
type: concept
category: framing
tags: [model-selection, cost, planning-vs-execution, agent-swarm, budget]
aliases: [모델 혼합, 계획 모델과 실행 모델, 모델 라우팅]
related: [cloud-agent-delegation, grok-4-6, plan-to-ticket-pipeline, compute-constrained-growth, harness-engineering, model-harness-knowledge-stack, value-maxing, system-1-model, jev, open-model-customization-loop, speculative-decoding, pareto-surfing]
first-seen: tech-bridge-cursor-legacy-refactoring
sources: [tech-bridge-cursor-legacy-refactoring, tech-bridge-grokbot-agent-teams, tech-bridge-mousepower-measuring-agents, tech-bridge-lauren-tan-trusting-agents, tech-bridge-voice-agent-failure-modes, tech-bridge-lopopolo-agent-harness, tech-bridge-tokenmaxxing-to-valuemaxxing, tech-bridge-oracle-agent-memory-harness, tech-bridge-jev-agent-harness, tech-bridge-nadella-copilot-autopilot, tech-bridge-factory-software-factory, tech-bridge-kimchi-cost-per-task-harness, tech-bridge-factory-bug-report-to-production, tech-bridge-fireworks-train-to-deploy-open-models, tech-bridge-just-in-time-ontology, tech-bridge-parakhin-shopify-ai-cost-barbell, tech-bridge-nick-saraev-gpt-6-1-terra-vs-opus-5-5, tech-bridge-greptile-daksh-gupta-build-review-agent, tech-bridge-salesforce-claude-code-agentic-shift, tech-bridge-nick-saraev-karpathy-ai-habits, tech-bridge-lance-martin-old-prompts-make-claude-worse, tech-bridge-addy-osmani-which-claude-model]
created: 2026-09-09
updated: 2026-11-13
---

# 모델 혼합의 경제학

**한 작업 안에서 단계마다 다른 모델을 쓰는 것이 성능이 아니라 예산의 문제로 다뤄진다**는 프레이밍.

> **하나의 더 무거운 모델을 계획(planning)에, 더 실행 중심인 모델을 실제 코드 작성에** 쓰는 것이 전체 예산에 정말 유용합니다. — [[tech-bridge-cursor-legacy-refactoring]]

## 실제 선택이 두 번 시연된다

| 단계 | 고른 모델 | 이유 (소스의 표현) |
|---|---|---|
| **계획** | GPT-5.6 계열 | *"글쓰기에 정말 좋은 모델"* · *"Grok보다 더 나은 작가"* |
| **실행·편집** | [[grok-4-6\|Grok 4.6]] | *"더 빠르고 효율적인 걸 원하니까"* |

그리고 **피하는 선택**도 명시된다:

> 저는 여기서 보통 **[[anthropic|Anthropic]] 모델은 피합니다. 비싸질 수 있어서요.**

## 클라우드는 압력이 더 강하다

> cloud agent는 오래 걸릴 수 있고 **스크린샷과 비디오를 돌려주기 때문에 일반 로컬 에이전트보다 토큰을 더 씁니다.** 그래서 **더 싸고 빠른 모델**을 쓰는 게 좋습니다.

즉 [[cloud-agent-delegation]]의 자기 검증 기능이 **토큰 비용을 올리고, 그것이 모델 선택을 되밀어낸다.** 기능과 경제가 맞물리는 자리다.

⚠️ 주장된 수치 — **마이그레이션 전체에 3~4달러.** 조건(규모·레포)이 명시되지 않는다.

## SQLite 케이스 스터디

> 우리 **에이전트 스웜** 덕분에 이 모델들의 조합으로 SQLite를 재구축할 수 있었고 **Fable 단독이나 GPT-5.5 단독보다 훨씬 저렴했습니다.**

> **모델은 각기 다른 것을 잘하고 각기 다른 것에 활용되어야 합니다.**

⚠️ **수치가 없다.** *"훨씬 저렴"* 뿐이고 블로그 링크는 채팅으로 넘겼다고만 한다. 벤치마크 차트는 화면에만 있고 자막에 값이 없다.

## 이 위키에서의 자리

[[grok-4-6]] 페이지가 이미 기록한 **가격이 곧 병렬성**이라는 논리의 연장이다. 저기서는 *봇 팀을 유지하려면 작업당 비용이 한 자릿수 달러여야 한다* 는 조직 예산의 문제였고, 여기서는 **한 작업 내부에서 단계별로 모델을 갈아 끼우는** 형태로 나타난다.

그리고 이것을 가능하게 하는 것이 [[harness-engineering|하네스]]다 — Cursor는 플랫폼과 모델 사이의 층(도구 실행·캐시 관리·동적 컨텍스트 관리·컨텍스트 조립)을 **cursor harness**라 부르고, 모델 교체가 그 층 위에서 일어난다.

> ⚠️ **당사자 진술.** 모델 유연성을 파는 회사가 모델 유연성이 중요하다고 말하는 구조다. 경쟁 모델의 가격·성능 비교도 판매자 진술이며 독립 확인이 없다.

## 두 개의 새 사례 (2026-09-12)

**Coinbase** — [[tech-bridge-mousepower-measuring-agents]]가 드는 반례. CEO가 X에 올린 차트로, **내부적으로 어떤 모델로 시작할지 기본값을 바꾸고 프런티어 모델을 가장 어려운 작업에만 남겼더니 AI 지출이 토큰 사용량에서 갈라지기 시작**했다. 다만 평가는 유보적이다 — *"좋은 출발이지만 문제는 여전히 토큰에 너무 집중돼 있다"*(→ [[overspending-underusing-loop]]). **수치는 자막에 없다.**

**"Fable 급이 아닌 에이전트"** — [[tech-bridge-lauren-tan-trusting-agents]]가 믹스의 **다른 방향**을 제시한다. 모델을 고르는 대신 **코드베이스를 고쳐서 작은 모델이 통하게** 만든다:

> **토큰을 써서 가장 순진하고 가장 멍청한 에이전트조차 일을 잘하도록 코드베이스를 세팅할 것인가.** 그 지점에 도달하면 **Fable 급이 아닌 에이전트조차 코드를 아주 훌륭하게 씁니다.**

→ [[shortest-path-architecture]] · [[dune-architecture]]

그리고 [[grok-4-6|Grok 4.6]]에 대한 방향 진술이 반복된다 — *"가장 큰 모델을 만들고 싶은 게 아닙니다. 돌리는 데 극도로 비싸니까요. 거대할 필요 없이 아주 똑똑하면서 추론 비용이 크지 않은 스위트 스팟."* ⚠️ 가격 진술(*"토큰당 비용이 4.5와 같다"*)에는 **화자 본인의 유보**가 붙어 있다.

## 세 번째 분할 축 — 대화 vs 도구 호출, 그리고 기준이 지연일 때 (2026-09-19)

[[tech-bridge-voice-agent-failure-modes]]가 모델을 가르는 **세 번째 축**을 준다. 지금까지는 *계획/실행*(Cursor)과 *스웜 내 역할*(Grok)이었는데, 보이스 에이전트에서는 **대화 / 도구 호출**로 가른다.

> 사람들은 **여러 모델을 혼합해서 에이전트를 구축**합니다. **대화 부분에서는 훨씬 더 작은 규모의 대화형 모델**을 사용하고, 어쩌면 **[3B] 모델**도 사용하는 반면, **도구 호출 부분에서는 훨씬 더 큰 규모의 모델을 사용하여 도구 호출 성공률을 향상**시키는 것입니다. (12:53~13:18)

**그런데 이 도메인에서는 가르는 기준이 예산이 아니라 지연이다.** 대화는 사용자가 기다리는 앞단이라 작아야 하고, 도구 호출은 뒤에서 도는 부분이라 클 수 있다. → [[time-to-first-audio]]

그리고 이 페이지가 전제해 온 *더 비싼 모델을 어디에 쓸까* 라는 선택 자체가 **좁아진다**:

> **음성 [에이전트]의 아이러니는 … 사고(thinking) 기능을 꺼야 한다는 점이죠. 그러니까 지난 1년 동안 LLM [계층]에서 이루어진 모든 발전은 이제 여기에는 전혀 적용되지 않는다는 거죠?** (06:53~07:11)

→ [[voice-latency-thinking-tradeoff]]

**조달의 벽도 다르다.** 프런티어 API의 문제는 가격이 아니라 **꼬리 지연**(P50 450~500ms인데 P90·P95가 1.2~1.3초)이고, [[cerebras]]·[[groq]]의 전용 용량은 *"12개월 선예약"* 이라 **모델 수명보다 계약이 길어진다.** 그래서 이 소스의 결론은 **오픈소스 소형 모델 자체 호스팅**([[qwen3-5|Qwen 3.5]]·[[gemma-4|Gemma 4]])이고, 선택 기준에 **[[token-fertility|토크나이저]]** 가 들어온다 — 다국어에서는 단어당 토큰 수가 곧 지연이다.

⚠️ **비용이 한 번도 계산되지 않는다.** *비용·지능·지연* 삼각형을 내세우면서 자체 GPU 호스팅이 프런티어 API 대비 얼마인지 수치가 없다 — 이 페이지의 주제인 축이 정작 비어 있다.

## 일에 맞는 모델을 맞는 가격에 — Salesforce · Karpathy (2026-11-08 · [[tech-bridge-salesforce-claude-code-agentic-shift]] · [[tech-bridge-nick-saraev-karpathy-ai-habits]])

- Salesforce(해설 전달): 가장 큰 실수가 뭐였냐는 질문에 *"일에 맞는 모델을 맞는 가격에 쓰는 것."*(05:26~05:28) 평범한 파일 하나에 무거운 모델을 쓰는 사람들이 있었다. 9월 글의 원칙은 *"일상적인 일은 가벼운 모델로 가장 강력한 모델은 정말 어려운 문제에만"*(05:34~05:36) — 24시간 버그는 *큰 모델이 맞았던* 경우다. 비용 쪽 지표는 [[effective-output-metric|점수당 비용]].
- Karpathy(Saraev 전달): Opus 5.5 medium effort가 Sonnet 서브에이전트들에게 위임하는 구조를 좋아한다 — *"Opus 5.5 maybe on medium effort delegating to a bunch of Sonnet subagents."*(04:18~04:22) 데이터 작업은 Claude가 만든 싼 필터로 먼저 거른다.
- ⚠️ 둘 다 원칙 진술이고 비용 수치는 없다.

## 두 번째 손잡이 — 똑똑한 모델을 덜 애쓰게 (2026-11-09 · [[tech-bridge-lance-martin-old-prompts-make-claude-worse]])

[[lance-martin|Lance Martin]] 워크숍 해설(⚠️ 벤더 자기 실험의 2차 전달). 원칙: *"똑똑한 모델을 덜 애쓰게 하는 쪽이 덜 똑똑한 모델을 오래 고민시키는 것보다 싸고 잘한다는 거예요."*(05:02~05:06) 조언: *"맥스로 시작하지 말고 오퍼스 5.1 로우 부터 시작해 보라."*(05:22~05:26)(⚠️ *5.1* ASR 미확정)

- ⭐ 이 페이지는 주로 **모델 크기**(계획은 큰 모델, 실행은 작은 모델)를 다뤄 왔다. 이 편은 **노력(effort) 수준**을 따로 떼어 같은 비교 축에 올린다 — 블로그 예: Cursor bench에서 Fable 5.1 낮은 노력 = Fable 5 높은 노력, 비용 3분의 1(05:14~05:19).
- 그러나 같은 영상의 고객센터 실험 사다리는 **더 작은 모델로 내려간다**(Opus 4.8 높음 4.6센트 → Opus 5.0(ASR) 낮음 1.9센트 → Sonnet 5 낮음 1센트, 시험용 78.6% → 90.5%). 두 결론(*큰 모델 · 낮은 노력* vs *작은 모델로 하강*)은 충돌하지 않고, **노력을 먼저 낮추고 그다음 크기를 낮춘다**로 읽힌다(위키의 읽기). → [[climbable-eval]]
- ⚠️ 시험 세트 14건. 11-04 Greptile 편의 *혼합의 안전장치는 평가 셋이다*와 같은 구조로, 여기선 그 평가 셋이 학습/시험으로 나뉘어 있다.

## References

- [[tech-bridge-cursor-legacy-refactoring]] · [[cursor]] · [[grok-4-6]] · [[tech-bridge-grokbot-agent-teams]]

## 루프 횟수가 곱하는 비용 (2026-09-23 · [[tech-bridge-lopopolo-agent-harness]])

지금까지 이 페이지의 축은 **단계 배분**(계획은 비싼 모델, 실행은 싼 모델)이었다. 스미타가 **루프 횟수**라는 축을 더한다.

> 에이전트는 디렉터리를 검사하고, 함수를 업데이트하고, 단위 테스트를 실행한 다음, **하나의 작업을 완료하기 위해 해당 시퀀스를 20번, 40번 또는 심지어 60번 반복**할 수 있습니다. 따라서 **연속적인 홉을 많이 사용하는 경우 속도와 비용이 급격히 증가합니다.** 따라서 **빠르고 비용 효율적인 모델은 결코 성능 저하를 의미하지 않습니다.** (26:29~26:50)

→ [[model-harness-knowledge-stack]]. ⚠️ **당사자 발표(Gemini 3.8 Flash 소개)이고 수치가 없다.** 그리고 **약한 모델이 홉 수 자체를 늘릴 가능성**(비용 = 홉 수 × 단가)을 다루지 않는다. 같은 에피소드에서 하네스 쪽은 **Antigravity `/boost`를 "아껴 쓰라"** 고 한다 — 모드 선택도 예산 문제라는 암시지만 말하지 않는다.

## 선택보다 오케스트레이션 — IDC 예측 (2026-09-24 · [[tech-bridge-tokenmaxxing-to-valuemaxxing]])

> **모델 오케스트레이션[이] 모델 선택[보다] 점점 더 중요해지고 있다.** **IDC는 2028년까지 [선도적인] 대규모 AI [배포]의 70%[가] 단 [하나의 모델]에만 의존하는 대신 여러 모델과 함께 작업할 것[이라고] 예측합니다.** (05:48~06:05)

근거가 이 페이지의 *예산* 논리가 아니라 **결과 논리**다 — *"결과가 토큰보다 더 중요[하다면], 시스템이 모델들보다 더 중요해집니다"*(05:43~05:48). 이 페이지에 처음 들어온 **애널리스트 예측**이지만 ⚠️ **예측이고, 출처·정의(무엇이 *선도적 대규모 배포* 인지)가 자막에 없다.**

⚠️ 같은 소스가 *"최신 [모델] 제한"* 을 **실패하는 긴축 정책 목록**에 넣는다(03:12~03:16, → [[token-minimization-trap]]). 이 페이지의 *실행은 싼 모델* 과 어디서 갈리는지는 말하지 않는다. → [[value-maxing]]

## 라우터를 하네스 안에 — 그리고 "절감액의 10%" (2026-09-24 · [[tech-bridge-oracle-agent-memory-harness]])

[[ignacio-martinez|Ignacio Martinez]]([[oracle|Oracle]])가 모델 혼합을 **하네스의 기능**으로 둔다:

> **모델에 결함이 있는 경우**[모델이 형편없으면] (…) **라우터** (…) 어려운 문제는 **[프런티어] LLM**으로 (…) **간단한 문제의 경우, 개방형 가중치 SLM을 할당합니다.** (53:29~53:44)

> 개인적으로 **미래는** (…) **각 유형별 소규모 전문가**[의 혼합] (…) [1억 파라미터 모델] (…) **애그리게이터** (…) [오케스트레이터] (…) **라우팅을 구현할 수 있습니다. [하네스] 내의 모델.** (53:58~54:32)

그리고 이 축에 처음으로 **사업 모델**이 붙는다 — *"일부 회사들은 본질적으로 그것만 한다 (…) 원래 쓰려던 돈에서 **절감해 드린 토큰의 10%를 받겠습니다**"*(54:33~54:45, en-orig 대조; ⚠️ ko는 *"토큰 가격의 10%"* 로 바꿨다). 회사 이름은 말하지 않는다.

이 페이지의 분할 축들(계획 vs 실행, 대화 vs 도구 호출, 루프 횟수가 곱하는 비용)에 **난이도 라우팅**이 더해진다 — 기준이 *단계*가 아니라 **문제의 난이도**다. ⚠️ **난이도를 누가 어떻게 판정하는지**(라우터 자체가 LLM인가)는 말하지 않는다. *소규모 전문가 혼합이 미래*는 **개인 의견**이라고 스스로 단서를 단다(53:58).

## 라우터가 LLM이 아닐 때 — System 1 모델 (2026-09-26 · [[tech-bridge-jev-agent-harness]])

바로 위 절이 남긴 빈칸(*난이도를 누가 판정하나, 라우터 자체가 LLM인가*)에 [[langchain|LangChain]]이 **한 가지 구체적 답**을 낸다 — 라우터를 **텍스트를 생성하지 않는 분류 모델**([[typesafe-ai|TypeSafe]]의 [[jev|Jev]])로 둔다.

> 최근 LangChain에서 탐색하고 있는 예가 있는데, **저희 내부 코딩 에이전트가 주어진 질문이나 코딩 작업의 복잡도에 따라 빠르고 저렴한 모델과 더 비싸고 강력한 모델 사이를 전환**하게 하고 싶습니다. (…) **주어진 기준에 비추어 프롬프트를 평가해 빠른 모델을 쓸지 더 강력한 모델을 쓸지 결정**하는 데 도움을 받을 수 있습니다. 그리고 Jev는 거의 즉시 결정합니다. (06:17~06:44)

라우팅은 **매 요청마다** 일어나므로 라우터의 지연·단가가 절감액을 깎는다 — 라우터가 LLM이면 *싼 모델로 보내기 위해 비싼 판정을 치르는* 역설이 생길 수 있다. 이 소스의 논거가 정확히 그 비용 쪽이다(*"분류형 작업에서 LLM 대비 20~200배 빠르고 40~400배 저렴할 수 있다"*, 02:22~02:34). → [[system-1-model]]

⚠️ **벤더 소개이고 *"탐색 중"*(06:18) 단계다.** 라우팅 정확도, **오라우팅**(어려운 작업을 싼 모델로 보냈을 때)의 비용, 20~200배의 측정 조건이 **전부 없다.** Oracle 편의 *"절감액의 10%"* 사업 모델과 같은 자리를 **모델 제공자**가 노리는 구도지만 소스는 그렇게 말하지 않는다.

## "auto가 제품" — 사용자가 고르지 않는다 (2026-09-29 · [[tech-bridge-nadella-copilot-autopilot]])

이 페이지의 사례는 지금까지 **개발자·팀이 예산을 보고 모델을 섞는** 것이었다. [[satya-nadella|Satya Nadella]]([[microsoft|Microsoft]])는 그 선택을 **제품이 가져간다**고 말한다.

> the last time I picked a model has been a long time because in an interesting way **auto has become the product** essentially (…) the idea that you go in and pick models is becoming pretty passe both (…) in GitHub co-pilot as well as in co-pilot. (08:15~08:31)
> we are even not just doing model routing, but (…) we have **learned routers**, right? So the the real model is **my model that routes**. (08:33~08:41)
> it's about sort of the intensity of the task that then really picks the model. So it's not the user. (…) **your agent picks the model**. (09:10~09:17)

- **라우팅 기준** — 작업 강도(진행자 *"Hard model for hard tasks"* → *"Correct"*, 08:42~08:44). 스웜·서브에이전트에서는 **여러 모델 패밀리를 넘나들며 KV 캐시 적중률**까지 최적화해야 하고, 그것이 *"much easier in coding"*, 지식 노동·사이버에서는 아직 과제다(08:45~09:02). ⭐ 이 페이지에 **캐시**가 라우팅 변수로 처음 들어온다 — 모델을 자주 바꾸면 캐시가 깨진다는 **라우팅의 숨은 비용**.
- **구조** — *"the model router plus a model that we have trained together in a harness. And our harness is capable of calling all the other models"*(09:45~09:53). 자체 **MAI 모델**이 더 강한 모델로 **넘기는** 역할이라 구조상 사용량이 가장 많다. Oracle 편의 *"라우터를 하네스 안에"* 와 같은 모양이고, 라우터가 **학습된** 모델이라는 점은 Jev 편(System 1)과 같은 방향이다.
- **모델 간 경쟁** — *"every model … needs to compete … for handling tasks inside of the Copilot system"*(10:19~10:25). OpenAI(Astra)·Anthropic·Grok이 한 라우터 아래에 있고, 고객은 **자기 모델(BYO)** 을 넣을 수 있다(11:01~11:10).
- ⚠️ **당사자 진술, 측정 없음.** 라우팅 정확도·오라우팅 비용·사용자가 모델을 고정할 수 있는지 **전부 없다.** ⚠️ ko가 *learned routers* 를 **"스마트 라우터"**, *auto has become the product* 를 **"자동 조종 장치 자체"**(Autopilot과 혼동), *KV cache hit ratios* 를 **"지식 캐시 조정"** 으로 옮긴다.

## 라우터의 4단계 — 임계값 위 최저가 (2026-10-02 · [[tech-bridge-factory-software-factory]])

[[factory-ai|Factory]]의 [[tereza-tizkova|Tereza Tížková]]가 자사 **automatic model routing** 을 단계별로 설명한다 → [[automatic-model-routing]] (신규). ① 할당(조직이 사람별 권한·**기본 모델**을 준다 — 마케팅·영업·엔지니어) ② **난이도 분류**(프롬프트 구조·코드베이스·도구, *"This is the magic of the routing"* 07:33) ③ 임계값 ④ *"you choose the cheapest model above the threshold"*(07:54~07:59). 실패·공급자 장애 시 전환 — 라우터의 이점을 비용만이 아니라 **신뢰성·속도(오픈 모델이 빠르다)** 로 든다(06:37~06:51).

같은 발표의 **Coinbase** 읽기: 이 페이지의 기존 서술(*기본 모델을 바꾸고 프런티어를 가장 어려운 작업에만*)에 레버 셋이 더해진다 — **캐싱**(*"to stop prefilling the stuff every time"* 05:49~05:51), **지출 한도 없이 결과 요구**(05:51~05:55), **라우팅**(05:57~06:06).

> ⚠️ *"You can save for example 25% but even more probably"*(07:03~07:09) — *"very conservative"* 라는 자사 벤치마크, 구성 미발화. 캐싱 질문에는 *"just a pricing decision. It's not a technical challenge because everyone can do caching"*(09:15~09:22)로 답했다 — 과제 중간 모델 전환이 캐시를 깨는 비용은 말하지 않는다(위 Nadella 편 *KV 캐시 적중률* 과 긴장).

## "상용은 엣지 케이스에만, 나머지는 오픈소스" — 작업당 비용으로 (2026-10-09 · [[tech-bridge-kimchi-cost-per-task-harness]])

[[cast-ai|Cast AI]]의 [[kimchi|Kimchi]] 발표 부제가 이 페이지의 한 줄 요약이다: *"proprietary models for edge case but use open source for the rest"*(00:12~00:17). 근거로 든 대학 연구(미특정) 표는 **토큰 단가와 작업당 비용이 다른 순서**라는 것 — Gemini 3 Flash *"$3.5 per million token"* vs 작업당 ⚠️ *"$75"*(en-orig) / *"$705"*(`en`·ko), MiniMax 2.7 토큰 *"1.5"* vs 작업당 *"$148"*(03:27~03:59). *"They don't cost the same, but they also not the same per task."*(04:05~04:08)

혼합의 결과로 제시된 곡선은 [[overspending-underusing-loop]]의 Coinbase 차트와 같은 모양 — **토큰 1.5배↑, 비용 1.5배↓**(05:06~05:21, 자사 3개월). ⚠️ 화자는 이를 *"2.5 times"* 절감이라 부르지만 1.5×1.5 = 2.25.

## 벤더의 수치 한 쌍 — GPT 5.2 = Opus 반값, 오픈소스 10~30x (2026-10-17 · [[tech-bridge-factory-bug-report-to-production]])

[[davis-palmie|Davis Palmie]]([[factory-ai|Factory]]): *"We found, for instance, that you can achieve the same performance on code review with GPT 5.2 as with the latest Opus models, but at half the price."*(08:13~08:22) 오픈소스 대안은 *"that can slash your cost down to 10 to 30x cheaper."*(08:26~08:30)이다. 원칙으로는 *"Not being locked into a single lab means you unlock the entire Pareto frontier of LLMs."*(08:38~08:44) CEO의 비유도 든다: *"if your kid needs a algebra tutor, you can definitely find someone cheaper than Albert Einstein."*(03:19~03:26)

⚠️ 과제·벤치마크·Opus 버전·오픈소스의 기준 모델은 발화되지 않는다. 같은 회사 Tereza 편의 라우터 4단계는 이번엔 *"dynamically routed"*(03:48~03:51) 한 구절로만 나온다 → [[automatic-model-routing]]

## 고르는 것에서 고치는 것으로 — 오픈 모델 맞춤 학습 (2026-10-18 · [[tech-bridge-fireworks-train-to-deploy-open-models]])

[[fireworks-ai|Fireworks AI]] 발표는 손들기로 시작한다: *"How many of you feel like it's getting really expensive really quickly? Okay. That's that's a good percentage of you all."*(00:11~00:20) 같은 비용 압력이 여기서는 단계별 모델 선택이 아니라 **폐쇄형 → 오픈 모델 전환**으로 간다. 전환의 병목은 품질이고(*"their biggest bottleneck or the gap is quality"* 07:03~07:05), 처방은 오픈 모델을 자기 데이터로 학습하는 것이다 → [[open-model-customization-loop]]. Kimchi·Factory가 오픈 모델을 **싼 실행 모델로 고르는** 쪽이라면, 이쪽은 **학습해서 격차를 닫는** 쪽이다. ⚠️ 학습 비용과 손익분기는 발화되지 않았다.

## 셋째 역할 — hill climber (2026-10-18 · [[tech-bridge-just-in-time-ontology]])

[[hrishi-olickel|Hrishi Olickel]]은 계획/실행 분할에 셋째 역할을 더한다. 데이터 작업에서 지능은 *"three separate roles that coding agents kind of mash into one context window"*(08:31~08:34)를 맡는다.
- **설계**: *"slower models with heavier, thicker tokens (…) Opus or up."*(09:07~09:22)
- **작업**: *"cheaper, faster, specialized, good at following instructions, repeatable workers with noble[=known] defects."*(09:28~09:33). 두 역할은 *"pull in very different directions"*(09:03~09:05)다.
- **hill climber**: 파이프라인을 스스로 최적화하는 모델 → [[pareto-surfing]]

수치 한 쌍(⚠️ 자기 보고): *"the cheap reasoning model on its own did as well as Fable for about 2% of the cost"*(11:20~11:26, 모델명·Fable 버전 미발화). 그리고 오하이오 작업 전체가 예상 약 $10,000 대신 $795였다(12:19~12:40). 비유는 잎꾼개미의 *"four different sizes of worker (…) Small, medium, high, extra high"*(09:38~09:42)다.

## 바벨 — 단계가 아니라 개발 / 운영으로 가른다 (2026-10-28 · [[tech-bridge-parakhin-shopify-ai-cost-barbell]])

[[mikhail-parakhin|Parakhin]]([[shopify|Shopify]] CTO)의 처방: *"always use this dichotomy barbell strategy for anything coding, for anything development, testing, auto research. Use the largest model. Budget for it (…) For everything production, use fine-tuning, use the right model for that production, auto research the hell out of it so that you balance both cost throughput and and quality."*(07:29~07:55)

이 페이지의 혼합은 대부분 **한 작업 안에서** 계획 모델과 실행 모델을 나누는 라우팅이었다. 바벨은 축이 다르다. **조직의 활동을 탐색(개발 · 테스트 · 연구)과 서빙(운영)으로 가른다.** 탐색 쪽은 비용을 아끼지 않고, 절감은 전부 운영 쪽에서 한다. 운영 쪽 끝은 10-18 [[tech-bridge-fireworks-train-to-deploy-open-models|Fireworks 편]]의 *고르는 것에서 고치는 것으로*(맞춤 학습)와 같은 자리다.

⚠️ 개발 단계의 *"Use the largest model"* 은 이 페이지의 라우팅 수치들(임계값 위 최저가, 오픈소스 10~30x 저렴)과 부딪친다. 화자의 근거는 측정이 아니라 *"you don't know the counterfactual"*(07:24~07:26)이다. 당사자 진술이고 수치가 없다.

## 사용자 결론으로서의 혼합 — "90퍼센타일은 싼 모델, 최상단은 비싼 모델" (2026-11-02 · [[tech-bridge-nick-saraev-gpt-6-1-terra-vs-opus-5-5]])

[[nick-saraev|Nick Saraev]](추정)의 [[openai-terra|GPT-6.1 Terra]] vs [[claude-opus-5-5|Opus 5.5]] 비교 결론은 단계별이 아니라 **작업 등급별** 분할이다: *"I would absolutely use 6.1 Terra for computer use as well as probably most like 90th percentile applications."*(11:13~11:23) · *"on upper echelons of quality, you know, it doesn't really hold a candle to Opus 5.5, especially in some design applications."*(11:28~11:35) 근거는 데모의 *"great up to a certain level of complexity"*(06:09~06:14)와 비용 대비 점수 그래프(*"90, I don't know, 7%[=97%] of performance for 1/9 or maybe 11% cost"* 10:04~10:12)다. 사실 오류율이 가장 낮다는 그래프를 근거로 *"daily driver for most conversations"*(11:08~11:11)도 Terra에 준다. ⚠️ 1인 판단 + 출처 미표기 그래프. → [[cost-vs-score-frontier]]

## 리뷰 제품의 배분 — 프런티어 20%, 하위 작업 20개 (2026-11-04 · [[tech-bridge-greptile-daksh-gupta-build-review-agent]])

[[daksh-gupta|Daksh Gupta]](설명란 근거, [[greptile|Greptile]])의 자사 수치: ⚠️ *"our share today is about 20% frontier models for the most critical tasks."*(13:42~13:45) 나머지 *"long tail of tokens which is exploratory file reads and so on we use a variety of smaller models."*(13:46~13:50) 예시는 작은 모델이 맥락 찾기, 가벼운 computer use 모델이 흐름 시험, 프런티어가 버그 분석 · 리뷰 적용 · 제출이다(14:01~14:12). 실제로는 *"20 different subtasks"*(14:13)이고 조합을 고치는 연구 팀이 따로 있으며, 직접 하면 *"You can probably get 70 to 80% of the way there"*(14:21~14:23)라고 한다.

- ⭐ **혼합의 안전장치는 평가 셋이다** — 좋은 데이터셋 없이 작은 모델로 바꾸면 *"you'll only find out when it misses something that then causes an outage or incident."*(14:43~14:46) 이 페이지의 라우팅 논의에 **바꾼 뒤 나빠졌는지 어떻게 아느냐**가 붙는다. 치명적 버그가 드물수록 늦게 드러난다는 논리다 → [[automated-code-review]]
- **컨텍스트 선별에 작은 모델** — *"In theory, you should be able to use a decision model for this, something like JV or the decisions API to do effective ranking"*(14:59~15:05) ⚠️ *"JV"* 는 [[jev|Jev]] 추정(`en`은 `"Java"`). *"decisions API"* 의 동일성은 [[system-1-model]]의 DevDay 기록과 이름이 같다는 것뿐이다. "in theory"이고 자사 사용이라는 말은 없다.
- ⚠️ 20%의 단위(토큰 · 비용 · 작업)가 발화되지 않고, 절감 폭도 없다. 작은 모델이 오픈 모델인지는 단정할 수 없다. 프런티어가 오픈 모델보다 낫다면서 *"the rubber band is tightening."*(13:40)이라고 덧붙인다.
- [[review-model-inversion]]과 함께 읽으면 **혼합의 이유가 둘**이다(비용, 상관 실패 깨기). 둘이 충돌할 때의 순서는 발화되지 않았다.

## 2026-11-13 — 섞기의 숨은 비용 네 가지 ([[tech-bridge-addy-osmani-which-claude-model]])

[[addy-osmani|Addy Osmani]]의 모델 선택 가이드 해설(⚠️ 원 글 미열람)이 혼합을 권하면서 **섞을 때 드는 비용** 을 함께 적는다.

1. **캐시가 모델에 묶인다** — 모델을 바꾸면 첫 턴에 전체 대화를 다시 캐시에 쓴다 → 전환은 작업 경계에서, Claude Code에선 먼저 `/compact`.
2. **생각 블록이 아래로 안 내려간다** — 상위 모델은 하위 모델의 생각 블록을 읽지만 내려가면 이전 추론은 버려진다. API에선 요약으로 새 대화를 시작하는 편이 낫다.
3. **계획 · 합치기 비용** — 워커 분할(약 2,200만 토큰 결함 탐색, Opus 5.5 지휘 + Sonnet 5.5 워커)은 단독보다 약 1/3 저렴 · 성능 비슷했지만, 앞 단계 의존 작업이나 한 컨텍스트에 들어가는 작업은 *"계획하고 합치는 비용이 절감액보다 큽니다."*(07:09~07:11)
4. **어드바이저** — Opus 5.5 + Fable 5.1 어드바이저는 약 1.7 오르고 비용 약 2.1배 — *"먼저 측정해 보라는 뜻입니다."*(07:25~07:28)

- 서브에이전트는 *틀리면 금방 드러나는 일*(파일 찾기 · 테스트 실행 · 로그 읽기)에 Haiku · Sonnet, 코드 수정 · 판단은 메인에. ⚠️ 작은 모델이 검색 결과를 잘못 읽으면 메인이 엉뚱한 파일을 열어 토큰을 낭비한다 → [[orchestrator-searcher-split]].
- 여러 모델을 함께 쓰려면 가장 엄격한 모델에 맞춰 요청을 구성한다(덧붙이기만 · 도구 선택 자동 · 응답 블록은 타입으로).
- 같은 날 [[tech-bridge-lydia-hallie-rethinking-claude-code-best-practices]]: [[lydia-hallie|Lydia Hallie]]의 구성은 *판단하는 메인 세션 Fable · 작업 스레드 Opus 5.5* — 이 가이드의 *상위 모델이 쪼개고 판단* 과 같은 모양.
