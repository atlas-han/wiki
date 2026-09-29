---
title: 계층형 문서 파싱 — 빠른 1차 훑기 후 필요한 페이지만 VLM (Tiered Document Parsing)
type: concept
category: pattern
tags: [document-parsing, agent-loop, latency, cost, vlm, progressive-disclosure, tool-design]
aliases: [fast pass then VLM, 빠른 1차 파싱, 에이전트 루프 안의 파서, escalation parsing]
related: [document-parsing-for-agents, document-context-layer, search-latency-tiers, agentic-search, corpus-as-filesystem-workspace, orchestrator-searcher-split, agent-skills]
first-seen: tech-bridge-llamaindex-document-context-layer
sources: [tech-bridge-llamaindex-document-context-layer]
created: 2026-09-29
updated: 2026-09-29
---

# 계층형 문서 파싱

**에이전트 루프 안에서는 모든 문서를 싸고 빠른 비-VLM 파서로 먼저 훑고, 표·차트처럼 값을 정확히 읽어야 하는 페이지에서만 느린 VLM 파서를 도구로 호출한다.** 파싱 품질을 일괄로 올리는 대신 **에이전트가 필요할 때 깊이를 고르게** 한다. [[jerry-liu|Jerry Liu]]([[llamaindex|LlamaIndex]])가 [[tech-bridge-llamaindex-document-context-layer]]에서.

> *"what these agents will do is they'll do like a fast pass over all the documents first kind of like just scan through all the contents extremely efficiently. And then if actually needs to dive into a page with like tables, with like charts, and actually needs to more deeply understand the values, it'll use a VLM based tool, slower processing, to actually make sure it reads the information correctly."* (17:37~17:59)

## 구성

| 단계 | 도구 | 소스 |
|---|---|---|
| 기본값 | **VLM 없는 빠른 파서** — LlamaIndex의 Rust 기반 오픈소스 "Light Parse" | 16:53~17:16 |
| 승격 | **VLM 기반 파서를 도구로** — LlamaParse *"or other frontier models"* | 17:31~17:37 |
| 배포 | *"one-click installable skill"* 로 Claude Code·Claude Cowork·Codex에 | 17:22~18:01 → [[agent-skills]] |

동기는 **지연**이다: 천 개 문서를 1분 안에 처리해야 하는 실시간 업로드에서 VLM은 *"really tough for basically every single OCR service out there … that includes ours, too"*(16:23~16:28). → [[document-parsing-for-agents]]의 초저지연 영역.

## 핵심 가정 — 파싱 품질과 에이전트 능력은 대체재

같은 발표의 저비용 영역이 이 패턴의 전제를 명시한다:

> *"even if it's a little bit messed up, it's okay, too, because in the end if you have a sufficiently good agent, it can always dive deeper into the document and surface the right information with the right citations and grounding"* (15:44~15:54)

**앞단을 싸게 하고 틀린 부분은 에이전트가 되돌아가 메운다.** 이것은 [[agentic-search]]의 *"검색은 한 번이 아니다"* (궤적)를 **파싱에 적용**한 것이다.

## 이 위키의 인접 패턴

- [[search-latency-tiers]] — 같은 제품이 빠른 티어·느린 티어를 동시에 판다. 여기선 두 티어가 **한 에이전트 루프 안에서 연쇄**된다.
- [[corpus-as-filesystem-workspace]] — 결과를 밀어 넣지 않고 펼쳐 두면 에이전트가 파고든다. 1차 파싱 결과가 그 "펼쳐 둔 작업 공간"이 된다(⚠️ 소스는 파일 시스템을 말하지 않는다 — 위키의 연결).
- [[orchestrator-searcher-split]] — 분업의 축이 *사람/역할* 이 아니라 **비용/지연**이다.
- [[agent-skills]]의 progressive disclosure — 필요할 때만 깊은 것을 로드한다는 같은 모양.

## ⚠️ 유보

- **당사자 제품 조합이다**(Light Parse + LlamaParse). 1차 파싱이 틀렸을 때 **에이전트가 그 사실을 알아차리는가** — 표가 깨졌는데 깨진 줄 모르면 승격이 일어나지 않는다. 소스는 승격 트리거를 *"if actually needs to"* 로만 말한다.
- 비용·지연 수치 없음.
- 반대 방향 주장: [[retrieval-side-context-compression]]([[exa|Exa]])은 에이전트가 **한 번에 압축된 답**을 받는 쪽에 건다 — 되돌아가 파고드는 루프를 전제하지 않는다.

## References

- [[tech-bridge-llamaindex-document-context-layer]] · [[llamaindex]] · [[jerry-liu]]
- [[document-parsing-for-agents]] · [[document-context-layer]] · [[search-latency-tiers]] · [[agentic-search]]
