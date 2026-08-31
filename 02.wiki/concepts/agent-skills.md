---
title: Agent Skills
type: concept
category: pattern
tags: [skills, harness, governance, mcp, workflow]
related: [harness-engineering, spec-driven-development, frontier-engineering, agent-org-adoption, model-context-protocol, self-harness, prompt-injection]
first-seen: tech-bridge-ai-native-skills
sources: [tech-bridge-ai-native-skills]
created: 2026-08-31
updated: 2026-08-31
---

# Agent Skills

조직 know-how를 에이전트가 실행 가능한 단위로 묶은 것. [[imad-touil|Imad Touil]]([[tech-bridge-ai-native-skills]])이 hooks / [[model-context-protocol|MCP]] / sub-agents와 구분해 first-class로 둔다. [[harness-engineering]] AI Layer의 "Skills & MCP" 칸을 **조직·거버넌스 면**으로 확장한 페이지.

> AI-native organizations run on skills — and ungoverned skills become a new class of technical debt.

## 스택에서의 자리

| 루프 | 역할 |
|---|---|
| **Inner harness** | coding agent: context · tools/MCP · memory · **skills loader** |
| **Outer workflows** | skills · sub-agents · MCP · hooks — Touil은 워크플로를 "harness blueprints"라고 부름 |

Hooks는 이벤트 트리거, MCP는 대개 **제공 도구를 소비**, sub-agent는 컨텍스트 위임. **구조화된 가치가 모이는 곳은 skills.**

## 설계 원칙 (마이크로서비스 유추)

Reusable · discoverable · portable across harnesses(Claude Code 스킬이 Cursor에서도) · specialized(모놀리스 금지) · composable · deterministic · cost efficient.

비용 축은 **progressive disclosure**: 맞는 스킬을 맞는 양·타이밍에 넣어 토큰을 줄인다.

## 거버넌스

거버넌스 없으면 부채: 중복, 품질(최신 모델 대비 미검증), 발견 불가, 오너 없음, 조합 충돌, [[prompt-injection]]/스킬 내 스크립트, ACL 부재.

처방: 개인 → 팀 → 중앙 플랫폼(catalog+metadata, MCP/CLI, 의존성, 버전, eval, ACL) + 도메인 오너. 다음 단계는 registry/IDP, static eval, auto-evolve — 가드레일 없이 돌리면 부채를 증폭([[self-harness]]와 맞닿되 조직 전제가 다름).

15팀×6개월은 **시뮬레이션**. 현장 A/B가 아님.

## 위키 자매

- [[frontier-engineering]]: 개인 steering/skills 습관. 여기는 그 파일을 **전사 카탈로그**로 올리는 면.
- [[spec-driven-development]]: spec–plan–task는 product increment 한 칸. 스킬 거버넌스는 그 앞뒤 SDLC까지.
- [[agent-org-adoption]]: 도구가 같아도 방식·가시성이 가른다.

## References

- [[tech-bridge-ai-native-skills]] · [[imad-touil]] · [[harness-engineering]] · [[tech-bridge-frontier-engineering]]
