---
title: Annie Wang
type: entity
category: person
tags: [google, agent-harness, adk, mcp, sandbox, evaluation, educator]
aliases: [애니 왕, 애니왕]
links: []
sources: [tech-bridge-annie-wang-harness-four-designs]
created: 2026-10-26
updated: 2026-10-26
---

# Annie Wang

[[tech-bridge-annie-wang-harness-four-designs]]의 발췌 화자. 설명란은 *"구글 엔지니어 Annie Wang"* 이라고만 적었다(소속 부서 · 원본 영상 미상). 고객 명단 CSV 내려받기 예제 하나로 하네스의 네 층 — **기억 · 도구와 순서 · 실행 환경과 권한 · 완료 기준** — 을 설명한다.

## 위키에서 알려진 사실 (전부 그 영상의 발췌)

- 하네스: *"It provides [connections?], connect tools and enforce permissions and also manage all the back-and-forth communication."*(00:25~00:33) → [[agent-harness-design]]
- **session · state**: 세션은 대화 transcript 전체, 상태는 *"more like a scratch pad for your application"*(00:57~01:25). → [[agent-memory]]
- 도구와 MCP, 병렬 검사(unit test + browser test) · retry limit을 가진 graph workflow(⚠️ ADK로 판독 추정). → [[model-context-protocol]] · [[deterministic-agent-pipeline]]
- *"Those controls need to be enforced by software. Simply telling the model to be careful isn't enough."*(04:33~04:37) → [[hard-vs-soft-enforcement]] · [[prompt-injection]]
- *"Even if a tool runs on your laptop, it's output may be sent to a [hosted] model."*(05:02~05:07) → [[agent-sandboxing]]
- 결정적 평가 → judge → 사람 평가: *"The judge can make mistakes."*(06:29~06:31) → [[generator-evaluator-pattern]]

## ⚠️ 유보

- 발췌에서 이름을 말하지 않는다 — 귀속은 설명란 근거. 원본 영상의 제목 · 날짜 · 링크 없음.

## References

- [[tech-bridge-annie-wang-harness-four-designs]] · [[tech-bridge]]
