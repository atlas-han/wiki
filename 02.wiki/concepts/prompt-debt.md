---
title: "프롬프트 부채 (Prompt Debt) — 옛 모델용 주문이 새 모델의 비용과 성능을 깎는다"
type: concept
category: pattern
tags: [prompt-engineering, prompt-debt, prompt-audit, model-upgrade, cost, claude-code, claude-md, anthropic, harness-pruning]
aliases: [prompt debt, 프롬프트 부채, 프롬프트 빚, prompt audit, prompt-audit, /claude-api prompt-audit, 옛날 프롬프트, legacy prompt instructions]
related: [harness-pruning, prompt-caching, skill-evals, climbable-eval, model-mixing-economics, tools-and-context-over-harness, agent-harness-design]
first-seen: tech-bridge-lance-martin-old-prompts-make-claude-worse
sources: [tech-bridge-lance-martin-old-prompts-make-claude-worse]
created: 2026-11-09
updated: 2026-11-09
---

# 프롬프트 부채 (Prompt Debt)

**옛 모델의 약점을 메우려고 넣은 프롬프트 문장이 모델이 바뀐 뒤에도 남아, 새 모델의 비용을 올리고 성능을 깎는 현상.** [[tech-bridge-lance-martin-old-prompts-make-claude-worse]]에서 해설자가 [[lance-martin|Lance Martin]]([[anthropic|Anthropic]])의 말로 전한다:

> *"렌스마틴은 프롬프트에도 코드처럼 빚이 쌓인다고 말합니다."*(00:59~01:01)

> ⚠️ **소스 하나, 벤더 자기 실험의 2차 전달.** 이름 *prompt debt*는 위키가 붙인 것이다(해설은 *프롬프트에도 빚이 쌓인다*). 수치는 Anthropic이 자사 명령으로 잰 것을 해설자가 옮겼고, 원 발표 · 블로그는 열지 않았다.

## 빚의 종류 (해설이 든 예)

| 유형 | 예 | 해설이 전한 결과 |
|---|---|---|
| 과잉 지시 | *단계별로 생각해라 · 두 번 확인해라 · 최대한 꼼꼼하게* | 문자 그대로 따르느라 토큰을 더 씀. *두 번 검증* 한 줄 → 티켓당 비용 +48%, 정확도 그대로. 같은 주문 조회를 환불마다 두 번 |
| 모순된 규칙 | 몇 달 간격으로 붙은 *정책에 맞으면 환불* + *에스컬레이션 없이 환불 금지* | 새 모델이 환불 4건을 붙잡고 확인만 요청. 정확도 약 9점 하락 |
| 낡은 설정 | 옛날 생각(thinking) 설정 | API가 요청을 전부 거절 |
| 손수 만든 스캐폴드 | 직접 짠 스크래치패드 | 내장 생각과 충돌 → 티켓 3건에서 도구 호출을 생각 속에만 쓰고 실행 안 함 |

공통 원인: *"지금 모델은 언제 생각할지 스스로 고르고 알아서 검증합니다."*(01:08~01:10)

## 갚는 방법 — audit

- [[claude-code|Claude Code]]의 `/claude-api prompt-audit`(설명란 표기)가 스킬 · CLAUDE.md · 프롬프트 · 도구 설명을 훑어 이런 패턴을 지운다.
- 해설 수치: Opus 4.8 → 5.5 교체만으로 비용 약 18% ↓, auditor 한 번에 9% 더 ↓, 정확도 약 2%p ↑. 한 개발자는 자기 Claude Code 설정에서 약 70곳을 찾았다.
- ⚠️ 지운 뒤 나빠지지 않았는지는 **평가로** 본다 — 같은 영상이 [[climbable-eval]](학습/시험 분할)을 바로 뒤에 놓는다.

## 위키 안의 연결

- [[harness-pruning]] — *하네스의 가정은 낡는다*를 하네스 · 서브에이전트 단위로 다룬 페이지. 프롬프트 부채는 **같은 논리의 문장 단위 판**이고, 지울 곳을 찾는 도구(audit)까지 갖춘 첫 소스다.
- [[prompt-caching]] — 시스템 프롬프트의 타임스탬프 하나도 일종의 부채다(캐시를 깬다). 같은 영상 3절.
- [[skill-evals]] — 스킬 문서도 audit 대상에 들어간다.

## 미해결

- audit가 *무엇을* 패턴으로 보는지(규칙 목록인지 모델 판단인지), 오탐으로 필요한 지시까지 지울 위험.
- 48% · 9점 · 18% + 9%의 표본 크기와 과제. 고객센터 시뮬레이션 하나로 보인다.

## References

- [[tech-bridge-lance-martin-old-prompts-make-claude-worse]] (1절 · 2절) — first-seen
- [[lance-martin]] · [[anthropic]] · [[claude-code]]
- 관련: [[harness-pruning]] · [[prompt-caching]] · [[climbable-eval]] · [[skill-evals]]
