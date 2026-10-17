---
title: Gitar
type: entity
category: org
tags: [automated-code-review, ci, flaky-tests, autofix, auto-merge, agent-harness, sonar, vendor]
aliases: [Gitar, Gitar by Sonar, gitar.ai, guitar (ASR), 기타 (ko 오역)]
links:
  - "https://www.sonarsource.com/products/gitar/"
sources: [tech-bridge-gitar-agentic-pr-validation]
created: 2026-10-16
updated: 2026-10-16
---

# Gitar

PR 검증(코드 리뷰 + CI)을 에이전트로 자동화하는 제품이자 그 회사다. [[sonar|Sonar]]에 인수되었다. 공동 창업자 [[ali-reza|Ali-Reza]]가 [[tech-bridge-gitar-agentic-pr-validation]]에서 소개했고, 이 위키 첫 등장이다. 자기 규정: *"an agent that fully automates all the validation steps and as outcomes it delivers for you green PRs that are ready to merge or merge automatically."*(03:43~03:55) 이름은 en-orig ASR이 *"guitar"* 로 받는다. "Gitar"는 설명란과 링크로 판독한 것이다.

## 기능 (발화 기준)

| 기능 | en-orig |
|---|---|
| 리뷰 | *"it reviews your PR and posts issues and inline comments"*(03:57~04:01). 노이즈 최소화는 목표다(*"our goal has been to really make this experience as noisefree as possible"* 04:01~04:06) |
| 머지 차단 | *"block merging if there are any unresolved code review findings"*(04:25~04:31) |
| CI 실패 분석 · flaky | *"analyzes CI failures and posts a summary of the root causes"*(04:31~04:36), *"really good at catching flaky tests"*(04:36~04:40), flaky 자동 재시도 규칙은 *"a very popular feature"*(04:41~04:47) |
| 자동 수정 루프 | *"automatically loop until all the fish[=] issues have been fixed in your PR and you have a green PR ready to merge"*(05:04~05:11) |
| 자동 승인·머지 | *"you can define rules and conditions that control when uh PRs get automatically approved by the agent and merged automatically"*(05:18~05:31) |
| 인사이트 | 플랫폼 팀용 *"categorization of the top CI failures"*(06:55~06:58), 리더십용 PR 분류(07:24~07:44) |

## 내부 구조 (07:46~08:45)

- control plane: *"orchestration layer for handling PR workflows"*(07:57~07:59)
- 자체 agent harness: *"We built our own harness here that handles multi- aent[=multi-agent] execution, context management, memory management, um tool calling"*(08:03~08:10). 검증 용도 최적화(*"token cost, precision, and coverage"* 08:24~08:27)로 *"essentially guarantee outcomes at a fixed PR price"*(08:30~08:36)를 한다고 말한다. → [[agent-harness-design]]
- LLM proxy: *"handles the routing across different models as well as things like failover"*(08:37~08:45). → [[automatic-model-routing]]

## ⚠️ 유보

- 당사자 발표이고 **수치가 0개**다(오탐률, flaky 정확도, autofix 성공률, 자동 머지 비율, 회귀율, 고객 이름, 가격 모두 없음).
- 자동 승인 규칙의 예시·기본값, *"guarantee outcomes"* 의 outcome이 무엇인지는 발화되지 않는다.
- 링크는 열어 보지 않았다.

## References

- [[tech-bridge-gitar-agentic-pr-validation]] · [[ali-reza]] · [[sonar]] · [[automated-code-review]]
