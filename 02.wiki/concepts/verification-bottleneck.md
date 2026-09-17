---
title: 검증 병목 (Verification Bottleneck)
type: concept
category: framing
tags: [code-review, verification, throughput, bottleneck, agents]
aliases: [병목은 검증으로 옮겨갔다, 코드 리뷰 병목]
related: [verification-cost-asymmetry, agent-verification-skill, behavior-validated-trust, trusted-throughput, agent-trust-curve, hard-vs-soft-enforcement, generator-evaluator-pattern]
first-seen: tech-bridge-mousepower-measuring-agents
sources: [tech-bridge-mousepower-measuring-agents, tech-bridge-lauren-tan-trusting-agents, tech-bridge-ambitious-software-agent-era, tech-bridge-pstack-third-party-review, tech-bridge-graft-code-knowledge-graph, tech-bridge-shift-left-security-ai-code]
created: 2026-09-13
updated: 2026-09-17
---

# 검증 병목

**코드 생성이 싸지면서 병목이 생성에서 검증으로 옮겨갔다**는 진단. 2026-09-12에 업로드된 두 소스가 **서로를 언급하지 않으면서 같은 진단에 도달**했다.

## 진단

> **우리 모두가 천 개의 pull request에 치여 죽고 있습니다.** **코딩을 풀었다고 주장하는 사람이 있는 [[anthropic|Anthropic]]조차 코드 리뷰는 풀지 못했다고 인정**했습니다. — [[tech-bridge-mousepower-measuring-agents]]

> **병목이 검증 쪽으로 옮겨가면서 대규모로 가치를 측정하고 같은 속도로 품질을 판정할 방법이 없습니다.**

같은 상태를 개인의 경험으로 말한 것:

> 검증 스킬 없이 개발하면 — **검증자는 여러분 자신이고, 여러분이 병목**입니다. (…) **병렬화할 방법이 전혀 없죠.** — [[tech-bridge-lauren-tan-trusting-agents]]

## 두 개의 답

| | **작업을 고른다** | **역량을 짓는다** |
|---|---|---|
| 소스 | [[tech-bridge-mousepower-measuring-agents]] | [[tech-bridge-lauren-tan-trusting-agents]] |
| 처방 | 검증이 실행만큼 비싼 작업은 **하지 않는다** → [[task-entropy-matrix]] | 검증을 **스킬로 만들어 에이전트에게 넘긴다** → [[agent-verification-skill]] |
| 그다음 | **검증하는 에이전트**를 만든다 | 제약을 **CI로 하드 강제**해 검증을 애초에 줄인다 → [[hard-vs-soft-enforcement]] |
| 화자의 위치 | 판매자(고객의 작업을 고를 수 없다) | 코드베이스 소유자(자기 환경을 바꿀 수 있다) |

→ [[verification-cost-asymmetry]]

## 왜 코드 리뷰는 풀릴 것처럼 느껴지는가

Mousepower 편이 **Noah Hine**(철자 미확정)의 글을 인용해 답한다:

> **문화로서 코드 리뷰는 공유된 가정에 대한 수렴이 아주 좋다** — 모두가 측정에 수렴할 수 있으면 **대규모 측정이 가능해지고 그것이 명확한 루브릭**이 됩니다. 이제 할 일은 **그 가정들을 에이전트 시대에 맞게 적응시키는 것**입니다.

> **컴퓨트 속도의 실행에서 컴퓨트 속도의 측정으로.**

Lauren Tan 쪽의 답은 그 적응의 구체적 형태다 — **사람이 PR 댓글로 강제하던 가정을 CI 실패로 옮긴다.**

## 위키의 다른 페이지와 맞닿는 자리

- **[[behavior-validated-trust]]** — *증거가 작성자를 대체한다* 는 프레이밍의 **처리량 판본**. 증거를 만드는 비용이 병목이다.
- **[[trusted-throughput]]** — 그 지표가 *신뢰하는 결과물* 을 세는데, **신뢰를 붙이는 단계가 바로 이 병목**이다.
- **[[tech-bridge-knowledge-work-agent-infrastructure]]**(Composio) — *"코딩 에이전트만 폭발한 이유는 검증 인프라가 있었기 때문"* 이라는 주장과 정확히 이어진다. 그 인프라조차 **리뷰 단계에서는 아직 부족하다**는 것이 이 페이지의 내용이다.
- **[[tech-bridge-ai-era-code-quality]]**(IBM) — *"완벽한 코드로도 부족하다"* 와 같은 자리. 시스템 수준 품질은 리뷰로 확인되는데 리뷰가 확장되지 않는다.


## 2026-09-15 — 검증 앞에 있는 다른 병목, 그리고 디자인으로의 확장

이날 들어온 두 소스가 이 페이지의 양쪽을 건드린다.

- [[tech-bridge-graft-code-knowledge-graph]]는 **변경 *전*의 병목**을 가리킨다 — [[file-discovery-tax|탐색세]]. 이 페이지가 말하는 병목(변경 *후*의 검증)과 **경쟁하지 않고 작업의 앞뒤를 각각** 차지한다.
- [[tech-bridge-one-designer-plus-ai]]는 검증 병목이 **디자인 조직에서도 성립**함을 보여 준다 — 140곳 스폰서 배너의 **누락 검사**를 에이전트에게 넘긴다 → [[agent-visual-qa]].

