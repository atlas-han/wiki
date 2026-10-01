---
title: Lineage 기반 위험 가시성 (Lineage-Driven Risk Visibility)
type: concept
category: pattern
tags: [security, data-security, data-lineage, observability, data-transformation, rag, agents, dlp]
aliases: [lineage-driven risk visibility, 데이터 계보 기반 가시성, data lineage, 데이터 계보, 변환 인지 추적]
related: [ai-data-exposure, retrieval-augmented-generation, agent-governance-layers, continuous-security-validation, production-trace-eval-flywheel]
first-seen: tech-bridge-ai-data-exposure-hidden-risk
sources: [tech-bridge-ai-data-exposure-hidden-risk]
created: 2026-10-01
updated: 2026-10-01
---

# Lineage 기반 위험 가시성

**민감 데이터를 원본의 형태로만 찾지 않고, 출처 → (RAG·에이전트·시스템에 의한) 변환 → 전파 → 최종 목적지까지의 계보(lineage)로 추적해, 형태가 바뀌거나 파생된 사본도 원본과 같은 위험으로 보는 것.** [[jeff-crume|Jeff Crume]]([[ibm|IBM]])이 [[tech-bridge-ai-data-exposure-hidden-risk]]에서 [[ai-data-exposure|AI 데이터 노출]] 관리의 요구사항 ②로 제시했다.

> *"Next thing we need is something that shows the lineage driven risk visibility. So data gets transformed by rag[=RAG], AI agents and systems and things of that sort may also do transformations and then we need to see how the data propagates through the system and it will be changed as it propagates in some cases."* (09:52~10:13)

## 왜 필요한가 — 형태가 바뀌면 놓친다

> *"I've got data transformations that are going to occur. The information looked like this, but now it's in some other form. I still need to know about that. If I'm looking for it in only this form, I might miss it and not realize that the data has leaked out."* (05:33~05:46)

같은 문제가 사람 쪽(workforce)에서는 **파생 파일**로 나타난다:

> *"I have a main file and then there are child files that could be derived from that. And I need to be able to track all of those just as I did the original file that had the sensitive information."* (06:33~06:45)

즉 **민감도는 형태가 아니라 계보를 따라 상속된다** — 요약·임베딩·청크·복사본·파생 파일이 모두 원본의 민감도를 물려받는다는 것이 이 패턴의 전제다(⚠️ "상속"은 위키의 표현, 화자는 *"track all of those just as I did the original"*).

## 보여야 하는 세 칸

*"I need to be able to show the sources of where the data came from. I need to be able to show these transformations (…) And then ultimately, where does all this information go?"*(05:52~06:04). 통합 플랫폼 요구에서 다시:

| 칸 | en-orig |
|---|---|
| **출처** | *"where did the data come from"* (07:11) |
| **이동·변환** | *"how did it move through (…) the system"* (07:13) · *"it will be changed as it propagates"* (10:11~10:13) |
| **목적지** | *"then it went through this AI, and then it ended up on this endpoint system"* (07:16~07:21) |

## 이 위키에서의 좌표

- **[[production-trace-eval-flywheel]]** — 같은 "트레이스를 따라간다"는 발상이 **품질** 쪽에 있다(W&B, 09-29). 거기서는 에이전트 실행 트레이스를 eval 태스크로 옮기고, 여기서는 **데이터 트레이스**를 위험 판정에 쓴다. 두 소스는 서로 관계없다 — ⚠️ 위키의 대응.
- **[[retrieval-augmented-generation]]** — RAG 파이프라인이 **변환 지점**으로 처음 지목된다. 그 페이지에 기록된 *PII 가리기*(Oracle 편 적재 단계)는 변환이 민감도를 **줄이는** 경우이고, 이 페이지의 우려는 변환이 민감도를 **숨기는** 경우다.
- **[[agent-governance-layers]]** — 거기 모인 벽들은 대부분 *접근 시점*에 선다. lineage는 *접근 이후*를 본다.

## ⚠️ 미해결

- **어떻게** 변환된 데이터를 원본과 연결하는가(핑거프린트? 메타데이터 전파? 분류기 재적용?) — 소스는 요구만 말하고 방법은 없다.
- 변환이 민감도를 **없애는** 경우(익명화·집계)를 어떻게 구분하는가 — 언급 없음.
- 설명란의 *"실시간 추적"* — "real-time"은 발화에 없다(*"continuous"* 는 분류·발견 요구사항 ①에 붙은 말).
- 제품·도구 이름 없음.

## References

- [[tech-bridge-ai-data-exposure-hidden-risk]] (first-seen) · [[jeff-crume]] · [[ibm]]
- 관련: [[ai-data-exposure]] · [[retrieval-augmented-generation]] · [[agent-governance-layers]] · [[production-trace-eval-flywheel]]
