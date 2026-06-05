---
title: Claude Sonnet 4.5
type: entity
category: model
tags: [anthropic, claude, sonnet]
aliases: [Sonnet 4.5]
sources: [anthropic-harness-design-long-running-apps, anthropic-managed-agents]
links: []
created: 2026-05-25
updated: 2026-05-25
---

# Claude Sonnet 4.5

[[anthropic|Anthropic]] Claude 시리즈의 한 세대 전 mid-tier 모델. 본 위키에서는 **에이전트 harness의 가정**이 모델 capability에 어떻게 묶이는지를 보여주는 비교 baseline으로 등장.

## 알려진 사실

- **Context anxiety**가 두드러진 모델 ([[context-anxiety]]): context limit이 가까워졌다고 *느끼면* 작업을 조기 마무리. [[anthropic-managed-agents]]·[[anthropic-harness-design-long-running-apps]] 두 글에서 모두 명시.
- 이 때문에 **compaction만으로는 부족**, [[context-resets-and-compaction|context reset]]이 harness의 essential 컴포넌트였음.
- [[anthropic-harness-design-long-running-apps]]에서는 [[claude-opus-4-5]] 기준 sprint construct로 work decomposition을 강제 → [[claude-opus-4-6]]에서 제거.

## 위치

- 같은 세대 상위: [[claude-opus-4-5]]
- 후속: [[claude-sonnet-4-6]]

## References

- [[anthropic-harness-design-long-running-apps]]
- [[anthropic-managed-agents]]
