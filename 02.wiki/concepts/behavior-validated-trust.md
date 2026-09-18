---
title: 행동 검증 기반 신뢰 (Behavior-Validated Trust)
type: concept
category: framing
tags: [testing, trust, evidence, observability, authorship]
aliases: [행동 검증, 작성자 신뢰, evidence not authorship]
related: [decision-quality, executable-standards, agent-action-record, generator-evaluator-pattern, cloud-agent-delegation, trusted-throughput, verifiable-goals, named-human-accountability]
first-seen: tech-bridge-ai-era-code-quality
sources: [tech-bridge-ai-era-code-quality, tech-bridge-knowledge-work-agent-infrastructure, tech-bridge-company-brain-security, tech-bridge-lauren-tan-trusting-agents, tech-bridge-shift-left-security-ai-code, tech-bridge-legacy-code-modernization-ai]
created: 2026-09-09
updated: 2026-09-18
---

# 행동 검증 기반 신뢰

**신뢰의 근거가 "누가 썼는가"에서 "무엇을 하는 것이 확인됐는가"로 옮겨간다**는 프레이밍.

> **우리는 "사람이 썼기 때문에 코드를 신뢰하는 것"에서 "행동을 검증했기 때문에 소프트웨어를 신뢰하는 것"으로 옮겨가고 있습니다.** 그것은 미묘하지만 심오한 변화이고, **확신은 신뢰할 만한 작성자(authorship)가 아니라 테스팅을 통한 증거(evidence)에서 옵니다.** — [[tech-bridge-ai-era-code-quality]]

## 테스팅의 지위 변화

> 수십 년 동안 테스팅은 **모범 사례(best practice)** 로 여겨졌습니다. 오늘날 그것은 **품질의 일차적 증거(primary proof of quality)** 가 되고 있습니다.

이유는 단순하다 — AI가 쓴 코드는 **우아해 보이고 주석도 잘 쓰여 있어서** 외형이 신뢰의 신호가 되지 못한다.

> 코드는 **그 행동이 검증된 뒤에야** 올바른 것으로 표시될 수 있습니다.

증거의 목록: **유닛 · 통합 · 계약 테스트, 보안 검증, 성능 테스트, 런타임 모니터링, 옵저버빌리티.**

## 같은 원리가 두 소스에서 따로 나왔다

이 위키가 놓는 연결이다 — 두 소스는 서로를 언급하지 않는다.

| 소스 | 대상 | 같은 말 |
|---|---|---|
| [[tech-bridge-ai-era-code-quality]] (IBM) | 코드 | *작성자가 아니라 검증된 행동을 신뢰하라* |
| [[tech-bridge-knowledge-work-agent-infrastructure]] (Composio) | 에이전트 행동 | *"에이전트가 하는 말을 믿는 대신 그 앱들에 직접 가서 무엇을 했는지 볼 수 있다"* |

→ [[agent-action-record]]가 지식 노동에서의 구현이고, 테스트 스택이 코드에서의 구현이다.

## 그리고 검증자가 작성자일 때

[[tech-bridge-cursor-legacy-refactoring|Cursor 편]]은 이 원리를 **에이전트 자신이 수행하는** 형태를 보여준다 — 원격 VM에서 자기 마우스로 UI를 조작하고 그 비디오를 증거로 제출한다([[cloud-agent-delegation]]).

> ⚠️ **작성자와 검증자가 같은 에이전트일 때 그 증거가 얼마나 독립적인가**는 어느 소스도 제기하지 않는다. [[generator-evaluator-pattern]]이 다뤄온 문제다.

그리고 [[tech-bridge-knowledge-work-agent-infrastructure|Composio 편]]은 반대 방향의 한계를 보여준다 — **모든 검사가 통과해도 *"이게 애초에 나갔어야 했는가"* 는 물어지지 않는다.** 즉 행동 검증은 *올바르게 했는가* 를 답하지 검증하지 *올바른 것을 했는가* 를 답하지 않는다. 그 자리는 [[decision-quality]]가 맡는다.

## 그리고 위키에는 테스트가 없다 (2026-09-10)

[[tech-bridge-company-brain-security]]가 이 개념과 **정면으로 마주 보는** 규칙을 놓는다 — *"모든 변경이 사람의 이름으로 뒷받침되게 하라. 'Claude가 추가했다'는 허용되지 않는다."* → [[named-human-accountability]]. 그런데 묻는 것이 다르다: 이 개념은 *믿어도 되는가*(머지 전), 저 규칙은 *문제였을 때 누구에게 가는가*(사고 후). 둘은 양립하며 어느 소스도 그 구분을 짓지 않는다. 그리고 그 규칙이 드러내는 전제 하나 — **공유 지식에는 테스트가 없다.** 사실의 정확성은 코드처럼 실행해 검증할 수 없으므로, 코드에서는 evidence가 authorship을 대체해도 위키에서는 사람 이름이 마지막 보루로 남는다. 이 개념의 적용 범위가 *검증 가능한 산출물* 에 한정된다는 것이 이 대비로 보인다.

