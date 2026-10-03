---
title: Bun
type: entity
category: tool
tags: [javascript, runtime, toolkit, rust, zig]
aliases: [번]
sources: [anthropic-dynamic-workflows, tech-bridge-death-of-code-review]
links:
  - https://bun.sh
  - https://github.com/oven-sh/bun
created: 2026-05-30
updated: 2026-10-03
---

# Bun

JavaScript/TypeScript 런타임·툴킷. [[jarred-sumner|Jarred Sumner]]이 제작. 본 위키에는 [[claude-code|Claude Code]]의 [[dynamic-workflows|dynamic workflows]] 스케일 사례로 처음 등장 ([[anthropic-dynamic-workflows]]).

## 위키에서 알려진 사실

- 기존 구현이 **Zig**로 작성되어 있었고, [[dynamic-workflows]]를 통해 **Rust로 재작성(port)** 됨:
  - 기존 테스트 suite **99.8% 통과**
  - 약 **75만 줄(750,000 lines)** Rust
  - 첫 커밋 → 머지까지 **11일**
  - 아직 프로덕션 투입 전
- 포팅은 다단계 workflow로 진행 — lifetime 매핑 → 파일별 behavior-identical 포팅(파일당 리뷰어 2명) → fix loop → 야간 최적화 PR. 상세는 [[dynamic-workflows#Bun rewrite — 구체 workflow 사례]] 참조.

## 미해결 사항

- Bun 자체의 기능·포지셔닝(Node.js 대비), Oven 사·생태계 — 별도 소스 ingest 필요
- Zig→Rust 전환의 동기·결과 (Jarred의 후속 글 예정)

## References

- [[anthropic-dynamic-workflows]]
- [bun.sh](https://bun.sh)

## 테스트가 보지 못한 것 — unsafe 블록 13,044개 (2026-10-03 · [[tech-bridge-death-of-code-review]])

[[laurie-voss|Laurie Voss]]가 Zig → Rust 포팅을 **사람 없는 리뷰의 한계 사례**로 든다. 화자 진술(2차 인용):

- Bun은 *"now part of Anthropic"*(02:44~02:46). 게이트는 기존 테스트 스위트, *"99.8% of the test suite passed"*(15:59~16:04) — 위 수치와 같다.
- Zig 코드를 전부 지운 마지막 PR을 *"another robot"* 이 *"this is AI slop"* 으로 플래그(16:09~16:22).
- ⭐ 포팅된 코드에 **unsafe 블록 13,044개**, 비슷한 크기의 사람 Rust 코드는 **약 74개**(16:29~16:46). *"the test suite can certify behavior at the public interface. um it cannot certify 13,000 assertions that the test suite was never designed to look for"*(16:55~17:04). 분석자는 *"Somebody"* — 미발화. ⚠️ 화자는 *"three orders of magnitude"* 라 했으나 13,044/74 ≈ 176배.

> ⚠️ **Contradiction: 규모·기간.** 위 [[anthropic-dynamic-workflows]] 기준은 **Rust 약 75만 줄, 첫 커밋 → 머지 11일**. Voss는 *"over a million lines of Zigg uh to Rust in six days"*(02:46~02:51), *"about a million lines of code by agents in six days"*(15:52~15:56). 줄 수의 기준(Zig 원본 vs Rust 결과)과 기간의 기준(에이전트 작업 vs 머지까지)이 다를 수 있다 — **미확정.**

→ [[mergeability-gap]] · [[syntactically-correct-behaviorally-wrong]]
