---
title: Token Roles
type: concept
category: pattern
tags: [agent, token-economics, model-routing, evaluation, memory, anthropic]
related: [generator-evaluator-pattern, self-harness, managed-agents, agent-harness-design, trusted-throughput, agent-distributed-systems, verifiable-goals, intelligence-as-infrastructure, compute-constrained-growth, fixed-budget-alpha, all-or-nothing-accuracy, true-cost-to-perfect-answer, strategy-primitives]
first-seen: tech-bridge-claude-platform-agent-era
sources: [tech-bridge-claude-platform-agent-era, tech-bridge-altman-g20-economic-boom, tech-bridge-jensen-huang-g20-agi, tech-bridge-mousepower-measuring-agents, tech-bridge-tokens-should-have-jobs]
created: 2026-09-02
updated: 2026-09-18
---

# Token Roles

**Token roles**는 [[anthropic|Anthropic]] Claude Platform 팀([[angela-jiang|Angela Jiang]]·[[katelyn-lesse|Katelyn Lesse]])이 [[tech-bridge-claude-platform-agent-era|Builders 대담]]에서 제시한 프레이밍으로, 토큰을 **균질한 소모품**으로 보는 대신 **실행 말고 다른 역할(job)을 부여**해 dollar당 지능을 올리는 전략을 가리킨다.

반박 대상은 두 가지 통념이다.

> **모든 토큰이 똑같다**는 건데, 마치 가스나 전기처럼 쉽게 구할 수 있는 것처럼 생각하는 거죠.

> 이런 종류의 **토큰 경제학은 불행히도 현실과 다소 동떨어져** 있는 것 같습니다.

> ⚠️ 이 용어(`token roles`)는 이 위키가 대담의 서술("give tokens different jobs")에 붙인 이름이다. 벤더가 쓰는 제품 용어가 아니다. 아래 세 전략 중 **grading은 `outcomes`라는 실제 제품 기능명**을 갖는다.

## 세 가지 역할

### 1. Advising — 작은 모델이 실행하고 큰 모델이 조언한다

작은 모델이 실행하다가 **문제의 더 어려운 부분**에 부딪히면 큰 모델에 도움을 청한다.

> we've got some evals that show like **sonnet executing with opus advising ends up getting almost opus level performance and it's actually cheaper than just sonnet** because opus taught it how to do its job better and it used less tokens to get the job done.

비용 구조의 주장이 반직관적인 부분이다 — advisor를 **추가**했는데 Sonnet 단독보다 **싸다**. 메커니즘은 Opus가 더 나은 수행 방법을 가르쳐서 **Sonnet이 쓰는 토큰 수 자체가 줄어든다**는 것이다.

> ⚠️ 발표자가 "우리가 본 몇몇 eval"이라고만 말한 **내부 평가**다. 벤치마크 이름·구성·수치가 제시되지 않았고 독립 검증이 없다. 벤더 자사 대담이라는 점도 감안해야 한다.

이는 단순한 model routing(쉬운 건 싼 모델로)과 다르다 — **두 모델이 같은 작업 안에서 다른 역할을 맡는다.**

### 2. Grading — 루브릭을 주면 채점자를 프로비저닝한다

[[managed-agents]]의 **`outcomes`** 기능이다.

> 예를 들어 "좋은 결과는 이렇습니다"와 같은 **루브릭**을 제시하면 그 기준을 충족하는 **두 번째 에이전트를 제공**합니다.

> 첫 번째 담당자가 시도해보고, 그다음엔 '좋아, 해봤는데 아직 충분하지 않네. 다시 해보자'라고 하는 거죠. (…) **채점자와 실행자가 함께** 일을 처리하기 때문이죠.

이것이 [[generator-evaluator-pattern]]을 **플랫폼 기능으로 승격**시킨 형태다. 이 위키의 [[verifiable-goals]]가 요구한 verifier를, 사용자가 직접 만드는 대신 **루브릭만 쓰면 플랫폼이 프로비저닝**한다.

### 3. Dreaming — 과거 세션을 돌아보고 자신을 고친다

> 과거 세션을 되돌아보고 **메모리에 쓰고 개선해야 할 스킬을 작성**하는 또 다른 방법입니다.

[[self-harness]]가 논문에서 제시한 자기개선 루프와 같은 구조이고, [[agent-skills]]가 정적 자산으로 다룬 스킬을 **에이전트가 스스로 쓰는 산출물**로 만든다.

Angela 본인의 수동 버전도 대담에 나온다 — 마음에 안 드는 결과가 나오면 "**그것이 잘못된 일이었다는 것을 기억하세요. 메모리에 저장해 둬**"라고 말하고 저장된 내용을 확인한다.

