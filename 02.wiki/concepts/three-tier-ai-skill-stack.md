---
title: AI 엔지니어의 세 층 — 기초 · AI 특화 · 배포 (Three-Tier AI Skill Stack)
type: concept
category: pattern
tags: [ai-engineer, career, learning-path, rag, agents, deployment, kubernetes, observability]
aliases: [3단계 기술 스택, 순서가 중요하다, 기초를 건너뛰지 말라]
related: [ai-engineer-vs-ml-researcher, read-fluency-for-agent-output, workflow-vs-agent, retrieval-augmented-generation, agent-action-record, agent-harness-design, build-time-vs-runtime-tools]
first-seen: tech-bridge-ai-engineer-three-tier-skill-stack
sources: [tech-bridge-ai-engineer-three-tier-skill-stack]
created: 2026-09-16
updated: 2026-09-16
---

# AI 엔지니어의 세 층

**배울 것은 세 층 — (1) AI에 국한되지 않는 기초, (2) AI 특화 기술, (3) 출시·배포·운영 — 이고 순서가 중요하다. 기초를 건너뛰고 에이전트부터 만들면 기본기를 다시 배우는 데 시간을 쓴다.** [[cedric-clyburn|Cedric Clyburn]]([[ibm|IBM Technology]])이 [[tech-bridge-ai-engineer-three-tier-skill-stack]]에서 제시.

## 세 층

| 층 | 내용 | 소스의 정당화 |
|---|---|---|
| **1. 기초** | **Python**(에이전트가 쓴 것을 읽을 만큼) · **Git** · **CLI** · **Linux**(*"AI 도구 상당수가 내부적으로 Linux"*) · **API**(호출·응답 처리·속도 제한) | *"AI에만 국한된 것은 아니지만 이것 없이는 절대 만들 수 없다"* |
| **2. AI 특화** | **임베딩·벡터 검색**(의미 vs 키워드) → **RAG 파이프라인**(청킹 → 임베딩 → 저장 → 검색 → 컨텍스트 창) → **에이전트와 도구 사용**(동적 결정 루프) | *"거의 모든 회사가 RAG를 원한다"* · *"에이전트는 현재 가장 수요가 많은 응용 AI 기술"* |
| **3. 출시·배포** | **컨테이너화·Kubernetes**(에이전트, 때로 모델까지) → **관측 가능성**(*"왜 그 결정을 내렸는지"*) → **모니터링**(토큰 비용·보안) | *"노트북에서 나와 실제 사용자의 손에"* |

## 순서

> **이 순서는 정말 중요합니다.** 사람들이 종종 하는 일은 **기초를 건너뛰고 데이터를 다루거나 인프라의 복잡성을 이해하기도 전에 바로 에이전트 구축이나 배포로 넘어가는 것**입니다. 그래서 **기본기를 다시 익히는 데 많은 시간을 보냅니다.** (02:37~03:01)

층의 논리는 **의존**이다 — 2층의 RAG는 1층의 API·데이터 다루기 위에, 3층의 배포는 1층의 Linux·CLI 위에 선다. 그래서 건너뛴 층은 **없어지지 않고 나중에 청구된다.**

## 층별로 위키가 이미 가진 것

- **1층** — [[read-fluency-for-agent-output]](Python의 기준), [[agent-distributed-systems]](*"전부 API 호출"*).
- **2층** — [[retrieval-augmented-generation]](이 소스가 파이프라인 서술을 처음 준다), [[workflow-vs-agent]](에이전트의 정의), [[agent-harness-design]](*루프를 안정적으로 만드는 일*).
- **3층** — [[agent-action-record]]·[[behavior-validated-trust]](관측 가능성과 신뢰), [[build-time-vs-runtime-tools]](배포 후의 도구 노출).

이 위키의 대부분 소스가 **2층의 위쪽 절반**(에이전트·하네스·스킬)에 몰려 있다는 것이 이 표에서 보인다. 1층과 3층은 이 소스가 처음으로 **한 프레임 안에** 넣었다.

## 화자가 보는 프로덕션의 세 사례

RAG 지식 시스템(HR·병원·챗봇) · 도구를 쓰는 에이전트(DB 조회·시각화) · 배포 지원(*"몇 주가 아니라 몇 시간"*). ⚠️ *"제가 현재 보는"* — 관찰이고 수치 없음.

## ⚠️ 유보

- **평가(eval)·파인튜닝·프롬프트 설계가 세 층 어디에도 없다.** 이 위키가 [[skill-evals]]·[[agent-verification-skill]]로 쌓은 검증 층이 이 스택에는 빠져 있다.
- **재랭킹·청크 크기 결정** — RAG 서술이 저장·검색까지다.
- **채택률 주장 전부 근거 없음.**
- **Kubernetes·하이브리드 클라우드가 3층의 핵심**인 것은 화자 소속 벤더들이 파는 것과 같은 자리다. 소스는 그 연결을 하지 않는다.
- 약속된 *"세 가지 프로젝트"* 가 소스에 없다.

## References

- [[tech-bridge-ai-engineer-three-tier-skill-stack]] — first-seen
- [[cedric-clyburn]] · [[ibm]]
- 관련: [[ai-engineer-vs-ml-researcher]] · [[read-fluency-for-agent-output]] · [[workflow-vs-agent]] · [[retrieval-augmented-generation]] · [[agent-action-record]]
