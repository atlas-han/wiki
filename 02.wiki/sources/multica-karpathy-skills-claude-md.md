---
title: "multica-ai — andrej-karpathy-skills · CLAUDE.md"
type: source
tags: [pattern, llm-coding, claude-code, system-prompt]
source-url: https://github.com/multica-ai/andrej-karpathy-skills/blob/main/CLAUDE.md
source-type: docs
author: multica-ai (org), Karpathy-inspired
date-published: 2026
ingested: 2026-05-25
created: 2026-05-25
updated: 2026-05-25
---

# multica-ai — andrej-karpathy-skills · CLAUDE.md

[[multica-ai]] 조직이 GitHub에 공개한 `andrej-karpathy-skills` repo의 **CLAUDE.md** 헤더. LLM 코딩 어시스턴트(특히 [[claude-code]] 류)의 흔한 실수를 줄이기 위한 **행동 가이드라인 4원칙**을 제시. *"caution-biased"* 트레이드오프를 명시하며 trivial task에는 judgment 적용을 허용.

## 핵심 takeaways

1. **Think Before Coding** — 가정을 표면화하라. 불확실하면 멈춰서 질문, 다중 해석은 침묵 선택 금지, 더 단순한 대안이 있으면 push back. *"Don't hide confusion"* 이 핵심 동사.
2. **Simplicity First** — 요청된 최소 코드만. 미요청 feature·추상화·flexibility·불가능 시나리오 error handling 전부 금지. *"200줄이 50줄로 가능하면 다시 써라"*.
3. **Surgical Changes** — 외과 수술적 수정 ([[surgical-edits]]). 인접 코드·주석·포맷 손대지 말 것. 깨지지 않은 것 리팩토링 금지. 기존 스타일 일치. *변경으로 인해* 발생한 orphan만 정리, 기존 dead code는 언급만.
4. **Goal-Driven Execution** — 검증 가능한 목표 ([[verifiable-goals]]). 모호한 task → 검증 가능한 goal로 변환. 멀티스텝은 `step → verify` 형식 plan 명시. 강한 success criteria가 independent loop를 가능케 함.
5. **메타 — Tradeoff 명시**: caution > speed bias. 효과 측정은 diff 내 불필요한 변경 감소, overcomplication 재작성 감소, 사후 수정보다 사전 질문 비중 증가로.

## 인용

> Don't assume. Don't hide confusion. Surface tradeoffs.

> Minimum code that solves the problem. Nothing speculative.

> Touch only what you must. Clean up only your own mess.

> The test: Every changed line should trace directly to the user's request.

> Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.

> These guidelines are working if: fewer unnecessary changes in diffs, fewer rewrites due to overcomplication, and clarifying questions come before implementation rather than after mistakes.

## 등장 개체·개념

- 조직: [[multica-ai]] (GitHub org 운영자)
- 인물: [[andrej-karpathy]] (repo 이름이 직접 참조 — Karpathy의 *skills* 컨셉)
- 도구: [[claude-code]] (이 가이드라인의 1차 대상), `CLAUDE.md` (Claude Code의 prompt convention)
- 개념: [[llm-coding-guidelines]] (이 글이 제시하는 패턴 자체), [[surgical-edits]], [[verifiable-goals]]
- 관련 패턴: [[sprint-contract]] ([[verifiable-goals|verifiable goals]]와 같은 사상의 multi-agent 변형), [[ralph-wiggum-method]] (loop 패턴), [[context-engineering]]

## 위치 — 위키 내 좌표

> Karpathy의 [[llm-wiki-pattern]]이 *"LLM이 위키 자체를 만들고 유지하는 패턴"* 이라면, 이 글은 *"LLM이 코드를 만들고 유지할 때의 행동 규약"*. 둘 다 LLM의 운영을 규정하는 **메타 layer**.

같은 vault의 [[anthropic-claude-code-auto-mode|auto mode]]가 *권한 게이트*로 위험 행동을 차단한다면, 이 글은 *system prompt*로 **선의의 과잉 행동**(over-engineering, scope creep, refactor drift)을 줄이는 방향. 보완 관계.

## 비고

- 원문에는 license·세부 author 정보 없음 — repo 메타데이터에 의존
- repo 이름 `andrej-karpathy-skills`가 Karpathy의 *skills* 운영 컨셉에 영향받음을 시사 (직접 인용은 없음)
- 글이 짧고 prescriptive — 그 자체가 본 가이드라인의 **Simplicity First** 원칙을 따름

## References

- [원문 GitHub](https://github.com/multica-ai/andrej-karpathy-skills/blob/main/CLAUDE.md)
- raw 캡처: `01.raw/articles/2026-05-25_claude-md-behavioral-guidelines.md`
