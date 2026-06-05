---
title: Claude Sonnet 4.6
type: entity
category: model
tags: [anthropic, claude, sonnet, classifier]
aliases: [Sonnet 4.6]
sources: [anthropic-claude-code-auto-mode]
links: []
created: 2026-05-25
updated: 2026-05-25
---

# Claude Sonnet 4.6

[[anthropic|Anthropic]] Claude 시리즈의 mid-tier 모델. 본 위키에서는 [[claude-code|Claude Code]] **auto mode**의 [[transcript-classifier|transcript classifier]] 백본 모델로 등장.

## 알려진 사실

- [[anthropic-claude-code-auto-mode]]에서 *2-stage transcript classifier*를 구동하는 모델
- Stage 1: fast single-token yes/no, **err on blocking**. Stage 2: 동일 prompt + CoT reasoning
- Stage 2가 거의 전부 prompt cache hit이라 비용 효율적
- 평가 결과 (auto mode 풀 파이프라인): real traffic FPR 0.4%, real overeager FNR 17%, synthetic exfil FNR 5.7%

## 위치

- 직전: [[claude-sonnet-4-5]]
- 같은 세대 상위: [[claude-opus-4-6]]

## References

- [[anthropic-claude-code-auto-mode]]
