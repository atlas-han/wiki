---
title: 코퍼스를 파일 시스템 워크스페이스로 (Corpus as Filesystem Workspace)
type: concept
category: architecture
tags: [retrieval, filesystem, progressive-disclosure, grep, workspace, agentic-search]
aliases: [dynamic workspace expansion, 동적 작업 공간 확장, 에이전트용 SERP]
related: [file-system-agent, agent-skills, agentic-search, bm25, context-window-as-floppy-disk, push-vs-pull-context-retrieval, ride-the-optimization-trajectory]
first-seen: tech-bridge-bm25-agentic-search
sources: [tech-bridge-bm25-agentic-search, tech-bridge-exa-perfect-search-for-agents]
created: 2026-09-21
updated: 2026-09-22
---

# 코퍼스를 파일 시스템 워크스페이스로

**검색 결과를 컨텍스트에 밀어 넣지 말고, 파일 시스템처럼 생긴 작업 공간에 펼쳐 놓고 에이전트가 `grep`으로 파고들게 한다.**

출처는 제품이 아니라 **논문**이다 — [[jimmy-lin|워털루 지미 린 그룹]]의 *"동적 작업 공간 확장을 통한 직접적인 코퍼스 상호 작용 확장"*, [[jo-bergum]]이 [[tech-bridge-bm25-agentic-search]]에서 인용한다.

## 구조

| 단계 | 무엇이 일어나나 |
|---|---|
| 1 | 수십억 문서를 **BM25로 검색**한다 — *"BM25는 좋은 기준점입니다"* (12:44) |
| 2 | 결과를 **에이전트용 SERP**로 본다 — *"페이지별 검색 엔진 결과 페이지"* (12:51~13:00) |
| 3 | 그 문서들을 **작업 공간에 배치**한다 (13:02~13:07) |
| 4 | 작업 공간을 **파일 시스템으로 조직**한다 → **점진적 정보 공개** (13:09~13:19) |
| 5 | 모델이 **제목 + 스니펫**만 보고 *"더 읽어야겠군"* 을 판단한다 (13:19~13:31) |
| 6 | 더 읽을 때 **`grep`·`ripgrep`·`sed`·`awk`** 를 쓴다 (13:31~13:41) |

> 이 작업 공간을 **파일 시스템처럼 구성하면 [스킬]에서 사용하는 것과 같은 방식으로 활용할 수 있습니다. 점진적 정보 공개(progressive disclosure) 방식을 이용할 수 있습니다.** (13:09~13:19)

> 그렇게 할 때, **그것은 자신이 정말 잘 사용하는 모든 기본적인 도구(primitive tools)들을 활용할 수 있습니다.** (13:31~13:35)

## ⭐ 이틀 만에 같은 구조가 다른 도메인에서 나타났다

**2026-09-19에 이 위키에 [[file-system-agent]]가 섰다** — [[vercel|Vercel]]의 [[andrew-qu|Andrew Qu]]가 *도구를 깎지 말고 바닥을 줘라* 로 도달한 구조. **그리고 이틀 뒤 ingest된 이 소스에서 같은 구조가 검색 도메인에서 독립적으로 나온다.**

| | [[file-system-agent]] (09-19) | **이 페이지** (09-20) |
|---|---|---|
| 출처 | [[vercel\|Vercel]] — **제품, 세 번 실패하고 도달** | [[jimmy-lin\|워털루]] — **논문** |
| 파일 시스템에 무엇을 두나 | **회사의 지식·컨텍스트** | **검색 결과(코퍼스의 일부)** |
| 무엇이 채우나 | 사람·파이프라인이 미리 | **쿼리가 실행 시점에** — *동적* 확장 |
| 에이전트가 쓰는 것 | `grep`·bash | **같다** |
| 왜 되나 | 모델이 파일 시스템에 훈련돼 있다 | **같다** → [[ride-the-optimization-trajectory]] |

**핵심 차이는 워크스페이스가 정적이냐 동적이냐다.** [[file-system-agent]]의 바닥은 **거기 있다**. 여기서는 **쿼리마다 새로 깔린다** — 그래서 이름이 *dynamic workspace expansion* 이다.

**그리고 이 구조는 [[agent-skills|스킬]]의 progressive disclosure를 검색 결과에 그대로 적용한 것**이다. 화자가 그렇게 말한다(13:15). 이 위키는 progressive disclosure를 [[agent-skills]]·[[three-tier-ai-skill-stack]]에서 **사람이 쓴 문서의 계층화**로만 봐 왔는데, 여기서는 **검색된 문서에 자동으로 붙는다.**

## 컨텍스트 조달의 네 번째 태도

