---
title: Minions (Stripe)
type: entity
category: product
tags: [coding-agent, internal-tool, stripe, goose, devbox, blueprint, deterministic-pipeline]
aliases: [Minions, 미니언즈, Stripe Minions]
links:
  - https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents
  - https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents-part-2
sources: [tech-bridge-stripe-collison-cherny-ai-dev-workflow]
created: 2026-10-23
updated: 2026-10-23
---

# Minions (Stripe)

[[stripe|Stripe]]의 **사내 코딩 에이전트**. [[block|Block]]의 [[goose|goose]]를 바탕으로 만들었다(설명란 · 해설 01:40~01:44). 블로그 제목은 *"Minions: Stripe's one-shot, end-to-end coding agents"*(설명란 링크 slug 기준). 첫 소스 [[tech-bridge-stripe-collison-cherny-ai-dev-workflow]].

## 위키에서 알려진 사실 (모두 해설이 Stripe 공식 기술 블로그를 인용한 것)

- **실행 환경 = devbox**: *"코드와 개발 중인 서비스를 담은 클라우드 개발 환경"* — 사람이 쓰던 개발 기반을 에이전트에 그대로 쓴다(01:20~01:33). → [[agent-sandboxing]] · [[cloud-agent-delegation]]
- **blueprint**: 흐름에 *"모델이 판단하는 단계와 정해진 코드가 실행하는 단계를 함께 둡니다. 구현에는 에이전트를 쓰고 정해둔 검사에는 일반 코드를 쓰는 방식"*(03:53~04:06). → [[deterministic-agent-pipeline]]
- **Claude Code와 다른 시스템**: *"미니언즈의 처리 순서를 클로드 코드의 내부 구조로 받아들이시면 안 됩니다"*(01:46~01:48, 설명란도 같은 고지). → [[claude-code]]

> ⚠️ 이 위키는 Stripe 블로그를 열어 보지 않았다. *one-shot, end-to-end* 는 URL slug에서 읽은 것이고, blueprint의 구체 구성·규모·성과 수치는 자막에 없다.

## References

- [[tech-bridge-stripe-collison-cherny-ai-dev-workflow]] · [[stripe]] · [[goose]] · [[block]]
