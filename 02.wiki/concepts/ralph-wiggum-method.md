---
title: Ralph Wiggum Method
type: concept
category: pattern
tags: [agent, coding-agent, loop, claude-code, autonomous]
aliases: [Ralph, Ralph loop]
related: [agent-harness-design, harness-engineering, generator-evaluator-pattern, verifiable-goals, llm-coding-guidelines, geoff-huntley, archon]
first-seen: anthropic-harness-design-long-running-apps
sources: [anthropic-harness-design-long-running-apps, tech-bridge-harness-engineering]
created: 2026-05-25
updated: 2026-06-03
---

# Ralph Wiggum Method

[[geoff-huntley|Geoff Huntley]](ghuntley.com)가 명명·정리한 **AI coding agent의 자율 루프 패턴**. 단순 shell 루프로 [[claude-code|Claude Code]] 같은 에이전트를 마크다운 prompt와 함께 반복 실행해 최소 개입으로 소프트웨어를 빌드한다. [[anthropic-harness-design-long-running-apps]]에서 "[[agent-harness-design|harness]] 커뮤니티가 수렴한 인사이트"의 대표로 인용.

## 핵심 루프

```bash
while :; do cat PROMPT.md | claude-code ; done
```

이 무한 루프가 PROMPT.md를 매번 agent에 먹이면서 feature 빌드·테스트·이슈 해결을 자율적으로 반복.

## 왜 "Ralph Wiggum"인가

심슨 가족의 캐릭터에서. Huntley의 설명:

> The technique is deterministically bad in an undeterministic world.

Ralph처럼 *예측 불가능한 결과*를 내지만 어쨌든 작동한다. 실패를 거부할 게 아니라 **튜닝 신호**로 받아들이는 철학.

## 핵심 인프라 파일

| 파일 | 역할 |
|---|---|
| `@PROMPT.md` | 매 루프 iteration의 지시문. 관찰을 통해 진화 |
| `@fix_plan.md` | Ralph가 자율로 갱신하는 우선순위 todo. 자주 지우고 다시 만들어 방향 redirect |
| `@AGENT.md` | 빌드/테스트 명령, 발견된 최적화를 Ralph가 기록·재학습 |
| `@specs/*` | 컴포넌트별 명세, 코드 생성 패턴 제약 |
| `@stdlib/*` | 표준 라이브러리 구현 (가급적 타겟 언어로) |

## 추천 환경

- 타이트한 빌드/테스트 피드백 루프
- 동적 타입 언어용 타입 체커 (Dialyzer, Pyre)
- 구현 전 요구사항 명세
- *왜* 그 테스트가 중요한지 설명 코멘트 포함된 테스트 스위트
- **한 루프에 한 작업** (critical constraint)
- expensive 작업은 subagent로 병렬화

## 구체적 가이드

- **프롬프트**: *"no such thing as a perfect prompt."* 효과적 프롬프트는 관찰된 실패 기반의 반복 튜닝으로 진화. Huntley의 CURSED 프롬프트를 공유하면서도 "복사 붙여넣기가 아니라 운영자 기량이 결과를 결정"이라 경고.
- **컨텍스트 윈도우**: 핵심 컨텍스트를 lean하게 유지. expensive 작업(요약 등)은 subagent에. ~170k 토큰 사용, 품질 저하는 147–152k 부근.
- **검증**: "make the wheel turn fast" — 정확성(타입·테스트) vs 반복 속도 균형. Rust는 강한 타입 but 느린 컴파일.
- **결정적 지시**: *"Before making changes search codebase (don't assume not implemented)"* — 중복 구현 방지.

## 한계

- 시니어 엔지니어의 판단이 필수 — *"engineers are still needed"*
- Greenfield 프로젝트에서 90% 완성도, 레거시에는 효과적이지 않음
- 철학: *"any problem created by AI can be resolved through a different series of prompts."*

## "Ralph Loop" 프레이밍 ([[harness-engineering]] 시각)

[[tech-bridge-harness-engineering]] 영상은 이 패턴을 **Ralph Loop**라 부르며 [[harness-engineering|harness engineering]]의 *최종 진화*(다중 세션 오케스트레이션 자동화)로 위치시킨다:

- 큰 작업(대규모 PRD)을 받아 **세부 태스크로 자동 분할**, 한 번에 하나씩 처리.
- 완료 조건(영상 예시: `done` 표식 파일 생성)이 충족될 때까지 while 루프 반복. *유일한 종료 조건*이 그 표식.
- PIV(Plan→Implement→Validate) 핸드오프 + 병렬 리뷰 에이전트(보안·정확성·단순성) → PR 생성까지 **인간 베이비시팅 없이** 자동화.
- [[archon|Archon]](발표자의 오픈소스 하네스 빌더)이 이런 Ralph Loop류를 사용자 SDLC에 맞춰 커스텀 구축하는 도구로 소개됨.

> ⚠️ 영상은 제작자를 "Jeffrey Huntley"로 표기 — 본 위키는 [[geoff-huntley|Geoff Huntley]]로 통일(동일 인물).

## 본 위키 내 비교

- [[anthropic-harness-design-long-running-apps]]의 generator/evaluator 다중 에이전트는 Ralph의 **명시적 evaluator + sprint contract** 변형. Ralph가 단일 루프 + 운영자 관찰이라면, Anthropic 접근은 evaluator를 분리·자동화.
- [[dynamic-workflows]]는 사람이 *고정* Ralph 스크립트를 짜는 것과 달리 Claude가 오케스트레이션을 *동적 작성* — 자동화의 다음 단계.
- 세 접근 다 [[agent-harness-design]]의 일반 원리 — "모델이 못하는 것을 인코딩하는 scaffold" — 의 다른 응용.

## References

- [[anthropic-harness-design-long-running-apps]]
- [원문 ghuntley.com/ralph/](https://ghuntley.com/ralph/)
