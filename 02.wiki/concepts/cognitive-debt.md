---
title: "인지 부채 (Cognitive Debt)와 AI 피로 (AI Fatigue)"
type: concept
category: theory
tags: [cognitive-load, code-review, human-in-the-loop, verification, spec-driven-development, agents]
aliases: [cognitive debt, 인지 부채, AI fatigue, AI 피로]
related: [verification-bottleneck, cognitive-offloading, read-fluency-for-agent-output, spec-driven-development, generator-evaluator-pattern, trusted-throughput, context-rot]
first-seen: tech-bridge-sdd-full-course
sources: [tech-bridge-sdd-full-course]
created: 2026-09-27
updated: 2026-09-27
---

# 인지 부채와 AI 피로

**에이전트가 코드를 사람이 따라갈 수 있는 속도보다 빨리 쓰면, "내 코드가 무엇을 하고 어떻게 변해 왔는가"를 추적하는 정신적 부담이 빚처럼 쌓인다(인지 부채). 그리고 그 양을 매번 검증하는 일이 사람을 소진시킨다(AI 피로).** [[tech-bridge-sdd-full-course]]가 두 이름을 붙여 스펙 주도 개발의 동기로 쓴다. 기술 부채가 **코드**에 쌓이는 빚이라면, 인지 부채는 **코드를 소유하는 사람의 이해**에 쌓이는 빚이다.

## 정의 (강좌 원문)

> *"Because agents are so fast at writing code, software developers have lately been talking about cognitive debt. The mental load of tracking what your code is doing and how it has evolved."* (26:26~26:37)

> *"AI fatigue. Agents can generate a lot of code with a lot of changes. This massive amount of code makes the human in the loop validation exhausting. So much to review."* (36:01~36:12)

강좌는 *"developers have lately been talking about"* 이라며 **자기 조어가 아니라 커뮤니티 용어**로 소개한다. 누가 처음 썼는지는 말하지 않는다.

## 처방 (강좌)

| 처방 | 발화 |
|---|---|
| **변경을 감당할 크기로** | *"to reduce cognitive debt, the changes should be manageable"*(26:42~26:48). 로드맵을 작은 단계로(17:50~17:53), 큰 기능은 계획의 일부만 먼저(38:38~38:47) |
| **작은 단계 + 잦은 커밋** | *"working in small steps with frequent commits keeps the review from overloading your brain"*(32:26~32:32) |
| **기능 경계를 깨끗하게** | 시작 전 점검 — 미완 작업, main 병합, 다음 로드맵 항목, **에이전트 컨텍스트 비우기**(36:14~36:41). *"This clean break between features helps manage AI fatigue."*(42:24~42:27) |
| **리뷰는 고수준으로** | 변수 이름 트집 금지, *"make sure it creates code that you can commit under your name"*(39:17~39:27) |
| **이해를 검증** | 앱이 동작하는지와 별개로 *"prevent cognitive debt by validating that we understand these changes"* — 테스트를 읽고 디버거로 밟는다(40:31~40:43) |
| **두 번째 눈은 에이전트에게** | 서브에이전트 deep review — 메인 컨텍스트를 오염시키지 않고 문제를 찾는다(40:54~41:41) |

특징: 처방의 대부분이 **리뷰 양을 줄이거나 쪼개는 것**이고, 이해 자체를 늘리는 처방은 **테스트를 디버거로 읽기** 하나다. 컨텍스트 과부하를 *"ours and agents"*(38:34) — **사람과 에이전트 양쪽의 문제**로 나란히 두는 것도 이 소스의 특징이다.

## 위키 내 자매 개념

- [[verification-bottleneck]] — 병목이 생성에서 검증으로 옮겨 갔다는 진단. 인지 부채는 그 병목을 **통과시킨 뒤에도 남는 비용**(이해하지 못한 채 병합된 코드)이다.
- [[cognitive-offloading]] — [[andrew-ng|Andrew Ng]] 편의 *LLM에 맡기면 점수는 오르고 장기 retention은 떨어진다.* 같은 현상을 **학습**에서 본 것.
- [[read-fluency-for-agent-output]] — 언어를 배우는 목표가 "쓸 수 있을 만큼"에서 "에이전트가 쓴 것을 읽고 이해할 수 있을 만큼"으로 옮겨 간다는 주장. 인지 부채를 **갚는 데 필요한 전제 역량**.
- [[trusted-throughput]] — PR 수가 아니라 신뢰할 수 있는 처리량. AI 피로는 신뢰 없이 처리량을 올렸을 때의 사람 쪽 비용.
- [[context-rot]] — 에이전트 쪽의 대응물. 이 강좌는 Agent Clinic의 "질병" 목록에 context rot을 넣는다(16:38~16:41).

> ⚠️ **측정 없음.** 두 용어 모두 강좌에서 정의와 처방만 나오고, 인지 부채를 재는 방법이나 AI 피로의 발생 조건에 대한 데이터는 없다. 이 위키의 단일 소스 개념이다.

## References

- [[tech-bridge-sdd-full-course]] · [[spec-driven-development]] · [[verification-bottleneck]]
