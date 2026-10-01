---
title: Dreaming — 아웃오브밴드 메모리 정리 (Agent Dreaming)
type: concept
category: pattern
tags: [agent-memory, dreaming, out-of-band, batch, continual-learning, transcripts, human-in-the-loop, anthropic, managed-agents]
aliases: [dreaming, 드리밍, 꿈꾸기, 회고, dreamer, 드리머, out-of-band memory curation, 아웃오브밴드 메모리, memory dreaming]
related: [agent-memory, nightly-memory-consolidation, token-roles, strategy-primitives, managed-agents, production-memory-guardrails, self-harness, skill-self-improvement, continual-learning, context-engineering, generator-evaluator-pattern]
first-seen: tech-bridge-claude-platform-agent-era
sources: [tech-bridge-anthropic-dreaming-memory, tech-bridge-claude-platform-agent-era, tech-bridge-tokens-should-have-jobs]
created: 2026-10-01
updated: 2026-10-01
---

# Dreaming — 아웃오브밴드 메모리 정리

**작업하는 에이전트의 세션 밖에서, 별도 자원으로, 일정 기간의 세션 트랜스크립트와 기존 메모리 스토어를 함께 훑어 메모리 변경을 제안하는 배치·비동기 과정.** [[anthropic|Anthropic]]의 용어. 이름은 09-01([[tech-bridge-claude-platform-agent-era]])부터 이 위키에 있었지만 **구조는 [[tech-bridge-anthropic-dreaming-memory]](10-01, [[lamis-mukta|Lamis Mukta]])에서 처음 나왔다.**

> *"we introduced this concept of dreaming which is like a second o second order process over memory"* (17:49~17:54) · *"dreaming which is a process that runs in batch and asynchronously with its own allocated resources to ensure that those memories themselves are effective up to date"* (18:10~18:20)

## 왜 세션 밖인가 — 인밴드 메모리의 한계

세션 안에서 에이전트가 직접 읽고 쓰는 메모리(**인밴드**, memory tool·CLAUDE.md 쓰기)에는 구조적 한계가 있다고 한다(15:04~17:45):

| 한계 | en-orig |
|---|---|
| **자원·주의의 분할** — 과제 수행과 미래의 자신을 위한 메모리 큐레이션이 한 예산을 나눈다 | *"how much capacity should an agent put into like helping future versions of itself versus doing the task that you actually asked it to do?"* (15:58~16:03) |
| **가시성** — 세션을 넘는 패턴, 다른 에이전트의 실패를 못 본다 | *"they just won't see patterns that happen across sessions"* (16:21~16:22) |
| **낡은 기억** — 써 둔 것이 아직 맞는지 점검하는 패스가 없다 | *"you need something some pass that checks that everything that's written there is still correct"* (17:40~17:45) |

비유는 학교 — 학생(작업 에이전트), 채점 교사, 전체를 보는 교장. *dedicated capacity* 와 *visibility over the whole fleet* 가 따로 있어야 한다(16:57~17:34).

## 동작

| 칸 | 내용 | en-orig |
|---|---|---|
| 입력 | 기존 **메모리 스토어**(디렉터리의 마크다운 파일) + 일정 기간의 **세션 트랜스크립트**(대화뿐 아니라 도구 호출·스킬 등 메타데이터) | 18:32~18:46, 21:30~21:54 |
| 분석 | **오케스트레이터가 서브에이전트 함대**를 띄워 트랜스크립트를 나눠 분석 | 21:56~22:02 |
| 선별 | 오케스트레이터가 *"prevalent enough patterns"* 만 변경 대상으로 | 22:35~22:46 |
| 출력 | *"a new memory store where there are proposed changes to the existing memory store"* + **근거 트랜스크립트 예시와 빈도 통계** | 19:02~19:07, 22:57~23:05 |
| 게이트 | 사람이 변경별로 수락/거부 | 23:13~23:21 |
| 조정 | 조직에 맞춰 무엇이 중요/무관한지 **steer** | 22:06~22:32 |
| 권한 | 첨부할 트랜스크립트를 골라 권한 집합을 맞춘다 | 29:20~29:48 |

