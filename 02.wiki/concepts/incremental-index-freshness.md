---
title: Incremental Index Freshness
type: concept
category: pattern
tags: [indexing, caching, staleness, developer-tooling]
related: [code-knowledge-graph, build-time-vs-runtime-tools, reference-graph-vs-vector-search, file-discovery-tax]
first-seen: tech-bridge-graft-code-knowledge-graph
sources: [tech-bridge-graft-code-knowledge-graph]
created: 2026-09-15
updated: 2026-09-15
---

# Incremental Index Freshness

**에이전트용 인덱스의 고질적 약점은 낡는 것이다.** 코드는 매 편집마다 바뀌는데 인덱스가 따라가지 못하면 **에이전트는 존재하지 않는 구조 위에서 일한다** — 아무 인덱스도 없는 것보다 나쁠 수 있다.

[[tech-bridge-graft-code-knowledge-graph]]가 보여 주는 방어는 **두 겹**이다.

| 겹 | 동작 | 비용 |
|---|---|---|
| **증분 갱신** | 코드가 바뀌면 **전체 재빌드가 아니라 바뀐 부분만** | 편집 후 훅 → [[hook-enforced-workflow]] |
| **조회 직전 검사** | 질문에 답하기 전에 **지도 생성 이후 코드가 바뀌었는지 확인**, 바뀌었으면 먼저 갱신 | **모델을 쓰지 않는다** |

두 번째가 설계의 핵심이다. 훅을 놓쳤거나 에디터·다른 브랜치에서 파일이 바뀌어도 **조회 시점에 한 번 더 걸러진다.** 그리고 갱신에 **모델을 쓰지 않으므로** 신선도 유지가 [[file-discovery-tax|탐색세]] 절감을 도로 까먹지 않는다.

## 일반화

[[build-time-vs-runtime-tools]]가 말하는 **빌드타임 산출물이 런타임에 쓰일 때**의 일반 문제다. 빌드타임에 만든 것은 반드시 **언제 무효가 되는지**와 **누가 그것을 알아차리는지**를 함께 정해야 한다.

> ⚠️ 이 위키가 가진 근거는 소스의 **설계 진술**뿐이다. 대형 저장소에서 증분 갱신이 실제로 얼마나 걸리는지, 갱신이 실패하면 어떻게 되는지는 **소스에 없다.**

## References

- [[tech-bridge-graft-code-knowledge-graph]] · [[graft]] · [[code-knowledge-graph]]
