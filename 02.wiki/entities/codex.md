---
title: Codex
type: entity
category: product
tags: [openai, coding-agent, gpt, fast-mode]
links:
  - https://openai.com/index/nextdoor/
created: 2026-06-27
updated: 2026-06-27
---

# Codex

[[openai|OpenAI]]의 coding agent. [[openai-nextdoor-codex|Nextdoor 케이스 스터디]] 기준 GPT‑5.4/5.5를 기반으로 동작하며, 재현 어려운 버그 조사부터 멀티플랫폼 기능 구축까지 폭넓게 쓰인다. [[claude-code|Claude Code]]에 대응하는 OpenAI 측 에이전트.

## 소스에 나타난 특징 (Nextdoor 사례)

- **재현 어려운 문제 디버깅**: embedded Rust DB, tight race condition, Kubernetes pod 기동 실패 등에서 root cause까지 *persistent*하게 파고듦. 사용자가 *"clean environment and harness for investigation"* 를 제공하는 워크플로.
- **Fast Mode** (Codex + GPT‑5.5): 빠른 피드백 루프 — Nextdoor 팀이 "addicted"라 표현. (참고: [[claude-code]]에도 fast mode 개념 존재.)
- **Outcome 중심 사용**: 스크린샷·영상·성능·테스트 결과를 목표로 빌드 → [[outcome-engineering]] 프레이밍의 도구적 토대.

> ⚠️ 2026 제품·모델이라 스펙은 소스 명시 범위로 한정. 벤치마크 수치는 출처(마케팅)에 없음.

## References

- [[openai-nextdoor-codex]] · [[openai]]
- 외부: <https://openai.com/index/nextdoor/>
