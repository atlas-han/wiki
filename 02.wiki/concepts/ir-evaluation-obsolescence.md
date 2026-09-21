---
title: 고전적 IR 평가의 종말 (The End of Classical IR Evaluation)
type: concept
category: theory
tags: [evaluation, ndcg, information-retrieval, agentic-search, benchmark]
aliases: [nDCG는 끝났다, 단일 쿼리 평가]
related: [agentic-search, llm-as-search-user, browsecomp-plus, which-bm25-problem, skill-evals, field-level-unit-test-evals, all-or-nothing-accuracy, agent-roi-measurement]
first-seen: tech-bridge-bm25-agentic-search
sources: [tech-bridge-bm25-agentic-search]
created: 2026-09-21
updated: 2026-09-21
---

# 고전적 IR 평가의 종말

**쿼리 하나에 순위 목록 하나를 놓고 nDCG를 계산하던 평가는, 사용자가 쿼리를 열 번 고쳐 던지는 순간 잴 것을 잃는다.**

> 기존 정보 검색에서는 **하나의 쿼리, 하나의 순위 목록, NDCG 계산 및 비교**만 하는 방식이 일반적이었습니다. **새로운 사용자[에이전트]가 등장하면 더 이상 그 부분은 그다지 중요하지 않습니다.** 왜냐하면 그 에이전트는 **쿼리를 재구성하고, 더 많은 쿼리를 수행하고, 확장하는 등** 다양한 작업을 할 수 있기 때문입니다. **그래서 기존의 정보 검색 평가 방식은 이제 거의 쓸모없어졌습니다.** — [[jo-bergum]], [[tech-bridge-bm25-agentic-search]] (14:45~15:09)

대안은 한 문장이다:

> 그 대신, **모델이 설정된 작업을 수행할 수 있는지 살펴보세요.** 예를 들어 질문에 답하는 경우, **정답을 맞히는가?** (15:11~15:19)

## 왜 무너지나

| 전제 | 고전적 IR | [[agentic-search\|에이전트 검색]] |
|---|---|---|
| 쿼리는 **하나** | ✅ | ❌ 궤적이다 |
| 결과를 **사람이 훑는다** | ✅ (파란 링크 10개) | ❌ 모델이 읽고 **재구성한다** |
| **순위**가 값이다 | ✅ (위에 있을수록 좋다) | ❌ 모델은 아래도 읽고 다시 던진다 |
| 관련성이 **쿼리에 대해** 정의된다 | ✅ | ❌ **작업**에 대해 정의된다 |

**마지막 줄이 핵심이다.** 고전적 지표는 *이 문서가 이 쿼리에 관련되는가*를 매긴다. 에이전트 루프에서 값은 **그 문서가 최종 작업을 성공시켰는가**이고, 이 둘은 **같지 않다** — 관련성 낮은 문서가 다음 쿼리의 단서를 주기도 한다.

## 이 위키의 평가 축에 붙는 자리

이 위키는 *무엇을 재는가*를 세 번 다시 물어 왔고, 그때마다 **해상도가 안쪽으로 밀렸다.**

| 페이지 | 재는 단위 | 언제 |
|---|---|---|
| [[agent-roi-measurement]] · [[mousepower]] | 조직·사람의 산출 | 09-15 |
| [[skill-evals]] | 스킬 하나 | 09-02 |
| [[field-level-unit-test-evals]] | **필드 하나** | 09-19 |
| **이 페이지** | **작업 하나의 종단 성공** | 09-20 |

**방향이 반대다.** 앞의 셋은 *더 잘게 쪼개서 재라*였고, 여기서는 **더 크게 묶어서 재라**이다 — 중간 지표(nDCG)가 종단 결과와 어긋나기 때문이다.

같은 긴장이 [[all-or-nothing-accuracy]]에 이미 있었다. 그쪽은 *부분 점수가 의미 없는 과제가 있다*였고, 여기서는 **부분 점수(순위 품질)가 존재하지만 종단과 상관이 깨졌다**고 말한다.

## ⚠️ 그런데 종단 평가도 조건에 민감하다

이 소스 자신이 그 증거를 준다 — [[browsecomp-plus|BrowseComp-Plus]]의 **BM25 기준선 매개변수가 잘못 설정돼 있어서** 종단 정확도 비교가 통째로 기울었다는 것([[which-bm25-problem]]).

**즉 "작업을 해냈는가"로 옮겨도 측정의 문제는 사라지지 않는다. 옮겨갈 뿐이다** — 순위 지표의 설정에서 **하네스·도구·기준선의 설정**으로.

> ⚠️ **소스는 대안 프로토콜을 제시하지 않는다.** *"작업을 해냈는지 보라"* 가 전부다. **몇 번 돌리는지, 분산을 어떻게 다루는지, 비용을 어떻게 셈하는지** 말하지 않는다. (같은 날 [[benjamin-clavie|Clavié]]가 *"89.8에서 90.2로의 도약은 중요하지 않은 실행 편차"*(10:16~10:23)라며 **분산 문제를 지나가듯 인정**하는데, 그쪽도 프로토콜은 주지 않는다.)

## References

- [[tech-bridge-bm25-agentic-search]] · [[jo-bergum]] · [[browsecomp-plus]]
- 개념: [[agentic-search]] · [[llm-as-search-user]] · [[which-bm25-problem]] · [[retrieval-not-reasoning-bottleneck]]
- 평가 축: [[skill-evals]] · [[field-level-unit-test-evals]] · [[all-or-nothing-accuracy]] · [[agent-roi-measurement]] · [[mousepower]]
