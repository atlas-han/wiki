---
title: Claude Opus 4.5
type: entity
category: model
tags: [anthropic, claude, opus]
aliases: [Opus 4.5]
sources: [anthropic-harness-design-long-running-apps, anthropic-managed-agents]
links: []
created: 2026-05-25
updated: 2026-05-25
---

# Claude Opus 4.5

[[anthropic|Anthropic]] Claude 시리즈의 한 세대 전 플래그십. [[anthropic-harness-design-long-running-apps]] 초기 실험의 메인 coding 모델.

## 알려진 사실

- [[anthropic-harness-design-long-running-apps]] 첫 버전(레트로 게임 메이커)의 generator. Solo 20분 $9 vs full harness 6시간 $200 비교의 그 모델.
- [[claude-sonnet-4-5|Sonnet 4.5]]에서 두드러졌던 [[context-anxiety|context anxiety]]는 Opus 4.5 시점에서 *자체적으로* 사라짐 → [[context-resets-and-compaction|context resets]]을 harness에서 dropped 가능 ([[anthropic-managed-agents]] 인용).
- [[anthropic-harness-design-long-running-apps]] 시점에서는 sprint construct로 work decomposition을 받아야 일관성을 유지 → [[claude-opus-4-6]] 등장 후 제거.

## 위치

- 같은 세대 하위: [[claude-sonnet-4-5]]
- 후속: [[claude-opus-4-6]]

## References

- [[anthropic-harness-design-long-running-apps]]
- [[anthropic-managed-agents]]
