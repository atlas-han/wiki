---
title: ultracode
type: concept
category: pattern
tags: [claude-code, setting, effort, dynamic-workflows]
related: [dynamic-workflows, agent-harness-design, reasoning-effort-levels]
first-seen: anthropic-dynamic-workflows
sources: [anthropic-dynamic-workflows, tech-bridge-chase-ai-fable-5-2-prompting-rules]
created: 2026-05-30
updated: 2026-11-12
---

# ultracode

[[claude-code|Claude Code]]의 effort menu에 추가된 세팅. 켜면 effort level을 **xhigh**로 설정하고, 동시에 **Claude가 [[dynamic-workflows|dynamic workflow]]를 언제 쓸지 자동으로 판단**하게 한다. 즉 "최대 노력 + workflow 자동 트리거"를 한 토글로 묶은 진입점.

## 핵심

- effort = **xhigh** (Claude Code-specific effort 레벨)
- workflow 사용 여부를 사용자가 매번 지시하지 않고 **모델이 task에 따라 결정**
- dynamic workflow 진입의 두 경로 중 하나 — 다른 하나는 "Create a workflow" 식 직접 요청
- [[anthropic-claude-code-auto-mode|auto mode]]를 켠 상태에서 쓰는 것을 권장

> Switch on a new Claude Code-specific setting called `ultracode` ... it sets the effort level to xhigh, while letting Claude decide automatically when to use a workflow to handle your task.

## 맥락

이름이 "ultra-" 계열(예: `ultrathink`)의 effort 상향 관용구를 잇는다. dynamic workflows가 토큰을 많이 쓰므로, `ultracode`는 scoped task에서 먼저 감을 잡고 켜는 것이 권장된다. 상세 동작은 [[dynamic-workflows]] 참조.

## References

- [[anthropic-dynamic-workflows]]
- [Claude Code settings](https://code.claude.com/docs/en/settings)

## 모델이 스스로 띄우는 *작은 Ultra Code* (2026-11-12 · [[tech-bridge-chase-ai-fable-5-2-prompting-rules]])

[[chase-ai|Chase AI]]: [[fable-5-2|Fable 5.2]]는 extra high · max 강도에서 자기 작업을 검사하는 서브에이전트를 스스로 띄운다 — *"Almost like a miniature version of Ultra Code."*(08:16~08:19) 그래서 *서브에이전트를 써서 늘 검사하라* 같은 규칙은 지우라고 한다(그대로 따르느라 사용량을 태운다). → [[reasoning-effort-levels]] · [[prompt-debt]]

- 위키의 읽기: 오케스트레이션을 **하네스 · 사용자가 짜는 것**(이 페이지)과 **모델이 강도에 따라 알아서 하는 것** 이 겹치기 시작한다. 둘을 함께 켜면 이중 검사가 된다(화자의 경고를 위키가 일반화).
