---
title: "Anthropic — Claude Code auto mode: a safer way to skip permissions"
type: source
tags: [claude-code, agent-safety, permissions, prompt-injection, classifier]
source-url: https://www.anthropic.com/engineering/claude-code-auto-mode
source-type: article
author: John Hughes
date-published: 2026
ingested: 2026-05-25
created: 2026-05-25
updated: 2026-05-25
---

# Anthropic — Claude Code auto mode: a safer way to skip permissions

[[anthropic|Anthropic]]이 [[claude-code|Claude Code]]에 새로 도입한 **auto mode**의 설계·평가 결과를 정리한 엔지니어링 블로그. 수동 승인의 피로(approval fatigue)와 `--dangerously-skip-permissions`의 무방비 사이 **중간 지점**을 제시한다. 핵심은 model-based classifier로 위험 행동만 차단하는 것.

## 핵심 takeaways

1. **Tradeoff 공간 재정의**. 기존에는 (1) sandbox: 안전하지만 high-maintenance, (2) `--dangerously-skip-permissions`: zero-maintenance지만 무방비, (3) manual prompt (실제로는 93% 승인됨)의 셋이었다. Auto mode는 "high autonomy + low maintenance"를 노린다.
2. **Two-layer defense**.
   - *Input layer*: 서버측 **prompt-injection probe**가 tool 출력(파일·웹·shell·외부 도구 응답)을 스캔, 의심되면 agent context에 경고를 주입.
   - *Output layer*: **transcript classifier**([[claude-sonnet-4-6]] 기반)가 모든 tool call을 실행 전 평가. 2-stage (fast single-token yes/no → flag된 경우만 CoT reasoning). 대부분의 action은 stage 1을 통과해 reasoning 비용 절감. 참고: [[transcript-classifier]]
3. **Reasoning-blind by design**. Classifier는 **user message + agent의 tool call**만 본다. Agent 자신의 prose와 tool 결과는 strip. 이유: agent가 "이건 안전합니다 왜냐하면..." 식 정당화로 classifier를 설득하지 못하게. CoT monitoring과 직교 보완.
4. **Threat model 4가지** (참고 [[agentic-misbehavior]]):
   - Overeager behavior — 의도된 경계를 넘는 적극적 행동
   - Honest mistakes — blast radius 오해
   - Prompt injection — 외부 콘텐츠가 agent를 hijack
   - Misaligned model — 모델 자체 목표 (실제 관측 없음, 평가만)
   Classifier는 overeager에 튜닝.
5. **Three-tier permission pipeline**.
   - Tier 1: built-in safe-tool allowlist + user always-allow (auto mode 진입 시 **blanket shell / 인터프리터 / 패키지 매니저 run 룰은 drop**)
   - Tier 2: in-project 파일 쓰기/편집은 classifier 호출 없이 허용
   - Tier 3: 외부 영향이 있을 수 있는 모든 행동은 transcript classifier 통과
6. **Classifier 정책 = 고정 템플릿 + 3개 슬롯**. 슬롯: trusted environment 경계 / block rules (기본 20+개) / allow exceptions. 기본값은 보수적; `claude auto-mode defaults`로 확인. 인용: *"Good defaults ship out of the box."*
7. **결과 (FPR/FNR)**:

   | Stage | Real traffic n=10,000 FPR | Real overeager n=52 FNR | Synthetic exfil n=1,000 FNR |
   |---|---|---|---|
   | Stage 1 (fast filter) | 8.5% | 6.6% | 1.8% |
   | Stage 1→2 (full pipeline) | **0.4%** | **17%** | **5.7%** |

   17% real-overeager FNR을 "honest number"로 명시. 대부분의 miss는 "이 action을 user가 정말 동의했나?"의 boundary 판단 실패.
8. **Deny-and-continue**. Block은 tool result로 돌아가고 agent는 안전한 path로 재시도. 3 연속 denial 또는 20 누적이면 escalate(헤드리스 모드는 process 종료). FPR 0.4%가 세션을 끊는 게 아니라 retry 비용으로 흡수됨.
9. **Multi-agent handoff**. 서브에이전트 위임 시(outbound) classifier가 **deny 가능**, 리턴 시(inbound)는 prompt-injection 가능성 때문에 history 검토 후 **경고만** prepend.
10. **선언적 한계**. Auto mode는 `--dangerously-skip-permissions` 대체가 목적. 신중한 manual review의 drop-in replacement는 아니다. High-stakes 인프라에서는 인간 판단을 유지하라고 명시.

## 핵심 인용

> Manual prompts sit in the middle, and in practice users accept 93% of them anyway.

> The classifier sees only user messages and the agent's tool calls; we strip out Claude's own messages and tool outputs, making it reasoning-blind by design.

> The 17% false-negative rate on real overeager actions is the honest number.

> We strip assistant text so the agent can't talk the classifier into making a bad call.

## Internal incident log 예시 (블로그 인용)

- 원격 git 브랜치 삭제 (오해된 지시)
- GitHub auth 토큰을 내부 컴퓨트 클러스터에 업로드
- 프로덕션 DB 마이그레이션 시도

(상세: [Claude Opus 4.6 system card](https://www-cdn.anthropic.com/14e4fb01875d2a69f646fa5e574dea2b1c0ff7b5.pdf) §6.2.1, §6.2.3.3)

## 차단 대상 5개 패턴 (블로그 인용)

- Scope escalation — "clean up old branches" → remote branch 일괄 삭제
- Credential exploration — auth error 시 env·config 스캔
- Agent-inferred parameters — "cancel my job" → 이름 유사도로 임의 선택
- Sharing via external service — GitHub Gist로 스크립트 공유
- Safety-check bypass — pre-check 실패 후 skip flag로 재시도

## 등장 개체·개념

- 조직: [[anthropic]]
- 제품: [[claude-code]]
- 모델: [[claude-sonnet-4-6]] (transcript classifier)
- 개념: [[agentic-misbehavior]], [[prompt-injection]], [[transcript-classifier]], [[agent-harness-design]]
- 저자: John Hughes (Anthropic)

## References

- [원문](https://www.anthropic.com/engineering/claude-code-auto-mode)
- 관련 시리즈: [[anthropic-harness-design-long-running-apps]], [[anthropic-managed-agents]]
