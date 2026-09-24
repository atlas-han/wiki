---
title: Oracle
type: entity
category: org
tags: [database, cloud, enterprise, agent-memory, vendor]
aliases: [오라클, OCI, Oracle Cloud Infrastructure]
links:
  - https://www.oracle.com/
sources: [tech-bridge-oracle-agent-memory-harness]
created: 2026-09-24
updated: 2026-09-24
---

# Oracle

데이터베이스·클라우드(OCI) 기업. 이 위키에는 [[ignacio-martinez|Ignacio Martinez]]의 워크숍([[tech-bridge-oracle-agent-memory-harness]], 2026-09-23 업로드)으로 처음 들어왔다 — **에이전트 메모리의 저장 계층을 파는 벤더**로서다.

> ⚠️ 이 페이지의 제품 서술은 **전부 발표자(Oracle 직원)의 주장**이다. 측정값·가격·벤치마크가 없다.
>
> (이 위키의 [[oracle-gap|오라클 갭]]은 *완벽한 문서(oracle)* 라는 IR 용어로, 이 회사와 **무관**하다.)

## 소스에 나온 제품·주장

| 제품 | 소스의 설명 | 시각 |
|---|---|---|
| **Oracle DBFS** | 데이터베이스 안의 파일 시스템 — 파일 인터페이스 + ACID·벡터 검색·관계·보안·고가용성 | 17:18~17:42 |
| **LangChain Oracle DB** | 벡터 스토어 삽입·검색·retrieve를 쉽게 하는 LangChain 통합 | 18:19~18:30 |
| **In-database embeddings** | 임베딩 모델이 DB 안에 있어 **제3자 서비스 호출이 없다** → 데이터 보존·보안 | 18:33~18:58 |
| **컨버지드 데이터베이스** | JSON·관계형·공간·그래프·벡터를 한 엔진·한 쿼리 인터페이스로. ⚠️ *"우리는 시장에서 유일한 컨버지드 데이터베이스"* | 21:16~22:22 |
| **Oracle Agent Memory Package (OAMP)** | 관리형 에이전트 메모리(Python). 압축·요약·추출·토큰 예산 결정을 *"단 한 줄의 코드로"*. **컨텍스트 카드** 생성 | 27:51~29:57 |
| **OCI Generative AI** | 관리형 추론 서비스. *"구글, 메타와 파트너십 (…) 당분간은 OpenAI와 xAI"* — *"엔터프라이즈판 OpenRouter"* | 42:27~42:51 |

**OAMP 컨텍스트 카드의 구조**(28:51~29:44): 주제(모델의 방향) · 요약(스레드 압축 + 에이전트의 현재 의도) · 관련 정보(**사실 · 선호 · 기억**) · 일화 기억(**아직 답이 나오지 않은 질문을 명시적으로 추적**) · 최근 메시지(지역 맥락). 모델에 직접 가는 것이 아니라 **하네스가 쓰는 추상화**라고 청중 질문에 확인한다(30:03~30:09). OAMP 개발에 동료 *"Valentine"*(27:31~27:42, 성 없음)이 참여했다. Discord 서버 운영(38:05~38:12). → [[agent-memory]] · [[context-resets-and-compaction]]

## 이 벤더가 서 있는 자리

화자의 에이전트 스택 5계층(애플리케이션·데이터·모델·인프라·컴퓨트)에서 *"데이터만 상품화되지 않는다"*(03:48~04:13) — **Oracle 제품이 있는 층이 곧 "우리가 통제할 수 있는 유일한 층"** 이 된다. [[model-harness-knowledge-stack|Google의 모델·하네스·지식 3계층]](09-23)이 자사 모델·하네스·스킬을 층마다 배치한 것과 **같은 형식의 벤더 스택 그림**이다.

⚠️ **보안 논거가 반쪽이다** — 컨버지드 DB는 *"단일 공격 벡터만 걱정하면 된다"*(22:04~22:14)고 하는데, 단일 저장소는 **폭발 반경이 전부**라는 반대편을 말하지 않는다. → [[tech-bridge-oracle-agent-memory-harness]]

## References

- [[tech-bridge-oracle-agent-memory-harness]] · [[ignacio-martinez]]
- [[files-vs-database-agent-memory]] · [[agent-memory]] · [[retrieval-augmented-generation]] · [[model-harness-knowledge-stack]]
