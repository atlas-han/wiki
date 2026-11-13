---
title: Claude Haiku 5.5
type: entity
category: model
tags: [anthropic, claude, haiku, llm, pricing, subagent]
aliases: [Haiku 5.5, 하이쿠 5.5, claude-haiku-5-5]
links:
  - https://platform.claude.com/docs/en/about-claude/models/choosing-a-model
sources: [tech-bridge-addy-osmani-which-claude-model]
created: 2026-11-13
updated: 2026-11-13
---

# Claude Haiku 5.5

[[anthropic|Anthropic]]의 가장 작고 빠른 Claude 모델. [[addy-osmani|Addy Osmani]]의 모델 선택 가이드를 해설한 [[tech-bridge-addy-osmani-which-claude-model]]에서 처음 위키에 들어왔다. 이전 판으로 *Haiku 4.5* 가 언급된다(budget tokens → effort 전환).

> ⚠️ **해설 전달의 수치다.** 위키는 원 블로그 · 공식 문서를 열지 않았다. 발표일은 미상.

## 위키에서 알려진 것 (해설 기준)

- 가격: 입력 $0.10 · 출력 $0.50 / 100만 토큰. 컨텍스트 100만 토큰. ⭐ **프롬프트 길이에 따라 가격이 달라지는 유일한 모델** — 10만 토큰을 넘으면 다섯 배, 그래도 [[claude-sonnet-5-5|Sonnet 5.5]] 토큰 가격의 1/4.
- 기본 effort: API medium.
- 맞는 일: 분류 · 라우팅 · 대량 처리처럼 단순하고 양이 많은 일, 단순 대량 채팅, **큰 모델의 부수 작업을 맡는 서브에이전트**(파일 찾기 · 테스트 실행 · 로그 읽기 — 틀리면 금방 드러나는 일). Claude Code 내장 Explore 서브에이전트는 세션 모델을 따르므로 비용을 낮추려면 Haiku를 지정한 Explore를 직접 정의한다 → [[orchestrator-searcher-split]].
- 위험: 작은 모델이 검색 결과를 잘못 읽으면 메인 모델이 엉뚱한 파일을 열어 토큰을 낭비한다.
- 마이그레이션: Haiku 4.5 → 5.5는 budget tokens를 effort 수준으로 바꿔야 한다 → [[reasoning-effort-levels]].

## References

- [[tech-bridge-addy-osmani-which-claude-model]]
