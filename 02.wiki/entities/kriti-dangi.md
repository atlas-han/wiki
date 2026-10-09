---
title: Kriti Dangi
type: entity
category: person
tags: [uber, debugging-agent, observability, platform-engineering]
aliases: [Kriti]
links: []
sources: [tech-bridge-uber-debug-assist]
created: 2026-10-09
updated: 2026-10-09
---

# Kriti Dangi

[[uber|Uber]] 엔지니어. [[tech-bridge-uber-debug-assist]]에서 사내 디버깅 에이전트 [[debug-assist|Debug Assist]]의 구조와 운영 지표를 발표했다. 본 위키 첫 등장.

> ⚠️ **이름·직함은 발화에 없다.** 발표는 자기소개 없이 *"So, this talk is about debug assist and (…) AI agent for debugging that we built at Uber."*(00:00~00:04)로 시작한다. 이름은 영상 제목·설명란에만, 직함 *시니어 소프트웨어 엔지니어* 는 설명란에만 있다. 발화된 자기 정보는 Q&A의 *"even though I work in observability space"*(25:16~25:20) 하나 — 소속 팀이 관측(observability) 쪽이라는 진술.

## 발표에서 (자막 근거)

- 계획을 모델에 맡기지 않는다 — LangGraph 골격에 결정론 노드와 LLM 노드, *"We control the plan."*(09:28~09:29) → [[deterministic-agent-pipeline]]
- 턴 예산을 표류 감지기로 — *"if it's taking more than 20 turns, it's generally going in the wrong direction"*(12:29~12:34)
- 골격은 고정, 스킬·플러그인은 런타임에 — *"we are not the owners of domain, we are the providers of the harness"*(27:46~27:50) → [[harness-as-platform]]
- 지표: 월 약 9,000 RCA, 정확도 50%, PR 머지율 5% → 약 48%(19:09~20:18) ⚠️ 자기 보고

## 태도

1인칭 운영자 보고 — 실패한 경로·비용 수치는 말하지 않는다. 트레이싱 도구로 Arize를 언급하지만 홍보 문맥은 아니다(25:23~25:28). 사람 손 디버깅도 *"I would also encourage you to do so"*(18:38~18:39)라고 권한다.

## References

- [[tech-bridge-uber-debug-assist]] — first-seen
- [[uber]] · [[debug-assist]]