두 번째는 **작성자 = 검증자** 구도의 네 번째 사례이기도 하다(배너를 만든 사람이 검수도 시킨다).

## References

- [[tech-bridge-mousepower-measuring-agents]] · [[tech-bridge-lauren-tan-trusting-agents]] · [[verification-cost-asymmetry]] · [[agent-verification-skill]] · [[behavior-validated-trust]] · [[trusted-throughput]] · [[hard-vs-soft-enforcement]]


## 세 번째 답 — 일을 쪼갠다 (2026-09-14 추가)

[[tech-bridge-ambitious-software-agent-era]]가 **검증 작업 자체를 둘로 가른다** → [[test-harness-vs-test-authoring]].

| 답 | 소스 | 처방 |
|---|---|---|
| **작업을 고른다** | [[tech-bridge-mousepower-measuring-agents]] (09-12) | 검증이 비싼 작업은 에이전트에게 주지 마라 |
| **역량을 짓는다** | [[tech-bridge-lauren-tan-trusting-agents]] (09-12) | 검증을 스킬로 만들어 에이전트에게 넘겨라 |
| **일을 쪼갠다** | [[tech-bridge-ambitious-software-agent-era]] (09-13) | **무엇을 검증할지는 사람이, 검증 장치(퍼징 하네스)는 에이전트가** |

> **어떤 API에 대해서든 테스트를 쉽게 쓸 수 있지만, **인간과 마찬가지로 올바른 테스트를 쓰는 데는 실패**합니다.** (…) **코딩 에이전트는 이런 [퍼징] 하네스를 만드는 데 탁월합니다.**

**세 번째가 고유한 점**: 에이전트에게 넘기는 것이 **판정이 아니라 도구**다. 2026-09-09 이래 이 위키가 반복 표시해 온 **평가자의 독립성 문제**(작성자=검증자)를 **구조적으로 피한다** — 퍼징 하네스는 의견을 내지 않고 **크래시를 낼 뿐**이다.

⚠️ **대가가 있다.** 같은 소스가 **엔드투엔드 테스트에서는 에이전트도 고전한다**고 인정하고(*"zed를 열어 보지 않고서는"*), [[agent-verification-skill]](에이전트가 앱을 실제로 띄운다)과 **긴장 관계**에 있다. **두 접근을 비교한 소스는 아직 없다.**

## 검증이 실제로 무엇을 잡았는가 (2026-09-14 추가)

[[tech-bridge-pstack-third-party-review]]에 **관측된 사례**가 하나 있다.

> **E 단계에서 검증 테스트를 전부 하고 감사로 마무리합니다. 바로 이래서 검증이 중요합니다 — **에이전트가 세부 일부를 환각했다는 걸 스스로 깨달았습니다. 시스템이 허위 주장 세 건을 잡아 고칠 수 있었습니다.**** (07:49~08:03)

**이 위키가 기록한 검증 사례 중 "무엇이 몇 건 잡혔는지"가 나온 첫 사례**다. ⚠️ 다만 **세 건의 내용이 없고, 놓친 것이 있었는지도 알 수 없다.**

→ [[test-harness-vs-test-authoring]] · [[agent-arena]] · [[agent-swarm]] · [[minimizing-reader-load]]

## 보안 쪽에서 나타난 같은 병목 (2026-09-17)

[[tech-bridge-shift-left-security-ai-code]]가 사후 보안 검토의 실패를 **이 페이지와 같은 구조**로 진단한다.

> 보안이 프로세스 마지막 단계에서 **사후적으로 추가(retrofit)** 되는 방식으로만 이루어진다면 **품질이 저하되고 전체 프로세스가 완전히 멈춰 섭니다.**

> **코드 생성이 몇 초 만에 이루어질 수 있는 상황에서, 마지막까지 기다리는 것은 병목을 만들고 위험을 키웁니다.**

**두 방향으로 깨진다** — 검토가 형식이 되거나(품질 저하), 검토가 처리량을 못 따라간다(정체). 그리고 양이 늘면 상황이 나빠진다:

> **코드가 많을수록 기능이 많아지고 복잡성도 커집니다. 그리고 복잡성은 보안의 적입니다.** / **속도만으로는 가치를 만들어내지 못합니다. 신뢰가 만듭니다.**

[[trusted-throughput]]과 짝을 이루되 방향이 반대다 — 그쪽은 *처리량의 값은 신뢰에서 온다*, 이쪽은 **처리량 자체가 검증 표면을 키운다.**

⚠️ 소스가 내놓는 해법은 **자동화**(프론티어 모델을 쓴 취약점 탐지)인데, **AI가 만든 코드를 AI가 검증하는 구성의 독립성을 논의하지 않는다** — 이 위키가 [[embedded-external-evaluators]]·[[skill-evals]]에서 반복해 기록한 *작성자=검증자* 문제가 여기서도 열린 채로 남는다.

→ [[shift-left-security]] · [[continuous-security-validation]]
