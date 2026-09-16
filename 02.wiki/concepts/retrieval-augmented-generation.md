---
title: Retrieval-Augmented Generation (RAG)
type: concept
category: technique
tags: [rag, retrieval, vector-db, semantic-search, context]
aliases: [RAG, 검색 증강 생성]
related: [agent-memory, agent-knowledge-sourcing, context-engineering, agentic-sites, llm-wiki-pattern, code-knowledge-graph, agent-collaboration-as-search]
first-seen: tech-bridge-agent-knowledge-four-ways
sources: [tech-bridge-agent-knowledge-four-ways, tech-bridge-agentic-sites, karpathy-llm-wiki-gist, tech-bridge-agent-to-agent-as-search, tech-bridge-graft-code-knowledge-graph, tech-bridge-ai-engineer-three-tier-skill-stack]
created: 2026-09-08
updated: 2026-09-16
---

# Retrieval-Augmented Generation (RAG)

컨텍스트 창에 모든 것을 미리 넣는 대신, **필요할 때 외부 소스에서 관련 조각만 가져와** 생성에 쓰는 기법.

> 핵심은 **모든 정보를 컨텍스트 창에 미리 입력하는 대신**, 에이전트가 필요한 정보, 즉 **외부 소스에서 관련 정보만 가져와 실제로 필요할 때만** 처리한다는 것입니다. — [[tech-bridge-agent-knowledge-four-ways]]

> 📌 **이 페이지는 늦게 생겼다.** RAG는 이 위키가 [[agentic-sites]]·[[llm-wiki-pattern]]·[[code-knowledge-graph]]·[[karpathy-llm-wiki-gist]]에서 **대비항으로만 계속 언급**해 온 용어였고, 2026-09-08에 [[tech-bridge-agent-knowledge-four-ways]]가 처음으로 RAG 자체를 설명하면서 페이지가 섰다.

## 동작

1. 문서 모음을 준비한다 — 소스의 예시는 **매뉴얼·의존성 맵**.
2. 에이전트가 질문을 던진다.
3. **의미 검색(semantic search)** 으로 일치하는 조각을 찾는다.
4. **관련 청크가 컨텍스트 창으로 반환된다.**

저장소는 통상 **벡터 데이터베이스**다.

## RAG를 정의하는 것은 검색 기술이 아니라 출처

[[agent-memory|메모리]]와 나란히 놓았을 때에만 RAG의 경계가 분명해진다. 둘 다 *필요할 때 관련 지식을 불러오고*, 둘 다 벡터 DB일 수 있으며, 둘 다 의미 검색을 쓸 수 있다.

> 언뜻 보면 메모리는 (…) **RAG와 상당히 유사해 보이지만** (…) **차이점은 그 지식이 어디에서 오는가에 있습니다.**

> RAG는 **벡터 데이터베이스에 저장된 문서**를 읽는데, 그 문서들은 **사람이 직접 벡터 데이터베이스에 넣은 것**들입니다. 마치 **일부러 거기에 보관해둔** 것 같았어요.

| | RAG | [[agent-memory\|메모리]] |
|---|---|---|
| **지식의 출처** | **사람이 의도적으로 적어 넣은 문서** | 에이전트가 겪고 스스로 저장한 경험 |
| **쓰기 주체** | 사람 | 에이전트 |
| **방향** | 읽기 | **읽고 쓴다** |
| 저장소·검색 | 벡터 DB · 의미 검색 | (같을 수 있다) |

→ [[agent-knowledge-sourcing]]

## 이 위키의 다른 RAG 사례

- **[[agentic-sites]]** — [[carlos-sanchez]]의 *"자기 사이트 RAG"*. 방문자 의도에 맞춰 자기 사이트의 블록을 검색해 재조립한다. **1~2초 예산** 안에서 도는 것이 제약이고, 그래서 작은 모델([[gemma-4]])+빠른 추론([[cerebras]]) 조합을 쓴다. → 이 위키에서 **RAG에 정량적 제약이 붙은 유일한 사례**다.
- **[[llm-wiki-pattern]]·[[karpathy-llm-wiki-gist]]** — LLM 위키는 RAG의 **대안**으로 제시된다. 검색해서 조각을 끌어오는 대신, **미리 합성해 둔 페이지**를 읽는다.
- **[[code-knowledge-graph]]** — 코드에 대해 청크 검색 대신 **구조를 그래프로** 둔다.

세 사례가 같은 축 위에 있다 — **검색 시점에 조각을 모을 것인가, 미리 합성해 둘 것인가.** [[tech-bridge-agent-knowledge-four-ways]]는 이 축을 다루지 않고 RAG를 기본형으로만 설명한다.

## 미해결 사항

- **RAG와 [[agent-memory|메모리]]가 어긋날 때** 무엇을 믿는가. 소스의 예시 자체가 이 충돌을 품고 있다 — *"실제 원인은 여기 런북에 기록되지 않은 내용이었을 수도 있습니다"*. 즉 **문서가 틀렸고 경험이 맞았던 사례**인데, 판정 규칙은 없다. [[context-engineering]]의 신뢰 등급 슬롯이 다루는 문제와 같은 자리다.
- 청킹·임베딩·재랭킹 등 구현 층위는 이 위키의 어느 소스도 다루지 않았다.
- 비용·지연 특성 (첫 소스에 수치가 없다).

## 세 단계 역사 속의 자리 (2026-09-10)

