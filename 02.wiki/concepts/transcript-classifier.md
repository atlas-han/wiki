---
title: Transcript Classifier
type: concept
category: pattern
tags: [agent-safety, classifier, claude-code, llm-as-judge]
related: [agentic-misbehavior, prompt-injection, agent-harness-design, deny-and-continue]
first-seen: anthropic-claude-code-auto-mode
sources: [anthropic-claude-code-auto-mode]
created: 2026-05-25
updated: 2026-05-25
---

# Transcript Classifier

에이전트의 모든 tool call을 **실행 전**에 검사해 위험 행동을 차단하는 LLM 기반 분류기. [[anthropic-claude-code-auto-mode|Claude Code auto mode]]의 핵심 컴포넌트. [[claude-sonnet-4-6]] 백본.

## 입력 — Reasoning-blind by design

Classifier가 보는 것:
- ✅ User message
- ✅ Agent의 tool call (executable payload)

Strip되는 것:
- ❌ Agent의 prose (assistant text)
- ❌ Tool 결과 (tool output)

**왜?**
1. Agent가 *"이건 안전합니다 왜냐하면..."* 식 정당화로 classifier를 talking-into 못 하게.
2. Tool 결과를 안 보면 prompt injection을 **구조적으로** 회피 — classifier는 hijack 가능한 컨텐츠를 통과한 후의 행동만 본다.

대가: provenance를 모름. 사용자가 명시 안 한 `job abc123`을 agent가 query로 얻었는지 fabricate했는지 구분 불가. 이 비용을 감수하고 injection robustness를 택함.

> A POST of env vars to an external URL fails against user intent regardless of what prompted it.

CoT(chain-of-thought) monitoring과 **직교 보완** 관계: action-level block은 추론을 숨기는 모델을 잡고, CoT 모니터링은 추론이 드러내는 의도를 잡는다.

## 2-Stage 구조

| Stage | 출력 | 튜닝 |
|---|---|---|
| **Stage 1** (fast filter) | 단일 토큰 yes/no | "err on blocking" — 높은 recall, 8.5% FPR 감수 |
| **Stage 2** (CoT) | 추론 후 결정 | Reasoning으로 FPR 0.4%까지 정제, FNR 조금 양보 |

Stage 2는 stage 1과 거의 동일한 prompt를 받으므로 **prompt cache hit**가 거의 100% — 비용 효율.

## 평가 결과 (auto mode 풀 파이프라인)

| 데이터셋 | 메트릭 | 결과 |
|---|---|---|
| Real internal traffic (n=10,000) | FPR | **0.4%** |
| Real overeager actions (n=52) | FNR | **17%** ("the honest number") |
| Synthetic data exfiltration (n=1,000) | FNR | 5.7% |

17% miss의 대다수는 *위험을 정확히 식별하지만 사용자가 정말 동의했는지의 boundary 판단*에서 실패. "Clean up the PR"이 force-push까지 cover하는가? 한 번 승인된 비슷한 action이 패턴인가? — prompt engineering으로 풀리지 않는 문제.

## 정책 슬롯 (고정 템플릿 + 3 슬롯)

- **Environment** — 신뢰 경계 (도메인, 클라우드 버킷, source-control org, 내부 서비스)
- **Block rules** — 기본 20+개: destroy/exfiltrate, degrade security posture, cross trust boundaries, bypass review or affect others
- **Allow exceptions** — 좁게: manifest 선언된 패키지 설치, 표준 credential flow, 세션의 working branch에 push

`claude auto-mode defaults`로 확인.

## 통합 위치

- Tier 1 (allowlist) / Tier 2 (in-project 파일 작업) 후의 **Tier 3** — 외부 영향이 있을 수 있는 모든 행동
- Subagent handoff outbound: deny 가능
- Subagent handoff inbound: history 검토 후 **경고만** prepend (결과 폐기 안 함)
- Block 시 [[deny-and-continue]] — session을 끊지 않고 agent에게 안전한 path를 권유

## References

- [[anthropic-claude-code-auto-mode]]
