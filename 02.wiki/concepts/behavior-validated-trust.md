---
title: 행동 검증 기반 신뢰 (Behavior-Validated Trust)
type: concept
category: framing
tags: [testing, trust, evidence, observability, authorship]
aliases: [행동 검증, 작성자 신뢰, evidence not authorship]
related: [decision-quality, executable-standards, agent-action-record, generator-evaluator-pattern, cloud-agent-delegation, trusted-throughput, verifiable-goals, named-human-accountability]
first-seen: tech-bridge-ai-era-code-quality
sources: [tech-bridge-ai-era-code-quality, tech-bridge-knowledge-work-agent-infrastructure, tech-bridge-company-brain-security]
created: 2026-09-09
updated: 2026-09-10
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

## References

- [[tech-bridge-ai-era-code-quality]] · [[tech-bridge-knowledge-work-agent-infrastructure]] · [[ibm]]
- [[tech-bridge-company-brain-security]] — 사람 이름 규칙과의 대비 · [[named-human-accountability]] (2026-09-10)
