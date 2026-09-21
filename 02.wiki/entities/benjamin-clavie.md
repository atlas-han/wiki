---
title: Benjamin Clavié
type: entity
category: person
tags: [retrieval, knowledge-work, agent-architecture, mixedbread]
aliases: [Ben Clavié, 벤자민 클라비에, 벤 클라비에]
links:
  - https://x.com/bclavie
  - https://ben.clavie.eu
sources: [tech-bridge-knowledge-agents-not-coding-agents]
created: 2026-09-21
updated: 2026-09-21
---

# Benjamin Clavié

[[mixedbread|Mixedbread]] 소속. **이 위키에서 에이전트 설계의 근거를 인류의 지식 노동사에서 끌어온 첫 화자**다.

> 저는 **[Mixedbread]** 에서 일했는데, 거기서는 **검색(retrieval)** 을 합니다. 저는 **프랑스인이고 도쿄에 살고 있습니다.** — [[tech-bridge-knowledge-agents-not-coding-agents]] (00:04~00:09)

**소속·국적·거주지를 화자가 직접 말하는 드문 경우**다. 이 위키의 인물 페이지 대부분은 설명란에 의존해 왔다.

## 논지

한 문장으로:

> **에이전트가 하는 일은 지식 노동이다. 그러니 코딩 에이전트가 아니라 지식 노동자처럼 설계해야 한다.** (00:09~00:22)

화자 스스로 이것을 ***"조금 뜨거운 [hot take]"*** 이라고 부른다(00:22~00:24).

논증의 형태가 이 위키에서 특이하다 — **모델·벤치마크가 아니라 제도사(制度史)에서 출발한다.** 알렉산드리아 도서관의 [피나케스], 박식가에서 수도원·대학·관료제로, 병원의 직급 분화 → [[tool-organization-loop]]. **에이전트 아키텍처의 근거로 로펌의 파트너/어시스턴트 구조를 드는 것**이 처방의 핵심이다 → [[orchestrator-searcher-split]].

## 이 화자가 이 위키에 세운 것

| 페이지 | 무엇을 말하나 |
|---|---|
| [[knowledge-agents-vs-coding-agents]] | 코딩은 지식 노동의 **특수 사례**이고, 거기서 일반화하면 틀린다 |
| [[code-as-atypical-knowledge]] | 코드가 쉬운 건 모델이 아니라 **도메인과 과제 형태** 때문 — 견고한 단서·`grep` 가능·**그리고 사람이 이미 쪼개 준다** |
| [[tool-organization-loop]] | 도구와 조직은 서로를 끝없이 촉발하는 **하나의 루프** |
| [[tools-are-not-neutral]] | 도구는 가능/불가능이 아니라 **확장 가능/불가능**을 정한다 |
| [[orchestrator-searcher-split]] | 파트너가 쪼개고 어시스턴트가 조사해 **메모**를 올린다 |
| [[oracle-gap]] | 완벽한 문서와 내 검색 시스템 사이의 거리 — **아키텍처로 좁힌다** |
| [[retrieval-primitive-repertoire]] | `grep`·BM25·시맨틱 검색은 **프리미티브**이고 모델이 전부를 알아야 한다 |

그리고 [[which-bm25-problem]]에서 **같은 날 [[jo-bergum|Bergum]]과 독립적으로 같은 결론**에 닿는다.

## ⚠️ 당사자 진술

발표 후반(13:18~15:00)은 **자사 제품의 리더보드 성적**이다. 수치는 전부 자기 보고이고 **측정 조건이 없다** — *20% 적은 툴 호출* · *3.5포인트 상승* · *오라클 갭 10→6포인트*. 앞 2/3(지식 노동의 정의·코드의 특수성·두 루프·도구의 비중립성)은 **제품과 무관한 논증**이고 이 위키는 그 부분을 개념으로 올린다.

⚠️ **자기 회사에 불리한 말도 한다** — *"왜 내 에이전트는 88.9를 받는데 인간은 99.4를 받죠? 10%를 그냥 테이블에 두고 오는 셈입니다. 그런데 저는 그걸 이해할 수 없습니다"*(13:44~13:58). **자사 도구의 남은 격차를 스스로 지목하고 "이해할 수 없다"고 말하는 것**은 이 위키의 당사자 발표 중 드물다.

## 미해결

- **행사 이름** — 설명란에 없다. 다만 *"오늘 아침에 이 얘기를 하셨는데"*(09:23)가 [[jo-bergum|Bergum]] 편을 가리켜 **같은 무대임은 확인된다.** → [[tech-bridge-knowledge-agents-not-coding-agents]]
- **[[mixedbread|Mixedbread]]에서의 직함** — *"일했는데(I worked at)"* 뿐이다.
- ⚠️ **자막 양 트랙이 이름을 *"Ben Clavier"* 로 적는다.** 설명란의 **Benjamin Clavié** 를 따랐다.
- **같은 발표에서 [BrowseComp-Plus] 코퍼스 크기를 20만 → 10만으로 다르게 말한다**(09:20 vs 11:03).

## References

- [[tech-bridge-knowledge-agents-not-coding-agents]] · [[mixedbread]] · [[tech-bridge]]
- 개념: [[knowledge-agents-vs-coding-agents]] · [[code-as-atypical-knowledge]] · [[tool-organization-loop]] · [[tools-are-not-neutral]] · [[orchestrator-searcher-split]] · [[oracle-gap]] · [[retrieval-primitive-repertoire]] · [[which-bm25-problem]]
- 같은 무대: [[jo-bergum]]