09-19 ingest가 세 태도를 정리했다 — **고른다**([[context-engineering]]) / **쪼갠다**([[typed-field-collection]]) / **펼쳐 놓고 찾게 한다**([[file-system-agent]]). 이 페이지는 세 번째의 **자동·동적 판**이고, 같은 날의 [[orchestrator-searcher-split]]이 **다섯 번째**(나눠서 시킨다)를 더한다.

## 결합되는 것들

> **샌드박스 인프라, 검색 인프라 등을 VFS와 bash 등을 통해 결합**할 수도 있습니다. (…) **현재 일어나고 있는 이러한 새로운 유형의 패러다임을 모두 결합하고 있기 때문**입니다. (13:45~13:59)

이 위키가 따로 모아 온 것들이 한자리에 온다 — 샌드박스([[credential-injection-outside-sandbox]]·[[confidential-vm]]), 파일 시스템([[file-system-agent]]), 검색([[bm25]]), 스킬([[agent-skills]]).

## ⚠️ 미해결

- **논문의 수치가 하나도 인용되지 않는다.** 화자는 *"제가 아주 좋아하는 논문"* 이라 하고 **구조만 설명한다.** 정확도·비용·비교 대상이 전부 없다.
- **워크스페이스의 수명·크기·정리 정책**이 없다 — 쿼리마다 쌓이면 무엇이 지워지는가.
- ⚠️ **보안이 한 번도 언급되지 않는다.** 검색된 **신뢰할 수 없는 웹 문서**를 에이전트의 작업 공간에 놓고 bash를 붙이는 구조인데, [[prompt-injection]]·[[lethal-trifecta]]가 **정확히 이 형태**(비공개 데이터 + 신뢰 불가 콘텐츠 + 외부 노출 능력)를 경고한다. **소스는 이 조합을 장점으로만 제시한다.** 09-19 [[tech-bridge-vercel-eve-filesystem-agent|Vercel 편]]에서 기록한 **같은 공백의 재발**이다.


## ⭐ 같은 문제에 세 번째 처방, 그리고 정반대 (2026-09-22 추가)

이 페이지의 처방은 **전부 줘라**다 — 결과를 파일 시스템에 펼쳐 놓고 에이전트가 `grep`·`sed`로 직접 판다. 하루 뒤 [[exa|Exa]]가 **정반대**를 내놓는다.

> **10개의 문서를 제공하고, 그중에서 가장 중요한 100개 정도의 토큰만 뽑아서 드립니다. 이렇게 하면 후속 LLM 비용을 크게 절감할 수 있습니다.** — [[will-bryk]], [[tech-bridge-exa-perfect-search-for-agents]] (11:51~12:00)

→ **[[retrieval-side-context-compression]]**

| 처방 | 소스 | 에이전트가 받는 것 |
|---|---|---|
| **전부 줘라** | 이 페이지 (09-21) | 워크스페이스에 펼쳐진 **결과 전체** |
| **왜 나왔는지 알려 줘라** | [[bm25]] ③ (09-21) | 결과 + **설명 가능성** |
| **골라서 줄여 줘라** | [[retrieval-side-context-compression]] (09-22) | **100 토큰** |

⚠️ **세 번째는 앞의 둘과 양립하기 어렵다** — 버린 것을 에이전트가 모르면 **점진적 정보 공개가 성립하지 않는다.** 이 페이지의 구조는 *모델이 스스로 깊이를 정한다*는 전제 위에 있는데, 검색 쪽 압축은 **그 깊이를 미리 고정한다.**

✅ **반대 방향의 한 가지**: 이 페이지의 근거 중 하나는 **비용**이었는데([[ride-the-optimization-trajectory]]는 아니고, 워크스페이스가 컨텍스트를 아낀다는 것), [[retrieval-side-context-compression]]은 **버릴 토큰의 값을 처음부터 치르지 않는다**는 점에서 더 싸다. **두 처방은 비용 축에서는 같은 방향이고 검사 가능성 축에서만 갈린다.**

## References

- [[tech-bridge-bm25-agentic-search]] · [[jo-bergum]] · [[jimmy-lin]] · [[tech-bridge-exa-perfect-search-for-agents]]
- 개념: [[file-system-agent]] · [[agent-skills]] · [[agentic-search]] · [[bm25]] · [[ride-the-optimization-trajectory]] · [[context-window-as-floppy-disk]]
- ⚠️ 비어 있는 쪽: [[prompt-injection]] · [[lethal-trifecta]]
- 관련: [[push-vs-pull-context-retrieval]] · [[three-tier-ai-skill-stack]] · [[orchestrator-searcher-split]]
