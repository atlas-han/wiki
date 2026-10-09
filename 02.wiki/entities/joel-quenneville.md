---
title: Joël Quenneville
type: entity
category: person
tags: [rails, ruby, harness-engineering, rubocop, agent-skills]
aliases: [Joël Quenneville, Joel Quenneville, JoelQ]
links: []
sources: [tech-bridge-rails-harness-engineering]
created: 2026-10-09
updated: 2026-10-09
---

# Joël Quenneville

Ruby/Rails 개발자. [[tech-bridge-rails-harness-engineering]]에서 **자기 Rails 코드베이스의 하네스 엔지니어링 실천**을 발표했다 — 판단을 AGENTS.md에서 RuboCop·제너레이터·훅·좁은 리뷰 스킬로 옮겨 AI 산출물의 *바닥을 올린다(raise the floor)*. 본 위키 첫 등장.

> ⚠️ **이름·소속 표기.** 이름은 **영상 제목에만** 있다 — 영상이 문장 중간에서 시작해 자기소개 구간이 없다. 자막 속 유일한 자기 지칭은 retro 스킬 위치 *"This is up on my GitHub (…) Uh JoelQskills"*(29:29~29:33). **소속은 발화되지 않는다.** 설명란 링크 shopify.engineering은 본문과 연결이 없어 **소속 근거로 쓰지 않는다.**

## 발표에서 (자막 근거)

- 출발 일화 — 2일짜리 기능을 1시간에 생성, 다듬기에 이틀(00:00~01:54) → [[ai-slop]] · [[verification-bottleneck]]
- 에이전트 = 하네스 + 루프, *"a brain in a jar"*(04:14~04:17), 사람이 결과를 손으로 나르는 [[human-plumbing]]에서 빠져나와라
- AGENTS.md는 스타일 가이드 자리가 아니다 → RuboCop(지시 한 줄 → Stop 훅), 커스텀 cop, 마이그레이션은 제너레이터 + 쓰기 차단 훅 + 거부 사유 → [[hard-vs-soft-enforcement]] · [[hook-enforced-workflow]] · [[deny-and-continue]]
- 결정론으로 못 잡는 휴리스틱은 **좁은 리뷰 스킬 3종**(구조·메서드·폴리시)을 서브에이전트로, 생성 *뒤에* 적용 → [[automated-code-review]]
- Birgitta Böckeler의 2×2로 정리, AGENTS.md는 *"a very thin almost routing layer"*(21:39~21:43) → [[feedforward-feedback-steering]]
- Goodhart 경고, 도메인 전용 스크립트(새는 깔때기 분류) → [[domain-specific-scripts]]
- retro 스킬 — *"how could this be the last time?"*(28:20~28:26) → [[skill-self-improvement]]

## 태도

**측정이 아니라 실천을 말한다.** 수치는 *"maybe 90%"*(14:07~14:10), *"2 minutes"*(12:27~12:30), *"about 5%"*(24:13~24:17) 정도이고 전부 자기 경험이다. 자기 처방에도 단서를 단다 — 훅 코드는 *"the exact code on this slide doesn't really matter so much as the idea"*(11:11~11:14), 서브에이전트 스킬은 *"This is not real orchestration"*(18:20), 그리고 너무 조이면 에이전트가 해킹한다(23:19~23:23). 판매하는 제품은 없다(retro 스킬은 공개 저장소).

## References

- [[tech-bridge-rails-harness-engineering]]
- 자막상 GitHub: *"JoelQskills"* (⚠️ 저장소 경로 미확정, 열어 보지 않았다)
