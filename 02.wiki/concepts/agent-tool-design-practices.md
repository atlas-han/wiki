---
title: 에이전트용 도구 설계 모범 사례 다섯 (Agent Tool Design Practices)
type: concept
category: pattern
tags: [tool-design, mcp, agent-tooling, errors, read-write, api-design]
aliases: [도구 품질 모범 사례, 결과 중심 도구, 조치 가능한 오류]
related: [secure-tool-evolution, build-time-vs-runtime-tools, model-context-protocol, no-silent-write, deny-and-continue, agent-harness-design, action-reversibility, agent-distributed-systems]
first-seen: tech-bridge-build-time-vs-runtime-tools
sources: [tech-bridge-build-time-vs-runtime-tools, tech-bridge-vercel-eve-filesystem-agent, tech-bridge-knowledge-agents-not-coding-agents]
created: 2026-09-11
updated: 2026-09-21
---

# 에이전트용 도구 설계 모범 사례 다섯

**에이전트가 쓸 도구는 사람이 쓸 API와 다르게 설계해야 한다**는 다섯 규칙. [[tech-bridge-build-time-vs-runtime-tools]]([[google-cloud|Google Cloud]], [[mcp-toolbox-for-databases|Toolbox]] 팀)가 *"도구 품질"* 절에서 정리했다.

| # | 규칙 | 근거 |
|---|---|---|
| 1 | **결과(outcome) 중심** — 원자적 REST API로 생각하지 말 것 | 여러 번 호출해야 하는 **왕복**이 줄어든다 |
| 2 | **설명은 안내(guidance)** — 입력 파라미터 정보를 중복하지 말 것 | 에이전트는 파라미터 스키마를 이미 본다; 설명은 *언제·어떻게 쓰는가* 를 위해 |
| 3 | **읽기 도구와 쓰기 도구 분리** | **읽기는 자동 승인**, **쓰기는 사용자 확인**으로 보낼 수 있다 |
| 4 | **조치 가능한 오류(actionable errors)** — *"우리 모두가 더 잘할 수 있는 1번"* | 일반 HTTP 404 대신 **재시도 가능한 오류**를 주면 에이전트가 행동한다 |
| 5 | **단순한 평면 입력** — 복잡한 map·프리미티브 금지 | *"신뢰할 수 없다"* — 평면 구조가 신뢰성을 크게 올린다 |

## 각 규칙이 이 위키의 어디와 닿는가

### 1 — 결과 중심

> 도구는 **결과에 초점**을 두길 강력히 권합니다. **원자적 REST API로 생각하면 안 됩니다.** 그 행동이 실제로 무엇을 해야 하는지를 생각해야 합니다.

REST의 자원 단위(GET /orders, DELETE /orders/1)가 아니라 **의도 단위**(주문 취소)로 도구를 자른다. [[build-time-vs-runtime-tools]]의 *주문 취소* 예제가 그것이다. 이것은 [[outcome-engineering]]이 *프롬프트* 에 대해 말한 것(*how* 가 아니라 *원하는 결과*)을 **도구 경계**에 옮긴 형태다.

### 2 — 설명은 안내

[[agent-skills]]가 *"description에 'use when'을 써라"* 고 한 것과 같은 규칙이 **도구 설명**에도 적용된다. [[secure-tool-evolution]]의 커스텀 도구가 *이름과 설명을 맞춤 설정* 하는 이유다.

### 3 — 읽기/쓰기 분리

> 그러면 **읽기 도구는 자동 승인**하고, **쓰기 도구는 사용자에게 확인**을 보낼 수 있습니다. 에이전트가 쓰기에도 훨씬 명확해집니다.

이 위키가 여러 자리에서 본 **승인 게이트를 도구 경계에 미리 새기는** 규칙이다:
- [[no-silent-write]] — 공유 지식에의 쓰기는 사람 승인. 같은 축.
- [[action-reversibility]] — 읽기는 되돌릴 필요가 없고 쓰기는 되돌리기 어렵다. 분리의 근거.
- [[secure-tool-evolution]] 2단계(읽기 전용 제한)는 이 분리를 **드라이버 수준**까지 내린 것.
- [[anthropic-claude-code-auto-mode]]의 [[transcript-classifier]]가 *행동을 보고* 판정하는 것과 달리, 이 규칙은 **도구 이름만 보고** 판정할 수 있게 한다 — 분류기가 필요 없어지는 방향.

### 4 — 조치 가능한 오류

> 보통은 일반적인 HTTP 404 같은 오류를 돌려주죠. 그런데 에이전트는 이제 정말 똑똑합니다. **재시도할 수 있는 오류**를 줄 수 있으면 에이전트가 실제로 그 조치를 취할 수 있습니다.

[[deny-and-continue]]가 *차단 사유를 tool result로 돌려보내 에이전트가 다른 길을 찾게* 하는 것과 같은 원리를 **일반 오류**에 적용한 것이다. 그리고 [[agent-distributed-systems]]의 *"타임아웃은 실패가 아니라 알 수 없음"* — 오류의 **종류**를 에이전트가 구분할 수 있어야 재시도·보상·중단을 고를 수 있다.

