---
title: Bun
type: entity
category: tool
tags: [javascript, runtime, toolkit, rust, zig]
aliases: [번]
sources: [anthropic-dynamic-workflows]
links:
  - https://bun.sh
  - https://github.com/oven-sh/bun
created: 2026-05-30
updated: 2026-05-30
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
