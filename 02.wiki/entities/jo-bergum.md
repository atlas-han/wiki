---
title: Jo Kristian Bergum
type: entity
category: person
tags: [retrieval, search, bm25, information-retrieval, hornet]
aliases: [Jo Bergum, 조 베르굼, 조 크리스티안 베르굼]
links:
  - https://x.com/jobergum
  - https://www.linkedin.com/in/jo-bergum
sources: [tech-bridge-bm25-agentic-search, tech-bridge-exa-perfect-search-for-agents]
created: 2026-09-21
updated: 2026-09-22
---

# Jo Kristian Bergum

[[hornet|Hornet]] CEO. **이 위키에 들어온 첫 정보 검색(IR) 전공자**다.

지금까지 이 위키의 검색 논의는 전부 **에이전트를 만드는 쪽**에서 나왔다 — [[retrieval-augmented-generation|RAG]]는 [[ibm|IBM]]의 에이전트 지식 조달 4갈래 중 하나였고([[agent-knowledge-sourcing]]), [[reference-graph-vs-vector-search]]는 코드 인덱싱 도구를 파는 쪽이 세웠고, [[agent-collaboration-as-search]]는 멀티 에이전트를 검색으로 **재해석**한 것이었다. **검색 자체를 20년 해 온 사람이 검색을 말하는 것은 이번이 처음**이고, 그래서 이 소스만 **BM25의 하이퍼파라미터·top-K 가속·nDCG 같은 IR 내부 어휘**를 쓴다.

## 소스에서 확인되는 것

- **[[hornet|Hornet]] CEO** — *"에이전트를 위한 검색 인프라를 구축"* (00:28~00:33).
- **경력 20년 이상** — *"검색 및 정보 추출 문제를 오랫동안 연구했습니다. 보시다시피 저는 흰머리가 많습니다. 이 분야에서 20년 넘게 일해 왔습니다"* (00:33~00:42). 설명란도 *"20년 이상 검색 엔진을 연구"* 로 같은 말을 한다.
- **노르웨이 사람으로 보인다** — *"저도 월드컵 보고 있어요. 노르웨이는 후반전에 코트디부아르와 경기를 합니다. 노르웨이가 선두를 달리고 있으니 좋은 일이죠"* (00:17~00:23). ⚠️ **국적을 직접 말하지는 않는다.**
- **벤치마크를 좋아한다고 자처한다** — *"저는 벤치마크에 대해 이야기하는 것을 좋아합니다"* (04:44~04:46). 실제로 발표의 절반이 [[browsecomp-plus|BrowseComp-Plus]] 위에서 진행된다.
- **자사 블로그에 [GPT-5] 쿼리 궤적 분석을 썼다** — *"최근 블로그 게시물에서도 이에 대해 설명했습니다. `hornet.dev` 에서 찾을 수 있습니다"* (08:39~08:43).

## 이 위키에서의 위치

이 화자가 세운 것은 **[[agentic-search]]** 의 정의(*에이전트 루프 내부에서의 검색*)와 그 아래 다섯 페이지다 — [[bm25]] · [[llm-as-search-user]] · [[retrieval-not-reasoning-bottleneck]] · [[context-window-as-floppy-disk]] · [[ir-evaluation-obsolescence]]. 그리고 [[which-bm25-problem]]은 **같은 날 [[benjamin-clavie|Clavié]]가 독립적으로 같은 지적**을 해서 두 출처를 한꺼번에 얻었다.

가장 멀리 가는 주장은 **검색이 AGI보다 오래 산다**는 것이다 — [[context-window-as-floppy-disk]].

> ⚠️ **당사자 진술이 섞인다.** 발표 마지막 1/4(15:23~16:23)은 **자사 엔진 vs "익명화된 엔진들"** 의 처리량 비교이고 상대의 이름·설정이 전부 없다. **그리고 화자가 자기 그래프의 Y축을 QPS라고 했다가 지연 시간으로 정정한다**(16:12~16:23). 이 위키는 **그 수치를 인용하지 않는다.** 앞 3/4는 제품과 무관한 논증이다.

## 미해결

- **행사 이름** — 설명란에 없고 화자도 말하지 않는다. → [[tech-bridge-bm25-agentic-search]]
- **촬영 시점** — 월드컵 언급이 있으나 대회·연도를 말하지 않는다.
- **[[hornet|Hornet]]의 규모·자금·창업 시점** — 한 마디도 없다.
- ⚠️ **자막 양 트랙이 성을 *"Bergum"* 이 아니라 *"Joe Bergum"* 으로 적는다.** 설명란의 **Jo Kristian Bergum** 을 따랐다.


## 하루 뒤의 반대 진영 (2026-09-22 추가)

[[will-bryk|Will Bryk]]([[exa|Exa]])이 **같은 질문에 반대로 답하는 발표**로 들어왔다 — 키워드는 간단한 쿼리까지이고 복잡한 쿼리는 임베딩이 필요하다는 것. 전체 대조는 [[tech-bridge-exa-perfect-search-for-agents]] 참조.

⚠️ **Bryk은 이 화자의 세 근거(정확 일치·비용·설명 가능성)에 하나도 답하지 않는다** — 반박이 아니라 **닿지 않는다.** 그리고 **두 사람 다 정확도 수치를 한 개도 제시하지 않는다.**

✅ **한 가지는 Bryk이 더 멀리 간다** — 이 화자는 *사용자가 바뀌었다* 에서 멈췄는데, Bryk은 **왜 기존 엔진이 그 사용자에게 맞지 않는지**를 목적함수로 설명한다([[search-as-recommendation-engine]]). 그리고 *사람이 짧게 치는 이유* 에 대한 두 번째 읽기를 연다 → [[suppressed-query-demand]].

## References

- [[tech-bridge-bm25-agentic-search]] · [[hornet]] · [[tech-bridge]] · [[tech-bridge-exa-perfect-search-for-agents]]
- 개념: [[agentic-search]] · [[bm25]] · [[which-bm25-problem]] · [[llm-as-search-user]] · [[retrieval-not-reasoning-bottleneck]] · [[context-window-as-floppy-disk]] · [[corpus-as-filesystem-workspace]] · [[ir-evaluation-obsolescence]] · [[ride-the-optimization-trajectory]]
- 같은 무대: [[benjamin-clavie]]
