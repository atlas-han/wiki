---
title: 세 신원의 분리 — 사용자·애플리케이션·에이전트 (Agent Identity Separation)
type: concept
category: pattern
tags: [identity, access-control, least-privilege, security, agent-safety, parameters]
aliases: [3대 Identity 분리, 에이전트 신원, 에이전트 파라미터 vs 애플리케이션 파라미터]
related: [confused-deputy-attack, lethal-trifecta, bound-parameters, credential-injection-outside-sandbox, agent-governance-layers, multiplayer-agent-context, agent-distributed-systems, secure-tool-evolution]
first-seen: tech-bridge-build-time-vs-runtime-tools
sources: [tech-bridge-build-time-vs-runtime-tools]
created: 2026-09-11
updated: 2026-09-11
---

# 세 신원의 분리

**에이전트 기반 애플리케이션에서는 사용자·애플리케이션(워크로드)·에이전트의 신원을 따로 두고, 에이전트에게는 그중 가장 좁은 접근을 준다**는 설계. 그리고 도구 입력을 **에이전트가 만든 것**과 **에이전트 밖에서 고정한 것**으로 가른다. [[tech-bridge-build-time-vs-runtime-tools]]([[google-cloud|Google Cloud]])에서.

## 왜 — 전통 아키텍처의 전제가 깨졌다

> 전통적 아키텍처에서는 (…) **애플리케이션이 접근을 조금 더 가져도 괜찮았습니다 — 무슨 행동을 할지 정확히 알았으니까.** 하지만 에이전트 기반 애플리케이션에서는 이 규칙이 그렇게 명확하지 않습니다.

애플리케이션은 행동이 고정돼 있어 넓은 권한이 남용되지 않았다. 에이전트는 행동을 고르므로 **애플리케이션의 권한을 에이전트에게 그대로 물려주면** [[confused-deputy-attack|혼동된 대리인]]이 된다.

## 세 신원

| 신원 | 접근 범위 | 근거 |
|---|---|---|
| **사용자** | **애플리케이션에만** | 사용자는 앱을 쓸 뿐 |
| **애플리케이션 (워크로드)** | *"좀 더 넓게"* — 여러 서비스와 통신 | 앱은 무슨 행동을 할지 정해져 있다 |
| **에이전트** | **최종 사용자가 처음에 필요로 하는 데이터에만** | 행동을 스스로 고르므로 가장 좁게 |

> 그 애플리케이션 안에서 도는 **에이전트는 최종 사용자가 처음에 필요로 하는 데이터에만** 접근하면 됩니다.

핵심은 **에이전트 ≠ 애플리케이션**이다. 에이전트가 앱 *안에서* 돌더라도 앱의 워크로드 신원을 쓰면 안 된다. 최소 권한 원칙의 에이전트 판이며, [[agent-distributed-systems]]가 *scoped 권한* 으로 언급한 것의 구체적 형태다.

## 두 종류의 파라미터

신원을 갈랐으면 **도구 입력**도 가른다:

| | 누가 만드나 | 성질 |
|---|---|---|
| **에이전트 파라미터** | 에이전트가 **동적으로 도출** | **신뢰할 수 없는 입력** |
| **애플리케이션 파라미터** | 애플리케이션이 고정 | **사실적 제약(factual constraints)** — 에이전트 통제 **밖**에 둔다 |

> 에이전트 파라미터는 **에이전트가 동적으로 도출하는 신뢰할 수 없는 입력**입니다. 애플리케이션 파라미터는 **에이전트의 통제 밖에 두어야 하는 사실적 제약**입니다.

*사용자 ID* 가 대표 예다 — 에이전트가 *"나는 Avery다"* 라고 도출하면 신뢰할 수 없고, 애플리케이션이 인증으로 확정하면 사실적 제약이다. 이것을 도구에 묶는 기법이 [[bound-parameters]]다.

이 구분은 [[agentic-misbehavior]]의 차단 패턴 *Agent-inferred parameters*(*"cancel my job"* → 이름 유사도로 임의 선택)와 정확히 맞물린다 — 그 패턴은 **에이전트 파라미터를 애플리케이션 파라미터 자리에 쓴 것**이다.

## 이 위키의 다른 접근 제어와의 관계

- [[credential-injection-outside-sandbox]]([[promptql]]) — *에이전트가 말하는 사람의 자격증명으로 행동* 은 **에이전트 신원 = 사용자 신원**으로 놓는 선택이다. 이 개념은 에이전트 신원을 **따로** 두되 사용자 범위로 좁힌다. 결과는 비슷하고(에이전트의 유효 접근 ≤ 사용자), 구현이 다르다(프록시 주입 / 신원 3분할 + 파라미터 바인딩). 두 소스는 서로를 모른다.
- [[multiplayer-agent-context]] — 여러 사람이 한 에이전트를 쓸 때 에이전트가 **자기 신원**을 가지면 권한 상승이 난다. 이 개념의 "에이전트 신원은 최종 사용자 범위로"가 그 대응책이다.
- [[agent-governance-layers]] ①층(결정론적 접근 제어)의 **신원 축**이다.

## ⚠️ 미해결

- **에이전트 신원을 누가 발급·관리하는가** — 소스는 개념만 말하고 IAM 구현은 없다.
- 에이전트가 **여러 사용자를 순차로** 대리할 때 신원 전환은? ([[multiplayer-agent-context]]와 같은 빈자리)
- 애플리케이션 파라미터가 **틀렸을 때** — 사실적 제약이 사실이 아니면? 소스에 없다.

## References

- [[tech-bridge-build-time-vs-runtime-tools]] (first-seen) · [[averi-kitsch]]
- 관련: [[bound-parameters]] · [[confused-deputy-attack]] · [[credential-injection-outside-sandbox]] · [[agent-governance-layers]] · [[agentic-misbehavior]]
