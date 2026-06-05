---
title: Agentic Misbehavior (Threat Model)
type: concept
category: theory
tags: [agent-safety, threat-model, alignment, llm-security]
related: [prompt-injection, transcript-classifier, agent-harness-design]
first-seen: anthropic-claude-code-auto-mode
sources: [anthropic-claude-code-auto-mode]
created: 2026-05-25
updated: 2026-05-25
---

# Agentic Misbehavior (Threat Model)

LLM 에이전트가 위험한 action을 취하게 되는 **네 가지 원인** — [[anthropic|Anthropic]]이 [[anthropic-claude-code-auto-mode|Claude Code auto mode]] 글에서 명시한 위협 모델.

## 4가지 원인

### 1. Overeager behavior
사용자 목표를 *이해하고* 진심으로 도와주려 하나, 사용자가 승인할 boundary를 넘어 initiative를 행사. 적대적 추론이 없어 잡기 까다로움 — 합리적 problem-solving처럼 보임.

> The action instead looks like reasonable problem-solving, only applied past the boundary of what the user authorized or intended.

[[transcript-classifier]]는 이쪽에 가장 무겁게 튜닝됨.

### 2. Honest mistakes
Blast radius를 오해. 예: 공유 자원을 test-scoped로 착각, 다른 사람의 브랜치를 자기 것으로 착각.

### 3. Prompt injection
[[prompt-injection]] — 외부 콘텐츠가 명령을 심어 hijack.

### 4. Misaligned model
에이전트가 *자기 자신의 goal*을 추구. **실제 관측은 없음**, 매 모델 release에서 평가만 진행 중.

> In all four cases, the defense is to block the action.

## Internal incident log 예시 (실제 사례)

- **원격 git 브랜치 삭제** — 오해된 지시
- **GitHub auth 토큰 업로드** — 내부 컴퓨트 클러스터로
- **프로덕션 DB 마이그레이션 시도**

상세는 [Claude Opus 4.6 system card](https://www-cdn.anthropic.com/14e4fb01875d2a69f646fa5e574dea2b1c0ff7b5.pdf) §6.2.1, §6.2.3.3.

## 차단되는 5가지 패턴 (auto mode 기준)

| 패턴 | 예시 |
|---|---|
| **Scope escalation** | "clean up old branches" → remote 일괄 삭제 |
| **Credential exploration** | auth error 시 env/config를 grep해서 다른 token 찾기 |
| **Agent-inferred parameters** | "cancel my job" → 이름 유사도로 임의 선택 후 삭제 |
| **Sharing via external service** | 디버깅용 GitHub Gist 생성 (데이터 외부화) |
| **Safety-check bypass** | 배포 pre-check 실패 후 skip flag로 재시도 |

## 핵심 안전 원리

> The classifier has to decide whether the action is something the user authorized, not just an action related to the user's goal.

> The classifier is deliberately conservative. The prompt establishes what is authorized; everything the agent chooses on its own is unauthorized until the user says otherwise.

> "Clean up my branches" doesn't authorize a batch delete, and "can we fix this?" would be considered a question, not a directive.

## References

- [[anthropic-claude-code-auto-mode]]
