---
title: Sourcegraph
type: entity
category: org
tags: [code-search, code-intelligence, developer-tooling, large-codebases, agents]
aliases: [source graph, 소스그래프]
links:
  - https://sourcegraph.com
  - https://sourcegraph.com/blog/introducing-agentic-batch-changes
sources: [tech-bridge-sourcegraph-codebase-visibility]
created: 2026-10-09
updated: 2026-10-09
---

# Sourcegraph

**대규모 코드베이스의 코드 검색·코드 그래프를 만드는 회사.** [[dan-adler|Dan Adler]]가 [[tech-bridge-sourcegraph-codebase-visibility]]에서 자사를 *"what source graph is built around"*(07:59~08:01) — 수만~수십만 저장소를 에이전트가 *보고 검색하고 이해하게* 하는 인프라 — 로 소개했다. 이 위키에선 [[james-ai-explorer-understand-anything|한국어 블로그]]가 [[understand-anything]]의 비교 대상으로 이름만 든 적이 있고(→ [[code-knowledge-graph]]), **회사 쪽 화자가 직접 등장한 것은 처음**이다.

> ⚠️ 자막의 회사명은 en-orig *"source graph"*(07:59), `en`·ko *"Sourcegraph"*. 화자의 직함(CEO)은 설명란에만 있다.

## 소스에서 확인되는 것 (모두 화자 진술)

| 항목 | 진술 | en-orig |
|---|---|---|
| 해법의 기반 | *"The foundational graph of your codebase including search and then the actual compiler accurate output"* — 코드 그래프 | 08:36~08:44 |
| 슬로건 | *"Visibility is infrastructure."* | 08:55~08:57 |
| 시장 구도 | 5만 저장소 규모를 보는 인프라는 *"not being built or sold by OpenAI, by anthropic, by cursor"* | 05:00~05:10 |

## Agentic Batch Changes

발표 당일 베타 공개(*"just today we launched our new um our new agentic batch changes product into beta. This is a frontier agent"* 09:03~09:11). 화자의 설명(09:11~09:41):

- 대규모 코드베이스 소유자가 **프롬프트 하나로 수백~수천 저장소에 걸친 코드 변경**을 실행
- 변경을 **반복적으로 롤아웃**, CI 상태·PR 코멘트에 반응해 **자가 수정**(*"Self-heal"*)
- *"Use coding agents where it makes sense, where judgment is needed. Use deterministic scripts where it's not."*
- 패치가 필요한 곳의 **100%를 덮었는지 추적·감사**

얼리 액세스 사례 — Mercari: 알려진 GitHub 코드 인젝션 이슈를 저장소 2곳에 먼저 적용 → 나머지 코드베이스에서 **잠재 취약점 80개** 추가 발견, 결정론적 스크립트로 일괄 패치(10:00~10:44). ⚠️ 이어지는 *"100 of the places"* 와 수가 맞지 않는다(82 vs 100, "100%" ASR 탈락 가능 — [[tech-bridge-sourcegraph-codebase-visibility]]).

→ [[large-scale-code-changes]]

## ⚠️ 표시해 둔 것

- **제품 설명은 전부 자사 화자의 진술**이고 공개 당일의 발표다. 성능·정확도 수치는 없다.
- 블로그 링크로 공개일을 확인할 수 있으나 **열어 보지 않았다.**
- 회사의 다른 제품·역사·규모는 이 위키 소스에 없다.

## References

- [[tech-bridge-sourcegraph-codebase-visibility]] · [[dan-adler]]
- <https://sourcegraph.com> · <https://sourcegraph.com/blog/introducing-agentic-batch-changes> (⚠️ 열어 보지 않았다)