찾는 것(19:32~21:16): **빠진 지식**(지리 주제가 커리큘럼에 없다), **도구 설정 오류**(모든 답이 라디안 — 계산기 설정 = 반복 실패하는 도구 호출), **조직 전역의 습관**(em dash 남용 → 전역 공지).

## 메모리(인밴드)와 dreaming — 병렬의 두 과정 (23:28~24:46)

| | 인밴드 메모리 | dreaming |
|---|---|---|
| 언제 | 세션 안 | 배치·비동기, *"next day"* 에 반영 |
| 장점 | *"shorter time to kind of seeing that change"* (23:54~23:55) | *"broader visibility and dedicated capacity i.e. token spend"* (24:12~24:21) |
| 약점 | 자원 경쟁, 가시성 부족 | 비용 — 화자는 원샷이 늘어 비용이 내려간다고 답한다(24:25~24:46, ⚠️ 수치 없음) |

## 이 위키에서의 좌표

| 소스 | dreaming을 무엇으로 말하나 |
|---|---|
| [[tech-bridge-claude-platform-agent-era]] (09-01) | 토큰의 세 번째 역할 — 과거 세션을 돌아보며 **메모리에 쓰고 스킬을 작성** → [[token-roles]] |
| [[tech-bridge-tokens-should-have-jobs]] (09-18) | 실행자 → 조언 → 채점 → **회고**의 마지막 칸, 드리머가 기록을 검토해 **메모리에 저장**, Managed Agents 기본 제공 → [[strategy-primitives]] |
| **[[tech-bridge-anthropic-dreaming-memory]] (10-01)** | **인밴드 메모리의 한계에 대한 답** — 입력·구조·출력·사람 게이트 |
| (비 Anthropic) [[nightly-memory-consolidation]] (Muse, 09-17) | 하루 끝 일괄 압축, **모델이 스스로 정한다**, 사용자 가시성 서술 없음 |

> ⚠️ **Contradiction: 직접 쓰기 vs 제안.** 09-18의 드리머는 *"발견한 내용을 메모리에 저장"* 하고 *채점을 통과한* 자료를 받는다. 10-01의 dreaming은 **실패 패턴**(*"where agents are consistently failing"* 19:17~19:22)을 찾고 **변경을 제안**해 사람이 수락한다. 같은 제품의 다른 모드인지, 다른 층(전략 루프 vs 메모리 API)인지 **미확정.**

- [[self-harness]] — 논문의 루프(트레이스 → 약점 → bounded edit → 회귀 검증)와 칸이 같다. 차이: 개선 대상이 **메모리**, 채택 게이트가 **회귀 테스트가 아니라 사람의 수락**.
- [[skill-self-improvement]] — task-observer가 교훈을 *사람 검토 후* 승격하는 것과 같은 형태가 **메모리 층**에서 반복된다.
- [[production-memory-guardrails]] — dreaming이 쓰는 제안도 버전 관리·권한 위에서 돈다(위키의 연결 — 화자가 둘을 명시적으로 묶지는 않는다).

## ⚠️ 미해결

- **효과 측정 없음** — 수락한 변경이 실제로 다음 날 성능을 올렸는지 재는 고리가 없다. [[production-trace-eval-flywheel]]의 eval 단계에 해당하는 것이 비어 있다.
- **주기** — *"next day"* 만. "자는 동안·밤새"는 제목·설명란의 말이다.
- **스킬도 출력인가** — 09-01은 스킬을 말했고 10-01은 메모리 스토어만 말한다.
- **자동 적용 모드** — *"in our case, the way that we've designed this in production"*(22:54~22:56)이라 했을 뿐.
- **인젝션** — 트랜스크립트 자체가 오염됐을 때(사용자 입력·도구 출력에 심긴 지시) 제안이 어떻게 걸러지는지 말하지 않는다. → [[prompt-injection]]

## References

- [[tech-bridge-anthropic-dreaming-memory]] (구조의 1차 출처) · [[lamis-mukta]]
- [[tech-bridge-claude-platform-agent-era]] (first-seen, 이름) · [[tech-bridge-tokens-should-have-jobs]]
- 관련: [[agent-memory]] · [[nightly-memory-consolidation]] · [[token-roles]] · [[strategy-primitives]] · [[managed-agents]] · [[production-memory-guardrails]] · [[self-harness]] · [[skill-self-improvement]] · [[continual-learning]]
