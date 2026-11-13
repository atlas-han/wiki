---
title: Claude Sonnet 5.5
type: entity
category: model
tags: [anthropic, claude, sonnet, llm, pricing]
aliases: [Sonnet 5.5, 소넷 5.5, claude-sonnet-5-5]
links:
  - https://platform.claude.com/docs/en/about-claude/models/choosing-a-model
sources: [tech-bridge-addy-osmani-which-claude-model]
created: 2026-11-13
updated: 2026-11-13
---

# Claude Sonnet 5.5

[[anthropic|Anthropic]]의 중간 등급 Claude 모델. [[addy-osmani|Addy Osmani]]의 모델 선택 가이드를 해설한 [[tech-bridge-addy-osmani-which-claude-model]]에서 처음 위키에 들어왔다. [[claude-sonnet-4-6|Sonnet 4.6]]의 후속 계열로 보인다(⚠️ 계보는 위키의 추정 — 해설은 *소넷 5* 와의 속도 비교만 말한다).

> ⚠️ **해설 전달의 수치다.** 위키는 원 블로그 · 공식 문서를 열지 않았다. 발표일은 미상.

## 위키에서 알려진 것 (해설 기준)

- 가격: 입력 $2 · 출력 $10 / 100만 토큰 — [[claude-opus-5-5|Opus 5.5]]의 절반. 컨텍스트 100만 토큰.
- 기본 effort: API high, [[claude-code|Claude Code]]에서는 medium으로 시작.
- 맞는 일: 버그 수정 · 스펙이 분명한 기능처럼 **범위가 정해진 일**, 채팅 · 대화형 세션(low/medium), 반복 실행하는 조사 · 리뷰 · 초안 에이전트(medium), 문서 · 슬라이드. 사람이 응답을 기다리는 경우의 기본.
- 속도: Sonnet 5보다 30% 빠르다.
- 혼합: 약 2,200만 토큰 결함 탐색에서 Opus 5.5 지휘 + **Sonnet 5.5 워커** 가 Opus 단독보다 약 1/3 저렴, 성능 거의 같음 → [[model-mixing-economics]]. 서브에이전트 모델로도 지정한다.
- 호환성: 도구 사용 강제 설정이 400 오류를 낸다(Opus 5.5 · Fable 5.2와 같음).

## References

- [[tech-bridge-addy-osmani-which-claude-model]]
