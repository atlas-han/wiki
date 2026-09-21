---
title: Code-Only Index Blind Spot
type: concept
category: theory
tags: [indexing, context-engineering, documentation, limits]
related: [file-discovery-tax, code-knowledge-graph, llm-coding-guidelines, agent-memory, context-engineering]
first-seen: tech-bridge-graft-code-knowledge-graph
sources: [tech-bridge-graft-code-knowledge-graph, tech-bridge-knowledge-agents-not-coding-agents]
created: 2026-09-15
updated: 2026-09-21
---

# Code-Only Index Blind Spot

**코드만 인덱싱하는 도구는 에이전트가 실제로 읽는 것의 절반만 덮는다.**

[[tech-bridge-graft-code-knowledge-graph]]에서 이 한계를 말하는 사람은 **도구를 소개하던 화자 자신**이다.

> **실제 프로젝트에는 코드만 있는 게 아니라 에이전트에게 맥락을 주는 다른 파일들도 있습니다** — PRD, `learnings.md` 같은 것들이죠. **그런데 [이 도구는] 코드만 매핑합니다.** 그것들을 읽어야 할 때 에이전트는 **평소의 기본 방식을 씁니다.**

## 왜 중요한가

[[file-discovery-tax|탐색세]]가 **사라지는 것이 아니라 코드 영역에서만 사라진다.** 남는 쪽은 하필 **사람이 쓴 산문**이라 참조 관계로 그래프를 만들 수 없다 — PRD가 어느 함수를 "쓴다"고 말할 수 없으므로 **같은 방법이 통하지 않는다.** 이 위키에 이미 있는 [[llm-coding-guidelines]]·[[intent-md]]·[[agent-memory]]가 전부 이 범주의 파일이다.

즉 **정적 분석으로 만드는 인덱스와 산문으로 쓰는 맥락은 조달 경로가 다르고, 도구가 전자만 다루면 후자의 비용은 그대로 남는다.**

## 이 위키가 이미 가진 반쪽

| 범주 | 어떻게 조달되나 | 위키 페이지 |
|---|---|---|
| **코드** | 참조 그래프 인덱스 | [[code-knowledge-graph]] · [[reference-graph-vs-vector-search]] |
| **의도·규칙** | 파일로 써서 컨텍스트에 상주 | [[llm-coding-guidelines]] · [[intent-md]] |
| **과거 결정** | 검색·복원 스킬 | [[agent-knowledge-sourcing]] · [[agent-memory]] |

**셋을 하나로 잇는 소스는 아직 이 위키에 없다.**

> [[ai-labs]]는 이 빈자리를 **자체 수정판**으로 메웠다고 말하고 그것을 자사 커뮤니티에 올려 두었다고 한다 — **어떻게 고쳤는지는 소스에 없다.**

## 2026-09-20 — 세 번째 각도

[[code-as-atypical-knowledge]]([[benjamin-clavie|Clavié]])가 같은 경계선을 **도구가 아니라 지식의 성질** 쪽에서 긋는다 — 코드에는 **견고한 단서와 함수 정의**가 있고 산문에는 없다.

**이 페이지의 표에 한 줄이 더 붙는 셈이다**: 코드 밖의 파일들이 남는 이유는 *도구가 아직 안 다뤄서*가 아니라 **참조로 그래프를 만들 수 있는 구조가 애초에 없어서**다. 그래서 이 위키가 적어 둔 *"같은 방법이 통하지 않는다"* 는 **도구의 한계가 아니라 도메인의 성질**로 다시 읽힌다.

⚠️ 그리고 [[benjamin-clavie|Clavié]]의 처방은 이 페이지가 기다리던 *셋을 하나로 잇는 소스*가 **아니다** — 그는 **다른 프리미티브를 더하고**([[retrieval-primitive-repertoire]]) **조직으로 푼다**([[orchestrator-searcher-split]]). **인덱스를 확장하지 않는다.**

## References

- [[tech-bridge-graft-code-knowledge-graph]] · [[graft]] · [[file-discovery-tax]]
