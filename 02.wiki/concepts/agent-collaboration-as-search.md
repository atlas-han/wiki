---
title: 에이전트 간 협업은 검색 문제다 (Agent Collaboration as Search)
type: concept
category: theory
tags: [agent-to-agent, multi-agent, search, retrieval, privacy, coase-theorem, context-window]
aliases: [A2A as search, 에이전트 대 에이전트, 단일 전지 에이전트]
related: [context-engineering, retrieval-augmented-generation, long-context-agents, agent-distributed-systems, persistent-agent-teams, sweeper-agent, black-box-agent-approach, privacy-auto-mode, sutton-bitter-lesson]
first-seen: tech-bridge-agent-to-agent-as-search
sources: [tech-bridge-agent-to-agent-as-search, tech-bridge-bm25-agentic-search, tech-bridge-knowledge-agents-not-coding-agents]
created: 2026-09-10
updated: 2026-09-21
---

# 에이전트 간 협업은 검색 문제다

**에이전트 대 에이전트(A2A)는 별개의 개념이 아니라, 도구 호출 직전 컨텍스트 창에 올바른 정보를 넣는 검색 문제이며, 이상은 세상 모든 정보를 보는 단일 에이전트다. 그 이상을 막는 것은 프라이버시라는 거래 비용이고, 멀티 에이전트 시스템의 시험은 그 이상을 얼마나 잘 근사하는가다.** [[jean-denis-greze]]([[town]])의 재구성.

> **대부분의 LLM 시스템은 그냥 검색 문제**라고 생각합니다. (…) 도구 호출 직전에 **컨텍스트 창이 올바른 정보를 갖고 있게** 하는 겁니다. 올바른 정보를 컨텍스트 창에 넣으면 LLM의 지능에 기반해 **가능한 최선의 결과**를 얻습니다. — [[tech-bridge-agent-to-agent-as-search]]

## 세 단계 역사

| 시기 | 방식 | 한계 |
|---|---|---|
| 4년 전 | 사람이 컨텍스트 창을 **수동**으로 채움 | — |
| 몇 년 전 | [[retrieval-augmented-generation\|RAG]] — 시스템을 훑는 검색 도구 | *"확장이 잘 안 되고 문제가 있어"* |
| 지금 | **에이전틱 검색** — 도구를 많이 주고 콘텐츠 공간을 검색 | (이 개념이 답하는 것) |

*"여기에는 사람이 없다. 중요한 그 한 번의 LLM 호출이 올바른 컨텍스트를 갖는 것뿐."* → [[context-engineering]]의 정의를 한 문장으로 압축한 것이다.

## 이상 상태와 그것을 막는 것

> 에이전트가 하나뿐이고, 컨텍스트 창이 하나이고, **우주의 모든 정보에 접근**합니다. (…) **그것이 멀티 에이전트 세계**입니다. 세상 모든 정보에 접근하는 에이전트 하나일 뿐이죠.

막는 것은 **코즈 정리** — *"모두가 올바른 정보에 접근하고 거래 비용이 없다면 경제적으로 이상적인 결과. 똑같다. **무한한 컨텍스트 창이 있더라도 프라이버시와 보안 때문에** 세상의 모든 컨텍스트를 LLM에 줄 수 없다."*

> 이것이 **멀티 에이전트 시스템의 시험**입니다 — **이것을 얼마나 잘 근사하는가.**

이 위키에서 멀티 에이전트는 지금까지 **분산 시스템**([[agent-distributed-systems]] — 타임아웃·멱등성), **팀**([[persistent-agent-teams]] — 코디네이터·역할), **fan-out**([[dynamic-workflows]])으로 다뤄졌다. 이 개념은 그것들을 **하나의 이상적 에이전트를 프라이버시 제약 아래 근사하는 것**으로 다시 놓는다. 그리고 [[long-context-agents]]·[[tech-bridge-minimax-m3-long-context]]가 컨텍스트 **길이**를 늘리는 쪽이라면, 여기서는 **길이가 무한해도 남는 한계**가 문제다.

## 다섯 전략과 판정 기준

사일로를 넘어 올바른 데이터를 LLM 호출에 넣는 방식:

| # | 전략 | 판정 |
|---|---|---|
| 1 | 신뢰 경계 안 전체 접근 (부부 공용 에이전트, 인사팀 에이전트) | 지금은 좋으나 **end game 아님** — 사람이 생각해 만든 **새 사일로** |
| 2 | 힘↔프라이버시를 맞바꾼 커스텀 도구 (관계 강도 점수만 반환) | 멋지지만 **수동, 동적이지 않음** |
| 3 | 공유 사일로 + [[sweeper-agent\|청소부 AI]] | **즉각적 ROI** — AI가 자동으로 만드는 위키 |
| 4 | 정보 통로로서의 인간 (*"전통적 A2A"*) | 소수만 아는 정보에 **모두를 스팸** |
| 5 | [[black-box-agent-approach\|블랙박스]] | **가장 강력**, 실제로는 드묾 |

