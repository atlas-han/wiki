---
title: 검증 스킬 (Agent Verification Skill)
type: concept
category: technique
tags: [verification, skills, tracing, cdp, correctness, agents]
aliases: [verification skill, 에이전트가 스스로 확인하게 하기]
related: [verification-bottleneck, feature-map, behavior-validated-trust, agent-trust-curve, generator-evaluator-pattern, verifiable-goals, skill-evals, ai-formal-verification]
first-seen: tech-bridge-lauren-tan-trusting-agents
sources: [tech-bridge-lauren-tan-trusting-agents, tech-bridge-lauren-tan-2000-prs]
created: 2026-09-13
updated: 2026-09-26
---

# 검증 스킬

**에이전트가 자기가 쓴 코드를 실제로 돌려서 확인하게 만드는 스킬.** [[lauren-tan]]이 [[tech-bridge-lauren-tan-trusting-agents]]에서 *"에이전트와 일할 때 도구함에 있어야 할 가장 중요한 스킬"* 로 꼽았다.

## 정의

> 검증이란 **에이전트가 실제로 코드를 돌리고, CPU 트레이스나 힙 스냅샷을 뜨고, iOS 시뮬레이터를 열고** — 여러분의 앱이 사용자에게 노출되는 방식이 무엇이든 **그것을 똑같이 하고 실제로 돌려 검증**하는 능력입니다. **그게 루프를 닫는 것**이니까요.

구현은 어렵지 않다고 말한다 — *"코드 자체는 대단히 흥미롭지 않고 여러분의 에이전트가 쉽게 하나 만들어 줄 수 있습니다."* 가르치는 것은 **Chrome DevTools Protocol** 이나 **Apple의 시뮬레이터 실행·트레이스·프로그램적 제어 유틸리티** 사용법이다.

## 경계 — correctness는 주지만 quality는 아니다

> 이게 **에이전트가 좋은 코드를 쓴다는 보장은 아닙니다.** 하지만 **적어도 올바른(correct) 코드**를 쓰게 해 줍니다. **에이전트를 신뢰할 수 있게 되는 데 아주 큰 진전**이죠.

**이 구분이 이 개념의 핵심 기여**다. [[behavior-validated-trust]]가 *증거가 작성자를 대체한다* 고 했을 때 그 증거가 보증하는 범위를 정확히 긋는다 — **동작의 올바름까지이고 설계의 좋음은 아니다.** 좋음은 여전히 [[taste-vs-judgment|판단]]의 영역이다.

## 없을 때의 상태 — 사람이 검증자다

> 검증 스킬 없이 개발하면 — **검증자는 여러분 자신이고, 여러분이 병목**입니다. 에이전트에게 시키면 코드를 쓰고, 여러분이 로컬 dev 빌드를 열어 *"안 되는데요"* 하고, **스크린샷이나 콘솔 에러를 복붙**하고… **병렬화할 방법이 전혀 없죠.**

화자의 첫 경험은 성능 작업이었다 — Chrome DevTools로 직접 플레임 그래프를 읽으려 했는데 **에이전트도 자기도 무엇을 보는지 몰랐고**, 에이전트는 *"자신 있게 '이거다'라고 단정"* 한 뒤 틀렸다. → [[verification-bottleneck]] · [[agent-trust-curve]]

## 두 번째 재료 — 기능 지도

스킬만으로는 부족했다. 에이전트가 앱을 띄울 수는 있어도 **그 앱이 무엇인지 몰랐다.** → [[feature-map]]

## 규모의 효과

검증 스킬은 개인 도구가 아니라 **조직 자산**으로 제시된다 — 클라우드 에이전트가 같은 스킬로 버그를 재현하기 때문이다([[grokbot|Benny]]).

> **한 명의 엔지니어를 낫게 하는 게 아니라 팀 전체, 회사 전체를 레벨업**시키기 때문입니다.

→ [[cloud-agent-delegation]]

## 표시해 둔 것

> ⚠️ **당사자 진술**이고 효과 수치는 자기 보고다. 그리고 **검증 스킬 자체를 무엇이 검증하는가**는 [[skill-evals]]로 넘어가는데, 거기서도 **작성자=검증자 문제**가 닫히지 않는다.

## References

- [[tech-bridge-lauren-tan-trusting-agents]] · [[feature-map]] · [[skill-evals]] · [[verification-bottleneck]] · [[behavior-validated-trust]] · [[agent-trust-curve]] · [[pstack]] · [[lauren-tan]]

## 검증의 스펙트럼, 그리고 스킬 = CLI + feature map (2026-09-26 · [[tech-bridge-lauren-tan-2000-prs]])

같은 화자의 녹화 발표가 두 가지를 더한다.

**① 스펙트럼의 반대쪽 끝 — 형식 검증.**

> 스케일의 **낮은 쪽 끝**에는 검증 스킬 (…) **반대쪽 끝은 훨씬 어렵고 여전히 열린 문제**인데, **형식 검증** — **Lean, TLA+** 같은 언어로 **비즈니스 로직 불변식이 항상 참인지** 확인하는 것. (…) **형식 기법을 돌릴 능력이 없더라도 — 그런 사람은 아주 적습니다 — 검증 스킬만으로도 아주 멀리 갈 수 있습니다.** (07:12~08:37)

검증 스킬은 **스펙트럼의 싼 쪽 끝**이라는 자기 위치 규정이다. → [[ai-formal-verification]]

**② 두 구성 요소** — *"반복 끝에 도달한 형태이고 처음부터 이렇지는 않았다"*(09:03~09:08):

- **스킬 디렉터리 안의 CLI** — *"에이전트가 **세션마다 달라질 수 있는 스크립트를 매번 만들게 하는 대신**, 스킬 디렉터리 안에 CLI를 만들어 두면 매번 그걸 쓴다"*(09:41~09:56). 목적은 **재현 가능성**과 **경험적 증거**이고, *"거기에 투자해서 좋게 만들어야"* 한다.
- **[[feature-map]]** — *"구체화된 기억"*.

**③ 경계가 다시 그어졌다** — *"검증은 정확성에 관한 것 (…) 성능이나 코드 품질에 대해서는 많은 걸 말해 주지 않는다"*(12:36~13:11). 빈칸은 **경험 많은 엔지니어가 만드는 품질 스킬**([[pstack]])이 채우고, **검증과 결합해야** *"정확할 뿐 아니라 품질도 높다"* 를 확인할 수 있다(14:18~14:30).

**기원** — control glass는 Cursor agents window의 **성능 회귀 감시**를 손으로 하던 데서 나왔다(*"PR이 랜딩되는 속도로는 넘을 수 없는 PR의 벽"*, 03:08~03:16).