## 검증이 보증하는 범위의 경계 (2026-09-12 Lauren Tan 편)

[[tech-bridge-lauren-tan-trusting-agents]]가 이 개념의 **경계를 정확히 긋는다.**

> [검증은] **에이전트가 좋은 코드를 쓴다는 보장은 아닙니다.** 하지만 **적어도 올바른(correct) 코드**를 쓰게 해 줍니다. **에이전트를 신뢰할 수 있게 되는 데 아주 큰 진전**이죠.

**증거가 보증하는 것은 동작의 올바름까지이고 설계의 좋음은 아니다.** 좋음은 여전히 [[taste-vs-judgment|판단]]의 영역으로 남는다 — 화자도 곡선을 오르는 데 필요한 것을 *"취향과 판단"* 이라고 부른다.

검증의 형태도 구체화된다 — **에이전트가 앱을 실제로 띄우고 CPU 트레이스·힙 스냅샷·시뮬레이터로 직접 확인**하는 것. → [[agent-verification-skill]]

그리고 정적 분석·컴파일러가 같은 신뢰를 준다:

> [Rust의 컴파일러는] **인간 엔지니어가 더 이상 직접 확인하러 갈 필요가 없다는 신뢰와 확신**을 줍니다.

→ [[hard-vs-soft-enforcement]] · [[verification-bottleneck]]

## References

- [[tech-bridge-ai-era-code-quality]] · [[tech-bridge-knowledge-work-agent-infrastructure]] · [[ibm]]
- [[tech-bridge-company-brain-security]] — 사람 이름 규칙과의 대비 · [[named-human-accountability]] (2026-09-10)

## 같은 벤더가 보안 쪽에서 다시 말한다 (2026-09-17)

[[tech-bridge-shift-left-security-ai-code]]의 **첫 번째 원칙**이 이 페이지의 명제를 **보안 어휘로** 반복한다. 두 소스 모두 [[ibm]]에서 왔다.

| | [[tech-bridge-ai-era-code-quality]] (09-08) | [[tech-bridge-shift-left-security-ai-code]] (09-17) |
|---|---|---|
| 문장 | *"사람이 썼기 때문에 → **행동을 검증했기 때문에**"* | *"**결과를 믿어라, 생성만이 아니라**"* |
| 무엇이 신뢰를 속이는가 | **우아해 보이는 코드**(외형) | **컴파일되고 테스트를 통과하는 코드**(통과 이력) |
| 증거로 삼을 것 | 테스트·보안 검증·런타임 모니터링 | **실제 조건에서의 결과** — 권한·데이터 유출·실패 모드 |

보안판이 더하는 것은 **통과 이력도 외형이 될 수 있다**는 지적이다:

> **컴파일도 되고, 실행도 되고, 모든 보안 테스트도 통과합니다. 그래서 우리는 이것이 괜찮다고 생각하지만, 눈에 보이지 않는 아래쪽에 보안 위험이 여전히 남아 있을 수 있습니다.**

그래서 검증 질문이 한 칸 더 내려간다 — *테스트를 통과했는가*가 아니라 **"실제 환경에서 예상되는 결과를 내고 안전하게 동작하는가"**. 실패 모드가 그 예다:

> **시스템이 안전하게 고장나는가(fail safe), 아니면 위험하게 열린 채로 고장나는가(fail open)?**

→ [[shift-left-security]] · [[continuous-security-validation]]

## 같은 벤더가 마이그레이션 쪽에서 세 번째로 (2026-09-18 · [[tech-bridge-legacy-code-modernization-ai]])

[[ibm|IBM]]의 세 번째 진술. [[anna-gutowska|Anna Gutowska]]:

> AI 모델은 (…) **문법적으로는 올바르지만 동작상으로는 잘못된 번역**을 생성할 수도 있습니다. (07:45~07:51)

| | 09-08 품질 | 09-17 보안 | **09-18 마이그레이션** |
|---|---|---|---|
| 무엇이 신뢰를 속이는가 | 우아해 보이는 코드 | 컴파일되고 테스트를 통과하는 코드 | **문법적으로 옳은 번역** |
| 검증 질문 | 행동이 맞는가 | 실제 조건에서 안전한가 | **원본과 같은가** |

세 번째가 다른 점은 **비교 대상이 있다**는 것 — 검증이 기능 검증이 아니라 **동등성 검증**이 된다. 그리고 레거시의 정의(*아무도 완전히 이해하지 못하는 도메인 로직*, 테스트 없음)가 **동등성을 판정할 기준 자체가 없는 상태**를 말하므로, 이 소스의 처방은 테스트 스택이 아니라 *"테스트, 사람 검토 및 검증을 통합하는 잘 설계된 워크플로"*(08:14~08:23)와 [[risk-proportional-human-review|위험한 결정 곁의 사람]]이다. → [[syntactically-correct-behaviorally-wrong]]