1·2를 기각하는 기준이 이 개념에서 가장 이식성 높은 도구다:

> 제가 아침에 일어나면 사실상 유일하게 생각하는 것인데 — **시간이 지나면서 시스템이 자연히 더 적은 사람을 필요로 하는가? 모델이 좋아질수록 이 접근도 좋아지는가?** 이 접근의 문제는 **둘 다 답이 '아니오'** 라는 겁니다.

→ [[sutton-bitter-lesson]]의 **아키텍처 판정 버전**이다. Sutton이 *계산과 함께 스케일하는 방법이 이긴다* 고 했다면, Greze는 *모델 용량과 함께 스케일하는 아키텍처를 골라라* 고 한다 — 그리고 그 결론이 [[privacy-auto-mode]]다.

## 이 위키의 회사 두뇌와의 관계

같은 날 [[tech-bridge-company-brain-security|PromptQL 편]]의 [[company-brain]]은 이 개념의 **전략 3**에 해당한다(공유 위키 + 스코프). 다만 PromptQL은 **접근을 사용자 단위로 잠그고**([[credential-injection-outside-sandbox]]) Greze의 블랙박스는 **읽기를 다 풀고 쓰기에서 잠근다.** 두 소스는 서로를 모른다. 위키는 둘을 **벽의 위치(입구/출구)** 로 대비해 둔다.

## ⚠️ 한계

- **"검색 문제"의 정의가 넓다** — 프라이버시 정책의 집행, 승인, 감사가 전부 *검색* 안에 들어가면 그 말은 설명력을 잃는다. 소스는 이를 다루지 않는다.
- 코즈 정리는 **비유**로만 쓰인다 — 거래 비용의 크기나 내부화 방법은 없다.
- 수치 없음. 당사자 진술(에이전트 간 협업이 자기 사업의 전제).
- 화자의 마지막 유보 — *"에이전트가 프라이버시 결정을 전부 내리는 미래를 신뢰하는가? 잘 모르겠다."*

## ⭐ 2026-09-20 — 같은 문장이 비유가 아니라 직업이 되었다

이 페이지의 출발 문장(*"대부분의 LLM 시스템은 그냥 검색 문제"*)은 [[jean-denis-greze|Greze]]가 **멀티 에이전트를 설명하기 위해** 쓴 재해석이었다. [[tech-bridge-bm25-agentic-search]]에서 **검색을 20년 해 온 사람이 같은 자리에 선다** — 그리고 문장에서 멈추지 않고 **모델·하네스·엔진으로 쪼갠 뒤 어디가 병목인지 실험으로 가른다**([[retrieval-not-reasoning-bottleneck]]). → [[agentic-search]]

**분업의 값에 대해서는 이 페이지와 [[orchestrator-searcher-split]]이 정반대로 셈한다.**

| | **이 페이지** ([[jean-denis-greze\|Greze]]) | [[orchestrator-searcher-split]] ([[benjamin-clavie\|Clavié]]) |
|---|---|---|
| 이상 | **단일 전지 에이전트** | **분업 구조** — 파트너/어시스턴트 |
| 멀티 에이전트는 | 이상의 **근사**(손실) | **유일한 길**(이득) |
| 제약의 출처 | **프라이버시**라는 거래 비용 | **컨텍스트 용량**과 **문제의 개방성** |

⚠️ **모순은 아니다.** 이 페이지의 이상적 단일 에이전트는 *모든 정보를 볼 수 있다*고 가정하는데, 저쪽은 **볼 수 있어도 컨텍스트에 안 들어간다**고 말한다 — *"1억 토큰도 한 개 주 법전의 절반 미만"*. **프라이버시 제약이 사라져도 용량 제약은 남는다.**

그리고 이 페이지가 기록한 실패 형태 — *"LLM이 실수해서 정보 하나가 틀리면 영원히 오염된다"* — 는 **서처가 올리는 메모에 그대로 적용되는데 [[benjamin-clavie|Clavié]]는 그것을 다루지 않는다.**

## References

- [[tech-bridge-agent-to-agent-as-search]] (first-seen) · [[jean-denis-greze]] · [[town]]
- 관련: [[context-engineering]] · [[retrieval-augmented-generation]] · [[sweeper-agent]] · [[black-box-agent-approach]] · [[privacy-auto-mode]] · [[sutton-bitter-lesson]] · [[company-brain]]
