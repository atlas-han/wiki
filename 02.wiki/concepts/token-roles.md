---
title: Token Roles
type: concept
category: pattern
tags: [agent, token-economics, model-routing, evaluation, memory, anthropic]
related: [generator-evaluator-pattern, self-harness, managed-agents, agent-harness-design, trusted-throughput, agent-distributed-systems, verifiable-goals]
first-seen: tech-bridge-claude-platform-agent-era
sources: [tech-bridge-claude-platform-agent-era]
created: 2026-09-02
updated: 2026-09-02
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

## References

- [[tech-bridge-claude-platform-agent-era]] — [[angela-jiang]] · [[katelyn-lesse]] (Anthropic), 2026-09-01
