---
title: Andrej Karpathy
type: entity
category: person
tags: [researcher, educator, llm, transformer, computer-vision]
aliases: [카파시, Karpathy, 안드레 카파시]
sources: [karpathy-llm-wiki-gist, multica-karpathy-skills-claude-md, tech-bridge-karpathy-transformers-stanford, tech-bridge-six-agent-skills]
links:
  - https://karpathy.ai
  - https://github.com/karpathy
created: 2026-05-25
updated: 2026-09-05
---

# Andrej Karpathy

AI 연구자·교육자. 본 위키에 두 갈래로 등장한다 — **위키 운영 패턴의 원안 저자**이자, **트랜스포머 아키텍처의 해설자**.

## 위키 패턴 쪽

- [[llm-wiki-pattern]] 제안자 — RAG와 대비되는 누적적 지식 베이스 패턴. 2026년 gist [[karpathy-llm-wiki-gist]]가 이 LLM-WIKI 구조의 사상적 출처이고 `CLAUDE.md` 헤더가 직접 인용한다.
- "Obsidian = IDE, LLM = programmer, wiki = codebase" 비유의 출처
- [[memex|Memex]] ([[vannevar-bush]], 1945) 계보를 명시적으로 호명하며 LLM이 그 유지보수 부족 문제를 해결한다고 주장
- [[multica-ai]]의 GitHub repo `andrej-karpathy-skills`가 이름을 직접 차용 — Karpathy의 *skills* 컨셉에서 영감 (본인 endorsement 여부 미확인). [[multica-karpathy-skills-claude-md]] 참조

## 연구·교육 쪽 (2026-09-03 추가)

[[tech-bridge-karpathy-transformers-stanford]] (Stanford CS25, **~2023년 강연**의 2026년 재배포)에서 확인된 것:

- **2012년경 AI에 진입**했고 컴퓨터 비전이 전공이었다. 당시를 회고하며 *"AI에 합류했다는 말조차 하지 않았죠. 그건 마치 욕설 같았어요"* 라고 말한다.
- 2011년 비전 파이프라인의 실상에 대한 1인칭 증언 — 특징 기술자를 수십 개 추출해 SVM을 얹던 시절, *"여기저기서 코드를 모아서 실행했는데, 정말 악몽 같았어요"*. [[sutton-bitter-lesson]]의 컴퓨터 비전 항목에 대한 당사자 근거.
- **[[nanogpt|nanoGPT]]** 저자. 강연 시점에 "지금 하고 있는 일"로 지목했고, 컴퓨터 비전 제품에서 언어 도메인으로 옮겨가는 중이라고 밝혔다.
- **Tesla** 재직 경험을 멀티모달 설계 사례로 든다 — ConvNet에 radar·지도·차종을 어떻게 넣을지가 매번 문제였는데 [[transformer]]는 "썰어서 집합에 던져 넣으면" 된다는 것.
- **[[dzmitry-bahdanau]]에게 직접 이메일을 보내** [[attention-mechanism|어텐션]]의 탄생 경위를 확인했다. 이 위키의 어텐션 계보 서술은 그 답장에 근거한다.

### 이 강연에서 나온 그의 프레이밍

| 프레이밍 | 내용 |
|---|---|
| **어텐션 = 그래프 메시지 전달** | 본인이 *"어제 생각해냈다"*고 농담한 개인적 재해석. → [[attention-mechanism]] |
| **트랜스포머가 이긴 3가지 이유** | 표현력 · 최적화 가능성 · **GPU 효율성**. 3번이 가장 저평가됐다고 주장 |
| **범용 컴퓨터 재명명** | *"GPT는 런타임에 재구성되어 자연어 프로그램을 실행하는 범용 컴퓨터"* → [[transformer]] |
| **in-context learning이 핵심** | GPT-3 논문 제목을 바꾸고 싶다고 말한다 → [[in-context-learning]] |
| **scratch pad** | 컨텍스트를 늘리는 대신 모델에게 노트를 주자 — 본인의 [[llm-wiki-pattern]]을 3년 앞서 예고한 셈 |

### 밝힌 선호·불만

- **autoregressive를 좋아하지 않는다** — *"토큰을 샘플링하고 거기에 커밋해 버리는 게 이상하다"*. diffusion 하이브리드를 선호한다고 밝힘
- **graph neural network라는 용어가 헷갈린다** — *"오늘날에는 어쩌면 모든 게 graph neural network"*
- inductive bias 주입은 **데이터 규모에 달렸다**고 본다 — 데이터가 많으면 덜 넣는 쪽이 낫다

## 미해결 사항

- OpenAI 시절 작업 미반영. Tesla는 위 강연에서 **사례로만** 언급됐고 재직 기간·역할은 확인 안 됨
- "Zero to Hero" 시리즈 등 다른 강의 미반영
- 2023년 강연 이후 ~2026년 사이의 활동 공백 — [[karpathy-llm-wiki-gist]](2026)와 위 강연(~2023) 사이를 잇는 소스가 없다

## 이름이 붙은 코딩 규칙의 재유통 (2026-09-05 · [[tech-bridge-six-agent-skills]])

[[ai-labs]]의 스킬 카탈로그에 *"[[andrej-karpathy|Karpathy]]의 조언을 네 가지 규칙으로 바꾼"* 스킬이 포함됐다. 실체는 [[multica-ai]]의 `andrej-karpathy-skills` repo이고 이 위키가 [[multica-karpathy-skills-claude-md]]로 이미 갖고 있던 것이다.

⚠️ **이 위키에 Karpathy 본인이 그 규칙을 썼거나 승인했다는 근거는 없다.** repo 이름과 영상의 표현 모두 *"Karpathy의 조언에서 온"* 정도이고, 두 소스 어디에도 본인의 직접 인용이나 endorsement가 없다. 이름이 **규칙 집합의 브랜드로 유통되고 있다**는 사실 자체는 기록해 둘 만하다.

## References## References

- [[karpathy-llm-wiki-gist]]
- [[multica-karpathy-skills-claude-md]]
- [[tech-bridge-karpathy-transformers-stanford]]
