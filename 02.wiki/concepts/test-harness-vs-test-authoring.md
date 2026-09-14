---
title: 테스트 작성과 테스트 하네스 구축의 분리 (Test Authoring vs Test Harness)
type: concept
category: framing
tags: [testing, fuzzing, verification, coding-agents, quality]
aliases: [퍼징 하네스, 올바른 테스트를 고르는 일]
related: [verification-bottleneck, agent-verification-skill, verification-cost-asymmetry, generator-evaluator-pattern, decision-quality]
first-seen: tech-bridge-ambitious-software-agent-era
sources: [tech-bridge-ambitious-software-agent-era]
created: 2026-09-14
updated: 2026-09-14
---

# 테스트 작성과 테스트 하네스 구축의 분리

**"무엇을 테스트할지 고르는 일"과 "테스트를 돌릴 장치를 만드는 일"은 다른 작업이고, 에이전트는 후자에서만 탁월하다.**

[[tech-bridge-ambitious-software-agent-era]]가 이 구분을 처음 명시적으로 긋는다.

| 작업 | 평가 | 근거 |
|---|---|---|
| **올바른 테스트를 고르기** | ❌ | *"어떤 API에 대해서든 테스트를 쉽게 쓸 수 있지만, **인간과 마찬가지로 올바른 테스트를 쓰는 데는 실패**합니다"* · *"**생성자를 주면 생성자를 테스트**하는데 그건 그리 흥미로운 테스트가 아닙니다"* |
| **테스트 아이디어의 대화 상대** | ⚠️ | *"커버리지를 확인할 **테스트 아이디어를 떠올리고 예외 상황을 열거**하는 데는 훌륭한 대화 상대가 되기도 합니다"* |
| **테스트 하네스·퍼징 장치 구축** | ✅ | *"코딩 에이전트로 테스트를 하면서 **정말 만족한 자리**"* — **수백만 가지 입력, 자주 적대적인 입력** 아래 애플리케이션을 두는 장치 |

> **퍼징은 프로덕션급 소프트웨어를 만드는 데 결정적인 부분**인데, 이는 **애플리케이션을 수백만 가지 서로 다른 입력, 그것도 자주 적대적인 입력 아래에 두는 것**을 뜻합니다. **잘못된 형식의 입력이나, 사용자가 그렇게 쓰면 안 되지만 쓸 수는 있는 방식들**이죠. **코딩 에이전트는 이런 하네스를 만드는 데 탁월합니다.** (15:17~15:48)

## 왜 갈리는가

소스는 이유를 명시하지 않지만 구조가 답을 준다.

- **테스트 선택은 의도의 문제다.** *이 시스템에서 무엇이 깨지면 안 되는가* 는 코드 안에 없다. → [[decision-quality]]
- **하네스 구축은 기계적 문제다.** 입력 공간을 어떻게 생성하고, 크래시를 어떻게 잡고, 재현을 어떻게 최소화하는가 — **정답이 있고 문서가 있다.** → [[agents-as-patient-specialists]]

그래서 **퍼징이 특히 잘 맞는다** — 퍼징은 **무엇을 테스트할지 고르는 일을 무작위성에 넘기는 기법**이다. **선택 문제가 사라진 자리에서 에이전트가 가장 잘한다.**

## 검증 논쟁의 세 번째 답

이 위키에 [[verification-bottleneck|병목은 검증]]에 대한 답이 셋 모였다.

| 답 | 소스 | 처방 |
|---|---|---|
| **작업을 고른다** | [[tech-bridge-mousepower-measuring-agents]] (09-12) | 검증이 비싼 작업은 에이전트에게 주지 마라 → [[task-entropy-matrix]] |
| **역량을 짓는다** | [[tech-bridge-lauren-tan-trusting-agents]] (09-12) | 검증을 **스킬로 만들어** 에이전트에게 넘겨라 → [[agent-verification-skill]] |
| **일을 쪼갠다** | **이 개념** (09-13) | **무엇을 검증할지는 사람이, 검증 장치는 에이전트가** |

세 번째가 앞의 둘과 다른 점은 **에이전트에게 넘기는 것이 판정이 아니라 도구**라는 데 있다. Lauren Tan의 검증 스킬이 *에이전트가 앱을 띄우고 확인하게* 한다면, 여기서는 **에이전트가 만든 장치를 사람의 기준이 운전한다.**

09-09 이래 이 위키가 반복 표시해 온 **평가자의 독립성 문제**(작성자=검증자)를 **구조적으로 피하는** 답이기도 하다 — 퍼징 하네스는 **의견을 내지 않는다. 크래시를 낼 뿐이다.**

## 소스가 닫지 않은 것

- ⚠️ **퍼징으로 무엇을 잡았는지 사례가 없다.** 발견 건수·종류가 없다.
- ⚠️ **엔드투엔드 테스트의 어려움은 그대로 남는다** — *"확장이 zed에 제대로 설치돼 작동하는지는 말 그대로 zed를 열어 보지 않고서는 테스트하기 어렵다"*, *"코딩 에이전트도 여기서는 어느 정도 고전한다."* **이 위키의 [[agent-verification-skill]](에이전트가 앱을 실제로 띄운다)과 긴장 관계**이고, 소스는 두 접근을 비교하지 않는다.
- ⚠️ **"허술한 테스트"의 판정도 사람 몫**이다. 그 판정을 자동화하는 방법은 논의되지 않는다.

## References

- [[tech-bridge-ambitious-software-agent-era]] · [[jonathan-kelley]] · [[dioxus]]
- 관련: [[verification-bottleneck]] · [[agent-verification-skill]] · [[verification-cost-asymmetry]] · [[task-entropy-matrix]] · [[decision-quality]] · [[agents-as-patient-specialists]]
