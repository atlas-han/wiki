---
title: Memex
type: concept
category: theory
tags: [hypertext-precursor, knowledge-base, history-of-computing, associative-trails]
related: [llm-wiki-pattern]
first-seen: karpathy-llm-wiki-gist
sources: [karpathy-llm-wiki-gist, tech-bridge-karpathy-transformers-stanford]
created: 2026-05-25
updated: 2026-09-03
---

# Memex

**"Memory" + "index"** 의 합성어. [[vannevar-bush|Vannevar Bush]]가 1945년 *Atlantic Monthly* 에세이 ["As We May Think"](https://www.theatlantic.com/magazine/archive/1945/07/as-we-may-think/303881/)에서 제시한 가상의 전기기계 장치. 개인용 지식 저장·연관 탐색 시스템의 사상적 원형.

## 디자인 (Bush의 비전)

- 마이크로필름 저장·카메라·리더가 통합된 **책상형 장치**
- 반투명 스크린으로 자료 열람, 투명 platen으로 문서·노트를 사진 촬영
- *Electric photocell*이 코드 심볼을 읽어 색인·검색
- "개인의 모든 책·기록·소통을 압축 저장"하는 personal filing system

## 핵심 혁신 — Associative Trails

가장 영향력 있는 아이디어. 사용자가 문서들 사이에 **연관 경로(trail)** 를 구축할 수 있다. 선형 색인이 아니라 인간 기억의 연상 방식을 모방. 사용자는 자기 관심사의 trail을 만들고 동료에게 공유 가능.

> A trail of his interest through the maze of materials available to him.

## 영향사 (계보)

| 인물 | 이어받은 것 |
|---|---|
| **Douglas Engelbart** | "augment human intellect" 비전, 개인용 컴퓨터 개념 |
| **Ted Nelson** (1965) | "hypertext" 용어 명명, 직접적으로 Bush 인용 |
| **Tim Berners-Lee** (1989) | World Wide Web — trail은 hyperlink가 됨 |
| **DARPA Memex Program** (2014) | 다크웹 범죄 수사를 위한 검색 도구 (이름 차용) |
| **Transformer scratch pad** (~2023) | 모델에게 외부 노트를 주는 발상 — [[tech-bridge-karpathy-transformers-stanford]] |
| **[[llm-wiki-pattern]]** (2026) | LLM이 trail의 유지보수자, [[karpathy-llm-wiki-gist|Karpathy 명시 인용]] |

## Bush가 풀지 못한 것 — 유지보수자

Bush의 비전은 *trail을 만들고 유지하는 사람의 시간*을 가정했다. 실제 인간은 그 부담을 견디지 못해 위키들은 쇠퇴한다. [[llm-wiki-pattern]]의 핵심 주장:

> The part [Bush] couldn't solve was who does the maintenance. The LLM handles that.
> — [[andrej-karpathy|Karpathy]] ([[karpathy-llm-wiki-gist]])

본 vault 자체가 그 가설의 instantiation.

## 왜 기계가 노트를 쓰는가 — 아키텍처 쪽 동기

Bush의 memex는 **인간의 기억 한계**에서 출발했다. [[tech-bridge-karpathy-transformers-stanford]]는 같은 처방이 **모델의 기억 한계**에서도 독립적으로 도출됨을 보여준다. [[transformer]]의 컨텍스트 길이는 유한하고, [[andrej-karpathy|Karpathy]]는 그것을 늘리는 대신 노트를 주자고 제안하며 **사람의 노트 습관을 직접 비유로 든다.**

> 그건 사람이 노트를 쓰는 법을 배우는 것과 똑같습니다. 머릿속에 다 넣어둘 필요가 없죠.

즉 Bush의 계보에서 LLM은 단지 **유지보수자**로 합류한 것이 아니라, 애초에 memex를 필요로 하는 **또 하나의 유한한 기억 장치**로도 합류한다. 이 vault는 두 역할을 동시에 수행한다 — 사람의 associative trail이자 모델의 scratch pad.

## References

- [[karpathy-llm-wiki-gist]]
- [[vannevar-bush]]
- [[llm-wiki-pattern]]
- [Wikipedia: Memex](https://en.wikipedia.org/wiki/Memex)
- [As We May Think (Atlantic, 1945)](https://www.theatlantic.com/magazine/archive/1945/07/as-we-may-think/303881/)
