---
title: 코드는 예외적인 지식이다 (Code as Atypical Knowledge)
type: concept
category: theory
tags: [knowledge-work, code-search, grep, ambiguity, agent-design]
aliases: [코드의 특수성, durable cues, 견고한 단서]
related: [knowledge-agents-vs-coding-agents, reference-graph-vs-vector-search, code-only-index-blind-spot, bm25, retrieval-primitive-repertoire, knowledge-work-agent-gap, file-discovery-tax]
first-seen: tech-bridge-knowledge-agents-not-coding-agents
sources: [tech-bridge-knowledge-agents-not-coding-agents]
created: 2026-09-21
updated: 2026-09-21
---

# 코드는 예외적인 지식이다

**코드는 지식이지만, 모든 지식이 코드는 아니다.** 코딩 에이전트가 잘 도는 이유를 모델이 아니라 **코드라는 도메인의 세 가지 우연한 성질**에서 찾는 프레이밍.

> **코드는 지식이지만 모든 지식이 코드는 아닙니다. 코드는 매우 독특한 형태의 지식입니다.** — [[benjamin-clavie]], [[tech-bridge-knowledge-agents-not-coding-agents]] (03:38~03:46)

## 세 가지 성질

| | 코드 | 일반 지식 |
|---|---|---|
| **① 견고한 단서** | **식별자·파일·경로**가 있고 *"대부분의 경우 크게 변경되지 않습니다"* (03:46~04:01) | **없다.** *"의미는 항상 암묵적"* (04:53) |
| **② 표면이 `grep` 가능** | **키워드·메서드 정의** — *"정의상 [`grep`] 할 수 있는 많은 것들"* (04:04~04:11) | PDF·계약서·판례 — *"PDF는 [`grep`] 할 수 없습니다"* (16:19) |
| **③ 과제가 좁다** | 사람이 **티켓 하나로 쪼개서** 건넨다 (04:24~04:41) | **개방형**이고 에이전트가 직접 쪼개야 한다 (12:19~12:28) |

**③이 이 소스의 가장 새로운 지적**이고, [[knowledge-agents-vs-coding-agents]]에서 자세히 다룬다.

## ① — "30일"이 네 가지를 뜻할 때

②·③보다 이 위키에 덜 알려져 있던 것은 **①의 실패 양상**이다.

> **동일한 단서가 아주 다양한 것을 의미할 수 있다는 점입니다. 지식 노동에는 함수 정의가 없습니다.** (04:56~05:01)

> **예를 들어 '30일'을 받았다고 합시다. 에이전트가 '30일'을 찾고 있다면, 그것은 마감 기한인가요? 유예 기간인가요? 보존 규칙인가요? 애초에 같은 도메인이기는 한가요? 계약서에서 '30일'을 검색했는데 약품 정보가 나오는 건 아닌가요?** (05:01~05:15)

**"함수 정의가 없다"가 핵심 문장이다.** 코드에서 식별자는 **정의로 소급된다** — 한 곳에 정의가 있고 나머지는 참조다. [[reference-graph-vs-vector-search]]가 그래프를 세울 수 있는 이유가 정확히 이것이다. **일반 지식에는 그 정의 지점이 없다.**

그리고 의미는 쿼리보다 앞에 있다:

> **더 중요한 것은, 검색이 의도(intent)에서 출발한다는 점**입니다. (…) **작업에 미리 정의되어 있지 않은 조건부 정보가 아주 많고, 그건 전부 에이전트가 찾아내야 할 몫입니다.** (05:17~05:34)

> **그래서 코드가 아닌 지식은 매우 맥락적이고 의미 중심적이며, 이것이 코드보다 훨씬 어렵습니다.** (05:34~05:41)

## ⭐ 이 위키가 반대 방향에서 같은 곳에 도달해 있었다

[[reference-graph-vs-vector-search]] (09-15)가 코드 검색을 논하며 **정확히 이 대비를 반대편에서** 적었다:

> 자연어 문서에서는 **유사도가 곧 관련성**인 경우가 많다. 코드에서는 **반대말이 가장 비슷하게 생긴다**(`createAccount` / `deleteAccount`).

| | [[reference-graph-vs-vector-search]] | **이 페이지** |
|---|---|---|
| 누가 말하나 | [[graft]] 개발팀 (**코드 도구를 판다**) | [[mixedbread\|Mixedbread]] (**지식 검색을 판다**) |
| 결론 | 코드에서는 **벡터가 약하다** → 참조 그래프를 써라 | 코드는 **쉬운 예외**다 → 일반 지식에서 일반화하지 마라 |
| 공통 전제 | **코드와 산문은 검색 문제로서 종류가 다르다** | 〃 |

**서로를 모르는 두 회사가 같은 구분에 도달하고, 각자 자기 쪽이 어렵다고 말한다.** 그리고 [[code-only-index-blind-spot]]은 **세 번째 각도**로 같은 선을 긋는다 — *코드만 인덱싱하는 도구는 에이전트가 읽는 것의 절반만 덮는다.* **셋을 겹치면 이 위키의 검색 지형이 코드/비코드로 갈라진다는 것이 세 출처에서 확인된다.**

## ⚠️ `grep`이라는 단어가 자막에서 사라진다

**en-orig가 `grep`을 전편에 걸쳐 *"grape"* 로 적고**, ko는 그것을 영어 그대로 두거나 *"파악"* 으로 의역한다(04:17·16:09·16:11·16:19). **이 발표의 핵심 논거 하나가 통째로 그 단어 위에 있는데 ko만 읽으면 도구 이름이 보이지 않는다.** → [[tech-bridge-knowledge-agents-not-coding-agents]]

## References

- [[tech-bridge-knowledge-agents-not-coding-agents]] · [[benjamin-clavie]]
- 상위: [[knowledge-agents-vs-coding-agents]]
- 같은 구분에 도달한 곳: [[reference-graph-vs-vector-search]] · [[code-only-index-blind-spot]] · [[knowledge-work-agent-gap]]
- 관련: [[bm25]] · [[retrieval-primitive-repertoire]] · [[file-discovery-tax]] · [[code-knowledge-graph]]