> ⚠️ 역방향 위험을 소스는 말하지 않는다 — [[build-time-vs-runtime-tools]]의 테이블 삭제는 정확히 *오류를 만난 에이전트가 조치를 취한* 결과였다. 조치 가능한 오류는 **런타임 도구**(행동이 잘려 있는)에서만 안전하다.

### 5 — 평면 입력

> 사람들이 에이전트가 만들어야 하는 **복잡한 map, 복잡한 프리미티브**를 쓰려는 걸 보는데, **신뢰할 수 없습니다.**

에이전트가 중첩 구조를 조립하는 것 자체가 실패 지점이라는 관찰. 근거 수치는 없다.

## ⚠️ 미해결

- **측정치 없음** — 다섯 규칙 모두 *"신뢰성이 크게 올라간다"* 류의 서술이고 수치가 없다. Prerna의 eval bench가 그것을 재는 도구로 언급되지만 결과는 소스에 없다.
- 규칙 1(결과 중심 = 굵은 도구)과 규칙 5(단순 입력)의 **긴장** — 결과 단위가 커질수록 입력이 복잡해지기 쉽다. 소스는 다루지 않는다.
- 당사자 진술.

## 파일 시스템 에이전트라는 반대 각도 (2026-09-19)

[[tech-bridge-vercel-eve-filesystem-agent]]가 **정반대 방향의 처방**을 낸다 — 도구를 좁히지 말고 **모델이 이미 잘 훈련된 범용 도구**(list·read·bash·grep)를 주고 **바닥을 넓혀라.** → [[file-system-agent]]

> **[Claude Code]에 매우 구체적인 도구 세트를 제공하지 않았습니다.** 마치 **자유롭게 탐색하고 새로운 행동(emergent behavior)을 발견하도록 내버려 둔 것**과 같았습니다. (08:11~08:28)

**모순이 아니라 층이 다르다:**

| | 이 페이지 ([[google-cloud\|Google Cloud]], 09-11) | [[file-system-agent]] ([[vercel\|Vercel]], 09-19) |
|---|---|---|
| 도구 | **좁히고 결과 중심으로** | **넓히고 범용으로** |
| 앞에 있는 사람 | **프로덕션 최종 사용자** | **사내 신뢰 사용자** |
| 시간대 | 런타임 ([[build-time-vs-runtime-tools]]) | 탐색·분석 |
| 위험 | 유출·권한 오용 | ⚠️ **소스가 다루지 않음** |

이 페이지가 세운 [[build-time-vs-runtime-tools]] 축이 정확히 적용된다 — *빌드타임 도구를 프로덕션에 두지 마라* 의 반대편에서 *탐색용 도구는 좁히지 마라* 가 나온 셈이다. **두 소스는 서로를 모른다.** ⚠️ Vercel 편은 보안·권한을 한 번도 다루지 않으므로, 이 페이지의 규칙이 그쪽에서 반박된 것이 아니라 **그쪽 범위 밖**이다.

## 2026-09-20 — 네 번째 실패 모드: 학습 데이터가 선택을 편향시킨다

[[benjamin-clavie|Clavié]]가 [[tech-bridge-knowledge-agents-not-coding-agents]]에서 **이 위키가 아직 갖고 있지 않던 형태의 도구 실패**를 지목한다.

> 자주 보게 되는 한 가지는 **에이전트가 [`grep`] 쿼리를 쓰려고 한다는 것입니다. [`grep`]은 학습 데이터 어디에나 있고 BM25도 데이터 어디에나 있으니까요. 그리고 그게 항상 필요한 것은 아닙니다.** (…) **PDF는 [`grep`] 할 수 없습니다.** (16:06~16:23)

| 실패 모드 | 원인 |
|---|---|
| 도구를 못 찾는다 | 발견 비용 → [[capability-discovery-burden]] |
| 도구가 너무 많다 | 선택 과부하 → **이 페이지** |
| 설명이 나쁘다 | 인터페이스 → [[build-a-lever]] |
| **도구가 있는데 익숙한 쪽으로 간다** | **학습 데이터 분포** → [[retrieval-primitive-repertoire]] |

**네 번째는 도구 설계로 고쳐지지 않는다** — 소스의 처방은 **공동 설계(co-design)** 이고, 모델이 그 도구에 훈련돼 있을 것을 요구한다. ⚠️ **그런데 그것은 도구 제작자가 통제할 수 없는 변수이고, 소스는 그 비대칭을 지적하지 않는다.**

## References

- [[tech-bridge-build-time-vs-runtime-tools]] (first-seen) · [[averi-kitsch]]
- 관련: [[secure-tool-evolution]] · [[no-silent-write]] · [[deny-and-continue]] · [[outcome-engineering]] · [[agent-skills]] · [[model-context-protocol]]
