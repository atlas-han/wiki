---
title: Dynamic Workflows
type: concept
category: pattern
tags: [agent, multi-agent, orchestration, parallel-agents, claude-code, long-running]
related: [agent-harness-design, generator-evaluator-pattern, managed-agents, ultracode, verifiable-goals, ralph-wiggum-method, context-resets-and-compaction]
first-seen: anthropic-dynamic-workflows
sources: [anthropic-dynamic-workflows]
created: 2026-05-30
updated: 2026-05-30
---

# Dynamic Workflows

[[claude-code|Claude Code]]가 하나의 prompt를 받아 **오케스트레이션 스크립트를 동적으로 작성**하고, 작업을 subtask로 쪼개 단일 세션에서 **수십~수백 개의 parallel subagent**로 fan-out한 뒤, 결과를 사용자에게 보여주기 전에 **자체 검증**하는 실행 형태. 단일 에이전트의 한 패스로는 너무 큰 문제 — 레거시 코드베이스 전역 버그 헌트, 수백 파일 마이그레이션, 다각도 stress-test — 를 end-to-end로 처리한다. [[anthropic|Anthropic]] 발표: [[anthropic-dynamic-workflows]] (2026-05-28, research preview).

> Work you'd normally plan in quarters now finishes in days.

## 작동 방식 (4단계 루프)

1. **동적 계획(plan dynamically)** — prompt를 기반으로 그 자리에서 계획 수립. 미리 정해진 고정 그래프가 아니라 task에 맞춰 생성.
2. **분할(break into subtasks) + fan-out** — subtask로 쪼개 parallel subagent에 분배.
3. **검증 후 fold-in** — 각 결과는 본 답에 합쳐지기 *전에* 검증됨.
4. **수렴(converge)** — agent들이 독립 각도로 공격하고, *다른 agent가 반박(refute)* 시도, 답이 수렴할 때까지 iterate.

> Agents address the problem from independent angles, other agents try to refute what they found, and the run keeps iterating until the answers converge—which is how a workflow reaches results a single pass can't.

이 **adversarial 수렴**이 dynamic workflows의 본질이자, "단일 패스가 도달 못 하는 결과"의 출처. [[generator-evaluator-pattern]](생성/평가 분리 + skeptical evaluator)을 *오케스트레이션 차원*으로 확장한 형태로 읽을 수 있다.

## 오케스트레이션 아키텍처

- **Coordination outside the conversation** — 조정 로직이 대화 컨텍스트 *바깥*에서 돌아, 작업이 아무리 커져도 plan이 흔들리지 않음. cf. [[managed-agents]]의 session-log 외부화([[context-resets-and-compaction]]) 사상과 동형.
- **Resumable (checkpoint)** — 진행상황이 run 도중 저장되어 중단된 job이 처음부터가 아니라 멈춘 지점에서 재개. long-running(시간~일 단위) 전제.
- **Parallel-first** — 단일 세션 안에서 10s~100s agent가 동시 실행. Bun 사례에선 *파일당 리뷰어 2명*까지 붙는 수백 agent 병렬.

## 활성화

| 방법 | 내용 |
|---|---|
| 직접 요청 | "Create a workflow" 등으로 Claude에게 명시적으로 지시 |
| [[ultracode]] 세팅 | effort menu의 새 Claude Code 세팅. effort를 **xhigh**로 올리고 *Claude가 workflow 사용 시점을 자동 판단* |

- **[[anthropic-claude-code-auto-mode|auto mode]] 권장** — 최선의 경험을 위해 켜둘 것.
- **최초 트리거 시 확인** — 무엇이 실행될지 보여주고 사용자 confirm을 받음.
- **Org admin 비활성화 가능** — managed settings.

## 가용성 (research preview, 2026-05)

- 클라이언트: Claude Code CLI · Desktop · VS Code 확장
- 플랜: Max / Team / Enterprise(admin enabled). Max·Team·API는 기본 on, Enterprise는 launch 시 기본 off
- 플랫폼: Claude API, Amazon Bedrock, Vertex AI, Microsoft Foundry

## 비용·한계

- 일반 Claude Code 세션보다 **토큰 소모가 현저히 큼** → **scoped task로 시작**해 사용량 감 잡기를 권장.
- Research preview 단계.

## 대표 use case

1. **Codebase-wide bug hunt / optimization audit / security audit** — 병렬 검색 + *모든 finding에 독립 검증* → 진짜 이슈만. auth 체크·input validation·unsafe 패턴 hardening 패스에도 동형 적용.
2. **Large migration / modernization** — framework swap, API deprecation, 수천 파일 언어 포팅. → [[bun|Bun]] Zig→Rust 사례.
3. **Critical work checked twice** — 독립 시도 + adversarial agent가 결과를 깨뜨리려 시도한 뒤 전달.

## Bun rewrite — 구체 workflow 사례

[[jarred-sumner|Jarred Sumner]]의 [[bun|Bun]] Zig→Rust 포팅 (99.8% 테스트 통과, ~75만 줄, 11일). 다단계 파이프라인:

1. **Lifetime mapping workflow** — Zig 코드베이스의 모든 struct field에 맞는 Rust lifetime을 매핑.
2. **Port workflow** — 각 `.zig` 파일을 behavior-identical `.rs`로, *파일당 리뷰어 2명*씩 수백 agent 병렬.
3. **Fix loop** — build·test suite가 둘 다 clean해질 때까지 구동.
4. **Overnight optimization** — 불필요한 data copy를 제거하고 각각 PR을 오픈해 최종 리뷰 대기.

## 관련 위키 맥락

- [[agent-harness-design]] — dynamic workflows는 *더 강한 모델이 더 야심찬 harness 조합을 가능케 한다*("the space moves")의 최신 사례. 단발 multi-agent를 넘어 **자기 작성 오케스트레이션**으로 진화.
- [[generator-evaluator-pattern]] — refute/converge가 evaluator 사상의 오케스트레이션판.
- [[ralph-wiggum-method]] — 사람이 짠 고정 루프 vs. Claude가 *동적으로 작성*하는 워크플로의 대비.
- [[verifiable-goals]] — build·test가 clean해질 때까지의 fix loop = 검증 가능한 goal로의 수렴.

## References

- [[anthropic-dynamic-workflows]]
- [공식 문서 — workflows](https://code.claude.com/docs/en/workflows)
- 관련: [[agent-harness-design]], [[generator-evaluator-pattern]], [[managed-agents]], [[ultracode]]