[[tech-bridge-agent-to-agent-as-search]]가 RAG를 **중간 단계**로 놓는다 — *"4년 전에는 사람이 컨텍스트 창을 수동으로 채웠다. 몇 년 전에는 대부분이 RAG를 했다 — '여러 시스템을 훑어 데이터를 가져오는 검색 도구를 두자.' 그러자 '그건 확장이 잘 안 되고 문제가 있어.' 그리고 지금은 다들 에이전틱 검색이다."* 그리고 셋을 한 문장으로 묶는다: *"대부분의 LLM 시스템은 그냥 검색 문제다."* → [[agent-collaboration-as-search]]. 이 페이지가 RAG를 *출처* 로 정의한 것과 충돌하지 않는다 — Greze의 분류는 *메커니즘의 세대* 이고 IBM의 분류는 *지식의 출처* 다. ⚠️ *"확장이 잘 안 된다"* 의 근거는 소스에 없다.


## 2026-09-15 — 코드 도메인에서 벡터 경로가 약한 이유

[[tech-bridge-graft-code-knowledge-graph]]가 기존 벡터 기반 코드 검색을 명시적으로 기각한다.

> **계정을 만드는 코드와 계정을 지우는 코드는 둘 다 "계정" 질문에 걸리지만 정반대 일을 합니다. 잘못 고르면 대가가 큽니다.**

자연어 문서에서는 유사도가 대체로 관련성이지만 **코드에서는 반대말이 가장 비슷하게 생긴다.** 그리고 편집 작업이 정말 알아야 하는 것은 *"이걸 바꾸면 무엇이 깨지는가"* 인데 **그건 유사도가 아니라 의존 관계**다. 소스는 이것을 채택률로 뒷받침한다 — *"대부분의 코딩 에이전트는 아예 쓰지 않습니다."*

2026-09-08 IBM 편이 *"컨텍스트에 다 쏟아붓지 말고 경로를 나눠라"* 로 이 페이지를 세웠다면, 이 소스는 **그 경로 중 하나의 적용 범위를 좁힌다** → [[reference-graph-vs-vector-search]].

> ⚠️ **당사자 진술이다** — 대안([[graft]])을 파는 쪽의 말이고, 하이브리드 논의는 하지 않는다. 벡터 검색 쪽 반론은 이 위키에 아직 없다.

## References

- [[tech-bridge-agent-knowledge-four-ways]] — RAG를 [[agent-skills]]·[[model-context-protocol]]·[[agent-memory]]와 나란히 정의한 첫 소스
- [[tech-bridge-agentic-sites]] · [[karpathy-llm-wiki-gist]]
- 관련: [[agent-knowledge-sourcing]] · [[agent-memory]] · [[context-engineering]] · [[agentic-sites]] · [[llm-wiki-pattern]] · [[code-knowledge-graph]]
- [[tech-bridge-agent-to-agent-as-search]] — 수동→RAG→에이전틱 검색의 세 단계 (2026-09-10)

## 2026-09-16 — 파이프라인 서술이 처음 들어왔다

이 페이지의 미해결 항목 *"청킹·임베딩·재랭킹 등 구현 층위는 이 위키의 어느 소스도 다루지 않았다"* 를 [[tech-bridge-ai-engineer-three-tier-skill-stack]]([[cedric-clyburn|Cedric Clyburn]], [[ibm|IBM Technology]])이 **부분적으로** 채운다.

> 문서들이 파이프라인으로 들어옵니다. **우리가 쓸 데이터 소스에 맞도록 고정된 크기로 청킹**됩니다. **벡터, 즉 수치 표현으로 임베딩되어 데이터베이스에 저장되고 검색**됩니다. 질문이 오면 **그 질문에 데이터베이스나 벡터 소스에서 검색한 관련 정보를 더하고, 관련 정보와 질문을 둘 다 대규모 언어 모델의 컨텍스트 창에** 넣습니다. **사실 정보에 근거하면서도 자연어로 된** 결과를 얻습니다. (05:58~06:48)

| 단계 | 소스의 말 |
|---|---|
| 청킹 | **고정 크기** — 데이터 소스에 맞춰 |
| 임베딩 | 수치 벡터 — *"키워드 일치가 아니라 의미"* (*Kubernetes ↔ 컨테이너·오케스트레이션*) |
| 저장·검색 | 데이터베이스, **유사도** |
| 증강 | 질문 + 검색 결과 → 컨텍스트 창 |
| 생성 | 근거 있는 자연어 |

**재랭킹·청크 크기 결정·평가는 여전히 없다.** 정당화는 **환각 방지**(*"학습되지 않은 회사 정책·법률 문서를 지어내는 대신"*)이고, 채택률 주장이 붙는다 — *"AI를 실험하는 거의 모든 회사는 어떤 형태로든 RAG를 원한다, 임베딩을 쓰지 않더라도"*(⚠️ 근거 없음). 09-07 IBM 편([[tech-bridge-agent-knowledge-four-ways]])의 정의와 **일치**한다 — 같은 채널, 같은 설명.

2026-09-15 [[tech-bridge-graft-code-knowledge-graph|Graft 편]]이 *"코드에서는 유사도가 방향을 모른다"* 고 한 것과 나란히 두면, **이 소스의 예시는 전부 자연어 문서**(회사 정책·법률 문서·PDF·HR·병원)다. 모순이 아니라 **도메인이 다르다.** ⚠️ ko가 07:00에서 *retrieval augmented generation* 을 **"증강 현실 생성"** 으로 옮겼다.
