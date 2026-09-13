---
title: 검증 병목 (Verification Bottleneck)
type: concept
category: framing
tags: [code-review, verification, throughput, bottleneck, agents]
aliases: [병목은 검증으로 옮겨갔다, 코드 리뷰 병목]
related: [verification-cost-asymmetry, agent-verification-skill, behavior-validated-trust, trusted-throughput, agent-trust-curve, hard-vs-soft-enforcement, generator-evaluator-pattern]
first-seen: tech-bridge-mousepower-measuring-agents
sources: [tech-bridge-mousepower-measuring-agents, tech-bridge-lauren-tan-trusting-agents]
created: 2026-09-13
updated: 2026-09-13
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

## References

- [[tech-bridge-mousepower-measuring-agents]] · [[tech-bridge-lauren-tan-trusting-agents]] · [[verification-cost-asymmetry]] · [[agent-verification-skill]] · [[behavior-validated-trust]] · [[trusted-throughput]] · [[hard-vs-soft-enforcement]]
