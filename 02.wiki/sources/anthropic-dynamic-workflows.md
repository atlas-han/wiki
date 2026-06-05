---
title: "Anthropic — Introducing dynamic workflows in Claude Code"
type: source
tags: [claude-code, multi-agent, orchestration, parallel-agents, dynamic-workflows, ultracode]
source-url: https://claude.com/blog/introducing-dynamic-workflows-in-claude-code
source-type: article
author:
date-published: 2026-05-28
ingested: 2026-05-30
created: 2026-05-30
updated: 2026-05-30
---

# Anthropic — Introducing dynamic workflows in Claude Code

[[anthropic|Anthropic]]이 [[claude-code|Claude Code]]에 도입한 **dynamic workflows**(동적 워크플로) 발표 블로그. Claude가 **오케스트레이션 스크립트를 동적으로 작성**해 한 세션에서 수십~수백 개의 parallel subagent를 돌리고, 결과가 사용자에게 닿기 전에 자체 검증하는 기능. "분기(quarter) 단위로 계획하던 일이 며칠 만에 끝난다"가 핵심 주장.

> ⚠️ raw frontmatter의 `published: 2001-05-28`은 오타로 판단 (claude.com 블로그·research preview 맥락상 2026-05-28). 본 노트는 **2026-05-28**로 기록.

## 핵심 takeaways

1. **정의**. Dynamic workflow = Claude가 prompt를 받아 **동적으로 계획**하고, subtask로 쪼개, 단일 세션에서 **10s~100s parallel subagent**로 fan-out한 뒤, fold-in 전에 결과를 검증하는 실행 형태. 단일 패스로는 너무 큰 문제(레거시 코드베이스 전역 버그 헌트, 수백 파일 마이그레이션, 다각도 stress-test)를 end-to-end로 처리.
2. **검증·수렴 메커니즘** (이 기능의 본질). Agent들이 **독립된 각도**에서 문제를 공격하고, *다른 agent가 그 결과를 반박(refute)하려* 시도하며, **답이 수렴(converge)할 때까지 iterate**. "단일 패스가 도달 못 하는 결과에 이르는" 이유가 바로 이 adversarial 수렴. → [[generator-evaluator-pattern]]의 동일 사상.
3. **오케스트레이션 아키텍처**. 조정(coordination)이 **대화(conversation) 바깥**에서 일어나 작업이 아무리 커져도 plan이 흔들리지 않음. 진행상황이 run 도중 **저장(checkpoint)** 되어 중단돼도 **resume**(처음부터 다시 시작 안 함). 시간·일 단위 long-running 작업을 위해 설계.
4. **Bun rewrite 사례**. Jarred Sumner이 dynamic workflows로 [[bun|Bun]]을 **Zig → Rust** 포팅: 기존 테스트 **99.8% 통과**, 약 **75만 줄 Rust**, 첫 커밋부터 머지까지 **11일**. 다단계 workflow: ① Zig 코드베이스의 모든 struct field에 맞는 Rust lifetime 매핑 → ② 각 `.zig`의 동작-동일(behavior-identical) `.rs` 포팅, 파일당 리뷰어 2명씩 수백 agent 병렬 → ③ build·test가 clean해질 때까지 fix loop → ④ 야간(overnight) workflow가 불필요한 data copy 제거 후 각각 PR 오픈. (프로덕션 투입 전 단계.)
5. **활성화·운영**. 두 가지 진입: (a) 직접 "Create a workflow" 요청, (b) 새 Claude Code 세팅 **`ultracode`** — effort menu에서 켜며 effort를 **xhigh**로 올리고 Claude가 workflow 사용 시점을 자동 판단. **auto mode** 권장. **Research preview**: Claude Code CLI·Desktop·VS Code 확장 (Max/Team/Enterprise[admin enabled]) + Claude API + Amazon Bedrock·Vertex AI·Microsoft Foundry. 토큰 소모가 일반 세션보다 **현저히 큼** → scoped task로 시작 권장. 최초 트리거 시 무엇이 실행될지 보여주고 **확인**받음. Org admin은 managed settings로 비활성화 가능.

## 핵심 인용

> Claude dynamically writes orchestration scripts that run tens to hundreds of parallel subagents in a single session, checking its work before anything reaches you.

> Agents address the problem from independent angles, other agents try to refute what they found, and the run keeps iterating until the answers converge—which is how a workflow reaches results a single pass can't.

> Because the coordination happens outside the conversation, the plan stays on track no matter how big the task gets.

> Progress is saved as the run goes, so a job that's interrupted picks up where it left off instead of starting over.

> [Jarred Sumner] used dynamic workflows to port Bun from Zig to Rust with 99.8% of the existing test suite passing, roughly 750,000 lines of Rust, and eleven days from first commit to merge.

## 3대 use case (블로그 인용)

- **Codebase-wide bug hunts / profiler-guided optimization audits / security audits**: 서비스·repo를 병렬 검색 후 *모든 finding에 독립 검증*을 돌려 진짜 이슈만 리포트. 동일 형태가 hardening 패스(auth 체크, input validation, unsafe 패턴)에도 적용.
- **Large migrations / modernization**: framework swap, API deprecation, 수천 파일 규모 언어 포팅을 end-to-end.
- **두 번 확인이 필요한 critical work**: 오답 비용이 클 때, workflow가 Claude에게 **독립 시도**들을 주고 **adversarial agent**가 결과를 깨뜨리려 시도한 뒤 사용자에게 전달.

## 등장 개체·개념

- 조직: [[anthropic]]
- 제품: [[claude-code]] (dynamic workflows·`ultracode` 세팅 추가)
- 개념: [[dynamic-workflows]] (신규 허브), [[ultracode]], [[generator-evaluator-pattern]], [[agent-harness-design]]
- 인물: [[jarred-sumner]] (Bun 제작자)
- 도구: [[bun]] (Zig→Rust 포팅 대상)
- 플랫폼: Amazon Bedrock, Vertex AI, Microsoft Foundry, Claude API
- 관련 모드: [[anthropic-claude-code-auto-mode|auto mode]] (권장 전제)

## References

- [원문](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code)
- [공식 문서 — workflows](https://code.claude.com/docs/en/workflows)
- [Claude Code settings](https://code.claude.com/docs/en/settings)
- 관련 연작: [[anthropic-harness-design-long-running-apps]], [[anthropic-managed-agents]], [[anthropic-claude-code-auto-mode]]