## 왜 이것이 비용 논쟁의 답인가

대담은 "비용을 줄이려면 오픈소스 모델을 써야 하지 않나"라는 질문에서 출발해 질문 자체를 되돌린다.

> 사람들은 문제를 해결하기 위한 메커니즘으로 **모델**을 찾는 경향이 있는데 (…) 비용에 대한 이야기는 들었지만, **도대체 무엇을 하려고 했던 건가요?**

그리고 결론이 반직관적이다.

> 때로는 역설적이게도 **더 크고 비싼 모델을 사용하는 것이 더 나은 선택**일 수도 있습니다. (…) **모든 토큰이 정확하다면 낭비되는 것이 전혀 없고** 문제를 완벽하게 해결한 셈입니다.

즉 최적화 대상은 토큰 **단가**가 아니라 **intelligence per dollar**다.

> if you give tokens different jobs besides just executing, you can get to a better maybe like **intelligence per dollar** sort of setup than if you were just brute force executing.

[[trusted-throughput]]이 구매자 쪽에서 같은 주에 도달한 결론("토큰 지출은 LOC 같은 지표다")과 정확히 맞물린다. 다만 양쪽 다 **각자의 인센티브가 그 결론과 정렬돼 있다**는 점은 감안해야 한다.

## 전략 계층 = 메타 하네스

토큰 역할 부여는 하네스 **위** 계층에 속한다.

> 하네스는 **루프**인데 (…) 가장 기본적인 형태는 말 그대로 **while 루프**와 같아요.

> 어떤 사람들은 이를 **메타 하네스**라고 부르기도 합니다. 우리는 **'전략(strategy)'**과 같은 단어를 사용했습니다.

그 계층에서 에이전트들을 서로 다르게 조율하고, 소통하게 하고, 서로의 루프에 피드백되게 한다. 그리고 이 계층이 지금 열린 이유가 명시된다.

> 요즘에는 그런 영역에서 알파 버전이 더 많이 만들어지고 있는데, **가장 기본적인 내용들이 어느 정도 이해 가능해졌기 때문**이죠. 오류를 처리하고, 반복문이 제대로 실행되도록 하고, 실행 시간이 길도록 해야 합니다.

즉 [[agent-distributed-systems]]의 신뢰성 문제가 풀려야 이 계층이 열린다 — **순서가 있는 의존성**이다.

> 문제 영역, 도메인, 해결하려는 내용 등을 고려할 때, **이러한 전략들을 실제로 어떻게 조합하느냐에 따라 상당히 다른 성능 결과**가 나타나는 것을 확인했습니다.

## 관련

- [[generator-evaluator-pattern]] — grading의 원형
- [[self-harness]] — dreaming의 원형
- [[managed-agents]] — `outcomes`가 구현된 자리
- [[agent-harness-design]] — 하네스 / 메타 하네스 계층 구분
- [[trusted-throughput]] — 구매자 쪽에서 만나는 같은 결론
- [[agent-distributed-systems]] — 이 계층이 열리기 위한 선행 조건

## 공급자가 단위를 부정한다 (2026-09-07 · [[tech-bridge-altman-g20-economic-boom]])

같은 G20 회의에서 토큰을 두고 두 판매자가 정반대로 말한다.

| 화자 | 토큰은 무엇인가 |
|---|---|
| [[jensen-huang]] | **상품 단위** — *"백만 토큰당 달러. kWh와 **같은 개념이에요.**"* → [[intelligence-as-infrastructure]] |
| [[sam-altman]] | **버려야 할 단위** — *"저는 여기서 토큰이라는 단위를 정말 싫어합니다. **어리석은 단위이고 아무도 신경 쓰지 않아야** 하지만, 그냥 **지능 수준을 나타내는 약어**로 생각해 보자면"* |

이 페이지는 토큰을 **역할**(advising·grading·dreaming)로 봤고 [[trusted-throughput]]은 **연기 감지기**로 봤다. Altman의 진술은 그 둘과 같은 방향이다 — **토큰 자체는 의미가 없고 대용치일 뿐**이라는 것. 다만 그가 곧바로 그 단위로 6년 반 외삽을 한다는 점에서, *부정하면서 쓰는* 형태다. → [[compute-constrained-growth]]

⚠️ 두 입장을 해소하지 않는다. 토큰을 **파는 층**과 토큰을 **소모하는 층**의 차이로 읽는다.

## 토큰은 산출물이지 결과가 아니다 (2026-09-12 마우스파워 편)

[[tech-bridge-mousepower-measuring-agents]]가 토큰의 지위를 한 줄로 정리한다.

