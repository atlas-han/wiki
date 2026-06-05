---
title: ultracode
type: concept
category: pattern
tags: [claude-code, setting, effort, dynamic-workflows]
related: [dynamic-workflows, agent-harness-design]
first-seen: anthropic-dynamic-workflows
sources: [anthropic-dynamic-workflows]
created: 2026-05-30
updated: 2026-05-30
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
