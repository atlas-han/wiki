---
title: "플레이키 테스트 (Flaky Tests) — 다시 돌리면 통과하는 실패"
type: concept
category: pattern
tags: [ci, testing, flaky-tests, long-running-agents, codex, verification]
aliases: [flaky test, flaky tests, 플레이키 테스트, 불안정한 테스트, 하이젠버그]
related: [goal-level-delegation, verification-bottleneck, scheduled-agent-automations, generator-evaluator-pattern, subagent-vs-thread-handoff, trusted-throughput]
first-seen: tech-bridge-codex-agents-that-dont-quit
sources: [tech-bridge-codex-agents-that-dont-quit]
created: 2026-11-15
updated: 2026-11-15
---

# 플레이키 테스트 (Flaky Tests)

**한 번 실패했다가 다시 돌리면 통과하는 테스트.** CI가 초록불이어야 모두가 배포할 수 있으므로, 진짜 고장인지 우연인지 누군가 들여다봐야 하고, 까다로운 건 몇 시간에서 며칠이 걸리며, 그 사이 다음 실패가 또 들어온다 — *"끝이 없는 일이죠."*(02:17) ([[tech-bridge-codex-agents-that-dont-quit]], 해설). 이 위키에서는 **장기 실행 에이전트에게 맡기기 좋은 일의 대표 사례** 로 처음 페이지가 되었다.

## 왜 에이전트에게 맞는가 (2026-11-15 · [[tech-bridge-codex-agents-that-dont-quit]])

[[aaron-friel|Aaron Friel]](OpenAI, 철자 추정)은 자기 팀의 이 일을 [[codex|Codex]] 에이전트 하나에게 6주 동안 맡겼다(해설 전달).

- **끝이 없고 반복적이다** — 시작하는 법 1번 *"내 시간을 잡아먹는 반복 업무 하나"* 의 전형.
- **스스로 확인할 수단이 이미 있다** — 테스트 자체가 판정기다. *"돌려볼 테스트가 있어야 루프가 돕니다."* → [[verifiable-goals]]
- **대기가 많다** — 도구 호출 49만 9천여 번 중 6만 7천여 번이 *그냥 기다리는* 호출이었다. 사람은 그 사이 커피를 가지러 가지만 에이전트는 결과가 오면 바로 다음 단계로 → [[scheduled-agent-automations]](heartbeat)
- **사람이 피하던 꼬리** — 머지 213건은 *"고치느니 건너뛰거나 재시도하고 말던"* 가장 어려운 버그들이었다.

## 운영 규칙과 함정

- 예산 규칙: CI에는 **한 시간에 한 번** 넘게 올리지 않는다 · CI 작업을 동시에 몇 개까지 돌릴지 정한다 · 근무 시간 외 메시지는 모아 둔다.
- **가장 쉬운 해결은 테스트를 지우는 것** — 해설: *가끔은 그게 먹히기도 하죠.* 에이전트는 확신이 없을 때 다른 에이전트를 하나 더 만들어 자기 수정을 따져 묻게 했다(사람 리뷰 요청 전) → [[generator-evaluator-pattern]]
- 하이젠버그: GPU 부동소수점이 아주 가끔 다른 값을 내는 문제 — 몇 주 치 로그로 **특정 노드 한 대** 를 찾고, 그 노드에서 반복 실행으로 (매번은 아니게) 재현, 마지막엔 시스템 담당 연구자에게 *선언되지 않은 소프트웨어 최적화인지 하드웨어 결함인지* 물었다.

## 다른 소스와의 연결

- [[tech-bridge-trusted-throughput]](09-02, Ironclad)은 병목을 리뷰 · CI로 특정하며 *flaky 테스트 → 수동 재실행 또는 AI 반복 재시도 → 토큰 낭비의 원인이 CI 품질* 이라는 인과를 냈다(위키 log 기록) — 이 소스의 *재시도하고 말던 버그* 와 같은 비용 구조다. → [[trusted-throughput]]
- [[gitar|Gitar]]는 PR 검증 자동화의 범위에 flaky를 넣는다([[tech-bridge-gitar-agentic-pr-validation]]).
- → [[verification-bottleneck]]

## References

- [[tech-bridge-codex-agents-that-dont-quit]]
- [[tech-bridge-trusted-throughput]]
- [[tech-bridge-gitar-agentic-pr-validation]]