> 토큰은 **내부 시스템의 측정값으로는 유용**하지만 **결국 산출물일 뿐**이고, 따라서 **토큰은 결과로 아주 깨끗하게 추적**돼야 합니다. **우리가 산 토큰으로 버그를 몇 개 잡았나? 지원 요청을 몇 개 닫았나?**

지표로 삼았을 때의 병리도 사례로 나온다 — **토큰 리더보드**, 그리고 *"1년 치 토큰 예산을 한 분기에 다 태우는"* 조직. → [[overspending-underusing-loop]] · [[trusted-throughput]]

## References

- [[tech-bridge-claude-platform-agent-era]] — [[angela-jiang]] · [[katelyn-lesse]] (Anthropic), 2026-09-01

## 두 번째 소스 — 처음으로 수치가 붙었다 (2026-09-18 · [[tech-bridge-tokens-should-have-jobs]])

같은 두 화자([[katelyn-lesse]]·[[angela-jiang]])가 [[ai-engineer|AI Engineer]] 무대에서 **같은 세 전략에 벤치 수치를 붙였다.** 09-01의 세 전략이 *말* 이었다면 이번엔 *실험* 이다 — 단, 내부 벤치이고 절반의 수치는 자막에 없다.

전제가 **가설의 형태**로 다시 세워진다:

> 예산을 사용하는 이러한 가정의 기저에는 **모든 토큰이 기본적으로 대체 가능하다(fungible)는 암묵적인 관점**이 깔려 있습니다. (…) 이 토큰들은 모두 실제로 대체 가능한가요? 그리고 이를 검증하기 위해, **토큰에 역할을 부여하면 어떨까** (00:42~00:57)

> 실행 중인 토큰과 다른 작업을 수행하는 토큰을 각각 구분해서, **이를 전략(strategy)이라고 부릅니다.** (01:46~01:54)

### 수치

| 실험 | 실행 | 조언 | 채점 | 회고 |
|---|---|---|---|---|
| one-shot (자율 지출) | **15%** · 39k | — | — | *"정말 잘했다"* · **600k** |
| 고정 예산 600k, 정확도 | **76** | **89** | *"60대 → 90 근처"*(조언과 묶어) | — |
| 고정 예산, **100% 합격률** | **42%** | *"복잡한 전략 최대 75%"* | ← | ← |
| **진짜 비용**(600k × 기대 횟수) | **1.8M** | *"상당히 효율적"* | *"상당히 효율적"* | *"약간의 차이"* |

→ [[fixed-budget-alpha]](왜 예산을 고정하는가) · [[all-or-nothing-accuracy]](왜 100%/실패로 채점하는가) · [[true-cost-to-perfect-answer]](왜 분모가 합격률인가)

### 처방 — 최적화 대상에 따라

| 원하는 것 | 전략 |
|---|---|
| 토큰 효율 | **조언** |
| 신뢰성(완벽한 답의 비율) | **채점 · 회고** |

### 09-01과 대조 — 사라진 것

**Sonnet 실행 + Opus 조언이 Sonnet 단독보다 싸다** 는 이 페이지의 가장 강한 주장이 **이 발표에 없다.** 모델 이름이 역할에 붙지 않고(*Fable* 한 번, 문맥 불명), 비교는 **같은 예산**에서 이뤄진다. 모순은 아니지만 **비용 역전은 되풀이되지 않았다.** *intelligence per dollar* 라는 표현도 **alpha** 와 **진짜 비용**으로 바뀌었다.

### 더해진 것

- 세 **사용 사례**(영업 후속 조치 / 환불 루브릭 / 채용 피드백) — 전부 가상.
- 회고의 정의에 **역할 분리** — 드리머가 실행자의 기록을 읽고 메모리에 쓴다 → [[agent-memory]].
- **메타 하네스가 제품 층**이 됐고 회고·`outcomes`가 기본 제공 → [[strategy-primitives]] · [[managed-agents]].
- 장기 목표: **모델·플랫폼이 전략을 동적으로 구성** → [[self-harness]] · [[dynamic-workflows]]와 같은 방향.

> ⚠️ 이 페이지의 이름 경고는 유지된다 — 발표 제목이 *"tokens should have jobs"* 이지 *token roles* 가 아니다. ⚠️ 벤치의 과제 수·모델·평가자 없음, 채점·회고 수치 없음, 화자 스스로 *"미미한 차이"*. ⚠️ ko가 *executor* 를 **"유언집행자"** 로, *600,000 tokens* 를 **"60만 달러"** 로, *outcomes* 를 **"결과"** 로 옮겼다 — raw 헤더 참조.
